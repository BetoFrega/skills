#!/usr/bin/env node
// Adds click and keystroke sounds and the recorder's zooms to a demo recording and writes an MP4.
// Usage: node finish-recording.mjs <video.webm|mp4> <events.json> <out.mp4> [--no-trim] [--offset=<seconds>] [--fade=<seconds>] [--silent]
// events.json comes from recorder.saveEvents(). When it holds a sync event (rec.syncFlash()),
// the script finds the magenta flash in the video, aligns every sound to it, and cuts the
// video at the end of the flash; --no-trim keeps the part before it. Without a sync event the
// sounds follow the recorder clock, whose start differs from the video's by an amount that
// changes per run. --offset adds a manual shift (positive = later). The video ends with a
// fade to black of --fade seconds (default 1.2; 0 turns it off). Zoom events become a camera
// that crops and scales the video, on the same clock as the sounds. Needs ffmpeg on PATH.
import { writeFile, readFile, rm } from 'node:fs/promises';
import { spawnSync } from 'node:child_process';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

const args = process.argv.slice(2);
const flags = Object.fromEntries(args.filter((a) => a.startsWith('--')).map((a) => a.slice(2).split('=')));
const [video, eventsPath, out] = args.filter((a) => !a.startsWith('--'));
if (!video || !eventsPath || !out) {
  console.error('usage: finish-recording.mjs <video> <events.json> <out.mp4> [--no-trim] [--offset=s] [--fade=s] [--silent]');
  process.exit(2);
}

const probe = spawnSync('ffprobe', ['-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', video], { encoding: 'utf8' });
const duration = parseFloat(probe.stdout);
if (!Number.isFinite(duration)) { console.error(`cannot read duration of ${video}: ${probe.stderr}`); process.exit(1); }

const { events } = JSON.parse(await readFile(eventsPath, 'utf8'));
const sync = events.find((e) => e.type === 'sync');

// Finds the first run of magenta frames, sampled at 50 fps on a 16x9 thumbnail.
function findFlash() {
  const fps = 50, w = 16, h = 9;
  const raw = spawnSync('ffmpeg', ['-v', 'error', '-i', video, '-vf', `fps=${fps},scale=${w}:${h},format=rgb24`, '-f', 'rawvideo', '-'],
    { maxBuffer: 1 << 30 });
  if (raw.status !== 0) { console.error(`ffmpeg could not read ${video}: ${raw.stderr}`); process.exit(1); }
  const size = w * h * 3, frames = raw.stdout.length / size;
  const magenta = (i) => {
    let r = 0, g = 0, b = 0;
    for (let p = i * size; p < (i + 1) * size; p += 3) { r += raw.stdout[p]; g += raw.stdout[p + 1]; b += raw.stdout[p + 2]; }
    const n = w * h;
    return r / n > 180 && g / n < 80 && b / n > 180;
  };
  let first = -1;
  for (let i = 0; i < frames; i++) if (magenta(i)) { first = i; break; }
  if (first < 0) return null;
  let last = first;
  while (last + 1 < frames && magenta(last + 1)) last++;
  return { start: first / fps, end: (last + 1) / fps };
}

let offset = parseFloat(flags.offset ?? '0');
let trim = 0;
if (sync) {
  const flash = findFlash();
  if (!flash) {
    console.error(`events.json has a sync event at ${sync.t}s, but no magenta flash was found in ${video}`);
    process.exit(1);
  }
  offset += flash.start - sync.t;
  if (!('no-trim' in flags)) trim = flash.end;
  console.log(`sync: flash at ${flash.start.toFixed(2)}s in the video, ${sync.t.toFixed(2)}s on the recorder clock; ` +
    `sounds shifted ${(flash.start - sync.t).toFixed(2)}s${trim ? `, video cut at ${trim.toFixed(2)}s` : ''}`);
}

const length = duration - trim;
// The video ends with a fade to black so the audience sees the recording is over.
const fade = Math.min(parseFloat(flags.fade ?? '1.2'), length / 2);
const fadeAt = (length - fade).toFixed(3);
const rate = 44100;
const samples = new Float32Array(Math.ceil((length + 0.5) * rate));
// Synthesized, license-free sounds: a mouse click (two short ticks) and a soft key tap.
let seed = 7;
const noise = () => ((seed = (seed * 16807) % 2147483647) / 2147483647) * 2 - 1;
function tick(at, { gain, decay, tone }) {
  const start = Math.round(at * rate);
  const len = Math.round(rate * 0.03);
  for (let i = 0; i < len && start + i < samples.length; i++) {
    if (start + i < 0) continue;
    const env = Math.exp(-i / (rate * decay));
    samples[start + i] += gain * env * (0.6 * noise() + 0.4 * Math.sin((2 * Math.PI * tone * i) / rate));
  }
}
const sounds = {
  click: (t) => { tick(t, { gain: 0.55, decay: 0.0025, tone: 2400 }); tick(t + 0.065, { gain: 0.35, decay: 0.002, tone: 2000 }); },
  key: (t) => tick(t, { gain: 0.16 + Math.random() * 0.06, decay: 0.0018, tone: 1500 + Math.random() * 500 }),
};

if (!('silent' in flags)) for (const e of events) sounds[e.type]?.(e.t + offset - trim);

// The camera: each zoom event eases the frame's scale and middle point (fractions of the
// frame) from where they were to the event's values, over the event's ms. Every quantity is
// start + the sum of its changes, each eased by its progress clipped to 0..1, so holds
// need no terms of their own. ffmpeg's perspective filter takes the four corners of the
// visible rectangle; register 0 holds the progress, 1 the scale, 2 the middle point.
const FPS = 25; // Playwright records at 25 fps; the filter chain resamples to it.
const EASE = {
  linear: 'ld(0)',
  easeInOut: 'if(lt(ld(0),0.5),4*ld(0)^3,1-(2-2*ld(0))^3/2)',
  easeOut: '1-(1-ld(0))^3',
  backOut: '1+2.70158*(ld(0)-1)^3+1.70158*(ld(0)-1)^2',
};
function camera() {
  const zooms = events.filter((e) => e.type === 'zoom');
  if (!zooms.length) return null;
  const terms = { scale: [], x: [], y: [] };
  let at = { scale: 1, x: 0.5, y: 0.5 };
  for (const e of zooms) {
    const ease = EASE[e.easing];
    if (!ease) { console.error(`unknown zoom easing ${e.easing}`); process.exit(1); }
    const start = (e.t + offset - trim).toFixed(3), ms = Math.max(1, e.ms) / 1000;
    for (const k of Object.keys(terms)) {
      const d = e[k] - at[k];
      if (d) terms[k].push(`(st(0,clip((in/${FPS}-(${start}))/${ms},0,1));${d.toFixed(5)}*(${ease}))`);
    }
    at = { scale: e.scale, x: e.x, y: e.y };
  }
  const sum = (k, base) => [base, ...terms[k]].join('+');
  // Keeps the visible rectangle inside the frame, so a zoom near an edge never shows past it.
  const middle = (k, size) => `st(1,${sum('scale', 1)});st(2,clip(${size}*(${sum(k, 0.5)}),${size}/2/ld(1),${size}-${size}/2/ld(1)))`;
  const x = (side) => `'${middle('x', 'W')};ld(2)${side}W/2/ld(1)'`;
  const y = (side) => `'${middle('y', 'H')};ld(2)${side}H/2/ld(1)'`;
  return `fps=${FPS},perspective=x0=${x('-')}:y0=${y('-')}:x1=${x('+')}:y1=${y('-')}:x2=${x('-')}:y2=${y('+')}:x3=${x('+')}:y3=${y('+')}` +
    ':interpolation=cubic:eval=frame';
}
const zoom = camera();
const vf = [zoom, fade > 0 && `fade=t=out:st=${fadeAt}:d=${fade}`].filter(Boolean).join(',');

const pcm = Buffer.alloc(44 + samples.length * 2);
pcm.write('RIFF', 0); pcm.writeUInt32LE(36 + samples.length * 2, 4); pcm.write('WAVEfmt ', 8);
pcm.writeUInt32LE(16, 16); pcm.writeUInt16LE(1, 20); pcm.writeUInt16LE(1, 22); pcm.writeUInt32LE(rate, 24);
pcm.writeUInt32LE(rate * 2, 28); pcm.writeUInt16LE(2, 32); pcm.writeUInt16LE(16, 34); pcm.write('data', 36);
pcm.writeUInt32LE(samples.length * 2, 40);
samples.forEach((v, i) => pcm.writeInt16LE(Math.round(Math.max(-1, Math.min(1, v)) * 32767), 44 + i * 2));
const wav = join(tmpdir(), `demo-sounds-${process.pid}.wav`);
await writeFile(wav, pcm);

const ff = spawnSync('ffmpeg', ['-y', '-loglevel', 'error', '-ss', String(trim), '-i', video, '-i', wav,
  ...(vf ? ['-vf', vf] : []), ...(fade > 0 ? ['-af', `afade=t=out:st=${fadeAt}:d=${fade}`] : []),
  '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-crf', '18', '-preset', 'medium', '-pix_fmt', 'yuv420p',
  '-c:a', 'aac', '-b:a', '128k', '-shortest', '-movflags', '+faststart', out], { stdio: 'inherit' });
await rm(wav, { force: true });
if (ff.status !== 0) process.exit(ff.status ?? 1);
console.log(`${out}: ${length.toFixed(1)}s, ${events.filter((e) => sounds[e.type]).length} sound events, ` +
  `${events.filter((e) => e.type === 'zoom').length} zoom moves`);

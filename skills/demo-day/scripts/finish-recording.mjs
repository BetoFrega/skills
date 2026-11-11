#!/usr/bin/env node
// Adds click and keystroke sounds to a demo recording and writes an MP4.
// Usage: node finish-recording.mjs <video.webm|mp4> <events.json> <out.mp4> [--no-trim] [--offset=<seconds>] [--fade=<seconds>] [--silent]
// events.json comes from recorder.saveEvents(). When it holds a sync event (rec.syncFlash()),
// the script finds the magenta flash in the video, aligns every sound to it, and cuts the
// video at the end of the flash; --no-trim keeps the part before it. Without a sync event the
// sounds follow the recorder clock, whose start differs from the video's by an amount that
// changes per run. --offset adds a manual shift (positive = later). The video ends with a
// fade to black of --fade seconds (default 1.2; 0 turns it off). Needs ffmpeg on PATH.
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

const pcm = Buffer.alloc(44 + samples.length * 2);
pcm.write('RIFF', 0); pcm.writeUInt32LE(36 + samples.length * 2, 4); pcm.write('WAVEfmt ', 8);
pcm.writeUInt32LE(16, 16); pcm.writeUInt16LE(1, 20); pcm.writeUInt16LE(1, 22); pcm.writeUInt32LE(rate, 24);
pcm.writeUInt32LE(rate * 2, 28); pcm.writeUInt16LE(2, 32); pcm.writeUInt16LE(16, 34); pcm.write('data', 36);
pcm.writeUInt32LE(samples.length * 2, 40);
samples.forEach((v, i) => pcm.writeInt16LE(Math.round(Math.max(-1, Math.min(1, v)) * 32767), 44 + i * 2));
const wav = join(tmpdir(), `demo-sounds-${process.pid}.wav`);
await writeFile(wav, pcm);

const ff = spawnSync('ffmpeg', ['-y', '-loglevel', 'error', '-ss', String(trim), '-i', video, '-i', wav,
  ...(fade > 0 ? ['-vf', `fade=t=out:st=${fadeAt}:d=${fade}`, '-af', `afade=t=out:st=${fadeAt}:d=${fade}`] : []),
  '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-crf', '18', '-preset', 'medium', '-pix_fmt', 'yuv420p',
  '-c:a', 'aac', '-b:a', '128k', '-shortest', '-movflags', '+faststart', out], { stdio: 'inherit' });
await rm(wav, { force: true });
if (ff.status !== 0) process.exit(ff.status ?? 1);
console.log(`${out}: ${length.toFixed(1)}s, ${events.filter((e) => sounds[e.type]).length} sound events`);

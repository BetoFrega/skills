#!/usr/bin/env node
// Adds click and keystroke sounds to a demo recording and writes an MP4.
// Usage: node finish-recording.mjs <video.webm|mp4> <events.json> <out.mp4> [--offset=<seconds>] [--silent]
// events.json comes from recorder.saveEvents(). --offset shifts every sound (positive = later)
// when the video started before or after the recorder's clock. Needs ffmpeg on PATH.
import { writeFile, readFile, rm } from 'node:fs/promises';
import { spawnSync } from 'node:child_process';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

const args = process.argv.slice(2);
const flags = Object.fromEntries(args.filter((a) => a.startsWith('--')).map((a) => a.slice(2).split('=')));
const [video, eventsPath, out] = args.filter((a) => !a.startsWith('--'));
if (!video || !eventsPath || !out) {
  console.error('usage: finish-recording.mjs <video> <events.json> <out.mp4> [--offset=s] [--silent]');
  process.exit(2);
}

const probe = spawnSync('ffprobe', ['-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', video], { encoding: 'utf8' });
const duration = parseFloat(probe.stdout);
if (!Number.isFinite(duration)) { console.error(`cannot read duration of ${video}: ${probe.stderr}`); process.exit(1); }

const rate = 44100;
const samples = new Float32Array(Math.ceil((duration + 0.5) * rate));

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

const offset = parseFloat(flags.offset ?? '0');
const { events } = JSON.parse(await readFile(eventsPath, 'utf8'));
if (!('silent' in flags)) for (const e of events) sounds[e.type]?.(e.t + offset);

const pcm = Buffer.alloc(44 + samples.length * 2);
pcm.write('RIFF', 0); pcm.writeUInt32LE(36 + samples.length * 2, 4); pcm.write('WAVEfmt ', 8);
pcm.writeUInt32LE(16, 16); pcm.writeUInt16LE(1, 20); pcm.writeUInt16LE(1, 22); pcm.writeUInt32LE(rate, 24);
pcm.writeUInt32LE(rate * 2, 28); pcm.writeUInt16LE(2, 32); pcm.writeUInt16LE(16, 34); pcm.write('data', 36);
pcm.writeUInt32LE(samples.length * 2, 40);
samples.forEach((v, i) => pcm.writeInt16LE(Math.round(Math.max(-1, Math.min(1, v)) * 32767), 44 + i * 2));
const wav = join(tmpdir(), `demo-sounds-${process.pid}.wav`);
await writeFile(wav, pcm);

const ff = spawnSync('ffmpeg', ['-y', '-loglevel', 'error', '-i', video, '-i', wav,
  '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-crf', '18', '-preset', 'medium', '-pix_fmt', 'yuv420p',
  '-c:a', 'aac', '-b:a', '128k', '-shortest', '-movflags', '+faststart', out], { stdio: 'inherit' });
await rm(wav, { force: true });
if (ff.status !== 0) process.exit(ff.status ?? 1);
console.log(`${out}: ${duration.toFixed(1)}s, ${events.length} sound events`);

# Recording a demo video

Read this when a feature's rehearsal passes and the demo day needs a video of it.

## Tools

[recorder.mjs](../scripts/recorder.mjs) wraps Playwright actions so they read as a
person on camera: a drawn cursor with character, eased curved moves, click ripples,
human typing, and staging effects. Its header shows the setup.
[finish-recording.mjs](../scripts/finish-recording.mjs) adds click and key sounds
and writes the MP4. It needs ffmpeg.

Copy `recorder.mjs` next to the recording scripts in the demo day's folder, so the
recording reproduces after the plugin updates. Write one recording script per
feature that follows its demo script step by step and its Staging column, starting
from the clean setup state.

## Rules the helpers cannot enforce

- Drive every visible action through the recorder. A raw `page.click`, `fill`, or
  `selectOption` makes the cursor jump and the field fill at once.
- Open what a person would open. For a custom dropdown, click the trigger, then the
  option. For a native `<select>`, use `select()`: Playwright's video never shows the
  native popup, so the helper draws a look-alike list.
- Use realistic data: names, emails, and amounts an audience believes. No `test123`.
- Hide what does not belong in the product: dev toolbars, cookie banners, framework
  error overlays, debug logs.
- Keep a fixed viewport, 1280x720 or 1920x1080, and log in during setup, off camera.
- Give the audience time to read: pause after each result, longer after the payoff.
- Avoid states that only exist on hover with nothing to read; hover only when the
  hover shows something.
- Watch the result before calling it done. Sample frames or watch it whole; a cut
  callout, a cursor in a corner, or a flash of an unstyled page fails the recording.

## Direct it: be bold

Treat the recording as a short cartoon and the cursor as its lead character. A flat
recording of correct clicks is the failure to avoid; so is a cursor that only points.
The video cursor is drawn, not a real mouse, so it can rotate, stretch, jump, and
show feelings. Use that freedom.

Before recording, give the cursor a small arc for each feature: what it looks for,
where it gets stuck or curious, and how it feels at the payoff. Every video needs at
least:

- an entrance: `enter()` before the first move;
- one expression before the payoff that builds tension, such as `confused`, `think`,
  or `hesitate`;
- the payoff staged with suspense, an impact click, and a reaction, such as
  `celebrate`, `wow`, or `excited`;
- an exit: `exit()` as the last beat, before the closing pause.

Place each expression where the audience feels the same thing. A `confused` while
looking for a hidden setting sells the old pain; a `celebrate` right next to the
saved record sells the win. Move the cursor next to the result before it reacts.

- **Expressions.** `react(name)`: `celebrate` jumps for joy with a spin and stars,
  `excited` bounces, `wow` jumps back with a "!", `confused` tilts its head both ways
  under a "?", `sad` droops with a tear, `nod` agrees, `shake` refuses, `think`
  circles while pondering, and `react('hesitate', { target })` approaches, backs
  off, and returns.
- **Character.** `installCursor(context, { life })`: the cursor stretches and leaves
  smear trails on fast moves, leans into them, springs back when it stops, squashes on
  clicks, and breathes while idle, after the Disney principles of animation. `1.4`
  is the default, `1` is milder, `2` is cartoon-loud, and `0` draws a plain cursor.
- **Entrance and exit.** `enter({ side, at })` flies in from beyond an edge and lands
  with a spring; `exit({ side })` winds up and zips out.
- **Motion.** `createRecorder(page, { motion })` sets the default style and each
  action takes `{ motion }`. `calm` is near straight, `natural` is the default,
  `flourish` swings wide with overshoot and wobble, `showtime` adds anticipation
  and big arcs. Every field (`curve`, `overshoot`, `wobble`, `waves`, `pace`,
  `anticipation`, `easing`) can be set by hand. Use `flourish` or `showtime` for
  the moves into key moments.
- **Suspense and impact.** `click(target, { suspense: ms, impact: true })` stops
  just short of the target, holds, then presses hard with rings and sparks. Save the
  impact for the click that delivers the payoff.
- **Staging.** `spotlight(target)` darkens everything else; `callout(target, text)`
  puts a short caption beside it that hovers above the page (`float` sets the bob);
  `chapter(title, description)` opens a section. Keep captions to a few words that
  say why it matters.
- **Zoom.** `zoom(target, { mood })` frames the result: `subtle` nudges, `reveal`
  pushes in calmly, `punch` pops with overshoot for a win, `dramatic` pushes in
  slowly and holds for the big reveal.
- **Humanity.** `type(target, text, { typos: 1 })` slips and corrects;
  `glance(area)` lets the cursor wander as if reading before it acts.

Contrast makes the acting land: keep routine steps brisk, then slow down and play
the moment that matters. When unsure between more and less, record the bolder take
first; tone it down only if the user asks.

## Finish

Call `rec.syncFlash()` once, after the page has loaded and right before the part
the audience should see. The recorder clock and the video start at different
moments, and the gap changes from run to run, so neither a fixed `--offset` nor a
cut time taken from the script clock lines up the sounds. Save the events with
`rec.saveEvents()`, then run:

```sh
node finish-recording.mjs <video.webm> <events.json> <feature>.mp4
```

It finds the flash in the video, aligns every sound to it, and cuts the video at
the end of the flash, which also removes the loading. The video ends with a 1.2 s
fade to black, so end the script with a pause the fade can take. `--no-trim` keeps
the part before the flash, `--offset=<seconds>` adds a manual shift, `--fade=<seconds>`
changes the fade (`0` turns it off), and `--silent` drops the sounds. Link the MP4 in the rehearsal report as the feature's evidence.

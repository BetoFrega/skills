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
feature that follows its demo script step by step, starting from the clean setup
state.

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

Treat the cursor as a character and the recording as a short film. A flat recording
of correct clicks is the failure to avoid. Pick a moment that carries the feature,
usually the result the audience came to see, and spend your flourishes there.

- **Motion.** `createRecorder(page, { motion })` sets the default style and each
  action takes `{ motion }`. `calm` is near straight, `natural` is the default,
  `flourish` swings wide with overshoot and wobble, `showtime` adds anticipation
  and big arcs. Every field (`curve`, `overshoot`, `wobble`, `waves`, `pace`,
  `anticipation`, `easing`) can be set by hand. Use `flourish` or `showtime` for
  the moves into key moments.
- **Character.** `installCursor(context, { life })`: the cursor stretches along fast
  moves, leans into them, springs back when it stops, squashes on clicks, and
  breathes while idle, after the Disney principles of animation. `1` is the
  default, `0` turns it off, `2` exaggerates it.
- **Suspense.** `click(target, { suspense: ms })` stops just short of the target,
  holds, then clicks. Use it right before the click that delivers the payoff.
- **Staging.** `spotlight(target)` darkens everything else; `callout(target, text)`
  puts a short caption beside it; `chapter(title, description)` opens a section.
  Keep captions to a few words that say why it matters.
- **Zoom.** `zoom(target, { mood })` frames the result: `subtle` nudges, `reveal`
  pushes in calmly, `punch` pops with overshoot for a win, `dramatic` pushes in
  slowly and holds for the big reveal.
- **Humanity.** `type(target, text, { typos: 1 })` slips and corrects;
  `glance(area)` lets the cursor wander as if reading before it acts.

Contrast makes flourishes land: keep routine steps brisk and plain, then slow down
and stage the moment that matters. When unsure between more and less, record both
takes and keep the better one.

## Finish

Save the events with `rec.saveEvents()`, then run:

```sh
node finish-recording.mjs <video.webm> <events.json> <feature>.mp4
```

Pass `--offset=<seconds>` when sounds drift from the clicks, or `--silent` for no
sounds. Link the MP4 in the rehearsal report as the feature's evidence.

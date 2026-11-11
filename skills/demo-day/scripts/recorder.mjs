// Recorder-friendly Playwright helpers for demo-day videos.
//
// Draws a visible cursor (arrow, hand, or I-beam, following the CSS `cursor` under
// it), moves it along eased curves, shows a ripple on clicks, types at human speed,
// renders native <select> options as a visible list, shows chapter cards, and logs
// clicks and keystrokes so finish-recording.mjs can add sounds.
//
// Usage:
//   const context = await browser.newContext({ viewport, recordVideo: { dir, size: viewport } });
//   await installCursor(context);
//   const page = await context.newPage();
//   const rec = createRecorder(page); // right after newPage: the video starts there
//   await page.goto(url);
//   await rec.chapter('Customer sign-up', 'New flow for sales');
//   await rec.click('#name'); await rec.type('#name', 'Ana Souza');
//   await rec.select('#plan', 'Pro'); await rec.click('#save');
//   await rec.pause(1500);
//   await rec.saveEvents('events.json');
//   const video = page.video(); await context.close(); await video.saveAs('demo.webm');
//
// Playwright's video does not capture native <select> popups, so select() draws a
// look-alike list over the page while it picks the option.

const CURSOR_SCRIPT = `(() => {
  if (window.__demoCursor) return;
  const svg = (body, w = 28, h = 28) =>
    '<svg xmlns="http://www.w3.org/2000/svg" width="' + w + '" height="' + h + '" viewBox="0 0 28 28">' + body + '</svg>';
  const shapes = {
    arrow: { x: 3, y: 2, html: svg('<path d="M3 2v20l5.5-5.2 3.6 8.2 3.4-1.5-3.6-8H19z" fill="#111" stroke="#fff" stroke-width="1.6" stroke-linejoin="round"/>') },
    pointer: { x: 9, y: 2, html: svg('<path d="M9 13V4.5a2 2 0 0 1 4 0V12h.5V10a2 2 0 0 1 4 0v2h.5v-1a2 2 0 0 1 4 0v1.5a2 2 0 0 1 3.5 1.3V18c0 4.5-3 8-7.5 8H15c-2.5 0-4-1-5.5-3L5 17.2a2 2 0 0 1 3-2.6z" fill="#fff" stroke="#111" stroke-width="1.6" stroke-linejoin="round"/>') },
    text: { x: 14, y: 14, html: svg('<path d="M10 4h8M10 24h8M14 4v20" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/><path d="M10 4h8M10 24h8M14 4v20" fill="none" stroke="#111" stroke-width="1.8" stroke-linecap="round"/>') },
  };
  // Two layers: el moves the cursor; body gives it life (squash, stretch, lean, breath).
  const life = window.__demoLife ?? 1;
  const el = document.createElement('div');
  const body = document.createElement('div');
  el.setAttribute('data-demo-overlay', '');
  el.appendChild(body);
  Object.assign(el.style, { position: 'fixed', left: '0', top: '0', zIndex: '2147483647', pointerEvents: 'none', willChange: 'transform' });
  Object.assign(body.style, { willChange: 'transform', transition: 'transform .35s cubic-bezier(.34,1.8,.64,1)' });
  const style = document.createElement('style');
  style.textContent = '@keyframes demo-breathe{0%,100%{transform:scale(1)}50%{transform:scale(' + (1 + 0.07 * life) + ') rotate(' + (-3 * life) + 'deg)}}';
  let kind = '', x = -100, y = -100, lastT = 0, vx = 0, vy = 0, idle = 0, pressed = false;
  const setKind = (k) => {
    if (k === kind) return;
    kind = k; body.innerHTML = shapes[k].html;
    body.style.transformOrigin = shapes[k].x + 'px ' + shapes[k].y + 'px';
    place();
  };
  const place = () => { const s = shapes[kind]; el.style.transform = 'translate(' + (x - s.x) + 'px,' + (y - s.y) + 'px)'; };
  // Follows the motion: stretches along the direction of travel and leans into it.
  const pose = () => {
    if (pressed || !life) return;
    const v = Math.hypot(vx, vy);
    if (v < 0.05) { body.style.transform = ''; return; }
    const angle = Math.atan2(vy, vx) * 180 / Math.PI;
    const k = Math.min(0.35, v * 0.12) * life;
    const lean = Math.max(-18, Math.min(18, vx * 9)) * life;
    body.style.transition = 'transform .08s linear';
    body.style.transform = 'rotate(' + lean + 'deg) rotate(' + angle + 'deg) scale(' + (1 + k) + ',' + (1 - k * 0.6) + ') rotate(' + -angle + 'deg)';
  };
  // When the cursor stops, it springs back to rest (follow-through), then breathes.
  const settle = () => {
    vx = vy = 0;
    body.style.transition = 'transform .45s cubic-bezier(.34,1.8,.64,1)';
    body.style.transform = '';
    clearTimeout(idle);
    if (life) idle = setTimeout(() => { body.style.transition = ''; body.style.animation = 'demo-breathe 2.4s ease-in-out infinite'; }, 900);
  };
  let settleTimer = 0;
  const kindAt = (px, py) => {
    const t = document.elementFromPoint(px, py);
    if (!t) return 'arrow';
    const c = getComputedStyle(t).cursor;
    if (c === 'pointer') return 'pointer';
    if (c === 'text' || c === 'vertical-text') return 'text';
    if (c === 'auto' && (t.isContentEditable || t.matches('input:not([type=checkbox]):not([type=radio]):not([type=button]):not([type=submit]), textarea'))) return 'text';
    return 'arrow';
  };
  window.__demoCursor = { el };
  setKind('arrow');
  const mount = () => { document.documentElement.appendChild(style); document.documentElement.appendChild(el); };
  document.documentElement ? mount() : addEventListener('DOMContentLoaded', mount);
  addEventListener('mousemove', (e) => {
    const now = performance.now(), dt = Math.max(8, now - lastT);
    if (lastT && now - lastT < 200) { vx = vx * 0.5 + 0.5 * (e.clientX - x) / dt; vy = vy * 0.5 + 0.5 * (e.clientY - y) / dt; }
    lastT = now; x = e.clientX; y = e.clientY;
    body.style.animation = ''; clearTimeout(idle);
    setKind(kindAt(x, y)); place(); pose();
    clearTimeout(settleTimer); settleTimer = setTimeout(settle, 60);
  }, true);
  addEventListener('mousedown', (e) => {
    pressed = true;
    body.style.animation = '';
    body.style.transition = 'transform .07s ease-out';
    body.style.transform = 'scale(' + (1 + 0.15 * life) + ',' + (1 - 0.25 * life) + ')';
    const r = document.createElement('div');
    r.setAttribute('data-demo-overlay', '');
    Object.assign(r.style, { position: 'fixed', left: e.clientX - 16 + 'px', top: e.clientY - 16 + 'px', width: '32px', height: '32px',
      borderRadius: '50%', background: 'rgba(37,99,235,.35)', zIndex: '2147483646', pointerEvents: 'none', transition: 'transform .45s ease-out, opacity .45s ease-out' });
    document.documentElement.appendChild(r);
    requestAnimationFrame(() => { r.style.transform = 'scale(2.2)'; r.style.opacity = '0'; });
    setTimeout(() => r.remove(), 500);
  }, true);
  addEventListener('mouseup', () => { pressed = false; settle(); }, true);
})()`;

// life: 0 draws a plain cursor; 1 (default) gives it character, following the Disney
// principles of animation (squash and stretch, follow-through, secondary action);
// up to 2 exaggerates it.
export async function installCursor(context, { life = 1 } = {}) {
  await context.addInitScript('window.__demoLife = ' + Number(life) + ';' + CURSOR_SCRIPT);
}

const easings = {
  linear: (t) => t,
  easeInOut: (t) => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2),
  easeOut: (t) => 1 - Math.pow(1 - t, 3),
};
const between = (a, b) => a + Math.random() * (b - a);

// Motion styles. Every field can be overridden per recorder or per action.
//   curve:     how far the path bows sideways, as a fraction of the distance (0 = straight)
//   overshoot: how far it passes the target before settling back (fraction of the distance)
//   wobble:    sideways waviness in pixels along the way
//   waves:     how many wobble waves fit in one move
//   pace:      duration multiplier (>1 slower)
//   anticipation: a small pull back before leaving, as a fraction of the distance
//   easing:    linear | easeInOut | easeOut
export const MOTION = {
  calm: { anticipation: 0, curve: 0.06, overshoot: 0, wobble: 0, waves: 1, pace: 1.2, easing: 'easeInOut' },
  natural: { anticipation: 0.02, curve: 0.18, overshoot: 0.04, wobble: 2, waves: 1.5, pace: 1, easing: 'easeInOut' },
  flourish: { anticipation: 0.05, curve: 0.42, overshoot: 0.12, wobble: 9, waves: 2.5, pace: 1.15, easing: 'easeOut' },
  showtime: { anticipation: 0.08, curve: 0.55, overshoot: 0.16, wobble: 14, waves: 3, pace: 1.35, easing: 'easeOut' },
};
// Zoom moods: subtle (a nudge), reveal (calm push-in to show a result), punch (fast pop
// with overshoot, for a win), dramatic (slow push-in with a long hold, for the big reveal).
export const ZOOM = {
  subtle: { scale: 1.25, ms: 900, easing: 'cubic-bezier(.4,0,.2,1)', hold: 1400 },
  reveal: { scale: 1.5, ms: 1100, easing: 'cubic-bezier(.65,0,.35,1)', hold: 1800 },
  punch: { scale: 1.8, ms: 420, easing: 'cubic-bezier(.34,1.56,.64,1)', hold: 1200, outMs: 500 },
  dramatic: { scale: 2.1, ms: 2600, easing: 'cubic-bezier(.3,0,.2,1)', hold: 2600, outMs: 1400 },
};
const resolveMotion = (m) => ({ ...MOTION.natural, ...(typeof m === 'string' ? MOTION[m] : m) });

export function createRecorder(page, options = {}) {
  const frameMs = options.frameMs ?? 16;
  const speed = options.speed ?? 1; // >1 moves and types faster
  let motion = resolveMotion(options.motion ?? 'natural');
  const t0 = Date.now();
  const events = [];
  const log = (type) => events.push({ type, t: (Date.now() - t0) / 1000 });
  const viewport = page.viewportSize() ?? { width: 1280, height: 720 };
  let pos = { x: viewport.width / 2, y: viewport.height / 2 };
  let parked = false;

  const wait = (ms) => page.waitForTimeout(ms / speed);

  async function glide(from, to, ms, m, easing) {
    const dx = to.x - from.x, dy = to.y - from.y;
    const dist = Math.hypot(dx, dy) || 1;
    const nx = -dy / dist, ny = dx / dist; // unit normal
    const bend = m.curve * (Math.random() < 0.5 ? -1 : 1) * between(0.7, 1.3);
    const cx = (from.x + to.x) / 2 + nx * dist * bend, cy = (from.y + to.y) / 2 + ny * dist * bend;
    const phase = Math.random() * Math.PI;
    const steps = Math.max(6, Math.round(ms / frameMs));
    for (let i = 1; i <= steps; i++) {
      const t = easing(i / steps), u = 1 - t;
      const w = m.wobble * Math.sin(t * Math.PI) * Math.sin(phase + t * Math.PI * 2 * m.waves);
      const px = u * u * from.x + 2 * u * t * cx + t * t * to.x + nx * w;
      const py = u * u * from.y + 2 * u * t * cy + t * t * to.y + ny * w;
      await page.mouse.move(Math.min(viewport.width - 4, Math.max(4, px)), Math.min(viewport.height - 4, Math.max(4, py)));
      await page.waitForTimeout(frameMs);
    }
  }

  async function moveTo(x, y, override) {
    const m = override ? { ...motion, ...resolveMotion(override) } : motion;
    await page.mouse.move(pos.x, pos.y); // redraws the cursor after a navigation
    const dist = Math.hypot(x - pos.x, y - pos.y);
    if (dist < 2) return;
    const ms = (Math.min(1000, 280 + dist * 0.7) * m.pace) / speed;
    const easing = easings[m.easing] ?? easings.easeInOut;
    if (m.anticipation > 0 && dist > 80) {
      const back = Math.min(18, dist * m.anticipation);
      const wind = { x: pos.x - ((x - pos.x) / dist) * back, y: pos.y - ((y - pos.y) / dist) * back };
      await glide(pos, wind, 140 * m.pace, { ...m, curve: 0, wobble: 0 }, easings.easeOut);
      pos = wind;
      await page.waitForTimeout(60);
    }
    if (m.overshoot > 0 && dist > 60) {
      const k = 1 + m.overshoot;
      const past = { x: pos.x + (x - pos.x) * k, y: pos.y + (y - pos.y) * k };
      await glide(pos, past, ms * 0.85, m, easing);
      await glide(past, { x, y }, Math.max(120, ms * 0.25), { ...m, curve: 0, wobble: 0 }, easings.easeOut);
    } else {
      await glide(pos, { x, y }, ms, m, easing);
    }
    pos = { x, y };
  }

  const setMotion = (m) => { motion = resolveMotion(m); };

  async function targetPoint(locator) {
    if (!parked) { parked = true; await page.mouse.move(pos.x, pos.y); } // no cursor stuck in the corner
    await locator.waitFor({ state: 'visible' });
    const inView = await locator.evaluate((el) => {
      const r = el.getBoundingClientRect();
      return r.top >= 0 && r.bottom <= innerHeight && r.left >= 0 && r.right <= innerWidth;
    });
    if (!inView) {
      await locator.evaluate((el) => el.scrollIntoView({ behavior: 'smooth', block: 'center' }));
      await wait(700);
    }
    const box = await locator.boundingBox();
    return {
      x: box.x + box.width * between(0.35, 0.6),
      y: box.y + box.height * between(0.4, 0.6),
      box,
    };
  }

  const loc = (target) => (typeof target === 'string' ? page.locator(target) : target);

  async function hover(target, { motion: m } = {}) {
    const p = await targetPoint(loc(target));
    await moveTo(p.x, p.y, m);
    await wait(250);
  }

  // suspense: ms of anticipation. The cursor stops just short of the target, holds,
  // then eases onto it and clicks. Use it before the click that delivers the payoff.
  async function clickAt(x, y, m, suspense = 0) {
    if (suspense) {
      const dx = x - pos.x, dy = y - pos.y, d = Math.hypot(dx, dy) || 1;
      const gap = Math.min(28, d / 3);
      await moveTo(x - (dx / d) * gap, y - (dy / d) * gap, m);
      await wait(suspense);
      await glide(pos, { x, y }, 420, { ...motion, curve: 0, wobble: 0 }, easings.easeInOut);
      pos = { x, y };
      await wait(180);
    } else {
      await moveTo(x, y, m);
    }
    await wait(between(120, 220));
    log('click');
    await page.mouse.down();
    await page.waitForTimeout(70);
    await page.mouse.up();
    await wait(250);
  }

  async function click(target, { motion: m, suspense = 0 } = {}) {
    const p = await targetPoint(loc(target));
    await clickAt(p.x, p.y, m, suspense === true ? 1200 : suspense);
  }

  // typos: how many slips to make and correct on the way (never on the first character).
  async function type(target, text, { clear = true, typos = 0 } = {}) {
    const l = loc(target);
    if (target !== null) {
      const focused = await l.evaluate((el) => el === document.activeElement);
      if (!focused) await click(l);
      if (clear) await l.fill('');
    }
    const slips = new Set();
    const letters = [...text].map((c, i) => (i > 0 && /[a-z]/i.test(c) ? i : -1)).filter((i) => i > 0);
    while (slips.size < Math.min(typos, letters.length)) slips.add(letters[Math.floor(Math.random() * letters.length)]);
    const neighbor = (c) => {
      const rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm'];
      const lower = c.toLowerCase();
      for (const r of rows) { const i = r.indexOf(lower); if (i >= 0) return r[i + 1] ?? r[i - 1]; }
      return 'x';
    };
    const key = async (k, extra = 0) => {
      log('key');
      await page.keyboard.type(k);
      await page.waitForTimeout(between(45, 130) / speed + extra);
    };
    for (const [i, ch] of [...text].entries()) {
      if (slips.has(i)) {
        await key(neighbor(ch));
        await page.waitForTimeout(between(250, 450) / speed); // notices the slip
        log('key');
        await page.keyboard.press('Backspace');
        await page.waitForTimeout(between(120, 200) / speed);
      }
      await key(ch, ch === ' ' ? 60 : 0);
    }
    await wait(300);
  }

  async function press(key) {
    log('key');
    await page.keyboard.press(key);
    await wait(250);
  }

  // Native <select> popups are drawn outside the page, so videos never show them.
  // This opens a look-alike list over the page, clicks the option, then sets the value.
  async function select(target, label) {
    const l = loc(target);
    const isNative = await l.evaluate((el) => el.tagName === 'SELECT');
    if (!isNative) throw new Error('select() is for native <select>; click the trigger and the option instead');
    const p = await targetPoint(l);
    await clickAt(p.x, p.y);
    const optionBox = await l.evaluate((el, wanted) => {
      const r = el.getBoundingClientRect();
      const cs = getComputedStyle(el);
      const list = document.createElement('div');
      list.setAttribute('data-demo-select', '');
      Object.assign(list.style, { position: 'fixed', left: r.left + 'px', top: r.bottom + 2 + 'px', width: r.width + 'px',
        background: '#fff', border: '1px solid #c8c8c8', borderRadius: '6px', boxShadow: '0 8px 24px rgba(0,0,0,.18)',
        zIndex: '2147483640', font: cs.font, padding: '4px 0', overflow: 'hidden' });
      let hit = null;
      for (const o of el.options) {
        const row = document.createElement('div');
        row.textContent = o.label;
        Object.assign(row.style, { padding: '6px 12px', cursor: 'pointer',
          background: o.selected ? '#e8eefc' : 'transparent' });
        row.addEventListener('mouseenter', () => { row.style.background = '#2563eb'; row.style.color = '#fff'; });
        row.addEventListener('mouseleave', () => { row.style.background = o.selected ? '#e8eefc' : 'transparent'; row.style.color = ''; });
        list.appendChild(row);
        if (o.label === wanted || o.value === wanted) hit = row;
      }
      document.documentElement.appendChild(list);
      if (!hit) { list.remove(); return null; }
      const b = hit.getBoundingClientRect();
      return { x: b.left, y: b.top, width: b.width, height: b.height };
    }, label);
    if (!optionBox) throw new Error(`option not found: ${label}`);
    await wait(450);
    await clickAt(optionBox.x + Math.min(60, optionBox.width / 3), optionBox.y + optionBox.height / 2);
    await page.evaluate(() => document.querySelectorAll('[data-demo-select]').forEach((n) => n.remove()));
    await l.selectOption({ label }).catch(() => l.selectOption(label));
    await wait(300);
  }

  async function chapter(title, description = '', ms = 1800) {
    await page.mouse.move(pos.x, pos.y); // parks the cursor before the first move
    await page.evaluate(({ title, description }) => {
      const card = document.createElement('div');
      card.setAttribute('data-demo-chapter', '');
      card.innerHTML = '<div style="font-size:34px;font-weight:650">' + title.replace(/</g, '&lt;') + '</div>' +
        (description ? '<div style="font-size:18px;opacity:.8;margin-top:10px">' + description.replace(/</g, '&lt;') + '</div>' : '');
      Object.assign(card.style, { position: 'fixed', inset: '0', display: 'flex', flexDirection: 'column', alignItems: 'center',
        justifyContent: 'center', background: 'rgba(15,23,42,.72)', backdropFilter: 'blur(6px)', color: '#fff',
        font: '16px system-ui, sans-serif', zIndex: '2147483645', opacity: '0', transition: 'opacity .35s' });
      document.documentElement.appendChild(card);
      requestAnimationFrame(() => (card.style.opacity = '1'));
    }, { title, description });
    await page.waitForTimeout(ms / speed);
    await page.evaluate(() => document.querySelectorAll('[data-demo-chapter]').forEach((n) => (n.style.opacity = '0')));
    await page.waitForTimeout(400);
    await page.evaluate(() => document.querySelectorAll('[data-demo-chapter]').forEach((n) => n.remove()));
  }


  // --- Staging -------------------------------------------------------------------

  // Darkens everything except the target. hold: ms before it fades (0 keeps it until clearSpotlight()).
  async function spotlight(target, { hold = 1800, padding = 10, dim = 0.6 } = {}) {
    const box = (await targetPoint(loc(target))).box;
    await page.evaluate(({ box, padding, dim }) => {
      document.querySelectorAll('[data-demo-spotlight]').forEach((n) => n.remove());
      const s = document.createElement('div');
      s.setAttribute('data-demo-spotlight', '');
      Object.assign(s.style, { position: 'fixed', left: box.x - padding + 'px', top: box.y - padding + 'px',
        width: box.width + padding * 2 + 'px', height: box.height + padding * 2 + 'px', borderRadius: '12px',
        boxShadow: `0 0 0 200vmax rgba(10,14,25,${dim})`, zIndex: '2147483600', pointerEvents: 'none',
        opacity: '0', transition: 'opacity .5s ease' });
      document.documentElement.appendChild(s);
      requestAnimationFrame(() => (s.style.opacity = '1'));
    }, { box, padding, dim });
    await wait(500);
    if (hold) { await wait(hold); await clearSpotlight(); }
  }

  async function clearSpotlight() {
    await page.evaluate(() => document.querySelectorAll('[data-demo-spotlight]').forEach((n) => (n.style.opacity = '0')));
    await wait(450);
    await page.evaluate(() => document.querySelectorAll('[data-demo-spotlight]').forEach((n) => n.remove()));
  }

  // A speech-bubble caption beside the target, with a tail pointing at it. It hovers
  // above the page: it bobs up and down while its shadow widens and fades, so it
  // reads as an annotation, not part of the UI. float: bob height in px (0 = still).
  // hold: ms on screen (0 keeps it until clearCallouts()).
  async function callout(target, text, { hold = 2200, float = 6 } = {}) {
    const box = (await targetPoint(loc(target))).box;
    await page.evaluate(({ box, text, float }) => {
      if (!document.getElementById('demo-callout-style')) {
        const st = document.createElement('style');
        st.id = 'demo-callout-style';
        st.textContent = '@keyframes demo-hover{0%,100%{transform:translateY(0);box-shadow:0 6px 14px rgba(0,0,0,.30),0 2px 4px rgba(0,0,0,.18)}' +
          '50%{transform:translateY(calc(-1px * var(--demo-float)));box-shadow:0 22px 38px rgba(0,0,0,.20),0 8px 12px rgba(0,0,0,.08)}}';
        document.documentElement.appendChild(st);
      }
      const c = document.createElement('div');
      const bubble = document.createElement('div');
      const tail = document.createElement('div');
      c.setAttribute('data-demo-callout', '');
      bubble.textContent = text;
      bubble.appendChild(tail);
      c.appendChild(bubble);
      const right = box.x + box.width + 300 < innerWidth;
      Object.assign(c.style, { position: 'fixed', zIndex: '2147483620', pointerEvents: 'none', opacity: '0',
        transform: 'scale(.6)', transformOrigin: right ? 'left center' : 'top left',
        transition: 'opacity .25s ease, transform .45s cubic-bezier(.34,1.56,.64,1)' });
      Object.assign(bubble.style, { position: 'relative', maxWidth: '280px', background: '#111827', color: '#fff',
        font: '600 16px system-ui, sans-serif', padding: '10px 14px', borderRadius: '10px',
        boxShadow: '0 6px 14px rgba(0,0,0,.30),0 2px 4px rgba(0,0,0,.18)' });
      bubble.style.setProperty('--demo-float', String(float));
      if (float) bubble.style.animation = 'demo-hover 2.6s ease-in-out infinite';
      Object.assign(tail.style, { position: 'absolute', width: '12px', height: '12px', background: '#111827',
        transform: 'rotate(45deg)', borderRadius: '2px' });
      if (right) {
        c.style.left = box.x + box.width + 22 + 'px'; c.style.top = box.y + box.height / 2 - 20 + 'px';
        Object.assign(tail.style, { left: '-5px', top: '14px' });
      } else {
        c.style.left = Math.max(8, box.x + 12) + 'px'; c.style.top = box.y + box.height + 20 + 'px';
        Object.assign(tail.style, { left: '18px', top: '-5px' });
      }
      document.documentElement.appendChild(c);
      requestAnimationFrame(() => { c.style.opacity = '1'; c.style.transform = 'scale(1)'; });
      setTimeout(() => { c.style.transformOrigin = ''; c.style.transform = ''; c.style.transition = 'opacity .3s'; }, 500);
    }, { box, text, float });
    await wait(500);
    if (hold) { await wait(hold); await clearCallouts(); }
  }

  async function clearCallouts() {
    await page.evaluate(() => document.querySelectorAll('[data-demo-callout]').forEach((n) => { n.style.opacity = '0'; }));
    await wait(300);
    await page.evaluate(() => document.querySelectorAll('[data-demo-callout]').forEach((n) => n.remove()));
  }

  // Magnifies the page around the target. mood picks the feeling (see ZOOM); any field
  // can be overridden. hold: ms before zooming back (0 keeps it until unzoom()).
  // center (0..1) pulls the target toward the middle of the frame; fit caps the target's
  // zoomed size as a fraction of the frame. Spotlights and
  // callouts on screen zoom with the page.
  async function zoom(target, { mood = 'reveal', ...overrides } = {}) {
    const z = { center: 0.8, fit: 0.6, ...ZOOM.reveal, ...ZOOM[mood], ...overrides };
    const box = (await targetPoint(loc(target))).box;
    await page.evaluate(({ box, z }) => {
      const cx = box.x + box.width / 2, cy = box.y + box.height / 2;
      // Never magnify the target past z.fit of the frame, so it and its callout stay in view.
      z.scale = Math.min(z.scale, (innerWidth * z.fit) / box.width, (innerHeight * z.fit) / box.height);
      const apply = (n) => {
        const r = n.getBoundingClientRect();
        n.style.transition = `transform ${z.ms}ms ${z.easing}, opacity .4s`;
        n.style.transformOrigin = `${cx - r.left}px ${cy - r.top}px`;
        n.style.transform = `translate(${(innerWidth / 2 - cx) * z.center}px, ${(innerHeight / 2 - cy) * z.center}px) scale(${z.scale})`;
      };
      apply(document.body);
      document.querySelectorAll('[data-demo-spotlight],[data-demo-callout]').forEach(apply);
    }, { box, z });
    await wait(z.ms + 100);
    if (z.hold) { await wait(z.hold); await unzoom({ ms: z.outMs ?? 900 }); }
  }

  async function unzoom({ ms = 900 } = {}) {
    await page.evaluate((ms) => {
      [document.body, ...document.querySelectorAll('[data-demo-spotlight],[data-demo-callout]')].forEach((n) => {
        n.style.transition = `transform ${ms}ms cubic-bezier(.65,0,.35,1), opacity .4s`;
        n.style.transform = '';
      });
    }, ms);
    await wait(ms + 100);
  }

  // The cursor wanders slowly over an area, as if reading it.
  async function glance(target, { points = 3 } = {}) {
    const { box } = await targetPoint(loc(target));
    for (let i = 0; i < points; i++) {
      await moveTo(box.x + box.width * between(0.1, 0.9), box.y + box.height * between(0.15, 0.85),
        { curve: 0.25, overshoot: 0, wobble: 3, waves: 1, pace: 1.8, easing: 'easeInOut' });
      await wait(between(250, 500));
    }
  }

  async function saveEvents(path) {
    const { writeFile } = await import('node:fs/promises');
    await writeFile(path, JSON.stringify({ events }, null, 2));
  }

  return { moveTo, setMotion, hover, glance, click, type, press, select, chapter, spotlight, clearSpotlight,
    callout, clearCallouts, zoom, unzoom, pause: wait, events, saveEvents };
}


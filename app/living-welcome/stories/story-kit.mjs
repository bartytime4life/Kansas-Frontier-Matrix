// Shared helpers for "The Kansas record" story visuals. The contract for a story module, ./<id>.jsx:
//
//   export default function Story({ bundle, mode, paused, reduced, time, onTime, controls, onControls })
//   export function range(bundle)   // optional: { min, max, step, label, format(value), rate }, enables the scrubber
//   export function toCSV(bundle, { time, controls })   // optional: { filename, rows: [[...], ...] }
//
//   mode     'card' is a living thumbnail; 'lab' is the full instrument.
//   bundle   the JSON the pipeline built; bundle.data is the builder's result. Derive models once per bundle, in a
//            WeakMap, so that a card's first paint is under 50 ms.
//   paused || reduced   a single composed frame with no animation loop. useStoryCanvas handles this, along with
//            offscreen and hidden-tab stops, when the story passes held={paused||reduced}.
//   time, onTime, controls, onControls   lab state owned by StoryLab. Merge controls over the story's defaults.
//
// Rules: Canvas 2D, SVG or raw WebGL2; no new dependencies; no fetch, video, remote images or AI calls. Colour is never the
// only cue. Everything here stays inside the welcome's 32 MiB heap budget, so keep models compact.
import { createElement as h, useEffect, useRef } from 'react';

export const clamp = (value, min = 0, max = 1) => Math.min(max, Math.max(min, value));
export const lerp = (a, b, t) => a + (b - a) * t;
export const ease = Object.freeze({
  linear: t => t,
  outCubic: t => 1 - (1 - t) ** 3,
  inOutCubic: t => (t < .5 ? 4 * t ** 3 : 1 - (-2 * t + 2) ** 3 / 2),
  outExpo: t => (t >= 1 ? 1 : 1 - 2 ** (-10 * t)),
});

// --- Perceptual colour scales: functions over 0..1 returning an rgb() string --------------------------------------
function scale(stops) {
  const last = stops.length - 1;
  return t => {
    const at = clamp(Number.isFinite(t) ? t : 0) * last, index = Math.min(last - 1, Math.floor(at)), f = at - index;
    const a = stops[index], b = stops[index + 1];
    return `rgb(${Math.round(lerp(a[0], b[0], f))},${Math.round(lerp(a[1], b[1], f))},${Math.round(lerp(a[2], b[2], f))})`;
  };
}
export const viridis = scale([[68, 1, 84], [71, 44, 122], [59, 81, 139], [44, 113, 142], [33, 144, 141], [39, 173, 129], [92, 200, 99], [170, 220, 50], [253, 231, 37]]);
export const magma = scale([[0, 0, 4], [28, 16, 68], [79, 18, 123], [129, 37, 129], [181, 54, 122], [229, 80, 100], [251, 135, 97], [254, 194, 135], [252, 253, 191]]);
export const cividis = scale([[0, 34, 78], [18, 53, 112], [59, 73, 108], [87, 92, 109], [112, 113, 115], [138, 134, 120], [165, 156, 116], [195, 180, 104], [254, 232, 56]]);
// Diverging around .5. Both ends stay distinct in lightness, so a stripe's sign also reads in greyscale.
export const divergingBlueRed = scale([[5, 48, 97], [33, 102, 172], [67, 147, 195], [146, 197, 222], [240, 240, 236], [244, 165, 130], [214, 96, 77], [178, 24, 43], [103, 0, 31]]);
export const divergingBrownTeal = scale([[84, 48, 5], [140, 81, 10], [191, 129, 45], [223, 194, 125], [240, 240, 236], [128, 205, 193], [53, 151, 143], [1, 102, 94], [0, 60, 48]]);

// --- Kansas ---------------------------------------------------------------------------------------------------------
// The state line as [lon, lat]: the union of the 105 modern counties in the Newberry Atlas of Historical County
// Boundaries (kfm_ahcb_county_versions, verified snapshot of 2026-11-03), generalized to 0.012 degrees for display.
export const KANSAS_OUTLINE = Object.freeze([[-94.97,39.419],[-94.937,39.387],[-94.882,39.386],[-94.91,39.353],[-94.905,39.31],[-94.831,39.256],[-94.824,39.21],[-94.783,39.207],[-94.742,39.17],[-94.68,39.184],[-94.662,39.158],[-94.592,39.155],[-94.607,39.113],[-94.618,36.998],[-102.042,36.993],[-102.052,40.003],[-95.308,40.0],[-95.25,39.949],[-95.204,39.939],[-95.198,39.902],[-95.15,39.906],[-95.137,39.878],[-95.082,39.862],[-95.032,39.868],[-95.013,39.9],[-94.952,39.901],[-94.928,39.886],[-94.938,39.85],[-94.878,39.825],[-94.884,39.794],[-94.936,39.779],[-94.911,39.759],[-94.867,39.772],[-94.87,39.735],[-94.901,39.724],[-94.963,39.741],[-94.971,39.686],[-95.018,39.673],[-95.05,39.638],[-95.053,39.585],[-95.101,39.579],[-95.113,39.559],[-95.041,39.466],[-94.972,39.421]]);
export const KANSAS_OUTLINE_CREDIT = 'Kansas outline generalized from the Newberry Atlas of Historical County Boundaries.';
export const KANSAS_BOUNDS = Object.freeze({ west: -102.052, east: -94.592, south: 36.993, north: 40.003 });

/** Lon/lat to canvas pixels, keeping Kansas's aspect at its middle latitude. Padding is in pixels. */
export function kansasProjection(width, height, { padding = 8, bounds = KANSAS_BOUNDS } = {}) {
  const mid = (bounds.south + bounds.north) / 2, k = Math.cos(mid * Math.PI / 180);
  const spanX = (bounds.east - bounds.west) * k, spanY = bounds.north - bounds.south;
  const s = Math.max(.001, Math.min((width - padding * 2) / spanX, (height - padding * 2) / spanY));
  const left = (width - spanX * s) / 2, top = (height - spanY * s) / 2;
  const x = lon => left + (lon - bounds.west) * k * s, y = lat => top + (bounds.north - lat) * s;
  return { x, y, scale: s, k, invert: (px, py) => [(px - left) / (k * s) + bounds.west, bounds.north - (py - top) / s] };
}
export function kansasPath(projection) {
  const path = new Path2D();
  KANSAS_OUTLINE.forEach(([lon, lat], index) => (index ? path.lineTo(projection.x(lon), projection.y(lat)) : path.moveTo(projection.x(lon), projection.y(lat))));
  path.closePath();
  return path;
}
/** Reverses grid_path() from tools/local_data/stories: flat [x0, y0, dx1, dy1, ...] to flat [lon, lat, ...]. */
export function decodeGridPath(path, origin, unit) {
  const out = new Float32Array(path.length);
  let x = 0, y = 0;
  for (let i = 0; i < path.length; i += 2) {
    x += path[i]; y += path[i + 1];
    out[i] = origin[0] + x * unit; out[i + 1] = origin[1] + y * unit;
  }
  return out;
}

// --- Numbers and text ---------------------------------------------------------------------------------------------
const numberFormats = new Map();
export function fmt(value, { digits = 0, unit = '', sign = false } = {}) {
  if (value === null || value === undefined || !Number.isFinite(value)) return '—';
  const key = `${digits}${sign}`;
  if (!numberFormats.has(key)) numberFormats.set(key, new Intl.NumberFormat('en-US', { minimumFractionDigits: digits, maximumFractionDigits: digits, signDisplay: sign ? 'exceptZero' : 'auto' }));
  return numberFormats.get(key).format(value).replace('-', '−') + (unit ? (unit === '°F' ? unit : ` ${unit}`) : '');
}
/** Canvas text with fixed-width digits, so a running counter does not jitter. */
export function fillTabular(ctx, text, x, y) {
  const value = String(text), digit = ctx.measureText('0').width;
  const widths = [...value].map(ch => (/\d/.test(ch) ? digit : ctx.measureText(ch).width));
  const total = widths.reduce((a, b) => a + b, 0), align = ctx.textAlign, saved = ctx.textAlign;
  let at = align === 'right' || align === 'end' ? x - total : align === 'center' ? x - total / 2 : x;
  ctx.textAlign = 'left';
  [...value].forEach((ch, index) => { ctx.fillText(ch, at + (widths[index] - ctx.measureText(ch).width) / 2, y); at += widths[index]; });
  ctx.textAlign = saved;
}

// --- Canvas effects ------------------------------------------------------------------------------------------------
/** Draws with additive light and a soft halo. fn does the stroking or filling. */
export function glow(ctx, color, blur, fn) {
  ctx.save();
  ctx.globalCompositeOperation = 'lighter';
  ctx.shadowColor = color;
  ctx.shadowBlur = blur;
  fn(ctx);
  ctx.restore();
}
const grainCache = new Map();
function seededRandom(seed) {
  let s = seed >>> 0 || 1;
  return () => { s ^= s << 13; s ^= s >>> 17; s ^= s << 5; return (s >>> 0) / 4294967296; };
}
/** A small seeded noise tile, shared by every canvas. */
export function drawGrain(ctx, width, height, alpha = .05, seed = 7) {
  if (typeof document === 'undefined') return;
  let tile = grainCache.get(seed);
  if (!tile) {
    tile = document.createElement('canvas'); tile.width = tile.height = 96;
    const c = tile.getContext('2d'), image = c.createImageData(96, 96), random = seededRandom(seed);
    for (let i = 0; i < image.data.length; i += 4) { const v = random() * 255; image.data[i] = image.data[i + 1] = image.data[i + 2] = v; image.data[i + 3] = 255; }
    c.putImageData(image, 0, 0);
    grainCache.set(seed, tile);
  }
  ctx.save();
  ctx.globalAlpha = alpha;
  ctx.globalCompositeOperation = 'overlay';
  ctx.fillStyle = ctx.createPattern(tile, 'repeat');
  ctx.fillRect(0, 0, width, height);
  ctx.restore();
}
/** A faint moving sketch for a card that is waiting for its data. Deterministic for a story id. Its still parts are kept in `cache`. */
export function drawWaitingSketch(ctx, { w, h, dpr = 1, t, still, palette, seed, cache = {} }) {
  const [ground, light, accent] = palette;
  if (cache.w !== w || cache.h !== h || cache.dpr !== dpr) {
    const base = document.createElement('canvas');
    base.width = Math.round(w * dpr); base.height = Math.round(h * dpr);
    const c = base.getContext('2d'), projection = kansasProjection(w, h, { padding: Math.max(10, w * .06) });
    c.setTransform(dpr, 0, 0, dpr, 0, 0);
    c.fillStyle = ground; c.fillRect(0, 0, w, h);
    const outline = kansasPath(projection);
    c.strokeStyle = light; c.globalAlpha = .28; c.lineWidth = 1; c.stroke(outline); c.globalAlpha = 1;
    drawGrain(c, w, h, .05, seed);
    const random = seededRandom(seed);
    cache.lines = Array.from({ length: 9 }, () => ({ phase: random() * Math.PI * 2, y: h * (.15 + .7 * random()), rate: .25 + random() * .35 }));
    Object.assign(cache, { w, h, dpr, base, outline });
  }
  ctx.drawImage(cache.base, 0, 0, w, h);
  ctx.save(); ctx.clip(cache.outline);
  cache.lines.forEach(({ phase, y, rate }, index) => {
    const reveal = still ? 1 : (Math.sin(t * rate + phase) + 1) / 2, drift = still ? 0 : t * .3;
    ctx.beginPath();
    for (let step = 0; step <= 24; step++) {
      const f = step / 24, wave = Math.sin(f * 7 + phase + drift) * h * .05;
      if (f > reveal) break;
      if (step) ctx.lineTo(w * f, y + wave); else ctx.moveTo(w * f, y + wave);
    }
    ctx.strokeStyle = index % 3 ? light : accent; ctx.globalAlpha = .16 + .14 * reveal; ctx.lineWidth = 1.2; ctx.stroke();
  });
  ctx.restore(); ctx.globalAlpha = 1;
}
export const hashSeed = text => [...String(text)].reduce((hash, ch) => (Math.imul(hash, 31) + ch.charCodeAt(0)) | 0, 7) >>> 0;

// --- Hit testing ----------------------------------------------------------------------------------------------------
/** A coarse grid over a canvas. add() registers an id under a box; near() lists ids around a point. */
export function hitGrid(width, height, cell = 24) {
  const columns = Math.max(1, Math.ceil(width / cell)), rows = Math.max(1, Math.ceil(height / cell)), cells = new Map();
  return {
    add(id, x0, y0, x1, y1) {
      const c0 = clamp(Math.floor(Math.min(x0, x1) / cell), 0, columns - 1), c1 = clamp(Math.floor(Math.max(x0, x1) / cell), 0, columns - 1);
      const r0 = clamp(Math.floor(Math.min(y0, y1) / cell), 0, rows - 1), r1 = clamp(Math.floor(Math.max(y0, y1) / cell), 0, rows - 1);
      for (let r = r0; r <= r1; r++) for (let c = c0; c <= c1; c++) { const key = r * columns + c; if (!cells.has(key)) cells.set(key, []); cells.get(key).push(id); }
    },
    near(x, y, radius = cell) {
      const found = new Set(), c0 = Math.floor((x - radius) / cell), c1 = Math.floor((x + radius) / cell), r0 = Math.floor((y - radius) / cell), r1 = Math.floor((y + radius) / cell);
      for (let r = Math.max(0, r0); r <= Math.min(rows - 1, r1); r++) for (let c = Math.max(0, c0); c <= Math.min(columns - 1, c1); c++) for (const id of cells.get(r * columns + c) || []) found.add(id);
      return found;
    },
  };
}
export function distanceToSegment(px, py, ax, ay, bx, by) {
  const dx = bx - ax, dy = by - ay, span = dx * dx + dy * dy, t = span ? clamp(((px - ax) * dx + (py - ay) * dy) / span) : 0;
  return Math.hypot(px - ax - t * dx, py - ay - t * dy);
}

// --- CSV ------------------------------------------------------------------------------------------------------------
export function csvText(rows) {
  const cell = value => { const text = value === null || value === undefined ? '' : String(value); return /[",\n\r]/.test(text) ? `"${text.replaceAll('"', '""')}"` : text; };
  return rows.map(row => row.map(cell).join(',')).join('\r\n') + '\r\n';
}
export function downloadCSV(filename, rows) {
  const url = URL.createObjectURL(new Blob([csvText(rows)], { type: 'text/csv;charset=utf-8' })), link = document.createElement('a');
  link.href = url; link.download = filename; link.style.display = 'none';
  document.body.append(link); link.click(); link.remove();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}

// --- The canvas hook ------------------------------------------------------------------------------------------------
/** The nearest scrolling ancestor: an IntersectionObserver's root, since the welcome scrolls inside itself. */
export function scrollParent(node) {
  for (let at = node?.parentElement; at; at = at.parentElement) {
    const overflow = getComputedStyle(at).overflowY;
    if (overflow === 'auto' || overflow === 'scroll') return at;
  }
  return null;
}

/**
 * Sizes a canvas to its CSS box at devicePixelRatio (capped at 2) and paints it.
 * draw(ctx, { w, h, dpr, t, still }) is in CSS pixels. t is seconds of animation, kept across a pause. still is true
 * for a composed static frame, and a story must then draw its finished state.
 * animate: run a frame loop, which also stops while held, offscreen or the tab is hidden. deps: repaint on change.
 */
export function useStoryCanvas({ draw, animate = false, held = false, fps = 30, deps = [] }) {
  const ref = useRef(null), latest = useRef(draw), run = useRef(animate && !held);
  useEffect(() => { latest.current = draw; });
  useEffect(() => { run.current = animate && !held; }, [animate, held]);
  useEffect(() => {
    const canvas = ref.current;
    if (!canvas) return undefined;
    const ctx = canvas.getContext('2d');
    if (!ctx) return undefined;
    let w = 0, h = 0, dpr = 1, frame = 0, onscreen = false, t = canvas.__storyT || 0, last = 0, sized = false;
    const paint = still => {
      if (!sized) return;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      latest.current(ctx, { w, h, dpr, t, still });
    };
    const interval = 1000 / fps;
    const shouldRun = () => run.current && onscreen && sized && !document.hidden;
    const tick = now => {
      frame = 0;
      if (!shouldRun()) return;
      frame = requestAnimationFrame(tick);
      const delta = now - last;
      if (delta < interval - 1) return;
      last = now - (delta % interval);
      t += Math.min(delta, 100) / 1000;
      canvas.__storyT = t;
      paint(false);
    };
    const settle = () => {
      if (shouldRun()) { if (!frame) { last = performance.now(); paint(false); frame = requestAnimationFrame(tick); } }
      else {
        if (frame) { cancelAnimationFrame(frame); frame = 0; }
        paint(!animate || !run.current || !onscreen || document.hidden);
      }
    };
    const resize = () => {
      const box = canvas.getBoundingClientRect(), nextDpr = Math.min(2, window.devicePixelRatio || 1);
      const nextW = Math.round(box.width), nextH = Math.round(box.height);
      if (!nextW || !nextH) return;
      if (nextW === w && nextH === h && nextDpr === dpr) return;
      w = nextW; h = nextH; dpr = nextDpr; sized = true;
      canvas.width = Math.round(w * dpr); canvas.height = Math.round(h * dpr);
      settle();
    };
    const sizes = new ResizeObserver(resize);
    sizes.observe(canvas);
    resize();
    const sight = new IntersectionObserver(entries => { onscreen = entries.at(-1).isIntersecting; settle(); }, { root: scrollParent(canvas), threshold: 0 });
    sight.observe(canvas);
    document.addEventListener('visibilitychange', settle);
    canvas.__storySettle = settle;
    return () => {
      if (frame) cancelAnimationFrame(frame);
      sizes.disconnect(); sight.disconnect();
      document.removeEventListener('visibilitychange', settle);
      canvas.__storySettle = undefined;
    };
  }, [fps, animate, held]);
  // Repaint without touching the canvas's size, so that a hover does not reallocate it.
  // eslint-disable-next-line react-hooks/exhaustive-deps -- deps is the caller's list of repaint triggers
  useEffect(() => { ref.current?.__storySettle?.(); }, deps);
  return ref;
}

// --- Small shared controls ------------------------------------------------------------------------------------------
export function Segmented({ label, options, value, onChange, disabled = false }) {
  return h('div', { className: 'story-segmented', role: 'group', 'aria-label': label },
    h('span', { className: 'story-segmented-label', 'aria-hidden': 'true' }, label),
    h('div', { className: 'story-segmented-options' }, options.map(option => h('button', {
      type: 'button', key: option.id, 'aria-pressed': value === option.id, disabled, onClick: () => onChange(option.id),
    }, option.label))));
}
/** items: [{ label, color, dash }] for categories, or ramp: { scale, from, to } for a continuous key. */
export function Legend({ title, items, ramp }) {
  return h('figure', { className: 'story-legend' },
    title ? h('figcaption', null, title) : null,
    ramp ? h('div', { className: 'story-legend-ramp' },
      h('span', { className: 'story-num' }, ramp.from),
      h('i', { 'aria-hidden': 'true', style: { background: `linear-gradient(90deg,${[0, .125, .25, .375, .5, .625, .75, .875, 1].map(ramp.scale).join(',')})` } }),
      h('span', { className: 'story-num' }, ramp.to)) : null,
    items ? h('ul', null, items.map(item => h('li', { key: item.label },
      h('i', { 'aria-hidden': 'true', 'data-dash': item.dash ? 'true' : undefined, style: { borderColor: item.color } }), item.label))) : null);
}
export function Readout({ children }) {
  return h('p', { className: 'story-readout', role: 'status', 'aria-live': 'polite' }, children);
}
export function Summary({ children }) {
  return h('p', { className: 'sr-only story-summary' }, children);
}

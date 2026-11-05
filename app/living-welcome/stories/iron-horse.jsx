'use client';
import { useRef, useState } from 'react';
import { Legend, Readout, Segmented, Summary, clamp, decodeGridPath, distanceToSegment, drawGrain, ease, fillTabular, fmt, glow, hitGrid, kansasPath, kansasProjection, magma, useStoryCanvas } from './story-kit.mjs';

const GROUND = '#0f1720', LIGHT = '#f2b134', EMBER = '#e05d3a';
const DEFAULTS = Object.freeze({ color: 'year', extent: 'kansas' });
// Wide enough for the lines that reach past the state line.
const WIDE_BOUNDS = Object.freeze({ west: -102.6, east: -93.9, south: 36.45, north: 40.55 });
const models = new WeakMap();

function modelOf(bundle) {
  let model = models.get(bundle);
  if (model) return model;
  const data = bundle.data, { origin, unit } = data.grid, standard = data.gauges.findIndex(g => g > 0);
  const lines = data.lines.map(([year, state, name, gauge, miles, path], id) => ({
    id, year: data.years[year], yearIndex: year, state: data.states[state], kansas: state === data.kansasState,
    name: data.names[name], gauge: data.gauges[gauge], gauged: gauge === standard && standard >= 0, miles,
    points: decodeGridPath(path, origin, unit),
  }));
  model = { data, lines, byYear: data.years.map((_, index) => lines.filter(line => line.yearIndex === index)), first: data.years[0], last: data.years.at(-1), rows: data.milesByYear };
  models.set(bundle, model);
  return model;
}
const totalAt = (model, year) => { let row = null; for (const entry of model.rows) { if (entry.year <= year) row = entry; else break; } return row; };

function trace(target, points, projection) {
  target.moveTo(projection.x(points[0]), projection.y(points[1]));
  for (let i = 2; i < points.length; i += 2) target.lineTo(projection.x(points[i]), projection.y(points[i + 1]));
}
function linePath(line, projection) {
  const path = new Path2D();
  trace(path, line.points, projection);
  return path;
}
function pathLength(points, projection) {
  let total = 0;
  for (let i = 2; i < points.length; i += 2) total += Math.hypot(projection.x(points[i]) - projection.x(points[i - 2]), projection.y(points[i + 1]) - projection.y(points[i - 1]));
  return total;
}

// --- The card: track draws itself in warm light, one benchmark at a time ---------------------------------------
const SECONDS_PER_BENCHMARK = .95, HOLD_SECONDS = 3.2;

function cardScene(model, w, h, dpr) {
  const projection = kansasProjection(w, h, { padding: Math.max(8, w * .05) }), outline = kansasPath(projection);
  const base = document.createElement('canvas');
  base.width = Math.round(w * dpr); base.height = Math.round(h * dpr);
  const b = base.getContext('2d');
  b.setTransform(dpr, 0, 0, dpr, 0, 0);
  const wash = b.createRadialGradient(w * .55, h * .35, 0, w * .55, h * .35, w * .8);
  wash.addColorStop(0, '#1a2a38'); wash.addColorStop(1, GROUND);
  b.fillStyle = wash; b.fillRect(0, 0, w, h);
  b.fillStyle = '#ffffff0b'; b.fill(outline);
  b.strokeStyle = '#d8c58f55'; b.lineWidth = 1; b.stroke(outline);
  drawGrain(b, w, h, .07, 11);
  const kansas = model.lines.filter(line => line.kansas);
  const years = model.byYear.map(group => group.filter(line => line.kansas).map(line => ({ path: linePath(line, projection), length: Math.max(1, pathLength(line.points, projection)) })));
  return { w, h, dpr, base, settled: null, reached: -1, years, projection, kansas };
}
function settle(scene, index) {
  if (!scene.settled) {
    scene.settled = document.createElement('canvas');
    scene.settled.width = scene.base.width; scene.settled.height = scene.base.height;
    scene.reached = -1;
  }
  const c = scene.settled.getContext('2d');
  if (index < scene.reached) { c.setTransform(1, 0, 0, 1, 0, 0); c.clearRect(0, 0, scene.settled.width, scene.settled.height); scene.reached = -1; }
  c.setTransform(scene.dpr, 0, 0, scene.dpr, 0, 0);
  c.lineCap = 'round'; c.lineJoin = 'round';
  for (let i = scene.reached + 1; i <= index; i++) {
    c.strokeStyle = LIGHT; c.globalAlpha = .9; c.lineWidth = 1.05;
    for (const line of scene.years[i] || []) c.stroke(line.path);
  }
  scene.reached = index;
}
function drawCard(ctx, model, scene, { t, still }) {
  const { w, h } = scene, count = model.byYear.length, cycle = count * SECONDS_PER_BENCHMARK + HOLD_SECONDS;
  const at = still ? count : Math.min(count, (t % cycle) / SECONDS_PER_BENCHMARK);
  const index = Math.floor(at), progress = ease.outCubic(at - index);
  ctx.drawImage(scene.base, 0, 0, w, h);
  settle(scene, index - 1);
  if (index > 0 && scene.settled) {
    ctx.drawImage(scene.settled, 0, 0, w, h);
    if (still) { ctx.save(); ctx.globalCompositeOperation = 'lighter'; ctx.globalAlpha = .3; ctx.filter = 'blur(2px)'; ctx.drawImage(scene.settled, 0, 0, w, h); ctx.restore(); }
  }
  if (index < count && !still) {
    // The front of the new track: a wide faint stroke under a thin bright one. A canvas shadow here would cost
    // far too much per frame on a phone.
    ctx.save();
    ctx.lineCap = 'round'; ctx.lineJoin = 'round'; ctx.globalCompositeOperation = 'lighter';
    for (const [style, width] of [[`${EMBER}55`, 4], ['#ffd98a', 1.4]]) {
      ctx.strokeStyle = style; ctx.lineWidth = width;
      for (const line of scene.years[index] || []) { ctx.setLineDash([line.length * progress, line.length]); ctx.stroke(line.path); }
    }
    ctx.restore();
  }
  const year = model.data.years[Math.min(count - 1, index)];
  ctx.fillStyle = '#efd395'; ctx.font = `600 ${Math.round(clamp(w * .055, 12, 20))}px ui-sans-serif,system-ui,sans-serif`; ctx.textAlign = 'left'; ctx.textBaseline = 'alphabetic';
  fillTabular(ctx, String(year), 10, h - 7);
}
function Card({ bundle, held }) {
  const model = modelOf(bundle), scene = useRef(null);
  const ref = useStoryCanvas({
    animate: true, held, fps: 30, deps: [bundle],
    draw(ctx, frame) {
      if (scene.current?.w !== frame.w || scene.current?.h !== frame.h || scene.current?.dpr !== frame.dpr) scene.current = cardScene(model, frame.w, frame.h, frame.dpr);
      drawCard(ctx, model, scene.current, frame);
    },
  });
  return <canvas ref={ref} className="story-canvas" aria-hidden="true"/>;
}

// --- The lab -----------------------------------------------------------------------------------------------------
function colourOf(line, model, color) {
  if (color === 'gauge') return line.gauged ? LIGHT : '#8ea3ad';
  return magma(.35 + .62 * ((line.year - model.first) / Math.max(1, model.last - model.first)));
}
function drawMap(ctx, { w, h }, model, year, controls, hover, grid) {
  const wide = controls.extent === 'neighbours', projection = kansasProjection(w, h, { padding: 10, bounds: wide ? WIDE_BOUNDS : undefined });
  ctx.fillStyle = GROUND; ctx.fillRect(0, 0, w, h);
  const outline = kansasPath(projection);
  ctx.fillStyle = '#ffffff09'; ctx.fill(outline);
  ctx.strokeStyle = '#d8c58f66'; ctx.lineWidth = 1; ctx.stroke(outline);
  ctx.lineCap = 'round'; ctx.lineJoin = 'round';
  const shown = model.lines.filter(line => line.year <= year && (wide || line.kansas));
  const newest = model.data.years.filter(y => y <= year).at(-1);
  for (const line of shown) {
    const fresh = line.year === newest;
    ctx.beginPath(); trace(ctx, line.points, projection);
    ctx.setLineDash(line.kansas ? [] : [3, 3]);
    ctx.strokeStyle = colourOf(line, model, controls.color);
    ctx.globalAlpha = line.kansas ? (fresh ? 1 : .78) : .5;
    ctx.lineWidth = controls.color === 'gauge' && line.gauged ? 2.4 : fresh ? 1.9 : 1.15;
    ctx.stroke();
  }
  ctx.globalAlpha = 1; ctx.setLineDash([]);
  const active = hover === null ? null : shown.find(line => line.id === hover);
  if (active) {
    glow(ctx, '#ffffff', 8, c => { c.beginPath(); trace(c, active.points, projection); c.strokeStyle = '#fff'; c.lineWidth = 2.6; c.stroke(); });
  }
  drawGrain(ctx, w, h, .05, 11);
  ctx.fillStyle = '#efd395'; ctx.font = `600 ${Math.round(clamp(w * .045, 18, 34))}px ui-sans-serif,system-ui,sans-serif`; ctx.textAlign = 'right'; ctx.textBaseline = 'alphabetic';
  fillTabular(ctx, String(year), w - 12, h - 12);
  if (grid) {
    grid.current = { index: hitGrid(w, h, 20), projection, shown };
    for (const line of shown) {
      const p = line.points;
      for (let i = 2; i < p.length; i += 2) grid.current.index.add(line.id, projection.x(p[i - 2]), projection.y(p[i - 1]), projection.x(p[i]), projection.y(p[i + 1]));
    }
  }
}
function nearestLine(grid, x, y, reach) {
  if (!grid) return null;
  const { index, projection, shown } = grid, ids = index.near(x, y, reach);
  let best = null, bestDistance = reach;
  for (const line of shown) {
    if (!ids.has(line.id)) continue;
    const p = line.points;
    for (let i = 2; i < p.length; i += 2) {
      const d = distanceToSegment(x, y, projection.x(p[i - 2]), projection.y(p[i - 1]), projection.x(p[i]), projection.y(p[i + 1]));
      if (d < bestDistance) { best = line.id; bestDistance = d; }
    }
  }
  return best;
}
function drawChart(ctx, { w, h }, model, year, extent) {
  const pad = { left: 46, right: 10, top: 12, bottom: 22 }, rows = model.rows, x0 = model.first, x1 = model.last;
  const total = row => row.kansasTotal + (extent === 'neighbours' ? row.neighboursTotal : 0), top = Math.max(1, total(rows.at(-1)));
  const x = value => pad.left + (value - x0) / Math.max(1, x1 - x0) * (w - pad.left - pad.right), y = value => h - pad.bottom - value / top * (h - pad.top - pad.bottom);
  ctx.clearRect(0, 0, w, h);
  ctx.font = '11px ui-sans-serif,system-ui,sans-serif'; ctx.textBaseline = 'middle'; ctx.fillStyle = '#a9bdc4'; ctx.textAlign = 'right';
  for (let tick = 0; tick <= 4; tick++) {
    const value = top * tick / 4, py = y(value);
    ctx.strokeStyle = '#ffffff14'; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(pad.left, py); ctx.lineTo(w - pad.right, py); ctx.stroke();
    fillTabular(ctx, fmt(value), pad.left - 6, py);
  }
  ctx.textAlign = 'center'; ctx.textBaseline = 'top';
  for (const tick of [1870, 1880, 1890, 1900, 1910]) if (tick >= x0 && tick <= x1) fillTabular(ctx, String(tick), x(tick), h - pad.bottom + 6);
  let level = y(0);
  ctx.beginPath(); ctx.moveTo(x(x0), level);
  for (const row of rows) { ctx.lineTo(x(row.year), level); level = y(total(row)); ctx.lineTo(x(row.year), level); }
  ctx.lineTo(x(x1), level);
  ctx.strokeStyle = LIGHT; ctx.lineWidth = 2; ctx.stroke();
  for (const row of rows) {
    ctx.fillStyle = row.year <= year ? LIGHT : '#ffffff33';
    ctx.beginPath(); ctx.arc(x(row.year), y(total(row)), 3, 0, Math.PI * 2); ctx.fill();
  }
  ctx.strokeStyle = EMBER; ctx.lineWidth = 1.5; ctx.beginPath(); ctx.moveTo(x(year), pad.top); ctx.lineTo(x(year), h - pad.bottom); ctx.stroke();
  return { x, invert: px => x0 + (px - pad.left) / Math.max(1, w - pad.left - pad.right) * (x1 - x0), left: pad.left, right: w - pad.right };
}
function Lab({ bundle, time, onTime, controls, onControls }) {
  const model = modelOf(bundle), settings = { ...DEFAULTS, ...controls }, year = clamp(Math.round(time ?? model.last), model.first, model.last);
  const [hover, setHover] = useState(null), grid = useRef(null), chart = useRef(null);
  const map = useStoryCanvas({ deps: [bundle, year, settings.color, settings.extent, hover], draw: (ctx, frame) => drawMap(ctx, frame, model, year, settings, hover, grid) });
  const plot = useStoryCanvas({ deps: [bundle, year, settings.extent], draw: (ctx, frame) => { chart.current = drawChart(ctx, frame, model, year, settings.extent); } });
  const active = hover === null ? null : model.lines[hover], row = totalAt(model, year);
  const shownTotal = row ? row.kansasTotal + (settings.extent === 'neighbours' ? row.neighboursTotal : 0) : 0;
  const counts = model.data.counts;
  const pick = event => {
    const box = event.currentTarget.getBoundingClientRect();
    setHover(nearestLine(grid.current, event.clientX - box.left, event.clientY - box.top, event.pointerType === 'touch' ? 22 : 10));
  };
  const scrub = event => {
    if (!chart.current || (event.type === 'pointermove' && !event.buttons)) return;
    const box = event.currentTarget.getBoundingClientRect(), value = chart.current.invert(event.clientX - box.left);
    onTime?.(clamp(Math.round(value), model.first, model.last));
  };
  const legend = settings.color === 'gauge'
    ? [{ label: `Gauge recorded, 56.5 in (${fmt(counts.gauged)} segments)`, color: LIGHT }, { label: `Gauge blank in the file (${fmt(counts.segments - counts.gauged)})`, color: '#8ea3ad' }]
    : null;
  const summary = `Railroad map of Kansas. By the ${row?.year ?? model.first} benchmark, Atack's file shows ${fmt(row?.kansasTotal ?? 0)} miles of track tagged Kansas. It reaches ${fmt(model.rows.at(-1).kansasTotal)} miles at the ${model.last} benchmark.`;
  return <div className="story-lab-layout">
    <div className="story-lab-main"><canvas ref={map} className="story-canvas story-map" role="img" aria-label={summary} onPointerMove={pick} onPointerDown={pick} onPointerLeave={() => setHover(null)}/></div>
    <aside className="story-lab-side" aria-label="Railroad tools">
      <section className="story-panel">
        <p className="story-kicker">In operation by {row?.year ?? '—'}</p>
        <p className="story-stat"><strong className="story-num">{fmt(shownTotal)}</strong> miles{settings.extent === 'neighbours' ? ', with neighbours' : ' tagged Kansas'}</p>
        <canvas ref={plot} className="story-canvas story-chart" aria-hidden="true" onPointerDown={scrub} onPointerMove={scrub}/>
        <p className="story-note">Cumulative miles at each of the file’s {model.data.years.length} benchmarks. Drag to set the year.</p>
      </section>
      <section className="story-panel">
        <Segmented label="Colour" value={settings.color} onChange={color => onControls?.({ ...settings, color })} options={[{ id: 'year', label: 'First year' }, { id: 'gauge', label: 'Gauge' }]}/>
        <Segmented label="Show" value={settings.extent} onChange={extent => onControls?.({ ...settings, extent })} options={[{ id: 'kansas', label: 'Kansas only' }, { id: 'neighbours', label: 'With neighbours' }]}/>
        {legend ? <Legend title="Line colour" items={legend}/> : <Legend title="First year in operation" ramp={{ scale: t => magma(.35 + .62 * t), from: model.first, to: model.last }}/>}
        {settings.extent === 'neighbours' && <Legend items={[{ label: 'Dashed: tagged a neighbouring state', color: '#a9bdc4', dash: true }]}/>}
      </section>
      <section className="story-panel">
        <Readout>{active
          ? <>In operation by <span className="story-num">{active.year}</span> · {active.state} · <span className="story-num">{fmt(active.miles, { digits: 1 })}</span> mi · {active.name || 'Railroad name blank in the file'} · {active.gauged ? `Gauge ${active.gauge} in` : 'Gauge blank in the file'}</>
          : `Point at a line to read it. The file names ${fmt(counts.named)} of its ${fmt(counts.segments)} segments.`}</Readout>
      </section>
      <details className="story-panel story-table-wrap"><summary>Miles by benchmark</summary>
        <table className="story-table"><thead><tr><th scope="col">Year</th><th scope="col">Added</th><th scope="col">Kansas total</th></tr></thead>
          <tbody>{model.rows.map(entry => <tr key={entry.year} data-current={entry.year === row?.year || undefined}><th scope="row">{entry.year}</th><td>{fmt(entry.kansas, { digits: 1 })}</td><td>{fmt(entry.kansasTotal, { digits: 1 })}</td></tr>)}</tbody></table>
      </details>
    </aside>
    <Summary>{summary}</Summary>
  </div>;
}

export default function Story({ bundle, mode, paused, reduced, time, onTime, controls, onControls }) {
  if (!bundle?.data?.lines) return null;
  return mode === 'lab' ? <Lab bundle={bundle} time={time} onTime={onTime} controls={controls} onControls={onControls}/> : <Card bundle={bundle} held={Boolean(paused || reduced)}/>;
}
export function range(bundle) {
  const years = bundle.data.years;
  return { min: years[0], max: years.at(-1), step: 1, label: 'In operation by', format: value => String(value), rate: 3.5 };
}
export function toCSV(bundle) {
  const header = ['benchmark_year', 'kansas_miles_added', 'kansas_miles_total', 'neighbour_miles_added', 'neighbour_miles_total', 'kansas_segments', 'neighbour_segments'];
  return { filename: 'iron-horse-miles-by-benchmark.csv', rows: [header, ...bundle.data.milesByYear.map(row => [row.year, row.kansas, row.kansasTotal, row.neighbours, row.neighboursTotal, row.kansasSegments, row.neighbourSegments])] };
}

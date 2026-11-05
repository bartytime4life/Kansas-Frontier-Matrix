'use client';
import { useRef, useState } from 'react';
import { Legend, Readout, Segmented, Summary, clamp, divergingBlueRed, divergingBrownTeal, drawGrain, ease, fillTabular, fmt, useStoryCanvas } from './story-kit.mjs';

const GROUND = '#0c1420', STATE = '20';
const DEFAULTS = Object.freeze({ element: 'tmpc', baseline: '1901-2000', area: STATE });
const MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
const models = new WeakMap();

function modelOf(bundle) {
  let model = models.get(bundle);
  if (!model) { model = { data: bundle.data, annual: new Map() }; models.set(bundle, model); }
  return model;
}
/** One value per year for an area. The anomaly compares only the months the year has with the same months of the baseline. */
function annualOf(model, element, area, baseline) {
  const key = `${element}/${area}/${baseline}`;
  if (model.annual.has(key)) return model.annual.get(key);
  const { years, values, normals, elements } = model.data, spec = elements[element], factor = spec.scale;
  const flat = values[element]?.[area] || [], normal = element === 'pdsi' ? null : normals[baseline]?.[element]?.[area] || null;
  const sum = spec.annual === 'sum';
  const rows = years.map((year, index) => {
    let total = 0, reference = 0, months = 0;
    for (let m = 0; m < 12; m++) {
      const v = flat[index * 12 + m];
      if (v === null || v === undefined) continue;
      total += v; months += 1;
      if (normal) reference += normal[m] ?? 0;
    }
    if (!months) return { year, value: null, anomaly: null, months: 0 };
    const value = (sum ? total : total / months) / factor;
    const anomaly = normal ? value - (sum ? reference : reference / months) / factor : value;
    return { year, value, anomaly, months };
  });
  const result = { rows, extreme: rows.reduce((max, row) => Math.max(max, Math.abs(row.anomaly ?? 0)), .001) };
  model.annual.set(key, result);
  return result;
}
/** One scale for the state and all nine divisions, so that their stripes can be compared. */
const sharedExtreme = (model, element, baseline) => model.data.areas.reduce((max, area) => Math.max(max, annualOf(model, element, area.id, baseline).extreme), .001);
const colourFor = element => (element === 'tmpc' ? divergingBlueRed : divergingBrownTeal);
const digitsFor = element => (element === 'tmpc' ? 1 : 2);
const position = (value, extreme) => .5 + .5 * clamp((value ?? 0) / extreme, -1, 1);

function monthlyExtreme(model, element, area, baseline) {
  const { values, normals, elements } = model.data, flat = values[element]?.[area] || [], factor = elements[element].scale;
  const normal = element === 'pdsi' ? null : normals[baseline]?.[element]?.[area] || null;
  let extreme = .001;
  for (let m = 0; m < flat.length; m++) { const v = flat[m]; if (v !== null && v !== undefined) extreme = Math.max(extreme, Math.abs(v / factor - (normal ? normal[m % 12] / factor : 0))); }
  return extreme;
}
function drawStripes(ctx, rows, extreme, paint, x, y, w, h) {
  const width = w / rows.length;
  rows.forEach((row, index) => {
    const px = x + index * width;
    if (row.months === 0) {
      ctx.fillStyle = '#ffffff10'; ctx.fillRect(px, y, width + .5, h);
      return;
    }
    ctx.fillStyle = paint(position(row.anomaly, extreme));
    ctx.fillRect(px, y, width + .5, h);
    if (row.months < 12) {
      // An unfinished year is hatched, so that it is not read as a whole year.
      ctx.save(); ctx.beginPath(); ctx.rect(px, y, width + .5, h); ctx.clip();
      ctx.strokeStyle = '#000000aa'; ctx.lineWidth = 1;
      for (let d = -h; d < width + h; d += 4) { ctx.beginPath(); ctx.moveTo(px + d, y + h); ctx.lineTo(px + d + h, y); ctx.stroke(); }
      ctx.restore();
    }
  });
}

// --- The card: the stripes sweep in from 1895 -----------------------------------------------------------------------
const SWEEP_SECONDS = 5.5, HOLD_SECONDS = 3.5;

function cardScene(model, w, h, dpr) {
  const { rows, extreme } = annualOf(model, 'tmpc', STATE, '1901-2000');
  const stripes = document.createElement('canvas');
  stripes.width = Math.round(w * dpr); stripes.height = Math.round(h * dpr);
  const c = stripes.getContext('2d');
  c.setTransform(dpr, 0, 0, dpr, 0, 0);
  drawStripes(c, rows, extreme, divergingBlueRed, 0, 0, w, h);
  drawGrain(c, w, h, .08, 23);
  return { w, h, dpr, stripes, rows };
}
function drawCard(ctx, scene, { t, still }) {
  const { w, h, rows, stripes } = scene, cycle = SWEEP_SECONDS + HOLD_SECONDS, at = still ? 1 : clamp((t % cycle) / SWEEP_SECONDS);
  const reveal = ease.inOutCubic(at), front = reveal * w;
  ctx.fillStyle = GROUND; ctx.fillRect(0, 0, w, h);
  ctx.drawImage(stripes, 0, 0, Math.round(front * scene.dpr), stripes.height, 0, 0, front, h);
  if (at < 1) {
    const light = ctx.createLinearGradient(front - 28, 0, front + 8, 0);
    light.addColorStop(0, '#ffffff00'); light.addColorStop(.8, '#ffffff66'); light.addColorStop(1, '#ffffff00');
    ctx.fillStyle = light; ctx.fillRect(front - 28, 0, 36, h);
  }
  const shade = ctx.createLinearGradient(0, h * .62, 0, h);
  shade.addColorStop(0, '#0c142000'); shade.addColorStop(1, '#0c1420d9');
  ctx.fillStyle = shade; ctx.fillRect(0, h * .62, w, h * .38);
  const year = rows[Math.min(rows.length - 1, Math.floor(reveal * rows.length))]?.year;
  ctx.fillStyle = '#f6efe0'; ctx.font = `600 ${Math.round(clamp(w * .055, 12, 20))}px ui-sans-serif,system-ui,sans-serif`; ctx.textAlign = 'left'; ctx.textBaseline = 'alphabetic';
  fillTabular(ctx, String(year), 10, h - 7);
}
function Card({ bundle, held }) {
  const model = modelOf(bundle), scene = useRef(null);
  const ref = useStoryCanvas({
    animate: true, held, fps: 30, deps: [bundle],
    draw(ctx, frame) {
      if (scene.current?.w !== frame.w || scene.current?.h !== frame.h || scene.current?.dpr !== frame.dpr) scene.current = cardScene(model, frame.w, frame.h, frame.dpr);
      drawCard(ctx, scene.current, frame);
    },
  });
  return <canvas ref={ref} className="story-canvas" aria-hidden="true"/>;
}

// --- The lab -------------------------------------------------------------------------------------------------------
function labLayout(w, h, areas) {
  const gap = 10, label = 16, compact = w < 520;
  const stateH = compact ? 62 : Math.round(h * .22), calendarH = compact ? 132 : Math.round(h * .3);
  const smallH = Math.max(40, Math.round((h - stateH - calendarH - gap * 2 - label * 5 - 22) / 3));
  const smallW = (w - gap * 2) / 3;
  const state = { x: 0, y: label, w, h: stateH };
  const smalls = areas.slice(1).map((area, index) => ({
    id: area.id, name: area.name,
    x: (index % 3) * (smallW + gap), y: label + stateH + gap + label + Math.floor(index / 3) * (smallH + label + 2), w: smallW, h: smallH,
  }));
  const calendarTop = state.y + stateH + gap + 3 * (smallH + label + 2) + label;
  return { state, smalls, calendar: { x: 30, y: calendarTop, w: w - 30, h: calendarH }, axisY: calendarTop + calendarH + 4 };
}
function drawLab(ctx, { w, h }, model, year, settings, hover) {
  const { years, areas, values, normals, elements } = model.data, element = settings.element, paint = colourFor(element);
  const layout = labLayout(w, h, areas), first = years[0], width = w;
  ctx.clearRect(0, 0, w, h);
  ctx.font = '11px ui-sans-serif,system-ui,sans-serif'; ctx.textBaseline = 'alphabetic'; ctx.textAlign = 'left';
  const stateSeries = annualOf(model, element, STATE, settings.baseline), shared = sharedExtreme(model, element, settings.baseline);
  ctx.fillStyle = settings.area === STATE ? '#efd395' : '#c7d6db';
  ctx.fillText('Kansas', 0, layout.state.y - 4);
  drawStripes(ctx, stateSeries.rows, shared, paint, layout.state.x, layout.state.y, layout.state.w, layout.state.h);
  // A line over the state's stripes gives the same values a second cue beside colour.
  ctx.beginPath();
  let drawing = false;
  stateSeries.rows.forEach((row, index) => {
    if (row.months === 0) { drawing = false; return; }
    const px = (index + .5) / years.length * width, py = layout.state.y + layout.state.h * (1 - position(row.anomaly, shared));
    if (drawing) ctx.lineTo(px, py); else ctx.moveTo(px, py);
    drawing = true;
  });
  ctx.strokeStyle = '#ffffffb0'; ctx.lineWidth = 1; ctx.stroke();
  for (const small of layout.smalls) {
    const series = annualOf(model, element, small.id, settings.baseline);
    ctx.fillStyle = settings.area === small.id ? '#efd395' : '#c7d6db';
    ctx.fillText(small.name, small.x, small.y - 4);
    drawStripes(ctx, series.rows, shared, paint, small.x, small.y, small.w, small.h);
    if (settings.area === small.id) { ctx.strokeStyle = '#efd395'; ctx.lineWidth = 1.5; ctx.strokeRect(small.x - 1, small.y - 1, small.w + 2, small.h + 2); }
  }
  // The monthly calendar for the chosen area: years across, months down.
  const calendar = layout.calendar, flat = values[element]?.[settings.area] || [], factor = elements[element].scale;
  const normal = element === 'pdsi' ? null : normals[settings.baseline]?.[element]?.[settings.area] || null;
  const cellW = calendar.w / years.length, cellH = calendar.h / 12;
  const extreme = monthlyExtreme(model, element, settings.area, settings.baseline);
  for (let index = 0; index < years.length; index++) for (let m = 0; m < 12; m++) {
    const v = flat[index * 12 + m];
    ctx.fillStyle = v === null || v === undefined ? '#ffffff0d' : paint(position(v / factor - (normal ? normal[m] / factor : 0), extreme));
    ctx.fillRect(calendar.x + index * cellW, calendar.y + m * cellH, cellW + .5, cellH + .5);
  }
  ctx.fillStyle = '#c7d6db'; ctx.fillText(`${areas.find(a => a.id === settings.area)?.name} by month`, 0, calendar.y - 4);
  ctx.fillStyle = '#a9bdc4'; ctx.textAlign = 'right'; ctx.textBaseline = 'middle';
  for (const m of [0, 3, 6, 9]) ctx.fillText(MONTHS[m], calendar.x - 5, calendar.y + (m + .5) * cellH);
  ctx.textAlign = 'center'; ctx.textBaseline = 'top';
  const ticks = years.filter(y => y % (w < 520 ? 40 : 20) === 0);
  for (const tick of ticks) fillTabular(ctx, String(tick), calendar.x + (tick - first + .5) * cellW, layout.axisY);
  // The chosen year as a cursor through every panel.
  const index = clamp(year - first, 0, years.length - 1);
  ctx.strokeStyle = '#ffffff'; ctx.lineWidth = 1.5;
  const mark = (x, y, panelW, panelH) => { const px = x + (index + .5) / years.length * panelW; ctx.beginPath(); ctx.moveTo(px, y - 2); ctx.lineTo(px, y + panelH + 2); ctx.stroke(); };
  mark(layout.state.x, layout.state.y, layout.state.w, layout.state.h);
  layout.smalls.forEach(small => mark(small.x, small.y, small.w, small.h));
  mark(calendar.x, calendar.y, calendar.w, calendar.h);
  if (hover?.kind === 'month') { ctx.strokeStyle = '#fff'; ctx.lineWidth = 1; ctx.strokeRect(calendar.x + hover.index * cellW - .5, calendar.y + hover.month * cellH - .5, Math.max(cellW, 2) + 1, cellH + 1); }
  drawGrain(ctx, w, h, .03, 23);
  return { layout };
}
function locate(layout, x, y, count) {
  const inside = panel => x >= panel.x && x < panel.x + panel.w && y >= panel.y && y < panel.y + panel.h;
  const yearIndex = panel => clamp(Math.floor((x - panel.x) / panel.w * count), 0, count - 1);
  if (inside(layout.state)) return { kind: 'year', area: STATE, index: yearIndex(layout.state) };
  for (const small of layout.smalls) if (inside(small)) return { kind: 'year', area: small.id, index: yearIndex(small) };
  if (inside(layout.calendar)) return { kind: 'month', index: yearIndex(layout.calendar), month: clamp(Math.floor((y - layout.calendar.y) / layout.calendar.h * 12), 0, 11) };
  return null;
}
function describe(model, hover, settings) {
  const { years, areas, elements, values, normals } = model.data, spec = elements[settings.element], digits = digitsFor(settings.element);
  const unit = spec.unit === 'index' ? '' : spec.unit, baseline = settings.element === 'pdsi' ? null : settings.baseline;
  if (hover.kind === 'month') {
    const raw = values[settings.element]?.[settings.area]?.[hover.index * 12 + hover.month], name = areas.find(a => a.id === settings.area)?.name;
    if (raw === null || raw === undefined) return `${MONTHS[hover.month]} ${years[hover.index]} · ${name} · no value yet`;
    const value = raw / spec.scale, normal = baseline ? normals[baseline]?.[settings.element]?.[settings.area]?.[hover.month] / spec.scale : null;
    return `${MONTHS[hover.month]} ${years[hover.index]} · ${name} · ${fmt(value, { digits, unit })}${baseline ? ` · ${fmt(value - normal, { digits, unit, sign: true })} against ${baseline}` : ''}`;
  }
  const area = hover.area, row = annualOf(model, settings.element, area, settings.baseline).rows[hover.index], name = areas.find(a => a.id === area)?.name;
  if (!row.months) return `${row.year} · ${name} · no value yet`;
  const kind = spec.annual === 'sum' ? 'total' : 'mean';
  return `${row.year} · ${name} · ${fmt(row.value, { digits, unit })} ${kind}${baseline ? ` · ${fmt(row.anomaly, { digits, unit, sign: true })} against ${baseline}` : ''}${row.months < 12 ? ` · ${row.months} of 12 months` : ''}`;
}
function Lab({ bundle, time, onTime, controls, onControls }) {
  const model = modelOf(bundle), settings = { ...DEFAULTS, ...controls }, { years, areas, elements, latest } = model.data;
  const year = clamp(Math.round(time ?? latest.year), years[0], years.at(-1));
  const [hover, setHover] = useState(null), geometry = useRef(null);
  const canvas = useStoryCanvas({
    deps: [bundle, year, settings.element, settings.baseline, settings.area, hover?.kind === 'month' ? `${hover.index}/${hover.month}` : ''],
    draw: (ctx, frame) => { geometry.current = drawLab(ctx, frame, model, year, settings, hover); },
  });
  const element = settings.element, spec = elements[element], paint = colourFor(element), digits = digitsFor(element);
  const series = annualOf(model, element, settings.area, settings.baseline), shared = sharedExtreme(model, element, settings.baseline), monthly = monthlyExtreme(model, element, settings.area, settings.baseline), fallback = { kind: 'year', area: settings.area, index: clamp(year - years[0], 0, years.length - 1) };
  const pick = event => {
    if (!geometry.current) return;
    const box = event.currentTarget.getBoundingClientRect(), x = event.clientX - box.left, y = event.clientY - box.top;
    setHover(locate(geometry.current.layout, x, y, years.length));
  };
  const choose = event => {
    pick(event);
    if (!geometry.current) return;
    const box = event.currentTarget.getBoundingClientRect(), found = locate(geometry.current.layout, event.clientX - box.left, event.clientY - box.top, years.length);
    if (!found) return;
    if (found.area && found.area !== settings.area) onControls?.({ ...settings, area: found.area });
    onTime?.(years[found.index]);
  };
  const unit = spec.unit === 'index' ? 'index' : spec.unit;
  const stateRow = annualOf(model, element, STATE, settings.baseline).rows.find(row => row.year === year), highest = [...series.rows].filter(row => row.months === 12).sort((a, b) => b.anomaly - a.anomaly)[0];
  const summary = `Stripes of annual ${spec.label.toLowerCase()} for Kansas and nine climate divisions, ${years[0]} to ${years.at(-1)}, with a monthly calendar below. In ${year}, Kansas was ${stateRow?.months ? fmt(stateRow.value, { digits, unit: spec.unit === 'index' ? '' : spec.unit }) : 'not yet reported'}. The highest whole year for the chosen area was ${highest?.year}.`;
  return <div className="story-lab-layout">
    <div className="story-lab-main"><canvas ref={canvas} className="story-canvas story-stripes-lab" role="img" aria-label={summary} onPointerMove={pick} onPointerDown={choose} onPointerLeave={() => setHover(null)}/></div>
    <aside className="story-lab-side" aria-label="Climate tools">
      <section className="story-panel">
        <Segmented label="Measure" value={element} onChange={value => onControls?.({ ...settings, element: value })} options={[{ id: 'tmpc', label: 'Temperature' }, { id: 'pcpn', label: 'Precipitation' }, { id: 'pdsi', label: 'Drought index' }]}/>
        <Segmented label="Baseline" value={settings.baseline} disabled={element === 'pdsi'} onChange={value => onControls?.({ ...settings, baseline: value })} options={model.data.baselines.map(id => ({ id, label: id }))}/>
        {element === 'pdsi' && <p className="story-note">The drought index is relative to each place’s own climate, so it has no baseline here.</p>}
        <label className="story-select">Area
          <select value={settings.area} onChange={event => onControls?.({ ...settings, area: event.target.value })}>{areas.map(area => <option key={area.id} value={area.id}>{area.name}</option>)}</select>
        </label>
      </section>
      <section className="story-panel">
        <Legend title={element === 'pdsi' ? 'Drought index: dry to wet' : `Against ${settings.baseline}, ${element === 'tmpc' ? 'cool to warm' : 'dry to wet'}`} ramp={{ scale: paint, from: fmt(-shared, { digits, sign: true }), to: `${fmt(shared, { digits, sign: true })}${unit === 'index' ? '' : ` ${unit}`}` }}/>
        <p className="story-note">Every stripe shares this scale. The monthly calendar’s own scale runs to ±{fmt(monthly, { digits })}{unit === 'index' ? '' : ` ${unit}`}. Hatching marks an unfinished year; a white line over the Kansas stripes traces the same values.</p>
      </section>
      <section className="story-panel"><Readout>{describe(model, hover || fallback, settings)}</Readout></section>
    </aside>
    <Summary>{summary}</Summary>
  </div>;
}

export default function Story({ bundle, mode, paused, reduced, time, onTime, controls, onControls }) {
  if (!bundle?.data?.values) return null;
  return mode === 'lab' ? <Lab bundle={bundle} time={time} onTime={onTime} controls={controls} onControls={onControls}/> : <Card bundle={bundle} held={Boolean(paused || reduced)}/>;
}
export function range(bundle) {
  const years = bundle.data.years;
  return { min: years[0], max: years.at(-1), step: 1, label: 'Year', format: value => String(value), rate: 6 };
}
export function toCSV(bundle, { controls } = {}) {
  const settings = { ...DEFAULTS, ...controls }, model = modelOf(bundle), { areas, elements } = model.data, spec = elements[settings.element];
  const baseline = settings.element === 'pdsi' ? '' : settings.baseline, rows = [['year', 'area', 'measure', 'annual_value', 'unit', 'anomaly', 'baseline', 'months']];
  for (const area of areas) for (const row of annualOf(model, settings.element, area.id, settings.baseline).rows) {
    rows.push([row.year, area.name, spec.label, row.months ? +row.value.toFixed(3) : '', spec.unit, row.months && baseline ? +row.anomaly.toFixed(3) : '', baseline, row.months]);
  }
  return { filename: `climate-stripes-${settings.element}${baseline ? `-${baseline}` : ''}.csv`, rows };
}

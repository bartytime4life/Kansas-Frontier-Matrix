import { useEffect, useRef, useState } from 'react';
import { createPortal } from 'react-dom';
import spotlight from './subsurface-spotlight.json';
import { materialFor, materialInfo } from '../subsurface-materials';

/**
 * Geology welcome spotlight: one real KGS record at a time (a water well, a
 * Core Library core, or an inventoried mine) rises from its own location on
 * the preview map, shows what its layer holds, then gives way to the next.
 * Records are fixed and named in scripts/build-welcome-spotlight.py; nothing
 * here interpolates geology or claims current conditions.
 */
const KINDS = ['well', 'core', 'mine'];
const DWELL_MS = 9000, EXIT_MS = 520, RETRY_MS = 1600;
// Measured footprints [width, height, stem] in px, used to keep cards clear of the
// welcome's own panels. Behind the category cards only a labelled chip fits; the
// opened preview has room for the full card (a mine's KGS note adds a few lines).
const CHIP = [232, 66, 18], CARD = { well: [276, 340, 36], core: [276, 348, 36], mine: [276, 340, 36] };
const footprint = (record, expanded) => expanded ? [CARD[record.kind][0], CARD[record.kind][1] + (record.note ? 70 : 0), CARD[record.kind][2]] : CHIP;
const OBSTACLES = ['.welcome-hero', '.welcome-toolbar', '.welcome-preview-brief', '.discovery-hint', '.discovery-field', '.welcome-layer-demo', '.welcome-scene-deck', '.domain-stage-caption'].map(s => `.living-welcome ${s}`).concat('header.topbar').join(',');
const SPOTLIGHT_RECORDS = spotlight.records;
const SOURCE = Object.fromEntries(spotlight.sources.map(source => [source.id, source]));
const ft = n => `${Math.round(n).toLocaleString('en-US')} ft`;
const clip = (text, n) => text.length > n ? `${text.slice(0, n - 1).trimEnd()}…` : text;
const title = text => /[a-z]/.test(text) ? text : text.toLowerCase().replace(/\b[a-z]/g, c => c.toUpperCase());
const PRODUCT = { Salt: 'salt', 'Salt Brine': 'salt', Gypsum: 'gypsum', Limestone: 'limestone', Lead: 'ore', Coal: 'coal', Clay: 'clay' };
const productColor = category => category === 'Volcanic Ash' ? '#d9d3c4' : materialInfo(PRODUCT[category] ?? 'unknown').color;

/** 'above' or 'below' its pin where the card fits clear of the welcome panels, else null. */
function placement(engine, host, record, expanded, only = null) {
 const point = engine.project(record.coordinates, 'geology');
 if (!point || !host) return null;
 const box = host.getBoundingClientRect(), [w, h, stem] = footprint(record, expanded);
 const blocked = [...host.ownerDocument.querySelectorAll(OBSTACLES)].flatMap(element => {
  const r = element.getBoundingClientRect(), style = getComputedStyle(element);
  return !r.width || !r.height || style.visibility === 'hidden' || Number(style.opacity) < 0.1 ? [] : [{ left: r.left - box.left, top: r.top - box.top, right: r.right - box.left, bottom: r.bottom - box.top }];
 });
 const clear = card => card.left >= 12 && card.right <= box.width - 12 && card.top >= 12 && card.bottom <= box.height - 12
  && !blocked.some(r => r.left < card.right && r.right > card.left && r.top < card.bottom && r.bottom > card.top);
 const left = point.x - w / 2, right = point.x + w / 2;
 if (only !== 'below' && clear({ left, right, top: point.y - h - stem, bottom: point.y + 12 })) return 'above';
 return only !== 'above' && clear({ left, right, top: point.y - 12, bottom: point.y + h + stem }) ? 'below' : null;
}

/** The opened preview prefers the full card; a short window, or the category view, gets the chip. */
function fit(engine, host, record, expanded) {
 const side = placement(engine, host, record, expanded);
 if (side) return { side, compact: !expanded };
 const small = expanded && placement(engine, host, record, false);
 return small ? { side: small, compact: true } : null;
}

/** Next kind in turn, preferring a record not seen recently and that fits on screen now. */
function nextRecord(place, memory) {
 for (let step = 0; step < KINDS.length; step++) {
  const kind = KINDS[(memory.turn + step) % KINDS.length], ofKind = SPOTLIGHT_RECORDS.filter(r => r.kind === kind).map(record => ({ record, ...place(record) })).filter(o => o.side);
  const fresh = ofKind.filter(o => !memory.recent.includes(o.record.id));
  const options = fresh.length ? fresh : ofKind.filter(o => o.record.id !== memory.recent.at(-1));
  if (options.length) return { ...options[Math.floor(Math.random() * options.length)], turn: memory.turn + step + 1 };
 }
 return null;
}

function Pinned({ engine, element, coordinates, anchor = 'bottom', children }) {
 useEffect(() => engine.pin(element, coordinates, anchor), [engine, element, coordinates, anchor]);
 return createPortal(children, element);
}
const pinElement = (kind, extra = '') => {
 const element = document.createElement('div');
 element.className = `welcome-spot ${extra}`.trim(); element.dataset.kind = kind;
 return element;
};

function WellLog({ record }) {
 const H = 112, scale = H / record.totalDepth;
 const rows = record.intervals.map((row, i) => ({ ...row, i, y: row.top * scale, h: (row.bottom - row.top) * scale, material: materialInfo(materialFor(row, 'well')) }));
 const labels = [];
 for (const row of [...rows].sort((a, b) => b.h - a.h)) {
  const y = row.y + row.h / 2;
  if (labels.length < 5 && labels.every(label => Math.abs(label.y - y) >= 12)) labels.push({ ...row, y });
 }
 labels.sort((a, b) => a.y - b.y);
 return <svg className="welcome-spot-art" viewBox="0 0 240 128" aria-hidden="true">
  <path className="welcome-spot-ground" d="M8 10H232"/>
  <g transform="translate(0 10)">
   {[0, record.totalDepth / 2, record.totalDepth].map(d => <g key={d} className="welcome-spot-ruler"><path d={`M26 ${d * scale}h6`}/><text x="23" y={d * scale + 3} textAnchor="end">{Math.round(d)}</text></g>)}
   <g className="welcome-spot-drill">
    {rows.map(row => <rect key={row.i} x="36" y={row.y} width="26" height={Math.max(row.h, 0.8)} fill={row.material.color}><title>{row.top}–{row.bottom} ft: {row.description}</title></rect>)}
    <path d={`M36 0V${H}M62 0V${H}`} stroke="#061c28" strokeOpacity=".5"/>
   </g>
   <path className="welcome-spot-bit" d="M41 -6h16l-8 10z"/>
   {labels.map((label, n) => <g key={label.i} className="welcome-spot-label" style={{ '--n': n }}><path d={`M64 ${label.y}h8`}/><text x="76" y={label.y + 3}>{clip(label.description, 30)}</text></g>)}
  </g>
 </svg>;
}

function CoreTray({ record }) {
 const deepest = record.bottom * 1.08, H = 104, y = d => 12 + d / deepest * H;
 const cols = 10, rows = Math.ceil(record.boxes / cols), pitch = Math.min(11, 86 / rows);
 return <svg className="welcome-spot-art" viewBox="0 0 240 124" aria-hidden="true">
  <path className="welcome-spot-ground" d="M8 12H40"/>
  <rect x="16" y="12" width="12" height={H} rx="2" className="welcome-spot-hole"/>
  <rect className="welcome-spot-span" x="16" y={y(record.top)} width="12" height={Math.max(y(record.bottom) - y(record.top), 2)} rx="2"/>
  <g className="welcome-spot-ruler"><text x="32" y={y(record.top) + 3}>{ft(record.top)}</text><text x="32" y={y(record.bottom) + 3}>{ft(record.bottom)}</text></g>
  <g transform="translate(96 14)">
   {Array.from({ length: record.boxes }, (_, i) => <g key={i} className="welcome-spot-box" style={{ '--i': i }} transform={`translate(${(i % cols) * 13.6} ${Math.floor(i / cols) * pitch})`}>
    <rect width="12" height={pitch - 2} rx="1"/><path d={`M2 ${(pitch - 2) / 3}h8M2 ${2 * (pitch - 2) / 3}h8`}/>
   </g>)}
   <text className="welcome-spot-count" x="0" y={rows * pitch + 12}>{record.boxes} boxes in the KGS Core Library</text>
  </g>
 </svg>;
}

function MineSection({ record }) {
 const color = productColor(record.category), abandoned = record.status === 'Abandoned';
 const style = ['Underground', 'Subsurface'].includes(record.operation) ? 'underground' : record.operation === 'Solution Mine' ? 'solution' : record.operation?.startsWith('Surface') ? 'surface' : 'unrecorded';
 return <svg className="welcome-spot-art" viewBox="0 8 240 124" aria-hidden="true" data-style={style} data-abandoned={abandoned}>
  <path className="welcome-spot-land" d="M0 40H240V132H0Z"/>
  <path className="welcome-spot-ground" d="M0 40H240"/>
  {style === 'underground' && <>
   <rect x="16" y="88" width="216" height="24" fill={color} opacity=".85"/>
   <path className="welcome-spot-frame" d="M38 40L50 12L62 40M42 30H58M50 12V40"/><circle className="welcome-spot-frame" cx="50" cy="12" r="5"/>
   <path className="welcome-spot-shaft" d="M47 40V100M53 40V100"/>
   <rect className="welcome-spot-cage" x="46" y="42" width="8" height="9" rx="1"/>
   {Array.from({ length: 8 }, (_, i) => <rect key={i} className="welcome-spot-room" style={{ '--i': i }} x={62 + i * 21} y="92" width="13" height="16" rx="1"/>)}
  </>}
  {style === 'solution' && <>
   <ellipse className="welcome-spot-cavern" cx="120" cy="104" rx="70" ry="18" fill={color}/>
   <path className="welcome-spot-shaft" d="M98 30V100M142 30V100"/>
   <path className="welcome-spot-flow welcome-spot-flow--in" d="M98 32V98"/><path className="welcome-spot-flow welcome-spot-flow--out" d="M142 98V32"/>
   <path className="welcome-spot-frame" d="M92 30h12M136 30h12"/>
   <text className="welcome-spot-tag" x="70" y="24">water in</text><text className="welcome-spot-tag" x="150" y="24">brine out</text>
  </>}
  {style === 'surface' && <>
   <path d="M40 40L56 56H72L84 70H156L168 56H184L200 40Z" fill={color} opacity=".9"/>
   <path className="welcome-spot-bench" d="M40 40L56 56H72L84 70H156L168 56H184L200 40"/>
   <path className="welcome-spot-road" d="M200 40L176 54L150 64L96 68"/>
  </>}
  {style === 'unrecorded' && <>
   {[[96, 82], [118, 90], [140, 80], [128, 102], [106, 104]].map(([x, y], i) => <path key={i} className="welcome-spot-crystal" style={{ '--i': i }} d={`M${x} ${y - 7}l6 7l-6 7l-6 -7z`} fill={color}/>)}
   <ellipse cx="120" cy="92" rx="44" ry="22" className="welcome-spot-unknown"/>
  </>}
  <text className="welcome-spot-tag" x="232" y="126" textAnchor="end">{style === 'unrecorded' ? 'operation type not recorded' : 'schematic · depth not in record'}</text>
 </svg>;
}

/** One-line strip for the compact chip: the log's bands, the cored span, or the product colour. */
function MiniStrip({ record }) {
 if (record.kind === 'well') return <svg className="welcome-spot-mini" viewBox="0 0 100 6" preserveAspectRatio="none" aria-hidden="true">{record.intervals.map((row, i) => <rect key={i} x={row.top / record.totalDepth * 100} width={(row.bottom - row.top) / record.totalDepth * 100} height="6" fill={materialInfo(materialFor(row, 'well')).color}/>)}</svg>;
 if (record.kind === 'core') { const deepest = record.bottom * 1.08; return <svg className="welcome-spot-mini" viewBox="0 0 100 6" preserveAspectRatio="none" aria-hidden="true"><rect width="100" height="6" fill="#0a1f28"/><rect className="welcome-spot-span" x={record.top / deepest * 100} width={Math.max((record.bottom - record.top) / deepest * 100, 1)} height="6"/></svg>; }
 return <svg className="welcome-spot-mini" viewBox="0 0 100 6" preserveAspectRatio="none" aria-hidden="true"><rect width="100" height="6" fill={productColor(record.category)}/></svg>;
}
function Chip({ record, onNext }) {
 const kicker = record.kind === 'well' ? 'Water well' : record.kind === 'core' ? 'Core sample' : `Mine · ${record.county} County`;
 const fact = record.kind === 'well' ? `${ft(record.totalDepth)} driller's log · ${record.recordDate.slice(0, 4)}`
  : record.kind === 'core' ? `${ft(record.top)}–${ft(record.bottom)} cored · ${record.boxes} boxes`
   : `${record.product ?? record.category} · ${(record.operation ?? 'operation not recorded').toLowerCase()} · ${record.abandonedDuring ? `abandoned (listed ${record.abandonedDuring})` : `${record.status?.toLowerCase()} c. 2000`}`;
 return <article className="welcome-spot-card welcome-spot-chip" aria-label={`${kicker}: ${record.label}`}>
  <span className="welcome-spot-kicker">{kicker}</span>
  <strong className="welcome-spot-title">{record.label}</strong>
  <span className="welcome-spot-fact">{fact}</span>
  <MiniStrip record={record}/>
  {onNext && <button type="button" className="welcome-spot-chip-next" onClick={onNext}>Next <span aria-hidden="true">→</span></button>}
  <i className="welcome-spot-timer" aria-hidden="true"/>
 </article>;
}

function Card({ record, expanded, compact, onNext }) {
 if (compact) return <Chip record={record} onNext={expanded ? onNext : null}/>;
 const fields = record.kind === 'well'
  ? [['Logged', record.recordDate], ['Total depth', ft(record.totalDepth)], ['Location', record.locationMethod], ['Intervals', record.intervals.length]]
  : record.kind === 'core'
   ? [['Operator', title(record.operator)], ['Cored span', `${ft(record.bottom - record.top)}`], ['Depth', 'drilled, not true vertical'], ['KGS ID', record.kid]]
   : [['Operation', record.operation ?? 'not recorded'], ['Status', record.abandonedDuring ? `abandoned (listed ${record.abandonedDuring})` : `${record.status?.toLowerCase()} in inventory`], ...record.acres ? [['Acres in mine', record.acres]] : [], ['KGS ID', record.kid]];
 const kicker = record.kind === 'well' ? 'Water well · KGS WWC5' : record.kind === 'core' ? 'Core sample · KGS Core Library' : `Mine · ${record.product ?? record.category} · ${record.county} County`;
 const footer = record.kind === 'well' ? "Driller's log as recorded. Unknown between wells." : record.kind === 'core' ? SOURCE['kgs-core-boxes'].limitation.split('. ')[1] : 'KGS inventory, largely c. 2000. Not a current operating status.';
 return <article className="welcome-spot-card" aria-label={`${kicker}: ${record.label}`}>
  <span className="welcome-spot-kicker">{kicker}</span>
  <strong className="welcome-spot-title">{record.label}</strong>
  {record.kind === 'well' && <WellLog record={record}/>}
  {record.kind === 'core' && <CoreTray record={record}/>}
  {record.kind === 'mine' && <MineSection record={record}/>}
  <dl className="welcome-spot-fields">{fields.map(([name, value]) => <div key={name}><dt>{name}</dt><dd>{value}</dd></div>)}</dl>
  {record.kind === 'mine' && record.note && <p className="welcome-spot-note">KGS note: {title(record.note)}</p>}
  <small className="welcome-spot-limit">{footer}</small>
  {expanded && <div className="welcome-spot-actions">
   <a href={record.sourceUrl} target="_blank" rel="noreferrer">KGS record ↗</a>
   {record.photosUrl && <a href={record.photosUrl} target="_blank" rel="noreferrer">Core photos ↗</a>}
   <button type="button" onClick={onNext}>Next <span aria-hidden="true">→</span></button>
  </div>}
  <i className="welcome-spot-timer" aria-hidden="true"/>
 </article>;
}

export function SubsurfaceSpotlight({ engine, host, paused = false, reduced = false, expanded = false, onPlaced }) {
 const [current, setCurrent] = useState(null), [leaving, setLeaving] = useState(false), [trail, setTrail] = useState([]);
 const [hidden, setHidden] = useState(() => typeof document !== 'undefined' && document.hidden);
 const memory = useRef({ turn: 0, recent: [] }), shown = useRef(null), layout = useRef(expanded);
 useEffect(() => {
  const change = () => setHidden(document.hidden);
  document.addEventListener('visibilitychange', change);
  return () => document.removeEventListener('visibilitychange', change);
 }, []);
 useEffect(() => {
  if (!engine || !host) return;
  let timer = 0, alive = true;
  const show = () => {
   if (!alive) return;
   const pick = nextRecord(record => fit(engine, host, record, expanded), memory.current);
   if (!pick) { timer = setTimeout(show, RETRY_MS); return; }
   const previous = shown.current;
   memory.current = { turn: pick.turn, recent: [...memory.current.recent, pick.record.id].slice(-9) };
   // The last few spots stay as faint markers, so the wander reads across the map.
   if (previous) setTrail(list => [...list.filter(item => item.record.id !== previous.record.id && item.record.id !== pick.record.id), { record: previous.record, element: pinElement(previous.record.kind, 'welcome-spot--trail') }].slice(-5));
   shown.current = { record: pick.record, side: pick.side, compact: pick.compact, element: pinElement(pick.record.kind) };
   setCurrent(shown.current); setLeaving(false);
  };
  if (!shown.current) show();
  else if (leaving) timer = setTimeout(show, EXIT_MS);
  else if (!paused && !reduced && !hidden) timer = setTimeout(() => setLeaving(true), DWELL_MS);
  return () => { alive = false; clearTimeout(timer); };
 }, [engine, host, current, leaving, paused, reduced, hidden, expanded]);
 // Opening or closing the preview re-fits the record on screen now, not the next one.
 useEffect(() => {
  if (layout.current === expanded) return;
  layout.current = expanded;
  const now = shown.current;
  if (!engine || !host || !now || leaving) return;
  const next = fit(engine, host, now.record, expanded);
  if (!next) { setLeaving(true); return; }
  if (next.side === now.side && next.compact === now.compact) return;
  shown.current = { ...now, ...next };
  setCurrent(shown.current);
 }, [engine, host, expanded, leaving]);
 useEffect(() => { onPlaced?.(Boolean(current)); }, [current, onPlaced]);
 useEffect(() => () => onPlaced?.(false), [onPlaced]);
 // Scrolled category cards, an opened panel or the drift can cover a card; it then gives way early.
 useEffect(() => {
  if (!engine || !host || !current || leaving) return;
  const check = setInterval(() => { if (!placement(engine, host, current.record, expanded && !current.compact, current.side)) setLeaving(true); }, 1500);
  return () => clearInterval(check);
 }, [engine, host, current, leaving, expanded]);
 if (!engine || !current) return null;
 const still = paused || reduced || hidden;
 return <>
  {trail.map(item => <Pinned key={item.record.id} engine={engine} element={item.element} coordinates={item.record.coordinates}><span className="welcome-spot-pin" title={item.record.label}/></Pinned>)}
  <Pinned key={current.record.id} engine={engine} element={current.element} coordinates={current.record.coordinates} anchor={current.side === 'below' ? 'top' : 'bottom'}>
   <div className="welcome-spot-inner" data-kind={current.record.kind} data-side={current.side} data-phase={leaving ? 'out' : 'in'} data-still={still} data-reduced={reduced} data-expanded={expanded && !current.compact} style={{ '--dwell': `${DWELL_MS}ms` }}>
    <Card record={current.record} expanded={expanded} compact={current.compact} onNext={() => setLeaving(true)}/>
    <span className="welcome-spot-stem" aria-hidden="true"/>
    <span className="welcome-spot-pin" aria-hidden="true"><i/><i/></span>
   </div>
  </Pinned>
 </>;
}

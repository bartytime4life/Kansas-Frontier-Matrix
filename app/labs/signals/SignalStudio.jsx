'use client';

import { useEffect, useMemo, useRef, useState } from 'react';
import Link from 'next/link';
import { PUBLIC_LAB_SNAPSHOTS } from '../public-snapshots.mjs';
import { loadPublicLabSnapshot } from '../snapshot-loader.mjs';
import { signalCatalog, analyzeSignals, SIGNAL_PRESETS } from '../signal-model.mjs';
import { encodeWorkbenchView, decodeWorkbenchView } from '../workbench-view.mjs';
import NotebookPanel from '../NotebookPanel.jsx';
import styles from './signals.module.css';

const SOURCE_IDS = ['climate-stripes', 'energy-shift', 'river-memory', 'tornado-tracks', 'shaking-ground'];
const SOURCE_BINDINGS = Object.fromEntries(SOURCE_IDS.map(id => [id, PUBLIC_LAB_SNAPSHOTS[id]?.sha256]).filter(([, hash]) => hash));
const INITIAL = SIGNAL_PRESETS[0]?.controls || { x: '', y: '', from: 1960, to: 2024, lag: 0, transform: 'raw' };
const TRANSFORMS = { raw: 'Recorded annual values', detrended: 'Linear trends removed', difference: 'Year-to-year differences' };
const number = new Intl.NumberFormat('en-US', { maximumFractionDigits: 2 });
const precise = new Intl.NumberFormat('en-US', { maximumFractionDigits: 4 });
const finite = value => typeof value === 'number' && Number.isFinite(value);
const fmt = value => finite(value) ? number.format(value) : 'Unavailable';
const coeff = value => finite(value) ? value.toFixed(3) : '—';
const csvCell = value => `"${String(value ?? '').replaceAll('"', '""')}"`;
const toCSV = rows => rows.map(row => row.map(csvCell).join(',')).join('\r\n') + '\r\n';
const excludedCount = value => Array.isArray(value) ? value.length : finite(value) ? value : 0;

function download(content, filename, type = 'application/json') {
  const url = URL.createObjectURL(new Blob([content], { type }));
  const anchor = document.createElement('a'); anchor.href = url; anchor.download = filename; anchor.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}

function useSignalBundles() {
  const [bundles, setBundles] = useState({}), [states, setStates] = useState(() => Object.fromEntries(SOURCE_IDS.map(id => [id, 'loading']))), [attempt, setAttempt] = useState(0);
  useEffect(() => {
    const controller = new AbortController();
    for (const id of SOURCE_IDS) {
      if (bundles[id]) continue;
      loadPublicLabSnapshot(id, { signal: controller.signal }).then(result => {
        if (controller.signal.aborted) return;
        if (result.state === 'ready') setBundles(current => ({ ...current, [id]: result.bundle }));
        setStates(current => ({ ...current, [id]: result.state }));
      }).catch(() => { if (!controller.signal.aborted) setStates(current => ({ ...current, [id]: 'offline' })); });
    }
    return () => controller.abort();
    // A retry fetches only missing bundles. Incoming bundles do not restart in-flight requests.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [attempt]);
  return { bundles, states, retry: () => { setStates(() => Object.fromEntries(SOURCE_IDS.map(id => [id, bundles[id] ? 'ready' : 'loading']))); setAttempt(value => value + 1); } };
}

function AxisControl({ axis, selected, catalog, onChange }) {
  const entry = catalog.find(item => item.id === selected), family = entry?.family || '';
  const families = [...new Set(catalog.map(item => item.family))];
  return <div className={styles.axisControl} data-axis={axis.toLowerCase()}><span><b>{axis}</b>{axis === 'X' ? 'LEADING SIGNAL' : 'FOLLOWING SIGNAL'}</span>
    <select aria-label={`${axis} signal family`} value={family} onChange={event => onChange(catalog.find(item => item.family === event.target.value)?.id || '')} disabled={!catalog.length}>{!family && <option value="">Choose field</option>}{families.map(value => <option key={value} value={value}>{value}</option>)}</select>
    <select aria-label={`${axis} annual signal`} value={selected} onChange={event => onChange(event.target.value)} disabled={!catalog.length}>{!entry && <option value={selected}>{selected ? 'Loading chosen signal…' : 'Choose a signal'}</option>}{catalog.filter(item => item.family === family).map(item => <option key={item.id} value={item.id}>{item.label}</option>)}</select>
  </div>;
}

function pointKey(event, pairs, row, onSelect) {
  if (['Enter', ' '].includes(event.key)) { event.preventDefault(); onSelect(row.year); return; }
  const step = ['ArrowRight', 'ArrowUp'].includes(event.key) ? 1 : ['ArrowLeft', 'ArrowDown'].includes(event.key) ? -1 : 0;
  if (!step) return;
  event.preventDefault();
  const index = pairs.findIndex(pair => pair.year === row.year), target = pairs[Math.max(0, Math.min(pairs.length - 1, index + step))];
  onSelect(target.year);
  event.currentTarget.ownerSVGElement?.querySelector(`[data-pair-year="${target.year}"]`)?.focus();
}

function pathFor(rows, field, scaleX, scaleY) {
  let path = '', previous = null;
  for (const row of rows) {
    if (!finite(row[field])) { previous = null; continue; }
    path += `${previous !== null && row.year === previous + 1 ? 'L' : 'M'}${scaleX(row.year).toFixed(2)},${scaleY(row[field]).toFixed(2)} `;
    previous = row.year;
  }
  return path.trim();
}

function Overlay({ pairs, x, y, selectedYear, onSelect, lag }) {
  const marks = pairs.filter(row => finite(row.zX) || finite(row.zY)), width = 760, height = 300;
  if (!marks.length) return <div className={styles.emptyChart}>The overlay needs complete annual pairs with variation in both signals. Adjust the period or choose a different signal.</div>;
  const minYear = Math.min(...marks.map(row => row.year)), maxYear = Math.max(...marks.map(row => row.year));
  const extent = Math.max(2, ...marks.flatMap(row => [Math.abs(row.zX || 0), Math.abs(row.zY || 0)]));
  const sx = year => 55 + (year - minYear) / (maxYear - minYear || 1) * (width - 85), sy = value => 140 - value / extent * 100;
  const selected = pairs.find(row => row.year === selectedYear), years = [...new Set([minYear, Math.round((minYear + maxYear) / 2), maxYear])];
  return <><svg viewBox={`0 0 ${width} ${height}`} role="group" aria-label={`Standardized annual ${x?.label || 'X'} and ${y?.label || 'Y'} overlay. X-year ${minYear} to ${maxYear}; Y is shifted by ${lag} years. Choose a point or use the paired-year table.`}>
    {[-2, -1, 0, 1, 2].filter(value => Math.abs(value) <= extent).map(value => <g key={value}><line x1="55" y1={sy(value)} x2={width - 30} y2={sy(value)} stroke={value === 0 ? '#6b8d99' : '#aac7d01e'} strokeDasharray={value === 0 ? undefined : '3 4'}/><text x="43" y={sy(value) + 4} textAnchor="end">{value > 0 ? '+' : ''}{value}</text></g>)}
    {years.map(year => <g key={year}><line x1={sx(year)} y1="31" x2={sx(year)} y2="249" stroke="#a7c6d014"/><text x={sx(year)} y="272" textAnchor="middle">{year}</text></g>)}
    <text x="55" y="19">Paired-period sample standard deviations</text><path d={pathFor(marks, 'zX', sx, sy)} fill="none" stroke="#e8bf72" strokeWidth="2.2"/><path d={pathFor(marks, 'zY', sx, sy)} fill="none" stroke="#70d6da" strokeWidth="2.2"/>
    {selected && <line x1={sx(selected.year)} y1="30" x2={sx(selected.year)} y2="249" stroke="#fff4cf" strokeDasharray="3 4"/>}
    {marks.map(row => <g key={row.year}>{[['zX', '#e8bf72'], ['zY', '#70d6da']].filter(([key]) => finite(row[key])).map(([key, color]) => <circle key={key} cx={sx(row.year)} cy={sy(row[key])} r={row.year === selectedYear ? 5 : 2.6} fill={color} stroke={row.year === selectedYear ? '#fff9e7' : 'transparent'} onClick={() => onSelect(row.year)} onFocus={() => onSelect(row.year)} data-pair-year={key === 'zX' ? row.year : undefined} tabIndex={key === 'zX' ? row.year === selectedYear ? 0 : -1 : undefined} role={key === 'zX' ? 'button' : undefined} aria-label={key === 'zX' ? `Inspect pair ${row.xYear} / ${row.yYear}` : undefined} onKeyDown={event => pointKey(event, pairs, row, onSelect)}><title>{row.xYear} / {row.yYear} · {key === 'zX' ? 'X' : 'Y'} z = {precise.format(row[key])}</title></circle>)}</g>)}
  </svg><div className={styles.legend}><span><i/><b>X · {x?.label}</b></span><span><i/><b>Y · {y?.label}</b></span></div></>;
}

function Scatter({ pairs, x, y, fit, selectedYear, onSelect }) {
  if (!pairs.length) return <div className={styles.emptyChart}>No complete annual pairs in this selection. The source coverage below explains which years are eligible.</div>;
  const width = 620, height = 370, xs = pairs.map(row => row.x), ys = pairs.map(row => row.y), minX = Math.min(...xs), maxX = Math.max(...xs), minY = Math.min(...ys), maxY = Math.max(...ys);
  const padX = (maxX - minX || Math.abs(maxX) || 1) * .08, padY = (maxY - minY || Math.abs(maxY) || 1) * .08;
  const lowX = minX - padX, highX = maxX + padX, lowY = minY - padY, highY = maxY + padY;
  const sx = value => 85 + (value - lowX) / (highX - lowX) * 495, sy = value => 290 - (value - lowY) / (highY - lowY) * 240;
  const ticksX = Array.from({ length: 4 }, (_, index) => minX + (maxX - minX) * index / 3), ticksY = Array.from({ length: 4 }, (_, index) => minY + (maxY - minY) * index / 3);
  const unique = values => [...new Set(values)];
  return <svg viewBox={`0 0 ${width} ${height}`} role="group" aria-label={`Annual signal scatter plot. ${pairs.length} complete pairs. Horizontal axis X ${x?.unit || ''}; vertical axis Y ${y?.unit || ''}. Select a point or use the paired-year table.`}>
    <defs><clipPath id="signal-scatter-clip"><rect x="85" y="30" width="495" height="260"/></clipPath></defs>
    {unique(ticksX).map(value => <g key={value}><line x1={sx(value)} x2={sx(value)} y1="30" y2="290" stroke="#abc4ce20"/><text x={sx(value)} y="314" textAnchor="middle">{fmt(value)}</text></g>)}
    {unique(ticksY).map(value => <g key={value}><line y1={sy(value)} y2={sy(value)} x1="85" x2="580" stroke="#abc4ce20"/><text x="75" y={sy(value) + 4} textAnchor="end">{fmt(value)}</text></g>)}
    <line x1="85" x2="580" y1="290" y2="290" stroke="#8fadb8"/><line x1="85" x2="85" y1="30" y2="290" stroke="#8fadb8"/>
    <g clipPath="url(#signal-scatter-clip)">{finite(fit.slope) && finite(fit.intercept) && <line x1={sx(lowX)} y1={sy(fit.intercept + fit.slope * lowX)} x2={sx(highX)} y2={sy(fit.intercept + fit.slope * highX)} stroke="#f0d59b" strokeWidth="1.6" strokeDasharray="6 4"/>}{pairs.map((row, index) => <circle key={row.year} cx={sx(row.x)} cy={sy(row.y)} r={selectedYear === row.year ? 6 : 4} fill={selectedYear === row.year ? '#f0d59b' : '#70d6da'} fillOpacity={selectedYear === row.year ? 1 : .45 + index / pairs.length * .5} stroke={selectedYear === row.year ? '#fff8e4' : '#0b2635'} strokeWidth="1" data-pair-year={row.year} role="button" tabIndex={selectedYear === row.year ? 0 : -1} aria-label={`Inspect pair ${row.xYear} / ${row.yYear}: X ${fmt(row.x)}, Y ${fmt(row.y)}`} onClick={() => onSelect(row.year)} onFocus={() => onSelect(row.year)} onKeyDown={event => pointKey(event, pairs, row, onSelect)}><title>{row.xYear} / {row.yYear} · X {fmt(row.x)} · Y {fmt(row.y)}</title></circle>)}</g>
    <text x="332" y="347" textAnchor="middle">X · {x?.unit || 'source units'}</text><text x="18" y="160" textAnchor="middle" transform="rotate(-90 18 160)">Y · {y?.unit || 'source units'}</text>
  </svg>;
}

function Coverage({ axis, entry, coverage, bundle }) {
  const excluded = Array.isArray(coverage?.excluded) ? coverage.excluded : [], gaps = coverage?.missingYears || [];
  const snapshot = PUBLIC_LAB_SNAPSHOTS[entry?.story];
  return <article className={styles.source}><span>{axis} / SOURCE & ELIGIBILITY</span><h3>{entry?.label || 'Chosen signal is loading'}</h3><p>{entry?.method || coverage?.method || 'Annual aggregation is defined by the named source and its source coverage.'}</p>
    <p><b>Source span:</b> {entry?.from ?? '—'}–{entry?.to ?? '—'} · <b>Units:</b> {entry?.unit || '—'}<br/><b>Eligible annual values:</b> {finite(coverage?.eligible) ? coverage.eligible : coverage?.rows?.length ?? '—'} · <b>Rejected annual values:</b> {excludedCount(coverage?.excluded)}</p>
    {gaps.length > 0 && <p><b>Missing years:</b> {gaps.join(', ')}</p>}
    {excluded.length > 0 && <details><summary>{excluded.length} excluded annual {excluded.length === 1 ? 'value' : 'values'}</summary><p>{excluded.map(row => `${row.year}: ${row.reason}${finite(row.count) && finite(row.expected) ? ` (${row.count}/${row.expected} observations)` : ''}`).join('; ')}</p></details>}
    {(bundle?.sources || []).map((source, index) => <p key={index}>{source.url ? <a href={source.url} target="_blank" rel="noreferrer">{source.name || 'Provider source'} ↗</a> : source.name}</p>)}
    {snapshot && <><p>Snapshot retrieved {snapshot.retrievedAt.slice(0, 10)} · <a href={snapshot.path} download>download source bundle</a></p><code>SHA-256 {snapshot.sha256}</code></>}
  </article>;
}

export default function SignalStudio() {
  const { bundles, states, retry } = useSignalBundles();
  const [controls, setControls] = useState({ ...INITIAL }), [selectedYear, setSelectedYear] = useState(null), [preset, setPreset] = useState(SIGNAL_PRESETS[0]?.id || ''), [notice, setNotice] = useState(''), [shareURL, setShareURL] = useState('');
  const restored = useRef(false);
  const catalog = useMemo(() => signalCatalog(bundles), [bundles]);
  const analysis = useMemo(() => analyzeSignals(bundles, controls), [bundles, controls]);
  const pairs = analysis.pairs || [], selected = pairs.find(row => row.year === selectedYear) || pairs.at(-1), chosenYear = selected?.year ?? null;
  const loadedCount = SOURCE_IDS.filter(id => states[id] === 'ready').length, loading = SOURCE_IDS.some(id => !states[id] || states[id] === 'loading'), failed = SOURCE_IDS.filter(id => ['offline', 'waiting'].includes(states[id]));
  useEffect(() => {
    let active = true;
    queueMicrotask(() => {
    if (!active || restored.current) return;
    restored.current = true;
    const params = new URLSearchParams(window.location.search), token = params.get('view');
    if (token) {
      const view = decodeWorkbenchView(token, { workspace: 'signal', sourceBindings: SOURCE_BINDINGS });
      if (view) { setControls({ ...INITIAL, ...view.state }); setSelectedYear(view.state.selectedYear ?? null); setPreset(''); setNotice('Shared investigation restored against the exact source snapshots.'); }
      else setNotice('This shared view could not be restored: its state or source snapshot bindings do not match this edition. The default investigation is shown.');
    } else if (params.has('preset')) {
      const match = SIGNAL_PRESETS.find(item => item.id === params.get('preset'));
      if (match) { setControls({ ...INITIAL, ...match.controls }); setPreset(match.id); }
    }
    });
    return () => { active = false; };
  }, []);
  const update = (key, value) => { setControls(current => ({ ...current, [key]: value })); setPreset(''); setShareURL(''); };
  const changePreset = item => { setControls({ ...INITIAL, ...item.controls }); setSelectedYear(null); setPreset(item.id); setShareURL(''); setNotice(item.description); };
  const downloadPairs = () => {
    const rows = [['X year', 'Y year', `X ${analysis.x?.label || ''} (${analysis.x?.unit || ''}); ${controls.transform}`, `Y ${analysis.y?.label || ''} (${analysis.y?.unit || ''}); ${controls.transform}`, 'Recorded X annual value', 'Recorded Y annual value', 'X standardized z', 'Y standardized z'], ...pairs.map(row => [row.xYear, row.yYear, row.x, row.y, row.rawX, row.rawY, row.zX, row.zY])];
    download(toCSV(rows), 'kfm-signal-pairs.csv', 'text/csv;charset=utf-8'); setNotice(`${pairs.length} complete annual pairs downloaded, with recorded values and transformed values.`);
  };
  const receipt = () => {
    download(JSON.stringify({ schema: 'kfm-signal-investigation-v1', generatedAt: new Date().toISOString(), controls, selectedYear: chosenYear, sourceBindings: SOURCE_BINDINGS, selectionBindings: analysis.bindings, x: analysis.x, y: analysis.y, bounds: analysis.bounds, count: pairs.length, excluded: analysis.excluded, coverage: analysis.coverage, statistics: { pearson: analysis.pearson, spearman: analysis.spearman, rSquared: analysis.rSquared, slope: analysis.slope, intercept: analysis.intercept, reason: analysis.reason }, lagProfile: analysis.lagProfile, methods: ['Annual values are joined by calendar year; a positive lag pairs X(t) with Y(t + lag). Both source years must fall within the selected period.', 'Only complete finite pairs enter transformations, standardization and descriptive statistics. No interpolation or imputation.', 'Neighboring years can be autocorrelated. Shared trends and serial dependence can inflate raw associations.', 'Scanning 11 lags is exploratory; there is no significance claim or best causal lag.', 'No causal inference, hypothesis testing, p-values or adjustment for multiple exploration.'], pairs }, null, 2) + '\n', 'kfm-signal-investigation.json');
    setNotice('Investigation receipt downloaded with paired values, methods, statistics and exact snapshot hashes.');
  };
  const share = async () => {
    const url = new URL('/labs/signals', window.location.origin);
    url.searchParams.set('view', encodeWorkbenchView({ workspace: 'signal', state: { ...controls, selectedYear: chosenYear }, sourceBindings: SOURCE_BINDINGS }));
    setShareURL(url.href);
    try { await navigator.clipboard.writeText(url.href); setNotice('Exact investigation link copied. It reopens with these source snapshot bindings.'); }
    catch { setNotice('The exact investigation link is ready below. Select it to copy.'); }
  };
  const swapSignals = () => { setControls(current => ({ ...current, x: current.y, y: current.x, lag: -(Number(current.lag) || 0) })); setPreset(''); setShareURL(''); setNotice('Signals swapped. The lag sign also changed to preserve the same temporal direction.'); };
  const commonPeriod = () => {
    if (!analysis.x || !analysis.y) return;
    const from = Math.max(Number(analysis.x.from), Number(analysis.y.from)), to = Math.min(Number(analysis.x.to), Number(analysis.y.to));
    if (finite(from) && finite(to) && from <= to) { setControls(current => ({ ...current, from, to })); setPreset(''); setShareURL(''); setNotice('Analysis period set to the overlapping source years. Annual eligibility rules still apply.'); }
  };
  const restoreNotebook = entry => { setControls({ ...INITIAL, ...entry.state }); setSelectedYear(entry.state.selectedYear ?? null); setPreset(''); setNotice('Saved investigation restored from this browser.'); setShareURL(''); };
  return <div className={styles.page}>
    <header className={styles.masthead}><Link prefetch={false} className={styles.brand} href="/labs"><strong>KFM</strong><span>KANSAS FRONTIER MATRIX<small>The research atlas</small></span></Link><nav className={styles.nav} aria-label="Research navigation"><Link prefetch={false} href="/labs">All labs ↗</Link><Link prefetch={false} href="/labs/observatory">County Observatory ↗</Link></nav></header>
    <main><section className={styles.hero} aria-labelledby="signal-title"><div><span className={styles.eyebrow}>CONNECTED SCIENCE / THE KANSAS RECORD</span><h1 id="signal-title">Find the rhythm.<br/><em>Question the connection.</em></h1><p>Put two Kansas signals on the same clock. Follow energy transitions, changing climate, river flows and recorded events. Separate long trends from year-to-year movement, inspect every pair and take the evidence with you.</p></div><aside className={styles.heroAside}><div><strong>5</strong><span>public source families</span></div><div><strong>{catalog.length || '—'}</strong><span>annual signals available</span></div><div><strong>11</strong><span>calendar lags to inspect</span></div><p>A shared pattern is a starting point for a question. It does not establish a mechanism or a cause.</p></aside></section>
      <div className={styles.workbench}>
        <section aria-label="Named investigations" className={styles.presets}><span>START WITH A QUESTION</span>{SIGNAL_PRESETS.map(item => <button key={item.id} type="button" className={styles.preset} aria-pressed={preset === item.id} onClick={() => changePreset(item)} title={item.description}>{item.title}</button>)}</section>
        {loading && <p className={styles.status} role="status">Reading and checking public source snapshots · {loadedCount} of {SOURCE_IDS.length} ready. Selected signals appear as their sources arrive.</p>}
        {failed.length > 0 && <p className={`${styles.status} ${styles.error}`} role="status">{failed.length} source {failed.length === 1 ? 'snapshot is' : 'snapshots are'} unavailable. Other loaded signals remain usable. <button type="button" onClick={retry}>Retry missing sources</button></p>}
        {notice && <p className={styles.status} role="status">{notice}</p>}
        <section className={styles.controls} aria-label="Signal analysis controls"><AxisControl axis="X" selected={controls.x} catalog={catalog} onChange={value => update('x', value)}/><AxisControl axis="Y" selected={controls.y} catalog={catalog} onChange={value => update('y', value)}/><div className={styles.period}><span>ANALYSIS PERIOD · BOTH SOURCE YEARS</span><label>From year<input aria-label="Analysis from year" type="number" min="1800" max="2100" value={controls.from ?? ''} onChange={event => update('from', event.target.value === '' ? '' : Number(event.target.value))}/></label><label>Through year<input aria-label="Analysis through year" type="number" min="1800" max="2100" value={controls.to ?? ''} onChange={event => update('to', event.target.value === '' ? '' : Number(event.target.value))}/></label></div><label className={styles.control}><span>LAG · YEARS</span><select aria-label="Calendar lag in years" value={controls.lag ?? 0} onChange={event => update('lag', Number(event.target.value))}>{Array.from({ length: 11 }, (_, index) => index - 5).map(lag => <option key={lag} value={lag}>{lag > 0 ? '+' : ''}{lag}{lag === 0 ? ' · same year' : lag > 0 ? ' · X precedes Y' : ' · Y precedes X'}</option>)}</select></label><label className={styles.control}><span>ANALYSIS MODE</span><select aria-label="Signal transformation" value={controls.transform || 'raw'} onChange={event => update('transform', event.target.value)}>{Object.entries(TRANSFORMS).map(([key, value]) => <option key={key} value={key}>{value}</option>)}</select></label><div className={styles.controlActions}><button type="button" onClick={swapSignals} disabled={!analysis.x || !analysis.y}>Swap X ↔ Y</button><button type="button" onClick={commonPeriod} disabled={!analysis.x || !analysis.y}>Use overlapping source years</button></div><p className={styles.controlNote}>{Number(controls.lag) > 0 ? `X in year t is paired with Y in year t + ${controls.lag}.` : Number(controls.lag) < 0 ? `X in year t is paired with Y in year t − ${Math.abs(controls.lag)}.` : 'X and Y are paired within the same calendar year.'} Changing the mode recalculates the full eligible selection. Lines connect consecutive paired years; gaps stay open.</p></section>
        <div className={styles.analysisHeading}><div><h2>{TRANSFORMS[controls.transform] || 'Annual signal comparison'}</h2><p>{analysis.x?.label || 'Chosen X signal'} <span aria-hidden="true">×</span> {analysis.y?.label || 'Chosen Y signal'}</p></div><span>FULL ELIGIBLE SELECTION / NO IMPUTATION</span></div>
        <section className={styles.statistics} aria-label="Descriptive association statistics"><div className={styles.stat}><span>COMPLETE ANNUAL PAIRS</span><strong>{pairs.length}</strong><small>{excludedCount(analysis.excluded)} candidate pairs excluded</small></div><div className={styles.stat}><span>PEARSON r</span><strong>{coeff(analysis.pearson)}</strong><small>Linear association</small></div><div className={styles.stat}><span>SPEARMAN ρ</span><strong>{coeff(analysis.spearman)}</strong><small>Rank association · tied ranks averaged</small></div><div className={styles.stat}><span>DESCRIPTIVE FIT R²</span><strong>{coeff(analysis.rSquared)}</strong><small>Ordinary least squares with intercept</small></div><div className={styles.stat}><span>FIT SLOPE · Y / X</span><strong>{finite(analysis.slope) ? precise.format(analysis.slope) : '—'}</strong><small>{analysis.reason || 'Describes these paired values only'}</small></div></section>
        {finite(analysis.pearson) && pairs.length > 0 && <p className={styles.readout}><b>Read this result.</b> In these {pairs.length} complete pairs, the {controls.transform === 'raw' ? 'recorded annual values' : controls.transform === 'difference' ? 'year-to-year changes' : 'values after linear trends are removed'} have a {analysis.pearson < 0 ? 'negative' : analysis.pearson > 0 ? 'positive' : 'zero'} linear association (r = {coeff(analysis.pearson)}). X years {pairs[0].xYear}–{pairs.at(-1).xYear} are paired with Y years {pairs[0].yYear}–{pairs.at(-1).yYear}. This describes the selected record; it does not explain why.</p>}
        <div className={styles.plots}><section className={styles.plot} aria-labelledby="overlay-title"><header><h3 id="overlay-title">Two signals. One paired clock.</h3><p>Centered and scaled using this selection. The overlay compares shape; the recorded units remain in the table.</p></header><Overlay pairs={pairs} x={analysis.x} y={analysis.y} selectedYear={chosenYear} onSelect={setSelectedYear} lag={Number(controls.lag) || 0}/><p className={styles.plotFooter}>Horizontal axis is X year. Each Y value belongs to its lagged year. Standardization uses the sample standard deviation of all transformed pairs.</p></section><section className={styles.plot} aria-labelledby="scatter-title"><header><h3 id="scatter-title">Look at the relationship.</h3><p>One point per complete annual pair. Select a point to inspect the same pair in both views.</p></header><Scatter pairs={pairs} x={analysis.x} y={analysis.y} fit={analysis} selectedYear={chosenYear} onSelect={setSelectedYear}/><p className={styles.plotFooter}>Dashed line: descriptive OLS fit. Points are all complete pairs, ordered from earlier to later with increasing opacity. No confidence band or inferential claim.</p></section></div>
        {selected && <aside className={styles.inspector} aria-label="Selected annual pair"><div><span>INSPECTING THE RECORD</span><h3>{selected.xYear === selected.yYear ? selected.xYear : `${selected.xYear} / ${selected.yYear}`}</h3></div><div><span>X · {analysis.x?.label} · {selected.xYear}</span><strong>{fmt(selected.x)} {analysis.x?.unit}</strong><small>Recorded annual value {fmt(selected.rawX)} · standardized {coeff(selected.zX)}</small></div><div><span>Y · {analysis.y?.label} · {selected.yYear}</span><strong>{fmt(selected.y)} {analysis.y?.unit}</strong><small>Recorded annual value {fmt(selected.rawY)} · standardized {coeff(selected.zY)}</small></div></aside>}
        <div className={styles.lagAndMethod}><section className={styles.panel} aria-labelledby="lag-title"><h3 id="lag-title">Does timing change the pattern?</h3><p>Compare the same analysis mode at every lag. Each lag can have a different set of eligible pairs. Select a bar to inspect it.</p><div className={styles.lagBars} aria-label="Pearson correlation by calendar lag">{(analysis.lagProfile || []).map(row => <button type="button" key={row.lag} aria-pressed={Number(controls.lag) === row.lag} data-negative={finite(row.pearson) && row.pearson < 0} aria-label={`Lag ${row.lag} years. Pearson ${coeff(row.pearson)}, ${row.count} complete pairs. Select this lag.`} onClick={() => update('lag', row.lag)} style={{ '--bar-size': `${finite(row.pearson) ? Math.max(2, Math.abs(row.pearson) * 65) : 2}px` }}><b>{coeff(row.pearson)}</b><i aria-hidden="true"/><span>{row.lag > 0 ? '+' : ''}{row.lag}</span><small>n={row.count}</small></button>)}</div><p>Bar height is |r|. Cyan = positive; gold = negative. A dash means there are too few complete pairs or an axis has no variation.</p></section><section className={styles.panel} aria-labelledby="methods-title"><h3 id="methods-title">Know what enters the instrument.</h3><div className={styles.methodLine}><b>Annual eligibility</b><span>NOAA needs all 12 months. River means need at least 90% of calendar days. Event zeros appear only within known source coverage.</span></div><div className={styles.methodLine}><b>Remove trends</b><span>Fit each paired signal against calendar time, then compare the residuals. This is descriptive linear detrending.</span></div><div className={styles.methodLine}><b>Differences</b><span>Compare changes between consecutive paired calendar years. Gaps are excluded, never bridged.</span></div><div className={styles.methodLine}><b>Missing values</b><span>Unknown source values stay unknown. No interpolation, filling or invented years.</span></div></section></div>
        <p className={styles.warning}><b>Explore a hypothesis; do not declare a cause.</b> Trends, autocorrelation, shared external factors, incomplete reporting and selected periods can create apparent associations. Searching many signals or lags increases the chance of finding a striking pattern. These are descriptive statistics without hypothesis tests, significance claims or causal adjustment.</p>
        <section className={styles.dataSection} aria-labelledby="pairs-title"><div className={styles.sectionHead}><div><h2 id="pairs-title">Every pair, in the open.</h2><p>{pairs.length} complete pairs · {analysis.bounds?.from ?? controls.from}–{analysis.bounds?.to ?? controls.to} · recorded values accompany each transformation in the download.</p></div><div className={styles.actions}><button type="button" onClick={downloadPairs} disabled={!pairs.length}>Download paired CSV ↓</button><button type="button" onClick={receipt} disabled={!pairs.length}>Download receipt ↓</button><button type="button" onClick={share} className={styles.primary}>Share exact investigation ↗</button><button type="button" onClick={() => window.print()} disabled={!pairs.length}>Print investigation</button></div></div><div className={styles.tableScroll}><table className={styles.table}><caption className={styles.srOnly}>Complete annual pairs for this selected analysis. Select an X year to inspect its pair.</caption><thead><tr><th scope="col">X year / inspect</th><th scope="col">Y year</th><th scope="col">X · {analysis.x?.unit || 'value'}</th><th scope="col">Y · {analysis.y?.unit || 'value'}</th><th scope="col">Recorded X</th><th scope="col">Recorded Y</th></tr></thead><tbody>{pairs.map(row => <tr key={row.year} aria-selected={chosenYear === row.year}><td><button type="button" onClick={() => setSelectedYear(row.year)} aria-label={`Inspect annual pair ${row.xYear} / ${row.yYear}`}>{row.xYear}</button></td><td>{row.yYear}</td><td>{fmt(row.x)}</td><td>{fmt(row.y)}</td><td>{fmt(row.rawX)}</td><td>{fmt(row.rawY)}</td></tr>)}{!pairs.length && <tr><td colSpan={6}>No complete pairs. Choose another period or inspect source eligibility below.</td></tr>}</tbody></table></div></section>
        {shareURL && <label className={styles.shareBox}>Reopen this investigation against the same snapshot edition<input readOnly value={shareURL} aria-label="Exact investigation share link" onFocus={event => event.target.select()}/></label>}
        <div className={styles.notebook}><NotebookPanel workspace="signal" state={{ ...controls, selectedYear: chosenYear }} sourceBindings={SOURCE_BINDINGS} onRestore={restoreNotebook}/></div>
        <section className={styles.sourceGrid} aria-label="Source coverage and snapshot bindings"><Coverage axis="X" entry={analysis.x} coverage={analysis.coverage?.x} bundle={bundles[analysis.x?.story]}/><Coverage axis="Y" entry={analysis.y} coverage={analysis.coverage?.y} bundle={bundles[analysis.y?.story]}/></section>
        <details className={styles.details}><summary>Read the interpretation and reproduction notes</summary><ul><li>Climate, energy, gauges and event catalogues observe different things at different geographic supports. A statewide aggregate and a single river gauge are not interchangeable samples of Kansas.</li><li>Some signals overlap by construction: M≥3 earthquakes are part of the M≥1 catalogue, and energy accounting categories can overlap. Their association does not represent independent evidence.</li><li>Recorded events reflect source definitions, thresholds and changes in detection or reporting. Counts do not measure individual exposure or harm; unknown impact values are not zero.</li><li>Raw mode compares annual measurements. Detrended mode compares residuals from separate linear trends on the complete paired period. Difference mode compares consecutive-year changes. Standardization is for the overlay; correlation and fit use the transformed values in their original units.</li><li>Neighboring years can be autocorrelated. Shared trends and serial dependence can inflate raw associations. Scanning 11 lags is exploratory; no lag is identified as statistically significant or the best causal lag.</li><li>All displayed statistics and exports use the full eligible pair set. Each receipt records source hashes, years, lag, transformations, coverage and paired values so another visitor can examine the same result.</li></ul></details>
      </div></main><footer className={styles.footer}><span>KANSAS FRONTIER MATRIX / SOURCE-BOUND EXPLORATION</span><Link prefetch={false} href="/labs">Return to the research atlas ↑</Link></footer>
  </div>;
}

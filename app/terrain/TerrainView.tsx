'use client';
import Link from 'next/link';
import { useEffect, useMemo, useRef, useState } from 'react';
import { createTerrainController, initialTerrainState, type TerrainController } from './terrain-controller';
import { neonScienceDatasetJSON } from '../neon-lidar-science';
import { neonElevationDomain, neonSampleColor } from '../neon-lidar-preview';
import '../maplibre-seam.css';
import styles from './terrain.module.css';

const MODES = [
  { id: 'dtm', label: 'Ground', detail: 'DTM · sampled elevation' },
  { id: 'dsm', label: 'Surface', detail: 'DSM · sampled elevation' },
  { id: 'chm', label: 'Canopy', detail: 'CHM · independent provider height' },
] as const;
const number = (value: number | null | undefined, digits = 2) => value == null ? 'No data' : value.toLocaleString('en-US', { minimumFractionDigits: digits, maximumFractionDigits: digits });
const stamp = (value: string) => new Date(value).toISOString().replace('T', ' ').replace('.000Z', ' UTC');

export default function TerrainView() {
  const host = useRef<HTMLDivElement>(null), session = useRef<TerrainController | null>(null);
  const [view, setView] = useState(initialTerrainState), [attempt, setAttempt] = useState(0);
  useEffect(() => {
    if (!host.current) return;
    const motion = window.matchMedia('(prefers-reduced-motion: reduce)');
    const controller = createTerrainController(host.current, setView, motion.matches);
    session.current = controller;
    const changeMotion = () => controller.setReducedMotion(motion.matches);
    motion.addEventListener('change', changeMotion);
    return () => { motion.removeEventListener('change', changeMotion); controller.dispose(); if (session.current === controller) session.current = null; };
  }, [attempt]);
  const retry = () => { session.current?.dispose(); session.current = null; setView(initialTerrainState()); setAttempt(value => value + 1); };
  const dataset = view.dataset, receipt = dataset?.receipt, source = receipt?.preview.source, grid = receipt?.preview.grid;
  const failed = view.phase === 'error' || view.phase === 'unsupported', enabled = Boolean(dataset) && !failed;
  const mode = MODES.find(item => item.id === view.mode)!;
  const legend = useMemo(() => {
    if (!receipt) return null;
    const domain: [number, number] | null = view.mode === 'chm' ? [0, 30] : neonElevationDomain(receipt.preview);
    if (!domain) return null;
    let min = Infinity, max = -Infinity;
    for (const value of receipt.preview.grid[view.mode]) if (value !== null) { min = Math.min(min, value); max = Math.max(max, value); }
    return { domain, min: min === Infinity ? null : min, max: max === -Infinity ? null : max,
      ramp: `linear-gradient(to right, ${[0, 1 / 3, 2 / 3, 1].map(fraction => neonSampleColor(domain[0] * (1 - fraction) + domain[1] * fraction, domain)).join(', ')})` };
  }, [receipt, view.mode]);
  const saveSource = () => {
    if (!dataset) return;
    const url = URL.createObjectURL(new Blob([neonScienceDatasetJSON(dataset)], { type: 'application/json' }));
    const link = document.createElement('a'); link.href = url; link.download = 'kfm-konza-terrain-science.json';
    document.body.append(link); link.click(); link.remove(); setTimeout(() => URL.revokeObjectURL(url), 1000);
  };
  return <div className={styles.page}>
    <header className={styles.header}><Link href="/" className={styles.brand}>KFM <span>/ 3D TERRAIN</span></Link><nav aria-label="Terrain navigation"><Link href="/">Main map ↗</Link><Link href="/labs/terrain">Terrain Science ↗</Link></nav></header>
    <main className={styles.main}>
      <div className={styles.titleRow}><div><p className={styles.eyebrow}>NEON / HISTORICAL KONZA PRAIRIE</p><h1>A landscape, raised.</h1></div><p className={styles.identity}>September 2024 catalog month · 1 km tile<br/><span>Sampled preview · scientific review pending · not admitted</span></p></div>
      <section aria-label="Terrain display controls" className={styles.toolbar}>
        <div className={styles.modes} role="group" aria-label="Observed surface">{MODES.map(item => <button key={item.id} type="button" disabled={!enabled} aria-pressed={view.mode === item.id} onClick={() => session.current?.setMode(item.id)}><b>{item.label}</b><span>{item.detail}</span></button>)}</div>
        <label className={styles.scale}>Visual height <output htmlFor="terrain-scale">{view.scale}×</output><input id="terrain-scale" aria-label="Vertical exaggeration" type="range" min="1" max="5" step="0.5" value={view.scale} disabled={!enabled || view.representation === 'flat'} onChange={event => session.current?.setScale(Number(event.target.value))}/><span>1×–5× · measurements stay unscaled</span></label>
      </section>
      <div className={styles.workspace}>
        <section className={styles.landscape} aria-label="Interactive Konza landscape">
          <div className={styles.mapFrame}>
            <div className={styles.map} ref={host} data-terrain-map=""/>
            <div className={styles.mapBadge}><b>{mode.label} · {view.representation === 'columns' ? `${view.scale}× relative sampled heights` : '2D sample footprints'}</b><span>{view.representation === 'columns' ? `Local baseline ${number(view.metadata?.baseline_m)} m · visual exaggeration` : 'Overhead display · source measurements unchanged'}</span></div>
            {view.phase !== 'ready' && <div className={styles.mapStatus} data-state={view.phase} role={failed ? 'alert' : 'status'}><p className={styles.eyebrow}>{failed ? 'LANDSCAPE UNAVAILABLE' : 'OPENING THE LANDSCAPE'}</p><h2>{view.phase === 'unsupported' ? '3D needs WebGL2.' : failed ? 'The landscape could not open.' : view.phase === 'loading' ? 'Loading Konza Prairie…' : 'Drawing the sampled relief…'}</h2><p>{view.message}</p>{failed && <div className={styles.recovery}><button type="button" onClick={retry}>Retry 3D</button><Link href="/labs/terrain">Open 2D Science inspector ↗</Link></div>}</div>}
          </div>
          {legend && <div className={styles.legend} aria-label={`${mode.label} color scale in original metres`}><span>{mode.label} color · source metres</span><span>{number(legend.domain[0])} m</span><i aria-hidden="true" style={{ background: legend.ramp }}/><span>{number(legend.domain[1])} m</span><small>Sample range {number(legend.min)}–{number(legend.max)} m{view.mode === 'chm' ? ' · colors saturate at 30 m' : ' · shared ground/surface scale'}</small></div>}
          <div className={styles.camera} role="group" aria-label="Map camera"><button type="button" disabled={!enabled} onClick={() => session.current?.show3D()}>Fit &amp; tilt 3D</button><button type="button" disabled={!enabled} aria-pressed={view.representation === 'flat'} onClick={() => session.current?.show2D()}>2D samples</button><button type="button" disabled={!enabled} onClick={() => session.current?.turn(-30)} aria-label="Rotate landscape left">↶ Rotate</button><button type="button" disabled={!enabled} onClick={() => session.current?.turn(30)} aria-label="Rotate landscape right">Rotate ↷</button></div>
          <p className={styles.mapHint}>Drag to pan · scroll or pinch to zoom · right-drag to orbit · click a column to read its sample.</p>
          <p className={styles.sampling}>{grid ? `${grid.width} × ${grid.height} samples · ${grid.preview_resolution_m} m display footprints · nearest native ${grid.source_resolution_m} m readings` : '100 × 100 samples · 10 m display footprints · nearest native 1 m readings'}. Columns show relative heights, not a surveyed terrain mesh.</p>
        </section>
        <aside className={styles.inspector}>
          <section aria-labelledby="terrain-story-title" className={styles.stories}><p className={styles.eyebrow}>01 / FOLLOW THE SAMPLES</p><h2 id="terrain-story-title">Four ways into the tile.</h2><div>{view.stops.length ? view.stops.map((stop, index) => <button type="button" key={stop.id} disabled={!enabled} aria-pressed={view.activeStop === stop.id} onClick={() => session.current?.focus(stop.id)}><span className={styles.storyIndex}>0{index + 1}</span><span><b>{stop.label}</b><small>Row {stop.row + 1} · column {stop.column + 1}</small></span><strong>{number(stop.value_m)}<small>m</small></strong></button>) : <p className={styles.muted}>Story stops use actual sample extrema once the receipt is validated.</p>}</div></section>
          <section className={styles.probe} aria-labelledby="terrain-probe-title"><p className={styles.eyebrow}>02 / READ THE SOURCE</p><h2 id="terrain-probe-title">One sample. Original values.</h2><div className={styles.coordinates}>{(['row', 'column'] as const).map(axis => <label key={axis}>{axis === 'row' ? 'Row' : 'Column'}<input type="text" inputMode="numeric" pattern="[0-9]*" maxLength={4} disabled={!enabled} value={view[axis]} aria-invalid={enabled && !view.probe ? true : undefined} onChange={event => session.current?.setCoordinate(axis, event.target.value)}/></label>)}</div>
            {view.probe ? <><dl className={styles.readings}><div><dt>Ground · DTM</dt><dd>{number(view.probe.dtm)} <small>m</small></dd></div><div><dt>Surface · DSM</dt><dd>{number(view.probe.dsm)} <small>m</small></dd></div><div><dt>Provider canopy · CHM</dt><dd>{number(view.probe.chm)} <small>m</small></dd></div><div><dt>DSM − DTM</dt><dd>{number(view.probe.surfaceAboveGround)} <small>m</small></dd></div></dl><p className={styles.native}>Native sample · easting {number(view.probe.easting, 1)} m<br/>northing {number(view.probe.northing, 1)} m</p>{view.probe.differenceIssue && <p className={styles.caution}>DSM − DTM QA: {view.probe.differenceIssue}. Source values are retained.</p>}</> : <p className={styles.muted}>{dataset ? `Enter row 1–${grid?.height} and column 1–${grid?.width} to inspect a sample.` : 'Readings appear after the dataset is validated.'}</p>}
            <p className={styles.smallNote}>Provider CHM is independent of DSM − DTM. Canopy columns sit on sampled ground; their tops are not DSM. Missing values remain missing.</p>
          </section>
        </aside>
      </div>
      <div className={styles.reviewStrip}><p><b>Preview, not ground truth.</b> {receipt ? <>Native canopy has a retained {number(receipt.review.canopy_native_max_m)} m maximum and {receipt.review.canopy_native_cells_above_50m.toLocaleString('en-US')} cells above 50 m, still under review. Those native outliers are not located by this sampled display.</> : <>Native canopy outliers and reference systems remain under review. Source-specific statistics appear after the receipt is validated.</>} No independent accuracy is established.</p><Link href="/labs/terrain">Compare distributions &amp; relationships in Science →</Link></div>
      {receipt && source && <section className={styles.sourceDetails} aria-label="Source and interpretation"><p className={receipt.cache.state === 'stale' ? styles.caution : styles.cache}><b>{receipt.cache.state === 'stale' ? 'Stale cached package' : 'Provider preview · dev-processed'}.</b> Relay cache {stamp(receipt.cache.at)} · package prepared {stamp(receipt.generatedAt)}. These are processing times, not the flight date.</p><details><summary>Source files, method &amp; limitations <span>3 original SHA-256 references</span></summary><div className={styles.provenance}><dl><div><dt>Recorded identity</dt><dd>{source.site} · catalog {source.month} · run {source.acquisition_run} · {source.release}<br/>{source.tile}</dd></div><div><dt>Vertical reference</dt><dd>{source.vertical_reference}<br/>{source.vertical_reference_basis}</dd></div><div><dt>Recorded horizontal CRS</dt><dd>{source.horizontal_crs}</dd></div><div><dt>Canopy floor</dt><dd>{source.canopy_floor_m === null ? 'Unknown' : `${source.canopy_floor_m} m`} · {source.canopy_floor_basis}</dd></div></dl><ul>{dataset.bundle.data.limits.map(limit => <li key={limit}>{limit}</li>)}{receipt.review.notes.map(note => <li key={note}>{note}</li>)}</ul><p>The recorded acquisition run is not independent authentication. Offline geographic display corners do not establish coordinate epoch or horizontal registration accuracy. Heights are unchanged. {view.metadata?.omitted_cells ? `${view.metadata.omitted_cells} of ${view.metadata.input_cells} available display cells are omitted from 3D because required heights are unavailable or outside the ${view.metadata.render_height_limit_m} m rendering limit.` : 'No display height is treated as a field accuracy estimate.'}</p><div className={styles.hashes}>{source.files.map(file => <div key={file.kind}><b>{file.kind.toUpperCase()} · {file.product}</b><span>{file.name} · {file.bytes.toLocaleString('en-US')} bytes</span><code>{file.sha256}</code></div>)}</div><button type="button" onClick={saveSource}>Download source-linked Science JSON ↓</button><p>{source.attribution} · <a href="https://www.neonscience.org/usage-policies" target="_blank" rel="noreferrer">NEON usage policy ↗</a> · <a href="https://www.neonscience.org/data-collection/lidar" target="_blank" rel="noreferrer">LiDAR methods ↗</a></p></div></details></section>}
    </main><footer className={styles.footer}><span>KANSAS FRONTIER MATRIX / ONE HISTORICAL TILE</span><span>Free public preview · no subscription</span></footer>
  </div>;
}

"use client";

import { useEffect, useId, useMemo, useRef, useState, type PointerEvent } from "react";
import { createAcquisitionSession } from "./acquisition-client";
import { neonElevationDomain, neonLidarProbe, neonLidarProfile, neonSampleColor, parseNeonLidarPreview, readNeonLidarLocalJson, type NeonLidarMode, type NeonLidarProfileAxis, type NeonLidarPreview } from "./neon-lidar-preview";
import { readNeonLidarPilot, type NeonPilotReceipt } from "./neon-lidar-pilot-client";
import styles from "./neon-lidar-panel.module.css";

const MODES: { kind: NeonLidarMode; label: string; short: string }[] = [
  { kind: "dtm", label: "Ground elevation", short: "DTM" },
  { kind: "dsm", label: "Surface elevation", short: "DSM" },
  { kind: "chm", label: "Canopy height", short: "CHM" },
];
const INITIAL_NOTICE = "Choose a prepared local JSON to compare terrain, surface and canopy at the same location.";
const meters = (value: number | null) => value === null ? "NoData" : `${value.toFixed(2)} m`;
const coordinate = (value: number) => value.toLocaleString("en-US", { minimumFractionDigits: 1, maximumFractionDigits: 1 });
const coordinateIndex = (input: string, limit: number): number | null => /^\d+$/.test(input) && Number.isInteger(Number(input)) && Number(input) >= 1 && Number(input) <= limit ? Number(input) - 1 : null;

function GridCanvas({ preview, mode, selected, select, descriptionId, hover = true }: {
  preview: NeonLidarPreview; mode: NeonLidarMode; selected: { row: number; column: number } | null;
  select: (selection: { row: number; column: number }) => void; descriptionId: string; hover?: boolean;
}) {
  const ref = useRef<HTMLCanvasElement>(null);
  const domain = useMemo(() => mode === "chm" ? [0, 30] as [number, number] : neonElevationDomain(preview), [mode, preview]);
  useEffect(() => {
    const canvas = ref.current, ctx = canvas?.getContext("2d");
    if (!canvas || !ctx) return;
    const { width, height } = preview.grid;
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.imageSmoothingEnabled = false;
    preview.grid[mode].forEach((value, index) => {
      if (value === null || !domain) return;
      const column = index % width, row = Math.floor(index / width);
      const x = Math.floor(column * canvas.width / width), y = Math.floor(row * canvas.height / height);
      const right = Math.floor((column + 1) * canvas.width / width), bottom = Math.floor((row + 1) * canvas.height / height);
      ctx.fillStyle = neonSampleColor(value, domain);
      ctx.fillRect(x, y, right - x, bottom - y);
      if (mode === "chm" && value > 30) {
        ctx.fillStyle = "#c77532";
        ctx.fillRect(right - Math.max(1, Math.floor((right - x) / 3)), y, Math.max(1, Math.floor((right - x) / 3)), Math.max(1, Math.floor((bottom - y) / 3)));
      }
    });
    if (selected) {
      const x = Math.floor(selected.column * canvas.width / width), y = Math.floor(selected.row * canvas.height / height);
      const w = Math.floor((selected.column + 1) * canvas.width / width) - x, h = Math.floor((selected.row + 1) * canvas.height / height) - y;
      ctx.strokeStyle = "#091710"; ctx.lineWidth = 3; ctx.strokeRect(x + 1.5, y + 1.5, w - 3, h - 3);
      ctx.strokeStyle = "#fff2b4"; ctx.lineWidth = 1; ctx.strokeRect(x + 1.5, y + 1.5, w - 3, h - 3);
    }
  }, [preview, mode, selected, domain]);
  function pointer(event: PointerEvent<HTMLCanvasElement>) {
    const rect = event.currentTarget.getBoundingClientRect();
    if (!rect.width || !rect.height) return;
    select({
      column: Math.max(0, Math.min(preview.grid.width - 1, Math.floor((event.clientX - rect.left) / rect.width * preview.grid.width))),
      row: Math.max(0, Math.min(preview.grid.height - 1, Math.floor((event.clientY - rect.top) / rect.height * preview.grid.height))),
    });
  }
  return <div className={styles.canvasFrame}>
    <canvas ref={ref} width={preview.grid.width * 4} height={preview.grid.height * 4} role="img" aria-label={`${MODES.find(item => item.kind === mode)?.label}, north-up local sampled raster`} aria-describedby={descriptionId}
      onPointerMove={event => { if (hover && event.pointerType === "mouse") pointer(event); }} onPointerDown={pointer}>
      Use the row and column controls to read every numeric sample without the canvas.
    </canvas>
    <span className={styles.north} aria-hidden="true">N ↑</span>
  </div>;
}

type Profile = NonNullable<ReturnType<typeof neonLidarProfile>>;
type ProfileKey = "dtm" | "dsm" | "chm" | "surfaceAboveGround";
type ProfileSeries = { key: ProfileKey; label: string; color: string; shape: "circle" | "diamond" | "square" };
const ELEVATION_SERIES: ProfileSeries[] = [
  { key: "dtm", label: "DTM · ground", color: "#8cdee2", shape: "circle" },
  { key: "dsm", label: "DSM · surface", color: "#f2ce86", shape: "diamond" },
];
const HEIGHT_SERIES: ProfileSeries[] = [
  { key: "chm", label: "Provider CHM", color: "#c5dfa3", shape: "circle" },
  { key: "surfaceAboveGround", label: "DSM − DTM", color: "#f2ce86", shape: "square" },
];
const profileNumber = (value: number) => Math.abs(value) >= 100000 || (value !== 0 && Math.abs(value) < .01) ? value.toExponential(2) : value.toLocaleString("en-US", { maximumFractionDigits: 2 });
function ProfileMark({ shape, x, y, color, size = 3 }: { shape: ProfileSeries["shape"]; x: number; y: number; color: string; size?: number }) {
  if (shape === "circle") return <circle cx={x} cy={y} r={size} fill={color} />;
  if (shape === "diamond") return <path d={`M ${x} ${y-size-1} L ${x+size+1} ${y} L ${x} ${y+size+1} L ${x-size-1} ${y} Z`} fill={color} />;
  return <rect x={x-size} y={y-size} width={size*2} height={size*2} fill="#0b2634" stroke={color} strokeWidth={1.6} />;
}
function ProfilePlot({ profile, selectedIndex, select, title, series, includeZero, id }: {
  profile: Profile; selectedIndex: number; select: (index: number) => void; title: string; series: ProfileSeries[]; includeZero: boolean; id: string;
}) {
  const values = profile.samples.flatMap(sample => series.flatMap(item => sample[item.key] === null ? [] : [sample[item.key] as number]));
  const domain = values.length ? [Math.min(...values, ...(includeZero ? [0] : [])), Math.max(...values, ...(includeZero ? [0] : []))] : null;
  const left = "2%", right = "98%", top = 10, bottom = 132, distance = profile.samples.at(-1)?.distance_m ?? 0;
  const x = (value: number) => `${2+(distance ? value/distance : .5)*96}%`;
  const y = (value: number) => {
    if (!domain || domain[0] === domain[1]) return (top+bottom)/2;
    const span = domain[1]-domain[0];
    // Dividing before subtraction preserves finite coordinates even for +/-1e308.
    const fraction = Number.isFinite(span) ? (value-domain[0])/span : (value/2-domain[0]/2)/(domain[1]/2-domain[0]/2);
    return bottom-Math.max(0,Math.min(1,fraction))*(bottom-top);
  };
  function pointer(event: PointerEvent<SVGSVGElement>) {
    const rect = event.currentTarget.getBoundingClientRect();
    if (!rect.width) return;
    const targetDistance = Math.max(0,Math.min(1,((event.clientX-rect.left)/rect.width-.02)/.96))*distance;
    let nearest = 0;
    profile.samples.forEach((sample,index) => { if (Math.abs(sample.distance_m-targetDistance) < Math.abs(profile.samples[nearest].distance_m-targetDistance)) nearest=index; });
    select(nearest);
  }
  return <figure className={styles.profilePlot}>
    <figcaption><strong>{title}</strong><span>Dynamic profile scale · {includeZero ? "height" : "source elevation"} (m){includeZero ? " · includes zero" : ""}</span></figcaption>
    <ul className={styles.profileLegend}>{series.map(item => <li key={item.key}><svg width="14" height="14" viewBox="0 0 14 14" aria-hidden="true"><ProfileMark shape={item.shape} x={7} y={7} color={item.color} /></svg><span>{item.label}</span><span className={styles.profileMissing}>{profile.samples.filter(sample => sample[item.key] === null).length} missing</span></li>)}</ul>
    <div className={styles.profileGraph}><div className={styles.profileScale} aria-hidden="true"><span>{domain ? profileNumber(domain[1]) : "—"}</span><span>{domain ? profileNumber(domain[0]) : "—"}</span></div><div className={styles.profileDrawing}><svg width="100%" height="142" className={styles.profileChart} role="img" aria-labelledby={`${id}-title ${id}-description`} onPointerDown={pointer}>
      <title id={`${id}-title`}>{title}, discrete retained source samples</title>
      <desc id={`${id}-description`}>{domain ? `Dynamic vertical range ${profileNumber(domain[0])} to ${profileNumber(domain[1])} meters. ` : "No retained values on this profile. "}Horizontal distance is {profileNumber(distance)} projected meters from the first retained source sample center. Points are not interpolated. Use the sample slider or Previous and Next controls to read numeric values in the shared probe.</desc>
      {[top,(top+bottom)/2,bottom].map((line,index) => <line key={index} x1={left} x2={right} y1={line} y2={line} className={styles.profileGrid} />)}
      {domain && includeZero && domain[0] !== domain[1] && <line x1={left} x2={right} y1={y(0)} y2={y(0)} className={styles.profileZero} />}
      <line x1={x(profile.samples[selectedIndex].distance_m)} x2={x(profile.samples[selectedIndex].distance_m)} y1={top-3} y2={bottom+3} className={styles.profileCursor} />
      {series.map(item => <g key={item.key} data-series={item.key}>{profile.samples.map((sample,index) => sample[item.key] === null ? null : <g key={index} data-sample-index={index}><svg x={x(sample.distance_m)} y={y(sample[item.key] as number)} width={1} height={1} overflow="visible"><ProfileMark shape={item.shape} x={0} y={0} color={item.color} size={index === selectedIndex ? 4.5 : 2.7} /></svg></g>)}</g>)}
    </svg>{!domain && <p className={styles.profileEmptyText}>No retained values on this profile</p>}<div className={styles.profileDistance} aria-hidden="true"><span>0 m</span><span>{profileNumber(distance)} m</span></div></div></div><p className={styles.profileAxisLabel}>Projected distance from first retained sample center (m)</p>
  </figure>;
}
function SampleProfile({ preview, selected, select, id }: { preview: NeonLidarPreview; selected: { row: number; column: number } | null; select: (selection: { row: number; column: number }) => void; id: string }) {
  const [axis,setAxis] = useState<NeonLidarProfileAxis>("row");
  const profile = useMemo(() => selected ? neonLidarProfile(preview,axis,axis === "row" ? selected.row : selected.column) : null, [preview,axis,selected]);
  const selectedIndex = selected ? axis === "row" ? selected.column : selected.row : 0;
  function selectIndex(index: number) {
    if (!profile || !Number.isInteger(index) || index < 0 || index >= profile.samples.length) return;
    const sample = profile.samples[index]; select({row:sample.row,column:sample.column});
  }
  const negative = profile?.samples.filter(sample => sample.differenceIssue === "negative").length ?? 0;
  const nonfinite = profile?.samples.filter(sample => sample.differenceIssue === "nonfinite").length ?? 0;
  return <section className={styles.profile} aria-labelledby={`${id}-heading`}>
    <div className={styles.profileHeading}><div><p className={styles.eyebrow}>LINKED SAMPLE PROFILE</p><h3 id={`${id}-heading`}>Follow a line through the tile</h3></div><div className={styles.profileAxis} role="group" aria-label="Profile direction"><button type="button" aria-pressed={axis === "row"} onClick={() => setAxis("row")}>Across row <span>W → E</span></button><button type="button" aria-pressed={axis === "column"} onClick={() => setAxis("column")}>Down column <span>N → S</span></button></div></div>
    {!profile ? <p className={styles.profilePrompt}>Choose a valid row and column above to compare retained samples along that line. Clearing either coordinate removes the profile.</p> : <>
      <div className={styles.profileSelection}><p><strong>{axis === "row" ? "Row" : "Column"} {profile.fixedIndex+1}</strong><span>Selected: row {selected!.row+1}, column {selected!.column+1} · {profileNumber(profile.samples[selectedIndex].distance_m)} m from first center</span></p><span className={styles.profileSampleCount}>{profile.samples.length} retained positions</span></div>
      <div className={styles.profileNavigator}><button type="button" onClick={() => selectIndex(selectedIndex-1)} disabled={selectedIndex === 0} aria-label="Previous profile sample">← Previous</button><label htmlFor={`${id}-sample`}>Shared sample · {selectedIndex+1} of {profile.samples.length}<input id={`${id}-sample`} type="range" min={1} max={profile.samples.length} step={1} value={selectedIndex+1} aria-valuetext={`Row ${selected!.row+1}, column ${selected!.column+1}, ${profileNumber(profile.samples[selectedIndex].distance_m)} projected meters from first sample center`} onChange={event => selectIndex(Number(event.target.value)-1)} /></label><button type="button" onClick={() => selectIndex(selectedIndex+1)} disabled={selectedIndex === profile.samples.length-1} aria-label="Next profile sample">Next →</button></div>
      <div className={styles.profilePlots}><ProfilePlot profile={profile} selectedIndex={selectedIndex} select={selectIndex} title="Elevation · ground and surface" series={ELEVATION_SERIES} includeZero={false} id={`${id}-elevation`} /><ProfilePlot profile={profile} selectedIndex={selectedIndex} select={selectIndex} title="Height · canopy and source difference" series={HEIGHT_SERIES} includeZero id={`${id}-height`} /></div>
      {(negative > 0 || nonfinite > 0) && <p className={styles.warning}>QA retained: {negative} negative DSM − DTM {negative === 1 ? "difference" : "differences"}; {nonfinite} {nonfinite === 1 ? "difference exceeds" : "differences exceed"} numeric limits. Negative values are plotted; nonfinite differences remain missing.</p>}
      <p className={styles.profileLimits}>Discrete nearest source samples; no interpolation or inferred values between them. Missing values leave gaps; zero remains valid. Elevation and height use separate scales. DSM − DTM includes structures and is distinct from provider CHM. Preview sampling omits detail; source accuracy remains unverified.</p>
    </>}
  </section>;
}

export function useNeonLidarPreview() {
  const [preview, setPreview] = useState<NeonLidarPreview | null>(null);
  const [pilotReceipt, setPilotReceipt] = useState<NeonPilotReceipt | null>(null);
  const [mode, setMode] = useState<NeonLidarMode>("chm");
  const [coordinateDraft, setCoordinateDraft] = useState({ row: "", column: "" });
  const [notice, setNotice] = useState(INITIAL_NOTICE);
  const [reading, setReading] = useState(false);
  const [failed, setFailed] = useState(false);
  const [session] = useState(createAcquisitionSession);
  useEffect(() => () => session.cancel(), [session]);
  async function importFile(file: File | undefined) {
    if (!file) return;
    const request = session.begin();
    setPreview(null); setPilotReceipt(null); setCoordinateDraft({ row: "", column: "" }); setReading(true); setFailed(false);
    setNotice("Reading the selected local preview…");
    try {
      const parsed = parseNeonLidarPreview(await readNeonLidarLocalJson(file, request.signal));
      if (!parsed) throw new Error("Preview validation failed. Choose a kfm-neon-lidar-preview-v1 file from the local preparer; all three grids must share one tile and reference system.");
      if (request.current()) { setPreview(parsed); setNotice("Local preview loaded. Nothing has been uploaded, saved, admitted or released."); }
    } catch (error: unknown) {
      if (request.current()) { setFailed(true); setNotice(error instanceof Error ? error.message : "The local preview could not be read."); }
    } finally { if (request.current()) setReading(false); }
  }
  async function loadPilot() {
    const request = session.begin();
    setPreview(null); setPilotReceipt(null); setCoordinateDraft({ row: "", column: "" }); setReading(true); setFailed(false); setNotice("Loading the dev-processed Konza Prairie preview…");
    try {
      const receipt = await readNeonLidarPilot(request.signal);
      if (request.current()) { setPreview(receipt.preview); setPilotReceipt(receipt); setNotice("Dev-processed provider preview loaded. Scientific review remains pending; nothing has been admitted or released."); }
    } catch (error: unknown) { if (request.current()) { setFailed(true); setNotice(error instanceof Error ? error.message : "The Konza Prairie preview is unavailable. Import a prepared file or try again later."); } }
    finally { if (request.current()) setReading(false); }
  }
  function clear() {
    session.cancel(); setPreview(null); setPilotReceipt(null); setCoordinateDraft({ row: "", column: "" }); setReading(false); setFailed(false); setNotice(INITIAL_NOTICE);
  }
  function selectAxis(axis: "row" | "column", input: string) {
    if (!preview) return;
    setCoordinateDraft(previous => {
      if (previous[axis] === input) return previous;
      const next = { ...previous, [axis]: input };
      // A first valid axis starts at the other axis's first cell; later edits stay independent.
      if (!previous.row && !previous.column && coordinateIndex(input, preview.grid.width) !== null) next[axis === "row" ? "column" : "row"] = "1";
      return next;
    });
  }
  return { preview, pilotReceipt, mode, setMode, coordinateDraft, setCoordinateDraft, notice, reading, failed, importFile, loadPilot, clear, selectAxis };
}
export type NeonLidarPreviewController = ReturnType<typeof useNeonLidarPreview>;

/** One controller owns the exact preview shared by raster and scientific analysis. */
export function NeonLidarWorkspace({ controller, embedded = false, anchorId }: { controller: NeonLidarPreviewController; embedded?: boolean; anchorId?: string }) {
  const id = useId();
  const { preview, pilotReceipt, mode, setMode, coordinateDraft, setCoordinateDraft, notice, reading, failed, importFile, loadPilot, clear, selectAxis } = controller;
  const domain = useMemo(() => preview ? neonElevationDomain(preview) : null, [preview]);
  const selected = useMemo(() => {
    if (!preview) return null;
    const row = coordinateIndex(coordinateDraft.row, preview.grid.height), column = coordinateIndex(coordinateDraft.column, preview.grid.width);
    return row === null || column === null ? null : { row, column };
  }, [preview, coordinateDraft]);
  const probe = preview && selected ? neonLidarProbe(preview, selected.row, selected.column) : null;
  const samples = preview?.grid[mode];
  const covered = samples?.filter(value => value !== null).length ?? 0;
  const saturated = mode === "chm" ? samples?.filter(value => value !== null && value > 30).length ?? 0 : 0;
  return <section id={anchorId} className={`${styles.panel} ${embedded ? styles.embedded : ""}`} aria-labelledby={`${id}-heading`}>
    <div className={styles.heading}>
      <div><p className={styles.eyebrow}>NEON / TERRAIN + VEGETATION</p><h2 id={`${id}-heading`}>Read the same ground</h2></div>
      <span className={styles.badge}>{pilotReceipt ? "Provider preview · review pending" : "Local preview · not admitted"}</span>
    </div>
    <p className={styles.intro}>Compare ground, surface and provider canopy height on one 1 km tile. Free, no subscription.</p>
    <div className={styles.loadActions}><button type="button" className={styles.pilotButton} disabled={reading} onClick={() => void loadPilot()}>Load Konza Prairie pilot</button>
      <button type="button" onClick={clear} disabled={!preview && !reading && !failed}>{reading ? "Cancel local read" : "Clear preview"}</button>
      {!embedded && <a href="/labs/terrain">Analyze in the Science lab →</a>}
    </div>
    <details className={styles.localImport}><summary>Import your own prepared preview</summary><div className={styles.importControls}>
      <label htmlFor={`${id}-file`}>Prepared preview JSON <span>2 MiB maximum · stays in this tab; not uploaded</span><input id={`${id}-file`} type="file" accept="application/json,.json" onChange={event => { void importFile(event.target.files?.[0]); event.target.value = ""; }} /></label>
    </div></details>
    <p className={failed ? styles.error : styles.notice} role="status" aria-live="polite" aria-busy={reading}>{notice}</p>
    {!preview ? <div className={styles.empty}>
      <span className={styles.emptyMark} aria-hidden="true">01 / 02 / 03</span><h3>Three surfaces. One numeric probe.</h3>
      <p>Load the Konza Prairie pilot, or import a prepared NEON preview JSON from your data workstation with matching ground, surface and canopy samples. The viewer starts with no sample terrain.</p>
      <p>Use a Kansas NEON tile from Konza Prairie (KONZ), the Konza agricultural site (KONA), or the University of Kansas Field Station (UKFS). These site tiles do not cover all of Kansas.</p>
    </div> : <>
      {pilotReceipt && <div className={styles.pilotReview}><p><strong>Provider preview · processed on the data workstation.</strong> Scientific review pending; independent accuracy and vertical reference are unverified.</p><p className={pilotReceipt.cache.state === "stale" ? styles.warning : styles.precision}>Cache {pilotReceipt.cache.state} · <time dateTime={pilotReceipt.cache.at}>{pilotReceipt.cache.at}</time>{pilotReceipt.cache.state === "stale" ? ". This cached preview is stale; it is not a new observation." : ". Acquisition dates remain separate from cache time."}</p><p className={styles.warning}>Native CHM maximum {pilotReceipt.review.canopy_native_max_m.toFixed(2)} m; {pilotReceipt.review.canopy_native_cells_above_50m} native cells above 50 m. Outliers retained for review, not identified as trees.</p></div>}
      {preview.data_kind === "synthetic-test" && <p className={styles.synthetic}><strong>Synthetic test grid · not observed terrain.</strong> These analytic values demonstrate the viewer and do not describe this NEON site.</p>}
      <div className={styles.identity}><strong>{preview.source.site}</strong><span>Catalog month {preview.source.month}</span><span>Recorded run {preview.source.acquisition_run}</span><span>{preview.source.release}</span><code>{preview.source.tile}</code></div>
      <div className={styles.modeControls} role="group" aria-label="Raster surface">
        {MODES.map(item => <button key={item.kind} type="button" aria-pressed={mode === item.kind} onClick={() => setMode(item.kind)}><span>{item.short}</span>{item.label}</button>)}
      </div>
      <div className={styles.lab}>
        <figure className={styles.figure}>
          <div className={styles.northBounds}><span>{coordinate(preview.grid.bounds[0])} E</span><span>{coordinate(preview.grid.bounds[3])} N</span></div>
          <GridCanvas preview={preview} mode={mode} selected={selected} hover={!embedded} select={selection => setCoordinateDraft(previous => { const row = String(selection.row + 1), column = String(selection.column + 1); return previous.row === row && previous.column === column ? previous : { row, column }; })} descriptionId={`${id}-canvas-description`} />
          <div className={styles.southBounds}><span>{coordinate(preview.grid.bounds[1])} N</span><span>{coordinate(preview.grid.bounds[2])} E</span></div>
          <figcaption id={`${id}-canvas-description`}>North up · native projected meters. Each block is one nearest source sample; no interpolation. {embedded ? "Click or tap" : "Hover or tap"} to probe, or use row and column.</figcaption>
          <div className={styles.legend} aria-label={mode === "chm" ? "Fixed canopy legend, 0 to 30 meters" : "Shared ground and surface elevation legend"}>
            <div className={styles.legendBar} />
            <div className={styles.legendLabels}><span>{mode === "chm" ? "0 m" : domain ? meters(domain[0]) : "No elevation samples"}</span><span>{mode === "chm" ? "30 m" : domain ? meters(domain[1]) : ""}</span></div>
            <p>{mode === "chm" ? "Fixed canopy scale. Values above 30 m use the upper color and an orange corner." : "Shared DTM / DSM scale, held constant when switching elevation surfaces."}</p>
          </div>
          <p className={styles.coverage}>{covered.toLocaleString("en-US")} / {preview.grid.width ** 2} samples present · {preview.grid.preview_resolution_m.toLocaleString("en-US", { maximumFractionDigits: 3 })} m preview of 1 m source{mode === "chm" && saturated > 0 ? ` · ${saturated} above 30 m` : ""}</p>
          <p className={styles.noData}><span aria-hidden="true" />Hatching = NoData. Zero is a valid value.</p>
        </figure>
        <aside className={styles.probe} aria-labelledby={`${id}-probe-heading`}>
          <p className={styles.eyebrow}>SHARED SAMPLE / METERS</p><h3 id={`${id}-probe-heading`}>Read the same place</h3>
          <div className={styles.probeControls}>
            <label htmlFor={`${id}-row`}>Row · north to south<input id={`${id}-row`} type="number" min={1} max={preview.grid.height} step={1} placeholder={`1–${preview.grid.height}`} value={coordinateDraft.row} onChange={event => selectAxis("row", event.target.value)} /></label>
            <label htmlFor={`${id}-column`}>Column · west to east<input id={`${id}-column`} type="number" min={1} max={preview.grid.width} step={1} placeholder={`1–${preview.grid.width}`} value={coordinateDraft.column} onChange={event => selectAxis("column", event.target.value)} /></label>
          </div>
          {!probe ? <p className={styles.probePrompt}>Select a cell to read all three original samples and their source position.</p> : <>
            <p className={styles.position}>Nearest 1 m source sample<br /><strong>{coordinate(probe.easting)} E / {coordinate(probe.northing)} N</strong></p>
            <dl className={styles.values}>
              <div><dt>DTM · ground elevation</dt><dd>{meters(probe.dtm)}</dd></div>
              <div><dt>DSM · surface elevation</dt><dd>{meters(probe.dsm)}</dd></div>
              <div><dt>Provider CHM · canopy height</dt><dd>{meters(probe.chm)}</dd></div>
              <div className={styles.difference}><dt>DSM − DTM · surface above ground</dt><dd>{meters(probe.surfaceAboveGround)}</dd></div>
            </dl>
            <p>DSM − DTM includes structures; it is a separate source difference, not the provider CHM.</p>
            {probe.differenceIssue === "negative" && <p className={styles.warning}>Negative source difference: retain for QA; it has not been clamped to zero.</p>}
            {probe.differenceIssue === "nonfinite" && <p className={styles.warning}>Source difference exceeds numeric limits and needs QA.</p>}
            {probe.chm === 0 && <p className={styles.warning}>Zero CHM does not establish bare earth. Heights below the sensor-dependent floor may be suppressed.</p>}
          </>}
          <p className={styles.precision}>Two decimals express display precision, not measurement accuracy. Sampling omits detail between preview cells.</p>
        </aside>
      </div>
      <SampleProfile preview={preview} selected={selected} select={selection => setCoordinateDraft({ row: String(selection.row+1), column: String(selection.column+1) })} id={`${id}-profile`} />
      <details className={styles.provenance}>
        <summary>Provenance, reference systems &amp; scientific limits</summary>
        <dl className={styles.metadata}>
          <div><dt>Prepared</dt><dd><time dateTime={preview.generated_at}>{preview.generated_at}</time></dd></div>
          <div><dt>Attribution</dt><dd>{preview.source.attribution}</dd></div>
          <div><dt>Recorded acquisition run</dt><dd>{preview.source.acquisition_run}</dd></div>
          <div><dt>Vertical reference</dt><dd>{preview.source.vertical_reference}<br />{preview.source.vertical_reference_basis}</dd></div>
          <div><dt>Recorded canopy floor</dt><dd>{preview.source.canopy_floor_m === null ? "Unknown" : `${preview.source.canopy_floor_m} m`}. {preview.source.canopy_floor_basis}</dd></div>
        </dl>
        <p>Nearest-neighbor display retains individual source samples. NoData is missing coverage, and zero canopy can include suppressed low vegetation. Canopy height alone does not identify species, biomass, carbon, grass growth, tree counts or change.</p>
        <p>The catalog month is not an exact flight date. Site, catalog month, acquisition run and release are recorded during preparation; local hashes do not independently authenticate the run or release.</p>
        <p>Original file SHA-256 values below are recorded by the local preparer. This browser has not verified those GeoTIFFs, provider checksums, survey accuracy or metadata claims.</p>
        <p>NEON data use <a href="https://www.neonscience.org/usage-policies" target="_blank" rel="noreferrer">CC BY 4.0 and NEON attribution policies ↗</a>. Direct provider downloads require <a href="https://www.neonscience.org/about/user-accounts" target="_blank" rel="noreferrer">free NEON sign-in or an API token ↗</a>; this local viewer requires no account.</p>
        {pilotReceipt && <><p>Native maximum DSM − DTM: {pilotReceipt.review.surface_minus_ground_native_max_m.toFixed(2)} m, distinct from provider CHM.</p><ul>{pilotReceipt.review.notes.map((note, index) => <li key={index}>{note}</li>)}</ul></>}
        <ul className={styles.files}>{preview.source.files.map(file => <li key={file.kind}><strong>{file.kind.toUpperCase()} · {file.product}</strong><code>{file.name}</code><span>{file.bytes.toLocaleString("en-US")} bytes</span><code>SHA-256 {file.sha256}</code></li>)}</ul>
        <div className={styles.sourceLinks}><a href="https://data.neonscience.org/data-products/DP3.30024.001" target="_blank" rel="noreferrer">NEON elevation products ↗</a><a href="https://data.neonscience.org/data-products/DP3.30015.001" target="_blank" rel="noreferrer">NEON canopy height ↗</a></div><h4>Recorded native horizontal CRS</h4><pre>{preview.source.horizontal_crs}</pre>
      </details>
    </>}
  </section>;
}

export function NeonLidarPanel() {
  const controller = useNeonLidarPreview();
  return <NeonLidarWorkspace controller={controller} anchorId="neon-lidar-lab" />;
}

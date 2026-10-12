"use client";
import { useCallback, useEffect, useLayoutEffect, useMemo, useRef, useState } from "react";
import type { Map as AtlasMap } from "./maplibre-seam";
import { atlasMobilePadding } from "./local-atlas-presentation";
import { PREPARED_COLLECTIONS } from "./prepared-collection-pins";
import { inspectPreparedCollection, preparedTable, preparedText, type PreparedSelection } from "./prepared-collections";
import { buildLocalImportPreview } from "./import-preview";
import { parseAtlasPreview, type AtlasPreview } from "./local-atlas-client";
import { attachAtlasPreview, atlasScale, ATLAS_COLORS } from "./local-atlas-map";

// Presentation and actions only; verified file buffers remain owned by this control.
export type PreparedCompactReview = {
  title: string; detail: string; range: string | null; status: string; selected: string | null;
  hasPreview: boolean; visible: boolean; canFit: boolean; busy: boolean; error: string;
  fit(): void; toggle(): void; inspect(): void; clearMap(): void; cancel(): void;
};
type Props = { compact: boolean; onViewMap(): void; onExpand(): void; onCompactReview(review: PreparedCompactReview | null): void; map: AtlasMap | null; styleReady: boolean; flatMap: boolean; suspended: boolean; reducedMotion: boolean; onFlatMap(): void; onPrivateView(): void };
const number = (n: number) => n.toLocaleString();
const cell = (value: unknown) => value === null || value === undefined ? "Missing / not supplied" : typeof value === "object" ? JSON.stringify(value).slice(0, 2000) : String(value).slice(0, 2000);
const label = (name: string) => name.replace(/^geojson\//, "").replace(/\.geojson$/, "").replace("temperature_f", "Temperature · °F").replace("precipitation_in", "Precipitation · inches");
const bounds = { west: -104.8, south: 34.8, east: -92, north: 42.2 };

export function PreparedCollectionControl({ map, styleReady, flatMap, suspended, compact, onViewMap, onExpand, onCompactReview, reducedMotion, onFlatMap, onPrivateView }: Props) {
  const [id, setId] = useState<string>("normals"), [selection, setSelection] = useState<PreparedSelection | null>(null);
  const [busy, setBusy] = useState(false), [error, setError] = useState(""), [member, setMember] = useState("");
  const [preview, setPreview] = useState<AtlasPreview | null>(null), [visible, setVisible] = useState(true), [mapState, setMapState] = useState("");
  const [inspected, setInspected] = useState<Record<string, unknown> | null>(null), [filter, setFilter] = useState(""), [offset, setOffset] = useState(0);
  const [mode, setMode] = useState<"map" | "table" | "notes">("map");
  const request = useRef<AbortController | null>(null), generation = useRef(0);
  const overlay = useRef<ReturnType<typeof attachAtlasPreview> | null>(null);
  const controlRef = useRef<HTMLElement>(null);
  const currentView = useRef({ preview, suspended });
  useLayoutEffect(() => { currentView.current = { preview, suspended }; }, [preview, suspended]);
  const profile = PREPARED_COLLECTIONS.find(p => p.id === id)!;
  const clear = useCallback(() => { generation.current++; request.current?.abort(); request.current = null; overlay.current?.dispose(); overlay.current = null; setSelection(null); setPreview(null); setInspected(null); setBusy(false); setMapState(""); setMember(""); setError(""); setFilter(""); setOffset(0); }, []);
  useEffect(() => () => { generation.current++; request.current?.abort(); overlay.current?.dispose(); }, []);
  // External view suspension retires pending verification and loaded device bytes together.
  // eslint-disable-next-line react-hooks/set-state-in-effect
  useEffect(() => { if (suspended) clear(); }, [suspended, clear]);
  useEffect(() => {
    if (!map || !styleReady || !preview || !visible || suspended) return;
    const display = attachAtlasPreview(map, preview, { field: preview.valueField, density: false, difference: false, opacity: .75, flatMap }, setInspected, setMapState);
    overlay.current = display;
    return () => { display.dispose(); if (overlay.current === display) overlay.current = null; };
  }, [map, styleReady, preview, visible, suspended, flatMap]);
  const choose = async (files: FileList | null) => {
    if (!files?.length) return;
    clear(); const sequence = generation.current; const controller = new AbortController(); request.current = controller; setBusy(true);
    try {
      const result = await inspectPreparedCollection(id, Array.from(files), controller.signal);
      if (controller.signal.aborted || sequence !== generation.current) return;
      setSelection(result); setVisible(true);
      const next = profile.mapFiles.length ? profile.mapFiles[0] : profile.tableFiles[0] ?? "README.md";
      setMember(next); setMode(profile.mapFiles.length ? "map" : profile.tableFiles.length ? "table" : "notes");
    } catch (e) { if (!controller.signal.aborted && sequence === generation.current) setError(e instanceof Error ? e.message : "Preparation held."); }
    finally { if (sequence === generation.current) setBusy(false); }
  };
  const show = () => {
    if (!selection || suspended) return;
    setPreview(null); setInspected(null); setError(""); setMapState("");
    try {
      const raw = selection.files.get(member)!;
      const imported = buildLocalImportPreview({ fileName: member.split("/").at(-1)!, fileSizeBytes: raw.byteLength, text: preparedText(selection, member), inspectedAt: new Date().toISOString(), supportedBounds: bounds });
      if (!imported.renderAllowed || imported.invalidFeatureCount || imported.authority !== "UNADMITTED_BROWSER_PREVIEW" || imported.publicEffect !== "NONE") throw new Error("This view cannot be rendered within the review boundary.");
      const units = id === "normals" ? member.includes("temperature_f") ? "°F" : "inches" : id === "discharge" ? "ft³/s" : null;
      const field = id === "normals" ? "value" : id === "discharge" ? "last_captured_value" : null;
      const source = profile.members.find(m => m.file === member)!;
      const result = parseAtlasPreview({ schema: "kfm-local-atlas-preview/v1", id: `prepared-${id}-${source.sha256}`, kind: "vector", title: `${profile.title} · ${label(member)}`, data: imported.featureCollection,
        source: { role: "Verified device-selected preparation · private review only", attribution: imported.attribution, sourceUrl: profile.sources[0], sha256: source.sha256 },
        time: { kind: "frozen-review", label: profile.period, start: null, end: null, processedAt: null }, units, bounds: imported.bounds,
        limitations: [profile.limitation, "Pending independent review and source admission. Unreleased; no report, evidence, saved-workspace, AI or public effect."],
        displayedCount: imported.featureCount, totalCount: imported.featureCount, truncated: false, authority: { admission: false, evidence: false, release: false }, numericFields: field ? [field] : [], valueField: field });
      if (!result) throw new Error("Unsupported bounded geometry. Data held.");
      onPrivateView(); setPreview(result); setVisible(true);
    } catch (e) { setError(e instanceof Error ? e.message : "Map view held."); }
  };
  const fit = useCallback(() => {
    if (!map || !preview?.bounds || suspended) return;
    const b = preview.bounds, sequence = generation.current;
    onPrivateView();
    if (compact) onViewMap();
    // Collapse first, then measure the exposed map after React and layout settle.
    window.requestAnimationFrame(() => window.requestAnimationFrame(() => {
      if (!controlRef.current?.isConnected || sequence !== generation.current || currentView.current.preview !== preview || currentView.current.suspended) return;
      const rect = map.getCanvas().getBoundingClientRect();
      const sheet = controlRef.current.closest(".map-utility-panel")?.getBoundingClientRect();
      map.fitBounds([[b[0], b[1]], [b[2], b[3]]], { padding: compact ? atlasMobilePadding(rect.top, rect.bottom, sheet?.top ?? rect.bottom) : { top: 70, left: 60, right: 440, bottom: 90 }, maxZoom: 12, duration: reducedMotion ? 0 : 500 });
    }));
  }, [map, preview, suspended, compact, onPrivateView, onViewMap, reducedMotion]);
  const table = useMemo(() => {
    if (!selection || mode !== "table" || !profile.tableFiles.some(f => f === member)) return null;
    try { return { value: preparedTable(preparedText(selection, member)), error: "" }; } catch (e) { return { value: null, error: e instanceof Error ? e.message : "Table held." }; }
  }, [selection, mode, member, profile]);
  const matches = useMemo(() => table?.value?.rows.filter(r => !filter || r.some(c => c.toLowerCase().includes(filter.toLowerCase()))) ?? [], [table, filter]);
  const scale = useMemo(() => preview ? atlasScale(preview, preview.valueField) : null, [preview]);
  const features = preview?.kind === "vector" ? (preview.data as GeoJSON.FeatureCollection).features : [];
  const changeMember = useCallback((name: string) => { generation.current++; overlay.current?.dispose(); overlay.current = null; setPreview(null); setInspected(null); setMapState(""); setError(""); setMember(name); setFilter(""); setOffset(0); }, []);
  const clearMap = useCallback(() => changeMember(member), [changeMember, member]);
  const toggle = useCallback(() => setVisible(v => !v), []);
  const inspect = useCallback(() => {
    const sequence = generation.current;
    onExpand();
    window.requestAnimationFrame(() => window.requestAnimationFrame(() => {
      if (sequence !== generation.current || !controlRef.current?.isConnected || currentView.current.suspended) return;
      const select = controlRef.current.querySelector<HTMLSelectElement>(".prepared-review-inspector");
      select?.scrollIntoView({ block: "nearest", behavior: "instant" });
      select?.focus({ preventScroll: true });
    }));
  }, [onExpand]);
  const status = !visible ? "Preview hidden" : !styleReady ? "Waiting for map" : mapState === "visible" ? "Private review visible on map" : mapState === "unavailable" ? "Map preview unavailable; data held from display" : "Preparing review map…";
  useEffect(() => {
    onCompactReview({ title: preview?.title ?? profile.title,
      detail: preview ? `${preview.displayedCount.toLocaleString()} features · ${preview.units ?? "statistical boundaries"} · ${preview.time.label}` : busy ? "Verifying the complete preparation on this device…" : selection ? `${profile.fileCount} files verified · ${mode === "table" ? "table" : mode === "notes" ? "review notes" : "choose a map view"}` : "Show controls to choose a prepared folder",
      range: scale ? `${scale.min.toLocaleString()}–${scale.max.toLocaleString()} ${preview?.units ?? ""} · selected frame range` : null,
      status, selected: inspected ? cell(inspected.name ?? inspected.station_id ?? inspected.GEOID ?? "Selected prepared feature") : null,
      hasPreview: Boolean(preview), visible, canFit: Boolean(map && preview?.bounds && !suspended), busy, error,
      fit, toggle, inspect, clearMap, cancel: clear });
  }, [onCompactReview, preview, profile, busy, selection, mode, scale, status, inspected, visible, map, suspended, error, fit, toggle, inspect, clearMap, clear]);
  useEffect(() => () => onCompactReview(null), [onCompactReview]);
  return <section ref={controlRef} className="prepared-review" aria-label="Prepared collection review">
    <header><span>PREPARED · DEVICE REVIEW</span><h3>Explore a prepared collection</h3><p>Verified files stay on this device. Review maps and tables without admitting or releasing data.</p></header>
    <label>Prepared collection<select value={id} onChange={e => { clear(); setId(e.target.value); }} disabled={busy}>{PREPARED_COLLECTIONS.map(p => <option key={p.id} value={p.id}>{p.title}</option>)}</select></label>
    <article className="prepared-review-card"><strong>{profile.title}</strong><p>{profile.period}</p><small>{profile.limitation}</small><p className="prepared-review-state">Independent review pending · not admitted · unreleased</p></article>
    <label>Open prepared folder<input ref={node => node?.setAttribute("webkitdirectory", "")} type="file" multiple disabled={busy || suspended} onChange={e => { void choose(e.target.files); e.target.value = ""; }} /></label>
    <details><summary>Folder and verification details</summary><p>Choose {profile.folder} from the protected WORK store. Expected: {profile.fileCount} files, {(profile.totalBytes / 1e6).toFixed(2)} MB. Every declared member must match before a view opens.</p><code>{profile.manifestSha256}</code><p>File verification makes no network request or cloud upload. The existing basemap can still request tiles. No original overwrite, provider activation or store relocation.</p></details>
    <p role="status">{busy ? "Verifying the complete preparation on this device…" : selection ? `${profile.fileCount} files verified · exact preparation identity` : "No prepared files selected."}</p>
    {busy && <button type="button" onClick={clear}>Cancel verification</button>}
    {error && <p role="alert">{error}</p>}
    {selection && <>
      <nav aria-label="Prepared review formats">{(["map", "table", "notes"] as const).filter(m => m === "notes" || (m === "map" ? profile.mapFiles.length : profile.tableFiles.length)).map(m => <button type="button" key={m} aria-pressed={mode === m} onClick={() => { changeMember(m === "map" ? profile.mapFiles[0]! : m === "table" ? profile.tableFiles[0]! : "README.md"); setMode(m); }}>{m === "map" ? "Map" : m === "table" ? "Table" : "Review notes"}</button>)}</nav>
      {mode === "map" && <><label>Prepared map view<select value={member} onChange={e => changeMember(e.target.value)}>{profile.mapFiles.map(f => <option key={f} value={f}>{label(f)}</option>)}</select></label><button type="button" disabled={suspended || busy} onClick={show}>Show verified view</button>
        {preview && <article aria-label="Prepared map inspection"><strong>{number(preview.displayedCount)} verified features · {preview.units ?? "statistical boundary overview"}</strong><p>{preview.time.label}</p><p role="status">{status}</p>
          {scale && <div className="prepared-review-scale"><i style={{ background: `linear-gradient(90deg, ${ATLAS_COLORS.low}, ${ATLAS_COLORS.mid}, ${ATLAS_COLORS.high})` }} /><span>{scale.min.toLocaleString()}–{scale.max.toLocaleString()} {preview.units} · selected frame range</span></div>}
          <div className="local-atlas-actions"><button type="button" onClick={toggle}>{visible ? "Hide review" : "Show review"}</button><button type="button" onClick={fit}>Fit review</button><button type="button" onClick={clearMap}>Clear map</button></div>
          {!flatMap && <button type="button" onClick={onFlatMap}>Use flat map for inspection</button>}
          <label>Inspect prepared feature<select className="prepared-review-inspector" value="" onChange={e => { const f = features[Number(e.target.value)]; if (e.target.value && f) setInspected(f.properties ?? {}); }}><option value="">Choose a feature · first {Math.min(features.length, 200)}</option>{features.slice(0, 200).map((f, i) => <option key={i} value={i}>{cell(f.properties?.name ?? f.properties?.station_id ?? f.properties?.GEOID ?? `Feature ${i + 1}`)}</option>)}</select></label>
          {inspected && <dl>{Object.entries(inspected).slice(0, 60).map(([k, v]) => <div key={k}><dt>{k}</dt><dd>{cell(v)}</dd></div>)}</dl>}
          <p>{preview.source.attribution}</p><small>Temporary review overlay · never a released layer or claim.</small></article>}
      </>}
      {mode === "table" && <><label>Prepared table<select value={member} onChange={e => changeMember(e.target.value)}>{profile.tableFiles.map(f => <option key={f} value={f}>{f.split("/").at(-1)}</option>)}</select></label>{table?.error && <p role="alert">{table.error}</p>}{table?.value && <><label>Filter prepared rows<input type="search" value={filter} maxLength={100} onChange={e => { setFilter(e.target.value); setOffset(0); }} placeholder="Station, year, element, or flag" /></label><p>{number(matches.length)} of {number(table.value.rows.length)} rows match · missing markers are preserved</p><div className="prepared-review-table" tabIndex={0} role="region" aria-label="Verified prepared table"><table><thead><tr>{table.value.headers.map(h => <th scope="col" key={h}>{h}</th>)}</tr></thead><tbody>{matches.slice(offset, offset + 40).map((r, i) => <tr key={offset + i}>{r.map((c, j) => <td key={j}>{c || "—"}</td>)}</tr>)}</tbody></table></div><div className="local-atlas-actions"><button type="button" disabled={!offset} onClick={() => setOffset(v => Math.max(0, v - 40))}>Previous rows</button><button type="button" disabled={offset + 40 >= matches.length} onClick={() => setOffset(v => v + 40)}>Next rows</button></div><small>Rows {matches.length ? offset + 1 : 0}–{Math.min(offset + 40, matches.length)}. Empty cells stay empty; no interpolation or zero filling.</small></>}</>}
      {mode === "notes" && <><label>Verified review document<select value={member} onChange={e => changeMember(e.target.value)}>{profile.members.filter(m => !m.file.endsWith(".csv") && !m.file.endsWith(".geojson")).map(m => <option key={m.file} value={m.file}>{m.file}</option>)}</select></label><pre>{preparedText(selection, member).slice(0, 64000)}</pre><small>Read-only verified text. References and local paths in documents are never fetched automatically.</small></>}
      <button type="button" onClick={clear}>Remove collection from review</button>
    </>}
    <details><summary>Publisher references</summary>{profile.sources.map(s => <p key={s}><a href={s} target="_blank" rel="noreferrer">Official source ↗</a></p>)}</details>
    <details className="prepared-review-holds"><summary>Collections still held</summary><p>KDOT map reuse needs inspectable permission scope and capture locators. Your public-use confirmation is recorded; it does not supply missing source-specific documentation.</p><p>PRISM needs exact access dates and file/version-specific units. NWM geometry/gauge routing remains held. Earth Engine projection metadata does not establish current export entitlement.</p><p>These holds do not change when a preview is opened. No held map/model payload is loaded here.</p></details>
    <footer>Review on this device only. Nothing enters the Layer Catalog, Evidence Drawer, AI context, saved workspaces, reports, exports or release state. Closing this view removes the overlay; original files remain intact.</footer>
  </section>;
}

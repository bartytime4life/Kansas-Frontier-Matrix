"use client";
import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import type { Map as AtlasMap } from "./maplibre-seam";
import { INTAKE_DESK_ORIGIN } from "./intake-desk-client";
import { AtlasRequestGate, atlasErrorMessage, atlasRequest, atlasSession, parseAtlasCatalog, parseAtlasCoverage, parseAtlasFrames, parseAtlasGroups, parseAtlasPreview,
  type AtlasCatalog, type AtlasCoverage, type AtlasFrames, type AtlasGroup, type AtlasItem, type AtlasPreview, type AtlasRaster } from "./local-atlas-client";
import { atlasCollectionLabel, atlasInspectorLabel, atlasMobilePadding } from "./local-atlas-presentation";
import { ATLAS_COLORS, atlasPointsOnly, atlasScale, attachAtlasPreview } from "./local-atlas-map";

type Props = { map: AtlasMap | null; styleReady: boolean; flatMap: boolean; suspended: boolean; compact: boolean; collapsed: boolean; onViewMap: () => void; onExpand: () => void; reducedMotion: boolean; onFlatMap: () => void; onArchive: () => void };
const number = (n: number) => n.toLocaleString(undefined, { maximumFractionDigits: 3 });
const textValue = (v: unknown): string => v === null || v === undefined ? "No value" : typeof v === "number" ? number(v) : typeof v === "object" ? JSON.stringify(v).slice(0, 400) : String(v).slice(0, 400);
const featureName = (p: GeoJSON.GeoJsonProperties, i: number) => String(p?.name ?? p?.NAME ?? p?.county_name ?? p?.title ?? p?.id ?? `Feature ${i + 1}`);
const bytes = (n: number) => n >= 1e9 ? `${(n / 1e9).toFixed(1)} GB` : n >= 1e6 ? `${(n / 1e6).toFixed(1)} MB` : `${Math.ceil(n / 1000)} KB`;

export function LocalAtlasControl({ map, styleReady, flatMap, suspended, compact, collapsed, onViewMap, onExpand, reducedMotion, onFlatMap, onArchive }: Props) {
  const [section, setSection] = useState<"climate" | "files" | "coverage">("climate");
  const [connection, setConnection] = useState<"connecting" | "connected" | "offline">("connecting");
  const [connectionKey, setConnectionKey] = useState(0), [token, setToken] = useState("");
  const [groups, setGroups] = useState<AtlasGroup[]>([]), [groupId, setGroupId] = useState("");
  const [year, setYear] = useState(""), [frameOffset, setFrameOffset] = useState(0), [frames, setFrames] = useState<AtlasFrames | null>(null);
  const [frameId, setFrameId] = useState(""), [compareId, setCompareId] = useState(""), [comparing, setComparing] = useState(false);
  const [representation, setRepresentation] = useState<"counties" | "raster">("counties"), [playing, setPlaying] = useState(false);
  const [query, setQuery] = useState(""), [draftQuery, setDraftQuery] = useState(""), [family, setFamily] = useState("");
  const [offset, setOffset] = useState(0), [catalog, setCatalog] = useState<AtlasCatalog | null>(null), [coverage, setCoverage] = useState<AtlasCoverage | null>(null);
  const [item, setItem] = useState<AtlasItem | null>(null), [band, setBand] = useState(1);
  const [preview, setPreview] = useState<AtlasPreview | null>(null), [previewDifference, setPreviewDifference] = useState(false);
  const [busy, setBusy] = useState(false), [listingBusy, setListingBusy] = useState(false), [error, setError] = useState("");
  const [field, setField] = useState<string | null>(null), [density, setDensity] = useState(false), [opacity, setOpacity] = useState(.8);
  const [mapState, setMapState] = useState(""), [inspected, setInspected] = useState<Record<string, unknown> | null>(null), [inspectQuery, setInspectQuery] = useState("");
  const controlRef = useRef<HTMLElement>(null);
  const gate = useRef(new AtlasRequestGate());
  const overlay = useRef<ReturnType<typeof attachAtlasPreview> | null>(null);
  const clear = useCallback(() => { gate.current.clear(); overlay.current?.dispose(); overlay.current = null; setPreview(null); setInspected(null); setBusy(false); setPlaying(false); setMapState(""); }, []);
  useEffect(() => () => { gate.current.clear(); overlay.current?.dispose(); }, []);
  useEffect(() => {
    const abort = new AbortController(); setConnection("connecting"); setToken(""); setFrames(null); setFrameId(""); setError("");
    atlasRequest("/api/status", abort.signal, atlasSession).then(async session => {
      if (abort.signal.aborted) return;
      setToken(session); setConnection("connected");
      try {
        const available = await atlasRequest("/api/atlas/prism/groups", abort.signal, parseAtlasGroups);
        if (abort.signal.aborted) return;
        setGroups(available); setGroupId(current => available.some(g => g.id === current) ? current : available[0]?.id ?? "");
      } catch (e) { if (!abort.signal.aborted) setError(atlasErrorMessage(e)); }
    }).catch(e => { if (!abort.signal.aborted) { setConnection("offline"); setError(atlasErrorMessage(e)); } });
    return () => abort.abort();
  }, [connectionKey]);
  useEffect(() => {
    setFrames(null); setFrameId(""); setCompareId(""); setListingBusy(false);
    if (!token || !groupId || section !== "climate" || (year.length > 0 && year.length !== 4)) return;
    const abort = new AbortController(); setListingBusy(true); setError("");
    const params = new URLSearchParams({ group: groupId, offset: String(frameOffset), limit: "366", ...(year ? { year } : {}) });
    atlasRequest(`/api/atlas/prism/frames?${params}`, abort.signal, parseAtlasFrames).then(result => { if (!abort.signal.aborted) { setFrames(result); setFrameId(result.frames[0]?.id ?? ""); setCompareId(result.frames[1]?.id ?? ""); } })
      .catch(e => { if (!abort.signal.aborted) setError(atlasErrorMessage(e)); }).finally(() => { if (!abort.signal.aborted) setListingBusy(false); });
    return () => abort.abort();
  }, [token, groupId, year, frameOffset, section]);
  useEffect(() => {
    if (!token || section === "climate") return;
    const abort = new AbortController(); setListingBusy(true); setCatalog(null); setCoverage(null); setError("");
    const params = new URLSearchParams({ text: query, family, offset: String(offset), limit: section === "coverage" ? "100" : "50" });
    const request = section === "coverage" ? atlasRequest(`/api/extents?${params}`, abort.signal, parseAtlasCoverage).then(v => { if (!abort.signal.aborted) setCoverage(v); })
      : atlasRequest(`/api/atlas/catalog?${params}`, abort.signal, parseAtlasCatalog).then(v => { if (!abort.signal.aborted) setCatalog(v); });
    request.catch(e => { if (!abort.signal.aborted) setError(atlasErrorMessage(e)); }).finally(() => { if (!abort.signal.aborted) setListingBusy(false); });
    return () => abort.abort();
  }, [token, section, query, family, offset]);
  const loadPreview = useCallback(async (request: { kind: "prism" | "file"; id: string; compareId?: string; representation?: "counties" | "raster"; band?: number }) => {
    const ownership = gate.current.begin(); overlay.current?.dispose(); overlay.current = null; setPreview(null); setInspected(null); setMapState(""); setError(""); setBusy(true);
    try {
      const data = await atlasRequest("/api/atlas/preview", ownership.signal, parseAtlasPreview, request, token);
      if (!ownership.current()) return;
      setField(data.valueField); setDensity(false); setPreviewDifference(Boolean(request.compareId)); setPreview(data);
    } catch (e) { if (ownership.current()) { setError(atlasErrorMessage(e)); setPlaying(false); } }
    finally { if (ownership.current()) setBusy(false); }
  }, [token]);
  useEffect(() => { if (suspended) clear(); }, [suspended, clear]);
  useEffect(() => {
    if (!preview || !map || !styleReady || suspended) return;
    const control = attachAtlasPreview(map, preview, { field, density, difference: previewDifference && field === preview.valueField, opacity, flatMap }, setInspected, setMapState);
    overlay.current = control;
    return () => { control.dispose(); if (overlay.current === control) overlay.current = null; };
  }, [map, preview, styleReady, suspended, field, density, previewDifference, opacity, flatMap]);
  const frameIndex = frames?.frames.findIndex(f => f.id === frameId) ?? -1;
  const showFrame = useCallback((id = frameId) => { if (id && !suspended && (!year || year.length === 4)) void loadPreview({ kind: "prism", id, representation, ...(comparing && compareId ? { compareId } : {}) }); }, [frameId, suspended, loadPreview, representation, comparing, compareId, year]);
  useEffect(() => {
    if (!playing || busy || !preview || !frames || section !== "climate" || suspended) return;
    // A new timer starts only after the accepted response. Never accumulate requests.
    const next = frameIndex - 1;
    if (next < 0) { setPlaying(false); return; }
    const timer = window.setTimeout(() => { const id = frames.frames[next].id; setFrameId(id); showFrame(id); }, 1800);
    return () => window.clearTimeout(timer);
  }, [playing, busy, preview, frames, frameIndex, section, suspended, showFrame]);
  const scale = useMemo(() => preview ? atlasScale(preview, field, previewDifference && field === preview.valueField) : null, [preview, field, previewDifference]);
  const raster = preview?.kind === "raster" ? preview.data as AtlasRaster : null;
  const fit = () => {
    if (!map || !preview?.bounds) return;
    const b = preview.bounds;
    if (compact) onViewMap();
    // Wait for the collapsed bar to lay out before measuring the exposed map.
    window.requestAnimationFrame(() => window.requestAnimationFrame(() => {
      if (!controlRef.current?.isConnected) return;
      const rect = map.getCanvas().getBoundingClientRect();
      const sheet = controlRef.current.closest(".map-utility-panel")?.getBoundingClientRect();
      map.fitBounds([[b[0], b[1]], [b[2], b[3]]], { padding: compact ? atlasMobilePadding(rect.top, rect.bottom, sheet?.top ?? rect.bottom) : { top: 80, left: 50, right: 420, bottom: 100 }, duration: reducedMotion ? 0 : 650, maxZoom: 14 });
    }));
  };
  const features = preview?.kind === "vector" ? (preview.data as GeoJSON.FeatureCollection).features : [];
  const inspectMatches = features.map((f, i) => ({ f, i, name: featureName(f.properties, i) })).filter(v => v.name.toLowerCase().includes(inspectQuery.toLowerCase()));
  const changeSection = (next: typeof section) => { clear(); setError(""); setItem(null); setOffset(0); setSection(next); };
  const selectFrame = (id: string) => { clear(); setFrameId(id); };
  const previewCoverage = () => {
    if (!coverage || suspended) return;
    clear(); setPreviewDifference(false); setField(null); setDensity(false); setError("");
    setPreview({ schema: "kfm-local-atlas-preview/v1", id: `coverage-${offset}`, kind: "vector", title: "Local file bounds", data: coverage,
      source: { role: "Indexed file extents · not measured coverage", attribution: "Local Intake Desk", sourceUrl: null, sha256: null },
      time: { kind: "catalog", label: "File metadata · source dates vary", start: null, end: null, processedAt: null }, units: null,
      bounds: (() => { const points = coverage.features.flatMap(f => f.geometry?.type === "Polygon" ? f.geometry.coordinates.flat() : []); return points.length ? [Math.min(...points.map(p => p[0])), Math.min(...points.map(p => p[1])), Math.max(...points.map(p => p[0])), Math.max(...points.map(p => p[1]))] : null; })(), limitations: [coverage.note, "An extent is a file boundary. It does not establish observations, complete geographic coverage, or source approval."],
      displayedCount: coverage.displayedCount, totalCount: coverage.total, truncated: coverage.nextOffset !== null || coverage.offset > 0,
      authority: { admission: false, evidence: false, release: false }, numericFields: [], valueField: null });
  };
  const selectedGroup = groups.find(g => g.id === groupId);
  const climatePreview = preview?.source.role === "gridded climate estimate";
  const expandInspector = () => {
    onExpand();
    window.requestAnimationFrame(() => window.requestAnimationFrame(() => {
      const details = controlRef.current?.querySelector<HTMLDetailsElement>(".local-atlas-inspector");
      if (details) { details.open = true; details.scrollIntoView({ block: "nearest", behavior: "instant" }); details.querySelector<HTMLElement>("summary")?.focus({ preventScroll: true }); }
    }));
  };
  return <section ref={controlRef} className="local-atlas map-utility-section" data-collapsed={collapsed || undefined} aria-label="Local Atlas">
    {collapsed && <div className="local-atlas-peek" aria-label="Local preview on map">
      <div className="local-atlas-peek-title"><strong>{preview?.title ?? (busy ? "Preparing local preview…" : "Local Atlas · map view")}</strong><span>{preview ? `${preview.units || "Units not supplied"} · ${preview.time.label}` : "Show controls to choose local data"}</span></div>
      {preview && <>
        <div className="local-atlas-peek-range">{raster?.paletteType === "categorical" ? "Source class palette · legend in controls" : density ? "Relative point density" : scale ? `${number(scale.min)} to ${number(scale.max)} ${preview.units ?? ""}${previewDifference ? " · B − A" : ""}` : "Uniform features · no numerical scale"}</div>
        {inspected && <div className="local-atlas-peek-selection" role="status"><strong>{featureName(inspected, 0)}</strong><span>{field ? `${atlasInspectorLabel(field, climatePreview, previewDifference)}: ${textValue(inspected[field])} ${preview.units ?? ""}` : "Selected local feature"}</span><button type="button" onClick={expandInspector}>Inspect details</button></div>}
        {!inspected && <small>{preview.kind === "raster" ? "Sampled overview · no point-value lookup" : "Tap a feature on the map to inspect"}</small>}
        {mapState === "flat-map-required" && <button type="button" onClick={onFlatMap}>Switch to flat map to view raster</button>}
        {mapState === "unavailable" && <p role="status">Preview could not render. Clear it and choose another view.</p>}
        <div className="local-atlas-peek-actions"><button type="button" disabled={!preview.bounds || !map} onClick={fit}>Fit</button><button type="button" onClick={onExpand}>Legend &amp; opacity</button><button type="button" onClick={clear}>Clear</button></div>
      </>}
      {busy && <button type="button" onClick={clear}>Cancel preparation</button>}
      {error && <p role="alert">{error}</p>}
    </div>}
    <div id="local-atlas-controls" className="local-atlas-body" hidden={collapsed} inert={collapsed}>
    <div className="local-atlas-connection" data-state={connection}><span className="local-atlas-dot" aria-hidden="true" /><div><strong>Data on this PC</strong><small>{connection === "connected" ? "Intake Desk connected · originals stay local" : connection === "connecting" ? "Connecting to the local Intake Desk…" : "Local Intake Desk unavailable"}</small></div><button type="button" disabled={connection === "connecting"} onClick={() => { clear(); setItem(null); setCatalog(null); setCoverage(null); setGroups([]); setGroupId(""); setConnectionKey(v => v + 1); }}>{connection === "connected" ? "Refresh catalog" : connection === "connecting" ? "Connecting…" : "Reconnect"}</button></div>
    {connection === "offline" && <div className="local-atlas-message"><p>Start the Intake Desk on this computer, then reconnect. Your local files are not uploaded to the Site.</p><a href={INTAKE_DESK_ORIGIN} target="_blank" rel="noreferrer">Open Intake Desk ↗</a></div>}
    <nav className="local-atlas-sections" aria-label="Local Atlas views">{(["climate", "files", "coverage"] as const).map(id => <button key={id} type="button" aria-pressed={section === id} onClick={() => changeSection(id)}>{id === "climate" ? "Climate" : id === "files" ? "Local files" : "Coverage"}</button>)}</nav>
    {suspended && <p className="local-atlas-message" role="status">Finish measuring or close Underground to show a local map preview.</p>}
    {section === "climate" && <>
      <div className="local-atlas-intro"><span>PRISM · COUNTY / GRID</span><h3>See a climate period</h3><p>Explore county means or the source raster. Compare matching periods with B minus A.</p></div>
      <label>Climate collection<select value={groupId} disabled={!groups.length} onChange={e => { clear(); setGroupId(e.target.value); setFrameOffset(0); setComparing(false); }}><option value="" disabled>{connection === "connected" && !groups.length ? "No processed PRISM frames" : "Choose a collection"}</option>{groups.map(g => <option key={g.id} value={g.id}>{atlasCollectionLabel(g)} · {g.series}</option>)}</select></label>
      {selectedGroup && <div className="local-atlas-collection-summary"><strong>{atlasCollectionLabel(selectedGroup)}</strong><span>{selectedGroup.units} · {number(selectedGroup.frameCount)} available periods</span><small>Source series / version: {selectedGroup.series}</small></div>}
      <div className="local-atlas-row"><label>Year filter<input inputMode="numeric" placeholder="All years" aria-label="Filter climate frames by four digit year" maxLength={4} value={year} onChange={e => { const value = e.target.value.replace(/\D/g, ""); clear(); setFrames(null); setFrameId(""); setCompareId(""); setYear(value); setFrameOffset(0); }} /></label><label>Presentation<select value={representation} onChange={e => { clear(); setRepresentation(e.target.value as typeof representation); setComparing(false); }}><option value="counties">County means</option><option value="raster">Source raster</option></select></label></div>
      {groups.find(g => g.id === groupId)?.series.toLowerCase().includes("normal") && <p className="local-atlas-note">1991–2020 normal calendar · these are long-term normals, not weather observed in 2020.</p>}
      {year && year.length !== 4 && <p className="local-atlas-note">Enter all four digits to filter a year.</p>}
      <label>{comparing ? "Period B" : "Source period"}<select value={frameId} disabled={!frames?.frames.length} onChange={e => selectFrame(e.target.value)}><option value="" disabled>{listingBusy ? "Reading available frames…" : "Choose an available frame"}</option>{frames?.frames.map(f => <option key={f.id} value={f.id}>{f.label}</option>)}</select></label>
      {frames && <div className="local-atlas-pager"><span>{number(frames.total)} available · {frames.offset + (frames.frames.length ? 1 : 0)}–{frames.offset + frames.frames.length}</span><button type="button" disabled={!frameOffset || listingBusy} onClick={() => { clear(); setFrameOffset(Math.max(0, frameOffset - 366)); }}>Newer page</button><button type="button" disabled={frameOffset + frames.frames.length >= frames.total || listingBusy} onClick={() => { clear(); setFrameOffset(frameOffset + 366); }}>Older page</button></div>}
      <label className="local-atlas-checkbox"><input type="checkbox" checked={comparing} disabled={representation !== "counties" || !frames?.frames.length} onChange={e => { clear(); setComparing(e.target.checked); }} />Compare two periods · B − A</label>
      {comparing && <label>Period A · reference<select value={compareId} onChange={e => { clear(); setCompareId(e.target.value); }}><option value="" disabled>Choose reference period</option>{frames?.frames.map(f => <option key={f.id} value={f.id}>{f.label}</option>)}</select></label>}
      <div className="local-atlas-actions"><button className="local-atlas-primary" type="button" disabled={!token || !frameId || (comparing && !compareId) || busy || suspended || year.length > 0 && year.length !== 4} onClick={() => showFrame()}>{busy ? "Preparing map…" : comparing ? "Map difference" : "Show on map"}</button><button type="button" disabled={!frames || frameIndex < 0 || frameIndex >= frames.frames.length - 1 || busy || suspended} onClick={() => { setPlaying(false); const id = frames!.frames[frameIndex + 1].id; setFrameId(id); showFrame(id); }}>← Older</button><button type="button" disabled={frameIndex <= 0 || busy || suspended} onClick={() => { setPlaying(false); const id = frames!.frames[frameIndex - 1].id; setFrameId(id); showFrame(id); }}>Newer →</button></div>
      <button type="button" className="local-atlas-play" aria-pressed={playing} disabled={(!playing && (frameIndex <= 0 || !preview || busy)) || suspended || year.length > 0 && year.length !== 4} onClick={() => setPlaying(v => !v)}>{playing ? "Pause playback" : "Play toward newer frames"}</button>
      <p className="local-atlas-note">County values are gridded cell-center means. Daily periods end at 12:00 UTC. Local source time is independent of the main map timeline.</p>
    </>}
    {section !== "climate" && <>
      <div className="local-atlas-intro"><span>{section === "coverage" ? "CATALOG · SPATIAL INDEX" : "FILES · SPATIAL PREVIEWS"}</span><h3>{section === "coverage" ? "Where files have bounds" : "Bring a local file onto the map"}</h3><p>{section === "coverage" ? "File bounds, not measured coverage. Only the current page is drawn." : "Preview supported geometry, coordinate tables, or raster bands. Every indexed format remains searchable."}</p></div>
      <form className="local-atlas-search" onSubmit={e => { e.preventDefault(); clear(); setQuery(draftQuery.trim()); setOffset(0); setItem(null); }}><label><span className="sr-only">Search local data files</span><input type="search" value={draftQuery} maxLength={180} placeholder="Find a file, county, or source…" onChange={e => setDraftQuery(e.target.value)} /></label><button type="submit">Search</button></form>
      <label>File family<select value={family} onChange={e => { clear(); setFamily(e.target.value); setOffset(0); setItem(null); }}><option value="">All formats</option>{["vector", "table", "raster", "archive", "array", "document", "image", "unknown"].map(f => <option key={f}>{f}</option>)}</select></label>
      {section === "files" && catalog && <><div className="local-atlas-pager"><span>{number(catalog.total)} matches · {offset + (catalog.items.length ? 1 : 0)}–{offset + catalog.items.length}</span><button type="button" disabled={!offset} onClick={() => { clear(); setOffset(Math.max(0, offset - 50)); setItem(null); }}>Previous</button><button type="button" disabled={offset + catalog.items.length >= catalog.total} onClick={() => { clear(); setOffset(offset + 50); setItem(null); }}>Next</button></div>
        <div className="local-atlas-file-list" aria-label="Matching local files">{catalog.items.map(f => <button type="button" key={f.id} aria-pressed={item?.id === f.id} onClick={() => { clear(); setItem(f); setBand(1); setError(""); }}><strong>{f.name}</strong><small>{f.family} · {bytes(f.size_bytes)} · {f.preview === "unsupported" ? "Catalog only" : `${f.preview} preview`}</small></button>)}{!catalog.items.length && <p>No files match this search.</p>}</div></>}
      {section === "files" && item && <article className="local-atlas-file-detail"><strong>{item.name}</strong><p>{item.reason ?? (item.preview === "raster" ? "A bounded raster view is prepared from this file on your PC." : "A bounded geometry preview is prepared from this file on your PC.")}</p><small>Review state: {item.status} · {item.domain}</small>{item.preview === "raster" && <label>Raster band<input type="number" min={1} max={256} value={band} onChange={e => { clear(); setBand(Math.max(1, Math.min(256, Number(e.target.value) || 1))); }} /></label>}
        <button className="local-atlas-primary" type="button" disabled={!token || item.preview === "unsupported" || busy || suspended} onClick={() => void loadPreview({ kind: "file", id: item.id, band })}>{busy ? "Preparing map…" : "Show file on map"}</button>
        {item.family === "document" && <button type="button" onClick={onArchive}>Open historical map tools</button>}</article>}
      {section === "coverage" && coverage && <><div className="local-atlas-coverage-count"><strong>{number(coverage.displayedCount)}</strong><span>file bounds on this page<br />{number(coverage.total)} matching files · {number(coverage.scannedCount)} scanned</span></div><p className="local-atlas-note">{coverage.note}</p><div className="local-atlas-actions"><button className="local-atlas-primary" type="button" disabled={!token || !coverage.displayedCount || suspended} onClick={previewCoverage}>Show this page’s bounds</button><button type="button" disabled={!offset} onClick={() => { clear(); setOffset(0); }}>First page</button><button type="button" disabled={coverage.nextOffset === null} onClick={() => { clear(); setOffset(coverage.nextOffset!); }}>Next page</button></div></>}
      <button type="button" className="local-atlas-archive" onClick={onArchive}>Historical maps &amp; prepared GeoPDF overlays →</button>
    </>}
    {listingBusy && <p className="local-atlas-message" role="status">Reading the local catalog…</p>}
    {busy && <div className="local-atlas-loading" role="status"><span aria-hidden="true" />Preparing a bounded map view…<button type="button" onClick={clear}>Cancel</button></div>}
    {error && <p className="local-atlas-error" role="alert">{error}</p>}
    {preview && <article className="local-atlas-preview" aria-label="Selected map preview"><header><span>{previewDifference ? "DIFFERENCE · B − A" : "LOCAL MAP PREVIEW"}</span><h3>{preview.title}</h3><p>{preview.time.label}</p></header>
      <div className="local-atlas-source-line"><strong>{preview.units || "Units not supplied"}</strong><small>{preview.kind === "vector" ? `${number(preview.displayedCount)} features` : `${(preview.data as AtlasRaster).width} × ${(preview.data as AtlasRaster).height} pixels`}{preview.truncated ? " · bounded preview" : ""}</small></div>
      {preview.kind === "vector" && preview.numericFields.length > 0 && <label>Color by<select value={field ?? ""} onChange={e => { setField(e.target.value || null); setDensity(false); }}><option value="">Uniform color</option>{preview.numericFields.map(f => <option key={f} value={f}>{f}</option>)}</select></label>}
      {atlasPointsOnly(preview) && <label className="local-atlas-checkbox"><input type="checkbox" checked={density} onChange={e => setDensity(e.target.checked)} />Point density · relative concentration</label>}
      {raster?.paletteType === "categorical" ? <div className="local-atlas-classes"><strong>Source class codes</strong><p>Original palette · nearest-neighbor overview</p>{raster.colorMap?.map(c => <span key={c.value}><i style={{ background: c.color }} />{c.value}</span>)}</div> : density ? <p className="local-atlas-note">Relative point density at this zoom. Each point has equal weight; this is not a measured quantity.</p> : scale ? <div className="local-atlas-legend" aria-label={`Color scale ${number(scale.min)} to ${number(scale.max)} ${preview.units ?? ""}`}><div style={{ background: scale.min === scale.max ? ATLAS_COLORS.mid : `linear-gradient(90deg, ${(raster?.colors ?? [ATLAS_COLORS.low, ATLAS_COLORS.mid, ATLAS_COLORS.high]).join(", ")})` }} /><span>{number(scale.min)}{previewDifference ? " · decrease" : ""}</span><span>{number(scale.max)}{previewDifference ? " · increase" : ""}</span><small><i style={{ background: ATLAS_COLORS.missing }} />{raster ? "Transparent = no data · sampled range" : "Gray = missing value"}{previewDifference ? " · zero at center" : ""}</small></div> : <p className="local-atlas-note">Uniform features · no numerical scale.</p>}
      <label className="local-atlas-opacity">Opacity <output>{Math.round(opacity * 100)}%</output><input type="range" min={0} max={100} value={Math.round(opacity * 100)} onChange={e => setOpacity(Number(e.target.value) / 100)} /></label>
      <div className="local-atlas-actions"><button type="button" disabled={!preview.bounds || !map} onClick={fit}>{compact ? "Fit & view map" : "Fit preview"}</button><button type="button" onClick={clear}>Clear preview</button></div>
      <p className="local-atlas-map-state" role="status">{!styleReady ? "Waiting for the map style…" : mapState === "visible" ? preview.kind === "raster" ? "Raster visible · sampled range only; no point value lookup" : "Visible on map · click a feature to inspect" : mapState === "flat-map-required" ? "Raster preview needs the flat Mercator map." : mapState === "unavailable" ? "Map preview failed to render. Clear it and try again." : "Preparing the map overlay…"}</p>
      {mapState === "flat-map-required" && <button type="button" onClick={onFlatMap}>Switch to flat map</button>}
      {features.length > 0 && <details className="local-atlas-inspector" open={Boolean(inspected) || undefined}><summary>Inspect features{inspected ? " · selected" : " · map or keyboard"}</summary><label>Find a feature<input type="search" value={inspectQuery} onChange={e => setInspectQuery(e.target.value)} placeholder="County or feature name" /></label><select aria-label="Choose a preview feature to inspect" value="" onChange={e => { const f = features[Number(e.target.value)]; if (f) setInspected(f.properties ?? {}); }}><option value="">Choose a feature · {inspectMatches.length} matches</option>{inspectMatches.slice(0, 200).map(v => <option key={v.i} value={v.i}>{v.name}</option>)}</select>{inspectMatches.length > 200 && <small>First 200 matches shown. Refine the feature search.</small>}{inspected && <dl>{Object.entries(inspected).slice(0, 60).map(([key, value]) => <div key={key}><dt>{atlasInspectorLabel(key, climatePreview, previewDifference)}</dt><dd>{textValue(value)}</dd></div>)}</dl>}</details>}
      <details className="local-atlas-provenance"><summary>Source, dates &amp; limitations</summary><p>{preview.source.role}</p><p>{preview.source.attribution}</p>{preview.source.sourceUrl && /^https?:\/\//.test(preview.source.sourceUrl) && <a href={preview.source.sourceUrl} target="_blank" rel="noreferrer">Source reference ↗</a>}{preview.time.processedAt && <p>Processed: {preview.time.processedAt}</p>}{preview.source.sha256 && <p className="local-atlas-hash">SHA-256: {preview.source.sha256}</p>}<ul>{preview.limitations.map((limitation, i) => <li key={i}>{limitation}</li>)}</ul></details>
    </article>}
    <footer className="local-atlas-footer"><p>Exploratory display from this PC. Local previews are not admitted evidence or released layers. Closing Local Atlas clears the preview.</p><a href={INTAKE_DESK_ORIGIN} target="_blank" rel="noreferrer">Review data in Intake Desk ↗</a></footer>
    </div>
  </section>;
}

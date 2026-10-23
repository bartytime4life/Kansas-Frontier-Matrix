"use client";
import { lazy, Suspense, useEffect, useRef, useState } from "react";
import type { Map as MapLibreMap } from "./maplibre-seam";
import { inspectTransportStudy, transportDay, transportDetail, transportFrame, TRANSPORT_STUDY_MAX_BYTES, type TransportWork } from "./transport-history";
import { TRANSPORT_HISTORY_LEADS, TRANSPORT_HISTORY_DISCOVERY } from "./transport-history-sources";
const CrewPreview = lazy(() => import("./transport-crew-preview").then(m => ({ default: m.TransportCrewPreview })));
type Props = { map: MapLibreMap | null; mapReady: boolean; date: string | null; reducedMotion: boolean; animate: boolean };
export function TransportHistoryControl({ map, mapReady, date, reducedMotion, animate }: Props) {
  const [works, setWorks] = useState<readonly TransportWork[]>([]);
  const [shown, setShown] = useState(true), [preview, setPreview] = useState(false);
  const [localDate, setLocalDate] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null), [busy, setBusy] = useState(false);
  const [rendererState, setRendererState] = useState("No local route study loaded");
  const [lod, setLod] = useState("Overview lines · equipment resolves at closer scales");
  const input = useRef<HTMLInputElement>(null), generation = useRef(0);
  const view = useRef<ReturnType<typeof import("./transport-construction-layer").attachTransportConstruction> | null>(null);
  const day = localDate ?? date;
  const latest = useRef({ works, day });
  useEffect(() => { latest.current = { works, day }; }, [works, day]);
  const ready = shown && works.length > 0 && day !== null;
  useEffect(() => () => { generation.current++; }, []);
  useEffect(() => {
    if (!map || !mapReady || !ready) return;
    let disposed = false;
    void import("./transport-construction-layer").then(({ attachTransportConstruction }) => {
      if (disposed || !latest.current.day) return;
      try { view.current = attachTransportConstruction(map, latest.current.works, latest.current.day, animate && !reducedMotion); setRendererState("Browser-local overlay · source assertions unverified"); }
      catch { setRendererState("Construction renderer unavailable; study data retained"); }
    }).catch(() => { if (!disposed) setRendererState("Construction renderer unavailable; study data retained"); });
    return () => { disposed = true; view.current?.dispose(); view.current = null; };
    // Date and route changes update the installed layer without allocating a new renderer.
  }, [map, mapReady, ready, animate, reducedMotion]);
  useEffect(() => { if (day) view.current?.update(works, day); }, [works, day]);
  useEffect(() => {
    if (!map || !works.length) return;
    const update = () => {
      if (works.every(w => w.progressMode === "milestones")) return setLod("Milestones: corridor context only · crew location, width and progress unknown");
      if (map.getProjection().type === "globe") return setLod("Globe: route cues only · detailed crew held");
      if (map.getTerrain()) return setLod("Terrain: route cues only · historical ground elevation unresolved");
      const detail = transportDetail(map.getZoom(), works[0].coordinates[0][1], works[0].positionAccuracyM);
      setLod(detail === "overview" ? "Overview lines · crew requires closer zoom and ≤4 m positional uncertainty" : detail === "equipment" ? "Equipment at metre scale · workers remain below readable size" : "Equipment and workers at metre scale");
    }; update(); map.on("moveend", update); map.on("terrain", update); map.on("projectiontransition", update);
    return () => { map.off("moveend", update); map.off("terrain", update); map.off("projectiontransition", update); };
  }, [map, works]);
  async function inspect(file?: File) {
    if (!file) return;
    const request = ++generation.current; setBusy(true); setError(null);
    try {
      if (file.size > TRANSPORT_STUDY_MAX_BYTES) throw new Error("Choose a study smaller than 2 MB.");
      const result = inspectTransportStudy(await file.text());
      if (request !== generation.current) return;
      setPlaying(false); setWorks(result); setLocalDate(null); setShown(true); setRendererState("Preparing construction overlay…");
    } catch (e) { if (request === generation.current) setError(e instanceof Error ? e.message : "Could not read the construction study."); }
    finally { if (request === generation.current) { setBusy(false); if (input.current) input.current.value = ""; } }
  }
  const [playing, setPlaying] = useState(false);
  const firstDay = works.length ? Math.min(...works.map(w => transportDay(w.start)!)) : 0;
  const lastDay = works.length ? Math.max(...works.map(w => transportDay(w.end)!)) : 0;
  useEffect(() => {
    if (!playing || reducedMotion || !shown || !works.length) return;
    const timer = window.setInterval(() => {
      if (document.hidden) return;
      const at = transportDay(latest.current.day) ?? firstDay;
      const next = Math.min(lastDay, Math.max(firstDay, at) + Math.max(86_400_000, Math.ceil((lastDay - firstDay) / 180 / 86_400_000) * 86_400_000));
      if (next === lastDay) setPlaying(false);
      setLocalDate(new Date(next).toISOString().slice(0, 10));
    }, 120);
    return () => window.clearInterval(timer);
  }, [playing, reducedMotion, shown, works, firstDay, lastDay, date]);
  const clear = () => { generation.current++; setBusy(false); setPlaying(false); setWorks([]); setLocalDate(null); setError(null); setRendererState("No local route study loaded"); if (input.current) input.current.value = ""; };
  const fit = () => { if (!map || !works.length) return; const points = works.flatMap(w => [...w.coordinates]); map.fitBounds([[Math.min(...points.map(p => p[0])), Math.min(...points.map(p => p[1]))], [Math.max(...points.map(p => p[0])), Math.max(...points.map(p => p[1]))]], { padding: 70, maxZoom: 18, duration: reducedMotion ? 0 : 600 }); };
  return <details className="transport-history-control">
    <summary><strong>Construction through time</strong><span>Road + rail · dates, progress and closures</span></summary>
    <div className="transport-history-body">
      <p>See an advancing work front where dated route progress is available. Crew size follows the map’s physical scale; distant views use route cues.</p>
      <div className="transport-history-actions"><button type="button" aria-expanded={preview} onClick={() => setPreview(v => !v)}>{preview ? "Close equipment study" : "View 3D equipment study"}</button></div>
      {preview && <Suspense fallback={<p>Preparing equipment study…</p>}><CrewPreview reducedMotion={reducedMotion} /></Suspense>}
      <details><summary>Historical source notes · {TRANSPORT_HISTORY_LEADS.length} leads</summary><div className="transport-history-sources">
        {TRANSPORT_HISTORY_LEADS.map(source => <article key={source.id}><span>{source.mode.toUpperCase()} · {source.date}</span><h4>{source.title}</h4><p>{source.fact}</p><small>{source.missing}</small><a href={source.url} target="_blank" rel="noreferrer">Read primary source ↗</a></article>)}
        <p>These notes do not supply qualified route geometry or construction rates. No map animation is inferred from them.</p>
        {TRANSPORT_HISTORY_DISCOVERY.map(source => <p key={source.url}><a href={source.url} target="_blank" rel="noreferrer">{source.title} ↗</a> · {source.purpose}</p>)}
      </div></details>
      <label className="transport-study-input">Local construction-study JSON<input ref={input} type="file" accept=".json,application/json" disabled={busy} onChange={event => void inspect(event.target.files?.[0])} /></label>
      <p className="transport-history-note">Browser memory only · 2 MB · 12 routes · no upload. Advancing fronts require actual dates, physical width, positional uncertainty and dated chainage. Milestone studies keep unsupported progress unknown. Imported assertions remain unverified. <a href="/transport-construction-study-example.json" download>Download synthetic format example</a>.</p>
      {error && <p role="alert" className="transport-study-error">{error}</p>}
      {!!works.length && <>
        <div className="transport-history-actions"><button type="button" aria-pressed={shown} onClick={() => setShown(v => !v)}>{shown ? "Hide study" : "Show study"}</button><button type="button" onClick={fit} disabled={!mapReady}>Fit routes</button><button type="button" onClick={clear}>Clear study</button></div>
        <label className="transport-study-scrub">Traverse study dates<input type="range" min={firstDay} max={lastDay} step={86_400_000} value={Math.max(firstDay, Math.min(lastDay, transportDay(day) ?? firstDay))} onChange={event => { setPlaying(false); setLocalDate(new Date(Number(event.target.value)).toISOString().slice(0, 10)); }} /></label>
        <div className="transport-history-actions"><button type="button" disabled={reducedMotion || !shown} onClick={() => { if (!playing && (transportDay(day) ?? lastDay) >= lastDay) setLocalDate(new Date(firstDay).toISOString().slice(0, 10)); setPlaying(v => !v); }}>{playing ? "Pause traversal" : "Play work history"}</button><small>{reducedMotion ? "Reduced motion: use the date or slider" : "Playback compresses calendar time; it is not equipment travel speed"}</small></div>
        <label className="transport-study-date">Study date<input type="date" value={day ?? ""} onChange={event => { if (transportDay(event.target.value) !== null) { setPlaying(false); setLocalDate(event.target.value); } }} /></label>
        <div className="transport-history-actions"><button type="button" disabled={!localDate} onClick={() => setLocalDate(null)}>Follow map time</button><small>{localDate ? "Local day overrides map time for this study" : date ? "Following map time · year-only frames use January 1" : "Map time is outside supported calendar dates · choose a study day"}</small></div>
        <p role="status">{shown ? !mapReady ? "Map renderer unavailable · date study remains readable" : rendererState : "Construction study hidden"} · {works.every(w => w.progressMode === "milestones") ? "Milestones: corridor context only · crew location, width and progress unknown" : lod}</p>
        <div className="transport-study-legend"><span>Gold: pending</span><span>Slate: built</span><span>Red: recorded closure</span><span>Faded brown: removed</span><span>Blue-grey: context; progress unknown</span><span>Purple tint: interpolated progress</span></div>
        {works.map(work => { const frame = day ? transportFrame(work, day) : null; return <article key={work.id} className="transport-study-record"><h4>{work.synthetic ? "SYNTHETIC · " : ""}{work.title}</h4><p>{work.progressMode === "milestones" ? "Milestone study · front, closure status and completion fraction unknown" : frame ? `${frame.state} · ${frame.closed ? "recorded closure" : "closure not established"} · ${(frame.chainageM / 1000).toFixed(2)} km` : "Select a supported date"}</p>
          <p>{work.progressMode === "milestones" ? "Dates identify source reports. No intermediate activity, direction or rate is reconstructed" : frame?.basis === "interpolated" ? "Illustrative interpolation between supplied observations" : frame?.sourceDate ? `Last supplied chainage observation: ${frame.sourceDate}` : "No observation at this date"}. {work.progressMode !== "milestones" && (work.interpolate ? "Interpolation was requested in this local file." : "Progress holds between supplied observations.")}</p>
          {frame?.rateMPerDay !== null && frame?.rateMPerDay !== undefined && <small>Interval average: {frame.rateMPerDay.toFixed(1)} m/day · not a daily measured speed</small>}
          {work.progressMode === "milestones" && <ul>{(work.milestones ?? []).filter(m => day && transportDay(m.date)! <= transportDay(day)!).map(m => <li key={m.date}><time>{m.date}</time> · {m.kind} · {m.title} <a href={m.sourceUrl} target="_blank" rel="noreferrer">Source report ↗</a></li>)}</ul>}
          <p>{work.limitation}</p>{work.action === "remove" && <small>Removal uses route cues; equipment-specific removal staging is unresolved.</small>}<small>{work.progressMode === "milestones" ? "Corridor context; physical width, historical survey accuracy and construction direction unestablished" : <>±{work.positionAccuracyM} m positional uncertainty · {work.widthM} m supplied corridor width</>}</small><p><a href={work.sourceUrl} target="_blank" rel="noreferrer">Date source ↗</a> · <a href={work.geometrySourceUrl} target="_blank" rel="noreferrer">Geometry source ↗</a></p>
        </article>; })}
        <p className="transport-history-note">Local overlays do not reconstruct the basemap or establish navigability. Models are representative; tight curves, narrow corridors, uncertain positions, terrain and globe views retain line cues. Removal needs an explicit removal record; map absence never proves closure.</p>
      </>}
    </div>
  </details>;
}

"use client";
import { useCallback, useEffect, useRef, useState, type RefObject } from "react";
import type { Map as MapLibreMap } from "./maplibre-seam";
import { readBoundedJson } from "./bounded-json";
import { approvalRemainingMs } from "./governed-water";
import type { SoilResponse } from "./governed-soil";
import { waterBrowserLabel, waterBrowserStateForResponse, type WaterBrowserState } from "./governed-water-availability";
import { latestSoilDay, SOIL_DEPTHS, soilEvidenceMatchesSelection, soilExportMatchesSelection, soilValueText } from "./governed-soil-availability";

const SOURCE = "kfm-reviewed-soil", LAYER = "kfm-reviewed-soil-points", ROUTE = "/api/governed/soil/v1";
const reasonText: Record<string, string> = { NO_APPROVED_SNAPSHOT: "No reviewed soil snapshot is active.", RELEASE_STORE_UNAVAILABLE: "Reviewed soil storage is unavailable.", REVIEW_REQUIRED: "This soil package is waiting for review.", RIGHTS_OR_SENSITIVITY_HOLD: "Rights or sensitivity review is still required.", CORRECTION_HOLD: "This snapshot has been corrected or withdrawn.", RELEASE_TIME_INVALID: "The release approval has expired or is not yet valid." };
const freshnessText: Record<string, string> = { RECENT: "Reporting soil moisture", STALE: "Soil moisture not reported recently", EMPTY: "No soil moisture in the window" };
export function GovernedSoilControl({ mapRef, styleReady, onSelectionChange }: { mapRef: RefObject<MapLibreMap | null>; styleReady: boolean; onSelectionChange?: (selected: boolean) => void }) {
  const [response, setResponse] = useState<SoilResponse | null>(null), [status, setStatus] = useState("Not checked"), [loading, setLoading] = useState(false);
  const [clock, setClock] = useState(Date.now);
  const [browserState, setBrowserState] = useState<WaterBrowserState>("not-checked");
  const [visible, setVisible] = useState(false), [selected, setSelected] = useState("53974"), [render, setRender] = useState("Hidden");
  const [evidenceRecord, setEvidenceRecord] = useState<{ stationId: string; packageId: unknown; value: SoilResponse } | null>(null);
  const [exportStatus, setExportStatus] = useState("");
  const controller = useRef<AbortController | null>(null);
  const selectedRef = useRef(selected);
  const selectionGeneration = useRef(0);
  const chooseStation = useCallback((id: string) => {
    if (selectedRef.current !== id) selectionGeneration.current += 1;
    selectedRef.current = id; setSelected(id); setExportStatus("");
  }, []);
  const refresh = useCallback(async () => {
    controller.current?.abort(); const abort = new AbortController(); controller.current = abort; setLoading(true); setResponse(null); setEvidenceRecord(null); setStatus("Checking current release…"); setBrowserState("checking"); setRender("Waiting for map frame");
    const timeout = setTimeout(() => abort.abort(), 15000);
    try {
      const fetched = await fetch(`${ROUTE}/layers`, { signal: abort.signal, cache: "no-store", credentials: "same-origin" });
      const value = await readBoundedJson(fetched, 2 * 1024 * 1024) as SoilResponse;
      if (abort.signal.aborted) return;
      const next = waterBrowserStateForResponse(value, fetched.ok);
      setBrowserState(next);
      if (next !== "received") { setResponse(null); setEvidenceRecord(null); setStatus(reasonText[value?.envelope?.reason_code] ?? (next === "unavailable" ? "Browser request unavailable. Try again." : "Soil evidence is withheld.")); }
      else { setClock(Date.now()); setResponse(value); setStatus("Reviewed snapshot received"); }
    } catch { if (controller.current === abort) { setResponse(null); setEvidenceRecord(null); setBrowserState("unavailable"); setStatus("Browser request unavailable. Try again."); } }
    finally { clearTimeout(timeout); if (controller.current === abort) setLoading(false); }
  }, []);
  // Daily data: a ten-minute recheck is enough to notice a withdrawal or replacement.
  useEffect(() => { const initial = setTimeout(() => void refresh(), 0); const interval = setInterval(() => void refresh(), 600000); return () => { clearTimeout(initial); controller.current?.abort(); controller.current = null; clearInterval(interval); }; }, [refresh]);
  useEffect(() => {
    if (!response?.data) return;
    const remaining = approvalRemainingMs(response.data.approval_expires_at, Date.now());
    if (remaining <= 0) return;
    const timer = setTimeout(() => setClock(Date.now()), Math.min(remaining, 2147483647));
    return () => clearTimeout(timer);
  }, [response]);
  const expired = Boolean(response?.data && approvalRemainingMs(response.data.approval_expires_at, clock) <= 0);
  const data = expired ? null : response?.data, station = data?.stations?.find(s => s.id === selected);
  const evidence = evidenceRecord?.stationId === selected && evidenceRecord.packageId === data?.package_id ? evidenceRecord.value : null;
  const shownStatus = expired ? "Release approval expired. Check for a reviewed update." : status;
  const shownBrowserState = expired ? "withheld" : browserState;
  const shownRender = !visible || !data ? "Hidden" : !styleReady ? "Not ready" : render;
  const freshness = (data?.freshness_at_capture ?? {}) as Record<string, string>;
  useEffect(() => { onSelectionChange?.(visible); }, [visible, onSelectionChange]);
  const latest = latestSoilDay(data?.observations, selected);
  useEffect(() => {
    const map = mapRef.current; if (!map || !styleReady) return;
    const remove = () => { try { if (map.getLayer(LAYER)) map.removeLayer(LAYER); if (map.getSource(SOURCE)) map.removeSource(SOURCE); } catch { /* Map teardown already removed its sources. */ } };
    remove();
    if (!visible || !data?.stations) return;
    try {
      const states = (data.freshness_at_capture ?? {}) as Record<string, string>;
      map.addSource(SOURCE, { type: "geojson", data: { type: "FeatureCollection", features: data.stations.map(s => ({ type: "Feature", id: s.id, geometry: s.geometry, properties: { stationId: s.id, freshness: states[s.id] ?? "UNKNOWN" } })) } });
      // A station that has stopped reporting is drawn hollow, never as a current reading.
      map.addLayer({ id: LAYER, type: "circle", source: SOURCE, paint: { "circle-radius": 7, "circle-color": ["match", ["get", "freshness"], "RECENT", "#a47148", "rgba(0,0,0,0)"], "circle-stroke-color": "#3e2614", "circle-stroke-width": 2 } });
      const clicked = (event: { features?: { properties: Record<string, unknown> | null }[] }) => { const id = event.features?.[0]?.properties?.stationId; if (typeof id === "string" && data.stations?.some(s => s.id === id)) chooseStation(id); };
      const rendered = () => setRender("Map frame drawn");
      map.on("click", LAYER, clicked); map.once("idle", rendered);
      return () => { map.off("click", LAYER, clicked); map.off("idle", rendered); remove(); };
    } catch {
      // The external renderer failed during source installation; surface that failure immediately.
      // eslint-disable-next-line react-hooks/set-state-in-effect
      setRender("Map rendering unavailable"); remove();
    }
  }, [mapRef, styleReady, visible, data, chooseStation]);
  useEffect(() => {
    if (!data || !response) return;
    const abort = new AbortController(), timeout = setTimeout(() => { abort.abort(); setResponse(null); setEvidenceRecord(null); setBrowserState("unavailable"); setStatus("Evidence request timed out. Data withheld."); }, 15000);
    void fetch(`${ROUTE}/evidence?station_id=${encodeURIComponent(selected)}`, { signal: abort.signal, cache: "no-store" }).then(r => readBoundedJson(r, 1024 * 1024)).then(value => { const next = value as SoilResponse; clearTimeout(timeout); if (abort.signal.aborted) return;
      if (soilEvidenceMatchesSelection(response, next, selected)) setEvidenceRecord({ stationId: selected, packageId: data.package_id, value: next });
      else { setResponse(null); setEvidenceRecord(null); setBrowserState("withheld"); setStatus("Evidence or release changed. Check the connection again."); }
    }).catch(() => { clearTimeout(timeout); if (!abort.signal.aborted) { setResponse(null); setEvidenceRecord(null); setBrowserState("unavailable"); setStatus("Evidence request unavailable. Data withheld."); } });
    return () => { abort.abort(); clearTimeout(timeout); };
  }, [selected, data, response]);
  async function exportStation() {
    setExportStatus("Checking current release…");
    const requested = selected, requestedGeneration = selectionGeneration.current;
    try {
      const fresh = await fetch(`${ROUTE}/layers?station_id=${encodeURIComponent(requested)}`, { cache: "no-store", signal: AbortSignal.timeout(15000) }).then(r => readBoundedJson(r, 2 * 1024 * 1024)) as SoilResponse;
      const refs = await fetch(`${ROUTE}/evidence?station_id=${encodeURIComponent(requested)}`, { cache: "no-store", signal: AbortSignal.timeout(15000) }).then(r => readBoundedJson(r, 1024 * 1024)) as SoilResponse;
      if (selectionGeneration.current !== requestedGeneration || selectedRef.current !== requested || !soilExportMatchesSelection(fresh, refs, requested)
          || approvalRemainingMs(fresh.data?.approval_expires_at, Date.now()) <= 0
          || approvalRemainingMs(refs.data?.approval_expires_at, Date.now()) <= 0) throw new Error("WITHHELD");
      const blob = new Blob([JSON.stringify({ observations: fresh, evidence: refs }, null, 2)], { type: "application/json" }), url = URL.createObjectURL(blob);
      const link = document.createElement("a"); link.href = url; link.download = `kfm-reviewed-soil-${requested}.json`; link.click(); setTimeout(() => URL.revokeObjectURL(url), 1000); setExportStatus("Export includes source, evidence and release references.");
    } catch { setExportStatus("Export withheld: current evidence or release could not be verified."); }
  }
  return <section className="official-context-row" aria-label="Reviewed daily soil snapshot">
    <div className="official-context-primary"><label className="visibility-switch"><input type="checkbox" checked={visible} disabled={!visible && !data} aria-label={visible ? "Hide reviewed soil stations" : "Show reviewed soil stations"} onChange={event => { setVisible(event.target.checked); if (event.target.checked) setRender("Waiting for map frame"); }} /><span aria-hidden="true" /></label><i style={{ "--swatch": "#a47148" } as React.CSSProperties} /><div><strong>Reviewed soil moisture</strong><small>NOAA USCRN · {visible ? !data ? "Selected · held" : shownRender : waterBrowserLabel(shownBrowserState)}</small></div></div>
    <details className="specialty-layer-details"><summary>Evidence, source &amp; controls</summary><div className="official-context-option-body">
    <button type="button" onClick={() => void refresh()} disabled={loading}>{loading ? "Checking…" : "Check connection"}</button>
    <p role="status">{shownStatus}</p><small>Acquisition: {data ? "Preserved capture" : "Not established"} · Browser: {waterBrowserLabel(shownBrowserState)} · Map: {shownRender} · Evidence: {evidence ? "Resolved and released" : "Withheld"}</small>
    {data && <>
      <label>Station<select value={selected} onChange={e => chooseStation(e.target.value)}>{data.stations?.map(s => <option key={s.id} value={s.id}>{s.name}</option>)}</select></label>
      <p>Coverage: {String(data.coverage)} · Freshness: {String(response?.envelope.freshness)} · Station: {freshnessText[freshness[selected]] ?? "Unknown"} · Correction: {String(data.correction_state)}</p>
      {latest && <><p><strong>{latest.date}</strong> (local standard time day) · Station point only; values may be revised</p>
        <table><thead><tr><th scope="col">Depth</th><th scope="col">Soil moisture</th><th scope="col">Soil temperature</th></tr></thead>
          <tbody>{SOIL_DEPTHS.map(depth => <tr key={depth}><th scope="row">{depth} cm</th><td>{soilValueText(latest.moisture[depth])}</td><td>{soilValueText(latest.temperature[depth])}</td></tr>)}</tbody></table></>}
      <details><summary>Evidence and source times</summary><dl><dt>Observation window</dt><dd>{latest ? `to ${latest.date}` : "No reported values"}</dd><dt>KFM retrieval</dt><dd>{String(data.retrieved_at)}</dd><dt>Review</dt><dd>{String(data.reviewed_at)}</dd><dt>Release</dt><dd>{String(data.released_at)}</dd></dl><p>{String(data.attribution)}</p>{evidence?.data?.entries?.[0] && <p><a href={evidence.data.entries[0].bundle.citations[0]} target="_blank" rel="noreferrer">NOAA NCEI source</a></p>}{evidence?.data?.entries?.map(e => <p key={e.series}>{e.series} cm: <code>{e.evidence_ref.ref}</code></p>)}</details>
      <button type="button" disabled={!station || !evidence} onClick={() => void exportStation()}>Export selected station with evidence</button><p role="status">{exportStatus}</p></>}
    </div></details>
  </section>;
}

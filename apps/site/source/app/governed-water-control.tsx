"use client";
import { useCallback, useEffect, useRef, useState, type RefObject } from "react";
import type { Map as MapLibreMap } from "./maplibre-seam";
import { readBoundedJson } from "./bounded-json";
import { approvalRemainingMs, type WaterResponse } from "./governed-water";

const SOURCE = "kfm-reviewed-water", LAYER = "kfm-reviewed-water-points";
const reasonText: Record<string, string> = { NO_APPROVED_SNAPSHOT: "No reviewed water snapshot is active.", AUTHENTICATION_REQUIRED: "Sign in to check reviewed water.", RELEASE_STORE_UNAVAILABLE: "Reviewed water storage is unavailable.", REVIEW_REQUIRED: "This water package is waiting for review.", RIGHTS_OR_SENSITIVITY_HOLD: "Rights or sensitivity review is still required.", CORRECTION_HOLD: "This snapshot has been corrected or withdrawn.", RELEASE_TIME_INVALID: "The release approval has expired or is not yet valid." };
export function GovernedWaterControl({ mapRef, styleReady }: { mapRef: RefObject<MapLibreMap | null>; styleReady: boolean }) {
  const [response, setResponse] = useState<WaterResponse | null>(null), [status, setStatus] = useState("Not checked"), [loading, setLoading] = useState(false);
  const [visible, setVisible] = useState(false), [selected, setSelected] = useState("USGS-06892518"), [render, setRender] = useState("Hidden"), [evidence, setEvidence] = useState<WaterResponse | null>(null);
  const [exportStatus, setExportStatus] = useState("");
  const controller = useRef<AbortController | null>(null);
  const refresh = useCallback(async () => {
    controller.current?.abort(); const abort = new AbortController(); controller.current = abort; setLoading(true); setResponse(null); setEvidence(null); setStatus("Checking current release…");
    const timeout = setTimeout(() => abort.abort(), 15000);
    try {
      const fetched = await fetch("/api/governed/v1/layers", { signal: abort.signal, cache: "no-store", credentials: "same-origin" });
      const value = await readBoundedJson(fetched, 2 * 1024 * 1024) as WaterResponse;
      if (abort.signal.aborted) return;
      if (!value?.envelope || value.envelope.outcome !== "ANSWER" || !Array.isArray(value.data?.stations) || !Array.isArray(value.data?.observations)) { setResponse(null); setEvidence(null); setStatus(reasonText[value?.envelope?.reason_code] ?? "Water evidence is withheld."); }
      else { setResponse(value); setStatus("Reviewed snapshot received"); }
    } catch { if (controller.current === abort) { setResponse(null); setEvidence(null); setStatus("Browser request unavailable. Try again."); } }
    finally { clearTimeout(timeout); if (controller.current === abort) setLoading(false); }
  }, []);
  useEffect(() => { void refresh(); const interval = setInterval(() => void refresh(), 60000); return () => { controller.current?.abort(); controller.current = null; clearInterval(interval); }; }, [refresh]);
  useEffect(() => {
    const expiry = response?.data?.approval_expires_at;
    if (!response?.data) return;
    const remaining = approvalRemainingMs(expiry, Date.now());
    const withhold = () => { setResponse(null); setEvidence(null); setStatus("Release approval expired. Check for a reviewed update."); };
    if (!Number.isFinite(remaining) || remaining <= 0) { withhold(); return; }
    const timer = setTimeout(withhold, Math.min(remaining, 2147483647));
    return () => clearTimeout(timer);
  }, [response]);
  const data = response?.data, station = data?.stations?.find(s => s.id === selected);
  const observations = data?.observations?.filter(r => r.station_id === selected) ?? [];
  const latest = [...observations].sort((a, b) => b.observed_at.localeCompare(a.observed_at))[0];
  useEffect(() => {
    const map = mapRef.current; if (!map || !styleReady) return;
    const remove = () => { try { if (map.getLayer(LAYER)) map.removeLayer(LAYER); if (map.getSource(SOURCE)) map.removeSource(SOURCE); } catch { /* Map teardown already removed its sources. */ } };
    remove();
    if (!visible || !data?.stations) { setRender("Hidden"); return; }
    try {
      map.addSource(SOURCE, { type: "geojson", data: { type: "FeatureCollection", features: data.stations.map(s => ({ type: "Feature", id: s.id, geometry: s.geometry, properties: { stationId: s.id } })) } });
      map.addLayer({ id: LAYER, type: "circle", source: SOURCE, paint: { "circle-radius": 7, "circle-color": "#80f6dd", "circle-stroke-color": "#063c3b", "circle-stroke-width": 2 } });
      const clicked = (event: { features?: { properties: Record<string, unknown> | null }[] }) => { const id = event.features?.[0]?.properties?.stationId; if (typeof id === "string") setSelected(id); };
      const rendered = () => setRender("Map frame drawn");
      map.on("click", LAYER, clicked); map.once("idle", rendered); setRender("Waiting for map frame");
      return () => { map.off("click", LAYER, clicked); map.off("idle", rendered); remove(); };
    } catch { setRender("Map rendering unavailable"); remove(); }
  }, [mapRef, styleReady, visible, data]);
  useEffect(() => {
    setEvidence(null); if (!data) return;
    const abort = new AbortController(), timeout = setTimeout(() => { abort.abort(); setResponse(null); setEvidence(null); setStatus("Evidence request timed out. Data withheld."); }, 15000);
    void fetch(`/api/governed/v1/evidence?station_id=${encodeURIComponent(selected)}`, { signal: abort.signal, cache: "no-store" }).then(r => readBoundedJson(r, 512 * 1024)).then(value => { const next = value as WaterResponse; clearTimeout(timeout); if (abort.signal.aborted) return;
      if (next.envelope?.outcome === "ANSWER" && next.data?.package_id === data.package_id) setEvidence(next);
      else { setResponse(null); setEvidence(null); setStatus("Evidence or release changed. Check the connection again."); }
    }).catch(() => { clearTimeout(timeout); if (!abort.signal.aborted) { setResponse(null); setEvidence(null); setStatus("Evidence request unavailable. Data withheld."); } });
    return () => { abort.abort(); clearTimeout(timeout); };
  }, [selected, data]);
  async function exportObservation() {
    setExportStatus("Checking current release…");
    try {
      const fresh = await fetch(`/api/governed/v1/layers?station_id=${encodeURIComponent(selected)}`, { cache: "no-store", signal: AbortSignal.timeout(15000) }).then(r => readBoundedJson(r, 2 * 1024 * 1024)) as WaterResponse;
      const refs = await fetch(`/api/governed/v1/evidence?station_id=${encodeURIComponent(selected)}`, { cache: "no-store", signal: AbortSignal.timeout(15000) }).then(r => readBoundedJson(r, 512 * 1024)) as WaterResponse;
      if (fresh.envelope?.outcome !== "ANSWER" || refs.envelope?.outcome !== "ANSWER" || fresh.data?.package_id !== refs.data?.package_id || (fresh.data?.observations?.length ?? 0) > 127 || approvalRemainingMs(fresh.data?.approval_expires_at, Date.now()) <= 0 || approvalRemainingMs(refs.data?.approval_expires_at, Date.now()) <= 0) throw new Error("WITHHELD");
      const blob = new Blob([JSON.stringify({ observations: fresh, evidence: refs }, null, 2)], { type: "application/json" }), url = URL.createObjectURL(blob);
      const link = document.createElement("a"); link.href = url; link.download = `kfm-reviewed-water-${selected}.json`; link.click(); setTimeout(() => URL.revokeObjectURL(url), 1000); setExportStatus("Export includes source, evidence and release references.");
    } catch { setExportStatus("Export withheld: current evidence or release could not be verified."); }
  }
  return <section className="official-context-row" aria-label="Reviewed water snapshot">
    <header><strong>Reviewed water snapshot</strong><button type="button" onClick={() => void refresh()} disabled={loading}>{loading ? "Checking…" : "Check connection"}</button></header>
    <p role="status">{status}</p><small>Acquisition: {data ? "Preserved capture" : "Not established"} · Browser: {loading ? "Checking" : data ? "Received" : "No released data"} · Map: {styleReady ? render : "Not ready"} · Evidence: {evidence ? "Resolved and released" : "Withheld"}</small>
    {data && <><label>Show reviewed stations <input type="checkbox" checked={visible} onChange={e => setVisible(e.target.checked)} /></label>
      <label>Station<select value={selected} onChange={e => setSelected(e.target.value)}>{data.stations?.map(s => <option key={s.id} value={s.id}>{s.name}</option>)}</select></label>
      <p>Coverage: {String(data.coverage)} · Freshness: {String(response?.envelope.freshness)} · Correction: {String(data.correction_state)}</p>
      {latest && <p><strong>{latest.value === null ? "No reported value" : `${latest.value} ${latest.unit}`}</strong> {latest.provisional ? "· Provisional" : "· Provider approved"}</p>}
      <details><summary>Evidence and source times</summary><dl><dt>Provider observation</dt><dd>{latest?.observed_at ?? "Unavailable"}</dd><dt>Provider revision</dt><dd>{latest?.provider_revision_at ?? "Unavailable"}</dd><dt>KFM retrieval</dt><dd>{String(data.retrieved_at)}</dd><dt>Review</dt><dd>{String(data.reviewed_at)}</dd><dt>Release</dt><dd>{String(data.released_at)}</dd></dl><p>{String(data.attribution)}</p>{evidence?.data?.entries?.map(e => <p key={e.station_id}><a href={e.bundle.citations[0]} target="_blank" rel="noreferrer">USGS source</a><br /><code>{e.evidence_ref.ref}</code></p>)}</details>
      <button type="button" disabled={!station || !evidence} onClick={() => void exportObservation()}>Export selected station with evidence</button><p role="status">{exportStatus}</p></>}
  </section>;
}

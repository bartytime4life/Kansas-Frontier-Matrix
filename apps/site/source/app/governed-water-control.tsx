"use client";
import { useCallback, useEffect, useRef, useState, type RefObject } from "react";
import type { Map as MapLibreMap } from "./maplibre-seam";
import { readBoundedJson } from "./bounded-json";
import { approvalRemainingMs, type WaterResponse } from "./governed-water";
import { waterBrowserLabel, waterBrowserStateForResponse, waterEvidenceMatchesSelection, waterExportMatchesSelection, type WaterBrowserState } from "./governed-water-availability";

const SOURCE = "kfm-reviewed-water", LAYER = "kfm-reviewed-water-points";
const reasonText: Record<string, string> = { NO_APPROVED_SNAPSHOT: "No reviewed water snapshot is active.", AUTHENTICATION_REQUIRED: "Sign in to check reviewed water.", RELEASE_STORE_UNAVAILABLE: "Reviewed water storage is unavailable.", REVIEW_REQUIRED: "This water package is waiting for review.", RIGHTS_OR_SENSITIVITY_HOLD: "Rights or sensitivity review is still required.", CORRECTION_HOLD: "This snapshot has been corrected or withdrawn.", RELEASE_TIME_INVALID: "The release approval has expired or is not yet valid." };
export function GovernedWaterControl({ mapRef, styleReady, onSelectionChange }: { mapRef: RefObject<MapLibreMap | null>; styleReady: boolean; onSelectionChange?: (selected: boolean) => void }) {
  const [response, setResponse] = useState<WaterResponse | null>(null), [status, setStatus] = useState("Not checked"), [loading, setLoading] = useState(false);
  const [clock, setClock] = useState(Date.now);
  const [browserState, setBrowserState] = useState<WaterBrowserState>("not-checked");
  const [visible, setVisible] = useState(false), [selected, setSelected] = useState("USGS-06892518"), [render, setRender] = useState("Hidden");
  const [evidenceRecord, setEvidenceRecord] = useState<{ stationId: string; packageId: unknown; value: WaterResponse } | null>(null);
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
      const fetched = await fetch("/api/governed/v1/layers", { signal: abort.signal, cache: "no-store", credentials: "same-origin" });
      const value = await readBoundedJson(fetched, 2 * 1024 * 1024) as WaterResponse;
      if (abort.signal.aborted) return;
      const nextBrowserState = waterBrowserStateForResponse(value, fetched.ok);
      setBrowserState(nextBrowserState);
      if (nextBrowserState !== "received") { setResponse(null); setEvidenceRecord(null); setStatus(reasonText[value?.envelope?.reason_code] ?? (nextBrowserState === "unavailable" ? "Browser request unavailable. Try again." : "Water evidence is withheld.")); }
      else { setClock(Date.now()); setResponse(value); setStatus("Reviewed snapshot received"); }
    } catch { if (controller.current === abort) { setResponse(null); setEvidenceRecord(null); setBrowserState("unavailable"); setStatus("Browser request unavailable. Try again."); } }
    finally { clearTimeout(timeout); if (controller.current === abort) setLoading(false); }
  }, []);
  useEffect(() => { const initial = setTimeout(() => void refresh(), 0); const interval = setInterval(() => void refresh(), 60000); return () => { clearTimeout(initial); controller.current?.abort(); controller.current = null; clearInterval(interval); }; }, [refresh]);
  useEffect(() => {
    const expiry = response?.data?.approval_expires_at;
    if (!response?.data) return;
    const remaining = approvalRemainingMs(expiry, Date.now());
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
  useEffect(() => { onSelectionChange?.(visible); }, [visible, onSelectionChange]);
  const observations = data?.observations?.filter(r => r.station_id === selected) ?? [];
  const latest = [...observations].sort((a, b) => b.observed_at.localeCompare(a.observed_at))[0];
  useEffect(() => {
    const map = mapRef.current; if (!map || !styleReady) return;
    const remove = () => { try { if (map.getLayer(LAYER)) map.removeLayer(LAYER); if (map.getSource(SOURCE)) map.removeSource(SOURCE); } catch { /* Map teardown already removed its sources. */ } };
    remove();
    if (!visible || !data?.stations) return;
    try {
      map.addSource(SOURCE, { type: "geojson", data: { type: "FeatureCollection", features: data.stations.map(s => ({ type: "Feature", id: s.id, geometry: s.geometry, properties: { stationId: s.id } })) } });
      map.addLayer({ id: LAYER, type: "circle", source: SOURCE, paint: { "circle-radius": 7, "circle-color": "#80f6dd", "circle-stroke-color": "#063c3b", "circle-stroke-width": 2 } });
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
    void fetch(`/api/governed/v1/evidence?station_id=${encodeURIComponent(selected)}`, { signal: abort.signal, cache: "no-store" }).then(r => readBoundedJson(r, 512 * 1024)).then(value => { const next = value as WaterResponse; clearTimeout(timeout); if (abort.signal.aborted) return;
      if (waterEvidenceMatchesSelection(response, next, selected)) setEvidenceRecord({ stationId: selected, packageId: data.package_id, value: next });
      else { setResponse(null); setEvidenceRecord(null); setBrowserState("withheld"); setStatus("Evidence or release changed. Check the connection again."); }
    }).catch(() => { clearTimeout(timeout); if (!abort.signal.aborted) { setResponse(null); setEvidenceRecord(null); setBrowserState("unavailable"); setStatus("Evidence request unavailable. Data withheld."); } });
    return () => { abort.abort(); clearTimeout(timeout); };
  }, [selected, data, response]);
  async function exportObservation() {
    setExportStatus("Checking current release…");
    const requested = selected, requestedGeneration = selectionGeneration.current;
    try {
      const fresh = await fetch(`/api/governed/v1/layers?station_id=${encodeURIComponent(requested)}`, { cache: "no-store", signal: AbortSignal.timeout(15000) }).then(r => readBoundedJson(r, 2 * 1024 * 1024)) as WaterResponse;
      const refs = await fetch(`/api/governed/v1/evidence?station_id=${encodeURIComponent(requested)}`, { cache: "no-store", signal: AbortSignal.timeout(15000) }).then(r => readBoundedJson(r, 512 * 1024)) as WaterResponse;
      if (selectionGeneration.current !== requestedGeneration || selectedRef.current !== requested || !waterExportMatchesSelection(fresh, refs, requested)
          || approvalRemainingMs(fresh.data?.approval_expires_at, Date.now()) <= 0
          || approvalRemainingMs(refs.data?.approval_expires_at, Date.now()) <= 0) throw new Error("WITHHELD");
      const blob = new Blob([JSON.stringify({ observations: fresh, evidence: refs }, null, 2)], { type: "application/json" }), url = URL.createObjectURL(blob);
      const link = document.createElement("a"); link.href = url; link.download = `kfm-reviewed-water-${requested}.json`; link.click(); setTimeout(() => URL.revokeObjectURL(url), 1000); setExportStatus("Export includes source, evidence and release references.");
    } catch { setExportStatus("Export withheld: current evidence or release could not be verified."); }
  }
  return <section className="official-context-row" aria-label="Reviewed water snapshot">
    <div className="official-context-primary"><label className="visibility-switch"><input type="checkbox" checked={visible} disabled={!visible && !data} aria-label={visible ? "Hide reviewed water stations" : "Show reviewed water stations"} onChange={event => { setVisible(event.target.checked); if (event.target.checked) setRender("Waiting for map frame"); }} /><span aria-hidden="true" /></label><i style={{ "--swatch": "#82c4d2" } as React.CSSProperties} /><div><strong>Reviewed water stations</strong><small>USGS · {visible ? !data ? "Selected · held" : shownRender : waterBrowserLabel(shownBrowserState)}</small></div></div>
    <details className="specialty-layer-details"><summary>Evidence, source &amp; controls</summary><div className="official-context-option-body">
    <button type="button" onClick={() => void refresh()} disabled={loading}>{loading ? "Checking…" : "Check connection"}</button>
    <p role="status">{shownStatus}</p><small>Acquisition: {data ? "Preserved capture" : "Not established"} · Browser: {waterBrowserLabel(shownBrowserState)} · Map: {shownRender} · Evidence: {evidence ? "Resolved and released" : "Withheld"}</small>
    {data && <>
      <label>Station<select value={selected} onChange={e => chooseStation(e.target.value)}>{data.stations?.map(s => <option key={s.id} value={s.id}>{s.name}</option>)}</select></label>
      <p>Coverage: {String(data.coverage)} · Freshness: {String(response?.envelope.freshness)} · Correction: {String(data.correction_state)}</p>
      {latest && <p><strong>{latest.value === null ? "No reported value" : `${latest.value} ${latest.unit}`}</strong> {latest.provisional ? "· Provisional" : "· Provider approved"}</p>}
      <details><summary>Evidence and source times</summary><dl><dt>Provider observation</dt><dd>{latest?.observed_at ?? "Unavailable"}</dd><dt>Provider revision</dt><dd>{latest?.provider_revision_at ?? "Unavailable"}</dd><dt>KFM retrieval</dt><dd>{String(data.retrieved_at)}</dd><dt>Review</dt><dd>{String(data.reviewed_at)}</dd><dt>Release</dt><dd>{String(data.released_at)}</dd></dl><p>{String(data.attribution)}</p>{evidence?.data?.entries?.map(e => <p key={e.station_id}><a href={e.bundle.citations[0]} target="_blank" rel="noreferrer">USGS source</a><br /><code>{e.evidence_ref.ref}</code></p>)}</details>
      <button type="button" disabled={!station || !evidence} onClick={() => void exportObservation()}>Export selected station with evidence</button><p role="status">{exportStatus}</p></>}
    </div></details>
  </section>;
}

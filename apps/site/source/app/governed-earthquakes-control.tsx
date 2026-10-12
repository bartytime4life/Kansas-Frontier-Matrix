"use client";
import { useCallback, useEffect, useRef, useState, type RefObject } from "react";
import type { Map as MapLibreMap } from "./maplibre-seam";
import { readBoundedJson } from "./bounded-json";
import { approvalRemainingMs } from "./governed-water";
import type { EarthquakeResponse } from "./governed-earthquakes";
import { waterBrowserLabel, type WaterBrowserState } from "./governed-water-availability";
import { EARTHQUAKE_MONTH_NAMES, earthquakeBrowserStateForResponse, earthquakeEvidenceMatchesSelection, earthquakeExportMatchesSelection, earthquakeMagnitudeText, earthquakePoints } from "./governed-earthquakes-availability";

const SOURCE = "kfm-reviewed-earthquakes", LAYER = "kfm-reviewed-earthquakes-points", ROUTE = "/api/governed/earthquakes/v1";
const SHOWN_EVENTS = 25;
const reasonText: Record<string, string> = { NO_APPROVED_SNAPSHOT: "No reviewed earthquake snapshot is active.", RELEASE_STORE_UNAVAILABLE: "Reviewed earthquake storage is unavailable.", REVIEW_REQUIRED: "This earthquake package is waiting for review.", RIGHTS_OR_SENSITIVITY_HOLD: "Rights or sensitivity review is still required.", CORRECTION_HOLD: "This snapshot has been corrected or withdrawn.", RELEASE_TIME_INVALID: "The release approval has expired or is not yet valid.", EVIDENCE_NOT_FOUND: "No reviewed earthquakes in that month." };
export function GovernedEarthquakesControl({ mapRef, styleReady, onSelectionChange }: { mapRef: RefObject<MapLibreMap | null>; styleReady: boolean; onSelectionChange?: (selected: boolean) => void }) {
  const [response, setResponse] = useState<EarthquakeResponse | null>(null), [status, setStatus] = useState("Not checked"), [loading, setLoading] = useState(false);
  const [clock, setClock] = useState(Date.now);
  const [browserState, setBrowserState] = useState<WaterBrowserState>("not-checked");
  const [visible, setVisible] = useState(false), [month, setMonth] = useState(0), [render, setRender] = useState("Hidden");
  const [evidenceRecord, setEvidenceRecord] = useState<{ month: number; packageId: unknown; value: EarthquakeResponse } | null>(null);
  const [exportStatus, setExportStatus] = useState("");
  const [months, setMonths] = useState<number[]>([]);
  const controller = useRef<AbortController | null>(null);
  const monthRef = useRef(month);
  const selectionGeneration = useRef(0);
  const withhold = useCallback((state: WaterBrowserState, text: string) => { setResponse(null); setEvidenceRecord(null); setBrowserState(state); setStatus(text); }, []);
  // Bootstrap names the months that have events; the layer is then read one month at a time.
  const refresh = useCallback(async (requested?: number) => {
    controller.current?.abort(); const abort = new AbortController(); controller.current = abort; setLoading(true); setResponse(null); setEvidenceRecord(null); setStatus("Checking current release…"); setBrowserState("checking"); setRender("Waiting for map frame");
    const timeout = setTimeout(() => abort.abort(), 15000);
    try {
      const booted = await fetch(`${ROUTE}/bootstrap`, { signal: abort.signal, cache: "no-store", credentials: "same-origin" });
      const boot = await readBoundedJson(booted, 256 * 1024) as EarthquakeResponse;
      if (abort.signal.aborted) return;
      const listed = Array.isArray(boot?.data?.months) ? boot.data.months.filter(m => Number.isInteger(m) && m >= 1 && m <= 12) : [];
      if (earthquakeBrowserStateForResponse(boot, booted.ok) !== "received" || !listed.length) { withhold(earthquakeBrowserStateForResponse(boot, booted.ok), reasonText[boot?.envelope?.reason_code] ?? "Earthquakes are withheld."); return; }
      setMonths(listed);
      const chosen = requested && listed.includes(requested) ? requested : listed.includes(monthRef.current) ? monthRef.current : listed[listed.length - 1];
      monthRef.current = chosen; setMonth(chosen);
      const fetched = await fetch(`${ROUTE}/layers?month=${chosen}`, { signal: abort.signal, cache: "no-store", credentials: "same-origin" });
      const value = await readBoundedJson(fetched, 8 * 1024 * 1024) as EarthquakeResponse;
      if (abort.signal.aborted) return;
      const next = earthquakeBrowserStateForResponse(value, fetched.ok);
      if (next !== "received") withhold(next, reasonText[value?.envelope?.reason_code] ?? (next === "unavailable" ? "Browser request unavailable. Try again." : "Earthquakes are withheld."));
      else { setBrowserState(next); setClock(Date.now()); setResponse(value); setStatus("Reviewed snapshot received"); }
    } catch { if (controller.current === abort) withhold("unavailable", "Browser request unavailable. Try again."); }
    finally { clearTimeout(timeout); if (controller.current === abort) setLoading(false); }
  }, [withhold]);
  const chooseMonth = useCallback((value: number) => {
    if (monthRef.current !== value) selectionGeneration.current += 1;
    monthRef.current = value; setMonth(value); setExportStatus(""); void refresh(value);
  }, [refresh]);
  // A released year changes only when the owner replaces it: an hourly recheck notices a withdrawal or replacement.
  useEffect(() => { const initial = setTimeout(() => void refresh(), 0); const interval = setInterval(() => void refresh(), 3600000); return () => { clearTimeout(initial); controller.current?.abort(); controller.current = null; clearInterval(interval); }; }, [refresh]);
  useEffect(() => {
    if (!response?.data) return;
    const remaining = approvalRemainingMs(response.data.approval_expires_at, Date.now());
    if (remaining <= 0) return;
    const timer = setTimeout(() => setClock(Date.now()), Math.min(remaining, 2147483647));
    return () => clearTimeout(timer);
  }, [response]);
  const expired = Boolean(response?.data && approvalRemainingMs(response.data.approval_expires_at, clock) <= 0);
  const data = expired ? null : response?.data;
  const evidence = evidenceRecord?.month === month && evidenceRecord.packageId === data?.package_id ? evidenceRecord.value : null;
  const shownStatus = expired ? "Release approval expired. Check for a reviewed update." : status;
  const shownBrowserState = expired ? "withheld" : browserState;
  const shownRender = !visible || !data ? "Hidden" : !styleReady ? "Not ready" : render;
  useEffect(() => { onSelectionChange?.(visible); }, [visible, onSelectionChange]);
  // Strongest first, then newest; the export carries every event in source order.
  const rows = (data?.observations ?? []).slice().sort((a, b) => (b.magnitude ?? -9) - (a.magnitude ?? -9) || (a.origin_utc < b.origin_utc ? 1 : a.origin_utc > b.origin_utc ? -1 : 0));
  const points = earthquakePoints(rows);
  useEffect(() => {
    const map = mapRef.current; if (!map || !styleReady) return;
    const remove = () => { try { if (map.getLayer(LAYER)) map.removeLayer(LAYER); if (map.getSource(SOURCE)) map.removeSource(SOURCE); } catch { /* Map teardown already removed its sources. */ } };
    remove();
    if (!visible || !data?.observations) return;
    try {
      map.addSource(SOURCE, { type: "geojson", data: { type: "FeatureCollection", features: earthquakePoints(data.observations) } });
      // Epicenter estimates only: a dot is where a rupture began, never a shaking or damage area. Size follows
      // magnitude (no magnitude draws smallest); points outside the Kansas rectangle are hollow.
      map.addLayer({ id: LAYER, type: "circle", source: SOURCE, paint: { "circle-radius": ["interpolate", ["linear"], ["get", "magnitude"], -1, 3, 1, 4, 3, 7, 5, 12],
        "circle-stroke-color": "#5a2d0c", "circle-stroke-width": 1.5, "circle-color": ["case", ["get", "margin"], "rgba(0,0,0,0)", ["get", "automatic"], "#e0a35c", "#a8521c"] } });
      const rendered = () => setRender("Map frame drawn");
      map.once("idle", rendered);
      return () => { map.off("idle", rendered); remove(); };
    } catch {
      // The external renderer failed during source installation; surface that failure immediately.
      // eslint-disable-next-line react-hooks/set-state-in-effect
      setRender("Map rendering unavailable"); remove();
    }
  }, [mapRef, styleReady, visible, data]);
  useEffect(() => {
    if (!data || !response || !month) return;
    const abort = new AbortController(), timeout = setTimeout(() => { abort.abort(); withhold("unavailable", "Evidence request timed out. Data withheld."); }, 15000);
    void fetch(`${ROUTE}/evidence?month=${month}`, { signal: abort.signal, cache: "no-store" }).then(r => readBoundedJson(r, 8 * 1024 * 1024)).then(value => { const next = value as EarthquakeResponse; clearTimeout(timeout); if (abort.signal.aborted) return;
      if (earthquakeEvidenceMatchesSelection(response, next, month)) setEvidenceRecord({ month, packageId: data.package_id, value: next });
      else withhold("withheld", "Evidence or release changed. Check the connection again.");
    }).catch(() => { clearTimeout(timeout); if (!abort.signal.aborted) withhold("unavailable", "Evidence request unavailable. Data withheld."); });
    return () => { abort.abort(); clearTimeout(timeout); };
  }, [month, data, response, withhold]);
  async function exportMonth() {
    setExportStatus("Checking current release…");
    const requested = month, requestedGeneration = selectionGeneration.current;
    try {
      const fresh = await fetch(`${ROUTE}/layers?month=${requested}`, { cache: "no-store", signal: AbortSignal.timeout(15000) }).then(r => readBoundedJson(r, 8 * 1024 * 1024)) as EarthquakeResponse;
      const refs = await fetch(`${ROUTE}/evidence?month=${requested}`, { cache: "no-store", signal: AbortSignal.timeout(15000) }).then(r => readBoundedJson(r, 8 * 1024 * 1024)) as EarthquakeResponse;
      if (selectionGeneration.current !== requestedGeneration || monthRef.current !== requested || !earthquakeExportMatchesSelection(fresh, refs, requested)
          || approvalRemainingMs(fresh.data?.approval_expires_at, Date.now()) <= 0
          || approvalRemainingMs(refs.data?.approval_expires_at, Date.now()) <= 0) throw new Error("WITHHELD");
      const blob = new Blob([JSON.stringify({ earthquakes: fresh, evidence: refs }, null, 2)], { type: "application/json" }), url = URL.createObjectURL(blob);
      const link = document.createElement("a"); link.href = url; link.download = `kfm-reviewed-earthquakes-${String(fresh.data?.data_year)}-${String(requested).padStart(2, "0")}.json`; link.click(); setTimeout(() => URL.revokeObjectURL(url), 1000); setExportStatus("Export includes source, evidence and release references.");
    } catch { setExportStatus("Export withheld: current evidence or release could not be verified."); }
  }
  const selection = data?.selection, statuses = Object.entries(selection?.review_status ?? {});
  return <section className="official-context-row" aria-label="Reviewed earthquakes">
    <div className="official-context-primary"><label className="visibility-switch"><input type="checkbox" checked={visible} disabled={!visible && !data} aria-label={visible ? "Hide reviewed earthquakes" : "Show reviewed earthquakes"} onChange={event => { setVisible(event.target.checked); if (event.target.checked) setRender("Waiting for map frame"); }} /><span aria-hidden="true" /></label><i style={{ "--swatch": "#a8521c" } as React.CSSProperties} /><div><strong>Reviewed earthquakes</strong><small>USGS ComCat · {visible ? !data ? "Selected · held" : shownRender : waterBrowserLabel(shownBrowserState)}</small></div></div>
    <details className="specialty-layer-details"><summary>Evidence, source &amp; controls</summary><div className="official-context-option-body">
    <button type="button" onClick={() => void refresh()} disabled={loading}>{loading ? "Checking…" : "Check connection"}</button>
    <p role="status">{shownStatus}</p><small>Acquisition: {data ? "Preserved capture" : "Not established"} · Browser: {waterBrowserLabel(shownBrowserState)} · Map: {shownRender} · Evidence: {evidence ? "Resolved and released" : "Withheld"}</small>
    <p><strong>Catalog solutions, not shaking estimates or alerts.</strong> For current earthquake information use the USGS. The area shown is a Kansas context envelope, not the state boundary; hollow points lie outside a coarse Kansas rectangle. A missing record does not mean no earthquake occurred.</p>
    {data && <>
      <label>Month<select value={month} onChange={e => chooseMonth(Number(e.target.value))}>{months.map(m => <option key={m} value={m}>{EARTHQUAKE_MONTH_NAMES[m - 1]} {String(data.data_year)}</option>)}</select></label>
      <p>Earthquakes this month: {String(selection?.observation_count ?? 0)} · Outside the Kansas rectangle: {String(selection?.context_margin_count ?? 0)} · Magnitude range: {selection?.magnitude_range ? `${selection.magnitude_range[0]} to ${selection.magnitude_range[1]}` : "–"} · Drawn: {points.length} · Freshness: {String(response?.envelope.freshness)} · Correction: {String(data.correction_state)}</p>
      {statuses.length > 0 && <table><thead><tr><th scope="col">Review status</th><th scope="col">Earthquakes</th></tr></thead>
        <tbody>{statuses.map(([state, n]) => <tr key={state}><th scope="row">{state}</th><td>{n}</td></tr>)}</tbody></table>}
      <table><thead><tr><th scope="col">Origin (UTC)</th><th scope="col">Magnitude</th><th scope="col">Depth</th><th scope="col">Place (USGS)</th><th scope="col">Status</th></tr></thead>
        <tbody>{rows.slice(0, SHOWN_EVENTS).map(r => <tr key={r.event_id}><td>{r.origin_utc.slice(0, 19).replace("T", " ")}</td><td>{earthquakeMagnitudeText(r.magnitude, r.magnitude_type)}</td><td>{r.depth_km === null ? "Not reported" : `${r.depth_km} km`}</td><td>{r.place ?? "–"}{r.flags.includes("CONTEXT_MARGIN") ? " (outside Kansas rectangle)" : ""}</td><td>{r.review_status ?? "unknown"}</td></tr>)}</tbody></table>
      {rows.length > SHOWN_EVENTS && <small>Showing the {SHOWN_EVENTS} strongest of {rows.length}; the export carries every earthquake this month.</small>}
      <details><summary>Evidence and source times</summary><dl><dt>Catalog year</dt><dd>{String(data.data_year)} ({String(data.year_state) === "CLOSED" ? "closed year" : "year in progress"}; solutions may be revised)</dd><dt>KFM retrieval</dt><dd>{String(data.retrieved_at)}</dd><dt>Review</dt><dd>{String(data.reviewed_at)}</dd><dt>Release</dt><dd>{String(data.released_at)}</dd></dl><p>{String(data.attribution)}</p>{evidence?.data?.entries?.[0] && <p><a href={evidence.data.entries[0].bundle.citations[0]} target="_blank" rel="noreferrer">USGS ComCat query</a></p>}{evidence?.data?.entries?.map(e => <p key={e.part}>Part {e.part}: <code>{e.evidence_ref.ref}</code></p>)}</details>
      <button type="button" disabled={!evidence} onClick={() => void exportMonth()}>Export selected month with evidence</button><p role="status">{exportStatus}</p></>}
    </div></details>
  </section>;
}

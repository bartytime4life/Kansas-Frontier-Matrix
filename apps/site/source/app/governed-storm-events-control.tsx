"use client";
import { useCallback, useEffect, useRef, useState, type RefObject } from "react";
import type { Map as MapLibreMap } from "./maplibre-seam";
import { readBoundedJson } from "./bounded-json";
import { approvalRemainingMs } from "./governed-water";
import type { StormResponse } from "./governed-storm-events";
import { waterBrowserLabel, type WaterBrowserState } from "./governed-water-availability";
import { STORM_MONTH_NAMES, stormBrowserStateForResponse, stormDamageText, stormEventPoints, stormEvidenceMatchesSelection, stormExportMatchesSelection } from "./governed-storm-events-availability";

const SOURCE = "kfm-reviewed-storm-events", LAYER = "kfm-reviewed-storm-events-points", ROUTE = "/api/governed/storm-events/v1";
const SHOWN_EVENTS = 25;
const reasonText: Record<string, string> = { NO_APPROVED_SNAPSHOT: "No reviewed storm events snapshot is active.", RELEASE_STORE_UNAVAILABLE: "Reviewed storm events storage is unavailable.", REVIEW_REQUIRED: "This storm events package is waiting for review.", RIGHTS_OR_SENSITIVITY_HOLD: "Rights or sensitivity review is still required.", CORRECTION_HOLD: "This snapshot has been corrected or withdrawn.", RELEASE_TIME_INVALID: "The release approval has expired or is not yet valid.", EVIDENCE_NOT_FOUND: "No reviewed events in that month." };
export function GovernedStormEventsControl({ mapRef, styleReady, onSelectionChange }: { mapRef: RefObject<MapLibreMap | null>; styleReady: boolean; onSelectionChange?: (selected: boolean) => void }) {
  const [response, setResponse] = useState<StormResponse | null>(null), [status, setStatus] = useState("Not checked"), [loading, setLoading] = useState(false);
  const [clock, setClock] = useState(Date.now);
  const [browserState, setBrowserState] = useState<WaterBrowserState>("not-checked");
  const [visible, setVisible] = useState(false), [month, setMonth] = useState(0), [render, setRender] = useState("Hidden");
  const [evidenceRecord, setEvidenceRecord] = useState<{ month: number; packageId: unknown; value: StormResponse } | null>(null);
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
      const boot = await readBoundedJson(booted, 256 * 1024) as StormResponse;
      if (abort.signal.aborted) return;
      const listed = Array.isArray(boot?.data?.months) ? boot.data.months.filter(m => Number.isInteger(m) && m >= 1 && m <= 12) : [];
      if (stormBrowserStateForResponse(boot, booted.ok) !== "received" || !listed.length) { withhold(stormBrowserStateForResponse(boot, booted.ok), reasonText[boot?.envelope?.reason_code] ?? "Storm events are withheld."); return; }
      setMonths(listed);
      const chosen = requested && listed.includes(requested) ? requested : listed.includes(monthRef.current) ? monthRef.current : listed[listed.length - 1];
      monthRef.current = chosen; setMonth(chosen);
      const fetched = await fetch(`${ROUTE}/layers?month=${chosen}`, { signal: abort.signal, cache: "no-store", credentials: "same-origin" });
      const value = await readBoundedJson(fetched, 8 * 1024 * 1024) as StormResponse;
      if (abort.signal.aborted) return;
      const next = stormBrowserStateForResponse(value, fetched.ok);
      if (next !== "received") withhold(next, reasonText[value?.envelope?.reason_code] ?? (next === "unavailable" ? "Browser request unavailable. Try again." : "Storm events are withheld."));
      else { setBrowserState(next); setClock(Date.now()); setResponse(value); setStatus("Reviewed snapshot received"); }
    } catch { if (controller.current === abort) withhold("unavailable", "Browser request unavailable. Try again."); }
    finally { clearTimeout(timeout); if (controller.current === abort) setLoading(false); }
  }, [withhold]);
  const chooseMonth = useCallback((value: number) => {
    if (monthRef.current !== value) selectionGeneration.current += 1;
    monthRef.current = value; setMonth(value); setExportStatus(""); void refresh(value);
  }, [refresh]);
  // A historical file changes only when NCEI reissues it: an hourly recheck notices a withdrawal or replacement.
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
  const rows = (data?.observations ?? []).slice().sort((a, b) => a.begin_local < b.begin_local ? -1 : a.begin_local > b.begin_local ? 1 : a.event_id - b.event_id);
  const points = stormEventPoints(rows);
  useEffect(() => {
    const map = mapRef.current; if (!map || !styleReady) return;
    const remove = () => { try { if (map.getLayer(LAYER)) map.removeLayer(LAYER); if (map.getSource(SOURCE)) map.removeSource(SOURCE); } catch { /* Map teardown already removed its sources. */ } };
    remove();
    if (!visible || !data?.observations) return;
    try {
      map.addSource(SOURCE, { type: "geojson", data: { type: "FeatureCollection", features: stormEventPoints(data.observations) } });
      // Report points only: a dot is where a report began, never a path, footprint or warning area.
      map.addLayer({ id: LAYER, type: "circle", source: SOURCE, paint: { "circle-radius": 5, "circle-stroke-color": "#1f1f1f", "circle-stroke-width": 1,
        "circle-color": ["match", ["get", "eventType"], "Tornado", "#b3261e", "Hail", "#2f6fb0", "Thunderstorm Wind", "#d4a017", "Flash Flood", "#127a6b", "Flood", "#127a6b", "#7a7a7a"] } });
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
    void fetch(`${ROUTE}/evidence?month=${month}`, { signal: abort.signal, cache: "no-store" }).then(r => readBoundedJson(r, 8 * 1024 * 1024)).then(value => { const next = value as StormResponse; clearTimeout(timeout); if (abort.signal.aborted) return;
      if (stormEvidenceMatchesSelection(response, next, month)) setEvidenceRecord({ month, packageId: data.package_id, value: next });
      else withhold("withheld", "Evidence or release changed. Check the connection again.");
    }).catch(() => { clearTimeout(timeout); if (!abort.signal.aborted) withhold("unavailable", "Evidence request unavailable. Data withheld."); });
    return () => { abort.abort(); clearTimeout(timeout); };
  }, [month, data, response, withhold]);
  async function exportMonth() {
    setExportStatus("Checking current release…");
    const requested = month, requestedGeneration = selectionGeneration.current;
    try {
      const fresh = await fetch(`${ROUTE}/layers?month=${requested}`, { cache: "no-store", signal: AbortSignal.timeout(15000) }).then(r => readBoundedJson(r, 8 * 1024 * 1024)) as StormResponse;
      const refs = await fetch(`${ROUTE}/evidence?month=${requested}`, { cache: "no-store", signal: AbortSignal.timeout(15000) }).then(r => readBoundedJson(r, 8 * 1024 * 1024)) as StormResponse;
      if (selectionGeneration.current !== requestedGeneration || monthRef.current !== requested || !stormExportMatchesSelection(fresh, refs, requested)
          || approvalRemainingMs(fresh.data?.approval_expires_at, Date.now()) <= 0
          || approvalRemainingMs(refs.data?.approval_expires_at, Date.now()) <= 0) throw new Error("WITHHELD");
      const blob = new Blob([JSON.stringify({ events: fresh, evidence: refs }, null, 2)], { type: "application/json" }), url = URL.createObjectURL(blob);
      const link = document.createElement("a"); link.href = url; link.download = `kfm-reviewed-storm-events-${String(fresh.data?.data_year)}-${String(requested).padStart(2, "0")}.json`; link.click(); setTimeout(() => URL.revokeObjectURL(url), 1000); setExportStatus("Export includes source, evidence and release references.");
    } catch { setExportStatus("Export withheld: current evidence or release could not be verified."); }
  }
  const selection = data?.selection, types = Object.entries(selection?.event_types ?? {});
  return <section className="official-context-row" aria-label="Reviewed storm event reports">
    <div className="official-context-primary"><label className="visibility-switch"><input type="checkbox" checked={visible} disabled={!visible && !data} aria-label={visible ? "Hide reviewed storm event reports" : "Show reviewed storm event reports"} onChange={event => { setVisible(event.target.checked); if (event.target.checked) setRender("Waiting for map frame"); }} /><span aria-hidden="true" /></label><i style={{ "--swatch": "#b3261e" } as React.CSSProperties} /><div><strong>Reviewed storm event reports</strong><small>NOAA Storm Events · {visible ? !data ? "Selected · held" : shownRender : waterBrowserLabel(shownBrowserState)}</small></div></div>
    <details className="specialty-layer-details"><summary>Evidence, source &amp; controls</summary><div className="official-context-option-body">
    <button type="button" onClick={() => void refresh()} disabled={loading}>{loading ? "Checking…" : "Check connection"}</button>
    <p role="status">{shownStatus}</p><small>Acquisition: {data ? "Preserved capture" : "Not established"} · Browser: {waterBrowserLabel(shownBrowserState)} · Map: {shownRender} · Evidence: {evidence ? "Resolved and released" : "Withheld"}</small>
    <p><strong>Historical event reports, not warnings.</strong> For current warnings use the National Weather Service. A missing report does not mean nothing happened.</p>
    {data && <>
      <label>Month<select value={month} onChange={e => chooseMonth(Number(e.target.value))}>{months.map(m => <option key={m} value={m}>{STORM_MONTH_NAMES[m - 1]} {String(data.data_year)}</option>)}</select></label>
      <p>Events this month: {String(selection?.observation_count ?? 0)} · Drawn as report points: {points.length} · Freshness: {String(response?.envelope.freshness)} · Correction: {String(data.correction_state)}</p>
      {types.length > 0 && <table><thead><tr><th scope="col">Event type</th><th scope="col">Reports</th></tr></thead>
        <tbody>{types.map(([type, n]) => <tr key={type}><th scope="row">{type}</th><td>{n}</td></tr>)}</tbody></table>}
      <table><thead><tr><th scope="col">Began (local)</th><th scope="col">Type</th><th scope="col">County or zone</th><th scope="col">Magnitude</th><th scope="col">Property damage</th></tr></thead>
        <tbody>{rows.slice(0, SHOWN_EVENTS).map(r => <tr key={r.event_id}><td>{r.begin_local.replace("T", " ")}</td><td>{r.event_type}</td><td>{r.cz_name} ({r.cz_type === "C" ? "county" : "zone"})</td><td>{[r.magnitude_source, r.magnitude_type, r.tor_f_scale].filter(Boolean).join(" ") || "–"}</td><td>{stormDamageText(r.damage_property_usd, r.damage_property_source)}</td></tr>)}</tbody></table>
      {rows.length > SHOWN_EVENTS && <small>Showing {SHOWN_EVENTS} of {rows.length}; the export carries every event this month.</small>}
      <details><summary>Evidence and source times</summary><dl><dt>Source file</dt><dd>{String(data.source_file)} (NCEI vintage {String(data.vintage_created)})</dd><dt>KFM retrieval</dt><dd>{String(data.retrieved_at)}</dd><dt>Review</dt><dd>{String(data.reviewed_at)}</dd><dt>Release</dt><dd>{String(data.released_at)}</dd></dl><p>{String(data.attribution)}</p>{evidence?.data?.entries?.[0] && <p><a href={evidence.data.entries[0].bundle.citations[0]} target="_blank" rel="noreferrer">NOAA NCEI source</a></p>}{evidence?.data?.entries?.map(e => <p key={e.part}>Part {e.part}: <code>{e.evidence_ref.ref}</code></p>)}</details>
      <button type="button" disabled={!evidence} onClick={() => void exportMonth()}>Export selected month with evidence</button><p role="status">{exportStatus}</p></>}
    </div></details>
  </section>;
}

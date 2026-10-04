"use client";
import { useCallback, useEffect, useRef, useState, type RefObject } from "react";
import type { Map } from "./maplibre-seam";
import { readBoundedJson } from "./bounded-json";
import { bridgeLayerUrl, BRIDGE_TOTAL_LIMIT, type BridgeLayerId, type BridgeResult } from "./kansas-bridge-records";

export function BridgeRecordInspector({ layer, mapRef, enabled, reducedMotion }: {
  layer: BridgeLayerId; mapRef: RefObject<Map | null>; enabled: boolean; reducedMotion: boolean;
}) {
  const [radius, setRadius] = useState(500), [busy, setBusy] = useState(false);
  const [result, setResult] = useState<BridgeResult | null>(null);
  const [status, setStatus] = useState("Center the map on a bridge, then inspect nearby inventory records.");
  const request = useRef<AbortController | null>(null), generation = useRef(0);
  const cancel = useCallback(() => { generation.current++; request.current?.abort(); request.current = null; setBusy(false); }, []);
  useEffect(() => {
    if (!enabled) request.current?.abort();
  }, [enabled]);
  useEffect(() => {
    const pending = request, version = generation;
    return () => { pending.current?.abort(); version.current++; };
  }, []);
  useEffect(() => {
    const map = mapRef.current;
    const moved = () => { if (request.current) { cancel(); setStatus("Map moved. Search again at the new center; any prior results retain their original search location."); } };
    map?.on("movestart", moved);
    return () => { map?.off("movestart", moved); };
  }, [mapRef, cancel, enabled]);
  const search = async () => {
    const map = mapRef.current;
    if (!enabled || !map) return;
    cancel(); const token = generation.current, controller = new AbortController(); request.current = controller;
    const center = map.getCenter();
    const params = new URLSearchParams({ layer, radius: String(radius), longitude: center.lng.toFixed(6), latitude: center.lat.toFixed(6) });
    setBusy(true); setStatus("Checking KDOT records near this map center…");
    const timer = setTimeout(() => controller.abort(), 15000);
    try {
      const response = await fetch(`/api/bridge-records?${params}`, { signal: controller.signal, cache: "no-store" });
      if (!response.ok) throw new Error("Unavailable");
      const next = await readBoundedJson(response, 512 * 1024, controller.signal) as BridgeResult;
      if (controller.signal.aborted || token !== generation.current) return;
      if (!Array.isArray(next.records) || next.records.length > BRIDGE_TOTAL_LIMIT || !Number.isSafeInteger(next.providerCount) || (next.providerCount ?? -1) < next.records.length || !Number.isInteger(next.pagesRead) || (next.pagesRead ?? 0) > 5 || next.query?.layer !== layer || next.query.radius !== radius || next.query.longitude !== Number(params.get("longitude")) || next.query.latitude !== Number(params.get("latitude")) || next.role !== "EXTERNAL_CONTEXT_ONLY") throw new Error("Unexpected response");
      setResult(next);
      setStatus(next.partial ? `Partial KDOT result: ${next.records.length} shown from ${next.providerCount} matching provider records. Narrow the radius or inspect the official service; omitted or changing records may also affect this result.` : next.records.length ? `${next.records.length} matching KDOT inventory records across ${next.pagesRead} page${next.pagesRead === 1 ? "" : "s"}.` : "No matching records in this search area. This does not establish that no bridge exists.");
    } catch {
      if (token === generation.current) setStatus("Records unavailable or timed out. Check that the map center is in Kansas, then retry. Prior results, if any, are retained at their original location.");
    } finally {
      clearTimeout(timer);
      if (token === generation.current) { request.current = null; setBusy(false); }
    }
  };
  return <section className="bridge-record-inspector" aria-label="Bridge inventory inspection">
    <h4>Inspect bridge records</h4>
    <div className="source-time-actions"><label>Search radius<select aria-label="Bridge search radius" value={radius} onChange={e => { cancel(); setRadius(Number(e.target.value)); setStatus("Radius changed. Inspect again to update the results."); }}><option value={100}>100 m</option><option value={500}>500 m</option><option value={1000}>1 km</option></select></label><button type="button" disabled={!enabled || busy} onClick={() => void search()}>{busy ? "Checking…" : "Inspect map center"}</button>{busy && <button type="button" onClick={() => { cancel(); setStatus("Search cancelled. Prior results retain their original location."); }}>Cancel</button>}</div>
    <p role="status">{enabled ? status : "Enable this layer in a Present flat-map view to inspect its records."}</p>
    {result && <>
      <p className="bridge-search-scope">Searched {result.query.latitude.toFixed(5)}, {result.query.longitude.toFixed(5)} · {result.query.radius} m radius. Retrieved {result.retrievedAt.slice(0, 19).replace("T", " ")} UTC.{result.omittedRecords > 0 ? ` ${result.omittedRecords} out-of-scope or invalid records omitted.` : ""}</p>
      <div className="bridge-record-list">{result.records.map(record => <details key={record.objectId}>
        <summary>{record.facility ?? record.name} · {record.distanceMeters} m from search center</summary>
        <dl>
          <div><dt>KDOT identifier</dt><dd>{record.name}</dd></div>
          <div><dt>County / location</dt><dd>{record.county ?? "Not reported"} · {record.location ?? "Not reported"}</dd></div>
          <div><dt>Crossing</dt><dd>{record.crossing ?? "Not reported"}</dd></div>
          <div><dt>Recorded status</dt><dd>{record.recordedStatus ?? "Not reported"}</dd></div>
          <div><dt>Construction / reconstruction year</dt><dd>{record.builtYear ?? "Unknown"} / {record.reconstructedYear ?? "Not reported"}</dd></div>
          <div><dt>Historic designation</dt><dd>{record.historicDesignation ?? "Not supplied by this service"}</dd></div>
          <div><dt>Inspection date (INSPDATE)</dt><dd>{record.inspectionDate ?? "Not reported"}</dd></div>
          <div><dt>Prior inspection field (LASTINSP)</dt><dd>{record.previousInspectionDate ?? "Not reported"}</dd></div>
          {record.modifiedDate && <div><dt>Provider modification field</dt><dd>{record.modifiedDate}</dd></div>}
        </dl>
        <button type="button" disabled={!enabled} onClick={() => mapRef.current?.easeTo({ center: record.coordinates, zoom: Math.max(mapRef.current.getZoom(), 15), duration: reducedMotion ? 0 : 450 })}>Center map on bridge</button>{" "}<a href={record.sourceUrl} target="_blank" rel="noreferrer">Official record</a>
      </details>)}</div>
    </>}
    <small>Point inventory, not deck geometry. Inspection and retrieval dates do not date a closure. Recorded status may lag changes; no structural-safety or access determination.</small>
    <a href={bridgeLayerUrl(layer)} target="_blank" rel="noreferrer">KDOT service and field definitions</a>
  </section>;
}

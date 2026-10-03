"use client";
import { useCallback, useEffect, useRef, useState, type RefObject } from "react";
import type { Map } from "./maplibre-seam";
import { readBoundedJson } from "./bounded-json";
import { blmPlssLayerUrl, BLM_PLSS_LIMIT, gloSearchReference, type BlmPlssLayerId, type BlmPlssQuery, type BlmPlssRecord, type BlmPlssResult } from "./blm-plss-records";

function GloSearchHandoff({ record, query }: { record: BlmPlssRecord; query: BlmPlssQuery }) {
  const reference = gloSearchReference(record, query);
  const [copyStatus, setCopyStatus] = useState("");
  return <div className="glo-search-handoff">
    <strong>Official land-record search</strong>
    <p>Use the survey reference to search Kansas in BLM GLO. Check any patent, plat, or field note there; no GLO document has been matched or reviewed for this map feature.</p>
    {reference ? <output aria-label="BLM survey search reference">{reference}</output> :
      <small>BLM did not return a usable Kansas township identifier for a search handoff. Use the official GLO map search directly.</small>}
    <div className="source-time-actions">
      {reference && <button type="button" onClick={async () => {
          try {
            await navigator.clipboard.writeText(reference);
            setCopyStatus("Survey search reference copied.");
          } catch { setCopyStatus("Clipboard unavailable. Select the visible reference text to copy it."); }
        }}>Copy search reference</button>}
      <a href="https://glorecords.blm.gov/" target="_blank" rel="noopener noreferrer">Open official GLO search ↗</a>
    </div>
    {copyStatus && <small role="status">{copyStatus}</small>}
  </div>;
}

export function BlmPlssInspector({ layer, mapRef, enabled }: {
  layer: BlmPlssLayerId; mapRef: RefObject<Map | null>; enabled: boolean;
}) {
  const [busy, setBusy] = useState(false), [result, setResult] = useState<BlmPlssResult | null>(null);
  const [status, setStatus] = useState("Center the flat map on a survey division, then inspect BLM's identifiers.");
  const pending = useRef<AbortController | null>(null), generation = useRef(0);
  const cancel = useCallback(() => { generation.current++; pending.current?.abort(); pending.current = null; setBusy(false); }, []);
  useEffect(() => {
    if (!enabled) pending.current?.abort();
  }, [enabled]);
  useEffect(() => () => { pending.current?.abort(); generation.current++; }, []);
  useEffect(() => {
    const map = mapRef.current;
    const moved = () => { if (pending.current) { cancel(); setStatus("Map moved. Inspect again at the new center; earlier records keep their original search point."); } };
    map?.on("movestart", moved);
    return () => { map?.off("movestart", moved); };
  }, [mapRef, cancel, enabled]);
  const inspect = async () => {
    const map = mapRef.current;
    if (!enabled || !map) return;
    cancel(); const token = generation.current, controller = new AbortController(); pending.current = controller;
    const center = map.getCenter();
    const params = new URLSearchParams({ layer, longitude: center.lng.toFixed(6), latitude: center.lat.toFixed(6) });
    setBusy(true); setStatus("Checking BLM survey identifiers at this map center…");
    const timer = setTimeout(() => controller.abort(new Error("PLSS inspection timed out.")), 15000);
    try {
      const response = await fetch(`/api/blm-plss-records?${params}`, { signal: controller.signal, cache: "no-store" });
      if (!response.ok) throw new Error("BLM records unavailable.");
      const next = await readBoundedJson(response, 64 * 1024, controller.signal) as BlmPlssResult;
      if (controller.signal.aborted || token !== generation.current) return;
      if (!Array.isArray(next.records) || next.records.length > BLM_PLSS_LIMIT || !Number.isSafeInteger(next.providerCount) || next.providerCount < next.records.length ||
          next.query?.layer !== layer || next.query.longitude !== Number(params.get("longitude")) || next.query.latitude !== Number(params.get("latitude")) ||
          typeof next.partial !== "boolean" || next.role !== "EXTERNAL_CONTEXT_ONLY") throw new Error("Unexpected BLM response.");
      setResult(next);
      setStatus(next.partial ? `Partial BLM lookup: ${next.records.length} shown from ${next.providerCount} provider matches. Inspect the official service for the full set.` :
        next.records.length ? `${next.records.length} BLM survey record${next.records.length === 1 ? "" : "s"} at this map point.` :
          "No BLM survey record returned at this point. This does not establish unsurveyed land or an ownership gap.");
    } catch {
      if (token === generation.current) setStatus("BLM records unavailable or timed out. Check the Kansas map center and retry; earlier results retain their original search point.");
    } finally {
      clearTimeout(timer);
      if (token === generation.current) { pending.current = null; setBusy(false); }
    }
  };
  return <section className="bridge-record-inspector blm-plss-inspector" aria-label="BLM survey record inspection">
    <h4>Inspect PLSS identifiers</h4>
    <div className="source-time-actions"><button type="button" disabled={!enabled || busy} onClick={() => void inspect()}>{busy ? "Checking…" : "Inspect map center"}</button>{busy && <button type="button" onClick={() => { cancel(); setStatus("Inspection cancelled. Earlier results retain their original point."); }}>Cancel</button>}</div>
    <p role="status">{enabled ? status : "Enable this PLSS layer in a Present flat-map view to inspect its identifiers."}</p>
    {result && <>
      <p className="bridge-search-scope">Point {result.query.latitude.toFixed(5)}, {result.query.longitude.toFixed(5)} · retrieved {result.retrievedAt.slice(0, 19).replace("T", " ")} UTC.{result.omittedRecords ? ` ${result.omittedRecords} out-of-scope records withheld.` : ""}</p>
      <div className="bridge-record-list">{result.records.map(record => <details key={record.objectId}>
        <summary>{record.secondDivisionLabel ?? record.firstDivisionLabel ?? record.townshipLabel ?? record.plssId} · {record.plssId}</summary>
        <dl>
          <div><dt>PLSS township ID</dt><dd>{record.plssId}</dd></div>
          {record.townshipLabel && <div><dt>Township label</dt><dd>{record.townshipLabel}</dd></div>}
          {record.principalMeridian && <div><dt>Principal meridian</dt><dd>{record.principalMeridian}</dd></div>}
          {record.firstDivisionId && <div><dt>First division ID</dt><dd>{record.firstDivisionId}</dd></div>}
          {record.firstDivisionLabel && <div><dt>First division label / type</dt><dd>{record.firstDivisionLabel} · {record.firstDivisionType ?? "Not reported"}</dd></div>}
          {record.secondDivisionId && <div><dt>Intersected division ID</dt><dd>{record.secondDivisionId}</dd></div>}
          {record.secondDivisionLabel && <div><dt>Intersected label / type</dt><dd>{record.secondDivisionLabel} · {record.secondDivisionType ?? "Not reported"}</dd></div>}
          <div><dt>Source document date</dt><dd>{record.sourceDocumentDate ?? "Not reported"}</dd></div>
          {record.revisedDate && <div><dt>Provider revision date</dt><dd>{record.revisedDate}</dd></div>}
          {record.sourceReference && <div><dt>Source reference</dt><dd>{record.sourceReference}</dd></div>}
        </dl>
        <a href={record.officialRecordUrl} target="_blank" rel="noopener noreferrer">BLM survey feature attributes ↗</a>
        <GloSearchHandoff record={record} query={result.query} />
      </details>)}</div>
    </>}
    <small>PLSS survey reference only. These identifiers do not establish a parcel, owner, legal title, public access, or an exact surveyed corner. Source dates are separate from retrieval time.</small>
    <a href={blmPlssLayerUrl(layer)} target="_blank" rel="noreferrer">BLM service and field definitions ↗</a>
  </section>;
}

"use client";

import { useEffect, useRef, useState } from "react";
import {
  inspectSeismicSnapshot, previewScope, SEISMIC_PREVIEW_MAX_BYTES,
  SeismicPreviewSession, type PreviewSessionState,
} from "./seismic-snapshot-preview";

const phaseText: Record<PreviewSessionState["phase"], string> = {
  IDLE: "No file inspected", PROCESSING: "Inspecting local file",
  PREVIEW: "Local preview loaded — not admitted",
  STALE_PREVIEW: "Import failed — previous same-window preview retained",
  ERROR: "Import failed — no data substituted",
};
const utc = (ms: number | null) => ms === null ? "Not supplied" : new Date(ms).toISOString();

/** Lives beside the existing local waveform utility; never submits candidates to the map or Evidence Drawer. */
export default function SeismicSnapshotPanel() {
  const session = useRef(new SeismicPreviewSession());
  const [state, setState] = useState(session.current.state);
  const [startDay, setStartDay] = useState("");
  const [endDay, setEndDay] = useState("");
  const input = useRef<HTMLInputElement>(null);
  const startMs = Date.parse(`${startDay}T00:00:00.000Z`);
  const endMs = Date.parse(`${endDay}T00:00:00.000Z`);
  const validWindow = Number.isFinite(startMs) && Number.isFinite(endMs) && startMs < endMs;
  useEffect(() => { const controller = session.current; return () => controller.clear(); }, []);
  const clear = () => {
    session.current.clear(); setState(session.current.state);
    if (input.current) input.current.value = "";
  };
  const inspect = async (file: File | undefined) => {
    if (!file || !validWindow) return;
    const scope = previewScope(startMs, endMs);
    const ticket = session.current.begin(scope);
    setState(session.current.state);
    try {
      if (!file.size || file.size > SEISMIC_PREVIEW_MAX_BYTES) throw new Error("FILE_BOUND");
      const result = await inspectSeismicSnapshot(await file.arrayBuffer(), scope, new Date().toISOString());
      if (session.current.accept(ticket, result)) setState(session.current.state);
    } catch {
      if (session.current.fail(ticket)) setState(session.current.state);
    }
    if (input.current) input.current.value = "";
  };
  const selected = state.preview?.events.find((event) => event.id === state.selectedId);
  return <details className="waveform-preview-panel">
    <summary>Earthquake catalog file inspection · local preview only</summary>
    <p>Choose a USGS-format GeoJSON file you are permitted to inspect. File origin is unverified.
      No URL request, upload, saved cache, source admission, map layer, or report evidence is created.</p>
    <p>Kansas context envelope: −102.1 to −94.5 longitude; 36.9 to 40.1 latitude. This is not a legal state boundary.</p>
    <label>Start date (UTC, included) <input type="date" value={startDay} onChange={(e) => { clear(); setStartDay(e.target.value); }} /></label>
    <label>End date (UTC, excluded) <input type="date" value={endDay} onChange={(e) => { clear(); setEndDay(e.target.value); }} /></label>
    {!validWindow && <p>Enter a start date before the end date to enable file inspection.</p>}
    <label>Local GeoJSON (8 MiB and 10,000 records maximum)
      <input ref={input} type="file" disabled={!validWindow} accept=".json,.geojson,application/geo+json,application/json"
        onChange={(e) => void inspect(e.target.files?.[0])} /></label>
    <button type="button" onClick={clear}>Clear earthquake preview</button>
    <p role="status" aria-live="polite">{phaseText[state.phase]}</p>
    {state.preview && <>
      <p>{state.preview.events.length} matching earthquake records of {state.preview.suppliedCount} supplied;
        {" "}{state.preview.excludedCount} excluded by type, time or envelope. No catalog completeness or all-clear is implied.</p>
      <dl className="waveform-file-metadata">
        <div><dt>File integrity</dt><dd>{state.preview.sha256}</dd></div>
        <div><dt>Inspected locally</dt><dd>{state.preview.inspectedAt}</dd></div>
        <div><dt>File-reported generation</dt><dd>{utc(state.preview.generatedMs)}</dd></div>
        <div><dt>Admission</dt><dd>NOT_ADMITTED · file shape is not provider authentication</dd></div>
      </dl>
      <p>Showing the first {Math.min(200, state.preview.events.length)} matching records in file order.</p>
      <ul>{state.preview.events.slice(0, 200).map((event) => <li key={event.id}>
        <button type="button" aria-pressed={state.selectedId === event.id} onClick={() => {
          session.current.select(event.id); setState(session.current.state);
        }}>{event.id} · magnitude {event.magnitude ?? "not supplied"} · {utc(event.originMs)}</button>
      </li>)}</ul>
      {selected && <section aria-label="Selected local earthquake record">
        <h4>{selected.id} — unadmitted local record</h4>
        <dl className="waveform-file-metadata">
          <div><dt>Origin time (UTC)</dt><dd>{utc(selected.originMs)}</dd></div>
          <div><dt>Provider-reported update (UTC)</dt><dd>{utc(selected.updatedMs)}</dd></div>
          <div><dt>Magnitude and method</dt><dd>{selected.magnitude ?? "Not supplied"} · {selected.magnitudeType ?? "Not supplied"}</dd></div>
          <div><dt>Depth in km (not surface elevation)</dt><dd>{selected.depthKm ?? "Not supplied"}</dd></div>
          <div><dt>Longitude / latitude</dt><dd>{selected.longitude} / {selected.latitude}</dd></div>
          <div><dt>Provider-reported review status</dt><dd>{selected.reviewStatus ?? "Not supplied"}</dd></div>
        </dl>
        <p>This inspection does not resolve an EvidenceBundle or establish earthquake causation, damage, or safety.</p>
      </section>}
    </>}
  </details>;
}

"use client";
import { useLayoutEffect, useState, type RefObject } from "react";
import { createPortal } from "react-dom";
import type { Map as MapLibreMap } from "./maplibre-seam";
import { bindLivingWaters, LIVING_WATERS_PROOF as proof, projectLivingWaters, type FixtureCorrection } from "./living-waters-fixture";

export function LivingWatersControl({ mapRef, styleReady, flatMap, onFlatMap, onInspect }: {
  mapRef: RefObject<MapLibreMap | null>; styleReady: boolean; flatMap: boolean; onFlatMap: () => void; onInspect?: () => void;
}) {
  const [open, setOpen] = useState(false), [visible, setVisible] = useState(false);
  const [scenarioId, setScenarioId] = useState("current"), [pointIndex, setPointIndex] = useState(0);
  const [correction, setCorrection] = useState<FixtureCorrection>("BASELINE"), [opacity, setOpacity] = useState(0.8);
  const [selected, setSelected] = useState<string | null>(null), [render, setRender] = useState("Hidden");
  const projected = projectLivingWaters(scenarioId, pointIndex, correction);
  const canShow = open && visible && flatMap && projected.features.features.length > 0;
  useLayoutEffect(() => {
    const map = mapRef.current;
    if (!map || !styleReady) return;
    try {
      const data = canShow ? projectLivingWaters(scenarioId, pointIndex, correction).features : { type: "FeatureCollection" as const, features: [] };
      return bindLivingWaters(map, data, opacity, setSelected, () => setRender("Map frame drawn"), () => setRender("Map rendering unavailable"));
    } catch {
      // eslint-disable-next-line react-hooks/set-state-in-effect
      setRender("Map rendering unavailable");
    }
  }, [mapRef, styleReady, canShow, scenarioId, pointIndex, correction, opacity]);
  const selectedFeature = canShow ? projected.features.features.find(feature => feature.id === selected) : undefined;
  const change = () => { setSelected(null); setRender("Waiting for map frame"); };
  const close = () => { setOpen(false); setVisible(false); setSelected(null); setCorrection("BASELINE"); setRender("Hidden"); };
  return <section className="official-context-row" aria-label="Synthetic Living Waters proof">
    {canShow && createPortal(<aside aria-label="Synthetic map presentation" style={{ position: "fixed", left: 12, bottom: 84, zIndex: 75, maxWidth: "calc(100vw - 24px)", padding: 12, background: "#221331", color: "#fff", border: "2px dashed #c084fc", borderRadius: 8 }}><strong>SYNTHETIC LIVING WATERS{projected.stale ? " · STALE" : ""}</strong><br />Illustrative positions · {projected.point?.observed_at}<br /><button type="button" onClick={onInspect}>Inspect synthetic evidence</button><button type="button" onClick={close}>Close synthetic map proof</button></aside>, document.body)}
    <header><strong>Living Waters · SYNTHETIC PROOF</strong><button type="button" aria-expanded={open} onClick={() => open ? close() : setOpen(true)}>{open ? "Close proof" : "Inspect synthetic proof"}</button></header>
    <p>Finite fixture scenarios · illustrative geometry · no real observations.</p>
    {open && <>
      <label>Fixture scenario<select value={scenarioId} onChange={event => { change(); setScenarioId(event.target.value); }}>{proof.packet.scenarios.map(item => <option key={item.id} value={item.id}>{item.id} · {item.state}</option>)}</select></label>
      <p role="status"><strong>SYNTHETIC · {projected.state}{projected.stale && projected.state !== "STALE" ? " · STALE" : ""}</strong><br />Backend fixture decision: {projected.envelope?.outcome ?? "ERROR"}<br />{projected.message}<br /><code>{projected.envelope?.reason_code ?? "SCENARIO_UNKNOWN"}</code></p>
      {!flatMap && <button type="button" onClick={onFlatMap}>Use flat 2D for synthetic proof</button>}
      <label>Show synthetic schematic<input type="checkbox" checked={visible} onChange={event => { change(); setVisible(event.target.checked); }} /></label>
      <small>Map: {!canShow ? "Hidden" : !styleReady ? "Not ready" : render} · Dashed reaches / purple support are illustrative, not mapped waterways or a HUC12 boundary.</small>
      <label>Synthetic opacity<input type="range" min="0" max="1" step="0.1" value={opacity} onChange={event => { change(); setOpacity(Number(event.target.value)); }} /></label>
      <button type="button" disabled={!canShow || !styleReady} onClick={() => mapRef.current?.fitBounds([[-98.65, 38.4], [-98.25, 38.7]], { padding: 60, duration: 0 })}>Fit synthetic schematic</button>
      <label>Exact fixture sample<select value={pointIndex} onChange={event => { change(); setPointIndex(Number(event.target.value)); }}>{proof.packet.series.points.map((point, index) => <option key={point.observed_at} value={index}>{point.observed_at}</option>)}</select></label>
      {projected.point && <p><strong>{projected.point.value} {proof.packet.series.unit_code}</strong> · SYNTHETIC {proof.packet.series.parameter_name} · {proof.packet.series.statistic_name} · {proof.packet.series.qualifier_name}<br />{projected.point.observed_at}</p>}
      <p>Fixture time only: {proof.packet.series.points[0].observed_at} through {proof.packet.series.points.at(-1)?.observed_at}. No interpolation or present-day validity is asserted.</p>
      <p>Uncertainty: provisional qualifier; no numerical accuracy or confidence supplied. Gauge support: {proof.packet.gauge.spatial_support}. Snapshot role: {proof.packet.snapshot.role}; gauge role: {proof.packet.gauge.role}; series role: {proof.feature_source_role}. Regulatory context is not an observed event.</p>
      <label>Inspect fixture feature<select value={selectedFeature ? selected ?? "" : ""} onChange={event => setSelected(event.target.value || null)}><option value="">Select a schematic feature</option>{canShow && projected.features.features.map(feature => <option key={String(feature.id)} value={String(feature.id)}>{String(feature.properties?.label)} · {String(feature.id)}</option>)}</select></label>
      <details open={Boolean(selectedFeature)}><summary>Synthetic evidence and lineage</summary>
        {selectedFeature && <p>Selected: {String(selectedFeature.id)} · {String(selectedFeature.properties?.role)}</p>}
        <dl><dt>Packet</dt><dd><code>{proof.packet.packet_id}</code></dd><dt>Packet digest</dt><dd><code>{proof.packet_sha256}</code></dd><dt>EvidenceBundle</dt><dd><code>{proof.evidence_bundle.bundle_id}</code></dd><dt>Bundle spec hash</dt><dd><code>{proof.evidence_bundle.spec_hash.value}</code></dd><dt>Proof record</dt><dd><code>{proof.proof_record_hash}</code></dd><dt>Evaluated at (fixture)</dt><dd>{projected.envelope?.evaluated_at}</dd><dt>Snapshot identity / version</dt><dd>{proof.packet.snapshot.identity} · {proof.packet.snapshot.version}</dd><dt>Snapshot declared fixture digest</dt><dd><code>{proof.packet.snapshot.content_digest}</code> · placeholder, not a provider artifact checksum</dd><dt>Join</dt><dd>{projected.scenario?.join_outcome}</dd><dt>License</dt><dd>{proof.evidence_bundle.rights.license}</dd><dt>Correction</dt><dd>{correction} · no provider correction history supplied</dd></dl>
        {proof.evidence_bundle.citations.map(citation => <p key={citation}>{citation}</p>)}
        {projected.envelope?.evidence_refs.map(ref => <p key={ref}><code>{ref}</code></p>)}
      </details>
      <button type="button" onClick={() => { change(); setCorrection("CORRECTION_HOLD"); }}>Rehearse correction hold</button>
      <button type="button" onClick={() => { change(); setCorrection("BASELINE"); }}>Restore pinned fixture</button>
      <p>Local rehearsal only. Closing rolls back this map presentation. Dry-run candidate: {proof.rollback_rehearsal.release_candidate}; rollback: {proof.rollback_rehearsal.rollback_target}. Source admission, release, deployment and acceptance remain separate.</p>
    </>}
  </section>;
}

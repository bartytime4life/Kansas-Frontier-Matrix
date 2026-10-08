import proof from "./living-waters-proof.json";
import type { FeatureCollection, Geometry } from "geojson";
import type { Map as MapLibreMap, MapEventType } from "./maplibre-seam";

export const LIVING_WATERS_PROOF = proof;
export const LIVING_WATERS_SOURCE = "kfm-synthetic-living-waters";
export const LIVING_WATERS_LAYERS = ["kfm-synthetic-water-area", "kfm-synthetic-water-reaches", "kfm-synthetic-water-gauge"] as const;
export type FixtureCorrection = "BASELINE" | "CORRECTION_HOLD";

/** The only input is a checked, bundled fixture. There is no provider fallback. */
export function projectLivingWaters(scenarioId: string, pointIndex: number, correction: FixtureCorrection) {
  const scenario = proof.packet.scenarios.find(item => item.id === scenarioId);
  const envelope = proof.scenarios.find(item => item.id === scenarioId)?.envelope;
  const point = Number.isInteger(pointIndex) ? proof.packet.series.points[pointIndex] : undefined;
  const held = correction !== "BASELINE";
  const answer = Boolean(!held && scenario && envelope?.outcome === "ANSWER" && point);
  const stale = scenario?.state === "STALE";
  const features: FeatureCollection<Geometry> = { type: "FeatureCollection", features: [] };
  if (answer) {
    // Deliberately schematic Kansas display positions; never source geometry.
    // In particular, this polygon is NOT the packet's named HUC12 boundary.
    const add = (id: string, kind: string, role: string, geometry: Geometry) => features.features.push({
      type: "Feature", id, geometry, properties: { id, kind, role, synthetic: true,
        label: `SYNTHETIC ${kind}${stale ? " · STALE" : ""}`, geometryRole: "schematic_display_only",
        packetId: proof.packet.packet_id, bundleId: proof.evidence_bundle.bundle_id,
        observedAt: point!.observed_at, stale },
    });
    add(proof.packet.snapshot.identity, "support", proof.packet.snapshot.role, { type: "Polygon", coordinates: [
      [[-98.65, 38.4], [-98.25, 38.4], [-98.25, 38.7], [-98.65, 38.7], [-98.65, 38.4]],
    ] });
    add(proof.packet.snapshot.reach_ids[0], "reach", proof.packet.snapshot.role, { type: "LineString", coordinates: [[-98.6, 38.6], [-98.45, 38.55]] });
    add(proof.packet.snapshot.reach_ids[1], "reach", proof.packet.snapshot.role, { type: "LineString", coordinates: [[-98.45, 38.55], [-98.3, 38.48]] });
    add(proof.packet.gauge.site_id, "gauge", proof.packet.gauge.role, { type: "Point", coordinates: [-98.45, 38.55] });
  }
  return { scenario, envelope, features, point: answer ? point : null, stale,
    state: held ? "CORRECTION_HOLD" : !scenario || !envelope || !point ? "UNAVAILABLE" : scenario.state,
    message: held ? "Local correction rehearsal: fixture presentation withheld." : scenario?.display_message ?? "Unknown fixture selection; presentation withheld.",
  };
}

/** Own only this fixture's source, layers and callbacks, including style reload. */
export function bindLivingWaters(map: MapLibreMap, data: FeatureCollection<Geometry>, opacity: number, inspect: (id: string) => void, drawn: () => void, unavailable: () => void = () => {}) {
  let active = true;
  const remove = () => {
    for (const id of [...LIVING_WATERS_LAYERS].reverse()) if (map.getLayer(id)) map.removeLayer(id);
    if (map.getSource(LIVING_WATERS_SOURCE)) map.removeSource(LIVING_WATERS_SOURCE);
  };
  const clicked = (event: { features?: { properties?: Record<string, unknown> | null }[] }) => {
    const id = event.features?.[0]?.properties?.id;
    if (active && typeof id === "string" && data.features.some(feature => feature.id === id)) inspect(id);
  };
  const rendered = () => { if (active) drawn(); };
  const dispose = () => {
    active = false;
    for (const id of LIVING_WATERS_LAYERS) map.off("click", id, clicked);
    map.off("idle", rendered);
    map.off("error", failed);
    try { remove(); } catch { /* Renderer may already be destroyed. */ }
  };
  const failed = (event: MapEventType["error"] & { sourceId?: string }) => {
    if (!active || event.sourceId !== LIVING_WATERS_SOURCE) return;
    dispose(); unavailable();
  };
  try {
    remove();
    if (!data.features.length) return dispose;
    const alpha = Number.isFinite(opacity) ? Math.max(0, Math.min(1, opacity)) : 0;
    map.addSource(LIVING_WATERS_SOURCE, { type: "geojson", data });
    map.addLayer({ id: LIVING_WATERS_LAYERS[0], type: "fill", source: LIVING_WATERS_SOURCE,
      filter: ["==", ["get", "kind"], "support"], paint: { "fill-color": "#c084fc", "fill-opacity": alpha * 0.15 } });
    map.addLayer({ id: LIVING_WATERS_LAYERS[1], type: "line", source: LIVING_WATERS_SOURCE,
      filter: ["==", ["get", "kind"], "reach"], paint: { "line-color": "#c084fc", "line-width": 4, "line-dasharray": [2, 2], "line-opacity": alpha } });
    map.addLayer({ id: LIVING_WATERS_LAYERS[2], type: "circle", source: LIVING_WATERS_SOURCE,
      filter: ["==", ["get", "kind"], "gauge"], paint: { "circle-color": "#c084fc", "circle-radius": 8, "circle-opacity": alpha } });
    for (const id of LIVING_WATERS_LAYERS) map.on("click", id, clicked);
    map.once("idle", rendered);
    map.on("error", failed);
    return dispose;
  } catch (error) { dispose(); throw error; }
}

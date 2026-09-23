import { LAYER_REGISTRY } from "./explorer-data";
import { BASEMAPS } from "./map-runtime";
import type { MapSnapshot, ReportDraft, StoryDraft } from "./workspace-model";

export const REPORT_STORAGE_KEY = "kfm-report-draft-v2";
export const STORY_STORAGE_KEY = "kfm-story-draft-v2";
const object = (value: unknown): value is Record<string, unknown> => Boolean(value) && typeof value === "object" && !Array.isArray(value);
const text = (value: unknown): value is string => typeof value === "string" && value.length <= 24000;
const strings = (value: unknown): value is string[] => Array.isArray(value) && value.length <= 1000 && value.every(text);
const number = (value: unknown): value is number => typeof value === "number" && Number.isFinite(value);
const registryIds = () => ({
  layerIds: new Set(LAYER_REGISTRY.map((layer) => layer.id)),
  featureIds: new Set(LAYER_REGISTRY.flatMap((layer) => layer.data.features.map((feature) => feature.properties.fid))),
  evidenceRefs: new Set(LAYER_REGISTRY.flatMap((layer) => layer.data.features.map((feature) => feature.properties.citation))),
});
const bounds = (value: unknown) => object(value) && number(value.west) && number(value.east) && number(value.north) && number(value.south)
  && value.west >= -180 && value.east <= 180 && value.south >= -85 && value.north <= 85 && value.west <= value.east && value.south <= value.north;

export function validMapSnapshot(value: unknown): value is MapSnapshot {
  const { layerIds, featureIds, evidenceRefs } = registryIds();
  if (!object(value) || !text(value.id) || !text(value.createdAt) || !object(value.area) || !object(value.camera) || !object(value.committedTime) || !object(value.policy)) return false;
  if (!["selection", "aoi", "viewport"].includes(String(value.area.kind)) || !text(value.area.label) || (value.area.bounds !== undefined && !bounds(value.area.bounds))) return false;
  const camera = value.camera;
  if (camera.center === "WITHHELD_BROWSER_LOCATION") {
    if (value.area.bounds !== undefined) return false;
    if (camera.zoom !== "WITHHELD" || camera.bearing !== "WITHHELD" || camera.pitch !== "WITHHELD") return false;
  } else if (!Array.isArray(camera.center) || camera.center.length !== 2 || !camera.center.every(number)
    || Math.abs(camera.center[0]) > 180 || Math.abs(camera.center[1]) > 85 || !number(camera.zoom) || camera.zoom < 0 || camera.zoom > 22
    || !number(camera.bearing) || Math.abs(camera.bearing) > 360 || !number(camera.pitch) || camera.pitch < 0 || camera.pitch > 85) return false;
  if (!["2D", "Terrain 3D", "Globe", "Compare"].includes(String(value.representation)) || !["mercator", "globe"].includes(String(value.projection)) || !Object.hasOwn(BASEMAPS, String(value.basemap))) return false;
  if (value.evidenceFilter !== undefined && !["ALL", "ANSWER", "MISSING_EVIDENCE", "SOURCE_STALE", "GENERALIZED_GEOMETRY", "RESTRICTED_ACCESS", "DENIED_BY_POLICY", "CORRECTED", "SUPERSEDED", "ERROR"].includes(String(value.evidenceFilter))) return false;
  if (value.comparison !== undefined && (!object(value.comparison) || !layerIds.has(String(value.comparison.layerA)) || !layerIds.has(String(value.comparison.layerB)) || !number(value.comparison.timeA) || !number(value.comparison.timeB))) return false;
  if (value.temporalSweep !== undefined) {
    if (!object(value.temporalSweep)) return false;
    const sweep = value.temporalSweep;
    if (!["snapshot", "moving-window", "event-stepping", "accumulation", "comparison"].includes(String(sweep.mode))
      || !["available-events", "regular-calendar"].includes(String(sweep.stepRule))
      || !number(sweep.frame) || !number(sweep.rangeStart) || !number(sweep.rangeEnd) || !number(sweep.windowStart) || !number(sweep.windowFrames)
      || sweep.rangeStart > sweep.frame || sweep.frame > sweep.rangeEnd || sweep.windowStart < sweep.rangeStart || sweep.windowStart > sweep.frame
      || !Number.isInteger(sweep.windowFrames) || sweep.windowFrames < 1 || sweep.windowFrames > 8 || sweep.interpolation !== false) return false;
  }
  const time = value.committedTime;
  if (!number(time.start) || !number(time.end) || time.start > time.end || time.start < -4540000000 || time.end > new Date().getFullYear() || !text(time.label) || !["instant", "interval", "cumulative", "timeless", "unknown"].includes(String(time.mode))) return false;
  if (!Array.isArray(value.visibleLayers) || value.visibleLayers.length > LAYER_REGISTRY.length || !value.visibleLayers.every((layer) => object(layer) && layerIds.has(String(layer.id)) && text(layer.title) && text(layer.domain) && number(layer.order) && number(layer.opacity) && layer.opacity >= 0 && layer.opacity <= 1 && text(layer.trustState))) return false;
  if (new Set(value.visibleLayers.map((layer) => layer.id)).size !== value.visibleLayers.length) return false;
  if (!strings(value.evidenceRefs) || !value.evidenceRefs.every((ref) => evidenceRefs.has(ref))) return false;
  if (value.inspectableFeatureIds !== undefined && (!strings(value.inspectableFeatureIds) || !value.inspectableFeatureIds.every((id) => featureIds.has(id)))) return false;
  if (value.selection !== null && (!object(value.selection) || !featureIds.has(String(value.selection.featureId)) || !layerIds.has(String(value.selection.layerId)) || !text(value.selection.title) || !evidenceRefs.has(String(value.selection.evidenceReference)))) return false;
  return [value.inspectableRecordCount, value.sourceBackedCount, value.boundedCount].every((count) => number(count) && count >= 0 && count <= 1000)
    && ["ALLOW", "ABSTAIN", "DENY", "ERROR"].includes(String(value.policy.outcome)) && text(value.policy.reason) && ["NONE", "DRAFT_ONLY"].includes(String(value.policy.publicEffect));
}

export function validReportDraft(value: unknown): value is ReportDraft {
  return object(value) && value.status === "DRAFT" && text(value.id) && text(value.title) && text(value.updatedAt) && text(value.researchQuestion)
    && validMapSnapshot(value.snapshot) && strings(value.includedEvidenceIds) && strings(value.generatedFields) && object(value.sections)
    && ["summary", "observations", "findings", "limitations", "openQuestions", "sources"].every((key) => text((value.sections as Record<string, unknown>)[key]));
}

export function validStoryDraft(value: unknown): value is StoryDraft {
  const { evidenceRefs } = registryIds();
  return object(value) && value.status === "DRAFT" && text(value.id) && text(value.title) && text(value.updatedAt) && text(value.researchQuestion)
    && (value.baseSnapshot === undefined || validMapSnapshot(value.baseSnapshot)) && Array.isArray(value.scenes) && value.scenes.length > 0 && value.scenes.length <= 64
    && value.scenes.every((scene) => object(scene) && text(scene.id) && text(scene.title) && text(scene.narrative) && validMapSnapshot(scene.snapshot) && strings(scene.evidenceRefs) && scene.evidenceRefs.every((ref) => evidenceRefs.has(ref)) && strings(scene.caveats) && ["none", "ease"].includes(String(scene.motion)));
}

export function readDraft(key: string): ReportDraft | StoryDraft | null {
  if (typeof window === "undefined") return null;
  try {
    const raw = window.localStorage.getItem(key);
    if (!raw || raw.length > 2000000) return null;
    const value: unknown = JSON.parse(raw);
    if (key === REPORT_STORAGE_KEY && validReportDraft(value)) return value;
    if (key === STORY_STORAGE_KEY && validStoryDraft(value)) return value;
  } catch { /* Storage denial or invalid drafts cannot block the map. */ }
  return null;
}

export function readDraftSnapshot(mode: "reports" | "stories"): MapSnapshot | null {
  const draft = readDraft(mode === "reports" ? REPORT_STORAGE_KEY : STORY_STORAGE_KEY);
  return draft ? "snapshot" in draft ? draft.snapshot : draft.baseSnapshot ?? draft.scenes[0].snapshot : null;
}

import { isMapRuntimeCamera } from "@kfm/maplibre";

import {
  ATLAS_VIEWS,
  LAYER_RECORDS,
  TEMPORAL_EXTENTS,
  evaluateFocusSelection,
  findLayerRecord,
  isLayerTemporallyCompatible,
} from "./registry";
import type {
  MapLayerState,
  MapSnapshot,
  ReportDraft,
  StoryScene,
} from "./types";

type UnknownRecord = Record<string, unknown>;
type DraftGuard<T> = (value: unknown) => value is T;

const SNAPSHOT_FIELDS = [
  "profile",
  "capturedAt",
  "area",
  "representation",
  "basemap",
  "camera",
  "committedTimeId",
  "activeViewId",
  "layers",
  "selectedLayerId",
  "evidenceRefs",
  "publicSafe",
  "draftOnly",
] as const;
const LAYER_STATE_FIELDS = ["id", "visible", "opacity"] as const;
const REPORT_FIELDS = [
  "profile",
  "id",
  "title",
  "researchQuestion",
  "createdAt",
  "snapshot",
  "includedEvidenceRefs",
  "sections",
  "lifecycle",
  "publishable",
] as const;
const REPORT_SECTION_FIELDS = [
  "summary",
  "observations",
  "findings",
  "limitations",
  "openQuestions",
] as const;
const STORY_FIELDS = [
  "profile",
  "id",
  "title",
  "narrative",
  "order",
  "snapshot",
  "evidenceRefs",
  "caveats",
  "motion",
  "lifecycle",
] as const;
const REPRESENTATIONS = new Set(["2D", "TERRAIN_3D", "GLOBE", "COMPARE"]);
const STORY_MOTIONS = new Set(["NONE", "CAMERA_GUIDE"]);

function isRecord(value: unknown): value is UnknownRecord {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function hasExactFields(
  value: UnknownRecord,
  fields: readonly string[],
): boolean {
  const actual = Object.keys(value);
  return actual.length === fields.length &&
    fields.every((field) => Object.hasOwn(value, field));
}

function isNonEmptyString(value: unknown): value is string {
  return typeof value === "string" && value.length > 0;
}

function isIsoTimestamp(value: unknown): value is string {
  if (typeof value !== "string") return false;
  const instant = new Date(value);
  return !Number.isNaN(instant.valueOf()) && instant.toISOString() === value;
}

function isStringArray(value: unknown): value is readonly string[] {
  return Array.isArray(value) && value.every((entry) => typeof entry === "string");
}

function arraysEqual(
  left: readonly string[],
  right: readonly string[],
): boolean {
  return left.length === right.length &&
    left.every((entry, index) => entry === right[index]);
}

function isPersistedLayerState(
  value: unknown,
  committedTimeId: string,
): value is MapLayerState {
  if (!isRecord(value) || !hasExactFields(value, LAYER_STATE_FIELDS)) return false;
  if (
    !isNonEmptyString(value.id) ||
    typeof value.visible !== "boolean" ||
    typeof value.opacity !== "number" ||
    !Number.isFinite(value.opacity) ||
    value.opacity < 0 ||
    value.opacity > 1
  ) {
    return false;
  }
  const layer = findLayerRecord(value.id);
  if (layer === null) return false;
  return !value.visible || (
    layer.availability === "AVAILABLE" &&
    isLayerTemporallyCompatible(layer.temporalExtentId, committedTimeId)
  );
}

export function isPersistedMapSnapshot(value: unknown): value is MapSnapshot {
  if (!isRecord(value) || !hasExactFields(value, SNAPSHOT_FIELDS)) return false;
  if (
    value.profile !== "kfm.explorer.map-snapshot.v1" ||
    !isIsoTimestamp(value.capturedAt) ||
    !isNonEmptyString(value.area) ||
    typeof value.representation !== "string" ||
    !REPRESENTATIONS.has(value.representation) ||
    value.basemap !== "SITE_LOCAL_ATLAS" ||
    !isMapRuntimeCamera(value.camera) ||
    !isNonEmptyString(value.committedTimeId) ||
    !TEMPORAL_EXTENTS.some((entry) => entry.id === value.committedTimeId) ||
    !isNonEmptyString(value.activeViewId) ||
    !ATLAS_VIEWS.some((entry) => entry.id === value.activeViewId) ||
    value.publicSafe !== true ||
    value.draftOnly !== true ||
    !Array.isArray(value.layers) ||
    !isStringArray(value.evidenceRefs)
  ) {
    return false;
  }

  if (
    value.layers.length !== LAYER_RECORDS.length ||
    !value.layers.every((entry) =>
      isPersistedLayerState(entry, value.committedTimeId as string)
    )
  ) {
    return false;
  }
  const layerIds = value.layers.map((entry) => (entry as MapLayerState).id);
  if (new Set(layerIds).size !== LAYER_RECORDS.length) return false;

  if (value.selectedLayerId !== null && !isNonEmptyString(value.selectedLayerId)) {
    return false;
  }
  const selectedLayer = value.selectedLayerId === null
    ? null
    : findLayerRecord(value.selectedLayerId);
  if (value.selectedLayerId !== null && selectedLayer === null) return false;
  const decision = evaluateFocusSelection(
    value.selectedLayerId,
    false,
    value.activeViewId,
  );
  if (
    selectedLayer !== null &&
    decision.outcome !== "DENY" &&
    !isLayerTemporallyCompatible(
      selectedLayer.temporalExtentId,
      value.committedTimeId,
    )
  ) {
    return false;
  }
  return arraysEqual(value.evidenceRefs, decision.evidenceRefs);
}

export function isPersistedReportDraft(value: unknown): value is ReportDraft {
  if (!isRecord(value) || !hasExactFields(value, REPORT_FIELDS)) return false;
  const sections = value.sections;
  if (
    !isRecord(sections) ||
    !hasExactFields(sections, REPORT_SECTION_FIELDS) ||
    !REPORT_SECTION_FIELDS.every((field) =>
      isNonEmptyString(sections[field])
    )
  ) {
    return false;
  }
  if (
    value.profile !== "kfm.explorer.report-draft.v1" ||
    !isNonEmptyString(value.id) ||
    !isNonEmptyString(value.title) ||
    !isNonEmptyString(value.researchQuestion) ||
    !isIsoTimestamp(value.createdAt) ||
    value.lifecycle !== "DRAFT" ||
    value.publishable !== false ||
    !isPersistedMapSnapshot(value.snapshot) ||
    !isStringArray(value.includedEvidenceRefs)
  ) {
    return false;
  }
  return arraysEqual(value.includedEvidenceRefs, value.snapshot.evidenceRefs);
}

export function isPersistedStoryScene(value: unknown): value is StoryScene {
  if (!isRecord(value) || !hasExactFields(value, STORY_FIELDS)) return false;
  if (
    value.profile !== "kfm.explorer.story-scene.v1" ||
    !isNonEmptyString(value.id) ||
    !isNonEmptyString(value.title) ||
    !isNonEmptyString(value.narrative) ||
    !Number.isSafeInteger(value.order) ||
    (value.order as number) < 1 ||
    value.lifecycle !== "DRAFT" ||
    typeof value.motion !== "string" ||
    !STORY_MOTIONS.has(value.motion) ||
    !isPersistedMapSnapshot(value.snapshot) ||
    !isStringArray(value.evidenceRefs) ||
    !isStringArray(value.caveats)
  ) {
    return false;
  }
  return arraysEqual(value.evidenceRefs, value.snapshot.evidenceRefs);
}

export function parsePersistedDraftCollection<T>(
  raw: string | null,
  guard: DraftGuard<T>,
): readonly T[] | null {
  if (raw === null) return null;
  try {
    const value: unknown = JSON.parse(raw);
    if (!Array.isArray(value)) return Object.freeze([]);
    return Object.freeze(value.filter((entry): entry is T => guard(entry)));
  } catch {
    return Object.freeze([]);
  }
}

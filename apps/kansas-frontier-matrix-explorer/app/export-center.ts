import type { Geometry } from "geojson";
import type { EvidenceState, ReleaseState } from "./explorer-data";
import type { BasemapKey } from "./map-runtime";

export type ExportCheckState = "PASS" | "NOTICE" | "REDACTED" | "BLOCK";

export type ExportCheck = Readonly<{
  id: "identity" | "camera" | "selection" | "evidence" | "time" | "attribution" | "release" | "correction";
  label: string;
  state: ExportCheckState;
  detail: string;
}>;

export type ExportLayerInput = Readonly<{
  id: string;
  title: string;
  opacity: number;
  attribution: string;
  releaseState: ReleaseState;
  generalization: string;
  correction: string;
}>;

export type ExportSelectionInput = Readonly<{
  featureId: string;
  title: string;
  layerId: string;
  evidenceState: EvidenceState;
  evidenceReference: string;
  temporalScope: string;
  sourceYear: number;
  temporalMode: "exact" | "through" | "untimed";
  sourceTime: string;
  releaseTime: string;
  lastUpdate: string;
  reviewState: string;
  releaseState: ReleaseState;
  correctionState: string;
  geometry: Geometry;
  generalization: string;
}>;

export type PublicSafeExportInput = Readonly<{
  exportedAt: string;
  locationCameraRedacted: boolean;
  view: Readonly<{ center: readonly [number, number]; zoom: number; bearing: number; pitch: number }>;
  projection: "mercator" | "globe";
  basemap: BasemapKey;
  layerOrder: readonly string[];
  activeYear: number;
  workspace: "explore" | "knowledge" | "features" | "trust";
  layers: readonly ExportLayerInput[];
  selection: ExportSelectionInput | null;
}>;

const protectedSelection = (selection: ExportSelectionInput | null) =>
  Boolean(selection && ["DENIED_BY_POLICY", "RESTRICTED_ACCESS"].includes(selection.evidenceState));

export const buildPublicSafeExport = (input: PublicSafeExportInput) => {
  const isProtected = protectedSelection(input.selection);
  const hasAttribution = input.layers.every((layer) => layer.attribution.trim().length > 0);
  const evidenceClosed = Boolean(input.selection && ["ANSWER", "CORRECTED"].includes(input.selection.evidenceState));
  const correctionVisible = Boolean(input.selection && input.selection.correctionState !== "NONE");

  const checks: readonly ExportCheck[] = Object.freeze([
    Object.freeze({ id: "identity", label: "Artifact identity", state: "PASS", detail: "The export carries a stable format name, generation time, and site-local authority label." }),
    Object.freeze(input.locationCameraRedacted
      ? { id: "camera", label: "Camera privacy", state: "REDACTED", detail: "A browser-location-derived camera is replaced with an explicit withheld marker." }
      : { id: "camera", label: "Camera privacy", state: "PASS", detail: "The current camera is user-arranged map context, not a browser-location-derived position." }),
    Object.freeze(!input.selection
      ? { id: "selection", label: "Selection scope", state: "NOTICE", detail: "No feature is selected; the export contains the visible map context only." }
      : isProtected
        ? { id: "selection", label: "Selection scope", state: "REDACTED", detail: "Protected selection geometry is withheld while its public-safe reason class remains visible." }
        : { id: "selection", label: "Selection scope", state: "PASS", detail: "The selected site fixture may travel with its generalization and limitation fields." }),
    Object.freeze(!input.selection
      ? { id: "evidence", label: "Evidence closure", state: "NOTICE", detail: "No selection means no claim-bearing EvidenceRef is asserted by this export." }
      : evidenceClosed
        ? { id: "evidence", label: "Evidence closure", state: "PASS", detail: "The selected fixture carries its bounded demonstration EvidenceRef." }
        : { id: "evidence", label: "Evidence closure", state: "NOTICE", detail: `${input.selection.evidenceState} remains explicit; the export does not promote it into support.` }),
    Object.freeze({ id: "time", label: "Temporal disclosure", state: "PASS", detail: "Active time, feature/source year, query mode, source time, release time, and update time remain separate." }),
    Object.freeze(hasAttribution
      ? { id: "attribution", label: "Attribution", state: "PASS", detail: "Every visible layer includes its attribution string." }
      : { id: "attribution", label: "Attribution", state: "BLOCK", detail: "At least one visible layer lacks attribution; download must remain unavailable." }),
    Object.freeze({ id: "release", label: "Release posture", state: "NOTICE", detail: "The artifact is labeled SITE_LOCAL_DEMONSTRATION and does not claim KFM publication." }),
    Object.freeze(correctionVisible
      ? { id: "correction", label: "Correction lineage", state: "NOTICE", detail: `The selected record retains correction state ${input.selection?.correctionState}.` }
      : { id: "correction", label: "Correction lineage", state: "PASS", detail: "No selected correction marker is silently omitted." }),
  ]);

  const payload = {
    format: "kfm-public-safe-map-export-v2",
    authority: "SITE_LOCAL_DEMONSTRATION",
    exportedAt: input.exportedAt,
    publicEffect: "DOWNLOAD_ONLY",
    workspace: input.workspace,
    map: input.locationCameraRedacted
      ? { center: "WITHHELD_BROWSER_LOCATION", zoom: "WITHHELD", bearing: "WITHHELD", pitch: "WITHHELD", projection: input.projection, basemap: input.basemap, layerOrder: input.layerOrder }
      : { center: input.view.center, zoom: input.view.zoom, bearing: input.view.bearing, pitch: input.view.pitch, projection: input.projection, basemap: input.basemap, layerOrder: input.layerOrder },
    temporalQuery: {
      activeYear: input.activeYear,
      mode: input.selection?.temporalMode ?? "layer-specific",
      featureOrSourceYear: input.selection?.sourceYear ?? null,
      sourceTime: input.selection?.sourceTime ?? "SELECTION_NOT_PRESENT",
      releaseTime: input.selection?.releaseTime ?? "SELECTION_NOT_PRESENT",
      lastUpdate: input.selection?.lastUpdate ?? "SELECTION_NOT_PRESENT",
      geographyVersion: "site-local-generalized-v1",
      limitation: "Layer-specific temporal semantics remain authoritative for this demonstration view.",
    },
    layers: input.layers,
    selection: input.selection ? {
      featureId: input.selection.featureId,
      title: input.selection.title,
      layerId: input.selection.layerId,
      evidenceState: input.selection.evidenceState,
      evidenceReference: input.selection.evidenceReference,
      temporalScope: input.selection.temporalScope,
      reviewState: input.selection.reviewState,
      releaseState: input.selection.releaseState,
      correctionState: input.selection.correctionState,
      geometry: isProtected ? "WITHHELD_BY_POLICY" : input.selection.geometry,
      generalization: input.selection.generalization,
    } : null,
    trust: {
      checks: checks.map((check) => ({ id: check.id, state: check.state })),
      withheldFeatureCount: isProtected ? 1 : 0,
      rawCanonicalAccess: false,
      browserToModelCall: false,
      evidencePolicyReviewReleaseMutation: false,
    },
    limitations: [
      "This artifact describes site-local demonstration context, not a released KFM dataset.",
      "Map pixels, measurements, basemap labels, and browser state are not evidence or authority.",
      "The export does not admit a source, change policy or review state, release, deploy, promote, or publish anything.",
    ],
  };

  return Object.freeze({
    payload,
    checks,
    downloadAllowed: checks.every((check) => check.state !== "BLOCK"),
    withheldFeatureCount: isProtected ? 1 : 0,
    filename: `kfm-public-safe-view-${input.activeYear}.json`,
  });
};

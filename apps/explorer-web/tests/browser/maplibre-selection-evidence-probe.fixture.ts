import answerFixture from "../../../../fixtures/ui/evidence_drawer_payload/valid/answer-corrected.json";
import layerAdmissionFixture from "../../../../fixtures/runtime/layer_manifest_admission/cases.json";
import {
  MAP_FEATURE_SELECTION_PROFILE,
  type MapFeatureSelection,
} from "@kfm/maplibre";
import {
  createViteMapLibreAdapter,
  type MapLibreRenderedFeatureCandidate,
} from "@kfm/maplibre/vite-adapter";
import { mountEvidenceDrawer } from "../../src/features/evidence_drawer";
import { bindMapRuntimeEvidence } from "../../src/features/map_runtime/runtime-evidence-binding";

const RENDER_LAYER_ID = "synthetic-selection";
const RENDER_SOURCE_ID = "synthetic-selection-source";
const RELEASED_LAYER_ID = "layer:released:synthetic-streamflow";
const SELECTION_ID = "selection:maplibre:flow-001";
const FEATURE_ID = "feature:maplibre:flow-001";
const CURRENT_EVIDENCE = "kfm:evidence:synthetic:flow-001";
const HISTORY_EVIDENCE = "kfm:evidence:synthetic:flow-000";

const runtimeStatus = document.querySelector<HTMLElement>("#runtime-status");
const evidenceStatus = document.querySelector<HTMLElement>("#evidence-status");
const selectMapCenter = document.querySelector<HTMLButtonElement>(
  "#select-map-center",
);
const drawerHost = document.querySelector<HTMLElement>(
  "#evidence-drawer-host",
);
if (
  runtimeStatus === null ||
  evidenceStatus === null ||
  selectMapCenter === null ||
  drawerHost === null
) {
  throw new Error("MapLibre selection probe controls are missing.");
}

function projectSelection(
  candidate: MapLibreRenderedFeatureCandidate,
): MapFeatureSelection | null {
  document.body.dataset.renderedCandidate = JSON.stringify(candidate);
  if (
    candidate.layerId !== RENDER_LAYER_ID ||
    candidate.sourceId !== RENDER_SOURCE_ID ||
    candidate.featureId !== "flow-001" ||
    candidate.properties.fixture_key !== "flow-001"
  ) {
    return null;
  }
  return Object.freeze({
    profile: MAP_FEATURE_SELECTION_PROFILE,
    selectionId: SELECTION_ID,
    layerId: RELEASED_LAYER_ID,
    featureId: FEATURE_ID,
    evidenceRefs: Object.freeze([CURRENT_EVIDENCE]),
    historyEvidenceRefs: Object.freeze([HISTORY_EVIDENCE]),
  });
}

function admittedManifest(selection: MapFeatureSelection): unknown {
  const manifest = structuredClone(layerAdmissionFixture.base);
  manifest.layer_id = selection.layerId;
  manifest.runtime_request.layer_id = selection.layerId;
  return manifest;
}

const runtime = createViteMapLibreAdapter({
  containerId: "maplibre-selection-map",
  interactive: true,
  style: {
    version: 8,
    sources: {
      [RENDER_SOURCE_ID]: {
        type: "geojson",
        data: {
          type: "FeatureCollection",
          features: [
            {
              type: "Feature",
              id: "flow-001",
              properties: {
                fixture_key: "flow-001",
                trust_state: "SYNTHETIC",
              },
              geometry: {
                type: "Polygon",
                coordinates: [
                  [
                    [-110, 30],
                    [-90, 30],
                    [-90, 45],
                    [-110, 45],
                    [-110, 30],
                  ],
                ],
              },
            },
          ],
        },
      },
    },
    layers: [
      {
        id: "background",
        type: "background",
        paint: { "background-color": "#071517" },
      },
      {
        id: RENDER_LAYER_ID,
        type: "fill",
        source: RENDER_SOURCE_ID,
        paint: {
          "fill-color": "#4fd1c5",
          "fill-opacity": 0.35,
          "fill-outline-color": "#ffffff",
        },
      },
    ],
  },
  selectionProjection: {
    layerIds: [RENDER_LAYER_ID],
    project: projectSelection,
  },
});

runtime.subscribeSnapshot((snapshot) => {
  runtimeStatus.dataset.state = snapshot.state;
  runtimeStatus.dataset.reason = snapshot.reason ?? "NONE";
  runtimeStatus.textContent =
    `State ${snapshot.state}; reason ${snapshot.reason ?? "NONE"}`;
});

selectMapCenter.addEventListener("click", () => {
  runtime.selectAtPoint({ x: 320, y: 180 });
});

const binding = bindMapRuntimeEvidence(
  runtime,
  admittedManifest,
  async () => answerFixture,
  (update) => {
    if (update.kind !== "EVIDENCE_RESOLVED") return;
    const resolution = update.resolution;
    const selection = resolution.evidence.selection;
    document.body.dataset.selectionId = selection?.selectionId ?? "MISSING";
    document.body.dataset.layerAdmission =
      resolution.layerAdmission?.outcome ?? "MISSING";
    evidenceStatus.dataset.state = resolution.evidence.drawer.outcome;
    evidenceStatus.dataset.code = resolution.evidence.code;
    evidenceStatus.textContent =
      `${resolution.evidence.drawer.outcome} / ${resolution.evidence.code}`;
    const drawer = mountEvidenceDrawer(
      drawerHost,
      resolution.evidence.drawerInput,
    );
    drawer.open();
  },
);

void runtime.initialize().then(
  () => {
    document.body.dataset.initialization = "resolved";
  },
  () => {
    document.body.dataset.initialization = "rejected";
  },
);

window.addEventListener(
  "pagehide",
  () => {
    binding.destroy();
    runtime.dispose();
  },
  { once: true },
);

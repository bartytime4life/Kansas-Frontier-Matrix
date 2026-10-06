import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import ts from "typescript";
import { hasSafeQwenContextShape } from "../app/qwen-context-safety.mjs";
import {
  QWEN_LOCAL_MAX_OFFICIAL_SOURCES,
  QWEN_LOCAL_MAX_REQUEST_BYTES,
  hasRequiredLocalQwenContext,
  inspectLocalQwenEvidence,
} from "../scripts/qwen-local-contract.mjs";

const modules = new Map();
async function moduleUrl(file) {
  const resolved = path.resolve(file);
  if (modules.has(resolved)) return modules.get(resolved);
  let javascript = ts.transpileModule(await readFile(resolved, "utf8"), {
    compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
  }).outputText;
  for (const match of [...javascript.matchAll(/from ["'](\.[^"']+)["']/g)]) {
    javascript = javascript.replace(
      match[0],
      `from ${JSON.stringify(await moduleUrl(path.resolve(path.dirname(resolved), match[1]) + ".ts"))}`,
    );
  }
  const url = `data:text/javascript;base64,${Buffer.from(javascript).toString("base64")}`;
  modules.set(resolved, url);
  return url;
}

const liveContext = await import(await moduleUrl("app/live-context.ts"));
const explorerData = await import(await moduleUrl("app/explorer-data.ts"));

const soilMoisture = Object.freeze({
  enabled: true,
  availabilityState: "ready",
  mapState: "blending",
  selectedView: "surface",
  selectedDepthCm: [0, 5],
  selectedUtcDay: "2026-10-05",
  selectedFrameTimeUtc: "2026-10-05T00:00:00Z",
  renderedFrameTimeUtc: "2026-10-04T00:00:00Z",
  renderedAtUtc: "2026-10-06T01:00:00Z",
  retainedFrameTimeUtc: null,
  visualTransition: {
    fromFrameTimeUtc: "2026-10-04T00:00:00Z",
    toFrameTimeUtc: "2026-10-05T00:00:00Z",
    fraction: 0.5,
    kind: "adjacent-frame-blend",
    numericInterpolation: false,
  },
  displaySmoothing: "visual blend and bilinear color resampling",
  playing: false,
  rangeStartUtcDay: "2026-09-22",
  rangeEndUtcDay: "2026-10-05",
  rangeFrameCount: 14,
  availableFrameCount: 14,
  latestAvailableUtcDay: "2026-10-05",
  sourceCheckedAtUtc: "2026-10-06T01:00:00Z",
  product: "NASA-USDA SMAP",
  version: "test fixture",
  displayCadence: "daily",
  nativeCadence: "subdaily composite",
  nativeFormat: "PNG display tiles",
  approximateResolutionKm: 9,
  coverageBoundsWgs84: [-180, -85, 180, 85],
  evidenceRole: "EXTERNAL_CONTEXT_ONLY",
  dataKind: "COLORIZED_IMAGE_CONTEXT",
  numericPixelsAvailable: false,
  qualityNotice: null,
  sourceUrl: "https://earthdata.nasa.gov/",
  productGuideUrl: "https://nsidc.org/data/spl3smp_e/versions/6",
});

test("the real 48-source empty-registry browser envelope stays below the shared request cap", () => {
  assert.equal(liveContext.OFFICIAL_CONTEXT_SOURCES.length, QWEN_LOCAL_MAX_OFFICIAL_SOURCES);
  assert.equal(explorerData.LAYER_REGISTRY.length, 0);

  const realContext = {
    camera: { center: [-98, 38.5], locationRedacted: true, zoom: 5, bearing: 0, pitch: 0, projection: "mercator", representation: "2D map" },
    basemap: { key: "standard", title: "Standard vector context", note: "Reference context only" },
    time: { value: 2026, label: "2026", era: "Present · snapshot" },
    visibleLayers: explorerData.LAYER_REGISTRY.slice(0, 14).map((layer) => ({
      id: layer.id,
      title: layer.title,
      domain: layer.domain,
      sourceType: layer.sourceType,
      releaseState: layer.releaseState,
      publicStatus: layer.publicStatus,
      freshnessState: layer.freshnessState,
      evidenceReference: layer.evidenceReference,
    })),
    officialSources: liveContext.OFFICIAL_CONTEXT_SOURCES.map((source) => ({
      id: source.id,
      title: source.shortTitle,
      selected: source.defaultVisibility,
      displayed: false,
      state: "idle",
      featureCount: null,
      retrievedAt: null,
      evidenceRole: "EXTERNAL_CONTEXT_ONLY",
    })),
    telemetry: {
      authority: "SITE_LOCAL_REDACTED_DIAGNOSTIC",
      renderer: { state: "ready", styleLoaded: true, canvasReady: true, tilesLoaded: true, failedChecks: [] },
      registry: { total: explorerData.LAYER_REGISTRY.length, ready: 0, loading: 0, error: 0 },
      radar: { state: "idle", frameTime: null, manifestFresh: false },
      streamflow: { state: "idle", frameTime: null },
    },
    selection: null,
    nearbyContext: [],
  };
  const body = JSON.stringify({ question: "What should I notice in this map view?", context: realContext });
  const bodyBytes = Buffer.byteLength(body);
  assert.equal(hasSafeQwenContextShape(realContext), true);
  assert.equal(hasRequiredLocalQwenContext(realContext), true);
  assert.equal(inspectLocalQwenEvidence(realContext).disposition, "context-only");
  assert.ok(bodyBytes > QWEN_LOCAL_MAX_OFFICIAL_SOURCES * 100,
    "the fixture must include the current complete official-source serialization");
  assert.ok(bodyBytes < QWEN_LOCAL_MAX_REQUEST_BYTES);
});

test("non-null soil transitions require the complete bounded transition contract", () => {
  const base = {
    camera: { center: [-98, 38.5], locationRedacted: true, zoom: 5, bearing: 0, pitch: 0, projection: "mercator", representation: "2D map" },
    basemap: { key: "standard", title: "Standard vector context", note: "Reference context only" },
    time: { value: 2026, label: "2026", era: "Present · snapshot" },
    visibleLayers: [],
    officialSources: [],
    telemetry: {
      authority: "SITE_LOCAL_REDACTED_DIAGNOSTIC",
      renderer: { state: "ready", styleLoaded: true, canvasReady: true, tilesLoaded: true, failedChecks: [] },
      registry: { total: 0, ready: 0, loading: 0, error: 0 },
      radar: { state: "idle", frameTime: null, manifestFresh: false },
      streamflow: { state: "idle", frameTime: null },
    },
    soilMoisture,
    selection: null,
    nearbyContext: [],
  };
  assert.equal(hasSafeQwenContextShape(base), true);
  assert.equal(hasRequiredLocalQwenContext(base), true);
  for (const field of ["fromFrameTimeUtc", "toFrameTimeUtc", "fraction", "kind", "numericInterpolation"]) {
    const visualTransition = { ...soilMoisture.visualTransition };
    delete visualTransition[field];
    const candidate = { ...base, soilMoisture: { ...soilMoisture, visualTransition } };
    assert.equal(hasSafeQwenContextShape(candidate), false, `safe shape missing ${field}`);
    assert.equal(hasRequiredLocalQwenContext(candidate), false, `required shape missing ${field}`);
  }
});

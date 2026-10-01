/** Reject undeclared context fields before they can reach a configured model. */
const record = (value) => value !== null && typeof value === "object" && !Array.isArray(value);
const string = (value) => typeof value === "string" && value.length <= 2048;
const number = (value) => typeof value === "number" && Number.isFinite(value);
const boolean = (value) => typeof value === "boolean";
const nullable = (check) => (value) => value === null || check(value);
const array = (check, max) => (value) => Array.isArray(value) && value.length <= max && value.every(check);
const tuple = (size) => (value) => Array.isArray(value) && value.length === size && value.every(number);
const shape = (fields) => (value) => record(value) && Object.keys(value).every(
  (key) => Object.hasOwn(fields, key) && fields[key](value[key]),
);

const camera = shape({
  center: tuple(2), locationRedacted: boolean, zoom: number, bearing: number,
  pitch: number, projection: string, representation: string,
});
const basemap = shape({ key: string, title: string, note: string });
const time = shape({ value: number, label: string, era: string });
const layer = shape({
  id: string, title: string, domain: string, sourceType: string,
  releaseState: string, publicStatus: string, freshnessState: string,
});
const officialSource = shape({
  id: string, title: string, selected: boolean, displayed: boolean,
  state: string, featureCount: nullable(number), retrievedAt: nullable(string),
  evidenceRole: (value) => value === "EXTERNAL_CONTEXT_ONLY",
});
const visualTransition = shape({
  fromFrameTimeUtc: string, toFrameTimeUtc: string, fraction: number,
  kind: string, numericInterpolation: (value) => value === false,
});
const soilMoisture = shape({
  enabled: boolean, availabilityState: string, mapState: string,
  selectedView: string, selectedDepthCm: tuple(2),
  selectedUtcDay: nullable(string), selectedFrameTimeUtc: nullable(string),
  renderedFrameTimeUtc: nullable(string), renderedAtUtc: nullable(string),
  retainedFrameTimeUtc: nullable(string), visualTransition: nullable(visualTransition),
  displaySmoothing: string, playing: boolean,
  rangeStartUtcDay: nullable(string), rangeEndUtcDay: nullable(string),
  rangeFrameCount: number, availableFrameCount: number,
  latestAvailableUtcDay: nullable(string), sourceCheckedAtUtc: nullable(string),
  product: string, version: string, displayCadence: string, nativeCadence: string,
  nativeFormat: string, approximateResolutionKm: number,
  coverageBoundsWgs84: tuple(4), evidenceRole: string, dataKind: string,
  numericPixelsAvailable: (value) => value === false,
  qualityNotice: nullable(string), sourceUrl: string, productGuideUrl: string,
});
const telemetry = shape({
  authority: (value) => value === "SITE_LOCAL_REDACTED_DIAGNOSTIC",
  renderer: shape({
    state: string, styleLoaded: boolean, canvasReady: boolean,
    tilesLoaded: boolean, failedChecks: array(string, 32),
  }),
  registry: shape({ total: number, ready: number, loading: number, error: number }),
  radar: shape({ state: string, frameTime: nullable(string), manifestFresh: boolean }),
  streamflow: shape({ state: string, frameTime: nullable(string) }),
});
const selection = shape({
  featureId: string, title: string, layerId: string, layerTitle: string,
  domain: string, evidenceState: string, evidenceReference: string,
  sourceYear: number, spatialScope: string, summary: string,
});
const nearby = shape({
  title: string, layerTitle: string, distanceMiles: number, evidenceState: string,
});

export const hasSafeQwenContextShape = shape({
  camera, basemap, time, visibleLayers: array(layer, 14),
  officialSources: array(officialSource, 32), soilMoisture: nullable(soilMoisture),
  telemetry, selection: nullable(selection), nearbyContext: array(nearby, 8),
});

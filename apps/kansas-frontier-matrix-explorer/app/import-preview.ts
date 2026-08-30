import type { Feature, FeatureCollection, GeoJsonProperties, Geometry, Position } from "geojson";

export const IMPORT_PREVIEW_MAX_BYTES = 2 * 1024 * 1024;

export type ImportSourceFormat = "GEOJSON" | "KML";
export type ImportCheckState = "PASS" | "WARN" | "BLOCK";
export type ImportCoverage = "WITHIN_KANSAS_CONTEXT" | "PARTIAL_KANSAS_CONTEXT" | "OUTSIDE_KANSAS_CONTEXT" | "NO_GEOMETRY";

export type ImportPreviewCheck = Readonly<{
  id: string;
  label: string;
  state: ImportCheckState;
  detail: string;
}>;

export type LocalImportPreview = Readonly<{
  format: "kfm-browser-import-preview-v1";
  authority: "UNADMITTED_BROWSER_PREVIEW";
  publicEffect: "NONE";
  fileName: string;
  fileSizeBytes: number;
  sourceFormat: ImportSourceFormat;
  inspectedAt: string;
  featureCount: number;
  invalidFeatureCount: number;
  unsupportedElementCount: number;
  externalReferenceCount: number;
  geometryCounts: Readonly<Record<string, number>>;
  bounds: readonly [number, number, number, number] | null;
  coverage: ImportCoverage;
  propertyKeys: readonly string[];
  temporalFields: readonly string[];
  sensitivitySignals: readonly string[];
  attribution: string | null;
  renderAllowed: boolean;
  featureCollection: FeatureCollection;
  checks: readonly ImportPreviewCheck[];
}>;

type SupportedBounds = Readonly<{ west: number; south: number; east: number; north: number }>;

const temporalFieldPattern = /(^|_)(date|time|year|start|end|valid|observed|effective|updated|timestamp)(_|$)/i;
const sensitivityFieldPattern = /(^|_)(address|owner|phone|email|parcel|well|species|site|tribe|burial|archaeolog|protected|sensitive)(_|$)/i;
const supportedGeometryTypes = new Set(["Point", "MultiPoint", "LineString", "MultiLineString", "Polygon", "MultiPolygon", "GeometryCollection"]);

const localName = (element: Element) => element.localName || element.tagName.split(":").at(-1) || element.tagName;
const descendants = (element: ParentNode, name: string) => Array.from(element.querySelectorAll("*")).filter((candidate) => localName(candidate) === name);
const firstDescendant = (element: ParentNode, name: string) => descendants(element, name)[0];
const textOf = (element: ParentNode, name: string) => firstDescendant(element, name)?.textContent?.trim() ?? "";

const sanitizeProperties = (value: unknown): GeoJsonProperties => {
  if (!value || typeof value !== "object" || Array.isArray(value)) return {};
  return Object.fromEntries(Object.entries(value as Record<string, unknown>).map(([key, entry]) => {
    if (entry === null || typeof entry === "string" || typeof entry === "number" || typeof entry === "boolean") return [key, entry];
    try { return [key, JSON.stringify(entry).slice(0, 2_000)]; } catch { return [key, String(entry).slice(0, 2_000)]; }
  }));
};

const positionsForGeometry = (geometry: Geometry): Position[] => {
  if (geometry.type === "GeometryCollection") return geometry.geometries.flatMap(positionsForGeometry);
  const positions: Position[] = [];
  const visit = (value: unknown) => {
    if (!Array.isArray(value)) return;
    if (value.length >= 2 && typeof value[0] === "number" && typeof value[1] === "number") {
      positions.push(value as Position);
      return;
    }
    for (const entry of value) visit(entry);
  };
  visit(geometry.coordinates);
  return positions;
};

const geometryIsValid = (value: unknown): value is Geometry => {
  if (!value || typeof value !== "object") return false;
  const geometry = value as Geometry;
  if (!supportedGeometryTypes.has(geometry.type)) return false;
  if (geometry.type === "GeometryCollection") return Array.isArray(geometry.geometries) && geometry.geometries.every(geometryIsValid);
  const positions = positionsForGeometry(geometry);
  if (!positions.length) return false;
  return positions.every((position) => Number.isFinite(position[0]) && Number.isFinite(position[1]) && position[0] >= -180 && position[0] <= 180 && position[1] >= -90 && position[1] <= 90);
};

const normalizeGeoJson = (raw: unknown) => {
  const object = raw as { type?: string; features?: unknown[]; geometry?: unknown; properties?: unknown; id?: string | number; attribution?: unknown; metadata?: { attribution?: unknown } };
  const candidates = object?.type === "FeatureCollection" && Array.isArray(object.features)
    ? object.features
    : object?.type === "Feature"
      ? [object]
      : supportedGeometryTypes.has(object?.type ?? "")
        ? [{ type: "Feature", properties: {}, geometry: object }]
        : [];
  if (!candidates.length) throw new Error("The file is not a GeoJSON FeatureCollection, Feature, or supported Geometry.");

  let invalidFeatureCount = 0;
  const features: Feature[] = [];
  for (const [index, candidate] of candidates.entries()) {
    const feature = candidate as { type?: string; geometry?: unknown; properties?: unknown; id?: string | number };
    if (feature?.type !== "Feature" || !geometryIsValid(feature.geometry)) {
      invalidFeatureCount += 1;
      continue;
    }
    features.push({
      type: "Feature",
      id: typeof feature.id === "string" || typeof feature.id === "number" ? feature.id : `local-import-${index + 1}`,
      properties: sanitizeProperties(feature.properties),
      geometry: feature.geometry,
    });
  }
  const attribution = typeof object.attribution === "string"
    ? object.attribution.trim()
    : typeof object.metadata?.attribution === "string" ? object.metadata.attribution.trim() : "";
  return { features, invalidFeatureCount, unsupportedElementCount: 0, attribution: attribution || null };
};

const parseKmlCoordinates = (value: string): Position[] => value
  .trim()
  .split(/\s+/)
  .map((token) => token.split(",").map(Number))
  .filter((position) => position.length >= 2 && Number.isFinite(position[0]) && Number.isFinite(position[1]))
  .map((position) => position.slice(0, 3));

const geometryFromKmlElement = (element: Element): Geometry | null => {
  const kind = localName(element);
  if (kind === "Point") {
    const coordinate = parseKmlCoordinates(textOf(element, "coordinates"))[0];
    return coordinate ? { type: "Point", coordinates: coordinate } : null;
  }
  if (kind === "LineString") {
    const coordinates = parseKmlCoordinates(textOf(element, "coordinates"));
    return coordinates.length >= 2 ? { type: "LineString", coordinates } : null;
  }
  if (kind === "Polygon") {
    const outer = firstDescendant(element, "outerBoundaryIs");
    const outerRing = outer ? parseKmlCoordinates(textOf(outer, "coordinates")) : [];
    if (outerRing.length < 3) return null;
    const closedOuter = outerRing[0][0] === outerRing.at(-1)?.[0] && outerRing[0][1] === outerRing.at(-1)?.[1] ? outerRing : [...outerRing, outerRing[0]];
    const innerRings = descendants(element, "innerBoundaryIs").map((boundary) => parseKmlCoordinates(textOf(boundary, "coordinates"))).filter((ring) => ring.length >= 3).map((ring) => (
      ring[0][0] === ring.at(-1)?.[0] && ring[0][1] === ring.at(-1)?.[1] ? ring : [...ring, ring[0]]
    ));
    return { type: "Polygon", coordinates: [closedOuter, ...innerRings] };
  }
  return null;
};

const extendedDataForPlacemark = (placemark: Element) => Object.fromEntries(descendants(placemark, "Data").map((data) => {
  const key = data.getAttribute("name")?.trim() ?? "";
  return [key, textOf(data, "value")];
}).filter(([key]) => key));

const normalizeKml = (text: string) => {
  if (typeof DOMParser === "undefined") throw new Error("KML inspection is unavailable in this browser runtime.");
  const document = new DOMParser().parseFromString(text, "application/xml");
  if (descendants(document, "parsererror").length) throw new Error("The KML document is not well-formed XML.");
  const placemarks = descendants(document, "Placemark");
  let invalidFeatureCount = 0;
  const features: Feature[] = [];
  placemarks.forEach((placemark, index) => {
    const geometryElements = descendants(placemark, "Point").concat(descendants(placemark, "LineString"), descendants(placemark, "Polygon"));
    const geometries = geometryElements.map(geometryFromKmlElement).filter((geometry): geometry is Geometry => Boolean(geometry && geometryIsValid(geometry)));
    if (!geometries.length) {
      invalidFeatureCount += 1;
      return;
    }
    const extendedData = extendedDataForPlacemark(placemark);
    const timestamp = textOf(placemark, "when");
    const start = textOf(placemark, "begin");
    const end = textOf(placemark, "end");
    features.push({
      type: "Feature",
      id: `kml-placemark-${index + 1}`,
      properties: sanitizeProperties({
        name: textOf(placemark, "name") || `Placemark ${index + 1}`,
        description: textOf(placemark, "description"),
        ...(timestamp ? { timestamp } : {}),
        ...(start ? { start } : {}),
        ...(end ? { end } : {}),
        ...extendedData,
      }),
      geometry: geometries.length === 1 ? geometries[0] : { type: "GeometryCollection", geometries },
    });
  });
  const unsupportedElementCount = ["NetworkLink", "GroundOverlay", "PhotoOverlay", "Model", "Track", "MultiTrack"]
    .reduce((count, name) => count + descendants(document, name).length, 0);
  const author = firstDescendant(document, "author");
  const extendedAttribution = descendants(document, "Data").find((data) => data.getAttribute("name")?.toLowerCase() === "attribution");
  const attribution = (author ? textOf(author, "name") : "") || (extendedAttribution ? textOf(extendedAttribution, "value") : "");
  return { features, invalidFeatureCount, unsupportedElementCount, attribution: attribution || null };
};

const geometryCountsFor = (features: Feature[]) => {
  const counts: Record<string, number> = {};
  const count = (geometry: Geometry) => {
    if (geometry.type === "GeometryCollection") {
      geometry.geometries.forEach(count);
      return;
    }
    counts[geometry.type] = (counts[geometry.type] ?? 0) + 1;
  };
  features.forEach((feature) => feature.geometry && count(feature.geometry));
  return Object.freeze(Object.fromEntries(Object.entries(counts).sort(([left], [right]) => left.localeCompare(right))));
};

const boundsFor = (features: Feature[]): readonly [number, number, number, number] | null => {
  const positions = features.flatMap((feature) => feature.geometry ? positionsForGeometry(feature.geometry) : []);
  if (!positions.length) return null;
  return Object.freeze([
    Math.min(...positions.map((position) => position[0])),
    Math.min(...positions.map((position) => position[1])),
    Math.max(...positions.map((position) => position[0])),
    Math.max(...positions.map((position) => position[1])),
  ] as const);
};

const coverageFor = (bounds: readonly [number, number, number, number] | null, supported: SupportedBounds): ImportCoverage => {
  if (!bounds) return "NO_GEOMETRY";
  const [west, south, east, north] = bounds;
  if (east < supported.west || west > supported.east || north < supported.south || south > supported.north) return "OUTSIDE_KANSAS_CONTEXT";
  if (west >= supported.west && east <= supported.east && south >= supported.south && north <= supported.north) return "WITHIN_KANSAS_CONTEXT";
  return "PARTIAL_KANSAS_CONTEXT";
};

const countExternalReferences = (text: string) => (text.match(/https?:\/\/[^\s"'<>]+/gi) ?? []).length;

export const buildLocalImportPreview = (input: Readonly<{
  fileName: string;
  fileSizeBytes: number;
  text: string;
  inspectedAt: string;
  supportedBounds: SupportedBounds;
}>): LocalImportPreview => {
  if (input.fileSizeBytes > IMPORT_PREVIEW_MAX_BYTES) throw new Error("The preview is limited to files no larger than 2 MB.");
  const trimmed = input.text.trim();
  if (!trimmed) throw new Error("The selected file is empty.");
  const looksLikeKml = /\.kml$/i.test(input.fileName) || /^<\?xml|^<kml[\s>]/i.test(trimmed);
  const sourceFormat: ImportSourceFormat = looksLikeKml ? "KML" : "GEOJSON";
  let normalized: ReturnType<typeof normalizeGeoJson>;
  if (sourceFormat === "KML") normalized = normalizeKml(trimmed);
  else {
    let raw: unknown;
    try { raw = JSON.parse(trimmed); } catch { throw new Error("The GeoJSON file is not valid JSON."); }
    normalized = normalizeGeoJson(raw);
  }

  const featureCollection: FeatureCollection = { type: "FeatureCollection", features: normalized.features };
  const propertyKeys = [...new Set(normalized.features.flatMap((feature) => Object.keys(feature.properties ?? {})))].sort();
  const temporalFields = propertyKeys.filter((key) => temporalFieldPattern.test(key));
  const sensitivitySignals = propertyKeys.filter((key) => sensitivityFieldPattern.test(key));
  const bounds = boundsFor(normalized.features);
  const coverage = coverageFor(bounds, input.supportedBounds);
  const externalReferenceCount = countExternalReferences(trimmed);
  const renderAllowed = normalized.features.length > 0 && coverage !== "OUTSIDE_KANSAS_CONTEXT";
  const checks: ImportPreviewCheck[] = [
    { id: "format", label: "Readable structure", state: "PASS", detail: `${sourceFormat} parsed locally without uploading the file.` },
    { id: "geometry", label: "Renderable geometry", state: normalized.features.length ? normalized.invalidFeatureCount ? "WARN" : "PASS" : "BLOCK", detail: normalized.features.length ? `${normalized.features.length} preview feature${normalized.features.length === 1 ? "" : "s"}; ${normalized.invalidFeatureCount} invalid or empty.` : "No supported point, line, or polygon geometry was found." },
    { id: "context", label: "Kansas context", state: coverage === "OUTSIDE_KANSAS_CONTEXT" || coverage === "NO_GEOMETRY" ? "BLOCK" : coverage === "PARTIAL_KANSAS_CONTEXT" ? "WARN" : "PASS", detail: coverage.replaceAll("_", " ").toLowerCase() },
    { id: "attribution", label: "Attribution", state: normalized.attribution ? "PASS" : "WARN", detail: normalized.attribution ?? "No explicit author or attribution field was found." },
    { id: "external", label: "External references", state: externalReferenceCount || normalized.unsupportedElementCount ? "WARN" : "PASS", detail: `${externalReferenceCount} URL reference${externalReferenceCount === 1 ? "" : "s"}; ${normalized.unsupportedElementCount} unsupported network, overlay, model, or track element${normalized.unsupportedElementCount === 1 ? "" : "s"}. None are fetched.` },
    { id: "sensitivity", label: "Sensitivity signals", state: sensitivitySignals.length ? "WARN" : "PASS", detail: sensitivitySignals.length ? `Review fields before any admission handoff: ${sensitivitySignals.join(", ")}.` : "No obvious sensitivity-key signal was detected; this is not a policy clearance." },
  ];

  return Object.freeze({
    format: "kfm-browser-import-preview-v1",
    authority: "UNADMITTED_BROWSER_PREVIEW",
    publicEffect: "NONE",
    fileName: input.fileName,
    fileSizeBytes: input.fileSizeBytes,
    sourceFormat,
    inspectedAt: input.inspectedAt,
    featureCount: normalized.features.length,
    invalidFeatureCount: normalized.invalidFeatureCount,
    unsupportedElementCount: normalized.unsupportedElementCount,
    externalReferenceCount,
    geometryCounts: geometryCountsFor(normalized.features),
    bounds,
    coverage,
    propertyKeys: Object.freeze(propertyKeys),
    temporalFields: Object.freeze(temporalFields),
    sensitivitySignals: Object.freeze(sensitivitySignals),
    attribution: normalized.attribution,
    renderAllowed,
    featureCollection,
    checks: Object.freeze(checks.map((check) => Object.freeze({ ...check }))),
  });
};

export const importPreviewAudit = (preview: LocalImportPreview) => Object.freeze({
  format: preview.format,
  authority: preview.authority,
  publicEffect: preview.publicEffect,
  file: { name: preview.fileName, sizeBytes: preview.fileSizeBytes, sourceFormat: preview.sourceFormat },
  inspectedAt: preview.inspectedAt,
  featureCount: preview.featureCount,
  invalidFeatureCount: preview.invalidFeatureCount,
  geometryCounts: preview.geometryCounts,
  bounds: preview.bounds,
  coverage: preview.coverage,
  attribution: preview.attribution,
  temporalFields: preview.temporalFields,
  sensitivitySignals: preview.sensitivitySignals,
  externalReferenceCount: preview.externalReferenceCount,
  unsupportedElementCount: preview.unsupportedElementCount,
  checks: preview.checks,
  effects: "NO_UPLOAD_NO_SAVE_NO_SOURCE_ADMISSION_NO_REPORT_DATA_NO_PUBLICATION",
});

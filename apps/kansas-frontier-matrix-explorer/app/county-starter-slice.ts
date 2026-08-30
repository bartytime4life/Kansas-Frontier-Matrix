import type { FeatureCollection, Point } from "geojson";

import countyStarterSource from "./county-starter-points.json";
import type { FeatureProperties, LayerRecord } from "./explorer-data";

type CountyStarterRow = Readonly<{
  geoid: string;
  name: string;
  latitude: number;
  longitude: number;
}>;

type CountyStarterProperties = FeatureProperties & Readonly<{
  countyGeoid: string;
  countyName: string;
  countyLabel: string;
  starterKind: "COUNTY_INTERNAL_POINT";
}>;

type CountyStarterSource = Readonly<{
  schemaVersion: string;
  source: Readonly<{
    title: string;
    publisher: string;
    year: number;
    coordinateMeaning: string;
    referenceUrl: string;
    retrievedAt: string;
  }>;
  counties: readonly CountyStarterRow[];
}>;

const source = countyStarterSource as CountyStarterSource;

export const COUNTY_STARTER_LAYER_ID = "county-starter-points";
export const COUNTY_STARTER_FEATURE_COUNT = source.counties.length;
export const COUNTY_STARTER_SOURCE = Object.freeze({ ...source.source });

const countyStarterData: FeatureCollection<Point, CountyStarterProperties> = {
  type: "FeatureCollection",
  features: source.counties.map((county) => ({
    type: "Feature" as const,
    id: `county-${county.geoid}`,
    geometry: {
      type: "Point" as const,
      coordinates: [county.longitude, county.latitude],
    },
    properties: {
      fid: `county-${county.geoid}`,
      title: `${county.name} starter`,
      summary: "One public-safe county locator used as the starting point for future governed county slices.",
      sourceRole: "reference locator",
      sourceOrganization: source.source.publisher,
      citation: `${source.source.title} · GEOID ${county.geoid}`,
      spatialScope: `${county.name}, Kansas · representative internal point`,
      temporalScope: `${source.source.year} Gazetteer geography reference`,
      lastUpdate: String(source.source.year),
      freshnessState: "NOT_APPLICABLE",
      evidenceState: "GENERALIZED_GEOMETRY",
      reviewState: "SOURCE-REFERENCED DEMONSTRATION",
      releaseState: "DEMONSTRATION",
      rights: "U.S. Census Bureau public data embedded as a site-local reference fixture; not an admitted KFM release.",
      generalizationNote: "Representative internal point only; not a county boundary, centroid, address, county seat, parcel location, or jurisdictional determination.",
      uncertainty: "The point locates the county generally and does not describe county shape, conditions, or any county-level claim.",
      correctionState: "NONE",
      relatedLayers: "Kansas demonstration extent; Communities",
      year: source.source.year,
      focusLng: county.longitude,
      focusLat: county.latitude,
      countyGeoid: county.geoid,
      countyName: county.name,
      countyLabel: county.name.replace(/ County$/, ""),
      starterKind: "COUNTY_INTERNAL_POINT",
    },
  })),
};

export const COUNTY_STARTER_LAYER: LayerRecord = {
  id: COUNTY_STARTER_LAYER_ID,
  title: "County starter points",
  description: `One representative internal point for each of Kansas's ${COUNTY_STARTER_FEATURE_COUNT} counties, ready for search, selection, evidence inspection, and report scoping.`,
  domain: "Boundaries",
  category: "Boundaries & places",
  sourceType: "GeoJSON",
  sourceId: "kfm-county-starters",
  datasetName: "2025 Census Gazetteer Kansas county internal points · site-local starter slice",
  geometryType: "Point",
  minZoom: 4,
  maxZoom: 16,
  defaultVisibility: true,
  defaultOpacity: 0.78,
  legend: [{ label: "County starter locator", color: "#f4d06f", shape: "point" }],
  units: "representative internal point",
  scaleNote: "Statewide locator points; county labels begin at zoom 7.5",
  validTimeExtent: "2025 reference geography",
  sourceTime: "2025 U.S. Gazetteer Files",
  releaseTime: "Demonstration build 2026-08-30",
  freshnessState: "NOT_APPLICABLE",
  attribution: "U.S. Census Bureau · 2025 Gazetteer Files",
  evidenceReference: "Per-feature Census GEOID and citation; no claim-bearing county EvidenceBundle is asserted.",
  publicStatus: "PUBLIC_SAFE",
  sensitivityNote: "Public county names and representative internal points only.",
  releaseState: "DEMONSTRATION",
  correctionNote: "Promote or replace only through an admitted county source manifest, validator, release receipt, and correction path.",
  relatedLayers: ["Kansas demonstration extent", "Communities"],
  interactions: ["hover", "select", "search", "zoom", "evidence", "report"],
  filters: ["county name", "Census GEOID"],
  viewingModes: ["2D", "globe", "pitched"],
  bounds: [-102.06, 36.99, -94.75, 40.01],
  data: countyStarterData,
  renderers: [
    {
      id: "county-starter-points-circle",
      interactive: true,
      opacityProperties: ["circle-opacity"],
      spec: {
        id: "county-starter-points-circle",
        type: "circle",
        source: "kfm-county-starters",
        minzoom: 4,
        maxzoom: 16,
        paint: {
          "circle-color": ["case", ["boolean", ["feature-state", "hover"], false], "#fff4ce", "#f4d06f"],
          "circle-radius": ["interpolate", ["linear"], ["zoom"], 4, 2.25, 7, 4, 10, 5.5],
          "circle-opacity": 0.78,
          "circle-stroke-color": "#142b2f",
          "circle-stroke-width": 1,
        },
      },
    },
    {
      id: "county-starter-points-label",
      opacityProperties: ["text-opacity"],
      spec: {
        id: "county-starter-points-label",
        type: "symbol",
        source: "kfm-county-starters",
        minzoom: 7.5,
        maxzoom: 16,
        layout: {
          "text-field": ["get", "countyLabel"],
          "text-size": 10,
          "text-offset": [0, 1.05],
          "text-anchor": "top",
          "text-allow-overlap": false,
          "text-ignore-placement": false,
        },
        paint: {
          "text-color": "#f7edcf",
          "text-halo-color": "#07171a",
          "text-halo-width": 1.4,
          "text-opacity": 0.88,
        },
      },
    },
  ],
};

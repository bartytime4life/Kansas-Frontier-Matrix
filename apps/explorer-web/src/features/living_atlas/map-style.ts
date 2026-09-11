import type { MapLibreSafeStyle } from "@kfm/maplibre/vite-adapter";

import { isLayerTemporallyCompatible, LAYER_RECORDS } from "./registry";
import type { MapLayerState, MapRepresentation } from "./types";

type Position = [number, number];

const kansasRing: Position[] = [
  [-102.05, 40.0],
  [-94.61, 40.0],
  [-94.61, 37.0],
  [-102.05, 37.0],
  [-102.05, 40.0],
];

const domainPoints = LAYER_RECORDS.filter(
  (record) =>
    record.representation === "MAPLIBRE_INLINE" &&
    record.geometryType === "POINT",
).map((record, index) => ({
  type: "Feature" as const,
  id: record.id,
  properties: {
    layer_id: record.id,
    domain: record.domain,
    trust_state: record.trustState,
    fixture: true,
  },
  geometry: {
    type: "Point" as const,
    coordinates: [
      -101.35 + (index % 5) * 1.48,
      37.55 + Math.floor(index / 5) * 0.92,
    ] as Position,
  },
}));

const polygonFeatures = LAYER_RECORDS.filter(
  (record) =>
    record.representation === "MAPLIBRE_INLINE" &&
    record.geometryType === "POLYGON" &&
    record.id !== "layer:kansas-frame",
).map((record, index) => {
  const column = index % 4;
  const row = Math.floor(index / 4);
  const west = -101.45 + column * 1.62;
  const south = 37.38 + row * 0.88;
  const east = west + 1.18;
  const north = south + 0.58;
  return {
    type: "Feature" as const,
    id: record.id,
    properties: {
      layer_id: record.id,
      domain: record.domain,
      trust_state: record.trustState,
      fixture: true,
    },
    geometry: {
      type: "Polygon" as const,
      coordinates: [[[west, south], [east, south], [east, north], [west, north], [west, south]]] as Position[][],
    },
  };
});

const lineFeatures = LAYER_RECORDS.filter(
  (record) =>
    record.representation === "MAPLIBRE_INLINE" &&
    (record.geometryType === "LINE" || record.geometryType === "GRID"),
).map((record, index) => ({
  type: "Feature" as const,
  id: record.id,
  properties: {
    layer_id: record.id,
    domain: record.domain,
    trust_state: record.trustState,
    fixture: true,
  },
  geometry: {
    type: "LineString" as const,
    coordinates: [
      [-101.55, 37.35 + index * 0.26],
      [-99.7, 37.65 + index * 0.24],
      [-97.55, 37.45 + index * 0.28],
      [-95.05, 37.72 + index * 0.25],
    ] as Position[],
  },
}));

function layerState(
  states: readonly MapLayerState[],
  id: string,
): MapLayerState {
  return states.find((entry) => entry.id === id) ?? {
    id,
    visible: false,
    opacity: 0,
  };
}

export function createLivingAtlasStyle(
  representation: MapRepresentation,
  states: readonly MapLayerState[],
  committedTimeId = "time:modern",
): MapLibreSafeStyle {
  const renderable = LAYER_RECORDS.filter(
    (record) => record.representation === "MAPLIBRE_INLINE",
  );
  return {
    version: 8,
    projection: { type: representation === "GLOBE" ? "globe" : "mercator" },
    sources: {
      "kfm-kansas-frame": {
        type: "geojson",
        data: {
          type: "Feature",
          id: "layer:kansas-frame",
          properties: {
            layer_id: "layer:kansas-frame",
            trust_state: "GENERALIZED",
            fixture: true,
          },
          geometry: { type: "Polygon", coordinates: [kansasRing] },
        },
      },
      "kfm-domain-points": {
        type: "geojson",
        data: { type: "FeatureCollection", features: domainPoints },
      },
      "kfm-domain-polygons": {
        type: "geojson",
        data: { type: "FeatureCollection", features: polygonFeatures },
      },
      "kfm-domain-lines": {
        type: "geojson",
        data: { type: "FeatureCollection", features: lineFeatures },
      },
    },
    layers: [
      {
        id: "kfm-background",
        type: "background",
        paint: { "background-color": "#071517" },
      },
      ...renderable.map((record) => {
        const state = layerState(states, record.id);
        const temporallyCompatible = isLayerTemporallyCompatible(
          record.temporalExtentId,
          committedTimeId,
        );
        const filter: ["==", ["get", string], string] | undefined =
          record.id === "layer:kansas-frame"
            ? undefined
            : ["==", ["get", "layer_id"], record.id];
        const common = {
          id: record.id,
          source:
            record.id === "layer:kansas-frame"
              ? "kfm-kansas-frame"
              : record.geometryType === "POINT"
                ? "kfm-domain-points"
                : record.geometryType === "POLYGON"
                  ? "kfm-domain-polygons"
                  : "kfm-domain-lines",
          filter,
          layout: {
            visibility:
              state.visible && temporallyCompatible ? "visible" : "none",
          },
        } as const;
        if (record.geometryType === "POINT") {
          return {
            ...common,
            type: "circle" as const,
            paint: {
              "circle-color": record.color,
              "circle-opacity": state.opacity,
              "circle-radius": 7,
              "circle-stroke-color": "#071517",
              "circle-stroke-width": 2,
            },
          };
        }
        if (record.geometryType === "POLYGON") {
          return {
            ...common,
            type: "fill" as const,
            paint: {
              "fill-color": record.color,
              "fill-opacity": state.opacity,
              "fill-outline-color": record.color,
            },
          };
        }
        return {
          ...common,
          type: "line" as const,
          paint: {
            "line-color": record.color,
            "line-opacity": state.opacity,
            "line-width": record.geometryType === "GRID" ? 1 : 3,
            "line-dasharray": record.geometryType === "GRID" ? [2, 2] : [1, 0],
          },
        };
      }),
      {
        id: "kfm-kansas-outline",
        type: "line",
        source: "kfm-kansas-frame",
        paint: {
          "line-color": "#f3ddaa",
          "line-opacity": 0.92,
          "line-width": 2.2,
        },
      },
    ],
  };
}

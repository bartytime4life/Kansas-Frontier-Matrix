import pluginConnectionSource from "./maplibre-plugin-connections.json";

export type MapLibrePluginConnectionStatus = "READY_FOR_ADAPTER" | "HOLD" | "DEVELOPMENT_ONLY";
export type MapLibrePluginConnectionClass =
  | "SEARCH"
  | "CARRIER"
  | "COMPARISON"
  | "INTERACTION"
  | "EXPORT"
  | "RASTER"
  | "TERRAIN"
  | "DIAGNOSTICS"
  | "VISUALIZATION";

export type MapLibrePluginConnection = Readonly<{
  id: string;
  title: string;
  project: string;
  connectionClass: MapLibrePluginConnectionClass;
  status: MapLibrePluginConnectionStatus;
  reason: string;
  connection: string;
  gate: string;
  fallback: string;
}>;

type MapLibrePluginConnectionSource = Readonly<{
  schemaVersion: string;
  source: Readonly<{
    title: string;
    publisher: string;
    referenceUrl: string;
    reviewedAt: string;
  }>;
  connections: readonly MapLibrePluginConnection[];
}>;

const source = pluginConnectionSource as MapLibrePluginConnectionSource;

export const MAPLIBRE_PLUGIN_CONNECTION_SOURCE = Object.freeze({ ...source.source });

export const MAPLIBRE_PLUGIN_CONNECTIONS: readonly MapLibrePluginConnection[] = Object.freeze(
  source.connections.map((connection) => Object.freeze({ ...connection })),
);

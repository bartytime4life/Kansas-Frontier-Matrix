import { useEffect, useRef, useState } from "react";
import maplibregl from "maplibre-gl";
import "maplibre-gl/dist/maplibre-gl.css";

import { fetchEcologyStacCatalog } from "./stac";
import {
  ECOLOGY_LAYER_ID,
  ECOLOGY_SOURCE_ID,
  buildEcologyFillLayer,
  buildEcologyVectorSource
} from "./ecologyLayer";

type EcologyMapProps = {
  apiBase?: string;
  tilesUrl?: string;
};

export function EcologyMap({
  apiBase = "/api",
  tilesUrl = "https://example.invalid/tiles/{z}/{x}/{y}.pbf"
}: EcologyMapProps) {
  const mapContainerRef = useRef<HTMLDivElement | null>(null);
  const mapRef = useRef<maplibregl.Map | null>(null);
  const [status, setStatus] = useState("Loading governed ecology catalog...");

  useEffect(() => {
    if (!mapContainerRef.current || mapRef.current) return;

    const map = new maplibregl.Map({
      container: mapContainerRef.current,
      style: {
        version: 8,
        sources: {
          basemap: {
            type: "raster",
            tiles: ["https://tile.openstreetmap.org/{z}/{x}/{y}.png"],
            tileSize: 256,
            attribution: "© OpenStreetMap contributors"
          }
        },
        layers: [
          {
            id: "basemap",
            type: "raster",
            source: "basemap"
          }
        ]
      },
      center: [-98.5, 38.5],
      zoom: 5
    });

    mapRef.current = map;

    map.on("load", async () => {
      try {
        const catalog = await fetchEcologyStacCatalog(apiBase);

        if (catalog.type !== "Catalog") {
          throw new Error("Governed ecology STAC response was not a Catalog");
        }

        if (!map.getSource(ECOLOGY_SOURCE_ID)) {
          map.addSource(ECOLOGY_SOURCE_ID, buildEcologyVectorSource(tilesUrl));
        }

        if (!map.getLayer(ECOLOGY_LAYER_ID)) {
          map.addLayer(buildEcologyFillLayer());
        }

        setStatus(`Loaded ${catalog.title}`);
      } catch (error) {
        setStatus(error instanceof Error ? error.message : "Failed to load ecology layer");
      }
    });

    return () => {
      map.remove();
      mapRef.current = null;
    };
  }, [apiBase, tilesUrl]);

  return (
    <section>
      <div
        ref={mapContainerRef}
        style={{
          width: "100%",
          height: "520px",
          borderRadius: "12px",
          overflow: "hidden"
        }}
      />
      <p>{status}</p>
    </section>
  );
}

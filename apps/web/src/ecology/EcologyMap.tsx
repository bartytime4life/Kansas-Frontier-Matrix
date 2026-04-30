import { useEffect, useRef, useState } from "react";
import maplibregl, { type MapMouseEvent } from "maplibre-gl";
import "maplibre-gl/dist/maplibre-gl.css";

import EvidenceDrawer, {
  type EvidenceDrawerLayerMetadata
} from "./EvidenceDrawer";
import { fetchEcologyLayerManifest } from "./layerManifest";
import {
  ECOLOGY_LAYER_ID,
  ECOLOGY_SOURCE_ID,
  buildEcologyFillLayer,
  buildEcologyVectorSource
} from "./ecologyLayer";

type EcologyMapProps = {
  apiBase?: string;
  layerId?: string;
};

export function EcologyMap({
  apiBase = "/api",
  layerId = "example-pass"
}: EcologyMapProps) {
  const mapContainerRef = useRef<HTMLDivElement | null>(null);
  const mapRef = useRef<maplibregl.Map | null>(null);

  const [status, setStatus] = useState("Loading governed ecology layer...");
  const [drawerOpen, setDrawerOpen] = useState(false);
  const [featureProperties, setFeatureProperties] =
    useState<Record<string, unknown>>();
  const [layerMetadata, setLayerMetadata] =
    useState<EvidenceDrawerLayerMetadata>();

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
        const manifest = await fetchEcologyLayerManifest(layerId, apiBase);

        if (!map.getSource(ECOLOGY_SOURCE_ID)) {
          map.addSource(ECOLOGY_SOURCE_ID, buildEcologyVectorSource(manifest));
        }

        if (!map.getLayer(ECOLOGY_LAYER_ID)) {
          map.addLayer(buildEcologyFillLayer(manifest));
        }

        const metadata: EvidenceDrawerLayerMetadata = {
          layerId: manifest.layer_id,
          evidenceBundleRef: manifest.evidence_bundle_ref,
          promotionDecisionRef: manifest.promotion_decision_ref,
          runReceiptRef: manifest.run_receipt_ref,
          allowedFields: manifest.allowed_fields,
          publicSafe: manifest.public_safe
        };

        setLayerMetadata(metadata);

        map.on("mouseenter", ECOLOGY_LAYER_ID, () => {
          map.getCanvas().style.cursor = "pointer";
        });

        map.on("mouseleave", ECOLOGY_LAYER_ID, () => {
          map.getCanvas().style.cursor = "";
        });

        map.on("click", ECOLOGY_LAYER_ID, (event: MapMouseEvent) => {
          const feature = event.features?.[0];
          const rawProperties = feature?.properties ?? {};

          const filteredProperties = Object.fromEntries(
            Object.entries(rawProperties).filter(([key]) =>
              manifest.allowed_fields.includes(key)
            )
          );

          setFeatureProperties(filteredProperties);
          setLayerMetadata(metadata);
          setDrawerOpen(true);
        });

        if (manifest.bounds) {
          map.fitBounds(
            [
              [manifest.bounds[0], manifest.bounds[1]],
              [manifest.bounds[2], manifest.bounds[3]]
            ],
            { padding: 32, duration: 0 }
          );
        }

        setStatus(`Loaded governed layer: ${manifest.title}`);
      } catch (error) {
        setStatus(
          error instanceof Error ? error.message : "Failed to load ecology layer"
        );
      }
    });

    return () => {
      map.remove();
      mapRef.current = null;
    };
  }, [apiBase, layerId]);

  return (
    <section style={{ position: "relative" }}>
      <div
        ref={mapContainerRef}
        style={{
          width: "100%",
          height: "520px",
          borderRadius: "12px",
          overflow: "hidden"
        }}
      />

      <EvidenceDrawer
        open={drawerOpen}
        onClose={() => setDrawerOpen(false)}
        featureProperties={featureProperties}
        layerMetadata={layerMetadata}
      />

      <p>{status}</p>
    </section>
  );
}

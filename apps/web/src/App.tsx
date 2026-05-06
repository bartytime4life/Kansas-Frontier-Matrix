import { useMemo, useState } from "react";
import FocusPanel from "./ecology/FocusPanel";
import { releaseRenderableLayers, type ReleaseManifest } from "./ecology/mapLayers";

const demoManifest: ReleaseManifest = {
  layers: [
    { id: "released-hydrology", name: "Hydrology", source: { kind: "released" }, trust: { derivation: "observed", precision: "generalized" } },
    { id: "released-habitat", name: "Habitat Suitability", source: { kind: "released" }, trust: { derivation: "derived", precision: "generalized" } },
    { id: "sensitive-exact", name: "Sensitive Nests", source: { kind: "released" }, trust: { derivation: "observed", precision: "exact" } }
  ]
};

export default function App() {
  const [clicked, setClicked] = useState<{ lng: number; lat: number } | null>(null);
  const layers = useMemo(() => releaseRenderableLayers(demoManifest), []);

  return (
    <main style={{ display: "grid", gridTemplateColumns: "1fr 340px", minHeight: "100vh" }}>
      <section style={{ position: "relative" }}>
        <div
          role="button"
          tabIndex={0}
          onClick={() => setClicked({ lng: -97.3301, lat: 37.6872 })}
          onKeyDown={(e) => e.key === "Enter" && setClicked({ lng: -97.3301, lat: 37.6872 })}
          style={{ height: "100%", minHeight: 480, background: "#eef3f8", padding: 16 }}
        >
          <h1>Ecology Map</h1>
          <p>MapLibre view (v1): rendering only ReleaseManifest layers.</p>
          <ul>{layers.map((layer) => <li key={layer.id}>{layer.name ?? layer.id}</li>)}</ul>
          <p>{clicked ? `Selected point: ${clicked.lat}, ${clicked.lng}` : "Click map to open focus context."}</p>
        </div>
      </section>

      <FocusPanel />
    </main>
  );
}

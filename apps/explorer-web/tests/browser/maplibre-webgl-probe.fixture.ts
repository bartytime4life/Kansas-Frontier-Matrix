import { createViteMapLibreAdapter } from "@kfm/maplibre/vite-adapter";

const status = document.querySelector<HTMLElement>("#probe-status");
if (status === null) {
  throw new Error("MapLibre WebGL probe status control is missing.");
}

document.body.dataset.fixtureId = "kfm-maplibre-webgl-probe-v1";
const runtime = createViteMapLibreAdapter({
  containerId: "map",
  interactive: false,
  style: { version: 8, sources: {}, layers: [] },
});

runtime.subscribeSnapshot((snapshot) => {
  status.dataset.state = snapshot.state;
  status.dataset.reason = snapshot.reason ?? "NONE";
  status.textContent = `State ${snapshot.state}; reason ${snapshot.reason ?? "NONE"}`;
});

void runtime.initialize().catch(() => {
  // The status snapshot is the finite browser outcome.
});

window.addEventListener("pagehide", () => runtime.dispose(), { once: true });

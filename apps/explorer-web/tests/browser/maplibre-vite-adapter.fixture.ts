import { createViteMapLibreAdapter } from "@kfm/maplibre/vite-adapter";

const status = document.querySelector<HTMLElement>("#runtime-status");
const disposeButton = document.querySelector<HTMLButtonElement>("#dispose-runtime");
if (status === null || disposeButton === null) {
  throw new Error("MapLibre Vite adapter fixture controls are missing.");
}

const runtime = createViteMapLibreAdapter({
  containerId: "maplibre-vite-map",
  interactive: false,
});

runtime.subscribeSnapshot((snapshot) => {
  status.dataset.state = snapshot.state;
  status.dataset.reason = snapshot.reason ?? "NONE";
  status.textContent = `State ${snapshot.state}; reason ${snapshot.reason ?? "NONE"}`;
});

void runtime.initialize().then(
  () => {
    document.body.dataset.initialization = "resolved";
  },
  () => {
    document.body.dataset.initialization = "rejected";
  },
);

disposeButton.addEventListener("click", () => runtime.dispose());
window.addEventListener("pagehide", () => runtime.dispose(), { once: true });

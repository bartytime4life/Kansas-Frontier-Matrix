import { createViteMapLibreAdapter } from "@kfm/maplibre/vite-adapter";

const status = document.querySelector<HTMLElement>("#runtime-status");
const disposeButton = document.querySelector<HTMLButtonElement>("#dispose-runtime");
const mapContainer = document.querySelector<HTMLElement>("#maplibre-vite-map");
const revealButton = document.querySelector<HTMLButtonElement>("#reveal-map");
if (
  status === null ||
  disposeButton === null ||
  mapContainer === null ||
  revealButton === null
) {
  throw new Error("MapLibre Vite adapter fixture controls are missing.");
}

const startsHidden = new URL(location.href).searchParams.get("hidden") === "1";
if (startsHidden) {
  mapContainer.style.display = "none";
  revealButton.hidden = false;
  revealButton.addEventListener("click", () => {
    mapContainer.style.display = "block";
  });
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

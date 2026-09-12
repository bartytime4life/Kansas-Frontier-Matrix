import maplibregl from "maplibre-gl";

const status = document.querySelector<HTMLElement>("#probe-status");
const container = document.querySelector<HTMLElement>("#map");
if (status === null || container === null) {
  throw new Error("MapLibre WebGL probe controls are missing.");
}

document.body.dataset.maplibreVersion = maplibregl.getVersion?.() ?? "unknown";
document.body.dataset.fixtureId = "kfm-maplibre-webgl-probe-v1";
const map = new maplibregl.Map({
  container,
  style: { version: 8, sources: {}, layers: [] },
  interactive: false,
  attributionControl: false,
});

map.once("load", () => {
  status.dataset.state = "READY";
  status.textContent = "State READY";
});

map.on("error", (event) => {
  status.dataset.state = "ERROR";
  status.dataset.reason = event.error?.message ?? "MAP_ERROR";
  status.textContent = `State ERROR; reason ${status.dataset.reason}`;
});

window.addEventListener("pagehide", () => map.remove(), { once: true });

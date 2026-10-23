// The Site's single MapLibre acquisition seam (ADR-0006, separately built Site exception).
// Every other Site module takes renderer types and the runtime from here, never from
// maplibre-gl directly; tools/validators/maplibre/assess_acquisition_inventory.py enforces it.
export type * from "maplibre-gl";

export type MapLibreModule = typeof import("maplibre-gl");

// Loaded on demand so the renderer stays out of the initial bundle.
let cacheProtocolInstalled = false;
export const loadMapLibre = async (): Promise<MapLibreModule> => {
  const runtime = await import("maplibre-gl");
  const { basemapCacheProtocol } = await import("./basemap-cache");
  if (!cacheProtocolInstalled) {
    installMapProtocol(runtime, "kfm-basemap", basemapCacheProtocol);
    cacheProtocolInstalled = true;
  }
  return runtime;
};

// Keep renderer protocol registration at the same acquisition seam as the
// module import. Callers provide only the bounded tile loader and own teardown.
export function installMapProtocol(runtime: MapLibreModule, name: string,
  load: Parameters<MapLibreModule["addProtocol"]>[1]): void {
  runtime.addProtocol(name, load);
}


/** Native fullscreen for a stage containing both the map and its provenance UI.
 * Own the button state explicitly so a custom fullscreen target cannot leave
 * the renderer control claiming "Enter" while that stage is already fullscreen. */
export function createStageFullscreenControl(target: HTMLElement): import("maplibre-gl").IControl {
  const owner = target.ownerDocument;
  let root: HTMLDivElement | null = null;
  let button: HTMLButtonElement | null = null;
  let status: HTMLSpanElement | null = null;
  let map: import("maplibre-gl").Map | null = null;
  const synchronize = () => {
    if (!button) return;
    const active = owner.fullscreenElement === target;
    const label = active ? "Exit fullscreen" : "Enter fullscreen";
    button.className = active ? "maplibregl-ctrl-shrink" : "maplibregl-ctrl-fullscreen";
    button.title = label;
    button.setAttribute("aria-label", label);
    button.setAttribute("aria-pressed", String(active));
  };
  const changed = () => { synchronize(); map?.resize(); };
  const unavailable = () => {
    if (status) status.textContent = "Fullscreen is unavailable. You can continue using the map.";
    synchronize();
  };
  const toggle = (event: Event) => {
    event.stopPropagation();
    if (status) status.textContent = "";
    try {
      const operation = owner.fullscreenElement === target ? owner.exitFullscreen() : target.requestFullscreen();
      void Promise.resolve(operation).catch(unavailable);
    } catch { unavailable(); }
  };
  return {
    onAdd(addedMap) {
      map = addedMap;
      root = owner.createElement("div");
      root.className = "maplibregl-ctrl maplibregl-ctrl-group";
      button = owner.createElement("button");
      button.type = "button";
      const icon = owner.createElement("span");
      icon.className = "maplibregl-ctrl-icon";
      icon.setAttribute("aria-hidden", "true");
      button.appendChild(icon);
      status = owner.createElement("span");
      status.className = "sr-only";
      status.setAttribute("role", "status");
      status.setAttribute("aria-live", "polite");
      root.append(button, status);
      if (!owner.fullscreenEnabled || typeof target.requestFullscreen !== "function") root.style.display = "none";
      button.addEventListener("click", toggle);
      owner.addEventListener("fullscreenchange", changed);
      synchronize();
      return root;
    },
    onRemove() {
      owner.removeEventListener("fullscreenchange", changed);
      button?.removeEventListener("click", toggle);
      root?.remove();
      root = null; button = null; status = null; map = null;
    },
  };
}

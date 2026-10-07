import { validVolumeBounds, type AquiferVolume, type VolumeBounds } from "./aquifer-volume";

type Locator = {
  getPitch(): number; getBearing(): number; getProjection(): {type?: unknown} | null | undefined;
  getBounds(): {getWest(): number; getSouth(): number; getEast(): number; getNorth(): number};
  isMoving(): boolean; areTilesLoaded(): boolean; triggerRepaint(): void;
  on(event: string, listener: () => void): unknown; off(event: string, listener: () => void): unknown;
};
type WorkerPort = {
  postMessage(value: {id: number; bounds: VolumeBounds}): void;
  onmessage: ((event: MessageEvent<{id: number; volume?: AquiferVolume; error?: string}>) => void) | null;
  onerror: ((event: ErrorEvent) => unknown) | null;
};
export type AquiferViewSnapshot<Image> = {volume: AquiferVolume; image: Image | null};

/** Geometry is independent of optional map imagery. A slow external layer cannot hold local polygons. */
export function startAquiferView<Image>(options: {
  map: Locator; worker: WorkerPort; sampleSurface: () => Image;
  manual?: boolean; onArea?: (bounds: VolumeBounds | null) => void; onPreview?: (changed: boolean) => void;
  onSnapshot: (snapshot: AquiferViewSnapshot<Image> | null) => void;
  onStatus: (status: string) => void; onSurfaceStatus: (status: string) => void;
  timers?: {set: (callback: () => void, delay: number) => unknown; clear: (handle: unknown) => void};
}) {
  const {map, worker, sampleSurface, onSnapshot, onStatus, onSurfaceStatus} = options;
  const timers = options.timers ?? {
    set: (callback: () => void, delay: number) => globalThis.setTimeout(callback, delay),
    clear: (handle: unknown) => globalThis.clearTimeout(handle as ReturnType<typeof setTimeout>),
  };
  let serial = 0, disposed = false, awaitingLocator = false, timeout: unknown, debounce: unknown, capture: (() => void) | null = null;
  let pending: {id: number; bounds: VolumeBounds; volume: AquiferVolume | null; image: Image | null} | null = null;
  const clearCapture = () => { if (capture) map.off("render", capture); capture = null; timers.clear(timeout); };
  const publish = () => { if (pending?.volume) onSnapshot({volume: pending.volume, image: pending.image}); };
  const prepare = () => {
    if (disposed) return;
    clearCapture(); pending = null; const id = ++serial;
    onSnapshot(null);
    let bounds: VolumeBounds;
    awaitingLocator = true;
    try {
      const projection = map.getProjection()?.type;
      if (typeof projection !== "string") {
        options.onArea?.(null); onStatus("Waiting for the locator style and projection to become available…"); return;
      }
      if (Math.abs(map.getPitch()) > .1 || Math.abs(map.getBearing()) > .1 || projection !== "mercator") {
        options.onArea?.(null); onStatus("Choose Reset to 2D before showing this area."); return;
      }
      if (map.isMoving()) { options.onArea?.(null); onStatus("Wait for the selector to stop moving, then show this area."); return; }
      const b = map.getBounds(); bounds = [b.getWest(), b.getSouth(), b.getEast(), b.getNorth()];
    } catch {
      options.onArea?.(null); onStatus("Waiting for the locator style and projection to become available…"); return;
    }
    awaitingLocator = false;
    if (!validVolumeBounds(bounds)) {
      options.onArea?.(null); onStatus("Zoom into Kansas to a view narrower than one degree, or choose the High Plains example."); return;
    }
    pending = {id, bounds, volume: null, image: null};
    options.onPreview?.(false); options.onArea?.(bounds);
    onStatus("Preparing verified aquifer geometry…");
    onSurfaceStatus("Surface image loading separately. The locator above stays available.");
    // Start first: neither tile completeness nor canvas readback grants geometry eligibility.
    worker.postMessage({id, bounds});
    capture = () => {
      if (disposed || id !== serial || !pending) return;
      try {
        if (map.isMoving() || !map.areTilesLoaded()) return;
        const current = map.getBounds(), actual = [current.getWest(),current.getSouth(),current.getEast(),current.getNorth()];
        if (actual.some((value,index)=>value!==pending!.bounds[index])) { clearCapture(); options.onPreview?.(true); onSurfaceStatus("Surface capture withheld: the selector no longer matches the selected area."); return; }
        const image = sampleSurface();
        if (disposed || id !== serial || !pending) return;
        pending.image = image;
        clearCapture(); publish(); onSurfaceStatus("Surface image matches this locator extent.");
      } catch {
        if (disposed || id !== serial) return;
        clearCapture(); onSurfaceStatus("Surface image unavailable. The outlined plane marks the locator extent; aquifer geometry remains available.");
      }
    };
    map.on("render", capture);
    timeout = timers.set(() => {
      if (disposed || id !== serial) return;
      clearCapture();
      onSurfaceStatus("Surface tiles are incomplete. The outlined plane marks the locator extent; aquifer geometry remains available. Refresh to retry the image.");
    }, 8000);
    map.triggerRepaint();
  };
  worker.onmessage = ({data}) => {
    if (disposed || data.id !== serial || pending?.id !== data.id) return;
    if (data.volume) {
      if (!data.volume.bounds || data.volume.bounds.some((value,index)=>value!==pending!.bounds[index])) { clearCapture(); onStatus("Area geometry did not match the selected frame; display held. Show this area again."); return; }
      pending.volume = data.volume; publish();
      onStatus(`${data.volume.envelopes.length} classified overlap regions · 2022–2024 snapshot${data.volume.heldClasses ? ` · ${data.volume.heldClasses} open-ended or missing classes withheld` : ""}${data.volume.truncated ? " · partial geometry: display budget reached" : ""}`);
    } else { clearCapture(); onStatus(data.error ?? "Aquifer preparation unavailable. Refresh to retry."); }
  };
  worker.onerror = () => { if (!disposed) { clearCapture(); onStatus("Aquifer preparation failed. Refresh to retry; source ranges are not substituted."); } };
  const invalidate = () => {
    if (disposed) return;
    awaitingLocator = false;
    clearCapture(); pending = null; serial++; timers.clear(debounce);
    if (options.manual) {
      options.onPreview?.(true);
      onStatus("Selector preview changed. Show this area to apply it to the underlay.");
      onSurfaceStatus("The underlay keeps its selected-area image while you frame a new area.");
    } else { onSnapshot(null); onSurfaceStatus(""); onStatus("Locator changed. Preparing the new area when movement stops…"); }
  };
  const schedule = () => { if (disposed) return; invalidate(); if (!options.manual) debounce = timers.set(prepare, 250); };
  const locatorReady = () => {
    if (disposed || !awaitingLocator) return;
    timers.clear(debounce); debounce = timers.set(prepare, 250);
  };
  const stop = () => {
    if (disposed) return;
    disposed = true; serial++; pending = null; clearCapture(); timers.clear(debounce);
    map.off("movestart", invalidate); map.off("moveend", schedule); map.off("resize", schedule);
    map.off("styledata", locatorReady); map.off("load", locatorReady); map.off("remove", removed);
    worker.onmessage = null; worker.onerror = null;
  };
  const removed = () => { if (disposed) return; stop(); onSnapshot(null); onSurfaceStatus(""); onStatus("Locator removed. Reopen Underground when the map is available."); };
  map.on("movestart", invalidate); map.on("moveend", schedule); map.on("resize", schedule);
  map.on("styledata", locatorReady); map.on("load", locatorReady); map.on("remove", removed); if (!options.manual) prepare(); else onStatus("Frame a local area in the selector, then choose Show this area.");
  return Object.assign(stop, {prepare});
}

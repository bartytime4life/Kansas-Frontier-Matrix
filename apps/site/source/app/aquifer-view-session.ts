import { validVolumeBounds, type AquiferVolume, type VolumeBounds } from "./aquifer-volume";

type Locator = {
  getPitch(): number; getBearing(): number; getProjection(): {type?: unknown};
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
  onSnapshot: (snapshot: AquiferViewSnapshot<Image> | null) => void;
  onStatus: (status: string) => void; onSurfaceStatus: (status: string) => void;
  timers?: {set: (callback: () => void, delay: number) => unknown; clear: (handle: unknown) => void};
}) {
  const {map, worker, sampleSurface, onSnapshot, onStatus, onSurfaceStatus} = options;
  const timers = options.timers ?? {set: setTimeout, clear: (handle: unknown) => clearTimeout(handle as ReturnType<typeof setTimeout>)};
  let serial = 0, disposed = false, timeout: unknown, debounce: unknown, capture: (() => void) | null = null;
  let pending: {id: number; volume: AquiferVolume | null; image: Image | null} | null = null;
  const clearCapture = () => { if (capture) map.off("render", capture); capture = null; timers.clear(timeout); };
  const publish = () => { if (pending?.volume) onSnapshot({volume: pending.volume, image: pending.image}); };
  const prepare = () => {
    if (disposed) return;
    clearCapture(); pending = null; const id = ++serial;
    onSnapshot(null);
    if (Math.abs(map.getPitch()) > .1 || Math.abs(map.getBearing()) > .1 || map.getProjection().type !== "mercator") {
      onStatus("Choose Reset to 2D above before preparing the aquifer shape."); return;
    }
    const b = map.getBounds(), bounds: VolumeBounds = [b.getWest(), b.getSouth(), b.getEast(), b.getNorth()];
    if (!validVolumeBounds(bounds)) {
      onStatus("Zoom into Kansas to a view narrower than one degree, or choose the High Plains example."); return;
    }
    pending = {id, volume: null, image: null};
    onStatus("Preparing verified aquifer geometry…");
    onSurfaceStatus("Surface image loading separately. The locator above stays available.");
    // Start first: neither tile completeness nor canvas readback grants geometry eligibility.
    worker.postMessage({id, bounds});
    capture = () => {
      if (disposed || id !== serial || !pending || map.isMoving() || !map.areTilesLoaded()) return;
      try {
        pending.image = sampleSurface();
        clearCapture(); publish(); onSurfaceStatus("Surface image matches this locator extent.");
      } catch {
        clearCapture(); onSurfaceStatus("Surface image unavailable. The outlined plane marks the locator extent; aquifer geometry remains available.");
      }
    };
    map.on("render", capture);
    timeout = timers.set(() => {
      clearCapture();
      onSurfaceStatus("Surface tiles are incomplete. The outlined plane marks the locator extent; aquifer geometry remains available. Refresh to retry the image.");
    }, 8000);
    map.triggerRepaint();
  };
  worker.onmessage = ({data}) => {
    if (disposed || data.id !== serial || pending?.id !== data.id) return;
    if (data.volume) {
      pending.volume = data.volume; publish();
      onStatus(`${data.volume.envelopes.length} classified overlap regions · 2022–2024 snapshot${data.volume.heldClasses ? ` · ${data.volume.heldClasses} open-ended or missing classes withheld` : ""}${data.volume.truncated ? " · partial geometry: display budget reached" : ""}`);
    } else { clearCapture(); onStatus(data.error ?? "Aquifer preparation unavailable. Refresh to retry."); }
  };
  worker.onerror = () => { if (!disposed) { clearCapture(); onStatus("Aquifer preparation failed. Refresh to retry; source ranges are not substituted."); } };
  const invalidate = () => {
    clearCapture(); pending = null; serial++; timers.clear(debounce);
    onSnapshot(null); onSurfaceStatus(""); onStatus("Locator changed. Preparing the new area when movement stops…");
  };
  const schedule = () => { invalidate(); debounce = timers.set(prepare, 250); };
  map.on("movestart", invalidate); map.on("moveend", schedule); map.on("resize", schedule); prepare();
  return () => { disposed = true; serial++; pending = null; clearCapture(); timers.clear(debounce); map.off("movestart", invalidate); map.off("moveend", schedule); map.off("resize", schedule); worker.onmessage = null; worker.onerror = null; };
}

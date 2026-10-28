import type { Map as MapLibreMap } from "maplibre-gl";

// Explicit, local diagnostic opt-in. No network transport, source bodies,
// coordinates, credentials or production timer is added by this probe.
type FrameEvent = { kind: "stage" | "confirmed" | "failed"; observedAt: string; at: number };
type Probe = { record: (kind: FrameEvent["kind"], observedAt: string) => void; snapshot: () => unknown };
let activeProbe: Probe | null = null;

export function recordStormDeskFrame(kind: FrameEvent["kind"], observedAt: string) {
  activeProbe?.record(kind, observedAt);
}

export function installStormDeskPerformanceProbe(map: MapLibreMap): () => void {
  if (new URLSearchParams(window.location.search).get("stormPerf") !== "1") return () => {};
  const diagnosticWindow = window as Window & { __kfmStormDeskPerf?: Probe };
  const events: FrameEvent[] = [];
  let rendered = 0, droppedEvents = 0, contextLosses = 0;
  const startedAt = performance.now();
  const canvas = map.getCanvas();
  const render = () => { rendered++; };
  const lost = () => { contextLosses++; };
  const probe: Probe = {
    record(kind, observedAt) {
      if (events.length === 2048) { events.shift(); droppedEvents++; }
      events.push({ kind, observedAt, at: performance.now() });
    },
    snapshot: () => ({ startedAt, sampledAt: performance.now(), rendered, contextLosses,
      canvas: { width: canvas.width, height: canvas.height },
      sourceCount: Object.keys(map.getStyle()?.sources ?? {}).length,
      layerCount: map.getStyle()?.layers?.length ?? 0,
      events: events.map(event => ({ ...event })), droppedEvents,
      boundary: "MapLibre render callbacks and exact-frame readiness, not GPU presentation FPS or complete pixel coverage." }),
  };
  activeProbe = probe;
  diagnosticWindow.__kfmStormDeskPerf = probe;
  map.on("render", render);
  canvas.addEventListener("webglcontextlost", lost);
  return () => {
    map.off("render", render);
    canvas.removeEventListener("webglcontextlost", lost);
    if (activeProbe === probe) activeProbe = null;
    if (diagnosticWindow.__kfmStormDeskPerf === probe) delete diagnosticWindow.__kfmStormDeskPerf;
  };
}

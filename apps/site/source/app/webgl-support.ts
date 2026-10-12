// One WebGL2 support probe per page.
//
// A detached probe canvas keeps its context alive until garbage collection,
// and browsers force-lose the oldest live context once they hit their cap
// (about 16 on desktop, fewer on mobile) — usually the main Explorer map.
// Probing on every map mount (story scenes, comparison year pairs) piled up
// those contexts, so a successful probe is remembered for the page. The probe
// is not released with WEBGL_lose_context: some embedded Chromium runtimes
// treat that deliberate loss as a wider GPU failure.
//
// Only success is remembered. A failed probe holds no context, and a later
// mount may succeed once a crashed GPU process has restarted.
let webgl2Confirmed = false;

export function webgl2Available(): boolean {
  if (webgl2Confirmed) return true;
  try {
    webgl2Confirmed = Boolean(document.createElement("canvas").getContext("webgl2"));
  } catch {
    webgl2Confirmed = false;
  }
  return webgl2Confirmed;
}

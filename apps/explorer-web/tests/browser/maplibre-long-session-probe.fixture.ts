import { createViteMapLibreAdapter } from "@kfm/maplibre/vite-adapter";

const FIXTURE_ID = "kfm-maplibre-long-session-probe-v1";
const CYCLES = 3;
const STYLE = { version: 8 as const, sources: {}, layers: [] };

const status = document.querySelector<HTMLElement>("#probe-status");
if (status === null) {
  throw new Error("MapLibre long-session probe status control is missing.");
}

document.body.dataset.fixtureId = FIXTURE_ID;
status.dataset.state = "RUNNING";
status.dataset.cycles = "0";
status.textContent = `State RUNNING; cycles 0/${CYCLES}`;

let activeRuntime: { dispose: () => void } | null = null;
window.addEventListener("pagehide", () => activeRuntime?.dispose(), { once: true });

const canvasPresent = (): boolean => Boolean(document.querySelector("#map canvas"));

const run = async (): Promise<void> => {
  const results: Array<{
    cycle: number;
    observed_states: string[];
    initialization_state: string;
    canvas_before_teardown: boolean;
    disposed_state: string;
    canvas_after_teardown: boolean;
    passed: boolean;
  }> = [];

  for (let cycle = 1; cycle <= CYCLES; cycle += 1) {
    const runtime = createViteMapLibreAdapter({
      containerId: "map",
      interactive: false,
      style: STYLE,
      initializationDeadlineMs: 4_000,
    });
    activeRuntime = runtime;
    const observedStates: string[] = [];
    runtime.subscribeSnapshot((snapshot) => {
      observedStates.push(snapshot.state);
    });

    let initializationState = "UNKNOWN";
    try {
      initializationState = (await runtime.initialize()).state;
    } catch {
      initializationState = runtime.getSnapshot().state;
    }

    const canvasBeforeTeardown = canvasPresent();
    runtime.dispose();
    activeRuntime = null;
    const disposedState = runtime.getSnapshot().state;
    const canvasAfterTeardown = canvasPresent();
    const passed =
      initializationState === "READY" &&
      canvasBeforeTeardown &&
      disposedState === "DISPOSED" &&
      !canvasAfterTeardown;
    results.push({
      cycle,
      observed_states: observedStates,
      initialization_state: initializationState,
      canvas_before_teardown: canvasBeforeTeardown,
      disposed_state: disposedState,
      canvas_after_teardown: canvasAfterTeardown,
      passed,
    });
    status.dataset.cycles = String(cycle);
    status.textContent = `State RUNNING; cycles ${cycle}/${CYCLES}`;
  }

  const passed = results.length === CYCLES && results.every((result) => result.passed);
  document.body.dataset.probeResult = JSON.stringify({
    fixture_id: FIXTURE_ID,
    cycles: CYCLES,
    results,
    passed,
  });
  status.dataset.state = passed ? "PASS" : "FAIL";
  status.textContent = `State ${passed ? "PASS" : "FAIL"}; cycles ${CYCLES}/${CYCLES}`;
};

void run().catch(() => {
  document.body.dataset.probeResult = JSON.stringify({
    fixture_id: FIXTURE_ID,
    cycles: CYCLES,
    results: [],
    passed: false,
    error: "UNEXPECTED_PROBE_FAILURE",
  });
  status.dataset.state = "FAIL";
  status.textContent = `State FAIL; cycles ${status.dataset.cycles ?? "0"}/${CYCLES}`;
});

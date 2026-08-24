import {
  createNullMapRuntime,
  isMapRuntimeTrustState,
} from "@kfm/maplibre";
import { mountMapRuntimeTrustStatus } from "../../src/features/map_runtime";

const root = document.querySelector<HTMLElement>("#fixture-root");
if (root === null) throw new Error("Map runtime trust-status fixture root is missing.");

const runtime = createNullMapRuntime();
mountMapRuntimeTrustStatus(root, runtime);

for (const button of document.querySelectorAll<HTMLButtonElement>("button")) {
  button.addEventListener("click", () => {
    const action = button.dataset.runtimeAction;
    if (action === "initialize") {
      void runtime.initialize();
      return;
    }
    if (action === "dispose") {
      runtime.dispose();
      return;
    }

    const state = button.dataset.runtimeState;
    if (isMapRuntimeTrustState(state)) runtime.emitTrustState(state);
  });
}

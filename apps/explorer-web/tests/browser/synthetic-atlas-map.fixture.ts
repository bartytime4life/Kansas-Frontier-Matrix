import { createViteMapLibreAdapter } from "@kfm/maplibre/vite-adapter";
import { type MapRuntimePort } from "@kfm/maplibre";
import { mountEvidenceDrawer, type EvidenceDrawerController } from "../../src/features/evidence_drawer";
import { bindMapRuntimeEvidence, resolveMapRuntimeSelectionEvidence, type MapRuntimeEvidenceBinding, type MapRuntimeEvidenceUpdate } from "../../src/features/map_runtime/runtime-evidence-binding";
import { fixtureProjectionForScenario, loadSyntheticAtlasFixture, type SyntheticAtlasScenario } from "./synthetic-atlas-evidence.fixture";

/** Browser-only composition: literal pinned geometry, simulated trust, no loader. */
export async function mountSyntheticAtlasMap(host: HTMLElement): Promise<void> {
  host.textContent = "Verifying synthetic Kansas fixture…";
  const packet = await loadSyntheticAtlasFixture();
  const document = host.ownerDocument;
  const region = document.createElement("section");
  region.dataset.component = "synthetic-atlas-map";
  const heading = document.createElement("h2");
  heading.textContent = "Synthetic Kansas map to evidence proof";
  const notice = document.createElement("p");
  notice.textContent = "Repository-authored synthetic geometry. Trust and release fields are simulated fixture values; this proof grants no source, policy, release or publication authority.";
  const legend = document.createElement("p");
  legend.dataset.component = "atlas-legend";
  legend.textContent = `Blue fill: synthetic test extent. Units: ${packet.units}. Time: ${packet.timeStart} to ${packet.timeEnd}. This is not an observed Kansas measurement.`;
  const provenance = document.createElement("details");
  provenance.dataset.component = "atlas-provenance";
  const provenanceTitle = document.createElement("summary");
  provenanceTitle.textContent = "Inspect fixture provenance";
  const provenanceList = document.createElement("ul");
  for (const value of [packet.candidateId, packet.featureId, packet.evidenceRef, packet.bundleId, packet.carrierDigest, ...packet.provenance]) {
    const item = document.createElement("li");
    item.textContent = value;
    provenanceList.append(item);
  }
  provenance.append(provenanceTitle, provenanceList);
  const controls = document.createElement("div");
  const textSelector = document.createElement("button");
  textSelector.type = "button";
  textSelector.textContent = "Inspect synthetic Kansas test extent without the map";
  textSelector.disabled = true;
  const scenarioLabel = document.createElement("label");
  scenarioLabel.textContent = "Synthetic evidence state ";
  const scenarioSelect = document.createElement("select");
  scenarioSelect.dataset.component = "atlas-scenario";
  const scenarios = ["available", "no-results", "stale", "deny", "error"] as const;
  for (const scenario of scenarios) {
    const option = document.createElement("option");
    option.value = scenario;
    option.textContent = scenario;
    scenarioSelect.append(option);
  }
  scenarioLabel.append(scenarioSelect);
  const destroyButton = document.createElement("button");
  destroyButton.type = "button";
  destroyButton.textContent = "Dispose synthetic map";
  controls.append(textSelector, scenarioLabel, destroyButton);
  const runtimeStatus = document.createElement("p");
  runtimeStatus.dataset.component = "atlas-runtime-status";
  const status = document.createElement("p");
  status.setAttribute("role", "status");
  status.dataset.component = "atlas-evidence-status";
  status.textContent = "ABSTAIN / SELECTION_REQUIRED";
  const mapHost = document.createElement("div");
  mapHost.id = "synthetic-atlas-map-canvas";
  mapHost.style.cssText = "width:720px;max-width:100%;height:420px;position:relative";
  mapHost.setAttribute("aria-label", "Synthetic Kansas fixture map");
  const drawerHost = document.createElement("div");
  region.append(heading, notice, legend, provenance, controls, runtimeStatus, status, mapHost, drawerHost);
  host.replaceChildren(region);

  // The consumer sees only the accepted KFM port; raw renderer values stay in
  // the package. Selection bindings derive only from the verified fixture.
  const runtime: MapRuntimePort = createViteMapLibreAdapter({
    containerId: mapHost.id,
    style: packet.style,
    fixtureSelections: [packet.selection],
    initializationDeadlineMs: 15_000,
  });
  let scenario: SyntheticAtlasScenario = "available";
  let drawer: EvidenceDrawerController | null = null;
  let binding: MapRuntimeEvidenceBinding | null = null;
  let destroyed = false;
  let selections = 0;
  let deliveries = 0;
  let textRequestVersion = 0;
  region.dataset.selectionCount = "0";
  region.dataset.deliveryCount = "0";
  region.dataset.textSelectionCount = "0";
  const unsubscribeSnapshot = runtime.subscribeSnapshot((snapshot) => {
    region.dataset.runtimeState = snapshot.state;
    region.dataset.camera = JSON.stringify(snapshot.camera);
    runtimeStatus.textContent = `Map runtime: ${snapshot.state}`;
    textSelector.disabled = snapshot.state !== "READY";
    if (snapshot.state !== "READY") {
      textRequestVersion += 1;
      drawer?.destroy();
      drawer = null;
      if (!destroyed) status.textContent = `ABSTAIN / ${snapshot.reason ?? snapshot.state}`;
    }
  });
  const unsubscribeSelection = runtime.subscribeSelection(() => {
    textRequestVersion += 1;
    region.dataset.selectionCount = String(++selections);
  });
  async function resolveFixtureProjection() {
    if (scenario === "error") throw new Error("SYNTHETIC_ATLAS_RESOLVER_CANARY");
    return fixtureProjectionForScenario(packet, scenario);
  }
  function consume(update: MapRuntimeEvidenceUpdate): void {
      if (destroyed) return;
      region.dataset.deliveryCount = String(++deliveries);
      drawer?.destroy();
      drawer = null;
      if (update.kind === "RUNTIME_INVALIDATED") {
        status.textContent = `ABSTAIN / ${update.runtimeReason ?? update.runtimeState}`;
        return;
      }
      const result = update.resolution.evidence;
      drawer = mountEvidenceDrawer(drawerHost, result.drawerInput);
      status.textContent = `${result.drawer.outcome} / ${result.code}`;
      drawer.open();
  }
  function bind(): void {
    binding = bindMapRuntimeEvidence(runtime, () => packet.admission, resolveFixtureProjection, consume);
  }
  async function selectWithoutMap(): Promise<void> {
    if (destroyed || runtime.getSnapshot().state !== "READY") return;
    // Same immutable selection, admission gate and resolver as the canvas;
    // this text alternative does not manufacture a renderer selection event.
    binding?.destroy();
    bind();
    const request = ++textRequestVersion;
    const resolution = await resolveMapRuntimeSelectionEvidence(packet.selection, packet.admission, resolveFixtureProjection);
    if (destroyed || request !== textRequestVersion || runtime.getSnapshot().state !== "READY") return;
    region.dataset.textSelectionCount = String(Number(region.dataset.textSelectionCount) + 1);
    consume({ kind: "EVIDENCE_RESOLVED", resolution });
  }
  function changeScenario(): void {
    if (destroyed) return;
    const value = scenarioSelect.value;
    if (!scenarios.some((item) => item === value)) return;
    scenario = value as SyntheticAtlasScenario;
    textRequestVersion += 1;
    binding?.destroy();
    drawer?.destroy();
    drawer = null;
    status.textContent = "ABSTAIN / SELECTION_REQUIRED";
    bind();
  }
  function destroy(): void {
    if (destroyed) return;
    destroyed = true;
    textRequestVersion += 1;
    binding?.destroy();
    drawer?.destroy();
    unsubscribeSelection();
    runtime.dispose();
    unsubscribeSnapshot();
    scenarioSelect.removeEventListener("change", changeScenario);
    textSelector.removeEventListener("click", selectWithoutMap);
    destroyButton.removeEventListener("click", destroy);
    window.removeEventListener("pagehide", destroy);
    scenarioSelect.disabled = true;
    textSelector.disabled = true;
    destroyButton.disabled = true;
    status.textContent = "ABSTAIN / MAP_RUNTIME_DISPOSED";
  }
  bind();
  scenarioSelect.addEventListener("change", changeScenario);
  textSelector.addEventListener("click", selectWithoutMap);
  destroyButton.addEventListener("click", destroy);
  window.addEventListener("pagehide", destroy);
  try {
    await runtime.initialize({ longitude: -98.3, latitude: 38.5, zoom: 5.2, bearing: 0, pitch: 0 });
  } catch {
    status.textContent = "ERROR / MAP_RUNTIME_INITIALIZATION_FAILED";
  }
}

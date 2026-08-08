import {
  mountEvidenceDrawer,
  type EvidenceDrawerController,
} from "../evidence_drawer";
import { resolveFocusComposedClaim } from "./resolver";
import type {
  FocusComposedClaimFixtureCase,
  FocusComposedClaimFixtureController,
  FocusComposedClaimPanelController,
  FocusComposedClaimResolution,
  GovernedFocusComposedClaimResolver,
} from "./types";

const SAFE_ID = /^[A-Za-z0-9][A-Za-z0-9:._/-]{0,159}$/;
const CONTROL_CHARACTER = /[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/;

function isFixtureCase(value: FocusComposedClaimFixtureCase): boolean {
  return (
    SAFE_ID.test(value.caseId) &&
    value.label.length > 0 &&
    value.label.length <= 160 &&
    value.label.trim() === value.label &&
    !CONTROL_CHARACTER.test(value.label)
  );
}

export function mountFocusComposedClaimPanel(
  host: HTMLElement,
  resolution: FocusComposedClaimResolution,
  returnFocus?: HTMLElement | null,
): FocusComposedClaimPanelController {
  const state = resolution.view;
  const document = host.ownerDocument;
  const panel = document.createElement("section");
  const heading = document.createElement("h2");
  const outcome = document.createElement("p");
  const message = document.createElement("p");
  const identityList = document.createElement("ul");
  const dependencyList = document.createElement("ul");
  const evidenceList = document.createElement("ul");
  const citationList = document.createElement("ul");
  const limitationList = document.createElement("ul");
  const receipt = document.createElement("p");
  const drawerHost = document.createElement("div");
  const closeButton = document.createElement("button");
  let closed = false;
  let destroyed = false;
  let drawerController: EvidenceDrawerController | null = null;

  heading.id = "focus-composed-claim-title";
  heading.textContent = state.title;
  outcome.textContent = `${state.outcome} / ${state.code}`;
  outcome.dataset.focusOutcome = state.outcome;
  outcome.dataset.focusCode = state.code;
  message.textContent = state.message;

  identityList.setAttribute("aria-label", "Composed claim identity");
  for (const label of [
    state.claimId === null ? null : `Claim: ${state.claimId}`,
    state.closureId === null ? null : `Closure: ${state.closureId}`,
    state.closureOutcome === null ? null : `Closure outcome: ${state.closureOutcome}`,
  ]) {
    if (label === null) continue;
    const item = document.createElement("li");
    item.textContent = label;
    identityList.append(item);
  }

  dependencyList.setAttribute("aria-label", "Composed claim dependency state");
  for (const label of state.dependencyLabels) {
    const item = document.createElement("li");
    item.textContent = label;
    dependencyList.append(item);
  }

  evidenceList.setAttribute("aria-label", "Focus evidence references");
  for (const evidenceRef of state.evidenceRefs) {
    const item = document.createElement("li");
    item.textContent = evidenceRef;
    evidenceList.append(item);
  }

  citationList.setAttribute("aria-label", "Focus citations");
  for (const citation of state.citations) {
    const item = document.createElement("li");
    const link = document.createElement("a");
    link.href = citation.href;
    link.textContent = citation.label;
    item.append(link);
    citationList.append(item);
  }

  limitationList.setAttribute("aria-label", "Focus limitations");
  for (const limitation of state.limitations) {
    const item = document.createElement("li");
    item.textContent = limitation;
    limitationList.append(item);
  }

  receipt.dataset.component = "focus-process-receipt";
  receipt.textContent =
    state.aiReceiptLabel ?? "No process receipt is exposed for this outcome.";
  closeButton.type = "button";
  closeButton.textContent = "Close Focus Panel";

  panel.dataset.component = "focus-composed-claim-panel";
  panel.dataset.outcome = state.outcome;
  panel.setAttribute("role", "region");
  panel.setAttribute("aria-label", state.accessibilityLabel);
  panel.setAttribute("aria-live", state.ariaLive);
  panel.replaceChildren(
    heading,
    outcome,
    message,
    identityList,
    dependencyList,
    evidenceList,
    citationList,
    limitationList,
    receipt,
    drawerHost,
    closeButton,
  );
  host.replaceChildren(panel);
  drawerController = mountEvidenceDrawer(drawerHost, state.evidenceDrawerInput);

  function close(): void {
    if (closed || destroyed) return;
    closed = true;
    panel.hidden = true;
    if (returnFocus?.isConnected) returnFocus.focus();
  }

  function handleKeydown(event: KeyboardEvent): void {
    if (event.defaultPrevented || event.key !== "Escape" || closed || destroyed) return;
    event.preventDefault();
    close();
  }

  function destroy(): void {
    if (destroyed) return;
    destroyed = true;
    drawerController?.destroy();
    drawerController = null;
    closeButton.removeEventListener("click", close);
    panel.removeEventListener("keydown", handleKeydown);
    host.replaceChildren();
  }

  closeButton.addEventListener("click", close);
  panel.addEventListener("keydown", handleKeydown);
  closeButton.focus();
  return Object.freeze({ state, close, destroy });
}

export function mountFocusComposedClaimFixture(
  host: HTMLElement,
  cases: readonly FocusComposedClaimFixtureCase[],
  resolver: GovernedFocusComposedClaimResolver,
): FocusComposedClaimFixtureController {
  if (cases.length === 0 || !cases.every(isFixtureCase)) {
    throw new Error("Focus composed-claim fixture cases are invalid.");
  }
  if (new Set(cases.map((item) => item.caseId)).size !== cases.length) {
    throw new Error("Focus composed-claim fixture case IDs must be unique.");
  }

  const document = host.ownerDocument;
  const region = document.createElement("section");
  const heading = document.createElement("h2");
  const guidance = document.createElement("p");
  const controls = document.createElement("div");
  const status = document.createElement("p");
  const panelHost = document.createElement("div");
  const buttons = new Map<string, HTMLButtonElement>();
  const listeners = new Map<HTMLButtonElement, () => void>();
  let panelController: FocusComposedClaimPanelController | null = null;
  let requestVersion = 0;
  let destroyed = false;

  heading.id = "focus-composed-claim-fixture-title";
  heading.textContent = "Synthetic composed-claim Focus requests";
  guidance.textContent =
    "Each control submits a bounded synthetic request to an injected governed resolver. No model, source, or lifecycle store is contacted by this feature.";
  controls.setAttribute("aria-label", "Synthetic composed-claim Focus requests");

  for (const item of cases) {
    const button = document.createElement("button");
    button.type = "button";
    button.textContent = item.label;
    button.dataset.focusComposedClaimCase = item.caseId;
    controls.append(button);
    buttons.set(item.caseId, button);
  }

  status.setAttribute("role", "status");
  status.setAttribute("aria-live", "polite");
  status.dataset.component = "focus-composed-claim-status";
  status.textContent = "ABSTAIN / REQUEST_REQUIRED";
  region.dataset.component = "focus-composed-claim-fixture";
  region.setAttribute("aria-labelledby", heading.id);
  region.replaceChildren(heading, guidance, controls, status, panelHost);
  host.replaceChildren(region);

  function setButtonsDisabled(disabled: boolean): void {
    for (const button of buttons.values()) button.disabled = disabled;
  }

  async function select(caseId: string): Promise<FocusComposedClaimResolution | null> {
    const fixtureCase = cases.find((item) => item.caseId === caseId);
    const trigger = buttons.get(caseId);
    if (fixtureCase === undefined || trigger === undefined || destroyed) return null;

    const currentRequest = ++requestVersion;
    setButtonsDisabled(true);
    status.textContent = "Resolving governed composed claim...";
    status.dataset.focusOutcome = "PENDING";

    const result = await resolveFocusComposedClaim(fixtureCase.request, resolver);
    if (destroyed || currentRequest !== requestVersion) return result;

    panelController?.destroy();
    panelController = mountFocusComposedClaimPanel(panelHost, result, trigger);
    status.textContent = `${result.view.outcome} / ${result.code}`;
    status.dataset.focusOutcome = result.view.outcome;
    status.dataset.focusCode = result.code;
    setButtonsDisabled(false);
    return result;
  }

  for (const item of cases) {
    const button = buttons.get(item.caseId);
    if (button === undefined) continue;
    const listener = (): void => {
      void select(item.caseId);
    };
    listeners.set(button, listener);
    button.addEventListener("click", listener);
  }

  function destroy(): void {
    if (destroyed) return;
    destroyed = true;
    requestVersion += 1;
    panelController?.destroy();
    panelController = null;
    for (const [button, listener] of listeners) {
      button.removeEventListener("click", listener);
    }
    host.replaceChildren();
  }

  return Object.freeze({ select, destroy });
}

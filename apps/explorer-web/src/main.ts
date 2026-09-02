import "./site/site-foundation-a.css";
import "./site/site-foundation-b.css";
import "./site/site-map.css";
import "./site/site-catalog.css";
import "./site/site-trust.css";
import "./site/site-responsive.css";
import { mountExplorerSite } from "./site/mount-explorer-site";
import { mountSyntheticFocusWorkspace } from "./site/mount-synthetic-focus-workspace";
import { mountPublicTrustSurface } from "./site/trust-surface";
import {
  mountPublicWorkspaceNavigation,
  resolvePublicEvidenceFreeMapCaseId,
  resolvePublicKnowledgeDomainSelectionTransition,
  sanitizePublicWorkspaceNavigationUrl,
  syncPublicWorkspaceNavigation,
} from "./site/workspace-navigation";
import {
  PUBLIC_MAP_CASE_DEEP_LINK_RETRY_LIMIT,
  isPublicMapCaseRetryGenerationCurrent,
  resolvePublicMapCaseManualSelectionTransition,
  resolvePublicMapCaseRetryPlan,
  resolvePublicMapCaseUrlConsumerCommit,
  resolvePublicMapCaseUrlTransition,
  type PublicMapCaseRetryState,
} from "./site/workspace-map-deep-link";
import {
  PUBLIC_KNOWLEDGE_DOMAIN_DEEP_LINK_RETRY_LIMIT,
  hasSinglePublicKnowledgeDomainConsumer,
  isPublicKnowledgeDomainRetryGenerationCurrent,
  resolvePublicKnowledgeDomainRetryPlan,
  resolvePublicKnowledgeDomainManualSelectionTransition,
  resolvePublicKnowledgeDomainUrlConsumerCommit,
  resolveSinglePublicKnowledgeDomainControlId,
  type PublicKnowledgeDomainRetryState,
} from "./site/workspace-knowledge-deep-link";

const root = document.querySelector<HTMLElement>("#root");

if (root === null) {
  throw new Error("Explorer Web root element is missing.");
}

const site = mountExplorerSite(root);
const navigation = root.querySelector<HTMLElement>(".site-nav");
const trustSection = root.querySelector<HTMLElement>("#trust");

if (navigation === null || trustSection === null) {
  site.destroy();
  throw new Error("Explorer workspace composition mount is missing.");
}

mountPublicWorkspaceNavigation(navigation);
let activeDeepLinkMapCaseId: "missing" | null = null;
let activeDeepLinkKnowledgeDomainId: string | null = null;
let pendingMapDeepLinkRetry: number | null = null;
let pendingKnowledgeDomainDeepLinkRetry: number | null = null;
let mapDeepLinkRetryGeneration = 0;
let knowledgeDomainDeepLinkRetryGeneration = 0;
let mapDeepLinkRetryState: PublicMapCaseRetryState = Object.freeze({
  attemptsRemaining: PUBLIC_MAP_CASE_DEEP_LINK_RETRY_LIMIT,
  urlHref: null,
});
let knowledgeDomainDeepLinkRetryState: PublicKnowledgeDomainRetryState =
  Object.freeze({
    attemptsRemaining: PUBLIC_KNOWLEDGE_DOMAIN_DEEP_LINK_RETRY_LIMIT,
    urlHref: null,
  });

const cancelPendingMapDeepLinkRetry = (): void => {
  mapDeepLinkRetryGeneration += 1;
  if (pendingMapDeepLinkRetry !== null) {
    window.clearTimeout(pendingMapDeepLinkRetry);
  }
  pendingMapDeepLinkRetry = null;
  mapDeepLinkRetryState = Object.freeze({
    attemptsRemaining: PUBLIC_MAP_CASE_DEEP_LINK_RETRY_LIMIT,
    urlHref: null,
  });
};

const scheduleMapDeepLinkRetry = (url: URL): void => {
  if (pendingMapDeepLinkRetry !== null) return;
  const retryPlan = resolvePublicMapCaseRetryPlan(
    mapDeepLinkRetryState,
    url.href,
  );
  mapDeepLinkRetryState = retryPlan;
  if (!retryPlan.shouldSchedule) return;
  mapDeepLinkRetryGeneration += 1;
  const retryGeneration = mapDeepLinkRetryGeneration;
  pendingMapDeepLinkRetry = window.setTimeout(() => {
    if (
      !isPublicMapCaseRetryGenerationCurrent(
        mapDeepLinkRetryGeneration,
        retryGeneration,
      )
    ) {
      return;
    }
    pendingMapDeepLinkRetry = null;
    if (window.location.href !== retryPlan.urlHref) {
      cancelPendingMapDeepLinkRetry();
      return;
    }
    syncWorkspaceNavigation();
  }, 16);
};

const cancelPendingKnowledgeDomainDeepLinkRetry = (): void => {
  knowledgeDomainDeepLinkRetryGeneration += 1;
  if (pendingKnowledgeDomainDeepLinkRetry !== null) {
    window.clearTimeout(pendingKnowledgeDomainDeepLinkRetry);
  }
  pendingKnowledgeDomainDeepLinkRetry = null;
  knowledgeDomainDeepLinkRetryState = Object.freeze({
    attemptsRemaining: PUBLIC_KNOWLEDGE_DOMAIN_DEEP_LINK_RETRY_LIMIT,
    urlHref: null,
  });
};

const scheduleKnowledgeDomainDeepLinkRetry = (url: URL): void => {
  if (pendingKnowledgeDomainDeepLinkRetry !== null) return;
  const retryPlan = resolvePublicKnowledgeDomainRetryPlan(
    knowledgeDomainDeepLinkRetryState,
    url.href,
  );
  knowledgeDomainDeepLinkRetryState = retryPlan;
  if (!retryPlan.shouldSchedule) return;
  knowledgeDomainDeepLinkRetryGeneration += 1;
  const retryGeneration = knowledgeDomainDeepLinkRetryGeneration;
  pendingKnowledgeDomainDeepLinkRetry = window.setTimeout(() => {
    if (
      !isPublicKnowledgeDomainRetryGenerationCurrent(
        knowledgeDomainDeepLinkRetryGeneration,
        retryGeneration,
      )
    ) {
      return;
    }
    pendingKnowledgeDomainDeepLinkRetry = null;
    if (window.location.href !== retryPlan.urlHref) {
      cancelPendingKnowledgeDomainDeepLinkRetry();
      return;
    }
    syncWorkspaceNavigation();
  }, 16);
};

const releaseDeepLinkMapOwnershipOnManualSelection = (event: MouseEvent): void => {
  const button =
    event.target instanceof Element
      ? event.target.closest<HTMLButtonElement>("button[data-map-evidence-case]")
      : null;
  const caseId = button?.dataset.mapEvidenceCase;
  if (button === null || caseId === undefined || !root.contains(button)) return;

  const currentUrl = new URL(window.location.href);
  const transition = resolvePublicMapCaseManualSelectionTransition(
    currentUrl,
    activeDeepLinkMapCaseId,
    caseId,
    button.disabled,
  );
  activeDeepLinkMapCaseId = transition.activeDeepLinkMapCaseId;
  if (
    transition.replacementUrl !== null &&
    transition.replacementUrl.href !== currentUrl.href
  ) {
    cancelPendingMapDeepLinkRetry();
    window.history.replaceState(
      window.history.state,
      "",
      transition.replacementUrl.toString(),
    );
    syncPublicWorkspaceNavigation(navigation, transition.replacementUrl);
  }
};
root.addEventListener("click", releaseDeepLinkMapOwnershipOnManualSelection);

const releaseDeepLinkKnowledgeOwnershipOnManualSelection = (
  event: MouseEvent,
): void => {
  const button =
    event.target instanceof Element
      ? event.target.closest<HTMLButtonElement>("button[data-domain-id]")
      : null;
  const domainId = button?.dataset.domainId;
  if (button === null || domainId === undefined || !root.contains(button)) return;

  const currentUrl = new URL(window.location.href);
  const transition = resolvePublicKnowledgeDomainManualSelectionTransition(
    currentUrl,
    activeDeepLinkKnowledgeDomainId,
    domainId,
    !button.disabled && button.getAttribute("aria-pressed") === "true",
  );
  activeDeepLinkKnowledgeDomainId = transition.activeDeepLinkDomainId;
  if (
    transition.replacementUrl !== null &&
    transition.replacementUrl.href !== currentUrl.href
  ) {
    cancelPendingKnowledgeDomainDeepLinkRetry();
    window.history.replaceState(
      window.history.state,
      "",
      transition.replacementUrl.toString(),
    );
    syncPublicWorkspaceNavigation(navigation, transition.replacementUrl);
  }
};
root.addEventListener(
  "click",
  releaseDeepLinkKnowledgeOwnershipOnManualSelection,
);

const syncWorkspaceNavigation = (): void => {
  const currentUrl = new URL(window.location.href);
  const safeUrl = sanitizePublicWorkspaceNavigationUrl(currentUrl);
  if (safeUrl.href !== currentUrl.href) {
    window.history.replaceState(window.history.state, "", safeUrl.toString());
  }
  syncPublicWorkspaceNavigation(navigation, safeUrl);

  const mapTransition = resolvePublicMapCaseUrlTransition(
    safeUrl,
    activeDeepLinkMapCaseId,
  );
  if (mapTransition.releaseOwnedSelection) {
    cancelPendingMapDeepLinkRetry();
  }
  const mapCaseId = mapTransition.mapCaseIdToSelect;
  if (mapCaseId !== null) {
    const mapCaseButton = root.querySelector<HTMLButtonElement>(
      `button[data-map-evidence-case="${mapCaseId}"]`,
    );
    if (mapCaseButton === null || mapCaseButton.disabled) {
      scheduleMapDeepLinkRetry(safeUrl);
    } else {
      const priorFocus =
        document.activeElement instanceof HTMLElement
          ? document.activeElement
          : null;
      mapCaseButton.click();
      const selectionApplied = mapCaseButton.disabled;
      activeDeepLinkMapCaseId = resolvePublicMapCaseUrlConsumerCommit(
        mapTransition,
        selectionApplied,
      );
      if (selectionApplied) cancelPendingMapDeepLinkRetry();
      if (priorFocus?.isConnected) priorFocus.focus();
    }
  } else {
    activeDeepLinkMapCaseId = resolvePublicMapCaseUrlConsumerCommit(
      mapTransition,
      false,
    );
    if (activeDeepLinkMapCaseId === null) cancelPendingMapDeepLinkRetry();
  }

  const currentDomainId = resolveSinglePublicKnowledgeDomainControlId(
    Array.from(
      root.querySelectorAll<HTMLButtonElement>(
        'button[data-domain-id][aria-pressed="true"]',
      ),
    ).map((button) => button.dataset.domainId),
  );
  const domainTransition = resolvePublicKnowledgeDomainSelectionTransition(
    safeUrl,
    activeDeepLinkKnowledgeDomainId,
    currentDomainId,
  );
  const domainIdToSelect = domainTransition.domainIdToSelect;
  const requestedDomainId = domainTransition.activeDeepLinkDomainId;
  const domainConsumerId = domainIdToSelect ?? requestedDomainId;
  const domainButtons = Array.from(
    root.querySelectorAll<HTMLButtonElement>("button[data-domain-id]"),
  );
  const domainConsumerIsUnique =
    domainConsumerId !== null &&
    hasSinglePublicKnowledgeDomainConsumer(
      domainButtons.map((button) => button.dataset.domainId),
      domainConsumerId,
    );
  const domainButton =
    !domainConsumerIsUnique
      ? undefined
      : domainButtons.find(
          (button) => button.dataset.domainId === domainConsumerId,
        );
  const consumerReady = domainButton !== undefined && !domainButton.disabled;
  if (requestedDomainId !== null && !consumerReady) {
    scheduleKnowledgeDomainDeepLinkRetry(safeUrl);
  }
  if (domainIdToSelect !== null) {
    if (consumerReady) {
      // Provisional ownership keeps the programmatic click from looking like a
      // manual selection to the delegated release listener. The observed DOM
      // state below is still authoritative for the final commit.
      activeDeepLinkKnowledgeDomainId =
        domainTransition.activeDeepLinkDomainId;
    }
    if (
      domainButton !== undefined &&
      !domainButton.disabled &&
      domainButton.getAttribute("aria-pressed") !== "true"
    ) {
      const priorFocus =
        document.activeElement instanceof HTMLElement
          ? document.activeElement
          : null;
      domainButton.click();
      if (priorFocus?.isConnected) priorFocus.focus();
    }
  }
  const selectedDomainId = resolveSinglePublicKnowledgeDomainControlId(
    Array.from(
      root.querySelectorAll<HTMLButtonElement>(
        'button[data-domain-id][aria-pressed="true"]',
      ),
    ).map((button) => button.dataset.domainId),
  );
  activeDeepLinkKnowledgeDomainId =
    resolvePublicKnowledgeDomainUrlConsumerCommit(
      domainTransition,
      selectedDomainId,
      requestedDomainId === null || consumerReady,
    );
  if (activeDeepLinkKnowledgeDomainId !== null || requestedDomainId === null) {
    cancelPendingKnowledgeDomainDeepLinkRetry();
  }
};
const syncWorkspaceNavigationFromBrowser = (): void => {
  cancelPendingMapDeepLinkRetry();
  cancelPendingKnowledgeDomainDeepLinkRetry();
  syncWorkspaceNavigation();
};
syncWorkspaceNavigationFromBrowser();
window.addEventListener("hashchange", syncWorkspaceNavigationFromBrowser);
window.addEventListener("popstate", syncWorkspaceNavigationFromBrowser);

mountSyntheticFocusWorkspace(root);

const trustSurfaceHost = document.createElement("div");
trustSurfaceHost.className = "trust-surface-host";
trustSection.insertBefore(trustSurfaceHost, trustSection.children.item(1));
mountPublicTrustSurface(trustSurfaceHost);

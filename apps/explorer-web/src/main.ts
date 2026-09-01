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
import { resolvePublicMapCaseManualSelectionTransition } from "./site/workspace-map-deep-link";

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
  );
  activeDeepLinkMapCaseId = transition.activeDeepLinkMapCaseId;
  if (
    transition.replacementUrl !== null &&
    transition.replacementUrl.href !== currentUrl.href
  ) {
    window.history.replaceState(
      window.history.state,
      "",
      transition.replacementUrl.toString(),
    );
    syncPublicWorkspaceNavigation(navigation, transition.replacementUrl);
  }
};
root.addEventListener("click", releaseDeepLinkMapOwnershipOnManualSelection);

const syncWorkspaceNavigation = (): void => {
  const currentUrl = new URL(window.location.href);
  const safeUrl = sanitizePublicWorkspaceNavigationUrl(currentUrl);
  if (safeUrl.href !== currentUrl.href) {
    window.history.replaceState(window.history.state, "", safeUrl.toString());
  }
  syncPublicWorkspaceNavigation(navigation, safeUrl);

  const mapCaseId = resolvePublicEvidenceFreeMapCaseId(safeUrl);
  if (mapCaseId === null) {
    activeDeepLinkMapCaseId = null;
  } else if (mapCaseId !== activeDeepLinkMapCaseId) {
    const mapCaseButton = root.querySelector<HTMLButtonElement>(
      `button[data-map-evidence-case="${mapCaseId}"]`,
    );
    if (mapCaseButton !== null) {
      const priorFocus =
        document.activeElement instanceof HTMLElement
          ? document.activeElement
          : null;
      activeDeepLinkMapCaseId = mapCaseId;
      mapCaseButton.click();
      if (priorFocus?.isConnected) priorFocus.focus();
    }
  }

  const currentDomainId =
    root.querySelector<HTMLButtonElement>(
      'button[data-domain-id][aria-pressed="true"]',
    )?.dataset.domainId ?? null;
  const domainTransition = resolvePublicKnowledgeDomainSelectionTransition(
    safeUrl,
    activeDeepLinkKnowledgeDomainId,
    currentDomainId,
  );
  activeDeepLinkKnowledgeDomainId = domainTransition.activeDeepLinkDomainId;
  const domainIdToSelect = domainTransition.domainIdToSelect;
  if (domainIdToSelect !== null) {
    const domainButton = Array.from(
      root.querySelectorAll<HTMLButtonElement>("button[data-domain-id]"),
    ).find((button) => button.dataset.domainId === domainIdToSelect);
    if (
      domainButton !== undefined &&
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
};
syncWorkspaceNavigation();
window.addEventListener("hashchange", syncWorkspaceNavigation);
window.addEventListener("popstate", syncWorkspaceNavigation);

mountSyntheticFocusWorkspace(root);

const trustSurfaceHost = document.createElement("div");
trustSurfaceHost.className = "trust-surface-host";
trustSection.insertBefore(trustSurfaceHost, trustSection.children.item(1));
mountPublicTrustSurface(trustSurfaceHost);

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
  resolveSinglePublicKnowledgeDomainId,
  sanitizePublicWorkspaceNavigationUrl,
  syncPublicWorkspaceNavigation,
} from "./site/workspace-navigation";

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
const syncWorkspaceNavigation = (): void => {
  const currentUrl = new URL(window.location.href);
  const safeUrl = sanitizePublicWorkspaceNavigationUrl(currentUrl);
  if (safeUrl.href !== currentUrl.href) {
    window.history.replaceState(window.history.state, "", safeUrl.toString());
  }
  syncPublicWorkspaceNavigation(navigation, safeUrl);

  const domainId = resolveSinglePublicKnowledgeDomainId(safeUrl);
  if (domainId !== null) {
    const domainButton = Array.from(
      root.querySelectorAll<HTMLButtonElement>("button[data-domain-id]"),
    ).find((button) => button.dataset.domainId === domainId);
    if (domainButton?.getAttribute("aria-pressed") !== "true") {
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

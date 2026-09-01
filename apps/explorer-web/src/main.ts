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
  syncPublicWorkspaceNavigation(navigation, new URL(window.location.href));
};
syncWorkspaceNavigation();
window.addEventListener("hashchange", syncWorkspaceNavigation);
window.addEventListener("popstate", syncWorkspaceNavigation);

mountSyntheticFocusWorkspace(root);

const trustSurfaceHost = document.createElement("div");
trustSurfaceHost.className = "trust-surface-host";
trustSection.insertBefore(trustSurfaceHost, trustSection.children.item(1));
mountPublicTrustSurface(trustSurfaceHost);

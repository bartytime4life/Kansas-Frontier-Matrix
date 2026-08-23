import "./site/site-foundation-a.css";
import "./site/site-foundation-b.css";
import "./site/site-map.css";
import "./site/site-catalog.css";
import "./site/site-responsive.css";
import { mountExplorerSite } from "./site/mount-explorer-site";
import { mountSyntheticFocusWorkspace } from "./site/mount-synthetic-focus-workspace";
import { mountPublicWorkspaceNavigation } from "./site/workspace-navigation";

const root = document.querySelector<HTMLElement>("#root");

if (root === null) {
  throw new Error("Explorer Web root element is missing.");
}

const site = mountExplorerSite(root);
const navigation = root.querySelector<HTMLElement>(".site-nav");

if (navigation === null) {
  site.destroy();
  throw new Error("Explorer workspace navigation mount is missing.");
}

mountPublicWorkspaceNavigation(navigation);
mountSyntheticFocusWorkspace(root);

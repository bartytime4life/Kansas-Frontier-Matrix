import { PUBLIC_WORKSPACES } from "./workspace-registry";

export const PUBLIC_WORKSPACE_NAVIGATION_PROFILE =
  "kfm.explorer.public-workspace-navigation.v1" as const;

/**
 * Project the public workspace registry into the existing anchor navigation.
 * This replaces display links only; it creates no routes or privileged actions.
 */
export function mountPublicWorkspaceNavigation(nav: HTMLElement): void {
  const document = nav.ownerDocument;
  const fragment = document.createDocumentFragment();

  PUBLIC_WORKSPACES.forEach((workspace) => {
    const link = document.createElement("a");
    link.textContent = workspace.navLabel;
    link.href = workspace.href;
    link.dataset.workspaceId = workspace.id;
    fragment.append(link);
  });

  nav.setAttribute("aria-label", "Explorer workspaces");
  nav.dataset.workspaceNavigationProfile = PUBLIC_WORKSPACE_NAVIGATION_PROFILE;
  nav.replaceChildren(fragment);
}

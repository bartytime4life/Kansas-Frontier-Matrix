import {
  PUBLIC_WORKSPACE_CONTEXT_QUERY_PARAM,
  parsePublicWorkspaceContextUrl,
} from "./workspace-context";
import {
  PUBLIC_WORKSPACES,
  findPublicWorkspaceByHash,
  type PublicWorkspaceId,
} from "./workspace-registry";

export const PUBLIC_WORKSPACE_NAVIGATION_PROFILE =
  "kfm.explorer.public-workspace-navigation.v1" as const;

export type PublicWorkspaceNavigationContextState =
  | "PUBLIC_CONTEXT_MATCHED"
  | "ANCHOR_ONLY"
  | "UNRESOLVED";

export type PublicWorkspaceNavigationState = Readonly<{
  workspaceId: PublicWorkspaceId | null;
  contextState: PublicWorkspaceNavigationContextState;
}>;

/**
 * Resolve one browser URL against the existing public workspace registry and
 * public-safe context parser. A valid context must already match its section
 * anchor; rejected or absent context can only fall back to ordinary public
 * anchor navigation.
 */
export function resolvePublicWorkspaceNavigationState(
  url: URL,
): PublicWorkspaceNavigationState {
  const context = parsePublicWorkspaceContextUrl(url);
  const anchorWorkspace = findPublicWorkspaceByHash(url.hash);

  return Object.freeze({
    workspaceId: context?.workspaceId ?? anchorWorkspace?.id ?? null,
    contextState:
      context !== null
        ? "PUBLIC_CONTEXT_MATCHED"
        : anchorWorkspace !== null
          ? "ANCHOR_ONLY"
          : "UNRESOLVED",
  });
}

/**
 * Clone one browser URL and remove only a rejected KFM public-context query.
 *
 * The strict context parser already rejects malformed, duplicate, oversized,
 * evidence-bearing, private, or hash-mismatched projections. Keeping a rejected
 * projection in the address bar would leave stale or sensitive-looking values
 * in browser history and copied links even though Explorer refuses to consume
 * them. This helper preserves unrelated query parameters and the public anchor.
 */
export function sanitizePublicWorkspaceNavigationUrl(url: URL): URL {
  const safeUrl = new URL(url.toString());
  if (
    safeUrl.searchParams.has(PUBLIC_WORKSPACE_CONTEXT_QUERY_PARAM) &&
    parsePublicWorkspaceContextUrl(safeUrl) === null
  ) {
    safeUrl.searchParams.delete(PUBLIC_WORKSPACE_CONTEXT_QUERY_PARAM);
  }
  return safeUrl;
}

/**
 * Return one explicit public Knowledge-domain selection from a validated deep
 * link. Multi-domain context is intentionally not collapsed into an arbitrary
 * primary domain, and non-Knowledge or rejected context produces no selection.
 * The returned value is only the catalog-bounded public domain identifier.
 */
export function resolveSinglePublicKnowledgeDomainId(url: URL): string | null {
  const context = parsePublicWorkspaceContextUrl(url);
  if (
    context?.workspaceId !== "knowledge" ||
    context.domainIds.length !== 1
  ) {
    return null;
  }
  return context.domainIds[0] ?? null;
}

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

/**
 * Synchronize the visible workspace navigation with one public browser URL.
 * Only the registered workspace ID is projected into DOM state; no layer,
 * selection, evidence, camera, place, time, compare, or story payload is copied.
 */
export function syncPublicWorkspaceNavigation(
  nav: HTMLElement,
  url: URL,
): PublicWorkspaceNavigationState {
  const state = resolvePublicWorkspaceNavigationState(url);

  nav.querySelectorAll<HTMLAnchorElement>("a[data-workspace-id]").forEach((link) => {
    const isCurrent =
      state.workspaceId !== null &&
      link.dataset.workspaceId === state.workspaceId;
    if (isCurrent) {
      link.setAttribute("aria-current", "page");
    } else {
      link.removeAttribute("aria-current");
    }
  });

  nav.dataset.workspaceContextState = state.contextState;
  return state;
}

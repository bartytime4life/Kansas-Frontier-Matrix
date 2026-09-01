import { PUBLIC_WORKSPACE_CONTEXT_QUERY_PARAM } from "./workspace-context";
import { resolvePublicEvidenceFreeMapCaseId } from "./workspace-navigation";

export const PUBLIC_MAP_CASE_DEEP_LINK_RELEASE_PROFILE =
  "kfm.explorer.public-map-case-deep-link-release.v1" as const;

export type PublicMapCaseDeepLinkRelease = Readonly<{
  activeDeepLinkMapCaseId: "missing" | null;
  replacementUrl: URL | null;
  reason: "UNCHANGED" | "RELEASED" | "STALE_OWNER";
}>;

export type PublicMapCaseUrlTransition = Readonly<{
  activeDeepLinkMapCaseId: "missing" | null;
  mapCaseIdToSelect: "missing" | null;
  resetOwnedSelection: boolean;
}>;

/**
 * Reconcile the synthetic map fixture that is still owned by public URL state.
 *
 * Departing from an active deep link asks the site controller to reset the
 * owned fixture, which invalidates any in-flight request and removes its
 * Evidence Drawer. Manual selection releases ownership before URL
 * synchronization, so a user's later fixture remains visible.
 */
export function resolvePublicMapCaseUrlTransition(
  url: URL,
  activeDeepLinkMapCaseId: "missing" | null,
): PublicMapCaseUrlTransition {
  const requestedMapCaseId = resolvePublicEvidenceFreeMapCaseId(url);
  if (requestedMapCaseId !== null) {
    return Object.freeze({
      activeDeepLinkMapCaseId: requestedMapCaseId,
      mapCaseIdToSelect:
        requestedMapCaseId === activeDeepLinkMapCaseId
          ? null
          : requestedMapCaseId,
      resetOwnedSelection: false,
    });
  }

  return Object.freeze({
    activeDeepLinkMapCaseId: null,
    mapCaseIdToSelect: null,
    resetOwnedSelection: activeDeepLinkMapCaseId !== null,
  });
}

/**
 * Release URL ownership when a user manually selects another synthetic map
 * fixture while the public-safe evidence-free deep link owns the `missing`
 * case. The replacement URL removes only `kfm-context`; it never serializes the
 * newly selected fixture, EvidenceRefs, feature properties, or protected state.
 *
 * A programmatic click restoring the same `missing` case leaves the deep link
 * intact. If the tracked owner is already stale relative to the current URL,
 * ownership is dropped without rewriting unrelated browser state.
 */
export function resolvePublicMapCaseManualSelectionTransition(
  url: URL,
  activeDeepLinkMapCaseId: "missing" | null,
  selectedCaseId: string,
): PublicMapCaseDeepLinkRelease {
  if (activeDeepLinkMapCaseId === null) {
    return Object.freeze({
      activeDeepLinkMapCaseId: null,
      replacementUrl: null,
      reason: "UNCHANGED",
    });
  }

  if (resolvePublicEvidenceFreeMapCaseId(url) !== activeDeepLinkMapCaseId) {
    return Object.freeze({
      activeDeepLinkMapCaseId: null,
      replacementUrl: null,
      reason: "STALE_OWNER",
    });
  }

  if (selectedCaseId === activeDeepLinkMapCaseId) {
    return Object.freeze({
      activeDeepLinkMapCaseId,
      replacementUrl: null,
      reason: "UNCHANGED",
    });
  }

  const replacementUrl = new URL(url.toString());
  replacementUrl.searchParams.delete(PUBLIC_WORKSPACE_CONTEXT_QUERY_PARAM);
  return Object.freeze({
    activeDeepLinkMapCaseId: null,
    replacementUrl,
    reason: "RELEASED",
  });
}

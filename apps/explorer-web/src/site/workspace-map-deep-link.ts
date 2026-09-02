import { PUBLIC_WORKSPACE_CONTEXT_QUERY_PARAM } from "./workspace-context";
import { resolvePublicEvidenceFreeMapCaseId } from "./workspace-navigation";

export const PUBLIC_MAP_CASE_DEEP_LINK_RELEASE_PROFILE =
  "kfm.explorer.public-map-case-deep-link-release.v1" as const;

export const PUBLIC_MAP_CASE_DEEP_LINK_RETRY_LIMIT = 8 as const;

export type PublicMapCaseRetryState = Readonly<{
  attemptsRemaining: number;
  urlHref: string | null;
}>;

export type PublicMapCaseRetryPlan = PublicMapCaseRetryState &
  Readonly<{ shouldSchedule: boolean }>;

export type PublicMapCaseDeepLinkRelease = Readonly<{
  activeDeepLinkMapCaseId: "missing" | null;
  replacementUrl: URL | null;
  reason: "UNCHANGED" | "RELEASED" | "STALE_OWNER";
}>;

export type PublicMapCaseUrlTransition = Readonly<{
  activeDeepLinkMapCaseId: "missing" | null;
  mapCaseIdToSelect: "missing" | null;
  releaseOwnedSelection: boolean;
}>;

/**
 * Reserve one finite retry for a disabled public map-selection control.
 * A different URL receives a fresh budget; exhausting the budget fails closed
 * with no timer rather than polling indefinitely or claiming URL ownership.
 */
export function resolvePublicMapCaseRetryPlan(
  state: PublicMapCaseRetryState,
  requestedUrlHref: string,
): PublicMapCaseRetryPlan {
  const attemptsRemaining =
    state.urlHref === requestedUrlHref
      ? state.attemptsRemaining
      : PUBLIC_MAP_CASE_DEEP_LINK_RETRY_LIMIT;
  if (attemptsRemaining <= 0) {
    return Object.freeze({
      attemptsRemaining: 0,
      urlHref: requestedUrlHref,
      shouldSchedule: false,
    });
  }
  return Object.freeze({
    attemptsRemaining: attemptsRemaining - 1,
    urlHref: requestedUrlHref,
    shouldSchedule: true,
  });
}

/**
 * Commit URL ownership only after the fixture control accepted the requested
 * selection. A disabled control ignores `click()`, so retaining the prior
 * owner keeps the URL request retryable instead of falsely claiming that its
 * Evidence Drawer was restored.
 */
export function resolvePublicMapCaseUrlConsumerCommit(
  transition: PublicMapCaseUrlTransition,
  selectionApplied: boolean,
): "missing" | null {
  if (transition.mapCaseIdToSelect === null || !selectionApplied) {
    return transition.activeDeepLinkMapCaseId;
  }
  return transition.mapCaseIdToSelect;
}

/**
 * Reconcile the synthetic map fixture that is still owned by public URL state.
 *
 * Departing from an active deep link releases consumer ownership. Fixture
 * lifecycle remains producer-owned; this consumer cancels its own pending
 * retry without independently remounting or reinterpreting the fixture.
 */
export function resolvePublicMapCaseUrlTransition(
  url: URL,
  activeDeepLinkMapCaseId: "missing" | null,
): PublicMapCaseUrlTransition {
  const requestedMapCaseId = resolvePublicEvidenceFreeMapCaseId(url);
  if (requestedMapCaseId !== null) {
    return Object.freeze({
      activeDeepLinkMapCaseId,
      mapCaseIdToSelect:
        requestedMapCaseId === activeDeepLinkMapCaseId
          ? null
          : requestedMapCaseId,
      releaseOwnedSelection: false,
    });
  }

  return Object.freeze({
    activeDeepLinkMapCaseId: null,
    mapCaseIdToSelect: null,
    releaseOwnedSelection: activeDeepLinkMapCaseId !== null,
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

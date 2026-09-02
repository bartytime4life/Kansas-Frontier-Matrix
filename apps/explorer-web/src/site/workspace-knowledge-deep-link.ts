import { PUBLIC_WORKSPACE_CONTEXT_QUERY_PARAM } from "./workspace-context";
import {
  resolveSinglePublicKnowledgeDomainId,
  type PublicKnowledgeDomainSelectionTransition,
} from "./workspace-navigation";

export const PUBLIC_KNOWLEDGE_DOMAIN_DEEP_LINK_RELEASE_PROFILE =
  "kfm.explorer.public-knowledge-domain-deep-link-release.v1" as const;

export const PUBLIC_KNOWLEDGE_DOMAIN_DEEP_LINK_RETRY_LIMIT = 8 as const;

export type PublicKnowledgeDomainRetryState = Readonly<{
  attemptsRemaining: number;
  urlHref: string | null;
}>;

export type PublicKnowledgeDomainRetryPlan = PublicKnowledgeDomainRetryState &
  Readonly<{ shouldSchedule: boolean }>;

export type PublicKnowledgeDomainDeepLinkRelease = Readonly<{
  activeDeepLinkDomainId: string | null;
  replacementUrl: URL | null;
  reason: "UNCHANGED" | "RELEASED" | "STALE_OWNER";
}>;

/**
 * Resolve visible Knowledge state only when exactly one control reports the
 * selection. Responsive or repeated mounts must not turn DOM order into
 * catalog authority.
 */
export function resolveSinglePublicKnowledgeDomainControlId(
  selectedDomainIds: readonly (string | undefined)[],
): string | null {
  if (selectedDomainIds.length !== 1) return null;
  const selectedDomainId = selectedDomainIds[0];
  return selectedDomainId === undefined || selectedDomainId.length === 0
    ? null
    : selectedDomainId;
}

/**
 * A URL request has one truthful consumer only when exactly one mounted
 * Knowledge control carries the requested catalog identifier.
 */
export function hasSinglePublicKnowledgeDomainConsumer(
  mountedDomainIds: readonly (string | undefined)[],
  requestedDomainId: string,
): boolean {
  return (
    mountedDomainIds.filter((domainId) => domainId === requestedDomainId)
      .length === 1
  );
}

/**
 * Reserve one finite retry for a Knowledge-domain control that is absent or
 * disabled while its validated public URL request is pending. A different URL
 * receives a fresh budget; exhaustion fails closed without polling forever or
 * claiming that the requested catalog domain became visible.
 */
export function resolvePublicKnowledgeDomainRetryPlan(
  state: PublicKnowledgeDomainRetryState,
  requestedUrlHref: string,
): PublicKnowledgeDomainRetryPlan {
  const attemptsRemaining =
    state.urlHref === requestedUrlHref
      ? state.attemptsRemaining
      : PUBLIC_KNOWLEDGE_DOMAIN_DEEP_LINK_RETRY_LIMIT;
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
 * Accept a scheduled retry callback only while it still owns the active local
 * generation. Navigation, manual release, or a newer retry invalidates older
 * callbacks so they cannot clear a replacement timer or resynchronize stale
 * URL state.
 */
export function isPublicKnowledgeDomainRetryGenerationCurrent(
  activeGeneration: number,
  callbackGeneration: number,
): boolean {
  return activeGeneration === callbackGeneration;
}

/**
 * Commit URL ownership only after the existing Knowledge control is enabled
 * and visibly applies the requested domain. This readiness proof is required
 * even when the requested domain was already selected before synchronization;
 * an absent, disabled, or ineffective control leaves ownership clear and
 * retryable instead of treating an unavailable consumer as restored.
 */
export function resolvePublicKnowledgeDomainUrlConsumerCommit(
  transition: PublicKnowledgeDomainSelectionTransition,
  selectedDomainId: string | null,
  consumerReady: boolean,
): string | null {
  if (transition.activeDeepLinkDomainId !== null && !consumerReady) {
    return null;
  }
  if (
    transition.domainIdToSelect !== null &&
    selectedDomainId !== transition.domainIdToSelect
  ) {
    return null;
  }
  return transition.activeDeepLinkDomainId;
}

/**
 * Release URL ownership when a user manually selects another Knowledge domain
 * while a validated public deep link owns the visible domain selection. The
 * replacement URL removes only `kfm-context`; it never serializes the new
 * domain or any unconsumed context dimension.
 *
 * A programmatic click restoring the URL-owned domain leaves the deep link
 * intact. A successful different manual choice also releases a still-pending
 * URL request before ownership has committed, keeping visible selection and
 * the address bar coherent. If the tracked owner is already stale relative to
 * the current URL, ownership is dropped without rewriting unrelated state.
 */
export function resolvePublicKnowledgeDomainManualSelectionTransition(
  url: URL,
  activeDeepLinkDomainId: string | null,
  selectedDomainId: string,
  selectionApplied: boolean,
): PublicKnowledgeDomainDeepLinkRelease {
  const requestedDomainId = resolveSinglePublicKnowledgeDomainId(url);
  if (activeDeepLinkDomainId === null) {
    if (
      selectionApplied &&
      requestedDomainId !== null &&
      selectedDomainId !== requestedDomainId
    ) {
      const replacementUrl = new URL(url.toString());
      replacementUrl.searchParams.delete(PUBLIC_WORKSPACE_CONTEXT_QUERY_PARAM);
      return Object.freeze({
        activeDeepLinkDomainId: null,
        replacementUrl,
        reason: "RELEASED",
      });
    }
    return Object.freeze({
      activeDeepLinkDomainId: null,
      replacementUrl: null,
      reason: "UNCHANGED",
    });
  }

  if (requestedDomainId !== activeDeepLinkDomainId) {
    return Object.freeze({
      activeDeepLinkDomainId: null,
      replacementUrl: null,
      reason: "STALE_OWNER",
    });
  }

  if (!selectionApplied) {
    return Object.freeze({
      activeDeepLinkDomainId,
      replacementUrl: null,
      reason: "UNCHANGED",
    });
  }

  if (selectedDomainId === activeDeepLinkDomainId) {
    return Object.freeze({
      activeDeepLinkDomainId,
      replacementUrl: null,
      reason: "UNCHANGED",
    });
  }

  const replacementUrl = new URL(url.toString());
  replacementUrl.searchParams.delete(PUBLIC_WORKSPACE_CONTEXT_QUERY_PARAM);
  return Object.freeze({
    activeDeepLinkDomainId: null,
    replacementUrl,
    reason: "RELEASED",
  });
}

import { PUBLIC_WORKSPACE_CONTEXT_QUERY_PARAM } from "./workspace-context";
import {
  resolveSinglePublicKnowledgeDomainId,
  type PublicKnowledgeDomainSelectionTransition,
} from "./workspace-navigation";

export const PUBLIC_KNOWLEDGE_DOMAIN_DEEP_LINK_RELEASE_PROFILE =
  "kfm.explorer.public-knowledge-domain-deep-link-release.v1" as const;

export type PublicKnowledgeDomainDeepLinkRelease = Readonly<{
  activeDeepLinkDomainId: string | null;
  replacementUrl: URL | null;
  reason: "UNCHANGED" | "RELEASED" | "STALE_OWNER";
}>;

/**
 * Commit URL ownership only after the existing Knowledge controls visibly
 * apply a newly requested domain. An absent, disabled, or ineffective control
 * leaves ownership clear, allowing later synchronization to retry instead of
 * treating an unrendered domain as restored.
 */
export function resolvePublicKnowledgeDomainUrlConsumerCommit(
  transition: PublicKnowledgeDomainSelectionTransition,
  selectedDomainId: string | null,
): string | null {
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
 * intact. If the tracked owner is already stale relative to the current URL,
 * ownership is dropped without rewriting unrelated browser state.
 */
export function resolvePublicKnowledgeDomainManualSelectionTransition(
  url: URL,
  activeDeepLinkDomainId: string | null,
  selectedDomainId: string,
  selectionApplied: boolean,
): PublicKnowledgeDomainDeepLinkRelease {
  if (activeDeepLinkDomainId === null) {
    return Object.freeze({
      activeDeepLinkDomainId: null,
      replacementUrl: null,
      reason: "UNCHANGED",
    });
  }

  if (resolveSinglePublicKnowledgeDomainId(url) !== activeDeepLinkDomainId) {
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

import type { EvidenceDrawerViewModel } from "../evidence_drawer";

export const FOCUS_COMPOSED_CLAIM_REQUEST_PROFILE =
  "kfm.explorer.focus-composed-claim-request.v1" as const;

export const FOCUS_COMPOSED_CLAIM_PROJECTION_PROFILE =
  "kfm.explorer.focus-composed-claim.public-safe.v1" as const;

export type FocusOutcome = "ANSWER" | "ABSTAIN" | "DENY" | "ERROR";
export type FocusClosureOutcome =
  | "SUPPORTED"
  | "QUALIFIED"
  | "ABSTAIN"
  | "DENY"
  | "ERROR";

export type FocusProjectionReasonCode =
  | "COMPOSED_CLAIM_SUPPORTED"
  | "COMPOSED_CLAIM_QUALIFIED"
  | "REQUIRED_DEPENDENCY_UNRESOLVED"
  | "ALTERNATIVE_GROUP_UNRESOLVED"
  | "POLICY_DENIED"
  | "UPSTREAM_ERROR";

export type FocusResolutionCode =
  | FocusProjectionReasonCode
  | "REQUEST_INVALID"
  | "MISSING_EVIDENCE_SCOPE"
  | "PROJECTION_INVALID"
  | "RESPONSE_SCOPE_MISMATCH"
  | "EVIDENCE_OUTSIDE_REQUEST"
  | "GOVERNED_RESOLVER_ERROR";

export type FocusComposedClaimRequest = Readonly<{
  profile: typeof FOCUS_COMPOSED_CLAIM_REQUEST_PROFILE;
  requestId: string;
  claimId: string;
  question: string;
  allowedEvidenceRefs: readonly string[];
}>;

export type FocusComposedClaimCitation = Readonly<{
  evidenceRef: string;
  label: string;
  href: string;
}>;

export type FocusPolicyState = "ALLOW" | "ABSTAIN" | "DENY" | "ERROR";
export type FocusReviewState = "REVIEWED" | "PENDING" | "NOT_APPLICABLE";
export type FocusReleaseState = "RELEASED" | "UNRELEASED" | "WITHDRAWN";
export type FocusFreshnessState = "CURRENT" | "STALE" | "UNKNOWN";

export type FocusComposedClaimProjection = Readonly<{
  profile: typeof FOCUS_COMPOSED_CLAIM_PROJECTION_PROFILE;
  requestId: string;
  claimId: string;
  outcome: FocusOutcome;
  reasonCode: FocusProjectionReasonCode;
  closureId: string;
  closureOutcome: FocusClosureOutcome;
  answer: string | null;
  evidenceRefs: readonly string[];
  citations: readonly FocusComposedClaimCitation[];
  resolvedRoles: readonly string[];
  unavailableRoles: readonly string[];
  limitations: readonly string[];
  policy: FocusPolicyState;
  review: FocusReviewState;
  release: FocusReleaseState;
  freshness: FocusFreshnessState;
  aiReceiptRef: string | null;
  evidenceDrawerInput: unknown;
  evidenceDrawer: EvidenceDrawerViewModel;
}>;

export type FocusComposedClaimViewModel = Readonly<{
  outcome: FocusOutcome;
  code: FocusResolutionCode;
  title: string;
  message: string;
  claimId: string | null;
  closureId: string | null;
  closureOutcome: FocusClosureOutcome | null;
  evidenceRefs: readonly string[];
  citations: readonly FocusComposedClaimCitation[];
  dependencyLabels: readonly string[];
  limitations: readonly string[];
  aiReceiptLabel: string | null;
  evidenceDrawerInput: unknown;
  accessibilityLabel: string;
  ariaLive: "polite" | "assertive";
}>;

export type FocusComposedClaimResolution = Readonly<{
  request: FocusComposedClaimRequest | null;
  code: FocusResolutionCode;
  projection: FocusComposedClaimProjection | null;
  view: FocusComposedClaimViewModel;
}>;

export type GovernedFocusComposedClaimResolver = (
  request: FocusComposedClaimRequest,
) => Promise<unknown>;

export type FocusComposedClaimFixtureCase = Readonly<{
  caseId: string;
  label: string;
  request: unknown;
}>;

export type FocusComposedClaimPanelController = Readonly<{
  state: FocusComposedClaimViewModel;
  close: () => void;
  destroy: () => void;
}>;

export type FocusComposedClaimFixtureController = Readonly<{
  select: (caseId: string) => Promise<FocusComposedClaimResolution | null>;
  destroy: () => void;
}>;

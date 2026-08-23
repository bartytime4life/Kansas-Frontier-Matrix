import { mountCitationPill } from "../features/citation_pill";
import { mountDenialReasonExplorer } from "../features/denial_reason_explorer";
import { mountEvidenceDrawer } from "../features/evidence_drawer";
import { mountTimeScrubber } from "../features/time_banner";
import { mountTrustHeader } from "../features/trust_header";
import { REPOSITORY_SNAPSHOT } from "./catalog";
import {
  TRUST_STATE_PRIMITIVE_PROFILE,
  mountTrustStateSummary,
  resolveTrustStateSummary,
  type TrustStateSummary,
  type TrustStateSummaryInput,
} from "./trust-state-primitives";

export const PUBLIC_TRUST_SURFACE_PROFILE =
  "kfm.explorer.public-trust-surface.v1" as const;

export const PUBLIC_TRUST_CASE_IDS = [
  "supported",
  "unresolved",
  "restricted",
  "stale",
  "error",
  "loading",
] as const;

export type PublicTrustCaseId = (typeof PUBLIC_TRUST_CASE_IDS)[number];

export type PublicTrustSurfaceCase = Readonly<{
  id: PublicTrustCaseId;
  label: string;
  description: string;
  summary: TrustStateSummaryInput;
  governedProjection?: unknown;
  timeProjection?: unknown;
  denialProjection?: unknown;
}>;

export type PublicTrustSurfaceController = Readonly<{
  getActiveCaseId: () => PublicTrustCaseId;
  selectCase: (caseId: PublicTrustCaseId, focus?: boolean) => boolean;
  destroy: () => void;
}>;

type DestroyableController = Readonly<{ destroy: () => void }>;

const EMPTY_HISTORY = Object.freeze({
  negative_outcomes: Object.freeze([]),
  corrections: Object.freeze([]),
});

export const SUPPORTED_TRUST_PROJECTION = Object.freeze({
  profile: "kfm.explorer.evidence-drawer.public-safe.v1",
  id: "kfm:ui:evidence-drawer:answer-001",
  outcome: "ANSWER",
  reason_code: "SUPPORTED",
  title: "Synthetic streamflow observation",
  summary:
    "A synthetic, generalized flow observation is supported by the cited fixture evidence.",
  evidence_refs: Object.freeze(["kfm:evidence:synthetic:flow-001"]),
  citations: Object.freeze([
    Object.freeze({
      label: "Synthetic fixture evidence",
      href: `https://github.com/${REPOSITORY_SNAPSHOT.repository}/blob/${REPOSITORY_SNAPSHOT.commit}/fixtures/ui/evidence_drawer_payload/valid/answer-corrected.json`,
    }),
  ]),
  limitations: Object.freeze([
    "Fixture-only demonstration; not a live observation or life-safety instruction.",
  ]),
  trust_state: Object.freeze({
    source_role: "official",
    policy: "ALLOW",
    review: "REVIEWED",
    release: "RELEASED",
    freshness: "CURRENT",
    correction: "CORRECTED",
  }),
  history: Object.freeze({
    negative_outcomes: Object.freeze([
      Object.freeze({
        evidence_ref: "kfm:evidence:synthetic:flow-000",
        state: "SUPERSEDED",
        reason_code: "SUPERSEDED_EVIDENCE",
        recorded_at: "2026-08-01T00:00:00Z",
        visible_in_runtime: true,
        resolvable_as_current: false,
      }),
    ]),
    corrections: Object.freeze([
      Object.freeze({
        prior_evidence_ref: "kfm:evidence:synthetic:flow-000",
        active_evidence_ref: "kfm:evidence:synthetic:flow-001",
        status: "ACTIVE_CORRECTION",
        recorded_at: "2026-08-01T00:00:00Z",
      }),
    ]),
  }),
});

const UNRESOLVED_TRUST_PROJECTION = Object.freeze({
  profile: "kfm.explorer.evidence-drawer.public-safe.v1",
  id: "kfm:ui:evidence-drawer:abstain-unresolved-001",
  outcome: "ABSTAIN",
  reason_code: "MISSING_EVIDENCE",
  title: "Unresolved synthetic observation",
  summary: "Required evidence has not resolved for this fixture.",
  evidence_refs: Object.freeze([]),
  citations: Object.freeze([]),
  limitations: Object.freeze(["No unsupported claim is shown."]),
  trust_state: Object.freeze({
    source_role: "context",
    policy: "ABSTAIN",
    review: "PENDING",
    release: "UNRELEASED",
    freshness: "UNKNOWN",
    correction: "NONE",
  }),
  history: EMPTY_HISTORY,
});

export const RESTRICTED_TRUST_PROJECTION = Object.freeze({
  profile: "kfm.explorer.evidence-drawer.public-safe.v1",
  id: "kfm:ui:evidence-drawer:deny-sensitive-001",
  outcome: "DENY",
  reason_code: "SENSITIVE_DETAIL_RESTRICTED",
  title: "Restricted map detail",
  summary: "The requested detail is restricted by policy.",
  evidence_refs: Object.freeze([]),
  citations: Object.freeze([]),
  limitations: Object.freeze(["Protected spatial detail is not exposed."]),
  trust_state: Object.freeze({
    source_role: "context",
    policy: "DENY",
    review: "PENDING",
    release: "UNRELEASED",
    freshness: "UNKNOWN",
    correction: "NONE",
  }),
  history: EMPTY_HISTORY,
});

const STALE_TRUST_PROJECTION = Object.freeze({
  profile: "kfm.explorer.evidence-drawer.public-safe.v1",
  id: "kfm:ui:evidence-drawer:abstain-stale-001",
  outcome: "ABSTAIN",
  reason_code: "STALE_EVIDENCE",
  title: "Stale synthetic observation",
  summary: "Released evidence is outside the freshness window for this view.",
  evidence_refs: Object.freeze([]),
  citations: Object.freeze([]),
  limitations: Object.freeze(["No stale evidence is presented as current support."]),
  trust_state: Object.freeze({
    source_role: "official",
    policy: "ABSTAIN",
    review: "REVIEWED",
    release: "RELEASED",
    freshness: "STALE",
    correction: "NONE",
  }),
  history: EMPTY_HISTORY,
});

const ERROR_TRUST_PROJECTION = Object.freeze({
  profile: "kfm.explorer.evidence-drawer.public-safe.v1",
  id: "kfm:ui:evidence-drawer:error-001",
  outcome: "ERROR",
  reason_code: "UPSTREAM_ERROR",
  title: "Governed evidence unavailable",
  summary: "The synthetic governed resolver did not complete.",
  evidence_refs: Object.freeze([]),
  citations: Object.freeze([]),
  limitations: Object.freeze(["No partial or unsupported claim is shown."]),
  trust_state: Object.freeze({
    source_role: "context",
    policy: "ERROR",
    review: "NOT_APPLICABLE",
    release: "UNRELEASED",
    freshness: "UNKNOWN",
    correction: "NONE",
  }),
  history: EMPTY_HISTORY,
});

const SUPPORTED_TIME_PROJECTION = Object.freeze({
  outcome: "ANSWER",
  reason_code: "SUPPORTED",
  time: Object.freeze({
    minimum: "2026-08-23T15:00:00Z",
    maximum: "2026-08-23T17:00:00Z",
    selected: "2026-08-23T16:00:00Z",
    kind: "SELECTED_TIME",
    precision: "SECOND",
    timezone: "UTC",
  }),
  trust_state: Object.freeze({
    policy: "ALLOW",
    release: "RELEASED",
    freshness: "CURRENT",
    temporal_conflict: false,
  }),
});

const RESTRICTED_DENIAL_PROJECTION = Object.freeze({
  profile: "kfm.explorer.denial-reason.public-safe.v1",
  review_id: "kfm:review:synthetic:denial-001",
  outcome: "DENY",
  reason_codes: Object.freeze(["ZOOM_TOO_FINE"]),
  release_candidate_ref:
    "kfm://release-candidate/synthetic-denial@sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
  policy_decision_ref:
    "kfm://policy-decision/synthetic-denial@sha256:bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
  evaluated_at: "2026-08-23T16:00:00Z",
});

function summary(
  input: Omit<TrustStateSummaryInput, "profile">,
): TrustStateSummaryInput {
  return Object.freeze({ profile: TRUST_STATE_PRIMITIVE_PROFILE, ...input });
}

export const PUBLIC_TRUST_SURFACE_CASES: readonly PublicTrustSurfaceCase[] =
  Object.freeze([
    Object.freeze({
      id: "supported",
      label: "Supported",
      description: "Released, reviewed, current, generalized fixture evidence.",
      summary: summary({
        caseId: "supported",
        outcome: "ANSWER",
        evidence: "RESOLVED",
        freshness: "CURRENT",
        sensitivity: "GENERALIZED",
        release: "RELEASED",
        correction: "CORRECTED",
        title: "Supported released evidence",
        message:
          "The finite answer resolves to current, corrected fixture evidence and remains visibly generalized.",
      }),
      governedProjection: SUPPORTED_TRUST_PROJECTION,
      timeProjection: SUPPORTED_TIME_PROJECTION,
    }),
    Object.freeze({
      id: "unresolved",
      label: "Unresolved",
      description: "Evidence resolution is incomplete, so the view abstains.",
      summary: summary({
        caseId: "unresolved",
        outcome: "ABSTAIN",
        evidence: "UNRESOLVED",
        freshness: "UNKNOWN",
        sensitivity: "PUBLIC_SAFE",
        release: "UNRELEASED",
        correction: "NONE",
        title: "Evidence unresolved",
        message:
          "Required support has not resolved. The surface keeps the gap visible and shows no claim-bearing detail.",
      }),
      governedProjection: UNRESOLVED_TRUST_PROJECTION,
    }),
    Object.freeze({
      id: "restricted",
      label: "Restricted",
      description: "Coarse public status is visible while protected detail stays hidden.",
      summary: summary({
        caseId: "restricted",
        outcome: "DENY",
        evidence: "RESTRICTED",
        freshness: "UNKNOWN",
        sensitivity: "RESTRICTED",
        release: "UNRELEASED",
        correction: "NONE",
        title: "Sensitive detail restricted",
        message:
          "Policy denies the requested precision. Only fixed public-safe reason codes are presented.",
      }),
      governedProjection: RESTRICTED_TRUST_PROJECTION,
      denialProjection: RESTRICTED_DENIAL_PROJECTION,
    }),
    Object.freeze({
      id: "stale",
      label: "Stale",
      description: "Released evidence exists but cannot support a current answer.",
      summary: summary({
        caseId: "stale",
        outcome: "ABSTAIN",
        evidence: "STALE",
        freshness: "STALE",
        sensitivity: "GENERALIZED",
        release: "RELEASED",
        correction: "NONE",
        title: "Released evidence is stale",
        message:
          "The stale condition is stated in text and the view abstains rather than presenting old support as current.",
      }),
      governedProjection: STALE_TRUST_PROJECTION,
    }),
    Object.freeze({
      id: "error",
      label: "Error",
      description: "The governed resolver failed and no partial claim is exposed.",
      summary: summary({
        caseId: "error",
        outcome: "ERROR",
        evidence: "ERROR",
        freshness: "UNKNOWN",
        sensitivity: "UNKNOWN",
        release: "UNKNOWN",
        correction: "UNKNOWN",
        title: "Governed trust state unavailable",
        message:
          "The request did not complete. The error presentation is fixed, assertive, and free of internal diagnostics.",
      }),
      governedProjection: ERROR_TRUST_PROJECTION,
    }),
    Object.freeze({
      id: "loading",
      label: "Loading",
      description: "A transient pending state carries no authority or claim content.",
      summary: summary({
        caseId: "loading",
        outcome: "LOADING",
        evidence: "PENDING",
        freshness: "PENDING",
        sensitivity: "UNKNOWN",
        release: "PENDING",
        correction: "PENDING",
        title: "Awaiting governed response",
        message:
          "No claim-bearing detail is displayed while the bounded fixture response is pending.",
      }),
    }),
  ]);

const caseById = new Map(
  PUBLIC_TRUST_SURFACE_CASES.map((entry) => [entry.id, entry] as const),
);

export function findPublicTrustSurfaceCase(
  value: unknown,
): PublicTrustSurfaceCase | null {
  return typeof value === "string"
    ? caseById.get(value as PublicTrustCaseId) ?? null
    : null;
}

export function resolvePublicTrustSurfaceCase(
  value: unknown,
): Readonly<{ entry: PublicTrustSurfaceCase; state: TrustStateSummary }> | null {
  const entry = findPublicTrustSurfaceCase(value);
  if (!entry) return null;
  return Object.freeze({ entry, state: resolveTrustStateSummary(entry.summary) });
}

/**
 * Compose existing app-local trust components around one shared text-first state.
 * The surface is fixture-only and performs no transport, policy evaluation,
 * evidence resolution, source activation, lifecycle mutation, or model call.
 */
export function mountPublicTrustSurface(
  host: HTMLElement,
  initialCaseId: PublicTrustCaseId = "supported",
): PublicTrustSurfaceController {
  const document = host.ownerDocument;
  const root = document.createElement("section");
  const surfaceHeader = document.createElement("header");
  const surfaceEyebrow = document.createElement("p");
  const surfaceHeading = document.createElement("h3");
  const surfaceSummary = document.createElement("p");
  const caseNavigation = document.createElement("div");
  const panel = document.createElement("section");
  const buttons = new Map<PublicTrustCaseId, HTMLButtonElement>();
  let activeCaseId: PublicTrustCaseId = initialCaseId;
  let childControllers: DestroyableController[] = [];
  let destroyed = false;

  root.className = "trust-surface card";
  root.dataset.component = "public-trust-surface";
  root.dataset.profile = PUBLIC_TRUST_SURFACE_PROFILE;
  root.setAttribute("aria-label", "Public trust and finite-outcome fixture surface");

  surfaceHeader.className = "trust-surface__header";
  surfaceEyebrow.className = "eyebrow";
  surfaceEyebrow.textContent = "Unified Workspace UI-02";
  surfaceHeading.textContent = "Shared trust and negative-state primitives";
  surfaceSummary.textContent =
    "Exercise the same text-first grammar across supported, unresolved, restricted, stale, error, and loading fixture states.";
  surfaceHeader.append(surfaceEyebrow, surfaceHeading, surfaceSummary);

  caseNavigation.className = "trust-surface__cases";
  caseNavigation.setAttribute("role", "group");
  caseNavigation.setAttribute("aria-label", "Trust-state fixture cases");

  panel.className = "trust-surface__panel";
  panel.setAttribute("role", "region");
  panel.setAttribute("aria-live", "polite");

  function destroyChildren(): void {
    childControllers.forEach((controller) => controller.destroy());
    childControllers = [];
  }

  function componentCard(label: string): HTMLElement {
    const card = document.createElement("section");
    const heading = document.createElement("h4");
    const content = document.createElement("div");
    card.className = "trust-surface__component";
    heading.textContent = label;
    content.className = "trust-surface__component-host";
    card.append(heading, content);
    return card;
  }

  function render(entry: PublicTrustSurfaceCase, focus: boolean): void {
    destroyChildren();
    panel.replaceChildren();
    panel.dataset.caseId = entry.id;
    panel.setAttribute("aria-label", `${entry.label} trust-state fixture`);

    const intro = document.createElement("header");
    const eyebrow = document.createElement("p");
    const heading = document.createElement("h3");
    const description = document.createElement("p");
    eyebrow.className = "eyebrow";
    eyebrow.textContent = "Shared trust grammar";
    heading.textContent = entry.label;
    heading.tabIndex = -1;
    description.textContent = entry.description;
    intro.className = "trust-surface__intro";
    intro.append(eyebrow, heading, description);

    const summaryHost = document.createElement("div");
    summaryHost.className = "trust-surface__summary";
    childControllers.push(mountTrustStateSummary(summaryHost, entry.summary));

    const components = document.createElement("div");
    components.className = "trust-surface__components";

    if (entry.governedProjection !== undefined) {
      const drawerCard = componentCard("Evidence Drawer");
      const drawerHost = drawerCard.lastElementChild as HTMLElement;
      const drawer = mountEvidenceDrawer(drawerHost, entry.governedProjection);
      childControllers.push(drawer);

      const headerCard = componentCard("Trust Header");
      const headerHost = headerCard.lastElementChild as HTMLElement;
      childControllers.push(
        mountTrustHeader(headerHost, entry.governedProjection, {
          compact: true,
          onOpenDrawer: () => drawer.open(),
        }),
      );
      components.append(headerCard, drawerCard);
    }

    if (entry.timeProjection !== undefined) {
      const timeCard = componentCard("Time Banner");
      const timeHost = timeCard.lastElementChild as HTMLElement;
      childControllers.push(
        mountTimeScrubber(timeHost, entry.timeProjection, {
          copyText: () => undefined,
        }),
      );
      components.append(timeCard);
    }

    if (entry.governedProjection !== undefined) {
      const citationCard = componentCard("Citation Pill");
      const citationHost = citationCard.lastElementChild as HTMLElement;
      const citation = mountCitationPill(citationHost, entry.governedProjection, {
        timestamp: "2026-08-23T16:00:00Z",
        view: "map",
        label: "Fixture evidence",
        copyText: () => undefined,
      });
      childControllers.push(citation);
      if (citation.state.visibility === "VISIBLE") components.append(citationCard);
      else citationCard.remove();
    }

    if (entry.denialProjection !== undefined) {
      const denialCard = componentCard("Denial reason");
      const denialHost = denialCard.lastElementChild as HTMLElement;
      childControllers.push(
        mountDenialReasonExplorer(denialHost, entry.denialProjection),
      );
      components.append(denialCard);
    }

    if (entry.id === "loading") {
      const loading = document.createElement("p");
      loading.className = "trust-surface__pending";
      loading.setAttribute("role", "status");
      loading.setAttribute("aria-live", "polite");
      loading.setAttribute("aria-busy", "true");
      loading.textContent =
        "Loading is a transient UI condition. It does not imply evidence, review, release, or authority.";
      components.append(loading);
    }

    panel.append(intro, summaryHost, components);
    if (focus) heading.focus();
  }

  function selectCase(caseId: PublicTrustCaseId, focus = false): boolean {
    if (destroyed) return false;
    const entry = findPublicTrustSurfaceCase(caseId);
    if (!entry) return false;
    activeCaseId = entry.id;
    buttons.forEach((button, id) => {
      button.setAttribute("aria-pressed", id === activeCaseId ? "true" : "false");
    });
    render(entry, focus);
    return true;
  }

  for (const entry of PUBLIC_TRUST_SURFACE_CASES) {
    const button = document.createElement("button");
    button.type = "button";
    button.textContent = entry.label;
    button.dataset.trustCaseId = entry.id;
    button.setAttribute("aria-pressed", "false");
    button.addEventListener("click", () => selectCase(entry.id, true));
    buttons.set(entry.id, button);
    caseNavigation.append(button);
  }

  root.append(surfaceHeader, caseNavigation, panel);
  host.replaceChildren(root);
  if (!selectCase(initialCaseId)) selectCase("supported");

  return Object.freeze({
    getActiveCaseId: () => activeCaseId,
    selectCase,
    destroy(): void {
      if (destroyed) return;
      destroyed = true;
      destroyChildren();
      buttons.forEach((button) => button.replaceWith());
      buttons.clear();
      host.replaceChildren();
    },
  });
}

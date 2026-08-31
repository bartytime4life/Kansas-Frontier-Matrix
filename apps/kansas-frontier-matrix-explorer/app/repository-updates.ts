export type RepositoryUpdateState =
  | "ACCEPTED"
  | "BOUNDED PROOF"
  | "CORRECTED"
  | "NEEDS VERIFICATION";

export type RepositoryCapabilityMaturity =
  | "IMPLEMENTED"
  | "PARTIAL"
  | "DOCUMENTED"
  | "NOT INSPECTED";

export type RepositoryUpdate = Readonly<{
  id: string;
  area: string;
  title: string;
  state: RepositoryUpdateState;
  maturity: RepositoryCapabilityMaturity;
  date: string;
  summary: string;
  boundary: string;
  sourceLabel: string;
  sourceUrl: string;
  layerId?: string;
  featureId?: string;
}>;

export const REPOSITORY_SNAPSHOT = Object.freeze({
  repository: "bartytime4life/Kansas-Frontier-Matrix",
  ref: "main",
  commit: "5d835798e09a4dd14735779cb44206a8a3e8b2d3",
  shortCommit: "5d83579",
  inspectedAt: "2026-08-31T11:07:55Z",
  counts: Object.freeze({
    knowledgeDomains: 13,
    explorerFeatureFamilies: 38,
    mapFunctions: 20,
    countyPlanningLanes: 105,
    repositoryUpdates: 17,
    transitionBoundaries: 4,
    readinessGates: 7,
  }),
});

const repoAtSnapshot = `https://github.com/${REPOSITORY_SNAPSHOT.repository}/blob/${REPOSITORY_SNAPSHOT.commit}`;

export const REPOSITORY_UPDATES: readonly RepositoryUpdate[] = Object.freeze([
  Object.freeze({
    id: "local-import-review-hardening",
    area: "Explorer security and privacy",
    title: "Local geodata inspection now fails closed on malformed or stale input",
    state: "CORRECTED",
    maturity: "IMPLEMENTED",
    date: "31 Aug 2026",
    summary:
      "Current main integrates the review-hardened local KML and GeoJSON inspector: geometry-type-specific validation, coordinate-range checks, bounded recursion, iterative large-file bounds, inert KML fragment parsing, and inspection-generation tokens that discard stale asynchronous reads.",
    boundary:
      "Files remain browser-local and unadmitted. Exact imported bounds are withheld from copied audits and location-derived camera state is redacted from URLs and saved workspaces. A successful preview is not source admission, evidence, policy approval, release, deployment, or publication.",
    sourceLabel: "Review-hardened local geodata inspector",
    sourceUrl: `${repoAtSnapshot}/apps/kansas-frontier-matrix-explorer/app/import-preview.ts`,
  }),
  Object.freeze({
    id: "county-starter-slice",
    area: "MapLibre and search",
    title: "All 105 Kansas counties now have public locator starters",
    state: "ACCEPTED",
    maturity: "IMPLEMENTED",
    date: "30 Aug 2026",
    summary:
      "Current main adds one 2025 U.S. Census Gazetteer representative internal point for each Kansas county, with stable GEOIDs and registry metadata for search, selection, evidence inspection, report scoping, and future governed county slices.",
    boundary:
      "These are public reference locators, not county boundaries, centroids, county seats, parcels, conditions, protected geometry, jurisdictional determinations, source admission, or a KFM data release.",
    sourceLabel: "County starter slice",
    sourceUrl: `${repoAtSnapshot}/apps/kansas-frontier-matrix-explorer/app/county-starter-slice.ts`,
    layerId: "county-starter-points",
  }),
  Object.freeze({
    id: "temporal-catalog-comparison",
    area: "Timeline and report",
    title: "Time A / Time B comparison preserves report scope",
    state: "ACCEPTED",
    maturity: "IMPLEMENTED",
    date: "30 Aug 2026",
    summary:
      "Current main compares which site-local records are compatible at two timeline steps and binds the same layer, query, evidence, selection, visibility, viewport, or analysis-area scope into generated report comparisons.",
    boundary:
      "Entered and exited identifiers describe fixture catalog availability under declared temporal rules. They are not observed real-world change, imagery analysis, causation, an event claim, evidence, policy approval, release, or publication authority.",
    sourceLabel: "Temporal catalog comparison",
    sourceUrl: `${repoAtSnapshot}/apps/kansas-frontier-matrix-explorer/app/temporal-comparison.ts`,
  }),
  Object.freeze({
    id: "planning-scenario-review",
    area: "Explorer UI",
    title: "Planning scenarios now have a strict review projection",
    state: "BOUNDED PROOF",
    maturity: "PARTIAL",
    date: "29 Aug 2026",
    summary:
      "Current main adds a fixture-only, text-first planning-scenario review with a held ABSTAIN state, explicit horizon and uncertainty, equity questions, participation and evidence references, limitations, and fixed negative-state copy.",
    boundary:
      "The repository feature is not mounted on a production route and performs no transport, scenario computation, policy evaluation, preference aggregation, lifecycle write, recommendation, release, or publication action. This Site replays only the public synthetic fixture and negative states.",
    sourceLabel: "Planning scenario review",
    sourceUrl: `${repoAtSnapshot}/apps/explorer-web/src/features/planning_scenario_review/README.md`,
    layerId: "public-safe-planning",
    featureId: "planning-generalized-envelope",
  }),
  Object.freeze({
    id: "accessibility-evidence-boundary",
    area: "Accessibility",
    title: "Accessibility guidance now separates targets from proof",
    state: "CORRECTED",
    maturity: "PARTIAL",
    date: "28 Aug 2026",
    summary:
      "The revised repository guidance records an eight-spec keyboard and focus smoke as bounded fixture evidence while keeping axe coverage, whole-application review, non-map parity, reduced motion, touch, zoom, reflow, contrast, and assistive-technology testing explicitly held or unverified.",
    boundary:
      "A passing bounded workflow is not WCAG conformance, a manual accessibility review, a release gate, deployment approval, or publication authority. WCAG 2.2 Level AA remains a proposed target in this draft guidance.",
    sourceLabel: "Accessibility commitments v1.1",
    sourceUrl: `${repoAtSnapshot}/docs/brand/accessibility-commitments.md`,
  }),
  Object.freeze({
    id: "public-workspace-registry",
    area: "Explorer UI",
    title: "Four public workspaces now share one navigation boundary",
    state: "BOUNDED PROOF",
    maturity: "IMPLEMENTED",
    date: "23 Aug 2026",
    summary:
      "Current main registers Explore, Knowledge, Features, and Trust as public-safe, non-privileged workspace destinations backed by the repository feature catalog.",
    boundary:
      "The registry is navigation metadata only. It creates no privileged route, policy decision, review authority, source activation, release, deployment, or publication power.",
    sourceLabel: "Public workspace registry",
    sourceUrl: `${repoAtSnapshot}/apps/explorer-web/src/site/workspace-registry.ts`,
  }),
  Object.freeze({
    id: "governed-api-checkpoint",
    area: "Governed API",
    title: "The executable API checkpoint is intentionally negative-only",
    state: "BOUNDED PROOF",
    maturity: "PARTIAL",
    date: "22 Aug 2026",
    summary:
      "The exact route registry contains GET /bootstrap, GET /layers, and GET /evidence. Each emits a schema-shaped ABSTAIN / NOT_IMPLEMENTED envelope; unknown paths and unsupported methods fail closed with safe ERROR envelopes.",
    boundary:
      "This proves deterministic code shape and negative tests, not authentication, policy execution, evidence resolution, a governed ANSWER, deployment, or public availability.",
    sourceLabel: "Master API surface checkpoint",
    sourceUrl: `${repoAtSnapshot}/docs/atlas/master-api-surface.md`,
  }),
  Object.freeze({
    id: "consent-projection-boundary",
    area: "Consent and Focus Mode",
    title: "Consent metadata is normalized; the fixture-first boundary remains",
    state: "CORRECTED",
    maturity: "PARTIAL",
    date: "22 Aug 2026",
    summary:
      "Current main normalizes the consent-pattern document metadata to the standard type while preserving the Focus boundary between a browser-session show/hide choice and any consent grant, credential, status, withdrawal, or policy authority.",
    boundary:
      "The repository proves a strict fixture-first consent-card projection, not operational consent issuance, verification, policy composition, withdrawal propagation, release, or publication.",
    sourceLabel: "Focus consent boundary",
    sourceUrl: `${repoAtSnapshot}/docs/focus-mode/CONSENT_PATTERN.md`,
    layerId: "public-safe-planning",
    featureId: "planning-generalized-envelope",
  }),
  Object.freeze({
    id: "lifecycle-boundary",
    area: "Lifecycle",
    title: "Lifecycle state guidance now separates stage from readiness",
    state: "CORRECTED",
    maturity: "DOCUMENTED",
    date: "22 Aug 2026",
    summary:
      "The current state guidance distinguishes the KFM lifecycle spine from fixture-only gate assessment, final readiness, accountable decisions, transition application, correction, and rollback.",
    boundary:
      "The repository proves bounded validators and documentation, not a production transition operator, public release, correction propagation, or rollback execution.",
    sourceLabel: "Lifecycle state boundary",
    sourceUrl: `${repoAtSnapshot}/docs/focus-mode/state/lifecycle-states.md`,
  }),
  Object.freeze({
    id: "transition-index",
    area: "Focus Mode state",
    title: "Transition families now preserve the four-outcome runtime boundary",
    state: "CORRECTED",
    maturity: "DOCUMENTED",
    date: "22 Aug 2026",
    summary:
      "The transition index separates runtime responses, review/workflow posture, lifecycle, payload evidence posture, release accountability, validator results, and repository delivery.",
    boundary:
      "HOLD is not a fifth client-facing runtime outcome. The current runtime envelope remains ANSWER, ABSTAIN, DENY, or ERROR.",
    sourceLabel: "Transition documentation index",
    sourceUrl: `${repoAtSnapshot}/docs/focus-mode/state/transitions/README.md`,
  }),
  Object.freeze({
    id: "answer-to-abstain",
    area: "Runtime outcomes",
    title: "ANSWER to ABSTAIN is modeled as a later immutable response",
    state: "CORRECTED",
    maturity: "DOCUMENTED",
    date: "22 Aug 2026",
    summary:
      "The revised boundary keeps the earlier ANSWER immutable and treats a later ABSTAIN as a new governed envelope when current support no longer closes.",
    boundary:
      "A prohibition maps to DENY, an operational failure maps to ERROR, and eligible replacement evidence may support another ANSWER. Reason-code names remain open unless accepted elsewhere.",
    sourceLabel: "ANSWER to ABSTAIN boundary",
    sourceUrl: `${repoAtSnapshot}/docs/focus-mode/state/transitions/answer-to-abstain.md`,
    layerId: "water-context",
    featureId: "water-kansas-river",
  }),
  Object.freeze({
    id: "hold-to-deny",
    area: "Review and policy",
    title: "Candidate rejection and runtime DENY are now explicitly separate",
    state: "CORRECTED",
    maturity: "DOCUMENTED",
    date: "22 Aug 2026",
    summary:
      "The current boundary distinguishes a held candidate, a review rejection, and any later policy-aware runtime projection instead of collapsing them into one state change.",
    boundary:
      "Rejection does not automatically produce DENY and cannot revoke a prior release. Each effect needs its own authority and accountability record.",
    sourceLabel: "HOLD to rejection / DENY boundary",
    sourceUrl: `${repoAtSnapshot}/docs/focus-mode/state/transitions/hold-to-deny.md`,
    layerId: "public-safe-planning",
    featureId: "planning-generalized-envelope",
  }),
  Object.freeze({
    id: "hydrology-dashboard",
    area: "Hydrology",
    title: "Hydrology dashboard boundary is now repository-grounded",
    state: "BOUNDED PROOF",
    maturity: "PARTIAL",
    date: "21 Aug 2026",
    summary:
      "The current specification recognizes closed synthetic schema families, Evidence Drawer convergence, and one manifest-backed, no-network Hydrology fixture adapter.",
    boundary:
      "The map layer adapter, live sources, bound policy, dashboard route, production metrics, release, and public ANSWER remain unverified or held.",
    sourceLabel: "Hydrology dashboard specification",
    sourceUrl: `${repoAtSnapshot}/docs/dashboards/domain/hydrology.md`,
    layerId: "water-context",
    featureId: "water-smoky-hill",
  }),
  Object.freeze({
    id: "maplibre-boundary",
    area: "Map runtime",
    title: "The renderer seam is accepted; its neutral port is a verified slice",
    state: "ACCEPTED",
    maturity: "PARTIAL",
    date: "28 Aug 2026",
    summary:
      "ADR-0006 and ADR-0007 bind KFM browser rendering to packages/maplibre. Current main records exact maplibre-gl 6.6.0 lock closure, a package-owned lifecycle and camera adapter, the Vite worker seam, deterministic positive and fail-closed tests, and a bounded real-browser fixture.",
    boundary:
      "The repository still holds Explorer production activation, broader browser readiness, governed performance execution, source and layer admission, PMTiles, terrain, long-session evidence, release, deployment, and publication. This Site remains a separate synthetic demonstration and is not KFM runtime-readiness evidence.",
    sourceLabel: "MapRuntimePort implementation",
    sourceUrl: `${repoAtSnapshot}/packages/maplibre/README.md`,
  }),
  Object.freeze({
    id: "geoparquet-crs",
    area: "Carrier interoperability",
    title: "The retained GeoParquet 1.1 CRS fixture was corrected",
    state: "CORRECTED",
    maturity: "IMPLEMENTED",
    date: "21 Aug 2026",
    summary:
      "Merge #3221 completed the retained 1.1 fixture's OGC:CRS84 PROJJSON while guarding the separate 2.0 release-candidate metadata path against unintended change.",
    boundary:
      "This is a synthetic fixture correction. It does not adopt a format, migrate data, establish a released layer, or turn GeoParquet bytes into evidence authority.",
    sourceLabel: "Merged correction #3221",
    sourceUrl: "https://github.com/bartytime4life/Kansas-Frontier-Matrix/commit/40f68c17b16cdc4219ea3d00756912f9fdb768b8",
  }),
  Object.freeze({
    id: "county-focus-inventory",
    area: "County Focus Mode",
    title: "The county inventory is useful but snapshot-sensitive",
    state: "NEEDS VERIFICATION",
    maturity: "NOT INSPECTED",
    date: "20 Aug 2026",
    summary:
      "The latest formal inventory records 105 county-shaped directories at its older pinned base, while many county documentation changes landed afterward.",
    boundary:
      "Do not project the inventory's anomaly totals as current-head facts without recomputation. It proves no county lifecycle readiness, release, or publication state.",
    sourceLabel: "County Focus Mode master index",
    sourceUrl: `${repoAtSnapshot}/docs/focus-mode/counties/COUNTY_INDEX.md`,
  }),
  Object.freeze({
    id: "runbook-interface-wave",
    area: "Operational handoffs",
    title: "Runbook lanes expanded across seven knowledge domains",
    state: "CORRECTED",
    maturity: "DOCUMENTED",
    date: "25 Aug 2026",
    summary:
      "The current snapshot is 521 commits after the prior Site evidence pin; the inspected change set includes the earlier multi-domain runbook wave alongside newer Explorer and accessibility work.",
    boundary:
      "Documentation depth improves navigation and handoff shape only. It does not prove executable commands, live source access, policy evaluation, reviewer authority, release, deployment, promotion, or publication; the parent inventory remains snapshot-sensitive.",
    sourceLabel: "Atmosphere runbook boundary",
    sourceUrl: `${repoAtSnapshot}/docs/runbooks/atmosphere/README.md`,
  }),
]);

export type TransitionBoundary = Readonly<{
  id: "answer-to-abstain" | "candidate-to-hold" | "hold-to-deny" | "published-to-revoked";
  family: "RUNTIME" | "REVIEW" | "RELEASE";
  title: string;
  from: string;
  to: string;
  posture: "GROUNDED DOC" | "LINEAGE / VERIFY";
  summary: string;
  guard: string;
  projection: string;
  proof: readonly string[];
  sourceUrl: string;
  layerId?: string;
  featureId?: string;
  analogueLabel?: string;
}>;

export const TRANSITION_BOUNDARIES: readonly TransitionBoundary[] = Object.freeze([
  Object.freeze({
    id: "answer-to-abstain",
    family: "RUNTIME",
    title: "Later support no longer closes",
    from: "ANSWER",
    to: "ABSTAIN",
    posture: "GROUNDED DOC",
    summary: "Issue a new finite envelope; never rewrite the earlier ANSWER or silently erase its lineage.",
    guard: "Current evidence is insufficient or stale, while no current policy prohibition or operational failure controls the request.",
    projection: "ABSTAIN is valid only for the new request context. DENY, ERROR, or another ANSWER may be correct under different current evidence.",
    proof: ["Prior envelope identity", "Current evidence and policy evaluation", "Append-only correlation record"],
    sourceUrl: `${repoAtSnapshot}/docs/focus-mode/state/transitions/answer-to-abstain.md`,
    layerId: "water-context",
    featureId: "water-kansas-river",
    analogueLabel: "Inspect missing-evidence analogue",
  }),
  Object.freeze({
    id: "candidate-to-hold",
    family: "REVIEW",
    title: "A bounded candidate needs accountable resolution",
    from: "CANDIDATE",
    to: "HOLD",
    posture: "GROUNDED DOC",
    summary: "HOLD is a review, workflow, placement, or promotion-readiness posture—not a fifth runtime response.",
    guard: "The unresolved condition is scoped, recoverable, assigned to an accountable route, and has an explicit clearance or escalation condition.",
    projection: "Public requests still receive ANSWER, ABSTAIN, DENY, or ERROR. The held candidate is never projected directly.",
    proof: ["Immutable candidate identity", "Hold scope and basis", "Owner, review time, and clearance conditions"],
    sourceUrl: `${repoAtSnapshot}/docs/focus-mode/state/transitions/candidate-to-hold.md`,
  }),
  Object.freeze({
    id: "hold-to-deny",
    family: "REVIEW",
    title: "Review rejection and runtime denial remain separate",
    from: "HOLD",
    to: "REJECT / DENY",
    posture: "GROUNDED DOC",
    summary: "A review may reject the candidate; a later policy-aware runtime request may separately return DENY.",
    guard: "An accountable decision resolves the hold and current policy, rights, sensitivity, or access rules independently control the runtime request.",
    projection: "DENY is not automatic. Current evidence and policy could instead yield ANSWER, ABSTAIN, or ERROR.",
    proof: ["Review decision and authority", "Current policy evaluation", "Separate runtime envelope"],
    sourceUrl: `${repoAtSnapshot}/docs/focus-mode/state/transitions/hold-to-deny.md`,
    layerId: "public-safe-planning",
    featureId: "planning-generalized-envelope",
    analogueLabel: "Inspect policy-denial analogue",
  }),
  Object.freeze({
    id: "published-to-revoked",
    family: "RELEASE",
    title: "A released artifact must stop serving",
    from: "PUBLISHED",
    to: "REVOKED",
    posture: "LINEAGE / VERIFY",
    summary: "The current sibling document still carries older normative claims that have not yet been reconciled to the newly grounded transition index.",
    guard: "A current release, accountable issuer, reason, artifact identity, replacement posture, correction path, and client effect all require verification.",
    projection: "Clients must not silently render a revoked artifact. Rebinding, ABSTAIN, or another governed outcome depends on current accepted release authority.",
    proof: ["Release and revocation records", "Issuer and signature authority", "Cache, client, correction, and rollback evidence"],
    sourceUrl: `${repoAtSnapshot}/docs/focus-mode/state/transitions/published-to-revoked.md`,
    layerId: "historical-context",
    featureId: "history-route-1910",
    analogueLabel: "Inspect supersession analogue",
  }),
]);

export type LifecycleGate = Readonly<{
  id: string;
  transition: string;
  roles: string;
  failClosed: string;
}>;

export const LIFECYCLE_GATES: readonly LifecycleGate[] = Object.freeze([
  Object.freeze({ id: "ADMISSION", transition: "DISCOVERED → RAW", roles: "Source descriptor · payload identity · policy decision", failClosed: "NOT_ADMITTED" }),
  Object.freeze({ id: "NORMALIZATION", transition: "RAW → WORK", roles: "Transform receipt · validation report · policy decision", failClosed: "QUARANTINE" }),
  Object.freeze({ id: "VALIDATION", transition: "WORK → PROCESSED", roles: "Validation report · policy decision · conditional transformation receipts", failClosed: "STAY_WORK" }),
  Object.freeze({ id: "CATALOG_CLOSURE", transition: "PROCESSED → CATALOG", roles: "Catalog matrix · EvidenceBundle · policy decision", failClosed: "HOLD_PROCESSED" }),
  Object.freeze({ id: "RELEASE", transition: "CATALOG → PUBLISHED", roles: "Release manifest · rollback target · correction path · policy decision", failClosed: "HOLD_CATALOG" }),
  Object.freeze({ id: "CORRECTION", transition: "PUBLISHED → PUBLISHED_SUPERSEDED", roles: "Correction notice · review record · invalidation list · release manifest · policy decision", failClosed: "STALE_STATE_ANNOUNCEMENT" }),
  Object.freeze({ id: "ROLLBACK", transition: "PUBLISHED → PRIOR_RELEASE", roles: "Rollback card · correction notice · invalidation list · release manifest · policy decision", failClosed: "HOLD_CURRENT_RELEASE" }),
]);

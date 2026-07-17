---
name: Feature request
about: Propose a bounded KFM capability or improvement with evidence, scope, governance impact, and measurable acceptance criteria.
title: "[Feature]: "
labels: []
assignees: ["bartytime4life"]
---

<!--
KFM public feature-intake template.

This issue is a proposal and routing record. Filing it does not create a roadmap
commitment, approve architecture, reserve a repository path, decide policy,
authorize implementation, change release state, or prove that the feature exists.

Before submitting:
1. Search open and closed issues, pull requests, ADRs, and verification work for
   duplicates or overlapping proposals.
2. Use bug.md for observed defects and evidence_correction.md for correction of
   public or semi-public claims, releases, layers, artifacts, or AI answers.
3. Use adr.md when the proposal changes canonical roots, schema authority,
   lifecycle boundaries, trust-membrane behavior, public access, sensitive-data
   posture, source/evidence authority, object-family meaning, or other
   consequential cross-cutting decisions.
4. Describe desired outcomes before prescribing file paths or implementation.
5. Do not include secrets, exploit details, restricted source payloads, exact
   sensitive locations, living-person records, DNA/genomic material, or
   unreleased RAW/WORK/QUARANTINE data.
6. Use the private-first path in SECURITY.md for security-sensitive proposals or
   vulnerability details.

Use UNKNOWN or NEEDS VERIFICATION rather than guessing.
-->

> [!IMPORTANT]
> A feature request is not an accepted design or implementation plan. Any resulting ADR, contract, schema, policy, source descriptor, migration, test, release, correction, receipt, or proof must be created and reviewed in its governing responsibility root.

> [!CAUTION]
> Do not post credentials, private endpoints, exploit details, exact rare-species or archaeology locations, critical-infrastructure vulnerability details, living-person records, DNA/genomic material, private-land details, restricted source payloads, or unreleased lifecycle data. Route security-sensitive material through `SECURITY.md`.

## Feature summary

<!-- In one or two sentences, describe the capability or improvement and the user-visible or operational outcome. -->

-

## Reporter preflight

- [ ] I searched issues, pull requests, ADRs, and related documentation for overlapping work.
- [ ] This is a feature or enhancement request, not primarily a reproducible defect or evidence correction.
- [ ] I described the problem and outcome before proposing paths or implementation details.
- [ ] I marked repository, architecture, staffing, cost, and runtime assumptions with the appropriate truth label.
- [ ] I removed or generalized secrets, private data, restricted content, and exact sensitive locations.
- [ ] This proposal is safe for a public issue. Security-sensitive details have been routed privately.
- [ ] I understand that filing, assigning, labeling, prioritizing, or closing this issue does not approve architecture, implementation, release, or publication.

## Current truth posture

<!-- Apply labels per material claim. Most new feature proposals begin as PROPOSED. -->

- [ ] `CONFIRMED` — verified from current repository evidence, tests, logs, accepted decisions, or generated artifacts.
- [ ] `PROPOSED` — desired capability, design, placement, or implementation approach under review.
- [ ] `NEEDS VERIFICATION` — checkable, but not checked strongly enough to act as fact.
- [ ] `UNKNOWN` — unresolved and unsafe to assume.

**Overall proposal posture:** `PROPOSED`

## Problem or opportunity

<!--
Describe the current limitation, unmet need, governance gap, user pain, or
opportunity. Separate current evidence from desired future behavior.
-->

-

### Who is affected?

- [ ] Public map or explorer users
- [ ] Researchers, educators, or community users
- [ ] Domain stewards or reviewers
- [ ] Data/source maintainers
- [ ] Connector or pipeline maintainers
- [ ] API, UI, map, search, graph, or AI maintainers
- [ ] Release, correction, policy, security, or operations maintainers
- [ ] Contributors or documentation users
- [ ] Other:
- [ ] `UNKNOWN`

### Desired outcome

<!-- What should become possible, safer, clearer, faster, more inspectable, or more correct? -->

-

## Request type

Check all that apply.

- [ ] New user-facing capability
- [ ] Enhancement to an existing capability
- [ ] Documentation, contributor, or governance improvement
- [ ] New source, connector, or source-admission capability
- [ ] Pipeline, transform, or data-quality improvement
- [ ] Contract, schema, identity, provenance, or evidence improvement
- [ ] Policy, rights, sensitivity, or access-control improvement
- [ ] Validation, fixture, test, proof, or observability improvement
- [ ] Governed API, authentication, authorization, or trust-membrane improvement
- [ ] Explorer, MapLibre, layer, popup, Evidence Drawer, or export improvement
- [ ] Search, catalog, graph, triplet, or discovery improvement
- [ ] Focus Mode, governed AI, model adapter, or runtime-envelope improvement
- [ ] CI, workflow, dependency, deployment, or operations improvement
- [ ] Release, correction, withdrawal, rollback, or auditability improvement
- [ ] Accessibility, usability, performance, or reliability improvement
- [ ] Other:

## Proposed user or operator workflow

<!--
Describe the intended workflow from the user's perspective. Include safe negative
outcomes such as HOLD, ABSTAIN, DENY, unavailable, stale, or permission required.
-->

1.
2.
3.

**Expected successful outcome:**

-

**Expected fail-safe or negative outcomes:**

-

## Scope and non-goals

### In scope

-

### Non-goals

-

### Explicitly unchanged

<!-- Name trust boundaries, APIs, formats, roots, lifecycle stages, or compatibility promises that should remain unchanged. -->

-

## Evidence and need basis

<!--
Use current repository paths plus immutable refs, issue/PR numbers, user research,
test results, logs, metrics, or authoritative sources. Memory and plausibility are
not evidence.
-->

| Truth label | Evidence location | Observation supported | Limitation / verification needed |
|---|---|---|---|
| `CONFIRMED` | | | |
| `PROPOSED` | | | |
| `NEEDS VERIFICATION` | | | |
| `UNKNOWN` | | | |

**EvidenceRef / EvidenceBundle implications:** `N/A / describe`

## Alternatives and status quo

<!-- Include genuine alternatives. "Do nothing" or a narrower manual workflow is valid. -->

1. **Preferred capability —**
2. **Narrower alternative —**
3. **Different implementation approach —**
4. **Status quo —**

**Why the preferred capability is proportionate:**

-

## Architecture and ADR routing

A feature request must route to the ADR process when it would make a consequential architecture or governance decision.

- [ ] Adds, removes, renames, or reclassifies a canonical responsibility root.
- [ ] Promotes or retires a compatibility root.
- [ ] Changes schema-home authority or contract/schema placement.
- [ ] Splits, merges, bypasses, or redefines a lifecycle phase.
- [ ] Creates a parallel schema, contract, policy, source, registry, release, proof, receipt, or canonical-truth home.
- [ ] Bends a KFM invariant or trust-membrane boundary.
- [ ] Approves or changes a direct public-access path.
- [ ] Changes promotion, release, correction, withdrawal, or rollback gates.
- [ ] Changes sensitive-location, rights, sovereignty, consent, or geoprivacy posture.
- [ ] Changes source-ledger, source-role, evidence, deterministic identity, canonicalization, or object-family meaning.
- [ ] Adopts or materially changes a model/runtime/public-response envelope.
- [ ] Introduces or materially changes a steward role or separation-of-duties rule.
- [ ] Requires structural migration, semantic rename, compatibility break, or contract-version change.
- [ ] No formal ADR trigger identified.
- [ ] `NEEDS VERIFICATION`

**ADR issue or proposed ADR path:** `N/A / ADR-XXXX / related issue`

> [!IMPORTANT]
> Do not use this feature issue to approve an ADR-triggering decision. Route the decision through `.github/ISSUE_TEMPLATE/adr.md` and the governed `docs/adr/` process.

## Affected responsibility roots and placement

<!--
Paths are PROPOSED until checked against Directory Rules, current repository
evidence, and visible ADRs. Choose paths by responsibility, not topic.
-->

| Proposed or affected path | Owning responsibility root | Responsibility / authority role | Status | Directory Rules or ADR basis |
|---|---|---|---|---|
| | | | `PROPOSED` | |

- [ ] No new parallel authority home is proposed.
- [ ] Canonical and compatibility roots remain distinct.
- [ ] Meaning, machine shape, policy, proof, lifecycle data, and release authority remain separated.
- [ ] Domain files stay inside the proper responsibility root rather than creating a new root-level domain folder.
- [ ] Any move, rename, or authority change has a migration or deprecation plan.
- [ ] Placement is not yet known and is explicitly `NEEDS VERIFICATION`.

## Affected KFM surfaces

### Responsibility roots

- [ ] `.github/`
- [ ] `docs/`
- [ ] `control_plane/`
- [ ] `contracts/`
- [ ] `schemas/`
- [ ] `policy/`
- [ ] `data/`
- [ ] `release/`
- [ ] `apps/`
- [ ] `packages/`
- [ ] `connectors/`
- [ ] `pipelines/` / `pipeline_specs/`
- [ ] `tools/` / `scripts/`
- [ ] `tests/` / `fixtures/`
- [ ] `runtime/` / `infra/` / `configs/`
- [ ] `migrations/`
- [ ] Other:
- [ ] `UNKNOWN`

**Cross-cutting explanation:** <!-- Required when several roots are affected. -->

### Lifecycle stages

- [ ] RAW
- [ ] WORK / QUARANTINE
- [ ] PROCESSED
- [ ] CATALOG / TRIPLET
- [ ] PUBLISHED
- [ ] No lifecycle-stage impact
- [ ] `UNKNOWN`

### Public and governed interfaces

- [ ] Governed API
- [ ] Explorer, MapLibre, Evidence Drawer, or export
- [ ] Search, catalog, graph, or triplet
- [ ] Focus Mode or governed AI
- [ ] Authentication, authorization, or access tier
- [ ] Release, correction, or publication surface
- [ ] No public-interface impact
- [ ] `UNKNOWN`

## Sources, data, evidence, and provenance

- New or changed source family / `SourceDescriptor`:
- Intended source role: `primary / corroborating / contextual / modeled / administrative / aggregate / synthetic / restricted / UNKNOWN`
- Rights, license, attribution, or source-term implications:
- Sensitivity, sovereignty, consent, or geoprivacy implications:
- Deterministic identity or canonicalization implications:
- `EvidenceRef` / `EvidenceBundle` requirements:
- Provenance, receipt, proof, validation-report, or lineage requirements:
- Freshness, valid-time, source-time, retrieval-time, or release-time requirements:
- Quarantine and malformed/ambiguous input behavior:
- Not applicable:

## Trust, policy, rights, and sensitivity impact

Check all that apply.

- [ ] Requires new or changed policy behavior.
- [ ] Could expose sensitive or restricted material.
- [ ] Could expose unreleased `RAW`, `WORK`, `QUARANTINE`, candidate, or internal data.
- [ ] Could bypass the governed API or trust membrane.
- [ ] Could let a watcher, connector, workflow, intake job, or model act as a publisher.
- [ ] Could make an uncited or unsupported claim appear authoritative.
- [ ] Could confuse a derived map, tile, graph, search result, summary, or AI response with canonical truth.
- [ ] Could affect rights, licensing, attribution, redistribution, consent, sovereignty, or source terms.
- [ ] Requires redaction, generalization, staged access, delayed release, or denial.
- [ ] Requires a correction path and rollback target before public release.
- [ ] No known trust, policy, rights, sensitivity, or release impact.
- [ ] `UNKNOWN`

**Impact explanation:**

-

## Security and public-safety review

- [ ] No security-sensitive behavior is proposed.
- [ ] Authentication or authorization changes.
- [ ] New network, secret, token, signing, or third-party integration.
- [ ] New upload, parsing, rendering, execution, or generated-content surface.
- [ ] New public route, data exposure, map layer, export, search, graph, or AI surface.
- [ ] Critical infrastructure, exact-sensitive location, living-person, DNA/genomic, private-land, or restricted-source implications.
- [ ] Security review is required before public discussion continues.
- [ ] `UNKNOWN`

**Private handling required:** `no / yes / NEEDS VERIFICATION`

## Proposed implementation approach

<!--
Optional. Keep design and paths PROPOSED. Prefer the smallest useful reversible
change. Do not turn this section into an unreviewed architecture decision.
-->

| Step | Proposed artifact or path | Owning root | Dependency | Reversible? | Status |
|---|---|---|---|---|---|
| 1 | | | | | `PROPOSED` |

### Companion artifacts

- [ ] Documentation or runbook
- [ ] ADR or migration/deprecation record
- [ ] Semantic contract
- [ ] Machine schema or context
- [ ] Policy bundle
- [ ] Positive and negative fixtures
- [ ] Validator and targeted tests
- [ ] Source descriptor or registry record
- [ ] Connector, pipeline, package, app, or UI implementation
- [ ] Review record or stewardship assignment
- [ ] Generated receipt, validation report, or proof
- [ ] Release manifest, correction notice, withdrawal notice, or rollback card
- [ ] Accessibility or user guidance
- [ ] None
- [ ] `UNKNOWN`

## Dependencies, compatibility, and operational cost

- Related issues, PRs, ADRs, or verification items:
- Upstream or external dependencies:
- Backward-compatibility requirements:
- Migration, backfill, or deprecation requirements:
- Storage, compute, network, or maintenance cost:
- Performance or scale expectations:
- Availability, offline, or no-network requirements:
- Observability, telemetry, audit, or receipt requirements:
- Staffing or reviewer requirements:
- Cost or ownership is `UNKNOWN`:

## Acceptance criteria

<!--
Make each criterion observable and independently evaluable. Include safe negative
behavior, trust visibility, documentation, and rollback—not only the happy path.
-->

| Criterion | Expected outcome | Evidence required |
|---|---|---|
| User or operator outcome | | Demonstration, test, or reviewed artifact |
| Positive path | | Deterministic test or fixture |
| Negative / denied path | | Negative fixture or policy test |
| Evidence and provenance | | Resolved evidence, receipt, or proof as applicable |
| Public-surface safety | | Boundary or exposure test |
| Accessibility / usability | | Review or test as applicable |
| Documentation | | Updated path or explicit N/A rationale |
| Compatibility / migration | | Compatibility test or migration evidence |
| Rollback | | Named reversal target and validation |
| No unintended publication | | Proof that PR, CI, watcher, or intake cannot publish directly |

## Validation and evaluation plan

### Before implementation

- [ ] Confirm repository state, owning roots, related ADRs, and overlapping work.
- [ ] Resolve `UNKNOWN` and `NEEDS VERIFICATION` items required for design.
- [ ] Define representative positive, negative, denied, abstain, stale, and error cases where applicable.
- [ ] Establish baseline behavior or metrics.
- [ ] Complete rights, sensitivity, security, and policy review where applicable.

### During implementation

- [ ] Add or update deterministic fixtures and targeted tests.
- [ ] Validate contracts, schemas, policy, provenance, and public boundaries affected by the change.
- [ ] Verify no direct publish path from watchers, connectors, CI, or model output.
- [ ] Record generated-work provenance where AI authors substantive artifacts.
- [ ] Update documentation alongside behavior.

### Post-implementation

- [ ] Evaluate every acceptance criterion as `PASS`, `FAIL`, `PARTIAL`, `NOT RUN`, `NOT APPLICABLE`, or `UNKNOWN`.
- [ ] Confirm correction and rollback paths.
- [ ] Confirm public-safe release state and reviewer approvals.
- [ ] Capture follow-up verification work without disguising it as completion.

## Rollout, release, correction, and rollback

- Proposed rollout stages:
- Feature flag or staged-access plan:
- Release/candidate manifest implications:
- Public communication or changelog:
- Correction path:
- Withdrawal or disable path:
- Rollback target:
- Data or artifact cleanup:
- Post-release monitoring:
- No release impact:

> [!NOTE]
> A pull request or merge does not publish KFM data, claims, layers, exports, or AI answers. Release and publication remain governed state transitions.

## Review and separation of duties

| Review role | Proposed reviewer or owner | Required because | Independent from author? |
|---|---|---|---|
| Repository / architecture steward | | | |
| Affected subsystem or domain steward | | | |
| Docs / accessibility reviewer | | | |
| Policy / rights / sensitivity / sovereignty reviewer | | | |
| Security reviewer | | | |
| Release / correction authority | | | |

- [ ] Required review roles are identified.
- [ ] A material author/approver conflict is avoided or explicitly held.
- [ ] Missing reviewer identity or authority produces `HOLD` / `NEEDS VERIFICATION`, not implicit approval.

## Priority and sequencing inputs

<!-- These fields inform triage; they do not create a roadmap commitment. -->

- User or governance value:
- Urgency or deadline:
- Cost of delay:
- Dependencies that must land first:
- Smallest useful deliverable:
- Follow-up phases:
- Reasons to defer or reject:
- Priority remains `UNKNOWN`:

## Related issues, PRs, ADRs, docs, research, or artifacts

<!-- Link only public-safe material. -->

-

## Submitter acknowledgements

- [ ] I understand this issue is a proposal, not an approved roadmap item or design.
- [ ] I used repository evidence for current-state claims and labeled uncertainty.
- [ ] I did not invent a file path, owner, workflow, API, label, or runtime behavior as current fact.
- [ ] I identified ADR triggers, affected responsibility roots, and governed public-path implications.
- [ ] I included measurable acceptance criteria, safe negative behavior, validation, and rollback.
- [ ] I did not include sensitive, restricted, private, or unreleased material.
- [ ] I understand implementation, release, publication, and issue closure require separate governed evidence.

## Maintainer triage

<!-- Maintainers may update this section after review. -->

### Classification

- [ ] Duplicate or covered by existing work
- [ ] Needs more evidence or problem definition
- [ ] `NEEDS VERIFICATION`
- [ ] Suitable for bounded backlog / planning
- [ ] Suitable for implementation scoping
- [ ] Requires ADR before implementation
- [ ] Requires security, policy, rights, sensitivity, sovereignty, or legal review
- [ ] Requires source-admission or release/correction review
- [ ] Not planned, with reason recorded
- [ ] Out of scope for KFM
- [ ] Route to bug, correction, documentation, or other intake process

### Definition of ready for implementation planning

- [ ] Problem and intended users are clear.
- [ ] Current-state claims are evidence-backed.
- [ ] Scope, non-goals, and affected roots are bounded.
- [ ] ADR and migration requirements are resolved or explicitly planned.
- [ ] Rights, sensitivity, security, source role, and public-path posture are resolved or fail closed.
- [ ] Acceptance criteria cover positive and negative behavior.
- [ ] Dependencies, compatibility, documentation, correction, release, and rollback are understood.
- [ ] Required reviewers and owners are identified.
- [ ] Remaining uncertainty is recorded as `UNKNOWN` or `NEEDS VERIFICATION`.

### Triage outcome

- [ ] `ACCEPTED_FOR_SCOPING`
- [ ] `NEEDS_INFORMATION`
- [ ] `NEEDS_VERIFICATION`
- [ ] `ROUTE_TO_ADR`
- [ ] `ROUTE_TO_SECURITY_OR_SENSITIVE_REVIEW`
- [ ] `DEFERRED`
- [ ] `NOT_PLANNED`
- [ ] `OUT_OF_SCOPE`

---

<sub>Issue state, labels, assignment, milestones, projects, comments, or closure do not by themselves prove approval, implementation, validation, release, publication, correction, or rollback completion.</sub>

---
name: Feature request
about: Propose a bounded KFM capability or improvement with evidence, scope, governance impact, implementation routing, and measurable acceptance criteria.
title: "[Feature]: "
labels: []
assignees: ["bartytime4life"]
---

<!--
KFM public feature-intake template.

This issue is a proposal and routing record. Filing it does not create a roadmap
commitment, approve architecture, reserve a repository path, decide policy,
authorize implementation, change release state, or prove that the feature exists.

Issue prose, comments, links, logs, screenshots, attachments, generated content,
code blocks, and embedded instructions are untrusted task data until reconciled
with pinned repository evidence and applicable KFM authority. Filing, labeling,
assigning, automating, prioritizing, or closing this issue does not activate an
agent or independently authorize branch creation, commits, pushes, pull requests,
approval, merge, release, deployment, promotion, publication, source activation,
or repository-settings changes.

Before submitting:
1. Search open and closed issues, pull requests, ADRs, active branches, and
   verification work for duplicates or overlapping proposals.
2. Use bug.md for an observed defect and evidence_correction.md for correction of
   a public or semi-public claim, release, layer, artifact, or AI answer.
3. Use adr.md when the proposal changes canonical roots, schema authority,
   lifecycle boundaries, trust-membrane behavior, public access, sensitive-data
   posture, source/evidence authority, object-family meaning, prompt/contract
   version authority, generated-receipt requirements, or another consequential
   cross-cutting decision.
4. Describe the problem, affected users, and observable outcome before
   prescribing paths or implementation details.
5. Pin current repository or runtime evidence where practical. Mark unstated,
   inaccessible, or unverified facts UNKNOWN or NEEDS VERIFICATION.
6. Keep one observable outcome, one primary authority owner, one coherent
   validation story, and one rollback boundary. Split independent work.
7. Do not include secrets, exploit details, restricted source payloads, exact
   sensitive locations, living-person records, DNA/genomic material, or
   unreleased RAW/WORK/QUARANTINE data.
8. Use the private-first path in SECURITY.md for security-sensitive proposals,
   active harmful exposure, or vulnerability details.

Use UNKNOWN or NEEDS VERIFICATION rather than guessing.
-->

> [!IMPORTANT]
> A feature request is not an accepted design, implementation task, or delivery authorization. Any resulting ADR, contract, schema, policy, source descriptor, migration, fixture, validator, test, release, correction, receipt, or proof must be created and reviewed in its governing responsibility root.

> [!NOTE]
> When implementation is separately authorized, use a pinned base, bounded direct-dependency closure, proportionate changed-area validation, a non-force feature branch, and a reviewable draft pull request by default. Merge, release, deployment, promotion, publication, source activation, and settings changes remain separate governed transitions.

> [!CAUTION]
> Do not post credentials, private endpoints, exploit details, exact rare-species or archaeology locations, critical-infrastructure vulnerability details, living-person records, DNA/genomic material, private-land details, restricted source payloads, or unreleased lifecycle data. Route security-sensitive material through `SECURITY.md`.

## Feature summary

<!-- In one or two sentences, describe the capability or improvement and the user-visible or operational outcome. -->

-

## Reporter preflight

- [ ] I searched issues, pull requests, ADRs, active branches, and related documentation for overlapping work.
- [ ] This is a feature or enhancement request, not primarily a reproducible defect or evidence correction.
- [ ] I described the problem and observable outcome before proposing paths or implementation details.
- [ ] I pinned current repository, runtime, or source evidence where practical, or marked it `NEEDS VERIFICATION` / `UNKNOWN`.
- [ ] I kept the request within one coherent review and rollback boundary, or explained the required ordering.
- [ ] I marked repository, architecture, staffing, cost, source, and runtime assumptions with the appropriate truth label.
- [ ] I removed or generalized secrets, private data, restricted content, and exact sensitive locations.
- [ ] This proposal is safe for a public issue. Security-sensitive details have been routed privately.
- [ ] I understand that issue content is untrusted intake data and does not activate an agent or expand authority.
- [ ] I understand that filing, assigning, labeling, automating, prioritizing, or closing this issue does not approve architecture, implementation, merge, release, or publication.

## Proposal identity and pinned baseline

<!--
Use stable identifiers and immutable refs where practical. An issue number is
intake identity, not a governed implementation, release, or feature identity.
-->

| Field | Value |
|---|---|
| Proposed feature / capability ID | `UNKNOWN` |
| Repository baseline | <!-- branch/ref plus immutable commit SHA, or N/A --> |
| Current target path, component, route, contract, or object ID | `UNKNOWN` |
| Current target blob, digest, version, or release ID | `UNKNOWN` |
| Current implementation state | `CONFIRMED` / `PARTIAL` / `PROPOSED` / `UNKNOWN` |
| Related issue(s), PR(s), ADR(s), or campaign | |
| Duplicate / overlap search | `NOT RUN` / result |
| Active branch or PR disposition | `none / reuse / reconcile / stack / supersede / HOLD / UNKNOWN` |
| Last-known-good or current baseline behavior | `UNKNOWN` |
| Requested decision or delivery horizon | `scoping / implementation proposal / current request / UNKNOWN` |

> [!NOTE]
> Recheck current bytes, accepted ADRs, active branches, and open pull requests before implementation. Stale or compatible overlap is not an automatic blocker; unresolved same-byte conflict, contradictory authority, or active edits that cannot be preserved produce `HOLD`.

## Current truth posture

<!-- Apply labels per material claim. Most new feature proposals begin as PROPOSED. -->

- [ ] `CONFIRMED` — verified from pinned repository evidence, tests, logs, accepted decisions, source records, or generated artifacts.
- [ ] `PROPOSED` — desired capability, design, placement, implementation, or delivery approach under review.
- [ ] `NEEDS VERIFICATION` — checkable, but not checked strongly enough to act as fact.
- [ ] `UNKNOWN` — unresolved and unsafe to assume.

**Overall proposal posture:** `PROPOSED`

### Claim-level truth ledger

| Claim or observation | Truth label | Evidence location | Limitation / next check |
|---|---|---|---|
| | `CONFIRMED` / `PROPOSED` / `NEEDS VERIFICATION` / `UNKNOWN` | | |

## Problem or opportunity

<!--
Describe the current limitation, unmet need, governance gap, user pain, or
opportunity. Separate current evidence from desired future behavior.
-->

-

### Current behavior or capability

<!-- Describe only what current evidence supports. -->

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

## Request and change classification

### Request type

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
- [ ] Focus Mode, governed AI, model adapter, prompt, or runtime-envelope improvement
- [ ] CI, workflow, dependency, deployment, or operations improvement
- [ ] Release, correction, withdrawal, rollback, or auditability improvement
- [ ] Accessibility, usability, performance, or reliability improvement
- [ ] Other:

### Change class

Select the strongest class currently supported.

- [ ] `EDITORIAL` — wording or presentation only.
- [ ] `ADDITIVE` — backward-compatible capability, guardrail, or documentation.
- [ ] `BEHAVIORAL` — current runtime, validation, workflow, policy application, or public behavior changes.
- [ ] `STRUCTURAL` — path ownership, generation, lifecycle, migration, or dependency topology changes.
- [ ] `AUTHORITY_CHANGING` — normative governance, policy meaning, object authority, responsibility, or public-path boundary changes.
- [ ] `NEEDS VERIFICATION`

### Implementation risk

- [ ] `LOW` — bounded editorial or deterministic additive work with no trust-boundary effect.
- [ ] `MODERATE` — multi-file or behavioral work with contained compatibility and rollback.
- [ ] `HIGH` — security, policy, source rights, persisted data, migration, public interface, workflow, or release implications.
- [ ] `CRITICAL` — harmful exposure, authority bypass, irreversible loss, or publication-integrity risk.
- [ ] `UNKNOWN`

### Materiality and urgency

- User or governance value:
- Urgency or deadline:
- Cost of delay:
- Public-safety or trust impact:
- Reuse across domains or components:
- Materiality remains `UNKNOWN`:

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

### Finite behavior outcomes

Check all outcomes the feature must represent explicitly.

- [ ] `ANSWER` / `ALLOW` / successful operation
- [ ] `ABSTAIN` / insufficient or stale evidence
- [ ] `DENY` / policy, rights, sensitivity, or access restriction
- [ ] `HOLD` / unresolved authority, review, identity, or dependency
- [ ] `ERROR` / operational failure with no unsafe fallback
- [ ] `NO_ACTION` / duplicate, no material change, or no useful bounded work
- [ ] `NOT_APPLICABLE`
- [ ] Other domain-specific finite state:

## Scope and non-goals

### In scope

-

### Non-goals

-

### Explicitly unchanged

<!-- Name trust boundaries, APIs, formats, roots, lifecycle stages, or compatibility promises that should remain unchanged. -->

-

## Review boundary and direct-dependency closure

<!--
Define one observable outcome, one primary authority owner, a bounded direct
companion set, one validation story, and one rollback boundary.
-->

| Boundary item | Decision |
|---|---|
| Observable feature outcome | |
| Primary authority owner | |
| Hand-edited canonical artifacts | |
| Generated or synchronized outputs | |
| Direct contracts / schemas / policy | |
| Direct fixtures / validators / tests | |
| Documentation / navigation / migration closure | |
| Work intentionally deferred or split | |
| Ordered or stacked dependency sequence | |
| Rollback / abandonment boundary | |
| Active overlap disposition | |

- [ ] The proposal has one coherent outcome, validation story, and rollback boundary.
- [ ] Direct dependencies are limited to buildability, semantic agreement, fixtures/tests, generation, navigation, compatibility, migration, correction, rollback, or repository-required receipts.
- [ ] Confirmed required consumers are included, ordered, or named as concrete blockers.
- [ ] Optional consumers and unrelated cleanup are excluded or listed as follow-up work.
- [ ] Generated or mirrored artifacts will be changed through their writable canonical source and deterministic regeneration.
- [ ] A governance change and implementation that depends on it are ordered separately.
- [ ] Any active overlap has a survivor, reconciliation, supersession, stack, or intentionally disjoint boundary.
- [ ] `NEEDS VERIFICATION`

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

### Evidence conflicts or alternative interpretations

| Source, object, or authority | Supported interpretation | Conflicting interpretation | Controlling evidence / next decision |
|---|---|---|---|
| | | | |

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
- [ ] Promotes or retires a compatibility or conditional root.
- [ ] Changes schema-home authority or contract/schema/policy placement.
- [ ] Changes the `CONTRACT_VERSION` pinned by an adopted operating contract or governed prompt.
- [ ] Changes generated-receipt requirements, validation, review controls, or process-memory authority.
- [ ] Splits, merges, bypasses, or redefines a lifecycle phase.
- [ ] Creates a parallel schema, contract, policy, source, registry, release, proof, receipt, catalog, or canonical-truth home.
- [ ] Bends a KFM invariant or trust-membrane boundary.
- [ ] Approves or changes a direct public-access path.
- [ ] Changes promotion, release, correction, withdrawal, or rollback gates.
- [ ] Changes sensitive-location, rights, sovereignty, consent, or geoprivacy posture.
- [ ] Changes source-ledger, source-role, evidence, deterministic identity, canonicalization, hashing, replay, or object-family meaning.
- [ ] Adopts or materially changes a model, runtime, prompt, or public-response envelope.
- [ ] Introduces or materially changes a steward role or separation-of-duties rule.
- [ ] Requires structural migration, semantic rename, compatibility break, or contract-version change.
- [ ] No formal ADR trigger identified.
- [ ] `NEEDS VERIFICATION`

**ADR issue or proposed ADR path:** `N/A / ADR-XXXX / related issue`

> [!IMPORTANT]
> Do not use this feature issue to approve an ADR-triggering decision. Route the decision through `.github/ISSUE_TEMPLATE/adr.md` and the governed `docs/adr/` process. Dependent implementation must wait for acceptance and a repinned base unless it can remain non-authoritative behind an existing accepted boundary.

## Directory Rules and placement

<!--
Paths are PROPOSED until checked against adopted Directory Rules, current
repository evidence, path-scoped instructions, and visible accepted ADRs.
Choose paths by responsibility, not topic.
-->

| Proposed or affected path | Owning responsibility root | Responsibility / authority role | Change class | Placement outcome | Directory Rules or ADR basis |
|---|---|---|---|---|---|
| | | | | `PLACE` / `SPLIT` / `MIGRATE` / `MIRROR` / `HOLD` / `DENY` | |

- [ ] Existing same-path edits were checked for canonical, generated, mirror, compatibility, migration, localization, or deprecation markers.
- [ ] New, moved, renamed, deleted, cross-root, or authority-bearing paths received full placement review.
- [ ] No new parallel authority home is proposed.
- [ ] Canonical, compatibility, generated, mirror, and external-storage surfaces remain distinct.
- [ ] Meaning, machine shape, policy, proof, lifecycle data, and release authority remain separated.
- [ ] Domain files stay inside the proper responsibility root rather than creating a new root-level domain folder.
- [ ] Any move, rename, delete, or authority change has a migration, deprecation, link-repair, and rollback plan.
- [ ] A docs/implementation conflict is surfaced as drift rather than silently normalized.
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
- [ ] Compatibility, transitional, or generated-output root:
- [ ] Other:
- [ ] `UNKNOWN`

**Cross-cutting explanation:** <!-- Required when several roots are affected. -->

### Object families and authority surfaces

- [ ] Source / source-admission objects
- [ ] Evidence / citation objects
- [ ] Semantic contracts
- [ ] Machine schemas / contexts
- [ ] Policy / rights / sensitivity decisions
- [ ] Identity / canonicalization / hashing / replay
- [ ] Validation / review records
- [ ] Receipts / proofs / attestations
- [ ] Catalog / graph / triplet projections
- [ ] Runtime / API / AI envelopes
- [ ] Layer / tile / style / export manifests
- [ ] Promotion / release / correction / rollback objects
- [ ] No object-family meaning change
- [ ] Other:

### Lifecycle stages and support planes

- [ ] Pre-RAW admission edge
- [ ] RAW
- [ ] WORK / QUARANTINE
- [ ] PROCESSED
- [ ] CATALOG / TRIPLET
- [ ] PUBLISHED
- [ ] Registry / receipt / proof / rollback support plane
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

**Trust-membrane notes:**

-

## Sources, data, evidence, and provenance

- New or changed source family / `SourceDescriptor`:
- Intended source role: `primary / corroborating / contextual / modeled / administrative / aggregate / synthetic / restricted / UNKNOWN`
- Rights, license, attribution, or source-term implications:
- Sensitivity, sovereignty, consent, or geoprivacy implications:
- Deterministic identity or canonicalization implications:
- `EvidenceRef` / `EvidenceBundle` requirements:
- Provenance, receipt, proof, validation-report, or lineage requirements:
- Freshness, valid-time, source-time, retrieval-time, processing-time, correction-time, or release-time requirements:
- Quarantine and malformed/ambiguous input behavior:
- Fixture posture: `synthetic / minimized / public-safe / no-network / UNKNOWN`
- Not applicable:

## Trust, policy, rights, and sensitivity impact

Check all that apply.

- [ ] Requires new or changed policy behavior.
- [ ] Could expose sensitive or restricted material.
- [ ] Could expose unreleased `RAW`, `WORK`, `QUARANTINE`, candidate, or internal data.
- [ ] Could bypass the governed API or trust membrane.
- [ ] Could let a watcher, connector, workflow, intake job, or model act as a publisher.
- [ ] Could make an uncited or unsupported claim appear authoritative.
- [ ] Could confuse a derived map, tile, graph, search result, summary, model, or AI response with canonical truth.
- [ ] Could affect rights, licensing, attribution, redistribution, consent, sovereignty, or source terms.
- [ ] Requires redaction, generalization, staged access, delayed release, quarantine, abstention, or denial.
- [ ] Requires a correction path and rollback target before public release.
- [ ] No known trust, policy, rights, sensitivity, or release impact.
- [ ] `UNKNOWN`

**Impact explanation:**

-

## Security and public-safety review

- [ ] No security-sensitive behavior is proposed.
- [ ] Authentication or authorization changes.
- [ ] New network, secret, token, signing, OIDC, or third-party integration.
- [ ] New upload, parsing, rendering, execution, or generated-content surface.
- [ ] New public route, data exposure, map layer, export, search, graph, or AI surface.
- [ ] New dependency, package lifecycle script, action, container, or binary.
- [ ] Critical infrastructure, exact-sensitive location, living-person, DNA/genomic, private-land, or restricted-source implications.
- [ ] Security review is required before public discussion continues.
- [ ] `UNKNOWN`

**Private handling required:** `no / yes / NEEDS VERIFICATION`

## Proposed implementation task contract

> [!IMPORTANT]
> The fields below support later implementation scoping. Completing them does not authorize repository mutation. A current direct implementation request and applicable safeguards still control any branch, commit, push, or pull request.

| Field | Proposed value |
|---|---|
| `task_id` | `PROPOSED` |
| `goal` | |
| `repository` | `bartytime4life/Kansas-Frontier-Matrix` / other |
| `base` | ref plus immutable commit / `NEEDS VERIFICATION` |
| `profile` | `DOCS_ONLY` / `DOCS_PLUS_DEPENDENCIES` / `REPOSITORY_SLICE` / `CAMPAIGN` / `GOVERNANCE_CHANGE` |
| `operation` | `MODERNIZE_MARKDOWN` / `CREATE_DOCUMENTATION` / `IMPLEMENT_REPOSITORY_SLICE` / `FIX_ISSUE` / `MIGRATE_STRUCTURE` / `IMPLEMENT_NEXT_GAP` / `RUN_CAMPAIGN` / other |
| `user_intent` | `DRAFT` / `IMPLEMENT` / `IMPLEMENT_AND_READY` / `UNKNOWN` |
| `authority_reference` | `CURRENT_USER_REQUEST` / accepted control / `UNKNOWN` |
| `delivery_target` | `ARTIFACT_ONLY` / `WORKSPACE_PATCH` / `PUSHED_BRANCH` / `DRAFT_PR` / `READY_PR` / `UNKNOWN` |
| `target_selectors` | paths, issue, component, acceptance criteria, or discovery selector |
| `writable_manifest` | exact intended paths; identify generated outputs |
| `in_scope` | implementation plus direct dependency closure |
| `non_goals` | merge, release, deployment, promotion, publication, settings, or other exclusions |
| `acceptance_criteria` | observable functional, structural, safety, and documentation outcomes |
| `validation_plan` | changed-area, safety, hosted, and delivery checks |
| `stop_conditions` | concrete conflict, safety, authority, sensitivity, or irreversibility conditions |
| `rollback` | abandon, revert, forward-fix, compatibility, and correction boundary |
| `budgets` | changed paths, roots, diff size, commits, PRs, time, and repair cycles |

## Proposed implementation approach

<!--
Keep design and paths PROPOSED. Prefer the smallest complete, useful, reversible
change. Do not turn this section into an unreviewed architecture decision.
-->

| Order | Proposed artifact or path | Owning root | Direct dependency | Hand-edited / generated | Reversible? | Status |
|---:|---|---|---|---|---:|---|
| 1 | | | | | | `PROPOSED` |

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
- [ ] Workflow or repository automation
- [ ] Review record or stewardship assignment
- [ ] Generated receipt, validation report, attestation, or proof
- [ ] Release manifest, correction notice, withdrawal notice, or rollback card
- [ ] Accessibility or user guidance
- [ ] None
- [ ] `UNKNOWN`

## Workflow-trigger and execution-safety preflight

Complete this section when `.github/workflows/`, automation, CI, external execution, or repository control may change.

- [ ] No workflow or externally executing behavior changes.
- [ ] Trigger events and trusted/untrusted input boundaries are identified.
- [ ] Token permissions, secrets, OIDC, environments, and write scopes are least privilege.
- [ ] No unsafe `pull_request_target`, secret-bearing untrusted execution, unrestricted self-hosted execution, or administrative write is introduced.
- [ ] Required check names and failure semantics remain stable, or their contract change is separately approved.
- [ ] Network access, downloads, dependency installation, and artifact retention are bounded and justified.
- [ ] The workflow cannot automatically merge, release, deploy, promote, publish, activate a source, or change settings from untrusted input.
- [ ] A failing baseline is classified as introduced, inherited, drift, or unrelated before repair.
- [ ] Not applicable.
- [ ] `NEEDS VERIFICATION`

**Threat or trigger notes:**

-

## Generated, mirrored, derived, and compatibility outputs

- Canonical writable source:
- Generator / tool / version:
- Deterministic command:
- Synchronized outputs:
- Mirror, localization, alias, or compatibility surface:
- Required indexes, links, manifests, or receipts:
- Drift detection or stale-output check:
- Regeneration cannot currently run safely; consequence:
- Not applicable:

- [ ] Generated outputs will not be hand-edited to bypass their source.
- [ ] Derived artifacts remain downstream carriers rather than canonical truth.
- [ ] Old generated-work receipts remain immutable; a new receipt will bind new AI-authored bytes when required.
- [ ] `NEEDS VERIFICATION`

## Dependencies, compatibility, and operational cost

- Related issues, PRs, ADRs, or verification items:
- Upstream or external dependencies:
- Backward-compatibility requirements:
- Migration, backfill, alias, or deprecation requirements:
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
| Negative / denied / abstain path | | Negative fixture, policy test, or finite outcome |
| Evidence and provenance | | Resolved evidence, receipt, or proof as applicable |
| Public-surface safety | | Boundary or exposure test |
| Security / rights / sensitivity | | Review, test, or explicit N/A rationale |
| Accessibility / usability | | Review or test as applicable |
| Documentation | | Updated path or explicit N/A rationale |
| Compatibility / migration | | Compatibility test or migration evidence |
| Generated-output closure | | Regeneration and drift evidence or N/A |
| Rollback / correction | | Named reversal target and validation |
| No unintended publication | | Proof that issue, PR, CI, watcher, connector, or model cannot publish directly |

## Validation and evaluation plan

### Before implementation

- [ ] Confirm repository identity, base commit, target blobs, owning roots, related ADRs, and overlapping work.
- [ ] Freeze the goal, initial writable manifest, direct dependencies, validation plan, stop conditions, and rollback boundary.
- [ ] Resolve `UNKNOWN` and `NEEDS VERIFICATION` items required to make the next action safe and materially correct.
- [ ] Define representative positive, negative, denied, abstain, stale, no-action, and error cases where applicable.
- [ ] Establish baseline behavior, tests, metrics, or current known failures.
- [ ] Complete rights, sensitivity, security, source, and policy review where applicable.

### During implementation

- [ ] Re-read target bytes after relevant base or branch drift.
- [ ] Add or update deterministic, rights-safe, no-network fixtures and targeted tests.
- [ ] Validate contracts, schemas, policy, provenance, identity, migration, and public boundaries affected by the change.
- [ ] Verify no direct publish path from watchers, connectors, CI, issue intake, or model output.
- [ ] Record generated-work provenance when AI authors substantive artifacts.
- [ ] Update documentation, indexes, links, and generated outputs alongside behavior.
- [ ] Inspect the complete diff for unrelated churn, missing companions, false claims, and recoverability.

### Post-implementation and delivery

- [ ] Evaluate every acceptance criterion as `PASS`, `FAIL`, `PARTIAL`, `PENDING`, `NOT RUN`, `NOT APPLICABLE`, or `UNKNOWN`.
- [ ] Verify exact branch head, parentage, base-to-head diff, changed paths, and consequential remote bytes.
- [ ] Verify pull-request base, head, open state, draft/ready state, and task identity.
- [ ] Separate local validation, hosted checks, delivery state, human review, merge, release, and publication state.
- [ ] Confirm correction and rollback paths.
- [ ] Capture follow-up verification work without disguising it as completion.

### Planned validation matrix

| Check or command | Scope | Required? | Expected outcome | Evidence location |
|---|---|---:|---|---|
| | | `yes` / `no` | `PASS` / `FAIL` / `PENDING` / `NOT RUN` / `N/A` / `UNKNOWN` | |

### Hosted checks and exact-head evidence

| Check | Required? | State | Exact run / head evidence |
|---|---:|---|---|
| | `yes` / `no` | `PASS` / `FAIL` / `PENDING` / `NOT RUN` / `UNKNOWN` | |

## Rollout, delivery, release, correction, and rollback

- Proposed rollout stages:
- Feature flag or staged-access plan:
- Requested repository delivery target:
- Draft/ready pull-request boundary:
- Merge prerequisite and owner:
- Release/candidate manifest implications:
- Public communication or changelog:
- Correction path:
- Withdrawal or disable path:
- Rollback target:
- Data, artifact, cache, index, graph, alias, or generated-output cleanup:
- Post-release monitoring:
- No release impact:

> [!NOTE]
> A branch, pull request, passing check, merge, tag, or GitHub release does not by itself publish KFM data, claims, layers, exports, or AI answers. Release and publication remain governed state transitions with their own evidence, review, correction, and rollback requirements.

## Review and separation of duties

| Review role | Proposed reviewer or owner | Required because | Independent from author? |
|---|---|---|---|
| Repository / architecture steward | | | |
| Affected subsystem or domain steward | | | |
| Docs / accessibility reviewer | | | |
| Policy / rights / sensitivity / sovereignty reviewer | | | |
| Security reviewer | | | |
| Workflow / operations reviewer | | | |
| Release / correction authority | | | |

- [ ] Required review roles are identified.
- [ ] A material author/approver conflict is avoided or explicitly held.
- [ ] Governance adoption and dependent implementation remain separate when required.
- [ ] Missing reviewer identity or authority produces `HOLD` / `NEEDS VERIFICATION`, not implicit approval.
- [ ] Human review, issue triage, implementation delivery, merge, release, and publication are represented as distinct states.

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

- [ ] I understand this issue is a proposal, not an approved roadmap item, design, task contract, or delivery authorization.
- [ ] I used current evidence for present-state claims and labeled uncertainty.
- [ ] I did not invent a file path, owner, workflow, API, label, source state, review, or runtime behavior as current fact.
- [ ] I identified ADR triggers, affected responsibility roots, lifecycle/public-path implications, and placement uncertainty.
- [ ] I bounded direct dependencies and excluded unrelated cleanup.
- [ ] I included measurable acceptance criteria, safe negative behavior, validation, delivery, and rollback.
- [ ] I identified generated/mirrored outputs and workflow-trigger risk where applicable.
- [ ] I did not include sensitive, restricted, private, or unreleased material.
- [ ] I understand implementation, merge, release, publication, and issue closure require separate governed evidence and authority.

## Maintainer triage

<!-- Maintainers may update this section after review. -->

### Intake classification

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

- [ ] Problem, affected users, current evidence, and desired outcome are clear.
- [ ] Scope, non-goals, one review boundary, and affected roots are bounded.
- [ ] Current target identity, baseline, overlap, and required authority are resolved or explicitly planned.
- [ ] ADR, placement, migration, generated-output, and compatibility requirements are resolved or ordered.
- [ ] Rights, sensitivity, security, source role, and public-path posture are resolved or fail closed.
- [ ] Acceptance criteria cover positive, negative, denied, abstain, stale, and error behavior as applicable.
- [ ] Direct dependencies, documentation, delivery, correction, release, and rollback are understood.
- [ ] Required reviewers and owners are identified.
- [ ] Remaining uncertainty is recorded as `UNKNOWN` or `NEEDS VERIFICATION`.

### Proposed implementation routing

| Field | Maintainer disposition |
|---|---|
| Task ID | |
| Resolved profile / operation | |
| Authority reference | |
| Delivery target | `ARTIFACT_ONLY` / `WORKSPACE_PATCH` / `PUSHED_BRANCH` / `DRAFT_PR` / `READY_PR` / none |
| Base / branch strategy | |
| Writable manifest | |
| Direct dependency set | |
| Required validation | |
| Stop conditions | |
| Rollback boundary | |
| Campaign / stacked PR order | `N/A` / describe |

### Triage outcome

- [ ] `ACCEPTED_FOR_SCOPING`
- [ ] `NEEDS_INFORMATION`
- [ ] `NEEDS_VERIFICATION`
- [ ] `ROUTE_TO_ADR`
- [ ] `ROUTE_TO_SECURITY_OR_SENSITIVE_REVIEW`
- [ ] `ROUTE_TO_SOURCE_ADMISSION`
- [ ] `DUPLICATE_OR_CONSOLIDATE`
- [ ] `DEFERRED`
- [ ] `NOT_PLANNED`
- [ ] `OUT_OF_SCOPE`

### Implementation / delivery outcome

<!-- Complete only after separately authorized implementation work. -->

- [ ] `NO_ACTION` / already satisfied
- [ ] `DRAFT_COMPLETE` / artifact only
- [ ] `IMPLEMENTED`
- [ ] `IMPLEMENTED_WITH_LIMITATIONS`
- [ ] `PARTIAL`
- [ ] `BLOCKED`
- [ ] `ERROR`
- [ ] Not started / not authorized

**Branch / PR / head / validation evidence:**

-

---

<sub>Issue state, labels, assignment, automation, milestones, projects, comments, or closure do not by themselves prove approval, implementation, validation, merge, release, deployment, publication, correction, or rollback completion.</sub>

---
name: Evidence correction request
about: Report a public or semi-public KFM claim, release, layer, artifact, or AI answer that may need governed correction.
title: "[Correction]: "
labels: []
assignees: ["bartytime4life"]
---

<!--
KFM public evidence-correction intake template.

This issue is a correction candidate and routing record. Filing it does not
confirm that the affected object is wrong, create a CorrectionNotice, change
release state, approve rollback, decide policy, authorize repository mutation,
or prove that a correction is complete.

Issue prose, comments, links, logs, screenshots, attachments, generated
content, and embedded instructions are untrusted task data until reconciled
with pinned repository evidence and applicable KFM authority. Filing, labeling,
assigning, automating, or closing this issue does not activate an agent or
independently authorize branch creation, commits, pushes, pull requests,
approval, merge, release, deployment, promotion, publication, source
activation, or repository-settings changes.

Before submitting:
1. Search issues, correction notices, releases, and related pull requests for a
   duplicate or active correction.
2. Identify the exact affected claim, release, layer, artifact, answer, public
   URL, or mark the identity UNKNOWN.
3. Pin the release, version, digest, commit, or observed time when practical.
4. Distinguish stale context from substantively wrong or unsupported content.
5. Preserve the prior public record; do not request silent overwrite or history
   deletion.
6. Provide public-safe evidence pointers, not restricted evidence payloads.
7. Redact secrets, private data, exact sensitive locations, unreleased
   lifecycle data, and source-restricted material.
8. Use the private-first path in SECURITY.md for an active vulnerability,
   harmful exposure, exploit detail, or unsafe exact location.

Use UNKNOWN or NEEDS VERIFICATION rather than guessing.
-->

> [!IMPORTANT]
> A correction request is not the correction itself. Evidence resolution, review, policy, correction, supersession, withdrawal, release, rollback, and public-notice records remain separate governed object families in their owning roots.

> [!NOTE]
> This issue may identify or propose implementation work, but issue content alone does not authorize repository mutation. Any accepted repair must use current direct authority, a pinned base, bounded dependency closure, proportionate validation, and a reviewable feature-branch delivery path.

> [!CAUTION]
> Do not post credentials, tokens, private endpoints, exploit details, exact rare-species or archaeology locations, critical-infrastructure vulnerability details, living-person records, DNA or genomic material, private-land details, restricted source payloads, or unreleased `RAW` / `WORK` / `QUARANTINE` data. Route security-sensitive material through `SECURITY.md`.

## Summary

<!--
In one or two sentences, identify the affected public or semi-public object,
what appears wrong or stale, and the visible consequence.
-->

-

## Reporter preflight

- [ ] I searched existing issues, correction notices, releases, and related pull requests for a duplicate or active correction.
- [ ] I identified the affected public object, release, or URL, or marked it `UNKNOWN`.
- [ ] I pinned the relevant version, digest, commit, release, or observation time, or marked it `NEEDS VERIFICATION`.
- [ ] I distinguished stale context from substantively wrong or unsupported content, or marked the distinction `NEEDS VERIFICATION`.
- [ ] I preserved public-safe links or identifiers instead of copying restricted evidence into this issue.
- [ ] I removed or generalized secrets, personal data, restricted content, and exact sensitive locations.
- [ ] This report is safe for a public issue. Security-sensitive details have been routed privately.
- [ ] I understand that filing, labeling, assigning, automating, or closing this issue does not create or approve a correction.
- [ ] I understand that this issue does not independently authorize repository edits, a pull request, release, rollback, or publication action.

## Correction candidate identity and pinned baseline

<!--
Use stable identifiers and immutable refs where practical. A GitHub issue
number is intake identity, not the governed correction identity.
-->

| Field | Value |
|---|---|
| Proposed correction candidate ID | `UNKNOWN` |
| Repository baseline | <!-- branch/ref plus immutable commit SHA, or N/A --> |
| Affected claim ID | `UNKNOWN` |
| Affected release ID / `ReleaseManifest` | `UNKNOWN` |
| Layer / dataset / artifact ID | `UNKNOWN` |
| Catalog / triplet / graph object | `UNKNOWN` |
| AI answer / `RuntimeResponseEnvelope` / receipt | `UNKNOWN` |
| Public URL, route, map view, export, or document | `UNKNOWN` |
| Domain / feature family | `UNKNOWN` |
| Current release or review state | `UNKNOWN` |
| Current `spec_hash`, digest, version, or commit | `UNKNOWN` |
| First observed date/time | `UNKNOWN` |
| Last known supportable state | `UNKNOWN` |
| Related issue(s), correction(s), or PR(s) | |
| Duplicate / overlap check | `NOT RUN` / result |

> [!NOTE]
> Recheck identity, current bytes, active branches, and open pull requests before implementation. A stale issue or historical branch is evidence, not a perpetual veto; an unresolved same-byte or semantic-authority conflict is a `HOLD`.

## Current truth posture

<!-- Apply labels per material claim. One report may contain several labels. -->

- [ ] `CONFIRMED` — verified from pinned repository evidence, source records, tests, logs, or governed artifacts.
- [ ] `PROPOSED` — suggested correction, explanation, containment, or release response under review.
- [ ] `NEEDS VERIFICATION` — checkable, but not checked strongly enough to act as fact.
- [ ] `UNKNOWN` — unresolved and unsafe to assume.

**Reporter-selected posture:** `NEEDS VERIFICATION`

### Claim-level truth ledger

| Claim or observation | Truth label | Evidence location | Limitation / next check |
|---|---|---|---|
| | `CONFIRMED` / `PROPOSED` / `NEEDS VERIFICATION` / `UNKNOWN` | | |

## Urgency, consequence, and materiality

Select the closest current classification. Do not expose sensitive details to justify urgency.

- [ ] `C0 — Emergency containment`: active harmful exposure, trust-membrane bypass, unsafe publication, or material data-loss risk. Use private handling when details are sensitive.
- [ ] `C1 — High`: materially unsupported public claim, rights/sensitivity breach, release-integrity failure, or broad derivative impact.
- [ ] `C2 — Moderate`: substantive defect with bounded exposure or a safe temporary mitigation.
- [ ] `C3 — Low`: clarification, stale marker, narrow wording correction, or limited derivative impact.
- [ ] `UNKNOWN`

**Who or what may be affected:**

-

**Blast radius / consequence:**

-

**Materiality dimensions:**

- [ ] Public safety or harmful precision
- [ ] Rights, license, attribution, consent, sovereignty, or redistribution
- [ ] Evidence authority or source-role integrity
- [ ] Review, policy, proof, receipt, or release integrity
- [ ] Public map, API, export, search, graph, catalog, or AI interpretation
- [ ] Correction, withdrawal, rollback, or public-notice obligation
- [ ] Limited editorial or freshness-only impact
- [ ] `UNKNOWN`

## Correction classification

### Stale versus wrong

- [ ] **Stale** — the content may have been supportable when released, but freshness, review, source, policy, model, geography, or time context has aged.
- [ ] **Wrong / unsupported** — the substance is incorrect, no longer supported, or violates rights, sensitivity, policy, or release requirements.
- [ ] **Both**
- [ ] `NEEDS VERIFICATION`
- [ ] `UNKNOWN`

### Defect or correction class

Check all that apply.

- [ ] Evidence gap or unresolved `EvidenceRef`
- [ ] Evidence no longer supports the published claim
- [ ] Source-role misclassification or authority upcast
- [ ] Source update, silent replacement, or source-version mismatch
- [ ] Rights, license, attribution, consent, or sovereignty change
- [ ] Sensitivity, geoprivacy, or restricted-location exposure
- [ ] Geometry, CRS, topology, scale, or generalization defect
- [ ] Observation, valid, source, retrieval, processing, correction, or release-time defect
- [ ] Identity, canonicalization, digest, alias, or replay defect
- [ ] Policy or admissibility defect
- [ ] Validation, review, proof, receipt, signature, or integrity defect
- [ ] Rendering, style, tile, popup, Evidence Drawer, story, or export defect
- [ ] Governed API, catalog, graph, search, index, or route defect
- [ ] Focus Mode, AI answer, model adapter, citation, or runtime-envelope defect
- [ ] Catalog closure, manifest, release-lineage, or correction-propagation defect
- [ ] Documentation or public-notice defect
- [ ] Clarification only; no release-state change expected
- [ ] Other:

### Change class for a possible repair

- [ ] `EDITORIAL` — wording or presentation only.
- [ ] `ADDITIVE` — backward-compatible correction support or regression protection.
- [ ] `BEHAVIORAL` — runtime, validation, policy application, or public behavior changes.
- [ ] `STRUCTURAL` — path, ownership, generation, lifecycle, or dependency topology changes.
- [ ] `AUTHORITY_CHANGING` — normative governance, policy meaning, object authority, or public-path boundary changes.
- [ ] `NEEDS VERIFICATION`

> [!IMPORTANT]
> A proposed repair that changes governance, normative policy, authority ownership, lifecycle meaning, or canonical placement requires the corresponding adopted decision path. A correction issue must not treat its own proposal as accepted authority.

## Current published statement or behavior

<!--
Quote only the smallest necessary public-safe excerpt, or link to the affected
object. Preserve the released wording and identity for correction lineage.
-->

-

## What appears wrong

<!-- Describe the observed problem without overstating what is proven. -->

-

## Proposed corrected statement or posture

<!--
Mark this PROPOSED. Examples include a corrected claim, narrower scope, stale
marker, caveat, ABSTAIN, DENY, redaction, generalization, supersession,
withdrawal, or rollback review.
-->

**Status:** `PROPOSED`

-

### Proposed finite correction outcome

Select the narrowest outcome currently supported.

- [ ] `NO_ACTION` — current public state remains supportable; record the rationale.
- [ ] `CLARIFY` — improve explanation without changing the supported claim or release state.
- [ ] `MARK_STALE` — retain history and visibly mark freshness/review limitations.
- [ ] `CORRECT` — issue a governed correction while preserving prior lineage.
- [ ] `NARROW` / `ABSTAIN` — reduce scope or withhold the unsupported assertion.
- [ ] `DENY` / `REDACT` / `GENERALIZE` — restrict unsafe or inadmissible exposure.
- [ ] `SUPERSEDE` — replace through an explicit successor and forward/back links.
- [ ] `WITHDRAW` — remove the current release or public alias through governed withdrawal.
- [ ] `ROLLBACK_REVIEW` — assess return to a last-known-good target.
- [ ] `HOLD` — required evidence, authority, policy, or review is unresolved.
- [ ] `ERROR` — correction processing failed and no unsafe fallback is allowed.
- [ ] `NEEDS VERIFICATION`

**Reason code or bounded rationale:**

-

## Scope, non-goals, and review boundary

### In scope

-

### Non-goals

-

### Explicitly unchanged

-

### Review-boundary and dependency-closure ledger

<!--
Define one observable correction outcome, one primary authority owner, a
bounded direct dependency set, and one rollback boundary.
-->

| Boundary item | Decision |
|---|---|
| Observable correction outcome | |
| Primary authority owner | |
| Affected canonical object(s) | |
| Direct companion changes required | |
| Derivatives that must be revalidated or rebuilt | |
| Work intentionally deferred or split | |
| Ordered or stacked dependency sequence | |
| Rollback / abandonment boundary | |
| Active overlap disposition | |

- [ ] The proposed work has one coherent correction outcome and rollback boundary.
- [ ] Direct dependencies are limited to what is required for evidence, policy, review, validation, propagation, release, correction, and rollback closure.
- [ ] Optional consumers and unrelated cleanup are excluded or listed as follow-up work.
- [ ] Generated or mirrored artifacts will be changed through their writable canonical source and deterministic regeneration.
- [ ] A governance decision and implementation that depends on it are ordered separately.
- [ ] Any active overlap has a survivor, consolidation, supersession, or intentionally disjoint boundary.
- [ ] `NEEDS VERIFICATION`

## Evidence basis

<!--
EvidenceBundle outranks generated summaries. Use immutable paths, IDs, hashes,
source versions, or public-safe authoritative links. Memory and repeated prose
are not evidence.
-->

| Evidence role | Identifier or location | Observation supported | Resolution / validation state | Limitation |
|---|---|---|---|---|
| Existing published evidence | | | | |
| New or corrected evidence | | | | |
| Corroborating evidence | | | | |
| Contextual evidence | | | | |
| Conflicting evidence | | | | |

### Evidence and source objects

| Field | Value |
|---|---|
| `SourceDescriptor` / source ID | `UNKNOWN` |
| Source role | `primary / corroborating / contextual / restricted / modeled / aggregate / synthetic / UNKNOWN` |
| Source version / retrieval time | `UNKNOWN` |
| `EvidenceRef` | `UNKNOWN` |
| Resolved `EvidenceBundle` | `UNKNOWN` |
| Citation or provenance record | `UNKNOWN` |
| Validation report / proof pack | `UNKNOWN` |
| `ReviewRecord` | `UNKNOWN` |
| `PolicyDecision` | `UNKNOWN` |
| Generated receipt / run receipt | `UNKNOWN` |
| Release / correction / withdrawal record | `UNKNOWN` |

- [ ] Every evidence-dependent claim resolves from `EvidenceRef` to an inspectable `EvidenceBundle`, or the outcome abstains/denies.
- [ ] Source roles remain distinct; modeled, aggregate, synthetic, administrative, or contextual material is not upcast.
- [ ] Conflicting, missing, stale, or denied evidence is visible.
- [ ] Rights and sensitivity metadata are current.
- [ ] Evidence cannot be safely posted publicly; a restricted review path is identified.
- [ ] The current public object is not being treated as self-proving evidence.
- [ ] `NEEDS VERIFICATION`

### Evidence conflicts

<!--
Record authoritative conflicts instead of selecting the most convenient source.
-->

| Source or object | Supported interpretation | Conflicting interpretation | Controlling authority / next decision |
|---|---|---|---|
| | | | |

## Verification and reproduction

<!-- Explain how a reviewer can verify the concern using public-safe inputs. -->

### Minimal verification steps

1.
2.
3.

```bash
# Optional safe, redacted, deterministic, no-network commands.
```

### Expected result

-

### Observed result

-

### Verification already attempted

- [ ] Confirmed against the named published release or artifact.
- [ ] Re-resolved the cited evidence bundle.
- [ ] Compared source versions, digests, or retrieval timestamps.
- [ ] Re-ran relevant schema or contract validation.
- [ ] Re-ran policy, rights, sensitivity, or public-safe transform checks.
- [ ] Re-ran positive and negative fixtures.
- [ ] Compared current and prior release manifests, signatures, aliases, or digests.
- [ ] Checked map, UI, export, API, graph, search, catalog, and AI derivatives.
- [ ] Tested correction, withdrawal, cache invalidation, or rollback behavior.
- [ ] No verification performed yet.
- [ ] `UNKNOWN`

### Reproducibility

- [ ] Deterministic
- [ ] Intermittent
- [ ] Source-dependent
- [ ] Time-dependent
- [ ] Environment-dependent
- [ ] Cannot reproduce with public-safe evidence
- [ ] `UNKNOWN`

**Conditions and limitations:**

-

## Spatial and temporal scope

> [!WARNING]
> Generalize locations involving archaeology, burial or sacred sites, rare species or plants, habitat, critical infrastructure, private land, living people, DNA/genomics, or steward-controlled records. Reference the restricted evidence path rather than posting exact details.

| Field | Value |
|---|---|
| Generalized geographic area | `UNKNOWN` |
| Geometry type / CRS / scale | `UNKNOWN` |
| Exact sensitive geometry involved? | `No / Yes / UNKNOWN` |
| Observation / valid time | `UNKNOWN` |
| Source publication / retrieval time | `UNKNOWN` |
| Processing / ingest time | `UNKNOWN` |
| Original release time | `UNKNOWN` |
| Correction / review time | `UNKNOWN` |
| Freshness tolerance or review cycle | `UNKNOWN` |
| Stale or future-dated context suspected? | `No / Yes / UNKNOWN` |
| Bitemporal or supersession implications | `UNKNOWN` |

## Affected surfaces and derivative impact

### Responsibility roots

Check only roots with confirmed or proposed direct impact.

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
- [ ] Compatibility or generated-output root:
- [ ] External released artifact or service:
- [ ] `UNKNOWN`

**Directory Rules / owning-root basis:**

-

### Object families

- [ ] Claim / assertion / observation
- [ ] `SourceDescriptor` / source-admission record
- [ ] `EvidenceRef` / `EvidenceBundle` / citation
- [ ] `PolicyDecision` / sensitivity / rights record
- [ ] Validation / review record
- [ ] Receipt / proof / signature / attestation
- [ ] Catalog / triplet / graph / search index
- [ ] Layer / tile / style / export / scene manifest
- [ ] Runtime / API / Focus Mode / AI envelope
- [ ] `ReleaseManifest` / promotion decision
- [ ] `CorrectionNotice` / supersession / withdrawal / rollback
- [ ] Documentation / public notice
- [ ] `UNKNOWN`

### Lifecycle and governed interfaces

- [ ] Pre-RAW admission edge
- [ ] `RAW`
- [ ] `WORK` / `QUARANTINE`
- [ ] `PROCESSED`
- [ ] `CATALOG` / `TRIPLET`
- [ ] `PUBLISHED`
- [ ] Receipts / proofs / registry / rollback support
- [ ] Governed API
- [ ] Explorer / MapLibre / Evidence Drawer
- [ ] Focus Mode / governed AI
- [ ] Search / graph / catalog / export
- [ ] Release / publication
- [ ] No confirmed lifecycle or public-interface impact
- [ ] `UNKNOWN`

### Known derivatives and dependents

| Dependent object or surface | Current exposure | Required action | Owner / reviewer | Status |
|---|---|---|---|---|
| | | | | |

> [!IMPORTANT]
> Tiles, maps, summaries, dashboards, graph projections, indexes, screenshots, and AI answers are downstream carriers. Correcting one carrier does not complete correction when the underlying claim, evidence, manifest, alias, cache, or release lineage remains inconsistent.

## Trust, policy, rights, and sensitivity impact

- [ ] Could expose sensitive or restricted material.
- [ ] Could expose unreleased `RAW`, `WORK`, `QUARANTINE`, candidate, or internal data.
- [ ] Could bypass the governed API or trust membrane.
- [ ] Could make an unsupported or uncited claim appear authoritative.
- [ ] Could collapse source roles or confuse derived output with canonical truth.
- [ ] Could affect licensing, attribution, consent, redistribution rights, or sovereignty.
- [ ] Could break deterministic identity, receipt/proof linkage, or correction lineage.
- [ ] Could require immediate public disablement or access restriction.
- [ ] Could require redaction, generalization, delayed access, or restricted review.
- [ ] Could require public correction, supersession, withdrawal, rollback, or release hold.
- [ ] No known trust, policy, rights, sensitivity, or release impact.
- [ ] `UNKNOWN`

**Impact explanation:**

-

**Required private handling or additional reviewer:**

-

## Immediate containment or public-surface action

<!--
Use only safe, reversible actions. A public issue must not contain exploit or
sensitive implementation detail.
-->

- [ ] No immediate containment appears necessary.
- [ ] Add a visible stale or review-pending marker.
- [ ] Disable or restrict an affected route, layer, export, answer, or alias pending review.
- [ ] Remove an unsafe answer while preserving its evidence and receipt trail.
- [ ] Freeze a generated mirror and repair its canonical source.
- [ ] Hold release, promotion, or publication.
- [ ] Withdraw or roll back to a previously reviewed target.
- [ ] Private security or incident handling is required.
- [ ] `NEEDS VERIFICATION`

**Suggested containment:**

-

**Last-known-good / rollback target:**

-

**Containment expiry or review trigger:**

-

## Proposed correction plan

<!--
A correction is an ordered governed transition, not a wording-only file edit.
Delete phases that are not applicable; do not combine independent authority
decisions into one unreviewed step.
-->

| Order | Phase | Required artifact or action | Owner role | Exit evidence |
|---:|---|---|---|---|
| 1 | Contain | | | |
| 2 | Re-resolve identity and evidence | | | |
| 3 | Decide policy, rights, sensitivity, and review posture | | | |
| 4 | Implement the smallest dependency-closed repair | | | |
| 5 | Validate affected and negative paths | | | |
| 6 | Propagate to derivatives, aliases, caches, indexes, and public surfaces | | | |
| 7 | Record correction, supersession, withdrawal, release, or rollback | | | |
| 8 | Verify public read-back and monitoring | | | |

### Compatibility, migration, and regeneration

- Compatibility or deprecation window:
- Canonical source and generated/mirror outputs:
- Schema, contract, policy, or API versioning:
- Data backfill or reprocessing:
- Cache / index / graph invalidation:
- Documentation and public-notice update:
- Correction replay / deterministic rebuild:
- Abandonment path before merge or release:

## Suggested correction lineage

<!-- These are requested follow-up artifacts, not approvals. -->

- [ ] `CorrectionNotice`
- [ ] `SupersessionNotice`
- [ ] `WithdrawalNotice`
- [ ] `RollbackCard`
- [ ] Superseding `ReleaseManifest`
- [ ] Stale-state marker only
- [ ] Policy hold or review hold
- [ ] Redaction or generalization receipt
- [ ] Corrected `EvidenceBundle` / citation lineage
- [ ] Corrected validation report / proof pack
- [ ] Changelog or public notice
- [ ] No release-facing notice after review
- [ ] Other:

### Existing and proposed lineage

| Relationship | Current pointer | Proposed pointer | Status |
|---|---|---|---|
| Affected release / object | | | |
| Corrects | | | |
| Supersedes | | | |
| Superseded by | | | |
| Withdraws | | | |
| Rollback target | | | |
| Correction notice | | | |
| Withdrawal notice | | | |
| Public notice / changelog | | | |

### Deterministic correction identity

| Field | Value |
|---|---|
| Correction ID strategy | `UNKNOWN` |
| Canonicalization / hash profile | `UNKNOWN` |
| Prior object digest | `UNKNOWN` |
| Corrected object digest | `UNKNOWN` |
| Replay or rebuild manifest | `UNKNOWN` |
| Alias / cache invalidation receipt | `UNKNOWN` |

## Public-safe correction summary

<!-- Draft only. Do not include restricted evidence or exact sensitive details. -->

**Status:** `PROPOSED`

-

## Review and separation of duties

| Role | Proposed reviewer / owner | Required because | Independent from detector/author? |
|---|---|---|---|
| Affected domain or subsystem steward | | | |
| Evidence / source reviewer | | | |
| Correction reviewer | | | |
| Policy / rights / sensitivity reviewer | | | |
| Release authority | | | |
| Docs / public-notice reviewer | | | |
| AI surface steward, when applicable | | | |
| Security / privacy / sovereignty reviewer, when applicable | | | |

- [ ] Detector / author is identified.
- [ ] Required reviewer roles are identified.
- [ ] Material author/approver separation is preserved.
- [ ] The detector, AI author, validator, or passing workflow is not treated as approval.
- [ ] Missing reviewer authority produces `HOLD` / `NEEDS VERIFICATION`, not implicit approval.
- [ ] Single-owner bootstrap or emergency containment, if used, is explicit and time-bounded.

## Validation and acceptance

<!--
Correction is not complete merely because public wording changes. Distinguish
changed-area, safety, delivery, and hosted checks. A passing check proves only
its stated scope.
-->

### Required criteria

| Criterion | Expected outcome | Evidence required |
|---|---|---|
| Affected object identity | Exact claim, release, layer, artifact, or answer is named | Stable ID, path, URL, digest, or manifest pointer |
| Evidence support | Corrected posture is supported, or the system abstains/denies | Resolved evidence and source-role review |
| Prior record preservation | Original release and correction history remain inspectable | Supersession/correction lineage |
| Policy and sensitivity | Rights, sensitivity, sovereignty, and public-safe posture pass | `PolicyDecision` / review evidence |
| Dependency closure | Contracts, schemas, validators, fixtures, docs, manifests, and derivatives agree where applicable | Bounded changed-path and validation ledger |
| Derivative closure | Known maps, exports, APIs, search, graph, catalog, caches, and AI derivatives are reviewed | Impact inventory and read-back validation |
| Release state | Correction, withdrawal, supersession, or rollback is governed | `ReleaseManifest` / `RollbackCard` / decision |
| Public communication | Public-safe correction or notice is linked when required | Approved notice or no-notice decision |
| Regression protection | The defect is detectable in future | Test, fixture, validator, or monitoring evidence |
| Rollback | A clear reversal or last-known-good target exists | Commit, manifest, digest, artifact, or alias |
| Documentation | Behavior-changing guidance is updated or explicitly not applicable | Changed path or rationale |

### Validation ledger

| Class | Check or command | Scope | State | Evidence |
|---|---|---|---|---|
| `REQUIRED_CHANGED_AREA` | | | `PASS` / `FAIL` / `PENDING` / `NOT RUN` / `N/A` / `UNKNOWN` | |
| `REQUIRED_SAFETY` | | | `PASS` / `FAIL` / `PENDING` / `NOT RUN` / `N/A` / `UNKNOWN` | |
| `REQUIRED_DELIVERY` | | | `PASS` / `FAIL` / `PENDING` / `NOT RUN` / `N/A` / `UNKNOWN` | |
| `HOSTED_CI` | | | `PASS` / `FAIL` / `PENDING` / `NOT RUN` / `N/A` / `UNKNOWN` | |
| `OBSERVATIONAL` | | | `PASS` / `FAIL` / `PENDING` / `NOT RUN` / `N/A` / `UNKNOWN` | |

### Acceptance outcome

- [ ] `PASS`
- [ ] `FAIL`
- [ ] `PARTIAL`
- [ ] `PENDING`
- [ ] `NOT RUN`
- [ ] `NOT APPLICABLE`
- [ ] `UNKNOWN`

### Failure signals

-

### Post-correction verification

-

## Implementation and delivery boundary

> [!IMPORTANT]
> An accepted correction decision and an authorized repository implementation are separate transitions. The issue may define the requested outcome, but repository mutation requires current authority, pinned current bytes, overlap reconciliation, a feature branch, proportionate validation, non-force delivery, and remote read-back.

| Field | Maintainer value |
|---|---|
| Resolved implementation intent | `READ_ONLY` / `DRAFT` / `IMPLEMENT` / `IMPLEMENT_AND_READY` / `UNKNOWN` |
| Operation | `AUDIT` / `PLAN` / `MODERNIZE_MARKDOWN` / `FIX_ISSUE` / `IMPLEMENT_REPOSITORY_SLICE` / `MIGRATE_STRUCTURE` / `UNKNOWN` |
| Profile | `DOCS_ONLY` / `DOCS_PLUS_DEPENDENCIES` / `REPOSITORY_SLICE` / `GOVERNANCE_CHANGE` / `UNKNOWN` |
| Immutable base | |
| Writable manifest | |
| Delivery target | `ARTIFACT_ONLY` / `WORKSPACE_PATCH` / `PUSHED_BRANCH` / `DRAFT_PR` / `READY_PR` / `UNKNOWN` |
| Branch / pull request | |
| Hosted checks | `PASS` / `FAIL` / `PENDING` / `NOT RUN` / `UNKNOWN` |
| Run outcome | `IMPLEMENTED` / `IMPLEMENTED_WITH_LIMITATIONS` / `PARTIAL` / `NO_OP` / `READ_ONLY_COMPLETE` / `BLOCKED` / `ERROR` / `UNKNOWN` |
| Rollback reference | |

- [ ] No direct default-branch write, force-push, self-approval, merge, release, deploy, promotion, publication, or settings change is implied.
- [ ] A draft pull request may be delivered with hosted checks pending when changed-area and safety requirements permit; `READY_PR` requires required checks and no review-blocking defect.
- [ ] Remote bytes, branch head, base-to-head diff, changed paths, and PR state will be read back before delivery is claimed.
- [ ] This issue requires no repository mutation.
- [ ] `UNKNOWN`

## Related issues, PRs, records, runs, or artifacts

<!-- Link only public-safe material. -->

-

## Maintainer triage

### Task contract

| Field | Maintainer decision |
|---|---|
| Task ID | |
| Observable goal | |
| Authority reference | `CURRENT_USER_REQUEST` / accepted control / `UNKNOWN` |
| Primary owner | |
| Immutable base | |
| Change class | `EDITORIAL` / `ADDITIVE` / `BEHAVIORAL` / `STRUCTURAL` / `AUTHORITY_CHANGING` |
| In scope | |
| Non-goals | |
| Acceptance criteria | |
| Validation plan | |
| Stop conditions | |
| Rollback / correction boundary | |
| Change budget | |

### Classification

- [ ] Duplicate
- [ ] Correction candidate reproduced and `CONFIRMED`
- [ ] Stale only; route to freshness/review handling
- [ ] `NEEDS VERIFICATION`
- [ ] Existing publication is supportable; no correction required
- [ ] Security-sensitive; move details to private handling
- [ ] Rights, sensitivity, sovereignty, or consent review required
- [ ] Immediate containment or release hold required
- [ ] `CorrectionNotice` required
- [ ] Supersession or withdrawal required
- [ ] Rollback review required
- [ ] Drift or verification-register entry required
- [ ] Architecture/governance decision required before implementation
- [ ] Implementation authorized through a separate current instruction
- [ ] No repository mutation authorized

### Required follow-up

- [ ] Affected object, release, owner, and responsibility root are identified.
- [ ] Current baseline, target bytes, open branches, pull requests, and direct dependencies were inspected.
- [ ] Evidence, source role, and truth labels are recorded per material claim.
- [ ] Stale-versus-wrong classification and finite correction outcome are recorded.
- [ ] Derivative impact, public exposure, and correction propagation are reviewed.
- [ ] Required correction, release, policy, review, proof, and rollback artifacts are linked.
- [ ] Sensitive or restricted handling uses the proper private path.
- [ ] Public-safe notice or no-notice decision is recorded.
- [ ] Regression protection and rollback evidence are present.
- [ ] Closure links to the governed correction outcome, implementing PR, or explicit no-action rationale.

### Final issue disposition

- [ ] `CORRECTED`
- [ ] `SUPERSEDED`
- [ ] `WITHDRAWN`
- [ ] `ROLLED_BACK`
- [ ] `MARKED_STALE`
- [ ] `NO_ACTION`
- [ ] `DUPLICATE`
- [ ] `BLOCKED`
- [ ] `PARTIAL`
- [ ] `ERROR`
- [ ] `UNKNOWN`

**Governed outcome links and rationale:**

-

## Submitter acknowledgements

- [ ] I understand this issue is a correction request, not a `CorrectionNotice`, release decision, implementation authorization, or rollback approval.
- [ ] I have not asked maintainers to silently overwrite or delete published history.
- [ ] I have used public-safe evidence pointers and generalized restricted details.
- [ ] I have marked inferences and unknowns instead of presenting them as confirmed facts.
- [ ] I understand issue closure is administrative state and does not prove correction completion.
- [ ] I understand a passing test, generated receipt, pull request, merge, GitHub release, or public wording change does not by itself prove governed correction or publication closure.

---

<sub>Correction is a governed, append-only, reviewable, and reversible state transition. Issue intake does not replace evidence, policy, review, release, correction, supersession, withdrawal, rollback, or public read-back evidence.</sub>

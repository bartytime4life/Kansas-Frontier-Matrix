<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook-hazards-promotion
title: Hazards Promotion Runbook
type: operational-runbook
version: v2.0.0
status: DRAFT_REPOSITORY_GROUNDED; PROMOTION_EXECUTION_HELD; BOUNDED_NO_NETWORK_VALIDATION; NON_RELEASE; NON_PUBLICATION
owner: NEEDS VERIFICATION — Hazards domain steward plus accountable release authority
created: 2026-05-12
updated: 2026-08-27
policy_label: repository-facing; hazards; promotion-preflight; fail-closed; not-for-life-safety; non-publisher
owning_root: docs/
path_authority: docs/runbooks/ under accepted ADR-0029 and Directory Rules v2
authority_effect: none
release_effect: none
deployment_effect: none
promotion_effect: none
publication_effect: none
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 0d236241a58b56291797c32a79ee3c04a9ab2ec0
  target_path: docs/runbooks/hazards/PROMOTION_RUNBOOK.md
  target_prior_blob: 37832ce0bd445d70b6ecbbf223e0baa89e880896
  open_pull_requests_touching_target: 0
  current_candidate_lane: release/candidates/hazards/ contains README.md only
related:
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../doctrine/directory-rules.md
  - ../README.md
  - ../../domains/hazards/README.md
  - NOT_FOR_LIFE_SAFETY_AUDIT_RUNBOOK.md
  - ROLLBACK_RUNBOOK.md
  - ../../../release/README.md
  - ../../../release/candidates/hazards/README.md
  - ../../../policy/domains/hazards/README.md
  - ../../../tools/validators/promotion_gate/README.md
  - ../../../.github/workflows/domain-hazards.yml
notes:
  - This runbook prepares and evaluates a candidate; it never authorizes or executes promotion.
  - Current repository evidence supports bounded no-network fixtures and readiness validation, not an operational Hazards release.
  - Existing Hazards manifest files inspected in release/manifests/ are PROPOSED documentation-inventory placeholders, not release evidence.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hazards Promotion Runbook

> **One-line purpose.** Prepare, validate, and hand off a Hazards release candidate through a fail-closed promotion preflight without creating review, release, promotion, deployment, publication, or life-safety authority.

[![Status: promotion held](https://img.shields.io/badge/status-promotion%20held-b42318?style=flat-square)](#current-disposition)
[![Validation: bounded no-network](https://img.shields.io/badge/validation-bounded%20no--network-8250df?style=flat-square)](#repository-native-validation)
[![Life safety: no](https://img.shields.io/badge/life%20safety-not%20an%20alerting%20system-b42318?style=flat-square)](#not-for-life-safety-boundary)
[![Release effect: none](https://img.shields.io/badge/release%20effect-none-6e7781?style=flat-square)](#authority-and-terminal-boundary)

> [!CAUTION]
> **KFM Hazards is not an emergency-alerting system, emergency-operations system, or regulatory authority.** Do not use KFM to issue, replace, delay, retract, or interpret current life-safety instructions. Public-facing Hazards material must remain planning, research, historical, modeled, regulatory-context, or explanatory content and must direct urgent needs to the appropriate official source.

> [!IMPORTANT]
> **Current disposition: `HOLD`.** At the pinned repository snapshot, the Hazards candidate lane contains no candidate packet, Hazards policy remains default-deny and runtime enforcement is unverified, the domain workflow intentionally blocks proof and release jobs, and no operational promotion executor or authenticated release authority has been demonstrated. A green bounded validator result may support review; it does not change lifecycle or release state.

## Quick navigation

- [1. Goal and scope](#1-goal-and-scope)
- [2. Authority and terminal boundary](#2-authority-and-terminal-boundary)
- [3. Current disposition](#3-current-disposition)
- [4. Promotion vocabulary](#4-promotion-vocabulary)
- [5. Preconditions](#5-preconditions)
- [6. Gate matrix](#6-gate-matrix)
- [7. Roles and separation of duties](#7-roles-and-separation-of-duties)
- [8. Procedure](#8-procedure)
- [9. Repository-native validation](#9-repository-native-validation)
- [10. Mandatory stop conditions](#10-mandatory-stop-conditions)
- [11. Candidate handoff packet](#11-candidate-handoff-packet)
- [12. Decision record worksheet](#12-decision-record-worksheet)
- [13. Release handoff](#13-release-handoff)
- [14. Correction and rollback](#14-correction-and-rollback)
- [15. Acceptance and negative cases](#15-acceptance-and-negative-cases)
- [16. Related repository surfaces](#16-related-repository-surfaces)
- [17. Open verification backlog](#17-open-verification-backlog)
- [18. Runbook maintenance and rollback](#18-runbook-maintenance-and-rollback)

---

## 1. Goal and scope

This runbook governs the **preflight and handoff** for a proposed transition of one Hazards candidate from `CATALOG` or `TRIPLET` toward `PUBLISHED`.

It preserves the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed state transition. It is not inferred from:

- a file move or copy;
- a branch, commit, pull request, merge, tag, GitHub release, or badge;
- a passing test, workflow, validator, schema, receipt, proof, or signature by itself;
- a manifest-shaped file;
- a map layer becoming visible;
- an API response, dashboard, screenshot, export, summary, or AI answer; or
- a document that says a release is ready.

### In scope

- freezing the exact candidate and evaluation baseline;
- verifying declared identity, artifacts, source roles, time, rights, sensitivity, evidence, catalog, policy, review, correction, and rollback closure;
- running repository-owned, no-network validation;
- recording finite results and unresolved blockers;
- assembling a reviewable handoff packet when every applicable precondition is supported; and
- preserving a no-change outcome when support is insufficient or unsafe.

### Out of scope

- admitting or activating a live source;
- fetching production data;
- changing RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED state;
- authenticating a reviewer or assigning release authority;
- evaluating a production policy bundle;
- signing, releasing, deploying, promoting, publishing, changing aliases, invalidating production caches, or modifying public routes;
- changing repository settings, secrets, environments, permissions, or branch protection; and
- issuing or interpreting emergency guidance.

[Back to top](#top)

---

<a id="authority-and-terminal-boundary"></a>

## 2. Authority and terminal boundary

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) and [Directory Rules v2](../../doctrine/directory-rules.md) place operational procedures under `docs/runbooks/` and release decisions under `release/`. This file therefore explains procedure; it is not a release, policy, evidence, proof, review, receipt, or publication object.

| Responsibility | Canonical surface | This runbook may do | This runbook must not do |
|---|---|---|---|
| Operational procedure | `docs/runbooks/hazards/` | Explain preflight and handoff | Create release authority |
| Domain meaning | `contracts/domains/hazards/` | Link and consume | Redefine contracts |
| Machine shape | `schemas/contracts/v1/domains/hazards/` and release schemas | Require validation | Treat shape validity as truth or approval |
| Policy source | `policy/` | Require an accepted policy result | Invent or activate policy |
| Evidence, proof, receipt, catalog | `data/` trust-artifact lanes | Resolve and inspect references | Collapse the families or manufacture support |
| Release decisions | `release/` | Prepare a bounded handoff | Write or infer a decision |
| Public-safe carriers | `data/published/` | Verify declared target references | Publish or mutate a carrier |

The highest result this runbook can establish is:

```text
READY_FOR_ACCOUNTABLE_RELEASE_REVIEW
```

That result means the preflight packet is reviewable. It does **not** mean `APPROVED`, `PROMOTED`, `RELEASED`, `DEPLOYED`, or `PUBLISHED`.

[Back to top](#top)

---

<a id="current-disposition"></a>

## 3. Current disposition

The following assessment is pinned to `main@0d236241a58b56291797c32a79ee3c04a9ab2ec0`.

| Surface | Current evidence | Truth / maturity | Safe conclusion |
|---|---|---|---|
| Runbook path | Existing file under `docs/runbooks/hazards/` | **CONFIRMED** | Same-path replacement is valid; no new path is needed. |
| Hazards candidate lane | `release/candidates/hazards/` contains its README only | **CONFIRMED / ABSENT candidate** | No real candidate can be promoted. |
| Hazards manifests | Small `hazards-r000*` files under `release/manifests/` declare `status: PROPOSED` and describe themselves as documentation-inventory placeholders | **CONFIRMED placeholders** | They are not evidence of a candidate, review, release, or publication. |
| Domain validation | `make hazards-validate` runs the deterministic USDM materiality fixture suite with `KFM_NO_NETWORK=1` | **CONFIRMED / BOUNDED** | Useful changed-area proof; not full Hazards or release closure. |
| Hazards workflow | `validate-offline` runs bounded tests; `proof-gate` and `release-gate` exit nonzero intentionally | **CONFIRMED / FAIL-CLOSED** | Hosted orchestration deliberately withholds proof and release readiness. |
| Hazards policy | Domain policy files exist and default deny; the README says runtime enforcement is unverified | **CONFIRMED defaults / PARTIAL** | Do not infer an active policy evaluator or operational policy decision. |
| Promotion validator | A no-network A-G readiness validator, fixtures, tests, and `make publish-check` exist | **CONFIRMED / BOUNDED** | `PASS` means `APPROVE_READY` for accountable review only. |
| Publication-denial dry run | `make release-dry-run` applies five synthetic negative mutations and writes nothing | **CONFIRMED / BOUNDED** | Proves denial polarity only; assembles no candidate and creates no authority. |
| Review authority | Repository routing exists; independent accountable Hazards release stewardship and authenticated assignments were not demonstrated | **NEEDS VERIFICATION** | Missing authority or separation requires `HOLD`. |
| Operational promotion | No verified live candidate assembler, accepted evaluator-to-decision path, alias mutation, deployment, or publication flow was demonstrated | **UNKNOWN / HOLD** | Do not execute promotion. |
| Public/runtime parity | No production endpoint, deployment, dashboard, runtime log, or public recovery exercise was inspected for this runbook | **UNKNOWN** | Do not claim operational readiness. |

### Current finite result

```text
work_state: HOLD
reason_codes:
  - HAZ_PROMOTION_CANDIDATE_ABSENT
  - HAZ_POLICY_RUNTIME_UNVERIFIED
  - HAZ_RELEASE_AUTHORITY_UNVERIFIED
  - HAZ_OPERATIONAL_PROMOTION_UNVERIFIED
release_effect: none
publication_effect: none
```

[Back to top](#top)

---

## 4. Promotion vocabulary

Keep validation, work state, review, release, and publication separate.

| Term | Meaning here | Effect |
|---|---|---|
| `PASS` | The invoked bounded validator found no condition in its declared profile | No lifecycle or release change |
| `ABSTAIN` | Evidence or authority is insufficient without a proven unsafe contradiction | Candidate remains unchanged; narrow or resolve support |
| `DENY` | A mandatory, unsafe, prohibited, or contradictory condition blocks readiness | Candidate remains unchanged; do not route around the denial |
| `ERROR` | The evaluation could not complete safely | Candidate remains unchanged; repair the evaluator or input |
| `HOLD` | Governance/work-state block such as absent candidate, unresolved rights, missing review authority, or pending overlap | Candidate remains unchanged; no release handoff |
| `READY_FOR_ACCOUNTABLE_RELEASE_REVIEW` | Every applicable preflight item is supported and the packet can be reviewed by the proper authority | Still not approval or publication |
| `PUBLISHED` | A separate governed transition has completed and a public-safe carrier is released through the proper path | Outside this runbook |

Never convert `SKIPPED`, `NOT_RUN`, `PENDING`, `NO_RUN_FOUND`, or an intentionally blocked workflow job into `PASS`.

[Back to top](#top)

---

## 5. Preconditions

A candidate is eligible for preflight only when every applicable item below is traceable to an immutable or versioned object. Missing support produces `HOLD`, `ABSTAIN`, `DENY`, or `ERROR`; it never produces a partial promotion.

| # | Required condition | Minimum evidence | Failure posture |
|---:|---|---|---|
| 1 | Exact candidate identity | Candidate ID, exact repository ref, artifact inventory, deterministic digests | `HOLD` or `DENY` |
| 2 | Correct lifecycle boundary | Declared `CATALOG` or `TRIPLET` to `PUBLISHED`; no earlier-stage material in the public packet | `DENY` |
| 3 | Canonical source descriptors | Source identity, authority role, rights, access, sensitivity, citation, cadence, and version | `ABSTAIN`, `HOLD`, or `DENY` |
| 4 | Source-role anti-collapse | Observation, regulatory, modeled, aggregate, administrative, candidate, and synthetic roles remain explicit where applicable | `DENY` |
| 5 | Temporal semantics | Observed, valid, source, retrieval, publication, effective, correction, and transaction times remain distinct where material | `DENY` or `ABSTAIN` |
| 6 | Contract and schema fit | Accepted or currently applicable contract/schema references plus successful validation | `ERROR` or `DENY` |
| 7 | Geometry and CRS integrity | Valid, deterministic, correctly bounded public geometry and declared CRS | `DENY` |
| 8 | Rights and sensitivity clearance | Public-use basis and every required minimization, redaction, generalization, delay, or access obligation | `HOLD` or `DENY` |
| 9 | Evidence closure | Every consequential `EvidenceRef` resolves to an admissible `EvidenceBundle` for the candidate scope | `ABSTAIN` or `DENY` |
| 10 | Receipt/proof/catalog separation | Receipts record execution; proofs support closure; catalog entries describe; none substitutes for another | `DENY` |
| 11 | Policy result | Result from an accepted, identified policy profile with bundle/version reference and finite outcome | `HOLD`, `DENY`, or `ERROR` |
| 12 | Review authority | Authenticated reviewer identities, current assignments, subject/scope binding, and required separation | `HOLD` or `ABSTAIN` |
| 13 | Release manifest draft | Candidate-bound manifest with artifact-set agreement and no claim of release | `DENY` |
| 14 | Correction path | Candidate-bound correction lineage and outward notice plan | `ABSTAIN` or `DENY` |
| 15 | Rollback target | Prior safe target or explicit initial-bind posture, rollback card draft, invalidation scope, and recovery verification plan | `ABSTAIN` or `DENY` |
| 16 | Public-path conformance | Governed API or released public-safe carrier only; no RAW, WORK, QUARANTINE, internal-store, or direct-model path | `DENY` |
| 17 | Not-for-life-safety disclosure | Visible planning/context boundary plus referral to official sources on every affected public surface | `DENY` |
| 18 | Accessibility and degraded behavior | Keyboard, screen-reader, mobile, low-bandwidth, stale, denied, and unavailable states are bounded where the public UI changes | `HOLD` or `DENY` |
| 19 | Overlap and ownership | No active branch, pull request, migration, or steward work owns the same candidate or authority surface | `HOLD` |
| 20 | Reproducible validation | Required checks run at the exact candidate ref; outcomes and limitations are recorded | `HOLD` or `ERROR` |

[Back to top](#top)

---

## 6. Gate matrix

The repository's bounded promotion validator defines gates A-G. This runbook uses those names for preflight alignment but does not expand the validator's authority.

| Gate | Bounded concern | Candidate-specific evidence required beyond a fixture pass | Current Hazards posture |
|:---:|---|---|---|
| A | Identity and closure | Real candidate identity, lifecycle boundary, manifest identity, exact spec hash | `HOLD` — no candidate |
| B | Asset integrity | Candidate/manifest/receipt digest equality over the actual artifact set | `HOLD` — no candidate packet |
| C | Geometry and CRS | Real geometry validation, deterministic transformation evidence, public-safe precision | `NEEDS VERIFICATION` |
| D | Temporal semantics | Real intervals and role-specific time fields for the candidate | `NEEDS VERIFICATION` |
| E | Rights and sensitivity policy context | Accepted evaluator result, current policy bundle reference, rights/sensitivity evidence | `HOLD` — runtime evaluator unverified |
| F | Proof and catalog support | Resolved EvidenceBundles, attestations, STAC/DCAT/PROV or applicable catalog closure, conditional AI receipt | `NEEDS VERIFICATION` |
| G | Review, correction, and rollback | Authenticated ReviewRecord/authority, separation, correction lineage, rollback target | `HOLD` — authority unverified |

> [!NOTE]
> `make publish-check` proves the synthetic A-G fixture profile and finite outcomes. It does not dereference candidate references, authenticate actors, evaluate live Rego, verify signatures, prove rights, inspect a public surface, or create a release decision.

[Back to top](#top)

---

## 7. Roles and separation of duties

Role names below describe required responsibilities, not verified assignments.

| Role | Required responsibility | Current assignment status |
|---|---|---|
| Candidate author | Assemble the candidate and evidence without approving it | `UNKNOWN` until a candidate exists |
| Hazards domain steward | Confirm object meaning, source roles, domain invariants, and candidate scope | `NEEDS VERIFICATION` |
| Source/rights steward | Confirm source admission, rights, terms, citation, and permitted public use | `NEEDS VERIFICATION` |
| Sensitivity reviewer | Confirm precision, redaction, generalization, delay, and access obligations | `NEEDS VERIFICATION` when applicable |
| Evidence steward | Confirm `EvidenceRef` to `EvidenceBundle` resolution and bounded support | `NEEDS VERIFICATION` |
| Policy steward | Identify the accepted policy profile and evaluator result | `NEEDS VERIFICATION` |
| Accountable release authority | Review the packet and issue any separate release decision | `NEEDS VERIFICATION` |
| Correction/rollback reviewer | Confirm correction notice, rollback target, invalidation, and recovery path | `NEEDS VERIFICATION` |
| Public-surface reviewer | Confirm governed-path, not-for-life-safety, accessibility, stale, denied, and error states | `NEEDS VERIFICATION` when a public surface changes |

For policy-significant, life-safety-adjacent, rights-sensitive, precision-sensitive, first-source, or first-public-surface changes, do not let the candidate author self-approve. If the required independent authority cannot be authenticated, return `HOLD`.

[Back to top](#top)

---

## 8. Procedure

### Step 0 — Stop at the emergency boundary

Before touching a candidate, confirm that the request is not asking KFM to issue, replace, modify, or suppress current emergency guidance. If it is, do not run this procedure. Preserve KFM state and direct the operator to the official authority.

Record:

- affected surface;
- whether current official guidance could be confused with KFM content;
- official referral destination class, without embedding secrets or unstable private links; and
- `HAZ_NOT_LIFE_SAFETY_BOUNDARY_CONFIRMED` or the reason for `DENY`.

### Step 1 — Freeze the candidate and authority baseline

Pin all of the following before evaluation:

- repository and exact commit;
- candidate ID and declared lifecycle transition;
- complete artifact path and digest inventory;
- contract, schema, validator, policy, and release-profile versions;
- source descriptor IDs and dataset versions;
- evidence, receipt, proof, catalog, review, correction, and rollback references;
- public surfaces and downstream consumers;
- active pull requests, branches, migrations, and owners; and
- baseline failures that predate candidate work.

Do not continue when the candidate is mutable, incompletely inventoried, or semantically owned by active overlapping work.

### Step 2 — Verify source, role, rights, sensitivity, and time

For each source and derived artifact:

1. confirm the source descriptor and authority role;
2. confirm rights and terms for the proposed public use;
3. classify sensitivity and harmful precision;
4. preserve observation, regulatory, model, aggregate, administrative, candidate, and synthetic distinctions;
5. verify material time fields and freshness/expiry posture; and
6. record every transform, minimization, generalization, or delay obligation.

A current warning, watch, advisory, forecast, detection, model, declaration, regulatory map, or aggregate must never silently become an observed event or KFM life-safety instruction.

### Step 3 — Run bounded Hazards validation

Run the repository-native no-network checks in [Section 9](#9-repository-native-validation) at the exact candidate ref. Record each result as `PASS`, `FAIL`, `ERROR`, `SKIPPED`, `NOT_RUN`, `PENDING`, `CANCELLED`, `TIMED_OUT`, or `NO_RUN_FOUND`.

A failure outside the candidate scope may be classified as inherited only when exact base/head evidence supports that classification. Do not weaken a validator, baseline, ratchet, or policy to obtain a green result.

### Step 4 — Run bounded promotion and publication-denial proof

Run:

```bash
make publish-check
make release-dry-run
```

Interpretation:

- `make publish-check` validates synthetic ReviewRecord and A-G promotion-gate fixtures;
- `make release-dry-run` validates five synthetic publication-denial paths;
- neither command assembles or evaluates a real Hazards candidate;
- neither command writes a decision, receipt, proof, release, or public artifact; and
- `PASS` remains bounded evidence only.

When an explicit candidate packet exists and is authorized for evaluation, run the bounded validator directly:

```bash
python tools/validators/validate_promotion_gate.py path/to/candidate.json
```

The path above is operator-supplied. Do not create a new canonical candidate home from this example.

### Step 5 — Resolve real evidence and catalog support

For every consequential claim and public-facing feature:

1. resolve `EvidenceRef` to `EvidenceBundle`;
2. verify scope, source role, spatial extent, temporal extent, limitations, and digest;
3. confirm the evidence is admissible for the exact claim;
4. confirm catalog and provenance projections point to the same released object identity; and
5. return `ABSTAIN` when support is insufficient.

Search results, map pixels, tiles, graph edges, vector indexes, screenshots, summaries, and model output are not substitutes for evidence resolution.

### Step 6 — Obtain an actual policy result

The candidate requires an identified, accepted policy profile and an evaluator result bound to the candidate, policy bundle/version, evaluation time, labels, reasons, and obligations.

At the pinned snapshot, Hazards policy runtime enforcement is unverified. Therefore a real promotion remains `HOLD` until repository evidence demonstrates the accepted evaluator path. A default-deny Rego file or successful parse is not an operational policy decision.

### Step 7 — Complete accountable review

Confirm:

- reviewer identity and current authority;
- reviewer independence where required;
- candidate, scope, artifact-set, and spec-hash binding;
- review time within the authority interval;
- no unresolved obligations in an approving review;
- correction and rollback review; and
- explicit acknowledgement of the not-for-life-safety boundary.

Missing or unauthenticated review authority produces `HOLD` or `ABSTAIN`, not approval.

### Step 8 — Close correction and rollback before release review

Before handoff, require:

- a candidate-bound correction path;
- a rollback target or explicit initial-bind posture;
- rollback scope and invalidation list;
- cache, catalog, graph, search, tile, API, UI, export, and AI consequences where applicable;
- expected recovery verification; and
- the outward notice posture.

Do not use a generic rollback document as proof that the candidate is reversible.

### Step 9 — Audit the public boundary

Run the [Not-for-Life-Safety Audit Runbook](NOT_FOR_LIFE_SAFETY_AUDIT_RUNBOOK.md) over every affected public surface. Verify:

- the content is planning/contextual and never authoritative emergency guidance;
- stale, denied, withheld, unavailable, and corrected states are visible;
- official-source referrals are present where needed;
- no public path reaches RAW, WORK, QUARANTINE, an internal store, or a direct model runtime;
- evidence, time, policy, review, release, and correction state remain inspectable; and
- sensitive or harmful precision is transformed before rendering, not merely hidden by styling.

### Step 10 — Reconcile the final preflight result

Use the most restrictive supported result:

```text
ERROR > DENY > ABSTAIN > HOLD > READY_FOR_ACCOUNTABLE_RELEASE_REVIEW
```

`HOLD` is a work-state label rather than a promotion-validator status. It remains mandatory when governance, ownership, authority, overlap, or operational closure is unresolved even if bounded validators return `PASS`.

### Step 11 — Hand off; do not promote

When every precondition is supported, assemble the packet in [Section 11](#11-candidate-handoff-packet) and hand it to the accountable release authority. This runbook stops there.

No operator may infer authority to:

- write a `PromotionDecision`;
- mutate a live alias;
- move a carrier into public service;
- deploy;
- publish; or
- mark the lifecycle `PUBLISHED`.

Those are separate governed transitions.

[Back to top](#top)

---

<a id="repository-native-validation"></a>

## 9. Repository-native validation

Run from the repository root at the exact candidate ref.

### 9.1 Hazards bounded validation

```bash
export KFM_NO_NETWORK=1
export PYTHONHASHSEED=0
export PYTHONDONTWRITEBYTECODE=1
export PYTHONUNBUFFERED=1
export TZ=UTC

make hazards-validate
python -m unittest -q tests.domains.hazards.test_fixture_provenance
python -m unittest -q tests.domains.hazards.test_source_hash_validation
python -m unittest -q tests.domains.hazards.test_source_descriptor_validation
python -m unittest -q tests.domains.hazards.test_usdm_materiality
```

These commands mirror the implemented offline Hazards workflow. They prove only their bounded fixtures and assertions.

### 9.2 Promotion-readiness fixture proof

```bash
make publish-check
```

Expected finite statuses are `PASS`, `ABSTAIN`, `DENY`, and `ERROR`. A `PASS` establishes only bounded `APPROVE_READY` shape/readiness for accountable review.

### 9.3 Synthetic publication-denial proof

```bash
make release-dry-run
```

The current tool exercises missing evidence, policy denial, artifact-integrity mismatch, non-public-safe rights/sensitivity posture, and missing review. It must report:

- no network use;
- no candidate assembly;
- no decision creation;
- no release creation; and
- no publication creation.

### 9.4 Optional documentation and repository checks

Use repository-native changed-area or documentation checks selected by the current CI configuration. Record hosted checks separately from local commands. Do not call an absent check `PASS`.

### 9.5 Result record

For each command or hosted check, record:

| Field | Required value |
|---|---|
| Check name | Exact command or hosted job |
| Evaluated ref | Exact full commit SHA or merge ref |
| Outcome | `PASS`, `FAIL`, `ERROR`, `SKIPPED`, `NOT_RUN`, `PENDING`, `CANCELLED`, `TIMED_OUT`, or `NO_RUN_FOUND` |
| Scope | What the check actually covers |
| Classification | Candidate-introduced, inherited, intentional hold/skip, or unresolved |
| Evidence | Stable log/run/receipt reference where available |
| Limitation | What the result cannot prove |

[Back to top](#top)

---

## 10. Mandatory stop conditions

### Return `HOLD` when

- the candidate lane has no immutable candidate packet;
- required ownership, reviewer authority, separation, or CODEOWNERS/ruleset enforcement is unresolved;
- an active pull request, branch, migration, or steward owns the same bytes or semantic authority;
- rights, terms, sensitivity, sovereignty, consent, or precision posture needs review;
- evidence, catalog, correction, or rollback references have not been resolved;
- policy runtime/evaluator binding is not demonstrated;
- required checks are pending, skipped, not run, or unavailable;
- a public-surface audit is incomplete; or
- operational release, alias, deployment, cache invalidation, or recovery behavior is unverified.

### Return `ABSTAIN` when

- evidence does not support the proposed consequential claim;
- source authority is insufficient for the asserted role;
- review authority or correction lineage is missing but no unsafe contradiction is asserted; or
- temporal or spatial scope cannot be narrowed safely.

### Return `DENY` when

- the candidate presents KFM as an emergency or life-safety authority;
- policy returns `DENY`;
- source rights prohibit the proposed use;
- sensitive or harmful precision would be exposed without authorization;
- a model, forecast, aggregate, regulatory record, detection, or context layer is relabeled as observation or ground truth;
- a public client would access RAW, WORK, QUARANTINE, an internal store, or a direct model runtime;
- artifact, identity, geometry, CRS, time, manifest, receipt, proof, review, correction, or rollback declarations contradict each other;
- the candidate bypasses a required governed interface or release decision; or
- a validator, ratchet, baseline, policy, or security default would need to be weakened to proceed.

### Return `ERROR` when

- input cannot be parsed safely;
- a validator or evaluator crashes or times out;
- duplicate or noncanonical fields prevent deterministic interpretation;
- the repository ref or artifact digest cannot be resolved; or
- the evaluation environment violates the no-network or no-write boundary.

Every stop preserves the previous lifecycle and public state.

[Back to top](#top)

---

## 11. Candidate handoff packet

A handoff packet must be dependency-closed and candidate-specific. At minimum, include:

| Packet field | Required content |
|---|---|
| Candidate identity | Candidate ID, author, exact repository ref, lifecycle from/to |
| Artifact inventory | Paths, media types, sizes where material, immutable digests |
| Contract/schema profile | Applicable versions and validation results |
| Source inventory | SourceDescriptor and DatasetVersion references, authority roles, rights, sensitivity, citations |
| Spatial/temporal scope | CRS, bbox/coverage, precision transform, valid/observed/source/retrieval/effective times |
| Evidence closure | EvidenceRefs, resolved EvidenceBundles, limitations, abstentions |
| Process memory | RunReceipt references and reproducibility inputs |
| Proof/catalog closure | Proof, attestation, catalog, provenance, and identity bindings |
| Policy | Accepted profile, bundle/version, finite outcome, reasons, obligations |
| Review | Authenticated reviewers, authority assignments, separation, scope/hash binding |
| Public surfaces | Governed APIs, layers, drawers, exports, dashboards, AI surfaces, stale/error states |
| Hazards boundary | Exact not-for-life-safety wording and official referral posture |
| Release draft | Candidate-bound ReleaseManifest draft; no release claim |
| Correction | Correction lineage and outward notice plan |
| Rollback | Rollback target/card draft, invalidation scope, recovery verification |
| Validation | Exact commands/jobs, refs, outcomes, classifications, limitations |
| Open limitations | Every unresolved item and why it does or does not block handoff |
| Requested decision | `HOLD`, `ABSTAIN`, `DENY`, `ERROR`, or `READY_FOR_ACCOUNTABLE_RELEASE_REVIEW` |

Do not include private connector URLs, credentials, temporary workspace paths, restricted source content, or large copyrighted excerpts.

[Back to top](#top)

---

## 12. Decision record worksheet

This worksheet is operator memory, not a schema or release decision.

| Field | Value |
|---|---|
| Candidate ID | `<required>` |
| Exact candidate commit | `<full SHA>` |
| Evaluation time | `<UTC-second timestamp>` |
| Lifecycle request | `CATALOG|TRIPLET -> PUBLISHED` |
| Hazards boundary audit | `PASS / FAIL / NOT_RUN` |
| Domain validation | `PASS / FAIL / ERROR / NOT_RUN` |
| Promotion fixture proof | `PASS / FAIL / ERROR / NOT_RUN` |
| Candidate-specific A-G result | `PASS / ABSTAIN / DENY / ERROR / NOT_RUN` |
| Policy result | `PASS / ABSTAIN / DENY / ERROR / NOT_RUN` |
| Review authority | `CONFIRMED / NEEDS VERIFICATION / UNKNOWN` |
| Correction closure | `CONFIRMED / NEEDS VERIFICATION / UNKNOWN` |
| Rollback closure | `CONFIRMED / NEEDS VERIFICATION / UNKNOWN` |
| Hosted checks | `<per-check finite outcomes>` |
| Work-state result | `HOLD / READY_FOR_ACCOUNTABLE_RELEASE_REVIEW` |
| Reason codes | `<stable, non-sensitive list>` |
| Release effect | `none` |
| Publication effect | `none` |

If a canonical decision is later authorized, write it through the accepted release contract, schema, policy, reviewer, and append-only release path. Do not promote this worksheet into authority by copying it into `release/`.

[Back to top](#top)

---

## 13. Release handoff

A successful preflight produces a review packet and a bounded recommendation. It does not produce a release.

### Valid handoff result

```text
READY_FOR_ACCOUNTABLE_RELEASE_REVIEW
```

Required handoff statement:

> The candidate passed the bounded checks listed in this packet and has no unresolved preflight blocker identified within the inspected scope. This is a recommendation for accountable release review only. It does not authenticate reviewers, issue a PromotionDecision, mutate release state, deploy, promote, or publish.

### Current repository limitation

At `main@0d236241a58b56291797c32a79ee3c04a9ab2ec0`, real Hazards promotion remains `HOLD` because no candidate packet exists and operational policy/release authority has not been demonstrated. Do not manufacture a handoff merely to exercise the procedure.

[Back to top](#top)

---

## 14. Correction and rollback

### Preflight failure

Before publication, a failed preflight requires no data rollback because no lifecycle or public state changed. Preserve the candidate evidence, record the finite result, and either:

- correct the candidate on a reviewable branch;
- narrow the scope;
- return it to the owning lifecycle stage;
- quarantine unsafe or unresolved material; or
- close the candidate without release effect.

### After a separately authorized release

Use the [Hazards Rollback Runbook](ROLLBACK_RUNBOOK.md) and canonical release objects. The sibling runbook is itself documentation; verify its paths and operational assumptions against current repository evidence before use.

Keep object families separate:

- release/correction decision: `release/correction_notices/`;
- release/withdrawal decision: `release/withdrawal_notices/`;
- rollback decision: `release/rollback_cards/`;
- promotion decision: `release/promotion_decisions/`;
- release manifest: `release/manifests/`;
- process receipts, proofs, catalog records, published carriers, and rollback data events: their respective `data/` lanes.

A rollback card does not execute rollback. A correction notice does not update a carrier. A signature does not prove evidence truth. Runtime rollback, cache invalidation, alias mutation, and public parity remain separate operational evidence.

[Back to top](#top)

---

## 15. Acceptance and negative cases

### Documentation acceptance criteria

This runbook is acceptable when it:

- states the current real-candidate disposition as `HOLD`;
- preserves the not-for-life-safety boundary at the top and in the procedure;
- distinguishes bounded validation from release authority;
- names current repository commands accurately;
- does not present placeholder Hazards manifests as releases;
- does not claim active Hazards policy enforcement;
- stops at accountable review handoff;
- keeps release, correction, withdrawal, rollback, receipts, proofs, catalogs, and public carriers separate; and
- provides a reversible documentation-only rollback.

### Required negative cases for any future candidate implementation

| Negative case | Required result |
|---|---|
| No candidate packet | `HOLD` |
| Missing EvidenceRef support | `ABSTAIN` / blocked |
| Policy `DENY` | `DENY` / blocked |
| Policy evaluator error | `ERROR` / blocked |
| Artifact-set mismatch | `DENY` / blocked |
| Invalid geometry or CRS | `DENY` / blocked |
| Inverted or malformed time | `DENY` / blocked |
| Unclear rights or non-public-safe sensitivity | `HOLD` or `DENY` / blocked |
| Missing or unauthenticated review authority | `HOLD` or `ABSTAIN` / blocked |
| Self-review where separation is required | `DENY` / blocked |
| Missing correction lineage | `ABSTAIN` / blocked |
| Missing rollback target | `ABSTAIN` or `DENY` / blocked |
| Current alert presented as KFM authority | `DENY` / blocked |
| Direct public RAW/internal/model path | `DENY` / blocked |
| Required check skipped or pending | `HOLD`; never `PASS` |
| Attempted network or write in a no-network validator | `ERROR` / blocked |

[Back to top](#top)

---

## 16. Related repository surfaces

| Surface | Current role | Use with this runbook |
|---|---|---|
| [Directory Rules v2](../../doctrine/directory-rules.md) | Accepted placement and responsibility authority | Determines runbook and release-object homes |
| [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Accepted adoption decision | Confirms Directory Rules authority |
| [Runbooks README](../README.md) | Runbook boundary and non-emergency posture | Defines instruction-versus-authority separation |
| [Hazards domain README](../../domains/hazards/README.md) | Domain scope and current maturity | Supplies domain boundary, not release authority |
| [Not-for-Life-Safety Audit Runbook](NOT_FOR_LIFE_SAFETY_AUDIT_RUNBOOK.md) | Repository-grounded public-boundary audit | Required before public-surface handoff |
| [Hazards Rollback Runbook](ROLLBACK_RUNBOOK.md) | Draft rollback procedure | Verify current assumptions before operational use |
| [Hazards contracts README](../../../contracts/domains/hazards/README.md) | Hazards semantic contract index | Confirm applicable object meaning |
| [Hazards schemas README](../../../schemas/contracts/v1/domains/hazards/README.md) | Hazards schema-lane index | Confirm actual concrete schema coverage |
| [Hazards policy README](../../../policy/domains/hazards/README.md) | Default-deny policy-lane status | Do not infer active enforcement |
| [Hazards workflow](../../../.github/workflows/domain-hazards.yml) | Offline validation plus intentional proof/release holds | Hosted orchestration evidence |
| [Promotion-gate validator README](../../../tools/validators/promotion_gate/README.md) | Bounded no-network A-G readiness profile | Interpret `PASS` narrowly |
| [Release root README](../../../release/README.md) | Canonical append-only release-decision root | Defines release object separation and holds |
| [Hazards candidate README](../../../release/candidates/hazards/README.md) | Candidate-lane contract | Current lane has no candidate packet |
| [Hazards release index](../../domains/hazards/RELEASE_INDEX.md) | Docs-side navigation draft | Does not override canonical release objects |
| [Makefile](../../../Makefile) | Repository command surface | Source of current validation commands |

[Back to top](#top)

---

## 17. Open verification backlog

A real Hazards promotion remains blocked until current evidence resolves, at minimum:

- [ ] One immutable, candidate-specific packet exists under the accepted candidate contract and home.
- [ ] Applicable Hazards contracts and concrete schemas are identified and accepted for the candidate.
- [ ] Every source descriptor, right, term, sensitivity label, and precision transform is verified for public use.
- [ ] Candidate-specific geometry, CRS, temporal-role, source-role, evidence, catalog, and artifact-integrity checks pass.
- [ ] `EvidenceRef` to `EvidenceBundle` resolution is demonstrated for every consequential public claim.
- [ ] The accepted Hazards policy bundle, evaluator, version, result, reasons, and obligations are demonstrated.
- [ ] Hazards, evidence, source/rights, sensitivity, policy, release, correction, and rollback steward assignments are authenticated where required.
- [ ] Separation of duties is enforced for policy-significant or life-safety-adjacent releases.
- [ ] A candidate-bound ReviewRecord, ReleaseManifest draft, correction path, and RollbackCard draft exist and cross-bind correctly.
- [ ] Public API, MapLibre/Evidence Drawer, exports, dashboards, search, and AI surfaces pass the not-for-life-safety and governed-path audit.
- [ ] Alias mutation, cache invalidation, correction propagation, rollback execution, and recovery verification have operational evidence.
- [ ] Required hosted checks and repository settings enforcement are verified at the exact candidate head/merge ref.
- [ ] The accountable release authority performs a separate governed decision; this runbook does not do so.

[Back to top](#top)

---

## 18. Runbook maintenance and rollback

This revision changes documentation only. It creates no source admission, data mutation, schema migration, policy activation, candidate, review, release decision, deployment, promotion, or publication.

### Validation for a future runbook edit

1. Re-pin the evidence snapshot to current `main`.
2. Re-read accepted Directory Rules and applicable ADRs.
3. Re-check the target, sibling runbooks, candidate lane, policy lane, Makefile, workflows, validators, tests, release root, and open pull requests.
4. Confirm every command and status statement against current bytes.
5. Run applicable documentation and repository guardrails.
6. Read back the exact committed file and inspect the pull-request diff.

### Rollback

Before merge, close the draft pull request and delete only its task branch if no longer needed. After merge, revert the documentation commit through a reviewed pull request. No data, registry, policy, release, deployment, or public-state cleanup is required.

[Back to top](#top)

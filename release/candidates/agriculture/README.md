<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-candidates-agriculture-readme
title: Agriculture Release Candidate Review Lane
type: per-domain-release-candidate-index
version: v2
status: draft; repository-grounded; pre-publication
contract_version: "3.0.0"
owners: [bartytime4life]
created: 2026-07-03
updated: 2026-07-18
policy_label: public
truth_posture: cite-or-abstain
responsibility_root: release/
lane_role: agriculture candidate dossier index and pre-publication review boundary
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: 3c0b8f0fa2d9d2a490701d72a5a5b3bc448b02e0
  prior_blob: 02bd65e2e3785bfdbf3922ba16dc79afadc84ee9
related:
  - ../README.md
  - ../../README.md
  - ../../agriculture/README.md
  - ./county_year_panel_v0/README.md
  - ../../manifests/agriculture/README.md
  - ../../promotion_decisions/README.md
  - ../../correction_notices/README.md
  - ../../rollback_cards/README.md
  - ../../withdrawal_notices/README.md
  - ../../changelog/README.md
  - ../../../data/processed/agriculture/README.md
  - ../../../data/published/agriculture/README.md
  - ../../../data/registry/sources/agriculture/README.md
  - ../../../data/proofs/agriculture/README.md
  - ../../../pipeline_specs/agriculture/README.md
  - ../../../contracts/domains/agriculture/aggregation-receipt.md
  - ../../../schemas/contracts/v1/domains/agriculture/aggregation_receipt.schema.json
  - ../../../schemas/contracts/v1/release/release_manifest.schema.json
  - ../../../policy/domains/agriculture/README.md
  - ../../../tests/domains/agriculture/README.md
  - ../../../tests/release/README.md
  - ../../../fixtures/domains/agriculture/release/README.md
  - ../../../docs/domains/agriculture/PIPELINE.md
  - ../../../docs/domains/agriculture/CANONICAL_PATHS.md
  - ../../../docs/domains/agriculture/MISSING_OR_PLANNED_FILES.md
  - ../../../docs/runbooks/agriculture/PROMOTION_RUNBOOK.md
  - ../../../docs/runbooks/agriculture/ROLLBACK_RUNBOOK.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/registers/DRIFT_REGISTER.md
  - ../../../.github/CODEOWNERS
  - ../../../.github/workflows/domain-agriculture.yml
  - ../../../.github/workflows/release-dry-run.yml
tags: [kfm, release, candidates, agriculture, pre-publication, evidence, policy, validation, review, rollback]
notes:
  - "This README indexes Agriculture release-candidate dossiers and defines their pre-publication review boundary. It is not release approval, a manifest, a promotion decision, a proof bundle, or a published artifact."
  - "The bounded inventory currently establishes one child candidate, county_year_panel_v0, whose merged dossier remains PROPOSED and BLOCKED_FOR_EVIDENCE_AND_VALIDATION."
  - "Candidate-local ReleaseManifest, PromotionDecision, and RollbackCard files proposed in planning documents remain LINEAGE / CONFLICTED with the shared release-lane topology and are not created here."
  - "CODEOWNERS review routing is not a stewardship assignment, independent review, release approval, or publication authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `release/candidates/agriculture/` — Agriculture Release Candidate Review Lane

> Index Agriculture release-candidate dossiers, preserve their blockers and support pointers, and prevent proposed Agriculture outputs from being treated as released before evidence, policy, validation, review, correction, and rollback gates close.

![status](https://img.shields.io/badge/status-repository--grounded%20draft-orange)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-candidates-blueviolet)
![domain](https://img.shields.io/badge/domain-agriculture-green)
![publication](https://img.shields.io/badge/publication-not__authorized-red)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)
![contract](https://img.shields.io/badge/contract-v3.0.0-1f6feb)

> [!IMPORTANT]
> **Safe conclusion at `main@3c0b8f0f…`:** the bounded Agriculture candidate inventory contains this parent README and one indexed child, [`county_year_panel_v0`](./county_year_panel_v0/README.md). That child is `PROPOSED`, `BLOCKED`, not released, and not approved for manifest preparation. No inspected candidate, workflow, schema, fixture, proof lane, merge, or generated receipt establishes an Agriculture release.
>
> Differently named, unindexed, generated, external, or runtime-only material remains **UNKNOWN** unless separately verified.

## Quick navigation

- [Purpose](#purpose)
- [Status and evidence boundary](#status-and-evidence-boundary)
- [Authority and repository fit](#authority-and-repository-fit)
- [Current candidate inventory](#current-candidate-inventory)
- [Candidate lifecycle](#candidate-lifecycle)
- [What belongs here](#what-belongs-here)
- [What does not belong here](#what-does-not-belong-here)
- [Candidate admission contract](#candidate-admission-contract)
- [Agriculture release gates](#agriculture-release-gates)
- [Required dossier structure](#required-dossier-structure)
- [Evidence, source-role, and sensitivity rules](#evidence-source-role-and-sensitivity-rules)
- [Validation and fixture posture](#validation-and-fixture-posture)
- [Automation posture](#automation-posture)
- [Release handoff routing](#release-handoff-routing)
- [Review and separation of duties](#review-and-separation-of-duties)
- [Maintenance and definition of done](#maintenance-and-definition-of-done)
- [Evidence ledger](#evidence-ledger)
- [Open verification](#open-verification)
- [Changelog](#changelog)
- [Rollback for this README](#rollback-for-this-readme)

---

## Purpose

`release/candidates/agriculture/` is the Agriculture pre-publication review lane under the `release/` responsibility root.

It answers five bounded questions:

1. Which Agriculture release candidates are currently indexed?
2. What is each candidate's verified status and finite decision?
3. Which artifact, source, evidence, rights, policy, validation, review, correction, and rollback records support it?
4. Which blockers prevent manifest preparation or release?
5. Which shared release lane owns the next governed record?

A candidate is not a release. A candidate folder, README, pull request, merge, workflow result, schema pass, fixture pass, generated receipt, or public URL must not be interpreted as publication approval.

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed state transition, not a file move or repository event.

[Back to top](#top)

---

## Status and evidence boundary

| Field | Current posture |
|---|---|
| Document type | Per-domain candidate-lane index and review contract |
| Owning root | `release/` |
| Candidate lane | `release/candidates/agriculture/` |
| Current bounded child inventory | One indexed child: `county_year_panel_v0/` |
| Current child state | `PROPOSED` / `BLOCKED_FOR_EVIDENCE_AND_VALIDATION` |
| Approved Agriculture candidate | None established by the inspected evidence |
| Approved Agriculture manifest | None established by the inspected evidence |
| Published Agriculture release | None established by the inspected evidence |
| Candidate artifact inventory | **UNKNOWN** beyond README-level records |
| Executable candidate validation | Not established |
| Release authority of this README | None |
| Default posture | Hold, deny, abstain, narrow, or error rather than infer readiness |

### Truth labels

| Label | Meaning here |
|---|---|
| `CONFIRMED` | Verified from a repository file, immutable ref/blob, workflow definition/run, or generated artifact in the current work session |
| `PROPOSED` | Candidate meaning, contract, path interpretation, future gate, or implementation direction not yet established |
| `UNKNOWN` | Not resolved by the bounded inspection |
| `NEEDS VERIFICATION` | Checkable but not verified strongly enough to act as fact |
| `CONFLICTED` | Current repository or doctrine sources disagree and no accepted decision selects a winner |
| `LINEAGE` | Historical or planning material retained for traceability, not current authority by itself |

Runtime and release outcomes such as `HOLD_FOR_EVIDENCE`, `PROMOTE_TO_MANIFEST`, `DENY`, `ABSTAIN`, and `ERROR` are operational states, not substitutes for these authoring labels.

[Back to top](#top)

---

## Authority and repository fit

Directory Rules place release-candidate review under `release/` while keeping data, evidence, policy, validation, and published carriers in their own responsibility roots.

| Responsibility | Owning lane |
|---|---|
| Agriculture candidate dossiers and blocker state | This lane |
| Agriculture release orientation | [`release/agriculture/`](../../agriculture/README.md) |
| Candidate artifacts | [`data/processed/agriculture/`](../../../data/processed/agriculture/README.md) or another accepted staging lane |
| Source admission and source role | [`data/registry/sources/agriculture/`](../../../data/registry/sources/agriculture/README.md) |
| Evidence and proof support | [`data/proofs/agriculture/`](../../../data/proofs/agriculture/README.md) |
| Semantic meaning | `contracts/` |
| Machine-checkable shape | `schemas/` |
| Admissibility and obligations | `policy/` |
| Executable tests and fixtures | `tests/` and `fixtures/` |
| Release manifest | Shared manifest lane or accepted successor |
| Promotion decision | Shared promotion-decision lane |
| Correction, withdrawal, supersession, and rollback | Shared release-governance lanes |
| Published public-safe carriers | [`data/published/agriculture/`](../../../data/published/agriculture/README.md) |
| Public client access | Governed API and released-artifact paths only |

### Candidate-local release-object conflict

[`MISSING_OR_PLANNED_FILES.md`](../../../docs/domains/agriculture/MISSING_OR_PLANNED_FILES.md) proposed candidate-local files such as `release_manifest.json`, `promotion_decision.json`, and `rollback_card.json`.

Current repository guidance routes those record families into shared, record-type-specific release lanes. Treat candidate-local release-object paths as **LINEAGE / CONFLICTED** until an accepted ADR and migration plan resolve the topology. Do not create both homes.

[Back to top](#top)

---

## Current candidate inventory

The bounded repository search and direct file reads establish the following candidate lane:

| Candidate | Candidate meaning | Current status | Manifest readiness | Public effect |
|---|---|---|---|---|
| [`county_year_panel_v0`](./county_year_panel_v0/README.md) | **PROPOSED** county-by-year Agriculture aggregate panel | `BLOCKED` / `BLOCKED_FOR_EVIDENCE_AND_VALIDATION` | Not approved | None |

The child dossier reports:

- no concrete candidate artifact or digest;
- no admitted source set or closed rights posture;
- no field-to-`EvidenceBundle` mapping;
- no enforced aggregation profile or typed `AggregationReceipt`;
- no substantive candidate-specific validation suite;
- no accepted `PromotionDecision`, `ReleaseManifest`, correction path, or rollback target; and
- no independent release approval.

### Inventory limits

A code-search result is not a recursive filesystem proof. Other candidate directories, generated files, unindexed records, history-only content, or external systems remain **UNKNOWN** until directly inspected.

Add a row here only after the candidate path exists and its status can be verified. Do not add roadmap ideas as if they were active candidates.

[Back to top](#top)

---

## Candidate lifecycle

Use finite states and preserve the difference between dossier maturity and release authority.

| Candidate state | Meaning | Permitted next step |
|---|---|---|
| `PROPOSED` | Candidate identity exists; packet is incomplete | Assemble bounded support records |
| `ASSEMBLING` | Artifact and support packet are being gathered | Continue closure work |
| `READY_FOR_REVIEW` | Required packet is complete enough for steward review | Open governed review |
| `BLOCKED` | One or more named gates are unresolved | Hold; remediate the named blocker |
| `REPAIR_REQUIRED` | Candidate content or support records require correction | Return to the owning upstream lane |
| `DEFERRED` | Candidate remains eligible but is not being advanced | Preserve state and review trigger |
| `APPROVED_FOR_MANIFEST` | Steward decision permits manifest preparation | Prepare a manifest in the accepted manifest lane |
| `PROMOTED` | Candidate is bound into an approved release path | Preserve release, correction, and rollback lineage |
| `SUPERSEDED` | A newer candidate replaces this candidate | Link the replacement and preserve history |
| `WITHDRAWN` | Candidate is removed from consideration | Record reason and affected references |

`APPROVED_FOR_MANIFEST` does not mean `RELEASED`. `PROMOTE_TO_MANIFEST` authorizes manifest preparation only.

### Candidate hold outcomes

Prefer explicit reasoned holds:

- `HOLD_FOR_ARTIFACT`
- `HOLD_FOR_SOURCE_ADMISSION`
- `HOLD_FOR_RIGHTS`
- `HOLD_FOR_EVIDENCE`
- `HOLD_FOR_AGGREGATION`
- `HOLD_FOR_POLICY`
- `HOLD_FOR_VALIDATION`
- `HOLD_FOR_REVIEW`
- `HOLD_FOR_RELEASE_TOPOLOGY`
- `HOLD_FOR_CORRECTION_PATH`
- `HOLD_FOR_ROLLBACK`

[Back to top](#top)

---

## What belongs here

- This parent README and candidate-lane indexes.
- One child directory per distinct Agriculture release candidate.
- Candidate dossier Markdown that records identity, scope, support pointers, blockers, review state, and finite decision.
- Candidate readiness checklists and version history.
- Pointers to immutable processed/staged artifacts without duplicating payloads.
- Pointers to admitted sources, evidence, policy decisions, validation reports, review records, manifests, corrections, withdrawals, supersession records, and rollback targets.
- Public-safe summaries of why a candidate is blocked, deferred, repair-required, approved for manifest preparation, superseded, or withdrawn.
- Migration notes when accepted release topology changes.

Candidate records should be compact, pointer-based, and safe to review publicly. Sensitive details belong in approved restricted systems and should be represented here only by safe references and disposition state.

[Back to top](#top)

---

## What does not belong here

- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED payloads.
- Bulk tables, rasters, vectors, COGs, PMTiles, GeoParquet, shapefiles, CSV exports, API payloads, or report data.
- Source descriptors, credentials, API keys, tokens, private endpoints, source dumps, or live-query secrets.
- `EvidenceBundle` or proof content as the primary record.
- Semantic contracts, machine schemas, policy bundles, validator code, tests, or fixtures.
- Final `ReleaseManifest`, `PromotionDecision`, `CorrectionNotice`, `WithdrawalNotice`, or `RollbackCard` records when a shared lane owns that family.
- Private farm, operator, landowner, tenant, worker, parcel, facility, storage, chemical, livestock, irrigation, production, logistics, compliance, or proprietary detail.
- Exact sensitive cross-domain joins or suppression parameters that increase re-identification risk.
- Generated prose presented as evidence, validation, steward review, or release approval.
- Silent promotion by moving, copying, renaming, merging, or publishing files.

[Back to top](#top)

---

## Candidate admission contract

A new child candidate may be indexed only when it has a stable identity and an explicit non-release status.

### Minimum fields at candidate creation

| Field | Requirement |
|---|---|
| Candidate ID | Stable, deterministic where practical |
| Candidate version | Explicit and immutable for the dossier revision |
| Domain | `agriculture` |
| Proposed meaning | Narrow, bounded, and labeled `PROPOSED` until contract evidence exists |
| Candidate owner | Verified GitHub identity or `OWNER_TBD`; do not invent teams |
| Artifact state | Pointer or explicit `NOT ESTABLISHED` |
| Proposed release target | Pointer or explicit `NOT ESTABLISHED` |
| Source/evidence state | Explicit closure status |
| Rights/sensitivity state | Explicit posture and blockers |
| Validation state | Performed checks, failures, and not-run checks |
| Review state | Pending, approved, changes requested, rejected, or governed override |
| Finite decision | Proposed, hold, repair, defer, approve-for-manifest, supersede, or withdraw |
| Correction/rollback state | Pointer or explicit blocker |
| Date and immutable evidence snapshot | Required for repository-state claims |

### Candidate identity rules

- Do not derive meaning solely from a folder name.
- Do not reuse an ID for materially different data, grain, time, source set, or public surface.
- Do not mutate an approved candidate packet in place; supersede it with traceable lineage.
- Preserve content digests and immutable artifact references where practical.
- Keep candidate identity distinct from release ID, manifest ID, layer ID, run ID, and source ID.

[Back to top](#top)

---

## Agriculture release gates

Every Agriculture candidate must fail closed when a load-bearing gate is unresolved.

| Gate | Required question | Failure posture |
|---|---|---|
| Identity | Is the candidate stable, versioned, scoped, and owned? | `HOLD_FOR_ARTIFACT` |
| Artifact | Is there an immutable candidate artifact pointer and digest? | `HOLD_FOR_ARTIFACT` |
| Meaning and shape | Are grain, keys, fields, units, time, geography, and schema defined? | `REPAIR_REQUIRED` or hold |
| Source admission | Do all sources resolve to admitted records with source role and rights? | `HOLD_FOR_SOURCE_ADMISSION` |
| Evidence | Do claim/field `EvidenceRef` values resolve to `EvidenceBundle` support? | `HOLD_FOR_EVIDENCE` / `ABSTAIN` |
| Aggregation | Is public aggregation/suppression defined and receipt-backed? | `HOLD_FOR_AGGREGATION` |
| Rights and sensitivity | Is requested use allowed at the requested precision and audience? | `DENY`, `RESTRICT`, or hold |
| Policy | Is a versioned `PolicyDecision` present with obligations and reason code? | `HOLD_FOR_POLICY` |
| Validation | Do deterministic positive and negative checks pass? | `HOLD_FOR_VALIDATION` |
| Review | Are required, distinct reviewers recorded? | `HOLD_FOR_REVIEW` |
| Release topology | Are manifest and decision homes accepted and non-duplicative? | `HOLD_FOR_RELEASE_TOPOLOGY` |
| Correction | Can errors be corrected and downstream consumers identified? | `HOLD_FOR_CORRECTION_PATH` |
| Rollback | Is a prior safe target or withdrawal plan defined and drilled? | `HOLD_FOR_ROLLBACK` |

Exact field/operator, parcel-adjacent, small-cell, facility, irrigation, chemical, livestock, storage, logistics, or cross-domain inference defaults to deny public exact exposure unless a reviewed, rights-cleared transformation explicitly permits a safer representation.

Style-only hiding is not redaction, generalization, aggregation, or policy enforcement.

[Back to top](#top)

---

## Required dossier structure

A candidate child README should include at least:

```markdown
# <candidate-id> — <candidate title>

## Candidate status
PROPOSED / ASSEMBLING / READY_FOR_REVIEW / BLOCKED / REPAIR_REQUIRED /
DEFERRED / APPROVED_FOR_MANIFEST / PROMOTED / SUPERSEDED / WITHDRAWN

## Candidate identity
<id, version, domain, owner, date, evidence snapshot>

## Proposed scope
<grain, geography, time, measures, intended audience and surface>

## Candidate artifact
<immutable pointer, digest, artifact manifest, or NOT ESTABLISHED>

## Source and rights closure
<SourceDescriptor refs, source roles, rights, query/snapshot identity, blockers>

## Evidence closure
<EvidenceRef-to-EvidenceBundle mapping and unresolved claims>

## Aggregation and sensitivity
<profile, suppression, redaction/generalization, receipt refs, obligations>

## Validation
<schema, identity, units, time, geography, source role, evidence, policy,
public-boundary, correction, and rollback checks>

## Review
<required reviewers, states, dates, and separation-of-duties posture>

## Release handoff
<PromotionDecision and ReleaseManifest pointers or explicit blockers>

## Correction and rollback
<correction consumers, withdrawal/supersession path, rollback target and drill>

## Current decision
<finite outcome plus evidence-grounded reason>
```

Candidate payloads, evidence objects, policy code, tests, fixtures, and final release records remain in their owning roots.

[Back to top](#top)

---

## Evidence, source-role, and sensitivity rules

### Source-role anti-collapse

Preserve source role from admission through candidate review:

| Source role | Candidate rule |
|---|---|
| `observed` | Use only when measurement method and rights support direct-observation status |
| `aggregate` | Do not infer field, operator, parcel, or facility truth from aggregate cells |
| `modeled` | Preserve model/run identity, inputs, uncertainty, validation, and reality boundary |
| `regulatory` | Preserve legal/effective scope; do not treat as observation or release approval |
| `administrative` | Administrative presence does not prove real-world condition |
| `context` | May frame interpretation; cannot prove a consequential claim alone |
| `candidate` | Blocks publication until reviewed and promoted |
| `synthetic` | Must remain visibly non-real and excluded from evidence claims |
| `restricted` | Defaults to deny, restrict, redact, generalize, delay, or quarantine |

### Evidence closure

A candidate is not evidence. Its consequential claims must resolve to admissible evidence through `EvidenceRef` and `EvidenceBundle` support. Missing, stale, revoked, conflicted, or non-resolvable evidence produces a hold, abstention, denial, or error.

### Agriculture privacy and rights

Candidate review must explicitly address:

- operator, landowner, tenant, worker, or living-person identity;
- parcel, field, facility, storage, irrigation, equipment, chemical, livestock, or logistics precision;
- private yield, proprietary production, program participation, inspection, enforcement, disease, pest, contamination, and pesticide records;
- aggregate-cell suppression and re-identification risk;
- source license, redistribution, attribution, and revision rights; and
- cross-domain joins with People/DNA/Land, Soil, Hydrology, Habitat, Hazards, Roads/Rail/Trade, and Settlements/Infrastructure.

When rights or sensitivity is unclear, keep the candidate blocked.

[Back to top](#top)

---

## Validation and fixture posture

Current repository evidence does not establish a complete Agriculture candidate-validation or release-governance suite.

| Surface | Current safe interpretation |
|---|---|
| [`tests/domains/agriculture/`](../../../tests/domains/agriculture/README.md) | Documentation-heavy; known NASS test modules are placeholders rather than collected tests |
| [`tests/release/`](../../../tests/release/README.md) | Direct lane is README-only in its bounded inventory; dedicated release suite not established |
| [`fixtures/domains/agriculture/release/`](../../../fixtures/domains/agriculture/release/README.md) | Release-shaped fixture guidance exists; direct payload inventory remains unverified |
| [`data/proofs/agriculture/`](../../../data/proofs/agriculture/README.md) | Draft proof-lane guidance; concrete proof schemas, indexes, validators, access controls, and release linkage remain unresolved |
| `AggregationReceipt` contract/schema | Draft semantic contract plus permissive scaffold schema |
| `ReleaseManifest` schema | Permissive scaffold; not sufficient release validation |
| Agriculture policy lane | Fail-closed intent documented; executable enforcement remains unverified |

### Required negative cases

A mature no-network suite should reject:

- missing or mutable artifact pointers;
- unresolved source identity, rights, or source role;
- aggregate-to-field or model-to-observed promotion;
- unstable county/crop/year keys or mixed units;
- unclear missing-value, revision, or suppression semantics;
- unresolved or stale `EvidenceRef` values;
- absent `AggregationReceipt` or redaction/generalization support;
- field/operator/small-cell inference;
- missing policy, reviewer, manifest, correction, or rollback support;
- direct public access to candidate, processed, catalog, or proof stores; and
- generated language presented as evidence or approval.

A passing test proves only the declared test scope. It does not approve a candidate or release.

[Back to top](#top)

---

## Automation posture

| Workflow | Current boundary |
|---|---|
| [`domain-agriculture`](../../../.github/workflows/domain-agriculture.yml) | Read-only readiness holds for validation, proof, and release-dry-run maturity; no Agriculture truth validation or release |
| [`release-dry-run`](../../../.github/workflows/release-dry-run.yml) | TODO-only jobs that echo candidate assembly, promotion gate, and rollback-card checks |

`domain-agriculture` uses ordinary pull-request/push triggers, `workflow_dispatch`, `contents: read`, GitHub-hosted runners, concurrency cancellation, timeouts, and disabled persisted checkout credentials. It intentionally reports `WORKFLOW_HOLD` while accepted executable commands are absent.

The general `release-dry-run` workflow still produces TODO-only green jobs. Its success is not candidate assembly, promotion-gate enforcement, rollback verification, release approval, or publication authority.

The Agriculture workflow's current placeholder detector excludes one known placeholder test path while another docstring-only Agriculture `test_*.py` exists. Treat the actual workflow result and detector behavior as **NEEDS VERIFICATION**; do not infer success from the workflow definition.

Branch protection, required-check coupling, immutable action pinning, and workflow-run history remain separate evidence.

[Back to top](#top)

---

## Release handoff routing

Use the narrowest accepted shared lane for the next record:

| Record or action | Route | Candidate-lane boundary |
|---|---|---|
| Candidate dossier | This lane | Pre-publication review only |
| Promotion decision | [`release/promotion_decisions/`](../../promotion_decisions/README.md) | Decision may permit manifest preparation; it does not publish |
| Release manifest | [`release/manifests/`](../../manifests/agriculture/README.md) or accepted successor | Canonical singular/plural and domain segmentation remain unresolved |
| Correction notice | [`release/correction_notices/`](../../correction_notices/README.md) | Communication record; not correction authority by itself |
| Rollback/review card | [`release/rollback_cards/`](../../rollback_cards/README.md) or accepted successor | Current parent semantics are conflicted; do not duplicate |
| Withdrawal notice | [`release/withdrawal_notices/`](../../withdrawal_notices/README.md) | Notice must point to governed withdrawal decision |
| Release history | [`release/changelog/`](../../changelog/README.md) | Narrative companion, not sovereign release state |
| Published carrier | [`data/published/agriculture/`](../../../data/published/agriculture/README.md) | Downstream only after governed release |

The repository still carries manifest, correction, and rollback topology drift. Candidate authors must surface that conflict rather than silently selecting or duplicating homes.

[Back to top](#top)

---

## Review and separation of duties

[`CODEOWNERS`](../../../.github/CODEOWNERS) routes `/release/` review to `@bartytime4life`. That is GitHub review routing only.

Before an Agriculture candidate reaches manifest preparation, verify distinct responsibility for:

- Agriculture domain meaning and candidate scope;
- artifact production and pipeline operation;
- source admission, rights, and source-role assignment;
- evidence and proof closure;
- policy, aggregation, privacy, and sensitivity disposition;
- deterministic validation and negative cases;
- release decision and manifest review; and
- correction, withdrawal, supersession, and rollback.

The generator or candidate author must not be treated as the sole approver for policy-significant release work. Merge approval remains separate from release and publication approval.

### Review burden

| Change | Minimum review posture |
|---|---|
| README-only lane guidance | Docs/release-root review |
| New candidate identity or scope | Agriculture domain + release review |
| Candidate artifact or source-set change | Domain + data/pipeline + source/rights review |
| Aggregation, suppression, redaction, or audience change | Policy/sensitivity/aggregation review |
| `READY_FOR_REVIEW` transition | Domain, evidence, policy, validation, and release reviewers identified |
| `APPROVED_FOR_MANIFEST` transition | Independent release decision and complete support pointers |
| Supersession, withdrawal, correction, or rollback | Release + domain + correction/rollback ownership |

[Back to top](#top)

---

## Maintenance and definition of done

Update this README when:

- a candidate child is added, renamed, superseded, withdrawn, or removed;
- a candidate changes finite state;
- manifest, promotion-decision, correction, withdrawal, or rollback topology changes;
- candidate schemas, validators, fixtures, proof producers, policy rules, or CI mature;
- CODEOWNERS or stewardship assignments change;
- Agriculture public aggregation or sensitivity posture changes; or
- a correction reveals that this index overstated repository maturity.

### Definition of done for this lane

This lane may graduate beyond draft only when:

- [ ] candidate inventory is generated or deterministically validated;
- [ ] every indexed child exposes a stable identity, version, status, decision, and immutable evidence snapshot;
- [ ] source, evidence, rights, aggregation, policy, validation, review, correction, and rollback fields are machine-checkable or explicitly governed;
- [ ] candidate-local versus shared release-record topology is resolved by accepted decision and migration guidance;
- [ ] substantive positive and negative fixtures and tests exist;
- [ ] candidate validation and release dry-run commands are deterministic and no-network by default;
- [ ] CI invokes accepted commands and cannot turn missing coverage into success;
- [ ] branch-protection and reviewer requirements are verified;
- [ ] correction and rollback drills have evidence; and
- [ ] public surfaces remain downstream of governed APIs and released artifacts.

[Back to top](#top)

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Prior parent README, blob `02bd65e2…` | `CONFIRMED` | Existing candidate-lane purpose and generic dossier fields | Did not reflect the grounded child dossier or current workflow maturity |
| [`release/candidates/README.md`](../README.md) | `CONFIRMED file / draft guidance` | Parent candidate states and review fields | Does not prove Agriculture candidate completeness |
| [`release/agriculture/README.md`](../../agriculture/README.md) | `CONFIRMED current index` | Agriculture release authority routing and blocked candidate posture | Does not create release records |
| [`county_year_panel_v0`](./county_year_panel_v0/README.md) | `CONFIRMED file / blocked candidate` | Current child identity, blockers, support requirements, and no-release conclusion | Candidate artifact and release support remain unresolved |
| Bounded repository search | `CONFIRMED search` | Surfaced this parent and the county-year child as indexed Agriculture candidate paths | Not a recursive filesystem proof |
| [`PIPELINE.md`](../../../docs/domains/agriculture/PIPELINE.md) and promotion runbook | `CONFIRMED docs / PROPOSED wiring` | Lifecycle, aggregation, gate, receipt, and fail-closed intent | Execution remains unverified |
| Source/spec, contract/schema, policy, test, fixture, and proof READMEs | `CONFIRMED repository artifacts / mixed maturity` | Current placeholder and draft maturity boundaries | Do not establish closure or runtime enforcement |
| Agriculture and release workflows | `CONFIRMED definitions` | Readiness-hold and TODO orchestration posture | Green status is not substantive validation or release proof |
| Directory Rules and drift register | `CONFIRMED governance artifacts` | Responsibility-root separation and conflict visibility | Do not settle unresolved release topology by themselves |
| CODEOWNERS | `CONFIRMED routing` | Current GitHub review route | Not stewardship, independent approval, or branch-protection proof |

No external web research is required for this repository-state documentation update.

[Back to top](#top)

---

## Open verification

- [ ] Confirm exhaustive child inventory under `release/candidates/agriculture/`.
- [ ] Confirm candidate naming, identity, and versioning convention.
- [ ] Confirm canonical candidate artifact/staging path and artifact-manifest contract.
- [ ] Confirm accepted Agriculture candidate schema and validator command.
- [ ] Confirm admitted source records, rights, source roles, and reproducible source-head/query identity.
- [ ] Confirm EvidenceRef-to-EvidenceBundle and proof-manifest contracts.
- [ ] Confirm aggregation/suppression profiles, typed `AggregationReceipt`, redaction/generalization obligations, and public-safe thresholds.
- [ ] Confirm executable Agriculture policy and deterministic positive/negative fixtures.
- [ ] Confirm candidate-to-PromotionDecision and candidate-to-ReleaseManifest handoff.
- [ ] Resolve singular/plural manifest, correction, and rollback/review-card topology.
- [ ] Confirm correction consumers, withdrawal/supersession records, rollback target, and drill.
- [ ] Confirm candidate-specific no-network test suite and release dry-run.
- [ ] Confirm `domain-agriculture` placeholder-detection behavior after the second placeholder test is considered.
- [ ] Confirm branch protection, required checks, immutable action pinning, and independent reviewer assignments.
- [ ] Confirm whether candidate inventory and status can be generated from machine-readable records without making generated output sovereign truth.

[Back to top](#top)

---

## Changelog

### v2 — 2026-07-18

- Replaced generic candidate-lane guidance with a repository-grounded Agriculture candidate index and review contract.
- Indexed the merged `county_year_panel_v0` dossier and preserved its blocked, unreleased posture.
- Added responsibility routing and candidate-local release-object conflict handling.
- Added finite states and hold outcomes, candidate admission rules, common Agriculture release gates, dossier structure, source-role and sensitivity controls, validation maturity, automation posture, handoff routing, separation of duties, evidence ledger, definition of done, and rollback.
- Added `CONTRACT_VERSION = "3.0.0"` and a bounded evidence snapshot.

### v1 — 2026-07-03

- Replaced the prior greenfield stub with initial Agriculture candidate-lane guidance.

[Back to top](#top)

---

## Rollback for this README

This revision changes documentation only.

Before merge, close the pull request or delete the scoped branch.

After merge, revert the generated-receipt commit and README commit in reverse order and restore the prior README blob:

```text
02bd65e2e3785bfdbf3922ba16dc79afadc84ee9
```

No candidate artifact, source admission, pipeline state, evidence, policy, validation, manifest, release, publication, correction, withdrawal, supersession, or rollback state requires restoration.

[Back to top](#top)

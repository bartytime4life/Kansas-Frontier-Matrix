<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-readme
title: release/ — Release Governance Root
type: README
version: v2.0
status: draft; repository-grounded; release-governance-root; readiness-holds-visible; non-authoritative
owner: NEEDS VERIFICATION — default CODEOWNERS route is @bartytime4life; no independent release steward, approver separation, or required-review enforcement was established
created: 2026-07-03
updated: 2026-07-23
supersedes: v1 documentation at the same path; no release, promotion, rollback, correction, publication, signing, deployment, or data behavior is superseded
policy_label: repository-facing; release-governance; candidate-is-not-release; promotion-is-state-transition; no-payloads; cite-or-abstain; correction-aware; rollback-aware
owning_root: release/
responsibility: explain and index release-governance records without becoming a release decision, proof, receipt, policy, schema, data payload, or publication authority
truth_posture: cite-or-abstain; current files and workflow definitions are evidence of bounded repository surfaces, not proof of operational release capability
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: fae69bb52e0ebc7670dc7d20c9eb05cb587520ff
  prior_blob: 089c4a394c5cbf3b9e5a2a1963e68e16be485dce
  directory_rules_blob: 18653c00ba193a4afaa3e07a0924452807fb98ef
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  makefile_blob: 51537af34ee065c2de571134688415042b83b22a
  release_dry_run_workflow_blob: 9baf5b92f954c994ab11e8bb54d480e6309a0579
  promotion_gate_workflow_blob: c22941d5e1fad3317f46591705091ef2b6e7d265
  rollback_drill_workflow_blob: dc42ec4931f95023d364f2559ddcffab94ecfab5
  candidates_readme_blob: 469a5b088bf5367b330b9c8c292165063f3e2d1f
  reviews_readme_blob: d927536c39a2102b1f012007fc8de4facb7abd90
  promotion_decisions_readme_blob: 18c6342f93212992f98d0e354390a36a79749858
  manifests_readme_blob: c699a527ff11bebad6a874ed1a37aa3a8213b86c
  decisions_readme_blob: 9cdd61ae826bfc2fb27db5885c9f903212e8591a
  rollback_readme_blob: aa8b60f4d47e7b73ab3e862f1dcd498691ea4e0c
  rollback_cards_readme_blob: c1fc4d27bca8144faa16e1b888ca95c5d2f88eb5
  withdrawal_notices_readme_blob: 24358c5d9286b74988c42e38aedcba06a87349b1
  signatures_readme_blob: e25a62e73762af96d15fbb6c32c8d03fbac66e30
related:
  - ../docs/architecture/directory-rules.md
  - ../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../.github/CODEOWNERS
  - ../.github/workflows/release-dry-run.yml
  - ../.github/workflows/promotion-gate.yml
  - ../.github/workflows/rollback-drill.yml
  - ../contracts/release/
  - ../schemas/contracts/v1/release/
  - ../policy/release/
  - ../tools/release/
  - ../tests/release/test_promotion_decision_schema.py
  - ../data/receipts/
  - ../data/proofs/
  - ../data/published/
notes:
  - "The first twelve H2 sections follow the Directory Rules §15 folder-README contract."
  - "The workflow files named above are read-only readiness and drift checks. Their success does not assemble, approve, publish, or roll back a release."
  - "The current Makefile release-dry-run and publish-check targets are explicit TODO readiness markers."
  - "Manifest, correction, rollback, review, and decision lane semantics contain unresolved overlap. This README records the conflict and does not choose a migration."
  - "No release, promotion, rollback execution, publication, deployment, source activation, or ADR transition is performed by this document."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `release/` — Release Governance Root

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#status)
[![Authority: release governance](https://img.shields.io/badge/authority-release%20governance-8250df?style=flat-square)](#authority-level)
[![Readiness: explicit holds](https://img.shields.io/badge/readiness-explicit%20holds-b42318?style=flat-square)](#workflow-readiness-boundaries)
[![Publication: not performed](https://img.shields.io/badge/publication-not%20performed-6e7781?style=flat-square)](#outputs)
[![Truth: cite or abstain](https://img.shields.io/badge/truth-cite%20or%20abstain-1a7f37?style=flat-square)](../CONTRIBUTING.md#evidence-and-truth-labels)
[![Rollback: required](https://img.shields.io/badge/rollback-required-1f6feb?style=flat-square)](#maintenance-correction-and-rollback)

> **One-line purpose.** `release/` owns KFM release-governance records and review state; it does not store published payloads, turn prose into approval, or make a candidate public.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Does not belong](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related roots](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Lanes](#current-repository-lane-map) · [Workflow holds](#workflow-readiness-boundaries) · [States](#release-state-model) · [Record contract](#release-record-minimum-contract) · [Open verification](#open-verification-register) · [Rollback](#maintenance-correction-and-rollback)

> [!IMPORTANT]
> **Release governance is not publication.** A candidate, review, manifest, decision, signature packet, correction note, rollback card, workflow result, pull request, or merge is not automatically a released public artifact. Published payloads belong under [`data/published/`](../data/published/) only after the applicable evidence, policy, validation, review, release, correction, and rollback gates are satisfied.

> [!WARNING]
> **Current release automation is bounded by explicit holds.** The repository can inspect release readiness and validate selected proposed shapes, but the accepted candidate assembler, manifest validator, accountable review flow, promotion evaluator, rollback engine, and published-alias verifier are not established as operational release machinery.

> [!NOTE]
> This README is a repository-grounded index and maintenance contract. It records current surfaces and conflicts without accepting an ADR, resolving lane duplication, promoting a candidate, or changing any release state.

---

## Purpose

`release/` is the canonical responsibility root for KFM release-governance records.

Its job is to make the path from candidate review to a reversible release decision inspectable. It connects release-facing records to evidence, validation, policy, review, manifests, correction, withdrawal, supersession, signatures, changelog, and rollback support.

The root answers governance questions such as:

- What candidate or release-facing record is under review?
- Which evidence and validation records support it?
- Which policy posture and public-safety obligations apply?
- Who reviewed or decided the release state?
- Which manifest, correction, withdrawal, notice, or changelog record carries the transition?
- What prior state and rollback target would be restored if the change is reversed?

It must not answer those questions by implication, folder movement, badge color, workflow success, or generated prose.

[Back to top](#top)

---

<a id="status--authority"></a>

## Authority level

| Field | Current bounded result |
|---|---|
| Responsibility root | **CONFIRMED:** `release/` is the release-governance root. |
| README authority | Guidance, index, and maintenance contract only. |
| Higher-authority records | Governed release records, evidence and validation support, applicable policy decisions, accountable reviews, manifests, corrections, rollback records, signatures, and accepted ADRs. |
| Artifact boundary | Released public-safe payloads belong under `data/published/`; receipts under `data/receipts/`; proofs under `data/proofs/`; contracts, schemas, and policy remain in their canonical roots. |
| GitHub review routing | **CONFIRMED:** [`.github/CODEOWNERS`](../.github/CODEOWNERS) routes `/release/` to `@bartytime4life`. |
| Review limitation | CODEOWNERS is routing, not a `ReviewRecord`, stewardship assignment, independent approval, release authorization, or proof that review occurred. |
| Publication authority | **NOT CREATED by this README.** |
| Operational release capability | **UNKNOWN / NEEDS VERIFICATION** beyond the bounded workflow and shape checks documented below. |

<a id="placement-basis"></a>

Directory Rules basis:

- release decisions, manifests, rollback cards, corrections, and related governance records belong under `release/`;
- published artifacts remain distinct under `data/published/`;
- receipts and proofs must not be duplicated here;
- canonical policy-as-code remains under `policy/`;
- lane consolidation, root retirement, or a parallel authority requires the applicable ADR and migration discipline.

[Back to top](#top)

---

## Status

| Surface | Truth status | Current bounded finding |
|---|---|---|
| Root path and README | `CONFIRMED` | `release/README.md` exists at the canonical release-governance root. |
| Candidate, review, manifest, decision, correction, notice, rollback, withdrawal, signature, and changelog lanes | `CONFIRMED_MIXED` | Parent indexes and selected records exist; maturity and semantics differ by lane. |
| ReleaseManifest shape | `PROPOSED / HOLD` | The current schema is permissive and id-only; its declared fixture and validator paths are absent. |
| PromotionDecision shape | `PROPOSED / BOUNDED` | Non-empty valid/invalid fixtures and a dedicated shape test exist, but no operational policy/review gate is thereby proven. |
| Review records | `HOLD` | The inspected release review lane contains guidance, not accountable review records. |
| RollbackCard shape and records | `PROPOSED / HOLD` | Schemas are permissive; declared fixtures/validators are absent; root card JSONs remain placeholder records. |
| Candidate assembly | `WORKFLOW_SKIPPED_EXPLICIT / HOLD` | No candidate packet is assembled by the current workflow. |
| Promotion execution | `WORKFLOW_SKIPPED_EXPLICIT / HOLD` | The hydrology promoter is not executed; its smoke decision has unresolved support references. |
| Rollback execution | `WORKFLOW_SKIPPED_EXPLICIT / HOLD` | No rollback engine, accepted profile, target mutation, or receipt flow is run. |
| Published-alias verification | `WORKFLOW_SKIPPED_EXPLICIT / HOLD` | No accepted alias mechanism or behavioral rollback proof is established. |
| Human review enforcement | `NEEDS VERIFICATION` | Branch protection, required reviews, separation of duties, and ruleset coupling were not established from file evidence. |
| Production release/runtime parity | `UNKNOWN` | No deployment, production release, registry, dashboard, or runtime evidence is claimed here. |

> [!CAUTION]
> A successful readiness workflow can prove that a known hold remains visible and fail-closed. It does not prove that the held capability exists.

[Back to top](#top)

---

## What belongs here

- Root and lane READMEs for release governance.
- Candidate review packets and candidate indexes.
- Governed review, decision, and promotion-decision records.
- Release manifests and manifest indexes.
- Release-facing policy review pointers, not canonical policy rules.
- Correction and withdrawal records and notices.
- Rollback review records and rollback cards.
- Signature and signoff packets.
- Human-readable changelog records tied to governed transitions.
- Stable pointers to evidence, validation receipts, policy decisions, proofs, source records, published targets, correction lineage, and rollback targets.
- Explicit `DRAFT`, `READY_FOR_REVIEW`, `HELD`, `NO_ACTION`, correction, withdrawal, supersession, and release-state records.
- Documentation of unresolved lane semantics when the repository carries overlapping singular/plural or review/decision paths.

[Back to top](#top)

---

## What does NOT belong here

- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data payloads.
- Bulk datasets, tiles, PMTiles, COGs, GeoParquet, exports, service payloads, or map-ready artifacts.
- Receipts of record that belong under `data/receipts/`.
- Proof objects that belong under `data/proofs/`.
- Source descriptors or source registries.
- Semantic contracts or machine schemas.
- Canonical policy rules, bundles, or policy fixtures.
- Validator, pipeline, connector, application, or runtime code.
- Generated summaries presented as evidence, approval, release authority, or publication truth.
- Silent promotion, correction, withdrawal, or rollback by moving files.
- A duplicate release, proof, receipt, catalog, source, schema, contract, or policy authority.
- Secrets, private keys, signing credentials, protected material, or restricted precise locations.

[Back to top](#top)

---

## Inputs

Release governance consumes pointers and review state, not ungoverned payload copies.

| Input family | Minimum posture |
|---|---|
| Candidate | Stable identity, bounded scope, artifact pointer, proposed target, and current candidate state. |
| Evidence | Resolvable `EvidenceRef` / `EvidenceBundle` support where release claims depend on evidence. |
| Validation | Applicable schema, contract, integrity, catalog, citation, boundary, and public-safety results. |
| Policy | Rights, sensitivity, access, stale-state, correction, and public-surface decisions where applicable. |
| Review | Accountable reviewer identity, review target, outcome, reason, and separation-of-duties posture where required. |
| Manifest inputs | Included records, artifact identities, release scope, previous state, correction path, and rollback target. |
| Correction or withdrawal support | Affected state, evidence and validation reason, public effect, notice needs, and replacement or rollback path. |
| Signature support | Verified signoff or attestation references; never raw secret material. |
| Repository evidence | Pinned files, schemas, fixtures, tests, workflows, manifests, receipts, proofs, logs, and generated outputs tied to a known revision. |

Missing or unresolved inputs produce a visible hold, abstention, denial, or error rather than an implied approval.

[Back to top](#top)

---

## Outputs

The root may support or contain governed records such as:

- candidate status and review packets;
- release review records;
- promotion and release decisions;
- release manifests;
- release-facing policy-review pointers;
- correction, withdrawal, and supersession records;
- correction and withdrawal notices;
- rollback review records and rollback cards;
- signature/signoff packets;
- changelog entries;
- explicit hold, no-action, repair, defer, and supersession outcomes.

The root does **not** emit a public artifact merely because one of those records exists. A released payload is a separate governed output under `data/published/` and must retain the release, evidence, policy, correction, and rollback references required by its significance.

No release, promotion, correction, rollback execution, deployment, or publication is performed by editing this README.

[Back to top](#top)

---

## Validation

Validation must distinguish document correctness, shape checks, readiness inspection, and operational release proof.

### Repository commands and their scope

| Command or workflow | What it currently proves | What it does not prove |
|---|---|---|
| `make validate` | Runs the configured aggregate schema validators and the repository schema/contract tests. | A full release system, candidate assembly, review, promotion, rollback, or publication. |
| `make release-dry-run` | Prints the current TODO marker. | Candidate assembly or dry-run execution. |
| `make publish-check` | Prints the current TODO marker. | Promotion policy evaluation or release approval. |
| `tests/release/test_promotion_decision_schema.py` | Exercises selected `PromotionDecision` shape fixtures. | Evidence resolution, policy execution, accountable review, rollback target validity, or lifecycle transition. |
| `release-dry-run` workflow | Fails on drift from its known readiness boundary and runs a bounded `PromotionDecision` fixture test. | Candidate assembly, release record creation, or publication. |
| `promotion-gate` workflow | Proves selected doctrine absence is fail-closed and exercises proposed descriptor/decision shapes. | A real review record, promotion policy decision, or release transition. |
| `rollback-drill` workflow | Inspects placeholder rollback, card, and published-alias surfaces. | A rollback simulation, alias mutation, invalidation, or rollback receipt. |

### Required documentation checks for this README

- one stable H1 and preserved `kfm://doc/release-readme` identity;
- the twelve Directory Rules §15 H2 sections first and in exact order;
- balanced metadata and fenced blocks;
- unique custom anchors and resolved internal fragments;
- repository-relative links checked against the pinned tree;
- no invented owners, approvals, commands, test passes, release states, or deployment claims;
- no secret, credential, restricted-location, living-person, DNA, or other sensitive payload introduced;
- generated provenance receipt validates and binds the README content hash;
- remote branch bytes and exact changed-path set match the reviewed packet.

[Back to top](#top)

---

## Review burden

| Review question | Required posture |
|---|---|
| Does the record change release state? | Require an accountable release decision and the applicable evidence, validation, policy, manifest, correction, and rollback support. |
| Does it affect rights, sensitivity, living people, DNA, archaeology, rare species, infrastructure, sovereignty, or precise locations? | Require the applicable policy and domain review; fail closed when unclear. |
| Does it change a canonical root, lane meaning, schema home, lifecycle phase, or parallel authority? | Require the applicable accepted ADR and migration/rollback plan. |
| Does it only update documentation? | Still require review for accuracy, preserved identity, claim limits, links, and no-loss behavior. |
| Does CODEOWNERS request `@bartytime4life`? | Treat that as GitHub routing only; do not infer independent approval or separation of duties. |
| Did a workflow pass? | Inspect whether it proved behavior or merely preserved a readiness hold. |

**NEEDS VERIFICATION:** repository rulesets, required checks, required CODEOWNER review, independent author/approver separation, approved steward assignments, and operational signing authority.

[Back to top](#top)

---

## Related folders

| Responsibility | Canonical or current related home |
|---|---|
| Released public-safe payloads | [`data/published/`](../data/published/) |
| Process receipts | [`data/receipts/`](../data/receipts/) |
| Proof and evidence-closure objects | [`data/proofs/`](../data/proofs/) |
| Release semantic contracts | [`contracts/release/`](../contracts/release/) |
| Release machine schemas | [`schemas/contracts/v1/release/`](../schemas/contracts/v1/release/) |
| Canonical release policy | [`policy/release/`](../policy/release/) |
| Release support tooling | [`tools/release/`](../tools/release/) |
| Validators of record | [`tools/validators/`](../tools/validators/) |
| Release fixture shape test | [`tests/release/test_promotion_decision_schema.py`](../tests/release/test_promotion_decision_schema.py) |
| Candidate lane | [`candidates/`](candidates/) |
| Review lane | [`reviews/`](reviews/) |
| Promotion-decision lane | [`promotion_decisions/`](promotion_decisions/) |
| Manifest lanes | [`manifest/`](manifest/) and [`manifests/`](manifests/) |
| Decision lane | [`decisions/`](decisions/) |
| Correction lanes | [`correction/`](correction/) and [`corrections/`](corrections/) |
| Rollback lanes | [`rollback/`](rollback/) and [`rollback_cards/`](rollback_cards/) |
| Communication/history lanes | [`correction_notices/`](correction_notices/), [`withdrawal_notices/`](withdrawal_notices/), and [`changelog/`](changelog/) |
| Signoff packets | [`signatures/`](signatures/) |

[Back to top](#top)

---

## ADRs

| Decision or conflict | Current status | Consequence |
|---|---|---|
| [`ADR-0011 — Receipts vs Proofs vs Manifests vs Catalog Separation`](../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md) | `PROPOSED` | It is not yet authority for a migration or lane retirement. |
| `OPEN-DR-09-b` — trust content under `artifacts/release/` | Unresolved | Do not migrate, delete, canonize, or publish from that compatibility lane without an accepted decision and rollback plan. |
| Manifest singular/plural semantics | Unresolved | Preserve `manifest/` and `manifests/`; do not silently consolidate. |
| Correction singular/plural semantics | Unresolved | Preserve `correction/` and `corrections/`; record the conflict. |
| Rollback review vs. rollback-card semantics | Unresolved | Preserve `rollback/`, `correction/rollback/`, and `rollback_cards/` until their responsibilities are accepted. |
| Review vs. decision vs. promotion-decision separation | Unresolved | Do not collapse lanes from prose alone. |
| Published current-alias mechanism | Draft / proposed | Absence of an alias is not proof of rollback capability. |

This README accepts, rejects, supersedes, or amends no ADR.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-23 |
| Evidence snapshot | `main@fae69bb52e0ebc7670dc7d20c9eb05cb587520ff` |
| Prior README blob | `089c4a394c5cbf3b9e5a2a1963e68e16be485dce` |
| Review result | Repository-grounded documentation modernization; release behavior unchanged. |
| Next review trigger | A release lane appears or changes meaning; a proposed ADR is accepted; a real candidate/review/manifest/promotion/rollback path lands; a workflow hold is replaced by implementation; or a release, correction, withdrawal, rollback, or published alias is exercised. |
| Maximum staleness signal | Re-review when this evidence snapshot is more than six months old or a trigger above occurs first. |

[Back to top](#top)

---

<a id="repo-fit"></a>
<a id="current-lane-index"></a>

## Current repository lane map

The table records verified parent surfaces without claiming equal maturity.

| Lane | Current bounded role | Current evidence posture |
|---|---|---|
| `candidates/` | Pre-release candidate review packets. | Parent README exists; current dry-run workflow confirms guidance/placeholders and no candidate packet payload. |
| `reviews/` | Accountable release-review record lane. | Parent README exists; inspected workflow inventory contains guidance only, not review records. |
| `promotion_decisions/` | Promotion-decision records. | Parent README exists; hydrology smoke decision has unresolved evidence and rollback references and is not authority. |
| `manifest/` | Singular manifest lane. | Exists; semantics relative to `manifests/` remain unresolved. |
| `manifests/` | Plural manifest collection and domain sublanes. | Parent README and multiple sublanes exist. |
| `decisions/` | Release decision records. | Parent guidance and finite decision classes exist. |
| `policy/` | Release-facing policy review pointers. | Must remain subordinate to canonical `policy/`. |
| `changelog/` | Human-readable release history. | Companion record only; not a manifest, receipt, proof, or decision. |
| `correction/` | Singular correction review lane. | Exists with a nested rollback lane; semantics remain draft. |
| `corrections/` | Plural domain-scoped correction lane. | Exists; overlap with singular lane remains unresolved. |
| `correction_notices/` | Correction communication records. | Notice prose must point to governed correction and decision records. |
| `rollback/` | Rollback review records. | Parent and domain sublanes exist; no operational rollback is thereby proven. |
| `rollback_cards/` | Compact rollback/release review cards. | Parent and domain sublanes exist; root JSON records remain proposed placeholders under current workflow checks. |
| `withdrawal_notices/` | Withdrawal communication records. | Parent index exists; notice is not the withdrawal decision. |
| `signatures/` | Signature and signoff packets. | Parent index and at least one child packet exist; signoff is not publication by itself. |
| `agriculture/` | Agriculture release-governance router. | Existing domain index; explicitly not a parallel release-record home. |
| `people-dna-land/` | Sensitive-domain dated release review material. | A dated child README exists; parent-lane completeness and policy/review posture need verification. |

The lane map is descriptive. It does not authorize a new record, approve a release, or settle naming and responsibility conflicts.

[Back to top](#top)

---

<a id="lifecycle-boundary"></a>
<a id="root-responsibilities"></a>

## Lifecycle and authority boundary

```text
candidate / review inputs
  -> evidence + validation + policy + accountable review
  -> decision / manifest / correction / withdrawal / rollback support
  -> governed release state
  -> public-safe artifact under data/published/
```

The release root owns the governance transition, not the data payload.

| Responsibility | Required boundary |
|---|---|
| Identity | Stable IDs and subject pointers; do not rely on filenames alone. |
| Evidence | Link evidence support where release claims depend on it. |
| Validation | Link applicable validation and integrity results. |
| Policy | Record rights, sensitivity, access, stale-state, and public-safety posture. |
| Review | Identify accountable review and unresolved separation-of-duties needs. |
| Decision | Use finite, reasoned outcomes; no approval by implication. |
| Manifest | Bind release scope, included records, previous state, correction path, and rollback target. |
| Correction | Preserve forward correction, supersession, withdrawal, and public notice as required. |
| Rollback | Name a valid prior target and invalidation/cache consequences before release. |
| Publication | Keep the released payload and its governed metadata in the correct published-data lane. |

[Back to top](#top)

---

## Workflow readiness boundaries

### `release-dry-run`

**Current bounded result:** the workflow inspects whether a candidate could be assembled, exercises the selected `PromotionDecision` shape fixture, and checks rollback-card readiness without writing a candidate or release record.

Current explicit holds include:

- no candidate packet payload under `release/candidates/`;
- `tools/release/release_dry_run.py` remains comment-only;
- the Make target remains a TODO marker;
- `ReleaseManifest` remains a permissive proposed id-only schema;
- its declared fixtures and validator are absent.

### `promotion-gate`

**Current bounded result:** the workflow proves missing doctrine artifacts fail closed, validates proposed descriptor and promotion-decision shapes, and exposes missing review and promotion implementation.

Current explicit holds include:

- the doctrine prerequisite remains intentionally unsatisfied until required artifacts are admitted;
- no release review record is present;
- generic promotion and review validators remain placeholders;
- the hydrology smoke promoter is not executed;
- its referenced evidence bundle and rollback card are unresolved;
- no promotion policy execution or accountable review decision is emitted.

### `rollback-drill`

**Current bounded result:** the workflow inspects rollback placeholders, proposed schemas, placeholder card records, and published-alias absence without mutating release state.

Current explicit holds include:

- rollback pipeline and apply helpers remain comment-only;
- direct rollback-drill tests contain guidance only;
- release and agriculture rollback-card schemas remain permissive proposed id-only shapes;
- declared fixtures and validators are absent;
- root rollback-card JSON records remain non-conforming placeholders;
- published-alias auditing remains comment-only;
- no current alias or rollback receipt is behaviorally verified.

> [!IMPORTANT]
> These workflows are useful because they keep missing release machinery visible and fail on drift. They must not be described as operational release, promotion, or rollback execution.

[Back to top](#top)

---

<a id="release-state-model"></a>

## Release state model

Use finite states and preserve the distinction between record state and public artifact state.

| State | Meaning |
|---|---|
| `DRAFT` | Record exists but is not ready for accountable review. |
| `READY_FOR_REVIEW` | Required review inputs appear complete enough for review. |
| `HELD` | Evidence, validation, policy, rights, sensitivity, review, correction, or rollback support is unresolved. |
| `READY_FOR_MANIFEST` | A reviewed candidate may support manifest preparation; it is not yet released. |
| `APPROVED` | A governed decision approves the named scope; publication still depends on the complete release path. |
| `RELEASED` | Governed release state is complete for the named target and public scope. |
| `CORRECTED` | A governed correction changes or replaces prior release state. |
| `SUPERSEDED` | A newer governed state replaces the prior state while preserving lineage. |
| `WITHDRAWN` | The release-facing state is withdrawn through governed process. |
| `NO_ACTION` | Review authorizes no release-state change. |

Recommended decision outcomes remain lane-specific. Do not silently map `APPROVE`, `PROMOTE_TO_MANIFEST`, `READY_FOR_DECISION`, `ROLLBACK_REQUIRED`, or `NO_ACTION` to one another without an accepted contract.

[Back to top](#top)

---

<a id="required-release-root-record-fields"></a>

## Release record minimum contract

A release-governance record should include the fields appropriate to its lane and, at minimum:

- stable record ID;
- record type and schema/contract version when applicable;
- record status and finite outcome;
- subject or affected-record pointer;
- domain, layer, artifact, geography, time, and public-scope boundaries as applicable;
- candidate, manifest, decision, release, correction, notice, changelog, or artifact pointer;
- evidence pointer when claims depend on evidence;
- validation and integrity pointer when applicable;
- policy review or decision pointer when applicable;
- accountable reviewer/decider identity and review state;
- manifest pointer when a release target is prepared or changed;
- correction, withdrawal, supersession, or notice pointer when applicable;
- rollback target and invalidation/cache posture when release state may change;
- release-facing effect;
- date recorded and recorded-by identity;
- follow-up items and unresolved holds.

A record missing support must hold, abstain, deny, or error rather than imply completion.

[Back to top](#top)

---

<a id="minimal-release-root-record"></a>

## Minimal release-root record

```markdown
# <stable-release-record-id>

## Record type
CANDIDATE / REVIEW / PROMOTION_DECISION / MANIFEST / DECISION / POLICY_REVIEW /
CORRECTION / CORRECTION_NOTICE / WITHDRAWAL_NOTICE / ROLLBACK_REVIEW /
ROLLBACK_CARD / SIGNATURE_PACKET / CHANGELOG / NO_ACTION

## Status and outcome
- Status: DRAFT / READY_FOR_REVIEW / HELD / READY_FOR_MANIFEST / APPROVED /
  RELEASED / CORRECTED / SUPERSEDED / WITHDRAWN / NO_ACTION
- Outcome: <finite lane-specific outcome>
- Reason codes: <one or more stable reason codes>

## Scope
<domain, layer, artifact family, geography, time slice, release target, and public scope>

## Subject
<candidate, manifest, decision, release, correction, notice, changelog, or artifact pointer>

## Governed support
- Evidence: <EvidenceRef/EvidenceBundle pointer or N/A with reason>
- Validation: <validation/integrity pointer or N/A with reason>
- Policy: <PolicyDecision/review pointer or N/A with reason>
- Review: <review record and accountable reviewer>
- Manifest: <manifest pointer or N/A>
- Correction/withdrawal/supersession: <pointer or N/A>
- Rollback target: <stable prior target or N/A with reason>
- Changelog/notice: <pointer or N/A>

## Release-facing effect
<none / held / ready for manifest / released / corrected / withdrawn / superseded>

## Date and actor
- Recorded at: <ISO-8601>
- Recorded by: <verified actor identity>

## Follow-up
<open items or none>
```

The template is guidance. An accepted semantic contract and machine schema outrank it.

[Back to top](#top)

---

<a id="review-checklist"></a>

## Review checklist

Before treating a release-facing transition as complete:

- [ ] The record is in the correct release lane.
- [ ] Stable identity, subject, scope, and time are explicit.
- [ ] Evidence resolves where claims depend on evidence.
- [ ] Validation and integrity support are linked.
- [ ] Rights, sensitivity, access, stale-state, and public-safety posture are resolved.
- [ ] Accountable review and decision state are explicit.
- [ ] The outcome is finite and carries reason codes.
- [ ] The manifest names included records, prior state, and release-facing effect.
- [ ] Correction, withdrawal, supersession, notice, and changelog pointers are present when applicable.
- [ ] A valid rollback target and invalidation/cache plan exist when public state may change.
- [ ] No payload, receipt, proof, source, schema, contract, policy, validator, or application authority is duplicated under `release/`.
- [ ] No generated text, map, tile, workflow result, pull request, merge, or signature packet is used as approval by itself.
- [ ] Sensitive or restricted material is not exposed in the release record.
- [ ] The reviewed diff is bounded and a corrective/revert path is documented.

[Back to top](#top)

---

<a id="naming-guidance"></a>

## Naming guidance

Prefer stable IDs and readable filenames. A useful human-facing pattern is:

```text
<YYYY-MM-DD>_<scope>_<record-type>.md
```

Examples:

```text
2026-07-23_hydrology-watershed_release-review.md
2026-07-23_fauna-public-range_correction-notice.md
2026-07-23_agriculture-county-panel_rollback-card.md
```

Guidance:

- use lowercase filenames and hyphenated human-readable scope;
- keep stable IDs inside the record so identity does not depend on the filename;
- do not rename approved records without migration and lineage notes;
- do not create a new lane merely to obtain a preferred naming style;
- preserve current singular/plural paths until an accepted decision resolves them.

[Back to top](#top)

---

## Evidence and no-loss ledger

| Baseline surface | Preservation or upgrade result |
|---|---|
| `kfm://doc/release-readme`, path, and H1 | Preserved. |
| Purpose and release-vs-published distinction | Preserved and strengthened. |
| Status/authority table | Recast into evidence-bounded authority and maturity sections. |
| Placement basis | Preserved through `#placement-basis` and Directory Rules citations. |
| Lifecycle invariant | Preserved through `#lifecycle-boundary`. |
| Repo fit and lane index | Expanded with verified rollback, rollback-card, withdrawal, signature, and domain-router lanes. |
| Root responsibilities | Preserved through `#root-responsibilities` and the authority-boundary matrix. |
| Belongs / does not belong | Preserved and aligned with receipts/proofs/published-data separation. |
| Release state model | Preserved with clearer record-state/public-state limits. |
| Required fields and minimal record | Preserved and expanded with finite outcome, reason codes, review, and rollback support. |
| Review checklist and naming guidance | Preserved under legacy anchors. |
| Open verification | Converted to a current evidence-backed register below. |
| Last reviewed | Updated to the current pinned revision. |
| Release implementation gap | Made explicit; documentation does not claim to satisfy it. |

[Back to top](#top)

---

<a id="open-verification"></a>

## Open verification register

1. **Stewardship and enforcement:** approved release, data, policy, correction, rollback, and domain stewards; branch rules; required checks; independent review.
2. **Manifest semantics:** accepted relationship between `manifest/` and `manifests/`.
3. **Correction semantics:** accepted relationship between `correction/` and `corrections/`.
4. **Rollback semantics:** accepted relationship among `rollback/`, `correction/rollback/`, `rollback_cards/`, and any future execution lane.
5. **Decision semantics:** accepted relationship among `reviews/`, `decisions/`, and `promotion_decisions/`.
6. **Release record identity:** stable ID and filename conventions.
7. **Accepted schemas:** non-permissive `ReleaseManifest`, `RollbackCard`, review, correction, withdrawal, signature, and changelog profiles.
8. **Fixtures and validators:** non-empty valid/invalid fixtures and validators for each state-changing record family.
9. **Policy execution:** accepted policy bundle, inputs, finite outcomes, reason codes, and negative tests.
10. **Evidence closure:** operational `EvidenceRef -> EvidenceBundle` validation for release claims.
11. **Candidate assembly:** deterministic, no-write candidate packet assembly and identity.
12. **Accountable review:** real review records, subject binding, reviewer authority, and separation of duties.
13. **Promotion execution:** policy-aware evaluation that does not self-approve or publish.
14. **Rollback execution:** target selection, signature/review validation, invalidation, receipts, and no-write simulation.
15. **Published aliases:** accepted alias/pointer mechanism and behavioral verification.
16. **Signatures:** accepted signing/attestation profile, key management, verification, and revocation.
17. **Corrections and notices:** public-effect, cache, catalog, API, map, and citation invalidation behavior.
18. **Artifacts compatibility:** `OPEN-DR-09-b` and `artifacts/perf/` placement.
19. **Production parity:** deployed release path, registry, logs, dashboards, retention, and recovery evidence.
20. **Human adoption:** review and acceptance of this README modernization.

[Back to top](#top)

---

## Maintenance, correction, and rollback

### Documentation correction

When this README becomes stale or wrong:

1. pin the current repository revision and read the complete file;
2. identify the exact claim, lane, workflow, or link that drifted;
3. update the smallest sound section while preserving identity and legacy anchors;
4. validate the full Markdown and connected release-document neighborhood;
5. add or update provenance as required;
6. use a focused review branch and reviewed correction.

### Before merge

Close the review pull request and delete or abandon its branch. No shared history rewrite is required.

### After merge

Use a reviewed revert or corrective documentation/provenance pull request. Reverting this README must not be described as rolling back a release, candidate, published artifact, schema, policy, workflow, or runtime state.

### Operational release correction

Operational correction, withdrawal, supersession, rollback, and invalidation require governed records in their accepted lanes. A documentation revert is not an operational rollback.

[Back to top](#top)

---

## Changelog

| Version | Date | Change |
|---|---|---|
| v1 | 2026-07-03 | Expanded the compact root stub into release-governance guidance. |
| v2.0 | 2026-07-23 | Reordered the root contract to Directory Rules §15; refreshed current repository evidence; added missing lane coverage; exposed workflow holds, Makefile readiness markers, CODEOWNERS limits, no-loss ledger, open verification, and explicit documentation-vs-release rollback boundaries. |

[Back to top](#top)

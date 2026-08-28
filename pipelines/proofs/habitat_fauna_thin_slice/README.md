<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-proofs-habitat-fauna-thin-slice-readme
title: Habitat × Fauna Thin Slice Proof Pipeline README
type: readme
version: v0.2
status: draft
owners:
  - <proof-pipeline-owner>
  - <habitat-domain-steward>
  - <fauna-domain-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-07-21
policy_label: public-with-sensitive-ecology-proof-and-release-gates
path: pipelines/proofs/habitat_fauna_thin_slice/README.md
related:
  - docs/architecture/directory-rules.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-habitat-fauna-thin-slice.md
  - docs/domains/habitat/FILE_SYSTEM_PLAN.md
  - docs/domains/habitat/ARCHITECTURE.md
  - docs/domains/fauna/FILE_SYSTEM_PLAN.md
  - pipelines/domains/habitat/README.md
  - pipelines/domains/fauna/README.md
  - pipelines/domains/habitat/land_cover/README.md
  - pipelines/domains/habitat/ecoregions/README.md
  - fixtures/domains/habitat/habitat_fauna_thin_slice/README.md
  - tests/domains/habitat/test_habitat_fauna_thin_slice.py
  - tests/domains/habitat/thin-slice.habitat-fauna.test/README.md
  - .github/workflows/domain-habitat.yml
  - data/catalog/domain/habitat/
  - data/catalog/domain/fauna/
  - data/triplets/
  - data/proofs/evidence_bundle/
  - data/receipts/pipeline/
  - release/candidates/habitat/
  - release/candidates/fauna/
tags: [kfm, pipelines, proofs, habitat, fauna, thin-slice, evidence-bundle, geoprivacy, policy, release-gate, governance]
notes:
  - "This README defines the proposed contract and placement boundary for a cross-domain proof harness; it does not establish an executable producer."
  - "At main@2eb6ff628a4fd1514667c0155693558a58878cbc, the Habitat test module is a one-line PROPOSED placeholder and the domain-habitat workflow records explicit validation, proof, and release-dry-run holds."
  - "This directory is under pipelines/ because executable proof orchestration, if accepted, is implementation responsibility. It is not the EvidenceBundle store; proof artifacts remain under accepted data/proofs or receipt homes."
  - "The Habitat × Fauna thin slice is a proposed proof-bearing lane, not a new domain root and not a shortcut around Habitat or Fauna ownership."
  - "Habitat owns habitat context and suitability/corridor surfaces; Fauna owns occurrence/taxon/sensitive-fauna truth. A future proof harness must preserve that split."
  - "The repository contains conflicting Directory Rules authority surfaces, and the Habitat × Fauna ADR remains a PROPOSED scaffold; exact long-term placement is NEEDS VERIFICATION."
  - "Concrete executable behavior, fixture payloads, accepted proof-receipt shape, CI execution, release wiring, and public API/map behavior remain PROPOSED or NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat × Fauna Thin Slice Proof Pipeline

> Proposed contract for a cross-domain proof harness that would demonstrate how Habitat context and Fauna evidence can move through a governed thin slice without collapsing source roles, exposing sensitive fauna material, bypassing EvidenceBundle closure, or letting public clients read internal lifecycle stores.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-habitat%20%C3%97%20fauna%20thin%20slice-2e7d32)
![authority](https://img.shields.io/badge/authority-proof%20harness%20only-0a7ea4)
![sensitivity](https://img.shields.io/badge/sensitive%20ecology-fail%20closed-d62728)
![publication](https://img.shields.io/badge/publication-no%20direct%20publish-d62728)

**Status:** Draft  
**Path:** `pipelines/proofs/habitat_fauna_thin_slice/README.md`  
**Responsibility root:** `pipelines/` — proposed executable pipeline/proof orchestration  
**Cross-domain lane:** Habitat × Fauna  
**Sublane:** Thin-slice proof contract / proposed governed integration harness  
**Evidence snapshot:** `bartytime4life/Kansas-Frontier-Matrix` at `main@2eb6ff628a4fd1514667c0155693558a58878cbc`  
**Implementation state:** `CONFIRMED` documentation and readiness holds · `PROPOSED` executable proof producer · no accepted proof command or emitted proof inventory established  
**Placement posture:** existing cross-domain sublane under `pipelines/proofs/`; long-term placement is `PROPOSED / CONFLICTED / NEEDS VERIFICATION` because the lane ADR is a scaffold and Directory Rules authority is duplicated  
**Public posture:** no direct publication; any future proof outputs remain receipts, reports, fixture results, and release-readiness blockers until evidence, policy, review, release, correction, and rollback gates close.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [Current repository state](#current-repository-state)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Proof anti-collapse rules](#3-proof-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Thin-slice scope](#6-thin-slice-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required proof gates](#8-required-proof-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal proof receipt](#11-minimal-proof-receipt)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Promotion, publication, correction, and rollback](#13-promotion-publication-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/proofs/habitat_fauna_thin_slice/` documents the boundary and graduation contract for a proposed Habitat × Fauna integration proof harness. The README is implementation guidance; it is not evidence that a runner, fixture payload set, proof receipt, or passing CI job exists.

If implemented and accepted, the harness should prove with public-safe fixtures before live data that KFM can:

- read released or fixture-scoped Habitat context and Fauna evidence without merging the two domain authorities;
- join habitat patches, land-cover/ecoregion context, and fauna occurrence/range/suitability inputs through governed cross-lane relations;
- preserve Fauna ownership of taxon, occurrence, sensitive-fauna, nest/den/roost/hibernacula/spawning, and steward-controlled records;
- preserve Habitat ownership of habitat patches, habitat classes, ecological systems, suitability surfaces, connectivity/corridors, model receipts, and uncertainty surfaces;
- produce proof receipts that show no public client reads RAW, WORK, QUARANTINE, restricted lifecycle stores, direct source APIs, graph internals, or direct model output;
- prove EvidenceBundle, policy, geoprivacy, release, correction, and rollback preconditions before any public-facing artifact can be considered.

A future implementation in this directory would own only the **how** of proof orchestration. This directory does not own Habitat doctrine, Fauna doctrine, source descriptors, schemas, contracts, policy, EvidenceBundle truth, catalog truth, release decisions, or public API/map behavior.

[⬆ Back to top](#top)

---

## Current repository state

The following boundary is confirmed only for the pinned evidence snapshot above.

| Surface | Repository evidence | Truth status |
|---|---|---|
| This lane | This README exists and defines the proposed proof boundary. | CONFIRMED documentation |
| Executable test module | `tests/domains/habitat/test_habitat_fauna_thin_slice.py` contains only a PROPOSED placeholder string and no test function or class. | CONFIRMED placeholder |
| Test-lane documentation | `tests/domains/habitat/thin-slice.habitat-fauna.test/README.md` is a draft, placeholder-expanded contract and marks executable tests, fixtures, proof behavior, CI coverage, and pass rates as needing verification. | CONFIRMED documentation / PROPOSED execution |
| Fixture lane | `fixtures/domains/habitat/habitat_fauna_thin_slice/README.md` documents synthetic public-safe fixtures but reports no verified payload inventory and no tests or validators run. | CONFIRMED documentation / payloads NEEDS VERIFICATION |
| Habitat CI | `.github/workflows/domain-habitat.yml` runs repository-readiness checks with read-only contents permission. Its validation, proof, and release-dry-run jobs emit explicit `WORKFLOW_HOLD` outcomes and state that no accepted producer or command exists. | CONFIRMED workflow definition / execution result NEEDS VERIFICATION |
| Lane ADR | `docs/adr/ADR-habitat-fauna-thin-slice.md` is a 17-line PROPOSED scaffold and is not an accepted placement or behavior decision. | CONFIRMED scaffold / decision PROPOSED |
| Directory Rules | `CONTRIBUTING.md` directs live preflight to `docs/architecture/directory-rules.md` and records a same-`doc_id` conflict with `docs/architecture/DIRECTORY_RULES.md`; the newer artifact also leaves its canonical home open. | CONFIRMED conflict / resolution NEEDS VERIFICATION |
| Proof receipts and release state | No accepted thin-slice proof-receipt schema, emitted proof inventory, or release decision was established by the bounded inspection. | NEEDS VERIFICATION |

> [!IMPORTANT]
> A green Habitat readiness workflow currently means the documented holds still apply. It does not mean the thin slice executed, produced an EvidenceBundle or proof receipt, passed sensitive-fauna review, or became release-ready.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | The responsibility is proposed executable orchestration rather than doctrine or lifecycle data. | CONFIRMED responsibility rule / implementation PROPOSED |
| Why `proofs/` under `pipelines/`? | The existing parent and target READMEs treat this as a proof-orchestration sublane; emitted proof or receipt artifacts must remain in their accepted data homes. | CONFIRMED existing placement / long-term placement NEEDS VERIFICATION |
| Why not `pipelines/domains/habitat/`? | The proposed harness spans Habitat and Fauna; choosing Habitat as the authority owner would collapse the Fauna boundary. | CONFIRMED domain-boundary rule |
| Why not `pipelines/domains/fauna/`? | The proposed harness also verifies Habitat context and join behavior; choosing Fauna as the authority owner would collapse the Habitat boundary. | CONFIRMED domain-boundary rule |
| Does this create a new domain root? | No. The existing path is a sublane under an implementation root. | CONFIRMED repository path |
| Is placement accepted? | No accepted lane ADR was established; the named ADR is a scaffold and Directory Rules authority remains conflicted. | PROPOSED / CONFLICTED / NEEDS VERIFICATION |
| Can this publish? | No. A future harness may emit review inputs and blockers only; publication remains separately governed. | CONFIRMED governance rule / no current producer |

> [!IMPORTANT]
> Passing this proof means the thin-slice invariants were demonstrated for the scoped fixtures and implementation. It is not a release decision, not an EvidenceBundle by itself, and not proof that live Habitat or Fauna pipelines are complete.

[⬆ Back to top](#top)

---

## 3. Proof anti-collapse rules

Disallowed collapses:

```text
proof pass -> release approval
proof receipt -> EvidenceBundle
fixture result -> live-data truth
Habitat context -> Fauna occurrence truth
Fauna occurrence -> Habitat object
suitability model -> observed occurrence
candidate corridor -> regulatory habitat authority
public-safe derivative -> unrestricted source geometry
redaction/generalization check -> release decision
graph projection -> canonical truth
generated proof summary -> evidence
pipeline run -> ReleaseManifest
```

Required distinctions:

- proof harness, fixture, RunReceipt, ValidationReport, EvidenceBundle, PolicyDecision, ReviewRecord, catalog record, graph/triplet projection, ReleaseManifest, CorrectionNotice, RollbackCard, and public artifact remain separate;
- Habitat and Fauna object families retain their owning domain lanes;
- sensitive fauna and steward-controlled inputs fail closed unless public-safe derivatives, receipts, review, and policy allow them;
- model, candidate, observation, range, occurrence, and public representation labels remain visible;
- every claim resolves EvidenceBundle support or abstains.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable proof orchestration for the Habitat × Fauna thin slice.

Appropriate contents include:

- fixture-only proof runners;
- no-network integration smoke tests;
- proof-plan adapters that call Habitat and Fauna fixture outputs by stable refs;
- source-role, domain-boundary, and object-family invariant checks;
- sensitive-fauna and public-safe derivative checks;
- EvidenceBundle resolution checks;
- catalog/triplet handoff checks;
- release-blocker checks;
- public-client trust-membrane checks;
- proof receipts and proof-summary builders, if they write to accepted receipt/proof homes;
- rollback/correction readiness checks for released derivatives.

A good placement test:

> If the code proves the cross-domain thin slice without owning either domain's truth, it may belong here. If it implements Habitat domain processing, Fauna domain processing, source fetching, schema definition, policy decisions, catalog truth, release decisions, or public serving, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Habitat domain pipeline logic | `pipelines/domains/habitat/` |
| Fauna domain pipeline logic | `pipelines/domains/fauna/` |
| Source fetchers and API clients | `connectors/<source_id>/` or accepted connector home |
| Source descriptors | `data/registry/sources/<domain>/` or accepted registry home |
| Domain doctrine | `docs/domains/habitat/`, `docs/domains/fauna/`, cross-domain ADR/docs |
| Schemas | `schemas/contracts/v1/...` accepted schema home |
| Contracts / meaning | `contracts/domains/habitat/`, `contracts/domains/fauna/` |
| Policy | `policy/domains/...`, `policy/sensitivity/...` |
| Fixtures | Existing documented lane: `fixtures/domains/habitat/habitat_fauna_thin_slice/`; payload inventory and final cross-domain placement remain NEEDS VERIFICATION. |
| Tests | Existing documented lanes: `tests/domains/habitat/test_habitat_fauna_thin_slice.py` and `tests/domains/habitat/thin-slice.habitat-fauna.test/`; both remain placeholder-level and final cross-domain placement is NEEDS VERIFICATION. |
| EvidenceBundles | `data/proofs/evidence_bundle/` or accepted proof data home |
| Lifecycle records | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` |
| Release decisions | `release/...` |
| Public API/UI code | `apps/governed-api/`, `apps/explorer-web/`, packages |

[⬆ Back to top](#top)

---

## 6. Thin-slice scope

| Scope area | Proof-harness responsibility | Failure behavior |
|---|---|---|
| Domain ownership | Verify Habitat and Fauna ownership boundaries are preserved. | Fail proof. |
| Source role | Verify observation/model/context/authority roles are not collapsed. | Fail proof. |
| Sensitive fauna | Verify restricted inputs do not reach public artifacts or public fixtures. | Deny/hold proof. |
| Habitat context | Verify habitat patches/classes/suitability remain Habitat records. | Fail proof. |
| Fauna context | Verify taxon/occurrence/status/range remain Fauna records. | Fail proof. |
| Evidence | Resolve EvidenceRef to EvidenceBundle where claims are made. | Hold/abstain. |
| Catalog/triplet | Verify catalog and graph projections are downstream carriers, not root truth. | Fail proof. |
| Release readiness | Emit blockers instead of publishing. | No public edge. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

The proof must exercise, but not bypass, the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** fixture or release-approved Habitat and Fauna inputs only.
2. **Verify** source descriptors, source roles, object-family boundaries, sensitivity posture, EvidenceBundle refs, policy refs, and receipts.
3. **Run** thin-slice join checks through public-safe or fixture-safe representations.
4. **Emit** proof receipts, invariant results, release-readiness blockers, and correction/rollback expectations.
5. **Hold** proof if evidence, policy, sensitivity, review, catalog, release, or rollback prerequisites are missing.
6. **Never publish, create release decisions, or expose internal lifecycle stores.**

[⬆ Back to top](#top)

---

## 8. Required proof gates

Every proof run must check or explicitly fail closed on:

1. **Fixture/no-network gate** — default execution uses synthetic or public-safe fixtures and performs no network calls.
2. **Domain-boundary gate** — Habitat and Fauna object ownership remains distinct.
3. **SourceDescriptor gate** — input refs have source identity, role, rights, and citation metadata.
4. **Sensitive-fauna gate** — restricted or re-derivable sensitive occurrence material does not enter public outputs or public examples.
5. **Public-safe representation gate** — released derivatives use reviewed/generalized/redacted forms with receipts where required.
6. **EvidenceBundle gate** — all claim-bearing outputs resolve EvidenceBundle refs or abstain.
7. **Policy/review gate** — finite policy and review outcomes exist where sensitivity or materiality requires them.
8. **Catalog/triplet gate** — graph and catalog outputs carry provenance and do not become root truth.
9. **Release-blocker gate** — missing rollback target, correction path, policy, review, or evidence becomes an explicit blocker.
10. **Trust-membrane gate** — public clients would read only governed APIs or released artifacts.
11. **No-direct-publish gate** — the proof runner never writes public layers, release manifests, or API/UI state as a side effect.

[⬆ Back to top](#top)

---

## 9. Directory contract

At the pinned snapshot, this README is the only lane artifact established by the bounded inspection. The Habitat workflow separately states that no accepted Habitat proof producer or deterministic proof command exists.

The following shape is illustrative and entirely **PROPOSED**. Do not add these paths until the lane ADR, executable ownership, test placement, receipt schema, and validation command are accepted:

```text
pipelines/proofs/habitat_fauna_thin_slice/
├── README.md                         # CONFIRMED: this boundary document
├── PROOF_CONTRACT.md                 # PROPOSED
├── run_dry_fixture.py                # PROPOSED no-network fixture proof
├── check_domain_boundaries.py        # PROPOSED
├── check_sensitive_fauna_gate.py     # PROPOSED
├── check_evidence_refs.py            # PROPOSED
├── check_catalog_triplets.py         # PROPOSED
├── check_release_blockers.py         # PROPOSED
├── emit_proof_receipt.py             # PROPOSED; only if not shared
└── adapters/                         # PROPOSED thin refs; no domain ownership
```

A declarative spec location is also **PROPOSED / NEEDS VERIFICATION**:

```text
pipeline_specs/proofs/habitat_fauna_thin_slice.yaml
```

Generated proof outputs must never be written beside executable code. Exact output paths remain subject to accepted schemas, ADRs, and receipt/proof ownership; no path listed here authorizes a parallel proof, receipt, release, catalog, or publication home.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Proof fixture | `fixtures/domains/habitat/habitat_fauna_thin_slice/` currently documents the lane; final cross-domain fixture placement remains NEEDS VERIFICATION. | Synthetic/public-safe only; no verified payload inventory at the pinned snapshot. |
| Habitat input | `data/processed/habitat/` or `data/catalog/domain/habitat/` | Stable refs only. |
| Fauna input | `data/processed/fauna/` or `data/catalog/domain/fauna/` | Restricted material must not be public-facing. |
| Evidence proof | `data/proofs/evidence_bundle/` | Required for claim-bearing outputs. |
| Proof receipt | Accepted receipt home and schema are NEEDS VERIFICATION. | Must record refs, gates, outcomes, and blockers without becoming an EvidenceBundle or release decision. |
| Triplet proof | `data/triplets/` or accepted graph-delta home | Provenance-bound carrier only. |
| Release blocker | `release/candidates/...` or accepted release-candidate home | Handoff only; no release decision. |

[⬆ Back to top](#top)

---

## 11. Minimal proof receipt

The final schema and storage path are not accepted here. This non-executable example shows the minimum information a future thin-slice receipt should preserve; it is not an emitted receipt, schema authority, EvidenceBundle, PolicyDecision, ReviewRecord, or release decision.

```yaml
schema_version: kfm.proof.habitat_fauna_thin_slice.v1
proof_run_id: habitat_fauna_thin_slice_run_YYYYMMDDThhmmssZ
pipeline_id: proofs.habitat_fauna_thin_slice
status: HELD
inputs:
  habitat_refs: []
  fauna_refs: []
  evidence_bundle_refs: []
  policy_decision_refs: []
  review_record_refs: []
checks:
  no_network: true
  domain_boundaries_preserved: false
  source_roles_preserved: false
  sensitive_fauna_public_safe: false
  evidence_resolved: false
  catalog_triplet_provenance_ready: false
  release_blockers_emitted: false
  trust_membrane_preserved: false
anti_collapse:
  proof_receipt_is_evidence_bundle: false
  habitat_context_is_fauna_truth: false
  fauna_occurrence_is_habitat_truth: false
  suitability_model_is_observation: false
  proof_run_is_release_decision: false
outputs:
  proof_receipt_ref: data/receipts/pipeline/proofs/habitat_fauna_thin_slice/run_YYYYMMDDThhmmssZ.yml
  release_blocker_refs: []
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

The default future execution posture is **fixture-only, synthetic/public-safe, and no-network** until fixtures, proof specs, receipt shapes, policy fixtures, and CI wiring are accepted.

Current repository evidence does not establish an executable test:

- `tests/domains/habitat/test_habitat_fauna_thin_slice.py` is a one-line placeholder with no test function or class;
- `tests/domains/habitat/thin-slice.habitat-fauna.test/README.md` documents the intended invariant but explicitly leaves executable coverage and pass rates unverified;
- the documented fixture lane reports no verified payload inventory; and
- `domain-habitat` CI deliberately holds instead of running a proof producer.

Exact test placement is **CONFLICTED / NEEDS VERIFICATION**: current test scaffolds are Habitat-scoped, while cross-domain placement doctrine favors a non-domain segment under the owning responsibility root. Resolve that placement before creating another test tree.

A future accepted suite must cover:

- no-network deterministic execution and non-empty fixture collection;
- Habitat/Fauna ownership and source-role preservation;
- sensitive-fauna denial and public-safe generalization;
- EvidenceRef-to-EvidenceBundle resolution or explicit abstention;
- catalog/triplet provenance without authority collapse;
- explicit release blockers, correction lineage, and rollback targets;
- deterministic receipt hashes; and
- denial of direct writes to public UI, public API state, published layers, or release manifests.

A dry run may prove only that those guardrails behaved as expected for the pinned fixtures and implementation. It does not prove live-data truth, full source coverage, release approval, public safety outside the tested cases, or publication readiness.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

A future accepted proof harness may prepare proof receipts, invariant reports, graph-projection checks, and release-readiness blockers. No such producer or emitted inventory is established by the pinned evidence, and this lane never publishes.

Proposed chain:

```text
fixture / processed / catalog Habitat refs
  + fixture / processed / catalog Fauna refs
  -> proof harness checks
  -> proof receipt + blockers
  -> domain steward review
  -> release candidate, if appropriate
  -> ReleaseManifest
  -> RollbackCard
  -> public-safe artifact
```

Correction and rollback posture:

- failed proof runs remain auditable;
- proof receipts preserve input refs, evidence refs, policy refs, review refs, object-boundary checks, and failure reasons;
- proof outputs are superseded by governed state transitions, not hidden overwrite;
- downstream artifacts are invalidated if Habitat refs, Fauna refs, EvidenceBundle refs, policy refs, review refs, sensitivity transforms, correction refs, or rollback refs drift;
- rollback is owned by `release/`, not by this proof directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

### Documentation boundary

This README is complete for review when it:

- identifies the path as the proposed cross-domain proof-orchestration boundary under `pipelines/` without claiming an executable producer exists;
- records the pinned placeholder, fixture, ADR, workflow-hold, and Directory Rules evidence;
- prevents Habitat logic, Fauna logic, schemas, policy, source descriptors, lifecycle data, EvidenceBundles, release decisions, public API, and UI authority from being placed here;
- preserves ownership, source roles, EvidenceBundle refs, policy refs, sensitive-fauna gates, catalog/triplet provenance, release blockers, correction paths, and rollback boundaries; and
- keeps proposed paths, schemas, commands, receipts, and public behavior visibly unimplemented.

### Executable graduation

Executable work is ready only when:

- the Habitat × Fauna ADR or equivalent accepted decision resolves ownership and placement;
- synthetic public-safe fixture payloads and invalid/denied cases are reviewed;
- a deterministic no-network runner and substantive tests exist;
- an accepted proof-receipt schema and storage home exist;
- domain-boundary, source-role, sensitive-fauna, EvidenceBundle, provenance, blocker, direct-publication-denial, correction, and rollback checks pass;
- CI invokes the accepted command instead of the current explicit hold;
- the resulting receipts and remote checks are read back and reviewed; and
- human governance review remains separate from generation, test success, release, and publication.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `HF-PROOF-001` | Is the existing `pipelines/proofs/` placement final, given the proposed lane ADR and conflicting Directory Rules authority surfaces? | CONFLICTED / NEEDS VERIFICATION / ADR |
| `HF-PROOF-002` | Which accepted schema and canonical receipt home own thin-slice proof receipts and invariant reports? | NEEDS VERIFICATION |
| `HF-PROOF-003` | Which payloads populate the documented Habitat × Fauna fixture lane, including valid, invalid, denied, held, and abstained cases? | NEEDS VERIFICATION |
| `HF-PROOF-004` | Which accepted CI job and repository-native command replace the current `domain-habitat` proof hold? | NEEDS VERIFICATION |
| `HF-PROOF-005` | Which release candidate, if any, may consume this proof's blockers without turning proof success into release approval? | NEEDS VERIFICATION |
| `HF-PROOF-006` | Should a later reviewed scope include Flora-sensitive joins, or remain Habitat × Fauna only? | NEEDS VERIFICATION |
| `HF-PROOF-007` | What minimum evidence, policy, sensitivity, review, correction, and rollback closure is required before a public map layer may demonstrate this slice? | NEEDS VERIFICATION |
| `HF-PROOF-008` | Should executable tests remain under the current Habitat-scoped paths or move to a non-domain cross-domain test segment? | CONFLICTED / NEEDS VERIFICATION |
| `HF-PROOF-009` | Which generated-work receipt and proof-receipt validators are required before CI graduation? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic/public-safe fixtures and negative tests. The current Habitat workflow intentionally holds and is designed to fail when an executable test, validator, proof producer, or release command surfaces without deliberate graduation; update the runner, tests, fixtures, workflow, and documentation coherently when that happens. Do not add live source fetching, Habitat/Fauna authority, schema or policy authority, release decisions, public API/UI code, release-manifest writes, published-layer writes, or generated ecology summaries until domain boundaries, source roles, sensitive-fauna controls, EvidenceBundle refs, policy decisions, review state, catalog/triplet provenance, deterministic receipts, correction paths, and rollback expectations are proven.

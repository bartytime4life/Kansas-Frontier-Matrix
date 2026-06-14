<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-proofs-habitat-fauna-thin-slice-readme
title: Habitat × Fauna Thin Slice Proof Pipeline README
type: readme
version: v0.1
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
updated: 2026-06-13
policy_label: public-with-sensitive-ecology-proof-and-release-gates
path: pipelines/proofs/habitat_fauna_thin_slice/README.md
related:
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-habitat-fauna-thin-slice.md
  - docs/domains/habitat/FILE_SYSTEM_PLAN.md
  - docs/domains/habitat/ARCHITECTURE.md
  - docs/domains/fauna/FILE_SYSTEM_PLAN.md
  - pipelines/domains/habitat/README.md
  - pipelines/domains/fauna/README.md
  - pipelines/domains/habitat/land_cover/README.md
  - pipelines/domains/habitat/ecoregions/README.md
  - data/catalog/domain/habitat/
  - data/catalog/domain/fauna/
  - data/triplets/
  - data/proofs/evidence_bundle/
  - data/receipts/pipeline/
  - release/candidates/habitat/
  - release/candidates/fauna/
tags: [kfm, pipelines, proofs, habitat, fauna, thin-slice, evidence-bundle, geoprivacy, policy, release-gate, governance]
notes:
  - "This README fills the blank pipelines/proofs/habitat_fauna_thin_slice path as a cross-domain executable proof-harness lane."
  - "This directory is under pipelines/ because it describes executable proof orchestration. It is not the EvidenceBundle store; proof artifacts remain under data/proofs/evidence_bundle or accepted proof homes."
  - "The Habitat × Fauna thin slice is a proof-bearing lane, not a new domain root and not a shortcut around Habitat or Fauna ownership."
  - "Habitat owns habitat context and suitability/corridor surfaces; Fauna owns occurrence/taxon/sensitive-fauna truth. The proof harness must preserve that split."
  - "Concrete executable behavior, CI coverage, fixture coverage, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat × Fauna Thin Slice Proof Pipeline

> Cross-domain executable proof harness for demonstrating that Habitat context and Fauna evidence can move through a governed thin slice without collapsing source roles, exposing sensitive fauna material, bypassing EvidenceBundle closure, or letting public clients read internal lifecycle stores.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-habitat%20%C3%97%20fauna%20thin%20slice-2e7d32)
![authority](https://img.shields.io/badge/authority-proof%20harness%20only-0a7ea4)
![sensitivity](https://img.shields.io/badge/sensitive%20ecology-fail%20closed-d62728)
![publication](https://img.shields.io/badge/publication-no%20direct%20publish-d62728)

**Status:** Draft  
**Path:** `pipelines/proofs/habitat_fauna_thin_slice/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline/proof orchestration  
**Cross-domain lane:** Habitat × Fauna  
**Sublane:** Thin-slice proof / governed integration harness  
**Placement posture:** cross-domain executable proof lane under `pipelines/proofs/`; concrete behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests, fixtures, receipts, and CI evidence  
**Public posture:** no direct publication; proof outputs are receipts, reports, fixture results, and release-readiness blockers only until catalog, release, correction, and rollback gates close.

---

## Quick jump

- [1. Purpose](#1-purpose)
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

`pipelines/proofs/habitat_fauna_thin_slice/` is the executable proof-harness lane for the first Habitat × Fauna integration proof.

It should prove, with public-safe fixtures before live data, that KFM can:

- read released or fixture-scoped Habitat context and Fauna evidence without merging the two domain authorities;
- join habitat patches, land-cover/ecoregion context, and fauna occurrence/range/suitability inputs through governed cross-lane relations;
- preserve Fauna ownership of taxon, occurrence, sensitive-fauna, nest/den/roost/hibernacula/spawning, and steward-controlled records;
- preserve Habitat ownership of habitat patches, habitat classes, ecological systems, suitability surfaces, connectivity/corridors, model receipts, and uncertainty surfaces;
- produce proof receipts that show no public client reads RAW, WORK, QUARANTINE, restricted lifecycle stores, direct source APIs, graph internals, or direct model output;
- prove EvidenceBundle, policy, geoprivacy, release, correction, and rollback preconditions before any public-facing artifact can be considered.

This directory implements or will implement the **how** of the proof harness. It does not own Habitat doctrine, Fauna doctrine, source descriptors, schemas, contracts, policy, EvidenceBundle truth, catalog truth, release decisions, or public API/map behavior.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable orchestration / proof-harness logic, not doctrine or lifecycle data. | CONFIRMED root responsibility |
| Why `proofs/` under `pipelines/`? | This is an executable proof runner; emitted proof artifacts belong in `data/proofs/` or receipts, not beside code. | PROPOSED / NEEDS VERIFICATION |
| Why not `pipelines/domains/habitat/`? | This is cross-domain Habitat × Fauna; Habitat does not own Fauna occurrence truth. | CONFIRMED domain-boundary posture |
| Why not `pipelines/domains/fauna/`? | This also verifies Habitat context and join behavior; Fauna does not own Habitat truth. | CONFIRMED domain-boundary posture |
| Does this create a new domain root? | No. It is a proof-harness folder under an implementation root. | CONFIRMED Directory Rules posture |
| Can this publish? | No. It emits proof receipts and release-readiness blockers only. | CONFIRMED governance posture |

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
| Fixtures | `fixtures/proofs/habitat_fauna_thin_slice/` or accepted fixture home |
| Tests | `tests/pipelines/proofs/habitat_fauna_thin_slice/` or accepted test home |
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

Recommended shape:

```text
pipelines/proofs/habitat_fauna_thin_slice/
├── README.md                         # this file
├── PROOF_CONTRACT.md                 # PROPOSED: proof harness contract
├── run_dry_fixture.py                # PROPOSED no-network fixture proof
├── check_domain_boundaries.py        # PROPOSED
├── check_sensitive_fauna_gate.py     # PROPOSED
├── check_evidence_refs.py            # PROPOSED
├── check_catalog_triplets.py         # PROPOSED
├── check_release_blockers.py         # PROPOSED
├── emit_proof_receipt.py             # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin refs to domain outputs, no domain ownership
```

Declarative specs should live outside this directory:

```text
pipeline_specs/proofs/habitat_fauna_thin_slice.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated proof outputs must not be written beside this code. Use accepted lifecycle/proof homes under `data/receipts/pipeline/`, `data/proofs/evidence_bundle/`, `data/catalog/domain/habitat/`, `data/catalog/domain/fauna/`, `data/triplets/`, and `release/candidates/` as governed downstream locations.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Proof fixture | `fixtures/proofs/habitat_fauna_thin_slice/` or accepted fixture home | Synthetic/public-safe only by default. |
| Habitat input | `data/processed/habitat/` or `data/catalog/domain/habitat/` | Stable refs only. |
| Fauna input | `data/processed/fauna/` or `data/catalog/domain/fauna/` | Restricted material must not be public-facing. |
| Evidence proof | `data/proofs/evidence_bundle/` | Required for claim-bearing outputs. |
| Proof receipt | `data/receipts/pipeline/proofs/habitat_fauna_thin_slice/<run_id>.yml` or accepted receipt home | Records refs, gates, outcomes, and blockers. |
| Triplet proof | `data/triplets/` or accepted graph-delta home | Provenance-bound carrier only. |
| Release blocker | `release/candidates/...` or accepted release-candidate home | Handoff only; no release decision. |

[⬆ Back to top](#top)

---

## 11. Minimal proof receipt

The final schema is not defined here. This example shows the minimum information a thin-slice proof receipt should preserve.

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

Default execution is **fixture-only, synthetic/public-safe, and no-network** until domain fixtures, proof specs, evidence fixtures, policy fixtures, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/proofs/habitat_fauna_thin_slice/
├── test_no_network_dry_run.py              # PROPOSED
├── test_domain_boundaries_preserved.py     # PROPOSED
├── test_source_roles_preserved.py          # PROPOSED
├── test_sensitive_fauna_public_safe.py     # PROPOSED
├── test_habitat_context_not_fauna_truth.py # PROPOSED
├── test_fauna_occurrence_not_habitat_truth.py # PROPOSED
├── test_suitability_model_labeled.py       # PROPOSED
├── test_evidence_bundle_required.py        # PROPOSED
├── test_catalog_triplet_provenance.py      # PROPOSED
├── test_release_blockers_emitted.py        # PROPOSED
├── test_no_internal_store_exposure.py      # PROPOSED
├── test_receipt_hashes.py                  # PROPOSED
└── test_no_direct_publish.py               # PROPOSED
```

A dry run should prove fixtures load without network access, Habitat/Fauna boundaries are preserved, sensitive-fauna material does not leak into public-safe outputs, EvidenceBundle refs are required, catalog/triplet projections carry provenance, release blockers are explicit, receipts are deterministic, and no run writes directly to public UI, public API, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

This proof harness may prepare proof receipts, invariant reports, graph-projection checks, and release-readiness blockers. It does not publish.

Required chain:

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

This README is done when it:

- fills the blank `pipelines/proofs/habitat_fauna_thin_slice/README.md` file;
- identifies this directory as a cross-domain executable proof harness under `pipelines/`;
- prevents Habitat domain logic, Fauna domain logic, schemas, policy, source descriptors, lifecycle data, EvidenceBundles, release decisions, public API, and UI authority from being placed here;
- preserves Habitat/Fauna ownership boundaries, source roles, EvidenceBundle refs, policy refs, sensitive-fauna gates, catalog/triplet provenance, release blockers, correction paths, and rollback boundaries;
- blocks proof-pass-as-release, proof-receipt-as-EvidenceBundle, Habitat-context-as-Fauna-truth, Fauna-occurrence-as-Habitat-truth, suitability-model-as-observation, generated-summary-as-evidence, internal-store exposure, and direct publication writes;
- gives maintainers a fixture-first, no-network, receipt-emitting, fail-closed expansion pattern.

Future executable work in this proof lane is done only when it has public-safe fixtures, no-network tests, domain-boundary checks, sensitive-fauna denial tests, EvidenceBundle checks, catalog/triplet provenance tests, release-blocker checks, deterministic receipts, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `HF-PROOF-001` | Is `pipelines/proofs/` the final accepted home for executable proof harnesses, or should this move under `tests/`, `tools/`, or a dedicated `proofs/` implementation root by ADR? | NEEDS VERIFICATION / ADR |
| `HF-PROOF-002` | Which schema owns thin-slice proof receipts and proof invariant reports? | NEEDS VERIFICATION |
| `HF-PROOF-003` | Which Habitat and Fauna fixtures are the first public-safe proof set? | NEEDS VERIFICATION |
| `HF-PROOF-004` | Which CI job owns the Habitat × Fauna thin-slice proof run? | UNKNOWN |
| `HF-PROOF-005` | Which release candidate, if any, should consume this proof's release blockers? | NEEDS VERIFICATION |
| `HF-PROOF-006` | Should the proof include Flora-sensitive joins in a later pass, or remain Habitat × Fauna only? | NEEDS VERIFICATION |
| `HF-PROOF-007` | What minimum proof is required before a public map layer demonstrates this thin slice? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic/public-safe fixtures and negative tests. Do not add live source fetching, Habitat/Fauna domain ownership, source-profile editing, schema authority, policy authority, release-decision authority, public API code, UI code, release-manifest writes, published-layer writes, or generated ecology summaries until domain boundaries, source roles, sensitive-fauna controls, EvidenceBundle refs, policy decisions, review state, catalog/triplet provenance, deterministic receipts, and rollback expectations are proven.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-proofs-readme
title: Pipeline Proofs README
type: readme
version: v0.2
status: draft
owners:
  - <pipeline-owner>
  - <proof-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-07-21
policy_label: public-with-proof-harness-and-release-gates
path: pipelines/proofs/README.md
related:
  - docs/architecture/directory-rules.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - pipelines/README.md
  - pipelines/proofs/habitat_fauna_thin_slice/README.md
  - tests/cross_domain/README.md
  - tests/cross_domain/fauna_habitat/README.md
  - data/proofs/README.md
  - catalog/proof/README.md
  - data/receipts/generated/README.md
  - .github/workflows/domain-habitat.yml
tags: [kfm, pipelines, proofs, proof-harness, evidence-bundle, receipts, no-network, release-blockers, governance]
notes:
  - "This README documents an existing proof-orchestration path and a proposed implementation boundary; the bounded evidence snapshot does not establish an executable proof harness in this subtree."
  - "The pipelines root owns executable transformation and orchestration responsibilities, but final shared-proof placement remains CONFLICTED / NEEDS VERIFICATION."
  - "This path is not the canonical EvidenceBundle store and does not create lifecycle, schema, contract, policy, source, registry, catalog, receipt, release, or publication authority."
  - "Illustrative spec, fixture, test, receipt, and proof-output paths are not placement decisions."
  - "Executable behavior, CI coverage, fixture payloads, proof-receipt schema/home, release wiring, and public behavior remain PROPOSED or NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Pipeline Proofs

> Documentation index and proposed responsibility boundary for future KFM integration-proof orchestration — without claiming that an executable proof producer, accepted proof-receipt contract, CI command, release decision, or public path currently exists here.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-proof%20orchestration%20proposed-f59e0b)
![authority](https://img.shields.io/badge/authority-documentation%20boundary-6b7280)
![evidence](https://img.shields.io/badge/evidence-bundle%20separate-d62728)
![publication](https://img.shields.io/badge/publication-no%20direct%20publish-d62728)

**Status:** Draft  
**Path:** `pipelines/proofs/README.md`  
**Evidence snapshot:** `main@f9c257b8f9ba9479bce69dfa2fd2411b9cdcf566`  
**Responsibility root:** `pipelines/` — executable pipeline logic when implementation exists  
**Current maturity:** parent index plus a documented Habitat × Fauna child lane; no executable producer established by the bounded inspection  
**Placement posture:** existing path; final shared-proof and cross-domain test placement is `CONFLICTED / NEEDS VERIFICATION / ADR`  
**Public posture:** no direct publication; a future proof runner may emit review inputs and blockers only through accepted contracts and homes.

---

## Quick jump

- [0. Current repository state](#0-current-repository-state)
- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Proof anti-collapse rules](#3-proof-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Proof harness inventory](#6-proof-harness-inventory)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal proof run receipt](#11-minimal-proof-run-receipt)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Promotion, publication, correction, and rollback](#13-promotion-publication-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 0. Current repository state

This table records the bounded evidence at `main@f9c257b8f9ba9479bce69dfa2fd2411b9cdcf566`. It describes repository maturity; it does not accept an ADR, certify exhaustive file absence, or promote documentation into executable behavior.

| Surface | Repository evidence | Status |
|---|---|---|
| Parent lane | `pipelines/proofs/README.md` exists as this draft index. | CONFIRMED documentation |
| Child lane | `pipelines/proofs/habitat_fauna_thin_slice/README.md` v0.2 exists and explicitly describes a proposed contract, placeholder tests, workflow holds, and unresolved placement. | CONFIRMED document / executable producer PROPOSED |
| Executable content in this subtree | The bounded path and code searches established the parent and child READMEs but did not establish a runner, invariant checker, adapter, or receipt emitter under `pipelines/proofs/`. | NOT ESTABLISHED / NEEDS VERIFICATION |
| Declarative proof specs | References to `pipeline_specs/proofs/` were found in proof documentation, but no implemented proof spec was established. | PROPOSED / NEEDS VERIFICATION |
| Generic proof fixtures and tests | `fixtures/proofs/` and `tests/pipelines/proofs/` were cited by this README, but the bounded search did not establish those as accepted homes. | PROPOSED / NEEDS VERIFICATION |
| Cross-domain tests | `tests/cross_domain/` and `tests/cross_domain/fauna_habitat/` exist as documentation surfaces that label placement conflicted and executable depth absent or unknown. | CONFIRMED documents / CONFLICTED |
| Habitat proof CI | `.github/workflows/domain-habitat.yml` records explicit validation, proof-producer, and release-dry-run holds. | CONFIRMED hold |
| Proof, receipt, catalog, and release separation | `data/proofs/`, `data/receipts/`, `catalog/proof/`, and `release/` are separate responsibility surfaces; ADR-0011 describes the separation but remains proposed. | CONFIRMED surfaces / authority resolution NEEDS VERIFICATION |
| Directory authority | Multiple Directory Rules documents share or compete for authority and do not provide a single accepted resolution for this lane. | CONFLICTED / NEEDS VERIFICATION |

The safe current reading is narrow: this directory documents a possible home for proof orchestration. It does not prove that a harness runs, that a generic proof receipt schema or storage home is accepted, that CI invokes a proof command, or that any release or publication gate is satisfied.

[⬆ Back to top](#top)

---

## 1. Purpose

`pipelines/proofs/` documents a proposed implementation boundary for proof harnesses that may demonstrate KFM invariants across one or more domains. The existing path is real; executable ownership and placement are not yet accepted strongly enough to describe the lane as operational.

A future accepted implementation could run checks such as:

- thin-slice integration proofs;
- cross-domain ownership-boundary checks;
- no-network fixture proof runs;
- EvidenceRef-to-EvidenceBundle resolution checks;
- receipt and digest closure checks;
- policy, review, and release-readiness blockers;
- trust-membrane checks proving public clients would use governed APIs or released artifacts only;
- regression checks for prior proof slices; and
- correction and rollback readiness checks for proof-backed public derivatives.

If executable work is later accepted here, it may implement the **how** of proof orchestration. This README does not confer domain doctrine, source-descriptor, schema, contract, policy, EvidenceBundle, lifecycle, catalog, receipt, release, public API, or public UI authority.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why consider `pipelines/`? | An executable proof runner would perform orchestration and validation work, which is compatible with the pipeline responsibility root. | CONFIRMED responsibility rule / placement PROPOSED |
| Why does `proofs/` exist under `pipelines/`? | The path and documentation exist and are intended to avoid assigning cross-domain proof authority to a single domain lane. Existence is not acceptance. | CONFIRMED path / long-term placement NEEDS VERIFICATION |
| Is this a canonical proof store? | No. Proof artifacts, EvidenceBundles, receipts, catalog projections, and release records stay in their separately governed homes. | CONFIRMED boundary posture |
| Does this define proof schemas or receipt homes? | No. Those require accepted schema, contract, and Directory Rules decisions. | CONFIRMED authority separation |
| Does this decide release? | No. Release decisions remain under `release/` and require separate evidence, policy, review, correction, and rollback closure. | CONFIRMED authority separation |
| Can public clients read this lane? | No. Public clients use governed interfaces and released artifacts only. | CONFIRMED trust-membrane posture |
| Is cross-domain test placement settled? | No. Existing `tests/cross_domain/` documentation and Habitat-scoped test scaffolds report conflicting or unresolved placement. | CONFLICTED / NEEDS VERIFICATION |

> [!IMPORTANT]
> If a future accepted proof run passes, that result is not an EvidenceBundle, publication decision, PolicyDecision, ReviewRecord, or ReleaseManifest. It demonstrates only the stated invariants for the pinned implementation, fixtures, and inputs.

[⬆ Back to top](#top)

---

## 3. Proof anti-collapse rules

Disallowed collapses:

```text
proof pass -> release approval
proof run -> EvidenceBundle
proof receipt -> EvidenceBundle
fixture result -> live-data truth
cross-domain proof -> new domain root
pipeline proof -> policy decision
pipeline proof -> schema authority
run summary -> evidence
catalog/triplet projection -> canonical truth
public-safe check -> public release
```

Required distinctions:

- proof harness code, proof specs, fixtures, tests, receipts, EvidenceBundles, catalog records, triplets, PolicyDecisions, ReviewRecords, ReleaseManifests, CorrectionNotices, RollbackCards, and public artifacts remain separate;
- cross-domain proofs preserve each domain's owning lane and cannot create mixed domain roots;
- proof receipts point to EvidenceBundles where claims require proof but do not replace them;
- sensitive-domain checks fail closed unless policy, review, receipts, and public-safe representations are present;
- every release-facing proof emits blockers rather than publishing directly.

[⬆ Back to top](#top)

---

## 4. What belongs here

Until ownership and placement are accepted, documentation that clarifies the boundary may live here. Executable files belong here only if an accepted ADR or equivalent governed decision assigns their primary responsibility to shared proof orchestration.

Potential contents, all **PROPOSED** unless independently established, include:

- proof-harness boundary and contract documentation;
- fixture-only, no-network proof runners;
- cross-domain invariant, source-role, and ownership checks;
- EvidenceBundle reference checks;
- policy and review prerequisite checks;
- release-blocker candidate builders;
- trust-membrane checks;
- digest and receipt validation helpers;
- rollback and correction readiness checks; and
- thin adapters that read stable domain outputs without taking domain ownership.

A placement test:

> If an artifact proves scoped invariants without owning domain truth and emits only governed review inputs or blockers, this lane may be a candidate. If it owns a domain pipeline, connector, schema, policy, receipt contract, catalog truth, release decision, lifecycle data, public API, or UI behavior, it belongs elsewhere.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Responsibility boundary |
|---|---|
| Single-domain ingest, normalize, validate, catalog, or publish logic | `pipelines/domains/<domain>/...` or the accepted domain pipeline home |
| Source fetchers and API clients | Accepted connector responsibility home |
| Source descriptors | Accepted source-registry home |
| Domain doctrine | `docs/domains/<domain>/` or governed cross-domain documentation |
| Schemas | Accepted `schemas/` responsibility home |
| Contracts and object meaning | Accepted `contracts/` responsibility home |
| Policy | Accepted `policy/` responsibility home |
| Declarative proof specs | Accepted spec/config home; `pipeline_specs/proofs/...` is illustrative and PROPOSED |
| Fixtures | Accepted fixture home; the existing Habitat × Fauna fixture documentation is Habitat-scoped and final cross-domain placement remains unresolved |
| Tests | Accepted test home; `tests/cross_domain/` and Habitat-scoped thin-slice documentation exist, while `tests/pipelines/proofs/` is not established by the bounded inspection |
| EvidenceBundles and proof artifacts | Governed `data/proofs/` surfaces under their accepted schemas and lifecycle rules |
| Receipts | Governed `data/receipts/` surfaces under an accepted receipt schema and subtype home |
| Lifecycle data | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, and `data/published` |
| Catalog authority or compatibility redirects | Accepted catalog surfaces; `catalog/proof/` must not become a second proof store |
| Release decisions | `release/` |
| Public API or UI code | Governed application and package roots |

[⬆ Back to top](#top)

---

## 6. Proof harness inventory

| Documented lane | Path | Intended purpose | Verified maturity |
|---|---|---|---|
| Habitat × Fauna thin slice | `pipelines/proofs/habitat_fauna_thin_slice/` | Preserve Habitat and Fauna ownership while checking evidence, sensitivity, trust-membrane, blocker, correction, and rollback invariants. | README v0.2 CONFIRMED; executable runner, payload inventory, proof receipt, accepted CI command, and release wiring PROPOSED or NEEDS VERIFICATION |

No additional executable proof harness was established under this subtree by the bounded inspection. ADR-0009 proposes Hydrology as the first proof-bearing lane, but its draft/proposed state does not add a verified executable entry to this directory.

Add another inventory row only after its path, owner, invariant set, fixture plan, receipt plan, evidence and sensitivity policy, tests, correction/rollback posture, and executable maturity have been checked. A README alone is not an executable harness.

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

A future proof harness must exercise KFM lifecycle transitions without bypassing them:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Proposed operating stance:

1. **Read** only fixture, processed, catalog, triplet, release-candidate, or released-artifact references allowed for the proof scope.
2. **Verify** source roles, ownership boundaries, EvidenceBundle refs, policy refs, review refs, receipts, digests, sensitivity transforms, and release blockers.
3. **Run** deterministically and without network access by default.
4. **Emit** only contract-valid proof results, receipts, blocker candidates, and review handoffs into accepted homes.
5. **Hold or abstain** when evidence, policy, sensitivity, review, catalog, release, correction, or rollback prerequisites are missing.
6. **Never publish, create release decisions, mutate canonical lifecycle stores, or expose internal stores.**

This is a future execution contract. It is not evidence that a runner currently performs these steps.

[⬆ Back to top](#top)

---

## 8. Required gates

Every future harness accepted under this directory must check or explicitly fail closed on:

1. **Scope gate** — proof scope, owner, fixture/input set, and invariant list are explicit.
2. **No-network gate** — default execution is fixture-only and no-network unless a separately approved integration profile allows otherwise.
3. **Input-ref gate** — input refs are stable, digestable, lifecycle-appropriate, and authorized.
4. **Evidence gate** — claim-bearing outputs resolve EvidenceRefs to EvidenceBundles or abstain.
5. **Policy/review gate** — finite policy and review outcomes exist where sensitivity or materiality requires them.
6. **Domain-boundary gate** — cross-domain proof harnesses preserve each owning domain lane.
7. **Sensitivity and rights gate** — restricted data cannot leak into public fixtures, examples, artifacts, logs, receipts, or summaries.
8. **Receipt gate** — each run uses an accepted schema and records inputs, checks, hashes, outcomes, blockers, and emitter identity.
9. **Release-blocker gate** — missing rollback target, correction path, policy, review, evidence, rights, sensitivity transform, or artifact proof becomes an explicit blocker.
10. **Trust-membrane gate** — public clients would read only governed APIs or released artifacts.
11. **No-direct-publish gate** — a proof harness never writes public layers, ReleaseManifests, public API state, or UI state as a side effect.

Documentation conformance is not gate execution. These gates become CONFIRMED only when an accepted implementation and tests demonstrate them.

[⬆ Back to top](#top)

---

## 9. Directory contract

At the pinned evidence snapshot, the bounded inspection established this parent README and the Habitat × Fauna child README. It did not establish executable proof files in this subtree.

The following shape is entirely **PROPOSED** and must not be treated as an accepted file plan:

```text
pipelines/proofs/
├── README.md                         # CONFIRMED: this documentation boundary
└── <proof_id>/
    ├── README.md                     # PROPOSED for new lanes
    ├── PROOF_CONTRACT.md             # PROPOSED
    ├── run_dry_fixture.py            # PROPOSED
    ├── check_<invariant>.py          # PROPOSED
    ├── emit_proof_receipt.py         # PROPOSED only if not shared
    └── adapters/                     # PROPOSED thin refs to domain outputs
```

A declarative spec location such as `pipeline_specs/proofs/<proof_id>.yaml` is also **PROPOSED / NEEDS VERIFICATION**. Existing references to that path do not establish the directory or its authority.

Generated outputs must never be written beside executable code. Exact proof, receipt, catalog, triplet, blocker, and release-candidate destinations require accepted schemas, contracts, Directory Rules, and ADRs; this README does not authorize parallel homes.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Governed posture | Status |
|---|---|---|
| Proof fixture | Use a reviewed synthetic or public-safe fixture in an accepted fixture home. The documented Habitat × Fauna fixture lane is Habitat-scoped; a generic `fixtures/proofs/` home is not established here. | NEEDS VERIFICATION |
| Proof spec | Use an accepted declarative spec/config home. `pipeline_specs/proofs/<proof_id>.yaml` remains illustrative. | PROPOSED |
| Domain inputs | Read stable refs from the owning domain and lifecycle surfaces without taking ownership or bypassing quarantine, validation, catalog, or release gates. | CONFIRMED boundary |
| Evidence support | Resolve EvidenceRefs to governed EvidenceBundles under accepted `data/proofs/` contracts. | CONFIRMED rule / exact subtype placement NEEDS VERIFICATION |
| Proof receipt | Use an accepted proof-receipt schema and receipt home. This README establishes neither. | NEEDS VERIFICATION |
| Catalog/triplet projection | Emit only provenance-bound derivatives into accepted catalog or triplet flows; projections do not become root truth. | CONFIRMED boundary |
| Release blocker | Emit a blocker candidate or review handoff through an accepted contract; never create release approval. | NEEDS VERIFICATION |
| Public output | None directly. Publication requires a separate reviewed release transition with correction and rollback support. | DENIED by default |

[⬆ Back to top](#top)

---

## 11. Minimal proof run receipt

The repository evidence inspected for this update does not establish a final generic proof-receipt schema or storage home. The following example is non-executable and non-authoritative; it shows information a future accepted contract should preserve.

```yaml
schema_version: NEEDS_VERIFICATION
proof_run_id: proof_run_YYYYMMDDThhmmssZ
pipeline_id: proofs.<proof_id>
status: HELD
scope:
  proof_id: <proof_id>
  invariant_set_ref: NEEDS_VERIFICATION
  fixture_profile: synthetic_public_safe
inputs:
  domain_refs: []
  evidence_bundle_refs: []
  policy_decision_refs: []
  review_record_refs: []
checks:
  no_network: true
  input_refs_resolved: false
  domain_boundaries_preserved: false
  evidence_resolved: false
  policy_review_resolved: false
  sensitivity_and_rights_safe: false
  release_blockers_emitted: false
  trust_membrane_preserved: false
anti_collapse:
  proof_run_is_release_decision: false
  proof_receipt_is_evidence_bundle: false
  fixture_result_is_live_truth: false
  generated_summary_is_evidence: false
outputs:
  proof_receipt_ref: NEEDS_VERIFICATION
  blocker_refs: []
rollback:
  required_before_publication: true
```

This example is not an emitted receipt, EvidenceBundle, PolicyDecision, ReviewRecord, catalog record, ReleaseManifest, or publication decision.

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Current repository evidence does not establish a generic executable test suite for this lane:

- the bounded inspection established documentation in `pipelines/proofs/`, not a runner or checker;
- `tests/cross_domain/` and `tests/cross_domain/fauna_habitat/` describe surviving but placement-conflicted documentation surfaces and do not establish executable proof coverage;
- the Habitat × Fauna child README records a one-line Habitat test placeholder and an unverified fixture payload inventory; and
- `.github/workflows/domain-habitat.yml` intentionally holds when accepted validation, proof-producer, or release-dry-run commands are absent.

Exact test and fixture placement is **CONFLICTED / NEEDS VERIFICATION**. Do not create another parallel tree until ownership and migration expectations are accepted.

An illustrative future suite might contain these checks under an accepted test home:

```text
<accepted_test_home>/<proof_id>/
├── test_no_network_dry_run.py
├── test_input_refs_resolve.py
├── test_domain_boundaries_preserved.py
├── test_sensitive_data_public_safe.py
├── test_evidence_bundle_required.py
├── test_policy_review_required.py
├── test_release_blockers_emitted.py
├── test_trust_membrane_preserved.py
├── test_receipt_hashes.py
└── test_no_direct_publish.py
```

A dry run may prove only that the stated guardrails behaved as expected for the pinned fixtures and implementation. It does not prove live-data truth, full source coverage, policy approval, human review, release approval, public safety outside tested cases, or publication readiness.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

A future accepted proof harness may prepare contract-valid receipts, invariant reports, graph checks, and release-readiness blocker candidates. No generic producer or emitted inventory is established here, and this lane never publishes.

Proposed chain:

```text
fixture / processed / catalog / approved release refs
  -> accepted proof harness checks
  -> proof receipt + blocker candidates
  -> steward review
  -> release candidate, if appropriate
  -> ReleaseManifest
  -> RollbackCard
  -> public-safe artifact
```

Correction and rollback posture:

- failed and held proof runs remain auditable;
- proof receipts preserve input, evidence, policy, review, sensitivity, invariant, digest, and failure references;
- proof outputs are superseded through governed transitions, not hidden overwrite;
- downstream artifacts are invalidated when material inputs, EvidenceBundles, policy decisions, reviews, sensitivity transforms, correction refs, or rollback targets drift;
- proof success cannot authorize release;
- rollback is owned by `release/`, not by proof-harness directories; and
- a merged documentation change is reversed through a transparent revert, not shared-history rewriting.

[⬆ Back to top](#top)

---

## 14. Definition of done

### Documentation boundary

This README is ready for review when it:

- identifies `pipelines/proofs/` as an existing documentation path and proposed proof-orchestration boundary without claiming an executable producer exists;
- records the pinned repository maturity, cross-domain test-placement conflict, workflow holds, and Directory Rules conflict;
- prevents schema, contract, policy, source, lifecycle, EvidenceBundle, receipt, catalog, release, public API, UI, and domain-pipeline authority from being placed here;
- preserves proof-code, proof-spec, fixture, test, receipt, EvidenceBundle, catalog, triplet, review, release, correction, and rollback distinctions;
- blocks proof-pass-as-release, proof-receipt-as-EvidenceBundle, fixture-result-as-live-truth, generated-summary-as-evidence, internal-store exposure, and direct publication; and
- keeps proposed paths, commands, schemas, receipts, and public behavior visibly unimplemented.

### Executable graduation

This lane is executable only when:

- an accepted ADR or equivalent decision resolves shared-proof ownership, lane placement, and cross-domain test placement;
- public-safe fixtures include valid, invalid, denied, held, and abstained cases;
- a deterministic no-network runner and substantive tests exist;
- accepted proof-spec and proof-receipt contracts and homes exist;
- domain-boundary, evidence, policy, review, rights, sensitivity, provenance, blocker, trust-membrane, no-direct-publish, correction, and rollback checks pass;
- CI invokes an accepted repository-native command rather than an explicit hold;
- outputs are read back, hashed, validated, and reviewed; and
- human governance review remains separate from generation, test success, mergeability, release, and publication.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `PIPE-PROOF-001` | Is `pipelines/proofs/` the accepted executable home, or should shared proof orchestration live under tests, tools, runtime, or another responsibility root? | CONFLICTED / NEEDS VERIFICATION / ADR |
| `PIPE-PROOF-002` | Which accepted schema and canonical receipt home own proof-run receipts and invariant reports? | NEEDS VERIFICATION |
| `PIPE-PROOF-003` | Which CI workflow and repository-native command own proof-harness execution? | NEEDS VERIFICATION |
| `PIPE-PROOF-004` | Is a declarative proof-spec family required, and which accepted root owns it? | NEEDS VERIFICATION |
| `PIPE-PROOF-005` | Should proof harnesses emit blocker candidates, or can an accepted contract write blockers directly for release stewards to adopt? | NEEDS VERIFICATION |
| `PIPE-PROOF-006` | Which proof harnesses and closure criteria are required before any public KFM demonstration? | NEEDS VERIFICATION |
| `PIPE-PROOF-007` | How should `tests/cross_domain/`, Habitat-scoped thin-slice tests, and any future shared-proof tests be reconciled without a parallel authority? | CONFLICTED / NEEDS VERIFICATION |
| `PIPE-PROOF-008` | Which surface is canonical for proof artifacts, given `data/proofs/`, the `catalog/proof/` compatibility redirect, and proposed ADR-0011? | NEEDS VERIFICATION |
| `PIPE-PROOF-009` | Who owns the executable inventory and verifies that README-only lanes are not reported as operational harnesses? | NEEDS VERIFICATION |

---

## Maintainer note

Start with accepted placement, synthetic/public-safe fixtures, and negative tests. The current documentation does not authorize executable creation. Do not add live source fetching, source-profile editing, schema or policy authority, proof or receipt authority, release decisions, domain truth ownership, public API/UI code, ReleaseManifest writes, published-layer writes, or generated factual summaries until proof scope, ownership, contracts, fixture sensitivity, EvidenceBundle refs, policy decisions, review state, deterministic receipts, CI coverage, correction paths, and rollback expectations are established and tested.

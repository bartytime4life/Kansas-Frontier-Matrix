<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-proofs-readme
title: Pipeline Proofs README
type: readme
version: v0.1
status: draft
owners:
  - <pipeline-owner>
  - <proof-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public-with-proof-harness-and-release-gates
path: pipelines/proofs/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipeline_specs/proofs/
  - tests/pipelines/proofs/
  - fixtures/proofs/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/
  - release/manifests/
  - pipelines/proofs/habitat_fauna_thin_slice/README.md
tags: [kfm, pipelines, proofs, proof-harness, evidence-bundle, receipts, no-network, release-blockers, governance]
notes:
  - "This README fills the blank pipelines/proofs path as an implementation-lane index for executable proof harnesses."
  - "The pipelines root is executable pipeline logic — the how — while pipeline_specs is declarative configuration — the what."
  - "This path is a proof-harness code lane, not the canonical EvidenceBundle store and not a new lifecycle, schema, contract, policy, source, registry, or release root."
  - "Because pipelines/proofs is a sublane under an implementation root rather than a top-level canonical root, exact long-term placement remains NEEDS VERIFICATION / ADR if future proof harnesses harden into a broader authority surface."
  - "Concrete executable behavior, CI coverage, fixture coverage, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Pipeline Proofs

> Executable proof-harness lane for KFM integration proofs, thin slices, invariant checks, trust-membrane checks, no-network fixture runs, receipt emission, and release-readiness blockers — without owning EvidenceBundle truth, release decisions, policy decisions, domain truth, schemas, contracts, lifecycle data, or public API/UI behavior.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-proof%20harnesses-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20proof%20logic-0a7ea4)
![evidence](https://img.shields.io/badge/evidence-bundle%20separate-d62728)
![publication](https://img.shields.io/badge/publication-no%20direct%20publish-d62728)

**Status:** Draft  
**Path:** `pipelines/proofs/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Sublane:** Proof harnesses / integration proof orchestration  
**Placement posture:** implementation sublane under `pipelines/`; exact long-term authority remains `NEEDS VERIFICATION / ADR` if proof harnesses become a shared authority surface  
**Public posture:** no direct publication; proof outputs are receipts, reports, invariant results, and release-readiness blockers only.

---

## Quick jump

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

## 1. Purpose

`pipelines/proofs/` is the implementation lane for executable proof harnesses that demonstrate KFM invariants across one or more domains.

It exists to run checks such as:

- thin-slice integration proofs;
- cross-domain ownership-boundary checks;
- no-network fixture proof runs;
- EvidenceRef/EvidenceBundle resolution checks;
- receipt and digest closure checks;
- policy/review/release-readiness blockers;
- trust-membrane checks proving public clients would use governed APIs or released artifacts only;
- regression checks for prior proof slices;
- correction and rollback readiness checks for proof-backed public derivatives.

This directory implements or will implement the **how** of proof orchestration. It does not own domain doctrine, source descriptors, schemas, contracts, policies, EvidenceBundles, lifecycle records, release decisions, public API behavior, or public UI behavior.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | Proof harnesses are executable orchestration: the **how**. | CONFIRMED root responsibility |
| Why `proofs/` under `pipelines/`? | It groups executable proof runners that are not owned by a single domain pipeline. | PROPOSED / NEEDS VERIFICATION |
| Is this a canonical proof store? | No. Proof artifacts and EvidenceBundles belong under accepted `data/proofs/` and receipt homes. | CONFIRMED boundary posture |
| Does this define proof schemas? | No. Schemas belong under accepted schema homes. | CONFIRMED authority separation |
| Does this decide release? | No. Release decisions remain under `release/`. | CONFIRMED authority separation |
| Can public clients read this lane? | No. Public clients use governed APIs and released artifacts only. | CONFIRMED trust-membrane posture |

> [!IMPORTANT]
> A passing proof run is not an EvidenceBundle, not publication, and not a ReleaseManifest. It is executable evidence that a scoped harness met its stated invariants for the checked fixtures or inputs.

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

Files belong here when their primary responsibility is executable proof-harness orchestration.

Appropriate contents include:

- proof-harness README files;
- fixture-only proof runners;
- no-network proof entrypoints;
- cross-domain invariant checks;
- source-role and domain-boundary checks;
- EvidenceBundle reference checks;
- policy/review gate checks;
- release-blocker generators;
- trust-membrane checks;
- digest/receipt validation helpers;
- rollback/correction readiness checks;
- adapters that read outputs from domain pipelines by stable refs without taking ownership of those domains.

A good placement test:

> If the code proves one or more KFM invariants using already-scoped inputs and emits receipts/blockers without owning domain truth, it may belong here. If it owns a domain pipeline, source connector, schema, policy, release decision, lifecycle data, public API, or UI behavior, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Single-domain ingest/normalize/validate/catalog/publish logic | `pipelines/domains/<domain>/...` |
| Source fetchers and API clients | `connectors/<source_id>/` or accepted connector home |
| Source descriptors | `data/registry/sources/<domain>/` or accepted registry home |
| Domain doctrine | `docs/domains/<domain>/` or cross-domain ADR/docs |
| Schemas | `schemas/contracts/v1/...` accepted schema home |
| Contracts / object meaning | `contracts/...` accepted contract home |
| Policy | `policy/...` responsibility roots |
| Declarative proof specs | `pipeline_specs/proofs/...` |
| Fixtures | `fixtures/proofs/...` or accepted fixture home |
| Tests | `tests/pipelines/proofs/...` or accepted test home |
| EvidenceBundles | `data/proofs/evidence_bundle/` or accepted proof data home |
| Receipts | `data/receipts/...` accepted receipt homes |
| Lifecycle data | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` |
| Release decisions | `release/...` |
| Public API/UI code | `apps/governed-api/`, `apps/explorer-web/`, packages |

[⬆ Back to top](#top)

---

## 6. Proof harness inventory

| Proof harness | Path | Purpose | Status |
|---|---|---|---|
| Habitat × Fauna thin slice | `pipelines/proofs/habitat_fauna_thin_slice/` | Cross-domain proof that Habitat context and Fauna evidence can be joined without collapsing domain ownership or exposing sensitive fauna material. | Draft / NEEDS VERIFICATION |

New proof harnesses should be added only when they have a clear invariant, fixture plan, receipt plan, evidence policy, test plan, rollback/correction posture, and owner assignment.

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Proof harnesses exercise KFM lifecycle transitions without bypassing them:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** fixture, processed, catalog, triplet, release-candidate, or released-artifact refs appropriate to the proof scope.
2. **Verify** source roles, ownership boundaries, EvidenceBundle refs, policy refs, review refs, receipts, digests, and release blockers.
3. **Run** proof checks without network access by default.
4. **Emit** proof receipts, invariant results, blocker lists, and review handoffs into accepted receipt/proof homes.
5. **Hold** proof outputs if evidence, policy, sensitivity, review, catalog, release, correction, or rollback preconditions are missing.
6. **Never publish, create release decisions, mutate canonical lifecycle stores, or expose internal stores.**

[⬆ Back to top](#top)

---

## 8. Required gates

Every proof harness under this directory must check or explicitly fail closed on:

1. **Scope gate** — proof scope, owner, fixture/input set, and invariant list are explicit.
2. **No-network gate** — default execution is fixture-only and no-network unless an approved integration profile says otherwise.
3. **Input-ref gate** — all input refs are stable, digestable, and lifecycle-appropriate.
4. **Evidence gate** — claim-bearing outputs resolve EvidenceBundle refs or abstain.
5. **Policy/review gate** — finite policy and review outcomes exist where sensitivity or materiality requires them.
6. **Domain-boundary gate** — cross-domain proof harnesses preserve owning domain lanes.
7. **Sensitivity gate** — sensitive-domain data cannot leak into public fixtures, examples, artifacts, or summaries.
8. **Receipt gate** — every proof run emits deterministic receipts with inputs, checks, hashes, outcomes, and blockers.
9. **Release-blocker gate** — missing rollback target, correction path, policy, review, evidence, or artifact proof becomes an explicit blocker.
10. **Trust-membrane gate** — public clients would read only governed APIs or released artifacts.
11. **No-direct-publish gate** — proof harnesses never write public layers, release manifests, public API state, or UI state as side effects.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/proofs/
├── README.md
└── <proof_id>/
    ├── README.md
    ├── PROOF_CONTRACT.md             # PROPOSED
    ├── run_dry_fixture.py            # PROPOSED
    ├── check_<invariant>.py          # PROPOSED
    ├── emit_proof_receipt.py         # PROPOSED only if not shared
    └── adapters/                     # PROPOSED thin refs to domain outputs
```

Declarative specs should live outside this directory:

```text
pipeline_specs/proofs/<proof_id>.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated proof outputs must not be written beside this code. Use accepted homes under `data/receipts/pipeline/`, `data/proofs/evidence_bundle/`, `data/catalog/`, `data/triplets/`, and `release/candidates/` as governed downstream locations.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Proof fixture | `fixtures/proofs/<proof_id>/` or accepted fixture home | Synthetic/public-safe by default. |
| Proof spec | `pipeline_specs/proofs/<proof_id>.yaml` | Declarative proof shape, not executable logic. |
| Domain inputs | `data/processed/<domain>/`, `data/catalog/domain/<domain>/`, `data/triplets/`, or release refs | Read by stable refs only. |
| Evidence proof | `data/proofs/evidence_bundle/` | Required for claim-bearing outputs. |
| Proof receipt | `data/receipts/pipeline/proofs/<proof_id>/<run_id>.yml` or accepted receipt home | Records refs, gates, outcomes, blockers. |
| Release blocker | `release/candidates/...` or accepted release-candidate home | Handoff only; no release decision. |

[⬆ Back to top](#top)

---

## 11. Minimal proof run receipt

The final schema is not defined here. This example shows the minimum information a proof harness receipt should preserve.

```yaml
schema_version: kfm.proof_run_receipt.v1
proof_run_id: proof_run_YYYYMMDDThhmmssZ
pipeline_id: proofs.<proof_id>
status: HELD
scope:
  proof_id: <proof_id>
  invariant_set_ref: pipeline_specs/proofs/<proof_id>.yaml
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
  sensitivity_safe: false
  release_blockers_emitted: false
  trust_membrane_preserved: false
anti_collapse:
  proof_run_is_release_decision: false
  proof_receipt_is_evidence_bundle: false
  fixture_result_is_live_truth: false
  generated_summary_is_evidence: false
outputs:
  proof_receipt_ref: data/receipts/pipeline/proofs/<proof_id>/run_YYYYMMDDThhmmssZ.yml
  blocker_refs: []
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Recommended tests for every proof harness:

```text
tests/pipelines/proofs/<proof_id>/
├── test_no_network_dry_run.py              # PROPOSED
├── test_input_refs_resolve.py              # PROPOSED
├── test_domain_boundaries_preserved.py     # PROPOSED when cross-domain
├── test_sensitive_data_public_safe.py      # PROPOSED when sensitivity applies
├── test_evidence_bundle_required.py        # PROPOSED
├── test_policy_review_required.py          # PROPOSED
├── test_release_blockers_emitted.py        # PROPOSED
├── test_trust_membrane_preserved.py        # PROPOSED
├── test_receipt_hashes.py                  # PROPOSED
└── test_no_direct_publish.py               # PROPOSED
```

A dry run should prove fixtures load without network access, stable input refs resolve, domain boundaries hold, evidence refs are required, policy/review gates are enforced, blockers are explicit, receipts are deterministic, and no proof run writes directly to public UI, public API, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

Proof harnesses may prepare receipts, invariant reports, graph/check summaries, and release-readiness blockers. They do not publish.

Required chain:

```text
fixture / processed / catalog / release refs
  -> proof harness checks
  -> proof receipt + blockers
  -> steward review
  -> release candidate, if appropriate
  -> ReleaseManifest
  -> RollbackCard
  -> public-safe artifact
```

Correction and rollback posture:

- failed proof runs remain auditable;
- proof receipts preserve input refs, evidence refs, policy refs, review refs, invariant checks, and failure reasons;
- proof outputs are superseded through governed state transitions, not hidden overwrite;
- downstream artifacts are invalidated if input refs, EvidenceBundle refs, policy refs, review refs, sensitivity transforms, correction refs, or rollback refs drift;
- rollback is owned by `release/`, not by proof harness directories.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/proofs/README.md` file;
- identifies this directory as an executable proof-harness sublane under `pipelines/`;
- prevents schemas, contracts, policy, source descriptors, lifecycle data, EvidenceBundles, release decisions, public API, UI, and domain-owned pipeline logic from being placed here;
- preserves proof-code/proof-spec/fixture/test/receipt/EvidenceBundle/catalog/triplet/release boundaries;
- blocks proof-pass-as-release, proof-receipt-as-EvidenceBundle, fixture-result-as-live-truth, generated-summary-as-evidence, internal-store exposure, and direct publication writes;
- gives maintainers a fixture-first, no-network, receipt-emitting, fail-closed expansion pattern.

Future executable work in this lane is done only when it has public-safe fixtures, no-network tests, invariant checks, EvidenceBundle checks, policy/review checks, release-blocker checks, deterministic receipts, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `PIPE-PROOF-001` | Is `pipelines/proofs/` the final accepted home for executable proof harnesses, or should this move under `tests/`, `tools/`, or another implementation root by ADR? | NEEDS VERIFICATION / ADR |
| `PIPE-PROOF-002` | Which schema owns proof receipts and invariant reports? | NEEDS VERIFICATION |
| `PIPE-PROOF-003` | Which CI job owns proof harness execution? | UNKNOWN |
| `PIPE-PROOF-004` | Should every proof harness have a matching `pipeline_specs/proofs/<proof_id>.yaml`? | NEEDS VERIFICATION |
| `PIPE-PROOF-005` | Should proof harnesses write release blockers directly or emit blocker candidates for release stewards to adopt? | NEEDS VERIFICATION |
| `PIPE-PROOF-006` | Which proof harnesses are required before first public KFM demo release? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic/public-safe fixtures and negative tests. Do not add live source fetching, source-profile editing, schema authority, policy authority, release-decision authority, domain truth ownership, public API code, UI code, release-manifest writes, published-layer writes, or generated summaries until proof scope, invariant checks, EvidenceBundle refs, policy decisions, review state, deterministic receipts, CI coverage, and rollback expectations are proven.

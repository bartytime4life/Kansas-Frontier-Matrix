<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-flora-redact-readme
title: Flora Redact Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <flora-pipeline-owner>
  - <flora-domain-steward>
  - <sensitivity-steward>
  - <geoprivacy-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public-with-flora-redaction-and-geoprivacy-gates
path: pipelines/domains/flora/redact/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/flora/README.md
  - pipelines/domains/flora/ingest/README.md
  - pipelines/domains/flora/normalize/README.md
  - pipelines/domains/flora/catalog/README.md
  - pipelines/domains/flora/publish/README.md
  - docs/domains/flora/README.md
  - docs/domains/flora/DATA_LIFECYCLE.md
  - docs/domains/flora/SENSITIVITY_POSTURE.md
  - docs/domains/flora/PUBLICATION_AND_ROLLBACK.md
  - docs/domains/flora/IDENTITY_MODEL.md
  - policy/domains/flora/
  - policy/sensitivity/flora/
  - pipeline_specs/flora/redact.yaml
  - contracts/domains/flora/
  - schemas/contracts/v1/domains/flora/
  - data/work/flora/
  - data/quarantine/flora/
  - data/processed/flora/
  - data/catalog/domain/flora/
  - data/published/layers/flora/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/flora/
  - release/manifests/flora/
tags:
  - kfm
  - pipelines
  - domains
  - flora
  - redact
  - redaction-receipt
  - geoprivacy
  - public-safe-transform
  - sensitivity
  - source-role
  - evidence-bundle
  - policy
  - rollback
  - governance
notes:
  - "This README fills the blank pipelines/domains/flora/redact path as a nested executable Flora redaction/geoprivacy transform sublane."
  - "Flora redaction logic is executable transform support only; it does not own policy decisions, geoprivacy decisions, source descriptors, schemas, EvidenceBundle truth, catalog truth, release decisions, or public API authority."
  - "Redaction creates reviewable public-representation candidates and transform receipts; it does not make a Flora record public by itself."
  - "Controlled Flora coordinates, steward-reviewed material, rights-unclear material, and join-sensitive context fail closed until policy, review, transform receipt, correction path, and rollback target are present."
  - "Concrete executable behavior, CI coverage, release wiring, public API/map behavior, and transform schemas remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Flora Redact Pipeline

> Executable Flora sublane for producing controlled public representations, redaction receipts, generalized or aggregated geometry candidates, suppression/withholding markers, quarantine records, catalog/release handoffs, and audit receipts from sensitive Flora records — while preserving source identity, source role, EvidenceBundle refs, policy outcomes, review refs, correction paths, and rollback targets.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-flora%20redact-2e7d32)
![authority](https://img.shields.io/badge/authority-transform%20logic%20only-0a7ea4)
![geoprivacy](https://img.shields.io/badge/geoprivacy-fail%20closed-d62728)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/flora/redact/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Flora  
**Sublane:** Redact / geoprivacy transform / public-representation preparation  
**Placement posture:** nested executable sublane under `pipelines/domains/flora/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no independent publication authority; this lane prepares transform candidates and receipts only. Public use still requires EvidenceBundle, policy, review, ReleaseManifest, correction, and rollback closure.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Redaction anti-collapse rules](#3-redaction-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Redaction scope](#6-redaction-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal redaction receipt candidate](#11-minimal-redaction-receipt-candidate)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Promotion, publication, correction, and rollback](#13-promotion-publication-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/domains/flora/redact/` is the executable sublane for Flora redaction and geoprivacy transform preparation.

It supports candidate processing for:

- controlled Flora occurrences, specimen localities, vegetation-community geometry, survey locations, range surfaces, and habitat-association links;
- public representations such as withheld, generalized, gridded, aggregated, coarsened, buffered, masked, delayed, or denied geometry states;
- `RedactionReceipt` / transform-receipt candidates that record what changed, why, by which policy outcome, with which reviewer, and for which release candidate;
- audit-friendly links between protected source geometry and public representation without exposing protected fields in public artifacts;
- negative-state markers such as held, denied, generalized, aggregated, stale, corrected, superseded, or withdrawn;
- quarantine records for missing policy decision, missing review state, unsupported transform, unresolved rights, source-role collapse, missing EvidenceBundle, join-sensitive exposure risk, digest mismatch, or rollback gap;
- handoffs to validate, catalog, publish, EvidenceBundle, release-review, correction, and rollback workflows.

This directory implements or will implement the **how** of redaction transform execution. It does not decide policy, decide release, define sensitivity tiers, own source descriptors, define schemas, approve taxonomy, own EvidenceBundle truth, own catalog truth, mutate source geometry, or publish public artifacts by itself.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/flora/`? | Flora is a domain lane under the domain-pipeline umbrella. | CONFIRMED path responsibility pattern; behavior NEEDS VERIFICATION |
| Why `redact/`? | This is a narrow executable sublane for Flora public-representation transforms and receipts. | PROPOSED / NEEDS VERIFICATION |
| Does this own policy? | No. It consumes policy/review outcomes and fails closed when unresolved. | CONFIRMED policy separation |
| Does this own release? | No. It prepares transform receipts and release handoffs; release decisions live under `release/`. | CONFIRMED release separation |
| Can public clients read this lane? | No. Public clients use governed APIs and release-approved public artifacts only. | CONFIRMED trust membrane posture |

> [!IMPORTANT]
> Redaction is not publication. A transform receipt proves that a protective transform was attempted and recorded; it does not by itself authorize a public layer, public API response, map card, export, or AI answer.

[⬆ Back to top](#top)

---

## 3. Redaction anti-collapse rules

Redaction must preserve source geometry, public representation, policy outcome, evidence support, review state, and release state as separate objects.

Disallowed collapses:

```text
redaction run -> policy approval
redaction receipt -> release approval
public representation -> source geometry
withheld marker -> missing data
aggregated layer -> source occurrence set
redaction token -> EvidenceBundle
policy hint -> PolicyDecision
review note -> ReleaseManifest
catalog record -> public artifact
copied artifact -> publication
generated caveat -> evidence
pipeline run -> rollback proof
```

Required distinctions:

- source object, protected fields, transform candidate, transform receipt, policy decision, review record, EvidenceBundle, catalog record, release candidate, ReleaseManifest, CorrectionNotice, RollbackCard, and public artifact remain separate;
- public representation carries enough metadata to be useful without exposing protected source fields;
- every transform is deterministic or receipt-backed enough to audit and invalidate;
- held, denied, generalized, aggregated, corrected, stale, and withdrawn states are surfaced, not silently hidden;
- release-facing artifacts bind to content hashes and release refs, not floating outputs.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable Flora redaction/geoprivacy transform logic.

Appropriate contents include:

- fixture-only redaction dry-run entrypoints;
- public-representation transform runners;
- transform receipt builders;
- policy/review/EvidenceBundle presence validators;
- source/public geometry separation validators;
- generalized, aggregated, gridded, buffered, masked, withheld, or delayed representation builders;
- join-sensitivity preflight helpers;
- caveat and negative-state metadata builders;
- digest, invalidation, and rollback-target validators;
- quarantine/hold routing helpers for missing policy, review, evidence, transform, rights, or rollback preconditions;
- release handoff helpers that do not decide release.

A good placement test:

> If the code transforms controlled Flora material into a protected public representation and emits receipts for downstream review, it may belong here. If it decides policy, fetches sources, normalizes records, validates botanical truth, owns catalog truth, decides release, or serves API/UI output, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Source fetchers, API clients, watchers | `connectors/` or watcher roots |
| Ingest, normalize, validate, or catalog logic | sibling Flora pipeline sublanes |
| Source descriptors / source registry entries | `data/registry/sources/flora/` or approved registry home |
| Flora doctrine and object meaning | `docs/domains/flora/`, `contracts/domains/flora/` |
| JSON Schemas | `schemas/contracts/v1/domains/flora/` or accepted schema home |
| Policy, rights, sensitivity, geoprivacy rules | `policy/...` responsibility roots |
| Release decisions, ReleaseManifest authorship, RollbackCards | `release/...` responsibility roots |
| Fixtures | `fixtures/domains/flora/redact/` or accepted fixture home |
| Tests | `tests/pipelines/domains/flora/redact/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published lifecycle outputs | `data/...` lifecycle homes |
| Public API or map viewer code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Direct model summaries or generated answer text | Governed AI/released artifact paths only after review |

[⬆ Back to top](#top)

---

## 6. Redaction scope

| Scope area | Redact-lane responsibility | Failure behavior |
|---|---|---|
| Input state | Confirm input is processed/work candidate material with source refs and sensitivity posture. | Hold or quarantine. |
| Policy/review | Confirm policy and review refs exist for transform direction. | Hold; do not transform toward public. |
| Source/public separation | Preserve source geometry and public representation as distinct refs. | Quarantine on collapse. |
| Transform receipt | Record method, parameters, reason, reviewer, digests, and output refs. | Hold if receipt cannot be emitted. |
| Evidence | Preserve EvidenceBundle refs and citation state for claim-bearing public records. | Abstain or hold if unresolved. |
| Join risk | Detect joins that reconstruct protected locations or identities. | Hold or escalate to policy review. |
| Correction | Support restriction, withdrawal, supersession, and derivative invalidation. | Emit correction handoff. |
| Release readiness | Prepare release handoff only after transform, policy, review, and rollback refs resolve. | No direct publication. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Flora redaction run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** approved fixtures, work candidates, processed Flora records, catalog candidates, EvidenceBundle refs, policy decisions, review records, correction refs, and release-candidate refs.
2. **Verify** source/public separation, source role, rights, evidence, sensitivity posture, transform eligibility, review state, and rollback expectations.
3. **Transform** only into approved public-representation candidates such as withheld, generalized, aggregated, gridded, masked, delayed, staged, or denied states.
4. **Emit** transform receipts with input refs, policy refs, review refs, method refs, parameters, digests, output refs, and failure reasons.
5. **Hold or quarantine** missing evidence, policy, review, rights, source role, transform, digest, or rollback preconditions.
6. **Never publish directly.**

Redaction is a governed transform step. It is not source admission, botanical validation, catalog closure, release approval, or public serving.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Flora redaction run must check or explicitly fail closed on:

1. **Input lifecycle gate** — input is approved fixture, WORK, PROCESSED, CATALOG candidate, or release-candidate material.
2. **SourceDescriptor gate** — source identity, source role, rights, citation, and source vintage are present.
3. **EvidenceBundle gate** — claim-bearing records resolve evidence or abstain.
4. **PolicyDecision gate** — finite policy outcome exists; no silent allow.
5. **ReviewRecord gate** — steward/reviewer state exists where materiality or sensitivity requires it.
6. **Transform eligibility gate** — requested public representation is allowed by policy and has a defined method.
7. **Source/public separation gate** — protected fields and public representation remain separate.
8. **Join-sensitivity gate** — derived joins cannot reconstruct protected geometry or identities.
9. **Receipt gate** — every transform emits a deterministic, reviewable receipt.
10. **Correction/rollback gate** — release-facing output carries correction path and rollback target expectations.
11. **No-direct-catalog gate** — redaction does not write catalog/triplet records as a side effect unless explicitly in a handoff mode.
12. **No-direct-publish gate** — redaction does not write public UI, public API, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/flora/redact/
├── README.md                         # this file
├── REDACT_CONTRACT.md                # PROPOSED: Flora redaction execution contract
├── run_dry_fixture.py                # PROPOSED synthetic/redacted fixture only
├── validate_policy_review.py         # PROPOSED
├── validate_evidence_refs.py         # PROPOSED
├── validate_source_public_split.py   # PROPOSED
├── validate_join_sensitivity.py      # PROPOSED
├── build_public_representation.py    # PROPOSED
├── build_transform_receipt.py        # PROPOSED
├── validate_rollback_target.py       # PROPOSED
├── route_hold_quarantine.py          # PROPOSED
├── emit_redaction_receipt.py         # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/flora/redact.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use accepted lifecycle homes under `data/work/flora/`, `data/quarantine/flora/`, `data/processed/flora/`, `data/catalog/domain/flora/`, `data/receipts/`, `data/proofs/`, and `release/`.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/flora/redact/` or accepted fixture home | Synthetic or already-redacted. |
| Work/processed Flora input | `data/work/flora/`, `data/processed/flora/` | Input by stable refs; do not mutate. |
| Catalog/release candidate input | `data/catalog/domain/flora/`, `release/candidates/flora/` | Release-facing transform check. |
| Public representation candidate | `data/work/flora/<run_id>/` or accepted processed derivative home | Candidate only until reviewed. |
| Hold/quarantine record | `data/quarantine/flora/<reason>/<run_id>/` | Failed, restricted, unresolved, stale, or unsafe material. |
| Transform receipt | `data/receipts/pipeline/flora/redact/<run_id>.yml` or accepted receipt home | Records method, policy, review, refs, digests, outputs. |
| Evidence proof | `data/proofs/evidence_bundle/` | Required for claim-bearing records. |
| Release handoff | `release/candidates/flora/` | Reviewable, release-gated output only. |

[⬆ Back to top](#top)

---

## 11. Minimal redaction receipt candidate

The final schema is not defined here. This example shows the minimum information a Flora redaction run should preserve.

```yaml
schema_version: kfm.flora_redaction_receipt_candidate.v1
redaction_run_id: flora_redact_run_YYYYMMDDThhmmssZ
pipeline_id: domains.flora.redact
status: HELD
input:
  flora_object_ref: data/processed/flora/<dataset_id>/<version>/<object_id>.json
  source_descriptor_ref: data/registry/sources/flora/<source_id>.yml
  source_role: <observed|regulatory|administrative|aggregate|model|candidate|synthetic|generated_context>
  evidence_bundle_refs: []
policy:
  policy_decision_ref: null
  review_record_ref: null
  outcome: ABSTAIN
transform:
  requested_public_state: <withheld|generalized|aggregated|gridded|masked|delayed|staged|denied|public>
  method_id: null
  parameters_hash: null
  public_representation_ref: null
  source_public_split_preserved: false
checks:
  evidence_resolved: false
  policy_resolved: false
  review_resolved: false
  rollback_resolved: false
  join_reconstruction_risk: needs_review
anti_collapse:
  redaction_run_is_policy_approval: false
  redaction_receipt_is_release_approval: false
  public_representation_is_source_geometry: false
  withheld_marker_is_missing_data: false
  generated_caveat_is_evidence: false
outputs:
  receipt_ref: data/receipts/pipeline/flora/redact/run_YYYYMMDDThhmmssZ.yml
  work_ref: data/work/flora/run_YYYYMMDDThhmmssZ/public_representation_candidate.yml
  quarantine_ref: null
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/redacted, and no-network** until redaction specs, policy fixtures, evidence, sensitivity, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/flora/redact/
├── test_no_network_dry_run.py              # PROPOSED
├── test_policy_decision_required.py        # PROPOSED
├── test_review_record_required.py          # PROPOSED
├── test_evidence_bundle_required.py        # PROPOSED
├── test_source_public_split_preserved.py   # PROPOSED
├── test_transform_receipt_required.py      # PROPOSED
├── test_join_reconstruction_risk_holds.py  # PROPOSED
├── test_withheld_not_missing.py            # PROPOSED
├── test_public_representation_not_source.py # PROPOSED
├── test_rollback_target_required.py        # PROPOSED
├── test_no_catalog_side_effect.py          # PROPOSED
├── test_receipt_hashes.py                  # PROPOSED
└── test_no_direct_publish.py               # PROPOSED
```

A dry run should prove fixtures load without network access, policy and review refs are required, evidence refs resolve or abstain, source/public separation is preserved, join-reconstruction risk holds, receipts are deterministic, and no run writes directly to catalog, triplet, public UI, public API, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

Flora redaction pipelines may prepare public-representation candidates and transform receipts. They do not publish.

Required chain:

```text
processed Flora record + policy/review/evidence refs
  -> redaction transform candidate
  -> transform receipt
  -> catalog / triplet handoff update
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public artifact assembly
```

Correction and rollback posture:

- protective downgrade is always available through correction workflow;
- correction is a governed forward transition, not a silent edit;
- rollback is receipt-backed and preserves history;
- any derivative depending on a transformed representation must be invalidated when source, policy, transform, evidence, correction, or rollback refs drift;
- release rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/flora/redact/README.md` file;
- identifies this directory as a nested executable Flora redaction/geoprivacy transform sublane;
- prevents source, ingest, normalize, validate, catalog, schema, contract, policy, sensitivity-decision, release-decision, public API, UI, and canonical-store authority from being placed here;
- preserves source role, protected source fields, public representation, policy decision, review record, EvidenceBundle, transform receipt, correction path, rollback target, lifecycle, catalog/triplet, and release boundaries;
- blocks redaction-run-as-policy, redaction-receipt-as-release, public-representation-as-source, withheld-marker-as-missing-data, generated-caveat-as-evidence, catalog side effects, and direct publication writes;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has redacted-fixture coverage, schema-backed transform receipts, contract conformance, policy/review/evidence/source-public-split/join-risk/no-catalog/no-direct-publish tests, deterministic receipts, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `FLORA-REDACT-001` | Should Flora redaction remain one sublane, or split into geometry generalization, aggregation, withholding, caveats, and release-check processors? | NEEDS VERIFICATION / ADR |
| `FLORA-REDACT-002` | Which schema owns transform receipts, public representation states, and redaction reason codes? | NEEDS VERIFICATION |
| `FLORA-REDACT-003` | Which transform vocabulary is approved for first-wave implementation? | NEEDS VERIFICATION / ADR |
| `FLORA-REDACT-004` | Which CI job owns Flora redaction invariant tests? | UNKNOWN |
| `FLORA-REDACT-005` | Should redaction run before catalog closure, during catalog closure, or only during release-candidate preparation? | NEEDS VERIFICATION |
| `FLORA-REDACT-006` | Which rollback proof is required before transformed Flora artifacts can be published? | NEEDS VERIFICATION |
| `FLORA-REDACT-007` | Where should shared geoprivacy transform libraries live if Fauna, Habitat, Archaeology, and Flora use the same operators? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Start with synthetic/redacted fixture-only dry runs and negative tests. Do not add live source fetching, schema authority, policy authority, sensitivity-decision authority, release-decision authority, direct catalog writes, direct public API code, direct UI code, release-manifest authorship, or generated botanical summaries until policy refs, review refs, EvidenceBundle refs, transform receipts, correction paths, rollback targets, and deterministic receipts are proven.

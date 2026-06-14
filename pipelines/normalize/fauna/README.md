<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-normalize-fauna-readme
title: Fauna Shared Normalize Adapter README
type: readme
version: v0.1
status: draft
owners:
  - <pipeline-owner>
  - <normalization-steward>
  - <fauna-domain-steward>
  - <geoprivacy-steward>
  - <evidence-steward>
  - <policy-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public-with-fauna-normalization-geoprivacy-and-receipt-gates
path: pipelines/normalize/fauna/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/normalize/README.md
  - pipelines/domains/fauna/README.md
  - docs/domains/fauna/ARCHITECTURE.md
  - pipeline_specs/normalize/fauna.yaml
  - pipeline_specs/fauna/
  - contracts/domains/fauna/
  - schemas/contracts/v1/domains/fauna/
  - policy/domains/fauna/
  - policy/sensitivity/fauna/
  - data/raw/fauna/
  - data/work/fauna/
  - data/quarantine/fauna/
  - data/processed/fauna/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
tags: [kfm, pipelines, normalize, fauna, adapter, occurrence, monitoring, geoprivacy, transform-receipt, evidence-bundle, policy, governance]
notes:
  - "This README fills the blank pipelines/normalize/fauna path as a Fauna adapter/profile under the shared normalization lane."
  - "This path is not the primary Fauna domain-normalization authority. Domain-owned behavior remains under pipelines/domains/fauna/ or an accepted domain normalize sublane."
  - "Because pipelines/normalize/fauna creates a domain-named segment under a shared helper lane, long-term placement remains NEEDS VERIFICATION / ADR if it hardens beyond adapter/profile support."
  - "Fauna normalization must preserve source roles, occurrence evidence, restricted/public split, geoprivacy transform inputs, RedactionReceipt candidates, EvidenceRef candidates, policy state, and receipts."
  - "Concrete executable behavior, CI coverage, fixtures, schema paths, and release wiring remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Fauna Shared Normalize Adapter

> Shared normalization adapter/profile for Fauna-specific field shaping, source-role preservation, occurrence/monitoring normalization helpers, taxon crosswalk preparation, geoprivacy transform inputs, and receipt-ready WORK fragments — without replacing the Fauna domain pipeline, owning Fauna truth, creating EvidenceBundles, deciding policy, or publishing public artifacts.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-fauna%20normalize%20adapter-2e7d32)
![authority](https://img.shields.io/badge/authority-shared%20adapter%20only-0a7ea4)
![sensitivity](https://img.shields.io/badge/fauna%20sensitivity-fail%20closed-d62728)
![publication](https://img.shields.io/badge/publication-no%20direct%20publish-d62728)

**Status:** Draft  
**Path:** `pipelines/normalize/fauna/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Sublane:** Shared normalize / Fauna adapter-profile support  
**Placement posture:** `PROPOSED / NEEDS VERIFICATION`; use this only as a shared adapter/profile lane. Domain-owned Fauna normalization remains under `pipelines/domains/fauna/` unless an ADR or migration note says otherwise.  
**Public posture:** no direct publication; outputs are WORK fragments, quarantine reasons, transform-receipt candidates, and handoff refs only.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Fauna normalize anti-collapse rules](#3-fauna-normalize-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Adapter scope](#6-adapter-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal adapter receipt fragment](#11-minimal-adapter-receipt-fragment)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Promotion, publication, correction, and rollback](#13-promotion-publication-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/normalize/fauna/` is a Fauna-specific adapter/profile under the shared normalization lane.

It may support reusable helper behavior for:

- animal taxon identifier/crosswalk preparation;
- occurrence and monitoring event field-shaping;
- original observation/source-field preservation;
- source-role and source-vintage preservation;
- restricted/public split preparation;
- geoprivacy transform input preparation;
- RedactionReceipt or generalization-receipt candidate preparation;
- uncertainty, time, geometry, coordinate reference, observation-method, and protocol field shaping;
- quarantine reason preparation for unresolved source role, rights, evidence, policy, geoprivacy, or steward-review state;
- shared receipt fragments used by the owning Fauna domain normalizer.

This directory implements or will implement **adapter support** only. It does not replace `pipelines/domains/fauna/`, does not own Fauna object meaning, does not admit sources, does not fetch upstream data, does not define SourceDescriptors, does not create EvidenceBundles, does not decide policy/geoprivacy/review state, does not write catalog truth, and does not release public artifacts.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline/helper logic: the **how**. | CONFIRMED root responsibility |
| Why `normalize/`? | Parent lane holds shared normalization helpers and adapter profiles. | CONFIRMED parent-lane posture |
| Why `fauna/` under shared normalize? | It can hold Fauna-specific adapter glue for shared helpers, but should not become the primary domain lane. | PROPOSED / NEEDS VERIFICATION |
| Does this replace `pipelines/domains/fauna/`? | No. Fauna domain behavior remains under the domain pipeline lane. | CONFIRMED boundary posture |
| Does this decide geoprivacy or policy? | No. It preserves and carries refs/state; policy and geoprivacy authority live in policy/review roots. | CONFIRMED authority separation |
| Can this publish? | No. It returns WORK fragments, quarantine reasons, and receipt fragments only. | CONFIRMED governance posture |

> [!IMPORTANT]
> This folder is an adapter/profile lane, not a canonical Fauna domain pipeline. If it starts owning domain behavior, it should move to `pipelines/domains/fauna/normalize/` or be governed by an ADR.

[⬆ Back to top](#top)

---

## 3. Fauna normalize anti-collapse rules

Disallowed collapses:

```text
adapter output -> Fauna truth
normalization success -> validation pass
occurrence evidence -> public occurrence without geoprivacy review
OccurrenceRestricted -> OccurrencePublic
geoprivacy transform candidate -> public-safe release
RedactionReceipt candidate -> approved RedactionReceipt
TaxonCrosswalk candidate -> accepted taxonomy
monitoring event -> occurrence truth without source role
range polygon -> occurrence evidence
transform receipt fragment -> EvidenceBundle
generated normalization summary -> evidence
```

Required distinctions:

- RAW capture, WORK candidate, QUARANTINE record, TransformReceipt, RedactionReceipt, ValidationReport, EvidenceBundle, catalog record, triplet projection, ReleaseManifest, CorrectionNotice, RollbackCard, and public artifact remain separate;
- Fauna object families stay under Fauna domain ownership;
- occurrence evidence, restricted occurrence, public occurrence, range, sensitive-site class, monitoring event, mortality, disease, invasive-species, and derived indicators remain separately labeled;
- public-safe derivatives require geoprivacy/review/policy closure, not only geometry transformation;
- unresolved rights, sensitivity, evidence, policy, or steward-review state fails closed.

[⬆ Back to top](#top)

---

## 4. What belongs here

Appropriate contents include:

- Fauna adapter README files;
- fixture-only adapter dry-run entrypoints;
- Fauna profile wrappers for shared unit/time/geometry/source-role helpers;
- occurrence-field and monitoring-event field mappers used by the domain normalizer;
- taxon crosswalk preparation helpers that do not assert accepted taxonomy;
- geoprivacy transform input builders that do not approve release;
- RedactionReceipt candidate builders that do not finalize policy;
- quarantine reason helpers for unresolved Fauna-specific normalization blockers;
- receipt-fragment emitters, if not already shared.

A good placement test:

> If the code adapts shared normalization helpers for Fauna while returning control to the Fauna domain normalizer, it may belong here. If it owns full Fauna normalization behavior, put it under `pipelines/domains/fauna/normalize/`. If it owns schema, policy, source admission, EvidenceBundle truth, catalog truth, release decisions, or public serving, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Primary Fauna domain workflow | `pipelines/domains/fauna/` or accepted Fauna sublane |
| Full domain-specific normalize pipeline | `pipelines/domains/fauna/normalize/` if/when accepted |
| Ingest/source admission | `pipelines/domains/fauna/ingest/` or accepted ingest lane |
| Source fetchers and API clients | `connectors/<source_id>/` or accepted connector home |
| Source descriptors | `data/registry/sources/fauna/` or accepted registry home |
| Fauna doctrine and object meaning | `docs/domains/fauna/`, `contracts/domains/fauna/` |
| JSON Schemas | `schemas/contracts/v1/domains/fauna/` or accepted schema home |
| Policy / geoprivacy / review decisions | `policy/domains/fauna/`, `policy/sensitivity/fauna/`, review roots |
| Fixtures | `fixtures/normalize/fauna/` or `fixtures/domains/fauna/` |
| Tests | `tests/pipelines/normalize/fauna/` or domain test homes |
| Lifecycle outputs | `data/raw/fauna/`, `data/work/fauna/`, `data/quarantine/fauna/`, `data/processed/fauna/`, `data/catalog/domain/fauna/`, `data/published/layers/fauna/` |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Release decisions | `release/...` |
| Public API/UI code | `apps/governed-api/`, `apps/explorer-web/`, packages |

[⬆ Back to top](#top)

---

## 6. Adapter scope

| Scope area | Adapter responsibility | Failure behavior |
|---|---|---|
| Source role | Preserve provided source role; do not invent authority. | Fail or return quarantine reason. |
| Original fields | Preserve source labels, observation values, geometry refs, uncertainty, and payload hashes. | Fail if lossy. |
| Taxon crosswalk | Prepare crosswalk candidates without accepting taxonomy. | Hold on ambiguity. |
| Occurrence/monitoring | Shape fields while retaining event/occurrence/source-role distinction. | Fail on collapse. |
| Geoprivacy input | Prepare transform inputs and receipt fragments without approving public derivative. | Hold pending policy/review. |
| Evidence | Carry EvidenceRef candidates forward; never fabricate EvidenceBundles. | Abstain if unresolved. |
| Receipts | Emit shared receipt fragments or transform-receipt candidates. | Fail closed on missing method/hash refs. |
| Handoff | Return WORK fragments to the Fauna domain normalizer. | No validation/catalog/publish side effects. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every helper in this adapter must preserve KFM lifecycle posture:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** fixture, RAW, WORK, or QUARANTINE-remediation refs only when an owning Fauna pipeline or proof harness provides scope.
2. **Normalize** shared Fauna fields while preserving original fields, source refs, source roles, taxon refs, observation/monitoring distinctions, uncertainty, geometry refs, geoprivacy state, and evidence refs.
3. **Return** normalized WORK fragments, quarantine reasons, and receipt fragments to the owning caller.
4. **Never mark validation pass, write catalog records, create EvidenceBundles, approve geoprivacy, decide release, or publish.**

[⬆ Back to top](#top)

---

## 8. Required gates

Every adapter run must check or explicitly fail closed on:

1. **Caller ownership gate** — an owning Fauna domain pipeline or approved proof harness must provide scope.
2. **Input lifecycle gate** — input is fixture, RAW, WORK, or approved QUARANTINE remediation.
3. **SourceDescriptor/source-role gate** — source identity, role, rights, and citation refs are carried forward.
4. **Original-field gate** — original fields and payload hashes remain recoverable.
5. **Taxon/occurrence boundary gate** — taxon crosswalks, occurrence evidence, monitoring events, ranges, and derived indicators are not collapsed.
6. **Restricted/public split gate** — restricted occurrence and public derivative remain separate.
7. **Geoprivacy gate** — transform inputs do not imply public-safe release.
8. **Evidence gate** — EvidenceRef candidates are carried forward; EvidenceBundles are not fabricated here.
9. **Policy/review gate** — unresolved geoprivacy, rights, sensitivity, or review state remains unresolved and blocks exposure.
10. **Receipt gate** — transform and adapter receipt metadata is produced where material.
11. **No-direct-validation gate** — adapter output does not mark data as validated.
12. **No-direct-catalog gate** — adapter output does not write catalog/triplet records.
13. **No-direct-publish gate** — adapter output does not write public UI, public API, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/normalize/fauna/
├── README.md
├── FAUNA_NORMALIZE_ADAPTER_CONTRACT.md # PROPOSED
├── run_dry_fixture.py                  # PROPOSED
├── map_taxon_crosswalk_candidate.py    # PROPOSED
├── map_occurrence_fields.py            # PROPOSED
├── map_monitoring_event_fields.py      # PROPOSED
├── prepare_geoprivacy_inputs.py        # PROPOSED
├── prepare_redaction_receipt_candidate.py # PROPOSED
├── preserve_source_role.py             # PROPOSED
├── emit_adapter_receipt_fragment.py    # PROPOSED
└── adapters/                           # PROPOSED caller adapters only
```

Declarative specs should live outside this directory:

```text
pipeline_specs/normalize/fauna.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use the owning Fauna domain lifecycle homes under `data/work/fauna/`, `data/quarantine/fauna/`, and `data/receipts/pipeline/`.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Adapter fixture | `fixtures/normalize/fauna/` or accepted fixture home | Synthetic/public-safe by default. |
| Caller scope | `pipelines/domains/fauna/` or approved proof harness | Required; this adapter does not run ownerless. |
| Fauna input refs | `data/raw/fauna/`, `data/work/fauna/`, or approved remediation refs | Read by stable refs only. |
| WORK fragment | `data/work/fauna/` | Owned by the Fauna domain lane. |
| QUARANTINE reason | `data/quarantine/fauna/` | Owned by the Fauna domain lane. |
| Receipt fragment | `data/receipts/pipeline/fauna/normalize/` or accepted receipt home | Method, refs, hashes, and outputs. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced only; not created here. |

[⬆ Back to top](#top)

---

## 11. Minimal adapter receipt fragment

The final schema is not defined here. This example shows the minimum information a Fauna adapter receipt fragment should preserve.

```yaml
schema_version: kfm.normalize.fauna_adapter_receipt.v1
adapter_run_id: fauna_normalize_adapter_run_YYYYMMDDThhmmssZ
pipeline_id: normalize.fauna
status: HELD
caller:
  owner_pipeline: pipelines/domains/fauna/normalize
  profile_ref: pipeline_specs/normalize/fauna.yaml
inputs:
  fauna_refs: []
  source_descriptor_refs: []
  input_payload_hashes: []
source_role:
  source_role_preserved: false
normalization:
  original_fields_preserved: false
  taxon_crosswalk_candidate_ready: false
  occurrence_fields_ready: false
  monitoring_event_fields_ready: false
  geoprivacy_inputs_ready: false
  redaction_receipt_candidate_ready: false
checks:
  evidence_refs_carried_forward: false
  policy_state_preserved: false
  receipt_hashes_ready: false
anti_collapse:
  adapter_output_is_fauna_truth: false
  normalization_success_is_validation_pass: false
  occurrence_restricted_is_occurrence_public: false
  geoprivacy_transform_candidate_is_release_approval: false
outputs:
  work_fragment_refs: []
  quarantine_reason_refs: []
  receipt_fragment_ref: data/receipts/pipeline/fauna/normalize/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Recommended tests:

```text
tests/pipelines/normalize/fauna/
├── test_no_network_dry_run.py              # PROPOSED
├── test_caller_scope_required.py           # PROPOSED
├── test_source_role_preserved.py           # PROPOSED
├── test_original_fields_preserved.py       # PROPOSED
├── test_taxon_crosswalk_not_accepted_taxonomy.py # PROPOSED
├── test_occurrence_monitoring_boundary.py  # PROPOSED
├── test_restricted_public_split.py         # PROPOSED
├── test_geoprivacy_candidate_not_release.py # PROPOSED
├── test_evidence_refs_not_fabricated.py    # PROPOSED
├── test_policy_state_not_silently_allowed.py # PROPOSED
├── test_no_validation_pass_side_effect.py  # PROPOSED
├── test_no_catalog_side_effect.py          # PROPOSED
└── test_no_direct_publish.py               # PROPOSED
```

A dry run should prove fixtures load without network access, caller scope is required, source roles and original fields are preserved, taxon/occurrence/monitoring boundaries hold, restricted/public split is maintained, geoprivacy inputs do not imply release, EvidenceRefs are not fabricated, receipts are deterministic, and no run writes directly to validation pass state, catalog, triplet, public UI, public API, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

Fauna shared normalize adapters may prepare WORK fragments, quarantine reasons, transform-receipt candidates, and receipt fragments. They do not publish.

Required chain:

```text
Fauna domain caller
  -> shared Fauna normalize adapter
  -> WORK fragment / quarantine reason / receipt fragment
  -> Fauna domain validation
  -> EvidenceBundle closure
  -> catalog / triplet handoff
  -> geoprivacy-reviewed release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public-safe artifact
```

Correction and rollback posture:

- failed adapter runs remain auditable;
- receipts preserve source refs, source-role refs, original fields, taxon refs, occurrence refs, geoprivacy refs, EvidenceRef refs, policy refs, and failure reasons;
- adapter outputs are superseded through governed state transitions, not hidden overwrite;
- downstream artifacts are invalidated if source refs, source-role refs, geoprivacy refs, EvidenceBundle refs, policy refs, correction refs, or rollback refs drift;
- rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/normalize/fauna/README.md` file;
- identifies this directory as a Fauna adapter/profile under the shared normalize lane;
- prevents primary Fauna domain logic, schemas, contracts, policy, source descriptors, lifecycle data, EvidenceBundles, release decisions, public API, UI, catalog, and publication authority from being placed here;
- preserves source-role, original-field, taxon/occurrence/monitoring boundaries, restricted/public split, geoprivacy input, transform-receipt, EvidenceRef, policy, lifecycle, quarantine, correction, and rollback boundaries;
- blocks adapter-output-as-Fauna-truth, normalization-success-as-validation-pass, OccurrenceRestricted-as-OccurrencePublic, geoprivacy-candidate-as-release, generated-summary-as-evidence, catalog side effects, and direct publication writes;
- gives maintainers a fixture-first, receipt-emitting, fail-closed expansion pattern.

Future executable work in this adapter lane is done only when it has public-safe fixtures, no-network tests, caller-scope checks, source-role/original-field preservation tests, taxon/occurrence/monitoring-boundary tests, restricted/public split tests, geoprivacy and receipt tests, evidence/policy preservation tests, deterministic receipts, CI coverage, Fauna steward handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `PIPE-NORM-FAUNA-001` | Should this adapter remain under `pipelines/normalize/fauna/`, or should it move to `pipelines/domains/fauna/normalize/` once domain normalize scaffolding is accepted? | NEEDS VERIFICATION / ADR |
| `PIPE-NORM-FAUNA-002` | Which schema owns Fauna adapter receipt fragments and geoprivacy transform candidate fields? | NEEDS VERIFICATION |
| `PIPE-NORM-FAUNA-003` | Which Fauna fixture set should be first-wave for no-network dry runs? | NEEDS VERIFICATION |
| `PIPE-NORM-FAUNA-004` | Which CI job owns shared Fauna adapter invariant tests? | UNKNOWN |
| `PIPE-NORM-FAUNA-005` | Should this adapter emit receipt fragments only, or full Fauna normalize receipts? | NEEDS VERIFICATION |
| `PIPE-NORM-FAUNA-006` | Which geoprivacy transform vocabulary is canonical for Fauna public derivatives? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Start with synthetic/public-safe fixtures and negative tests. Do not add live source fetching, Fauna truth ownership, source-profile editing, schema authority, policy/geoprivacy authority, validation-pass shortcuts, catalog writes, public API code, UI code, release-manifest writes, published-layer writes, or generated summaries until caller scope, source roles, original fields, taxon/occurrence boundaries, restricted/public split, geoprivacy inputs, receipt hashes, EvidenceRef handling, policy state, deterministic receipts, and rollback expectations are proven.

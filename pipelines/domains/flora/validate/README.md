<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-flora-validate-readme
title: Flora Validate Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <flora-pipeline-owner>
  - <flora-domain-steward>
  - <validation-steward>
  - <taxonomy-steward>
  - <sensitivity-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public-with-flora-validation-and-geoprivacy-gates
path: pipelines/domains/flora/validate/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/flora/README.md
  - pipelines/domains/flora/ingest/README.md
  - pipelines/domains/flora/normalize/README.md
  - pipelines/domains/flora/redact/README.md
  - pipelines/domains/flora/catalog/README.md
  - docs/domains/flora/README.md
  - docs/domains/flora/DATA_LIFECYCLE.md
  - docs/domains/flora/IDENTITY_MODEL.md
  - docs/domains/flora/CROSSWALKS.md
  - docs/domains/flora/SENSITIVITY_POSTURE.md
  - docs/domains/flora/PUBLICATION_AND_ROLLBACK.md
  - policy/domains/flora/
  - policy/sensitivity/flora/
  - pipeline_specs/flora/validate.yaml
  - contracts/domains/flora/
  - schemas/contracts/v1/domains/flora/
  - data/work/flora/
  - data/quarantine/flora/
  - data/processed/flora/
  - data/catalog/domain/flora/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/flora/
  - release/manifests/flora/
tags:
  - kfm
  - pipelines
  - domains
  - flora
  - validate
  - validation-report
  - plant-taxon
  - flora-occurrence
  - specimen
  - vegetation-community
  - geoprivacy
  - redaction-receipt
  - source-role
  - evidence-bundle
  - policy
  - governance
notes:
  - "This README fills the blank pipelines/domains/flora/validate path as a nested executable Flora validation sublane."
  - "Flora validation logic is executable implementation support only; it does not own source descriptors, connectors, source profiles, schemas, contracts, policy, taxonomy authority, lifecycle data, catalog truth, sensitivity decisions, or release decisions."
  - "Validation converts normalized WORK candidates into validation reports, processed-candidate handoffs, or quarantine outcomes; it does not make public Flora artifacts by itself."
  - "Taxon identity, source role, EvidenceBundle readiness, RedactionReceipt requirements, geometry handling, temporal facets, rights, schema conformance, and cross-lane ownership must be checked before promotion from WORK to PROCESSED."
  - "Controlled Flora records, steward-reviewed material, rights-unclear material, and join-sensitive context fail closed until evidence, policy, review, transform receipt, correction path, and rollback target are present."
  - "Concrete executable behavior, source activation, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Flora Validate Pipeline

> Executable Flora sublane for validating normalized Flora WORK candidates into `ValidationReport` outcomes, processed-candidate handoffs, quarantine records, receipts, and downstream catalog/release readiness checks — while preserving source identity, source role, taxonomic uncertainty, geometry/sensitivity posture, EvidenceBundle readiness, policy results, correction paths, and rollback boundaries.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-flora%20validate-2e7d32)
![authority](https://img.shields.io/badge/authority-validation%20logic%20only-0a7ea4)
![sensitivity](https://img.shields.io/badge/sensitivity-fail%20closed-d62728)
![publication](https://img.shields.io/badge/publication-no%20direct%20publish-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/flora/validate/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Flora  
**Sublane:** Validate / WORK-to-PROCESSED readiness  
**Placement posture:** nested executable sublane under `pipelines/domains/flora/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no direct publication; validation outputs remain reports, processed-candidate handoffs, quarantine records, and receipts until catalog, release, correction, and rollback closure.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Validate anti-collapse rules](#3-validate-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Validation scope](#6-validation-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal validation report candidate](#11-minimal-validation-report-candidate)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Promotion, publication, correction, and rollback](#13-promotion-publication-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/domains/flora/validate/` is the executable sublane for Flora validation.

It supports validation for:

- normalized `PlantTaxon`, `FloraOccurrence`, `Specimen`, `VegetationCommunity`, `PhenologyObservation`, `InvasivePlantRecord`, `RangePolygon`, restoration, and distribution candidates;
- source descriptor, source role, rights, citation, source-vintage, and payload-hash closure;
- taxon identity and taxonomic crosswalk readiness without making taxonomic authority decisions;
- occurrence/specimen/community object-role conformance and anti-collapse checks;
- geometry precision, coordinate uncertainty, temporal facets, CRS, and public-representation state;
- EvidenceRef readiness and EvidenceBundle closure preconditions;
- RedactionReceipt / aggregation / transform requirements where sensitivity applies;
- policy, review, quarantine reason, and fail-closed outcomes;
- `ValidationReport` outputs, processed-candidate handoffs, quarantine records, receipts, catalog-readiness signals, and release-readiness blockers.

This directory implements or will implement the **how** of Flora validation. It does not fetch source data, admit sources, normalize final records, define schemas, decide policy, decide sensitivity handling, approve taxonomic identity, own EvidenceBundle truth, own catalog truth, decide release, or publish public API/map payloads.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/flora/`? | Flora is a domain lane under the domain-pipeline umbrella. | CONFIRMED path responsibility pattern; behavior NEEDS VERIFICATION |
| Why `validate/`? | This is a narrow executable sublane for validating normalized WORK candidates before processed/catalog handoff. | PROPOSED / NEEDS VERIFICATION |
| Is this normalize? | No. Normalization reshapes input; validation proves candidate conformance, evidence readiness, and fail-closed conditions. | CONFIRMED local separation |
| Does this own schemas or policy? | No. It consumes accepted contracts, schemas, and policy outcomes. | CONFIRMED authority separation |
| Can this sublane publish? | No. It may prepare validation reports and handoffs only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> Validation pass is not publication. A passing `ValidationReport` means a candidate met the validation contract for the checked scope; it still requires EvidenceBundle closure, catalog closure, release review, correction path, and rollback target before any public surface changes.

[⬆ Back to top](#top)

---

## 3. Validate anti-collapse rules

Flora validation must preserve normalized candidates, validation reports, processed records, catalog records, EvidenceBundles, policy decisions, and release artifacts as separate objects.

Disallowed collapses:

```text
validation pass -> public release
validation pass -> accepted botanical truth
ValidationReport -> EvidenceBundle
EvidenceRef -> EvidenceBundle
schema-valid object -> policy-approved object
normalized taxon string -> accepted PlantTaxon
specimen validation -> field occurrence validation
redaction candidate -> RedactionReceipt
catalog readiness -> catalog closure
processed handoff -> published artifact
generated validation summary -> evidence
pipeline run -> ReleaseManifest
```

Required distinctions:

- normalized WORK candidate, ValidationReport, processed candidate, quarantine record, EvidenceBundle, catalog record, release candidate, ReleaseManifest, CorrectionNotice, and RollbackCard remain separate;
- source roles are preserved and cannot be silently upgraded;
- original fields, normalized fields, taxon refs, temporal facets, geometry precision, sensitivity state, and evidence refs remain auditable;
- sensitive or rights-unclear material fails closed unless transform/review/policy artifacts resolve;
- every public claim resolves evidence or abstains.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable Flora validation.

Appropriate contents include:

- fixture-only validation dry-run entrypoints;
- schema/contract conformance checks that reference accepted schema homes;
- source descriptor, source-role, rights, and citation validators;
- taxon-identity readiness validators that do not decide taxonomy;
- object-role validators for taxa, occurrences, specimens, vegetation communities, phenology observations, range polygons, and invasive-plant records;
- geometry, temporal, CRS, uncertainty, and public-representation-state validators;
- sensitivity, review, policy, RedactionReceipt, and aggregation-receipt presence checks;
- EvidenceRef and EvidenceBundle readiness checks;
- quarantine reason-code routing helpers;
- `ValidationReport` builders and receipt emitters;
- handoff helpers for processed, catalog, triplet, and release workflows without owning those decisions.

A good placement test:

> If the code checks normalized Flora candidates and emits validation reports, processed-candidate handoffs, quarantine records, or receipts, it may belong here. If it fetches sources, admits sources, normalizes records, defines schemas, decides policy, writes catalog truth, approves release, or serves public API/map output, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Source fetchers and API clients | `connectors/<source>` or accepted connector home |
| Ingest routing / source admission | `pipelines/domains/flora/ingest/` |
| Normalization mappers | `pipelines/domains/flora/normalize/` |
| Redaction transform execution | `pipelines/domains/flora/redact/` |
| Catalog and triplet builders | `pipelines/domains/flora/catalog/` and lifecycle catalog/triplet homes |
| Flora doctrine and object meaning | `docs/domains/flora/`, `contracts/domains/flora/` |
| JSON Schemas | `schemas/contracts/v1/domains/flora/` or accepted schema home |
| Policy, rights, sensitivity, release rules | `policy/...` responsibility roots |
| Taxonomic authority decisions | Taxonomy contracts/registries and steward review roots |
| Declarative run specs | `pipeline_specs/flora/...` |
| Fixtures | `fixtures/domains/flora/validate/` or accepted fixture home |
| Tests | `tests/pipelines/domains/flora/validate/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Release decisions and manifests | `release/...` responsibility roots |

[⬆ Back to top](#top)

---

## 6. Validation scope

| Scope area | Validate responsibility | Failure behavior |
|---|---|---|
| Source identity | Confirm source id, descriptor ref, role, citation, rights, vintage, and input hashes are present. | Fail/hold or quarantine. |
| Schema/contract | Confirm candidate shape and object role match accepted contract. | Fail validation. |
| Taxon identity | Confirm taxon refs and uncertainty are explicit. | Hold or quarantine if unresolved. |
| Object role | Confirm occurrence/specimen/community/taxon/model/aggregate distinctions are preserved. | Fail on role collapse. |
| Geometry/time | Confirm CRS, uncertainty, temporal facets, public-representation state, and source/public split. | Hold or quarantine if unsafe. |
| Sensitivity | Confirm policy/review/receipt requirements for controlled material. | Fail closed. |
| Evidence | Confirm claim-bearing candidates can resolve EvidenceRef/EvidenceBundle requirements or abstain. | Hold if unresolved. |
| Handoff | Emit validation report and processed-candidate handoff only when all required gates close. | No direct catalog or publish. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Flora validation run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** approved fixtures, normalized WORK candidates, or approved QUARANTINE remediation records.
2. **Validate** source descriptor refs, source roles, rights, taxon identity readiness, object role, schema shape, temporal facets, geometry handling, sensitivity posture, evidence readiness, policy/review refs, and receipt refs.
3. **Emit** `ValidationReport` records with pass/fail/hold outcomes and deterministic reason codes.
4. **Route** failures or unresolved material to QUARANTINE with structured reasons.
5. **Prepare** processed-candidate handoffs only when validation closes; processed promotion remains governed and auditable.
6. **Never catalog or publish directly.**

Validation is the WORK-to-PROCESSED readiness gate. It is not catalog closure, release approval, or public serving.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Flora validation run must check or explicitly fail closed on:

1. **Input lifecycle gate** — input is normalized WORK, approved QUARANTINE remediation, or fixture-only material.
2. **SourceDescriptor gate** — source identity, source family, source role, rights, citation, and cadence/vintage are present.
3. **Schema/contract gate** — candidate validates against the accepted Flora contract shape.
4. **Source-role gate** — observed, regulatory, administrative, aggregate, modeled, candidate, synthetic, and generated-context records remain distinct.
5. **Taxon identity gate** — taxon refs, original taxon strings, accepted-name candidates, synonyms, and uncertainty are explicit.
6. **Object-role gate** — specimen, occurrence, taxon, vegetation community, range, phenology, invasive, and restoration candidates are not collapsed.
7. **Geometry/sensitivity gate** — controlled geometry has public-representation state, review expectation, and transform receipt where required.
8. **Temporal gate** — observed, valid, source-vintage, retrieval, processing, release, and correction times remain distinct.
9. **Evidence gate** — claim-bearing candidates resolve EvidenceRef/EvidenceBundle preconditions or abstain.
10. **Policy/review gate** — finite policy outcome and review state exist where materiality or sensitivity requires it.
11. **Receipt gate** — validation output includes deterministic input/output digests and reason codes.
12. **No-direct-catalog gate** — validation does not write catalog/triplet records as a side effect.
13. **No-direct-publish gate** — validation does not write public UI, public API, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/flora/validate/
├── README.md                         # this file
├── VALIDATE_CONTRACT.md              # PROPOSED: Flora validation execution contract
├── run_dry_fixture.py                # PROPOSED synthetic/generalized/redacted fixture only
├── validate_schema_contract.py       # PROPOSED
├── validate_source_descriptor.py     # PROPOSED
├── validate_source_role.py           # PROPOSED
├── validate_taxon_identity.py        # PROPOSED
├── validate_object_role.py           # PROPOSED
├── validate_geometry_temporal.py     # PROPOSED
├── validate_sensitivity_policy.py    # PROPOSED
├── validate_evidence_refs.py         # PROPOSED
├── build_validation_report.py        # PROPOSED
├── route_quarantine.py               # PROPOSED
├── emit_validation_receipt.py        # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/flora/validate.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use accepted lifecycle homes under `data/work/flora/`, `data/quarantine/flora/`, `data/processed/flora/`, and `data/receipts/` before downstream catalog, release, and published-layer roots.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/flora/validate/` or accepted fixture home | Synthetic, generalized, or redacted. |
| Normalized WORK input | `data/work/flora/<run_id>/` | Candidate from normalization; read by stable refs. |
| QUARANTINE remediation input | `data/quarantine/flora/<reason>/<run_id>/` | Only in explicit remediation mode. |
| ValidationReport | `data/processed/flora/<dataset_id>/<version>/` or accepted validation-report home | Report/handoff only; not public. |
| Processed candidate | `data/processed/flora/<dataset_id>/<version>/` | Only after governed validation and promotion. |
| QUARANTINE output | `data/quarantine/flora/<reason>/<run_id>/` | Failed, restricted, malformed, stale, or unresolved material. |
| Receipt | `data/receipts/pipeline/flora/validate/<run_id>.yml` or accepted receipt home | Records inputs, checks, reason codes, and output refs. |
| Downstream handoff | catalog/release sublanes | Handoff only; no publication by file move. |

[⬆ Back to top](#top)

---

## 11. Minimal validation report candidate

The final schema is not defined here. This example shows the minimum information a Flora validation report should preserve.

```yaml
schema_version: kfm.flora_validation_report.v1
validation_report_id: flora_validate_<source_id>_<object_role>_<hash>
pipeline_id: domains.flora.validate
run_id: run_YYYYMMDDThhmmssZ
status: HOLD
source:
  source_id: <source_id>
  source_descriptor_ref: data/registry/sources/flora/<source_id>.yml
  source_role: <observed|regulatory|administrative|aggregate|modeled|candidate|synthetic|generated_context>
  source_vintage: null
  rights_state: needs_review
candidate:
  work_ref: data/work/flora/<run_id>/normalized_candidate.yml
  object_role: <PlantTaxon|FloraOccurrence|Specimen|VegetationCommunity|PhenologyObservation|InvasivePlantRecord|RangePolygon>
checks:
  schema_contract_passed: false
  source_descriptor_resolved: false
  source_role_preserved: false
  taxon_identity_ready: false
  object_role_preserved: false
  geometry_temporal_valid: false
  sensitivity_policy_ready: false
  evidence_ready: false
  receipt_ready: false
failure:
  outcome: HOLD
  reason_codes: []
evidence:
  evidence_ref_candidates: []
  evidence_bundle_ready: false
policy:
  policy_decision_ref: null
  review_record_ref: null
anti_collapse:
  validation_pass_is_publication: false
  validation_report_is_evidence_bundle: false
  schema_valid_is_policy_approved: false
  normalized_taxon_string_is_accepted_taxon: false
outputs:
  validation_report_ref: data/processed/flora/<dataset_id>/<version>/validation_report.yml
  quarantine_ref: null
  receipt_ref: data/receipts/pipeline/flora/validate/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/generalized/redacted, and no-network** until validation specs, source descriptors, evidence, policy, sensitivity, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/flora/validate/
├── test_no_network_dry_run.py              # PROPOSED
├── test_normalized_work_input_required.py  # PROPOSED
├── test_source_descriptor_required.py      # PROPOSED
├── test_schema_contract_required.py        # PROPOSED
├── test_source_role_preserved.py           # PROPOSED
├── test_taxon_identity_ready_not_decided.py # PROPOSED
├── test_object_role_not_collapsed.py       # PROPOSED
├── test_geometry_temporal_facets.py        # PROPOSED
├── test_controlled_geometry_requires_transform_receipt.py # PROPOSED
├── test_evidence_ref_resolution_required.py # PROPOSED
├── test_policy_review_required.py          # PROPOSED
├── test_no_catalog_side_effect.py          # PROPOSED
├── test_receipt_hashes.py                  # PROPOSED
└── test_no_direct_publish.py               # PROPOSED
```

A dry run should prove fixtures load without network access, normalized WORK inputs are required, source descriptors and source roles are preserved, schema/contract checks run deterministically, taxon readiness does not become a taxonomic decision, controlled geometry fails closed, EvidenceRef readiness is explicit, receipts are deterministic, and no run writes directly to catalog, triplet, public UI, public API, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

Flora validation pipelines may prepare reports, processed-candidate handoffs, quarantine records, and receipts. They do not publish.

Required chain:

```text
normalized WORK candidate
  -> validation checks
  -> ValidationReport pass / hold / fail
  -> processed candidate or QUARANTINE hold
  -> EvidenceBundle closure
  -> catalog / triplet handoff
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public artifact
```

Correction and rollback posture:

- denied, held, failed, restricted, stale, conflicted, and quarantined validation runs remain auditable;
- receipts preserve source refs, source-role refs, taxon refs, original/normalized field refs, geometry/temporal refs, evidence refs, policy refs, check versions, and failure reasons;
- validation reports are superseded through governed state transitions, not hidden overwrite;
- downstream artifacts are invalidated if source refs, source-role refs, taxon refs, validation versions, EvidenceBundle refs, policy refs, correction refs, or rollback refs drift;
- release rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/flora/validate/README.md` file;
- identifies this directory as a nested executable Flora validation sublane;
- prevents connector, source-admission, normalization, source-profile, schema, contract, policy, fixture, test, data, proof, public API, UI, sensitivity-decision, catalog, and release authority from being placed here;
- preserves source descriptor, source family, source role, source vintage, taxon identity readiness, object role, geometry/temporal handling, EvidenceRef/EvidenceBundle readiness, policy/review state, lifecycle, quarantine, correction, and rollback boundaries;
- blocks validation-pass-as-publication, validation-report-as-EvidenceBundle, schema-valid-as-policy-approved, normalized-name-as-accepted-taxon, generated-summary-as-evidence, catalog side effects, and direct publication writes;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has source-descriptor fixtures, no-network tests, schema-backed validation reports, contract conformance, source-role/taxon/object-role/sensitivity/evidence/no-catalog/no-direct-publish tests, deterministic receipts, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `FLORA-VAL-001` | Should Flora validation remain one sublane, or split into taxon, occurrence, specimen, vegetation, phenology, range, and invasive-plant validators? | NEEDS VERIFICATION / ADR |
| `FLORA-VAL-002` | Which schema owns `ValidationReport`, validation reason codes, validation receipts, and processed-candidate handoff fields? | NEEDS VERIFICATION |
| `FLORA-VAL-003` | Which validator bundle is first-wave: source-role, schema, taxon, geometry/sensitivity, evidence, or all through a composed fixture? | NEEDS VERIFICATION |
| `FLORA-VAL-004` | Which CI job owns Flora validation invariant tests? | UNKNOWN |
| `FLORA-VAL-005` | Should EvidenceBundle construction begin during validation or wait for catalog closure? | NEEDS VERIFICATION / ADR |
| `FLORA-VAL-006` | Which transform receipt must exist before controlled Flora geometry can pass validation into PROCESSED? | NEEDS VERIFICATION |
| `FLORA-VAL-007` | What is the authoritative reason-code mapping between validation failure and Flora quarantine records? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic/generalized/redacted fixture-only dry runs and negative tests. Do not add live source fetching, ingest authority, normalization authority, source-profile editing, schema authority, policy authority, sensitivity-decision authority, accepted-taxonomy authority, direct catalog writes, direct public API code, direct UI code, release-manifest writes, public layer writes, or generated validation summaries until source roles, source descriptors, schema/contract checks, taxon readiness, EvidenceRef handling, policy review, deterministic receipts, and rollback expectations are proven.

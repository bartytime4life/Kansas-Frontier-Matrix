<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-hydrology-validate-readme
title: Hydrology Validate Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <hydrology-pipeline-owner>
  - <hydrology-domain-steward>
  - <validation-steward>
  - <evidence-steward>
  - <policy-steward>
  - <catalog-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipelines/domains/hydrology/validate/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/hydrology/README.md
  - pipelines/domains/hydrology/ingest/README.md
  - pipelines/domains/hydrology/normalize/README.md
  - pipelines/domains/hydrology/normalize_observation/README.md
  - pipelines/domains/hydrology/catalog/README.md
  - pipelines/domains/hydrology/catalog_close/README.md
  - docs/domains/hydrology/README.md
  - docs/domains/hydrology/DATA_LIFECYCLE.md
  - docs/domains/hydrology/PUBLICATION_POSTURE.md
  - pipeline_specs/hydrology/validate.yaml
  - contracts/domains/hydrology/
  - schemas/contracts/v1/domains/hydrology/
  - policy/domains/hydrology/
  - policy/sensitivity/hydrology/
  - data/work/hydrology/
  - data/quarantine/hydrology/
  - data/processed/hydrology/
  - data/catalog/domain/hydrology/
  - data/triplets/hydrology/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/hydrology/
  - release/manifests/hydrology/
tags:
  - kfm
  - pipelines
  - domains
  - hydrology
  - validate
  - validation
  - quality-gates
  - schema-validation
  - contract-validation
  - source-role
  - time-freshness
  - evidence-bundle
  - policy
  - quarantine
  - catalog-handoff
  - release-gated
  - governance
notes:
  - "This README fills the blank pipelines/domains/hydrology/validate path as a nested executable Hydrology validation sublane."
  - "Hydrology validate logic is executable validation support only; it does not own source descriptors, connectors, schemas, contracts, policy, lifecycle data, catalog truth, graph truth, release decisions, or public API authority."
  - "Validation is not ingest, normalization, processed-state promotion, catalog closure, release approval, or publication. It verifies whether normalized candidates may proceed or must abstain, deny, or quarantine."
  - "Observed readings, modeled hydrographs, regulatory context, official-source context, terrain/topology derivatives, aggregates, administrative records, and generated summaries must remain separate truth/support classes."
  - "Regulatory-context records must never validate as observed-condition records."
  - "Concrete executable behavior, schema linkage, schedules, CI coverage, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology Validate Pipeline

> Executable Hydrology sublane for validating normalized Hydrology candidates before processed-state, catalog, triplet, and release handoff — preserving source roles, evidence references, time/freshness state, units, QA, geometry, policy posture, correction path, and rollback targets without turning validation into promotion or publication.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-hydrology%20validate-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20validation%20logic-0a7ea4)
![source-role](https://img.shields.io/badge/source--role-preserved-d62728)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/hydrology/validate/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Hydrology  
**Sublane:** Validation / quality gates  
**Placement posture:** nested executable sublane under `pipelines/domains/hydrology/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Publication posture:** no direct publication; validated outputs require governed promotion, catalog/triplet handoff, release review, correction path, and rollback closure

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Validation anti-collapse rules](#3-validation-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Validation scope](#6-validation-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal validation report](#11-minimal-validation-report)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Promotion, publication, correction, and rollback](#13-promotion-publication-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/domains/hydrology/validate/` is the executable sublane for Hydrology validation after ingest and normalization have produced admitted candidates.

It supports validation for:

- watershed and HUC candidates;
- stream, reach, waterbody, gauge, well, station, and observation-site candidates;
- flow, stage, water-level, groundwater, water-quality, aquifer, hydrograph, and time-series candidates;
- regulatory-context candidates such as NFHL-derived records;
- terrain, topology, NHDPlus HR, WBD/HUC, USGS Water, 3DEP, and other admitted context candidates;
- source-role, knowledge-character, source-vintage, time/freshness, unit, parameter, QA, approval-state, geometry, CRS, datum, method, and evidence checks;
- validation reports, quarantine decisions, abstention records, denial records, receipts, processed-state handoff packages, catalog/triplet handoff packages, correction-path requirements, and rollback-target requirements.

This directory implements or will implement the **how** of Hydrology validation. It does not fetch source data, normalize raw source captures, define Hydrology object meaning, define schemas, encode policy, store lifecycle data, decide release, issue official notices, or decide regulatory meaning.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/hydrology/`? | Hydrology is the domain lane used by Hydrology docs and pipeline READMEs. | CONFIRMED documentation pattern; behavior NEEDS VERIFICATION |
| Why `validate/` here? | This is a narrow executable sublane for validating normalized Hydrology candidates before promotion and handoff. | PROPOSED / NEEDS VERIFICATION |
| Is this an ingest or normalize lane? | No. It consumes admitted/normalized candidates and emits validation outcomes. | PROPOSED |
| Does this own policy? | No. It evaluates against policy outcomes and policy refs but does not author policy. | CONFIRMED governance posture |
| Does this own schemas/contracts? | No. It can call validators against accepted schemas/contracts, but schema/contract authority stays in schema/contract roots. | CONFIRMED root separation |
| Can this sublane publish? | No. It may emit validation reports, quarantine outputs, and handoff packages only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> Validation is a gate, not a promotion. A passed validation report is not catalog truth, graph truth, release approval, or publication. A failed or incomplete validation must abstain, deny, quarantine, or return a reviewable remediation path.

[⬆ Back to top](#top)

---

## 3. Validation anti-collapse rules

Hydrology validation must preserve truth class, evidence state, and lifecycle state.

Disallowed collapses:

```text
validation pass -> processed-state promotion
validation pass -> catalog approval
validation pass -> release approval
validation report -> EvidenceBundle
normalized candidate -> canonical truth
observed reading -> modeled hydrograph
modeled output -> observed reading
regulatory context -> observed condition
administrative framework -> observed hydrology
terrain/topology derivative -> observed record
aggregate -> instantaneous observation
provisional value -> approved value
generated summary -> evidence
```

Required distinctions:

- source identity, source role, knowledge character, support class, lifecycle state, and review state are explicit;
- observed, modeled, regulatory, administrative, aggregate, derived, official-source context, and generated records remain distinct;
- observation time, valid time, source time, retrieval time, processing time, normalization time, validation time, catalog time, release time, and correction time remain distinct;
- schema/contract validity, evidence closure, policy outcome, sensitivity/public-safe transform, and rollback readiness are separate checks;
- validation failures are auditable and routed to quarantine or remediation rather than hidden overwrite.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable Hydrology validation.

Appropriate contents include:

- fixture-only validation entrypoints;
- schema and contract validator wrappers;
- source-role and knowledge-character validators;
- evidence-reference resolvability checks;
- policy-outcome presence checks;
- sensitivity/public-safe posture checks;
- time/freshness, unit, parameter, QA, approval-state, CRS, datum, geometry, topology, and method receipt validators;
- regulatory-context anti-collapse validators;
- observed/model/aggregate/admin/terrain/topology anti-collapse validators;
- validation report builders;
- quarantine, denial, abstention, and remediation routing helpers;
- receipt emitters, if not shared;
- handoff helpers for processed-state review, catalog, triplet, and release workflow.

A good placement test:

> If the code decides whether normalized Hydrology candidates may proceed to processed-state review, catalog/triplet handoff, or release review — and emits auditable validation reports and receipts — it may belong here. If it fetches source data, normalizes records, defines schemas, stores canonical records, writes catalog/triplet outputs, decides release, or exposes public API/map payloads, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Source fetchers / connectors | `connectors/<source>` or accepted connector home |
| Source-specific ingest code | `pipelines/domains/hydrology/ingest_*` or accepted ingest sublane |
| Normalization code | `pipelines/domains/hydrology/normalize/`, `normalize_observation/`, or accepted normalize sublane |
| Source catalog profiles | `docs/sources/catalog/...` |
| Source descriptors / source registry entries | `data/registry/sources/hydrology/` or approved registry home |
| Hydrology architecture and doctrine | `docs/domains/hydrology/...` |
| Object meaning contracts | `contracts/domains/hydrology/` or accepted contract home |
| JSON Schemas | `schemas/contracts/v1/domains/hydrology/` or accepted schema home |
| Policy, rights, sensitivity, release rules | `policy/...` responsibility roots |
| Declarative run specs | `pipeline_specs/hydrology/...` |
| Fixtures | `fixtures/domains/hydrology/validate/` or accepted fixture home |
| Tests | `tests/pipelines/domains/hydrology/validate/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Catalog/triplet builders or close checks | `pipelines/domains/hydrology/catalog/`, `pipelines/domains/hydrology/triplets/`, `pipelines/domains/hydrology/catalog_close/` |
| Receipts and proofs | `data/receipts/...`, `data/proofs/...` |
| Release decisions and manifests | `release/...` responsibility roots |
| Public API, map, or UI code | `apps/governed-api/`, `apps/explorer-web/`, packages |

[⬆ Back to top](#top)

---

## 6. Validation scope

| Scope area | Validation responsibility | Failure behavior |
|---|---|---|
| Input state | Confirm input is normalized candidate, fixture, or approved remediation input. | Deny or quarantine. |
| Source role | Confirm source role and knowledge class remain distinct. | Quarantine on collapse. |
| Schema/contract | Run accepted schema and contract checks. | Deny or quarantine on drift. |
| Evidence | Confirm EvidenceBundle refs resolve for claim-bearing candidates. | Abstain or quarantine if unresolved. |
| Policy | Confirm policy outcome exists and supports the requested handoff. | Deny on missing or failed policy. |
| Time/freshness | Validate observed, valid, source, retrieval, processing, normalization, validation, and stale states. | Quarantine on ambiguity. |
| Units/QA | Validate units, parameter codes, qualifiers, QA flags, and approval states. | Quarantine on ambiguity or collapse. |
| Geometry/topology | Validate CRS, datum, geometry lineage, topology refs, and source vintage. | Quarantine on mismatch. |
| Handoff readiness | Confirm correction path and rollback target expectations are available before release-facing handoff. | Deny release handoff. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Hydrology validation run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** approved fixtures, normalized work candidates, quarantine-remediation candidates, validation inputs, or processed baselines for revalidation.
2. **Validate** schema, contract, source role, evidence refs, policy refs, time/freshness state, units, QA, geometry, topology, sensitivity, public-safe posture, correction path, and rollback readiness.
3. **Emit** validation reports, receipts, quarantine records, abstention records, denial records, or handoff packages into accepted lifecycle homes.
4. **Quarantine** source-role collapse, missing EvidenceBundle, policy failure, schema drift, validation failure, stale source, time ambiguity, unit ambiguity, QA gaps, geometry drift, missing method receipt, missing correction path, or missing rollback target.
5. **Support promotion** only by providing reviewable validation evidence to downstream workflows.
6. **Never publish directly.**

Validation is an intermediate lifecycle gate. It is not promotion, catalog closure, release approval, or public artifact creation by itself.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Hydrology validation run must check or explicitly fail closed on:

1. **Input lifecycle gate** — input is normalized, fixture-only, quarantine-remediation, or explicitly revalidation material.
2. **Ingest/normalize receipt gate** — source-derived candidates have upstream receipt refs unless explicitly fixture-only.
3. **Source descriptor gate** — source identity, role, rights, cadence/freshness, and sensitivity posture are known.
4. **Schema/contract gate** — candidate conforms to accepted Hydrology schema and contract shape.
5. **Source-role gate** — observed, modeled, regulatory, administrative, official-source context, aggregate, derived, and generated records remain distinct.
6. **Regulatory-context gate** — regulatory-context records remain regulatory context, not observed-condition records.
7. **Evidence gate** — claim-bearing candidates resolve EvidenceBundle support or abstain.
8. **Policy gate** — finite policy outcome exists; no silent allow.
9. **Time/freshness gate** — observation, valid, source, retrieval, processing, normalization, validation, and stale states are explicit.
10. **Unit/QA gate** — variables, parameter codes, units, qualifiers, QA flags, approval states, and conversion refs are explicit.
11. **Geometry/CRS/topology gate** — geometry refs, CRS, datum, topology refs, and source vintage are explicit.
12. **Method receipt gate** — modeled, terrain, aggregate, rating, conversion, or reconstruction products carry method receipt refs.
13. **Correction/rollback gate** — correction path and rollback target expectations exist before release-facing handoff.
14. **No-direct-publish gate** — no writes to public UI, public API, published layers, or release manifests as a validation side effect.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/hydrology/validate/
├── README.md                         # this file
├── VALIDATION_CONTRACT.md            # PROPOSED: hydrology validation execution contract
├── run_dry_fixture.py                # PROPOSED synthetic/redacted fixture only
├── validate_schema_contract.py       # PROPOSED
├── validate_source_role.py           # PROPOSED
├── validate_evidence_refs.py         # PROPOSED
├── validate_policy_refs.py           # PROPOSED
├── validate_time_freshness.py        # PROPOSED
├── validate_units_qa.py              # PROPOSED
├── validate_geometry_topology.py     # PROPOSED
├── validate_method_receipts.py       # PROPOSED
├── build_validation_report.py        # PROPOSED
├── route_quarantine.py               # PROPOSED
├── emit_receipt.py                   # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/hydrology/validate.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use accepted lifecycle homes under `data/work/hydrology/`, `data/quarantine/hydrology/`, `data/processed/hydrology/`, catalog homes under `data/catalog/domain/hydrology/`, graph homes under `data/triplets/hydrology/`, proof homes under `data/proofs/`, receipt homes under `data/receipts/`, and release homes under `release/`.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/hydrology/validate/` or accepted fixture home | Synthetic, generalized, or redacted. |
| Normalized candidate input | `data/work/hydrology/<run_id>/` | Main validation input. |
| Quarantine remediation input | `data/quarantine/hydrology/<reason>/<run_id>/` | Remediation mode only. |
| Validation report | `data/work/hydrology/<run_id>/validation/` or approved report home | Reviewable output only. |
| Quarantine output | `data/quarantine/hydrology/<reason>/<run_id>/` | Failed or unresolved material. |
| Processed handoff candidate | `data/processed/hydrology/<dataset_id>/<version>/` | Only after downstream governed promotion gates. |
| Receipt | `data/receipts/pipeline/hydrology/validate/<run_id>.yml` or accepted receipt home | Records checks, inputs, outcomes, and handoff refs. |
| Evidence proof | `data/proofs/evidence_bundle/` or accepted proof home | Required for claim-bearing downstream records. |
| Release handoff | `release/candidates/hydrology/...` | Only through release workflow. |

[⬆ Back to top](#top)

---

## 11. Minimal validation report

The final schema is not defined here. This example shows the minimum information a Hydrology validation report should preserve.

```yaml
schema_version: kfm.hydrology_validation_report.v1
report_id: hydrology_validate_<candidate_id>_<run_id>_<hash>
pipeline_id: domains.hydrology.validate
run_id: run_YYYYMMDDThhmmssZ
status: VALIDATION_REPORT
candidate:
  candidate_id: <candidate_id>
  candidate_ref: data/work/hydrology/<run_id>/<candidate>.yml
  source_role: <observed|modeled|regulatory_context|administrative|aggregate|derived|generated_context>
  object_family: <watershed|huc_unit|reach|gauge|well|observation|regulatory_context|terrain_support|network_topology|modeled_hydrograph>
upstream_refs:
  ingest_receipt_ref: null
  normalize_receipt_ref: null
  evidence_bundle_ref: null
  policy_decision_ref: null
checks:
  schema_contract: <pass|fail|abstain>
  source_role: <pass|fail|abstain>
  evidence: <pass|fail|abstain>
  policy: <pass|fail|abstain>
  time_freshness: <pass|fail|abstain>
  units_qa: <pass|fail|abstain>
  geometry_topology: <pass|fail|abstain>
  method_receipts: <pass|fail|abstain>
anti_collapse:
  validation_is_promotion: false
  validation_is_release_approval: false
  regulatory_context_is_observed_condition: false
  generated_summary_is_evidence: false
outcome:
  decision: <pass_to_handoff|quarantine|deny|abstain|needs_review>
  reason_codes: []
outputs:
  validation_report_ref: data/work/hydrology/run_YYYYMMDDThhmmssZ/validation/<candidate_id>.yml
  receipt_ref: data/receipts/pipeline/hydrology/validate/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/generalized/redacted, and no-network** until validation spec, schema/contract refs, evidence, policy, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/hydrology/validate/
├── test_no_network_dry_run.py              # PROPOSED
├── test_upstream_receipts_required.py      # PROPOSED
├── test_schema_contract_required.py        # PROPOSED
├── test_source_role_preserved.py           # PROPOSED
├── test_regulatory_context_not_observed.py # PROPOSED
├── test_observed_not_modeled.py            # PROPOSED
├── test_evidence_bundle_required.py        # PROPOSED
├── test_policy_decision_required.py        # PROPOSED
├── test_time_fields_not_collapsed.py       # PROPOSED
├── test_units_qa_required.py               # PROPOSED
├── test_geometry_topology_required.py      # PROPOSED
├── test_method_receipt_required.py         # PROPOSED
├── test_validation_not_promotion.py        # PROPOSED
├── test_no_direct_publish.py               # PROPOSED
└── test_receipt_hashes.py                  # PROPOSED
```

A dry run should prove fixtures load without network access, upstream receipts are required for non-fixture inputs, schema/contract checks run, source roles are preserved, evidence and policy refs are required for claim-bearing candidates, validation does not promote or publish, receipts are deterministic, and failures route to abstain, deny, quarantine, or reviewable remediation.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

Hydrology validation may prepare validation reports and handoff packages. It does not publish.

Required promotion chain:

```text
normalized Hydrology candidate
  -> validation report
  -> governed promotion review
  -> processed Hydrology record
  -> catalog / triplet candidate
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> released artifact
```

Correction and rollback posture:

- denied, abstained, errored, restricted, stale, conflicted, and quarantined validation runs remain auditable;
- validation receipts preserve input hashes, upstream receipt refs, schema refs, evidence refs, source-role refs, policy outcomes, and failure reasons;
- validation reports are superseded by governed state transition, not hidden overwrite;
- downstream artifacts are invalidated if validation refs, EvidenceBundle refs, policy refs, source-role refs, schema refs, method refs, correction refs, or rollback refs drift;
- release rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/hydrology/validate/README.md` file;
- identifies this directory as a nested executable Hydrology validation sublane;
- prevents source fetcher, source-profile, ingest, normalize, schema, contract, policy, fixture, test, data, proof, catalog-store, graph-store, app, UI, and release authority from being placed here;
- preserves source role, knowledge character, schema/contract, evidence refs, policy refs, identity, time/freshness, units, QA, geometry/topology, method receipts, lifecycle, catalog/triplet, release, correction, and rollback boundaries;
- blocks validation-as-promotion, validation-as-release-approval, regulatory-context-as-observed, model-as-observation, generated-summary-as-evidence, and direct publication writes;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has normalized-candidate fixtures, schema-backed validation reports, contract conformance, source-role/evidence/policy/schema/time/unit/QA/geometry/no-direct-publish tests, deterministic receipts, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `HYDRO-VALIDATE-001` | Should Hydrology validation remain generic, or split into observation, regulatory-context, terrain/topology, and catalog-handoff validators? | NEEDS VERIFICATION / ADR |
| `HYDRO-VALIDATE-002` | Which schema owns validation reports, validation receipts, and quarantine reason codes? | NEEDS VERIFICATION |
| `HYDRO-VALIDATE-003` | Which first-wave families should validate first: WBD/HUC, USGS Water, NHDPlus HR, 3DEP terrain, or regulatory-context candidates? | NEEDS VERIFICATION |
| `HYDRO-VALIDATE-004` | Which CI job owns Hydrology validation invariant tests? | UNKNOWN |
| `HYDRO-VALIDATE-005` | Should validation reports live under `data/work/`, `data/processed/`, or a dedicated report home? | NEEDS VERIFICATION / ADR |
| `HYDRO-VALIDATE-006` | Which receipt type owns source-role, schema, evidence, policy, and method-receipt validation outcomes? | PROPOSED / NEEDS ADR |
| `HYDRO-VALIDATE-007` | Should catalog handoff be allowed from validation output directly, or only after governed processed-state promotion? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic/generalized fixture-only dry runs and negative tests. Do not add live source fetching, schema authority, policy authority, direct processed-state promotion, direct catalog writes, release-decision logic, public API code, UI code, or generated claim summaries until source roles, schemas, evidence refs, policy refs, validation receipts, correction, and rollback are proven.

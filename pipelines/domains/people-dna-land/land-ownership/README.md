<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-people-dna-land-land-ownership-readme
title: People DNA Land Land Ownership Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <people-dna-land-pipeline-owner>
  - <land-records-steward>
  - <people-dna-land-domain-steward>
  - <source-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: restricted-doctrine
path: pipelines/domains/people-dna-land/land-ownership/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/people-dna-land/README.md
  - docs/domains/people-dna-land/README.md
  - docs/domains/people-dna-land/ARCHITECTURE.md
  - docs/domains/people-dna-land/SENSITIVITY.md
  - docs/domains/people-dna-land/sublanes/land.md
  - docs/domains/people-dna-land/sublanes/land_ownership.md
  - docs/domains/people-dna-land/CHAIN_OF_TITLE_NOTES.md
  - docs/domains/people-dna-land/DATA_LIFECYCLE.md
  - docs/domains/people-dna-land/CANONICAL_PATHS.md
  - pipeline_specs/people-dna-land/
  - pipeline_specs/people-dna-land/land-ownership.yaml
  - contracts/domains/people-dna-land/
  - schemas/contracts/v1/domains/people-dna-land/
  - policy/domains/people-dna-land/
  - policy/sensitivity/people-dna-land/
  - data/raw/people-dna-land/
  - data/work/people-dna-land/
  - data/quarantine/people-dna-land/
  - data/processed/people-dna-land/
  - data/catalog/domain/people-dna-land/
  - data/triplets/people-dna-land/
  - data/registry/sources/people-dna-land/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/people-dna-land/
  - release/manifests/people-dna-land/
tags:
  - kfm
  - pipelines
  - domains
  - people-dna-land
  - land-ownership
  - deed
  - title-instrument
  - assessor-record
  - tax-record
  - parcel-version
  - legal-description
  - chain-of-title
  - assertion-first
  - evidence
  - policy
  - governance
notes:
  - "This README fills the blank pipelines/domains/people-dna-land/land-ownership path as a nested executable Land Ownership sublane."
  - "Land Ownership pipeline logic is executable implementation support only; it does not own source descriptors, source catalog profiles, schemas, policy, lifecycle data, catalog truth, title determinations, parcel-boundary determinations, or release decisions."
  - "Assessor/tax records are not title truth, and parcel geometry is not title-boundary proof."
  - "Land ownership is a temporal, evidence-bound assertion supported by instruments and review state, not a bare map label."
  - "Sensitive joins, unresolved rights, unsupported chain outputs, and over-broad public derivatives fail closed by default."
  - "Concrete executable behavior, source linkage, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Land Ownership Pipeline

> Executable People / DNA / Land sublane for normalizing admitted land instruments, assessor/tax context, parcel versions, legal descriptions, ownership intervals, and chain-of-title candidates into governed work records, quarantine records, validation handoffs, catalog/triplet handoffs, receipts, and release-review packages — without turning administrative records into title truth, parcel geometry into boundary proof, or ownership assertions into bare map labels.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-land%20ownership%20pipeline-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20logic-0a7ea4)
![title](https://img.shields.io/badge/title%20truth-not%20determined%20here-d62728)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/people-dna-land/land-ownership/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** People / Genealogy / DNA / Land Ownership  
**Sublane:** Land Ownership  
**Placement posture:** nested executable sublane under `pipelines/domains/people-dna-land/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no direct publication; public output requires lifecycle, EvidenceBundle, source-role, rights, sensitivity, policy, catalog/triplet, release, correction, and rollback closure

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Land ownership anti-collapse rules](#3-land-ownership-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Processing scope](#6-processing-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal candidate record](#11-minimal-candidate-record)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Promotion, publication, correction, and rollback](#13-promotion-publication-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/domains/people-dna-land/land-ownership/` is the executable sublane for Land Ownership processing inside the People / Genealogy / DNA / Land Ownership domain.

It supports candidate processing for:

- land ownership assertions;
- ownership intervals;
- deed instruments and title instruments as evidence;
- land instruments and legal-description references where admitted;
- assessor records and tax records as administrative context only;
- parcel versions and land parcel evidence-bound geometry references;
- chain-of-title candidates, gap reports, and contradiction reports;
- restricted relation handoffs that remain generalized, withheld, or denied until release review closes;
- catalog/triplet, Evidence Drawer, Focus Mode, correction, and rollback handoff packages.

This directory implements or will implement the **how** of Land Ownership candidate processing. It does not define object meaning, source descriptors, title truth, parcel-boundary truth, person identity truth, schemas, policy, lifecycle storage, catalog truth, or release approval.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/people-dna-land/`? | The whole-domain pipeline README identifies People / DNA / Land executable processing under this lane. | CONFIRMED documentation pattern; behavior NEEDS VERIFICATION |
| Why `land-ownership/`? | This is a narrow executable sublane for land-instrument and ownership-assertion processing. | PROPOSED / NEEDS VERIFICATION |
| Is this a source fetcher? | No. Fetching belongs in connectors or accepted source-edge homes. This sublane reads admitted lifecycle inputs or fixtures. | CONFIRMED separation |
| Where do declarative run specs live? | `pipeline_specs/people-dna-land/land-ownership.yaml` or accepted spec home. | PROPOSED / NEEDS VERIFICATION |
| Where do schemas and contracts live? | Whole-domain People/DNA/Land schema and contract homes unless an ADR establishes sublane split. | PROPOSED / NEEDS VERIFICATION |
| Can this sublane publish? | No. It may prepare candidates, validation handoffs, receipts, and release candidates only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> Land Ownership pipeline code is subordinate to source descriptors, source roles, rights, EvidenceBundle closure, sensitivity transforms, review state, policy decisions, release manifests, correction notices, and rollback cards. A successful run is not a title determination, boundary determination, public ownership label, or public release.

[⬆ Back to top](#top)

---

## 3. Land ownership anti-collapse rules

Land Ownership processing is assertion-first and evidence-bound.

Disallowed collapses:

```text
assessor record -> title truth
tax record -> title truth
parcel polygon -> boundary proof
current parcel id -> stable historical parcel identity
land instrument mention -> confirmed ownership
ownership assertion -> public map label
chain-of-title candidate -> title determination
sensitive relation join -> public fact
generated summary -> evidence
```

Required distinctions:

- source role is explicit for every input;
- party references, land instruments, legal descriptions, parcel versions, and ownership intervals remain distinct;
- instrument date, recording date, valid time, retrieval time, processing time, release time, and correction time remain distinct;
- assessor and tax records remain administrative context;
- parcel geometry is versioned evidence, not boundary proof;
- chain-of-title reasoning emits candidates, contradictions, gaps, and receipts, not determinations;
- public products require redaction, generalization, restriction, delay, denial, or release review where needed.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable Land Ownership processing.

Appropriate contents include:

- fixture-only dry-run entrypoints for land-ownership candidate processing;
- land-instrument normalizers;
- deed and title-instrument candidate builders;
- assessor/tax administrative-context normalizers;
- parcel-version normalizers;
- legal-description parsers and normalization helpers;
- ownership-interval candidate builders;
- chain-of-title candidate and contradiction builders;
- source-role anti-collapse validators;
- title/boundary overclaim validators;
- sensitivity and release-preflight validators;
- quarantine routing helpers for rights, identity, title, parcel, legal-description, temporal, source-role, evidence, or validation failures;
- receipt emitters, if not shared;
- catalog/triplet handoff helpers, if not centralized in `pipelines/catalog/`;
- thin adapters that read governed lifecycle inputs, not live source systems.

A good placement test:

> If the code transforms admitted People/DNA/Land lifecycle inputs into land ownership candidates, review handoffs, quarantine records, receipts, or catalog handoffs, it may belong here. If it fetches source data, defines legal meaning, decides title, decides boundaries, defines schemas, encodes policy, stores lifecycle data, creates public maps, or approves release, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Source fetchers / connectors | `connectors/<source>` or accepted connector home |
| Source catalog profiles | `docs/sources/catalog/...` |
| Source descriptors / source registry entries | `data/registry/sources/people-dna-land/` or accepted registry home |
| Land Ownership doctrine | `docs/domains/people-dna-land/sublanes/land.md` or ADR-selected doc home |
| Object meaning contracts | `contracts/domains/people-dna-land/` or accepted contract home |
| JSON Schemas | `schemas/contracts/v1/domains/people-dna-land/` or accepted schema home |
| Policy, sensitivity, rights, retention, and release rules | `policy/...` responsibility roots |
| Declarative run specs | `pipeline_specs/people-dna-land/...` |
| Fixtures | `fixtures/domains/people-dna-land/land-ownership/` or accepted fixture home |
| Tests | `tests/pipelines/domains/people-dna-land/land-ownership/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Receipts and proofs | `data/receipts/...`, `data/proofs/...` |
| Release decisions | `release/candidates/people-dna-land/`, `release/manifests/people-dna-land/`, rollback/correction release homes |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Title determination, boundary adjudication, or ownership certification | Outside KFM pipeline authority |
| Public-land office panels and aggregates | Frontier Matrix domain, cited into this lane when relevant |

[⬆ Back to top](#top)

---

## 6. Processing scope

| Scope area | Pipeline responsibility | Publication posture |
|---|---|---|
| Land instruments | Normalize instruments, roles, parties, dates, references, and evidence links. | Evidence only; not determination. |
| Deeds and title instruments | Build candidate instrument records and chain links. | Requires source role and evidence closure. |
| Legal descriptions | Parse and normalize text/location references with uncertainty. | Geometry conversion requires separate spatial review. |
| Assessor records | Normalize administrative context. | Never title truth. |
| Tax records | Normalize payment/delinquency context. | Never title truth. |
| Parcel versions | Normalize versioned parcel references and source vintage. | Geometry is administrative footprint, not boundary proof. |
| Ownership intervals | Build evidence-bound interval candidates. | Candidate until evidence and review close. |
| Chain-of-title reasoning | Build candidate chain, gap, contradiction, and evidence reports. | Not title determination. |
| Catalog/triplet handoff | Prepare restricted or public-safe candidates after evidence closure. | Projection does not replace canonical review state. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Land Ownership run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** approved synthetic/redacted fixtures, immutable raw captures, work candidates, quarantine inputs in remediation mode, or prior processed baselines.
2. **Normalize** into assertion-first candidates with source role, rights, party refs, instrument refs, legal-description refs, parcel-version refs, temporal scope, evidence refs, sensitivity posture, and receipt refs.
3. **Quarantine** unresolved rights, missing source role, restricted relation exposure, legal-description ambiguity, parcel/version ambiguity, unsupported title/boundary language, source contradiction, missing evidence, schema drift, or validation failure.
4. **Promote to processed** only after validation, policy, evidence, source-role, rights, sensitivity/public-safe transform, and review gates close.
5. **Prepare catalog/triplet handoffs** only after processed-state and evidence closure, and only with title/boundary caveats and sensitivity-safe payloads.
6. **Publish** only through release decisions, public-safe artifacts, rollback targets, and correction paths.

Promotion is a governed state transition with receipts and review evidence, not a file move.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Land Ownership run must check or explicitly fail closed on:

1. **Source descriptor gate** — every input has stable source identity, role, cadence/vintage, rights, and sensitivity posture.
2. **Source-role gate** — deed, title, assessor, tax, parcel, legal-description, instrument, derived, context, and generated records are not silently collapsed.
3. **Assessor/tax gate** — assessor and tax records remain administrative context, not title truth.
4. **Parcel geometry gate** — parcel geometry remains versioned administrative footprint, not boundary proof.
5. **Instrument gate** — land instruments are evidence and must not become determinations by pipeline output.
6. **Temporal gate** — instrument date, recording date, valid interval, source time, retrieval time, processing time, release time, and correction time remain distinct.
7. **Legal-description gate** — textual/legal descriptions remain cited, uncertain where applicable, and separate from geometry transforms.
8. **Party-reference gate** — party names and identity references remain assertion-bound and reviewable.
9. **Sensitivity gate** — restricted relation joins, precise derivatives, and unresolved review cases deny, restrict, or quarantine unless release review closes.
10. **Rights gate** — unknown or restrictive license, permission, attribution, privacy, or redistribution terms block public release.
11. **Chain-of-title gate** — chain outputs carry gaps, conflicts, support, and uncertainty; they do not certify title.
12. **AI/generation gate** — generated summaries remain downstream carriers and cannot replace evidence or review state.
13. **Schema, contract, evidence, policy, validation, receipt, catalog/triplet, and release gates** — all must close or the run abstains, denies, or quarantines.
14. **No-direct-publish gate** — no writes to public UI, public API, published layers, or release manifests without release workflow authority.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/people-dna-land/land-ownership/
├── README.md                         # this file
├── PIPELINE_CONTRACT.md              # PROPOSED: sublane execution contract
├── run_dry_fixture.py                # PROPOSED synthetic/redacted fixture only
├── normalize_land_instrument.py      # PROPOSED
├── normalize_deed_instrument.py      # PROPOSED
├── normalize_assessor_record.py      # PROPOSED
├── normalize_tax_record.py           # PROPOSED
├── normalize_parcel_version.py       # PROPOSED
├── parse_legal_description.py        # PROPOSED
├── build_ownership_interval.py       # PROPOSED
├── build_chain_of_title_candidate.py # PROPOSED
├── validate_title_boundary_claims.py # PROPOSED
├── validate_sensitivity_release.py   # PROPOSED
├── build_catalog_handoff.py          # PROPOSED if not centralized in pipelines/catalog/
├── emit_receipt.py                   # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/people-dna-land/land-ownership.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside the pipeline code. Use accepted lifecycle homes under `data/`, proof homes under `data/proofs/`, receipt homes under `data/receipts/`, and release homes under `release/`.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/people-dna-land/land-ownership/` or accepted fixture home | Synthetic, public-domain, generalized, or redacted. |
| Raw capture | `data/raw/people-dna-land/<source_id>/<run_id>/` | Immutable source-edge capture with descriptor and receipt. |
| Work candidate | `data/work/people-dna-land/<run_id>/` | Candidate only. |
| Quarantine record | `data/quarantine/people-dna-land/<reason>/<run_id>/` | Failed, restricted, unresolved, or unsafe material. |
| Processed restricted dataset | `data/processed/people-dna-land/<dataset_id>/<version>/` | Validated/restricted; not automatically public. |
| Catalog candidate | `data/catalog/domain/people-dna-land/...` or approved catalog home | After processed-state, transform, and evidence gates. |
| Triplet / graph delta | `data/triplets/people-dna-land/...` or approved graph-delta home | Projection only; does not replace canonical records. |
| Receipts / proofs | `data/receipts/...`, `data/proofs/...` | Required for auditable promotion and release review. |
| Release handoff | `release/candidates/people-dna-land/...` | Only through release workflow. |

[⬆ Back to top](#top)

---

## 11. Minimal candidate record

The final schema is not defined here. This example shows the minimum information a Land Ownership candidate should preserve.

```yaml
schema_version: kfm.land_ownership_pipeline_candidate.v1
candidate_id: pdl_land_<object_family>_<run_id>_<hash>
pipeline_id: domains.people-dna-land.land-ownership
run_id: run_YYYYMMDDThhmmssZ
status: WORK_CANDIDATE
object_family: <land_ownership_assertion|ownership_interval|deed_instrument|title_instrument|land_instrument|legal_description|assessor_record|tax_record|parcel_version|chain_of_title_candidate>
source_inputs:
  - source_id: <source_id>
    source_role: <recorded_instrument|administrative|tax|assessor|parcel_geometry|context|derived|synthetic|restricted>
    lifecycle_ref: data/raw/people-dna-land/<source_id>/<run_id>/
    input_hash: sha256:<hash>
    rights_state: needs_review
land_reference:
  legal_description_ref: null
  parcel_version_ref: null
  geometry_role: administrative_footprint_not_boundary_proof
temporal_scope:
  instrument_date: null
  recorded_at: null
  valid_start: null
  valid_end: null
  retrieved_at: YYYY-MM-DDThh:mm:ssZ
  processed_at: YYYY-MM-DDThh:mm:ssZ
anti_collapse:
  assessor_record_is_title_truth: false
  tax_record_is_title_truth: false
  parcel_geometry_is_boundary_proof: false
  chain_candidate_is_title_determination: false
  generated_summary_is_evidence: false
sensitivity:
  relation_join_risk: needs_review
  precise_derivative_risk: needs_review
  public_release_default: DENY_UNTIL_REVIEW
policy:
  outcome: ABSTAIN
  reason_code: RIGHTS_TITLE_BOUNDARY_SENSITIVITY_OR_EVIDENCE_NOT_RESOLVED
evidence:
  evidence_bundle_ref: null
  citation_state: ABSTAIN
outputs:
  candidate_record: data/work/people-dna-land/run_YYYYMMDDThhmmssZ/land_ownership_candidate.yml
  receipt: data/receipts/pipeline/people-dna-land/land-ownership/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/public-domain/generalized/redacted, and no-network** until source activation, rights review, sensitivity review, title/boundary review, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/people-dna-land/land-ownership/
├── test_no_network_dry_run.py                  # PROPOSED
├── test_source_role_required.py                # PROPOSED
├── test_assessor_not_title_truth.py            # PROPOSED
├── test_tax_not_title_truth.py                 # PROPOSED
├── test_parcel_geometry_not_boundary_proof.py  # PROPOSED
├── test_ownership_interval_temporal_scope.py   # PROPOSED
├── test_chain_candidate_not_title.py           # PROPOSED
├── test_restricted_join_denied.py              # PROPOSED
├── test_legal_description_uncertainty.py       # PROPOSED
├── test_missing_evidence_abstains.py           # PROPOSED
├── test_receipt_hashes.py                      # PROPOSED
└── test_no_direct_publish.py                   # PROPOSED
```

A dry run should prove fixtures load without network access, source roles are present, assessor/tax and parcel anti-collapse rules run, ownership intervals preserve time boundaries, restricted joins fail closed, EvidenceBundle gaps produce abstention, receipts are deterministic, and no run writes directly to public UI, public API, `data/published/`, or release manifests.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

Land Ownership pipelines may prepare candidates. They do not publish.

Required promotion chain:

```text
land instrument / assessor / tax / parcel source or work input
  -> land ownership candidate
  -> validation report
  -> policy decision
  -> title-boundary / public-safe transform receipt where required
  -> EvidenceBundle closure
  -> processed restricted People/DNA/Land dataset version
  -> catalog / triplet candidate
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public-safe artifact
```

Correction and rollback posture:

- denied, abstained, errored, restricted, conflicted, and quarantined runs remain auditable;
- candidate rollback preserves receipts and proof state;
- processed versions are superseded by governed state transition, not hidden overwrite;
- chain-of-title candidates are invalidated if source refs, instrument refs, parcel-version refs, party refs, policy refs, or evidence refs drift;
- public artifact rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/people-dna-land/land-ownership/README.md` file;
- identifies this directory as a nested executable Land Ownership sublane;
- prevents source fetcher, source-profile, schema, contract, policy, fixture, test, data, proof, catalog, and release authority from being placed here;
- preserves source role, instrument evidence, assessor/tax limits, parcel-version limits, legal-description uncertainty, ownership intervals, relation sensitivity, evidence, policy, lifecycle, catalog/triplet, release, correction, and rollback boundaries;
- blocks assessor-as-title, tax-as-title, parcel-as-boundary, chain-as-determination, public exposure of restricted joins, and generated-summary-as-evidence promotion;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has source-descriptor coverage, synthetic/public-domain/generalized/redacted no-network fixtures, schema-backed candidates, contract conformance, source-role/title-boundary/temporal/sensitivity/evidence tests, deterministic receipts, no-direct-publish tests, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `PDL-LAND-PIPE-001` | Should this subdirectory remain `land-ownership/`, or should all land executable helpers stay directly under `pipelines/domains/people-dna-land/` until sublane ADR resolution? | NEEDS VERIFICATION / ADR |
| `PDL-LAND-PIPE-002` | Which source-edge jobs own deed, assessor, tax, parcel, and instrument retrieval before this sublane reads lifecycle inputs? | NEEDS VERIFICATION |
| `PDL-LAND-PIPE-003` | Which first-wave object families are approved for fixture-only dry runs: instruments, assessor context, tax context, parcel versions, or ownership intervals? | NEEDS VERIFICATION |
| `PDL-LAND-PIPE-004` | Which schema owns land-ownership candidate and validation receipt fields? | NEEDS VERIFICATION |
| `PDL-LAND-PIPE-005` | Which CI job owns land-ownership invariant tests? | UNKNOWN |
| `PDL-LAND-PIPE-006` | Should catalog handoff logic live here or in centralized `pipelines/catalog/` with a People/DNA/Land adapter? | NEEDS VERIFICATION |
| `PDL-LAND-PIPE-007` | Which public-safe map/API products are allowed after review and release, and at what redaction/generalization level? | NEEDS VERIFICATION |
| `PDL-LAND-PIPE-008` | How should this sublane resolve overlap with duplicate docs `sublanes/land.md` and `sublanes/land_ownership.md`? | NEEDS ADR |

---

## Maintainer note

Start with synthetic/public-domain/redacted fixture-only dry runs and negative tests. Do not add live source fetching, public relation joins, title determinations, parcel-boundary claims, public map labels, release handoff automation, or direct API payload generation until source roles, rights, title-boundary anti-collapse, sensitivity review, evidence closure, and rollback are proven.

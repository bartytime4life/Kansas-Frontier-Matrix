<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-hydrology-ingest-nfhl-readme
title: Hydrology NFHL Ingest Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <hydrology-pipeline-owner>
  - <hydrology-domain-steward>
  - <fema-source-steward>
  - <hazards-domain-steward>
  - <source-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public-context-only; not-for-current-safety-guidance
path: pipelines/domains/hydrology/ingest_nfhl/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/hydrology/README.md
  - pipelines/domains/hydrology/ingest/README.md
  - pipelines/domains/hydrology/catalog/README.md
  - pipelines/domains/hydrology/catalog_close/README.md
  - docs/domains/hydrology/README.md
  - docs/domains/hydrology/DATA_LIFECYCLE.md
  - docs/domains/hydrology/PUBLICATION_POSTURE.md
  - docs/sources/catalog/fema/nfhl-flood-hazard.md
  - docs/sources/catalog/fema/map-service-center.md
  - docs/sources/catalog/fema/README.md
  - pipeline_specs/hydrology/ingest_nfhl.yaml
  - contracts/domains/hydrology/
  - schemas/contracts/v1/domains/hydrology/
  - policy/domains/hydrology/
  - policy/sensitivity/hydrology/
  - data/raw/hydrology/
  - data/work/hydrology/
  - data/quarantine/hydrology/
  - data/processed/hydrology/
  - data/catalog/domain/hydrology/
  - data/triplets/hydrology/
  - data/registry/sources/hydrology/
  - data/registry/sources/fema/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/hydrology/
  - release/manifests/hydrology/
tags:
  - kfm
  - pipelines
  - domains
  - hydrology
  - ingest
  - nfhl
  - fema
  - flood-hazard
  - regulatory-context
  - firm
  - dfirm-id
  - version-id
  - effective-date
  - bfe
  - vertical-datum
  - source-role
  - evidence
  - policy
  - governance
notes:
  - "This README fills the blank pipelines/domains/hydrology/ingest_nfhl path as a nested executable NFHL ingest sublane."
  - "NFHL ingest logic is executable implementation support only; it does not own FEMA source descriptors, source catalog profiles, connector/fetch logic, schemas, policy, lifecycle data, catalog truth, regulatory determinations, current guidance, or release decisions."
  - "The subdirectory name uses the requested underscore form ingest_nfhl; if repo slug rules prefer hyphenated names, record the path decision with ADR/path-map/rollback notes before moving."
  - "NFHL must ingest as regulatory context only, not observed inundation, not a predictive model, and not current safety guidance."
  - "Regulatory attributes such as DFIRM_ID, VERSION_ID, EFFECTIVE_DATE, flood zone designation, BFE, study references, and LOMR/LOMA references must be preserved verbatim where present."
  - "Vector REST analytic surfaces, WMS visualization surfaces, MSC panel snapshots, and KFM-derived layers remain separate support/role classes."
  - "Concrete executable behavior, source linkage, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# FEMA NFHL Hydrology Ingest Pipeline

> Executable Hydrology sublane for normalizing admitted FEMA National Flood Hazard Layer material into governed work candidates, quarantine records, validation handoffs, receipts, and downstream catalog/release-review packages — without collapsing regulatory flood-hazard context into observed flooding, forecasts, current guidance, engineering determinations, or public release approval.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-NFHL%20hydrology%20ingest-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20logic-0a7ea4)
![source-role](https://img.shields.io/badge/source--role-regulatory%20context-d62728)
![anti-collapse](https://img.shields.io/badge/NFHL%20%E2%89%A0%20observed%20flooding-d62728)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/hydrology/ingest_nfhl/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Hydrology  
**Sublane:** FEMA NFHL ingest / regulatory-context normalization  
**Placement posture:** nested executable sublane under `pipelines/domains/hydrology/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no direct publication; NFHL-derived output is work/quarantine/validation input only and requires downstream evidence, policy, catalog, release, correction, and rollback closure

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. NFHL anti-collapse rules](#3-nfhl-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Ingest scope](#6-ingest-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal NFHL ingest candidate record](#11-minimal-nfhl-ingest-candidate-record)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Promotion, publication, correction, and rollback](#13-promotion-publication-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/domains/hydrology/ingest_nfhl/` is the executable sublane for FEMA NFHL regulatory-context normalization inside the Hydrology domain.

It supports candidate processing for:

- NFHL feature-class snapshots and source-vintage metadata;
- flood-hazard area polygons as regulatory context;
- base-flood-elevation records where datum, units, and source refs are explicit;
- study lines, FIRM panel index links, community boundary context, and revision references where admitted;
- DFIRM, VERSION_ID, EFFECTIVE_DATE, flood zone designation, BFE, study reference, and LOMR/LOMA lineage fields where present;
- vector REST analytic input records and visualization-only WMS refs as separate access surfaces;
- MSC panel snapshot cross-refs without merging MSC and NFHL descriptors;
- quarantine records for missing source descriptor, missing regulatory attributes, vector/WMS collapse, MSC/NFHL collapse, BFE datum gaps, source-role collapse, schema drift, or validation failure;
- validation, catalog, triplet, EvidenceBundle, release-review, correction, and rollback handoff packages.

This directory implements or will implement the **how** of NFHL regulatory-context ingest. It does not fetch FEMA data directly, define FEMA source identity, define Hydrology object meaning, define schemas, encode policy, store lifecycle data, decide release, issue current safety guidance, decide regulatory outcomes, or certify engineering use.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/hydrology/`? | Hydrology is the domain lane used by Hydrology docs and the Hydrology pipeline README. | CONFIRMED documentation pattern; behavior NEEDS VERIFICATION |
| Why `ingest_nfhl/`? | This is a narrow executable sublane for FEMA NFHL regulatory-context input normalization. | PROPOSED / NEEDS VERIFICATION |
| Is this a connector? | No. Source fetching belongs in `connectors/fema/` or an accepted source-edge home. This sublane reads admitted lifecycle inputs or fixtures. | CONFIRMED separation |
| Does this own the NFHL source profile? | No. Source profile content lives under `docs/sources/catalog/fema/nfhl-flood-hazard.md` and source descriptors live in registry homes. | CONFIRMED source-doc separation |
| Does this replace MSC ingest? | No. FEMA MSC panel/FIS snapshots are companion source descriptors and must remain distinct from NFHL vector aggregates. | CONFIRMED source-role posture |
| Where do declarative run specs live? | `pipeline_specs/hydrology/ingest_nfhl.yaml` or accepted spec home. | PROPOSED / NEEDS VERIFICATION |
| Can this sublane publish? | No. It may emit work candidates, quarantine records, validation handoffs, and receipts only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> NFHL ingest is not publication, not observed flooding, not a flood forecast, not engineering certification, not current safety guidance, and not release approval. It prepares evidence-bound regulatory-context candidates for downstream validation and review.

[⬆ Back to top](#top)

---

## 3. NFHL anti-collapse rules

NFHL ingest must preserve regulatory-context semantics and FEMA source lineage.

Disallowed collapses:

```text
NFHL polygon -> observed inundation
NFHL zone -> current flood condition
NFHL regulatory baseline -> predictive model
NFHL WMS visualization -> analytic vector source
NFHL vector aggregate -> MSC FIRM panel snapshot
MSC panel snapshot -> NFHL vector aggregate
BFE value -> engineering claim without datum and units
zone code summary -> verbatim regulatory attribute
LOMR / LOMA reference -> untracked geometry overwrite
generated summary -> evidence
ingest receipt -> release approval
```

Required distinctions:

- NFHL source role is explicit as regulatory context;
- vector REST analytic inputs and WMS visualization refs remain separate;
- NFHL and MSC have separate source descriptors and lineage;
- DFIRM_ID, VERSION_ID, EFFECTIVE_DATE, zone designation, BFE, study reference, and LOMR/LOMA references are preserved where present;
- BFE and elevation use requires datum and unit checks before claim-bearing use;
- update/version events remain explicit and localized rather than one synthetic national release date;
- generated summaries and cartographic symbology never replace verbatim regulatory attributes or EvidenceBundle support.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable NFHL regulatory-context ingest normalization.

Appropriate contents include:

- fixture-only NFHL ingest entrypoints;
- NFHL feature-class metadata normalizers;
- flood-hazard polygon candidate builders;
- BFE, study-line, panel-index, community-context, and revision-reference normalizers;
- DFIRM_ID, VERSION_ID, EFFECTIVE_DATE, zone, BFE, study ref, and LOMR/LOMA verbatim-preservation validators;
- vector REST vs WMS access-surface validators;
- NFHL vs MSC companion-source validators;
- CRS, datum, elevation-unit, and geometry validators;
- source-role and regulatory-context anti-collapse validators;
- quarantine routing helpers for missing attributes, missing datum/units, missing descriptor, source-role collapse, geometry drift, or schema failures;
- receipt emitters, if not shared;
- handoff helpers for Hydrology validation, catalog, and triplet stages;
- thin adapters that read governed lifecycle inputs, not live FEMA endpoints.

A good placement test:

> If the code transforms admitted NFHL lifecycle inputs into Hydrology regulatory-context candidates, quarantine records, validation handoffs, receipts, or downstream handoff packages, it may belong here. If it fetches FEMA data, defines schemas, stores lifecycle data, decides public release, or claims observed flooding/regulatory determination, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| FEMA source fetchers / connectors | `connectors/fema/` or accepted connector home |
| NFHL source catalog profile | `docs/sources/catalog/fema/nfhl-flood-hazard.md` |
| FEMA MSC source profile | `docs/sources/catalog/fema/map-service-center.md` |
| Source descriptors / source registry entries | `data/registry/sources/fema/`, `data/registry/sources/hydrology/`, or approved registry home |
| Hydrology architecture and doctrine | `docs/domains/hydrology/...` |
| Hazards architecture and doctrine | `docs/domains/hazards/...` |
| Object meaning contracts | `contracts/domains/hydrology/` or accepted contract home |
| JSON Schemas | `schemas/contracts/v1/domains/hydrology/` or accepted schema home |
| Policy, rights, sensitivity, release rules | `policy/...` responsibility roots |
| Declarative run specs | `pipeline_specs/hydrology/...` |
| Fixtures | `fixtures/domains/hydrology/ingest_nfhl/` or accepted fixture home |
| Tests | `tests/pipelines/domains/hydrology/ingest_nfhl/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Catalog/triplet builders | `pipelines/domains/hydrology/catalog/`, `pipelines/catalog/`, or accepted graph/catalog adapter home |
| Catalog close / release preflight | `pipelines/domains/hydrology/catalog_close/` or release workflow homes |
| Receipts and proofs | `data/receipts/...`, `data/proofs/...` |
| Release decisions and manifests | `release/...` responsibility roots |
| Public API, map code, or public layers | `apps/governed-api/`, `apps/explorer-web/`, `data/published/...`, or release-controlled artifact homes |

[⬆ Back to top](#top)

---

## 6. Ingest scope

| Scope area | Ingest responsibility | Failure behavior |
|---|---|---|
| Source identity | Preserve FEMA/NFHL source id, source role, access surface, source version, and retrieval refs. | Quarantine if missing. |
| Regulatory attributes | Preserve DFIRM_ID, VERSION_ID, EFFECTIVE_DATE, zone, BFE, study refs, and revision refs where present. | Quarantine or abstain if missing for claim-bearing use. |
| Flood-hazard polygons | Normalize polygon candidates as regulatory context. | Deny if treated as observed event. |
| BFE/elevation records | Preserve datum, units, and source refs. | Abstain on elevation claim if datum/units unresolved. |
| WMS refs | Preserve as visualization-only refs. | Deny analytic use if WMS substituted for vector source. |
| MSC cross refs | Preserve companion descriptor links to FIRM/FIS snapshots. | Deny if merged into NFHL source identity. |
| Update events | Preserve effective dates, revision lineage, and localized update posture. | Quarantine if silently overwritten. |
| Hydrology/Hazards handoff | Prepare context candidates with domain ownership caveats. | No current safety guidance or event claim. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every NFHL ingest run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** approved fixtures, immutable raw captures, work inputs, quarantine inputs in remediation mode, or prior processed NFHL baselines.
2. **Normalize** into Hydrology regulatory-context work candidates with source role, access surface, regulatory attributes, geometry refs, CRS/datum/units, source vintage/effective date, evidence refs, policy refs, and receipt refs.
3. **Quarantine** missing source descriptor, missing regulatory attributes, NFHL/observed collapse, vector/WMS collapse, NFHL/MSC collapse, datum/unit ambiguity, geometry ambiguity, rights failure, schema drift, or validation failure.
4. **Emit receipts** with input refs, source refs, method refs, validation refs, original regulatory attributes, output refs, and outcomes.
5. **Support promotion** only by feeding downstream Hydrology validation and review workflows.
6. **Never publish directly.**

NFHL ingest is an early lifecycle transformation. It is not processed-state promotion, catalog closure, release approval, or public artifact creation by itself.

[⬆ Back to top](#top)

---

## 8. Required gates

Every NFHL ingest run must check or explicitly fail closed on:

1. **Input lifecycle gate** — input is fixture, raw capture, work input, quarantine-remediation input, or accepted baseline.
2. **Source descriptor gate** — FEMA NFHL source identity, source role, access surface, cadence/version, rights, and sensitivity posture are known.
3. **Source-role gate** — NFHL remains regulatory context and is never observed inundation, forecast, or current guidance.
4. **NFHL/MSC gate** — NFHL vector aggregate and MSC panel/FIS snapshots remain companion descriptors, not duplicates.
5. **Access-surface gate** — vector REST analytic inputs and WMS visualization refs are not interchanged.
6. **Attribute-preservation gate** — DFIRM_ID, VERSION_ID, EFFECTIVE_DATE, zone, BFE, study refs, and LOMR/LOMA refs are preserved where present.
7. **BFE/datum gate** — BFE or elevation use has explicit datum, unit, and transform posture.
8. **Geometry gate** — geometry refs, CRS, source vintage, and update lineage are explicit.
9. **Time/version gate** — effective date, source version, revision date, retrieval time, processing time, release time, and correction time remain distinct.
10. **Evidence gate** — claim-bearing downstream candidates can resolve evidence refs or abstain.
11. **Rights and sensitivity gate** — unresolved rights or restricted context cannot proceed to public-safe handoff.
12. **Schema/contract gate** — candidates match accepted schema and Hydrology semantics.
13. **No-direct-publish gate** — no writes to public UI, public API, catalog store, published layers, or release manifests as an ingest side effect.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/hydrology/ingest_nfhl/
├── README.md                         # this file
├── INGEST_CONTRACT.md                # PROPOSED: NFHL ingest execution contract
├── run_dry_fixture.py                # PROPOSED synthetic/redacted fixture only
├── normalize_nfhl_feature_class.py   # PROPOSED
├── normalize_flood_hazard_polygon.py # PROPOSED
├── normalize_bfe_record.py           # PROPOSED
├── normalize_panel_index_ref.py      # PROPOSED
├── normalize_revision_ref.py         # PROPOSED
├── validate_regulatory_attributes.py # PROPOSED
├── validate_vector_wms_boundary.py   # PROPOSED
├── validate_nfhl_msc_boundary.py     # PROPOSED
├── validate_bfe_datum_units.py       # PROPOSED
├── validate_regulatory_context.py    # PROPOSED
├── route_quarantine.py               # PROPOSED
├── emit_receipt.py                   # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/hydrology/ingest_nfhl.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside the ingest code. Use accepted lifecycle homes under `data/work/hydrology/`, `data/quarantine/hydrology/`, `data/processed/hydrology/`, proof homes under `data/proofs/`, receipt homes under `data/receipts/`, and release homes under `release/`.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/hydrology/ingest_nfhl/` or accepted fixture home | Synthetic, generalized, or redacted. |
| Raw NFHL capture | `data/raw/hydrology/<source_id>/<run_id>/` or accepted FEMA raw home | Immutable source-edge capture with descriptor and receipt. |
| Work candidate | `data/work/hydrology/<run_id>/` | Candidate only. |
| Quarantine record | `data/quarantine/hydrology/<reason>/<run_id>/` | Failed, restricted, unresolved, or unsafe material. |
| Processed context handoff | `data/processed/hydrology/<dataset_id>/<version>/` | Only after downstream validation and promotion gates. |
| Receipt | `data/receipts/pipeline/hydrology/ingest_nfhl/<run_id>.yml` or accepted receipt home | Records input refs, attributes, methods, checks, and outputs. |
| Evidence proof | `data/proofs/evidence_bundle/` or accepted proof home | Required for claim-bearing downstream records. |
| Catalog handoff | `pipelines/domains/hydrology/catalog/` via lifecycle data homes | No direct catalog writes from ingest unless approved by spec. |

[⬆ Back to top](#top)

---

## 11. Minimal NFHL ingest candidate record

The final schema is not defined here. This example shows the minimum information a NFHL ingest candidate should preserve.

```yaml
schema_version: kfm.hydrology_nfhl_ingest_candidate.v1
candidate_id: hydrology_nfhl_<feature_class>_<dfirm_or_digest>_<run_id>
pipeline_id: domains.hydrology.ingest_nfhl
run_id: run_YYYYMMDDThhmmssZ
status: WORK_CANDIDATE
object_family: <nfhl_zone|bfe_record|study_line|firm_panel_index|community_context|revision_reference>
source:
  source_id: fema_nfhl
  source_role: regulatory_context
  access_surface: <vector_rest|wms_visualization|bulk_snapshot|fixture>
  lifecycle_ref: data/raw/hydrology/fema_nfhl/<run_id>/
  input_hash: sha256:<hash>
  rights_state: needs_review
regulatory_attributes:
  dfirm_id: null
  version_id: null
  effective_date: null
  flood_zone: null
  bfe: null
  bfe_vertical_datum: null
  bfe_units: null
  study_ref: null
  lomr_loma_refs: []
geometry:
  geometry_ref: null
  crs: null
  source_vintage: null
anti_collapse:
  nfhl_is_observed_flooding: false
  nfhl_is_predictive_model: false
  wms_is_analytic_source: false
  msc_panel_is_nfhl_vector: false
  generated_summary_is_evidence: false
policy:
  outcome: ABSTAIN
  reason_code: SOURCE_DESCRIPTOR_REGULATORY_ATTRIBUTES_OR_EVIDENCE_NOT_RESOLVED
evidence:
  evidence_bundle_ref: null
  citation_state: ABSTAIN
outputs:
  candidate_record: data/work/hydrology/run_YYYYMMDDThhmmssZ/nfhl_candidate.yml
  receipt: data/receipts/pipeline/hydrology/ingest_nfhl/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/generalized/redacted, and no-network** until source activation, NFHL ingest spec, evidence, policy, sensitivity, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/hydrology/ingest_nfhl/
├── test_no_network_dry_run.py                 # PROPOSED
├── test_source_descriptor_required.py         # PROPOSED
├── test_source_role_regulatory_context.py     # PROPOSED
├── test_nfhl_not_observed_flooding.py         # PROPOSED
├── test_nfhl_not_predictive_model.py          # PROPOSED
├── test_vector_rest_not_wms.py                # PROPOSED
├── test_nfhl_msc_not_merged.py                # PROPOSED
├── test_regulatory_attributes_preserved.py    # PROPOSED
├── test_bfe_datum_units_required.py           # PROPOSED
├── test_effective_date_version_required.py    # PROPOSED
├── test_evidence_gap_abstains.py              # PROPOSED
├── test_quarantine_on_schema_failure.py       # PROPOSED
├── test_receipt_hashes.py                     # PROPOSED
└── test_no_direct_publish.py                  # PROPOSED
```

A dry run should prove fixtures load without network access, source descriptors and source roles are required, NFHL stays regulatory context, vector/WMS and NFHL/MSC boundaries hold, regulatory attributes remain verbatim, BFE claims require datum/units, EvidenceBundle gaps produce abstention, receipts are deterministic, and no run writes directly to public UI, public API, catalog store, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

NFHL ingest may prepare work candidates and quarantine records. It does not publish.

Required chain:

```text
admitted NFHL source capture
  -> NFHL regulatory-context ingest candidate
  -> validation report
  -> policy decision
  -> EvidenceBundle closure
  -> processed Hydrology regulatory-context record
  -> catalog / triplet candidate
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public-safe artifact
```

Correction and rollback posture:

- denied, abstained, errored, restricted, stale, conflicted, and quarantined NFHL ingest runs remain auditable;
- ingest receipts preserve source refs, access surface, regulatory attributes, version/effective-date refs, rule ids, and outcomes;
- processed versions are produced by governed promotion, not hidden overwrite;
- downstream artifacts are invalidated if source refs, version refs, effective-date refs, regulatory attributes, evidence refs, source-role refs, or policy refs drift;
- public artifact rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/hydrology/ingest_nfhl/README.md` file;
- identifies this directory as a nested executable Hydrology NFHL ingest sublane;
- prevents connector, source-profile, schema, contract, policy, fixture, test, data, proof, catalog, and release authority from being placed here;
- preserves FEMA source role, NFHL/MSC boundary, vector/WMS boundary, regulatory attributes, BFE datum/units, effective-date/version handling, evidence, policy, lifecycle, catalog/triplet, release, correction, and rollback boundaries;
- blocks NFHL-as-observed-flooding, NFHL-as-forecast, WMS-as-analytic-source, MSC-as-NFHL, BFE-without-datum, generated-summary-as-evidence, and direct catalog/release writes;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has source-descriptor coverage, synthetic/generalized/redacted no-network fixtures, schema-backed candidates, contract conformance, source-role/NFHL/MSC/BFE/evidence/policy/no-direct-publish tests, deterministic receipts, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `HYDRO-NFHL-001` | Should NFHL ingest remain Hydrology-specific, Hazards-specific, or shared with a domain adapter split? | NEEDS VERIFICATION / ADR |
| `HYDRO-NFHL-002` | Which source-edge job owns FEMA NFHL retrieval before this sublane reads lifecycle inputs? | NEEDS VERIFICATION |
| `HYDRO-NFHL-003` | Which first-wave feature classes are approved for fixture-only dry runs: flood hazard polygons, BFE lines/points, study lines, panel index, community boundaries, or revision refs? | NEEDS VERIFICATION |
| `HYDRO-NFHL-004` | Which schema owns NFHL regulatory-context candidates and quarantine reasons? | NEEDS VERIFICATION |
| `HYDRO-NFHL-005` | Which CI job owns NFHL ingest invariant tests? | UNKNOWN |
| `HYDRO-NFHL-006` | Should catalog handoff be forbidden as an ingest side effect, or allowed only through an explicit chained spec? | NEEDS VERIFICATION |
| `HYDRO-NFHL-007` | Which receipt type owns regulatory-attribute preservation, BFE datum checks, and NFHL/MSC cross-reference validation? | PROPOSED / NEEDS ADR |

---

## Maintainer note

Start with synthetic/generalized fixture-only dry runs and negative tests. Do not add live FEMA fetching, direct catalog writes, public layer writes, release-manifest writes, current safety guidance, engineering-use language, or direct API payload generation until source roles, regulatory attributes, datum/units, evidence closure, public-safe transforms, release review, and rollback are proven.

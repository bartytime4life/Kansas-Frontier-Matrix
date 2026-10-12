<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-flora-normalize-readme
title: Flora Normalize Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <flora-pipeline-owner>
  - <flora-domain-steward>
  - <taxonomy-steward>
  - <source-steward>
  - <evidence-steward>
  - <geoprivacy-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public-with-rare-flora-normalization-and-geoprivacy-gates
path: pipelines/domains/flora/normalize/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/flora/README.md
  - pipelines/domains/flora/ingest/README.md
  - pipelines/domains/flora/catalog/README.md
  - docs/domains/flora/README.md
  - docs/domains/flora/DATA_LIFECYCLE.md
  - docs/domains/flora/IDENTITY_MODEL.md
  - docs/domains/flora/CROSSWALKS.md
  - docs/domains/flora/SOURCES.md
  - docs/domains/flora/SOURCE_FAMILIES.md
  - docs/domains/flora/PUBLICATION_AND_ROLLBACK.md
  - pipeline_specs/flora/normalize.yaml
  - contracts/domains/flora/
  - schemas/contracts/v1/domains/flora/
  - policy/domains/flora/
  - policy/sensitivity/flora/
  - data/raw/flora/
  - data/work/flora/
  - data/quarantine/flora/
  - data/processed/flora/
  - data/catalog/domain/flora/
  - data/triplets/flora/
  - data/published/layers/flora/
  - data/registry/sources/flora/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/flora/
  - release/manifests/flora/
tags:
  - kfm
  - pipelines
  - domains
  - flora
  - normalize
  - plant-taxon
  - taxonomic-crosswalk
  - flora-occurrence
  - specimen
  - vegetation-community
  - rare-plants
  - geoprivacy
  - source-role
  - deterministic-identity
  - evidence
  - policy
  - governance
notes:
  - "This README fills the blank pipelines/domains/flora/normalize path as a nested executable Flora normalization sublane."
  - "Flora normalization logic is executable implementation support only; it does not own source descriptors, connectors, source profiles, schemas, contracts, policy, taxonomy authority, lifecycle data, catalog truth, geoprivacy decisions, or release decisions."
  - "Normalization converts admitted RAW/WORK/fixture inputs into structured WORK candidates and validation-ready records; it does not make accepted botanical truth or public-safe output by itself."
  - "Taxon-name normalization, accepted-name resolution, synonym crosswalks, occurrence normalization, specimen normalization, vegetation-community normalization, and redaction-token handling must preserve source role, evidence refs, uncertainty, and sensitivity posture."
  - "Rare, protected, culturally sensitive, steward-reviewed, join-sensitive, and rights-unclear flora records fail closed until geoprivacy, evidence, review, policy, correction, and rollback closure are present."
  - "Concrete executable behavior, source activation, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Flora Normalize Pipeline

> Executable Flora sublane for transforming admitted RAW/WORK/fixture flora source material into normalized, validation-ready Flora candidates — while preserving source identity, source role, taxonomic uncertainty, deterministic identity inputs, geometry/geoprivacy posture, rights, evidence refs, quarantine reasons, receipts, and downstream validation/release boundaries.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-flora%20normalize-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20normalize%20logic-0a7ea4)
![identity](https://img.shields.io/badge/identity-deterministic%20basis%20preserved-455a64)
![geoprivacy](https://img.shields.io/badge/rare%20flora-fail%20closed-d62728)
![publication](https://img.shields.io/badge/publication-no%20direct%20publish-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/flora/normalize/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Flora  
**Sublane:** Normalize / canonicalization-ready candidate shaping  
**Placement posture:** nested executable sublane under `pipelines/domains/flora/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no direct publication; normalized outputs remain work candidates, quarantine records, validation inputs, processed-candidate handoffs, or receipts until governed validation, catalog, release, correction, and rollback closure

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Normalize anti-collapse rules](#3-normalize-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Normalization scope](#6-normalization-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal normalized candidate record](#11-minimal-normalized-candidate-record)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Promotion, publication, correction, and rollback](#13-promotion-publication-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/domains/flora/normalize/` is the executable sublane for Flora normalization.

It supports candidate processing for:

- plant taxon-name and taxonomic-backbone normalization;
- accepted-name, synonym, rank, authority, and taxon-id candidate refs;
- Flora occurrence and specimen record normalization from admitted source captures;
- vegetation-community, invasive-plant, phenology, restoration, range, and distribution candidate shaping;
- source-role, source-vintage, citation, rights, geometry precision, temporal fields, and public-safe transform-state preservation;
- deterministic identity inputs such as source id, object role, temporal scope, and normalized digest candidate fields;
- redaction token, generalized geometry, aggregation key, and geoprivacy-state preservation;
- quarantine records for unresolved taxon names, source-role collapse, malformed fields, rights uncertainty, exact sensitive geometry, missing temporal fields, geometry/CRS ambiguity, schema drift, or validation failure;
- handoffs to validate, catalog, triplet, EvidenceBundle, release-review, correction, and rollback workflows.

This directory implements or will implement the **how** of Flora normalization. It does not fetch source data, define source descriptors, decide taxonomic truth, define schemas, encode policy, decide geoprivacy, store lifecycle data, create catalog truth, decide release, or publish public API/map payloads.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/flora/`? | Flora is a domain lane under the domain-pipeline umbrella. | CONFIRMED path responsibility pattern; behavior NEEDS VERIFICATION |
| Why `normalize/`? | This is a narrow executable sublane for converting admitted Flora inputs into normalized candidates. | PROPOSED / NEEDS VERIFICATION |
| Is this ingest? | No. Ingest admits and routes captures; normalization reshapes admitted material for validation. | CONFIRMED local separation |
| Does this own taxonomic authority? | No. It records candidate refs and uncertainty; steward/source evidence decides acceptance. | CONFIRMED identity posture |
| Does this own geoprivacy decisions? | No. It preserves/derives preflight state and fails closed when unresolved. | CONFIRMED sensitivity posture |
| Can this sublane publish? | No. It may prepare validation-ready candidates only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> A normalized Flora record is not accepted botanical truth. Normalization makes records comparable, validatable, evidence-linkable, and digestable; it does not prove a taxon, verify an occurrence, approve a redaction, or release a public layer.

[⬆ Back to top](#top)

---

## 3. Normalize anti-collapse rules

Flora normalization must preserve source identity, taxonomic uncertainty, evidence state, geoprivacy state, and lifecycle state.

Disallowed collapses:

```text
normalized record -> accepted Flora truth
source taxon string -> accepted PlantTaxon
synonym match -> taxonomic decision
specimen record -> field occurrence without basis
occurrence coordinate -> public exact geometry
generalized geometry -> original exact geometry
redaction token -> public-safe approval
source role hint -> final source role without SourceDescriptor
remote-sensing surface -> Flora occurrence truth
vegetation community candidate -> HabitatPatch truth
validation-ready candidate -> processed record
generated normalization summary -> evidence
pipeline run -> release approval
```

Required distinctions:

- source family, admitted source, source role, source-vintage, raw capture, work candidate, quarantine record, normalized candidate, validation report, processed object, catalog record, release candidate, and published artifact remain distinct;
- taxon strings, taxon ids, accepted-name refs, synonym refs, authority refs, and steward-review refs remain distinct;
- geometry precision, uncertainty radius, redaction/generalization/aggregation state, and original geometry state remain explicit;
- observed, valid, source-vintage, retrieval, processing, release, and correction time remain distinct;
- rare/protected/culturally sensitive/steward-reviewed/join-sensitive material defaults to quarantine, withholding, generalization, aggregation, staged review, or denial;
- every downstream claim resolves evidence or abstains.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable Flora normalization.

Appropriate contents include:

- fixture-only normalization dry-run entrypoints;
- source-to-normalized-field mappers;
- taxon-name cleanup helpers that preserve original strings;
- taxonomic-backbone candidate reference builders;
- synonym/crosswalk candidate attachment helpers;
- occurrence and specimen normalizers;
- vegetation-community, invasive-plant, phenology, restoration, range, and distribution normalizers;
- temporal, coordinate, CRS, uncertainty, basis-of-record, and source-vintage validators;
- geoprivacy/redaction/generalization/aggregation state preservation helpers;
- deterministic identity-field preparation helpers;
- quarantine routing helpers for unresolved taxon identity, rights uncertainty, geometry sensitivity, source-role collapse, schema drift, or malformed fields;
- receipt emitters, if not shared;
- handoff helpers for validation and catalog workflows.

A good placement test:

> If the code transforms admitted Flora RAW/WORK/fixture inputs into normalized WORK candidates, quarantine records, validation-ready handoffs, or receipts, it may belong here. If it fetches from an upstream, admits source captures, defines a SourceDescriptor, decides taxonomic truth, decides policy/geoprivacy/release, writes catalog truth, or serves public API/map output, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Upstream fetchers and API clients | `connectors/<source>` or accepted connector home |
| Ingest routing / source admission | `pipelines/domains/flora/ingest/` |
| Source-family profiles | `docs/domains/flora/SOURCE_FAMILIES.md` and source docs |
| Source descriptors / source registry entries | `data/registry/sources/flora/` or approved registry home |
| Flora doctrine and object meaning | `docs/domains/flora/`, `contracts/domains/flora/` |
| Taxonomic authority decisions | Taxonomy contracts/registries and steward review roots |
| JSON Schemas | `schemas/contracts/v1/domains/flora/` or accepted schema home |
| Policy, rights, sensitivity, geoprivacy, release rules | `policy/...` responsibility roots |
| Declarative run specs | `pipeline_specs/flora/...` |
| Fixtures | `fixtures/domains/flora/normalize/` or accepted fixture home |
| Tests | `tests/pipelines/domains/flora/normalize/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Catalog and triplet builders | `pipelines/domains/flora/catalog/`, `data/catalog/domain/flora/`, `data/triplets/flora/` |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Release decisions and manifests | `release/...` responsibility roots |

[⬆ Back to top](#top)

---

## 6. Normalization scope

| Scope area | Normalize responsibility | Failure behavior |
|---|---|---|
| Source identity | Preserve source id, source role, source family, source vintage, citation refs, and rights state. | Quarantine if missing or conflicting. |
| Taxon identity | Preserve original strings and attach candidate taxon refs without forcing acceptance. | Quarantine or mark needs review on ambiguity. |
| Object role | Preserve PlantTaxon, FloraOccurrence, Specimen, VegetationCommunity, PhenologyObservation, RangePolygon, and related object families. | Quarantine on role collapse. |
| Geometry | Normalize CRS/precision/uncertainty while preserving original/public geometry distinction. | Quarantine or restrict if sensitive. |
| Time | Preserve source, observed, valid, retrieval, processing, release, and correction times. | Quarantine on material collapse. |
| Evidence | Carry source refs and candidate EvidenceRef inputs forward. | Abstain if unresolved. |
| Geoprivacy | Preserve redaction/generalization/aggregation state and fail closed where unresolved. | Deny release-facing handoff. |
| Validation handoff | Emit validation-ready candidates with receipts. | No direct processed/catalog output. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Flora normalization run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** approved fixtures, admitted RAW captures, WORK candidates, or QUARANTINE remediation inputs with source identity and receipts.
2. **Normalize** fields into validation-ready Flora candidates while preserving original source fields, source refs, source roles, taxon strings, candidate authority refs, temporal facets, geometry precision, rights, sensitivity, and evidence refs.
3. **Prepare** deterministic identity inputs without claiming final identity/truth until validation and evidence closure.
4. **Quarantine** unresolved taxon names, source-role ambiguity, rights uncertainty, sensitive exact geometry, malformed payloads, missing temporal fields, join-induced sensitivity, and schema drift.
5. **Emit receipts** for every normalized, rejected, quarantined, or abstained normalization action.
6. **Never publish or catalog directly.**

Normalization is a WORK-stage shaping operation. It is not source admission, validation pass, catalog closure, or release.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Flora normalization run must check or explicitly fail closed on:

1. **Input lifecycle gate** — input is admitted RAW, WORK, approved QUARANTINE remediation, or fixture-only material.
2. **SourceDescriptor gate** — source identity, source family, source role, rights, citation, and cadence/vintage are present.
3. **Source-role gate** — observed, regulatory, administrative, aggregate, modeled, candidate, synthetic, and generated-context material remains distinct.
4. **Original-field preservation gate** — original taxon strings, source ids, coordinates, event dates, basis-of-record fields, and source labels remain recoverable.
5. **Taxon identity gate** — candidate accepted-name/synonym/authority refs are separate from accepted taxonomic truth.
6. **Geometry/geoprivacy gate** — exact rare/protected/culturally sensitive/steward-reviewed/join-sensitive geometry fails closed or carries restricted transform state.
7. **Temporal gate** — source, observed, valid, retrieval, processing, release, and correction times remain distinct.
8. **Identity-prep gate** — source id, object role, temporal scope, and normalized digest candidate fields are present before validation handoff.
9. **Evidence gate** — candidate evidence refs are preserved and unresolved support abstains.
10. **Quarantine reason gate** — every denied/held record has a structured reason code and receipt.
11. **No-direct-catalog gate** — normalization does not write catalog/triplet records as a side effect.
12. **No-direct-publish gate** — normalization does not write public UI, public API, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/flora/normalize/
├── README.md                         # this file
├── NORMALIZE_CONTRACT.md             # PROPOSED: Flora normalization execution contract
├── run_dry_fixture.py                # PROPOSED synthetic/generalized/redacted fixture only
├── normalize_taxon_name.py           # PROPOSED
├── normalize_taxon_crosswalk.py      # PROPOSED
├── normalize_occurrence.py           # PROPOSED
├── normalize_specimen.py             # PROPOSED
├── normalize_vegetation_community.py # PROPOSED
├── normalize_geometry_privacy.py     # PROPOSED
├── normalize_temporal_scope.py       # PROPOSED
├── prepare_identity_fields.py        # PROPOSED
├── route_quarantine.py               # PROPOSED
├── emit_normalize_receipt.py         # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/flora/normalize.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use accepted lifecycle homes under `data/work/flora/`, `data/quarantine/flora/`, and `data/receipts/` before downstream validation, processed, catalog, release, and published-layer roots.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/flora/normalize/` or accepted fixture home | Synthetic, generalized, or redacted. |
| RAW capture | `data/raw/flora/<source_id>/<run_id>/` | Immutable input; read only. |
| WORK input | `data/work/flora/<run_id>/` | Candidate from ingest or remediation. |
| Normalized WORK candidate | `data/work/flora/<run_id>/` | Validation-ready candidate; not processed truth. |
| QUARANTINE record | `data/quarantine/flora/<reason>/<run_id>/` | Failed, restricted, malformed, stale, or unresolved material. |
| Receipt | `data/receipts/pipeline/flora/normalize/<run_id>.yml` or accepted receipt home | Records inputs, normalization choices, checks, hashes, and output refs. |
| Downstream handoff | validate/catalog sublanes | Handoff only; no promotion by file move. |

[⬆ Back to top](#top)

---

## 11. Minimal normalized candidate record

The final schema is not defined here. This example shows the minimum information a Flora normalized candidate should preserve.

```yaml
schema_version: kfm.flora_normalized_candidate.v1
normalized_candidate_id: flora_normalized_<source_id>_<object_role>_<hash>
pipeline_id: domains.flora.normalize
run_id: run_YYYYMMDDThhmmssZ
status: WORK_CANDIDATE
source:
  source_id: <source_id>
  source_family: <gbif|idigbio|inaturalist|kdwp|usfws_ecos|natureserve|herbarium|other>
  source_role: <observed|regulatory|administrative|aggregate|modeled|candidate|synthetic|generated_context>
  source_descriptor_ref: data/registry/sources/flora/<source_id>.yml
  source_vintage: null
  rights_state: needs_review
object:
  object_role: <PlantTaxon|FloraOccurrence|Specimen|VegetationCommunity|PhenologyObservation|InvasivePlantRecord|RangePolygon>
  original_taxon_string: null
  candidate_taxon_refs: []
  accepted_taxon_ref: null
  acceptance_state: needs_review
identity_prep:
  temporal_scope: null
  normalized_digest_candidate: null
  identity_ready_for_validation: false
spatial_privacy:
  original_geometry_state: restricted
  public_geometry_state: <withheld|generalized|aggregated|staged|denied|public|not_applicable>
  public_safe_transform_ref: null
  coordinate_uncertainty: null
policy:
  outcome: ABSTAIN
  reason_code: TAXON_GEOPRIVACY_RIGHTS_OR_EVIDENCE_NOT_RESOLVED
evidence:
  evidence_ref_candidates: []
  citation_state: ABSTAIN
anti_collapse:
  normalized_is_accepted_truth: false
  taxon_name_string_is_taxon_identity: false
  generalized_geometry_is_exact_geometry: false
  source_role_hint_is_final_role: false
  generated_summary_is_evidence: false
outputs:
  work_ref: data/work/flora/run_YYYYMMDDThhmmssZ/normalized_candidate.yml
  quarantine_ref: null
  receipt_ref: data/receipts/pipeline/flora/normalize/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/generalized/redacted, and no-network** until normalization specs, source descriptors, evidence, policy, sensitivity, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/flora/normalize/
├── test_no_network_dry_run.py              # PROPOSED
├── test_source_descriptor_required.py      # PROPOSED
├── test_source_role_preserved.py           # PROPOSED
├── test_original_fields_preserved.py       # PROPOSED
├── test_taxon_name_not_identity.py         # PROPOSED
├── test_synonym_match_not_acceptance.py    # PROPOSED
├── test_temporal_facets_preserved.py       # PROPOSED
├── test_rare_flora_geoprivacy_preserved.py # PROPOSED
├── test_generalized_geometry_not_exact.py  # PROPOSED
├── test_identity_fields_prepared.py        # PROPOSED
├── test_malformed_payload_quarantines.py   # PROPOSED
├── test_no_catalog_side_effect.py          # PROPOSED
├── test_receipt_hashes.py                  # PROPOSED
└── test_no_direct_publish.py               # PROPOSED
```

A dry run should prove fixtures load without network access, source descriptors and source roles are required, original fields are preserved, taxon strings are not accepted identity, temporal facets are distinct, rare-flora geometry fails closed, receipts are deterministic, and no run writes directly to catalog, triplet, public UI, public API, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

Flora normalization pipelines may prepare normalized work candidates, quarantine records, validation handoffs, and receipts. They do not publish.

Required chain:

```text
admitted RAW / WORK / fixture input
  -> normalization checks
  -> normalized WORK candidate or QUARANTINE hold
  -> validation report
  -> EvidenceBundle closure
  -> processed Flora object
  -> catalog / triplet handoff
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public-safe artifact
```

Correction and rollback posture:

- denied, abstained, malformed, restricted, stale, conflicted, and quarantined normalization runs remain auditable;
- receipts preserve source refs, source-role refs, original fields, normalized fields, taxon refs, geoprivacy refs, evidence refs, payload hashes, parser/normalizer refs, and failure reasons;
- normalized candidates are superseded through governed state transitions, not hidden overwrite;
- downstream artifacts are invalidated if source refs, source-role refs, taxon refs, temporal scopes, normalized digest inputs, EvidenceBundle refs, geoprivacy refs, policy refs, review refs, correction refs, or rollback refs drift;
- release rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/flora/normalize/README.md` file;
- identifies this directory as a nested executable Flora normalization sublane;
- prevents connector, ingest/source-admission, source-profile, schema, contract, policy, fixture, test, data, proof, public API, UI, geoprivacy decision, catalog, and release authority from being placed here;
- preserves source descriptor, source family, source role, source vintage, original fields, normalized fields, taxon-name uncertainty, candidate taxon refs, temporal scope, identity-prep fields, geometry/geoprivacy posture, lifecycle, quarantine, evidence, policy, correction, and rollback boundaries;
- blocks normalized-record-as-truth, taxon-name-as-identity, synonym-as-acceptance, generalized-geometry-as-exact, generated-summary-as-evidence, catalog side effects, and direct publication writes;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has source-descriptor fixtures, no-network tests, schema-backed normalized candidates, contract conformance, source-role/original-field/taxon/geoprivacy/identity-prep/no-catalog/no-direct-publish tests, deterministic receipts, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `FLORA-NORM-001` | Should Flora normalization remain one sublane, or split into taxon, occurrence, specimen, vegetation, phenology, range, and invasive-plant normalizers? | NEEDS VERIFICATION / ADR |
| `FLORA-NORM-002` | Which normalized candidate schema owns object-role-specific fields and quarantine reason codes? | NEEDS VERIFICATION |
| `FLORA-NORM-003` | Which taxonomic authority backbone is first-wave for fixture-only dry runs: USDA PLANTS, GBIF Backbone, ITIS, WFO, NatureServe, or synthetic taxonomy? | NEEDS VERIFICATION |
| `FLORA-NORM-004` | Which CI job owns Flora normalization invariant tests? | UNKNOWN |
| `FLORA-NORM-005` | Which geoprivacy preflight is required before exact flora geometry can become validation-ready instead of quarantined? | NEEDS VERIFICATION |
| `FLORA-NORM-006` | Which deterministic identity hash policy should choose normalized digest fields for each Flora object family? | NEEDS VERIFICATION / ADR |
| `FLORA-NORM-007` | Should normalization produce EvidenceRef candidates, or should that wait until validation/catalog closure? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic/generalized/redacted fixture-only dry runs and negative tests. Do not add live source fetching, ingest authority, source-profile editing, schema authority, policy authority, geoprivacy-decision authority, accepted-taxonomy authority, direct catalog writes, direct public API code, direct UI code, release-manifest writes, public layer writes, or generated botanical summaries until source roles, source descriptors, original-field preservation, taxon identity handling, geoprivacy preflight, deterministic receipts, review state, and rollback are proven.

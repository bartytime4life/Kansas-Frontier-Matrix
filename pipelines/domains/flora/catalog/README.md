<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-flora-catalog-readme
title: Flora Catalog Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <flora-pipeline-owner>
  - <flora-domain-steward>
  - <catalog-steward>
  - <taxonomy-steward>
  - <evidence-steward>
  - <geoprivacy-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public-with-rare-flora-geoprivacy-gates
path: pipelines/domains/flora/catalog/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/flora/README.md
  - docs/domains/flora/README.md
  - docs/domains/flora/DATA_LIFECYCLE.md
  - docs/domains/flora/PUBLICATION_AND_ROLLBACK.md
  - docs/domains/flora/IDENTITY_MODEL.md
  - docs/domains/flora/SOURCES.md
  - docs/domains/flora/SOURCE_FAMILIES.md
  - docs/domains/flora/CROSSWALKS.md
  - pipeline_specs/flora/catalog.yaml
  - contracts/domains/flora/
  - schemas/contracts/v1/domains/flora/
  - policy/domains/flora/
  - policy/sensitivity/flora/
  - data/processed/flora/
  - data/catalog/domain/flora/
  - data/triplets/flora/
  - data/quarantine/flora/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/flora/
  - release/manifests/flora/
tags:
  - kfm
  - pipelines
  - domains
  - flora
  - catalog
  - catalog-handoff
  - evidence-bundle
  - plant-taxon
  - flora-occurrence
  - specimen
  - vegetation-community
  - geoprivacy
  - sensitive-species
  - source-role
  - policy
  - governance
notes:
  - "This README fills the blank pipelines/domains/flora/catalog path as a nested executable Flora catalog-handoff sublane."
  - "Flora catalog logic is executable catalog support only; it does not own source descriptors, connectors, schemas, policy, lifecycle data, graph truth, EvidenceBundle truth, release decisions, geoprivacy decisions, or public API authority."
  - "Catalog records are downstream carriers from processed Flora records and EvidenceBundle refs; they are not canonical botanical truth and are not public release by themselves."
  - "Rare, protected, culturally sensitive, steward-reviewed, join-sensitive, and unresolved flora records fail closed until geoprivacy, review, evidence, policy, correction, and rollback closure are present."
  - "Flora may reference Habitat, Fauna, Soil, Hydrology, Agriculture, and Hazards context, but cross-lane ownership and EvidenceBundle support must remain visible."
  - "Concrete executable behavior, source activation, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Flora Catalog Pipeline

> Executable Flora sublane for preparing governed catalog records, EvidenceBundle handoffs, STAC/DCAT/PROV-style metadata candidates, graph handoff references, receipts, and release-review packages from processed Flora objects — without turning catalog metadata into botanical truth, geoprivacy approval, release approval, or public map/API output.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-flora%20catalog-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20catalog%20logic-0a7ea4)
![geoprivacy](https://img.shields.io/badge/rare%20flora-fail%20closed-d62728)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/flora/catalog/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Flora  
**Sublane:** Catalog / EvidenceBundle handoff  
**Placement posture:** nested executable sublane under `pipelines/domains/flora/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no direct publication; catalog outputs require lifecycle, EvidenceBundle, source-role, geoprivacy/sensitivity transform, review, policy, correction, release, and rollback closure before public use

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Catalog anti-collapse rules](#3-catalog-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Catalog scope](#6-catalog-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal catalog candidate record](#11-minimal-catalog-candidate-record)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Promotion, publication, correction, and rollback](#13-promotion-publication-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/domains/flora/catalog/` is the executable sublane for Flora catalog preparation.

It supports candidate processing for:

- processed `PlantTaxon`, `FloraOccurrence`, `Specimen`, `VegetationCommunity`, invasive-plant, phenology, restoration, range, and distribution records;
- catalog records that preserve source ids, source roles, taxonomic identity refs, validation refs, public-safe transform refs, EvidenceBundle refs, geoprivacy refs, review refs, policy refs, correction refs, and rollback refs;
- STAC/DCAT/PROV-style metadata where an accepted contract exists;
- catalog matrix and release-candidate handoff packages;
- triplet/graph projection handoff refs without making graph truth;
- Evidence Drawer and Focus Mode metadata handoffs without exposing internal stores;
- quarantine records for missing EvidenceBundle, missing taxon identity, source-role collapse, unresolved geoprivacy, unresolved rights, unresolved review, policy failure, schema drift, stale source, or validation failure.

This directory implements or will implement the **how** of Flora catalog handoff. It does not fetch source data, normalize raw records, define Flora object meaning, define schemas, encode policy, decide geoprivacy, own EvidenceBundle truth, store catalog truth as authority, decide release, or publish public API/map payloads.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/flora/`? | Flora is a domain lane under the domain-pipeline umbrella. | CONFIRMED path responsibility pattern; behavior NEEDS VERIFICATION |
| Why `catalog/`? | This is a narrow executable sublane for catalog and EvidenceBundle handoff preparation. | PROPOSED / NEEDS VERIFICATION |
| Does this own catalog truth? | No. It prepares reviewable catalog candidates and receipts; catalog state is governed by lifecycle and release controls. | CONFIRMED governance posture |
| Does this own geoprivacy decisions? | No. It consumes geoprivacy/policy/review outputs and fails closed when they are unresolved. | CONFIRMED sensitivity posture |
| Can this sublane publish? | No. It may prepare catalog/release handoffs only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> A Flora catalog record is not a public record by default. Exact rare-plant, protected, culturally sensitive, steward-reviewed, or join-sensitive geometry must not pass catalog handoff without public-safe transform, EvidenceBundle, review, policy, correction, and rollback refs.

[⬆ Back to top](#top)

---

## 3. Catalog anti-collapse rules

Catalog processing must preserve source role, evidence state, geoprivacy, review state, lifecycle state, and release state.

Disallowed collapses:

```text
catalog record -> botanical truth
catalog candidate -> public layer
EvidenceRef -> EvidenceBundle
redacted geometry -> original exact geometry
public-safe transform -> geoprivacy approval
taxon name string -> accepted taxon identity
specimen record -> field occurrence without basis
community polygon -> habitat truth without owning-domain refs
flora occurrence -> fauna/habitat/soil/hydrology truth
watcher event -> catalog record
validation pass -> release approval
generated summary -> evidence
```

Required distinctions:

- source identity, source role, taxonomic identity, observation/specimen/community class, geometry precision, sensitivity tier, public-safe transform, evidence refs, policy refs, and review refs are explicit;
- processed record, catalog candidate, EvidenceBundle, graph projection, release candidate, ReleaseManifest, and RollbackCard remain distinct;
- rare/protected/culturally sensitive flora defaults to withheld, generalized, delayed, staged, or denied public geometry;
- cross-lane joins preserve the owning domain and cannot import another domain's truth into Flora;
- every public claim resolves evidence or abstains;
- release requires correction path and rollback target.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable Flora catalog handoff.

Appropriate contents include:

- fixture-only catalog dry-run entrypoints;
- catalog candidate builders for processed Flora objects;
- EvidenceBundle reference and digest-closure validators;
- taxon-identity, synonym, source-role, and source-vintage checks for catalog metadata;
- geoprivacy, redaction, generalization, and public-safe transform validators;
- policy/review-state presence checks;
- catalog matrix builders and catalog receipt emitters;
- triplet/graph handoff reference builders without graph authority;
- release-candidate handoff package builders without release authority;
- quarantine routing helpers for missing evidence, unresolved taxon identity, unresolved geoprivacy, policy failure, stale source, or schema drift.

A good placement test:

> If the code transforms processed Flora records and evidence refs into reviewable catalog candidates, catalog receipts, graph handoff refs, or release-candidate handoff packages, it may belong here. If it fetches source data, normalizes occurrence records, defines schemas, decides policy/geoprivacy/release, writes public artifacts, or serves API/map payloads, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Source fetchers / connectors | `connectors/<source>` or accepted connector home |
| Source descriptors / source registry entries | `data/registry/sources/flora/` or approved registry home |
| Flora doctrine and object meaning | `docs/domains/flora/`, `contracts/domains/flora/` |
| JSON Schemas | `schemas/contracts/v1/domains/flora/` or accepted schema home |
| Policy, rights, sensitivity, geoprivacy, release rules | `policy/...` responsibility roots |
| Declarative run specs | `pipeline_specs/flora/...` |
| Fixtures | `fixtures/domains/flora/catalog/` or accepted fixture home |
| Tests | `tests/pipelines/domains/flora/catalog/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Taxonomic authority decisions | Taxonomy contracts/registries and steward review roots |
| Habitat patches, fauna occurrences, soils, hydrology, agriculture, hazards, archaeology, or land truth | Owning domain roots |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Release decisions and manifests | `release/...` responsibility roots |

[⬆ Back to top](#top)

---

## 6. Catalog scope

| Scope area | Catalog responsibility | Failure behavior |
|---|---|---|
| Processed input | Confirm input is processed Flora material or accepted fixture. | Deny or quarantine. |
| Taxon identity | Preserve accepted taxon refs, synonyms, authority refs, and uncertainty. | Abstain or quarantine on unresolved identity. |
| Evidence | Resolve EvidenceBundle refs for claim-bearing records. | Abstain or quarantine if unresolved. |
| Source role | Preserve occurrence, specimen, checklist, taxonomic, stewarded, model, aggregate, and generated-context distinctions. | Quarantine on collapse. |
| Geoprivacy | Preserve exact/private geometry protection and public-safe transform refs. | Deny release-facing handoff if unresolved. |
| Cross-lane refs | Preserve owning-domain refs for Habitat/Fauna/Soil/Hydrology/Agriculture/Hazards joins. | Deny if join becomes Flora truth. |
| Catalog metadata | Emit STAC/DCAT/PROV-like metadata only under accepted contract. | Quarantine on schema drift. |
| Release readiness | Check correction path and rollback target expectations. | Deny release handoff if missing. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Flora catalog run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** approved fixtures, processed Flora records, validation reports, public-safe transform refs, EvidenceBundle refs, review records, policy decisions, correction refs, and rollback refs.
2. **Validate** taxon identity, source role, evidence closure, geoprivacy, sensitivity, rights, review state, policy outcome, cross-lane ownership, stale state, correction path, and rollback target.
3. **Emit** catalog candidates, catalog receipts, graph/triplet handoff refs, or release-candidate handoff packages into accepted lifecycle homes.
4. **Quarantine** missing EvidenceBundle, missing source role, unresolved taxon identity, unresolved geoprivacy, rights failure, sensitivity failure, policy failure, stale source, schema drift, or cross-lane ownership collapse.
5. **Support release** only by providing reviewable handoff packages to release workflow.
6. **Never publish directly.**

Catalog is a governed lifecycle handoff, not publication and not a file move.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Flora catalog run must check or explicitly fail closed on:

1. **Input lifecycle gate** — input is processed Flora material, fixture-only material, or approved re-catalog material.
2. **Validation report gate** — upstream validation refs exist and pass or state a reviewable exception.
3. **EvidenceBundle gate** — claim-bearing catalog records resolve EvidenceBundle support.
4. **Taxon identity gate** — accepted taxon refs, synonym refs, authority refs, and uncertainty are explicit.
5. **Source-role gate** — occurrence/specimen/taxonomic/checklist/model/aggregate/generated distinctions remain distinct.
6. **Geoprivacy gate** — exact rare/protected/culturally sensitive/steward-reviewed records have withheld/generalized/staged/denied posture.
7. **Policy/review gate** — finite policy outcome and review state exist; no silent allow.
8. **Public-safe transform gate** — release-facing records have redaction/generalization/aggregation receipts where needed.
9. **Cross-lane ownership gate** — joins do not become Habitat, Fauna, Soil, Hydrology, Agriculture, Hazards, Archaeology, or People/Land truth.
10. **Schema/contract gate** — catalog candidates match accepted metadata contract and Flora semantics.
11. **Correction/rollback gate** — release-facing handoff includes correction path and rollback target expectations.
12. **No-direct-publish gate** — no writes to public UI, public API, published layers, or release manifests as a catalog side effect.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/flora/catalog/
├── README.md                         # this file
├── CATALOG_CONTRACT.md               # PROPOSED: Flora catalog execution contract
├── run_dry_fixture.py                # PROPOSED synthetic/generalized/redacted fixture only
├── build_catalog_candidate.py        # PROPOSED
├── validate_taxon_identity.py        # PROPOSED
├── validate_evidence_refs.py         # PROPOSED
├── validate_source_role.py           # PROPOSED
├── validate_geoprivacy.py            # PROPOSED
├── validate_policy_review.py         # PROPOSED
├── validate_cross_lane_refs.py       # PROPOSED
├── build_release_handoff.py          # PROPOSED, no release authority
├── route_quarantine.py               # PROPOSED
├── emit_receipt.py                   # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/flora/catalog.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use accepted lifecycle homes under `data/catalog/domain/flora/`, `data/triplets/flora/`, `data/quarantine/flora/`, `data/receipts/`, `data/proofs/`, and `release/`.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/flora/catalog/` or accepted fixture home | Synthetic, generalized, or redacted. |
| Processed Flora input | `data/processed/flora/<dataset_id>/<version>/` | Validated normalized objects only. |
| Evidence proof | `data/proofs/evidence_bundle/` | Required for claim-bearing catalog records. |
| Catalog candidate | `data/catalog/domain/flora/<dataset_id>/<version>/` | Candidate metadata; not release. |
| Triplet handoff | `data/triplets/flora/` | Projection refs only; graph truth is separate. |
| Quarantine record | `data/quarantine/flora/<reason>/<run_id>/` | Failed, restricted, stale, unresolved, or unsafe material. |
| Receipt | `data/receipts/pipeline/flora/catalog/<run_id>.yml` or accepted receipt home | Records inputs, checks, geoprivacy, evidence, outputs. |
| Release handoff | `release/candidates/flora/` | Reviewable, release-gated output only. |

[⬆ Back to top](#top)

---

## 11. Minimal catalog candidate record

The final schema is not defined here. This example shows the minimum information a Flora catalog candidate should preserve.

```yaml
schema_version: kfm.flora_catalog_candidate.v1
catalog_candidate_id: flora_catalog_<dataset_id>_<version>_<hash>
pipeline_id: domains.flora.catalog
run_id: run_YYYYMMDDThhmmssZ
status: CATALOG_CANDIDATE
object_family: <PlantTaxon|FloraOccurrence|Specimen|VegetationCommunity|PhenologyObservation|InvasivePlantRecord>
source:
  source_ids: []
  source_roles: []
  source_vintage: null
processed_input:
  processed_ref: data/processed/flora/<dataset_id>/<version>/
  validation_report_ref: null
taxon_identity:
  accepted_taxon_ref: null
  synonym_refs: []
  identity_confidence: needs_review
spatial_privacy:
  original_geometry_state: restricted
  public_geometry_state: <withheld|generalized|aggregated|staged|denied|public>
  public_safe_transform_ref: null
evidence:
  evidence_bundle_ref: null
  citation_state: ABSTAIN
policy:
  outcome: ABSTAIN
  review_ref: null
anti_collapse:
  catalog_is_publication: false
  catalog_is_evidence_bundle: false
  redacted_geometry_is_exact_geometry: false
  taxon_name_string_is_taxon_identity: false
  cross_lane_context_is_flora_truth: false
outputs:
  catalog_record_ref: data/catalog/domain/flora/<dataset_id>/<version>/catalog.yml
  receipt_ref: data/receipts/pipeline/flora/catalog/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/generalized/redacted, and no-network** until catalog specs, evidence, policy, sensitivity, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/flora/catalog/
├── test_no_network_dry_run.py              # PROPOSED
├── test_processed_input_required.py        # PROPOSED
├── test_validation_report_required.py      # PROPOSED
├── test_evidence_bundle_required.py        # PROPOSED
├── test_taxon_identity_required.py         # PROPOSED
├── test_source_role_preserved.py           # PROPOSED
├── test_rare_flora_geoprivacy_required.py  # PROPOSED
├── test_redacted_geometry_not_exact.py     # PROPOSED
├── test_cross_lane_context_not_truth.py    # PROPOSED
├── test_policy_review_required.py          # PROPOSED
├── test_catalog_not_publication.py         # PROPOSED
├── test_receipt_hashes.py                  # PROPOSED
└── test_no_direct_publish.py               # PROPOSED
```

A dry run should prove fixtures load without network access, processed inputs are required, EvidenceBundle refs are required for claim-bearing catalog records, rare-flora geometry fails closed, receipts are deterministic, and no run writes directly to public UI, public API, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

Flora catalog pipelines may prepare catalog and release-candidate handoff packages. They do not publish.

Required chain:

```text
processed Flora record
  -> catalog candidate
  -> EvidenceBundle closure
  -> policy and geoprivacy review
  -> catalog / triplet handoff
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public-safe artifact
```

Correction and rollback posture:

- denied, abstained, errored, restricted, stale, conflicted, and quarantined catalog runs remain auditable;
- receipts preserve source refs, taxon identity refs, evidence refs, source-role refs, geoprivacy refs, review refs, policy outcomes, and failure reasons;
- catalog candidates are superseded by governed state transition, not hidden overwrite;
- downstream artifacts are invalidated if processed refs, EvidenceBundle refs, taxon identity refs, geoprivacy refs, policy refs, review refs, correction refs, or rollback refs drift;
- release rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/flora/catalog/README.md` file;
- identifies this directory as a nested executable Flora catalog sublane;
- prevents connector, source-profile, schema, contract, policy, fixture, test, data, proof, public API, UI, geoprivacy decision, and release authority from being placed here;
- preserves PlantTaxon, FloraOccurrence, Specimen, VegetationCommunity, source-role, taxon identity, EvidenceBundle, geoprivacy, policy, lifecycle, catalog/triplet, release, correction, and rollback boundaries;
- blocks catalog-as-truth, catalog-as-publication, EvidenceRef-as-EvidenceBundle, redacted-geometry-as-exact-geometry, taxon-name-as-identity, generated-summary-as-evidence, and direct publication writes;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has processed-fixture coverage, schema-backed catalog candidates, contract conformance, taxon/evidence/source-role/geoprivacy/policy/no-direct-publish tests, deterministic receipts, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `FLORA-CAT-001` | Should Flora catalog execution remain one sublane, or split into occurrence, specimen, taxon, vegetation, phenology, and invasive-plant catalog builders? | NEEDS VERIFICATION / ADR |
| `FLORA-CAT-002` | Which schema owns Flora catalog candidates, catalog receipts, geoprivacy refs, and quarantine reasons? | NEEDS VERIFICATION |
| `FLORA-CAT-003` | Which metadata profile is first-wave: STAC, DCAT, PROV, a KFM CatalogMatrix profile, or all through adapters? | NEEDS VERIFICATION |
| `FLORA-CAT-004` | Which CI job owns Flora catalog invariant tests? | UNKNOWN |
| `FLORA-CAT-005` | Should catalog handoff consume only `data/processed/flora/` records, or may it consume catalog-close remediation records? | NEEDS VERIFICATION |
| `FLORA-CAT-006` | Which geoprivacy receipt format is required before rare-flora catalog records can become release candidates? | NEEDS VERIFICATION / ADR |
| `FLORA-CAT-007` | Which rollback format is required for public-safe Flora catalog and layer artifacts? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic/generalized/redacted fixture-only dry runs and negative tests. Do not add live source fetching, schema authority, policy authority, geoprivacy-decision authority, direct public API code, direct UI code, release-manifest writes, public layer writes, or generated botanical summaries until source roles, taxon identity, EvidenceBundle closure, geoprivacy transforms, review state, release review, and rollback are proven.

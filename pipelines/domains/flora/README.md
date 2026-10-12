<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-flora-readme
title: Flora Domain Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <flora-pipeline-owner>
  - <flora-domain-steward>
  - <habitat-domain-steward>
  - <source-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipelines/domains/flora/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/biodiversity/README.md
  - pipelines/biodiversity/vegetation_stress/README.md
  - pipelines/cross_lane/riparian_vegetation/README.md
  - docs/domains/flora/README.md
  - docs/domains/flora/ARCHITECTURE.md
  - docs/domains/flora/DATA_LIFECYCLE.md
  - docs/domains/flora/OBJECT_FAMILIES.md
  - docs/domains/flora/PUBLICATION_AND_ROLLBACK.md
  - docs/domains/flora/RELEASE_INDEX.md
  - docs/domains/flora/CANONICAL_PATHS.md
  - pipeline_specs/flora/
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
  - biodiversity
  - botany
  - plant-taxa
  - occurrence
  - specimen
  - vegetation
  - phenology
  - invasive-plants
  - geoprivacy
  - evidence
  - policy
  - governance
notes:
  - "This README replaces the greenfield scaffold for pipelines/domains/flora."
  - "Flora pipeline logic is executable implementation support only; it does not own object meaning, schemas, source descriptors, policy, lifecycle data, catalog truth, geoprivacy decisions, or release decisions."
  - "Rare, protected, culturally sensitive, steward-reviewed, and unresolved flora records fail closed by default and require governed public-safe transformation before release."
  - "Concrete executable behavior, source activation, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# 🌿 Flora Domain Pipeline

> Executable Flora-domain pipeline lane for converting admitted plant taxonomy, occurrence, specimen, vegetation-community, invasive-plant, phenology, restoration, and botanical-context source material into governed candidates, quarantine records, processed records, catalog/triplet handoffs, receipts, and release-review packages — without bypassing evidence, policy, geoprivacy, sensitivity, review, or release gates.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-flora%20domain%20pipeline-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20logic-0a7ea4)
![sensitivity](https://img.shields.io/badge/rare%20flora-fail%20closed-d62728)
![publication](https://img.shields.io/badge/publication-geoprivacy%20%2B%20release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/flora/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Flora  
**Placement posture:** flora child lane under `pipelines/domains/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no direct publication; public output requires lifecycle, EvidenceBundle, geoprivacy/sensitivity transform, review record, policy decision, catalog/triplet, release, correction, and rollback closure

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. What belongs here](#3-what-belongs-here)
- [4. What does not belong here](#4-what-does-not-belong-here)
- [5. Flora pipeline scope](#5-flora-pipeline-scope)
- [6. Source-family posture](#6-source-family-posture)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Sensitivity and geoprivacy posture](#9-sensitivity-and-geoprivacy-posture)
- [10. Directory contract](#10-directory-contract)
- [11. Inputs and outputs](#11-inputs-and-outputs)
- [12. Minimal flora pipeline candidate record](#12-minimal-flora-pipeline-candidate-record)
- [13. Dry-run, tests, fixtures, receipts, and proofs](#13-dry-run-tests-fixtures-receipts-and-proofs)
- [14. Promotion, publication, correction, and rollback](#14-promotion-publication-correction-and-rollback)
- [15. Definition of done](#15-definition-of-done)
- [16. Open questions](#16-open-questions)

---

## 1. Purpose

`pipelines/domains/flora/` is the executable pipeline lane for Flora-domain transformations.

It supports candidate processing for:

- plant taxonomic identity and status context;
- flora occurrence and specimen evidence;
- vegetation-community candidates;
- rare, protected, culturally sensitive, or steward-reviewed flora records;
- invasive-plant records;
- phenology observations and seasonal indicators;
- restoration planting context;
- range, distribution, and public-safe botanical surfaces;
- flora × habitat, soil, hydrology, agriculture, hazards, and fauna context joins;
- catalog, graph, Evidence Drawer, and Focus Mode handoff packages.

This directory implements or will implement the **how** of Flora processing. It does not define Flora object meaning, schemas, policy, source descriptors, geoprivacy decisions, lifecycle storage, catalog truth, or release approval.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/flora/`? | Flora is a domain lane under the domain-pipeline umbrella. | CONFIRMED path responsibility pattern; executable behavior NEEDS VERIFICATION |
| Where do declarative specs live? | `pipeline_specs/flora/` or accepted spec home. | PROPOSED / NEEDS VERIFICATION |
| Where do source fetchers live? | `connectors/<source>/`, not here. | CONFIRMED separation |
| Where do schemas live? | `schemas/contracts/v1/domains/flora/` or accepted schema home. | PROPOSED / NEEDS VERIFICATION |
| Where does policy live? | `policy/domains/flora/`, `policy/sensitivity/flora/`, `policy/rights/`, and `policy/release/` as applicable. | PROPOSED / NEEDS VERIFICATION |
| Where do outputs live? | Lifecycle homes under `data/`, not beside pipeline code. | CONFIRMED lifecycle posture |
| Can this lane publish? | No. It may prepare candidates and release handoffs only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> Flora pipeline code is subordinate to source descriptors, source roles, rights, EvidenceBundle closure, geoprivacy/sensitivity transforms, review state, policy decisions, release manifests, correction notices, and rollback cards. A successful run is not public release.

[⬆ Back to top](#top)

---

## 3. What belongs here

Files belong here when their primary responsibility is executable Flora-domain processing.

Appropriate contents include:

- fixture-only dry-run entrypoints for Flora pipeline behavior;
- flora-specific candidate builders;
- occurrence and specimen normalizers;
- plant-taxonomy reconciliation helpers, if not centralized elsewhere;
- vegetation-community candidate builders;
- invasive-plant and phenology normalizers;
- geoprivacy and sensitivity-transform helpers, if not centralized elsewhere;
- review-record and policy-decision handoff helpers;
- quarantine routing helpers for sensitive, unresolved, or steward-controlled material;
- validator wrappers, if not reusable under `tools/`;
- catalog/triplet handoff helpers, if not centralized in `pipelines/catalog/`;
- receipt emitters, if not shared;
- thin adapters that read governed lifecycle inputs, not live source systems.

A good placement test:

> If the code transforms Flora lifecycle inputs into candidates, processed records, restricted catalog/triplet handoffs, receipts, or review handoffs, it may belong here. If it fetches source data, defines meaning, defines schema, encodes policy, stores lifecycle data, or approves release, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 4. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Source fetchers / connectors | `connectors/<source>/` |
| Source catalog profiles | `docs/sources/catalog/...` |
| Source descriptors / source registry entries | `data/registry/sources/flora/` or approved registry home |
| Flora architecture / doctrine | `docs/domains/flora/...` |
| Flora object meaning contracts | `contracts/domains/flora/...` |
| JSON Schemas | `schemas/contracts/v1/domains/flora/...` |
| Policy bundles, sensitivity rules, release rules | `policy/domains/flora/`, `policy/sensitivity/flora/`, `policy/rights/`, `policy/release/` |
| Declarative run specs | `pipeline_specs/flora/...` |
| Fixtures | `fixtures/domains/flora/` or accepted fixture home |
| Tests | `tests/pipelines/domains/flora/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Receipts and proofs | `data/receipts/...`, `data/proofs/...` |
| Release decisions | `release/candidates/flora/`, `release/manifests/flora/`, `release/rollback_cards/`, `release/correction_notices/` |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, `packages/ui/`, `packages/maplibre-runtime/` |
| Sensitive flora occurrence details or location-revealing examples | Not in this README; use governed restricted lifecycle/proof homes with review controls |

> [!WARNING]
> The previous scaffold wording allowed “docs, contracts, schemas, policies, fixtures, tests, packages, pipelines, registries, or data lifecycle artifacts” here. This README narrows the boundary: **only executable Flora pipeline logic belongs here.** The other responsibility roots remain separate authority surfaces.

[⬆ Back to top](#top)

---

## 5. Flora pipeline scope

Flora pipeline work may include these governed processing responsibilities:

| Scope area | Pipeline responsibility | Publication posture |
|---|---|---|
| Plant taxonomy | Normalize plant-taxon identity, synonymy, status, and source-role context. | Public only when source role and evidence support close. |
| Occurrence evidence | Normalize botanical occurrence observations and observation metadata. | Sensitive geometry withheld unless review allows a safe derivative. |
| Specimen evidence | Normalize specimen and repository metadata. | Collection and sensitive-location risk reviewed. |
| Vegetation communities | Build vegetation-community candidates and uncertainty notes. | Derived, not habitat truth; needs evidence and caveats. |
| Rare/protected flora | Route restricted records through sensitivity review and transformation. | Public exact exposure denied. |
| Invasive plants | Normalize occurrence/status context without collapsing source roles. | Sensitive or private-location context reviewed. |
| Phenology | Normalize timing and seasonal plant indicators. | Observation context only; source cadence and time window required. |
| Restoration context | Prepare restoration planting or recovery context candidates. | Avoid unsupported land-management or success claims. |
| Cross-lane joins | Prepare flora × habitat/soil/hydrology/agriculture/hazards relationship candidates. | Other domains keep ownership; joins are derived. |
| Catalog/triplet handoff | Prepare restricted or public-safe catalog/graph candidates after evidence closure. | Does not replace canonical review state. |

[⬆ Back to top](#top)

---

## 6. Source-family posture

Flora pipeline code may consume only admitted or fixture-bound source material.

Candidate source families may include, subject to source descriptors, rights, and steward review:

- herbarium or specimen records;
- plant occurrence observations;
- vegetation-community and land-cover references;
- rare/protected plant stewardship records;
- invasive-plant records;
- phenology and restoration-monitoring records;
- habitat, soil, hydrology, agriculture, hazards, fauna, and land-cover context through governed cross-lane joins;
- local upload or steward-curated material only through source-descriptor, rights, sensitivity, and review gates.

This README does not activate any source. Each source family requires SourceDescriptor coverage, source role, rights posture, sensitivity classification, attribution, fixtures, validation, and review routing before use.

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Flora pipeline must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal Flora pipeline stance:

1. **Read** approved fixtures, immutable raw captures, work candidates, quarantine inputs in remediation mode, or prior processed baselines.
2. **Normalize** into work candidates with source role, rights, temporal scope, spatial scope, sensitivity/geoprivacy posture, evidence references, and restricted geometry handling.
3. **Quarantine** unresolved rights, source-role mismatch, schema drift, sensitivity risk, location-risk, steward-control mismatch, private-location detail, or validation failure.
4. **Promote to processed** only after validation, policy, evidence, sensitivity transform, review, and reviewer gates appropriate to significance.
5. **Prepare catalog/triplet handoffs** only after processed-state and evidence closure, and only with sensitivity-safe payloads.
6. **Publish** only through release decisions, public-safe artifacts, rollback targets, and correction paths.

Do not treat a move from one lifecycle folder to another as promotion. Promotion is a governed state transition with receipts and review evidence.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Flora pipeline run must check or explicitly fail closed on:

1. **Source descriptor gate** — every input has stable source identity, role, cadence, rights, and sensitivity posture.
2. **Source-role gate** — context, range, model, specimen, vegetation, and occurrence records are not silently upgraded to confirmed botanical truth.
3. **Rights gate** — unknown or restrictive license, permission, steward protocol, attribution, or redistribution terms block public release.
4. **Sensitivity gate** — rare, protected, culturally sensitive, steward-reviewed, restricted, and unresolved records fail closed.
5. **Geoprivacy gate** — public products require approved generalization, redaction, delay, aggregation, or denial decisions with receipts.
6. **Review gate** — required steward or domain review state is recorded before promotion beyond candidate or quarantine where applicable.
7. **Candidate-vs-confirmed gate** — candidates remain candidates unless confirmation evidence and review close.
8. **Geometry gate** — restricted geometry is withheld, generalized, redacted, delayed, or denied unless governed restricted authority permits use.
9. **Schema gate** — candidate and processed records match approved schemas.
10. **Contract gate** — object meanings match Flora contracts and do not invent new semantics silently.
11. **Evidence gate** — claim-bearing outputs resolve EvidenceBundle support or abstain.
12. **Temporal gate** — observation, specimen, valid, seasonal, retrieval, processing, catalog, and release times remain distinct.
13. **Spatial gate** — CRS, geometry precision, aggregation/generalization method, and public-safe transforms are recorded.
14. **Policy gate** — policy decisions are finite and recorded; no silent allow.
15. **Validation gate** — validators exercise pass, fail, restrict, abstain, deny, and error paths, not only success.
16. **Receipt gate** — every run records input refs, versions, parameters, transforms, hashes, output refs, and outcomes.
17. **No-direct-publish gate** — no writes to public UI, public API, or `data/published/` without release workflow authority.
18. **Catalog/triplet gate** — catalog and graph projections preserve provenance and do not replace canonical records or review state.
19. **Release gate** — public release requires ReleaseManifest, rollback target, correction path, and review state.

[⬆ Back to top](#top)

---

## 9. Sensitivity and geoprivacy posture

Flora is fail-closed for sensitive botanical occurrence material.

Default posture:

- sensitive occurrence details are denied from public outputs by default;
- rare, protected, culturally sensitive, and steward-controlled records require review before downstream use;
- candidate records are not confirmations;
- public products must use approved geoprivacy and sensitivity transforms;
- generated summaries cannot replace evidence, steward review, transform receipts, policy, or release state;
- public map layers must be generalized, redacted, delayed, restricted, aggregated, or withheld where needed;
- outputs that could expose sensitive records, private-location context, or unsupported land-management claims must abstain, deny, quarantine, or require reviewer handoff.

[⬆ Back to top](#top)

---

## 10. Directory contract

Recommended shape:

```text
pipelines/domains/flora/
├── README.md                         # this file
├── PIPELINE_CONTRACT.md              # PROPOSED: Flora execution contract
├── run_dry_fixture.py                # PROPOSED if repo Python convention is accepted
├── normalize_occurrence.py           # PROPOSED
├── normalize_specimen.py             # PROPOSED
├── reconcile_taxonomy.py             # PROPOSED
├── normalize_vegetation_community.py # PROPOSED
├── normalize_invasive_record.py      # PROPOSED
├── normalize_phenology_record.py     # PROPOSED
├── apply_geoprivacy_transform.py     # PROPOSED; may belong in shared tools if reused
├── build_review_handoff.py           # PROPOSED
├── build_catalog_handoff.py          # PROPOSED if not centralized in pipelines/catalog/
├── validate_flora_candidate.py       # PROPOSED wrapper if not centralized in tools/
├── emit_receipt.py                   # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/flora/
├── README.md                         # PROPOSED / NEEDS VERIFICATION
├── occurrence_dry_run.yaml           # PROPOSED
├── specimen_dry_run.yaml             # PROPOSED
├── taxonomy_reconcile.yaml           # PROPOSED
├── geoprivacy_transform.yaml         # PROPOSED; policy ownership must be resolved
├── review_handoff.yaml               # PROPOSED
└── catalog_handoff.yaml              # PROPOSED
```

Generated outputs must not be written beside the code that generated them. Use lifecycle homes under `data/`, proof homes under `data/proofs/`, receipt homes under `data/receipts/`, and release homes under `release/`.

[⬆ Back to top](#top)

---

## 11. Inputs and outputs

### Inputs

| Input class | Allowed source | Required condition |
|---|---|---|
| No-network fixture | `fixtures/domains/flora/` or accepted fixture home | Synthetic, generalized, or redacted; no sensitive real locations. |
| Raw flora capture | `data/raw/flora/<source_id>/<run_id>/` | Immutable source-edge capture with source descriptor, checksums, and ingest receipt. |
| Work candidate | `data/work/flora/<run_id>/` | Candidate-only; not public. |
| Quarantine input | `data/quarantine/flora/<reason>/<run_id>/` | Audit/remediation mode only. |
| Prior processed baseline | `data/processed/flora/<dataset_id>/<version>/` | Validated restricted baseline for diff/supersession. |
| Source registry / descriptor | `data/registry/sources/flora/`, `docs/sources/catalog/...` | Source role, rights, cadence, attribution, sensitivity. |
| Review state | approved review/proof home | Required before promotion where applicable. |
| Policy / schema / contract refs | `policy/`, `schemas/`, `contracts/` | Referenced by validators, not stored here. |

### Outputs

| Output class | Correct home | Notes |
|---|---|---|
| Flora work candidate | `data/work/flora/<run_id>/` | Candidate only. |
| Flora quarantine record | `data/quarantine/flora/<reason>/<run_id>/` | Failed, restricted, unresolved, or unsafe material. |
| Flora processed dataset version | `data/processed/flora/<dataset_id>/<version>/` | Validated/restricted; not automatically public. |
| Public-safe catalog candidate | `data/catalog/domain/flora/...` or approved catalog home | After processed-state, transform, and evidence gates. |
| Triplet / graph delta | `data/triplets/flora/...` or approved graph-delta home | Projection; does not replace canonical truth or review state. |
| Geoprivacy / sensitivity receipt | `data/receipts/...` or approved receipt/proof home | Required before public-safe derivative. |
| Run receipt | `data/receipts/pipeline/...` | Process memory, not release proof. |
| Evidence / validation proof | `data/proofs/...` | EvidenceBundle, validation reports, proof packs. |
| Release handoff | `release/candidates/flora/...` | Only through release workflow. |

[⬆ Back to top](#top)

---

## 12. Minimal flora pipeline candidate record

The final schema is not defined here. This example shows the minimum information a Flora pipeline candidate should preserve.

```yaml
schema_version: kfm.flora_pipeline_candidate.v1
candidate_id: flora_<object_family>_<run_id>_<hash>
pipeline_id: domains.flora
run_id: run_YYYYMMDDThhmmssZ
status: WORK_CANDIDATE
object_family: <plant_taxon|occurrence|specimen|vegetation_community|invasive_record|phenology_record|restoration_context|...>
source_inputs:
  - source_id: src_flora_example
    source_role: <observation|specimen|context|range|restricted>
    lifecycle_ref: data/raw/flora/<source_id>/<run_id>/
    input_hash: sha256:<hash>
    rights_state: needs_review
spatial_scope:
  geometry_ref: restricted_internal_ref
  public_precision: denied_until_geoprivacy_and_release
temporal_scope:
  observed_at: YYYY-MM-DDThh:mm:ssZ
  collected_at: null
  valid_start: null
  valid_end: null
  retrieved_at: YYYY-MM-DDThh:mm:ssZ
  processed_at: YYYY-MM-DDThh:mm:ssZ
method:
  transform_family: flora_candidate_normalization
  algorithm_version: <version>
  parameter_hash: sha256:<hash>
review:
  steward_review_required: true
  review_state: not_started
sensitivity:
  botanical_sensitivity: needs_review
  geoprivacy_required: true
  public_release_default: DENY
policy:
  outcome: ABSTAIN
  reason_code: GEOPRIVACY_REVIEW_AND_EVIDENCE_NOT_RESOLVED
evidence:
  evidence_bundle_ref: null
  citation_state: ABSTAIN
outputs:
  candidate_record: data/work/flora/run_YYYYMMDDThhmmssZ/candidate.yml
  receipt: data/receipts/pipeline/flora/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 13. Dry-run, tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/generalized/redacted, and no-network** until source activation, rights review, sensitivity review, geoprivacy review, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/flora/
├── test_no_network_dry_run.py                # PROPOSED
├── test_no_sensitive_real_locations.py       # PROPOSED
├── test_source_role_required.py              # PROPOSED
├── test_rights_unknown_denied.py             # PROPOSED
├── test_candidate_not_confirmed.py           # PROPOSED
├── test_sensitive_record_review_required.py  # PROPOSED
├── test_restricted_geometry_denied.py        # PROPOSED
├── test_geoprivacy_receipt_required.py       # PROPOSED
├── test_missing_evidence_abstains.py         # PROPOSED
├── test_receipt_hashes.py                    # PROPOSED
└── test_no_direct_publish.py                 # PROPOSED
```

A dry run should prove:

- fixtures load without network access;
- fixtures are synthetic, generalized, or redacted and contain no sensitive real locations;
- every input has source identity and source role;
- unknown rights produce `ABSTAIN`, `DENY`, or quarantine;
- candidate records cannot become confirmed records without review and evidence closure;
- restricted geometry is withheld from public-safe outputs;
- missing EvidenceBundle support produces `ABSTAIN`;
- steward review and transform receipts are required where sensitivity is unresolved;
- invalid records fail validation;
- receipts include input hashes, method hashes, transform refs, output refs, and outcomes;
- no outputs are written to public UI, public API, `data/published/`, or release manifests by default.

[⬆ Back to top](#top)

---

## 14. Promotion, publication, correction, and rollback

Flora pipelines may prepare candidates. They do not publish.

Required promotion chain:

```text
flora source/work input
  -> flora candidate
  -> validation report
  -> policy decision
  -> steward review where required
  -> geoprivacy / sensitivity receipt where required
  -> EvidenceBundle closure
  -> processed restricted dataset version
  -> catalog / triplet candidate
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public-safe artifact
```

Correction and rollback posture:

- denied, abstained, errored, restricted, and quarantined runs remain auditable;
- candidate rollback preserves receipts and proof state;
- processed versions are superseded by governed state transition, not hidden overwrite;
- public artifact rollback is owned by `release/`, not by this directory;
- correction notices must point back to source, evidence, geoprivacy/sensitivity transform, validation, steward review, catalog, release, and rollback state.

[⬆ Back to top](#top)

---

## 15. Definition of done

This README is done when it:

- replaces the greenfield scaffold with a usable Flora pipeline contract;
- identifies this directory as executable Flora pipeline logic only;
- corrects the boundary so docs, schemas, contracts, policy, fixtures, tests, data, registries, receipts, proofs, and release decisions do not live here;
- preserves source-role, candidate-vs-confirmed, evidence, geoprivacy, sensitivity, policy, lifecycle, catalog/triplet, release, correction, and rollback boundaries;
- denies direct publication and sensitive flora exposure;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable Flora pipeline implementation is done only when it has:

- owners and review burden;
- source-descriptor coverage;
- synthetic/generalized/redacted no-network fixtures;
- schema-backed candidates;
- Flora contract conformance;
- rights, sensitivity, geoprivacy, temporal, spatial, and evidence tests;
- deterministic receipts;
- no-direct-publish tests;
- CI coverage;
- steward-review handoff;
- release, correction, and rollback documentation.

[⬆ Back to top](#top)

---

## 16. Open questions

| ID | Question | Status |
|---|---|---|
| `FLORA-PIPE-001` | Which Flora child modules should be implemented first: occurrences, specimens, taxonomy reconciliation, vegetation communities, geoprivacy transforms, or catalog handoff? | NEEDS VERIFICATION |
| `FLORA-PIPE-002` | Which object family owns geoprivacy, sensitivity, redaction, and review receipts if they become reusable outside Flora? | PROPOSED / NEEDS ADR |
| `FLORA-PIPE-003` | Which source descriptors are first-wave approved for fixture-only dry runs? | NEEDS VERIFICATION |
| `FLORA-PIPE-004` | Which CI job owns Flora pipeline invariant tests? | UNKNOWN |
| `FLORA-PIPE-005` | Should catalog handoff logic live here or in centralized `pipelines/catalog/` with Flora adapters? | NEEDS VERIFICATION |
| `FLORA-PIPE-006` | Which public-safe map/API products are allowed after review and release, and at what generalization? | NEEDS VERIFICATION |
| `FLORA-PIPE-007` | Which roles must approve candidate-to-processed and processed-to-release transitions for restricted flora records? | NEEDS VERIFICATION |
| `FLORA-PIPE-008` | How should cross-lane joins with Habitat, Fauna, Soil, Hydrology, Hazards, Agriculture, or People/Land be denied, restricted, or generalized? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic/generalized fixture-only dry runs and negative tests. Do not add live source fetching, real precise-location examples, public map layers, release handoff automation, or direct API payload generation until source roles, rights, steward review, geoprivacy/sensitivity transforms, evidence closure, and rollback are proven.

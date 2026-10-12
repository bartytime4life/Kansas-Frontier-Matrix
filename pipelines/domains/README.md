<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-readme
title: Domain Pipelines README
type: readme
version: v0.1
status: draft
owners:
  - <pipeline-owner>
  - <domain-lane-stewards>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipelines/domains/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipeline_specs/
  - docs/domains/
  - contracts/domains/
  - schemas/contracts/v1/domains/
  - policy/domains/
  - tests/pipelines/
  - fixtures/
  - data/raw/
  - data/work/
  - data/quarantine/
  - data/processed/
  - data/catalog/
  - data/triplets/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/
  - release/manifests/
tags:
  - kfm
  - pipelines
  - domains
  - domain-lanes
  - executable-logic
  - lifecycle
  - evidence
  - policy
  - governance
notes:
  - "This README replaces the minimal stub for pipelines/domains."
  - "Domain pipeline lanes execute domain-specific transformations while preserving source role, EvidenceBundle, policy, sensitivity, lifecycle, release, correction, and rollback boundaries."
  - "Concrete child directories, executable behavior, schedules, CI jobs, schema paths, and release wiring remain NEEDS VERIFICATION unless verified by repo evidence and tests."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# 🧭 Domain Pipelines

> Executable pipeline lanes for domain-specific KFM processing. `pipelines/domains/` is the **how** for domain transformations; it is not the source of domain meaning, schema shape, policy, lifecycle data, catalog truth, or release decisions.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-domain%20pipelines-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20logic-0a7ea4)
![lifecycle](https://img.shields.io/badge/lifecycle-RAW%E2%86%92PUBLISHED-0a7ea4)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Placement posture:** canonical root pattern for executable domain-pipeline lanes; concrete child lanes remain `PROPOSED / NEEDS VERIFICATION` unless verified  
**Public posture:** no direct publication; outputs must pass lifecycle, evidence, policy, catalog/triplet, release, correction, and rollback gates

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. What belongs here](#3-what-belongs-here)
- [4. What does not belong here](#4-what-does-not-belong-here)
- [5. Domain lane model](#5-domain-lane-model)
- [6. Lifecycle contract](#6-lifecycle-contract)
- [7. Directory contract](#7-directory-contract)
- [8. Recommended child lanes](#8-recommended-child-lanes)
- [9. Required gates for every domain pipeline](#9-required-gates-for-every-domain-pipeline)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Specs, tests, fixtures, receipts, and proofs](#11-specs-tests-fixtures-receipts-and-proofs)
- [12. Promotion, publication, correction, and rollback](#12-promotion-publication-correction-and-rollback)
- [13. Definition of done](#13-definition-of-done)
- [14. Open questions](#14-open-questions)

---

## 1. Purpose

`pipelines/domains/` is the domain-specific execution lane for KFM pipeline implementations.

It exists so each domain can run repeatable processing steps while preserving the KFM trust spine:

```text
SourceDescriptor
  -> SourceIntakeRecord
  -> RAW capture
  -> WORK / QUARANTINE candidate
  -> PROCESSED record
  -> CATALOG / TRIPLET projection
  -> RELEASE decision
  -> PUBLISHED artifact
```

This directory is for executable logic that transforms, validates, normalizes, enriches, crosswalks, or prepares domain-specific records. It does not define what domain objects mean, what their schemas are, what policy allows, or whether public release is approved.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | Domain pipeline code is executable logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/` under `pipelines/`? | Directory Rules show `pipelines/` with a `domains/` sublane for domain pipeline implementations. | CONFIRMED doctrine pattern |
| What is `pipeline_specs/` for? | Declarative run specifications: the **what**. | CONFIRMED root split |
| Does this directory define domain meaning? | No. Domain meaning belongs under `contracts/domains/` and human docs under `docs/domains/`. | CONFIRMED by this README |
| Does this directory define schemas? | No. Schemas belong under `schemas/contracts/v1/...`. | CONFIRMED by this README |
| Does this directory publish? | No. It emits candidates, processed outputs, receipts, validations, catalog/triplet handoffs, and release handoffs only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> Domain pipeline code must remain subordinate to source descriptors, evidence, policy, sensitivity, validation, catalog state, release state, correction path, and rollback path. A successful pipeline run is not a public release.

[⬆ Back to top](#top)

---

## 3. What belongs here

Files belong here when their primary responsibility is executable domain processing.

Appropriate contents include:

- domain-specific normalizers;
- domain-specific validators or validator wrappers when not reusable under `tools/`;
- domain-specific crosswalk builders;
- domain-specific processed-record builders;
- domain-specific catalog/triplet handoff helpers;
- domain-specific receipt emitters when not shared;
- local README files that explain each domain pipeline lane;
- adapters that read governed lifecycle inputs, not live source systems;
- fixture-only dry-run entrypoints for domain pipeline behavior.

A good placement test:

> If the code executes a domain transformation and writes only to governed lifecycle homes, it may belong here. If it fetches from a source, defines object meaning, defines schema shape, encodes policy, stores data, or approves release, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 4. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Source-specific fetchers / admitters | `connectors/<source_id>/` |
| Source catalog profiles | `docs/sources/catalog/...` |
| Machine-readable source registries | `data/registry/sources/...` |
| Domain architecture and explanation | `docs/domains/<domain>/...` |
| Object meaning contracts | `contracts/domains/<domain>/...` |
| Machine schemas | `schemas/contracts/v1/domains/<domain>/...` or approved schema home |
| Policy and admissibility logic | `policy/domains/<domain>/`, `policy/sensitivity/`, `policy/rights/`, `policy/release/` |
| Declarative pipeline specs | `pipeline_specs/<domain>/...` or accepted spec lane |
| Fixtures | `fixtures/...` or `tests/fixtures/...` per repo convention |
| Tests | `tests/pipelines/domains/<domain>/...` or accepted test home |
| Lifecycle outputs | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, `data/catalog/`, `data/triplets/`, `data/published/` |
| Receipts and proofs | `data/receipts/...`, `data/proofs/...` |
| Release decisions | `release/candidates/`, `release/manifests/`, `release/rollback_cards/`, `release/correction_notices/` |
| Public UI / map code | `apps/explorer-web/`, `packages/ui/`, `packages/maplibre-runtime/` |

[⬆ Back to top](#top)

---

## 5. Domain lane model

Each child directory should represent one domain lane already recognized by the KFM domain model.

Typical domain pipeline responsibilities:

| Domain lane | Typical pipeline work |
|---|---|
| `hydrology/` | Normalize watersheds, waterbody observations, flood/riparian context, hydrologic IDs, and catalog handoff. |
| `soil/` | Normalize soil units, horizons, map-unit joins, interpretations, and scale-limited derived context. |
| `flora/` | Normalize plant taxa, flora occurrences, rare-plant redaction inputs, vegetation communities, phenology, invasive plant candidates. |
| `fauna/` | Normalize animal taxa, occurrences, monitoring records, range/sensitivity split, fauna evidence candidates. |
| `habitat/` | Normalize habitat patches, suitability/condition context, land-cover joins, habitat evidence packages. |
| `geology/` | Normalize geology and natural-resource layers with rights, scale, and sensitivity controls. |
| `atmosphere/` | Normalize air, weather, climate, smoke, heat, and atmospheric observations where admitted. |
| `hazards/` | Normalize hazard observations and derived hazard candidates without becoming emergency authority. |
| `agriculture/` | Normalize crop/field/agricultural context with private-property and operational sensitivity controls. |
| `roads-rail-trade/` | Normalize transport and corridor context with infrastructure exposure controls. |
| `settlements-infrastructure/` | Normalize built-environment context with public-safety and infrastructure sensitivity controls. |
| `archaeology/` | Process only under strict quarantine/restriction defaults; exact sensitive locations fail closed. |
| `people-dna-land/` | High-sensitivity processing only; living-person, genealogy, DNA, land, consent, and sovereignty controls apply. |

Child directory names should follow accepted domain-lane names. Naming conflicts, aliases, or proposed new domain lanes require review before implementation.

[⬆ Back to top](#top)

---

## 6. Lifecycle contract

Every domain pipeline must preserve the lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal domain pipeline stance:

1. **Read** immutable raw captures, work candidates, approved fixtures, or prior validated records.
2. **Normalize** into work outputs with explicit source roles, rights, temporal scope, spatial scope, and evidence references.
3. **Quarantine** anything with unresolved rights, source role, schema drift, sensitivity, validation failure, or over-precise geometry.
4. **Promote to processed** only after validation, policy, evidence, and steward-review gates appropriate to significance.
5. **Prepare catalog/triplet candidates** only after processed-state and evidence closure.
6. **Publish** only through release decisions, public-safe artifacts, rollback targets, and correction paths.

Do not treat a directory move as promotion. Promotion is a governed state transition with receipts and review evidence.

[⬆ Back to top](#top)

---

## 7. Directory contract

Recommended umbrella shape:

```text
pipelines/domains/
├── README.md                         # this file
├── hydrology/                        # PROPOSED / NEEDS VERIFICATION unless present and reviewed
├── soil/                             # PROPOSED / NEEDS VERIFICATION
├── flora/                            # PROPOSED / NEEDS VERIFICATION
├── fauna/                            # PROPOSED / NEEDS VERIFICATION
├── habitat/                          # PROPOSED / NEEDS VERIFICATION
├── geology/                          # PROPOSED / NEEDS VERIFICATION
├── atmosphere/                       # PROPOSED / NEEDS VERIFICATION
├── hazards/                          # PROPOSED / NEEDS VERIFICATION
├── agriculture/                      # PROPOSED / NEEDS VERIFICATION
├── roads-rail-trade/                 # PROPOSED / NEEDS VERIFICATION
├── settlements-infrastructure/       # PROPOSED / NEEDS VERIFICATION
├── archaeology/                      # PROPOSED / NEEDS VERIFICATION; fail-closed defaults
└── people-dna-land/                  # PROPOSED / NEEDS VERIFICATION; high-sensitivity defaults
```

Recommended child-lane shape:

```text
pipelines/domains/<domain>/
├── README.md                         # required before trust-bearing code grows
├── PIPELINE_CONTRACT.md              # PROPOSED: domain execution contract
├── run_dry_fixture.py                # PROPOSED if repo Python convention is accepted
├── normalize.py                      # PROPOSED lane-specific normalizer
├── validate_candidate.py             # PROPOSED lane-specific validator wrapper
├── build_catalog_handoff.py          # PROPOSED if not centralized in pipelines/catalog/
├── emit_receipt.py                   # PROPOSED only if not shared in tools/
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Every child directory should have a README before adding trust-bearing executable code.

[⬆ Back to top](#top)

---

## 8. Recommended child lanes

| Child lane | Status | Notes |
|---|---|---|
| `hydrology/` | PROPOSED / NEEDS VERIFICATION | Water, watershed, wetland, flood, riparian context pipeline logic. |
| `soil/` | PROPOSED / NEEDS VERIFICATION | Soil map-unit, horizon, hydric, salinity, erosion, interpretation pipelines. |
| `flora/` | PROPOSED / NEEDS VERIFICATION | Plant, vegetation, phenology, rare-plant, invasive, restoration pipeline logic. |
| `fauna/` | PROPOSED / NEEDS VERIFICATION | Animal taxa, occurrence, range, monitoring, sensitive species pipeline logic. |
| `habitat/` | PROPOSED / NEEDS VERIFICATION | Habitat patch, suitability, condition, land-cover context pipeline logic. |
| `geology/` | PROPOSED / NEEDS VERIFICATION | Geology, minerals, groundwater-adjacent geology context. |
| `atmosphere/` | PROPOSED / NEEDS VERIFICATION | Weather, air, climate, smoke, heat, atmospheric observation pipelines. |
| `hazards/` | PROPOSED / NEEDS VERIFICATION | Fire, flood, drought, storm, smoke, heat, erosion hazard-context pipelines. |
| `agriculture/` | PROPOSED / NEEDS VERIFICATION | Crop, field, land-use, conservation, restoration-adjacent agricultural context. |
| `roads-rail-trade/` | PROPOSED / NEEDS VERIFICATION | Movement, routes, rail, roads, trade corridors, exposure controls. |
| `settlements-infrastructure/` | PROPOSED / NEEDS VERIFICATION | Built environment and infrastructure context, with deny-by-default public-safety posture. |
| `archaeology/` | PROPOSED / NEEDS VERIFICATION | Restricted processing only; public exact site exposure denied. |
| `people-dna-land/` | PROPOSED / NEEDS VERIFICATION | Consent, living-person, DNA/genomic, genealogy, land ownership sensitivity defaults. |

[⬆ Back to top](#top)

---

## 9. Required gates for every domain pipeline

Each domain pipeline must implement or defer to gates for:

1. **Source descriptor gate** — every source input has stable identity and role.
2. **Rights gate** — unknown or restrictive rights fail closed.
3. **Sensitivity gate** — exact sensitive ecology, archaeology, cultural, living-person, DNA/genomic, private-property, infrastructure, or public-safety exposure is denied, restricted, generalized, delayed, or quarantined.
4. **Schema gate** — candidate and processed records match approved schemas.
5. **Contract gate** — object meaning matches the domain contract; pipelines do not invent new semantics silently.
6. **Evidence gate** — claim-bearing outputs resolve EvidenceBundle support or abstain.
7. **Temporal gate** — observation, retrieval, processing, valid, catalog, and release times remain distinct.
8. **Spatial gate** — CRS, geometry precision, scale, aggregation, and public-safe transforms are recorded.
9. **Policy gate** — policy decisions are finite and recorded; no silent allow.
10. **Validation gate** — validators exercise pass, fail, abstain/deny/error paths, not only success.
11. **Receipt gate** — every run records inputs, versions, parameters, hashes, outputs, and outcomes.
12. **No-direct-publish gate** — domain pipelines do not write directly to public UI, public API, or `data/published/` without release workflow authority.
13. **Catalog/triplet gate** — catalog and graph projections preserve provenance and do not replace canonical domain records.
14. **Release gate** — public release requires ReleaseManifest, rollback target, correction path, and review state.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

### Inputs

| Input class | Allowed source | Required condition |
|---|---|---|
| No-network fixture | `fixtures/...` | Safe default for tests and dry runs. |
| Raw capture | `data/raw/<domain>/<source_id>/<run_id>/` | Immutable capture with source descriptor, checksums, and ingest receipt. |
| Work candidate | `data/work/<domain>/<run_id>/` | Candidate-only; not public. |
| Quarantine input | `data/quarantine/<domain>/<reason>/<run_id>/` | Audit/remediation mode only. |
| Prior processed baseline | `data/processed/<domain>/<dataset_id>/<version>/` | Validated baseline for diff/supersession. |
| Source registry / descriptor | `data/registry/sources/...`, `docs/sources/catalog/...` | Source role, rights, cadence, steward, sensitivity. |
| Policy / schema / contract refs | `policy/`, `schemas/`, `contracts/` | Referenced by validators, not stored here. |

### Outputs

| Output class | Correct home | Notes |
|---|---|---|
| Work candidate | `data/work/<domain>/<run_id>/` | Candidate only. |
| Quarantine record | `data/quarantine/<domain>/<reason>/<run_id>/` | Failed, restricted, unresolved, or unsafe material. |
| Processed dataset version | `data/processed/<domain>/<dataset_id>/<version>/` | Validated; not automatically public. |
| Catalog candidate | `data/catalog/...` | After processed-state and evidence gates. |
| Triplet / graph delta | `data/triplets/graph_deltas/...` | Projection; does not replace canonical truth. |
| Run receipt | `data/receipts/pipeline/...` | Process memory, not proof of release. |
| Evidence / validation proof | `data/proofs/...` | EvidenceBundle, validation reports, proof packs. |
| Release handoff | `release/candidates/...` | Only through release workflow. |

[⬆ Back to top](#top)

---

## 11. Specs, tests, fixtures, receipts, and proofs

Declarative specs should live in `pipeline_specs/`, not here:

```text
pipeline_specs/<domain>/
└── <job>.yaml                         # PROPOSED / NEEDS VERIFICATION per domain
```

Recommended tests:

```text
tests/pipelines/domains/
├── README.md                          # PROPOSED / NEEDS VERIFICATION
├── test_no_direct_publish.py          # shared invariant test
├── test_lifecycle_phase_rules.py      # shared invariant test
└── <domain>/
```

Recommended fixtures:

```text
fixtures/pipelines/domains/
├── valid/                             # PROPOSED / NEEDS VERIFICATION
├── invalid/                           # PROPOSED / NEEDS VERIFICATION
├── golden/                            # PROPOSED / NEEDS VERIFICATION
└── synthetic/                         # PROPOSED / NEEDS VERIFICATION
```

Receipts and proofs belong under approved lifecycle homes:

```text
data/receipts/pipeline/
data/proofs/
```

Each domain pipeline should begin with fixture-only, no-network execution and negative tests for missing source role, unknown rights, unresolved sensitivity, missing evidence, schema drift, stale inputs, and direct-publish attempts.

[⬆ Back to top](#top)

---

## 12. Promotion, publication, correction, and rollback

Domain pipelines may prepare candidates. They do not publish.

Required promotion chain:

```text
raw or work input
  -> domain candidate
  -> validation report
  -> policy decision
  -> EvidenceBundle closure
  -> processed dataset version
  -> catalog / triplet candidate
  -> steward review
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public-safe artifact
```

Correction and rollback posture:

- failed, denied, abstained, and quarantined runs remain auditable;
- candidate rollback preserves receipts and proof state;
- processed versions are superseded by governed state transition, not hidden overwrite;
- public artifact rollback is owned by `release/`, not by this directory;
- correction notices must point back to source, evidence, validation, catalog, release, and rollback state.

[⬆ Back to top](#top)

---

## 13. Definition of done

This README is done when it:

- replaces the minimal stub with a usable domain-pipeline contract;
- identifies `pipelines/domains/` as executable logic, not meaning, schema, policy, data, or release authority;
- preserves domain ownership and lifecycle boundaries;
- keeps source descriptors, schemas, contracts, policies, fixtures, tests, data, receipts, proofs, catalog outputs, and release decisions in their proper homes;
- names expected child-lane behavior and review burden;
- denies direct publication;
- gives maintainers a safe expansion pattern.

Future executable domain pipeline implementation is done only when it has:

- owners and review burden;
- source-descriptor coverage;
- no-network fixtures;
- schema-backed candidate records;
- domain-contract conformance;
- source-role, rights, sensitivity, temporal, spatial, and evidence tests;
- deterministic receipts;
- no-direct-publish tests;
- CI coverage;
- steward-review handoff;
- release, correction, and rollback documentation.

[⬆ Back to top](#top)

---

## 14. Open questions

| ID | Question | Status |
|---|---|---|
| `DOMAIN-PIPES-001` | Which domain child directories already exist and are active versus placeholders? | NEEDS VERIFICATION |
| `DOMAIN-PIPES-002` | Should child lane names exactly mirror `docs/domains/` names, including hyphenated names such as `roads-rail-trade` and `people-dna-land`? | NEEDS VERIFICATION |
| `DOMAIN-PIPES-003` | Should declarative specs live at `pipeline_specs/<domain>/` or `pipeline_specs/domains/<domain>/`? | NEEDS VERIFICATION |
| `DOMAIN-PIPES-004` | Which CI job owns shared domain-pipeline invariant tests? | UNKNOWN |
| `DOMAIN-PIPES-005` | Which child domains should be implemented first after fixtures and validators are in place? | NEEDS VERIFICATION |
| `DOMAIN-PIPES-006` | Which object family owns generic `DomainPipelineCandidate` and `DomainPipelineRunReceipt`, if those become reusable contracts? | PROPOSED / NEEDS ADR if new object family |
| `DOMAIN-PIPES-007` | How should high-sensitivity lanes, especially archaeology and people-dna-land, be separated from normal domain-pipeline execution? | NEEDS VERIFICATION |
| `DOMAIN-PIPES-008` | Should `pipelines/cross_lane/` reuse shared helpers from `pipelines/domains/` or keep all cross-lane helpers separate? | NEEDS VERIFICATION |

---

## Maintainer note

Keep each child lane small and fixture-first. Add trust-bearing executable code only with source descriptors, no-network fixtures, negative tests, receipts, policy decisions, evidence posture, and rollback planning in the same or immediately paired change.

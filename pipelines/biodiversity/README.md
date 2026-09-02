<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-biodiversity-readme
title: Biodiversity Pipelines README
type: readme
version: v0.1
status: draft
owners:
  - <biodiversity-pipeline-owner>
  - <flora-domain-steward>
  - <fauna-domain-steward>
  - <habitat-domain-steward>
  - <hydrology-domain-steward>
  - <soil-domain-steward>
  - <hazards-domain-steward>
  - <agriculture-domain-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipelines/biodiversity/README.md
related:
  - docs/doctrine/directory-rules.md
  - docs/domains/flora/ARCHITECTURE.md
  - docs/domains/habitat/SOURCE_REGISTRY.md
  - docs/domains/fauna/
  - docs/domains/habitat/
  - docs/domains/flora/
  - docs/domains/soil/
  - docs/domains/hydrology/
  - docs/domains/hazards/
  - docs/domains/agriculture/
  - pipelines/biodiversity/vegetation_stress/README.md
  - pipelines/domains/flora/
  - pipelines/domains/fauna/
  - pipelines/domains/habitat/
  - pipeline_specs/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/
tags:
  - kfm
  - pipelines
  - biodiversity
  - cross-lane
  - flora
  - fauna
  - habitat
  - evidence
  - policy
  - governance
notes:
  - "This README governs the requested pipelines/biodiversity/ umbrella path. It does not establish Biodiversity as a new canonical domain root."
  - "Biodiversity pipeline lanes compose evidence from owned domain lanes. They do not own Flora, Fauna, Habitat, Soil, Hydrology, Hazards, Agriculture, or release truth."
  - "Concrete executable behavior, schedules, CI jobs, source activation, schema contracts, and release behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# 🧬 Biodiversity Pipelines

> Cross-lane execution space for biodiversity-related pipeline slices that compose Flora, Fauna, Habitat, Soil, Hydrology, Hazards, Agriculture, and related evidence **without creating a new truth authority or public publication shortcut**.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-cross--lane%20biodiversity-2e7d32)
![authority](https://img.shields.io/badge/authority-not%20a%20domain%20root-d62728)
![lifecycle](https://img.shields.io/badge/lifecycle-RAW%E2%86%92PUBLISHED-0a7ea4)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/biodiversity/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Placement posture:** `PROPOSED / NEEDS VERIFICATION` because `biodiversity/` is treated here as a cross-lane pipeline umbrella, not as a proven canonical domain segment  
**Public posture:** no direct publication; all outputs must pass KFM lifecycle, evidence, policy, catalog, release, and rollback gates

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. What belongs here](#3-what-belongs-here)
- [4. What does not belong here](#4-what-does-not-belong-here)
- [5. Cross-lane ownership model](#5-cross-lane-ownership-model)
- [6. Lifecycle contract](#6-lifecycle-contract)
- [7. Directory contract](#7-directory-contract)
- [8. Current lanes](#8-current-lanes)
- [9. Required gates for every biodiversity pipeline](#9-required-gates-for-every-biodiversity-pipeline)
- [10. Sensitivity and public-safety posture](#10-sensitivity-and-public-safety-posture)
- [11. Specs, tests, fixtures, and receipts](#11-specs-tests-fixtures-and-receipts)
- [12. Promotion, publication, and rollback](#12-promotion-publication-and-rollback)
- [13. Definition of done](#13-definition-of-done)
- [14. Open questions](#14-open-questions)

---

## 1. Purpose

`pipelines/biodiversity/` is a cross-lane execution umbrella for biodiversity-related pipeline slices that need to compose multiple KFM domain lanes.

It exists because some biodiversity questions are not owned by a single domain:

- vegetation stress draws from Flora, Habitat, Hazards, Hydrology, Soil, and Agriculture;
- habitat-condition analysis draws from Habitat, Flora, Fauna, Hydrology, Soil, and Hazards;
- invasive-species context can touch Flora, Fauna, Agriculture, Habitat, and policy;
- pollinator or food-web context touches Flora, Fauna, Habitat, Agriculture, and stewardship review;
- restoration or conservation-condition review can touch multiple domain lanes and public-safety gates.

This directory coordinates **how cross-lane pipeline logic runs**. It does not own the truth of the domains it composes.

[⬆ Back to top](#top)

---

## 2. Placement and authority

The placement basis is responsibility-rooted:

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic, not source documentation, schema, policy, fixture, data, release, or UI code. | CONFIRMED root responsibility |
| Why `biodiversity/`? | It is a cross-lane umbrella for biodiversity compositions that span multiple domain lanes. | PROPOSED |
| Is Biodiversity a new canonical domain root? | No. This README does not create a new `docs/domains/biodiversity/` authority lane or root-level domain. | CONFIRMED by this README |
| Can domain-specific pipeline logic live here? | Only when it is genuinely cross-lane. Single-domain logic should prefer `pipelines/domains/<domain>/`. | PROPOSED |
| Can this directory publish outputs? | No. It can create candidates, receipts, validation reports, and handoffs; publication remains release-gated. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> `pipelines/biodiversity/` is an execution umbrella, not a canonical truth authority. Flora owns plant truth; Fauna owns animal truth; Habitat owns habitat truth; other domains keep their own truth. Biodiversity pipelines may compose those lanes only through governed inputs and evidence-bound outputs.

[⬆ Back to top](#top)

---

## 3. What belongs here

Files belong here when their **primary responsibility** is cross-lane biodiversity pipeline orchestration.

Appropriate contents include:

- README and local pipeline contract documents;
- thin executable entrypoints for cross-lane biodiversity slices;
- local adapters that orchestrate already-governed inputs;
- candidate-emission helpers for biodiversity compositions;
- pipeline-local validation or receipt glue when not reusable elsewhere;
- subdirectories for bounded cross-lane slices such as `vegetation_stress/`.

A good test: if the code cannot be owned by exactly one domain lane without hiding a cross-lane dependency, it may belong here.

[⬆ Back to top](#top)

---

## 4. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Source catalog profiles | `docs/sources/catalog/...` |
| Source descriptors / machine registries | `data/registry/sources/...` |
| Connector/fetcher code | `connectors/<source_id>/` |
| Domain architecture docs | `docs/domains/<domain>/...` |
| Object meaning contracts | `contracts/domains/<domain>/...` or accepted cross-domain contract family |
| JSON Schemas | `schemas/contracts/v1/...` |
| Policy rules | `policy/domains/<domain>/`, `policy/sensitivity/`, `policy/rights/`, `policy/release/` |
| Golden, valid, invalid, or synthetic fixtures | `fixtures/...` or `tests/fixtures/...` per repo convention |
| Tests | `tests/pipelines/biodiversity/...` or accepted test home |
| Lifecycle data | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, `data/catalog/`, `data/published/` |
| Proofs and EvidenceBundles | `data/proofs/...` |
| Receipts | `data/receipts/...` |
| Release decisions | `release/candidates/`, `release/manifests/`, `release/rollback_cards/`, `release/correction_notices/` |
| Public UI or map code | `apps/explorer-web/`, `packages/ui/`, `packages/maplibre-runtime/` |

> [!WARNING]
> Do not store outputs beside the code that generated them. Pipeline code lives here; lifecycle outputs live under `data/`; release decisions live under `release/`; public-safe artifacts live only after governed promotion.

[⬆ Back to top](#top)

---

## 5. Cross-lane ownership model

Biodiversity pipelines compose evidence across owned lanes. They must preserve ownership and source role at every boundary.

| Owned lane | What it owns | Biodiversity pipeline may do |
|---|---|---|
| Flora | Plant taxa, plant occurrences, rare plants, phenology, vegetation communities, invasive plant records. | Consume governed flora inputs; never expose exact sensitive flora geometry. |
| Fauna | Animal taxa, occurrences, ranges, monitoring evidence, sensitive species controls. | Consume public-safe or restricted-reviewed fauna context; never become fauna truth. |
| Habitat | Habitat patches, suitability, land-cover context, condition surfaces. | Compose habitat context and condition candidates with domain-reviewed evidence. |
| Soil | Soil map units, horizons, substrate and soil-water context. | Use as contextual evidence when source role and scale support it. |
| Hydrology | Watersheds, water observations, wetland/riparian context. | Use as contextual evidence for stress, habitat, or restoration analysis. |
| Hazards | Drought, fire, flood, smoke, heat, storm, disturbance context. | Use as disturbance/stressor context, not emergency authority. |
| Agriculture | Crop/field/agricultural context. | Use with care; never infer private operational or crop-loss claims without release controls. |
| Release / Policy | Promotion, public-safety, rights, rollback, correction. | Obey; never bypass. |

[⬆ Back to top](#top)

---

## 6. Lifecycle contract

Every biodiversity pipeline must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

The normal pipeline stance is:

1. **Read** only approved fixtures or governed lifecycle inputs.
2. **Emit** candidate records to `data/work/...` or quarantine records to `data/quarantine/...`.
3. **Validate** with schema, source-role, rights, sensitivity, temporal, spatial, and evidence checks.
4. **Prepare** processed or catalog candidates only after validation and evidence closure.
5. **Promote** only through release review and release manifests.
6. **Publish** only released public-safe artifacts through governed interfaces.

This directory must not create shortcuts around lifecycle gates.

[⬆ Back to top](#top)

---

## 7. Directory contract

Recommended shape:

```text
pipelines/biodiversity/
├── README.md                         # this file
├── PIPELINE_CONTRACT.md              # PROPOSED: umbrella execution contract
├── vegetation_stress/                # existing cross-lane candidate pipeline
└── <future-cross-lane-slice>/         # PROPOSED only after placement review
```

Potential future cross-lane slices must be reviewed before landing, especially if they involve sensitive ecology, rare species, private property, cultural knowledge, or high-consequence public interpretation.

Candidate future lanes might include:

```text
pipelines/biodiversity/
├── habitat_condition/                 # PROPOSED / NEEDS VERIFICATION
├── invasive_pressure/                 # PROPOSED / NEEDS VERIFICATION
├── pollinator_context/                # PROPOSED / NEEDS VERIFICATION
├── restoration_monitoring/            # PROPOSED / NEEDS VERIFICATION
└── species_habitat_join/              # PROPOSED / NEEDS VERIFICATION
```

Do not create those directories until each has a placement note, owners, fixtures, policy gates, and a failure-closed plan.

[⬆ Back to top](#top)

---

## 8. Current lanes

| Lane | Purpose | Status |
|---|---|---|
| [`vegetation_stress/`](vegetation_stress/) | Candidate vegetation-stress signals across Flora, Habitat, Hazards, Hydrology, Soil, Agriculture, and related evidence. | Draft README exists; executable behavior NEEDS VERIFICATION. |

[⬆ Back to top](#top)

---

## 9. Required gates for every biodiversity pipeline

Each child pipeline must implement or defer to gates for:

1. **Source identity** — every input source has a stable identifier.
2. **Source role** — sources are not silently upgraded from context to authority.
3. **Rights** — unclear or restrictive rights fail closed.
4. **Sensitivity** — rare species, precise habitat, cultural knowledge, private property, and join-induced exposure risks are denied, restricted, generalized, delayed, or quarantined.
5. **Temporal scope** — observation, retrieval, processing, valid, and release time remain distinct.
6. **Spatial fitness** — geometry precision, CRS, scale, aggregation, and public-safe generalization are recorded.
7. **Evidence closure** — claim-like outputs require EvidenceBundle support or abstain.
8. **Validation** — schema, policy, and business-rule validation emit finite outcomes.
9. **Receipts** — every run records inputs, parameters, hashes, outputs, and outcome.
10. **No-public-shortcut** — no child pipeline writes directly to public UI, public API, or published artifacts.
11. **Catalog readiness** — STAC/DCAT/PROV or KFM-equivalent catalog closure exists before discovery/public use.
12. **Release readiness** — ReleaseManifest, rollback target, correction path, and review state exist before public release.

[⬆ Back to top](#top)

---

## 10. Sensitivity and public-safety posture

Biodiversity pipelines are high-risk for **join-induced sensitivity**. Even when inputs are public individually, a derived output may expose sensitive locations, vulnerable species, cultural knowledge, private-property patterns, or stewardship risks.

Default posture:

- exact sensitive species locations are denied from public outputs;
- culturally sensitive plant, animal, or habitat knowledge requires steward review;
- derived risk surfaces are evaluated at the output level, not only at source admission;
- uncertain rights or source roles produce `ABSTAIN`, `DENY`, or quarantine;
- high-consequence public interpretation requires review and release controls;
- public map layers must be generalized, redacted, aggregated, or withheld when needed.

> [!CAUTION]
> Biodiversity products can look like neutral map layers while carrying sensitive ecological implications. Treat each derived layer as a claim-bearing surface until policy proves otherwise.

[⬆ Back to top](#top)

---

## 11. Specs, tests, fixtures, and receipts

Declarative specs should not be embedded in this README. Use a spec home if accepted:

```text
pipeline_specs/biodiversity/
├── README.md                          # PROPOSED / NEEDS VERIFICATION
└── vegetation_stress/
    └── dry_run.yaml                   # PROPOSED / NEEDS VERIFICATION
```

Recommended test home:

```text
tests/pipelines/biodiversity/
├── README.md                          # PROPOSED / NEEDS VERIFICATION
└── vegetation_stress/
```

Recommended fixture home:

```text
fixtures/pipelines/biodiversity/
├── valid/                             # PROPOSED / NEEDS VERIFICATION
├── invalid/                           # PROPOSED / NEEDS VERIFICATION
├── golden/                            # PROPOSED / NEEDS VERIFICATION
└── synthetic/                         # PROPOSED / NEEDS VERIFICATION
```

Run receipts should be emitted to the approved receipt home, typically under:

```text
data/receipts/pipeline/
```

Proof outputs such as EvidenceBundle or validation reports should use the approved proof home, typically under:

```text
data/proofs/
```

[⬆ Back to top](#top)

---

## 12. Promotion, publication, and rollback

Biodiversity pipelines may prepare candidates. They do not publish.

Required promotion chain:

```text
cross-lane candidate
  -> validation report
  -> policy decision
  -> EvidenceBundle closure
  -> catalog candidate
  -> steward review
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public-safe artifact
```

Rollback responsibilities:

- local candidate rollback preserves run receipts and marks candidate status clearly;
- denied, abstained, and quarantined runs remain auditable;
- published artifact rollback is owned by `release/`, not by this directory;
- correction notices must point back to release and evidence state.

[⬆ Back to top](#top)

---

## 13. Definition of done

This README is done when it:

- explains `pipelines/biodiversity/` as a cross-lane pipeline umbrella;
- denies Biodiversity as a new canonical domain root unless later approved by ADR/domain registry;
- preserves lifecycle, evidence, policy, catalog, release, and rollback boundaries;
- keeps contracts, schemas, policies, tests, fixtures, data, receipts, proofs, and releases in their proper homes;
- names child lane expectations;
- warns about sensitive and join-induced biodiversity risk;
- gives maintainers a safe expansion pattern.

Future executable biodiversity pipelines are done only when they have:

- owners;
- source-descriptor coverage;
- no-network fixtures;
- schema-backed candidate records;
- policy tests;
- rights and sensitivity tests;
- evidence-closure tests;
- deterministic receipts;
- no-direct-publish tests;
- CI coverage;
- steward-review handoff;
- release and rollback documentation.

[⬆ Back to top](#top)

---

## 14. Open questions

| ID | Question | Status |
|---|---|---|
| `BIODIV-PIPES-001` | Should `pipelines/biodiversity/` be accepted as a stable cross-lane pipeline umbrella, or should all child lanes migrate under `pipelines/domains/<domain>/` with explicit cross-lane specs? | NEEDS VERIFICATION |
| `BIODIV-PIPES-002` | Should there be a formal `pipeline_specs/biodiversity/` home? | NEEDS VERIFICATION |
| `BIODIV-PIPES-003` | Which object family owns cross-lane biodiversity candidate records? | PROPOSED / NEEDS ADR if new object family |
| `BIODIV-PIPES-004` | Which steward role arbitrates Flora × Fauna × Habitat sensitivity conflicts? | NEEDS VERIFICATION |
| `BIODIV-PIPES-005` | What CI job owns no-network cross-lane biodiversity fixtures? | UNKNOWN |
| `BIODIV-PIPES-006` | Which derived biodiversity products are eligible for public map layers, and at what precision/generalization? | NEEDS VERIFICATION |
| `BIODIV-PIPES-007` | Should `biodiversity/` also exist under `tests/pipelines/`, `fixtures/pipelines/`, and `pipeline_specs/`, or only under `pipelines/`? | NEEDS VERIFICATION |

---

## Maintainer note

Keep this umbrella small. Add child lanes one at a time, with fixture-only dry runs, negative tests, source-role checks, policy decisions, evidence closure, and rollback plans before any public or semi-public surface is touched.

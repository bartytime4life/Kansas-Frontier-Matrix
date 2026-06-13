<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-cross-lane-readme
title: Cross-Lane Pipelines README
type: readme
version: v0.1
status: draft
owners:
  - <cross-lane-pipeline-owner>
  - <domain-lane-stewards>
  - <policy-steward>
  - <evidence-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipelines/cross_lane/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/cross_lane/riparian_vegetation/README.md
  - pipelines/biodiversity/README.md
  - pipelines/biodiversity/vegetation_stress/README.md
  - pipelines/domains/
  - pipeline_specs/
  - docs/domains/
  - contracts/domains/
  - schemas/contracts/v1/domains/
  - policy/domains/
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
  - cross-lane
  - orchestration
  - evidence
  - policy
  - lifecycle
  - governance
notes:
  - "This README governs the requested pipelines/cross_lane umbrella path. It does not establish cross_lane as a new canonical root or domain."
  - "Cross-lane pipelines compose evidence across owned domain lanes while preserving source role, policy, sensitivity, provenance, release state, and rollback boundaries."
  - "Concrete executable behavior, child-lane registry, specs, schemas, schedules, CI coverage, and release wiring remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# 🔀 Cross-Lane Pipelines

> Execution umbrella for pipeline slices that must compose multiple KFM domain lanes while preserving domain ownership, source role, evidence closure, policy gates, lifecycle boundaries, and release control.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-cross--lane%20pipelines-2e7d32)
![authority](https://img.shields.io/badge/authority-not%20a%20domain%20root-d62728)
![lifecycle](https://img.shields.io/badge/lifecycle-WORK%20candidate%20first-0a7ea4)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/cross_lane/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Placement posture:** `PROPOSED / NEEDS VERIFICATION` because `cross_lane/` is treated here as an umbrella segment under `pipelines/`, not as a proven canonical domain or authority root  
**Public posture:** no direct publication; all child outputs must pass KFM lifecycle, evidence, policy, catalog, release, and rollback gates

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
- [9. Required gates for every child lane](#9-required-gates-for-every-child-lane)
- [10. Sensitivity and public-safety posture](#10-sensitivity-and-public-safety-posture)
- [11. Specs, tests, fixtures, receipts, and proofs](#11-specs-tests-fixtures-receipts-and-proofs)
- [12. Promotion, publication, and rollback](#12-promotion-publication-and-rollback)
- [13. Definition of done](#13-definition-of-done)
- [14. Open questions](#14-open-questions)

---

## 1. Purpose

`pipelines/cross_lane/` is an execution umbrella for pipeline slices whose primary work is **composition across multiple KFM domain lanes**.

It exists for work that would hide important dependencies if forced under a single domain pipeline. Examples include:

- Hydrology × Flora × Habitat riparian vegetation analysis;
- Flora × Fauna × Habitat species-habitat association checks;
- Hazards × Habitat × Flora post-fire or drought ecological recovery candidates;
- Soil × Hydrology × Agriculture × Habitat wetland or riparian context candidates;
- Roads/Settlements × Ecology public-safety or exposure-risk review candidates;
- Archaeology × Hydrology × Habitat sensitivity-adjacent landform context, when allowed by policy.

This directory coordinates **how cross-lane pipeline logic runs**. It does not own the truth of any lane it composes.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | Cross-lane builders are executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| What does `cross_lane/` mean? | A pipeline segment for compositions that require multiple domain lanes. | PROPOSED |
| Is `cross_lane/` canonical? | Not proven here. Treat this as a governed working segment until Directory Rules, ADR, or a domain-lane registry accepts or migrates it. | NEEDS VERIFICATION |
| Is Cross-Lane a domain? | No. This README does not create `docs/domains/cross_lane/`, `schemas/contracts/v1/domains/cross_lane/`, or a new root. | CONFIRMED by this README |
| Can child lanes publish? | No. They may emit candidates, receipts, validation reports, quarantine records, catalog/triplet candidates, and release handoffs only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> Cross-lane does not mean “authority over everything.” It means “composition across authorities.” Every input retains its owning domain, source role, rights posture, evidence state, sensitivity class, and lifecycle phase.

[⬆ Back to top](#top)

---

## 3. What belongs here

Files belong here when their primary responsibility is cross-lane pipeline orchestration.

Appropriate contents include:

- this README and umbrella execution contracts;
- child-lane README files for bounded cross-lane compositions;
- thin executable entrypoints for cross-lane candidate production;
- adapters that read governed lifecycle inputs, not live source systems;
- join validators that preserve source role and domain ownership;
- receipt emitters for cross-lane composition runs when not shared in `tools/`;
- candidate builders for cross-lane outputs that require multiple domain stewards;
- local notes on handoff to catalog, triplet, proof, or release paths.

A good placement test:

> If the logic cannot be responsibly owned by one domain without hiding another domain's authority, source role, evidence, or sensitivity state, it may belong under `pipelines/cross_lane/`.

[⬆ Back to top](#top)

---

## 4. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| New domain architecture | `docs/domains/<domain>/...` |
| Source catalog profiles | `docs/sources/catalog/...` |
| Machine-readable source registry entries | `data/registry/sources/...` |
| Source fetchers / connectors | `connectors/<source_id>/` |
| Object meaning contracts | `contracts/domains/<domain>/...` or accepted cross-domain contract family |
| JSON Schemas | `schemas/contracts/v1/...` |
| Policy rules | `policy/domains/<domain>/`, `policy/sensitivity/`, `policy/rights/`, `policy/release/` |
| Fixtures | `fixtures/...` or `tests/fixtures/...` per repo convention |
| Tests | `tests/pipelines/cross_lane/...` or accepted test home |
| Lifecycle data | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, `data/catalog/`, `data/triplets/`, `data/published/` |
| Receipts and proofs | `data/receipts/...`, `data/proofs/...` |
| Release decisions | `release/candidates/`, `release/manifests/`, `release/rollback_cards/`, `release/correction_notices/` |
| Public UI / map code | `apps/explorer-web/`, `packages/ui/`, `packages/maplibre-runtime/` |

> [!WARNING]
> Do not store generated outputs beside the code that generated them. Pipeline code lives here; lifecycle outputs live under `data/`; release decisions live under `release/`; public-safe artifacts are created only after governed promotion.

[⬆ Back to top](#top)

---

## 5. Cross-lane ownership model

Cross-lane pipelines must preserve ownership at every boundary.

| Concern | Rule |
|---|---|
| Domain meaning | Each contributing domain owns its own object meanings, terms, and limitations. |
| Source role | A source admitted as context cannot become primary authority just because it appears in a join. |
| Evidence | A cross-lane candidate must resolve EvidenceBundle support for claim-like outputs or abstain. |
| Sensitivity | Sensitivity is evaluated on the derived product, not only the inputs. |
| Policy | Policy outcomes must be finite: `ALLOW_AT_STAGE`, `RESTRICT`, `ABSTAIN`, `DENY`, or `ERROR`. |
| Release | Public release requires release decisions, rollback path, correction path, and review state. |
| AI | Generated summaries cannot become evidence or publication approval. |

Typical domain contributors include:

| Domain lane | Common cross-lane contribution |
|---|---|
| Hydrology | Streams, watersheds, wetlands, floodplains, water observations. |
| Flora | Plant taxa, vegetation communities, phenology, rare/culturally sensitive flora. |
| Fauna | Species occurrences, habitat interactions, sensitive fauna controls. |
| Habitat | Habitat patches, suitability, land-cover context, condition surfaces. |
| Soil | Map units, hydric/substrate context, erosion, salinity, soil-water context. |
| Hazards | Fire, drought, flood, heat, smoke, storms, disturbance context. |
| Agriculture | Cropland, irrigation, restoration adjacency, land-use context. |
| Roads / Settlements / Infrastructure | Access, exposure, public-safety, maintenance, and built-environment context. |
| Archaeology / People-DNA-Land | High-sensitivity context; use only through strict policy and steward review. |

[⬆ Back to top](#top)

---

## 6. Lifecycle contract

Every child lane must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal cross-lane stance:

1. **Read** only approved fixtures or governed lifecycle inputs.
2. **Join** inputs while preserving owning domain, source role, rights, sensitivity, temporal scope, and spatial scale.
3. **Emit** cross-lane candidate records to `data/work/...` or quarantine records to `data/quarantine/...`.
4. **Validate** with schema, source-role, rights, sensitivity, spatial, temporal, evidence, and no-direct-publish checks.
5. **Prepare** catalog or triplet candidates only after validation and evidence closure.
6. **Promote** only through steward review and release decision paths.
7. **Publish** only released public-safe artifacts through governed interfaces.

[⬆ Back to top](#top)

---

## 7. Directory contract

Recommended shape:

```text
pipelines/cross_lane/
├── README.md                         # this file
├── PIPELINE_CONTRACT.md              # PROPOSED: umbrella cross-lane execution contract
├── registry.yml                      # PROPOSED: child-lane registry, if accepted
├── shared/                           # PROPOSED: shared cross-lane helpers only
├── riparian_vegetation/              # existing child lane
└── <future-cross-lane-slice>/         # PROPOSED only after placement review
```

Potential future child lanes must be reviewed before landing:

```text
pipelines/cross_lane/
├── habitat_species_join/              # PROPOSED / NEEDS VERIFICATION
├── fire_recovery_ecology/             # PROPOSED / NEEDS VERIFICATION
├── drought_ecology_context/           # PROPOSED / NEEDS VERIFICATION
├── invasive_spread_context/           # PROPOSED / NEEDS VERIFICATION
├── wetland_riparian_context/          # PROPOSED / NEEDS VERIFICATION
└── ecological_public_safety_review/   # PROPOSED / NEEDS VERIFICATION
```

Do not create those directories until each has owners, placement rationale, fixture-only plan, policy gates, negative tests, and rollback posture.

[⬆ Back to top](#top)

---

## 8. Current lanes

| Lane | Purpose | Status |
|---|---|---|
| [`riparian_vegetation/`](riparian_vegetation/) | Candidate riparian vegetation products across Hydrology, Flora, Habitat, Soil, Hazards, Agriculture, and related policy review. | Draft README exists; executable behavior NEEDS VERIFICATION. |

[⬆ Back to top](#top)

---

## 9. Required gates for every child lane

Each child lane must implement or defer to gates for:

1. **Ownership gate** — every input has an owning domain and object-family meaning.
2. **Source descriptor gate** — every input source has a stable identity and role.
3. **Rights gate** — unclear or restrictive rights fail closed.
4. **Sensitivity gate** — exact sensitive ecology, archaeology, cultural, private, infrastructure, or living-person exposure is denied, restricted, generalized, delayed, or quarantined.
5. **Join-induced risk gate** — derived products are checked for new risks created by combining otherwise-safe inputs.
6. **Temporal gate** — observation, retrieval, processing, valid, catalog, and release times remain distinct.
7. **Spatial fitness gate** — CRS, scale, precision, adjacency, buffer, and public-generalization limits are recorded.
8. **Evidence gate** — claim-like outputs require EvidenceBundle support or abstain.
9. **Validation gate** — schema and semantic validation emit finite outcomes.
10. **Policy gate** — policy decisions are recorded; no silent allow.
11. **Receipt gate** — every run records inputs, versions, hashes, parameters, outputs, and outcomes.
12. **No-direct-publish gate** — no child lane writes directly to public UI, public API, or `data/published/`.
13. **Catalog/triplet gate** — catalog and graph projections preserve provenance and do not replace canonical domain truth.
14. **Release gate** — public release requires ReleaseManifest, rollback target, correction path, and review state.

[⬆ Back to top](#top)

---

## 10. Sensitivity and public-safety posture

Cross-lane products are high-risk because joins can reveal or imply things no single input source reveals by itself.

Default posture:

- exact sensitive geometry is denied from public output;
- rare species, archaeology, sacred/cultural, private-property, living-person, infrastructure, and public-safety risks fail closed;
- uncertainty produces `ABSTAIN`, `DENY`, `ERROR`, quarantine, or reviewer handoff, not a confident map;
- map tiles, API payloads, graphs, and summaries must be evaluated as derived products;
- public products must be generalized, redacted, delayed, restricted, or withheld when needed;
- reviewers must be able to trace every derived output to source roles, EvidenceBundle state, policy decision, and release state.

> [!CAUTION]
> A cross-lane join can turn benign public context into sensitive derived knowledge. Evaluate the output, not just the inputs.

[⬆ Back to top](#top)

---

## 11. Specs, tests, fixtures, receipts, and proofs

Declarative specs should prefer a spec home, not this README:

```text
pipeline_specs/cross_lane/
├── README.md                         # PROPOSED / NEEDS VERIFICATION
└── riparian_vegetation/
    └── dry_run.yaml                  # PROPOSED / NEEDS VERIFICATION
```

Recommended tests:

```text
tests/pipelines/cross_lane/
├── README.md                         # PROPOSED / NEEDS VERIFICATION
├── test_no_direct_publish.py         # PROPOSED shared invariant test
└── riparian_vegetation/
```

Recommended fixtures:

```text
fixtures/pipelines/cross_lane/
├── valid/                            # PROPOSED / NEEDS VERIFICATION
├── invalid/                          # PROPOSED / NEEDS VERIFICATION
├── golden/                           # PROPOSED / NEEDS VERIFICATION
└── synthetic/                        # PROPOSED / NEEDS VERIFICATION
```

Run receipts belong under approved receipt homes, typically:

```text
data/receipts/pipeline/
```

Evidence bundles, validation reports, and proof packs belong under approved proof homes, typically:

```text
data/proofs/
```

[⬆ Back to top](#top)

---

## 12. Promotion, publication, and rollback

Cross-lane pipelines may prepare candidates. They do not publish.

Required promotion chain:

```text
cross-lane candidate
  -> cross-lane join receipt
  -> validation report
  -> policy decision
  -> EvidenceBundle closure
  -> catalog / triplet candidate
  -> steward review
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public-safe artifact
```

Rollback responsibilities:

- local candidate rollback preserves receipts and proof state;
- denied, abstained, errored, and quarantined runs remain auditable;
- invalidated candidates are removed from downstream consideration by state transition, not by hidden deletion;
- published artifact rollback is owned by `release/`, not by this directory;
- correction notices must point back to release, catalog/triplet, policy, and evidence state.

[⬆ Back to top](#top)

---

## 13. Definition of done

This README is done when it:

- explains `pipelines/cross_lane/` as a proposed execution umbrella, not a canonical domain root;
- preserves domain ownership and source-role boundaries;
- preserves lifecycle, evidence, policy, catalog, triplet, release, and rollback boundaries;
- keeps schemas, policies, fixtures, tests, data, receipts, proofs, and release decisions in their proper homes;
- names child-lane expectations;
- warns about join-induced sensitivity;
- denies direct publication;
- gives maintainers a safe expansion pattern.

Future executable cross-lane implementation is done only when it has:

- owners and review burden;
- source-descriptor coverage;
- no-network fixtures;
- schema-backed candidate records;
- cross-lane ownership tests;
- source-role, rights, sensitivity, and join-risk tests;
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
| `CROSS-LANE-001` | Should `pipelines/cross_lane/` be accepted as a stable pipeline umbrella, or should every child lane live under `pipelines/domains/<primary-domain>/` with explicit cross-lane specs? | NEEDS VERIFICATION |
| `CROSS-LANE-002` | Should the path use `cross_lane` or `cross-lane` if standardized by ADR? | NEEDS VERIFICATION |
| `CROSS-LANE-003` | Should a machine-readable `pipelines/cross_lane/registry.yml` exist, or should the registry live under `control_plane/` or `pipeline_specs/`? | PROPOSED / NEEDS VERIFICATION |
| `CROSS-LANE-004` | Which object family owns cross-lane candidates and join receipts? | PROPOSED / NEEDS ADR if new object family |
| `CROSS-LANE-005` | Which steward role arbitrates conflicts between contributing domain stewards? | NEEDS VERIFICATION |
| `CROSS-LANE-006` | Which CI job owns shared no-direct-publish and join-induced-risk tests? | UNKNOWN |
| `CROSS-LANE-007` | What public-safe generalization rules apply to cross-lane map surfaces? | NEEDS VERIFICATION |
| `CROSS-LANE-008` | Should `pipeline_specs/cross_lane/`, `tests/pipelines/cross_lane/`, and `fixtures/pipelines/cross_lane/` be created as matching lanes? | NEEDS VERIFICATION |

---

## Maintainer note

Keep the umbrella narrow. Add one child lane at a time, with a README, owners, no-network fixtures, negative tests, source-role checks, EvidenceBundle posture, policy decisions, and rollback plan before any public or semi-public surface is touched.

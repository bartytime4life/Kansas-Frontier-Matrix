<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-agriculture-readme
title: schemas/contracts/v1/agriculture/ — Agriculture Schema Compatibility Index
type: readme; directory-readme; schema-compatibility-index; non-authoritative-router
authority_class: compatibility-index
version: v1.2
status: draft; compatibility; transitional; index-only; repository-grounded
policy_label: public
owners:
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Agriculture domain steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
updated: 2026-07-20
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 13e1b27bf8cc4fdd4d88305532e69c444c07a4b5
  prior_blob: fcf276c5dea4e90afc057e38151fdc1f7c0927b8
  original_pre_v1_1_blob: 716b3fd1e73feaeba678e6800606604e7d621d16
related:
  - ../../../README.md
  - ../README.md
  - ../domains/README.md
  - ../domains/agriculture/README.md
  - ../../../../docs/domains/agriculture/README.md
  - ../../../../docs/domains/agriculture/DOMAIN.md
  - ../../../../docs/domains/agriculture/OBJECT_FAMILIES.md
  - ../../../../docs/domains/agriculture/SOURCE_REGISTRY.md
  - ../../../../docs/domains/agriculture/DATA_LIFECYCLE.md
  - ../../../../docs/domains/agriculture/CROSS_LANE.md
  - ../../../../docs/domains/agriculture/API_CONTRACTS.md
  - ../../../../docs/domains/agriculture/MAP_UI_CONTRACTS.md
  - ../../../../docs/domains/agriculture/EXPANSION_PLAN.md
  - ../../../../docs/domains/agriculture/VERIFICATION_BACKLOG.md
  - ../../../../contracts/domains/agriculture/README.md
  - ../../../../fixtures/domains/agriculture/README.md
  - ../../../../tests/domains/agriculture/README.md
  - ../../../../tools/validators/domains/agriculture/README.md
  - ../../../../docs/architecture/directory-rules.md
  - ../../../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - ../../../../docs/registers/DRIFT_REGISTER.md
tags: [kfm, schemas, contracts, v1, agriculture, compatibility, transitional, index-only, json-schema, no-parallel-authority]
notes:
  - "This directory contains only README.md and .gitkeep at the recorded evidence snapshot."
  - "Agriculture machine-schema files currently live under schemas/contracts/v1/domains/agriculture/; that lane is doctrine-aligned but remains proposed because ADR-0001 is proposed."
  - "This README is a router and drift guard. It does not make this flat lane or the domain lane accepted schema authority."
  - "Domain doctrine defines twelve Agriculture-owned object families; the observed nineteen direct schema files are mostly cross-cutting scaffolds and do not yet provide one-to-one domain-family coverage."
[/KFM_META_BLOCK_V2] -->

# `schemas/contracts/v1/agriculture/` — Agriculture Schema Compatibility Index

`schemas/contracts/v1/agriculture/` is an index-only compatibility lane that routes maintainers to the Agriculture domain schema surface without creating a second schema authority.

**Audience:** schema, Agriculture-domain, contract, validation, governance, and documentation maintainers.

> [!IMPORTANT]
> Do not add machine schemas to this flat lane. The current Directory Rules place domain-specific machine shape under `schemas/contracts/v1/domains/<domain>/`, while [ADR-0001](../../../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) is still `proposed`. Until that decision and any migration are closed, treat [`../domains/agriculture/`](../domains/agriculture/README.md) as the proposed domain lane and this directory as a compatibility pointer only.

[Purpose](#purpose) · [Authority level](#authority-level) · [Status](#status) · [Domain doctrine](#agriculture-domain-doctrine-crosswalk) · [Implementation crosswalk](#repository-implementation-crosswalk) · [What belongs here](#what-belongs-here) · [What does NOT belong here](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review burden](#review-burden) · [Related folders](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Evidence ledger](#evidence-ledger) · [Open verification](#open-verification) · [Rollback](#rollback)

## Purpose

This directory preserves discoverability for the older flat Agriculture schema path while preventing it from evolving independently.

It exists to:

- point readers and legacy references toward the proposed Agriculture domain schema lane;
- record the flat-path versus domain-path relationship;
- expose material schema, contract, fixture, validator, and CI maturity gaps;
- support a future ADR-backed migration, deprecation, or alias decision; and
- prevent documentation from upgrading permissive schema scaffolds into implementation, policy, evidence, or release claims.

This README documents repository state. It is not a JSON Schema, semantic contract, schema registry, migration manifest, policy decision, validation report, receipt, proof, release record, or publication authority.

## Authority level

**Compatibility / transitional / index-only.** The `schemas/` root owns machine-checkable shape. This flat lane owns no schema family and must not become a parallel Agriculture schema home.

The placement basis is:

1. [Directory Rules](../../../../docs/architecture/directory-rules.md) assign machine shape to `schemas/` and apply the domain lane pattern `schemas/contracts/v1/domains/<domain>/` to Agriculture.
2. [ADR-0001](../../../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) proposes `schemas/contracts/v1/` as the machine-schema home and `schemas/contracts/v1/domains/<domain>/` for domain-specific schemas.
3. [`schemas/README.md`](../../../README.md) preserves the meaning/shape/policy/proof split and warns against parallel authority.
4. The current repository contains this flat directory as a README-and-`.gitkeep` compatibility lane and contains Agriculture schema files in [`../domains/agriculture/`](../domains/agriculture/README.md).

The target path is therefore **CONFIRMED present**, but its long-term disposition remains **NEEDS VERIFICATION**. The proposed domain lane is not upgraded to accepted authority by this README.

## Status

### Compatibility status

| Concern | Current state | Evidence posture |
|---|---|---|
| Flat directory | `README.md` plus `.gitkeep`; no machine schema files | **CONFIRMED** at `main@13e1b27bf8cc4fdd4d88305532e69c444c07a4b5` |
| Lane class | Compatibility / transitional / index-only | **PROPOSED classification**, consistent with the prior README and Directory Rules anti-drift posture |
| Proposed domain lane | `schemas/contracts/v1/domains/agriculture/` exists | **CONFIRMED path / PROPOSED authority** |
| ADR status | ADR-0001 is `proposed`, not accepted | **CONFIRMED** from the ADR metadata and status block |
| Migration or deprecation decision | No accepted decision was verified for this flat lane | **NEEDS VERIFICATION** |
| Generated or mirrored status | No generator, synchronization command, or mirror notice was found for this README | **UNKNOWN** beyond the inspected paths; treat as manually maintained |
| Public or release authority | None | **CONFIRMED boundary** |

### Repository fit

```text
schemas/
└── contracts/
    └── v1/
        ├── agriculture/
        │   ├── .gitkeep
        │   └── README.md                    # this compatibility index
        └── domains/
            └── agriculture/
                ├── README.md                # proposed domain schema index
                ├── *.schema.json            # 19 direct schema scaffolds at the snapshot
                ├── hydrology-ext/README.md  # extension-placement question remains open
                └── receipts/README.md       # receipt-schema placement remains open
```

### Bounded domain-schema snapshot

The direct Agriculture domain lane contains 19 `*.schema.json` files at the recorded base commit. All declare JSON Schema Draft 2020-12, all have distinct `$id` values within that bounded set, all carry `x-kfm.status: PROPOSED`, and all permit unspecified properties.

| Shape group | Files | Observed structure | Interpretation |
|---|---|---|---|
| Empty-property scaffolds | `aggregation_receipt`, `agriculture_decision_envelope`, `agriculture_feature_dto`, `crop_observation` | No declared properties or required fields; `additionalProperties: true` | **PROPOSED scaffold**; not a meaningful payload contract |
| ID-only scaffolds | `catalog_matrix`, `correction_notice`, `decision_envelope`, `domain_feature_identity`, `domain_layer_descriptor`, `domain_observation`, `domain_validation_report`, `evidence_bundle`, `evidence_drawer_payload`, `layer_manifest`, `promotion_decision`, `release_manifest`, `rollback_card`, `run_receipt`, `source_state_hash` | Requires `id`; exposes only `id`, `spec_hash`, and `version`; `additionalProperties: true` | **PROPOSED minimal scaffold**; not field-complete domain validation |

The bounded inventory also exposes these conflicts and gaps:

- `$id` uses two namespaces: four `kfm://schemas/...` identifiers and fifteen `https://schemas.kfm.local/...` identifiers. Namespace authority is **NEEDS VERIFICATION**.
- Four schema-declared contract paths exist exactly. Fifteen exact targets are absent; one absent target, `aggregation_receipt.md`, has a hyphenated semantic-contract counterpart at [`contracts/domains/agriculture/aggregation-receipt.md`](../../../../contracts/domains/agriculture/aggregation-receipt.md).
- None of the fifteen schema-declared family fixture directories exists. The Agriculture fixture root contains eight named fixture lanes plus `valid`, `invalid`, and `golden` indexes, but all observed contents are README, `.gitkeep`, or `PLACEHOLDER.md` scaffolding rather than deterministic JSON payloads.
- Two schema-declared validator paths exist, but both are four-line `NotImplementedError` placeholders. Two additional Agriculture validator files in the same lane are also placeholders; no field-level Agriculture validator was established.
- [`schema-validation.yml`](../../../../.github/workflows/schema-validation.yml) parses all schema JSON, checks Draft 2020-12 meta-schema validity, and requires unique canonical-v1 `$id` values. Its configured aggregate fixture validators cover six shared families, not the Agriculture schemas listed here.
- Seven `tests/domains/agriculture/test_*.py` modules exist. One is a four-line `assert True` smoke placeholder; six contain only `PROPOSED placeholder` module docstrings, so filename presence is **CONFIRMED** while substantive Agriculture assertion coverage remains **UNESTABLISHED**.
- [`domain-agriculture.yml`](../../../../.github/workflows/domain-agriculture.yml) is out of sync with that test tree: [PR #1468's Agriculture run](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/29726156611) failed because `test_vegetation_index_mask_time.py` exists, while the workflow assumes any test beyond `test_nass_aggregate_only.py` means the lane has graduated. This is **CONFIRMED workflow/test-topology drift**, not Agriculture conformance.
- The proposed domain-lane README currently describes only one known schema, while the pinned tree contains 19. Treat that README inventory as stale until it is regenerated and reviewed.
- The 27 direct Markdown files under [`docs/domains/agriculture/`](../../../../docs/domains/agriculture/README.md) carry a much richer bounded-context, source, lifecycle, cross-lane, API, map/UI, and expansion model than the machine schemas. Several still say no mounted repository was inspected and therefore must be read as doctrine lineage or proposed design, not current implementation evidence.

No item above establishes source truth, semantic completeness, EvidenceBundle closure, policy approval, rights or sensitivity clearance, runtime use, release readiness, or publication.

## Agriculture domain doctrine crosswalk

This section restores the Agriculture domain model that the schema-only inventory does not express. It is a **routing crosswalk**, not a second semantic contract. The governing narrative remains in [`docs/domains/agriculture/`](../../../../docs/domains/agriculture/README.md), especially the [domain glossary and conceptual model](../../../../docs/domains/agriculture/DOMAIN.md), [object-family register](../../../../docs/domains/agriculture/OBJECT_FAMILIES.md), [source registry](../../../../docs/domains/agriculture/SOURCE_REGISTRY.md), [lifecycle](../../../../docs/domains/agriculture/DATA_LIFECYCLE.md), and [cross-lane contracts](../../../../docs/domains/agriculture/CROSS_LANE.md).

### Mission and boundary

**CONFIRMED doctrine / PROPOSED implementation:** Agriculture represents crops, field candidates, rotations, yields, irrigation relationships, conservation practices, soil-crop suitability, agricultural-economy observations, supply-chain context, and drought or pest stress in public-safe aggregate or permissioned form.

Agriculture does not own soil survey truth, water observations, weather observations, hazard alerts, living-person or land-title identity, plant or animal taxonomy, geology, or changing county geometry. It cites those bounded contexts through governed cross-lane references and must not redefine them.

Field polygons and operator-resolvable records can be sensitive. Public products default to county, HUC, or governed grid aggregation; operator and farm joins are denied unless rights, sensitivity, evidence, review, and a public-safe transform are explicitly closed.

### Twelve Agriculture-owned object families

The domain corpus identifies twelve owned families. Their names are doctrinally established, but their machine-schema coverage at the pinned snapshot is uneven.

| Domain family | Direct domain schema observed | Current machine-shape posture |
|---|---|---|
| `CropObservation` | `crop_observation.schema.json` | Empty-property, permissive **PROPOSED scaffold** |
| `AggregationReceipt` | `aggregation_receipt.schema.json` | Empty-property, permissive **PROPOSED scaffold**; semantic filename separator conflict remains |
| `FieldCandidate` | None by that name | **PROPOSED doctrine / schema NEEDS VERIFICATION** |
| `CropRotation` | None by that name | **PROPOSED doctrine / schema NEEDS VERIFICATION** |
| `YieldObservation` | None by that name | **PROPOSED doctrine / schema NEEDS VERIFICATION** |
| `IrrigationLink` | None by that name | **PROPOSED doctrine / schema NEEDS VERIFICATION** |
| `ConservationPractice` | None by that name | **PROPOSED doctrine / schema NEEDS VERIFICATION** |
| `SoilCropSuitability` | None by that name | **PROPOSED doctrine / schema NEEDS VERIFICATION** |
| `AgriculturalEconomyObservation` | None by that name | **PROPOSED doctrine / schema NEEDS VERIFICATION** |
| `SupplyChainNode` | None by that name | **PROPOSED doctrine / schema NEEDS VERIFICATION** |
| `DroughtStressIndicator` | None by that name | **PROPOSED doctrine / schema NEEDS VERIFICATION** |
| `PestStressIndicator` | None by that name | **PROPOSED doctrine / schema NEEDS VERIFICATION** |

The other 17 direct schema files are supporting or cross-cutting scaffolds rather than dedicated schemas for the ten missing domain families:

| Support surface | Observed schema scaffolds | Intended role; not proof of implementation |
|---|---|---|
| Governed feature and decision surfaces | `agriculture_feature_dto`, `agriculture_decision_envelope`, `decision_envelope`, `evidence_drawer_payload` | Governed API, Evidence Drawer, and finite response projection |
| Domain identity, observation, and validation | `domain_feature_identity`, `domain_observation`, `domain_validation_report`, `source_state_hash` | Shared identity, observation envelope, validation result, and source-state pinning |
| Evidence, catalog, and layer description | `evidence_bundle`, `catalog_matrix`, `domain_layer_descriptor`, `layer_manifest` | Evidence resolution, catalog closure, and released layer description |
| Promotion, release, correction, and rollback | `promotion_decision`, `release_manifest`, `correction_notice`, `rollback_card` | Governed lifecycle and reversibility surfaces |
| Process memory | `run_receipt` | Run provenance; distinct from proof, policy, promotion, or publication |

### Source families and source roles

The [source registry](../../../../docs/domains/agriculture/SOURCE_REGISTRY.md) requires source role to survive admission and promotion. Rights and live-source activation remain **NEEDS VERIFICATION** until a reviewed `SourceDescriptor` establishes them.

| Source family | Proposed primary role | Boundary that schemas and validators must preserve |
|---|---|---|
| USDA NASS CDL | `modeled` annual crop classification | Pin product year and `classmap_version`; never label as field observation |
| USDA NASS QuickStats / Crop Progress | `aggregate` | County/state/crop-year use; deny field or operator inference |
| NRCS SSURGO / SDA | `observed` survey evidence | Preserve MUKEY, component/horizon lineage, scale, vintage, and fitness-for-use |
| NRCS gSSURGO | `aggregate` derivative | Do not relabel as observed pedon evidence |
| Kansas Mesonet, NRCS SCAN, NOAA USCRN | `observed` station measurements | Preserve units, depth, QC, station support, and observation time |
| NASA SMAP and HLS/HLS-VI | `modeled` or derived context | Preserve product level, mask/QC, model identity, time, and uncertainty |
| NRCS conservation-practice records | `administrative` or `observed`, source dependent | Restrict operator-identifying detail and preserve terms |
| Irrigation and water-use records | `administrative` or `observed`, source dependent | Govern Hydrology/People-Land joins; deny operator-resolvable public output |
| Crop-insurance, market, and economy sources | `administrative` or `aggregate` | Publish only when redistribution rights and aggregation close |
| Local extension sources | Source-specific | No default authority upgrade; each source requires explicit role and rights review |

### Identity, space, and time

Agriculture schemas are expected to preserve, where applicable:

- stable object identity plus source identity and source role;
- crop year and growing season;
- observed, source, retrieval, processing, and release time rather than one collapsed timestamp;
- geometry identity, CRS, scale, and `geography_version_id` for county/HUC/grid aggregates;
- `classmap_version` for CDL-derived comparisons;
- model identity, assumptions, support type, uncertainty, and quality flags for derived indicators; and
- sensitivity, rights, audience class, evidence references, validation state, correction state, and rollback target.

A domain-family schema that omits these fields may still be legal JSON Schema, but it is not yet sufficient for the domain doctrine.

### Governed surfaces and finite outcomes

The [API](../../../../docs/domains/agriculture/API_CONTRACTS.md) and [Map/UI](../../../../docs/domains/agriculture/MAP_UI_CONTRACTS.md) plans describe downstream consumers, not schema authority:

- crop/soil/weather dashboards, CDL crop maps, county/HUC aggregate panels, irrigation context, suitability, and drought/pest-stress context;
- Evidence Drawer inspection, source comparison, correction submission, public-safe export, review, promotion, and rollback actions;
- terrain-draped SSURGO/gNATSGO diffs and NDVI time series only from governed released raster artifacts;
- runtime outcomes `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`, with any additional narrowed/bounded vocabulary resolved by the governing envelope contract;
- policy outcomes kept separate from runtime and workflow outcomes; and
- AI limited to evidence-bounded explanation over released or review-authorized evidence, with citation validation and receipts; direct RAW/WORK/QUARANTINE access and unsupported authoritative claims are denied.

MapLibre, Focus Mode, search, graph, analytics, and generated language remain derivative surfaces. None may turn a permissive schema scaffold, a live source, or an internal candidate into public truth.

### First credible thin slice

The domain corpus's first proposed vertical slice is one county, one crop year, and one crop using:

1. CDL with a pinned class ontology/version;
2. QuickStats county aggregates;
3. SSURGO suitability with survey lineage and scale caveats;
4. Kansas Mesonet weather or soil-moisture context;
5. one EvidenceBundle and AggregationReceipt per public aggregate;
6. explicit denial of field-level and operator-level detail;
7. deterministic no-network positive and negative fixtures; and
8. promotion, release, correction, and rollback records that remain distinct.

That slice is **PROPOSED**. The files currently in this repository do not close those acceptance conditions.

## Repository implementation crosswalk

The current Agriculture repository surface is broader than the schema directory but remains documentation- and scaffold-heavy.

| Responsibility surface | Confirmed repository state | Maturity limit |
|---|---|---|
| Domain documentation | 27 direct Markdown files plus sublane, policy, and runbook docs | Rich doctrine/proposal corpus; several current-state statements are stale or explicitly unverified |
| Semantic contracts | `README.md` plus five Agriculture contract files | Only four are exact `x-kfm.contract` targets; object-family pairing is incomplete |
| Machine schemas | 19 direct `PROPOSED`, permissive Draft 2020-12 scaffolds | Ten of twelve Agriculture-owned families have no direct schema by doctrinal family name |
| Fixtures | 24 files across catalog, field-level-attempt, golden, HLS-VI, NASS, no-network, release, soil-moisture, SSURGO, valid, and invalid lanes | README, `.gitkeep`, and placeholder material only; no deterministic payload corpus observed |
| Tests | Seven `test_*.py` modules plus boundary READMEs | One no-op smoke assertion and six docstring-only placeholders; targeted assertions are not established |
| Validators | Four Python files under `tools/validators/domains/agriculture/` | All raise `NotImplementedError`; the parallel `tools/validators/agriculture/` lane is README-only |
| Generic schema CI | `schema-validation` passed for PR #1468 | Establishes JSON/meta-schema/ID checks within workflow scope, not Agriculture semantics |
| Agriculture CI | `domain-agriculture` failed for PR #1468 on test-topology drift | Confirms workflow assumptions and repository test filenames disagree; no Agriculture validation proof |
| Release/publication | Release and policy documentation exists | No Agriculture release, publication, or public-surface authority is established here |

### Doctrine-to-machine closure gates

Before any Agriculture schema family can move beyond scaffold status, reviewers should require:

1. semantic contract pairing and stable identity;
2. field-complete Draft 2020-12 shape with explicit required fields and bounded `additionalProperties` posture;
3. source-role, rights, sensitivity, audience, temporal, spatial, and uncertainty invariants;
4. valid, invalid, boundary, stale, source-role-mismatch, and public-denial fixtures;
5. substantive validator and test implementation wired to CI;
6. EvidenceBundle, AggregationReceipt, citation, policy, promotion, and catalog closure as applicable;
7. correction, withdrawal, and rollback behavior; and
8. steward review and registry activation without treating merge as publication.

## What belongs here

- `README.md` as the compatibility router and drift guard.
- `.gitkeep` while the compatibility directory must remain addressable.
- A short, reviewed migration, deprecation, or mirror notice when an accepted decision requires one.
- Stable links to the proposed domain schema lane, semantic contracts, fixtures, validators, tests, workflows, ADRs, and drift records.
- Evidence-bounded status notes that clearly distinguish path presence, schema shape, validation coverage, and release state.

Any additional file must keep this lane non-authoritative and must identify its canonical source, synchronization rule, owner, sunset or review trigger, and rollback path.

## What does NOT belong here

- `*.schema.json`, JSON-LD contexts, or other machine-shape definitions.
- Hand-maintained or generated copies of schemas from `../domains/agriculture/`.
- Semantic contract prose or object-family definitions.
- Policy rules, rights decisions, sensitivity decisions, redaction rules, or release decisions.
- Valid, invalid, golden, live-source, or production payloads.
- Validator or runtime implementation.
- Schema registry records, source registry records, EvidenceBundles, proofs, receipts, catalogs, manifests, or lifecycle data.
- Public API, map, UI, Focus Mode, export, search, graph, or model-runtime behavior.
- Claims that schema presence, JSON validity, a green workflow, a commit, or a pull request proves correctness or publication.

## Inputs

Changes to this index must be grounded in the smallest sufficient evidence set:

- current [Directory Rules](../../../../docs/architecture/directory-rules.md) and any accepted amending ADR;
- [ADR-0001](../../../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) and its current lifecycle state;
- the exact flat-lane and proposed domain-lane tree at a pinned commit;
- the Agriculture bounded-context, object-family, source, lifecycle, cross-lane, API, Map/UI, expansion, and verification documents under [`docs/domains/agriculture/`](../../../../docs/domains/agriculture/README.md), with their self-declared evidence limits preserved;
- machine schema metadata, including `$schema`, `$id`, `required`, `properties`, `additionalProperties`, and `x-kfm` pointers;
- paired semantic contracts under [`contracts/domains/agriculture/`](../../../../contracts/domains/agriculture/README.md);
- fixtures, validators, tests, workflows, schema-registry records, migrations, and drift entries that actually exist; and
- policy, evidence, review, release, correction, and rollback records only when a claim depends on them.

Lineage documents and proposed paths may guide review, but they do not prove implementation. Memory and README prose do not upgrade a schema or integration claim to **CONFIRMED**.

## Outputs

This lane emits no runtime or lifecycle object.

Its only supported outputs are:

- a human-readable routing index;
- a compatibility classification;
- a bounded snapshot of observed drift and maturity;
- review and validation instructions; and
- pointers for a future ADR-backed migration or deprecation.

It does not emit schemas, generated mirrors, registry entries, validation reports, policy decisions, evidence, receipts, proofs, catalogs, release records, published artifacts, or public responses.

## Validation

### Documentation checks

For this README:

- verify one H1, consecutive heading levels, balanced fences, readable tables, and a final newline;
- verify every repository-relative link against the resulting branch;
- confirm the KFM Meta Block markers are balanced and the preserved `doc_id` remains unique;
- confirm the flat lane still contains no machine schema files;
- compare the pinned domain-schema inventory and maturity claims with the actual JSON files;
- compare the twelve-family doctrine register with dedicated schema, contract, fixture, validator, and test coverage;
- inventory the complete Agriculture fixture and test trees instead of inferring maturity from their root READMEs;
- scan for credentials, restricted payloads, private identities, or exact sensitive locations; and
- inspect the complete base-to-head diff for unrelated changes.

### Repository checks and their limits

| Check | What it establishes | What it does not establish |
|---|---|---|
| JSON parsing of `schemas/contracts/v1/domains/agriculture/*.schema.json` | The inspected files are syntactically valid JSON | Semantic completeness or admissibility |
| Draft 2020-12 meta-schema check | The inspected schema documents are legal Draft 2020-12 schemas | Useful Agriculture constraints, fixtures, or runtime enforcement |
| Unique `$id` check in [`schema-validation.yml`](../../../../.github/workflows/schema-validation.yml) | No duplicate `$id` exists in the workflow's canonical-v1 scan when the job passes | Accepted namespace, stable identity, or registry activation |
| `make schemas` | The configured aggregate validator runner completes | Agriculture-specific schema validation; the configured families are shared source/evidence/runtime families |
| `python -m pytest -q tests/schemas tests/contracts` | The repository-owned schema/contract suite passes within its collected scope | Agriculture-domain test coverage unless those tests are collected there |
| Static inspection of `tests/domains/agriculture/test_*.py` | One no-op smoke assertion and six docstring-only placeholder modules are present | Substantive Agriculture behavior, negative cases, or enforceability |
| [`domain-agriculture.yml`](../../../../.github/workflows/domain-agriculture.yml) | The workflow's expected topology and readiness assumptions | Executable Agriculture validation, proof, release readiness, or publication; PR #1468 demonstrates current topology drift |

Do not promote this lane, remove it, add schemas to it, or call the domain lane active solely because generic schema validation passes.

## Review burden

[`.github/CODEOWNERS`](../../../../.github/CODEOWNERS) routes all `/schemas/` changes to `@bartytime4life`. That is review routing, not proof that independent schema, Agriculture, contract, validation, policy, or release review occurred.

Before approving a change here, reviewers must confirm:

- [ ] the flat lane remains compatibility/index-only;
- [ ] no schema definition or divergent mirror was added;
- [ ] the Directory Rules and ADR-0001 status are represented accurately;
- [ ] schema counts, `$id` namespaces, contract pointers, fixture roots, validator paths, and CI claims match the pinned tree;
- [ ] unresolved schema-home, receipt-family, extension-lane, and naming conflicts remain visible;
- [ ] schema validity is not presented as evidence, policy permission, release approval, or publication;
- [ ] public clients remain downstream of governed interfaces and released artifacts;
- [ ] the generated-work receipt is valid and remains pending human review until an authorized reviewer acts; and
- [ ] rollback restores the prior blob without rewriting shared history.

A migration, deprecation, schema-home change, or new parallel definition requires the appropriate schema, Agriculture-domain, contract, validation, migration, and governance review in addition to GitHub code-owner routing.

## Related folders

| Path | Relationship | Current posture |
|---|---|---|
| [`../../../README.md`](../../../README.md) | Schema responsibility root | **CONFIRMED root boundary** |
| [`../README.md`](../README.md) | v1 schema-family index | **CONFIRMED / mixed maturity** |
| [`../domains/README.md`](../domains/README.md) | Parent domain-schema index | **CONFIRMED file / proposed lane model** |
| [`../domains/agriculture/`](../domains/agriculture/README.md) | Agriculture machine-shape lane and direct schema files | **CONFIRMED path / PROPOSED authority / stale README inventory** |
| [`../domains/agriculture/hydrology-ext/`](../domains/agriculture/hydrology-ext/README.md) | Agriculture-Hydrology extension index | **NEEDS VERIFICATION / cross-domain placement-sensitive** |
| [`../domains/agriculture/receipts/`](../domains/agriculture/receipts/README.md) | Agriculture receipt-schema index | **NEEDS VERIFICATION / receipt-family placement-sensitive** |
| [`../../../../docs/domains/agriculture/`](../../../../docs/domains/agriculture/README.md) | Agriculture bounded-context and implementation-planning corpus | **CONFIRMED paths / mixed doctrine, proposal, and stale current-state claims** |
| [`../../../../docs/domains/agriculture/DOMAIN.md`](../../../../docs/domains/agriculture/DOMAIN.md) | Ubiquitous language, twelve-family conceptual model, invariants, and AI boundary | **CONFIRMED document / proposed implementation** |
| [`../../../../docs/domains/agriculture/OBJECT_FAMILIES.md`](../../../../docs/domains/agriculture/OBJECT_FAMILIES.md) | Twelve-family register and proposed pairings | **CONFIRMED register / incomplete machine coverage** |
| [`../../../../docs/domains/agriculture/SOURCE_REGISTRY.md`](../../../../docs/domains/agriculture/SOURCE_REGISTRY.md) | Source families, roles, rights, and activation posture | **CONFIRMED document / source activation NEEDS VERIFICATION** |
| [`../../../../docs/domains/agriculture/DATA_LIFECYCLE.md`](../../../../docs/domains/agriculture/DATA_LIFECYCLE.md) | Agriculture lifecycle, aggregation, proof, and fail-closed model | **CONFIRMED document / implementation unestablished** |
| [`../../../../docs/domains/agriculture/CROSS_LANE.md`](../../../../docs/domains/agriculture/CROSS_LANE.md) | Soil, Hydrology, Atmosphere, Habitat, Fauna, Flora, Geology, Hazards, People/Land, and Matrix edges | **CONFIRMED document / validators proposed** |
| [`../../../../docs/domains/agriculture/API_CONTRACTS.md`](../../../../docs/domains/agriculture/API_CONTRACTS.md) | Governed API and finite-outcome plan | **CONFIRMED document / routes proposed** |
| [`../../../../docs/domains/agriculture/MAP_UI_CONTRACTS.md`](../../../../docs/domains/agriculture/MAP_UI_CONTRACTS.md) | Aggregate-first map, Evidence Drawer, Focus Mode, and trust-visible UI plan | **CONFIRMED document / surfaces proposed** |
| [`../../../../docs/domains/agriculture/EXPANSION_PLAN.md`](../../../../docs/domains/agriculture/EXPANSION_PLAN.md) | Sequenced closure waves and county-year thin slice | **CONFIRMED document / execution proposed** |
| [`../../../../contracts/domains/agriculture/`](../../../../contracts/domains/agriculture/README.md) | Agriculture semantic contracts | **CONFIRMED path / partial pairing** |
| [`../../../../fixtures/domains/agriculture/`](../../../../fixtures/domains/agriculture/README.md) | Agriculture fixture index | **CONFIRMED documentation / declared schema-family fixtures absent** |
| [`../../../../tests/domains/agriculture/`](../../../../tests/domains/agriculture/README.md) | Agriculture enforceability boundary | **CONFIRMED seven Python module names / one no-op assertion / six docstring-only placeholders** |
| [`../../../../tools/validators/domains/agriculture/`](../../../../tools/validators/domains/agriculture/README.md) | Agriculture edge-validator lane | **CONFIRMED files / placeholder implementations** |
| [`../../../../policy/domains/agriculture/`](../../../../policy/domains/agriculture/README.md) | Agriculture policy boundary | **Separate authority; not changed here** |
| [`../../../../release/agriculture/`](../../../../release/agriculture/README.md) | Agriculture release orientation | **Separate authority; blocked/held posture** |

## ADRs

### ADR-0001 — schema home

[ADR-0001](../../../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) proposes:

- `schemas/contracts/v1/` for machine-checkable schemas;
- `schemas/contracts/v1/domains/<domain>/` for domain-specific schemas;
- `contracts/` for semantic meaning; and
- no divergent machine definitions across `schemas/` and `contracts/`.

Its current status is `proposed`. This README follows its anti-drift direction without claiming the decision is accepted.

### Unresolved lane decision

No accepted ADR or migration record was verified that classifies `schemas/contracts/v1/agriculture/` as a permanent alias, generated mirror, deprecated path, or removable directory. Until that decision exists:

1. keep this lane index-only;
2. place no schema files here;
3. do not silently redirect or delete the path;
4. record any migration mapping and downstream consumer impact; and
5. preserve rollback to the prior path state.

The inspected [`DRIFT_REGISTER.md`](../../../../docs/registers/DRIFT_REGISTER.md) does not yet contain an Agriculture flat-versus-domain schema-lane entry. Add one when a migration or deprecation decision enters scope; this documentation-only revision does not create that decision.

## Last reviewed

| Field | Value |
|---|---|
| Review date | 2026-07-20 |
| Repository snapshot | `bartytime4life/Kansas-Frontier-Matrix` `main@13e1b27bf8cc4fdd4d88305532e69c444c07a4b5` |
| Flat-lane prior blob | `fcf276c5dea4e90afc057e38151fdc1f7c0927b8` (v1.1); original pre-v1.1 blob `716b3fd1e73feaeba678e6800606604e7d621d16` |
| Review state | Follow-up revision requested after v1.1; independent approval not established |
| Next review trigger | ADR-0001 status change; flat-lane migration/deprecation decision; Agriculture schema inventory change; `$id` namespace decision; contract/fixture/validator/test activation; child-lane placement decision; or schema workflow change |

## Evidence ledger

| Evidence | Observation supported | Truth status | Does not prove |
|---|---|---|---|
| `schemas/contracts/v1/agriculture/` at the pinned commit | Directory contains `README.md` and `.gitkeep`, with no schema definitions | **CONFIRMED** | Long-term alias policy |
| [`Directory Rules`](../../../../docs/architecture/directory-rules.md) | `schemas/` owns machine shape; domains belong inside responsibility roots | **CONFIRMED doctrine / specific placement subject to stated limits** | Accepted ADR-0001 or implementation completeness |
| [ADR-0001](../../../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) | Proposed schema-home and domain-lane decision | **CONFIRMED text / PROPOSED decision** | Accepted governance state |
| [`docs/domains/agriculture/`](../../../../docs/domains/agriculture/README.md) | Twenty-seven direct domain documents carry the missing mission, boundary, object-family, source, lifecycle, cross-lane, API, Map/UI, and expansion model | **CONFIRMED file inventory / mixed truth posture** | Current runtime, validator, release, or publication state |
| [`../domains/agriculture/`](../domains/agriculture/README.md) plus direct schema JSON | Nineteen direct, permissive, `PROPOSED` schema scaffolds and two child indexes exist | **CONFIRMED bounded inventory** | Semantic completeness, fixture closure, validator enforcement, or runtime use |
| [`contracts/domains/agriculture/`](../../../../contracts/domains/agriculture/README.md) | Four exact schema-declared contract targets and one hyphenated counterpart exist | **CONFIRMED bounded inventory** | Complete contract pairing |
| [`fixtures/domains/agriculture/`](../../../../fixtures/domains/agriculture/README.md) | Named fixture lanes exist, but all observed files are README, `.gitkeep`, or placeholder material and schema-declared family roots are absent | **CONFIRMED recursive inventory** | Deterministic positive or negative fixture coverage |
| [`tests/domains/agriculture/`](../../../../tests/domains/agriculture/README.md) | Seven `test_*.py` files exist: one no-op smoke assertion and six docstring-only placeholders | **CONFIRMED recursive inventory** | Substantive Agriculture behavior or negative-test enforcement |
| Agriculture validator scripts and READMEs | Four per-domain Agriculture validator filenames are `NotImplementedError` placeholders | **CONFIRMED** | Future validator design or activation |
| [`schema-validation.yml`](../../../../.github/workflows/schema-validation.yml) and PR #1468 | Generic schema JSON, meta-schema, identity, configured-fixture, and shared schema/contract checks passed | **CONFIRMED workflow run** | Agriculture-specific conformance |
| [`domain-agriculture.yml`](../../../../.github/workflows/domain-agriculture.yml) and PR #1468 | Read-only readiness workflow failed on its stale test-topology assumption | **CONFIRMED workflow/test drift** | Agriculture validation, proof, release, or publication |

## Open verification

- [ ] Decide whether this flat lane is a permanent compatibility alias, temporary transition, deprecated path, or removal candidate.
- [ ] Accept, revise, supersede, or reject ADR-0001 through authorized review.
- [ ] Add or link the Agriculture flat-versus-domain lane decision in the drift and migration records.
- [ ] Reconcile the proposed domain-lane README with the 19-file schema inventory.
- [ ] Reconcile the twelve Agriculture-owned doctrinal families with dedicated semantic contracts and machine schemas; do not substitute cross-cutting envelope scaffolds for missing domain-family shape.
- [ ] Resolve the two `$id` namespace patterns and register accepted identities.
- [ ] Resolve `aggregation-receipt.md` versus `aggregation_receipt.md` without silently changing object identity.
- [ ] Decide whether receipt schemas belong in the Agriculture domain root, its `receipts/` child, or the shared receipt family.
- [ ] Decide whether `hydrology-ext/` is an Agriculture-owned extension or a cross-domain schema concern.
- [ ] Complete semantic contracts or explicitly profile shared contracts for every Agriculture schema.
- [ ] Add deterministic valid and invalid fixtures for accepted Agriculture schema families.
- [ ] Replace placeholder validators with reviewed implementations and replace the no-op/docstring-only test modules with deterministic assertions.
- [ ] Reconcile `domain-agriculture.yml` with the seven-file test topology so a filename does not falsely imply accepted executable coverage.
- [ ] Confirm schema registry, policy, evidence, release, correction, and rollback integration before promoting any schema beyond scaffold status.

## Rollback

Before merge, rollback means closing or abandoning the follow-up draft pull request; deleting its review branch is a separate cleanup action.

After merge, create a transparent revert of the follow-up implementation or merge commit, restoring v1.1 blob `fcf276c5dea4e90afc057e38151fdc1f7c0927b8`, then re-run the same Markdown, link, doctrine-crosswalk, schema-structure, recursive fixture/test inventory, and remote-diff checks. Do not force-push or rewrite shared history.

## Changelog

### v1.2 — 2026-07-20

- Added the missing Agriculture mission, boundary, twelve-family model, source-role matrix, space/time/identity expectations, governed surfaces, and first credible thin slice as non-authoritative crosswalks.
- Routed readers to the existing Agriculture bounded-context, object, source, lifecycle, cross-lane, API, Map/UI, expansion, and verification documents.
- Distinguished the twelve Agriculture-owned object families from the nineteen observed supporting and cross-cutting schema scaffolds.
- Corrected the fixture and test inventory: named fixture lanes contain documentation/placeholders; seven Python test modules contain one no-op smoke assertion and six docstring-only placeholders.
- Recorded PR #1468's passing generic schema validation and failing Agriculture readiness job as workflow/test-topology drift rather than conformance.

### v1.1 — 2026-07-20

- Reclassified the flat path as a bounded compatibility/transitional index rather than a candidate schema home.
- Added a pinned repository evidence snapshot and current two-file flat-lane inventory.
- Recorded the 19-file proposed domain-schema inventory, permissive scaffold shapes, split `$id` namespaces, partial contract pairing, absent declared fixture roots, placeholder validators, and CI limits.
- Added the Directory Rules README contract sections, review burden, evidence ledger, open verification, and transparent rollback.
- Preserved the existing `doc_id`, Agriculture routing purpose, no-parallel-authority rule, compatibility boundary, review checklist intent, and unresolved migration posture.

---

**Compatibility rule:** keep this lane pointer-only until an accepted decision and verified migration establish a different role.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/data-processed-atmosphere-climate-anomaly-readme
title: data/processed/atmosphere/climate_anomaly/ — Atmosphere Climate-Anomaly Processed Data
version: v0.2.0
type: directory-readme
subtype: processed-atmosphere-climate-anomaly-lane
status: repository-grounded draft; ownership convention, payload inventory, enforceable schema, validators, fixtures, receipts, proof, release, and runtime behavior remain bounded
owners:
  - "NEEDS VERIFICATION — Atmosphere domain steward"
  - "NEEDS VERIFICATION — climate, baseline, and anomaly steward"
  - "NEEDS VERIFICATION — aggregation, source-role, data-quality, and scientific-method reviewers"
  - "NEEDS VERIFICATION — data, evidence, policy, release, correction, rollback, and docs stewards"
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-07-25
policy_label: public-doc; processed-stage; atmosphere; climate-anomaly; baseline-relative-context; aggregation-aware; source-role-aware; release-gated; no-direct-public-path
path: data/processed/atmosphere/climate_anomaly/README.md
truth_posture: >
  CONFIRMED exact target path, prior blob, Directory Rules placement, current Atmosphere parent lane,
  ClimateAnomaly semantic contract, paired scaffold schema posture, mandatory baseline anchor,
  aggregate/climate sibling lane, and PROCESSED lifecycle boundary / PROPOSED lane-local admission
  profile, normalized anomaly packet, comparability rules, and downstream promotion expectations /
  UNKNOWN recursive payload inventory, production validators, fixtures, receipts, proof closure,
  release instances, hosting, and public behavior / NEEDS VERIFICATION accountable owners,
  canonical ownership between climate_anomaly and aggregate/climate, accepted variables and methods,
  baseline comparability rules, correction propagation, cache invalidation, and rollback drills
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 3843be327db500da76f62e04c9fb0f5c903a3c69
  prior_blob: 305ce2eae73e5ad7d7684b0d5e616f1df01ee69a
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  atmosphere_parent_blob: e37ce206f396f832c414fc46a70dd9cd9b3f64e4
  climate_anomaly_contract_blob: b80f840e18ed1da45f82112f7eb81517a4bf6999
  aggregate_climate_blob: 73794645c682c74937e76f5dee12dff72e126c80
related:
  - ../README.md
  - ../aggregate/climate/README.md
  - ../../README.md
  - ../../../README.md
  - ../../../../docs/domains/atmosphere/README.md
  - ../../../../docs/domains/atmosphere/CANONICAL_PATHS.md
  - ../../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md
  - ../../../../docs/domains/atmosphere/POLICY.md
  - ../../../../docs/domains/atmosphere/PUBLICATION_POSTURE.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../contracts/domains/atmosphere/ClimateAnomaly.md
  - ../../../../contracts/domains/atmosphere/ClimateNormal.md
  - ../../../../contracts/domains/atmosphere/TemperatureObservation.md
  - ../../../../contracts/domains/atmosphere/PrecipitationObservation.md
  - ../../../../schemas/contracts/v1/domains/atmosphere/ClimateAnomaly.schema.json
  - ../../../../schemas/contracts/v1/domains/atmosphere/ClimateNormal.schema.json
  - ../../../../policy/domains/atmosphere/README.md
  - ../../../raw/atmosphere/README.md
  - ../../../work/atmosphere/README.md
  - ../../../quarantine/atmosphere/README.md
  - ../../../catalog/domain/atmosphere/README.md
  - ../../../triplets/README.md
  - ../../../proofs/README.md
  - ../../../receipts/README.md
  - ../../../registry/sources/atmosphere/README.md
  - ../../../../release/candidates/atmosphere/README.md
  - ../../../../release/README.md
notes:
  - "Same-path Markdown modernization only; no anomaly bytes, source state, contract, schema, policy, validator, workflow, proof, release, route, hosting, or KFM publication state changed."
  - "ClimateAnomaly is baseline-relative context, not a raw observation, event claim, attribution result, trend-significance proof, model field, or release decision."
  - "The object-named climate_anomaly lane and aggregate/climate lane must not become parallel truth stores; canonical ownership remains unresolved and is not decided here."
  - "Rollback target for v0.2.0 is prior blob SHA `305ce2eae73e5ad7d7684b0d5e616f1df01ee69a`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/processed/atmosphere/climate_anomaly/` — Atmosphere climate-anomaly processed data

> **One-line purpose.** Hold normalized baseline-relative climate-anomaly artifacts while preserving baseline identity, comparison period, variable, units, aggregation method, spatial and temporal support, uncertainty, source role, evidence, correction, and downstream-use limits.

[![Status: grounded draft](https://img.shields.io/badge/status-grounded%20draft-f59e0b?style=flat-square)](#status)
[![Lifecycle: PROCESSED](https://img.shields.io/badge/lifecycle-PROCESSED-8250df?style=flat-square)](#authority-level)
[![Role: baseline-relative context](https://img.shields.io/badge/role-baseline--relative%20context-1f8fff?style=flat-square)](#what-belongs-here)
[![Exposure: not public](https://img.shields.io/badge/exposure-not%20public-b42318?style=flat-square)](#outputs)
[![Baseline: required](https://img.shields.io/badge/baseline-required-6f42c1?style=flat-square)](#baseline-comparability-and-method)
[![Truth: cite or abstain](https://img.shields.io/badge/truth-cite%20or%20abstain-1a7f37?style=flat-square)](#validation)

> [!IMPORTANT]
> **An anomaly is a comparison, not an observation or attribution result.** A numeric departure can be mathematically valid while still being non-comparable, baseline-unclear, method-limited, rights-unclear, weakly supported, policy-held, unreleased, or inappropriate for a causal, trend, hazard, health, or impact claim.

**Path:** `data/processed/atmosphere/climate_anomaly/README.md`  
**Owning root:** `data/`  
**Lifecycle phase:** `processed/`  
**Domain segment:** `atmosphere/`  
**Parent lane:** `data/processed/atmosphere/`  
**Lane role:** `ClimateAnomaly` baseline-relative climate context  
**Direct public access:** denied  
**Last reviewed:** 2026-07-25

**Quick navigation:** [Purpose](#purpose) · [Authority level](#authority-level) · [Status](#status) · [What belongs here](#what-belongs-here) · [What does NOT belong here](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review burden](#review-burden) · [Related folders](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Naming and compatibility](#naming-and-compatibility) · [ClimateAnomaly admission profile](#climateanomaly-admission-profile) · [Baseline, comparability, and method](#baseline-comparability-and-method) · [Anomaly guardrails](#anomaly-guardrails) · [Lifecycle and promotion](#lifecycle-and-promotion) · [Correction and rollback](#correction-and-rollback)

---

## Purpose

This directory is the Atmosphere domain's **PROCESSED-stage lane for `ClimateAnomaly` context**. It may hold normalized anomaly tables, rasters, grids, vectors, summaries, and object-ready derivatives that compare a declared period against a declared `ClimateNormal` or reviewed baseline and have moved beyond RAW capture, WORK calculation, and QUARANTINE holds.

The lane exists to preserve the answer to seven questions before downstream use:

1. Which baseline or `ClimateNormal` is the comparison anchored to?
2. Which reference period and anomaly period are being compared?
3. Which variable, units, aggregation method, and anomaly semantics apply?
4. What spatial support, temporal support, weighting, interpolation, coverage, and missingness apply?
5. Which observations, modeled inputs, or aggregate inputs contributed, and what source role did each retain?
6. Which uncertainty, caveat, correction, evidence, and review state qualify the result?
7. Which downstream claims and uses are allowed, restricted, narrowed, or denied?

It is not a raw observation store, climate-normal authority, forecast/model lane, climate-attribution service, trend-significance proof, hazard-event lane, proof store, receipt authority, catalog authority, release authority, or public map/API/UI source.

## Authority level

**Implementation-bearing lifecycle lane.** The target path is CONFIRMED in the repository and remains under `data/processed/atmosphere/`, consistent with Directory Rules' lifecycle and domain-placement rules.

Its authority is deliberately narrow:

- it may carry processed anomaly artifacts and lane-local explanatory metadata;
- it does not define `ClimateAnomaly` meaning—that remains in the semantic contract;
- it does not define machine shape—the paired schema remains under `schemas/contracts/v1/domains/atmosphere/`;
- it does not define or approve the `ClimateNormal` or reviewed baseline;
- it does not decide scientific fitness, attribution, trend significance, policy, release, or public exposure;
- it does not establish that a schema-valid or mathematically valid anomaly is true, comparable, consequential, or publishable.

## Status

| Surface | Status | Evidence-bounded interpretation |
|---|---|---|
| This README and path | **CONFIRMED** | The file exists at the pinned base and is updated in place. |
| Parent Atmosphere processed lane | **CONFIRMED** | `data/processed/atmosphere/README.md` identifies `climate_anomaly/` as the `ClimateAnomaly` lane and denies direct public use. |
| `ClimateAnomaly` semantic contract | **CONFIRMED repository document / draft** | Defines baseline-relative context, mandatory baseline anchoring, anomaly boundaries, and non-release authority. |
| Paired `ClimateAnomaly` schema | **CONFIRMED scaffold / not enforceable as verified** | File exists, but the contract reports empty properties, `additionalProperties: true`, and unresolved title casing. |
| Aggregate climate sibling lane | **CONFIRMED path / ownership unresolved** | `aggregate/climate/` holds aggregate climate inputs and object-ready derivatives; canonical ownership of anomaly artifacts between the two lanes remains NEEDS VERIFICATION. |
| Real processed anomaly payload inventory | **UNKNOWN** | This documentation task did not inspect or expose climate-anomaly data payloads. |
| Validators, fixtures, and CI enforcement | **NEEDS VERIFICATION** | No accepted production `ClimateAnomaly` validator suite was verified. |
| Receipts, proof, policy decisions, release instances, hosting, public behavior | **UNKNOWN / held** | Presence in this directory creates none of these states. |

## What belongs here

Good fits are processed anomaly artifacts whose baseline and comparison lineage remain inspectable, including:

- normalized `ClimateAnomaly` candidates anchored to a declared `ClimateNormal` or reviewed baseline;
- baseline-relative temperature, precipitation, drought/climate-context, or other supported-variable anomaly products with explicit units and method;
- monthly, seasonal, annual, rolling-window, or other declared comparison-period anomaly products;
- station, station-network, grid-cell, county, region, basin-adjacent, climate-zone, or other declared spatial-support anomaly products;
- source-preserved links to contributing observations, model context, aggregate products, normals, and baselines without copying or relabeling those source objects;
- uncertainty, coverage, missingness, interpolation, weighting, completeness, comparability, and correction sidecars that are not proofs, receipts, policies, or release decisions;
- cross-version or cross-baseline comparison notes that explicitly deny equivalence where methods, periods, variables, units, or supports differ;
- public-candidate anomaly derivatives that remain upstream of catalog and release review;
- object-ready candidates prepared for future contract/schema validation, EvidenceBundle closure, catalog review, or release review;
- lane-local README or non-release manifest notes that explain artifact identity without becoming authority records.

## What does NOT belong here

Do not place these in `data/processed/atmosphere/climate_anomaly/`:

- RAW station observations, source-native climate products, normals, anomaly files, gridded products, downloads, screenshots, model outputs, forecasts, or source captures;
- WORK anomaly calculations, temporary baselines, method experiments, weighting trials, interpolation tuning, scratch joins, notebooks, or QA experiments;
- QUARANTINE material with unresolved source role, rights, baseline identity, reference period, anomaly period, variable, units, method, comparability, dispute, staleness, or quality state;
- `ClimateNormal` baseline artifacts except as controlled references to their owning objects or lanes;
- direct observations such as `TemperatureObservation`, `PrecipitationObservation`, `WeatherObservation`, station records, air-quality observations, AQI reports, smoke/AOD context, advisories, forecasts, or model fields;
- climate attribution, trend-significance, event, hazard, damage, exposure, health, safety, policy, or causal conclusions unsupported by separate evidence and review;
- semantic contracts, JSON Schemas, policy rules, validators, tests, fixtures, executable pipelines, source descriptors, catalogs, STAC/DCAT/PROV projections, triplets, proofs, receipts, releases, correction notices, rollback cards, or published artifacts;
- public map, tile, API, download, export, Focus Mode, Evidence Drawer, graph, search, or AI-answer payloads;
- artifacts duplicated into both this lane and `aggregate/climate/` without a documented canonical owner, alias/compatibility relation, migration note, and rollback plan.

## Inputs

Inputs may enter this lane only through governed lifecycle transitions from:

- `data/work/atmosphere/` after baseline, comparison period, variable, units, method, spatial support, temporal support, source role, rights, uncertainty, evidence, and correction posture are recorded;
- `data/quarantine/atmosphere/` after the hold condition is resolved and the remediation decision is auditable;
- accepted Atmosphere pipelines or tools that preserve source bytes by reference, contributing-object identities, baseline identity, method version, aggregation lineage, input digests, uncertainty, and correction state;
- `data/processed/atmosphere/aggregate/climate/` only through a documented relation that does not silently establish duplicate canonical ownership.

A connector-to-PROCESSED, watcher-to-PROCESSED, or public-upload-to-PROCESSED shortcut is not an accepted normal path. Connectors and watchers create source or candidate state; they do not publish or silently promote.

## Outputs

This lane may support downstream candidates for:

- `data/catalog/domain/atmosphere/` and accepted STAC/DCAT/PROV projections;
- `data/triplets/` or other relationship projections that preserve anomaly identity, baseline identity, source role, method, support, and evidence references;
- separate `data/proofs/` and `data/receipts/` objects;
- `release/candidates/atmosphere/` after baseline, comparability, rights, validation, evidence, policy, review, correction, and rollback obligations are met;
- a separately governed public-safe climate-anomaly product only through a release transition and separate published path;
- governed API, MapLibre, Evidence Drawer, export, or Focus Mode carriers only after public-safe release.

> [!CAUTION]
> Ordinary public clients must not read this directory directly. A processed anomaly is not a released climate claim merely because the calculation is reproducible or the map is visually compelling.

## Validation

No production `ClimateAnomaly` validator suite was verified in this task. The paired schema remains a permissive scaffold, so this README does not claim field-level machine enforcement.

A credible anomaly validation profile should check, at minimum:

1. stable anomaly identity and deterministic digest where practical;
2. resolvable `ClimateNormal` or reviewed-baseline identity;
3. explicit reference period and anomaly/comparison period;
4. variable name, code, units, accumulation/average semantics, and vertical level or height where material;
5. aggregation method, weighting, interpolation, resampling, gap handling, completeness, and missingness;
6. spatial support, temporal support, geometry, CRS, resolution, extent, and scale;
7. source and source-role identity for every contributing input;
8. baseline and anomaly comparability, including method, variable, unit, support, and class consistency;
9. uncertainty, caveats, confidence, correction lineage, and disputed-state handling;
10. evidence references, rights, policy, review, release hold, correction path, and rollback target;
11. no collapse into observation, forecast/model, event, attribution, trend, hazard, damage, or health semantics;
12. no duplicate canonical artifact across `climate_anomaly/` and `aggregate/climate/` without governed compatibility state.

Fail closed or quarantine when a material baseline, period, variable, unit, method, support, source role, rights, uncertainty, evidence, or ownership-convention requirement is absent, contradictory, unsupported, stale beyond policy, or non-comparable.

## Review burden

| Change | Minimum review burden |
|---|---|
| README wording or navigation only | Docs steward plus Atmosphere/climate reviewer. |
| New variable, anomaly method, baseline family, or comparison rule | Climate subject-matter reviewer, contract/schema reviewer, validation reviewer, and data-quality reviewer. |
| Change to canonical ownership between `climate_anomaly/` and `aggregate/climate/` | Directory Rules review, Atmosphere steward, migration note or ADR where authority changes, compatibility test plan, and rollback plan. |
| Public-facing candidate, map, API, Focus Mode, report, or export linkage | Evidence, policy, release, correction, rollback, and domain review. |
| Attribution, trend, hazard, damage, exposure, health, or life-safety implication | Hold by default; require separate owning authority, methods, evidence, and review appropriate to consequence. |

## Related folders

| Responsibility | Path |
|---|---|
| Parent processed lane | `data/processed/atmosphere/` |
| Aggregate climate sibling | `data/processed/atmosphere/aggregate/climate/` |
| Semantic meaning | `contracts/domains/atmosphere/ClimateAnomaly.md` and `ClimateNormal.md` |
| Machine shape | `schemas/contracts/v1/domains/atmosphere/ClimateAnomaly.schema.json` and `ClimateNormal.schema.json` |
| Domain doctrine | `docs/domains/atmosphere/` |
| Admissibility | `policy/domains/atmosphere/` |
| Lifecycle predecessors | `data/raw/atmosphere/`, `data/work/atmosphere/`, `data/quarantine/atmosphere/` |
| Catalog and graph | `data/catalog/domain/atmosphere/`, `data/triplets/` |
| Evidence and receipts | `data/proofs/`, `data/receipts/` |
| Source registry | `data/registry/sources/atmosphere/` |
| Release authority | `release/candidates/atmosphere/`, `release/` |

## ADRs

No accepted ADR was verified that assigns canonical anomaly-artifact ownership between `data/processed/atmosphere/climate_anomaly/` and `data/processed/atmosphere/aggregate/climate/`.

Until that ownership question is resolved:

- do not create divergent canonical copies;
- do not infer that both paths are independently authoritative;
- preserve explicit alias, compatibility, or candidate relationships where both are referenced;
- require a migration note or ADR before moving or renaming authority-bearing artifacts;
- keep rollback targets for either direction.

## Last reviewed

2026-07-25 — repository-grounded Markdown modernization against `main@3843be327db500da76f62e04c9fb0f5c903a3c69`.

## Naming and compatibility

Two processed climate paths are currently relevant:

| Path | Verified role | Current posture |
|---|---|---|
| `data/processed/atmosphere/aggregate/climate/` | Aggregate climate inputs and object-ready `ClimateNormal` / `ClimateAnomaly` derivatives | CONFIRMED path; broader aggregate family |
| `data/processed/atmosphere/climate_anomaly/` | Object-named `ClimateAnomaly` context lane | CONFIRMED path; canonical ownership NEEDS VERIFICATION |

These paths must not evolve into parallel truth stores. A safe compatibility decision should identify one of the following:

1. `aggregate/climate/` is canonical and `climate_anomaly/` is an index, compatibility lane, or deprecated alias;
2. `climate_anomaly/` is canonical for validated anomaly objects and `aggregate/climate/` holds only inputs/object-ready derivatives;
3. both remain distinct under an explicit admission and promotion contract that prohibits duplicate canonical bytes and identities.

This README does not choose among those options.

## ClimateAnomaly admission profile

A proposed normalized anomaly packet should preserve at least:

| Field group | Minimum semantics |
|---|---|
| Identity | `climate_anomaly_id`, schema/contract version, content digest, correction/supersession references |
| Baseline | `climate_normal_ref` or reviewed-baseline ref, baseline period, source, method, version, and digest |
| Comparison | anomaly period, comparison window, variable, code, units, direction, and anomaly-value semantics |
| Method | aggregation, weighting, interpolation, resampling, gap handling, completeness, and method version |
| Spatial support | support type, geometry/ref, CRS, resolution, extent, scale, and coverage |
| Temporal support | source time, valid time, retrieval time, generation time, correction time, and release time where material |
| Inputs | contributing observation/model/aggregate refs, source roles, source descriptors, and input digests |
| Quality | missingness, coverage, uncertainty, confidence, caveats, disputed state, and comparability notes |
| Governance | EvidenceRefs, rights, policy state, review state, release hold, correction path, and rollback target |

These are **PROPOSED semantic expectations**, not claims that the current scaffold schema enforces them.

## Baseline, comparability, and method

- An anomaly must resolve to a declared baseline or `ClimateNormal`; an implicit or missing baseline is a hard failure.
- Reference and anomaly periods must remain distinct and machine-readable.
- Absolute difference, percentage difference, standardized anomaly, percentile, return-period, categorical departure, and other anomaly semantics must not be interchanged.
- Units and accumulation/average semantics must be compatible before comparison.
- Spatial and temporal support must match or carry a reviewed reconciliation method.
- Changes in station network, source composition, class definitions, observation practice, interpolation, resolution, or processing method can break comparability and must remain visible.
- A valid calculation does not establish trend significance, attribution, cause, impact, damages, or hazard status.
- Cross-baseline comparisons require explicit mapping and cannot silently imply equivalence.

## Anomaly guardrails

- `ClimateAnomaly` is baseline-relative climate context, not a direct observation.
- `ClimateNormal` owns baseline meaning; an anomaly does not define its normal implicitly.
- Forecast and modeled context must remain labeled as model or forecast when they contribute.
- A single anomaly does not prove a climate trend.
- A climate trend does not by itself prove attribution, impact, hazard, damage, exposure, or health effect.
- Schema validity does not prove evidence closure, comparability, or publication readiness.
- Public climate context requires baseline disclosure, method disclosure, uncertainty, evidence, policy, release, correction, and rollback.
- Public clients and Focus Mode use governed released carriers, not this directory directly.

## Lifecycle and promotion

```text
RAW source captures
  -> WORK calculation and comparison
  -> QUARANTINE when baseline, rights, role, method, support, or comparability is unresolved
  -> PROCESSED ClimateAnomaly candidate
  -> contract/schema validation when enforceable
  -> catalog + EvidenceBundle closure
  -> policy and scientific-method review
  -> release candidate + rollback/correction readiness
  -> separately published public-safe artifact
  -> governed API / MapLibre / Evidence Drawer / Focus Mode
```

Promotion is a governed state transition, not a file move. A commit, merge, catalog entry, map render, or successful calculation does not establish release.

## Correction and rollback

Corrections must preserve:

- the affected anomaly identity and artifact digest;
- the baseline and comparison periods;
- the baseline identity, source, method, version, and digest;
- the changed variable, units, method, support, input, uncertainty, or interpretation;
- the prior and replacement artifact relationships;
- impacted catalog, evidence, release, map, API, cache, export, and narrative carriers;
- whether withdrawal, recomputation, re-review, re-release, or abstention is required;
- the rollback target and reason.

Rollback is required if this lane becomes a raw-observation store, implicit-baseline store, parallel truth store, attribution or trend-proof source, model/forecast relabeling path, hazard or impact source, proof/receipt/catalog/release authority, published-output substitute, or direct public API/map/UI shortcut.

Rollback target for this modernization: prior blob `305ce2eae73e5ad7d7684b0d5e616f1df01ee69a`.

<p align="right"><a href="#top">Back to top</a></p>

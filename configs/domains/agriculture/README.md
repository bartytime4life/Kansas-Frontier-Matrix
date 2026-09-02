<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-domains-agriculture-readme
title: configs/domains/agriculture/ — Governed Agriculture Configuration Boundary
type: readme
version: v0.3
status: draft
owners: OWNER_TBD — Config steward · Agriculture steward · Crop/field steward · Agricultural statistics steward · Privacy/aggregation steward · Source and rights steward · Consumer owner · Validation steward · Policy steward · Release steward · Docs steward
created: 2026-07-13
updated: 2026-07-14
policy_label: "public; config-sublane; agriculture; source-role-aware; crop-year-aware; revision-aware; aggregation-aware; privacy-aware; rights-aware; non-secret; non-authoritative; no-live-binding; no-field-truth; no-operator-identification; no-agronomic-advice; no-regulatory-or-compliance-authority; no-release-authority"
current_path: configs/domains/agriculture/README.md
truth_posture: CONFIRMED canonical Agriculture config lane, parent configuration contract, repository-present Agriculture doctrine and implementation-shaped surfaces, README-only bounded config inventory, placeholder/scaffold status of inspected package metadata, pipeline entrypoints, pipeline specs, policy lane, aggregation-receipt schema, validator lane, workflow, governed-api route source, source registries, and catalog compatibility redirect, unresolved segmented-versus-short contract/schema paths, unresolved aggregation-receipt naming and placement, and unresolved source-registry topology / PROPOSED future consumer-bound templates and accepted profile references / UNKNOWN direct consumers, loader behavior, precedence, deployment binding, exhaustive recursive inventory, runtime behavior, and publication use / NEEDS VERIFICATION accepted owners, canonical authority paths, source-role vocabulary, source rights, suppression and aggregation rules, field-candidate identity rules, crop/yield/statistical revision semantics, model and remote-sensing profiles, private-operation handling, executable config validation, scanners, CI enforcement, correction propagation, and rollback integration
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 916a13651c4a6596df8d9e7990bb6515b598365b
  prior_blob: 1125052b1892a00df3b4af2755f92e163e9d1d6c
  bounded_path_search: configs/domains/agriculture/README.md only
related:
  - ../README.md
  - ../../README.md
  - ../../../docs/domains/agriculture/README.md
  - ../../../docs/domains/agriculture/ARCHITECTURE.md
  - ../../../docs/domains/agriculture/CANONICAL_PATHS.md
  - ../../../docs/domains/agriculture/DATA_LIFECYCLE.md
  - ../../../docs/domains/agriculture/SOURCES.md
  - ../../../docs/domains/agriculture/SENSITIVITY.md
  - ../../../docs/domains/agriculture/POLICY.md
  - ../../../docs/domains/agriculture/IDENTITY_MODEL.md
  - ../../../docs/domains/agriculture/VERIFICATION_BACKLOG.md
  - ../../../docs/registers/DOMAIN_LANE.md
  - ../../../docs/registers/DRIFT_REGISTER.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/security/SECRETS.md
  - ../../../contracts/domains/agriculture/
  - ../../../contracts/agriculture/
  - ../../../schemas/contracts/v1/domains/agriculture/
  - ../../../schemas/contracts/v1/agriculture/
  - ../../../policy/domains/agriculture/
  - ../../../data/registry/sources/agriculture/
  - ../../../data/registry/agriculture/
  - ../../../data/registry/source_descriptors/agriculture/
  - ../../../data/catalog/domain/agriculture/
  - ../../../catalog/domain/agriculture/
  - ../../../packages/domains/agriculture/
  - ../../../pipelines/domains/agriculture/
  - ../../../pipeline_specs/agriculture/
  - ../../../tools/validators/agriculture/
  - ../../../tests/domains/agriculture/
  - ../../../fixtures/domains/agriculture/
  - ../../../apps/governed-api/src/routes/agriculture/
  - ../../../apps/explorer-web/src/features/domains/agriculture/
  - ../../../data/raw/agriculture/
  - ../../../data/work/agriculture/
  - ../../../data/quarantine/agriculture/
  - ../../../data/processed/agriculture/
  - ../../../data/triplets/agriculture/
  - ../../../data/published/agriculture/
  - ../../../data/receipts/agriculture/
  - ../../../data/proofs/agriculture/
  - ../../../release/candidates/agriculture/
  - ../../../release/agriculture/
  - ../../../docs/runbooks/agriculture/PROMOTION_RUNBOOK.md
  - ../../../docs/runbooks/agriculture/NO_NETWORK_TEST_RUNBOOK.md
  - ../../../.github/workflows/domain-agriculture.yml
tags: [kfm, configs, agriculture, crops, fields, yield, rotation, irrigation, conservation, stress, economy, aggregation, suppression, source-role, crop-year, revision, privacy, rights, no-secrets, governance]
notes:
  - "The bounded repository search for configs/domains/agriculture returned this README only. No executable Agriculture configuration payload or indexed direct consumer was found."
  - "The prior v0.2 README already contained strong privacy, aggregation, source-role, failure, and rollback controls. v0.3 preserves them and adds current repository evidence, implementation maturity, compatibility and registry conflicts, richer Agriculture-specific invariants, and a stricter first-payload gate."
  - "Inspected package metadata, pipeline entrypoints, declarative specs, policy lane, aggregation-receipt schema, validator lane, and domain workflow are version-0.0.0, placeholder, empty-stage, proposed, empty-permissive, documentation-only, TODO-only, or otherwise not proof of production behavior."
  - "Repository evidence contains segmented-versus-short contract/schema paths, three source-registry orderings, an aggregation_receipt versus aggregation-receipt naming conflict, root-versus-receipts schema placement uncertainty, and a root-level catalog compatibility redirect. This lane does not resolve, alias, or duplicate those conflicts."
  - "Configuration may reference accepted source, role, crop-year, revision, aggregation, suppression, model, privacy, review, or release profiles. It cannot create crop, field, yield, operator, parcel, regulatory, compliance, market, suitability, evidence, policy, release, or publication truth."
  - "Only this Markdown file changes."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Agriculture Domain Configuration

`configs/domains/agriculture/`

> Safe-to-commit configuration documentation and future consumer-bound templates for crop observations, cropland classifications, field candidates, rotations, aggregate yields, irrigation context, conservation context, suitability and stress indicators, agricultural-economy summaries, supply-chain context, and public-safe derivatives. This lane is not crop or field truth, farm/operator identity authority, parcel/title authority, agronomic advice, compliance authority, market advice, evidence, policy, or release authority.

![status](https://img.shields.io/badge/status-draft-blue)
![version](https://img.shields.io/badge/version-v0.3-informational)
![authority](https://img.shields.io/badge/authority-config__sublane-green)
![maturity](https://img.shields.io/badge/maturity-README--only-lightgrey)
![privacy](https://img.shields.io/badge/field__operator-exposure__denied-red)
![secrets](https://img.shields.io/badge/secrets-forbidden-red)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-0b7285)

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs-and-drift-triggers) · [Last reviewed](#last-reviewed) · [Scope](#scope-and-bounded-context) · [Classes](#configuration-classes) · [Contract](#minimum-configuration-contract) · [Binding](#consumer-binding-precedence-and-discovery) · [Objects](#agriculture-object-family-boundaries) · [Roles](#source-role-and-knowledge-character) · [Identity](#field-parcel-operator-and-facility-identity) · [Space](#spatial-unit-aggregation-suppression-and-reconstruction) · [Time](#crop-year-survey-year-time-and-revision-state) · [Measurements](#units-methods-denominators-quality-and-uncertainty) · [Models](#classified-imagery-remote-sensing-and-model-products) · [Interpretation](#suitability-stress-and-advice-boundary) · [Operations](#irrigation-conservation-regulatory-and-compliance-context) · [Economy](#agricultural-economy-and-supply-chain-context) · [Joins](#cross-domain-joins) · [Rights](#source-rights-attribution-and-redistribution) · [Logging](#logging-telemetry-and-observability) · [Failure](#failure-behavior) · [AI](#governed-ai-and-generated-language) · [Migration](#migration-and-anti-bypass-posture) · [Rollback](#rollback-correction-and-deactivation) · [Done](#definition-of-done-for-the-first-payload)

> [!IMPORTANT]
> **Document lifecycle:** draft `v0.3`  
> **Observed lane maturity:** README-only in the bounded path search; no executable Agriculture configuration payload or direct consumer binding is established  
> **Authority:** implementation-supporting configuration sublane; non-authoritative for agricultural meaning, source admission, crop/field/operator identity, privacy thresholds, evidence, policy, or release  
> **Runtime posture:** no loader, precedence rule, source activation, network fetch, survey query, imagery job, field inference, statistical disclosure check, public layer, release, or publication is established by this README

> [!CAUTION]
> A configuration value cannot turn a classified pixel into an observed crop, a field candidate into a confirmed field or parcel, a survey aggregate into an operator fact, a modeled yield into a measured yield, a suitability score into a recommendation, a conservation indicator into compliance proof, or a public map into permission to expose field/operator detail. Missing source role, rights, aggregation/suppression support, time, revision, evidence, policy, review, or release state fails closed.

---

## Purpose

This directory defines the safe-to-commit configuration boundary for the canonical `agriculture` domain segment under `configs/domains/`.

It may eventually hold small defaults, templates, examples, or review-oriented settings for a **named and verified consumer**. Those files may describe how that consumer should parse, validate, compare, aggregate, suppress, generalize, render, or package already-governed Agriculture material, but they cannot decide:

- whether a crop, field, rotation, yield, irrigation link, conservation practice, suitability rating, stress indicator, agricultural-economy observation, or supply-chain node is true;
- whether a field boundary is actual, current, operator-confirmed, parcel-aligned, or publicly releasable;
- whether a source is admitted, active, licensed, current, redistributable, or authoritative for a requested claim;
- whether an administrative, aggregate, modeled, inferred, candidate, contextual, or restricted record may be relabeled as observed;
- whether a county, crop-reporting-district, HUC, grid, pixel, field, parcel, facility, farm, ranch, operation, or operator is the correct spatial or identity unit;
- whether a crop-year, survey-year, imagery acquisition, observation, valid period, retrieval time, release time, revision, or correction is current;
- whether a numeric value has a valid unit, denominator, method, sample frame, confidence interval, suppression state, revision state, or uncertainty description;
- whether field/operator/facility/private-land detail may be exposed or reconstructed through small cells, temporal differencing, or cross-layer joins;
- whether an interpretation constitutes agronomic, engineering, insurance, lending, market, pesticide, animal-health, conservation-compliance, regulatory, legal, or hazard advice;
- whether evidence supports a claim;
- whether an artifact may be promoted, released, or published.

This README is intended for configuration maintainers, Agriculture stewards, crop/field and statistical stewards, source and rights stewards, privacy/aggregation reviewers, consumer owners, validation owners, policy and release reviewers, security reviewers, and contributors checking Directory Rules placement.

[Back to top](#top)

---

## Authority level

**Configuration-supporting and non-authoritative.**

| Concern | Authority in this lane |
|---|---|
| Agriculture domain meaning | **None.** Human doctrine remains under `docs/domains/agriculture/`; semantic meaning remains in accepted contract homes. |
| Source identity and activation | **None.** Config may reference reviewed source IDs or profiles; it cannot admit, activate, suspend, retire, or supersede a source. |
| Source role | **None.** Config cannot upgrade observed, regulatory, administrative, modeled, aggregate, candidate, context, synthetic, restricted, or other accepted roles. |
| Crop and land-cover class meaning | **None.** Config may select an accepted class crosswalk; it cannot silently remap crop, land-cover, or confidence semantics. |
| Field, parcel, farm, operator, or facility identity | **None.** Config cannot infer identity or equivalence from geometry overlap, name, address, program record, imagery, or repeated appearance. |
| Statistical estimates and revisions | **None.** Config cannot make an estimate final, remove suppression, downscale an aggregate, or promote a revision without authority support. |
| Aggregation, suppression, redaction, or generalization policy | **None.** Config may select an accepted profile; it cannot define a privacy threshold or authorize exact exposure. |
| Suitability, stress, conservation, irrigation, or economic interpretation | **None.** Config may select a method profile; it cannot create accepted fitness-for-use, advice, compliance, market, or operational authority. |
| Evidence and claim truth | **None.** Config cannot create an `EvidenceBundle`, close proof, validate a claim, or turn a candidate into truth. |
| Release and publication | **None.** Config cannot authorize promotion, release, public display, export, Focus Mode use, or publication. |
| Consumer behavior | **Supporting only.** A verified consumer may read a validated file through explicit binding and deterministic precedence. |

A configuration value may point to authority. It cannot acquire that authority through parsing, naming, location, reuse, or a successful pipeline run.

[Back to top](#top)

---

## Status

### Evidence snapshot

| Field | Value |
|---|---|
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Repository ID | `1059091169` |
| Visibility | public |
| Base ref | `main` |
| Base commit | `916a13651c4a6596df8d9e7990bb6515b598365b` |
| Prior target blob | `1125052b1892a00df3b4af2755f92e163e9d1d6c` |
| Bounded config search | `configs/domains/agriculture/README.md` only |

### Confirmed repository surfaces

The following current-repository surfaces were directly inspected for this revision:

- `configs/domains/agriculture/README.md` — existing v0.2 configuration boundary;
- `configs/domains/README.md` — parent v0.4 domain-config contract;
- `docs/domains/agriculture/README.md`, `ARCHITECTURE.md`, and `CANONICAL_PATHS.md`;
- `packages/domains/agriculture/README.md` and `pyproject.toml`;
- `pipelines/domains/agriculture/README.md` plus `ingest.py`, `normalize.py`, `validate.py`, `publish.py`, and `rollback.py`;
- `pipeline_specs/agriculture/ingest.yaml`, `validate.yaml`, and `publish.yaml`;
- `schemas/contracts/v1/domains/agriculture/README.md` and `aggregation_receipt.schema.json`;
- `policy/domains/agriculture/README.md`;
- `tools/validators/agriculture/README.md` and the exact probe for `validate_agriculture_candidate.py`;
- `.github/workflows/domain-agriculture.yml`;
- `data/registry/sources/agriculture/README.md` and `data/registry/agriculture/README.md`;
- `catalog/domain/agriculture/README.md`;
- `apps/governed-api/src/routes/agriculture/README.md`.

### Maturity matrix

| Surface | Confirmed state | Safe conclusion |
|---|---|---|
| Config lane | README-only bounded result | No payload or direct consumer is established. |
| Parent config contract | Draft v0.4 | Non-secret, inactive, non-authoritative child-lane rules apply. |
| Agriculture doctrine | Rich draft documentation | Strong domain boundaries exist; implementation claims remain bounded. |
| Package | Detailed README; `pyproject.toml` version `0.0.0` and labeled greenfield | Helper responsibilities are documented; working modules, exports, tests, and consumers remain unverified. |
| Pipeline | Detailed README; five inspected core entrypoints contain only placeholder comments | No executable ingest/normalize/validate/publish/rollback behavior is established by those files. |
| Pipeline specs | `stages: []` in inspected ingest/validate/publish files | No declarative stage wiring is established. |
| Policy | Detailed draft README; concrete policy modules not confirmed in the bounded search | Policy intent is documented; accepted executable rules and runtime enforcement remain unverified. |
| Schema | Domain index plus one `AggregationReceipt` scaffold with empty `properties` and permissive `additionalProperties` | Path and draft shape exist; meaningful validation is not established. |
| Validator | README-only lane; proposed executable exact path returned `Not Found` | Validator responsibilities are documented; an executable entrypoint is not established. |
| Workflow | PR/push workflow with TODO echo jobs | Trigger scaffolding exists; substantive validation/proof/publish checks are not established. |
| Governed API route source | Detailed README | Route-source boundary exists; handlers, DTOs, middleware, integrations, tests, and runtime behavior remain unverified. |
| Source registries | Subtype-first and domain-first README lanes | Registry path presence and conflict are established; active descriptor payloads and canonical topology remain unverified. |
| Catalog compatibility | Root-level redirect points to `data/catalog/domain/agriculture/` | Compatibility boundary exists; migration and producer compliance remain unverified. |
| Runtime/release/publication | Not established by this lane | Presence of docs, schemas, or config files does not authorize use. |

### Current conflicts and drift

| Conflict | State | Required handling |
|---|---:|---|
| `contracts/domains/agriculture/` vs `contracts/agriculture/` | `CONFLICTED / ADR-SENSITIVE` | Do not duplicate semantic contracts or select a winner in config. |
| `schemas/contracts/v1/domains/agriculture/` vs `schemas/contracts/v1/agriculture/` | `CONFLICTED / COMPATIBILITY` | Treat the short path as compatibility/index unless accepted migration evidence says otherwise. |
| `aggregation_receipt` vs `aggregation-receipt` contract naming | `CONFLICTED` | Preserve both references in drift/migration records; no silent rename. |
| Agriculture schema root vs `receipts/` child for `AggregationReceipt` | `NEEDS VERIFICATION` | Resolve by schema/receipt governance before binding a config. |
| `data/registry/sources/agriculture/` vs `data/registry/agriculture/sources/` vs `data/registry/source_descriptors/agriculture/` | `CONFLICTED` | Do not maintain divergent authoritative descriptor sets. |
| `catalog/domain/agriculture/` vs `data/catalog/domain/agriculture/` | `COMPATIBILITY REDIRECT` | Canonical catalog records stay under `data/catalog/domain/agriculture/`. |
| Source-role vocabulary and sensitivity tiers | `NEEDS VERIFICATION` | Config must reference an accepted vocabulary/profile, not invent one. |

[Back to top](#top)

---

## What belongs here

Only safe, non-secret, Agriculture-scoped configuration support for a named and verified consumer belongs here.

| Material | Permitted purpose | Minimum posture |
|---|---|---|
| `README.md` | Define this boundary. | Preserve privacy, source-role, evidence, policy, release, and rollback controls. |
| `*.template.yaml` / `*.template.yml` | Placeholder-based consumer template. | Parseable, versioned, synthetic, explicit binding, no automatic activation. |
| `*.example.yaml` / `*.example.json` / `*.example.toml` | Tiny illustrative example. | Non-operational mock values; no real operator, field, parcel, facility, or source payload. |
| Review defaults | Select an accepted hold, abstain, restrict, deny, or review route. | Cannot reduce mandatory policy or release review. |
| Aggregation/suppression profile references | Select an already-governed public-safe profile. | Profile identity and version only; do not define thresholds as local policy. |
| Class/crosswalk profile references | Select an accepted crop or land-cover crosswalk. | Preserve native codes, source role, vintage, uncertainty, and mapping receipt. |
| Temporal/freshness profile references | Select accepted crop-year, survey-year, imagery, observation, revision, or stale-state handling. | Cannot manufacture currency or finality. |
| Model/method profile references | Select accepted remote-sensing, suitability, stress, or statistical method profiles. | Preserve model/run/version/input/uncertainty refs; not evidence by itself. |
| Public-safe display hints | Select accepted generalized layers, zoom limits, labels, legends, or caveat profiles. | No exact sensitive geometry or operator-resolvable detail. |
| Migration notes | Document a real key, filename, or consumer transition. | Time-bounded, owner-linked, tested, reversible, and not a second authority. |

Examples must remain synthetic and must not approximate a real field, parcel, farm, ranch, facility, storage site, livestock operation, well, operator, worker, or protected location closely enough to enable reconstruction.

[Back to top](#top)

---

## What does not belong here

- private producer, operator, landowner, tenant, employee, worker, household, customer, or living-person data;
- person–parcel, operator–field, farm–owner, livestock–operator, permit–operator, or facility–operator joins;
- exact field boundaries, parcel geometries, farmstead locations, storage or chemical locations, livestock-facility locations, private wells, irrigation infrastructure, equipment, routes, or other reconstructable operational details;
- source payloads, API responses, imagery, rasters, vectors, statistics extracts, survey microdata, farm records, assessor records, program records, market transactions, or model outputs;
- credentials, tokens, signed URLs, connection strings, private endpoints, workstation paths, deployment secrets, or real local values;
- source descriptors, source activation decisions, cadence, rights, license, terms, authority-role, or stale-state decisions;
- canonical crop/land-cover classifications, object contracts, JSON Schemas, policy rules, registry records, receipts, proofs, catalogs, triplets, release records, or published artifacts;
- settings that relabel modeled, classified, inferred, estimated, survey, aggregate, administrative, candidate, contextual, or synthetic material as direct observation;
- settings that infer field identity from pixels, repeated crop classes, parcel overlap, management similarity, or address proximity;
- settings that downscale county, district, watershed, or survey aggregates to farm, parcel, field, operator, or household claims;
- settings that remove suppression, reconstruct small cells, or combine layers/time slices to reveal protected operations;
- settings that treat assessor or cadastral records as title, operator, crop, yield, tenancy, or management truth;
- settings that convert suitability/stress/conservation/economy indicators into advice, compliance, enforcement, insurance, lending, taxation, market, or legal conclusions;
- hidden bypasses for rights, aggregation, suppression, redaction, generalization, review, quarantine, deny, abstain, correction, withdrawal, rollback, or release gates;
- directory scanning or filename conventions that activate consumers or sources automatically.

[Back to top](#top)

---

## Inputs

A future Agriculture configuration payload requires all of the following:

1. **Named consumer** — exact package, app, pipeline, service, runtime, test harness, or tool.
2. **Declared class** — template, example, development default, test default, review default, public-safe profile selector, or compatibility layer.
3. **Declared format** — file type, format version, canonical parser, and parser version/range.
4. **Explicit binding** — exact path and code/deployment mechanism that selects the file.
5. **Authority references** — verified contract, schema, policy, registry, profile, and domain documentation as applicable.
6. **Safe values** — synthetic placeholders or non-sensitive defaults only.
7. **Source-role preservation** — observed, regulatory, administrative, modeled, aggregate, candidate, context, synthetic, restricted, and accepted variants remain distinguishable.
8. **Spatial-unit declaration** — county, district, HUC, grid, pixel, field-candidate, parcel-adjacent, facility, or other support is explicit.
9. **Temporal declaration** — crop year, survey year, imagery acquisition, observation time, valid period, retrieval time, revision status, release time, correction time, and stale state as applicable.
10. **Statistical/method declaration** — unit, denominator, estimate status, sample frame, method, model/run, confidence/uncertainty, suppression, and revision as applicable.
11. **Privacy and rights review** — field, operator, parcel, facility, small-cell, temporal differencing, cross-layer reconstruction, attribution, redistribution, and source-term risks are reviewed.
12. **Validation path** — deterministic parsing, schema checks, semantic checks, privacy/suppression tests, rights tests, no-network fixtures, and finite outcomes.
13. **Precedence rule** — deterministic relation to defaults, environment, local, test, deployment, command-line, and runtime overlays.
14. **Failure posture** — explicit `ABSTAIN`, `DENY`, `RESTRICT`, `HOLD`, `QUARANTINE`, or `ERROR` behavior.
15. **Rollback path** — prior known-good configuration, deactivation, cache/derivative invalidation, correction, and rollback lineage.

A payload missing any required item remains `PROPOSED` and must not be treated as active.

[Back to top](#top)

---

## Outputs

This lane currently outputs documentation only.

A future validated configuration file may support a named consumer by selecting safe, already-governed behavior. It may not:

- admit, activate, retire, or supersede a source;
- identify a producer, operator, owner, worker, parcel, field, facility, or farm;
- define crop or land-cover class truth;
- remove suppression or lower a privacy/aggregation threshold;
- expose exact field, facility, operator, or private-land detail;
- waive rights, attribution, redistribution, policy, review, evidence, receipt, proof, release, correction, withdrawal, or rollback requirements;
- create evidence, an `AggregationReceipt`, a `RedactionReceipt`, a `PolicyDecision`, a `ReleaseManifest`, or claim truth;
- promote an object through the lifecycle;
- create catalog/triplet records or published artifacts;
- provide agronomic, regulatory, compliance, legal, insurance, lending, market, pesticide, livestock-health, water-right, or emergency advice.

[Back to top](#top)

---

## Validation

No executable config validator or direct Agriculture config consumer was verified for this lane. The matrix below is the **required validation target**, not a claim that every check is implemented.

### Validation matrix

| Check | Required result | Current evidence |
|---|---|---|
| Markdown structure | One H1, valid hierarchy, resolvable internal anchors, balanced fences, final newline. | Performed for this README revision. |
| Parse and format | File parses deterministically under declared parser/version. | `NEEDS VERIFICATION` per future payload. |
| Schema | File conforms to an accepted, non-empty schema or explicit format contract. | Current opened Agriculture schema is an empty permissive scaffold. |
| Known keys | Unknown/misspelled keys reject or enter documented safe behavior. | `UNKNOWN`. |
| Consumer binding | Exact consumer/path/selection mechanism is tested. | `UNKNOWN`; no direct consumer found. |
| Precedence | Merge/replace order is deterministic and tested. | `UNKNOWN`. |
| Missing-file behavior | Absence enters safe inactive/error/hold state. | `PROPOSED`. |
| Source-role preservation | No role upcast or collapse. | Required; executable enforcement unverified. |
| Spatial-unit preservation | Aggregate/grid/pixel/field/parcel/facility units cannot silently change. | Required; executable enforcement unverified. |
| Crop/field identity | Field candidates cannot become confirmed field, parcel, or operator identities. | Required; executable enforcement unverified. |
| Crop-year/revision | Crop/survey year, revision/finality, release, correction, and stale state remain explicit. | Required; executable enforcement unverified. |
| Measurement/statistics | Unit, denominator, method, sample frame, estimate/suppression/revision, and uncertainty remain explicit. | Required; executable enforcement unverified. |
| Model/classification | Model/run/product/version, inputs, resolution, QA, uncertainty, and limitation refs remain attached. | Required; executable enforcement unverified. |
| Aggregation/suppression | Public-bound outputs use accepted profiles; small-cell and differencing tests fail closed. | Required; policy/receipt implementation unverified. |
| Reconstruction resistance | Cross-layer, temporal, spatial, and category combinations do not reveal protected operations. | Required; tooling unverified. |
| Rights/attribution | License, terms, attribution, redistribution, and audience limitations resolve. | `NEEDS VERIFICATION` per source. |
| Cross-domain ownership | Soil, Hydrology, Atmosphere, Hazards, People/Land, Infrastructure, Roads/Rail, Habitat, Flora, and Fauna truth stays with owning lanes. | Required. |
| No secrets/private values | No credential, private endpoint, personal path, operator identity, or restricted detail. | Bounded pattern/manual checks required. |
| No-network validation | Parse and core validation use local synthetic/sanitized fixtures where practical. | Agriculture no-network fixture docs exist; executable config coverage unverified. |
| Logging/telemetry | Sensitive values are redacted; field/operator details never appear in default logs. | Required; runtime unverified. |
| Lifecycle isolation | Config stores no RAW/WORK/QUARANTINE/PROCESSED/CATALOG/TRIPLET/PUBLISHED or trust/release objects. | Manual boundary review required. |
| Rollback | Prior config, deactivation, cache/derivative invalidation, correction, and rollback are tested. | `NEEDS VERIFICATION`. |

### Configuration-review outcomes

These outcomes apply to configuration review, not publication:

| Outcome | Meaning | Required action |
|---|---|---|
| `PASS` | Required config checks pass. | May merge as configuration support; no release authority follows. |
| `RESTRICT` | File is usable only for a bounded audience/purpose/profile. | Enforce audience, precision, and obligations. |
| `HOLD` | Review, rights, source, schema, receipt, or migration support is incomplete. | Do not activate or claim consumption. |
| `ABSTAIN` | Meaning, role, identity, method, or evidence cannot be resolved safely. | Narrow or reject use. |
| `DENY` | Secret, private detail, unsafe exposure, authority bypass, or prohibited advice is present. | Remove/quarantine and follow incident/correction procedures. |
| `ERROR` | Parser, validator, or review machinery failed. | Fail closed and repair the process. |

A successful parse does not prove authorization, privacy safety, evidentiary support, runtime activation, or publication readiness.

[Back to top](#top)

---

## Review burden

### Minimum review posture

| Change class | Minimum reviewers |
|---|---|
| README clarification | Config/docs steward + Agriculture steward. |
| New Agriculture config template/example | Config steward + named consumer owner + Agriculture steward + validation owner. |
| Source ID, role, cadence, freshness, rights, or attribution reference | Add source and rights reviewers. |
| Crop/land-cover crosswalk or model profile | Add crop/classification/model and validation reviewers. |
| Field/parcel/facility/operator-related key | Add privacy, sensitivity, People/Land, security, policy, and release reviewers. |
| Aggregation/suppression/generalization/redaction profile | Add privacy/statistical disclosure, policy, receipt, evidence, and release reviewers. |
| Yield/economy/supply-chain/statistical key | Add statistical/economy steward and privacy reviewer. |
| Irrigation/conservation/regulatory/compliance key | Add Hydrology/People-Land/regulatory-domain reviewers as applicable. |
| Public API/UI/export/Focus Mode selector | Add governed API/UI, evidence, AI, policy, release, correction, and rollback reviewers. |
| Loader/discovery/precedence behavior | ADR-class config architecture review plus consumer/test owners. |
| Path or authority migration | Directory Rules, ADR, migration, compatibility, drift, test, and rollback review. |

No single reviewer or config owner may convert configuration into source, identity, policy, evidence, release, or publication authority.

### Change budget

Prefer one bounded concern per PR:

- one README revision;
- one template plus schema/consumer/test support;
- one profile reference update;
- one key migration with compatibility and rollback;
- one consumer binding with negative-state tests.

Do not combine config cleanup with unrelated source activation, schema redesign, policy changes, data migration, or public release.

[Back to top](#top)

---

## Related folders

| Responsibility | Current or proposed home | Relationship |
|---|---|---|
| Parent domain config | `configs/domains/` | Common non-secret, non-authoritative child-lane contract. |
| Repository config root | `configs/` | Safe defaults/templates/examples; real secrets and live bindings excluded. |
| Agriculture doctrine | `docs/domains/agriculture/` | Scope, object families, source families, sensitivity, lifecycle, and human guidance. |
| Semantic contracts | `contracts/domains/agriculture/` or ADR-selected equivalent | Object meaning; config references but never duplicates. |
| Short contract compatibility | `contracts/agriculture/` | `CONFLICTED / NEEDS VERIFICATION`; do not create duplicate truth. |
| Machine schemas | `schemas/contracts/v1/domains/agriculture/` | Draft schema index and current scaffold. |
| Short schema compatibility | `schemas/contracts/v1/agriculture/` | Compatibility/index lane; canonical behavior needs verification. |
| Policy | `policy/domains/agriculture/` | Agriculture admissibility/exposure intent; executable rules/runtime remain unverified. |
| Source registry, subtype-first | `data/registry/sources/agriculture/` | Source admission/control; path presence confirmed. |
| Source registry, domain-first | `data/registry/agriculture/sources/` | Existing companion; topology conflicted. |
| Source-descriptor compatibility | `data/registry/source_descriptors/agriculture/` | Additional documented pattern; topology conflicted. |
| Package helpers | `packages/domains/agriculture/` | Reusable helpers; version `0.0.0`, implementation depth unverified. |
| Pipeline logic | `pipelines/domains/agriculture/` | Intended transformations; inspected core entrypoints are placeholders. |
| Pipeline specs | `pipeline_specs/agriculture/` | Inspected core specs have empty stage lists. |
| Validators | `tools/validators/agriculture/` | README-only proposed validator lane; exact proposed executable not found. |
| Tests/fixtures | `tests/domains/agriculture/`, `fixtures/domains/agriculture/` | Enforceability and synthetic/no-network examples; coverage/pass rates unverified. |
| Governed API route source | `apps/governed-api/src/routes/agriculture/` | README boundary confirmed; handlers/runtime unverified. |
| Explorer feature | `apps/explorer-web/src/features/domains/agriculture/` | Search-surfaced feature README; implementation unverified. |
| Lifecycle | `data/raw|work|quarantine|processed/agriculture/` | Data states, not config. |
| Catalog | `data/catalog/domain/agriculture/` | Canonical catalog lane. |
| Catalog compatibility | `catalog/domain/agriculture/` | Redirect/drift fence only. |
| Triplets | `data/triplets/agriculture/` or accepted lane | Derived relationship projections; not sovereign truth. |
| Receipts/proofs | `data/receipts/agriculture/`, `data/proofs/agriculture/` | Process memory/evidence support; not config. |
| Release | `release/candidates/agriculture/`, `release/agriculture/`, accepted release roots | Promotion, correction, withdrawal, rollback. |
| Public artifacts | `data/published/agriculture/` or accepted released layer homes | Governed release output only. |

[Back to top](#top)

---

## ADRs and drift triggers

This README enacts no ADR.

A separate accepted decision is required before this lane is used to:

- resolve `contracts/domains/agriculture/` versus `contracts/agriculture/`;
- resolve `schemas/contracts/v1/domains/agriculture/` versus `schemas/contracts/v1/agriculture/`;
- resolve `aggregation_receipt` versus `aggregation-receipt` naming;
- move `AggregationReceipt` between the Agriculture schema root and `receipts/`;
- resolve the three Agriculture source-registry orderings;
- convert `catalog/domain/agriculture/` from compatibility redirect into any trust-bearing use;
- establish universal config discovery, merge, precedence, unknown-key, fallback, or environment-substitution behavior;
- define source-role or sensitivity vocabulary;
- define privacy, aggregation, suppression, redaction, generalization, or public-precision thresholds;
- authorize field/operator/private-facility exposure;
- establish a current-state operational, advisory, compliance, market, or recommendation surface;
- create a new schema, contract, policy, registry, receipt, proof, release, or public authority.

### Drift triggers

Open or update a drift record when:

- a consumer reads an undeclared config path;
- two config files claim the same scope;
- a compatibility path receives canonical records;
- a source descriptor is duplicated across registry shapes;
- schema and contract refs disagree on filename or authority home;
- a field/operator-sensitive key appears without policy and review support;
- a public-bound consumer reads internal data or config directly;
- a config change alters released output without correction and rollback lineage.

[Back to top](#top)

---

## Last reviewed

**2026-07-14**, against `main@916a13651c4a6596df8d9e7990bb6515b598365b`.

Review again before:

- the first non-README payload;
- the first direct consumer binding;
- any loader/discovery/precedence decision;
- any source-related, crosswalk, aggregation, suppression, field, operator, parcel, facility, crop-year, revision, yield, model, suitability, stress, irrigation, conservation, compliance, economy, export, API/UI, Focus Mode, or public-layer setting;
- any schema/contract/registry/catalog path migration;
- any change to policy, release, correction, or rollback behavior;
- six months elapse.

[Back to top](#top)

---

## Scope and bounded context

Agriculture configuration may support already-governed handling for these domain object families:

| Object family | Configuration may support | Configuration must not decide |
|---|---|---|
| `CropObservation` | Accepted class/crosswalk, display, temporal, aggregation, and caveat profile selection. | Crop truth, field identity, source authority, or current condition. |
| `FieldCandidate` | Candidate-review, generalization, suppression, and restricted-audience profile selection. | Field confirmation, parcel equivalence, ownership, operator, or public release. |
| `CropRotation` | Sequence-window and display profile selection. | Farm-management history, operator continuity, or definitive rotation truth. |
| `YieldObservation` | Unit/denominator/statistical/revision/aggregation profile selection. | Measured-versus-estimated truth, field-level yield, operator performance, or financial conclusion. |
| `IrrigationLink` | Cross-domain link and public-safe caveat profile selection. | Water right, allocation, pumping, legal access, actual use, or compliance. |
| `ConservationPractice` | Context/review profile selection. | Adoption, compliance, effectiveness, payment/program participation, or operator behavior. |
| `SoilCropSuitability` | Accepted method/fitness-for-use/caveat profile selection. | Agronomic recommendation, land appraisal, engineering decision, crop guarantee, or Soil truth. |
| `AgriculturalEconomyObservation` | Aggregate statistical and disclosure-control profile selection. | Business performance, individual transaction, valuation, forecast, trading, lending, or tax advice. |
| `SupplyChainNode` | Generalized network/context profile selection. | Operator identity, inventory, capacity, vulnerability, route, security, or real-time status. |
| `DroughtStressIndicator` | Model/method/uncertainty/caveat profile selection. | Hazard warning, crop-loss determination, insurance outcome, or emergency advice. |
| `PestStressIndicator` | Model/taxonomy/caveat/review profile selection. | Confirmed infestation, pesticide recommendation, quarantine status, or regulatory finding. |
| `AggregationReceipt` | Reference to an accepted receipt/profile and required-presence behavior. | Receipt fabrication, privacy approval, release approval, or proof closure. |

Other Agriculture object families may be added only after doctrine, contract, schema, policy, source, validation, review, and release impacts are verified.

---

## Configuration classes

Every future payload should declare one class:

| Class | Intended use | Commit posture | Activation posture |
|---|---|---|---|
| `template` | Demonstrate supported keys and external placeholders. | Safe after review. | Never active by presence. |
| `example` | Explain a realistic but synthetic configuration. | Safe after review. | Never active by presence. |
| `dev-default` | Conservative defaults for a verified development consumer. | Portable and non-secret. | Explicit opt-in only. |
| `test-default` | Deterministic, synthetic, no-network test settings. | No real data or source access. | Test harness only. |
| `review-default` | Hold/abstain/restrict routing for review tools. | Fail closed. | Verified review tooling only. |
| `public-safe-profile-selector` | References an accepted aggregation/redaction/generalization/display profile. | Identifier/version only; no protected detail. | Policy, receipt, evidence, review, release still required. |
| `source-profile-selector` | References an accepted source/cadence/role profile. | No credentials/endpoints that are unsafe to publish. | Cannot activate a source. |
| `model-method-selector` | References an accepted model/method/run family. | Preserve version/input/uncertainty refs. | Cannot create model truth. |
| `compatibility` | Temporary key/path mapping during migration. | Time-bounded and owner-linked. | Remove after closure. |
| `production-binding` | Real environment, credential, private source, or deployment values. | **Forbidden here.** | External deployment/secret system only. |

---

## Minimum configuration contract

Every future non-README file should document, in-file or through an accepted adjacent machine contract:

| Field | Requirement |
|---|---|
| `domain_slug` | `agriculture`. |
| `config_id` / `config_version` | Stable identity and semantic version. |
| `config_class` | One class from the table above. |
| `intended_consumer` | Exact repo path/component or `NEEDS VERIFICATION`. |
| `consumer_version` | Accepted version/range when verified. |
| `format` / `parser` | File type, parser, parser version, and canonicalization behavior. |
| `binding` | Exact selection mechanism; no directory-presence activation. |
| `authority_refs` | Contract, schema, policy, registry, profile, receipt, and ADR refs as applicable. |
| `source_refs` | Reviewed source/profile IDs only; no secret/live credentials. |
| `source_role_behavior` | Accepted roles and no-upcast behavior. |
| `spatial_support` | County/district/HUC/grid/pixel/field-candidate/parcel-adjacent/facility/other. |
| `temporal_scope` | Crop/survey/acquisition/observation/valid/retrieval/revision/release/correction fields as applicable. |
| `measurement_semantics` | Unit, denominator, method, sample frame, model/run, confidence, uncertainty, suppression, revision. |
| `privacy_posture` | Audience, aggregation/suppression/generalization profile, small-cell and reconstruction constraints. |
| `rights_posture` | License/terms/attribution/redistribution/audience refs. |
| `network_behavior` | `none` for parse/validation by default; live access belongs to the consumer/source systems. |
| `side_effects` | `none` for parse/validation; lifecycle/release side effects forbidden. |
| `unknown_key_behavior` | Reject/warn/other safe behavior. |
| `missing_file_behavior` | Safe inactive/error/hold behavior. |
| `precedence` | Deterministic merge/replace order. |
| `observability` | Safe diagnostics with redaction. |
| `validation_ref` | Executable check or explicit `NEEDS VERIFICATION`. |
| `owner` / `reviewers` | Accepted owner/review classes or unresolved placeholders. |
| `reviewed_at` | ISO date. |
| `deprecation` | Replacement/sunset for temporary files. |
| `rollback` | Prior known-good ref, deactivation, invalidation, correction, and restore steps. |

No value may grant authority not already provided by the referenced accepted surfaces.

---

## Consumer binding, precedence, and discovery

### Explicit binding

A consumer must identify the exact config file it reads. Avoid recursive discovery, first-match behavior, filename conventions, or “load every YAML under this directory.”

### No implicit precedence

This README does not establish an order such as:

```text
repository default
  -> domain default
  -> environment profile
  -> local override
  -> command-line
  -> runtime/deployment
```

A verified consumer must define and test:

- included files;
- merge versus replace semantics;
- key-level precedence;
- environment substitution;
- type coercion;
- unknown-key behavior;
- missing-file behavior;
- partial-load behavior;
- stale/deprecated config behavior;
- logging/redaction;
- cache and derivative invalidation;
- rollback selection.

### Safe failure

Loading failure must not silently:

- activate a source;
- reveal field/operator/facility detail;
- remove aggregation or suppression;
- broaden audience;
- treat candidates/models/estimates as observations;
- produce advice or compliance conclusions;
- continue using a stale public profile;
- publish or retain a released derivative after invalidation.

---

## Agriculture object-family boundaries

| Object or concept | Must remain separate from | Reason |
|---|---|---|
| Crop observation | Classified pixel, model inference, survey estimate, crop-progress aggregate | Different role, method, support, and uncertainty. |
| Field candidate | Parcel, cadastral boundary, Common Land Unit, operator field, farm, management unit | Geometry or overlap does not prove identity, control, ownership, or public release. |
| Crop rotation | Repeated classification sequence, farm-management record, conservation practice | Sequence is an inference unless evidence and method support stronger status. |
| Yield observation | Modeled yield, survey estimate, county aggregate, insurance yield, operator record | Units, denominator, method, aggregation, rights, and revision differ. |
| Irrigation link | Water right, well ownership, pumping record, legal allocation, actual use | Hydrology/People-Land/regulatory authority remains separate. |
| Conservation practice | Program participation, compliance, payment, effectiveness, observed management | Administrative/planning records do not prove on-ground practice. |
| Suitability | Crop recommendation, appraisal, engineering design, guaranteed productivity | Interpretation is method- and use-specific. |
| Drought/pest stress | Hazard warning, loss determination, infestation, disease diagnosis, pesticide recommendation | Indicator is not operational/regulatory truth. |
| Agricultural economy aggregate | Farm/business/household transaction or performance | Aggregate statistics cannot be downscaled. |
| Supply-chain node | Operator identity, inventory, capacity, security condition, real-time logistics | Infrastructure and private-operation risks. |
| Aggregation receipt | EvidenceBundle, policy decision, proof, release manifest | Separate trust objects with distinct authority. |

---

## Source role and knowledge character

Configuration must preserve the accepted role assigned at source admission and used for the specific claim.

| Role | Agriculture example | Config boundary |
|---|---|---|
| `observed` | Direct measurement or field-verified record with method and rights support. | Cannot be assigned to classification, survey, model, aggregate, or administrative records. |
| `regulatory` | Official restriction, designation, inspection, quarantine, eligibility, or compliance determination. | Cannot be inferred from context or config; may be sensitive and time-bound. |
| `administrative` | Program record, inventory, directory, permit index, CLU-like record, assessor record. | Administrative presence is not crop, field, operator, ownership, condition, or compliance truth. |
| `modeled` | Crop classification, yield estimate, evapotranspiration, stress model, remote-sensing inference. | Preserve model/run/product/version/input/uncertainty/validation refs. |
| `aggregate` | County/district/HUC/survey/economy statistic. | Never downscale to farm, parcel, field, operator, worker, or household. |
| `candidate` | Imported field boundary, geocode, extracted table, provisional match, unreviewed crosswalk. | Blocks public truth and release until governed transition. |
| `context` | Agronomic publication, extension note, background report, explanatory narrative. | Not sufficient claim proof by itself. |
| `synthetic` | Scenario, demo, simulated crop pattern, generated teaching example. | Reality-boundary label required; never mixed with observations. |
| `restricted` | Private operator/farm records, confidential survey microdata, sensitive facility, compliance or health detail. | Deny, restrict, redact, generalize, delay, or quarantine according to policy. |

A source family may support different roles for different products or uses. Config must reference the reviewed use/profile, not assume one universal role.

---

## Field, parcel, operator, and facility identity

- A field candidate is not automatically a cadastral parcel, CLU, farm, ranch, management unit, operator field, or ownership unit.
- Geometry overlap, centroid proximity, matching acreage, repeated crop class, address, facility proximity, or temporal persistence does not prove identity.
- Parcel/assessor data does not prove operator, tenant, crop, management, compliance, ownership title, or field use.
- A field boundary may be inferred, classified, digitized, administrative, surveyed, operator-supplied, or synthetic; the identity method and uncertainty must remain explicit.
- Splits, merges, rotations, fallow periods, boundary revisions, survey vintages, imagery artifacts, and crop-class changes must not be treated as identity continuity without evidence.
- Farmstead, storage, livestock, chemical, irrigation, well, elevator, processor, or supply-chain facilities require role, source, rights, sensitivity, valid-time, and release review.
- Public identifiers must be deterministic where practical but must not encode private identity or enable reverse lookup.
- Config cannot define a hidden crosswalk that joins field, parcel, operator, owner, facility, permit, inspection, program, or financial records.

---

## Spatial unit, aggregation, suppression, and reconstruction

### Spatial/support units

A payload must declare the support of every threshold or profile:

- state;
- crop-reporting district;
- county;
- watershed/HUC;
- administrative region;
- grid cell;
- raster pixel;
- generalized tile;
- field candidate;
- parcel-adjacent feature;
- facility or point;
- route/network node;
- other accepted support.

A value defined for one support cannot silently apply to another.

### Aggregation rules

- Public-safe products default to accepted aggregate/generalized supports.
- Aggregation must preserve denominator, population/frame, geography, time window, method, suppression, revision, and source role.
- A county or district value cannot be copied to fields or parcels as if observed there.
- Raster resampling or zonal statistics do not create field truth.
- Aggregation profiles must be versioned and referenced, not reimplemented as ad hoc local thresholds.

### Suppression and disclosure control

Configuration must not:

- remove or override source suppression;
- infer suppressed cells from totals or adjacent categories;
- expose small-cell or sparse-category details;
- combine time slices to reveal entries/exits or operator activity;
- combine maps, exports, search, tooltips, APIs, or filters to reconstruct protected detail;
- use randomized/jittered display as proof of privacy without an accepted method and receipt;
- lower minimum counts, area thresholds, precision, or delay without policy review.

### Transform evidence

A public-bound transform may require an accepted `AggregationReceipt`, `RedactionReceipt`, `GeneralizationReceipt`, `TransformReceipt`, or equivalent. Config may require or reference the object; it cannot fabricate or self-approve it.

---

## Crop year, survey year, time, and revision state

Where material, preserve:

| Time/revision field | Meaning |
|---|---|
| `crop_year` | Production/planting/harvest season represented. |
| `survey_year` / `reference_period` | Statistical or administrative reporting period. |
| `acquired_at` | Imagery/sensor acquisition time. |
| `observed_at` | Direct observation time. |
| `valid_from` / `valid_to` | Period for which a status or classification is asserted. |
| `retrieved_at` | KFM/source retrieval time. |
| `published_at` | Upstream publication time. |
| `revision_status` | Preliminary, revised, final, superseded, corrected, withdrawn, or source-specific state. |
| `release_time` | KFM release time. |
| `correction_time` | KFM/source correction time. |
| `freshness_state` | Current, stale, expired, superseded, unavailable, or unresolved under an accepted profile. |

Rules:

- A newer retrieval does not make an old crop/survey year current.
- Preliminary estimates cannot be presented as final.
- Revised values must supersede through explicit lineage rather than silent replacement.
- Imagery acquisition and product publication dates are distinct.
- Crop progress, condition, market, facility, pest, disease, drought, irrigation, and supply-chain context may be operationally time-sensitive; stale state must be visible.
- Historic records remain historic even when loaded recently.
- Config cannot define finality, effective dates, or revision authority independently.

---

## Units, methods, denominators, quality, and uncertainty

A numeric Agriculture value is incomplete without applicable context:

- measure and unit;
- numerator and denominator;
- area/weight/count/volume basis;
- commodity/crop/livestock/product class;
- geography/support;
- crop/survey/reference year;
- method and instrument;
- sample frame or population;
- model/product/run/version;
- resolution and scale;
- confidence interval, standard error, accuracy, QA/QC, or uncertainty;
- suppression/disclosure status;
- preliminary/revised/final status;
- known limitations and fitness for use.

Examples of forbidden collapse:

```text
classified acreage -> observed planted acreage
county yield estimate -> field yield
production total -> operator output
pixel confidence -> field certainty
survey response -> complete population
price index -> transaction price
suitability score -> recommendation
stress index -> confirmed loss
```

Config may select accepted normalization and display profiles. It cannot make an untyped, unsupported, suppressed, or methodless value valid.

---

## Classified imagery, remote sensing, and model products

For CDL/HLS/SMAP/vegetation-index/ET/stress/yield/classification or similar products, preserve:

- source/product family;
- product version;
- scene/granule/tile/run identity;
- acquisition and processing time;
- spatial and temporal resolution;
- class scheme and crosswalk version;
- training/reference/validation basis where available;
- QA/cloud/mask/quality flags;
- method/model/version;
- uncertainty/accuracy/confusion limits;
- source role;
- valid use and prohibited use;
- aggregation/generalization method;
- evidence and release refs.

A model or classification is not a direct field observation. A repeated classification is not proof of rotation, ownership, or management. A vegetation signal is not a diagnosis. A field candidate extracted from pixels is not a confirmed field or public parcel layer.

---

## Suitability, stress, and advice boundary

Configuration may reference accepted method and caveat profiles for:

- soil–crop suitability;
- drought/heat/moisture stress;
- vegetation condition;
- pest/disease stress indicators;
- erosion/conservation context;
- yield potential or productivity indicators;
- restoration or land-cover transition context.

It must not convert those outputs into:

- planting, spraying, fertilizer, irrigation, harvest, grazing, livestock-health, storage, safety, or management instructions;
- pesticide, veterinary, quarantine, or disease diagnosis/recommendation;
- engineering design, drainage, erosion-control, water-system, or infrastructure advice;
- crop-loss, insurance, appraisal, lending, tax, subsidy, eligibility, or compliance determinations;
- legal, regulatory, enforcement, title, boundary, or water-right determinations;
- hazard alerts or emergency instructions;
- financial, market, commodity-trading, procurement, or investment advice.

Display must preserve method, input, scale, time, uncertainty, source role, limitations, and evidence. Where those are missing, abstain or hold.

---

## Irrigation, conservation, regulatory, and compliance context

- Agriculture may reference Hydrology-owned water observations and People/Land-owned rights/parcel context; it does not own water-right, allocation, pumping, ownership, title, or legal-access truth.
- An irrigation link may be modeled, administrative, observed, inferred, or candidate. The role must remain explicit.
- Conservation-practice context may come from planning, technical assistance, program, remote-sensing, self-report, or field-verification sources; these are not interchangeable.
- Program participation does not prove practice implementation, effectiveness, compliance, or payment status.
- Regulatory, inspection, pesticide, animal-health, disease, quarantine, contamination, or enforcement records may be highly sensitive and time-bound.
- Config cannot disable mandatory review, retention, redaction, delay, audience restriction, or correction.
- Public presentation must not expose vulnerabilities, private facilities, operational patterns, restricted materials, or individuals through combined attributes.

---

## Agricultural economy and supply-chain context

Agricultural economy and supply-chain config must preserve:

- aggregation level;
- statistical method;
- source role;
- reference period;
- commodity/product class;
- price/quantity/value basis;
- inflation or index basis;
- revision/finality;
- suppression/confidentiality;
- geographic and business support;
- uncertainty and caveats.

It must not expose or infer:

- individual farm/ranch/business transactions;
- operator revenue, cost, inventory, debt, insurance, tax, loan, contract, customer, employee, or performance;
- facility inventory, capacity, vulnerability, schedules, routing, access, security, or real-time operational status;
- private buyer/seller relationships;
- market manipulation, trading signals, price forecasts, or financial recommendations.

Supply-chain nodes and routes are contextual or derived unless supported by their owning domains and release controls. Roads/Rail/Trade owns transport-route truth; Settlements/Infrastructure owns facility/infrastructure context; People/Land owns ownership/private-person context.

---

## Cross-domain joins

| Join | Agriculture may consume | Must remain owned elsewhere | Fail-closed risk |
|---|---|---|---|
| Agriculture × Soil | Map-unit, component, HSG, property, suitability inputs with refs. | Soil identity, survey lineage, horizons, soil truth. | Treating SoilGrid/SSURGO context as field management truth. |
| Agriculture × Hydrology | Streamflow, groundwater, drought/water context, irrigation-support evidence. | Water observations, rights, flood/regulatory truth. | Inferring pumping, allocation, access, or compliance. |
| Agriculture × Atmosphere | Weather, climate, heat, precipitation, smoke/AOD context. | Atmospheric observations and forecast authority. | Treating forecast/model context as observed crop impact. |
| Agriculture × Hazards | Drought, flood, wildfire, storm, disease-event context. | Hazard events, warnings, declarations, emergency authority. | Converting indicators into warnings/loss determinations. |
| Agriculture × People/DNA/Land | Parcel/ownership/consent context under restricted governance. | Title, ownership, living-person, DNA, consent truth. | Operator/owner/tenant identification or private joins. |
| Agriculture × Settlements/Infrastructure | Facilities, service areas, critical assets, dependencies. | Facility/infrastructure truth and security posture. | Exposing storage, livestock, chemical, utility, or operational detail. |
| Agriculture × Roads/Rail/Trade | Freight/market corridor context. | Route, rail, access, restriction, operational truth. | Revealing logistics or treating routes as current/safe. |
| Agriculture × Habitat/Flora/Fauna | Habitat, vegetation, taxa, rare-species or plant context. | Ecological/taxonomic/occurrence truth. | Rare-location leakage through land/crop joins. |
| Agriculture × Geology | Parent material, groundwater/geologic context where relevant. | Lithology, stratigraphy, mineral/resource truth. | Overclaiming causal or site-specific conditions. |

Every join must preserve source role, domain ownership, time, scale, rights, sensitivity, evidence, policy, receipt, release, correction, and rollback.

---

## Source rights, attribution, and redistribution

Before a configuration references or enables a source/product profile, verify:

- publisher/maintainer;
- source/product identity;
- access method and endpoint status;
- current terms/license;
- public-domain or licensed status;
- attribution requirements;
- redistribution and derivative-product limits;
- rate limits and automation restrictions;
- privacy/confidentiality restrictions;
- crop/survey/reference vintage and revision behavior;
- spatial/temporal scale and coverage;
- permitted claim families and audience;
- source role;
- stale/supersession/correction behavior;
- steward and review state.

Missing or unclear rights must produce `HOLD`, `ABSTAIN`, `DENY`, `RESTRICT`, or `QUARANTINE` as applicable. Config cannot declare rights resolved.

---

## Logging, telemetry, and observability

Logs and diagnostics must never include by default:

- credentials, tokens, signed URLs, private endpoints, or local paths;
- exact field/parcel/facility/well/storage/livestock/chemical locations;
- operator, owner, tenant, worker, household, customer, or business identity;
- unsuppressed small-cell data;
- confidential survey or program records;
- source payloads or restricted attributes;
- model prompts or generated text containing protected context.

Prefer safe fields:

- config ID/version/digest;
- consumer version;
- parser/validator version;
- source/profile IDs when public-safe;
- object family and source role;
- aggregate support class;
- crop/reference year;
- policy decision ID/reason code;
- receipt/evidence/release refs;
- finite outcome;
- redacted error class.

Logging must not become a shadow export or private-data store.

---

## Failure behavior

A consumer must fail closed when a config is:

- malformed or unsigned where integrity is required;
- missing required keys;
- using unknown/deprecated keys;
- bound to an unsupported consumer/parser version;
- referencing unresolved schema/contract/policy/registry/profile paths;
- selecting an unverified source or role;
- missing time, revision, spatial support, unit, denominator, method, uncertainty, or suppression context;
- exposing field/operator/private-facility detail;
- removing aggregation/suppression;
- enabling cross-layer reconstruction;
- using a stale or withdrawn profile;
- selecting an interpretation for advice/compliance/operational use;
- missing evidence, receipt, policy, review, release, correction, or rollback support.

Safe outcomes include `ABSTAIN`, `DENY`, `RESTRICT`, `HOLD`, `QUARANTINE`, or `ERROR`. Silent permissive fallback is prohibited.

---

## Governed AI and generated language

AI may interpret already-retrieved, already-governed Agriculture evidence. It must not:

- treat this config as evidence;
- invent crop, field, yield, operator, compliance, facility, market, or source facts;
- infer private operations from maps or cross-layer context;
- remove source-role, aggregation, suppression, time, revision, uncertainty, rights, or release caveats;
- provide agronomic, pesticide, veterinary, regulatory, legal, insurance, lending, market, or emergency advice from config-selected context;
- turn model/classification/aggregate/candidate outputs into observations;
- expose restricted detail through prose even when the map is generalized;
- answer when `EvidenceRef` cannot resolve to an authorized `EvidenceBundle`.

Preferred order:

```text
scope
  -> retrieve governed evidence
  -> resolve EvidenceRef to EvidenceBundle
  -> apply rights, sensitivity, aggregation, and policy
  -> verify release and audience
  -> answer with citations and bounded confidence
  -> otherwise abstain, deny, restrict, or narrow scope
```

Generated summaries remain downstream carriers, never root truth.

---

## Migration and anti-bypass posture

When misplaced or duplicated Agriculture config material is found:

1. freeze new consumers and authority claims;
2. identify the real consumer and responsibility owner;
3. remove/quarantine secrets and protected details immediately;
4. preserve the current blob, provenance, consumers, and release impact;
5. resolve schema/contract/registry/catalog compatibility status through accepted governance;
6. move meaning to contracts, shape to schemas, policy to policy, source control to registry, data to lifecycle lanes, and release objects to release;
7. update explicit bindings and precedence;
8. add valid/invalid/no-network/privacy/reconstruction tests;
9. verify aggregation/suppression and transform receipts;
10. issue correction/withdrawal/rollback records for affected public outputs;
11. invalidate caches, tiles, exports, search/vector/graph products, screenshots, and AI carriers as applicable;
12. keep compatibility redirects time-bounded;
13. close drift/migration only after consumers and rollback are verified.

### Anti-bypass matrix

| Bypass | Required response |
|---|---|
| Config file activates a source | Reject; activation belongs to registry/governed source control. |
| Config contains private source credentials or endpoint bindings | Remove; rotate/revoke if exposed; externalize binding. |
| Config supplies exact field/operator/facility data | Deny/quarantine; config is not data storage. |
| Config defines aggregation/suppression thresholds as local policy | Move to accepted policy/profile authority; retain reference only. |
| Config points public client to internal stores | Reject; public clients use governed APIs/released artifacts. |
| Config labels model/classification/candidate as observed | Deny; preserve source role and knowledge character. |
| Config bypasses receipt/evidence/release | Deny/hold; config cannot close trust objects. |
| Config writes catalog/release/published objects | Move behavior to governed pipeline/release roots. |
| Config enables advice/compliance/market decisions | Deny; narrow to explanatory, evidence-bound context. |
| Compatibility path gains canonical records | Stop writes, migrate reversibly, preserve redirect/drift documentation. |

---

## Rollback, correction, and deactivation

### Rollback triggers

- wrong source/profile/role;
- unsafe field/operator/private-facility exposure;
- aggregation or suppression regression;
- cross-layer reconstruction risk;
- stale/revision/finality error;
- wrong class crosswalk or model profile;
- unit/denominator/method error;
- rights or attribution failure;
- authority-path conflict;
- advice/compliance/market boundary breach;
- evidence/policy/release/correction/rollback link failure;
- consumer/precedence behavior differs from documented behavior.

### Required rollback sequence

1. disable the exact consumer binding;
2. enter safe inactive/deny/hold state;
3. restore the prior reviewed config;
4. stop or quarantine affected jobs and candidates;
5. invalidate derived caches, tiles, exports, search/vector/graph indexes, screenshots, and AI context;
6. identify affected source/crop/reference years, geographies, profiles, releases, and audiences;
7. preserve receipts, logs, evidence, and provenance without exposing protected detail;
8. issue correction, supersession, withdrawal, or rollback records through owning release governance;
9. re-run parse, schema, semantic, role, time, revision, measurement, privacy, suppression, rights, policy, evidence, release, and no-network tests;
10. document the incident/drift and prevention changes.

For this README, mechanical restoration uses the prior blob recorded in metadata. Do not force-push or rewrite shared history.

---

## Definition of done for the first payload

Before the first non-README file is accepted:

- [ ] exact consumer and accepted owner verified;
- [ ] config class, format, parser, binding, discovery, precedence, unknown-key, missing-file, and fallback behavior defined;
- [ ] accepted non-empty schema or format contract validates;
- [ ] contract/policy/registry/profile/ADR references verified;
- [ ] segmented/short contract-schema conflicts do not create duplicate authority;
- [ ] source-registry topology is resolved or one authoritative record family is clearly selected with redirects;
- [ ] source identity, role, rights, terms, attribution, cadence, vintage, revision, and stale handling verified;
- [ ] crop/land-cover crosswalk version and native-code preservation tested;
- [ ] field-candidate versus parcel/operator/farm identity tests pass;
- [ ] spatial-unit and no-downscaling tests pass;
- [ ] crop-year/survey-year/acquisition/observation/valid/retrieval/revision/release/correction tests pass;
- [ ] unit/denominator/method/sample/model/QA/uncertainty/suppression tests pass;
- [ ] aggregation/suppression/small-cell/temporal-differencing/cross-layer reconstruction tests pass;
- [ ] private field/operator/facility/parcel/worker/business denial tests pass;
- [ ] model/classification/candidate no-upcast tests pass;
- [ ] suitability/stress/conservation/irrigation/economy no-advice and no-compliance tests pass;
- [ ] cross-domain ownership tests pass;
- [ ] accepted transform receipt, evidence, policy, review, release, correction, and rollback requirements are enforced;
- [ ] no secrets/private endpoints/private values;
- [ ] no-network parsing and validation where practical;
- [ ] logging/telemetry redaction verified;
- [ ] no lifecycle/trust/catalog/triplet/release objects stored here;
- [ ] deactivation, cache/derivative invalidation, correction, withdrawal, and rollback tested;
- [ ] docs, evidence ledger, migration, and drift records updated.

---

## Verification backlog

| Item | Status |
|---|---:|
| Recursive config inventory | `NEEDS VERIFICATION` |
| Direct consumer/loader | `UNKNOWN` |
| Discovery/precedence/fallback | `UNKNOWN` |
| Segmented vs short contract path | `CONFLICTED / ADR-SENSITIVE` |
| Segmented vs short schema path | `CONFLICTED / COMPATIBILITY` |
| `aggregation_receipt` vs `aggregation-receipt` naming | `CONFLICTED` |
| Aggregation receipt root vs `receipts/` child placement | `NEEDS VERIFICATION` |
| Source-registry topology | `CONFLICTED` |
| Catalog compatibility migration | `NEEDS VERIFICATION` |
| Source-role vocabulary | `NEEDS VERIFICATION` |
| Package implementation | `VERSION 0.0.0 / NEEDS VERIFICATION` |
| Pipeline implementation | `PLACEHOLDER ENTRYPOINTS` |
| Pipeline specs | `EMPTY STAGE LISTS` |
| Policy executable modules/runtime | `NEEDS VERIFICATION` |
| Schema completeness | `PROPOSED EMPTY-PROPERTIES SCAFFOLD` |
| Validator executable | `NOT FOUND AT PROPOSED EXACT PATH` |
| Workflow enforcement | `TODO SCAFFOLD` |
| Tests/pass rates | `NEEDS VERIFICATION` |
| Governed API handlers/runtime | `NEEDS VERIFICATION` |
| Source descriptor payloads/activation | `NEEDS VERIFICATION` |
| Source rights/endpoints/cadence | `NEEDS VERIFICATION` |
| Crop/land-cover crosswalk authority | `NEEDS VERIFICATION` |
| Field identity/merge/split rules | `NEEDS VERIFICATION` |
| Crop-year/revision/finality profiles | `NEEDS VERIFICATION` |
| Units/denominators/method/statistical profiles | `NEEDS VERIFICATION` |
| Aggregation/suppression/reconstruction profiles | `NEEDS VERIFICATION` |
| Model/remote-sensing/uncertainty profiles | `NEEDS VERIFICATION` |
| Private operation/facility handling | `NEEDS VERIFICATION` |
| Advice/compliance/economy boundaries in runtime | `NEEDS VERIFICATION` |
| Secret/sensitive scanners | `NEEDS VERIFICATION` |
| Ownership/CODEOWNERS/branch protection | `NEEDS VERIFICATION` |
| Runtime/release/publication | `UNKNOWN` |

[Back to top](#top)

---

## Safe language rules

| Avoid | Prefer |
|---|---|
| “The pipeline uses this config.” | “This file names an intended consumer; direct binding is `NEEDS VERIFICATION`.” |
| “Observed crop.” | “Source-role-labeled crop observation/classification under a stated method, year, scale, and uncertainty.” |
| “This is the field boundary.” | “A field candidate under a stated source/method/time/uncertainty; parcel/operator equivalence is not implied.” |
| “This farm grows…” | “An aggregate or candidate crop context is shown; operator/farm identity is not asserted.” |
| “County yield applies here.” | “County-level estimate under a stated reference period; no field/operator downscaling.” |
| “Final NASS value.” | “Value with explicit preliminary/revised/final status from the cited source.” |
| “This pixel proves crop rotation.” | “A classified sequence that may support a rotation hypothesis under a stated method.” |
| “This land is suitable.” | “A method-specific interpretation with inputs, scale, uncertainty, limitations, and evidence.” |
| “Drought/pest damage.” | “A stress indicator; hazard, infestation, diagnosis, and loss authority remain separate.” |
| “Irrigated field.” | “An irrigation-related candidate/context under cited source role; rights/use/compliance not implied.” |
| “Conservation practice implemented.” | “Administrative, modeled, contextual, or observed practice evidence as specifically supported.” |
| “Service/facility is operational.” | “Time-bound cited context; no operational assurance.” |
| “Public-safe because aggregated.” | “An accepted profile plus disclosure tests, transform receipt, policy, review, and release support a bounded derivative.” |
| “Schema is active.” | “Opened schema is a `PROPOSED` scaffold with empty properties.” |
| “Policy enforces this.” | “Policy intent is documented; executable modules/runtime binding remain `NEEDS VERIFICATION`.” |
| “Validators enforce this.” | “Validator README exists; proposed executable exact path was not found.” |
| “CI validates Agriculture.” | “The inspected domain workflow currently runs TODO echo jobs.” |
| “catalog/domain/agriculture is the catalog.” | “It is a compatibility redirect; canonical catalog records belong under `data/catalog/domain/agriculture/`.” |

[Back to top](#top)

---

## Evidence ledger

| Evidence | State | Supports | Does not prove |
|---|---|---|---|
| Target README | prior blob `1125052b…`, v0.2 | Existing privacy/aggregation/source-role/failure/rollback contract. | Consumers or payloads. |
| Parent config README | blob `2c5e8b70…`, v0.4 | Non-secret/non-authoritative child contract. | Agriculture runtime behavior. |
| Bounded config search | README only | No indexed payload/direct consumer. | Exhaustive absence. |
| Agriculture domain README | blob `a2cac517…` | Object families, source/privacy/publication doctrine. | Current implementation. |
| Agriculture architecture | blob `3e241679…` | Bounded context, source roles, lifecycle, trust membrane, sensitivity. | Executable behavior. |
| Canonical paths | blob `94e9fb5d…` | Responsibility-root mapping and short/segmented path variance. | Accepted migration resolution. |
| Package README / pyproject | blobs `dd2fc20d…`, `9ff43f0d…` | Intended helper boundary; version `0.0.0`. | Working modules/exports/tests. |
| Pipeline README | blob `ec53bc7e…` | Intended executable boundary and privacy gates. | Implemented transformations. |
| Pipeline entrypoints | placeholder comments | Inspected core entrypoints are greenfield placeholders. | All possible code elsewhere. |
| Pipeline specs | `stages: []` | Spec paths exist. | Stage wiring/execution. |
| Policy README | blob `ba73c387…` | Policy lane/default-deny intent. | Concrete accepted policy modules/runtime enforcement. |
| Schema index | blob `35d28a2c…` | Schema/alias/child-lane/naming conflict. | Production-ready validation. |
| Aggregation receipt schema | blob `16c55157…` | Proposed path/id/contract ref. | Meaningful fields or strict validation. |
| Validator README | blob `ba9009bd…` | Intended validation responsibilities and outcomes. | Executable validator. |
| Proposed validator path | exact fetch `Not Found` | Proposed command is not current path proof. | Absence of all validator code. |
| Domain workflow | blob `a9f5f212…` | PR/push trigger and TODO jobs. | Substantive validation/proof/release. |
| Source registry subtype-first | blob `7828ec0b…` | Source families/roles/risks and path posture. | Active descriptor payloads. |
| Registry domain-first parent | blob `020b7257…` | Three-way registry ordering conflict. | Canonical topology or active records. |
| Catalog compatibility README | blob `5295809c…` | Root path is redirect; canonical catalog under `data/catalog/domain/agriculture/`. | Migration completeness. |
| Governed API route-source README | blob `cec20a47…` | Intended trust-membrane and field/operator denial boundary. | Handlers, integrations, tests, deployment, runtime. |

[Back to top](#top)

---

<details>
<summary><strong>Appendix A — no-loss preservation note</strong></summary>

v0.2 established:

- the Agriculture config lane and documentation-only maturity;
- non-authoritative and no-live-binding posture;
- privacy, field/operator, parcel, facility, and sensitive-location controls;
- source-role separation;
- aggregation, generalization, rights, evidence, policy, review, release, and rollback boundaries;
- minimum configuration contract;
- deterministic validation and finite failure behavior;
- review burden, maintenance, ADR, correction, and rollback requirements.

v0.3 preserves those controls and adds:

- pinned current repository evidence;
- implementation/scaffold maturity;
- schema/contract/registry/catalog compatibility conflicts;
- aggregation-receipt naming and placement conflict;
- full Agriculture object-family boundaries;
- field/parcel/operator/facility identity rules;
- spatial support, aggregation, suppression, and reconstruction resistance;
- crop-year, survey-year, time, revision, and stale-state rules;
- units, denominators, methods, QA, statistical uncertainty, and suppression context;
- classified imagery and model-product controls;
- suitability/stress/no-advice boundaries;
- irrigation, conservation, compliance, economy, and supply-chain safeguards;
- cross-domain ownership matrix;
- rights/attribution/redistribution rules;
- logging, AI, migration, anti-bypass, invalidation, and first-payload gates;
- expanded backlog, safe language, and evidence ledger.

No v0.2 safeguard is intentionally weakened.

</details>

<details>
<summary><strong>Appendix B — documentation-only boundary</strong></summary>

This revision changes no:

- executable config payload;
- consumer, loader, discovery, or precedence behavior;
- source descriptor, source activation, connector, or watcher;
- schema, contract, policy, package, pipeline, validator, test, fixture, or workflow code;
- source data, imagery, statistics, field candidate, parcel, facility, model, or interpretation;
- lifecycle, registry, receipt, proof, catalog, triplet, graph, or published artifact;
- release, correction, withdrawal, supersession, or rollback object;
- API, map, UI, export, Focus Mode, AI, advice, compliance, market, or deployment behavior.

Any future behavior change must be implemented and validated in its owning responsibility roots.

</details>

## Status summary

`configs/domains/agriculture/` is a README-only, non-secret, non-authoritative configuration-support lane. The surrounding repository contains rich Agriculture documentation and many implementation-shaped paths, but inspected package, pipeline, specification, policy, schema, validator, workflow, registry, catalog, and route-source surfaces remain draft, scaffolded, placeholder, compatibility-only, conflicted, or unverified. No direct config consumer is established. Future payloads require explicit binding, accepted source/role/classification profiles, field/operator identity limits, crop-year/revision and measurement semantics, disclosure-resistant aggregation, privacy and rights review, cross-domain authority preservation, validation, evidence, policy, review, release, correction, invalidation, and rollback.

<p align="right"><a href="#top">Back to top</a></p>

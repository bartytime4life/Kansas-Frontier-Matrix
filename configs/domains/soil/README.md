<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-domains-soil-readme
title: configs/domains/soil/ — Governed Soil Configuration Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Config steward · Soil steward · Survey/lineage steward · Soil-moisture steward · Source steward · Land/privacy reviewer · Consumer owner · Validation steward · Policy steward · Release steward · Docs steward
created: 2026-07-13
updated: 2026-07-14
policy_label: "public; config-sublane; soil; support-type-aware; source-role-aware; source-vintage-aware; depth-unit-method-aware; private-land-aware; non-secret; non-authoritative; no-live-binding; no-agronomic-advice; no-engineering-advice; no-conservation-compliance-authority; no-hazard-authority; no-release-authority"
current_path: configs/domains/soil/README.md
truth_posture: CONFIRMED canonical Soil config lane, parent configuration contract, repository-present Soil architecture/canonical-path/contract/schema/policy/pipeline/registry/validator/catalog surfaces, README-only bounded config inventory, placeholder/scaffold status of inspected package metadata, pipeline entrypoints, pipeline specs, policy module, schemas, validators, and workflow, explicit compatibility catalog redirect, unresolved segmented-versus-flat contract/schema paths and source-registry topology, and prior README lineage / PROPOSED future consumer-bound templates and accepted profile references / UNKNOWN direct consumers, loader behavior, precedence, deployment binding, exhaustive recursive inventory, runtime behavior, and publication use / NEEDS VERIFICATION accepted owners, canonical authority paths, source-role vocabulary, source rights, support-type vocabulary authority, MUKEY/COKEY/CHKEY lineage rules, units/depth/method/QC constraints, freshness budgets, interpretation fitness-for-use rules, private-land handling, executable config validation, scanners, CI enforcement, correction propagation, and rollback integration
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 484b2f682d99f53586376ea95a46f962a96ee4bd
  prior_blob: 5b9b0c36546d48b338a1aed1818c5c64816ff094
  bounded_path_search: configs/domains/soil/README.md only
related:
  - ../README.md
  - ../../README.md
  - ../../../docs/domains/soil/README.md
  - ../../../docs/domains/soil/ARCHITECTURE.md
  - ../../../docs/domains/soil/CANONICAL_PATHS.md
  - ../../../docs/domains/soil/DATA_LIFECYCLE.md
  - ../../../docs/domains/soil/API_CONTRACTS.md
  - ../../../docs/registers/DOMAIN_LANE.md
  - ../../../docs/registers/DRIFT_REGISTER.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/security/SECRETS.md
  - ../../../contracts/domains/soil/
  - ../../../contracts/soil/
  - ../../../schemas/contracts/v1/domains/soil/
  - ../../../schemas/contracts/v1/soil/
  - ../../../policy/domains/soil/
  - ../../../data/registry/sources/soil/
  - ../../../data/registry/soil/
  - ../../../data/registry/domains/soil/
  - ../../../data/catalog/domain/soil/
  - ../../../catalog/domain/soil/
  - ../../../packages/domains/soil/
  - ../../../pipelines/domains/soil/
  - ../../../pipeline_specs/soil/
  - ../../../tools/validators/domains/soil/
  - ../../../tests/domains/soil/
  - ../../../fixtures/domains/soil/
  - ../../../data/raw/soil/
  - ../../../data/work/soil/
  - ../../../data/quarantine/soil/
  - ../../../data/processed/soil/
  - ../../../data/triplets/soil/
  - ../../../data/published/layers/soil/
  - ../../../data/receipts/soil/
  - ../../../data/proofs/soil/
  - ../../../release/candidates/soil/
  - ../../../release/manifests/soil/
  - ../../../docs/runbooks/soil/PROMOTION_RUNBOOK.md
  - ../../../docs/runbooks/soil/ROLLBACK_RUNBOOK.md
  - ../../../.github/workflows/domain-soil.yml
tags: [kfm, configs, soil, ssurgo, sda, gssurgo, gnatsgo, soilgrids, mesonet, scan, uscrn, smap, map-unit, component, horizon, pedon, moisture, support-type, source-role, lineage, units, depth, time, sensitivity, no-secrets, governance]
notes:
  - "The bounded repository search for configs/domains/soil returned this README only. No executable Soil configuration payload or indexed direct consumer was found."
  - "The human-facing docs/domains/soil/README.md is a greenfield placeholder; richer Soil doctrine and architecture are carried by ARCHITECTURE.md, CANONICAL_PATHS.md, DATA_LIFECYCLE.md, contract/schema indexes, source-registry docs, and catalog compatibility controls."
  - "Inspected package metadata, pipeline entrypoints, declarative specs, policy, schemas, validators, and workflow are experimental, proposed, empty-stage, empty-permissive, documentation-only, TODO-only, or otherwise not proof of production behavior."
  - "Repository evidence contains segmented-versus-flat contract/schema paths, domain-first versus subtype-first source-registry paths, and a root-level catalog compatibility redirect. This lane does not resolve, alias, or duplicate those conflicts."
  - "Configuration may reference accepted source, support-type, lineage, units, depth, QC, temporal, interpretation, sensitivity, public-safe, review, or release profiles. It cannot create Soil truth, source authority, field verification, suitability authority, agronomic/engineering/legal advice, policy, evidence, release, or publication state."
  - "Only this Markdown file changes."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Soil Domain Configuration

`configs/domains/soil/`

> Safe-to-commit configuration documentation and future consumer-bound templates for Soil survey, map-unit, component, horizon, pedon/profile, gridded derivative, station and satellite soil-moisture, hydrologic-group, erosion-context, suitability, catalog, and public-safe derivative workflows. This lane is not Soil truth, source admission, field verification, conservation-compliance authority, agronomic or engineering advice, hazard authority, policy, evidence, or release authority.

![status](https://img.shields.io/badge/status-draft-blue)
![version](https://img.shields.io/badge/version-v0.2-informational)
![authority](https://img.shields.io/badge/authority-config__sublane-green)
![maturity](https://img.shields.io/badge/maturity-README--only-lightgrey)
![support](https://img.shields.io/badge/support__types-must__stay__separate-red)
![secrets](https://img.shields.io/badge/secrets-forbidden-red)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-0b7285)

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs-and-drift-triggers) · [Last reviewed](#last-reviewed) · [Scope](#scope-and-bounded-context) · [Classes](#configuration-classes) · [Contract](#minimum-configuration-contract) · [Binding](#consumer-binding-precedence-and-discovery) · [Objects](#soil-object-family-boundaries) · [Support](#source-role-and-support-type-separation) · [Lineage](#survey-identity-and-lineage) · [Measurements](#units-depth-method-and-quality-control) · [Time](#time-freshness-and-stale-state) · [Scale](#scale-resolution-and-spatial-support) · [Interpretation](#interpretation-suitability-and-advice-boundary) · [Joins](#cross-domain-joins-and-sensitive-context) · [Logging](#logging-telemetry-and-observability) · [Failure](#failure-behavior) · [AI](#governed-ai-and-generated-language) · [Migration](#migration-and-anti-bypass-posture) · [Rollback](#rollback-correction-and-deactivation) · [Done](#definition-of-done-for-the-first-payload)

> [!IMPORTANT]
> **Document lifecycle:** draft `v0.2`  
> **Observed lane maturity:** README-only in the bounded path search; no executable Soil configuration payload or direct consumer binding is established  
> **Authority:** implementation-supporting configuration sublane; non-authoritative for Soil meaning, source admission, support-type vocabulary, field condition, policy, evidence, advice, or release  
> **Runtime posture:** no loader, precedence rule, source activation, network fetch, survey query, sensor subscription, raster build, interpretation run, public layer, release, or publication is established by this README

> [!CAUTION]
> A Soil configuration value cannot turn a survey into current field truth, a raster into survey authority, a station reading into a countywide surface, a satellite grid into an in-situ observation, a pedon into map-unit truth, a suitability rating into a recommendation, or a hydrologic soil group into flood truth. Missing support type, source role, lineage, units, depth, method, time, rights, evidence, policy, or release state fails closed.

---

## Purpose

This directory defines the safe-to-commit configuration boundary for the canonical `soil` domain segment under `configs/domains/`.

It may eventually hold small defaults, templates, examples, or review-oriented settings for a **named and verified consumer**. Those files may describe how that consumer should parse, validate, compare, aggregate, generalize, render, or package already-governed Soil material, but they cannot decide:

- whether a `SoilMapUnit`, `SoilComponent`, `Horizon`, property, pedon, profile, moisture observation, hydrologic group, erosion rating, or suitability rating is true;
- whether a source is admitted, active, licensed, current, redistributable, or authoritative for a claim;
- whether SSURGO/SDA, gSSURGO/gNATSGO/SoilGrids, Mesonet/SCAN/USCRN, SMAP, pedon records, and interpretation products may be merged;
- whether MUKEY, COKEY, CHKEY, station IDs, grid cells, survey areas, horizons, components, or source versions refer to the same entity;
- whether a numeric value has a valid unit, depth interval, method, support, quality state, or temporal basis;
- whether a survey polygon represents current field conditions;
- whether a gridded or modeled product may be presented as static survey authority;
- whether a station or satellite moisture value is fresh, representative, quality-controlled, or suitable for public display;
- whether an erosion or suitability interpretation constitutes agronomic, conservation, engineering, insurance, lending, regulatory, legal, or hazard advice;
- whether parcel, owner, producer, field, private-sensor, or restricted-source context may be exposed;
- whether evidence supports a claim;
- whether an artifact may be promoted, released, or published.

This README is intended for configuration maintainers, Soil stewards, survey/lineage stewards, moisture and sensor stewards, source and evidence stewards, consumer owners, privacy and land-context reviewers, validation owners, policy and release reviewers, and contributors checking Directory Rules placement.

[Back to top](#top)

---

## Authority level

**Configuration-supporting and non-authoritative.**

| Concern | Authority in this lane |
|---|---|
| Soil domain meaning | **None.** Human doctrine and architecture remain under `docs/domains/soil/`; semantic meaning remains in accepted contract homes. |
| Source identity and activation | **None.** Config may reference a reviewed source ID or profile; it cannot admit, activate, suspend, or supersede a source. |
| Source role | **None.** Config cannot upgrade observed, regulatory, administrative, modeled, aggregate, candidate, context, synthetic, restricted, or legacy role vocabulary. |
| Support type | **None.** Config may select an accepted profile; it cannot invent or silently translate support-type classes. |
| SoilMapUnit / Component / Horizon identity | **None.** Config cannot merge or rewrite MUKEY/COKEY/CHKEY identity or lineage by convenience. |
| Soil-moisture identity | **None.** Config cannot collapse station, depth, variable, product, grid, granule, time, or QC identity. |
| Units, depth, method, QC | **None.** Config may reference an accepted normalization profile; it cannot make an untyped or unsupported value valid. |
| Spatial support and resolution | **None.** Config cannot make a point representative of a polygon, a grid representative of a survey unit, or a generalized surface representative of a field. |
| Interpretation and fitness for use | **None.** Config cannot create an accepted suitability, erosion, hydrologic, engineering, or management interpretation. |
| Private land, producer, or sensor exposure | **None.** Config cannot authorize release, remove restrictions, or prove consent/rights. |
| Cross-domain truth | **None.** Soil config cannot create crop/yield, flood, groundwater, geology, habitat, flora, fauna, hazard, ownership, or legal-boundary truth. |
| Evidence | **None.** Config cannot create an `EvidenceBundle`, validate a claim, or make generated language sovereign. |
| Policy and sensitivity | **None.** Config may reference accepted policies or profiles; it cannot weaken, waive, or replace them. |
| Release and publication | **None.** Config cannot authorize lifecycle promotion, public display, publication, correction approval, or rollback approval. |
| Consumer behavior | **Supporting only.** A verified consumer may read a validated file under explicit binding, precedence, and safe-failure rules. |

Successful parsing, a familiar source name, a public dataset, a high confidence score, or a map-ready raster does not transfer authority into this lane.

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
| Base commit | `484b2f682d99f53586376ea95a46f962a96ee4bd` |
| Prior README blob | `5b9b0c36546d48b338a1aed1818c5c64816ff094` |
| Bounded config-path result | `configs/domains/soil/README.md` only |

### Repository evidence boundary

| Surface | Observed state | Safe conclusion |
|---|---:|---|
| `configs/domains/soil/README.md` | **CONFIRMED v0.1** | Existing documentation boundary and rollback target. |
| Parent config README | **CONFIRMED v0.4** | Child lanes are non-secret, non-authoritative, and not auto-loaded by folder presence. |
| `docs/domains/soil/README.md` | **GREENFIELD PLACEHOLDER** | Path exists; it does not establish current doctrine depth or implementation maturity. |
| Soil architecture and canonical-path docs | **CONFIRMED DRAFTS** | Carry the strongest inspected Soil-specific scope, support-type, lifecycle, path, sensitivity, and cross-lane rules. |
| Config payloads/direct consumer | **NOT FOUND IN BOUNDED SEARCH** | No indexed executable payload or direct consumer was found; differently named or unindexed content remains `UNKNOWN`. |
| Package README | **CONFIRMED DRAFT** | Defines intended shared-helper boundary. |
| Package metadata | **GREENFIELD PLACEHOLDER**, version `0.0.0` | Package path exists; working exports and behavior are not proven. |
| Pipeline README | **CONFIRMED DRAFT** | Defines intended executable boundary and support-type invariant. |
| Pipeline entrypoints | **PLACEHOLDER COMMENTS** | Inspected ingest, normalize, validate, publish, and rollback entrypoints do not implement behavior. |
| Pipeline specs | **`stages: []`** | Declarative paths exist; no stage wiring is established. |
| Soil policy README | **GREENFIELD SCAFFOLD** | Policy path exists; complete rules are not established. |
| Support-type policy | **PROPOSED DEFAULT-DENY SCAFFOLD** | Fail-closed intent is visible; accepted policy behavior is not proven. |
| Schema index | **DRAFT / SCAFFOLDED** | Many schema paths exist. |
| Opened Soil schemas | **PROPOSED, `properties: {}`, `additionalProperties: true`** | Path and identifiers exist; meaningful validation is not established. |
| Validator index | **CONFIRMED README LANES** | Intended checks are documented. |
| Validator executables | **NEEDS VERIFICATION** | Parent README explicitly does not confirm executable files or CI wiring. |
| Domain workflow | **TODO ECHO JOBS** | Trigger and job scaffolding exist; substantive domain validation/proof/dry-run enforcement is not established by the inspected file. |
| Source registry topology | **CONFLICTED / NEEDS VERIFICATION** | Subtype-first and domain-first Soil source-registry surfaces coexist. |
| Domain registry | **CONFIRMED DRAFT README** | Domain-state registry boundary exists; emitted records and validators remain unverified. |
| Contract/schema path shape | **CONFLICTED / ADR-SENSITIVE** | Segmented `.../domains/soil/` and flatter `.../soil/` variants coexist in documentation/repository evidence. |
| Catalog path | **CANONICAL + COMPATIBILITY** | `data/catalog/domain/soil/` is canonical; `catalog/domain/soil/` is a compatibility redirect/drift fence. |
| Runtime/publication | **NOT ESTABLISHED** | Nothing here authorizes source use, public layer creation, advice, or publication. |

### Current configuration inventory

```text
configs/domains/soil/
└── README.md
```

This is a bounded indexed result, not a recursive tree receipt. No claim is made about differently named, branch-only, generated, ignored, or unindexed files.

### Default maturity posture

Until stronger evidence exists:

- configuration files are **inactive by presence**;
- no recursive discovery is assumed;
- no precedence order is assumed;
- no fallback is assumed safe;
- source and support-type vocabularies remain authority-bound;
- executable validation remains `NEEDS VERIFICATION`;
- public use remains unauthorized.

[Back to top](#top)

---

## What belongs here

Only safe, non-secret, Soil-scoped configuration material for a named and verified consumer belongs here.

| Accepted material | Purpose | Minimum posture |
|---|---|---|
| This `README.md` | Define the Soil configuration boundary. | Evidence-bounded and non-authoritative. |
| `*.template.yaml` / `*.template.yml` | Safe template for a verified Soil consumer. | Parseable; placeholders only; consumer and validation path named. |
| `*.example.yaml` / `*.example.json` / `*.example.toml` | Synthetic demonstration of supported keys. | No live source, private field, private sensor, restricted query, or exact protected context. |
| Development/test defaults | Deterministic fixture-bound behavior. | No-network where practical; never production by fallback. |
| Review defaults | Conservative hold, quarantine, abstain, caveat, or deny routing. | Cannot waive policy or release review. |
| Source-profile references | Select an already accepted SourceDescriptor/profile by stable ID. | Cannot create or activate a source. |
| Support-type profile references | Select an accepted static survey, grid, station, satellite, pedon, interpretation, or public-safe derivative profile. | Cannot invent or translate vocabulary locally. |
| Unit/depth/QC normalization references | Point to accepted normalization profiles. | Must preserve original value, unit, method, depth, QC, and transform provenance. |
| Freshness and stale-state profile references | Select accepted time handling for a source/product class. | Cannot silently present stale observations as current. |
| Public-safe display references | Select accepted generalization, aggregation, redaction, or caveat profiles. | Policy decision, transform receipt, review, and release remain required. |
| Migration notes | Document a verified key/path/version transition. | Time-bounded, reversible, and not a parallel authority. |

A config file should remain small, portable, deterministic, and explicit about the authority surfaces it references.

[Back to top](#top)

---

## What does NOT belong here

| Prohibited material | Why prohibited | Correct home or action |
|---|---|---|
| Tokens, passwords, private keys, cookies, signed URLs, service-account material | Repository is not a secret store. | Approved external secret system; rotate/revoke on exposure. |
| Live database strings, private endpoints, internal hosts, workstation paths | Creates operational disclosure and non-portable binding. | Deployment/infra/local ignored configuration. |
| SSURGO/SDA query results, survey tables, shapefiles, rasters, COGs, GeoParquet, PMTiles | These are source/lifecycle data, not config. | Appropriate `data/<phase>/soil/` lane. |
| Station, satellite, pedon, or private sensor payloads | Data and potentially sensitive operational context. | Lifecycle lanes with source, rights, policy, evidence, and release controls. |
| Source descriptors, rights rows, activation decisions, cadence records | Config cannot admit or activate sources. | Accepted source-registry lane. |
| MUKEY/COKEY/CHKEY crosswalk records | Trust-bearing identity/lineage state. | Registry/crosswalk/contract/data lanes under accepted authority. |
| Soil object definitions or semantic rules | Config cannot define meaning. | Accepted contract home. |
| JSON Schemas or enums | Config cannot define machine shape. | Accepted schema home. |
| Policy, support-type rules, sensitivity decisions, release rules | Config cannot authorize use or exposure. | `policy/` and release governance. |
| EvidenceBundles, EvidenceRefs as stored records, proofs, receipts | Config cannot prove itself. | `data/proofs/`, `data/receipts/`, accepted evidence homes. |
| Catalog, triplet, layer, release, correction, rollback records | Config is not lifecycle or release state. | `data/catalog/`, `data/triplets/`, `data/published/`, `release/`. |
| Exact private field, parcel, owner, producer, conservation-practice, or private-sensor context | Privacy, rights, business, and operational risk. | Quarantine/restricted handling; generalize or deny. |
| Suitability thresholds presented as recommendations | Interpretation is not advice or authority. | Accepted contract/policy/model methodology plus evidence and review. |
| Erosion scores presented as hazard warnings | Soil interpretation is not Hazards authority. | Hazards lane and official warning sources. |
| Hydrologic soil group presented as flood truth | Soil classification is only one input. | Hydrology/Hazards evidence and policy. |
| Generated summaries presented as observations | AI/model language is not evidence. | Governed AI runtime with evidence and receipts. |
| Automatic public-layer settings that bypass release | Config cannot publish. | Governed release workflow and released artifacts. |

Do not use this lane as a convenient parallel home for source, schema, contract, policy, registry, data, proof, catalog, graph, release, or publication objects.

[Back to top](#top)

---

## Inputs

### Admissible authoring inputs

A future config payload may be authored only from:

- a verified consumer requirement;
- accepted source-profile identifiers;
- accepted support-type vocabulary/profile identifiers;
- accepted contract and schema references;
- accepted unit, method, depth, QC, time, sensitivity, and public-safe profile references;
- conservative local/test/review defaults;
- synthetic examples;
- a documented migration from a verified key or path.

### Required authoring context

Before adding a payload, identify:

1. canonical domain slug;
2. exact consumer path and owner;
3. configuration class;
4. parser/loader and version;
5. binding path and precedence behavior;
6. missing-file, unknown-key, and fallback behavior;
7. authoritative source/profile references;
8. object families affected;
9. support type(s) affected;
10. source role and vocabulary version;
11. survey/source vintage and lineage expectations;
12. units, depth basis, method, and QC expectations;
13. time, freshness, stale-state, and supersession expectations;
14. rights, privacy, private-land, and operational-sensor posture;
15. cross-domain joins;
16. validation and no-network strategy;
17. logging/redaction behavior;
18. deactivation, correction, and rollback.

### Reject or quarantine authoring inputs that contain

- real credentials or private bindings;
- source payloads or live operational data;
- field/parcel/owner/producer identifiers;
- private sensor coordinates, network IDs, or access details;
- undocumented role/support-type aliases;
- thresholds copied without a method, source, unit, depth, or fitness-for-use statement;
- instructions to bypass source admission, evidence, policy, review, release, or rollback.

[Back to top](#top)

---

## Outputs

This lane may provide configuration support to a verified consumer by supplying:

- safe templates and examples;
- explicit profile references;
- conservative validation/review defaults;
- documented migration mappings;
- parseable configuration with no side effects.

It does **not** output or authorize:

- a soil observation or interpretation;
- source activation or data fetch;
- lifecycle transitions;
- schema, policy, or contract authority;
- EvidenceBundle closure;
- catalog or graph closure;
- a public layer or API response;
- agronomic, engineering, conservation, insurance, legal, or hazard advice;
- release, correction, withdrawal, or rollback decisions.

A consumer must explicitly bind to a file. Directory presence alone has no operational meaning.

[Back to top](#top)

---

## Validation

No executable validator for this config lane was verified in this revision. The matrix below defines the expected validation target; it is not a claim of current enforcement.

### Validation matrix

| Check | Required result | Current evidence |
|---|---|---|
| Syntax/parse | Declared format parses under the named parser/version. | `NEEDS VERIFICATION` per payload. |
| Known-key validation | Unknown/misspelled keys fail or produce an explicit safe outcome. | `UNKNOWN`. |
| Schema validation | Accepted non-empty schema validates the payload. | Opened Soil schemas are `PROPOSED` scaffolds; not sufficient yet. |
| Consumer compatibility | Named consumer reads the exact file and version. | No direct consumer found in bounded search. |
| Deterministic normalization | Same inputs and parser version produce the same normalized config. | `PROPOSED`. |
| Source/profile existence | Referenced source/profile exists, is active where required, and is valid for the consumer. | `NEEDS VERIFICATION`. |
| Source-role vocabulary | Referenced role uses an accepted vocabulary/version; no local upcast. | `CONFLICTED / NEEDS VERIFICATION`. |
| Support-type separation | Static survey, grid, station, satellite, pedon/profile, interpretation, and public-safe derivative remain distinct. | Mandatory doctrine; executable enforcement unverified. |
| Survey lineage | MUKEY/COKEY/CHKEY, survey area, source vintage, join path, and derivation remain auditable. | `NEEDS VERIFICATION`. |
| Units/depth/method/QC | Required dimensions and measurement context are present and compatible. | `NEEDS VERIFICATION`. |
| Time/freshness/stale state | Source, observed, valid, retrieval, release, correction, expiry, and supersession behavior are explicit where material. | `NEEDS VERIFICATION`. |
| Scale/resolution/support | Source scale, raster resolution, geometry support, aggregation basis, and limitations remain visible. | `NEEDS VERIFICATION`. |
| Interpretation caveat | Suitability/erosion/hydrologic interpretation includes method, inputs, limitations, and no-advice boundary. | `NEEDS VERIFICATION`. |
| Rights and privacy | No private owner/producer/parcel/field/sensor context is exposed. | Required; scanner/review coverage unverified. |
| Secret scan | No credentials, private keys, tokens, cookies, signed URLs, or secret values. | Required; full automation unverified. |
| Private endpoint/path scan | No private endpoints, connection strings, or personal paths. | Required; full automation unverified. |
| No-network parse | Parsing and basic validation do not access live services where practical. | `PROPOSED`. |
| No side effects | Validation does not fetch, write lifecycle data, publish, deploy, or mutate registry/release state. | Required. |
| Cross-domain boundary | Soil config does not create crop, water, geology, ecology, hazard, ownership, or legal truth. | Manual and executable review required. |
| Public-boundary check | Public consumers use governed APIs/released artifacts, not this lane directly. | Required; runtime integration unverified. |
| Logging/redaction | Secrets, private land, source payloads, and exact restricted context are not logged. | `NEEDS VERIFICATION`. |
| Rollback | Prior config and downstream state can be restored or deactivated. | `NEEDS VERIFICATION`. |
| Documentation links | Referenced paths and anchors resolve or are labeled unresolved. | Structural check performed for this README. |

### Finite configuration-review outcomes

These outcomes apply to configuration support only—not source admission or publication.

| Outcome | Meaning | Required action |
|---|---|---|
| `PASS` | Required checks pass for the scoped config change. | May merge as config support; no authority is transferred. |
| `HOLD` | Checkable uncertainty remains without a known immediate leak. | Keep inactive and resolve the evidence gap. |
| `DENY` | Secret, unsafe binding, support collapse, privacy leak, authority bypass, or public-path bypass exists. | Remove/quarantine and invoke incident/correction handling as applicable. |
| `ABSTAIN` | Consumer cannot safely choose among unresolved sources, roles, support types, methods, or time states. | Do not fabricate a default. |
| `ERROR` | Parser, validator, or review process failed. | Repair the process; failure is not permission. |

### Documentation validation for this revision

- one H1;
- required Directory Rules folder headings present and ordered;
- no duplicate H2s;
- internal quick-link anchors resolve;
- fenced code blocks balance;
- final newline present;
- bounded secret-pattern scan passes;
- only the requested Markdown file changes.

[Back to top](#top)

---

## Review burden

### Review matrix

| Change | Required review posture |
|---|---|
| README clarification | Config/docs + Soil steward. |
| New template/example | Config steward + consumer owner + Soil steward + validation steward. |
| Source/profile reference | Add source steward, rights reviewer, and connector/pipeline owner. |
| Support-type mapping | Add Soil architecture/contract/schema/policy stewards; mapping must not be local-only. |
| MUKEY/COKEY/CHKEY or survey-lineage key | Add survey/lineage steward and schema/contract/registry reviewers. |
| Unit/depth/method/QC key | Add moisture/property/pedon subject reviewer and validation steward. |
| Freshness/stale-state key | Add source/operations steward and public-surface reviewer when current-state display is affected. |
| Suitability/erosion/interpretation key | Add policy, evidence, domain-method, and release reviewers; no-advice language required. |
| Parcel/field/producer/private-sensor handling | Add privacy, rights, security, policy, and release reviewers. |
| Public-safe geometry/aggregation/redaction key | Add policy, sensitivity, release, and UI/API reviewers. |
| Config discovery/precedence/fallback | ADR-class architecture and consumer review. |
| Schema/contract path migration | ADR, migration map, compatibility note, tests, and rollback. |
| Source-registry topology change | Registry ADR/migration and source-steward review. |

### Change budget

Prefer one bounded concern per PR:

- one README revision;
- one template plus its validation and consumer test;
- one source/profile reference update;
- one key migration with compatibility and rollback;
- one accepted vocabulary/profile version update.

Do not bundle config cleanup with source activation, schema redesign, policy rewrite, registry migration, pipeline implementation, or release changes unless the task explicitly requires a governed multi-root change.

[Back to top](#top)

---

## Related folders

| Responsibility | Current or proposed home | Relationship |
|---|---|---|
| Parent configuration boundary | `configs/domains/README.md` | Defines the no-secret, non-authoritative child-lane contract. |
| Soil doctrine placeholder | `docs/domains/soil/README.md` | Path exists but is currently a greenfield placeholder. |
| Soil architecture | `docs/domains/soil/ARCHITECTURE.md` | Strongest inspected Soil scope/support-type/lifecycle architecture surface. |
| Soil path governance | `docs/domains/soil/CANONICAL_PATHS.md` | Records segmented-versus-flat path variance and canonical placement law. |
| Soil lifecycle | `docs/domains/soil/DATA_LIFECYCLE.md` | Human-facing RAW→PUBLISHED and continuity posture. |
| Soil API contracts | `docs/domains/soil/API_CONTRACTS.md` | Proposed governed interface shapes and finite outcomes. |
| Semantic contracts | `contracts/domains/soil/` and `contracts/soil/` | Path authority is ADR-sensitive; config references, never duplicates. |
| Schemas | `schemas/contracts/v1/domains/soil/` and `schemas/contracts/v1/soil/` | Path authority is ADR-sensitive; opened segmented schemas are proposed scaffolds. |
| Policy | `policy/domains/soil/` and accepted cross-cutting roots | Current parent is a greenfield scaffold; support-type module is proposed default-deny. |
| Shared implementation | `packages/domains/soil/` | Package README is draft; `pyproject.toml` is version `0.0.0` placeholder. |
| Pipelines | `pipelines/domains/soil/` | README is detailed; inspected core entrypoints are placeholders. |
| Declarative specs | `pipeline_specs/soil/` | Inspected ingest/validate/publish specs have empty stage lists. |
| Validators | `tools/validators/domains/soil/` | README child lanes exist; executables and CI binding remain unverified. |
| Tests/fixtures | `tests/domains/soil/`, `fixtures/domains/soil/` | Expected enforceability and samples; current depth requires verification. |
| Source registry | `data/registry/sources/soil/`, `data/registry/soil/sources/` | Subtype-first/domain-first topology remains unresolved. |
| Domain registry | `data/registry/domains/soil/` | Domain-state registry boundary; emitted records unverified. |
| Canonical catalog | `data/catalog/domain/soil/` | CATALOG-stage Soil records. |
| Compatibility catalog | `catalog/domain/soil/` | Redirect/drift fence only; not canonical authority. |
| Lifecycle data | `data/<phase>/soil/` | Source and derived data by governed phase. |
| Triplets/graphs | `data/triplets/soil/` or accepted lane | Derived projection only; not Soil truth. |
| Published artifacts | `data/published/layers/soil/` | Released public-safe derivatives only. |
| Receipts/proofs | `data/receipts/soil/`, `data/proofs/soil/` or accepted shared homes | Process memory and evidence closure. |
| Release | `release/candidates/soil/`, `release/manifests/soil/`, correction/rollback homes | Promotion, publication, correction, withdrawal, rollback. |
| Workflow | `.github/workflows/domain-soil.yml` | Inspected file is a TODO-only scaffold. |

[Back to top](#top)

---

## ADRs and drift triggers

### Current decision surfaces

| Decision surface | Status | Config-lane effect |
|---|---:|---|
| Schema home | **ADR-SENSITIVE / CONFLICTED** | Do not select between segmented and flat schema paths locally. |
| Contract home | **ADR-SENSITIVE / CONFLICTED** | Do not create mirrors or local aliases. |
| Source registry topology | **CONFLICTED / NEEDS VERIFICATION** | Do not duplicate source records across domain-first and subtype-first lanes. |
| Source-role vocabulary | **CONFLICTED / NEEDS VERIFICATION** | Do not translate legacy `authority / observation / context / model` wording into canonical roles by config convention. |
| Support-type vocabulary | **DOCTRINE STRONG / MACHINE AUTHORITY NEEDS VERIFICATION** | Config may reference accepted terms but must not define them. |
| Config discovery/precedence | **UNDECIDED** | Explicit binding only. |
| Catalog compatibility root | **CONFIRMED COMPATIBILITY** | Never read/write `catalog/domain/soil/` as canonical catalog authority. |
| Current-condition/public-display profile | **UNDECIDED / NEEDS VERIFICATION** | Current displays fail closed without accepted freshness, QC, policy, and release rules. |
| Interpretation/advice boundary | **DOCTRINE STRONG / ENFORCEMENT NEEDS VERIFICATION** | Config cannot turn an interpretation into advice or authority. |

### ADR or drift review is triggered by

- introducing a third schema, contract, policy, registry, catalog, or release home;
- creating aliases between source-role or support-type vocabularies;
- enabling recursive config discovery;
- defining global precedence or fallback behavior;
- allowing config to activate sources;
- allowing station/satellite/current-condition public display;
- allowing field/parcel/owner/private-sensor configuration;
- using Soil interpretation for regulatory, conservation-compliance, agronomic, engineering, insurance, lending, or hazard decisions;
- changing the canonical catalog/compatibility relationship;
- changing public-client access to configuration or internal stores.

This README enacts none of those decisions.

[Back to top](#top)

---

## Last reviewed

**2026-07-14**, against `main@484b2f682d99f53586376ea95a46f962a96ee4bd`.

Review again when:

- the first non-README Soil config payload is proposed;
- a consumer binds to this lane;
- source-role or support-type vocabulary is accepted or changed;
- schema/contract or registry topology is resolved;
- Soil validators become executable;
- the domain workflow becomes substantive;
- a current-state moisture or interpretation surface is proposed;
- private-land, parcel, producer, or private-sensor context enters scope;
- six months pass.

[Back to top](#top)

---

## Scope and bounded context

The Soil configuration bounded context supports named consumers dealing with:

- static soil-survey objects;
- survey map units, components, horizons, and joins;
- measured or derived soil properties;
- hydrologic soil group;
- pedon/profile evidence;
- station and satellite soil moisture;
- gridded derivatives;
- source vintage and time caveats;
- erosion and suitability interpretations;
- public-safe Soil layers and evidence views.

It does not own:

- crop/yield or management truth;
- streamflow, groundwater, flood, or hazard truth;
- lithology, stratigraphy, or borehole truth;
- habitat, flora, or fauna occurrence truth;
- parcel/title/ownership truth;
- official conservation-compliance determinations;
- engineering/site-design recommendations;
- public release.

### Vocabulary used in this README

| Term | Meaning |
|---|---|
| **support type** | The spatial/observational/interpretive support class of a Soil record. |
| **source role** | The governed role assigned to a source/use at admission; never upgraded by config. |
| **source vintage** | Version/date/release state of the source dataset or product. |
| **lineage** | Auditable chain across source IDs, survey area, MUKEY/COKEY/CHKEY, transforms, versions, digests, and outputs. |
| **measurement context** | Value plus unit, depth, method, quality state, time, and support. |
| **interpretation** | Derived fitness-for-use result with explicit method, inputs, limitations, and non-advice posture. |
| **public-safe derivative** | Policy- and release-approved generalized/aggregated/redacted output with receipts and rollback. |
| **consumer binding** | Reviewed implementation that reads an exact config path/version. |

[Back to top](#top)

---

## Configuration classes

| Class | Intended use | Commit posture | Activation posture |
|---|---|---|---|
| `template` | Demonstrate supported fields and placeholders. | Safe after review. | Inactive by presence. |
| `example` | Explain a synthetic configuration. | No live data or bindings. | Inactive by presence. |
| `dev-default` | Conservative development behavior. | Portable, no secrets. | Explicit dev consumer only. |
| `test-default` | Deterministic fixture-bound behavior. | Synthetic, no-network where practical. | Test harness only. |
| `review-default` | Hold/abstain/quarantine routing. | Fail closed. | Review tooling only. |
| `source-profile-reference` | Select an accepted Soil source/profile. | Stable ID only. | Does not activate source. |
| `support-profile-reference` | Select accepted support-type and validation rules. | No local vocabulary invention. | Consumer applies only after validation. |
| `moisture-profile-reference` | Select accepted unit/depth/QC/time/freshness rules. | No station credentials or private coordinates. | No live subscription by presence. |
| `interpretation-profile-reference` | Select accepted suitability/erosion methodology and caveats. | No advisory authority. | Requires policy/evidence/release for public use. |
| `public-safe-template` | Select accepted aggregation/generalization/redaction profile. | No protected geometry. | Policy/receipt/review/release required. |
| `compatibility` | Temporary mapping for a verified key/path transition. | Owner-linked and sunset-bound. | Remove after migration closure. |
| `production-binding` | Real endpoint, credential, database, private sensor, or deployment value. | **Forbidden here.** | External deployment/secret system only. |

[Back to top](#top)

---

## Minimum configuration contract

A non-trivial Soil config should expose or reference:

| Field | Requirement |
|---|---|
| `domain_slug` | `soil`. |
| `config_class` | One declared class. |
| `intended_consumer` | Exact verified consumer path and owner. |
| `consumer_version` | Verified version/range or unresolved label. |
| `format` | YAML/JSON/TOML/etc. plus parser/version. |
| `binding` | Exact file selection mechanism. |
| `precedence` | Explicit order or `UNRESOLVED`; never inferred. |
| `missing_file_behavior` | Safe inactive/hold/error behavior. |
| `unknown_key_behavior` | Fail or explicit safe handling. |
| `object_families` | Affected Soil object families. |
| `source_profile_refs` | Stable references to accepted source profiles. |
| `source_role_vocabulary` | Accepted vocabulary/version reference. |
| `support_type_refs` | Accepted support-type profile references. |
| `source_vintage_rules` | Version/date selection and stale handling. |
| `lineage_rules` | Required survey/source IDs, joins, digests, and transforms. |
| `units_profile` | Accepted units and conversion rules. |
| `depth_profile` | Depth reference, units, interval semantics, and validation. |
| `method_profile` | Measurement/derivation method reference. |
| `quality_profile` | QC flags, rejection/hold rules, and missing-QC behavior. |
| `temporal_profile` | Source/observed/valid/retrieval/release/correction/expiry handling. |
| `spatial_support_profile` | Point/polygon/grid/profile support, scale, resolution, aggregation. |
| `interpretation_profile` | Method, inputs, limitations, caveats, non-advice boundary. |
| `sensitivity_profile` | Private land, producer, field, sensor, and cross-lane handling. |
| `public_safe_profile` | Accepted aggregation/generalization/redaction profile reference. |
| `validation_ref` | Executable validator or `NEEDS VERIFICATION`. |
| `network_behavior` | `none` for parse/validation by default. |
| `side_effects` | `none` for parsing/validation. |
| `logging_posture` | Redacted; no payload/private context. |
| `owner` | Accepted owner or `OWNER_TBD`. |
| `reviewed_at` | ISO date. |
| `deprecation` | Replacement/sunset when temporary. |
| `rollback` | Prior file/profile/version and deactivation procedure. |

A universal machine schema for this contract is **PROPOSED**, not created by this README.

[Back to top](#top)

---

## Consumer binding, precedence, and discovery

### Explicit binding only

A consumer should identify:

- exact path;
- config version;
- expected digest;
- parser version;
- accepted schema/profile refs;
- environment scope;
- safe failure behavior.

### No recursive discovery

Do not auto-load every file under `configs/domains/soil/`. Folder presence or filename resemblance must not:

- activate a source;
- select a survey vintage;
- subscribe to a sensor;
- initiate an SDA query;
- download a raster;
- build a catalog;
- publish a layer;
- choose an interpretation;
- broaden access.

### No precedence by convention

A sequence such as:

```text
base -> domain -> dev/test -> local -> environment -> deployment
```

is illustrative only. A verified consumer must define merge/replace semantics, environment substitution, type coercion, unknown-key behavior, fallback, and audit logging.

### Safe failure

Missing, invalid, stale, or ambiguous config should produce an explicit inactive, hold, abstain, deny, or error state. It must not silently:

- use the newest-looking source;
- choose the most detailed raster;
- assume a default unit or depth;
- treat missing QC as good;
- make an interpretation public;
- reveal private land/sensor context;
- fall back to production.

[Back to top](#top)

---

## Soil object-family boundaries

| Object family | Config may support | Config must not do |
|---|---|---|
| `SoilMapUnit` | Select display/validation profile for a verified consumer. | Create survey authority, merge units by geometry/name, or treat polygon as current condition. |
| `SoilComponent` | Select component percentage/lineage validation profile. | Rewrite component identity or make dominant component equal whole map unit. |
| `Horizon` | Select depth/unit/order validation profile. | Repair missing/overlapping horizons silently. |
| `ComponentHorizonJoin` | Select accepted join validation. | Invent MUKEY/COKEY/CHKEY relationships. |
| `SoilProperty` | Select unit/method/depth/QC profile. | Treat derived, estimated, or missing-method value as measured fact. |
| `HydrologicSoilGroup` | Select classification/caveat display profile. | Present as flood prediction, infiltration measurement, or engineering design value. |
| `SoilMoistureObservation` | Select station/satellite normalization/freshness profile. | Collapse support types or imply field-wide/current truth. |
| `Pedon` / `SoilProfileView` | Select profile display/validation profile. | Generalize a pedon into map-unit truth without reviewed derivation. |
| `ErosionRisk` | Select an accepted interpretation profile and caveat. | Issue hazard warning or compliance/management advice. |
| `SuitabilityRating` | Select accepted fitness-for-use interpretation. | Issue agronomic, engineering, lending, insurance, legal, or management recommendation. |
| `SoilTimeCaveat` | Select required caveat class/display behavior. | Suppress source vintage, observation time, stale state, or supersession. |
| Public-safe Soil derivative | Select accepted display profile reference. | Create release state or bypass policy/receipt/review. |

[Back to top](#top)

---

## Source role and support-type separation

### Support-type invariant

These support types must remain distinct:

| Support type | Examples | Must not become |
|---|---|---|
| `authoritative_static_soil` | SSURGO/SDA survey evidence | Current field condition or station observation. |
| `gridded_derivative_soil` | gSSURGO, gNATSGO, SoilGrids | Survey-table authority or exact field truth. |
| `station_soil_moisture` | Mesonet, SCAN, USCRN | Countywide/polygon surface or satellite reading. |
| `satellite_soil_moisture` | SMAP and similar grid products | In-situ station observation. |
| `pedon_evidence` | Profile descriptions and measurements | Map-unit-wide truth. |
| `interpretation` | Erosion, suitability, hydrologic interpretation | Measured property, official recommendation, or hazard warning. |
| `public_safe_derivative` | Released generalized/aggregated/redacted product | Canonical internal evidence or source record. |

A value without an accepted support-type tag must not proceed as a normal Soil fact.

### Source-role boundary

Soil repository materials contain multiple role vocabularies, including legacy `authority / observation / context / model` wording and broader canonical role sets. Until governance resolves the mapping:

- do not translate roles locally;
- record vocabulary/version explicitly;
- preserve original role and admission record;
- reject unsupported aliases;
- do not let support type substitute for source role;
- do not let source role substitute for support type.

### Aggregation across support types

Cross-support aggregation requires:

1. explicit derivation method;
2. stated purpose;
3. compatible units/time/scale;
4. retained source/support lineage;
5. uncertainty and limitations;
6. validation receipt;
7. policy/review;
8. release decision for public use.

[Back to top](#top)

---

## Survey identity and lineage

### Required lineage posture

Where applicable, preserve:

- source system and product;
- source vintage/version;
- survey area;
- `mukey`;
- `cokey`;
- `chkey`;
- component-horizon join path;
- source table/field;
- query hash;
- input/content digest;
- geometry hash;
- transform/spec hash;
- aggregation method;
- output digest;
- supersession/correction links.

### Prohibited config shortcuts

Configuration must not:

- merge records because geometries overlap;
- use names/symbols as canonical identity without accepted crosswalk;
- select “latest” without an accepted version policy;
- drop source vintage during export;
- repair orphan COKEY/CHKEY links silently;
- infer missing horizon depth;
- treat dominant component as the entire map unit;
- replace source-native identifiers with display IDs;
- overwrite raw/native values during normalization.

### Identity change handling

A change to identity or lineage keys requires contract, schema, registry, migration, fixture, validator, consumer, and rollback review. It is not a config-only change.

[Back to top](#top)

---

## Units, depth, method, and quality control

A Soil value is not safely interpretable without measurement context.

### Required measurement dimensions

| Dimension | Required handling |
|---|---|
| Value | Preserve native and normalized value separately. |
| Unit | Explicit unit and conversion profile; no silent assumptions. |
| Depth | Top/bottom or sensor depth plus units and reference convention. |
| Method | Laboratory, field, survey estimate, model, remote sensing, or other method reference. |
| Quality | QC flags, missing-QC state, rejection/hold rules. |
| Support | Survey/grid/station/satellite/pedon/interpretation class. |
| Time | Observed/valid/retrieval/source/release/correction as material. |
| Uncertainty | Precision, interval, confidence, limitations, or not-provided state. |
| Source | Source/profile/vintage and evidence refs. |

### Soil-moisture constraints

A moisture profile should define:

- volumetric versus gravimetric basis;
- accepted units;
- sensor/product variable;
- depth and interval;
- timestamp/timezone;
- QC and missing-QC behavior;
- cadence/freshness;
- station/grid/granule identity;
- duplicate key;
- stale-state behavior;
- public-display limits.

### Horizon-depth constraints

A horizon profile should define:

- top/bottom convention;
- units;
- ordering;
- overlap/gap policy;
- missing-depth policy;
- bedrock/restriction handling;
- component/pedon relationship;
- invalid-record outcome.

Config cannot repair scientifically material measurement gaps by convenience.

[Back to top](#top)

---

## Time, freshness, and stale state

Keep distinct where material:

| Time kind | Meaning |
|---|---|
| Source time | Time represented or published by source. |
| Observed time | Time measurement/observation occurred. |
| Valid time | Interval during which a classification/status applies. |
| Retrieval time | Time KFM retrieved material. |
| Run time | Time transformation/validation ran. |
| Release time | Time a public artifact became released. |
| Correction time | Time a correction/withdrawal/supersession took effect. |
| Expiry/stale threshold | Accepted point after which current-state use is blocked or caveated. |

### Static survey versus current observations

Static survey products and soil-moisture observations require different temporal treatment:

- survey vintage is not a current observation time;
- retrieval date does not make old source content current;
- station cadence does not establish representativeness;
- satellite revisit does not establish field-scale truth;
- stale-state behavior must be source/profile-specific;
- public current-state display requires accepted freshness/QC/policy/release support.

### Supersession

When source versions or observations are superseded:

- preserve prior IDs/digests;
- record replacement relationship;
- invalidate affected caches/derivatives where required;
- propagate correction/review;
- keep rollback target;
- never silently overwrite lineage.

[Back to top](#top)

---

## Scale, resolution, and spatial support

### Required distinctions

| Spatial support | Examples | Constraint |
|---|---|---|
| Survey polygon | SSURGO map unit | Not current field condition; internal heterogeneity remains. |
| Component/horizon | Tabular/profile support | Not a polygon without reviewed join/aggregation. |
| Pedon point/profile | Specific observation/profile | Not map-unit-wide truth. |
| Station point/depth | In-situ moisture sensor | Not a surrounding surface without explicit modeling. |
| Satellite/grid cell | SMAP or other raster cell | Not station truth; resolution and retrieval support remain visible. |
| Gridded derivative | gSSURGO/gNATSGO/SoilGrids | Not source survey authority; derivation limits remain visible. |
| Generalized public layer | Released derivative | Not canonical internal geometry or evidence. |

### Configuration requirements

Any spatial profile should preserve:

- CRS;
- source scale/resolution;
- cell size;
- geometry support type;
- aggregation/resampling method;
- nodata handling;
- uncertainty/limitations;
- source vintage;
- public-safe transform and receipt refs.

Do not select the highest-resolution product merely because it is available. Resolution is not authority, accuracy, fitness, or permission.

[Back to top](#top)

---

## Interpretation, suitability, and advice boundary

Soil interpretations are derived products, not universal facts.

### Required interpretation context

A referenced interpretation profile should identify:

- purpose and claim family;
- target use;
- input sources and support types;
- source vintages;
- method/version;
- units and thresholds;
- spatial/temporal scope;
- uncertainty;
- limitations;
- excluded uses;
- review requirements;
- evidence refs;
- policy and release requirements;
- correction/rollback path.

### Config must not authorize

- crop recommendations;
- fertilizer or irrigation prescriptions;
- conservation-compliance determinations;
- engineering foundation/septic/road design;
- insurance or lending decisions;
- property valuation;
- legal conclusions;
- hazard warnings;
- guaranteed suitability or performance.

### Erosion and hydrologic context

- `ErosionRisk` remains interpretation, not a Hazards event or warning.
- `HydrologicSoilGroup` remains classification/context, not infiltration measurement, runoff forecast, or flood determination.
- Soil × Hydrology/Agriculture/Hazards combinations require governed cross-domain evidence and ownership boundaries.

[Back to top](#top)

---

## Cross-domain joins and sensitive context

### Ownership-preserving joins

| Join | Soil may contribute | Soil config must not create |
|---|---|---|
| Soil × Agriculture | Soil properties, moisture, suitability context | Crop/yield/management truth. |
| Soil × Hydrology | Hydrologic group, moisture, infiltration context | Streamflow, groundwater, flood truth. |
| Soil × Geology | Parent-material relation | Lithology, stratigraphy, borehole truth. |
| Soil × Habitat/Flora/Fauna | Substrate/moisture context | Habitat or occurrence truth; rare-location exposure. |
| Soil × People/Land | Generalized land context where allowed | Ownership, title, parcel boundary, living-person/producer truth. |
| Soil × Hazards | Erosion/runoff context | Official warning, incident, or emergency guidance. |

### Sensitive contexts

Default to deny, quarantine, generalize, aggregate, or restricted review for:

- owner- or producer-identifying data;
- field-level private operational data;
- parcel-linked interpretations;
- conservation-practice or compliance context;
- private sensor locations/network identifiers;
- unpublished/proprietary surveys;
- rare-species or culturally sensitive joins;
- source-term-restricted data;
- derivative combinations that permit re-identification.

### Public-safe derivatives

A public-safe profile reference is insufficient by itself. Public use requires:

- accepted policy decision;
- transform/aggregation/redaction receipt;
- evidence closure;
- rights/attribution;
- review state;
- release manifest;
- correction and rollback.

[Back to top](#top)

---

## Logging, telemetry, and observability

### Permitted metadata

- config version/digest;
- consumer version;
- profile IDs;
- source IDs without credentials;
- support type;
- validator/reason code;
- run/correlation ID;
- finite outcome;
- redacted counts;
- timing metrics.

### Prohibited logging

- credentials or authorization headers;
- signed/private URLs;
- private database/endpoint details;
- full source payloads;
- exact private field/parcel/owner/producer data;
- private sensor coordinates/network IDs;
- proprietary survey content;
- unredacted queries containing protected context;
- raw evidence bundles;
- secret values from environment substitution.

Logs and telemetry are operational records, not evidence, policy, release state, or public truth.

[Back to top](#top)

---

## Failure behavior

| Condition | Required outcome |
|---|---|
| Missing source/profile | `HOLD` / `ABSTAIN`; do not invent. |
| Source inactive/rights unresolved | `DENY` or quarantine. |
| Unknown role vocabulary | `ABSTAIN`; governance mapping required. |
| Missing/unknown support type | `DENY` / `ABSTAIN` / quarantine. |
| Support-type collapse | `DENY`. |
| Broken MUKEY/COKEY/CHKEY lineage | quarantine or validation failure. |
| Missing unit/depth/method | `ABSTAIN` / validation failure. |
| Missing QC where required | hold/deny per accepted profile. |
| Stale observation | mark stale, suppress current-state claim, or deny. |
| Incompatible scale/resolution | `ABSTAIN` / validation failure. |
| Interpretation missing caveat/method | `DENY` public use. |
| Private-land/private-sensor exposure | `DENY`; invoke sensitivity review. |
| Missing EvidenceBundle support | `ABSTAIN`. |
| Policy denies/restricts | honor decision; config cannot override. |
| Release absent | no public output. |
| Parser/validator error | `ERROR`; do not fall back permissively. |
| Rollback target missing | block activation/promotion. |

Fail-safe behavior must be explicit and testable. Silence or best-effort publication is not acceptable.

[Back to top](#top)

---

## Governed AI and generated language

AI may help interpret released Soil evidence only after retrieval, evidence resolution, policy, sensitivity, and release checks.

Configuration may select an accepted AI behavior profile, but it cannot:

- make AI a source;
- let generated language replace EvidenceBundle support;
- infer missing units, depths, methods, QC, source role, or support type;
- turn a suitability score into advice;
- conceal source vintage or stale state;
- expose private land/sensor context;
- describe a grid as survey truth;
- describe an interpretation as measured fact;
- publish an unreleased candidate.

Expected finite outcomes:

- `ANSWER` with citations, support type, source role, time caveat, limitations, and release state;
- `ABSTAIN` when evidence, lineage, units, support, or freshness is insufficient;
- `DENY` when policy or sensitivity blocks the request;
- `ERROR` when retrieval/validation fails.

AI receipts belong in accepted receipt lanes, not this config directory.

[Back to top](#top)

---

## Migration and anti-bypass posture

### Misplaced material

When non-config material is found here:

1. freeze activation and public use;
2. identify the owning responsibility root;
3. remove/quarantine secrets or sensitive content;
4. preserve provenance and current consumers;
5. move source records to registry;
6. move meaning to contracts;
7. move shape to schemas;
8. move policy to policy roots;
9. move lifecycle/trust/catalog/release objects to their owning roots;
10. update explicit bindings;
11. add compatibility note only when required;
12. test deactivation and rollback;
13. record drift/correction when consequential.

### Anti-bypass matrix

| Bypass | Required response |
|---|---|
| Consumer recursively loads config directory | Reject; explicit allowlist/binding required. |
| Config activates a source | Reject; registry/source activation governance required. |
| Config selects private endpoint/credential | Remove and use external deployment/secret controls. |
| Config defines role/support vocabulary | Move to accepted contract/schema/policy/registry authority. |
| Config merges support types | Reject. |
| Config rewrites lineage | Reject; governed crosswalk/migration required. |
| Config converts interpretation to advice | Reject. |
| Config publishes to compatibility catalog | Reject; canonical catalog/release path required. |
| Public client reads config directly | Reject; governed API/released artifact path required. |
| Validation contacts live service | Replace with no-network fixtures or bounded documented exception. |
| Missing config causes permissive fallback | Replace with inactive/hold/error state. |

[Back to top](#top)

---

## Rollback, correction, and deactivation

### Rollback triggers

Rollback or deactivate when:

- a secret or private binding appears;
- source/profile authority is wrong or unresolved;
- support types collapse;
- lineage is corrupted;
- unit/depth/method/QC behavior is unsafe;
- stale observations appear current;
- private land/sensor context is exposed;
- interpretation is presented as advice/authority;
- public clients bypass governed interfaces;
- a compatibility path becomes authoritative;
- validation or release references are missing;
- consumer behavior differs from documented binding.

### Correction procedure

1. disable the affected consumer/config version;
2. stop source fetch/subscription if incorrectly bound;
3. restore the prior reviewed config;
4. quarantine affected outputs;
5. rotate/revoke credentials if exposed;
6. identify downstream artifacts/caches/answers;
7. issue correction/withdrawal/rollback through release governance;
8. invalidate or rebuild derivatives where required;
9. move misplaced content to the owning root;
10. add tests/validators/scanners;
11. verify cleanup and rollback completion.

For this README revision, the prior blob is:

```text
5b9b0c36546d48b338a1aed1818c5c64816ff094
```

[Back to top](#top)

---

## Definition of done for the first payload

Before the first non-README Soil config file is accepted:

- [ ] exact consumer and owner verified;
- [ ] config class, parser, version, binding, precedence, missing-file, unknown-key, and fallback behavior defined;
- [ ] accepted non-empty schema validates;
- [ ] contract, policy, registry, and release/profile references verified;
- [ ] source IDs, roles, rights, cadence, vintage, attribution, and authority limits verified;
- [ ] accepted source-role vocabulary/version referenced;
- [ ] accepted support-type vocabulary/profile referenced;
- [ ] support-type anti-collapse tests pass;
- [ ] object-family separation tests pass;
- [ ] MUKEY/COKEY/CHKEY and survey-lineage tests pass;
- [ ] unit/depth/method/QC tests pass;
- [ ] moisture station/satellite/grid identity and stale-state tests pass;
- [ ] scale/resolution/spatial-support tests pass;
- [ ] interpretation fitness-for-use/no-advice tests pass;
- [ ] private land, producer, field, sensor, rare-location, and restricted-source denial tests pass;
- [ ] cross-domain ownership tests pass;
- [ ] no credentials/private endpoints/personal paths/protected values;
- [ ] no-network parse/validation where practical;
- [ ] logging is redacted;
- [ ] no lifecycle/trust/catalog/graph/release objects stored here;
- [ ] consumer negative states pass;
- [ ] policy/review/release owners approve;
- [ ] deactivation, correction, cache invalidation, and rollback are tested;
- [ ] docs and evidence ledger updated.

[Back to top](#top)

---

## Verification backlog

| Item | Status |
|---|---:|
| Recursive config inventory | `NEEDS VERIFICATION` |
| Direct consumer/loader | `UNKNOWN` |
| Discovery/precedence/fallback | `UNKNOWN` |
| Soil doctrine parent README depth | `PLACEHOLDER` |
| Segmented vs flat contract path | `CONFLICTED / ADR-SENSITIVE` |
| Segmented vs flat schema path | `CONFLICTED / ADR-SENSITIVE` |
| Source-registry topology | `CONFLICTED / NEEDS VERIFICATION` |
| Catalog compatibility migration | `NEEDS VERIFICATION` |
| Source-role vocabulary | `CONFLICTED / NEEDS VERIFICATION` |
| Support-type vocabulary machine authority | `NEEDS VERIFICATION` |
| Package implementation | `EXPERIMENTAL; PYPROJECT 0.0.0` |
| Pipeline implementation | `PLACEHOLDER ENTRYPOINTS` |
| Pipeline specs | `EMPTY STAGE LISTS` |
| Policy completeness | `GREENFIELD / PROPOSED` |
| Schema completeness | `PROPOSED EMPTY-PROPERTIES SCAFFOLDS` |
| Validator executables | `NEEDS VERIFICATION` |
| Workflow enforcement | `TODO SCAFFOLD` |
| Tests/pass rates | `NEEDS VERIFICATION` |
| Source rights/endpoints/cadence | `NEEDS VERIFICATION` |
| MUKEY/COKEY/CHKEY rules | `NEEDS VERIFICATION` |
| Units/depth/method/QC profiles | `NEEDS VERIFICATION` |
| Moisture freshness/stale budgets | `NEEDS VERIFICATION` |
| Scale/resolution profiles | `NEEDS VERIFICATION` |
| Interpretation/advice profiles | `NEEDS VERIFICATION` |
| Private-land/private-sensor policy | `NEEDS VERIFICATION` |
| Public-safe transform profiles | `NEEDS VERIFICATION` |
| Secret/sensitive scanners | `NEEDS VERIFICATION` |
| Ownership/branch protection | `NEEDS VERIFICATION` |
| Runtime/release/publication | `UNKNOWN` |

[Back to top](#top)

---

## Safe language rules

| Avoid | Prefer |
|---|---|
| “The pipeline uses this config.” | “This file names an intended consumer; direct binding is `NEEDS VERIFICATION`.” |
| “Authoritative soil layer.” | “Source-role- and support-type-labeled product under a stated vintage and scope.” |
| “Current soil condition.” | “A cited observation/product with stated observed time, retrieval time, freshness, QC, depth, and support.” |
| “This grid is SSURGO truth.” | “A gridded derivative with stated source, resolution, method, and limitations.” |
| “This station represents the county.” | “A point/depth observation; representativeness is not implied.” |
| “This SMAP value is a station reading.” | “A satellite-grid observation at stated resolution/time/QC.” |
| “This soil is suitable.” | “An interpretation under a stated method, use, inputs, limitations, and evidence.” |
| “Erosion hazard.” | “Soil-side erosion interpretation; Hazards authority is separate.” |
| “HSG predicts flooding.” | “Hydrologic soil group is one classification input; flood truth belongs elsewhere.” |
| “This field/parcel has…” | “Public-safe generalized context, where policy/release permit; exact private context withheld.” |
| “Schema is active.” | “Opened schema is a `PROPOSED` scaffold with empty properties.” |
| “Validators enforce this.” | “Validator README lanes exist; executable behavior and CI binding remain `NEEDS VERIFICATION`.” |
| “CI validates Soil.” | “The inspected domain workflow currently runs TODO echo jobs.” |
| “catalog/domain/soil is the catalog.” | “It is a compatibility redirect; canonical catalog records belong under `data/catalog/domain/soil/`.” |

[Back to top](#top)

---

## Evidence ledger

| Evidence | State | Supports | Does not prove |
|---|---|---|---|
| Target README | prior blob `5b9b0c36…` | v0.1 boundary and rollback. | Consumers or payloads. |
| Parent config README | blob `2c5e8b70…`, v0.4 | No-secret/no-authority child contract. | Soil runtime behavior. |
| Bounded config search | README only | No indexed payload/direct consumer. | Exhaustive absence. |
| `docs/domains/soil/README.md` | blob `cf05c89d…` | Path exists. | Soil doctrine depth; it is a placeholder. |
| Soil architecture | blob `d984d8fc…` | Scope, objects, sources, support types, lifecycle, sensitivity. | Executable implementation. |
| Soil canonical paths | blob `89a0a07…` | Responsibility-root placement and path variance. | Accepted ADR resolution. |
| Package README / pyproject | blobs `b8112521…`, `5a4ddcd5…` | Intended helper boundary; package version `0.0.0`. | Working exports/tests. |
| Pipeline README | blob `388e5a14…` | Intended executable boundary/support invariant. | Implemented processing. |
| Pipeline entrypoints | placeholder comments | Inspected core entrypoints are greenfield placeholders. | All possible code elsewhere. |
| Pipeline specs | `stages: []` | Spec paths exist. | Stage wiring/execution. |
| Policy README/module | blobs `551e6768…`, `a23cc03e…` | Policy path and default-deny support intent. | Complete accepted policy/runtime enforcement. |
| Schema index | blob `da161213…` | Soil schema inventory/path maturity. | Production readiness. |
| SoilMapUnit schema | blob `4e94ee95…` | Proposed path/id/contract ref. | Meaningful fields or strict validation. |
| Soil moisture schema | blob `4d9f6b60…` | Proposed path/id/contract ref. | Meaningful fields or strict validation. |
| Validator index | blob `bceca437…` | Intended validator lanes/invariants. | Executable files, CI, pass rates. |
| Domain workflow | blob `b2cdd2d6…` | PR/push triggers and TODO jobs. | Substantive validation/proof/release. |
| Soil source registry README | blob `83942459…` | Source boundary and topology conflict. | Active/accepted descriptors. |
| Soil domain registry README | blob `18402f65…` | Domain-state registry boundary. | Emitted records/validators. |
| Catalog compatibility README | blob `5238fa28…` | Root catalog is redirect; canonical home is `data/catalog/domain/soil/`. | Migration completion or producer compliance. |

[Back to top](#top)

---

<details>
<summary><strong>Appendix A — no-loss preservation note</strong></summary>

v0.1 established the Soil config lane, documentation-only maturity, non-authoritative scope, no secrets/live bindings, support distinctions, private land/producer caution, and no source/lifecycle/release authority.

v0.2 preserves those controls and adds:

- pinned repository evidence;
- bounded config inventory;
- placeholder/scaffold maturity;
- segmented/flat schema-contract conflict;
- source-registry and catalog compatibility posture;
- detailed source-role and support-type anti-collapse;
- Soil object-family boundaries;
- survey identity and MUKEY/COKEY/CHKEY lineage;
- unit/depth/method/QC requirements;
- time/freshness/stale-state rules;
- scale/resolution/spatial-support rules;
- interpretation/no-advice safeguards;
- cross-domain and private-context controls;
- config classes and minimum file contract;
- explicit binding/no discovery/no implicit precedence;
- validation/review/failure/AI rules;
- migration/deactivation/correction/rollback;
- first-payload definition of done;
- verification backlog, safe language, and evidence ledger.

No v0.1 safeguard is intentionally weakened.

</details>

<details>
<summary><strong>Appendix B — documentation-only boundary</strong></summary>

This revision changes no:

- executable config payload;
- consumer or loader;
- source descriptor or activation decision;
- schema, contract, or policy;
- package/pipeline/validator/test/fixture/workflow code;
- lifecycle data;
- registry record;
- receipt, proof, catalog, triplet, graph, or published artifact;
- release, correction, withdrawal, or rollback object;
- public API, map, UI, export, Focus Mode, or AI behavior;
- source fetch, query, sensor subscription, raster build, interpretation, advice, or deployment.

Any future behavior change must be implemented and validated in its owning responsibility roots.

</details>

## Status summary

`configs/domains/soil/` is a README-only, non-secret, non-authoritative configuration-support lane. The surrounding repository contains rich Soil documentation and many implementation-shaped paths, but inspected package, pipeline, spec, policy, schema, validator, workflow, registry, and catalog surfaces remain draft, scaffolded, placeholder, conflicted, compatibility-only, or unverified. No direct config consumer is established. Future payloads require explicit binding, accepted source/role/support profiles, survey lineage, units/depth/method/QC, time/freshness/scale safeguards, privacy and cross-domain controls, validation, policy, review, release, correction, and rollback.

<p align="right"><a href="#top">Back to top</a></p>

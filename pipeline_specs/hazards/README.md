<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-hazards-readme
title: pipeline_specs/hazards/ — Governed Hazards Pipeline Specification Boundary
type: readme
version: v0.2
status: draft; repository-grounded; nine-placeholder-profiles; no-active-hazards-spec-established; life-safety-adjacent
owners: OWNER_TBD — Pipeline-spec steward · Hazards steward · Official-source/public-safety reviewer · Source/rights steward · Object-family stewards · Spatial/temporal/freshness steward · Model/method steward · Infrastructure-sensitivity reviewer · Consumer owner · Validation/evidence/policy/release stewards · Docs steward
created: 2026-06-13
updated: 2026-07-15
supersedes: v0.1
policy_label: public; pipeline-specs; hazards; declarative-only; not-for-life-safety; alert-authority-denied; official-source-referral; source-role-aware; object-family-aware; freshness-aware; expiry-aware; model-aware; regulatory-aware; infrastructure-sensitive; reconstruction-resistant; no-secrets; no-live-activation; no-direct-source-access; no-direct-lifecycle-write; no-release-authority
current_path: pipeline_specs/hazards/README.md
truth_posture: CONFIRMED target and prior blob, nine direct seven-line PROPOSED inventory placeholders, draft executable/configuration/contract/schema/source/policy/test/fixture/validator/receipt/proof/catalog/release/public documentation, empty PROPOSED source-authority register, fail-closed policy scaffolds, TODO-only Hazards CI, and placeholder CODEOWNERS / PROPOSED active-spec contract, finite statuses and outcomes, deterministic parser/consumer/activation, source/object/time/space/model/freshness/sensitivity/lifecycle/evidence/release gates, correction propagation, invalidation, and rollback / UNKNOWN accepted Hazards spec schema, parser, registry, scheduler, activation records, consumers, runtime, substantive CI, emitted receipts, proof closure, release integration, schedules, and public use / NEEDS VERIFICATION owners, exhaustive inventory, canonical source/schema/receipt/release topology, admitted sources, rights, roles, time/freshness/spatial/model profiles, official-source referral policy, infrastructure aggregation, fixtures, tests, validators, corrections, invalidation, and rollback execution
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 6006bcb2ce4b586e95d91d545b08b3a62c54ddf3
  prior_blob: 9799cbbb179adc1a91156c124c702e206acea06a
  direct_lane_files:
    - pipeline_specs/hazards/README.md
    - pipeline_specs/hazards/fema_nfhl.yaml
    - pipeline_specs/hazards/fema_openfema.yaml
    - pipeline_specs/hazards/nasa_firms.yaml
    - pipeline_specs/hazards/noaa_hms_smoke.yaml
    - pipeline_specs/hazards/noaa_storm_events.yaml
    - pipeline_specs/hazards/nws_alerts_context.yaml
    - pipeline_specs/hazards/usgs_earthquake.yaml
    - pipeline_specs/hazards/drought_monitor.yaml
    - pipeline_specs/hazards/exposure_resilience_rollup.yaml
  direct_lane_posture: nine flat YAML inventory placeholders; no active specification established
  workflow_posture: domain-hazards is pull-request-triggered TODO scaffolding
related:
  - ../README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/domains/hazards/README.md
  - ../../docs/domains/hazards/LIFE_SAFETY_BOUNDARY.md
  - ../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md
  - ../../docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md
  - ../../pipelines/domains/hazards/README.md
  - ../../configs/domains/hazards/README.md
  - ../../contracts/domains/hazards/README.md
  - ../../schemas/contracts/v1/domains/hazards/README.md
  - ../../data/registry/sources/hazards/README.md
  - ../../data/receipts/hazards/README.md
  - ../../data/proofs/hazards/README.md
  - ../../data/catalog/domain/hazards/README.md
  - ../../data/published/layers/hazards/README.md
  - ../../tests/domains/hazards/README.md
  - ../../fixtures/domains/hazards/README.md
  - ../../tools/validators/domains/hazards/README.md
  - ../../policy/domains/hazards/README.md
  - ../../release/candidates/hazards/README.md
  - ../../release/manifests/hazards-r0002.yaml
  - ../../.github/workflows/domain-hazards.yml
  - ../../.github/CODEOWNERS
notes:
  - "v0.2 replaces the speculative tree with the verified nine-placeholder inventory."
  - "Tests, fixtures, receipts, proofs, catalog, release, and public artifacts remain in their verified responsibility roots."
  - "KFM Hazards is permanently outside emergency alerting, incident command, warning issuance, evacuation, routing, medical, shelter, and other life-safety instruction authority."
  - "No source, profile, parser, consumer, schedule, pipeline, policy exception, lifecycle object, receipt, proof, release, runtime, or public artifact is activated or modified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Hazards Pipeline Specification Boundary

`pipeline_specs/hazards/`

> Declarative run-intent boundary for Hazards processing. A reviewed active specification may state **what** a verified consumer should process and which source, role, time, freshness, spatial, model, evidence, sensitivity, policy, review, correction, and release gates apply. It does not execute a pipeline, admit a source, issue or modify an alert, decide current operational truth, provide life-safety instructions, create evidence, or authorize publication.

![status](https://img.shields.io/badge/status-draft-blue)
![version](https://img.shields.io/badge/version-v0.2-informational)
![inventory](https://img.shields.io/badge/inventory-9__placeholders-lightgrey)
![life safety](https://img.shields.io/badge/life__safety-not__an__alert__system-critical)
![activation](https://img.shields.io/badge/activation-separate-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-0b7285)

**Quick links:** [Status](#current-status) · [Inventory](#verified-inventory) · [Placement](#repository-fit) · [Boundaries](#authority-and-anti-collapse) · [Profiles](#profile-family-boundaries) · [Contract](#minimum-active-specification-contract) · [Time](#time-freshness-and-correction) · [Safety](#not-for-life-safety-and-official-source-referral) · [Sensitivity](#sensitivity-and-reconstruction-risk) · [Lifecycle](#lifecycle-evidence-and-release) · [Example](#illustrative-inactive-profile) · [Validation](#validation-and-definition-of-done) · [Rollback](#rollback-correction-and-deactivation) · [Backlog](#open-verification-register) · [Evidence](#evidence-ledger)

> [!IMPORTANT]
> **Evidence snapshot:** `main@6006bcb2ce4b586e95d91d545b08b3a62c54ddf3`  
> **Prior target blob:** `9799cbbb179adc1a91156c124c702e206acea06a`  
> **Direct lane:** this README plus nine seven-line YAML placeholders  
> **Active specifications:** none established  
> **Source-authority register:** `PROPOSED`, with `entries: []`  
> **Activation:** file presence, merge state, syntax validity, schedule text, policy default denial, release-placeholder presence, rendering, or dry-run success activates nothing

> [!CAUTION]
> **KFM is not an emergency alert system.** It may preserve released, source-attributed Hazards context for planning, history, resilience, and explanation. It may not issue, rank, suppress, extend, cancel, replace, notify from, or operationalize warnings, watches, advisories, evacuations, shelter instructions, route decisions, medical guidance, fire-response instructions, or incident-command actions.

---

<a id="current-status"></a>

## Current status

| Surface | Evidence | Status | Safe conclusion |
|---|---|---:|---|
| Nine direct YAML profiles | Each contains only `status`, `source_doc`, `path`, and a placeholder note | **CONFIRMED placeholders** | Inventory slots only |
| Spec schema/parser/registry | No accepted binding surfaced | **UNKNOWN** | No canonical parse or discovery behavior |
| Scheduler/activation | No verified records surfaced | **UNKNOWN** | Assume inactive |
| Executable pipeline | Detailed draft README | **CONFIRMED docs** | Runtime and consumer binding unverified |
| Configuration | README-only bounded inventory | **CONFIRMED docs** | No polling, precedence, notification, or runtime binding |
| Contracts | Draft semantic surface | **CONFIRMED drafts** | Meaning is documented; enforcement is not proven |
| Schemas | Conflicted homes and permissive `PROPOSED` scaffolds | **CONFIRMED partial inventory** | No accepted profile schema or field-complete coverage |
| Source registry | Subtype-first and domain-first lanes | **CONFLICTED** | No duplicate authority; no admitted source established |
| Policy | Generic README, referrals placeholder, five default-deny Rego scaffolds | **CONFIRMED scaffolds** | Conservative default, not field-level enforcement |
| Tests/fixtures | Documentation-rich parent and child READMEs | **CONFIRMED docs** | Payloads, executable tests, consumers, and pass rates unverified |
| Validators | Parent index only | **CONFIRMED index-only** | No executable Hazards child validator established |
| Receipts/proofs/catalog | Draft parent guides | **CONFIRMED docs** | No emitted chain or closure established |
| Release | Draft candidate guide and `hazards-r0002.yaml` placeholder | **CONFIRMED placeholder** | No release authority |
| Published layers | Draft parent with `flood_event/` and `nfhl/` README children | **CONFIRMED docs** | Released bytes and manifest linkage unknown |
| CI | Three `echo TODO` jobs | **CONFIRMED scaffold-only** | Green status is not Hazards validation |
| CODEOWNERS | Generic placeholder | **CONFIRMED placeholder** | No Hazards-specific review enforcement |
| Runtime/public use | No activation or deployment evidence surfaced | **UNKNOWN** | Inactive and non-public by default |

The lane is a documentation and inventory boundary. Active behavior remains unproved.

[Back to top](#top)

---

<a id="verified-inventory"></a>

## Verified inventory

| File | Intended family | Current posture |
|---|---|---|
| `fema_nfhl.yaml` | FEMA regulatory flood context | **INACTIVE / PROPOSED placeholder** |
| `fema_openfema.yaml` | FEMA administrative/regulatory context | **INACTIVE / PROPOSED placeholder** |
| `nasa_firms.yaml` | Satellite fire/thermal detections | **INACTIVE / PROPOSED placeholder** |
| `noaa_hms_smoke.yaml` | Fire/smoke analyst, observed, candidate, or modeled context | **INACTIVE / PROPOSED placeholder** |
| `noaa_storm_events.yaml` | Historical storm-event records | **INACTIVE / PROPOSED placeholder** |
| `nws_alerts_context.yaml` | Warning/watch/advisory context | **INACTIVE / PROPOSED placeholder** |
| `usgs_earthquake.yaml` | Earthquake-event observations | **INACTIVE / PROPOSED placeholder** |
| `drought_monitor.yaml` | Drought modeled/aggregate context | **INACTIVE / PROPOSED placeholder** |
| `exposure_resilience_rollup.yaml` | Derived exposure/resilience summaries | **INACTIVE / PROPOSED placeholder** |

None defines a `spec_id`, schema version, parser, consumer, source descriptor, source role, cadence, lifecycle gate, time contract, evidence requirement, activation decision, correction path, or rollback target.

Exact filename searches surfaced placeholders and planning, connector, contract, or tool documentation—not verified parser, scheduler, activation, consumer, or spec-specific test bindings. This is a bounded indexed-search conclusion, not an exhaustive absence claim.

[Back to top](#top)

---

<a id="repository-fit"></a>

## Repository fit

| Responsibility | Home | Boundary |
|---|---|---|
| Declarative Hazards run intent | `pipeline_specs/hazards/` | This lane: the **what** |
| Executable behavior | `pipelines/domains/hazards/` | The **how**; not source or release authority |
| Configuration support | `configs/domains/hazards/` | No secrets or hidden authority |
| Human doctrine | `docs/domains/hazards/` | Scope, source-role, life-safety, publication, and UI doctrine |
| Semantic meaning | `contracts/domains/hazards/` | Object meaning only |
| Machine shape | `schemas/contracts/v1/domains/hazards/` or ADR-resolved home | Current path conflict remains visible |
| Source admission | `data/registry/sources/hazards/` or topology-resolved registry | Experimental; no source activated |
| Policy | `policy/domains/hazards/` and accepted shared policy roots | Admissibility, not profile authority |
| Tests and fixtures | `tests/domains/hazards/`, `fixtures/domains/hazards/` | Synthetic enforceability support |
| Validators | `tools/validators/domains/hazards/` and accepted shared validators | Index-only at current parent |
| Lifecycle data | `data/raw|work|quarantine|processed|catalog|triplets|published/.../hazards/` | Never beside specs |
| Receipts and proofs | `data/receipts/hazards/`, `data/proofs/hazards/` | Process memory and evidence closure remain separate |
| Catalog | `data/catalog/domain/hazards/` and accepted projections | Discovery, not release |
| Release | `release/` | Manifest, decision, correction, and rollback authority |
| Public artifacts | `data/published/layers/hazards/` | Released safe bytes only |
| Public clients | Governed API and released artifacts | No direct access to internal profiles or stores |

### Open placement conflicts

- `schemas/contracts/v1/domains/hazards/` versus `schemas/contracts/v1/hazards/`;
- `data/registry/sources/hazards/` versus `data/registry/hazards/sources/`;
- source-family connector aliases;
- domain-local trust schemas versus common/cross-domain homes;
- singular/plural release-manifest conventions;
- flat source profiles versus future child profile lanes;
- planned receipt subtypes versus the verified Hazards receipt parent.

This README documents those conflicts; it does not resolve or migrate them.

[Back to top](#top)

---

<a id="authority-and-anti-collapse"></a>

## Authority and anti-collapse

A reviewed active profile may declare an eligible consumer, admitted source refs, object family, allowed lifecycle inputs/candidate outputs, required gates, and finite failure outcomes.

It cannot decide that a source is admitted, official, current, complete, rights-cleared, or authoritative; that a warning is a KFM alert; that expired context is current; that regulatory flood context is observed inundation; that a satellite detection is a confirmed incident; that a model or aggregate is an observation; that exact infrastructure or private detail is safe; or that evidence, policy, review, catalog, or release closure exists.

```text
spec file -> executable pipeline                 FORBIDDEN
parse success -> active specification            FORBIDDEN
profile merge -> source activation               FORBIDDEN
schedule -> freshness proof                      FORBIDDEN
warning context -> KFM alert                     FORBIDDEN
regulatory area -> observed event                FORBIDDEN
detection -> confirmed incident                  FORBIDDEN
model / aggregate -> observation                 FORBIDDEN
successful run -> EvidenceBundle                 FORBIDDEN
catalog record -> release approval               FORBIDDEN
generated summary -> evidence or official advice FORBIDDEN
```

Neighboring domains retain truth ownership: Hydrology owns water observations/forecasts; Atmosphere/Air owns atmospheric observations and health-index context; Roads/Rail/Trade owns network identity; Settlements/Infrastructure owns facility identity; Geology, Soil, Agriculture, Habitat, Archaeology, and People/Land retain their own truth and sensitivity controls.

[Back to top](#top)

---

<a id="profile-family-boundaries"></a>

## Profile-family boundaries

### FEMA NFHL

Regulatory flood-hazard context only. Preserve effective dates, map/version identity, jurisdiction, scale, and revision lineage. Do not present as observed inundation, forecast extent, current condition, structural safety, insurance/permitting advice, or Hydrology measurement truth.

### FEMA OpenFEMA

Preserve administrative, regulatory, declaration, program, claim, or aggregate character by product. A declaration is not an observed footprint or damage measurement. Do not infer eligibility, entitlement, loss, legal status, or current emergency conditions.

### NASA FIRMS

Preserve sensor/product, acquisition time, confidence, processing, and candidate/detection posture. A thermal anomaly is not automatically a confirmed fire, perimeter, containment state, evacuation need, or response instruction.

### NOAA HMS smoke

Preserve analyst/observation/model/candidate and temporal-window distinctions. Smoke context does not establish ground-level PM2.5, AQI, exposure, health impact, visibility safety, or medical guidance. Atmosphere/Air retains that truth.

### NOAA/NCEI Storm Events

Historical event and administrative/observed context. Preserve event identity, source vintage, event times, revisions, and narrative limits. Historical records are not current warnings, forecasts, road conditions, or emergency instructions.

### NWS alerts context

Carry issuing authority, product identity, issue/onset/effective/expiry/cancellation/supersession/retrieval/release state, a permanent not-for-life-safety disclaimer, and official-source referral. Expired, cancelled, superseded, stale, or unverifiable context must not appear current. KFM may not issue, alter, prioritize, suppress, extend, cancel, replace, or notify from an official product.

### USGS earthquake

Preserve event ID, origin time, revisions, magnitude type, depth/location uncertainty, and correction lineage. An event record is not damage truth, building/road/utility safety, inspection advice, or emergency guidance.

### Drought indicators

Preserve modeled/aggregate character, classification/version, publication period, support, and cadence. A regional class is not parcel, field, crop, soil, water-supply, livestock, loss, or management truth.

### Exposure and resilience rollup

Derived/aggregate planning context only. Preserve analysis unit, source roles, period, method, uncertainty, coverage, missingness, and aggregation limits. Do not expose exact infrastructure, emergency resources, people, households, parcels, vulnerable sites, small cells, or reconstruction-enabling joins. Do not present as observed impact, loss, safety, priority, funding, or resilience guarantee.

[Back to top](#top)

---

<a id="minimum-active-specification-contract"></a>

## Minimum active-specification contract

A future active profile must provide or reference:

1. **Identity:** immutable `spec_id`, version, digest, owner, review state, supersession, correction, rollback.
2. **Shape:** accepted spec schema ID/version and deterministic unknown-key behavior.
3. **Binding:** accepted parser, one verified consumer, supported versions, discovery, precedence, duplicate handling, reload policy.
4. **Activation:** separate reviewed activation decision naming exact profile digest, scope, environment, consumer, effective time, reason, and rollback target.
5. **Sources:** admitted `SourceDescriptor` and source-activation refs; rights, terms, attribution, access, cadence, source head, role, and authority limits.
6. **Objects:** explicit Hazards object/knowledge-character family and cross-domain ownership.
7. **Time:** relevant event, issue, onset, effective, valid, expiry, cancellation, supersession, retrieval, processing, release, correction, and stale-state semantics.
8. **Space:** source/analysis/publication CRS, support type, extent, scale, resolution, topology, uncertainty, precision, and public representation.
9. **Models/detections/aggregates:** method/sensor, inputs, version, confidence, disposition, uncertainty, coverage, missingness, aggregation unit, denominator, and interpretation limits.
10. **Life safety:** permanent `not_for_life_safety`, official-source referral, and deterministic denial of protective-action guidance.
11. **Sensitivity:** infrastructure, people, parcels, cultural/sensitive sites, small cells, joins, differencing, mosaics, and reconstruction-risk controls.
12. **Lifecycle:** allowed inputs and candidate outputs without implying promotion.
13. **Evidence and governance:** validation, receipts, EvidenceRef/EvidenceBundle, proof, catalog, policy, review, release, correction, withdrawal, and rollback requirements.
14. **Security:** no secrets, private endpoints, exact sensitive coordinates, operational redaction parameters, or unsafe logs/telemetry.
15. **Invalidation:** affected tiles, caches, downloads, search, graph, indexes, exports, screenshots, reports, embeddings, and generated summaries.

Missing material fails closed with `HOLD`, `DENY`, `ABSTAIN`, `QUARANTINE`, or `ERROR`; it does not become an implicit default.

### Proposed statuses

`INVENTORY_PLACEHOLDER`, `DRAFT`, `VALIDATED_INACTIVE`, `REVIEW_REQUIRED`, `ACTIVE`, `SUSPENDED`, `SUPERSEDED`, `RETIRED`, `REJECTED`.

Current YAMLs remain `INVENTORY_PLACEHOLDER` regardless of `status: PROPOSED` inside them.

### Proposed run outcomes

`NO_OP`, `CANDIDATE_CREATED`, `QUARANTINED`, `HOLD`, `STALE_CONTEXT`, `EXPIRED_CONTEXT`, `CANCELLED_OR_SUPERSEDED`, `DENY`, `ABSTAIN`, `REVIEW_REQUIRED`, `ERROR`, `CORRECTION_REQUIRED`, `WITHDRAWAL_REQUIRED`, `ROLLBACK_REQUIRED`.

[Back to top](#top)

---

<a id="time-freshness-and-correction"></a>

## Time, freshness, and correction

Do not collapse event/observation, issue/publication, onset/effective, valid-through/expiry, cancellation/supersession, retrieval, processing, release, or correction time.

Required behaviors:

- stale, expired, cancelled, superseded, or unverifiable operational context cannot display as current;
- historical records stay historical even when retrieved recently;
- file modification time is not upstream freshness;
- outage or cadence failure produces a finite outcome;
- no profile extends or overrides an issuing authority's validity window;
- revisions and corrections propagate to catalogs, public artifacts, tiles, caches, downloads, search, graph, indexes, reports, and generated summaries.

[Back to top](#top)

---

<a id="not-for-life-safety-and-official-source-referral"></a>

## Not for life safety and official-source referral

```text
KFM context != official alert != protective-action instruction
```

Operational-context candidates must preserve issuing authority, source product, time state, permanent disclaimer, reviewed official-source referral, and deterministic `DENY`, `ABSTAIN`, `ERROR`, or historical-only handling when current status cannot be verified.

Outside KFM authority:

- emergency alert issuance or delivery;
- prioritizing, suppressing, extending, cancelling, or replacing official products;
- evacuation, shelter, travel, routing, re-entry, medical, fire-response, utility, water-safety, or incident-command instructions;
- declaring a road, building, facility, parcel, community, or person safe or unsafe for current action;
- replacing direct official-source access for urgent decisions.

[Back to top](#top)

---

<a id="sensitivity-and-reconstruction-risk"></a>

## Sensitivity and reconstruction risk

Fail closed when a profile or derivative could reveal or reconstruct:

- critical infrastructure, utilities, communications, emergency resources, response staging, or security-relevant access;
- people, households, addresses, parcels, medical/vulnerability attributes, or identifiable small cells;
- culturally sensitive, archaeological, cave, sacred, burial, or sovereign-controlled places;
- protected Fauna/Flora, Habitat, Agriculture, or People/Land detail through joins;
- hidden geometry through centroids, bounds, tile footprints, multiple zooms, search facets, graph links, differencing, mosaics, embeddings, or exports.

Public artifacts must be safe as bytes, not merely hidden by a style. Specs must not contain operational thresholds, redaction seeds, offsets, exact suppression parameters, credentials, protected query material, or private endpoints.

[Back to top](#top)

---

<a id="lifecycle-evidence-and-release"></a>

## Lifecycle, evidence, and release

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A profile may declare candidate transitions. It cannot perform or approve them by existing.

```text
receipt != proof != catalog != policy != review != release != publication
```

Current repository posture:

- `data/receipts/hazards/` is a draft parent with no confirmed child/emitted receipts;
- `data/proofs/hazards/` documents proposed proof families, not emitted closure;
- `data/catalog/domain/hazards/` documents the catalog boundary, not closure;
- `release/candidates/hazards/` is pre-release guidance;
- `release/manifests/hazards-r0002.yaml` is a placeholder, not release authority;
- `data/published/layers/hazards/` documents publication boundaries, not verified released bytes.

Public clients consume governed APIs and released artifacts only. They do not consume profiles, registries, lifecycle candidates, receipts, proofs, or release candidates directly.

[Back to top](#top)

---

<a id="illustrative-inactive-profile"></a>

## Illustrative inactive profile

Noncanonical and deliberately inactive:

```yaml
schema_version: PROPOSED-kfm.pipeline_spec.hazards.v1
spec_id: hazards.example.context-only
version: 0.0.0-example
status: DRAFT
active: false
binding:
  parser_id: NEEDS_VERIFICATION
  consumer_id: NEEDS_VERIFICATION
  activation_ref: null
sources:
  source_descriptor_refs: []
  source_activation_refs: []
scope:
  object_family: WarningContext
  knowledge_character: administrative
time:
  issue_time_required: true
  expiry_time_required: true
  retrieval_time_required: true
safety:
  not_for_life_safety: true
  official_source_referral_required: true
  protective_action_guidance: DENY
lifecycle:
  allowed_input_states: [RAW, WORK, QUARANTINE]
  candidate_output_state: PROCESSED
  publication_authority: false
requirements:
  evidence_ref_required: true
  policy_decision_required: true
  validation_report_required: true
  correction_path_required: true
  rollback_target_required: true
on_unresolved:
  outcome: ABSTAIN
```

Copying this example does not activate it.

[Back to top](#top)

---

<a id="validation-and-definition-of-done"></a>

## Validation and definition of done

Future executable validation must cover shape, immutable identity, parser/consumer binding, activation, source admission/roles/rights, object-family separation, time/freshness/expiry, spatial support, model/detection/aggregate limits, life-safety/referral, sensitivity/reconstruction risk, lifecycle, evidence, receipts/proof/catalog, policy/review/release, correction/rollback, and security.

Minimum negative scenarios:

- placeholder rejected as active;
- missing/duplicate identity or incompatible parser/consumer;
- absent source descriptor, activation, role, rights, or cadence;
- expired/cancelled/superseded context presented as current;
- missing disclaimer or official referral;
- historical event presented as live status;
- NFHL presented as observed flood;
- FIRMS/HMS detection presented as confirmed incident or health guidance;
- drought aggregate presented as parcel/crop/water truth;
- exposure rollup leaking infrastructure, people, parcels, or small cells;
- missing evidence, policy, review, release, correction, or rollback;
- successful run treated as release approval;
- stale public derivatives remaining resolvable after correction;
- watcher/refresh tooling attempting admission, activation, notification, or publication.

A profile is not done until it has accepted shape, parser, consumer, discovery, activation, admitted sources, rights, roles, object contract/schema, time/spatial/model/sensitivity controls, deterministic fixtures/tests, meaningful CI, receipts/evidence/proof/catalog requirements, policy/review/release support, public-interface controls, correction/invalidation, and a tested rollback path.

The current `domain-hazards` workflow proves none of this; its jobs are TODO echoes.

[Back to top](#top)

---

<a id="rollback-correction-and-deactivation"></a>

## Rollback, correction, and deactivation

Documentation rollback: close/abandon the branch before merge, or use a transparent revert after merge. Do not rewrite shared history.

Future active-profile rollback must:

1. suspend discovery, polling, scheduling, and consumer loading;
2. revoke/supersede activation;
3. preserve exact profile, parser, consumer, source, source-head, run, receipt, evidence, policy, review, catalog, release, and artifact lineage;
4. hold pending candidates and block new publication;
5. inventory affected processed records, catalogs, triplets, layers, tiles, caches, downloads, search, graphs, indexes, exports, reports, screenshots, embeddings, and generated summaries;
6. issue correction, withdrawal, supersession, or rollback records;
7. restore a reviewed prior state or remain disabled;
8. re-evaluate source role, rights, time, freshness, geometry, model, sensitivity, evidence, policy, and release state;
9. rerun deterministic validation and proof closure;
10. verify withdrawn/unsafe artifacts are no longer publicly resolvable;
11. preserve historical context and official-source referral without misrepresenting current state.

[Back to top](#top)

---

<a id="open-verification-register"></a>

## Open verification register

| ID | Verification | Status |
|---|---|---|
| `HAZ-SPEC-001` | Owners and reviewer routing | NEEDS VERIFICATION |
| `HAZ-SPEC-002` | Exhaustive profile inventory | NEEDS VERIFICATION |
| `HAZ-SPEC-003` | Canonical spec schema, parser, and registry | UNKNOWN |
| `HAZ-SPEC-004` | Discovery, precedence, duplicate, reload, scheduler, activation | UNKNOWN |
| `HAZ-SPEC-005` | Executable consumers by profile family | UNKNOWN |
| `HAZ-SPEC-006` | Source-registry topology and admitted descriptors | CONFLICTED / UNKNOWN |
| `HAZ-SPEC-007` | Rights, terms, attribution, redistribution, cadence | NEEDS VERIFICATION |
| `HAZ-SPEC-008` | Canonical roles and knowledge-character mapping | NEEDS VERIFICATION |
| `HAZ-SPEC-009` | Contract/schema topology and field-complete shapes | CONFLICTED / NEEDS VERIFICATION |
| `HAZ-SPEC-010` | Time, freshness, expiry, cancellation, supersession profiles | NEEDS VERIFICATION |
| `HAZ-SPEC-011` | Official-source referral and permanent life-safety denial | NEEDS VERIFICATION |
| `HAZ-SPEC-012` | Spatial, model, detection, aggregate, uncertainty profiles | NEEDS VERIFICATION |
| `HAZ-SPEC-013` | Infrastructure/private/cultural/small-cell/reconstruction policy | NEEDS VERIFICATION |
| `HAZ-SPEC-014` | Fixture payloads, executable tests, pass rates, validators | UNKNOWN |
| `HAZ-SPEC-015` | Receipt layout and emitted instances | NEEDS VERIFICATION |
| `HAZ-SPEC-016` | Proof schemas/validators and emitted closure | NEEDS VERIFICATION |
| `HAZ-SPEC-017` | Catalog/STAC/DCAT/PROV closure | NEEDS VERIFICATION |
| `HAZ-SPEC-018` | Release-manifest path/schema and review integration | CONFLICTED / UNKNOWN |
| `HAZ-SPEC-019` | Published bytes, digests, governed API behavior | UNKNOWN |
| `HAZ-SPEC-020` | Correction, withdrawal, invalidation, rollback drill | NEEDS VERIFICATION |
| `HAZ-SPEC-021` | Hazards CODEOWNERS and substantive required CI | UNKNOWN |
| `HAZ-SPEC-022` | Connector alias consolidation | NEEDS VERIFICATION |
| `HAZ-SPEC-023` | Evidence-safe Focus Mode and generated language | NEEDS VERIFICATION |

[Back to top](#top)

---

<a id="evidence-ledger"></a>

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| `main@6006bcb2ce4b586e95d91d545b08b3a62c54ddf3` | CONFIRMED snapshot | Evidence boundary | Later state may change |
| Prior README | CONFIRMED v0.1 | Existing boundary and stale tree | No implementation proof |
| Nine YAMLs | CONFIRMED | Direct inventory and placeholder shape | No active semantics |
| Exact profile searches | CONFIRMED bounded | No consumer/activation binding surfaced | Not exhaustive absence |
| Hazards pipeline/config/contracts/schema docs | CONFIRMED drafts | Responsibility and intended controls | Runtime/field enforcement unverified |
| Source registry + empty authority register | CONFIRMED | Admission boundary and no activation | Registry topology conflicted |
| Hazards policy scaffolds | CONFIRMED | Default denial and intended referral/freshness surfaces | No complete policy runtime |
| Test/fixture/validator READMEs | CONFIRMED docs | Intended enforceability families | Executables/payloads/pass rates unverified |
| Receipt/proof/catalog/release/public READMEs | CONFIRMED docs | Trust-family separation | Emitted closure/released bytes unknown |
| Hazards release placeholder | CONFIRMED placeholder | Planned manifest slot | No release |
| `domain-hazards` workflow | CONFIRMED TODO-only | Trigger and job names | No substantive enforcement |
| CODEOWNERS | CONFIRMED placeholder | Generic ownership | No Hazards-specific rule |
| Directory Rules v1.4 | CONFIRMED doctrine | Responsibility roots and lifecycle | Does not activate files |

This is a repository-grounded documentation update, not runtime proof.

[Back to top](#top)

---

## Maintenance checklist

- [ ] Re-pin the evidence snapshot and inventory every direct profile.
- [ ] Search exact profile names for parsers, consumers, activation, tests, and schedules.
- [ ] Recheck source registry, rights, roles, and source activation.
- [ ] Recheck contracts, schemas, policy, tests, fixtures, validators, and CI steps.
- [ ] Recheck receipts, proofs, catalog, release, published artifacts, and governed routes.
- [ ] Recheck official-source referral, freshness, life-safety denial, and reconstruction risk.
- [ ] Recheck correction, invalidation, withdrawal, and rollback.
- [ ] Emit generated provenance for AI-authored changes.
- [ ] Preserve truth labels and abstain from unverified implementation claims.

---

<p align="right"><a href="#top">Back to top</a></p>

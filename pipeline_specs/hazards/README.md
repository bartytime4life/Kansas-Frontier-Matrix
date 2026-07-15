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
truth_posture: CONFIRMED current target and prior blob, parent pipeline-spec contract, direct Hazards lane containing this README and nine seven-line PROPOSED inventory placeholders, draft executable Hazards pipeline documentation, README-only Hazards config lane, draft semantic contracts, broad but stale schema index with concrete permissive PROPOSED scaffolds and a /domains/hazards/ versus /hazards/ placement conflict, subtype-first/domain-first source-registry topology conflict, empty PROPOSED source-authority register, generic Hazards policy README plus five six-line default-deny Rego scaffolds and one referrals placeholder, documentation-rich tests and fixtures with executable payloads and pass rates unverified, index-only Hazards validator lane, Hazards receipt parent with no child receipt lane confirmed, draft proof/catalog/release-candidate/published-layer documentation, a PROPOSED Hazards release-manifest placeholder, TODO-only domain-hazards workflow, and placeholder CODEOWNERS / PROPOSED minimum active-spec contract, finite status and outcome vocabularies, deterministic parser and consumer binding, source/object/time/space/model/freshness/sensitivity/lifecycle/evidence/release gates, activation/deactivation discipline, validation matrix, correction propagation, and rollback requirements / UNKNOWN accepted Hazards pipeline-spec schema, parser, registry, discovery, scheduler, activation records, executable consumers, runtime behavior, substantive CI enforcement, emitted receipts, proof closure, release-manifest integration, deployed schedules, and public use / NEEDS VERIFICATION owners, exhaustive recursive inventory, canonical source-registry, contract/schema, receipt, and release topology, admitted SourceDescriptors, current rights and terms, object-family schemas, source-role mapping, temporal/freshness/spatial/model profiles, official-source referral policy, infrastructure aggregation rules, fixture payloads, executable tests, validator wiring, correction propagation, derived-output invalidation, and rollback execution
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
  - ./fema_nfhl.yaml
  - ./fema_openfema.yaml
  - ./nasa_firms.yaml
  - ./noaa_hms_smoke.yaml
  - ./noaa_storm_events.yaml
  - ./nws_alerts_context.yaml
  - ./usgs_earthquake.yaml
  - ./drought_monitor.yaml
  - ./exposure_resilience_rollup.yaml
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/domains/hazards/README.md
  - ../../docs/domains/hazards/MISSING_OR_PLANNED_FILES.md
  - ../../docs/domains/hazards/LIFE_SAFETY_BOUNDARY.md
  - ../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md
  - ../../docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md
  - ../../pipelines/domains/hazards/README.md
  - ../../configs/domains/hazards/README.md
  - ../../contracts/domains/hazards/README.md
  - ../../schemas/contracts/v1/domains/hazards/README.md
  - ../../schemas/contracts/v1/hazards/README.md
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
  - "v0.2 replaces the planning-only proposed tree with commit-pinned repository evidence and classifies all nine YAMLs as inactive inventory placeholders."
  - "The verified Hazards test and fixture parents are tests/domains/hazards/ and fixtures/domains/hazards/. The previously referenced tests/pipeline_specs/hazards/ and fixtures/pipeline_specs/hazards/ paths are not treated as current facts."
  - "The verified Hazards receipt and proof parents are data/receipts/hazards/ and data/proofs/hazards/. The previously referenced data/receipts/pipeline/hazards/ and data/proofs/evidence_bundle/ paths are not treated as Hazards parent authorities."
  - "KFM Hazards remains permanently outside emergency alerting, incident command, warning issuance, evacuation, routing, medical, shelter, or other life-safety instruction authority."
  - "No executable specification, source record, connector, pipeline, config payload, schema, contract, policy rule, fixture, test, validator, workflow, lifecycle object, receipt instance, proof, catalog object, release object, runtime behavior, or public artifact is created or modified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Hazards Pipeline Specification Boundary

`pipeline_specs/hazards/`

> Declarative run-intent boundary for Hazards processing. A reviewed active specification may state **what** a verified consumer should process, against which admitted sources, for which Hazards object or knowledge-character family, under which source-role, rights, time, freshness, expiry, spatial-support, model, evidence, sensitivity, policy, receipt, review, correction, and release gates. It does not execute a pipeline, admit a source, issue or alter an alert, decide current operational truth, provide life-safety instructions, create evidence, or authorize publication.

![status](https://img.shields.io/badge/status-draft-blue)
![version](https://img.shields.io/badge/version-v0.2-informational)
![authority](https://img.shields.io/badge/authority-declarative__spec-green)
![inventory](https://img.shields.io/badge/inventory-9__placeholders-lightgrey)
![life safety](https://img.shields.io/badge/life__safety-not__an__alert__system-critical)
![activation](https://img.shields.io/badge/activation-separate-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-0b7285)

**Quick links:** [Purpose](#purpose) · [Status](#current-status) · [Inventory](#current-inspected-inventory) · [Placement](#repository-fit) · [Authority](#authority-and-anti-collapse) · [Families](#profile-family-boundaries) · [Contract](#minimum-active-specification-contract) · [Activation](#status-activation-discovery-and-precedence) · [Sources](#sources-rights-and-source-roles) · [Objects](#object-family-and-knowledge-character-boundaries) · [Time](#time-freshness-expiry-and-correction) · [Space](#spatial-support-scale-crs-and-public-representation) · [Models](#models-detections-aggregates-and-uncertainty) · [Safety](#not-for-life-safety-and-official-source-referral) · [Sensitivity](#sensitivity-infrastructure-and-reconstruction-risk) · [Lifecycle](#lifecycle-gates-and-finite-outcomes) · [Evidence](#evidence-receipts-proof-catalog-and-release) · [Example](#illustrative-inactive-profile) · [Validation](#validation-and-enforceability) · [Done](#definition-of-done-for-an-active-specification) · [Rollback](#rollback-correction-and-deactivation) · [Backlog](#open-verification-register) · [Ledger](#evidence-ledger)

> [!IMPORTANT]
> **Evidence snapshot:** `main@6006bcb2ce4b586e95d91d545b08b3a62c54ddf3`  
> **Target blob before this revision:** `9799cbbb179adc1a91156c124c702e206acea06a`  
> **Direct-lane result:** this README plus nine flat YAML placeholders  
> **Active specifications:** none established  
> **Source-authority register:** `PROPOSED`, with an empty `entries` list  
> **Activation:** path presence, filename, merge state, YAML validity, schedule text, schema acceptance, fixture prose, policy default denial, release-manifest placeholder presence, map rendering, or a successful dry run activates nothing

> [!CAUTION]
> **KFM is not an emergency alert system.** A valid Hazards specification cannot issue, synthesize, rank, suppress, extend, cancel, replace, or operationalize warnings, watches, advisories, evacuations, shelter instructions, route-safety decisions, medical guidance, fire-response instructions, or incident-command actions. Operational products may be represented only as bounded, source-attributed context with visible time state and referral to appropriate official authorities.

---

<a id="purpose"></a>

## Purpose

This lane may eventually hold small, reviewed, deterministic declarative profiles that bind:

- stable specification identity, immutable version, digest, owner, status, and supersession lineage;
- one accepted parser and one verified executable consumer;
- explicit discovery, precedence, duplicate-handling, activation, deactivation, and rollback rules;
- admitted `SourceDescriptor` references and canonical source roles;
- rights, license, attribution, redistribution, access, cadence, and authority limits;
- Hazards object-family and knowledge-character boundaries;
- event, observation, issue, onset, effective, valid, expiry, cancellation, supersession, retrieval, processing, release, correction, and stale-state times;
- spatial support, CRS, scale, resolution, topology, precision, uncertainty, and public-safe representation;
- model, detection, aggregate, disposition, confidence, and uncertainty posture;
- input and output lifecycle states;
- official-source referral, permanent not-for-life-safety, infrastructure-sensitivity, and reconstruction-risk gates;
- schema, contract, validation, evidence, policy, review, receipt, proof, catalog, and release requirements;
- no-network fixtures, deterministic replay, finite outcomes, idempotency, correction propagation, and rollback.

This README is not a pipeline-spec schema, parser, registry, scheduler, activation decision, executable pipeline, connector, source descriptor, object contract, machine schema, policy decision, review record, alert, notification system, receipt, proof, catalog record, release record, public API, map layer, search index, graph projection, or generated answer.

[Back to top](#top)

---

<a id="current-status"></a>

## Current status

### Repository maturity matrix

| Surface | Current evidence | Status | Safe conclusion |
|---|---|---:|---|
| Parent Hazards spec README | v0.1 draft before this revision | **CONFIRMED** | Existing declarative boundary, not active behavior |
| Nine flat YAML profiles | Seven-line `PROPOSED` inventory placeholders | **CONFIRMED placeholders** | Inventory slots only |
| Pipeline-spec schema | No accepted Hazards spec schema surfaced | **UNKNOWN** | Canonical shape and versioning are unverified |
| Parser / registry / discovery | No accepted binding surfaced | **UNKNOWN** | Loader, precedence, duplicate handling, and activation lookup are unverified |
| Scheduler / activation records | No verified records surfaced | **UNKNOWN** | Assume inactive |
| Executable Hazards pipeline | Detailed draft README | **CONFIRMED docs; behavior NEEDS VERIFICATION** | No runnable parent consumer is established |
| Hazards configuration | README-only bounded inventory | **CONFIRMED documentation** | No loader, precedence, polling, notification, or runtime binding |
| Semantic contracts | Draft parent plus implementation-shaped contract files | **CONFIRMED drafts** | Meaning is documented; enforcement is not proven |
| Machine schemas | Broad but stale index; concrete permissive `PROPOSED` stubs exist | **CONFIRMED partial inventory** | No active profile schema or field-complete coverage |
| Schema topology | `/domains/hazards/` and `/hazards/` lanes | **CONFLICTED** | Do not select authority by convenience |
| Source registry | Subtype-first and domain-first Hazards lanes | **CONFIRMED topology conflict** | Do not duplicate source authority |
| Source-authority register | `PROPOSED`; `entries: []` | **CONFIRMED empty register** | No source activation is established |
| Policy | Generic README, one referrals placeholder, five fail-closed Rego scaffolds | **CONFIRMED scaffolds** | Default denial exists; field-level enforcement is not established |
| Validators | Hazards index, no child validators confirmed | **CONFIRMED index-only** | No executable Hazards validator is established |
| Tests | Parent and child README hierarchy | **CONFIRMED documentation** | Executable modules and pass rates remain unverified |
| Fixtures | Broad child README inventory | **CONFIRMED documentation** | Payload inventory and consumer binding remain unverified |
| Receipts | Hazards parent; no child receipt lanes confirmed | **CONFIRMED draft** | No emitted receipt chain; exact subtype layout unresolved |
| Proofs | Draft Hazards proof lane | **CONFIRMED documentation** | Emitted proof packs and closure are unknown |
| Domain catalog | Draft parent | **CONFIRMED documentation** | Inventory and closure are unverified |
| Release candidates | Draft parent | **CONFIRMED documentation** | No approval or promotion established |
| Release manifest | `hazards-r0002.yaml` eight-line placeholder | **CONFIRMED placeholder** | No release authority |
| Published layer lane | Draft parent; `flood_event/` and `nfhl/` README children | **CONFIRMED documentation** | Released bytes and manifest linkage remain unknown |
| CI | Three `echo TODO` Hazards jobs | **CONFIRMED scaffold-only** | Green status is not Hazards enforcement |
| Ownership | Generic placeholder CODEOWNERS | **CONFIRMED placeholder** | Hazards review is not repository-enforced |
| Runtime / public use | No activation or deployment evidence in bounded searches | **UNKNOWN** | Assume inactive and non-public |

### Bottom line

The lane is an inventory and documentation boundary, not an active runtime surface. All nine profiles remain inactive until accepted machine shape, parser, consumer, source admission, activation, policy, tests, receipts, evidence, release, correction, and rollback support are verified.

[Back to top](#top)

---

<a id="current-inspected-inventory"></a>

## Current inspected inventory

| File | Intended family | Verified content | Current posture |
|---|---|---|---|
| `README.md` | Parent boundary | v0.2 repository-grounded documentation | Draft documentation |
| `fema_nfhl.yaml` | FEMA regulatory flood context | Seven-line planning placeholder | **INACTIVE / PROPOSED** |
| `fema_openfema.yaml` | FEMA administrative/regulatory context | Seven-line planning placeholder | **INACTIVE / PROPOSED** |
| `nasa_firms.yaml` | Satellite thermal/fire detections | Seven-line planning placeholder | **INACTIVE / PROPOSED** |
| `noaa_hms_smoke.yaml` | Fire/smoke analyst or modeled context | Seven-line planning placeholder | **INACTIVE / PROPOSED** |
| `noaa_storm_events.yaml` | Historical storm-event records | Seven-line planning placeholder | **INACTIVE / PROPOSED** |
| `nws_alerts_context.yaml` | Warning/watch/advisory context | Seven-line planning placeholder | **INACTIVE / PROPOSED** |
| `usgs_earthquake.yaml` | Earthquake event observations | Seven-line planning placeholder | **INACTIVE / PROPOSED** |
| `drought_monitor.yaml` | Drought modeled/aggregate context | Seven-line planning placeholder | **INACTIVE / PROPOSED** |
| `exposure_resilience_rollup.yaml` | Derived exposure/resilience summary | Seven-line planning placeholder | **INACTIVE / PROPOSED** |

Each YAML currently contains only `status`, `source_doc`, `path`, and a placeholder note. None defines a `spec_id`, schema version, source descriptor, source role, parser, executable target, cadence, lifecycle transition, time contract, evidence gate, policy gate, activation decision, correction path, or rollback target.

Exact profile-name searches surfaced these files and planning, connector, contract, or tool documentation. They did not establish a verified profile parser, scheduler, activation record, executable consumer, or spec-specific executable test binding. This is a bounded indexed-search conclusion, not an exhaustive recursive absence claim.

[Back to top](#top)

---

<a id="repository-fit"></a>

## Repository fit

Directory Rules assigns files by responsibility rather than topic.

| Responsibility | Verified or candidate home | Boundary |
|---|---|---|
| Declarative Hazards run intent | `pipeline_specs/hazards/` | This lane; current YAMLs are placeholders |
| Executable processing | `pipelines/domains/hazards/` | The **how**, not source or release authority |
| Safe configuration support | `configs/domains/hazards/` | README-only; no consumer binding established |
| Human doctrine | `docs/domains/hazards/` | Scope, life-safety, source-role, publication, and UI doctrine |
| Semantic meaning | `contracts/domains/hazards/` | Draft object meaning; compatibility lane exists elsewhere |
| Machine shape | `schemas/contracts/v1/domains/hazards/` or ADR-resolved home | Topology conflicted; current schemas are mostly permissive scaffolds |
| Source admission | `data/registry/sources/hazards/` or topology-resolved registry | Experimental and inactive |
| Connector implementation | Source-family connector homes | Connector aliases and duplicate boundaries require resolution |
| Policy | `policy/domains/hazards/` and accepted release/rights/sensitivity roots | Current machine files are scaffolds |
| Tests | `tests/domains/hazards/` | Documented test lanes; executable coverage unverified |
| Fixtures | `fixtures/domains/hazards/` | Synthetic examples only; payload inventory unverified |
| Validators | `tools/validators/domains/hazards/` and accepted cross-domain validators | Index-only at the inspected parent |
| Lifecycle data | `data/raw|work|quarantine|processed|catalog|triplets|published/.../hazards/` | Never stored beside specs |
| Receipts | `data/receipts/hazards/` | Process memory, not proof or release |
| Proofs | `data/proofs/hazards/` | Evidence closure, not runtime output or release authority |
| Catalog | `data/catalog/domain/hazards/` and accepted projections | Discovery and provenance, not release |
| Release candidates | `release/candidates/hazards/` | Pre-release review only |
| Release authority | ADR-resolved `release/` manifest/decision lanes | Current Hazards manifest is a placeholder |
| Published layers | `data/published/layers/hazards/` | Released public-safe bytes only after gates close |
| Public clients | Governed API and released artifacts | No direct spec, registry, receipt, proof, or candidate access |

### Current placement conflicts

These are documented, not resolved here:

1. `schemas/contracts/v1/domains/hazards/` versus `schemas/contracts/v1/hazards/`.
2. `data/registry/sources/hazards/` versus `data/registry/hazards/sources/`.
3. Source-family connector homes versus duplicate compatibility aliases.
4. Domain-local trust-object schemas versus common or cross-domain homes.
5. Singular and plural release-manifest path conventions.
6. Flat source-named profiles versus future object/stage child directories.
7. Legacy source-role and knowledge-character terms versus the canonical seven-role vocabulary.
8. Planned receipt subtype paths versus the verified `data/receipts/hazards/` parent.

Do not create a parallel authority, migrate files, or choose a canonical path without the appropriate ADR, migration note, or steward decision.

[Back to top](#top)

---

<a id="authority-and-anti-collapse"></a>

## Authority and anti-collapse

A reviewed active specification may declare:

- the one verified consumer eligible to read it;
- admitted source identifiers and accepted roles;
- the requested object or processing family;
- allowed lifecycle inputs and candidate outputs;
- time, freshness, geometry, evidence, policy, receipt, review, and release gates;
- deterministic finite outcomes when a gate cannot close.

A specification cannot decide:

- that a source is official, admitted, active, current, complete, rights-cleared, or authoritative;
- that a warning, watch, advisory, declaration, regulatory zone, detection, model, aggregate, or candidate is an observed event;
- that a detection is a confirmed wildfire, smoke impact, or emergency condition;
- that regulatory flood context is observed inundation or forecast flood extent;
- that expired, cancelled, or superseded operational context is current;
- that a model or aggregate supports a place-specific fact without its own evidence;
- that exact or generalized infrastructure, parcel, person, cultural, or emergency-resource detail is safe;
- that evidence closes a claim;
- that validation, policy, review, catalog closure, or release approval exists;
- that public clients may bypass governed interfaces;
- that KFM may issue or operationalize life-safety guidance.

### Disallowed collapses

```text
spec file -> executable pipeline
parse success -> active specification
profile merge -> source activation
source list -> source authority
provider name -> accepted source role
schedule -> freshness proof
warning context -> KFM alert
expired context -> current context
regulatory flood area -> observed inundation
FIRMS or HMS detection -> confirmed incident
model or aggregate -> observation
administrative declaration -> event footprint
exposure rollup -> exact impact or loss truth
representation requirement -> performed redaction
successful run -> EvidenceBundle
catalog record -> release approval
publish-ready flag -> PUBLISHED
generated summary -> evidence or official guidance
```

[Back to top](#top)

---

<a id="profile-family-boundaries"></a>

## Profile-family boundaries

### FEMA NFHL

- Treat as regulatory flood-hazard context from the issuing authority.
- Preserve effective dates, map/version identifiers, jurisdiction, scale, and revision lineage.
- Do not present it as observed inundation, forecast flood extent, current conditions, structural safety, insurance advice, permitting advice, or Hydrology measurement truth.
- Hydrology retains water observation and forecast ownership.

### FEMA OpenFEMA

- Preserve administrative, regulatory, program, declaration, grant, claim, or aggregate character by product.
- A declaration is not an observed event footprint or damage measurement.
- Claims and policy aggregates require aggregation, privacy, rights, and interpretation controls.
- Do not infer eligibility, entitlement, damages, legal status, or current emergency conditions.

### NASA FIRMS

- Preserve sensor, product, acquisition time, confidence, processing, and detection/candidate posture.
- A thermal anomaly is not automatically a confirmed fire, legal incident perimeter, containment status, evacuation need, or response instruction.
- Require review/disposition when a public claim would imply confirmation.

### NOAA HMS smoke

- Preserve analyst, observation, model, candidate, temporal-window, and source-product distinctions.
- Smoke context does not establish ground-level PM2.5, AQI, exposure, health impact, visibility safety, or medical guidance.
- Atmosphere/Air retains atmospheric observation and health-index ownership.

### NOAA/NCEI Storm Events

- Treat as historical event and administrative/observed source material according to the product fields.
- Preserve event identity, source vintage, beginning/end time, narrative limitations, revisions, and source-role distinctions.
- Historical records are not current watches, warnings, advisories, forecasts, road conditions, or emergency instructions.

### NWS alerts context

- Carry source identity, product identity, issue time, onset/effective time, expiry time, cancellation/supersession state, retrieval time, processing time, release time, and freshness state.
- Preserve a permanent not-for-life-safety disclaimer and official-source referral.
- KFM may not issue, alter, rank, suppress, extend, cancel, replace, notify from, or operationalize an official warning, watch, or advisory.
- Expired, cancelled, superseded, stale, or unverifiable context must not appear current.

### USGS earthquake

- Preserve event ID, origin time, revision state, magnitude type, location/depth uncertainty, source update state, and supersession/correction lineage.
- An earthquake event record is not damage truth, building safety, road safety, utility safety, inspection advice, or emergency guidance.
- Later revisions must propagate through catalog, public derivatives, caches, and correction records.

### Drought monitor and drought indicators

- Preserve modeled or aggregate character, classification version, publication period, spatial support, and cadence.
- A regional drought class is not parcel, field, crop, soil, water-supply, livestock, economic-loss, or management truth.
- Agriculture, Hydrology, Soil, and other owning domains retain their source truth.

### Exposure and resilience rollup

- Treat as derived or aggregate planning context.
- Preserve source roles, analysis unit, time window, methodology, uncertainty, coverage, missingness, and aggregation limits.
- Do not expose exact critical infrastructure, emergency resources, private persons, households, parcels, vulnerable sites, or reconstruction-enabling joins.
- Do not represent a rollup as observed impact, loss, safety condition, priority decision, funding decision, or resilience guarantee.

[Back to top](#top)

---

<a id="minimum-active-specification-contract"></a>

## Minimum active-specification contract

A future active Hazards profile must satisfy every applicable section below. Missing material results in `HOLD`, `DENY`, `ABSTAIN`, `QUARANTINE`, or `ERROR`; it does not become an implicit default.

### Identity and ownership

- `spec_id`, immutable version, content digest, domain, family, owner, reviewers, created/updated times;
- status, supersedes/superseded-by lineage, correction and rollback references;
- paired schema ID and version.

### Parser, consumer, and discovery

- accepted parser ID/version and deterministic parse result;
- one verified executable consumer and supported consumer version range;
- discovery mechanism, precedence, duplicate-ID behavior, and reload policy;
- explicit no-consumer and incompatible-consumer failure outcomes.

### Activation

- separate `SpecActivationDecision` or accepted equivalent;
- activation scope, environment, actor/reviewer, effective time, reason, and rollback target;
- no activation inferred from file presence, merge state, schema validity, schedule text, or successful dry run.

### Sources and rights

- admitted `SourceDescriptor` references and revisions;
- source activation references;
- canonical source role for each product;
- authority limits, rights, terms, attribution, redistribution, access, cadence, and freshness obligations;
- source-head identity, upstream version, checksums/manifests where applicable.

### Objects and knowledge character

- explicit object family or output family;
- source-native, observed, regulatory, modeled, aggregate, administrative, candidate, synthetic, contextual, or public-derivative posture as applicable;
- cross-domain ownership and anti-collapse rules.

### Time and freshness

- relevant event, observation, issue, onset, effective, valid, expiry, cancellation, supersession, retrieval, processing, release, correction, and stale-state times;
- accepted clock/timezone and precision rules;
- freshness profile, outage behavior, source-cadence failure, and stale/expired/cancelled handling;
- correction and supersession propagation requirements.

### Spatial support

- source, analysis, and publication CRS;
- geometry/support type, scale, resolution, extent, topology, precision, uncertainty, and generalization posture;
- public attribute allowlist and safe-as-bytes requirement;
- spatial joins and cross-lane ownership.

### Models, detections, and aggregates

- model/sensor/method identity and version;
- inputs, calibration/training or processing context, uncertainty, confidence, coverage, missingness, and fitness limits;
- detection disposition and confirmation boundary;
- aggregation unit, denominator, suppression/small-cell posture, and inference limits.

### Life safety and referral

- permanent `not_for_life_safety` posture;
- official-source identity and referral profile where operational misuse is plausible;
- explicit denial of warning issuance, alert alteration, evacuation, shelter, routing, medical, fire-response, incident-command, or other protective-action guidance;
- deterministic handling of unavailable or unverifiable official referrals.

### Sensitivity and public safety

- sensitivity and rights profile references;
- infrastructure, emergency-resource, private-person, household, parcel, cultural, archaeological, cave, and sensitive-site handling;
- small-cell, sparse-class, differencing, mosaic, join-induced, and reconstruction-risk review;
- redaction/generalization/aggregation receipt requirements;
- restricted logging, telemetry, cache, search, graph, export, and AI rules.

### Lifecycle, evidence, and release

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

The profile may declare eligible transitions but cannot perform or approve them by declaration. It must identify required validation, evidence, receipt, proof, catalog, policy, review, release, correction, withdrawal, and rollback records.

### Security and observability

- no secrets, credentials, private endpoints, or protected query material;
- sanitized logs and receipts;
- no exact sensitive coordinates or reconstruction-enabling keys;
- invalidation targets for caches, tiles, downloads, search, graph, vectors, embeddings, screenshots, reports, and generated summaries.

[Back to top](#top)

---

<a id="status-activation-discovery-and-precedence"></a>

## Status, activation, discovery, and precedence

### Proposed finite specification statuses

| Status | Meaning |
|---|---|
| `INVENTORY_PLACEHOLDER` | Path slot only; not parseable as an active profile |
| `DRAFT` | Meaningful profile under author review |
| `VALIDATED_INACTIVE` | Shape/semantic checks pass, but activation is absent |
| `REVIEW_REQUIRED` | Trust-bearing review remains open |
| `ACTIVE` | Separately activated for named consumer/environment |
| `SUSPENDED` | Discovery/scheduling disabled pending review |
| `SUPERSEDED` | Replaced by a named immutable revision |
| `RETIRED` | No new runs; lineage retained |
| `REJECTED` | Not eligible for activation |

Current YAML files remain `INVENTORY_PLACEHOLDER` regardless of their internal `status: PROPOSED` field.

### Proposed finite run outcomes

`NO_OP`, `CANDIDATE_CREATED`, `QUARANTINED`, `HOLD`, `STALE_CONTEXT`, `EXPIRED_CONTEXT`, `CANCELLED_OR_SUPERSEDED`, `DENY`, `ABSTAIN`, `REVIEW_REQUIRED`, `ERROR`, `CORRECTION_REQUIRED`, `WITHDRAWAL_REQUIRED`, and `ROLLBACK_REQUIRED`.

### Precedence rule

Until an accepted parser/registry contract exists:

1. no profile is discoverable by default;
2. filename and directory proximity grant no priority;
3. duplicate or ambiguous identity fails closed;
4. flat source profiles and future child profiles must not silently shadow one another;
5. activation must name the exact immutable profile digest and consumer;
6. unsupported consumer/profile versions fail closed;
7. watcher or refresh tooling cannot activate, admit, promote, notify, or publish.

[Back to top](#top)

---

<a id="sources-rights-and-source-roles"></a>

## Sources, rights, and source roles

The current source-authority register has no entries. None of the nine profile names therefore proves an admitted source.

Use the canonical seven-role vocabulary unless an accepted schema says otherwise:

| Role | Hazards interpretation |
|---|---|
| `observed` | Instrument, survey, verified report, or event observation with source limits |
| `regulatory` | Issuing-authority designation or legally scoped context |
| `modeled` | Forecast, scenario, estimate, trajectory, susceptibility, or derived model |
| `aggregate` | Summarized values over an explicit unit and denominator |
| `administrative` | Declaration, program, roster, grant, account, or administrative record |
| `candidate` | Detection, report, or unresolved record awaiting disposition |
| `synthetic` | Test/fixture material only |

Operational warning context does not create an eighth authority role. It is a time-sensitive contextual use of source records whose canonical source role, issuing authority, time state, and public limitations remain explicit.

Rights, public availability, successful fetch, or a well-known provider name do not establish redistribution, derivative, commercial-use, publication, or authority status. Each profile must reference reviewed rights and source-admission records.

[Back to top](#top)

---

<a id="object-family-and-knowledge-character-boundaries"></a>

## Object-family and knowledge-character boundaries

Keep these families separate:

- `HazardEvent` and `HazardObservation`;
- `WarningContext` and `AdvisoryContext`;
- `DisasterDeclaration`;
- `FloodContext` and regulatory hazard areas;
- `WildfireDetection` and `SmokeContext`;
- `DroughtIndicator`;
- `EarthquakeEvent` and heat/cold context;
- `ExposureSummary`, `ResilienceSummary`, `HazardTimeline`, and `ImpactArea`;
- source descriptor, source activation, receipt, proof, catalog, policy, review, release, correction, rollback, and published artifact families.

A map feature, tile, popup, layer manifest, Evidence Drawer payload, Focus Mode response, graph edge, vector result, screenshot, or generated summary is a downstream carrier. It cannot become sovereign Hazards truth.

Neighboring domains retain ownership:

- Hydrology owns water observations and forecasts;
- Atmosphere/Air owns atmospheric measurements and health-index context;
- Geology owns geological and subsurface truth;
- Roads/Rail/Trade owns network and closure identity where applicable;
- Settlements/Infrastructure owns facility and infrastructure identity;
- Agriculture, Soil, Habitat, Archaeology, and People/Land retain their own truth and sensitivity controls.

[Back to top](#top)

---

<a id="time-freshness-expiry-and-correction"></a>

## Time, freshness, expiry, and correction

Time kinds must not collapse. A profile should declare only the kinds material to its product, but must not reuse one timestamp for several meanings.

| Time kind | Meaning |
|---|---|
| Event / observation time | When the event or measurement occurred |
| Issue / publication time | When the upstream authority issued the product |
| Onset / effective time | When its stated applicability begins |
| Valid-through / expiry time | When current-use validity ends |
| Cancellation / supersession time | When the product was withdrawn or replaced |
| Retrieval time | When KFM obtained it |
| Processing time | When a governed transform ran |
| Release time | When a public KFM artifact was approved |
| Correction time | When a correction or withdrawal became effective |

Required behaviors:

- stale, expired, cancelled, superseded, or unverifiable operational context must not display as current;
- historical records stay historical even if retrieved recently;
- a recent file timestamp does not prove upstream freshness;
- outage or cadence failure produces an explicit finite outcome;
- corrections propagate to catalog, tiles, downloads, search, graph, caches, indexes, screenshots, reports, and generated summaries where affected;
- no profile may extend or override an issuing authority’s validity window.

[Back to top](#top)

---

<a id="spatial-support-scale-crs-and-public-representation"></a>

## Spatial support, scale, CRS, and public representation

A profile must distinguish:

- source geometry from processed geometry;
- point, line, polygon, grid cell, raster pixel, administrative area, regulatory area, analysis unit, footprint, corridor, and generalized public geometry;
- source CRS, processing CRS, analysis CRS, and publication/tiling CRS;
- source resolution from analysis and display resolution;
- observed footprint from regulatory, modeled, candidate, or aggregate support.

Public safety rules:

- public artifacts must be safe as bytes, not merely hidden by a style;
- exact infrastructure, emergency-resource, private-person, sensitive-site, and reconstruction-enabling fields are excluded unless an approved public representation explicitly permits them;
- bounds, centroids, tile coverage, hover payloads, search facets, graph edges, exports, and metadata may create leakage even when the primary geometry is generalized;
- public geometry requires evidence, policy, review, transform receipts, release state, correction path, and rollback target.

[Back to top](#top)

---

<a id="models-detections-aggregates-and-uncertainty"></a>

## Models, detections, aggregates, and uncertainty

### Model boundary

A model profile must identify method, version, inputs, time window, processing/run identity, uncertainty, calibration or validation posture, limitations, and fitness scope. Model output is not an observation or official warning.

### Detection boundary

A remote-sensing or automated detection must retain sensor/product identity, acquisition and processing times, confidence/quality flags, disposition, and candidate status. Detection is not confirmation or legal incident status.

### Aggregate boundary

An aggregate must state analysis unit, denominator, coverage, missingness, suppression, small-cell posture, and whether the result is appropriate for public interpretation. An aggregate cannot silently become a parcel, facility, household, person, or site claim.

### Uncertainty

Uncertainty, revision state, quality flags, spatial support, temporal support, and known limitations must travel with derived outputs. Absence of an uncertainty field does not mean certainty.

[Back to top](#top)

---

<a id="not-for-life-safety-and-official-source-referral"></a>

## Not for life safety and official-source referral

The Hazards lane has a permanent non-transformable boundary:

```text
KFM context != official alert != protective-action instruction
```

A public-facing candidate with operational context must preserve:

- issuing authority and source product identity;
- issue, effective/onset, expiry, cancellation, supersession, retrieval, processing, and release state where applicable;
- visible stale/expired/cancelled state;
- permanent not-for-life-safety disclaimer;
- reviewed official-source referral suitable to the product and jurisdiction;
- finite `DENY`, `ABSTAIN`, `ERROR`, or historical-only behavior when current status cannot be verified.

The following remain outside KFM authority:

- emergency alert issuance or delivery;
- prioritizing, suppressing, extending, cancelling, or replacing official products;
- evacuation, shelter, travel, route, re-entry, medical, fire-response, utility, water-safety, or incident-command instructions;
- claiming a road, building, facility, parcel, community, or person is safe or unsafe for current action;
- replacing direct official-source access for urgent decisions.

[Back to top](#top)

---

<a id="sensitivity-infrastructure-and-reconstruction-risk"></a>

## Sensitivity, infrastructure, and reconstruction risk

Hazards joins can increase sensitivity even when each input is individually public. Fail closed when a profile or derivative could reveal or reconstruct:

- critical infrastructure, emergency resources, response staging, utility or communications dependencies;
- private persons, households, addresses, parcels, medical or vulnerability attributes;
- culturally sensitive, archaeological, cave, sacred, burial, or sovereign-controlled places;
- security-relevant routes, access points, control systems, or facility details;
- sparse populations, small cells, rare categories, or identifiable outliers;
- protected Fauna/Flora, Habitat, Agriculture, or People/Land details through cross-surface joins;
- hidden geometry through centroids, bounding boxes, tile footprints, differencing, multiple zooms, search facets, graph links, embeddings, or exports.

A spec must reference approved sensitivity and public-representation profiles. It must not embed operational thresholds, redaction seeds, offsets, exact suppression parameters, credentials, or restricted endpoints in the spec, logs, receipts, reports, or public metadata.

[Back to top](#top)

---

<a id="lifecycle-gates-and-finite-outcomes"></a>

## Lifecycle gates and finite outcomes

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A specification can declare candidate transitions and required gates. It cannot make a transition occur by existing.

| Condition | Required outcome |
|---|---|
| Source not admitted or rights unresolved | `HOLD`, `DENY`, or `QUARANTINED` |
| Parser or consumer missing/incompatible | `ERROR` or `HOLD` |
| Duplicate/ambiguous profile identity | `ERROR` and no activation |
| Operational time state missing or unverifiable | `ABSTAIN`, `DENY`, `STALE_CONTEXT`, or `ERROR` |
| Context expired/cancelled/superseded | Historical-only, withdrawal, correction, or rollback |
| Detection lacks confirmation/disposition support | Candidate or review-required; never confirmed truth |
| Model/aggregate lacks method or uncertainty | `ABSTAIN` or `HOLD` |
| Sensitive join or reconstruction risk unresolved | `DENY`, `QUARANTINED`, or `REVIEW_REQUIRED` |
| Evidence missing for consequential claim | `ABSTAIN` |
| Policy engine unavailable where required | `ERROR` or `ABSTAIN`, never public exposure |
| Release state or rollback target missing | Promotion-blocking failure |
| No material source change | `NO_OP` with checkpoint/receipt where applicable |

[Back to top](#top)

---

<a id="evidence-receipts-proof-catalog-and-release"></a>

## Evidence, receipts, proof, catalog, and release

```text
receipt != proof != catalog != policy != review != release != publication
```

| Family | Responsibility |
|---|---|
| Receipt | Process memory: what a governed run did |
| Evidence/Proof | Support and closure for consequential claims |
| Catalog | Discovery and provenance projections |
| PolicyDecision | Admissibility outcome |
| ReviewRecord | Human/steward review state |
| ReleaseManifest / PromotionDecision | Publication authority |
| Published artifact | Released public-safe bytes/carriers |

Current posture:

- `data/receipts/hazards/` is a draft parent with no confirmed child receipt lanes or emitted instances;
- `data/proofs/hazards/` documents proposed proof families, not emitted closure;
- `data/catalog/domain/hazards/` documents the catalog boundary, not catalog closure;
- `release/candidates/hazards/` is pre-release guidance only;
- `release/manifests/hazards-r0002.yaml` is a placeholder, not a release;
- `data/published/layers/hazards/` documents publication boundaries and two child README lanes, not verified released bytes.

Public clients consume governed APIs and released artifacts only. They do not read profiles, source registries, lifecycle candidates, receipts, proofs, or release candidates directly.

[Back to top](#top)

---

<a id="illustrative-inactive-profile"></a>

## Illustrative inactive profile

The following is noncanonical and deliberately inactive. It demonstrates the minimum direction without asserting an accepted schema or activation mechanism.

```yaml
schema_version: PROPOSED-kfm.pipeline_spec.hazards.v1
spec_id: hazards.example.context-only
version: 0.0.0-example
status: DRAFT
active: false

ownership:
  owner: OWNER_TBD
  reviewers: []

binding:
  parser_id: NEEDS_VERIFICATION
  consumer_id: NEEDS_VERIFICATION
  activation_ref: null

sources:
  source_descriptor_refs: []
  source_activation_refs: []

scope:
  profile_family: operational_context
  object_family: WarningContext
  knowledge_character: administrative

time:
  issue_time_required: true
  expiry_time_required: true
  retrieval_time_required: true
  stale_state_required: true

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

This example cannot be activated by copying it into the repository.

[Back to top](#top)

---

<a id="validation-and-enforceability"></a>

## Validation and enforceability

### Required validation layers

1. **Shape:** accepted schema, version, required fields, unknown-key policy.
2. **Identity:** immutable ID/version/digest and duplicate handling.
3. **Binding:** parser, consumer, discovery, precedence, and activation references resolve.
4. **Source:** descriptors, roles, rights, activation, cadence, and source heads resolve.
5. **Semantics:** object family and knowledge character do not collapse.
6. **Time:** issue/valid/expiry/cancellation/supersession/freshness behavior is deterministic.
7. **Spatial:** CRS, support, scale, resolution, geometry, and public representation are valid.
8. **Model/detection/aggregate:** method, disposition, uncertainty, and limits are present.
9. **Safety:** permanent alert-authority denial and official-source referral behavior hold.
10. **Sensitivity:** infrastructure, people, sites, small cells, joins, and reconstruction risks fail closed.
11. **Lifecycle:** only allowed candidate transitions are requested.
12. **Evidence:** consequential claims require resolvable evidence support.
13. **Receipts/proof/catalog:** required families remain separate and inspectable.
14. **Policy/review/release:** decisions and approvals are referenced, not inferred.
15. **Correction/rollback:** downstream derivatives can be located, invalidated, corrected, withdrawn, or restored.
16. **Security:** secrets, private endpoints, sensitive values, and unsafe logs are absent.

### Deterministic negative scenarios

At minimum, future executable tests should cover:

- placeholder profile rejected as active;
- missing or duplicate `spec_id`;
- unsupported schema or consumer version;
- absent parser, consumer, activation, source descriptor, or source activation;
- source-role conflict;
- expired alert context presented as current;
- cancelled or superseded context not withdrawn;
- missing official-source referral or disclaimer;
- historical event presented as live operational status;
- NFHL presented as observed flood;
- FIRMS/HMS detection presented as confirmed incident or health guidance;
- drought aggregate presented as parcel/crop/water truth;
- exposure rollup leaking sensitive infrastructure or small cells;
- missing evidence, policy, review, release, correction, or rollback support;
- successful run treated as release approval;
- stale public cache or tile remaining resolvable after correction;
- watcher or refresh process attempting admission, activation, notification, or publication.

The current `domain-hazards` workflow does not implement these checks; its three jobs are TODO echoes.

[Back to top](#top)

---

<a id="definition-of-done-for-an-active-specification"></a>

## Definition of done for an active specification

A Hazards profile is not active until all applicable items are verified:

- [ ] accepted spec schema and deterministic parser;
- [ ] immutable identity, version, digest, ownership, and supersession lineage;
- [ ] verified executable consumer and version compatibility;
- [ ] explicit discovery, precedence, duplicate, and reload behavior;
- [ ] separate reviewed activation decision;
- [ ] admitted source descriptors and source activation references;
- [ ] reviewed rights, terms, attribution, cadence, and source role;
- [ ] accepted object/knowledge-character contract and machine schema;
- [ ] complete time/freshness/expiry/cancellation/supersession behavior;
- [ ] spatial support, CRS, scale, uncertainty, and public-safe representation;
- [ ] model/detection/aggregate method and limitations where applicable;
- [ ] permanent not-for-life-safety and official-source referral enforcement;
- [ ] sensitivity, infrastructure, people, cultural, small-cell, and reconstruction controls;
- [ ] deterministic no-network fixtures and executable negative tests;
- [ ] validator and meaningful CI enforcement;
- [ ] receipt emission and evidence/proof/catalog closure requirements;
- [ ] policy and human review records;
- [ ] release, correction, invalidation, withdrawal, and rollback support;
- [ ] public clients restricted to governed released interfaces;
- [ ] deactivation and rollback drill completed.

[Back to top](#top)

---

<a id="rollback-correction-and-deactivation"></a>

## Rollback, correction, and deactivation

### Documentation-only rollback

Before merge, close the review branch and abandon it. After merge, use a transparent revert commit or revert PR restoring v0.1 and removing the generated receipt. Do not rewrite shared history.

### Future active-profile rollback

1. Suspend discovery, scheduling, polling, and consumer loading.
2. Revoke or supersede the activation decision.
3. Preserve the exact profile, parser, consumer, source, source-head, run, receipt, evidence, policy, review, catalog, release, and artifact lineage.
4. Hold pending candidates and prevent new publication.
5. Identify affected processed records, catalogs, triplets, public artifacts, tiles, caches, downloads, searches, graphs, indexes, exports, screenshots, reports, and generated summaries.
6. Issue correction, withdrawal, supersession, or rollback records as applicable.
7. Restore a reviewed prior state or remain disabled.
8. Re-evaluate source role, rights, time, freshness, geometry, model, sensitivity, evidence, policy, and release state.
9. Rerun deterministic validation and proof closure.
10. Verify withdrawn or unsafe artifacts are no longer publicly resolvable.
11. Preserve official-source referral and historical context without misrepresenting current state.

[Back to top](#top)

---

<a id="open-verification-register"></a>

## Open verification register

| ID | Open verification | Status |
|---|---|---|
| `HAZ-SPEC-001` | Accepted owners and reviewer routing | NEEDS VERIFICATION |
| `HAZ-SPEC-002` | Exhaustive direct and recursive profile inventory | NEEDS VERIFICATION |
| `HAZ-SPEC-003` | Canonical pipeline-spec schema and registry | UNKNOWN |
| `HAZ-SPEC-004` | Parser, discovery, precedence, and duplicate behavior | UNKNOWN |
| `HAZ-SPEC-005` | Scheduler, reload, activation, and deactivation contracts | UNKNOWN |
| `HAZ-SPEC-006` | Executable consumer for each profile family | UNKNOWN |
| `HAZ-SPEC-007` | Source-registry topology and authority | CONFLICTED |
| `HAZ-SPEC-008` | Admitted descriptors for the eight named source families | UNKNOWN |
| `HAZ-SPEC-009` | Current rights, terms, attribution, redistribution, and cadence | NEEDS VERIFICATION |
| `HAZ-SPEC-010` | Canonical source-role and knowledge-character mapping | NEEDS VERIFICATION |
| `HAZ-SPEC-011` | Canonical contract/schema topology and aliases | CONFLICTED |
| `HAZ-SPEC-012` | Field-complete object and trust schemas | NEEDS VERIFICATION |
| `HAZ-SPEC-013` | Time-kind vocabulary and precision | NEEDS VERIFICATION |
| `HAZ-SPEC-014` | Freshness, expiry, cancellation, supersession, and outage profiles | NEEDS VERIFICATION |
| `HAZ-SPEC-015` | Official-source referral profiles and validation | NEEDS VERIFICATION |
| `HAZ-SPEC-016` | Permanent not-for-life-safety runtime enforcement | NEEDS VERIFICATION |
| `HAZ-SPEC-017` | Spatial, CRS, scale, topology, and uncertainty profiles | NEEDS VERIFICATION |
| `HAZ-SPEC-018` | Model, detection, aggregate, and disposition contracts | NEEDS VERIFICATION |
| `HAZ-SPEC-019` | Infrastructure/private/cultural sensitivity policy | NEEDS VERIFICATION |
| `HAZ-SPEC-020` | Public attribute allowlists and reconstruction-risk review | NEEDS VERIFICATION |
| `HAZ-SPEC-021` | Executable fixture payloads and expected outputs | NEEDS VERIFICATION |
| `HAZ-SPEC-022` | Executable Hazards tests and pass rates | UNKNOWN |
| `HAZ-SPEC-023` | Per-domain and cross-domain validator implementations | UNKNOWN |
| `HAZ-SPEC-024` | Receipt subtype layout and emitted instances | NEEDS VERIFICATION |
| `HAZ-SPEC-025` | Proof schemas, validators, and emitted closure | NEEDS VERIFICATION |
| `HAZ-SPEC-026` | Catalog/STAC/DCAT/PROV closure | NEEDS VERIFICATION |
| `HAZ-SPEC-027` | Canonical release-manifest path and schema | CONFLICTED |
| `HAZ-SPEC-028` | Release review, published bytes, digests, and rollback linkage | UNKNOWN |
| `HAZ-SPEC-029` | Governed API and public-layer consumer behavior | UNKNOWN |
| `HAZ-SPEC-030` | Cache/tile/search/graph/export/AI invalidation | NEEDS VERIFICATION |
| `HAZ-SPEC-031` | Correction, withdrawal, and supersession propagation | NEEDS VERIFICATION |
| `HAZ-SPEC-032` | Deactivation and rollback drill | NEEDS VERIFICATION |
| `HAZ-SPEC-033` | Hazards-specific CODEOWNERS and required reviews | NEEDS VERIFICATION |
| `HAZ-SPEC-034` | Substantive CI jobs and required-check enforcement | UNKNOWN |
| `HAZ-SPEC-035` | Connector alias consolidation or redirect posture | NEEDS VERIFICATION |
| `HAZ-SPEC-036` | Evidence-safe Focus Mode and generated-language behavior | NEEDS VERIFICATION |

[Back to top](#top)

---

<a id="evidence-ledger"></a>

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| `main@6006bcb2ce4b586e95d91d545b08b3a62c54ddf3` | CONFIRMED snapshot | Repository evidence boundary | Later commits may change state |
| Prior `pipeline_specs/hazards/README.md` | CONFIRMED v0.1 draft | Existing boundary and stale proposed tree | Does not prove implementation |
| Nine direct Hazards YAMLs | CONFIRMED | Current inventory and identical placeholder shape | No active semantics |
| Exact profile-name searches | CONFIRMED bounded searches | No indexed consumer/activation binding surfaced | Not exhaustive recursive absence |
| `docs/domains/hazards/MISSING_OR_PLANNED_FILES.md` | CONFIRMED planning artifact | Placeholder origin | Planning is not implementation proof |
| `pipelines/domains/hazards/README.md` | CONFIRMED draft | Executable responsibility and life-safety boundary | Runtime unverified |
| `configs/domains/hazards/README.md` | CONFIRMED draft v0.3 | Config maturity, conflicts, permanent boundary | Consumer unverified |
| `contracts/domains/hazards/README.md` | CONFIRMED draft | Semantic families and anti-collapse | Broad field enforcement unverified |
| Hazards schema indexes and representative schemas | CONFIRMED draft/scaffolds | Concrete files, placement conflict, permissive shapes | No accepted profile schema |
| `data/registry/sources/hazards/README.md` | CONFIRMED experimental | Source admission and topology conflict | No admitted source |
| `control_plane/source_authority_register.yaml` | CONFIRMED empty `entries` | No source activation | Register is PROPOSED |
| Hazards policy README, referrals placeholder, and five Rego files | CONFIRMED scaffolds | Policy home and fail-closed default | No complete runtime policy |
| `tests/domains/hazards/README.md` | CONFIRMED draft index | Documented test families | Executables/pass rate unverified |
| `fixtures/domains/hazards/README.md` | CONFIRMED draft index | Documented synthetic families | Payload/consumer inventory unverified |
| `tools/validators/domains/hazards/README.md` | CONFIRMED index-only | Intended validation responsibilities | No child validators confirmed |
| `data/receipts/hazards/README.md` | CONFIRMED draft | Receipt boundary | No child/emitted instances |
| `data/proofs/hazards/README.md` | CONFIRMED draft | Proof boundary | Emitted closure unknown |
| `data/catalog/domain/hazards/README.md` | CONFIRMED draft | Catalog boundary | Closure unknown |
| `release/candidates/hazards/README.md` | CONFIRMED draft | Candidate review boundary | No approval |
| `release/manifests/hazards-r0002.yaml` | CONFIRMED placeholder | Planned manifest slot | No release |
| `data/published/layers/hazards/README.md` | CONFIRMED draft | Published boundary and child README inventory | Released bytes/manifests unknown |
| `.github/workflows/domain-hazards.yml` | CONFIRMED TODO-only | Workflow names and trigger | No substantive enforcement |
| `.github/CODEOWNERS` | CONFIRMED placeholder | Generic ownership posture | No Hazards-specific rule |
| Directory Rules v1.4 | CONFIRMED doctrine | Responsibility roots and lifecycle boundary | Does not activate files |

### Evidence conclusion

This revision is a repository-grounded documentation upgrade. It does not change or prove runtime behavior. Future implementation claims must be re-verified against the exact branch, files, tests, logs, receipts, release records, and deployed surfaces then in force.

[Back to top](#top)

---

## v0.1 preservation assessment

Strong v0.1 concepts preserved and strengthened:

- `pipeline_specs/` is the **what**; `pipelines/` is the **how**;
- Hazards specs do not execute or publish;
- KFM is not an emergency alert or life-safety instruction system;
- operational context requires source, issue, expiry, freshness, and official referral;
- historical, regulatory, observational, remote-sensing, modeled, operational, administrative, exposure, and generated states do not collapse;
- lifecycle, evidence, receipts, release, correction, and rollback remain separate;
- neighboring domains retain truth ownership.

Corrections in v0.2:

- the speculative profile tree is replaced by the nine verified direct placeholders;
- stale test, fixture, receipt, and proof parent paths are removed as repo facts;
- implementation maturity is bounded by current evidence;
- schema, source-registry, connector, and release-manifest conflicts remain visible;
- activation, parser, consumer, and source-admission requirements are explicit;
- freshness, infrastructure sensitivity, reconstruction risk, invalidation, and rollback controls are expanded.

---

## Maintenance checklist

- [ ] Re-pin the evidence snapshot.
- [ ] Re-inventory direct files and open every changed profile.
- [ ] Search exact profile names for consumers and activation.
- [ ] Recheck source registry, rights, source roles, and activation records.
- [ ] Recheck parser, consumer, scheduler, and precedence binding.
- [ ] Recheck contracts, schemas, policy, tests, fixtures, and validators.
- [ ] Recheck receipts, proofs, catalog, release, and published artifacts.
- [ ] Recheck official-source referral and not-for-life-safety enforcement.
- [ ] Recheck cross-lane ownership, infrastructure sensitivity, and reconstruction risk.
- [ ] Recheck CI job steps, not only green status.
- [ ] Recheck CODEOWNERS and required reviews.
- [ ] Update correction, invalidation, withdrawal, and rollback posture.
- [ ] Emit generated provenance for AI-authored changes.
- [ ] Preserve truth labels and abstain from unverified implementation claims.

---

<p align="right"><a href="#top">Back to top</a></p>

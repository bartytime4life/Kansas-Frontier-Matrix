<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-domains-hazards-readme
title: configs/domains/hazards/ — Hazards Configuration Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Config steward · Hazards steward · Public-safety reviewer · Official-source reviewer · Consumer owner · Validation steward
created: 2026-07-13
updated: 2026-07-14
policy_label: public; config-sublane; hazards; not-for-life-safety; alert-authority-denied; source-role-aware; freshness-aware; sensitive-infrastructure-aware; non-secret; non-authoritative; no-live-binding
current_path: configs/domains/hazards/README.md
truth_posture: CONFIRMED canonical hazards slug, repository-present parent config contract, repository-present Hazards doctrine, permanent not-for-life-safety boundary, KFM-as-alert-authority T4-forever rule, seven source-role classes, expired-as-current denial, official-source redirect requirement, watcher-as-non-publisher rule, and documentation-only lane / CONFLICTED Directory-Rules segment form versus Atlas shorthand and hazards release-policy path options / PROPOSED future consumer-bound templates and governed contextual-display profiles / UNKNOWN consumers, loader behavior, precedence, deployment binding, and enforcement / NEEDS VERIFICATION owners, executable validation, source rights, freshness thresholds, official-source link profiles, public-safe infrastructure aggregation parameters, and runtime binding
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 2a060759170e94a8c5827c0a8c460d7488c8fea2
  prior_blob: e4e426c18b93e1c1b6d3a9e961939632e05e4bf9
  bounded_search_result: configs/domains/hazards/README.md only
related:
  - ../README.md
  - ../../README.md
  - ../../../docs/domains/hazards/README.md
  - ../../../docs/registers/DOMAIN_LANE.md
  - ../../../docs/registers/DRIFT_REGISTER.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/security/SECRETS.md
notes:
  - "This lane contains documentation only in the bounded path search. No executable Hazards configuration payload, consumer, loader, alerting function, warning issuer, network source, or publication binding is established."
  - "A bounded repository search for configs/domains/hazards returned this README and no indexed executable consumer. This is bounded evidence, not proof that no differently named or unindexed consumer exists."
  - "v0.2 expands the not-for-life-safety, official-source redirect, source-role, freshness, expired-state, cross-lane ownership, sensitive-infrastructure, validation, correction, and rollback contract without creating policy, schema, alert, source activation, release, or emergency-response authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hazards Domain Configuration

`configs/domains/hazards/`

> Safe-to-commit, Hazards-specific configuration documentation and future consumer-bound contextual-display templates. This lane does not own emergency alerting, warning issuance, incident command, hazard truth, official-source authority, policy, evidence, release, or publication.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Scope](#scope) · [Repository fit](#repository-fit) · [Inputs](#inputs) · [Outputs](#outputs) · [File contract](#minimum-configuration-contract) · [Consumer binding](#consumer-binding-precedence-and-discovery) · [Semantic guardrails](#hazards-semantic-and-source-role-guardrails) · [Freshness](#temporal-freshness-and-expired-state-contract) · [Public-safety boundary](#not-for-life-safety-and-official-source-redirect) · [Cross-lane boundaries](#cross-lane-ownership-and-context-rules) · [Sensitivity](#sensitive-infrastructure-and-public-safe-aggregation) · [Validation](#validation) · [Failure behavior](#failure-behavior) · [Review](#review-burden) · [Maintenance](#maintenance-and-safe-change-pattern) · [Migration](#migration-and-anti-bypass-posture) · [Done](#definition-of-done-for-the-first-payload) · [Related](#related-folders) · [ADRs](#adrs-and-drift-triggers) · [Rollback](#rollback-and-correction) · [Language](#safe-language-rules)

> [!IMPORTANT]
> **Document lifecycle:** draft `v0.2`  
> **Observed lane maturity:** README-only in the bounded path search; no executable Hazards configuration payload is established  
> **Authority:** implementation-supporting configuration sublane; non-authoritative for hazard truth and public-safety decisions  
> **Runtime posture:** no loader, consumer binding, source activation, polling, warning issuance, notification delivery, incident response, public layer, release, or publication is established by this README

> [!CAUTION]
> **KFM is not an emergency alert system.** Hazards configuration must never issue, synthesize, rank, suppress, replace, or operationalize warnings, watches, advisories, evacuation instructions, shelter directions, road-closure instructions, incident-command actions, or other life-safety guidance. Operational records may be surfaced only as contextual evidence with freshness disclosure, a permanent not-for-life-safety disclaimer, and a redirect to official authorities.

---

## Purpose

This directory defines the safe-to-commit configuration boundary for the canonical Hazards lane.

It may eventually hold small defaults, templates, examples, or review-oriented settings for a **named and verified contextual consumer**. Those files may describe how that consumer should render or validate already-governed Hazards material, but they cannot decide:

- whether an event, observation, warning, advisory, watch, declaration, exposure analysis, impact area, or model is true;
- whether a source is official, authoritative, admissible, licensed, current, or active;
- whether a warning or advisory should be treated as actionable;
- whether an expired operational record may be presented as current;
- whether an official-source link is appropriate or complete;
- whether critical-infrastructure or exact-location detail may be exposed;
- whether evidence supports a claim;
- whether a user should take emergency action; or
- whether an artifact may be promoted, released, or published.

This README is intended for:

- Hazards domain stewards;
- configuration and developer-experience maintainers;
- public-safety, official-source, freshness, rights, sensitivity, policy, security, and release reviewers;
- package, pipeline, app, runtime, test, watcher, connector, and tooling owners that may consume Hazards configuration; and
- reviewers checking Directory Rules placement and trust-membrane integrity.

[Back to top](#top)

---

## Authority level

**Configuration-supporting, contextual-only, and non-authoritative.**

| Concern | Authority in this lane |
|---|---|
| Hazards domain meaning | **None.** Domain doctrine remains in [`docs/domains/hazards/`](../../../docs/domains/hazards/README.md). |
| Emergency alerting or incident command | **Permanently none.** KFM-as-alert-authority is denied and cannot be enabled by configuration. |
| Warning, watch, or advisory issuance | **None.** Configuration cannot create, alter, prioritize, suppress, extend, cancel, or operationalize an official product. |
| Action guidance | **None.** Configuration cannot generate evacuation, shelter, travel, medical, fire-response, or protective-action instructions. |
| Hazard event or observation truth | **None.** Configuration cannot establish evidentiary status or convert a candidate, model, aggregate, declaration, or context object into an observation. |
| Regulatory or administrative status | **None.** Configuration cannot create or alter a declaration, regulatory flood zone, emergency order, permit, closure, or official designation. |
| Source identity, role, rights, cadence, and activation | **None.** These require the applicable source registry, connector, rights, policy, and review surfaces. |
| Freshness or expiry decision | **Supporting only.** A verified consumer may apply an accepted freshness profile; configuration cannot invent a threshold or override official issue and expiry times. |
| Schema or contract shape | **None.** Configuration may reference a verified schema or contract but must not duplicate or redefine it. |
| Sensitivity or public-safe geometry decision | **None.** A value may select an already-governed profile; it cannot create, weaken, or approve an infrastructure-redaction or aggregation rule. |
| Evidence or claim truth | **None.** Configuration cannot create an `EvidenceBundle`, validate a claim, or make generated interpretation sovereign truth. |
| Release or publication | **None.** Configuration cannot authorize promotion, release, public display, or KFM publication. |
| Consumer behavior | **Supporting only.** A verified consumer may read a validated file under an explicit binding and precedence rule. |

A configuration value may point to an authority surface. It does not become authority through repetition, proximity, successful parsing, operational convenience, apparent urgency, or use by a map, dashboard, notification component, Evidence Drawer, Focus Mode, export, or AI surface.

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
| Base commit | `2a060759170e94a8c5827c0a8c460d7488c8fea2` |
| Prior README blob | `e4e426c18b93e1c1b6d3a9e961939632e05e4bf9` |
| Bounded path-search result | `configs/domains/hazards/README.md` only |

### Maturity matrix

| Item | State | Safe conclusion |
|---|---:|---|
| Canonical domain slug | **CONFIRMED** | `hazards` is a repository-present canonical domain lane. |
| Parent configuration contract | **CONFIRMED** | [`configs/domains/README.md`](../README.md) defines this path as a non-secret, non-authoritative configuration sublane. |
| Hazards doctrine | **CONFIRMED repository-present** | The domain README establishes the permanent not-for-life-safety boundary, source-role separation, freshness disclosure, stale-state handling, official-source redirection, and watcher non-publication. |
| Alert-authority posture | **CONFIRMED — T4 forever** | KFM cannot become an alert authority through any configuration, transform, release, or display mode. |
| Current lane content | **README ONLY IN BOUNDED SEARCH** | No executable payload, consumer, or activation path was found by the path-scoped search. Exhaustive inventory remains `NEEDS VERIFICATION`. |
| Indexed executable consumer | **NOT FOUND IN BOUNDED SEARCH** | Differently named or unindexed consumers remain `UNKNOWN`. |
| Consumer and loader | **UNKNOWN** | No parser, auto-discovery mechanism, merge order, precedence, or unknown-key behavior is established here. |
| Source-role vocabulary | **CONFIRMED doctrine** | `observed`, `regulatory`, `modeled`, `aggregate`, `administrative`, `candidate`, and `synthetic` remain distinct. |
| Expired-as-current behavior | **CONFIRMED DENY** | An expired warning or advisory context must be historical/stale, never presented as current. |
| Disclaimer and official redirect | **CONFIRMED REQUIRED** | Every Hazards public surface must retain not-for-life-safety language and direct users to official authorities. |
| Path form | **CONFLICTED / GOVERNED BY DIRECTORY RULES FOR THIS README** | Directory Rules uses domain segments; Atlas shorthand and release-policy path alternatives remain drift/ADR matters. |
| Source rights and terms | **NEEDS VERIFICATION** | Source-specific rights, attribution, redistribution, cadence, and access limits require verified source records. |
| Freshness thresholds | **NEEDS VERIFICATION** | Per-source latency, stale, expired, partial, and outage thresholds require accepted profiles and source-owner review. |
| Public-safe infrastructure parameters | **NEEDS VERIFICATION** | Aggregation, masking, suppression, and precision limits must come from policy and steward review. |
| Validation and CI enforcement | **NEEDS VERIFICATION** | Expectations are documented; substantive executable enforcement is not proven by this README. |
| Runtime, release, and publication | **NOT ESTABLISHED** | Nothing in this lane authorizes operational use, warning delivery, release, or publication. |

Directory presence must not trigger source discovery, polling, network access, alert ingestion, notification delivery, geofencing, sirens, messaging, incident workflows, emergency recommendations, map-layer creation, lifecycle promotion, or publication.

[Back to top](#top)

---

## Scope

### What belongs here

Only safe, non-secret, Hazards-specific configuration material for a named or explicitly proposed **contextual** consumer belongs here.

| Material | Permitted purpose | Minimum posture |
|---|---|---|
| `README.md` | Define this configuration boundary. | Preserve non-alert authority, source-role, freshness, evidence, sensitivity, and release controls. |
| `*.template.yaml` or `*.template.yml` | Placeholder-based template for a verified contextual consumer. | Parseable, versioned, consumer-bound, no secrets, no live binding, no alerting action. |
| `*.example.yaml`, `*.example.json`, or `*.example.toml` | Tiny illustrative configuration. | Clearly synthetic values; impossible identifiers and geometry; no automatic activation. |
| Conservative contextual-display defaults | Select existing historical, stale, contextual, hold, abstain, deny, or official-link modes. | Cannot weaken policy, freshness, disclaimer, source rights, evidence, or release burden. |
| Official-source link profile selectors | Select an already-reviewed link profile for a verified public surface. | Cannot claim completeness, replace official channels, or embed action instructions. |
| Freshness-profile selectors | Select an accepted per-source freshness profile. | Cannot override source issue/expiry fields or silently extend validity. |
| Public-safe display profile selectors | Select an already-governed generalized infrastructure or impact-area profile. | Cannot contain exact protected detail or authorize exposure. |
| Presentation hints | Configure role badges, time labels, stale-state banners, uncertainty, disclaimer placement, or caveat rendering. | Must not change evidence status, urgency, authority, validity, or sensitivity. |
| Migration notes | Document a real key, version, consumer, or path transition. | Time-bounded, owner-linked, reversible, and not a parallel authority. |
| Validation notes | Describe verified checks and finite outcomes. | Commands and workflows must resolve or remain labeled `PROPOSED` / `NEEDS VERIFICATION`. |

Synthetic examples must not resemble a real warning identifier, active incident, critical facility, emergency resource, shelter, hospital, utility asset, transport control point, hazardous-material site, or exact impact location closely enough to cause confusion or support reconstruction.

### What does not belong here

- current warnings, watches, advisories, emergency alerts, evacuation notices, shelter instructions, protective-action guidance, road-closure instructions, or incident-command material;
- real hazard events, observations, warning feeds, advisory feeds, detection payloads, model grids, declarations, exposure outputs, or source payloads;
- exact or reconstructable critical-infrastructure, emergency-response, hazardous-material, utility, communications, shelter, healthcare, transportation-control, or resilience-critical asset detail;
- credentials, tokens, private keys, cookies, signed URLs, private endpoints, workstation paths, internal deployment bindings, contact lists, pager routes, phone trees, or messaging secrets;
- settings that label a model or detection as an observation or confirmed event;
- settings that label historical or expired operational context as current;
- settings that suppress the not-for-life-safety disclaimer or official-source redirect;
- settings that trigger notifications, SMS, email, push messages, automated calls, sirens, dispatch, escalation, ticketing, or emergency workflows;
- settings that convert official-source context into KFM-authored advice;
- permissive fallbacks that hide stale, missing, partial, failed, or contradictory source state;
- source admission, activation, cadence, rights, redistribution, or source-role decisions;
- schemas, contracts, policy, registries, receipts, proofs, evidence bundles, release records, correction notices, or publication decisions;
- package code, pipeline logic, connector code, watcher code, runtime adapters, infrastructure definitions, generated artifacts, caches, exports, screenshots, or reports.

[Back to top](#top)

---

## Repository fit

This directory is a domain segment under the canonical `configs/` responsibility root.

| Responsibility | Canonical or proposed home | This lane's relationship |
|---|---|---|
| Human-facing Hazards doctrine | `docs/domains/hazards/` | This README references it; it does not duplicate doctrine authority. |
| Semantic object meaning | `contracts/domains/hazards/` | Future config may reference accepted contracts only. |
| Machine-checkable shape | `schemas/contracts/v1/domains/hazards/` | Future config must validate against the accepted schema home. |
| Admissibility and not-for-life-safety policy | `policy/domains/hazards/` or separately governed release-policy home | Configuration may select an accepted profile; it cannot define policy. |
| Source identity, role, rights, and activation | `data/registry/sources/hazards/` plus connector governance | Configuration cannot admit or activate sources. |
| Tests and fixtures | `tests/domains/hazards/`, `fixtures/domains/hazards/` | Future payloads require deterministic positive and negative tests. |
| Shared implementation | `packages/domains/hazards/`, if verified | Configuration may support a named package but cannot replace code. |
| Executable processing | `pipelines/domains/hazards/` | Configuration may parameterize a verified pipeline but cannot publish. |
| Declarative pipeline specification | `pipeline_specs/hazards/` | Pipeline execution remains separately reviewed. |
| Source-specific fetching | `connectors/<source_id>/` | No connector belongs in this config lane. |
| Lifecycle data | `data/<phase>/hazards/` | No event, feed, warning, model, receipt, proof, or release payload belongs here. |
| Release and rollback | `release/` | Configuration is not a release decision or rollback record. |
| Public clients | Governed APIs and released artifacts | Public clients must never read this directory as data or authority. |

### Path conflict posture

Directory Rules uses domain-segment paths. Some Atlas tables use shorthand paths, and Hazards release policy may have more than one defensible home pending ADR resolution. This README:

- follows the parent configuration lane at `configs/domains/hazards/`;
- does not create aliases, mirrors, or duplicate configuration authority;
- does not resolve the release-policy path question;
- requires an ADR or drift resolution before a future payload depends on a disputed path.

[Back to top](#top)

---

## Inputs

A future Hazards configuration payload may accept only explicit, inspectable, non-secret inputs for a verified contextual consumer.

| Input family | Required handling |
|---|---|
| Consumer identity | Name the exact package, pipeline, app, runtime adapter, test, or tool. |
| Format and version | Declare YAML/JSON/TOML or other format, semantic version, parser, and compatibility policy. |
| Source references | Use verified source IDs or placeholders; never embed real payloads, credentials, or private endpoints. |
| Source role | Preserve one canonical role: `observed`, `regulatory`, `modeled`, `aggregate`, `administrative`, `candidate`, or `synthetic`. |
| Hazard object role | Preserve event, observation, warning context, advisory context, declaration, detection, model context, exposure summary, resilience summary, timeline, and impact-area distinctions. |
| Official-source profile | Reference an accepted link profile for the relevant jurisdiction and hazard family; do not encode emergency advice. |
| Temporal fields | Preserve event, observed, issue, expiry, valid, source, retrieval, release, and correction times where material. |
| Freshness profile | Reference a reviewed source-specific profile; never invent validity by convenience. |
| Rights and attribution | Reference verified rights and attribution records; unresolved terms fail closed. |
| Sensitivity profile | Reference accepted infrastructure/public-safe aggregation policy; do not define exact precision locally. |
| Evidence reference | Consequential contextual displays must identify the applicable evidence and release surfaces. |
| Disclaimer profile | Select the permanent not-for-life-safety language and official-source redirect; suppression is forbidden. |
| Local override mechanism | Document how real local values remain ignored and uncommitted, if applicable. |
| Deactivation and rollback | Document how the consumer stops selecting the configuration and restores a known-good state. |

Missing or unresolved source role, rights, issue/expiry information, freshness, official-source profile, evidence, sensitivity, consumer binding, or release context must not fall back to an apparently current or actionable display.

[Back to top](#top)

---

## Outputs

This lane currently outputs documentation only.

A future configuration file may support a verified consumer in producing **contextual** behavior such as:

- explicit historical-versus-current-versus-stale labels;
- source-role badges;
- issue, expiry, valid, retrieval, release, and correction timestamps;
- not-for-life-safety disclaimer placement;
- official-source link presentation;
- uncertainty and caveat display;
- stale, partial, outage, correction, and supersession banners;
- generalized impact-area or exposure-summary display profiles; and
- finite internal validation outcomes.

A file here cannot:

- issue or deliver an alert;
- recommend emergency action;
- activate a live feed or connector;
- establish a hazard event or regulatory fact;
- convert a warning record into KFM authority;
- extend an expired product;
- expose exact critical infrastructure;
- create evidence, policy, release, or publication state; or
- make KFM suitable for life-safety reliance.

[Back to top](#top)

---

## Minimum configuration contract

Every future non-README file in this lane should document or carry the following fields, directly or through an adjacent manifest.

| Field | Requirement |
|---|---|
| `config_id` | Stable identifier for the configuration file or profile. |
| `config_version` | Explicit version with migration rules. |
| `format_version` | Parser/schema version, separate from content version where applicable. |
| `status` | `proposed`, `active-for-nonproduction-context`, `deprecated`, `disabled`, or another accepted bounded state. |
| `intended_consumer` | Exact consumer path or identifier; no generic “Hazards system” label. |
| `consumer_owner` | Accepted accountable owner. |
| `load_path` | Explicit verified load mechanism; directory presence is never enough. |
| `precedence` | Documented overlay position and duplicate-key behavior. |
| `unknown_key_behavior` | Prefer reject/fail; any alternative requires explicit compatibility review. |
| `missing_file_behavior` | Safe disabled, hold, or error behavior; never permissive alerting fallback. |
| `source_role_constraints` | Preserve the seven canonical roles without upgrades. |
| `hazard_object_constraints` | Preserve event, observation, operational context, declaration, detection, model, exposure, and resilience distinctions. |
| `official_source_profile_ref` | Reference to accepted official-authority link and attribution profile. |
| `freshness_profile_ref` | Reference to reviewed source-family freshness and expiry policy. |
| `disclaimer_profile_ref` | Permanent not-for-life-safety disclaimer profile; cannot be disabled. |
| `rights_profile_ref` | Verified rights, attribution, and redistribution reference. |
| `sensitivity_profile_ref` | Accepted public-safe infrastructure and geometry profile. |
| `evidence_requirement` | Evidence and release references required before contextual public display. |
| `network_behavior` | `disabled` for examples/tests; network activation belongs to connectors and runtime governance. |
| `notification_behavior` | `disabled`; alert and notification delivery is outside this lane. |
| `validation_command` | Verified command or `NEEDS VERIFICATION`. |
| `test_fixture_ref` | Synthetic fixture set covering valid and negative states. |
| `deactivation` | Explicit stop-selection or safe-disable procedure. |
| `rollback` | Prior known-good version and restoration procedure. |
| `last_reviewed` | Review date and responsible roles. |

A parser accepting the file is not proof that the values are safe, current, official, policy-compliant, releasable, or suitable for public use.

[Back to top](#top)

---

## Consumer binding, precedence, and discovery

No general Hazards configuration loader is established by this README.

A future consumer binding must identify:

1. the exact consumer and owner;
2. the exact file path and format;
3. whether loading is required or optional;
4. the load trigger and environment boundary;
5. the precedence order relative to defaults, environment, deployment, test, and local overrides;
6. duplicate-key behavior;
7. unknown-key behavior;
8. missing-file behavior;
9. malformed-file behavior;
10. stale-profile and unavailable-profile behavior;
11. deactivation and rollback behavior; and
12. tests proving that directory presence alone has no effect.

### Required defaults

Unless a verified consumer contract says otherwise:

- no auto-discovery;
- no network access;
- no feed activation;
- no notification or alert delivery;
- no implicit environment merge;
- no silent coercion of invalid values;
- no silent use of unknown keys;
- no extension of warning/advisory validity;
- no fallback from missing official-source links to KFM-authored guidance;
- no public exposure from configuration presence;
- no lifecycle promotion from successful parsing.

When precedence is ambiguous, the safe outcome is `ERROR` or `HOLD`, not an unpredictable merge.

[Back to top](#top)

---

## Hazards semantic and source-role guardrails

### Canonical source-role classes

The following roles remain distinct:

| Role | Meaning for configuration purposes | Must not become |
|---|---|---|
| `observed` | Measured or recorded observation tied to evidence and time. | Regulatory authority, model truth, or warning issuance. |
| `regulatory` | Official designation, zone, declaration, or rule context from the responsible authority. | Observation, forecast, or KFM-authored advice. |
| `modeled` | Forecast, simulation, trajectory, probability, susceptibility, or exposure model. | Observation, confirmed impact, regulatory zone, or alert. |
| `aggregate` | Summary across records, geography, or time. | Exact event detail, individual exposure, or current warning state. |
| `administrative` | Declaration, jurisdiction, program, or management record. | Physical hazard observation or instruction. |
| `candidate` | Unresolved, proposed, detected, or review-pending record. | Confirmed event, official warning, or published truth. |
| `synthetic` | Fixture or test-only material. | Real-world condition, official product, or public claim. |

Configuration may constrain a consumer to accept certain roles. It cannot upgrade, collapse, or reinterpret a source role.

### Hazard object anti-collapse

| Object or context | Required distinction |
|---|---|
| `HazardEvent` | Historical or evidence-supported event; not automatically a current emergency. |
| `HazardObservation` | Measured observation; not automatically a warning, declaration, or forecast. |
| `WarningContext` | Official warning record surfaced as context; never KFM-issued and never actionable without official verification. |
| `AdvisoryContext` / watch context | Operational context with issue, expiry, freshness, and disclaimer; not an instruction. |
| `DisasterDeclaration` | Administrative or legal declaration context; not proof of local impact severity or current danger. |
| `WildfireDetection` | Detection or hotspot indication; not automatic fire confirmation, perimeter, or evacuation trigger. |
| `SmokeContext` | Observation or model context as role-labeled; not interchangeable with health guidance or PM2.5 observation. |
| `DroughtIndicator` | Aggregate indicator; not exact field condition, individual loss, or emergency declaration. |
| `FloodContext` | References Hydrology/regulatory truth; not independent gauge or NFHL authority. |
| `ExposureSummary` | Analysis projection; not exact facility inventory, casualty prediction, or command priority. |
| `ResilienceSummary` | Planning analysis; not certification, guarantee, or emergency plan. |
| `ImpactArea` | Event/model-bound area with uncertainty; not an evacuation zone unless issued by the official authority. |

### Detection, model, observation, and confirmation

- A detection is not confirmation.
- A forecast is not an observation.
- A modeled trajectory is not measured concentration.
- A regulatory polygon is not an observed event footprint.
- A disaster declaration is not a current warning.
- A warning record is not KFM alert authority.
- A historical severe-weather event is not proof of present conditions.
- An exposure model is not a casualty or damage attestation.
- A map label, popup, tile, export, or AI summary is not sovereign truth.

[Back to top](#top)

---

## Temporal, freshness, and expired-state contract

Hazards configuration must preserve distinct time semantics wherever material.

| Time | Meaning | Prohibited collapse |
|---|---|---|
| `event_time` | When a historical or observed hazard occurred. | Must not be replaced by retrieval or publication time. |
| `observed_time` | When an observation was measured. | Must not be treated as warning issue time. |
| `issue_time` | When an official operational product was issued. | Must not be inferred from retrieval time. |
| `expiry_time` | When an official operational product ceased to be valid. | Must not be extended by configuration. |
| `valid_time` | Forecast/model validity window. | Must not be treated as observation time. |
| `source_time` | When the source asserted or published the record. | Must not become event time by default. |
| `retrieval_time` | When KFM obtained the record. | Must not imply source freshness or official validity. |
| `release_time` | When a governed KFM derivative was released. | Must not replace source or event time. |
| `correction_time` | When a correction or supersession was recorded. | Must not erase prior lineage. |

### Freshness states

A verified consumer should use explicit finite states such as:

- `current_context` — within accepted issue/expiry and freshness profile, still contextual only;
- `historical` — intentionally displayed as past context;
- `stale` — freshness threshold exceeded;
- `expired` — official expiry passed;
- `partial` — source coverage incomplete;
- `unavailable` — source or required dependency unavailable;
- `superseded` — replaced by a newer official record;
- `corrected` — corrected record with lineage preserved;
- `unknown` — freshness cannot be established.

### Hard rules

- Expired operational context must never appear as current.
- Stale or unknown time-sensitive context must not produce an apparently current answer.
- Retrieval success is not proof of official validity.
- Cached data must retain source time, retrieval time, and stale status.
- Source outage must be visible; do not silently reuse stale data as current.
- Partial feeds must be labeled partial; absence of records is not proof of safety.
- Corrections and supersessions must preserve prior lineage.
- A clock or timezone ambiguity must cause hold/abstention/error, not guessed validity.

[Back to top](#top)

---

## Not-for-life-safety and official-source redirect

### Permanent boundary

KFM-as-alert-authority is denied permanently. No configuration profile, environment variable, feature flag, release setting, model score, confidence threshold, administrator toggle, or emergency mode may relax this boundary.

A Hazards contextual display must not:

- say or imply “all clear,” “safe,” “evacuate,” “shelter now,” “avoid this route,” “take cover,” or similar operational guidance as KFM authority;
- rank or prioritize warnings for action;
- suppress an official warning because a model disagrees;
- extend, shorten, cancel, or modify an official warning;
- combine multiple records into a new KFM-authored alert;
- trigger notifications or dispatch;
- imply continuous monitoring or guaranteed coverage;
- claim that no official warning exists based only on missing data.

### Mandatory public-surface elements

Every governed public Hazards surface must retain:

1. a clear **not-for-life-safety** disclaimer;
2. a statement that KFM provides historical, scientific, regulatory, modeled, or operational context only;
3. the source role and source identity;
4. issue, expiry, observation, valid, retrieval, and freshness information as applicable;
5. an official-source redirect appropriate to the hazard and jurisdiction;
6. stale, partial, unavailable, superseded, and correction state where applicable;
7. evidence and release references; and
8. a bounded finite outcome rather than improvised guidance.

The disclaimer and official redirect must not be hidden behind optional expansion, low-contrast styling, hover-only interaction, client-side filtering, or a configuration toggle.

### Official-source profile rules

A future config may select an accepted official-source profile, but it must not:

- invent an authority;
- claim the profile is exhaustive;
- replace local, county, tribal, state, or federal emergency channels;
- embed emergency instructions copied out of context;
- use an unofficial mirror as the controlling source;
- omit jurisdictional scope;
- silently keep a broken or stale link as if verified.

Broken, missing, or unverified official-source profiles must produce `HOLD`, `ABSTAIN`, or `ERROR` for public contextual use.

[Back to top](#top)

---

## Cross-lane ownership and context rules

Hazards consumes adjacent-lane truth through governed references. Configuration cannot transfer ownership.

| Adjacent lane | Owned truth | Hazards may consume as | Required constraint |
|---|---|---|---|
| Hydrology | Gauge observations, hydrography, HUC identity, NFHL/regulatory water context | Flood/drought/water-event context | Preserve `observed`, `regulatory`, and `modeled` distinctions; Hazards does not become gauge or NFHL authority. |
| Atmosphere | Weather and air observations, smoke/AQI context, advisories, models | Smoke, heat/cold, wind, fire-weather context | AOD is not PM2.5; model is not observation; Atmosphere remains source owner. |
| Settlements / Infrastructure | Facilities, lifelines, dependencies, critical assets | Exposure and resilience summaries | Exact critical-infrastructure precision defaults to denial; summary does not become facility truth. |
| Roads, Rail, and Trade | Closures, detours, crossings, route status | Resilience or impact context | Hazards cannot issue or verify operational route instructions. |
| Agriculture | Fields, crops, yield, agricultural operations | Aggregate drought, heat, fire, or flood impact context | No exact per-field claim from aggregate hazard data. |
| Geology | Earthquakes, faults, subsidence or landslide context as owned | Hazard context and impact relations | Hazard risk interpretation does not replace geologic evidence. |
| People / Land | Population, parcel, ownership, demographic context | Public-safe exposure summaries | No individual, household, private parcel, or ownership inference from aggregate exposure. |

A join inherits the strongest applicable rights, sensitivity, freshness, and release burden of the inputs and may become more sensitive than any single source viewed alone.

[Back to top](#top)

---

## Sensitive infrastructure and public-safe aggregation

Hazards configuration is high-risk because apparently harmless display or aggregation settings can reveal emergency-response capacity, critical facilities, utility dependencies, hazardous-material sites, vulnerable populations, or operational weak points.

### Deny-by-default detail

Do not commit or enable exact or reconstructable:

- emergency operations centers, dispatch infrastructure, or communication nodes;
- hospitals, shelters, response staging areas, or resource stockpiles when operational sensitivity applies;
- utility control points, substations, pipelines, water-system controls, or communications dependencies;
- hazardous-material storage or response details;
- critical bridges, crossings, evacuation control points, or chokepoints where precision creates risk;
- private facilities, parcel-level vulnerability, or individual/household exposure;
- detailed infrastructure dependency graphs;
- protected operational contacts, escalation paths, or schedules.

### Public-safe profile requirements

An accepted profile should specify:

- allowed geographic aggregation;
- minimum count or population thresholds;
- suppression rules;
- precision and zoom limits;
- field allowlists;
- differencing and repeated-query controls;
- temporal aggregation;
- cross-layer join restrictions;
- residual-risk review;
- steward approval requirements;
- correction and withdrawal behavior.

Configuration may select a profile. It cannot create an ad hoc “safe” precision, lower a tier, or use styling as the only protection.

The output tier follows the most sensitive input that materially shaped the result. A public-safe default for an object family never overrides T3/T4 source detail.

[Back to top](#top)

---

## Validation

Validation must be deterministic, no-network by default, fail closed, and scoped to the named consumer.

### Documentation checks

- KFM Meta Block parses and remains internally consistent.
- Headings and anchors resolve.
- Relative links resolve or are labeled `PROPOSED` / `NEEDS VERIFICATION`.
- The final newline is present.
- Truth labels do not overstate implementation.
- The not-for-life-safety boundary remains explicit.

### Static safety checks

- No credentials, tokens, signed URLs, private endpoints, messaging secrets, contact lists, workstation paths, or deployment bindings.
- No real warnings, current incidents, emergency instructions, exact infrastructure details, or operational resource details.
- No realistic synthetic identifiers, coordinates, timestamps, or facility names that could be mistaken for a live event.
- No config key enables alerting, notification, dispatch, escalation, polling, or source activation.
- No disclaimer-suppression or official-redirect-suppression key exists.
- No map-style-only sensitivity control is treated as sufficient.

### Parse and shape checks

- Declared parser and format version succeed.
- Required keys are present.
- Unknown keys fail unless a documented compatibility rule applies.
- Duplicate keys fail deterministically.
- Invalid enum values fail.
- Invalid timestamps, timezones, intervals, and expiry ordering fail.
- Invalid CRS, geometry, precision, aggregation, and unit values fail.
- Missing disclaimer, official-source, freshness, rights, sensitivity, evidence, or consumer references fail or hold as defined.

### Semantic checks

- Seven source roles remain non-interchangeable.
- Event, observation, warning context, advisory context, declaration, detection, model, aggregate, exposure, and resilience classes remain distinct.
- Expired operational context cannot appear current.
- Stale, unknown, partial, unavailable, corrected, and superseded states remain visible.
- A detection cannot become confirmation.
- A model cannot become observation or warning.
- A declaration cannot become current danger.
- Hydrology, Atmosphere, Infrastructure, Roads, Agriculture, Geology, and People/Land ownership remains intact.
- Exact critical-infrastructure detail cannot reach public-safe output.
- Official-source redirection remains present and jurisdictionally scoped.
- No validation result is treated as release approval.

### Negative fixtures

Synthetic fixtures should cover at least:

- expired warning presented as current;
- stale advisory with no valid official-source profile;
- missing issue or expiry time;
- retrieval time incorrectly used as issue time;
- modeled impact labeled observed;
- detection labeled confirmed event;
- warning context presented as KFM alert;
- missing disclaimer;
- hidden disclaimer;
- missing or broken official redirect;
- source outage with stale fallback;
- partial feed presented as complete;
- unknown source role;
- unresolved rights;
- exact infrastructure precision;
- low-count exposure summary;
- join-induced sensitivity;
- unknown key and duplicate key;
- ambiguous precedence;
- attempted notification or source activation;
- rollback to prior safe disabled state.

Executable validation remains `NOT APPLICABLE` to the current README-only lane. It becomes required before any non-README payload is accepted.

[Back to top](#top)

---

## Failure behavior

Hazards configuration failures must produce finite, inspectable outcomes.

| Condition | Expected safe disposition |
|---|---|
| Valid non-sensitive contextual configuration | `PASS` for internal validation; continue to ordinary governed processing. |
| Malformed file, unsupported version, duplicate key, or contract violation | `FAIL` or `ERROR`; do not partially apply. |
| Unknown source role or object role | `HOLD` or `ABSTAIN`; quarantine rather than infer. |
| Missing issue/expiry/freshness information for operational context | `HOLD` or `ABSTAIN`; do not present as current. |
| Expired warning/advisory requested as current | `DENY`; historical display only with stale/expired labeling. |
| Missing not-for-life-safety disclaimer | `FAIL` and `DENY` public use. |
| Missing or unverified official-source redirect | `HOLD`, `ABSTAIN`, or `ERROR`; do not substitute KFM guidance. |
| Alerting, notification, dispatch, or action-instruction key detected | `FAIL` and `DENY`; configuration is out of scope. |
| Missing source rights, evidence, sensitivity, policy, review, or release state | `HOLD`, `DENY`, or `ABSTAIN`; do not infer permission. |
| Critical-infrastructure precision or reconstruction risk | `DENY` by default; require governed aggregation/redaction and review. |
| Source outage | `UNAVAILABLE` / `ABSTAIN`; show outage state and do not imply safety. |
| Partial feed | `PARTIAL` / `ABSTAIN` for completeness claims. |
| Stale cache with no released alternative | `STALE` / `ABSTAIN`; never silently relabel as current. |
| Conflicting official records | `HOLD` or `ABSTAIN`; preserve conflict and source lineage. |
| Consumer cannot determine precedence | `ERROR` or `HOLD`; do not merge unpredictably. |
| Sensitive value, secret, or live binding detected | `FAIL`; remove, assess exposure, rotate/revoke if necessary. |

`PASS` and `FAIL` are validator outcomes, not warning, policy, release, publication, or life-safety decisions.

[Back to top](#top)

---

## Review burden

README changes require:

- configuration or documentation review;
- Hazards domain review; and
- public-safety boundary review.

A future payload also requires the applicable:

- named consumer owner;
- official-source and jurisdiction reviewer;
- freshness and temporal-semantics reviewer;
- source-role and evidence reviewer;
- rights and attribution reviewer;
- sensitivity and critical-infrastructure reviewer;
- schema or contract reviewer;
- validation and test reviewer;
- security and privacy reviewer;
- accessibility and disclaimer-presentation reviewer; and
- policy and release reviewer.

No reviewer may approve KFM as an alert authority through this lane. The permanent boundary is not a discretionary review choice.

Do not infer acceptance from a missing reviewer rule or placeholder `CODEOWNERS` entry. Owners remain `OWNER_TBD` until verified.

[Back to top](#top)

---

## Maintenance and safe change pattern

When a Hazards configuration file is added or changed:

1. identify the exact contextual consumer and owner;
2. re-read the parent config contract and Hazards doctrine;
3. verify the canonical contract, schema, policy, registry, official-source, and source-rights references;
4. preserve the seven source roles and hazard-object distinctions;
5. preserve the permanent not-for-life-safety boundary;
6. verify issue, expiry, observed, valid, retrieval, release, correction, and timezone semantics;
7. review stale, partial, unavailable, superseded, correction, and outage behavior;
8. review rights, disclaimer, official redirect, sensitivity, infrastructure, join, low-count, and reconstruction risk;
9. run deterministic parse, shape, semantic, negative, and no-network checks;
10. document precedence, unknown-key behavior, migration, deactivation, correction, and rollback;
11. inspect the complete diff for secrets, live bindings, current operational content, action guidance, exact locations, and protected clues;
12. verify remote read-back and changed paths; and
13. keep evidence, policy, warning authority, release, and publication as separate governed concerns.

### Change-budget discipline

A configuration PR should not silently add or alter:

- source activation, polling, or network behavior;
- alerting, notifications, dispatch, escalation, or incident workflows;
- official-source authority or jurisdiction;
- contracts or schemas;
- freshness thresholds without source-owner review;
- not-for-life-safety policy or disclaimer language;
- critical-infrastructure exposure policy;
- connectors, watchers, or pipeline logic;
- lifecycle data;
- receipts or proofs;
- release decisions;
- public routes, map layers, exports, or notification surfaces.

Those changes require their own scoped implementation and review surfaces.

[Back to top](#top)

---

## Migration and anti-bypass posture

If misplaced material is found here:

1. do not treat it as authoritative merely because it is committed;
2. classify it as safe config, alert/action material, secret/live binding, contract, schema, policy, registry, source payload, package code, pipeline/connector/watcher code, runtime/infra, lifecycle object, trust artifact, release record, public artifact, generated output, or sensitive detail;
3. remove or quarantine credentials, live bindings, current operational instructions, exact infrastructure details, and protected context immediately;
4. rotate or revoke exposed credentials and messaging secrets as required;
5. move machine shape to `schemas/`;
6. move semantic meaning to `contracts/`;
7. move not-for-life-safety, admissibility, freshness, and sensitivity rules to `policy/`;
8. move source identity and activation state to registry/connector governance;
9. move implementation to packages, pipelines, connectors, runtime, apps, tools, or infrastructure as appropriate;
10. move lifecycle, catalog, receipt, proof, and published material to canonical `data/` lanes;
11. move release, correction, withdrawal, supersession, and rollback decisions to `release/`;
12. preserve provenance, consumer impact, migration reason, exposure assessment, and rollback instructions;
13. create a drift, correction, or incident record when misplaced material was consumed or exposed.

### Anti-bypass matrix

| Bypass risk | Required response |
|---|---|
| Config treated as alert authority | Reject permanently; KFM is contextual only. |
| Config creates or modifies an official warning | Reject; official authorities own operational products. |
| Config triggers notification, dispatch, or escalation | Reject and move implementation out of scope; assess public-safety risk. |
| Config suppresses disclaimer or official redirect | Reject; public use denied. |
| Config extends expired context | Reject; preserve expired/historical state. |
| Config treats missing data as safety | Reject; absence or outage is not an all-clear. |
| Config treated as policy authority | Reject; policy remains authoritative. |
| Config duplicates contract or schema | Move meaning/shape to the canonical root and keep only references here. |
| Directory presence activates a feed | Reject; require explicit verified source and consumer binding. |
| Config contains exact infrastructure context | Remove, assess exposure, and route through sensitivity/correction governance. |
| Client-side style hides protected geometry | Reject; aggregate, redact, restrict, or deny before public artifact generation. |
| Config writes catalog, receipt, proof, or release records | Reject and move to canonical trust/release homes. |
| Public client reads this directory | Reject; public access must cross the governed API and released artifacts. |
| Watcher publishes from config | Reject; watchers may propose candidates and receipts only. |
| Model or detection presented as confirmation | Reject; preserve method, role, uncertainty, time, and evidence. |

[Back to top](#top)

---

## Definition of done for the first payload

- [ ] A named contextual consumer and accepted owners are verified.
- [ ] The file format, version, parser, and explicit load path are verified.
- [ ] Canonical schema, contract, policy, registry, doctrine, and official-source references resolve.
- [ ] Precedence, duplicate-key, missing-file, and unknown-key behavior are documented and tested.
- [ ] Network, polling, alerting, notification, dispatch, and escalation behavior remain disabled and out of scope.
- [ ] The seven source-role classes remain explicit and non-interchangeable.
- [ ] Event, observation, warning/advisory context, declaration, detection, model, aggregate, exposure, resilience, and impact-area roles remain distinct.
- [ ] Expired operational context cannot appear current.
- [ ] Stale, partial, unavailable, superseded, corrected, and unknown states remain visible.
- [ ] The not-for-life-safety disclaimer cannot be disabled or hidden.
- [ ] An accepted jurisdiction-appropriate official-source redirect profile is present.
- [ ] No KFM-authored emergency instruction or all-clear language can be emitted.
- [ ] Spatial, temporal, uncertainty, freshness, correction, and supersession semantics are explicit.
- [ ] Rights, attribution, and redistribution terms are reviewed.
- [ ] Critical-infrastructure and public-safe aggregation parameters come from accepted policy profiles, not ad hoc config values.
- [ ] Join-induced sensitivity, low counts, differencing, repeated-query, and reconstruction risks are tested.
- [ ] Synthetic fixtures cover valid, invalid, held, denied, abstained, stale, expired, partial, unavailable, corrected, superseded, and error cases.
- [ ] No-network tests pass.
- [ ] Secret, private-endpoint, messaging, personal-path, action-guidance, live-event, and protected-context scans pass.
- [ ] Migration, deactivation, correction, withdrawal, and rollback behavior are tested.
- [ ] No source, feed, alert, notification, public layer, API route, release, or publication is activated by file presence.
- [ ] Repository-native checks are substantive or their scaffold limitations are stated explicitly.

[Back to top](#top)

---

## Related folders

- [`../README.md`](../README.md) — parent domain-configuration contract.
- [`../../README.md`](../../README.md) — repository-wide configuration boundary.
- [`../../../docs/domains/hazards/README.md`](../../../docs/domains/hazards/README.md) — Hazards doctrine, permanent not-for-life-safety boundary, source roles, freshness, sensitivity, and lifecycle posture.
- [`../../../docs/registers/DOMAIN_LANE.md`](../../../docs/registers/DOMAIN_LANE.md) — canonical lane and sensitivity register.
- [`../../../docs/registers/DRIFT_REGISTER.md`](../../../docs/registers/DRIFT_REGISTER.md) — unresolved path and authority drift.
- [`../../../docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) — placement and responsibility law.
- [`../../../docs/security/SECRETS.md`](../../../docs/security/SECRETS.md) — credential and sensitive-value handling.

Future files should link to verified Hazards contracts, schemas, policies, source descriptors, official-source profiles, freshness profiles, tests, fixtures, receipts, proofs, and release records only after those exact paths and authority relationships are confirmed.

[Back to top](#top)

---

## ADRs and drift triggers

No ADR is introduced by this README.

Separate governance is required for changes that would:

- add, rename, merge, or retire a canonical domain slug;
- change the permanent not-for-life-safety or alert-authority-denied boundary;
- change the seven source-role vocabulary or permit role upgrades;
- equate warning context with KFM-issued alerting;
- permit expired context to appear current;
- define or alter freshness thresholds, official-source authority, disclaimer requirements, sensitivity tiers, infrastructure aggregation, low-count rules, or public-safe geometry policy;
- decide source rights, source authority, live-source activation, or connector cadence;
- establish alerting, notification, dispatch, escalation, or incident-command behavior;
- resolve segment-versus-shorthand lane paths or Hazards release-policy path alternatives;
- establish universal config discovery, precedence, or unknown-key behavior;
- create a parallel contract, schema, policy, registry, receipt, proof, warning, or release authority;
- authorize direct public access to internal or canonical stores;
- change lifecycle, evidence, correction, withdrawal, promotion, or release separation; or
- introduce a direct public route to configuration material.

Configuration must not be used to settle these decisions indirectly.

[Back to top](#top)

---

## Rollback and correction

Before merge, rollback means closing the unmerged pull request and abandoning the scoped branch when separately authorized.

After merge, create a transparent revert commit or revert pull request that restores the prior known-good README or configuration version. Do not force-push or rewrite shared history.

For a future payload correction:

1. disable or stop selecting the affected configuration through the verified consumer mechanism;
2. stop any connector, watcher, poller, renderer, notification component, scheduled process, export, or public-output workflow that depends on the faulty selection;
3. preserve the faulty version and evidence needed for review;
4. identify affected objects, joins, source records, caches, tiles, indexes, exports, screenshots, notifications, and narratives without exposing protected locations;
5. assess whether KFM appeared to issue an alert, action instruction, all-clear, or official determination;
6. assess whether source roles, official authority, warning validity, temporal semantics, evidence status, or freshness were collapsed;
7. assess whether exact or reconstructable infrastructure or private information was exposed;
8. restore the prior known-good version or safe disabled state;
9. re-run validation and negative cases;
10. create any required correction, withdrawal, incident, redaction, release, or rollback records in their canonical homes; and
11. verify that no public surface continues to serve an unauthorized, stale, expired-as-current, actionable, misclassified, or reconstructable derivative.

A Git revert does not itself retract notifications, correct caches or exports, revoke exposed information, replace an official correction, or establish KFM publication lineage.

[Back to top](#top)

---

## Safe language rules

Use language such as:

- “Hazards contextual configuration for a named consumer”;
- “not for life safety”;
- “KFM does not issue alerts”;
- “official-source redirect required”;
- “official warning context, not KFM warning”;
- “historical context”;
- “expired operational context”;
- “stale or partial source state”;
- “modeled, not observed”;
- “detection, not confirmation”;
- “public-safe exposure summary”;
- “configuration aid, not authority”;
- “bounded search found no indexed executable consumer.”

Avoid unsupported or unsafe claims such as:

- “KFM warns you”;
- “KFM says it is safe”;
- “there is no danger”;
- “take action based on this layer”;
- “this is the current official alert” without direct official verification and contextual framing;
- “the feed is complete”;
- “no record means no hazard”;
- “this model confirms the event”;
- “this detection is a verified incident”;
- “this declaration proves current local impact”;
- “the Hazards pipeline uses this config” without implementation evidence;
- “this file activates the source or notifications”;
- “this config is validated by CI” when the workflow is only scaffolding;
- “this setting authorizes public display”;
- “this config replaces policy”;
- “this folder contains the complete operational Hazards configuration.”

[Back to top](#top)

---

## Last reviewed

**2026-07-14**, against `main@2a060759170e94a8c5827c0a8c460d7488c8fea2`.

Review again before the first non-README payload, consumer binding, loader or precedence decision, official-source profile, freshness profile, source-role profile, sensitivity/infrastructure profile, live-source activation, contextual public-output integration, or any notification-adjacent implementation.

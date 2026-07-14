<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-domains-hydrology-readme
title: configs/domains/hydrology/ — Hydrology Configuration Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Config steward · Hydrology steward · Measurement/identity reviewer · Public-safety reviewer · Consumer owner · Validation steward
created: 2026-07-13
updated: 2026-07-14
policy_label: public; config-sublane; hydrology; evidence-bound; source-role-aware; measurement-aware; freshness-aware; not-for-life-safety; private-property-aware; non-secret; non-authoritative; no-live-binding
current_path: configs/domains/hydrology/README.md
truth_posture: CONFIRMED canonical hydrology slug, repository-present parent config contract, repository-present Hydrology doctrine, NFHL-as-regulatory-context-only rule, observed/regulatory/modeled/aggregate/administrative/candidate anti-collapse posture, ambiguous-reach ABSTAIN rule, operational-warning non-authority, watcher-as-non-publisher rule, and documentation-only lane / CONFLICTED Directory-Rules domain-segment form versus Atlas flat-form navigation and canonical role-class mapping versus older authority-observation-context-model wording / PROPOSED future consumer-bound templates and governed profile selectors / UNKNOWN consumers, loader behavior, precedence, deployment binding, and enforcement / NEEDS VERIFICATION owners, executable validation, source rights, role-vocabulary mapping, freshness thresholds, measurement-conversion profiles, identity-crosswalk rules, public-safe well and infrastructure parameters, official-source redirect profiles, and runtime binding
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: b46db8e827d1ba851534568cbb16f76e78af5072
  prior_blob: 7bc5e829a374d9ace13bb7341d57d778b7cfc80a
  bounded_search_result: configs/domains/hydrology/README.md only
related:
  - ../README.md
  - ../../README.md
  - ../../../docs/domains/hydrology/README.md
  - ../../../docs/registers/DOMAIN_LANE.md
  - ../../../docs/registers/DRIFT_REGISTER.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/security/SECRETS.md
notes:
  - "This lane contains documentation only in the bounded path search. No executable Hydrology configuration payload, consumer, loader, source activation, network fetch, warning function, model execution, or publication binding is established."
  - "A bounded repository search for configs/domains/hydrology returned this README and no indexed executable consumer. This is bounded evidence, not proof that no differently named or unindexed consumer exists."
  - "v0.2 expands the Hydrology-specific source-role, NFHL, measurement, reach-identity, freshness, private-property, infrastructure, validation, correction, and rollback contract without creating policy, schema, source, model, warning, release, or public-surface authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology Domain Configuration

`configs/domains/hydrology/`

> Safe-to-commit, Hydrology-specific configuration documentation and future consumer-bound templates. This lane does not own hydrologic truth, source admission, flood-warning authority, measurement validity, identity resolution, sensitivity, evidence, release, or publication.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Scope](#scope) · [Repository fit](#repository-fit) · [Inputs](#inputs) · [Outputs](#outputs) · [File contract](#minimum-configuration-contract) · [Consumer binding](#consumer-binding-precedence-and-discovery) · [Source roles](#hydrology-semantic-and-source-role-guardrails) · [Measurements](#measurement-spatial-and-identity-contract) · [Time and freshness](#temporal-freshness-and-stale-state-contract) · [NFHL and warnings](#nfhl-flood-context-and-life-safety-boundary) · [Cross-lane rules](#cross-lane-ownership-and-context-rules) · [Sensitivity](#private-property-infrastructure-and-reconstruction-risk) · [Validation](#validation) · [Failure behavior](#failure-behavior) · [AI](#governed-ai-and-generated-language) · [Review](#review-burden) · [Maintenance](#maintenance-and-safe-change-pattern) · [Migration](#migration-and-anti-bypass-posture) · [Done](#definition-of-done-for-the-first-payload) · [Related](#related-folders) · [ADRs](#adrs-and-drift-triggers) · [Rollback](#rollback-and-correction) · [Language](#safe-language-rules)

> [!IMPORTANT]
> **Document lifecycle:** draft `v0.2`  
> **Observed lane maturity:** README-only in the bounded path search; no executable Hydrology configuration payload is established  
> **Authority:** implementation-supporting configuration sublane; non-authoritative for truth and governance  
> **Runtime posture:** no loader, consumer binding, source activation, polling, model execution, warning delivery, public layer, release, or publication is established by this README

> [!CAUTION]
> **NFHL is regulatory flood context, not observed inundation.** An observed gauge reading is not a forecast, a modeled hydrograph is not an observation, an aggregate HUC summary is not site truth, and KFM is not an emergency flood-warning system. Configuration must preserve those distinctions and fail closed when role, identity, time, rights, or sensitivity is unresolved.

---

## Purpose

This directory defines the safe-to-commit configuration boundary for the canonical Hydrology lane.

It may eventually hold small defaults, templates, examples, or review-oriented settings for a **named and verified consumer**. Those files may describe how that consumer should parse, display, validate, or select already-governed Hydrology material, but they cannot decide:

- whether a watershed, HUC unit, reach, gauge, well, observation, hydrograph, flood zone, flood event, or cross-lane link is true;
- whether a source is authoritative, admissible, licensed, current, or active;
- whether an NFHL polygon represents observed or forecast flooding;
- whether a reach identity crosswalk is defensible;
- whether a parameter, unit conversion, qualifier, datum, or no-data value is valid;
- whether a modeled or reconstructed series may be represented as observed;
- whether stale or unavailable data supports a current claim;
- whether private-well, water-right, dam, utility, or infrastructure detail may be exposed;
- whether evidence supports a hydrologic claim;
- whether a user should take emergency action; or
- whether an artifact may be promoted, released, or published.

This README is intended for:

- Hydrology domain stewards;
- configuration and developer-experience maintainers;
- source-role, measurement, identity, freshness, rights, sensitivity, policy, security, public-safety, and release reviewers;
- package, pipeline, app, runtime, test, watcher, connector, and tooling owners that may consume Hydrology configuration; and
- reviewers checking Directory Rules placement and trust-membrane integrity.

[Back to top](#top)

---

## Authority level

**Configuration-supporting and non-authoritative.**

| Concern | Authority in this lane |
|---|---|
| Hydrology domain meaning | **None.** Domain doctrine remains in [`docs/domains/hydrology/`](../../../docs/domains/hydrology/README.md). |
| Watershed, HUC, reach, site, or object identity | **None.** Configuration cannot create canonical identity or resolve ambiguity by convenience. |
| Gauge, flow, level, water-quality, or aquifer observation truth | **None.** Configuration cannot establish evidentiary status or alter source qualifiers. |
| NFHL or regulatory status | **None.** Configuration cannot turn regulatory context into observed inundation, forecast flooding, or a current warning. |
| Model or reconstruction truth | **None.** Configuration cannot convert a modeled hydrograph, terrain-derived surface, estimate, or candidate into an observation. |
| Emergency warning or life-safety guidance | **Permanently none.** KFM cannot become a flood-warning or evacuation authority through configuration. |
| Source identity, role, rights, cadence, and activation | **None.** These require applicable registry, connector, rights, policy, and review surfaces. |
| Parameter, unit, datum, qualifier, or conversion authority | **None.** A file may select an accepted profile; it cannot invent scientific meaning or silently convert values. |
| Freshness or expiry decision | **Supporting only.** A verified consumer may select an accepted per-source profile; configuration cannot extend source validity or hide stale state. |
| Schema or contract shape | **None.** Configuration may reference verified schemas and contracts but must not duplicate or redefine them. |
| Sensitivity, redaction, aggregation, or public-safe geometry | **None.** A value may select an accepted profile; it cannot create, weaken, or approve a rule. |
| Evidence or claim truth | **None.** Configuration cannot create an `EvidenceBundle`, validate a claim, or make generated interpretation sovereign truth. |
| Release or publication | **None.** Configuration cannot authorize promotion, release, public display, or KFM publication. |
| Consumer behavior | **Supporting only.** A verified consumer may read a validated file under an explicit binding and precedence rule. |

A configuration value may point to an authority surface. It does not become authority through repetition, proximity, successful parsing, operational convenience, apparent freshness, or use by a map, hydrograph, dashboard, Evidence Drawer, Focus Mode, export, or AI surface.

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
| Base commit | `b46db8e827d1ba851534568cbb16f76e78af5072` |
| Prior README blob | `7bc5e829a374d9ace13bb7341d57d778b7cfc80a` |
| Bounded path-search result | `configs/domains/hydrology/README.md` only |

### Maturity matrix

| Item | State | Safe conclusion |
|---|---:|---|
| Canonical domain slug | **CONFIRMED** | `hydrology` is a repository-present canonical domain lane. |
| Parent configuration contract | **CONFIRMED** | [`configs/domains/README.md`](../README.md) defines this path as a non-secret, non-authoritative configuration sublane. |
| Hydrology doctrine | **CONFIRMED repository-present** | The domain README establishes evidence-bound time semantics, NFHL role separation, identity ambiguity handling, freshness, publication gates, and non-alert authority. |
| NFHL role | **CONFIRMED — REGULATORY CONTEXT ONLY** | NFHL may not be labeled as observed inundation, forecast flooding, or current conditions. |
| Ambiguous reach identity | **CONFIRMED — ABSTAIN** | Multiple or unsupported reach mappings cannot be resolved by a default or “first match” rule. |
| Life-safety posture | **CONFIRMED — DENY** | KFM cannot provide flood warnings, evacuation instructions, or other life-safety replacement. |
| Current lane content | **README ONLY IN BOUNDED SEARCH** | No executable payload, consumer, or activation path was found by the path-scoped search. Exhaustive inventory remains `NEEDS VERIFICATION`. |
| Indexed executable consumer | **NOT FOUND IN BOUNDED SEARCH** | Differently named or unindexed consumers remain `UNKNOWN`. |
| Consumer and loader | **UNKNOWN** | No parser, auto-discovery mechanism, merge order, precedence, or unknown-key behavior is established here. |
| Role vocabulary mapping | **CONFLICTED / NEEDS VERIFICATION** | Repository-wide classes and older Hydrology `authority / observation / context / model` wording must be reconciled by governance, not configuration. |
| Path form | **CONFLICTED / GOVERNED BY DIRECTORY RULES FOR THIS README** | Directory Rules uses a `domains/hydrology/` segment; Atlas flat-form navigation remains a drift/ADR matter. |
| Source rights and terms | **NEEDS VERIFICATION** | Source-specific rights, attribution, redistribution, cadence, rate limits, and access restrictions require verified source records. |
| Freshness profiles | **NEEDS VERIFICATION** | Per-source latency, stale, partial, outage, and supersession thresholds require source-owner review. |
| Measurement and conversion profiles | **NEEDS VERIFICATION** | Parameter, unit, datum, qualifier, rounding, and conversion behavior must be governed and tested. |
| Identity crosswalk rules | **NEEDS VERIFICATION** | HUC and reach-vintage crosswalks require explicit methods, evidence, confidence, and ambiguity outcomes. |
| Public-safe well and infrastructure parameters | **NEEDS VERIFICATION** | Aggregation, masking, suppression, and precision limits must come from policy and steward review. |
| Validation and CI enforcement | **NEEDS VERIFICATION** | Expectations are documented; substantive executable enforcement is not proven by this README. |
| Runtime, release, and publication | **NOT ESTABLISHED** | Nothing in this lane authorizes operational use, source access, warnings, release, or publication. |

Directory presence must not trigger config discovery, source activation, polling, network access, model execution, identity resolution, unit conversion, warning delivery, geofencing, map-layer creation, lifecycle promotion, or publication.

[Back to top](#top)

---

## Scope

### What belongs here

Only safe, non-secret, Hydrology-specific configuration material for a named or explicitly proposed consumer belongs here.

| Material | Permitted purpose | Minimum posture |
|---|---|---|
| `README.md` | Define this configuration boundary. | Preserve non-authority, role separation, measurement integrity, freshness, sensitivity, evidence, and release controls. |
| `*.template.yaml` or `*.template.yml` | Placeholder-based template for a verified Hydrology consumer. | Parseable, versioned, consumer-bound, no secrets, no live binding, no network activation. |
| `*.example.yaml`, `*.example.json`, or `*.example.toml` | Tiny illustrative configuration. | Clearly synthetic values; impossible IDs, coordinates, site numbers, and observations; no automatic activation. |
| Conservative review defaults | Select an existing hold, abstain, deny, stale, contextual, or review profile. | Cannot waive policy, rights, evidence, or release burden. |
| Source-role profile selectors | Select an already-governed role-display or validation profile. | Cannot upgrade or relabel a claim. |
| Freshness-profile selectors | Select an accepted per-source freshness profile. | Cannot override source timestamps, silently extend validity, or suppress stale state. |
| Measurement-display profile selectors | Select accepted unit, precision, datum-label, qualifier, or no-data presentation behavior. | Cannot alter source values or perform hidden scientific conversion. |
| Identity-resolution profile selectors | Select a verified crosswalk or ambiguity policy. | Ambiguity must remain visible; no convenience fallback. |
| Public-safe display profile selectors | Select accepted generalization or aggregation for wells, dams, infrastructure, or private-property implications. | Cannot contain protected detail or authorize exposure. |
| Presentation hints | Configure role badges, vintages, time labels, stale banners, uncertainty, caveats, or provenance display. | Must not change evidence status, validity, sensitivity, or authority. |
| Migration notes | Document a real key, version, consumer, or path transition. | Time-bounded, owner-linked, reversible, and not a parallel authority. |
| Validation notes | Describe verified checks and finite outcomes. | Commands and workflows must resolve or remain labeled `PROPOSED` / `NEEDS VERIFICATION`. |

Synthetic examples must not resemble a real private well, water-right holder, dam interior, utility asset, active gauge event, warning polygon, regulated facility, or sensitive property closely enough to support confusion or reconstruction.

### What does not belong here

- real gauge, flow, water-level, water-quality, aquifer, well, hydrograph, flood-event, NFHL, source, or lifecycle payloads;
- credentials, API keys, private endpoints, signed URLs, internal hostnames, workstation paths, deployment bindings, or environment-specific secrets;
- current flood warnings, watches, emergency alerts, evacuation instructions, road-closure directions, protective-action guidance, or all-clear language;
- exact or reconstructable private-well, well-owner, water-right owner, dam-internal, utility, treatment, intake, outfall, or resilience-critical infrastructure detail;
- settings that label NFHL as observed inundation, a forecast, or a current warning;
- settings that label a modeled or reconstructed hydrograph as observed;
- settings that treat an HUC aggregate as per-site truth;
- settings that resolve ambiguous reaches by first match, nearest geometry, or silent best effort;
- settings that silently change units, datums, qualifiers, parameter meanings, provisional status, or no-data values;
- settings that treat missing, delayed, or unavailable data as safety or normal conditions;
- source admission, activation, cadence, rights, redistribution, or role decisions;
- schemas, contracts, policy rules, registry rows, receipts, proofs, evidence bundles, release records, correction notices, or publication decisions;
- package code, pipeline logic, connector or watcher code, runtime adapters, infrastructure definitions, generated artifacts, caches, exports, screenshots, or reports.

[Back to top](#top)

---

## Repository fit

`configs/domains/hydrology/` is the Hydrology segment under the `configs/` responsibility root.

| Responsibility | Canonical or proposed home | Relationship to this lane |
|---|---|---|
| Repository-wide configuration boundary | [`configs/README.md`](../../README.md) | Parent no-secrets and no-live-binding contract. |
| Domain configuration boundary | [`configs/domains/README.md`](../README.md) | Parent no-authority and consumer-binding contract. |
| Human-facing Hydrology doctrine | [`docs/domains/hydrology/`](../../../docs/domains/hydrology/README.md) | Defines lane meaning and governance posture. |
| Semantic object meaning | `contracts/domains/hydrology/` | Referenced only after exact paths and authority are verified. |
| Machine shape | `schemas/contracts/v1/domains/hydrology/` | Referenced only after exact paths and versions are verified. |
| Admissibility and exposure policy | `policy/domains/hydrology/` | Owns allow, restrict, deny, abstain, role, freshness, and sensitivity decisions. |
| Source identity and activation | `data/registry/sources/hydrology/`, connectors, pipeline specs | Configuration cannot admit or activate sources. |
| Reusable implementation | `packages/domains/hydrology/` | May consume config after explicit binding; configuration does not replace code. |
| Pipeline implementation | `pipelines/domains/hydrology/`, `pipeline_specs/hydrology/` | May consume config after explicit binding; presence does not imply execution. |
| Tests and fixtures | `tests/domains/hydrology/`, `fixtures/domains/hydrology/` | Own enforceability and deterministic examples. |
| Lifecycle data | `data/<phase>/hydrology/` | Never stored in this configuration lane. |
| Receipts and proofs | `data/receipts/`, `data/proofs/` | Trust-bearing objects remain outside configuration. |
| Release and rollback | `release/candidates/hydrology/`, canonical release homes | Configuration cannot create a release decision. |
| Public delivery | governed API and released public artifacts | Public clients must not read this directory as a data surface. |

### Path-form conflict

Directory Rules uses the domain-segment form, including `contracts/domains/hydrology/` and `schemas/contracts/v1/domains/hydrology/`. Older Atlas navigation uses flat forms such as `contracts/hydrology/`.

This README follows Directory Rules for references and records the disagreement as `CONFLICTED`. A future configuration change must not:

- create both path forms;
- add compatibility aliases without an accepted migration decision;
- infer that a path is authoritative because a similarly named directory exists; or
- resolve the conflict through consumer precedence.

[Back to top](#top)

---

## Inputs

A future Hydrology configuration file may consume only explicit, safe, inspectable configuration inputs such as:

- a named consumer ID and owning component;
- a format and configuration version;
- verified contract, schema, policy, registry, and doctrine references;
- accepted profile IDs for role display, freshness, measurements, identity ambiguity, public-safe geometry, review, or stale-state handling;
- source-independent presentation defaults;
- synthetic fixture IDs and impossible example values;
- local-override placeholders that contain no real path, endpoint, credential, site ID, owner identity, or sensitive geometry; and
- migration and rollback metadata.

A configuration input is not a source record, observation, warning, forecast, model output, identity decision, policy decision, receipt, proof, or release record.

[Back to top](#top)

---

## Outputs

This lane currently outputs **documentation only**.

A future verified file may provide:

- validated settings for one named consumer;
- a conservative profile selection;
- display and caveat preferences;
- an explicit hold, abstain, or stale-state default;
- a deterministic parser input; or
- migration metadata.

A file here must not output or trigger:

- a source fetch or network request;
- a gauge observation, hydrograph, flood polygon, HUC object, reach match, or well record;
- a warning, alert, notification, evacuation instruction, or all-clear message;
- an identity, unit, datum, or scientific validity decision;
- a redaction, aggregation, evidence, review, promotion, release, correction, or publication record;
- a public API response, map tile, layer manifest, index, cache, report, or export; or
- durable writes outside the verified consumer's configuration state.

[Back to top](#top)

---

## Minimum configuration contract

Before the first non-README file is accepted, it should document or encode the following fields. Exact key names remain `PROPOSED` until a schema and consumer are verified.

| Contract item | Required information |
|---|---|
| Status | Draft, example, template, or active-for-named-consumer state. |
| Owner | Named configuration owner and consumer owner; no placeholder at activation. |
| Intended consumer | Exact package, pipeline, app, runtime, test, or tool expected to read the file. |
| Binding evidence | Loader path, parser entrypoint, deployment selection, or test proving explicit use. |
| Format and version | YAML, JSON, TOML, or other format plus configuration version. |
| Contract and schema references | Exact verified IDs or paths; no copied machine authority. |
| Policy references | Exact role, freshness, sensitivity, public-safe geometry, rights, and life-safety controls. |
| Source-role handling | Accepted role profile and behavior for unknown, conflicting, or missing role. |
| Measurement handling | Parameter, unit, datum, qualifier, precision, no-data, and conversion profile references. |
| Identity handling | HUC/reach/site identifier rules, source vintage, crosswalk method, confidence, and ambiguity outcome. |
| Spatial handling | CRS, source scale/resolution, geometry type, precision, and generalization-profile reference. |
| Temporal handling | Source, observed, valid, issue, expiry, retrieval, release, correction, and supersession semantics. |
| Freshness handling | Accepted profile ID, stale/partial/outage behavior, and visible disclosure requirements. |
| Sensitivity handling | Private-property, well, owner, dam, utility, infrastructure, join, and reconstruction controls. |
| Warning boundary | Explicit non-alert posture and behavior for operational-warning context. |
| Unknown-key behavior | Reject or hold by default; never silently ignore consequential keys. |
| Missing-file behavior | Fail closed, remain disabled, or use a verified safe built-in default. |
| Duplicate-key behavior | Deterministic rejection unless the parser contract explicitly governs duplicates. |
| Precedence | Complete order among built-in, repository, environment, local, CLI, and deployment layers. |
| Local override | Ignored, documented mechanism for real local values; never commit them here. |
| Network behavior | Disabled during validation and disabled by file presence. |
| Validation | Deterministic parse, shape, semantic, negative, sensitivity, and no-network checks. |
| Finite failures | Recorded hold, abstain, deny, or error behavior; no permissive fallback. |
| Deactivation | How the consumer stops selecting the file without deletion or history rewriting. |
| Migration | Compatibility window, old/new keys, owner, removal condition, and rollback. |
| Rollback | Prior known-good version, restoration steps, dependent cache/output review, and correction path. |

### Safe placeholders

Use unmistakably synthetic placeholders such as:

```text
<HYDROLOGY_CONSUMER_ID>
<VERIFIED_SCHEMA_REF>
<VERIFIED_POLICY_PROFILE>
<ACCEPTED_FRESHNESS_PROFILE>
<ACCEPTED_MEASUREMENT_PROFILE>
<ACCEPTED_IDENTITY_PROFILE>
<PUBLIC_SAFE_GEOMETRY_PROFILE>
<LOCAL_ONLY_OVERRIDE>
```

Do not use realistic gauge IDs, COMIDs, HUC codes tied to a sensitive example, private-well IDs, owner names, active warning IDs, coordinates, endpoints, or credentials as placeholders.

[Back to top](#top)

---

## Consumer binding, precedence, and discovery

No configuration file in this directory is active merely because it exists.

A verified consumer binding must establish:

1. the exact file path;
2. the parser and supported format/version;
3. the component and owner;
4. when loading occurs;
5. whether loading is mandatory or optional;
6. the complete precedence order;
7. duplicate-key and unknown-key behavior;
8. missing, unreadable, invalid, and stale-file behavior;
9. whether reload is supported and how atomicity is preserved;
10. deactivation and rollback behavior; and
11. tests proving that directory presence alone does not activate sources, network calls, models, warnings, or public outputs.

### Required defaults before verification

Until binding is verified:

- auto-discovery is **off**;
- recursive loading is **off**;
- network access is **off**;
- source activation is **off**;
- model execution is **off**;
- public exposure is **off**;
- unknown keys cause hold or rejection;
- invalid values cause hold or rejection;
- missing configuration leaves the proposed feature disabled; and
- no fallback may weaken role, rights, evidence, freshness, sensitivity, or warning controls.

Environment variables, CLI arguments, local overrides, and deployment values do not automatically outrank repository configuration. Precedence must be explicit, deterministic, documented, and tested.

[Back to top](#top)

---

## Hydrology semantic and source-role guardrails

Hydrology must preserve source role as a first-class claim attribute. Promotion, display convenience, consumer preference, and model confidence do not upgrade role.

### Role vocabulary boundary

Repository-wide doctrine uses role classes such as `observed`, `regulatory`, `modeled`, `aggregate`, `administrative`, `candidate`, and `synthetic`. Older Hydrology text also uses `authority`, `observation`, `context`, and `model` wording.

The exact machine mapping is `NEEDS VERIFICATION` and may be `CONFLICTED`. Configuration must not:

- invent aliases;
- map `authority` to `regulatory` or `observed` without an accepted contract;
- treat `context` as a weaker validation state rather than a claim role;
- upgrade a candidate through successful parsing; or
- create a second role vocabulary.

### Anti-collapse matrix

| Claim or product | Must not become | Required posture |
|---|---|---|
| USGS gauge reading | Forecast, regulatory zone, model, or warning | Preserve parameter, unit, qualifier, provisional status, site, and observed time. |
| NFHL zone | Observed inundation, current condition, forecast, or warning | Label as regulatory context with source vintage and evidence. |
| Modeled or reconstructed hydrograph | Observed time series | Preserve model version, inputs, method, intended use, uncertainty, and run evidence. |
| HUC or watershed aggregate | Per-site or per-property truth | Preserve aggregation unit, support, time, source set, and receipt reference. |
| Administrative water-right or well roster | Observed flow, use, ownership proof, or event timeline | Preserve administrative status and applicable privacy/rights limits. |
| Candidate reach crosswalk | Resolved `ReachIdentity` | Record candidates, evidence, confidence, and `ABSTAIN` when ambiguous. |
| Terrain-derived drainage or inundation product | Official hydrography, observation, or regulatory designation | Preserve derived/modeled role, source resolution, method, and limitations. |
| Historical observed flood evidence | Current warning or forecast | Preserve historical time and explicit non-current status. |
| Synthetic fixture | Real site, observation, event, or source record | Use impossible values and synthetic labeling on every surface. |
| Operational warning context | KFM-issued alert or life-safety instruction | Context only, time-bounded, cited, and redirected to official authorities. |

Role mismatch is a **publication-blocking condition**, not a cosmetic quality issue.

[Back to top](#top)

---

## Measurement, spatial, and identity contract

### Measurement integrity

A future measurement-related configuration must reference governed behavior for:

- source parameter code and human label;
- source unit and display unit;
- conversion formula and version, when conversion is permitted;
- significant figures and rounding;
- vertical datum and reference datum;
- site datum and datum offsets;
- qualifiers, approvals, provisional status, censoring, and estimated values;
- no-data, missing, ice, equipment, and invalid-value codes;
- method and instrument context where material;
- uncertainty, precision, and support interval; and
- source-native value preservation.

Configuration must never:

- change a parameter's scientific meaning;
- assume unit compatibility from a field name;
- perform an undocumented conversion;
- discard qualifiers or provisional state;
- convert a no-data sentinel into zero;
- mix stage, discharge, elevation, depth, concentration, or withdrawal values;
- hide datum differences; or
- present converted precision beyond source support.

### Spatial integrity

A future spatial configuration must preserve:

- source CRS and output CRS;
- axis order;
- geometry type;
- source scale and resolution;
- horizontal and vertical accuracy;
- HUC digit level;
- source vintage;
- generalization or simplification profile;
- clipping boundary;
- topology expectations; and
- public-safe geometry class.

Client-side style, opacity, zoom, clustering, hidden properties, or popup omission is not a sensitivity control and does not change the underlying geometry class.

### Identity integrity

A future identity configuration must preserve:

- source identifier and source vintage;
- HUC code and declared digit level;
- reach or feature identifier namespace;
- site identifier namespace;
- crosswalk method and version;
- candidate set;
- confidence or decision reason;
- topology and geometry checks;
- temporal validity;
- supersession lineage; and
- ambiguity outcome.

When multiple reach mappings remain defensible, the correct outcome is `ABSTAIN` or hold for review. Configuration must not select the first, nearest, longest, newest, or most convenient candidate unless that decision rule is separately governed, evidence-backed, and tested.

[Back to top](#top)

---

## Temporal, freshness, and stale-state contract

Hydrology is time-aware. The following times remain distinct where material:

| Time field | Meaning |
|---|---|
| `source_time` | When the upstream source asserted or versioned the record. |
| `observed_time` | When a measurement or event occurred. |
| `valid_time` | Window for which a model, forecast, or context is valid. |
| `issue_time` | When an operational or regulatory product was issued. |
| `expiry_time` | When a time-bounded product ceased to be current. |
| `retrieval_time` | When KFM obtained the source. |
| `processing_time` | When a governed process transformed it. |
| `release_time` | When a public-safe artifact was released. |
| `correction_time` | When a correction was issued. |
| `superseded_time` | When a newer source or release replaced it. |

Configuration must not collapse these fields into one generic timestamp.

### Freshness profiles

A file may select an accepted source-specific freshness profile. It may not invent universal thresholds or imply that all hydrologic sources have the same cadence.

A profile should define:

- source family and product class;
- expected cadence;
- latency allowance;
- fresh, delayed, stale, expired, partial, unavailable, corrected, and superseded states;
- behavior when source-head metadata is missing;
- display and API disclosure requirements;
- whether a stale artifact may remain visible as historical context;
- when a consumer must `ABSTAIN`, hold, or deny; and
- recovery behavior after source service resumes.

### Required fail-closed behavior

- Stale does not mean wrong, but stale must be visible.
- Missing or unavailable data is not an all-clear and not evidence of zero flow, no flooding, or safe conditions.
- A cached last-known value must retain its original observation and retrieval times.
- A correction must not silently overwrite prior lineage.
- A superseded source or release must not remain labeled current.
- Timezone and UTC offset must be explicit where local-time rendering occurs.
- Forecast or warning validity may not be extended by configuration.
- A successful source request does not prove data completeness.

[Back to top](#top)

---

## NFHL, flood context, and life-safety boundary

### NFHL contract

NFHL is regulatory flood-hazard context. A future configuration may control public-safe presentation only through an accepted profile and must preserve:

- regulatory role;
- source and map vintage;
- zone or designation code;
- effective or publication date;
- source citation;
- geometry and scale limitations;
- applicable caveats; and
- evidence and release state.

It must not label NFHL as:

- observed inundation;
- current flooding;
- a gauge observation;
- a forecast;
- a hydraulic model run unless the source specifically is one and is role-typed accordingly;
- a warning, watch, or advisory;
- a parcel-level insurance or legal determination; or
- KFM emergency guidance.

### Flood-context composition

A composite flood-context view may contain regulatory, observed, modeled, historical, and operational-context material only when each constituent remains separately role-typed, time-stamped, cited, and sensitivity-filtered.

A consumer must not flatten those constituents into a single “flood” truth flag.

### Life-safety boundary

KFM is not an emergency warning system. Hydrology configuration must never:

- issue, rank, modify, suppress, extend, cancel, or replace official warnings;
- generate evacuation, shelter, travel, rescue, medical, or protective-action instructions;
- emit an all-clear;
- trigger sirens, pagers, phone trees, text messages, dispatch, escalation, or incident command;
- infer safety from missing data; or
- represent KFM as the current authority for flood conditions.

When a governed Hydrology surface displays operational-warning context, it must:

- identify the official source and jurisdiction;
- preserve issue and expiry times;
- make current, stale, expired, and historical states explicit;
- retain a not-for-life-safety disclaimer;
- direct the user to a verified jurisdiction-appropriate official-source profile; and
- return a finite deny or abstain outcome when freshness, authority, or official-link state is unresolved.

Exact disclaimer text and official-source profiles are policy and product decisions, not configuration authority, and remain `NEEDS VERIFICATION`.

[Back to top](#top)

---

## Cross-lane ownership and context rules

Hydrology may join other lanes, but the join must preserve ownership, source role, sensitivity, time, and evidence.

| Related lane | Hydrology relationship | Boundary |
|---|---|---|
| Hazards | Observed flow/level, regulatory NFHL, drought and flood context | Hazards owns event, warning, declaration, exposure, and resilience claims. Hydrology does not issue warnings. |
| Soil | HUC/watershed, infiltration, runoff, hydrologic-group context | Soil owns soil units, horizons, and properties. |
| Agriculture | Irrigation, water-use, drought, crop-water context | Agriculture owns crops, fields, yield, and production; observed flow is not yield without a governed model. |
| Settlements / Infrastructure | Bridges, dams, utilities, intakes, treatment, floodplain exposure | Infrastructure owns facility identity and operational status; sensitive precision fails closed. |
| Geology | Aquifer and hydrostratigraphic context | Geology owns physical geologic units; Hydrology owns observations and water-system relationships. |
| Habitat | Wetland, riparian, watershed, and reach context | Habitat owns habitat objects; sensitive joins retain Habitat and species controls. |
| Fauna | Aquatic and occurrence context | Fauna owns animal occurrences and sensitive sites. |
| Flora | Wetland, riparian, and vegetation context | Flora owns plant occurrences, specimens, and sensitive locations. |
| Roads, Rail, and Trade | Bridges, crossings, closures, detours, and flood exposure | Transport owns network and closure truth; Hydrology supplies water context only. |
| People, DNA, Land | Well ownership, water rights, parcels, and private-property implications | People/Land owns identity, title, ownership, and parcel claims; joins default to minimum necessary detail. |
| Spatial Foundation | CRS, geometry, scale, and generalization | Hydrology consumes shared spatial rules and does not override them. |

Join-induced sensitivity is evaluated on the resulting product, not only on each input. A harmless gauge, parcel, owner, well, dam, facility, or infrastructure record may become sensitive when combined with other data.

[Back to top](#top)

---

## Private property, infrastructure, and reconstruction risk

Hydrology's sensitive surface concentrates in private-property implications and infrastructure exposure.

### Protected or review-required context

Examples include:

- exact private-well locations;
- well-owner or water-right holder identity;
- domestic or vulnerable water-supply details;
- dam internals, control systems, or condition detail;
- treatment, intake, outfall, pumping, storage, utility, or communications detail;
- emergency water resources;
- resilience-critical dependencies;
- precise facility exposure derived from flood or drought joins;
- low-count or isolated well, facility, or owner summaries;
- restricted source attributes; and
- repeated-query combinations that reconstruct suppressed detail.

### Required posture

A future file may select only accepted sensitivity and public-safe profiles. It must not define ad hoc coordinates, buffer distances, masking, suppression, aggregation thresholds, jitter, delay, access tiers, or owner-redaction rules.

Validation and review must consider:

- exact geometry and attribute disclosure;
- low counts and small-area aggregates;
- differencing across releases;
- repeated query and zoom behavior;
- cached tiles and exports;
- alternate IDs and labels;
- temporal changes that reveal a hidden feature;
- joins with parcels, owners, facilities, roads, or emergency resources;
- metadata, media, filenames, and URLs; and
- residual risk after generalization.

When rights or sensitivity remains unresolved, the safe outcome is hold, restrict, deny, or abstain—not a more permissive default.

[Back to top](#top)

---

## Validation

### Documentation-only validation for this revision

- Markdown structure and final newline are present.
- Relative links are repository-plausible and authority-labeled.
- No secrets, private endpoints, personal paths, source payloads, real site values, warning content, private-property details, or exact protected geometry are included.
- NFHL, observations, models, aggregates, administrative records, candidates, and warnings remain distinct.
- No source, network, model, public route, release, or publication behavior is introduced.

### Required validation before a future payload

A payload should pass deterministic, no-network checks for:

1. syntax and parser compatibility;
2. format and configuration version;
3. required keys and type constraints;
4. duplicate and unknown keys;
5. consumer and owner binding;
6. canonical reference resolution;
7. source-role presence and allowed use;
8. NFHL misuse and role-collapse negative cases;
9. HUC, reach, site, and source-vintage identity semantics;
10. ambiguous-reach abstention;
11. parameter, unit, datum, qualifier, provisional, and no-data handling;
12. CRS, scale, resolution, geometry, and precision;
13. source, observed, valid, issue, expiry, retrieval, release, correction, and supersession times;
14. fresh, stale, partial, unavailable, corrected, and superseded states;
15. rights, attribution, redistribution, and rate-limit references;
16. private-property, well, owner, infrastructure, join, low-count, differencing, and reconstruction risk;
17. emergency-alert and action-guidance denial;
18. no-network and no-side-effect behavior;
19. deactivation, migration, correction, and rollback; and
20. proof that directory presence alone activates nothing.

### Essential negative cases

- NFHL labeled as observed flood;
- modeled hydrograph labeled as observed;
- aggregate used as site truth;
- administrative roster treated as observation or ownership proof;
- ambiguous reach auto-selected;
- unit or parameter mismatch;
- datum omitted where material;
- qualifier or provisional status discarded;
- no-data converted to zero;
- stale value shown as current;
- outage interpreted as safe conditions;
- warning context treated as KFM authority;
- emergency instruction or all-clear generation;
- unresolved rights accepted;
- exact private-well or infrastructure detail exposed;
- repeated-query reconstruction possible;
- unknown consequential key ignored;
- invalid config falling back to permissive behavior;
- network access during validation; and
- connector, watcher, or consumer writing directly to catalog, published, or release state.

Repository workflows that only echo TODO messages are scaffolds, not proof of substantive Hydrology validation.

[Back to top](#top)

---

## Failure behavior

Failures must be finite, visible, deterministic, and non-permissive. Exact machine enums and exit codes remain `NEEDS VERIFICATION`.

| Condition | Required behavior |
|---|---|
| Missing optional file | Keep the proposed feature disabled or use a separately verified safe built-in default. |
| Missing required file | Recorded error or hold; do not continue with partial assumptions. |
| Unreadable or malformed file | Recorded error; no best-effort parsing. |
| Unsupported version | Hold or error with migration guidance. |
| Unknown consequential key | Reject or hold. |
| Duplicate key | Reject unless explicitly governed by the parser contract. |
| Missing consumer or owner | Hold; no activation. |
| Unresolved schema, contract, policy, or registry reference | Hold or error. |
| Missing or conflicting source role | Deny or hold. |
| NFHL used as observed/forecast/current flood | Deny. |
| Modeled series used as observation | Deny. |
| Ambiguous reach identity | Abstain or hold for review. |
| Parameter, unit, datum, qualifier, or no-data mismatch | Deny or hold; preserve source-native value. |
| Stale source or release | Visible stale state; abstain from current claims as required. |
| Partial source response | Mark partial; do not imply completeness. |
| Source outage | Preserve last-known lineage with stale disclosure or return unavailable; never imply safety. |
| Unresolved rights | Deny public use or hold. |
| Unresolved private-property or infrastructure sensitivity | Restrict, deny, or hold. |
| Life-safety or emergency-warning use | Deny and redirect to official authority through the accepted product/policy path. |
| Network request attempted during no-network validation | Error. |
| Consumer side effect during validation | Error and rollback test state. |
| Rollback target unavailable | Hold activation or release-dependent use. |

No failure path may silently:

- widen exposure;
- lower review burden;
- relabel a claim;
- resolve identity ambiguity;
- extend validity;
- erase stale state;
- drop qualifiers;
- fabricate zero or normal conditions;
- activate a source or network request;
- publish an artifact; or
- generate life-safety advice.

[Back to top](#top)

---

## Governed AI and generated language

Configuration may support presentation preferences for an already-governed AI or Focus Mode consumer. It cannot authorize AI to become Hydrology truth or an emergency authority.

Generated language must:

- use released, resolvable evidence only;
- preserve source roles and object ownership;
- distinguish NFHL regulatory context from observed flooding;
- distinguish observations from models and aggregates;
- disclose measurement units, qualifiers, uncertainty, and time where material;
- disclose stale, partial, unavailable, corrected, and superseded state;
- abstain when reach identity, evidence, time, rights, or measurement semantics are insufficient;
- deny sensitive owner, well, infrastructure, or protected-detail exposure;
- deny flood-warning, evacuation, all-clear, and other life-safety replacement; and
- remain subordinate to policy, evidence, review, and release state.

Configuration must not contain prompts or text that instruct a model to:

- infer current flooding from NFHL;
- predict flooding without a governed forecasting product and evidence;
- suppress caveats or stale-state disclosure;
- choose an ambiguous reach;
- convert units or datums without an accepted method;
- expose private owner or infrastructure detail; or
- answer authoritatively when evidence requires abstention.

Any AI output is interpretive and requires the applicable runtime receipt and finite outcome. This README does not establish those runtime surfaces.

[Back to top](#top)

---

## Review burden

README changes require:

- configuration or documentation review; and
- Hydrology domain review.

A future payload also requires the applicable:

- named consumer owner;
- measurement, parameter, unit, datum, and qualifier reviewer;
- reach/HUC/site identity and crosswalk reviewer;
- source-role and evidence reviewer;
- source-owner and freshness reviewer;
- rights and attribution reviewer;
- private-property and infrastructure sensitivity reviewer;
- public-safety and warning-boundary reviewer;
- schema or contract reviewer;
- validation and test reviewer;
- security and privacy reviewer;
- accessibility and caveat-presentation reviewer; and
- policy and release reviewer.

No reviewer may approve NFHL as observed flooding, ambiguous identity as resolved without evidence, or KFM as a warning authority through this lane.

Do not infer acceptance from a missing reviewer rule or placeholder `CODEOWNERS` entry. Owners remain `OWNER_TBD` until verified.

[Back to top](#top)

---

## Maintenance and safe change pattern

When a Hydrology configuration file is added or changed:

1. identify the exact consumer and owner;
2. re-read the parent config contract and Hydrology doctrine;
3. verify canonical contract, schema, policy, registry, source, measurement, and identity references;
4. preserve NFHL, observed, modeled, aggregate, administrative, candidate, synthetic, and warning distinctions;
5. verify parameter, unit, datum, qualifier, provisional, no-data, and conversion semantics;
6. verify HUC digit level, reach/site namespace, source vintage, crosswalk, confidence, and ambiguity behavior;
7. verify spatial CRS, scale, resolution, geometry, precision, and public-safe profile;
8. verify source, observed, valid, issue, expiry, retrieval, release, correction, supersession, and timezone semantics;
9. review stale, partial, unavailable, corrected, superseded, and outage behavior;
10. review rights, private-property, well, owner, infrastructure, join, low-count, differencing, and reconstruction risk;
11. verify non-alert and official-source redirect behavior where warning context is displayed;
12. run deterministic parse, shape, semantic, negative, and no-network checks;
13. document precedence, unknown-key behavior, migration, deactivation, correction, and rollback;
14. inspect the complete diff for secrets, live bindings, real observations, current warnings, owner/infrastructure detail, and protected clues;
15. verify remote read-back and changed paths; and
16. keep configuration, source admission, evidence, policy, warning authority, release, and publication as separate governed concerns.

### Change-budget discipline

A configuration PR should not silently add or alter:

- source activation, polling, or network behavior;
- warning, notification, dispatch, escalation, or incident behavior;
- contracts or schemas;
- source-role vocabulary or mapping;
- scientific parameter meaning;
- unit or datum conversions;
- reach or HUC identity algorithms;
- freshness thresholds without source-owner review;
- sensitivity or public-safe geometry policy;
- connectors, watchers, pipelines, models, or package logic;
- lifecycle data;
- receipts or proofs;
- release decisions; or
- public routes, layers, tiles, hydrographs, reports, or exports.

Those changes require separate scoped implementation and review surfaces.

[Back to top](#top)

---

## Migration and anti-bypass posture

If misplaced material is found here:

1. do not treat it as authoritative merely because it is committed;
2. classify it as safe config, warning/action material, secret/live binding, contract, schema, policy, registry, source payload, measurement data, identity decision, package code, pipeline/connector/watcher code, runtime/infra, lifecycle object, trust artifact, release record, public artifact, generated output, or sensitive detail;
3. remove or quarantine credentials, live bindings, current operational instructions, private-owner detail, exact infrastructure detail, and protected context immediately;
4. rotate or revoke exposed credentials as required;
5. move machine shape to `schemas/`;
6. move semantic meaning to `contracts/`;
7. move admissibility, role, freshness, sensitivity, and warning rules to `policy/`;
8. move source identity and activation state to registry/connector governance;
9. move implementation to packages, pipelines, connectors, runtime, apps, tools, or infrastructure as appropriate;
10. move lifecycle, catalog, receipt, proof, and published material to canonical `data/` lanes;
11. move release, correction, withdrawal, supersession, and rollback decisions to `release/`;
12. preserve provenance, source-native values, consumer impact, migration reason, exposure assessment, and rollback instructions; and
13. create a drift, correction, or incident record when misplaced material was consumed or exposed.

### Anti-bypass matrix

| Bypass risk | Required response |
|---|---|
| Config treated as Hydrology truth | Reject; evidence and contracts remain authoritative. |
| Config treats NFHL as observed flood | Deny. |
| Config treats model as observation | Deny. |
| Config resolves ambiguous reach by convenience | Abstain or hold. |
| Config silently converts units or datums | Reject and route to governed measurement logic. |
| Config discards qualifier, provisional, or no-data state | Reject. |
| Config extends stale or expired data | Reject; preserve stale/historical state. |
| Config treats outage as safety | Reject. |
| Config treated as warning authority | Deny; KFM remains contextual only. |
| Config triggers source fetch, warning, or notification | Reject and move implementation out of scope. |
| Config duplicates contract or schema | Move meaning/shape to the canonical root and keep only references here. |
| Directory presence activates a source or model | Reject; require explicit verified binding. |
| Config contains exact well, owner, or infrastructure context | Remove, assess exposure, and route through sensitivity/correction governance. |
| Client-side style hides protected geometry | Reject; aggregate, redact, restrict, or deny before public artifact generation. |
| Config writes catalog, receipt, proof, or release records | Reject and move to canonical trust/release homes. |
| Public client reads this directory | Reject; public access must cross the governed API and released artifacts. |
| Watcher publishes from config | Reject; watchers and connectors may propose candidates and receipts only. |

[Back to top](#top)

---

## Definition of done for the first payload

- [ ] A named consumer and accepted owners are verified.
- [ ] The file format, version, parser, and explicit load path are verified.
- [ ] Canonical schema, contract, policy, registry, doctrine, and source references resolve.
- [ ] Precedence, duplicate-key, missing-file, and unknown-key behavior are documented and tested.
- [ ] Network, polling, model execution, warning, notification, dispatch, and escalation behavior remain disabled by file presence.
- [ ] Role-vocabulary mapping is governed and does not create aliases by configuration.
- [ ] NFHL cannot be labeled or queried as observed, forecast, or current flooding.
- [ ] Observations, models, aggregates, administrative records, candidates, synthetic fixtures, and warning context remain distinct.
- [ ] Parameter, unit, datum, qualifier, provisional, precision, conversion, and no-data semantics are explicit.
- [ ] HUC digit level, source vintage, reach/site namespace, crosswalk, confidence, and ambiguity behavior are explicit.
- [ ] Ambiguous reach identity produces abstention or review hold.
- [ ] CRS, scale, resolution, geometry, precision, and public-safe spatial semantics are explicit.
- [ ] Source, observed, valid, issue, expiry, retrieval, release, correction, supersession, and timezone semantics are explicit.
- [ ] Stale, partial, unavailable, corrected, superseded, and unknown states remain visible.
- [ ] Rights, attribution, redistribution, and source-rate-limit terms are reviewed.
- [ ] Private-well, owner, water-right, dam, utility, infrastructure, and private-property controls come from accepted policy profiles.
- [ ] Join-induced sensitivity, low counts, differencing, repeated-query, and reconstruction risks are tested.
- [ ] Operational-warning context cannot become KFM warning authority or action guidance.
- [ ] Synthetic fixtures cover valid, invalid, held, denied, abstained, stale, partial, unavailable, corrected, superseded, ambiguous, and error cases.
- [ ] No-network tests pass.
- [ ] Secret, private-endpoint, personal-path, warning, measurement, owner, infrastructure, and protected-context scans pass.
- [ ] Migration, deactivation, correction, withdrawal, and rollback behavior are tested.
- [ ] No source, model, warning, public layer, API route, release, or publication is activated by file presence.
- [ ] Repository-native checks are substantive or their scaffold limitations are stated explicitly.

[Back to top](#top)

---

## Related folders

- [`../README.md`](../README.md) — parent domain-configuration contract.
- [`../../README.md`](../../README.md) — repository-wide configuration boundary.
- [`../../../docs/domains/hydrology/README.md`](../../../docs/domains/hydrology/README.md) — Hydrology doctrine, source roles, object families, identity, freshness, sensitivity, and lifecycle posture.
- [`../../../docs/registers/DOMAIN_LANE.md`](../../../docs/registers/DOMAIN_LANE.md) — canonical lane and sensitivity register.
- [`../../../docs/registers/DRIFT_REGISTER.md`](../../../docs/registers/DRIFT_REGISTER.md) — unresolved path and authority drift.
- [`../../../docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) — placement and responsibility law.
- [`../../../docs/security/SECRETS.md`](../../../docs/security/SECRETS.md) — credential and sensitive-value handling.

Future files should link to verified Hydrology contracts, schemas, policies, source descriptors, measurement profiles, identity crosswalks, freshness profiles, tests, fixtures, receipts, proofs, and release records only after those exact paths and authority relationships are confirmed.

[Back to top](#top)

---

## ADRs and drift triggers

No ADR is introduced by this README.

Separate governance is required for changes that would:

- add, rename, merge, or retire a canonical domain slug;
- change Hydrology ownership or cross-lane boundaries;
- change or map the source-role vocabulary;
- permit NFHL to be treated as observed flooding, forecast flooding, or warning authority;
- alter measurement meaning, unit conversion, datum handling, qualifier behavior, or no-data semantics;
- define or change reach/HUC/site identity algorithms, crosswalk thresholds, or ambiguity resolution;
- define or alter freshness thresholds, stale-state rules, warning-boundary language, official-source profiles, sensitivity tiers, private-property rules, infrastructure aggregation, low-count rules, or public-safe geometry policy;
- decide source rights, source authority, live-source activation, or connector cadence;
- establish emergency warning, notification, dispatch, escalation, or incident-command behavior;
- resolve segment-versus-flat lane paths;
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
2. stop any connector, watcher, model, renderer, scheduled process, or public-output workflow that depends on the faulty selection;
3. preserve the faulty version, source-native values, and evidence needed for review;
4. identify affected objects, observations, identities, crosswalks, conversions, models, joins, caches, tiles, hydrographs, indexes, exports, screenshots, and narratives without exposing protected details;
5. assess whether NFHL, observation, model, aggregate, administrative, candidate, synthetic, or warning roles were collapsed;
6. assess whether measurement meaning, units, datums, qualifiers, provisional status, or no-data values were altered;
7. assess whether reach/HUC/site identity was incorrectly resolved;
8. assess whether stale, partial, unavailable, corrected, or superseded state was hidden;
9. assess whether exact or reconstructable private-property, well, owner, dam, utility, or infrastructure information was exposed;
10. restore the prior known-good version or safe disabled state;
11. re-run validation and negative cases;
12. create any required correction, redaction, aggregation, withdrawal, release, or rollback records in their canonical homes; and
13. verify that no public surface continues to serve an unauthorized, stale, misclassified, incorrectly converted, wrongly identified, or reconstructable derivative.

A Git revert does not itself revoke exposed data, correct released artifacts, restore scientific meaning, undo an identity decision, invalidate caches, or establish KFM publication lineage.

[Back to top](#top)

---

## Safe language rules

Use language such as:

- “safe Hydrology configuration template for a named consumer”;
- “intended consumer — `NEEDS VERIFICATION`”;
- “synthetic placeholder”;
- “NFHL regulatory context, not observed inundation”;
- “observed gauge reading with source time, unit, qualifier, and provisional state”;
- “modeled hydrograph, not observation”;
- “candidate reach mapping — ambiguous; abstain”;
- “stale historical context, not current conditions”;
- “public-safe display profile selector, subject to policy and release review”;
- “configuration aid, not authority”; and
- “bounded search found no indexed executable consumer.”

Avoid unsupported claims such as:

- “the Hydrology pipeline uses this config”;
- “this file activates the gauge source”;
- “this config is validated by CI” when the workflow is only scaffolding;
- “NFHL shows where flooding is happening”;
- “the hydrograph is observed” when it is modeled or reconstructed;
- “the nearest reach is the correct reach”;
- “missing data means no flood risk”;
- “this value is zero” when the source uses a no-data sentinel;
- “this conversion is exact” without governed method and precision;
- “this setting authorizes public display”;
- “this configuration replaces policy”; or
- “this folder contains the complete operational Hydrology configuration.”

[Back to top](#top)

---

## Last reviewed

**2026-07-14**, against `main@b46db8e827d1ba851534568cbb16f76e78af5072`.

Review again before the first non-README payload, consumer binding, loader or precedence decision, source-role mapping, measurement profile, identity-crosswalk profile, freshness profile, sensitivity profile, source or model activation, warning-context integration, or public-output integration.

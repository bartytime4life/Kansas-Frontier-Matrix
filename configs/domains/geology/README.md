<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-domains-geology-readme
title: configs/domains/geology/ — Geology Configuration Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Config steward · Geology steward · Resource/infrastructure sensitivity reviewer · Consumer owner · Validation steward
created: 2026-07-13
updated: 2026-07-13
policy_label: public; config-sublane; geology; natural-resources; anti-collapse; sensitive-location-aware; infrastructure-aware; source-role-aware; non-secret; non-authoritative; no-live-binding
current_path: configs/domains/geology/README.md
truth_posture: CONFIRMED canonical geology slug, repository-present parent config contract, repository-present Geology and Natural Resources doctrine, occurrence/deposit/estimate/permit/production/reserve anti-collapse rule, exact borehole/private-well/sensitive-resource restriction default, and documentation-only lane / CONFLICTED object-family naming and segment-versus-flat lane-path forms / PROPOSED future consumer-bound templates and governed profile selectors / UNKNOWN consumers, precedence, loader behavior, and enforcement / NEEDS VERIFICATION owners, executable validation, source rights, canonical object-family names, public-safe geometry parameters, and runtime binding
related:
  - ../README.md
  - ../../README.md
  - ../../../docs/domains/geology/README.md
  - ../../../docs/registers/DOMAIN_LANE.md
  - ../../../docs/registers/DRIFT_REGISTER.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/security/SECRETS.md
notes:
  - "This lane contains documentation only. It does not create, load, activate, interpret, expose, or publish a Geology configuration payload."
  - "v0.2 expands the Geology-specific source-role, object-family, anti-collapse, temporal, resource-sensitivity, public-safe geometry, validation, correction, and rollback contract without creating a new policy, schema, registry, estimate, permit, redaction, or release authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Geology Domain Configuration

`configs/domains/geology/`

> Safe-to-commit, Geology-specific configuration documentation and future consumer-bound templates. This lane does not own geologic truth, natural-resource claims, permit or production truth, source admission, sensitivity, evidence, release, or publication.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Scope](#scope) · [Repository fit](#repository-fit) · [Inputs](#inputs) · [Outputs](#outputs) · [Configuration contract](#minimum-configuration-contract) · [Anti-collapse](#geology-and-resource-claim-anti-collapse) · [Sensitive locations](#sensitive-locations-resource-context-and-public-safe-geometry) · [Validation](#validation) · [Failure behavior](#failure-behavior) · [Review](#review-burden) · [Maintenance](#maintenance) · [Related](#related-folders) · [ADRs](#adrs) · [Rollback](#rollback-and-correction)

> [!IMPORTANT]
> **Document lifecycle:** draft `v0.2`  
> **Component maturity:** documentation boundary only  
> **Authority:** implementation-supporting configuration sublane; non-authoritative for truth and governance  
> **Runtime posture:** no Geology payload, loader, consumer binding, source activation, interpretation, public-safe transform, or public exposure is established by this README

> [!CAUTION]
> Exact or reconstructable borehole, core, sample, well-log, private-well, sensitive-resource, geophysics, geochemistry, operator, and infrastructure detail fails closed unless governed policy and review authorize a public-safe derivative. Directory presence, a future configuration file, or a parsed value must never convert an occurrence into a deposit, a deposit into an estimate, a permit into production, an interpretation into an observation, or a model into geologic truth.

---

## Purpose

This directory defines the safe-to-commit configuration boundary for the canonical Geology and Natural Resources lane.

It may eventually hold small defaults, templates, examples, or review-oriented settings for a **named and verified consumer**. Those files may describe how that consumer should behave, but they cannot decide:

- which geologic map, stratigraphic interpretation, or source authority is controlling;
- whether a feature is an observation, occurrence, deposit, estimate, permit, production record, reserve claim, or model;
- whether a borehole, well log, sample, geophysical survey, or geochemical result is admissible or releasable;
- whether a resource estimate or reserve statement is valid;
- whether exact or generalized geometry may be exposed;
- whether rights, operator, parcel, infrastructure, or private-well restrictions have been satisfied;
- whether evidence supports a geologic or resource claim; or
- whether an artifact may be promoted, released, or published.

This README is intended for:

- Geology and Natural Resources domain stewards;
- configuration and developer-experience maintainers;
- source-role, resource, infrastructure, rights, sensitivity, policy, security, and release reviewers;
- package, pipeline, app, runtime, test, and tooling owners that may consume Geology configuration; and
- reviewers checking Directory Rules placement, anti-collapse discipline, and trust-membrane integrity.

[Back to top](#top)

---

## Authority level

**Configuration-supporting and non-authoritative.**

| Concern | Authority in this lane |
|---|---|
| Geology domain meaning | **None.** Domain doctrine remains in [`docs/domains/geology/`](../../../docs/domains/geology/README.md). |
| Geologic observation or interpretation truth | **None.** Configuration cannot establish evidentiary status or convert an interpretation, cross-section, generalized polygon, or model into an observation. |
| Resource classification | **None.** Configuration cannot convert `Occurrence`, `Deposit`, `Estimate`, `Permit`, `Production`, or `Reserve` claims into one another. |
| Permit, extraction, production, or reclamation status | **None.** Regulatory and operational claims require their own authority sources, evidence, and review. |
| Ownership, lease, title, or parcel truth | **None.** Geology may reference People/Land context but cannot establish ownership or title. |
| Source identity, role, rights, cadence, and activation | **None.** These require the applicable source registry, connector, policy, rights, and review surfaces. |
| Schema or contract shape | **None.** Configuration may reference a verified schema or contract but must not duplicate or redefine it. |
| Sensitivity or public-safe geometry decision | **None.** A value may select an already-governed profile; it cannot create, weaken, or approve a sensitivity or geometry rule. |
| Evidence or claim truth | **None.** Configuration cannot create an `EvidenceBundle`, validate a claim, or make generated interpretation sovereign truth. |
| Release or publication | **None.** Configuration cannot authorize promotion, release, public display, or KFM publication. |
| Consumer behavior | **Supporting only.** A verified consumer may read a validated file under an explicit binding and precedence rule. |

A configuration value may point to an authority surface. It does not become authority through repetition, proximity, successful parsing, operational convenience, or use by a map, dashboard, 3D scene, cross-section renderer, or AI surface.

[Back to top](#top)

---

## Status

| Item | State | Safe conclusion |
|---|---:|---|
| Canonical domain slug | **CONFIRMED** | `geology` is a repository-present canonical domain lane. |
| Parent configuration contract | **CONFIRMED** | [`configs/domains/README.md`](../README.md) defines this path as a non-secret, non-authoritative configuration sublane. |
| Geology doctrine | **CONFIRMED repository-present** | The domain README establishes evidence-first geologic handling, resource anti-collapse, and exact-location restriction defaults. |
| Anti-collapse rule | **CONFIRMED doctrine** | `Occurrence`, `Deposit`, `Estimate`, `Permit`, `Production`, and `Reserve` remain distinct in storage, evidence, graph projections, and public summaries. |
| Sensitive-location posture | **CONFIRMED doctrine** | Exact borehole, core, sample, well-log, private-well, sensitive-resource, geophysics, and geochemistry locations default to restricted or generalized public geometry. |
| Current lane content | **README ONLY** | This lane establishes documentation, not executable configuration. |
| Consumer and loader | **UNKNOWN** | No consumer, parser, discovery mechanism, merge order, or unknown-key behavior is established here. |
| Object-family names | **CONFLICTED** | Short conceptual names and `…Reference` schema-candidate names coexist in doctrine; configuration must not silently choose a canonical vocabulary. |
| Lane-path form | **CONFLICTED** | Segment and flat responsibility-path forms are documented; configuration must not create both or resolve the conflict by convention. |
| Source rights and redistribution | **NEEDS VERIFICATION** | Source-specific terms, attribution, redistribution classes, and access restrictions require verified `SourceDescriptor` evidence. |
| Public-safe geometry parameters | **NEEDS VERIFICATION** | Generalization, withholding, aggregation, delay, and restricted-view parameters must come from policy and steward review. |
| Validation and CI enforcement | **NEEDS VERIFICATION** | Expectations are documented; executable enforcement is not proven by this README. |
| Runtime, release, and publication | **NOT ESTABLISHED** | Nothing in this lane authorizes operational use, release, or publication. |

Directory presence must not trigger discovery, source activation, network access, indexing, interpretation generation, cross-section construction, 3D scene creation, map-layer creation, geometry exposure, lifecycle promotion, or publication.

[Back to top](#top)

---

## Scope

### What belongs here

Only safe, non-secret, Geology-specific configuration material for a named or explicitly proposed consumer belongs here.

| Material | Permitted purpose | Minimum posture |
|---|---|---|
| `README.md` | Define this configuration boundary. | Preserve non-authority, anti-collapse, sensitivity, rights, evidence, and release controls. |
| `*.template.yaml` or `*.template.yml` | Placeholder-based template for a verified Geology consumer. | Parseable, versioned, consumer-bound, no secrets, no live binding. |
| `*.example.yaml`, `*.example.json`, or `*.example.toml` | Tiny illustrative configuration. | Clearly synthetic values; impossible identifiers and geometry; no automatic activation. |
| Conservative review defaults | Select an existing hold, abstain, restrict, generalize, redact, or review profile. | Cannot weaken policy, rights, or release burden. |
| Public-safe display profile selectors | Select an already-governed generalized display profile. | Cannot contain exact protected geometry or authorize exposure. |
| Interpretation presentation hints | Configure labels, uncertainty display, or version visibility for a verified consumer. | Must not change evidentiary status or hide interpretation uncertainty. |
| Migration notes | Document a real key, version, or consumer transition. | Time-bounded, owner-linked, reversible, and not a parallel authority. |

Synthetic examples must not resemble a real borehole, well, operator, permit, resource occurrence, extraction site, mine, pipeline, storage facility, parcel, sample, or sensitive infrastructure location closely enough to support reconstruction.

### What does not belong here

- real borehole, well-log, core, sample, geophysics, geochemistry, cross-section, or source payloads;
- real mineral occurrence, deposit, estimate, reserve, permit, production, extraction, reclamation, operator, lease, parcel, or infrastructure records;
- exact or reconstructable private-well, sensitive-resource, subsurface, extraction, storage, pipeline, mine, or facility locations;
- credentials, tokens, private endpoints, signed URLs, workstation paths, internal deployment bindings, or environment-specific secrets;
- settings that present estimates, interpretations, generalized maps, AI summaries, synthetic surfaces, or models as observations;
- settings that treat a permit as production, a production record as a reserve, an occurrence as a deposit, or a deposit as an estimate;
- settings that treat geology as ownership, title, lease, regulatory, hazard, or hydrologic measurement authority;
- source admission, activation, cadence, rights, redistribution, or source-role decisions;
- schemas, contracts, policy, registries, receipts, proofs, evidence bundles, release records, correction notices, or publication decisions;
- lifecycle data from RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED stores;
- duplicate segment and flat path authorities created to bypass unresolved repository drift.

### Explicit non-ownership

This lane may reference verified outputs from other responsibility roots, but it must not redefine them. In particular, it does not own:

- soil map units, horizons, or soil-property surfaces;
- streamflow, groundwater measurements, water-quality measurements, flood truth, or hydrologic observations;
- hazard-event or risk truth;
- ownership, title, lease, parcel, operator identity, or living-person truth;
- archaeological sensitivity or cultural-resource review;
- regulatory permit authority outside verified regulatory sources;
- source descriptors, policy decisions, receipts, proofs, manifests, promotion decisions, releases, or public publication state.

[Back to top](#top)

---

## Repository fit

This directory is a child of the canonical domain-configuration boundary:

```text
configs/
└── domains/
    ├── README.md
    └── geology/
        └── README.md
```

The responsibility split is:

- [`configs/`](../../README.md): repository-wide safe configuration boundary;
- [`configs/domains/`](../README.md): common rules for domain-scoped defaults and templates;
- `configs/domains/geology/`: Geology-specific configuration support;
- [`docs/domains/geology/`](../../../docs/domains/geology/README.md): Geology and Natural Resources doctrine, terminology, source families, sensitivity, lifecycle, and anti-collapse expectations;
- `contracts/domains/geology/`: semantic object meaning, when verified;
- `schemas/contracts/v1/domains/geology/`: machine-checkable shape, subject to the unresolved lane-path and object-name conflicts;
- `policy/domains/geology/`: admissibility, rights, sensitivity, anti-collapse, and public-safe geometry rules, when verified;
- source registries, connectors, tests, fixtures, receipts, proofs, catalogs, lifecycle stores, and release surfaces: their own canonical responsibility roots.

This README must not duplicate those authorities. It should link to them only after exact paths and authority relationships are verified.

The repository doctrine records two unresolved forms:

1. short conceptual object names versus `…Reference` schema-candidate names; and
2. domain-segment responsibility paths versus flatter crosswalk paths.

A configuration file must not settle either conflict by creating aliases, duplicate keys, duplicate files, or parallel authority homes.

[Back to top](#top)

---

## Inputs

A future Geology configuration payload requires all of the following before it may be treated as implementation-supporting:

1. **Named consumer** — exact package, app, pipeline, service, runtime, test harness, renderer, or tool.
2. **Accepted owner** — accountable owner for the consumer and the configuration file.
3. **Declared format** — file type, format version, parser, encoding, and canonical load path.
4. **Authority references** — verified contract, schema, policy, source registry, domain documentation, and ADR or drift references where applicable.
5. **Object-role model** — explicit distinction among observation, occurrence, unit, deposit, estimate, permit, production, reserve, extraction, reclamation, interpretation, and model roles.
6. **Source-role model** — explicit authority, observation, context, and model roles that cannot be changed per query.
7. **Temporal semantics** — source, observed, valid, retrieval, model, permit, production, release, supersession, and correction times remain distinct where material.
8. **Spatial semantics** — coordinate reference system, dimensionality, geometry class, uncertainty, resolution, scale, and public-safe geometry profile are explicit.
9. **Units and measurement semantics** — physical units, datum, analyte, confidence class, estimate method, and uncertainty are explicit where applicable.
10. **Rights and sensitivity review** — redistribution, private-well, operator, parcel, infrastructure, resource, and cross-lane risks are reviewed.
11. **Synthetic fixtures** — no-network examples cover valid, invalid, held, denied, abstained, stale, and error states.
12. **Precedence contract** — merge order, override rules, environment interaction, unknown-key behavior, and missing-file behavior are explicit.
13. **Failure contract** — parsing, semantic, rights, sensitivity, stale-state, and source-outage failures produce finite reason-coded outcomes.
14. **Rollback contract** — deactivation, prior-known-good version, migration reversal, affected-output assessment, correction path, and verification steps are documented.

Missing authority, rights, source role, object role, sensitivity, geometry, or consumer evidence must not be filled in by configuration convention.

[Back to top](#top)

---

## Outputs

This lane currently outputs **documentation only**.

A future verified configuration file may produce:

- a parseable configuration object for one named consumer;
- a selected reference to an already-governed validation, interpretation-display, sensitivity, review, or public-safe geometry profile;
- deterministic validation results;
- explicit hold, deny, abstain, error, or stale-state behavior; and
- migration and rollback metadata.

It must not produce or imply:

- a geologic observation, unit, boundary, occurrence, deposit, estimate, reserve, permit, production, extraction, reclamation, or ownership claim;
- a source activation or admission decision;
- a public-safe geometry transform or `RedactionReceipt`;
- an `EvidenceBundle`, validation proof, policy decision, release manifest, or rollback card;
- a public map layer, cross-section, 3D scene, API route, alert, release, or KFM publication state.

Successful parsing means only that a file is syntactically readable. It does not prove that a consumer used it, that its values are authorized, or that resulting outputs are publishable.

[Back to top](#top)

---

## Minimum configuration contract

Every future non-README file in this directory should document or encode the following contract.

### Identity and ownership

| Field | Requirement |
|---|---|
| `config_id` | Stable identifier unique within the verified consumer. |
| `config_version` | Explicit version; no implicit latest behavior. |
| `consumer` | Exact consuming component, not a generic domain label. |
| `owner` | Accountable human or accepted team. |
| `purpose` | One bounded behavior the file controls. |
| `status` | Proposed, active, deprecated, or retired for that consumer. |
| `authority_refs` | Links to verified contract, schema, policy, source, doctrine, or ADR surfaces. |
| `supersedes` | Prior version where applicable. |
| `rollback_target` | Prior known-good version or safe disabled state. |

### Parsing and loading

A consumer contract must define:

- the canonical parser and supported format version;
- whether the file is required or optional;
- the exact load path;
- whether environment substitution is allowed;
- precedence relative to root, domain, development, test, local, deployment, and runtime settings;
- unknown-key behavior;
- duplicate-key behavior;
- missing-file behavior;
- partial-application behavior;
- caching and reload behavior; and
- deterministic rejection of unsupported versions.

No consumer may infer universal precedence from directory depth or filename convention.

### Semantic controls

A file must preserve:

- object-family identity and unresolved naming conflicts;
- source-role identity;
- physical observation versus interpretation versus model distinctions;
- occurrence, deposit, estimate, permit, production, reserve, extraction, and reclamation distinctions;
- source, observed, valid, retrieval, release, supersession, and correction times;
- units, datum, coordinate reference system, dimensionality, scale, resolution, and uncertainty;
- rights, sensitivity, public-safe geometry, and restricted-view boundaries;
- ownership and regulatory non-authority; and
- provenance links to the controlling surfaces.

### Safety controls

A file must:

- contain no credential, token, signed URL, private endpoint, workstation path, or secret;
- contain no real protected geometry, identifiers, operator detail, private-well detail, or reconstructable clue;
- use synthetic values for examples;
- fail closed when rights, source role, object role, sensitivity, or authority is unresolved;
- avoid automatic network access during validation;
- avoid source, watcher, renderer, or public-route activation by file presence;
- preserve finite reason-coded failures; and
- remain reversible without rewriting shared history.

### Change record

Each substantive change should record:

- why the change is needed;
- affected consumer and keys;
- authority references;
- prior behavior and new behavior;
- validation and negative cases;
- rights, sensitivity, reconstruction, and cross-lane risk review;
- migration and compatibility period;
- deactivation and rollback steps;
- affected-output assessment; and
- reviewer roles.

[Back to top](#top)

---

## Geology and resource-claim anti-collapse

The Geology lane's central configuration invariant is that **physical geology, interpretation, regulatory status, operational activity, and resource classification remain distinct**.

### Resource-claim classes

| Claim class | What it may mean | What it must not imply |
|---|---|---|
| `Occurrence` | Documented presence of a mineral, material, structure, or feature. | A delineated deposit, economic viability, an estimate, reserve status, permit, or production. |
| `Deposit` | Characterized geologic body or concentration. | Quantity, grade, economic viability, permit status, production, or reserve classification. |
| `Estimate` | Quantitative calculation with method, confidence, date, and assumptions. | Observation, reserve classification, permit, production, or guaranteed recoverability. |
| `Permit` | Regulatory authorization or application state from a verified authority. | Physical occurrence, production, compliance, ownership, or reserve status. |
| `Production` | Reported extraction or output for a defined source and period. | Reserve size, future production, ownership, permit compliance, or resource truth outside its scope. |
| `Reserve` | Classified recoverable quantity under a defined standard, date, assumptions, and authority. | Raw occurrence, general deposit, permit, production, or timeless truth. |
| `ExtractionSite` | Location or facility associated with past or present extraction. | Current operation, legal status, ownership, permit compliance, production, or reserve quantity. |
| `ReclamationRecord` | Recorded reclamation plan, status, or observation. | Closure certification, environmental compliance, completed restoration, or absence of future liability. |

A configuration key must not:

- rename one class as another;
- merge classes into a generic `resource` truth field;
- choose a stronger class as a fallback;
- infer estimate or reserve status from a polygon label;
- infer production from a permit;
- infer ownership from an operator, lease, parcel, or extraction record; or
- hide the source, method, date, uncertainty, and authority of an estimate.

### Observation, interpretation, and model classes

- `GeologicUnit` and mapped boundaries are source- and version-bound, not timeless ground truth.
- `CrossSection` is an interpretation with authorship, version, uncertainty, and evidence; it is not an attestation of subsurface conditions.
- `GeophysicalObservation` and `GeochemistrySample` are observations; inversions, interpolations, surfaces, and classifications derived from them are models or interpretations.
- A model field, synthetic surface, generalized map, or AI summary is not an observation.
- A `HydrostratigraphicUnit` provides geology context to Hydrology; it does not replace water-level, flow, quality, or aquifer measurements.
- A fault or structure feature can provide context to Hazards; it does not itself establish risk, event probability, or emergency truth.
- Geology can relate to People/Land records; it does not establish title, ownership, lease rights, or legal interest.

### Naming conflicts

The repository doctrine records short conceptual names and `…Reference` forms for several object families. Until resolved by contract, schema, or ADR:

- preserve the exact identifier expected by the verified consumer;
- include an authority reference and version;
- do not provide silent aliases;
- do not write both forms as separate truth-bearing objects;
- reject ambiguous or unsupported names; and
- record migration explicitly when a canonical vocabulary is accepted.

[Back to top](#top)

---

## Sensitive locations, resource context, and public-safe geometry

Exact geology and natural-resource geometry may expose private property, private wells, subsurface infrastructure, extraction assets, restricted source records, economically sensitive resource information, or security-relevant clues.

### Deny or restrict by default

The following require policy-backed review before any public use:

- exact private-well and water-well locations;
- exact borehole, well-log, core, sample, geophysics, and geochemistry locations;
- sensitive mineral occurrence, deposit, estimate, reserve, and exploration detail;
- extraction, mine, quarry, storage, pipeline, processing, or related infrastructure detail where exposure creates risk;
- operator, permit, lease, and parcel joins;
- rights-controlled LAS, log, core, geophysics, geochemistry, and commercial datasets;
- low-count or uniquely identifying aggregate outputs;
- cross-sections or 3D scenes that permit reverse inference of protected locations; and
- combinations of otherwise public datasets that create new reconstruction risk.

### Public-safe profiles

A future configuration may select a **verified** profile name, but the profile itself must be governed elsewhere. Possible governed outcomes include:

- suppress geometry;
- generalize to an approved grid, county, watershed, geologic region, or other public-safe unit;
- withhold protected attributes;
- delay publication;
- restrict exact detail to steward views;
- aggregate low-count records;
- publish a derived range or summary rather than source locations; or
- deny the output.

This README does not define radii, cell sizes, zoom thresholds, jitter, buffering, delay periods, minimum counts, or tier transitions. Those parameters remain policy and steward decisions.

### Join-induced sensitivity

The resulting product may be more sensitive than any input. Examples include:

- joining a mineral occurrence to a private parcel;
- joining a borehole to operator, permit, lease, or infrastructure records;
- combining generalized wells with high-resolution imagery or address data;
- combining resource estimates with extraction or storage infrastructure;
- rendering cross-sections or 3D volumes that expose restricted coordinates; or
- combining low-count samples with descriptive text that enables re-identification.

A joined product must inherit the strongest applicable restriction and pass its own reconstruction-risk review.

### Rights and redistribution

Rights, attribution, redistribution, derivative, and access restrictions are source-specific evidence. A configuration value cannot:

- declare a dataset public-domain or redistributable;
- downgrade a rights class;
- bypass a source-specific license;
- convert restricted access into public release;
- hide required attribution; or
- authorize a derivative that the verified source terms do not allow.

Unclear rights or missing source-role evidence blocks promotion and public use.

[Back to top](#top)

---

## Validation

### Documentation-only validation

For this README:

- [x] KFM metadata block is present and balanced.
- [x] The required folder-README sequence is represented.
- [x] Relative links point to repository-present parent, doctrine, register, drift, and secrets surfaces.
- [x] No real geology payload, protected location, credential, private endpoint, or deployment binding is included.
- [x] Anti-collapse, rights, source-role, sensitivity, review, and release boundaries are explicit.
- [x] A final newline is present.

### Future payload validation

A future non-README file requires deterministic validation covering:

#### Syntax and shape

- parser succeeds under the declared format version;
- duplicate keys are rejected or handled explicitly;
- required keys are present;
- unknown keys follow the declared rule;
- unsupported versions fail;
- authority references resolve;
- no secret-like values or private endpoints are present.

#### Semantic checks

- consumer and owner are known;
- object-family identifiers are supported and unambiguous;
- source role is explicit and immutable per admitted source;
- observation, interpretation, model, and aggregate roles remain distinct;
- occurrence, deposit, estimate, permit, production, reserve, extraction, and reclamation classes remain distinct;
- temporal fields and scopes are explicit;
- units, datum, coordinate reference system, dimensionality, scale, resolution, confidence, and uncertainty are valid;
- estimate method, assumptions, date, and authority are present when estimates are configured;
- rights and redistribution evidence exists;
- sensitivity and public-safe geometry profiles resolve to governed policy;
- cross-lane ownership is preserved;
- watcher, source, network, public route, release, and publication activation are absent unless independently authorized.

#### Negative cases

Tests should prove rejection or safe handling of:

- an occurrence presented as a deposit;
- a deposit presented as an estimate;
- a permit presented as production;
- production presented as reserve truth;
- an interpretation or cross-section presented as observation;
- a model or generalized polygon presented as direct observation;
- an ambiguous short versus `…Reference` object name;
- an unverified source role;
- unclear rights or redistribution;
- exact private-well or restricted borehole geometry requested for public use;
- operator, permit, or parcel joins without cross-lane review;
- unsupported coordinate reference systems or units;
- missing temporal scope or confidence class;
- unknown keys, duplicate keys, and unsupported versions;
- source outage, stale data, or incomplete inputs;
- partial application after a failed key;
- network access during no-network validation; and
- rollback to an unavailable or invalid target.

#### Structural behavior

- validation runs without live network access;
- repeated validation is deterministic;
- failures are finite and reason-coded;
- no partial configuration is applied after a failure;
- logs do not expose protected values or locations;
- caches and reloads do not preserve rejected configuration;
- the prior known-good configuration remains recoverable.

Executable config validation remains `NOT APPLICABLE` until a payload and consumer exist.

[Back to top](#top)

---

## Failure behavior

| Condition | Expected safe disposition |
|---|---|
| Valid, authorized, non-sensitive configuration | `PASS` for internal validation; continue to ordinary governed processing. |
| Malformed file, unsupported version, duplicate key, or contract violation | `FAIL` or `ERROR`; do not partially apply. |
| Unknown or conflicted object-family name | `HOLD` or `ERROR`; preserve the conflict and do not alias silently. |
| Missing source role, rights, policy, review, or authority reference | `HOLD`, `DENY`, or `ABSTAIN`; do not infer permission. |
| Occurrence/deposit/estimate/permit/production/reserve collapse | `FAIL` and `DENY` for consequential or public use. |
| Interpretation, cross-section, generalized polygon, or model presented as observation | `FAIL`; preserve its actual role. |
| Exact restricted geology location requested for public use | `DENY` by default. |
| Missing or stale evidence with no released alternative | `ABSTAIN`; do not substitute a model, cache, or estimate silently. |
| Unauthorized sensitivity reduction or public-safe geometry bypass | `FAIL` and `DENY`; record the reason without exposing protected values. |
| Source outage or incomplete data | Preserve stale or partial state explicitly; do not fabricate completeness. |
| Consumer cannot determine precedence | `ERROR` or `HOLD`; do not merge unpredictably. |
| Cross-lane ownership conflict | `HOLD`; route to the owning domain and preserve source references. |

`PASS` and `FAIL` are validator outcomes, not publication decisions. A valid configuration still requires evidence, policy, review, and release support for consequential outputs.

[Back to top](#top)

---

## Review burden

README changes require:

- config or documentation review; and
- Geology and Natural Resources domain review.

A future payload also requires the applicable:

- named consumer owner;
- object-model or contract reviewer;
- source and rights reviewer;
- resource and infrastructure sensitivity reviewer;
- public-safe geometry or geoprivacy reviewer;
- regulatory-data reviewer where permits or production are implicated;
- People/Land reviewer where operator, lease, title, or parcel context is joined;
- Hydrology, Soil, Hazards, or Archaeology reviewer where cross-lane truth or sensitivity is implicated;
- schema or contract reviewer;
- validation and test reviewer;
- security and privacy reviewer; and
- policy and release reviewer.

Do not infer acceptance from a missing reviewer rule or placeholder `CODEOWNERS` entry. Owners remain `OWNER_TBD` until verified.

[Back to top](#top)

---

## Maintenance

When a Geology configuration file is added or changed:

1. identify the exact consumer and owner;
2. re-read the parent config contract and Geology doctrine;
3. verify the canonical contract, schema, policy, source, ADR, and drift references;
4. preserve object-family, source-role, anti-collapse, temporal, units, and spatial semantics;
5. review rights, resource, infrastructure, private-well, operator, parcel, reconstruction, and cross-lane risk;
6. run deterministic parse, shape, semantic, negative, and no-network checks;
7. document precedence, unknown-key behavior, stale-state handling, migration, deactivation, and rollback;
8. inspect the complete diff for secrets, protected locations, and infrastructure clues;
9. verify remote read-back and changed paths; and
10. keep source activation, interpretation, public-safe transformation, release, and publication as separate governed decisions.

### Definition of done for the first payload

- [ ] A named consumer and accepted owners are verified.
- [ ] The file format, version, parser, and load path are verified.
- [ ] Canonical schema or contract references resolve.
- [ ] Object-family naming conflicts are resolved or explicitly rejected by the consumer.
- [ ] Source-role, resource-class, temporal, units, spatial, and uncertainty semantics are explicit.
- [ ] Rights and redistribution terms are verified.
- [ ] Public-safe geometry parameters come from accepted policy, not the config file.
- [ ] Cross-lane ownership and sensitivity reviews are complete.
- [ ] Synthetic fixtures cover valid, invalid, held, denied, abstained, stale, and error cases.
- [ ] Anti-collapse tests pass.
- [ ] No-network tests pass.
- [ ] Secret, private-location, and reconstruction-risk scans pass.
- [ ] Precedence, unknown-key, migration, deactivation, correction, and rollback behavior are tested.
- [ ] No source, watcher, interpretation, public layer, release, or publication is activated by file presence.

[Back to top](#top)

---

## Related folders

- [`../README.md`](../README.md) — parent domain-configuration contract.
- [`../../README.md`](../../README.md) — repository-wide configuration boundary.
- [`../../../docs/domains/geology/README.md`](../../../docs/domains/geology/README.md) — Geology and Natural Resources doctrine, terminology, anti-collapse rules, and sensitivity posture.
- [`../../../docs/registers/DOMAIN_LANE.md`](../../../docs/registers/DOMAIN_LANE.md) — canonical lane and sensitivity register.
- [`../../../docs/registers/DRIFT_REGISTER.md`](../../../docs/registers/DRIFT_REGISTER.md) — unresolved repository drift and authority conflicts.
- [`../../../docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) — placement and responsibility law.
- [`../../../docs/security/SECRETS.md`](../../../docs/security/SECRETS.md) — credential and sensitive-value handling.

Future files should link to verified Geology contracts, schemas, policies, source descriptors, tests, fixtures, receipts, proofs, and release records only after those exact paths and authority relationships are confirmed.

[Back to top](#top)

---

## ADRs

No ADR is introduced by this README.

Separate governance is required for changes that would:

- add, rename, merge, or retire a canonical domain slug;
- select canonical Geology object-family names or resolve short-form versus `…Reference` drift;
- select the segment or flat lane-path form;
- define or alter source-role, resource-class, sensitivity, public-safe geometry, or infrastructure-exposure rules;
- decide source rights, redistribution, or live-source activation;
- create a parallel contract, schema, policy, registry, taxonomy, receipt, proof, or release authority;
- establish universal config discovery, precedence, or unknown-key behavior;
- authorize direct public access to internal or canonical stores;
- change the separation among physical geology, regulatory status, ownership, interpretation, model, evidence, release, correction, and publication; or
- authorize direct public exposure of exact restricted geology or infrastructure detail.

Configuration must not be used to settle those decisions indirectly.

[Back to top](#top)

---

## Rollback and correction

Before merge, rollback means closing the unmerged pull request and abandoning the scoped branch when separately authorized.

After merge, create a transparent revert commit or revert pull request that restores the prior known-good README or configuration version. Do not force-push or rewrite shared history.

For a future payload correction:

1. disable or stop selecting the affected configuration through the verified consumer mechanism;
2. stop any watcher, renderer, scheduled process, or interpretation workflow that depends on the faulty selection;
3. preserve the faulty version and evidence needed for review;
4. identify affected objects, joins, estimates, interpretations, caches, tiles, cross-sections, 3D scenes, exports, and narratives without exposing protected locations;
5. assess whether physical, regulatory, ownership, resource-class, or source-role claims were collapsed;
6. assess whether exact or reconstructable sensitive information was exposed;
7. restore the prior known-good version or safe disabled state;
8. re-run validation and negative cases;
9. create any required correction, redaction, withdrawal, release, or rollback records in their canonical homes; and
10. verify that no public surface continues to serve an unauthorized, stale, misclassified, or reconstructable derivative.

A Git revert does not itself revoke exposed data, correct released artifacts, reverse a regulatory or operational claim, or establish KFM publication lineage.

[Back to top](#top)

---

## Last reviewed

**2026-07-13**, against `main@787d2fce458230eb556d205203b563adea2a9717`.

Review again before the first non-README payload, consumer binding, object-name selection, source-role profile, resource-class profile, public-safe geometry profile, source activation, interpretation workflow, or public-output integration.

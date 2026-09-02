<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-domain-habitat
title: Habitat Dashboard Specification
type: standard
version: v1.0.1
status: repository-grounded; specification-only; placement-hold; runtime-needs-verification; non-release; non-publication
owners:
  - "@bartytime4life — CONFIRMED GitHub review route through the repository default CODEOWNERS rule"
  - "Habitat domain steward — NEEDS VERIFICATION"
  - "Metric and observability steward — NEEDS VERIFICATION"
  - "Sensitivity and geoprivacy reviewer — NEEDS VERIFICATION"
owner_status: "CODEOWNERS confirms repository review routing only; domain, metric, source, sensitivity, evidence, policy, UI, release, and independent-review authority remain NEEDS VERIFICATION"
created: 2026-05-26
updated: 2026-08-29
policy_label: repository-facing; sensitivity-aware; no-restricted-payload
truth_posture: cite-or-abstain
owning_root: docs/
responsibility: "Specify a Habitat domain-health dashboard boundary, metric interpretation rules, finite states, sensitive-join controls, current implementation maturity, validation expectations, and correction behavior without creating Habitat truth, telemetry, policy, release, or publication authority."
current_path: docs/dashboards/domain/habitat.md
placement_status: "CONFIRMED existing path under canonical docs/ root; HOLD as part of the unadmitted docs/dashboards/ direct-child lane"
runtime_status: "NEEDS VERIFICATION — Explorer Habitat files are placeholders and no dashboard route, metric producer, telemetry series, query, deployed panel, or live feed was verified"
evidence_snapshot: main@1bc300c5aeaf5323edead670d648edfb8c3f21c2; prior target blob f7312a45157372a72600e738b14912bba23756d8; critical-habitat source-role validator blob 0e1c859b493f9c485885a1e4ae66ff60bf376a6d; focused test blob 3fb512a9812affb8caec9750fc29cd749f82cddf; focused workflow blob 704d911bd976acb65ba6beeadc5eb7df25660f73.
related:
  - ../README.md
  - ./README.md
  - ../DASHBOARD_CATALOG.md
  - ../INDICATOR_CATALOG.md
  - ../../domains/habitat/README.md
  - ../../domains/habitat/SENSITIVITY.md
  - ../../domains/habitat/MODEL_VS_OBSERVATION.md
  - ../../domains/habitat/MAP_UI_CONTRACTS.md
  - ../../../apps/explorer-web/src/features/domains/habitat/README.md
  - ../../../contracts/cross_domain/fauna_habitat/public_safe_assignment_profile.md
  - ../../../.github/workflows/domain-habitat.yml
  - ../../../.github/workflows/habitat-critical-habitat-source-role.yml
  - ../../../tools/validators/domains/habitat/validate_critical_habitat_source_role.py
  - ../../../tests/domains/habitat/test_critical_habitat_source_role.py
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../doctrine/directory-rules.md
tags: [kfm, dashboards, domain, habitat, evidence, source-role, land-cover, sensitivity, geoprivacy, finite-outcomes, cite-or-abstain]
notes:
  - "v1.0 is a same-path repository reconciliation of the v0.1 Atlas-derived proposal."
  - "v1.0.1 records the landed fixture-only critical-habitat source-role guard without upgrading policy, source, runtime, dashboard, or regulatory maturity."
  - "The dashboard specification reports posture; it does not create EvidenceBundles, PolicyDecisions, review decisions, release decisions, or Habitat truth."
  - "Current executable evidence is bounded to synthetic no-network validators and fixtures; UI and operational dashboard behavior remain unverified."
  - "This revision changes only docs/dashboards/domain/habitat.md. It does not execute a source, change policy, deploy an application, release data, or publish KFM knowledge."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat Dashboard Specification

> Repository-grounded specification for a future Habitat domain-health surface. It defines how a dashboard may report evidence, source-role, model, land-cover, sensitivity, cross-domain, release, and correction posture without becoming the authority for any of them.

> [!IMPORTANT]
> **Current state:** the specification file and supporting repository surfaces are **CONFIRMED** at the pinned base. The dashboard lane remains on a placement **HOLD** under the adopted Directory Rules, and Habitat dashboard runtime is **NEEDS VERIFICATION**. A Markdown file, workflow, fixture, map, metric, badge, or green check is not proof of a running dashboard or a released Habitat claim.

> [!CAUTION]
> **Habitat can become sensitive through composition.** A seemingly ordinary polygon, class, corridor, model surface, count, filter, or trend can disclose protected fauna or flora locations, steward-withheld knowledge, private-parcel relationships, corridor endpoints, or model support. Public outputs must be transformed and evaluated before they reach the client; client-side hiding is not a safety control.

> [!NOTE]
> Current executable Habitat evidence is narrow: a proposed-inactive land-cover materiality profile, a shared EvidenceBundle projection convergence check, a synthetic Fauna–Habitat candidate profile, and a fixture-only critical-habitat source-role guard. These checks prove only their fixture contracts. They do not admit a source, establish habitat or species truth, create regulatory authority, enforce production policy, authorize release, or publish data.

## Quick jump

- [1. Domain scope](#1-domain-scope)
- [2. Indicator subset](#2-indicator-subset)
- [3. Domain-specific indicators](#3-domain-specific-indicators-proposed)
- [Metric record and interpretation contract](#metric-record-and-interpretation-contract)
- [Source-role and claim boundaries](#source-role-and-claim-boundaries)
- [Sensitive joins and public-safe behavior](#sensitive-joins-and-public-safe-behavior)
- [Finite outcomes and negative states](#finite-outcomes-and-negative-states)
- [5. Implementation pointer](#5-implementation-pointer)
- [Validation and negative proof](#validation-and-negative-proof)
- [4. Ownership](#4-ownership)
- [6. Review cadence](#6-review-cadence)
- [7. Open questions](#7-open-questions)
- [8. Evidence basis](#8-evidence-basis--citations)
- [Correction and rollback](#correction-and-rollback)

---

<a id="1-domain-scope"></a>

## 1. Domain scope

Habitat is the landscape and model lane for habitat patches, land-cover observations and class systems, ecological systems, suitability, quality, uncertainty, connectivity, corridors, restoration opportunity, and stewardship zones. It does not own species occurrence truth, plant specimen truth, regulatory authority, or source admission.

### Belongs in this dashboard specification

- measurements of Habitat evidence resolution and citation readiness;
- source-role preservation, admission, rights, cadence, and stale-state posture;
- land-cover profile validation and material-change outcome summaries;
- model-versus-observation and modeled-versus-regulatory anti-collapse checks;
- public-safe Habitat × Fauna or Habitat × Flora join dispositions at an aggregation that cannot reveal protected detail;
- release, correction, withdrawal, cache-invalidation, and rollback readiness;
- explicit finite negative states and the evidence required to clear them;
- implementation maturity, metric ownership, producer identity, and known gaps.

### Does not belong in this dashboard specification

| Excluded responsibility | Owning boundary or disposition |
|---|---|
| Species occurrence or rare-plant truth | Fauna or Flora domain lane; Habitat may receive only a governed relationship or public-safe context |
| Habitat semantic contracts or machine shape | `contracts/domains/habitat/` and `schemas/contracts/v1/domains/habitat/` |
| Source admission, activation, rights, or terms | Governed source descriptors and activation decisions under the registry/source-governance boundary |
| Sensitivity, geoprivacy, or disclosure decisions | Accepted policy plus a recorded decision and required transform receipt |
| Raw source payloads, canonical lifecycle stores, or restricted geometry | Their governed lifecycle or restricted storage; never this document or an ordinary client |
| Telemetry storage, metric producers, queries, dashboards, or application code | Runtime, application, package, or infrastructure responsibility roots selected by implementation |
| Promotion, release, correction, withdrawal, rollback, or publication authority | Governed release and accountability object families |
| Scientific, legal, conservation, land-title, or regulatory determination | Applicable authoritative process and named reviewer; never a dashboard inference |

### Non-claims

This document does not establish a dashboard URL, application route, panel, query, database view, telemetry series, alert, SLO, metric threshold, source endpoint, active connector, policy decision, reviewer approval, release, deployment, or publication.

[Back to top](#top)

---

<a id="2-indicator-subset"></a>

## 2. Indicator subset

The following rows specify metric families, not current measurements. Each requires the record contract below, a verified producer, bounded data, and a named owner before a dashboard can present a health interpretation.

| Metric family | Numerator or outcome | Denominator or scope | Required evidence | Safe interpretation |
|---|---|---|---|---|
| Evidence resolution | Claim-bearing records whose `EvidenceRef` resolves to a valid shared `EvidenceBundle` | Eligible claim-bearing Habitat records in the same release, time, source-role, and audience scope | Resolver version, bundle identity, validator result, source and release refs | Reports evidence-link posture only; it does not prove claim correctness |
| Citation validation | Public or steward-visible claims with validated, audience-safe citations | Claims selected for the same surface and period | Citation-validation result, evidence bundle, rights and sensitivity state | Missing support becomes `ABSTAIN`; never silently drop the claim from the denominator |
| Source admission and currentness | Records whose source descriptor is admitted and current for the measurement time | Eligible records grouped by source identity, native version, role, and cadence | Descriptor, activation decision, source-head state, rights review | Repository YAML presence is not admission or currentness |
| Source-role preservation | Records retaining their admitted source role through the measured boundary | Records crossing that boundary | Input/output role, transform or model receipt, validator result | Any role collapse is a defect; promotion never upgrades authority |
| Land-cover materiality outcomes | Counts by `NON_EVENT`, `PROMOTION_CANDIDATE`, `HOLD`, and validation failure | Assessments produced by one profile version and analysis unit | Profile hash, input digests, fixture/live-source classification, validation result | The current profile is `PROPOSED_INACTIVE`; a candidate is not promotion |
| Model and observation separation | Surfaces with complete model card, uncertainty, fitness, source-role, and time labels | Eligible modeled Habitat surfaces | Model/run identity, source roles, uncertainty, evidence, review and release refs | Suitability is not occurrence; modeled habitat is not regulatory critical habitat |
| Sensitive-join disposition | Counts by `ALLOW`, `ABSTAIN`, `DENY`, and `ERROR` for one accepted pair profile | Join assessments with the same profile, audience, sensitivity, time, and geometry class | Endpoint roles, evidence refs, inherited sensitivity, profile version, policy/review state | `ALLOW` may mean review candidate only; never publication authority |
| Public-safe transform coverage | Released outputs with the required generalization, redaction, aggregation, or geoprivacy receipt | Released outputs whose inputs or joins require a transform | Transform receipt, before/after class, policy decision, review and release refs | Do not expose missing-transform counts if the count itself leaks protected existence |
| Correction and withdrawal propagation | Affected dashboard projections invalidated or replaced within the declared window | Affected panels, caches, exports, indexes, and AI summaries named by dependency inventory | Correction/withdrawal record, prior/new IDs, invalidation evidence, rollback target | Measures propagation mechanics, not substantive correction quality |

### Health targets

No universal percentage, latency, quarterly cadence, or alert threshold is accepted by current evidence for this dashboard. A future threshold must identify:

1. metric and contract version;
2. numerator, denominator, exclusions, and zero-denominator behavior;
3. source, audience, spatial unit, time window, and source-role partitions;
4. measured baseline and owner;
5. warning and breach semantics;
6. response playbook and rollback;
7. sensitivity review showing the metric cannot become a side channel.

Until then, the surface may report measured finite outcomes with their limitations but must not color them green, label them compliant, or infer health from absence of data.

[Back to top](#top)

---

<a id="3-domain-specific-indicators-proposed"></a>

## 3. Domain-specific indicators (PROPOSED)

| Candidate indicator | Habitat-specific question | Evidence required before adoption | Current state |
|---|---|---|---|
| Land-cover class-scheme/version skew | Are compared observations and derived products bound to compatible native class schemes, crosswalks, and vintages? | Accepted metric contract, source descriptors, crosswalk profile, fixtures, validator, producer, owner | `PROPOSED` |
| Material-change disposition profile | Which declared changes are `NON_EVENT`, `PROMOTION_CANDIDATE`, `HOLD`, or invalid under one profile version? | Current materiality profile and deterministic assessment output; scientific/operational threshold review for live use | Executable fixture slice; live use `HOLD` |
| Modeled/regulatory anti-collapse | Is every modeled suitability or habitat output kept distinct from designated critical habitat and observed occurrence? | Admitted source roles, model card, policy, negative fixtures, validator, API/UI tests | Fixture-only validator, negative tests, and focused workflow are `CONFIRMED`; policy activation, source admission, model-card binding, API/UI behavior, and runtime enforcement remain `HOLD` / `NEEDS VERIFICATION` |
| Uncertainty and fitness coverage | Do modeled views carry uncertainty, intended-use, unsupported-use, source-role, and valid-time context? | Accepted model/run contracts, validators, representative fixtures, release binding | `NEEDS VERIFICATION` |
| Habitat × Fauna candidate disposition | Does the pair profile preserve evidence, source role, sensitivity, generalized geometry, and non-publisher effects? | Pair profile, ten-case synthetic fixture matrix, validator and tests | Fixture behavior `CONFIRMED`; relationship truth and runtime not established |
| Protected-detail side-channel review | Could polygons, vertex density, filters, counts, errors, timing, exports, or correlation reveal protected detail? | Threat model, adversarial fixtures, transform policy, receipts, public/steward parity tests | `NEEDS VERIFICATION` |
| Release and correction closure | Can every displayed Habitat value resolve to release, correction, withdrawal, and rollback state? | Release/correction contracts, dependency inventory, producer and UI tests | `NEEDS VERIFICATION` |

The numeric triggers in the current land-cover materiality profile belong only to that `PROPOSED_INACTIVE` profile. Their presence and deterministic fixture behavior do not make them accepted dashboard health targets or scientific thresholds.

[Back to top](#top)

---

## Metric record and interpretation contract

A future dashboard must not derive a health judgment from an unversioned scalar. Every metric record should carry or resolve:

| Field | Requirement |
|---|---|
| Identity | Stable metric ID, semantic version, producer ID/version, query or ruleset hash, and deterministic run ID where practical |
| Measurement | Outcome or numerator/denominator, unit, zero-denominator state, exclusions, confidence/uncertainty, and completeness |
| Scope | Domain/sublane, audience, source identity/role/version, spatial unit, geometry class, sensitivity class, and aggregation level |
| Time | Measurement window, source valid time, observed/computed time, freshness basis, and stale-state rule |
| Evidence | EvidenceRefs that resolve to EvidenceBundles before claim-bearing interpretation; validation result and citation state |
| Governance | Policy decision, reviewer state, obligations, release ID, correction/supersession/withdrawal state, and rollback target where applicable |
| Safety | Transform or geoprivacy receipt when required; public-safe reason vocabulary; side-channel review state |
| Interpretation | Bounded meaning, limitations, non-claims, warning/breach semantics, and owner response path |

### Aggregation rules

- Never combine unlike source roles, profile versions, audiences, sensitivity classes, spatial units, time windows, or denominator definitions into one percentage.
- Preserve missing, denied, restricted, stale, malformed, and producer-error states; do not coerce them to zero.
- Do not publish small cells, filtered counts, exact vertices, transform parameters, or different error behavior that could reveal protected existence or location.
- Where the denominator cannot be disclosed safely, report a bounded qualitative state or deny the metric rather than exposing the denominator.
- Trend comparisons require compatible metric, producer, source, class scheme, crosswalk, time, and correction state.
- Dashboard aggregation does not upgrade a source role or create release/publication authority.

[Back to top](#top)

---

## Source-role and claim boundaries

Source role is declared at admission and preserved through every downstream product. The dashboard must render the role that supports the displayed claim and keep derived products separate from their inputs.

| Source/product role | Permitted dashboard statement | Prohibited collapse |
|---|---|---|
| `observed` | Bounded observation/inventory result with method, source, time, evidence, and limits | Observation as regulatory designation, universal habitat truth, or proof of species presence |
| `regulatory` | Current designation/status only within the issuing authority, version, geography, and valid time | Model or inventory relabeled as regulatory authority |
| `modeled` | Suitability, classification, prediction, or scenario with model card, support, uncertainty, fitness, and valid time | Model as observation, occurrence, critical-habitat designation, or causal fact |
| `aggregate` | Summary for its declared population/unit and suppression/public-safe rules | Aggregate as record-level truth or a path to reconstruct records |
| `administrative` | Stewardship, management, or jurisdiction context within the source's authority | Administrative boundary as ecological, title, ownership, or public-access truth |
| `candidate` | Item awaiting evidence, policy, review, or release disposition | Candidate as accepted relationship, catalog truth, or publication |
| `synthetic` | Fixture, demonstration, or deterministic test behavior | Fixture as real Habitat, source, species, release, or public-safety evidence |

### Habitat-specific anti-collapse rules

- A suitability raster is not a species occurrence.
- A modeled Habitat patch is not designated critical habitat.
- A land-cover classification is not a complete ecological-system or habitat-quality determination.
- A habitat association is not proof that a species occurs at a place or time.
- A public-safe join candidate is not relationship truth, policy approval, release approval, or public-use authorization.
- A map feature, tile, metric, chart, screenshot, AI summary, or dashboard panel is an interpretive carrier, not sovereign truth.

[Back to top](#top)

---

## Sensitive joins and public-safe behavior

Sensitivity is evaluated on the produced output, not inferred once from a source label. The strictest applicable source, join, rights, sovereignty, stewardship, living-person/private-land, and audience constraint wins.

### Fail-closed requirements

1. Resolve evidence, source role, rights, sensitivity, policy, review, release, valid time, correction, and audience before presenting a consequential claim.
2. Transform exact or reconstructive detail before tile, API, export, cache, search, analytics, screenshot, or AI-context generation.
3. Require generalized geometry and public-safe endpoint state for a public Habitat × Fauna candidate; restricted exact geometry remains denied.
4. Preserve `ABSTAIN` when evidence is absent, source roles conflict, or restricted generalized context needs review.
5. Keep internal reason codes, protected counts, transform parameters, and withheld existence out of ordinary public responses.
6. Apply the same safety boundary to maps, tables, filters, counts, comparisons, downloads, accessibility text, logs, timing, errors, and generated language.
7. Fail closed when the policy evaluator, EvidenceBundle resolver, transform receipt, reviewer state, or release state is unavailable.

### Visibility matrix

| State | Steward surface | Ordinary/public surface |
|---|---|---|
| Public-safe, released, evidence-backed aggregate | May show bounded detail and audit links according to role | May show only the released public-safe projection |
| Restricted generalized candidate needing review | Show only to authorized reviewers with obligations and audit trail | `ABSTAIN` or `DENY`; do not reveal candidate existence |
| Restricted exact or reconstructive geometry | Deny ordinary use; route through restricted review if a governed workflow exists | `DENY`; no differentiated count, filter, map, export, or error side channel |
| Missing EvidenceBundle, rights, policy, review, or release state | `HOLD`, `ABSTAIN`, or `ERROR` according to the governing interface | `ABSTAIN`, `DENY`, or public-safe `ERROR`; never optimistic fallback |
| Corrected, withdrawn, or superseded input | Show correction lineage and required action | Remove/invalidate the prior projection and link a safe correction notice when permitted |

[Back to top](#top)

---

## Finite outcomes and negative states

A future dashboard must preserve the finite outcome emitted by the governing interface:

| Outcome | Dashboard behavior |
|---|---|
| `ANSWER` | Render only a released, audience-appropriate, evidence-backed value with source role, time, limitations, and correction state reachable |
| `ALLOW` | Interpret strictly according to the producing contract; for the current Fauna–Habitat profile it means only a reviewable synthetic candidate |
| `ABSTAIN` | State that the required evidence or disposition is unavailable; do not substitute zero, stale data, prior values, or generated prose |
| `DENY` | Withhold protected detail and use a public-safe reason without confirming protected existence |
| `ERROR` | Surface bounded operational failure; do not expose internals or fall back to unsafe data |
| `HOLD` | Show implementation/readiness or review state only; never convert it into domain truth, release status, or a healthy score |
| `UNKNOWN` / `NEEDS VERIFICATION` | Keep uncertainty visible and exclude the value from positive health claims |

The panel itself needs explicit loading, unavailable, stale, restricted, malformed, corrected, withdrawn, superseded, and producer-error states. Status must remain understandable without color alone.

[Back to top](#top)

---

<a id="5-implementation-pointer"></a>

## 5. Implementation pointer

### Current repository evidence

| Surface | Pinned observation | What it proves | What it does not prove |
|---|---|---|---|
| [`apps/explorer-web/.../habitat/README.md`](../../../apps/explorer-web/src/features/domains/habitat/README.md) | Detailed proposed feature boundary | Intended governed API, sensitivity, evidence, release, correction, and UI constraints | Route, runtime, or deployment |
| [`EvidenceDrawer.tsx`](../../../apps/explorer-web/src/features/domains/habitat/EvidenceDrawer.tsx) | Literal greenfield placeholder exporting `placeholder = true` | Path exists | Evidence Drawer behavior or EvidenceBundle resolution |
| [`FocusFlow.tsx`](../../../apps/explorer-web/src/features/domains/habitat/FocusFlow.tsx) | Literal greenfield placeholder exporting `placeholder = true` | Path exists | Focus Mode, citation, or AI behavior |
| [`layers.ts`](../../../apps/explorer-web/src/features/domains/habitat/layers.ts) | Literal greenfield placeholder exporting `placeholder = true` | Path exists | Layer adapter, released tiles, or MapLibre behavior |
| [`evidence_drawer_payload.schema.json`](../../../schemas/contracts/v1/domains/habitat/evidence_drawer_payload.schema.json) | Proposed schema stub with `additionalProperties: true` | Placeholder shape exists | Complete, accepted, or enforced payload contract |
| [`evidence_bundle.schema.json`](../../../schemas/contracts/v1/domains/habitat/evidence_bundle.schema.json) | Proposed projection of the shared EvidenceBundle schema | Projection relationship exists | Independent evidence semantics or public-release authority |
| [Habitat land-cover materiality workflow](../../../.github/workflows/habitat-land-cover-materiality.yml) | Deterministic synthetic no-network validator/test commands | Bounded fixture-profile conformance when exact-head checks pass | Source admission, scientific threshold acceptance, promotion, or release |
| [EvidenceBundle convergence workflow](../../../.github/workflows/habitat-evidence-bundle-convergence.yml) | Shared-fixture projection convergence | Projection does not diverge from shared shape within test scope | Evidence truth, UI resolution, policy, or release |
| [Fauna–Habitat candidate workflow](../../../.github/workflows/fauna-habitat-public-safe-assignment.yml) | Ten-case synthetic, no-coordinate, non-publisher profile validation | Pair-profile fixture behavior | Real relationship, geoprivacy transform, policy review, or publication |
| [Habitat domain workflow](../../../.github/workflows/domain-habitat.yml) | Executable materiality slice plus explicit proof and release-dry-run holds | Current workflow maturity and hold semantics | Proof pack, release candidate, deployment, or publication |
| [Critical-habitat source-role workflow](../../../.github/workflows/habitat-critical-habitat-source-role.yml) | Deterministic fixture-only validator and negative tests | Regulatory designation and modeled habitat remain separate source roles; presence and movement claims are denied within fixture scope | Source admission, policy activation, regulatory authority, occurrence truth, runtime enforcement, release, or publication |

### Current maturity summary

- **CONFIRMED:** documentation, contract/schema/policy/test paths, placeholder UI files, bounded synthetic validator slices, path-scoped workflows, one executable synthetic cross-domain candidate profile, and the fixture-only critical-habitat source-role guard.
- **PROPOSED:** dashboard metrics, producers, panels, queries, routes, telemetry, thresholds, SLOs, and alerts.
- **NEEDS VERIFICATION:** application wiring, governed API envelopes, source admission/currentness, production policy enforcement, public-safe transform pipeline, release artifacts, metric ownership, hosted controls, deployment, and runtime observation.
- **UNKNOWN:** a running Habitat dashboard URL, active telemetry store, current dashboard feed, and production health posture.

### Runtime requirements

A future implementation must:

1. consume governed API envelopes or verified released public-safe artifacts, never direct RAW/WORK/QUARANTINE/PROCESSED/CATALOG or registry internals;
2. validate response, metric, evidence, source-role, sensitivity, transform, release, and correction contracts before render;
3. prevent protected dimensions and internal reason detail from reaching ordinary clients, analytics, logs, caches, exports, or AI context;
4. preserve source role, model/observation distinction, native class scheme, spatial/time scope, and uncertainty;
5. expose accessible finite states rather than inventing values;
6. bind each metric to a deterministic producer/query identity and reviewable release/build manifest where appropriate;
7. provide correction, withdrawal, cache invalidation, and rollback behavior with representative negative tests;
8. keep renderer and dashboard output interpretive, with EvidenceBundle resolution available before consequential claims.

[Back to top](#top)

---

## Validation and negative proof

### Documentation validation for this revision

| Check | Required result |
|---|---|
| Metadata | One parseable `KFM_META_BLOCK_V2`; stable `doc_id`, path, created date, and current evidence snapshot |
| Structure | One H1, logical heading order, balanced fences, final newline, no tabs or trailing whitespace |
| Compatibility | Preserve `top` and legacy section anchors `1-domain-scope` through `8-evidence-basis--citations` |
| Links | Every repository-relative destination resolves at the exact branch head |
| Claim boundary | Current behavior cites pinned repository evidence; proposals, holds, unknowns, and non-effects remain explicit |
| Sensitive content | No exact protected location, restricted payload, private endpoint, credential, transform secret, or revealing threshold is introduced |
| Catalog parity | The shared catalog row matches this spec's current documents/source/runtime posture |
| Receipt | Final AI-authored bytes are SHA-256-bound by a pending-review generated receipt |

### Repository-native executable evidence

These commands are copied from current workflows and identify bounded evidence that a future implementer may rerun in an isolated, dependency-complete checkout. They are not claimed as executed by this documentation revision.

```bash
python -m unittest discover \
  --start-directory tests/validators/domains/habitat \
  --pattern 'test_land_cover_materiality.py' \
  --verbose
python tools/validators/domains/habitat/validate_land_cover_materiality.py --fixtures

python -m unittest -v tests.domains.habitat.test_critical_habitat_source_role

python -m unittest -q \
  tests.validators.domains.habitat.test_evidence_bundle_schema_convergence
python tools/validators/validate_habitat_evidence_bundle_projection.py --fixtures

python tools/validators/cross_domain/fauna_habitat/validate_public_safe_assignment.py --fixtures
python -m pytest \
  tests/joins/test_join_candidates.py \
  tests/cross_domain/fauna_habitat/test_public_safe_assignment.py \
  -q --strict-config --strict-markers
```

### Future implementation fixture matrix

| Case | Expected outcome | What it proves |
|---|---|---|
| Released, evidence-backed public-safe Habitat aggregate | `ANSWER` | Narrow positive path only |
| EvidenceRef missing or unresolved | `ABSTAIN` | Cite-or-abstain |
| Restricted exact Fauna geometry joined to Habitat | `DENY` | Exact protected geometry remains blocked |
| Restricted generalized Fauna context | `ABSTAIN` pending sensitivity review | Generalization alone is not approval |
| Modeled Habitat endpoint in an observed-role expectation | `ABSTAIN` pending source-role review | Source-role anti-collapse |
| Suitability presented as occurrence or critical-habitat designation | `DENY` or `ABSTAIN` | Model/observation/regulatory separation |
| Missing rights, policy, review, release, or transform receipt | `HOLD`, `ABSTAIN`, or `DENY` | No unsafe allow fallback |
| Policy evaluator or EvidenceBundle resolver unavailable | `ERROR` | Dependency failure is not zero or allow |
| Small cell, filter, count, timing, or error reveals protected existence | `DENY`; indistinguishable public-safe response | Adversarial side-channel safety |
| Metric producer returns malformed denominator or mixed versions | `ERROR` / metric unavailable | No false precision or invalid aggregation |
| Corrected or withdrawn input | Prior panel, export, cache, index, and AI summary invalidated | Correction propagation |
| Synthetic fixture output | Labeled synthetic and non-publishing | Fixture anti-collapse |

Passing Markdown, schema, fixture, validator, workflow, or UI tests proves only their declared scope. It does not establish scientific correctness, source admission, rights, sensitivity clearance, policy enforcement, review approval, release, deployment, or publication.

[Back to top](#top)

---

<a id="4-ownership"></a>

## 4. Ownership

| Role | Current state | Required responsibility |
|---|---|---|
| GitHub review route | `@bartytime4life` through the default CODEOWNERS rule | Repository review routing only; not domain or release approval |
| Habitat domain steward | `NEEDS VERIFICATION` | Domain meaning, source-role interpretation, model/observation separation, metric fitness |
| Source/rights steward | `NEEDS VERIFICATION` | Source admission, native version, rights, terms, attribution, cadence, withdrawal |
| Sensitivity/geoprivacy reviewer | `NEEDS VERIFICATION` | Protected-species, rare-plant, private-land, stewardship, join, reconstruction, and side-channel risk |
| Metric/observability owner | `NEEDS VERIFICATION` | Metric contract, producer, denominator, baseline, thresholds, SLO, alert, and response playbook |
| Evidence/policy reviewer | `NEEDS VERIFICATION` | EvidenceBundle resolution, policy binding, obligations, finite outcomes, negative proof |
| UI/accessibility reviewer | `NEEDS VERIFICATION` | Governed API boundary, negative states, non-color cues, keyboard/screen-reader behavior, export safety |
| Release/correction reviewer | `NEEDS VERIFICATION` | Release binding, correction, withdrawal, invalidation, supersession, and rollback closure |
| Independent reviewer | `NEEDS VERIFICATION` | Required for policy-significant, model-significant, or sensitivity-significant interpretation changes |

The document author, metric producer, dashboard implementer, domain reviewer, sensitivity reviewer, and release approver must not be silently treated as one authority.

[Back to top](#top)

---

<a id="6-review-cadence"></a>

## 6. Review cadence

No fixed quarterly, annual, or source-release cadence is accepted for this dashboard. The accountable owners should establish a review schedule only after metric producers, source cadences, source versions, policy versions, release obligations, and correction paths are known.

Recheck this specification when:

- the dashboard lane, catalog, indicator catalog, Directory Rules, or an accepted ADR changes;
- a Habitat source descriptor is admitted, revoked, corrected, or changes role, rights, terms, cadence, schema, class system, or sensitivity;
- the land-cover materiality profile or another domain profile changes version, threshold, analysis unit, status, or live-source posture;
- a Habitat × Fauna/Flora relationship contract, transform, policy, fixture, validator, or release path changes;
- the EvidenceBundle projection, Evidence Drawer payload, governed API envelope, Explorer component, route, or export behavior becomes reviewable;
- a metric producer, query, panel, threshold, SLO, alert, access policy, or telemetry store is introduced or changed;
- a correction, withdrawal, supersession, cache invalidation, or rollback path changes;
- a rights, sensitivity, protected-location, private-land, stewardship, reconstruction, or side-channel concern is reported;
- a hosted check or runtime observation shows catalog, contract, source-role, release, or public/steward parity drift.

[Back to top](#top)

---

<a id="7-open-questions"></a>

## 7. Open questions

| ID | Question | State | Closure evidence |
|---|---|---|---|
| `DASH-HAB-01` | Which accepted machine contract owns Habitat dashboard metric records? | `NEEDS VERIFICATION` | Contract, schema, fixtures, validator, registry, producer, consumer, and migration decision |
| `DASH-HAB-02` | Which application and route own the steward and ordinary/public Habitat views? | `NEEDS VERIFICATION` | Non-placeholder implementation, ownership, access policy, tests, build and deployment evidence |
| `DASH-HAB-03` | Which source descriptors are admitted and current, and which registry topology is authoritative? | `HOLD` | Accepted topology decision, descriptors, activation decisions, rights/currentness review, no divergent writable copies |
| `DASH-HAB-04` | Which model, uncertainty, fitness, and model-card fields are required for every suitability view? | `NEEDS VERIFICATION` | Accepted contracts, schemas, validators, fixtures, model/run receipts, domain review |
| `DASH-HAB-05` | Which modeled-versus-regulatory negative tests and policy rules are accepted and executable? | `HOLD` | Accepted ADR/policy, representative fixtures, validator, CI binding, API/UI tests |
| `DASH-HAB-06` | Which geoprivacy transforms and disclosure tests govern Habitat × Fauna/Flora outputs? | `HOLD` | Accepted transform profile, sensitivity policy, receipts, adversarial tests, reviewer disposition |
| `DASH-HAB-07` | How is every public claim bound to EvidenceBundle, release, correction, and rollback state? | `NEEDS VERIFICATION` | Resolver, release manifest, correction dependency graph, public/steward parity tests |
| `DASH-HAB-08` | What metric baselines, warning bands, SLOs, and review cadence are justified? | `PROPOSED` | Measured baseline, named owner, sensitivity review, response playbook, rollback |
| `DASH-HAB-09` | How are protected dimensions excluded from logs, analytics, caches, exports, screenshots, and AI context? | `NEEDS VERIFICATION` | Data-flow inventory, threat model, negative tests, runtime observation |
| `DASH-HAB-10` | Which compatibility paths under Habitat contracts/schemas/registries survive, and how are consumers migrated? | `HOLD` for structural change | Accepted ADR/migration note, consumer inventory, redirect/deprecation plan, rollback target |
| `DASH-HAB-11` | Which hosted checks and branch controls are required for this specification and future implementation? | `UNKNOWN` | Current repository ruleset and branch-protection evidence |

[Back to top](#top)

---

<a id="8-evidence-basis--citations"></a>

## 8. Evidence basis and repository references

### Current repository references

- [Dashboard lane boundary](../README.md)
- [Per-domain dashboard index](./README.md)
- [Dashboard catalog](../DASHBOARD_CATALOG.md)
- [Indicator catalog](../INDICATOR_CATALOG.md)
- [Habitat domain boundary](../../domains/habitat/README.md)
- [Habitat sensitivity posture](../../domains/habitat/SENSITIVITY.md)
- [Habitat source boundary](../../domains/habitat/SOURCES.md)
- [Habitat model-versus-observation boundary](../../domains/habitat/MODEL_VS_OBSERVATION.md)
- [Habitat map and UI contract](../../domains/habitat/MAP_UI_CONTRACTS.md)
- [Habitat verification backlog](../../domains/habitat/VERIFICATION_BACKLOG.md)
- [Explorer Habitat feature boundary](../../../apps/explorer-web/src/features/domains/habitat/README.md)
- [Habitat contracts boundary](../../../contracts/domains/habitat/README.md)
- [Fauna–Habitat public-safe candidate profile](../../../contracts/cross_domain/fauna_habitat/public_safe_assignment_profile.md)
- [Habitat EvidenceBundle projection](../../../schemas/contracts/v1/domains/habitat/evidence_bundle.schema.json)
- [Habitat Evidence Drawer payload stub](../../../schemas/contracts/v1/domains/habitat/evidence_drawer_payload.schema.json)
- [Occurrence geoprivacy policy scaffold](../../../policy/domains/habitat/occurrence_geoprivacy.rego)
- [Model-versus-observation policy scaffold](../../../policy/domains/habitat/model_vs_observation.rego)
- [Fauna–Habitat candidate tests](../../../tests/cross_domain/fauna_habitat/test_public_safe_assignment.py)
- [Critical-habitat source-role validator](../../../tools/validators/domains/habitat/validate_critical_habitat_source_role.py)
- [Critical-habitat source-role tests](../../../tests/domains/habitat/test_critical_habitat_source_role.py)
- [Habitat domain workflow](../../../.github/workflows/domain-habitat.yml)
- [Critical-habitat source-role workflow](../../../.github/workflows/habitat-critical-habitat-source-role.yml)
- [Habitat land-cover materiality workflow](../../../.github/workflows/habitat-land-cover-materiality.yml)
- [Habitat EvidenceBundle convergence workflow](../../../.github/workflows/habitat-evidence-bundle-convergence.yml)
- [Fauna–Habitat candidate workflow](../../../.github/workflows/fauna-habitat-public-safe-assignment.yml)
- [Repository review routing](../../../.github/CODEOWNERS)
- [Accepted Directory Rules decision](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [Directory Rules v2](../../doctrine/directory-rules.md)
- [Repository drift register](../../registers/DRIFT_REGISTER.md)
- [Repository verification backlog](../../registers/VERIFICATION_BACKLOG.md)

### Evidence limits

| Evidence class | What it supports | What it cannot prove |
|---|---|---|
| Current file/tree bytes | Path presence, exact content, declared status, and bounded inventory | Runtime behavior, correctness, enforcement, release, or publication |
| Placeholder UI/schema/policy/test file | Explicit incompleteness and current intended boundary | Implemented behavior, accepted contract, production policy, or passing assertion |
| Deterministic synthetic fixtures and validators | Behavior of the named profile and cases at the tested revision | Live-source fitness, real relationship truth, sensitive-output safety, or release readiness |
| Workflow definition | Trigger, declared commands, permissions, timeout, and hold semantics | Hosted success for another head, deployment, scientific truth, or policy approval |
| Documentation and proposed ADRs | Domain language, risks, intended object families, and open decisions | Adoption, enforcement, source currentness, or runtime maturity |
| Future metric output | Measured posture only when producer, inputs, scope, and contract are verified | Evidence, policy, review, release, or truth by itself |

No live Habitat source, external source page, private service, policy evaluator, browser runtime, telemetry store, release producer, or deployment was exercised for this documentation revision. Version-sensitive source terms, cadence, endpoint, licensing, designation, and scientific fitness remain subject to a separate authoritative-source review before operational use.

[Back to top](#top)

---

## Correction and rollback

### Documentation correction

Before merge, close or abandon the draft pull request; `main` remains unchanged. After an authorized merge, revert this specification, its shared catalog row, and its generated authoring receipt together, or apply a bounded forward correction against the actual merged bytes. Do not rewrite shared history.

### Future runtime correction

A running Habitat dashboard must support:

1. freeze, abstain, or deny an affected metric or panel when evidence, source, rights, sensitivity, policy, review, release, or correction state becomes invalid;
2. preserve prior metric, producer/query, source, profile, model/run, release, and correction identities;
3. invalidate unsafe panels, caches, exports, indexes, screenshots where governable, analytics dimensions, and AI summaries;
4. link the corrected state to the governing source correction, model/profile supersession, `CorrectionNotice`, withdrawal, release, or rollback record;
5. verify public/steward parity and absence of protected-detail side channels after correction;
6. retain an auditable rollback target and negative proof that unsafe or superseded detail is no longer exposed.

This documentation change creates no source, metric, runtime, data, cache, release, deployment, or public state requiring operational rollback.

### Material change ledger

| Material element | Disposition | Result |
|---|---|---|
| Stable path, `doc_id`, created date, `top`, and eight legacy section anchors | `KEEP` | Compatibility preserved |
| Atlas-derived fixed health thresholds and quarterly cadence | `REMOVE_WITH_EVIDENCE` | Replaced with evidence-bounded metric/threshold adoption rules |
| `apps/review-console/` and generic telemetry pointers | `REPAIR` | Replaced with current Explorer placeholders, contracts, schemas, validators, fixtures, and workflows |
| Habitat sensitivity coupling | `CLARIFY` | Expanded from polygon intersection language to output-tier, reconstruction, and multi-surface fail-closed rules |
| Source roles and model/observation boundaries | `ENRICH` | Added explicit anti-collapse matrix and claims boundary |
| Executable maturity | `SURFACE_CONFLICT` | Bounded fixture slices are real; dashboard/UI/policy runtime remains unverified |
| Evidence, finite states, validation, correction, and rollback | `ENRICH` | Added measurable contracts, negative proof, and non-effects |
| Decorative status badges | `REMOVE_WITH_EVIDENCE` | Replaced with text states supported by the pinned repository snapshot |

### Revision history

| Version | Date | Change | Non-effect |
|---|---|---|---|
| v0.1 | 2026-05-26 | Initial Atlas-derived per-domain indicator proposal | No implementation or publication |
| v1.0 | 2026-08-21 | Reconciled against current main; replaced unsupported thresholds/cadence and stale implementation pointers; added metric, source-role, sensitivity, finite-outcome, evidence, validation, correction, and rollback boundaries | No source admission, policy activation, runtime change, release, deployment, or publication |
| v1.0.1 | 2026-08-29 | Corrected the executable inventory for the landed fixture-only critical-habitat source-role guard and focused workflow | No source admission, policy activation, regulatory authority, runtime change, release, deployment, or publication |

[Back to top](#top)

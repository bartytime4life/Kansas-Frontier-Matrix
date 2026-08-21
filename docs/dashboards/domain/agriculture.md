<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-domain-agriculture
title: Agriculture Dashboard Specification
type: standard
version: v1.0
status: draft
owners:
  - "@bartytime4life — CONFIRMED CODEOWNERS review route only; accountable Agriculture, source, privacy, observability, release, and independent-review stewardship remain NEEDS VERIFICATION"
created: 2026-05-26
updated: 2026-08-21
policy_label: public
truth_posture: cite-or-abstain
owning_root: docs/
responsibility: >-
  Specify the human-facing Agriculture domain-health dashboard contract: which
  governed signals may be summarized, how source roles, time, evidence,
  sensitivity, finite outcomes, correction, and rollback remain visible, and
  which negative cases prevent a positive dashboard posture.
authority: >-
  Documentation and review guidance only. This file does not define Agriculture
  truth, admit a source, create a metric emitter, activate policy, validate a
  payload, approve review, promote lifecycle state, release an artifact, deploy
  a dashboard, or publish a claim.
current_path: docs/dashboards/domain/agriculture.md
placement_status: >-
  CONFIRMED existing path under the docs/ responsibility root; HOLD as part of
  the unadmitted docs/dashboards/ direct-child lane recorded by the
  repository-grounded parent README.
runtime_status: >-
  NEEDS VERIFICATION — repository documents and workflow definitions exist, but
  no running Agriculture dashboard, dashboard route, metric query, telemetry
  feed, access-control binding, or deployed panel was verified in this change.
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 464148b8b1b3dff558086b23fc5ec8fb16d60572
  authoring_base_commit: 51d45e45a56d19961a3014009b80c2c94b1107ee
  target_prior_blob: b641f57a3fd22fe088727663f8e44a503626ee92
  dashboard_catalog_prior_blob: 207aa04e27f750570d80cb9d23c285e35cad60fe
  dashboards_parent_blob: c3a0ab69cfc14cea7269cc2cdd853fbac3bb14e3
  domain_parent_blob: fc18e269e8f674688ea580ac384ba46c40304840
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  adr_0029_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  nass_source_record_blob: 7e2d31a23f5a4bc5e5a30b62b5cc814359a05566
  aggregation_thresholds_blob: 31947ca3e468a967aed3fc5d44699130b7d588fd
  farm_operator_join_policy_blob: 1b6128c4e2470f198edb6464424c6effc9d246dd
  nass_aggregate_test_blob: 97939b939122f029f35ecf12c81f5989df00ae63
  field_level_nass_test_blob: 06e3abeabc57b01d8073dc614cace9b404e204db
  agriculture_workflow_blob: d89d5db8861812f7b0a1024ae37a23ed5bd61354
inspection_boundary: >-
  Current-session GitHub reads covered the prior target, dashboard parents and
  catalog, CODEOWNERS, accepted Directory Rules decision, Agriculture domain
  and sensitivity documentation, NASS source documentation and placeholder
  record, connector coordination, semantic-contract and schema compatibility
  and domain lanes, policy scaffolds, placeholder NASS tests, Agriculture
  workflow definition, Review Console, Explorer Agriculture feature, Governed
  API Agriculture route documentation, and current-main Atmosphere/catalog
  reconciliation. No live source request, production database, telemetry store,
  metric query, policy evaluator, browser session, deployed dashboard, released
  carrier, correction cascade, or rollback drill was exercised.
related:
  - docs/dashboards/README.md
  - docs/dashboards/domain/README.md
  - docs/dashboards/DASHBOARD_CATALOG.md
  - docs/dashboards/INDICATOR_CATALOG.md
  - docs/domains/agriculture/README.md
  - docs/domains/agriculture/SENSITIVITY.md
  - docs/domains/agriculture/VERIFICATION_BACKLOG.md
  - docs/sources/catalog/usda/usda-nass-quickstats.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - contracts/agriculture/README.md
  - contracts/domains/agriculture/README.md
  - schemas/contracts/v1/agriculture/README.md
  - schemas/contracts/v1/domains/agriculture/README.md
  - policy/sensitivity/agriculture/aggregation_thresholds.yaml
  - policy/sensitivity/agriculture/farm_operator_join.rego
  - data/registry/sources/agriculture/nass_quickstats.yaml
  - connectors/nass/README.md
  - tests/domains/agriculture/test_nass_aggregate_only.py
  - tests/domains/agriculture/test_policy_denial_field_level_nass.py
  - .github/workflows/domain-agriculture.yml
  - apps/review-console/README.md
  - apps/explorer-web/src/features/domains/agriculture/README.md
  - apps/governed-api/src/routes/agriculture/README.md
tags: [kfm, dashboards, agriculture, evidence, source-role, aggregation, sensitivity, correction, rollback, specification]
notes:
  - "v1.0 replaces the May 2026 proposal-only dashboard text with a current-main repository reconciliation at the same path."
  - "The prior hard-coded NASS n<3/complementary-suppression claim is removed; preserve source-native withheld states and require an accepted KFM policy decision before treating any threshold as enforceable."
  - "The prior >99.9% and fixed review-cadence claims are removed because no accepted SLO, metric producer, denominator, or runtime feed was verified."
  - "Legacy section anchors are retained for inbound-link compatibility."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Agriculture Dashboard Specification

> **One-line purpose.** Define a reviewable Agriculture domain-health dashboard contract without mistaking a specification, metric, map, workflow, or generated summary for Agriculture truth, policy enforcement, release state, or publication authority.

> [!IMPORTANT]
> **A dashboard is a downstream carrier.** It may summarize verified `SourceDescriptor`, `EvidenceBundle`, validation, policy, review, release, correction, rollback, and telemetry records. It does not create those records, repair a missing evidence chain, turn a placeholder into enforcement, or authorize publication.

> [!CAUTION]
> **Agriculture metrics can become privacy side channels.** Field/operator/parcel combinations, private well or irrigation joins, proprietary yield, pesticide or application detail, small-cell existence signals, and reconstructive filters must fail closed. Client-side hiding, a private panel, or an aggregation label is not an upstream policy control.

> [!WARNING]
> **Do not hard-code an external disclosure threshold into this specification.** The prior text named an `n < 3` rule and complementary suppression without current authoritative evidence or an accepted KFM policy binding. Preserve source-native withheld and suppressed states, show the governing source and policy version, and return a bounded negative state when disclosure safety is unresolved.

**Quick navigation:** [Status](#status-and-evidence-boundary) · [Scope](#1-domain-scope) · [Repo fit](#repository-fit-and-authority) · [Maturity](#current-repository-maturity) · [Indicators](#2-indicator-subset) · [Agriculture metrics](#3-domain-specific-indicators-proposed) · [Sources](#source-role-time-and-anti-collapse-contract) · [Sensitivity](#sensitivity-rights-and-public-safe-presentation) · [Outcomes](#finite-outcomes-and-negative-states) · [Implementation](#5-implementation-pointer) · [Validation](#validation-and-negative-proof) · [Review](#4-ownership) · [Open work](#7-open-questions) · [Evidence](#8-evidence-basis--citations) · [Rollback](#correction-and-rollback)

---

## Status and evidence boundary

| Surface | Current repository-grounded state | Safe interpretation |
|---|---|---|
| This specification | Existing tracked file; prior blob `b641f57a3fd22fe088727663f8e44a503626ee92` | Same-path documentation modernization only |
| Dashboard lane | Parent path and specification inventory exist | `CONFIRMED` path; placement remains `HOLD`; no runtime inferred |
| Agriculture documentation | Domain, lifecycle, source, policy, sensitivity, API, map/UI, and backlog documents exist | Documentation and planning lineage; not machine or release proof |
| Review routing | CODEOWNERS routes repository review to `@bartytime4life` | GitHub routing only; not stewardship, independent review, policy approval, or release authority |
| NASS QuickStats record | `data/registry/sources/agriculture/nass_quickstats.yaml` is a four-field `PROPOSED` placeholder | Not an admitted `SourceDescriptor`; no live source activation |
| Agriculture policy | Aggregation thresholds are a placeholder; farm/operator join Rego is a `PROPOSED` default-deny scaffold | Fail-closed intent only; accepted production evaluation is unverified |
| NASS negative tests | Two named files contain documentation-only module docstrings | Filename presence is not executable proof |
| Agriculture CI | Workflow runs a bounded fixture-only CDL watcher proof and names dedicated NDVI/vegetation validators; broader validation, proof, and release remain held | Bounded implementation evidence only |
| UI/API runtime | Review Console, Explorer Agriculture, and Governed API Agriculture README boundaries exist | Route, query, panel, feed, access binding, deployment, and behavior remain `NEEDS VERIFICATION` |
| Release/publication | Workflow and release documentation preserve holds | No Agriculture dashboard release or public feed is established |

### Truth posture

- **CONFIRMED:** current repository paths and bytes and the inspected source, contract, schema, policy, test, workflow, and app/API documentation.
- **PROPOSED:** indicators, formulas, denominators, panels, queries, owner assignments, warning bands, review cadence, and runtime bindings.
- **UNKNOWN:** production records, deployed dashboard state, actual telemetry, effective policy decisions, public parity, correction propagation, and operational rollback.
- **NEEDS VERIFICATION:** every positive health status and every public-use claim.
- **HOLD:** structural dashboard-lane admission, source activation, operator/parcel exposure, unreviewed metric publication, release, deployment, and publication.

[Back to top](#top)

---

<a id="1-domain-scope"></a>

## 1. Domain scope

This specification covers the **governance and delivery health** of Agriculture-domain claims and carriers:

- aggregate crop, production, progress, rotation, and agricultural-economy context;
- crop-classification and remote-sensing/model products such as CDL- and NDVI-related derivatives;
- soil-crop suitability, irrigation, drought/stress, conservation, and supply-chain context when the owning domain and source role remain explicit;
- evidence resolution, source admission, temporal/version pins, validation, policy, review, release, correction, withdrawal, and rollback posture;
- public-safe map/API/UI delivery only after upstream controls close.

It does not own:

| Excluded responsibility | Owning surface |
|---|---|
| Agriculture domain meaning | [`docs/domains/agriculture/`](../../domains/agriculture/README.md) and accepted semantic contracts |
| Source identity, rights, activation, and cadence | Governed source registry and source-admission records |
| Machine payload shape | Accepted Agriculture schema lane |
| Sensitivity, aggregation, disclosure, and join decisions | Accepted policy plus accountable review |
| Metric production, queries, panels, routes, and storage | Governed implementation and operations roots |
| Evidence, receipts, proofs, catalogs, and lifecycle data | Their distinct `data/` object families |
| Promotion, release, correction, withdrawal, and rollback | `release/` and accountable decision records |
| Public Agriculture truth | Released, evidence-backed claims served through governed interfaces |

A dashboard may **report** that an upstream gate passed, failed, abstained, denied, errored, or is held. It must not become the gate itself without a separately accepted contract, schema, policy, validator, implementation, and review packet.

[Back to top](#top)

---

## Repository fit and authority

The current file remains under the existing `docs/` responsibility root. Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the exact [Directory Rules v2](../../doctrine/directory-rules.md) bytes; those rules make `docs/` the human explanation surface and require responsibility boundaries to remain visible.

| Repository surface | Relationship | Current posture |
|---|---|---|
| [`docs/dashboards/README.md`](../README.md) | Parent dashboard-lane boundary | Repository-grounded; nested-lane placement `HOLD` |
| [`docs/dashboards/domain/README.md`](./README.md) | Per-domain specification index and legacy template | Present; older proposal-era wording needs a separate reconciliation |
| [`DASHBOARD_CATALOG.md`](../DASHBOARD_CATALOG.md) | Human index of dashboard specifications | Updated with this specification; runtime parity remains unverified |
| [`INDICATOR_CATALOG.md`](../INDICATOR_CATALOG.md) | Human indicator mirror | Documentation only; not machine metric authority |
| [`docs/domains/agriculture/`](../../domains/agriculture/README.md) | Agriculture bounded-context documentation | Richer domain context; does not replace contracts, schemas, policy, or evidence |
| [`contracts/agriculture/`](../../../contracts/agriculture/README.md) | Older compatibility semantic lane | Transitional; do not expand into parallel authority |
| [`contracts/domains/agriculture/`](../../../contracts/domains/agriculture/README.md) | Doctrine-aligned semantic lane | Present, mixed maturity, incomplete family coverage |
| [`schemas/contracts/v1/agriculture/`](../../../schemas/contracts/v1/agriculture/README.md) | Flat compatibility/index schema lane | Index-only; no machine schemas belong there |
| [`schemas/contracts/v1/domains/agriculture/`](../../../schemas/contracts/v1/domains/agriculture/README.md) | Proposed domain machine-shape lane | Mixed scaffolds and bounded dedicated shapes; not full conformance |
| [`policy/sensitivity/agriculture/`](../../../policy/sensitivity/agriculture/) | Agriculture sensitivity policy surface | Inspected scaffolds; accepted evaluator and complete bundle unverified |
| [`apps/review-console/`](../../../apps/review-console/README.md) | Candidate role-gated review surface | README confirmed; dashboard implementation unknown |
| [`apps/explorer-web/.../agriculture/`](../../../apps/explorer-web/src/features/domains/agriculture/README.md) | Candidate public-safe Agriculture feature | README confirmed; route/panel/runtime unknown |
| [`apps/governed-api/.../agriculture/`](../../../apps/governed-api/src/routes/agriculture/README.md) | Candidate trust-membrane route source | README confirmed; handlers/runtime unknown |

This update creates no new authority root, move, rename, machine registry, or structural migration.

[Back to top](#top)

---

## Current repository maturity

| Capability | Current evidence | Dashboard consequence |
|---|---|---|
| Agriculture source documentation | QuickStats is described as `aggregate`; field/operator inference is denied in doctrine | Preserve aggregation unit and source role |
| Live NASS source admission | Placeholder record only | Show `NEEDS VERIFICATION`, `ABSTAIN`, or `HOLD`; do not report the source healthy |
| NASS connector | Coordination README records conflicting connector paths and no executable connector proof | Do not infer collection or freshness |
| Semantic meaning | Compatibility and domain lanes coexist | Report path/contract drift separately from domain health |
| Machine shape | Compatibility index plus domain schema lane; mixed maturity | Metrics cannot assume a complete payload contract |
| Aggregation thresholds | Placeholder YAML only | No numeric disclosure threshold is enforceable from repository evidence |
| Farm/operator join policy | Default-deny Rego scaffold | Preserve denial intent; do not claim runtime enforcement |
| NASS aggregate-only tests | Documentation-only placeholders | Do not count them as passing controls |
| Bounded executable slices | Synthetic CDL material-change watcher and dedicated NDVI/vegetation validator suites are named by the workflow | Report only their declared fixture scope and exact head |
| Broad validation/proof/release | Explicit workflow holds | No promotion or release inference |
| Public dashboard feed | Not verified | Invent no route, endpoint, or static data path |

> [!NOTE]
> Maturity is uneven. A substantive fixture-only validator can be **CONFIRMED** for its narrow behavior while the broader source, evidence, policy, proof, and release chain remains **HOLD**. The dashboard must preserve both facts instead of flattening them into one badge.

[Back to top](#top)

---

<a id="2-indicator-subset"></a>

## 2. Indicator subset

### Metric-record contract

A future emitted metric is not reviewable unless it identifies:

| Required field | Purpose |
|---|---|
| `metric_id` and `metric_version` | Stable identity and semantic version |
| `scope` | Domain, geography, product/source family, lifecycle, and release scope |
| `window_start`, `window_end`, `observed_at` | Explicit UTC measurement basis |
| `numerator` and `denominator` | Reconstructable rate; no hidden exclusions |
| `outcome_counts` and `reason_code_counts` | Preserve finite outcomes without leaking protected detail |
| `source_refs`, `evidence_refs`, `policy_refs`, `release_refs` | Resolve the governing trust chain |
| `query_or_producer_ref` | Deterministic producer identity, version, and digest |
| `freshness_state` | Current, stale, or unknown using the owning source contract |
| `limitations` | Blind spots, withheld dimensions, and non-effects |

A missing denominator, unknown window, unresolved evidence reference, unavailable policy version, or failed producer must not become zero or disappear from the rate.

### Core dashboard indicators

| Indicator | What it measures | Mandatory negative behavior |
|---|---|---|
| `evidence_resolution_closure` | Consequential claims whose `EvidenceRef` resolves to an admissible `EvidenceBundle` | Missing/conflicting evidence → `ABSTAIN`; resolver failure → `ERROR` |
| `source_admission_closure` | Operational feed refs resolving to admitted, non-placeholder source records | Placeholder, missing, revoked, or unreviewed source → `ABSTAIN` or `HOLD` |
| `source_role_preservation` | Accepted source roles remain explicit through query and presentation | Aggregate/model treated as field observation → `DENY` or `ABSTAIN` |
| `temporal_version_pin_coverage` | Crop year, product/vintage, retrieval, release, model/class-map, and correction time | Missing/incompatible support → `ABSTAIN` or `HOLD` |
| `withheld_state_preservation` | Withheld/suppressed/not-available states survive every authorized projection | Lost marker or reconstructed value → `DENY` or `ERROR` |
| `sensitive_join_denial_coverage` | Public requests involving operator, parcel, private field, proprietary yield, pesticide/application, or reconstructive irrigation joins | Unauthorized positive result → critical failure and correction review |
| `aggregation_receipt_coverage` | Released aggregate claims with resolving transform support and declared unit/method | Missing receipt or unit mismatch → `ABSTAIN` or `HOLD` |
| `modeled_product_disclosure` | Classified/inferred/model outputs carry version, quality, uncertainty, and non-observation labels | Model presented as observed truth → `DENY` or `ABSTAIN` |
| `cross_lane_reference_integrity` | Soil, Hydrology, Atmosphere, People/Land, Habitat, Hazards, and Infrastructure refs preserve owner, scale, time, and evidence | Unowned or incompatible join → `ABSTAIN` or `DENY` |
| `correction_invalidation_closure` | Corrections/withdrawals reach APIs, maps, exports, indexes, caches, dashboards, and AI summaries | Stale derivative remains visible → `ERROR` or `HOLD` |
| `validation_topology_drift` | Expected validators/tests/workflows/fixtures versus substantive implementations | Placeholder presented as enforcement → `HOLD` |
| `documentation_authority_drift` | Conflicting paths, stale inventories, unresolved owners, and proposal/current-state mismatch | Parallel writable authority or hidden drift → `HOLD` |

### Threshold posture

This specification does not ratify arbitrary service levels. Safety-critical closure indicators use an all-or-fail posture for **positive public claims** because one unsupported or unlawfully exposed claim is material. Warning bands, error budgets, trend windows, and review thresholds remain **PROPOSED** until an accepted metric contract and accountable owner establish them.

[Back to top](#top)

---

<a id="3-domain-specific-indicators-proposed"></a>

## 3. Domain-specific indicators — PROPOSED

| Candidate metric | Agriculture-specific question | Closure evidence |
|---|---|---|
| `aggregate_scope_match_rate` | Does displayed geography/time match the source aggregation unit and period? | Admitted source, aggregation receipt, geometry/time validator |
| `cdl_classmap_version_skew` | Are cross-year CDL comparisons mixing incompatible class maps or legends? | Product-year/class-map identity, transform receipt, comparison policy |
| `classification_confidence_disclosure` | Are confidence, uncertainty, quality, and applicability limits visible for modeled products? | Accepted model/output contract, validation, source/model version |
| `nass_field_inference_denial_rate` | Do field/operator requests over aggregate NASS material fail closed? | Executable negative fixtures, policy binding, governed API tests |
| `irrigation_join_review_state` | Are irrigation or well/field relations bounded by Hydrology ownership, rights, precision, and operator privacy? | Cross-lane contract, policy, safe transform, review record |
| `stress_indicator_time_alignment` | Are crop/stress summaries aligned to compatible observation/model periods and crop stages? | Atmosphere/Hydrology refs, temporal contract, uncertainty record |
| `small_cell_side_channel_review` | Could counts, filters, drill-downs, errors, or timing reveal a protected operator/field or suppressed value? | Adversarial disclosure tests, policy review, access-role matrix |
| `source_correction_latency` | How quickly do source corrections reach KFM candidates and released derivatives? | Immutable source versions, correction notice, dependency graph, invalidation receipts |
| `public_export_parity` | Do exports preserve dashboard aggregation, redaction, evidence, release, and correction state? | Export contract, parity fixtures, release manifest, correction tests |

These are candidate metric families, not evidence that emitters, queries, stores, panels, or accepted thresholds exist.

[Back to top](#top)

---

## Source role, time, and anti-collapse contract

| Source/product family | Permitted interpretation | Prohibited interpretation |
|---|---|---|
| NASS QuickStats/Census-style aggregates | Aggregate statistics at the admitted unit/period with withheld state preserved | Field/operator truth, parcel value, disaggregated estimate, or regulatory determination |
| CDL or another classified land-cover product | Versioned classification/model context with class-map identity and limitations | Confirmed planting decision, ownership, yield, or direct field observation |
| NDVI/HLS or another remote-sensing derivative | Derived vegetation/stress context within validated applicability | Causal diagnosis, crop-failure determination, pesticide need, or field truth |
| Irrigation/water-use context | Governed reference to Hydrology-owned observations or administrative context | Operator identity, private well-to-field exposure, water-right determination, or inferred intent |
| Soil/suitability context | Governed reference to Soil-owned survey/model evidence at valid scale | Field productivity guarantee or agronomic prescription |
| Atmosphere/hazard context | Governed observations/models with issue, valid, retrieval, and source-role time | Official warning authority, emergency direction, or causation claim |
| Agriculture economy/supply chain | Released public aggregate/contextual records | Private operator chain, confidential business detail, or individual financial conclusion |

Keep distinct where material: source reporting period, crop year, observed time, model/product valid time, retrieval time, processing time, release time, correction/withdrawal time, and dashboard computation time. A recent computation does not make an old source current.

[Back to top](#top)

---

## Sensitivity, rights, and public-safe presentation

The Agriculture [sensitivity document](../../domains/agriculture/SENSITIVITY.md) uses a working T0–T4 scheme but treats adoption and executable policy as unresolved. This dashboard reports the referenced tier/policy state without pretending the scheme or scaffolds are accepted enforcement.

| Material class | Default dashboard posture |
|---|---|
| Released state/county/district aggregate | Public-safe candidate only when evidence, source role, withheld-state, policy/review, release, and correction closure pass |
| Generalized modeled/classified context | Context only; uncertainty and source/model role visible |
| Field-candidate footprint | Reviewer-only by default; not public field truth |
| Operator-linked, parcel-resolving, proprietary yield, pesticide/application, or private farm record | `DENY` from ordinary dashboard/public client |
| Private well/irrigation plus field/operator join | `DENY` from public output |
| Small-cell, existence-sensitive, or reconstructive metric | Suppress the dimension or `ABSTAIN`/`DENY`; never reveal through filters, counts, errors, timing, or export |
| Unknown rights, terms, sensitivity, or review state | `HOLD`, `ABSTAIN`, or `DENY` as the governing interface specifies |

Aggregate denial counts are allowed only when the aggregate cannot reveal the protected case, location, existence, or reason. Internal reason codes require a public-safe projection.

[Back to top](#top)

---

## Finite outcomes and negative states

| Upstream outcome | Dashboard behavior |
|---|---|
| `ANSWER` | Display only with supporting evidence, policy, review, release, time, and scope; keep citations and limitations reachable |
| `ABSTAIN` | Show no citable bounded answer; never substitute zero, no issue, a prior value, or generated prose |
| `DENY` | Withhold protected detail and use a public-safe reason; do not disclose existence through count, filter, map state, or error differences |
| `ERROR` | Surface operational failure without unsupported fallback data or internal-sensitive detail |
| Repository/workflow `HOLD` | Present as implementation/readiness state only; never translate into domain truth or release state |
| `UNKNOWN` / `NEEDS VERIFICATION` | Keep uncertainty visible; do not render a green posture |

The panel needs explicit loading, unavailable, stale, denied, restricted, malformed, and producer-error states.

[Back to top](#top)

---

<a id="5-implementation-pointer"></a>

## 5. Implementation pointer

### Verified boundary surfaces

- [Review Console README](../../../apps/review-console/README.md) — candidate role-gated steward surface; runtime unverified.
- [Explorer Agriculture README](../../../apps/explorer-web/src/features/domains/agriculture/README.md) — candidate public-safe feature boundary; runtime unverified.
- [Governed API Agriculture README](../../../apps/governed-api/src/routes/agriculture/README.md) — candidate trust-membrane route boundary; handlers unverified.
- [Agriculture workflow](../../../.github/workflows/domain-agriculture.yml) — current fixture/readiness execution definition; not a dashboard feed.
- [NASS connector coordination](../../../connectors/nass/README.md) — source-intake placement conflict and placeholder maturity; not live access.

A future implementation must consume governed envelopes or released public-safe artifacts; validate metric records before rendering; preserve source role, unit, time, evidence, policy/review, release, and correction state; prevent protected dimensions from reaching clients, logs, analytics, caches, exports, or AI context; expose accessible finite negative states; version deterministic producers; bind builds/feeds to a reviewable manifest; and test correction, invalidation, and rollback.

This document establishes no dashboard URL, route, panel, database view, query, telemetry series, alert, SLO, source activation, accepted policy, public dataset, released layer, deployment, or publication.

[Back to top](#top)

---

## Validation and negative proof

### Documentation validation

| Check | Required result |
|---|---|
| Meta block | One parseable `KFM_META_BLOCK_V2`; valid `type`; stable `doc_id`; current evidence snapshot |
| Structure | One H1; logical headings; balanced fences; final newline; no tabs/trailing whitespace |
| Compatibility | Preserve `top` and legacy anchors `1-domain-scope` through `8-evidence-basis--citations` |
| Links | Every repository-relative destination and same-document fragment resolves |
| Claim boundary | Current behavior is evidence-bound; proposals and unknowns remain labeled |
| Sensitive content | No key, private endpoint, operator identity, parcel payload, protected location, or invented threshold |
| Diff scope | Specification, dashboard-catalog row, and one generated receipt |
| Receipt | Final specification and catalog SHA-256 values resolve from a schema-valid pending-review receipt |

### Future fixture matrix

| Case | Expected outcome |
|---|---|
| Released county aggregate with admitted source, evidence, policy, aggregation support, and correction state | `ANSWER` |
| Placeholder source record | `ABSTAIN` / `HOLD` |
| Source-native withheld value | `ABSTAIN` or public-safe withheld state |
| Missing/conflicting `EvidenceBundle` | `ABSTAIN` |
| Policy evaluator unavailable | `ERROR` |
| Field/operator request over aggregate NASS data | `DENY` |
| Parcel + operator + irrigation/well join | `DENY` |
| CDL/NDVI value presented as confirmed observation | `DENY` or `ABSTAIN` |
| Missing crop year/product/class-map version | `ABSTAIN` / `HOLD` |
| Correction supersedes an input | Invalidate prior dashboard/export/cache state |
| Filter/count reveals a protected case | `DENY` without a differentiated side channel |
| Producer fails or returns a malformed denominator | `ERROR` |

Passing Markdown, workflow, fixture, or unit checks proves only their declared scope. It does not admit a source, validate Agriculture semantics, activate policy, approve release, deploy a dashboard, or publish KFM knowledge.

[Back to top](#top)

---

<a id="4-ownership"></a>

## 4. Ownership and review

| Role | Current state | Required decision |
|---|---|---|
| GitHub review route | `@bartytime4life` through CODEOWNERS | Confirmed routing only |
| Agriculture domain steward | `NEEDS VERIFICATION` | Own interpretation and metric fitness |
| Source/rights steward | `NEEDS VERIFICATION` | Own source admission, terms, and currentness |
| Privacy/sensitivity reviewer | `NEEDS VERIFICATION` | Review operator/parcel/small-cell/reconstruction risk |
| Metric/observability owner | `NEEDS VERIFICATION` | Own producer, denominator, windows, and SLOs |
| Evidence/policy reviewer | `NEEDS VERIFICATION` | Verify evidence and policy binding |
| UI/accessibility reviewer | `NEEDS VERIFICATION` | Verify negative states and non-color cues |
| Release/correction reviewer | `NEEDS VERIFICATION` | Verify release, invalidation, withdrawal, and rollback |
| Independent reviewer | `NEEDS VERIFICATION` | Required for policy-significant or privacy-sensitive change |

The author, metric producer, implementer, and release approver must not be silently treated as one authority.

[Back to top](#top)

---

<a id="6-review-cadence"></a>

## 6. Review cadence and maintenance triggers

No fixed annual or semiannual cadence is claimed as accepted. An accountable owner should establish cadence after metric producers, source schedules, policy versions, and release obligations are known.

Recheck when the dashboard lane/catalog/Directory Rules changes; an Agriculture source changes role, terms, cadence, schema, aggregation, or withheld-state behavior; a connector/watcher/validator graduates from placeholder or fixture scope; contract/schema/policy compatibility changes; a panel/route/export becomes reviewable; correction or rollback behavior changes; a privacy or harmful-precision concern is reported; or hosted/runtime evidence reveals topology or parity drift.

[Back to top](#top)

---

<a id="7-open-questions"></a>

## 7. Open questions

| ID | Question | State |
|---|---|---|
| `DASH-AG-01` | Which accepted machine contract owns Agriculture dashboard metric records? | `NEEDS VERIFICATION` |
| `DASH-AG-02` | Which application and route own the steward-facing Agriculture view? | `NEEDS VERIFICATION` |
| `DASH-AG-03` | Which source/policy version governs withheld or disclosure-sensitive cells? | `HOLD` |
| `DASH-AG-04` | How are aggregation receipts resolved for every public aggregate claim? | `NEEDS VERIFICATION` |
| `DASH-AG-05` | Which CDL/classification/NDVI quality measures are fit for public interpretation? | `NEEDS VERIFICATION` |
| `DASH-AG-06` | What is the accepted Agriculture ↔ Hydrology irrigation/well join boundary? | `HOLD` |
| `DASH-AG-07` | What warning bands, error budgets, and review cadence are accepted? | `PROPOSED` |
| `DASH-AG-08` | How do corrections propagate to panels, exports, caches, search, AI, and maps? | `NEEDS VERIFICATION` |
| `DASH-AG-09` | How should the stale parent domain README be reconciled? | `NEEDS VERIFICATION` |
| `DASH-AG-10` | Which contract/schema compatibility paths survive and how are consumers migrated? | `HOLD` |
| `DASH-AG-11` | Which hosted checks and branch controls are required for future implementation? | `UNKNOWN` |

[Back to top](#top)

---

<a id="8-evidence-basis--citations"></a>

## 8. Evidence basis and repository references

- [Dashboard lane boundary](../README.md)
- [Per-domain dashboard index](./README.md)
- [Dashboard catalog](../DASHBOARD_CATALOG.md)
- [Indicator catalog](../INDICATOR_CATALOG.md)
- [Agriculture domain documentation](../../domains/agriculture/README.md)
- [Agriculture sensitivity posture](../../domains/agriculture/SENSITIVITY.md)
- [Agriculture verification backlog](../../domains/agriculture/VERIFICATION_BACKLOG.md)
- [USDA NASS QuickStats documentation](../../sources/catalog/usda/usda-nass-quickstats.md)
- [NASS connector coordination](../../../connectors/nass/README.md)
- [NASS placeholder source record](../../../data/registry/sources/agriculture/nass_quickstats.yaml)
- [Agriculture compatibility contract lane](../../../contracts/agriculture/README.md)
- [Agriculture domain contract lane](../../../contracts/domains/agriculture/README.md)
- [Agriculture compatibility schema lane](../../../schemas/contracts/v1/agriculture/README.md)
- [Agriculture domain schema lane](../../../schemas/contracts/v1/domains/agriculture/README.md)
- [Aggregation-threshold placeholder](../../../policy/sensitivity/agriculture/aggregation_thresholds.yaml)
- [Farm/operator join policy scaffold](../../../policy/sensitivity/agriculture/farm_operator_join.rego)
- [NASS aggregate-only test placeholder](../../../tests/domains/agriculture/test_nass_aggregate_only.py)
- [Field-level NASS denial test placeholder](../../../tests/domains/agriculture/test_policy_denial_field_level_nass.py)
- [Agriculture workflow](../../../.github/workflows/domain-agriculture.yml)
- [Repository review routing](../../../.github/CODEOWNERS)
- [Review Console boundary](../../../apps/review-console/README.md)
- [Explorer Agriculture boundary](../../../apps/explorer-web/src/features/domains/agriculture/README.md)
- [Governed API Agriculture boundary](../../../apps/governed-api/src/routes/agriculture/README.md)
- [Accepted Directory Rules decision](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [Directory Rules v2](../../doctrine/directory-rules.md)
- [Repository drift register](../../registers/DRIFT_REGISTER.md)
- [Repository verification backlog](../../registers/VERIFICATION_BACKLOG.md)

Repository bytes support path/content/status claims, not runtime, correctness, enforcement, release, or publication. Workflow definitions support declared commands and holds, not production behavior. Placeholder source/policy/test files prove incompleteness, not admission or enforcement. No external source page was checked in this documentation update; endpoint, disclosure, cadence, license, and product facts require separate authoritative review before operational use.

[Back to top](#top)

---

## Correction and rollback

Before merge, close or abandon the draft pull request; `main` remains unchanged. After an authorized merge, revert the single merge/reconciliation commit or apply a bounded forward correction against the merged bytes. Do not rewrite shared history.

A future running dashboard must freeze or deny affected metrics when evidence, policy, source, or release state becomes invalid; preserve prior identities and reasons; invalidate unsafe caches, exports, indexes, and AI summaries; link corrected state to the governing correction/withdrawal/release record; verify public/steward parity; and retain an auditable rollback target.

This documentation change creates no runtime, data, cache, release, deployment, or public state requiring operational rollback.

### Revision history

| Version | Date | Change | Non-effect |
|---|---|---|---|
| v0.1 | 2026-05-26 | Initial Atlas-derived proposal-only dashboard specification | No implementation or publication |
| v1.0 | 2026-08-21 | Reconciled against current main; removed unsupported thresholds/cadence; added evidence, maturity, metric, source-role, time, privacy, finite-outcome, validation, correction, and rollback boundaries | No source admission, policy activation, runtime change, release, deployment, or publication |

[Back to top](#top)

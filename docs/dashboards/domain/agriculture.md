<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-domain-agriculture
title: Agriculture Dashboard Specification
type: dashboard-spec; domain-health; boundary-compact
version: v1.0
status: repository-grounded; specification-only; placement-hold; runtime-needs-verification; non-release; non-publication
owners:
  - "@bartytime4life — CONFIRMED CODEOWNERS review route only"
owner_status: "Agriculture, source, privacy/sensitivity, observability, review, release, and independent-review stewardship remain NEEDS VERIFICATION"
created: 2026-05-26
updated: 2026-08-21
policy_label: public; documentation; agriculture; dashboard-spec; cite-or-abstain; fail-closed
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
  CONFIRMED existing path under the canonical docs/ responsibility root; HOLD as
  part of the unadmitted docs/dashboards/ direct-child lane recorded by the
  repository-grounded parent README.
runtime_status: >-
  NEEDS VERIFICATION — repository READMEs and workflow definitions exist, but
  no running Agriculture dashboard, dashboard route, metric query, telemetry
  feed, access-control binding, or deployed panel was verified in this change.
truth_labels: >-
  CONFIRMED current target bytes, parent dashboard boundaries, repository
  review route, Agriculture contract/schema/source/policy/test/workflow
  surfaces, and the implementation holds stated below / PROPOSED indicator
  definitions, metric queries, panel composition, owner assignments, review
  cadence, and future runtime bindings / UNKNOWN deployed dashboard state,
  production data, effective policy evaluation, exact public feed, release
  parity, and operational correction propagation / NEEDS VERIFICATION every
  positive health claim until its input records, denominator, time window,
  policy state, evidence closure, and release state are proven.
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 51d45e45a56d19961a3014009b80c2c94b1107ee
  target_prior_blob: b641f57a3fd22fe088727663f8e44a503626ee92
  dashboards_parent_blob: c3a0ab69cfc14cea7269cc2cdd853fbac3bb14e3
  domain_parent_blob: fc18e269e8f674688ea580ac384ba46c40304840
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  adr_0029_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  dashboard_catalog_blob: 30b9d35ede3410a8d2f946279891ae5ec2482a62
  nass_source_record_blob: 7e2d31a23f5a4bc5e5a30b62b5cc814359a05566
  aggregation_thresholds_blob: 31947ca3e468a967aed3fc5d44699130b7d588fd
  farm_operator_join_policy_blob: 1b6128c4e2470f198edb6464424c6effc9d246dd
  nass_aggregate_test_blob: 97939b939122f029f35ecf12c81f5989df00ae63
  field_level_nass_test_blob: 06e3abeabc57b01d8073dc614cace9b404e204db
  agriculture_workflow_blob: d89d5db8861812f7b0a1024ae37a23ed5bd61354
inspection_boundary: >-
  Current-session GitHub reads covered this complete prior specification, the
  dashboard parent and domain README, dashboard catalog, CODEOWNERS, accepted
  Directory Rules decision, Agriculture domain/sensitivity documentation,
  NASS source documentation and placeholder record, connector coordination,
  semantic-contract and schema compatibility/domain lanes, policy scaffolds,
  placeholder NASS tests, Agriculture workflow definition, Review Console,
  Explorer Agriculture feature, Governed API Agriculture route documentation,
  and one inbound report-lane reference. No live source request, production
  database, telemetry store, metric query, policy evaluator, browser session,
  deployed dashboard, released carrier, correction cascade, or rollback drill
  was exercised.
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
  - "The prior hard-coded NASS n<3/complementary-suppression claim is removed; this specification requires preservation of source-native withheld/suppressed states and an accepted KFM policy decision before any threshold is treated as enforceable."
  - "The prior >99.9% and fixed review-cadence claims are removed because no accepted SLO, metric producer, denominator, or runtime feed was verified."
  - "Legacy section anchors are retained for inbound-link compatibility."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Agriculture Dashboard Specification

> **One-line purpose.** Define the reviewable Agriculture domain-health dashboard contract without mistaking a specification, metric, map, workflow, or generated summary for Agriculture truth, policy enforcement, release state, or publication authority.

<p>
  <img alt="Path: confirmed" src="https://img.shields.io/badge/path-CONFIRMED-1f6feb">
  <img alt="Placement: hold" src="https://img.shields.io/badge/placement-HOLD-b42318">
  <img alt="Artifact: specification only" src="https://img.shields.io/badge/artifact-specification%20only-6e7781">
  <img alt="Runtime: needs verification" src="https://img.shields.io/badge/runtime-NEEDS%20VERIFICATION-d4a72c">
  <img alt="Policy: scaffold only" src="https://img.shields.io/badge/policy-scaffold%20only-d4a72c">
  <img alt="Publication: none" src="https://img.shields.io/badge/publication-none-6e7781">
</p>

> [!IMPORTANT]
> **A dashboard is a downstream carrier.** A panel may summarize verified `SourceDescriptor`, `EvidenceBundle`, validation, policy, review, release, correction, rollback, and telemetry records. It does not create those records, repair a missing evidence chain, turn a placeholder into enforcement, or authorize publication.

> [!CAUTION]
> **Agriculture metrics can become privacy side channels.** Field/operator/parcel combinations, private well or irrigation joins, proprietary yield, pesticide/application detail, small-cell existence signals, and reconstructive filters must fail closed. Client-side hiding, a “private” panel, or a chart-level aggregation label is not an upstream policy control.

> [!WARNING]
> **Do not hard-code an external disclosure threshold into this specification.** The prior text named an `n < 3` rule and complementary suppression without current authoritative evidence or an accepted KFM policy binding. A future dashboard must preserve source-native withheld/suppressed states, show the governing policy/version, and return a bounded negative state when disclosure safety is unresolved.

**Quick navigation:** [Status](#status-and-evidence-boundary) · [Scope](#1-domain-scope) · [Repo fit](#repository-fit-and-authority) · [Maturity](#current-repository-maturity) · [Indicators](#2-indicator-subset) · [Agriculture metrics](#3-domain-specific-indicators-proposed) · [Sources](#source-role-time-and-anti-collapse-contract) · [Sensitivity](#sensitivity-rights-and-public-safe-presentation) · [Outcomes](#finite-outcomes-and-negative-states) · [Implementation](#5-implementation-pointer) · [Validation](#validation-and-negative-proof) · [Review](#4-ownership) · [Open work](#7-open-questions) · [Evidence](#8-evidence-basis--citations) · [Rollback](#correction-and-rollback)

---

## Status and evidence boundary

| Surface | Current repository-grounded state | Safe interpretation |
|---|---|---|
| This specification | Existing tracked file; prior blob `b641f57a3fd22fe088727663f8e44a503626ee92` | Same-path documentation modernization only |
| Dashboard lane | Parent path and specification inventory exist | `CONFIRMED` path; placement remains `HOLD`; no runtime inferred |
| Agriculture domain documentation | Substantive domain, lifecycle, source, policy, sensitivity, API, map/UI, and backlog documents exist | Documentation and planning lineage; not machine or release proof |
| Review routing | Repository-wide CODEOWNERS routes review to `@bartytime4life` | GitHub routing only; not stewardship, independent review, policy approval, or release authority |
| NASS QuickStats record | `data/registry/sources/agriculture/nass_quickstats.yaml` is a four-field `PROPOSED` placeholder | Not an admitted `SourceDescriptor`; no live source activation |
| Agriculture policy | Aggregation thresholds are a placeholder; farm/operator join Rego is a `PROPOSED` default-deny scaffold | Useful fail-closed intent; no accepted production policy evaluator established |
| NASS negative tests | Two named tests contain documentation-only module docstrings | Filename presence is not executable proof |
| Agriculture CI | Workflow executes a bounded fixture-only CDL watcher proof and recognizes dedicated NDVI/vegetation validators; broader validation, proof, and release remain held | Current bounded implementation evidence, not Agriculture-wide conformance |
| Dashboard/UI/API runtime | Review Console, Explorer Agriculture, and Governed API Agriculture README boundaries exist | Route, query, panel, metric feed, policy binding, deployment, and user-visible behavior remain `NEEDS VERIFICATION` |
| Release/publication | Workflow and release documentation preserve holds | No Agriculture dashboard release or public feed is established |

### Truth posture

- **CONFIRMED:** the current path and prior bytes; parent dashboard boundaries; review route; inspected Agriculture source, contract, schema, policy, test, workflow, UI/API documentation, and their stated maturity.
- **PROPOSED:** indicator names, metric formulas, denominators, panels, query implementations, data contracts, owner assignments, review cadence, and any future dashboard composition.
- **UNKNOWN:** production records, deployed dashboard state, effective access control, actual telemetry, policy decisions, public parity, correction propagation, and operational rollback.
- **NEEDS VERIFICATION:** every positive health status and every public-use claim.
- **HOLD:** structural dashboard-lane admission, source activation, operator/parcel exposure, unreviewed metric publication, release, deployment, and publication.

[Back to top](#top)

---

<a id="1-domain-scope"></a>

## 1. Domain scope

This specification covers the **governance and delivery health** of Agriculture-domain claims and carriers, including:

- aggregate crop, production, progress, rotation, and agricultural-economy context;
- crop-classification and remote-sensing/model products such as CDL- and NDVI-related derivatives;
- soil-crop suitability, irrigation, drought/stress, conservation, and supply-chain context when the owning domain and source role remain explicit;
- evidence resolution, source admission, temporal/version pins, validation, policy, review, release, correction, withdrawal, and rollback posture;
- public-safe map/API/UI delivery only after upstream controls close.

It does **not** own:

| Excluded responsibility | Owning surface |
|---|---|
| Agriculture domain meaning | [`docs/domains/agriculture/`](../../domains/agriculture/README.md) and accepted semantic contracts |
| Source identity, rights, activation, and cadence | Governed source registry and admission records |
| Machine payload shape | Accepted Agriculture schema lane |
| Sensitivity, aggregation, disclosure, and join decisions | Accepted policy plus review records |
| Metric production, queries, panels, routes, and storage | Governed implementation/operations roots |
| Evidence, receipts, proofs, catalogs, and lifecycle data | Their distinct `data/` object families |
| Promotion, release, correction, withdrawal, and rollback decisions | `release/` and accountable decision records |
| Public Agriculture truth | Released, evidence-backed claims served through governed interfaces |

A dashboard may **report** that an upstream gate passed, failed, abstained, denied, errored, or is held. It must not become the gate itself unless a separate accepted contract, schema, policy, validator, implementation, and review packet explicitly establishes that authority.

[Back to top](#top)

---

## Repository fit and authority

The current file remains under the existing `docs/` responsibility root. Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the exact [Directory Rules v2](../../doctrine/directory-rules.md) bytes; those rules make `docs/` the human explanation surface and require responsibility boundaries to remain visible.

| Repository surface | Relationship to this specification | Current posture |
|---|---|---|
| [`docs/dashboards/README.md`](../README.md) | Parent dashboard-lane boundary | Repository-grounded; nested-lane placement `HOLD` |
| [`docs/dashboards/domain/README.md`](./README.md) | Per-domain specification index and legacy authoring template | Present but older proposal-era wording remains; separate reconciliation needed |
| [`DASHBOARD_CATALOG.md`](../DASHBOARD_CATALOG.md) | Human index of dashboard specifications | Path/row presence confirmed; catalog maturity and runtime parity require verification |
| [`INDICATOR_CATALOG.md`](../INDICATOR_CATALOG.md) | Human indicator mirror | Documentation only; not machine metric authority |
| [`docs/domains/agriculture/`](../../domains/agriculture/README.md) | Agriculture bounded-context documentation | Richer domain context; does not replace contracts, schemas, policy, or evidence |
| [`contracts/agriculture/`](../../../contracts/agriculture/README.md) | Older compatibility semantic lane | Transitional; do not expand into parallel authority |
| [`contracts/domains/agriculture/`](../../../contracts/domains/agriculture/README.md) | Doctrine-aligned Agriculture semantic lane | Present, mixed maturity, incomplete family coverage |
| [`schemas/contracts/v1/agriculture/`](../../../schemas/contracts/v1/agriculture/README.md) | Flat compatibility/index schema lane | Index-only; no machine schemas belong there |
| [`schemas/contracts/v1/domains/agriculture/`](../../../schemas/contracts/v1/domains/agriculture/README.md) | Proposed Agriculture machine-shape lane | Mixed permissive scaffolds and bounded dedicated shapes; not full conformance |
| [`policy/sensitivity/agriculture/`](../../../policy/sensitivity/agriculture/) | Agriculture sensitivity policy surface | Two inspected scaffolds; accepted evaluator and complete rule set unverified |
| [`apps/review-console/`](../../../apps/review-console/README.md) | Candidate role-gated review surface | README boundary confirmed; dashboard implementation unknown |
| [`apps/explorer-web/.../agriculture/`](../../../apps/explorer-web/src/features/domains/agriculture/README.md) | Candidate public-safe Agriculture feature boundary | README confirmed; route/panel/runtime unknown |
| [`apps/governed-api/.../agriculture/`](../../../apps/governed-api/src/routes/agriculture/README.md) | Candidate Agriculture trust-membrane route source | README confirmed; handlers and runtime unknown |

This update creates no path, move, rename, deletion, machine registry, new authority root, or structural migration.

[Back to top](#top)

---

## Current repository maturity

| Capability | Evidence at `main@51d45e45a56d` | Dashboard consequence |
|---|---|---|
| Agriculture source documentation | QuickStats is documented as `aggregate`; field/operator inference is denied in doctrine | The dashboard must preserve aggregation unit and source role |
| Live NASS source admission | Placeholder record only | Show `NEEDS VERIFICATION` or `ABSTAIN`; do not report source “healthy” |
| NASS connector | Coordination README records three conflicting connector paths and no executable connector proof | Do not infer live collection or freshness |
| Agriculture semantic meaning | Compatibility and domain lanes coexist | Report path/contract drift separately from domain health |
| Agriculture machine shape | Compatibility index plus domain schema lane; mixed scaffold/dedicated maturity | Metrics cannot assume a complete payload contract |
| Aggregation thresholds | Placeholder YAML only | No numeric disclosure threshold is enforceable from repository evidence |
| Farm/operator join policy | Default-deny Rego scaffold | Preserve denial intent; do not claim runtime enforcement |
| NASS aggregate-only tests | Documentation-only placeholders | “Test present” must not be counted as “control passed” |
| Bounded executable slices | Synthetic CDL material-change watcher and dedicated NDVI/vegetation validator suites are named and executed by workflow definitions | Report only their declared fixture scope and exact head |
| Broad validation/proof/release | Explicit workflow holds | Dashboard status remains bounded; no promotion or release inference |
| Public dashboard feed | Not verified | No public route, endpoint, or static data path may be invented |

> [!NOTE]
> Repository maturity is uneven. A substantive fixture-only validator can be **CONFIRMED** for its narrow behavior while the broader source, evidence, policy, proof, and release chain remains **HOLD**. The dashboard must preserve both facts instead of flattening them into one green or red badge.

[Back to top](#top)

---

<a id="2-indicator-subset"></a>

## 2. Indicator subset

### Metric-record contract

A future emitted metric is not reviewable unless it identifies, at minimum:

| Required field | Purpose |
|---|---|
| `metric_id` and `metric_version` | Stable identity and semantic version |
| `scope` | Domain, geography, product/source family, and lifecycle/release scope |
| `window_start` / `window_end` | Explicit UTC measurement window |
| `observed_at` | When the metric was computed |
| `numerator` / `denominator` | Reconstructable rate; no hidden exclusions |
| `outcome_counts` | Upstream `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` counts where applicable |
| `reason_code_counts` | Explain negative outcomes without leaking protected detail |
| `source_refs` | Resolving source identities and source-state versions |
| `evidence_refs` | Resolving support for consequential claims |
| `policy_refs` | Policy and policy-version references used for admissibility or disclosure |
| `release_refs` | Release/correction/rollback context when public state is summarized |
| `query_or_producer_ref` | Deterministic producer identity, version, and digest |
| `freshness_state` | Current/stale/unknown using the owning source contract, not a guessed cadence |
| `limitations` | Known blind spots, withheld dimensions, and non-effects |

A missing denominator, unknown time window, unresolved evidence reference, unavailable policy version, or failed producer must not be converted to zero or silently excluded.

### Core dashboard indicators

| Indicator | What it measures | Positive posture | Mandatory negative behavior |
|---|---|---|---|
| `evidence_resolution_closure` | Consequential Agriculture claims whose `EvidenceRef` resolves to an admissible `EvidenceBundle` | Complete closure for every positive public/release claim | Missing or conflicting evidence → `ABSTAIN`; resolver failure → `ERROR` |
| `source_admission_closure` | Feed records whose source ref resolves to an admitted, non-placeholder source record | Every operational feed source is admitted and version-pinned | Placeholder, missing, revoked, or unreviewed source → `ABSTAIN` or `HOLD` |
| `source_role_preservation` | Records that preserve `aggregate`, `modeled`, `observed`, `regulatory`, or other accepted source role | No role collapse in metric queries or panels | Aggregate/model treated as field observation → `DENY` or `ABSTAIN` |
| `temporal_version_pin_coverage` | Crop year, product/vintage, retrieval time, release time, class map/model version, and correction time | Required temporal dimensions present for each applicable record | Missing or incompatible temporal support → `ABSTAIN` or `HOLD` |
| `withheld_state_preservation` | Applicable source values whose withheld/suppressed/not-available state survives ingest, transform, aggregate, API, export, and display | Source-native state and reason remain visible at every authorized projection | Lost marker or reconstructed value → `DENY` / `ERROR`; never infer a hidden value |
| `sensitive_join_denial_coverage` | Public requests involving operator, parcel, private field, proprietary yield, pesticide/application, or reconstructive irrigation joins | Every disallowed join returns a bounded denial without existence leakage | Any unauthorized positive result → critical failure and correction review |
| `aggregation_receipt_coverage` | Released aggregate claims with a resolving aggregation/transform receipt and declared unit/method | Complete coverage for every released aggregate claim | Missing receipt or unit mismatch → `ABSTAIN` / `HOLD` |
| `modeled_product_disclosure` | Classified, inferred, or modeled outputs that carry product/model version, uncertainty/quality, and non-observation labeling | Every modeled value remains visibly modeled | Model or classification presented as observed field truth → `DENY` / `ABSTAIN` |
| `cross_lane_reference_integrity` | Agriculture references to Soil, Hydrology, Atmosphere, People/Land, Habitat, Flora/Fauna, Hazards, and Infrastructure that resolve without semantic takeover | Owning-domain reference, time, scale, and evidence remain explicit | Unowned join or incompatible scale/time → `ABSTAIN` / `DENY` |
| `correction_invalidation_closure` | Corrections/withdrawals propagated to released APIs, maps, exports, indexes, caches, dashboards, and AI summaries | Every affected derivative reaches corrected, withdrawn, or blocked state | Stale derivative remains visible → `ERROR` / `HOLD` |
| `validation_topology_drift` | Difference between registered/expected Agriculture tests, validators, workflows, fixtures, and actual substantive implementations | Drift is explicit and bounded; no placeholder counted as enforcement | Unwired substantive file or scaffold presented as pass → `HOLD` |
| `documentation_authority_drift` | Conflicting compatibility/domain paths, stale inventories, unresolved owners, and proposal/current-state mismatches | One visible authority relationship with migration state | Parallel writable authority or hidden drift → `HOLD` and governance review |

### Threshold posture

This specification does not ratify arbitrary service levels. Safety-critical closure indicators above use an all-or-fail posture for **positive public claims** because one unsupported or unlawfully exposed claim is material. Operational warning bands, error budgets, trend windows, and review thresholds remain **PROPOSED** until an accepted metric contract and accountable owner establish them.

[Back to top](#top)

---

<a id="3-domain-specific-indicators-proposed"></a>

## 3. Domain-specific indicators — PROPOSED

| Candidate metric | Agriculture-specific question | Evidence required before implementation |
|---|---|---|
| `aggregate_scope_match_rate` | Does the displayed geography/time exactly match the source aggregation unit and reporting period? | Admitted source descriptor, aggregation receipt, geometry/time validator |
| `cdl_classmap_version_skew` | Are cross-year CDL comparisons mixing incompatible class maps or legends? | Product-year/class-map identity, transform receipt, comparison-policy decision |
| `classification_confidence_disclosure` | Are classification confidence, uncertainty, quality, or applicability limits visible where a modeled product supports a claim? | Accepted model/output contract, validation report, source/model version |
| `nass_field_inference_denial_rate` | Do field/operator requests over aggregate NASS material fail closed? | Executable negative fixtures, policy binding, governed API tests |
| `irrigation_join_review_state` | Are irrigation or well/field relations bounded by Hydrology ownership, rights, precision, and operator privacy? | Cross-lane contract, policy decision, public-safe transform, review record |
| `stress_indicator_time_alignment` | Are crop/stress summaries aligned to compatible observation/model periods and crop stages? | Atmosphere/Hydrology evidence refs, temporal contract, uncertainty record |
| `small_cell_side_channel_review` | Could counts, filters, drill-downs, error differences, or timing reveal a protected operator/field or suppressed value? | Adversarial disclosure tests, policy review, access-role matrix |
| `source_correction_latency` | How quickly do source re-releases or corrections reach KFM candidates and released derivatives? | Immutable source versions, correction notice, dependency graph, release/invalidation receipts |
| `public_export_parity` | Do exports preserve the same aggregation, redaction, evidence, release, and correction state as the dashboard? | Export contract, fixture parity tests, release manifest, correction tests |

These are candidate metric families, not evidence that emitters, queries, stores, panels, or accepted thresholds exist.

[Back to top](#top)

---

## Source role, time, and anti-collapse contract

| Source/product family | Permitted dashboard interpretation | Prohibited interpretation |
|---|---|---|
| NASS QuickStats / Census-style aggregates | Aggregate statistics at the admitted unit and period, with withheld states and aggregation support preserved | Field/operator truth, observation, parcel value, disaggregated estimate, or regulatory determination |
| CDL or another classified land-cover product | Versioned classification/model context with class-map identity and uncertainty/limitations | Confirmed operator planting decision, parcel ownership, actual yield, or direct field observation |
| NDVI/HLS or another remote-sensing derivative | Modeled/derived stress or vegetation context within validated time/space applicability | Causal diagnosis, crop failure determination, pesticide need, or unqualified field truth |
| Irrigation/water-use context | Governed reference to Hydrology-owned observations or administrative context | Operator identity, private well-to-field exposure, water-right determination, or inferred intent |
| Soil/suitability context | Governed reference to Soil-owned survey/model evidence at its valid scale | Field-specific productivity guarantee or agronomic prescription |
| Atmosphere/hazard context | Governed observations/models with issue/valid/retrieval time and source role | Official warning authority, emergency direction, or causation claim |
| Agriculture economy/supply chain | Released public aggregate/contextual records with source and time | Private operator chain, confidential business detail, or individual financial conclusion |

### Required temporal dimensions

The dashboard must keep distinct where material:

- source reporting period and crop year;
- observed/measurement time;
- model or product valid time;
- retrieval/ingestion time;
- processing time;
- release time;
- correction, supersession, or withdrawal time;
- dashboard metric-computation time.

A recent dashboard computation does not make an old source current. A new source release does not silently rewrite the time basis of an earlier public claim.

[Back to top](#top)

---

## Sensitivity, rights, and public-safe presentation

The Agriculture [sensitivity document](../../domains/agriculture/SENSITIVITY.md) uses a working T0–T4 scheme, but that document explicitly treats adoption and executable policy as unresolved. This dashboard therefore reports the referenced tier/policy state without pretending the tier scheme or scaffolds are accepted enforcement.

| Material class | Default dashboard posture | Required evidence before a less restrictive posture |
|---|---|---|
| Released state/county/district aggregate | Public-safe candidate when evidence, source role, withheld-state, release, and correction closure pass | Admitted source, aggregation support, policy/review state, release reference |
| Generalized modeled/classified context | Context only; uncertainty and model/source role visible | Accepted model/output contract, validation, generalization/aggregation receipt |
| Field-candidate footprint | Reviewer-only by default; not public field truth | Named review role, policy decision, safe geometry, evidence, audit trail |
| Operator-linked, parcel-resolving, proprietary yield, pesticide/application, or private farm record | `DENY` from ordinary dashboard/public client | No public lift inferred; any restricted access requires a separately governed agreement and review record |
| Private well/irrigation + field/operator join | `DENY` from public output | Hydrology/People-Land ownership, rights, public-safe transform, policy, review |
| Small-cell, existence-sensitive, or reconstructive metric | Suppress the dimension or `ABSTAIN`/`DENY`; do not reveal by filters, counts, errors, timing, or export | Approved disclosure analysis, policy version, negative proof |
| Unknown rights, source terms, sensitivity, or review state | `HOLD`, `ABSTAIN`, or `DENY` as the governing interface specifies | Current rights/source review and explicit policy decision |

A dashboard may show an aggregate count of denials only when that aggregate cannot reveal the protected case, existence, location, or reason. Internal reason codes must be projected through a public-safe vocabulary.

[Back to top](#top)

---

## Finite outcomes and negative states

A running dashboard must preserve upstream finite outcomes rather than coerce them into a value:

| Upstream outcome | Dashboard behavior |
|---|---|
| `ANSWER` | Display only when evidence, policy, review, release, time, and scope support the claim; keep citations and limitations reachable |
| `ABSTAIN` | Show that no citable bounded answer is available; do not substitute zero, “no issue,” a prior value, or generated prose |
| `DENY` | Withhold protected detail and use a public-safe reason; do not disclose existence through counts, filters, map state, or different errors |
| `ERROR` | Surface operational failure without unsupported fallback data or internal-sensitive detail |
| Repository/workflow `HOLD` | Present as implementation/readiness state only; never translate it into domain truth or release status |
| `UNKNOWN` / `NEEDS VERIFICATION` documentation state | Keep the uncertainty visible; do not render a green health posture |

The panel itself must have explicit loading, unavailable, stale, denied, restricted, malformed, and producer-error states.

[Back to top](#top)

---

<a id="5-implementation-pointer"></a>

## 5. Implementation pointer

### Verified boundary surfaces

- [Review Console README](../../../apps/review-console/README.md) — candidate role-gated steward surface; runtime remains unverified.
- [Explorer Web Agriculture README](../../../apps/explorer-web/src/features/domains/agriculture/README.md) — candidate public-safe Agriculture feature boundary; implementation remains unverified.
- [Governed API Agriculture route README](../../../apps/governed-api/src/routes/agriculture/README.md) — candidate trust-membrane route boundary; implementation remains unverified.
- [Agriculture CI workflow](../../../.github/workflows/domain-agriculture.yml) — current readiness and fixture-only execution definition; not a dashboard feed.
- [NASS connector coordination README](../../../connectors/nass/README.md) — source-intake placement conflict and placeholder maturity; not live access.

### Runtime requirements

A future implementation must:

1. consume governed API envelopes or verified released public-safe artifacts, never direct RAW/WORK/QUARANTINE/canonical stores;
2. validate the response and metric-record contract before rendering;
3. preserve source role, aggregation unit, time basis, evidence refs, policy/review state, release ID, and correction state;
4. prevent protected dimensions from reaching the ordinary client, logs, analytics, caches, exports, screenshots, or AI context;
5. expose finite negative states and accessible non-color cues;
6. keep query/producers deterministic and versioned where practical;
7. bind each dashboard build/feed to a reviewable manifest or equivalent implementation record;
8. make correction, withdrawal, cache invalidation, and rollback behavior testable;
9. avoid inventing a route or dashboard home until current implementation and ownership evidence supports it.

### Explicit non-implementation claims

This document does not establish:

- an Agriculture dashboard URL, route, panel, database view, query, telemetry series, alert, or SLO;
- a current source endpoint, credential, activation, or successful fetch;
- an accepted Agriculture source descriptor, complete schema, complete policy bundle, or broad validator suite;
- a public dataset, released layer, report, dashboard feed, or Focus Mode capability;
- a steward assignment, review approval, release decision, deployment, or publication.

[Back to top](#top)

---

## Validation and negative proof

### Documentation validation for this revision

| Check | Required result |
|---|---|
| Meta block | One parseable `KFM_META_BLOCK_V2`; stable `doc_id`; current evidence snapshot |
| Structure | One H1; logical heading order; balanced fences; final newline; no trailing whitespace |
| Compatibility | Preserve `top` and legacy section anchors `1-domain-scope` through `8-evidence-basis--citations` |
| Links | Every repository-relative destination resolves at the exact branch head |
| Claim boundary | Current behavior is tied to repository evidence; proposals and unknowns remain labeled |
| Sensitive content | No live key, private endpoint, exact protected location, operator identity, parcel data, or hidden threshold is introduced |
| Diff scope | Target specification plus its generated authoring receipt only |
| Receipt | Final target SHA-256 resolves from a schema-valid pending-review `GENERATED_RECEIPT` |

### Future implementation fixture matrix

| Case | Expected outcome | What it proves |
|---|---|---|
| Released county aggregate with admitted source, evidence, policy, aggregation support, and correction state | `ANSWER` | Narrow positive path only |
| QuickStats placeholder source record | `ABSTAIN` / `HOLD` | Placeholder is not admission |
| Source-native withheld value | `ABSTAIN` or public-safe withheld state | No hidden-value reconstruction |
| Missing/conflicting EvidenceBundle | `ABSTAIN` | Cite-or-abstain |
| Policy evaluator unavailable | `ERROR` | No unsafe allow fallback |
| Field/operator request over aggregate NASS data | `DENY` | Source-role and privacy boundary |
| Parcel + operator + irrigation/well join | `DENY` | Cross-lane harmful-precision boundary |
| CDL/NDVI value presented as confirmed observation | `DENY` or `ABSTAIN` | Model/classification anti-collapse |
| Missing crop year/product/class-map version | `ABSTAIN` / `HOLD` | Temporal/version closure |
| Correction supersedes an input | Prior dashboard/export/cache entry invalidated | Correction propagation |
| Filter or count reveals a protected case exists | `DENY`; no differentiated side channel | Adversarial disclosure safety |
| Metric producer fails or returns malformed denominator | `ERROR` | No zero/default coercion |

Passing Markdown, workflow, fixture, or unit checks proves only their declared scope. It does not admit a source, validate Agriculture semantics, activate policy, approve review, release data, deploy a dashboard, or publish KFM knowledge.

[Back to top](#top)

---

<a id="4-ownership"></a>

## 4. Ownership and review

| Role | Current state | Required decision |
|---|---|---|
| GitHub review route | `@bartytime4life` through CODEOWNERS | Confirmed routing only |
| Agriculture domain steward | `NEEDS VERIFICATION` | Own domain interpretation and metric fitness |
| Source/rights steward | `NEEDS VERIFICATION` | Own source admission, terms, and currentness |
| Privacy/sensitivity reviewer | `NEEDS VERIFICATION` | Review operator/parcel/small-cell/reconstruction risk |
| Metric/observability owner | `NEEDS VERIFICATION` | Own metric contract, producer, denominator, windows, SLOs |
| Evidence/policy reviewer | `NEEDS VERIFICATION` | Verify EvidenceBundle and policy binding |
| UI/accessibility reviewer | `NEEDS VERIFICATION` | Verify negative states, non-color cues, keyboard/screen-reader behavior |
| Release/correction reviewer | `NEEDS VERIFICATION` | Verify release, invalidation, withdrawal, and rollback closure |
| Independent reviewer | `NEEDS VERIFICATION` | Required when policy-significant or privacy-sensitive behavior changes |

The document author, metric producer, dashboard implementer, and release approver must not be silently treated as one authority.

[Back to top](#top)

---

<a id="6-review-cadence"></a>

## 6. Review cadence and maintenance triggers

No fixed annual or semi-annual cadence is claimed as accepted. The accountable owner should establish one after metric producers, source cadences, policy versions, and release obligations are known.

Recheck this specification when:

- the parent dashboard lane, catalog, indicator catalog, Directory Rules, or an accepted ADR changes;
- an Agriculture source descriptor is admitted, revoked, corrected, or materially changes role, terms, cadence, schema, aggregation unit, or withheld-state behavior;
- a NASS/CDL/remote-sensing connector, watcher, pipeline, validator, or fixture graduates from placeholder or bounded fixture scope;
- an Agriculture contract/schema/policy path is accepted, migrated, deprecated, or changes compatibility status;
- a metric producer, query, dashboard panel, route, access policy, export, Evidence Drawer, or Focus Mode behavior becomes reviewable;
- source correction, release correction, withdrawal, cache invalidation, or rollback behavior changes;
- a privacy, rights, operator-identification, small-cell, reconstruction, or harmful-precision concern is reported;
- a hosted check or runtime observation reveals topology or parity drift.

[Back to top](#top)

---

<a id="7-open-questions"></a>

## 7. Open questions

| ID | Question | State | Closure evidence |
|---|---|---|---|
| `DASH-AG-01` | Which accepted machine contract owns Agriculture dashboard metric records? | `NEEDS VERIFICATION` | Contract, schema, fixtures, validator, registry, consumer, and migration decision |
| `DASH-AG-02` | Which dashboard application and route own the steward-facing Agriculture view? | `NEEDS VERIFICATION` | Current implementation files, ownership, tests, access policy, deployment evidence |
| `DASH-AG-03` | Which source/policy version governs withheld or disclosure-sensitive Agriculture cells? | `HOLD` | Admitted source descriptors, authoritative terms, accepted policy, negative proof |
| `DASH-AG-04` | How are aggregation receipts identified and resolved for every public aggregate claim? | `NEEDS VERIFICATION` | Accepted contract/schema, producer, resolver, fixtures, release binding |
| `DASH-AG-05` | Which CDL/classification/NDVI quality and uncertainty measures are fit for public interpretation? | `NEEDS VERIFICATION` | Domain review, model/product contracts, validation, limitations, release decision |
| `DASH-AG-06` | What is the accepted Agriculture ↔ Hydrology irrigation/well join boundary? | `HOLD` | Cross-lane contract, rights/sensitivity policy, transform receipt, adversarial tests |
| `DASH-AG-07` | What error budgets, warning bands, and review cadence are accepted for operational metrics? | `PROPOSED` | Named owner, measured baseline, SLO decision, alert/non-alert boundary |
| `DASH-AG-08` | How are corrections and withdrawals propagated to panels, exports, caches, search, AI, and map carriers? | `NEEDS VERIFICATION` | Dependency graph, correction receipts, exact tests, rollback drill |
| `DASH-AG-09` | How should the stale parent domain README and dashboard catalog be reconciled without widening this file's scope? | `NEEDS VERIFICATION` | Separate bounded documentation task and current inventory proof |
| `DASH-AG-10` | Which Agriculture contract/schema compatibility paths survive, and how are consumers migrated? | `HOLD` for structural change | Accepted ADR/migration note, consumer inventory, rollback target |
| `DASH-AG-11` | Which hosted checks and branch controls are required for this specification and its future implementation? | `UNKNOWN` | Current repository ruleset/branch-protection evidence |

[Back to top](#top)

---

<a id="8-evidence-basis--citations"></a>

## 8. Evidence basis and repository references

### Current repository references

- [Dashboard lane boundary](../README.md)
- [Per-domain dashboard index](./README.md)
- [Dashboard catalog](../DASHBOARD_CATALOG.md)
- [Indicator catalog](../INDICATOR_CATALOG.md)
- [Agriculture domain documentation](../../domains/agriculture/README.md)
- [Agriculture sensitivity posture](../../domains/agriculture/SENSITIVITY.md)
- [Agriculture verification backlog](../../domains/agriculture/VERIFICATION_BACKLOG.md)
- [USDA NASS QuickStats source product page](../../sources/catalog/usda/usda-nass-quickstats.md)
- [NASS connector coordination boundary](../../../connectors/nass/README.md)
- [NASS QuickStats placeholder source record](../../../data/registry/sources/agriculture/nass_quickstats.yaml)
- [Agriculture contract compatibility lane](../../../contracts/agriculture/README.md)
- [Agriculture domain contract lane](../../../contracts/domains/agriculture/README.md)
- [Agriculture schema compatibility lane](../../../schemas/contracts/v1/agriculture/README.md)
- [Agriculture domain schema lane](../../../schemas/contracts/v1/domains/agriculture/README.md)
- [Aggregation-threshold policy placeholder](../../../policy/sensitivity/agriculture/aggregation_thresholds.yaml)
- [Farm/operator join default-deny policy scaffold](../../../policy/sensitivity/agriculture/farm_operator_join.rego)
- [NASS aggregate-only test placeholder](../../../tests/domains/agriculture/test_nass_aggregate_only.py)
- [Field-level NASS denial test placeholder](../../../tests/domains/agriculture/test_policy_denial_field_level_nass.py)
- [Agriculture CI readiness workflow](../../../.github/workflows/domain-agriculture.yml)
- [Repository review routing](../../../.github/CODEOWNERS)
- [Review Console boundary](../../../apps/review-console/README.md)
- [Explorer Web Agriculture boundary](../../../apps/explorer-web/src/features/domains/agriculture/README.md)
- [Governed API Agriculture route boundary](../../../apps/governed-api/src/routes/agriculture/README.md)
- [Accepted Directory Rules decision](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [Directory Rules v2](../../doctrine/directory-rules.md)
- [Repository drift register](../../registers/DRIFT_REGISTER.md)
- [Repository verification backlog](../../registers/VERIFICATION_BACKLOG.md)

### Evidence limits

| Evidence class | What it supports | What it cannot prove |
|---|---|---|
| Current file/tree bytes | Path presence, exact content, declared status, and bounded inventory | Runtime behavior, correctness, enforcement, release, or publication |
| Workflow definition | Triggers, declared commands, permissions, and documented holds | Hosted result for a different head, production behavior, or domain truth |
| Placeholder source/policy/test files | Explicit incompleteness and current fail-closed intent | Admission, complete policy, executable assertion, or successful runtime |
| Documentation corpus | Domain language, proposed object families, risks, and review questions | Accepted implementation or source currentness |
| Future metric output | Measured posture only when producer and inputs are verified | Evidence, policy, review, release, or truth by itself |

No external source page was checked in this documentation update. Version-sensitive endpoint, disclosure, cadence, license, and product facts remain subject to a separate authoritative-source review before operational use.

[Back to top](#top)

---

## Correction and rollback

### Documentation correction

Before merge, close or abandon the draft pull request; `main` remains unchanged. After an authorized merge, revert the Agriculture dashboard specification and its generated authoring receipt together, or apply a bounded forward correction against the actual merged bytes. Do not rewrite shared history.

### Future runtime correction

A running dashboard must support:

1. freeze or deny the affected metric/panel when evidence, policy, source, or release state becomes invalid;
2. preserve the prior metric/query/build identity and correction reason;
3. invalidate unsafe caches, exports, search/index projections, screenshots where governable, and AI summaries;
4. link the corrected dashboard state to the governing source correction, `CorrectionNotice`, withdrawal, release, or rollback record;
5. verify public/steward parity after the correction;
6. retain an auditable rollback target and negative proof that protected detail is no longer exposed.

This documentation change creates no runtime, data, cache, release, deployment, or public state requiring operational rollback.

### Revision history

| Version | Date | Change | Non-effect |
|---|---|---|---|
| v0.1 | 2026-05-26 | Initial Atlas-derived proposal-only per-domain dashboard specification | No implementation or publication |
| v1.0 | 2026-08-21 | Reconciled the specification against current main; replaced unsupported thresholds/cadence; added evidence, maturity, metric, source-role, time, privacy, finite-outcome, validation, correction, and rollback boundaries | No source admission, policy activation, runtime change, release, deployment, or publication |

[Back to top](#top)

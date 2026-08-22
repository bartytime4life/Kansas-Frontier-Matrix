<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-domain-soil
title: Soil Dashboard Specification — Repository-Grounded Governance and Readiness Boundary
type: standard
version: v0.2.0
status: draft
owners:
  - "@bartytime4life"
owner_status: "@bartytime4life is the verified CODEOWNERS review route; Soil, source, evidence, policy, sensitivity, metric, UI, release, correction, rollback, and independent-review stewardship remain NEEDS VERIFICATION"
created: 2026-05-26
updated: 2026-08-22
policy_label: public
owning_root: docs/
responsibility: >-
  Define a human-readable Soil dashboard measurement, presentation, review,
  correction, and graduation boundary grounded in current repository evidence
  without becoming Soil truth, source admission, contract, schema, policy,
  telemetry, runtime, release, or publication authority.
truth_posture: >-
  CONFIRMED current repository paths and bounded fixture-first validation
  surfaces / PROPOSED dashboard indicators, payloads, panels, thresholds,
  metric producers, runtime wiring, and review procedures / UNKNOWN deployed
  dashboard behavior, production telemetry, live-source state, policy
  evaluation, release state, and public parity / NEEDS VERIFICATION every
  claim beyond the pinned evidence and declared test boundary.
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 6aaea704230259e4fca30fcc0b9c1a168e12c2c2
  target_prior_blob: 13da91fde4e62b080bb742c45e6a00adcfd021f0
  inspected_at: 2026-08-22
related:
  - ./README.md
  - ../DASHBOARD_CATALOG.md
  - ../../domains/soil/README.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../contracts/domains/soil/README.md
  - ../../../schemas/contracts/v1/domains/soil/README.md
  - ../../../fixtures/domains/soil/README.md
  - ../../../tests/domains/soil/README.md
  - ../../../tools/validators/domains/soil/README.md
  - ../../../policy/domains/soil/README.md
  - ../../../data/registry/sources/soil/README.md
  - ../../../data/proofs/soil/README.md
  - ../../../release/candidates/soil/README.md
  - ../../../apps/explorer-web/src/features/domains/soil/README.md
  - ../../../.github/workflows/domain-soil.yml
tags:
  - kfm
  - dashboards
  - domain
  - soil
  - repository-grounded
  - support-type
  - source-role
  - ssurgo
  - sda
  - mukey
  - cokey
  - chkey
  - component-horizon
  - soil-moisture
  - evidence
  - correction
  - rollback
notes:
  - "v0.2.0 replaces an Atlas-first generic dashboard proposal with a current-repository evidence and readiness boundary."
  - "The attached KFM Soil Architecture Extended Pro report is retained as planning lineage, not current implementation proof."
  - "Static survey, gridded derivative, station observation, satellite grid, pedon/profile evidence, interpretation, and public-safe derivative support must not collapse."
  - "No fixed health threshold is adopted here; thresholds require a versioned metric profile, eligible population, denominator, time window, evidence, uncertainty, and accountable review."
  - "No dashboard route, production metric producer, telemetry store, live source, EvidenceBundle resolver, policy evaluator, proof producer, release, deployment, or publication is created by this document."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>
<a id="soil-dashboard-specification"></a>

# Soil Dashboard Specification — Repository-Grounded Governance and Readiness Boundary

> Human-readable specification for reviewing Soil evidence, lineage, support
> type, validation, sensitivity, correction, rollback, and implementation
> readiness without turning dashboard presentation into Soil authority.

[![status](https://img.shields.io/badge/status-draft-d97706?style=flat-square)](#status-and-evidence-boundary)
[![evidence](https://img.shields.io/badge/evidence-repository--grounded-0969da?style=flat-square)](#status-and-evidence-boundary)
[![runtime](https://img.shields.io/badge/runtime-NEEDS%20VERIFICATION-6e7781?style=flat-square)](#5-implementation-pointer)
[![support types](https://img.shields.io/badge/support%20types-must%20remain%20separate-b42318?style=flat-square)](#support-type-anti-collapse)
[![publication](https://img.shields.io/badge/publication-none-6e7781?style=flat-square)](#authority-and-non-effects)

> [!IMPORTANT]
> **This page specifies a review surface; it does not implement one.** The
> repository contains substantial Soil documentation, semantic and machine
> profiles, deterministic synthetic fixtures, validators, tests, and workflows.
> No production metric producer, dashboard route, telemetry store, active source
> admission, EvidenceBundle resolution, policy evaluation, proof-bearing release,
> deployment, or published Soil dashboard was verified at the pinned commit.

> [!WARNING]
> **A green fixture workflow is not Soil truth.** It proves only the exact,
> synthetic, no-network assertions named by that workflow. It does not certify
> agronomic suitability, engineering fitness, conservation compliance, flood or
> drought condition, land value, legal status, regulatory status, or current field
> condition.

> [!CAUTION]
> **Missing, stale, restricted, partial, or conflicting data must never become
> zero, normal, complete, or healthy.** The dashboard must preserve finite states,
> source role, support type, time basis, uncertainty, policy posture, release
> state, correction lineage, and rollback support.

**Quick navigation:** [Status](#status-and-evidence-boundary) ·
[Scope](#1-domain-scope) · [Indicator contract](#2-indicator-subset) ·
[Soil indicators](#3-domain-specific-indicators-proposed) ·
[Ownership](#4-ownership) · [Implementation](#5-implementation-pointer) ·
[Review cadence](#6-review-cadence) · [Open questions](#7-open-questions) ·
[Evidence and validation](#8-evidence-basis--citations) ·
[Rollback](#documentation-correction-and-rollback)

---

## Status and evidence boundary

| Question | Bounded answer | Truth label |
|---|---|---|
| Does this specification exist at the requested path? | Yes; the prior v0.1 file is tracked at blob `13da91fde4e62b080bb742c45e6a00adcfd021f0`. | `CONFIRMED` |
| Is `docs/dashboards/domain/soil.md` a dashboard runtime? | No. It is human-readable documentation under `docs/`. | `CONFIRMED` |
| Does the repository contain Soil contracts, schemas, fixtures, validators, tests, and workflows? | Yes, with uneven maturity and multiple bounded fixture-first profiles. | `CONFIRMED` repository presence |
| Do current Soil workflows use live sources or publish data? | The inspected focused workflows are explicitly no-network or hold publication. | `CONFIRMED` inspected workflow boundary |
| Is a production Soil metric producer or telemetry store verified? | No. | `UNKNOWN` |
| Is a routed Soil dashboard panel verified? | No. The Explorer Soil feature README is a proposed app-local seam, not route or runtime proof. | `NEEDS VERIFICATION` |
| Is active source admission verified for SSURGO, SDA, Mesonet, SCAN, USCRN, SMAP, or SoilGrids? | No source activation was verified in this work. | `UNKNOWN` |
| Is complete EvidenceRef-to-EvidenceBundle, policy, proof, release, correction, and rollback execution verified? | No; documentation and explicit workflow holds remain. | `NEEDS VERIFICATION` / `HOLD` |
| Does this update release, deploy, promote, or publish anything? | No. | `CONFIRMED` |

Repository presence proves bytes and bounded implementation shape. It does not
prove scientific validity, source authority, legal rights, currentness, policy
approval, accountable review, release eligibility, deployment, or public parity.

[Back to top](#top)

---

<a id="1-domain-scope"></a>

## 1. Domain scope

The Soil dashboard is a **governance-health and implementation-readiness
projection** for the Soil lane. Its primary question is not “what is the soil
condition?” but:

> What Soil support is available for this scope, which source and support class
> produced it, how was it validated, what remains unresolved, what is safe to
> expose, and which correction or rollback path applies?

### 1.1 What the dashboard may summarize

The dashboard may summarize repository-grounded or future governed metrics for:

- Soil map-unit, component, horizon, component-horizon, property, hydrologic
  soil-group, pedon/profile, soil-moisture, interpretation, and public-safe
  derivative families;
- `MUKEY`, `COKEY`, and `CHKEY` lineage continuity;
- component and horizon depth ordering, coverage, overlap, gaps, and method
  caveats;
- source admission, source role, support type, rights, sensitivity, source
  vintage, retrieval time, observation time, valid time, release time, and
  correction time;
- deterministic fixture polarity and validator outcomes;
- SSURGO/SDA package or micro-snapshot drift candidates;
- evidence, policy, review, proof, release, correction, withdrawal, and rollback
  closure;
- public-safe map, Evidence Drawer, export, and Focus Mode readiness.

The dashboard must not turn those summaries into agronomic prescriptions,
engineering determinations, conservation-compliance findings, insurance
decisions, land-value estimates, legal conclusions, emergency guidance, or
current field truth.

<a id="support-type-anti-collapse"></a>

### 1.2 Support-type anti-collapse

Current repository profiles use more than one support vocabulary. The table
below is a crosswalk for dashboard presentation only; it is **not** a new global
enum.

| Support family | Current repository examples | Dashboard rule | Prohibited collapse |
|---|---|---|---|
| Static survey | `static_survey`; SSURGO/SDA map-unit, component, and horizon context | Show survey area, source version/vintage, identity lineage, aggregation basis, and interpretation limits. | Static survey is not a live field observation. |
| Gridded derivative | `modeled_derivative`; gSSURGO/gNATSGO or other derived raster context | Show source inputs, cell/resolution, method, uncertainty, and derivation identity. | A derived grid is not an authoritative map-unit record or direct observation. |
| Station observation | `station_observation`; `station_soil_moisture` | Show station identity class, depth, units, timestamp, timezone, QC, freshness, and spatial support. | A station reading is not countywide, fieldwide, or satellite-grid truth. |
| Satellite grid | `satellite_grid`; `satellite_grid_soil_moisture` | Show product/granule or profile identity, grid support, latency, masking, QA, model contribution, and resolution. | A satellite or model grid is not a station reading, field sample, or direct in-situ observation. |
| Pedon/profile evidence | Repository docs name pedon/profile and horizon evidence; a single accepted executable profile was not verified here. | Show profile identity, location sensitivity, depth basis, analytical method, and evidence limits. | A pedon/profile is not automatically representative of an entire map unit. |
| Interpretation | Hydric, suitability, erosion, limitation, or other source interpretations and KFM-derived summaries | Show authoritative source, interpretation method, aggregation, intended use, edition, and disclaimer. | An interpretation is not a regulation, guarantee, engineering design, or operational recommendation. |
| Public-safe derivative | Generalized, aggregated, or otherwise transformed public carrier | Show transform identity, source support, sensitivity decision, release identity, correction state, and rollback target. | A public-safe derivative does not replace the canonical evidence or erase withheld detail. |
| Candidate / fixture | Synthetic fixtures, inactive candidate profiles, comparator reports | Show `SYNTHETIC`, `FIXTURE_ONLY`, `PROPOSED_INACTIVE`, or equivalent status prominently. | Fixture success is not source admission, evidence truth, policy approval, release, or publication. |

Where vocabularies differ, the dashboard must retain the source profile's exact
token and a separately versioned display label. It must not silently coerce one
profile into another.

### 1.3 Source families and activation boundary

Current Soil documentation and workflow boundaries refer to source families such
as NRCS SSURGO/SDA, gSSURGO/gNATSGO, Kansas Mesonet, NRCS SCAN, NOAA
USCRN, NASA SMAP, and ISRIC SoilGrids. Naming a source family does not prove:

- current endpoint, product, version, terms, rights, or redistribution posture;
- source admission or a current `SourceDescriptor`;
- a successful live retrieval;
- scientific fitness for a requested place, depth, time, or decision;
- released public use.

A source-specific dashboard metric is eligible only when its source identity,
role, rights, sensitivity, cadence, time basis, and evidence relationship are
resolvable for the metric snapshot. Otherwise the metric state is `NO_DATA`,
`STALE`, `RESTRICTED`, `REVIEW_PENDING`, `ABSTAIN`, `DENY`, or `ERROR` as
appropriate—not “healthy.”

### 1.4 Cross-domain ownership

| Relation | Soil may contribute | Soil must not claim |
|---|---|---|
| Agriculture × Soil | Survey properties, hydrologic group, moisture context, and explicitly scoped interpretations | Crop condition, yield, management recommendation, compliance, or farm economics |
| Hydrology × Soil | Infiltration/runoff context, hydrologic soil group, moisture support, and public-safe join context | Streamflow, groundwater condition, flood determination, water right, or emergency state |
| Geology × Soil | Parent-material or stratigraphic context when supported by governed relations | Bedrock, mineral-resource, borehole, or geologic-map authority |
| Habitat / Flora / Fauna × Soil | Soil context for habitat or species interpretation | Habitat condition, occurrence truth, range, or protected-location authority |
| Hazards × Soil | Erosion, shrink-swell, ponding, or other bounded source interpretations | Active hazard warning, engineering suitability, insurance determination, or life-safety guidance |
| People / Land × Soil | Generalized public context when policy allows | Ownership, parcel identity, title, land value, or private operational inference |

Cross-domain joins must preserve participant identities, source roles, support
types, time, scale, evidence, the most restrictive applicable policy, and
correction lineage. A join cannot transfer authority from one lane to another.

### 1.5 Sensitivity and public-safety posture

Public soil surveys may be broadly accessible, but a Soil dashboard can still
create exposure through:

- private field observations or farm submissions;
- partner-station metadata or precise sensor locations;
- proprietary agronomic or operational data;
- parcel-scale joins, repeated filtering, small cells, or exported URLs;
- profile/pedon precision associated with private property;
- composition with water, infrastructure, land, archaeology, biodiversity, or
  other restricted layers.

Where sensitivity or rights are unclear, the dashboard must restrict, aggregate,
generalize, delay, omit, or deny. Client-side hiding is not a public-safe
transform.

### 1.6 Lifecycle and authority

```text
SOURCE / PRE-RAW
  -> RAW
  -> WORK / QUARANTINE
  -> PROCESSED
  -> CATALOG / TRIPLET
  -> PUBLISHED
  -> GOVERNED API / RELEASED ARTIFACT
  -> DASHBOARD / MAP / EVIDENCE DRAWER / FOCUS MODE
```

A dashboard may display a governed projection of lifecycle and accountability
state. It must not:

- read RAW, WORK, QUARANTINE, unresolved candidate, or internal canonical stores
  through the normal public path;
- turn validation into promotion;
- turn a receipt into proof;
- turn a catalog record into evidence;
- turn a pull request or merge into release;
- turn a dashboard card into publication authority.

[Back to top](#top)

---

<a id="2-indicator-subset"></a>

## 2. Indicator subset

The prior v0.1 page selected generic Atlas §24.11 indicators and embedded
unsupported health targets. This revision keeps those indicator families as
**design lineage** but requires every implemented metric to satisfy the current
domain-dashboard measurement contract.

### 2.1 Minimum measurement contract

Every metric definition must provide:

| Field | Required meaning |
|---|---|
| Stable identity | Metric ID, semantic version, owner, status, and supersession rule |
| Purpose | The bounded review question the metric answers and decisions it does not authorize |
| Eligible population | Exact records, candidates, artifacts, runs, sources, or releases included |
| Exclusions | Records intentionally omitted and why |
| Numerator / denominator | Exact computation, null handling, zero-denominator state, and deduplication |
| Unit | Count, ratio, duration, categorical state, distribution, or other explicit unit |
| Dimensions | Source family, source role, support type, object family, survey area, geography, depth, time window, profile version, policy state, release state, or other declared groupings |
| Spatial support | Geometry or scope identity, CRS where material, scale/resolution, and generalization |
| Temporal support | Observation, valid, source, retrieval, processing, metric-snapshot, release, and correction time where material |
| Evidence | Immutable source/evidence/validation/receipt/proof/release references supporting the metric |
| Method and uncertainty | Algorithm/profile version, known bias, confidence/uncertainty, and limitations |
| Sensitivity and rights | Public/restricted classification, transforms, aggregation, suppression, and reviewer |
| Finite state | Presentation state and, separately, any governed outcome or validator result |
| Threshold | Versioned baseline or threshold authority; no undocumented universal constant |
| Correction | How defects, late data, source reissues, and denominator changes update prior metric snapshots |
| Rollback | Prior metric profile/snapshot and deterministic restoration target |
| Review | Accountable domain, metric, evidence, policy, sensitivity, release, and independent roles as applicable |

A metric without this contract remains a `PROPOSED` card or `NO_DATA`; it is not a
production health signal.

### 2.2 Presentation states

| Presentation state | Meaning | Required behavior |
|---|---|---|
| `AVAILABLE` | The metric snapshot passed its declared structural and governance prerequisites. | Show value, unit, dimensions, method/profile, snapshot time, evidence, uncertainty, and release/correction state. |
| `NO_DATA` | No eligible records exist or the denominator is zero. | Show the reason and eligible-population definition; never display zero. |
| `STALE` | The metric or supporting source exceeds its profile-specific freshness rule. | Show source/observation/snapshot times and stop implying currentness. |
| `PARTIAL` | Some required dimensions, sources, evidence, or populations are incomplete. | Show coverage and omissions; do not normalize to complete. |
| `RESTRICTED` | Rights, sensitivity, consent, or access policy blocks the value or detail. | Show only public-safe reason/category; do not leak protected basis. |
| `REVIEW_PENDING` | Required source, evidence, scientific, policy, sensitivity, or release review is incomplete. | Hold interpretation and public-facing health classification. |
| `CORRECTED` | A newer governed snapshot corrects an earlier one. | Preserve prior identity, correction reason, affected interval, and forward link. |
| `SUPERSEDED` | A new profile, source edition, or release replaces the current one. | Preserve lineage and direct readers to the successor. |
| `WITHDRAWN` | The metric snapshot is no longer eligible for reliance. | Remove current-use presentation while preserving the withdrawal record. |
| `ERROR` | Parser, resolver, validator, policy, store, or runtime operation failed. | Fail closed; expose safe diagnostic identity without protected details. |

### 2.3 Outcome separation

| Axis | Current vocabulary | Dashboard rule |
|---|---|---|
| Runtime response | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` | Do not add dashboard-only runtime outcomes. Presentation states may refine display but cannot rewrite the envelope. |
| Validator result | Usually `PASS` / `FAIL`, with profile-specific finite outcomes where declared | Show the exact validator profile and result; never call `PASS` “approved” or “released.” |
| Review/workflow | Draft, review pending, changes requested, approved, held, or profile-specific state | Keep separate from runtime outcome and release state. |
| Lifecycle | RAW, WORK/QUARANTINE, PROCESSED, CATALOG/TRIPLET, PUBLISHED | A chart cannot mutate lifecycle state. |
| Release/correction | Candidate, released, corrected, superseded, withdrawn, rolled back, or profile-specific state | Resolve through owning release/correction records, not UI inference. |

### 2.4 Shared governance-health subset

The following Atlas-origin indicator families remain useful as lineage when
instantiated through a versioned metric contract:

- EvidenceRef-to-EvidenceBundle resolution and citation closure;
- source-role and support-type distribution;
- source vintage, refresh, and stale-state posture;
- quarantine and fail-closed reasons;
- release, correction, withdrawal, and rollback support;
- documentation, ADR, and placement drift.

No old numeric target is carried forward as current authority.

[Back to top](#top)

---

<a id="3-domain-specific-indicators-proposed"></a>

## 3. Domain-specific indicators (PROPOSED)

All metrics below are **candidate contracts**. Current repository evidence can
supply parts of some fixture-first metrics, but no production producer,
persistent snapshot store, routed panel, or accountable threshold approval was
verified.

### 3.1 Core metric register

| Metric ID | Review question | Eligible population and computation | Required dimensions and state | Current evidence boundary |
|---|---|---|---|---|
| `soil.source_support_closure` | Do candidate Soil records declare resolvable source identity, source role, support type, vintage, rights, and sensitivity? | Numerator: eligible records with all declared source/support fields and resolvable references. Denominator: exact selected candidate population. Zero denominator -> `NO_DATA`. | Source family, role, support type, object family, source vintage, rights/sensitivity, snapshot. | Contract, schema, registry, and fixture surfaces exist; live admission and universal closure are unverified. |
| `soil.support_type_separation` | Are static survey, grid, station, satellite, profile, interpretation, public-safe derivative, and fixture classes kept distinct? | Count and distribution of declared support types plus anti-collapse violations under one immutable validation run. | Profile version, exact tokens, validator, source family, object family, violation reason. | Bounded smoke, station, and SMAP profiles test selected separation; no global accepted enum is verified. |
| `soil.mukey_cokey_chkey_lineage_integrity` | Do map units, components, and horizons preserve valid ancestry and source vintage? | Numerator: eligible lineage records with unique, resolvable parent chain and matching source context. Denominator: records requiring that chain. | Survey area, source version, MUKEY/COKEY/CHKEY, object family, transform/run identity. | Synthetic fixture profiles exist; production SSURGO lineage closure is unverified. |
| `soil.component_horizon_join_integrity` | Are component-horizon joins structurally coherent and depth-valid? | Exact positive/negative fixture polarity or future production validation population; never mix fixture and production denominators. | Component/horizon identity, depth unit, top/bottom, overlap/gap rule, source vintage, validator version. | Focused no-network contract/schema/fixture/validator/test/workflow exists; persistence and public use are absent. |
| `soil.mukey_properties_aggregate_conformance` | Does a deterministic aggregate preserve component closure, horizon continuity, physical ranges, weighting, and hash binding? | Exact selected aggregate profile cases passing schema, semantic, range, aggregation, and identity checks. | MUKEY, component set, horizon set, method, depth interval, property/unit, hash/profile version. | Fixture-only `MukeyProperties` profile and workflow exist; it is inactive and non-authoritative. |
| `soil.moisture_observation_integrity` | Do soil-moisture records preserve station/reference/satellite class, depth, units, time, QC, evidence, and finite outcome? | Numerator: eligible observations passing the selected closed profile. Denominator: exact immutable fixture or future governed observation set. | Support type, source/station/product, depth, unit, timestamp/timezone, QC, freshness, evidence, outcome. | Fixture-first `SoilMoistureObservation`, station, and SMAP L4 profiles exist; live observations and production identity are unverified. |
| `soil.ssurgo_drift_state` | Did the selected SSURGO package or SDA micro-snapshot materially change, remain unchanged, fail validation, or error? | Deterministic comparison of pinned prior/current inputs under one comparator profile; categorical output, not automatic promotion. | Source package/snapshot identity, area/query, retrieval/source time, hashes, changed members/fields, reason. | Fixture-only package drift and SDA micro-snapshot surfaces exist; live fetch, rights/currentness, and source admission remain unverified. |
| `soil.temporal_vintage_state` | Are source vintage, observation time, retrieval time, metric snapshot, release time, and correction time fit for the metric's purpose? | Profile-specific classification across eligible support; no universal TTL. | Source/support type, purpose, time fields, freshness profile, stale reason, affected scope. | Time fields are enforced in bounded moisture/drift profiles; production freshness policy is absent. |
| `soil.public_safe_exposure_closure` | Are public-bound Soil metrics and geometries rights-cleared, sensitivity-reviewed, scale-fit, generalized where required, and free of protected aliases? | Numerator: eligible public-bound candidates with required policy/transform/release support. Denominator: exact public-bound population. | Audience, geography/precision, support type, rights, sensitivity, transform, policy, release, correction. | Bounded public-safe fixture validation exists; no active public policy evaluator or released panel was verified. |
| `soil.evidence_policy_release_closure` | Can each claim-bearing metric resolve evidence, policy, review, proof/release, correction, and rollback support? | Conjunctive closure over the exact eligible metric snapshots; any missing required family blocks `AVAILABLE`. | Metric/profile, EvidenceRef/EvidenceBundle, policy, review, validation, proof, release, correction, rollback. | Documentation and candidate lanes exist; proof and release jobs remain explicit holds. |
| `soil.correction_rollback_readiness` | Can a defect, source reissue, stale result, or withdrawn release be traced and reversed? | Coverage of released/current-use snapshots with correction and rollback targets. No released denominator -> `NO_DATA` or `HOLD`, not 100%. | Release identity, prior/successor, affected interval/scope, correction/withdrawal reason, invalidation, rollback drill. | Runbooks and support lanes exist; an executed Soil rollback or correction propagation was not verified. |
| `soil.dashboard_implementation_readiness` | Which dependency layers exist, are executable, are integrated, or remain held? | Categorical inventory of docs, contracts, schemas, fixtures, validators, tests, workflows, producer, store, API, panel, accessibility, policy, evidence, release, correction, deployment. | Path/blob, status, test/run identity, owner/reviewer, last check, blocker, rollback. | Repository presence and bounded workflows are inspectable; production producer, route, panel, telemetry, and release are unverified. |

### 3.2 Supplemental candidates

The following v0.1 ideas remain planning candidates, not current metrics:

| Candidate | Required clarification before admission |
|---|---|
| Soil-taxonomy edition skew | Identify the exact taxonomy field, source editions, eligible object families, crosswalk authority, and whether mixed editions are invalid or merely disclosed. |
| Hydric-soil derivative coverage | Define owning source/derivative, geographic denominator, missing/no-data treatment, relation to Habitat and Wetlands contexts, evidence, sensitivity, and release profile. |
| Prime-farmland or suitability coverage | Separate source interpretation from KFM-derived summary; prohibit land-value, regulatory, eligibility, or management inference. |
| Survey-area refresh posture | Bind to authoritative source cadence and retrieval evidence; do not infer staleness from a generic calendar interval. |
| Quarantine throughput | Define candidate class, entry/exit event, age calculation, reason taxonomy, sensitive reason handling, and whether throughput is an appropriate health signal. |

### 3.3 Proposed panel composition

| Panel | Shows | Must also show | Must not do |
|---|---|---|---|
| Source and support ledger | Source families, roles, support types, vintages, rights/sensitivity, refresh states | Snapshot identity, omissions, unresolved admission, profile version | Suggest that a listed source is active or authoritative by presence alone |
| Survey lineage | MUKEY/COKEY/CHKEY and component-horizon closure | Survey area, source version, transform/run, invalid/abstain reasons | Flatten unresolved lineage or substitute generated IDs |
| Moisture integrity | Station/reference/satellite distributions, depth/unit/QC/time posture | Support class, source/product identity, freshness profile, spatial support, uncertainty | Blend station and satellite values into an unlabeled condition surface |
| Drift review | SSURGO/SDA comparator states and changed members | Prior/current hashes, source/query identity, materiality reason, review state | Auto-update, promote, or publish changed inputs |
| Public-safety gate | Rights, sensitivity, precision/generalization, policy/release closure | Audience, transform, reviewer, release/correction/rollback identity | Reveal protected detail or protective thresholds |
| Release and correction | Candidate/release/proof/correction/rollback readiness | Exact records and missing dependencies | Equate merge or green CI with release |
| Implementation readiness | Repository surfaces from documentation through runtime | Pinned evidence and explicit `UNKNOWN` / `HOLD` states | Convert file presence into production maturity |

### 3.4 Filters and dimensions

A dashboard filter is part of the claim surface. Every filter must preserve:

- source family and source role;
- support type and exact profile vocabulary;
- object family and identity lineage;
- survey area, geography, CRS, scale/resolution, and public-safe precision;
- depth interval and unit;
- observation/source/retrieval/snapshot/release/correction time;
- validator/profile version and finite result;
- rights, sensitivity, policy, review, release, and correction state;
- no-data, stale, partial, restricted, and error states.

Filter combinations that create a sensitive small cell, private-property inference,
station-location exposure, or cross-layer reconstruction risk must be restricted
server-side before delivery. URLs, exports, logs, analytics, accessibility text,
cached payloads, search indexes, and generated language inherit the same rule.

### 3.5 Map, Evidence Drawer, and Focus Mode obligations

A claim-bearing Soil map or dashboard selection should route through a governed
payload that can expose, at a public-safe level:

- object and metric identity;
- source role and support type;
- spatial and temporal support;
- property, unit, depth, method, aggregation, QC, and uncertainty;
- EvidenceRef and resolvable EvidenceBundle status;
- policy and sensitivity posture;
- release, stale, correction, supersession, withdrawal, and rollback state;
- citations and bounded limitations.

MapLibre, the Evidence Drawer, and Focus Mode remain downstream carriers.
Focus Mode may explain released evidence and return finite outcomes; it may not
invent a Soil condition, classify a field, prescribe management, or treat model
language as evidence.

[Back to top](#top)

---

<a id="4-ownership"></a>

## 4. Ownership

### 4.1 Verified review route and missing stewardship

`@bartytime4life` is the repository's verified CODEOWNERS review route for the
inspected surfaces. CODEOWNERS routing does not establish qualified Soil,
scientific, source, evidence, policy, rights, sensitivity, metric, accessibility,
release, correction, rollback, or independent review.

| Responsibility | Required role | Current status |
|---|---|---|
| Soil domain meaning and fitness | Soil domain steward with appropriate subject expertise | `NEEDS VERIFICATION` |
| Source identity, role, rights, and cadence | Source steward / rights reviewer | `NEEDS VERIFICATION` |
| Evidence and citation closure | Evidence steward | `NEEDS VERIFICATION` |
| Pipeline, data, and metric computation | Data/pipeline and metric/observability steward | `NEEDS VERIFICATION` |
| Policy and public-safe exposure | Policy and sensitivity/privacy reviewer | `NEEDS VERIFICATION` |
| Map, dashboard, Evidence Drawer, export, and accessibility | UI/map/accessibility steward | `NEEDS VERIFICATION` |
| Release, correction, withdrawal, and rollback | Release and correction/rollback steward | `NEEDS VERIFICATION` |
| Independent review for consequential public metrics | Reviewer independent from generator/author where warranted | `NEEDS VERIFICATION` |
| GitHub review routing | `@bartytime4life` | `CONFIRMED` routing only |

### 4.2 Separation of duties

For a consequential public Soil dashboard metric, do not collapse:

1. metric author and source authority;
2. validator author and policy approver;
3. generator and human reviewer;
4. release assembler and independent release approver;
5. dashboard maintainer and correction/rollback authority.

Repository maturity may require one person to hold several roles temporarily, but
the exception must be explicit, scoped, reviewable, and must not be represented as
independent approval.

### 4.3 Review disposition vocabulary

This document may record `DRAFT`, `HOLD`, `NEEDS PATCH`, `READY FOR HUMAN
REVIEW`, `MERGE RECOMMENDED`, or `MERGE BLOCKED` for repository review. Those
states are separate from metric presentation, policy outcome, lifecycle, release,
deployment, and publication.

[Back to top](#top)

---

<a id="5-implementation-pointer"></a>

## 5. Implementation pointer

### 5.1 Current repository evidence matrix

| Surface | Current bounded evidence | What it does not prove |
|---|---|---|
| [`docs/domains/soil/README.md`](../../domains/soil/README.md) | Repository-grounded domain map with object families, support-type anti-collapse, source families, lifecycle, and partial implementation inventory. | Source admission, end-to-end production, release, or public correctness |
| [`contracts/domains/soil/README.md`](../../../contracts/domains/soil/README.md) | Soil semantic-contract index and separation of meaning from machine shape. | Accepted global vocabulary or production producer |
| [`schemas/contracts/v1/domains/soil/README.md`](../../../schemas/contracts/v1/domains/soil/README.md) | Soil schema index with mixed scaffold and concrete candidate profiles. | Universal schema closure or policy fitness |
| [`tools/validators/domains/soil/README.md`](../../../tools/validators/domains/soil/README.md) | Bounded public-safe, station-moisture, and SMAP fixture validators plus documented child lanes. | Soil truth, source admission, policy, proof, release, or runtime |
| [`domain-soil.yml`](../../../.github/workflows/domain-soil.yml) | Three deterministic synthetic Soil suites plus fixture-only SSURGO drift comparison; proof and release jobs explicitly held. | Live sources, EvidenceBundle closure, policy, proof, release, publication |
| [`soil-component-horizon-join.yml`](../../../.github/workflows/soil-component-horizon-join.yml) | Closed fixture-only ComponentHorizonJoin candidate validation. | Persisted production joins or public use |
| [`soil-mukey-properties.yml`](../../../.github/workflows/soil-mukey-properties.yml) | Fixture-only aggregate validation for lineage, continuity, ranges, weighting, and hash binding. | Authoritative Soil properties or an admitted aggregate |
| [`soil-moisture-observation.yml`](../../../.github/workflows/soil-moisture-observation.yml) | Fixture-first SoilMoistureObservation identity, support, depth, unit, QC, time, evidence, and finite-outcome checks. | Live observations or current field condition |
| [`soil-ssurgo-sda-micro-snapshot.yml`](../../../.github/workflows/soil-ssurgo-sda-micro-snapshot.yml) | Deterministic no-network micro-snapshot candidate and change-report profile. | Live SDA retrieval, source authority, or automatic promotion |
| [`apps/explorer-web/src/features/domains/soil/README.md`](../../../apps/explorer-web/src/features/domains/soil/README.md) | Proposed app-local Soil feature boundary and UI obligations. | Implemented route, panel, transport, metric producer, or deployed dashboard |
| [`data/proofs/soil/README.md`](../../../data/proofs/soil/README.md) | Soil proof-support guidance and anti-collapse boundaries. | Emitted proof object or proof-bearing release |
| [`release/candidates/soil/README.md`](../../../release/candidates/soil/README.md) | Candidate review guidance stating that a candidate is not a release. | Candidate manifest, approval, release, deployment, or publication |
| [`policy/domains/soil/README.md`](../../../policy/domains/soil/README.md) | Soil policy lane documentation. | Bound evaluator, production decision, or enforcement |
| [`data/registry/sources/soil/README.md`](../../../data/registry/sources/soil/README.md) | Source-registry boundary and topology discussion. | Activated source or current source-rights clearance |

### 5.2 Current executable proof versus held maturity

```mermaid
flowchart LR
    A["Synthetic Soil fixtures"] --> B["Closed candidate schemas / profiles"]
    B --> C["No-network validators and tests"]
    C --> D["Focused GitHub workflows"]
    D --> E["Bounded structural / polarity evidence"]

    E -. "not established" .-> F["Production metric producer"]
    F -. "not established" .-> G["Governed metric snapshot store"]
    G -. "not established" .-> H["Governed API dashboard payload"]
    H -. "not established" .-> I["Routed accessible dashboard panel"]
    I -. "not established" .-> J["Proof + release + correction + rollback"]
    J -. "not established" .-> K["Public Soil dashboard"]

    classDef confirmed fill:#ddf4ff,stroke:#0969da,color:#24292f
    classDef unknown fill:#f6f8fa,stroke:#6e7781,color:#24292f,stroke-dasharray:5 5
    class A,B,C,D,E confirmed
    class F,G,H,I,J,K unknown
```

The left side is bounded repository implementation evidence. The right side is
`PROPOSED`, `UNKNOWN`, `NEEDS VERIFICATION`, or `HOLD`.

### 5.3 Proposed runtime seam

No exact route name is adopted here. A future runtime should separate:

```text
admitted / released Soil inputs
  -> deterministic metric producer
  -> immutable metric snapshot + validation report
  -> evidence / policy / release resolver
  -> governed API response
  -> Explorer or review dashboard adapter
  -> accessible card, chart, map, Evidence Drawer, export, or Focus response
```

The browser must not query canonical lifecycle stores, source endpoints, station
feeds, model runtimes, or private data directly.

### 5.4 Minimum governed payload

A future dashboard payload should carry or resolve, as applicable:

- request, metric, profile, snapshot, and release identity;
- finite runtime outcome and public-safe reason code;
- metric state, value, unit, numerator, denominator, dimensions, and coverage;
- source roles, support types, object families, and source vintages;
- spatial support, CRS, scale/resolution, and generalization;
- temporal support and freshness profile;
- method, uncertainty, QC, exclusions, and limitations;
- EvidenceRefs and EvidenceBundle status;
- policy, sensitivity, review, proof, release, stale, correction, withdrawal, and
  rollback references;
- citations and safe next action.

A Markdown example cannot establish the final DTO. Semantic contracts and schemas
must own that decision.

### 5.5 Proposed user-interface zones

| Zone | Purpose | Minimum negative-state behavior |
|---|---|---|
| Scope bar | Geography, time, depth, source/support class, object family, profile, and audience | Refuse unsupported combinations; show narrowed scope |
| Summary cards | High-level metric states with coverage and snapshot identity | `NO_DATA`, `STALE`, `PARTIAL`, `RESTRICTED`, `REVIEW_PENDING`, and `ERROR` remain first-class |
| Lineage panel | MUKEY/COKEY/CHKEY, component-horizon, source vintage, and transform lineage | Do not fill missing parents or infer joins |
| Moisture panel | Station/reference/satellite integrity and freshness by support class | Never blend support classes without explicit derived profile and evidence |
| Drift panel | SSURGO/SDA comparator state and review queue | Changed does not mean accepted or promoted |
| Map | Public-safe scope and selected released carrier | No direct internal store; no hidden sensitive precision |
| Evidence Drawer | Sources, support, evidence, method, uncertainty, policy, release, correction | No claim-bearing value without resolvable support |
| Release/correction panel | Candidate, proof, release, correction, withdrawal, rollback | Merge/CI state must not appear as release |
| Implementation panel | Repository surfaces and holds | File presence must not appear as production maturity |

### 5.6 Accessibility and export

The future panel must provide:

- keyboard-operable filters and disclosure controls;
- text alternatives for charts and maps;
- table equivalents for essential values;
- non-color-only state encoding;
- announced loading, no-data, stale, restricted, correction, and error states;
- stable headings and focus order;
- export metadata sufficient to preserve metric/profile/snapshot/release identity,
  citations, scope, state, and correction status.

An export that loses support type, time, evidence, sensitivity, release, or
correction context is `DENY`.

### 5.7 Governed AI boundary

AI may:

- summarize an already governed metric snapshot;
- explain source role, support type, method, uncertainty, and limitations;
- compare released snapshots within scope;
- propose safe navigation or a narrower query.

AI must not:

- decide source authority, policy, sensitivity, release, or correction state;
- infer field condition from a survey, station, satellite, or model outside its
  support;
- provide agronomic, engineering, regulatory, legal, insurance, or emergency
  advice from dashboard context;
- cite dashboard pixels or generated prose as evidence;
- expose private or restricted reasons;
- answer without resolvable evidence when the claim requires it.

### 5.8 Graduation gates

A Soil dashboard remains `HOLD` for production or public use until all applicable
gates have evidence:

1. **Metric semantics** — versioned definitions, populations, units, dimensions,
   state rules, uncertainty, and thresholds.
2. **Source closure** — admitted sources, role/support classification, rights,
   sensitivity, cadence, and immutable input identity.
3. **Evidence closure** — EvidenceRefs resolve to appropriate EvidenceBundles.
4. **Implementation** — deterministic producer, snapshot schema, fixtures,
   validator, tests, and observability.
5. **Policy** — active fail-closed evaluator and public-safe transforms.
6. **Transport** — governed API contract/schema and no direct internal-store path.
7. **UI** — routed panel, accessibility, finite negative states, safe filters,
   map/drawer/export behavior.
8. **Release** — proof, review, manifest, correction, withdrawal, and rollback.
9. **Operations** — monitoring, incident/correction runbooks, backup/restore, and
   rollback drill.
10. **Accountable review** — qualified and independent review where significance
    warrants it.

[Back to top](#top)

---

<a id="6-review-cadence"></a>

## 6. Review cadence

A universal semiannual cadence is not adopted. Review frequency must follow the
metric profile, source cadence, consequence, and change signals.

### 6.1 Mandatory review triggers

Review this specification or an implemented metric when:

- a Soil semantic contract, schema, fixture profile, validator, workflow, source
  descriptor, policy, release profile, or support vocabulary changes;
- SSURGO/SDA/gSSURGO/gNATSGO or another admitted source issues a material
  package, schema, identifier, interpretation, rights, or cadence change;
- a station or satellite profile changes depth, unit, time, QC, product, latency,
  masking, or uncertainty semantics;
- a metric threshold, denominator, dimension, aggregation, spatial support, time
  window, public audience, or sensitivity transform changes;
- a new map, Evidence Drawer, Focus Mode, export, API, or dashboard consumer is
  added;
- a correction, withdrawal, supersession, rollback, incident, or public
  discrepancy occurs;
- Directory Rules, a governing ADR, CODEOWNERS, or the dashboard lane's
  placement changes;
- a hosted workflow reveals a new failure or a held proof/release producer
  appears.

### 6.2 Review packet

A review packet should include:

- immutable base, producer, profile, schema, source, and output identities;
- changed metric definitions and consumer impacts;
- source, rights, sensitivity, and public-safe transform review;
- positive, no-data, stale, partial, restricted, denied, corrected, withdrawn, and
  error cases;
- evidence, policy, review, proof, release, correction, and rollback references;
- accessibility and disclosure-resistance review;
- validation results with exact tested revision;
- rollback target and correction communication plan.

### 6.3 Correction propagation

```text
defect or source reissue detected
  -> preserve affected snapshot and evidence
  -> classify scope and consequence
  -> correct source/contract/schema/producer/profile through owning root
  -> emit new validation and review evidence
  -> issue correction / supersession / withdrawal as required
  -> rebuild governed metric snapshot
  -> invalidate affected API, map, dashboard, export, search, cache, and AI carriers
  -> verify public-safe readback
```

Never edit a historical metric snapshot in place when its identity or public
meaning changes.

<a id="documentation-correction-and-rollback"></a>

### 6.4 Documentation correction and rollback

Before merge, close the draft pull request and abandon the task branch; branch
deletion is separate. After an authorized merge:

1. transparently revert the documentation commit or apply a bounded forward
   correction;
2. restore the prior file blob `13da91fde4e62b080bb742c45e6a00adcfd021f0` only through normal shared history;
3. re-run the same documentation and receipt checks;
4. update the dashboard catalog or generated receipt if the correction changes
   their factual relationship.

A Git revert of this Markdown file is not a source rollback, metric rollback,
release withdrawal, public correction, deployment rollback, or KFM publication
transition.

[Back to top](#top)

---

<a id="7-open-questions"></a>

## 7. Open questions

### P0 — authority and safety

- [ ] **SOIL-DASH-OQ-01 — Metric authority.** Which contract family owns dashboard metric semantics and versions?
- [ ] **SOIL-DASH-OQ-02 — Active source registry.** Which Soil sources are admitted, under which roles/support types, rights, sensitivity, cadence, and public-use conditions?
- [ ] **SOIL-DASH-OQ-03 — Support vocabulary.** Which tokens are globally accepted, which are profile-local, and what lossless crosswalk governs display?
- [ ] **SOIL-DASH-OQ-04 — Policy binding.** Which active evaluator produces public-safe allow/abstain/deny/error decisions for Soil metric payloads?
- [ ] **SOIL-DASH-OQ-05 — Sensitive composition.** Which combinations of field, station, parcel, water, infrastructure, biodiversity, archaeology, or land context require aggregation, generalization, delayed access, or denial?
- [ ] **SOIL-DASH-OQ-06 — Accountable roles.** Who owns Soil science, source rights, evidence, metric/observability, policy, sensitivity, UI/accessibility, release, correction/rollback, and independent review?

### P1 — first credible dashboard slice

- [ ] **SOIL-DASH-OQ-07 — First metric.** Should the first dependency-closed slice expose fixture-suite readiness, SSURGO drift candidates, component-horizon integrity, or another lower-risk review metric?
- [ ] **SOIL-DASH-OQ-08 — Metric snapshot contract.** What fields and deterministic identity bind population, numerator, denominator, dimensions, profile, evidence, policy, release, and correction?
- [ ] **SOIL-DASH-OQ-09 — Runtime seam.** Which governed API resource and app surface own delivery without creating a parallel dashboard truth store?
- [ ] **SOIL-DASH-OQ-10 — Zero and missing semantics.** Which metric families may legitimately equal zero, and how are no-data, not-applicable, withheld, stale, and failed states encoded?
- [ ] **SOIL-DASH-OQ-11 — Freshness.** Which source- and support-specific profiles govern survey vintage, station observations, satellite products, derived grids, and metric snapshots?
- [ ] **SOIL-DASH-OQ-12 — Correction propagation.** Which clients, caches, exports, search indexes, and AI surfaces must be invalidated or recompiled after a correction?

### P2 — expansion and convergence

- [ ] **SOIL-DASH-OQ-13 — Taxonomy editions.** How are Soil Taxonomy edition, source interpretation edition, and map-unit lineage represented and crosswalked?
- [ ] **SOIL-DASH-OQ-14 — Hydric and suitability metrics.** Which domain owns cross-domain coverage metrics, and what conclusions are explicitly prohibited?
- [ ] **SOIL-DASH-OQ-15 — Telemetry.** Which metric producer/run signals are operationally necessary, safe to retain, and allowed for the dashboard audience?
- [ ] **SOIL-DASH-OQ-16 — Dashboard-lane placement.** Does accepted documentation governance retain this lane long term, or is a reviewed compatibility/migration decision required?
- [ ] **SOIL-DASH-OQ-17 — Runtime proof.** What exact evidence moves runtime status from `NEEDS VERIFICATION` to `CONFIRMED` without conflating route presence, green tests, deployment, release, and public use?

[Back to top](#top)

---

<a id="8-evidence-basis--citations"></a>

## 8. Evidence basis & citations

### 8.1 Repository evidence ledger

| Evidence | Verified observation | Limits |
|---|---|---|
| Current target at `main@6aaea704230259e4fca30fcc0b9c1a168e12c2c2` | v0.1 exists at the requested path with stable document identity and eight legacy sections. | Prior prose is Atlas-first and predates current Soil implementation evidence. |
| [`docs/dashboards/domain/README.md`](./README.md) | Domain dashboard specs must preserve measurement, finite-state, source-role, sensitivity, correction, and authority boundaries. | It does not implement metrics or runtime. |
| [`docs/dashboards/DASHBOARD_CATALOG.md`](../DASHBOARD_CATALOG.md) | The Soil specification is cataloged as a confirmed file; runtime remains proposal-level. | The row is an index, not runtime proof. |
| [`docs/domains/soil/README.md`](../../domains/soil/README.md) | Current Soil object families, support-type distinctions, source families, lifecycle, and partial implementation posture. | Documentation does not prove active source, policy, release, or public behavior. |
| Soil contract and schema indexes | Semantic and machine surfaces exist with mixed maturity and profile-local authority. | No single global Soil runtime DTO or support enum is accepted here. |
| Soil validator index and focused workflows | Multiple bounded deterministic no-network profiles exist. | Their results are limited to selected synthetic fixtures and declared checks. |
| Explorer Soil feature README | A proposed app-local feature and governed UI boundary exists. | No routed dashboard, transport, producer, or deployed panel is proved. |
| Soil proof and candidate release READMEs | Proof-support and release-candidate boundaries explicitly preserve holds and non-effects. | No emitted proof, approved candidate, release, correction propagation, or rollback drill is proved. |
| Accepted ADR-0029 and [`directory-rules.md`](../../doctrine/directory-rules.md) | `docs/` owns human-readable explanation; same-path maintenance does not create machine or release authority. | This update does not settle every dashboard-lane migration question. |
| CODEOWNERS | `@bartytime4life` is the verified GitHub review route. | Routing is not specialist stewardship, independent approval, release approval, or publication authority. |

### 8.2 Supplied planning lineage

The **KFM Soil Architecture Extended Pro PDF-Only Planning Report** is retained as
a design source. It proposed a governed Soil family spanning static survey,
gridded derivatives, station moisture, satellite grids, profile evidence,
interpretations, validators, receipts, catalog closure, and public map delivery.
It also explicitly recorded that no mounted repository was available during that
report's creation. Therefore:

- its support-type anti-collapse, evidence-first, fixture-first, lifecycle, and
  public-interface boundaries remain useful planning lineage;
- its proposed paths, routes, schemas, sources, thresholds, and implementation
  sequence are not current repository facts;
- current repository bytes and tests control current implementation claims.

The Atlas §24.11 indicator family remains additional design lineage. Neither
source outranks current accepted decisions, contracts, schemas, policy, code,
tests, evidence, or release records for current behavior.

### 8.3 Validation expected for this documentation change

| Check | Expected outcome |
|---|---|
| One complete `KFM_META_BLOCK_V2` and one H1 | `PASS` |
| Metadata token grammar | `type: standard`; no semicolon-delimited pseudo-enum |
| Legacy anchors | `top` plus the eight prior section anchors remain resolvable |
| Same-document navigation | Every fragment resolves |
| Fences and Mermaid source | Balanced and parseable as Markdown source |
| Tables | Consistent column count and readable at GitHub width |
| Relative links | Resolve to inspected repository-present paths |
| Text hygiene | UTF-8, LF, final newline, no tabs, trailing whitespace, or conflict markers |
| Sensitive-content review | No private source payload, exact protected location, credential, or operational transform threshold |
| Authority review | No source, evidence, policy, review, release, deployment, or publication overclaim |
| Remote diff/readback | Only the authorized documentation and provenance paths change; final bytes match their recorded identities |

Repository-native and hosted checks remain separate evidence. A passing
documentation check proves only the source/document contract it evaluates.

### 8.4 Negative tests for a future implementation

A future dashboard implementation should include deterministic cases proving it
does not:

1. treat no denominator as 100% or zero;
2. treat missing, stale, restricted, partial, or error data as healthy;
3. merge station, satellite, static survey, model, profile, and interpretation
   support without an explicit governed derivative;
4. lose MUKEY/COKEY/CHKEY or component-horizon lineage;
5. infer a field, county, watershed, or parcel condition outside source support;
6. expose exact private station, farm, parcel, profile, or cross-layer-sensitive
   detail;
7. use a dashboard card, map pixel, model output, generated summary, or fixture
   as evidence;
8. read RAW, WORK, QUARANTINE, unresolved candidate, or direct model stores from
   the public client;
9. treat CI, a receipt, proof-support README, candidate, merge, or deployment as
   release;
10. omit correction, withdrawal, supersession, or rollback state from a current-use
    metric;
11. retain corrected values in caches, exports, search, maps, or AI responses
    without invalidation;
12. provide agronomic, engineering, legal, regulatory, insurance, compliance, or
    emergency advice from dashboard context.

### 8.5 No-loss modernization ledger

| Prior v0.1 element | v0.2.0 treatment |
|---|---|
| Stable `doc_id` and path | Preserved |
| H1 identity and `top` anchor | Preserved; title clarified |
| Eight numbered sections | Preserved through explicit anchors and expanded content |
| Atlas §24.11 indicator relationship | Retained as design lineage, not current machine authority |
| Evidence/source and documentation/drift emphasis | Expanded into versioned measurement and readiness contracts |
| MUKEY stability, taxonomy skew, hydric coverage ideas | Retained as candidate metrics with missing-definition gates |
| SSURGO-focused scope | Expanded to current repository support families while preserving source admission limits |
| Generic ownership placeholders | Replaced with verified GitHub routing plus explicit missing specialist roles |
| Proposed `apps/review-console/` runtime claim | Replaced with current Explorer feature seam and runtime `UNKNOWN` |
| Semiannual cadence | Replaced with source-, profile-, consequence-, and event-driven review |
| Two open questions | Retained and expanded into prioritized verification work |
| “Specification only” boundary | Strengthened with current executable/held maturity and explicit non-effects |

<a id="authority-and-non-effects"></a>

### 8.6 Authority and non-effects

This document does not:

- create or modify a Soil source descriptor, contract, schema, fixture, validator,
  test, workflow, policy, EvidenceBundle, receipt, proof, catalog record, release
  candidate, manifest, correction, withdrawal, or rollback card;
- activate or fetch a live source;
- compute or store a production metric;
- create a dashboard route, API payload, map layer, Evidence Drawer response,
  Focus Mode answer, export, telemetry stream, deployment, or public endpoint;
- accept a metric threshold, support vocabulary, policy, or steward assignment;
- promote lifecycle state, release, deploy, publish, merge itself, or change
  repository settings.

### 8.7 Current disposition

| Area | Disposition |
|---|---|
| Documentation modernization | `PROPOSED` pending review |
| Bounded fixture-first Soil validation | `CONFIRMED` repository presence; exact scope only |
| Production metric semantics | `PROPOSED` |
| Live sources and production telemetry | `UNKNOWN` |
| Routed dashboard and governed payload | `NEEDS VERIFICATION` |
| Policy, proof, release, correction, rollback execution | `HOLD` / `NEEDS VERIFICATION` |
| Deployment and public parity | `UNKNOWN` |
| Release, promotion, publication | None |

[Back to top](#top)

---

<sub>
This specification is a human review contract. Soil meaning remains with its
semantic authorities; machine shape with schemas; source identity with the
source registry; evidence with EvidenceBundle records; admissibility with policy;
validation with validators and tests; release, correction, withdrawal, and
rollback with their owning records; and public behavior with governed,
released implementations.
</sub>

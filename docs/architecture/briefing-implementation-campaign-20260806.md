<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/architecture/briefing-implementation-campaign-20260806
title: Briefing Implementation Campaign — Current Bounded Record and Graduation Map
type: architecture-implementation-record
version: v1.0-draft
status: repository-grounded; historical-campaign-record; synthetic-only; no-network; non-authoritative; migration-hold
owners:
  - "@bartytime4life — CODEOWNERS review route only"
  - "NEEDS VERIFICATION — accountable data, temporal, observability, map/runtime, hazards, validation, and release stewardship"
created: 2026-08-06
updated: 2026-08-19
policy_label: public; architecture; implementation-history; validation; geospatial; non-authoritative
owning_root: docs/
current_path: docs/architecture/briefing-implementation-campaign-20260806.md
responsibility: Record the bounded August 6 implementation campaign, its current repository-backed component state, later successor lineage, validation surface, trust boundary, graduation holds, and rollback without becoming durable briefing architecture, contract, schema, policy, source, evidence, release, deployment, or publication authority.
truth_posture: CONFIRMED current repository paths and bytes at the pinned snapshot / CONFIRMED historical PR and receipt records within their original scope / PROPOSED graduation requirements / UNKNOWN current runtime, live-source, browser, production-storage, and public-operation state unless separately evidenced
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 4f222c5b7ef852d2f3577b2a27c146d3d3641225
  prior_target_blob: ce6471fde67e4e5d7f65ba0ae763077be81cdaac
  original_campaign_pr: 2056
  original_campaign_head: 308e974c031be80ef1e6c675cbbfc9f590d56d06
  original_campaign_merge: fb9ec74909689d481d780575f23754bfc4cba964
  accepted_directory_decision: ADR-0029
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  current_campaign_workflow_blob: 47f667022cf3c5030bf5e7597ad793470ad67a60
  current_temporal_store_blob: 3a965ba5a0a5bf9ca57c3fb48ef4283758712324
  current_trace_closure_blob: 355c6d538131cb7b665f2feb7f84128183d21255
  current_maplibre_readiness_profile: kfm-maplibre-v6-4-readiness-v3
  current_maplibre_target: 6.4.0
  current_maplibre_upstream_tag_commit: 4529c6e451f0e5607ef42ad0ed81aa76a14a0f43
  current_usdm_materiality_blob: dac5f56560f40e725c4d8924d8d20138ae5708fd
  open_pull_requests_for_exact_target_at_preflight: 0
related:
  - README.md
  - briefing-integration.md
  - briefing-live-issue-inventory-binding.md
  - document-convergence-plan.md
  - ../doctrine/directory-rules.md
  - ../adr/ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md
  - "../adr/ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md"
  - ../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../contracts/data/temporal_slice.md
  - ../../contracts/data/material_change_assessment.md
  - ../../contracts/telemetry/trace_receipt_link.md
  - ../../tools/experiments/temporal_slice_store.py
  - ../../tools/validators/validate_trace_temporal_closure.py
  - ../../tools/validators/maplibre/validate_v6_readiness.py
  - ../../tools/validators/domains/hazards/validate_usdm_materiality.py
  - ../../tests/experiments/test_temporal_slice_store.py
  - ../../tests/validators/test_validate_trace_temporal_closure.py
  - ../../tests/maplibre/test_validate_v6_readiness.py
  - ../../tests/domains/hazards/test_validate_usdm_materiality.py
  - ../../.github/workflows/briefing-implementation-campaign.yml
  - ../../data/receipts/generated/genrec-briefing-implementation-campaign-20260806.json
  - ../../data/receipts/generated/genrec-maplibre-v6-4-readiness-current-binding-20260818.json
notes:
  - "Same-path documentation modernization only. The implementation components, contracts, schemas, fixtures, tests, workflow, historical receipts, dependencies, source posture, release state, and repository settings are unchanged."
  - "The durable briefing-to-system architecture is briefing-integration.md. This dated page is implementation history and must not compete with it."
  - "The architecture convergence plan assigns this page HOLD for any future move to a reports/archive/history lane until destination, identity, inbound links, and no-loss closure are verified."
  - "The original generated receipt remains historical process memory. It is not rewritten into a current-byte manifest or human approval record."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Briefing implementation campaign — August 6, 2026

> **Purpose.** Preserve an inspectable, repository-grounded record of the bounded August 6 campaign; distinguish what its four synthetic implementation slices currently prove from what they do not prove; record later MapLibre successor lineage; and identify the evidence required before any component can graduate toward operational use.

| Field | Current bounded result |
|---|---|
| **Document role** | Dated architecture implementation record under `docs/architecture/`; not the durable briefing architecture and not implementation, policy, evidence, release, or publication authority. |
| **Evidence snapshot** | `main@4f222c5b7ef852d2f3577b2a27c146d3d3641225`. |
| **Original campaign lineage** | PR [#2056](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/2056), head `308e974c031be80ef1e6c675cbbfc9f590d56d06`, merge commit `fb9ec74909689d481d780575f23754bfc4cba964`. |
| **Durable briefing architecture** | [`briefing-integration.md`](briefing-integration.md). That page owns the reusable BriefingSignal-to-governed-work narrative. |
| **Placement decision** | `PLACE` for this same-path correction; `HOLD` on any move or archival migration under the current [convergence plan](document-convergence-plan.md). |
| **Campaign scope** | Four fixture-first, deterministic, no-network slices: TemporalSlice SQL indexing, trace-to-temporal reference closure, MapLibre readiness classification, and USDM material-change classification. |
| **Current MapLibre target** | Exact `6.4.0` under profile `kfm-maplibre-v6-4-readiness-v3`; current repository posture remains `HOLD`. |
| **Current external operation** | No live USDM retrieval, live telemetry, production database, admitted MapLibre dependency, authenticated browser probe packet, source activation, or public product is established. |
| **Publication effect** | None. A fixture, test, validator, workflow, receipt, pull request, merge, or `PROMOTION_CANDIDATE` is not KFM release or publication. |

> [!IMPORTANT]
> **This page records implementation history; it does not create present-tense authority.** Repository bytes prove that bounded tools, fixtures, tests, and a read-only workflow exist. They do not prove a production storage service, a live observability chain, a functioning MapLibre renderer, an admitted USDM source, an approved materiality policy, a release, a deployment, or public operation.

> [!CAUTION]
> **Do not collapse the dated campaign into the durable briefing architecture.** The reusable intake, identity, routing, official-source, evidence-binding, and issue-inventory model lives in [`briefing-integration.md`](briefing-integration.md). This page explains one historical implementation packet and its current descendants.

> [!WARNING]
> **All four slices remain downstream of KFM trust controls.** A local `PASS`, `READY` fixture, or `PROMOTION_CANDIDATE` classification cannot resolve `EvidenceRef`, evaluate rights or policy, approve review, promote lifecycle state, release an artifact, deploy a service, publish a map, or authorize public use.

**Quick navigation:** [Role and scope](#1-role-and-scope) · [Truth and evidence](#2-truth-and-evidence) · [Campaign lineage](#3-campaign-lineage-and-current-state) · [Components](#components) · [Artifact map](#5-current-artifact-map) · [Trust boundary](#trust-boundary) · [Validation](#validation) · [Graduation holds](#8-graduation-and-hold-register) · [Provenance](#9-provenance-and-receipt-lineage) · [Directory Rules](#10-directory-rules-and-document-convergence) · [Rollback](#rollback) · [Related work](#12-related-work) · [Change history](#appendix-a--change-history)

---

<a id="1-role-and-scope"></a>

## 1. Role and scope

The campaign began as a dependency-closed implementation of four still-actionable items from the August 6 briefing. The earlier `AIChangeProposal` fixture-classification correction already existed in later repository history and was deliberately not duplicated.

### This record owns

- the historical campaign boundary and its original pull-request lineage;
- a current map of the four implementation slices;
- the distinction between historical validation evidence and current repository bytes;
- later successor lineage that materially changed the MapLibre readiness component;
- explicit trust, graduation, correction, and rollback boundaries;
- a review-oriented map of contracts, tools, fixtures, tests, workflows, and receipts.

### This record does not own

| Concern | Owning surface |
|---|---|
| Reusable briefing intake and routing architecture | [`briefing-integration.md`](briefing-integration.md) |
| Live issue-inventory read and stored-receipt binding detail | [`briefing-live-issue-inventory-binding.md`](briefing-live-issue-inventory-binding.md) and its contract/tool surfaces |
| Object meaning | `contracts/` |
| Machine-valid shape | `schemas/` |
| Admissibility, rights, sensitivity, or disclosure | `policy/` plus governed review |
| Source identity and activation | governed source/registry and connector surfaces |
| Lifecycle instances, evidence, receipts, proofs, catalogs, and published carriers | `data/` under their distinct families |
| Release, correction, withdrawal, and rollback decisions | `release/` and governing records |
| Executable validation | `tools/`, `tests/`, fixtures, and workflows |
| MapLibre architecture decision | ADR-0006/ADR-0007 decision process; both remain proposed |
| Deployment and public operation | application, runtime, infrastructure, release, and operations evidence |

### Non-goals of this update

This documentation correction does not:

- change the four implementation modules, fixtures, tests, or workflow;
- rewrite the historical campaign receipt;
- install or admit MapLibre;
- create a production database or migration;
- start live telemetry or resolve a live EvidenceBundle;
- fetch USDM or activate any source;
- select or approve a materiality threshold profile;
- accept ADR-0006 or ADR-0007;
- change GitHub settings, checks, rulesets, or branch protection;
- promote, release, deploy, publish, or widen access;
- move this page into a new history/archive lane.

[Back to top](#top)

---

<a id="2-truth-and-evidence"></a>

## 2. Truth and evidence

### Truth labels

| Label | Meaning in this page |
|---|---|
| `CONFIRMED` | Verified from current repository bytes at the pinned snapshot, accepted ADR-0029, an inspected historical PR/receipt, or an inspected issue. |
| `PROPOSED` | A semantic contract, readiness target, threshold profile, architecture decision, or graduation step not accepted or operationally proven. |
| `UNKNOWN` | Current runtime, source, environment, review, release, or public state cannot be established from the inspected repository evidence. |
| `NEEDS VERIFICATION` | A specific current test, hosted run, live probe, source-rights check, operational rehearsal, or owner decision remains. |
| `HOLD` | Advancement must stop until the named evidence closes. |

Runtime and validator outcomes such as `FOUND`, `NOT_FOUND`, `AMBIGUOUS`, `READY`, `PASS`, `FAIL`, `NON_EVENT`, `PROMOTION_CANDIDATE`, `HOLD`, and `ERROR` are component-local finite outcomes. They do not replace truth labels, review state, lifecycle state, release state, or publication state.

### Evidence basis

| Evidence | What it supports | What it does not prove |
|---|---|---|
| Current target and component files at `main@4f222c5b7ef852d2f3577b2a27c146d3d3641225` | File presence, current text/code/config shape, and bounded implementation posture | Current successful execution or production behavior |
| Accepted [`ADR-0029`](../adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Adopted Directory Rules bytes and responsibility-root placement law | Acceptance of any component contract, threshold, source, or renderer decision |
| PR [#2056](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/2056) | Original campaign scope, original head, declared local validation, changed roots, and historical trust boundary | Current exact-head validation, human approval, operational maturity, release, or publication |
| Original [`GENERATED_RECEIPT`](../../data/receipts/generated/genrec-briefing-implementation-campaign-20260806.json) | Historical authorship/process memory and original artifact-byte bindings | Current-byte manifest, factual proof, human approval, merge authority, or release authority |
| Current campaign [workflow](../../.github/workflows/briefing-implementation-campaign.yml) | Declared read-only/no-network orchestration and expected MapLibre `HOLD` assertion | That the workflow is required, currently green, or production-equivalent |
| MapLibre 6.4 successor PR [#3017](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/3017) and successor receipt | Exact inactive readiness target, profile evolution, historical-receipt preservation, and declared local validation | Dependency admission, tarball integrity, browser evidence, ADR acceptance, or renderer deployment |
| Open issues [#2957](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/2957) and [#2906](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/2906) | Current architecture/ownership and browser-probe HOLDs | Their future disposition or permission to implement around them |
| Architecture [convergence plan](document-convergence-plan.md) | Provisional `HOLD` on moving this dated record until receiving-lane and reference closure exist | Automatic migration authority |

### Evidence hierarchy

For current behavior, current code/configuration/tests/workflows/logs/artifacts outrank this page. For meaning, contracts outrank implementation-note prose. For machine shape, schemas outrank examples. For admissibility, policy and review outrank validators. For release, the release decision and its evidence closure outrank a pull request or receipt.

[Back to top](#top)

---

<a id="3-campaign-lineage-and-current-state"></a>

## 3. Campaign lineage and current state

### 3.1 Original campaign

PR [#2056](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/2056) introduced the initial fourteen-artifact campaign on a synthetic, no-network basis. Its recorded local validation included 27 focused tests, fixture polarity, module compilation, workflow parsing, and a generated receipt. That evidence is **historical at the original head**, not a current-main rerun.

The campaign's original non-goals remain controlling for interpretation:

- no live USDM retrieval;
- no production storage;
- no MapLibre dependency selection;
- no telemetry deployment;
- no source admission;
- no proof, promotion, release, deployment, or publication.

### 3.2 Later evolution

The MapLibre readiness lane evolved after the original campaign. The current classifier targets exact MapLibre GL JS `6.4.0`, profile `kfm-maplibre-v6-4-readiness-v3`, and upstream tag commit `4529c6e451f0e5607ef42ad0ed81aa76a14a0f43`. A successor receipt preserves the historical earlier receipts rather than rewriting them.

The other three campaign components remain fixture-first, local, and no-network at the inspected snapshot.

### 3.3 Current bounded state

| Component | Current repository state | Operational state |
|---|---|---|
| TemporalSlice SQL index | Standard-library SQLite experiment plus focused tests | Production repository/database is `UNKNOWN`; graduation `HOLD` |
| Trace-to-temporal closure | Deterministic local validator, synthetic artifact, exact negative fixtures, focused tests | Live trace, receipt, evidence resolver, attestation, and policy closure are `UNKNOWN`; graduation `HOLD` |
| MapLibre readiness | Exact 6.4.0 classifier, 12-probe profile, fixtures/tests, successor receipt, workflow assertion | Current repository is `HOLD`; dependency and browser evidence are absent |
| USDM materiality | Synthetic weekly snapshot comparator, finite outcomes, exact negative fixtures, focused tests | Source activation, native snapshots, reviewed thresholds, and release path are `UNKNOWN`; graduation `HOLD` |

### 3.4 State separation

Do not compress these states:

```text
fixture passes
  != contract accepted
  != source admitted
  != evidence resolved
  != policy approved
  != review approved
  != promotion authorized
  != release approved
  != deployed
  != published
```

A `PROMOTION_CANDIDATE` is an input to later evidence/policy/review/release gates. `READY` is classifier eligibility under one profile. Neither is a release decision.

[Back to top](#top)

---

<a id="components"></a>

## Components

<a id="4-1-temporal-slice-sql-storage-experiment"></a>

### 4.1 TemporalSlice SQL storage experiment

[`tools/experiments/temporal_slice_store.py`](../../tools/experiments/temporal_slice_store.py) provides an in-memory, Python-standard-library SQLite executor for a conservative SQL subset intended to remain portable to DuckDB.

It creates two explicit indexes:

```text
(dataset_version_ref, grid_key, temporal_start, temporal_end, slice_id)
(dataset_version_ref, grid_key, temporal_start, delta_magnitude, slice_id)
```

#### Current confirmed behavior

- half-open selection windows: `temporal_start <= instant < temporal_end`;
- stable partitioning by `dataset_version_ref` and `grid_key`;
- finite `FOUND`, `NOT_FOUND`, and fail-closed `AMBIGUOUS` outcomes;
- explicit predecessor/successor lineage rather than implicit overlap resolution;
- deterministic changed-slice ordering by delta, start time, and slice identity;
- validation of canonical UTC timestamps, governed change states, nonnegative deltas, non-placeholder SHA-256 digests, and non-self lineage;
- duplicate `slice_id` rejection by the local table constraint;
- an in-memory self-test only.

The current focused test file contains eight test methods covering index presence, half-open selection, ambiguity, explicit supersession, deterministic ordering, partition isolation, invalid input, and duplicate identity.

#### Semantic boundary

[`TemporalSlice`](../../contracts/data/temporal_slice.md) remains a **proposed, fixture-first, non-authoritative semantic contract**. It permits `PROCESSED` or `CATALOG` candidates only. This SQL experiment is not that contract's production repository and does not prove that referenced evidence, receipts, policies, or artifacts resolve.

#### Explicit non-proof

The experiment does not establish:

- a selected production database engine;
- durable storage, migrations, transactions, concurrency, retention, backups, restore, or access control;
- canonical JSON identity recomputation for every persisted row;
- foreign-key resolution to `DatasetVersion`, `EvidenceBundle`, `RunReceipt`, or artifact records;
- policy, review, catalog, release, deployment, publication, or public use.

#### Graduation evidence required

Before this experiment can inform a production repository, a separate reviewed slice must establish:

1. accountable storage and temporal ownership;
2. accepted physical/logical storage decision;
3. contract/schema/repository mapping and migration semantics;
4. concurrent write and supersession behavior;
5. idempotent replay and correction handling;
6. evidence/receipt/artifact reference resolution;
7. retention, backup, restore, security, and observability;
8. focused failure, migration, and rollback tests;
9. no direct public-store path.

[Back to top](#top)

<a id="4-2-trace-to-temporal-closure"></a>

### 4.2 Trace-to-temporal closure

[`tools/validators/validate_trace_temporal_closure.py`](../../tools/validators/validate_trace_temporal_closure.py) checks a synthetic, local chain:

```text
RunReceipt digest
  -> EvidenceBundle run-receipt binding
  -> TraceReceiptLink run/evidence anchors
  -> TemporalSlice provenance references
  -> materialized artifact SHA-256
```

#### Current confirmed behavior

The validator:

- parses bounded UTF-8 JSON while rejecting duplicate keys and non-finite numbers;
- rejects missing, oversized, unreadable, symlinked, or non-object inputs;
- recomputes a closure identity from the declared cross-contract anchors;
- checks run ID, `spec_hash`, receipt reference, EvidenceBundle reference, and digest agreement;
- requires canonical sorted evidence references;
- rejects noncanonical artifact paths, path escape, and symlink traversal;
- recomputes committed materialized artifact bytes;
- keeps authority, evidence-closure, policy, promotion, release, publication, and public-use flags false;
- emits stable finding codes and fields rather than protected payload values.

The current focused test file contains six test methods, including exact fixture findings, closure-ID recomputation, artifact-byte mutation, path escape, and authority-overclaim rejection.

#### Semantic boundary

[`TraceReceiptLink`](../../contracts/telemetry/trace_receipt_link.md) remains a **draft/proposed, fixture-first linkage contract**. A local closure `PASS` says only that the synthetic references and bytes agree under this validator. It does not authenticate any referenced object or prove truth.

#### Explicit non-proof

This slice does not:

- start or observe a real OpenTelemetry trace;
- operate an OTLP collector, Tempo, Jaeger, Grafana, or alert route;
- resolve a live `RunReceipt` or `EvidenceBundle`;
- verify OCI presence, Cosign signature, Rekor inclusion, SLSA provenance, or external attestation;
- evaluate policy, rights, sensitivity, or review;
- promote, release, deploy, publish, or open a public route.

#### Graduation evidence required

A live closure profile needs a separately governed packet for real trace identity, service and environment binding, resolver authority, signature/attestation verification, freshness, safe telemetry retention, sensitive-payload minimization, policy behavior, failure containment, correction, and rollback. A missing dependency must fail closed rather than degrade to generated confidence.

[Back to top](#top)

<a id="4-3-maplibre-gl-js-6-4-readiness"></a>

### 4.3 MapLibre GL JS 6.4 readiness

[`tools/validators/maplibre/validate_v6_readiness.py`](../../tools/validators/maplibre/validate_v6_readiness.py) is an **inactive readiness classifier**, not a package installer or renderer admission gate.

#### Current target

| Field | Current value |
|---|---|
| Profile | `kfm-maplibre-v6-4-readiness-v3` |
| Exact target | `6.4.0` |
| Upstream tag commit binding | `4529c6e451f0e5607ef42ad0ed81aa76a14a0f43` |
| Finite outcomes | `READY`, `HOLD`, `ERROR` |
| Current repository result | `HOLD` by the declared workflow expectation |
| Decision state | ADR-0006 and ADR-0007 remain proposed |
| Execution owners | Issues [#2957](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/2957) and [#2906](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/2906) remain open |

#### Current repository evidence

- [`packages/maplibre/package.json`](../../packages/maplibre/package.json) is private `@kfm/maplibre` version `0.0.0` with no `maplibre-gl` dependency.
- [`packages/maplibre/src/index.ts`](../../packages/maplibre/src/index.ts) is a placeholder export.
- [`apps/explorer-web/package.json`](../../apps/explorer-web/package.json) is ESM but has no MapLibre dependency.
- [`apps/explorer-web/tsconfig.json`](../../apps/explorer-web/tsconfig.json) targets ES2022.
- [`apps/explorer-web/src/adapters/MapLibreAdapter.ts`](../../apps/explorer-web/src/adapters/MapLibreAdapter.ts) is comment-only.
- `configs/maplibre/v6-probe-results.json` was absent at the pinned snapshot.
- ADR-0006 and ADR-0007 are not accepted decisions.
- The successor generated receipt binds the current classifier/workflow/test/fixture bytes but records human review as pending and no upgrade authority.

Those facts support `HOLD`; they do not support a functioning adapter or renderer.

#### Readiness conditions

The classifier requires:

- one exact `6.4.0` dependency selection;
- ESM and ES2022;
- no direct MapLibre acquisition outside the inspected `packages/maplibre/` boundary;
- no known internal `map.transform` access;
- an exact profile and upstream-tag binding;
- all required probe outcomes supplied as `PASS`, `FAIL`, or `NOT_RUN`;
- governance effects fixed false.

#### Required probe matrix

1. `webgl2_failure_handling`
2. `worker_csp_loading`
3. `style_spec_v25`
4. `geojson_set_data`
5. `query_rendered_features`
6. `visual_pixel_diff`
7. `image_source_texture_reclamation`
8. `query_rendered_features_tile_churn`
9. `pmtiles_vector_tile_loading`
10. `terrain_dem_regression`
11. `evidence_drawer_selection_stability`
12. `headless_render_parity`

A missing result is `NOT_RUN`, not `PASS`. A fully populated synthetic `READY` fixture proves classifier polarity only.

#### Current focused tests

The current focused test file contains fourteen test methods covering:

- exact 6.4.0 success;
- prior-minor and missing-dependency holds;
- package/Explorer version conflict;
- Explorer-manifest compatibility;
- malformed package metadata;
- floating version rejection;
- internal API and import-boundary violations;
- new probe pending/failure behavior;
- legacy profile rejection;
- upstream tag mismatch; and
- declared-outcome overclaim.

#### Remaining HOLDs

- resolve package home, adapter seam, dependency ownership, acquisition inventory, consumer migration, and renderer-family disposition in [#2957](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/2957);
- bind npm tarball integrity, package-manager resolution, and lockfile bytes;
- execute all 12 authenticated interactive/headless probes under [#2906](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/2906);
- establish a functioning `MapRuntimePort` / `MapLibreAdapter` implementation only after authority closes;
- preserve rollback to the dependency-free scaffold;
- keep dependency admission, ADR acceptance, release, deployment, and publication as separate decisions.

[Back to top](#top)

<a id="4-4-usdm-material-change-profile"></a>

### 4.4 USDM material-change profile

[`tools/validators/domains/hazards/validate_usdm_materiality.py`](../../tools/validators/domains/hazards/validate_usdm_materiality.py) compares immutable **synthetic** weekly U.S. Drought Monitor-shaped snapshots under profile `kfm-usdm-materiality-v1`.

#### Finite state and outcome mapping

| Computed state | Outcome | Meaning |
|---|---|---|
| `UNCHANGED` | `NON_EVENT` | Geometry, severity areas, and population support did not change. |
| `SEMANTIC_NON_MATERIAL` | `NON_EVENT` | Meaning changed, but no declared threshold triggered. |
| `MATERIAL` | `PROMOTION_CANDIDATE` | One or more declared criteria triggered; later gates still control advancement. |
| `UNDETERMINED` | `HOLD` | Available geometry/metrics do not support a deterministic materiality result. |

#### Current confirmed behavior

The validator:

- requires synthetic-only and network-forbidden flags;
- restricts observation snapshots to `valid_date`, `geometry_digest`, `area_percent`, and `population_in_drought`;
- checks weekly ordering;
- checks `D4 <= D3-D4 <= D2-D4 <= D1-D4`;
- validates area percentages and population counts;
- compares statewide/severe area, population fraction, severe-category appearance, and geometry/metric agreement;
- recomputes and compares the declared assessment;
- rejects authority, source-activation, promotion, release, or publication overclaims;
- rejects administrative drought-stage or other legal/government-action fields from the physical classification snapshot.

The current focused test file contains six test methods covering all four valid states, deterministic criteria, geometry-only hold, severe-category appearance, exact invalid findings, and administrative-field rejection.

#### Source-role anti-collapse

The profile deliberately keeps these object families separate:

```text
USDM expert classification
  != precipitation observation
  != soil-moisture observation
  != streamflow or groundwater observation
  != reservoir or supply status
  != forecast
  != impact report
  != administrative or legal drought declaration
```

The profile compares one synthetic classification family only. It does not decide whether a physical classification should trigger a government action, public warning, planning response, or KFM release.

#### Semantic boundary

[`MaterialChangeAssessment`](../../contracts/data/material_change_assessment.md) is a **proposed, fixture-first, non-authoritative shared contract**. It records comparison results; it does not own domain thresholds. `PROMOTION_CANDIDATE` means only that later evidence, policy, review, and release evaluation may begin.

#### Graduation evidence required

Before using live USDM materiality:

1. admit an exact official source descriptor and terms/rights posture;
2. bind source-native identity, publication/valid/retrieval times, geography, revision, and correction lineage;
3. capture immutable source snapshots with digests and retrieval receipts;
4. have qualified domain review approve or revise the threshold profile;
5. prove Kansas/spatial aggregation semantics and uncertainty behavior;
6. preserve classification versus administrative-action separation;
7. add stale, missing-week, correction, conflict, and withdrawal fixtures;
8. bind evidence, policy, review, release, correction, and rollback;
9. ensure public map/API/UI language is non-emergency and source-attributed.

[Back to top](#top)

---

<a id="5-current-artifact-map"></a>

## 5. Current artifact map

| Responsibility | Current path | Status and role |
|---|---|---|
| Campaign record | `docs/architecture/briefing-implementation-campaign-20260806.md` | Current page; dated non-authoritative history |
| Durable briefing architecture | `docs/architecture/briefing-integration.md` | Reusable architecture; separate from this record |
| SQL experiment | `tools/experiments/temporal_slice_store.py` | Synthetic in-memory experiment |
| Trace closure validator | `tools/validators/validate_trace_temporal_closure.py` | Synthetic local cross-reference/byte closure |
| MapLibre readiness validator | `tools/validators/maplibre/validate_v6_readiness.py` | Inactive exact-target classifier |
| USDM materiality validator | `tools/validators/domains/hazards/validate_usdm_materiality.py` | Synthetic domain comparison profile |
| Temporal tests | `tests/experiments/test_temporal_slice_store.py` | Eight focused test methods |
| Trace tests | `tests/validators/test_validate_trace_temporal_closure.py` | Six focused test methods |
| MapLibre tests | `tests/maplibre/test_validate_v6_readiness.py` | Fourteen focused test methods |
| USDM tests | `tests/domains/hazards/test_validate_usdm_materiality.py` | Six focused test methods |
| Trace fixtures | `fixtures/contracts/v1/data/trace_temporal_closure/` | Synthetic positive/negative closure inputs |
| MapLibre fixtures | `fixtures/maplibre/v6_readiness/` | Synthetic `READY`/`HOLD`/`ERROR` classifier inputs |
| USDM fixtures | `fixtures/domains/hazards/usdm_materiality/` | Synthetic state and invalid-case inputs |
| Workflow | `.github/workflows/briefing-implementation-campaign.yml` | Read-only/no-network focused orchestration |
| Original generated receipt | `data/receipts/generated/genrec-briefing-implementation-campaign-20260806.json` | Historical process memory for original campaign bytes |
| Current MapLibre successor receipt | `data/receipts/generated/genrec-maplibre-v6-4-readiness-current-binding-20260818.json` | Successor binding for current MapLibre readiness bytes; no upgrade authority |

The 34 current focused test methods are source inventory, not a current execution result.

[Back to top](#top)

---

<a id="trust-boundary"></a>

## Trust boundary

### 6.1 No-network and source boundary

The campaign's deterministic path uses committed synthetic inputs. The current workflow sets `KFM_NO_NETWORK=1` and read-only repository permissions. It does not contact USDM, Kansas agencies, telemetry services, a database, an OCI registry, npm for dependency admission, or another external source as part of the four fixture runners.

Dependency installation performed by CI is a toolchain step, not source activation or evidence acquisition.

### 6.2 Authority boundary

A passing campaign check cannot:

- authenticate an `EvidenceBundle`;
- activate or admit a source;
- prove a source's rights, authority, freshness, or completeness;
- decide policy, sensitivity, consent, or disclosure;
- approve human review;
- authorize repository mutation beyond the separately reviewed pull request;
- promote RAW/WORK/QUARANTINE/PROCESSED/CATALOG/PUBLISHED state;
- generate release authority;
- deploy software;
- publish KFM knowledge;
- permit public use.

### 6.3 Public-client boundary

No component creates a direct browser path to RAW, WORK, QUARANTINE, a canonical database, telemetry backend, model runtime, or unreleased artifact. A future public surface must use governed APIs or released public-safe carriers and preserve evidence, scope, time, policy, release, correction, and rollback context.

### 6.4 Sensitive and operational language

The USDM slice is a material-change classifier, not an alert system. MapLibre is a downstream renderer candidate, not a geoprivacy mechanism. Telemetry is operational process data, not evidence authority. A SQL store is infrastructure, not truth.

[Back to top](#top)

---

<a id="validation"></a>

## Validation

### 7.1 Current repository-native workflow

The current [workflow](../../.github/workflows/briefing-implementation-campaign.yml) declares this focused sequence:

```bash
python -m unittest discover --start-directory tests/experiments --pattern 'test_temporal_slice_store.py' --verbose
python -m unittest discover --start-directory tests/validators --pattern 'test_validate_trace_temporal_closure.py' --verbose
python -m unittest discover --start-directory tests/maplibre --pattern 'test_validate_v6_readiness.py' --verbose
python -m unittest discover --start-directory tests/domains/hazards --pattern 'test_validate_usdm_materiality.py' --verbose

python tools/experiments/temporal_slice_store.py --self-test
python tools/validators/validate_trace_temporal_closure.py --fixtures
python tools/validators/maplibre/validate_v6_readiness.py --fixtures
python tools/validators/domains/hazards/validate_usdm_materiality.py --fixtures
```

It then scans the current tree and requires exit code `3` plus `HOLD` for the unpinned/pending MapLibre 6.4 candidate, and validates the current MapLibre 6.4 successor receipt.

### 7.2 Validation status for this documentation update

| Check | Current result |
|---|---|
| Current target and related path inspection | `CONFIRMED` through the GitHub connector |
| Exact-target open PR search | `CONFIRMED`: none returned at preflight |
| Current issues #2957 and #2906 | `CONFIRMED` open at preflight |
| Directory Rules/ADR-0029 placement review | `CONFIRMED` |
| Full local campaign test execution at `main@4f222c5b7ef852d2f3577b2a27c146d3d3641225` | `NOT RUN` — no mounted checkout in this connector-only documentation update |
| Current exact-main hosted campaign run | `NEEDS VERIFICATION` |
| Runtime/browser/source/production validation | `NOT RUN / HOLD` |
| Documentation structure, explicit anchors, and internal-fragment validation | Required before push for this changed file |
| Hosted documentation, link, topology, security, and aggregate checks | Pending after draft pull-request creation |

Historical PR/receipt validation is retained as historical evidence only. It must not be described as a current-main run.

### 7.3 Interpretation rule

A green focused workflow proves only the checked synthetic code and fixture behavior at its exact SHA. A red check must be classified as introduced, inherited, expected hold, or external before altering this docs-only branch. No gate should be weakened merely to make a dated campaign record mergeable.

[Back to top](#top)

---

<a id="8-graduation-and-hold-register"></a>

## 8. Graduation and HOLD register

| Priority | Seam | Current state | Required evidence before graduation |
|---:|---|---|---|
| P0 | Public/release authority | `DENY / HOLD` | Evidence, rights, policy, review, release manifest, correction, rollback, and public-safe carrier closure |
| P0 | MapLibre architecture/ownership | `HOLD` | Maintainer disposition of #2957; no implicit ADR acceptance |
| P0 | MapLibre runtime evidence | `HOLD` | Exact package integrity/lock binding and all 12 probes under #2906 |
| P0 | Live USDM source | `HOLD` | Official SourceDescriptor, terms/rights, immutable snapshots, revision/correction handling, source admission |
| P1 | Production TemporalSlice store | `HOLD` | Storage decision, migrations, concurrency, durability, security, backup/restore, resolver integration |
| P1 | Live trace closure | `HOLD` | Telemetry identity, resolver, signature/attestation, freshness, safe retention, failure and rollback proof |
| P1 | USDM materiality profile | `PROPOSED / HOLD` | Domain-steward review, threshold versioning, negative cases, scale/uncertainty, correction and release integration |
| P1 | Current exact-main focused validation | `NEEDS VERIFICATION` | Exact-SHA hosted or mounted-repo results |
| P2 | Dated document migration | `HOLD` | Verified receiving lane, complete content and identity comparison, inbound links/fragments, navigation, no-loss migration, rollback |
| P2 | Accountable stewardship | `NEEDS VERIFICATION` | Named roles beyond the current CODEOWNERS routing account |

A hold is a truthful finite result. It is not permission to bypass the missing evidence and not proof that the underlying design is wrong.

[Back to top](#top)

---

<a id="9-provenance-and-receipt-lineage"></a>

## 9. Provenance and receipt lineage

### 9.1 Original campaign receipt

[`genrec-briefing-implementation-campaign-20260806.json`](../../data/receipts/generated/genrec-briefing-implementation-campaign-20260806.json) binds the original campaign's fourteen authored artifacts and original hashes. It records:

- original authorship/process memory;
- historical validation claims at the original head;
- `human_review.state: pending`;
- hosted CI as skipped at emission time;
- no policy decision, override, release, deployment, publication, or public-use authority.

It is intentionally **not** a rolling manifest. Later changes to a listed artifact do not justify rewriting the historical receipt. Successors should bind their own changed bytes and preserve lineage.

### 9.2 MapLibre successor receipt

[`genrec-maplibre-v6-4-readiness-current-binding-20260818.json`](../../data/receipts/generated/genrec-maplibre-v6-4-readiness-current-binding-20260818.json) binds the current 6.4 classifier, fixtures, tests, and workflow at its creation snapshot. It preserves prior MapLibre receipts as historical process memory and keeps dependency admission, browser evidence, ADR acceptance, review, release, deployment, and publication separate.

### 9.3 Receipt non-equivalence

```text
generated receipt
  != factual proof
  != EvidenceBundle
  != policy decision
  != human approval
  != release manifest
  != publication decision
```

The receipt lane supports audit and rollback. It does not upgrade the authority of the artifact it describes.

[Back to top](#top)

---

<a id="10-directory-rules-and-document-convergence"></a>

## 10. Directory Rules and document convergence

### 10.1 Same-path placement

Accepted [`ADR-0029`](../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the exact Directory Rules v2 bytes. Under those rules, this artifact is:

| Responsibility axis | Value |
|---|---|
| Artifact kind | Human implementation-history/architecture record |
| Authority owner | Documentation explanation |
| Lifecycle stage | Not a lifecycle data instance |
| Execution role | None |
| Scope | Cross-cutting dated campaign |
| Exposure | Public documentation; no protected payload |
| Mutability | Versioned correction |
| Retention | Repository history |

The existing `docs/architecture/` path remains a valid place for correcting the record. This change creates no new root or parallel authority.

### 10.2 Future move remains held

The [architecture convergence plan](document-convergence-plan.md) gives this page a provisional `HOLD` for migration to an existing reports/archive/history lane. Before any move:

1. verify the receiving lane and README contract;
2. inventory inbound links, fragments, registries, workflows, and generated references;
3. preserve `doc_id`, history, unique trust boundaries, and successor links;
4. distinguish durable architecture from implementation history;
5. repair navigation in the same atomic change;
6. run link, metadata, document-graph, topology, and aggregate validation;
7. record rollback and exit criteria.

This update does not choose a target path or authorize migration.

[Back to top](#top)

---

<a id="rollback"></a>

## Rollback

### 11.1 This documentation change

Before merge, rollback is closing the draft pull request and deleting the scoped feature branch when authorized. After an authorized merge, rollback is a focused revert of the documentation change and its new generated provenance receipt.

No contract, schema, fixture, validator, test, workflow, source, dependency, database, telemetry service, lifecycle instance, release, deployment, public endpoint, or publication state needs restoration because this update changes none of them.

### 11.2 Future component rollback

Any later graduation slice must define its own rollback:

- **Temporal storage:** schema/migration rollback or forward-fix, persisted identity preservation, backup/restore, and correction lineage.
- **Trace closure:** collector/exporter disable path, credential and endpoint rollback, retained audit continuity, and safe telemetry purge rules.
- **MapLibre:** exact dependency/lock rollback to the dependency-free scaffold, adapter/consumer reversal, browser artifact invalidation, and preserved historical probe receipts.
- **USDM:** source deactivation, snapshot retention, correction/supersession, catalog/map/cache invalidation, and public notice where needed.

“Revert the code” is insufficient once external or public state exists.

[Back to top](#top)

---

<a id="12-related-work"></a>

## 12. Related work

### Briefing architecture

- [`briefing-integration.md`](briefing-integration.md) — durable BriefingSignal/TemporalAuthorityEnvelope architecture and current bounded foundations.
- [`briefing-live-issue-inventory-binding.md`](briefing-live-issue-inventory-binding.md) — later read-only issue-inventory binding repair.
- [`document-convergence-plan.md`](document-convergence-plan.md) — provisional documentation disposition and migration HOLD.

### Governing boundaries

- [`docs/doctrine/directory-rules.md`](../doctrine/directory-rules.md) — adopted placement bytes through ADR-0029.
- [`ADR-0029`](../adr/ADR-0029-adopt-directory-governance-standard-v2.md) — accepted Directory Rules decision.
- [`ADR-0006`](../adr/ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md) — proposed adapter/acquisition boundary.
- [`ADR-0007`](../adr/ADR-0007%20%E2%80%94%20MapLibre%20GL%20JS%20Is%20the%20Sole%20Browser-Side%20Renderer.md) — proposed renderer-family boundary.

### Semantic contracts

- [`TemporalSlice`](../../contracts/data/temporal_slice.md)
- [`TraceReceiptLink`](../../contracts/telemetry/trace_receipt_link.md)
- [`MaterialChangeAssessment`](../../contracts/data/material_change_assessment.md)

### Current executable surfaces

- [`temporal_slice_store.py`](../../tools/experiments/temporal_slice_store.py)
- [`validate_trace_temporal_closure.py`](../../tools/validators/validate_trace_temporal_closure.py)
- [`validate_v6_readiness.py`](../../tools/validators/maplibre/validate_v6_readiness.py)
- [`validate_usdm_materiality.py`](../../tools/validators/domains/hazards/validate_usdm_materiality.py)
- [`briefing-implementation-campaign.yml`](../../.github/workflows/briefing-implementation-campaign.yml)

### Current decision/execution queues

- [#2957 — MapLibre architecture, ownership, and package boundary](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/2957)
- [#2906 — MapLibre 6.4 browser and long-session probes](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/2906)

[Back to top](#top)

---

<a id="appendix-a--change-history"></a>

## Appendix A — Change history

| Version | Date | Change |
|---|---|---|
| `v0.1.0` | 2026-08-06 | Initial bounded campaign note for TemporalSlice SQL, trace closure, MapLibre v6 readiness, and USDM materiality. |
| `v1.0-draft` | 2026-08-19 | Repository-grounded modernization: separates dated history from durable briefing architecture; records original PR/receipt lineage; updates MapLibre to exact 6.4.0 and 12 probes; maps current files/tests/workflow; adds truth, graduation, receipt, convergence, validation, and rollback boundaries. |

### Correction rule

Correct this page when current repository evidence changes a material statement, but preserve historical state as historical state. Do not silently rewrite an old receipt, convert a former validation claim into current evidence, or present a successor readiness profile as an accepted renderer decision.

---

<sub>Evidence basis: repository bytes and issue/PR records inspected against `main@4f222c5b7ef852d2f3577b2a27c146d3d3641225`, accepted ADR-0029, and the current documentation-convergence record. This page creates no source, evidence, policy, review, promotion, release, deployment, publication, or public-use authority.</sub>

**Last updated:** `2026-08-19` · **Status:** `repository-grounded / historical campaign record / graduation HOLD` · [Back to top](#top)

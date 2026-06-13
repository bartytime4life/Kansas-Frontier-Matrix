<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-roads-rail-trade-readme
title: Roads Rail Trade Domain Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <roads-rail-trade-pipeline-owner>
  - <roads-rail-trade-domain-steward>
  - <transport-contract-steward>
  - <source-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipelines/domains/roads-rail-trade/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - docs/domains/roads-rail-trade/README.md
  - docs/domains/roads-rail-trade/OBJECT_FAMILIES.md
  - docs/domains/roads-rail-trade/PIPELINE.md
  - docs/domains/roads-rail-trade/PRESERVATION_MATRIX.md
  - pipeline_specs/roads-rail-trade/
  - contracts/transport/
  - schemas/contracts/v1/transport/
  - policy/sensitivity/transport/
  - policy/domains/roads-rail-trade/
  - data/raw/roads-rail-trade/
  - data/work/roads-rail-trade/
  - data/quarantine/roads-rail-trade/
  - data/processed/roads-rail-trade/
  - data/catalog/domain/roads-rail-trade/
  - data/triplets/roads-rail-trade/
  - data/published/layers/roads-rail-trade/
  - data/registry/sources/roads-rail-trade/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/roads-rail-trade/
  - release/manifests/roads-rail-trade/
tags:
  - kfm
  - pipelines
  - domains
  - roads-rail-trade
  - transport
  - roads
  - rail
  - historic-routes
  - trade-routes
  - network-graph
  - access-restrictions
  - evidence
  - policy
  - governance
notes:
  - "This README replaces the greenfield scaffold for pipelines/domains/roads-rail-trade."
  - "Roads/Rail/Trade pipeline logic is executable implementation support only; it does not own object meaning, schemas, source descriptors, policy, lifecycle data, catalog truth, operational closures, legal route authority, or release decisions."
  - "Schema and contract homes use the transport segment while pipelines and most lifecycle/release lanes use roads-rail-trade; do not create a third slug or parallel authority without ADR/path-map/migration/rollback notes."
  - "Operational closure/restriction context, critical-infrastructure exposure, archaeology/cultural-route joins, private-property joins, and unsupported generated route narratives fail closed by default."
  - "Concrete executable behavior, source activation, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# 🛣️ Roads / Rail / Trade Routes Domain Pipeline

> Executable Roads / Rail / Trade Routes pipeline lane for converting admitted road, rail, historic-route, freight, crossing, depot, corridor, operator-status, restriction, and movement-story source material into governed candidates, quarantine records, processed records, catalog/triplet handoffs, receipts, and release-review packages — without becoming a traffic authority, legal route authority, infrastructure exposure surface, or replacement for source evidence and release governance.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-roads%20rail%20trade%20pipeline-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20logic-0a7ea4)
![slug](https://img.shields.io/badge/schema%20contract-transport%20slug-d62728)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/roads-rail-trade/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Roads / Rail / Trade Routes  
**Placement posture:** `roads-rail-trade` child lane under `pipelines/domains/`; schema and contract homes use `transport/`, so slug handling remains governed by the documented crosswalk and `OQ-RRT-01`  
**Public posture:** no direct publication; public output requires lifecycle, EvidenceBundle, source-role, rights, sensitivity, policy, catalog/triplet, release, correction, and rollback closure

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Slug posture: roads-rail-trade vs transport](#3-slug-posture-roads-rail-trade-vs-transport)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Pipeline scope](#6-pipeline-scope)
- [7. Source-family posture](#7-source-family-posture)
- [8. Lifecycle contract](#8-lifecycle-contract)
- [9. Required gates](#9-required-gates)
- [10. Sensitivity, operational-context, and network-graph posture](#10-sensitivity-operational-context-and-network-graph-posture)
- [11. Directory contract](#11-directory-contract)
- [12. Inputs and outputs](#12-inputs-and-outputs)
- [13. Minimal pipeline candidate record](#13-minimal-pipeline-candidate-record)
- [14. Dry-run, tests, fixtures, receipts, and proofs](#14-dry-run-tests-fixtures-receipts-and-proofs)
- [15. Promotion, publication, correction, and rollback](#15-promotion-publication-correction-and-rollback)
- [16. Definition of done](#16-definition-of-done)
- [17. Open questions](#17-open-questions)

---

## 1. Purpose

`pipelines/domains/roads-rail-trade/` is the executable pipeline lane for Roads / Rail / Trade Routes-domain transformations.

It supports candidate processing for:

- road segments and inherited road linework;
- historic routes, including wagon, military, mail, emigrant, stage, cattle, and trade routes;
- rail segments, depots, sidings, yards, crossings, ferries, bridges, and river crossings;
- freight corridors, movement corridors, and logistics context;
- route events such as designation, redesignation, abandonment, decommissioning, and renaming;
- operator-status and jurisdiction assertions over time;
- access restrictions, closures, seasonal limits, weight/height restrictions, and permit context;
- derived network edges and graph projections;
- movement story nodes and Focus Mode narrative handoffs;
- public-safe transportation map products after evidence, policy, and release review;
- catalog, graph, Evidence Drawer, and correction/rollback handoff packages.

This directory implements or will implement the **how** of Roads/Rail/Trade processing. It does not define object meaning, schemas, policy, source descriptors, operational traffic truth, legal route authority, lifecycle storage, catalog truth, or release approval.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/roads-rail-trade/`? | The domain docs place executable pipeline logic under `pipelines/domains/roads-rail-trade/`. | CONFIRMED documentation pattern; executable behavior NEEDS VERIFICATION |
| Why not `transport/` here? | The documented split uses `transport/` for schemas/contracts and `roads-rail-trade/` for pipelines and most other roots. | CONFIRMED doctrine split; ADR still open |
| Where do declarative specs live? | `pipeline_specs/roads-rail-trade/` or accepted spec home. | PROPOSED / NEEDS VERIFICATION |
| Where do source fetchers live? | `connectors/<source>`, not here. | CONFIRMED separation |
| Where do schemas live? | `schemas/contracts/v1/transport/`, not `schemas/contracts/v1/domains/roads-rail-trade/`, unless future ADR changes the crosswalk. | CONFIRMED slug in docs; presence NEEDS VERIFICATION |
| Where do contracts live? | `contracts/transport/`, not this pipeline lane. | CONFIRMED slug in docs; presence NEEDS VERIFICATION |
| Where does policy live? | `policy/sensitivity/transport/`, `policy/domains/roads-rail-trade/`, or accepted policy home. | PROPOSED / NEEDS VERIFICATION |
| Where do outputs live? | Lifecycle homes under `data/`, not beside pipeline code. | CONFIRMED lifecycle posture |
| Can this lane publish? | No. It may prepare candidates and release handoffs only through governed workflow. | CONFIRMED doctrine posture |
| Can this lane issue traffic or access instructions? | No. It can carry official-source context and redirects only. | CONFIRMED governance posture |

> [!IMPORTANT]
> Roads/Rail/Trade pipeline code is subordinate to source descriptors, source roles, rights, EvidenceBundle closure, temporal validity, sensitivity transforms, operator-status limits, policy decisions, release manifests, correction notices, and rollback cards. A successful run is not public release and never authorizes operational route, closure, access, or legal authority claims.

[⬆ Back to top](#top)

---

## 3. Slug posture: roads-rail-trade vs transport

This lane uses two governed segment names:

- `roads-rail-trade` for `docs/`, `pipelines/`, `pipeline_specs/`, `data/`, `release/`, tests, fixtures, and most lane-specific roots;
- `transport` for `contracts/transport/` and `schemas/contracts/v1/transport/`.

Until an ADR resolves or ratifies the split:

- do not create a third segment such as `roads-rail-trade-routes`;
- do not move schema or contract work from `transport/` into a parallel `roads-rail-trade/` schema/contract home;
- do not create duplicate source registries, policy bundles, data lanes, release lanes, or public surfaces under both names;
- record any migration with a path map, drift note, compatibility note, tests, and rollback note;
- do not let slug choice change evidence, source-role, rights, sensitivity, graph, or release semantics.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable Roads/Rail/Trade-domain processing.

Appropriate contents include:

- fixture-only dry-run entrypoints for Roads/Rail/Trade pipeline behavior;
- road-segment, rail-segment, historic-route, crossing, facility, and corridor candidate builders;
- route-event, operator-status, and access-restriction normalizers;
- movement-story and Focus Mode handoff builders that preserve citations and sensitivity state;
- network-edge and graph-projection builders, if not centralized elsewhere;
- source-role and knowledge-character validators for route evidence, administrative records, graph projections, and generated narratives;
- public-safe geometry and sensitivity transform helpers, if not centralized elsewhere;
- quarantine routing helpers for sensitive, unresolved, stale, over-precise, or operationally risky material;
- catalog/triplet handoff helpers, if not centralized in `pipelines/catalog/`;
- receipt emitters, if not shared;
- thin adapters that read governed lifecycle inputs, not live source systems.

A good placement test:

> If the code transforms Roads/Rail/Trade lifecycle inputs into candidates, processed records, graph/catal­og handoffs, receipts, or review handoffs, it may belong here. If it fetches source data, defines meaning, defines schema, encodes policy, stores lifecycle data, approves release, or issues route/traffic instructions, it belongs somewhere else — or nowhere in KFM.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Source fetchers / connectors | `connectors/<source>` |
| Source catalog profiles | `docs/sources/catalog/...` |
| Source descriptors / source registry entries | `data/registry/sources/roads-rail-trade/` or approved registry home |
| Roads/Rail/Trade architecture / doctrine | `docs/domains/roads-rail-trade/...` |
| Object meaning contracts | `contracts/transport/` |
| JSON Schemas | `schemas/contracts/v1/transport/` |
| Policy bundles, sensitivity rules, release rules | `policy/sensitivity/transport/`, `policy/domains/roads-rail-trade/`, `policy/rights/`, `policy/release/` |
| Declarative run specs | `pipeline_specs/roads-rail-trade/...` |
| Fixtures | `fixtures/domains/roads-rail-trade/` or accepted fixture home |
| Tests | `tests/pipelines/domains/roads-rail-trade/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Receipts and proofs | `data/receipts/...`, `data/proofs/...` |
| Release decisions | `release/candidates/roads-rail-trade/`, `release/manifests/roads-rail-trade/`, `release/rollback_cards/`, `release/correction_notices/` |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Emergency route instructions, traffic control, dispatch, evacuation routing, or official operational closure authority | Outside this executable pipeline lane; redirect to official authorities |
| Archaeological site identity, water evidence, hazard event authority, living-person/land-ownership claims, or settlement/infrastructure canonical truth | Owning domain lanes only |

> [!WARNING]
> The previous scaffold wording allowed “docs, contracts, schemas, policies, fixtures, tests, packages, pipelines, registries, or data lifecycle artifacts” here. This README narrows the boundary: **only executable Roads/Rail/Trade pipeline logic belongs here.** The other responsibility roots remain separate authority surfaces.

[⬆ Back to top](#top)

---

## 6. Pipeline scope

Roads/Rail/Trade pipeline work may include these governed processing responsibilities:

| Scope area | Pipeline responsibility | Publication posture |
|---|---|---|
| Road segments | Normalize segment evidence, lineage, source role, and temporal validity. | Public only when source role, scale, and evidence close. |
| Historic routes | Normalize corridor claims, confidence, and source evidence. | Interpretive and sensitivity-aware; not exact archaeological truth. |
| Rail segments and facilities | Normalize rail alignments, depots, sidings, yards, crossings, and operator context. | Infrastructure sensitivity and status reviewed. |
| Bridges, ferries, river crossings | Normalize crossing evidence without claiming hydrology ownership. | Hydrology owns water evidence. |
| Route events | Normalize designations, redesignations, abandonment, decommissioning, and renaming. | Event time, source time, and valid time stay distinct. |
| Operator status | Preserve operator/jurisdiction assertion over time. | Not legal authority unless source role supports it. |
| Access restrictions | Normalize restrictions and source metadata. | Not operational instruction unless official-source and release rules close. |
| Freight/trade corridors | Build corridor candidates and uncertainty notes. | Derived; needs method and evidence. |
| Network edges | Build graph projections. | Projection only; does not replace canonical evidence. |
| Movement story nodes | Prepare narrative + route + evidence handoffs. | Generated prose is downstream carrier, not truth. |
| Catalog/triplet handoff | Prepare restricted or public-safe catalog/graph candidates after evidence closure. | Does not replace canonical review state. |

[⬆ Back to top](#top)

---

## 7. Source-family posture

Roads/Rail/Trade pipeline code may consume only admitted or fixture-bound source material.

Candidate source families may include, subject to source descriptors, rights, freshness, and steward review:

- state, county, municipal, railroad, or transportation network records;
- historic maps, plats, atlases, postal, military, emigrant, cattle, trade, and wagon-road references;
- rail timetable, depot, siding, yard, crossing, and operator records;
- bridge, ferry, crossing, route-event, closure, restriction, and jurisdiction records;
- freight, logistics, and corridor context;
- hydrology, settlements/infrastructure, hazards, archaeology, people/land, agriculture, geology, and spatial foundation context through governed joins;
- local upload or steward-curated material only through source-descriptor, rights, sensitivity, and review gates.

This README does not activate any source. Each source family requires SourceDescriptor coverage, source role, rights posture, sensitivity classification, attribution, fixtures, validation, and review routing before use.

[⬆ Back to top](#top)

---

## 8. Lifecycle contract

Every Roads/Rail/Trade pipeline must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal Roads/Rail/Trade pipeline stance:

1. **Read** approved fixtures, immutable raw captures, work candidates, quarantine inputs in remediation mode, or prior processed baselines.
2. **Normalize** into work candidates with source role, rights, temporal scope, spatial scope, scale, confidence, operator/status posture, graph-projection posture, evidence references, and public-safe geometry handling.
3. **Quarantine** unresolved rights, source-role mismatch, schema drift, sensitivity risk, operational-status ambiguity, over-precise infrastructure exposure, cultural-route risk, stale restriction context, or validation failure.
4. **Promote to processed** only after validation, policy, evidence, sensitivity/public-safe transform, review, and reviewer gates appropriate to significance.
5. **Prepare catalog/triplet handoffs** only after processed-state and evidence closure, and only with sensitivity-safe payloads.
6. **Publish** only through release decisions, public-safe artifacts, rollback targets, and correction paths.

Do not treat a move from one lifecycle folder to another as promotion. Promotion is a governed state transition with receipts and review evidence.

[⬆ Back to top](#top)

---

## 9. Required gates

Every Roads/Rail/Trade pipeline run must check or explicitly fail closed on:

1. **Source descriptor gate** — every input has stable source identity, role, cadence, rights, and sensitivity posture.
2. **Source-role gate** — historical, administrative, observed, modeled, operational, aggregate, candidate, graph, and generated records are not silently collapsed.
3. **Slug gate** — schema/contract work uses `transport/`; executable/lifecycle/release lane uses `roads-rail-trade/` unless ADR says otherwise.
4. **Rights gate** — unknown or restrictive license, permission, attribution, privacy, or redistribution terms block public release.
5. **Operational-status gate** — closures, access restrictions, operator status, and restrictions remain source-bound and time-bound; KFM does not issue instructions.
6. **Network-graph gate** — network edges are projections, not source truth, and must preserve provenance and method.
7. **Historic-route gate** — interpretive route candidates preserve uncertainty and do not become confirmed exact corridors without evidence and review.
8. **Cross-lane ownership gate** — settlements, infrastructure, hydrology, archaeology, hazards, and People/Land truths remain owned by their lanes.
9. **Sensitivity gate** — critical-infrastructure exposure, culturally sensitive routes, archaeological joins, private-property joins, and security-relevant context fail closed.
10. **Public-safe geometry gate** — public products require approved generalization, redaction, aggregation, delay, restriction, or denial decisions with receipts.
11. **Scale and uncertainty gate** — method, confidence, uncertainty, spatial resolution, and source vintage are recorded.
12. **Review gate** — required steward or domain review state is recorded before promotion beyond candidate or quarantine where applicable.
13. **Schema gate** — candidate and processed records match approved schemas.
14. **Contract gate** — object meanings match Transport contracts and do not invent new semantics silently.
15. **Evidence gate** — claim-bearing outputs resolve EvidenceBundle support or abstain.
16. **Temporal gate** — source, event, valid, operational, retrieval, processing, catalog, and release times remain distinct.
17. **Spatial gate** — CRS, geometry precision, route interpolation, graph projection method, and public-safe transforms are recorded.
18. **Policy gate** — policy decisions are finite and recorded; no silent allow.
19. **Validation gate** — validators exercise pass, fail, restrict, abstain, deny, and error paths, not only success.
20. **Receipt gate** — every run records input refs, versions, parameters, transforms, hashes, output refs, and outcomes.
21. **No-direct-publish gate** — no writes to public UI, public API, or `data/published/` without release workflow authority.
22. **Catalog/triplet gate** — catalog and graph projections preserve provenance and do not replace canonical records or review state.
23. **Release gate** — public release requires ReleaseManifest, rollback target, correction path, and review state.

[⬆ Back to top](#top)

---

## 10. Sensitivity, operational-context, and network-graph posture

Roads/Rail/Trade is fail-closed where output could expose critical infrastructure, imply current operational status, reveal culturally or archaeologically sensitive corridors, or overinterpret graph projections.

Default posture:

- route candidates are evidence-bound, not guaranteed route truth;
- network edges are graph projections, not canonical source truth;
- historic-route candidates preserve uncertainty, source role, and review state;
- closures and access restrictions are source-bound context, not KFM instructions;
- public products must preserve source role, scale, method, uncertainty, time basis, and EvidenceBundle support;
- sensitive exact geometry and high-risk joins are generalized, redacted, delayed, restricted, aggregated, or withheld where needed;
- generated route narratives cannot replace source evidence, movement-story provenance, policy, or release state;
- outputs that could imply unsupported access rights, legal route status, operator authority, evacuation guidance, infrastructure vulnerability, archaeological exposure, or private land access must abstain, deny, quarantine, or require reviewer handoff.

[⬆ Back to top](#top)

---

## 11. Directory contract

Recommended shape:

```text
pipelines/domains/roads-rail-trade/
├── README.md                         # this file
├── PIPELINE_CONTRACT.md              # PROPOSED: Roads/Rail/Trade execution contract
├── run_dry_fixture.py                # PROPOSED if repo Python convention is accepted
├── normalize_road_segment.py         # PROPOSED
├── normalize_rail_segment.py         # PROPOSED
├── normalize_historic_route.py       # PROPOSED
├── normalize_crossing.py             # PROPOSED
├── normalize_route_event.py          # PROPOSED
├── normalize_operator_status.py      # PROPOSED
├── normalize_access_restriction.py   # PROPOSED
├── build_network_edge.py             # PROPOSED
├── build_movement_story_node.py      # PROPOSED
├── validate_source_role_anticollapse.py # PROPOSED
├── validate_operational_status.py    # PROPOSED
├── apply_public_safe_geometry.py     # PROPOSED; may belong in shared tools if reused
├── build_catalog_handoff.py          # PROPOSED if not centralized in pipelines/catalog/
├── validate_roads_rail_trade_candidate.py # PROPOSED wrapper if not centralized in tools/
├── emit_receipt.py                   # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/roads-rail-trade/
├── README.md                         # PROPOSED / NEEDS VERIFICATION
├── road_segment_dry_run.yaml         # PROPOSED
├── rail_segment_dry_run.yaml         # PROPOSED
├── historic_route_dry_run.yaml       # PROPOSED
├── network_edge_build.yaml           # PROPOSED
├── movement_story_handoff.yaml       # PROPOSED
├── public_safe_geometry.yaml         # PROPOSED; policy ownership must be resolved
└── catalog_handoff.yaml              # PROPOSED
```

Generated outputs must not be written beside the code that generated them. Use lifecycle homes under `data/`, proof homes under `data/proofs/`, receipt homes under `data/receipts/`, and release homes under `release/`.

[⬆ Back to top](#top)

---

## 12. Inputs and outputs

### Inputs

| Input class | Allowed source | Required condition |
|---|---|---|
| No-network fixture | `fixtures/domains/roads-rail-trade/` or accepted fixture home | Synthetic, generalized, stale-marked, or redacted where needed. |
| Raw transport capture | `data/raw/roads-rail-trade/<source_id>/<run_id>/` | Immutable source-edge capture with source descriptor, checksums, and ingest receipt. |
| Work candidate | `data/work/roads-rail-trade/<run_id>/` | Candidate-only; not public. |
| Quarantine input | `data/quarantine/roads-rail-trade/<reason>/<run_id>/` | Audit/remediation mode only. |
| Prior processed baseline | `data/processed/roads-rail-trade/<dataset_id>/<version>/` | Validated restricted baseline for diff/supersession. |
| Source registry / descriptor | `data/registry/sources/roads-rail-trade/`, `docs/sources/catalog/...` | Source role, rights, cadence, attribution, sensitivity. |
| Cross-lane context | Settlements/Infrastructure, Hydrology, Hazards, Archaeology, People/Land, Agriculture, Geology, Spatial Foundation, or other lifecycle homes | Must preserve source role and domain ownership. |
| Transport schema / contract refs | `schemas/contracts/v1/transport/`, `contracts/transport/` | Referenced by validators, not stored here. |
| Policy refs | `policy/sensitivity/transport/`, `policy/domains/roads-rail-trade/`, `policy/rights/`, `policy/release/` | Referenced by validators, not stored here. |

### Outputs

| Output class | Correct home | Notes |
|---|---|---|
| Roads/Rail/Trade work candidate | `data/work/roads-rail-trade/<run_id>/` | Candidate only. |
| Roads/Rail/Trade quarantine record | `data/quarantine/roads-rail-trade/<reason>/<run_id>/` | Failed, restricted, stale, unresolved, or unsafe material. |
| Processed dataset version | `data/processed/roads-rail-trade/<dataset_id>/<version>/` | Validated/restricted; not automatically public. |
| Public-safe catalog candidate | `data/catalog/domain/roads-rail-trade/...` or approved catalog home | After processed-state, transform, and evidence gates. |
| Triplet / graph delta | `data/triplets/roads-rail-trade/...` or approved graph-delta home | Projection; does not replace canonical truth or review state. |
| Network / public-safe geometry / source-role receipt | `data/receipts/...` or approved receipt/proof home | Required for graph and public-safe derivatives. |
| Run receipt | `data/receipts/pipeline/...` | Process memory, not release proof. |
| Evidence / validation proof | `data/proofs/...` | EvidenceBundle, validation reports, proof packs. |
| Release handoff | `release/candidates/roads-rail-trade/...` | Only through release workflow. |

[⬆ Back to top](#top)

---

## 13. Minimal pipeline candidate record

The final schema is not defined here. This example shows the minimum information a Roads/Rail/Trade pipeline candidate should preserve.

```yaml
schema_version: kfm.roads_rail_trade_pipeline_candidate.v1
candidate_id: rrt_<object_family>_<run_id>_<hash>
pipeline_id: domains.roads-rail-trade
schema_contract_segment: transport
run_id: run_YYYYMMDDThhmmssZ
status: WORK_CANDIDATE
object_family: <road_segment|historic_route|rail_segment|depot|siding|yard|crossing|bridge|ferry|river_crossing|freight_corridor|route_event|operator_status|access_restriction|network_edge|movement_story_node>
source_inputs:
  - source_id: src_transport_example
    source_role: <historical|administrative|observed|modeled|operational|aggregate|candidate|graph|synthetic|restricted>
    lifecycle_ref: data/raw/roads-rail-trade/<source_id>/<run_id>/
    input_hash: sha256:<hash>
    rights_state: needs_review
anti_collapse:
  network_edge_is_source_truth: false
  historic_route_candidate_is_confirmed_corridor: false
  operational_context_is_kfm_instruction: false
  generated_story_is_evidence: false
spatial_scope:
  geometry_ref: restricted_or_public_safe_ref
  public_precision: denied_until_public_safe_transform
temporal_scope:
  source_time: null
  event_time: null
  valid_start: null
  valid_end: null
  operational_valid_until: null
  retrieved_at: YYYY-MM-DDThh:mm:ssZ
  processed_at: YYYY-MM-DDThh:mm:ssZ
method:
  transform_family: roads_rail_trade_candidate_normalization
  algorithm_version: <version>
  parameter_hash: sha256:<hash>
scale_and_uncertainty:
  source_scale: unknown
  confidence: needs_review
  limitations:
    - candidate_only
sensitivity:
  infrastructure_exposure_risk: needs_review
  cultural_route_risk: needs_review
  archaeology_join_risk: needs_review
  private_property_join_risk: needs_review
  public_release_default: DENY_UNTIL_REVIEW
policy:
  outcome: ABSTAIN
  reason_code: SOURCE_ROLE_RIGHTS_OR_EVIDENCE_NOT_RESOLVED
evidence:
  evidence_bundle_ref: null
  citation_state: ABSTAIN
outputs:
  candidate_record: data/work/roads-rail-trade/run_YYYYMMDDThhmmssZ/candidate.yml
  receipt: data/receipts/pipeline/roads-rail-trade/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 14. Dry-run, tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/generalized/stale-marked/redacted, and no-network** until source activation, rights review, operational-context review, sensitivity review, slug-path review, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/roads-rail-trade/
├── test_no_network_dry_run.py                 # PROPOSED
├── test_transport_slug_for_schema_contract.py # PROPOSED
├── test_no_third_slug.py                      # PROPOSED
├── test_source_role_required.py               # PROPOSED
├── test_rights_unknown_denied.py              # PROPOSED
├── test_network_edge_not_source_truth.py      # PROPOSED
├── test_historic_route_candidate_not_confirmed.py # PROPOSED
├── test_operational_context_not_instruction.py # PROPOSED
├── test_sensitive_join_quarantines.py         # PROPOSED
├── test_missing_evidence_abstains.py          # PROPOSED
├── test_receipt_hashes.py                     # PROPOSED
└── test_no_direct_publish.py                  # PROPOSED
```

A dry run should prove:

- fixtures load without network access;
- every input has source identity and source role;
- schema/contract checks reference `transport/` while pipeline/lifecycle outputs use `roads-rail-trade/`;
- unknown rights produce `ABSTAIN`, `DENY`, or quarantine;
- network edges remain graph projections;
- historic route candidates remain candidates unless evidence and review close;
- operational closure or restriction context is not emitted as KFM instruction;
- sensitive or over-precise geometry is withheld from public-safe outputs;
- missing EvidenceBundle support produces `ABSTAIN`;
- invalid records fail validation;
- receipts include input hashes, method hashes, transform refs, graph refs, output refs, and outcomes;
- no outputs are written to public UI, public API, `data/published/`, or release manifests by default.

[⬆ Back to top](#top)

---

## 15. Promotion, publication, correction, and rollback

Roads/Rail/Trade pipelines may prepare candidates. They do not publish.

Required promotion chain:

```text
roads / rail / trade source or work input
  -> roads / rail / trade candidate
  -> validation report
  -> policy decision
  -> source-role / graph / public-safe transform receipt where required
  -> EvidenceBundle closure
  -> processed roads-rail-trade dataset version
  -> catalog / triplet candidate
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public-safe artifact
```

Correction and rollback posture:

- denied, abstained, errored, stale, restricted, and quarantined runs remain auditable;
- candidate rollback preserves receipts and proof state;
- processed versions are superseded by governed state transition, not hidden overwrite;
- graph projections are invalidated if source refs, method refs, topology, or policy refs drift;
- public artifact rollback is owned by `release/`, not by this directory;
- correction notices must point back to source, evidence, source-role checks, graph transforms, validation, catalog, release, and rollback state.

[⬆ Back to top](#top)

---

## 16. Definition of done

This README is done when it:

- replaces the greenfield scaffold with a usable Roads/Rail/Trade pipeline contract;
- identifies this directory as executable pipeline logic only;
- preserves the documented `roads-rail-trade` / `transport` slug split without creating a third authority;
- corrects the boundary so docs, schemas, contracts, policy, fixtures, tests, data, registries, receipts, proofs, and release decisions do not live here;
- preserves source-role, operational-context, historic-route, graph-projection, evidence, policy, lifecycle, catalog/triplet, release, correction, and rollback boundaries;
- denies direct publication and traffic/access-instruction behavior;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable Roads/Rail/Trade pipeline implementation is done only when it has:

- owners and review burden;
- source-descriptor coverage;
- synthetic/generalized/stale-marked/redacted no-network fixtures;
- schema-backed candidates through `schemas/contracts/v1/transport/`;
- contract conformance through `contracts/transport/`;
- rights, sensitivity, source-role, operational-status, temporal, spatial, network-graph, and evidence tests;
- deterministic receipts;
- no-direct-publish tests;
- CI coverage;
- steward-review handoff;
- release, correction, and rollback documentation.

[⬆ Back to top](#top)

---

## 17. Open questions

| ID | Question | Status |
|---|---|---|
| `RRT-PIPE-001` | Which child modules should be implemented first: roads, rail, historic routes, route events, access restrictions, graph edges, or catalog handoff? | NEEDS VERIFICATION |
| `RRT-PIPE-002` | Should an ADR ratify the `roads-rail-trade` / `transport` split or unify the slug? | NEEDS VERIFICATION / ADR |
| `RRT-PIPE-003` | Which object family owns network-edge, movement-story, and public-safe geometry receipts if reusable outside this lane? | PROPOSED / NEEDS ADR |
| `RRT-PIPE-004` | Which source descriptors are first-wave approved for fixture-only dry runs? | NEEDS VERIFICATION |
| `RRT-PIPE-005` | Which CI job owns Roads/Rail/Trade pipeline invariant tests? | UNKNOWN |
| `RRT-PIPE-006` | Should catalog handoff logic live here or in centralized `pipelines/catalog/` with Roads/Rail/Trade adapters? | NEEDS VERIFICATION |
| `RRT-PIPE-007` | Which public-safe map/API products are allowed after review and release, and at what freshness/generalization level? | NEEDS VERIFICATION |
| `RRT-PIPE-008` | How should cross-lane joins with Settlements, Infrastructure, Hydrology, Hazards, Archaeology, People/Land, Agriculture, Geology, or Spatial Foundation be denied, restricted, or generalized? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic/generalized/stale-marked fixture-only dry runs and negative tests. Do not add live source fetching, public current-route instructions, official closure behavior, public infrastructure-exposure products, sensitive historic-route precision, archaeological exposure joins, release handoff automation, or direct API payload generation until source roles, rights, source-role anti-collapse, public-safe transforms, graph provenance, evidence closure, and rollback are proven.

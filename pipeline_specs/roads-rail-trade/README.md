<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-roads-rail-trade-readme
title: Roads Rail Trade Pipeline Specs README
type: readme
version: v0.1
status: draft
owners:
  - <pipeline-spec-steward>
  - <roads-rail-trade-domain-steward>
  - <transport-contract-steward>
  - <pipeline-owner>
  - <evidence-steward>
  - <policy-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipeline_specs/roads-rail-trade/README.md
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - pipeline_specs/README.md
  - pipelines/README.md
  - pipelines/domains/roads-rail-trade/README.md
  - docs/domains/roads-rail-trade/README.md
  - docs/domains/roads-rail-trade/OBJECT_FAMILIES.md
  - docs/domains/roads-rail-trade/PIPELINE.md
  - docs/domains/roads-rail-trade/PRESERVATION_MATRIX.md
  - contracts/transport/
  - schemas/contracts/v1/transport/
  - data/registry/sources/roads-rail-trade/
  - data/receipts/pipeline/roads-rail-trade/
  - data/proofs/evidence_bundle/
  - tests/pipeline_specs/roads-rail-trade/
  - fixtures/pipeline_specs/roads-rail-trade/
tags: [kfm, pipeline-specs, roads-rail-trade, transport, roads, rail, historic-routes, trade-routes, network-graph, access-restrictions, declarative-config, receipts, governance]
notes:
  - "This README replaces the short pipeline_specs/roads-rail-trade stub with a governed declarative-spec lane contract."
  - "pipeline_specs/ is declarative configuration — the what. pipelines/ is executable logic — the how."
  - "Roads/Rail/Trade specs configure pipeline intent, source scope, lifecycle gates, temporal and source-role checks, network-graph posture, operational-context boundaries, evidence gates, receipts, and release blockers. They do not execute pipeline logic or store lifecycle outputs."
  - "Schemas and contracts use the transport segment while most lane roots use roads-rail-trade; do not create a third slug or parallel authority without ADR/path-map/migration/rollback notes."
  - "Operational closures, legal route authority, access instructions, critical-infrastructure exposure, archaeology/cultural-route joins, private-property joins, and unsupported generated route narratives fail closed by default."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Roads / Rail / Trade Pipeline Specs

> Declarative configuration lane for Roads / Rail / Trade Routes pipeline profiles, source scopes, schedules, lifecycle gates, source-role and temporal checks, network-graph posture, operational-context boundaries, evidence requirements, fixtures, receipts, and release-readiness intent — separate from executable Roads/Rail/Trade pipeline logic.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipeline__specs%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-declarative%20config-0a7ea4)
![implementation](https://img.shields.io/badge/implementation-pipelines%2Fdomains%2Froads--rail--trade%2F-d62728)
![slug](https://img.shields.io/badge/schema%20contract-transport%20slug-d62728)

**Status:** Draft  
**Path:** `pipeline_specs/roads-rail-trade/README.md`  
**Responsibility root:** `pipeline_specs/` — declarative pipeline configuration, the **what**  
**Companion implementation lane:** `pipelines/domains/roads-rail-trade/` — executable pipeline logic, the **how**  
**Schema/contract slug posture:** schemas and contracts use `transport/`; this lane uses `roads-rail-trade/` for specs, docs, pipelines, data, tests, fixtures, and release unless an ADR changes the crosswalk.  
**Public posture:** no public release, data storage, legal route authority, access instruction, traffic authority, or executable side effect; specs only configure governed pipeline runs.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Slug posture](#3-slug-posture)
- [4. Spec anti-collapse rules](#4-spec-anti-collapse-rules)
- [5. What belongs here](#5-what-belongs-here)
- [6. What does not belong here](#6-what-does-not-belong-here)
- [7. Roads/Rail/Trade spec scope](#7-roadsrailtrade-spec-scope)
- [8. Lifecycle posture](#8-lifecycle-posture)
- [9. Required gates](#9-required-gates)
- [10. Directory contract](#10-directory-contract)
- [11. Spec profile families](#11-spec-profile-families)
- [12. Inputs and outputs](#12-inputs-and-outputs)
- [13. Minimal spec profile shape](#13-minimal-spec-profile-shape)
- [14. Tests, fixtures, and validation](#14-tests-fixtures-and-validation)
- [15. Definition of done](#15-definition-of-done)
- [16. Open questions](#16-open-questions)

---

## 1. Purpose

`pipeline_specs/roads-rail-trade/` owns declarative Roads / Rail / Trade Routes pipeline configuration.

It may describe:

- which Roads/Rail/Trade pipeline profile should run;
- which source descriptor ids are in scope;
- which source-family, cadence, source-vintage, route-event, operator-status, restriction, and temporal-validity checks apply;
- which lifecycle gates are required;
- which network-graph, historical-route, operational-context, infrastructure-exposure, rights, and public-safe representation requirements apply;
- which fixtures support no-network tests;
- which receipts, reports, blockers, and review handoffs are expected;
- which downstream implementation lane is authorized to execute the spec.

It does **not** implement pipeline behavior. Roads/Rail/Trade implementation belongs under `pipelines/domains/roads-rail-trade/` and related executable lanes.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipeline_specs/`? | This root owns declarative pipeline configuration, separate from implementation. | CONFIRMED root contract |
| Why `roads-rail-trade/`? | Domain docs use this lane segment for docs, pipelines, specs, data, tests, fixtures, and release. | CONFIRMED docs posture / NEEDS VERIFICATION for active specs |
| What about `transport/`? | Transport is the documented schema/contract segment. | CONFIRMED docs posture / ADR still open |
| Does this execute pipelines? | No. Execution belongs under `pipelines/`. | CONFIRMED separation |
| Does this define transport object meaning? | No. Object meaning belongs under contracts/domain doctrine. | CONFIRMED authority separation |
| Does this store data or receipts? | No. Lifecycle data and receipts belong under `data/`. | CONFIRMED lifecycle posture |
| Can this approve closures, access, legal route authority, or release? | No. Specs can require gates only; operational/legal/release authority remains separate. | CONFIRMED boundary posture |

> [!IMPORTANT]
> A pipeline spec says what should run and under which constraints. It is not a run, not a receipt, not evidence, not processed data, not traffic authority, not legal route authority, not a closure/access instruction, not catalog truth, and not release approval.

[⬆ Back to top](#top)

---

## 3. Slug posture

This lane intentionally carries two governed segment names:

- `roads-rail-trade` for `docs/`, `pipelines/`, `pipeline_specs/`, `data/`, `release/`, tests, fixtures, and most lane-specific roots;
- `transport` for `contracts/transport/` and `schemas/contracts/v1/transport/`.

Until an ADR ratifies or changes this split:

- do not create a third segment such as `roads-rail-trade-routes`;
- do not move schema or contract work into a parallel `roads-rail-trade/` schema/contract home;
- do not duplicate source registries, policies, data lanes, release lanes, or public surfaces under both names;
- record any migration with a path map, drift note, compatibility note, tests, and rollback note;
- keep evidence, source-role, rights, sensitivity, network-graph, and release semantics unchanged by slug choice.

[⬆ Back to top](#top)

---

## 4. Spec anti-collapse rules

Disallowed collapses:

```text
spec file -> executable pipeline
spec profile -> release approval
source list -> source authority
schedule -> source freshness proof
road linework -> legal road authority
rail alignment -> active operator status
historic route corridor -> exact route certainty
restriction context -> access instruction
network edge -> public routing instruction
movement story -> evidence
movement story -> catalog truth
generated route narrative -> evidence
```

Required separations:

- declarative specs stay in `pipeline_specs/`;
- executable logic stays in `pipelines/`;
- source descriptors stay in the source registry;
- lifecycle data stays in `data/`;
- receipts and proofs stay in their receipt/proof homes;
- contracts and schemas use the governed `transport/` segment unless ADR changes it;
- policy, review, and release decisions stay in their authority roots;
- road segment, rail segment, historic route, trade corridor, facility, operator-status, jurisdiction, restriction, bridge/crossing, graph edge, and movement-story objects remain separately labeled.

[⬆ Back to top](#top)

---

## 5. What belongs here

Appropriate contents include declarative specs for:

- source-intake profiles;
- normalization profiles;
- validation profiles;
- catalog and triplet profiles;
- publish-readiness profiles;
- rollback-readiness profiles;
- watcher profiles;
- proof or dry-run profiles;
- road, rail, historic-route, trade-route, crossing, bridge, ferry, depot, siding, yard, freight-corridor, operator-status, jurisdiction, restriction, network-graph, and public-safe map-product variants.

A good placement test:

> If the file answers “what Roads/Rail/Trade pipeline should run, with what source scope, temporal gates, operator-status limits, network-graph posture, and release blockers?”, it may belong here. If it answers “how does the pipeline execute?”, it belongs under `pipelines/`.

[⬆ Back to top](#top)

---

## 6. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Executable Roads/Rail/Trade pipeline code | `pipelines/domains/roads-rail-trade/` |
| Shared executable helpers | `pipelines/<lane>/` or accepted package/tool home |
| Source connectors | `connectors/<source>` |
| Source descriptors | `data/registry/sources/roads-rail-trade/` or accepted registry home |
| Object meaning | `contracts/transport/` and domain doctrine |
| JSON Schemas | `schemas/contracts/v1/transport/` |
| Policy and review decisions | `policy/domains/roads-rail-trade/`, `policy/sensitivity/transport/`, review roots |
| Tests | `tests/pipeline_specs/roads-rail-trade/` or accepted test home |
| Fixtures | `fixtures/pipeline_specs/roads-rail-trade/` or accepted fixture home |
| Lifecycle data | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Release decisions/manifests/corrections/rollback cards | `release/` |
| Public API/UI code | `apps/governed-api/`, `apps/explorer-web/`, packages |

[⬆ Back to top](#top)

---

## 7. Roads/Rail/Trade spec scope

Roads/Rail/Trade specs may configure profiles for object families and candidate products such as:

- Road Segment and inherited road linework;
- Historic Route, trade route, stage route, cattle route, military route, emigrant route, mail route, and wagon route candidates;
- Rail Segment, depot, siding, yard, crossing, bridge, ferry, and river crossing records;
- freight corridors, movement corridors, and logistics context;
- route events including designation, redesignation, abandonment, decommissioning, and renaming;
- operator-status and jurisdiction assertions over time;
- access restrictions, closure context, seasonal limits, height/weight restrictions, and permit context;
- derived network edges and graph projections;
- movement story nodes and public-safe narrative handoffs;
- release-reviewed map products and public-safe derivatives.

This lane may cite other domains for context, including Settlements, Hydrology, Hazards, Archaeology, Agriculture, People/DNA/Land, and Spatial Foundation, but those contexts must not weaken source-role, rights, infrastructure-sensitivity, archaeology/cultural, private-property, or release controls.

[⬆ Back to top](#top)

---

## 8. Lifecycle posture

Specs may target lifecycle stages, but do not create lifecycle transitions themselves:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A spec may declare input lifecycle state, expected output lifecycle state, source descriptor refs, source-role labels, temporal-validity checks, operator-status posture, access/closure context handling, EvidenceBundle requirements, receipt requirements, release blockers, rollback support, and correction support.

Only governed pipeline implementation and release authority can perform transitions.

[⬆ Back to top](#top)

---

## 9. Required gates

Every Roads/Rail/Trade spec should declare or explicitly mark not applicable:

1. **Profile identity gate** — stable `spec_id`, owner, domain, lane, and version.
2. **Implementation gate** — target executable lane under `pipelines/`.
3. **Source gate** — source descriptor refs and source roles.
4. **Temporal gate** — valid time, source time, route-event time, operator-status time, retrieval time, processing time, and stale-source behavior.
5. **Lifecycle gate** — allowed input and output lifecycle states.
6. **Slug gate** — `roads-rail-trade` lane references remain distinct from `transport` schema/contract references.
7. **Operational-context gate** — closure, restriction, access, and permit context are not public instructions.
8. **Network-graph gate** — graph edges and routing derivatives cannot become legal or operational routing authority.
9. **Evidence gate** — EvidenceRef/EvidenceBundle requirements for claims.
10. **Receipt gate** — required run, transform, validation, temporal, graph, sensitivity, source-vintage, or release-readiness receipts.
11. **Release gate** — ReleaseManifest input requirements, rollback target, and correction path where output can publish.

[⬆ Back to top](#top)

---

## 10. Directory contract

Recommended shape:

```text
pipeline_specs/roads-rail-trade/
├── README.md
├── ingest.yaml                  # PROPOSED
├── normalize.yaml               # PROPOSED
├── validate.yaml                # PROPOSED
├── catalog.yaml                 # PROPOSED
├── triplets.yaml                # PROPOSED
├── publish.yaml                 # PROPOSED
├── rollback.yaml                # PROPOSED
├── watchers.yaml                # PROPOSED
├── roads.yaml                   # PROPOSED
├── rail.yaml                    # PROPOSED
├── historic_routes.yaml         # PROPOSED
├── trade_routes.yaml            # PROPOSED
├── crossings_facilities.yaml    # PROPOSED
├── restrictions_context.yaml    # PROPOSED
└── network_graph.yaml           # PROPOSED
```

These filenames are proposed placeholders until actual spec files, schema validation, CI coverage, and ADR/path resolution are implemented.

[⬆ Back to top](#top)

---

## 11. Spec profile families

| Profile family | Purpose | Implementation lane |
|---|---|---|
| `ingest` | Declare source intake scope and prerequisites. | `pipelines/domains/roads-rail-trade/` or shared ingest lane |
| `normalize` | Declare transform profile, expected receipts, and blockers. | Roads/Rail/Trade normalize implementation |
| `validate` | Declare source-role, temporal, slug, graph, and operational-context checks. | Roads/Rail/Trade validate implementation |
| `catalog` | Declare catalog closure requirements. | Roads/Rail/Trade catalog implementation |
| `triplets` | Declare graph/triplet projection profile. | Roads/Rail/Trade triplet implementation |
| `publish` | Declare release-candidate readiness checks. | Roads/Rail/Trade publish support |
| `rollback` | Declare rollback-readiness check profile. | Roads/Rail/Trade rollback support |
| `watchers` | Declare source-change observation profiles. | Roads/Rail/Trade watcher support |
| `object-family` | Declare road, rail, historic-route, trade-route, facility, restriction, and network-graph variants. | Domain sublane implementations |

[⬆ Back to top](#top)

---

## 12. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Spec file | `pipeline_specs/roads-rail-trade/` | Declarative config only. |
| Executable target | `pipelines/domains/roads-rail-trade/` or accepted pipeline lane | The spec references it; it does not implement it. |
| Source descriptor | `data/registry/sources/roads-rail-trade/` | Stable source ref. |
| Fixture | `fixtures/pipeline_specs/roads-rail-trade/` or accepted fixture home | Supports no-network validation. |
| Spec validation test | `tests/pipeline_specs/roads-rail-trade/` | Verifies shape, slug boundaries, and anti-collapse gates. |
| Runtime output | `data/` lifecycle homes | Never beside the spec. |
| Receipts | `data/receipts/pipeline/roads-rail-trade/` or accepted receipt home | Emitted by execution, not by the spec file alone. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced by spec; not created here. |
| Release material | `release/candidates/roads-rail-trade/`, `release/manifests/roads-rail-trade/` | Release authority owns final state. |

[⬆ Back to top](#top)

---

## 13. Minimal spec profile shape

```yaml
schema_version: kfm.pipeline_spec.roads_rail_trade.v1
spec_id: roads-rail-trade.<profile>
version: 0.1.0
status: draft
domain: roads-rail-trade
schema_contract_segment: transport
owner: <roads-rail-trade-domain-steward>
implementation:
  target_pipeline: pipelines/domains/roads-rail-trade/<lane>
  execution_mode: dry_run_first
sources:
  source_descriptor_refs: []
lifecycle:
  input_state: WORK
  output_state: PROCESSED
requirements:
  evidence_bundle_required: true
  source_role_required: true
  temporal_fields_required: true
  slug_crosswalk_required: true
  network_graph_receipt_required: true
  operational_context_not_instruction: true
  receipts_required: []
  release_ready: false
anti_collapse:
  spec_is_executable: false
  route_context_is_legal_authority: false
  restriction_context_is_access_instruction: false
  network_edge_is_routing_authority: false
  movement_story_is_evidence: false
  spec_is_release_approval: false
```

[⬆ Back to top](#top)

---

## 14. Tests, fixtures, and validation

Recommended validation coverage:

```text
tests/pipeline_specs/roads-rail-trade/
├── test_spec_shape.py                    # PROPOSED
├── test_no_runtime_outputs.py            # PROPOSED
├── test_implementation_refs.py           # PROPOSED
├── test_transport_slug_boundary.py       # PROPOSED
├── test_source_descriptor_refs.py        # PROPOSED
├── test_temporal_status_gates.py         # PROPOSED
├── test_restriction_not_instruction.py   # PROPOSED
├── test_network_graph_boundary.py        # PROPOSED
├── test_required_receipts.py             # PROPOSED
└── test_root_boundary.py                 # PROPOSED
```

A spec is not ready for execution until it has schema validation, fixture coverage, owner review, source descriptor refs, lifecycle-state assertions, temporal/status gates, slug-boundary checks, operational-context checks, graph-boundary checks, receipt requirements, and release/correction/rollback posture where applicable.

[⬆ Back to top](#top)

---

## 15. Definition of done

This README is done when it:

- replaces the short `pipeline_specs/roads-rail-trade/README.md` stub;
- identifies this path as Roads/Rail/Trade declarative pipeline configuration;
- preserves the `pipeline_specs/` versus `pipelines/` split;
- preserves the governed `roads-rail-trade` vs `transport` slug crosswalk;
- blocks specs from becoming executable logic, source authority, data storage, proof storage, traffic/access/legal route authority, catalog truth, release approval, or public API/UI authority;
- defines expected Roads/Rail/Trade profile families, lifecycle gates, temporal gates, slug gates, operational-context gates, graph gates, receipts, tests, and open questions.

Future spec files are done only when they validate, point to executable lanes, use stable source descriptors, declare lifecycle states, require receipts, preserve evidence/source-role/slug/operational/graph posture, and document release/correction/rollback expectations.

[⬆ Back to top](#top)

---

## 16. Open questions

| ID | Question | Status |
|---|---|---|
| `PIPE-SPEC-RRT-001` | Which Roads/Rail/Trade spec schema is canonical? | NEEDS VERIFICATION |
| `PIPE-SPEC-RRT-002` | Which first-wave Roads/Rail/Trade source descriptors should be activated? | NEEDS VERIFICATION |
| `PIPE-SPEC-RRT-003` | Which profile should be implemented first: roads, rail, historic routes, restrictions, crossings/facilities, or network graph? | NEEDS VERIFICATION |
| `PIPE-SPEC-RRT-004` | Which CI workflow validates Roads/Rail/Trade specs and the transport slug boundary? | UNKNOWN |
| `PIPE-SPEC-RRT-005` | Which temporal, operator-status, route-event, graph, restriction-context, and release-readiness receipt vocabulary is canonical? | NEEDS VERIFICATION |
| `PIPE-SPEC-RRT-006` | Should specs be split by lifecycle stage, source family, object family, route family, or graph family? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Keep this directory declarative and slug-safe. Do not add executable code, source clients, schemas, contracts, policy decisions, lifecycle outputs, receipts, EvidenceBundles, release decisions, public API code, UI code, traffic/access instructions, legal route decisions, infrastructure exposure packages, or generated movement narratives here. Add those to their responsibility roots and reference them from specs by stable path or identifier.

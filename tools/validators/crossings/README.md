<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-crossings-readme
title: tools/validators/crossings README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-roads-rail-trade-steward-plus-hydrology-steward-plus-infrastructure-steward-plus-policy-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: repository-facing; crossings-validator-parent; transport-side-claim; graph-projection-aware; release-gated
owning_root: tools/
responsibility: proposed parent validator lane for crossing candidate checks across Roads/Rail/Trade crossing families, including source-role, time, carried/crossed object separation, specialization boundaries, graph-derivative boundaries, evidence, policy, release, correction, and public-surface denial checks
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../bridge_river_crossing/README.md
  - ../../../contracts/domains/roads-rail-trade/crossing.md
  - ../../../contracts/domains/roads-rail-trade/bridge.md
  - ../../../contracts/domains/roads-rail-trade/river_crossing.md
  - ../../../contracts/domains/roads-rail-trade/ferry.md
  - ../../../contracts/domains/roads-rail-trade/road_segment.md
  - ../../../contracts/domains/roads-rail-trade/rail_segment.md
  - ../../../contracts/domains/roads-rail-trade/network_node.md
  - ../../../contracts/domains/roads-rail-trade/network_edge.md
  - ../../../docs/domains/roads-rail-trade/README.md
  - ../../../docs/domains/roads-rail-trade/OBJECT_FAMILIES.md
  - ../../../docs/domains/roads-rail-trade/GRAPH_PROJECTIONS.md
  - ../../../docs/domains/hydrology/README.md
  - ../../../docs/domains/settlements-infrastructure/
  - ../../../policy/domains/roads-rail-trade/
  - ../../../data/proofs/evidence_bundle/
  - ../../../data/receipts/
  - ../../../release/
notes:
  - "This README documents a proposed crossings validator parent lane. It does not confirm executable files."
  - "Crossing records are transport-side claims. They do not certify safe passage, active closure, legal access, rail safety, bridge condition, ferry service, flood/ford condition, routing authority, graph truth, map truth, or publication approval."
  - "Validators enforce declared contracts, schemas, and policy. They do not create EvidenceBundles, define crossing truth, approve release, or publish public outputs."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/crossings

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-crossings--validators-informational)
![boundary](https://img.shields.io/badge/boundary-transport--side-blueviolet)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/crossings/` is the proposed parent validator lane for Roads/Rail/Trade crossing candidates: generic crossings, road-rail crossings, road-road intersections, rail-rail crossings, grade-separated crossings, water crossings, historic crossings, candidate/model-derived crossings, graph projections, evidence support, policy review, release readiness, and public-surface denial checks.

---

## Purpose

`tools/validators/crossings/` exists to hold parent-level validator guidance for crossing records and crossing-adjacent specializations.

The durable KFM question for this lane is:

> Does a crossing candidate preserve transport-side claim scope, crossing family, carried/crossed object separation, source-role/time discipline, specialization boundaries, graph-derivative boundaries, evidence closure, policy posture, release readiness, and rollback support?

The answer should be a deterministic validation result. It should not create crossing truth, graph truth, route truth, hydrology truth, infrastructure truth, EvidenceBundles, policy decisions, release decisions, public map layers, API payloads, or AI answers.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/crossings/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Crossing validator executables | **PROPOSED / NEEDS VERIFICATION** | No script name is claimed here. |
| Crossing contract | **CONFIRMED in repo evidence / draft** | Contract defines `crossing` as a transport-side claim and denies routing, live closure, hydrology truth, specialization truth, graph truth, and publication authority. |
| Crossing claim families | **CONFIRMED in repo evidence / draft** | Contract names road-rail, road-road, rail-rail, grade-separated, water, historic, and candidate crossing families. |
| Child specialization lane | **PARTIAL / NEEDS VERIFICATION** | `bridge_river_crossing/` is documented; other specialization validators may be added later. |
| Paired schemas and CI wiring | **NEEDS VERIFICATION** | Crossing contract notes paired schema was not found in its expansion task; validator/test/CI behavior remains unverified. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Crossings validator parent/index | `tools/validators/crossings/` |
| Bridge/river-crossing validator specialization | `tools/validators/bridge_river_crossing/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Generic crossing meaning | `contracts/domains/roads-rail-trade/crossing.md` |
| Crossing specializations | `contracts/domains/roads-rail-trade/bridge.md`, `ferry.md`, `river_crossing.md`, and accepted companion contracts |
| Roads/Rail/Trade domain doctrine | `docs/domains/roads-rail-trade/` |
| Hydrology truth and water evidence | `docs/domains/hydrology/`, accepted hydrology contracts/data lanes |
| Structural asset/infrastructure identity | `docs/domains/settlements-infrastructure/` and accepted infrastructure contract lanes |
| Schemas | `schemas/contracts/v1/domains/roads-rail-trade/` or ADR-selected schema home |
| Policy rules | `policy/domains/roads-rail-trade/` or accepted policy homes |
| EvidenceBundles and receipts | `data/proofs/evidence_bundle/`, `data/receipts/` |
| Release records | `release/` |
| Tests and fixtures | `tests/validators/crossings/` or accepted test convention |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** parent/index validator code may live here only when it checks crossing-family invariants and delegates specific meaning to contracts and child validator lanes.
- **NEEDS VERIFICATION:** exact executable names, schema homes, fixtures, policy bundles, source descriptors, child lanes, graph checks, and CI wiring.
- **DENY:** using this folder as a contract home, schema home, policy home, source registry, evidence store, lifecycle data store, release record store, graph authority, public runtime surface, routing authority, or safety authority.

[Back to top](#top)

---

## Child lanes

| Child lane | Validator question | Status |
|---|---|---|
| `../bridge_river_crossing/` | Do bridge and river-crossing candidates preserve transport-side claim scope, hydrology/infrastructure references, graph boundaries, evidence, policy, and release support? | README confirmed; executable proposed. |

Future child lanes should be named for concrete crossing-specialization invariants, not as new authority roots. Examples may include road-rail crossing, ferry crossing, grade-separation, access-restriction crossing, or graph-projection crossing if supported by contracts, schemas, policy, and fixtures.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/crossings/` include checks that:

- validate generic crossing candidates against the declared crossing contract;
- preserve road segment, rail segment, corridor route, route membership, crossing, bridge, ferry, river-crossing, network-node, and network-edge separation;
- prevent spatial intersection from becoming confirmed crossing truth without evidence and review;
- preserve crossing family and mode for road-rail, road-road, rail-rail, grade-separated, water, historic, candidate, modeled, administrative, and observed crossings;
- require source-role, source authority, valid time, retrieval time, release time, and correction time discipline;
- require EvidenceRef or EvidenceBundle support for public-bound crossing claims;
- require policy, review, release, correction, and rollback references for public-bound crossing records;
- prevent derived graph nodes/edges from replacing crossing evidence;
- deny unsupported live closure, legal access, emergency routing, safety, inspection, flood/ford condition, or public release claims.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/crossings/` | Correct home |
|---|---|
| Shared validator plumbing | `tools/validators/_common/` |
| Roads/Rail/Trade contracts | `contracts/domains/roads-rail-trade/` |
| Hydrology observations or water truth | hydrology contracts and lifecycle data lanes |
| Infrastructure asset contracts | accepted infrastructure contract lane |
| Schemas | `schemas/contracts/v1/...` |
| Policy rules | `policy/...` |
| Source descriptors | `data/registry/sources/...` |
| Lifecycle data | dedicated `data/` lifecycle roots |
| EvidenceBundles or receipts | `data/proofs/`, `data/receipts/` |
| Release records | `release/` |
| Graph authority | graph/triplet lanes, derived from source records |
| Live routing, emergency, access, or safety products | denied unless governed by a separate accepted path |
| Tests and fixtures | `tests/` and `fixtures/` conventions |

[Back to top](#top)

---

## Crossings validation posture

This validator parent lane is for anti-collapse checks around transport-side crossing meaning.

It should fail closed, deny, abstain, or route to review when a candidate collapses:

- spatial intersection into confirmed crossing truth;
- crossing record into road/rail segment or route membership truth;
- crossing record into bridge, ferry, river-crossing, water, or infrastructure truth;
- historic crossing evidence into modern access truth;
- graph node/edge into source crossing evidence;
- closure/status/restriction context into emergency, legal, routing, or safety advice;
- candidate/model/OCR/map-derived output into published crossing truth without evidence and review;
- public map/API/export into release-approved product without required evidence and release support.

The validator lane must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `CROSSINGS_VALIDATION_PASS` | Configured crossings checks passed. |
| `CROSSINGS_VALIDATION_FAIL` | Configured checks failed. |
| `SPATIAL_INTERSECTION_NOT_EVIDENCE` | Candidate treats geometry overlap as confirmed crossing truth. |
| `OBJECT_FAMILY_COLLAPSE` | Candidate collapses route, segment, crossing, bridge, ferry, river-crossing, or graph object families. |
| `SOURCE_ROLE_COLLAPSE` | Candidate collapses source roles or authority limits. |
| `TIME_COLLAPSE` | Valid/source/retrieval/release/correction times are collapsed. |
| `GRAPH_AUTHORITY_COLLAPSE` | Derived graph node/edge replaces source crossing record. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef or EvidenceBundle pointer is absent. |
| `RELEASE_REFERENCE_MISSING` | Required ReleaseManifest, rollback target, or correction path is absent. |
| `SAFETY_ROUTING_OR_ACCESS_DENIED` | Candidate makes unsupported safety, routing, emergency, closure, or legal-access claim. |
| `PUBLIC_BOUNDARY_VIOLATION` | Candidate is not safe for public/governed output as shaped. |
| `LIFECYCLE_VIOLATION` | Candidate appears to skip required lifecycle states. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/crossings/
├── README.md
├── test_crossings_validators.py
└── fixtures/
    ├── valid_generic_crossing_claim/
    ├── valid_road_rail_crossing_claim/
    ├── spatial_intersection_as_truth_denied/
    ├── graph_edge_as_source_record_denied/
    ├── crossing_family_collapse_denied/
    ├── live_closure_without_fresh_source_denied/
    ├── historic_crossing_as_modern_access_denied/
    └── missing_release_reference/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/crossings
```

```bash
python tools/validators/crossings/validate_crossing_candidate.py --fixtures --dry-run
```

> [!NOTE]
> This is a proposed interface, not proof that `validate_crossing_candidate.py` or the test path exists.

[Back to top](#top)

---

## Review checklist

- [ ] Validator reads declared crossing contracts rather than defining meaning locally.
- [ ] Validator reads declared schemas and policy rather than defining shape or policy locally.
- [ ] Spatial intersection does not become confirmed crossing truth without evidence and review.
- [ ] Route, segment, membership, crossing, bridge, ferry, river-crossing, network-node, and network-edge objects remain distinct.
- [ ] Hydrology, infrastructure, hazards, access restriction, status, and specialization boundaries are preserved.
- [ ] Graph projections remain derived and cite source records.
- [ ] EvidenceBundle, policy, review, release, rollback, and correction support are checked where required.
- [ ] Safety, routing, closure, legal access, and public release claims are denied unless separately governed.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for empty file. |
| Next smallest safe change | Verify paired schemas, source descriptors, policy bundles, fixtures, validator entrypoints, graph checks, child lanes, and CI wiring before promoting this lane beyond draft. |

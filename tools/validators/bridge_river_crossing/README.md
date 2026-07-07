<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-bridge-river-crossing-readme
title: tools/validators/bridge_river_crossing README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-roads-rail-trade-steward-plus-hydrology-steward-plus-infrastructure-steward-plus-policy-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: repository-facing; cross-domain-validator; bridge-river-crossing; transport-side-claim; hydrology-boundary-aware
owning_root: tools/
responsibility: proposed validator lane for bridge and river-crossing candidate checks across Roads/Rail/Trade, Hydrology, Settlements/Infrastructure, Hazards, Archaeology/Cultural Heritage, evidence, policy, release, graph, and public-surface boundaries
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../../../contracts/domains/roads-rail-trade/bridge.md
  - ../../../contracts/domains/roads-rail-trade/river_crossing.md
  - ../../../contracts/domains/roads-rail-trade/crossing.md
  - ../../../contracts/domains/roads-rail-trade/ferry.md
  - ../../../docs/domains/roads-rail-trade/README.md
  - ../../../docs/domains/roads-rail-trade/OBJECT_FAMILIES.md
  - ../../../docs/domains/roads-rail-trade/IDENTITY_MODEL.md
  - ../../../docs/domains/roads-rail-trade/GRAPH_PROJECTIONS.md
  - ../../../docs/domains/hydrology/README.md
  - ../../../docs/domains/hydrology/IDENTITY_MODEL.md
  - ../../../docs/domains/settlements-infrastructure/
  - ../../../policy/domains/roads-rail-trade/
  - ../../../policy/domains/hydrology/
  - ../../../data/proofs/evidence_bundle/
  - ../../../data/receipts/
  - ../../../release/
notes:
  - "This README documents a proposed validator lane. It does not confirm executable files."
  - "Bridge and river-crossing records are transport-side claims in Roads/Rail/Trade. They do not certify structural condition, hydrology truth, live closure, safe passage, legal access, emergency routing, or publication approval."
  - "Validators enforce declared contracts, schemas, and policy. They do not create EvidenceBundles, define water truth, own infrastructure assets, approve release, or publish public outputs."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/bridge_river_crossing

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-bridge--river--crossing--validators-informational)
![boundary](https://img.shields.io/badge/boundary-transport--side-blueviolet)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/bridge_river_crossing/` is the proposed validator lane for bridge and river-crossing candidates: transport-side crossing claims, carried/crossed object separation, hydrology references, infrastructure references, source-role/time discipline, graph-derivative boundaries, evidence support, policy review, release readiness, and public-surface denial checks.

---

## Purpose

`tools/validators/bridge_river_crossing/` exists for validator logic that spans bridge and river-crossing contracts in Roads / Rail / Trade while preserving Hydrology and Infrastructure boundaries.

The durable KFM question for this lane is:

> Does a bridge or river-crossing candidate preserve transport-side claim scope, carried/crossed object separation, hydrology and infrastructure references, source-role/time discipline, evidence closure, public-surface policy, and release readiness?

The answer should be a deterministic validation result. It should not create bridge truth, water truth, structural safety truth, live access truth, EvidenceBundles, policy decisions, release decisions, emergency messages, graph truth, or map/API products.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/bridge_river_crossing/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Validator executables | **PROPOSED / NEEDS VERIFICATION** | No script name is claimed here. |
| Bridge contract | **CONFIRMED in repo evidence / draft** | Contract defines a transport-side bridge claim and denies structural inspection, live routing, hydrology truth, and publication authority. |
| River-crossing contract | **CONFIRMED in repo evidence / draft** | Contract defines a transport-side river-crossing claim and states Hydrology owns water evidence. |
| Paired schemas | **NEEDS VERIFICATION** | Bridge and river-crossing contracts note paired schemas were not found in their expansion tasks. |
| Policy and release wiring | **PROPOSED / NEEDS VERIFICATION** | This README does not prove policy bundles, source descriptors, release gates, or CI are wired. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Bridge/river-crossing validator entrypoints | `tools/validators/bridge_river_crossing/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Transport-side bridge meaning | `contracts/domains/roads-rail-trade/bridge.md` |
| Transport-side river-crossing meaning | `contracts/domains/roads-rail-trade/river_crossing.md` |
| Roads/Rail/Trade domain doctrine | `docs/domains/roads-rail-trade/` |
| Hydrology truth and water-system evidence | `docs/domains/hydrology/`, `contracts/domains/hydrology/` |
| Structural asset/infrastructure identity | `docs/domains/settlements-infrastructure/` and accepted infrastructure contract lanes |
| Schemas | `schemas/contracts/v1/domains/roads-rail-trade/` or ADR-selected schema home |
| Policy rules | `policy/domains/roads-rail-trade/`, `policy/domains/hydrology/`, or accepted policy homes |
| EvidenceBundles and receipts | `data/proofs/evidence_bundle/`, `data/receipts/` |
| Release records | `release/` |
| Tests and fixtures | `tests/validators/bridge_river_crossing/` or accepted test convention |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it validates declared bridge/river-crossing contracts and cross-lane invariants.
- **NEEDS VERIFICATION:** exact executable names, schema homes, fixtures, policy bundles, source descriptors, and CI wiring.
- **DENY:** using this folder as a contract home, schema home, policy home, source registry, evidence store, lifecycle data store, release record store, graph authority, public runtime surface, live routing surface, or structural-safety authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/bridge_river_crossing/` include checks that:

- verify bridge and river-crossing candidates preserve transport-side claim scope;
- separate bridge, river-crossing, generic crossing, ferry, route, segment, route membership, status, and access restriction objects;
- require hydrology references for river, waterbody, flood, ford, water-condition, or reach evidence where applicable;
- require infrastructure references when structural asset identity is outside Roads/Rail/Trade ownership;
- reject structural inspection, load safety, legal clearance, live closure, routing-suitability, safe-passage, and emergency claims unless a separate governed path exists;
- verify source-role, source authority, valid time, retrieval time, release time, and correction time are distinct or explicitly unknown;
- require EvidenceRef or EvidenceBundle support for public-bound bridge/crossing claims;
- check graph projections remain derived topology and cite source bridge/crossing records;
- check release references, rollback targets, and correction propagation for public-bound outputs.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/bridge_river_crossing/` | Correct home |
|---|---|
| Shared validator plumbing | `tools/validators/_common/` |
| Roads/Rail/Trade contracts | `contracts/domains/roads-rail-trade/` |
| Hydrology contracts or observations | `contracts/domains/hydrology/`, lifecycle `data/.../hydrology/` |
| Infrastructure asset contracts | accepted infrastructure contract lane |
| Schemas | `schemas/contracts/v1/...` |
| Policy rules | `policy/...` |
| Source descriptors | `data/registry/sources/...` |
| Lifecycle data | dedicated `data/` lifecycle roots |
| EvidenceBundles or receipts | `data/proofs/`, `data/receipts/` |
| Release records | `release/` |
| Graph authority | graph/triplet lanes, derived from source records |
| Live routing, emergency, or safety products | denied unless governed by a separate accepted path |
| Tests and fixtures | `tests/` and `fixtures/` conventions |

[Back to top](#top)

---

## Cross-domain validation posture

This validator lane is for anti-collapse checks around movement, water, structure, time, graph, and publication meaning.

It should fail closed, deny, abstain, or route to review when a candidate collapses:

- bridge identity into full infrastructure asset truth;
- river-crossing claim into hydrology truth;
- hydrology context into transport ownership;
- bridge/river-crossing record into live routing or safe-passage advice;
- historic crossing evidence into modern access truth;
- graph edge into source record truth;
- closure/status/restriction context into emergency or legal advice;
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
| `BRIDGE_RIVER_CROSSING_VALIDATION_PASS` | Configured bridge/river-crossing checks passed. |
| `BRIDGE_RIVER_CROSSING_VALIDATION_FAIL` | Configured checks failed. |
| `TRANSPORT_SCOPE_COLLAPSE` | Candidate exceeds transport-side claim scope. |
| `HYDROLOGY_REF_MISSING` | Required Hydrology reference is absent. |
| `INFRASTRUCTURE_REF_MISSING` | Required infrastructure/asset reference is absent. |
| `SOURCE_ROLE_COLLAPSE` | Candidate collapses source roles or authority limits. |
| `TIME_COLLAPSE` | Valid/source/retrieval/release/correction times are collapsed. |
| `GRAPH_AUTHORITY_COLLAPSE` | Derived graph edge replaces source bridge/crossing record. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef or EvidenceBundle pointer is absent. |
| `RELEASE_REFERENCE_MISSING` | Required ReleaseManifest, rollback target, or correction path is absent. |
| `SAFETY_OR_ROUTING_DENIED` | Candidate makes unsupported safety, legal, emergency, or live-routing claim. |
| `PUBLIC_BOUNDARY_VIOLATION` | Candidate is not safe for public/governed output as shaped. |
| `LIFECYCLE_VIOLATION` | Candidate appears to skip required lifecycle states. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/bridge_river_crossing/
├── README.md
├── test_bridge_river_crossing_validators.py
└── fixtures/
    ├── valid_transport_side_bridge_claim/
    ├── valid_river_crossing_with_hydrology_ref/
    ├── missing_hydrology_ref/
    ├── bridge_as_full_asset_denied/
    ├── historic_crossing_as_modern_access_denied/
    ├── graph_edge_as_source_record_denied/
    ├── live_closure_without_fresh_source_denied/
    └── missing_release_reference/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/bridge_river_crossing
```

```bash
python tools/validators/bridge_river_crossing/validate_bridge_river_crossing_candidate.py --fixtures --dry-run
```

> [!NOTE]
> This is a proposed interface, not proof that `validate_bridge_river_crossing_candidate.py` or the test path exists.

[Back to top](#top)

---

## Review checklist

- [ ] Validator reads declared bridge/river-crossing contracts rather than defining meaning locally.
- [ ] Validator reads declared schemas and policy rather than defining shape or policy locally.
- [ ] Bridge, crossing, river-crossing, ferry, route, segment, status, and restriction objects remain distinct.
- [ ] Hydrology references are required for water evidence where material.
- [ ] Infrastructure references are required for asset identity where material.
- [ ] Structural condition, safety, access, live closure, legal, and routing claims are denied unless separately governed.
- [ ] Graph projections remain derived and cite source records.
- [ ] EvidenceBundle, policy, review, release, rollback, and correction support are checked where required.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for empty file. |
| Next smallest safe change | Verify paired schemas, source descriptors, policy bundles, fixtures, validator entrypoints, graph checks, and CI wiring before promoting this lane beyond draft. |

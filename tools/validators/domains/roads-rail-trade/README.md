<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-domains-roads-rail-trade-readme
title: tools/validators/domains/roads-rail-trade README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-roads-rail-trade-steward-plus-transport-contract-steward-plus-policy-steward-plus-evidence-steward-plus-release-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: repository-facing; per-domain-validator-index; roads-rail-trade; transport; network; crossings; routes; release-gated; non-authoritative
owning_root: tools/
responsibility: proposed per-domain Roads/Rail/Trade validator index for RoadSegment, HistoricRoute, RailSegment, Depot, Siding, Yard, Crossing, Bridge, Ferry, RiverCrossing, FreightCorridor, RouteEvent, OperatorStatus, AccessRestriction, NetworkEdge, MovementStoryNode, source-role separation, route/network identity, live-closure denial, legal-access denial, transport/hydrology/infrastructure boundary preservation, evidence, policy, release, correction, rollback, and public-surface denial checks while deferring domain meaning, policy decisions, proof records, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../README.md
  - ../../_common/README.md
  - ../README.md
  - ../../crossings/README.md
  - ../../bridge_river_crossing/README.md
  - ../../cross-domain-joins/README.md
  - ../../cross-lane/README.md
  - ../../../../docs/domains/roads-rail-trade/README.md
  - ../../../../docs/domains/roads-rail-trade/OBJECT_FAMILIES.md
  - ../../../../docs/domains/roads-rail-trade/PIPELINE.md
  - ../../../../docs/domains/roads-rail-trade/PRESERVATION_MATRIX.md
  - ../../../../docs/domains/roads-rail-trade/VERIFICATION_BACKLOG.md
  - ../../../../contracts/transport/
  - ../../../../contracts/domains/roads-rail-trade/
  - ../../../../schemas/contracts/v1/transport/
  - ../../../../schemas/contracts/v1/domains/roads-rail-trade/
  - ../../../../policy/domains/roads-rail-trade/
  - ../../../../data/registry/sources/roads-rail-trade/
  - ../../../../data/proofs/
  - ../../../../data/receipts/
  - ../../../../release/
notes:
  - "This README replaces a greenfield stub. It does not confirm executable files."
  - "No broad tools/validators/roads-rail-trade/README.md was found during this task, so this path currently serves as the inspected per-domain Roads/Rail/Trade validator index."
  - "The domain docs record a documented slug split: roads-rail-trade for most lane segments, with transport used for schema/contract homes. This README follows the requested path and marks schema/contract homes as NEEDS VERIFICATION where the split remains operationally unresolved."
  - "Roads/Rail/Trade validators must not certify safe passage, live closure status, legal access, right-of-way, bridge condition, rail operating status, emergency routing, public route guidance, or publication approval."
  - "Validators enforce declared contracts, schemas, and policy. They do not define route truth, network truth, EvidenceBundle content, policy decisions, release decisions, or public outputs."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/domains/roads-rail-trade

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-roads--rail--trade--validators-informational)
![authority](https://img.shields.io/badge/authority-index--only-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/domains/roads-rail-trade/` is the proposed per-domain Roads/Rail/Trade validator index for road, rail, route, crossing, bridge, ferry, river-crossing, freight-corridor, access-restriction, network-edge, and movement-story checks while preserving source-role, cross-domain ownership, evidence, policy, release, correction, rollback, and public-surface boundaries.

---

## Purpose

`tools/validators/domains/roads-rail-trade/` exists to organize Roads/Rail/Trade validators under the durable `tools/validators/` surface.

The durable KFM question for this index is:

> Do transport candidates preserve route, segment, crossing, event, restriction, operator, and graph identity; source-role posture; temporal scope; live-closure and legal-access boundaries; neighboring-domain ownership; evidence closure; review state; policy decisions; release readiness; correction paths; rollback support; and public-surface denial boundaries before they reach any governed output?

The answer should be a navigable validator index and deterministic validation outputs from configured child lanes. This folder should not create route truth, legal access truth, live closure truth, emergency routing, bridge condition truth, rail operating truth, EvidenceBundles, PolicyDecisions, release decisions, public map layers, API payloads, or AI answers.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/domains/roads-rail-trade/README.md` | **CONFIRMED** | This README replaces the previous greenfield stub. |
| Parent per-domain validators README | **CONFIRMED stub** | `tools/validators/domains/README.md` currently says only `# Per-domain validators`; this file keeps its own boundary explicit. |
| Broad `tools/validators/roads-rail-trade/README.md` | **NOT FOUND in this task** | This path currently serves as the inspected Roads/Rail/Trade validator index. |
| Roads/Rail/Trade domain doctrine | **CONFIRMED in repo evidence / draft** | `docs/domains/roads-rail-trade/README.md` defines scope, object roster, non-ownership boundaries, and the `transport/` schema/contract slug split. |
| Crossing contract evidence | **CONFIRMED in repo evidence / draft** | `contracts/domains/roads-rail-trade/crossing.md` defines a transport-side crossing claim and denies routing advice, live closure authority, hydrology truth, legal access status, graph truth, and publication approval. |
| Existing related validator lanes | **CONFIRMED README siblings / executable proposed** | `crossings/`, `bridge_river_crossing/`, and cross-domain lanes exist where scope overlaps; executable behavior remains unverified. |
| Child README lanes | **NONE CONFIRMED IN THIS TASK** | No child Roads/Rail/Trade validator README was verified while writing this index. |
| Executables, schemas, fixtures, policy bundles, and CI wiring | **NEEDS VERIFICATION** | No script names, test paths, schema maturity, policy bundles, receipts, runtime behavior, or CI behavior are claimed as implemented here. |

[Back to top](#top)

---

## Child lanes

No child README lanes were confirmed during this edit.

Future child lanes should be added only when they represent a distinct Roads/Rail/Trade validator specialty, fixture family, edge, or public-surface invariant with accepted contracts, schemas, policy posture, fixtures, receipts, and report semantics.

Possible future children remain **PROPOSED** until verified:

- `road-segment/` for road segment identity, lineage, source role, geometry, and public-safe rendering;
- `rail-segment/` for rail alignment, operator status, active/abandoned posture, and rail/non-rail role separation;
- `historic-route/` for historic route membership, temporal uncertainty, source conflict, and narrative caution;
- `crossing/` for road/rail/intersection/crossing relation checks without hydrology, bridge, legal-access, or live-routing collapse;
- `bridge-ferry-river-crossing/` for transport crossing specializations while preserving Hydrology and Infrastructure authority;
- `access-restriction/` for closure, detour, weight, height, seasonal, permit, and access claims without live operational authority;
- `network-edge/` for derived graph topology, route membership, and graph-as-derivative posture;
- `movement-story/` for Focus Mode narrative nodes with evidence, policy, sensitivity, and rollback support.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Per-domain Roads/Rail/Trade validator index | `tools/validators/domains/roads-rail-trade/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Crossing validator context | `tools/validators/crossings/`, `tools/validators/bridge_river_crossing/` |
| Cross-domain invariant validators | `tools/validators/cross-domain-joins/` |
| Roads/Rail/Trade domain meaning | `docs/domains/roads-rail-trade/`, `contracts/transport/`, `contracts/domains/roads-rail-trade/`, or ADR-selected contract home |
| Transport schemas | `schemas/contracts/v1/transport/`, `schemas/contracts/v1/domains/roads-rail-trade/`, or ADR-selected schema home |
| Policy rules | `policy/domains/roads-rail-trade/` or accepted policy homes |
| Source descriptors | `data/registry/sources/roads-rail-trade/` or accepted source registry home |
| Evidence/proof support | `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, manifests, rollback, corrections | `release/` |
| Tests and fixtures | `tests/validators/domains/roads-rail-trade/`, `tests/domains/roads-rail-trade/`, `fixtures/domains/roads-rail-trade/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live below this folder when it checks declared Roads/Rail/Trade invariants and delegates meaning, source roles, policy, evidence, and release authority to owning roots.
- **NEEDS VERIFICATION:** exact executable names, schema homes, policy bundle digests, source descriptors, fixtures, report destinations, receipts, runtime behavior, slug resolution, and CI wiring.
- **DENY:** using this folder as transport doctrine, contract home, schema home, policy home, source registry, evidence store, lifecycle data store, receipt store, release record store, routing engine, live closure service, legal access authority, bridge safety authority, rail operating authority, public map product surface, or domain-meaning authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/domains/roads-rail-trade/` include:

- this parent/index README;
- child README lanes for narrow transport validator families;
- optional parent runner code that delegates to child validators without redefining their rules;
- validators that check road, rail, historic route, freight corridor, crossing, bridge, ferry, river crossing, access restriction, route event, operator status, network edge, and movement story posture;
- validators that check source-role discipline, route membership, temporal scope, geometry lineage, public-safe generalization, evidence closure, review state, policy decisions, release references, correction cascade, and rollback support;
- validators that check cross-lane joins preserve Settlements/Infrastructure, Hydrology, Archaeology, People/DNA/Land, Hazards, Geology, Agriculture, and other neighboring-domain authority boundaries;
- synthetic fixture references and test-surface guidance;
- docs or reports that explain validator scope without becoming authoritative transport doctrine.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/domains/roads-rail-trade/` | Correct home |
|---|---|
| Shared validator plumbing | `tools/validators/_common/` |
| Roads/Rail/Trade domain docs | `docs/domains/roads-rail-trade/` |
| Transport contracts | `contracts/transport/`, `contracts/domains/roads-rail-trade/`, or ADR-selected home |
| Schemas | `schemas/contracts/v1/...` |
| Policy rules | `policy/...` |
| Source descriptors | `data/registry/sources/...` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| EvidenceBundles, proofs, receipts, ValidationReports | `data/proofs/`, `data/receipts/` |
| Release manifests, decisions, rollback, corrections | `release/` |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and fixture conventions |
| Public API, UI, map, tile, export, search, graph, Focus Mode, routing, live closure, legal access, emergency route, safety, regulatory, or AI runtime code | governed application/runtime roots |

[Back to top](#top)

---

## Roads/Rail/Trade validator posture

Roads/Rail/Trade validators must fail closed, deny, abstain, or route to steward review when a candidate:

- lacks EvidenceRef, EvidenceBundle, source descriptor, source-role, rights, time, geometry lineage, route membership, or object-family support;
- collapses RoadSegment, HistoricRoute, RailSegment, Depot, Siding, Yard, Crossing, Bridge, Ferry, RiverCrossing, FreightCorridor, RouteEvent, OperatorStatus, AccessRestriction, NetworkEdge, or MovementStoryNode into another role;
- treats a derived network edge as source geometry or graph truth without cited transport evidence;
- treats a route/story/narrative claim as confirmed route membership without evidence and temporal scope;
- certifies safe passage, legal access, live closure status, emergency routing, rail operating status, bridge condition, ferry service status, flood/ford condition, or right-of-way without owning authority and release support;
- imports Hydrology water truth, Settlements/Infrastructure asset truth, Archaeology location truth, Hazards event/closure truth, People/Land ownership truth, or Geology/Soil truth without preserving ownership, source role, sensitivity, and EvidenceBundle support;
- exposes sensitive infrastructure, archaeology, private land, historical/cultural route context, or reverse-engineerable derivatives without review, policy, release, correction, and rollback support;
- lacks a required ReviewRecord, PolicyDecision, ValidationReport, ReleaseManifest, correction path, or rollback target;
- maps, tiles, exports, searches, embeds, graphs, summarizes, or answers with Roads/Rail/Trade content beyond the approved public-safe derivative;
- bypasses lifecycle gates or treats validator output as release approval.

The validator lane must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard parent outcomes

| Outcome | Meaning |
|---|---|
| `RRT_DOMAIN_VALIDATORS_PASS` | Configured Roads/Rail/Trade validators passed. |
| `RRT_DOMAIN_VALIDATORS_FAIL` | One or more configured validators failed. |
| `CHILD_VALIDATOR_MISSING` | Expected Roads/Rail/Trade child validator lane or runner is absent. |
| `CHILD_VALIDATOR_FAILED` | Child validator reported one or more findings. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef or EvidenceBundle pointer is absent. |
| `SOURCE_ROLE_COLLAPSE` | Candidate collapses source-role or object-family posture. |
| `TRANSPORT_IDENTITY_UNRESOLVED` | Road, rail, crossing, route, corridor, operator, or network identity is missing or unresolved. |
| `NETWORK_EDGE_AS_TRUTH_DENIED` | Derived graph edge is treated as source truth. |
| `LIVE_CLOSURE_AUTHORITY_DENIED` | Candidate presents KFM as live closure or routing authority. |
| `LEGAL_ACCESS_AUTHORITY_DENIED` | Candidate presents KFM as legal access, right-of-way, or regulatory authority. |
| `CROSSING_BOUNDARY_COLLAPSE` | Crossing claim absorbs Hydrology, Infrastructure, Bridge/Ferry/Ford, or legal-access truth. |
| `ROUTE_MEMBERSHIP_UNSUPPORTED` | Route, historic route, or movement-story membership lacks evidence or temporal support. |
| `SENSITIVE_JOIN_DENIED` | Transport join reveals or infers restricted neighboring-domain context. |
| `REVIEW_OR_POLICY_GAP` | Required review state or PolicyDecision is absent. |
| `RELEASE_REFERENCE_MISSING` | Required ReleaseManifest, correction path, or rollback target is absent. |
| `CROSS_DOMAIN_AUTHORITY_COLLAPSE` | Candidate absorbs another domain's truth into Roads/Rail/Trade without preserving boundaries. |
| `PUBLIC_SURFACE_LEAK_RISK` | Candidate is unsafe for public/governed output as shaped. |
| `REPORT_DESTINATION_INVALID` | QA report or receipt destination is outside an accepted root. |
| `IGNORED_WITH_REASON` | Finding was ignored under an explicit, reviewable rule. |
| `IGNORE_RULE_EXPIRED` | Ignore rule is stale and must be reviewed. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/domains/roads-rail-trade/
├── README.md
├── test_roads_rail_trade_domain_validator_parent.py
└── fixtures/
    ├── valid_public_safe_route_bundle/
    ├── missing_evidence_ref/
    ├── source_role_collapse/
    ├── unresolved_transport_identity/
    ├── network_edge_as_truth_denied/
    ├── live_closure_authority_denied/
    ├── legal_access_authority_denied/
    ├── crossing_boundary_collapse/
    ├── sensitive_join_denied/
    └── ignored_with_reason/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/domains/roads-rail-trade
```

```bash
python tools/validators/domains/roads-rail-trade/run_roads_rail_trade_domain_validators.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `run_roads_rail_trade_domain_validators.py` or the test path exists.

[Back to top](#top)

---

## Review checklist

- [ ] Parent runner delegates to child validators instead of redefining their rules.
- [ ] Validator reads declared transport contracts, schemas, and policy rather than defining meaning locally.
- [ ] Road, rail, route, crossing, restriction, operator, event, network, and story object families remain distinct.
- [ ] Source role, route membership, geometry lineage, and temporal scope remain visible.
- [ ] Crossings do not become hydrology truth, infrastructure truth, legal-access truth, live-routing truth, or publication approval.
- [ ] KFM is never presented as live closure, routing, safe-passage, legal-access, right-of-way, bridge-safety, rail-operating, emergency-route, or regulatory authority.
- [ ] Cross-domain joins preserve ownership, source role, sensitivity, and EvidenceBundle support.
- [ ] Map, tile, search, graph, export, Focus Mode, and AI surfaces do not reveal restricted details or reverse-engineerable derivatives.
- [ ] Reports and receipts are written only to accepted roots.
- [ ] Validator output is not described as truth, policy, release, publication, route authority, or Directory Rules approval.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for greenfield stub and current parent index for Roads/Rail/Trade validators. |
| Next smallest safe change | Verify child validator scripts, accepted profiles, schemas, source descriptors, policy bundles, fixtures, report destinations, receipts, slug resolution, transport identity behavior, crossing boundary behavior, release linkage, cross-domain join behavior, and CI/runtime wiring before promoting this lane beyond draft. |

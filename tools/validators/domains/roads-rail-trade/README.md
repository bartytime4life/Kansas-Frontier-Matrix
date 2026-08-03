<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-domains-roads-rail-trade-readme
title: tools/validators/domains/roads-rail-trade README
type: README
version: v0.2
status: draft; one-bounded-executable
owner: TODO-tooling-qa-owner-plus-roads-rail-trade-steward-plus-contract-schema-policy-evidence-release-stewards
created: 2026-07-07
updated: 2026-08-03
policy_label: repository-facing; per-domain-validator-index; roads-rail-trade; route; release-gated; non-authoritative
owning_root: tools/
truth_posture: cite-or-abstain; implementation claims require current repository evidence
related:
  - ../../README.md
  - ../../_common/README.md
  - ../README.md
  - ../../../../docs/domains/roads-rail-trade/README.md
  - ../../../../docs/domains/roads-rail-trade/CORRIDOR_ROUTE_SCHEMA_PROFILE.md
  - ../../../../contracts/domains/roads-rail-trade/corridor_route.md
  - ../../../../schemas/contracts/v1/domains/roads-rail-trade/corridor_route.schema.json
  - ../../../../fixtures/domains/roads-rail-trade/corridor_route/
  - ../../../../tests/schemas/test_corridor_route_contract.py
  - ../../../../policy/domains/roads-rail-trade/
  - ../../../../data/registry/sources/roads-rail-trade/
  - ../../../../release/
notes:
  - "v0.2 records the fixture-only CorridorRoute validator added from New Ideas 3-31-26.pdf."
  - "The validator checks declared schema and anti-collapse invariants only. It does not define route truth, fetch sources, execute policy, approve review, release, publish, or provide live/legal routing advice."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tools/validators/domains/roads-rail-trade/`

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-roads--rail--trade--validators-informational)
![executables](https://img.shields.io/badge/executables-one__bounded__profile-orange)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** This lane holds deterministic Roads / Rail / Trade validator code that checks declared contracts and schemas while preserving evidence, policy, lifecycle, release, correction, rollback, neighboring-domain, and public-surface boundaries.

## Authority boundary

Validators may check shape, deterministic identity, temporal ordering, object-family separation, source-role declarations, rights/sensitivity posture, and required governance references. They must not create route truth, legal-access truth, live closure truth, safe-passage advice, bridge or rail operating status, EvidenceBundles, PolicyDecisions, ReviewRecords, release decisions, public layers, API payloads, or AI answers.

| Responsibility | Owning root |
|---|---|
| Semantic meaning | `contracts/` |
| Machine shape | `schemas/` |
| Validation implementation | `tools/validators/` |
| Synthetic examples | `fixtures/` |
| Behavior proof | `tests/` |
| Source identity/rights/cadence | `data/registry/sources/` |
| Policy decision | `policy/` |
| Receipts/proofs | `data/receipts/`, `data/proofs/` |
| Release/correction/rollback | `release/` and accepted accountability lanes |

## Current executable inventory

| Validator | Status | Inputs | Outcomes | Scope limit |
|---|---|---|---|---|
| [`validate_corridor_route.py`](./validate_corridor_route.py) | **CONFIRMED bounded executable** | [`CorridorRoute` schema](../../../../schemas/contracts/v1/domains/roads-rail-trade/corridor_route.schema.json) and synthetic fixtures under [`fixtures/domains/roads-rail-trade/corridor_route/`](../../../../fixtures/domains/roads-rail-trade/corridor_route/) | `PASS`, `ABSTAIN`, `DENY`, `ERROR` | No network; no source admission, historical accuracy determination, policy execution, reviewer authority, release, publication, legal designation, public access, or live routing authority. |

No other executable in this lane is claimed by this README without current repository evidence.

## CorridorRoute checks

The current runner:

- loads the paired Draft 2020-12 schema through the repository-owned local resolver;
- recomputes `spec_hash` as SHA-256 over canonical JSON excluding `_fixture_meta` and `spec_hash`;
- requires non-reversed valid time;
- preserves route-versus-segment-versus-membership separation;
- forbids embedded geometry, legal-designation authority, live-routing authority, and publication-approval fields;
- requires bound evidence to carry at least one EvidenceRef;
- returns `ABSTAIN` for non-released candidates with unresolved source, evidence, geometry, or rights;
- returns `DENY` when unresolved support claims release, when sensitive/restricted geometry claims public generalization, or when authoritative representation depends on derived geocoding;
- never mutates lifecycle state.

## Exact fixture outcomes

| Fixture class | Expected result |
|---|---|
| Bound, synthetic historic candidate with explicit uncertainty and generalized public-safe geometry | `PASS` |
| Synthetic candidate with unresolved source/evidence/geometry/rights | `ABSTAIN` |
| Authoritative derived geocode | `DENY` |
| Bound evidence without EvidenceRef | `DENY` |
| Embedded segment truth | `DENY` |
| Live-routing-authority claim | `DENY` |
| Missing temporal uncertainty | `DENY` |
| Sensitive geometry marked for generalized public use | `DENY` |
| Released posture without policy/review/manifest/rollback closure | `DENY` |
| Mismatched deterministic hash | `DENY` |

## Validation

```bash
KFM_NO_NETWORK=1 PYTHONHASHSEED=0 TZ=UTC \
  python tools/validators/domains/roads-rail-trade/validate_corridor_route.py --fixtures

KFM_NO_NETWORK=1 PYTHONHASHSEED=0 TZ=UTC \
  python -m pytest -q tests/schemas/test_corridor_route_contract.py
```

A green focused run means only that the bounded fixture profile behaved as declared. It does not mean the source is admitted, the route exists, the alignment is historically accurate, rights are cleared, policy approved exposure, review occurred, or release/publication is authorized.

## Candidate backlog

Future validators remain **PROPOSED** until paired contracts, schemas, fixtures, tests, source roles, policy posture, and review ownership exist:

- road and rail segment identity;
- source- and time-scoped RouteMembership;
- historic/trade route conflict and sensitivity;
- crossing/bridge/ferry boundaries with Hydrology and Infrastructure;
- access restriction and status-event freshness without live-routing authority;
- derived NetworkEdge and graph-as-derivative checks;
- public-safe route summaries with release/correction/rollback closure.

## Finite outcome guidance

| Outcome | Meaning |
|---|---|
| `PASS` | Declared bounded checks passed. No higher authority is granted. |
| `ABSTAIN` | Input is structurally admissible as a non-released candidate, but required support is unresolved or restricted. |
| `DENY` | Input violates schema, anti-collapse, temporal, integrity, public-safety, or release-closure constraints. |
| `ERROR` | The validator could not safely load or evaluate the input/profile. |

## Open verification

- [ ] Resolve the `roads-rail-trade` versus `transport` path/slug conflict.
- [ ] Confirm schema-registry admission.
- [ ] Bind admitted source-role and rights vocabularies.
- [ ] Add policy-bundle integration without duplicating policy authority.
- [ ] Confirm CODEOWNERS and reviewer responsibilities.
- [ ] Wire the bounded profile into the accepted CI suite without weakening existing checks.
- [ ] Run broader repository regressions on the exact pull-request head.
- [ ] Add release/correction/rollback integration only in a separate governed slice.

[Back to top](#top)

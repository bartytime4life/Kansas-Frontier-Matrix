# `schemas/tests/invalid/domains/transport/` — Transport Invalid Schema Test Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-tests-invalid-domains-transport-readme
title: schemas/tests/invalid/domains/transport/ README
type: readme; compatibility-index; invalid-test-placement-guardrail
version: v0.1
status: draft; empty-invalid-test-path; transport-path-conflicted; NEEDS VERIFICATION
updated: 2026-07-04
policy_label: public
tags: [kfm, schemas, tests, invalid, domains, transport, roads-rail-trade, fixtures, route, corridor, decision-envelope, compatibility]
[/KFM_META_BLOCK_V2] -->

## Purpose

`schemas/tests/invalid/domains/transport/` is a README-only compatibility guardrail for invalid Transport schema-test placement.

The inspected flat Transport schema compatibility lane lives at `schemas/contracts/v1/transport/`.

A path-conflicted domain Transport schema lane also exists at `schemas/contracts/v1/domains/transport/`.

The broader Roads / Rail / Trade schema lane remains the placement-sensitive parent context at `schemas/contracts/v1/domains/roads-rail-trade/`.

## Status

| Item | Status |
|---|---|
| README | present |
| Direct invalid test files found under this path | none found in current search |
| Current role | compatibility guardrail |
| Placement | NEEDS VERIFICATION |
| Transport path posture | slug/path conflict remains visible |

## Boundary

This directory is not the Transport schema family, Roads / Rail / Trade schema authority, fixture authority, policy authority, validator implementation, CI configuration, emitted test-result store, data root, graph root, map root, or release root.

It should not contain canonical Transport schemas, route records, corridor records, source records, lifecycle data, public map payloads, graph projection outputs, release records, or validator code while accepted homes remain separate.

A failing or passing test here would prove only the tested shape behavior. It would not prove route truth, source authority, geometry validity, network validity, policy approval, release readiness, or public-safety.

## Current inventory

| Path | Status | Notes |
|---|---|---|
| `schemas/tests/invalid/domains/transport/README.md` | present | Empty file expanded by this README. |
| `schemas/tests/invalid/domains/transport/*` | not found in current search | No direct invalid test files were found under this path. |
| `schemas/contracts/v1/transport/README.md` | present | Inspected flat Transport schema compatibility index. |
| `schemas/contracts/v1/domains/transport/README.md` | present | Inspected path-conflicted Transport schema lane README. |
| `schemas/contracts/v1/domains/roads-rail-trade/README.md` | present by search | Parent Roads / Rail / Trade schema lane; not reopened in this pass. |
| `fixtures/domains/transport/invalid/README.md` | not found in current search | No matching fixture lane confirmed. |
| `fixtures/domains/roads-rail-trade/invalid/README.md` | not found in current search | No matching fixture lane confirmed. |

## Correct nearby lanes

| Need | Preferred lane |
|---|---|
| Flat Transport compatibility schemas | `schemas/contracts/v1/transport/` |
| Path-conflicted domain Transport scaffolds | `schemas/contracts/v1/domains/transport/` |
| Parent Roads / Rail / Trade schema context | `schemas/contracts/v1/domains/roads-rail-trade/` |
| Roads / Rail / Trade semantic meaning | `contracts/domains/roads-rail-trade/` |
| Transport semantic meaning, if retained | `contracts/domains/transport/` after path review |
| Invalid examples | Fixture lane NEEDS VERIFICATION |
| Schema test code | `tests/schemas/` or accepted project test root |
| Validator implementation | `tools/validators/` |
| Roads / Rail / Trade policy posture | `policy/domains/roads-rail-trade/` or accepted policy lane |
| Release, correction, rollback decisions | `release/` |

## What belongs here

- This README.
- Compatibility notes for this invalid schema-test path.
- Migration notes if historical invalid transport schema tests are discovered here.
- Temporary mirror notes while transport vs Roads / Rail / Trade placement is unresolved.

## What does not belong here

- Canonical `.schema.json` files.
- Invalid fixture JSON files unless an accepted migration assigns them here.
- Real road, rail, route, corridor, crossing, facility, operator, schedule, source, lifecycle, graph, map, tile, or release payloads.
- Graph projections, public map payloads, source-system exports, public tiles, dashboards, screenshots, generated summaries, or direct model-runtime output.
- Policy rules, policy decisions, rights approvals, release records, receipts, proofs, emitted validation reports, validator code, runtime code, package code, or API/UI outputs.
- Claims that Transport or Roads / Rail / Trade data is valid, invalid, source-supported, topology-valid, policy-approved, released, or public-safe merely because this path exists.

## Compatibility rules

| Rule | Requirement |
|---|---|
| Keep path conflict visible | Do not hide the unresolved `transport` vs `roads-rail-trade` and flat-vs-domain lane conflict. |
| Keep schemas in schema lanes | Transport and Roads / Rail / Trade schemas belong in accepted schema homes, not in this test guardrail. |
| Keep fixtures in fixtures | Invalid examples should live in a verified fixture lane unless an accepted migration says otherwise. |
| Shape is not route truth | Test outcomes do not prove route, corridor, network, geometry, source, or operator truth. |
| Tests are not publication | Test outcomes do not publish data, authorize map display, or approve release. |
| Avoid parallel test roots | Add test files only to accepted test homes unless a migration note explains the exception. |

## Validation

```bash
find schemas/tests/invalid/domains/transport -maxdepth 4 -type f | sort
find schemas/contracts/v1/transport schemas/contracts/v1/domains/transport schemas/contracts/v1/domains/roads-rail-trade -maxdepth 4 -type f 2>/dev/null | sort
find fixtures/domains/transport fixtures/domains/roads-rail-trade -maxdepth 5 -type f 2>/dev/null | sort
pytest tests/schemas tests/contract || true
```

Replace `|| true` with fail-closed CI behavior once the relevant test paths are confirmed.

## Open questions

| Question | Status |
|---|---|
| Should `schemas/tests/invalid/domains/transport/` remain as a compatibility guardrail or be retired? | NEEDS VERIFICATION |
| Are there historical references that expect invalid Transport schema tests under this path? | NEEDS VERIFICATION |
| Which fixture lane should own invalid transport or Roads / Rail / Trade examples? | NEEDS VERIFICATION |
| Which route, corridor, network, geometry, source-role, decision-envelope, rights, release-readiness, and public-map cases must be represented as invalid tests? | NEEDS VERIFICATION |

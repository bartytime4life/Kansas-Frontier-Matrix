# `schemas/tests/valid/domains/transport/` — Transport Valid Schema Test Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-tests-valid-domains-transport-readme
title: schemas/tests/valid/domains/transport/ README
type: readme; compatibility-index; valid-test-placement-guardrail
version: v0.1
status: draft; empty-valid-test-path; transport-path-conflicted; NEEDS VERIFICATION
updated: 2026-07-04
policy_label: public
tags: [kfm, schemas, tests, valid, domains, transport, roads-rail-trade, fixtures, route, corridor, network, compatibility]
[/KFM_META_BLOCK_V2] -->

## Purpose

`schemas/tests/valid/domains/transport/` is a README-only compatibility guardrail for valid Transport schema-test placement.

The inspected flat Transport schema compatibility lane lives at `schemas/contracts/v1/transport/`.

A path-conflicted domain Transport schema lane also exists at `schemas/contracts/v1/domains/transport/`.

The broader Roads / Rail / Trade schema lane remains the placement-sensitive parent context at `schemas/contracts/v1/domains/roads-rail-trade/`.

No matching `fixtures/domains/transport/valid/README.md` or `fixtures/domains/roads-rail-trade/valid/README.md` was confirmed in current search.

## Status

| Item | Status |
|---|---|
| README | present |
| Direct valid test files found under this path | none found in current search |
| Current role | compatibility guardrail |
| Placement | NEEDS VERIFICATION |
| Transport path posture | slug/path conflict remains visible |
| Dedicated valid fixture lane | not confirmed in current search |

## Boundary

This directory is not the Transport schema family, Roads / Rail / Trade schema authority, fixture authority, policy authority, validator implementation, CI configuration, emitted test-result store, data root, graph root, map root, or release root.

It should not contain canonical Transport schemas, route records, corridor records, road or rail records, source records, lifecycle data, graph projection outputs, public map payloads, release records, direct model-runtime output, or validator code while accepted homes remain separate.

A passing valid test here would prove only the tested shape behavior. It would not prove route truth, corridor truth, network truth, source authority, geometry validity, topology validity, operator truth, legal road status, policy approval, release readiness, routing safety, implementation proof, or public-safety.

## Current inventory

| Path | Status | Notes |
|---|---|---|
| `schemas/tests/valid/domains/transport/README.md` | present | Empty file expanded by this README. |
| `schemas/tests/valid/domains/transport/*` | not found in current search | No direct valid test files were found under this path. |
| `schemas/tests/invalid/domains/transport/README.md` | present | Inspected related invalid schema-test guardrail. |
| `schemas/contracts/v1/transport/README.md` | present | Inspected flat Transport schema compatibility index. |
| `schemas/contracts/v1/domains/transport/README.md` | present | Inspected path-conflicted Transport schema lane README. |
| `schemas/contracts/v1/domains/roads-rail-trade/README.md` | present by related evidence | Parent Roads / Rail / Trade schema lane; not reopened in this pass. |
| `fixtures/domains/transport/valid/README.md` | not found in current search | Dedicated Transport valid fixture lane NEEDS VERIFICATION. |
| `fixtures/domains/roads-rail-trade/valid/README.md` | not found in current search | Dedicated Roads / Rail / Trade valid fixture lane NEEDS VERIFICATION. |

## Correct nearby lanes

| Need | Preferred lane |
|---|---|
| Flat Transport compatibility schemas | `schemas/contracts/v1/transport/` |
| Path-conflicted domain Transport scaffolds | `schemas/contracts/v1/domains/transport/` |
| Parent Roads / Rail / Trade schema context | `schemas/contracts/v1/domains/roads-rail-trade/` |
| Roads / Rail / Trade semantic meaning | `contracts/domains/roads-rail-trade/` |
| Transport semantic meaning, if retained | `contracts/domains/transport/` after path review |
| Valid examples | Fixture lane NEEDS VERIFICATION |
| Expected outputs or golden cases | Fixture lane NEEDS VERIFICATION |
| Schema test code | `tests/schemas/` or accepted project test root |
| Validator implementation | `tools/validators/` |
| Roads / Rail / Trade policy posture | `policy/domains/roads-rail-trade/` or accepted policy lane |
| Release, correction, rollback decisions | `release/` |

## What belongs here

- This README.
- Compatibility notes for this valid schema-test path.
- Migration notes if historical valid transport schema tests are discovered here.
- Temporary mirror notes while `transport` versus Roads / Rail / Trade and `domains/` versus flat-path placement are unresolved.

## What does not belong here

- Canonical `.schema.json` files.
- Valid fixture JSON, YAML, GeoJSON, graph, or expected-output files unless an accepted migration assigns them here.
- Real road, rail, route, corridor, crossing, facility, operator, schedule, source, lifecycle, graph, map, tile, or release payloads.
- Graph projections, public map payloads, source-system exports, public tiles, dashboards, screenshots, generated summaries, or direct model-runtime output.
- Policy rules, policy decisions, rights approvals, release records, receipts, proofs, emitted validation reports, validator code, runtime code, package code, or API/UI outputs.
- Claims that Transport or Roads / Rail / Trade data is evidence-supported, topology-valid, geometry-valid, source-supported, policy-approved, released, legally authoritative, routing-safe, public-safe, or domain truth merely because a payload passes a schema test.

## Compatibility rules

| Rule | Requirement |
|---|---|
| Keep path conflict visible | Do not hide the unresolved `transport` vs `roads-rail-trade` and flat-vs-domain lane conflict. |
| Keep schemas in schema lanes | Transport and Roads / Rail / Trade schemas belong in accepted schema homes, not in this test guardrail. |
| Keep fixtures in fixtures | Valid examples should live in a verified fixture lane unless an accepted migration says otherwise. |
| Shape is not route truth | Passing schema validation does not prove route, corridor, network, geometry, source, operator, or legal status truth. |
| Graphs are derivatives | Valid graph-like outputs must not replace canonical route, segment, membership, facility, or source-bound records. |
| Tests are not publication | Test outcomes do not publish data, authorize map display, provide routing advice, or approve release. |
| Avoid parallel test roots | Add test files only to accepted test homes unless a migration note explains the exception. |

## Validation

```bash
find schemas/tests/valid/domains/transport -maxdepth 4 -type f | sort
find schemas/tests/invalid/domains/transport -maxdepth 4 -type f 2>/dev/null | sort
find schemas/contracts/v1/transport schemas/contracts/v1/domains/transport schemas/contracts/v1/domains/roads-rail-trade -maxdepth 4 -type f 2>/dev/null | sort
find fixtures/domains/transport fixtures/domains/roads-rail-trade -maxdepth 5 -type f 2>/dev/null | sort
pytest tests/schemas tests/contract || true
```

Replace `|| true` with fail-closed CI behavior once the relevant test paths are confirmed.

## Open questions

| Question | Status |
|---|---|
| Should `schemas/tests/valid/domains/transport/` remain as a compatibility guardrail or be retired? | NEEDS VERIFICATION |
| Are there historical references that expect valid Transport schema tests under this path? | NEEDS VERIFICATION |
| Which fixture lane should own valid Transport or Roads / Rail / Trade examples? | NEEDS VERIFICATION |
| Should valid Transport tests live under a Roads / Rail / Trade child path instead? | NEEDS VERIFICATION |
| Which route, corridor, network, geometry, source-role, decision-envelope, rights, release-readiness, legal-status, graph-projection, and public-map cases must be represented as valid tests? | NEEDS VERIFICATION |

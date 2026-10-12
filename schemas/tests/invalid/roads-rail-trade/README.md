# `schemas/tests/invalid/roads-rail-trade/` — Roads / Rail / Trade Invalid Schema Test Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-tests-invalid-roads-rail-trade-readme
title: schemas/tests/invalid/roads-rail-trade/ README
type: readme; compatibility-index; invalid-test-placement-guardrail
version: v0.1
status: draft; empty-invalid-test-path; non-domain-test-path; roads-rail-trade-slug-conflicted; NEEDS VERIFICATION
updated: 2026-07-04
policy_label: public
tags: [kfm, schemas, tests, invalid, roads-rail-trade, transport, fixtures, route, corridor, rail, trade, network, compatibility]
[/KFM_META_BLOCK_V2] -->

## Purpose

`schemas/tests/invalid/roads-rail-trade/` is a README-only compatibility guardrail for invalid Roads / Rail / Trade schema-test placement.

The inspected Roads / Rail / Trade schema lane lives at `schemas/contracts/v1/domains/roads-rail-trade/`.

The inspected related Transport invalid-test guardrail lives at `schemas/tests/invalid/domains/transport/`.

## Status

| Item | Status |
|---|---|
| README | present |
| Direct invalid test files found under this path | none found in current search |
| Current role | compatibility guardrail |
| Placement | NEEDS VERIFICATION |
| Path posture | non-`domains/` test path; keep slug/path conflict visible |

## Boundary

This directory is not the Roads / Rail / Trade schema family, Transport schema authority, fixture authority, policy authority, validator implementation, CI configuration, emitted test-result store, data root, graph root, map root, or release root.

It should not contain canonical Roads / Rail / Trade schemas, route records, corridor records, rail records, source records, lifecycle data, graph projection outputs, public map payloads, release records, or validator code while accepted homes remain separate.

A failing or passing test here would prove only the tested shape behavior. It would not prove route truth, corridor truth, network truth, source authority, geometry validity, topology validity, policy approval, release readiness, legal road status, routing advice, or public-safety.

## Current inventory

| Path | Status | Notes |
|---|---|---|
| `schemas/tests/invalid/roads-rail-trade/README.md` | present | Empty file expanded by this README. |
| `schemas/tests/invalid/roads-rail-trade/*` | not found in current search | No direct invalid test files were found under this path. |
| `schemas/tests/invalid/domains/transport/README.md` | present | Inspected related Transport invalid schema-test guardrail. |
| `schemas/contracts/v1/domains/roads-rail-trade/README.md` | present | Inspected Roads / Rail / Trade domain schema index. |
| `fixtures/domains/roads-rail-trade/invalid/README.md` | not found in current search | No matching fixture lane confirmed. |
| `fixtures/domains/transport/invalid/README.md` | not found in current search | No matching fixture lane confirmed. |

## Correct nearby lanes

| Need | Preferred lane |
|---|---|
| Roads / Rail / Trade schema shape | `schemas/contracts/v1/domains/roads-rail-trade/` |
| Related flat Transport compatibility schemas | `schemas/contracts/v1/transport/` |
| Path-conflicted domain Transport scaffolds | `schemas/contracts/v1/domains/transport/` |
| Roads / Rail / Trade semantic meaning | `contracts/domains/roads-rail-trade/` |
| Invalid examples | Fixture lane NEEDS VERIFICATION |
| Schema test code | `tests/schemas/` or accepted project test root |
| Validator implementation | `tools/validators/` |
| Roads / Rail / Trade policy posture | `policy/domains/roads-rail-trade/` or accepted policy lane |
| Release, correction, rollback decisions | `release/` |

## What belongs here

- This README.
- Compatibility notes for this invalid schema-test path.
- Migration notes if historical Roads / Rail / Trade invalid schema tests are discovered here.
- Temporary mirror notes while `roads-rail-trade` versus `transport` and `domains/` versus flat-path placement are unresolved.

## What does not belong here

- Canonical `.schema.json` files.
- Invalid fixture JSON files unless an accepted migration assigns them here.
- Real road, rail, route, corridor, crossing, facility, operator, schedule, source, lifecycle, graph, map, tile, or release payloads.
- Graph projections, public map payloads, source-system exports, public tiles, dashboards, screenshots, generated summaries, or direct model-runtime output.
- Policy rules, policy decisions, rights approvals, release records, receipts, proofs, emitted validation reports, validator code, runtime code, package code, or API/UI outputs.
- Claims that Roads / Rail / Trade data is valid, invalid, source-supported, topology-valid, policy-approved, released, legally authoritative, routing-safe, or public-safe merely because this path exists.

## Compatibility rules

| Rule | Requirement |
|---|---|
| Keep path conflict visible | Do not hide unresolved `roads-rail-trade` vs `transport` or `domains/` vs flat-path drift. |
| Keep schemas in schema lanes | Roads / Rail / Trade schemas belong in accepted schema homes, not in this test guardrail. |
| Keep fixtures in fixtures | Invalid examples should live in a verified fixture lane unless an accepted migration says otherwise. |
| Shape is not route truth | Test outcomes do not prove route, corridor, network, geometry, source, operator, or legal status truth. |
| Tests are not publication | Test outcomes do not publish data, authorize map display, provide routing advice, or approve release. |
| Avoid parallel test roots | Add test files only to accepted test homes unless a migration note explains the exception. |

## Validation

```bash
find schemas/tests/invalid/roads-rail-trade -maxdepth 4 -type f | sort
find schemas/tests/invalid/domains/transport -maxdepth 4 -type f 2>/dev/null | sort
find schemas/contracts/v1/domains/roads-rail-trade schemas/contracts/v1/transport schemas/contracts/v1/domains/transport -maxdepth 4 -type f 2>/dev/null | sort
find fixtures/domains/roads-rail-trade fixtures/domains/transport -maxdepth 5 -type f 2>/dev/null | sort
pytest tests/schemas tests/contract || true
```

Replace `|| true` with fail-closed CI behavior once the relevant test paths are confirmed.

## Open questions

| Question | Status |
|---|---|
| Should `schemas/tests/invalid/roads-rail-trade/` remain as a compatibility guardrail or be retired? | NEEDS VERIFICATION |
| Should invalid Roads / Rail / Trade schema tests live under `schemas/tests/invalid/domains/roads-rail-trade/` instead? | NEEDS VERIFICATION |
| Which fixture lane should own invalid Roads / Rail / Trade or Transport examples? | NEEDS VERIFICATION |
| Which route, corridor, network, geometry, source-role, decision-envelope, rights, release-readiness, legal-status, and public-map cases must be represented as invalid tests? | NEEDS VERIFICATION |

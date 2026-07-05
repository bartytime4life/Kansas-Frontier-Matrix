# `schemas/tests/valid/roads-rail-trade/` — Roads / Rail / Trade Valid Schema Test Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-tests-valid-roads-rail-trade-readme
title: schemas/tests/valid/roads-rail-trade/ README
type: readme; compatibility-index; valid-test-placement-guardrail
version: v0.1
status: draft; empty-valid-test-path; non-domain-test-path; roads-rail-trade-slug-conflicted; NEEDS VERIFICATION
updated: 2026-07-04
policy_label: public
tags: [kfm, schemas, tests, valid, roads-rail-trade, transport, fixtures, route, corridor, rail, trade, network, compatibility]
[/KFM_META_BLOCK_V2] -->

## Purpose

`schemas/tests/valid/roads-rail-trade/` is a README-only compatibility guardrail for valid Roads / Rail / Trade schema-test placement.

The related non-domain invalid-test guardrail lives at `schemas/tests/invalid/roads-rail-trade/`.

The inspected related Transport valid-test guardrail lives at `schemas/tests/valid/domains/transport/`.

No matching `fixtures/domains/roads-rail-trade/valid/README.md` or `fixtures/domains/transport/valid/README.md` was confirmed in current search.

## Status

| Item | Status |
|---|---|
| README | present |
| Direct valid test files found under this path | none found in current search |
| Current role | compatibility guardrail |
| Placement | NEEDS VERIFICATION |
| Path posture | non-`domains/` test path; keep `roads-rail-trade` vs `transport` conflict visible |
| Dedicated valid fixture lane | not confirmed in current search |

## Boundary

This directory is not the Roads / Rail / Trade schema family, Transport schema authority, fixture authority, policy authority, validator implementation, CI configuration, emitted test-result store, data root, graph root, map root, or release root.

It should not contain canonical Roads / Rail / Trade schemas, route records, corridor records, rail records, road records, source records, lifecycle data, graph projection outputs, public map payloads, release records, direct model-runtime output, or validator code while accepted homes remain separate.

A passing valid test here would prove only the tested shape behavior. It would not prove route truth, corridor truth, network truth, source authority, geometry validity, topology validity, operator truth, legal road status, policy approval, release readiness, routing safety, implementation proof, or public-safety.

## Current inventory

| Path | Status | Notes |
|---|---|---|
| `schemas/tests/valid/roads-rail-trade/README.md` | present | Empty file expanded by this README. |
| `schemas/tests/valid/roads-rail-trade/*` | not found in current search | No direct valid test files were found under this path. |
| `schemas/tests/invalid/roads-rail-trade/README.md` | present | Inspected related non-domain invalid schema-test guardrail. |
| `schemas/tests/valid/domains/transport/README.md` | present | Inspected related Transport valid schema-test guardrail. |
| `schemas/contracts/v1/domains/roads-rail-trade/README.md` | present by related evidence | Parent Roads / Rail / Trade schema lane; not reopened in this pass. |
| `schemas/contracts/v1/transport/README.md` | present by related evidence | Flat Transport compatibility schema lane; not reopened in this pass. |
| `schemas/contracts/v1/domains/transport/README.md` | present by related evidence | Path-conflicted Transport schema lane; not reopened in this pass. |
| `fixtures/domains/roads-rail-trade/valid/README.md` | not found in current search | Dedicated Roads / Rail / Trade valid fixture lane NEEDS VERIFICATION. |
| `fixtures/domains/transport/valid/README.md` | not found in current search | Dedicated Transport valid fixture lane NEEDS VERIFICATION. |

## Correct nearby lanes

| Need | Preferred lane |
|---|---|
| Roads / Rail / Trade schema shape | `schemas/contracts/v1/domains/roads-rail-trade/` |
| Related flat Transport compatibility schemas | `schemas/contracts/v1/transport/` |
| Path-conflicted domain Transport scaffolds | `schemas/contracts/v1/domains/transport/` |
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
- Migration notes if historical Roads / Rail / Trade valid schema tests are discovered here.
- Temporary mirror notes while `roads-rail-trade` versus `transport` and `domains/` versus flat-path placement are unresolved.

## What does not belong here

- Canonical `.schema.json` files.
- Valid fixture JSON, YAML, GeoJSON, graph, or expected-output files unless an accepted migration assigns them here.
- Real road, rail, route, corridor, crossing, facility, operator, schedule, source, lifecycle, graph, map, tile, or release payloads.
- Graph projections, public map payloads, source-system exports, public tiles, dashboards, screenshots, generated summaries, or direct model-runtime output.
- Policy rules, policy decisions, rights approvals, release records, receipts, proofs, emitted validation reports, validator code, runtime code, package code, or API/UI outputs.
- Claims that Roads / Rail / Trade or Transport data is evidence-supported, topology-valid, geometry-valid, source-supported, policy-approved, released, legally authoritative, routing-safe, public-safe, or domain truth merely because a payload passes a schema test.

## Compatibility rules

| Rule | Requirement |
|---|---|
| Keep path conflict visible | Do not hide unresolved `roads-rail-trade` vs `transport` or `domains/` vs flat-path drift. |
| Keep schemas in schema lanes | Roads / Rail / Trade and Transport schemas belong in accepted schema homes, not in this test guardrail. |
| Keep fixtures in fixtures | Valid examples should live in a verified fixture lane unless an accepted migration says otherwise. |
| Shape is not route truth | Passing schema validation does not prove route, corridor, network, geometry, source, operator, or legal status truth. |
| Graphs are derivatives | Valid graph-like outputs must not replace canonical route, segment, membership, facility, or source-bound records. |
| Tests are not publication | Test outcomes do not publish data, authorize map display, provide routing advice, or approve release. |
| Avoid parallel test roots | Add test files only to accepted test homes unless a migration note explains the exception. |

## Validation

```bash
find schemas/tests/valid/roads-rail-trade -maxdepth 4 -type f | sort
find schemas/tests/valid/domains/transport schemas/tests/invalid/roads-rail-trade -maxdepth 4 -type f 2>/dev/null | sort
find schemas/contracts/v1/domains/roads-rail-trade schemas/contracts/v1/transport schemas/contracts/v1/domains/transport -maxdepth 4 -type f 2>/dev/null | sort
find fixtures/domains/roads-rail-trade fixtures/domains/transport -maxdepth 5 -type f 2>/dev/null | sort
pytest tests/schemas tests/contract || true
```

Replace `|| true` with fail-closed CI behavior once the relevant test paths are confirmed.

## Open questions

| Question | Status |
|---|---|
| Should `schemas/tests/valid/roads-rail-trade/` remain as a compatibility guardrail or be retired? | NEEDS VERIFICATION |
| Should valid Roads / Rail / Trade schema tests live under `schemas/tests/valid/domains/roads-rail-trade/` instead? | NEEDS VERIFICATION |
| Which fixture lane should own valid Roads / Rail / Trade or Transport examples? | NEEDS VERIFICATION |
| Should valid Transport tests remain under `schemas/tests/valid/domains/transport/` or migrate to a Roads / Rail / Trade child path? | NEEDS VERIFICATION |
| Which route, corridor, network, geometry, source-role, decision-envelope, rights, release-readiness, legal-status, graph-projection, and public-map cases must be represented as valid tests? | NEEDS VERIFICATION |

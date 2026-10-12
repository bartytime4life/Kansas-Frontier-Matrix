<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/domains/roads-rail-trade/valid/authoring-guide
title: Roads, Rail and Trade valid fixture authoring guide
type: fixture-guide
version: v1
status: repository-grounded documentation; no new fixture payloads
owners: ["@bartytime4life"]
created: 2026-10-08
updated: 2026-10-08
policy_label: synthetic-public-safe-only; no-network; no-authority
current_path: fixtures/domains/roads-rail-trade/valid/PLACEHOLDER.md
owning_root: fixtures/
responsibility: Explain the actual roads-rail-trade valid inventory, authoring boundaries and existing consumer routes.
truth_posture: CONFIRMED inventory and code/test pointers inspected at main@ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe; no new runtime acceptance claimed.
related:
  - ../../../README.md
  - ../../../../tests/schemas/test_corridor_route_contract.py
[/KFM_META_BLOCK_V2] -->

# Roads, Rail and Trade: valid fixture guide

Describe the positive-input lane for a specific declared profile. Valid means the input satisfies that bounded schema and semantic contract; it does not mean the source is admitted, complete or ready for publication.

## Current inventory

The historic_route_claim child contains chisholm_trail.json, pony_express.json and santa_fe_trail.json, but each is a PROPOSED inventory object with a path and source-document pointer. They are not validated historic-route claim payloads. The road_segment, rail_segment and wzdx_v4 children contain only .gitkeep. Thus this generic lane has no operational positive route fixture coverage; use the concrete corridor_route family below.

The filename is retained for existing path references and workflow checks. This page replaces its former one-line marker with operational guidance; it does not create payloads or change test coverage.

## Domain rules to preserve

The implemented corridor-route family distinguishes historic candidates and unresolved evidence from live routing authority. Its negatives reject embedded segment truth, missing temporal uncertainty, sensitive geometry and derived geocodes treated as authoritative. The frontier-route trust-status family keeps public projection, visibility and release identity aligned without raw-geometry leakage.

Use the corridor-route fixture profile for a bounded historic claim with temporal uncertainty and evidence references. Do not infer road access, operational status, legal designation or navigation safety from route names or OSM/GNIS context.

## Author or revise a case

1. Start from the closest concrete positive family, not a free-form object or an inventory stub.
2. Keep synthetic identity and references, declared source role, time semantics and domain limitations intact. Change only fields required by the scenario.
3. Name the actual schema and semantic consumer and add a companion negative case for the boundary being demonstrated.
4. Update the consuming test's explicit inventory or manifest when required. Record which outcome is expected; a valid candidate may intentionally produce ABSTAIN or HOLD.

## Existing evidence and consumers

- [fixtures/domains/roads-rail-trade/corridor_route/valid/valid_historic_candidate.json](../corridor_route/valid/valid_historic_candidate.json)
- [fixtures/domains/roads-rail-trade/corridor_route/valid/valid_unresolved_evidence.json](../corridor_route/valid/valid_unresolved_evidence.json)
- [fixtures/domains/roads-rail-trade/frontier_route_trust_status/valid/public-safe.json](../frontier_route_trust_status/valid/public-safe.json)
- [Primary bounded test](../../../../tests/schemas/test_corridor_route_contract.py)
- [Related regression coverage](../../../../tests/domains/roads-rail-trade/test_roads_rail_trade_smoke.py)
- [Concrete validator](../../../../tools/validators/domains/roads-rail-trade/validate_corridor_route.py)

After installing the repository's declared test dependencies, run the relevant existing tests from the repository root:

```bash
KFM_NO_NETWORK=1 PYTHONDONTWRITEBYTECODE=1 python -m pytest -q -p no:cacheprovider tests/schemas/test_corridor_route_contract.py tests/domains/roads-rail-trade/test_roads_rail_trade_smoke.py
```

This command exercises the linked families, not an empty directory or every domain promise. It is provided as a contributor workflow and was not run for this documentation-only edit. Inspect the test assertions before extending their scope; README names and schema-file syntax checks do not establish behavioral coverage.

## Review boundary

Use only small synthetic, public-safe examples under this public fixture root. Keep real provider captures and sensitive records in their governed data lanes. Passing a fixture proves the named implementation's response to those bytes only; admission, policy decisions, source activation, release, deployment and publication remain separate.

Placement and owner routing follow [the reusable fixture-root guide](../../../README.md) and [CODEOWNERS](../../../../.github/CODEOWNERS). The existing [domain fixture index](../README.md) supplies broader context; this guide does not move any source, contract, policy or release responsibility.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/domains/agriculture/valid/authoring-guide
title: Agriculture valid fixture authoring guide
type: fixture-guide
version: v1
status: repository-grounded documentation; no new fixture payloads
owners: ["@bartytime4life"]
created: 2026-10-08
updated: 2026-10-08
policy_label: synthetic-public-safe-only; no-network; no-authority
current_path: fixtures/domains/agriculture/valid/PLACEHOLDER.md
owning_root: fixtures/
responsibility: Explain the actual agriculture valid inventory, authoring boundaries and existing consumer routes.
truth_posture: CONFIRMED inventory and code/test pointers inspected at main@ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe; no new runtime acceptance claimed.
related:
  - ../../../README.md
  - ../../../../tests/domains/agriculture/test_public_safe_map_feature.py
[/KFM_META_BLOCK_V2] -->

# Agriculture: valid fixture guide

Describe the positive-input lane for a specific declared profile. Valid means the input satisfies that bounded schema and semantic contract; it does not mean the source is admitted, complete or ready for publication.

## Current inventory

This directory contains documentation only at the inspected source revision; it has no executable valid payloads. It does not provide valid fixture coverage merely because the lane or this file exists. Concrete sibling families below have their own consumers and must be evaluated separately.

The filename is retained for existing path references and workflow checks. This page replaces its former one-line marker with operational guidance; it does not create payloads or change test coverage.

## Domain rules to preserve

The implemented public-safe map-feature family separates observed aggregates from derived crop rotation, modeled soil/crop suitability and context-only irrigation or supply-chain features. Field boundaries, farm/operator identity and proprietary yield detail are excluded from that public-safe profile. NDVI arithmetic is tested separately; a vegetation index does not become crop yield or a field-level observation.

Choose one declared object family and generalized support key. Keep observed, derived, modeled and context-only roles consistent with that family's profile; bind vintage, freshness and source references independently.

## Author or revise a case

1. Start from the closest concrete positive family, not a free-form object or an inventory stub.
2. Keep synthetic identity and references, declared source role, time semantics and domain limitations intact. Change only fields required by the scenario.
3. Name the actual schema and semantic consumer and add a companion negative case for the boundary being demonstrated.
4. Update the consuming test's explicit inventory or manifest when required. Record which outcome is expected; a valid candidate may intentionally produce ABSTAIN or HOLD.

## Existing evidence and consumers

- [fixtures/domains/agriculture/public_safe_map_feature/cases.json](../public_safe_map_feature/cases.json)
- [fixtures/domains/agriculture/public_safe_map_feature/crop_observation.json](../public_safe_map_feature/crop_observation.json)
- [fixtures/domains/agriculture/ndvi_delta_computation/cases.json](../ndvi_delta_computation/cases.json)
- [Primary bounded test](../../../../tests/domains/agriculture/test_public_safe_map_feature.py)
- [Related regression coverage](../../../../tests/domains/agriculture/test_ndvi_delta_computation.py)
- [Concrete validator](../../../../tools/validators/domains/agriculture/validate_public_safe_map_feature.py)

After installing the repository's declared test dependencies, run the relevant existing tests from the repository root:

```bash
KFM_NO_NETWORK=1 PYTHONDONTWRITEBYTECODE=1 python -m pytest -q -p no:cacheprovider tests/domains/agriculture/test_public_safe_map_feature.py tests/domains/agriculture/test_ndvi_delta_computation.py
```

This command exercises the linked families, not an empty directory or every domain promise. It is provided as a contributor workflow and was not run for this documentation-only edit. Inspect the test assertions before extending their scope; README names and schema-file syntax checks do not establish behavioral coverage.

## Review boundary

Use only small synthetic, public-safe examples under this public fixture root. Keep real provider captures and sensitive records in their governed data lanes. Passing a fixture proves the named implementation's response to those bytes only; admission, policy decisions, source activation, release, deployment and publication remain separate.

Placement and owner routing follow [the reusable fixture-root guide](../../../README.md) and [CODEOWNERS](../../../../.github/CODEOWNERS). The existing [domain fixture index](../README.md) supplies broader context; this guide does not move any source, contract, policy or release responsibility.

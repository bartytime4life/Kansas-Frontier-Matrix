<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/domains/settlements-infrastructure/valid/authoring-guide
title: Settlements and Infrastructure valid fixture authoring guide
type: fixture-guide
version: v1
status: repository-grounded documentation; no new fixture payloads
owners: ["@bartytime4life"]
created: 2026-10-08
updated: 2026-10-08
policy_label: synthetic-public-safe-only; no-network; no-authority
current_path: fixtures/domains/settlements-infrastructure/valid/PLACEHOLDER.md
owning_root: fixtures/
responsibility: Explain the actual settlements-infrastructure valid inventory, authoring boundaries and existing consumer routes.
truth_posture: CONFIRMED inventory and code/test pointers inspected at main@ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe; no new runtime acceptance claimed.
related:
  - ../../../README.md
  - ../../../../tests/validators/domains/settlements-infrastructure/test_domain_feature_identity.py
[/KFM_META_BLOCK_V2] -->

# Settlements and Infrastructure: valid fixture guide

Describe the positive-input lane for a specific declared profile. Valid means the input satisfies that bounded schema and semantic contract; it does not mean the source is admitted, complete or ready for publication.

## Current inventory

Two domain-level examples are present: valid_1_settlement.json (Settlement, historic-place role) and valid_2_service_area.json (synthetic aggregate ServiceArea footprint). The ServiceArea example is deliberately sparse and is not a fully bound identity-validator positive. For executable identity polarity, use the separate domain_feature_identity fixtures linked below. The existing README describes the weaker proposed-schema shape expectation.

The filename is retained for existing path references and workflow checks. This page replaces its former one-line marker with operational guidance; it does not create payloads or change test coverage.

## Domain rules to preserve

The generic valid lane contains Settlement and ServiceArea examples, while domain_feature_identity has two fully bound positive identity envelopes and a collapsed-family negative. The bounded identity validator checks object family, feature role, source role, digests, source key and temporal scope. The paired proposed schema remains permissive; schema-document validity is not candidate semantics or infrastructure policy clearance.

Distinguish settlement-side place identity from infrastructure-side assets and service areas. Bind source role, source/normalized digests, evidence and time when exercising the identity validator. An aggregate footprint is not facility vulnerability or condition data.

## Author or revise a case

1. Start from the closest concrete positive family, not a free-form object or an inventory stub.
2. Keep synthetic identity and references, declared source role, time semantics and domain limitations intact. Change only fields required by the scenario.
3. Name the actual schema and semantic consumer and add a companion negative case for the boundary being demonstrated.
4. Update the consuming test's explicit inventory or manifest when required. Record which outcome is expected; a valid candidate may intentionally produce ABSTAIN or HOLD.

## Existing evidence and consumers

- [fixtures/domains/settlements-infrastructure/domain_feature_identity/valid_settlement.json](../domain_feature_identity/valid_settlement.json)
- [fixtures/domains/settlements-infrastructure/domain_feature_identity/valid_infrastructure_asset.json](../domain_feature_identity/valid_infrastructure_asset.json)
- [fixtures/domains/settlements-infrastructure/domain_feature_identity/invalid_collapsed_object_family.json](../domain_feature_identity/invalid_collapsed_object_family.json)
- [Primary bounded test](../../../../tests/validators/domains/settlements-infrastructure/test_domain_feature_identity.py)
- [Related regression coverage](../../../../tests/domains/settlements-infrastructure/test_settlements_infrastructure_smoke.py)
- [Concrete validator](../../../../tools/validators/domains/settlements-infrastructure/validate_domain_feature_identity.py)

After installing the repository's declared test dependencies, run the relevant existing tests from the repository root:

```bash
KFM_NO_NETWORK=1 PYTHONDONTWRITEBYTECODE=1 python -m pytest -q -p no:cacheprovider tests/validators/domains/settlements-infrastructure/test_domain_feature_identity.py tests/domains/settlements-infrastructure/test_settlements_infrastructure_smoke.py
```

This command exercises the linked families, not an empty directory or every domain promise. It is provided as a contributor workflow and was not run for this documentation-only edit. Inspect the test assertions before extending their scope; README names and schema-file syntax checks do not establish behavioral coverage.

## Review boundary

Use only small synthetic, public-safe examples under this public fixture root. Keep real provider captures and sensitive records in their governed data lanes. Passing a fixture proves the named implementation's response to those bytes only; admission, policy decisions, source activation, release, deployment and publication remain separate.

Placement and owner routing follow [the reusable fixture-root guide](../../../README.md) and [CODEOWNERS](../../../../.github/CODEOWNERS). The existing [domain fixture index](../README.md) supplies broader context; this guide does not move any source, contract, policy or release responsibility.

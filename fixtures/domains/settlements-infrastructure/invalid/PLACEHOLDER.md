<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/domains/settlements-infrastructure/invalid/authoring-guide
title: Settlements and Infrastructure invalid fixture authoring guide
type: fixture-guide
version: v1
status: repository-grounded documentation; no new fixture payloads
owners: ["@bartytime4life"]
created: 2026-10-08
updated: 2026-10-08
policy_label: synthetic-public-safe-only; no-network; no-authority
current_path: fixtures/domains/settlements-infrastructure/invalid/PLACEHOLDER.md
owning_root: fixtures/
responsibility: Explain the actual settlements-infrastructure invalid inventory, authoring boundaries and existing consumer routes.
truth_posture: CONFIRMED inventory and code/test pointers inspected at main@ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe; no new runtime acceptance claimed.
related:
  - ../../../README.md
  - ../../../../tests/validators/domains/settlements-infrastructure/test_domain_feature_identity.py
[/KFM_META_BLOCK_V2] -->

# Settlements and Infrastructure: invalid fixture guide

Describe safe negative inputs that violate a named schema, role, time, evidence or privacy invariant. Each case needs the expected finite failure/hold and the checker that enforces it.

## Current inventory

Two synthetic negatives and their .expected_error.txt companions are present: invalid_1_missing_source_role and invalid_2_public_condition_leak. Their sidecars explicitly describe target gaps under the permissive proposed schema, not exact current outputs of every checker. The separate identity validator now rejects missing source role/time using REQUIRED_TEXT_INVALID:source_role and TEMPORAL_SCOPE_MISSING; it is not a full condition-disclosure policy gate.

The filename is retained for existing path references and workflow checks. This page replaces its former one-line marker with operational guidance; it does not create payloads or change test coverage.

## Domain rules to preserve

The generic valid lane contains Settlement and ServiceArea examples, while domain_feature_identity has two fully bound positive identity envelopes and a collapsed-family negative. The bounded identity validator checks object family, feature role, source role, digests, source key and temporal scope. The paired proposed schema remains permissive; schema-document validity is not candidate semantics or infrastructure policy clearance.

Use an otherwise bound identity envelope for missing source role or time tests, and assert current REQUIRED_TEXT_INVALID:source_role or TEMPORAL_SCOPE_MISSING diagnostics. Policy denial for public condition/vulnerability detail is separate from identity-field validation.

## Author or revise a case

1. Copy a fully understood synthetic positive from the same profile and change one invariant.
2. State the precise input defect and expected code/status. Avoid introducing several unrelated failures that obscure which guard matters.
3. Compare exact stable findings using the family's existing sidecar/manifest convention. Keep malformed-input errors distinct from semantic denial, abstention or hold.
4. Verify that diagnostics omit candidate values and that no network, source mutation, release or publication effect occurs. Pair the case with an unchanged positive control.

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

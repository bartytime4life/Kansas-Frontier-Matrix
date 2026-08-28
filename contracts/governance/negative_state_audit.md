<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/negative-state-audit
title: NegativeStateAudit Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive
owners: OWNER_TBD — governance steward · evidence steward · validation steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; fixture-only; non-authoritative
related:
  - ../../schemas/contracts/v1/governance/negative_state_audit.schema.json
  - ../../fixtures/contracts/v1/governance/negative_state_audit/cases.json
  - ../../tools/validators/governance/validate_negative_state_audit.py
  - ../../tests/validators/governance/test_validate_negative_state_audit.py
tags: [kfm, governance, negative-state, evidence, policy, validation, release]
[/KFM_META_BLOCK_V2] -->

# NegativeStateAudit Contract

`NegativeStateAudit` is a deterministic, fixture-only governance profile that proves three outward states remain distinct: one approved released artifact, one policy denial, and one citation or validation failure. It implements the Pass 11 three-way negative-state audit without creating a public route, policy decision, evidence object, lifecycle transition, release, or publication authority.

## Status and boundary

| Field | Value |
|---|---|
| Profile | `kfm.governance.negative-state-audit.v1` |
| Execution | `FIXTURE_ONLY_NO_NETWORK` |
| Validator outcomes | `PASS`, `DENY`, `ERROR` |
| Authority | `NONE` |

A `PASS` proves only local fixture shape, deterministic identity, and separation among the three declared states. It does not authenticate referenced evidence, policy, validation, citation, artifact, or release objects.

## Required case matrix

Each packet contains exactly one case of each kind:

1. `APPROVED_ARTIFACT`
   - outward outcome is `ANSWER`;
   - policy, validation, and citation outcomes are all passing;
   - lifecycle state is `PUBLISHED`;
   - evidence, policy, validation, citation, artifact, and release references are present;
   - no failure reference or failure reason is present.
2. `POLICY_DENIAL`
   - outward outcome is `DENY`;
   - lifecycle state is `QUARANTINE`;
   - policy outcome is `DENY` and points to a policy decision;
   - validation and citation are `NOT_EVALUATED`;
   - no artifact or release manifest is exposed;
   - at least one stable reason code is present.
3. `CITATION_OR_VALIDATION_FAILURE`
   - outward outcome is `ABSTAIN` or `ERROR`;
   - lifecycle state is `WORK` or `QUARANTINE`;
   - citation or validation is explicitly `FAIL` or `ERROR`;
   - a failure report is present;
   - no artifact or release manifest is exposed;
   - at least one stable reason code is present.

## Invariants

- the packet declares deterministic execution and no network access;
- the three case kinds are present exactly once and case IDs are unique;
- a denied or failed case cannot carry a released artifact or release manifest;
- an approved case cannot pass without resolvable evidence and release references;
- `ABSTAIN`, `DENY`, and `ERROR` are legitimate finite outcomes, not presentation defects;
- `spec_hash` binds the complete packet except the `spec_hash` field through the repository RFC 8785 JCS plus SHA-256 implementation;
- malformed shape or identity returns `ERROR`; trust-boundary overclaim returns `DENY`.

## Directory Rules basis

Accepted ADR-0029 and Directory Rules v2 place cross-cutting governance meaning in `contracts/governance/`, machine shape in `schemas/contracts/v1/governance/`, synthetic examples in `fixtures/contracts/v1/governance/`, executable validation in `tools/validators/governance/`, enforceability in `tests/validators/governance/`, CI in `.github/workflows/`, source adaptation in `docs/intake/exploratory/`, and AI-authoring provenance in `data/receipts/generated/`. No new root or parallel evidence, policy, release, proof, receipt, or publication home is introduced.

## Validation

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python -m unittest \
  tests.validators.governance.test_validate_negative_state_audit --verbose

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/governance/validate_negative_state_audit.py --fixtures
```

## Rollback

Before merge, close the draft pull request and abandon its feature branch. After an authorized merge, revert the additive commit. This inactive profile creates no source, evidence, policy, lifecycle, release, deployment, cache, or public state requiring operational cleanup.

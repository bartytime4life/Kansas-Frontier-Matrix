<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/policy/sovereignty-exception-receipt
title: SovereigntyExceptionReceipt Candidate Contract
type: contract
version: v1.0.0
status: proposed-inactive
owners: OWNER_TBD — Sovereignty steward · Policy steward · Review steward · Contract steward
created: 2026-08-09
updated: 2026-08-09
policy_label: restricted-review; fixture-only; non-authoritative
related:
  - ../../schemas/contracts/v1/policy/sovereignty_exception_receipt.schema.json
  - ../../fixtures/contracts/v1/policy/sovereignty_exception_receipt/
  - ../../tools/validators/policy/validate_sovereignty_exception_receipt.py
  - ../../tests/validators/test_validate_sovereignty_exception_receipt.py
  - conditional_decision_closure.md
  - ../governance/ReviewRecord.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, policy, sovereignty, exception, review, provenance, receipt, no-authority]
notes:
  - "Records an asserted external decision; it cannot create or authenticate exception authority."
  - "A RECORDED_APPROVED fixture remains blocked from execution until separate policy, access, release, and runtime gates act."
[/KFM_META_BLOCK_V2] -->

# SovereigntyExceptionReceipt Candidate Contract

> **Purpose.** Make a proposed sovereignty or sensitive-release exception explicit, typed, reason-coded, time-bounded, review-bound, and provenance-bound so an implicit UI or pipeline override cannot masquerade as governed authority.

## Status and authority boundary

| Field | Value |
|---|---|
| Contract status | `PROPOSED_INACTIVE` |
| Execution mode | `FIXTURE_ONLY` |
| Machine shape | `schemas/contracts/v1/policy/sovereignty_exception_receipt.schema.json` |
| Validator | `tools/validators/policy/validate_sovereignty_exception_receipt.py` |
| Policy, review, access, release, or publication authority | None |

A passing `RECORDED_APPROVED` fixture means only that the record points to a separate PolicyDecision, ReviewRecord set, approver roster, provenance activity, evidence, expiry, and obligations. This validator does not authenticate any referenced actor or record and does not grant an exception.

## Source-derived gap and existing-authority integration

Pass 32 card `KFM-P32-IDEA-0007` proposes typed, reason-coded, steward-approved sovereignty exceptions recorded as PROV events rather than implicit overrides. Current repository evidence already defines PolicyDecision, conditional-obligation closure, ReviewRecord meaning, PROV catalog lanes, and generated receipt boundaries. This profile binds references to those families; it does not redefine or replace them.

## Finite dispositions

| Disposition | Required binding | Local meaning |
|---|---|---|
| `PENDING_REVIEW` | No decision, review, roster, activity, expiry, or obligations yet | `ABSTAIN`; the requested exception is unresolved. |
| `RECORDED_APPROVED` | Separate policy decision, reviews, roster, provenance activity, evidence, expiry, and enforceable obligations | The external approval assertion is coherently recorded; no operation is authorized here. |
| `RECORDED_DENIED` | Separate policy decision, reviews, roster, provenance activity, and evidence | The external denial assertion is coherently recorded. |
| `EXPIRED` | Previously recorded decision plus expiry at or before record time | The exception record is no longer current and cannot be silently reused. |

## Fail-closed rules

- All reference and reason arrays are sorted and unique.
- Recorded dispositions require external policy and review references; the receipt cannot reference itself as authority.
- Approved exceptions require `AUDIT_REQUIRED` and `EXPIRY_ENFORCED`.
- Approved `EXPORT` also requires `NO_RAW_EGRESS`; approved `RELEASE_CANDIDATE` requires `GENERALIZED_OUTPUT_ONLY`.
- Requested, decided, recorded, and expiry times must be ordered consistently.
- Every authority-bearing effect is fixed false, including `exception_authority_created`, `policy_overridden`, `access_granted`, `release_authorized`, and `published`.

## Deterministic identity

RFC 8785 JCS plus SHA-256 is computed over all fields except `receipt_id` and `spec_hash`.

```text
spec_hash = SHA-256(JCS(identity subject))
receipt_id = "kfm://policy/sovereignty-exception-receipt/" + first 24 digest hex characters
```

## Directory Rules basis

Policy-object meaning remains in `contracts/policy/`; machine shape in `schemas/contracts/v1/policy/`; synthetic cases in `fixtures/contracts/v1/policy/`; reusable validation in `tools/validators/policy/`; tests in `tests/validators/`; CI in `.github/workflows/`; source mapping in `docs/intake/exploratory/`; and authoring accountability in `data/receipts/generated/`. A future emitted receipt would require separate placement review under `data/receipts/`, while a PROV projection would remain under the accepted catalog lane.

No policy bundle, reviewer registry, approver authority, PROV store, lifecycle write, release decision, capability, deployment, or publication surface is created.

## Rollback

Close the draft or revert the additive packet. The profile has no runtime consumer, live exception, policy decision, access grant, release, deployment, or public artifact to restore.

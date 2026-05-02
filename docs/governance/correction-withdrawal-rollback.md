# Correction, Withdrawal, and Rollback Governance

## KFM Meta Block V2
- status: draft fixture-backed governance slice
- mode: offline, deterministic, fail-closed

## Purpose
Defines append-only governance evidence for correcting, withdrawing, and rolling back promoted artifacts without mutating prior publication evidence.

## Lifecycle placement
After promotion evidence registry + replay verification; before any live publication control plane integration.

## Artifact separation model
- CorrectionNotice: append correction evidence only.
- WithdrawalNotice: preserve audit chain with authority.
- RollbackPlan + RollbackExecutionReceipt: reference prior governed release artifacts.
- PromotionCorrectionLedger + PublicCorrectionIndex: public-safe summaries and chain integrity.

## Correction vs Withdrawal vs Rollback
| Action | Mutates prior receipts | Requires authority | Requires prior decision/run refs |
|---|---|---|---|
| Correction | No | Yes | Yes |
| Withdrawal | No | Yes | Yes |
| Rollback | No | Yes | Yes |

## Append-only evidence chain diagram
`notice/receipt -> ledger entry hash -> ledger chain_hash`

## Fail-closed matrix
Missing reason, authority, registry ref, prior decision log, prior run receipt, unsafe path, unknown rollback target, or hash mismatch => validation fail.

## CLI examples
- `python tools/validators/governance/validate_correction_governance.py tests/fixtures/governance/corrections/valid/correction_notice_valid.json`
- `python tools/governance/plan_promotion_rollback.py <rollback_request.json>`
- `python tools/governance/build_correction_ledger.py <ordered-events...>`

## Fixture inventory
See `tests/fixtures/governance/corrections/{valid,invalid}`.

## Public-safety rules
Disallow RAW/WORK/QUARANTINE/private/candidate/secret/token paths for public index and rollback targets.

## Definition of done
All valid fixtures pass; invalid fixtures fail; deterministic plan/ledger hashes; policy tests pass when OPA is available.

## Rollback/correction rehearsal notes
Use local fixture receipt index only; no live Gatehouse, no live signatures, no live publication claims.

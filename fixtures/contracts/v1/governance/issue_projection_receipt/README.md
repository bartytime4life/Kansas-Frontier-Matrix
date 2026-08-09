# IssueProjectionReceipt fixtures

These fixtures exercise the proposed, inactive
`kfm.briefing.issue-projection-receipt.v1` profile.

## Valid

- `proposed-update.json` — one declared existing issue remains one bound open
  target and produces a dry-run `PROPOSED` update.
- `held-closed-target.json` — a closed projected target converts the declared
  update into `HOLD_FOR_DEPENDENCY`.
- `no-action.json` — no issue inventory is required and no operation is proposed.

## Invalid

- `mutation-attempted.json` — v1 cannot record an attempted operation.
- `digest-mismatch.json` — receipt bytes do not match the declared digest.
- `target-mismatch.json` — the effective target is outside the declared target.
- `missing-open-reason.json` — a proposed update omits the open-target reason.
- `inventory-reference-missing.json` — fixture inventory lacks its required ID.
- `reason-order.json` — reason codes are not canonical sorted unique values.

All content is synthetic. No fixture represents live GitHub state, issue
authorization, evidence, policy, review, proof, release, publication, or public
truth.

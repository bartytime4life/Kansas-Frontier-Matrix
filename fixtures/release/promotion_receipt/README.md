# PromotionReceipt fixtures

Synthetic, no-network fixtures for the PROPOSED release-scoped receipt profile.

## Valid lane

- `ready_not_applied.json` — all gates pass and the candidate is ready for accountable review, but no transition is declared applied.
- `denied_attempt.json` — rights/sensitivity denial blocks readiness and preserves the separate decision reference.
- `abstained_attempt.json` — unresolved proof/catalog support produces an auditable abstention.
- `applied_synthetic_transition.json` — synthetic all-pass example with the declarations required when `transition.applied` is true. It is not a real release.

## Invalid lane

Each invalid fixture has a sibling `.expected_code.txt` containing the stable semantic finding expected from the validator.

- `overall_status_mismatch.json`
- `digest_mismatch.json`
- `applied_without_decision.json`
- `applied_while_blocked.json`
- `applied_support_incomplete.json`

Fixtures prove shape and internal consistency only. They contain no real evidence, source activation, review authority, release credentials, public artifact, or publication state.

# Replay-Safe Effect Ledger Fixtures

These synthetic, no-network fixtures exercise the inactive `ReplaySafeEffectLedgerCandidate` profile.

| Lane | Expected outcome | Purpose |
|---|---|---|
| `valid/` | `PASS` | Prove one completed effect, duplicate suppression, failure before effect, and compensation as distinct finite records. |
| `schema_invalid/` | `ERROR` | Prove a missing governance boundary fails closed at the machine-shape gate. |
| `semantic_invalid/` | `DENY` | Prove attempt gaps, missing duplicate suppression, outcome upgrades, and unbound ledger entries are rejected. |

The fixtures do not connect to a queue, reserve a real effect, write a lifecycle lane, mutate data, or authorize review, release, deployment, publication, or public use. The manifest binds every file to its exact expected outcome and finding list.

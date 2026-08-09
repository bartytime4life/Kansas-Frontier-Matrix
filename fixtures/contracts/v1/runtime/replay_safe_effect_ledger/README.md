# Replay-Safe Effect Ledger Fixtures

These synthetic, no-network fixtures exercise the inactive `ReplaySafeEffectLedgerCandidate` profile.

| Lane | Expected outcome | Purpose |
|---|---|---|
| `valid/` | `PASS` | Prove one completed effect, post-completion release, per-delivery duplicate suppression, failure before completion, and compensation as distinct finite records. |
| `schema_invalid/` | `ERROR` | Prove a missing governance boundary fails closed at the machine-shape gate. |
| `semantic_invalid/` | `DENY` | Prove attempt gaps, missing or misbound duplicate suppression, pre-delivery ledger writes, compensation without completion, reservation timestamp/state drift, result upgrades, and unbound entries are rejected. |

The fixtures do not connect to a queue, reserve a real effect, write a lifecycle lane, mutate data, or authorize review, release, deployment, publication, or public use. The manifest binds every file to its exact expected outcome and finding list.

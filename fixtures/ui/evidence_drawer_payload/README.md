# EvidenceDrawerPayload fixtures

Reusable, synthetic, public-safe fixtures for the proposed UI projection at
`schemas/contracts/v1/ui/evidence_drawer_payload.schema.json`.

- `valid/` covers supported single-step and multi-step corrections, stale, superseded, denied, and error outcomes.
- `invalid/` pairs each JSON candidate with one `.expected_code.txt` containing
  the stable validator finding that must remain present.
- The corrected answer demonstrates that current support and superseded history
  remain distinct: each prior evidence record is audit-visible and cannot resolve as
  current truth; only the terminal correction target may support the current answer.

These fixtures contain no live source, protected geometry, credential, review,
release, or publication authority. A passing fixture run proves only the bounded
schema and semantic profile.

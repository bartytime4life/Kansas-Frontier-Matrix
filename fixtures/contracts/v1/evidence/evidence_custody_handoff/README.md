# Evidence Custody Handoff fixtures

Synthetic, no-network fixtures for `kfm.evidence-custody-handoff.v1`.

- `valid/` contains one closed mixed partition, one open quarantine partition, and one all-duplicate idempotency case.
- `semantic_invalid/` contains schema-valid records that violate deterministic identity, accounting, integrity, posture, or lifecycle rules.
- `invalid/` contains a schema-invalid record that attempts to claim publication authority.

No fixture contains real source bytes, exact geometry, credentials, living-person data, source activation, EvidenceBundle resolution, policy approval, lifecycle writes, release, or publication authority.

# Policy transform receipt fixtures

Synthetic, no-network fixtures for the proposed `PolicyTransformReceiptCandidate` profile.

- `valid/` contains three candidates bound to the landed satisfying generalize, combined,
  and suppress transform-plan simulations.
- `invalid/invalid_*.json` are true JSON-Schema negatives used by the repository-wide
  schema fixture convention.
- `invalid/semantic_invalid_*.json` remain schema-valid and exercise source binding,
  operation derivation, obligation closure, rollback, no-op, and identity failures.
- `expected_findings_manifest.json` fixes exact validator polarity and finding codes.

No record proves a runtime transform, policy decision, review, release, publication, or
public-use authority.

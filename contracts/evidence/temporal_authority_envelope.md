# Legacy evidence TemporalAuthorityEnvelope compatibility alias

Status: **LEGACY COMPATIBILITY / PROPOSED / non-authoritative**.

This path preserves the original evidence-local record shape, schema ID, diagnostics, fixtures, and `kfm:temporal-authority:` identifiers for exact replay. It is not the canonical semantic `TemporalAuthorityEnvelope`; that name remains owned by [`contracts/common/temporal_authority_envelope.md`](../common/temporal_authority_envelope.md).

New evidence-local work must use [`EvidenceTemporalPostureAssessment`](evidence_temporal_posture_assessment.md). The canonical evidence assessment initially preserves every legacy field, finite posture value, chronology rule, and pass/fail outcome. The legacy validator is a wrapper over that engine and loads the unchanged legacy schema.

No common↔evidence translator exists. In particular, the evidence `source_role` enum is not a governed `SourceDescriptor#/source_role` binding, and evidence correction-after-release chronology cannot be silently reinterpreted as the common envelope's correction-at-or-before-retrieval chronology.

Legacy removal is blocked until external databases, object storage, deployed clients, downstream repositories, and generated CI artifacts are inventoried with stable counts and digests. Historical receipts remain immutable.

Validation:

```bash
python -m unittest tests.evidence.test_temporal_authority_envelope --verbose
python tools/validators/evidence/validate_temporal_authority_envelope.py \
  fixtures/contracts/v1/evidence/temporal_authority_envelope/valid/current_observation.json
```

Rollback restores this wrapper and documentation to their pre-split bytes. No common-family, persisted-record, release, deployment, or publication state is rewritten.

# EvidenceTemporalPostureAssessment fixtures

These synthetic, rights-safe fixtures are byte-for-byte copies of the legacy evidence `TemporalAuthorityEnvelope` JSON fixtures. They prove exact replay compatibility while the semantic object receives a distinct evidence responsibility and name.

- `valid/current_observation.json` must pass both canonical and legacy evidence entry points at the same validation instant.
- `invalid/inverted_validity.json` must be rejected for inverted validity.
- `invalid/source_after_retrieval.json` must be rejected because the source update follows retrieval.

The fixtures do not conform to the common `TemporalAuthorityEnvelope`, authenticate a source role, resolve evidence, or authorize release/publication. Do not change one fixture tree without changing the compatibility proof and explicitly documenting the migration.

## Bounded correction replay

The existing [assessment tests](../../../../../tests/evidence/test_evidence_temporal_posture_assessment.py)
derive test-local correction, supersession, and withdrawal variants from the unchanged
`current_observation.json` fixture. At fixed validation instants, they replay those
records through the legacy validator, canonical assessment, and legacy fallback
with sockets denied. Observation, validity, source-update, retrieval, release, and
correction clocks retain their distinct values; rejected chronology, missing
lineage references, elapsed freshness, and a renamed identifier namespace retain
their diagnostic polarity. Input records and the historical fixture bytes must
remain unchanged.

The replay input's digest and canonical schema digest remain bound to the
[20260827 successor receipt](../../../../../data/receipts/generated/genrec-evidence-temporal-posture-split-reconciliation-20260827.json),
whose predecessor reference and digest are checked. That narrow identity check
does not refresh historical receipt results or claim current integrity for its
other artifacts.

This is executable evidence for entrypoint compatibility and validator fallback.
It is not an implemented record-history store, common-to-evidence translation,
lineage resolver, policy evaluation, migration execution, or persisted-data
rollback. External databases, object storage, deployed clients, downstream
repositories, and generated CI artifacts remain unverified. Issues #3370, #3383,
and #3394 therefore retain their broader consumer, migration, review, and rollback
holds. The existing workflow runs these tests; hosted execution on a future head
remains a separate check.

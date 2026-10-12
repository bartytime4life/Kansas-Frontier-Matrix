# EvidenceTemporalPostureAssessment

Status: **PROPOSED**, fixture-first, deterministic, no-network, and non-authoritative.

`EvidenceTemporalPostureAssessment` is the distinctly named evidence-local object extracted from the former evidence-side `TemporalAuthorityEnvelope` collision. It evaluates finite temporal posture, evidence-source update and retrieval chronology, release/correction chronology, a freshness deadline, and evidence-local lineage references. The common [`TemporalAuthorityEnvelope`](../common/temporal_authority_envelope.md) remains the only canonical semantic object named `TemporalAuthorityEnvelope`.

## Responsibility split

| Surface | Responsibility |
|---|---|
| Common `TemporalAuthorityEnvelope` | Cross-domain identity, governed `SourceDescriptor#/source_role` binding, authority scope, time, space, state/certainty, typed lineage, and governance references. |
| `EvidenceTemporalPostureAssessment` | Evidence-local posture and freshness assessment over the legacy evidence record shape. |
| Legacy evidence `TemporalAuthorityEnvelope` | Temporary exact-shape compatibility alias only; no common-family conformance or new semantic authority. |

The assessment retains the legacy fields and meanings without translating them:

- finite posture: `CURRENT`, `STALE`, `SUPERSEDED`, `WITHDRAWN`, or `UNKNOWN`;
- `source_updated_at <= retrieved_at`;
- `released_at >= retrieved_at` when present;
- `corrected_at >= released_at` and requires a release;
- `CURRENT` cannot use an elapsed freshness deadline;
- `SUPERSEDED` requires `supersedes_ref`;
- `WITHDRAWN` requires `withdrawal_ref`.

The `source_role` enum is an evidence-assessment label. It is **not** a substitute for the common envelope's governed `source_descriptor_ref` plus exact `source_role_ref` binding. No common↔evidence translator is defined because the two families carry different fields and incompatible correction chronologies.

## Compatibility boundary

The legacy evidence schema, fixture bytes, identifier prefix `kfm:temporal-authority:`, and validator entry point remain available. The legacy validator delegates to the canonical assessment engine while loading the unchanged legacy schema. Replay must produce the same diagnostics at the same validation instant.

Existing opaque references are identities only. The split assessment classifies the synthetic ProgramOutcomeChain legacy prefix as a fenced compatibility reference; it does not infer conformance to either temporal schema. New unclassified implementation references fail closed in the split assessment.

## Validation

```bash
python -m unittest tests.evidence.test_evidence_temporal_posture_assessment --verbose
python -m unittest tests.evidence.test_temporal_authority_envelope --verbose
python tools/validators/evidence/validate_evidence_temporal_posture_assessment.py \
  fixtures/contracts/v1/evidence/evidence_temporal_posture_assessment/valid/current_observation.json
```

A green result proves only bounded schema, chronology, fixture replay, and compatibility behavior. It does not resolve evidence, authenticate source roles, accept ADR-0014, change lifecycle state, authorize release/publication, or prove that external persisted records are absent.

## Removal gate and rollback

Databases, object storage, deployed clients, downstream repositories, and generated CI artifacts remain outside the tracked-text proof boundary. Their counted and digest-bound inventory is mandatory before deprecating, tombstoning, or removing the legacy path, schema ID, validator, workflow, fixtures, or identifier prefix.

Before merge, close the draft pull request and abandon the branch. After an authorized merge, revert the additive assessment, wrapper, workflow, split-assessment, tests, and successor receipt. The unchanged legacy evidence schema and records remain the fallback; the common family and Advisory `$ref` chain require no restoration.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/fixtures-release-temporal-replay
title: Synthetic temporal replay and recovery fixture
type: fixture-family-readme
version: v0.1.0
status: proposed; synthetic-only; no-network; non-authoritative
owner: "@bartytime4life via CODEOWNERS; temporal and compatibility acceptance pending"
created: 2026-11-17
updated: 2026-11-17
policy_label: public; synthetic-fixture; no-release-authority
owning_root: fixtures/
responsibility: Bind one synthetic legacy/evidence compatibility replay to distinct common chronology, a successor receipt and isolated recovery branches.
truth_posture: CONFIRMED bounded executable fixture proof; UNKNOWN external consumers and operational migration acceptance.
related:
  - ../README.md
  - ../../../contracts/evidence/evidence_temporal_posture_assessment.md
  - ../../../contracts/evidence/temporal_authority_envelope.md
  - ../../../contracts/common/temporal_authority_envelope.md
  - ../../../tools/release/temporal_replay.py
  - ../../../tests/release/test_temporal_replay.py
[/KFM_META_BLOCK_V2] -->

# Synthetic temporal replay and recovery

This is the first bounded replay fixture for
[#3394](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3394).
It exercises the existing legacy evidence compatibility alias and
`EvidenceTemporalPostureAssessment` against versioned synthetic records, while
the common envelope retains its separate meaning and chronology. It performs
no common/evidence translation and does not migrate a persisted store.

| Input | Responsibility |
|---|---|
| `case.json` | Explicit synthetic marker, fixed evaluation instant and fixture release identities |
| `legacy.json` | Original evidence identifier and exact bytes, including fractional seconds, an explicit UTC offset and an unknown correction time |
| `successor.json` | Corrected evidence assessment with a distinct revision, predecessor reference and all seven evidence clock fields populated distinctly |
| `common-v1.json`, `common-v2.json` | Separate common envelopes, preserving their object/revision identities and source correction before capture |
| `successor-receipt.json` | Synthetic digest binding of both evidence records, common context, schema IDs and the explicit dual-read-only boundary |
| `withdrawn.json` | Later evidence posture whose withdrawal reference and correction instant bind the synthetic withdrawal record |

The evidence clock fields are observation, validity start/end, source update,
retrieval, release and correction. Original spellings and missing values remain
byte-identical on legacy replay. Common source correction precedes capture;
the evidence correction follows release. Cross-family false acceptance is
rejected by the existing validators. This fixture does not resolve ADR-0014 or
declare a universal temporal vocabulary.

Run with the repository's hash-locked `project-test` dependencies:

```bash
PYTHONPATH="$PWD/tools/ci/kfm_no_network:$PWD" KFM_NO_NETWORK=1 \
  python tools/release/temporal_replay.py --fixtures
python -m pytest -q tests/release/test_temporal_replay.py
```

The command has no production-root or apply argument. It validates the complete
fixture before creating disposable workspaces. Withdrawal and rollback run on
**separate copies of the same successor state** through the existing synthetic
`rollback_apply.py` helper. Plan mode writes nothing; applied branches read back
the alias, complete correction and all nine invalidations. Every manifest and
record in both release histories must retain its original bytes. Rollback
reopens the original evidence bytes through both supported evidence validators;
withdrawal leaves no current release selected.

`PASS` means these fixture assertions passed. The report binds input and schema
hashes plus six declared first-party consumers. It is not a complete repository
consumer census. Databases, object storage, deployed clients, downstream
repositories and generated CI artifacts retain `NOT_INSPECTED`, unknown counts
and unknown digests. **Legacy removal remains `HOLD_EXTERNAL_INVENTORY_REQUIRED`.**
Real source authentication, persisted-record migration, public API/UI/AI parity,
operator recovery and accountable acceptance remain separate work.

The existing `rollback-drill` workflow runs the new `synthetic-temporal-replay`
job under the Python-process no-network guard. Passing checks create no source,
policy, review, release, publication or legacy-removal authority. No historical
fixture, schema, validator, identifier prefix or generated receipt is replaced.

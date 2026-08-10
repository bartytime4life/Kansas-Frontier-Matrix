<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://tests/joins/readme
title: Join Candidate Test Lane
type: test-lane-readme
version: v0.1.0
status: proposed; synthetic-only; no-network
owners: OWNER_TBD — join steward; validation steward; sensitivity steward
created: 2026-08-09
updated: 2026-08-09
policy_label: repository-facing; tests; joins; non-publisher
owning_root: tests/
responsibility: Define the bounded synthetic proof surface for generic cross-lane join candidate helpers.
truth_posture: cite-or-abstain
[/KFM_META_BLOCK_V2] -->

# Join candidate test lane

`tests/joins/` proves only deterministic behavior for repository-owned, synthetic join fixtures. It does not prove endpoint truth, a real spatial relationship, source rights, consent, evidence resolution, policy permission, review approval, release, or publication.

## Required fixture classes

The first executable matrix covers the six cases named by `tools/joins/README.md`:

- parameterized exact-key match;
- synthetic spatial-temporal match and mismatch;
- source-role conflict;
- restricted exact geometry;
- living-person denial;
- missing EvidenceRef abstention.

It also covers dependency error, SQL metacharacter handling, generalized restricted context, decision tamper, interval error, identity tamper, and forbidden publisher effects.

## Safety boundary

- Fixture refs and spatial cells are synthetic.
- SQLite is in-memory and parameterized.
- The helper writes no file and has no network client.
- `ALLOW` means candidate-report emission only; every effect field remains false.
- Pair-specific validators, evidence, policy, review, correction, release, and rollback remain downstream.

## Command

```bash
python tools/joins/join_candidates.py --fixtures
python -m pytest tests/joins/test_join_candidates.py -q --strict-config --strict-markers
```

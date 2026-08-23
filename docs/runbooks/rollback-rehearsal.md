# Synthetic rollback, withdrawal, and correction rehearsal

## Purpose

Exercise the correction and rollback path in an isolated temporary root before any real
release machinery is admitted. The rehearsal verifies identity, artifact digests, append-only
correction lineage, complete cache/index invalidation, alias restoration or withdrawal, and
retention of the affected release bytes.

## Authority boundary

`tools/release/rollback_apply.py` is **synthetic-only**. It requires a marker-protected
workspace and a scenario with `synthetic: true`. Its report is process evidence for tests; it
is not a `RollbackCard`, `PolicyDecision`, `ReviewRecord`, `ReleaseManifest`, promotion
approval, release mutation, or publication authority.

Directory ownership follows the adopted responsibility roots: executable release tooling is
under `tools/release/`, proof of behavior under `tests/release/`, synthetic fixture guidance
under `fixtures/release/`, and this operator explanation under `docs/runbooks/`.

## Run

```bash
python -m unittest -q tests.release.test_synthetic_rollback_rehearsal
```

The CLI defaults to a no-write plan. `--apply` still changes only a synthetic workspace:

```bash
python tools/release/rollback_apply.py \
  --workspace /tmp/kfm-rehearsal \
  --scenario /tmp/kfm-rehearsal/scenario.json
```

## Required checks

- current alias identifies the affected release and matches its expected digest;
- affected and target manifests have stable release identities and canonical JSON digests;
- every referenced artifact digest matches the bytes in the synthetic release directory;
- rollback targets a distinct prior release; withdrawal has no target release;
- a correction identifier, reason, and fixed decision time are present;
- all API/CDN/tile/catalog/triplet/search/vector/AI/downstream invalidations are explicit;
- original release manifests and artifacts remain byte-identical after the rehearsal;
- the resulting alias no longer exposes the affected release as current.

## Rollback of this repository change

Revert the feature-branch commits. No real release record, public alias, cache, catalog,
artifact, source, policy decision, or published state is touched by the helper or its tests.

# Synthetic Hazards rollback rehearsal

This lane contains one deterministic, no-network workspace for rehearsing a
Hazards planning-context rollback through the generic synthetic-only helper at
`tools/release/rollback_apply.py`.

The affected toy carrier deliberately labels expired planning context as
`CURRENT`. The prior carrier keeps the same expired context fail-closed as
`WITHHELD_STALE`. Both carriers are synthetic, non-locating, unreleased,
unpublished, and explicitly not for life-safety use. They contain no real
warning, watch, advisory, event, person, property, infrastructure, source
payload, credential, or sensitive location.

`tests/domains/hazards/test_synthetic_rollback_rehearsal.py` copies the tracked
workspace to a temporary directory before invoking the helper. It proves only
that:

- identical plans are deterministic and make no workspace changes;
- apply mode moves the temporary alias to the withheld stale carrier, records
  the synthetic correction and complete declared invalidation set, and retains
  both releases byte-for-byte; and
- tampered carrier bytes and a non-synthetic scenario fail closed before alias,
  correction, or invalidation state changes.

A passing test is bounded repository evidence for this fixture and helper. It
is not a `RollbackCard`, `CorrectionNotice`, `ReviewRecord`, `PolicyDecision`,
release decision, operational recovery result, deployment, promotion, or
publication authorization.

Run the focused slice from the repository root:

```bash
KFM_NO_NETWORK=1 PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 TZ=UTC \
  python -m unittest -q \
  tests.domains.hazards.test_synthetic_rollback_rehearsal
```

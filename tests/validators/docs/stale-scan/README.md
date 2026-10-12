<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-validators-docs-stale-scan-readme
title: Documentation Freshness Validator Tests
type: README
version: v0.1
status: draft; executable-tests; synthetic-only
owner: TODO-validation-steward-plus-docs-steward
created: 2026-08-07
updated: 2026-08-07
policy_label: repository-facing; tests; public-safe-fixtures
owning_root: tests/
responsibility: executable synthetic evidence for bounded stale-scan behavior, deterministic replay, failure polarity, changed-file ratcheting, path safety, and no-mutation boundaries
truth_posture: CONFIRMED focused tests pass locally / NEEDS VERIFICATION hosted exact-head execution
related:
  - ../../../../../tools/validators/docs/stale-scan/README.md
  - ./fixtures/valid_repo/README.md
notes:
  - "Fixtures are synthetic and grant no authority to repository documents or freshness thresholds."
[/KFM_META_BLOCK_V2] -->

# Documentation freshness validator tests

The focused suite covers:

- deterministic JSON and SHA-256 report replay;
- advisory and bounded-required profiles;
- missing, invalid, future, and reversed dates;
- expired review windows and temporal markers;
- stale owner placeholders;
- review-due signals for implementation language and unresolved verification posture;
- type-specific windows;
- changed-file ratcheting and historical failure downgrade;
- warning promotion for specifically adopted bounded lanes;
- malformed metadata delegation;
- path escape and symbolic-link denial;
- CLI outcome/exit-code behavior;
- explicit output without input mutation; and
- static no-network imports.

Run:

```bash
python -m unittest discover \
  --start-directory tests/validators/docs/stale-scan \
  --pattern 'test_*.py' \
  --verbose
```

The reviewed snapshot uses `--as-of 2026-08-07`. It is fixture evidence only,
not a repository-wide freshness baseline.

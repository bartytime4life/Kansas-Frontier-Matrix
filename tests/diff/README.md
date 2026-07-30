<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-diff-readme
title: tests/diff README
type: README
version: v1
status: active
owner: TODO-tooling-qa-owner
created: 2026-07-29
updated: 2026-07-29
policy_label: public
owning_root: tests/
responsibility: Executable conformance evidence for deterministic repository diff tools
related:
  - ../../tools/diff/README.md
  - ../../tools/diff/stable_diff.py
  - ../README.md
  - ../../docs/doctrine/directory-rules.md
notes:
  - Synthetic fixtures are public-safe and carry no source, policy, proof, release, or publication authority.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Diff tool tests

`tests/diff/` owns executable conformance evidence for repository-wide
comparison helpers under [`tools/diff/`](../../tools/diff/README.md).

## Boundary

These tests prove deterministic local comparison behavior. They do not prove
that a changed artifact is material, admissible, promotion-ready,
release-approved, or safe to publish.

## Direct children

```text
tests/diff/
├── README.md
├── fixtures/                  # public-safe JSON inputs
└── test_stable_diff.py        # stable top-level JSON diff behavior
```

## Fixture posture

- Fixtures are synthetic and contain no secrets, credentials, real people,
  exact sensitive locations, source payloads, or unpublished records.
- `same/` proves key-order-independent equivalence.
- `changed/` proves deterministic added, removed, and changed key lists.
- `malformed/` proves fail-closed parse behavior.

## Validation

```bash
pytest -q tests/diff/test_stable_diff.py
```

[Back to top](#top)

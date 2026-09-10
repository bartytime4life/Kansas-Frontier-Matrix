<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-validators-docs-critical-structure-readme
title: tests/validators/docs/critical-structure README
type: README
version: v0.1
status: draft; executable; no-network; synthetic; non-authoritative
owners: OWNER_TBD — QA steward · Docs steward · Validator steward · CI steward
created: 2026-09-10
updated: 2026-09-10
policy_label: repository-facing; tests; documentation-qa; no-network; non-authoritative
owning_root: tests/
responsibility: deterministic synthetic behavior tests for the critical-document structure checker
truth_posture: CONFIRMED executable standard-library suite and current-tree contributor-contract assertion / NEEDS VERIFICATION hosted exact-head execution, broader critical-document coverage, and required-check coupling
related:
  - ../../README.md
  - ../../../../tools/validators/docs/critical-structure/README.md
  - ../../../../.github/workflows/validator-suite.yml
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tests/validators/docs/critical-structure/`

> **Purpose.** Prove the critical-document sentinel accepts the repaired
> contributor contract and rejects the self-insertion shape deterministically
> without network access.

## Coverage

`test_critical_structure.py` covers the current `CONTRIBUTING.md`, duplicate H2
sections, interrupted link/heading syntax, expected H1 identity, H1 count,
unresolved merge-conflict markers, ATX headings and tab indentation, valid and
invalid fence openers, inert fenced and commented headings, inert same-line
inline-code comment and title tokens, escaped and exact backtick delimiter
handling, bounded unmatched-run scanning, distinct inline-code H2 titles,
permitted repeated H3s, unclosed boundaries, final-newline failure, symlink and
path-escape denial, type, UTF-8, size, control-character and absolute-path
denial, deterministic JSON, CLI exit polarity including operational error, and
blocked network entrypoints.

All negative inputs are synthetic and created under temporary directories. The
suite does not store production data, request URLs, interpret document claims,
or grant governance, review, release, deployment, or publication authority.

## Run

```bash
python -m unittest discover \
  --start-directory tests/validators/docs/critical-structure \
  --pattern 'test_*.py' \
  --verbose
```

## Rollback

Revert this test lane with the paired validator and workflow wiring through a
reviewed change. Do not treat removal of a regression test as evidence that the
underlying corruption is acceptable.

[Back to top](#top)

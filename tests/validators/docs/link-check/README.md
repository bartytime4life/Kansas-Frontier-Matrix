<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-validators-docs-link-check-readme
title: tests/validators/docs/link-check README
type: README
version: v1.1
status: draft; executable; no-network; synthetic; non-authoritative
owners: OWNER_TBD — QA steward · Docs steward · Validator steward · CI steward
created: 2026-07-30
updated: 2026-07-31
policy_label: repository-facing; tests; documentation-qa; no-network; non-authoritative
owning_root: tests/
responsibility: deterministic synthetic behavior tests for the local-only documentation link checker
truth_posture: CONFIRMED executable standard-library suite including GitHub basic heading-anchor fidelity and code-span boundary cases / NEEDS VERIFICATION hosted exact-head execution, broader Markdown dialect coverage, and required-check coupling
related:
  - ../../README.md
  - ../../../../tools/validators/docs/link-check/README.md
  - ../../../../.github/workflows/link-check.yml
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tests/validators/docs/link-check/` — Local Markdown Link-Check Tests

> **Purpose.** Prove the bounded documentation checker resolves local files,
> directories, images, and Markdown anchors deterministically, fails closed for
> missing or escaping targets, and never requests external URLs.

## Repository fit

Directory Rules assign executable conformance proof to `tests/`. The validator
implementation remains under
[`tools/validators/docs/link-check/`](../../../../tools/validators/docs/link-check/README.md),
and the workflow only orchestrates both surfaces.

## Accepted inputs

- synthetic Markdown created in temporary directories;
- local target and anchor cases;
- external URLs used only to prove abstention and no-network behavior;
- CLI output and exit-code assertions.

## Exclusions

- real external requests or redirect checks;
- source, citation, policy, evidence, proof, release, or publication decisions;
- production documents as test fixtures;
- a second validator implementation.

## Coverage

`test_docs_link_check.py` covers:

- files, directories, images, heading anchors, explicit anchors, and duplicate
  GitHub-style heading suffixes;
- heading slugs containing inline code (including angle-bracket placeholders),
  image alt text, link labels, em dashes, slashes, arrows, ampersands, adjacent
  spaces, and normalized duplicates;
- separate code-span policies: inline-code links and explicit anchors remain
  inert, while inline-code heading content remains part of the heading slug;
- missing targets, missing anchors, exact-case mismatch, and repository escape;
- symbolic-link input denial and explicit zero-Markdown changed scope;
- fenced code, inline code, and HTML-comment exclusion;
- external-target classification with socket and URL entrypoints denied;
- deterministic JSON and CLI exit polarity;
- strict `git diff` selector syntax.

## Run

```bash
python -m unittest discover \
  --start-directory tests/validators/docs/link-check \
  --pattern 'test_*.py' \
  --verbose
```

A passing suite proves only the listed synthetic mechanics. It does not prove
that every repository Markdown dialect or historical link is covered.

## Rollback

Before merge, close the draft PR. After an authorized merge, revert the focused
validator/test/docs/receipt commit; do not treat removal of this test lane as
permission to weaken unrelated documentation or release controls.

[Back to top](#top)

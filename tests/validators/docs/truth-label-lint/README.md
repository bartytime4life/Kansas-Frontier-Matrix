<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-validators-docs-truth-label-lint-readme
title: tests/validators/docs/truth-label-lint README
type: README
version: v0.1.0
status: bounded-executable-tests; synthetic; no-network; review-pending
owner: TODO-tooling-qa-owner-plus-docs-steward-plus-ci-steward
created: 2026-08-23
updated: 2026-08-23
policy_label: repository-facing; tests; docs-validator; synthetic; non-authoritative
owning_root: tests/
responsibility: Prove the finite structural behavior, deterministic reporting, failure polarity, and no-network boundary of the opt-in documentation assessment-axis linter.
truth_posture: CONFIRMED focused standard-library test implementation and synthetic cases / PROPOSED review and hosted execution / NEEDS VERIFICATION broader repository adoption and required-check coupling
related:
  - ../../../../tools/validators/docs/truth-label-lint/README.md
  - ../../../../tools/validators/docs/truth-label-lint/lint_truth_labels.py
  - ../../../../.github/workflows/truth-label-assessment-axes.yml
notes:
  - "Synthetic Markdown strings do not support any real repository, policy, source, or public claim."
  - "A passing test suite proves only the behavior exercised by the reviewed cases."
[/KFM_META_BLOCK_V2] -->

# Truth-label assessment-axis validator tests

This lane contains the focused, no-network proof for the opt-in structural rule
implemented by `lint_truth_labels.py`.

## Test surfaces

- `cases.json` records reviewed Markdown inputs, exact aggregate outcomes, and required finding codes.
- `test_truth_label_lint.py` checks fixture polarity, value preservation, explicit marker enforcement, deterministic discovery and JSON, UTF-8 errors, finite exits, fenced-example exclusion, symlink refusal, and no network/process/model dependency.

Run:

```bash
python -m unittest discover \
  --start-directory tests/validators/docs/truth-label-lint \
  --pattern 'test_*.py' \
  --verbose
```

A pass does not validate the truth, authority, evidence sufficiency, policy
posture, implementation maturity, review state, release state, or publication
fitness of any document.

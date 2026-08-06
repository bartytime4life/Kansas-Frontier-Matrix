<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-validators-docs-meta-block-readme
title: Documentation Metadata-Block Validator Tests
type: README
version: v0.1
status: draft; bounded-test-suite
owner: TODO-tooling-qa-owner-plus-docs-steward
created: 2026-08-06
updated: 2026-08-06
policy_label: repository-facing; test-documentation; synthetic-only
owning_root: tests/
responsibility: document deterministic positive, negative, replay, ratchet, registry-delta, CLI, no-mutation, and no-network tests for the bounded metadata-block validator
truth_posture: CONFIRMED synthetic fixture suite / NEEDS VERIFICATION hosted exact-head execution
related:
  - ../../../../tools/validators/docs/meta-block/README.md
  - ./test_docs_meta_block.py
  - ./fixtures/valid_repo/expected_meta_block_report.json
notes:
  - "Fixtures are synthetic and contain no real source, person, location, rights, or release data."
[/KFM_META_BLOCK_V2] -->

# Documentation metadata-block validator tests

The suite exercises the bounded `KFM_META_BLOCK_V2` profile and the review-only
machine document-registry comparison. It verifies deterministic JSON and digest
replay, a reviewed snapshot, required-vs-present profiles, delimiter and key
failures, required fields, owner posture, document identity, responsibility-root
alignment, date ordering, related-path escape denial, duplicate identities,
registry additions/conflicts, changed-file ratcheting, warning promotion, CLI
outputs, symbolic-link denial, registry non-mutation, and the static no-network
boundary.

Run:

```bash
python -m unittest discover \
  --start-directory tests/validators/docs/meta-block \
  --pattern 'test_*.py' \
  --verbose
```

A passing suite proves only the configured synthetic behavior. It does not prove
whole-repository metadata health, documentation authority, human review,
registry approval, release, or publication.

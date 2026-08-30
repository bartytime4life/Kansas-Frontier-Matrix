<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-diff-readme
title: tests/diff README
type: README
version: v2
status: active
owner: TODO-tooling-qa-owner
created: 2026-07-29
updated: 2026-08-30
policy_label: public
owning_root: tests/
responsibility: Executable conformance evidence for deterministic repository diff tools
related:
  - ../../tools/diff/README.md
  - ../../tools/diff/stable_diff.py
  - ../../tools/ci/render_stable_diff_summary.py
  - ../../tools/ci/build_stable_diff_review_handoff.py
  - ../../.github/workflows/stable-diff-review-summary.yml
  - ../../.github/workflows/stable-diff-review-handoff.yml
  - ../README.md
  - ../../docs/doctrine/directory-rules.md
notes:
  - Synthetic fixtures are public-safe and carry no source, policy, proof, release, or publication authority.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Diff tool tests

`tests/diff/` contains deterministic, no-network tests for the stable JSON
comparator and its reviewer-facing summary and handoff helpers. The executable
implementations remain under [`tools/diff/`](../../tools/diff/README.md) and
[`tools/ci/`](../../tools/ci/README.md); this directory owns their test evidence
and synthetic fixtures.

## Authority boundary

These tests can establish that the inspected code behaves as asserted for the
covered inputs. They do not decide whether a difference is material, resolve
evidence, interpret policy, authenticate a reviewer, approve promotion, release
or publish an artifact, or authorize public use. A generated summary or handoff
is derived review material, not sovereign truth or a release decision.

## Inventory

| Test module | Implementation under test | Confirmed coverage |
|---|---|---|
| [`test_stable_diff.py`](test_stable_diff.py) | [`tools/diff/stable_diff.py`](../../tools/diff/stable_diff.py) | Top-level JSON comparison; deterministic key ordering and report bytes; changed, blocking, malformed, missing, duplicate-key, non-finite-number, non-object, and CLI paths |
| [`test_render_stable_diff_summary.py`](test_render_stable_diff_summary.py) | [`tools/ci/render_stable_diff_summary.py`](../../tools/ci/render_stable_diff_summary.py) | Deterministic bounded Markdown; report-shape and status consistency; basename-only path display; escaping; blocking and error exit behavior |
| [`test_build_stable_diff_review_handoff.py`](test_build_stable_diff_review_handoff.py) | [`tools/ci/build_stable_diff_review_handoff.py`](../../tools/ci/build_stable_diff_review_handoff.py) | Exact input, report, summary, and context binding; deterministic hashes; finite handoff dispositions; policy-key declaration handling; tamper and stale-report rejection |

Direct children are limited to this README, the three test modules, and
`fixtures/`.

## Fixture posture

`fixtures/` contains only the comparator inputs used by
`test_stable_diff.py`:

```text
fixtures/
├── changed/
│   ├── left.json
│   └── right.json
├── malformed/
│   └── invalid.json
└── same/
    ├── left.json
    └── right.json
```

- `same/` verifies equivalence despite JSON key order.
- `changed/` verifies sorted added, removed, and changed top-level key lists.
- `malformed/` verifies fail-closed parse behavior.
- The fixtures are synthetic and contain no credentials, source payloads,
  living-person records, exact sensitive locations, or unpublished data.
- The summary and handoff suites create additional synthetic inputs in
  temporary directories and do not require checked-in source artifacts.

## Run the tests

From the repository root, run the complete directory with pytest so it collects
both pytest-style functions and `unittest.TestCase` classes:

```bash
pytest -q tests/diff
```

For a focused failure, run the owning module:

```bash
pytest -q tests/diff/test_stable_diff.py
python -m unittest tests.diff.test_render_stable_diff_summary -v
python -m unittest tests.diff.test_build_stable_diff_review_handoff -v
```

The commands are offline. They create temporary files only; they do not write
receipts, proofs, release records, or published artifacts.

## Hosted workflow binding

| Workflow | Trigger and collection behavior | Evidence limit |
|---|---|---|
| [`stable-diff-review-summary.yml`](../../.github/workflows/stable-diff-review-summary.yml) | Changes under `tests/diff/**` trigger the workflow. Its `unittest` command collects the renderer class, and a separate step exercises comparator-to-summary CLI output. | `test_stable_diff.py` uses pytest-style top-level functions, so naming it in the workflow's `unittest` command does **not** collect that module's assertions. |
| [`stable-diff-review-handoff.yml`](../../.github/workflows/stable-diff-review-handoff.yml) | Changes under `tests/diff/**` trigger the workflow. Its `unittest` command collects the renderer and handoff classes, and a separate step exercises the comparator, renderer, and handoff CLIs together. | The same collection gap applies to the pytest-style comparator module; the CLI exercise is narrower than that module's full assertion set. |

Workflow success is evidence only for the checked-out revision and the commands
that actually ran. Required-check status and any broader workflow that may also
collect this directory must be verified from the exact pull-request head; they
are not established by this README.

## Interpret failures

| Failure area | First investigation |
|---|---|
| Comparator | Input parsing, top-level comparison semantics, deterministic ordering, exit codes, or report serialization changed. |
| Summary renderer | The report envelope is malformed or contradictory, Markdown bounding or escaping regressed, or exit behavior changed. |
| Review handoff | An artifact, report, summary, or context digest no longer binds; a policy declaration is invalid; or stale or tampered material was accepted. |
| Workflow only | Compare the failing hosted command with the local command, dependency installation, path filters, and the exact checked-out SHA before attributing the failure to product behavior. |

Do not weaken fail-closed assertions merely to make a workflow pass. If a
contract intentionally changes, update the implementation, tests, and owning
documentation together and preserve deterministic error behavior.

## Maintenance checklist

- Keep this inventory synchronized with direct children of `tests/diff/`.
- Add or change fixtures only when they remain synthetic and public-safe.
- Bind every new helper to its implementation path and document what the test
  proves and does not prove.
- Prefer `pytest` for the directory-level command unless every module is
  deliberately compatible with `unittest` discovery.
- Reconcile workflow commands when test style changes; a named module is not
  proof that its tests were collected.
- Keep review, policy, promotion, release, publication, and rollback authority
  outside this test lane.

[Back to top](#top)

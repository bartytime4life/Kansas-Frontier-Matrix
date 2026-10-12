<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-governance-readme
title: tests/governance/ — Governance Validator Test Lane
type: README
version: v0.2
status: draft; repository-grounded; six-module-inventory; split-workflow-binding; deterministic; no-network; non-authoritative
owners: OWNER_TBD — Governance steward · QA steward · Validator steward · Evidence steward · Policy steward · Security reviewer · CI steward · Release steward
created: 2026-07-29
updated: 2026-08-31
policy_label: repository-facing; tests; governance; briefing-signals; issue-inventory; fixture-backed; read-only; no-network; non-publisher
owning_root: tests/
responsibility: executable conformance checks for bounded BriefingSignal validation, deduplication, materiality, issue routing, and read-only GitHub issue-inventory projections without granting governance or repository-mutation authority
truth_posture: CONFIRMED six direct test modules, 53 source-defined test methods, two directly bound workflow definitions, and no dedicated Make target at the pinned snapshot / UNKNOWN complete governance coverage, full-directory hosted collection, required-check status, production parity, accountable stewardship, correction propagation, and operational rollback
evidence_repository: bartytime4life/Kansas-Frontier-Matrix
evidence_base_ref: main
evidence_base_commit: 5d835798e09a4dd14735779cb44206a8a3e8b2d3
evidence_prior_blob: 724ce8cb818d7d0f8b4e0e2412e30609142f17f1
direct_test_module_count: 6
source_defined_test_count: 53
direct_workflow_binding_count: 2
related:
  - ../README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../contracts/governance/briefing_signal.md
  - ../../contracts/governance/github_issue_inventory_read.md
  - ../../fixtures/contracts/v1/governance/briefing_signal/
  - ../../fixtures/contracts/v1/governance/github_issue_inventory_read/
  - ../../tools/validators/governance/
  - ../../.github/workflows/briefing-integration.yml
  - ../../.github/workflows/github-issue-inventory-read.yml
notes:
  - "Counts describe source-defined unittest methods at the pinned Git tree, not durable coverage, collected-case evidence for another revision, or production behavior."
  - "The word live in a test name refers to binding a committed read receipt; the suite performs no live GitHub request."
  - "Passing tests do not authorize review, repository mutation, source admission, evidence closure, release, deployment, promotion, or publication."
[/KFM_META_BLOCK_V2] -->

# Governance tests

`tests/governance/` contains six modules and 53 deterministic tests for bounded governance
validators, routing helpers, and read-only issue-inventory projections. These
tests verify repository code and fixtures at the checked-out commit. They do
not create governance authority, approve review, admit a source, close
evidence, mutate GitHub, release, deploy, or publish.

## Suite inventory

| Test module | Tests | Confirmed coverage |
| --- | ---: | --- |
| [`test_briefing_signal.py`](test_briefing_signal.py) | 13 | Closed `1.2.0` schema, fixture polarity, deterministic identity, parser safety, examples, false-authority denial, value-minimized CLI output, and active network denial |
| [`test_briefing_signal_dedup.py`](test_briefing_signal_dedup.py) | 8 | Cluster stability, replay, collision detection, duplicate classification, input-order invariance, dry-run-only output, and active network denial |
| [`test_briefing_signal_materiality.py`](test_briefing_signal_materiality.py) | 9 | Exact materiality thresholds, mandatory overrides, six finite route profiles, schema-valid semantic negatives, deterministic reporting, and active network denial |
| [`test_briefing_signal_issue_inventory.py`](test_briefing_signal_issue_inventory.py) | 11 | Closed issue-inventory projections, existing-target binding, missing/closed/ambiguous target holds, invalid-inventory precedence, deterministic reports, and absence of mutation clients |
| [`test_briefing_signal_live_issue_inventory.py`](test_briefing_signal_live_issue_inventory.py) | 6 | Binding a stored GitHub issue-read receipt to BriefingSignal routing, identity reproduction, freshness and `as_of` requirements, fixture/live-input separation, and active network denial |
| [`test_github_issue_inventory_read.py`](test_github_issue_inventory_read.py) | 6 | Fixture-backed issue-read schema, repository/ref binding, pull-request exclusion, rate-limit holds, explicit staleness, and deterministic identity |
| **Total** | **53** | Source-defined `unittest` methods; not a coverage percentage or production claim. |

The “live” binding test uses the committed read receipt under
[`fixtures/contracts/v1/governance/github_issue_inventory_read/`](../../fixtures/contracts/v1/governance/github_issue_inventory_read/).
It does not query GitHub during the test.

## Run locally

From the repository root, run the complete directory:

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 PYTHONHASHSEED=0 TZ=UTC \
  python -m unittest discover \
  --start-directory tests/governance \
  --pattern 'test_*.py' \
  --verbose
```

To match the two hosted workflow boundaries separately:

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 PYTHONHASHSEED=0 TZ=UTC \
  python -m unittest discover \
  --start-directory tests/governance \
  --pattern 'test_briefing_signal*.py' \
  --verbose

KFM_NO_NETWORK=1 python -m pytest \
  tests/governance/test_github_issue_inventory_read.py \
  -q --strict-config --strict-markers
```

The environment flag records the intended execution posture. The five
`test_briefing_signal*.py` modules also patch socket and
`urllib.request` access so a network attempt fails the suite. The standalone
issue-read test exercises stored fixture data and pure projection behavior.

## Hosted workflow bindings

| Workflow | Direct command | Parent README trigger |
| --- | --- | --- |
| [Briefing Integration](../../.github/workflows/briefing-integration.yml) | `unittest discover` with `test_briefing_signal*.py`; five modules and 47 source-defined tests | Yes; the workflow watches `tests/governance/**`. |
| [GitHub Issue Inventory Read](../../.github/workflows/github-issue-inventory-read.yml) | Strict `pytest` invocation of `test_github_issue_inventory_read.py`; six source-defined tests | No; its path filter names the module and does not include this README. |

No dedicated Make target is claimed for this directory. A passing local
command does not prove that a hosted check is required, current, or successful
at another commit.

## Interpret results

- Expected rejection of an invalid fixture is a passing negative test, not a
  validator failure.
- `HOLD`, stale, missing-target, closed-target, ambiguous-target, and
  rate-limit outcomes are bounded domain results when the fixture expects
  them; they are not approval or mutation instructions.
- Import, collection, dependency, or unexpected-network failures mean the
  suite did not establish its behavioral claims.
- A valid BriefingSignal, issue projection, or read receipt remains a
  non-authoritative candidate. It does not prove the underlying claim, issue
  state at another time, accountable review, or permission to write to GitHub.

## Maintenance

When this directory changes:

1. update the inventory and complete-directory command in the same change;
2. keep fixture-backed and externally acquired evidence clearly distinct;
3. preserve exact invalid-fixture findings and finite outcomes;
4. link a workflow only when its current YAML directly invokes the test; and
5. keep validation, review, GitHub mutation, release, deployment, promotion,
   and publication as separate states.

## Known gaps and rollback

- No hosted command was established that collects all six modules in one job.
- Required-check status and complete governance-validator coverage remain
  unknown.
- The focused jobs use synthetic fixtures and a stored read receipt; they do
  not establish live GitHub behavior, production confinement, or current issue
  state.
- Accountable stewardship, correction propagation, and operational rollback
  remain unverified.

Before integration, close the draft pull request to abandon this documentation
change. After separately authorized integration, revert its commit. Reverting
this README does not change a validator, fixture, issue, repository setting,
review state, release, deployment, promotion, or publication.

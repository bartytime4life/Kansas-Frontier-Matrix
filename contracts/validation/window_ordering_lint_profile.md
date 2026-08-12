<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/validation/window-ordering-lint-profile
title: WindowOrderingLintCandidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-execution; no-network; non-authoritative
owners: OWNER_TBD — Analytics steward · Validation steward · SQL review steward
created: 2026-08-11
updated: 2026-08-11
owning_root: contracts/
policy_label: internal; validation; analytics; sql; window-ordering; reproducibility
responsibility: Define a bounded static-lint profile for explicit ordering and tie-breaker syntax in SQL window clauses without executing SQL or creating analytical, evidence, policy, review, release, or publication authority.
truth_posture: "CONFIRMED supplied-card traceability and repository placement; PROPOSED inactive ANSI-subset linter; UNKNOWN consumer adoption and engine coverage; NEEDS VERIFICATION steward review and hosted exact-head CI"
related:
  - ../common/rolling_metric_window_disclosure.md
  - ../evidence/indicator_definition.md
  - ../../schemas/contracts/v1/validation/window_ordering_lint_profile.schema.json
  - ../../fixtures/contracts/v1/validation/window_ordering_lint_profile/cases.json
  - ../../tools/validators/validate_window_ordering_lint_profile.py
  - ../../tests/validators/test_validate_window_ordering_lint_profile.py
  - ../../docs/intake/exploratory/pass-18-window-ordering-lint-source-map.md
[/KFM_META_BLOCK_V2] -->

# WindowOrderingLintCandidate

`WindowOrderingLintCandidate` is an additive, fixture-only profile for conservatively inspecting SQL window clauses for an explicit primary ordering field and stable final tie-breaker.

It adapts supplied Pass 18 card `KFM-P18-INV-132`: window-function rankings, deltas, moving averages, and panels require deterministic `ORDER BY` clauses and tie-breaker fields so release-to-release output does not drift with unspecified row order.

## Boundary

A validator `PASS` means only that every `OVER (...)` clause in the supplied SQL text fits the closed `SQL_ANSI_WINDOW_SUBSET_V1` grammar, carries `ORDER BY`, starts with the declared primary key, ends with the declared tie-breaker, has no duplicate ordering keys, and falls within the declared clause-count range.

The linter never sends SQL to a database, imports a database driver, resolves tables or columns, proves key uniqueness, compares result rows, validates a query plan, establishes cross-engine parity, computes an indicator, creates evidence, decides policy or review, promotes, releases, deploys, publishes, or authorizes public use.

The existing `RollingMetricWindowDisclosureCandidate` owns semantic partition, frame, missing-data, time, revision, and parity declarations. This profile adds a narrower static query-syntax check and may reference an existing disclosure or analysis contract without replacing it.

## Supported subset

The linter recognizes ordinary `OVER (...)` clauses and top-level `ORDER BY` lists with simple unquoted identifiers, optional qualification, `ASC`/`DESC`, and `NULLS FIRST`/`NULLS LAST`. It ignores keywords inside string literals and comments.

The profile intentionally abstains on:

- named windows such as `OVER window_name`, because resolving the later `WINDOW` definition is outside v1; and
- computed ordering expressions such as function calls, arithmetic, collations, or dialect-specific syntax.

Malformed quotes, comments, or parentheses are `ERROR`. Queries with no window clause, multiple statements, missing order, missing or misplaced keys, duplicate order keys, or an unexpected window count are `DENY`.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Every recognized window clause satisfies the closed static ordering rules. |
| `ABSTAIN` | Named-window resolution or a complex ordering expression is outside the supported subset. |
| `DENY` | A deterministic ordering invariant or exact-content binding fails. |
| `ERROR` | Shape or lexical structure cannot be evaluated safely. |

These are static fixture-lint outcomes only, not analytical correctness, uniqueness, evidence, policy, review, release, or publication decisions.

## Directory Rules basis

Reusable validation-profile meaning belongs under `contracts/validation/`; machine shape, synthetic SQL cases, repository validator code, focused tests, CI orchestration, exploratory source reconciliation, and generated accountability remain in their established responsibility roots.

No database adapter, query runtime, SQL authority, analytics engine, evidence lane, policy surface, release lane, or public route is created.

## Validation

```bash
python -m unittest tests.validators.test_validate_window_ordering_lint_profile -v
python tools/validators/validate_window_ordering_lint_profile.py --fixtures
```

## Rollback

Revert the additive packet. No query is executed and no database, analytical output, lifecycle record, evidence, policy, review, release, deployment, or public artifact is mutated.

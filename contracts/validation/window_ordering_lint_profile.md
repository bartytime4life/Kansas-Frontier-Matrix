<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/validation/window-ordering-lint-profile
title: WindowOrderingLintCandidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-execution; no-network; non-authoritative
owners: OWNER_TBD — Analytics steward · Validation steward · SQL review steward
created: 2026-08-11
updated: 2026-09-06
owning_root: contracts/
policy_label: internal; validation; analytics; sql; window-ordering; reproducibility
responsibility: Define a bounded static-lint profile for explicit ordering and tie-breaker syntax in SQL window clauses without executing SQL or creating analytical, evidence, policy, review, release, or publication authority.
truth_posture: "CONFIRMED supplied-card traceability, repository placement, and bounded current-main packet; PROPOSED inactive ANSI-subset linter; UNKNOWN consumer adoption, engine coverage, and current hosted exact-head result; NEEDS VERIFICATION steward ownership and human review"
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

## Repository reconciliation (2026-09-06)

This profile was re-read against GitHub `main@23c3487a1731f9558a6efc7143be65966f59efd5` on 2026-09-06. GitHub is the implementation authority for this snapshot; Notion and Google Drive remain coordination and lineage inputs. The semantic rules below remain inactive and unchanged by this currentness refresh.

The base snapshot contains the complete bounded packet:

| Surface | Repository evidence | Confirmed boundary |
|---|---|---|
| Contract meaning | `contracts/validation/window_ordering_lint_profile.md` (base blob `7b7a986927b3f1c70a7f7232fb861fb0eb2fae1a`) | This document owns the semantic profile; it does not own execution or authority. |
| Machine shape | schema blob `49ebf1786c10974a74aba5079aa02e4d11a52fd8` | Draft 2020-12 shape; closed object; `metric_truth_authority: false`. |
| Fixture replay | fixture manifest blob `e03d39701c7066e262adf1f4b440ae20c4b7e38f` | 22 synthetic cases covering `PASS`, `ABSTAIN`, `DENY`, and `ERROR`. |
| Static validator | validator blob `612f3282bc38d93add837e8bf0ae6159ee19cc78` | Validates schema and fixtures without network access or SQL execution; exits non-zero when the fixture manifest is not `PASS`. |
| Focused tests | test blob `3ea1218fa56a0c243bf4d8b133b3f45b899599d6` | Covers exact outcomes, schema closure, hash binding, determinism, no-network behavior, and hostile-input bounds. |
| Hosted workflow | workflow blob `b21a005d448e88ef585262b93cc38e284ef52be9` | Runs byte compilation, focused unittest, fixture replay, and generated-receipt integrity validation. |
| Source/semantic adjacency | source-map blob `b85f22a0bbd5050075b1d20db37b244bfa8b5534`; rolling disclosure blob `464349986d0fa388d082b154aed242a49f6b3409` | Preserves Pass 18 lineage and keeps semantic window disclosure separate from static syntax lint. |

The checked-in generated receipt `data/receipts/generated/genrec-pass18-window-ordering-lint-20260811.json` records authoring-time fixture and focused-test passes for the packet, while hosted exact-head CI and human review are explicitly `SKIPPED`. Its integrity binding is refreshed mechanically with this documentation update; that refresh does not turn the receipt into current hosted-run evidence or approval.

## Current verification boundary

Confirmed from the repository snapshot:

- The validator implementation, schema, fixtures, tests, workflow, and source map are present at the paths named above.
- The fixture manifest is the executable review surface for 22 finite cases; it is not a corpus of production SQL.
- The workflow is a command-bearing CI path, not proof that a run passed at the current `main` SHA. No matching `window-ordering-lint-profile` check run was identified for `main@23c3487a1731f9558a6efc7143be65966f59efd5` during this reconciliation.
- The profile remains proposed/inactive, fixture-only, no-execution, no-network, and non-authoritative.

Still open:

- steward ownership, human review, and hosted exact-head validation for any future change;
- consumer adoption and SQL-engine/dialect coverage;
- database execution, uniqueness proof, result equivalence, analytics correctness, evidence, policy, release, publication, and public-use authority.

This update does not promote the profile, widen the supported SQL subset, change the validator, change fixtures, change policy, or authorize production use.

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
python tools/validators/validate_generated_receipt.py data/receipts/generated/genrec-pass18-window-ordering-lint-20260811.json --repo-root .
```

## Rollback

Revert the additive packet. No query is executed and no database, analytical output, lifecycle record, evidence, policy, review, release, deployment, or public artifact is mutated.

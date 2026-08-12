<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/pass-18-window-ordering-lint
title: Pass 18 Window-Ordering Lint Source Map
type: exploratory-source-map
version: v1.0.0
status: draft; proposed-inactive; implementation-candidate
owners: OWNER_TBD — Intake steward · Analytics steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: docs/
policy_label: internal; source-lineage; analytics; sql; reproducibility; no-authority
responsibility: Preserve source lineage and repository reconciliation for a bounded static SQL window-ordering linter without promoting proposal material into analytical, database, evidence, policy, review, release, or publication authority.
truth_posture: "CONFIRMED supplied-card transcription and inspected-repository comparison; PROPOSED bounded ANSI-subset adaptation; UNKNOWN consumer and engine coverage; NEEDS VERIFICATION steward review and hosted exact-head CI"
related:
  - ../../../contracts/validation/window_ordering_lint_profile.md
  - ../../../contracts/common/rolling_metric_window_disclosure.md
  - ../../../docs/doctrine/directory-rules.md
[/KFM_META_BLOCK_V2] -->

# Pass 18 Window-Ordering Lint Source Map

## Evidence basis

| Evidence | Observation | Status |
|---|---|---|
| Supplied `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf`, SHA-256 `efc0d159761581b5ae043c607dfa28bbc58b3ca5423c9d18a659e650271d73b9`, physical pages 229–230 / printed pages 226–227 | Card `KFM-P18-INV-132` proposes deterministic `ORDER BY` clauses and tie-breakers for window-function rankings, deltas, moving averages, and panels; its expansion direction calls for SQL fixtures that fail ambiguous ordering. | `CONFIRMED` |
| Google Drive `Kansas Frontier Matrix — AI Build Operating Contract` and `Kansas Frontier Matrix — Connected-Dots Architecture Brief`, inspected 2026-08-11 | Corroborate small proof-bearing slices, deterministic no-network fixtures, finite outcomes, and explicit non-authority boundaries. | `PROPOSAL LINEAGE` |
| `main@074a39c4acb8e4e72cafe4bdea4c9e237dbf2496` | `RollingMetricWindowDisclosureCandidate` already declares ordering and tie-breaker metadata but explicitly does not inspect or execute SQL. Exact searches found no SQL parser dependency, window-order linter, matching fixture family, workflow, branch, or pull request. | `CONFIRMED` for the inspected snapshot |

The supplied and Drive documents are proposal evidence. The upstream `Advanced-SQL-Concepts.pdf` named by the atlas card was not independently admitted as current database or query-policy authority.

## Reconciliation and selected increment

The current rolling-metric disclosure profile already owns partition, ordering, frame, time, missing-data, revision, and cross-engine declaration semantics. A second disclosure contract would be duplicate authority.

The collision-safe increment is a narrower static linter: inspect exact query text as inert data, recognize a conservative `OVER (...)` subset, and prove that every recognized clause contains the declared simple primary key and final tie-breaker. It composes an existing disclosure by optional reference and never executes the query.

## Source-to-profile mapping

| Source pressure | Bounded adaptation | Held boundary |
|---|---|---|
| Require explicit window ordering. | Every ordinary `OVER (...)` clause must carry top-level `ORDER BY`. | No query execution or result comparison. |
| Require deterministic tie-breaking. | Declared primary key is first; a distinct declared tie-breaker is present and last. | Field existence and uniqueness are not resolved. |
| Add ambiguous-order fixtures. | Exact positive, abstain, deny, and error SQL strings cover missing, misplaced, duplicate, named, complex, and malformed forms. | This is not a general SQL parser or dialect authority. |
| Avoid keyword false positives. | Strings, quoted identifiers, and comments are masked before keyword scanning. | Dialect-specific quoting and computed expressions remain held. |
| Preserve exact input identity. | Raw UTF-8 query digest and candidate profile hash are replayed. | Digest equality is not evidence or analytical correctness. |

## Directory Rules path decision

```yaml
path_decision:
  artifact: WindowOrderingLintCandidate packet
  proposed_path: contracts/validation/window_ordering_lint_profile.md
  artifact_kind: semantic validation profile plus dependency-closed test packet
  authority_owner: validation contract stewardship
  lifecycle_stage: not_applicable
  execution_role: repository tool
  scope_kind: object_family
  scope_id: window-ordering-lint-profile
  exposure: internal
  mutability: versioned
  evidence:
    - docs/doctrine/directory-rules.md
    - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
    - contracts/common/rolling_metric_window_disclosure.md
  rules: [DIR-SIGNATURE-001, DIR-PLACE-005]
  outcome: PLACE
```

Meaning, shape, fixtures, tool code, tests, CI, source reconciliation, and generated accountability remain in their established roots. No new root, SQL authority, database runtime, or parallel rolling-metric contract is created.

## Validation and rollback

Focused validation covers ordinary and qualified identifiers, multiple windows, comments and strings, named-window abstention, computed-expression abstention, missing `OVER`, missing order, misplaced or absent tie-breakers, duplicate keys, clause-count bounds, multiple statements, exact query identity, hostile JSON, malformed quotes/parentheses, no-network replay, and closed schema/non-authority constraints.

Rollback is a focused revert of this additive packet. No SQL is executed and no database, analytical output, lifecycle record, evidence, policy, review, release, deployment, or public artifact is changed.

# Repository-control test contexts

Small, deterministic, no-network context and transition-authorization fixtures owned by `tests/validators/test_repository_control.py`, `tests/validators/test_repository_transition_authorization.py`, and incident-specific companion tests.

- `context_expected_hold.json` models an in-scope open PR whose state explicitly denies merge.
- `context_path_out_of_scope.json` proves exact-path and recursive-prefix scope rejection.
- `context_pr_1679_terminal_divergence.json` preserves public PR metadata for the confirmed cursor-divergence incident.
- `context_pr_1738_terminal_divergence.json` preserves a second public incident where a PR body stated “No merge or rebase” before the PR merged.
- `context_pr_1789_terminal_divergence.json` preserves the repository-control core incident: the PR was draft, had no submitted review, declared no merge authority, and then reached a merged terminal state.
- `context_pr_1791_terminal_divergence.json` preserves the bounded draft recovery PR incident: the tracked projection was `HELD`, every consequential permission was false, the PR body explicitly denied ready transition and merge, and the draft PR nevertheless reached a merged terminal state with no submitted reviews or requested reviewer.
- `context_pr_1792_terminal_divergence.json` preserves the documentation-only Agriculture compatibility update incident: the tracked projection was `HELD`, every consequential permission was false, the PR body explicitly denied merge authorization, and the draft PR nevertheless reached a merged terminal state with no submitted reviews or requested reviewer.
- `context_pr_1829_terminal_divergence.json` preserves the bounded CI-readiness reconciliation incident: the durable authorization explicitly denied ready and merge transitions, but the draft delivery later reached a merged terminal state with zero submitted reviews, requested reviewers, review threads, or PR comments.
- `pull_request_target_event_ready.json` is a synthetic ready-for-review event pinned to one default-branch base and one pull-request head.
- `issue_comments_transition_authorization_valid.json` is a synthetic paginated GitHub response containing one unedited owner-authored, exact-base, exact-head, two-hour transition authorization.

The incident and transition fixtures do not identify or infer an initiating client that the durable evidence does not establish. For PR #1829, the permissive pre-change ruleset and later platform recovery are recorded separately in issue #1675; the exact initiating client remains `UNKNOWN`. The transition fixture proves only strict parsing, owner-account binding, base/head binding, and expiry behavior. It does not prove human authorship, independent review, GitHub-settings enforcement, merge authority outside the record, release readiness, or publication authority.

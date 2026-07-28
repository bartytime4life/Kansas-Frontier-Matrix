# Repository-control test contexts

Small, deterministic, no-network context fixtures owned by `tests/validators/test_repository_control.py` and incident-specific companion tests.

- `context_expected_hold.json` models an in-scope open PR whose state explicitly denies merge.
- `context_path_out_of_scope.json` proves exact-path and recursive-prefix scope rejection.
- `context_pr_1679_terminal_divergence.json` preserves public PR metadata for the confirmed cursor-divergence incident.
- `context_pr_1738_terminal_divergence.json` preserves a second public incident where a PR body stated “No merge or rebase” before the PR merged.
- `context_pr_1789_terminal_divergence.json` preserves the repository-control core incident: the PR was draft, had no submitted review, declared no merge authority, and then reached a merged terminal state.
- `context_pr_1791_terminal_divergence.json` preserves the bounded draft recovery PR incident: the tracked projection was `HELD`, every consequential permission was false, the PR body explicitly denied ready transition and merge, and the draft PR nevertheless reached a merged terminal state with no submitted reviews or requested reviewer.
- `context_pr_1792_terminal_divergence.json` preserves the documentation-only Agriculture compatibility update incident: the tracked projection was `HELD`, every consequential permission was false, the PR body explicitly denied merge authorization, and the draft PR nevertheless reached a merged terminal state with no submitted reviews or requested reviewer.

The incident fixtures do not identify or infer the actor, bypass mechanism, ruleset behavior, or automation responsible for a merge. Those facts remain `NEEDS_VERIFICATION`. Fixture success proves only the declared evaluator behavior; it is not GitHub-settings evidence, review, merge authority, release readiness, or publication authority.

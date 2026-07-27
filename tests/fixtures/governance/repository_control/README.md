# Repository-control test contexts

Small no-network context fixtures owned by `tests/validators/test_repository_control.py`.

- `context_expected_hold.json` models an in-scope open PR whose state explicitly denies merge.
- `context_path_out_of_scope.json` proves path-scope rejection.
- `context_pr_1679_terminal_divergence.json` preserves public PR metadata for the confirmed cursor-divergence incident.
- `context_pr_1738_terminal_divergence.json` preserves a second public incident where a PR body stated “No merge or rebase” before the PR merged.

The incident fixtures do not identify or infer the actor, bypass mechanism, ruleset behavior, or automation responsible for a merge. Those facts remain `NEEDS_VERIFICATION`.

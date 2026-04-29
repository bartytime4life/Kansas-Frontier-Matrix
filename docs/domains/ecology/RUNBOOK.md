# Ecology Runbook

## Operator validation sequence

Run the ecology validators in this order before approving release or promotion changes:

```bash
tools/validators/ecology/run_ecology_fixture_checks.sh
tools/validators/ecology/run_ecology_release_checks.sh
tools/validators/ecology/run_ecology_focus_mode_checks.sh
```

## Notes

- Keep this order to ensure fixture correctness is established before release checks.
- Execute Focus Mode checks last to validate final sensitivity gating behavior.

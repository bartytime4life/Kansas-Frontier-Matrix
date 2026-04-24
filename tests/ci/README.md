# tests/ci

CI-focused tests for helper renderers in `tools/ci/`.

## Current thin slice

- `test_render_diff_summary.py`
- `test_render_bundle_diff_policy_summary.py`
- `test_render_promotion_review_handoff.py`
- `test_end_to_end_review_handoff.py`
- `test_end_to_end_diff_policy_summary.py`
- `test_end_to_end_diff_summary.py`
- `test_end_to_end_promotion_summary.py`
- `test_end_to_end_promotion_bundle_summary.py`

Run with:

```bash
python3 -m pytest -q tests/ci
```

# Governance tests

`tests/governance/` proves bounded behavior of governance validators and examples. Tests do not create governance authority, review approval, source admission, evidence, release state, or public truth.

## BriefingSignal suite

- `test_briefing_signal.py`: closed `1.2.0` schema, structural fixture polarity, identity/idempotency, parser safety, false-authority denial, and worked-example anti-collapse.
- `test_briefing_signal_dedup.py`: cluster stability, replay, collision detection, duplicate classification, input-order invariance, and dry-run-only output.
- `test_briefing_signal_materiality.py`: exact threshold boundaries, mandatory overrides, six finite route profiles, schema-valid semantic negatives, deterministic value-minimized reporting, and no-network behavior.

## Command

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 PYTHONHASHSEED=0 \
  python -m unittest discover \
  --start-directory tests/governance \
  --pattern 'test_briefing_signal*.py' \
  --verbose
```

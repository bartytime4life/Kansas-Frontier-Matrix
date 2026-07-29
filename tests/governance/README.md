# Governance tests

`tests/governance/`

Status: proposed test lane.

This lane proves bounded behavior of governance validators and examples. Tests do not create governance authority, review approval, source admission, evidence, release state, or public truth.

## Current suite

`test_briefing_signal.py` verifies:

- one valid synthetic fixture;
- stable fail-closed findings for public-use, evidence, and geometry violations;
- deterministic no-network CLI behavior;
- Hays meeting occurrence remains unconfirmed; and
- GMD link presence does not become approval or non-submission.

## Command

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1   python -m unittest discover   --start-directory tests/governance   --pattern 'test_briefing_signal.py'   --verbose
```

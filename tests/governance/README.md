# Governance tests

`tests/governance/` proves bounded behavior of governance validators and examples. Tests do not create governance authority, review approval, source admission, evidence, release state, or public truth.

## BriefingSignal suite

`test_briefing_signal.py` verifies:

- the closed Draft 2020-12 `1.1.0` schema and corrected claim closure;
- two valid synthetic fixtures and four exact invalid fixture families;
- deterministic signal digest, daily signal ID, event-cluster ID, and issue idempotency key;
- object-key and unordered-array order invariance;
- changed-headline/new-signal but stable-cluster behavior;
- normalized identity tokens, tamper detection, duplicate-key/non-finite/non-object JSON rejection;
- deterministic value-free CLI output and explicit no-network behavior;
- Hays meeting occurrence remains unconfirmed; and
- GMD link presence does not become approval or non-submission.

`test_briefing_signal_dedup.py` verifies:

- same-story follow-ups form one cluster;
- input ordering does not affect output;
- exact replays are counted rather than recreated;
- duplicate issue creation fails closed;
- unclassified same-cluster signals are rejected;
- declared signal-ID collisions fail; and
- the dry run never calls the network or grants mutation authority.

## Command

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 PYTHONHASHSEED=0 \
  python -m unittest discover \
  --start-directory tests/governance \
  --pattern 'test_briefing_signal*.py' \
  --verbose
```

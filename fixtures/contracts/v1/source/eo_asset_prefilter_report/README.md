# EO asset prefilter fixtures

These fixtures exercise a **synthetic, deterministic, no-network** source-edge report.
They contain sanitized `fixture://` and `kfm://` references only. They do not call a STAC
API, sign provider URLs, retrieve imagery, activate a source, admit RAW bytes, resolve
evidence, or publish a derived layer.

## Valid lane

| Fixture family | Expected decision |
|---|---|
| Six usable items with replayable assets | `PASS` |
| Fewer than six otherwise usable items | `HOLD` |
| A non-missing asset without a replay validator | `HOLD` |
| Any missing asset | `DENY` |
| Empty result set | `DENY` |

## Invalid lane

Exact-negative fixtures prove rejection of count drift, decision drift, profile/hash drift,
noncanonical references, non-normalized ETags, public-use escalation, and non-governed
HTTP locators.

```bash
python tools/validators/source/validate_eo_asset_prefilter_report.py --fixtures
```

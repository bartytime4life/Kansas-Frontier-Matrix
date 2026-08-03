# Semantic-Invalid TemporalWindow Fixtures

These candidates require the dedicated validator because their failure is not fully proved by the generic common-schema harness.

| Fixture | Expected finding |
|---|---|
| `invalid_1_reversed_interval.json` | `TEMPORAL_ORDER_INVALID` |
| `invalid_2_naive_datetime.json` | Date-time format/timezone rejection |

The lane is non-vacuous and every fixture has reviewed expected-error evidence. These cases do not decide the final KFM-wide temporal vocabulary.

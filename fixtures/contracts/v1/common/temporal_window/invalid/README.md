# Schema-Invalid TemporalWindow Fixtures

Each fixture fails the paired JSON Schema for one primary reviewed reason.

| Fixture | Expected reason |
|---|---|
| `invalid_1_missing_time_kind.json` | Required property missing. |
| `invalid_2_unknown_time_kind.json` | Closed enum violation. |
| `invalid_3_extra_property.json` | Additional properties are closed. |

These files are exercised by both the generic common-contract schema test and the dedicated validator.

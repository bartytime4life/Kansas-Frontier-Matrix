# Valid TemporalWindow Fixtures

These synthetic candidates must pass both the proposed JSON Schema and the dedicated interval-ordering validator.

| Fixture | Purpose |
|---|---|
| `valid_1.json` | Ordinary UTC observed interval. |
| `valid_2.json` | Equal instants represented with `Z` and `-05:00`; equality is valid after UTC normalization. |

Acceptance proves only the bounded validation profile. It does not establish source truth, freshness, policy, release, or publication.

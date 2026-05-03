# Schema authority map

| Home | Family | Likely authority | Interim use | Prohibited duplication | Migration rule | Validator expectation | Owner/status | Rollback risk |
|---|---|---|---|---|---|---|---|---|
| `contracts/` | semantic contracts | object meaning | stable | duplicate machine schema IDs | no machine-schema move without ADR | manifest records conflict | Architecture / CONFLICTED | medium |
| `schemas/` | JSON schemas | machine shape authority | stable | duplicate schema IDs across homes | keep IDs stable | add duplicate-id checks later | Architecture / CONFLICTED | high |
| `jsonschema/` | python helper package | runtime helper | compatible | shadowing canonical schema registries | keep package-only | lint path ownership | Tools / PROPOSED | low |

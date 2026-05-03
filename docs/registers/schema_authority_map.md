# Schema Authority Map

| Home | Family | Likely authority | Interim use | Prohibited | Migration rule | Validator expectation | Owner/status | Rollback risk |
|---|---|---|---|---|---|---|---|---|
| contracts/ | schema_contract | semantic contracts | keep existing files | duplicating schema IDs across homes | ADR-driven only | detect duplicate ids | Architecture / CONFLICTED | high |
| schemas/ | schema_contract | machine validation schemas | keep existing files | redefining same canonical ID differently | ADR-driven only | schema id uniqueness check | Data architecture / CONFLICTED | high |
| jsonschema/ | schema_contract | python package helper layer | read-only compatibility | new canonical schema sources | keep as adapter only | import-path health checks | Platform / PROPOSED | medium |

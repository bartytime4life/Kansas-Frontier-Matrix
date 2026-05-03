# Policy Authority Map

| Home | Family | Likely authority | Interim use | Prohibited | Migration rule | Validator expectation | Owner/status | Rollback risk |
|---|---|---|---|---|---|---|---|---|
| policy/ | policy | primary policy-as-code and policy docs | continue primary usage | silent duplication into policies/ | ADR-0013 gate required | ensure conflicts documented | Governance / CONFLICTED | high |
| policies/ | policy | legacy/secondary policy examples | keep for compatibility only | introducing new canonical policy packages | converge by ADR | package-name collision detection | Governance / CONFLICTED | medium |

# ReviewShareLink Validator

Validates the fixture-only `ReviewShareLink` profile defined by:

- `contracts/review/review_share_link.md`
- `schemas/contracts/v1/review/review_share_link.schema.json`

The validator is deterministic and no-network. It checks strict JSON loading, Draft 2020-12 schema shape, timestamp ordering, safe governed context references, derived active/expired/revoked state, exact finite decision reasons/outcome, and canonical `spec_hash`.

It does not create bearer tokens, grant access, run an HTTP service, write lifecycle data, approve review, promote, release, or publish.

```bash
python tools/validators/review/review_share_link/validate_review_share_link.py \
  fixtures/review/review_share_link/valid/active.json
```

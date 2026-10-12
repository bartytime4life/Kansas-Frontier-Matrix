# `fixtures/domains/flora/valid/` — Valid Flora Fixtures

This lane contains the exact positive inventory for the bounded synthetic public-safe Flora profile.

| Fixture | Expected result | Meaning |
|---|---|---|
| `public_safe_occurrence.json` | `PASS` | The candidate conforms to the frozen fixture-only profile. It is not a botanical occurrence claim and is not released. |

The fixture uses synthetic references, generalized fixture-area support, explicit no-network posture, fixture-only rights/evidence/review controls, `not_released`, and `promotion_eligible: false`.

It must contain no real taxa, coordinates, geometry, private-land detail, access or collection clues, URLs, credentials, or geoprivacy transform parameters.

Run:

```bash
python tools/validators/domains/flora/validate_public_safe_fixture.py \
  fixtures/domains/flora/valid/public_safe_occurrence.json
```

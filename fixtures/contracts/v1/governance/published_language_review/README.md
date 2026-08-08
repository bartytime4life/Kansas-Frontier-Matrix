# PublishedLanguageReview fixtures

This directory contains one closed fixture manifest for the inactive `PublishedLanguageReview` candidate profile.

## Polarity

| Class | Count | Purpose |
|---|---:|---|
| `PASS` | 2 | Stable additive vocabulary and a bounded deprecation candidate with migration support. |
| `DENY` | 9 | Context ownership, alias, migration, ordering, adoption, public-use, and compatibility failures. |
| `ERROR` | 1 | Intentional deterministic-hash corruption. |

`cases.json` stores identity-free bases. The validator assigns `spec_hash` and `review_id` after applying each mutation, except for the explicit identity-corruption case.

All values are synthetic. No source is activated, no API or schema is changed, no term is adopted, and no public-use authority is created.

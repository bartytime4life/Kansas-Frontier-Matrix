# Flora Pipelines and Lifecycle

## Lifecycle stages
1. **Source descriptor ready** (role/rights/sensitivity resolved).
2. **RAW intake** captured with immutable provenance.
3. **WORK normalization** applies crosswalks and geometry handling.
4. **Validation gates** enforce schema + policy.
5. **PROCESSED** objects produced for eligible records.
6. **Catalog/proof closure** for reproducibility.
7. **Promotion decision** approves, holds, denies, or quarantines.
8. **PUBLISHED** public-safe artifacts served via governed surfaces.

## Gate outcomes
- `PASS` -> continue.
- `HOLD` -> pending steward or policy review.
- `DENY` -> blocked until corrected.
- `QUARANTINE` -> unresolved rights/sensitivity/integrity.

## Non-negotiable controls
- No direct publication from RAW/WORK.
- All public payloads must trace to cataloged artifacts.
- Rollback target required for each promoted bundle.

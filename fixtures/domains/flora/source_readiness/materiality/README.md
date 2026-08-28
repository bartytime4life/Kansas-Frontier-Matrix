# Flora source-readiness materiality fixtures

These fixtures exercise a **synthetic, deterministic, no-network** profile for
transparent changes in Flora source readiness. They do not query GBIF, USDA
PLANTS, iDigBio, NatureServe, a herbarium, or any other live source.

## Valid families

| Family | Expected shared outcome |
|---|---|
| Unchanged bytes | `UNCHANGED / NON_EVENT` |
| Byte-only drift | `BYTE_ONLY / NON_EVENT` |
| Semantic change below every threshold | `SEMANTIC_NON_MATERIAL / NON_EVENT` |
| Georeference completeness crosses its delta threshold | `MATERIAL / PROMOTION_CANDIDATE` |
| License-resolution posture changes | `MATERIAL / PROMOTION_CANDIDATE` |
| API access state changes | `MATERIAL / PROMOTION_CANDIDATE` |
| Freshness crosses the stale-state boundary | `MATERIAL / PROMOTION_CANDIDATE` |
| Sensitivity posture changes | `MATERIAL / PROMOTION_CANDIDATE` |
| Required metric is unavailable | `UNDETERMINED / HOLD` |
| Analysis-unit kind does not match the profile | `UNDETERMINED / HOLD` |

`PROMOTION_CANDIDATE` means only that a deterministic review candidate exists.
It is not a source-admission record, `PolicyDecision`, `EvidenceBundle`,
`PromotionDecision`, `ReleaseManifest`, release, or publication.

## Invalid families

The invalid lane proves exact rejection for missing metrics, out-of-range
fractions, negative uncertainty, unknown sensitivity posture, invalid time
ordering, noncanonical reference arrays, undeclared fields, placeholder
digests, and incomplete evidence input.

## Commands

```bash
python -m unittest discover \
  --start-directory tests/validators/domains/flora \
  --pattern 'test_source_readiness_materiality.py' \
  --verbose

python tools/validators/domains/flora/validate_source_readiness_materiality.py \
  --fixtures
```

Passing these commands proves only the reviewed fixture polarity, profile hash,
local schema shape, deterministic classification, and non-echoing CLI output.

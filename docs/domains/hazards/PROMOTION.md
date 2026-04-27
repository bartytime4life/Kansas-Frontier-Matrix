# Hazards Promotion

Promotion is a governed decision that controls whether hazard material can become a released public surface.

## Gates

| Gate | Condition |
| --- | --- |
| A `ownership_present` | Responsible steward/reviewer assigned. |
| B `schema_valid` | Required hazard schemas and payload contracts validate. |
| C `evidence_complete` | All public evidence references resolve successfully. |
| D `catalog_linkage_closed` | Manifest/proof/catalog links are internally consistent. |
| E `signatures_verified` | Sign/attest checks pass or explicit hold reason recorded. |
| F `policy_compliant` | Rights/sensitivity/source-role/no-emergency posture passes. |
| G `diff_clean` | Reviewable, bounded diffs with no unresolved migration risk. |

## Outcomes

- `PROMOTE`: all gates pass.
- `HOLD`: outstanding fixable obligations.
- `DENY`: policy/evidence/rights posture forbids release.
- `ERROR`: validator/service/runtime fault prevents decision.

## Required output shape

Each decision should include:

- decision id and timestamp;
- candidate release id;
- gate-by-gate status;
- reason codes;
- reviewer/steward attribution;
- follow-up obligations when not promoted.

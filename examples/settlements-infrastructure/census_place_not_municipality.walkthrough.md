# A synthetic CensusPlace is not a municipality

This static walkthrough keeps statistical place identity separate from municipal legal identity. Its label and identifiers are invented, with no geometry, real jurisdiction, source record, or community referent. The existing `settlements-infrastructure` example path is used without resolving the documented `settlement` segment conflict.

```yaml
example: true
authority: non_authoritative_example
do_not_publish: true
maturity: STATIC_WALKTHROUGH
real_vs_synthetic: synthetic_only
expected_outcome: ABSTAIN
operational_home: Settlements/Infrastructure identity and governed runtime
validation_boundary: JSON snippet parsing and relative-link checks; no identity, policy, or runtime execution
correction_trigger: place-identity, source-role, path-governance, or runtime contract change
```

## Toy identity question

> Does a statistical place label establish municipal legal status?

```json
{
  "example": true,
  "authority": "non_authoritative_example",
  "do_not_publish": true,
  "scenario_id": "kfm://example/settlements-infrastructure/census-not-municipality-001",
  "identity_ref": "kfm://example/place/synthetic-census-001",
  "identity_family": "CensusPlace",
  "source_role": "synthetic_statistical_context",
  "legal_status_claimed": false,
  "census_status_claimed": true,
  "municipal_status_evidence_refs": [],
  "release_state": "not_released",
  "expected_outcome": "ABSTAIN"
}
```

This is an example question, not a `PlaceIdentityProfile`, municipal record, Census record, EvidenceBundle, or runtime response. The [place-identity contract](../../contracts/domains/settlements-infrastructure/place-identity.md) and [strict proposed schema](../../schemas/contracts/v1/domains/settlements-infrastructure/place-identity.schema.json) define the object shape; the [synthetic public-safe fixture](../../fixtures/public_safe/settlement/valid_1_unreleased_settlement.json) is a separate checking input.

## Expected reasoning

| Check | Toy result | Consequence |
|---|---|---|
| Statistical identity | `CensusPlace` is the example family | It says nothing about municipal incorporation. |
| Municipal legal support | No municipal-status EvidenceRef | Do not assert legal status. |
| Public response | `ABSTAIN` | No substantive municipality claim; the toy example is unreleased anyway. |

The [canonical-path guidance](../../docs/domains/settlements-infrastructure/CANONICAL_PATHS.md) still records the segment conflict. This walkthrough does not select a schema, proof, receipt, or release home. Revise or retire it if identity semantics or path governance change; using it in a test or public runtime requires separate review.

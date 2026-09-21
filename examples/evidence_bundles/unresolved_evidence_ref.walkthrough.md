# Unresolved synthetic evidence reference

This static walkthrough teaches why a claim must stop at `ABSTAIN` when its toy EvidenceRef has no resolved support. Every identifier and statement below is invented. Nothing here is an EvidenceBundle, citation-validation record, proof, policy decision, runtime response, or released fact.

```yaml
example: true
authority: non_authoritative_example
do_not_publish: true
maturity: STATIC_WALKTHROUGH
real_vs_synthetic: synthetic_only
expected_outcome: ABSTAIN
operational_home: data/proofs/evidence_bundle/ (actual proof records only)
validation_boundary: JSON snippet parsing and relative-link checks; no resolver or runtime execution
correction_trigger: evidence-resolution, citation, policy, or runtime contract change
```

## Toy question and input

> Can KFM state that synthetic feature Alpha has a supported observation?

```json
{
  "example": true,
  "authority": "non_authoritative_example",
  "do_not_publish": true,
  "scenario_id": "kfm://example/evidence-bundles/unresolved-ref-001",
  "feature_ref": "kfm://example/feature/synthetic-alpha",
  "source_role": "synthetic",
  "evidence_refs": [
    {
      "ref": "fixture://evidence/synthetic/unresolved-001",
      "kind": "measurement",
      "resolution_state": "UNRESOLVED"
    }
  ],
  "expected_outcome": "ABSTAIN"
}
```

The snippet is a teaching scenario, not an instance of the [EvidenceBundle schema](../../schemas/contracts/v1/evidence/evidence_bundle.schema.json). Its `evidence_refs` vocabulary follows the [valid contract fixture](../../fixtures/contracts/v1/evidence/evidence_bundle/valid/valid_1.json); the added `resolution_state` describes this walkthrough only.

## Expected reasoning

| Step | Toy result | Consequence |
|---|---|---|
| Resolve EvidenceRef | `UNRESOLVED` | No EvidenceBundle or source record supports the question. |
| Check citation closure | `NOT_RUN` | No citation can be attached to a substantive claim. |
| Compose answer | `ABSTAIN` | Return no factual statement about feature Alpha. |

A valid-looking reference string is not evidence. The [EvidenceBundle contract](../../contracts/evidence/evidence_bundle.md) and [proof home](../../data/proofs/evidence_bundle/README.md) own actual meaning and records. This walkthrough neither tests those systems nor grants publication authority. If those contracts change, revise or retire this example and any inbound links; copying it into a fixture or runtime requires separate review.

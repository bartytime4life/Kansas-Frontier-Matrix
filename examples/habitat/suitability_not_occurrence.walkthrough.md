# Habitat context is not a Fauna occurrence

This static walkthrough asks whether a synthetic HabitatPatch can support a species-occurrence claim. It cannot: habitat context and Fauna occurrence have different owners and evidence requirements. No real patch, species, coordinate, or source record is represented here.

```yaml
example: true
authority: non_authoritative_example
do_not_publish: true
maturity: STATIC_WALKTHROUGH
real_vs_synthetic: synthetic_only
expected_outcome: ABSTAIN
operational_home: Habitat and Fauna domain evidence and governed runtime
validation_boundary: JSON snippet parsing and relative-link checks; no model, policy, or runtime execution
correction_trigger: Habitat/Fauna ownership, evidence, sensitivity, or runtime contract change
```

## Toy question

> Does this invented HabitatPatch prove that a species occurs there?

```json
{
  "example": true,
  "authority": "non_authoritative_example",
  "do_not_publish": true,
  "scenario_id": "kfm://example/habitat/suitability-not-occurrence-001",
  "habitat_patch_ref": "kfm://fixture/synthetic/habitat/patch-001",
  "habitat_context_role": "synthetic_suitability_context",
  "fauna_occurrence_evidence_refs": [],
  "expected_outcome": "ABSTAIN"
}
```

The toy patch reference follows the [HabitatPatch fixture](../../fixtures/domains/habitat/valid/valid_1_habitat_patch.json). This snippet is an example question, not a HabitatPatch, suitability-model result, Fauna observation, EvidenceBundle, or runtime response.

## Expected reasoning

| Check | Toy result | Consequence |
|---|---|---|
| Habitat context | Synthetic patch reference exists | It illustrates habitat context only. |
| Fauna occurrence support | No occurrence EvidenceRef | No species-presence claim can be cited. |
| Public response | `ABSTAIN` | Do not infer occurrence from suitability, land cover, or connectivity. |

The [Habitat domain](../../docs/domains/habitat/README.md) owns patch and suitability meaning; the [Fauna domain](../../docs/domains/fauna/README.md) owns occurrence meaning. The [domain-boundary fixture](../../fixtures/domains/habitat/habitat_fauna_thin_slice/valid_1_domain_boundary_case.json) demonstrates the same separation as a checking input. This walkthrough adds no consumer or proof. Revise or retire it if that boundary, evidence profile, or public-response contract changes.

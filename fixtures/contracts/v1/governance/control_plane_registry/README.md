# Normalized control-plane registry fixtures

This packet exercises the proposed common schema and semantic validator for the seven existing legacy registry paths.

- `valid/valid_minimal.yaml` proves the smallest evidence-bearing partial entry with an explicit `UNKNOWN` owner.
- `invalid/duplicate_entry_id.yaml` rejects duplicate stable IDs.
- `invalid/unresolved_governing_ref.yaml` rejects missing repository references.
- `invalid/missing_material_authority.yaml` rejects a material authority claim without governing references and source digests.
- `invalid/self_activation.yaml` rejects any claim that the projection is authoritative.
- `invalid/unknown_field.yaml` rejects undeclared fields.
- `expected_findings_manifest.json` binds each negative case to its exact reviewed finding-code set.

Run:

```bash
python tools/validators/control_plane/validate_control_plane_registry_packet.py --fixtures
```

The fixtures are synthetic, deterministic, public-safe, and no-network. Fixture success does not populate a live registry, create authority, activate sources, approve policy, close verification, resolve contradictions, deprecate paths, or change release/publication state.

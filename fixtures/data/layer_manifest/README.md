# LayerManifest fixture profile

This directory contains synthetic, no-network examples for the dual-profile `LayerManifest` schema.

- `valid/valid_legacy_minimal.json` proves the prior permissive `id`-required profile remains accepted.
- The remaining valid files use the closed `PROPOSED_INACTIVE` / `FIXTURE_ONLY` profile.
- `invalid/invalid_*.json` files are schema-invalid.
- `invalid/semantic_invalid_*.json` files pass JSON Schema and fail a named deterministic semantic invariant.
- `expected_findings_manifest.json` is the exact reviewed polarity contract.

No fixture resolves a reference, verifies an artifact or signature, evaluates policy, authenticates review, authorizes release/publication/public use, registers a layer, or supplies precise sensitive geometry.

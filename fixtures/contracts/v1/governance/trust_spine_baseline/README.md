# Trust-spine baseline fixtures

This packet exercises the proposed trust-spine authority baseline contract with deterministic, public-safe, no-network inputs.

- `valid/valid_minimal.yaml` is the smallest reviewed shape that reconciles counts, paths, digests, execution state, overlap, non-effects, and correction metadata.
- `invalid/duplicate_projection_id.yaml` proves projection IDs fail closed on duplication.
- `invalid/digest_mismatch.yaml` proves referenced bytes must match their pinned SHA-256 values.
- `invalid/missing_referenced_path.yaml` proves a declared repository path cannot silently disappear.
- `invalid/self_authority.yaml` proves the projection cannot claim authority for itself.
- `invalid/unexecuted_pass.yaml` proves a command that was not run cannot claim a pass.
- `expected_findings_manifest.json` binds each invalid fixture to the exact reviewed finding-code set.

Run:

```bash
python tools/validators/control_plane/validate_trust_spine_baseline.py --fixtures
```

Fixtures validate structure and failure polarity only. They do not establish repository truth, accept decisions, waive drift, activate sources, approve review, or change release, deployment, promotion, or publication state.

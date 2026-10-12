# LayerManifest validator

`validate_layer_manifest.py` validates the existing permissive legacy shape and a closed, fixture-only `LayerManifest` candidate profile.

```bash
python tools/validators/data/validate_layer_manifest.py --fixtures
python tools/validators/data/validate_layer_manifest.py path/to/candidate.json
```

Outcomes are `PASS`, `FAIL`, or `ERROR`. Diagnostics are value-free finding codes plus JSON pointers.

A `PASS` does not resolve references, verify artifact bytes or signatures, evaluate policy, authenticate review, authorize release/publication/public use, or register a layer with MapLibre. The strict profile remains `PROPOSED_INACTIVE` and `FIXTURE_ONLY`.

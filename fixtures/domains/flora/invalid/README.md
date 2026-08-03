# `fixtures/domains/flora/invalid/` — Invalid Flora Fixtures

This lane contains the exact negative inventory for the bounded synthetic public-safe Flora profile. Each JSON file is paired with a sorted tab-separated `*.expected_error.txt` sidecar containing only stable finding code and JSON path.

| Fixture | Primary boundary |
|---|---|
| `candidate_not_object.json` | Top-level candidate must be an object |
| `missing_public_controls.json` | Redaction/review references, no-release state, and no-promotion state are required |
| `missing_references.json` | Taxon, source descriptor, and evidence references are required |
| `role_and_taxonomy_collapse.json` | Source role, taxon state, and rights posture are frozen for this profile |
| `undeclared_external_transform.json` | Undeclared fields, URLs, numeric values, and transform secrets fail closed |
| `unsafe_location_and_sensitivity.json` | Exact/reverse-engineerable/private-land location material fails closed |

These fixtures are synthetic negative examples, not real sensitive records. Candidate values are never echoed by the validator.

Run all negative fixtures:

```bash
python tools/validators/domains/flora/validate_public_safe_fixture.py \
  fixtures/domains/flora/invalid/*.json
```

The command is expected to exit `1` because every supplied candidate has findings.

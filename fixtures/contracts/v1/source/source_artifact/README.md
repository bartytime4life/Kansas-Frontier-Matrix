# SourceArtifact fixture profile

`valid_cases.json`, `invalid_cases.json`, and the two `semantic_invalid_cases_*.json` files form the synthetic, no-network fixture corpus for the proposed `SourceArtifact` profile. It contains three valid metadata/payload pairs, three schema-invalid records, and eight schema-valid semantic-negative records with reviewed expected finding codes.

The payloads are short synthetic UTF-8 byte streams embedded only to make exact SHA-256 and byte-length binding reproducible. The corpus contains no live source response, credential, real person, protected location, or operational endpoint.

```bash
python tools/validators/validate_source_artifact.py --fixtures
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_source_artifact.py' \
  --verbose
```

A passing fixture proves only shape, local consistency, and exact synthetic byte binding. It does not admit or activate a source, establish source truth, resolve evidence, promote lifecycle state, release, or publish.

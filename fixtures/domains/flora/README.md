# `fixtures/domains/flora/` — Flora Fixtures

Status: repository-grounded draft; one bounded public-safe fixture profile is executable.

This root holds compact synthetic Flora examples for deterministic repository checks. It is not a lifecycle data root, source registry, evidence store, policy home, release lane, or public-serving surface.

## Implemented profile

The bounded public-safe profile is consumed by:

```text
tools/validators/domains/flora/validate_public_safe_fixture.py
tests/domains/flora/test_flora_smoke.py
.github/workflows/domain-flora.yml
```

Its explicit inventory is:

```text
valid/public_safe_occurrence.json
invalid/candidate_not_object.json
invalid/missing_public_controls.json
invalid/missing_references.json
invalid/role_and_taxonomy_collapse.json
invalid/undeclared_external_transform.json
invalid/unsafe_location_and_sensitivity.json
```

Every invalid JSON file has an exact `*.expected_error.txt` sidecar.

## Fixture rules

- Use synthetic identifiers and fixture-only references.
- Never include real precise plant locations, private-land details, access routes, collection clues, restricted cultural knowledge, credentials, or source payloads.
- Never include redaction offsets, jitter seeds, generalization thresholds, precision values, or other parameters that could reverse a public-safe transform.
- Keep files compact, deterministic, duplicate-key-free, and no-network.
- Make positive, negative, and boundary behavior explicit.
- Treat schema conformance, semantic validity, evidence resolution, policy allowance, review, proof, release, and public safety as separate states.
- A passing fixture is not a project record, occurrence claim, EvidenceBundle, PolicyDecision, ReviewRecord, ReleaseManifest, or published artifact.

## Other child lanes

Other Flora fixture directories remain independent planning or test surfaces. This implementation does not promote their payloads, validators, or consumers. Their own README and executable evidence determine their maturity.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/domains/flora \
  --pattern 'test_flora_smoke.py' \
  --verbose
```

# Synthetic public-safe range fixtures

This directory contains a bounded, deterministic, no-network fixture profile
for the proposed Fauna `RangePolygon` family.

- `valid/public_safe_synthetic_range.json` is explicitly synthetic,
  generalized, fixture-only, unreleased, and ineligible for promotion. Its
  polygon is a map-consumable test carrier, not a real range or occurrence.
- `invalid/exact_occurrence_claim.json` proves that exact precision,
  unresolved sensitivity, missing derivation disclosure, and occurrence-truth
  collapse fail closed.
- `invalid/open_ring.json` proves malformed polygon topology fails closed.
- `expected_findings_manifest.json` binds the complete fixture inventory to
  exact finite findings.

Run:

```bash
python tools/validators/domains/fauna/range/validate_public_safe_range_fixture.py --fixtures
python -m unittest tests.domains.fauna.test_public_safe_range_fixture
```

These fixtures contain no production, protected, private-land, or sensitive
occurrence data. Passing this profile does not promote the scaffolded schema,
admit a source, approve policy or review, release a layer, or authorize
publication.

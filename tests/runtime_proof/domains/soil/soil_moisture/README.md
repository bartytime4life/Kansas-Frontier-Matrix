# Soil-moisture runtime proof

This no-network test lane maps the existing synthetic station soil-moisture
fixture profile through its validator and into the current closed
`RuntimeResponseEnvelope` shape.

The profile is deliberately fail-closed:

- the repository fixtures are `fixture_only`, `not_released`, and
  `promotion_eligible: false`, so a validator-clean fixture returns `ABSTAIN`,
  never `ANSWER`;
- missing evidence/source/receipt support returns `ABSTAIN`;
- semantic or public-safety validation failures return `DENY`;
- malformed non-object input returns `ERROR`;
- outward envelopes contain only the paired runtime-schema fields and do not
  expose readings, station identifiers, proof, catalog, promotion, release, or
  publication objects.

Run the focused proof with:

```bash
python -m pytest \
  tests/packages/envelopes/test_runtime_response_candidate.py \
  tests/runtime_proof/domains/soil/soil_moisture/test_runtime_mapper.py \
  -q --strict-config --strict-markers
```

A green result proves only deterministic mapping of synthetic fixtures under
this proposed test profile. It does not activate a source, resolve an
`EvidenceBundle`, evaluate release policy, authorize an API route, or publish
soil-moisture data.

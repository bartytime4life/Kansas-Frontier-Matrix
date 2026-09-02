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
  tests/ci/test_render_runtime_proof_summary.py \
  -q --strict-config --strict-markers
```

Emit and render the reviewer-only QA artifacts with:

```bash
mkdir -p artifacts/qa/soil-moisture-runtime-proof
PYTHONPATH=packages/envelopes/src python -m \
  tests.runtime_proof.domains.soil.soil_moisture.emit_runtime_proof_report \
  --repo-root . \
  --issued-at 2026-08-05T22:00:00Z \
  --output artifacts/qa/soil-moisture-runtime-proof/actual-responses.json
python tools/ci/render_runtime_proof_summary.py \
  --report artifacts/qa/soil-moisture-runtime-proof/actual-responses.json \
  --output artifacts/qa/soil-moisture-runtime-proof/summary.md
```

The JSON report and Markdown summary are temporary review aids. They are not
canonical evidence, receipts, proofs, policy decisions, promotion decisions,
release manifests, publication records, or public API responses.

A green result proves only deterministic mapping of synthetic fixtures under
this proposed test profile. It does not activate a source, resolve an
`EvidenceBundle`, evaluate release policy, authorize an API route, or publish
soil-moisture data.

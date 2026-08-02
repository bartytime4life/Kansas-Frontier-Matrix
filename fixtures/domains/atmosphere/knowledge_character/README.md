# Atmosphere knowledge-character fixture profile

This lane contains synthetic, deterministic inputs for
`tools/validators/domains/atmosphere/validate_knowledge_character.py`.
It proves a bounded anti-collapse profile for six Atmosphere knowledge
characters and exact negative cases. It is not the canonical enum or registry,
an Atmosphere observation, a PolicyDecision, an EvidenceBundle, an advisory,
an alert, a release record, or publication authority.

The profile ID is `kfm-atmosphere-knowledge-character-fixture-v1`. The terms in
the profile come from the draft Atmosphere semantic contract, while the exact
pairings and JSON shape are `PROPOSED` fixture bindings. The permissive machine
schema and placeholder registry remain unchanged until their ADR-class enum and
placement decisions are resolved.

## Inventory

`valid/` contains one public-safe case for each bounded character:

- `OBSERVED_SENSOR`
- `PUBLIC_AQI_REPORT`
- `ATMOSPHERIC_MODEL_FIELD`
- `REMOTE_SENSING_MASK`
- `ALERT_AND_ADVISORY_CONTEXT`
- `NETWORK_AND_SITE_CONTEXT`

`invalid/` contains exact fail-closed cases for model-as-observation,
AQI-as-concentration, AOD-as-ground-PM2.5, advisory-as-life-safety, and
precise-site exposure. Every invalid JSON file has a sorted
`.expected_error.txt` sidecar containing only finding code and JSON path.
Missing, unknown, and multiple character states are generated in memory by the
focused test so they do not masquerade as reusable registry entries.

All geometry is synthetic and generalized. No file contains a live endpoint,
credential, station coordinate, alert text, medical advice, source payload, or
release-ready data.

## Run

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tests/domains/atmosphere/test_knowledge_character_registry.py --verbose
```

Rollback is a clean revert of the feature change. No source, lifecycle, proof,
release, or published state is created by these fixtures.

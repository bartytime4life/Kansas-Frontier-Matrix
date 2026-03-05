## Summary

This PR applies a deterministic Planner output for `hazards.noaa_storm_events.normalize` and updates governed documentation + policy fixtures.

### What changed

- Added normalized field mapping for NOAA Storm Events ingestion.
- Added policy fixture to deny release when `license` metadata is missing.
- Updated pipeline receipt schema examples with `spec_hash` and evidence references.

## Governance evidence

### Gate outcomes

| Gate | Result | Evidence |
|---|---|---|
| schema | ✅ pass | `plans/2026-03-05T012233Z/hazards/evidence/schema_report.json` |
| policy | ✅ pass | `plans/2026-03-05T012233Z/hazards/evidence/policy_report.json` |
| qa | ✅ pass | `plans/2026-03-05T012233Z/hazards/evidence/qa_report.json` |
| repro | ✅ pass | `plans/2026-03-05T012233Z/hazards/evidence/repro_report.json` |
| supply-chain | ✅ pass | `plans/2026-03-05T012233Z/hazards/evidence/sbom.spdx.json` |

### Policy decision excerpt

```json
{
  "decision": "allow",
  "policy_label": "public",
  "obligations": [],
  "bundle_digest": "sha256:80149b22f3f75fb5d5e3a2a6408c5bcacdc2f84828681e22e163ce9abeb2dd5d"
}
```

## Determinism and provenance

- `idempotency_key`: `executor.hazards-noaa-storm-events.2026w10.seed-6f5a2f11`
- `run_id`: `run_2026-03-05T012233Z_6f5a2f11`
- `spec_hash`: `jcs:sha256:3fe2c6b48f8d16f2f2b4f8ab5ecf2209b6a2e4e96fbb4d4d84cece92a53f5f9f`
- `prov_bundle`: `prov/executor/2026-03-05T012233Z/bundle.jsonld`

## Risk and rollback

- **User impact:** low (documentation + validation fixtures only).
- **Operational risk:** low; no runtime policy broadening.
- **Rollback:** revert this PR commit; rerun pipeline with previous spec hash.

## Reviewer checklist

- [ ] Validate evidence paths and digests.
- [ ] Confirm no restricted data appears in logs or PR text.
- [ ] Confirm contract docs remain consistent with governance charter.

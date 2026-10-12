# Flora rare-plant-record fixtures

`fixtures/domains/flora/rare_plant_record/`

Status: draft / fixture lane / high-sensitivity semantic-contract support.

This directory is for small synthetic Flora `RarePlantRecord` fixture examples used by bounded schema checks, semantic-contract reviews, governed API tests, Evidence Drawer examples, Focus Mode examples, renderer checks, and documentation dry-runs. These fixtures may represent toy restricted-record handling, public-safe derivative behavior, review-state handling, or refusal cases, but they are not real rare-plant records and must not be treated as source truth, catalog truth, release proof, or publication state.

These files are examples only. They are not authoritative project records, source records, EvidenceBundles, source descriptors, policy decisions, review approvals, release state, public API material, public map material, public tiles, or published artifacts.

## Contract and schema posture

The semantic contract for `RarePlantRecord` is present at `contracts/domains/flora/rare_plant_record.md`. It describes the object as the high-sensitivity Flora record for rare, protected, tracked, steward-controlled, culturally sensitive, or otherwise policy-significant plant occurrences, statuses, evidence, locations, review states, public-safe derivatives, correction, and rollback.

The paired schema at `schemas/contracts/v1/domains/flora/rare_plant_record.schema.json` is present but still a `PROPOSED` scaffold with no declared properties and `additionalProperties: true`. Fixtures in this lane may support semantic review and future validator work, but they do not prove field-level machine enforcement until the schema, validators, and tests are upgraded and run.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic fixture examples, not governed lifecycle data. It is not a `data/`, `policy/`, `schemas/`, `contracts/`, `release/`, proof, source-registry, or publication root.

The root fixture README states that fixtures are operational/runtime examples, not canonical truth, and that RAW, WORK, or QUARANTINE data does not belong here. The Flora backlog also calls this lane synthetic and generalized. This README inherits those boundaries.

## Related references

- `../README.md`
- `../../README.md`
- `../golden/README.md`
- `../invalid/README.md`
- `../flora_occurrence/README.md`
- `../plant_taxon/README.md`
- `../evidence_bundles/README.md`
- `../../../../contracts/domains/flora/rare_plant_record.md`
- `../../../../contracts/domains/flora/occurrence_public.md`
- `../../../../contracts/domains/flora/occurrence_restricted.md`
- `../../../../contracts/domains/flora/flora_occurrence.md`
- `../../../../contracts/domains/flora/plant_taxon.md`
- `../../../../contracts/domains/flora/redaction_receipt.md`
- `../../../../schemas/contracts/v1/domains/flora/rare_plant_record.schema.json`
- `../../../../docs/domains/flora/MISSING_OR_PLANNED_FILES.md`
- `../../../../docs/domains/flora/API_CONTRACTS.md`
- `../../../../docs/domains/flora/MAP_UI_CONTRACTS.md`
- `../../../../docs/domains/flora/SENSITIVITY.md`
- `../../../../policy/domains/flora/`
- `../../../../policy/sensitivity/flora/`
- `../../../../data/registry/sources/flora/`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.expected.json`, `*.json`, `*.geojson`, `*.jsonl`, or `*.md` examples;
- toy rare-plant record examples for positive-path and negative-path checks;
- generalized or suppressed public-safe derivative examples;
- examples that keep taxon support, status support, source role, evidence support, review state, and release state separate;
- examples that prove restricted detail does not pass into public surfaces;
- examples that prove missing support, unresolved taxonomy, stale support, policy denial, or release-state gaps produce bounded outcomes;
- paired expected outputs in `../golden/` when behavior becomes a stable regression anchor.

## Exclusions

Do not use this lane for real source data, real restricted records, lifecycle data, release artifacts, proof packs, policy rules, implementation code, public map data, public API payloads, public tiles, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, and reviewable.
- Use toy identifiers, toy taxa, toy source names, toy source roles, toy timestamps, toy evidence references, and toy geometries unless a bounded check explicitly requires a more realistic shape.
- Make record posture explicit: restricted-case example, public-safe derivative, review-pending example, suppressed example, candidate example, or synthetic example.
- Keep source role, taxon state, status state, evidence state, review state, release state, correction state, and expected outcome explicit where material.
- Prefer no geometry unless the fixture explicitly needs geometry. When geometry is required, use toy or public-safe generalized geometry.
- Pair each input with an expected output when practical.
- Treat `schema-valid`, `semantic-valid`, `taxon-resolved`, `evidence-resolved`, `policy-admissible`, `review-ready`, `release-safe`, and `renderer-safe` as separate checks.
- Do not treat rare-plant fixtures as evidence, approval, release state, source authority, schema authority, implementation proof, access authority, or published output.

## Expected fixture examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Public-safe derivative with resolved synthetic support | `ANSWER` | Demonstrates positive path without becoming source truth. |
| Restricted-case record presented to public surface | `DENY` or public-safe derivative | Public surface must fail closed or use approved derivative shape. |
| Missing evidence support | `ABSTAIN` | Cite-or-abstain blocks unsupported claims. |
| Unresolved taxon or status support | `ABSTAIN` | Taxon/status uncertainty remains visible. |
| Stale support with no current alternative | `ABSTAIN` / `SOURCE_STALE` | Freshness state is visible and bounded. |
| Release or review state missing | `HOLD`, `DENY`, or `ABSTAIN` | Fixture must not imply release approval. |
| Incomplete contract-shaped payload | Validation failure or `ERROR` | Contract shape must not be silently accepted. |

## Maintenance notes

- Update this README when payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each fixture to the schema check, semantic-contract review, governed-API test, Evidence Drawer test, Focus Mode test, renderer check, policy check, or documentation example that consumes it.
- If a fixture becomes stable enough to anchor a regression check, pair it with an expected output and document the consumer.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: populated from empty placeholder content.
- Fixture payload inventory: no payloads verified in this directory during this update.
- Contract alignment: PARTIALLY VERIFIED against `contracts/domains/flora/rare_plant_record.md`.
- Schema alignment: NEEDS VERIFICATION because the paired schema is present but remains a permissive `PROPOSED` scaffold.
- Consumer alignment: NEEDS VERIFICATION against validators, renderer checks, governed-API tests, Evidence Drawer tests, Focus Mode tests, and policy checks.
- Tests and validators: NOT RUN.

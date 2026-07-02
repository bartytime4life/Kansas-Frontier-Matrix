# Flora invasive-plant-record fixtures

`fixtures/domains/flora/invasive_plant_record/`

Status: draft / fixture lane / semantic-contract support.

This directory is for small synthetic Flora `InvasivePlantRecord` fixture examples used by bounded schema checks, semantic-contract reviews, renderer checks, governed API tests, Evidence Drawer examples, Focus Mode examples, and documentation dry-runs. These fixtures may represent toy invasive-plant observations, status records, survey detections, management-context examples, or refusal cases, but they are not real invasive-plant records and must not be treated as source truth, catalog truth, management direction, release proof, or publication state.

These files are examples only. They are not authoritative project records, source records, EvidenceBundles, source descriptors, policy decisions, rights approvals, review approvals, release state, public API material, public map material, public tiles, or published artifacts.

## Contract and schema posture

The semantic contract for `InvasivePlantRecord` is present at `contracts/domains/flora/invasive_plant_record.md`. It describes the object as an evidence-bound record for invasive plant observations, source status, spread context, management posture, cross-lane interactions, public-safe exposure, correction, and rollback.

The paired schema at `schemas/contracts/v1/domains/flora/invasive_plant_record.schema.json` is present but still a `PROPOSED` scaffold with no declared properties and `additionalProperties: true`. Fixtures in this lane may support semantic review and future validator work, but they do not prove field-level machine enforcement until the schema, validators, and tests are upgraded and run.

## Placement basis

Directory rules and the root fixture README keep fixture material under the `fixtures/` responsibility root. This lane is therefore a Flora-domain fixture lane for invasive-plant-record examples, not a data lifecycle root, not a source registry, not a catalog root, not a proof root, not a policy root, not a schema root, not a release root, and not a publication target.

The root fixture README states that `fixtures/` is for operational rendering inputs rather than validator-only test data. It also states that fixture corpora must not contain RAW, WORK, QUARANTINE data, restricted geospatial detail, or canonical truth. This README inherits those boundaries.

## Related fixture and doctrine references

- `../README.md`
- `../../README.md`
- `../flora_occurrence/README.md`
- `../golden/README.md`
- `../invalid/README.md`
- `../evidence_bundles/README.md`
- `../../../../contracts/domains/flora/invasive_plant_record.md`
- `../../../../contracts/domains/flora/flora_occurrence.md`
- `../../../../contracts/domains/flora/plant_taxon.md`
- `../../../../contracts/domains/flora/flora_taxon_crosswalk.md`
- `../../../../contracts/domains/flora/habitat_association.md`
- `../../../../contracts/domains/flora/range_polygon.md`
- `../../../../contracts/domains/flora/botanical_survey.md`
- `../../../../contracts/domains/flora/restoration_planting.md`
- `../../../../contracts/domains/flora/redaction_receipt.md`
- `../../../../schemas/contracts/v1/domains/flora/invasive_plant_record.schema.json`
- `../../../../docs/domains/flora/MISSING_OR_PLANNED_FILES.md`
- `../../../../docs/domains/flora/API_CONTRACTS.md`
- `../../../../docs/domains/flora/MAP_UI_CONTRACTS.md`
- `../../../../docs/domains/flora/SENSITIVITY.md`
- `../../../../docs/domains/flora/DATA_LIFECYCLE.md`
- `../../../../policy/domains/flora/`
- `../../../../policy/sensitivity/flora/`
- `../../../../data/registry/sources/flora/`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.expected.json`, `*.json`, `*.geojson`, `*.jsonl`, or `*.md` examples;
- toy invasive-plant record examples for positive-path and negative-path checks;
- public-safe status, survey, spread-context, or management-context examples;
- examples that keep taxon identity, invasive status, source role, evidence support, and management context separate;
- examples that prove modeled, aggregate, candidate, or administrative support is not silently upgraded into observed fact;
- examples that prove stale support, missing evidence, unresolved taxonomy, policy denial, or release-state gaps produce bounded outcomes;
- paired expected outputs in `../golden/` when behavior becomes a stable regression anchor;
- README files explaining fixture intent and boundaries.

## Exclusions

Do not use this lane for real source data, lifecycle data, release artifacts, proof packs, policy rules, implementation code, public map data, public API payloads, public tiles, management orders, treatment instructions, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, and reviewable.
- Use toy identifiers, toy taxa, toy source names, toy source roles, toy timestamps, toy evidence references, and toy geometries unless a bounded check explicitly requires a more realistic shape.
- Make record posture explicit: observed occurrence, survey detection, survey non-detection, treatment record, regulatory status, aggregate report, modeled risk, candidate report, or synthetic example.
- Keep source role, taxon state, invasive-status state, evidence state, rights state, policy state, freshness state, review state, release state, correction state, and expected outcome explicit where material.
- Prefer no geometry unless the fixture explicitly needs geometry. When geometry is required, use toy or public-safe generalized geometry.
- Pair each input with an expected output when practical.
- Treat `schema-valid`, `semantic-valid`, `taxon-resolved`, `evidence-resolved`, `policy-admissible`, `release-safe`, and `renderer-safe` as separate checks.
- Do not treat invasive-plant fixtures as evidence, approval, release state, source authority, schema authority, implementation proof, management direction, or published output.

## Expected fixture examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Public-safe invasive-plant record with resolved synthetic support | `ANSWER` | Demonstrates positive path without becoming source truth. |
| Status-list example without occurrence support | `ABSTAIN` or contextual output | Status context must not become occurrence proof. |
| Modeled-risk example | Bounded modeled output | Model support remains uncertainty-bearing. |
| Stale record with no current alternative | `ABSTAIN` / `SOURCE_STALE` | Freshness state is visible and bounded. |
| Missing evidence support | `ABSTAIN` | Cite-or-abstain blocks unsupported claims. |
| Incomplete contract-shaped payload | Validation failure or `ERROR` | Contract shape must not be silently accepted. |
| Management-context example | Informational only | Fixture must not become an operational instruction. |

## Maintenance notes

- Update this README when payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each fixture to the schema check, semantic-contract review, governed-API test, Evidence Drawer test, Focus Mode test, renderer check, policy check, or documentation example that consumes it.
- If a fixture becomes stable enough to anchor a regression check, pair it with an expected output and document the consumer.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real or restricted material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: populated from empty placeholder content.
- Fixture payload inventory: no payloads verified in this directory during this update.
- Contract alignment: PARTIALLY VERIFIED against `contracts/domains/flora/invasive_plant_record.md`.
- Schema alignment: NEEDS VERIFICATION because the paired schema is present but remains a permissive `PROPOSED` scaffold.
- Consumer alignment: NEEDS VERIFICATION against validators, renderer checks, governed-API tests, Evidence Drawer tests, Focus Mode tests, and policy checks.
- Tests and validators: NOT RUN.

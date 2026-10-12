# Flora synthetic fixtures

`fixtures/domains/flora/synthetic/`

Status: draft / fixture lane / synthetic toy-data support.

This directory is for small synthetic Flora fixture examples that support bounded schema checks, semantic-contract reviews, renderer checks, governed API examples, Evidence Drawer examples, Focus Mode examples, source-admission dry-runs, watcher dry-runs, and documentation examples. Synthetic fixtures are intentionally toy examples. They are not real Flora records and must not be treated as source truth, catalog truth, release proof, or publication state.

These files are examples only. They are not authoritative project records, source records, EvidenceBundles, source descriptors, policy decisions, review approvals, release state, public API material, public map material, public tiles, or published artifacts.

## Relationship to sibling lanes

Use this lane for synthetic examples that do not yet belong to a more specific Flora fixture lane.

Prefer a specific sibling lane when the example clearly belongs there:

| Sibling lane | Use when |
|---|---|
| `golden/` | The file is an expected output for a stable input. |
| `invalid/` | The file is intentionally rejected or expected to produce a bounded non-answer. |
| `plant_taxon/` | The file primarily exercises PlantTaxon identity or crosswalk behavior. |
| `flora_occurrence/` | The file primarily exercises occurrence semantics. |
| `rare_plant_record/` | The file primarily exercises rare-plant restricted/public-safe posture. |
| `invasive_plant_record/` | The file primarily exercises invasive-plant semantics. |
| `phenology_observation/` | The file primarily exercises seasonal/time-series semantics. |
| `source_descriptors/` or `sources/` | The file primarily exercises source-family or source-admission behavior. |
| `evidence_bundles/` | The file primarily exercises EvidenceBundle or catalog-closure examples. |
| `plants_drift/` | The file primarily exercises plants-source drift/watch behavior. |

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic fixture examples, not governed lifecycle data. It is not a `data/`, `policy/`, `schemas/`, `contracts/`, `connectors/`, `release/`, proof, source-registry, or publication root.

The root fixture README states that fixtures are operational/runtime examples, not canonical truth, and that RAW, WORK, or QUARANTINE data does not belong here. This README inherits those boundaries.

## Related references

- `../README.md`
- `../../README.md`
- `../golden/README.md`
- `../invalid/README.md`
- `../plant_taxon/README.md`
- `../flora_occurrence/README.md`
- `../rare_plant_record/README.md`
- `../invasive_plant_record/README.md`
- `../phenology_observation/README.md`
- `../source_descriptors/README.md`
- `../sources/README.md`
- `../plants_drift/README.md`
- `../evidence_bundles/README.md`
- `../../../../docs/domains/flora/MISSING_OR_PLANNED_FILES.md`
- `../../../../docs/domains/flora/API_CONTRACTS.md`
- `../../../../docs/domains/flora/MAP_UI_CONTRACTS.md`
- `../../../../docs/domains/flora/SENSITIVITY.md`
- `../../../../contracts/domains/flora/`
- `../../../../schemas/contracts/v1/domains/flora/`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.expected.json`, `*.json`, `*.geojson`, `*.jsonl`, `*.yaml`, `*.yml`, or `*.md` examples;
- toy records for early review before a specific fixture lane is chosen;
- synthetic cross-lane examples that combine taxonomy, occurrence, evidence, source, and runtime-envelope concepts without becoming canonical examples;
- toy public-safe geometries, toy IDs, toy source labels, toy taxon labels, toy time values, toy evidence references, and toy expected outcomes;
- examples that prove generated or fixture-only content is not promoted into evidence, registry authority, catalog closure, release authority, or public output;
- paired expected outputs in `../golden/` when behavior becomes a stable regression anchor.

## Exclusions

Do not use this lane for real source data, real upstream payloads, credentials, lifecycle data, registry authority, release artifacts, proof packs, policy rules, connector or pipeline implementation code, public API payloads, public map data, public tiles, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, and reviewable.
- Use toy identifiers, toy taxa, toy sources, toy times, toy evidence references, and toy geometries unless a bounded check explicitly requires a more realistic shape.
- Make the fixture purpose explicit in the file name, metadata, or paired expected output.
- Move examples into a more specific sibling lane once their object family or consumer is clear.
- Pair each input with an expected output when practical.
- Treat `synthetic`, `schema-valid`, `semantic-valid`, `evidence-resolved`, `policy-admissible`, `release-safe`, and `renderer-safe` as separate checks.
- Do not treat synthetic fixtures as source authority, evidence, approval, release state, schema authority, implementation proof, or published output.

## Expected synthetic fixture examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Toy Flora record used for first-pass schema review | Review fixture | Move to object-specific lane when stable. |
| Toy cross-lane example joining taxon, source, and evidence concepts | Review fixture | Must preserve source/evidence boundaries. |
| Toy public-safe geometry example | Renderer fixture | Must not imply real location or source truth. |
| Toy generated record | Synthetic-only output | Must not become EvidenceBundle or catalog truth. |
| Synthetic fixture later becomes a regression anchor | Move or pair with `golden/` | Expected output belongs in `golden/`. |
| Synthetic fixture intentionally fails | Move or pair with `invalid/` | Failure intent belongs in `invalid/`. |

## Maintenance notes

- Update this README when payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Keep this lane small; prefer object-specific sibling lanes for stable examples.
- Link each fixture to the validator, renderer check, governed-API test, Evidence Drawer test, Focus Mode test, policy check, or documentation example that consumes it.
- If a fixture becomes stable enough to anchor a regression check, pair it with an expected output and document the consumer.
- If a fixture accidentally includes real source material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: populated from empty placeholder content.
- Fixture payload inventory: no payloads verified in this directory during this update.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Sibling fixture alignment: PARTIALLY VERIFIED against populated Flora `golden/` and `invalid/` READMEs.
- Consumer alignment: NEEDS VERIFICATION against validators, renderer checks, governed-API tests, Evidence Drawer tests, Focus Mode tests, schema checks, and policy checks.
- Tests and validators: NOT RUN.

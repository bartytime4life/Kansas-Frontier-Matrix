# Flora phenology-observation fixtures

`fixtures/domains/flora/phenology_observation/`

Status: draft / fixture lane / semantic-contract support.

This directory is for small synthetic Flora `PhenologyObservation` fixture examples used by bounded schema checks, semantic-contract reviews, time-series checks, renderer checks, governed API tests, Evidence Drawer examples, Focus Mode examples, and documentation dry-runs. These fixtures may represent toy seasonal-state observations, survey snapshots, specimen-derived phenology, aggregate summaries, modeled seasonal timing, or refusal cases, but they are not real phenology records and must not be treated as source truth, catalog truth, release proof, or publication state.

These files are examples only. They are not authoritative project records, source records, EvidenceBundles, source descriptors, policy decisions, rights approvals, review approvals, release state, public API material, public map material, public tiles, or published artifacts.

## Contract and schema posture

The semantic contract for `PhenologyObservation` is present at `contracts/domains/flora/phenology_observation.md`. It describes the object as an evidence-bound, time-aware record of plant seasonal state, including flowering, leaf-out, fruiting, senescence, dormancy, survey snapshots, specimen-derived phenology, aggregate summaries, and modeled seasonal timing.

The paired schema at `schemas/contracts/v1/domains/flora/phenology_observation.schema.json` is present but still a `PROPOSED` scaffold with no declared properties and `additionalProperties: true`. Fixtures in this lane may support semantic review and future validator work, but they do not prove field-level machine enforcement until the schema, validators, and tests are upgraded and run.

## Placement basis

Directory rules and the root fixture README keep fixture material under the `fixtures/` responsibility root. This lane is therefore a Flora-domain fixture lane for phenology-observation examples, not a data lifecycle root, not a source registry, not a catalog root, not a proof root, not a policy root, not a schema root, not a release root, and not a publication target.

The root fixture README states that `fixtures/` is for operational rendering inputs rather than validator-only test data. It also states that fixture corpora must not contain RAW, WORK, QUARANTINE data, restricted geospatial detail, or canonical truth. This README inherits those boundaries.

## Related fixture and doctrine references

- `../README.md`
- `../../README.md`
- `../flora_occurrence/README.md`
- `../golden/README.md`
- `../invalid/README.md`
- `../evidence_bundles/README.md`
- `../../../../contracts/domains/flora/phenology_observation.md`
- `../../../../contracts/domains/flora/flora_occurrence.md`
- `../../../../contracts/domains/flora/plant_taxon.md`
- `../../../../contracts/domains/flora/flora_taxon_crosswalk.md`
- `../../../../contracts/domains/flora/specimen_record.md`
- `../../../../contracts/domains/flora/botanical_survey.md`
- `../../../../contracts/domains/flora/vegetation_community.md`
- `../../../../contracts/domains/flora/restoration_planting.md`
- `../../../../contracts/domains/flora/redaction_receipt.md`
- `../../../../schemas/contracts/v1/domains/flora/phenology_observation.schema.json`
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
- toy phenology observation examples for positive-path and negative-path checks;
- public-safe seasonal-state, survey snapshot, specimen-derived, aggregate, modeled, or synthetic examples;
- examples that keep plant subject, phenophase, time support, place support, source role, and evidence support separate;
- examples that prove modeled, aggregate, candidate, or administrative support is not silently upgraded into observed fact;
- examples that prove stale support, missing evidence, unresolved taxonomy, policy denial, or release-state gaps produce bounded outcomes;
- paired expected outputs in `../golden/` when behavior becomes a stable regression anchor;
- README files explaining fixture intent and boundaries.

## Exclusions

Do not use this lane for real source data, lifecycle data, release artifacts, proof packs, policy rules, implementation code, public map data, public API payloads, public tiles, operational advice, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, and reviewable.
- Use toy identifiers, toy taxa, toy source names, toy source roles, toy timestamps, toy evidence references, toy phenophase labels, and toy geometries unless a bounded check explicitly requires a more realistic shape.
- Make record posture explicit: observed phase, specimen-derived state, survey snapshot, time-series point, aggregate summary, modeled phase, administrative window, candidate report, or synthetic example.
- Keep source role, taxon state, phenophase state, evidence state, time precision, rights state, policy state, freshness state, review state, release state, correction state, and expected outcome explicit where material.
- Prefer no geometry unless the fixture explicitly needs geometry. When geometry is required, use toy or public-safe generalized geometry.
- Pair each input with an expected output when practical.
- Treat `schema-valid`, `semantic-valid`, `taxon-resolved`, `phenophase-resolved`, `time-bounded`, `evidence-resolved`, `policy-admissible`, `release-safe`, and `renderer-safe` as separate checks.
- Do not treat phenology fixtures as evidence, approval, release state, source authority, schema authority, implementation proof, operational guidance, or published output.

## Expected fixture examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Public-safe seasonal-state record with resolved synthetic support | `ANSWER` | Demonstrates positive path without becoming source truth. |
| Modeled bloom-window example | Bounded modeled output | Modeled support remains uncertainty-bearing. |
| Aggregate seasonal summary | Bounded aggregate output | Aggregate support must not become a direct observation. |
| Missing evidence support | `ABSTAIN` | Cite-or-abstain blocks unsupported claims. |
| Unresolved taxon or phenophase mapping | `ABSTAIN` | Crosswalk uncertainty remains visible. |
| Stale seasonal support with no current alternative | `ABSTAIN` / `SOURCE_STALE` | Freshness state is visible and bounded. |
| Incomplete contract-shaped payload | Validation failure or `ERROR` | Contract shape must not be silently accepted. |

## Maintenance notes

- Update this README when payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each fixture to the schema check, semantic-contract review, time-series check, governed-API test, Evidence Drawer test, Focus Mode test, renderer check, policy check, or documentation example that consumes it.
- If a fixture becomes stable enough to anchor a regression check, pair it with an expected output and document the consumer.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real or restricted material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: populated from empty placeholder content.
- Fixture payload inventory: no payloads verified in this directory during this update.
- Contract alignment: PARTIALLY VERIFIED against `contracts/domains/flora/phenology_observation.md`.
- Schema alignment: NEEDS VERIFICATION because the paired schema is present but remains a permissive `PROPOSED` scaffold.
- Consumer alignment: NEEDS VERIFICATION against validators, time-series checks, renderer checks, governed-API tests, Evidence Drawer tests, Focus Mode tests, and policy checks.
- Tests and validators: NOT RUN.

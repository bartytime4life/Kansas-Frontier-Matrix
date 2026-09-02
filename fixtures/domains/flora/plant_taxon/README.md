# Flora plant-taxon fixtures

`fixtures/domains/flora/plant_taxon/`

Status: draft / fixture lane / semantic-contract support.

This directory is for small synthetic Flora `PlantTaxon` fixture examples used by bounded schema checks, semantic-contract reviews, taxonomy and crosswalk checks, governed API tests, Evidence Drawer examples, Focus Mode examples, and documentation dry-runs. These fixtures may represent toy accepted names, candidate names, source-native labels, synonyms, deprecated names, rank states, or crosswalk situations, but they are not taxonomic authority and must not be treated as source truth, catalog truth, release proof, or publication state.

These files are examples only. They are not authoritative project records, source records, EvidenceBundles, source descriptors, policy decisions, review approvals, release state, public API material, public map material, public tiles, or published artifacts.

## Contract and schema posture

The semantic contract for `PlantTaxon` is present at `contracts/domains/flora/plant_taxon.md`. It describes the object as the evidence-bound botanical identity object used to anchor plant names, accepted or candidate taxonomy, source taxon labels, synonyms, rank, status, provenance, crosswalks, correction, and rollback.

The paired schema at `schemas/contracts/v1/domains/flora/plant_taxon.schema.json` is present but still a `PROPOSED` scaffold with no declared properties and `additionalProperties: true`. Fixtures in this lane may support semantic review and future validator work, but they do not prove field-level machine enforcement until the schema, validators, and tests are upgraded and run.

## Placement basis

This lane belongs under `fixtures/` because it contains fixture examples, not governed lifecycle data. It is not a `data/`, `policy/`, `schemas/`, `contracts/`, `release/`, or publication root.

The root fixture README states that fixtures are operational/runtime examples, not canonical truth, and that RAW, WORK, or QUARANTINE data does not belong here.

## Related references

- `../README.md`
- `../../README.md`
- `../golden/README.md`
- `../invalid/README.md`
- `../flora_occurrence/README.md`
- `../invasive_plant_record/README.md`
- `../phenology_observation/README.md`
- `../evidence_bundles/README.md`
- `../../../../contracts/domains/flora/plant_taxon.md`
- `../../../../contracts/domains/flora/flora_taxon_crosswalk.md`
- `../../../../contracts/domains/flora/domain_feature_identity.md`
- `../../../../contracts/domains/flora/flora_occurrence.md`
- `../../../../contracts/domains/flora/specimen_record.md`
- `../../../../contracts/domains/flora/invasive_plant_record.md`
- `../../../../contracts/domains/flora/phenology_observation.md`
- `../../../../schemas/contracts/v1/domains/flora/plant_taxon.schema.json`
- `../../../../docs/domains/flora/MISSING_OR_PLANNED_FILES.md`
- `../../../../docs/domains/flora/API_CONTRACTS.md`
- `../../../../docs/domains/flora/MAP_UI_CONTRACTS.md`
- `../../../../docs/domains/flora/DATA_LIFECYCLE.md`
- `../../../../policy/domains/flora/`
- `../../../../data/registry/sources/flora/`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.expected.json`, `*.json`, `*.jsonl`, or `*.md` examples;
- toy plant-taxon identity examples for positive-path and negative-path checks;
- source-native name, synonym, rank, accepted-name, candidate-name, deprecated-name, and unresolved-name examples;
- crosswalk-oriented examples that pair with `FloraTaxonCrosswalk` fixture or test work;
- examples that prove source-native labels are preserved and not silently upgraded into accepted taxonomy;
- examples that prove conflicting concepts, unresolved names, or stale taxonomy produce bounded outcomes;
- paired expected outputs in `../golden/` when behavior becomes a stable regression anchor.

## Exclusions

Do not use this lane for real source data, lifecycle data, release artifacts, proof packs, policy rules, implementation code, public map data, public API payloads, public tiles, taxonomic authority decisions, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, and reviewable.
- Use toy identifiers, toy names, toy ranks, toy authorities, toy source names, toy source roles, toy timestamps, and toy evidence references unless a bounded check explicitly requires a more realistic shape.
- Make taxon posture explicit: accepted, candidate, synonym, deprecated, unresolved, conflicted, source-native, source-confirmed, steward-reviewed, rejected, superseded, or synthetic example.
- Keep source role, taxon state, backbone state, crosswalk state, evidence state, freshness state, review state, release state, correction state, and expected outcome explicit where material.
- Do not include direct model-runtime output, source exports, or unpublished candidate content in public-surface examples.
- Pair each input with an expected output when practical.
- Treat `schema-valid`, `semantic-valid`, `name-preserved`, `crosswalk-resolved`, `evidence-resolved`, `release-safe`, and `renderer-safe` as separate checks.
- Do not treat plant-taxon fixtures as taxonomic authority, evidence, approval, release state, source authority, schema authority, implementation proof, management guidance, or published output.

## Expected fixture examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Public-safe reviewed toy taxon with resolved synthetic support | `ANSWER` | Demonstrates positive path without becoming taxonomic authority. |
| Source-native label without accepted-name support | `ABSTAIN` or candidate output | Source label remains auditable. |
| Synonym maps cleanly to reviewed toy identity | Bounded accepted/crosswalk output | Preserve synonym and source-native form. |
| Conflicting taxon concepts | `ABSTAIN` / `CONFLICTED_SUPPORT` | Conflicts must not be merged silently. |
| Deprecated or superseded toy name | Supersession output | Correction and rollback posture remain visible. |
| Missing evidence support | `ABSTAIN` | Cite-or-abstain blocks unsupported identity claims. |
| Incomplete contract-shaped payload | Validation failure or `ERROR` | Contract shape must not be silently accepted. |

## Maintenance notes

- Update this README when payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each fixture to the schema check, semantic-contract review, taxonomy resolver, crosswalk test, governed-API test, Evidence Drawer test, Focus Mode test, renderer check, policy check, or documentation example that consumes it.
- If a fixture becomes stable enough to anchor a regression check, pair it with an expected output and document the consumer.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: populated from empty placeholder content.
- Fixture payload inventory: no payloads verified in this directory during this update.
- Contract alignment: PARTIALLY VERIFIED against `contracts/domains/flora/plant_taxon.md`.
- Schema alignment: NEEDS VERIFICATION because the paired schema is present but remains a permissive `PROPOSED` scaffold.
- Consumer alignment: NEEDS VERIFICATION against validators, taxonomy resolver checks, crosswalk checks, governed-API tests, Evidence Drawer tests, Focus Mode tests, and policy checks.
- Tests and validators: NOT RUN.

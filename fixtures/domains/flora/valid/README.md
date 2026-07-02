# Flora valid fixtures

`fixtures/domains/flora/valid/`

Status: draft / fixture lane / positive-path support.

This directory is for small synthetic Flora examples that are expected to pass bounded checks or produce governed positive-path outputs. Valid fixtures support review of schema behavior, semantic-contract behavior, renderer behavior, governed API behavior, Evidence Drawer behavior, Focus Mode behavior, source-admission dry-runs, watcher dry-runs, and documentation examples.

These files are examples only. They are not authoritative project records, source records, EvidenceBundles, source descriptors, policy decisions, review approvals, release state, public API material, public map material, public tiles, or published artifacts.

## Relationship to sibling lanes

Use this lane for synthetic positive-path inputs. Expected outputs should usually live in `../golden/`, and intentionally failing examples should live in `../invalid/`.

Prefer a more specific sibling lane when the fixture clearly belongs to one object family or consumer:

| Sibling lane | Use when |
|---|---|
| `plant_taxon/` | The fixture primarily exercises PlantTaxon identity or crosswalk behavior. |
| `flora_occurrence/` | The fixture primarily exercises occurrence semantics. |
| `rare_plant_record/` | The fixture primarily exercises rare-plant restricted/public-safe posture. |
| `invasive_plant_record/` | The fixture primarily exercises invasive-plant semantics. |
| `phenology_observation/` | The fixture primarily exercises seasonal/time-series semantics. |
| `source_descriptors/` or `sources/` | The fixture primarily exercises source-family or source-admission behavior. |
| `evidence_bundles/` | The fixture primarily exercises EvidenceBundle or catalog-closure examples. |
| `plants_drift/` | The fixture primarily exercises plants-source drift/watch behavior. |
| `synthetic/` | The fixture is still exploratory and not yet object-family specific. |

## Placement basis

This lane belongs under `fixtures/` because it contains fixture examples, not governed lifecycle data. It is not a `data/`, `policy/`, `schemas/`, `contracts/`, `connectors/`, `release/`, proof, source-registry, or publication root.

The root fixture README states that fixtures are operational/runtime examples, not canonical truth, and that RAW, WORK, or QUARANTINE data does not belong here. This README inherits those boundaries.

## Related references

- `../README.md`
- `../../README.md`
- `../golden/README.md`
- `../invalid/README.md`
- `../synthetic/README.md`
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

- small synthetic `*.input.json`, `*.valid.json`, `*.json`, `*.geojson`, `*.jsonl`, `*.yaml`, `*.yml`, or `*.md` examples;
- positive-path inputs expected to pass schema, semantic, renderer, governed-API, Evidence Drawer, Focus Mode, source-admission, or watcher dry-run checks;
- toy public-safe records with toy IDs, toy taxon labels, toy source labels, toy time values, toy evidence references, and toy geometries;
- examples that keep source role, evidence state, rights state, policy state, freshness state, review state, release state, correction state, and expected output state explicit where material;
- examples that prove positive validation does not create evidence, registry authority, catalog closure, release authority, or public output;
- paired expected outputs in `../golden/` when behavior becomes a stable regression anchor.

## Exclusions

Do not use this lane for real source data, real upstream payloads, credentials, lifecycle data, registry authority, release artifacts, proof packs, policy rules, connector or pipeline implementation code, public API payloads, public map data, public tiles, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, and reviewable.
- Use toy identifiers, toy taxa, toy sources, toy times, toy evidence references, and toy geometries unless a bounded check explicitly requires a more realistic shape.
- Make the expected positive-path behavior explicit in the file name, metadata, or paired expected output.
- Pair each valid input with an expected output in `../golden/` when practical.
- Move examples into a more specific sibling lane once their object family or consumer is clear.
- Treat `schema-valid`, `semantic-valid`, `evidence-resolved`, `policy-admissible`, `release-safe`, and `renderer-safe` as separate checks.
- Do not treat valid fixtures as source authority, evidence, approval, release state, schema authority, implementation proof, or published output.

## Expected valid fixture examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Toy public-safe Flora record with complete synthetic support | Positive fixture input | Pair expected output in `../golden/`. |
| Toy taxon identity with resolved synthetic crosswalk | Positive fixture input | Prefer `../plant_taxon/` once stable. |
| Toy occurrence-like record with public-safe generalized geometry | Positive fixture input | Must not imply real occurrence truth. |
| Toy source descriptor with complete synthetic support | Positive fixture input | Prefer `../source_descriptors/` once stable. |
| Toy EvidenceBundle closure example | Positive fixture input | Prefer `../evidence_bundles/` once stable. |
| Toy renderer-safe geometry payload | Positive fixture input | Must remain public-safe and synthetic. |

## Maintenance notes

- Update this README when payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Keep this lane focused on positive-path inputs; move stable expected outputs to `../golden/` and negative examples to `../invalid/`.
- Link each fixture to the validator, renderer check, governed-API test, Evidence Drawer test, Focus Mode test, policy check, or documentation example that consumes it.
- If a fixture becomes object-family specific, move it to the appropriate sibling lane and leave a migration note if needed.
- If a fixture accidentally includes real source material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: populated from empty placeholder content.
- Fixture payload inventory: no payloads verified in this directory during this update.
- Flora fixture backlog alignment: PARTIALLY VERIFIED against the Flora missing/planned-files register and sibling fixture READMEs.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, renderer checks, governed-API tests, Evidence Drawer tests, Focus Mode tests, schema checks, and policy checks.
- Tests and validators: NOT RUN.

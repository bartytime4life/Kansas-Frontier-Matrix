# Geology unit fixtures

`fixtures/domains/geology/units/`

Status: draft / fixture lane / GeologicUnit and map-unit examples.

This directory is for small synthetic Geology unit fixture examples used by bounded semantic-contract reviews, future schema checks, topology checks, renderer checks, governed API examples, Evidence Drawer examples, Focus Mode examples, source-role checks, public-safe layer examples, pipeline dry-runs, and documentation dry-runs. These fixtures may represent toy `GeologicUnit`, source map-unit, legend-row, boundary-version, lithology-reference, age-reference, stratigraphic-context, public-safe derivative, candidate, invalid, or non-answer cases, but they are not real geology records, source truth, lifecycle data, public tiles, release proof, or publication state.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, source descriptors, proof packs, review approvals, release state, public API material, public map material, public tiles, or published artifacts.

## Contract posture

The Geology file-system plan identifies `GeologicUnit` as a core owned object family covering bedrock and surficial mapped units, with generalized polygons public-safe when source rights allow. The `GeologicUnit` semantic contract is present and describes the object as an evidence-bound mapped-unit assertion with unit symbols, polygons, interpretation versions, lithology and age references, boundary lineage, public-safe derivatives, correction, and rollback.

The same contract says field-level schema shape, fixtures, validators, source registry records, policy runtime, release workflow, API behavior, UI behavior, and test coverage remain `NEEDS VERIFICATION`. This fixture lane can support that work, but it does not prove schema enforcement or implementation maturity by itself.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic fixture examples, not governed lifecycle data. It is not a `data/`, `policy/`, `schemas/`, `contracts/`, `pipelines/`, `pipeline_specs/`, `connectors/`, `release/`, proof, source-registry, catalog, triplet, tile, or publication root.

The root fixture README states that fixtures are operational/runtime examples, not canonical truth, and that RAW, WORK, or QUARANTINE data does not belong here. This README inherits those boundaries.

## Relationship to sibling lanes

Use this lane for GeologicUnit and map-unit examples where unit semantics are the main purpose.

| Sibling lane | Relationship |
|---|---|
| `../golden/` | Stable expected outputs for unit examples may be paired there. |
| `../invalid/` | Negative-path unit inputs may move there when the failure posture is the main purpose. |
| `../map-ui/` | Map/UI envelope examples may reference unit fixture inputs. |
| `../source_role/` | Source-role examples may be referenced when unit source role is being tested. |
| `../tier-transitions/` | Release-tier, redaction, generalization, or withdrawal examples may reference unit fixtures. |
| `../sublanes/surficial/` | SurficialUnit-specific examples belong there when the surficial sublane is the main purpose. |
| `../cross_sections/` | Cross-section examples may reference unit fixtures without replacing CrossSection authority. |

## Related references

- `../README.md`
- `../../README.md`
- `../golden/README.md`
- `../invalid/README.md`
- `../map-ui/README.md`
- `../source_role/README.md`
- `../tier-transitions/README.md`
- `../sublanes/README.md`
- `../sublanes/surficial/README.md`
- `../cross_sections/README.md`
- `../../../../contracts/domains/geology/GeologicUnit.md`
- `../../../../contracts/domains/geology/GeologicAge.md`
- `../../../../contracts/domains/geology/Lithology.md`
- `../../../../contracts/domains/geology/StratigraphicInterval.md`
- `../../../../contracts/domains/geology/GeologyBoundaryVersion.md`
- `../../../../contracts/domains/geology/CrossSection.md`
- `../../../../docs/domains/geology/FILE_SYSTEM_PLAN.md`
- `../../../../docs/domains/geology/OBJECT_FAMILIES.md`
- `../../../../docs/domains/geology/ARCHITECTURE.md`
- `../../../../docs/domains/geology/MAP_UI_CONTRACTS.md`
- `../../../../docs/domains/geology/API_CONTRACTS.md`
- `../../../../docs/domains/geology/SOURCE_REGISTRY.md`
- `../../../../schemas/contracts/v1/domains/geology/`
- `../../../../policy/domains/geology/`
- `../../../../data/registry/sources/geology/`
- `../../../../release/manifests/geology/`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.expected.json`, `*.json`, `*.geojson`, `*.jsonl`, `*.yaml`, `*.yml`, or `*.md` examples;
- toy `GeologicUnit` examples for positive-path and negative-path checks;
- toy source map-unit, legend-row, unit-symbol, unit-name, correlation-unit, composite-unit, or public-derivative examples;
- toy geometry, CRS, topology, boundary-version, map-provenance, interpretation-version, source-vintage, lithology-reference, age-reference, interval-reference, and evidence-reference examples;
- toy unit examples for source-role checks, tier-transition checks, Evidence Drawer examples, Focus Mode examples, renderer checks, topology checks, and public-safe layer dry-runs;
- examples that prove a unit does not silently become Lithology, GeologicAge, StratigraphicInterval, GeologyBoundaryVersion, CrossSection, SurficialUnit, Soil truth, Hydrology measurement, Hazards risk, People/Land truth, AI evidence, or public-release approval;
- paired expected outputs in `../golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for real geology records, real source exports, live upstream fetch results, lifecycle data, real EvidenceBundles, proof packs, run receipts, release manifests, correction notices, review records, implementation code, public API material, public map material, public tiles, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, and reviewable.
- Use toy unit IDs, toy source IDs, toy map names, toy unit symbols, toy unit names, toy boundary-version IDs, toy evidence references, toy timestamps, toy hashes, and toy geometries unless a bounded check explicitly requires a more realistic shape.
- Make unit posture explicit: bedrock unit, source map unit, legend row, correlation unit, composite unit, candidate, synthetic, invalid, generalized public derivative, or released-output expectation.
- Keep source role, evidence state, interpretation version, source vintage, rights state, geometry lineage, topology state, policy state, review state, release state, correction state, rollback state, and expected outcome explicit where material.
- Prefer public-safe generalized geometry. Do not include geometry that could reasonably be mistaken for sensitive real-world data.
- Pair each input with an expected output when practical.
- Treat `schema-valid`, `semantic-valid`, `source-role-valid`, `vocabulary-resolved`, `evidence-resolved`, `topology-valid`, `generalization-recorded`, `policy-admissible`, `citation-safe`, `release-safe`, and `renderer-safe` as separate checks.
- Do not treat unit fixtures as source authority, evidence, release state, schema authority, implementation proof, public-map authority, tile authority, or published output.

## Expected unit fixture examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Synthetic public-safe GeologicUnit polygon with toy source support | Valid input or `ANSWER` output | Demonstrates positive path without becoming source truth. |
| Unit missing map provenance | `ABSTAIN` or validation failure | Map provenance remains part of unit support. |
| Unit missing interpretation version | Validation failure or review-required output | Interpretation version is required for derived map-unit use. |
| Unit treated as Lithology or GeologicAge | `ABSTAIN` or validation failure | Linked support objects keep separate identity. |
| Unit treated as Soil, Hydrology, or Hazards truth | `ABSTAIN` | Adjacent-domain authority remains separate. |
| Public derivative without release manifest or rollback target | Validation failure or review-required output | Public-safe display requires governed release posture. |
| Invalid topology or CRS | Validation failure or `ERROR` | Geometry safety remains separate from semantic validity. |

## Maintenance notes

- Update this README when payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each fixture to the semantic-contract review, future schema check, topology check, renderer check, governed-API test, Evidence Drawer test, Focus Mode test, source-role check, tier-transition check, policy check, or documentation example that consumes it.
- If a fixture becomes stable enough to anchor a regression check, pair it with an expected output and document the consumer.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real source material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: populated from empty placeholder content.
- Fixture payload inventory: no payloads verified in this directory during this update.
- GeologicUnit contract alignment: PARTIALLY VERIFIED against `contracts/domains/geology/GeologicUnit.md`.
- Schema alignment: NEEDS VERIFICATION because the GeologicUnit contract reports the exact paired schema path was not confirmed in-session.
- Geology file-system alignment: PARTIALLY VERIFIED against `docs/domains/geology/FILE_SYSTEM_PLAN.md`.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Sibling fixture alignment: NEEDS VERIFICATION against populated `golden/`, `invalid/`, `map-ui/`, `source_role/`, `tier-transitions/`, `sublanes/`, and `cross_sections/` READMEs.
- Consumer alignment: NEEDS VERIFICATION against validators, topology checks, renderer checks, governed-API tests, Evidence Drawer tests, Focus Mode tests, pipeline dry-runs, source-role checks, tier-transition checks, schema checks, and policy checks.
- Tests and validators: NOT RUN.

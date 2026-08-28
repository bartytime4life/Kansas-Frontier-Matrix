# Geology cross-section fixtures

`fixtures/domains/geology/cross_sections/`

Status: draft / fixture lane / CrossSection semantic and pipeline dry-run support.

This directory is for small synthetic Geology `CrossSection` fixture examples used by bounded semantic-contract reviews, future schema checks, cross-section pipeline dry-runs, topology/rendering checks, governed API tests, Evidence Drawer examples, Focus Mode examples, and documentation dry-runs. These fixtures may represent toy section traces, interpretive panels, stratigraphic correlation examples, borehole/well-log reference examples, uncertainty bands, public-safe derivative panels, or refusal cases, but they are not real cross sections and must not be treated as source truth, subsurface truth, resource proof, release proof, or publication state.

These files are examples only. They are not authoritative project records, source records, EvidenceBundles, source descriptors, policy decisions, review approvals, release state, public API material, public map material, public tiles, public diagrams, reserve/resource estimates, permit/title evidence, or published artifacts.

## Contract and schema posture

The semantic contract for `CrossSection` is present at `contracts/domains/geology/CrossSection.md`. It describes `CrossSection` as the evidence-bound object for 2D / 2.5D interpretive subsurface sections, section traces, panels, vertical scales, correlation surfaces, uncertainty bands, evidence inputs, public-safe derivatives, correction, and rollback.

The contract states that the exact paired schema path `schemas/contracts/v1/domains/geology/CrossSection.schema.json` was not found in that session, and that field-level schema shape, fixtures, validators, policy runtime, source registry records, release workflow, API behavior, UI behavior, rendering behavior, and test coverage remain `NEEDS VERIFICATION`. Fixtures in this lane may support semantic review and future validator work, but they do not prove field-level machine enforcement until schema, validators, and tests are added and run.

## Pipeline posture

The cross-sections pipeline README describes `pipelines/domains/geology/cross_sections/` as executable support for assembling evidence-bound geologic cross-section candidates, quarantine records, normalized section panels, catalog/triplet handoffs, receipts, and release-review packages. It also states that cross-section pipeline logic does not own source descriptors, source catalog profiles, connectors, schemas, policy, lifecycle data, catalog truth, geology truth, or release decisions.

This fixture lane is not executable pipeline logic. It supplies toy inputs, expected shapes, and dry-run examples that pipeline and validator work may consume later.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic fixture examples, not governed lifecycle data. It is not a `data/`, `policy/`, `schemas/`, `contracts/`, `pipelines/`, `pipeline_specs/`, `connectors/`, `release/`, proof, source-registry, catalog, triplet, or publication root.

The root fixture README states that fixtures are operational/runtime examples, not canonical truth, and that RAW, WORK, or QUARANTINE data does not belong here. The Geology file-system plan identifies `fixtures/domains/geology/` as the Geology fixture home for golden, valid, and invalid samples. This README inherits those boundaries.

## Related references

- `../README.md`
- `../../README.md`
- `../../../../contracts/domains/geology/CrossSection.md`
- `../../../../contracts/domains/geology/BoreholeReference.md`
- `../../../../contracts/domains/geology/CoreSample.md`
- `../../../../contracts/domains/geology/StratigraphicInterval.md`
- `../../../../contracts/domains/geology/StructureFeature.md`
- `../../../../docs/domains/geology/FILE_SYSTEM_PLAN.md`
- `../../../../docs/domains/geology/OBJECT_FAMILIES.md`
- `../../../../docs/domains/geology/API_CONTRACTS.md`
- `../../../../docs/domains/geology/sublanes/stratigraphy.md`
- `../../../../docs/domains/geology/sublanes/bedrock_geology.md`
- `../../../../docs/domains/geology/sublanes/surficial.md`
- `../../../../docs/domains/geology/sublanes/boreholes-wells.md`
- `../../../../pipelines/domains/geology/cross_sections/README.md`
- `../../../../pipeline_specs/geology/cross_sections.yaml`
- `../../../../policy/domains/geology/`
- `../../../../policy/sensitivity/geology/`
- `../../../../data/registry/sources/geology/`
- `../../../../release/manifests/geology/`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.expected.json`, `*.json`, `*.geojson`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy `CrossSection` inputs for positive-path and negative-path checks;
- toy section traces, panel metadata, vertical datum references, vertical exaggeration values, interpretation-version labels, and display envelopes;
- toy stratigraphic interval, borehole, well-log, core, measured-section, mapped-unit, structure, or geophysical reference examples;
- public-safe generalized section examples and renderer-safe diagram examples;
- examples that keep observed evidence, inferred interpretation, modeled surfaces, generalized display, policy state, release state, correction state, and rollback state separate;
- examples that prove a cross-section panel is not silently upgraded into direct observation, canonical map truth, resource proof, or public-release approval;
- paired expected outputs in sibling `golden/` lanes if those lanes are later created and documented.

## Exclusions

Do not use this lane for real source data, real well records, real private-well details, proprietary subsurface interpretations, real upstream payloads, credentials, lifecycle data, registry authority, release artifacts, proof packs, policy rules, executable pipeline code, public API payloads, public map data, public tiles, reserve/resource estimates, permit/title evidence, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, and reviewable.
- Use toy identifiers, toy section names, toy line geometries, toy well IDs, toy depths, toy units, toy horizons, toy timestamps, toy evidence references, and toy source labels unless a bounded check explicitly requires a more realistic shape.
- Make interpretation posture explicit: observed support, inferred contact, modeled horizon, schematic panel, generalized public derivative, candidate interpretation, or synthetic example.
- Keep source role, evidence state, vertical datum, scale, vertical exaggeration, uncertainty, topology state, sensitivity state, review state, release state, correction state, and expected outcome explicit where material.
- Prefer no real-looking coordinates unless the fixture explicitly needs geometry. When geometry is required, use toy or public-safe generalized geometry.
- Pair each input with an expected output when practical.
- Treat `schema-valid`, `semantic-valid`, `evidence-resolved`, `interpretation-bounded`, `topology-valid`, `renderer-safe`, `policy-admissible`, and `release-safe` as separate checks.
- Do not treat cross-section fixtures as subsurface truth, evidence, source authority, schema authority, implementation proof, approval, release state, or published output.

## Expected fixture examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Synthetic public-safe cross-section candidate with resolved toy support | `ANSWER` or valid candidate output | Demonstrates positive path without becoming subsurface truth. |
| Inferred contact lacking evidence support | `ABSTAIN` | Interpretation cannot become observed contact. |
| Missing vertical datum or vertical exaggeration disclosure | Validation failure or `ERROR` | Display semantics must remain explicit. |
| Modeled horizon presented as observed contact | `ABSTAIN` or review-required output | Source-role and interpretation class remain visible. |
| Section panel used as reserve/resource proof | `DENY` or `ABSTAIN` | Resource claims require separate governed authority. |
| Private/source-restricted well detail in public output | `DENY` or generalized derivative | Public surfaces must fail closed or use approved derivative shape. |
| Renderer-unsafe geometry or panel envelope | Validation failure or bounded error | Renderer safety remains separate from semantic validity. |

## Maintenance notes

- Update this README when payload files, sibling golden/valid/invalid lanes, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each fixture to the semantic-contract review, future schema check, cross-section pipeline dry-run, renderer check, topology check, governed-API test, Evidence Drawer test, Focus Mode test, policy check, or documentation example that consumes it.
- If a fixture becomes stable enough to anchor a regression check, pair it with an expected output and document the consumer.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real source material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: populated from empty placeholder content.
- Parent geology fixture README: present but still a greenfield stub during this update.
- Fixture payload inventory: no payloads verified in this directory during this update.
- Contract alignment: PARTIALLY VERIFIED against `contracts/domains/geology/CrossSection.md`.
- Schema alignment: NEEDS VERIFICATION because the exact paired schema path was not confirmed in the CrossSection contract evidence.
- Pipeline alignment: PARTIALLY VERIFIED against `pipelines/domains/geology/cross_sections/README.md`.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, topology checks, renderer checks, governed-API tests, Evidence Drawer tests, Focus Mode tests, pipeline dry-runs, schema checks, and policy checks.
- Tests and validators: NOT RUN.

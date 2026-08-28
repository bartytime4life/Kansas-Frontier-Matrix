# Flora vegetation-community fixtures

`fixtures/domains/flora/vegetation_community/`

Status: draft / fixture lane / semantic-contract support.

This directory is for small synthetic Flora `VegetationCommunity` fixture examples used by bounded schema checks, semantic-contract reviews, topology and renderer checks, governed API tests, Evidence Drawer examples, Focus Mode examples, and documentation dry-runs. These fixtures may represent toy community polygons, plot classifications, floristic summaries, modeled community labels, aggregate community summaries, or refusal cases, but they are not real vegetation-community records and must not be treated as source truth, catalog truth, release proof, or publication state.

These files are examples only. They are not authoritative project records, source records, EvidenceBundles, source descriptors, policy decisions, review approvals, release state, public API material, public map material, public tiles, or published artifacts.

## Contract and schema posture

The semantic contract for `VegetationCommunity` is present at `contracts/domains/flora/vegetation_community.md`. It describes the object as the evidence-bound record for polygonal, plot-based, survey-derived, modeled, aggregate, or reviewed vegetation-community classification and floristic composition support.

The paired schema at `schemas/contracts/v1/domains/flora/vegetation_community.schema.json` is present but still a `PROPOSED` scaffold with no declared properties and `additionalProperties: true`. Fixtures in this lane may support semantic review and future validator work, but they do not prove field-level machine enforcement until the schema, validators, and tests are upgraded and run.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic fixture examples, not governed lifecycle data. It is not a `data/`, `policy/`, `schemas/`, `contracts/`, `release/`, proof, source-registry, or publication root.

The root fixture README states that fixtures are operational/runtime examples, not canonical truth, and that RAW, WORK, or QUARANTINE data does not belong here. The Flora backlog identifies this lane for community polygon fixtures. This README inherits those boundaries.

## Related references

- `../README.md`
- `../../README.md`
- `../golden/README.md`
- `../invalid/README.md`
- `../valid/README.md`
- `../synthetic/README.md`
- `../plant_taxon/README.md`
- `../flora_occurrence/README.md`
- `../rare_plant_record/README.md`
- `../phenology_observation/README.md`
- `../invasive_plant_record/README.md`
- `../evidence_bundles/README.md`
- `../../../../contracts/domains/flora/vegetation_community.md`
- `../../../../contracts/domains/flora/plant_taxon.md`
- `../../../../contracts/domains/flora/flora_occurrence.md`
- `../../../../contracts/domains/flora/habitat_association.md`
- `../../../../contracts/domains/flora/range_polygon.md`
- `../../../../contracts/domains/flora/botanical_survey.md`
- `../../../../contracts/domains/flora/domain_validation_report.md`
- `../../../../schemas/contracts/v1/domains/flora/vegetation_community.schema.json`
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
- toy vegetation-community examples for positive-path and negative-path checks;
- public-safe polygon, multipolygon, plot, transect, grid, modeled, aggregate, or generalized community examples;
- examples that keep community classification, source vocabulary, method, scale, uncertainty, floristic support, evidence support, and release state separate;
- examples that prove community polygons are not silently upgraded into exact species occurrence proof, habitat truth, or public-release approval;
- examples that prove missing support, unresolved vocabulary, topology problems, stale support, policy denial, or release-state gaps produce bounded outcomes;
- paired expected outputs in `../golden/` when behavior becomes a stable regression anchor.

## Exclusions

Do not use this lane for real source data, real upstream payloads, lifecycle data, release artifacts, proof packs, policy rules, implementation code, public API payloads, public map data, public tiles, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, and reviewable.
- Use toy identifiers, toy community labels, toy classification vocabularies, toy source names, toy source roles, toy timestamps, toy evidence references, and toy geometries unless a bounded check explicitly requires a more realistic shape.
- Make community posture explicit: observed plot classification, mapped polygon, modeled community, aggregate summary, candidate label, generalized public-safe derivative, or synthetic example.
- Keep source role, classification vocabulary, topology state, taxon/composition support, method state, evidence state, freshness state, review state, release state, correction state, and expected outcome explicit where material.
- Prefer no geometry unless the fixture explicitly needs geometry. When geometry is required, use toy or public-safe generalized geometry.
- Pair each input with an expected output when practical.
- Treat `schema-valid`, `semantic-valid`, `topology-valid`, `vocabulary-resolved`, `evidence-resolved`, `policy-admissible`, `release-safe`, and `renderer-safe` as separate checks.
- Do not treat vegetation-community fixtures as occurrence proof, habitat authority, evidence, approval, release state, source authority, schema authority, implementation proof, or published output.

## Expected fixture examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Public-safe synthetic community polygon with resolved support | `ANSWER` | Demonstrates positive path without becoming source truth. |
| Modeled community label | Bounded modeled output | Modeled support remains uncertainty-bearing. |
| Aggregate community summary | Bounded aggregate output | Aggregate support must not become plot-level proof. |
| Community polygon used as exact species occurrence proof | `ABSTAIN` | Community classification does not replace occurrence support. |
| Missing evidence support | `ABSTAIN` | Cite-or-abstain blocks unsupported claims. |
| Unresolved classification vocabulary | `ABSTAIN` or review-required output | Vocabulary uncertainty remains visible. |
| Topology or renderer-unsafe geometry | Validation failure or `ERROR` | Geometry problems must be bounded. |

## Maintenance notes

- Update this README when payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each fixture to the schema check, semantic-contract review, topology check, renderer check, governed-API test, Evidence Drawer test, Focus Mode test, policy check, or documentation example that consumes it.
- If a fixture becomes stable enough to anchor a regression check, pair it with an expected output and document the consumer.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real source material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: populated from empty placeholder content.
- Fixture payload inventory: no payloads verified in this directory during this update.
- Contract alignment: PARTIALLY VERIFIED against `contracts/domains/flora/vegetation_community.md`.
- Schema alignment: NEEDS VERIFICATION because the paired schema is present but remains a permissive `PROPOSED` scaffold.
- Flora fixture backlog alignment: PARTIALLY VERIFIED against the Flora missing/planned-files register.
- Consumer alignment: NEEDS VERIFICATION against validators, topology checks, renderer checks, governed-API tests, Evidence Drawer tests, Focus Mode tests, and policy checks.
- Tests and validators: NOT RUN.

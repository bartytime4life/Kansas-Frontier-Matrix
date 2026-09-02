# Habitat ecoregions fixtures

`fixtures/domains/habitat/ecoregions/`

Status: draft / fixture lane / ecoregion and regionalization examples.

This directory is for small synthetic, public-safe Habitat ecoregion fixture examples used by bounded semantic-contract reviews, future schema checks, hierarchy checks, renderer checks, governed API examples, Evidence Drawer examples, Focus Mode examples, source-role checks, context-join checks, pipeline dry-runs, and documentation dry-runs. These fixtures may represent toy `EcoregionFramework`, `EcoregionSnapshot`, `EcoregionLevel`, `EcoregionContextJoin`, `EcoregionBoundaryVersion`, public-safe layer, or non-answer cases, but they are not real ecoregion records, source truth, lifecycle data, public tiles, release proof, species truth, plant truth, or publication state.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, source descriptors, proof packs, policy decisions, review approvals, release state, public API material, public map material, public tiles, or published artifacts.

## Doctrine posture

Habitat ecoregion doctrine treats ecoregion polygons as regionalization context: they classify places by a named framework and source version, but they do not prove species presence, plant presence, habitat-patch quality, regulatory designation, or other domain truth.

The Habitat ecoregions contracts README defines ecoregions as semantic-contract material for framework identity, source version, hierarchy level, context-join rules, evidence posture, public-safe geometry, correction, and rollback. It explicitly keeps contracts separate from executable pipelines, schemas, policy, fixtures, tests, source registries, lifecycle data, and release decisions.

The Habitat ecoregions pipeline README describes executable processing for admitted ecoregion and biophysical regionalization inputs, but also says pipeline logic does not own source descriptors, source catalog profiles, connectors, schemas, policy, lifecycle data, catalog truth, occurrence truth, regulatory truth, or release decisions. This fixture lane is not executable pipeline logic; it supplies toy inputs, expected shapes, and dry-run examples.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic fixture examples and runtime/checking inputs, not governed lifecycle data. It is not a `data/`, `policy/`, `schemas/`, `contracts/`, `pipelines/`, `pipeline_specs/`, `connectors/`, `release/`, proof, source-registry, catalog, triplet, tile, or publication root.

The root fixture README states that `fixtures/` is for operational rendering inputs, not validator-only test data. It also states that RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here. The parent Habitat fixture README is still a greenfield stub during this update, so this README keeps its own boundaries explicit.

## Relationship to adjacent lanes

Use this lane for ecoregion and regionalization examples where framework/version/hierarchy/context-join semantics are the main purpose.

| Adjacent lane | Relationship |
|---|---|
| `../../../contracts/domains/habitat/ecoregions/` | Defines semantic meaning; this lane supplies synthetic examples only. |
| `../../../schemas/contracts/v1/domains/habitat/ecoregions/` | Expected machine-shape home; fixture success does not prove schema authority. |
| `../../../pipelines/domains/habitat/ecoregions/` | Executable processing home; this lane is only fixture support. |
| `../../../pipeline_specs/habitat/ecoregions/` | Declarative run/spec home; this lane is not a pipeline spec. |
| `../../../policy/domains/habitat/` and `../../../policy/sensitivity/habitat/` | Policy homes; fixtures do not decide allow/deny/restrict behavior. |
| `../../../data/registry/sources/habitat/` | Source descriptor home; fixtures do not create source authority. |
| `../../../release/manifests/habitat/` | Release home; fixtures do not approve publication. |

## Related references

- `../README.md`
- `../../README.md`
- `../../../docs/domains/habitat/sublanes/ecoregions.md`
- `../../../docs/domains/habitat/SOURCE_FAMILIES.md`
- `../../../docs/domains/habitat/API_CONTRACTS.md`
- `../../../contracts/domains/habitat/ecoregions/README.md`
- `../../../pipelines/domains/habitat/ecoregions/README.md`
- `../../../pipeline_specs/habitat/ecoregions/README.md`
- `../../../schemas/contracts/v1/domains/habitat/ecoregions/`
- `../../../policy/domains/habitat/`
- `../../../policy/sensitivity/habitat/`
- `../../../data/registry/sources/habitat/`
- `../../../release/manifests/habitat/`
- `../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.invalid.json`, `*.expected.json`, `*.json`, `*.geojson`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy ecoregion framework, level, snapshot, hierarchy, boundary-version, source-version, CRS, and public-safe geometry examples;
- toy ecoregion context-join examples that preserve Habitat, Fauna, Flora, Hydrology, Soil, Hazards, Agriculture, Spatial Foundation, and People/Land authority boundaries;
- toy source-role, source-vintage, rights-state, evidence-state, sensitivity-state, review-state, release-state, correction-state, and rollback-state examples;
- toy renderer, Evidence Drawer, Focus Mode, governed API, policy, hierarchy, topology, context-join, and pipeline dry-run examples;
- paired expected outputs when behavior becomes stable enough to anchor a regression check.

## Exclusions

Do not use this lane for real ecoregion source records, live upstream fetch results, credentials, lifecycle data, registry authority, source truth, evidence authority, release artifacts, proof packs, policy rules, connector code, pipeline implementation code, public API payloads, public map data, public tiles, species occurrence data, plant occurrence data, habitat patch quality claims, regulatory designation truth, hydrology truth, soil truth, hazards truth, land/title truth, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, and reviewable.
- Use toy framework IDs, toy source IDs, toy level codes, toy region codes, toy feature IDs, toy evidence references, toy timestamps, toy hashes, and toy geometries unless a bounded check explicitly requires a more realistic shape.
- Make regionalization posture explicit: framework, level, snapshot, source version, hierarchy relation, boundary version, context join, candidate, invalid, generalized derivative, or expected output.
- Keep source role, evidence state, source vintage, rights state, sensitivity state, hierarchy state, geometry lineage, topology state, policy state, review state, release state, correction state, rollback state, and expected outcome explicit where material.
- Prefer public-safe generalized geometry. Do not include geometry that could reasonably be mistaken for sensitive real-world data.
- Pair each input with an expected output when practical.
- Treat `schema-valid`, `semantic-valid`, `source-role-valid`, `framework-resolved`, `hierarchy-valid`, `evidence-resolved`, `rights-cleared`, `policy-admissible`, `topology-valid`, `generalization-recorded`, `citation-safe`, `release-safe`, `renderer-safe`, and `join-safe` as separate checks.
- Do not treat ecoregion fixtures as occurrence evidence, habitat quality proof, regulatory proof, source authority, evidence authority, schema authority, implementation proof, approval, release state, public-map authority, tile authority, or published output.

## Expected ecoregion fixture examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Synthetic public-safe ecoregion snapshot with toy framework/version support | Valid input or `ANSWER` output | Demonstrates regionalization context without becoming occurrence truth. |
| Ecoregion feature missing framework or level | Validation failure or `ERROR` | Framework and hierarchy must be explicit. |
| Ecoregion context used as species or plant occurrence proof | `ABSTAIN` or validation failure | Occurrence truth belongs to Fauna or Flora. |
| Ecoregion context used as habitat patch quality proof | `ABSTAIN` | Ecoregions are context, not patch-quality truth. |
| Cross-lane join without EvidenceBundle support | `ABSTAIN` | EvidenceBundle support is required before claims travel. |
| Public layer derivative without release/generalization posture | Validation failure or review-required output | Public-safe derivative state remains explicit. |
| Renderer example with malformed hierarchy or geometry | Validation failure or bounded error | Renderer safety remains separate from semantic validity. |

## Maintenance notes

- Update this README when payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each fixture to the semantic-contract review, future schema check, hierarchy check, topology check, renderer check, governed-API test, Evidence Drawer test, Focus Mode test, source-role check, context-join check, policy check, pipeline dry-run, or documentation example that consumes it.
- If a fixture becomes stable enough to anchor a regression check, pair it with an expected output and document the consumer.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real source material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: populated from empty placeholder content.
- Parent habitat fixture README: present but still a greenfield stub during this update.
- Fixture payload inventory: no payload files verified in this directory during this update.
- Habitat ecoregion doctrine alignment: PARTIALLY VERIFIED against `docs/domains/habitat/sublanes/ecoregions.md`.
- Habitat ecoregion contract alignment: PARTIALLY VERIFIED against `contracts/domains/habitat/ecoregions/README.md`.
- Habitat ecoregion pipeline alignment: PARTIALLY VERIFIED against `pipelines/domains/habitat/ecoregions/README.md`.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, hierarchy checks, topology checks, renderer checks, governed-API tests, Evidence Drawer tests, Focus Mode tests, source-role checks, context-join checks, schema checks, and policy checks.
- Tests and validators: NOT RUN.

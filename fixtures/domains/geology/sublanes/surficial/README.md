# Geology surficial sublane fixtures

`fixtures/domains/geology/sublanes/surficial/`

Status: draft / fixture lane / Surficial sublane examples.

This directory is for small synthetic Geology surficial-sublane fixture examples used by bounded semantic-contract reviews, future schema checks, renderer checks, governed API examples, Evidence Drawer examples, Focus Mode examples, public-safe layer examples, pipeline dry-runs, and documentation dry-runs. These fixtures may represent toy `SurficialUnit`, `GeologyBoundaryVersion`, lithology-reference, parent-material context, hydrostratigraphic-context, public-safe map-unit, or non-answer cases, but they are not real geology records, source truth, lifecycle data, release proof, public tiles, or publication state.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, source descriptors, proof packs, review approvals, release state, public API material, public map material, public tiles, or published artifacts.

## Doctrine posture

The Surficial sublane doctrine describes the surficial facet of the Geology domain as covering Quaternary and unconsolidated map units, evidence, lifecycle, cross-lane relations, and public-safe release posture. It states that surficial geology does not own bedrock truth, soil mapunit truth, hydrology measurements, hazards risk, archaeology, land ownership, title, or UI/AI statements.

The same doctrine marks `fixtures/domains/geology/sublanes/surficial/` as a proposed co-lane companion path if the `sublanes/` convention is accepted. This README documents the fixture lane without claiming that the convention is fully resolved by ADR.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic fixture examples, not governed lifecycle data. It is not a `data/`, `policy/`, `schemas/`, `contracts/`, `pipelines/`, `pipeline_specs/`, `connectors/`, `release/`, proof, source-registry, catalog, triplet, tile, or publication root.

The root fixture README states that fixtures are operational/runtime examples, not canonical truth, and that RAW, WORK, or QUARANTINE data does not belong here. The parent Geology fixture README is still a greenfield stub during this update, so this README keeps its own boundaries explicit.

## Relationship to sibling lanes

Use this lane for synthetic SurficialUnit and surficial-context examples. Cross-cutting expected outputs and UI-specific examples should remain in the appropriate sibling fixture lanes when possible.

| Sibling lane | Relationship |
|---|---|
| `../../golden/` | Stable expected outputs for surficial examples may be paired there. |
| `../../invalid/` | Negative-path surficial inputs may move there when the failure posture is the main purpose. |
| `../../map-ui/` | Map/UI envelope examples may reference public-safe surficial layer examples. |
| `../../source_role/` | Source-role examples may be referenced when surficial source roles are being tested. |
| `../../cross_sections/` | Cross-section examples may reference surficial units as context, without replacing CrossSection authority. |

Future lanes may add bedrock, boreholes, well logs, stratigraphy, geophysics, resources, or runtime-envelope fixtures. Surficial examples should link to those lanes rather than duplicating their authority.

## Related references

- `../../README.md`
- `../../../README.md`
- `../../golden/README.md`
- `../../invalid/README.md`
- `../../map-ui/README.md`
- `../../source_role/README.md`
- `../../cross_sections/README.md`
- `../../../../../docs/domains/geology/sublanes/surficial.md`
- `../../../../../docs/domains/geology/FILE_SYSTEM_PLAN.md`
- `../../../../../docs/domains/geology/MAP_UI_CONTRACTS.md`
- `../../../../../docs/domains/geology/API_CONTRACTS.md`
- `../../../../../docs/domains/geology/SOURCE_REGISTRY.md`
- `../../../../../contracts/domains/geology/`
- `../../../../../schemas/contracts/v1/domains/geology/`
- `../../../../../data/registry/sources/geology/`
- `../../../../../policy/domains/geology/`
- `../../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.expected.json`, `*.json`, `*.geojson`, `*.jsonl`, `*.yaml`, `*.yml`, or `*.md` examples;
- toy `SurficialUnit` examples for positive-path and negative-path checks;
- toy `GeologyBoundaryVersion` examples scoped to surficial polygons;
- toy lithology-reference and parent-material-context examples;
- toy generalized polygon or boundary examples for renderer and public-safe layer checks;
- toy source-role, source-vintage, rights-state, evidence-state, review-state, release-state, correction-state, and rollback-state examples;
- examples that prove surficial polygons do not become soil mapunits, hydrology measurements, hazards risk, archaeology locations, ownership claims, or public-release approval;
- paired expected outputs in `../../golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for real geology records, real source exports, live upstream fetch results, lifecycle data, real EvidenceBundles, proof packs, run receipts, release manifests, correction notices, review records, implementation code, public API material, public map material, public tiles, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, and reviewable.
- Use toy unit IDs, toy source IDs, toy map names, toy lithology labels, toy boundary-version IDs, toy evidence references, toy timestamps, toy hashes, and toy geometries unless a bounded check explicitly requires a more realistic shape.
- Make surficial posture explicit: mapped unit, boundary version, generalized derivative, terrain-derived context, parent-material context, hydrostratigraphic context, candidate, invalid, or synthetic example.
- Keep source role, evidence state, source vintage, rights state, generalization state, topology state, policy state, review state, release state, correction state, and expected outcome explicit where material.
- Prefer public-safe generalized geometry. Do not include geometry that could reasonably be mistaken for sensitive real-world data.
- Pair each input with an expected output when practical.
- Treat `schema-valid`, `semantic-valid`, `source-role-valid`, `evidence-resolved`, `topology-valid`, `generalization-recorded`, `policy-admissible`, `citation-safe`, `release-safe`, and `renderer-safe` as separate checks.
- Do not treat surficial fixtures as source authority, evidence, release state, schema authority, implementation proof, public-map authority, tile authority, or published output.

## Expected surficial fixture examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Synthetic public-safe SurficialUnit polygon with toy source support | Valid input or `ANSWER` output | Demonstrates positive path without becoming source truth. |
| Boundary version without source vintage | Validation failure or `ERROR` | Source vintage remains part of identity/release posture. |
| Terrain-derived class presented as observed map truth | `ABSTAIN` or validation failure | Modeled/context material does not become observed authority. |
| Surficial polygon used as soil mapunit truth | `ABSTAIN` | Soil owns mapunit and horizon truth. |
| Surficial context used as hydrology measurement | `ABSTAIN` | Hydrology owns measurement truth. |
| Public layer derivative without generalization record | Validation failure or review-required output | Public-safe derivative state remains explicit. |
| Cross-lane join without EvidenceBundle support | `ABSTAIN` | EvidenceBundle support is required before claims travel. |

## Maintenance notes

- Update this README when payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each fixture to the semantic-contract review, future schema check, renderer check, governed-API test, Evidence Drawer test, Focus Mode test, source-role check, topology check, pipeline dry-run, policy check, or documentation example that consumes it.
- If a fixture becomes stable enough to anchor a regression check, pair it with an expected output and document the consumer.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real source material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: populated from empty placeholder content.
- Parent geology fixture README: present but still a greenfield stub during this update.
- Fixture payload inventory: no payloads verified in this directory during this update.
- Surficial doctrine alignment: PARTIALLY VERIFIED against `docs/domains/geology/sublanes/surficial.md`.
- Sublane path convention: NEEDS VERIFICATION / ADR-sensitive because the surficial doctrine marks `sublanes/` as PROPOSED.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Sibling fixture alignment: PARTIALLY VERIFIED against populated `golden/`, `invalid/`, `map-ui/`, `source_role/`, and `cross_sections/` READMEs.
- Consumer alignment: NEEDS VERIFICATION against validators, renderer checks, topology checks, governed-API tests, Evidence Drawer tests, Focus Mode tests, pipeline dry-runs, source-role checks, schema checks, and policy checks.
- Tests and validators: NOT RUN.

# Geology sublane fixtures

`fixtures/domains/geology/sublanes/`

Status: draft / fixture coordination lane / ADR-sensitive sublane convention.

This directory coordinates small synthetic Geology sublane fixture examples. Child lanes may hold toy examples for sublane-specific semantic-contract reviews, future schema checks, renderer checks, governed API examples, Evidence Drawer examples, Focus Mode examples, public-safe layer examples, source-role checks, pipeline dry-runs, and documentation dry-runs.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, source descriptors, proof packs, review approvals, release state, public API material, public map material, public tiles, or published artifacts.

## Convention posture

The Geology surficial doctrine says that the `sublanes/` path segment is a `PROPOSED` convention and remains `NEEDS VERIFICATION` / ADR-sensitive. It also says that the sublane breakdown of Geology is confirmed as an organizational pattern for keeping Geology objects distinct, while the exact directory convention remains open.

This README therefore treats `fixtures/domains/geology/sublanes/` as a coordination lane for already-created fixture child lanes, not as proof that every Geology sublane has a settled canonical fixture directory.

## Child lanes

| Child lane | Purpose | Current README posture |
|---|---|---|
| `surficial/` | Synthetic SurficialUnit, GeologyBoundaryVersion, lithology-reference, parent-material context, hydrostratigraphic-context, public-safe map-unit, and non-answer examples. | Present README populated. |

Future child lanes may be added for bedrock, stratigraphy, structures, lithology, boreholes, well logs, geophysics, geochemistry, resources, extraction, reclamation, hydrostratigraphy, or other Geology sublane fixture families only when they remain synthetic and fixture-scoped.

## Placement basis

This lane belongs under `fixtures/` because it coordinates synthetic fixture examples, not governed lifecycle data. It is not a `data/`, `policy/`, `schemas/`, `contracts/`, `pipelines/`, `pipeline_specs/`, `connectors/`, `release/`, proof, source-registry, catalog, triplet, tile, or publication root.

The root fixture README states that fixtures are operational/runtime examples, not canonical truth, and that RAW, WORK, or QUARANTINE data does not belong here. The parent Geology fixture README is still a greenfield stub during this update, so this README keeps its own boundaries explicit.

## Relationship to sibling lanes

Use this lane for sublane-specific fixture groups. Cross-cutting Geology fixtures should remain in sibling lanes when possible.

| Sibling lane | Relationship |
|---|---|
| `../golden/` | Stable expected outputs for sublane fixtures may be paired there. |
| `../invalid/` | Negative-path sublane inputs may move there when the failure posture is the main purpose. |
| `../map-ui/` | Map/UI envelope examples may reference sublane fixture inputs. |
| `../source_role/` | Source-role examples may be referenced when sublane source roles are being tested. |
| `../cross_sections/` | Cross-section examples may reference sublane inputs without replacing CrossSection authority. |

## Related references

- `../README.md`
- `../../README.md`
- `surficial/README.md`
- `../golden/README.md`
- `../invalid/README.md`
- `../map-ui/README.md`
- `../source_role/README.md`
- `../cross_sections/README.md`
- `../../../../docs/domains/geology/sublanes/surficial.md`
- `../../../../docs/domains/geology/FILE_SYSTEM_PLAN.md`
- `../../../../docs/domains/geology/MAP_UI_CONTRACTS.md`
- `../../../../docs/domains/geology/API_CONTRACTS.md`
- `../../../../docs/domains/geology/SOURCE_REGISTRY.md`
- `../../../../contracts/domains/geology/`
- `../../../../schemas/contracts/v1/domains/geology/`
- `../../../../data/registry/sources/geology/`
- `../../../../policy/domains/geology/`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- child directories with README files and small synthetic fixture payloads;
- small synthetic `*.input.json`, `*.expected.json`, `*.json`, `*.geojson`, `*.jsonl`, `*.yaml`, `*.yml`, or `*.md` examples when a fixture genuinely spans sublanes;
- toy sublane-specific examples for positive-path, negative-path, renderer, governed API, Evidence Drawer, Focus Mode, source-role, topology, policy, and pipeline dry-run checks;
- toy boundary-version, map-unit, lithology, structure, stratigraphy, borehole, geophysics, geochemistry, resource, extraction, reclamation, or hydrostratigraphic context examples when placed in an appropriate child lane;
- examples that prove sublane context does not silently become another domain's truth, public-release approval, source authority, or published output;
- paired expected outputs in `../golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for real geology records, real source exports, live upstream fetch results, lifecycle data, real EvidenceBundles, proof packs, run receipts, release manifests, correction notices, review records, implementation code, public API material, public map material, public tiles, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, and reviewable.
- Prefer named child lanes over loose files at this parent.
- Use toy identifiers, toy source IDs, toy map names, toy object-family names, toy evidence references, toy timestamps, toy hashes, and toy geometries unless a bounded check explicitly requires a more realistic shape.
- Make the sublane posture explicit: surficial, bedrock, stratigraphy, structures, lithology, boreholes, well logs, geophysics, geochemistry, resources, extraction, reclamation, hydrostratigraphy, or other documented facet.
- Keep source role, evidence state, source vintage, rights state, topology state, policy state, review state, release state, correction state, and expected outcome explicit where material.
- Prefer public-safe generalized geometry. Do not include geometry that could reasonably be mistaken for sensitive real-world data.
- Pair each input with an expected output when practical.
- Treat `schema-valid`, `semantic-valid`, `source-role-valid`, `evidence-resolved`, `topology-valid`, `policy-admissible`, `citation-safe`, `release-safe`, and `renderer-safe` as separate checks.
- Do not treat sublane fixtures as source authority, evidence, release state, schema authority, implementation proof, public-map authority, tile authority, or published output.

## Expected sublane fixture examples

| Scenario | Preferred lane | Expected posture | Notes |
|---|---|---|---|
| Synthetic public-safe surficial unit example | `surficial/` | Valid input or `ANSWER` output | Demonstrates positive path without becoming source truth. |
| Sublane context used as another domain's truth | child lane or `../invalid/` | `ABSTAIN` | Adjacent-domain authority remains separate. |
| Source role mismatch inside a sublane example | child lane plus `../source_role/` | `ABSTAIN` or validation failure | Source-role anti-collapse remains visible. |
| Public derivative without release/generalization posture | child lane or `../invalid/` | Validation failure or review-required output | Public-safe derivative state remains explicit. |
| Stable expected output for a sublane input | `../golden/` | Expected output | Golden output remains fixture-only, not release state. |

## Maintenance notes

- Update this README when child lanes, payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Keep child READMEs aligned with root fixture rules and Geology doctrine.
- Link each fixture to the semantic-contract review, future schema check, renderer check, governed-API test, Evidence Drawer test, Focus Mode test, source-role check, topology check, pipeline dry-run, policy check, or documentation example that consumes it.
- If a fixture becomes stable enough to anchor a regression check, pair it with an expected output and document the consumer.
- If the `sublanes/` convention is later rejected or relocated by ADR, update this README and child references through a reversible migration.
- If a fixture accidentally includes real source material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: populated from empty placeholder content.
- Child lane inventory: `surficial/README.md` verified as present during this update; no other child sublane README was verified as present.
- Fixture payload inventory: no payloads verified in this directory during this update.
- Sublane convention alignment: PARTIALLY VERIFIED against `docs/domains/geology/sublanes/surficial.md`, but still ADR-sensitive / NEEDS VERIFICATION.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Parent geology fixture README: present but still a greenfield stub during this update.
- Sibling fixture alignment: PARTIALLY VERIFIED against populated `golden/`, `invalid/`, `map-ui/`, `source_role/`, and `cross_sections/` READMEs.
- Consumer alignment: NEEDS VERIFICATION against validators, renderer checks, topology checks, governed-API tests, Evidence Drawer tests, Focus Mode tests, pipeline dry-runs, source-role checks, schema checks, and policy checks.
- Tests and validators: NOT RUN.

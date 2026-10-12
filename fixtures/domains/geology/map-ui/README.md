# Geology map/UI fixtures

`fixtures/domains/geology/map-ui/`

Status: draft / fixture lane / map and UI envelope examples.

This directory is for small synthetic Geology map/UI fixture examples used by MapLibre/Cesium renderer checks, governed API examples, Evidence Drawer examples, Focus Mode examples, timeline examples, cross-section display examples, policy-envelope examples, and documentation dry-runs. These fixtures may represent toy `MapContextEnvelope`, `LayerManifest`, `StyleManifest`, `TileArtifactManifest`, `EvidenceDrawerPayload`, `RuntimeResponseEnvelope`, or public-safe view-state examples, but they are not real map layers, real tiles, real evidence, or release artifacts.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, source descriptors, policy decisions, review approvals, release state, public API material, public map material, public tiles, or published artifacts.

## Contract posture

The Geology map/UI contract document identifies `fixtures/domains/geology/map-ui/` as the proposed fixture home for Geology map and UI examples. It also states that the renderer is not truth: map renderers are downstream of the trust membrane and render released artifacts and view state; they do not substitute for EvidenceBundle resolution.

The same document separates cross-cutting map/UI contract families from Geology-specific profiles. Geology may fill or profile objects such as `MapContextEnvelope`, `EvidenceDrawerPayload`, layer/style/tile manifests, and Focus Mode response envelopes, but it does not redefine those cross-cutting contract families inside the Geology lane.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic fixture examples, not governed lifecycle data. It is not a `data/`, `policy/`, `schemas/`, `contracts/`, `pipelines/`, `pipeline_specs/`, `connectors/`, `release/`, proof, source-registry, catalog, triplet, tile, or publication root.

The root fixture README states that fixtures are operational/runtime examples, not canonical truth, and that RAW, WORK, or QUARANTINE data does not belong here. The Geology missing/planned-files register identifies `map-ui/*` as map/UI envelope fixtures per `MAP_UI_CONTRACTS.md`. This README inherits those boundaries.

## Relationship to sibling lanes

Use this lane for synthetic map/UI envelopes and public-safe view-state examples. Object-family inputs and expected outputs should remain in the appropriate sibling fixture lanes when possible.

| Sibling lane | Relationship |
|---|---|
| `../golden/` | Stable expected outputs for map/UI examples may be paired there. |
| `../invalid/` | Negative-path map/UI inputs may move there when their failure posture is the main purpose. |
| `../cross_sections/` | Cross-section display examples may reference synthetic cross-section inputs from that lane. |

Future lanes may add valid, source, borehole, well-log, stratigraphy, unit, geophysics, or runtime-envelope fixtures. Map/UI examples should link to those lanes rather than duplicating their authority.

## Related references

- `../README.md`
- `../../README.md`
- `../golden/README.md`
- `../invalid/README.md`
- `../cross_sections/README.md`
- `../../../../docs/domains/geology/MAP_UI_CONTRACTS.md`
- `../../../../docs/domains/geology/MISSING_OR_PLANNED_FILES.md`
- `../../../../docs/domains/geology/FILE_SYSTEM_PLAN.md`
- `../../../../docs/domains/geology/API_CONTRACTS.md`
- `../../../../contracts/domains/geology/domain_layer_descriptor.md`
- `../../../../contracts/domains/geology/`
- `../../../../schemas/contracts/v1/domains/geology/`
- `../../../../schemas/contracts/v1/map/`
- `../../../../schemas/contracts/v1/ui/`
- `../../../../policy/domains/geology/`
- `../../../../policy/sensitivity/geology/`
- `../../../../data/registry/sources/geology/`
- `../../../../release/manifests/geology/`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.expected.json`, `*.json`, `*.geojson`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy `MapContextEnvelope` examples for camera, time, visible-layer, selection, and policy-state checks;
- toy `EvidenceDrawerPayload` examples for clicked Geology features;
- toy Focus Mode response-envelope examples with finite outcomes;
- toy layer/style/tile manifest fragments for renderer dry-runs;
- toy public-safe cross-section, unit, borehole, stratigraphy, or source-selection display examples;
- examples that keep view state, evidence state, policy state, release state, source state, renderer state, and expected outcome separate;
- paired expected outputs in `../golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for real geology records, real source exports, live upstream fetch results, lifecycle data, real EvidenceBundles, proof packs, run receipts, release manifests, correction notices, review records, implementation code, public API material, public map material, public tiles, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, and reviewable.
- Use toy feature references, toy layer IDs, toy camera bounds, toy time states, toy source labels, toy evidence references, and toy geometries unless a bounded check explicitly requires a more realistic shape.
- Make the UI state explicit: visible layers, selected feature, time state, policy state, evidence state, and expected finite outcome.
- Pair each input with an expected output when practical.
- Keep map/UI fixtures downstream of governed evidence and release posture.
- Treat `schema-valid`, `semantic-valid`, `evidence-resolved`, `policy-admissible`, `citation-safe`, `release-safe`, `renderer-safe`, and `ui-safe` as separate checks.
- Do not treat map/UI fixtures as evidence, approval, release state, source authority, schema authority, implementation proof, public-map authority, tile authority, or published output.

## Expected map/UI fixture examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Public-safe `MapContextEnvelope` with released toy layer IDs | Valid UI input | Demonstrates view-state handling without becoming a public API record. |
| Clicked toy feature with resolvable synthetic support | Evidence Drawer `ANSWER` output | Pair expected output in `../golden/` when stable. |
| Focus Mode request with no released evidence | `ABSTAIN` | Cite-or-abstain remains visible. |
| View request for restricted detail | `DENY` or generalized alternative | Public surface remains bounded. |
| Renderer example with malformed geometry | Validation failure or bounded error | Renderer safety remains separate from semantic validity. |
| Cross-section display example | Valid display fixture or bounded non-answer | Link to `../cross_sections/` input when practical. |

## Maintenance notes

- Update this README when payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each fixture to the renderer check, governed-API test, Evidence Drawer test, Focus Mode test, map/UI contract review, policy check, or documentation example that consumes it.
- If a fixture becomes stable enough to anchor a regression check, pair it with an expected output and document the consumer.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: populated from empty placeholder content.
- Parent geology fixture README: present but still a greenfield stub during this update.
- Fixture payload inventory: no payloads verified in this directory during this update.
- Map/UI contract alignment: PARTIALLY VERIFIED against `docs/domains/geology/MAP_UI_CONTRACTS.md`.
- Geology fixture-home alignment: PARTIALLY VERIFIED against the Geology missing/planned-files register.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Sibling fixture alignment: PARTIALLY VERIFIED against `golden/`, `invalid/`, and `cross_sections/` READMEs.
- Consumer alignment: NEEDS VERIFICATION against renderer checks, governed-API tests, Evidence Drawer tests, Focus Mode tests, schema checks, map/UI contract tests, and policy checks.
- Tests and validators: NOT RUN.

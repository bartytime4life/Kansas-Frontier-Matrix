# Geology fixtures

`fixtures/domains/geology/`

Status: draft / fixture root / Geology-domain runtime and contract support.

This directory coordinates small synthetic, public-safe Geology fixture examples used by bounded semantic-contract reviews, future schema checks, topology checks, renderer checks, governed API examples, Evidence Drawer examples, Focus Mode examples, source-role checks, sensitivity/tier-transition checks, pipeline dry-runs, no-network validation slices, and documentation dry-runs. It is a fixture root, not a governed data lifecycle root and not a publication surface.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, source descriptors, proof packs, policy decisions, review approvals, release state, public API material, public map material, public tiles, or published artifacts.

## Placement basis

This lane belongs under `fixtures/` because it coordinates synthetic fixture examples and runtime/checking inputs. It is not a `data/`, `policy/`, `schemas/`, `contracts/`, `pipelines/`, `pipeline_specs/`, `connectors/`, `release/`, proof, source-registry, catalog, triplet, tile, or publication root.

The root fixture README states that `fixtures/` is for operational rendering inputs, not validator-only test data. It also states that RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here. The Geology file-system plan identifies `fixtures/domains/geology/` as the Geology home for golden, valid, and invalid samples. This README inherits those boundaries.

## Child lanes

| Lane | Purpose | README posture |
|---|---|---|
| `valid/` | Positive-path synthetic Geology inputs. | Populated. |
| `golden/` | Stable expected-output fixtures for known synthetic inputs. | Populated. |
| `invalid/` | Negative-path synthetic inputs expected to fail, abstain, deny, or require review. | Populated. |
| `units/` | Synthetic `GeologicUnit` and map-unit examples. | Populated. |
| `cross_sections/` | Synthetic `CrossSection` semantic and pipeline dry-run examples. | Populated. |
| `map-ui/` | Synthetic map/UI envelope, renderer, Evidence Drawer, Focus Mode, and view-state examples. | Populated. |
| `source_role/` | Synthetic source-role anti-collapse and source-admission examples. | Populated. |
| `tier-transitions/` | Synthetic sensitivity, redaction, generalization, review, release-tier, correction, and withdrawal examples. | Populated. |
| `sublanes/` | ADR-sensitive parent lane for sublane-specific fixture families. | Populated. |
| `sublanes/surficial/` | Synthetic SurficialUnit, boundary-version, lithology-reference, parent-material context, and public-safe map-unit examples. | Populated; sublane path remains ADR-sensitive. |

Future child lanes may be added for other Geology object families only when they remain synthetic, public-safe, and fixture-scoped.

## Related references

- `../../README.md`
- `valid/README.md`
- `golden/README.md`
- `invalid/README.md`
- `units/README.md`
- `cross_sections/README.md`
- `map-ui/README.md`
- `source_role/README.md`
- `tier-transitions/README.md`
- `sublanes/README.md`
- `sublanes/surficial/README.md`
- `../../../docs/runbooks/geology/NO_NETWORK_TEST_RUNBOOK.md`
- `../../../docs/domains/geology/FILE_SYSTEM_PLAN.md`
- `../../../docs/domains/geology/ARCHITECTURE.md`
- `../../../docs/domains/geology/OBJECT_FAMILIES.md`
- `../../../docs/domains/geology/API_CONTRACTS.md`
- `../../../docs/domains/geology/MAP_UI_CONTRACTS.md`
- `../../../docs/domains/geology/SOURCE_REGISTRY.md`
- `../../../contracts/domains/geology/`
- `../../../schemas/contracts/v1/domains/geology/`
- `../../../policy/domains/geology/`
- `../../../data/registry/sources/geology/`
- `../../../release/manifests/geology/`
- `../../../docs/doctrine/directory-rules.md`

## Accepted material

This fixture root may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.invalid.json`, `*.expected.json`, `*.json`, `*.geojson`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- child directories grouped by fixture purpose, object family, source-role behavior, policy posture, UI/runtime behavior, sublane, or expected-output role;
- public-safe toy geometries and toy records for topology, renderer, governed API, Evidence Drawer, Focus Mode, source-admission, source-role, sensitivity, release-review, policy, pipeline, and documentation examples;
- positive-path examples in `valid/` or object-specific lanes;
- expected-output examples in `golden/`;
- negative-path examples in `invalid/` or object-specific lanes;
- object-family examples in lanes such as `units/` and `cross_sections/`;
- cross-cutting policy/runtime examples in lanes such as `map-ui/`, `source_role/`, and `tier-transitions/`.

## Exclusions

Do not use this fixture root for real geology records, real source exports, live upstream fetch results, credentials, lifecycle data, registry authority, source truth, evidence authority, release artifacts, proof packs, policy rules, connector code, pipeline implementation code, public API payloads, public map data, public tiles, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, and reviewable.
- Prefer purpose-specific or object-specific child lanes over loose files at this root.
- Use toy source IDs, toy object IDs, toy layer IDs, toy map names, toy unit symbols, toy evidence references, toy timestamps, toy hashes, and toy geometries unless a bounded check explicitly requires a more realistic shape.
- Keep source role, evidence state, rights state, sensitivity state, source vintage, interpretation version, geometry lineage, topology state, policy state, review state, release state, correction state, rollback state, and expected outcome explicit where material.
- Prefer public-safe generalized geometry.
- Pair each input with an expected output when practical.
- Treat `schema-valid`, `semantic-valid`, `source-role-valid`, `vocabulary-resolved`, `evidence-resolved`, `rights-cleared`, `policy-admissible`, `topology-valid`, `generalization-recorded`, `citation-safe`, `release-safe`, `renderer-safe`, and `ui-safe` as separate checks.
- Do not treat fixture success as evidence closure, source authority, registry authority, schema authority, implementation proof, approval, release state, public-map authority, tile authority, or published output.
- Move any real source material out of this fixture root and route it through the governed lifecycle.

## Expected fixture patterns

| Pattern | Preferred lane | Notes |
|---|---|---|
| Stable positive input | `valid/` or object-specific lane | Pair with `golden/` when practical. |
| Stable expected output | `golden/` | Expected outputs are not release artifacts. |
| Failure or non-answer input | `invalid/` | Keep the intended failure explicit. |
| Geologic unit example | `units/` | Unit fixtures do not become public layer authority. |
| Cross-section example | `cross_sections/` | Cross-section fixtures remain interpretive and evidence-bound. |
| Map/UI envelope example | `map-ui/` | UI/runtime state remains downstream of governed evidence. |
| Source-role example | `source_role/` | Source role remains fixed at admission and not upgraded by wording. |
| Sensitivity or release-tier transition | `tier-transitions/` | Transform/review/release posture remains auditable. |
| Sublane-specific example | `sublanes/<name>/` | Sublane convention is ADR-sensitive; keep child README explicit. |

## Maintenance notes

- Update this README when child lanes, payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Keep child READMEs aligned with root fixture rules and Geology doctrine.
- Link each fixture to the semantic-contract review, future schema check, topology check, renderer check, governed-API test, Evidence Drawer test, Focus Mode test, source-role check, sensitivity/tier-transition check, no-network runbook, pipeline dry-run, policy check, or documentation example that consumes it.
- If a fixture becomes stable enough to anchor a regression check, pair it with an expected output and document the consumer.
- If a fixture becomes broad enough to be a release artifact, move that concern to the governed release lane instead of expanding this fixture root.
- If a fixture accidentally includes real source material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: replaced greenfield stub content.
- Child README inventory: PARTIALLY VERIFIED against the populated child README files available during this documentation pass.
- Fixture payload inventory: no payload files verified in this directory during this update.
- Geology fixture-home alignment: PARTIALLY VERIFIED against the Geology file-system plan.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Sublane convention alignment: NEEDS VERIFICATION / ADR-sensitive where `sublanes/` is used.
- Contract/schema alignment: NEEDS VERIFICATION per child lane because several paired schemas and validators remain unconfirmed or explicitly bounded as draft/proposed.
- Consumer alignment: NEEDS VERIFICATION against validators, topology checks, renderer checks, governed-API tests, Evidence Drawer tests, Focus Mode tests, source-role checks, sensitivity/tier-transition checks, pipeline dry-runs, schema checks, and policy checks.
- Tests and validators: NOT RUN.

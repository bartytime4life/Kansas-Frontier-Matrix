# Flora fixtures

`fixtures/domains/flora/`

Status: draft / fixture root / Flora-domain runtime and contract support.

This directory coordinates small synthetic, public-safe Flora fixture examples used by bounded schema checks, semantic-contract reviews, renderer checks, governed API tests, Evidence Drawer examples, Focus Mode examples, source-admission dry-runs, watcher dry-runs, and documentation examples. It is a fixture root, not a data lifecycle root and not a publication surface.

These files are examples only. They are not authoritative project records, source records, live upstream payloads, EvidenceBundles, source descriptors, policy decisions, review approvals, release state, public API material, public map material, public tiles, or published artifacts.

## Placement basis

This lane belongs under `fixtures/` because it contains runtime/example fixture corpora. It is not a `data/`, `policy/`, `schemas/`, `contracts/`, `connectors/`, `release/`, proof, source-registry, catalog, triplet, or publication root.

The root fixture README states that `fixtures/` is for operational rendering inputs rather than validator-only test data. It also states that fixture corpora must not contain RAW, WORK, or QUARANTINE data, must not contain sensitive exact geometry, and must not be treated as canonical truth.

The Flora missing/planned-files register identifies this path as the per-root README for `fixtures/domains/flora/` and describes the lane as golden, valid, and invalid sample data backing Flora tests, with no live data and no live network.

## Child lanes

| Lane | Purpose | Current README posture |
|---|---|---|
| `golden/` | Expected-output fixtures for stable synthetic inputs. | Populated. |
| `valid/` | Positive-path synthetic inputs. | Populated. |
| `invalid/` | Intentionally rejected or bounded non-answer examples. | Populated. |
| `synthetic/` | Exploratory toy examples before a specific lane is chosen. | Populated. |
| `source_descriptors/` | Synthetic `SourceDescriptor` examples for Flora source families. | Populated. |
| `sources/` | Parent for source-family fixture lanes. | Populated. |
| `sources/plants/` | Synthetic USDA PLANTS-style source examples. | Populated. |
| `plants_drift/` | Synthetic PLANTS/source drift and watcher dry-run examples. | Populated. |
| `plant_taxon/` | Synthetic PlantTaxon and taxonomy/crosswalk examples. | Populated. |
| `flora_occurrence/` | Synthetic occurrence examples and public-safe occurrence behavior. | Populated. |
| `rare_plant_record/` | Synthetic rare-plant/public-safe derivative examples. | Populated. |
| `vegetation_community/` | Synthetic community polygon and classification examples. | Populated. |
| `invasive_plant_record/` | Synthetic invasive-plant observation examples. | Populated. |
| `phenology_observation/` | Synthetic seasonal/time-series examples. | Populated. |
| `evidence_bundles/` | Synthetic EvidenceBundle and catalog-closure examples. | Populated. |
| `decision_envelopes/` | Synthetic finite-outcome decision envelope examples. | Populated; naming remains compatibility-sensitive. |
| `runtime_envelopes/` | Runtime response envelope examples. | Planned / needs verification from backlog. |

## Related references

- `../../README.md`
- `golden/README.md`
- `valid/README.md`
- `invalid/README.md`
- `synthetic/README.md`
- `source_descriptors/README.md`
- `sources/README.md`
- `sources/plants/README.md`
- `plants_drift/README.md`
- `plant_taxon/README.md`
- `flora_occurrence/README.md`
- `rare_plant_record/README.md`
- `vegetation_community/README.md`
- `invasive_plant_record/README.md`
- `phenology_observation/README.md`
- `evidence_bundles/README.md`
- `decision_envelopes/README.md`
- `../../../../docs/domains/flora/MISSING_OR_PLANNED_FILES.md`
- `../../../../docs/domains/flora/API_CONTRACTS.md`
- `../../../../docs/domains/flora/MAP_UI_CONTRACTS.md`
- `../../../../docs/domains/flora/SENSITIVITY.md`
- `../../../../docs/domains/flora/DATA_LIFECYCLE.md`
- `../../../../docs/domains/flora/SOURCE_REGISTRY.md`
- `../../../../docs/domains/flora/CROSSWALKS.md`
- `../../../../contracts/domains/flora/`
- `../../../../schemas/contracts/v1/domains/flora/`
- `../../../../schemas/contracts/v1/source/`
- `../../../../policy/domains/flora/`
- `../../../../policy/sensitivity/flora/`
- `../../../../data/registry/sources/flora/`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This fixture root may contain:

- small synthetic `*.input.json`, `*.expected.json`, `*.json`, `*.geojson`, `*.jsonl`, `*.yaml`, `*.yml`, or `*.md` examples;
- child directories grouped by fixture purpose, object family, source family, expected-output role, or dry-run behavior;
- public-safe toy geometries and toy records for renderer, API, Evidence Drawer, Focus Mode, source-admission, policy, and documentation examples;
- positive-path examples in `valid/` or object-specific lanes;
- expected-output examples in `golden/`;
- negative-path examples in `invalid/`;
- exploratory examples in `synthetic/` before a more specific lane is chosen;
- paired expected outputs when behavior becomes stable enough to anchor a regression check.

## Exclusions

Do not use this fixture root for real source data, real upstream payloads, credentials, lifecycle data, registry authority, release artifacts, proof packs, policy rules, connector or pipeline implementation code, public API payloads, public map data, public tiles, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, and reviewable.
- Prefer object-specific or source-specific child lanes over loose files at this root.
- Use toy identifiers, toy taxa, toy sources, toy timestamps, toy hashes, toy evidence references, and toy geometries unless a bounded check explicitly requires a more realistic shape.
- Keep source role, evidence state, rights state, policy state, freshness state, review state, release state, correction state, and expected output state explicit where material.
- Pair each input with an expected output when practical.
- Treat `schema-valid`, `semantic-valid`, `evidence-resolved`, `policy-admissible`, `citation-safe`, `release-safe`, and `renderer-safe` as separate checks.
- Do not treat fixture success as evidence closure, source authority, registry authority, schema authority, implementation proof, approval, release state, or published output.
- Move any real source material out of this fixture root and route it through the governed lifecycle.

## Expected fixture patterns

| Pattern | Preferred lane | Notes |
|---|---|---|
| Stable positive input | `valid/` or object-specific lane | Pair with `golden/` when practical. |
| Stable expected output | `golden/` | Expected outputs are not release artifacts. |
| Failure or non-answer input | `invalid/` | Keep the intended failure explicit. |
| Early toy example | `synthetic/` | Move once the object family or consumer is clear. |
| Source-family example | `source_descriptors/` or `sources/` | Does not create registry authority. |
| Drift/watch example | `plants_drift/` or source child lane | Watchers do not publish. |
| Object-family example | object-specific child lane | Contract/schema posture remains bounded by current evidence. |

## Maintenance notes

- Update this README when child lanes, payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Keep child READMEs aligned with root fixture rules and Flora doctrine.
- Link each fixture to the validator, renderer check, governed-API test, Evidence Drawer test, Focus Mode test, policy check, source-admission check, watcher dry-run, or documentation example that consumes it.
- If a fixture becomes stable enough to anchor a regression check, pair it with an expected output and document the consumer.
- If a fixture becomes broad enough to be a release artifact, move that concern to the governed release lane instead of expanding this fixture root.
- If a fixture accidentally includes real source material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: replaced greenfield stub content.
- Child README inventory: PARTIALLY VERIFIED by repository search and recent child README updates; not all possible child directories were exhaustively listed as payload-bearing directories.
- Fixture payload inventory: no payload files verified in this directory during this update.
- Flora fixture backlog alignment: PARTIALLY VERIFIED against the Flora missing/planned-files register.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Contract/schema alignment: NEEDS VERIFICATION per child lane because several paired schemas remain permissive `PROPOSED` scaffolds.
- Consumer alignment: NEEDS VERIFICATION against validators, renderer checks, governed-API tests, Evidence Drawer tests, Focus Mode tests, schema checks, source-admission checks, watcher dry-runs, and policy checks.
- Tests and validators: NOT RUN.

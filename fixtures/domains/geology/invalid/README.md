# Geology invalid fixtures

`fixtures/domains/geology/invalid/`

Status: draft / fixture lane / negative-path examples.

This directory is for small synthetic Geology examples that are intentionally rejected by bounded checks or expected to produce a bounded non-answer. Invalid fixtures support review of semantic-contract behavior, future schema checks, renderer checks, governed API behavior, Evidence Drawer behavior, Focus Mode behavior, pipeline dry-runs, topology checks, and documentation examples.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, source descriptors, proof packs, review approvals, release state, public API material, public map material, public tiles, or published artifacts.

## Placement basis

This lane belongs under `fixtures/` because it contains negative-path fixture examples, not governed lifecycle data. It is not a `data/`, `policy/`, `schemas/`, `contracts/`, `pipelines/`, `pipeline_specs/`, `connectors/`, `release/`, proof, source-registry, catalog, triplet, or publication root.

The root fixture README states that fixtures are operational/runtime examples, not canonical truth, and that RAW, WORK, or QUARANTINE data does not belong here. The Geology file-system plan identifies `fixtures/domains/geology/` as the Geology fixture home for golden, valid, and invalid samples. This README inherits those boundaries.

## Relationship to sibling lanes

Use this lane for invalid or negative-path synthetic inputs. Expected outputs should usually live in `../golden/` once behavior is stable.

| Sibling lane | Relationship |
|---|---|
| `../golden/` | Stores stable expected outputs for invalid inputs. |
| `../cross_sections/` | May contain cross-section positive-path or negative-path inputs; move stable invalid examples here when a dedicated negative lane is clearer. |

Future sibling lanes may add valid, borehole, well-log, stratigraphy, bedrock, surficial, geophysics, source, or runtime-envelope inputs. Invalid examples may live here when they are cross-cutting or when the object-specific lane does not yet exist.

## Related references

- `../README.md`
- `../../README.md`
- `../golden/README.md`
- `../cross_sections/README.md`
- `../../../../docs/domains/geology/FILE_SYSTEM_PLAN.md`
- `../../../../docs/domains/geology/OBJECT_FAMILIES.md`
- `../../../../docs/domains/geology/API_CONTRACTS.md`
- `../../../../contracts/domains/geology/`
- `../../../../schemas/contracts/v1/domains/geology/`
- `../../../../pipelines/domains/geology/cross_sections/README.md`
- `../../../../pipeline_specs/geology/`
- `../../../../data/registry/sources/geology/`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.invalid.json`, `*.input.json`, `*.json`, `*.geojson`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- intentionally incomplete examples;
- intentionally mismatched examples;
- examples with missing support references;
- examples with unsupported interpretation posture;
- examples with missing source role, missing evidence state, missing freshness state, missing display metadata, or missing expected outcome;
- examples used to confirm a bounded non-answer, validation failure, topology failure, renderer failure, or review-required result;
- paired expected outputs in `../golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for real geology records, real source exports, live upstream fetch results, lifecycle data, real EvidenceBundles, proof packs, run receipts, release manifests, correction notices, review records, implementation code, public API material, public map material, public tiles, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, and reviewable.
- Make the intended failure explicit in the file name, fixture metadata, or paired expected output.
- Prefer one failure reason per fixture unless a test intentionally checks precedence.
- Pair invalid inputs with expected outputs in `../golden/` when practical.
- Keep source role, evidence state, freshness state, interpretation state, topology state, review state, release state, correction state, and expected output state explicit where material.
- Do not include real source properties, direct model-runtime output, unpublished candidate content, or geometry that could reasonably be mistaken for real field data.
- Treat `schema-valid`, `semantic-valid`, `evidence-resolved`, `interpretation-bounded`, `topology-valid`, `citation-safe`, `release-safe`, and `renderer-safe` as separate checks.
- Do not treat invalid fixtures as evidence, approval, release state, source authority, schema authority, implementation proof, or published output.

## Expected invalid fixture examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Missing required identity | Validation failure | Identity must be stable before use. |
| Missing evidence support | `ABSTAIN` | No claim is emitted without support. |
| Incomplete contract shape | Validation failure or `ERROR` | Shape failures stay bounded. |
| Unsupported inferred contact | `ABSTAIN` | Interpretation support remains visible. |
| Missing vertical datum or display metadata | Validation failure or `ERROR` | Display semantics remain explicit. |
| Source role unclear | `ABSTAIN` or review-required output | Source-role anti-collapse remains visible. |
| Renderer-unsafe geometry | Validation failure or bounded error | Renderer safety remains separate from semantic validity. |

## Maintenance notes

- Update this README when payload files, sibling valid/golden lanes, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each invalid fixture to the semantic-contract review, future schema check, pipeline dry-run, renderer check, topology check, governed-API test, Evidence Drawer test, Focus Mode test, evidence resolver, or documentation example that consumes it.
- If a fixture becomes stable enough to anchor a regression check, pair it with an expected output and document the consumer.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: populated from empty placeholder content.
- Fixture payload inventory: no payloads verified in this directory during this update.
- Sibling fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/geology/golden/README.md` and `fixtures/domains/geology/cross_sections/README.md`.
- Geology fixture-home alignment: PARTIALLY VERIFIED against the Geology file-system plan.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, renderer checks, topology checks, governed-API tests, Evidence Drawer tests, Focus Mode tests, pipeline dry-runs, schema checks, and policy checks.
- Tests and validators: NOT RUN.

# Geology golden fixtures

`fixtures/domains/geology/golden/`

Status: draft / fixture lane / expected-output examples.

This directory is for small synthetic Geology expected-output fixtures. Golden fixtures describe the expected result for a known synthetic input used by bounded checks, renderer examples, governed API examples, Focus Mode examples, Evidence Drawer examples, pipeline dry-runs, and documentation examples.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, source descriptors, proof packs, review approvals, release state, public API material, public map material, public tiles, or published artifacts.

## Placement basis

This lane belongs under `fixtures/` because it contains expected-output examples for synthetic fixtures. It is not a `data/`, `policy/`, `schemas/`, `contracts/`, `pipelines/`, `pipeline_specs/`, `connectors/`, `release/`, proof, source-registry, catalog, triplet, or publication root.

The root fixture README states that fixtures are operational/runtime examples, not canonical truth, and that RAW, WORK, or QUARANTINE data does not belong here. The Geology file-system plan identifies `fixtures/domains/geology/` as the Geology fixture home for golden, valid, and invalid samples. This README inherits those boundaries.

## Relationship to input lanes

Use this lane for expected outputs paired with synthetic Geology inputs from sibling fixture lanes.

| Input lane | Expected-output use | Status |
|---|---|---|
| `../cross_sections/` | Expected cross-section candidate, bounded non-answer, topology, renderer, or pipeline dry-run outputs. | Present README populated. |

Future sibling lanes may add valid, invalid, borehole, well-log, stratigraphy, bedrock, surficial, geophysics, source, or runtime-envelope inputs. Expected outputs may be stored here when they are stable, deterministic, and documented.

## Related references

- `../README.md`
- `../../README.md`
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

- small synthetic `*.expected.json`, `*.expected.geojson`, `*.expected.jsonl`, `*.expected.yaml`, `*.expected.yml`, `*.expected.svg`, or `*.md` expected-output examples;
- expected positive-path outputs for valid public-safe Geology fixture inputs;
- expected bounded non-answer, validation-failure, stale-source, unsupported-interpretation, topology-failure, renderer-failure, or review-required outputs for negative-path fixture inputs;
- expected cross-section, borehole, stratigraphy, unit, geophysics, source-admission, Evidence Drawer, Focus Mode, governed API, renderer, topology, or pipeline dry-run outputs;
- paired expected outputs for inputs stored in sibling fixture lanes such as `../cross_sections/` and future geology fixture lanes.

## Exclusions

Do not use this lane for real geology records, real source exports, live upstream fetch results, lifecycle data, real EvidenceBundles, proof packs, run receipts, release manifests, correction notices, review records, implementation code, public API material, public map material, public tiles, or published artifacts.

## Fixture design rules

- Keep expected outputs synthetic, compact, deterministic, and reviewable.
- Pair golden outputs with a clearly named input fixture whenever practical.
- Use naming that makes the relationship obvious, such as `<scenario>.input.json` in a sibling lane and `<scenario>.expected.json` in this lane, or an equivalent documented pair.
- Keep expected outcomes explicit, such as `ANSWER`, `ABSTAIN`, `ERROR`, `HOLD`, `SOURCE_STALE`, validation failure, renderer-safe output, topology-safe output, or another documented finite posture.
- Keep source role, evidence state, freshness state, interpretation state, review state, release state, correction state, and expected output state explicit where material.
- Do not include real source properties, direct model-runtime output, unpublished candidate content, or geometry that could reasonably be mistaken for real field data.
- Treat `schema-valid`, `semantic-valid`, `evidence-resolved`, `interpretation-bounded`, `topology-valid`, `citation-safe`, `release-safe`, and `renderer-safe` as separate checks.
- Do not treat golden fixtures as evidence, approval, release state, proof authority, source authority, schema authority, implementation proof, or published output.

## Expected golden fixture examples

| Input lane | Example expected output | Notes |
|---|---|---|
| `../cross_sections/` | Public-safe cross-section candidate output | Demonstrates positive path without becoming source truth. |
| `../cross_sections/` | Cross-section `ABSTAIN` output for unsupported inferred contact | Interpretation support remains visible. |
| `../cross_sections/` | Validation failure for missing vertical datum or vertical-exaggeration disclosure | Display semantics remain explicit. |
| Future `valid/` | Positive governed API or renderer output | Must remain synthetic and public-safe. |
| Future `invalid/` | Bounded non-answer or validation output | Failure intent must remain explicit. |
| Future source fixture lane | Source-admission or source-role expected output | Registry authority remains separate. |

## Maintenance notes

- Update this README when payload files, input fixture lanes, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each golden fixture to the input fixture and the test, renderer check, governed-API contract, Focus Mode test, Evidence Drawer test, pipeline dry-run, topology check, evidence resolver, or documentation example that consumes it.
- Keep payloads small enough for normal code review.
- If an expected output becomes broad enough to be a release artifact, move that concern to the governed release lane instead of expanding this fixture lane.
- If a fixture accidentally includes real material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: populated from empty placeholder content.
- Fixture payload inventory: no payloads verified in this directory during this update.
- Sibling input alignment: PARTIALLY VERIFIED against `fixtures/domains/geology/cross_sections/README.md`.
- Geology fixture-home alignment: PARTIALLY VERIFIED against the Geology file-system plan.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, renderer checks, topology checks, governed-API tests, Evidence Drawer tests, Focus Mode tests, pipeline dry-runs, schema checks, and policy checks.
- Tests and validators: NOT RUN.

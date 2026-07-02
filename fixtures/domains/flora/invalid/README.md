# Flora invalid fixtures

`fixtures/domains/flora/invalid/`

Status: draft / fixture lane.

This directory is for small synthetic Flora examples that are intentionally not accepted by a bounded check. It supports review of schema behavior, semantic-contract behavior, renderer behavior, governed API behavior, Evidence Drawer behavior, Focus Mode behavior, and documentation examples.

These files are examples only. They are not source records, EvidenceBundles, policy decisions, release state, public API material, public map material, public tiles, or published artifacts.

## Placement basis

This lane belongs under `fixtures/` because it contains fixture examples, not governed lifecycle data. It is not a `data/`, `policy/`, `schemas/`, `contracts/`, `release/`, or publication root.

## Related references

- `../README.md`
- `../golden/README.md`
- `../flora_occurrence/README.md`
- `../evidence_bundles/README.md`
- `../decision_envelopes/README.md`
- `../../README.md`
- `../../../../docs/domains/flora/MISSING_OR_PLANNED_FILES.md`
- `../../../../docs/domains/flora/API_CONTRACTS.md`
- `../../../../contracts/domains/flora/`
- `../../../../schemas/contracts/v1/domains/flora/`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.json`, `*.geojson`, `*.jsonl`, or `*.md` examples;
- intentionally incomplete examples;
- intentionally mismatched examples;
- examples with missing support references;
- examples used to confirm a bounded non-answer or validation result;
- paired expected outputs when the stable expectation belongs in `../golden/`.

## Exclusions

Do not use this lane for real source data, lifecycle data, release artifacts, proof packs, implementation code, public map data, public API payloads, public tiles, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, and reviewable.
- Make the intended failure explicit in the file name, fixture metadata, or paired expected output.
- Prefer one failure reason per fixture unless a test intentionally checks precedence.
- Pair invalid inputs with expected outputs in `../golden/` when practical.
- Do not treat invalid fixtures as evidence, approval, release state, source authority, schema authority, implementation proof, or published output.

## Expected invalid fixture examples

| Scenario | Expected posture |
|---|---|
| Missing required identity | Validation failure |
| Missing evidence support | Non-answer outcome |
| Incomplete contract shape | Validation failure |
| Mismatched source role | Non-answer outcome |
| Renderer-unsafe payload | Validation failure or bounded error |

## Verification status

- Target README: populated from empty placeholder content.
- Fixture payload inventory: no payloads verified in this directory during this update.
- Flora fixture backlog alignment: PARTIALLY VERIFIED against the Flora missing/planned-files register.
- Consumer alignment: NEEDS VERIFICATION against validators, renderer checks, governed-API tests, Evidence Drawer tests, Focus Mode tests, schema checks, and policy checks.
- Tests and validators: NOT RUN.

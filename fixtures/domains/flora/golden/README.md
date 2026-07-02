# Flora golden fixtures

`fixtures/domains/flora/golden/`

Status: draft / fixture lane / expected-output surface.

This directory is for small synthetic Flora expected-output fixtures used by bounded regression checks, schema checks, semantic-contract reviews, renderer checks, governed API tests, Evidence Drawer examples, Focus Mode examples, and documentation dry-runs. Golden fixtures describe the expected result for a known synthetic input; they are not real evidence, source truth, catalog truth, release proof, or publication state.

These files are examples only. They are not authoritative project records, source records, EvidenceBundles, source descriptors, proof packs, policy decisions, rights approvals, review approvals, release state, public API material, public map material, public tiles, or published artifacts.

## Placement basis

Directory rules and the root fixture README keep fixture material under the `fixtures/` responsibility root. This lane is therefore a Flora-domain expected-output fixture lane, not a data lifecycle root, not a source registry, not a catalog root, not a proof root, not a policy root, not a schema root, not a release root, and not a publication target.

The root fixture README states that `fixtures/` is for operational rendering inputs rather than validator-only test data. It also states that fixture corpora must not contain RAW, WORK, QUARANTINE data, sensitive exact geometry, or canonical truth. This README inherits those boundaries.

## Related fixture and doctrine references

- `../README.md`
- `../../README.md`
- `../flora_occurrence/README.md`
- `../evidence_bundles/README.md`
- `../decision_envelopes/README.md`
- `../../../../docs/domains/flora/MISSING_OR_PLANNED_FILES.md`
- `../../../../docs/domains/flora/API_CONTRACTS.md`
- `../../../../docs/domains/flora/EVIDENCE_DRAWER.md`
- `../../../../docs/domains/flora/MAP_UI_CONTRACTS.md`
- `../../../../docs/domains/flora/SENSITIVITY.md`
- `../../../../docs/domains/flora/DATA_LIFECYCLE.md`
- `../../../../contracts/domains/flora/`
- `../../../../schemas/contracts/v1/domains/flora/`
- `../../../../policy/domains/flora/`
- `../../../../policy/sensitivity/flora/`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.expected.json`, `*.expected.geojson`, `*.expected.jsonl`, or `*.md` expected-output examples;
- expected positive-path outputs for valid public-safe Flora fixture inputs;
- expected abstention, denial, stale-source, conflicted-support, or error outputs for negative-path fixture inputs;
- expected renderer, Evidence Drawer, Focus Mode, governed API, evidence resolver, catalog-closure, or policy-check outputs;
- paired expected outputs for inputs stored in sibling fixture lanes such as `flora_occurrence/`, `evidence_bundles/`, `decision_envelopes/`, `runtime_envelopes/`, `plant_taxon/`, and other Flora fixture lanes;
- README files explaining fixture intent and boundaries.

## Exclusions

Do not use this lane for:

- real Flora observations, taxon records, specimen records, range layers, source descriptors, or source-system exports;
- live upstream fetch results, scraped payloads, steward-only records, or real upstream response samples;
- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, PUBLISHED, receipt, proof, registry, or release-lifecycle artifacts;
- real EvidenceBundles, proof packs, run receipts, source-refresh receipts, release manifests, rollback cards, correction notices, review records, or policy decisions;
- policy rules, rights approvals, reviewer approvals, concrete transform parameters, or operational freshness thresholds;
- sensitive exact geometry, reconstructive clues, or geometry that could reasonably be mistaken for a real sensitive observation;
- connector, pipeline, validator, package, schema, policy, release, or app implementation code;
- public API material, public map material, public tiles, published artifacts, or canonical layer registry entries.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, and reviewable.
- Pair golden outputs with a clearly named input fixture whenever practical.
- Use naming that makes the relationship obvious, such as `<scenario>.input.json` beside `<scenario>.expected.json` or an equivalent documented pair.
- Keep expected outcomes explicit: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, `HOLD`, `SOURCE_STALE`, `CONFLICTED_SUPPORT`, `RELEASE_WITHDRAWN`, validation failure, renderer-safe output, or another documented finite posture.
- Keep source role, evidence state, rights state, policy state, freshness state, review state, release state, correction state, and expected output state explicit where material.
- Do not include raw feature properties, sensitive geometry, direct model-runtime output, or unpublished candidate content in public-surface expected outputs.
- Treat `schema-valid`, `semantic-valid`, `evidence-resolved`, `policy-admissible`, `citation-safe`, `release-safe`, and `renderer-safe` as separate checks.
- Do not treat golden fixtures as evidence, approval, release state, proof authority, source authority, schema authority, implementation proof, or published output.

## Expected golden fixture examples

| Input lane | Example expected output | Notes |
|---|---|---|
| `flora_occurrence/` | Public-safe occurrence `ANSWER` output | Demonstrates positive path without becoming source truth. |
| `flora_occurrence/` | Occurrence `ABSTAIN` output for unresolved support | Cite-or-abstain remains visible. |
| `evidence_bundles/` | Catalog-closure success output | All synthetic evidence references resolve inside the fixture set. |
| `evidence_bundles/` | Missing evidence output | No claim is emitted without resolvable support. |
| `decision_envelopes/` | Finite-outcome expected envelope | Outcome and reason code are stable and bounded. |
| `runtime_envelopes/` | Focus Mode `ABSTAIN` or `DENY` output | No direct model-runtime output is stored here. |
| `plant_taxon/` | Taxon-resolution success or failure output | Taxonomy uncertainty remains explicit. |
| `rare_plant_record/` | Public-safe denial or transformed-output posture | Uses synthetic/generalized examples only. |

## Maintenance notes

- Update this README when payload files, input fixture lanes, validators, tests, helper scripts, or consumer contracts are added.
- Link each golden fixture to the input fixture and the test, renderer check, governed-API contract, Focus Mode test, evidence resolver, policy check, or documentation example that consumes it.
- Keep payloads small enough for normal code review.
- If an expected output becomes broad enough to be a release artifact, move that concern to the governed release lane instead of expanding this fixture lane.
- If a fixture accidentally includes real or sensitive material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: populated from empty placeholder content.
- Fixture payload inventory: no payloads verified in this directory during this update.
- Flora fixture backlog alignment: PARTIALLY VERIFIED against the Flora missing/planned-files register, which calls for golden, valid, and invalid sample data with no live data and no live network.
- Consumer alignment: NEEDS VERIFICATION against validators, renderer checks, governed-API tests, Evidence Drawer tests, Focus Mode tests, schema checks, and policy checks.
- Tests and validators: NOT RUN.

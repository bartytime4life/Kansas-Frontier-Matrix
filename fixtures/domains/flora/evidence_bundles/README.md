# Flora EvidenceBundle fixtures

`fixtures/domains/flora/evidence_bundles/`

Status: draft / fixture lane / planning-aligned surface.

This directory is for small synthetic Flora fixture examples that exercise EvidenceBundle-shaped support, catalog-closure checks, citation resolution, Evidence Drawer payloads, Focus Mode citation behavior, and governed API evidence-resolution seams. These examples may look like EvidenceBundles or EvidenceBundle fragments, but they are not real EvidenceBundles and must never be treated as source truth, catalog truth, proof, release evidence, or publication state.

These files are examples only. They are not authoritative project records, source records, EvidenceBundles, source descriptors, proof packs, policy decisions, rights approvals, review approvals, release state, public API material, public map material, public tiles, or published artifacts.

## Naming and alignment note

The Flora missing/planned-files register lists `fixtures/domains/flora/evidence_bundles/` as the proposed fixture lane for EvidenceBundle fixtures used by catalog closure. Repository evidence also shows a placeholder schema at `schemas/contracts/v1/domains/flora/evidence_bundle.schema.json` with status `PROPOSED` and an `x-kfm.fixtures_root` of `fixtures/domains/flora/evidence_bundle/`.

Until an ADR, schema update, or migration note reconciles the singular/plural fixture path, this README treats the requested plural path as the active planning fixture lane and records the singular schema pointer as NEEDS VERIFICATION. Do not maintain parallel fixture authorities without a migration note.

## Placement basis

Directory rules and the root fixture README keep fixture material under the `fixtures/` responsibility root. This lane is therefore a Flora-domain fixture lane for EvidenceBundle-shaped examples, not a data lifecycle root, not a catalog root, not a proof root, not a policy root, not a schema root, not a source registry, not a release root, and not a publication target.

The root fixture README also states that `fixtures/` is for operational rendering inputs rather than validator-only test data, and that fixtures must not contain RAW, WORK, QUARANTINE data, sensitive exact geometry, or canonical truth. This README inherits those boundaries.

## Related fixture and doctrine references

- `../README.md`
- `../../README.md`
- `../../../../docs/domains/flora/MISSING_OR_PLANNED_FILES.md`
- `../../../../docs/domains/flora/API_CONTRACTS.md`
- `../../../../docs/domains/flora/EVIDENCE_DRAWER.md`
- `../../../../docs/domains/flora/MAP_UI_CONTRACTS.md`
- `../../../../docs/domains/flora/SENSITIVITY.md`
- `../../../../docs/domains/flora/DATA_LIFECYCLE.md`
- `../../../../contracts/domains/flora/`
- `../../../../contracts/evidence/evidence_bundle.md`
- `../../../../schemas/contracts/v1/domains/flora/evidence_bundle.schema.json`
- `../../../../schemas/contracts/v1/domains/flora/`
- `../../../../policy/domains/flora/`
- `../../../../policy/sensitivity/flora/`
- `../../../../data/catalog/domain/flora/`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.expected.json`, `*.json`, `*.jsonl`, or `*.md` examples;
- toy EvidenceBundle-shaped fixtures for Flora catalog-closure checks;
- positive examples where every required synthetic `EvidenceRef` resolves inside the fixture set;
- negative examples where missing support, stale support, conflicted support, policy denial, or release-state gaps force bounded refusal or abstention;
- synthetic Evidence Drawer support examples that prove visible claims remain traceable;
- Focus Mode evidence examples that prove cite-or-abstain behavior without invoking live model output;
- source-role examples that keep authority, observation, aggregator, context, and model-derived support separate;
- README files explaining fixture intent and boundaries.

## Exclusions

Do not use this lane for:

- authoritative Flora observations, taxon records, specimens, range layers, source descriptors, or source-system exports;
- live upstream fetch results, scraped payloads, steward-only records, or real upstream response samples;
- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, PUBLISHED, receipt, proof, registry, or release-lifecycle artifacts;
- real EvidenceBundles, proof packs, run receipts, source-refresh receipts, release manifests, rollback cards, correction notices, review records, or policy decisions;
- policy rules, rights approvals, reviewer approvals, concrete transform parameters, or operational freshness thresholds;
- sensitive exact geometry, reconstructive clues, or geometry that could reasonably be mistaken for a real sensitive observation;
- connector, pipeline, validator, package, schema, policy, release, or app implementation code;
- public API material, public map material, public tiles, published artifacts, or canonical layer registry entries.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, and reviewable.
- Use toy identifiers, toy taxa, toy source names, toy source roles, toy timestamps, toy evidence references, and toy geometries unless a bounded check explicitly requires a more realistic shape.
- Keep evidence closure explicit: every positive-path claim should point to a synthetic evidence reference that can be resolved by the fixture consumer.
- Keep failure closure explicit: missing, stale, withdrawn, conflicted, unreleased, rights-blocked, or policy-blocked evidence should have an expected bounded outcome.
- Keep source role, evidence state, rights state, policy state, freshness state, review state, release state, correction state, and expected outcome explicit where material.
- Do not include raw feature properties, sensitive geometry, direct model-runtime output, or unpublished candidate content in public-surface examples.
- Pair each input with an expected output when practical.
- Treat `schema-valid`, `evidence-resolved`, `policy-admissible`, `citation-safe`, `release-safe`, and `renderer-safe` as separate checks.
- Do not treat EvidenceBundle fixtures as evidence, approval, release state, proof authority, source authority, schema authority, implementation proof, or published output.

## Expected EvidenceBundle fixture examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Released public-safe Flora claim with resolved synthetic evidence | `ANSWER` | Demonstrates traceable positive path with toy evidence references. |
| EvidenceRef missing from fixture set | `ABSTAIN` | No claim should be emitted without resolvable support. |
| Evidence exists but source role is inappropriate for the claim | `ABSTAIN` or `CONFLICTED_SUPPORT` | Source-role separation remains visible. |
| Evidence support is stale with no current alternative | `ABSTAIN` / `SOURCE_STALE` | Freshness state is visible and bounded. |
| Evidence support is blocked by policy or rights state | `DENY` | Include synthetic reason code; no fallback claim. |
| Evidence support is unreleased or withdrawn | `ABSTAIN` / `RELEASE_WITHDRAWN` | Public surfaces must not treat unreleased or withdrawn support as current proof. |
| Evidence Drawer payload references missing bundle support | `ABSTAIN` or error posture | Drawer must not fabricate support. |
| Focus Mode asks beyond released synthetic support | `ABSTAIN` | Cite-or-abstain remains the default. |

## Maintenance notes

- Update this README when payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each fixture to the catalog-closure test, evidence resolver test, Evidence Drawer test, Focus Mode test, governed-API test, schema check, policy check, or documentation example that consumes it.
- If the repo adopts `fixtures/domains/flora/evidence_bundle/` instead of this plural path, add a migration note and avoid maintaining parallel fixture authorities.
- If a fixture becomes stable enough to anchor a regression check, pair it with an expected output and document the consumer.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real or sensitive material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: populated from empty placeholder content.
- Fixture payload inventory: no payloads verified in this directory during this update.
- Schema naming alignment: NEEDS VERIFICATION because the repository has a PROPOSED `evidence_bundle.schema.json` pointing at singular `fixtures/domains/flora/evidence_bundle/`, while this requested path is plural.
- Catalog-closure alignment: NEEDS VERIFICATION against Flora catalog-closure tests, evidence resolver tests, Evidence Drawer tests, Focus Mode tests, and schema contracts.
- Tests and validators: NOT RUN.

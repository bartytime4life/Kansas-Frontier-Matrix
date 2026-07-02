# Flora decision-envelope fixtures

`fixtures/domains/flora/decision_envelopes/`

Status: draft / fixture lane / compatibility-planning surface.

This directory is for small synthetic Flora fixture examples that exercise finite-outcome decision-envelope behavior at governed API, Evidence Drawer, Focus Mode, review, correction, and release-gate seams. It may hold toy request/response examples for `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, and `HOLD` outcomes where Flora-specific policy, rights, evidence, freshness, review, release, or correction state changes the allowed response.

These files are examples only. They are not authoritative project records, source records, EvidenceBundles, policy decisions, review approvals, release state, public API material, public map material, public tiles, or published artifacts.

## Compatibility and naming note

This lane is intentionally cautious. Flora documentation contains a migration concern around bespoke Flora decision envelopes versus cross-cutting runtime envelopes. The Flora missing/planned-files register says the finite-outcome envelope should align to `RuntimeResponseEnvelope`, and it flags a bespoke `FloraDecisionEnvelope` as CONFLICTED / migration-tracked. The Flora API contracts likewise use cross-cutting finite outcomes and flag the distinct `FloraDecisionEnvelope` question as UNKNOWN rather than inventing a Flora-only envelope.

Repository evidence also shows a placeholder schema at `schemas/contracts/v1/domains/flora/decision_envelope.schema.json` with status `PROPOSED` and an `x-kfm.fixtures_root` of `fixtures/domains/flora/decision_envelope/`. The requested path for this README is plural: `fixtures/domains/flora/decision_envelopes/`. Until an ADR or migration note reconciles the singular/plural fixture path and the runtime-vs-domain envelope question, this README treats the current directory as a compatibility fixture lane, not canonical schema authority.

## Placement basis

Directory rules and the root fixture README keep fixture material under the `fixtures/` responsibility root. This lane is therefore a Flora-domain fixture lane for finite-outcome envelope examples, not a data lifecycle root, not a policy root, not a schema root, not a source registry, not a release root, and not a publication target.

The root fixture README also states that `fixtures/` is for operational rendering inputs rather than validator-only test data, and that fixtures must not contain RAW, WORK, QUARANTINE data, restricted geospatial detail, or canonical truth. This README inherits those boundaries.

## Related fixture and doctrine references

- `../README.md`
- `../../README.md`
- `../../../docs/domains/flora/API_CONTRACTS.md`
- `../../../docs/domains/flora/MISSING_OR_PLANNED_FILES.md`
- `../../../docs/domains/flora/MAP_UI_CONTRACTS.md`
- `../../../docs/domains/flora/SENSITIVITY.md`
- `../../../docs/domains/flora/DATA_LIFECYCLE.md`
- `../../../contracts/domains/flora/`
- `../../../contracts/runtime/decision_envelope.md`
- `../../../contracts/runtime/runtime_response_envelope.md`
- `../../../schemas/contracts/v1/domains/flora/decision_envelope.schema.json`
- `../../../schemas/contracts/v1/domains/flora/`
- `../../../schemas/contracts/v1/runtime/`
- `../../../policy/domains/flora/`
- `../../../policy/sensitivity/flora/`
- `../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.expected.json`, `*.json`, `*.jsonl`, or `*.md` examples;
- toy finite-outcome fixtures for `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, `HOLD`, and any explicitly supported runtime extensions;
- toy Flora feature/detail, Evidence Drawer, Focus Mode, correction, review, and release-gate envelope examples;
- compatibility examples that compare a Flora-shaped decision envelope with the cross-cutting `RuntimeResponseEnvelope` expectation;
- negative examples proving that policy, rights, release, evidence, freshness, or review gaps produce bounded refusal or abstention rather than uncited claims;
- public-safe examples proving that valid released support can produce an `ANSWER` with traceable evidence references;
- README files explaining fixture intent and boundaries.

## Exclusions

Do not use this lane for:

- authoritative Flora observations, taxon records, specimens, range layers, source descriptors, or source-system exports;
- live upstream fetch results, scraped payloads, steward-only records, restricted agency records, or real upstream response samples;
- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, PUBLISHED, receipt, proof, registry, or release-lifecycle artifacts;
- real EvidenceBundles, proof packs, run receipts, source-refresh receipts, release manifests, rollback cards, correction notices, review records, or policy decisions;
- policy rules, rights approvals, reviewer approvals, concrete transform parameters, or operational freshness thresholds;
- restricted location detail, reconstructive clues, or geometry that could reasonably be mistaken for a real restricted observation;
- connector, pipeline, validator, package, schema, policy, release, or app implementation code;
- public API material, public map material, public tiles, published artifacts, or canonical layer registry entries.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, and reviewable.
- Use toy identifiers, toy taxa, toy source names, toy timestamps, toy evidence references, and toy geometries unless a bounded check explicitly requires a more realistic shape.
- Keep envelope state explicit: outcome, reason code, evidence state, policy state, rights state, freshness state, review state, release state, correction state, and any receipt/reference state needed by the fixture.
- Do not let a fixture imply that a bespoke Flora-only envelope is canonical. Mark compatibility examples as compatibility examples.
- Prefer `RuntimeResponseEnvelope`-aligned examples for Focus Mode and AI-facing surfaces unless an accepted contract says otherwise.
- Pair each input with an expected finite outcome when practical.
- Do not include raw feature properties, restricted geometry, direct model-runtime output, or unpublished candidate content in public-surface examples.
- Treat `schema-valid`, `policy-admissible`, `release-safe`, `citation-safe`, and `renderer-safe` as separate checks.
- Do not treat decision-envelope fixtures as evidence, approval, release state, policy authority, source authority, schema authority, or implementation proof.

## Expected decision-envelope examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Released public-safe Flora feature with resolved evidence | `ANSWER` | Include synthetic evidence references and policy-allow state. |
| Evidence missing or unresolved | `ABSTAIN` | No generated Flora claim should be emitted without support. |
| Rights, policy, or release state blocks exposure | `DENY` | Include reason code; no fallback rendering or uncited answer. |
| Malformed request or schema-shaped payload failure | `ERROR` | Error state must not leak restricted or unpublished content. |
| Review or promotion pending | `HOLD` | Preserve pending state and do not promote through fixtures. |
| Focus Mode asks beyond released evidence | `ABSTAIN` | Cite-or-abstain remains the default. |
| Stale source support with no current alternative | `ABSTAIN` or stale reason state | Freshness state is visible and bounded. |
| Compatibility comparison between local and runtime envelope names | NEEDS VERIFICATION | Use only to document migration risk until an ADR resolves naming. |

## Maintenance notes

- Update this README when payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each fixture to the governed-API test, Focus Mode test, Evidence Drawer test, review/correction test, schema check, policy check, or documentation example that consumes it.
- If the repo adopts `fixtures/domains/flora/decision_envelope/` instead of this plural path, add a migration note and avoid maintaining parallel fixture authorities.
- If an ADR retires local `decision_envelope` fixtures in favor of `runtime_envelopes/`, move or deprecate this lane with a reversible migration note.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real or restricted material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: populated from empty placeholder content.
- Fixture payload inventory: no payloads verified in this directory during this update.
- Schema naming alignment: NEEDS VERIFICATION because the repository has a PROPOSED `decision_envelope.schema.json` pointing at singular `fixtures/domains/flora/decision_envelope/`, while this requested path is plural.
- Runtime envelope alignment: NEEDS VERIFICATION against accepted runtime contracts and any ADR resolving `DecisionEnvelope` / `RuntimeResponseEnvelope` / `FloraDecisionEnvelope` naming.
- Tests and validators: NOT RUN.

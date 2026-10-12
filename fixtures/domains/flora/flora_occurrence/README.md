# Flora occurrence fixtures

`fixtures/domains/flora/flora_occurrence/`

Status: draft / fixture lane / semantic-contract support.

This directory is for small synthetic Flora occurrence fixture examples used by bounded schema checks, semantic-contract reviews, renderer checks, governed API tests, Evidence Drawer examples, Focus Mode examples, and documentation dry-runs. A Flora occurrence fixture may represent a toy plant presence claim, occurrence candidate, public-safe derivative, or refusal case, but it is not a real occurrence record and must not be treated as source truth, catalog truth, release proof, or publication state.

These files are examples only. They are not authoritative project records, source records, EvidenceBundles, source descriptors, policy decisions, rights approvals, review approvals, release state, public API material, public map material, public tiles, or published artifacts.

## Contract and schema posture

The semantic contract for `FloraOccurrence` is present at `contracts/domains/flora/flora_occurrence.md`. It describes FloraOccurrence as an umbrella occurrence-class object for plant presence claims, source-role posture, evidence closure, geoprivacy, sensitivity, public-safe derivatives, correction, and rollback.

The paired schema at `schemas/contracts/v1/domains/flora/flora_occurrence.schema.json` is present but still a `PROPOSED` scaffold with no declared properties and `additionalProperties: true`. This means fixtures in this lane may support semantic review and future validator work, but they do not prove field-level machine enforcement until the schema, validators, and tests are upgraded and run.

## Placement basis

Directory rules and the root fixture README keep fixture material under the `fixtures/` responsibility root. This lane is therefore a Flora-domain fixture lane for occurrence-shaped examples, not a data lifecycle root, not a source registry, not a catalog root, not a proof root, not a policy root, not a schema root, not a release root, and not a publication target.

The root fixture README also states that `fixtures/` is for operational rendering inputs rather than validator-only test data, and that fixtures must not contain RAW, WORK, QUARANTINE data, sensitive exact geometry, or canonical truth. This README inherits those boundaries.

## Related fixture and doctrine references

- `../README.md`
- `../../README.md`
- `../../../../contracts/domains/flora/flora_occurrence.md`
- `../../../../contracts/domains/flora/occurrence_public.md`
- `../../../../contracts/domains/flora/occurrence_restricted.md`
- `../../../../contracts/domains/flora/rare_plant_record.md`
- `../../../../contracts/domains/flora/specimen_record.md`
- `../../../../contracts/domains/flora/plant_taxon.md`
- `../../../../contracts/domains/flora/flora_taxon_crosswalk.md`
- `../../../../contracts/domains/flora/redaction_receipt.md`
- `../../../../schemas/contracts/v1/domains/flora/flora_occurrence.schema.json`
- `../../../../docs/domains/flora/MISSING_OR_PLANNED_FILES.md`
- `../../../../docs/domains/flora/API_CONTRACTS.md`
- `../../../../docs/domains/flora/MAP_UI_CONTRACTS.md`
- `../../../../docs/domains/flora/SENSITIVITY.md`
- `../../../../docs/domains/flora/DATA_LIFECYCLE.md`
- `../../../../policy/domains/flora/`
- `../../../../policy/sensitivity/flora/`
- `../../../../data/registry/sources/flora/`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.expected.json`, `*.json`, `*.geojson`, `*.jsonl`, or `*.md` examples;
- toy Flora occurrence examples for positive-path and negative-path checks;
- public-safe occurrence derivative examples that demonstrate generalized, aggregated, or otherwise safe display posture;
- restricted-case examples that prove public surfaces deny, abstain, or require transformation rather than exposing unsafe detail;
- source-role examples that keep observed, specimen-backed, survey-derived, aggregate, modeled, administrative, candidate, and synthetic support separate;
- taxon-support examples that show unresolved taxonomy, synonymy, or crosswalk gaps as bounded outcomes rather than silent acceptance;
- temporal examples that keep observed time, source time, retrieval time, release time, freshness state, and correction time distinct where material;
- README files explaining fixture intent and boundaries.

## Exclusions

Do not use this lane for:

- real Flora occurrences, taxon records, specimen records, survey records, range layers, source descriptors, or source-system exports;
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
- Make occurrence posture explicit: candidate, observed, specimen-backed, survey-derived, aggregate, modeled, administrative, synthetic, public-safe derivative, or restricted-case fixture.
- Keep source role, evidence state, taxon state, rights state, policy state, sensitivity state, freshness state, review state, release state, correction state, and expected outcome explicit where material.
- Prefer no geometry unless the fixture explicitly needs geometry. When geometry is required, use toy or public-safe generalized geometry.
- Pair each input with an expected output when practical.
- Treat `schema-valid`, `semantic-valid`, `evidence-resolved`, `taxon-resolved`, `policy-admissible`, `release-safe`, and `renderer-safe` as separate checks.
- Do not treat occurrence fixtures as evidence, approval, release state, proof authority, source authority, schema authority, implementation proof, or published output.

## Expected occurrence fixture examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Public-safe non-sensitive occurrence with resolved synthetic support | `ANSWER` | Demonstrates positive path without becoming source truth. |
| Occurrence candidate with unresolved taxon support | `ABSTAIN` | Taxon uncertainty remains visible. |
| Occurrence with missing evidence support | `ABSTAIN` | Cite-or-abstain blocks unsupported claims. |
| Occurrence blocked by policy, rights, or release state | `DENY` | Include synthetic reason code and no fallback claim. |
| Restricted-case occurrence presented to public surface | `DENY` or transformed public-safe derivative | Public-facing fixtures must not expose unsafe detail. |
| Stale occurrence support with no current alternative | `ABSTAIN` / `SOURCE_STALE` | Freshness state is visible and bounded. |
| Conflicting source roles or source assertions | `CONFLICTED_SUPPORT` | Preserve source-role separation. |
| Malformed or contract-incomplete occurrence payload | `ERROR` or validation failure | Error state must not leak restricted or unpublished content. |

## Maintenance notes

- Update this README when payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each fixture to the schema check, semantic-contract review, governed-API test, Evidence Drawer test, Focus Mode test, renderer check, policy check, or documentation example that consumes it.
- If a fixture becomes stable enough to anchor a regression check, pair it with an expected output and document the consumer.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real or sensitive material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: populated from empty placeholder content.
- Fixture payload inventory: no payloads verified in this directory during this update.
- Contract alignment: PARTIALLY VERIFIED against `contracts/domains/flora/flora_occurrence.md`.
- Schema alignment: NEEDS VERIFICATION because the paired schema is present but remains a permissive `PROPOSED` scaffold.
- Consumer alignment: NEEDS VERIFICATION against validators, renderer checks, governed-API tests, Evidence Drawer tests, Focus Mode tests, and policy checks.
- Tests and validators: NOT RUN.

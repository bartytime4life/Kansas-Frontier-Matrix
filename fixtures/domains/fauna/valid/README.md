# Fauna valid fixtures

`fixtures/domains/fauna/valid/`

Status: draft / fixture lane.

This directory is for small synthetic Fauna fixture examples that are expected to pass the applicable bounded contract, schema, renderer, or governed-API checks for public-safe Fauna material. Valid fixtures demonstrate acceptable shapes for non-sensitive occurrences, public-safe range or seasonal-range representations, released/evidence-shaped examples, and other positive-path cases without becoming source truth.

These files are examples only. They are not authoritative project records, source records, EvidenceBundles, source descriptors, policy decisions, sensitivity decisions, rights approvals, release state, public API material, public map material, public tiles, or published artifacts.

## Placement basis

Directory rules and the root fixture README keep fixture material under the `fixtures/` responsibility root. This lane is therefore the Fauna-domain valid fixture lane, not a data lifecycle root, not a policy root, not a source registry, not a release root, and not a publication target.

The root fixture README also states that `fixtures/` is for operational rendering inputs rather than validator-only test data, and that fixtures must not contain RAW, WORK, QUARANTINE data, sensitive exact geometry, or canonical truth. This README inherits those boundaries.

## Related fixture lanes

- `../README.md`
- `../golden/README.md`
- `../invalid/README.md`
- `../layers/README.md`
- `../sensitive_deny/README.md`
- `../stale_source/README.md`
- `../synthetic/README.md`

## Related references

- `../../../../docs/domains/fauna/MISSING_OR_PLANNED_FILES.md`
- `../../../../docs/domains/fauna/MAP_UI_CONTRACTS.md`
- `../../../../docs/domains/fauna/SENSITIVITY.md`
- `../../../../docs/domains/fauna/DATA_LIFECYCLE.md`
- `../../../../docs/domains/fauna/POLICY.md`
- `../../../../contracts/domains/fauna/`
- `../../../../schemas/contracts/v1/domains/fauna/`
- `../../../../policy/domains/fauna/`
- `../../../../policy/sensitivity/fauna/`
- `../../../../docs/doctrine/directory-rules.md`

## Current known payloads

| File | Status | Notes |
|---|---|---|
| `non_sensitive_occurrence.json` | PROPOSED placeholder | Placeholder created from the Fauna missing/planned-files inventory. Treat as a proposed valid-fixture slot, not as evidence that a validator currently passes it. |
| `range_polygon.geojson` | PROPOSED placeholder | Placeholder created from the Fauna missing/planned-files inventory. Treat as a proposed public-safe range fixture slot, not as a canonical range layer. |
| `seasonal_range.geojson` | PROPOSED placeholder | Placeholder created from the Fauna missing/planned-files inventory. Treat as a proposed public-safe seasonal-range fixture slot, not as a canonical range layer. |

## Accepted material

This lane may contain:

- small synthetic `*.json`, `*.geojson`, `*.jsonl`, or `*.md` examples expected to pass bounded positive-path checks;
- non-sensitive occurrence examples with toy identifiers and public-safe attributes;
- public-safe range, seasonal-range, aggregated, generalized, or derivative geometry examples that do not reveal sensitive exact locations;
- valid `EvidenceDrawerPayload`, `LayerManifest`, renderer-input, governed-API, Focus Mode, or contract-shaped examples;
- fixture-shaped examples that prove source role, evidence state, rights state, sensitivity state, freshness state, review state, release state, and correction state are present and acceptable for the tested positive path;
- README files explaining fixture intent and boundaries.

## Exclusions

Do not use this lane for:

- authoritative taxon, occurrence, monitoring, mortality, disease, invasive-species, range, nest, den, roost, hibernacula, spawning-site, or sensitive-site records;
- source-system exports, live upstream fetch results, scraped payloads, steward-only records, restricted agency records, or real upstream response samples;
- real observer names, source-system identifiers, parcel-level hints, collection notes, field notes, coordinates, timestamps, or taxon-site combinations that could imply a real observation;
- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, PUBLISHED, receipt, proof, registry, or release-lifecycle artifacts;
- EvidenceBundles, proof packs, source descriptors, run receipts, release manifests, rollback cards, correction notices, review records, or policy decisions;
- policy rules, sensitivity approvals, rights approvals, reviewer approvals, concrete redaction radii, concrete fuzzing parameters, or operational freshness thresholds;
- exact sensitive locations, reconstructive geoprivacy clues, or geometry that could reasonably be mistaken for a protected species site;
- connector, pipeline, validator, package, schema, policy, release, or app implementation code;
- public API material, public map material, public tiles, published artifacts, or canonical layer registry entries.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, and reviewable.
- Use toy identifiers, toy taxa, toy source names, toy timestamps, and toy geometries unless a test explicitly requires a more realistic shape.
- Mark artificial values clearly when there is any chance they could be mistaken for real evidence.
- Positive-path validity means the fixture can pass its intended bounded check; it does not mean the payload is authoritative, released, sensitive-safe for all contexts, or valid for every contract.
- Keep source role, evidence state, rights state, sensitivity state, freshness state, review state, release state, correction state, and expected outcome explicit where material.
- Keep geometry public-safe. Prefer generalized polygons, coarse toy ranges, or no geometry unless the test requires geometry.
- Pair each valid input with a matching expected output in `../golden/` when practical.
- Do not let a valid fixture bypass sensitivity, rights, freshness, review, or release checks. A positive-path fixture should still show why the positive path is admissible.
- Do not treat valid fixtures as evidence, approval, release state, policy authority, source authority, or implementation proof.

## Expected valid-fixture examples

| Scenario | Expected use | Notes |
|---|---|---|
| Non-sensitive occurrence | Contract or API positive-path check | Uses toy identifiers and public-safe attributes only. |
| Public-safe range polygon | Renderer or layer-contract smoke test | Demonstrates generalized range shape, not a canonical range layer. |
| Public-safe seasonal range | Time-aware renderer or API check | Demonstrates seasonal window shape without real sensitive movement data. |
| Released/evidence-shaped drawer payload | Evidence Drawer fixture | Uses synthetic released/evidence-shaped references only. |
| Public-safe Focus Mode envelope | Governed-AI fixture | Contains bounded context, no raw feature properties, no restricted geometry. |
| Valid correction-visible state | UI trust-state fixture | Shows correction state shape without using a real CorrectionNotice. |
| Valid freshness-visible state | Freshness check | Demonstrates fresh/supportable state without real source-refresh receipts. |
| Valid redacted/generalized derivative | Policy/UI positive path | Must include synthetic transform reference shape without exposing exact sensitive geometry. |

## Maintenance notes

- Update this README when payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each fixture to the validator, renderer check, governed-API contract, Focus Mode test, planning register, or documentation example that consumes it.
- Keep payloads small enough for normal code review.
- Move expected outputs to `../golden/` when they become stable enough to anchor regression checks.
- If a valid fixture starts encoding real source behavior, move that concern to the appropriate source descriptor, pipeline fixture, test fixture, or governed lifecycle lane.
- If a fixture accidentally includes real or reconstructive sensitive detail, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: populated from empty placeholder content.
- Payload inventory: PARTIALLY VERIFIED — `non_sensitive_occurrence.json`, `range_polygon.geojson`, and `seasonal_range.geojson` are present as PROPOSED placeholders.
- Fixture-consumer alignment: NEEDS VERIFICATION against validators, renderer checks, governed-API tests, Focus Mode tests, and schema contracts.
- Tests and validators: NOT RUN.

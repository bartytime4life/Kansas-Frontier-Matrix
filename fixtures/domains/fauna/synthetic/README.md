# Fauna synthetic fixtures

`fixtures/domains/fauna/synthetic/`

Status: draft / fixture lane.

This directory is for small synthetic Fauna fixture examples used by bounded tests, validators, renderer checks, helper scripts, release dry-runs, and documentation examples. Synthetic fixtures are deliberately artificial: they may be shaped like Fauna inputs, outputs, manifests, envelopes, receipts, source windows, or policy contexts, but they are not real fauna evidence and must never be treated as source truth.

These files are examples only. They are not authoritative project records, source records, EvidenceBundles, source descriptors, policy decisions, sensitivity decisions, rights approvals, release state, public API material, public map material, public tiles, or published artifacts.

## Placement basis

Directory rules and the root fixture README keep fixture material under the `fixtures/` responsibility root. This lane is therefore the Fauna-domain synthetic fixture lane, not a data lifecycle root, not a policy root, not a source registry, not a release root, and not a publication target.

The root fixture README also states that `fixtures/` is for operational rendering inputs rather than validator-only test data, and that fixtures must not contain RAW, WORK, QUARANTINE data, sensitive exact geometry, or canonical truth. This README inherits those boundaries.

## Related fixture lanes

- `../README.md`
- `../golden/README.md`
- `../invalid/README.md`
- `../layers/README.md`
- `../sensitive_deny/README.md`
- `../stale_source/README.md`

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
| `no_network_drift_window.json` | PROPOSED placeholder | Placeholder created from the Fauna missing/planned-files inventory. Treat as a synthetic planning fixture only, not as proof of implemented drift-window behavior. |

## Accepted material

This lane may contain:

- small synthetic `*.json`, `*.geojson`, `*.jsonl`, or `*.md` examples;
- toy input payloads for Fauna contracts, schemas, validators, renderers, governed API seams, Evidence Drawer payloads, Focus Mode envelopes, and fixture-driven documentation;
- toy expected outputs for bounded tests and dry-runs;
- fixture-shaped placeholders that point back to planning registers without claiming implementation;
- no-network drift-window, source-window, freshness-window, sensitivity-window, or release-window examples;
- synthetic public-safe generalized geometries that cannot be mistaken for real sensitive locations;
- README files explaining fixture intent and boundaries.

## Exclusions

Do not use this lane for:

- authoritative taxon, occurrence, monitoring, mortality, disease, invasive-species, range, nest, den, roost, hibernacula, spawning-site, or sensitive-site records;
- source-system exports, live upstream fetch results, scraped payloads, steward-only records, restricted agency records, or real upstream response samples;
- real observer names, source-system identifiers, parcel-level hints, collection notes, field notes, coordinates, timestamps, or taxon-site combinations that could imply a real observation;
- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, PUBLISHED, receipt, proof, registry, or release-lifecycle artifacts;
- EvidenceBundles, proof packs, source descriptors, run receipts, release manifests, rollback cards, correction notices, review records, or policy decisions;
- policy rules, sensitivity approvals, rights approvals, reviewer approvals, concrete redaction radii, concrete fuzzing parameters, or operational freshness thresholds;
- connector, pipeline, validator, package, schema, policy, release, or app implementation code;
- public API material, public map material, public tiles, published artifacts, or canonical layer registry entries.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, and reviewable.
- Use toy identifiers, toy taxa, toy source names, toy timestamps, and toy geometries unless a test explicitly requires a more realistic shape.
- Mark artificial values clearly when there is any chance they could be mistaken for real evidence.
- Prefer no geometry unless the test explicitly needs a geometry-shaped placeholder.
- When geometry is required, use coarse toy geometry that does not correspond to real sensitive sites or reconstructive geoprivacy clues.
- Keep source role, evidence state, rights state, sensitivity state, freshness state, review state, release state, correction state, and expected outcome explicit where material.
- Keep synthetic fixtures independent from network access. They should be usable in no-network tests and dry-runs.
- Pair inputs with expected outputs when practical.
- Do not treat synthetic fixtures as evidence, approval, release state, policy authority, source authority, or implementation proof.

## Expected synthetic-fixture examples

| Scenario | Expected use | Notes |
|---|---|---|
| No-network drift window | Validator or planning dry-run | Proves comparison shape without live connector access. |
| Toy stale source window | Freshness test | Exercises stale logic without real source timestamps. |
| Toy sensitivity context | Policy / UI negative-state test | Exercises denial and redaction pathways without real sensitive records. |
| Toy layer manifest | Renderer or layer-contract smoke test | Must not become a real layer registry entry. |
| Toy Evidence Drawer payload | UI fixture | Must use released/evidence-shaped placeholders, not real EvidenceBundles. |
| Toy Focus Mode envelope | Governed-AI fixture | Must not include raw feature properties, restricted geometry, or direct model runtime outputs. |
| Toy correction state | UI trust-state fixture | Shows correction visibility without using a real CorrectionNotice. |
| Toy release window | Release dry-run fixture | Demonstrates state shape without creating a release decision. |

## Maintenance notes

- Update this README when payload files, validators, tests, helper scripts, or expected-output names are added.
- Link each fixture to the validator, renderer check, governed-API contract, Focus Mode test, planning register, or documentation example that consumes it.
- Keep payloads small enough for normal code review.
- If a synthetic fixture starts encoding real source behavior, move that concern to the appropriate source descriptor, pipeline fixture, test fixture, or governed lifecycle lane.
- If a fixture accidentally includes real or reconstructive sensitive detail, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: populated from empty placeholder content.
- Payload inventory: PARTIALLY VERIFIED — `no_network_drift_window.json` is present as a PROPOSED placeholder.
- Fixture-consumer alignment: NEEDS VERIFICATION against validators, renderer checks, governed-API tests, and source-refresh tests.
- Tests and validators: NOT RUN.

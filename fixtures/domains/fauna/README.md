# Fauna fixtures

`fixtures/domains/fauna/`

Status: draft / fixture root.

This directory is the Fauna-domain fixture root for small, public-safe, synthetic, and reviewable runtime examples. It organizes positive-path, negative-path, renderer, stale-source, synthetic, policy-denial, and expected-output fixture lanes for bounded checks around Fauna contracts, schemas, renderer behavior, governed-API seams, Evidence Drawer payloads, Focus Mode envelopes, and documentation examples.

These files are examples only. They are not authoritative project records, source records, EvidenceBundles, source descriptors, policy decisions, rights approvals, review approvals, release state, public API material, public map material, public tiles, or published artifacts.

## Placement basis

Directory rules make file placement part of governance: a file's location encodes ownership, responsibility, and lifecycle posture. The `fixtures/` root is therefore the correct responsibility root for small runtime fixture corpora and public-safe generalized examples, while `data/` remains the governed lifecycle root and `tests/fixtures/` remains the deterministic test-only fixture root.

The root fixture README states that `fixtures/` is for operational rendering inputs, not validator-only test data. It also prohibits RAW, WORK, or QUARANTINE data; restricted geospatial detail; and treating fixture corpora as canonical truth. This README inherits those boundaries for every Fauna fixture sublane.

## Current fixture lanes

| Lane | Purpose | Status |
|---|---|---|
| `golden/` | Stable expected-output examples for bounded tests, renderer checks, helper scripts, release dry-runs, or documentation examples. | Draft fixture lane. |
| `invalid/` | Negative examples expected to fail validation, policy, renderer, or governed-API checks. | Draft fixture lane. |
| `layers/` | Layer-shaped fixture examples for Fauna map, renderer, manifest, and trust-state behavior. | Draft fixture lane. |
| `sensitive_deny/` | Fail-closed examples for policy-restricted Fauna scenarios, rights uncertainty, missing review, missing transform receipts, and risky joins. | Draft fixture lane. |
| `stale_source/` | Stale-source, freshness-window, stale-badge, superseded-release, and `SOURCE_STALE` examples. | Draft fixture lane. |
| `synthetic/` | Artificial no-network and planning fixtures that may be shaped like Fauna objects but are not source truth or implementation proof. | Draft fixture lane. |
| `valid/` | Public-safe positive-path examples expected to pass bounded checks. | Draft fixture lane. |

## Current known payload examples

| Path | Status | Notes |
|---|---|---|
| `valid/non_sensitive_occurrence.json` | PROPOSED placeholder | Proposed valid-fixture slot from the Fauna missing/planned-files inventory. |
| `valid/range_polygon.geojson` | PROPOSED placeholder | Proposed public-safe range fixture slot, not a canonical range layer. |
| `valid/seasonal_range.geojson` | PROPOSED placeholder | Proposed public-safe seasonal-range fixture slot, not a canonical range layer. |
| `synthetic/no_network_drift_window.json` | PROPOSED placeholder | Proposed no-network drift-window fixture slot, not proof of implemented drift-window behavior. |
| `invalid/unresolved_taxonomy.json` | NEEDS VERIFICATION | Search-visible negative fixture payload; content and consumer alignment not reviewed in this README update. |
| `invalid/over_precise_sensitive.json` | NEEDS VERIFICATION | Search-visible negative fixture payload; content and consumer alignment not reviewed in this README update. |

Payload inventory is partial. Add or revise this table only after inspecting the exact files and any validator, renderer, governed-API, or Focus Mode consumers that use them.

## Related references

- `../../../docs/domains/fauna/MISSING_OR_PLANNED_FILES.md`
- `../../../docs/domains/fauna/MAP_UI_CONTRACTS.md`
- `../../../docs/domains/fauna/SENSITIVITY.md`
- `../../../docs/domains/fauna/DATA_LIFECYCLE.md`
- `../../../docs/domains/fauna/POLICY.md`
- `../../../docs/domains/fauna/VERIFICATION_BACKLOG.md`
- `../../../contracts/domains/fauna/`
- `../../../schemas/contracts/v1/domains/fauna/`
- `../../../policy/domains/fauna/`
- `../../../policy/sensitivity/fauna/`
- `../../../data/registry/sources/fauna/`
- `../../../docs/doctrine/directory-rules.md`
- `../../README.md`

## Accepted material

This fixture root may contain:

- small synthetic `*.json`, `*.geojson`, `*.jsonl`, or `*.md` examples;
- public-safe generalized geospatial examples used by renderer smoke tests, performance checks, or UI trust-state checks;
- positive-path fixtures in `valid/` and expected-output fixtures in `golden/`;
- negative-path fixtures in `invalid/`, `sensitive_deny/`, and `stale_source/`;
- no-network, drift-window, freshness-window, policy-window, and release-window examples in `synthetic/`;
- layer-shaped examples in `layers/` that exercise renderer and manifest behavior without becoming layer registry entries;
- README files explaining fixture intent, maturity, and boundaries.

## Exclusions

Do not use this fixture root for:

- authoritative taxon, occurrence, monitoring, mortality, disease, invasive-species, range, or restricted-site records;
- source-system exports, live upstream fetch results, scraped payloads, steward-only records, restricted agency records, or real upstream response samples;
- real observer names, source-system identifiers, parcel-level hints, collection notes, field notes, coordinates, timestamps, or combinations of attributes that could imply a real observation;
- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, PUBLISHED, receipt, proof, registry, or release-lifecycle artifacts;
- EvidenceBundles, proof packs, source descriptors, run receipts, source-refresh receipts, release manifests, rollback cards, correction notices, review records, or policy decisions;
- policy rules, rights approvals, reviewer approvals, concrete transform parameters, or operational freshness thresholds;
- restricted location detail, reconstructive clues, or geometry that could reasonably be mistaken for a real restricted observation;
- connector, pipeline, validator, package, schema, policy, release, or app implementation code;
- public API material, public map material, public tiles, published artifacts, or canonical layer registry entries.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, and reviewable.
- Use toy identifiers, toy taxa, toy source names, toy timestamps, and toy geometries unless a bounded check explicitly requires a more realistic shape.
- Mark artificial values clearly when there is any chance they could be mistaken for real evidence.
- Prefer no geometry unless the fixture explicitly needs a geometry-shaped placeholder.
- When geometry is required, use public-safe generalized or toy geometry that cannot reveal restricted details.
- Keep source role, evidence state, rights state, policy state, freshness state, review state, release state, correction state, and expected outcome explicit where material.
- Keep synthetic fixtures independent from network access. They should be usable in no-network checks and dry-runs.
- Pair positive inputs with stable expected outputs in `golden/` when practical.
- Treat `schema-valid`, `policy-admissible`, `release-safe`, and `renderer-safe` as separate checks.
- Do not treat any fixture as evidence, approval, release state, policy authority, source authority, implementation proof, or published output.

## Recommended naming pattern

Use explicit names that reveal the scenario and expected posture:

```text
<scenario>.input.json
<scenario>.expected.json
<scenario>.geojson
<scenario>.md
```

Examples:

```text
valid/non_sensitive_occurrence.json
golden/non_sensitive_occurrence.expected.json
invalid/unresolved_taxonomy.json
stale_source/source_stale_badge.input.json
stale_source/source_stale_badge.expected.json
synthetic/no_network_drift_window.json
layers/public_safe_range_layer.input.json
```

Existing placeholder names do not need to be renamed unless a validator, consumer contract, or steward review requires it.

## Review checklist

Before adding or changing a Fauna fixture, confirm:

- The file belongs under `fixtures/domains/fauna/`, not `data/`, `release/`, `policy/`, `schemas/`, `contracts/`, or `tests/fixtures/`.
- The fixture is synthetic or public-safe and does not contain RAW, WORK, QUARANTINE, source-export, or restricted material.
- The fixture contains no restricted geospatial detail or reconstructive clue.
- Rights, policy, freshness, review, release, and correction state are explicit where the tested behavior depends on them.
- The fixture is linked to a consumer: validator, renderer check, governed-API contract, Focus Mode test, helper script, dry-run, or documentation example.
- Expected outputs live in `golden/` when they become stable regression anchors.
- Any accidental restricted or real-source material is quarantined through the governed lifecycle and corrected with an auditable path.

## Maintenance notes

- Update this README when fixture lanes are added, removed, renamed, or materially re-scoped.
- Update lane READMEs when payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Keep payloads small enough for normal code review.
- Keep real source behavior in source descriptors, connectors, pipelines, or governed lifecycle lanes, not in synthetic fixture files.
- Keep concrete operational policy values in policy/config homes, not in public fixture prose, unless a value is explicitly synthetic and labeled as such.
- Prefer reversible edits: add fixtures with clear names, pair them with expected outputs, and document the consumer before treating them as regression anchors.

## Verification status

- Target README: replaced greenfield stub content.
- Fixture-lane inventory: PARTIALLY VERIFIED by repository search and recently populated lane READMEs.
- Payload inventory: PARTIALLY VERIFIED; listed payloads include search-visible files and known placeholders, but not a full recursive audit.
- Consumer alignment: NEEDS VERIFICATION against validators, renderer checks, governed-API tests, Focus Mode tests, source-refresh tests, and schema contracts.
- Tests and validators: NOT RUN.

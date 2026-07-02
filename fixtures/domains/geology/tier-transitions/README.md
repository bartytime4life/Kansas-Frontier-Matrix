# Geology tier-transition fixtures

`fixtures/domains/geology/tier-transitions/`

Status: draft / fixture lane / sensitivity and release-tier transition examples.

This directory is for small synthetic Geology tier-transition fixture examples used by sensitivity checks, redaction/generalization checks, governed API examples, Evidence Drawer examples, Focus Mode examples, renderer examples, release-review examples, policy dry-runs, and documentation dry-runs. These fixtures may represent toy changes between public-safe, generalized, restricted, review-only, denied, stale, corrected, or withdrawn postures, but they are not real sensitivity assessments, policy decisions, review approvals, release manifests, or publication records.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, source descriptors, proof packs, review approvals, release state, public API material, public map material, public tiles, or published artifacts.

## Doctrine posture

Geology architecture states that exact borehole, sample, sensitive resource, well-log, and private-well locations default to restricted or generalized public geometry, while unclear rights, unresolved source role, missing evidence, unresolved sensitivity, or absent release state blocks public promotion.

The same architecture describes proposed Geology tier assignments: generalized bedrock/surficial unit polygons are typically public-safe, generalized resource context requires aggregation/generalization support, mineral occurrence and borehole/well-log references require redaction/generalization posture, private/proprietary content fails closed, resource estimates require aggregation and uncertainty support, and 3D/interpolated scenes require representation posture.

The cross-cutting sensitivity doctrine states that sensitivity is a first-class property of every record, assessed at intake, carried on records, and enforced by deterministic, reviewable transforms before release. This fixture lane exists to test those transitions with toy examples.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic fixture examples, not governed lifecycle data. It is not a `data/`, `policy/`, `schemas/`, `contracts/`, `pipelines/`, `pipeline_specs/`, `connectors/`, `release/`, proof, source-registry, catalog, triplet, tile, or publication root.

The root fixture README states that fixtures are operational/runtime examples, not canonical truth, and that RAW, WORK, or QUARANTINE data does not belong here. This README inherits those boundaries.

## Relationship to sibling lanes

Use this lane for examples where the main purpose is a sensitivity, release-tier, redaction, generalization, review, correction, or withdrawal transition. Object-family and UI examples should remain in the appropriate sibling fixture lanes when possible.

| Sibling lane | Relationship |
|---|---|
| `../golden/` | Stable expected outputs for tier-transition examples may be paired there. |
| `../invalid/` | Negative-path tier inputs may move there when the failure posture is the main purpose. |
| `../map-ui/` | Map/UI envelope examples may reference tier-transition outcomes. |
| `../source_role/` | Source-role examples may be referenced when tier changes depend on role posture. |
| `../cross_sections/` | Cross-section examples may reference tier-transition fixtures when display/release posture changes. |
| `../sublanes/` | Sublane-specific examples may reference tier-transition fixtures when sensitivity posture is cross-cutting. |

## Related references

- `../README.md`
- `../../README.md`
- `../golden/README.md`
- `../invalid/README.md`
- `../map-ui/README.md`
- `../source_role/README.md`
- `../cross_sections/README.md`
- `../sublanes/README.md`
- `../../../../docs/domains/geology/ARCHITECTURE.md`
- `../../../../docs/domains/geology/PRESERVATION_MATRIX.md`
- `../../../../docs/domains/geology/MAP_UI_CONTRACTS.md`
- `../../../../docs/domains/geology/API_CONTRACTS.md`
- `../../../../docs/domains/geology/SOURCE_REGISTRY.md`
- `../../../../docs/doctrine/sensitivity.md`
- `../../../../contracts/domains/geology/`
- `../../../../schemas/contracts/v1/domains/geology/`
- `../../../../policy/domains/geology/`
- `../../../../policy/sensitivity/geology/`
- `../../../../data/registry/sources/geology/`
- `../../../../release/manifests/geology/`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.expected.json`, `*.json`, `*.geojson`, `*.jsonl`, `*.yaml`, `*.yml`, or `*.md` examples;
- toy sensitivity-assessment and release-tier transition examples;
- toy redaction/generalization transform examples and expected receipts;
- toy policy-decision examples for `ALLOW`, `DENY`, `HOLD`, `ABSTAIN`, `ERROR`, `SOURCE_STALE`, or review-required outcomes;
- toy transitions from internal candidate posture to public-safe generalized derivative posture;
- toy correction, withdrawal, stale-source, or rollback-trigger examples;
- examples that keep sensitivity, rights, source role, evidence support, review state, release state, correction state, and expected output separate;
- paired expected outputs in `../golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for real geology records, real source exports, live upstream fetch results, lifecycle data, real EvidenceBundles, proof packs, run receipts, release manifests, correction notices, review records, implementation code, public API material, public map material, public tiles, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, and reviewable.
- Use toy source IDs, toy feature IDs, toy layer IDs, toy policy IDs, toy evidence references, toy timestamps, toy hashes, and toy geometries unless a bounded check explicitly requires a more realistic shape.
- Make the starting posture, requested transition, required gate, transform/receipt expectation, and final expected outcome explicit.
- Prefer public-safe generalized geometry. Do not include geometry that could reasonably be mistaken for sensitive real-world data.
- Pair each input with an expected output when practical.
- Treat `tier-known`, `rights-cleared`, `source-role-valid`, `evidence-resolved`, `redaction-recorded`, `generalization-recorded`, `review-approved`, `release-safe`, `citation-safe`, and `renderer-safe` as separate checks.
- Do not treat tier-transition fixtures as policy authority, evidence, approval, release state, schema authority, implementation proof, public-map authority, tile authority, or published output.

## Expected tier-transition fixture examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Public-safe generalized unit polygon remains public-safe | `ALLOW` or valid output | Source terms and release manifest still need verification. |
| Restricted high-precision source requested for public map display | `DENY`, `HOLD`, or generalized derivative | Public exposure requires approved transform posture. |
| Generalized derivative missing transform receipt | Validation failure or review-required output | Public-safe status must be auditable. |
| Rights state unknown | `DENY` or `HOLD` | Unknown rights fail closed. |
| Source role unresolved | `ABSTAIN` or validation failure | Tier transition cannot bypass source-role checks. |
| Evidence support missing | `ABSTAIN` | Cite-or-abstain remains in force. |
| Published layer later corrected or withdrawn | rollback-required expected output | Correction and rollback remain first-class. |

## Maintenance notes

- Update this README when payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each fixture to the sensitivity check, redaction/generalization check, policy check, release-review check, governed-API test, Evidence Drawer test, Focus Mode test, renderer check, topology check, or documentation example that consumes it.
- If a fixture becomes stable enough to anchor a regression check, pair it with an expected output and document the consumer.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real source material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: populated from empty placeholder content.
- Fixture payload inventory: no payloads verified in this directory during this update.
- Geology sensitivity/tier alignment: PARTIALLY VERIFIED against `docs/domains/geology/ARCHITECTURE.md`.
- Cross-cutting sensitivity alignment: PARTIALLY VERIFIED against `docs/doctrine/sensitivity.md`.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Sibling fixture alignment: NEEDS VERIFICATION against populated `golden/`, `invalid/`, `map-ui/`, `source_role/`, `cross_sections/`, and `sublanes/` READMEs.
- Consumer alignment: NEEDS VERIFICATION against sensitivity validators, redaction/generalization checks, policy checks, release-review checks, governed-API tests, Evidence Drawer tests, Focus Mode tests, renderer checks, schema checks, and policy checks.
- Tests and validators: NOT RUN.

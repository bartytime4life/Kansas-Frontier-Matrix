# Flora source-descriptor fixtures

`fixtures/domains/flora/source_descriptors/`

Status: draft / fixture lane / source-registry support.

This directory is for small synthetic Flora `SourceDescriptor` fixture examples used by source-admission checks, source-role checks, rights/sensitivity dry-runs, governed API examples, Evidence Drawer examples, Focus Mode examples, watcher dry-runs, and documentation examples. These fixtures may represent toy Flora source families, authority limits, access posture, attribution posture, cadence posture, source-role posture, or refusal cases, but they are not real source registry records and must not be treated as source truth, catalog truth, release proof, or publication state.

These files are examples only. They are not authoritative project records, source records, live upstream payloads, EvidenceBundles, registry entries, policy decisions, review approvals, release state, public API material, public map material, public tiles, or published artifacts.

## Registry posture

The Flora source registry README describes `data/registry/sources/flora/` as the subtype-first source registry lane for Flora source descriptors, admission state, rights posture, sensitivity posture, and source-role discipline. That registry lane is an admission and authority-control lane, not source data, proof, catalog closure, policy, release authority, public API, or generated botanical truth.

This fixture lane is one step further removed: it is only for synthetic examples that can exercise source-descriptor behavior before real registry records, source payloads, evidence bundles, policy decisions, or release artifacts are involved.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic fixture examples, not governed lifecycle data. It is not a `data/registry/`, `data/raw/`, `data/work/`, `data/quarantine/`, `policy/`, `schemas/`, `contracts/`, `release/`, proof, or publication root.

The root fixture README states that fixtures are operational/runtime examples, not canonical truth, and that RAW, WORK, or QUARANTINE data does not belong here. The Flora fixture backlog lists this lane as the place for one `SourceDescriptor` fixture per Flora source family. This README inherits those boundaries.

## Related references

- `../README.md`
- `../../README.md`
- `../golden/README.md`
- `../invalid/README.md`
- `../plants_drift/README.md`
- `../plant_taxon/README.md`
- `../flora_occurrence/README.md`
- `../evidence_bundles/README.md`
- `../../../../data/registry/sources/flora/README.md`
- `../../../../data/registry/sources/README.md`
- `../../../../docs/domains/flora/MISSING_OR_PLANNED_FILES.md`
- `../../../../docs/domains/flora/SOURCE_REGISTRY.md`
- `../../../../docs/domains/flora/SOURCE_FAMILIES.md`
- `../../../../docs/domains/flora/SOURCES.md`
- `../../../../docs/domains/flora/SOURCE_INTAKE.md`
- `../../../../docs/domains/flora/DATA_LIFECYCLE.md`
- `../../../../docs/domains/flora/SENSITIVITY.md`
- `../../../../schemas/contracts/v1/source/`
- `../../../../policy/domains/flora/`
- `../../../../policy/sensitivity/flora/`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.json`, `*.yaml`, `*.yml`, `*.jsonl`, or `*.md` examples;
- toy source-descriptor examples for positive-path and negative-path checks;
- source-family examples for taxonomy, occurrence, specimen, vegetation, invasive-plant, phenology, restoration, and watcher-oriented source families;
- examples that keep source identity, source role, authority limits, rights posture, sensitivity posture, cadence, attribution, freshness, and activation state separate;
- examples that prove missing identity, unclear rights, stale metadata, source-role mismatch, or inactive source state produces a bounded outcome;
- paired expected outputs in `../golden/` when behavior becomes a stable regression anchor.

## Exclusions

Do not use this lane for real source records, real upstream payloads, live endpoint samples, credentials, lifecycle data, registry authority, release artifacts, proof packs, policy rules, implementation code, public API payloads, public map data, public tiles, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, and reviewable.
- Use toy source IDs, toy source names, toy URLs, toy licenses, toy contacts, toy cadence values, toy version strings, and toy evidence references unless a bounded check explicitly requires a more realistic shape.
- Make source posture explicit: candidate, active, inactive, restricted, denied, stale, superseded, synthetic, or review-required.
- Keep source role, source family, authority limits, rights state, sensitivity state, cadence state, freshness state, review state, release state, and expected outcome explicit where material.
- Pair each input with an expected output when practical.
- Treat `schema-valid`, `semantic-valid`, `source-role-valid`, `rights-known`, `sensitivity-reviewed`, `freshness-known`, `registry-admissible`, and `release-safe` as separate checks.
- Do not treat source-descriptor fixtures as registry authority, evidence, approval, release state, source authority, implementation proof, or published output.

## Expected fixture examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Public-safe toy source descriptor with complete support | `ANSWER` or valid descriptor output | Demonstrates positive path without becoming registry authority. |
| Missing source ID or source family | Validation failure or `ERROR` | Source identity must be stable before use. |
| Source role unclear | `ABSTAIN` or review-required output | Source-role anti-collapse remains visible. |
| Rights posture unknown | `HOLD`, `DENY`, or review-required output | Unknown reuse posture blocks public use. |
| Source freshness unknown or stale | `SOURCE_STALE` or review-required output | Freshness state remains visible. |
| Inactive or superseded toy source | Supersession or inactive output | Candidate is not silently admitted. |
| Descriptor asks for direct publication | Validation failure or deny output | Registry and fixtures do not publish. |

## Maintenance notes

- Update this README when payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each fixture to the source-admission check, source-role test, rights/sensitivity check, watcher dry-run, governed-API test, Evidence Drawer test, Focus Mode test, or documentation example that consumes it.
- If a fixture becomes stable enough to anchor a regression check, pair it with an expected output and document the consumer.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real source material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: populated from empty placeholder content.
- Fixture payload inventory: no payloads verified in this directory during this update.
- Flora fixture backlog alignment: PARTIALLY VERIFIED against the Flora missing/planned-files register.
- Registry alignment: PARTIALLY VERIFIED against `data/registry/sources/flora/README.md`.
- Consumer alignment: NEEDS VERIFICATION against source-admission checks, source-role checks, watcher dry-runs, governed-API tests, Evidence Drawer tests, Focus Mode tests, schema checks, and policy checks.
- Tests and validators: NOT RUN.

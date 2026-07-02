# Geology source-role fixtures

`fixtures/domains/geology/source_role/`

Status: draft / fixture lane / source-role anti-collapse examples.

This directory is for small synthetic Geology source-role fixtures used by source-admission checks, source-role anti-collapse checks, governed API examples, Evidence Drawer examples, Focus Mode examples, renderer examples, pipeline dry-runs, and documentation dry-runs. These fixtures may represent toy `SourceDescriptor` role examples, permitted-claim examples, not-authoritative-for examples, role-mismatch examples, or bounded non-answer cases, but they are not real source records, registry authority, evidence, release state, or publication material.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, source descriptors, proof packs, review approvals, release state, public API material, public map material, public tiles, or published artifacts.

## Doctrine posture

KFM architecture defines source role as fixed at admission, preserved through promotion, and never upgraded by paraphrase. The same architecture document identifies seven canonical roles: `observed`, `regulatory`, `modeled`, `aggregate`, `administrative`, `candidate`, and `synthetic`.

The Geology source registry applies that rule to Geology: a Geology source enters with exactly one source role, and a publisher that legitimately supports more than one role must be represented as separate `SourceDescriptor` instances rather than one folded multi-role descriptor.

This fixture lane is for proving those distinctions with toy examples. It does not create SourceDescriptor authority, policy authority, source-registry authority, or release authority.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic fixture examples, not governed lifecycle data. It is not a `data/`, `policy/`, `schemas/`, `contracts/`, `pipelines/`, `pipeline_specs/`, `connectors/`, `release/`, proof, source-registry, catalog, triplet, or publication root.

The root fixture README states that fixtures are operational/runtime examples, not canonical truth, and that RAW, WORK, or QUARANTINE data does not belong here. The Geology missing/planned-files register lists `source_role_conflation.json` as a negative fixture concept, which makes this lane a narrow home for source-role-focused examples.

## Relationship to sibling lanes

Use this lane for source-role examples that are broader than one object-family lane.

| Sibling lane | Relationship |
|---|---|
| `../golden/` | Stable expected outputs for source-role examples may be paired there. |
| `../invalid/` | Negative-path role-mismatch inputs may move there when the failure posture is the main purpose. |
| `../cross_sections/` | Cross-section examples may reference source-role fixtures when interpretation role matters. |
| `../map-ui/` | UI examples may reference source-role outcomes when Evidence Drawer or Focus Mode behavior is being checked. |

Future sibling lanes may add valid, borehole, well-log, stratigraphy, bedrock, surficial, geophysics, source, or runtime-envelope fixtures. Source-role examples should link to those lanes rather than duplicating their object-family authority.

## Related references

- `../README.md`
- `../../README.md`
- `../golden/README.md`
- `../invalid/README.md`
- `../cross_sections/README.md`
- `../map-ui/README.md`
- `../../../../docs/architecture/source-role-anti-collapse.md`
- `../../../../docs/architecture/source-roles.md`
- `../../../../docs/domains/geology/SOURCE_REGISTRY.md`
- `../../../../docs/domains/geology/MISSING_OR_PLANNED_FILES.md`
- `../../../../docs/domains/geology/API_CONTRACTS.md`
- `../../../../contracts/domains/geology/`
- `../../../../schemas/contracts/v1/source/`
- `../../../../schemas/contracts/v1/domains/geology/`
- `../../../../data/registry/sources/geology/`
- `../../../../policy/domains/geology/`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, or `*.md` examples;
- toy SourceDescriptor-like examples for the seven source roles;
- toy permitted-claims and not-authoritative-for examples;
- toy source-role mismatch examples;
- toy source-admission, source-role validation, Evidence Drawer, Focus Mode, governed API, renderer, or pipeline dry-run examples;
- examples that prove a source role is not silently upgraded into another role or claim class;
- paired expected outputs in `../golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for real source records, real source exports, live upstream fetch results, lifecycle data, real EvidenceBundles, proof packs, run receipts, release manifests, correction notices, review records, implementation code, public API material, public map material, public tiles, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, and reviewable.
- Use toy source IDs, toy source names, toy claim IDs, toy object-family names, toy evidence references, toy timestamps, and toy hashes unless a bounded check explicitly requires a more realistic shape.
- Make the source role explicit in every fixture.
- Prefer one source role per fixture; use a pair or matrix only when the test intentionally checks separation.
- Make permitted claims and not-authoritative-for claims explicit when relevant.
- Pair each input with an expected output when practical.
- Treat `source-role-valid`, `source-role-mismatch`, `permitted-claim-valid`, `not-authoritative-for-enforced`, `evidence-resolved`, `citation-safe`, `release-safe`, and `renderer-safe` as separate checks.
- Do not treat source-role fixtures as source authority, registry authority, evidence, approval, release state, schema authority, implementation proof, or published output.

## Expected source-role fixture examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Observed toy measurement source used for observed claim | Valid source-role input | Demonstrates positive path without becoming real evidence. |
| Modeled source used as observed support | `ABSTAIN` or validation failure | Modeled output does not become observation by wording. |
| Aggregate source joined to one feature as per-place truth | `ABSTAIN` or validation failure | Aggregate scope remains visible. |
| Candidate source requested for public surface | `HOLD`, `ABSTAIN`, or validation failure | Candidate posture remains pre-release. |
| Synthetic source presented as observed support | `ABSTAIN` or validation failure | Reality boundary remains visible. |
| One publisher represented with multiple roles | Multiple descriptors required | One descriptor should not carry folded roles. |
| Missing source role | Validation failure or `ERROR` | Role is mandatory before use. |

## Maintenance notes

- Update this README when payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each fixture to the source-admission check, source-role validator, governed-API test, Evidence Drawer test, Focus Mode test, renderer check, pipeline dry-run, or documentation example that consumes it.
- If a fixture becomes stable enough to anchor a regression check, pair it with an expected output and document the consumer.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real source material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: populated from empty placeholder content.
- Fixture payload inventory: no payloads verified in this directory during this update.
- Source-role doctrine alignment: PARTIALLY VERIFIED against `docs/architecture/source-role-anti-collapse.md`.
- Geology source-registry alignment: PARTIALLY VERIFIED against `docs/domains/geology/SOURCE_REGISTRY.md`.
- Geology fixture-home alignment: PARTIALLY VERIFIED against the Geology missing/planned-files register.
- Sibling fixture alignment: PARTIALLY VERIFIED against `golden/`, `invalid/`, `cross_sections/`, and `map-ui/` READMEs.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against source-admission checks, source-role validators, governed-API tests, Evidence Drawer tests, Focus Mode tests, renderer checks, pipeline dry-runs, schema checks, and policy checks.
- Tests and validators: NOT RUN.

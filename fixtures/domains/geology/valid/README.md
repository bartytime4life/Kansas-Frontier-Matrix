# Geology valid fixtures

`fixtures/domains/geology/valid/`

Status: draft / fixture lane / positive-path synthetic inputs.

This directory is for small synthetic Geology fixtures that are expected to pass bounded checks when paired with the appropriate schemas, validators, policies, evidence fixtures, and expected outputs. Valid fixtures support semantic-contract reviews, future schema checks, topology checks, renderer checks, governed API examples, Evidence Drawer examples, Focus Mode examples, source-role checks, release dry-runs, pipeline dry-runs, and documentation examples.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, source descriptors, proof packs, review approvals, release state, public API material, public map material, public tiles, or published artifacts.

## Positive-path posture

A valid Geology fixture demonstrates that a synthetic input has enough toy structure to pass the check it was designed for. It does not prove that real geology data, real source rights, real policy decisions, real release manifests, or real public artifacts are present.

Valid fixtures may represent toy `GeologicUnit`, `CrossSection`, `MapContextEnvelope`, source-role, tier-transition, surficial, or other Geology examples. Stable expected outputs should usually be paired in `../golden/`. Negative-path examples should live in `../invalid/` or an object-specific lane when clearer.

## Placement basis

This lane belongs under `fixtures/` because it contains positive-path synthetic examples, not governed lifecycle data. It is not a `data/`, `policy/`, `schemas/`, `contracts/`, `pipelines/`, `pipeline_specs/`, `connectors/`, `release/`, proof, source-registry, catalog, triplet, tile, or publication root.

The root fixture README states that fixtures are operational/runtime examples, not canonical truth, and that RAW, WORK, or QUARANTINE data does not belong here. The Geology no-network test runbook describes a deterministic offline slice using synthetic fixtures with no live source, network call, public data, or release surface. This README inherits those boundaries.

## Relationship to sibling lanes

Use this lane for positive-path synthetic inputs whose main purpose is to pass a bounded check.

| Sibling lane | Relationship |
|---|---|
| `../golden/` | Stable expected outputs for valid inputs should be paired there. |
| `../invalid/` | Negative-path or intentionally rejected inputs belong there. |
| `../units/` | Unit-specific positive examples may live there when unit semantics are the main purpose. |
| `../cross_sections/` | Cross-section positive examples may live there when CrossSection semantics are the main purpose. |
| `../map-ui/` | Map/UI envelope examples may live there when UI/rendering posture is the main purpose. |
| `../source_role/` | Source-role examples may live there when role anti-collapse is the main purpose. |
| `../tier-transitions/` | Sensitivity/release-tier transition examples may live there when transition posture is the main purpose. |
| `../sublanes/` | Sublane-specific valid examples may live in a child sublane when ADR/path posture supports it. |

## Related references

- `../README.md`
- `../../README.md`
- `../golden/README.md`
- `../invalid/README.md`
- `../units/README.md`
- `../cross_sections/README.md`
- `../map-ui/README.md`
- `../source_role/README.md`
- `../tier-transitions/README.md`
- `../sublanes/README.md`
- `../../../../docs/runbooks/geology/NO_NETWORK_TEST_RUNBOOK.md`
- `../../../../docs/domains/geology/FILE_SYSTEM_PLAN.md`
- `../../../../docs/domains/geology/ARCHITECTURE.md`
- `../../../../docs/domains/geology/API_CONTRACTS.md`
- `../../../../docs/domains/geology/MAP_UI_CONTRACTS.md`
- `../../../../docs/domains/geology/SOURCE_REGISTRY.md`
- `../../../../contracts/domains/geology/`
- `../../../../schemas/contracts/v1/domains/geology/`
- `../../../../policy/domains/geology/`
- `../../../../data/registry/sources/geology/`
- `../../../../release/manifests/geology/`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.valid.json`, `*.input.json`, `*.json`, `*.geojson`, `*.jsonl`, `*.yaml`, `*.yml`, or `*.md` examples;
- positive-path Geology object examples with toy identifiers, toy sources, toy evidence references, and public-safe toy geometry;
- valid examples for source role, evidence support, rights state, sensitivity state, geometry/topology state, interpretation state, release-candidate posture, renderer safety, and Focus Mode behavior;
- inputs that can be paired with stable expected outputs in `../golden/`;
- README files explaining fixture intent and boundaries.

## Exclusions

Do not use this lane for real geology records, real source exports, live upstream fetch results, lifecycle data, real EvidenceBundles, proof packs, run receipts, release manifests, correction notices, review records, implementation code, public API material, public map material, public tiles, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, and reviewable.
- Make the intended positive path explicit in the file name, fixture metadata, or paired expected output.
- Prefer one primary success condition per fixture unless a test intentionally checks a full no-network flow.
- Pair valid inputs with expected outputs in `../golden/` when practical.
- Use toy source IDs, toy object IDs, toy layer IDs, toy evidence references, toy timestamps, toy hashes, and toy geometries unless a bounded check explicitly requires a more realistic shape.
- Keep source role, evidence state, source vintage, rights state, sensitivity state, geometry lineage, topology state, review state, release state, correction state, rollback state, and expected outcome explicit where material.
- Prefer public-safe generalized geometry. Do not include geometry that could reasonably be mistaken for sensitive real-world data.
- Treat `schema-valid`, `semantic-valid`, `source-role-valid`, `evidence-resolved`, `rights-cleared`, `policy-admissible`, `topology-valid`, `citation-safe`, `release-safe`, and `renderer-safe` as separate checks.
- Do not treat valid fixtures as evidence, approval, release state, source authority, schema authority, implementation proof, public-map authority, tile authority, or published output.

## Expected valid fixture examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Synthetic generalized GeologicUnit polygon with toy evidence support | Valid input or `ANSWER` output | Pair expected output in `../golden/` when stable. |
| Synthetic CrossSection candidate with disclosed interpretation posture | Valid input or bounded answer | CrossSection truth still depends on evidence and release gates. |
| Synthetic MapContextEnvelope for a released toy layer | Valid UI input | UI state remains downstream of governed evidence. |
| Synthetic source-role example with one role and permitted claims | Valid source-role input | Source role remains fixed and explicit. |
| Synthetic public-safe tier-transition input | Valid policy/release dry-run input | Transition still requires expected outcome and receipt posture. |
| Synthetic Evidence Drawer request with resolvable toy support | `ANSWER` expected output | EvidenceBundle support must be represented by toy references. |

## Maintenance notes

- Update this README when payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each fixture to the semantic-contract review, future schema check, topology check, renderer check, governed-API test, Evidence Drawer test, Focus Mode test, source-role check, tier-transition check, no-network runbook, policy check, or documentation example that consumes it.
- If a fixture becomes stable enough to anchor a regression check, pair it with an expected output in `../golden/` and document the consumer.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real source material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: populated from empty placeholder content.
- Fixture payload inventory: no payloads verified in this directory during this update.
- Golden/invalid alignment: PARTIALLY VERIFIED against `fixtures/domains/geology/golden/README.md` and `fixtures/domains/geology/invalid/README.md`.
- No-network runbook alignment: PARTIALLY VERIFIED against `docs/runbooks/geology/NO_NETWORK_TEST_RUNBOOK.md`.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Sibling fixture alignment: NEEDS VERIFICATION against populated `units/`, `cross_sections/`, `map-ui/`, `source_role/`, `tier-transitions/`, and `sublanes/` READMEs.
- Consumer alignment: NEEDS VERIFICATION against validators, topology checks, renderer checks, governed-API tests, Evidence Drawer tests, Focus Mode tests, pipeline dry-runs, source-role checks, tier-transition checks, schema checks, and policy checks.
- Tests and validators: NOT RUN.

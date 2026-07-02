# Habitat fixtures

`fixtures/domains/habitat/`

Status: draft / fixture domain index / synthetic Habitat examples.

This directory is the parent fixture lane for Habitat-domain synthetic examples. Habitat fixtures support bounded contract reviews, future schema checks, renderer checks, governed API examples, Evidence Drawer examples, Focus Mode examples, source-role checks, context-join checks, policy dry-runs, pipeline dry-runs, watcher dry-runs, proof thin slices, documentation examples, and expected-output pairs.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, source descriptors, policy decisions, review approvals, release state, public API material, public map material, public tiles, Habitat truth, Fauna truth, Flora truth, or published artifacts.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The root fixture README states that `fixtures/` is for operational rendering inputs, not validator-only test data. It also states that RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here.

## Fixture posture

Use this parent lane as an index and boundary document. Object-specific fixture intent should live in child READMEs. Payload files should stay small, synthetic, deterministic, public-safe, and paired with expected outputs where practical.

Habitat fixtures may demonstrate context, evidence references, source-role labels, policy states, correction posture, rollback posture, finite outcomes, and renderer/API behavior. They do not create source authority, evidence closure, policy approval, release approval, public-map authority, tile authority, implementation proof, or published output.

## Current child lane inventory

The following child lanes have populated README coverage in this repository sequence. This table is a navigation index, not proof that payload files, validators, tests, pipelines, or public routes exist.

| Child lane | Purpose | Current posture |
|---|---|---|
| `ecoregions/` | Synthetic ecoregion and regionalization context examples. | Draft fixture lane. |
| `golden/` | Stable expected-output examples paired with synthetic Habitat inputs. | Draft fixture lane. |
| `invalid/` | Negative-path synthetic inputs and bounded non-answer examples. | Draft fixture lane. |
| `habitat_fauna_thin_slice/` | Synthetic cross-domain Habitat × Fauna proof-support examples. | Draft fixture lane. |
| `land_cover/change_summary/` | Synthetic `LandCoverChangeSummary` examples. | Draft fixture lane. |
| `land_cover/class_scheme/` | Synthetic `ClassSchemeProfile` examples. | Draft fixture lane. |
| `land_cover/crosswalk/` | Synthetic `CoverClassCrosswalk` examples. | Draft fixture lane. |
| `land_cover/layer_manifest/` | Synthetic land-cover layer-manifest examples. | Draft fixture lane. |
| `land_cover/model_run/` | Synthetic model-run and receipt examples. | Draft fixture lane. |
| `land_cover/observation/` | Synthetic `LandCoverObservation` examples. | Draft fixture lane. |
| `land_cover/uncertainty/` | Synthetic `UncertaintySurface` examples. | Draft fixture lane. |
| `land_cover/watcher/` | Synthetic watcher, checkpoint, source-drift, and proposed-work examples. | Draft fixture lane. |

## Relationship to responsibility roots

| Root or lane | Relationship |
|---|---|
| `contracts/domains/habitat/` | Semantic meaning for Habitat object families; fixtures supply examples only. |
| `schemas/contracts/v1/domains/habitat/` | Expected machine-shape homes; fixture success does not prove schema authority. |
| `policy/domains/habitat/` and `policy/sensitivity/habitat/` | Policy homes; fixtures do not decide allow, deny, restrict, or abstain outcomes. |
| `pipelines/domains/habitat/` | Executable processing home; fixtures do not implement pipelines. |
| `pipeline_specs/habitat/` | Declarative run/spec home; fixtures are not pipeline specs. |
| `data/registry/sources/habitat/` | Source descriptor home; fixtures do not activate or authorize sources. |
| `data/processed/habitat/` | Lifecycle data home; fixtures do not hold processed data. |
| `data/registry/layers/habitat/` | Layer registry home; fixtures do not create layer-registry authority. |
| `release/manifests/habitat/` | Release home; fixtures do not approve publication. |
| `tests/domains/habitat/` and `tests/fixtures/` | Test homes; this lane supports runtime/checking examples, not test-only fixture authority by itself. |

## Related references

- `../../README.md`
- `ecoregions/README.md`
- `golden/README.md`
- `invalid/README.md`
- `habitat_fauna_thin_slice/README.md`
- `land_cover/change_summary/README.md`
- `land_cover/class_scheme/README.md`
- `land_cover/crosswalk/README.md`
- `land_cover/layer_manifest/README.md`
- `land_cover/model_run/README.md`
- `land_cover/observation/README.md`
- `land_cover/uncertainty/README.md`
- `land_cover/watcher/README.md`
- `../../../docs/domains/habitat/README.md`
- `../../../docs/domains/habitat/sublanes/land_cover.md`
- `../../../docs/domains/habitat/sublanes/ecoregions.md`
- `../../../docs/domains/habitat/FILE_SYSTEM_PLAN.md`
- `../../../contracts/domains/habitat/`
- `../../../schemas/contracts/v1/domains/habitat/`
- `../../../policy/domains/habitat/`
- `../../../pipelines/domains/habitat/`
- `../../../pipeline_specs/habitat/`
- `../../../data/registry/sources/habitat/`
- `../../../release/manifests/habitat/`
- `../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane and its children may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.invalid.json`, `*.expected.json`, `*.json`, `*.geojson`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy Habitat object refs, source refs, evidence refs, policy refs, review refs, release refs, correction refs, rollback refs, finite outcomes, and renderer/API examples;
- toy ecoregion, land-cover, watcher, expected-output, invalid, cross-domain, layer, uncertainty, model-run, and context-join examples;
- paired expected outputs in `golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for real records, source exports, lifecycle data, EvidenceBundles, actual source descriptors, proof packs, run receipts, release manifests, implementation code, public API material, public map material, public tiles, source authority, evidence authority, policy authority, release authority, Habitat truth, Fauna truth, Flora truth, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Use toy IDs, toy refs, toy timestamps, toy digests, toy geometries, and toy hashes.
- Make fixture posture explicit: valid, invalid, expected output, context-only, proof-support, watcher no-op, watcher proposed work, candidate, review-required, deny, hold, abstain, or release-blocked.
- Keep source role, evidence state, rights state, policy state, review state, release state, correction state, rollback state, sensitivity posture, and expected outcome explicit where material.
- Pair each input with an expected output when practical.
- Keep schema validity, semantic validity, source-role validity, evidence support, policy admissibility, release posture, renderer safety, and trust-membrane safety separate.
- Do not treat fixture success as implementation proof, source authority, evidence closure, policy approval, release state, public-map authority, tile authority, or published output.

## Maintenance notes

- Update this README when new Habitat fixture child lanes, payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each fixture to the contract review, schema check, renderer check, governed-API test, Evidence Drawer test, Focus Mode test, source-role check, context-join check, watcher check, proof check, policy check, or pipeline dry-run that consumes it.
- If a fixture becomes stable enough to anchor a regression check, pair it with an expected output and document the consumer.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real source material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: replaced greenfield stub content.
- Child README inventory: PARTIALLY VERIFIED against populated child READMEs fetched during this sequence.
- Fixture payload inventory: no payload files verified under this parent during this update.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Habitat ecoregions fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/habitat/ecoregions/README.md`.
- Habitat land-cover fixture alignment: PARTIALLY VERIFIED against representative populated land-cover child READMEs.
- Cross-domain fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/habitat/habitat_fauna_thin_slice/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, renderer checks, governed-API tests, Evidence Drawer tests, Focus Mode tests, source-role checks, context-join checks, watcher checks, proof checks, pipeline dry-runs, schema checks, and policy checks.
- Tests and validators: NOT RUN.

# Habitat land-cover uncertainty fixtures

`fixtures/domains/habitat/land_cover/uncertainty/`

Status: draft / fixture lane / `UncertaintySurface` examples.

This directory is for small synthetic Habitat land-cover uncertainty fixture examples. These fixtures describe toy accuracy, confidence, valid-pixel footprint, nodata, source-vintage gap, crosswalk uncertainty, model-output uncertainty, geometry-quality, resolution-quality, and public-generalization caveat cases tied to toy land-cover observations or derived products.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, source descriptors, policy decisions, review approvals, release state, public API material, public map material, public tiles, Habitat truth, or published artifacts.

## Contract posture

The land-cover `UncertaintySurface` contract defines uncertainty as the object that carries per-observation accuracy, valid-pixel footprint, source-vintage gap, crosswalk uncertainty, raster or geometry quality, and confidence caveats alongside a governed `LandCoverObservation`.

The contract says the paired schema exists, but is still a proposed scaffold with empty properties and permissive additional properties. Field-level schema shape, fixtures, validators, source registry records, policy files, release artifacts, API behavior, UI behavior, and CI/test coverage remain `NEEDS VERIFICATION`.

This fixture lane can support future checks, but fixture examples do not prove schema enforcement, uncertainty authority, processed-output maturity, policy approval, or release readiness by themselves.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The Habitat land-cover sublane identifies `UncertaintySurface` as part of the land-cover slice when uncertainty is a property of the land-cover artifact itself. The root fixture README says fixture corpora are not canonical truth and RAW, WORK, and QUARANTINE data do not belong here.

## Relationship to adjacent lanes

| Adjacent lane | Relationship |
|---|---|
| `../observation/` | Uncertainty fixtures should attach to toy observation fixtures when observation quality is being checked. |
| `../class_scheme/` | Class accuracy and label uncertainty may depend on toy class-scheme fixtures. |
| `../crosswalk/` | Crosswalk ambiguity examples may reference toy crosswalk fixtures. |
| `../change_summary/` | Change-summary fixtures may carry toy source-vintage, footprint, and crosswalk uncertainty. |
| `../model_run/` | Modeled uncertainty fixtures may cite toy model-run fixtures. |
| `../layer_manifest/` | Layer-manifest fixtures may describe public-facing derivatives of uncertainty fixtures. |
| `../../golden/` | Stable expected outputs for uncertainty inputs may be paired there. |
| `../../invalid/` | Negative-path uncertainty inputs may be paired there when useful. |
| `../../../../../contracts/domains/habitat/land_cover/uncertainty.md` | Semantic meaning; this lane supplies examples only. |
| `../../../../../data/processed/habitat/land_cover/uncertainty/` | Processed lifecycle lane; fixtures do not create processed data authority. |
| `../../../../../release/manifests/habitat/` | Release home; fixtures do not approve publication. |

## Related references

- `../observation/README.md`
- `../class_scheme/README.md`
- `../crosswalk/README.md`
- `../change_summary/README.md`
- `../model_run/README.md`
- `../layer_manifest/README.md`
- `../../golden/README.md`
- `../../invalid/README.md`
- `../../../../../docs/domains/habitat/sublanes/land_cover.md`
- `../../../../../contracts/domains/habitat/land_cover/uncertainty.md`
- `../../../../../contracts/domains/habitat/land_cover/observation.md`
- `../../../../../contracts/domains/habitat/land_cover/class_scheme.md`
- `../../../../../contracts/domains/habitat/land_cover/crosswalk.md`
- `../../../../../contracts/domains/habitat/land_cover/change_summary.md`
- `../../../../../contracts/domains/habitat/land_cover/model_run_receipt.md`
- `../../../../../contracts/domains/habitat/uncertainty_surface.md`
- `../../../../../schemas/contracts/v1/domains/habitat/land_cover/`
- `../../../../../data/processed/habitat/land_cover/uncertainty/README.md`
- `../../../../../pipelines/domains/habitat/land_cover/`
- `../../../../../pipeline_specs/habitat/land_cover/`
- `../../../../../release/manifests/habitat/`
- `../../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.invalid.json`, `*.expected.json`, `*.json`, `*.geojson`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy uncertainty IDs, observation refs, source IDs, class-scheme refs, crosswalk refs, model-run refs, artifact refs, footprint refs, mask refs, metric refs, and digests;
- toy accuracy, confidence, valid-pixel footprint, nodata mask, source-vintage gap, crosswalk ambiguity, model uncertainty, geometry quality, resolution quality, and public-generalization caveat examples;
- toy evidence-ref, validation-ref, policy-ref, review-ref, release-ref, correction-ref, and rollback-ref examples;
- paired expected outputs in `../../golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for real records, source exports, lifecycle data, EvidenceBundles, processed uncertainty artifacts, actual source descriptors, proof packs, release manifests, implementation code, public API material, public map material, public tiles, observation truth, class-scheme authority, model proof, release authority, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, and reviewable.
- Use toy IDs, toy version labels, toy observation refs, toy footprint refs, toy metric refs, toy evidence refs, toy timestamps, and toy hashes.
- Make uncertainty posture explicit: accuracy, confidence, valid-pixel footprint, nodata mask, source-vintage gap, crosswalk uncertainty, model uncertainty, geometry quality, resolution quality, public generalization, candidate, invalid, or expected output.
- Keep uncertainty identity, observation attachment, source role, source vintage, class scheme, crosswalk state, model receipt state, spatial support, temporal support, evidence state, validation state, policy state, review state, release state, correction state, rollback state, and expected outcome explicit where material.
- Pair each input with an expected output when practical.
- Keep schema validity, semantic validity, observation attachment, footprint support, nodata handling, accuracy support, evidence support, model-vs-observation labeling, release posture, correction posture, and rollback posture separate.
- Do not treat fixture success as evidence closure, source authority, schema authority, uncertainty proof, implementation proof, release state, public-map authority, tile authority, or published output.

## Expected uncertainty fixture examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Synthetic uncertainty object attached to a toy observation with toy footprint and confidence refs | Valid input | Demonstrates uncertainty structure without becoming observation truth. |
| Missing observation reference | Validation failure | Uncertainty must attach to an observation or declared derived product. |
| Missing uncertainty kind | Validation failure | Confidence, footprint, or quality type must be explicit. |
| Valid-pixel footprint confused with nodata policy | Validation failure or review-required output | Footprint and nodata are related but distinct. |
| Modeled uncertainty presented as observed accuracy | `ABSTAIN` or validation failure | Model-vs-observation labeling must travel with outputs. |
| Uncertainty used as release approval | Validation failure | Release authority remains separate. |
| Public layer example without uncertainty caveat | Review-required output | Required caveats must remain visible. |

## Maintenance notes

- Update this README when payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each fixture to the contract review, schema check, observation-attachment check, footprint check, nodata check, accuracy check, source-vintage check, crosswalk-uncertainty check, model-vs-observation check, governed-API test, Evidence Drawer test, Focus Mode test, renderer check, release-readiness check, correction check, rollback check, or pipeline dry-run that consumes it.
- If a fixture becomes stable enough to anchor a regression check, pair it with an expected output and document the consumer.
- Keep payloads small enough for normal code review.

## Verification status

- Target README: replaced one-character placeholder content.
- Fixture payload inventory: no payload files verified in this directory during this update.
- UncertaintySurface contract alignment: PARTIALLY VERIFIED against `contracts/domains/habitat/land_cover/uncertainty.md`.
- Processed uncertainty lane alignment: PARTIALLY VERIFIED against `data/processed/habitat/land_cover/uncertainty/README.md`.
- Land-cover sublane alignment: PARTIALLY VERIFIED against `docs/domains/habitat/sublanes/land_cover.md`.
- Schema alignment: NEEDS VERIFICATION because the contract reports the paired schema is still a permissive scaffold.
- Sibling fixture alignment: PARTIALLY VERIFIED against populated `observation/`, `class_scheme/`, `crosswalk/`, `change_summary/`, `model_run/`, and `layer_manifest/` READMEs.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, uncertainty checks, observation checks, source-role checks, source-vintage checks, valid-pixel checks, renderer checks, governed-API tests, Evidence Drawer tests, Focus Mode tests, pipeline dry-runs, schema checks, and policy checks.
- Tests and validators: NOT RUN.

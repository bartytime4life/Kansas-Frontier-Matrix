# Habitat land-cover observation fixtures

`fixtures/domains/habitat/land_cover/observation/`

Status: draft / fixture lane / `LandCoverObservation` examples.

This directory is for small synthetic Habitat land-cover observation fixture examples. These fixtures describe toy land-cover classifications over a declared spatial and temporal scope with source role, class scheme, source vintage, CRS/resolution, valid-pixel support, evidence refs, policy posture, correction posture, and rollback posture.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, source descriptors, policy decisions, review approvals, release state, public API material, public map material, public tiles, Habitat truth, or published artifacts.

## Contract posture

The `LandCoverObservation` contract defines an observation as a governed categorical or continuous land-cover classification over a declared spatial and temporal scope. It is source-role-aware and must keep class scheme, source vintage, valid-pixel support, evidence refs, policy posture, correction, and rollback explicit.

The contract says the paired schema exists, but is still a proposed scaffold with empty properties and permissive additional properties. Field-level schema shape, fixtures, validators, source registry records, policy files, release artifacts, API behavior, UI behavior, and CI/test coverage remain `NEEDS VERIFICATION`.

This fixture lane can support future checks, but fixture examples do not prove schema enforcement, source activation, observation authority, pipeline implementation, policy approval, or release readiness by themselves.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The Habitat land-cover sublane lists `fixtures/domains/habitat/land_cover/` as the proposed fixture home for land-cover examples. The root fixture README says fixture corpora are not canonical truth and RAW, WORK, and QUARANTINE data do not belong here.

## Relationship to adjacent lanes

| Adjacent lane | Relationship |
|---|---|
| `../class_scheme/` | Observation fixtures must reference toy class-scheme fixtures where class vocabulary matters. |
| `../crosswalk/` | Observation fixtures may reference toy crosswalks when harmonized values are being checked. |
| `../change_summary/` | Change-summary fixtures compare observation fixtures; they do not replace observations. |
| `../model_run/` | Model-run fixtures may consume or emit toy observation-like candidates but must preserve model-vs-observation labels. |
| `../layer_manifest/` | Layer-manifest fixtures may describe public-facing derivatives of observation fixtures. |
| `../../golden/` | Stable expected outputs for observation inputs may be paired there. |
| `../../invalid/` | Negative-path observation inputs may be paired there when useful. |
| `../../../../../contracts/domains/habitat/land_cover/observation.md` | Semantic meaning; this lane supplies examples only. |
| `../../../../../pipelines/domains/habitat/land_cover/` | Executable processing home; this lane is not pipeline code. |
| `../../../../../release/manifests/habitat/` | Release home; fixtures do not approve publication. |

## Related references

- `../class_scheme/README.md`
- `../crosswalk/README.md`
- `../change_summary/README.md`
- `../model_run/README.md`
- `../layer_manifest/README.md`
- `../../golden/README.md`
- `../../invalid/README.md`
- `../../../../../docs/domains/habitat/sublanes/land_cover.md`
- `../../../../../contracts/domains/habitat/land_cover/observation.md`
- `../../../../../contracts/domains/habitat/land_cover/class_scheme.md`
- `../../../../../contracts/domains/habitat/land_cover/crosswalk.md`
- `../../../../../contracts/domains/habitat/land_cover/change_summary.md`
- `../../../../../contracts/domains/habitat/land_cover/model_run_receipt.md`
- `../../../../../contracts/domains/habitat/land_cover/uncertainty.md`
- `../../../../../schemas/contracts/v1/domains/habitat/land_cover/`
- `../../../../../pipelines/domains/habitat/land_cover/`
- `../../../../../pipeline_specs/habitat/land_cover/`
- `../../../../../data/registry/sources/habitat/`
- `../../../../../release/manifests/habitat/`
- `../../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.invalid.json`, `*.expected.json`, `*.json`, `*.geojson`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy observation IDs, source IDs, source vintages, source roles, class-scheme refs, raster/vector refs, spatial scope refs, CRS/resolution refs, valid-pixel refs, and artifact digests;
- toy categorical, continuous, fractional, wetland-class, vegetation-type, source-native, modeled, aggregate, candidate, or invalid observation examples;
- toy evidence-ref, validation-ref, policy-ref, review-ref, release-ref, correction-ref, and rollback-ref examples;
- paired expected outputs in `../../golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for real records, source exports, lifecycle data, EvidenceBundles, actual source descriptors, proof packs, release manifests, implementation code, public API material, public map material, public tiles, source authority, class-scheme authority, crosswalk authority, change-summary truth, model proof, release authority, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, and reviewable.
- Use toy IDs, toy version labels, toy class refs, toy spatial refs, toy evidence refs, toy timestamps, and toy hashes.
- Make observation posture explicit: categorical, continuous, fractional, wetland-class, vegetation-type, source-native, modeled, aggregate, candidate, invalid, or expected output.
- Keep observation identity, source identity, source role, source vintage, class scheme, spatial scope, temporal scope, valid-pixel support, uncertainty posture, evidence state, validation state, policy state, review state, release state, correction state, rollback state, and expected outcome explicit where material.
- Pair each input with an expected output when practical.
- Keep schema validity, semantic validity, class-scheme binding, source-role validity, source-vintage validity, valid-pixel support, evidence support, model-vs-observation labeling, release posture, correction posture, and rollback posture separate.
- Do not treat fixture success as evidence closure, source authority, schema authority, observation proof, implementation proof, release state, public-map authority, tile authority, or published output.

## Expected observation fixture examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Synthetic observation with toy source, class scheme, spatial scope, temporal scope, and evidence refs | Valid input | Demonstrates observation structure without becoming source truth. |
| Missing source ID or source role | Validation failure | Source identity and role must be explicit. |
| Missing class-scheme reference | Validation failure | Observations must bind to a known scheme. |
| Missing spatial or temporal scope | Validation failure | Scope must be declared. |
| Missing valid-pixel support for raster-like input | Review-required output | Valid data coverage must be inspectable. |
| Observation used as class scheme or crosswalk | Validation failure | Scheme and mapping objects stay separate. |
| Modeled output presented as observed input | `ABSTAIN` or validation failure | Model-vs-observation labeling must travel with outputs. |
| Observation treated as release approval | Validation failure | Release authority remains separate. |

## Maintenance notes

- Update this README when payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each fixture to the contract review, schema check, class-scheme check, source-role check, source-vintage check, valid-pixel check, model-vs-observation check, governed-API test, Evidence Drawer test, Focus Mode test, renderer check, release-readiness check, correction check, rollback check, or pipeline dry-run that consumes it.
- If a fixture becomes stable enough to anchor a regression check, pair it with an expected output and document the consumer.
- Keep payloads small enough for normal code review.

## Verification status

- Target README: replaced one-character placeholder content.
- Fixture payload inventory: no payload files verified in this directory during this update.
- LandCoverObservation contract alignment: PARTIALLY VERIFIED against `contracts/domains/habitat/land_cover/observation.md`.
- Land-cover sublane alignment: PARTIALLY VERIFIED against `docs/domains/habitat/sublanes/land_cover.md`.
- Schema alignment: NEEDS VERIFICATION because the contract reports the paired schema is still a permissive scaffold.
- Sibling fixture alignment: PARTIALLY VERIFIED against populated `class_scheme/`, `crosswalk/`, `change_summary/`, `model_run/`, and `layer_manifest/` READMEs.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, observation checks, source-role checks, source-vintage checks, valid-pixel checks, renderer checks, governed-API tests, Evidence Drawer tests, Focus Mode tests, pipeline dry-runs, schema checks, and policy checks.
- Tests and validators: NOT RUN.

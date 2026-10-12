# Habitat land-cover model-run fixtures

`fixtures/domains/habitat/land_cover/model_run/`

Status: draft / fixture lane / model-run and receipt examples.

This directory is for small synthetic Habitat land-cover model-run fixture examples. These fixtures describe toy run metadata, input digests, config digests, model or transform identity, output inventory, validation posture, uncertainty notes, receipt pointers, and bounded model-vs-observation checks for land-cover-derived work.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, source descriptors, policy decisions, review approvals, release state, public API material, public map material, public tiles, Habitat truth, or published artifacts.

## Contract posture

The land-cover `ModelRunReceipt` contract defines a receipt as process memory for a modeled, derived, reclassified, generalized, vectorized, summarized, or otherwise transformed run. It records what a run did without turning that run into source truth, proof, publication authority, or an observed land-cover product.

The contract reports that the expected paired schema path was not found during inspection, so field-level schema shape, fixtures, validators, tests, and CI coverage remain `NEEDS VERIFICATION`.

This fixture lane can support those future checks, but fixture examples do not prove schema enforcement, pipeline implementation, model correctness, proof closure, policy approval, or release readiness by themselves.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The Habitat land-cover sublane identifies `Model Run Receipt` as part of the land-cover slice when it runs a land-cover-derived model, while other Habitat and adjacent-domain claims remain outside this sublane. The root fixture README says fixture corpora are not canonical truth and RAW, WORK, and QUARANTINE data do not belong here.

## Relationship to adjacent lanes

| Adjacent lane | Relationship |
|---|---|
| `../class_scheme/` | Model-run fixtures may reference toy class schemes as inputs. |
| `../crosswalk/` | Model-run fixtures may reference toy crosswalks when a run uses reviewed recoding. |
| `../change_summary/` | Model-run fixtures may produce toy change-summary candidates. |
| `../layer_manifest/` | Model-run fixtures may produce toy artifact refs later described by layer-manifest fixtures. |
| `../../golden/` | Stable expected outputs for model-run inputs may be paired there. |
| `../../invalid/` | Negative-path model-run inputs may be paired there when useful. |
| `../../../../../contracts/domains/habitat/land_cover/model_run_receipt.md` | Semantic meaning; this lane supplies examples only. |
| `../../../../../pipelines/domains/habitat/land_cover/` | Executable processing home; this lane is not pipeline code. |
| `../../../../../data/receipts/habitat/land_cover/` | Receipt data home; fixtures do not create receipt authority. |
| `../../../../../release/manifests/habitat/` | Release home; fixtures do not approve publication. |

## Related references

- `../class_scheme/README.md`
- `../crosswalk/README.md`
- `../change_summary/README.md`
- `../layer_manifest/README.md`
- `../../golden/README.md`
- `../../invalid/README.md`
- `../../../../../docs/domains/habitat/sublanes/land_cover.md`
- `../../../../../docs/domains/habitat/MODEL_VS_OBSERVATION.md`
- `../../../../../contracts/domains/habitat/land_cover/model_run_receipt.md`
- `../../../../../contracts/domains/habitat/land_cover/observation.md`
- `../../../../../contracts/domains/habitat/land_cover/class_scheme.md`
- `../../../../../contracts/domains/habitat/land_cover/crosswalk.md`
- `../../../../../contracts/domains/habitat/land_cover/change_summary.md`
- `../../../../../contracts/domains/habitat/land_cover/uncertainty.md`
- `../../../../../contracts/domains/habitat/uncertainty_surface.md`
- `../../../../../pipelines/domains/habitat/land_cover/`
- `../../../../../pipeline_specs/habitat/land_cover/`
- `../../../../../data/receipts/habitat/land_cover/`
- `../../../../../release/manifests/habitat/`
- `../../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.invalid.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy run IDs, model IDs, model versions, tool digests, input digests, config digests, output refs, output digests, and run timestamps;
- toy reclassification, generalization, vectorization, summarization, valid-pixel, uncertainty, change-detection, and redaction run examples;
- toy source-role, evidence-ref, validation-ref, policy-ref, review-ref, release-ref, correction-ref, and rollback-ref examples;
- toy model-vs-observation, receipt-vs-proof, receipt-vs-release, and run-output boundary checks;
- paired expected outputs in `../../golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for real records, source exports, lifecycle data, EvidenceBundles, actual run receipts, proof packs, release manifests, implementation code, public API material, public map material, public tiles, source authority, observation truth, model proof, release authority, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, and reviewable.
- Use toy IDs, toy version labels, toy input refs, toy config refs, toy output refs, toy evidence refs, toy timestamps, and toy hashes.
- Make run posture explicit: reclassification, generalization, vectorization, model inference, uncertainty generation, valid-pixel footprint, change detection, redaction, candidate, invalid, or expected output.
- Keep model identity, input closure, configuration closure, output inventory, source role, evidence state, validation state, policy state, review state, release state, correction state, rollback state, and expected outcome explicit where material.
- Pair each input with an expected output when practical.
- Keep schema validity, semantic validity, receipt completeness, input closure, config closure, output digesting, evidence support, model-vs-observation labeling, release posture, correction posture, and rollback posture separate.
- Do not treat fixture success as evidence closure, source authority, schema authority, model proof, implementation proof, release state, public-map authority, tile authority, or published output.

## Expected model-run fixture examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Synthetic model run with toy inputs, config digest, and output refs | Valid input | Demonstrates process memory without becoming proof. |
| Missing input digest | Validation failure | Input closure must be explicit. |
| Missing config digest | Validation failure | Reproducibility requires config closure. |
| Modeled output presented as observed product | `ABSTAIN` or validation failure | Model-vs-observation labeling must travel with outputs. |
| Receipt treated as EvidenceBundle | Validation failure | Receipts are not proof objects. |
| Receipt treated as release approval | Validation failure | Release authority remains separate. |
| Output artifact missing correction or rollback posture | Review-required output | Public-use posture must be inspectable. |

## Maintenance notes

- Update this README when payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each fixture to the contract review, schema check, receipt-completeness check, input-closure check, config-closure check, model-vs-observation check, uncertainty check, governed-API test, Evidence Drawer test, Focus Mode test, renderer check, release-readiness check, correction check, rollback check, or pipeline dry-run that consumes it.
- If a fixture becomes stable enough to anchor a regression check, pair it with an expected output and document the consumer.
- Keep payloads small enough for normal code review.

## Verification status

- Target README: populated from empty placeholder content.
- Fixture payload inventory: no payload files verified in this directory during this update.
- ModelRunReceipt contract alignment: PARTIALLY VERIFIED against `contracts/domains/habitat/land_cover/model_run_receipt.md`.
- Land-cover sublane alignment: PARTIALLY VERIFIED against `docs/domains/habitat/sublanes/land_cover.md`.
- Schema alignment: NEEDS VERIFICATION because the contract reports the expected paired schema was not found.
- Layer-manifest sibling alignment: PARTIALLY VERIFIED against `fixtures/domains/habitat/land_cover/layer_manifest/README.md`.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, receipt checks, model-vs-observation checks, uncertainty checks, renderer checks, governed-API tests, Evidence Drawer tests, Focus Mode tests, pipeline dry-runs, schema checks, and policy checks.
- Tests and validators: NOT RUN.

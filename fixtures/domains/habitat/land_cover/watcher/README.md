# Habitat land-cover watcher fixtures

`fixtures/domains/habitat/land_cover/watcher/`

Status: draft / fixture lane / watcher and source-drift examples.

This directory is for small synthetic Habitat land-cover watcher fixture examples. These fixtures describe toy source-head checks, source-drift detections, class-histogram changes, materiality thresholds, checkpoint records, proposed-work records, and no-op outcomes for land-cover watcher behavior.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, source descriptors, policy decisions, review approvals, release state, public API material, public map material, public tiles, Habitat truth, or published artifacts.

## Watcher posture

The Habitat land-cover sublane states that watchers observe and record; watchers do not publish. A land-cover watcher may emit a `PROPOSED_WORK_RECORD` and write a `<key>.last.ok` checkpoint containing a `spec_hash`, but it does not move artifacts into published lanes and is consumed by review, not by public UI.

The same doctrine separates source activation from watcher activity: sources, connectors, and watchers remain inactive until source descriptors, source roles, rights posture, fixtures, validators, and activation decisions are in place.

This fixture lane can support future watcher checks, but fixture examples do not prove source activation, connector behavior, watcher execution, policy approval, review completion, or release readiness by themselves.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The Habitat land-cover sublane lists `fixtures/domains/habitat/land_cover/` as the proposed fixture home for land-cover examples. The root fixture README says fixture corpora are not canonical truth and RAW, WORK, and QUARANTINE data do not belong here.

## Relationship to adjacent lanes

| Adjacent lane | Relationship |
|---|---|
| `../observation/` | Watcher fixtures may propose work that later creates or updates toy observation candidates. |
| `../change_summary/` | Watcher fixtures may produce toy histogram or change-summary proposed-work records. |
| `../model_run/` | Watcher fixtures may trigger toy model-run candidates, but run receipts remain separate. |
| `../uncertainty/` | Watcher fixtures may flag uncertainty or footprint changes for review. |
| `../layer_manifest/` | Watcher fixtures may flag stale layer metadata but do not update manifests directly. |
| `../../golden/` | Stable expected outputs for watcher inputs may be paired there. |
| `../../invalid/` | Negative-path watcher inputs may be paired there when useful. |
| `../../../../../docs/domains/habitat/sublanes/land_cover.md` | Watcher doctrine and thresholds; this lane supplies examples only. |
| `../../../../../pipelines/domains/habitat/land_cover/` | Executable processing home; this lane is not pipeline code. |
| `../../../../../pipeline_specs/habitat/land_cover/` | Declarative run/spec home; this lane is not a pipeline spec. |
| `../../../../../release/manifests/habitat/` | Release home; fixtures do not approve publication. |

## Related references

- `../observation/README.md`
- `../change_summary/README.md`
- `../model_run/README.md`
- `../uncertainty/README.md`
- `../layer_manifest/README.md`
- `../class_scheme/README.md`
- `../crosswalk/README.md`
- `../../golden/README.md`
- `../../invalid/README.md`
- `../../../../../docs/domains/habitat/sublanes/land_cover.md`
- `../../../../../contracts/domains/habitat/land_cover/observation.md`
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

- small synthetic `*.input.json`, `*.valid.json`, `*.invalid.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy source heads, source versions, source vintages, ETags, digests, timestamps, checkpoint records, and no-op records;
- toy class-histogram, threshold, materiality, stale-source, source-drift, changed-source, unchanged-source, and proposed-work examples;
- toy `PROPOSED_WORK_RECORD`, `<key>.last.ok`, review-queue, PR-emitter, hold, deny, and no-op expected outputs;
- toy evidence-ref, validation-ref, policy-ref, review-ref, correction-ref, rollback-ref, and release-blocker examples;
- paired expected outputs in `../../golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for real records, source exports, lifecycle data, EvidenceBundles, actual watcher receipts, actual source descriptors, proof packs, release manifests, implementation code, public API material, public map material, public tiles, source authority, observation truth, model proof, release authority, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, and reviewable.
- Use toy source IDs, toy source heads, toy checkpoint keys, toy digests, toy threshold profiles, toy proposed-work IDs, toy timestamps, and toy hashes.
- Make watcher posture explicit: source unchanged, source changed, material threshold met, below threshold, stale source, activation missing, validator failed, review required, no-op, denied, invalid, or expected output.
- Keep source identity, source role, source activation state, rights state, watcher cadence, checkpoint state, materiality threshold, evidence state, validation state, policy state, review state, release-blocker state, correction state, rollback state, and expected outcome explicit where material.
- Pair each input with an expected output when practical.
- Keep schema validity, semantic validity, source activation, source-role validity, source-head comparison, materiality thresholding, checkpoint writing, proposed-work emission, review gating, release posture, correction posture, and rollback posture separate.
- Do not treat fixture success as evidence closure, source authority, schema authority, watcher proof, implementation proof, release state, public-map authority, tile authority, or published output.

## Expected watcher fixture examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Synthetic source-head unchanged with matching checkpoint | no-op output | Watcher records no work. |
| Synthetic source-head changed and threshold exceeded | `PROPOSED_WORK_RECORD` output | Review is required before promotion. |
| Synthetic source-head changed but below threshold | no-op or review-optional output | Materiality remains explicit. |
| Missing source activation | hold output | Watcher does not run as an authority without activation. |
| Missing source role or rights posture | hold or validation failure | Admission gates must remain visible. |
| Watcher output treated as publication | validation failure | Watchers observe and record; they do not publish. |
| Public UI attempts to consume proposed work | `DENY` or validation failure | Proposed work is not a public surface. |

## Maintenance notes

- Update this README when payload files, validators, tests, helper scripts, expected-output names, watcher contracts, or consumer contracts are added.
- Link each fixture to the watcher check, source-head check, no-op check, threshold check, proposed-work check, review-gate check, source-role check, source-activation check, governed-API test, Evidence Drawer test, Focus Mode test, release-readiness check, correction check, rollback check, or pipeline dry-run that consumes it.
- If a fixture becomes stable enough to anchor a regression check, pair it with an expected output and document the consumer.
- Keep payloads small enough for normal code review.

## Verification status

- Target README: replaced one-character placeholder content.
- Fixture payload inventory: no payload files verified in this directory during this update.
- Watcher doctrine alignment: PARTIALLY VERIFIED against `docs/domains/habitat/sublanes/land_cover.md`.
- Source-activation alignment: PARTIALLY VERIFIED against `docs/domains/habitat/sublanes/land_cover.md`.
- Sibling fixture alignment: PARTIALLY VERIFIED against populated `observation/`, `change_summary/`, `model_run/`, `uncertainty/`, and `layer_manifest/` READMEs.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, watcher checks, source-head checks, threshold checks, source-activation checks, review-gate checks, governed-API tests, Evidence Drawer tests, Focus Mode tests, pipeline dry-runs, schema checks, and policy checks.
- Tests and validators: NOT RUN.

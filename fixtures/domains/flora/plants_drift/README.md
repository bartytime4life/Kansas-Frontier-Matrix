# Flora plants-drift fixtures

`fixtures/domains/flora/plants_drift/`

Status: draft / fixture lane / watcher dry-run support.

This directory is for small synthetic Flora plants-drift fixture examples used by watcher dry-runs, taxonomy drift checks, source metadata drift checks, material-change classification, governed API examples, Evidence Drawer examples, Focus Mode examples, and documentation dry-runs. These fixtures may represent toy source-version changes, taxonomy-name changes, source descriptor mismatches, checksum changes, freshness changes, or no-op watcher runs, but they are not live watcher outputs and must not be treated as source truth, catalog truth, release proof, or publication state.

These files are examples only. They are not source records, EvidenceBundles, source descriptors, watcher run receipts, policy decisions, review approvals, release state, public API material, public map material, public tiles, or published artifacts.

## Watcher and spec posture

Repository evidence shows placeholder plants-drift watcher specs at `pipeline_specs/flora/plants_drift_watcher.yaml` and `pipeline_specs/watchers/plants_drift.yaml`; both are `PROPOSED` placeholders created from the Flora docs inventory. The plants watcher README describes `pipelines/watchers/plants/` as a watcher lane for plant-related source-change detection and states that watcher outputs are candidate evidence-development artifacts only: watchers do not publish.

This fixture README supports dry-run examples and expected outputs only. It does not activate a watcher, prove executable code exists, define source activation, approve credentials, schedule network checks, or create release authority.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic fixture examples, not executable watcher code, source registry records, lifecycle data, policy rules, schemas, contracts, release decisions, or published outputs.

The root fixture README states that fixtures are operational/runtime examples, not canonical truth, and that RAW, WORK, or QUARANTINE data does not belong here.

## Related references

- `../README.md`
- `../../README.md`
- `../plant_taxon/README.md`
- `../evidence_bundles/README.md`
- `../golden/README.md`
- `../invalid/README.md`
- `../../../../pipelines/watchers/plants/README.md`
- `../../../../pipeline_specs/flora/plants_drift_watcher.yaml`
- `../../../../pipeline_specs/watchers/plants_drift.yaml`
- `../../../../docs/domains/flora/FILE_SYSTEM_PLAN.md`
- `../../../../docs/domains/flora/DATA_LIFECYCLE.md`
- `../../../../docs/domains/flora/CROSSWALKS.md`
- `../../../../contracts/domains/flora/plant_taxon.md`
- `../../../../contracts/domains/flora/flora_taxon_crosswalk.md`
- `../../../../data/registry/sources/flora/`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, or `*.md` examples;
- no-op drift examples where a source check detects no material change;
- material-change examples for toy taxonomy-name, source-version, source-metadata, checksum, ETag, class-list, crosswalk, or freshness changes;
- examples that distinguish source time, retrieval time, release time, correction time, and stale state;
- examples that prove drift detection remains separate from evidence closure, review, and release;
- expected watcher dry-run shapes such as `NoOpReceipt`, `MaterialChangeReport`, `ProposedWorkRecord`, `ValidationReport`, `PolicyDecision`, `QuarantineReceipt`, or `RunReceipt` when represented synthetically;
- paired expected outputs in `../golden/` when behavior becomes a stable regression anchor.

## Exclusions

Do not use this lane for real source payloads, live upstream responses, credentials, executable watcher code, source registry records, lifecycle outputs, release artifacts, proof packs, policy rules, public API payloads, public map data, public tiles, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, and reviewable.
- Make the drift scenario explicit in the file name, fixture metadata, or paired expected output.
- Prefer one material-change reason per fixture unless a test intentionally checks precedence.
- Preserve watcher non-publication: fixture examples may describe candidate outcomes, but they must not imply direct publication.
- Keep source identity, source role, source version, retrieval time, materiality reason, evidence state, review state, release state, and expected outcome explicit where material.
- Pair each input with an expected output when practical.
- Do not treat plants-drift fixtures as source authority, evidence, approval, release state, watcher proof, implementation proof, or published output.

## Expected fixture examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Source metadata unchanged | `NoOpReceipt` | Records that a check ran without material change. |
| Toy taxonomy label changes | `MaterialChangeReport` | Requires review before downstream use. |
| Source role mismatch in drift candidate | `ABSTAIN` or quarantine-style outcome | Source-role anti-collapse remains visible. |
| Missing source identity or source version | Quarantine-style outcome | Candidate cannot proceed without stable identity. |
| Freshness threshold exceeded | `SOURCE_STALE` or review-required outcome | Freshness state remains distinct from observation time. |
| Evidence support missing for consequential claim | `ABSTAIN` | Drift detection does not become claim support. |
| Candidate asks for direct publication | Validation failure or deny outcome | Watcher fixtures must preserve no-publish behavior. |

## Verification status

- Target README: populated from empty placeholder content.
- Fixture payload inventory: no payloads verified in this directory during this update.
- Watcher spec alignment: PARTIALLY VERIFIED against the two PROPOSED plants-drift watcher spec placeholders.
- Watcher doctrine alignment: PARTIALLY VERIFIED against `pipelines/watchers/plants/README.md` and the Flora file-system plan watcher section.
- Consumer alignment: NEEDS VERIFICATION against watcher dry-runs, validators, governed-API tests, Evidence Drawer tests, Focus Mode tests, and policy checks.
- Tests and validators: NOT RUN.

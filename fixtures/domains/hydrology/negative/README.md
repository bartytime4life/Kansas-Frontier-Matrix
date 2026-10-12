# Hydrology negative fixtures

`fixtures/domains/hydrology/negative/`

Status: draft / negative fixture lane / Hydrology fail-closed scenario staging.

This directory is for small synthetic Hydrology negative-path fixture examples that are being drafted, grouped, or staged before they are promoted into a more specific invalid fixture lane. Use this lane for negative cases that should not produce a normal public `ANSWER`, but whose exact consumer, defect family, expected envelope, or child-lane placement is still being worked out.

These files are examples only. They are not source records, lifecycle data, actual EvidenceBundles, source descriptors, proof packs, policy decisions, review approvals, release state, public API material, public map material, public tiles, Hydrology truth, source authority, policy authority, release authority, AI authority, or published artifacts.

## Negative fixture posture

The populated `../invalid/` lane is the more specific fail-closed index for known Hydrology invalid fixture families. It currently points to decision-envelope invalid cases and EvidenceBundle invalid cases, with stable expected outputs routed to `../golden/`.

Use this `negative/` lane when a negative Hydrology case is useful but not yet sorted into a stable invalid child lane. Once the defect family and expected outcome stabilize, move or cross-link the case into `../invalid/`, `../decision_envelope/invalid/`, `../evidence_bundle/invalid/`, another specific invalid child lane, or `../golden/` for stable expected outputs.

This lane can support future validation and UI checks, but examples here do not prove validator implementation, governed API behavior, UI behavior, policy enforcement, release integration, schema enforcement, or CI coverage by themselves.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The root fixture README says `fixtures/` is for runtime fixture inputs and separates it from `tests/fixtures/`, `artifacts/`, and `data/`. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here. The parent Hydrology fixture README was not inspected during this update.

## Relationship to adjacent lanes

| Adjacent lane | Relationship |
|---|---|
| `../invalid/` | More specific fail-closed index for known invalid Hydrology fixture families. |
| `../golden/` | Stable expected outputs for negative and invalid inputs should be paired there. |
| `../decision_envelope/` | Negative runtime-envelope examples may be staged here before becoming invalid decision-envelope cases. |
| `../decision_envelope/invalid/` | Stable invalid decision-envelope examples belong there. |
| `../evidence_bundle/` | Negative evidence-support examples may be staged here before becoming invalid EvidenceBundle cases. |
| `../evidence_bundle/invalid/` | Stable invalid EvidenceBundle examples belong there. |
| `../README.md` | Parent Hydrology fixture lane; not inspected during this update. |

## When to use `negative/` vs `invalid/`

| Use case | Preferred lane | Reason |
|---|---|---|
| The defect family and expected failure are known | `../invalid/` or a specific invalid child lane | Specific invalid lanes are easier to validate and pair with golden outputs. |
| The case is exploratory or not yet categorized | `./` | This lane can stage the scenario without creating a premature child taxonomy. |
| The example is a malformed decision envelope with stable expected output | `../decision_envelope/invalid/` plus `../golden/` | Stable runtime-envelope cases should live in the precise lane. |
| The example is an invalid EvidenceBundle with stable expected output | `../evidence_bundle/invalid/` plus `../golden/` | Stable evidence-support cases should live in the precise lane. |
| The example is a broad negative scenario sketch | `./` | Narrative or design-stage examples can live here until narrowed. |
| The example accidentally contains real source material | Neither | Move it out of fixtures and route through the governed lifecycle/quarantine path. |

## Current known invalid families

These families are currently indexed under `../invalid/` rather than here:

- malformed or unsupported Hydrology runtime envelopes;
- insufficient or unresolved evidence support;
- citation-validation failure;
- missing required EvidenceBundle fields;
- source-role or regulatory-context boundary collapse;
- direct request for internal lifecycle material;
- missing release, rights, sensitivity, correction, or rollback support;
- stable fail-closed outputs ready for deterministic comparison.

## Related references

- `../invalid/README.md`
- `../golden/README.md`
- `../decision_envelope/README.md`
- `../decision_envelope/valid/README.md`
- `../decision_envelope/invalid/README.md`
- `../evidence_bundle/README.md`
- `../evidence_bundle/valid/README.md`
- `../evidence_bundle/invalid/README.md`
- `../README.md`
- `../../README.md`
- `../../../docs/domains/hydrology/API_CONTRACTS.md`
- `../../../docs/domains/hydrology/BOUNDARY.md`
- `../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md`
- `../../../contracts/domains/hydrology/decision_envelope.md`
- `../../../contracts/domains/hydrology/evidence_bundle.md`
- `../../../contracts/runtime/decision_envelope.md`
- `../../../contracts/evidence/evidence_bundle.md`
- `../../../schemas/contracts/v1/domains/hydrology/`
- `../../../schemas/contracts/v1/runtime/decision_envelope.schema.json`
- `../../../schemas/contracts/v1/evidence/evidence_bundle.schema.json`
- `../../../policy/domains/hydrology/`
- `../../../data/registry/sources/hydrology/`
- `../../../data/proofs/hydrology/`
- `../../../release/candidates/hydrology/`
- `../../../release/manifests/hydrology/`
- `../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.negative.json`, `*.invalid.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- draft negative examples for decision envelopes, EvidenceBundles, drawer outputs, Focus Mode outputs, layer resolver outputs, exports, source-role checks, evidence-resolution checks, citation-validation checks, rights/sensitivity checks, release-readiness checks, correction checks, rollback checks, and trust-membrane checks;
- toy `ABSTAIN`, `DENY`, `ERROR`, validation-failure, review-required, blocked-render, evidence-missing, citation-failed, rights-missing, sensitivity-missing, source-role-conflicted, release-blocked, or expected-output examples;
- design-stage scenario notes that need later sorting into a specific invalid child lane;
- contrast examples showing the difference between a negative input and a valid governed envelope or evidence-support object;
- paired expected outputs in `../golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for real records, source exports, lifecycle data, actual EvidenceBundles, source descriptors, proof packs, release manifests, implementation code, public API material, public map material, public tiles, direct model runtime output, source authority, policy authority, release authority, AI authority, or published artifacts.

## Shared fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Make the negative condition explicit in the file name, payload, expected output, and consumer notes.
- Make expected outcome explicit when known: `ABSTAIN`, `DENY`, `ERROR`, validation failure, review-required, blocked render, release-readiness failure, or expected output.
- Pair each stable negative input with an expected failure output in `../golden/` when practical.
- Move stable negative cases to `../invalid/` or a specific invalid child lane when the defect family becomes clear.
- Keep schema validity, semantic validity, evidence resolution, citation validation, rights posture, sensitivity posture, source-role validity, temporal validity, release posture, trust-membrane safety, drawer display, Focus Mode wording, layer-manifest state, UI behavior, correction posture, and rollback posture separate.
- Do not treat fixture failure as EvidenceBundle closure, policy approval, validator implementation proof, API implementation proof, UI implementation proof, release state, public-map authority, or published output.

## Maintenance notes

- Update this README when new negative child lanes, negative payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each stable negative fixture to the exact invalid lane, check, and consumer that uses it.
- If expected negative behavior stabilizes, update the paired input, expected output, consumer notes, child README, `../invalid/README.md`, `../golden/README.md`, and this index together.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real source material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: replaced blank placeholder content.
- Negative fixture payload inventory: no payload files verified under this parent during this update.
- Invalid lane relationship: PARTIALLY VERIFIED against `fixtures/domains/hydrology/invalid/README.md`.
- Golden fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hydrology/golden/README.md`.
- Decision-envelope fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hydrology/decision_envelope/README.md` and child lanes.
- EvidenceBundle fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hydrology/evidence_bundle/README.md` and child lanes.
- Parent Hydrology fixture README: NEEDS VERIFICATION.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, negative-fixture checks, invalid-fixture checks, golden-file checks, Hydrology governed-API tests, decision-envelope checks, evidence-bundle checks, drawer checks, Focus Mode checks, layer-manifest checks, evidence-resolution checks, citation-validation checks, rights checks, sensitivity checks, source-role checks, trust-membrane checks, release-readiness checks, schema checks, policy checks, renderer checks, and UI implementation.
- Tests and validators: NOT RUN.

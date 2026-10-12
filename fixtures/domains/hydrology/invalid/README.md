# Hydrology invalid fixtures

`fixtures/domains/hydrology/invalid/`

Status: draft / invalid fixture parent index / Hydrology fail-closed examples.

This directory is the parent lane for small synthetic Hydrology invalid fixture examples. Use it to index and stage Hydrology negative-path cases that should fail closed instead of producing a substantive public claim, public map state, public export, drawer projection, Focus Mode answer, layer resolver output, decision envelope, or evidence-support result.

These files are examples only. They are not source records, lifecycle data, actual EvidenceBundles, source descriptors, proof packs, policy decisions, review approvals, release state, public API material, public map material, public tiles, Hydrology truth, source authority, policy authority, release authority, AI authority, or published artifacts.

## Invalid fixture posture

Use this lane for synthetic inputs that should not produce a normal public `ANSWER`. Expected outcomes may include `ABSTAIN`, `DENY`, `ERROR`, validation failure, review-required, blocked render, release-readiness failure, evidence-resolution failure, citation-validation failure, source-role failure, rights/sensitivity failure, or trust-membrane failure.

Invalid fixtures should make the defect explicit and keep expected failure separate from implementation proof. A fixture can describe a desired negative case before validators, governed API routes, UI checks, schema enforcement, release integration, or CI coverage exist.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The root fixture README says `fixtures/` is for runtime fixture inputs and separates it from `tests/fixtures/`, `artifacts/`, and `data/`. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here. The parent Hydrology fixture README was not inspected during this update.

## Current child-lane inventory

The following Hydrology fixture lanes currently carry more specific invalid or fail-closed README coverage. This table is a navigation index, not proof that payload files, validators, tests, governed API routes, UI checks, policy bundles, release manifests, or CI coverage exist.

| Child or sibling lane | Invalid case family | Expected posture |
|---|---|---|
| `../decision_envelope/invalid/` | Invalid Hydrology runtime envelopes and blocked/no-answer outcomes. | `ABSTAIN`, `DENY`, `ERROR`, validation failure, review-required, or blocked render. |
| `../evidence_bundle/invalid/` | Invalid Hydrology EvidenceBundle claim-support cases. | Validation failure, review-required, `ABSTAIN`, `DENY`, `ERROR`, or release-readiness failure. |
| `../golden/` | Expected outputs for stable invalid inputs. | Deterministic expected fail-closed output, once paired with an input fixture. |

Future child lanes under this `invalid/` parent may be added when broader Hydrology negative-path families are stable enough to deserve their own directory, such as unresolved evidence refs, source-role collapse, stale-state misuse, direct internal-read requests, missing release state, rights/sensitivity gaps, malformed layer manifests, drawer boundary gaps, Focus Mode boundary gaps, or cross-lane evidence mismatch.

## Relationship to sibling fixture lanes

| Sibling lane | Relationship |
|---|---|
| `../decision_envelope/` | Runtime envelope fixture family; invalid envelope cases currently live under its `invalid/` child. |
| `../evidence_bundle/` | Evidence-support fixture family; invalid bundle cases currently live under its `invalid/` child. |
| `../golden/` | Stable expected fail-closed outputs should be paired there. |
| `../README.md` | Parent Hydrology fixture lane; not inspected during this update. |

## When to use this lane vs specific invalid children

| Use case | Preferred lane | Reason |
|---|---|---|
| Invalid runtime envelope shape or bounded runtime outcome | `../decision_envelope/invalid/` | The defect belongs to the runtime envelope family. |
| Invalid EvidenceBundle shape or claim-support closure | `../evidence_bundle/invalid/` | The defect belongs to evidence support. |
| Stable expected output for an invalid input | `../golden/` | Golden files anchor deterministic expectations. |
| Broad negative scenario not yet sorted | `./` | This parent can stage or document the family without creating premature taxonomy. |
| Real source material appears in a fixture | Neither | Move it out of fixtures and route through the governed lifecycle/quarantine path. |

## Related references

- `../decision_envelope/README.md`
- `../decision_envelope/invalid/README.md`
- `../decision_envelope/valid/README.md`
- `../evidence_bundle/README.md`
- `../evidence_bundle/invalid/README.md`
- `../evidence_bundle/valid/README.md`
- `../golden/README.md`
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

- small synthetic `*.input.json`, `*.invalid.json`, `*.negative.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- draft invalid examples for decision envelopes, EvidenceBundles, drawer outputs, Focus Mode outputs, layer resolver outputs, exports, source-role checks, evidence-resolution checks, citation-validation checks, rights/sensitivity checks, release-readiness checks, correction checks, rollback checks, and trust-membrane checks;
- toy `ABSTAIN`, `DENY`, `ERROR`, validation-failure, review-required, blocked-render, evidence-missing, citation-failed, rights-missing, sensitivity-missing, source-role-conflicted, release-blocked, or expected-output examples;
- contrast examples showing the difference between a valid governed envelope/support object and an invalid variant;
- paired expected outputs in `../golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for real records, source exports, lifecycle data, actual EvidenceBundles, source descriptors, proof packs, release manifests, implementation code, public API material, public map material, public tiles, direct model runtime output, source authority, policy authority, release authority, AI authority, or published artifacts.

## Shared fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Make the invalid condition explicit in the file name, payload, expected output, and consumer notes.
- Make expected outcome explicit when known: `ABSTAIN`, `DENY`, `ERROR`, validation failure, review-required, blocked render, release-readiness failure, or expected output.
- Pair each stable invalid input with an expected failure output in `../golden/` when practical.
- Move stable family-specific cases to a specific invalid child lane when the defect family becomes clear.
- Keep schema validity, semantic validity, evidence resolution, citation validation, rights posture, sensitivity posture, source-role validity, temporal validity, release posture, trust-membrane safety, drawer display, Focus Mode wording, layer-manifest state, UI behavior, correction posture, and rollback posture separate.
- Do not treat fixture failure as EvidenceBundle closure, policy approval, validator implementation proof, API implementation proof, UI implementation proof, release state, public-map authority, or published output.

## Expected invalid fixture families

| Scenario family | Preferred lane | Expected posture |
|---|---|---|
| Malformed or unsupported runtime envelope | `../decision_envelope/invalid/` | `ERROR` or validation failure. |
| Evidence is insufficient or cannot be resolved | `../decision_envelope/invalid/` or `../evidence_bundle/invalid/` | `ABSTAIN` or validation failure. |
| Citation validation fails | `../decision_envelope/invalid/` or `../golden/` | `ABSTAIN` or validation failure. |
| Required EvidenceBundle field is missing | `../evidence_bundle/invalid/` | Validation failure. |
| Source-role or regulatory-context boundary is collapsed | `../decision_envelope/invalid/` or future child lane | `DENY` or validation failure. |
| Direct request for internal lifecycle material | `../decision_envelope/invalid/` or future child lane | `DENY`. |
| Missing release, rights, sensitivity, correction, or rollback support | Specific fixture family or this parent until sorted | `DENY`, review-required, or release-readiness failure. |
| Stable fail-closed output is ready to compare | `../golden/` | Deterministic expected output. |

## Maintenance notes

- Update this README when new invalid child lanes, invalid payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each invalid fixture to the exact check and consumer that uses it.
- If expected invalid behavior stabilizes, update the paired input, expected output, consumer notes, child README, `../golden/README.md`, and this index together.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real source material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: replaced blank placeholder content.
- Fixture payload inventory: no payload files verified under this parent during this update.
- Decision-envelope invalid alignment: PARTIALLY VERIFIED against `fixtures/domains/hydrology/decision_envelope/invalid/README.md`.
- EvidenceBundle invalid alignment: PARTIALLY VERIFIED against `fixtures/domains/hydrology/evidence_bundle/invalid/README.md`.
- Golden fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hydrology/golden/README.md`.
- Parent Hydrology fixture README: NEEDS VERIFICATION.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, invalid-fixture checks, golden-file checks, Hydrology governed-API tests, decision-envelope checks, evidence-bundle checks, drawer checks, Focus Mode checks, layer-manifest checks, evidence-resolution checks, citation-validation checks, rights checks, sensitivity checks, source-role checks, trust-membrane checks, release-readiness checks, schema checks, policy checks, renderer checks, and UI implementation.
- Tests and validators: NOT RUN.

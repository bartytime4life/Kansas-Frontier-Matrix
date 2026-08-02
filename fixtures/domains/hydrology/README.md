# Hydrology fixtures

`fixtures/domains/hydrology/`

Status: draft / fixture parent index / Hydrology synthetic examples.

This directory is the Hydrology fixture root for small synthetic examples used to exercise governed Hydrology checks, bounded runtime envelopes, EvidenceBundle examples, RunReceipt examples, source-like examples, expected outputs, positive-path cases, fail-closed cases, and draft negative scenarios.

These files are examples only. They are not source records, lifecycle data, SourceDescriptors, actual EvidenceBundles, actual RunReceipts, proof packs, policy decisions, review approvals, release state, public API material, public map material, public tiles, Hydrology truth, source authority, policy authority, release authority, AI authority, or published artifacts.

## Fixture root posture

Hydrology fixtures are reviewable synthetic inputs and expected outputs for tests, validators, smoke checks, documentation examples, governed-API dry-runs, map/UI checks, and future CI coverage. They may imitate Hydrology object families, source roles, evidence support, decision envelopes, run receipts, and expected output states, but they must not become canonical truth, source registry records, proof authority, policy authority, release authority, or public-map authority.

A fixture may describe intended behavior before the corresponding validator, route, policy bundle, UI surface, release gate, or CI check exists. When implementation is not verified, the README must say so.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The root fixture README says `fixtures/` is for runtime fixture inputs and separates it from `tests/fixtures/`, `artifacts/`, and `data/`. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here.

## Current child-lane inventory

The following Hydrology fixture lanes have populated README coverage. This table is a navigation index, not proof that payload files, validators, tests, governed API routes, UI checks, policy bundles, release manifests, source-registry records, receipt stores, proof stores, or CI coverage exist.

| Child lane | Purpose | Expected posture |
|---|---|---|
| `decision_envelope/` | Synthetic Hydrology bounded runtime envelopes for governed API, drawer, Focus Mode, layer resolver, export, and review-facing outcomes. | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, validation pass/failure, review-required, or blocked render. |
| `evidence_bundle/` | Synthetic Hydrology claim-scope evidence-support examples. | Validation pass/failure, review-ready, evidence-resolved, citation-ready, `ABSTAIN`, `DENY`, `ERROR`, or release-readiness failure when consumed. |
| `run_receipt/` | Synthetic Hydrology governed-run provenance examples. | Validation pass/failure, provenance-resolved, replay-reviewable, review-required, release-readiness failure, or rollback-readiness failure. |
| `aquifer_observation/` | Synthetic groundwater measurement shapes, including linked and unlinked observations. | Valid observed measurement or expected rejection for source-role or embedded-Geology collapse. |
| `aquifer_context_link/` | Synthetic typed Hydrology-to-Geology relation shapes. | Valid observation/well relation or expected rejection for endpoint, measurement, or copied-geometry collapse. |
| `public_safe_flow/` | Frozen synthetic FlowObservation public-safe profile with exact positive/negative polarity. | Valid fixture-only flow shape or expected rejection for role, location, time, unit, governance, and warning-authority collapse. |
| `sources/` | Synthetic source-reference, source-role, rights, sensitivity, cadence, freshness, source-head, and admission examples. | Validation pass, review-ready, source-role-preserved, or fail-closed when source posture is unresolved. |
| `valid/` | Broad positive-path staging and navigation lane. | Validation pass, review-ready, evidence-resolved, citation-ready, provenance-resolved, public-safe context, or governed `ANSWER`. |
| `invalid/` | Broad fail-closed staging and navigation lane for known invalid families. | `ABSTAIN`, `DENY`, `ERROR`, validation failure, review-required, blocked render, or release-readiness failure. |
| `negative/` | Draft negative-path staging lane for cases not yet sorted into stable invalid families. | Negative example, review-required, fail-closed, or future invalid/golden pairing. |
| `golden/` | Expected-output lane for stable synthetic Hydrology inputs. | Deterministic expected output for positive-path and fail-closed inputs. |

## Relationship between major fixture families

| Family | Relationship |
|---|---|
| `sources/` | Exercises source-like posture; does not create SourceDescriptors or registry entries. |
| `run_receipt/` | Exercises governed-run provenance; does not prove truth, policy approval, or release. |
| `evidence_bundle/` | Exercises claim-scope evidence support; does not publish or decide policy. |
| `decision_envelope/` | Exercises bounded runtime outcomes; does not bypass evidence, policy, release, source-role, or trust-membrane gates. |
| `aquifer_observation/` | Exercises the measurement carrier; aquifer interpretation remains an optional external link. |
| `aquifer_context_link/` | Exercises relation metadata and typed endpoints; carries no measurement or Geology geometry. |
| `valid/` | Indexes broad positive cases and routes stable cases to more specific family lanes. |
| `invalid/` | Indexes broad fail-closed cases and routes stable defects to more specific invalid child lanes. |
| `negative/` | Stages exploratory negative cases before they become stable invalid fixtures. |
| `golden/` | Stores stable expected outputs paired with specific synthetic inputs. |

## Recommended use

| Use case | Preferred lane |
|---|---|
| Runtime `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` shape | `decision_envelope/` |
| Evidence refs, claim scopes, citations, rights, sensitivity, transforms, checksums, and spec linkage | `evidence_bundle/` |
| Run identity, stage, inputs, outputs, code ref, source descriptor refs, validation refs, spec hash, and outcome | `run_receipt/` |
| Groundwater-level or aquifer-state measurement shape | `aquifer_observation/` |
| Hydrology observation/well to Geology hydrostratigraphic relation shape | `aquifer_context_link/` |
| Source-like role, rights, sensitivity, cadence, source-head, and admission examples | `sources/` |
| Broad valid scenario not yet sorted | `valid/` |
| Broad known fail-closed scenario not yet sorted | `invalid/` |
| Draft negative scenario not ready for a precise lane | `negative/` |
| Stable expected output for any fixture input | `golden/` |
| Real source material, real registry records, actual EvidenceBundles, actual RunReceipts, release manifests, or public artifacts | Not fixtures; route through the governed responsibility root and lifecycle. |

## Related references

- `decision_envelope/README.md`
- `decision_envelope/valid/README.md`
- `decision_envelope/invalid/README.md`
- `evidence_bundle/README.md`
- `evidence_bundle/valid/README.md`
- `evidence_bundle/invalid/README.md`
- `run_receipt/README.md`
- `run_receipt/valid/README.md`
- `run_receipt/invalid/README.md`
- `aquifer_observation/README.md`
- `aquifer_context_link/README.md`
- `sources/README.md`
- `valid/README.md`
- `invalid/README.md`
- `negative/README.md`
- `golden/README.md`
- `../../README.md`
- `../../../docs/domains/hydrology/API_CONTRACTS.md`
- `../../../docs/domains/hydrology/BOUNDARY.md`
- `../../../docs/domains/hydrology/SOURCE_REGISTRY.md`
- `../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md`
- `../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md`
- `../../../contracts/domains/hydrology/decision_envelope.md`
- `../../../contracts/domains/hydrology/evidence_bundle.md`
- `../../../contracts/domains/hydrology/run_receipt.md`
- `../../../contracts/runtime/decision_envelope.md`
- `../../../contracts/evidence/evidence_bundle.md`
- `../../../contracts/runtime/run_receipt.md`
- `../../../schemas/contracts/v1/domains/hydrology/`
- `../../../schemas/contracts/v1/runtime/decision_envelope.schema.json`
- `../../../schemas/contracts/v1/evidence/evidence_bundle.schema.json`
- `../../../schemas/contracts/v1/runtime/run_receipt.schema.json`
- `../../../schemas/contracts/v1/source/`
- `../../../policy/domains/hydrology/`
- `../../../policy/sensitivity/hydrology/`
- `../../../data/registry/sources/hydrology/`
- `../../../data/registry/hydrology/sources/`
- `../../../data/proofs/hydrology/`
- `../../../release/candidates/hydrology/`
- `../../../release/manifests/hydrology/`
- `../../../docs/doctrine/directory-rules.md`

## Accepted material

This root and its child lanes may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.invalid.json`, `*.negative.json`, `*.expected.json`, `*.golden.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy decision envelopes, EvidenceBundle-like payloads, RunReceipt-like payloads, source-like refs, source-role cases, expected outputs, drawer contexts, Focus Mode contexts, layer resolver outputs, export examples, correction examples, rollback examples, and trust-membrane examples;
- positive-path, fail-closed, and expected-output examples that remain synthetic, deterministic, public-safe, and reviewable;
- contrast examples where a valid fixture is paired with an invalid or negative variant;
- README files documenting fixture intent, boundaries, consumer checks, and verification state.

## Exclusions

Do not use this root or its child lanes for real records, real source exports, lifecycle data, SourceDescriptors, actual EvidenceBundles, actual RunReceipts, source activation decisions, proof packs, release manifests, implementation code, public API material, public map material, public tiles, direct model runtime output, source authority, policy authority, release authority, AI authority, or published artifacts.

## Shared fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Use toy IDs, refs, timestamps, digests, checksums, hashes, source descriptor refs, evidence refs, validation refs, policy refs, release refs, and reviewer refs.
- Make fixture posture explicit: valid, invalid, negative, golden, expected output, source-role-preserved, source-role-conflicted, evidence-resolved, evidence-missing, citation-ready, citation-failed, rights-visible, rights-missing, sensitivity-visible, sensitivity-missing, provenance-resolved, replay-reviewable, public-safe, release-blocked, correction-visible, rollback-visible, or blocked render.
- Pair each stable input with an expected output in `golden/` when practical.
- Move stable broad examples into the most specific family lane once the object family and consumer are clear.
- Keep source admission, source role, evidence support, receipt provenance, citation validation, rights posture, sensitivity posture, policy filtering, release posture, trust-membrane safety, drawer display, Focus Mode wording, layer-manifest state, UI behavior, correction posture, rollback posture, and expected-output state separate.
- Do not treat fixture success or failure as source admission, SourceDescriptor authority, EvidenceBundle closure, RunReceipt storage proof, policy approval, validator implementation proof, API implementation proof, UI implementation proof, release state, public-map authority, or published output.

## Maintenance notes

- Update this README when new child lanes, payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each stable fixture to the exact check and consumer that uses it.
- If expected behavior stabilizes, update the paired input, expected output, consumer notes, child README, `golden/README.md`, and this root index together.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real source material, a real SourceDescriptor, an actual EvidenceBundle, an actual RunReceipt, or release material, move it out of this root, quarantine it through the governed lifecycle or registry process, and record the correction path.

## Verification status

- Target README: replaced greenfield stub content.
- Fixture payload inventory: the two aquifer families contain public-safe
  synthetic valid and expected-invalid JSON payloads, and `public_safe_flow/`
  contains one positive plus one exact expected-invalid profile; broader
  inventory remains only partially verified.
- Child README inventory: PARTIALLY VERIFIED against populated child lane READMEs fetched during this update and recent preceding updates.
- Decision-envelope fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hydrology/decision_envelope/README.md`.
- EvidenceBundle fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hydrology/evidence_bundle/README.md`.
- RunReceipt fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hydrology/run_receipt/README.md` from the recent preceding update.
- Source fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hydrology/sources/README.md` from the recent preceding update.
- Valid fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hydrology/valid/README.md`.
- Invalid fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hydrology/invalid/README.md`.
- Negative fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hydrology/negative/README.md`.
- Golden fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hydrology/golden/README.md`.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, Hydrology governed-API tests, decision-envelope checks, evidence-bundle checks, run-receipt checks, source-descriptor checks, source-role checks, drawer checks, Focus Mode checks, layer-manifest checks, evidence-resolution checks, citation-validation checks, rights checks, sensitivity checks, source-head checks, trust-membrane checks, release-readiness checks, rollback-readiness checks, schema checks, policy checks, renderer checks, and UI implementation.
- Aquifer pair tests and validators: VERIFIED locally with fixture polarity and
  fail-closed network guards; no source, endpoint, evidence, policy, proof, or
  release resolution is claimed.

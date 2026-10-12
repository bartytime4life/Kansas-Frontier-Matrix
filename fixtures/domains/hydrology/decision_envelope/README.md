# Hydrology decision-envelope fixtures

`fixtures/domains/hydrology/decision_envelope/`

Status: draft / fixture parent index / Hydrology decision-envelope examples.

This directory is the parent lane for small synthetic Hydrology `decision_envelope` fixture examples. These fixtures are used to exercise bounded runtime envelopes for Hydrology feature/detail responses, layer resolver outcomes, Evidence Drawer handoffs, Focus Mode bounded context, exports, review-facing runtime states, evidence resolution, citation validation, policy posture, release posture, source-role preservation, correction posture, rollback posture, and trust-membrane behavior.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, source descriptors, review approvals, policy decisions, release state, public API material, public map material, public tiles, source authority, policy authority, release authority, Hydrology truth, AI authority, or published artifacts.

## Decision-envelope posture

The Hydrology decision-envelope contract defines the domain alias of the shared runtime decision envelope. It is the finite-outcome wrapper Hydrology uses when a governed API, Evidence Drawer, Focus Mode response, layer resolver, export request, or review-facing runtime surface needs to return `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`.

The current Hydrology schema is an alias of the shared runtime schema and does not add Hydrology-specific top-level fields. Hydrology-specific meaning must therefore be carried through `policy_family`, `reason_code`, `reasons`, `obligations`, `evidence_refs`, policy, fixtures, and docs until the schema is revised.

This fixture parent can support future validation and governed-API checks, but examples here do not prove validator implementation, route behavior, policy enforcement, schema enforcement, EvidenceBundle storage, release integration, UI rendering, or CI coverage by themselves.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The root fixture README says `fixtures/` is for runtime fixture inputs and separates it from `tests/fixtures/`, `artifacts/`, and `data/`. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here.

## Child lane inventory

The following child lanes have populated README coverage. This table is a navigation index, not proof that payload files, validators, tests, governed API routes, UI checks, policy bundles, release manifests, or CI coverage exist.

| Child lane | Purpose | Expected posture |
|---|---|---|
| `valid/` | Positive-path and structurally valid finite Hydrology decision-envelope examples. | `ANSWER`, or valid `ABSTAIN` / `DENY` / `ERROR` when that is the correct bounded outcome. |
| `invalid/` | Fail-closed Hydrology decision-envelope examples for unsupported, blocked, malformed, or unresolved conditions. | `ABSTAIN`, `DENY`, `ERROR`, review-required, validation failure, or blocked render. |

## Relationship between fixture lanes

| Lane | Use |
|---|---|
| `valid/` | Synthetic inputs and envelopes intended to pass bounded semantic checks. |
| `invalid/` | Synthetic inputs and envelopes intended to fail closed without emitting a substantive claim. |
| Future `golden/` or expected-output lane | Stable expected outputs for valid and invalid inputs, if added. |
| Parent Hydrology fixture lane | Broader Hydrology fixture family; not inspected during this update. |

## Related references

- `valid/README.md`
- `invalid/README.md`
- `../README.md`
- `../../../README.md`
- `../../../../contracts/domains/hydrology/decision_envelope.md`
- `../../../../contracts/runtime/decision_envelope.md`
- `../../../../docs/domains/hydrology/API_CONTRACTS.md`
- `../../../../docs/domains/hydrology/BOUNDARY.md`
- `../../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md`
- `../../../../schemas/contracts/v1/domains/hydrology/decision_envelope.schema.json`
- `../../../../schemas/contracts/v1/runtime/decision_envelope.schema.json`
- `../../../../policy/domains/hydrology/`
- `../../../../data/registry/sources/hydrology/`
- `../../../../data/proofs/hydrology/`
- `../../../../release/candidates/hydrology/`
- `../../../../release/manifests/hydrology/`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This parent lane and its children may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.invalid.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy Hydrology decision envelopes using `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`;
- toy `decision_id`, `outcome`, `policy_family`, `reason_code`, `reasons`, `obligations`, `evidence_refs`, `evaluated_at`, `spec_hash`, `version`, and `issued_at` examples;
- toy examples for released feature/detail answers, layer resolver outcomes, drawer handoffs, Focus Mode bounded context, exports, review-facing states, missing evidence, citation failure, release blockers, source-role conflicts, trust-membrane blocks, malformed requests, and runtime errors;
- contrast examples showing the difference between a valid governed envelope and an invalid variant;
- paired expected outputs when behavior becomes stable.

## Exclusions

Do not use this lane for real records, source exports, lifecycle data, EvidenceBundles, actual source descriptors, proof packs, release manifests, implementation code, public API material, public map material, public tiles, direct model runtime output, source authority, policy authority, release authority, AI authority, or published artifacts.

## Shared fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Use toy decision IDs, toy feature refs, toy layer refs, toy reach refs, toy evidence refs, toy citation refs, toy policy refs, toy release refs, toy timestamps, toy digests, and toy hashes.
- Make the envelope posture explicit: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, valid, invalid, evidence-resolved, missing-evidence, citation-validated, citation-failed, policy-allowed, policy-blocked, release-permitted, release-missing, source-role-preserved, source-role-conflicted, correction-visible, rollback-visible, or expected output.
- Pair each stable input with an expected output when practical.
- Keep schema validity, semantic validity, evidence resolution, citation validation, policy filtering, source-role validity, temporal validity, release posture, trust-membrane safety, drawer display, Focus Mode wording, layer-manifest state, UI behavior, correction posture, and rollback posture separate.
- Do not document Hydrology-specific top-level decision-envelope fields as implemented unless the schema is expanded; the current contract says Hydrology-specific meaning is carried through runtime fields and semantic obligations.
- Do not treat fixture success or failure as EvidenceBundle closure, policy approval, validator implementation proof, API implementation proof, UI implementation proof, release state, public-map authority, or published output.

## Expected fixture families

| Scenario family | Preferred child lane | Expected posture |
|---|---|---|
| Released, evidence-backed Hydrology feature/detail response | `valid/` | `ANSWER` |
| Valid no-answer response where evidence is insufficient | `valid/` | `ABSTAIN` |
| Valid governed refusal for policy, sensitivity, or release posture | `valid/` | `DENY` |
| Valid finite runtime or schema failure envelope | `valid/` | `ERROR` |
| Missing evidence that should not emit a claim | `invalid/` | `ABSTAIN` or validation failure |
| Citation validation failure | `invalid/` | `ABSTAIN` |
| Source-role or regulatory-context misuse | `invalid/` | `DENY` or validation failure |
| Direct request for internal lifecycle material | `invalid/` | `DENY` |
| Malformed decision-envelope shape | `invalid/` | `ERROR` or validation failure |

## Maintenance notes

- Update this README when new child lanes, payload files, validators, tests, helper scripts, expected-output names, or decision-envelope consumer contracts are added.
- Link each stable fixture to the exact check and consumer that uses it.
- If expected behavior changes, update the paired input, expected output, consumer notes, child README, and this parent index together.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real source material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: replaced blank placeholder content.
- Child README inventory: PARTIALLY VERIFIED against populated `valid/README.md` and `invalid/README.md` fetched during this update.
- Fixture payload inventory: no payload files verified under this parent during this update.
- Valid fixture alignment: PARTIALLY VERIFIED against `valid/README.md`.
- Invalid fixture alignment: PARTIALLY VERIFIED against `invalid/README.md`.
- Hydrology decision-envelope contract alignment: PARTIALLY VERIFIED against `contracts/domains/hydrology/decision_envelope.md`.
- Hydrology API alignment: PARTIALLY VERIFIED against `docs/domains/hydrology/API_CONTRACTS.md`.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Parent Hydrology fixture alignment: NEEDS VERIFICATION.
- Consumer alignment: NEEDS VERIFICATION against validators, decision-envelope checks, Hydrology governed-API tests, feature-resolver checks, drawer checks, Focus Mode checks, layer-manifest checks, evidence-resolution checks, citation-validation checks, source-role checks, trust-membrane checks, release-readiness checks, schema checks, policy checks, and UI implementation.
- Tests and validators: NOT RUN.

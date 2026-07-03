# Hydrology decision-envelope valid fixtures

`fixtures/domains/hydrology/decision_envelope/valid/`

Status: draft / valid fixture lane / Hydrology decision-envelope positive-path examples.

This directory is for small synthetic Hydrology `decision_envelope` fixtures that represent valid bounded runtime envelopes. These examples are meant to exercise positive-path `ANSWER` outcomes and structurally valid finite non-answer outcomes when `ABSTAIN`, `DENY`, or `ERROR` is the correct governed result.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, source descriptors, review approvals, policy decisions, release state, public API material, public map material, public tiles, source authority, policy authority, release authority, Hydrology truth, AI authority, or published artifacts.

## Valid fixture posture

The Hydrology decision-envelope contract defines the domain alias of the shared runtime decision envelope. It is the bounded wrapper that lets Hydrology APIs return `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` without bypassing evidence, policy, release, source-role, sensitivity, or rollback gates.

A valid positive fixture should normally demonstrate `ANSWER` only when the toy Hydrology response is released, evidence-backed, policy-allowed, public-safe, source-role-preserving, and inside the governed trust membrane. The contract also permits valid `ABSTAIN`, `DENY`, and `ERROR` envelopes when those finite outcomes are the correct response for a structurally valid request.

Hydrology-specific meaning must remain inside the current runtime fields and semantic obligations because the Hydrology schema is currently an alias of the shared runtime schema and does not add Hydrology-specific top-level fields. Do not add top-level `feature_id`, `object_family`, `source_role`, `release_ref`, `rollback_ref`, or `not_for_life_safety` fields as implemented unless the schema is expanded.

This lane can support future validation and governed-API checks, but examples here do not prove validator implementation, route behavior, policy enforcement, schema enforcement, EvidenceBundle storage, release integration, UI rendering, or CI coverage by themselves.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The root fixture README says `fixtures/` is for operational rendering inputs, not validator-only test data. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here. The parent `fixtures/domains/hydrology/decision_envelope/README.md` is blank during this update.

## Relationship to adjacent lanes

| Adjacent lane | Relationship |
|---|---|
| `../` | Parent Hydrology decision-envelope fixture lane; blank during this update. |
| `../invalid/` | Sibling fail-closed lane for invalid or negative-path decision-envelope examples. |
| `../../` | Parent Hydrology fixture lane; not inspected during this update. |
| `../../../../README.md` | Root fixture rules; this lane follows the synthetic/public-safe fixture boundary. |
| `../../../../../contracts/domains/hydrology/decision_envelope.md` | Hydrology decision-envelope semantic contract; this lane supplies examples only. |
| `../../../../../docs/domains/hydrology/API_CONTRACTS.md` | Hydrology governed API and trust-membrane doctrine; this lane supplies examples only. |
| `../../../../../policy/domains/hydrology/` | Policy home; fixtures do not decide policy. |
| `../../../../../release/candidates/hydrology/` | Candidate release home; fixtures do not approve release. |
| `../../../../../release/manifests/hydrology/` | Release-manifest home if present; fixtures do not publish. |

## Related references

- `../README.md`
- `../invalid/README.md`
- `../../README.md`
- `../../../../README.md`
- `../../../../../contracts/domains/hydrology/decision_envelope.md`
- `../../../../../contracts/runtime/decision_envelope.md`
- `../../../../../docs/domains/hydrology/API_CONTRACTS.md`
- `../../../../../docs/domains/hydrology/BOUNDARY.md`
- `../../../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md`
- `../../../../../schemas/contracts/v1/domains/hydrology/decision_envelope.schema.json`
- `../../../../../schemas/contracts/v1/runtime/decision_envelope.schema.json`
- `../../../../../policy/domains/hydrology/`
- `../../../../../data/registry/sources/hydrology/`
- `../../../../../data/proofs/hydrology/`
- `../../../../../release/candidates/hydrology/`
- `../../../../../release/manifests/hydrology/`
- `../../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy valid Hydrology decision envelopes using `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` where the finite outcome is structurally and semantically valid;
- toy positive examples for released hydrology feature/detail answers, drawer handoffs, layer resolver outcomes, Focus Mode bounded context, public-safe exports, and review-facing runtime states;
- toy `decision_id`, `outcome`, `policy_family`, `reason_code`, `reasons`, `obligations`, `evidence_refs`, `evaluated_at`, `spec_hash`, `version`, and `issued_at` examples;
- toy contrast examples paired with `../invalid/` when a valid envelope is useful beside an invalid case;
- paired expected outputs when behavior becomes stable.

## Exclusions

Do not use this lane for real records, source exports, lifecycle data, EvidenceBundles, actual source descriptors, proof packs, release manifests, implementation code, public API material, public map material, public tiles, direct model runtime output, source authority, policy authority, release authority, AI authority, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Use toy decision IDs, toy feature refs, toy layer refs, toy reach refs, toy evidence refs, toy citation refs, toy policy refs, toy release refs, toy timestamps, toy digests, and toy hashes.
- Make the valid condition explicit: released evidence-backed answer, policy-allowed answer, valid abstain, valid deny, valid error, citation-validated answer, source-role-preserved answer, public-safe layer/export answer, or review-facing finite envelope.
- Make expected outcome explicit: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, expected output, or validation pass.
- Pair each valid input with an expected output when practical.
- Keep schema validity, semantic validity, evidence resolution, citation validation, policy filtering, source-role validity, temporal validity, release posture, trust-membrane safety, drawer display, Focus Mode wording, layer-manifest state, UI behavior, correction posture, and rollback posture separate.
- Do not document Hydrology-specific top-level decision-envelope fields as implemented unless the schema is expanded; the current contract says Hydrology-specific meaning is carried through runtime fields and semantic obligations.
- Do not treat fixture success as EvidenceBundle closure, policy approval, validator implementation proof, API implementation proof, UI implementation proof, release state, public-map authority, or published output.

## Expected valid examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Released, evidence-backed Hydrology feature/detail response with public-safe scope | `ANSWER` | Evidence and release state remain referenced, not embedded as authority. |
| Valid drawer handoff decision with evidence refs and citation obligations | `ANSWER` | Drawer projection still resolves through governed surfaces. |
| Valid layer resolver decision where release and policy posture allow serving metadata | `ANSWER` | Layer toggle is not publication by itself. |
| Valid Focus Mode bounded context over released Hydrology material | `ANSWER` | Generated language remains interpretive and receipt-backed. |
| Structurally valid no-answer case with missing evidence declared in runtime fields | `ABSTAIN` | A valid envelope can abstain without emitting a claim. |
| Structurally valid denial for policy or sensitivity reasons | `DENY` | A valid envelope can deny while remaining reviewable. |
| Structurally valid finite error for malformed upstream dependency | `ERROR` | Error does not fall through to raw source or generic AI text. |
| Valid contrast where regulatory context remains regulatory context | `ANSWER` | Regulatory context remains regulatory, not observed-event evidence. |

## Maintenance notes

- Update this README when valid payload files, validators, tests, helper scripts, expected-output names, or decision-envelope consumer contracts are added.
- Link each valid fixture to the decision-envelope check, schema check, evidence-resolution check, citation-validation check, source-role check, trust-membrane check, policy-filter check, release-readiness check, drawer check, Focus Mode check, correction check, rollback check, or governed-API dry-run that consumes it.
- If expected valid behavior changes, update the paired input, expected output, consumer notes, sibling invalid/contrast notes, and verification status together.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real source material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: replaced blank placeholder content.
- Fixture payload inventory: no payload files verified in this directory during this update.
- Parent decision-envelope fixture README: present but blank during this update.
- Sibling invalid fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hydrology/decision_envelope/invalid/README.md`.
- Hydrology decision-envelope contract alignment: PARTIALLY VERIFIED against `contracts/domains/hydrology/decision_envelope.md`.
- Hydrology API alignment: PARTIALLY VERIFIED against `docs/domains/hydrology/API_CONTRACTS.md`.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, decision-envelope checks, Hydrology governed-API tests, feature-resolver checks, drawer checks, Focus Mode checks, layer-manifest checks, evidence-resolution checks, citation-validation checks, source-role checks, trust-membrane checks, release-readiness checks, schema checks, policy checks, and UI implementation.
- Tests and validators: NOT RUN.

# Hydrology decision-envelope invalid fixtures

`fixtures/domains/hydrology/decision_envelope/invalid/`

Status: draft / invalid fixture lane / Hydrology decision-envelope negative-path examples.

This directory is for small synthetic Hydrology `decision_envelope` fixtures that should not produce a valid substantive Hydrology claim. These examples are meant to exercise fail-closed decision-envelope outcomes for malformed inputs, unresolved evidence, citation failure, release blockers, source-role collapse, trust-membrane bypass, life-safety framing, NFHL/regulatory misuse, sensitive joins, and runtime failures.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, source descriptors, review approvals, policy decisions, release state, public API material, public map material, public tiles, source authority, policy authority, release authority, Hydrology truth, alert authority, AI authority, or published artifacts.

## Invalid fixture posture

The Hydrology decision-envelope contract defines the domain alias of the shared runtime decision envelope. It is the bounded wrapper that lets Hydrology APIs return `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` without bypassing evidence, policy, release, source-role, sensitivity, or rollback gates.

For invalid fixtures in this lane, the expected posture is normally one of:

- `ABSTAIN` when evidence, citation validation, temporal scope, source-role clarity, or public-safe release support is insufficient;
- `DENY` when policy, rights, sensitivity, release state, source-role anti-collapse, direct RAW/WORK/QUARANTINE access, life-safety framing, or forbidden cross-lane use blocks the response;
- `ERROR` when request shape, schema validation, resolver behavior, dependency resolution, or runtime evaluation fails.

A fixture in this lane should never emit a substantive Hydrology `ANSWER` unless it is a contrast example that clearly belongs with a paired valid/golden fixture.

This lane can support future validation and governed-API checks, but examples here do not prove validator implementation, route behavior, policy enforcement, schema enforcement, EvidenceBundle storage, release integration, UI rendering, or CI coverage by themselves.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The root fixture README says `fixtures/` is for operational rendering inputs, not validator-only test data. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here. The parent `fixtures/domains/hydrology/decision_envelope/README.md` is blank during this update.

## Relationship to adjacent lanes

| Adjacent lane | Relationship |
|---|---|
| `../` | Parent Hydrology decision-envelope fixture lane; blank during this update. |
| `../../` | Parent Hydrology fixture lane; not inspected during this update. |
| `../../../../README.md` | Root fixture rules; this lane follows the synthetic/public-safe fixture boundary. |
| `../../../../../contracts/domains/hydrology/decision_envelope.md` | Hydrology decision-envelope semantic contract; this lane supplies examples only. |
| `../../../../../docs/domains/hydrology/API_CONTRACTS.md` | Hydrology governed API and trust-membrane doctrine; this lane supplies examples only. |
| `../../../../../policy/domains/hydrology/` | Policy home; fixtures do not decide policy. |
| `../../../../../release/candidates/hydrology/` | Candidate release home; fixtures do not approve release. |
| `../../../../../release/manifests/hydrology/` | Release-manifest home if/when present; fixtures do not publish. |

## Related references

- `../README.md`
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

- small synthetic `*.input.json`, `*.invalid.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy invalid Hydrology decision envelopes using `ABSTAIN`, `DENY`, or `ERROR`;
- toy examples for missing EvidenceBundle support, citation-validation failure, source-role conflict, release-missing state, direct RAW/WORK/QUARANTINE request, NFHL/regulatory-as-observed misuse, life-safety framing, sensitive joins, malformed request shape, and runtime failure;
- toy `reason_code`, `reasons`, `obligations`, `policy_family`, `evidence_refs`, `evaluated_at`, `spec_hash`, and decision-ID examples;
- paired expected outputs when behavior becomes stable.

## Exclusions

Do not use this lane for real records, source exports, lifecycle data, EvidenceBundles, actual source descriptors, proof packs, release manifests, implementation code, public API material, public map material, public tiles, operational alert feeds, life-safety instructions, direct model runtime output, source authority, policy authority, release authority, AI authority, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Use toy decision IDs, toy feature refs, toy layer refs, toy reach refs, toy evidence refs, toy citation refs, toy policy refs, toy release refs, toy timestamps, toy digests, and toy hashes.
- Make the defect explicit: missing evidence, failed citation validation, NFHL/regulatory-as-observed collapse, life-safety framing, direct RAW/WORK/QUARANTINE request, missing release manifest, sensitive join, malformed request, schema failure, resolver failure, or runtime failure.
- Make expected outcome explicit: `ABSTAIN`, `DENY`, `ERROR`, review-required, validation failure, blocked render, or expected output.
- Pair each invalid input with an expected failure output when practical.
- Keep schema validity, semantic validity, evidence resolution, citation validation, policy filtering, source-role validity, temporal validity, release posture, trust-membrane safety, drawer display, Focus Mode wording, layer-manifest state, UI behavior, correction posture, and rollback posture separate.
- Do not document Hydrology-specific top-level decision-envelope fields as implemented unless the schema is expanded; the current contract says Hydrology-specific meaning is carried through runtime fields and semantic obligations.
- Do not treat fixture failure as EvidenceBundle closure, policy approval, validator implementation proof, API implementation proof, UI implementation proof, release state, public-map authority, or published output.

## Expected invalid examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Missing EvidenceBundle support for a requested Hydrology claim | `ABSTAIN` | Cite-or-abstain remains visible. |
| Citation validation fails for available evidence refs | `ABSTAIN` | No substantive claim should be emitted. |
| NFHL regulatory context presented as observed flood extent | `DENY` | Regulatory context must not become observed flooding. |
| Public client requests RAW, WORK, QUARANTINE, or unreleased candidate content | `DENY` | Trust membrane blocks direct internal access. |
| Hydrology request asks KFM for flood-warning or life-safety instruction | `DENY` | KFM is not an emergency flood-warning authority. |
| Layer requested without ReleaseManifest or public-safe release state | `DENY` | Release state gates public answers. |
| Infrastructure/private-property sensitive join lacks steward review | `DENY` or `ABSTAIN` | Sensitive joins require governance. |
| Malformed decision envelope lacks required runtime fields | `ERROR` or validation failure | Required fields include decision ID, outcome, policy family, reasons, obligations, and evaluated time. |
| Resolver dependency fails during evaluation | `ERROR` | Error remains finite and must not fall through to raw source or AI text. |

## Maintenance notes

- Update this README when invalid payload files, validators, tests, helper scripts, expected-output names, or decision-envelope consumer contracts are added.
- Link each invalid fixture to the decision-envelope check, schema check, evidence-resolution check, citation-validation check, source-role check, NFHL/regulatory-boundary check, trust-membrane check, policy-filter check, release-readiness check, drawer check, Focus Mode check, correction check, rollback check, or governed-API dry-run that consumes it.
- If expected invalid behavior changes, update the paired input, expected output, consumer notes, and verification status together.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real source material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: replaced blank placeholder content.
- Fixture payload inventory: no payload files verified in this directory during this update.
- Parent decision-envelope fixture README: present but blank during this update.
- Hydrology decision-envelope contract alignment: PARTIALLY VERIFIED against `contracts/domains/hydrology/decision_envelope.md`.
- Hydrology API alignment: PARTIALLY VERIFIED against `docs/domains/hydrology/API_CONTRACTS.md`.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, decision-envelope checks, Hydrology governed-API tests, feature-resolver checks, drawer checks, Focus Mode checks, layer-manifest checks, evidence-resolution checks, citation-validation checks, source-role checks, NFHL/regulatory-boundary checks, trust-membrane checks, release-readiness checks, schema checks, policy checks, and UI implementation.
- Tests and validators: NOT RUN.

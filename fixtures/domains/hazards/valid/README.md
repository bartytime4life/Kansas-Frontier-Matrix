# Hazards valid fixtures

`fixtures/domains/hazards/valid/`

Status: draft / valid fixture lane / positive-path Hazards examples.

This directory is for small synthetic positive-path Hazards fixtures. Valid fixtures are designed to exercise bounded `ANSWER` outcomes and valid public-safe envelope shapes for Hazards feature resolution, Evidence Drawer projection, Focus Mode, identity references, layer manifests, source-role preservation, evidence resolution, citation validation, policy state, release posture, correction posture, rollback posture, and map/UI handoff examples.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, source descriptors, review approvals, release state, public API material, public map material, public tiles, source authority, policy authority, release authority, Hazards truth, AI authority, or published artifacts.

## Valid fixture posture

Use this lane for synthetic inputs that are intended to pass semantic checks and produce a bounded positive outcome, normally `ANSWER`, when paired with suitable golden expected outputs. A valid fixture should still preserve KFM trust boundaries: evidence refs remain refs, policy refs remain refs, release refs remain refs, source roles remain explicit, freshness remains visible, and disclaimers/limitations remain inspectable where material.

A valid fixture is not proof of implementation. It does not prove that validators, governed API routes, UI checks, schema enforcement, release integration, policy bundles, source descriptors, EvidenceBundles, or CI coverage exist. It only provides reviewable synthetic material for future checks.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The root fixture README says `fixtures/` is for operational rendering inputs, not validator-only test data. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here. The parent Hazards fixture README is still a greenfield stub during this update.

## Relationship to adjacent lanes

| Adjacent lane | Relationship |
|---|---|
| `../feature_resolver/` | Valid resolver inputs should produce bounded `HazardsDecisionEnvelope` outputs. |
| `../drawer/` | Valid drawer inputs should project governed evidence, citation, policy, release, and limitation state. |
| `../focus/` | Valid Focus inputs should be evidence-bounded and receipt-backed. |
| `../identity/` | Valid examples should use stable toy identity refs and preserve source role / temporal scope. |
| `../layer_manifest/` | Valid layer examples should preserve release, evidence, policy, stale/freshness, and rollback state. |
| `../golden/` | Stable valid inputs should be paired with expected positive outputs there. |
| `../negative/` | Exploratory negative cases live there until categorized. |
| `../invalid/` | Stable fail-closed cases live there, not in this valid lane. |
| `../README.md` | Parent Hazards fixture lane; still a greenfield stub during this update. |

## Relationship to `valid/`, `negative/`, `invalid/`, and `golden/`

| Lane | Use |
|---|---|
| `valid/` | Positive-path synthetic inputs expected to pass bounded checks. |
| `negative/` | Draft negative cases that are not yet sorted into stable invalid child lanes. |
| `invalid/` | Stable fail-closed negative cases with known defect families. |
| `golden/` | Expected outputs for stable valid, negative, and invalid inputs. |

## Related references

- `../feature_resolver/README.md`
- `../drawer/README.md`
- `../focus/README.md`
- `../identity/README.md`
- `../layer_manifest/README.md`
- `../golden/README.md`
- `../negative/README.md`
- `../invalid/README.md`
- `../../README.md`
- `../../../../docs/architecture/governed-api.md`
- `../../../../docs/architecture/hazards-trust-membrane.md`
- `../../../../docs/domains/hazards/API_CONTRACTS.md`
- `../../../../docs/domains/hazards/MAP_UI_CONTRACTS.md`
- `../../../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md`
- `../../../../docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md`
- `../../../../contracts/evidence/evidence_drawer_payload.md`
- `../../../../contracts/domains/hazards/hazards_decision_envelope.md`
- `../../../../contracts/domains/hazards/domain_feature_identity.md`
- `../../../../contracts/domains/hazards/domain_layer_descriptor.md`
- `../../../../contracts/data/layer_manifest.md`
- `../../../../schemas/contracts/v1/domains/hazards/`
- `../../../../schemas/contracts/v1/evidence/`
- `../../../../schemas/contracts/v1/focus/`
- `../../../../schemas/contracts/v1/data/layer_manifest.schema.json`
- `../../../../policy/domains/hazards/`
- `../../../../release/manifests/hazards/`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy valid resolver, drawer, Focus Mode, identity, layer-manifest, evidence, policy, release, correction, rollback, source-role, freshness, and trust-membrane examples;
- toy bounded `ANSWER` examples for released historical-context, regulatory-context, modeled-context, observation-context, exposure-summary, resilience-summary, and official-link/context-only scenarios;
- toy valid `ABSTAIN`, `DENY`, or `ERROR` examples only when the input is structurally valid and the valid behavior is a finite non-answer state by design;
- contrast examples showing the difference between a valid governed envelope and invalid or negative variants;
- paired expected outputs in `../golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for real records, source exports, lifecycle data, EvidenceBundles, actual source descriptors, proof packs, release manifests, implementation code, public API material, public map material, public tiles, direct model runtime output, source authority, policy authority, release authority, AI authority, or published artifacts.

## Shared fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Make the valid condition explicit in the file name, payload, expected output, and consumer notes.
- Use toy IDs, toy source refs, toy feature refs, toy layer refs, toy evidence refs, toy citation refs, toy policy refs, toy release refs, toy timestamps, toy digests, and toy hashes.
- Make expected posture explicit: `ANSWER`, bounded context, evidence-resolved, citation-validated, policy-allowed, release-permitted, source-role-preserved, freshness-visible, correction-visible, rollback-visible, disclaimer-visible, or expected output.
- Pair each stable valid input with an expected output when practical.
- Keep schema validity, semantic validity, evidence resolution, citation validation, policy filtering, source-role validity, temporal validity, release posture, trust-membrane safety, drawer display, Focus Mode wording, resolver context, layer-manifest state, UI behavior, correction posture, and rollback posture separate.
- Do not treat fixture success as EvidenceBundle closure, policy approval, validator implementation proof, API implementation proof, UI implementation proof, release state, public-map authority, or published output.

## Expected valid examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Synthetic released historical Hazards feature with resolvable evidence and release refs | `ANSWER` | Bounded context only; not source truth. |
| Synthetic drawer payload with citations, limitations, freshness, correction, and rollback state | Valid drawer projection | Trust-visible display state remains inspectable. |
| Synthetic Focus Mode request over released evidence with AI receipt and citation-validation state | `ANSWER` | Generated language remains interpretive. |
| Synthetic layer manifest with public-safe flag, release ref, policy ref, evidence refs, and disclaimer field | `ANSWER` | Layer manifest is metadata, not layer bytes or release authority. |
| Synthetic regulatory context presented as regulatory context | `ANSWER` | Regulatory role remains visible and does not become observed event evidence. |
| Synthetic modeled context presented as modeled context with bounds and method refs | `ANSWER` | Modeled role remains visible and does not become observation. |
| Synthetic valid contrast to a known invalid case | Valid expected output | Pair with `../invalid/` and `../golden/` when stable. |

## Maintenance notes

- Update this README when new valid child lanes, valid payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each stable valid fixture to the exact check and consumer that uses it.
- If expected valid behavior changes, update the paired input, expected output, consumer notes, child README, and `../golden/README.md` together.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real source material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: replaced one-character placeholder content.
- Valid fixture payload inventory: no payload files verified under this parent during this update.
- Hazards golden fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/golden/README.md`.
- Hazards feature-resolver fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/feature_resolver/README.md`.
- Hazards drawer fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/drawer/README.md`.
- Hazards Focus fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/focus/README.md`.
- Hazards layer-manifest fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/layer_manifest/README.md`.
- Hazards negative fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/negative/README.md`.
- Parent Hazards fixture README: present but still a greenfield stub during this update.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, valid-fixture checks, golden-file checks, governed-API tests, feature-resolver checks, drawer checks, Focus Mode checks, identity checks, layer-manifest checks, evidence-resolution checks, citation-validation checks, source-role checks, freshness checks, UI tests, release-readiness checks, schema checks, and policy checks.
- Tests and validators: NOT RUN.

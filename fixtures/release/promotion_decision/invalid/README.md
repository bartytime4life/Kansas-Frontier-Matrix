# PromotionDecision invalid release fixtures

`fixtures/release/promotion_decision/invalid/`

Status: draft / invalid release fixture lane / synthetic PromotionDecision fail-closed examples.

This directory is for small synthetic invalid `PromotionDecision` fixture examples. Use it for toy promotion-gate cases that should fail schema validation, policy validation, evidence-resolution checks, rollback-readiness checks, review-binding checks, release-readiness checks, public-summary projection checks, supersession checks, or CI dry-runs.

These files are examples only. They are not actual PromotionDecision records, ReleaseManifests, RollbackCards, ReviewRecords, PolicyDecisions, EvidenceBundles, SourceDescriptors, RunReceipts, proof packs, signed attestations, release artifacts, public API material, public map material, public tiles, source authority, evidence authority, policy authority, proof authority, review authority, release authority, AI authority, or published artifacts.

## Invalid fixture posture

Use this lane for synthetic release-promotion examples that must fail closed. Expected outcomes may include validation failure, policy failure, release-readiness failure, review-required, blocked projection, `DENY`, `ABSTAIN`, or a documented expected failure output.

A PromotionDecision fixture can imitate an invalid decision shape or unsafe promotion context, but it does not approve or deny a real transition, publish a release, move a file, issue policy authority, satisfy evidence closure, execute rollback, or permit public API/UI/map/AI serving.

The PromotionDecision contract treats promotion as a governed state transition, not a file move, rename, merge, deployment, or UI action. Missing evidence, rollback support, review binding, policy bundle, release manifest, validation report, or sensitivity/rights support must fail closed.

A fixture can describe desired invalid behavior before validators, policy rules, release storage, schemas, proof/receipt emission, public-summary projection, separation-of-duties checks, or CI coverage exist. Fixture failure is not implementation proof by itself.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, public API root, or publication root.

The parent PromotionDecision fixture README keeps this fixture family synthetic and non-authoritative. The root fixture README says `fixtures/` is for operational rendering inputs, not validator-only test data, and separates `fixtures/` from `tests/fixtures/`, `artifacts/`, and `data/`.

## Relationship to release governance

| Lane or document | Relationship |
|---|---|
| `../README.md` | Parent synthetic PromotionDecision fixture lane; this invalid lane specializes fail-closed cases. |
| `../../README.md` | Release fixture parent; not found during the parent README update, so this lane remains self-bounded. |
| `../../../../contracts/release/promotion_decision.md` | Semantic contract for `PromotionDecision`; invalid fixtures do not define meaning. |
| `../../../../contracts/release/README.md` | Release contract-family README; fixtures do not store release objects or run gates. |
| `../../../../contracts/release/release_manifest.md` | ReleaseManifest contract if present; invalid PromotionDecision fixtures are not release manifests. |
| `../../../../contracts/release/rollback_card.md` | RollbackCard contract if present; fixtures may test missing rollback support but do not execute rollback. |
| `../../../../schemas/contracts/v1/release/promotion_decision.schema.json` | Machine-shape authority if present; fixtures do not define schemas. |
| `../../../../policy/promotion/` | Promotion policy home if present; fixtures do not decide admissibility. |
| `../../../../policy/release/` | Release policy home if present; fixtures do not decide release. |
| `../../../../release/` | Release artifact/process root if present; fixtures do not publish. |
| `../../../../data/proofs/` | Proof home if present; fixtures do not create proof authority. |
| `../../../../data/receipts/` | Receipt home if present; fixtures do not store actual receipts. |
| `../../../invalid/README.md` | Top-level fail-closed fixture lane for broad invalid examples. |
| `../../../golden/README.md` | Top-level expected-output lane for stable synthetic expected outputs. |

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.invalid.json`, `*.negative.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy invalid `PromotionDecision` examples with missing required fields, invalid finite decision values, invalid version, invalid domain/id convention, unresolved evidence refs, missing EvidenceBundle URI refs, missing rollback refs, missing policy-bundle refs, missing review bindings, stale decision timestamps, stale policy context, unexpected fields, or unsafe public-summary projections;
- toy fail-closed cases where `APPROVE` is attempted without evidence closure, rollback support, review binding, policy bundle identity, or release-readiness support;
- toy `DENY` or `ABSTAIN` examples that preserve prior state and show safe fail-closed posture;
- toy supersession mistakes where a later decision attempts to silently mutate prior decision history instead of emitting a new object;
- paired expected failure outputs in `../../../golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for actual PromotionDecision records, actual release decisions, release manifests, rollback cards, review records, policy decisions, EvidenceBundles, SourceDescriptors, RunReceipts, proof packs, receipts, signed attestations, lifecycle data, source exports, implementation code, release artifacts, public API material, public map material, public tiles, generated CI artifacts, direct runtime output, source authority, evidence authority, policy authority, proof authority, review authority, release authority, AI authority, or published artifacts.

## Shared fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Use toy IDs, toy run refs, toy domains, toy evidence refs, toy EvidenceBundle refs, toy rollback refs, toy policy-bundle refs, toy review refs, toy timestamps, toy digests, and toy hashes.
- Make the invalid condition explicit in the file name, payload, expected output, and consumer notes.
- Make expected outcome explicit when known: validation failure, policy failure, release-readiness failure, review-required, blocked projection, `DENY`, `ABSTAIN`, or expected output.
- Keep schema validity, semantic validity, evidence closure, policy bundle identity, review binding, rollback readiness, lifecycle-boundary context, release-manifest relationship, proof/receipt emission, public-summary projection, correction posture, rollback posture, supersession state, and expected-output state separate.
- Pair each stable invalid input with an expected failure output when practical.
- Do not treat fixture failure as validator implementation proof, release-runtime proof, policy enforcement proof, review approval, evidence closure, rollback execution, release publication, file movement, public-surface permission, or published output.

## Expected invalid PromotionDecision fixture families

| Scenario family | Expected posture | Notes |
|---|---|---|
| Missing required field | Validation failure | Required field set is contract/schema-bound. |
| Invalid `version` | Validation failure | Current schema expects `v1`. |
| Invalid finite decision value | Validation failure | Release vocabulary is `APPROVE`, `DENY`, `ABSTAIN`. |
| `APPROVE` without resolvable evidence or EvidenceBundle support | Policy failure, `DENY`, or `ABSTAIN` | EvidenceBundle remains evidence authority. |
| `APPROVE` without rollback support | Validation failure or release-readiness failure | Rollback readiness is a core invariant. |
| Missing reviewer or ticket binding | Validation failure or review-required | Fixture does not replace ReviewRecord. |
| Stale or ambiguous policy bundle | Policy failure or `ABSTAIN` | Policy bundle identity must be auditable. |
| Hydrology id convention failure | Validation failure where schema rule applies | Hydrology ids use the schema-confirmed pattern. |
| Unexpected field present | Validation failure where schema closes properties | Object shape remains bounded. |
| Raw decision internals exposed as public surface | Blocked projection | Public surfaces must use bounded summaries. |
| Silent mutation of prior decision | Validation failure or review-required | Supersession emits a new object, not hidden history edits. |
| Stable fail-closed output is ready to compare | `../../../golden/` | Deterministic expected output, not release. |

## Maintenance notes

- Update this README when invalid payload files, validators, tests, helper scripts, expected-output names, schema decisions, policy rules, release storage paths, proof/receipt emitters, public-summary projections, or CI checks are added.
- Link each invalid fixture to the exact schema check, policy check, release-readiness check, validator check, public-projection check, correction check, rollback check, documentation example, or governed release dry-run that consumes it.
- If expected invalid behavior stabilizes, update the paired input, expected output, consumer notes, parent README, and this invalid index together.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes actual release decisions, proof material, receipt material, release material, source exports, lifecycle data, real reviewer data, restricted policy context, or sensitive source detail, move it out of this lane, quarantine it through the governed lifecycle or security process, and record the correction path.

## Verification status

- Target README: replaced blank placeholder content.
- Parent PromotionDecision fixture alignment: PARTIALLY VERIFIED against `fixtures/release/promotion_decision/README.md`.
- Fixture payload inventory: no payload files verified under this invalid lane during this update.
- Exact child-lane inventory under `fixtures/release/promotion_decision/invalid/`: NOT VERIFIED during this update.
- Root fixture alignment: PARTIALLY VERIFIED against recent `fixtures/README.md` evidence from the parent update.
- PromotionDecision contract alignment: PARTIALLY VERIFIED against `contracts/release/promotion_decision.md`.
- Schema/validator/policy alignment: NEEDS VERIFICATION against `schemas/contracts/v1/release/promotion_decision.schema.json`, `tools/validators/release/validate_promotion_decision.py`, `policy/promotion/`, and `policy/release/`.
- Consumer alignment: NEEDS VERIFICATION against validators, release dry-runs, policy checks, evidence-resolution checks, rollback checks, review checks, proof/receipt emission, public-summary projection, release-readiness checks, correction checks, rollback checks, schema checks, and CI implementation.
- Tests and validators: NOT RUN.

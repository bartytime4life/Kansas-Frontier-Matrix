# PromotionDecision release fixtures

`fixtures/release/promotion_decision/`

Status: draft / release fixture lane / synthetic PromotionDecision examples.

This directory is for small synthetic `PromotionDecision` fixture examples. Use it for toy promotion-gate cases that exercise release decision shape, finite decision outcomes, evidence refs, EvidenceBundle closure refs, rollback refs, policy-bundle refs, review bindings, lifecycle-boundary context, fail-closed behavior, supersession examples, public-summary behavior, release-readiness checks, validator dry-runs, and documentation examples.

These files are examples only. They are not actual PromotionDecision records, ReleaseManifests, RollbackCards, ReviewRecords, PolicyDecisions, EvidenceBundles, SourceDescriptors, RunReceipts, proof packs, signed attestations, release artifacts, public API material, public map material, public tiles, source authority, evidence authority, policy authority, proof authority, review authority, release authority, AI authority, or published artifacts.

## Fixture lane posture

Use this lane for synthetic release-promotion examples only. A fixture may imitate a valid or invalid `PromotionDecision` shape, but it does not approve a real transition, publish a release, move a file, issue policy authority, satisfy evidence closure, execute rollback, or permit public API/UI/map/AI serving.

The PromotionDecision contract defines `PromotionDecision` as a reviewed, evidence-bound, policy-bound decision about whether a specific run or release candidate may cross a governed lifecycle boundary. It is a release-family decision object, not a file move, deployment shortcut, release manifest, or public-surface permission by itself.

A fixture can describe expected valid or invalid behavior before validators, policy rules, release storage, schemas, signing checks, proof/receipt emission, public-summary projection, separation-of-duties checks, or CI coverage exist. Fixture success or failure is not implementation proof by itself.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, public API root, or publication root.

The root fixture README says `fixtures/` is for operational rendering inputs, not validator-only test data. It also separates `fixtures/` from `tests/fixtures/`, `artifacts/`, and `data/`, and says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here.

`fixtures/release/README.md` was not found during this update. Until a release fixture parent README exists, this lane must carry its own boundary statement and must not imply parent-level release fixture maturity.

## Relationship to release governance

| Lane or document | Relationship |
|---|---|
| `../../../contracts/release/promotion_decision.md` | Semantic contract for `PromotionDecision`; fixtures do not define meaning. |
| `../../../contracts/release/README.md` | Release contract-family README; fixtures do not store release objects or run gates. |
| `../../../contracts/release/release_manifest.md` | ReleaseManifest contract if present; PromotionDecision is not a ReleaseManifest. |
| `../../../contracts/release/rollback_card.md` | RollbackCard contract if present; PromotionDecision references rollback support but does not execute rollback. |
| `../../../contracts/policy/policy_decision.md` | Runtime/policy decision contract if present; PromotionDecision vocabulary is release-transition vocabulary. |
| `../../../contracts/evidence/evidence_bundle.md` | EvidenceBundle contract if present; EvidenceBundle remains evidence authority. |
| `../../../schemas/contracts/v1/release/promotion_decision.schema.json` | Machine-shape authority if present; fixtures do not define schemas. |
| `../../../policy/promotion/` | Promotion policy home if present; fixtures do not decide admissibility. |
| `../../../policy/release/` | Release policy home if present; fixtures do not decide release. |
| `../../../release/` | Release artifact/process root if present; fixtures do not publish. |
| `../../../data/proofs/` | Proof home if present; fixtures do not create proof authority. |
| `../../../data/receipts/` | Receipt home if present; fixtures do not store actual receipts. |
| `../../../tools/validators/release/validate_promotion_decision.py` | Validator path named by the contract; implementation and wiring remain verification-bound. |
| `../../golden/README.md` | Top-level expected-output lane for stable synthetic expected outputs. |
| `../../invalid/README.md` | Top-level fail-closed fixture lane for broad invalid examples. |

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.invalid.json`, `*.negative.json`, `*.expected.json`, `*.golden.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy valid `PromotionDecision` examples with complete required fields, finite decision outcome, toy domain/run refs, toy evidence refs, toy EvidenceBundle URI refs, toy rollback-card refs, toy policy-bundle refs, toy timestamps, and toy review bindings;
- toy invalid examples for missing required fields, invalid finite decision outcome, unresolved evidence, missing rollback support, missing review binding, stale policy context, invalid domain id convention, or unexpected fields;
- toy `APPROVE`, `DENY`, and `ABSTAIN` examples, where each outcome remains release-transition vocabulary and not runtime answer vocabulary;
- toy supersession examples where a new decision supersedes a previous decision without silently mutating history;
- toy public-summary examples that expose only a bounded summary instead of treating raw release decision internals as a public surface;
- paired expected outputs in `../../golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for actual PromotionDecision records, actual release decisions, release manifests, rollback cards, review records, policy decisions, EvidenceBundles, SourceDescriptors, RunReceipts, proof packs, receipts, signed attestations, lifecycle data, source exports, implementation code, release artifacts, public API material, public map material, public tiles, generated CI artifacts, direct runtime output, source authority, evidence authority, policy authority, proof authority, review authority, release authority, AI authority, or published artifacts.

## Shared fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Use toy IDs, toy run refs, toy domains, toy evidence refs, toy EvidenceBundle refs, toy rollback refs, toy policy-bundle refs, toy review refs, toy timestamps, toy digests, and toy hashes.
- Make fixture posture explicit: valid, invalid, negative, expected output, approve, deny, abstain, evidence-resolved, evidence-missing, rollback-ready, rollback-missing, policy-bound, policy-stale, review-bound, review-missing, release-ready, release-blocked, superseding, correction-visible, rollback-visible, or public-summary-safe.
- Make expected outcome explicit when known: validation pass, validation failure, policy pass, policy failure, release-readiness pass, release-readiness failure, `APPROVE`, `DENY`, `ABSTAIN`, blocked projection, or expected output.
- Keep schema validity, semantic validity, evidence closure, policy bundle identity, review binding, rollback readiness, lifecycle-boundary context, release-manifest relationship, proof/receipt emission, public-summary projection, correction posture, rollback posture, supersession state, and expected-output state separate.
- Pair each stable input with an expected output when practical.
- Do not treat fixture success or failure as promotion approval, release publication, file movement, release-manifest emission, evidence closure, policy approval, review approval, rollback execution, validator implementation proof, release-runtime proof, public-surface permission, or published output.

## Expected PromotionDecision fixture families

| Scenario family | Expected posture | Notes |
|---|---|---|
| Complete synthetic `APPROVE` decision | Validation pass or release-readiness pass | Still not publication or ReleaseManifest. |
| Complete synthetic `DENY` decision | Validation pass or policy pass | Prior state is preserved. |
| Complete synthetic `ABSTAIN` decision | Validation pass or fail-closed posture | Used when context is insufficient, unresolved, stale, conflicted, or unsafe. |
| Missing evidence ref or unresolved EvidenceBundle ref | Validation failure, policy failure, `DENY`, or `ABSTAIN` | EvidenceBundle remains evidence authority. |
| Missing rollback support | Validation failure or release-readiness failure | Rollback readiness is a core invariant unless explicitly waived elsewhere. |
| Missing reviewer or ticket binding | Validation failure or review-required | Fixture does not replace ReviewRecord. |
| Invalid finite decision value | Validation failure | Release vocabulary is `APPROVE`, `DENY`, `ABSTAIN`. |
| Hydrology id convention failure | Validation failure where schema rule applies | Contract notes the hydrology-specific id pattern. |
| Extra property present | Validation failure where schema closes properties | Object shape remains bounded. |
| Superseding decision | Review-ready or expected output | New object supersedes old state without silent mutation. |
| Stable expected output | `../../golden/` | Deterministic expected output, not release. |

## Maintenance notes

- Update this README when release fixture parent documentation, payload files, validators, tests, helper scripts, expected-output names, schema decisions, policy rules, release storage paths, proof/receipt emitters, public-summary projections, or CI checks are added.
- Link each stable fixture to the exact schema check, policy check, release-readiness check, validator check, public-projection check, correction check, rollback check, documentation example, or governed release dry-run that consumes it.
- If a `fixtures/release/README.md` parent is created later, update the parent/child references together.
- If expected behavior stabilizes, update the paired input, expected output, consumer notes, and this lane index together.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes actual release decisions, proof material, receipt material, release material, source exports, lifecycle data, real reviewer data, restricted policy context, or sensitive source detail, move it out of this lane, quarantine it through the governed lifecycle or security process, and record the correction path.

## Verification status

- Target README: replaced blank placeholder content.
- Parent `fixtures/release/README.md`: NOT FOUND during this update.
- Fixture payload inventory: no payload files verified under this promotion-decision fixture lane during this update.
- Exact child-lane inventory under `fixtures/release/promotion_decision/`: NOT VERIFIED during this update.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Release contract README alignment: PARTIALLY VERIFIED against `contracts/release/README.md`.
- PromotionDecision contract alignment: PARTIALLY VERIFIED against `contracts/release/promotion_decision.md`.
- Schema/validator/policy alignment: NEEDS VERIFICATION against `schemas/contracts/v1/release/promotion_decision.schema.json`, `tools/validators/release/validate_promotion_decision.py`, `policy/promotion/`, and `policy/release/`.
- Consumer alignment: NEEDS VERIFICATION against validators, release dry-runs, policy checks, evidence-resolution checks, rollback checks, review checks, proof/receipt emission, public-summary projection, release-readiness checks, correction checks, rollback checks, schema checks, and CI implementation.
- Tests and validators: NOT RUN.

# PromotionDecision valid release fixtures

`fixtures/release/promotion_decision/valid/`

Status: draft / valid release fixture lane / synthetic PromotionDecision positive-path examples.

This directory is for small synthetic valid `PromotionDecision` fixture examples. Use it for toy promotion-gate cases that should pass schema validation, policy validation, evidence-resolution checks, rollback-readiness checks, review-binding checks, release-readiness checks, bounded public-summary checks, supersession checks, or CI dry-runs when paired with the appropriate validator and expected output.

These files are examples only. They are not actual PromotionDecision records, ReleaseManifests, RollbackCards, ReviewRecords, PolicyDecisions, EvidenceBundles, SourceDescriptors, RunReceipts, proof packs, release artifacts, public API material, public map material, public tiles, source authority, evidence authority, policy authority, proof authority, review authority, release authority, AI authority, or published artifacts.

## Valid fixture posture

Use this lane for synthetic release-promotion examples that demonstrate complete, bounded, positive-path `PromotionDecision` shapes. Expected outcomes may include validation pass, policy pass, release-readiness pass, review-ready, bounded-summary-safe, `APPROVE`, `DENY`, `ABSTAIN`, or a documented expected positive output.

A PromotionDecision fixture can imitate a complete decision object, but it does not approve or deny a real transition, publish a release, move a file, issue policy authority, satisfy evidence closure, execute rollback, or permit public serving by itself.

The PromotionDecision contract treats promotion as a governed state transition, not a file move, rename, merge, deployment, or UI action. `APPROVE` is positive-path release-transition vocabulary, but it still requires the full release process and does not publish anything by itself.

A fixture can describe desired valid behavior before validators, policy rules, release storage, schemas, proof/receipt emission, bounded-summary projection, separation-of-duties checks, or CI coverage exist. Fixture success is not implementation proof by itself.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, public API root, or publication root.

The parent PromotionDecision fixture README keeps this fixture family synthetic and non-authoritative. The root fixture README says `fixtures/` is for operational rendering inputs, not validator-only test data, and separates `fixtures/` from `tests/fixtures/`, `artifacts/`, and `data/`.

## Relationship to release governance

| Lane or document | Relationship |
|---|---|
| `../README.md` | Parent synthetic PromotionDecision fixture lane; this valid lane specializes positive-path examples. |
| `../invalid/README.md` | Sibling fail-closed lane for PromotionDecision cases that must be rejected or blocked. |
| `../../README.md` | Release fixture parent; not found during the parent README update, so this lane remains self-bounded. |
| `../../../../contracts/release/promotion_decision.md` | Semantic contract for `PromotionDecision`; valid fixtures do not define meaning. |
| `../../../../contracts/release/README.md` | Release contract-family README; fixtures do not store release objects or run gates. |
| `../../../../schemas/contracts/v1/release/promotion_decision.schema.json` | Machine-shape authority if present; fixtures do not define schemas. |
| `../../../../policy/promotion/` | Promotion policy home if present; fixtures do not decide admissibility. |
| `../../../../policy/release/` | Release policy home if present; fixtures do not decide release. |
| `../../../../release/` | Release artifact/process root if present; fixtures do not publish. |
| `../../../../data/proofs/` | Proof home if present; fixtures do not create proof authority. |
| `../../../../data/receipts/` | Receipt home if present; fixtures do not store actual receipts. |
| `../../../golden/README.md` | Top-level expected-output lane for stable synthetic expected outputs. |
| `../../../invalid/README.md` | Top-level fail-closed fixture lane for broad invalid examples. |

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.positive.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy valid `PromotionDecision` examples with all required fields, valid finite decision values, valid version, valid domain/run refs, resolvable toy evidence refs, toy EvidenceBundle URI refs, toy rollback refs, toy policy-bundle refs, toy review bindings, toy decision timestamps, and bounded summary projections;
- toy complete `APPROVE`, `DENY`, and `ABSTAIN` examples, where each outcome remains release-transition vocabulary and not runtime answer vocabulary;
- toy `APPROVE` examples that include evidence support, EvidenceBundle support, rollback support, policy-bundle identity, review binding, and release-readiness context while still not publishing anything;
- toy `DENY` or `ABSTAIN` examples that preserve prior state and show safe governed decision posture;
- toy supersession examples where a later decision emits a new object instead of silently mutating prior decision history;
- paired expected positive outputs in `../../../golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for actual PromotionDecision records, actual release decisions, release manifests, rollback cards, review records, policy decisions, EvidenceBundles, SourceDescriptors, RunReceipts, proof packs, receipts, lifecycle data, source exports, implementation code, release artifacts, public API material, public map material, public tiles, generated CI artifacts, source authority, evidence authority, policy authority, proof authority, review authority, release authority, AI authority, or published artifacts.

## Shared fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Use toy IDs, toy run refs, toy domains, toy evidence refs, toy EvidenceBundle refs, toy rollback refs, toy policy-bundle refs, toy review refs, toy timestamps, toy digests, and toy hashes.
- Make the valid condition explicit in the file name, payload, expected output, and consumer notes.
- Make expected outcome explicit when known: validation pass, policy pass, release-readiness pass, review-ready, bounded-summary-safe, `APPROVE`, `DENY`, `ABSTAIN`, or expected output.
- Keep schema validity, semantic validity, evidence closure, policy bundle identity, review binding, rollback readiness, lifecycle-boundary context, release-manifest relationship, proof/receipt emission, bounded-summary projection, correction posture, rollback posture, supersession state, and expected-output state separate.
- Pair each stable valid input with an expected positive output when practical.
- Do not treat fixture success as validator implementation proof, release-runtime proof, policy enforcement proof, review approval, EvidenceBundle closure, rollback execution, release publication, file movement, public-surface permission, or published output.

## Expected valid PromotionDecision fixture families

| Scenario family | Expected posture | Notes |
|---|---|---|
| Complete synthetic `APPROVE` decision | Validation pass or release-readiness pass | Still not publication or ReleaseManifest. |
| Complete synthetic `DENY` decision | Validation pass or policy pass | Prior state is preserved. |
| Complete synthetic `ABSTAIN` decision | Validation pass or fail-closed posture | Used when context is insufficient, unresolved, stale, conflicted, or unsafe. |
| Hydrology `APPROVE` with valid id convention | Validation pass where schema rule applies | Uses the schema-confirmed hydrology id pattern. |
| Resolvable toy evidence and EvidenceBundle refs | Validation pass or evidence-resolution pass | EvidenceBundle remains evidence authority. |
| Rollback support present | Release-readiness pass | Rollback readiness remains visible. |
| Reviewer and ticket binding present | Review-ready or validation pass | Fixture does not replace a full ReviewRecord. |
| Policy bundle identity present | Policy pass or review-ready | Policy bundle identity must remain auditable. |
| Bounded summary projection | Bounded-summary-safe | Summary is not release authority. |
| Superseding decision | Review-ready or expected output | New object supersedes old state without silent mutation. |
| Stable positive output is ready to compare | `../../../golden/` | Deterministic expected output, not release. |

## Maintenance notes

- Update this README when valid payload files, validators, tests, helper scripts, expected-output names, schema decisions, policy rules, release storage paths, proof/receipt emitters, bounded-summary projections, or CI checks are added.
- Link each valid fixture to the exact schema check, policy check, release-readiness check, validator check, projection check, correction check, rollback check, documentation example, or governed release dry-run that consumes it.
- If expected valid behavior stabilizes, update the paired input, expected output, consumer notes, parent README, sibling invalid README, and this valid index together.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes actual release decisions, proof material, receipt material, release material, source exports, lifecycle data, real reviewer data, restricted policy context, or sensitive source detail, move it out of this lane, quarantine it through the governed lifecycle or security process, and record the correction path.

## Verification status

- Target README: replaced blank placeholder content.
- Parent PromotionDecision fixture alignment: PARTIALLY VERIFIED against `fixtures/release/promotion_decision/README.md`.
- Sibling invalid alignment: PARTIALLY VERIFIED against `fixtures/release/promotion_decision/invalid/README.md`.
- Fixture payload inventory: no payload files verified under this valid lane during this update.
- Exact child-lane inventory under `fixtures/release/promotion_decision/valid/`: NOT VERIFIED during this update.
- Root fixture alignment: PARTIALLY VERIFIED against recent `fixtures/README.md` evidence from the parent update.
- PromotionDecision contract alignment: PARTIALLY VERIFIED against `contracts/release/promotion_decision.md`.
- Schema/validator/policy alignment: NEEDS VERIFICATION against `schemas/contracts/v1/release/promotion_decision.schema.json`, `tools/validators/release/validate_promotion_decision.py`, `policy/promotion/`, and `policy/release/`.
- Consumer alignment: NEEDS VERIFICATION against validators, release dry-runs, policy checks, evidence-resolution checks, rollback checks, review checks, proof/receipt emission, bounded-summary projection, release-readiness checks, correction checks, rollback checks, schema checks, and CI implementation.
- Tests and validators: NOT RUN.

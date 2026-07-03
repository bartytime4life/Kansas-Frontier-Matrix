# Release fixtures

`fixtures/release/`

Status: draft / release fixture parent index / synthetic release-governance examples.

This directory is the parent lane for small synthetic release-governance fixture examples. Use it to organize toy release-family cases for release object shape, promotion gates, finite release decisions, evidence refs, EvidenceBundle refs, rollback refs, policy-bundle refs, review bindings, bounded summary behavior, release-readiness checks, correction checks, rollback checks, supersession examples, governed release dry-runs, and documentation examples.

These files are examples only. They are not actual release objects, release decisions, release artifacts, EvidenceBundles, SourceDescriptors, RunReceipts, proof packs, receipts, public API material, public map material, public tiles, source authority, evidence authority, policy authority, proof authority, review authority, release authority, AI authority, or published artifacts.

## Fixture parent posture

Release fixtures support bounded checking and documentation for release-governance object families. A fixture may imitate a release object shape or expected validation result, but it must remain synthetic and must not be treated as release storage, proof material, policy approval, review approval, rollback execution, publication state, or public truth.

The release contract README defines `contracts/release/` as the semantic-contract lane for release objects. It also says contracts do not store releases, publish artifacts, run promotion gates, replace policy, replace schemas, write proofs or receipts, or serve public API/UI/AI surfaces. Release fixtures must preserve the same boundary.

A fixture can describe desired behavior before validators, policy rules, release storage, schemas, proof/receipt emission, bounded-summary projection, separation-of-duties checks, or CI coverage exist. Fixture success or failure is not implementation proof by itself.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, public API root, or publication root.

The root fixture README says `fixtures/` is for operational rendering inputs, not validator-only test data. It also separates `fixtures/` from `tests/fixtures/`, `artifacts/`, and `data/`, and says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here.

## Child lane inventory

The following child lanes have populated README coverage. This table is a navigation index, not proof that payload files, validators, tests, release stores, proof stores, receipt stores, policy bundles, summary projections, release manifests, or CI coverage exist.

| Child lane | Purpose | Expected posture |
|---|---|---|
| `promotion_decision/` | Synthetic PromotionDecision fixture family for promotion-gate shape, finite decision outcomes, evidence refs, EvidenceBundle refs, rollback refs, policy-bundle refs, review bindings, fail-closed behavior, supersession, bounded summary behavior, release-readiness checks, validator dry-runs, and documentation examples. | Valid, invalid, expected output, approve, deny, abstain, evidence-resolved, evidence-missing, rollback-ready, rollback-missing, policy-bound, policy-stale, review-bound, review-missing, release-ready, release-blocked, superseding, correction-visible, rollback-visible, or bounded-summary-safe. |
| `promotion_decision/valid/` | Synthetic positive-path PromotionDecision examples. | Validation pass, policy pass, release-readiness pass, review-ready, bounded-summary-safe, `APPROVE`, `DENY`, `ABSTAIN`, or expected output. |
| `promotion_decision/invalid/` | Synthetic fail-closed PromotionDecision examples. | Validation failure, policy failure, release-readiness failure, review-required, blocked projection, `DENY`, `ABSTAIN`, or expected failure output. |

## Relationship to release governance

| Lane or document | Relationship |
|---|---|
| `../README.md` | Root fixture rules; this release lane must remain synthetic and non-authoritative. |
| `promotion_decision/README.md` | PromotionDecision fixture family parent. |
| `promotion_decision/valid/README.md` | Positive-path PromotionDecision fixture lane. |
| `promotion_decision/invalid/README.md` | Fail-closed PromotionDecision fixture lane. |
| `../../contracts/release/README.md` | Release semantic-contract family; fixtures do not define meaning. |
| `../../contracts/release/promotion_decision.md` | PromotionDecision semantic contract; fixtures do not approve transitions. |
| `../../schemas/contracts/v1/release/` | Machine-shape authority if present; fixtures do not define schemas. |
| `../../policy/release/` | Release policy home if present; fixtures do not decide release. |
| `../../policy/promotion/` | Promotion policy home if present; fixtures do not decide admissibility. |
| `../../release/` | Release artifact/process root if present; fixtures do not publish. |
| `../../data/proofs/` | Proof home if present; fixtures do not create proof authority. |
| `../../data/receipts/` | Receipt home if present; fixtures do not store actual receipts. |
| `../golden/README.md` | Top-level expected-output lane for stable synthetic expected outputs. |
| `../invalid/README.md` | Top-level fail-closed fixture lane for broad invalid examples. |

## Accepted material

This parent lane and its child lanes may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.invalid.json`, `*.positive.json`, `*.negative.json`, `*.expected.json`, `*.golden.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy release-governance examples for release object shapes, promotion decisions, rollback support, evidence refs, EvidenceBundle refs, policy refs, review refs, proof/receipt refs, finite outcomes, bounded summaries, correction posture, rollback posture, and expected outputs;
- positive-path examples in child `valid/` lanes;
- fail-closed examples in child `invalid/` or `negative/` lanes;
- paired expected outputs in `../golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for actual release objects, actual release decisions, release artifacts, EvidenceBundles, SourceDescriptors, RunReceipts, proof packs, receipts, lifecycle data, source exports, implementation code, public API material, public map material, public tiles, generated CI artifacts, source authority, evidence authority, policy authority, proof authority, review authority, release authority, AI authority, or published artifacts.

## Shared fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Use toy IDs, toy run refs, toy domains, toy evidence refs, toy EvidenceBundle refs, toy rollback refs, toy policy-bundle refs, toy review refs, toy proof refs, toy receipt refs, toy timestamps, toy digests, and toy hashes.
- Make fixture posture explicit: valid, invalid, positive, negative, expected output, approve, deny, abstain, release-ready, release-blocked, evidence-resolved, evidence-missing, rollback-ready, rollback-missing, policy-bound, policy-stale, review-bound, review-missing, correction-visible, rollback-visible, superseding, or bounded-summary-safe.
- Make expected outcome explicit when known: validation pass, validation failure, policy pass, policy failure, release-readiness pass, release-readiness failure, review-ready, review-required, blocked projection, `APPROVE`, `DENY`, `ABSTAIN`, or expected output.
- Keep schema validity, semantic validity, evidence closure, policy bundle identity, review binding, rollback readiness, lifecycle-boundary context, release-manifest relationship, proof/receipt emission, bounded-summary projection, correction posture, rollback posture, supersession state, and expected-output state separate.
- Pair each stable input with an expected output when practical.
- Do not treat fixture success or failure as validator implementation proof, release-runtime proof, policy enforcement proof, review approval, EvidenceBundle closure, proof creation, receipt creation, rollback execution, release publication, file movement, public-surface permission, or published output.

## Expected release fixture families

| Scenario family | Preferred lane | Expected posture |
|---|---|---|
| PromotionDecision family | `promotion_decision/` | Synthetic release-transition fixture, not approval. |
| Complete positive-path PromotionDecision | `promotion_decision/valid/` | Validation pass, policy pass, release-readiness pass, or bounded expected output. |
| Fail-closed PromotionDecision | `promotion_decision/invalid/` | Validation failure, policy failure, review-required, `DENY`, or `ABSTAIN`. |
| Future release-object fixture | Future child lane if created | Synthetic release-shape example, not publication. |
| Stable release expected output | `../golden/` | Deterministic expected output, not release. |

## Maintenance notes

- Update this README when release fixture child lanes, payload files, validators, tests, helper scripts, expected-output names, schema decisions, policy rules, release storage paths, proof/receipt emitters, bounded-summary projections, or CI checks are added.
- Link each stable fixture to the exact schema check, policy check, release-readiness check, validator check, projection check, correction check, rollback check, documentation example, or governed release dry-run that consumes it.
- If expected behavior stabilizes, update the paired input, expected output, consumer notes, child README, and this parent index together.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes actual release decisions, proof material, receipt material, release material, source exports, lifecycle data, real reviewer data, restricted policy context, or sensitive source detail, move it out of this lane, quarantine it through the governed lifecycle or security process, and record the correction path.

## Verification status

- Target README: replaced blank placeholder content.
- Child README inventory: PARTIALLY VERIFIED against populated `promotion_decision/README.md`, `promotion_decision/valid/README.md`, and `promotion_decision/invalid/README.md` fetched during this update.
- Fixture payload inventory: no payload files verified under this release fixture parent during this update.
- Exact child-lane inventory under `fixtures/release/`: PARTIALLY VERIFIED by fetching the PromotionDecision child READMEs; no exhaustive tree listing was performed.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md` from recent preceding updates.
- Release contract README alignment: PARTIALLY VERIFIED against `contracts/release/README.md`.
- PromotionDecision fixture alignment: PARTIALLY VERIFIED against `fixtures/release/promotion_decision/README.md`.
- PromotionDecision valid/invalid alignment: PARTIALLY VERIFIED against sibling child READMEs.
- Schema/validator/policy alignment: NEEDS VERIFICATION against release schemas, release validators, `policy/release/`, and `policy/promotion/`.
- Consumer alignment: NEEDS VERIFICATION against validators, release dry-runs, policy checks, evidence-resolution checks, rollback checks, review checks, proof/receipt emission, bounded-summary projection, release-readiness checks, correction checks, rollback checks, schema checks, and CI implementation.
- Tests and validators: NOT RUN.

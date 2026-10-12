# GateOutcomeMapping source and adaptation map

## Status

**PROPOSED_INACTIVE.** This packet turns Pass 22 card `KFM-P22-PROG-0012` into deterministic fixture infrastructure. It does not adopt the source atlas as repository authority and does not perform promotion, answer generation, policy evaluation, release, deployment, or publication.

## Source candidate

- Attachment: `KFM_Pass_22_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf`
- Stable card: `KFM-P22-PROG-0012`
- Source statement: map passing gates to promotion or answer, failing gates to denial, insufficient evidence to abstention, and execution failures to error; do not allow free-form outcomes.
- Source dependencies: `EvidenceBundle`, `RunReceipt`, and `PolicyDecision`.

The source atlas describes itself as a downstream carrier and leaves repository implementation unverified. This adaptation therefore uses the current repository as the authority for existing contract vocabulary and path placement.

## Current repository evidence used

| Evidence | Observed role | Adaptation consequence |
|---|---|---|
| `contracts/runtime/decision_envelope.md` and paired schema | Runtime outcomes are `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`. | The answer lane maps directly to `DecisionEnvelope`. |
| `contracts/release/promotion_decision.md` and paired schema | Promotion decisions use `APPROVE`, `DENY`, `ABSTAIN`. | Source `PROMOTE` is represented as `APPROVE`, avoiding a second release vocabulary. |
| Accepted `docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md` | Responsibility-root placement is adopted. | The profile uses existing governance contract/schema/validator/fixture roots. |
| `packages/hashing` | Repository-owned deterministic `spec_hash` implementation. | Mapping identity reuses existing hashing rather than inventing a profile. |

## Deliberate boundary

A `GateOutcomeMapping` is a translation candidate, not the translated object. The validator never emits a `PromotionDecision` or `DecisionEnvelope`. A later integration must separately validate the destination contract, evidence closure, policy decision, review state, release state, correction path, and rollback target.

## Future integration conditions

A later reviewed slice may add adapters only after it proves:

1. exact destination-schema construction;
2. EvidenceRef-to-EvidenceBundle resolution;
3. policy and sensitivity checks;
4. review and release-state binding for promotion;
5. citation obligations for answers;
6. safe error handling where `PromotionDecision` has no `ERROR` member; and
7. correction and rollback propagation.

## Non-effects

No source is activated; no gate is executed; no evidence or policy is resolved; no decision object is emitted; no lifecycle state, release state, deployment, publication, or public-use authority is changed.

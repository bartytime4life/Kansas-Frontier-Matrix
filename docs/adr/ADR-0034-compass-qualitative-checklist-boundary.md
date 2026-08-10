<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://adr/ADR-0034
title: Keep COMPASS qualitative and subordinate to KFM authority gates
type: adr
version: v1
status: proposed
owners: ["Architecture steward", "Evidence steward", "Policy steward", "Release steward"]
created: 2026-08-10
updated: 2026-08-10
policy_label: public
owning_root: docs/
responsibility: proposed cross-component boundary for using the Living Compass COMPASS questions as an optional planning checklist without scoring, workflow, policy, review, promotion, release, or publication authority
truth_posture: CONFIRMED governed source map and repository responsibility inventory / PROPOSED qualitative checklist boundary / UNKNOWN adopted consumer and scoring value / NEEDS VERIFICATION owner review and any later evaluation design
related:
  - "docs/doctrine/directory-rules.md"
  - "docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md"
  - "docs/intake/exploratory/kfm-living-compass-working-edition-1-0-source-map.md"
  - "contracts/evidence/evidence_bundle.md"
  - "contracts/policy/policy_decision.md"
  - "contracts/release/release_manifest.md"
  - "contracts/release/rollback_card.md"
tags: [adr, kfm, compass, planning, qualitative-checklist, evidence, policy, rollback, governance]
supersedes: []
superseded_by: []
notes:
  - "PROPOSED: COMPASS remains an optional planning aid; this record creates no score, threshold, workflow, template, automation, review decision, promotion, release, deployment, or publication authority."
  - "The private Drive source identity remains omitted in accordance with its governed source-map disclosure boundary."
[/KFM_META_BLOCK_V2] -->

# ADR-0034: Keep COMPASS qualitative and subordinate to KFM authority gates

KFM should permit the Living Compass `COMPASS` dimensions as an optional qualitative question set for comparing already-qualified ideas. It should not compute or persist a total, define a threshold, or let novelty, user value, architecture leverage, or smallness compensate for unresolved authority, evidence, rights, sensitivity, policy, review, correction, or rollback requirements.

| Field | Value |
|---|---|
| **ID** | ADR-0034 |
| **Status** | proposed |
| **Date** | 2026-08-10 |
| **Deciders** | Architecture steward · Evidence steward · Policy steward · Release steward |
| **Consulted** | Product/experience · domain · source · rights/sensitivity · validation · correction/rollback stewards |
| **Informed** | Contributor · issue/PR author · governed-API · map-client · documentation maintainers |
| **Supersedes** | — |
| **Superseded by** | — |
| **Directory Rules trigger** | `n/a — non-structural cross-component decision`; invariant-preserving boundary under §§2, 3, 4, and 6 |
| **Primary responsibility root** | `docs/` |
| **Migration required** | no |
| **Rollback required** | yes, documentation-only |
| **Truth posture** | CONFIRMED source/repository inventory · PROPOSED checklist boundary · UNKNOWN adopted consumer or scoring value |

---

## 1. Context

The governed source map for *KFM Living Compass Working Edition 1.0* identifies one novel decision candidate: the `COMPASS` rubric—Claim clarity, Observable value, Material evidence, Policy readiness, Architecture leverage, Smallness, and Safe reversal. The source presents a 0–4 scale and total as a prioritization aid while also stating a non-compensable rule: a high total cannot turn a held or denied candidate into permission to proceed.

The source map recommends a decision-only crosswalk before adding a score, workflow, template, or automation. It warns that a total can conceal a failed evidence, rights, sensitivity, policy, review, or rollback gate. Current KFM already assigns those responsibilities to separate contracts, policy, reviewers, lifecycle decisions, and release records. A new rubric must not become a parallel authority surface.

### 1.1 Decision drivers

- **Preserve useful questions.** The seven dimensions can expose why an idea is attractive, weak, or incomplete.
- **Keep hard gates visible.** Evidence, rights, sensitivity, policy, review, correction, and rollback are not weights in a sum.
- **Avoid a second decision vocabulary.** COMPASS cannot replace placement, validation, policy, promotion, release, or public-answer outcomes.
- **Prevent planning artifacts from self-authorizing.** A completed checklist proves only that questions were answered, not that the answers are correct or approved.
- **Stay reversible.** A qualitative documentation boundary can be removed without migrating data, settings, runtime, or consumers.

### 1.2 Confirmed repository boundary

The repository already separates the responsibilities that COMPASS asks about:

| Existing responsibility | Current owner surface | Why COMPASS cannot replace it |
|---|---|---|
| Placement and architecture authority | [`docs/doctrine/directory-rules.md`](../doctrine/directory-rules.md) and accepted ADRs | A planning answer cannot create or move a canonical responsibility root. |
| Source identity, role, rights, and sensitivity inputs | [`contracts/source/source_descriptor.md`](../../contracts/source/source_descriptor.md) and source/policy owners | A claim that evidence is “material” cannot admit a source or resolve its terms. |
| Claim support | [`contracts/evidence/evidence_bundle.md`](../../contracts/evidence/evidence_bundle.md) and evidence reviewers | A checklist cannot resolve evidence or turn synthetic support into real-world truth. |
| Policy result | [`contracts/policy/policy_decision.md`](../../contracts/policy/policy_decision.md) and policy owners | “Policy readiness” is not an allow decision. |
| Human review | [`schemas/contracts/v1/governance/review_record.schema.json`](../../schemas/contracts/v1/governance/review_record.schema.json) and named reviewers | A rubric author cannot approve their own evidence, policy, or release posture. |
| Promotion and release | [`contracts/release/promotion_decision.md`](../../contracts/release/promotion_decision.md) and [`contracts/release/release_manifest.md`](../../contracts/release/release_manifest.md) | Planning priority cannot move lifecycle state or create a release. |
| Correction and reversal | [`contracts/correction/correction_notice.md`](../../contracts/correction/correction_notice.md) and [`contracts/release/rollback_card.md`](../../contracts/release/rollback_card.md) | Saying reversal is practical does not prove a tested correction or rollback target. |

The repository also contains purpose-specific scorecards and ranking objects. They do not establish a generic COMPASS consumer, and this ADR does not change or reinterpret them.

### 1.3 Evidence boundary

- **CONFIRMED:** the private Drive document was reviewed through the governed source map and directly in the authorized Drive session; its disclosure boundary omits provider identity from repository artifacts.
- **CONFIRMED:** no exact COMPASS rubric, workflow, schema, or automation was found in the bounded current-repository search.
- **CONFIRMED:** KFM has separate authority owners for placement, source, evidence, policy, review, promotion, release, correction, and rollback.
- **PROPOSED:** permit the crosswalk in §2 as an optional qualitative planning aid.
- **UNKNOWN:** whether a numeric score would improve idea selection, repeatability, or outcomes.
- **NEEDS VERIFICATION:** an actual consumer, owner, evaluation question, measurement design, and failure analysis before scoring is reconsidered.

### 1.4 Out of scope

This ADR does not add a checklist file, form, issue template, score, threshold, schema, fixture, validator, workflow, automation, dashboard, source, policy rule, review record, promotion decision, release, deployment, or publication path. It does not adopt the Living Compass's timeboxes, mission portfolio, or finite vocabularies as KFM lifecycle or authority.

---

## 2. Decision

> **Decision:** Use `ADOPT_QUALITATIVE_CHECKLIST` as the proposed boundary for qualified planning work. Preserve `RETAIN_AS_QUESTIONS` for informal discovery, defer `EVALUATE_SCORING` until a separate evidence-bearing study is authorized, and apply `DENY_AUTHORITY_EFFECTS` to any attempt to use COMPASS to grant or override source, evidence, policy, review, promotion, release, deployment, publication, or public-use authority.

### 2.1 Finite routing outcomes

| Outcome | Meaning | Permitted effect |
|---|---|---|
| `RETAIN_AS_QUESTIONS` | The dimensions help discussion, but no stable consumer or review need justifies a structured checklist. | Ask the questions in planning prose; create no new object, status, score, or gate. |
| `ADOPT_QUALITATIVE_CHECKLIST` | A bounded experiment or change benefits from recording each dimension and its unresolved dependencies. | Use an optional human-readable crosswalk subordinate to the owning artifacts and reviewers. No total, threshold, or authority effect. |
| `EVALUATE_SCORING` | A named planning consumer and testable research question could justify studying numeric scoring. | Propose a separate, no-authority evaluation with historical/synthetic cases, inter-rater analysis, failure modes, and rollback. This ADR does not authorize it. |
| `DENY_AUTHORITY_EFFECTS` | COMPASS is used to admit a source, resolve evidence, make policy, approve review, promote, release, deploy, publish, or override a failed gate. | Stop the use, preserve the independent gate result, and route the missing responsibility to its owner. |

These outcomes route use of the planning aid only. They are not canonical runtime, policy, validation, placement, promotion, release, or public-answer outcomes.

### 2.2 Dimension-to-owner crosswalk

| Letter | Qualitative question | Owning artifact or reviewer | Gate posture | Non-claim |
|---|---|---|---|---|
| `C` — Claim clarity | What exact claim, question, place, time, and limitation are in scope? | Semantic contract or decision record; domain and evidence stewards | Unresolved scope means **hold or split the planning candidate**; it cannot be averaged away. | Does not establish truth or support. |
| `O` — Observable value | What can a named user understand, inspect, or decide at an identified governed surface? | Product/domain owner; relevant API, Evidence Drawer, map, export, or Focus Mode documentation | Comparative planning signal, not an authority gate. | Does not prove demand, usability, accessibility, or release fitness. |
| `M` — Material evidence | Which admitted source roles and EvidenceBundle inputs support the bounded claim? | SourceDescriptor and EvidenceBundle owners; source/evidence reviewers | **Hard dependency** for consequential claims; missing or synthetic-only support remains visible. | Does not admit a source, resolve evidence, or upgrade synthetic data. |
| `P` — Policy readiness | Which rights, sensitivity, audience, public-safe transform, and finite policy result apply? | Rights/sensitivity and policy owners; PolicyDecision | **Hard dependency** before consequential use; “ready” is not `ALLOW`. | Does not evaluate or override policy. |
| `A` — Architecture leverage | Which existing trust object or governed interface becomes more reusable? | Architecture steward; Directory Rules and relevant accepted ADRs | Comparative planning signal only. | Does not justify a new root, parallel object, or invariant change. |
| `S` — Smallness | Is the slice bounded, dependency-closed, fixtureable, testable, and reversible within its change budget? | Implementation owner and validation reviewer | May route to hold or split; short duration never excuses a missing responsibility. | Does not prove completeness, quality, or safety. |
| `S` — Safe reversal | What correction, supersession, withdrawal, rollback, cache/export propagation, and owner exist? | Correction and release stewards; CorrectionNotice, ReleaseManifest, RollbackCard | **Hard dependency** before promotion/release; a proposed plan is not a rehearsed rollback. | Does not create correction or release authority. |

The Authority Freeze precedes this checklist. Current repository bytes, effective Directory Rules, accepted ADRs, active PRs/branches, write freezes, and the exact requested authority must be checked before COMPASS is used.

### 2.3 Non-compensable rule

COMPASS **MUST NOT** produce an aggregate total under this proposed decision. Even if a later evaluation studies scores:

- an unresolved placement or accepted-ADR conflict cannot be offset;
- missing source rights, sensitivity, or EvidenceBundle support cannot be offset;
- a policy denial, abstention, or error cannot be offset;
- missing required human review cannot be offset;
- missing correction, withdrawal, or rollback readiness cannot be offset; and
- release, deployment, publication, and public use still require their own authority.

No label such as “strong,” “ready,” “high leverage,” or “small” may be translated into permission outside the planning context.

### 2.4 Synthetic no-network example

Consider a wholly synthetic proposal: one public-safe HUC12 fixture should open an Evidence Drawer that demonstrates a cited answer plus abstain, deny, and error states.

| Dimension | Illustrative answer | Independent consequence |
|---|---|---|
| Claim clarity | One fixture, one watershed identifier, one synthetic statement, one inspection interaction. | Planning scope is narrow enough to review. |
| Observable value | A user can inspect why the synthetic statement answered or failed. | Value is plausible but not user-tested. |
| Material evidence | Synthetic SourceDescriptor and EvidenceBundle-shaped references only. | Sufficient for fixture design; **not** support for a real Kansas claim. |
| Policy readiness | No evaluated production PolicyDecision. | Public or operational use remains blocked regardless of other answers. |
| Architecture leverage | Reuses existing EvidenceBundle, governed-interface, and Evidence Drawer boundaries. | Helpful comparison signal; grants no placement authority. |
| Smallness | One no-network fixture with finite positive and negative behavior. | Appropriate experiment size if its dependencies are closed. |
| Safe reversal | Ordinary fixture revert is clear; no release rollback rehearsal exists. | Experiment rollback is bounded; promotion/release remains blocked. |

The qualitative result is `ADOPT_QUALITATIVE_CHECKLIST` for planning the synthetic experiment. There is no total. The example cannot support a real claim, policy allow, review approval, promotion, release, deployment, or publication.

### 2.5 Requirements for any later scoring evaluation

A future `EVALUATE_SCORING` proposal **MUST** identify:

1. one named planning consumer and decision whose quality might improve;
2. why qualitative questions are insufficient;
3. a pinned rubric version and independent hard-gate model;
4. historical or synthetic cases without sensitive or private content;
5. inter-rater reliability, calibration, missing-answer, gaming, and high-total/failed-gate tests;
6. evidence that the score does not alter canonical statuses or authority;
7. retention, correction, versioning, and rollback behavior; and
8. an explicit stop condition if the score adds noise, false confidence, bias, or process burden.

The evaluation must remain outside production policy, merge protection, promotion, release, and publication until a later accepted decision says otherwise.

### 2.6 Placement basis

| Question | Answer |
|---|---|
| **Primary responsibility** | Cross-component planning boundary and authority non-effect |
| **Owning root** | `docs/adr/` |
| **Domain segment** | `n/a — cross-domain` |
| **Lifecycle phase** | `n/a`; this record creates no data object or transition |
| **Directory Rules basis** | §§2, 3, 4, and 6: Authority Freeze, responsibility separation, governed interfaces, evidence, policy-aware defaults, and reversible change |
| **Parallel authority risk** | Mitigated by mapping each question back to existing owners and forbidding totals, thresholds, and authority effects |

### 2.7 Conformance language

- COMPASS **MUST** remain subordinate to current repository evidence, accepted ADRs, Directory Rules, contracts, policy, reviewers, promotion, release, correction, and rollback authority.
- A structured use under this decision **MUST** record qualitative answers and unresolved dependencies without an aggregate total.
- Hard dependencies in §2.2 **MUST NOT** be compensated by another dimension.
- A checklist **MUST NOT** claim implementation, validation, evidence closure, policy permission, review approval, promotion, release, deployment, publication, or public-use fitness.
- Contributors **SHOULD** use the existing task/PR contract when it already captures the same questions instead of creating duplicate paperwork.
- A team **MAY** retain the questions informally when a structured checklist adds no value.

---

## 3. Consequences

### 3.1 Positive

- Preserves the Living Compass's memorable questions without creating a parallel gate system.
- Makes weak evidence, policy, and rollback dependencies harder to hide behind attractive features.
- Supports comparing bounded ideas while keeping current owners visible.
- Avoids premature schema, workflow, automation, dashboard, and issue-template maintenance.

### 3.2 Negative

- Produces no single number for ranking a large idea portfolio.
- Qualitative answers may vary across reviewers and require discussion.
- Contributors must still inspect multiple owning artifacts rather than relying on one rubric.

### 3.3 Accepted tradeoffs

KFM accepts less ranking convenience in exchange for transparent dependencies, separation of duties, and reduced false confidence. The questions may improve planning, but they cannot shortcut the work they point to.

### 3.4 Affected surfaces

| Surface | Impact |
|---|---|
| ADRs | Adds this proposed, non-binding decision record and index row. |
| Planning | Defines an optional qualitative crosswalk if the ADR is later accepted. |
| Contracts, schemas, policy, tests, workflows | Not changed; no COMPASS object or automation is created. |
| Sources, data, lifecycle, review | Not changed; no authority or transition is granted. |
| Release, runtime, and public clients | Not changed; no deployment or publication effect. |

---

## 4. Alternatives considered

### 4.1 Adopt the 0–4 scores and total now

- **Summary:** Implement the source rubric directly and rank qualified ideas by their total.
- **Why rejected:** No consumer study, calibration, inter-rater evidence, gaming analysis, or failure-mode proof exists; a total can conceal non-compensable gaps.

### 4.2 Reject COMPASS entirely

- **Summary:** Keep only existing task contracts and authority gates.
- **Why rejected:** The seven questions are a useful synthesis for early planning and can expose missing owners without changing authority.

### 4.3 Make COMPASS a required PR template

- **Summary:** Add required fields and a workflow check to every pull request.
- **Why rejected:** No evidence shows all PR classes need this rubric. It would duplicate existing task-contract material and turn a planning aid into process policy.

### 4.4 Let individual teams choose scores and thresholds

- **Summary:** Permit local adaptations without a repository-wide decision.
- **Why rejected:** Multiple unversioned scales would create drift, incomparable results, and opportunities to mistake planning scores for permission.

### 4.5 Keep the idea only in exploratory intake

- **Summary:** Preserve the source map and make no decision boundary.
- **Why rejected:** The rubric is compact and implementation-shaped. An explicit non-authority crosswalk prevents accidental transfer while retaining its useful questions.

---

## 5. Evidence and references

- [`docs/intake/exploratory/kfm-living-compass-working-edition-1-0-source-map.md`](../intake/exploratory/kfm-living-compass-working-edition-1-0-source-map.md) — full-source reconciliation, current-state correction, COMPASS decision candidate, non-compensable risk, and recommended bounded action.
- *KFM Living Compass Working Edition 1.0* — private Google Drive DOCX reviewed in the authorized Drive session; provider identity and direct link intentionally omitted from repository artifacts per the governed source-map boundary.
- [`docs/doctrine/directory-rules.md`](../doctrine/directory-rules.md) — Authority Freeze, responsibility roots, lifecycle law, governed interfaces, evidence, policy-aware defaults, and reversible change.
- [`docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md`](./ADR-0029-adopt-directory-governance-standard-v2.md) — accepted placement authority.
- [`contracts/evidence/evidence_bundle.md`](../../contracts/evidence/evidence_bundle.md), [`contracts/policy/policy_decision.md`](../../contracts/policy/policy_decision.md), [`contracts/release/promotion_decision.md`](../../contracts/release/promotion_decision.md), [`contracts/release/release_manifest.md`](../../contracts/release/release_manifest.md), and [`contracts/release/rollback_card.md`](../../contracts/release/rollback_card.md) — existing responsibility owners that a planning rubric cannot replace.

No numeric-scoring, prioritization-quality, inter-rater, productivity, or user-value claim is adopted. Those remain `UNKNOWN` or `NEEDS VERIFICATION` until a separately authorized evaluation produces evidence.

---

## 6. Migration plan

Not applicable. This proposed record adds no COMPASS object, score, stored status, workflow, template, dependency, or consumer. If later accepted, existing task and PR contracts may reference the qualitative questions without migrating historical work.

---

## 7. Rollback plan

Before merge, close the pull request and delete only its scoped branch if desired. After merge, reject or supersede this ADR through normal ADR governance and update `docs/adr/INDEX.md` in the same reviewed change. Revert or supersede the paired generated authoring receipt according to receipt-retention policy. No source, data, setting, workflow, runtime, review, release, deployment, or public artifact requires rollback.

---

## 8. Open questions

- Which contributor or review context, if any, needs a structured COMPASS checklist beyond the current task/PR contract?
- What evidence would show that qualitative questions improve idea selection or reduce incomplete slices?
- Which hard-gate references should be mandatory if a future worksheet exists, without duplicating their contents?
- Can inter-rater disagreement be useful planning evidence rather than something to hide with an average?
- What failure or burden threshold should end a future scoring experiment?

---

## 9. Change history

| Date | Status | Change | PR |
|---|---|---|---|
| 2026-08-10 | proposed | Initial decision-only crosswalk from the governed Living Compass Drive source and current KFM responsibility inventory. | pending |

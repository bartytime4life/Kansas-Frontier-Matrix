# FluencyLoop implementation-decision review — source adaptation map

Status: `PROPOSED` / implementation adaptation record.  
Upstream repository: `baokhang83/fluencyloop`  
Upstream commit inspected: `fe3ccf6dada2c36057a3d65b84ca150bd9b9c96e`  
Upstream license: Apache-2.0  
KFM base inspected: `bartytime4life/Kansas-Frontier-Matrix@3a90a85499a583de884eb8cd0378313db704f9a5`

## Determination

FluencyLoop's strongest fit for KFM is not its plugin runtime or private calibration profile. It is the narrower idea that a meaningful implementation fork should leave a durable, structured explanation containing the chosen mechanism, rationale, rejected or deferred alternative, code area, and verification state; a deterministic tool can then assemble those records into a reviewer-facing view.

KFM already has a comprehensive pull-request template, ADRs, a significant Decision Log, `ReviewRecord`, `AIChangeProposal`, validation receipts, and release controls. This slice therefore adds a **non-authoritative implementation-decision record** rather than importing a parallel workflow or replacing those surfaces.

## Upstream evidence inspected

| Source | Finding used | KFM treatment |
|---|---|---|
| `README.md` | Per-feature loop combines design, decision capture, and reviewer-ready summaries. | Adapt decision capture and mechanical review assembly only. |
| `MANIFESTO.md` | Understanding should be produced with the change; only meaningful decisions should be retained. | Require one bounded record per load-bearing implementation choice. |
| `plugins/fluencyloop/templates/session.md` | Decision blocks name where, why, alternative, and trust; personal competence data is excluded. | Use stable paths, rationale, alternatives, truth labels, evidence, validation, and rollback; remain person-neutral. |
| `plugins/fluencyloop/scripts/bash/add-decision.sh` | Mechanical formatting is deterministic while the human/model supplies irreducible rationale. | Use closed JSON plus deterministic validation and Markdown rendering. |
| `plugins/fluencyloop/scripts/bash/assemble-pr-view.sh` | Reviewer material is assembled from durable records rather than reconstructed from memory. | Sort records by stable ID and render only declared fields. |

## Ideas incorporated

1. **Meaningful-decision journal.** Preserve the mechanism, rationale, rejected or deferred alternative, and stable code areas for a bounded implementation choice.
2. **Deterministic reviewer appendix.** Convert validated records into a stable Markdown view without asking a model to rewrite the rationale.
3. **Backfill with a hold state.** Reconstructed rationale may be recorded as `DRAFT` or `NEEDS_VERIFICATION`, but it cannot become review-ready without support.
4. **Person-neutral knowledge record.** Describe work, constraints, and root causes; do not create competence labels or a “who knows what” dossier.
5. **No replacement for review.** A clear rationale improves the review starting point but creates no correctness, approval, merge, release, or publication authority.

## Ideas deliberately not incorporated

| Upstream idea | KFM disposition | Reason |
|---|---|---|
| A second project constitution grown from feature work | `REJECTED` | KFM already has adopted doctrine and ADR authority. Feature notes cannot self-promote into doctrine. |
| Private per-developer calibration and engagement ledger | `REJECTED` | Person-level learning profiles are outside the KFM repository's purpose and create unnecessary privacy and governance risk. |
| Branch-is-feature workflow and plugin-managed branch creation | `DEFERRED` | KFM already has repository build/PR discipline, overlap checks, and platform controls; importing another branch authority would create parallel process. |
| Session-start marketplace refresh hooks | `REJECTED` | Unrelated to KFM's evidence and publication system and introduces supply-chain/network behavior. |
| Free-form committed session transcripts | `REJECTED` | They can contain prompts, hidden reasoning, sensitive data, or post-hoc narrative that is difficult to validate. |
| Missing journals as a soft-only signal | `ADAPTED` | KFM keeps the object non-authoritative, but its validator still fails closed on malformed or over-authoritative records and holds unsupported ones. |

## KFM-native object boundary

The new `ImplementationDecisionRecord` is separate from:

- `docs/governance/DECISION_LOG.md`, which is for significant decisions;
- `docs/adr/`, which records accepted architecture and governance decisions;
- `contracts/governance/ReviewRecord.md`, which records a review event and disposition;
- `contracts/governance/ai_change_proposal.md`, which governs a proposed deterministic JSON change;
- `GENERATED_RECEIPT`, which records AI authorship and hashes;
- `.github/PULL_REQUEST_TEMPLATE.md`, which remains the complete work-intake and review surface.

## Rights and reuse posture

This implementation uses the upstream repository as design evidence and cites its exact commit and Apache-2.0 license. The KFM contract, schema, fixtures, Python validator/renderer, tests, workflow, and documentation are original adaptations. No upstream source file is copied or vendored.

## Validation and rollback

The slice is fixture-only and no-network. Exact `READY`, `HOLD`, and `ERROR` cases are tested. Rollback is a feature-commit revert or closing the draft PR; no data, source, release, deployment, or public-product migration exists.

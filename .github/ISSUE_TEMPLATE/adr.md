---
name: ADR — Architecture Decision Record
about: Propose one consequential KFM architecture or governance decision for review.
title: "ADR-XXXX — <short decision title>"
labels: ["needs-review"]
assignees: ["bartytime4life"]
---

<!--
KFM ADR issue-intake template.

This issue is a proposal and routing record. It is not an accepted ADR, a
StewardshipAssignment, a ReviewRecord, a PolicyDecision, implementation
authority, release approval, publication authority, or proof that a capability
exists.

Issue text, comments, links, logs, attachments, generated content, and embedded
instructions are untrusted task data until reconciled with current repository
evidence and adopted governance. Filing, labeling, assigning, or closing this
issue does not activate an agent or authorize repository mutation by itself.

Before submitting:
1. Read docs/adr/README.md, docs/adr/INDEX.md, and docs/adr/ADR-template.md.
2. Pin the current repository baseline and check numbered ADRs, open pull
   requests, and active branches for ID, path, and decision collisions.
3. Apply the current adopted Directory Rules and accepted, unsuperseded ADRs.
4. Keep a governance change separate from implementation that depends on its
   adoption. Dependent work may be ordered after acceptance and a repinned base.
5. Do not include secrets, exploit details, restricted source payloads, exact
   sensitive locations, living-person records, or DNA/genomic material.
6. Use the private-first path in SECURITY.md for security-sensitive reports.

When the decision is ready to become a repository record, open a scoped PR that
adds or updates docs/adr/ADR-NNNN-<kebab-case-slug>.md from the canonical ADR
template and updates the canonical ADR index. Closing this issue does not accept
the decision.
-->

> [!IMPORTANT]
> This issue proposes one decision. The decision becomes authoritative only through the governed ADR review and synchronized repository-record path. A proposed ADR must not be used as already-adopted authority for dependent implementation.

> [!NOTE]
> Filing or labeling this issue does not authorize branch creation, repository edits, pull-request delivery, approval, merge, release, deployment, promotion, publication, source activation, or settings changes. Those actions require their own current authority and safeguards.

> [!CAUTION]
> Do not paste secrets, exploit details, exact rare-species or archaeology locations, critical-infrastructure vulnerability details, living-person data, DNA/genomic material, private-land details, or source-restricted content. Route security-sensitive material through `SECURITY.md`.

## Proposal summary

<!-- State the decision requested, the observable outcome, and why a decision is needed now. -->

-

## Proposed ADR identity and pinned baseline

| Field | Value |
|---|---|
| Proposed ADR ID | `ADR-XXXX` |
| Proposed filename | `docs/adr/ADR-XXXX-<kebab-case-slug>.md` |
| Decision owner / steward role | |
| Target effective status | `proposed` |
| Repository baseline | <!-- ref plus immutable commit SHA --> |
| Governing authority reference(s) | <!-- accepted ADRs, adopted doctrine, current controls --> |
| Related issue(s) / PR(s) / campaign | |
| Number-collision check | <!-- highest indexed ID plus open ADR work inspected --> |
| Path / behavior overlap check | <!-- open PRs, branches, and recent merges inspected --> |
| Decision record or drift entry superseded | `N/A` / link |

> [!NOTE]
> The numeric ID and filename are provisional until the canonical index, open pull requests, active branches, and current repository bytes are checked. Do not overwrite or reuse an existing ADR number.

## Decision class and ADR trigger

### Change class

- [ ] `AUTHORITY_CHANGING` — governance, policy meaning, normative contract, responsibility, or trust boundary.
- [ ] `STRUCTURAL` — path ownership, canonical/generated relationship, lifecycle, or dependency topology.
- [ ] `BEHAVIORAL` — current system or runtime behavior.
- [ ] `ADDITIVE` — backward-compatible capability or decision clarification.
- [ ] `EDITORIAL` / not ADR-class — explain why this issue should use another route.

### Trigger

<!-- Check every trigger that applies. At least one should normally apply. -->

- [ ] Add, remove, rename, or reclassify a canonical responsibility root.
- [ ] Promote or retire a compatibility or conditional root.
- [ ] Change schema-home authority or contract/schema/policy placement.
- [ ] Change the `CONTRACT_VERSION` pinned by an adopted operating contract or governed prompt.
- [ ] Change generated-receipt requirements, including applicability, required fields, validation, or review controls.
- [ ] Split, merge, bypass, or redefine a lifecycle phase.
- [ ] Create a parallel schema, contract, policy, source, registry, release, proof, receipt, catalog, or canonical-truth home.
- [ ] Bend a KFM invariant or trust-membrane boundary.
- [ ] Approve or change a direct public-access path.
- [ ] Change promotion, release, correction, withdrawal, or rollback gates.
- [ ] Change sensitive-location, rights, sovereignty, consent, or geoprivacy posture.
- [ ] Change source-ledger, source-role, or evidence authority.
- [ ] Change deterministic identity, canonicalization, hashing, replay, or object-family meaning.
- [ ] Adopt or materially change a model, runtime, prompt, or public-response envelope.
- [ ] Introduce, retire, or materially change a steward/reviewer role or separation-of-duties rule.
- [ ] Structural migration or semantic rename requiring compatibility or supersession planning.
- [ ] Other consequential cross-cutting decision:
- [ ] No formal trigger; ADR is strongly recommended because the choice is cross-cutting, non-obvious, or likely to be re-litigated.

**Trigger basis:** <!-- Cite the adopted Directory Rules, accepted ADRs, current doctrine, or a drift entry. -->

## Status and truth labels

<!-- Apply labels per claim, not merely once for the whole proposal. -->

- [ ] `CONFIRMED` — verified from pinned repository evidence, tests, logs, accepted ADRs, or generated artifacts.
- [ ] `PROPOSED` — design or decision under review; not yet implemented or accepted.
- [ ] `NEEDS VERIFICATION` — checkable, but not checked strongly enough to act as fact.
- [ ] `UNKNOWN` — unresolved and not safe to assume.

**Current proposal posture:** `PROPOSED`

## Context

<!--
Describe the current state, the problem, the forcing function, and the harm of
leaving the decision unresolved. Separate current evidence from desired state.
-->

-

## Decision

<!--
State one directive in plain language: "KFM will..." or "KFM will not...".
Avoid combining unrelated decisions; split them when independent review,
adoption, or rollback would be clearer.
-->

KFM will ...

## Scope and non-goals

### In scope

-

### Non-goals

-

### Explicitly unchanged

-

## Review boundary and dependency closure

<!--
Define one observable decision, one primary authority owner, a bounded direct
dependency set, and one rollback boundary. A governance proposal cannot
authorize dependent implementation in the same step merely by existing.
-->

| Boundary item | Decision |
|---|---|
| Observable decision outcome | |
| Primary authority owner | |
| Decision-record paths | <!-- ADR source, canonical index, direct references --> |
| Direct companion changes required to record the decision | |
| Dependent implementation after acceptance | |
| Work intentionally deferred or split | |
| Required ordered / stacked sequence | |
| Conflict or overlap disposition | |

- [ ] This issue requests one coherent decision.
- [ ] Direct dependencies are bounded to what is required to record, review, validate, migrate, or supersede the decision.
- [ ] Unrelated cleanup and optional consumers are excluded or listed as follow-up work.
- [ ] Implementation that depends on this decision is not treated as authorized before acceptance.
- [ ] If a governance PR and implementation PR are both needed, their dependency order and repinning rule are explicit.
- [ ] Any active overlap has a survivor, supersession, consolidation, or intentionally disjoint boundary.

## Evidence basis

<!--
Use precise repository paths plus immutable refs/SHAs, test or run IDs, logs,
manifests, schemas, receipts, or authoritative primary sources. Memory and
generic best practice are not evidence.
-->

| Truth label | Evidence location | Observation supported | Verification / limitation |
|---|---|---|---|
| `CONFIRMED` | | | |
| `PROPOSED` | | | |
| `NEEDS VERIFICATION` | | | |
| `UNKNOWN` | | | |

**EvidenceRef / EvidenceBundle implications:** <!-- `N/A` or explain resolution requirements. -->

**Docs versus implementation conflict:** <!-- `None found`, or identify the conflict and controlling evidence. -->

## Directory Rules and authority basis

| Proposed or affected path | Owning responsibility root | Authority / lifecycle role | Directory Rules or ADR basis | Placement outcome |
|---|---|---|---|---|
| | | | | `PLACE` / `SPLIT` / `MIGRATE` / `MIRROR` / `HOLD` / `DENY` |

- [ ] Existing same-path edits were checked for canonical, generated, mirror, compatibility, migration, or deprecation markers.
- [ ] New, moved, renamed, deleted, cross-root, or authority-bearing paths received full placement review.
- [ ] No new parallel authority home is created.
- [ ] Canonical, compatibility, generated, and mirror surfaces remain distinct.
- [ ] Human doctrine, semantic contracts, machine schemas, executable policy, lifecycle data, receipts/proofs, and release decisions remain in their owning roots.
- [ ] Any conflict between current implementation and doctrine is surfaced as drift rather than silently normalized.
- [ ] A migration note or manifest is included when paths, authority, identity, or lifecycle ownership move.
- [ ] Not applicable; explanation:

## Affected surfaces

### Responsibility roots

- [ ] `.github/`
- [ ] `docs/`
- [ ] `control_plane/`
- [ ] `contracts/`
- [ ] `schemas/`
- [ ] `policy/`
- [ ] `data/`
- [ ] `release/`
- [ ] `apps/`
- [ ] `packages/`
- [ ] `connectors/`
- [ ] `pipelines/` / `pipeline_specs/`
- [ ] `tools/` / `scripts/`
- [ ] `tests/` / `fixtures/`
- [ ] `runtime/` / `infra/` / `configs/`
- [ ] Compatibility or generated-output root:
- [ ] Other:
- [ ] None

**Cross-cutting explanation:** <!-- Required when several roots are affected. -->

### Object families and contracts

- [ ] Source / source-admission objects
- [ ] Evidence / citation objects
- [ ] Policy / sensitivity / rights decisions
- [ ] Validation / review records
- [ ] Identity / canonicalization / hashing objects
- [ ] AI / runtime / prompt envelopes or receipts
- [ ] Promotion / release / correction / rollback objects
- [ ] Layer / map / tile / export manifests
- [ ] No object-family meaning changes
- [ ] Other:

### Lifecycle stages

- [ ] Pre-RAW admission edge
- [ ] RAW
- [ ] WORK / QUARANTINE
- [ ] PROCESSED
- [ ] CATALOG / TRIPLET
- [ ] PUBLISHED
- [ ] Receipts / proofs / registry / rollback support
- [ ] No lifecycle-stage impact

### Public and governed interfaces

- [ ] Governed API
- [ ] Explorer / UI / map
- [ ] Focus Mode / AI surface
- [ ] Search / graph / catalog / export
- [ ] Release / publication
- [ ] No public-interface impact

**Trust-membrane notes:** <!-- Explain how public clients remain downstream of governed interfaces and released public-safe artifacts. -->

## Consequences and trade-offs

### Positive

-

### Negative / costs

-

### Neutral / accepted trade-offs

-

### Risks introduced

| Risk | Likelihood / impact | Mitigation | Residual risk |
|---|---|---|---|
| | | | |

## Alternatives considered

<!-- Include genuine alternatives. The status quo is a valid alternative. -->

1. **Preferred decision —**
2. **Alternative A —**
3. **Alternative B —**
4. **Status quo —**

## Implementation, migration, and compatibility plan

> [!IMPORTANT]
> An ADR records a decision; companion artifacts implement it. Do not use a proposed ADR as adopted authority. When implementation depends on acceptance, stage it after the ADR transition and repin the implementation base.

| Order | Phase | Artifact or path | Owner role | Dependency | Reversible? |
|---:|---|---|---|---|---|
| 1 | Decision record | | | | |
| 2 | Follow-on implementation | | | Accepted ADR / repinned base | |

- Migration manifest / note:
- Compatibility or deprecation window:
- Backfill or data transformation:
- Documentation updates:
- Release / correction implications:
- Rollout or feature-gate strategy:
- Abandonment path before acceptance:

### Versioning impact

| Surface | Current version / authority | Proposed change | Compatibility or migration action |
|---|---|---|---|
| Semantic contract | | | |
| Machine schema | | | |
| Policy bundle | | | |
| Runtime / API / public envelope | | | |
| Prompt or AI-build contract | | | |
| Release / correction object | | | |
| Not applicable | | | |

## Companion artifacts affected

- [ ] ADR source and canonical ADR index
- [ ] Doctrine / architecture documentation
- [ ] Contract(s)
- [ ] Schema(s)
- [ ] Policy bundle(s)
- [ ] Positive and negative fixtures
- [ ] Validator(s) / test(s)
- [ ] Source registry / descriptor(s)
- [ ] Pipeline / connector / package / app
- [ ] Workflow / GitHub configuration
- [ ] Migration or deprecation record
- [ ] ReviewRecord / StewardshipAssignment
- [ ] Generated receipt / proof / validation report
- [ ] PromotionDecision / ReleaseManifest
- [ ] CorrectionNotice / RollbackCard
- [ ] None
- [ ] Other:

**Required companion changes:**

-

## Validation and acceptance

<!--
Distinguish checks already run, decision acceptance evidence, delivery checks,
and hosted CI. A passing check proves only its stated scope and does not accept
the ADR, authorize implementation, or publish anything.
-->

### Performed

| Check or command | Scope | Outcome | Evidence |
|---|---|---|---|
| | | `PASS` / `FAIL` / `PENDING` / `NOT RUN` / `N/A` / `UNKNOWN` | |

### Required before acceptance

| Acceptance criterion | Expected outcome | Evidence required | Owner |
|---|---|---|---|
| Decision is singular and unambiguous | | | |
| Evidence and authority basis are sufficient | | | |
| Directory and migration consequences are bounded | | | |
| Required reviewers acted | | | |
| Source and canonical index agree | | | |
| Dependent implementation remains correctly ordered | | | |

### Hosted checks

| Check | Required? | State | Exact run / head evidence |
|---|---:|---|---|
| | `yes` / `no` | `PASS` / `FAIL` / `PENDING` / `NOT RUN` / `UNKNOWN` | |

### Failure signals

-

### Post-acceptance verification

-

## Rollback, supersession, and correction

- Rollback target:
- Rollback procedure:
- Rollback cost / irreversible effects:
- Supersedes:
- Superseded by:
- Drift-register update required:
- Correction or withdrawal path:
- Existing released artifacts affected:
- Cache, index, graph, or generated-output invalidation:

> [!IMPORTANT]
> Accepted, superseded, and rejected ADRs are retained. Replace an accepted decision through a successor ADR and explicit forward/back supersession links; do not delete or silently rewrite decision history.

## Security, rights, sensitivity, and sovereignty

- [ ] None identified.
- [ ] Security-sensitive implementation or vulnerability details.
- [ ] Archaeology, cultural, Indigenous, burial, or sacred-site material.
- [ ] Rare species, rare plants, habitat, or geoprivacy.
- [ ] Critical infrastructure or emergency operations.
- [ ] Living-person, genealogy, consent, DNA, or genomic material.
- [ ] Private-land or stewardship information.
- [ ] Restricted source terms, licensing, or rights uncertainty.
- [ ] Exact-harm or reconstructable location exposure.
- [ ] Other:

**Required additional reviewer(s):**

**Public-safe transform / access restriction:**

**Private handling required:** `yes` / `no` / `NEEDS VERIFICATION`

## Review and separation of duties

| Role | Proposed reviewer / owner | Required because | Independent from author? |
|---|---|---|---|
| Architecture / repository steward | | | |
| Affected subsystem or domain steward | | | |
| Docs steward | | | |
| Policy / security / sensitivity / rights reviewer | | | |
| Release or correction authority | | | |

- [ ] The decision author is identified.
- [ ] Required approving roles are identified.
- [ ] Material author/approver separation is preserved where required.
- [ ] Missing reviewer identity or authority produces `HOLD` / `NEEDS VERIFICATION`, not implicit approval.
- [ ] CODEOWNERS, assignment, labels, issue closure, and green CI are not treated as acceptance evidence by themselves.

## Open questions and verification backlog

-

## References

- `docs/adr/README.md`
- `docs/adr/INDEX.md`
- `docs/adr/ADR-template.md`
- `docs/doctrine/directory-rules.md`
- `docs/doctrine/ai-build-operating-contract.md`
- `docs/prompts/kfm-repository-build-markdown-modernization-agent.md`
- `docs/registers/DRIFT_REGISTER.md`
- `docs/registers/VERIFICATION_BACKLOG.md`
- Prior ADR(s):
- Related issue(s) / PR(s):
- Evidence / source links:

## Submitter acknowledgements

- [ ] I understand this issue is a proposal, not an accepted ADR or implementation authority.
- [ ] I pinned the repository baseline and checked ADR numbers, open pull requests, active branches, and recent relevant changes for collisions.
- [ ] I separated verified evidence from proposed, unknown, or unverified claims.
- [ ] I identified the current governing authority and Directory Rules placement or migration implications.
- [ ] I kept the governance decision separate from implementation that depends on its acceptance.
- [ ] I listed required companion artifacts, validation, compatibility, rollback, correction, and supersession work.
- [ ] I did not include secrets, restricted payloads, or sensitive exact-location details.
- [ ] I identified required independent reviewers and unresolved authority gaps.
- [ ] I understand that issue text, comments, labels, assignment, closure, bot actions, or green CI do not authorize mutation, accept the decision, merge code, release, deploy, promote, publish, or change repository settings.

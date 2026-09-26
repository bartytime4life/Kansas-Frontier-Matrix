<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://adr/ADR-0043
adr_id: ADR-0043
title: "ADR-0043 — People/DNA/Land genealogy policy scaffolding uses policy/domains/people-dna-land/, not a genealogy sublane"
type: adr
version: v1.0
status: proposed
owners:
  - "NEEDS VERIFICATION — People/DNA/Land domain steward"
  - "NEEDS VERIFICATION — genealogy/consent steward"
owner_status: "CODEOWNERS routing to @bartytime4life is review routing only; it is not stewardship assignment, review evidence, decision quorum, or acceptance authority"
reviewers_required:
  - Architecture steward
  - Docs steward
  - People/DNA/Land domain steward
  - Genealogy/consent steward
created: 2026-09-26
updated: 2026-09-26
policy_label: public
truth_posture: cite-or-abstain
owning_root: docs/
responsibility_root: docs/
responsibility: "Propose a canonical policy/ home for People/DNA/Land genealogy policy scaffolding and a bounded migration/review path for the existing scaffold, without accepting the decision or authorizing migration by itself."
current_path: docs/adr/ADR-0043-people-dna-land-genealogy-policy-tooling-home.md
supersedes: []
superseded_by: null
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: claude/rego-placeholder-provenance-drift
  base_commit: a920352e420229078ddc242602779c0a74986c47
  target_prior_blob: null
  adr_index_blob: 7e22111f1a98c586cc32801aa6af2f09a9bab16e
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  relevant_contract_blob: null
  relevant_schema_blob: null
  relevant_policy_blob: f2811f825b5ac1b56f7d7dc4cbc8f4f65b7c438e
  relevant_fixture_or_test_blob: null
related:
  - docs/adr/README.md
  - docs/adr/INDEX.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/adr/ADR-0042-people-dna-land-genealogy-validator-tooling-home.md
  - docs/domains/people-dna-land/sublanes/dna.md
  - docs/registers/DRIFT_REGISTER.md
  - policy/genealogy/README.md
  - policy/genealogy/publication.rego
  - policy/domains/people-dna-land/README.md
tags: [kfm, adr, people-dna-land, genealogy, policy, tooling-placement, directory-rules]
notes:
  - "This record begins proposed; file presence, a commit, a pull request, a merge, or an index row does not accept it."
  - "This record authorizes no dependent implementation, migration, release, deployment, promotion, publication, source activation, or repository-settings change before an explicit reviewed acceptance transition."
  - "Direct policy-root sibling of ADR-0042, which resolved the equivalent tools/validators/ placement question for the same domain; raised from the same-day DRIFT_REGISTER.md entry documenting this conflict."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0043 — People/DNA/Land genealogy policy scaffolding uses `policy/domains/people-dna-land/`, not a genealogy sublane

> **Proposed decision.** KFM will treat `policy/domains/people-dna-land/` — the whole-domain policy lane, matching the pattern already established across policy domains and already named by this domain's own planning document — as the sole home for genealogy-concern policy scaffolding, and will retire `policy/genealogy/` as a policy home through a bounded migration.

> [!IMPORTANT]
> **This ADR is proposed.** It is not binding until the source record and canonical index carry a synchronized, reviewed acceptance transition. Moving `publication.rego` or editing `policy/genealogy/README.md` must not treat this proposal as already-adopted authority.

> [!NOTE]
> **Non-effects.** This record does not by itself move any file, implement any policy rule, change OPA/evaluator wiring, decide the separate `docs/domains/people-dna-land/sublanes/` documentation-layer question (`OQ-PEOPLE-SUB-01`/`OQ-PEOPLE-SUB-02`), decide `policy/consent/people/` vs. `policy/domains/people-dna-land/consent/` (`OQ-PEOPLE-DNA-11`/`OQ-GEN-12`, a separate already-flagged `CONFLICTED` question), grant consent/rights/policy authority, or authorize release, deployment, or publication.

**Quick navigation:** [Status](#1-status-and-authority) · [Evidence](#2-evidence-boundary) · [Context](#3-context) · [Decision](#4-decision) · [Consequences](#5-consequences-and-risks) · [Alternatives](#6-alternatives-considered) · [Implementation](#7-implementation-migration-and-compatibility) · [Validation](#8-validation-and-acceptance) · [Rollback](#9-rollback-correction-and-supersession) · [Sensitivity](#10-security-rights-sensitivity-and-sovereignty) · [Open work](#11-open-questions-and-verification-backlog) · [References](#12-evidence-and-references) · [History](#13-change-history)

---

## 1. Status and authority

| Field | Current value |
|---|---|
| **ADR ID** | `ADR-0043` — unique in [`INDEX.md`](./INDEX.md) at this evidence snapshot |
| **Tracked path** | `docs/adr/ADR-0043-people-dna-land-genealogy-policy-tooling-home.md` |
| **Source metadata** | `proposed` |
| **Effective decision status** | `proposed` — not binding |
| **Decision class** | `structural` (policy scaffolding placement within an already-existing responsibility root) |
| **Decision scope** | Which path is canonical for genealogy-concern policy scaffolding under `policy/` |
| **Primary authority owner** | People/DNA/Land domain steward (`NEEDS VERIFICATION` — no verified named individual) |
| **Required reviewers** | Architecture steward; Docs steward; People/DNA/Land domain steward; genealogy/consent steward |
| **Governing authority** | Directory Rules §12 (adopted via accepted `ADR-0029`); `docs/domains/people-dna-land/sublanes/dna.md`'s own domain-lane table; `ADR-0042` precedent |
| **Implementation maturity** | `absent` for the decision itself; `scaffold` for both candidate paths — neither carries operative policy logic yet |
| **Delivery state** | draft record, this change |
| **Publication effect** | None |
| **Supersedes** | — |
| **Superseded by** | — |
| **Rollback target for this document** | Not applicable — new file |

### 1.1 State separation

| Axis | Current state | Evidence |
|---|---|---|
| ADR lifecycle | `proposed` | This source record; not yet in `INDEX.md`'s accepted set |
| Truth posture | Mixed — see §2 evidence table | Evidence boundary below |
| Implementation maturity | `scaffold` on both sides — `policy/genealogy/publication.rego` is a four-line `default allow := false` stub; `policy/domains/people-dna-land/` holds seven similarly immature `.rego` files (two four-line stubs, five twelve-line stubs with only commented-out example rules) — unlike `ADR-0042`'s validator case, neither candidate path is a confirmed working implementation | Repository inspection, this snapshot |
| KFM lifecycle/release | Not applicable | Tooling-placement decision, not a data lifecycle change |
| Hosted validation | `NOT RUN` — no hosted CI observed for this proposal | Local-only checks in §8 |

### 1.2 Scope

**In scope**

- Whether `policy/genealogy/` or `policy/domains/people-dna-land/` is the canonical home for genealogy-concern policy scaffolding (currently just `publication.rego`).
- Disposition of the one existing scaffold at the disputed path (`policy/genealogy/publication.rego`) and its README.

**Out of scope / explicitly unchanged**

- Whether `docs/domains/<domain>/sublanes/` is a ratified documentation convention at all (`OQ-PEOPLE-SUB-01`).
- Whether genealogy is a standalone sublane or folds into "people" (`OQ-PEOPLE-SUB-02`).
- `policy/consent/people/` vs. `policy/domains/people-dna-land/consent/` canonicality (`OQ-PEOPLE-DNA-11`/`OQ-GEN-12`) — a separate, already-flagged `CONFLICTED` question in adjacent documents.
- Any consent, rights, policy, evidence, release, or publication decision for genealogy data itself; both candidate files are non-operative `default allow := false` / `default deny := false` scaffolds today.
- The broader cross-domain `policy/domains/<domain>/` vs. `policy/sensitivity/<domain>/` placement question logged separately in `DRIFT_REGISTER.md` (affects Archaeology, Flora, and People/DNA/Land's `living_person.rego`, in inconsistent directions) — that needs its own cross-domain ADR and is not resolved here.

[Back to top](#top)

---

## 2. Evidence boundary

| Evidence surface | Truth label | Current observation | What it proves — and does not prove |
|---|---|---|---|
| `docs/domains/people-dna-land/sublanes/dna.md` line 381 | `CONFIRMED` | Domain-lane table names `policy/domains/people-dna-land/` as the "(PROPOSED — §12 lane form)" home. | Proves the doc's own naming convention points to the whole-domain segment. Does not itself prove an accepted decision — the document is proposal-lineage, not an accepted contract. |
| `docs/doctrine/directory-rules.md` §12.2 (adopted via `ADR-0029`) | `CONFIRMED` | Domain-lane pattern illustrates `policy/domains/<domain>/` among other roots; no sublane segment is illustrated anywhere in §12. | Establishes the general whole-domain-lane convention `ADR-0042` already applied to `tools/validators/`; supports the same reading for `policy/`. |
| `policy/genealogy/publication.rego` | `CONFIRMED` | Four-line `PROPOSED` scaffold: `package kfm.generated.policy.genealogy.publication`, `default allow := false`. Header cites `docs/domains/people-dna-land/sublanes/dna.md` as its source. | Proves the scaffold exists and cites this doc; the doc's own table names a different path, so the citation does not grow into a placement decision. |
| `policy/genealogy/README.md` (v0.2, 561 lines, blob `8395d13e1f7c58d3c5637022ad762df81e8429f3`) | `CONFIRMED` | Declares its own `status` field `placement-conflicted`, and its `truth_posture` field states "CONFLICTED policy/genealogy/ compatibility path versus policy/domains/people-dna-land/ domain placement and standalone genealogy versus people-sublane ownership." | Proves the conflict was already self-recognized in-repo before this ADR. Does not itself constitute an ADR, and does not instruct logging to `DRIFT_REGISTER.md` (unlike the `tools/validators/genealogy/` sibling case). |
| `policy/domains/people-dna-land/` directory listing | `CONFIRMED` | Seven `.rego` files: `abstain_on_ambiguous.rego`, `consent_validator.rego`, `deny_unpublished.rego`, `dna_restricted.rego`, `living_person.rego`, `living_person_redaction.rego` (12 lines each except two 4-line stubs), plus `consent/dna_consent_revocation.rego`. Also an already-reserved, still-empty `genealogy/.gitkeep`. | Proves the whole-domain segment is already the active, populated convention for this domain's policy files — but, unlike `ADR-0042`'s validator precedent, none of these seven files carries operative rule logic yet; all are scaffolds. This is weaker "already confirmed" evidence than the validator case. |
| `docs/registers/DRIFT_REGISTER.md` (2026-09-26 entry, this branch) | `CONFIRMED` | Logs this exact conflict as the policy-root sibling of the already-logged `tools/validators/genealogy/` entry. | Proves the conflict was visible and tracked before this ADR. |
| `docs/adr/INDEX.md` | `CONFIRMED` | At blob `7e22111f1a98c586cc32801aa6af2f09a9bab16e`, the numbered sequence is complete and unique `ADR-0001`–`ADR-0042`; no open pull request or `ADR-0043` file existed prior to this change (checked via repository code search and `list_pull_requests`). | Establishes `ADR-0043` as the next collision-free number at this snapshot. |

### 2.1 Truth labels used

- **CONFIRMED** — verified from the pinned evidence above.
- **PROPOSED** — the decision or desired target state.
- **UNKNOWN** — evidence is insufficient for a stronger claim.
- **NEEDS VERIFICATION** — a concrete check remains.
- **CONFLICTED** — current admissible sources or writable homes disagree.
- **HOLD** — implementation or acceptance must stop until named evidence or authority closes.

[Back to top](#top)

---

## 3. Context

`docs/domains/people-dna-land/sublanes/dna.md` names `policy/domains/people-dna-land/` as the domain-lane home for People/DNA/Land policy (§12 lane form). A code-generation pass later created a genealogy publication-policy stub not at that path, but at a flat `policy/genealogy/` segment, citing this same document as its source. `policy/genealogy/README.md` already recognizes the resulting conflict explicitly in its own status and truth-posture metadata — but that recognition was never carried into `docs/registers/DRIFT_REGISTER.md`, and no ADR previously existed to resolve it.

This is the exact same shape of conflict `ADR-0042` already proposed a resolution for — `tools/validators/genealogy/` versus `tools/validators/domains/people-dna-land/`, in the same domain, one responsibility root over (`policy/` instead of `tools/validators/`) — though `ADR-0042` itself remains `proposed`, not accepted, so it is precedent-in-waiting rather than binding authority. Unlike that case, neither candidate policy path yet holds working rule logic — `policy/domains/people-dna-land/`'s other six files are themselves still scaffolds — so the evidence for "already-established convention" here rests on the domain doc's own naming and the already-reserved `genealogy/.gitkeep` subdirectory, not on existing substantive implementations.

### 3.1 Decision drivers

- **Consistency with the domain's own stated convention** — `dna.md` itself names `policy/domains/people-dna-land/` as the lane home.
- **Consistency with `ADR-0042`** — the same domain already has an accepted-basis reasoning for preferring the whole-domain segment over a flat `genealogy/` segment for tooling; applying the same reasoning to policy avoids a second, inconsistent precedent for the identical domain.
- **Respecting an already-reserved path** — `policy/domains/people-dna-land/genealogy/.gitkeep` already exists, suggesting a specific intended subdirectory that nobody has used yet.
- **Reversibility** — only one real scaffold file and one README are affected; migration cost is minimal.
- **Not deciding more than necessary** — the sublane documentation-layer questions and the separate `policy/consent/people/` vs. `policy/domains/people-dna-land/consent/` conflict are left untouched.

### 3.2 Current conflict or gap

| Surface | Current state | Conflict or gap |
|---|---|---|
| `policy/genealogy/publication.rego` | Four-line `PROPOSED` scaffold | Sits at a path its own cited source document does not name, and its own README calls "placement-conflicted" |
| `policy/genealogy/README.md` | 561-line self-aware compatibility-boundary document | Already declares `CONFLICTED` status but does not instruct logging or name a resolving ADR |
| `policy/domains/people-dna-land/` | Seven `.rego` scaffolds, one reserved empty `genealogy/` subdirectory | Named by `dna.md` as the lane home, but not yet a "confirmed implementation" the way `tools/validators/domains/people-dna-land/` was in `ADR-0042` |

### 3.3 Non-goals

- This ADR does not decide the `sublanes/` documentation convention question.
- This ADR does not decide `policy/consent/people/` vs. `policy/domains/people-dna-land/consent/` (`OQ-PEOPLE-DNA-11`/`OQ-GEN-12`).
- This ADR does not decide the broader `policy/domains/<domain>/` vs. `policy/sensitivity/<domain>/` cross-domain question separately logged in `DRIFT_REGISTER.md`.
- This ADR does not authorize moving, deleting, or implementing any file, or writing real policy logic into either candidate.

[Back to top](#top)

---

## 4. Decision

> **Decision:** KFM will treat `policy/domains/people-dna-land/` as the sole canonical home for genealogy-concern policy scaffolding, retire `policy/genealogy/` as a policy home through a reviewed migration, and place any future genealogy publication-policy implementation under the already-reserved `policy/domains/people-dna-land/genealogy/` subdirectory.

### 4.1 Normative rules

1. **MUST** — New genealogy-concern policy files for the People/DNA/Land domain are added only under `policy/domains/people-dna-land/genealogy/`.
2. **MUST NOT** — No new file is added under `policy/genealogy/` after this ADR's acceptance.
3. **SHOULD** — `publication.rego` is migrated to `policy/domains/people-dna-land/genealogy/` in a dedicated, reviewed follow-up change once this decision is accepted, preserving its current placeholder content exactly (no logic is added as part of the move).
4. **SHOULD** — `policy/genealogy/README.md`'s substantive compatibility-boundary content (self-aware conflict documentation, safe-input/output boundaries, sensitive-data exclusions) is merged into or cross-linked from `policy/domains/people-dna-land/README.md` as part of the same migration, so its analysis is not lost.

### 4.2 Responsibility and placement

| Axis | Decision |
|---|---|
| `artifact_kind` | `policy` (Rego scaffold) plus `human document` (README) |
| `authority_owner` | People/DNA/Land domain steward (placement); genealogy/consent steward (policy content) |
| `lifecycle_stage` | n/a — repository policy scaffolding, not lifecycle data |
| `execution_role` | `none` (non-operative scaffold; `default allow := false` only) |
| `scope_kind` / `scope_id` | `domain` / `people-dna-land` |
| `exposure` | internal (no operative rule, no evaluator binding, no public route) |
| `mutability` / `retention` | versioned; durable |
| Candidate path | `policy/domains/people-dna-land/genealogy/publication.rego` |
| Governing rule IDs / accepted ADRs | Directory Rules §12.2 (via accepted `ADR-0029`); `ADR-0042` precedent for the same domain |
| Placement outcome | `MIGRATE` |
| Parallel-authority posture | Explicitly denies a second, permanent genealogy-scoped policy lane; `policy/genealogy/` becomes a migration-only, non-authoritative path pending retirement |

### 4.3 Authority and public-boundary rules

- Public clients are not affected — neither candidate file has operative logic, an evaluator binding, or a public route.
- Evidence-dependent claims are unaffected.
- Policy, rights, sensitivity, review, and release decisions for genealogy or consent data are unaffected; this ADR is a placement decision only.
- Derived maps, tiles, graphs, indexes, summaries, and generated language are unaffected.

### 4.4 Non-effects

This decision does not:

- decide `OQ-PEOPLE-SUB-01`, `OQ-PEOPLE-SUB-02`, `OQ-PEOPLE-DNA-11`, or `OQ-GEN-12`;
- decide the cross-domain `policy/domains/<domain>/` vs. `policy/sensitivity/<domain>/` question logged separately;
- move, delete, or implement any file by itself;
- grant consent, rights, policy, evidence, review, or release authority; or
- authorize release, deployment, promotion, or publication.

[Back to top](#top)

---

## 5. Consequences and risks

### 5.1 Positive consequences

- Aligns the policy root with the same domain-lane reasoning `ADR-0042` already established for the tooling root, avoiding two different placement philosophies for the same domain.
- Resolves a conflict `policy/genealogy/README.md` already self-flagged but that had no logged register entry or ADR.
- Keeps migration bounded: one scaffold file plus one README's worth of content.

### 5.2 Negative consequences and costs

- Requires a follow-up migration PR before the decision is fully realized.
- `policy/genealogy/README.md`'s extensive self-documentation needs reconciliation, not just deletion, so its analysis isn't lost — additional review-bounded work.

### 5.3 Accepted tradeoffs

This ADR favors consistency with the domain's own stated lane convention and with `ADR-0042`'s precedent over preserving the path the placeholder-generation pass happened to use, even though — unlike the tooling case — neither candidate is yet a mature implementation.

### 5.4 Affected surfaces

| Responsibility surface | Current path(s) | Required change | Authority / compatibility note |
|---|---|---|---|
| ADR source and index | `docs/adr/...` | Add `ADR-0043`; update `INDEX.md` and `README.md` snapshot counts | Decision record only |
| Policy scaffolding | `policy/genealogy/`, `policy/domains/people-dna-land/` | Migrate `publication.rego` (follow-up, not this change) | No behavior change intended |
| Documentation | `policy/genealogy/README.md`, `policy/domains/people-dna-land/README.md` | Reconcile after migration (follow-up) | Explanation only |
| Drift register | `docs/registers/DRIFT_REGISTER.md` | Cross-reference this ADR once accepted (follow-up append) | Register entry, not authority |
| Contracts/Schemas/Data/Release | — | Not affected | Out of scope |

### 5.5 Risk ledger

| Risk | Likelihood / impact | Mitigation | Residual risk / owner |
|---|---|---|---|
| Migration loses `policy/genealogy/README.md`'s self-documented conflict analysis | Low / low | Explicitly require content reconciliation, not deletion, in §4.1 rule 4 | Residual: reviewer discretion on what counts as "substantive"; owner: migration PR author |
| Decision stalls without a confirmed steward | Medium / low | This record's required reviewers (§1) — architecture steward, docs steward, People/DNA/Land domain steward, genealogy/consent steward — must all act before acceptance; `ADR-0029`'s single-owner bootstrap exception was an explicit, disclosed, case-specific action and not a standing waiver, and `ADR-0042` remains itself `proposed`, so neither establishes a reusable shortcut around this record's own reviewer requirement. Acceptance holds until the named reviewers act or a repository owner records an equally explicit, disclosed exception here | Residual: any future bootstrap exception must be explicit and recorded at acceptance time, not assumed from precedent; owner: whoever accepts this ADR |
| Confused with the broader `policy/domains/` vs. `policy/sensitivity/` question | Low / medium | §3.3 and §4.4 explicitly exclude that question | Residual: a reviewer conflating the two; owner: reviewing steward |

[Back to top](#top)

---

## 6. Alternatives considered

### 6.1 Selected option — `policy/domains/people-dna-land/` (optionally its `genealogy/` subdirectory)

- **Summary:** Use the domain's own named lane, consistent with `ADR-0042`.
- **Why selected:** Directly named by `dna.md`; consistent with the sibling tooling decision; a subdirectory is already reserved.

### 6.2 Alternative A — Keep `policy/genealogy/`

- **Summary:** Ratify the path the scaffold already occupies.
- **Why rejected:** Directly contradicted by the scaffold's own cited source document and by the README's own self-declared `placement-conflicted` status.

### 6.3 Alternative B — A different flat root, e.g. `policy/sensitivity/people-dna-land/genealogy/`

- **Summary:** Route through the sensitivity-policy lane instead.
- **Why rejected:** That lane's own placement relative to `policy/domains/<domain>/` is itself an open, unresolved cross-domain question (logged separately); building on top of an unresolved foundation would risk a second migration.

### 6.4 Status quo

- **Summary:** Leave the conflict open.
- **Why rejected:** Already self-flagged as conflicted in-repo with no register entry or resolving ADR; costs nothing to decide now given the evidence already assembled for the identical tooling question.

[Back to top](#top)

---

## 7. Implementation, migration, and compatibility

> [!IMPORTANT]
> **Decision and dependent implementation are separate transitions.** This proposed ADR does not itself move or implement anything. Migration begins only after acceptance.

### 7.1 Ordered change sequence

| Order | Change | Dependency | Review boundary | Reversible? |
|---:|---|---|---|---:|
| 1 | Record this proposed ADR and update `INDEX.md`/`README.md` | Current authority (this change) | Decision review | yes |
| 2 | Explicit reviewed acceptance transition | Owner/steward review | Status review | yes |
| 3 | Migrate `publication.rego` to `policy/domains/people-dna-land/genealogy/`; update any inbound references | Accepted ADR | Implementation review | yes (git revert) |
| 4 | Reconcile `policy/genealogy/README.md`'s content into `policy/domains/people-dna-land/README.md`; retire the empty `policy/genealogy/` directory | Step 3 | Docs review | yes |

### 7.2 Migration and compatibility plan

- **Old → new mapping:** `policy/genealogy/publication.rego` → `policy/domains/people-dna-land/genealogy/publication.rego`.
- **Migration manifest/note:** Not applicable — a single-file `git mv`, described in the migration PR description.
- **Producer cutover:** N/A (no producer writes this file at runtime; no evaluator currently binds it).
- **Consumer migration:** None known — no test, workflow, or bundle reference to `policy/genealogy/publication.rego` was found at this snapshot.
- **Mirror/alias class:** `none` — direct move.
- **Compatibility window and exit criteria:** None needed.
- **Identity preservation or versioning:** Preserve `git mv` history; do not rewrite package name or logic as part of the move.
- **Backfill or transform:** Not applicable.
- **Reference/link repair:** Update any Markdown links to the old path in the same or an immediately following PR.
- **Destructive cleanup:** Delete `policy/genealogy/` only after the migration PR merges and no reference to it remains.

### 7.3 Direct dependency closure

| Artifact | Why directly required | Planned path | Validation |
|---|---|---|---|
| `publication.rego` | Only scaffold currently at the disputed path | `policy/domains/people-dna-land/genealogy/publication.rego` | Confirm package name and `default allow := false` are byte-identical after the move |
| `policy/genealogy/README.md` | Documents the lane being retired | Merge relevant content into `policy/domains/people-dna-land/README.md` | Manual review; no automated check known |

### 7.4 Deferred work

- Writing real genealogy publication-policy logic (contingent on separate rights/consent/policy review, not this ADR).
- The broader `policy/domains/<domain>/` vs. `policy/sensitivity/<domain>/` cross-domain ADR — explicitly out of scope here.

[Back to top](#top)

---

## 8. Validation and acceptance

### 8.1 Checks performed for this proposal

| Check / command / inspection | Scope | State | Exact evidence |
|---|---|---|---|
| `python tools/validators/validate_adr_index.py` | ADR inventory coherence | `PASS` | Re-run after this change's `INDEX.md` update (see commit) |
| `python -m pytest tests/validators/test_validate_adr_index.py -q --strict-config --strict-markers` | ADR validator failure paths | `PASS` | Re-run after this change (see commit) |
| Repository code search for `ADR-0043` | Number-collision check | `PASS` | Zero real files matched; one incidental example/placeholder mention in a validator test fixture, not a real file |
| `list_pull_requests` (open) | Overlap check | `PASS` | Zero open pull requests at check time |
| Repository search for consumers of `policy/genealogy/publication.rego` | Consumer-migration risk | `PASS` | No test, workflow, or bundle reference found |
| Hosted checks | Exact pull-request head | `NOT RUN` | No pull request opened yet |

### 8.2 Acceptance criteria

| Criterion | Required evidence | Current state | Owner/reviewer |
|---|---|---|---|
| Decision is singular and unambiguous | One directive (§4) | Met | Architecture steward |
| Current facts are pinned and truth-labeled | §2 evidence table | Met | Docs steward |
| Governing authority is sufficient | Directory Rules §12 + `ADR-0042` precedent cited | Met | Architecture steward |
| Placement and ownership are deterministic | §4.2 responsibility signature | Met | Architecture steward |
| Alternatives and consequences are complete | §5–§6 | Met | Architecture steward |
| Migration and rollback are executable | §7, §9 | Met (described; not yet executed) | Implementation reviewer |
| Security, rights, sensitivity, sovereignty addressed | §10 | Met (mostly not-applicable, explicitly stated) | Genealogy/consent steward |
| Required reviewers acted | Review evidence | `NOT MET` — no review yet | People/DNA/Land + genealogy/consent stewards |
| ADR source and canonical index agree | Validator pass after index update | Met, this change | Docs steward |
| Dependent implementation remains correctly ordered | §7.1 sequencing | Met | Implementation reviewer |

### 8.3 Current enforcement maturity

| Capability | Current state | Acceptance blocker? |
|---|---|---:|
| Contract/schema/policy support | Not applicable (tooling-placement decision) | no |
| Fixtures and negative tests | None exist for either candidate path | no |
| Validator/CI coverage | ADR-index validator only; no validator enforces this specific placement rule yet | no |
| Producer/consumer migration | Not yet executed (deferred to §7) | no — deferred by design |
| Runtime/API/UI behavior | Not applicable | no |
| Release/correction/rollback proof | Not applicable | no |

### 8.4 Post-acceptance verification

- Confirm the migration PR moves exactly `publication.rego`, with no logic change (still `default allow := false`).
- Confirm `policy/genealogy/` is empty (or removed) after migration and reference repair.
- Confirm `policy/genealogy/README.md`'s substantive analysis is preserved somewhere (merged or cross-linked), not silently dropped.
- Update `docs/registers/DRIFT_REGISTER.md` with a short append-only note pointing to this ADR once accepted.

[Back to top](#top)

---

## 9. Rollback, correction, and supersession

### 9.1 Documentation rollback

- **Prior blob / commit:** Not applicable — new file; revert is `git rm docs/adr/ADR-0043-people-dna-land-genealogy-policy-tooling-home.md` plus reverting the paired `INDEX.md`/`README.md` edits.
- **Revert procedure:** Standard `git revert` of the introducing commit.
- **Validation after revert:** Re-run `python tools/validators/validate_adr_index.py`.

### 9.2 Implementation rollback or forward fix

- **Trigger conditions:** Migration PR breaks something, an undiscovered consumer of the old path surfaces, or a steward determines a different path is correct.
- **Rollback steps:** `git revert` the migration commit, restoring the file at `policy/genealogy/`.
- **Forward-fix requirement if rollback is unsafe:** If other work has already built on the new path, patch forward rather than reverting.
- **Compatibility after rollback:** No parallel writable authority is created either way.
- **Data/release correction:** Not applicable.
- **Rollback must not recreate two writable authorities.**

### 9.3 Supersession

- **Supersedes:** none.
- **Superseded by:** none until an accepted successor exists.
- **Reciprocal index/source links:** To be added to `INDEX.md`/`README.md` if superseded later.
- **Drift-register update:** Required — append a short note to `docs/registers/DRIFT_REGISTER.md` once this ADR is accepted, cross-referencing its ID.

Accepted, rejected, and superseded records remain in the repository.

[Back to top](#top)

---

## 10. Security, rights, sensitivity, and sovereignty

| Concern | Applies? | Required control or reviewer | Evidence |
|---|---:|---|---|
| Security-sensitive behavior or vulnerability detail | no | — | File-path decision for a non-operative policy scaffold |
| Rights, license, source terms, or redistribution | no | — | No source or data is touched |
| Archaeology, cultural, Indigenous, burial, or sacred context | no | — | Not applicable to this domain/decision |
| Rare species, rare plants, habitat, or geoprivacy | no | — | Not applicable |
| Critical infrastructure or emergency operations | no | — | Not applicable |
| Living-person, genealogy, consent, DNA, or genomic data | yes — indirectly | Genealogy/consent steward review before real policy logic is written | Both candidate files are currently non-operative (`default allow := false`); this ADR changes their location, not their (absent) behavior |
| Private land or exact harmful location | no | — | Not applicable |

Unknown or unresolved high-risk handling returns `HOLD` or `DENY`; it is not solved by a disclaimer. Because neither candidate file has operative logic, this ADR's placement decision does not itself introduce a new sensitivity exposure.

[Back to top](#top)

---

## 11. Open questions and verification backlog

| Item | Status | Why unresolved | Owner / next evidence | Blocks |
|---|---|---|---|---|
| Who is the verified People/DNA/Land domain steward and genealogy/consent steward? | `NEEDS VERIFICATION` | No verified individual found in this session's evidence | Repository owner / CODEOWNERS update | Formal acceptance review; §1's four required reviewers cannot all act until identified |
| Does this decision have any bearing on `OQ-PEOPLE-SUB-01`/`OQ-PEOPLE-SUB-02`/`OQ-PEOPLE-DNA-11`/`OQ-GEN-12`, or the cross-domain `policy/sensitivity/` question? | `CONFIRMED` — no, by design (§3.3, §4.4) | Explicitly scoped out | — | Nothing; recorded for clarity |

Do not hide unresolved acceptance blockers in prose. Track the steward-identity gap through the repository's normal ownership process, not through a second ADR.

[Back to top](#top)

---

## 12. Evidence and references

### 12.1 Repository evidence ledger

| Evidence | Immutable identity | Claim supported | Limit |
|---|---|---|---|
| `docs/adr/INDEX.md` | blob `7e22111f1a98c586cc32801aa6af2f09a9bab16e` | 42 numbered records exist; `ADR-0043` is next | Snapshot only; re-verify before merge |
| `docs/doctrine/directory-rules.md` | blob `fd49a0b83e55cef52c1124281f093e263526898d` | §12.2 domain-lane pattern text | Adopted via `ADR-0029` |
| `docs/domains/people-dna-land/sublanes/dna.md` | blob `2340c5444d5ffb27c8b8ee01e79df7d632c936ed` | Line 381 names `policy/domains/people-dna-land/` as the lane home | `status: draft`; not an accepted contract |
| `policy/genealogy/README.md` | blob `8395d13e1f7c58d3c5637022ad762df81e8429f3` | Self-declares `placement-conflicted` status | Not an ADR |
| `policy/genealogy/publication.rego` | blob `f2811f825b5ac1b56f7d7dc4cbc8f4f65b7c438e` | Non-operative scaffold exists at the disputed path | — |
| `policy/domains/people-dna-land/` directory listing | seven files, this snapshot | Domain-lane segment already active but not yet substantively implemented | All seven files remain scaffolds |
| `docs/adr/ADR-0042-people-dna-land-genealogy-validator-tooling-home.md` | blob `73d7c5794448cce101ded2333869a67039546e26` | Sibling precedent for the same domain, tooling root | Proposed, not accepted |

### 12.2 Governing decisions and doctrine

- [`ADR-0029`](./ADR-0029-adopt-directory-governance-standard-v2.md) — accepted adoption of Directory Rules v2, including §12.2's domain-lane pattern.
- [`ADR-0042`](./ADR-0042-people-dna-land-genealogy-validator-tooling-home.md) — sibling precedent, same domain, tooling root.
- [`docs/doctrine/directory-rules.md`](../doctrine/directory-rules.md) §12.

### 12.3 External primary sources

- Not applicable — this decision rests entirely on repository-internal evidence.

### 12.4 Source lineage

- [`docs/domains/people-dna-land/sublanes/dna.md`](../domains/people-dna-land/sublanes/dna.md) line 381 — proposal lineage for the policy path.
- [`docs/registers/DRIFT_REGISTER.md`](../registers/DRIFT_REGISTER.md) — the 2026-09-26 entry this ADR resolves.

[Back to top](#top)

---

## 13. Change history

| Date | Record status | Change | Evidence / PR |
|---|---|---|---|
| 2026-09-26 | proposed | Initial repository record | This change |

[Back to top](#top)

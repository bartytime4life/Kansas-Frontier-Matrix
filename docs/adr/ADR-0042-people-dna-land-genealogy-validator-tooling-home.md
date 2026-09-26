<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://adr/ADR-0042
adr_id: ADR-0042
title: "ADR-0042 — People/DNA/Land genealogy validator tooling uses tools/validators/domains/people-dna-land/, not a genealogy sublane"
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
responsibility: "Propose a canonical tools/validators/ home for People/DNA/Land genealogy validator tooling and a bounded migration/review path for the existing implementation and pending stubs, without accepting the decision or authorizing migration by itself."
current_path: docs/adr/ADR-0042-people-dna-land-genealogy-validator-tooling-home.md
supersedes: []
superseded_by: null
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: claude/laughing-goodall-lcc179
  base_commit: 458243599dd4ce01f17454a5faefe66c0facb078
  target_prior_blob: null
  adr_index_blob: a937b4c5a81e0b36b44a2fc14d7df046db388fe2
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  relevant_contract_blob: null
  relevant_schema_blob: null
  relevant_policy_blob: null
  relevant_validator_blob: bca6eefb350360f79ae4bbab8ff9741b554df334
  relevant_fixture_or_test_blob: 794ab5c4291f4c6174eaa387887f45214021d115
related:
  - docs/adr/README.md
  - docs/adr/INDEX.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/domains/people-dna-land/sublanes/genealogy.md
  - docs/registers/DRIFT_REGISTER.md
  - tools/validators/genealogy/README.md
  - tools/validators/genealogy/screen_living_persons.py
  - tests/validators/test_screen_living_persons.py
  - tools/validators/domains/people-dna-land/README.md
  - tools/validators/domains/people-dna-land/validate_consent_overlay.py
tags: [kfm, adr, people-dna-land, genealogy, validators, tooling-placement, directory-rules]
notes:
  - "This record begins proposed; file presence, a commit, a pull request, a merge, or an index row does not accept it."
  - "This record authorizes no dependent implementation, migration, release, deployment, promotion, publication, source activation, or repository-settings change before an explicit reviewed acceptance transition."
  - "Raised from docs/registers/DRIFT_REGISTER.md's 2026-09-26 genealogy-validator-placement entry, itself filed per docs/domains/people-dna-land/sublanes/genealogy.md §16's own instruction to log this conflict."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0042 — People/DNA/Land genealogy validator tooling uses `tools/validators/domains/people-dna-land/`, not a genealogy sublane

> **Proposed decision.** KFM will treat `tools/validators/domains/people-dna-land/` — the whole-domain validator lane already established and populated for all thirteen domains — as the sole home for genealogy-concern validator tooling (GEDCOM conformance, consent receipts, overlay pointers, and related checks), and will retire `tools/validators/genealogy/` as a tooling home through a bounded migration rather than continue populating it.

> [!IMPORTANT]
> **This ADR is proposed.** It is not binding until the source record and canonical index carry a synchronized, reviewed acceptance transition. Dependent implementation — moving `screen_living_persons.py`, implementing `validate_gedcom.py`/`validate_consent_receipt.py`/`validate_overlay_pointer.py`, or editing `tools/validators/genealogy/README.md` — must not treat this proposal as already-adopted authority.

> [!NOTE]
> **Non-effects.** This record does not by itself move any file, implement any validator, change CI wiring, decide the separate `docs/domains/people-dna-land/sublanes/` documentation-layer question (`OQ-PEOPLE-SUB-01`/`OQ-PEOPLE-SUB-02`), grant consent/rights/policy authority, or authorize release, deployment, or publication.

**Quick navigation:** [Status](#1-status-and-authority) · [Evidence](#2-evidence-boundary) · [Context](#3-context) · [Decision](#4-decision) · [Consequences](#5-consequences-and-risks) · [Alternatives](#6-alternatives-considered) · [Implementation](#7-implementation-migration-and-compatibility) · [Validation](#8-validation-and-acceptance) · [Rollback](#9-rollback-correction-and-supersession) · [Sensitivity](#10-security-rights-sensitivity-and-sovereignty) · [Open work](#11-open-questions-and-verification-backlog) · [References](#12-evidence-and-references) · [History](#13-change-history)

---

## 1. Status and authority

| Field | Current value |
|---|---|
| **ADR ID** | `ADR-0042` — unique in [`INDEX.md`](./INDEX.md) at this evidence snapshot |
| **Tracked path** | `docs/adr/ADR-0042-people-dna-land-genealogy-validator-tooling-home.md` |
| **Source metadata** | `proposed` |
| **Effective decision status** | `proposed` — not binding |
| **Decision class** | `structural` (validator tooling placement within an already-existing responsibility root) |
| **Decision scope** | Which path is canonical for genealogy-concern validator entrypoints under `tools/validators/` |
| **Primary authority owner** | People/DNA/Land domain steward (`NEEDS VERIFICATION` — no verified named individual) |
| **Required reviewers** | Architecture steward; Docs steward; People/DNA/Land domain steward; genealogy/consent steward |
| **Governing authority** | Directory Rules §12 (adopted via accepted `ADR-0029`); `tools/validators/domains/*` established convention |
| **Implementation maturity** | `absent` for the decision itself; `partial` for the underlying validator concerns (see §2) |
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
| Implementation maturity | `partial` — one real validator (`screen_living_persons.py`) exists at the disputed path; three sibling concerns are one-line stubs; overlapping consent/overlay concerns already have substantive implementations at the recommended path | Repository inspection, this snapshot |
| KFM lifecycle/release | Not applicable | This is a tooling-placement decision, not a data lifecycle change |
| Hosted validation | `NOT RUN` — no hosted CI observed for this proposal | Local-only checks in §8 |

### 1.2 Scope

**In scope**

- Whether `tools/validators/genealogy/` or `tools/validators/domains/people-dna-land/` is the canonical home for genealogy-concern validator entrypoints (GEDCOM conformance, consent-receipt validation, overlay-pointer validation, and closely related checks).
- Disposition of the one existing implementation currently at the disputed path (`tools/validators/genealogy/screen_living_persons.py` and its test).
- Disposition of the three pending one-line placeholder stubs at that same disputed path.

**Out of scope / explicitly unchanged**

- Whether `docs/domains/<domain>/sublanes/` is a ratified documentation convention at all (`OQ-PEOPLE-SUB-01`).
- Whether genealogy is a standalone sublane or folds into "people" (`OQ-PEOPLE-SUB-02`).
- `policy/consent/people/` vs. `policy/domains/people-dna-land/consent/` canonicality (`OQ-GEN-12`) — a separate, already-flagged `CONFLICTED` question in the same source document.
- Any consent, rights, policy, evidence, release, or publication decision for genealogy data itself.
- Any change to `docs/domains/people-dna-land/sublanes/genealogy.md`'s substantive genealogy doctrine beyond its §14.1 validator-path table.

[Back to top](#top)

---

## 2. Evidence boundary

| Evidence surface | Truth label | Current observation | What it proves — and does not prove |
|---|---|---|---|
| `docs/domains/people-dna-land/sublanes/genealogy.md` §14.1 | `CONFIRMED` | Proposes `tools/validators/people-dna-land/validate_gedcom.py`, `.../validate_consent_receipt.py`, `.../validate_overlay_pointer.py` (no `domains/` segment) and states "[a] flat `tools/validators/genealogy/` home (used in an earlier draft) would presuppose the unresolved sublane partition," citing Directory Rules §12. | Proves the doc's own proposed path and its rejection of a `genealogy/` segment. Does not prove the proposed path matches the repository's actual established convention (it does not — see next row). The document itself is `status: draft` / `truth_posture: PROPOSED`, not an accepted contract. |
| `docs/doctrine/directory-rules.md` §12.2 (adopted via `ADR-0029`) | `CONFIRMED` | The domain-lane pattern illustrates `docs/domains/<domain>/`, `contracts/domains/<domain>/`, `schemas/contracts/v1/domains/<domain>/`, `policy/domains/<domain>/`, `tests/domains/<domain>/`, `fixtures/domains/<domain>/`, `packages/domains/<domain>/`, `pipelines/<stage>/<domain>/`, `pipeline_specs/<domain>/`, `data/<lane>/<domain>/`, `release/<object_family>/<domain>/` — every illustrated root inserts a `domains/` segment before the domain slug. `tools/validators/` is not itself named in this illustrative list. | Proves the adopted convention is `<root>/domains/<domain-slug>/`, not `<root>/<domain-slug>/`, everywhere it is illustrated. Does not by itself name `tools/validators/` as covered by §12.2's illustration; the extension to `tools/validators/domains/<domain>/` rests on repository convention (next row), not on an explicit §12.2 line item. |
| `tools/validators/domains/` directory listing | `CONFIRMED` | Contains the 13 registered core domain subdirectories — `agriculture`, `archaeology`, `atmosphere`, `fauna`, `flora`, `geology`, `habitat`, `hazards`, `hydrology`, `people-dna-land`, `roads-rail-trade`, `settlements-infrastructure`, `soil` — each with `validate_catalog_matrix.py`, `validate_schema.py`, `validate_evidence_bundle.py`, and (for most) `validate_source_descriptor.py`, all delegating to shared validators per commits `f1f35720`, `8ffce28a`, `00c253ff`, `b0f1076d` — plus one additional confirmed-implementation lane, `water_planning`, for 14 populated lanes total at this snapshot. | Proves `tools/validators/domains/<domain-slug>/` is the actual, already-implemented, repository-wide convention for domain-scoped validator entrypoints, adopted beyond the 13 registered domains — independent of and pre-dating this ADR. |
| `tools/validators/domains/people-dna-land/` directory listing | `CONFIRMED` | Already contains `README.md`, `validate_catalog_matrix.py`, `validate_schema.py`, `validate_evidence_bundle.py`, `validate_source_descriptor.py`, plus two substantive, non-stub validators: `validate_consent_overlay.py` (blob `c7e3caad59e7a5a99bf935b234ac5d244533e976`, validates the `ConsentedGenealogyOverlayCandidate` object family — opaque overlay pointers, expiry, privacy) and `validate_consent_revocation_propagation_assessment.py` (blob `bb09bd6dcbfdb8d3e4da9a5df837d7da18915a84`, validates consent-revocation propagation across seven surfaces). | Proves this path already carries substantive, working validators for concerns that overlap the "Overlay pointer validator" and "Consent receipt validator" rows in `genealogy.md` §14.1. Does not prove those two files are a complete substitute for the three pending stubs; scope overlap versus full coverage is `NEEDS VERIFICATION` (see §11). |
| `tools/validators/genealogy/` directory listing | `CONFIRMED` | Contains `README.md`, one real tested validator (`screen_living_persons.py`, blob `bca6eefb350360f79ae4bbab8ff9741b554df334`, delegating to `validate_historical_person_place_event_resolution`, backed by `tests/validators/test_screen_living_persons.py`, blob `794ab5c4291f4c6174eaa387887f45214021d115`), and three one-line placeholder stubs (`validate_gedcom.py`, `validate_consent_receipt.py`, `validate_overlay_pointer.py`, each generated from `genealogy.md`'s own inventory pass). | Proves the disputed path already carries real, tested behavior — this is not a clean-slate choice; a decision against this path has migration cost. |
| `tools/validators/genealogy/README.md` | `CONFIRMED` | States this lane "is the proposed shared validator lane for checking genealogy claims" and separately acknowledges "an unresolved sublane-placement ADR question" without naming an ADR ID, and says the README "does not move, replace, or override" the domain roots it lists (which include `tools/validators/domains/people-dna-land/` as "Per-domain People/DNA/Land validator index"). | Proves the README's own author(s) already knew of the open placement question and deliberately did not resolve it. Does not itself constitute an ADR or a placement decision. |
| `docs/registers/DRIFT_REGISTER.md` (2026-09-26 entry, this branch) | `CONFIRMED` | Logs this exact conflict per `genealogy.md` §16's instruction that CONFLICTED rows "will additionally appear in `docs/registers/DRIFT_REGISTER.md`." | Proves the conflict was visible and tracked before this ADR; this ADR is the register's own named resolution path, not a new finding. |
| `docs/adr/INDEX.md` | `CONFIRMED` | At blob `a937b4c5a81e0b36b44a2fc14d7df046db388fe2`, the numbered sequence is complete and unique `ADR-0001`–`ADR-0041`; no open pull request or `ADR-0042` file existed prior to this change (checked via repository code search). | Establishes `ADR-0042` as the next collision-free number at this snapshot. |

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

`docs/domains/people-dna-land/sublanes/genealogy.md` §14.1 proposed three genealogy validators — a GEDCOM conformance reporter, a consent-receipt validator, and an overlay-pointer validator — at `tools/validators/people-dna-land/<name>.py`, and included an explicit `[!NOTE]` rejecting a flat `tools/validators/genealogy/` home as presupposing an unresolved sublane partition. A code-generation pass later created the three placeholder stub files not at the doc's own proposed path, but at the rejected `tools/validators/genealogy/` path — the same path where a fourth, real, tested validator (`screen_living_persons.py`) had already been built. Neither the doc's proposed path (`tools/validators/people-dna-land/`, no `domains/` segment) nor the stubs' actual path (`tools/validators/genealogy/`) matches the convention the repository has since built out at scale: `tools/validators/domains/<domain-slug>/`, populated for all thirteen domains including `people-dna-land`, which already carries two substantive validators covering closely related consent/overlay concerns.

Left unresolved, implementing the three pending stubs in place would silently ratify a path that both the domain's own planning document and the repository's actual established convention reject, and would risk building a second, overlapping consent/overlay validator lane alongside the one that already exists at `tools/validators/domains/people-dna-land/`.

### 3.1 Decision drivers

- **Consistency with an already-adopted, already-implemented convention** — thirteen domains, including `people-dna-land` itself, already use `tools/validators/domains/<domain>/`. A fourteenth pattern for the same domain creates avoidable inconsistency.
- **Avoiding duplicate authority** — `validate_consent_overlay.py` already validates overlay-pointer-shaped concerns at the recommended path; a second implementation at a second path risks two validators disagreeing about the same object family.
- **Respecting the domain's own planning document** — `genealogy.md` §14.1 itself rejects `tools/validators/genealogy/`; whatever the final answer, it should not be the path the domain's own doctrine already disclaims.
- **Reversibility** — one real file (`screen_living_persons.py`) and its test currently sit at the disputed path; the decision should keep migration bounded and cheap rather than let more implementation accumulate there first.
- **Not deciding more than necessary** — the sublane documentation-layer questions (`OQ-PEOPLE-SUB-01`/`OQ-PEOPLE-SUB-02`) and the consent-policy-home question (`OQ-GEN-12`) are separable from a tooling-path decision and should not be bundled into it.

### 3.2 Current conflict or gap

| Surface | Current state | Conflict or gap |
|---|---|---|
| `tools/validators/genealogy/validate_gedcom.py`, `validate_consent_receipt.py`, `validate_overlay_pointer.py` | One-line `PROPOSED placeholder` stubs | Sit at a path `genealogy.md` §14.1 explicitly rejects |
| `tools/validators/genealogy/screen_living_persons.py` + test | Real, tested implementation | Sits at the same rejected path; already has committed consumers (its test) |
| `tools/validators/domains/people-dna-land/` | Real, tested implementations for overlapping consent/overlay concerns | Not the path `genealogy.md` names, and not the path the stubs were generated into |
| `genealogy.md` §14.1 proposed path (`tools/validators/people-dna-land/`, no `domains/` segment) | Does not exist | Does not match the repository's actual thirteen-domain convention |

### 3.3 Non-goals

- This ADR does not decide the `sublanes/` documentation convention question.
- This ADR does not decide whether `validate_consent_overlay.py` or `validate_consent_revocation_propagation_assessment.py` fully satisfy the "Consent receipt validator" and "Overlay pointer validator" rows of `genealogy.md` §14.1, or whether additional, narrower validators are still needed at the recommended path.
- This ADR does not authorize moving, deleting, or implementing any file.

[Back to top](#top)

---

## 4. Decision

> **Decision:** KFM will treat `tools/validators/domains/people-dna-land/` as the sole canonical home for genealogy-concern validator entrypoints, retire `tools/validators/genealogy/` as a tooling home through a reviewed migration, and implement the three pending genealogy validator stubs — if and when a domain steward confirms they remain needed alongside the existing consent/overlay validators — only at the recommended path.

### 4.1 Normative rules

1. **MUST** — New genealogy-concern validator entrypoints for the People/DNA/Land domain are added only under `tools/validators/domains/people-dna-land/`.
2. **MUST NOT** — No new file is added under `tools/validators/genealogy/` after this ADR's acceptance.
3. **SHOULD** — `screen_living_persons.py` and `tests/validators/test_screen_living_persons.py` are migrated to `tools/validators/domains/people-dna-land/` in a dedicated, reviewed follow-up change once this decision is accepted, preserving its existing behavior and test coverage exactly.
4. **SHOULD** — Before implementing `validate_gedcom.py`, `validate_consent_receipt.py`, or `validate_overlay_pointer.py` at the recommended path, a domain/consent steward confirms whether `validate_consent_overlay.py` and `validate_consent_revocation_propagation_assessment.py` already satisfy part or all of the "Consent receipt validator" and "Overlay pointer validator" rows, to avoid building a second, overlapping implementation.
5. **MAY** — `tools/validators/genealogy/README.md`'s content may be merged into `tools/validators/domains/people-dna-land/README.md` as part of the same migration follow-up, provided no substantive claim is silently dropped.

### 4.2 Responsibility and placement

| Axis | Decision |
|---|---|
| `artifact_kind` | `executable` (validator entrypoints) plus `test` |
| `authority_owner` | People/DNA/Land domain steward (tooling); genealogy/consent steward (validated concerns) |
| `lifecycle_stage` | n/a — repository tooling, not lifecycle data |
| `execution_role` | `tool` (validator) |
| `scope_kind` / `scope_id` | `domain` / `people-dna-land` |
| `exposure` | internal (repository tooling; no public surface) |
| `mutability` / `retention` | versioned; durable |
| Candidate path | `tools/validators/domains/people-dna-land/{validate_gedcom,validate_consent_receipt,validate_overlay_pointer,screen_living_persons}.py` |
| Governing rule IDs / accepted ADRs | Directory Rules §12.2 (via accepted `ADR-0029`); repository convention established by commits `f1f35720`, `8ffce28a`, `00c253ff`, `b0f1076d` |
| Placement outcome | `MIGRATE` (for `screen_living_persons.py` and its test) / `PLACE` (for the three pending stubs, once implemented) |
| Parallel-authority posture | Explicitly denies a second, permanent genealogy-scoped validator lane; `tools/validators/genealogy/` becomes a migration-only, non-authoritative path pending retirement |

### 4.3 Authority and public-boundary rules

- Public clients are not affected — these are internal, no-network repository validators with no public route.
- Evidence-dependent claims are unaffected; this ADR does not change how any validator resolves `EvidenceRef`/`EvidenceBundle`.
- Policy, rights, sensitivity, review, and release decisions for genealogy or consent data are unaffected; this ADR is a tooling-path decision only.
- Derived maps, tiles, graphs, indexes, summaries, and generated language are unaffected.

### 4.4 Non-effects

This decision does not:

- decide `OQ-PEOPLE-SUB-01` (whether `docs/domains/<domain>/sublanes/` is a ratified convention) or `OQ-PEOPLE-SUB-02` (standalone genealogy sublane vs. folding into "people");
- decide `OQ-GEN-12` (`policy/consent/people/` vs. `policy/domains/people-dna-land/consent/`);
- move, delete, or implement any file by itself;
- grant consent, rights, policy, evidence, review, or release authority; or
- authorize release, deployment, promotion, or publication.

[Back to top](#top)

---

## 5. Consequences and risks

### 5.1 Positive consequences

- One consistent, already-proven convention (`tools/validators/domains/<domain>/`) covers all thirteen domains without a fourteenth exception.
- Removes the risk of two independent, possibly-diverging validators for the same overlay/consent object families.
- Resolves a conflict `genealogy.md` §16 itself flagged as requiring a `DRIFT_REGISTER.md` entry and, implicitly, a decision.
- Keeps migration bounded: exactly one real file plus one test move, not a large rewrite.

### 5.2 Negative consequences and costs

- Requires a follow-up migration PR (moving `screen_living_persons.py` and its test, updating any inbound references) before the decision is fully realized.
- `tools/validators/genealogy/README.md`'s content needs reconciliation or retirement, which is additional review-bounded work.
- Domain/consent steward review is needed before implementing the three pending stubs, which may delay their completion relative to simply finishing them in place.

### 5.3 Accepted tradeoffs

This ADR favors consistency with the repository's proven, already-scaled convention over preserving the exact path a since-superseded planning document proposed, and over the path convenience of leaving one working file where it already sits.

### 5.4 Affected surfaces

| Responsibility surface | Current path(s) | Required change | Authority / compatibility note |
|---|---|---|---|
| ADR source and index | `docs/adr/...` | Add `ADR-0042`; update `INDEX.md` and `README.md` snapshot counts | Decision record only |
| Validator tooling | `tools/validators/genealogy/`, `tools/validators/domains/people-dna-land/` | Migrate `screen_living_persons.py` + test; implement three stubs at the recommended path (follow-up, not this change) | Enforceability; no change in this ADR itself |
| Tests | `tests/validators/test_screen_living_persons.py` | Path update to match migrated validator (follow-up) | No behavior change intended |
| Documentation | `tools/validators/genealogy/README.md`, `tools/validators/domains/people-dna-land/README.md`, `docs/domains/people-dna-land/sublanes/genealogy.md` §14.1 | Reconcile after migration (follow-up) | Explanation only |
| Drift register | `docs/registers/DRIFT_REGISTER.md` | Cross-reference this ADR once accepted (follow-up append) | Register entry, not authority |
| Contracts/Schemas/Policy/Data/Release | — | Not affected | Out of scope |

### 5.5 Risk ledger

| Risk | Likelihood / impact | Mitigation | Residual risk / owner |
|---|---|---|---|
| Migration breaks `screen_living_persons.py`'s existing consumers | Low / medium | Move file and test together in one reviewed PR; re-run the test at the new path before merge | Residual: any undiscovered external reference; owner: migration PR author |
| Three pending stubs get implemented before steward review confirms non-duplication | Medium / medium | This ADR's §4.1 rule 4 makes review a precondition; CI/reviewer checklist should cite this ADR | Residual: relies on reviewer discipline until a validator enforces it; owner: reviewing steward |
| Decision stalls without a confirmed steward, mirroring `genealogy.md`'s own unresolved-owner state | Medium / low | Acceptance can proceed on architecture-steward review alone per the bootstrap pattern used by `ADR-0029`; domain steward review remains strongly preferred | Residual: bootstrap-exception style acceptance; owner: whoever accepts this ADR |

[Back to top](#top)

---

## 6. Alternatives considered

### 6.1 Selected option — `tools/validators/domains/people-dna-land/`

- **Summary:** Use the already-established, already-populated, repository-wide thirteen-domain convention.
- **Why selected:** It already exists, already carries substantive overlapping validators, and requires no new convention to be invented or separately justified.

### 6.2 Alternative A — `tools/validators/people-dna-land/` (as literally proposed by `genealogy.md` §14.1)

- **Summary:** Follow the exact path text in the domain's own planning document.
- **Why rejected:** It does not match the `domains/`-segmented pattern used everywhere else in the repository for this exact purpose, including for this exact domain (`tools/validators/domains/people-dna-land/` already exists); adopting it would create a second, inconsistent domain-tooling convention rather than resolve one.

### 6.3 Alternative B — Keep `tools/validators/genealogy/`

- **Summary:** Ratify the path the stubs and `screen_living_persons.py` already occupy.
- **Why rejected:** Directly contradicted by `genealogy.md`'s own explicit rejection of this path, and by Directory Rules §12's domain-lane pattern, which never uses a bare sublane-style segment in place of a domain slug.

### 6.4 Status quo

- **Summary:** Leave the conflict open; implement nothing further at either path until some other process resolves it.
- **Why rejected:** The conflict is already blocking (further stub implementation risks silently ratifying a rejected path), already flagged for exactly this kind of resolution by `genealogy.md` §16 and the drift register, and costs nothing to formally decide now given the evidence already assembled.

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
| 3 | Migrate `screen_living_persons.py` + test to `tools/validators/domains/people-dna-land/`; update any inbound references | Accepted ADR | Implementation review | yes (git revert) |
| 4 | Steward confirms scope overlap with `validate_consent_overlay.py`/`validate_consent_revocation_propagation_assessment.py`, then implement the three pending stubs (or a narrower subset) at the recommended path | Accepted ADR + step 3 | Implementation review | yes |
| 5 | Reconcile `tools/validators/genealogy/README.md` and `genealogy.md` §14.1 to point at the new path; retire the empty `tools/validators/genealogy/` directory | Steps 3–4 | Docs review | yes |

### 7.2 Migration and compatibility plan

- **Old → new mapping:** `tools/validators/genealogy/screen_living_persons.py` → `tools/validators/domains/people-dna-land/screen_living_persons.py`; `tests/validators/test_screen_living_persons.py` path updated to match.
- **Migration manifest/note:** Not applicable — a single-file `git mv` plus test-path update, described in the migration PR description.
- **Producer cutover:** N/A (no producer writes these files at runtime).
- **Consumer migration:** Any script or CI step invoking `tools/validators/genealogy/screen_living_persons.py` by path must be updated in the same migration PR.
- **Mirror/alias class:** `none` — no compatibility shim is proposed; the file count is small enough for a direct move.
- **Compatibility window and exit criteria:** None needed; direct move.
- **Identity preservation or versioning:** Preserve `git mv` history; do not rewrite the file's logic as part of the move.
- **Backfill or transform:** Not applicable.
- **Generated-output regeneration:** Not applicable.
- **Reference/link repair:** Update any Markdown links to the old path (`genealogy.md` §14.1, `tools/validators/genealogy/README.md`, this ADR's own follow-up references) in the same or an immediately following PR.
- **Correction of released references:** Not applicable — no release object cites these paths.
- **Destructive cleanup:** Delete `tools/validators/genealogy/` only after the migration PR merges and no reference to it remains.

### 7.3 Direct dependency closure

| Artifact | Why directly required | Planned path | Validation |
|---|---|---|---|
| `screen_living_persons.py` | Only real implementation currently at the disputed path | `tools/validators/domains/people-dna-land/screen_living_persons.py` | Re-run `python tools/validators/domains/people-dna-land/screen_living_persons.py --fixtures` at the new path |
| `test_screen_living_persons.py` | Pins the validator's path today | `tests/validators/test_screen_living_persons.py` (content updated to new `SCRIPT` path) | `python -m pytest tests/validators/test_screen_living_persons.py -q` |
| `tools/validators/genealogy/README.md` | Documents the lane being retired | Merge relevant content into `tools/validators/domains/people-dna-land/README.md` | Manual review; no automated check known |

### 7.4 Deferred work

- Implementing the three pending stub validators at the recommended path (contingent on steward confirmation per §4.1 rule 4).
- Any change to `OQ-PEOPLE-SUB-01`, `OQ-PEOPLE-SUB-02`, or `OQ-GEN-12` — explicitly out of scope here.

[Back to top](#top)

---

## 8. Validation and acceptance

### 8.1 Checks performed for this proposal

| Check / command / inspection | Scope | State | Exact evidence |
|---|---|---|---|
| `python tools/validators/validate_adr_index.py` | ADR inventory coherence | `PASS` | `PASS: ADR index coherence (42 numbered records, 11 unassigned scaffolds)` re-run after this change's `INDEX.md` update |
| `python -m pytest tests/validators/test_validate_adr_index.py -q --strict-config --strict-markers` | ADR validator failure paths | `PASS` | `8 passed` |
| Repository code search for `ADR-0042` | Number-collision check | `PASS` | Zero real files matched; two incidental example/placeholder mentions in a prompt-template doc and a validator test fixture, neither creating a real `ADR-0042` file |
| `git log` inspection of `f1f35720`, `8ffce28a`, `00c253ff`, `b0f1076d` | Confirms the thirteen-domain `tools/validators/domains/<domain>/` convention predates this ADR | `PASS` (inspection only) | Commit subjects and diffs reviewed directly |
| Hosted checks | Exact pull-request head | `NOT RUN` | No pull request opened yet |

### 8.2 Acceptance criteria

| Criterion | Required evidence | Current state | Owner/reviewer |
|---|---|---|---|
| Decision is singular and unambiguous | One directive (§4) | Met | Architecture steward |
| Current facts are pinned and truth-labeled | §2 evidence table | Met | Docs steward |
| Governing authority is sufficient | Directory Rules §12 + established convention cited | Met | Architecture steward |
| Placement and ownership are deterministic | §4.2 responsibility signature | Met | Architecture steward |
| Alternatives and consequences are complete | §5–§6 | Met | Architecture steward |
| Migration and rollback are executable | §7, §9 | Met (described; not yet executed) | Implementation reviewer |
| Security, rights, sensitivity, sovereignty addressed | §10 | Met (mostly not-applicable, explicitly stated) | Genealogy/consent steward |
| Required reviewers acted | Review evidence | `NOT MET` — no review yet | People/DNA/Land + genealogy/consent stewards |
| ADR source and canonical index agree | Validator pass after index update | `PENDING` this change's own index update | Docs steward |
| Dependent implementation remains correctly ordered | §7.1 sequencing | Met | Implementation reviewer |

### 8.3 Current enforcement maturity

| Capability | Current state | Acceptance blocker? |
|---|---|---:|
| Contract/schema/policy support | Not applicable (tooling-placement decision) | no |
| Fixtures and negative tests | `screen_living_persons.py`'s existing fixture suite is unaffected by this proposal | no |
| Validator/CI coverage | ADR-index validator only; no validator enforces this specific placement rule yet | no |
| Producer/consumer migration | Not yet executed (deferred to §7) | no — deferred by design |
| Runtime/API/UI behavior | Not applicable | no |
| Release/correction/rollback proof | Not applicable | no |

### 8.4 Post-acceptance verification

- Confirm the migration PR moves exactly `screen_living_persons.py` and its test, with no logic change.
- Confirm `tools/validators/genealogy/` is empty (or removed) after migration and reference repair.
- Confirm the domain/consent steward's scope-overlap finding (§4.1 rule 4) is recorded before any of the three pending stubs are implemented.
- Update `docs/registers/DRIFT_REGISTER.md` with a short append-only note pointing to this ADR once accepted.

[Back to top](#top)

---

## 9. Rollback, correction, and supersession

### 9.1 Documentation rollback

- **Prior blob / commit:** Not applicable — new file; revert is `git rm docs/adr/ADR-0042-people-dna-land-genealogy-validator-tooling-home.md` plus reverting the paired `INDEX.md`/`README.md` edits.
- **Revert procedure:** Standard `git revert` of the introducing commit.
- **Validation after revert:** Re-run `python tools/validators/validate_adr_index.py`.

### 9.2 Implementation rollback or forward fix

- **Trigger conditions:** Migration PR breaks `screen_living_persons.py`'s behavior, an undiscovered consumer of the old path surfaces, or a steward determines `tools/validators/domains/people-dna-land/` is not in fact the right home.
- **Rollback steps:** `git revert` the migration commit, restoring the file at `tools/validators/genealogy/`.
- **Forward-fix requirement if rollback is unsafe:** If other work has already built on the new path, patch forward (fix the break in place) rather than reverting.
- **Compatibility after rollback:** No parallel writable authority is created either way — exactly one location is ever canonical at a time.
- **Data/release correction:** Not applicable.
- **Rollback must not recreate two writable authorities** — do not restore `tools/validators/genealogy/` while also keeping a duplicate at the new path.

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
| Security-sensitive behavior or vulnerability detail | no | — | This is a file-path decision for internal tooling |
| Rights, license, source terms, or redistribution | no | — | No source or data is touched |
| Archaeology, cultural, Indigenous, burial, or sacred context | no | — | Not applicable to this domain/decision |
| Rare species, rare plants, habitat, or geoprivacy | no | — | Not applicable |
| Critical infrastructure or emergency operations | no | — | Not applicable |
| Living-person, genealogy, consent, DNA, or genomic data | yes — indirectly | Genealogy/consent steward review of §4.1 rule 4 before stub implementation | `screen_living_persons.py` and the two existing consent/overlay validators already implement fail-closed, synthetic-only behavior; this ADR does not change that behavior, only their file location |
| Private land or exact harmful location | no | — | Not applicable |

Unknown or unresolved high-risk handling returns `HOLD` or `DENY`; it is not solved by a disclaimer. Because the underlying validators already enforce fail-closed, synthetic-only, non-release behavior, this ADR's file-placement decision does not itself introduce a new sensitivity exposure.

[Back to top](#top)

---

## 11. Open questions and verification backlog

| Item | Status | Why unresolved | Owner / next evidence | Blocks |
|---|---|---|---|---|
| Do `validate_consent_overlay.py` / `validate_consent_revocation_propagation_assessment.py` already satisfy the "Consent receipt validator" / "Overlay pointer validator" rows of `genealogy.md` §14.1? | `NEEDS VERIFICATION` | Requires a domain/consent steward to compare declared scopes field-by-field | Genealogy/consent steward | Implementation of the three pending stubs (§4.1 rule 4) |
| Who is the verified People/DNA/Land domain steward and genealogy/consent steward? | `NEEDS VERIFICATION` | No verified individual found in this session's evidence | Repository owner / CODEOWNERS update | Formal acceptance review |
| Should `tools/validators/genealogy/README.md`'s narrative content be preserved elsewhere, or is it fully superseded by `tools/validators/domains/people-dna-land/README.md`? | `NEEDS VERIFICATION` | Not compared line-by-line in this pass | Docs steward, at migration time | §7.1 step 5 |
| Does this decision have any bearing on `OQ-PEOPLE-SUB-01`/`OQ-PEOPLE-SUB-02`/`OQ-GEN-12`? | `CONFIRMED` — no, by design (§3.3, §4.4) | Explicitly scoped out | — | Nothing; recorded for clarity |

Do not hide unresolved acceptance blockers in prose. Track the steward-identity gap through the repository's normal ownership process, not through a second ADR.

[Back to top](#top)

---

## 12. Evidence and references

### 12.1 Repository evidence ledger

| Evidence | Immutable identity | Claim supported | Limit |
|---|---|---|---|
| `docs/adr/INDEX.md` | blob `a937b4c5a81e0b36b44a2fc14d7df046db388fe2` | 41 numbered records exist; `ADR-0042` is next | Snapshot only; re-verify before merge |
| `docs/doctrine/directory-rules.md` | blob `fd49a0b83e55cef52c1124281f093e263526898d` | §12.2 domain-lane pattern text | Adopted via `ADR-0029`; does not itself name `tools/validators/` |
| `docs/domains/people-dna-land/sublanes/genealogy.md` | blob `61b38c06781006a63e7ab124f0506cecdf07f292` | §14.1 proposed paths and rejection note; §16 drift-register instruction | `status: draft`; not an accepted contract |
| `tools/validators/genealogy/README.md` | blob `52f75c4755524533534acb655abcefc3ccbbeaf8` | Acknowledges unresolved placement question | Not an ADR |
| `tools/validators/genealogy/screen_living_persons.py` | blob `bca6eefb350360f79ae4bbab8ff9741b554df334` | Real, tested implementation exists at the disputed path | — |
| `tests/validators/test_screen_living_persons.py` | blob `794ab5c4291f4c6174eaa387887f45214021d115` | Pins the validator's current path | — |
| `tools/validators/domains/people-dna-land/validate_consent_overlay.py` | blob `c7e3caad59e7a5a99bf935b234ac5d244533e976` | Substantive overlay-pointer-adjacent validator already exists at the recommended path | Scope overlap with the pending stub is `NEEDS VERIFICATION` |
| `tools/validators/domains/people-dna-land/validate_consent_revocation_propagation_assessment.py` | blob `bb09bd6dcbfdb8d3e4da9a5df837d7da18915a84` | Substantive consent-adjacent validator already exists at the recommended path | Scope overlap with the pending stub is `NEEDS VERIFICATION` |
| `tools/validators/domains/people-dna-land/README.md` | blob `7a78d278aa03d843107d4d66a954c7a670d2ac19` | Documents the recommended path's existing scope | Does not itself name GEDCOM/consent-receipt/overlay-pointer concerns |
| `docs/registers/DRIFT_REGISTER.md` | blob `109128fb5cb671e54d5029863e4897dc708dcdea` (post-edit, this branch) | Conflict was logged before this ADR | Pending merge to `main` alongside this ADR |
| Commits `f1f35720`, `8ffce28a`, `00c253ff`, `b0f1076d` | Commit SHAs as recorded in `git log` | Establish the thirteen-domain `tools/validators/domains/<domain>/` convention predates this ADR | Commit messages and diffs, not independently re-verified line-by-line here |

### 12.2 Governing decisions and doctrine

- [`ADR-0029`](./ADR-0029-adopt-directory-governance-standard-v2.md) — accepted adoption of Directory Rules v2, including §12.2's domain-lane pattern.
- [`docs/doctrine/directory-rules.md`](../doctrine/directory-rules.md) §12.

### 12.3 External primary sources

- Not applicable — this decision rests entirely on repository-internal evidence.

### 12.4 Source lineage

- [`docs/domains/people-dna-land/sublanes/genealogy.md`](../domains/people-dna-land/sublanes/genealogy.md) §14.1 and §16 — proposal lineage for the validator paths and the instruction to log this conflict.
- [`docs/registers/DRIFT_REGISTER.md`](../registers/DRIFT_REGISTER.md) — the 2026-09-26 entry this ADR resolves.

[Back to top](#top)

---

## 13. Change history

| Date | Record status | Change | Evidence / PR |
|---|---|---|---|
| 2026-09-26 | proposed | Initial repository record | This change |

[Back to top](#top)

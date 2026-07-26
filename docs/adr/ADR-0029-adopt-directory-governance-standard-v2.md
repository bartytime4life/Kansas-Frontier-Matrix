<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://adr/ADR-0029
title: Adopt Directory Governance Standard v2
type: adr
version: v1
status: proposed
owners: ["@bartytime4life"]
created: 2026-07-26
updated: 2026-07-26
policy_label: public
related:
  - "docs/doctrine/directory-rules.md"
  - "docs/architecture/directory-rules.md"
  - "docs/adr/README.md"
  - "docs/adr/INDEX.md"
  - "docs/registers/ADR_INDEX.md"
  - "docs/registers/DRIFT_REGISTER.md"
  - "docs/registers/VERIFICATION_BACKLOG.md"
tags: [adr, kfm, directory-rules, doctrine, governance, placement, migration]
supersedes: []
superseded_by: []
notes:
  - "This record remains proposed. It does not adopt Directory Rules v2 or authorize the dependent legacy-path migration until an explicit reviewed transition changes this ADR to accepted."
  - "CODEOWNERS routes review to @bartytime4life; that route is not independent approval, a StewardshipAssignment, or proof that review occurred."
  - "PR #1763 restored the verified v2 bytes and merged this proposed record; that merge did not accept the decision or alter the legacy architecture path."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0029: Adopt Directory Governance Standard v2

If accepted after explicit governance and independent review, this decision adopts the exact verified UTF-8 bytes of Directory Rules `2.0.0-draft.1` at `docs/doctrine/directory-rules.md`, makes that path the single human-readable Directory Rules authority, and starts a controlled compatibility migration for the legacy architecture copy. While this ADR remains `proposed`, it has no adoption or supersession effect.

| Field | Value |
|---|---|
| **ID** | `ADR-0029` |
| **Status** | `proposed` |
| **Date** | 2026-07-26 |
| **Repository review route** | `@bartytime4life` via CODEOWNERS; this is routing, not decision authority or approval evidence |
| **Decision authority** | `NEEDS VERIFICATION` — verified stewardship assignments and acceptance approvers are not recorded |
| **Acceptance evidence** | Explicit decision review from every verified named owner, recorded approvers, reverified bytes, and a matching ADR/index status transition |
| **Consulted** | KFM doctrine, the two Directory Rules bodies, supplied source artifacts, and pinned repository evidence |
| **Informed** | All repository contributors and consumers of Directory Rules paths or fragments |
| **Supersedes** | No prior ADR |
| **Superseded by** | — |
| **Directory Rules trigger** | v2 §2.2 `DIR-AUTH-004`, §17, §18, and §21 bootstrap adoption |
| **Primary responsibility root** | `docs/` |
| **Migration required** | yes |
| **Rollback required** | yes |
| **Evidence checkpoint** | `main@b33687e072970ae12b36c9642ae1da09f900d1f2`; ratification merge checkpoint `7b75e3bd590cd37321113f8336559060ae4c4358` |
| **Truth posture** | `CONFIRMED` evidence; `PROPOSED` decision; acceptance review `NEEDS VERIFICATION` |

> [!IMPORTANT]
> Adding or merging this record with status `proposed` does not accept it. Adoption becomes effective only when the source ADR and canonical index both carry a reviewed `accepted` state, the exact proposed content digest is reverified, and the required approvals are recorded.

**Quick navigation:** [Context](#1-context) · [Decision](#2-decision) · [Consequences](#3-consequences) · [Alternatives](#4-alternatives-considered) · [Evidence](#5-evidence-and-references) · [Migration](#6-migration-plan) · [Rollback](#7-rollback-plan) · [Open questions](#8-open-questions) · [Acceptance gates](#9-acceptance-gates) · [History](#10-change-history)

## 1. Context

KFM currently has one proposed successor and one competing legacy Directory Rules body:

| Surface | Verified state | Effect |
|---|---|---|
| `docs/doctrine/directory-rules.md` | Directory Rules `2.0.0-draft.1`; current `main` blob `fd49a0b83e55cef52c1124281f093e263526898d`; status `PROPOSED_FOR_ADOPTION` | Exact proposed successor bytes are present, but not adopted |
| `docs/architecture/directory-rules.md` | v1.3.1 `review`; blob `18653c00ba193a4afaa3e07a0924452807fb98ef` | Competing rule body and active compatibility dependency |
| `docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md` | This record; source status `proposed`; blob `533b6f577019384ec03e4531b0f5bc68bd7cb1ee` at the checkpoint | No adoption or supersession effect |
| Numbered ADR corpus | `ADR-0001` through `ADR-0029`, all effectively `proposed` | No accepted bootstrap authority |

The successor itself requires an explicit adoption decision before dependent structural work. It also requires the architecture file to become a short read-only redirect before eventual retirement. The merged ratification packet recorded 214 resolving Markdown links to the architecture path, including 83 fragment links across 30 legacy anchors. Those counts are evidence from PR #1763, not proof of external-consumer closure; immediate path deletion would create broad link and semantic breakage.

The first copy of v2 committed directly to `main` in `a6de05fa468bd91b7ac990b166b769a4505b7ce2` was not byte-faithful to the finished artifact. PR #1763 restored the exact intended UTF-8 bytes and merged as `7b75e3bd590cd37321113f8336559060ae4c4358`. That merge completed byte restoration only: ADR-0029 and its index row still say `proposed`, and the legacy architecture blob is unchanged.

### Current ratification checkpoint

| Step | State at the evidence checkpoint | Governing effect |
|---|---|---|
| Exact v2 byte restoration | **CONFIRMED complete** in merged PR #1763 | Makes the proposed bytes reviewable; does not adopt them |
| ADR-0029 decision | **PROPOSED** | Creates no placement, supersession, migration, or deletion authority |
| Legacy-path tombstone | **HELD** | Requires an effective accepted decision and a separate migration PR |
| Physical legacy-path deletion | **HOLD / not authorized** | Requires zero-writer, zero-consumer, link-closure, and retirement-receipt evidence |

### 1.1 Decision drivers

- **Single authority** — two independently editable rules bodies create contradictory placement authority.
- **Byte integrity** — adoption must pin the restored verified source, not the historically corrupted commit.
- **Governed supersession** — prior editions need exact identity, digest, lineage, and forward links.
- **Compatibility** — active path and fragment consumers require a bounded redirect and reference migration.
- **Reversibility** — the cutover must not recreate two writable authorities or erase decision history.
- **Review integrity** — repository ownership and CODEOWNERS routing do not substitute for verified stewardship, explicit decision review, or recorded approval.

### 1.2 Evidence boundary

- **CONFIRMED:** at `main@b33687e072970ae12b36c9642ae1da09f900d1f2`, the two current repository paths, their versions and blobs, the restored v2 digest, ADR-0029's `proposed` source/index state, the absence of an accepted numbered ADR, and PR #1763's recorded repository link inventory.
- **PROPOSED:** adoption of v2, the canonical identity and aliases, the tombstone window, and the migration sequence below.
- **UNKNOWN:** external consumers that are not visible through repository search.
- **NEEDS VERIFICATION:** stewardship assignments, acceptance approvers and any required independent-review control, final reference inventory at acceptance time, machine-register parity, and zero-consumer proof before physical deletion.

### 1.3 Out of scope

This ADR does not:

- accept itself;
- implement the topology validator, root registry, alias register, or CI ratchet;
- move lifecycle data, trust objects, contracts, schemas, policy, code, release records, or published material;
- approve any later root, lane, or object-family migration;
- treat the proposed v2 convergence appendix as proof that its recommendations are implemented;
- authorize immediate deletion of `docs/architecture/directory-rules.md`.

## 2. Decision

> **Decision if accepted:** Adopt the exact verified UTF-8 Directory Rules v2 bytes identified below at `docs/doctrine/directory-rules.md`; make that path the sole writable human Directory Rules authority; supersede the enumerated prior editions; and migrate the legacy architecture path through a read-only tombstone before any physical deletion.

### 2.1 Adopted artifact identity

The proposed adopted artifact is:

| Field | Proposed accepted value |
|---|---|
| Canonical path | `docs/doctrine/directory-rules.md` |
| Version | `2.0.0-draft.1` |
| Document ID | `kfm://doctrine/directory-governance/v2` |
| SHA-256 | `44f7e94344cb42b630008eb0bc03a13fcb97dbdfba6f3e56579693a272571e6e` |
| Git blob | `fd49a0b83e55cef52c1124281f093e263526898d` |
| Byte count | 80,881 |
| Line count | 1,510 plus final newline |

The digest and blob MUST be reverified immediately before an `accepted` status transition. A content change requires a new digest and renewed review; this ADR must not silently accept different bytes.

The supplied rendered companion `KFM_Directory_Governance_Standard_v2.0.0-draft.1.pdf` is 33 pages with SHA-256 `2b8db8901f893d9aabb94bb32db5cbc2e0bb0c881bf74068551e9b3b76602893`. It was inspected as a presentation and lineage artifact. Its PDF digest is not the adoption digest and does not replace the exact UTF-8 Markdown identity above.

<a id="exact-supersession-targets"></a>

### 2.2 Supersession and lineage targets

Acceptance would establish the following exact doctrinal lineage without implying that every predecessor currently has repository authority:

| Prior artifact | Exact identity | Proposed relation after acceptance |
|---|---|---|
| Supplied unversioned `Directory Rules.pdf` | 22 pages; SHA-256 `759de4fcb51cf0f55896089e397d9c47481d60d9fb80ac9a44d47b2f60a0a335` | Source-lineage predecessor only; no repository deletion target and no current repository authority |
| Prior doctrine v1.4 | Git blob `2affb080e6f0043867c64c7f06c1ca52030fbd55` | Superseded repository doctrine edition; retained in Git history |
| Architecture v1.3.1 | Git blob `18653c00ba193a4afaa3e07a0924452807fb98ef` | Superseded content edition; body replaced only in a post-adoption migration PR while the path remains a read-only compatibility surface |

The meta-block fields `supersedes` and `superseded_by` describe ADR-to-ADR relationships, so they remain empty. The table above records document-edition lineage and must not be interpreted as an ADR identity relationship or as deletion authority.

### 2.3 Stable identity and aliases

The v2 document ID `kfm://doctrine/directory-governance/v2` becomes canonical only after acceptance. The prior IDs:

- `kfm://doc/directory-rules`
- `kfm://doc/doctrine/directory-rules`

become explicit superseded aliases to the canonical v2 identity. A later machine-projection PR must record those aliases without creating independent write authority.

### 2.4 Compatibility and deletion rule

The current deletion state is **HOLD**. This proposed ADR neither performs nor authorizes deletion. After acceptance:

1. all new Directory Rules edits go only to `docs/doctrine/directory-rules.md`;
2. `docs/architecture/directory-rules.md` is replaced in a separate migration PR with a short read-only tombstone;
3. the tombstone records the prior blob, canonical target, accepted ADR, effective date, owner, expiry or exit condition, and no-independent-edits rule;
4. active references and legacy fragments are migrated or intentionally mapped;
5. the path is physically deleted only after zero-writer, zero-consumer, link-closure, and retirement-receipt validation.

Historical receipts and commit-pinned evidence are not rewritten merely to remove a legacy string.

### 2.5 Conformance language

- **MUST** keep this ADR `proposed` until explicit required review is recorded.
- **MUST NOT** treat PR #1763, its merge commit, or byte equality as adoption evidence.
- **MUST** pin and reverify the exact v2 digest before acceptance.
- **MUST** record verified decision owners, approvers, and applicable review evidence.
- **MUST** use single-write authority at the doctrine path after acceptance.
- **MUST** preserve prior editions through Git history or explicit lineage records.
- **MUST NOT** delete the architecture path while verified consumers remain.
- **SHOULD** retain the final tombstone indefinitely if external-consumer closure cannot be proven.
- **MAY** perform reference migration in bounded batches after the accepted decision is effective.

## 3. Consequences

### 3.1 Positive

- If accepted, KFM gains one explicit Directory Rules identity and one writable human authority path.
- Supersession becomes inspectable and digest-pinned.
- The proposed cutover preserves active links while preventing independent legacy edits.
- Later topology enforcement can cite an accepted decision instead of inferring authority from repository convention.

### 3.2 Negative

- Adoption requires a deliberate review and status-transition step.
- The architecture redirect and old fragment map create temporary compatibility work.
- Physical deletion may remain permanently blocked if external consumers cannot be proven absent.
- The machine projection and topology validator remain separate implementation work.

### 3.3 Accepted tradeoffs

The proposal favors a small persistent redirect over broken links or premature historical cleanup. It also separates authority adoption from dependent structural migration, even though that requires multiple pull requests.

### 3.4 Affected surfaces

| Surface | File or path | Current or proposed impact |
|---|---|---|
| Doctrine | `docs/doctrine/directory-rules.md` | Exact v2 bytes become adopted only after reviewed acceptance |
| ADRs | `docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md` | Present and still `proposed`; this modernization makes no status transition |
| ADR inventory | `docs/adr/INDEX.md` | Already indexes `ADR-0029` as `proposed`; acceptance must update source and index together |
| ADR summaries | `docs/adr/README.md`, `docs/registers/ADR_INDEX.md` | Already report 29 proposed numbered records; no acceptance claim |
| Doctrine landing page | `docs/doctrine/README.md` | Already surfaces v2 and ADR-0029 as proposed |
| Legacy compatibility | `docs/architecture/directory-rules.md` | Unchanged by PR #1763 and this ADR modernization; later tombstone only after acceptance |
| Machine projection | `control_plane/` | Follow-up work only |
| Data, policy, release, runtime | governed roots | Not affected |

## 4. Alternatives Considered

### 4.1 Delete the architecture path immediately

- **Summary:** Remove the only remaining competing rule file now.
- **Why rejected:** v2 is not adopted, the path has active consumers and fragments, and v2 explicitly requires a redirect before retirement.

### 4.2 Keep both full rule bodies

- **Summary:** Treat doctrine and architecture paths as equivalent copies.
- **Why rejected:** they differ in content and status, allow parallel edits, and make path authority ambiguous.

### 4.3 Treat the repository owner instruction or PR merge as implicit adoption

- **Summary:** Infer acceptance without a reviewed source decision.
- **Why rejected:** CODEOWNERS routing and repository ownership are not independent review or an accepted ADR; the v2 draft explicitly requires a recorded bootstrap decision.

### 4.4 Adopt the corrupted main-branch bytes

- **Summary:** Ratify the file exactly as first committed in `a6de05fa468bd91b7ac990b166b769a4505b7ce2`.
- **Why rejected:** those historical bytes differ from the verified artifact and contain systematic mojibake; PR #1763 restored the proposed source before adoption review.

### 4.5 Status quo

- **Why rejected:** conflicting authority remains, contributors continue to cite divergent editions, and no governed retirement can begin.

## 5. Evidence and References

- Proposed standard: [`../doctrine/directory-rules.md`](../doctrine/directory-rules.md)
- Competing legacy body: [`../architecture/directory-rules.md`](../architecture/directory-rules.md)
- ADR operating contract: [`README.md`](./README.md)
- Canonical ADR inventory: [`INDEX.md`](./INDEX.md)
- Cross-register pointer: [`../registers/ADR_INDEX.md`](../registers/ADR_INDEX.md)
- Review routing: [`.github/CODEOWNERS`](../../.github/CODEOWNERS)
- Merged byte-restoration and ratification packet: [PR #1763](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/1763)
- Ratification merge checkpoint: [`7b75e3bd590cd37321113f8336559060ae4c4358`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/commit/7b75e3bd590cd37321113f8336559060ae4c4358)
- Supplied baseline lineage: `Directory Rules.pdf`, 22 pages, SHA-256 `759de4fcb51cf0f55896089e397d9c47481d60d9fb80ac9a44d47b2f60a0a335`
- Supplied rendered v2 companion: `KFM_Directory_Governance_Standard_v2.0.0-draft.1.pdf`, 33 pages, SHA-256 `2b8db8901f893d9aabb94bb32db5cbc2e0bb0c881bf74068551e9b3b76602893`

## 6. Migration Plan

### Phase 0 — Ratification

- [x] Restore the exact proposed bytes and preserve the legacy architecture body unchanged in merged PR #1763. This completed byte restoration only.
- [ ] Verify decision owners, approvers, and applicable independent-review requirements; then obtain the explicit decision review required by the ADR operating contract.
- [ ] Reverify the v2 path, digest, blob, prior-edition targets, consumers, and concurrent ADR state at the intended acceptance head.
- [ ] Transition this ADR and the canonical index together from `proposed` to `accepted`.

### Phase 1 — Single authority surface

1. Replace the architecture v1.3.1 body with a read-only tombstone in a separate PR.
2. Record the old-to-new identity and path mapping.
3. Establish single-write behavior at the doctrine path.
4. Preserve rollback through the prior blob and reviewed revert path.

### Phase 2 — Reference closure

1. Update active canonical-path and fragment references in bounded batches.
2. Preserve immutable historical receipts and commit-pinned evidence.
3. Validate repository links, anchors, source claims, and rule-section mappings.
4. Prove zero current writers and consumers before physical deletion.

### Phase 3 — Executable projection

Implement the root and alias registers, schema, fixtures, validator, tests, Make target, and CI ratchet in separately reviewed work. Machine files project accepted doctrine; they do not accept it.

## 7. Rollback Plan

### Before acceptance

- Keep this record and the canonical index at `proposed`; no legacy-path migration exists to undo.
- If governance declines the proposal, use a reviewed `proposed` → `rejected` transition in the source ADR and canonical index rather than inferring rejection from a closed PR.
- Revert an unmerged acceptance change if necessary; PR #1763 itself is a merged lineage and byte-restoration checkpoint, not an accepted decision.
- Keep v2 `PROPOSED_FOR_ADOPTION`.

### After acceptance but before tombstone migration

- Record a successor ADR that supersedes this decision; do not rewrite or delete the accepted record.
- Restore the prior doctrine edition only through the successor's explicit decision and digest.

### After tombstone migration

- Revert the migration commit only if doing so cannot recreate two writable authorities.
- Otherwise apply a forward fix to the doctrine file or redirect and record why rollback was unsafe.
- Re-run link, identity, and zero-writer checks after any rollback or forward fix.

## 8. Open Questions

- Who holds verified documentation-governance and architecture stewardship assignments?
- Which verified identity can provide independent acceptance review?
- What expiry or permanent-retention rule should govern the architecture tombstone?
- Which machine register owns document-ID aliases until the proposed alias register exists?
- Which legacy section anchors require explicit compatibility mapping rather than direct replacement?

## 9. Acceptance Gates

- [ ] `docs/doctrine/directory-rules.md` matches SHA-256 `44f7e94344cb42b630008eb0bc03a13fcb97dbdfba6f3e56579693a272571e6e`.
- [ ] Its Git blob is `fd49a0b83e55cef52c1124281f093e263526898d`.
- [ ] All exact supersession targets are reverified.
- [ ] No concurrent `ADR-0029` identity claim or competing Directory Rules adoption proposal exists, excluding the one reviewed acceptance change itself.
- [ ] Verified stewardship assignments, decision owners, approvers, and applicable independent-review evidence are recorded.
- [ ] Every verified named owner required by the ADR operating contract explicitly approves.
- [ ] The ADR source and index transition together to `accepted`.
- [ ] The architecture body remains unchanged until the acceptance decision is effective.
- [ ] Migration and rollback tickets or manifests identify the post-adoption work.

## 10. Change History

| Date | Status | Change | PR |
|---|---|---|---|
| 2026-07-26 | proposed | Initial ratification packet | [#1763](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/1763) |

[Back to top](#top)

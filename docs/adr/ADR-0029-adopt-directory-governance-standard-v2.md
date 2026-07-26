<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://adr/ADR-0029
title: Adopt Directory Governance Standard v2
type: adr
version: v1
status: accepted
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
  - "Accepted by explicit project-owner ratification on 2026-07-26; merge of the ratification pull request makes this decision effective."
  - "@bartytime4life is the sole verified named owner and review route. The explicit owner instruction is the bootstrap acceptance decision; no independent stewardship identity was available, so this record carries a transparent single-owner bootstrap exception and a later independent-review trigger."
  - "PR #1763 restored the verified v2 bytes without adoption. Commit 4977bca73cb8bc6232f5a48c7768baf6f0a290c6 later deleted the held legacy path before acceptance; this ratification restores prior blob 18653c00ba193a4afaa3e07a0924452807fb98ef and does not authorize deletion."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0029: Adopt Directory Governance Standard v2

Accepted on 2026-07-26 by explicit project-owner ratification, this decision adopts the exact verified UTF-8 bytes of Directory Rules `2.0.0-draft.1` at `docs/doctrine/directory-rules.md`, makes that path the single writable human-readable Directory Rules authority, and starts a controlled compatibility migration for the restored legacy architecture copy. It does not ratify the premature deletion or authorize tombstoning, reference migration, or physical deletion.

| Field | Value |
|---|---|
| **ID** | `ADR-0029` |
| **Status** | `accepted` |
| **Date** | 2026-07-26 |
| **Repository review route** | `@bartytime4life` via CODEOWNERS; sole verified named owner and review route |
| **Decision authority** | `@bartytime4life` — explicit project-owner ratification recorded in issue #1531 and the ratification pull request |
| **Acceptance evidence** | Explicit owner instruction; exact digest/blob re-verification; restoration of the prematurely deleted legacy body; synchronized source/index transition; transparent single-owner bootstrap exception |
| **Consulted** | KFM doctrine, the two Directory Rules bodies, supplied source artifacts, and pinned repository evidence |
| **Informed** | All repository contributors and consumers of Directory Rules paths or fragments |
| **Supersedes** | No prior ADR |
| **Superseded by** | — |
| **Directory Rules trigger** | v2 §2.2 `DIR-AUTH-004`, §17, §18, and §21 bootstrap adoption |
| **Primary responsibility root** | `docs/` |
| **Migration required** | yes |
| **Rollback required** | yes |
| **Evidence checkpoint** | Ratification base `67f1d7eac9baabd69da997ba569de54c6b7c1d11`; v2 byte-restoration merge `7b75e3bd590cd37321113f8336559060ae4c4358`; premature deletion `4977bca73cb8bc6232f5a48c7768baf6f0a290c6` |
| **Truth posture** | `CONFIRMED` evidence; `ACCEPTED` decision; independent stewardship remains `NEEDS VERIFICATION` as a follow-up trigger |

> [!IMPORTANT]
> Acceptance becomes effective only when this source ADR and the canonical index merge together with status `accepted`. This decision adopts only the pinned v2 bytes. It does not ratify commit `4977bca…`, authorize physical deletion, or collapse the separate tombstone and reference-migration phases.

**Quick navigation:** [Context](#1-context) · [Decision](#2-decision) · [Consequences](#3-consequences) · [Alternatives](#4-alternatives-considered) · [Evidence](#5-evidence-and-references) · [Migration](#6-migration-plan) · [Rollback](#7-rollback-plan) · [Open questions](#8-open-questions) · [Acceptance gates](#9-acceptance-gates) · [History](#10-change-history)

## 1. Context

KFM has one accepted successor and, after the corrective restoration in this ratification packet, one read-only legacy compatibility body:

| Surface | Verified state | Effect |
|---|---|---|
| `docs/doctrine/directory-rules.md` | Directory Rules `2.0.0-draft.1`; blob `fd49a0b83e55cef52c1124281f093e263526898d`; artifact label `PROPOSED_FOR_ADOPTION` | Exact pinned bytes are adopted by this accepted ADR; the internal artifact label remains part of the pinned bytes |
| `docs/architecture/directory-rules.md` | v1.3.1 `review`; restored exact blob `18653c00ba193a4afaa3e07a0924452807fb98ef` | Read-only compatibility dependency pending a separate tombstone migration |
| `docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md` | This record; source status `accepted` in the ratification change | Adoption and enumerated document-edition supersession become effective on merge |
| Numbered ADR corpus | `ADR-0001` through `ADR-0028` remain effectively `proposed`; `ADR-0029` is `accepted` | ADR-0029 is the first accepted numbered bootstrap authority |

The successor itself requires an explicit adoption decision before dependent structural work. It also requires the architecture file to become a short read-only redirect before eventual retirement. The merged ratification packet recorded 214 resolving Markdown links to the architecture path, including 83 fragment links across 30 legacy anchors. Those counts are evidence from PR #1763, not proof of external-consumer closure; immediate path deletion would create broad link and semantic breakage.

The first copy of v2 committed directly to `main` in `a6de05fa468bd91b7ac990b166b769a4505b7ce2` was not byte-faithful to the finished artifact. PR #1763 restored the exact intended UTF-8 bytes and merged as `7b75e3bd590cd37321113f8336559060ae4c4358`; that merge completed byte restoration only. Commit `4977bca73cb8bc6232f5a48c7768baf6f0a290c6` then deleted the held architecture path before acceptance. This ratification change restores the exact prior blob and synchronizes the first effective acceptance transition.

### Current ratification checkpoint

| Step | State at the evidence checkpoint | Governing effect |
|---|---|---|
| Exact v2 byte restoration | **CONFIRMED complete and reverified** | Provides the exact adopted bytes |
| ADR-0029 decision | **ACCEPTED on merge** | Establishes placement and document-edition supersession authority only |
| Legacy full body | **RESTORED / read-only on merge** | Repairs the premature deletion and preserves compatibility |
| Legacy-path tombstone | **HELD** | Requires a separate post-adoption migration PR |
| Physical legacy-path deletion | **HOLD / not authorized** | Requires zero-writer, zero-consumer, link-closure, and retirement-receipt evidence |

### 1.1 Decision drivers

- **Single authority** — two independently editable rules bodies create contradictory placement authority.
- **Byte integrity** — adoption must pin the restored verified source, not the historically corrupted commit.
- **Governed supersession** — prior editions need exact identity, digest, lineage, and forward links.
- **Compatibility** — active path and fragment consumers require a bounded redirect and reference migration.
- **Reversibility** — the cutover must not recreate two writable authorities or erase decision history.
- **Review integrity** — explicit project-owner ratification is recorded; the absence of an independent stewardship identity is disclosed as a bootstrap exception, not misrepresented as independent approval.

### 1.2 Evidence boundary

- **CONFIRMED:** at ratification base `67f1d7eac9baabd69da997ba569de54c6b7c1d11`, the exact v2 digest/blob, ADR-0029 and index still `proposed`, the premature legacy-path deletion at `4977bca…`, the prior legacy blob at the pre-deletion commit, no concurrent ADR-0029 claim, and PR #1763's repository link inventory.
- **CONFIRMED in this change:** restoration of legacy blob `18653c00ba193a4afaa3e07a0924452807fb98ef` and synchronized source/index transition to `accepted`.
- **ACCEPTED:** adoption of v2, the canonical identity and aliases, document-edition supersession, single-write authority, and the controlled migration sequence below.
- **UNKNOWN:** external consumers that are not visible through repository search.
- **NEEDS VERIFICATION:** future independent stewardship, final reference inventory for tombstoning, machine-register parity, and zero-consumer proof before physical deletion.

### 1.3 Out of scope

This ADR does not:

- accept itself;
- implement the topology validator, root registry, alias register, or CI ratchet;
- move lifecycle data, trust objects, contracts, schemas, policy, code, release records, or published material;
- approve any later root, lane, or object-family migration;
- treat the proposed v2 convergence appendix as proof that its recommendations are implemented;
- authorize immediate deletion of `docs/architecture/directory-rules.md`.

## 2. Decision

> **Decision:** Adopt the exact verified UTF-8 Directory Rules v2 bytes identified below at `docs/doctrine/directory-rules.md`; make that path the sole writable human Directory Rules authority; supersede the enumerated prior editions; and migrate the restored legacy architecture path through a read-only tombstone before any physical deletion.

### 2.1 Adopted artifact identity

The accepted artifact is:

| Field | Accepted value |
|---|---|
| Canonical path | `docs/doctrine/directory-rules.md` |
| Version | `2.0.0-draft.1` |
| Document ID | `kfm://doctrine/directory-governance/v2` |
| SHA-256 | `44f7e94344cb42b630008eb0bc03a13fcb97dbdfba6f3e56579693a272571e6e` |
| Git blob | `fd49a0b83e55cef52c1124281f093e263526898d` |
| Byte count | 80,881 |
| Line count | 1,510 plus final newline |

The digest and blob were reverified immediately before this `accepted` status transition. A content change requires a successor or explicitly renewed review with a new digest; this ADR does not silently accept different bytes.

The supplied rendered companion `KFM_Directory_Governance_Standard_v2.0.0-draft.1.pdf` is 33 pages with SHA-256 `2b8db8901f893d9aabb94bb32db5cbc2e0bb0c881bf74068551e9b3b76602893`. It was inspected as a presentation and lineage artifact. Its PDF digest is not the adoption digest and does not replace the exact UTF-8 Markdown identity above.

<a id="exact-supersession-targets"></a>

### 2.2 Supersession and lineage targets

Acceptance establishes the following exact doctrinal lineage without implying that every predecessor previously had repository authority:

| Prior artifact | Exact identity | Relation after acceptance |
|---|---|---|
| Supplied unversioned `Directory Rules.pdf` | 22 pages; SHA-256 `759de4fcb51cf0f55896089e397d9c47481d60d9fb80ac9a44d47b2f60a0a335` | Source-lineage predecessor only; no repository deletion target and no current repository authority |
| Prior doctrine v1.4 | Git blob `2affb080e6f0043867c64c7f06c1ca52030fbd55` | Superseded repository doctrine edition; retained in Git history |
| Architecture v1.3.1 | Git blob `18653c00ba193a4afaa3e07a0924452807fb98ef` | Superseded content edition; body replaced only in a post-adoption migration PR while the path remains a read-only compatibility surface |

The meta-block fields `supersedes` and `superseded_by` describe ADR-to-ADR relationships, so they remain empty. The table above records document-edition lineage and must not be interpreted as an ADR identity relationship or as deletion authority.

### 2.3 Stable identity and aliases

The v2 document ID `kfm://doctrine/directory-governance/v2` becomes canonical through this acceptance. The prior IDs:

- `kfm://doc/directory-rules`
- `kfm://doc/doctrine/directory-rules`

are explicit superseded aliases to the canonical v2 identity. A later machine-projection PR must record those aliases without creating independent write authority.

### 2.4 Compatibility and deletion rule

The deletion state remains **HOLD**. This accepted ADR neither performs nor authorizes deletion. From acceptance:

1. all new Directory Rules edits go only to `docs/doctrine/directory-rules.md`;
2. `docs/architecture/directory-rules.md` is replaced in a separate migration PR with a short read-only tombstone;
3. the tombstone records the prior blob, canonical target, accepted ADR, effective date, owner, expiry or exit condition, and no-independent-edits rule;
4. active references and legacy fragments are migrated or intentionally mapped;
5. the path is physically deleted only after zero-writer, zero-consumer, link-closure, and retirement-receipt validation.

Historical receipts and commit-pinned evidence are not rewritten merely to remove a legacy string.

### 2.5 Conformance language

- **MUST** preserve this accepted ADR as append-only decision history; a material reversal requires a successor ADR.
- **MUST NOT** treat PR #1763, its merge commit, or byte equality as adoption evidence.
- **MUST** pin and reverify the exact v2 digest before acceptance.
- **MUST** preserve the explicit owner-ratification evidence, the single-owner bootstrap exception, and any later independent review evidence.
- **MUST** use single-write authority at the doctrine path after acceptance.
- **MUST** preserve prior editions through Git history or explicit lineage records.
- **MUST NOT** delete the architecture path while verified consumers remain.
- **SHOULD** retain the final tombstone indefinitely if external-consumer closure cannot be proven.
- **MAY** perform reference migration in bounded batches after the accepted decision is effective.

## 3. Consequences

### 3.1 Positive

- KFM gains one explicit Directory Rules identity and one writable human authority path.
- Supersession becomes inspectable and digest-pinned.
- The accepted cutover preserves active links while preventing independent legacy edits.
- Later topology enforcement can cite this accepted decision instead of inferring authority from repository convention.

### 3.2 Negative

- Acceptance uses a transparent single-owner bootstrap exception because no independent stewardship identity is currently established.
- The architecture redirect and old fragment map create temporary compatibility work.
- Physical deletion may remain permanently blocked if external consumers cannot be proven absent.
- The machine projection and topology validator remain separate implementation work.

### 3.3 Accepted tradeoffs

The proposal favors a small persistent redirect over broken links or premature historical cleanup. It also separates authority adoption from dependent structural migration, even though that requires multiple pull requests.

### 3.4 Affected surfaces

| Surface | File or path | Current or proposed impact |
|---|---|---|
| Doctrine | `docs/doctrine/directory-rules.md` | Exact v2 bytes are adopted by this accepted ADR without mutating the pinned artifact |
| ADRs | `docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md` | Transitions to `accepted` in the ratification change |
| ADR inventory | `docs/adr/INDEX.md` | Transitions ADR-0029 to `accepted` with matching source metadata |
| ADR summaries | `docs/adr/README.md`, `docs/registers/ADR_INDEX.md` | Report 1 accepted and 28 proposed numbered records |
| Doctrine landing page | `docs/doctrine/README.md` | Surfaces v2 as adopted through accepted ADR-0029 |
| Legacy compatibility | `docs/architecture/directory-rules.md` | Restores exact prior blob after premature deletion; separate tombstone migration remains required |
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
- **Why rejected:** implicit adoption remains invalid. This acceptance rests on an explicit project-owner ratification, recorded bootstrap exception, exact-byte re-verification, legacy restoration, and synchronized source/index transition.

### 4.4 Adopt the corrupted main-branch bytes

- **Summary:** Ratify the file exactly as first committed in `a6de05fa468bd91b7ac990b166b769a4505b7ce2`.
- **Why rejected:** those historical bytes differ from the verified artifact and contain systematic mojibake; PR #1763 restored the proposed source before adoption review.

### 4.5 Status quo

- **Why rejected:** conflicting authority remains, contributors continue to cite divergent editions, and no governed retirement can begin.

## 5. Evidence and References

- Adopted standard bytes: [`../doctrine/directory-rules.md`](../doctrine/directory-rules.md)
- Restored legacy compatibility body: [`../architecture/directory-rules.md`](../architecture/directory-rules.md)
- ADR operating contract: [`README.md`](./README.md)
- Canonical ADR inventory: [`INDEX.md`](./INDEX.md)
- Cross-register pointer: [`../registers/ADR_INDEX.md`](../registers/ADR_INDEX.md)
- Review routing: [`.github/CODEOWNERS`](../../.github/CODEOWNERS)
- Merged byte-restoration and proposal packet: [PR #1763](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/1763)
- Byte-restoration merge checkpoint: [`7b75e3bd590cd37321113f8336559060ae4c4358`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/commit/7b75e3bd590cd37321113f8336559060ae4c4358)
- Premature deletion being corrected: [`4977bca73cb8bc6232f5a48c7768baf6f0a290c6`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/commit/4977bca73cb8bc6232f5a48c7768baf6f0a290c6)
- Durable authorization cursor: [issue #1531](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/1531)
- Acceptance change: [PR #RATIFICATION_PR](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/RATIFICATION_PR)
- Supplied baseline lineage: `Directory Rules.pdf`, 22 pages, SHA-256 `759de4fcb51cf0f55896089e397d9c47481d60d9fb80ac9a44d47b2f60a0a335`
- Supplied rendered v2 companion: `KFM_Directory_Governance_Standard_v2.0.0-draft.1.pdf`, 33 pages, SHA-256 `2b8db8901f893d9aabb94bb32db5cbc2e0bb0c881bf74068551e9b3b76602893`

## 6. Migration Plan

### Phase 0 — Ratification

- [x] Restore the exact proposed v2 bytes in merged PR #1763.
- [x] Record the sole verified named owner's explicit ratification and the transparent single-owner bootstrap exception; retain later independent review as a follow-up trigger.
- [x] Reverify the v2 path, digest, blob, repository prior-edition targets, current deletion state, and concurrent ADR state at the acceptance base.
- [x] Restore the prematurely deleted architecture body to exact prior blob `18653c00ba193a4afaa3e07a0924452807fb98ef`.
- [x] Transition this ADR and the canonical index together from `proposed` to `accepted`.

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

### Before the ratification pull request merges

- Close the draft ratification pull request; `main` remains `proposed` and the accepted decision is not effective.
- Preserve PR #1763 as merged lineage and byte-restoration evidence.
- Restore the legacy path only through a reviewed corrective change if the ratification branch is abandoned; do not treat the premature deletion as valid.
- Keep the pinned v2 bytes unchanged.

### After acceptance but before tombstone migration

- Record a successor ADR that supersedes this decision; do not rewrite or delete the accepted record.
- Restore the prior doctrine edition only through the successor's explicit decision and digest.

### After tombstone migration

- Revert the migration commit only if doing so cannot recreate two writable authorities.
- Otherwise apply a forward fix to the doctrine file or redirect and record why rollback was unsafe.
- Re-run link, identity, and zero-writer checks after any rollback or forward fix.

## 8. Open Questions

- Which verified independent identity should perform the post-bootstrap review and assume future documentation-governance stewardship?
- What evidence should close the transparent single-owner bootstrap exception without rewriting this accepted decision?
- What expiry or permanent-retention rule should govern the architecture tombstone?
- Which machine register owns document-ID aliases until the proposed alias register exists?
- Which legacy section anchors require explicit compatibility mapping rather than direct replacement?

## 9. Acceptance Gates

- [x] `docs/doctrine/directory-rules.md` matches SHA-256 `44f7e94344cb42b630008eb0bc03a13fcb97dbdfba6f3e56579693a272571e6e`.
- [x] Its Git blob is `fd49a0b83e55cef52c1124281f093e263526898d`.
- [x] Repository supersession targets are reverified; the unversioned source-lineage PDF digest is retained as recorded lineage, not as the adopted bytes or a repository deletion target.
- [x] No concurrent `ADR-0029` identity claim or competing Directory Rules adoption proposal exists, excluding this acceptance change.
- [x] The sole verified named owner explicitly ratified the decision; the unavailable independent stewardship role is recorded as a transparent bootstrap exception and follow-up trigger.
- [x] The ADR source and canonical index transition together to `accepted`.
- [x] The prematurely deleted architecture body is restored to exact prior blob `18653c00ba193a4afaa3e07a0924452807fb98ef` before or with the effective acceptance transition.
- [x] This ADR's phase plan and issue #1531 identify the separate tombstone, reference-closure, machine-projection, and rollback work.
- [x] Physical deletion remains explicitly unauthorized.

## 10. Change History

| Date | Status | Change | PR |
|---|---|---|---|
| 2026-07-26 | proposed | Initial byte-restoration and proposal packet | [#1763](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/1763) |
| 2026-07-26 | proposed | Clarified the held ratification and deletion boundaries | [#1765](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/1765) |
| 2026-07-26 | accepted | Explicit project-owner ratification; synchronized index transition; premature legacy deletion repaired | [#RATIFICATION_PR](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/RATIFICATION_PR) |

[Back to top](#top)

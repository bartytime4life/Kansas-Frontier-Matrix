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
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0029: Adopt Directory Governance Standard v2

If accepted after explicit governance and independent review, this decision adopts the exact verified UTF-8 bytes of Directory Rules `2.0.0-draft.1` at `docs/doctrine/directory-rules.md`, makes that path the single human-readable Directory Rules authority, and starts a controlled compatibility migration for the legacy architecture copy. While this ADR remains `proposed`, it has no adoption or supersession effect.

| Field | Value |
|---|---|
| **ID** | `ADR-0029` |
| **Status** | `proposed` |
| **Date** | 2026-07-26 |
| **Decider route** | `@bartytime4life` — verified CODEOWNERS route; stewardship authority remains `NEEDS VERIFICATION` |
| **Required acceptance review** | Documentation governance, architecture, affected responsibility-root owner, and a verified independent reviewer |
| **Consulted** | KFM doctrine, repository evidence, Directory Rules v2 reviewer classes |
| **Informed** | All repository contributors and consumers of Directory Rules paths or fragments |
| **Supersedes** | No prior ADR |
| **Superseded by** | — |
| **Directory Rules trigger** | v2 §2.2 `DIR-AUTH-004`, §17, §18, and §21 bootstrap adoption |
| **Primary responsibility root** | `docs/` |
| **Migration required** | yes |
| **Rollback required** | yes |
| **Truth posture** | `CONFIRMED` evidence; `PROPOSED` decision; acceptance review `NEEDS VERIFICATION` |

> [!IMPORTANT]
> Adding or merging this record with status `proposed` does not accept it. Adoption becomes effective only when the source ADR and canonical index both carry a reviewed `accepted` state, the exact proposed content digest is reverified, and the required approvals are recorded.

## 1. Context

KFM currently has one proposed successor and one competing legacy Directory Rules body:

| Surface | Verified state | Effect |
|---|---|---|
| `docs/doctrine/directory-rules.md` | Directory Rules `2.0.0-draft.1`; corrected branch blob `fd49a0b83e55cef52c1124281f093e263526898d`; status `PROPOSED_FOR_ADOPTION` | Proposed successor only |
| `docs/architecture/directory-rules.md` | v1.3.1 `review`; blob `18653c00ba193a4afaa3e07a0924452807fb98ef` | Competing rule body and active compatibility dependency |
| Numbered ADR corpus before this proposal | `ADR-0001` through `ADR-0028`, all effectively `proposed` | No accepted bootstrap authority |

The successor itself requires an explicit adoption decision before dependent structural work. It also requires the architecture file to become a short read-only redirect before eventual retirement. A current repository audit found 214 resolving Markdown links to the architecture path, including 83 fragment links across 30 legacy anchors, so immediate path deletion would create broad link and semantic breakage.

The first copy of v2 committed directly to `main` in `a6de05fa468bd91b7ac990b166b769a4505b7ce2` was not byte-faithful to the finished artifact. Draft PR #1763 restores the exact intended UTF-8 bytes before this decision can be reviewed.

### 1.1 Decision drivers

- **Single authority** — two independently editable rules bodies create contradictory placement authority.
- **Byte integrity** — adoption must pin the verified source, not the corrupted main-branch copy.
- **Governed supersession** — prior editions need exact identity, digest, lineage, and forward links.
- **Compatibility** — active path and fragment consumers require a bounded redirect and reference migration.
- **Reversibility** — the cutover must not recreate two writable authorities or erase decision history.
- **Review integrity** — repository ownership and CODEOWNERS routing do not substitute for independent approval.

### 1.2 Evidence boundary

- **CONFIRMED:** the two current repository paths, their versions and blobs, the corrected v2 digest, the absence of an accepted numbered ADR, and the current inbound-link count.
- **PROPOSED:** adoption of v2, the canonical identity and aliases, the tombstone window, and the migration sequence below.
- **UNKNOWN:** external consumers that are not visible through repository search.
- **NEEDS VERIFICATION:** verified governance owners, an independent reviewer, final reference inventory at acceptance time, machine-register parity, and zero-consumer proof before physical deletion.

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

### 2.2 Exact supersession targets

Acceptance would supersede these Directory Rules editions as current authority while preserving their lineage:

| Prior artifact | Exact identity | Disposition after acceptance |
|---|---|---|
| Supplied unversioned `Directory Rules.pdf` | SHA-256 `759de4fcb51cf0f55896089e397d9c47481d60d9fb80ac9a44d47b2f60a0a335` | Source lineage only; no current repository authority |
| Prior doctrine v1.4 | Git blob `2affb080e6f0043867c64c7f06c1ca52030fbd55` | Retained in Git history as superseded doctrine |
| Architecture v1.3.1 | Git blob `18653c00ba193a4afaa3e07a0924452807fb98ef` | Rule body removed only in a post-adoption migration PR; path becomes a temporary read-only redirect |

### 2.3 Stable identity and aliases

The v2 document ID `kfm://doctrine/directory-governance/v2` becomes canonical only after acceptance. The prior IDs:

- `kfm://doc/directory-rules`
- `kfm://doc/doctrine/directory-rules`

become explicit superseded aliases to the canonical v2 identity. A later machine-projection PR must record those aliases without creating independent write authority.

### 2.4 Compatibility and deletion rule

After acceptance:

1. all new Directory Rules edits go only to `docs/doctrine/directory-rules.md`;
2. `docs/architecture/directory-rules.md` is replaced in a separate migration PR with a short read-only tombstone;
3. the tombstone records the prior blob, canonical target, accepted ADR, effective date, owner, expiry or exit condition, and no-independent-edits rule;
4. active references and legacy fragments are migrated or intentionally mapped;
5. the path is physically deleted only after zero-writer, zero-consumer, link-closure, and retirement-receipt validation.

Historical receipts and commit-pinned evidence are not rewritten merely to remove a legacy string.

### 2.5 Conformance language

- **MUST** keep this ADR `proposed` until explicit required review is recorded.
- **MUST** pin and reverify the exact v2 digest before acceptance.
- **MUST** use single-write authority at the doctrine path after acceptance.
- **MUST** preserve prior editions through Git history or explicit lineage records.
- **MUST NOT** delete the architecture path while verified consumers remain.
- **SHOULD** retain the final tombstone indefinitely if external-consumer closure cannot be proven.
- **MAY** perform reference migration in bounded batches after the accepted decision is effective.

## 3. Consequences

### 3.1 Positive

- KFM gains one explicit Directory Rules identity and one writable human authority path.
- Supersession becomes inspectable and digest-pinned.
- The cutover preserves active links while preventing independent legacy edits.
- Later topology enforcement can cite an accepted decision instead of inferring authority from repository convention.

### 3.2 Negative

- Adoption requires a deliberate review and status-transition step.
- The architecture redirect and old fragment map create temporary compatibility work.
- Physical deletion may remain permanently blocked if external consumers cannot be proven absent.
- The machine projection and topology validator remain separate implementation work.

### 3.3 Accepted tradeoffs

The proposal favors a small persistent redirect over broken links or premature historical cleanup. It also separates authority adoption from dependent structural migration, even though that requires multiple pull requests.

### 3.4 Affected surfaces

| Surface | File or path | Proposed impact |
|---|---|---|
| Doctrine | `docs/doctrine/directory-rules.md` | Exact v2 bytes become adopted only after reviewed acceptance |
| ADRs | `docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md` | New decision record |
| ADR inventory | `docs/adr/INDEX.md` | Adds `ADR-0029` as `proposed` |
| ADR summaries | `docs/adr/README.md`, `docs/registers/ADR_INDEX.md` | Count and range update; no acceptance claim |
| Doctrine landing page | `docs/doctrine/README.md` | Corrects v1.4 label and surfaces v2 as proposed |
| Legacy compatibility | `docs/architecture/directory-rules.md` | No change in the ratification PR; later tombstone |
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

- **Summary:** Ratify the file exactly as first committed.
- **Why rejected:** those bytes differ from the verified artifact and contain systematic mojibake.

### 4.5 Status quo

- **Why rejected:** conflicting authority remains, contributors continue to cite divergent editions, and no governed retirement can begin.

## 5. Evidence and References

- Proposed standard: [`../doctrine/directory-rules.md`](../doctrine/directory-rules.md)
- Competing legacy body: [`../architecture/directory-rules.md`](../architecture/directory-rules.md)
- ADR operating contract: [`README.md`](./README.md)
- Canonical ADR inventory: [`INDEX.md`](./INDEX.md)
- Cross-register pointer: [`../registers/ADR_INDEX.md`](../registers/ADR_INDEX.md)
- Review routing: [`.github/CODEOWNERS`](../../.github/CODEOWNERS)
- Byte-restoration review: [PR #1763](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/1763)

## 6. Migration Plan

### Phase 0 — Ratification

1. Merge the exact-byte repair only after its digest and diff are reviewed.
2. Review this ADR with the required reviewer classes.
3. Reverify the v2 path, digest, blob, prior-edition targets, consumers, and concurrent ADR state.
4. Transition this ADR and the canonical index together from `proposed` to `accepted`.

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

- Close or revert the unmerged proposal.
- Restore no legacy path because the ratification PR does not change it.
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
- [ ] No concurrent `ADR-0029` or Directory Rules adoption proposal exists.
- [ ] Verified owners and an independent reviewer are recorded.
- [ ] Required reviewers explicitly approve.
- [ ] The ADR source and index transition together to `accepted`.
- [ ] The architecture body remains unchanged until the acceptance decision is effective.
- [ ] Migration and rollback tickets or manifests identify the post-adoption work.

## 10. Change History

| Date | Status | Change | PR |
|---|---|---|---|
| 2026-07-26 | proposed | Initial ratification packet | [#1763](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/1763) |

[Back to top](#top)

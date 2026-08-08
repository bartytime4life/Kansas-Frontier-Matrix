<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://adr/ADR-0029
title: Adopt Directory Governance Standard v2
type: adr
version: v1.1
status: accepted
owners: ["@bartytime4life"]
created: 2026-07-26
updated: 2026-08-08
policy_label: public
owning_root: "docs/"
responsibility: "Record the accepted Directory Rules v2 decision and bounded post-adoption implementation status."
truth_posture: "CONFIRMED evidence / ACCEPTED decision / NEEDS VERIFICATION follow-up"
related:
  - "docs/doctrine/directory-rules.md"
  - "docs/architecture/directory-rules.md"
  - "docs/adr/README.md"
  - "docs/adr/INDEX.md"
  - "docs/registers/ADR_INDEX.md"
  - "docs/registers/DRIFT_REGISTER.md"
  - "docs/registers/VERIFICATION_BACKLOG.md"
  - "control_plane/root_registry.yaml"
  - "control_plane/path_alias_register.yaml"
  - "control_plane/domain_lane_register.yaml"
  - "control_plane/cross_domain_seam_register.yaml"
  - "contracts/governance/path_decision_record.md"
tags: [adr, kfm, directory-rules, doctrine, governance, placement, migration, implementation-status]
supersedes: []
superseded_by: []
notes:
  - "Accepted by explicit project-owner ratification on 2026-07-26; merge of the ratification pull request makes this decision effective."
  - "@bartytime4life is the sole verified named owner and review route. The explicit owner instruction is the bootstrap acceptance decision; no independent stewardship identity was available, so this record carries a transparent single-owner bootstrap exception and a later independent-review trigger."
  - "PR #1763 restored the verified v2 bytes without adoption. Commit 4977bca73cb8bc6232f5a48c7768baf6f0a290c6 later deleted the held legacy path before acceptance; this ratification restores prior blob 18653c00ba193a4afaa3e07a0924452807fb98ef and does not authorize deletion."
  - "v1.1 is an append-only post-adoption implementation-status update. It does not alter the accepted decision, adopted bytes, digest, authority boundary, migration order, or deletion hold."
  - "Post-adoption governance projections are now present through PRs #2136, #2138, #2149, #2164, and #2187. Repository presence is CONFIRMED; current-main enforcement, consumer closure, tombstoning, and independent stewardship remain bounded below."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0029: Adopt Directory Governance Standard v2

Accepted on 2026-07-26 by explicit project-owner ratification, this decision adopts the exact verified UTF-8 bytes of Directory Rules `2.0.0-draft.1` at `docs/doctrine/directory-rules.md`, makes that path the single writable human-readable Directory Rules authority, and starts a controlled compatibility migration for the restored legacy architecture copy. It does not ratify the premature deletion or authorize tombstoning, reference migration, or physical deletion.

> [!NOTE]
> **v1.1 post-adoption record.** This edition adds a non-normative implementation-status record for governance projections that landed after acceptance. The accepted decision, pinned Directory Rules bytes and digest, authority boundary, migration sequence, physical-deletion hold, and transparent single-owner bootstrap exception are unchanged.

| Field | Value |
|---|---|
| **ID** | `ADR-0029` |
| **Status** | `accepted` |
| **Date** | 2026-07-26 |
| **Record edition** | `v1.1` — append-only post-adoption implementation-status update; decision unchanged |
| **Last status review** | 2026-08-08 against `main@b1e53f67b87973d987aab87359fba906f0f6388f` |
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
| **Post-adoption implementation** | `PARTIAL`: machine projections and validators are present; tombstone migration, consumer closure, current-main enforcement closure, and physical deletion remain incomplete or held |
| **Truth posture** | `CONFIRMED` evidence; `ACCEPTED` decision; independent stewardship remains `NEEDS VERIFICATION` as a follow-up trigger |

> [!IMPORTANT]
> Acceptance becomes effective only when this source ADR and the canonical index merge together with status `accepted`. This decision adopts only the pinned v2 bytes. It does not ratify commit `4977bca…`, authorize physical deletion, or collapse the separate tombstone and reference-migration phases.

**Quick navigation:** [Context](#1-context) · [Decision](#2-decision) · [Consequences](#3-consequences) · [Alternatives](#4-alternatives-considered) · [Evidence](#5-evidence-and-references) · [Migration](#6-migration-plan) · [Implementation record](#6a-post-adoption-implementation-record) · [Rollback](#7-rollback-plan) · [Open questions](#8-open-questions) · [Acceptance gates](#9-acceptance-gates) · [History](#10-change-history)

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

Unless a later section says otherwise, the context, consequences, and acceptance gates below describe the ratification checkpoint. Current post-adoption implementation is recorded separately in [§6A](#6a-post-adoption-implementation-record), without rewriting the accepted decision.

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

This list describes the scope of the 2026-07-26 ratification change. Later merged pull requests implemented several projection-only follow-ups; those follow-ups do not expand what the adoption decision itself authorized. See [§6A](#6a-post-adoption-implementation-record).

### 1.4 v1.1 post-adoption evidence boundary

- **CONFIRMED at `main@b1e53f67b87973d987aab87359fba906f0f6388f`:** repository presence of the Root Registry, `PathDecisionRecord` contract, Path Alias Register, Domain Lane Register, Cross-Domain Seam Register, their associated schemas/validators/tests/workflows from the cited merged PRs, the unchanged canonical Directory Rules digest, and the still-full legacy architecture body.
- **CONFIRMED:** each machine projection explicitly declares that it does not create or amend authority, execute migration, activate a root or domain, authorize a join, or publish.
- **NEEDS VERIFICATION:** current-main aggregate enforcement, required-check coupling, a consolidated Make target or equivalent ratchet, external consumers, and complete reference/fragment closure.
- **HOLD:** architecture-path tombstoning and physical deletion remain outside this update and require their own reviewed migration evidence.

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

> [!NOTE]
> This table records the direct impact of the ratification change. It is not a current implementation inventory. The post-adoption machine-projection status is maintained in [§6A](#6a-post-adoption-implementation-record).

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

### 5.1 Ratification and lineage evidence

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
- Acceptance change: [PR #1774](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/1774)
- Supplied baseline lineage: `Directory Rules.pdf`, 22 pages, SHA-256 `759de4fcb51cf0f55896089e397d9c47481d60d9fb80ac9a44d47b2f60a0a335`
- Supplied rendered v2 companion: `KFM_Directory_Governance_Standard_v2.0.0-draft.1.pdf`, 33 pages, SHA-256 `2b8db8901f893d9aabb94bb32db5cbc2e0bb0c881bf74068551e9b3b76602893`

### 5.2 Post-adoption repository evidence

- Root Registry projection: [`../../control_plane/root_registry.yaml`](../../control_plane/root_registry.yaml); [PR #2136](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/2136); merge `0eac9e38587cc991f0e803f11002d519cbed0b6a`.
- Path Decision Record: [`../../contracts/governance/path_decision_record.md`](../../contracts/governance/path_decision_record.md); [PR #2138](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/2138); merge `b7e8548a469f6849af97223a29c3a5e8bf646c0c`.
- Path Alias Register projection: [`../../control_plane/path_alias_register.yaml`](../../control_plane/path_alias_register.yaml); [PR #2149](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/2149); merge `0943549fd1f180a5dd05d2d1aac12209e9e13002`.
- Domain Lane Register projection: [`../../control_plane/domain_lane_register.yaml`](../../control_plane/domain_lane_register.yaml); [PR #2164](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/2164); merge `6f234b36c6ec30b243ca56e7c6bd1c1ebe2650fc`.
- Cross-Domain Seam Register projection: [`../../control_plane/cross_domain_seam_register.yaml`](../../control_plane/cross_domain_seam_register.yaml); [PR #2187](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/2187); merge `355d30d95bd0687b00cc2b0553bd9731cc8d594c`.

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

**Current status on 2026-08-08:**

- [ ] The architecture v1.3.1 body is still present; tombstoning has not occurred.
- [x] The accepted old-to-canonical path and document-ID mapping is recorded in `control_plane/path_alias_register.yaml`.
- [x] The register projects `dual_read`, `canonical_only` write behavior, zero alias writers, the prior legacy blob, and rollback guardrails.
- [ ] `consumer_closure` remains `OPEN`, `verification_state` remains `PARTIAL`, and current-main enforcement closure remains `NEEDS VERIFICATION`.

### Phase 2 — Reference closure

1. Update active canonical-path and fragment references in bounded batches.
2. Preserve immutable historical receipts and commit-pinned evidence.
3. Validate repository links, anchors, source claims, and rule-section mappings.
4. Prove zero current writers and consumers before physical deletion.

**Current status on 2026-08-08:** reference and fragment closure is incomplete. The alias register preserves the compatibility dependency and exit criteria but does not prove zero consumers or authorize retirement.

### Phase 3 — Executable projection

Machine files project accepted doctrine; they do not accept it, authorize a migration, or grant publication authority.

- [x] Root Registry semantic contract, machine projection, schema, fixtures, validator, tests, and read-only workflow landed in PR #2136.
- [x] `PathDecisionRecord` semantic contract, schema, finite-outcome fixtures, validator, tests, and read-only workflow landed in PR #2138.
- [x] Path Alias Register semantic contract, machine projection, schema, fixtures, validator, tests, and read-only workflow landed in PR #2149.
- [x] Domain Lane Register projection, schema, validator, tests, and read-only workflow landed in PR #2164 as a bounded extension of responsibility-scope governance.
- [x] Cross-Domain Seam Register contract, projection, schema, validator, tests, and read-only workflow landed in PR #2187 as a partial, hold-first Context Map.
- [ ] A consolidated repository-native Make target or equivalent current-main ratchet, required-check coupling, and aggregate enforcement evidence remain `NEEDS VERIFICATION`.
- [ ] None of these projections closes the Phase 1 tombstone or Phase 2 consumer/reference work.

## 6A. Post-Adoption Implementation Record

This section is a status ledger, not a new decision. It records repository evidence at `main@b1e53f67b87973d987aab87359fba906f0f6388f` on 2026-08-08. A later implementation change must update this section or supersede it through normal reviewed documentation, but cannot silently amend the accepted Directory Rules digest or ADR decision.

| Capability | Current repository evidence | Status | Authority boundary |
|---|---|---|---|
| Root Registry | `control_plane/root_registry.yaml`, blob `024f668b5f0a9239bafa4f8b09e2afd86300ff8c`; PR #2136 | `CONFIRMED PRESENT` | `machine_projection_only`; does not create, activate, migrate, retire, or authorize a root |
| Path Decision Record | `contracts/governance/path_decision_record.md`, blob `c91be4f6c2cf0db9db7c07ef10768a98a5d0c247`; PR #2138 | `CONFIRMED PRESENT` | A validated `PLACE`/`SPLIT`/`MIGRATE`/`MIRROR`/`HOLD`/`DENY` record documents reasoning; it does not execute or authorize the outcome |
| Path Alias Register | `control_plane/path_alias_register.yaml`, blob `8a6503fb1c7f419e362cf2ced44ace66eff1aa4d`; PR #2149 | `CONFIRMED PRESENT / PARTIAL` | Projects the one accepted legacy-to-canonical mapping; `consumer_closure: OPEN`, zero alias writers, canonical-only writes, no tombstone or deletion authority |
| Domain Lane Register | `control_plane/domain_lane_register.yaml`, blob `1bfc6f91cfa713a5e3d51ece011b63b46310734f`; PR #2164 | `CONFIRMED PRESENT / PROPOSED` | Projects 13 documented lanes without creating domains, assigning verified stewards, adopting sensitivity policy, or establishing implementation maturity |
| Cross-Domain Seam Register | `control_plane/cross_domain_seam_register.yaml`, blob `dc87ea9c2ab11cc10e51cf4e8284c030e7c9ab29`; PR #2187 | `CONFIRMED PRESENT / PROPOSED PARTIAL` | Records five hold-first seams; does not authorize a cross-domain join, mutation, release, or publication |
| Legacy architecture body | `docs/architecture/directory-rules.md`, blob `18653c00ba193a4afaa3e07a0924452807fb98ef` | `CONFIRMED STILL PRESENT` | Read-only compatibility body; must not receive independent Directory Rules edits |
| Tombstone and physical deletion | No accepted tombstone migration or retirement evidence was verified in this status review | `HOLD` | Requires separate migration PR, reference closure, zero writers, zero consumers, link closure, and retirement receipt |
| Current-main aggregate enforcement | Dedicated schemas, validators, tests, and workflows are present through the cited PRs | `NEEDS VERIFICATION` | Presence and prior PR validation do not prove current-main required-check coupling, ruleset enforcement, or all-workflow health |
| Independent stewardship | No independently verified documentation-governance steward was established in this status review | `NEEDS VERIFICATION` | The transparent single-owner bootstrap exception remains open and is not silently upgraded |

### 6A.1 Non-effects

The post-adoption projections and validators do not:

- change the accepted Directory Rules bytes, digest, document ID, or canonical path;
- accept, amend, supersede, or reverse this ADR;
- convert a `PathDecisionRecord` into migration authority;
- activate, deprecate, retire, or create a root, domain, source, seam, or lifecycle phase;
- tombstone or delete `docs/architecture/directory-rules.md`;
- close external consumers or legacy fragment compatibility;
- create evidence, policy, review, proof, release, deployment, promotion, publication, or public-use authority.

### 6A.2 Next governed increments

The smallest dependency-ordered follow-ups are:

1. verify current-main validator/workflow and required-check coupling without weakening inherited holds;
2. produce a current reference-and-fragment inventory for the legacy architecture path;
3. submit the separate read-only tombstone migration with exact old-blob, anchor mapping, rollback, and consumer evidence;
4. keep physical deletion held until zero-writer, zero-consumer, link-closure, and retirement-receipt evidence exists;
5. establish or explicitly defer independent post-bootstrap stewardship review.

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

### Post-adoption projection rollback

- Revert an individual projection PR only through normal reviewed correction if its removal does not erase required audit or compatibility evidence.
- Preserve this ADR and its accepted decision even if a projection implementation is rolled back.
- Re-run dependent registry, schema, validator, link, and generated-receipt checks after any projection rollback.
- Do not use projection rollback to bypass the tombstone/deletion hold or recreate parallel writable Directory Rules bodies.

## 8. Open Questions

- Which verified independent identity should perform the post-bootstrap review and assume future documentation-governance stewardship?
- What evidence should close the transparent single-owner bootstrap exception without rewriting this accepted decision?
- What expiry or permanent-retention rule should govern the architecture tombstone?
- What exact evidence moves the Path Alias Register from `verification_state: PARTIAL` and `consumer_closure: OPEN` to a verified closed state?
- Which legacy section anchors require explicit compatibility mapping rather than direct replacement?
- Which repository-native command, workflow set, and required-check projection constitute the complete current-main Directory Governance enforcement ratchet?
- Should the full legacy body be retained indefinitely when external-consumer closure cannot be proven, even after all repository-internal references move?

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

> [!NOTE]
> The post-adoption implementation record does not retroactively alter these ratification gates. Machine projection and validator presence are implementation evidence, not additional acceptance authority.

## 10. Change History

| Date | Status | Change | PR |
|---|---|---|---|
| 2026-07-26 | proposed | Initial byte-restoration and proposal packet | [#1763](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/1763) |
| 2026-07-26 | proposed | Clarified the held ratification and deletion boundaries | [#1765](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/1765) |
| 2026-07-26 | accepted | Explicit project-owner ratification; synchronized index transition; premature legacy deletion repaired | [#1774](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/1774) |
| 2026-08-08 | accepted | Added append-only post-adoption implementation-status record; accepted decision and deletion hold unchanged | [#2193](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/2193) |

[Back to top](#top)

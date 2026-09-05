<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://adr/0039
title: Directory Build and Verification Profiles Amendment
type: architecture-decision-record
version: v0.1.0
status: proposed
effective_decision_status: proposed
owners: ["@bartytime4life"]
created: 2026-09-05
updated: 2026-09-05
policy_label: public; governance; non-publisher
owning_root: docs/
responsibility_root: docs/
current_path: docs/adr/ADR-0039-directory-build-and-verification-profiles.md
responsibility: Carry a byte-bound, unadopted Directory Rules amendment and its inactive replacement diff, without changing effective authority or authorizing dependent migration.
base_commit: 8b9c52d88687986879c8f87d7e3835f6a58bbacd
related:
  - ./INDEX.md
  - ./ADR-0029-adopt-directory-governance-standard-v2.md
  - ./directory-rules-v2.1.0-draft.1.patch
  - ../architecture/directory-implementation-profiles.md
  - ../architecture/directory-current-state-20260905.md
  - ../doctrine/directory-rules.md
[/KFM_META_BLOCK_V2] -->

# ADR-0039 — Directory Build and Verification Profiles Amendment

## Status and decision boundary

**PROPOSED / NOT ADOPTED / NO ACTIVE CUTOVER / BRANCH-ONLY REVIEW.** This record registers one candidate decision. It does not accept itself, rewrite ADR-0029, replace effective Directory Rules, change machine projections, authorize migration, or clear #4024/#4228. The owner field is CODEOWNERS routing, not independent approval.

| Field | Value |
| --- | --- |
| Current effective standard | Exact Directory Rules `2.0.0-draft.1` bytes adopted by accepted ADR-0029. |
| Candidate | `2.1.0-draft.1`, additive build/verification/profile amendment. |
| Version rationale | Minor change: nine explicit obligations/refinements; no root-owner or lifecycle reassignment and no removal of an existing rule. More than an editorial patch, not a major reorganization. |
| Supersedes / superseded by | No ADR is superseded by this proposal. Future effective-edition supersession is conditional on acceptance and cutover. |
| Review required | Documentation governance, architecture and affected application/package/test owners; independent review for authority-changing acceptance. No qualifying approval is claimed. |
| Placement basis | Adopted Directory Rules §9.1 and established `docs/adr/` proposal/index mechanism; profiles and observations stay in existing `docs/architecture/`. |
| Separate cleanup | Existing build-context branch at `3d75f67e8ca48c74e1fab43b1fdebefc383e1d23`, not part of this proposal's diff. |

## Context and goal

The repository now has two materially different Explorer compositions, public reusable renderer interfaces, a Python temporal kernel and a TypeScript temporal implementation, bounded API handlers, extensive fixture checks, consumed root/app installer inputs, and a Sites source alias escaping the app directory. A proposed folder name or a README cannot explain those dependencies reliably.

The [pinned inventory](../architecture/directory-current-state-20260905.md) distinguishes code, composition, scaffold, fixture, test, deployment and release evidence. In particular, `apps/packages/` has only a README and `.gitkeep`; the two Explorer apps have different framework/build boundaries; and an app-only export does not include its aliased MapLibre source automatically. These observations justify clarifying ownership and build/test contracts, not renaming apps or accepting ADR-0005 by implication.

Adopted Directory Rules already separate normative law, projections, profiles and repository convergence. Retain that structure and every existing stable rule ID. Add explicit obligations at the seams where current implementation makes their absence costly. Keep volatile feature and build details outside the normative core.

## Proposed decision

Adopt the exact candidate bytes identified below through a distinct future acceptance decision, then perform a separately authorized effective cutover. The candidate has three layers:

- **A: normative standard.** Existing 94 rules are preserved; nine additions address amendment identity, app/package composition, build inputs, bundle boundaries, test placement, traceability and truthful validation.
- **B: implementation profiles.** The [candidate profiles](../architecture/directory-implementation-profiles.md) explain application, package, connector/pipeline, provider, fixture, generated-output, test and hosting conventions without new responsibility roots.
- **C: non-normative inventory.** The [current-state review](../architecture/directory-current-state-20260905.md) binds observations, application recommendation, existing capability IDs, tests, cleanup dispositions and limitations to a specific commit. Inventory updates cannot adopt architecture or promote data.

The `.patch` below is the single editable candidate-text carrier in this proposal. Reconstruct the full candidate from the immutable predecessor; do not maintain a second writable Directory Rules authority. The active doctrine file and compatibility tombstone remain byte-identical in this review unit.

## Exact candidate and predecessor identity

| Artifact | Identity / role |
| --- | --- |
| Predecessor commit/path | `8b9c52d88687986879c8f87d7e3835f6a58bbacd:docs/doctrine/directory-rules.md` |
| Predecessor Git blob | `fd49a0b83e55cef52c1124281f093e263526898d` |
| Predecessor SHA-256 | `44f7e94344cb42b630008eb0bc03a13fcb97dbdfba6f3e56579693a272571e6e` |
| Predecessor adoption record | ADR-0029 blob `a4de0d7a96b78da59cfc499d1025e1508afd8dd9`; the embedded draft label is part of adopted bytes. |
| Candidate Git blob | `706b0d21ed81db88704ee63a913b1660becf98c6` |
| Candidate SHA-256 | `800c704a1c5db1e94bb6936892c731abb8017a002767d9726f9c3f1eb057e31b` |
| [Replacement diff](./directory-rules-v2.1.0-draft.1.patch) SHA-256 | `d70b9ce5851b9e34e892d23db376f683c06e9c9a23f530db4fceb7a34f1e4ed0` |
| Profile SHA-256 | `b827934b1f082467b7a85f31e6e2bf0b07e0cc82d84b73f1675dcb35266c76a6` |
| Inventory SHA-256 | `999745620740872da6ad6d5d25202f27a54e242ee6b582e1a5624016b7cb8727` — non-normative; its digest is provenance, not authority. |

Digests use the complete raw UTF-8 file bytes, including final newline, without line-ending or Unicode normalization. A subsequent edit changes identity and must be re-reviewed; do not silently refresh an approval or make a changed candidate appear previously accepted.

From the repository root of a checkout containing the pinned predecessor, reconstruct into a disposable review directory without changing the active file:

```bash
set -euo pipefail
base=8b9c52d88687986879c8f87d7e3835f6a58bbacd
patch="$(pwd)/docs/adr/directory-rules-v2.1.0-draft.1.patch"
git cat-file -e "${base}^{commit}"
work="$(mktemp -d)"
mkdir -p "$work/docs/doctrine"
git show "${base}:docs/doctrine/directory-rules.md" > "$work/docs/doctrine/directory-rules.md"
(
  cd "$work"
  printf '%s  %s\n' 44f7e94344cb42b630008eb0bc03a13fcb97dbdfba6f3e56579693a272571e6e docs/doctrine/directory-rules.md | sha256sum --check
  git apply --check "$patch"
  git apply "$patch"
  printf '%s  %s\n' 800c704a1c5db1e94bb6936892c731abb8017a002767d9726f9c3f1eb057e31b docs/doctrine/directory-rules.md | sha256sum --check
)
printf 'Unadopted candidate for review: %s\n' "$work/docs/doctrine/directory-rules.md"
```

This is reconstruction, not cutover or adoption. The full reconstructed text accompanies the review download; its bytes must match the candidate digest above.

## Clause-level amendment and supersession ledger

| Clause / section | Classification | Effect / predecessor basis |
| --- | --- | --- |
| Document control, version and notice | Changed conditional authority description | Identifies 2.1 candidate; explains ADR-0029's actual exact-byte adoption. No active replacement. |
| Existing 94 `DIR-*` clauses | Preserved | All identifiers and original rule-definition lines remain byte-identical; no rule is retired. |
| `DIR-AUTH-005`, §2.4 | New explicit obligation; authority-sensitive clarification | Exact amendment identity, separate acceptance/effectiveness, review, compatibility and rollback; preserves DIR-AUTH-004. |
| `DIR-PROFILE-001`, §10.5 | Clarification plus explicit maintenance obligation | Three-layer separation and reuse of existing capability/verification identities; extends §§9, 16, 19–20. |
| `DIR-DEP-004`, §10.5 | Clarification | Legitimate app-local composition/framework files and genuinely shared package interfaces; extends DIR-EXEC-001 and §14. |
| `DIR-BUILD-001`, §10.6 | New obligation | Entrypoint-specific source/installer/lockfile/alias/builder contract; no lockfile removal or policy expansion. |
| `DIR-BUILD-002`, §10.6 | New obligation | Verified export assembly or dependency containment; preserve renderer acquisition and explicit missing-input failure. |
| `DIR-BUILD-003`, §10.6 | Clarification plus explicit bundle-control obligation | Runtime/test/released/generated/accountability separation; preserves §§11 and 15. |
| `DIR-TEST-001`, §10.7 | Clarification plus discovery obligation | Permitted local tests and shared conformance remain distinct; moved tests retain target and CI reachability. |
| `DIR-TEST-002`, §10.7 | New traceability obligation | Stable interfaces and separate maturity axes; no competing registry or private-function inventory. |
| `DIR-TEST-003`, §10.7 | New explicit verification obligation | Exact negative diagnostics, time/privacy/Focus/replay boundaries and comparable failure attribution. |
| §20 notice | Current-state correction | Retains the predecessor's historical convergence record and points to separately pinned observations. |
| §21 amendment cutover | Authority-sensitive clarification | Retains bootstrap phases; separates successor acceptance, projection/enforcement synchronization and held migrations. |
| Version-heading fragment | Compatibility preservation | Explicit `directory-rules-v200-draft1` anchor preserves the predecessor heading target; other existing headings/anchors are retained. |

No changed compatibility writer, root, lifecycle, source admission or release authority is proposed. Rule count becomes 103 in candidate prose; this is not the executable topology engine's count of 20. Inventory and profile revisions are not new adopted rules by themselves.

## Enforcement and cutover design — inactive

Current implementation hard-codes the adopted digest in root, alias, path-decision, domain, cross-domain and topology validators. The topology engine asserts exactly 20 unique operational rule IDs. Root registry and path-alias mechanisms also bind exact authority/projection bytes. A one-line digest replacement would be an invalid shortcut.

A future implementation should extend those existing mechanisms, not add another topology engine or authority registry:

1. **Accept the exact decision separately.** Record explicit acceptance, reviewer identities/roles, scope and any legitimate exception; synchronize this ADR and its canonical index status. Identify the exact candidate/profile bytes. Keep the existing effective binding until the authorized effective transition.
2. **Prepare successor support from accepted evidence.** Bind the existing active projection to the already-accepted decision and candidate identity, with immutable predecessor references. Update the existing dependent validators/alias bindings and applicable schemas coherently. A current-change proposal must not authorize itself.
3. **Validate before activation.** Keep the 20-rule baseline/invariant logic and strict-shrink behavior intact. Test correct predecessor/successor transitions and rejection of wrong bytes, missing/unaccepted decision, current-only authorization, substituted projection, duplicate authority, stale aliases, retained-rule/fragment loss and broadened roots. Assert specific diagnostics, not merely nonzero exit.
4. **Activate atomically under separate authority.** Install the exact standard/profile bytes and synchronize legitimate machine projections/enforcement. Preserve ADR-0029's historical digest and acceptance record. Record effective revision, validation, review and rollback; re-read all dependencies and holds first.
5. **Authorize later migrations independently.** No canonical-app convergence, frozen-catalog correction, alias retirement, data movement, source activation, deployment or release follows automatically.

No successor-enforcement code or active projection edit is included here. The nine additions initially require explicit review evidence; automated coverage is not claimed. A complete executable activation patch and its positive/negative tests remain a prerequisite for cutover, not a reason to block reversible proposal authoring.

## Alternatives and tradeoffs

Directly editing the effective doctrine and hashes would destroy the exact-byte authority distinction; reject. A major rewrite/new tree would increase compatibility and review risk without a demonstrated owner/lifecycle change; reject for this slice. Keeping all current build/test details in the standard would make it stale; use profiles/inventory. Selecting one Explorer immediately would couple rule clarification to an unaccepted application migration; retain distinct compositions pending actual parity/consumer closure.

The additive approach retains some lengthy historical text in v2. That cost preserves IDs, fragments and adoption lineage while the new material stays bounded. Later compaction needs its own explicit no-loss compatibility review, not an automatic cleanup script.

## Validation, delivery and non-goals

Required changed-area checks: candidate reconstruction and raw-byte digests; preservation of old rule definitions and heading/fragment targets; complete ADR/index coherence and its negative tests; new-path naming and relative-link resolution against the pinned tracked inventory; profile/inventory identity; GeneratedReceipt schema/hash binding; unchanged effective authority, aliases, baselines, locks, policies and frozen catalog.

The native ADR commands are `python tools/validators/validate_adr_index.py` and `python -m pytest tests/validators/test_validate_adr_index.py -q --strict-config --strict-markers`, also reached by the existing docs-control-plane workflow. Full topology and schema suites are separate results; inherited cleanup evidence does not certify this proposal. Local reconstruction uses exact exported sources, not a claimed complete local checkout. Hosted results after receipt emission belong in the handoff, not retroactive receipt edits.

Re-pin main, this head and open PR/branch overlap before delivery. Preserve #4024's branch-only boundary until a proven independent one-shot draft path exists; do not create a successor PR to evade it. #4228 remains Stage 1B HOLD / Stage 2 UNAUTHORIZED. No merge, settings, Site/Vercel, source, production-data, deployment or release action is authorized.

## Rollback and open decisions

Before acceptance, remove the unadopted proposal/index row or leave the branch unmerged; effective rules and machine bindings need no rollback because they are unchanged. Preserve the receipt as process history. After any future acceptance/cutover, use a distinct authorized correction to restore a coherent authority/projection/interface state without erasing the intervening decision. Installer/code rollback, data correction and deployed rollback remain separate.

Open decisions: independent review; exact-byte acceptance; successor-enforcement implementation and activation tests; comprehensive external consumers; application canonicality; source-export assembly; oversized/duplicate documentation disposition; current pointer-summary repairs; full browser/device/performance/long-session coverage; incident control exit and all held transitions.

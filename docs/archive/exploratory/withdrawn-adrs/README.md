<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-archive-exploratory-withdrawn-adrs-readme
title: docs/archive/exploratory/withdrawn-adrs — Withdrawn Proposed-ADR Drafts Boundary
type: README
version: v1.0
status: active
owners:
  - "@bartytime4life"
created: 2026-05-25
updated: 2026-08-17
policy_label: repository-facing
owning_root: docs/
parent_boundary: docs/archive/exploratory/README.md
responsibility: "Define the documentation-only archive leaf for distinct proposed ADR drafts voluntarily withdrawn before an accepted or rejected decision, without turning withdrawal or archive presence into decision authority."
truth_posture: "CONFIRMED commit-pinned lane, parent and sibling presence, README-only empty state, accepted Directory Rules v2, current ADR status and inventory surfaces, default CODEOWNERS route, and proposed empty exploratory register / NEEDS VERIFICATION first retained withdrawal, final entry metadata and closure vocabulary, exact future withdrawal evidence, external consumers, independent stewardship, dedicated archive-entry validation, and any future rejected-ADR archive disposition"
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 484245457346a5056551d42c03b9ceccd850251f
  target_prior_blob: 7363922a0d869fc805135aef8b2832a67644e94b
  target_prior_size_bytes: 38843
  target_tree_sha: 0f31cbe74fdca0dbf32b0f37675500d987f47299
  parent_readme_blob: ddb901a7d66343dc1f531afdac8a6a00c2fa2c15
  drafts_readme_blob: 4661b37ee9621783df7bb2a5a2ad12ea7db2e5fc
  idea_packets_readme_blob: 8274b89ddd067a9f09af2c3b7e4f25b5cb5a2b29
  adr_readme_blob: 48d3c1cd5ececbe8f1565f785215b3071cdde21c
  lineage_adr_readme_blob: 124be2be8e7334147d6118398cd84d867544b0ca
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  adr_0029_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  exploratory_register_blob: d04304071eebf7746a113daa8e7c4ffd9d62d94a
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  direct_file_count: 1
  child_directory_count: 0
  retained_withdrawn_adr_entry_count: 0
  exploratory_register_status: PROPOSED
  exploratory_register_entry_count: 0
related:
  - docs/README.md
  - docs/archive/README.md
  - docs/archive/exploratory/README.md
  - docs/archive/exploratory/drafts/README.md
  - docs/archive/exploratory/idea-packets/README.md
  - docs/archive/lineage/README.md
  - docs/archive/lineage/adr/README.md
  - docs/archive/deprecated/README.md
  - docs/adr/README.md
  - docs/adr/INDEX.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - docs/registers/CANONICAL_LINEAGE_EXPLORATORY.md
  - .github/CODEOWNERS
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# docs/archive/exploratory/withdrawn-adrs

`docs/archive/exploratory/withdrawn-adrs/` is KFM's documentation-only archive leaf for a **distinct proposed ADR draft that was voluntarily withdrawn before an accepted or rejected decision**. It preserves the historical proposal and withdrawal context without turning the archived draft, the withdrawal, or the underlying idea into current authority.

> [!IMPORTANT]
> **A retained withdrawal proves only that a specific historical ADR draft was preserved.** It does not prove the proposal was correct, incorrect, rejected, accepted for later work, implemented, released, or safe to reuse. Renewed work must enter the current ADR or authoring process and establish its own evidence, ownership, review, validation, correction, and rollback boundary.

## Quick navigation

- [Status, authority, and current state](#status-authority-and-current-state)
- [Generated repository-state data](#generated-repository-state-data)
- [Purpose and inherited boundary](#purpose-and-inherited-boundary)
- [ADR disposition distinctions](#adr-disposition-distinctions)
- [What belongs here](#what-belongs-here)
- [What does not belong here](#what-does-not-belong-here)
- [Direct-child map](#direct-child-map)
- [Withdrawal transition](#withdrawal-transition)
- [Entry requirements and correction discipline](#entry-requirements-and-correction-discipline)
- [Inputs, outputs, exposure, mutation, and retention](#inputs-outputs-exposure-mutation-and-retention)
- [Validation, ownership, and review](#validation-ownership-and-review)
- [Common decisions](#common-decisions)
- [Related authorities](#related-authorities)
- [Status and rollback](#status-and-rollback)

<!-- Legacy inbound anchor aliases retained from the previous README. -->
<a id="2-authority-level"></a>
<a id="3-status"></a>

## Status, authority, and current state

| Field | Current boundary |
|---|---|
| Path | `docs/archive/exploratory/withdrawn-adrs/` — **CONFIRMED present** on the reviewed `main` snapshot |
| Owning root | [`docs/`](../../../README.md), inherited through [`docs/archive/`](../../README.md) and [`docs/archive/exploratory/`](../README.md) |
| Placement outcome | `PLACE` — same-path boundary modernization; no move, rename, child creation, archived-entry creation, or authority change |
| README profile | `BOUNDARY_COMPACT` under the adopted Directory Rules v2 |
| Primary responsibility | Route a distinct proposed ADR draft into historical retention only after a voluntary pre-decision withdrawal is supported |
| Current direct children | `README.md` only |
| Current archive-entry state | **Zero retained withdrawn-ADR entries** and **zero child directories** |
| ADR status boundary | The adopted ADR model distinguishes `proposed`, `accepted`, `superseded`, and `rejected`; `withdrawn` is this archive lane's bounded historical classification, not a new formal ADR status |
| Rejected-ADR boundary | This README does not select, create, or imply a rejected-ADR archive home; unresolved archive routing returns `HOLD` |
| Human companion | [`CANONICAL_LINEAGE_EXPLORATORY.md`](../../../registers/CANONICAL_LINEAGE_EXPLORATORY.md) is `PROPOSED` and contains zero initial entries |
| Authority limit | Historical proposal and withdrawal context only; never current doctrine, an accepted or rejected decision, an ADR status transition, implementation proof, release state, or publication authority |
| Review route | `@bartytime4life` through the repository's default [`CODEOWNERS`](../../../../.github/CODEOWNERS) rule; routing is not review, approval, independent stewardship, or separation-of-duties proof |

**CONFIRMED:** the directory and README exist; the lane is empty apart from its boundary README; the parent, `drafts/`, and `idea-packets/` contracts are active; Directory Rules v2 is adopted through ADR-0029; and the repository has current ADR inventory and status guidance at `docs/adr/`.

**NEEDS VERIFICATION:** the first retained withdrawal, the exact evidence required to prove voluntary pre-decision withdrawal, final entry metadata and closure vocabulary, external consumers, dedicated archive-entry validation, independent stewardship, and any future rejected-ADR archive disposition.

<a id="generated-repository-state-data"></a>

## Generated repository-state data

The following projection was derived from the exact reviewed commit. It is an **informational, commit-pinned review snapshot**. It is not a live register, ADR decision, archive-entry schema, review record, receipt, proof, or release artifact.

| Observation | Generated value | Interpretation |
|---|---:|---|
| Reviewed commit | `484245457346a5056551d42c03b9ceccd850251f` | Exact `main` state inspected after merged PR #2996 |
| Withdrawn-ADRs directory tree | `0f31cbe74fdca0dbf32b0f37675500d987f47299` | Git tree identity for this lane before this modernization |
| Prior boundary README blob | `7363922a0d869fc805135aef8b2832a67644e94b` | Exact draft-era README bytes replaced by this update |
| Prior boundary README size | `38,843` bytes | Size of the prior README |
| Direct tracked files | `1` | `README.md` only |
| Direct child directories | `0` | No per-entry or topical subtree exists |
| Retained withdrawn-ADR entries | `0` | Count excludes the boundary README |
| Parent exploratory README blob | `ddb901a7d66343dc1f531afdac8a6a00c2fa2c15` | Active parent boundary produced by merged PR #2996 |
| Active drafts README blob | `4661b37ee9621783df7bb2a5a2ad12ea7db2e5fc` | Active sibling for deliberately retired standalone drafts |
| Active idea-packets README blob | `8274b89ddd067a9f09af2c3b7e4f25b5cb5a2b29` | Active sibling for closed documentation-intake packets |
| ADR operating README blob | `48d3c1cd5ececbe8f1565f785215b3071cdde21c` | Current repository-grounded ADR guidance and status model |
| ADR-lineage README blob | `124be2be8e7334147d6118398cd84d867544b0ca` | Existing draft curatorial view; not adopted here as a filing authority |
| Adopted Directory Rules blob | `fd49a0b83e55cef52c1124281f093e263526898d` | Exact bytes adopted by ADR-0029 |
| ADR-0029 blob | `a4de0d7a96b78da59cfc499d1025e1508afd8dd9` | Accepted decision adopting the Directory Rules bytes |
| Companion register blob | `d04304071eebf7746a113daa8e7c4ffd9d62d94a` | Exact reviewed exploratory-register bytes |
| Companion register posture | `PROPOSED` | The register grants no independent admission or closure authority |
| Companion register entries | `0` | Its initial entry set is intentionally empty |
| CODEOWNERS blob | `dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61` | Default GitHub review routing evidence |

### Neighbor and ADR-surface interpretation

| Surface | Posture at the reviewed commit | Bounded effect on this lane |
|---|---|---|
| `drafts/` | Active `v1.1` boundary; zero retained entries | Routes deliberately retired standalone drafts that never became a proposed ADR |
| `idea-packets/` | Active `v1.0` boundary; zero retained entries | Routes explicitly closed documentation-intake packets, not ADR drafts |
| `withdrawn-adrs/` | Draft-era boundary; zero retained entries | This update replaces stale local planning language without adding an entry |
| `docs/adr/README.md` and `INDEX.md` | Current ADR operating and inventory surfaces | Govern current ADR records and reviewed status transitions; archive presence cannot change either |
| `docs/archive/lineage/adr/README.md` | Existing draft curatorial view | Does not establish a general filing home for accepted, rejected, superseded, or withdrawn ADR records |
| `CANONICAL_LINEAGE_EXPLORATORY.md` | `PROPOSED`, zero entries | May become a human review companion; currently grants no archive admission or closure authority |

### Empty-state semantics

A generated count of zero means **no retained withdrawn-ADR entry is tracked in the reviewed repository state**. It does not prove that no proposal was ever withdrawn, that pull-request history is complete, that every closed ADR-shaped branch was inspected, or that an archive entry should be manufactured.

The count rules are intentionally narrow:

- the lane boundary `README.md` is not an archive entry;
- a future direct child file or direct child directory counts as one candidate entry identity until its evidence proves otherwise;
- a closed issue, pull request, branch, review thread, ADR index row, or deleted draft outside this lane is not counted as an archived entry;
- Git tree and blob identities establish path and byte identity, not semantic truth, voluntary withdrawal, safe exposure, or approval;
- the companion register's empty state is reported separately and does not override this directory.

### Snapshot freshness

The snapshot remains historically valid for its pinned commit. Treat it as needing regeneration before asserting current state whenever this directory, the parent or either sibling boundary, the ADR operating or inventory surfaces, the companion register, Directory Rules, ADR-0029, or CODEOWNERS changes materially.

<a id="1-purpose"></a>

## Purpose and inherited boundary

This README refines the parent [`docs/archive/exploratory/README.md`](../README.md) contract for one leaf lane. The parent establishes that exploratory archive content is retained, non-current, and non-authoritative. This leaf narrows that rule to one historical artifact form: a **distinct proposed ADR draft voluntarily closed before a reviewed terminal decision**.

This lane helps reviewers answer:

- What exact ADR draft was retained?
- Which path, branch, issue, pull request, or review surface established its identity?
- Did the artifact actually reach a proposed ADR stage rather than remain a standalone draft, intake packet, or backlog question?
- What evidence supports voluntary withdrawal before acceptance or rejection?
- When and why was the proposal closed?
- Did a separate current ADR, successor idea, or other authority later address the same question?
- Which rights, sensitivity, correction, retention, and rollback rules preserve the record safely?
- How may future work cite the draft without inheriting its authority?

This directory is outside KFM's data lifecycle. Adding documentation here does not perform `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLETS -> PUBLISHED`, admit a source, resolve an `EvidenceRef`, approve policy, accept or reject an ADR, release an artifact, deploy a system, or publish a claim.

<a id="4-adr-status-states-and-where-each-lands"></a>
<a id="41-why-the-distinction-matters"></a>

## ADR disposition distinctions

Preserve the historical distinction without turning this README into ADR-status authority.

| Verified artifact history | This lane's result | Reason |
|---|---|---|
| A distinct ADR draft reached proposed status and the author or accountable proposer voluntarily closed it before an accepted or rejected decision | Candidate for this lane, subject to the remaining admission evidence | This is the bounded historical meaning of `withdrawn-adrs/` |
| The ADR remains proposed or still seeks review | `REJECT` for this lane; keep it at the current ADR or review surface | Archive placement would close active work by implication |
| Review produced an accepted decision | `REJECT` for this lane; retain the decision at its current ADR authority surface | Acceptance is current decision authority, not exploratory withdrawal |
| Review produced a rejected decision | `HOLD` for archive routing unless a governing transition already fixes the destination; do not place it here by inference | Rejection is a reviewed terminal disposition, not voluntary pre-decision withdrawal |
| An accepted ADR was later replaced by an accepted successor | `REJECT` for this lane; preserve `status: superseded` and forward lineage through the current ADR process | Supersession concerns previously accepted authority |
| An ADR-shaped document never reached a supported proposed stage | Route by its actual artifact form—often `drafts/`, `idea-packets/`, current authoring, or no archive entry | ADR shape, filename, or intent does not establish proposed-ADR history |
| A question exists only in an index, issue, backlog, conversation, or planning note | Keep it at its current owning surface unless a distinct archiveable artifact is proven | A candidate question is not a withdrawn ADR |

### Why the distinction matters

- **Withdrawn versus rejected:** withdrawal records a voluntary pre-decision closure; rejection records a reviewed terminal “not adopted” decision. This leaf must not convert one into the other.
- **Withdrawn versus superseded:** a withdrawn proposal never became accepted authority; a superseded ADR was accepted and later replaced.
- **Withdrawn versus never proposed:** a branch draft, intake note, or backlog question may be useful history, but it is not a withdrawn proposed ADR without evidence that the distinct ADR artifact reached the proposed stage.
- **Archive presence versus decision state:** retaining bytes here cannot accept, reject, supersede, reopen, or otherwise change an ADR.
- **Historical relationship versus object identity:** a withdrawn draft may influence later current work, but the archived draft and the later authority remain separate artifacts.

<a id="5-what-belongs-here"></a>

## What belongs here

A human-readable artifact belongs under `docs/archive/exploratory/withdrawn-adrs/` only when all applicable conditions are supported:

1. **Distinct artifact identity.** Exact bytes and a stable source identity are available; the object is more than an inferred idea, index row, or vanished branch description.
2. **Proposed-ADR history.** Repository evidence supports that the artifact was treated as a proposed ADR rather than only a free-form draft, intake packet, scaffold, or candidate question.
3. **Voluntary pre-decision closure.** Evidence supports that the author or accountable proposer withdrew the proposal before a reviewed accepted or rejected outcome.
4. **No current authority.** The retained artifact did not become an accepted ADR, current doctrine, architecture, contract explanation, policy, runbook, or another writable authority.
5. **Explicit closure context.** The date or bounded period, closer, plain-language reason, and relevant review or issue context are preserved as far as repository evidence permits.
6. **Concrete retention value.** Anti-rediscovery, alternatives history, successor rationale, review context, research value, or correction value outweighs repository clutter.
7. **Correct lane.** The artifact is not more accurately a standalone retired draft, closed intake packet, rejected ADR, superseded ADR, previously current document, deprecation record, or ordinary Git history.
8. **Safe exposure.** Rights, privacy, security, sensitivity, and harmful-precision concerns are resolved for repository retention.
9. **One-writer posture.** The archive does not create a second writable current copy or imply that the historical draft remains open.
10. **Review and rollback.** The transition has appropriate review and a reversible or forward-fix path.

There is **no adopted universal word-count threshold, filename pattern, archive-entry ID, closure enum, metadata schema, mandatory register cross-write, child-directory layout, automation workflow, or ADR-number recycling rule** for this lane. Use current authority where it exists; otherwise preserve bounded plain language and return `HOLD` rather than inventing a permanent rule in an entry pull request.

<a id="6-what-does-not-belong-here"></a>

## What does not belong here

| Do not place here | Owning surface or action |
|---|---|
| Active proposed ADRs or work still seeking a decision | Keep at the current ADR, branch, issue, pull request, or review surface |
| Accepted ADRs | Keep at the current ADR authority surface |
| Rejected ADRs without a verified archive transition | Return `HOLD`; this README creates no rejected-ADR home |
| Superseded ADRs | Preserve the ADR at its current path with reviewed supersession status and forward lineage |
| ADR templates, numbered placeholders, slug-only scaffolds, or examples | Keep with the current ADR authoring and inventory surfaces |
| ADR-shaped drafts that never reached a supported proposed stage | Route by actual artifact form, commonly [`../drafts/`](../drafts/README.md), current authoring, or no archive entry |
| Closed documentation-intake packets that never became the ADR object | [`../idea-packets/`](../idea-packets/README.md) |
| Backlog questions, index rows, issues, or conversations with no distinct ADR draft | Keep at their owning current surface |
| Previously current documentation retained as lineage | [`../../lineage/`](../../lineage/README.md), when selected by the governing transition |
| Documentation under explicit deprecation, migration, sunset, or retirement | [`../../deprecated/`](../../deprecated/README.md), when selected by the governing transition |
| Ordinary revision history of a current ADR | Git history at the owning ADR path; do not materialize every revision |
| Contracts, schemas, policy, source records, data instances, evidence, receipts, proofs, release objects, or published carriers | Their governed non-`docs/` authority root |
| Generated previews, lint output, coverage, or temporary QA artifacts | External CI artifacts or the governed generated-output lane |
| Secrets, credentials, personal data, restricted content, unsafe exact locations, or material with unresolved rights | Do not commit; use the applicable protected system and policy path |
| A second writable copy of current decision text | Preserve one writer; use historical references only when authorized |

A filename beginning with `ADR-`, a `proposed` word in prose, a closed pull request, inactivity, an abandoned branch, reviewer disagreement, or the author's preference to retain everything is evidence to inspect—not sufficient archive admission authority.

<a id="8-directory-tree"></a>

## Direct-child map

The current tree is verified from repository evidence and intentionally stops at direct children.

```text
docs/archive/exploratory/withdrawn-adrs/
└── README.md                  # boundary contract; 1 tracked file, 0 entries, 0 child directories
```

This README does not reserve a filename suffix, four-digit pattern, date stamp, closure-kind field, topical subtree, or universal entry schema. The first retained entry must use the smallest identity and metadata shape supported by current repository authority and the specific withdrawal evidence. Adding, removing, or renaming child directories requires the applicable structural review under Directory Rules.

<a id="7-adr-lifecycle-and-the-withdrawal-path"></a>
<a id="19-worked-example--one-withdrawal-end-to-end"></a>

## Withdrawal transition

Use the smallest transition that preserves identity, historical meaning, safety, and rollback:

1. **Freeze exact identity.** Record the candidate bytes, current or prior path, title, document ID when one exists, and relevant commit, branch, issue, pull request, or review context.
2. **Resolve ADR stage.** Confirm that the distinct artifact reached a supported proposed ADR state. Do not infer this from filename or intent alone.
3. **Separate active from closed work.** Confirm an explicit voluntary withdrawal before any accepted or rejected decision; inactivity or a closed review surface is insufficient by itself.
4. **Resolve authority history.** Confirm that the artifact never became accepted authority and distinguish withdrawal from rejection, supersession, deprecation, ordinary revision history, or deletion.
5. **Classify the archive lane.** Compare this leaf with `drafts/`, `idea-packets/`, current ADR surfaces, `lineage/`, `deprecated/`, current authoring, and no-retention. Return `HOLD` when the route is unresolved.
6. **Assess retention value and exposure.** Record why preserving the draft is useful and complete any rights, privacy, security, sensitivity, or precision review required by its content.
7. **Preserve relationships without authority drift.** Add verified origin, withdrawal, successor, related-ADR, or path-not-taken links while keeping the artifact explicitly non-current.
8. **Preserve one writer and current status.** Do not let the archive copy change ADR inventory or decision status, and do not duplicate a writable current body.
9. **Regenerate state and validate.** Refresh the lane and parent projections, run changed-document metadata and local-link checks, and add any ADR, security, sensitivity, migration, or rollback checks required by the actual entry.
10. **Review and stop at a reversible state.** Keep the change reviewable; archive admission does not merge, accept an ADR, release, deploy, or publish.

Finite local outcomes:

| Outcome | Meaning |
|---|---|
| `PLACE` | Exact identity, proposed-ADR history, voluntary pre-decision withdrawal, non-authority, retention value, lane selection, safe exposure, and rollback are sufficiently supported |
| `HOLD` | A required identity, ADR stage, withdrawal fact, authority history, retention rationale, consumer inventory, relationship, or rights or sensitivity review is missing |
| `REJECT` | The artifact remains active, belongs to another artifact type or authority lane, reached a different terminal disposition, duplicates current work, lacks defensible retention value, or cannot be retained safely |
| `ERROR` | The transition or its validation could not complete safely |

These are local archive-review outcomes, not new ADR statuses or a replacement for the Directory Rules placement outcomes.

<a id="9-conventions"></a>
<a id="91-filename-convention-proposed"></a>
<a id="92-hard-rules"></a>

## Entry requirements and correction discipline

This README does not establish a universal archive-entry schema. Before the first or any later withdrawn ADR draft is added, the reviewable transition should preserve enough information to establish:

- exact archived path and stable document identity when available;
- original title and identifier, without allocating or changing an ADR number in this archive change;
- original path, branch, issue, pull request, review, or authoring surface;
- evidence that the artifact reached a proposed ADR stage;
- explicit voluntary withdrawal date or bounded period, accountable closer, and plain-language reason;
- evidence that no accepted or rejected decision preceded the withdrawal;
- related current ADR, successor proposal, resolved dependency, or no-successor rationale when supported;
- concrete retention value;
- rights, sensitivity, privacy, security, and exposure treatment;
- known links, fragments, references, or consumers whose compatibility must be preserved;
- permitted mutation, retention, correction, deletion, and rollback or forward-fix method.

Use an accepted repository vocabulary when one applies. Otherwise prefer bounded plain language and mark unresolved classification as `HOLD`; do not invent a permanent `closure_kind` enum merely to complete an entry.

The proposed [`CANONICAL_LINEAGE_EXPLORATORY.md`](../../../registers/CANONICAL_LINEAGE_EXPLORATORY.md) may serve as a human review companion when a verified entry is added. Its current `PROPOSED` status and empty entry set mean it is not independent admission, closure, or retention authority.

### Identity and revival

This leaf does not allocate, consume, recycle, or reserve ADR numbers. Preserve the identifier the historical artifact actually carried, if one can be verified. Any revived or successor proposal follows the current ADR authoring and inventory process; this archive README does not decide whether a new identifier is required.

### Historical-body rule

Retained withdrawn ADR bodies are **read-mostly**, not silently rewritten:

- preserve the original proposal, uncertainty, alternatives, review context, and historical status;
- use a visible correction note, addendum, metadata fix, or successor link when later evidence changes interpretation;
- redact or replace unsafe material through a reviewed security, privacy, rights, or sensitivity correction when retention would cause harm;
- create a new current ADR proposal or current document when the question is revived rather than editing the archive into current work;
- preserve provenance when reconstructing a draft from a branch, issue, pull request, or prior location;
- never erase an inconvenient withdrawal reason or retroactively describe the draft as rejected, accepted, or superseded.

<a id="10-inputs"></a>
<a id="11-outputs"></a>

## Inputs, outputs, exposure, mutation, and retention

### Inputs

- exact proposed-ADR draft bytes, title, identifier, path or source surface, and identity evidence;
- relevant branch, issue, pull request, review, status, withdrawal, successor, or closure evidence;
- current ADR operating and inventory surfaces;
- current parent and sibling archive contracts;
- current Directory Rules and accepted ADR-0029 decision;
- known links, fragments, navigation, and consumers;
- rights, sensitivity, privacy, security, and exposure evidence;
- correction, retention, deletion, and rollback requirements appropriate to significance.

### Outputs

- one retained human-readable proposed ADR draft, or a bounded metadata or navigation update for an existing retained draft;
- explicit proposed-stage, voluntary withdrawal, non-decision, and non-authority context;
- verified origin, successor, related-ADR, or path-not-taken links;
- repaired direct references where they are proven dependencies of the transition;
- regenerated leaf and parent state projections when the reviewed facts change;
- documentation QA evidence for the changed scope.

The output is historical documentation. It is not an accepted, rejected, or superseded ADR; an ADR status transition; a contract; schema; policy decision; `EvidenceBundle`; review record; receipt; proof; release object; implementation record; or publication artifact.

### Exposure, mutation, and retention

| Surface | Rule |
|---|---|
| This README | Versioned local boundary contract; update when the leaf responsibility, direct children, generated state, validation, or review route changes |
| Generated state table | Commit-pinned informational projection; regenerate rather than editing counts or identities by intuition |
| Retained withdrawn-ADR body | Read-mostly after closure; preserve historical meaning and use visible corrections or a new current artifact instead of silent rewriting |
| Archive metadata and navigation | Versioned updates may improve identity, classification, correction, exposure, provenance, or successor links without changing the historical proposal |
| ADR status and inventory | Remain owned by the current ADR surfaces; archive content cannot mutate them |
| Public exposure | Repository-facing or public only when rights and sensitivity permit; otherwise deny retention here or retain an approved public-safe representation |
| Physical storage | Tracked Git content unless an accepted transition establishes another governed store |
| Retention | Durable only while specific anti-rediscovery, alternatives, lineage, compatibility, audit, correction, review, or research value remains supported |
| Deletion | Final reviewed step after exact identity, known-consumer, rights or sensitivity, correction, and rollback checks; age or cleanup preference is insufficient |
| Rollback | Before merge, close the draft pull request and abandon its branch. After merge, revert the focused commit or apply a reviewed forward fix without recreating parallel writable authorities. |

<a id="12-validation"></a>
<a id="13-review-burden"></a>
<a id="14-anti-patterns"></a>
<a id="20-last-reviewed"></a>

## Validation, ownership, and review

### Repository-native checks

Run the smallest current check set that covers this README:

```bash
python tools/validators/docs/meta-block/check_meta_blocks.py \
  --repo-root . \
  --profile present \
  --registry control_plane/document_registry.yaml \
  --format text \
  docs/archive/exploratory/withdrawn-adrs/README.md

python tools/validators/docs/link-check/check_links.py \
  --repo-root . \
  --format text \
  docs/archive/exploratory/withdrawn-adrs/README.md
```

The repository's bounded documentation workflows may run these checks for changed Markdown. A passing result is documentation QA evidence only; it does not admit a withdrawn ADR, prove the withdrawal facts, change ADR status, create a rejected-ADR home, or authorize implementation, release, deployment, or publication.

### Snapshot regeneration

Before claiming a new current state:

1. pin the exact commit or branch head;
2. list direct objects under `docs/archive/exploratory/withdrawn-adrs/`;
3. count the boundary README separately from non-README candidate entries and child directories;
4. read the exact tree and blob identities;
5. inspect the parent, both sibling lane trees, current ADR operating and inventory surfaces, the companion register, Directory Rules, ADR-0029, and CODEOWNERS;
6. record zero as zero rather than substituting an inferred issue, pull request, branch, backlog, or external artifact count;
7. refresh the parent child-lane projection when the local contract or entry state changes;
8. update the snapshot and last-review table in the same change;
9. run metadata, link, document-graph, stale-reference, build, control-plane, and aggregate validation available for the changed scope.

A snapshot mismatch is not permission to enlarge a topology baseline, invent a missing withdrawal, move an ADR, or rewrite history. Correct the documentation projection, repair an underlying path only when separately authorized, or return `HOLD` or `ERROR`.

### Negative checks

Hold or reject a change that would:

- infer voluntary withdrawal from inactivity, disagreement, an unmerged branch, or a closed issue or pull request alone;
- route an active, accepted, rejected, superseded, never-proposed, or non-ADR artifact into this leaf;
- invent a rejected-ADR home, universal closure enum, filename pattern, ID-reuse rule, mandatory register cross-write, or automation workflow;
- change an ADR's status or inventory row through archive placement;
- create a second writable doctrine, ADR, architecture, contract, schema, policy, evidence, registry, release, receipt, proof, intake, or implementation home;
- silently rewrite a retained proposal's historical body;
- report generated counts or identities without pinning the inspected commit;
- treat a zero-entry state as an error, completion claim, or instruction to manufacture content;
- break a known stable path, fragment, status link, successor link, or consumer without bounded compatibility;
- conceal uncertainty, a failed check, correction lineage, or unresolved sensitivity;
- retain secrets, private information, restricted source material, or harmful precision.

### Ownership and escalation

[`CODEOWNERS`](../../../../.github/CODEOWNERS) routes the default review to `@bartytime4life`. Additional review is required from the affected ADR topic or authority owner when a transition asserts influence on current doctrine or architecture, links to an accepted ADR, changes security or sensitivity treatment, alters a public path, or performs a structural migration.

Escalate instead of guessing when the change would add the first retained withdrawal, reconstruct content from an external or unmerged surface, determine whether an ADR was withdrawn or rejected, decide a rejected-ADR destination, reconcile contradictory ADR identities, retain protected material, remove a stable path, or delete an archive object.

### Last evidence review and triggers

| Field | Value |
|---|---|
| Review date | `2026-08-17` |
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Reviewed base | `main@484245457346a5056551d42c03b9ceccd850251f` |
| Target prior blob | `7363922a0d869fc805135aef8b2832a67644e94b` |
| Target tree | `0f31cbe74fdca0dbf32b0f37675500d987f47299` |
| Parent exploratory README blob | `ddb901a7d66343dc1f531afdac8a6a00c2fa2c15` |
| Current direct payload | `README.md` only: `1` tracked file, `0` child directories, `0` retained withdrawal entries |
| Neighbor entry state | `drafts/`: `0`; `idea-packets/`: `0` |
| Current ADR posture | Current ADR surfaces distinguish proposed, accepted, superseded, and rejected records; this lane changes none of them |
| Human companion | `docs/registers/CANONICAL_LINEAGE_EXPLORATORY.md` at `d04304071eebf7746a113daa8e7c4ffd9d62d94a` — `PROPOSED`, `0` entries |
| Placement authority | Accepted ADR-0029 and adopted `docs/doctrine/directory-rules.md` |
| Review route | Default CODEOWNERS rule at `dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61` |

Re-review this boundary when:

- Directory Rules, ADR-0029, the parent archive contract, or the parent exploratory contract changes materially;
- the first withdrawn ADR draft is added or an existing entry is moved, renamed, corrected, redacted, or deleted;
- current ADR guidance or inventory adopts or changes a withdrawal, rejection, supersession, identity, or archive-transition rule;
- a governing decision establishes a rejected-ADR archive disposition;
- the proposed exploratory register gains an accepted schema or relevant verified entry;
- either sibling lane changes identity, responsibility, or entry state;
- a filename convention, entry schema, closure vocabulary, automation path, or child-directory structure is proposed;
- validation or CODEOWNERS coverage changes;
- a security, privacy, rights, sensitivity, broken-link, correction, or rollback event affects retained material;
- evidence shows this README conflicts with current repository behavior or an accepted transition.

<a id="17-faq"></a>

## Common decisions

### Is “withdrawn” the same as “rejected”?

No. This leaf uses “withdrawn” for a proposed ADR draft voluntarily closed before a reviewed accepted or rejected decision. A rejected ADR has a reviewed terminal disposition. This README does not convert or co-locate the two.

### Where do rejected ADRs belong?

This leaf does not decide that question and creates no rejected-ADR authority. Preserve the record at its current governed ADR surface and return `HOLD` for archive routing unless a reviewed governing transition already establishes the destination.

### Does every closed ADR pull request become an archive entry?

No. A closed pull request is context, not proof of a distinct proposed ADR, voluntary pre-decision withdrawal, retention value, safe exposure, or correct archive routing.

### Does every abandoned ADR-shaped draft belong here?

No. It may belong in `drafts/`, current authoring, an intake surface, ordinary Git history, or nowhere in the tracked archive. Route by verified artifact form and history.

### Can a withdrawn proposal be revived?

Yes, through a new current ADR proposal or other current authoring surface that cites the archived draft as history and explains what changed. This README does not allocate the revived proposal's identifier or status.

### May a current ADR cite a withdrawn draft?

Yes, as historical context or an alternative considered, with an explicit non-authority signal. The archived draft cannot carry the current decision by itself.

### What if the distinction between withdrawn and rejected is unclear?

Return `HOLD`. Do not solve missing review evidence by relabeling the artifact or by assigning a new archive destination.

### May the historical body be corrected?

Use a visible correction note, addendum, metadata repair, redaction, or successor link that preserves the original meaning and provenance. Do not silently rewrite the proposal into current thinking.

<a id="15-related-folders"></a>
<a id="16-adrs-governing-this-folder"></a>
<a id="18-open-questions"></a>

## Related authorities

| Surface | Relationship |
|---|---|
| [`docs/archive/exploratory/README.md`](../README.md) | Immediate parent; owns exploratory archive routing, finite local outcomes, shared entry principles, and non-authority posture |
| [`docs/archive/README.md`](../../README.md) | Parent archive admission, retention, correction, exposure, compatibility, and rollback boundary |
| [`docs/archive/exploratory/drafts/README.md`](../drafts/README.md) | Active sibling lane for deliberately retired standalone exploratory drafts |
| [`docs/archive/exploratory/idea-packets/README.md`](../idea-packets/README.md) | Active sibling lane for explicitly closed documentation-intake packets |
| [`docs/archive/lineage/README.md`](../../lineage/README.md) | Historical predecessors of previously current documentation when a governing transition selects lineage |
| [`docs/archive/lineage/adr/README.md`](../../lineage/adr/README.md) | Existing draft ADR-lineage view; not adopted here as a general filing authority |
| [`docs/archive/deprecated/README.md`](../../deprecated/README.md) | Explicit deprecation, migration, sunset, and retirement dispositions |
| [`docs/adr/README.md`](../../../adr/README.md) | Current repository-grounded ADR operating guidance; archive content cannot change its status model |
| [`docs/adr/INDEX.md`](../../../adr/INDEX.md) | Canonical human ADR inventory; this leaf does not add, remove, renumber, accept, reject, or supersede records |
| [`docs/doctrine/directory-rules.md`](../../../doctrine/directory-rules.md) | Adopted placement, README-profile, one-writer, compatibility, migration, and rollback law |
| [`ADR-0029`](../../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Accepted decision adopting the exact Directory Rules v2 bytes |
| [`CANONICAL_LINEAGE_EXPLORATORY.md`](../../../registers/CANONICAL_LINEAGE_EXPLORATORY.md) | Proposed human review companion; currently contains no entries and grants no independent authority |
| [`CODEOWNERS`](../../../../.github/CODEOWNERS) | Default GitHub review routing; not approval or stewardship proof |
| [`meta-block` validator](../../../../tools/validators/docs/meta-block/check_meta_blocks.py) | Deterministic bounded documentation metadata QA |
| [`link-check` validator](../../../../tools/validators/docs/link-check/README.md) | Deterministic no-network local Markdown link and fragment QA |

## Status and rollback

**CONFIRMED:** same-path boundary modernization; commit-pinned state of one boundary file, zero entries, and zero child directories; active parent, `drafts/`, and `idea-packets/` contracts; accepted Directory Rules v2 authority; current ADR status and inventory surfaces; default CODEOWNERS route; proposed empty exploratory register; and repository-native metadata and local-link validator entrypoints.

**NEEDS VERIFICATION:** the first retained withdrawal, authoritative future withdrawal evidence and entry metadata, rejected-ADR archive disposition, external consumers, independent stewardship, dedicated archive-entry validation, and any future structural migration or deletion.

Rollback this documentation-only update by closing the draft pull request and abandoning its branch before merge. After an authorized merge, revert the focused commits or apply a reviewed forward fix, then regenerate the leaf and parent state projections and rerun metadata, link, document-graph, stale-reference, build, control-plane, and aggregate checks. No ADR is accepted or rejected, and no source, data, policy, runtime, release, deployment, or public-system rollback is required.

[Back to top](#top)

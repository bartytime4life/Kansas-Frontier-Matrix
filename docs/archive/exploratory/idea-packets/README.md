<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-archive-exploratory-idea-packets-readme
title: docs/archive/exploratory/idea-packets — Closed Documentation-Intake Packets Boundary
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
responsibility: "Define the documentation-only archive leaf for explicitly closed documentation-intake packets retained as historical review context without turning intake disposition, archive presence, or the underlying idea into current authority."
truth_posture: "CONFIRMED commit-pinned lane, parent and sibling presence, README-only empty state, accepted Directory Rules v2, CODEOWNERS route, draft and overlapping current intake surfaces, and proposed empty exploratory register / NEEDS VERIFICATION first retained packet, authoritative packet identity and closure vocabulary, final entry metadata, external consumers, independent stewardship, and dedicated archive-entry validation"
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 3e78d5970b071ac11e7f1bcbc024a4282b1bd518
  target_prior_blob: ab2db8a502ac5498c8b2ebab776e5fd8a55bc10b
  target_prior_size_bytes: 48677
  target_tree_sha: b2ee48dcfc46c0da4507a102a7f9332879de61e0
  parent_readme_blob: 6f85fc72d4a4b0690b6b61745961a2ac559381d2
  drafts_readme_blob: 4661b37ee9621783df7bb2a5a2ad12ea7db2e5fc
  withdrawn_adrs_readme_blob: 7363922a0d869fc805135aef8b2832a67644e94b
  intake_readme_blob: 35cc8f301be00526d3334f0778d65d52965a8687
  idea_intake_blob: a02a346807897940752df7cc2fe8f55c86af9a78
  new_ideas_index_blob: c81db07c5f3de4c27f47d20447b3266bd7937b31
  exploratory_register_blob: d04304071eebf7746a113daa8e7c4ffd9d62d94a
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  direct_file_count: 1
  child_directory_count: 0
  retained_idea_packet_entry_count: 0
  exploratory_register_status: PROPOSED
  exploratory_register_entry_count: 0
related:
  - docs/README.md
  - docs/archive/README.md
  - docs/archive/exploratory/README.md
  - docs/archive/exploratory/drafts/README.md
  - docs/archive/exploratory/withdrawn-adrs/README.md
  - docs/archive/lineage/README.md
  - docs/archive/deprecated/README.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/intake/README.md
  - docs/intake/IDEA_INTAKE.md
  - docs/intake/NEW_IDEAS_INDEX.md
  - docs/registers/CANONICAL_LINEAGE_EXPLORATORY.md
  - .github/CODEOWNERS
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# docs/archive/exploratory/idea-packets

`docs/archive/exploratory/idea-packets/` is KFM's documentation-only archive leaf for **explicitly closed documentation-intake packets** that did not become current authority. It preserves a distinct historical review artifact without turning its closure, retention, or underlying idea into doctrine, an accepted decision, implementation evidence, backlog priority, or release authority.

> [!IMPORTANT]
> **A retained packet proves only that a specific historical intake artifact was preserved.** It does not prove that the idea was correct, incorrect, rejected by policy, approved for later work, implemented, released, or safe to reuse. Renewed work must enter a current governed authoring or intake surface and establish its own evidence, ownership, validation, review, and rollback boundary.

## Quick navigation

- [Status, authority, and current state](#status-authority-and-current-state)
- [Generated repository-state data](#generated-repository-state-data)
- [Purpose and inherited boundary](#purpose-and-inherited-boundary)
- [Closure classification](#closure-classification)
- [What belongs here](#what-belongs-here)
- [What does not belong here](#what-does-not-belong-here)
- [Direct-child map](#direct-child-map)
- [Packet closure transition](#packet-closure-transition)
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
| Path | `docs/archive/exploratory/idea-packets/` — **CONFIRMED present** on the reviewed `main` snapshot |
| Owning root | [`docs/`](../../../README.md), inherited through [`docs/archive/`](../../README.md) and [`docs/archive/exploratory/`](../README.md) |
| Placement outcome | `PLACE` — same-path boundary modernization; no move, rename, child creation, archived-entry creation, or authority change |
| README profile | `BOUNDARY_COMPACT` under the adopted Directory Rules v2 |
| Primary responsibility | Route a distinct human-readable documentation-intake packet into historical retention only after explicit closure and only when it did not become current authority |
| Current direct children | `README.md` only |
| Current archive-entry state | **Zero retained idea-packet entries** and **zero child directories** |
| Upstream intake posture | [`docs/intake/`](../../../intake/README.md) exists as a draft, intake-only lane; its current packet/index surfaces overlap and do not establish one adopted archive-entry or closure schema |
| Human companion | [`CANONICAL_LINEAGE_EXPLORATORY.md`](../../../registers/CANONICAL_LINEAGE_EXPLORATORY.md) is `PROPOSED` and contains zero initial entries |
| Authority limit | Historical and design-review context only; never current doctrine, architecture, an accepted or proposed ADR, an intake decision, a contract, schema, policy decision, source record, evidence object, implementation proof, release state, or publication authority |
| Review route | `@bartytime4life` through the repository's default [`CODEOWNERS`](../../../../.github/CODEOWNERS) rule; routing is not review, approval, independent stewardship, or separation-of-duties proof |

**CONFIRMED:** the directory and README exist; the lane is empty apart from its boundary README; the parent archive boundaries are active; the sibling `drafts/` contract is active; the sibling `withdrawn-adrs/` contract remains draft-era; and Directory Rules v2 is the adopted placement authority.

**NEEDS VERIFICATION:** the first retained packet, the authoritative identity of a documentation-intake packet, final closure vocabulary and entry metadata, external consumers, dedicated archive-entry validation, independent stewardship, and any future child structure.

<a id="generated-repository-state-data"></a>

## Generated repository-state data

The following projection was derived from the exact reviewed commit. It is an **informational, commit-pinned review snapshot**. It is not a live registry, intake decision, archive-entry schema, receipt, proof, or release artifact.

| Observation | Generated value | Interpretation |
|---|---:|---|
| Reviewed commit | `3e78d5970b071ac11e7f1bcbc024a4282b1bd518` | Repository state against which the counts and identities were derived |
| Idea-packets directory tree | `b2ee48dcfc46c0da4507a102a7f9332879de61e0` | Git tree identity for this lane |
| Prior boundary README blob | `ab2db8a502ac5498c8b2ebab776e5fd8a55bc10b` | Exact proposal-era README bytes replaced by this modernization |
| Prior boundary README size | `48,677` bytes | Size of the prior README |
| Direct tracked files | `1` | `README.md` only |
| Direct child directories | `0` | No per-entry or topical subtree exists |
| Retained idea-packet entries | `0` | Count excludes the boundary README |
| Parent exploratory README blob | `6f85fc72d4a4b0690b6b61745961a2ac559381d2` | Exact current parent boundary used for this refinement |
| Active sibling README blob | `4661b37ee9621783df7bb2a5a2ad12ea7db2e5fc` | Current `drafts/` boundary |
| Draft-era sibling README blob | `7363922a0d869fc805135aef8b2832a67644e94b` | Current `withdrawn-adrs/` boundary |
| Intake boundary blob | `35cc8f301be00526d3334f0778d65d52965a8687` | Current draft, intake-only `docs/intake/README.md` |
| `IDEA_INTAKE.md` blob | `a02a346807897940752df7cc2fe8f55c86af9a78` | Current overlapping intake surface; not adopted here as an archive schema |
| `NEW_IDEAS_INDEX.md` blob | `c81db07c5f3de4c27f47d20447b3266bd7937b31` | Current draft packet index; not independent closure authority |
| Companion register blob | `d04304071eebf7746a113daa8e7c4ffd9d62d94a` | Exact reviewed exploratory-register bytes |
| Companion register posture | `PROPOSED` | The register is not independent placement or closure authority |
| Companion register entries | `0` | Its initial entry set is intentionally empty |

### Neighbor and upstream interpretation

| Surface | Posture at the reviewed commit | Bounded effect on this lane |
|---|---|---|
| `drafts/` | Active `v1.1` boundary; zero retained entries | Routes deliberately retired standalone drafts, not intake packets |
| `idea-packets/` | Proposal-era boundary; zero retained entries | This update replaces the stale local contract without adding an entry |
| `withdrawn-adrs/` | Draft-era boundary; zero retained entries | Routes only verified proposed-ADR withdrawals under its own future modernization |
| `docs/intake/README.md` | Draft, repository-grounded, intake-only | Confirms the active intake lane but records unresolved lane classification and overlapping packet surfaces |
| `IDEA_INTAKE.md` | Draft; retains unresolved identity, owner, and path claims | Cannot supply a mandatory packet ID, status enum, or archive transition by itself |
| `NEW_IDEAS_INDEX.md` | Draft, repository-grounded, intake-only | May supply packet history, but its labels do not become archive law by citation |
| `CANONICAL_LINEAGE_EXPLORATORY.md` | `PROPOSED`, zero entries | May become a review companion; currently grants no admission, closure, or retention authority |

### Empty-state semantics

A generated count of zero means **no retained entry is tracked in the reviewed repository state**. It does not prove that no intake packet ever existed, that every idea was reviewed, that upstream intake history is complete, or that future entries should be created. Empty is a valid state and must not be “fixed” by manufacturing records.

The count rules are intentionally narrow:

- the lane boundary `README.md` is not an archive entry;
- a future direct child file or direct child directory counts as one candidate entry identity until its local evidence proves otherwise;
- nested files inside one entry directory do not automatically become separate packet identities;
- a row, card, issue, branch, pull request, or backlog question outside this lane is not counted as an archived packet;
- Git tree and blob identities establish path and byte identity, not semantic truth, safe exposure, closure, or approval;
- the companion register's empty state is reported separately and does not override this directory.

### Snapshot freshness

The snapshot remains historically valid for its pinned commit. Treat it as needing regeneration before asserting current state whenever this directory, its parent boundary, either sibling lane, the upstream intake surfaces, the companion register, Directory Rules, ADR-0029, or CODEOWNERS changes materially. A new unrelated commit does not invalidate the historical snapshot, but it prevents the snapshot from being described as current without a fresh comparison.

<a id="1-purpose"></a>

## Purpose and inherited boundary

This README refines the parent [`docs/archive/exploratory/README.md`](../README.md) contract for one leaf lane. The parent establishes that exploratory archive content is retained, non-current, and non-authoritative. This leaf narrows that rule to a particular historical artifact form: a **distinct documentation-intake packet or captured intake record that was explicitly closed without promotion to an owning current-authority surface**.

This lane helps reviewers answer:

- What exact packet or captured intake record was retained?
- Which intake document, source packet, issue, branch, review, or other authoring surface produced it?
- Was the artifact distinct from an index row, standalone draft, proposed ADR, or current document?
- When and why was the packet explicitly closed?
- Did the idea end, merge into another concept, remain dependent on unresolved work, or return later under a new identity?
- Which current artifact or open question may cite the packet as historical context?
- Which rights, sensitivity, correction, retention, and rollback rules preserve the record safely?
- How may future work cite the packet without inheriting its authority?

This directory is outside KFM's data lifecycle. Adding documentation here does not perform `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLETS -> PUBLISHED`, admit a source, resolve an `EvidenceRef`, validate an `EvidenceBundle`, approve policy, classify a county, release an artifact, deploy a system, or publish a claim.

<a id="4-closure-paths--where-an-idea-can-end-up"></a>

## Closure classification

Route by the verified artifact form and authority history, not by age, filename, topic, an intake label, or convenience.

### Fail-closed decision precedence

Apply the following order so a positive fact cannot hide a harder blocker:

1. **Inspection failure → `ERROR`.** Return `ERROR` when exact bytes, path identity, or required governing material cannot be read safely.
2. **Hard exclusion → `REJECT` for this lane.** Active work, current authority, unsafe content, machine trust objects, or a required non-documentation root cannot enter this lane.
3. **Artifact-type routing.** A standalone retired draft routes to `drafts/`; a verified proposed ADR voluntarily withdrawn before decision routes to `withdrawn-adrs/`; previously current or explicitly deprecated material routes through its governing lineage or deprecation transition. Active intake stays in the current intake surface.
4. **Missing positive evidence → `HOLD`.** Unknown packet identity, intake provenance, explicit closure, non-promotion, retention value, exposure, or one-writer posture blocks placement.
5. **All required evidence supported → `PLACE`.** Placement is available only when no earlier rule applies.

| Historical artifact or state | Correct route | Why |
|---|---|---|
| Distinct documentation-intake packet, explicitly closed without promotion to current authority, with supported retention value | **This lane** | It is a real intake-stage historical artifact rather than an inferred idea |
| Open packet, unresolved triage record, or work still seeking a decision | Current authoring or [`docs/intake/`](../../../intake/README.md) surface | Archive placement would close active work by implication |
| Closed index row or brief note with no distinct packet body | Keep the record at its owning intake surface unless a reviewed transition proves a separate archival object | This lane retains artifacts, not every status change |
| Idea promoted into doctrine, an ADR, a contract, schema, policy, implementation, or another current authority | The owning current-authority path, with intake lineage retained where governed | Promotion does not create an archive copy here by implication |
| Standalone exploratory document deliberately retired outside formal intake | [`../drafts/`](../drafts/README.md) | Standalone draft history is a different artifact form |
| Proposed ADR draft voluntarily withdrawn before acceptance or rejection | [`../withdrawn-adrs/`](../withdrawn-adrs/README.md) | Proposed-ADR history is not intake-packet history |
| Rejected ADR or ADR with unresolved final disposition | Governed ADR disposition; return `HOLD` when the repository home is unresolved | This README does not invent a rejected-ADR home |
| Candidate question, atlas backlog item, issue idea, or conversation that never produced a distinct intake packet | No entry here | A question or suggestion is not automatically a packet |
| Previously current documentation retained as supersession history | [`../../lineage/`](../../lineage/README.md), when the governing transition selects lineage | Previously current authority has lineage semantics |
| Documentation under an explicit deprecation, migration, sunset, or retirement disposition | [`../../deprecated/`](../../deprecated/README.md), when the governing transition selects that lane | Deprecation is a governed compatibility transition |
| Source descriptor, data object, evidence, receipt, proof, release object, or published carrier | Its governed non-`docs/` authority root | Trust objects never become documentation packets by relocation |

> [!NOTE]
> One underlying idea may produce several distinct artifacts over time: an intake packet, a standalone memo, an ADR draft, and a current implementation document. Classify each real object by its own form and history. Do not duplicate one body across lanes merely to make every stage appear populated.

### Candidate worksheet

This worksheet is a review aid, not an archive-entry schema.

| Question | Supported result | Unsupported or unknown result |
|---|---|---|
| Can the exact candidate bytes and source identity be read? | Continue | `ERROR` |
| Is the artifact still active or seeking a current decision? | `REJECT` for this lane; keep it active | `HOLD` when activity cannot be resolved |
| Is it a distinct documentation-intake packet or captured intake record? | Continue | Route another artifact type or `REJECT` when no distinct artifact exists |
| Was the idea promoted into a current owning surface? | Keep the current artifact and governed intake lineage outside this lane | `HOLD` when promotion history is unclear |
| Did the object itself become a proposed ADR? | Route the ADR object separately | `HOLD` when ADR history is unclear |
| Is explicit closure supported? | Continue | `HOLD` |
| Is concrete retention value supported? | Continue | `REJECT` when there is no defensible value; otherwise `HOLD` |
| Is repository exposure safe and rights-compatible? | Continue | `REJECT` when unsafe; `HOLD` when review is incomplete |
| Will one writable current authority remain? | `PLACE` may be available | `REJECT` or `HOLD` |

<a id="5-what-belongs-here"></a>

## What belongs here

A human-readable artifact belongs under `docs/archive/exploratory/idea-packets/` only when all applicable conditions are supported:

1. **Distinct packet identity.** The retained object is a real packet or captured intake record with exact bytes or a reproducible reconstruction, not merely an inferred idea, one-line status, or copied excerpt.
2. **Documentation-intake provenance.** Its history connects to a verified KFM documentation-intake, source-map, issue, branch, review, or packet surface.
3. **Explicit closure.** An accountable author, owner, or applicable reviewer deliberately ended active intake work; inactivity, a stale date, or a closed pull request alone is insufficient.
4. **No current-authority promotion.** The packet did not itself become doctrine, an accepted ADR, a current contract or schema explanation, policy source, implementation authority, or another writable current artifact.
5. **Artifact-type separation.** A distinct standalone draft, ADR draft, current document, index row, or machine object is classified independently rather than copied into this lane.
6. **Historical value.** Retention has concrete anti-rediscovery, rationale, alternatives, review, successor-context, research, or correction value that outweighs repository clutter.
7. **Traceable origin.** The original title, source surface, bounded authoring period, and relevant issue, branch, packet, or review context are known as far as the evidence permits.
8. **Safe exposure.** Repository retention does not disclose secrets, personal data, restricted source material, harmful precision, or unresolved rights or sensitivity.
9. **One-writer preservation.** The archive entry cannot become a second writable copy of current work.

There is **no adopted universal word-count threshold, filename pattern, packet-ID format, closure enum, entry schema, register cross-write, or mandatory child layout** for this lane. Use current authority when one exists; otherwise preserve bounded plain language and return `HOLD` rather than inventing a permanent rule in an entry pull request.

Typical admitted material may include:

- a substantive packet explicitly closed after reviewers confirmed that its need was already covered by a current authority;
- a packet deliberately ended because required evidence, ownership, rights, sensitivity review, or dependencies could not be established, when the closure and retention value are explicit;
- a packet absorbed into a differently identified concept, with a verified forward relationship and no claim that “merged” is an adopted repository-wide status;
- an author-closed packet that never became an ADR or current document;
- bounded metadata or navigation required to keep an already-retained packet discoverable and correctly classified.

<a id="6-what-does-not-belong-here"></a>

## What does not belong here

| Do not place here | Owning surface or action |
|---|---|
| Active packets, open intake records, unresolved triage, or material still seeking promotion | Keep in the current authoring, issue, branch, review, or [`docs/intake/`](../../../intake/README.md) surface |
| Promoted packet content or a current doctrine, ADR, architecture, contract, schema, policy, runbook, standard, or implementation document | Keep at the current owning authority path |
| A closed index row, one-sentence note, or status label with no distinct packet body | Retain it at the owning intake surface; do not manufacture an archive file |
| Standalone exploratory drafts authored outside formal intake | [`../drafts/`](../drafts/README.md) |
| Proposed ADRs withdrawn before decision | [`../withdrawn-adrs/`](../withdrawn-adrs/README.md) |
| Rejected ADRs without a verified repository disposition | Return `HOLD`; do not assign a home here |
| Candidate questions, atlas backlog entries, issues, or conversations that never produced a distinct packet | Keep at their owning current surface or close without an archive entry |
| Previously current documentation retained as supersession history | [`../../lineage/`](../../lineage/README.md), when selected by the governing transition |
| Explicit documentation deprecation, migration, sunset, or retirement records | [`../../deprecated/`](../../deprecated/README.md), when selected by the governing transition |
| Ordinary revision history of a current document or packet | Git history at the owning path; do not materialize every prior version |
| Semantic contracts, machine schemas, policy source, source descriptors, data instances, evidence, receipts, proofs, catalogs, release objects, or published carriers | Their governed non-`docs/` authority root |
| Generated previews, lint output, coverage, or temporary QA artifacts | External CI artifacts or the governed generated-output lane |
| Secrets, credentials, personal data, restricted content, unsafe exact locations, or material with unresolved rights | Do not commit; use the applicable protected system and policy path |
| A second writable copy of current documentation | Preserve one writer and use a historical reference, alias, tombstone, or successor link only when authorized |

A packet name, intake ID, closure label, old timestamp, abandoned branch, closed issue, closed pull request, or author's preference to retain everything is evidence to inspect, not archive admission authority.

<a id="8-directory-tree"></a>

## Direct-child map

The current tree is verified from repository evidence and intentionally stops at direct children.

```text
docs/archive/exploratory/idea-packets/
└── README.md                  # boundary contract; 1 tracked file, 0 entries, 0 child directories
```

This README does not reserve a filename pattern, packet-ID family, date-stamped naming scheme, closure-reason enum, topical subtree, or universal entry schema. The first entry must use the smallest naming and metadata shape supported by the governing repository rules and the specific packet evidence. Adding, removing, or renaming child directories requires the applicable structural review under Directory Rules.

<a id="7-intake--closure-lifecycle"></a>
<a id="19-worked-example--one-packet-closure-end-to-end"></a>

## Packet closure transition

Use the smallest transition that preserves identity, historical meaning, safety, and rollback:

1. **Freeze the packet identity.** Record the exact bytes, title, current path or source surface, document ID when one exists, and relevant commit, branch, issue, or review context.
2. **Resolve intake provenance.** Confirm that the candidate was a distinct documentation-intake packet or captured intake record rather than an inferred idea or copied summary.
3. **Separate active from closed work.** Obtain an explicit closure decision; do not infer closure from inactivity, a closed issue, an unmerged pull request, or a failed check.
4. **Resolve authority and artifact history.** Confirm that the packet did not become current authority and identify any distinct standalone draft, ADR, successor, current artifact, or index record that must remain separate.
5. **Classify the lane.** Apply the fail-closed precedence above and compare this leaf with `drafts/`, `withdrawn-adrs/`, `lineage/`, `deprecated/`, active intake, current authority, and no-retention.
6. **Assess retention value and exposure.** Record why preserving the packet is useful and complete any rights, privacy, security, sensitivity, or precision review required by its content.
7. **Preserve relationships without authority drift.** Add verified origin, successor, merged-concept, related-artifact, or path-not-taken links while keeping the archived packet explicitly non-current.
8. **Preserve one writer.** Close or remove obsolete writable copies only when the reviewed transition owns them; do not duplicate a current body into this lane.
9. **Validate and review.** Regenerate the lane snapshot, run the changed-document metadata and local-link checks, and add any topic-specific authority, security, sensitivity, migration, or rollback checks.

Finite outcomes:

| Outcome | Meaning |
|---|---|
| `PLACE` | The exact packet identity, intake provenance, explicit closure, non-promotion, retention value, lane selection, exposure, and rollback posture are sufficiently supported, with no earlier exclusion applying. |
| `HOLD` | A required identity, provenance, authority history, closure decision, retention rationale, consumer inventory, relationship, or rights or sensitivity review is missing. |
| `REJECT` | The artifact remains active, belongs to another artifact type or authority lane, was promoted, duplicates current work, lacks defensible retention value, or cannot be retained safely. |
| `ERROR` | The transition or its validation could not complete safely. |

Archiving the packet is a documentation-state operation only. It does not reject, accept, prioritize, implement, release, deploy, or publish the underlying idea.

<a id="9-conventions"></a>

## Entry requirements and correction discipline

This README does not establish a universal archive-entry schema. Before the first or any later packet is added, the reviewable transition should preserve enough information to establish:

- exact archived path and stable packet or document identity when available;
- original title and the source packet, intake path, issue, branch, shared document, or other authoring surface;
- bounded authoring period and verified author or review route where available;
- explicit closure date, accountable closer, and plain-language closure reason;
- evidence that the packet is no longer active and did not become current authority or the ADR object itself;
- concrete retention value, such as anti-rediscovery, alternatives history, successor rationale, review context, or research value;
- successor, merged concept, related artifact, or no-successor rationale when supported;
- rights, sensitivity, privacy, security, and exposure treatment;
- known links or consumers whose compatibility must be preserved;
- permitted mutation, retention, correction, deletion, and rollback or forward-fix method.

Use an accepted repository vocabulary when one applies. Otherwise prefer bounded plain language and mark unresolved classification as `HOLD`; do not invent a permanent closure enum merely to complete an entry.

The proposed [`CANONICAL_LINEAGE_EXPLORATORY.md`](../../../registers/CANONICAL_LINEAGE_EXPLORATORY.md) may serve as a human review companion when a verified entry is added. Its current `PROPOSED` status and empty entry set mean it is not independent admission, closure, or retention authority.

### Historical-body rule

Retained packet bodies are **read-mostly**, not silently rewritten:

- preserve the original meaning, uncertainty, review context, and historical status;
- use a visible correction note, addendum, metadata fix, or successor link when later evidence changes interpretation;
- redact or replace unsafe content through a reviewed security, privacy, rights, or sensitivity correction when retention would cause harm;
- create a new current intake record, ADR, or document when the idea is revived rather than editing the archive into current work;
- preserve provenance when reconstructing a packet from a branch, issue, shared document, or prior location;
- never erase an inconvenient closure reason merely to improve presentation.

<a id="10-inputs"></a>
<a id="11-outputs"></a>

## Inputs, outputs, exposure, mutation, and retention

### Inputs

- exact packet bytes, title, path or source surface, and identity evidence;
- relevant intake, source-map, issue, branch, review, ADR, successor, or closure evidence;
- current parent and sibling archive contracts;
- current upstream intake surfaces and their verified authority posture;
- known links, fragments, navigation, and consumers;
- rights, sensitivity, privacy, security, and exposure evidence;
- correction, retention, deletion, and rollback requirements appropriate to significance.

### Outputs

- one retained human-readable documentation-intake packet or a bounded metadata or navigation update for an existing retained packet;
- explicit intake provenance, closure, non-promotion, and non-authority context;
- verified origin, successor, merged-concept, related-artifact, or path-not-taken links;
- repaired direct references where they are proven dependencies of the transition;
- documentation QA evidence for the changed scope.

The output is historical documentation. It is not an intake decision, accepted ADR, `SourceDescriptor`, contract, schema, `EvidenceBundle`, `PolicyDecision`, receipt, proof, release object, implementation record, or publication artifact.

### Exposure, mutation, and retention

| Surface | Rule |
|---|---|
| This README | Versioned local boundary contract; update when the leaf responsibility, direct children, generated state, validation, or review route changes |
| Generated state table | Commit-pinned informational projection; regenerate rather than editing counts or identities by intuition |
| Retained packet body | Read-mostly after closure; preserve historical meaning and use visible corrections or a new current artifact instead of silent rewriting |
| Archive metadata and navigation | Versioned updates are permitted when they improve identity, classification, correction, exposure, provenance, or successor links without changing the historical claim |
| Public exposure | Repository-facing or public only when rights and sensitivity permit; otherwise deny retention here or retain an approved public-safe representation |
| Physical storage | Tracked Git content unless an accepted transition establishes another governed store |
| Retention | Durable only while the specific anti-rediscovery, lineage, compatibility, audit, correction, review, or research value remains supported |
| Deletion | Final reviewed step after exact identity, known-consumer, rights or sensitivity, correction, and rollback checks; age or a cleanup campaign is insufficient |
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
  docs/archive/exploratory/idea-packets/README.md

python tools/validators/docs/link-check/check_links.py \
  --repo-root . \
  --format text \
  docs/archive/exploratory/idea-packets/README.md
```

The repository's bounded documentation workflows may run these checks for changed Markdown. A passing check is QA evidence only; it does not admit an archived packet, adopt an entry schema, approve a closure decision, or authorize publication.

### Snapshot regeneration

Before claiming a new current state:

1. pin the exact commit under review;
2. list direct objects under `docs/archive/exploratory/idea-packets/`;
3. count the boundary README separately from non-README candidate entries and child directories;
4. read the exact tree and blob identities;
5. inspect both sibling lane trees, the upstream intake surfaces, the companion register, and CODEOWNERS;
6. record zero as zero rather than substituting a placeholder, inferred backlog, or external packet count;
7. update the snapshot and the last-review table in the same change;
8. run metadata, link, document-graph, stale-reference, and aggregate validation available for the changed scope.

A snapshot mismatch is not permission to enlarge a topology baseline, invent a missing packet, or rewrite history. Correct the README projection, repair the underlying path only when separately authorized, or return `HOLD` or `ERROR`.

### Negative checks

Hold or reject a change that would:

- archive active work or infer closure from inactivity, issue state, branch state, or pull-request state;
- route a standalone draft, proposed ADR, previously current document, deprecation record, or machine trust object into this leaf;
- create a second writable doctrine, architecture, contract, schema, policy, evidence, registry, release, receipt, proof, intake, or implementation home;
- invent a global filename convention, packet-ID format, numeric substance threshold, closure enum, mandatory register cross-write, or child subtree without the required authority;
- silently rewrite a retained packet's historical body;
- report generated counts or identities without pinning the inspected commit;
- treat a zero-entry state as an error, completion claim, or instruction to manufacture content;
- break a known stable path, anchor, successor link, or consumer without bounded compatibility;
- conceal uncertainty, a failed check, correction lineage, or unresolved sensitivity;
- retain secrets, private information, restricted source material, or harmful precision.

### Ownership and escalation

[`CODEOWNERS`](../../../../.github/CODEOWNERS) routes the default review to `@bartytime4life`. Additional review is required from the affected topic or authority owner when a transition asserts influence on current doctrine or architecture, links to an accepted ADR, changes security or sensitivity treatment, alters a public path, or performs a structural migration.

Escalate instead of guessing when the change would create the first retained-packet entry, reconstruct content from an external or unmerged surface, choose among multiple archive lanes, reconcile contradictory intake identities, retain protected material, remove a stable path, or delete an existing archive object.

### Last evidence review and triggers

| Field | Value |
|---|---|
| Review date | `2026-08-17` |
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Reviewed base | `main@3e78d5970b071ac11e7f1bcbc024a4282b1bd518` |
| Target prior blob | `ab2db8a502ac5498c8b2ebab776e5fd8a55bc10b` |
| Target tree | `b2ee48dcfc46c0da4507a102a7f9332879de61e0` |
| Parent exploratory README blob | `6f85fc72d4a4b0690b6b61745961a2ac559381d2` |
| Current direct payload | `README.md` only: `1` tracked file, `0` child directories, `0` retained packet entries |
| Neighbor entry state | `drafts/`: `0`; `withdrawn-adrs/`: `0` |
| Upstream intake state | Draft, intake-only lane with overlapping packet/index surfaces; no adopted archive closure schema established by those files |
| Human companion | `docs/registers/CANONICAL_LINEAGE_EXPLORATORY.md` at `d04304071eebf7746a113daa8e7c4ffd9d62d94a` — `PROPOSED`, `0` entries |
| Placement authority | Accepted ADR-0029 and adopted `docs/doctrine/directory-rules.md` |

Re-review this boundary when:

- Directory Rules, ADR-0029, the parent archive contract, or the parent exploratory contract changes materially;
- the first packet is added or an existing entry is moved, renamed, corrected, redacted, or deleted;
- the upstream intake surfaces converge on an accepted packet identity, closure vocabulary, or transition contract;
- the proposed exploratory register gains an accepted schema or relevant verified entry;
- either sibling lane changes identity, responsibility, or entry state;
- a filename convention, packet-ID family, entry schema, closure vocabulary, or child-directory structure is proposed;
- validation or CODEOWNERS coverage changes;
- a security, privacy, rights, sensitivity, broken-link, correction, or rollback event affects retained material;
- evidence shows the README conflicts with current repository behavior or an accepted transition.

<a id="17-faq"></a>

## Common decisions

### Does every closed intake row become a file here?

No. This lane retains a distinct packet or captured record whose identity, explicit closure, historical value, safe exposure, and correct route are supported. A row, status, or short note with no separate artifact remains at its owning intake surface unless a reviewed transition establishes a distinct archive object.

### Is packet closure the same as rejection?

No. “Closed” says only that active intake work ended. The bounded reason may involve duplication, absorption into another concept, unresolved dependencies, author withdrawal, lack of evidence, a negative decision, or another supported fact. This README does not convert those possibilities into an adopted closure enum.

### What does the generated zero-entry count prove?

Only that the pinned repository state contains no non-README direct child entry under this lane. It does not prove historical nonexistence, complete intake review, or a need to create an entry.

### What happens when an idea is promoted?

The current artifact belongs at its owning authority path, and governed intake lineage remains at the appropriate current surface. Do not copy the promoted body here merely to preserve every stage. A distinct packet may be cited as history only when its separate retention is explicitly supported and does not contradict the parent's non-promotion boundary.

### Can a closed idea return later?

Yes, through a new current intake record, ADR, document, or implementation task that cites the retained packet as historical context. Do not revive the idea by editing the archive body into current work.

### Which closure dispositions are valid?

No adopted repository-wide closure enum was found for this lane. Use an accepted current vocabulary when one is proven to govern the packet; otherwise record the closure in bounded plain language and return `HOLD` when classification matters but remains unresolved.

### What filename should the first packet use?

No filename convention is adopted by this README. Preserve a verified stable identity when one exists, avoid collisions, and choose the smallest reviewable path consistent with current Directory Rules and the specific transition evidence.

### What is the relationship to `withdrawn-adrs/`?

The artifacts are stage-distinct. This lane retains an intake-stage packet that never became current authority. The sibling lane is for a distinct ADR-shaped object that reached proposed status and was voluntarily withdrawn before decision. One idea may have both artifacts only when both objects truly existed and each retention case is independently supported.

### May an archived packet be corrected?

Use a visible metadata correction, addendum, successor link, or reviewed redaction. Preserve the historical body and uncertainty unless safety, legal, rights, or sensitivity obligations require a governed correction.

### Does a closed issue or pull request establish archival closure?

No. Repository state is useful provenance, not independent classification or retention authority. The transition still needs exact packet identity, explicit closure, correct lane selection, safe exposure, and review.

<a id="15-related-folders"></a>
<a id="16-adrs-governing-this-folder"></a>
<a id="18-open-questions"></a>

## Related authorities

| Surface | Relationship |
|---|---|
| [`docs/archive/exploratory/README.md`](../README.md) | Immediate parent; owns exploratory archive routing, finite outcomes, shared entry principles, and non-authority posture |
| [`docs/archive/README.md`](../../README.md) | Parent archive admission, retention, correction, exposure, compatibility, and rollback boundary |
| [`docs/archive/exploratory/drafts/README.md`](../drafts/README.md) | Sibling lane for deliberately retired standalone exploratory drafts |
| [`docs/archive/exploratory/withdrawn-adrs/README.md`](../withdrawn-adrs/README.md) | Sibling lane for verified proposed-ADR drafts voluntarily withdrawn before decision; its local contract remains draft-era |
| [`docs/archive/lineage/README.md`](../../lineage/README.md) | Historical predecessors of previously current documentation when the governing transition selects lineage |
| [`docs/archive/deprecated/README.md`](../../deprecated/README.md) | Explicit deprecation, migration, sunset, and retirement dispositions |
| [`docs/doctrine/directory-rules.md`](../../../doctrine/directory-rules.md) | Adopted placement, README-profile, one-writer, compatibility, migration, and rollback law |
| [`ADR-0029`](../../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Accepted decision adopting the exact Directory Rules v2 bytes |
| [`docs/intake/README.md`](../../../intake/README.md) | Current documentation-intake boundary; draft and intake-only rather than archive authority |
| [`IDEA_INTAKE.md`](../../../intake/IDEA_INTAKE.md) | Current overlapping intake surface; not adopted here as a packet or closure schema |
| [`NEW_IDEAS_INDEX.md`](../../../intake/NEW_IDEAS_INDEX.md) | Current draft packet index; useful lineage evidence but not independent archive authority |
| [`CANONICAL_LINEAGE_EXPLORATORY.md`](../../../registers/CANONICAL_LINEAGE_EXPLORATORY.md) | Proposed human review companion; currently contains no entries and is not independent authority |
| [`meta-block` validator](../../../../tools/validators/docs/meta-block/check_meta_blocks.py) | Deterministic bounded metadata QA |
| [`link-check` validator](../../../../tools/validators/docs/link-check/check_links.py) | Deterministic no-network local Markdown link and fragment QA |

## Status and rollback

**CONFIRMED:** same-path boundary modernization; commit-pinned generated state of one boundary file, zero entries, and zero child directories; active parent exploratory and archive boundaries; active `drafts/` sibling; draft-era `withdrawn-adrs/` sibling; accepted Directory Rules v2 authority; default CODEOWNERS route; draft and overlapping current intake surfaces; proposed empty exploratory register; and repository-native metadata and link-check validators.

**NEEDS VERIFICATION:** the first retained packet, authoritative packet identity, final entry schema and closure vocabulary, external consumers, independent stewardship, dedicated archive-entry validation, and any future structural migration or deletion.

Rollback this documentation-only update by closing the draft pull request and abandoning its branch before merge. After an authorized merge, revert the focused commit or apply a reviewed forward fix, then regenerate the state snapshot and rerun the metadata, link, document-graph, stale-reference, and aggregate checks. No source, data, policy, runtime, release, deployment, or public-system rollback is required.

[Back to top](#top)

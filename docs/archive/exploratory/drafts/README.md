<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-archive-exploratory-drafts-readme
title: docs/archive/exploratory/drafts — Retired Standalone Drafts Boundary
type: README
version: v1.1
status: active
owners:
  - "@bartytime4life"
created: 2026-05-25
updated: 2026-08-17
policy_label: repository-facing
owning_root: docs/
parent_boundary: docs/archive/exploratory/README.md
responsibility: "Define the documentation-only archive leaf for deliberately retired standalone exploratory drafts that never became current authority, an intake packet, or a proposed ADR."
truth_posture: "CONFIRMED commit-pinned lane, parent and sibling presence, README-only empty state, active local boundary, accepted Directory Rules v2, CODEOWNERS route, and proposed empty exploratory register / NEEDS VERIFICATION first retained draft, final entry metadata and closure vocabulary, external consumers, independent stewardship, and dedicated archive-entry validation"
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 2bfd956d386152d149c654c40f600ba9132ff16b
  target_prior_blob: a66d4751c5a666a84aba8119025c284091e5f2d8
  target_prior_size_bytes: 30249
  target_tree_sha: 39bd908b6b454ad8f43af8483770f1cff058d76d
  parent_readme_blob: f9dc6ad3c4f8ad432b208f5a78bdca58fc867b90
  idea_packets_tree_sha: b2ee48dcfc46c0da4507a102a7f9332879de61e0
  withdrawn_adrs_tree_sha: 0f31cbe74fdca0dbf32b0f37675500d987f47299
  exploratory_register_blob: d04304071eebf7746a113daa8e7c4ffd9d62d94a
  direct_file_count: 1
  child_directory_count: 0
  retired_draft_entry_count: 0
  exploratory_register_status: PROPOSED
  exploratory_register_entry_count: 0
related:
  - docs/README.md
  - docs/archive/README.md
  - docs/archive/exploratory/README.md
  - docs/archive/exploratory/idea-packets/README.md
  - docs/archive/exploratory/withdrawn-adrs/README.md
  - docs/archive/lineage/README.md
  - docs/archive/deprecated/README.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/intake/README.md
  - docs/intake/NEW_IDEAS_INDEX.md
  - docs/registers/CANONICAL_LINEAGE_EXPLORATORY.md
  - .github/CODEOWNERS
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>
<a id="-never-promoted-drafts"></a>
<a id="never-promoted-drafts"></a>

# docs/archive/exploratory/drafts

`docs/archive/exploratory/drafts/` is KFM's documentation-only archive leaf for **deliberately retired standalone exploratory drafts** that never became current authority, an intake packet, or a proposed ADR. It preserves useful design history without turning abandoned or unfinished prose into doctrine, architecture, implementation evidence, backlog authority, or a release decision.

> [!IMPORTANT]
> **A retained draft proves only that a specific historical document was preserved.** It does not prove that the draft was correct, rejected by policy, approved for later work, implemented, released, or safe to reuse. Revived work must enter a current governed authoring or intake surface and establish its own evidence, ownership, validation, review, and rollback boundary.

## Quick navigation

- [Status, authority, and current state](#status-authority-and-current-state)
- [Generated repository-state data](#generated-repository-state-data)
- [Purpose and inherited boundary](#purpose-and-inherited-boundary)
- [Closure classification](#closure-classification)
- [What belongs here](#what-belongs-here)
- [What does not belong here](#what-does-not-belong-here)
- [Direct-child map](#direct-child-map)
- [Draft retirement transition](#draft-retirement-transition)
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
| Path | `docs/archive/exploratory/drafts/` — **CONFIRMED present** on the reviewed `main` snapshot |
| Owning root | [`docs/`](../../../README.md), inherited through [`docs/archive/`](../../README.md) and [`docs/archive/exploratory/`](../README.md) |
| Placement outcome | `PLACE` — same-path boundary refinement; no move, rename, child creation, archived-entry creation, or authority change |
| README profile | `BOUNDARY_COMPACT` under the adopted Directory Rules v2 |
| Primary responsibility | Route retained standalone exploratory documents that were deliberately closed before becoming current authority or entering a formal intake or ADR path |
| Current direct children | `README.md` only |
| Current archive-entry state | **Zero retained draft entries** and **zero child directories** |
| Machine companion | [`CANONICAL_LINEAGE_EXPLORATORY.md`](../../../registers/CANONICAL_LINEAGE_EXPLORATORY.md) is `PROPOSED` and contains zero initial entries |
| Authority limit | Historical and design-lineage context only; never current doctrine, architecture, an accepted or proposed ADR, an intake decision, a contract, schema, policy decision, evidence object, implementation proof, release state, or publication authority |
| Review route | `@bartytime4life` through the repository's default [`CODEOWNERS`](../../../../.github/CODEOWNERS) rule; routing is not review, approval, independent stewardship, or separation-of-duties proof |

**CONFIRMED:** the directory and README exist, the lane is empty apart from its boundary README, the parent exploratory boundary is active, and Directory Rules v2 is the adopted placement authority.

**NEEDS VERIFICATION:** the first retained draft, final entry metadata and closure vocabulary, external consumers, dedicated archive-entry validation, independent stewardship, and any future child structure.

<a id="generated-repository-state-data"></a>

## Generated repository-state data

The following projection was regenerated from the exact reviewed commit. It is an **informational, commit-pinned review snapshot**. It is not a live registry, a schema, an admission decision, a receipt, or a release artifact.

| Observation | Generated value | Interpretation |
|---|---:|---|
| Reviewed commit | `2bfd956d386152d149c654c40f600ba9132ff16b` | Repository state against which the counts and hashes were derived |
| Drafts directory tree | `39bd908b6b454ad8f43af8483770f1cff058d76d` | Git tree identity for this lane |
| Boundary README blob | `a66d4751c5a666a84aba8119025c284091e5f2d8` | Exact prior README bytes used for this refinement |
| Boundary README size | `30,249` bytes | Size of the prior boundary README |
| Direct tracked files | `1` | `README.md` only |
| Direct child directories | `0` | No per-entry or topical subtree exists |
| Retained draft entries | `0` | Count excludes the boundary README |
| Companion register blob | `d04304071eebf7746a113daa8e7c4ffd9d62d94a` | Exact reviewed companion-register bytes |
| Companion register posture | `PROPOSED` | The register is not independent archive authority |
| Companion register entries | `0` | Its “Initial entries” section is intentionally empty |

### Neighbor-lane comparison

| Exploratory lane | Tree identity | Boundary files | Archived entries | Contract posture at the reviewed commit |
|---|---|---:|---:|---|
| `drafts/` | `39bd908b6b454ad8f43af8483770f1cff058d76d` | `1` | `0` | Active boundary README |
| `idea-packets/` | `b2ee48dcfc46c0da4507a102a7f9332879de61e0` | `1` | `0` | Draft-era README; modernization remains separate work |
| `withdrawn-adrs/` | `0f31cbe74fdca0dbf32b0f37675500d987f47299` | `1` | `0` | Draft-era README; modernization remains separate work |

### Empty-state semantics

A generated count of zero means **no retained entry is tracked in the reviewed repository state**. It does not prove that no exploratory draft ever existed, that every abandoned idea was reviewed, that the lane is complete, or that future entries should be created. Empty is a valid state and must not be “fixed” by manufacturing records.

The count rules are intentionally narrow:

- the lane boundary `README.md` is not an archive entry;
- a future direct child file or direct child directory counts as one candidate entry identity until its local contract proves otherwise;
- nested files inside one entry directory do not automatically become separate archive entries;
- Git tree and blob hashes establish byte and path identity, not semantic truth, safe exposure, or approval;
- the companion register's empty state is reported separately and does not override this directory.

### Snapshot freshness

The snapshot remains historically valid for its pinned commit. Treat it as needing regeneration before asserting current state whenever this directory, its parent boundary, either sibling lane, the companion register, Directory Rules, ADR-0029, or CODEOWNERS changes materially. A new unrelated commit does not invalidate the historical snapshot, but it does prevent the snapshot from being described as current without a fresh comparison.

<a id="1-purpose"></a>

## Purpose and inherited boundary

This README refines the parent [`docs/archive/exploratory/README.md`](../README.md) contract for one leaf lane. The parent establishes that exploratory archive content is retained, non-current, and non-authoritative. This leaf narrows that rule to a particular artifact form: a **standalone human-readable draft** that was consciously retired without becoming a current KFM authority surface.

This lane helps reviewers answer:

- What exact draft was retained?
- Where and when was it authored?
- Was it ever opened as an intake packet, proposed ADR, current document, or another formal artifact?
- Why was this specific draft closed?
- Did it shape a successor or remain a path not taken?
- Which rights, sensitivity, correction, retention, and rollback rules preserve the record safely?
- How may a future current artifact cite the draft without inheriting its authority?

This directory is outside KFM's data lifecycle. Adding documentation here does not perform `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLETS -> PUBLISHED`, admit a source, validate an `EvidenceBundle`, approve policy, classify a county, release an artifact, deploy a system, or publish a claim.

<a id="4-closure-paths--where-a-draft-fits-among-other-archive-buckets"></a>

## Closure classification

Route by the verified artifact form and authority history, not by age, filename, topic, or convenience.

### Fail-closed decision precedence

Apply the following order so a positive fact cannot hide a harder blocker:

1. **Inspection failure → `ERROR`.** Return `ERROR` when exact bytes, path identity, or required governing material cannot be read safely.
2. **Hard exclusion → `REJECT` for this lane.** Active work, current authority, unsafe content, machine trust objects, or a required non-documentation root cannot enter this lane.
3. **Artifact-type routing.** A formal intake packet routes to `idea-packets/`; a proposed ADR voluntarily withdrawn before decision routes to `withdrawn-adrs/`; previously current or explicitly deprecated material routes through its governing lineage or deprecation transition. Return `HOLD` when that history is unresolved.
4. **Missing positive evidence → `HOLD`.** Unknown closure, identity, retention value, origin, exposure, or one-writer posture blocks placement.
5. **All required evidence supported → `PLACE`.** Placement is available only when no earlier rule applies.

| Historical artifact | Correct route | Why |
|---|---|---|
| Standalone exploratory document, deliberately closed before formal intake, proposed ADR status, or current-authority adoption | **This lane** | It remained a distinct draft throughout its life |
| Structured documentation-intake packet or captured intake record that was later closed | [`../idea-packets/`](../idea-packets/README.md) | Intake is a formal artifact type with its own closure context |
| ADR-shaped artifact that reached proposed status and was voluntarily withdrawn before acceptance or rejection | [`../withdrawn-adrs/`](../withdrawn-adrs/README.md) | Proposed ADR history is not free-form draft history |
| Previously current doctrine, architecture, ADR, runbook, standard, or other canonical documentation that was superseded | [`../../lineage/`](../../lineage/README.md), when the governing transition selects lineage | Previously current authority has lineage semantics |
| Documentation carrying an explicit deprecation, migration, sunset, or retirement disposition | [`../../deprecated/`](../../deprecated/README.md), when the governing transition selects that lane | Deprecation is a governed compatibility transition |
| Active working draft, open proposal, or unresolved review item | Keep in the current authoring, issue, branch, intake, or review surface | Archive placement would close active work by implication |
| An idea that never produced a standalone artifact | No entry here | The lane retains documents, not inferred ideas |
| Multiple distinct artifacts about the same idea | Classify each identity separately; return `HOLD` when the retention pattern is unresolved | One topic does not collapse draft, intake, ADR, and current-document identities |

> [!NOTE]
> A standalone draft may have influenced a later intake packet, ADR, or current document. Influence does not make the artifacts identical. Preserve only the distinct historical objects whose retention is supported, cross-link verified relationships, and avoid duplicating one body merely to populate multiple archive lanes.

### Candidate worksheet

This worksheet is a review aid, not an archive-entry schema.

| Question | Supported result | Unsupported or unknown result |
|---|---|---|
| Can the exact candidate bytes and source identity be read? | Continue | `ERROR` |
| Is the artifact still active or seeking a current decision? | `REJECT` for this lane; keep it active | `HOLD` when activity cannot be resolved |
| Was it ever current authority? | Route through current authority, lineage, or deprecation | Continue only when never-current status is supported |
| Is it itself a formal intake packet? | Route to `idea-packets/` | Continue |
| Did it reach proposed ADR status? | Route to `withdrawn-adrs/` only when voluntary pre-decision withdrawal is supported | `HOLD` when ADR history is unclear |
| Is it a distinct standalone document? | Continue | `REJECT` when it is only copied text or ordinary revision history |
| Is explicit closure supported? | Continue | `HOLD` |
| Is concrete retention value supported? | Continue | `REJECT` when there is no defensible value; otherwise `HOLD` |
| Is repository exposure safe and rights-compatible? | Continue | `REJECT` when unsafe; `HOLD` when review is incomplete |
| Will one writable current authority remain? | `PLACE` may be available | `REJECT` or `HOLD` |

<a id="5-what-belongs-here"></a>
<a id="51-substance-threshold"></a>

## What belongs here

A human-readable artifact belongs under `docs/archive/exploratory/drafts/` only when all applicable conditions are supported:

1. **Standalone identity.** The retained object is a distinct document, not merely an old revision of a current path or text copied out of an intake packet or ADR.
2. **Never current authority.** It never became current doctrine, architecture, an accepted ADR, a current runbook or standard, a contract explanation, or another writable documentation authority.
3. **No formal artifact-type override.** It did not itself become the authoritative intake packet or reach proposed ADR status. Distinct companion artifacts, when they exist, must be classified separately.
4. **Explicit closure.** The author, accountable owner, or applicable reviewer deliberately closed this draft; inactivity alone is insufficient.
5. **Historical value.** Retention has concrete anti-rediscovery, rationale, successor-context, audit, research, or correction value that outweighs repository clutter.
6. **Traceable origin.** The original title, path or source surface, approximate authoring period, and relevant issue, branch, or review context are known as far as the evidence permits.
7. **Safe exposure.** Repository retention does not disclose secrets, personal data, restricted source material, harmful precision, or unresolved rights or sensitivity.
8. **One-writer preservation.** The archive entry cannot become a second writable copy of current work.

There is **no adopted numeric word-count, diagram-count, circulation-count, or filename-date threshold** for this lane. Reviewers should use evidence of historical value and return `HOLD` rather than inventing a universal threshold in an entry PR.

Typical admitted material may include:

- a substantive architecture sketch consciously abandoned before an ADR was opened;
- a design memo whose assumptions were displaced by later verified evidence;
- an exploratory dossier that informed a later, differently identified current artifact;
- a standalone alternatives brief retained to explain a path not taken;
- bounded metadata or navigation required to keep a retained draft discoverable and correctly classified.

<a id="6-what-does-not-belong-here"></a>

## What does not belong here

| Do not place here | Owning surface or action |
|---|---|
| Active drafts, open proposals, unresolved review work, or documents still seeking promotion | Keep in the current authoring, issue, branch, intake, or review surface |
| Closed intake packets or captured intake records | [`../idea-packets/`](../idea-packets/README.md) |
| Proposed ADRs withdrawn before decision | [`../withdrawn-adrs/`](../withdrawn-adrs/README.md) |
| Previously current documentation retained as supersession history | [`../../lineage/`](../../lineage/README.md), when selected by the governing transition |
| Explicit documentation deprecation, migration, sunset, or retirement records | [`../../deprecated/`](../../deprecated/README.md), when selected by the governing transition |
| Ordinary revision history of a current document | Git history at the current path; do not materialize every prior version as an archive file |
| Trivial scratch notes, personal journals, raw todo lists, empty templates, or abandoned fragments with no supported project-history value | Keep outside the repository or close without an archive entry |
| Semantic contracts, machine schemas, policy source, source descriptors, data instances, evidence, receipts, proofs, catalogs, release objects, or published carriers | Their governed non-`docs/` authority root |
| Generated previews, lint output, coverage, or temporary QA artifacts | External CI artifacts or the governed generated-output lane |
| Secrets, credentials, personal data, restricted content, unsafe exact locations, or material with unresolved rights | Do not commit; use the applicable protected system and policy path |
| A second writable copy of current documentation | Preserve one writer and use a historical reference, alias, tombstone, or successor link only when authorized |

A closed pull request, stale branch, old timestamp, “draft” filename, failed experiment, or an author's preference to keep everything is evidence to investigate, not archive admission authority.

<a id="8-directory-tree"></a>

## Direct-child map

The current tree is verified from repository evidence and intentionally stops at direct children.

```text
docs/archive/exploratory/drafts/
└── README.md                  # boundary contract; 1 tracked file, 0 entries, 0 child directories
```

This README does not reserve a filename pattern, date-stamped naming scheme, retirement-reason enum, topical subtree, or universal entry schema. The first entry must use the smallest naming and metadata shape supported by the governing repository rules and the specific artifact evidence. Adding, removing, or renaming child directories requires the applicable structural review under Directory Rules.

<a id="7-draft--closure-lifecycle"></a>
<a id="19-worked-example--one-draft-retirement-end-to-end"></a>

## Draft retirement transition

Use the smallest transition that preserves identity, historical meaning, safety, and rollback:

1. **Freeze the draft identity.** Record the exact bytes, title, current path or source surface, document ID when one exists, and relevant commit, branch, or issue context.
2. **Resolve authority history.** Confirm that the artifact never became current authority and is not itself the formal intake packet or a proposed ADR.
3. **Separate active from closed work.** Obtain an explicit closure decision for this draft; do not infer closure from inactivity or a failed check.
4. **Classify the lane.** Apply the fail-closed precedence above and compare this leaf with `idea-packets/`, `withdrawn-adrs/`, `lineage/`, `deprecated/`, the current authority path, and no-retention.
5. **Assess retention value and exposure.** Record why retaining the draft is useful and complete any rights, privacy, security, sensitivity, or precision review required by its content.
6. **Preserve relationships without authority drift.** Add verified origin, successor, related-artifact, or path-not-taken links while keeping the archived draft explicitly non-current.
7. **Preserve one writer.** Remove or close obsolete writable copies only when the reviewed transition owns them; do not duplicate a current body into this lane.
8. **Validate and review.** Regenerate the lane snapshot, run the changed-document metadata and local-link checks, and add any topic-specific authority, security, sensitivity, migration, or rollback checks.

Finite outcomes:

| Outcome | Meaning |
|---|---|
| `PLACE` | The exact draft identity, never-current status, explicit closure, retention value, lane selection, exposure, and rollback posture are sufficiently supported, with no earlier exclusion applying. |
| `HOLD` | A required identity, authority history, closure decision, retention rationale, consumer inventory, relationship, or rights or sensitivity review is missing. |
| `REJECT` | The artifact remains active, belongs to another artifact type or authority lane, duplicates current work, lacks defensible retention value, or cannot be retained safely. |
| `ERROR` | The transition or its validation could not complete safely. |

Archiving the draft is a documentation-state operation only. It does not accept, reject, prioritize, implement, release, deploy, or publish the underlying idea.

<a id="9-conventions"></a>

## Entry requirements and correction discipline

This README does not establish a universal archive-entry schema. Before the first or any later draft is added, the reviewable transition should preserve enough information to establish:

- exact archived path and stable document identity when available;
- original title and the source path, branch, issue, shared document, or other authoring surface;
- bounded authoring period and verified author or reviewer route where available;
- explicit closure date, accountable closer, and plain-language closure reason;
- evidence that the artifact never became current authority, the formal intake packet, or a proposed ADR;
- concrete retention value, such as anti-rediscovery, alternatives history, successor rationale, or research context;
- successor, merged concept, related artifact, or no-successor rationale when supported;
- rights, sensitivity, privacy, security, and exposure treatment;
- known links or consumers whose compatibility must be preserved;
- permitted mutation, retention, correction, deletion, and rollback or forward-fix method.

Use an accepted repository vocabulary when one applies. Otherwise prefer bounded plain language and mark unresolved classification as `HOLD`; do not invent a permanent enum merely to complete an entry.

The proposed [`CANONICAL_LINEAGE_EXPLORATORY.md`](../../../registers/CANONICAL_LINEAGE_EXPLORATORY.md) may serve as a human review companion when a verified entry is added. Its current `PROPOSED` status and empty entry set mean it is not independent admission, closure, or retention authority.

### Historical-body rule

Retained draft bodies are **read-mostly**, not silently rewritten:

- preserve the original meaning, uncertainty, and historical status;
- use a visible correction note, addendum, metadata fix, or successor link when later evidence changes interpretation;
- redact or replace unsafe content through a reviewed security, privacy, rights, or sensitivity correction when retention would cause harm;
- create a new current intake record, ADR, or document when the idea is revived rather than editing the archive into current work;
- preserve provenance when reconstructing a draft from a branch, shared document, or prior location;
- never erase an inconvenient closure reason merely to improve presentation.

<a id="10-inputs"></a>
<a id="11-outputs"></a>

## Inputs, outputs, exposure, mutation, and retention

### Inputs

- current draft bytes, title, path or source surface, and identity evidence;
- relevant branch, commit, issue, review, intake, ADR, or successor evidence;
- current parent and sibling archive contracts;
- known links, fragments, navigation, and consumers;
- rights, sensitivity, privacy, security, and exposure evidence;
- correction, retention, deletion, and rollback requirements appropriate to significance.

### Outputs

- one retained human-readable standalone draft or a bounded metadata or navigation update for an existing retained draft;
- explicit never-current and closure context;
- verified origin, successor, related-artifact, or path-not-taken links;
- repaired direct references where they are proven dependencies of the transition;
- documentation QA evidence for the changed scope.

The output is historical documentation. It is not an `IdeaIntake`, ADR decision, `SourceDescriptor`, `EvidenceBundle`, `PolicyDecision`, receipt, proof, release object, implementation record, or publication artifact.

### Exposure, mutation, and retention

| Surface | Rule |
|---|---|
| This README | Versioned local boundary contract; update when the leaf responsibility, direct children, generated state, validation, or review route changes |
| Generated state table | Commit-pinned informational projection; regenerate rather than editing counts or hashes by intuition |
| Retained draft body | Read-mostly after closure; preserve historical meaning and use visible corrections or a new current artifact instead of silent rewriting |
| Archive metadata and navigation | Versioned updates are permitted when they improve identity, classification, correction, exposure, provenance, or successor links without changing the historical claim |
| Public exposure | Repository-facing or public only when rights and sensitivity permit; otherwise deny retention here or retain an approved public-safe representation |
| Physical storage | Tracked Git content unless an accepted transition establishes another governed store |
| Retention | Durable only while the specific anti-rediscovery, lineage, compatibility, audit, correction, or research value remains supported |
| Deletion | Final reviewed step after exact identity, known-consumer, rights or sensitivity, correction, and rollback checks; age or a cleanup campaign is insufficient |
| Rollback | Before merge, close the draft PR and abandon its branch. After merge, revert the focused commit or apply a reviewed forward fix without recreating parallel writable authorities. |

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
  docs/archive/exploratory/drafts/README.md

python tools/validators/docs/link-check/check_links.py \
  --repo-root . \
  --format text \
  docs/archive/exploratory/drafts/README.md
```

The repository's bounded documentation workflows may run these checks for changed Markdown. A passing check is QA evidence only; it does not admit an archived draft, adopt an entry schema, approve a closure decision, or authorize publication.

### Snapshot regeneration

Before claiming a new current state:

1. pin the exact commit under review;
2. list direct objects under `docs/archive/exploratory/drafts/`;
3. count the boundary README separately from non-README candidate entries and child directories;
4. read the exact tree and blob identities;
5. inspect both sibling lane trees and the companion register;
6. record zero as zero rather than substituting a placeholder or inferred backlog;
7. update the snapshot and the last-review table in the same change;
8. run metadata, link, document-graph, stale-reference, and aggregate validation available for the changed scope.

A snapshot mismatch is not permission to enlarge a topology baseline or rewrite history. Correct the README projection, repair the underlying path only when separately authorized, or return `HOLD` or `ERROR`.

### Negative checks

Hold or reject a change that would:

- archive active work or infer closure from inactivity;
- route an intake packet, proposed ADR, previously current document, deprecation record, or machine trust object into this leaf;
- create a second writable doctrine, architecture, contract, schema, policy, evidence, registry, release, receipt, proof, or implementation home;
- invent a global filename convention, numeric substance threshold, closure enum, register requirement, or child subtree without the required authority;
- silently rewrite a retained draft's historical body;
- report generated counts or hashes without pinning the inspected commit;
- treat a zero-entry state as an error, completion claim, or instruction to manufacture content;
- break a known stable path, anchor, successor link, or consumer without bounded compatibility;
- conceal uncertainty, a failed check, correction lineage, or unresolved sensitivity;
- retain secrets, private information, restricted source material, or harmful precision.

### Ownership and escalation

[`CODEOWNERS`](../../../../.github/CODEOWNERS) routes the default review to `@bartytime4life`. Additional review is required from the affected topic or authority owner when a transition asserts influence on current doctrine or architecture, links to an accepted ADR, changes security or sensitivity treatment, alters a public path, or performs a structural migration.

Escalate instead of guessing when the change would create the first retained-draft entry, reconstruct content from an external or unmerged surface, choose among multiple archive lanes, retain protected material, remove a stable path, or delete an existing archive object.

### Last evidence review and triggers

| Field | Value |
|---|---|
| Review date | `2026-08-17` |
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Reviewed base | `main@2bfd956d386152d149c654c40f600ba9132ff16b` |
| Target prior blob | `a66d4751c5a666a84aba8119025c284091e5f2d8` |
| Target tree | `39bd908b6b454ad8f43af8483770f1cff058d76d` |
| Parent exploratory README blob | `f9dc6ad3c4f8ad432b208f5a78bdca58fc867b90` |
| Current direct payload | `README.md` only: `1` tracked file, `0` child directories, `0` retained entries |
| Neighbor entry state | `idea-packets/`: `0`; `withdrawn-adrs/`: `0` |
| Machine companion | `docs/registers/CANONICAL_LINEAGE_EXPLORATORY.md` at `d04304071eebf7746a113daa8e7c4ffd9d62d94a` — `PROPOSED`, `0` entries |
| Placement authority | Accepted ADR-0029 and adopted `docs/doctrine/directory-rules.md` |

Re-review this boundary when:

- Directory Rules, ADR-0029, the parent archive contract, or the parent exploratory contract changes materially;
- the first draft is added or an existing entry is moved, renamed, corrected, redacted, or deleted;
- the proposed exploratory register gains an accepted schema or relevant verified entry;
- either sibling lane changes identity, responsibility, or entry state;
- a filename convention, entry schema, closure vocabulary, or child-directory structure is proposed;
- validation or CODEOWNERS coverage changes;
- a security, privacy, rights, sensitivity, broken-link, correction, or rollback event affects retained material;
- evidence shows the README conflicts with current repository behavior or an accepted transition.

<a id="17-faq"></a>

## Common decisions

### Is every abandoned Markdown file archive-worthy?

No. Retain a draft only when its exact identity, explicit closure, historical value, safe exposure, and correct lane are supported. Trivial fragments and personal scratch work may be closed without entering the repository archive.

### Is there a 500-word or diagram threshold?

No adopted threshold was found for this lane. Word count, diagrams, citations, circulation, or influence can support historical value, but none is automatic admission authority. Return `HOLD` when the case is ambiguous.

### What does the generated zero-entry count prove?

Only that the pinned repository state contains no non-README direct child entry under this lane. It does not prove historical nonexistence, complete review coverage, or a need to create an entry.

### What happens when a draft later becomes a current document?

Create or retain the current artifact at its owning authority path. Keep a distinct archived predecessor only when preserving the standalone draft has supported historical value and does not duplicate the current writer. Link the relationship explicitly; do not call the archive body current authority.

### What happens when the same idea also has an intake packet or proposed ADR?

Classify each distinct artifact by its own form and history. Do not automatically copy one body into every lane. Preserve and cross-link multiple objects only when each object is real, distinct, safe, and worth retaining.

### Can a retired draft be revived?

Yes, through a new current artifact—such as a fresh intake record, ADR, architecture document, or other owning surface—that cites the retained draft as historical context. Do not revive the idea by editing the archive body into current work.

### May an archived draft be corrected?

Use a visible metadata correction, addendum, successor link, or reviewed redaction. Preserve the historical body and uncertainty unless safety or legal or rights obligations require a governed correction.

### Does a closed or unmerged pull request establish archival closure?

No. Pull-request state is useful provenance, not independent classification or retention authority. The transition still needs exact identity, explicit closure, correct lane selection, safe exposure, and review.

<a id="15-related-folders"></a>
<a id="16-adrs-governing-this-folder"></a>
<a id="18-open-questions"></a>

## Related authorities

| Surface | Relationship |
|---|---|
| [`docs/archive/exploratory/README.md`](../README.md) | Immediate parent; owns exploratory archive routing, finite outcomes, shared entry principles, and non-authority posture |
| [`docs/archive/README.md`](../../README.md) | Parent archive admission, retention, correction, exposure, compatibility, and rollback boundary |
| [`docs/archive/exploratory/idea-packets/README.md`](../idea-packets/README.md) | Sibling lane for closed documentation-intake artifacts |
| [`docs/archive/exploratory/withdrawn-adrs/README.md`](../withdrawn-adrs/README.md) | Sibling lane for proposed ADR drafts voluntarily withdrawn before decision |
| [`docs/archive/lineage/README.md`](../../lineage/README.md) | Historical predecessors of previously current documentation when the governing transition selects lineage |
| [`docs/archive/deprecated/README.md`](../../deprecated/README.md) | Explicit deprecation, migration, sunset, and retirement dispositions |
| [`docs/doctrine/directory-rules.md`](../../../doctrine/directory-rules.md) | Adopted placement, README-profile, one-writer, compatibility, migration, and rollback law |
| [`ADR-0029`](../../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Accepted decision adopting the exact Directory Rules v2 bytes |
| [`docs/intake/README.md`](../../../intake/README.md) | Current documentation-intake boundary |
| [`NEW_IDEAS_INDEX.md`](../../../intake/NEW_IDEAS_INDEX.md) | Current intake index; not an archive-entry generator by implication |
| [`CANONICAL_LINEAGE_EXPLORATORY.md`](../../../registers/CANONICAL_LINEAGE_EXPLORATORY.md) | Proposed human review companion; currently contains no entries and is not independent authority |
| [`meta-block` validator](../../../../tools/validators/docs/meta-block/check_meta_blocks.py) | Deterministic bounded metadata QA |
| [`link-check` validator](../../../../tools/validators/docs/link-check/check_links.py) | Deterministic no-network local Markdown link and fragment QA |

## Status and rollback

**CONFIRMED:** same-path boundary refinement; commit-pinned generated state of one boundary file, zero entries, and zero child directories; parent exploratory and archive boundaries; accepted Directory Rules v2 authority; default CODEOWNERS route; proposed empty exploratory register; repository-native metadata and link-check validators.

**NEEDS VERIFICATION:** the first retained-draft entry, final entry schema and closure vocabulary, external consumers, independent stewardship, dedicated archive-entry validation, and any future structural migration or deletion.

Rollback this documentation-only update by closing the draft pull request and abandoning its branch before merge. After an authorized merge, revert the focused commit or apply a reviewed forward fix, then regenerate the state snapshot and rerun the metadata, link, document-graph, stale-reference, and aggregate checks. No source, data, policy, runtime, release, deployment, or public-system rollback is required.

[Back to top](#top)

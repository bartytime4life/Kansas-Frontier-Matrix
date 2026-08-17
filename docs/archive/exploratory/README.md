<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-archive-exploratory-readme
title: docs/archive/exploratory — Exploratory Documentation Archive Boundary
type: README
version: v1.1
status: active
owners:
  - "@bartytime4life"
created: 2026-05-25
updated: 2026-08-17
policy_label: repository-facing
owning_root: docs/
parent_boundary: docs/archive/README.md
responsibility: "Define the documentation-only archive lane for closed, withdrawn, or never-promoted exploratory material without converting retained history into current authority."
truth_posture: "CONFIRMED commit-pinned parent and child presence, three README-only child lanes, zero archived entries, active drafts child contract, two remaining draft-era child contracts, accepted Directory Rules v2, and proposed empty exploratory register / NEEDS VERIFICATION remaining child modernization, authoritative closure vocabularies, future entries, external consumers, independent stewardship, and dedicated archive-entry validation"
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  reviewed_base_ref: main
  reviewed_base_commit: 2bfd956d386152d149c654c40f600ba9132ff16b
  branch_snapshot_commit: 87d26036cd18808f717d91f8de3b82ce01ddc1f6
  target_prior_blob: f9dc6ad3c4f8ad432b208f5a78bdca58fc867b90
  target_prior_size_bytes: 24422
  parent_archive_blob: 03b2d6984e3735247da8a3ee0bd1e0ffc09e7e24
  exploratory_tree_sha: 2b132fd0047ecc0b5094b6eec0a75af415fc10a4
  drafts_tree_sha: 7bd03c94b9bb0ba46d4e46fe96d60836166d559a
  drafts_readme_blob: 4661b37ee9621783df7bb2a5a2ad12ea7db2e5fc
  drafts_readme_size_bytes: 38267
  idea_packets_tree_sha: b2ee48dcfc46c0da4507a102a7f9332879de61e0
  idea_packets_readme_blob: ab2db8a502ac5498c8b2ebab776e5fd8a55bc10b
  withdrawn_adrs_tree_sha: 0f31cbe74fdca0dbf32b0f37675500d987f47299
  withdrawn_adrs_readme_blob: 7363922a0d869fc805135aef8b2832a67644e94b
  exploratory_register_blob: d04304071eebf7746a113daa8e7c4ffd9d62d94a
  direct_child_lane_count: 3
  archived_entry_count: 0
  active_child_contract_count: 1
  draft_child_contract_count: 2
  exploratory_register_status: PROPOSED
  exploratory_register_entry_count: 0
related:
  - docs/README.md
  - docs/archive/README.md
  - docs/archive/lineage/README.md
  - docs/archive/deprecated/README.md
  - docs/archive/exploratory/drafts/README.md
  - docs/archive/exploratory/idea-packets/README.md
  - docs/archive/exploratory/withdrawn-adrs/README.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/intake/README.md
  - docs/intake/NEW_IDEAS_INDEX.md
  - docs/registers/CANONICAL_LINEAGE_EXPLORATORY.md
  - .github/CODEOWNERS
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>
<a id="-archived-exploratory-material"></a>
<a id="archived-exploratory-material"></a>

# docs/archive/exploratory

`docs/archive/exploratory/` is KFM's documentation-only archive lane for closed, withdrawn, or never-promoted exploratory material. It preserves design history without allowing retained proposals to masquerade as current doctrine, accepted decisions, implementation evidence, or release authority.

> [!IMPORTANT]
> **Exploratory archive presence proves only that material was retained as history.** It does not prove the material is correct, incorrect, rejected by policy, accepted for future work, implemented, released, or safe for public use. Any renewed work must enter a current governed authoring or intake surface and establish its own evidence, ownership, validation, review, and rollback boundary.

## Quick navigation

- [Status, authority, and current state](#status-authority-and-current-state)
- [Generated child-lane state](#generated-child-lane-state)
- [Purpose and inherited boundary](#purpose-and-inherited-boundary)
- [What belongs here](#what-belongs-here)
- [What does not belong here](#what-does-not-belong-here)
- [Direct-child map](#direct-child-map)
- [Exploratory closure workflow](#exploratory-closure-workflow)
- [Entry requirements and correction discipline](#entry-requirements-and-correction-discipline)
- [Inputs, outputs, exposure, mutation, and retention](#inputs-outputs-exposure-mutation-and-retention)
- [Validation, ownership, and review](#validation-ownership-and-review)
- [Common decisions](#common-decisions)
- [Related authorities](#related-authorities)
- [Status and rollback](#status-and-rollback)

<!-- Legacy inbound anchor aliases retained from the previous README. -->
<a id="1-scope"></a>
<a id="2-repo-fit"></a>

## Status, authority, and current state

| Field | Current boundary |
|---|---|
| Path | `docs/archive/exploratory/` — **CONFIRMED present** on the reviewed repository snapshot |
| Owning root | [`docs/`](../../README.md), inherited through the [`docs/archive/`](../README.md) boundary |
| Placement outcome | `PLACE` — same-path parent correction and generated-state refresh; no move, rename, child creation, or authority change |
| README profile | `BOUNDARY_COMPACT` under the adopted Directory Rules v2 |
| Primary responsibility | Route retained human documentation that never became current authority into the correct exploratory child lane |
| Current direct children | `drafts/`, `idea-packets/`, and `withdrawn-adrs/`, plus this README |
| Current entry state | Each child contains its boundary README only; **zero archived exploratory entries are present** |
| Child-contract state | `drafts/` is active and current for its bounded role; `idea-packets/` and `withdrawn-adrs/` retain draft-era metadata and planning language |
| Authority limit | Historical and design-lineage context only; never current doctrine, an accepted ADR, a contract, schema, policy decision, evidence object, release state, or implementation proof |
| Review route | `@bartytime4life` through the repository's default [`CODEOWNERS`](../../../.github/CODEOWNERS) rule; routing is not review, approval, stewardship, or separation-of-duties proof |

**CONFIRMED:** the lane, its three direct child directories, all four README files, and the zero-entry state exist in the reviewed repository state.

**NEEDS VERIFICATION:** modernization of the two remaining draft-era child READMEs, final closure vocabulary for each child, future entry metadata, external consumers, independent stewardship, and dedicated archive-entry validation.

<a id="generated-child-lane-state"></a>

## Generated child-lane state

This table is a commit-pinned documentation projection, not a live registry or trust object. It corrects the former parent claim that all three child READMEs were still draft-era.

| Child lane | Tree identity | README identity | Boundary status | Direct payload | Archived entries |
|---|---|---|---|---:|---:|
| `drafts/` | `7bd03c94b9bb0ba46d4e46fe96d60836166d559a` | `4661b37ee9621783df7bb2a5a2ad12ea7db2e5fc` | `active`, `v1.1` | `1` file | `0` |
| `idea-packets/` | `b2ee48dcfc46c0da4507a102a7f9332879de61e0` | `ab2db8a502ac5498c8b2ebab776e5fd8a55bc10b` | draft-era contract | `1` file | `0` |
| `withdrawn-adrs/` | `0f31cbe74fdca0dbf32b0f37675500d987f47299` | `7363922a0d869fc805135aef8b2832a67644e94b` | draft-era contract | `1` file | `0` |

| Aggregate observation | Generated value |
|---|---:|
| Exploratory child lanes | `3` |
| Active child contracts | `1` |
| Draft-era child contracts | `2` |
| Child lanes with retained entries | `0` |
| Total retained exploratory entries | `0` |
| Companion register posture | `PROPOSED` |
| Companion register entries | `0` |

### Interpretation limits

- `0` entries means no non-README entry is tracked in the reviewed lane; it does not prove that no historical artifact ever existed.
- A README status describes that local boundary contract, not the acceptance or rejection of underlying ideas.
- Tree and blob hashes establish exact path and byte identity only.
- A draft-era child README remains readable routing evidence but cannot expand this parent's adopted authority.
- Empty child lanes must not be populated merely to make the archive appear complete.

### Freshness

Regenerate this state before describing it as current whenever a child path, child README, archived entry, companion register, parent archive contract, Directory Rules, ADR-0029, or CODEOWNERS changes materially. Preserve the old values as historical evidence only when the update explains which commit they describe.

<a id="3-inputs--what-belongs-here"></a>

## Purpose and inherited boundary

This README refines the parent [`docs/archive/README.md`](../README.md) contract for one child lane. The parent establishes that archived documentation is retained, non-current, and non-authoritative. This lane narrows that rule to human-readable material that **never became current authority** or was voluntarily closed before an authority-bearing decision was reached.

The lane helps reviewers answer:

- What exploratory artifact was retained?
- Which current or historical surface did it originate from?
- Did it remain a standalone draft, become an intake packet, or reach a proposed ADR stage?
- Why was it closed or withdrawn?
- What current artifact, open question, or future intake record may reference it?
- Which correction, exposure, retention, and rollback rules preserve the historical record safely?

This directory is outside KFM's data lifecycle. Moving documentation here does not perform `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLETS -> PUBLISHED`, admit a source, resolve an `EvidenceRef`, approve policy, release an artifact, deploy a system, or publish a claim.

<a id="4-exclusions--what-does-not"></a>

## What belongs here

A human-readable artifact belongs under `docs/archive/exploratory/` only when all applicable conditions are supported:

1. Its primary responsibility is documentation rather than executable behavior or a trust-object instance.
2. It never became current doctrine, an accepted ADR, an authoritative contract or schema explanation, an active runbook, or another current writable documentation authority.
3. Its active review or intake work is closed, withdrawn, or deliberately not advanced.
4. Its exact identity and artifact form are known well enough to select one child lane.
5. The closure or withdrawal reason is preserved at the level required to avoid misleading future readers.
6. Retention does not expose secrets, private data, restricted source material, protected precise locations, or unresolved rights and sensitivity.
7. No second writable copy of current material is created.

Typical admitted material may include:

- a substantive standalone design draft that was consciously retired without becoming current authority;
- a closed documentation-intake packet that was not promoted to an owning authority surface;
- a proposed ADR draft voluntarily withdrawn before acceptance or rejection;
- small metadata, index, or navigation records required to preserve the exploratory disposition.

> [!NOTE]
> A useful idea may still be archived here. Archive placement says the **historical artifact is closed**, not that the underlying question can never be revisited.

## What does not belong here

| Do not place here | Owning surface or action |
|---|---|
| Active drafts, open intake packets, or work still seeking a decision | Keep in the current authoring, intake, issue, branch, or review surface |
| Current doctrine, architecture, ADRs, runbooks, standards, or domain guidance | Keep at the current writable documentation authority |
| Previously current documentation retained as supersession history | [`../lineage/`](../lineage/README.md) when the governing transition selects lineage |
| Documentation under an explicit deprecation, migration, sunset, or retirement disposition | [`../deprecated/`](../deprecated/README.md) when the governing transition selects that lane |
| Rejected ADRs without a verified repository disposition | Return `HOLD`; this README does not invent a rejected-ADR home |
| Semantic contracts, machine schemas, or policy source | `contracts/`, `schemas/`, or `policy/` |
| Source descriptors, data instances, evidence, receipts, proofs, catalogs, or published carriers | Their governed `data/` family |
| Release manifests, promotion decisions, correction notices, withdrawal notices, or rollback cards | `release/` |
| Generated previews, lint output, coverage, or temporary QA artifacts | External CI artifacts or the governed generated-output lane |
| Secrets, credentials, personal data, restricted content, or unsafe exact locations | Do not commit; use the applicable protected system and policy path |

Age, inactivity, a closed pull request, a failed experiment, or the word “draft” is not enough to establish exploratory archive placement.

<a id="5-directory-layout"></a>
<a id="8-subfolders"></a>

## Direct-child map

The current tree is verified from repository evidence and intentionally stops at the direct children plus their README-only state.

```text
docs/archive/exploratory/
├── README.md
├── drafts/
│   └── README.md              # active boundary; 0 retained entries
├── idea-packets/
│   └── README.md              # draft-era boundary; 0 retained entries
└── withdrawn-adrs/
    └── README.md              # draft-era boundary; 0 retained entries
```

| Child lane | Bounded role | Current evidence | Local contract |
|---|---|---|---|
| `drafts/` | Standalone exploratory documents that never became current authority | Directory and active README present; no archived entries | [`drafts/README.md`](drafts/README.md) |
| `idea-packets/` | Closed documentation-intake packets retained as historical review context | Directory and draft-era README present; no archived entries | [`idea-packets/README.md`](idea-packets/README.md) |
| `withdrawn-adrs/` | Proposed ADR drafts voluntarily withdrawn before an acceptance or rejection decision | Directory and draft-era README present; no archived entries | [`withdrawn-adrs/README.md`](withdrawn-adrs/README.md) |

Only `idea-packets/README.md` and `withdrawn-adrs/README.md` still contain broad draft-era planning and placeholder language. Their presence is implementation evidence; their unreviewed vocabularies, thresholds, record shapes, or lifecycle claims are not automatically adopted by this parent.

<a id="6-lifecycle-intake--exploratory"></a>
<a id="10-authoring-workflow"></a>

## Exploratory closure workflow

Apply this fail-closed order:

1. **Inspection failure → `ERROR`.** Stop when exact identity, bytes, or governing material cannot be read safely.
2. **Wrong authority history or unsafe exposure → `REJECT` for this lane.** Active work, previously current authority, non-documentation objects, or unsafe material cannot be placed here.
3. **Select the exact child by artifact form.** Standalone never-promoted draft → `drafts/`; closed intake packet → `idea-packets/`; voluntarily withdrawn proposed ADR → `withdrawn-adrs/`.
4. **Missing identity, closure, route, retention, or review evidence → `HOLD`.**
5. **All requirements supported → `PLACE`.**

Use the smallest transition that preserves identity, one-writer authority, historical meaning, and rollback:

1. **Resolve the artifact identity.** Record the exact path, document ID when one exists, current bytes, authoring form, and current authority state.
2. **Separate active from closed work.** Do not archive an open draft, open intake packet, active ADR proposal, or current writable document.
3. **Classify the disposition.** Determine whether the artifact is exploratory closure, lineage, deprecation, correction, withdrawal, or another state; return `HOLD` when the distinction is unresolved.
4. **Select the child lane.** Route by verified artifact form—not by topic, age, filename, or convenience.
5. **Preserve closure evidence.** Keep the reason, date, originating surface, relevant current or successor work, review route, and any sensitivity treatment needed to interpret the record.
6. **Preserve compatibility and one writer.** Repair verified direct links and metadata without creating a second writable copy or silently rewriting the historical body.
7. **Regenerate state and validate.** Refresh the child-lane counts and identities, run changed-document metadata and local-link checks, and add any artifact-specific authority, security, sensitivity, or migration checks.

Finite outcomes:

| Outcome | Meaning |
|---|---|
| `PLACE` | The exact identity, never-current status, closure evidence, child lane, exposure, and retention posture are sufficiently supported, with no earlier exclusion applying. |
| `HOLD` | A required identity, authority decision, closure reason, child classification, consumer inventory, or rights or sensitivity review is missing. |
| `REJECT` | The artifact remains active, was previously current authority, belongs to another responsibility root, would create a parallel writer, or cannot be retained safely. |
| `ERROR` | The transition or its validation could not complete safely. |

An exploratory archive transition is a documentation-state operation only. It does not promote, publish, release, deploy, or approve the archived content.

<a id="7-immutability-invariant"></a>
<a id="9-conventions"></a>

## Entry requirements and correction discipline

This parent README does not establish a universal archive-entry schema. Before an artifact is added, the reviewable transition should preserve enough information to establish:

- exact path and stable document identity when available;
- artifact form and selected child lane;
- closure or withdrawal kind and bounded reason;
- closure date and verified author or review route;
- originating intake, ADR, branch, issue, or authoring surface when available;
- related current work, successor, merged concept, or no-successor rationale;
- exposure, rights, sensitivity, and any required redaction or generalization;
- permitted mutation, retention, correction, and rollback method;
- known links or consumers whose compatibility must be preserved.

The proposed [`CANONICAL_LINEAGE_EXPLORATORY.md`](../../registers/CANONICAL_LINEAGE_EXPLORATORY.md) may be used as a human review companion when an applicable entry exists. Its current `PROPOSED` status and empty entry set mean it is not independent placement or closure authority.

### Historical-body rule

Archived exploratory bodies are **read-mostly**, not silently rewritten:

- preserve the original meaning, uncertainty, and historical status;
- use a visible correction note, addendum, metadata fix, or successor link when later evidence changes the interpretation;
- redact or replace unsafe material through a reviewed security, privacy, rights, or sensitivity correction when retention would cause harm;
- create a new current intake record, ADR, or document when the idea is revived rather than editing the archive into current work;
- never erase an inconvenient closure reason merely to improve presentation.

<a id="inputs-outputs-exposure-mutation-and-retention"></a>

## Inputs, outputs, exposure, mutation, and retention

### Inputs

- current documentation bytes, path, identity, and authority state;
- the relevant intake, ADR, branch, issue, review, or closure evidence;
- current parent and child archive contracts;
- generated child-lane counts and identities;
- known links, fragments, navigation, and consumers;
- rights, sensitivity, privacy, security, and exposure evidence;
- correction and rollback requirements appropriate to significance.

### Outputs

- a retained human-readable exploratory artifact or bounded archive metadata or navigation update;
- explicit closure, withdrawal, or never-promoted context;
- regenerated child-lane state when the reviewed facts change;
- repaired direct references where they are verified dependencies of the transition;
- documentation QA evidence for the changed scope.

The output is historical documentation. It is not a `SourceDescriptor`, `EvidenceBundle`, `PolicyDecision`, receipt, proof, release object, or publication record.

### Exposure, mutation, and retention

| Surface | Rule |
|---|---|
| This README | Versioned boundary contract; update when the lane responsibility, direct children, generated state, validation, or review route changes |
| Child README | Versioned local contract; each child must remain consistent with this parent without expanding its authority |
| Generated child-lane state | Commit-pinned informational projection; regenerate exact counts and identities rather than editing by intuition |
| Archived body | Read-mostly after closure; preserve historical meaning and use visible corrections or a new current artifact instead of silent rewriting |
| Archive metadata and indexes | Versioned updates are permitted when they improve identity, navigation, correction, exposure, or successor links without changing the historical claim |
| Public exposure | Repository-facing or public only when rights and sensitivity permit; otherwise deny retention here or retain an approved public-safe representation |
| Physical storage | Tracked Git content unless an accepted transition establishes another governed store |
| Retention | Durable while needed for anti-rediscovery, lineage, compatibility, auditability, or correction; deletion is a final reviewed step after exact identity, consumer, sensitivity, and rollback checks |
| Rollback | Before merge, close the draft PR and abandon its branch. After merge, revert the focused commit or apply a reviewed forward fix without recreating two writable authorities. |

<a id="11-faq"></a>
<a id="12-related-docs"></a>
<a id="13-last-reviewed"></a>

## Validation, ownership, and review

### Repository-native checks

Run the smallest current check set that covers both changed boundaries:

```bash
python tools/validators/docs/meta-block/check_meta_blocks.py \
  --repo-root . \
  --profile present \
  --registry control_plane/document_registry.yaml \
  --format text \
  docs/archive/exploratory/README.md \
  docs/archive/exploratory/drafts/README.md

python tools/validators/docs/link-check/check_links.py \
  --repo-root . \
  --format text \
  docs/archive/exploratory/README.md \
  docs/archive/exploratory/drafts/README.md
```

The repository's bounded documentation workflows may run these checks for changed Markdown. A passing result is documentation QA evidence only; it does not adopt a child contract, approve an archived idea, validate its source claims, or authorize implementation, release, or publication.

### State regeneration checks

Before claiming a new current state:

1. pin the exact commit or branch head;
2. list direct objects in all three child lanes;
3. count each boundary README separately from non-README entry identities;
4. read each child README's exact status and byte identity;
5. inspect the companion register status and entry section;
6. preserve zero values without converting them to placeholders or inferred backlog;
7. update the generated table and last-review data in the same change;
8. run metadata, link, document-graph, stale-reference, and aggregate checks available for the changed scope.

### Negative checks

Hold or reject a change that would:

- make archived exploratory prose appear current or authoritative;
- archive active work or previously current authority under the wrong child lane;
- claim all child contracts share one status when the exact files disagree;
- invent a rejected-ADR or universal closure vocabulary without a governing decision;
- move or delete a document without the required identity, authority, consumer, and rollback evidence;
- create a second writable doctrine, contract, schema, policy, evidence, registry, release, receipt, proof, or current-documentation home;
- report generated counts or hashes without a pinned state;
- treat a zero-entry lane as an error or instruction to manufacture records;
- break a known stable path, fragment, or successor or reference link without bounded compatibility;
- conceal uncertainty, a failed validation, closure context, correction lineage, or sensitivity concern;
- retain secrets, private information, restricted source material, or harmful precision.

### Ownership and escalation

[`CODEOWNERS`](../../../.github/CODEOWNERS) routes the default review to `@bartytime4life`. Additional review is required from the affected authority owner when an archive change alters doctrine or ADR history, security or sensitivity posture, public navigation, or a structural migration.

Escalate instead of guessing when a change would create, rename, merge, split, or retire a child lane; decide the disposition of rejected ADRs; remove a stable or externally consumed path; change exposure of protected information; or contradict an accepted ADR or the parent archive contract.

### Last evidence review and triggers

| Field | Value |
|---|---|
| Review date | `2026-08-17` |
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Reviewed base | `main@2bfd956d386152d149c654c40f600ba9132ff16b` |
| Branch snapshot after leaf refresh | `87d26036cd18808f717d91f8de3b82ce01ddc1f6` |
| Target prior blob | `f9dc6ad3c4f8ad432b208f5a78bdca58fc867b90` |
| Parent archive blob | `03b2d6984e3735247da8a3ee0bd1e0ffc09e7e24` |
| Exploratory tree | `2b132fd0047ecc0b5094b6eec0a75af415fc10a4` |
| Current direct children | `drafts/`, `idea-packets/`, `withdrawn-adrs/` |
| Current child payload state | Each child contains `README.md` only; total archived entries: `0` |
| Child contract state | `1` active (`drafts/`), `2` draft-era (`idea-packets/`, `withdrawn-adrs/`) |
| Machine companion | `docs/registers/CANONICAL_LINEAGE_EXPLORATORY.md` at `d04304071eebf7746a113daa8e7c4ffd9d62d94a` — `PROPOSED`, `0` entries |
| Placement authority | Accepted [`ADR-0029`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) and adopted [`Directory Rules`](../../doctrine/directory-rules.md) |

Re-review this boundary when:

- Directory Rules, ADR-0029, or the parent archive contract changes materially;
- a child is added, removed, renamed, merged, split, or changes responsibility;
- the first archived artifact is admitted to any child lane;
- a child README is modernized or its closure vocabulary changes;
- the generated child-lane state no longer matches the inspected tree or file bytes;
- intake or ADR state vocabularies are adopted or superseded;
- validation or CODEOWNERS coverage changes;
- a correction, withdrawal, sensitive-data event, broken link, or rollback affects retained exploratory material;
- evidence shows this README conflicts with repository behavior or a governing transition.

## Common decisions

### Is every abandoned draft an archive candidate?

No. The artifact must be substantive enough to preserve, explicitly closed, safely retainable, and classifiable without creating a second writer. Trivial scratch notes may be deleted from an unmerged branch rather than admitted as durable history.

### What does the zero-entry aggregate prove?

Only that the pinned repository state contains no non-README entry identity in the three child lanes. It does not prove historical nonexistence, complete intake coverage, or a need to populate the archive.

### How is an archived idea revived?

Open a new current intake record, ADR proposal, or documentation artifact that cites the archived item as history and explains what evidence or conditions changed. Do not mutate the archived body into active work.

### Does “withdrawn” mean “rejected”?

No. This lane uses `withdrawn-adrs/` for voluntary author withdrawal before a terminal review decision. The repository disposition for formally rejected ADRs is not decided here and remains `HOLD` until governed evidence resolves it.

### May current documentation cite an exploratory artifact?

Yes, for historical context, prior alternatives, or lineage. The citation must identify the target as exploratory and must not rely on it as current authority or implementation proof.

### May source data, evidence, or release objects be archived here?

No. This lane owns human documentation only. Trust objects and lifecycle instances remain with their governed object families.

## Related authorities

| Surface | Relationship |
|---|---|
| [`docs/archive/README.md`](../README.md) | Parent archive boundary and child-lane routing authority |
| [`docs/archive/lineage/README.md`](../lineage/README.md) | Historical predecessors and supersession context for material that was current authority |
| [`docs/archive/deprecated/README.md`](../deprecated/README.md) | Explicit documentation deprecation, migration, sunset, and retirement dispositions |
| [`docs/archive/exploratory/drafts/README.md`](drafts/README.md) | Active child contract for retired standalone drafts |
| [`docs/archive/exploratory/idea-packets/README.md`](idea-packets/README.md) | Draft-era child contract for closed documentation-intake packets |
| [`docs/archive/exploratory/withdrawn-adrs/README.md`](withdrawn-adrs/README.md) | Draft-era child contract for voluntarily withdrawn proposed ADRs |
| [`docs/intake/README.md`](../../intake/README.md) | Current documentation-intake lane; not source or data intake authority |
| [`docs/intake/NEW_IDEAS_INDEX.md`](../../intake/NEW_IDEAS_INDEX.md) | Draft, intake-only packet index; not promotion authority |
| [`CANONICAL_LINEAGE_EXPLORATORY.md`](../../registers/CANONICAL_LINEAGE_EXPLORATORY.md) | Proposed human review register with no current entries |
| [`Directory Rules`](../../doctrine/directory-rules.md) | Adopted responsibility-root, README-inheritance, placement, migration, and rollback law |
| [`ADR-0029`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Accepted decision adopting the exact Directory Rules v2 bytes |
| [`CODEOWNERS`](../../../.github/CODEOWNERS) | Default GitHub review routing; not approval or stewardship proof |
| [`meta-block` validator](../../../tools/validators/docs/meta-block/check_meta_blocks.py) | Bounded documentation metadata QA |
| [`link-check` validator](../../../tools/validators/docs/link-check/README.md) | Deterministic, no-network local Markdown target and fragment QA |

## Status and rollback

**CONFIRMED:** same-path parent correction; three direct child lanes; README-only zero-entry state; active `drafts/` boundary; two remaining draft-era child contracts; parent archive contract; accepted Directory Rules v2 authority; default CODEOWNERS route; proposed empty exploratory register; repository-native metadata and local-link validator entrypoints.

**NEEDS VERIFICATION:** modernization of `idea-packets/` and `withdrawn-adrs/`, authoritative child closure vocabularies and entry metadata, rejected-ADR disposition, first real archive entries, external consumers, independent stewardship, and dedicated archive-entry validation.

Rollback this documentation-only update by closing the draft pull request and abandoning its branch before merge. After an authorized merge, revert the focused commits or apply a reviewed forward fix, regenerate the child-lane state, and rerun metadata, link, document-graph, stale-reference, and aggregate checks. No source, data, policy, runtime, release, deployment, or public-system rollback is required.

[Back to top](#top)

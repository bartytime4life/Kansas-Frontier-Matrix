<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-archive-deprecated-readme
title: docs/archive/deprecated — Deprecation and Retirement Documentation Boundary
type: README
version: v1.0
status: active
owners:
  - "@bartytime4life"
created: 2026-05-25
updated: 2026-08-17
policy_label: repository-facing
owning_root: docs/
parent_boundary: docs/archive/README.md
responsibility: "Define the documentation-only archive lane for explicit deprecation, migration, sunset, and retirement dispositions without creating removal, release, or current-authority effects."
truth_posture: "CONFIRMED current repository, accepted Directory Rules, parent archive contract, CODEOWNERS route, and empty proposed deprecation register / NEEDS VERIFICATION accepted deprecation-process authority, future lane entries, external consumers, and dedicated entry validation"
related:
  - docs/README.md
  - docs/archive/README.md
  - docs/archive/lineage/README.md
  - docs/archive/exploratory/README.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/governance/DEPRECATION_PROCESS.md
  - docs/doctrine/corrections-first-class.md
  - control_plane/deprecation_register.yaml
  - .github/CODEOWNERS
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>
<a id="-archived-deprecated-material"></a>

# docs/archive/deprecated

`docs/archive/deprecated/` is KFM's documentation-only archive lane for material whose **deprecation, migration, sunset, or retirement disposition is explicit**. It keeps a transition inspectable without allowing deprecated material to remain current authority.

> [!IMPORTANT]
> **This lane records or retains a governed documentation disposition; it does not perform the disposition.** A file is not deprecated because it is old, moved here, listed in a register, or past a date. The governing decision must identify the exact artifact, successor or no-successor rationale, compatibility treatment, review state, and safe closure path.

## Quick navigation

- [Status, authority, and current state](#status-authority-and-current-state)
- [Purpose and inherited boundary](#purpose-and-inherited-boundary)
- [What belongs here](#what-belongs-here)
- [What does not belong here](#what-does-not-belong-here)
- [Direct-child map](#direct-child-map)
- [Deprecation transition](#deprecation-transition)
- [Entry requirements and timing](#entry-requirements-and-timing)
- [Inputs, outputs, exposure, mutation, and retention](#inputs-outputs-exposure-mutation-and-retention)
- [Validation, ownership, and review](#validation-ownership-and-review)
- [Common decisions](#common-decisions)
- [Related authorities](#related-authorities)

<!-- Legacy inbound anchor aliases retained from the previous README. -->
<a id="2-repo-fit"></a>

## Status, authority, and current state

| Field | Current boundary |
|---|---|
| Path | `docs/archive/deprecated/` — **CONFIRMED present** on the reviewed `main` snapshot |
| Owning root | [`docs/`](../../README.md), inherited through the [`docs/archive/`](../README.md) boundary |
| Placement outcome | `PLACE` — same-path modernization of an existing boundary README; no move, rename, lane creation, or authority change |
| README profile | `BOUNDARY_COMPACT` under the adopted Directory Rules v2 |
| Primary responsibility | Explain when documentation may be retained here under an explicit deprecation or retirement disposition |
| Current direct children | `README.md` only; **no deprecated artifacts are currently present in this lane** |
| Machine companion | [`control_plane/deprecation_register.yaml`](../../../control_plane/deprecation_register.yaml) exists with status `PROPOSED` and `entries: []` on the reviewed snapshot |
| Process companion | [`DEPRECATION_PROCESS.md`](../../governance/DEPRECATION_PROCESS.md) exists as a draft governance document; it is guidance, not accepted authority by itself |
| Authority limit | Historical/deprecation context only; never current doctrine, a migration decision, removal approval, release state, or publication authority |
| Review route | `@bartytime4life` through the repository's default [`CODEOWNERS`](../../../.github/CODEOWNERS) rule; additional review depends on the affected authority boundary |

**CONFIRMED:** the directory exists, currently contains only this README, and sits under the accepted `docs/` responsibility root.

**NEEDS VERIFICATION:** future entries, external consumers, the acceptance status of the broader deprecation process, any dedicated archive-entry validator, and every future move or deletion.

<a id="1-scope"></a>

## Purpose and inherited boundary

This README refines the parent [`docs/archive/README.md`](../README.md) contract for one child lane. The parent owns archive-wide routing and establishes that archived material is non-current documentation. This lane narrows that rule to documentation carrying an explicit deprecation, migration, sunset, or retirement disposition.

A deprecation record may help readers answer:

- What exact documentation identity is being retired or migrated?
- Which accepted decision or reviewed transition governs it?
- What remains current, and where is the successor?
- Which stable path, alias, tombstone, or retained copy preserves compatibility?
- When is the next review or sunset checkpoint?
- What correction, rollback, or forward-fix path applies if the transition is wrong?

This directory is outside KFM's data lifecycle. Adding a document here does not perform `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLETS -> PUBLISHED`, approve a release, or change a public system.

<a id="3-inputs--what-belongs-here"></a>

## What belongs here

A documentation artifact or record belongs here only when all applicable conditions are supported:

1. Its primary responsibility is human-readable documentation.
2. Its exact identity and current authority state are known.
3. An accepted ADR, reviewed migration/deprecation decision, or other applicable governing record explicitly establishes the disposition.
4. The successor is identified, or a reviewed no-successor rationale is recorded.
5. Stable-path, link, fragment, and known-consumer treatment is defined.
6. Retention does not expose secrets, private data, restricted source material, or harmful precision.
7. The governing transition explicitly selects this lane rather than an in-place tombstone, alias, retained original path, or another authority-specific lineage mechanism.

Typical admitted material may include:

- a human-readable deprecation or sunset record for a documentation surface;
- a migration notice retained for historical inspection;
- a retired documentation copy when the accepted migration explicitly routes that copy here;
- a small local index or metadata record required to keep the deprecation disposition discoverable.

> [!NOTE]
> A deprecated document does **not** automatically move here. The governing transition may require the original path to remain as a read-only tombstone or compatibility alias. Follow the accepted decision and preserve one writable authority.

<a id="4-exclusions--what-does-not"></a>

## What does not belong here

| Do not place here | Owning surface or action |
|---|---|
| Current doctrine, architecture, ADRs, runbooks, standards, or domain guidance | Keep at the current canonical documentation path |
| Active drafts, open intake packets, or unresolved retirement proposals | Keep in the active authoring, intake, issue, or decision surface |
| Historical predecessors retained as long-term supersession context | [`../lineage/`](../lineage/README.md) when the governing disposition selects lineage |
| Closed or withdrawn material that never became current authority | [`../exploratory/`](../exploratory/README.md) |
| Semantic contracts, machine schemas, or policy source | `contracts/`, `schemas/`, or `policy/`, with their own version and supersession rules |
| Data instances, source descriptors, evidence, receipts, proofs, catalogs, or published carriers | Their governed `data/` family |
| Release manifests, promotion decisions, correction notices, withdrawal notices, or rollback cards | `release/` |
| A second writable copy of current documentation | Preserve one writer; use a governed alias, tombstone, or archive record only when authorized |
| Secrets, personal data, restricted content, or unsafe exact locations | Do not commit; use the applicable protected system and policy path |

Age, inactivity, broken links, or a contributor's belief that something is obsolete are evidence to investigate, not deprecation authority.

<a id="5-directory-layout"></a>

## Direct-child map

The current tree is verified from repository evidence and intentionally stops at direct children.

```text
docs/archive/deprecated/
└── README.md                  # this boundary contract; no deprecated entries currently present
```

A future child may be added only through a supported deprecation or retirement transition. This README does not reserve a speculative naming scheme or authorize date-named subtrees.

<a id="6-lifecycle-register--deprecated--sunset"></a>
<a id="9-authoring-workflow"></a>

## Deprecation transition

Use the smallest transition that preserves identity, compatibility, and rollback:

1. **Classify the event.** Distinguish planned deprecation from correction, withdrawal, supersession, rollback, exploratory closure, or simple editorial cleanup.
2. **Freeze identity and authority.** Record the exact path, document ID, governing decision, current writer, known consumers, and relevant digests or blobs.
3. **Choose compatibility treatment.** Decide whether the original path remains as a tombstone/alias, stays in place with a notice, receives an archive record, or has an explicitly authorized retained copy here.
4. **Define successor and timing.** Record the successor or no-successor rationale, effective date, sunset/review checkpoint, migration obligations, and unresolved risks.
5. **Update direct dependencies.** Repair links, fragments, navigation, metadata, and registers only when they are verified parts of the transition closure.
6. **Validate and review.** Run changed-document checks and any authority-specific migration, compatibility, security, or release validation.
7. **Close deliberately.** At the review or sunset checkpoint, retain lineage, extend the transition, remove the bounded archive object, or apply a forward fix through a reviewed change. A date never deletes content automatically.

Finite outcomes:

| Outcome | Meaning |
|---|---|
| `PLACE` | The exact documentation identity, governing disposition, lane selection, compatibility, retention, and review path are supported. |
| `HOLD` | A required decision, successor, consumer inventory, timing, sensitivity review, or rollback/forward-fix path is missing. |
| `REJECT` | The artifact is still current, belongs to another authority root/lane, would create a parallel writer, or cannot be retained safely. |
| `ERROR` | The transition or its validation could not complete safely. |

<a id="8-conventions"></a>
<a id="7-the-sunset-clock"></a>

## Entry requirements and timing

Before a child artifact is added, the governing transition must provide enough evidence to establish:

- exact archived or affected path and stable document identity;
- disposition type and governing ADR, migration, deprecation, or retirement record;
- predecessor/successor relationship, or a reviewed no-successor rationale;
- effective date and any sunset or next-review checkpoint;
- stable-path, alias, tombstone, link, and known-consumer treatment;
- exposure and sensitivity posture;
- mutation rule and permitted corrections;
- retention, deletion, rollback, or forward-fix method;
- verified owner/review route.

When the proposed [`deprecation_register.yaml`](../../../control_plane/deprecation_register.yaml) is used, the documentation record should cross-link the exact register entry. Do not fabricate a register key or treat the proposed register as independent authority.

| Timing state | Required posture |
|---|---|
| Before the effective date | Preserve current behavior and provide the announced migration/compatibility path. |
| During the deprecation window | Keep the disposition visible, current, and non-authoritative; monitor known consumers and corrections. |
| At the sunset/review checkpoint | Re-evaluate evidence and choose a reviewed disposition; do not rely on the date alone. |
| Past the checkpoint without closure | Return `HOLD`, record drift or a forward-fix task, and preserve compatibility until the unresolved risk is addressed. |

<a id="inputs-outputs-exposure-mutation-and-retention"></a>

## Inputs, outputs, exposure, mutation, and retention

### Inputs

- current documentation bytes, document ID, path, and authority state;
- accepted ADRs and reviewed deprecation, retirement, or migration records;
- successor/no-successor rationale and effective timing;
- current link, fragment, producer, consumer, and navigation evidence;
- rights, sensitivity, and exposure decisions when retention could reveal protected material;
- rollback or forward-fix plan.

### Outputs

- a read-only deprecation/sunset/migration record or an explicitly authorized retained documentation copy;
- bounded metadata and predecessor/successor links;
- repaired direct navigation or compatibility references where required;
- review evidence from documentation and transition-specific checks.

The output is historical documentation. It is not a `PolicyDecision`, `EvidenceBundle`, receipt, proof, release object, or publication record.

### Exposure, mutation, and retention

| Surface | Rule |
|---|---|
| This README | Versioned local boundary contract; update when the lane's responsibility, direct children, validation, or review route changes |
| Child record or retained copy | Read-only after closure except for explicit metadata correction, successor link, correction note, or reviewed timing change |
| Public exposure | Repository-facing/public only when rights and sensitivity permit; otherwise deny retention here or use an approved public-safe representation |
| Physical storage | Tracked Git content unless an accepted transition establishes another governed store |
| Retention | Keep while needed for compatibility, deprecation visibility, auditability, correction, or lineage; deletion is the final reviewed step after exact identity and consumer checks |
| Rollback | Before merge, close the PR and abandon its branch. After merge, revert the focused commit or apply a reviewed forward fix without recreating two writable authorities. |

<a id="10-validation"></a>
<a id="13-last-reviewed"></a>

## Validation, ownership, and review

### Repository-native checks

Run the smallest current check set that covers this README:

```bash
python tools/validators/docs/meta-block/check_meta_blocks.py \
  --repo-root . \
  --profile present \
  --registry control_plane/document_registry.yaml \
  --format text \
  docs/archive/deprecated/README.md

python tools/validators/docs/link-check/check_links.py \
  --repo-root . \
  --format text \
  docs/archive/deprecated/README.md
```

The repository's bounded documentation workflows may run these checks for changed Markdown. A passing check is QA evidence only; it does not adopt a deprecation decision, authorize removal, or prove publication.

### Negative checks

Hold or reject a change that would:

- move or delete a current document without the required authority and compatibility evidence;
- make deprecated prose appear current or authoritative;
- create a second writable doctrine, contract, schema, policy, evidence, registry, release, receipt, or proof home;
- use a proposed register entry or sunset date as automatic deletion authority;
- break a known stable path, anchor, successor link, or consumer without bounded compatibility;
- conceal uncertainty, a failed check, correction lineage, or unresolved sensitivity;
- retain secrets, private information, restricted source material, or harmful precision.

### Ownership and escalation

[`CODEOWNERS`](../../../.github/CODEOWNERS) routes the default review to `@bartytime4life`. Additional review is required from the affected authority owner when a change alters doctrine lineage, an accepted decision, security or sensitivity posture, a public path, or a structural migration.

Escalate instead of guessing when the change would create the first lane entry without an accepted disposition, remove a stable externally consumed path, choose between withdrawal and deprecation, or change exposure of protected information.

### Last evidence review and triggers

| Field | Value |
|---|---|
| Review date | `2026-08-17` |
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Reviewed base | `main@5af5f730d8d7c732b7321fee6d80221f3e511f40` |
| Target prior blob | `6b2c157c9d5d52306749f91d262806b361d915a7` |
| Current direct children | `README.md` only |
| Machine companion | `control_plane/deprecation_register.yaml` — `PROPOSED`, `entries: []` |
| Placement authority | Accepted ADR-0029 and adopted `docs/doctrine/directory-rules.md` |

Re-review this boundary when:

- Directory Rules, ADR-0029, the parent archive contract, or the deprecation process changes materially;
- a child is added, removed, renamed, or changes responsibility;
- the deprecation register gains an accepted schema or active entry relevant to this lane;
- validation or CODEOWNERS coverage changes;
- a sunset, correction, withdrawal, sensitive-data event, broken link, or rollback affects retained material;
- evidence shows the README conflicts with current repository behavior or a governing transition.

<a id="11-faq"></a>

## Common decisions

### Does every deprecated document move here?

No. The governing transition may keep the original path as a read-only tombstone or alias, retain the document in place with a notice, create only a deprecation record here, or explicitly route a retained copy here. Preserve one writable authority and follow the accepted decision.

### Is a sunset date enough to delete something?

No. A date triggers review. Deletion still requires exact identity, known-consumer and link checks, applicable rights/sensitivity review, and a credible rollback or forward-fix path.

### What is the difference between `deprecated/` and `lineage/`?

`deprecated/` carries an active or retained deprecation/retirement disposition. `lineage/` preserves long-term predecessor and supersession context. A reviewed transition may eventually retain a deprecation record as lineage, but the lanes are not interchangeable.

### What is the difference between deprecation and withdrawal?

Deprecation is a planned compatibility transition. Withdrawal is immediate containment for rights, sensitivity, or integrity risk. Do not use a deprecation window to delay required containment.

### How is deprecated material restored?

Create a new current artifact or reviewed migration that cites the deprecated material as historical context, then pass normal placement, evidence, policy, validation, and review gates. Do not silently turn the archived body back into current authority.

<a id="12-related-docs"></a>

## Related authorities

| Surface | Relationship |
|---|---|
| [`docs/archive/README.md`](../README.md) | Parent archive routing, non-authority posture, admission, retention, and rollback boundary |
| [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md) | Adopted placement, README-profile, compatibility, migration, and rollback law |
| [`ADR-0029`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Accepted decision adopting the exact Directory Rules v2 bytes |
| [`DEPRECATION_PROCESS.md`](../../governance/DEPRECATION_PROCESS.md) | Draft whole-system deprecation guidance; not independent accepted authority |
| [`corrections-first-class.md`](../../doctrine/corrections-first-class.md) | Distinguishes correction and withdrawal from planned deprecation |
| [`control_plane/deprecation_register.yaml`](../../../control_plane/deprecation_register.yaml) | Proposed machine companion; currently contains no entries |
| [`lineage/README.md`](../lineage/README.md) | Long-term documentation lineage and supersession context |
| [`exploratory/README.md`](../exploratory/README.md) | Closed or withdrawn material that never became current authority |
| [`meta-block` validator](../../../tools/validators/docs/meta-block/check_meta_blocks.py) | Deterministic bounded metadata QA |
| [`link-check` validator](../../../tools/validators/docs/link-check/check_links.py) | Deterministic no-network local Markdown link and fragment QA |

## Status

**CONFIRMED:** same-path modernization; current lane and direct-child state; accepted Directory Rules v2 authority; parent archive contract; default CODEOWNERS route; proposed empty deprecation register; repository-native metadata and link-check validators.

**NEEDS VERIFICATION:** accepted whole-system deprecation-process authority, future child entries and schemas, external consumers, dedicated archive-entry validation, and any later move, deletion, or structural migration.

[Back to top](#top)

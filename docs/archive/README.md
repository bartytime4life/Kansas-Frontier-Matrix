<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-archive-readme
title: docs/archive — Historical Documentation Boundary
type: README
version: v1.0
status: active
owners:
  - "@bartytime4life"
created: 2026-05-10
updated: 2026-08-17
policy_label: repository-facing
owning_root: docs/
responsibility: "Define the docs/archive boundary, child-lane routing, archive admission rules, non-authority posture, validation, retention, and review triggers."
truth_posture: "CONFIRMED current repository and accepted Directory Rules evidence / NEEDS VERIFICATION child-lane modernization, exhaustive archive-entry inventory, and external consumers"
related:
  - docs/README.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/archive/lineage/README.md
  - docs/archive/exploratory/README.md
  - docs/archive/deprecated/README.md
  - docs/registers/CANONICAL_LINEAGE_EXPLORATORY.md
  - control_plane/root_registry.yaml
  - control_plane/deprecation_register.yaml
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# docs/archive

`docs/archive/` is KFM's bounded human-documentation archive. It preserves historical and non-current material so readers can inspect lineage without confusing retained content with current authority.

> [!IMPORTANT]
> **Archived does not mean authoritative.** Nothing under `docs/archive/` becomes current doctrine, an accepted decision, implementation proof, evidence, policy, release state, or publication authority merely because it is retained here. Resolve current claims through canonical documentation, accepted ADRs, current repository evidence, and the owning trust surfaces.

## Quick navigation

- [Status, authority, and scope](#status-authority-and-scope)
- [Direct-child map](#direct-child-map)
- [What belongs here](#what-belongs-here)
- [What does not belong here](#what-does-not-belong-here)
- [Archive admission workflow](#archive-admission-workflow)
- [Inputs, outputs, mutability, and retention](#inputs-outputs-mutability-and-retention)
- [Validation, ownership, and review](#validation-ownership-and-review)
- [Common decisions](#common-decisions)
- [Related authorities](#related-authorities)

<!-- Legacy inbound anchor aliases retained from the previous README. -->
<a id="0-status--authority"></a>
<a id="1-purpose"></a>
<a id="2-authority-level"></a>
<a id="3-status"></a>
<a id="4-repo-fit"></a>

## Status, authority, and scope

| Field | Current boundary |
|---|---|
| Path | `docs/archive/` — **CONFIRMED present** on the reviewed `main` snapshot |
| Owning root | [`docs/`](../README.md), the canonical human-readable governance and explanation root |
| Placement outcome | `PLACE` — same-path modernization of an existing boundary README; no move, rename, new lane, or authority change |
| README profile | `BOUNDARY_COMPACT` under the adopted Directory Rules v2 |
| Primary responsibility | Route retained human documentation into the correct archive child lane and explain its non-current authority posture |
| Authority limit | Historical context and lineage only; never the writable source of current doctrine, contracts, schemas, policy, evidence, release, or runtime behavior |
| Exposure | Repository-facing and potentially public; sensitive or restricted material remains denied unless a governing review explicitly permits a public-safe representation |
| Review route | `@bartytime4life` through the repository's default CODEOWNERS rule; additional review depends on the affected authority boundary |

This directory sits inside `docs/`; it is not part of KFM's data lifecycle. Archiving a document does not perform `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLETS -> PUBLISHED`, approve a release, or change a public system.

**CONFIRMED:** the directory and its three child lanes exist in the reviewed repository state.

**NEEDS VERIFICATION:** exhaustive archive-entry classification, every inbound or external consumer, and modernization of the child-lane READMEs are outside this one-file change.

<a id="6-subfolders"></a>
<a id="7-directory-tree"></a>

## Direct-child map

The current tree below is verified from repository evidence and intentionally stops at direct children. Each child README owns deeper detail.

```text
docs/archive/
├── README.md                  # this boundary contract
├── deprecated/               # explicitly deprecated documentation dispositions
├── exploratory/              # closed or withdrawn material that never became current authority
└── lineage/                  # retained historical lineage and supersession context
```

| Child lane | Bounded role | Local contract |
|---|---|---|
| `lineage/` | Historical predecessors, supersession context, and documentation-lineage records retained for traceability | [`lineage/README.md`](lineage/README.md) |
| `exploratory/` | Closed, withdrawn, or never-promoted human documentation retained as design history rather than canon | [`exploratory/README.md`](exploratory/README.md) |
| `deprecated/` | Documentation governed by an explicit deprecation, migration, sunset, or retirement disposition | [`deprecated/README.md`](deprecated/README.md) |

A child path is selected by the artifact's verified disposition, not by age, filename, topic, or convenience.

<a id="8-what-belongs-here"></a>

## What belongs here

A human-readable artifact belongs under `docs/archive/` only when all applicable conditions are satisfied:

1. Its primary responsibility is documentation, not executable behavior or a trust-object instance.
2. It is no longer the current writable authority for the claim or decision it once carried, or it never became current authority.
3. Its disposition is explicit: lineage, exploratory closure, or deprecation/retirement.
4. The governing decision, closure record, migration record, successor link, or deprecation entry is available at the level required by the change.
5. Retention does not expose secrets, private data, restricted source material, protected precise locations, or unresolved rights and sensitivity.

Typical admitted material includes:

- retained documentation predecessors when an accepted migration or supersession decision requires an archive copy or record;
- historical architecture, domain, standards, runbook, or ADR context that remains useful but is no longer current authority;
- closed exploratory packets and withdrawn proposals that did not become canon;
- documentation under an explicit deprecation or retirement process;
- small indexes, metadata, or navigation records required to keep archive lineage inspectable.

> [!NOTE]
> A predecessor does not automatically move here. Accepted decisions may require an in-place tombstone, retained original path, archive record, or another compatibility treatment. Follow the governing migration rather than applying a blanket move rule.

<a id="9-what-does-not-belong-here"></a>
<a id="16-anti-patterns"></a>

## What does not belong here

| Do not place here | Owning surface or action |
|---|---|
| Current doctrine, architecture, ADRs, runbooks, standards, or domain guidance | Keep at the current canonical documentation path |
| Active drafts, open intake packets, or work still seeking a decision | Keep in the current authoring or intake surface |
| Semantic contracts, machine schemas, or policy source | `contracts/`, `schemas/`, or `policy/` |
| Source descriptors, data instances, evidence, receipts, proofs, catalogs, or published carriers | Their governed `data/` family |
| Release manifests, promotion decisions, correction notices, withdrawal notices, or rollback cards | `release/` |
| Generated previews, lint output, coverage, or temporary QA artifacts | External CI artifacts or the governed generated-output lane |
| Secrets, credentials, private endpoints, personal data, restricted source content, or unsafe precise locations | Do not commit; use the applicable protected system and policy path |
| A second writable copy of any current authority | Keep one writer; use an alias, tombstone, or archive record only when a governing migration permits it |

Age alone is never an archive admission criterion. "Old," "stale-looking," "unused," and "probably replaced" are findings to verify, not dispositions.

<a id="5-the-supersession-rule"></a>
<a id="10-lifecycle-how-things-arrive"></a>
<a id="13-conventions"></a>
<a id="22-worked-example--one-supersession-end-to-end"></a>

## Archive admission workflow

1. **Resolve current authority.** Identify the current document, exact path, stable identity, status, and any accepted ADR or governing register.
2. **Classify the disposition.** Select `lineage/`, `exploratory/`, or `deprecated/`; return `HOLD` when the disposition or authority is unresolved.
3. **Confirm the transition record.** Verify the successor, closure reason, migration/deprecation record, effective date, and rollback or forward-fix path required by significance.
4. **Preserve compatibility.** Inventory links and anchors; keep object identity stable; use an in-place tombstone, bounded alias, or archive record when the accepted decision requires it. Do not create dual writers.
5. **Update the connected documentation closure.** Repair successor/predecessor links, indexes, metadata, registers, and navigation only when they are verified direct dependencies of the transition.
6. **Validate and review.** Run the changed-document metadata and local-link checks, inspect the rendered GFM, and stop at a reviewable branch or pull request.

Finite outcomes:

| Outcome | Meaning |
|---|---|
| `PLACE` | The disposition, child lane, authority basis, links, and retention posture are sufficiently supported. |
| `HOLD` | A required decision, successor, owner, rights/sensitivity review, consumer inventory, or migration record is missing. |
| `REJECT` | The artifact belongs to another authority root, is still current, would create a parallel writer, or cannot be retained safely. |
| `ERROR` | The archive operation or validation could not complete safely. |

Archiving is a documentation-state operation only. It does not promote, publish, release, deploy, or approve the archived content.

<a id="11-inputs"></a>
<a id="12-outputs"></a>

## Inputs, outputs, mutability, and retention

### Inputs

- current documentation bytes and stable identity;
- accepted ADRs, supersession or retirement decisions, migration manifests, and closure records;
- current link, fragment, consumer, and navigation evidence;
- rights, sensitivity, and exposure decisions when retention could reveal protected material;
- current archive-child contracts and relevant machine projections.

### Outputs

- a retained human-readable archive artifact, lineage record, tombstone, or archive navigation update;
- repaired predecessor/successor references and bounded metadata where directly required;
- review evidence from metadata, link, and documentation checks.

Archive output is historical documentation. It is not a `PolicyDecision`, `EvidenceBundle`, receipt, proof, release object, or publication record.

### Mutability and retention

| Surface | Rule |
|---|---|
| This README | Versioned boundary contract; updated when archive responsibilities or direct children change |
| Archived body | Read-mostly after closure; preserve original meaning and use a correction note, addendum, successor, or new intake artifact instead of silently rewriting history |
| Archive metadata and indexes | Versioned updates are permitted when they improve identity, navigation, correction, or successor links without changing the historical claim |
| Physical storage | Tracked Git content unless a child contract and accepted decision establish another governed store |
| Retention | Durable while needed for lineage, compatibility, auditability, or correction; deletion is the final step after exact identity, consumer, link, sensitivity, and rollback review |
| Rollback | Before merge, close the draft PR and delete or abandon its branch. After merge, revert the focused commit or apply a reviewed forward fix; do not recreate two writable authorities. |

<a id="14-validation"></a>
<a id="15-review-burden"></a>
<a id="18-adrs"></a>
<a id="20-open-questions"></a>
<a id="21-last-reviewed"></a>

## Validation, ownership, and review

### Repository-native checks

Run the smallest check set that covers the changed document:

```bash
python tools/validators/docs/meta-block/check_meta_blocks.py \
  --repo-root . \
  --profile present \
  --registry control_plane/document_registry.yaml \
  --format text \
  docs/archive/README.md

python tools/validators/docs/link-check/check_links.py \
  --repo-root . \
  --format text \
  docs/archive/README.md
```

The pull request also triggers the bounded [`docs-meta-block`](../../.github/workflows/docs-meta-block.yml) and [`link-check`](../../.github/workflows/link-check.yml) workflows for changed Markdown. A green documentation check is QA evidence only; it is not adoption, implementation, release, deployment, or publication authority.

### Negative checks

Hold or reject a change that would:

- make archived prose appear current or authoritative;
- move or delete a document without the required authority, consumer review, and rollback path;
- create a second writable doctrine, contract, schema, policy, evidence, registry, release, receipt, or proof home;
- break a known stable anchor or successor/predecessor link without compatibility handling;
- conceal uncertainty, deprecation state, correction lineage, or a failed validation;
- expose secrets, private information, restricted material, or harmful precision.

### Ownership and escalation

[`CODEOWNERS`](../../.github/CODEOWNERS) routes the default repository review to `@bartytime4life`. Archive changes also require the owning subsystem or authority reviewer when they alter doctrine lineage, accepted decisions, security or sensitivity posture, public navigation, or a structural migration.

Escalate instead of guessing when the change would create or retire a child lane, amend the archive's responsibility, contradict an accepted ADR, remove an externally consumed path, or change a sensitive exposure decision.

### Last evidence review and triggers

| Field | Value |
|---|---|
| Review date | `2026-08-17` |
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Reviewed base | `main@1f1387a9478528e38be0f4ecca8f14dda3c1b962` |
| Target prior blob | `2a28377b0789974903f98fbd520fc6649f5e56e9` |
| Current direct children | `deprecated/`, `exploratory/`, `lineage/` |
| Placement authority | Accepted ADR-0029 and adopted `docs/doctrine/directory-rules.md` |

Re-review this boundary when:

- Directory Rules or ADR-0029 is superseded;
- the archive gains, loses, renames, or changes the responsibility of a direct child;
- deprecation, compatibility, alias, retention, or deletion policy changes;
- CODEOWNERS or documentation validation coverage changes materially;
- a broken link, correction, withdrawal, sensitive-data incident, or rollback affects archived documentation;
- evidence shows this README conflicts with a child-lane contract or current repository behavior.

<a id="19-faq"></a>

## Common decisions

### Is every old document an archive candidate?

No. Age is not a disposition. A document stays current until evidence and an authorized transition establish otherwise.

### May current documentation cite an archived file?

Yes, for historical context or lineage, with an explicit indication that the target is archived and a link to the current successor or authority when one exists. An archived citation must not carry a current claim by itself.

### How is archived material revived?

Create a new current artifact or intake entry that cites the archived source as lineage, then pass the normal evidence, governance, review, and placement process. Do not silently rewrite the archived body into current canon.

<a id="17-related-folders"></a>

## Related authorities

| Surface | Relationship |
|---|---|
| [`docs/README.md`](../README.md) | Parent human-documentation authority boundary |
| [`docs/doctrine/directory-rules.md`](../doctrine/directory-rules.md) | Adopted placement and README-profile law |
| [`ADR-0029`](../adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Accepted decision adopting Directory Rules v2 and its migration discipline |
| [`control_plane/root_registry.yaml`](../../control_plane/root_registry.yaml) | Machine projection classifying `docs/` as the human-document root; not independent authority |
| [`control_plane/deprecation_register.yaml`](../../control_plane/deprecation_register.yaml) | Proposed machine tracker for deprecated paths and sunset metadata |
| [`CANONICAL_LINEAGE_EXPLORATORY.md`](../registers/CANONICAL_LINEAGE_EXPLORATORY.md) | Proposed human register for exploratory lineage candidates |
| [`meta-block` validator](../../tools/validators/docs/meta-block/README.md) | Bounded metadata QA and review-only registry delta |
| [`link-check` validator](../../tools/validators/docs/link-check/README.md) | Deterministic no-network local Markdown target and fragment QA |

## Status

**CONFIRMED:** same-path modernization; current directory and child-lane presence; accepted Directory Rules v2 authority; default CODEOWNERS route; repository-native metadata and link-check workflows.

**NEEDS VERIFICATION:** child README modernization, exhaustive archive contents, external consumers, and any future move, deletion, or structural migration not explicitly authorized by an accepted decision.

[Back to top](#top)

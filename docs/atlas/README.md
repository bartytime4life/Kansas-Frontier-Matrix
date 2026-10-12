<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-atlas-readme
title: docs/atlas/ — Legacy Atlas Compatibility Lane
type: directory-readme; compatibility-lane; repository-evidence; navigation
version: v2.0
status: draft; repository-grounded; noncanonical; compatibility; pointer-only; migration-hold; non-release; non-publication
owner: "@bartytime4life via CODEOWNERS; independent documentation, atlas, migration, and consumer stewardship NEEDS VERIFICATION"
created: 2026-05-25
updated: 2026-08-22
policy_label: repository-public; documentation; compatibility; atlas; cite-or-abstain
owning_root: docs/
responsibility: >-
  Preserve the repository-present singular atlas lane as a bounded compatibility
  and navigation surface, inventory its direct children, direct readers to the
  canonical docs/atlases lane and current responsibility owners, and expose
  migration, consumer, alias, deprecation, and correction gaps without creating
  parallel atlas authority or authorizing path retirement.
authority: >-
  Human-readable compatibility orientation only. Curated atlas synthesis belongs
  under docs/atlases/; doctrine and accepted ADRs govern placement; contracts,
  schemas, policy, evidence, lifecycle records, release decisions, corrections,
  rollback, deployment, and publication remain with their owning roots and
  accountable authorities.
current_path: docs/atlas/README.md
canonical_relationship: >-
  Accepted Directory Rules v2 makes docs/atlases/ the canonical curated atlas
  lane. docs/atlas/ remains a repository-present singular compatibility lane,
  but no current path-alias entry, deprecation-register entry, accepted
  lane-specific migration decision, verified sunset date, or complete consumer
  closure was found at the evidence snapshot. Same-path maintenance is PLACE;
  migration, mirroring, tombstoning, or deletion remains HOLD.
truth_posture: >-
  CONFIRMED current main, target bytes, the three direct Markdown children,
  accepted ADR-0029 and Directory Rules v2, the canonical docs/atlases lane,
  the exact canonical source-role extract, the absence of a standalone
  docs/atlases/master-api-surface.md carrier, the empty deprecation register,
  and the absence of a docs/atlas mapping from the active path-alias register /
  LINEAGE the v1 claim that a 30-day migration clock and ADR-S-02 already
  governed this lane / PROPOSED a future finite compatibility classification,
  alias record, migration packet, consumer-closure record, sunset, tombstone,
  and retirement / UNKNOWN external consumers, deployed documentation links,
  independent steward assignments, and final carrier convergence / NEEDS
  VERIFICATION every structural or retirement action beyond this same-path
  documentation correction.
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  inspected_commit: 43792be16c693d7e4ce9da8afe5514da87440e0d
  target_prior_blob: 9b4330985fc790e0a0c777300ba7e5ae780472c6
  atlas_tree_direct_files: 3
  master_api_pointer_blob: 7d075b36e4e0ad0ae0a4ffb8b35cd7de6576c91c
  source_role_pointer_blob: 6291485a7a454eed9e4ec9d91630e5d6a107ed68
  canonical_atlases_readme_blob: 5dd756497b9eb20b4ffa55cd2cfadcd77ee2f3b4
  canonical_source_role_extract_blob: 4da701f70dda7acd2ca3584b25cdc6e1f9d93dc7
  deprecation_register_blob: 1fb7219dcdb7a437e38fa8ca92ba34e29667d3fa
  path_alias_register_blob: 6ad6840bd47eb8b176d03f9e946c16453fc4caee
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  adr_0029_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  docs_root_readme_blob: 1f8bac189dac1d01c1185e8b4fb8e25efd11d09f
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
inspection_boundary: >-
  Current-session GitHub reads covered current main, the complete target, both
  direct child pointers, the direct singular-lane tree, the canonical atlas-lane
  README and direct tree, accepted Directory Rules and ADR-0029, the docs root,
  CODEOWNERS, deprecation and path-alias registers, exact target-path probes,
  repository search for singular-lane references, and open pull-request and
  task-branch overlap. No mounted checkout, external-consumer inventory,
  documentation deployment, alias resolver, migration operator, release
  process, or public endpoint was exercised.
related:
  - ../README.md
  - ../atlases/README.md
  - ../atlases/source-role-anti-collapse.md
  - ./master-api-surface.md
  - ./source-role-anti-collapse.md
  - ../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../doctrine/directory-rules.md
  - ../registers/DRIFT_REGISTER.md
  - ../../control_plane/deprecation_register.yaml
  - ../../control_plane/path_alias_register.yaml
  - ../../data/receipts/generated/README.md
  - ../../schemas/contracts/v1/receipts/generated_receipt.schema.json
  - ../../.github/CODEOWNERS
tags:
  - kfm
  - docs
  - atlas
  - atlases
  - compatibility
  - pointer
  - migration-hold
  - repository-grounded
  - cite-or-abstain
notes:
  - "v2.0 replaces corpus-only deprecation assertions with current repository evidence while preserving the path and legacy section anchors."
  - "The canonical atlas lane is docs/atlases/; this singular lane is not a second writable atlas authority."
  - "No verified 30-day sunset is active: the deprecation register has no entries and the active path-alias register does not map docs/atlas/."
  - "Both direct child pointers are repository-grounded; the source-role pointer has an exact canonical atlas target, while the master API pointer has no standalone one-to-one atlas target."
  - "No path is moved, mirrored, tombstoned, deleted, released, deployed, promoted, or published by this document."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>
<a id="docsatlas--deprecated-compatibility-mirror"></a>

# `docs/atlas/` — Legacy Atlas Compatibility Lane

> **Purpose.** Preserve legacy singular-lane links and route readers to the
> repository surfaces that currently own atlas navigation, substantive reference
> material, API implementation, and other responsibilities—without allowing
> `docs/atlas/` to become a second atlas authority.

| Signal | Current bounded state |
|---|---|
| Canonical atlas lane | [`docs/atlases/`](../atlases/) |
| This lane | Repository-present compatibility and navigation surface |
| Formal compatibility class | `NEEDS VERIFICATION` |
| Direct children | Three Markdown files, including this README |
| New substantive atlas content | `DENY` |
| Migration or deletion | `HOLD` |
| Release or publication effect | None |

> [!IMPORTANT]
> **The singular lane is not canonical.** Accepted Directory Rules v2 places
> curated atlas collections under [`docs/atlases/`](../atlases/). Files here may
> preserve compatibility and direct readers elsewhere; they may not create a
> parallel atlas, API, contract, schema, policy, evidence, release, or
> publication authority.

> [!WARNING]
> **No verified 30-day sunset clock is active.** The current
> [`deprecation_register.yaml`](../../control_plane/deprecation_register.yaml)
> contains no entries, the active
> [`path_alias_register.yaml`](../../control_plane/path_alias_register.yaml)
> contains no `docs/atlas/` mapping, and the exact `ADR-S-02` path named by v1
> is not present at the evidence snapshot. The old timer and ADR wording are
> retained as `LINEAGE`, not current control state.

> [!CAUTION]
> **Do not infer that this lane can now be removed.** Repository search still
> finds singular-lane references, external consumers are unknown, and no
> accepted migration packet, link-parity proof, retirement receipt, or rollback
> record was verified. Structural convergence remains `HOLD`.

> [!NOTE]
> **Current direct children have different redirect semantics.**
> [`source-role-anti-collapse.md`](./source-role-anti-collapse.md) has an exact
> canonical atlas target and a current responsibility map. [`master-api-surface.md`](./master-api-surface.md)
> does not; it routes readers across the canonical atlas lane, Governed API,
> contracts, schemas, validators, and tests by responsibility.

**Quick navigation:** [Status](#1-purpose) · [Placement](#2-why-this-folder-is-deprecated) ·
[Inventory](#3-authority-level) · [Authority](#4-status) ·
[Permitted content](#5-what-belongs-here) ·
[Prohibited content](#6-what-does-not-belong-here) ·
[Inputs](#7-inputs) · [Outputs](#8-outputs) ·
[Redirect map](#9-migration-map) · [Validation](#10-validation) ·
[Review](#11-review-burden) · [Related surfaces](#12-related-folders) ·
[Decisions](#13-adrs-and-open-dr-references) ·
[Open work](#14-verification-checklist) · [Rollback](#15-rollback) ·
[History](#16-last-reviewed)

---

<a id="1-purpose"></a>

## 1. Status and evidence boundary

| Question | Current repository-grounded answer | Truth label |
|---|---|---|
| Does `docs/atlas/` exist? | Yes. The direct tree contains `README.md`, `master-api-surface.md`, and `source-role-anti-collapse.md`. | `CONFIRMED` |
| Is this the canonical atlas lane? | No. Accepted Directory Rules v2 identifies `docs/atlases/` as the curated atlas lane. | `CONFIRMED` |
| Is this lane a verified mirror? | No one-way generator, synchronization rule, parity artifact, or alias-register entry was verified. | `UNKNOWN`; do not call it a mirror |
| Is this lane formally deprecated in the machine register? | No. `control_plane/deprecation_register.yaml` currently has `entries: []`. | `CONFIRMED` |
| Is a 30-day sunset active? | No accepted start date, sunset date, or deprecation entry was found. | `CONFIRMED` absence at snapshot; activation `NEEDS VERIFICATION` |
| Does `ADR-S-02-docs-dossiers-vs-docs-atlases.md` exist at the old exact path? | No. The exact repository lookup returned no file. | `CONFIRMED` absence at snapshot |
| Does the active alias register map `docs/atlas/`? | No. Its current alias inventory covers the Directory Rules legacy architecture path only. | `CONFIRMED` |
| Does a canonical source-role extract exist? | Yes: [`docs/atlases/source-role-anti-collapse.md`](../atlases/source-role-anti-collapse.md). | `CONFIRMED` |
| Does a standalone canonical `master-api-surface.md` atlas file exist? | No exact `docs/atlases/master-api-surface.md` file was present. | `CONFIRMED` absence at snapshot |
| Are all consumers closed? | No external inventory or zero-consumer proof was verified; repository references remain. | `UNKNOWN` / `HOLD` |
| Does this README change runtime or public state? | No. | `CONFIRMED` |

### Truth labels used here

| Label | Meaning |
|---|---|
| `CONFIRMED` | Verified from current-session repository bytes or remote state. |
| `PROPOSED` | A future placement, compatibility, migration, or implementation choice not accepted or proved. |
| `UNKNOWN` | Available evidence does not establish the claim. |
| `NEEDS VERIFICATION` | A concrete repository, consumer, reviewer, or migration check remains. |
| `LINEAGE` | Earlier wording or design retained for history, not current authority. |
| `HOLD` | Proceeding would cross unresolved ownership, consumer, validation, correction, or rollback boundaries. |
| `DENY` | The proposed use would create parallel authority or violate the lane boundary. |

Repository presence proves that these files exist. It does not prove formal
compatibility classification, active deprecation, external-consumer closure,
deployment, release, or publication.

[Back to top](#top)

---

<a id="2-why-this-folder-is-deprecated"></a>

## 2. Purpose and canonical relationship

### This lane owns

- the stable legacy directory URL `docs/atlas/`;
- navigation for the direct compatibility documents currently stored here;
- current evidence about the lane's limited role;
- an explicit prohibition on new substantive atlas content;
- migration, consumer, validation, correction, and rollback questions that must
  close before structural action.

### This lane does not own

- an atlas edition, atlas register, or master reference body;
- the canonical atlas-lane index;
- API architecture or executable route registration;
- semantic contracts, machine schemas, or policy;
- source admission, evidence resolution, or lifecycle records;
- release, correction, withdrawal, rollback, deployment, or publication.

### Directory Rules decision

Accepted [`ADR-0029`](../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
adopts the exact Directory Rules v2 bytes at
[`docs/doctrine/directory-rules.md`](../doctrine/directory-rules.md).
Those rules make `docs/` the human-readable explanation root and
`docs/atlases/` its curated atlas lane.

| Proposed action | Finite placement outcome | Basis |
|---|---|---|
| Correct this README in place | `PLACE` | Existing human compatibility boundary; no authority or lifecycle change |
| Maintain an existing pointer in place | `PLACE`, bounded | Compatibility and consumer preservation only |
| Add a new atlas, register, dossier, or master matrix here | `DENY` | Would create a second writable atlas authority |
| Call this lane a generated mirror without a generator and parity proof | `DENY` | A mirror must have one-way production and verification |
| Add a formal alias or deprecation record | `PROPOSED` separate slice | Requires complete identity, consumer, expiry, parity, and rollback fields |
| Move, tombstone, or delete this lane | `HOLD` | Consumer closure, accepted disposition, validation, correction, and rollback are incomplete |

The v1 README collapsed doctrine, proposal, and execution by treating a proposed
migration timer as current state. This edition keeps the canonical relationship
clear while leaving unexecuted structural work visibly unresolved.

[Back to top](#top)

---

<a id="3-authority-level"></a>

## 3. Current direct inventory

The direct tree at the evidence snapshot contains exactly three Markdown files.

| Entry | Current role | Current destination or authority boundary | Status |
|---|---|---|---|
| [`README.md`](./README.md) | Lane boundary and navigation | Canonical lane contract is [`../atlases/README.md`](../atlases/README.md) | Updated in place by this slice |
| [`master-api-surface.md`](./master-api-surface.md) | Repository-grounded compatibility pointer | Routes by responsibility to atlas lineage, Governed API code, runtime contracts/schemas, validation, and review | Current v2.0 pointer; no standalone canonical atlas target |
| [`source-role-anti-collapse.md`](./source-role-anti-collapse.md) | Repository-grounded legacy compatibility pointer | Exact canonical atlas target plus architecture, taxonomy, contract, schema, and governance routing | Current v2.0 pointer; removal remains `HOLD` |

### Child-specific rules

#### `master-api-surface.md`

The pointer must not be rewritten into a route register. The executable API
surface and its semantic/machine boundaries live in their owning roots. Because
no exact `docs/atlases/master-api-surface.md` carrier exists, a one-to-one file
redirect would be false.

#### `source-role-anti-collapse.md`

The exact canonical extract exists, and the current v2.0 pointer now routes
readers to that extract plus the architecture, taxonomy, contract, schema, and
governance surfaces that own narrower responsibilities. This README preserves
that child boundary rather than duplicating its redirect map.

### Inventory drift rule

Whenever a direct child is added, removed, moved, or repurposed, update this
table in the same reviewed change. A pointer cannot become substantive merely
because its canonical target is incomplete or inconvenient.

[Back to top](#top)

---

<a id="4-status"></a>

## 4. Authority and compatibility status

| Dimension | Current bounded posture |
|---|---|
| Owning responsibility root | `docs/` |
| Canonical atlas lane | `docs/atlases/` |
| This lane's formal compatibility class | `NEEDS VERIFICATION` |
| Human authority | Compatibility orientation only |
| Machine alias authority | None for `docs/atlas/` in the active alias register |
| Deprecation authority | None recorded in the current deprecation register |
| Writers | Reviewed repository changes only; no substantive atlas authoring |
| Normal readers | Legacy-link consumers and maintainers resolving old paths |
| Exposure | Repository-public documentation |
| Mutability | Versioned, same-path maintenance |
| Retention | Until accepted consumer-closure and retirement evidence exists |
| Release/publication effect | None |

### Why the formal class remains unresolved

Directory Rules recognizes finite compatibility classes such as `legacy`,
`deprecated`, `mirror`, and `transitional`. Current repository evidence supports
the general conclusion that this is noncanonical compatibility space, but it
does not establish all fields needed to select one class operationally:

- no accepted lane-specific decision reference;
- no machine alias entry;
- no deprecation entry or sunset;
- no synchronization method;
- no complete internal and external consumer inventory;
- no parity or retirement receipt;
- no final rollback record.

Until those facts exist, this README uses **legacy compatibility lane** as a
human description, not a machine-evaluable class claim.

[Back to top](#top)

---

<a id="5-what-belongs-here"></a>

## 5. Permitted content

Only bounded compatibility material belongs in this lane:

1. **This README**, maintained as the current lane boundary.
2. **Existing pointer documents**, maintained only to:
   - preserve a stable legacy path;
   - identify their exact current responsibility owners;
   - route readers without duplicating substantive content;
   - record current evidence, limitations, correction, and rollback.
3. **A future tombstone or redirect body**, but only after an accepted migration
   disposition supplies consumer closure, alias/deprecation records, validation,
   and rollback.
4. **No other content by default.**

A permitted pointer must:

- carry a stable `doc_id` and repository-grounded metadata;
- state that it is non-authoritative;
- identify exact targets that exist, or explicitly describe why no one-to-one
  target exists;
- preserve source-role, truth-status, and implementation boundaries;
- avoid claims of active sunset, migration, aliasing, or parity without machine
  records and validation evidence;
- keep correction and rollback instructions visible.

[Back to top](#top)

---

<a id="6-what-does-not-belong-here"></a>

## 6. Prohibited content

The following must not be added under `docs/atlas/`:

- new atlas editions, domain atlases, master atlases, or consolidated bodies;
- substantive reference registers or master matrices;
- dossiers, encyclopedia chapters, source packets, or research reports;
- ADRs, doctrine, runbooks, security guidance, or drift-register bodies;
- contracts, schemas, policy source, validators, fixtures, or tests;
- source descriptors, EvidenceRefs, EvidenceBundles, or lifecycle instances;
- receipts, proofs, catalogs, manifests, decisions, corrections, or rollback cards;
- generated QA output, rendered site output, or temporary build products;
- copies of content whose writable source is under `docs/atlases/`;
- a new pointer to an unverified target represented as current fact.

### Anti-patterns

| Anti-pattern | Required response |
|---|---|
| “The canonical file is missing, so copy the content here.” | `DENY`; repair or decide the owning lane |
| “This folder is called a mirror, so edit both sides.” | `DENY`; one canonical writer only |
| “The README says 30 days, so delete the path.” | `HOLD`; no active timer or closure evidence exists |
| “A Git move proves migration completed.” | `DENY`; identity, consumers, references, validation, and rollback must close |
| “A green docs check proves the atlas is authoritative.” | `DENY`; documentation validation is bounded QA only |
| “The repository is public, so all atlas material is public-safe.” | `DENY`; rights and sensitivity remain separately governed |

[Back to top](#top)

---

<a id="7-inputs"></a>

## 7. Inputs

This lane may consume only the evidence needed to maintain compatibility
orientation:

- accepted Directory Rules and ADRs;
- the current direct `docs/atlas/` tree;
- the current [`docs/atlases/README.md`](../atlases/README.md) lane contract;
- exact canonical targets and responsibility-owner surfaces;
- repository-internal reference searches and known external-consumer records;
- path-alias, deprecation, drift, and verification registers;
- validation reports and migration evidence;
- Git history and prior blobs for rollback.

Inputs remain evidence, not authority expansion. A historical atlas, proposal,
comment, branch name, or old README cannot by itself activate a migration or
sunset.

[Back to top](#top)

---

<a id="8-outputs"></a>

## 8. Outputs and non-effects

### Outputs

- stable human-readable navigation at the legacy directory URL;
- exact redirects where one-to-one canonical targets exist;
- responsibility-based routing where they do not;
- visible compatibility, migration, and consumer gaps;
- bounded documentation validation evidence;
- a reversible Git history.

### Non-effects

This lane does not emit or authorize:

- source admission or source-role decisions;
- evidence resolution or citation closure;
- policy, rights, sensitivity, or access decisions;
- promotion or lifecycle transitions;
- release, correction, withdrawal, or rollback records;
- API routes, runtime responses, map layers, or AI answers;
- deployment or publication.

A commit, pull request, merge, pointer, alias record, or deprecation record is
repository/governance state only. None is automatically a KFM release or public
knowledge publication.

[Back to top](#top)

---

<a id="9-migration-map"></a>

## 9. Redirect and migration map

| Legacy surface | Current route | Current evidence | Structural disposition |
|---|---|---|---|
| `docs/atlas/README.md` | Stay at this path as the compatibility boundary | Existing tracked file | `PLACE` |
| `docs/atlas/source-role-anti-collapse.md` | [`docs/atlases/source-role-anti-collapse.md`](../atlases/source-role-anti-collapse.md) | Exact canonical target exists | Pointer maintenance `PLACE`; move/delete `HOLD` |
| `docs/atlas/master-api-surface.md` | Follow its responsibility map to atlas lineage, Governed API, contracts, schemas, validator, and tests | No standalone canonical atlas target exists | Keep pointer; carrier creation and deletion `HOLD` |
| `docs/atlas/` as a lane | [`docs/atlases/`](../atlases/) for all new curated atlas content | Canonical relationship accepted through ADR-0029 | Migration/retirement `HOLD` |

### Requirements before structural convergence

A future migration, tombstone, or deletion packet must include:

1. exact old and canonical identities;
2. a finite compatibility class and accepted decision reference;
3. internal and external consumer inventories;
4. canonical target and writer ownership;
5. alias/deprecation register updates;
6. backlink and fragment parity;
7. generated/mirror synchronization rules if applicable;
8. validation reports for links, identity, metadata, and rendering;
9. correction handling for released references, if any;
10. a rollback target and retirement receipt;
11. zero-writer and zero-consumer evidence before physical deletion.

The absence of any required element yields `HOLD`, not an inferred migration.

[Back to top](#top)

---

<a id="10-validation"></a>

## 10. Validation

### Changed-document checks

A same-path README update should verify:

- exactly one `KFM_META_BLOCK_V2` and one H1;
- UTF-8, LF endings, final newline, no tabs, trailing whitespace, or conflict markers;
- unique explicit anchors and closure of same-document fragments;
- preservation of the sixteen legacy section anchors;
- balanced fences and consistent Markdown tables;
- repository-relative link targets against the pinned tree;
- direct-child inventory against the GitHub contents API or a mounted checkout;
- no secrets, restricted payloads, private data, or harmful precision;
- exact artifact hash and generated-receipt binding when AI authors the change.

### Compatibility checks

| Check | Expected result |
|---|---|
| Canonical lane resolves | `docs/atlases/README.md` present |
| Exact source-role target resolves | `docs/atlases/source-role-anti-collapse.md` present |
| Standalone master API target probe | Absent; pointer must not invent it |
| Deprecation-register lookup | No `docs/atlas/` entry at this snapshot |
| Path-alias-register lookup | No `docs/atlas/` alias at this snapshot |
| Exact ADR-S-02 lookup | Absent at this snapshot |
| Open PR and branch overlap | No active same-path writer before this change |
| Base-to-head diff | Only declared documentation and generated receipt paths |

### Negative checks

The change must fail or be held if it:

- adds substantive atlas content to this lane;
- asserts an active deprecation or sunset without a governing record;
- declares a mirror without one-way generation and parity;
- links to a nonexistent target as though it were current;
- drops a known compatibility anchor without migration handling;
- claims consumer closure from repository search alone;
- represents documentation QA as release, deployment, or publication proof.

### Repository-native checks

Where a checkout is available, run the applicable documentation and receipt
validators. Hosted checks remain exact-head evidence and must be reported
separately from authoring validation. A green result proves only the check's
declared scope.

[Back to top](#top)

---

<a id="11-review-burden"></a>

## 11. Ownership and review burden

[`CODEOWNERS`](../../.github/CODEOWNERS) routes repository review to
`@bartytime4life`. That route is not an independent docs-steward assignment,
ReviewRecord, migration approval, release decision, or proof that review
occurred.

| Review concern | Required role or evidence |
|---|---|
| Same-path factual correction | Verified repository evidence plus current CODEOWNERS route |
| Canonical atlas content | Atlas/documentation steward and affected domain reviewers |
| Compatibility classification | Documentation and directory-governance review |
| Alias, deprecation, or sunset | Governance decision, complete register record, and consumer evidence |
| Move, tombstone, or deletion | Migration review, link/identity parity, correction, rollback, and retirement evidence |
| Sensitive atlas material | Domain, rights, sovereignty, privacy, security, or sensitivity reviewers as applicable |
| Public release or publication | Separate accountable release and publication authorities |

Independent documentation, atlas, migration, and consumer stewardship remains
`NEEDS VERIFICATION`.

[Back to top](#top)

---

<a id="12-related-folders"></a>

## 12. Related surfaces

| Surface | Relationship |
|---|---|
| [`../README.md`](../README.md) | Parent `docs/` authority and exposure boundary |
| [`../atlases/README.md`](../atlases/README.md) | Canonical curated atlas-lane contract and inventory |
| [`../atlases/source-role-anti-collapse.md`](../atlases/source-role-anti-collapse.md) | Exact canonical target for the legacy source-role pointer |
| [`./master-api-surface.md`](./master-api-surface.md) | Current responsibility-based API compatibility pointer |
| [`./source-role-anti-collapse.md`](./source-role-anti-collapse.md) | Current repository-grounded legacy source-role compatibility pointer |
| [`../doctrine/directory-rules.md`](../doctrine/directory-rules.md) | Adopted placement and compatibility law |
| [`../adr/ADR-0029-adopt-directory-governance-standard-v2.md`](../adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Accepted adoption decision |
| [`../registers/DRIFT_REGISTER.md`](../registers/DRIFT_REGISTER.md) | Human-readable drift tracking |
| [`../../control_plane/deprecation_register.yaml`](../../control_plane/deprecation_register.yaml) | Machine deprecation register; currently empty |
| [`../../control_plane/path_alias_register.yaml`](../../control_plane/path_alias_register.yaml) | Active alias projection; no singular-atlas mapping at snapshot |
| [`../../data/receipts/generated/README.md`](../../data/receipts/generated/README.md) | Generated-work provenance boundary |
| [`../../schemas/contracts/v1/receipts/generated_receipt.schema.json`](../../schemas/contracts/v1/receipts/generated_receipt.schema.json) | Machine shape for generated receipts |

[Back to top](#top)

---

<a id="13-adrs-and-open-dr-references"></a>

## 13. Governing decisions and unresolved decision work

| Decision or claim | Current status | Effect here |
|---|---|---|
| ADR-0029 adopts Directory Rules v2 | `ACCEPTED` | Makes `docs/atlases/` the curated atlas lane and permits this same-path correction |
| `ADR-S-02-docs-dossiers-vs-docs-atlases.md` at the exact v1 path | `ABSENT` at snapshot | Must not be cited as an accepted or active migration decision |
| 30-day singular-lane mirror window | `LINEAGE` / not activated | No start date, register entry, synchronization, or sunset was verified |
| Formal `docs/atlas/` compatibility class | `NEEDS VERIFICATION` | Do not encode a machine class by prose alone |
| Singular-to-plural lane migration | `HOLD` | Requires accepted disposition and dependency closure |
| Canonical carrier naming within `docs/atlases/` | `CONFLICTED` | This README cannot settle it |
| Physical deletion of the singular lane | `HOLD` | Requires zero-writer, zero-consumer, parity, and retirement evidence |

A future accepted decision may establish a compatibility class or migration
sequence. It must not retroactively turn the old README's proposed timer into
evidence that the sequence already ran.

[Back to top](#top)

---

<a id="14-verification-checklist"></a>

## 14. Open verification backlog

### P0 — required before structural action

- [ ] Assign accountable documentation, atlas, migration, and consumer stewards.
- [ ] Choose a finite compatibility class for `docs/atlas/` through an accepted decision.
- [ ] Inventory repository-internal, external, generated, and deployed consumers.
- [ ] Decide whether the master API lineage needs a standalone atlas carrier.
- [ ] Record a complete alias or deprecation entry only after its required fields are known.
- [ ] Prove link, fragment, identity, and content-routing parity.
- [ ] Define correction handling for any released artifact that embeds a singular-lane reference.
- [ ] Create and test a rollback target before tombstoning or deletion.

### P1 — lane quality and convergence

- [ ] Reconcile overlapping carrier names and roles within `docs/atlases/`.
- [ ] Resolve the `.pdf/` directory collision recorded by the canonical lane README.
- [ ] Verify document-registry coverage and current inbound-document graph.
- [ ] Decide whether legacy pointers remain durable or become condition-based tombstones.
- [ ] Establish re-review triggers and evidence freshness for every pointer.

### P2 — retirement proof

- [ ] Demonstrate zero writers to the singular lane.
- [ ] Demonstrate zero unresolved consumers.
- [ ] Record retirement, correction, and rollback evidence.
- [ ] Remove the lane only in a separately reviewed migration change.

[Back to top](#top)

---

<a id="15-rollback"></a>

## 15. Correction and rollback

### Documentation correction

When this README's repository facts drift:

1. pin the new base;
2. reread the direct singular and canonical atlas trees;
3. update only claims supported by current evidence;
4. preserve compatibility anchors and stable identity;
5. validate links and metadata;
6. issue a transparent forward correction or reviewed revert.

### Rollback of this documentation update

The prior target blob is:

```text
9b4330985fc790e0a0c777300ba7e5ae780472c6
```

Before merge, close the draft pull request and abandon the task branch; branch
deletion is separate. After an authorized merge, restore the prior blob or
transparently revert the documentation commit through normal Git history. Do
not reset or rewrite shared history.

### Structural rollback is separate

Reverting this README does not:

- reactivate a deprecation timer;
- migrate or restore an atlas carrier;
- change a path alias;
- repair external links;
- mutate evidence, policy, release, cache, deployment, or public state.

Any future structural migration must carry its own rollback record and cannot use
this documentation rollback as operational proof.

[Back to top](#top)

---

<a id="16-last-reviewed"></a>

## 16. Review record and change history

| Field | Current value |
|---|---|
| Last evidence review | 2026-08-22 |
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Evidence commit | `43792be16c693d7e4ce9da8afe5514da87440e0d` |
| Prior blob | `9b4330985fc790e0a0c777300ba7e5ae780472c6` |
| Direct children observed | Three Markdown files |
| Human review | Pending |
| Hosted exact-head checks | Pending until a pull request head exists |
| Runtime, deployment, release, publication | Not exercised |

### Change history

| Version | Date | Change |
|---|---|---|
| v1 | 2026-05-25 | Corpus-grounded deprecation/mirror proposal with a proposed 30-day sunset and placeholder authority fields. |
| v2.0 | 2026-08-22 | Repository-grounded compatibility boundary; current direct inventory; accepted Directory Rules basis; deprecation/alias/ADR negative-state evidence; exact redirects; migration and deletion hold. |

### Re-review triggers

Re-review this README when:

- a direct child changes;
- a formal alias or deprecation record is added;
- an atlas carrier decision is accepted;
- consumer closure materially advances;
- a migration, tombstone, or retirement is proposed;
- the canonical atlas lane's naming or PDF-path conflict is resolved;
- CODEOWNERS or documentation validation changes materially.

---

**Current conclusion:** `docs/atlas/` remains a noncanonical compatibility and
navigation lane. Maintain existing pointers truthfully, send all new curated
atlas content to [`docs/atlases/`](../atlases/), and keep structural convergence
on `HOLD` until accepted decision, consumer, validation, correction, and rollback
evidence closes.

[Back to top](#top)

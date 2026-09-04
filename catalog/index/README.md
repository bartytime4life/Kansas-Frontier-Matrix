<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/catalog-index-readme
title: catalog/index/ — Catalog Index Compatibility Redirect
type: readme; deprecated-root-descendant; compatibility-redirect
version: v0.3.0
status: repository-grounded draft; frozen-root integration hold
owners: NEEDS VERIFICATION — catalog, data, index, evidence, migration, and release stewards
created: 2026-06-16
updated: 2026-09-04
policy_label: public-review; non-authoritative; no-direct-public-data-path
current_path: catalog/index/README.md
owning_root: catalog/
root_class: deprecated
parent_contract: catalog/README.md
canonical_target: data/catalog/
mutation_posture: immutable; frozen_no_writes; redirect_only
retention: migration_bound
truth_posture: CONFIRMED pinned repository and adopted authority; PROPOSED README correction; UNKNOWN runtime and external consumers
review_scope: existing index redirect only; no catalog payload, migration, or authority change
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: 832d15769f142f70b0065c9b8c45a7b3e4cd5c10
  prior_blob: 3898725a2e3311222020c66099ae4a09f806ea5e
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  root_registry_blob: 024f668b5f0a9239bafa4f8b09e2afd86300ff8c
  correction_register_blob: b48e8df74a2b9d8c2599ce256ef5156687b98dbf
  method: full target read; parent and canonical README reads; exact direct-child listings; adopted rules and correction-authority review
related:
  - ../README.md
  - ../../data/catalog/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/adr/ADR-0038-trusted-base-topology-correction-transitions.md
  - ../../control_plane/root_registry.yaml
  - ../../control_plane/repository_topology_correction_register.yaml
notes:
  - "This is retained navigation, not an HTTP redirect, runtime service, index producer, or permission to consume internal data."
  - "The pinned catalog/index subtree contains this README and one empty .gitkeep, with no child directory."
  - "No direct index child exists under data/catalog at the evidence snapshot; this update does not create one."
  - "ADR-0038 accepts a Stage 1 mechanism, not this index README transition; the inspected register has only a proposed agriculture entry with null decision bindings."
  - "Reviewable branch authoring is separate from acceptance and integration; no topology baseline, validator, register, or release control changes."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Catalog Index Compatibility Redirect

**Looking for governed catalog indexes? Start at [`data/catalog/`](../../data/catalog/README.md).**

`catalog/index/` preserves a legacy navigation boundary inside the **deprecated,
frozen `catalog/` root**. It is not an index service, source registry, canonical
catalog, or public-data endpoint. The [parent containment contract](../README.md)
owns the inherited root boundary.

> [!IMPORTANT]
> **No new content belongs here.** Preserve the existing redirect and placeholder
> until their governed correction or retirement is authorized. Do not add index
> payloads, migration notes, drift files, schemas, receipts, or new placeholders.

> [!WARNING]
> **Frozen-root integration hold.** This README replacement is a reviewable
> proposal, not an accepted exact transition. A documentation-only change still
> changes a frozen blob identity. Neither this README nor an unrelated passing
> check authorizes integration, a baseline refresh, or a correction-register edit.

| Boundary | Evidence-bounded position |
|---|---|
| Owning root | `catalog/`; adopted class `deprecated` |
| Canonical destination | `data/catalog/`; catalog projections remain subordinate to evidence and release |
| Mutation and retention | `immutable`, `frozen_no_writes`, `redirect_only`; migration-bound |
| Tracked local contents | This README and one zero-byte `.gitkeep`; no child directories |
| Dedicated `data/catalog/index/` lane | Absent from the pinned direct-child listing; future placement is not decided here |
| Public exposure | No direct public-data use of this path or internal catalog stores |
| Stewardship and operational closure | `NEEDS VERIFICATION`; directory presence is not proof of enforcement or retirement readiness |

## Quick jump

[Evidence](#0-evidence-basis-for-this-revision) · [Purpose](#1-purpose) ·
[Canonical home](#2-canonical-home) · [Authority](#3-authority-boundary) ·
[Default posture](#4-default-posture) · [Allowed](#5-allowed-contents) ·
[Excluded](#6-forbidden-contents) · [Tree](#7-directory-shape) ·
[Minimum slice](#8-minimum-safe-redirect-slice) · [Diagram](#9-diagram) ·
[Migration](#10-migration-posture) · [Anti-bypass](#11-runtime-and-producer-anti-bypass-matrix) ·
[Inspection](#12-inspection-path) · [Validation](#13-validation-expectations) ·
[Change pattern](#14-safe-change-pattern) · [Rollback](#15-rollback-and-correction-posture) ·
[Language](#16-safe-language-rules) · [Done](#17-definition-of-done) ·
[Open verification](#18-open-verification-items)

## 0. Evidence basis for this revision

All repository observations below are bounded to
[`main@832d15769f142f70b0065c9b8c45a7b3e4cd5c10`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/commit/832d15769f142f70b0065c9b8c45a7b3e4cd5c10),
reviewed on **2026-09-04**. Relative links provide navigation; the immutable commit
and blob identities bind this review's evidence.

| Evidence | What was confirmed | Limit |
|---|---|---|
| Target README and exact `catalog/index/` listing | Prior README blob `3898725a2e3311222020c66099ae4a09f806ea5e`; empty `.gitkeep` blob `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`; no other children | No claim about ignored, untracked, hosted, cached, or external bytes |
| [Parent README](../README.md) and [Root Registry](../../control_plane/root_registry.yaml) | `root.catalog` is deprecated, immutable, migration-bound, and targets `data/catalog/` | An entry or README is not proof of universal no-write enforcement |
| [Canonical catalog README](../../data/catalog/README.md) and its direct-child listing | Catalog discovery/interoperability projections belong under `data/catalog/`; no direct `index/` child exists at this pin | Not a recursive inventory of index objects or a decision about a future sublane |
| [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) and [Directory Rules](../../docs/doctrine/directory-rules.md) | The exact v2 rules bytes are adopted; their retained internal `PROPOSED_FOR_ADOPTION` label does not undo the accepted decision | Later structural changes still need their own applicable authority |
| [ADR-0038](../../docs/adr/ADR-0038-trusted-base-topology-correction-transitions.md) and [correction register](../../control_plane/repository_topology_correction_register.yaml) | Stage 1 mechanism accepted; the register has only a proposed agriculture transition with null accepted-decision bindings | No entry authorizes this index README replacement; no Stage 2 consumption is established by this review |

**Directory Rules basis:** sections 11–12 assign lifecycle/accountability and
catalog-projection responsibilities; section 16 supplies the compact inherited
boundary and verified direct-child tree; sections 17–18 preserve compatibility,
correction, and rollback controls. ADR-0038 makes frozen-content correction a
separate exact-transition matter. Placement is not mutation permission.

## 1. Purpose

Keep legacy links understandable without creating another catalog-index writer.
This page explains where readers should go, what must not accumulate here, and
what evidence a correction or retirement requires.

The word **redirect** describes documentation navigation only. This update
installs no HTTP redirect, alias resolver, search backend, API route, producer,
consumer, or data migration.

## 2. Canonical home

[`data/catalog/`](../../data/catalog/README.md) owns governed catalog projections,
including catalog indexes, matrices, quality summaries, and release-linked
subsets. Index membership and lookup success do not establish source authority,
EvidenceBundle closure, policy permission, or release state.

The pinned direct-child listing contains `README.md` and the six directories
`dcat/`, `domain/`, `domains/`, `prov/`, `settlements-infrastructure/`, and `stac/`.
There is **no direct `index/` child**. This is a presence/absence observation, not
acceptance of every existing spelling or alias. The canonical README records
child-role distinctions; this leaf does not resolve their placement drift.

Do not create `data/catalog/index/` just to mirror this legacy path. A dedicated
lane remains **PROPOSED** until its responsibility, owner, existing-family overlap,
consumers, contract, validation, and applicable placement decision are established.
Catalog indexes may belong to an existing family; this README mandates no new tree.

## 3. Authority boundary

The local scope is `catalog/index/`; its owning responsibility root is `catalog/`,
not a new “index” root. It inherits the parent's deprecated containment posture.

**Inputs to this document:** pinned repository evidence, adopted rules, accepted
ADRs, and reviewed migration/correction evidence. **Outputs:** human navigation,
exclusions, and explicitly bounded verification work. **Permitted content writer:**
none by default under the frozen-root posture; a reviewed proposal is not an
accepted production writer.

This path owns no domain truth, source admission, semantic contract, schema,
policy, proof, receipt, release decision, public artifact, or operational index.
The Root Registry is a projection of adopted authority, not a way to grant an
exception. A note, badge, proposed ADR, or successful GitHub merge cannot create
that exception either.

## 4. Default posture

Preserve the governing lifecycle:

```text
RAW -> WORK/QUARANTINE -> PROCESSED -> CATALOG/TRIPLET -> PUBLISHED
```

Promotion is a governed transition, not a file move or completed indexing job.
Public clients use governed APIs and released public-safe artifacts, never this
compatibility path or direct internal stores.

For a consequential claim, resolve `EvidenceRef -> EvidenceBundle` and preserve
source role, identity, spatial/temporal scope, rights, sensitivity, validation,
provenance, integrity, receipts/proofs, policy, review, release, correction, and
rollback state. A search hit, map selection, tile, graph projection, summary, or AI
answer remains a carrier, not root truth.

Unclear rights, cultural authority, living-person/DNA data, rare-species or
archaeological precision, private-land detail, or infrastructure sensitivity
requires denial, quarantine, redaction, generalization, or staged access as
applicable. Record transforms and reasons; do not paste protected bytes into a
public issue, README, receipt, or branch.

## 5. Allowed contents

Only the **already tracked** navigation boundary is present:

| Existing item | Role | Restriction |
|---|---|---|
| `README.md` | Retained redirect and containment guidance | Any replacement remains subject to frozen-root correction authority |
| `.gitkeep` | Existing empty placeholder | Preserve in this update; it neither admits content nor justifies further scaffolding |

The earlier suggestions to add `MIGRATION.md`, `DRIFT.md`, `OPEN-QUESTIONS.md`, or
new placeholders are withdrawn. Keep migration and drift records in their existing
owning roots and link to them when verified. An unaccepted migration note is not a
write permit.

## 6. Forbidden contents

| Do not place here | Governing destination or responsibility |
|---|---|
| Catalog, lookup, crosswalk, collection, domain, source, layer, STAC/DCAT/PROV, CatalogMatrix, or publication-state index projections | `data/catalog/`, within the verified appropriate family |
| Source descriptors and source/dataset/layer/rights/sensitivity registry instances | `data/registry/`, under their owning registry family |
| RAW, WORK, QUARANTINE, or PROCESSED payloads; relationship projections | Their `data/` lifecycle lane; graph projections belong to `data/triplets/` |
| Process, validation, transform, redaction, or catalog-build receipts | `data/receipts/`; receipts describe execution, not approval |
| EvidenceBundles and proof-pack support | `data/proofs/`; proof support is not a release decision |
| Release manifests, promotion/correction/withdrawal decisions, rollback cards, and release signatures | `release/`, under their verified object family |
| Released discovery indexes, search manifests, maps, tiles, exports, or other public-safe carriers | `data/published/` only after governed release; serving remains governed |
| Semantic contracts, machine shapes, and policy rules | `contracts/`, `schemas/`, and `policy/`, respectively |
| Producer code, pipelines, application/runtime code, tools, workflow logic, or configuration | Their existing implementation/configuration responsibility roots, not this data-looking legacy path |

These are responsibility routes, not permission to create files, admit a source,
run a producer, relocate restricted data, or publish a derivative.

## 7. Directory shape

**CONFIRMED tracked direct children at the pinned commit:**

```text
catalog/index/
├── .gitkeep                 # existing zero-byte placeholder; no authority
└── README.md                # retained navigation and containment boundary
```

There are no child directories or tracked payload files in this subtree at the
snapshot. This closes the prior README's local tracked-inventory uncertainty,
not a repository-wide or external-storage audit.

## 8. Minimum safe redirect slice

| Property | Bounded result or remaining gate |
|---|---|
| Canonical navigation | Points to the verified `data/catalog/` parent, not an invented index sublane |
| Local payload exclusion | Confirmed for the pinned two-file tracked subtree only |
| Inherited frozen boundary | Adopted through ADR-0029; no new files or parallel authority permitted |
| Producer/public-use exclusion | Required behavior; complete writer, consumer, and runtime verification remains open |
| Exact correction authority | Not present for this README replacement; integration stays held |
| Retirement | Requires zero-writer/zero-consumer, migration, correction, and rollback evidence; not performed |

## 9. Diagram

The diagram separates navigation from the governed data path; it is not an
implemented route map or an automatic migration:

```text
Documentation navigation:
  catalog/index/README.md  -->  data/catalog/README.md

Governed data path:
  processed records  -->  catalog projections  -->  release-approved carriers
       evidence / policy / review / integrity / correction / rollback gates
                                                   |
                                                   v
                                     governed API or released-artifact delivery
```

There is no public-data shortcut from `catalog/index/` to the final delivery step.

## 10. Migration posture

No migration is performed by this update. If misplaced material is discovered,
first hold its consumption and classify its actual responsibility. Preserve
source identity, digests, producer history, evidence, rights/sensitivity, prior
references, and any exposure evidence without redistributing restricted bytes.

Then establish the accepted decision, exact old/new mappings, verified target,
single-writer cutover, positive and negative validation, correction propagation,
and rollback or forward-fix path. Regeneration is not permission to discard
lineage. Any temporary dual-read arrangement must be explicitly authorized and
must not weaken public or sensitivity controls.

Only retire the legacy path after zero-producer/zero-consumer and migration
closure. Do not automatically move files, remove `.gitkeep`, delete this README,
or create an index sublane in response to this guidance.

## 11. Runtime and producer anti-bypass matrix

| Risk | Required disposition | Evidence needed before claiming closure |
|---|---|---|
| A generator or CI job writes index objects here | Reject the destination; use the governed owning lane after review | Producer configuration, output-path checks, and negative tests |
| A public API, map, search, cache, export, or AI feature reads this path as data | Deny the shortcut; use governed release-aware delivery | Consumer inventory and authenticated runtime/access tests |
| Lookup success is treated as source/evidence/release authority | Resolve evidence and the actual policy/review/release state, or abstain | Claim-level references and finite negative outcomes |
| A proposed `data/catalog/index/` lane is advertised as implemented | Keep absence and future proposal separate | Exact tree, accepted placement where required, and consumer/validator evidence |
| A receipt, proof, schema, policy, or release object is added here | Hold and classify; use the existing owning responsibility | Reviewed migration and reference-closure evidence |
| A same-path README edit is assumed exempt from freezing | Keep integration held until its exact transition is authorized | Trusted-base decision and bindings, plus required validation |
| Downstream artifacts already consumed misplaced material | Preserve incident history and apply governed correction/invalidation | Correction notices, affected-object inventory, receipts, and rollback proof |

These are requirements, not claims that the current runtime enforces every row.

## 12. Inspection path

The following commands are **read-only review aids for a real checkout**. They do
not admit sources, rebuild indexes, or authorize correction:

```bash
# Run from the repository root; record the actual checkout identity.
git rev-parse --verify HEAD
git ls-tree -r HEAD -- catalog/index/
git ls-tree HEAD:data/catalog/
git grep -n -F 'catalog/index/' HEAD -- .
```

`git ls-tree` describes tracked Git state, not ignored files or external stores.
`git grep` returning status 1 means no match; other failures must be investigated.
A text match is only a candidate reference, and zero matches do not establish
zero dynamic, deployed, hosted, or external consumers. Classify documentation
references separately from executable producers and consumers.

## 13. Validation expectations

For a README correction, verify the complete target, inherited authority,
tracked inventory, supported destination, metadata, retained anchors, relative
links, tables, code fences, final newline, and absence of conflict markers or
sensitive payloads. Compare the exact base and head, not an unpinned working tree.

For AI-authored work, follow [CONTRIBUTING.md](../../CONTRIBUTING.md) and the
[existing generated-receipt lane](../../data/receipts/generated/README.md): record
final artifact hashes, pinned evidence, actual checks and omissions, and pending
human review. Do not put that receipt under `catalog/index/`.

**Integration is a separate gate.** ADR-0038 states that KFM-TOPO-004 uses
`path@object_id` for frozen-root evidence. Replacing this README introduces a new
frozen-content delta even when the path count is unchanged. The inspected
agriculture-only proposed entry does not authorize it. Do not label this new
index delta inherited, suppress its finding, refresh a baseline, or claim an
exception solely because another catalog edit previously merged.

This documentation review is not an executed full topology, producer, runtime,
release, accessibility, or public-access test. Record exact-head hosted outcomes
in the PR; distinguish performed, failed, pending, skipped, and unrun checks.

## 14. Safe change pattern

1. Re-pin the base, governing files, target blob, and current overlap before work.
2. Limit the proposal to this retained README and directly required provenance.
3. Preserve the document ID, legacy anchors, inherited freeze, and evidence limits.
4. Validate candidate bytes and final remote scope; leave `.gitkeep`, registries,
   topology baselines, validators, policies, and lifecycle payloads unchanged.
5. Open a draft only through an eligible delivery path. Read back actual GitHub
   state; body text is not draft-retention enforcement.
6. Keep ready/merge/integration held until the exact correction and required review
   are separately authorized. Do not bundle self-authorizing controls into the edit.

## 15. Rollback and correction posture

The pre-update README is available at
[the pinned source path](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/832d15769f142f70b0065c9b8c45a7b3e4cd5c10/catalog/index/README.md),
blob `3898725a2e3311222020c66099ae4a09f806ea5e`.

Before integration, retain the proposal unmerged or append a non-force revert on
the task-owned branch. Preserve its generated receipt as historical provenance;
do not silently rewrite a receipt to claim it described different bytes.

After integration, a revert is itself a frozen-content transition requiring
current review and authority. Restoring old bytes also restores their outdated
permission to add files, so choose an explicitly reviewed correction rather than
an automatic rollback. Do not restore another incident's damaged catalog blob,
reset shared history, reopen parallel writers, or undo unrelated work.

## 16. Safe language rules

| Avoid | Evidence-bounded wording |
|---|---|
| “This is the canonical index.” | “This is legacy navigation to governed catalog projections.” |
| “The entire system contains no index payloads.” | “The pinned `catalog/index/` subtree has only a README and empty placeholder.” |
| “`data/catalog/index/` is implemented.” | “No direct index child exists at the recorded pin; any future lane remains proposed.” |
| “CI blocks every unauthorized write.” | “The frozen-root rule is documented; actual runs and server-side coupling require their own evidence.” |
| “Documentation changes are exempt.” | “A new frozen blob needs its own accepted exact-transition authority.” |
| “Migration is complete” or “safe to serve.” | “Migration, consumer closure, release, and access remain unverified until their evidence closes.” |

## 17. Definition of done

**Documentation review scope:**

- [x] Preserve the stable document ID, title, top anchor, and numbered section anchors.
- [x] Verify the exact tracked local inventory and the canonical parent destination.
- [x] Replace speculative child files with the actual two-file tree.
- [x] Explain adopted deprecation and the separate frozen-root integration hold.
- [x] Preserve lifecycle, evidence, rights/sensitivity, public-access, and rollback boundaries.

**Not completed by this README:**

- [ ] Separately accepted and correctly bound exact transition for this replacement.
- [ ] Required exact-head validation and authorized human review before integration.
- [ ] Accountable specialist stewardship and independent review where required.
- [ ] Complete producer/consumer, external-storage, migration, and retirement proof.
- [ ] Operational policy/release/correction/rollback closure for any affected data.

## 18. Open verification items

| Open item | First affected transition | Evidence required |
|---|---|---|
| Exact index README correction authority | Integration | Separately accepted decision and exact trusted-base bindings; not the agriculture entry |
| Hosted checks and enforcement coupling | Readiness/integration | Exact-head run results and separately verified required-check behavior |
| Specialist ownership and review separation | Relevant approval | Named accountable reviewers and authenticated review evidence |
| Dynamic/deployed/external consumers and writers | Migration or retirement | Source/configuration, runtime, deployment, cache, and external-reference inventory |
| Dedicated canonical index family, if needed | New-lane creation | Responsibility, overlap, owner, contract, consumers, validation, and applicable decision |
| Correction, invalidation, retention, and rollback drills | Public change or retirement | Governed records and executed evidence, not directory presence |

<details>
<summary>Appendix A — no-loss preservation note</summary>

The v0.2 redirect, anti-parallel-authority, no-public-data-path, responsibility
routing, lifecycle, sensitivity, migration, and rollback intent is retained.
The document ID, H1, top anchor, all numbered H2 headings, Quick jump, and Status
summary remain available. The unverified local inventory is replaced with exact
tracked evidence. The old suggestion to create migration/drift files or new
placeholders is explicitly withdrawn because it conflicts with the adopted
frozen-root posture. The canonical index sublane remains uncreated; no payload,
producer, consumer, alias, schema, policy, release, or runtime state is upgraded.

</details>

## Status summary

**Verified navigation; deprecated frozen root; no catalog payloads in the pinned
local subtree; proposed README correction with integration held.** Use
[`data/catalog/`](../../data/catalog/README.md) for governed catalog discovery.
No index service, migration, release, deployment, promotion, or publication is
established by this page.

[Back to top](#top)

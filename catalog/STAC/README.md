<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/catalog-stac-readme
title: catalog/STAC/ — Deprecated STAC Compatibility Redirect
type: readme; deprecated-boundary; compatibility-redirect
version: v0.3.0
status: draft; repository-grounded; deprecated; redirect-only; integration-hold
owners: ["@bartytime4life"]
owner_scope: repository review route; specialist stewardship and independent approval remain NEEDS VERIFICATION
created: 2026-06-16
updated: 2026-09-04
policy_label: public-doc; no-catalog-publication; fail-closed
owning_root: catalog/
root_class: deprecated
readme_profile: BOUNDARY_COMPACT
canonical_target: data/catalog/stac/
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: 7187fb20a8c1f9bf838e0f1fd00fb691b378c434
  prior_readme_blob: 198a970db9e71b2dc7f5cdbf171b14c0f9a878ce
  stac_tree: 93947fa1b72ed6fe4915a2ed11653f4cd43473c9
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
truth_posture: CONFIRMED tracked inventory and adopted boundary; PROPOSED README correction; UNKNOWN external consumers and runtime state
related:
  - ../README.md
  - ../../data/catalog/stac/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/adr/ADR-0038-trusted-base-topology-correction-transitions.md
  - ../../control_plane/root_registry.yaml
  - ../../control_plane/repository_topology_correction_register.yaml
  - ../../data/receipts/generated/README.md
tags: [kfm, stac, deprecated, compatibility, redirect-only, frozen-no-writes]
notes:
  - "Preserves the existing document ID, top anchor, and numbered section anchors."
  - "Removes obsolete permission to add notes or placeholders beneath the frozen catalog root."
  - "This proposed correction does not authorize its own frozen-root blob replacement."
  - "No schema, policy, validator, baseline, register, payload, release, or runtime change."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# STAC Compatibility Redirect

**Looking for KFM STAC records? Start with the [canonical STAC lane](../../data/catalog/stac/README.md).**

`catalog/STAC/` is retained navigation beneath the **deprecated, frozen**
[`catalog/` root](../README.md). It is not a catalog service, storage target,
source registry, or public asset endpoint. This README is a documentation
redirect; it does not implement an HTTP redirect, filesystem alias, or resolver.

> [!IMPORTANT]
> The canonical logical home is `data/catalog/stac/`. Placement there does not
> authorize public access: public clients use governed APIs or released,
> public-safe artifacts, not internal or unreleased catalog stores.

> [!WARNING]
> **Draft correction; integration held.** Replacing this README changes a blob
> covered by the frozen-root topology rule. The existing agricultural correction
> mechanism does not authorize this STAC edit. Keep the validator, baseline, and
> correction register unchanged; see [validation expectations](#13-validation-expectations).

## Quick jump

[Evidence](#0-evidence-basis-for-this-revision) ·
[Canonical home](#2-canonical-home) ·
[Boundary](#3-authority-boundary) ·
[Inventory](#7-directory-shape) ·
[Inspection](#12-inspection-path) ·
[Validation](#13-validation-expectations) ·
[Open verification](#18-open-verification-items)

## 0. Evidence basis for this revision

Reviewed on **2026-09-04** against
[`main@7187fb20a8c1f9bf838e0f1fd00fb691b378c434`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/commit/7187fb20a8c1f9bf838e0f1fd00fb691b378c434).
The following are snapshot findings, not assertions about later `main`.

| Evidence | Confirmed scope | Limit |
|---|---|---|
| Exact `catalog/STAC/` Git tree `93947fa1b72ed6fe4915a2ed11653f4cd43473c9` | Only `README.md` and an empty `.gitkeep`; no tracked payload or child directory | Does not inventory ignored, untracked, cached, or externally stored bytes |
| [Parent README](../README.md), blob `44378e14fe7470f19df20ebfc9914ad1e3d2a6a9` | Deprecated containment; retain existing redirects without adding placeholders | Its older inventory and enforcement snapshot are not a current runtime audit |
| [Root Registry](../../control_plane/root_registry.yaml), blob `024f668b5f0a9239bafa4f8b09e2afd86300ff8c` | `root.catalog`: deprecated, immutable, `frozen_no_writes`, `redirect_only`; target `data/catalog/` | A machine projection does not grant write or release authority |
| [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) and [Directory Rules](../../docs/doctrine/directory-rules.md) | Accepted adoption of rules blob `fd49a0b83e55cef52c1124281f093e263526898d` | The adopted file's internal draft label does not undo that exact-byte adoption |
| [Canonical STAC README](../../data/catalog/stac/README.md), blob `6d534b95f46ba11bb86e8cbe9abd22b88fb7c1f9` | Documents the CATALOG-stage home and release-gated exposure | Its draft profile and historical version statements do not prove current conformance |
| [ADR-0038](../../docs/adr/ADR-0038-trusted-base-topology-correction-transitions.md), blob `79f37be0991b050d8bc9c00991d6db887d343cd7` | Stage 1 mechanism accepted; exact-transition and trusted-base requirements remain | No blanket frozen-root exception and no authorization for this path |
| [Correction register](../../control_plane/repository_topology_correction_register.yaml), blob `b48e8df74a2b9d8c2599ce256ef5156687b98dbf` | One proposed agriculture entry with null accepted-decision bindings | No accepted, bound STAC transition |

Drive's *Directory Rules* and the Notion *Frozen Catalog Correction-Mechanism
Decision Package* were consulted as lineage and coordination. The adopted
repository decisions above govern; neither coordination prose nor this README
creates an exception. `CONFIRMED` inventory is separate from `PROPOSED` correction
and from unverified runtime or release maturity.

## 1. Purpose

Preserve legacy navigation, direct contributors to the owning lifecycle lane,
and prevent a second writable STAC home. Inherit the parent root's containment
contract; do not turn this leaf into a replacement STAC specification.

## 2. Canonical home

| Path | Role |
|---|---|
| `catalog/STAC/` | Deprecated, frozen documentation redirect; no new catalog writes |
| `data/catalog/stac/` | Canonical logical STAC catalog lane inside the governed data lifecycle |

Use the exact lowercase canonical path. Do not create case variants, symlinks,
mirrors, or automatic rewrites as a shortcut. An external STAC source, synthetic
test fixture, or released representation is not automatically misplaced merely
because it is outside this lane; classify it by its owning responsibility and
lifecycle, rather than its filename.

## 3. Authority boundary

| Concern | Local contract |
|---|---|
| Ownership | `catalog/` owns deprecated containment only; `data/` owns lifecycle catalog instances |
| Review route | `@bartytime4life`, as recorded by the Root Registry; specialist stewardship and independent approval remain unverified |
| Inputs / outputs | Verified path and migration facts in; navigation and containment guidance out; no dataset or trust-object output |
| Mutation | Frozen; retaining a README does not authorize its replacement or new sibling files |
| Exposure | Public documentation is not permission to expose catalog records, source bytes, or internal stores |
| Retention | Migration-bound; no retirement until accepted decisions and zero-writer/zero-consumer evidence close |

Directory Rules §§16–18 supply the compact boundary profile, direct-child map,
compatibility constraints, migration discipline, and rollback rules. ADR-0029
establishes the adopted edition; ADR-0038 constrains frozen-topology corrections.
This draft changes none of those authorities.

## 4. Default posture

Unexpected content is **drift requiring review**, not admitted evidence. Do not
load, index, publish, or cite it as canonical STAC. Preserve its identity and
provenance before remediation. Unclear rights, sensitivity, sovereignty,
protected locations, living-person/DNA data, or private-land details require
restricted handling; do not copy them into public issues or review receipts.

## 5. Allowed contents

Retain the **existing** README and zero-byte `.gitkeep` while the root remains
under containment. Links may point to records in their actual owning homes.

Do **not** add `MIGRATION.md`, `DRIFT.md`, `OPEN-QUESTIONS.md`, `REMOVED.md`, extra
placeholders, or a second editable catalog here. The previous edition's suggested
files were proposals, not an exception to the subsequently adopted freeze.

## 6. Forbidden contents

| Not stored here | Owning responsibility |
|---|---|
| STAC Catalogs, Collections, Items, asset metadata, links, indexes, or profile sidecars | Governed catalog instances in `data/catalog/stac/`; standards and schemas in their separate homes |
| DCAT/PROV records or domain catalog instances | Appropriate family under `data/catalog/` |
| Source descriptors, rights/sensitivity registry instances | Governed registry family under `data/registry/` |
| Receipts or evidence/proof objects | Their respective `data/receipts/` and `data/proofs/` families |
| Release, promotion, correction, withdrawal, or rollback decisions | `release/` |
| Released public-safe payloads | `data/published/`, after governed release |
| Semantic contracts, schemas, or normative policy | `contracts/`, `schemas/`, and `policy/`, respectively |
| Producer code, validation code, tests, or migration implementation | Existing responsibility-owning implementation, tooling, test, and migration roots |

These are routing boundaries, not declarations that every proposed object family
or validator is implemented. Asset metadata does not relocate the asset bytes.

## 7. Directory shape

**CONFIRMED tracked inventory at the evidence snapshot:**

```text
catalog/STAC/
├── .gitkeep                  # existing zero-byte placeholder; not authority
└── README.md                 # existing deprecated STAC navigation boundary
```

The retained placeholder has blob
`e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`. The pre-edit README has blob
`198a970db9e71b2dc7f5cdbf171b14c0f9a878ce`. There are no tracked STAC records in
this subtree. That finding does not prove migration completion or zero consumers.

## 8. Minimum safe redirect slice

A useful redirect preserves the canonical pointer, existing anchors, no-payload
boundary, immutable-root posture, and explicit unknowns. A README, empty tree,
or successful formatting check cannot prove that producers and public clients
obey those boundaries.

## 9. Diagram

```text
Legacy navigation: catalog/STAC/README.md -> data/catalog/stac/README.md
                   (documentation link; no data transfer or publication)

Governed lifecycle: RAW -> WORK / QUARANTINE -> PROCESSED
                       -> CATALOG / TRIPLET -> PUBLISHED

Catalog discovery, EvidenceRef -> EvidenceBundle resolution, policy,
review, release, correction, and rollback remain separate responsibilities.
```

Maps, tiles, indexes, graphs, scenes, summaries, and AI are downstream carriers;
they do not acquire truth or publication authority from a STAC link.

## 10. Migration posture

If misplaced material is discovered, first inventory exact paths, bytes, hashes,
source roles, rights, sensitivity, writers, consumers, and existing references.
Then obtain the applicable accepted decision and record the migration in its
owning lane before moving or regenerating anything.

A reviewed migration preserves identity or explicitly versions it, keeps source
and transform lineage, validates target and consumer parity, supplies correction
and rollback evidence, and proves the old path is no longer written or consumed.
No migration, deletion, source admission, or retirement is performed by this
README. Moving a file does not promote it through the lifecycle.

## 11. Runtime and producer anti-bypass matrix

| Risk | Required boundary | Evidence needed before claiming closure |
|---|---|---|
| Producer targets `catalog/STAC/` | Reject new durable output here | Producer configuration, negative test, and exact-run result |
| Public API, map, search, export, or AI uses legacy content as authority | Deny or use the governed released path | Consumer trace and applicable policy/release evidence |
| Canonical path is mistaken for a public URL | No direct internal-store access | Serving configuration and public-boundary checks |
| Duplicate uppercase/lowercase writers or mirrors | Preserve one canonical writer | Case-aware inventory, verified consumer need, and accepted migration |
| Prior downstream use is discovered | Preserve correction and rollback lineage | Affected-consumer inventory and reviewed remediation |
| Documentation or a green check is called release approval | Keep evidence, policy, review, and release distinct | Actual decision records, not README assertions |

This matrix states obligations. It is not an assertion that runtime enforcement
or a comprehensive producer/consumer audit has passed.

## 12. Inspection path

Run these read-only commands from an actual checkout, replacing `REF` only when
intentionally reviewing another pinned commit. They do not validate or publish
STAC records.

```bash
REF=7187fb20a8c1f9bf838e0f1fd00fb691b378c434

git rev-parse --verify "${REF}^{commit}"
git ls-tree -r --long "$REF" -- catalog/STAC/
git show "${REF}:control_plane/root_registry.yaml"
git show "${REF}:control_plane/repository_topology_correction_register.yaml"

# Search tracked text for candidate references; a match is not proof of use.
git grep -n -F 'catalog/STAC' "$REF" -- .
```

`git grep` returning no matches normally exits `1`; a fatal Git error is not an
empty inventory. These commands cannot inspect untracked files, runtime mounts,
external catalogs, browser caches, or deployed configuration. Their presence
here does not claim they were executed in a local checkout for this revision.

## 13. Validation expectations

**Keep review validation and integration authorization separate.**

For this documentation correction, check exact base/head identity, the complete
diff, retained anchors, resolving relative links, balanced fences, final newline,
no sensitive payloads, and the generated-work receipt's schema and final content
hash. Record actual results in the PR rather than treating this checklist as a
passing test report.

For frozen-root integration, [ADR-0038](../../docs/adr/ADR-0038-trusted-base-topology-correction-transitions.md)
explains why `KFM-TOPO-004` fingerprints `path@object_id`. A README replacement
changes that evidence even when no path is added. The existing
[register](../../control_plane/repository_topology_correction_register.yaml)
contains only the proposed agricultural transition; it is not an STAC exception.

**The STAC blob delta is new to this change.** Do not attribute it to inherited
agricultural drift, waive it as “docs-only,” refresh the baseline, suppress the
finding, or use a same-change register edit to authorize it. Integration remains
held pending separately accepted exact authority and the required trusted-base
validation. A draft PR and a valid generation receipt do not satisfy that gate.

## 14. Safe change pattern

Re-pin current `main`, target bytes, applicable decisions, and overlapping work.
Prepare only the bounded correction and its provenance receipt, retaining the
existing path, document ID, and section anchors. Keep proposed bytes separate
from accepted implementation and preserve the frozen-root failure as a later
integration blocker. Follow the current contributor and PR-delivery controls;
do not turn branch authoring into ready, approval, or merge authority.

## 15. Rollback and correction posture

Before integration, leave the candidate branch unmerged or append a non-force
revert on that branch. The exact prior README blob is recorded in §7; `.gitkeep`
and all catalog payloads remain untouched. Preserve the generated receipt as
history rather than rewriting it to describe a different artifact hash.

After any authorized integration, reverting frozen content is itself a reviewed
transition. Re-check current authority and exact bytes; never restore damaged
content, erase correction history, or reopen parallel writers merely to obtain
a matching baseline fingerprint.

## 16. Safe language rules

| Avoid | Use instead |
|---|---|
| “STAC is published here” | “This is a deprecated documentation redirect” |
| “No STAC exists” | “No tracked STAC payload exists in this pinned subtree” |
| “Migration is complete” | “Tracked inventory is confirmed; consumer and migration closure remain unverified” |
| “The canonical path is safe to expose” | “Exposure still requires governed release and access checks” |
| “ADR-0038 permits this edit” | “The accepted mechanism does not authorize this unregistered STAC transition” |
| “CI passed” without exact-head results | Name the executed check, exact scope, result, and limitations |

## 17. Definition of done

For the **README draft**, completion means accurate canonical navigation,
confirmed bounded inventory, inherited freeze semantics, preserved identity and
anchors, documented validation, a hash-matching provenance receipt, and explicit
integration blockers.

For **integration or retirement**, additionally require the applicable accepted
exact transition, trusted-base checks, human review, producer/consumer closure
where relevant, and migration/correction/rollback evidence. Draft completion is
not integration, retirement, runtime readiness, or publication.

## 18. Open verification items

| Item | Status and first affected transition |
|---|---|
| Accepted, bound exact transition for this README replacement | **NEEDS VERIFICATION / HOLD integration**; none present in the inspected register |
| Exact-head hosted checks and independent human review | **NEEDS VERIFICATION** before any readiness or integration claim |
| Full producer, consumer, external-storage, and case-sensitive behavior | **UNKNOWN**; blocks migration/retirement and exposure claims |
| Specialist catalog stewardship and separation of review duties | **NEEDS VERIFICATION**; repository routing is not independent approval |
| Current STAC profile, namespace, schemas, and release/access implementation | **NOT INSPECTED** for this redirect change; no conformance or operational claim |

<details>
<summary>Appendix A — no-loss preservation note</summary>

Version v0.3.0 retains the canonical STAC pointer, trust-family separation,
no-public-bypass rule, case-aware routing, migration and rollback requirements,
document ID, top anchor, and all numbered section headings. It replaces stale
inventory uncertainty with the verified two-file tree, removes obsolete proposals
to add files beneath the deprecated root, and records the accepted directory and
exact-transition constraints. Historical v0.2 bytes remain available at the pinned
prior blob. This is not an adoption record or implementation-maturity upgrade.

</details>

## Status summary

**Deprecated navigation, not a catalog.** Use the canonical lifecycle lane for
STAC instances; preserve evidence, policy, review, release, correction, and
rollback boundaries. This proposed documentation correction does not authorize
its own integration or any data publication.

[Back to top](#top)

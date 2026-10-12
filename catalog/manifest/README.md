<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/catalog-manifest-readme
title: catalog/manifest/ — Deprecated Manifest Compatibility Redirect
type: readme; deprecated-boundary; compatibility-redirect
version: v0.3.0
status: draft; repository-grounded; deprecated; redirect-only; integration-hold
owners: ["@bartytime4life"]
owner_scope: repository review route only; specialist stewardship and independent approval remain NEEDS VERIFICATION
created: 2026-06-16
updated: 2026-09-04
policy_label: public-doc; no-catalog-publication; fail-closed
owning_root: catalog/
root_class: deprecated
readme_profile: BOUNDARY_COMPACT
canonical_target: data/catalog/
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: 832d15769f142f70b0065c9b8c45a7b3e4cd5c10
  prior_readme_blob: 9fe630fe18decc275d26ad99c5c7e2ac215d18ca
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
truth_posture: CONFIRMED tracked inventory and adopted boundary; PROPOSED documentation correction; UNKNOWN external consumers and runtime state
related:
  - ../README.md
  - ../../data/catalog/README.md
  - ../../release/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/adr/ADR-0038-trusted-base-topology-correction-transitions.md
  - ../../control_plane/root_registry.yaml
  - ../../control_plane/repository_topology_correction_register.yaml
  - ../../data/receipts/generated/README.md
notes:
  - "Preserves the document ID, top anchor, and all numbered section headings."
  - "No new manifest sublane, placeholder, migration note, payload, or authority is created here."
  - "This proposed README correction does not authorize its own frozen-root integration."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Catalog Manifest Compatibility Redirect

**Looking for catalog manifests? Start with [data/catalog/](../../data/catalog/README.md).
Looking for release-governance manifests? Start with [release/](../../release/README.md).**

`catalog/manifest/` is retained navigation beneath the **deprecated, frozen**
[`catalog/` root](../README.md), not a manifest store, catalog service, release
registry, or public endpoint. The links on this page are documentation redirects;
they do not implement an HTTP redirect, filesystem alias, or runtime resolver.

> [!IMPORTANT]
> A canonical logical home is not a public access path. Public clients consume
> governed APIs and released, public-safe artifacts, never internal or unreleased
> catalog stores. A manifest records or references state; it does not grant it.

> [!WARNING]
> **Draft correction; integration held.** Replacing this README changes a blob
> covered by the frozen-root topology rule. No accepted exact transition for
> this path is present in the inspected correction register. Keep the validator,
> baseline, and register unchanged; see [validation expectations](#13-validation-expectations).

## Quick jump

[Evidence](#0-evidence-basis-for-this-revision) ·
[Routing](#2-canonical-home) · [Boundary](#3-authority-boundary) ·
[Inventory](#7-directory-shape) · [Inspection](#12-inspection-path) ·
[Validation](#13-validation-expectations) · [Open items](#18-open-verification-items)

## 0. Evidence basis for this revision

Reviewed on **2026-09-04** against
[`main@832d15769f142f70b0065c9b8c45a7b3e4cd5c10`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/commit/832d15769f142f70b0065c9b8c45a7b3e4cd5c10).
These are pinned observations, not assertions about later repository state.

| Evidence | Confirmed scope | Limit |
|---|---|---|
| Exact `catalog/manifest/` listing | Only `README.md` and an empty `.gitkeep`; no tracked payload or child directory | Does not inventory untracked, ignored, cached, or external bytes |
| [Parent README](../README.md), blob `44378e14fe7470f19df20ebfc9914ad1e3d2a6a9` | Deprecated containment and no new placeholders | Its older inventory is not a current runtime audit |
| [Root Registry](../../control_plane/root_registry.yaml), blob `024f668b5f0a9239bafa4f8b09e2afd86300ff8c` | `root.catalog`: deprecated, immutable, `frozen_no_writes`, `redirect_only`; target `data/catalog/` | The projection grants no write, migration, or release authority |
| [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) and [Directory Rules](../../docs/doctrine/directory-rules.md) | Accepted adoption of rules blob `fd49a0b83e55cef52c1124281f093e263526898d` | The retained draft label inside the adopted bytes does not undo adoption |
| Exact `data/catalog/` listing and [README](../../data/catalog/README.md), blob `765dd1be99aa95d4377931344c05751b751243ec` | Canonical catalog-stage responsibility; no tracked `manifest/` child at this snapshot | Does not establish a dedicated manifest sublane or complete catalog implementation |
| [Release README](../../release/README.md), blob `60b6a656f8f2b765616bba7223f51c25863c7172` | Release-governance records are distinct from catalog projections and published payloads | Does not establish an operational release or final manifest sublane convention |
| [ADR-0038](../../docs/adr/ADR-0038-trusted-base-topology-correction-transitions.md), blob `79f37be0991b050d8bc9c00991d6db887d343cd7` | Stage 1 exact-transition mechanism accepted | The initial agricultural transition does not authorize this manifest edit |
| [Correction register](../../control_plane/repository_topology_correction_register.yaml), blob `b48e8df74a2b9d8c2599ce256ef5156687b98dbf` | One proposed agriculture entry with null accepted-decision bindings | No accepted, bound transition for `catalog/manifest/README.md` |

Drive's *Directory Rules* and the Notion *KFM Repository Workbench* were consulted
as lineage and coordination. Current repository decisions govern placement;
older coordination snapshots do not establish current implementation or approval.

## 1. Purpose

Preserve legacy navigation and prevent a second writable manifest authority.
Inherit the parent root's containment contract rather than duplicate catalog,
release, or manifest specifications in this leaf README.

## 2. Canonical home

Route by **object responsibility and lifecycle**, not by the word `manifest`.

| Artifact responsibility | Logical home or next step |
|---|---|
| Catalog inventory, lookup, collection, crosswalk, or release-linked discovery projection | `data/catalog/`, under its applicable accepted family/profile |
| ReleaseManifest instance or release/promotion/correction/withdrawal/rollback decision | `release/`, under the governing release-family contract |
| Source, dataset, layer, rights, or sensitivity registry instance | Its governed family under `data/registry/` |
| Execution or catalog-build receipt | `data/receipts/` |
| EvidenceBundle or proof-pack instance | `data/proofs/` |
| Object meaning, machine shape, or normative admissibility rule | `contracts/`, `schemas/`, or `policy/`, respectively |
| Released public-safe carrier | `data/published/`, only after the applicable release gates |

**`data/catalog/manifest/` is not tracked at the inspected base.** Do not create
it, link to an imagined README, or call it canonical merely to match this legacy
name. Any future sublane needs responsibility, accepted placement, contracts,
validation, ownership, and migration evidence appropriate to its scope.

A schema, semantic contract, synthetic fixture, source-native manifest, or released
representation is not a misplaced ReleaseManifest decision solely because of its
filename. Asset metadata also does not relocate the referenced asset bytes.

## 3. Authority boundary

| Concern | Local contract |
|---|---|
| Authority owner | `catalog/` owns deprecated containment only; `data/` and `release/` retain their distinct responsibilities |
| Review route | `@bartytime4life` from the Root Registry; specialist stewardship and independent approval remain unverified |
| Inputs / outputs | Verified path, identity, and migration facts in; navigation and boundary guidance out; no trust-object or dataset output |
| Mutation | Frozen; retaining a README is not blanket authority to replace its bytes or add siblings |
| Exposure | Public documentation is not permission to expose internal manifests, catalog records, or source material |
| Retention | Migration-bound; retirement requires accepted decisions and verified writer/consumer closure |

Directory Rules §§16–18 govern compact boundary documentation, direct-child maps,
compatibility, migration, and rollback. ADR-0029 adopts those rules; ADR-0038
constrains frozen-topology corrections. This README changes neither decision.

## 4. Default posture

Unexpected material is **drift requiring review**, not admitted evidence or a
release. Do not load, index, publish, export, or cite it as canonical. Preserve
identity and provenance before remediation. Unclear rights, sovereignty,
sensitivity, protected locations, living-person/DNA information, or private-land
details require restricted handling, not copying into public PRs or receipts.

## 5. Allowed contents

Retain the **existing** README and zero-byte `.gitkeep` while containment remains
in force. Link to migration, drift, correction, and rollback records in their
actual owning homes.

Do **not** add `MIGRATION.md`, `DRIFT.md`, `OPEN-QUESTIONS.md`, additional
placeholders, or a second writable manifest here. Earlier suggested files were
proposals, not exceptions to the adopted freeze.

## 6. Forbidden contents

No catalog, registry, receipt, proof, release, policy, schema, semantic-contract,
or lifecycle payload belongs in this deprecated directory. It also does not own
producer code, validators, pipeline outputs, generated indexes, tiles, exports,
AI responses, credentials, or sensitive source material.

Use the responsibility routing in §2 and the governing root's README. A new
filename, digest, signature, passing check, or generated manifest cannot grant
source admission, policy clearance, evidence closure, review, or release state.

## 7. Directory shape

**CONFIRMED tracked inventory at the evidence snapshot:**

```text
catalog/manifest/
├── .gitkeep                  # existing zero-byte placeholder; not authority
└── README.md                 # existing deprecated manifest navigation boundary
```

The retained placeholder is blob
`e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`; the pre-edit README is blob
`9fe630fe18decc275d26ad99c5c7e2ac215d18ca`. There are no tracked manifest payloads
in this subtree. This does not prove zero consumers or completed migration.

## 8. Minimum safe redirect slice

Preserve the canonical pointers, stable anchors, no-payload boundary, frozen-root
posture, and explicit unknowns. Keep any generated-work receipt under the existing
[receipt lane](../../data/receipts/generated/README.md), not here. Neither the
README nor its receipt is a policy decision, evidence proof, or release approval.

## 9. Diagram

```text
Legacy navigation: catalog/manifest/README.md
                   -> data/catalog/README.md  (catalog projections)
                   -> release/README.md       (release-governance records)
                   Documentation links only; no data transfer or publication.

Governed lifecycle: RAW -> WORK / QUARANTINE -> PROCESSED
                       -> CATALOG / TRIPLET -> PUBLISHED
```

EvidenceRef -> EvidenceBundle resolution, rights/sensitivity checks, validation,
provenance/integrity, receipts/proofs, policy, review, release, correction, and
rollback remain separate requirements. Maps, tiles, graphs, indexes, scenes,
summaries, and AI remain downstream carriers, not truth authorities.

## 10. Migration posture

First inventory discovered paths, bytes, hashes, source roles, rights, sensitivity,
writers, consumers, and existing references. Classify responsibility before
selecting a destination. Obtain the applicable accepted decision and record the
migration in its owning lane before moving or regenerating anything.

A reviewed migration preserves or explicitly versions identity, retains source
and transform lineage, cuts producers to the canonical writer, validates consumer
parity, and supplies correction and rollback evidence. Destructive cleanup comes
last. This README performs no migration, deletion, source admission, or retirement;
a file move is not lifecycle promotion.

## 11. Runtime and producer anti-bypass matrix

| Risk | Required boundary | Evidence needed before claiming closure |
|---|---|---|
| Producer targets `catalog/manifest/` | Reject new durable output here | Producer configuration, negative test, and exact-run result |
| Public API, map, search, export, or AI treats legacy content as authority | Deny or use the governed released path | Consumer trace and applicable evidence, policy, and release records |
| Catalog inventory is mistaken for a release decision | Preserve catalog/release responsibility separation | Matching object contracts, identity, and actual decision records |
| An imagined `data/catalog/manifest/` becomes a default writer | Do not create authority through naming | Accepted placement and current target/consumer evidence |
| Earlier downstream use is discovered | Preserve correction and rollback lineage | Affected-consumer inventory and reviewed remediation |

These are obligations, not claims that comprehensive runtime enforcement or a
producer/consumer audit has passed.

## 12. Inspection path

Run these read-only commands from an actual checkout. They inspect tracked state,
not live manifests or release readiness. Change `REF` only for a deliberate new
snapshot review.

```bash
REF=832d15769f142f70b0065c9b8c45a7b3e4cd5c10

git rev-parse --verify "${REF}^{commit}"
git ls-tree -r --long "$REF" -- catalog/manifest/
git ls-tree "$REF:data/catalog"
git show "${REF}:control_plane/repository_topology_correction_register.yaml"

# Candidate references, not proof of producer or consumer behavior.
git grep -n -F 'catalog/manifest' "$REF" -- .
```

`git grep` normally exits `1` for no matches; a fatal Git error is not an empty
inventory. These commands cannot inspect untracked files, external stores,
runtime mounts, browser caches, or deployed configuration. Listing commands here
does not claim they ran in a local checkout during this revision.

## 13. Validation expectations

**Review validation is not integration authorization.** Check exact base/head and
diff scope, retained headings/anchors, relative links, balanced fences, UTF-8,
final newline, sensitive-content absence, and the receipt's
[current schema](../../schemas/contracts/v1/receipts/generated_receipt.schema.json)
and final content hash. Record actual outcomes in the PR; this checklist is not
a passing test report.

For frozen-root integration, ADR-0038 explains that `KFM-TOPO-004` fingerprints
`path@object_id`. **This README replacement introduces a new blob delta.** It must
not be relabeled as wholly inherited drift or waived because it is documentation.
The inspected correction register authorizes no transition for this path.

Keep the topology validator, baseline, and correction register unchanged.
Integration remains held pending separately accepted exact authority and the
required trusted-base validation. A draft PR, generation receipt, mergeability
signal, or green unrelated check does not satisfy that gate.

## 14. Safe change pattern

Re-pin `main`, target bytes, applicable decisions, and overlapping work. Prepare
only the bounded README correction and its generated-work receipt, preserving
path, document ID, anchors, `.gitkeep`, and all unrelated content. Follow the
[current contributor controls](../../CONTRIBUTING.md); branch authoring does not
authorize ready-for-review, approval, merge, or public effects.

## 15. Rollback and correction posture

Before integration, retain the unmerged candidate or append a non-force revert
on its task branch. The exact prior README blob is recorded in §7. Keep the
receipt as historical process memory rather than rewriting its artifact hash to
claim it describes different bytes.

After any authorized integration, reverting frozen content is itself a reviewed
transition. Re-check current authority and bytes. Never erase correction history,
restore known damage, or reopen parallel writers just to match an old fingerprint.
No data, release, runtime, or deployment rollback is performed by this document.

## 16. Safe language rules

| Avoid | Use instead |
|---|---|
| “The canonical manifest lives here” | “This is deprecated navigation to the owning catalog or release family” |
| “No manifests exist” | “No tracked manifest payload exists in this pinned subtree” |
| “The canonical path is public” | “Public access still requires governed release and access checks” |
| “ADR-0038 allows this edit” | “Its accepted mechanism does not authorize this unregistered exact transition” |
| “CI passed” without a matching result | Name the executed check, exact scope, result, and limitations |

## 17. Definition of done

For the **README draft**: accurate responsibility routing, confirmed bounded
inventory, preserved identity and anchors, inherited freeze semantics, documented
validation, a hash-matching receipt, and explicit integration blockers.

For **integration or retirement**: additionally require the applicable accepted
exact transition, trusted-base checks, human review, and writer/consumer,
migration, correction, and rollback closure where relevant. Draft completion is
not integration, retirement, runtime readiness, or publication.

## 18. Open verification items

| Item | Status and first affected transition |
|---|---|
| Accepted, bound exact transition for this replacement | **NEEDS VERIFICATION / HOLD integration**; absent from the inspected register |
| Exact-head hosted checks and independent human review | **NEEDS VERIFICATION** before readiness or integration claims |
| External bytes, active writers/consumers, and operational enforcement | **UNKNOWN**; blocks migration/retirement and exposure claims |
| Dedicated catalog-manifest sublane and final release-family convention | **NEEDS VERIFICATION** before creating paths or asserting final conventions |
| Specialist stewardship, retention, correction propagation, and rollback drills | **NEEDS VERIFICATION**; repository routing is not independent approval |

<details>
<summary>Appendix A — no-loss preservation note</summary>

Version v0.3.0 preserves the catalog/release distinction, trust-family separation,
public-boundary rules, lifecycle law, migration and rollback requirements,
document ID, top anchor, and numbered section headings. It replaces stale
inventory uncertainty with the verified two-file tree, removes obsolete proposals
to add files beneath the deprecated root, and identifies the exact-transition
integration hold. Historical v0.2 bytes remain available at the pinned prior blob.
No manifest specification, authority decision, or runtime capability is added.

</details>

## Status summary

**Deprecated navigation, not a manifest store.** Catalog projections and release
records remain in their separate governed homes. This proposed documentation
correction does not authorize its own integration or any data publication.

[Back to top](#top)

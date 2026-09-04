<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/catalog-publication-readme
title: catalog/publication/ — Deprecated Publication Compatibility Redirect
type: readme; deprecated-boundary; compatibility-redirect
version: v0.3.0
status: draft; repository-grounded; deprecated; redirect-only; integration-hold
owners: ["@bartytime4life"]
owner_scope: repository review route from the Root Registry; specialist stewardship and independent approval remain NEEDS VERIFICATION
created: 2026-06-16
updated: 2026-09-04
policy_label: public-doc; no-payload-publication; fail-closed
owning_root: catalog/
root_class: deprecated
readme_profile: BOUNDARY_COMPACT
published_artifact_home: data/published/
release_decision_home: release/
inherited_root_target: data/catalog/
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: 832d15769f142f70b0065c9b8c45a7b3e4cd5c10
  prior_readme_blob: 7f37e6efab211e63eb3ae237adda8551dd640afd
  publication_tree: 8857c9b4245b17478a8c2df28e2b8fe789e7d9b4
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  root_registry_blob: 024f668b5f0a9239bafa4f8b09e2afd86300ff8c
truth_posture: CONFIRMED tracked inventory and adopted placement; PROPOSED README correction; UNKNOWN external consumers and runtime state
related:
  - ../README.md
  - ../../data/published/README.md
  - ../../release/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/adr/ADR-0038-trusted-base-topology-correction-transitions.md
  - ../../control_plane/root_registry.yaml
  - ../../control_plane/repository_topology_correction_register.yaml
  - ../../data/receipts/generated/README.md
tags: [kfm, publication, release, deprecated, compatibility, redirect-only, frozen-no-writes]
notes:
  - "Preserves the existing document ID, top anchor, H1, and numbered section anchors."
  - "Removes obsolete permission to create notes, placeholders, or payloads under this frozen root."
  - "The root catalog target does not collapse publication, release, receipt, proof, and registry responsibilities."
  - "This candidate does not authorize its own frozen-root blob replacement or any release."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Publication Compatibility Redirect

**Looking for released artifacts? Start with [data/published/](../../data/published/README.md).
Looking for the decision that permits release? Use [release/](../../release/README.md).**

`catalog/publication/` is retained navigation beneath the **deprecated, frozen**
[`catalog/` root](../README.md). It is not a publication queue, public download
location, release service, or producer output directory. This README provides
links and containment guidance, not an HTTP redirect, filesystem alias, or
working publication endpoint.

> [!IMPORTANT]
> A catalog entry, digest, generated receipt, rendered map, successful check,
> pull request, or merge is not publication approval. Public clients use governed
> APIs and released, public-safe carriers; they never gain direct access to
> RAW, WORK, QUARANTINE, internal catalog stores, or unreleased candidates.

> [!WARNING]
> **Draft correction; integration held.** Replacing this README changes a blob
> covered by the frozen-root topology rule. No accepted exact transition for
> this path was found in the inspected correction register. Keep the validator,
> baseline, and register unchanged; see [validation expectations](#13-validation-expectations).

## Quick jump

[Evidence](#0-evidence-basis-for-this-revision) ·
[Canonical homes](#2-canonical-homes) ·
[Allowed contents](#5-allowed-contents) ·
[Inventory](#7-directory-shape) ·
[Inspection](#12-inspection-path) ·
[Validation](#13-validation-expectations) ·
[Rollback](#15-rollback-and-correction-posture) ·
[Open verification](#18-open-verification-items)

## 0. Evidence basis for this revision

Reviewed on **2026-09-04** against
[`main@832d15769f142f70b0065c9b8c45a7b3e4cd5c10`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/commit/832d15769f142f70b0065c9b8c45a7b3e4cd5c10).
These are pinned observations, not claims about later `main`.

| Evidence | Confirmed scope | Limit |
|---|---|---|
| `catalog/publication/` tree `8857c9b4245b17478a8c2df28e2b8fe789e7d9b4` | Exactly the README and an empty `.gitkeep`; no tracked payload or child directory | Does not inventory ignored, untracked, cached, mounted, or external bytes |
| [Parent README](../README.md), blob `44378e14fe7470f19df20ebfc9914ad1e3d2a6a9` | Deprecated containment and retained redirects; no new placeholders | Its older operational snapshot is not a current producer/consumer audit |
| [Root Registry](../../control_plane/root_registry.yaml), blob `024f668b5f0a9239bafa4f8b09e2afd86300ff8c` | `root.catalog`: deprecated, immutable, `frozen_no_writes`, `redirect_only`; root target `data/catalog/` | Projection only; no write, migration, or publication permission |
| [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) and [Directory Rules](../../docs/doctrine/directory-rules.md) | Accepted adoption of rules blob `fd49a0b83e55cef52c1124281f093e263526898d` | The rules' retained internal draft label does not undo their exact-byte adoption |
| [Published-artifact README](../../data/published/README.md), blob `8ecb5d2f9737349fb6569efbde36659f398de151` | Describes release-approved public-safe carriers | Does not prove an actual release, hosted payload, or working delivery path |
| [Release README](../../release/README.md), blob `60b6a656f8f2b765616bba7223f51c25863c7172` | Separate append-only release, promotion, correction, withdrawal, rollback, and signature decision plane | Historical fixture/workflow claims are not revalidated by this README |
| [ADR-0038](../../docs/adr/ADR-0038-trusted-base-topology-correction-transitions.md), blob `79f37be0991b050d8bc9c00991d6db887d343cd7` | Stage 1 trusted-base exact-transition mechanism is accepted | No blanket frozen-root exception; no publication-path transition |
| [Correction register](../../control_plane/repository_topology_correction_register.yaml), blob `b48e8df74a2b9d8c2599ce256ef5156687b98dbf` | One proposed agriculture entry, with null accepted-decision bindings | Not authority for this README replacement |

Drive's *Directory Rules* and the Notion *KFM Repository Workbench* were consulted
as lineage and coordination. The adopted repository decisions govern placement;
coordination summaries, older plans, and this README do not grant acceptance.

## 1. Purpose

Preserve legacy navigation and explain where publication-related work belongs
without creating a second publication or release authority. Inherit the parent
root's containment contract; keep operational and object-family specifications
in their existing owning homes.

## 2. Canonical homes

Classify the object by responsibility and lifecycle, not by a filename containing
“publish,” “manifest,” “proof,” or “release.”

| Object or responsibility | Owning home | Important distinction |
|---|---|---|
| Released, public-safe payloads and delivery sidecars | [data/published/](../../data/published/README.md) | Layers, tiles, PMTiles, reports, stories, API snapshots, and downloads require governed release |
| ReleaseManifest, PromotionDecision, RollbackCard, CorrectionNotice, withdrawal, supersession, or signature decisions | [release/](../../release/README.md) | Decision records are not published payloads |
| Catalog records, indexes, STAC/DCAT/PROV catalog representations, and discovery projections | [data/catalog/](../../data/catalog/) | Discovery is not approval or automatic public access |
| Execution, ingest, transform, validation-run, and generation receipts | [data/receipts/](../../data/receipts/) | Records of what ran are process memory, not proof of truth |
| EvidenceBundle, ProofPack, citation-validation, and claim-support objects | [data/proofs/](../../data/proofs/) | Evidence support does not grant rights or release permission |
| Source, dataset, layer, rights, and sensitivity registry instances | [data/registry/](../../data/registry/) | Registry membership is not source activation or publication |
| Semantic contracts, machine-checkable shapes, normative policy | [contracts/](../../contracts/), [schemas/](../../schemas/), [policy/](../../policy/) | Meaning, shape, and admissibility remain separate |

These are **logical owning homes**, not a requirement to commit large or
restricted payload bytes to Git. Physical storage, approved external locators,
access controls, digests, and retention must follow the applicable contracts and
release records. Synthetic fixtures and upstream source material keep their own
responsibilities; they are not “misplaced publications” merely because they are
outside `data/published/`.

The root registry's generic `catalog/` target, `data/catalog/`, does not route all
publication-related objects into the catalog. Use the family-specific split
above. Concrete schema maturity, emitters, and public endpoints are not asserted
by this routing table.

## 3. Authority boundary

| Concern | Local contract |
|---|---|
| Owner and scope | `catalog/` owns deprecated containment only; this leaf owns no independent publication authority |
| Review route | `@bartytime4life`, from the Root Registry; specialist stewardship and independent approval remain unverified |
| Inputs / outputs | Verified path, placement, and migration facts in; navigation and containment guidance out; no payload or trust-object output |
| Mutation | Frozen; the existence of a README does not authorize its replacement or new sibling files |
| Exposure | Public documentation is not permission to expose underlying internal or unreleased records |
| Retention | Migration-bound; retirement requires accepted decisions and verified writer/consumer closure |

Directory Rules §§16–18 supply the compact boundary profile, direct-child map,
compatibility constraints, and migration discipline. ADR-0038 constrains frozen
content corrections. This candidate changes neither authority.

## 4. Default posture

Unexpected material is **drift requiring review**, not admitted evidence or a
released artifact. Do not load, index, cache, cite, export, tile, or host it as
canonical. Preserve identity and provenance before remediation.

Unclear rights, sovereignty, cultural sensitivity, protected locations, rare
species, living-person/DNA information, infrastructure, or private-land detail
require restricted handling. Quarantine, generalization, redaction, staged
access, or denial must retain the applicable reasons and transform records.
Do not copy sensitive material into public issues, PRs, or generation receipts.

## 5. Allowed contents

Retain only the **existing** redirect README and zero-byte `.gitkeep` while this
path remains under containment. Links may reference migration, drift, correction,
and rollback records in their actual owning homes.

Do **not** add `MIGRATION.md`, `DRIFT.md`, `OPEN-QUESTIONS.md`, new placeholders,
or release/publication records here. The previous edition's suggested files
were proposals, not exceptions to the subsequently adopted freeze. This README
correction itself remains subject to the exact-transition integration gate.

## 6. Forbidden contents

No durable data, registry, receipt, proof, catalog, release, or published payload
belongs here. The destinations in §2 apply only after the object's identity,
lifecycle, rights, sensitivity, and governing authority have been established.

Do not place producer code, publisher configuration, schema/profile definitions,
policy rules, migrations, generated previews, temporary builds, or model output
here. Use the existing implementation, configuration, schema, policy, migration,
and generated-output responsibility roots. A policy *decision instance* is not
normative policy source; follow its contract rather than filing it by name.

A manifest, digest, signature, “public” label, or attractive map cannot convert
an unreviewed candidate into a public-safe release.

## 7. Directory shape

The complete tracked subtree at the evidence commit is:

```text
catalog/publication/
├── .gitkeep     # Existing zero-byte placeholder; no implementation or authority
└── README.md    # Existing documentation redirect; frozen-root correction gated
```

| Entry at the evidence commit | Git blob | Bytes |
|---|---|---:|
| `.gitkeep` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` | 0 |
| Prior `README.md` | `7f37e6efab211e63eb3ae237adda8551dd640afd` | 34,101 |

There are no other tracked descendants in this subtree. This is not proof of
zero historical producers, consumers, external storage, ignored files, mounted
volumes, deployed references, or completed migration.

## 8. Minimum safe redirect slice

| Documentation acceptance condition | Evidence required |
|---|---|
| Accurate navigation | Published carriers point to `data/published/`; decisions point to `release/`; support families stay separate |
| No expansion | Preserve the existing path and placeholder; add no sibling content or operational behavior |
| Truthful inventory | Pin a complete tracked tree; explicitly bound external and runtime unknowns |
| Preserved compatibility | Keep the document ID, `top`, H1, and numbered section anchors |
| Reviewable correction | Final content hash, focused checks, provenance receipt, rollback, and unresolved integration gate are visible |

These conditions make a documentation candidate inspectable. They do not prove
publication controls, zero consumers, or authorized frozen-root integration.

## 9. Diagram

```text
Documentation navigation only:
  catalog/publication/README.md
    -> data/published/README.md  (released carrier responsibility)
    -> release/README.md         (release decision responsibility)
    -> separate catalog, receipt, proof, and registry homes

Governed lifecycle:
  RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED

Before public exposure:
  identity + rights + sensitivity + validation + provenance + integrity
  + EvidenceRef -> EvidenceBundle closure + receipts/proofs
  + policy + review + release decision + correction + rollback
```

The arrows do not implement a transfer, automatic approval, or file-copy release.
Maps, tiles, graphs, indexes, scenes, summaries, and AI remain downstream
carriers, not truth or publication authorities.

## 10. Migration posture

If misplaced material is discovered, inventory exact paths, bytes, hashes,
source roles, rights, sensitivity, writers, consumers, and references first.
Obtain the applicable accepted decision and record the migration in its owning
lane before moving or regenerating anything.

A reviewed migration must preserve identity or explicitly version it, retain
source and transform lineage, verify target and consumer parity, and provide
correction and rollback evidence. Released status must be resolved rather than
inferred from an old location or filename. Moving into `data/published/` is not
promotion; unreleased or uncertain material must not be routed there as released.

No migration, deletion, source admission, release, or retirement is performed by
this README. No new migration document belongs under the frozen legacy path.

## 11. Runtime and producer anti-bypass matrix

| Risk | Required boundary | Evidence before claiming closure |
|---|---|---|
| Generator or publisher targets this legacy path | Reject new durable output here | Producer configuration, negative test, and exact-run result |
| Public API, map, search, export, or AI consumes legacy content as authority | Deny or resolve the governed released path | Consumer trace and applicable policy/release evidence |
| Canonical logical home is mistaken for public access permission | Keep internal and unreleased stores inaccessible | Serving configuration and public-boundary checks |
| A copied preview, digest, or signature is called a release | Require evidence, policy, review, and actual release state | Bound decision and integrity records |
| Generalized output leaks protected detail through metadata | Apply sensitivity controls to payloads and sidecars | Reviewed transform and reconstruction-risk checks |
| Prior downstream use is discovered | Preserve correction, invalidation, and rollback lineage | Affected-consumer inventory and reviewed remediation |

This is an obligation matrix, not a report that runtime enforcement or a
comprehensive producer/consumer audit passed.

## 12. Inspection path

From an actual checkout containing the evidence commit, these commands inspect
tracked history without publishing or modifying repository content:

```bash
REF=832d15769f142f70b0065c9b8c45a7b3e4cd5c10

git rev-parse --verify "${REF}^{commit}"
git ls-tree -r --long "$REF" -- catalog/publication/
git show "${REF}:control_plane/root_registry.yaml"
git show "${REF}:control_plane/repository_topology_correction_register.yaml"

# Candidate references only: a text match is not proof of an active consumer.
git grep -n -F 'catalog/publication' "$REF" -- .
```

A no-match `git grep` result normally exits `1`; a fatal Git error is not an empty
inventory. Tracked-text search cannot inspect deployed configuration, ignored
files, mounts, external stores, or browser caches. Listing these commands does
not claim a local checkout or that they ran for this revision; the evidence
above came from pinned GitHub file and tree reads.

## 13. Validation expectations

**Documentation checks and integration authorization are separate.** Check
exact base/head and the complete diff, retained anchors, relative-link targets,
valid metadata, tables and fences, final newline, sensitive-data exclusion,
and the generation receipt's schema and final artifact hash. Report executed,
unavailable, pending, and not-run checks in the PR; do not turn this checklist
into a passing test report.

[ADR-0038](../../docs/adr/ADR-0038-trusted-base-topology-correction-transitions.md)
records that `KFM-TOPO-004` fingerprints frozen evidence as `path@object_id`.
Replacing this README therefore introduces a **new publication-path blob delta**
even though the path set does not grow. The inspected
[register](../../control_plane/repository_topology_correction_register.yaml)
contains only a proposed agricultural transition and cannot authorize this one.

Do not label this delta wholly inherited, waive it as “docs-only,” update the
baseline, suppress a finding, or add same-change authority to approve it.
Integration stays held pending separately accepted exact-transition authority
and the required trusted-base validation. A draft PR, valid receipt, previous
sibling merge, or advisory passing check does not close that gate.

## 14. Safe change pattern

Re-pin current `main`, target bytes, adopted decisions, and overlapping work.
Prepare only the bounded README correction and its new provenance receipt in
[data/receipts/generated/](../../data/receipts/generated/README.md), outside the
frozen root. Preserve the existing path, document identity, and anchors.

Keep the candidate distinct from accepted implementation. Follow the current
[contributor contract](../../CONTRIBUTING.md) and
[PR template](../../.github/PULL_REQUEST_TEMPLATE.md); separate generation,
validation, human review, ready/merge, release, and publication. An incident-held
PR-delivery path does not become eligible merely because the content is useful.

## 15. Rollback and correction posture

Before integration, leave the candidate unmerged or append a non-force revert
on its task branch. The exact prior README blob is in §7; the empty `.gitkeep`
and all payloads remain untouched. Keep the generated receipt as historical
process memory rather than rewriting it to claim a different content hash.

After any authorized integration, a frozen-content revert is itself a reviewed
transition. Re-check current authority and exact bytes; preserve correction
history and consumer obligations. Do not reopen parallel writers, erase audit
records, or restore damaged content merely to match a baseline fingerprint.

## 16. Safe language rules

| Avoid | Use instead |
|---|---|
| “Published from `catalog/publication/`” | “This path is a deprecated documentation redirect” |
| “No publication data exists” | “No tracked payload exists in the pinned publication subtree” |
| “The catalog approved release” | “Catalog discovery and release decisions have separate owners” |
| “The canonical location is public” | “Public exposure still requires governed release and access checks” |
| “Migration or enforcement is complete” | Identify the verified scope and retain unverified consumers or runtime checks |
| “ADR-0038 permits this edit” | “The accepted mechanism does not authorize this unregistered transition” |
| “CI passed” without exact-head evidence | Name the actual check, scope, result, and limitations |

## 17. Definition of done

For the **README candidate**, completion means correct navigation, confirmed
bounded inventory, adopted freeze semantics, preserved identity and anchors,
focused validation, a hash-matching provenance receipt, and explicit integration
blockers. Human review remains pending until an authorized reviewer acts.

For **integration, migration, or retirement**, require their separate accepted
exact transitions and validation, verified writer/consumer closure where
applicable, reviewed correction/rollback support, and current delivery controls.
Those later outcomes cannot be checked off by this documentation update.

## 18. Open verification items

| Item | First affected transition | Required evidence |
|---|---|---|
| Exact accepted correction for this README | Frozen-root integration | Trusted-base authority bound to this path, old/new blobs, and full evidence fingerprints |
| Current exact-head checks and qualifying review | Readiness / merge | Actual run results, failure attribution, reviewer disposition, and eligible delivery path |
| Historical and live producers/consumers, including external references | Migration / retirement | Bounded configuration and runtime inventory, then verified closure |
| Rights, sensitivity, integrity, evidence, policy, and release closure for actual artifacts | Public exposure | Applicable contracts, validated records, review, correction, and rollback support |
| Operational publication, invalidation, correction propagation, and rollback | Release / operation | Authenticated execution and consumer-parity evidence |
| Named specialist stewards and independent duties | Policy-significant approval | Explicit assignments and qualifying review, not assumed identities |

<details>
<summary>Appendix A — no-loss preservation note</summary>

This revision retains the original publication/release/catalog/receipt/proof/
registry split, default-deny public boundary, sensitivity posture, migration and
rollback obligations, document ID, H1, `top`, and all numbered section anchors.
It replaces the stale unknown tracked inventory with an exact two-file snapshot,
removes obsolete proposed sibling files, and replaces the ambiguous transfer
diagram with documentation navigation and a separate governed lifecycle.
Repeated tables and badges are consolidated; no payload, schema, policy,
validator, baseline, registry, release, runtime, or publication state is changed.

</details>

## Status summary

`catalog/publication/` remains deprecated, frozen navigation. Released carriers
belong to `data/published/`; release decisions belong to `release/`; catalog,
receipt, proof, and registry responsibilities remain separate. This is a
reviewable documentation correction, not authority to integrate frozen bytes,
migrate material, approve a release, or expose data.

[Back to top](#top)

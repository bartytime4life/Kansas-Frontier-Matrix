<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/catalog-proof-readme
title: "catalog/proof/ — Deprecated Proof Compatibility Redirect"
type: readme; deprecated-containment; compatibility-redirect
version: v0.3.0
status: proposed documentation correction; redirect-only; frozen-root merge gate unresolved
owners: "NEEDS VERIFICATION — proof, evidence, receipt, catalog, release, policy, and documentation stewards"
created: 2026-06-16
updated: 2026-09-04
policy_label: public documentation only; no payload or access authorization
current_path: catalog/proof/README.md
owning_root: catalog/
root_class: deprecated
canonical_proof_target: data/proofs/
parent_catalog_target: data/catalog/
truth_posture: "CONFIRMED pinned repository evidence; PROPOSED documentation correction; UNKNOWN runtime and external state; NEEDS VERIFICATION merge authorization and retirement closure"
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: 832d15769f142f70b0065c9b8c45a7b3e4cd5c10
  base_tree: 4c9f9a8dee75fe56df49362e86daeb57fcc68980
  prior_blob: 2e602944895f26229f41db2b17a603a4be4fafc1
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_decision: ADR-0029 accepted
  correction_register_blob: b48e8df74a2b9d8c2599ce256ef5156687b98dbf
  tracked_readmes: 3
  tracked_empty_placeholders: 2
  other_tracked_blobs: 0
  method: pinned file reads and complete child Git trees; no runtime inspection
related:
  - ../README.md
  - release/README.md
  - release-closure/README.md
  - ../../data/proofs/README.md
  - ../../data/receipts/README.md
  - ../../data/catalog/README.md
  - ../../data/published/README.md
  - ../../release/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../docs/adr/ADR-0038-trusted-base-topology-correction-transitions.md
  - ../../control_plane/repository_topology_correction_register.yaml
notes:
  - "Same-path documentation proposal; no migration, new files, authority transition, release, deployment, promotion, or publication."
  - "Preserves the document identity and existing section anchors; supersedes v0.2's speculative file-growth guidance, not governing decisions."
  - "The existing agriculture-only proposed correction entry does not authorize this README replacement."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Proof Compatibility Redirect

`catalog/proof/` — **deprecated containment, not a proof store**

Use [`data/proofs/`](../../data/proofs/README.md) for governed proof support, [`data/receipts/`](../../data/receipts/README.md) for process memory, [`data/catalog/`](../../data/catalog/README.md) for catalog projections, and [`release/`](../../release/README.md) for release decisions. This path preserves legacy navigation without becoming a second authority.

> [!IMPORTANT]
> Accepted **ADR-0029** adopts Directory Rules v2. Section 7.3 freezes `catalog/` writes while preserving redirect documentation during migration. This existing README is a **proposed containment correction**, not permission to reopen the root, add placeholders, or store trust-bearing content.

> [!WARNING]
> **Merge gate unresolved at the pinned snapshot.** ADR-0038 accepts a trusted-base exact-transition mechanism, but its current proposed register entry names only `catalog/domain/agriculture/README.md` and has null acceptance bindings. It does not authorize this README replacement. Do not weaken the topology ratchet, refresh its baseline, or edit an authority input to make this change authorize itself. See [validation expectations](#14-validation-expectations).

## Quick jump

[Evidence](#0-evidence-basis-for-this-revision) · [Canonical homes](#2-canonical-homes) · [Allowed contents](#5-allowed-contents) · [Tracked inventory](#7-directory-shape) · [Children](#8-child-redirect-lanes) · [Inspection](#13-inspection-path) · [Validation](#14-validation-expectations) · [Rollback](#16-rollback-and-correction-posture) · [Open verification](#19-open-verification-items)

## 0. Evidence basis for this revision

**Reviewed:** 2026-09-04 against [`main@832d15769f142f70b0065c9b8c45a7b3e4cd5c10`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/commit/832d15769f142f70b0065c9b8c45a7b3e4cd5c10). Relative links are navigation; this immutable commit bounds the observations below.

| Evidence | Confirmed observation | Limit |
|---|---|---|
| [Parent containment README](../README.md), [Directory Rules](../../docs/doctrine/directory-rules.md), and [accepted ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | `catalog/` is deprecated containment, not a canonical catalog or proof root. The adopted rule freezes writes and preserves redirects pending retirement. | Maintaining a draft does not authorize a frozen-root merge, migration, or deletion. |
| Pinned `catalog/proof/` listing and complete child Git trees | Three READMEs and two zero-byte `.gitkeep` files; no other tracked blobs. | No conclusion about ignored, untracked, historical, external, cached, or runtime-held material. |
| [Proof](../../data/proofs/README.md), [receipt](../../data/receipts/README.md), [catalog](../../data/catalog/README.md), [release](../../release/README.md), and [published](../../data/published/README.md) guidance | These families have separate responsibilities and public-access boundaries. | Their presence does not prove payload validity, operational enforcement, or release readiness. |
| Exact reads of `data/proofs/release/README.md` and `data/proofs/release-closure/README.md` | Both returned not found at the pinned commit. | Do not infer that release-support proofs are absent elsewhere, or create those sublanes from this README. |
| [ADR-0011](../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md) | The detailed receipt/proof/manifest/catalog decision remains `proposed`. | This README does not accept it; adopted Directory Rules remain the placement authority. |
| [ADR-0038](../../docs/adr/ADR-0038-trusted-base-topology-correction-transitions.md) and [correction register](../../control_plane/repository_topology_correction_register.yaml) | Stage 1 mechanism accepted; the sole entry remains proposed, unbound, and agriculture-specific. | No accepted exact transition for `catalog/proof/README.md` was established. |

Notion's *Frozen Catalog Correction-Mechanism Decision Package* and Drive's *Directory Rules* were consulted as coordination and lineage. They do not replace accepted repository authority, current code, or exact GitHub lifecycle evidence. Older snapshot claims in related READMEs remain historical unless reverified here.

## 1. Purpose

Keep a readable destination for legacy proof links, route contributors to the correct responsibility family, and prevent accidental proof-path duplication. The long-term goal is reviewed retirement after migration and zero-producer/zero-consumer evidence—not growth of this subtree.

This document does not create proof objects, accept sources, implement a resolver, run a migration, or demonstrate production enforcement.

## 2. Canonical homes

Choose by **responsibility**, not filename, producer, or the word “proof.”

| Material | Owning location | Boundary |
|---|---|---|
| EvidenceBundle, ProofPack, citation-validation report, integrity or claim-support packet | [`data/proofs/`](../../data/proofs/README.md), under a verified applicable profile | Support for evaluation; neither factual truth nor release approval by placement. |
| RunReceipt, TransformReceipt, validation-execution receipt, redaction or AI process receipt | [`data/receipts/`](../../data/receipts/README.md) | Records what ran; does not independently prove the claim. |
| STAC, DCAT, PROV, CatalogMatrix, and discovery/index projections | [`data/catalog/`](../../data/catalog/README.md) | Discoverability and interoperability do not confer evidentiary or release authority. |
| ReleaseManifest, PromotionDecision, signatures, correction/withdrawal records, rollback cards | [`release/`](../../release/README.md) | Governed decision records remain separate from their supporting proofs and public bytes. |
| Release-approved public-safe carriers | [`data/published/`](../../data/published/README.md) | Only after the applicable release and access checks; never a direct move from this redirect. |

A validation **report supporting a claim** and a validation **receipt recording execution** are not interchangeable. Inspect the governing contract before routing either. The producer does not determine the home: Directory Rules `DIR-SIGNATURE-004` applies.

The parent `catalog/` target is `data/catalog/`; this proof-specific redirect points to **`data/proofs/`**. Do not mechanically replace the prefix and invent a parallel proof home inside `data/catalog/`.

## 3. Authority boundary

`catalog/proof/` owns no evidence, receipt, catalog, policy, release, or public-serving authority. Accepted Directory Rules §7.3 and `DIR-PLACE-006` prohibit treating noncanonical paths as writable alternatives.

Semantic meaning remains with `contracts/`, machine shape with `schemas/`, normative admissibility rules with `policy/`, source/rights/sensitivity registry instances with `data/registry/`, and lifecycle data with their applicable `data/` lanes. This README establishes no new child path in any of those roots.

## 4. Default posture

**Do not write payloads here or consume this subtree as canonical proof.** A legacy link can guide a human to the correct family; it cannot grant access to a protected object.

Public clients, maps, search, exports, and AI must use governed interfaces and released, authorized carriers—not this subtree or unrestricted direct reads of internal `data/proofs/`. Consequential claims resolve `EvidenceRef -> EvidenceBundle` with applicable rights, sensitivity, policy, review, and release checks; otherwise narrow, abstain, deny, or report the failure.

Unclear rights or sensitive precision—including living-person/DNA data, cultural or archaeological material, rare species, private land, and protected infrastructure—requires controlled handling. A public repository path, digest, or convincing generated explanation does not make such material safe.

## 5. Allowed contents

**Preserve existing containment; do not add new files.**

| Existing item | Permitted purpose | What it does not permit |
|---|---|---|
| This README and the two child READMEs | Non-authoritative redirects; a proposed correction may be reviewed subject to the frozen-root gate. | An independent writable documentation, proof, or release home. |
| The two existing empty `.gitkeep` files | Preserve current tracked shape until separately reviewed disposition. | More placeholders, implementation claims, or automatic deletion. |
| Links in existing guidance | Point to records already maintained in their owning roots. | New local migration logs, registries, receipts, or copied authority. |

The former suggestions to add `MIGRATION.md`, `DRIFT.md`, or `OPEN-QUESTIONS.md` are superseded. A migration note is supporting evidence, not an exception to the adopted freeze.

## 6. Forbidden contents

No EvidenceBundles, ProofPacks, attestations, receipts, validation payloads, catalog records, source descriptors, policy decisions, release objects, signatures, or published products belong here. Route them by the distinctions in [canonical homes](#2-canonical-homes), with their own admission and review requirements.

Do not add schemas, contracts, executable policy, producer code, pipeline outputs, caches, tiles, search indexes, model output, credentials, private prompts, unsafe logs, or sensitive source bytes. Existing scaffolding is not an admission decision.

## 7. Directory shape

**Complete tracked subtree at the evidence snapshot:**

```text
catalog/proof/
├── README.md
├── release/
│   ├── .gitkeep              # zero bytes
│   └── README.md
└── release-closure/
    ├── .gitkeep              # zero bytes
    └── README.md
```

| Path relative to `catalog/proof/` | Pinned blob | Bytes |
|---|---|---:|
| `README.md` before this correction | `2e602944895f26229f41db2b17a603a4be4fafc1` | 33,451 |
| `release/README.md` | `f4c07c0e632d01242849b270ced3f81ec2aaa09b` | 32,389 |
| `release-closure/README.md` | `72093f0be53d8bbb9f030aa31c287ceecf4c4990` | 33,144 |
| `release/.gitkeep` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` | 0 |
| `release-closure/.gitkeep` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` | 0 |

The child trees were `329ad8bf77935c017b7048ed2fea413aa96a038c` and `21dc3478acdc91fa2a676c9e23d05a444995fd6f`, respectively; both recursive responses were untruncated. This is a tracked-tree observation, not a zero-consumer or runtime-isolation claim.

## 8. Child redirect lanes

| Existing child | Follow this responsibility | Do not infer |
|---|---|---|
| [Release proof redirect](release/README.md) | `data/proofs/` for support; `release/` for the decision. | That `data/proofs/release/` is an admitted destination. |
| [Release closure redirect](release-closure/README.md) | Keep proof support, process receipts, catalog closure, and release decisions in their respective families. | That `data/proofs/release-closure/` exists or that closure is operationally proven. |

Their July 2026 guidance remains unchanged in this one-file correction. Its generic “ADR/migration note” wording cannot override the adopted freeze or the exact-transition requirement. Future child-document corrections need their own scoped review and transition evidence.

## 9. Minimum safe redirect slice

The useful bounded result is correct navigation, no new payloads or placeholders, preserved document identity and anchors, and explicit separation between observed inventory and unverified behavior. A readable README does not itself prevent writes.

Keep producer exclusion, public-consumer exclusion, migration completion, and retirement as separate verification tasks. Do not require live source admission or publication merely to review a reversible documentation proposal.

## 10. Diagram

```text
Legacy catalog/proof/ reference
  -> classify the referenced object's responsibility
     -> proof support ................ data/proofs/
     -> execution receipt ............ data/receipts/
     -> catalog projection ........... data/catalog/
     -> release/correction decision .. release/

No arrow above performs a move, approval, or publication.

RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
                                      governed transition, not a file move
Public use -> governed API / released authorized carrier -> evidence resolution
```

Proof support and receipts support the lifecycle; they do not replace its policy, review, release, correction, or rollback decisions. Maps, tiles, graphs, scenes, indexes, summaries, and AI remain carriers, not root truth.

## 11. Migration posture

If unexpected material is discovered, first stop its use as canonical support and preserve its identity and custody without copying sensitive bytes into a public issue or commit. Record the exact path, digest, producer, consumers, source role, rights/sensitivity uncertainty, and any prior exposure in an appropriate existing record.

Then propose a family-correct migration with accepted authority, producer/consumer changes, validation, correction obligations, and rollback. Move, regenerate, or remove material only within that reviewed scope. Moving bytes does not complete evidence closure or release them.

No payload migration was performed or needed for the **five tracked blobs inspected here**. This does not establish that historical, local, or externally stored drift has been cleared. Retirement still requires zero-producer and zero-consumer evidence plus accepted disposition.

## 12. Runtime and producer anti-bypass matrix

The following are required boundaries, **not claims that enforcement was exercised**:

| Attempt | Required response | Evidence needed |
|---|---|---|
| Producer targets this subtree | Reject the target; choose the owning family and its admitted profile. | Producer configuration and negative path tests. |
| Public client, search, cache, export, or map consumes it as proof | Deny direct canonical use; resolve through a governed interface. | Consumer, delivery, and negative-access checks. |
| Receipt, catalog record, successful check, or model answer substitutes for evidence | Preserve the family distinction; require evidence resolution or abstain. | Contract and boundary tests. |
| Child README or placeholder is treated as destination approval | Keep the root frozen; do not create a new proof lane. | Exact path and accepted decision review. |
| Proposed correction register or refreshed baseline is used as self-authorization | Fail closed; do not suppress or relabel the finding. | Trusted-base, exact-transition, and independent review evidence. |
| Sensitive material is exposed during diagnosis | Use approved restricted handling and safe references. | Rights, sensitivity, and disclosure review. |

## 13. Inspection path

Run these read-only inspections from an actual checkout. The pin below intentionally reproduces this document's snapshot; it is not a substitute for a fresh preflight before later changes.

```bash
BASE=832d15769f142f70b0065c9b8c45a7b3e4cd5c10
git rev-parse HEAD
git ls-tree -r -l "$BASE" -- catalog/proof/
git diff --name-status "$BASE" HEAD -- catalog/proof/
git diff --check "$BASE" HEAD -- catalog/proof/README.md
git grep -n -F 'catalog/proof/' "$BASE" -- .
```

`git grep` returns status 1 when no matches are found; other failures must be investigated. Matches include documentation and fixtures and are not automatically active consumers. Git-tree inspection excludes ignored/untracked files and external systems. These commands are instructions, not execution results from this revision.

## 14. Validation expectations

For this documentation correction, verify metadata, UTF-8, whitespace, Markdown structure, links/anchors, exact file scope, family routing, and the inventory against the pinned tree. Record actual commands, environment, base/head, outputs, and limitations in the PR.

**Frozen-root acceptance is a separate gate.** ADR-0038 documents that `KFM-TOPO-004` fingerprints `path@object_id`. Replacing this README changes frozen-root evidence even if the number of paths is unchanged. An existing failing baseline does not make this additional replacement “inherited only.”

At the snapshot, register entry `KFM-TOPO-004-CORR-4228-01` is `proposed`, names the agriculture README, and has null `decision_ref.blob` and `decision_ref.accepted_commit`. It is not an authorization for this path. A future acceptance route must establish the applicable accepted exact transition and trusted-base enforcement; this README may not implement or waive that route itself.

Do not refresh the topology baseline, alter the correction register, weaken a validator, or bypass a required check to make this PR green. Native topology execution, hosted exact-head checks, and independent review must be reported separately from local Markdown checks. No passing topology, migration, release, or runtime result is claimed here.

## 15. Safe change pattern

Read current main, the whole target, parent/child guidance, applicable instructions, adopted rules, relevant ADRs, and overlapping work before editing. Scope this proposal to the existing README and retain its stable identity and anchors.

Use an isolated branch; recheck current target bytes and overlap before writing and before draft delivery. Report any changed base or governing input. Keep unresolved acceptance gates visible, and stop before ready, merge, migration, source admission, release, deployment, promotion, publication, or settings changes without their separate authority.

## 16. Rollback and correction posture

Before merge, close or withdraw the draft and preserve the branch and reviewed evidence; main need not change. The exact preimage is blob `2e602944895f26229f41db2b17a603a4be4fafc1` at the pinned commit.

After any separately authorized merge, rollback is a reviewed content change subject to the applicable frozen-root transition. Restoring old bytes must not be interpreted as restoring permission to add migration notes or placeholders. Do not delete children, move payloads, mutate release state, or change a baseline as an incidental rollback.

If a misplaced object was previously consumed, preserve its provenance and record correction, withdrawal, cache/export impact, and rollback through the existing responsible systems. Do not erase history to make the directory appear clean.

## 17. Safe language rules

| Avoid | Use instead |
|---|---|
| “Proof authority lives here.” | “This is a deprecated redirect; governed proof support is owned by `data/proofs/`.” |
| “No proof records exist anywhere.” | “The inspected subtree has no tracked payload blobs at this commit.” |
| “The receipt proves the claim.” | “The receipt records execution; the claim still needs admissible evidence.” |
| “Canonical means public.” | “Canonical responsibility does not grant direct public access.” |
| “ADR-0038 permits this edit.” | “Its current entry is unbound and agriculture-specific; this path is not authorized by it.” |
| “Checks pass, so migration/release is complete.” | “Report only the checks actually run and the scope each establishes.” |

## 18. Definition of done

**Documentation review:** one-file diff; correct immutable evidence pin; preserved identity/anchors; verified tracked inventory and navigation; no new storage or authority; explicit frozen-root gate, validation limits, and rollback.

**Merge acceptance:** the applicable accepted correction authority, exact trusted-base transition, current checks, and independent review are established without self-authorization. The author's draft and this section satisfy none of those by themselves.

**Operational retirement:** writers and consumers—including external, hosted, search, cache, export, and AI surfaces—are reconciled; any migration and correction are proven; accepted retirement and rollback evidence exist. No retirement claim is made by this update.

## 19. Open verification items

| Item | Current disposition / first affected transition |
|---|---|
| Exact correction authority for this README | **HOLD before merge acceptance**; no matching accepted transition established at the snapshot. |
| Native and hosted topology validation | **NEEDS VERIFICATION** for the exact change; do not call the new blob replacement inherited-only. |
| Authoritative stewardship and independent review | **NEEDS VERIFICATION**; review routing is not approval. |
| Active producers, consumers, ignored/untracked and external material | **UNKNOWN**; blocks global isolation and retirement claims. |
| Proof-family profiles, schema/validator coverage, and any proposed release-proof sublanes | **NEEDS VERIFICATION** before operational use or path admission. |
| Rights, sensitivity, evidence resolution, and public-access enforcement | **NEEDS VERIFICATION** for any real object; no data admission or public use authorized. |
| Historical migration, correction propagation, and rollback drill | **NEEDS VERIFICATION** before completion or retirement claims. |
| Child README currentness | Their legacy guidance is retained, not adopted as an exception; future corrections require scoped review. |

<details>
<summary>Appendix A — no-loss preservation note</summary>

The prior v0.2 redirect purpose, document ID, original section anchors, proof/receipt/catalog/release separation, deny-by-default access posture, and correction/rollback obligations are retained. The former speculative directory shape and permission to add local notes/placeholders are intentionally replaced by adopted deprecated-root containment and exact tracked inventory. Detailed repetition is consolidated; no payload, producer, consumer, schema, policy, decision, baseline, or child file changes accompany this correction.

</details>

## Status summary

**Observed:** three tracked READMEs, two empty placeholders, and no other tracked blobs in this subtree. **Required:** keep it non-authoritative and frozen; route each family to its owning responsibility. **Proposed:** this documentation correction. **Unresolved:** its exact frozen-root acceptance route, operational enforcement, external dependencies, and retirement.

[Back to top](#top)

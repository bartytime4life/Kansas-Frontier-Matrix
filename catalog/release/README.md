<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/catalog-release-readme
title: catalog/release/ — Deprecated Release Compatibility Redirect
type: readme; deprecated-boundary; compatibility-redirect
version: v0.3.0
status: draft; repository-grounded; deprecated; redirect-only; integration-hold
owners: ["@bartytime4life"]
owner_scope: repository review route only; specialist stewardship and independent approval remain NEEDS VERIFICATION
created: 2026-06-16
updated: 2026-09-04
policy_label: public-doc; no-release-authorization; fail-closed
owning_root: catalog/
root_class: deprecated
readme_profile: BOUNDARY_COMPACT
scope_id: catalog/release/
release_decision_home: release/
published_artifact_home: data/published/
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: bb3eb695e6068b38453ca3ded8f1394a8fdebc20
  prior_readme_blob: 309be86f3c589e47e47f60fbf8e84a40d3832f5b
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  root_registry_blob: 024f668b5f0a9239bafa4f8b09e2afd86300ff8c
truth_posture: CONFIRMED tracked inventory and adopted placement; PROPOSED README correction; UNKNOWN external consumers and operational state
related:
  - ../README.md
  - ../../release/README.md
  - ../../data/published/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/adr/ADR-0038-trusted-base-topology-correction-transitions.md
  - ../../control_plane/root_registry.yaml
  - ../../control_plane/repository_topology_correction_register.yaml
  - ../../data/receipts/generated/README.md
notes:
  - "Retains the existing document ID, H1, top anchor, numbered sections, and status-summary anchor."
  - "Corrects rollback-decision versus rollback-execution-receipt routing."
  - "Removes obsolete permission to add notes, placeholders, or trust objects under the frozen root."
  - "No accepted exact-transition authority for this replacement is supplied by this document."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Release Compatibility Redirect

**Looking for release decisions? Use the [release governance root](../../release/README.md).
Looking for released payloads? Use [data/published/](../../data/published/README.md).**

`catalog/release/` preserves navigation beneath the **deprecated, frozen**
[`catalog/` root](../README.md). It is not a release queue, manifest registry,
rollback service, publisher, or public download endpoint. This is a documentation
redirect, not an HTTP redirect, filesystem alias, or implemented resolver.

> [!IMPORTANT]
> Release decisions, evidence support, execution receipts, and released payloads
> are different object families. A successful check, signature, catalog entry,
> generated receipt, GitHub merge, or file location does not authorize release.

> [!WARNING]
> **Proposed correction; integration held.** Replacing this README changes frozen
> content. The inspected correction register contains no accepted, bound
> transition for this path. Preserve the validator, baseline, and register;
> [validation expectations](#13-validation-expectations) explain the boundary.

## Quick jump

[Evidence](#0-evidence-basis-for-this-revision) ·
[Routing](#2-canonical-homes) ·
[Inventory](#7-directory-shape) ·
[Inspection](#12-inspection-path) ·
[Validation](#13-validation-expectations) ·
[Rollback](#15-rollback-and-correction-posture) ·
[Open verification](#18-open-verification-items)

## 0. Evidence basis for this revision

Reviewed **2026-09-04** against
[`main@bb3eb695e6068b38453ca3ded8f1394a8fdebc20`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/commit/bb3eb695e6068b38453ca3ded8f1394a8fdebc20).
These findings are a pinned snapshot, not claims about future `main`.

| Evidence | Confirmed finding | Limit |
|---|---|---|
| Exact `catalog/release/` listing | Only `README.md` and zero-byte `.gitkeep`; no child directory or tracked payload | Does not inspect ignored, untracked, mounted, or external bytes |
| [Parent README](../README.md), blob `44378e14fe7470f19df20ebfc9914ad1e3d2a6a9` | Deprecated containment; retain existing redirects without growing the root | Its older operational snapshot is not a current consumer audit |
| [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) and [Directory Rules](../../docs/doctrine/directory-rules.md) | Accepted adoption of exact rules blob `fd49a0b83e55cef52c1124281f093e263526898d` | The internal draft label remains inside those adopted bytes |
| [Root Registry](../../control_plane/root_registry.yaml), blob `024f668b5f0a9239bafa4f8b09e2afd86300ff8c` | `root.catalog` is deprecated, immutable, `frozen_no_writes`, and `redirect_only`; root target `data/catalog/` | A projection does not authorize new writes or release |
| [Release README](../../release/README.md), blob `60b6a656f8f2b765616bba7223f51c25863c7172` | Separate append-only decision plane for release, promotion, correction, withdrawal, rollback, and signatures | Does not prove authenticated production release or signing custody |
| [Published-artifact README](../../data/published/README.md), blob `8ecb5d2f9737349fb6569efbde36659f398de151` | Released public-safe payload responsibility is distinct from release decisions | Does not prove a current payload, serving path, or public fitness |
| [ADR-0038](../../docs/adr/ADR-0038-trusted-base-topology-correction-transitions.md), blob `79f37be0991b050d8bc9c00991d6db887d343cd7` | Stage 1 trusted-base exact-transition mechanism accepted | No blanket frozen-root exception |
| [Correction register](../../control_plane/repository_topology_correction_register.yaml), blob `b48e8df74a2b9d8c2599ce256ef5156687b98dbf` | One proposed agriculture-specific entry, with null accepted-decision bindings | No authority for this release README replacement |

Drive's *Directory Rules* and Notion's *Frozen Catalog Correction-Mechanism
Decision Package* were consulted as lineage and coordination. Their historical
repository checkpoints do not supersede fresh GitHub evidence or adopted
repository decisions. Matching blob identities preserve the identity of
previously inspected source bytes; they do not rerun those sources' historical
tests or certify their operational claims.

## 1. Purpose

Keep legacy navigation useful while directing contributors to the responsibility
that actually owns each release-related object. Inherit the parent root's
containment contract rather than creating a second release specification here.

This leaf owns no release state, publication permission, policy, evidence,
signature authority, execution history, or payload. It neither migrates objects
nor proves retirement of historical producers and consumers.

## 2. Canonical homes

Classify by **object responsibility and lifecycle**, not by a filename containing
“release,” “manifest,” “proof,” or “rollback.”

| Object or responsibility | Owning home | Distinction to preserve |
|---|---|---|
| ReleaseManifest, PromotionDecision, release approval, correction, withdrawal, supersession, and signature decision records | [release/](../../release/README.md) | A candidate or stored decision-shaped object is not an effective approval |
| RollbackCard and rollback decisions | `release/`, in the governed rollback-card family | The decision to roll back is not evidence that rollback executed |
| Executed rollback, cache-invalidation, validation-run, generation, and other process receipts | `data/receipts/`, in the applicable receipt family | Records of what ran are process memory, not release authority |
| EvidenceBundle, ProofPack, citation-validation, and claim-support objects | `data/proofs/` | Support for a decision does not replace the decision |
| Released public-safe layers, tiles, PMTiles, reports, stories, API snapshots, and delivery sidecars | [data/published/](../../data/published/README.md) | Payloads require governed release and access checks |
| Catalog records, indexes, and STAC/DCAT/PROV discovery representations | `data/catalog/` | Discovery does not approve publication |
| Source, dataset, layer, rights, and sensitivity registry instances | `data/registry/` | Registration does not activate a source or release data |
| Semantic contracts, machine-checkable shapes, and normative policy | [contracts/](../../contracts/), [schemas/](../../schemas/), [policy/](../../policy/) | Meaning, shape, and admissibility are separate responsibilities |

**Correction to v0.2:** the former table sent a “rollback execution record” to
`release/`. Directory Rules `DIR-RELEASE-003` separates `RollbackCard` decisions
from executed rollback and cache-invalidation process receipts. Route the latter
to the receipt family, not the release decision plane. Likewise, classify a
validation report by its contract: an execution receipt and a proof-support
report must not be collapsed merely because both describe validation.

These are logical owning homes. They do not require large or restricted bytes
to be committed to Git. Approved external storage still needs identity, digest,
access policy, retention, provenance, and correction/rollback references.
Upstream source material and synthetic test fixtures keep their own roles;
they are not misplaced releases merely because they reside elsewhere.

The Root Registry's generic `catalog/` target, `data/catalog/`, does not route
release decisions into the catalog. Follow the family split above and the
canonical release root's current contracts; this README does not settle
singular/plural collection migrations or invent a new child lane.

## 3. Authority boundary

| Concern | Local contract |
|---|---|
| Owning root / local scope | Deprecated `catalog/`; `catalog/release/` is containment documentation only |
| Review route | `@bartytime4life`, from the Root Registry; specialist stewardship and independent approval remain unverified |
| Inputs / outputs | Verified placement, inventory, and migration facts in; navigation and containment guidance out |
| Mutation | Frozen; an existing README is not an automatic exception for replacement or new siblings |
| Exposure | Public documentation does not authorize access to internal decisions, source bytes, or unreleased payloads |
| Retention | Migration-bound; no deletion or retirement without accepted decisions and verified dependency closure |

Directory Rules §16 defines the compact inherited boundary and direct-child
map; §§17–18 govern compatibility, migration, correction, and rollback.
ADR-0029 establishes the adopted edition. ADR-0038 governs exact frozen-content
corrections. This candidate changes none of those authorities.

## 4. Default posture

Unexpected content is **drift requiring review**, not admitted evidence or an
authorized release. Do not cite, load, index, cache, export, tile, host, or use it
to make release decisions. Preserve its identity and provenance before
remediation; location alone does not establish its status.

Unclear rights, sovereignty, cultural sensitivity, living-person/DNA data,
protected locations, archaeology, rare species, infrastructure, or private-land
detail require quarantine, redaction, generalization, staged access, or denial
under the applicable controls. Record reasons and transforms without copying
sensitive payloads into public issues, PRs, or generated-work receipts.

## 5. Allowed contents

Retain only the **existing** README and zero-byte `.gitkeep` while this path
remains under containment. Navigation may point to migration, drift, correction,
and rollback records in their proper governing homes.

Do not add `MIGRATION.md`, `DRIFT.md`, `OPEN-QUESTIONS.md`, new placeholders,
or trust-bearing records here. The previous edition's suggested siblings were
not an exception to the subsequently adopted freeze. This replacement also
remains subject to its own exact-transition integration gate.

## 6. Forbidden contents

No release approvals, manifests, signatures, rollback cards, correction notices,
withdrawals, supersessions, receipts, proofs, registry instances, catalog
records, or published payloads belong here. The owning-home table in §2 is not
permission to move uncertain objects directly into a released lifecycle state.

Producer code, publisher configuration, schemas, normative policy, migration
implementation, generated previews, build output, model output, credentials,
and restricted source material also stay out. Use existing responsibility roots,
not an additional authority hidden under a familiar legacy name.

## 7. Directory shape

**CONFIRMED tracked inventory at the evidence commit:**

```text
catalog/release/
├── .gitkeep     # Existing zero-byte placeholder; no authority
└── README.md    # Existing release navigation; frozen-content correction gated
```

| Entry before this correction | Git blob | Bytes |
|---|---|---:|
| `.gitkeep` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` | 0 |
| `README.md` | `309be86f3c589e47e47f60fbf8e84a40d3832f5b` | 34,115 |

No other tracked descendants were returned. This closes the local tracked-tree
question, not historical migration, ignored-file, external-storage, producer,
consumer, runtime, hosting, or deletion-safety questions.

## 8. Minimum safe redirect slice

The documentation candidate must preserve canonical navigation, exact inventory,
existing identity and anchors, the no-new-content boundary, family separation,
sensitivity controls, and explicit validation/rollback limits. Its generation
receipt belongs in the existing accountability lane outside the frozen root.

A readable README, empty placeholder, valid receipt, or successful formatting
check does not prove that producers, release jobs, or public clients obey the
boundary. Those require their own implementation and execution evidence.

## 9. Diagram

```text
Documentation navigation only:
  catalog/release/README.md -> release/README.md
                           -> data/published/README.md

Distinct responsibilities:
  evidence/proofs + process receipts -> support release review
  release decision                  -> governs released payloads
  RollbackCard                      -> records rollback decision/target
  rollback execution receipt        -> records what the rollback actually did

Governed lifecycle:
  RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

These arrows do not implement transfer or automatic approval. Before release,
require identity, rights, sensitivity, validation, provenance, integrity,
EvidenceRef-to-EvidenceBundle closure, receipts/proofs, policy, review, release
state, correction, and rollback support. Maps, tiles, graphs, indexes, scenes,
summaries, and AI remain carriers, not truth or approval authorities.

## 10. Migration posture

First inventory exact paths, bytes, hashes, identities, source roles, rights,
sensitivity, producers, consumers, and downstream references. Obtain the
applicable accepted decision and record the migration in its owning lane before
moving, regenerating, deleting, or changing consumers.

A migration preserves identity or explicitly versions it, maintains source and
transform lineage, validates target and consumer parity, and retains correction
and rollback evidence. Decisions route to `release/`; execution receipts route
to their receipt family; already released payloads require verified release
state before placement under `data/published/`. Unreleased candidates do not
become published through a file move.

No migration, source admission, release, deletion, or retirement is performed by
this README. Existing placeholders remain unchanged.

## 11. Runtime and producer anti-bypass matrix

| Risk | Required boundary | Evidence before claiming closure |
|---|---|---|
| Producer targets `catalog/release/` | Reject new durable output here | Producer configuration, negative test, and exact-run result |
| Rollback execution receipt is treated as rollback approval | Keep decision and execution identities separate | Contract-aligned objects and negative family-substitution checks |
| Public client, map, search, export, or AI reads legacy content as authority | Deny; resolve governed APIs or released public-safe artifacts | Consumer trace plus applicable policy/release evidence |
| Signature, digest, or green check is treated as release permission | Require the actual authorized decision and closure | Bound review, policy, identity, and release records |
| Generalized payload leaks restricted detail through sidecars | Apply sensitivity controls to both payload and metadata | Transform review and reconstruction-risk checks |
| Historical drift was consumed downstream | Preserve correction, invalidation, and rollback obligations | Affected-consumer inventory and reviewed remediation |

This matrix states obligations. It does not report that runtime enforcement,
all producer exclusions, or a comprehensive consumer audit passed.

## 12. Inspection path

From a checkout containing the evidence commit, these commands inspect tracked
history without changing content or performing a release:

```bash
REF=bb3eb695e6068b38453ca3ded8f1394a8fdebc20

git rev-parse --verify "${REF}^{commit}"
git ls-tree -r --long "$REF" -- catalog/release/
git show "${REF}:control_plane/root_registry.yaml"
git show "${REF}:control_plane/repository_topology_correction_register.yaml"

# Candidate references, not proof of an active writer or consumer.
git grep -n -F 'catalog/release' "$REF" -- .
```

A no-match `git grep` result exits `1`; a fatal Git error is not an empty
inventory. Tracked-text searches do not inspect deployed configuration, ignored
files, external stores, mounts, or caches. Listing these commands does not claim
they ran: this revision's inventory came from pinned GitHub file/tree reads.

## 13. Validation expectations

Keep documentation validation separate from integration authorization. Check
the exact base/head diff, unchanged placeholder, stable document ID and anchors,
relative destinations, metadata, tables, fences, shell syntax, final newline,
absence of sensitive payloads, and generation-receipt shape and final-byte hash.
Record actual results, limitations, and not-run checks in the review handoff.

[ADR-0038](../../docs/adr/ADR-0038-trusted-base-topology-correction-transitions.md)
preserves `KFM-TOPO-004` evidence identity as `path@object_id`. Replacing this
README introduces a **new release-path blob delta** even with the same path
count. The inspected [register](../../control_plane/repository_topology_correction_register.yaml)
has only a proposed agriculture-specific transition and cannot authorize it.

Do not label this delta wholly inherited, waive it as documentation, refresh the
baseline, suppress the finding, or use a same-change authority input to approve
it. Integration requires separately accepted exact-transition authority and the
required trusted-base validation. Other edits under `catalog/` change the full
frozen evidence set even when they do not touch this leaf; re-pin that shared
set before any later transition. A sibling merge is not an exception.

## 14. Safe change pattern

Re-pin `main`, the target, relevant decisions, and overlapping work. Prepare the
bounded README candidate and its required new provenance record in
[data/receipts/generated/](../../data/receipts/generated/README.md). Preserve the
path, document identity, existing anchors, and placeholder; do not modify the
root classification, correction register, baseline, or validator.

Follow the current [contributor contract](../../CONTRIBUTING.md). Separate
branch authoring, validation, independent review, PR creation, readiness, merge,
release, and publication. An incident-held PR delivery path remains held even
when the candidate is useful; preserve branch progress and a precise handoff
rather than bypassing the [active delivery controls](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4024).

## 15. Rollback and correction posture

Before integration, leave the candidate unmerged or restore only the prior
README in a new, non-force task-branch commit. Preserve the generated receipt as
historical provenance instead of changing its hash to describe another artifact.
The exact prior blob is recorded in §7; it also contains the obsolete sibling-file
permission and rollback-execution routing that this candidate corrects.

After integration, reversal is itself a frozen-content transition requiring
current authority and review. Do not automatically restore old mistakes, erase
history, reset a shared branch, or reopen parallel writers merely to match a
baseline. Real release rollback additionally needs its own decision, execution
receipt, affected-consumer verification, correction, and cache-invalidation
support. A README revert proves none of those operational outcomes.

## 16. Safe language rules

| Avoid | Use instead |
|---|---|
| “Release truth lives here” | “This path preserves deprecated release navigation” |
| “The rollback receipt approved rollback” | “The decision authorizes; the receipt records execution” |
| “No release material exists anywhere” | “No tracked payload exists in this pinned subtree” |
| “A signed manifest or merge publishes the data” | “Release, policy, review, integrity, and public access still require closure” |
| “The canonical path is public” | “Logical ownership does not confer access permission” |
| “CI blocks this” or “migration complete” | Name the verified scope, execution evidence, and remaining unknowns |
| “ADR-0038 permits this replacement” | “The mechanism does not authorize this unregistered exact transition” |

## 17. Definition of done

For the **documentation candidate**: correct routing, verified bounded inventory,
adopted containment language, preserved identity/navigation, focused validation,
hash-bound provenance, rollback guidance, and explicit integration blockers.
Human review stays pending until an authorized reviewer acts.

For **integration, migration, retirement, or release**: satisfy the separate
accepted decisions, trusted-base transition validation, applicable writer and
consumer closure, review, correction/rollback evidence, and current delivery
controls. Completion of the README candidate cannot check off those outcomes.

## 18. Open verification items

| Item | First affected transition | Evidence required |
|---|---|---|
| Accepted exact correction for this README | Frozen-root integration | Trusted-base binding to path, old/new blobs, and full evidence fingerprints |
| Exact-head validation and qualifying review | Readiness / merge | Actual check results, failure attribution, and reviewer disposition |
| Eligible PR delivery boundary | Draft creation | Current incident controls and independent execution boundary where required |
| Historical/live producers and consumers, including external references | Migration / retirement | Configuration/runtime inventory and verified closure |
| Actual artifact rights, sensitivity, evidence, policy, integrity, and release state | Public exposure | Applicable validated objects, review, and correction/rollback support |
| Signing custody, executed rollback, invalidation, and consumer parity | Operational release | Authenticated execution evidence, not documentation or fixture inference |
| Specialist stewards and independent release duties | Policy-significant approval | Explicit assignments and qualifying review |

<details>
<summary>Appendix A — no-loss preservation note</summary>

This revision retains the release/publication/catalog/receipt/proof/registry
split, default-deny public boundary, sensitivity safeguards, migration and
rollback obligations, document ID, H1, `top`, all 19 numbered sections, and
status-summary anchor. It corrects the execution-receipt routing, replaces the
speculative directory shape with verified inventory, removes obsolete
file-addition permission, and distinguishes documentary completion from later
governed transitions. Repeated badges and tables are consolidated. No payload,
contract, schema, policy, validator, baseline, register, runtime, or release
state is changed by this documentation candidate.

</details>

## Status summary

`catalog/release/` is deprecated, frozen navigation only. Release decisions
belong to `release/`; released payloads belong to `data/published/`; execution
receipts and evidence/proof support retain their separate families. This
candidate is reviewable documentation, not authority to integrate frozen bytes,
approve a release, execute rollback, or expose data.

[Back to top](#top)

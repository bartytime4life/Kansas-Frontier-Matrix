<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/catalog/domain/readme
title: Domain Catalog Compatibility Redirect
type: readme; compatibility-redirect; drift-containment; non-authoritative
version: v0.4.0
status: repository-grounded draft; deprecated-parent; redirect-only; frozen; correction-approval-required
owners: NEEDS VERIFICATION — docs, architecture, catalog/data, affected-family, policy, release, correction, and rollback stewards
updated: 2026-09-04
supersedes: v0.3.0 documentation at the same path after an authorized correction; no authority or lifecycle transition
policy_label: public-review; compatibility-only; fail-closed; no-direct-public-path; correction-aware
current_path: catalog/domain/README.md
owning_root: catalog/
root_class: deprecated
canonical_target: data/catalog/domain/
readme_profile: BOUNDARY_COMPACT
review_packet_id: kfm-catalog-domain-readme-20260904
truth_posture: >-
  CONFIRMED adopted parent classification, complete tracked domain-subtree inventory,
  counterpart paths, and accepted-decision/register contents / PROPOSED README correction /
  UNKNOWN untracked, external, producer, consumer, runtime, and hosting state /
  NEEDS VERIFICATION exact correction authority, native validation, independent review,
  migration, and rollback closure
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: 7187fb20a8c1f9bf838e0f1fd00fb691b378c434
  prior_blob: fd4826b2b5e54672796b840d2664b5947d4054ec
  domain_tree: eaa52fbbc27149b6033e0f738ae5a2339c83567e
  canonical_domain_tree: 7c2dc6cf032333ce21f97eee514d4483d3e9cc1f
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  root_registry_blob: 024f668b5f0a9239bafa4f8b09e2afd86300ff8c
  correction_register_blob: b48e8df74a2b9d8c2599ce256ef5156687b98dbf
  tracked_readmes: 14
  tracked_zero_byte_gitkeeps: 7
  other_tracked_files: 0
  method: immutable GitHub files and complete Git subtree reads; no full checkout or runtime inspection
notes:
  - "Existing headings and anchors are retained for compatibility; Directory Rules section 16.3 supplies the boundary-README profile."
  - "This change is Markdown only and does not migrate or authorize any trust-bearing object."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `catalog/domain/` — Domain Catalog Compatibility Redirect

> **One-line purpose.** Keep historical domain-catalog links usable while directing readers to the governed `data/catalog/domain/` lanes, without reopening the frozen `catalog/` root.

[![Status: deprecated parent](https://img.shields.io/badge/status-deprecated%20parent-b42318?style=flat-square)](#status)
[![Authority: none](https://img.shields.io/badge/authority-non--authoritative-b42318?style=flat-square)](#authority-level)
[![Writes: denied](https://img.shields.io/badge/trust%20writes-denied-b42318?style=flat-square)](#what-does-not-belong-here)
[![Domain redirects: 13](https://img.shields.io/badge/domain%20redirects-13-0969da?style=flat-square)](#current-bounded-inventory)

> [!IMPORTANT]
> **Start at the [canonical domain catalog index](../../data/catalog/domain/README.md).** This page is a navigation-only compatibility redirect beneath the adopted **deprecated** `catalog/` root. It owns no catalog data, source registry, evidence, policy, release decision, or public truth.

> [!CAUTION]
> **Frozen-path correction gate.** Even a README-only replacement changes the frozen `path@object_id` evidence. [ADR-0038](../../docs/adr/ADR-0038-trusted-base-topology-correction-transitions.md) does not authorize this parent README correction: its initial exact transition is limited to the agriculture child. This draft, its PR, and its checks cannot authorize their own merge or amend the freeze. See [Validation](#validation).

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Redirect contract](#redirect-contract) · [Guardrails](#guardrails) · [Migration](#migration-correction-and-rollback) · [Inventory](#current-bounded-inventory) · [Verification](#open-verification-register) · [No-loss](#no-loss-ledger)

## Purpose

This README preserves historical navigation while preventing a legacy location from becoming a parallel catalog authority. Follow the [domain routing table](#current-bounded-inventory) to existing counterpart directories; inspect the counterpart's own contract before using or writing records.

The inherited parent is [`catalog/README.md`](../README.md). The owning root remains `catalog/`, not `data/`; the canonical destination is a redirect target, not a relocation performed by this document. No child file, placeholder, payload, schema, policy, or release record changes with this README.

## Authority level

**CONFIRMED existing path / CONFIRMED adopted deprecated parent / non-authoritative redirect / frozen to new writes.**

Accepted [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the exact [Directory Rules](../../docs/doctrine/directory-rules.md) bytes even though their retained header says `PROPOSED_FOR_ADOPTION`. The active [Root Registry](../../control_plane/root_registry.yaml) projects `root.catalog` as `deprecated`, `immutable`, `frozen_no_writes`, and `redirect_only`, with `data/catalog/` as its target. Neither this README nor that projection can expand the accepted authority.

Object meaning remains under `contracts/`; machine shape under `schemas/`; admissibility under `policy/`; lifecycle catalog and graph projections under `data/`; release decisions under `release/`; implementation under its existing implementation roots. Directory Rules sections 16–18 govern boundary documentation, compatibility, migration, and rollback.

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A catalog record is a carrier, not root truth. Consequential claims resolve `EvidenceRef -> EvidenceBundle`. Public clients use governed APIs and released, public-safe artifacts, never this legacy tree or unreleased canonical stores. A digest, schema pass, green check, PR, merge, map, or AI answer does not confer source, rights, review, or release authority.

## Status

All observations below are bounded to `main@7187fb20a8c1f9bf838e0f1fd00fb691b378c434`.

| Field | Verified result or limit |
|---|---|
| Path / candidate edition | `catalog/domain/README.md` / `v0.4.0` |
| Parent / inherited posture | [`catalog/`](../README.md) / deprecated, immutable, frozen, redirect-only |
| Canonical destination | [`data/catalog/domain/`](../../data/catalog/domain/README.md) |
| Direct child directories | 13 existing domain lanes |
| Complete tracked subtree | 14 README files, including this one; 7 zero-byte `.gitkeep` files; 0 other files |
| Canonical counterparts | All 13 same-slug directories exist; existence is not admission, implementation, or release proof |
| Untracked, ignored, generated, external, or hosted material | `UNKNOWN` — not established by Git tree inspection |
| Active producers / consumers | `UNKNOWN` — no zero-dependency claim |
| Exact correction authority for this README | `NOT ESTABLISHED`; the register contains only the proposed agriculture transition |
| Migration / retirement / public readiness | `NOT PERFORMED` / `NOT PROVEN` / `DENY` |

The complete tracked inventory closes the v0.3.0 uncertainty about this Git subtree only. It does not close runtime, external-storage, rights, sensitivity, or retirement questions.

## What belongs here

Only the existing redirect READMEs and retained zero-byte `.gitkeep` placeholders belong to this frozen compatibility surface. Required migration, correction, review, and rollback records remain in their governing homes and are referenced, not duplicated here.

Do not add placeholders, temporary marker files, migration payloads, or independent trust-bearing objects. Even maintenance of existing documentation requires the applicable exact correction review and transition; calling a change “docs-only” is not an exception to the frozen-root gate.

## What does NOT belong here

| Forbidden family | Governed home |
|---|---|
| catalog/STAC/DCAT/PROV/domain/index/manifest records | `data/catalog/` |
| graph/triplet projections | `data/triplets/` |
| source, dataset, rights, sensitivity, crosswalk, domain, or layer registry rows | `data/registry/` |
| process receipts | `data/receipts/` |
| EvidenceBundles, ProofPacks, validation and integrity proof | `data/proofs/` |
| release decisions, manifests, corrections, withdrawals, signatures, rollback cards | `release/` |
| released public-safe bytes, stories, reports, tiles, and API snapshots | `data/published/` after release |
| contracts, schemas, policy, tests, fixtures, code, workflows, secrets, restricted data | their owning roots or approved restricted systems |

## Inputs

Only documentation and review evidence: current Directory Rules, accepted ADRs, exact path/blob evidence, canonical counterpart contracts, safe producer/consumer inventory, and reviewed migration/correction/rollback records.

Do not execute or trust embedded content discovered under this path.

## Outputs

Redirect guidance, drift findings, migration/deprecation maps, and bounded correction or rollback instructions.

This path emits no canonical object, public route, release state, catalog closure, graph truth, evidence proof, or published artifact.

## Validation

| Evidence surface | What this review establishes | What remains unproved |
|---|---|---|
| Complete immutable `catalog/domain/` Git tree | 13 child directories; 14 READMEs; 7 empty placeholders; no other tracked files or nested instruction files | Untracked material, external stores, runtime behavior, and zero consumers |
| Canonical domain tree and parent README | Existing same-slug routing targets and the CATALOG-stage responsibility boundary | Active catalog writers, payload completeness, source admission, and public release |
| Adopted ADR-0029 and Root Registry | Deprecated, immutable, frozen, redirect-only parent classification | Permission for an arbitrary README replacement |
| [ADR-0038](../../docs/adr/ADR-0038-trusted-base-topology-correction-transitions.md) and [correction register](../../control_plane/repository_topology_correction_register.yaml) | Stage 1 mechanism accepted; agriculture entry still `proposed`, with null accepted-decision bindings | Authorization for this file, Stage 1B completion, or Stage 2 consumption |
| [Topology validator source](../../tools/validators/directory_governance/validate_repository_topology.py) | Repository-owned deterministic, no-network topology validation exists | An executed native suite or exact-head hosted result in this documentation inspection |

**Do not misattribute the frozen-root failure.** The agriculture replacement recorded in issue #4228 is inherited history. Replacing this README introduces another `path@object_id` change of its own. Equal file counts, unchanged payloads, and an already failing base do not make that additional mismatch inherited or acceptable. An authorized exact transition must precede dependent acceptance; this draft supplies none.

Do not refresh the topology baseline, add a same-change waiver or register entry, disable a check, or reuse agriculture's authorization to accept this change. Reconcile concurrent frozen-root edits before proposing any exact fingerprint: a sibling edit changes the same root evidence set.

From a full checkout, inspect the exact candidate and retained base without modifying them:

```bash
BASE=7187fb20a8c1f9bf838e0f1fd00fb691b378c434
git diff --check "$BASE" HEAD -- catalog/domain/README.md
git diff --name-status "$BASE" HEAD
git ls-tree -r --full-tree "$BASE" -- catalog/domain/
git ls-tree -r --full-tree HEAD -- catalog/domain/
```

Before acceptance, verify metadata, Markdown structure, retained anchors, every changed link, exact blob scope, applicable native checks, and base-versus-head findings. Record passing, failing, pending, skipped, and unrun results separately. No full repository suite or runtime test is claimed here.

Before migration or retirement, also inventory producers, consumers, workflows, runtime reads, hosts, caches, indexes, exports, maps, and AI surfaces; verify identity, rights, sensitivity, evidence, policy, review, release, correction, and rollback; and prove zero producers and zero consumers.

## Review burden

The Root Registry names `@bartytime4life` as its owner and review route. Independent docs, catalog/data, architecture, and migration reviewers remain **NEEDS VERIFICATION**; routing is not proof of review or stewardship separation.

This correction needs the frozen-topology review described above. Discovered payloads, sensitive material, producer/consumer changes, migration, or retirement also require the affected family and policy/security, validation, operations, correction, and rollback reviews. This README grants no ready-for-review, merge, source-admission, deployment, or publication authority.

## Related folders

- [Parent deprecated-root containment](../README.md) · [Canonical domain catalog index](../../data/catalog/domain/README.md)
- [Canonical catalog root](../../data/catalog/) · [Canonical triplet root](../../data/triplets/)
- [Receipts](../../data/receipts/) · [Proofs](../../data/proofs/) · [Registry](../../data/registry/)
- [Published artifacts](../../data/published/) · [Release governance](../../release/)
- [Directory Rules](../../docs/doctrine/directory-rules.md) · [Current ADR index](../../docs/adr/INDEX.md)

Links identify responsibility destinations, not permission to copy records, expose internal stores, or promote an artifact.

## ADRs

| Decision | Status at the evidence pin | Relevance and limit |
|---|---|---|
| [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | `accepted` | Adopts Directory Rules; does not authorize this correction, retirement, or physical deletion |
| [ADR-0038](../../docs/adr/ADR-0038-trusted-base-topology-correction-transitions.md) | Stage 1 mechanism `accepted` | Trusted-base exact correction mechanism; initial agriculture transition does not cover this README |
| ADR-0011 and ADR-0022 | `proposed` in the [canonical index](../../docs/adr/INDEX.md) | Separation and catalog-closure proposals; no implied acceptance |

This README accepts no ADR. A root or authority-family transition still requires its own accepted decision, identity and consumer mapping, correction path, rollback plan, and post-transition verification.

## Last reviewed

- **Date:** 2026-09-04.
- **Evidence pin:** `main@7187fb20a8c1f9bf838e0f1fd00fb691b378c434`.
- **Target preimage:** `fd4826b2b5e54672796b840d2664b5947d4054ec`.
- **Inspection:** complete immutable domain subtree, canonical counterpart directory inventory, target and parent READMEs, adopted rules, accepted ADRs, and current machine projection contents.
- **Limits:** no full checkout/native test suite, live runtime, deployment, external-storage inventory, or independent human review.

Re-review on authority or ADR changes, any frozen-root blob change, writer/consumer discovery, changed links or aliases, validation or review-routing changes, and migration/correction/rollback events. Directory Rules section 16.5 uses event- and risk-based review, not the former blanket six-month interval.

## Redirect contract

| Question | Required answer |
|---|---|
| What family is represented? | Explicit object family and source role |
| Where is the governed home? | Exact responsibility/lifecycle root or `NEEDS VERIFICATION` |
| May new writes occur here? | No; documentation maintenance cannot bypass exact correction controls |
| May public clients read here? | No |
| What blocks migration? | Unknown payloads, rights/sensitivity, producers/consumers, unresolved target, missing review |
| What closes migration? | Accepted decision, verified move/regeneration, parity, correction, rollback, zero dependencies |

## Guardrails

| # | Guardrail |
|---:|---|
| 1 | Domain names remain lane segments inside responsibility roots, never new authority roots. |
| 2 | Each domain child preserves its own source-role, time, sensitivity, evidence, and public-safety rules. |
| 3 | The parent must not resolve domain slug conflicts or create missing canonical lanes by assertion. |
| 4 | Cross-domain joins preserve the owning lane for every claim; navigation never grants join authority. |
| 5 | Unclear rights, cultural/sovereignty constraints, protected sites, rare species, infrastructure, private-land precision, living-person or DNA data remain restricted, generalized, quarantined, or denied pending the owning review. |

## Migration, correction, and rollback

1. Freeze current paths, blobs, doctrine, and accepted decisions.
2. Inventory tracked, ignored, generated, hosted, and externally referenced material.
3. Classify every object by responsibility, source role, lifecycle, rights, and sensitivity.
4. Preserve the existing freeze; verify negative validation rather than disabling it.
5. Obtain the separately accepted transition before any move, regeneration, or frozen-path correction; then use a reviewed migration.
6. Validate identity, digest, evidence, policy, release, public-safe transformation, and consumer parity.
7. Correct downstream indexes/caches/exports and preserve lineage.
8. Rehearse rollback without recreating parallel authority.
9. Retire the redirect only after zero-producer, zero-consumer, link, host, and rollback checks pass.

**Candidate rollback:** leave or close the draft unmerged and preserve its branch. If an authorized correction later lands, use a reviewed forward revert or successor correction with fresh exact-transition evidence; do not force-push, rewrite history, automatically restore a frozen blob, or reopen a second writable catalog. The preimage for review is `fd4826b2b5e54672796b840d2664b5947d4054ec`.

## Current bounded inventory

The complete legacy subtree at the evidence pin contains **21 tracked files**: this README, 13 child READMEs, and 7 zero-byte `.gitkeep` placeholders. The seven placeholders are under atmosphere, fauna, flora, geology, habitat, hazards, and hydrology. No other tracked files occur in this subtree.

Direct children only; each existing child README owns deeper compatibility guidance:

```text
catalog/domain/
├── README.md
├── agriculture/
├── archaeology/
├── atmosphere/
├── fauna/
├── flora/
├── geology/
├── habitat/
├── hazards/
├── hydrology/
├── people-dna-land/
├── roads-rail-trade/
├── settlements-infrastructure/
└── soil/
```

| Retained legacy redirect | Existing canonical counterpart directory |
|---|---|
| [`agriculture/`](./agriculture/README.md) | [`data/catalog/domain/agriculture/`](../../data/catalog/domain/agriculture/) |
| [`archaeology/`](./archaeology/README.md) | [`data/catalog/domain/archaeology/`](../../data/catalog/domain/archaeology/) |
| [`atmosphere/`](./atmosphere/README.md) | [`data/catalog/domain/atmosphere/`](../../data/catalog/domain/atmosphere/) |
| [`fauna/`](./fauna/README.md) | [`data/catalog/domain/fauna/`](../../data/catalog/domain/fauna/) |
| [`flora/`](./flora/README.md) | [`data/catalog/domain/flora/`](../../data/catalog/domain/flora/) |
| [`geology/`](./geology/README.md) | [`data/catalog/domain/geology/`](../../data/catalog/domain/geology/) |
| [`habitat/`](./habitat/README.md) | [`data/catalog/domain/habitat/`](../../data/catalog/domain/habitat/) |
| [`hazards/`](./hazards/README.md) | [`data/catalog/domain/hazards/`](../../data/catalog/domain/hazards/) |
| [`hydrology/`](./hydrology/README.md) | [`data/catalog/domain/hydrology/`](../../data/catalog/domain/hydrology/) |
| [`people-dna-land/`](./people-dna-land/README.md) | [`data/catalog/domain/people-dna-land/`](../../data/catalog/domain/people-dna-land/) |
| [`roads-rail-trade/`](./roads-rail-trade/README.md) | [`data/catalog/domain/roads-rail-trade/`](../../data/catalog/domain/roads-rail-trade/) |
| [`settlements-infrastructure/`](./settlements-infrastructure/README.md) | [`data/catalog/domain/settlements-infrastructure/`](../../data/catalog/domain/settlements-infrastructure/) |
| [`soil/`](./soil/README.md) | [`data/catalog/domain/soil/`](../../data/catalog/domain/soil/) |

These links are navigation, not a claim of operating catalog payloads. The canonical parent remains a draft/profile surface, and separately lists `people/` and `settlement/` as conflicted short-segment lanes. Their presence does not make them synonyms or replacements for the full domain slugs. This update neither creates an alias nor repairs or retires those lanes.

## Open verification register

| Item | Status | Required evidence / first blocked transition |
|---|---|---|
| Tracked legacy subtree | `CONFIRMED` at the pin | Re-enumerate if any frozen-root member changes |
| Ignored, untracked, generated, and external material | `UNKNOWN` | Inventory before migration or retirement |
| Producers and consumers | `UNKNOWN` | Code/config/workflow/runtime/host evidence; no zero-dependency assertion |
| Exact correction authority for this README | `NOT ESTABLISHED` | Separately accepted, exact trusted-base transition before dependent acceptance |
| Native and hosted exact-head validation | `NEEDS VERIFICATION` | Actual runs and introduced-versus-inherited attribution; no blanket green claim |
| Canonical child operation and alias closure | `NEEDS VERIFICATION` | Owning contracts, admitted records, writer/consumer evidence, and migration records |
| Rights, sensitivity, independent review, and public effects | `UNKNOWN` / `NEEDS VERIFICATION` | Per-object and reviewer evidence before exposure or promotion |
| Migration, correction, and rollback closure | `NOT PERFORMED` | Reviewed records, parity, zero dependencies, and a rollback drill |

## No-loss ledger

| Prior material | Disposition |
|---|---|
| Stable path and document identity | Preserved |
| Compatibility/non-authority boundary | Preserved and strengthened |
| Canonical routing | Preserved and normalized |
| Domain-specific guardrail requirement | Preserved; child warnings remain subordinate to adopted doctrine, accepted decisions, and canonical contracts |
| Migration, anti-bypass, correction, and rollback posture | Preserved; exact frozen-path acceptance boundary made explicit |
| Prior evidence and limitations | Reconciled into current status and verification register |
| Directory navigation | Verified direct-child tree and counterpart links added; no directory created or retired |
| Payload, code, schema, policy, release, or publication change | None |

### Change history

#### v0.4.0 — 2026-09-04

- reconciles deprecated-parent classification with accepted ADR-0029 and the active Root Registry;
- closes the tracked-subtree inventory gap: 14 READMEs, 7 empty placeholders, and no other files;
- adds direct canonical counterpart navigation without migrating or admitting any domain;
- records ADR-0038's narrow scope, the still-unbound agriculture entry, and this correction's separate acceptance gate;
- preserves all prior section anchors, the lifecycle and evidence boundary, child paths, and rollback lineage;
- replaces the blanket review timer with the adopted event-based profile; changes this README only.

#### v0.3.0 — 2026-07-24

- reconciled the 13 verified domain redirect children;
- normalized the first twelve H2 sections;
- updated the evidence boundary to current `main`;
- preserved compatibility, safety, migration, correction, and rollback controls;
- changed Markdown only.

<p align="right"><a href="#top">Back to top</a></p>

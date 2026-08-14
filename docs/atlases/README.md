<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-atlases-readme
title: docs/atlases/ — Curated Atlas Documentation Lane
type: README; directory-readme; documentation-index; atlas-boundary
version: v0.2
status: draft; repository-grounded; canonical-lane; mixed-lineage; naming-conflicted; non-release; non-publication
owners:
  - "@bartytime4life"
owner_status: "@bartytime4life is the confirmed CODEOWNERS review route; an independent docs steward, atlas editor, domain-review roster, and final artifact custodian remain NEEDS VERIFICATION"
created: 2026-07-16
updated: 2026-08-14
policy_label: repository-public
current_path: docs/atlases/README.md
owning_root: docs/
responsibility: "Define and index the canonical human-readable atlas lane, preserve edition and source lineage, expose naming and compatibility drift, and prevent atlas carriers from becoming evidence, policy, machine-contract, release, or publication authority."
truth_posture: "CONFIRMED current repository tree, adopted Directory Rules placement, review routing, and documentation QA surfaces / CONFLICTED carrier naming, legacy-lane convergence, child inventory, and PDF-path collision / PROPOSED future canonical carrier and artifact-rendering decisions / UNKNOWN external consumers and deployed documentation behavior"
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 710173d51a3a6bf288997df6f3eb4bf7f4da1ef6
  reviewed_at: 2026-08-14
  target_prior_blob: 71a2bc4e2b150a324ac05389dbe89f9ac8f1cba5
  atlases_tree: 980d41fa84c6f4896f5896cb6e7930cf908ba0c0
  legacy_atlas_tree: 7aa0c91b04c6e36ce5b66df8e1446de363bb71e0
  docs_root_blob: 1f8bac189dac1d01c1185e8b4fb8e25efd11d09f
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  adr_0029_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  docs_build_workflow_blob: 7816e07d66774d2e2b3b80b66d5d3349a1393861
  link_check_workflow_blob: 7b6c675d879a36d685b19b18fde401fca1bdd00e
  meta_block_workflow_blob: c2054a053ba3050cf41b731d85a7a0996e9231f6
  document_graph_workflow_blob: 636749f75621bf773ac558286789dadb41c47c35
  stale_scan_workflow_blob: 4717668d30f98d9be2e6d2ebf57862e820cd41aa
inventory_snapshot:
  direct_markdown_files_including_readme: 13
  direct_child_directories: 3
  direct_pdf_files: 0
related:
  - docs/README.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/atlas/README.md
  - docs/registers/DRIFT_REGISTER.md
  - docs/registers/VERIFICATION_BACKLOG.md
  - docs/atlases/master-atlas-v1.1/README.md
  - docs/atlases/KFM_Domains_Culmination_Atlas_v1_1.pdf/README.md
  - docs/atlases/pass-10/README.md
  - control_plane/document_registry.yaml
  - .github/CODEOWNERS
  - .github/workflows/docs-build.yml
  - .github/workflows/docs-meta-block.yml
  - .github/workflows/docs-document-graph.yml
  - .github/workflows/docs-stale-scan.yml
  - .github/workflows/link-check.yml
tags:
  - kfm
  - docs
  - atlases
  - documentation-index
  - edition-lineage
  - source-ledger
  - naming-drift
  - compatibility
  - cite-or-abstain
notes:
  - "v0.2 is a same-path documentation-only reconciliation. It does not select a canonical atlas carrier, migrate the singular legacy lane, resolve the PDF-path collision, render an atlas, or authorize release or publication."
  - "Accepted ADR-0029 adopts the exact Directory Rules v2 bytes and makes docs/atlases/ the canonical human atlas lane; individual files remain governed by their own status, source, edition, and review evidence."
  - "The current direct tree contains twelve atlas/reference Markdown files plus this README, three child directories, and no direct PDF file."
  - "The PDF-suffixed entry is a directory, not a PDF artifact, and therefore blocks the identically named proposed PDF file path until a separate reviewed migration resolves it."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `docs/atlases/` — Curated Atlas Documentation Lane

> Human-readable home for versioned KFM atlases, atlas navigation carriers, source-preserving synthesis, and bounded atlas-derived reference material.

[![lane](https://img.shields.io/badge/lane-canonical%20docs%2Fatlases-1f6feb)](#purpose-and-authority)
[![content](https://img.shields.io/badge/content-mixed%20lineage-d4a72c)](#current-repository-state)
[![naming](https://img.shields.io/badge/naming-CONFLICTED-b42318)](#naming-compatibility-and-path-drift)
[![publication](https://img.shields.io/badge/publication-none-6e7781)](#authority-and-publication-boundary)

> [!IMPORTANT]
> **The lane is canonical; its contents are not automatically canonical.** Accepted
> [`ADR-0029`](../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
> adopts the exact Directory Rules v2 bytes and places curated atlas collections
> under `docs/atlases/`. Each atlas carrier, pointer, extract, register, or
> integration packet still keeps its own status, source, edition, review,
> supersession, and correction boundary.

> [!WARNING]
> **An atlas is a navigation and synthesis surface, not a trust-object substitute.**
> Nothing in this lane may replace `SourceDescriptor`, `EvidenceRef`,
> `EvidenceBundle`, semantic contracts, schemas, policy decisions, review records,
> receipts, proofs, release manifests, correction notices, rollback targets, or
> governed published state.

> [!CAUTION]
> **Two structural conflicts remain open.** Multiple Markdown carriers cover
> overlapping atlas scope under incompatible naming conventions, and
> `KFM_Domains_Culmination_Atlas_v1_1.pdf/` is a directory that blocks an
> identically named PDF file. This README records those facts; it does not resolve
> them.

**Quick navigation:** [Purpose](#purpose-and-authority) · [Status](#current-repository-state) · [Inventory](#current-inventory) · [Content contract](#atlas-content-contract) · [Boundaries](#authority-and-publication-boundary) · [Drift](#naming-compatibility-and-path-drift) · [Maintenance](#maintenance-and-change-discipline) · [Validation](#validation) · [Review](#ownership-and-review) · [Rollback](#correction-supersession-and-rollback) · [Open work](#open-verification-register)

---

## Purpose and authority

`docs/atlases/` owns the **human-readable atlas documentation responsibility**:

- preserve versioned atlas editions and source lineage;
- give readers a stable navigation surface across large or split atlas bodies;
- host reviewable human crosswalks and reference extracts when their upstream
  authority is explicit;
- keep truth labels, scope, limitations, supersession, and correction history
  visible;
- expose conflicts and verification debt rather than silently normalizing them.

The lane does **not** own machine shape, object meaning, source admission,
admissibility, lifecycle instances, release decisions, or public serving.

### Directory Rules basis

Accepted Directory Rules v2 classify `docs/` as the human-readable governance and
explanation root and list `atlases/` as the curated atlas collection lane. This file
already exists at the selected path, so v0.2 preserves the path and updates the
lane contract in place.

| Responsibility | Owning surface | Role of `docs/atlases/` |
|---|---|---|
| Human atlas synthesis and navigation | `docs/atlases/` | Owns this lane |
| Stable doctrine and placement law | `docs/doctrine/` and accepted ADRs | Governs; atlas material cannot amend it |
| Human domain meaning and operating guidance | `docs/domains/` | Upstream domain context |
| Semantic object meaning | `contracts/` | Referenced, never copied as atlas authority |
| Machine-valid shape | `schemas/` | Referenced, never redefined here |
| Admissibility, rights, and sensitivity | `policy/` | Evaluated elsewhere |
| Evidence, receipts, proofs, and lifecycle instances | governed `data/` families | Referenced by stable identity |
| Release, correction, and rollback decisions | `release/` and adopted accountability lanes | Required before public reliance |
| Machine documentation registry | `control_plane/document_registry.yaml` | Review-only comparison target; not self-authorizing |

[Back to top](#top)

---

## Current repository state

| Field | Confirmed state at the evidence snapshot |
|---|---|
| Canonical lane | `docs/atlases/` under accepted Directory Rules v2 |
| Direct tree | Twelve content/reference Markdown files, this README, and three child directories |
| Direct PDF artifacts | None |
| Atlas carrier posture | Mixed: substantive carriers, navigation carriers, pointer-only files, working extracts, and downstream integration packets |
| Naming posture | `CONFLICTED` — several carriers cover overlapping scope under different filename grammars |
| Legacy singular lane | `docs/atlas/` remains present with four direct Markdown files; convergence is incomplete |
| PDF-path posture | `KFM_Domains_Culmination_Atlas_v1_1.pdf/` is a directory, not a PDF file |
| Accepted carrier-name decision | None verified |
| Documentation QA | Executable metadata, local-link, document-graph, and freshness workflows are present |
| Documentation rendering | Explicit `HOLD` — no accepted generator, deterministic site build, preview manifest, hosting target, or publication handoff |
| Runtime/public behavior | `UNKNOWN`; this lane is repository documentation, not a runtime or release surface |

### Material changes since v0.1

- Accepted ADR-0029 now supplies the operative placement authority; v1.4-era
  placement wording is stale.
- `pass-10/` is now a third direct child lane and carries a bounded, non-authoritative
  changed-idea integration packet.
- Documentation metadata, graph, freshness, and changed-file link validation now
  have executable no-network or no-external-request workflows.
- `docs-build` is no longer a TODO-only stub; it is an executable readiness check
  that intentionally records a generator and preview `HOLD`.
- The carrier-name, legacy-lane, chapter-inventory, and PDF-path conflicts remain
  unresolved.

[Back to top](#top)

---

## Current inventory

The inventory below is descriptive. It does not promote a file, reconcile duplicate
scope, or override the status declared inside a child artifact.

### Lane contract

| Entry | Role |
|---|---|
| [`README.md`](./README.md) | This directory boundary, current inventory, maintenance contract, and drift register |

### Atlas carriers, navigation surfaces, and extracts

| Entry | Current role | Authority boundary |
|---|---|---|
| [`KFM_Domains_Culmination_Atlas_v1_1.md`](./KFM_Domains_Culmination_Atlas_v1_1.md) | Underscored pointer variant for Atlas v1.1 | Pointer-only; explicitly naming-conflicted |
| [`KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.md`](./KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.md) | Underscored consolidated-atlas navigation carrier | Does not select itself as final canonical carrier |
| [`domains-atlas-v1.1.md`](./domains-atlas-v1.1.md) | Standalone Domains Culmination Atlas v1.1 Markdown carrier | Defers to its declared source and edition evidence |
| [`domains-v1.1.md`](./domains-v1.1.md) | Domain-focused atlas carrier | Human synthesis; not domain-contract authority |
| [`domains-v1.1-ch14.md`](./domains-v1.1-ch14.md) | Chapter-level extract | Partial carrier; scope is narrower than a whole atlas |
| [`kfm-domains-v1.1-pass23-32-consolidated-atlas.md`](./kfm-domains-v1.1-pass23-32-consolidated-atlas.md) | Kebab-case consolidated navigation carrier | Naming and role overlap remain unresolved |

### Atlas-derived human reference surfaces

| Entry | Current role | Must not become |
|---|---|---|
| [`maplibre-master.md`](./maplibre-master.md) | MapLibre/renderer atlas reference | Renderer decision, package pin, runtime proof, or release authority |
| [`pipeline-gate-reference.md`](./pipeline-gate-reference.md) | Human pipeline-gate reference | Executable gate, policy source, or PromotionDecision |
| [`receipt-catalog.md`](./receipt-catalog.md) | Human receipt taxonomy and crosswalk | Receipt schema, emitted receipt, proof, or release record |
| [`sensitivity-tier-reference.md`](./sensitivity-tier-reference.md) | Human sensitivity-tier reference | Active policy bundle or permission decision |
| [`source-role-anti-collapse.md`](./source-role-anti-collapse.md) | Human source-role and anti-collapse reference | SourceDescriptor, evidence resolution, or validator result |
| [`stale-state-reference.md`](./stale-state-reference.md) | Human stale-state and supersession reference | Runtime stale-state evaluator or correction decision |

### Direct child lanes

| Entry | Confirmed tree state | Current boundary |
|---|---|---|
| [`master-atlas-v1.1/`](./master-atlas-v1.1/) | README plus four Chapter 24 extracts | Proposed split-layout lane; its README inventory is stale because it still describes only two authored extracts |
| [`KFM_Domains_Culmination_Atlas_v1_1.pdf/`](./KFM_Domains_Culmination_Atlas_v1_1.pdf/) | Directory containing one sidecar README | Confirmed file/directory name collision; separate migration required |
| [`pass-10/`](./pass-10/) | README, two JSONL carriers, two JSON/metadata files, an integration matrix, and a path decision | Downstream source-integration carrier; all implementation routing remains held |

### Inventory rule

Before adding an atlas-family file, reviewers must determine whether the change:

1. updates an existing carrier;
2. adds a genuinely distinct edition or bounded extract;
3. introduces another alias, pointer, duplicate scope, or filename variant;
4. requires a naming, supersession, compatibility, or migration decision.

The default for an unresolved fourth case is `HOLD`, not a ninth carrier.

[Back to top](#top)

---

## Atlas content contract

Every substantive atlas carrier or bounded extract should make the following
information visible at the level appropriate to its scope.

| Requirement | Minimum expectation |
|---|---|
| Identity | Stable `doc_id`, title, path, edition/version, and artifact class |
| Source boundary | Named source documents or generated source set; no implied source authority |
| Truth posture | `CONFIRMED`, `PROPOSED`, `UNKNOWN`, and `NEEDS VERIFICATION` used consistently |
| Scope | Included domains, object families, time/geography, and explicit exclusions |
| Lineage | Predecessor, successor, retained editions, pointer/mirror status, and supersession effect |
| Authority | What the atlas may explain and what it must defer to |
| Evidence | Citations or stable source locators for consequential claims |
| Sensitivity | Public-safe treatment, omissions, generalization, and restricted-source caveats |
| Generation | Generator/tool identity, input identity, and review boundary when content is converted or generated |
| Integrity | Digest or manifest references when an immutable artifact is claimed |
| Correction | How a factual or structural correction is recorded and propagated |
| Rollback | Prior blob/edition or another deterministic restoration target |
| Navigation | Resolving links to parent lane, source edition, siblings, and affected domain/reference surfaces |
| Non-effects | No source admission, policy decision, promotion, release, deployment, or publication by file presence |

### Source-role preservation

An atlas may compare, summarize, or cross-reference sources, but it must preserve
the source role and limitation of each claim. It must not turn:

- modeled or synthetic material into observation;
- aggregate evidence into per-place truth;
- regulatory or administrative records into physical observations;
- a map, graph, tile, screenshot, or AI summary into evidence;
- a source packet into an admitted source;
- an atlas crosswalk into an accepted semantic contract.

Where sources disagree, retain the discrepancy, cite both sides, and route the
decision to the owning contract, policy, ADR, source, evidence, or review surface.

[Back to top](#top)

---

## What belongs here

- Versioned atlas carriers with explicit identity, source, edition, and
  supersession posture.
- Pointer and navigation files that state their non-authoritative status and have
  a verified consumer or migration purpose.
- Human-readable atlas-derived crosswalks and reference catalogs that preserve
  upstream authority.
- Bounded chapter extracts or edition child lanes whose relationship to the
  source artifact is explicit.
- Source-integration packets such as `pass-10/` when their purpose is durable
  human traceability and they do not claim implementation.
- Companion documentation for an atlas artifact when its path cannot collide
  with the artifact.
- This directory README.

## What does not belong here

| Excluded material | Owning family |
|---|---|
| Semantic object definitions | `contracts/` |
| JSON Schema or other machine shape | `schemas/` |
| Active admissibility, rights, sensitivity, or release rules | `policy/` |
| Machine governance registers | `control_plane/` |
| Source descriptors and source activation state | governed source-registry lanes |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG/TRIPLETS, or PUBLISHED instances | `data/` lifecycle lanes |
| Emitted receipts and proofs | adopted accountability lanes |
| Promotion decisions, release manifests, corrections, or rollback cards | `release/` and adopted accountability lanes |
| Executable validators, generators, pipelines, apps, or runtime code | the corresponding execution root |
| Generated site output, temporary previews, or QA scratch files | non-authoritative generated/QA lanes |
| Another atlas filename variant without a reviewed identity and migration need | `HOLD` pending decision |
| Real atlas content under `docs/atlas/` | migrate only through reviewed compatibility work |

[Back to top](#top)

---

## Authority and publication boundary

Atlas material is downstream of the authority appropriate to each claim.

```text
source identity and terms
  -> evidence and source-role resolution
  -> contracts / schemas / policy
  -> validation and human review
  -> release, correction, and rollback
  -> atlas synthesis and navigation
```

The diagram is an authority relationship, not a lifecycle shortcut. Atlas
documentation may be authored before a public release when it is clearly labeled
as draft or planning lineage, but it must not present unreviewed or unreleased
material as authoritative public truth.

### Public and sensitive content

This repository is public-facing. Atlas authors must not embed:

- credentials, private endpoints, signed URLs, or restricted source payloads;
- living-person, DNA/genomic, land/title, archaeology, rare-species, private-well,
  infrastructure, cultural, or sovereignty-sensitive details without approved
  public-safe treatment;
- precise coordinates whose disclosure posture is unresolved;
- proprietary source excerpts beyond verified rights and repository policy.

Prefer bounded paraphrase, citation, redaction, generalization, staged access,
abstention, or denial when the public-use posture is unclear.

[Back to top](#top)

---

## Inputs and outputs

### Permitted inputs

- accepted doctrine and ADRs;
- current repository contracts, schemas, policy, tests, workflows, manifests,
  receipts, proofs, and release records when a claim depends on them;
- domain documentation and source guidance;
- supplied atlas editions, source ledgers, manifests, and bounded extracts;
- authoritative external sources when a current fact requires them;
- historical plans and prior atlases as explicitly labeled lineage.

A cited input does not gain a stronger authority class by appearing in an atlas.

### Outputs

This lane may produce:

- reviewable Markdown atlas carriers;
- bounded navigation and chapter extracts;
- human crosswalks and source-preserving reference catalogs;
- documentation indexes and correction/supersession notes;
- review input for future ADR, contract, schema, policy, validation, or release
  work.

This lane does **not** emit an admitted source, EvidenceBundle, policy result,
proof, release state, published layer, deployed site, or public API response.

[Back to top](#top)

---

## Naming, compatibility, and path drift

### Carrier naming conflict

The current lane contains several carriers for overlapping material under
underscored UpperCase, kebab-case, chapter-suffixed, and consolidated-name
conventions. Some are pointer-only; some carry substantial content. No accepted
decision was verified that selects one writable carrier grammar or retires the
others.

Until that decision exists:

- do not infer canonical content authority from filename style;
- update the most directly applicable existing carrier;
- do not add another variant merely to satisfy a guessed reference;
- preserve pointer-only files as pointer-only;
- log content divergence rather than silently merging it;
- use a reviewed migration with inbound-link repair before renaming or deleting.

### Singular compatibility lane

[`docs/atlas/`](../atlas/) remains in the current tree with `README.md`,
`decision-outcome-envelope.md`, `master-api-surface.md`, and
`source-role-anti-collapse.md`. The directory's README describes the lane as a
deprecated mirror, but the extra content shows that convergence is not complete.

This update does not delete, move, rewrite, or bless those files. A separate
migration must classify each object's authority, compare it with plural-lane
counterparts, preserve stable identity and inbound links, and define rollback.

### PDF-path collision

`KFM_Domains_Culmination_Atlas_v1_1.pdf/` is a directory. Its sidecar README
states that the same path has also been proposed for a PDF file. Both cannot
coexist.

Resolution requires a separate, reviewed migration that:

1. selects a non-colliding home for the sidecar documentation;
2. verifies every inbound reference and generated consumer;
3. records the PDF artifact's actual source, digest, rights, review, and release
   posture;
4. moves or removes the directory without rewriting shared history;
5. validates links and rollback;
6. does not treat PDF placement as publication.

### Child inventory drift

`master-atlas-v1.1/` currently contains four chapter extracts, while its README
still describes two authored extracts. That is documentation drift, not authority
to regenerate or delete a chapter. Reconcile the child README in its own
reviewable change after checking each extract's source and status.

[Back to top](#top)

---

## Maintenance and change discipline

### Same-path update checklist

For an ordinary atlas documentation change:

1. Pin the current base commit and target blob.
2. Read the complete target plus its declared source, parent README, and relevant
   accepted ADRs.
3. Classify the change as correction, additive synthesis, edition update,
   extraction, generated conversion, pointer repair, or structural migration.
4. Search open pull requests and branches for overlapping work.
5. Preserve stable `doc_id`, anchors, source IDs, edition lineage, and
   supersession semantics unless the change explicitly governs them.
6. Verify every material claim against current evidence; mark implementation,
   rights, source, and release gaps.
7. Update affected navigation without creating a parallel writable authority.
8. Run the changed-area documentation checks.
9. Record rollback to a prior blob or edition.
10. Stop at a reviewable branch or pull request; merge and publication are
    separate transitions.

### Structural or authority-changing changes

A carrier rename, lane migration, edition retirement, pointer removal, child
layout adoption, or file/directory collision repair requires more than a content
edit. Before implementation, identify:

- accepted decision authority;
- canonical source and destination;
- verified writers and consumers;
- inbound links and stable anchors;
- source and generated relationships;
- compatibility window and single-write rule;
- correction and rollback evidence;
- deletion or retirement exit criteria.

[Back to top](#top)

---

## Validation

The repository now has substantive documentation QA. These checks remain quality
evidence only; none grants doctrine, source, policy, release, deployment, or
publication authority.

| Check | Current responsibility | Boundary |
|---|---|---|
| [`docs-meta-block`](../../.github/workflows/docs-meta-block.yml) | Validate changed top-level metadata, dates, responsibility-root agreement, related-path hygiene, duplicate identity, and review-only registry parity | No registry mutation or authority decision |
| [`link-check`](../../.github/workflows/link-check.yml) | Validate local file, directory, image, and fragment targets in changed Markdown | External URLs remain unrequested and unverified |
| [`docs-document-graph`](../../.github/workflows/docs-document-graph.yml) | Build bounded explicit-link and reachability QA for changed documentation | Graph is a review projection, not doctrine |
| [`docs-stale-scan`](../../.github/workflows/docs-stale-scan.yml) | Report changed-file freshness, placeholder, temporary-marker, and implementation-claim signals | Advisory profile; no owner or review assignment |
| [`docs-build`](../../.github/workflows/docs-build.yml) | Detect whether an accepted generator, dependencies, manifest, preview, and hosting handoff exist | Intentionally held; a green held job does not mean a site was built or published |

### Required review checks for this lane

- Metadata parses and preserves the stable `doc_id`.
- Exactly one H1 is present.
- Fences, tables, details blocks, and alerts are balanced.
- Every changed local link and fragment resolves with correct case.
- Source, edition, and supersession claims are supported.
- No carrier or extract is silently promoted.
- No sensitive or rights-restricted detail is exposed.
- Naming or placement drift is surfaced rather than normalized by prose.
- The diff changes only intended documentation and direct dependencies.
- Hosted results are reported separately from local structural checks.

No atlas-specific renderer or PDF build is established by these workflows.
Generating or validating an atlas PDF remains a separate artifact-producing
process with its own source, integrity, review, release, correction, and rollback
requirements.

[Back to top](#top)

---

## Ownership and review

[`CODEOWNERS`](../../.github/CODEOWNERS) routes this lane through the repository
default owner, `@bartytime4life`. CODEOWNERS is a review-routing mechanism only;
it does not assign a documentation steward, prove review, or grant release
authority.

Review should expand according to the change:

| Change type | Additional review needed |
|---|---|
| Domain content or cross-domain claim | Affected domain/source/evidence steward |
| Rights, sensitivity, or public-safe treatment | Policy and sensitivity reviewer |
| Contract, schema, policy, or source interpretation | Owner of the cited authority family |
| Edition or supersession change | Docs/atlas editor plus source-artifact reviewer |
| Naming, move, alias, or retirement | Architecture/directory-governance and migration review |
| Generated PDF or public documentation handoff | Artifact integrity, release, correction, and rollback review |

The named independent roles remain `NEEDS VERIFICATION`; do not encode placeholder
roles as executable GitHub owners.

[Back to top](#top)

---

## Correction, supersession, and rollback

### Corrections

A factual or structural atlas correction should:

1. preserve the original source and edition identity;
2. state what changed and why;
3. update affected navigation and cross-references;
4. retain prior Git history or a superseded edition;
5. identify downstream carriers that may need refresh;
6. avoid rewriting evidence, policy, review, or release history.

### Supersession

A successor atlas does not erase its predecessor. Record:

- predecessor and successor IDs;
- exact scope of supersession;
- material retained unchanged;
- material corrected, withdrawn, or added;
- source and review evidence;
- compatibility and citation behavior;
- rollback target.

### Rollback

For this README, rollback is restoration of prior blob
`71a2bc4e2b150a324ac05389dbe89f9ac8f1cba5` through a reviewed revert or
forward-fix. No atlas content, source, policy, data, runtime, release, or published
artifact is mutated by this lane-contract update.

A structural atlas migration needs its own rollback manifest; restoring this README
alone cannot undo moved files, repaired links, generated artifacts, or consumer
changes.

[Back to top](#top)

---

## Open verification register

| Item | Status | Required evidence |
|---|---|---|
| Canonical Markdown carrier name and grammar | `NEEDS VERIFICATION` | Accepted decision plus migration and inbound-link analysis |
| Final atlas artifact and sidecar placement | `CONFLICTED` | Path decision resolving the `.pdf/` directory collision |
| `docs/atlas/` convergence and retirement | `HOLD` | Per-file authority classification, consumer closure, migration, and rollback |
| `master-atlas-v1.1/` inventory reconciliation | `NEEDS VERIFICATION` | Source check for all four current extracts and child README update |
| Atlas v1.1 PDF bytes, digest, rights, and repository home | `UNKNOWN` | Actual artifact plus integrity and review evidence |
| Accepted atlas generator and deterministic build | `ABSENT / HOLD` | Reviewed generator contract, pinned dependencies, manifest, and replay test |
| Documentation preview/hosting handoff | `ABSENT / HOLD` | Built artifact, immutable manifest, hosting target, release boundary, rollback |
| Independent docs steward and atlas editor identities | `NEEDS VERIFICATION` | Approved assignments and repository access |
| External consumers and historical deep links | `UNKNOWN` | Consumer inventory and reference scan beyond the repository |
| Machine document-registry disposition for this revision | `NEEDS VERIFICATION` | Review of the workflow's emitted delta; no automatic mutation |
| Atlas-specific validation beyond generic docs QA | `PROPOSED` | Accepted contract, fixtures, validator, tests, and workflow wiring |
| Public or semi-public publication state | `NONE` | Governed release evidence appropriate to the artifact |

[Back to top](#top)

---

## Related documentation

- [Documentation root contract](../README.md)
- [Accepted Directory Rules adoption decision](../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [Adopted Directory Rules bytes](../doctrine/directory-rules.md)
- [Legacy singular atlas lane](../atlas/README.md)
- [Human drift register](../registers/DRIFT_REGISTER.md)
- [Verification backlog](../registers/VERIFICATION_BACKLOG.md)
- [Atlas v1.1 chapter-extract lane](./master-atlas-v1.1/README.md)
- [PDF-sidecar collision record](./KFM_Domains_Culmination_Atlas_v1_1.pdf/README.md)
- [Pass 10 integration carrier](./pass-10/README.md)
- [Machine document registry](../../control_plane/document_registry.yaml)

---

## Evidence review triggers

Re-review this lane contract when:

- an atlas naming or carrier ADR is accepted;
- `docs/atlas/` enters a new migration phase;
- the `.pdf/` file/directory collision is repaired;
- an actual atlas PDF or other immutable artifact is added;
- a generator, preview, or public documentation handoff is admitted;
- the direct inventory changes;
- CODEOWNERS or documentation QA changes materially;
- a correction, withdrawal, rights decision, or sensitivity review changes public
  atlas content;
- an atlas-derived reference becomes machine-enforced elsewhere.

**Last evidence review:** 2026-08-14 against
`main@710173d51a3a6bf288997df6f3eb4bf7f4da1ef6`.

[Back to top](#top)

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-atlases-readme
title: docs/atlases/ — Atlas Documentation Lane
type: README; directory-readme; documentation-index
version: v0.1
status: draft; repository-grounded; canonical-lane; naming-conflicted
owners: @kfm/maintainers; docs-steward-NEEDS-VERIFICATION; atlas-editor-NEEDS-VERIFICATION
created: 2026-07-16
updated: 2026-07-16
policy_label: public
current_path: docs/atlases/README.md
truth_posture: >
  CONFIRMED current directory inventory, Directory Rules v1.4 placement rule and
  anti-pattern resolution, wildcard CODEOWNERS coverage, and documentation QA
  scaffolds / PROPOSED atlas-carrier and chapter-extract authority choices,
  filename reconciliation, PDF placement, and dedicated docs validation / NEEDS
  VERIFICATION ADR acceptance, named docs steward and atlas editor, rendered
  publication path, and external-link state
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 9741610a833bc7112a1d42a766fae592baf8f1af
  reviewed_at: 2026-07-16
related:
  - ../doctrine/directory-rules.md
  - ../atlas/README.md
  - master-atlas-v1.1/README.md
  - KFM_Domains_Culmination_Atlas_v1_1.pdf/README.md
  - ../../.github/CODEOWNERS
  - ../../tools/docs/README.md
  - ../../tools/validators/docs/README.md
tags: [kfm, docs, atlases, directory-readme, navigation, drift-control]
notes:
  - "This README documents the observed lane; it does not select a canonical atlas-carrier filename or accept an ADR."
  - "At the evidence snapshot, twelve pre-existing direct Markdown files and two direct child directories were present; no direct PDF file was present."
  - "The PDF-suffixed child is a directory and its own README records the unresolved collision with the proposed PDF file path."
[/KFM_META_BLOCK_V2] -->

# `docs/atlases/`

## Purpose

`docs/atlases/` is the canonical documentation lane for versioned KFM atlases, atlas navigation carriers, and reviewable atlas-derived reference material. It explains and indexes atlas content; it does not replace contracts, schemas, policy, evidence, or release decisions.

## Authority level

**Canonical documentation lane; human-facing and non-machine-authoritative.** Directory Rules v1.4 §6.1 places versioned atlases and dossiers here, and §13.5 selects this plural lane over the duplicate `docs/atlas/` path.

The lane choice does not make every file inside it canonical. Several current carriers and the `master-atlas-v1.1/` chapter layout explicitly identify themselves as `PROPOSED`, `CONFLICTED`, pointer-only, or working extracts. When a document conflicts with an accepted contract, schema, policy decision, evidence object, or release record, the owning authority root wins.

## Status

**CONFIRMED lane; mixed-content maturity; naming reconciliation open.**

- **CONFIRMED:** `docs/atlases/` exists and is the Directory Rules choice over `docs/atlas/`.
- **CONFIRMED:** the reviewed snapshot contained twelve pre-existing direct Markdown files and two direct child directories; no direct PDF file was present.
- **CONFLICTED:** multiple Markdown carriers cover overlapping atlas scope under different filename conventions.
- **PROPOSED:** the chapter-extract layout under `master-atlas-v1.1/` and the final PDF placement described by current documents.
- **NEEDS VERIFICATION:** acceptance of ADR-S-02, a canonical atlas-carrier filename, named stewards, and a publication/rendering pipeline.

This README records the current inventory without resolving those open decisions.

## What belongs here

Accepted content is limited to:

- versioned atlas carriers and explicit pointer/navigation files;
- atlas-derived, human-readable registers and crosswalks whose upstream authority and truth posture are stated;
- per-edition child folders when their layout status and relationship to the source atlas are explicit;
- companion documentation for an atlas artifact, provided its path cannot collide with the artifact itself;
- this directory contract and navigation index.

### Current inventory

| Group | Observed entries | Current boundary |
|---|---|---|
| Atlas carriers and pointers | `KFM_Domains_Culmination_Atlas_v1_1.md`, `KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.md`, `domains-atlas-v1.1.md`, `domains-v1.1-ch14.md`, `domains-v1.1.md`, `kfm-domains-v1.1-pass23-32-consolidated-atlas.md` | Overlapping names and roles are explicitly conflicted; this README does not select among them. |
| Atlas-derived references | `maplibre-master.md`, `pipeline-gate-reference.md`, `receipt-catalog.md`, `sensitivity-tier-reference.md`, `source-role-anti-collapse.md`, `stale-state-reference.md` | Human-facing references only; they do not become machine authority by living here. |
| Child lanes | `master-atlas-v1.1/`, `KFM_Domains_Culmination_Atlas_v1_1.pdf/` | The first documents a proposed chapter-extract layout. The second is a directory whose own README records a collision with the proposed PDF file path. |

Before adding another carrier, confirm that it does not duplicate an existing scope or filename role. Current files repeatedly identify an atlas-Markdown naming ADR as blocking further carrier proliferation.

## What does NOT belong here

- Machine schemas, semantic contracts, or policy code; use `schemas/`, `contracts/`, and `policy/`.
- Evidence bundles, proofs, receipts, promotion decisions, release manifests, or correction records; use their governed data and release roots.
- Source datasets, generated tiles, application code, runtime configuration, or build output.
- Per-domain operational documentation that belongs in `docs/domains/` or `docs/runbooks/`.
- New atlas content under `docs/atlas/`; that singular lane is a compatibility/deprecation surface.
- Another spelling, case, or punctuation variant of an existing carrier without an accepted naming decision and migration plan.
- A directory named like a final artifact when that directory blocks the artifact's file path. The existing `.pdf/` collision is recorded here as unresolved, not endorsed as a pattern.

## Inputs

Inputs may include manually reviewed atlas editions, bounded Markdown extracts, atlas-to-domain crosswalks, accepted corrections, and navigation metadata from the owning documentation lanes. Each file must identify its upstream source, edition, truth posture, and supersession relationship.

No executable atlas generator or accepted PDF build pipeline was verified in the reviewed snapshot. Generated or converted content therefore needs explicit provenance and human review before it is treated as more than a draft.

## Outputs

This lane supports:

- human-readable atlas navigation and edition discovery;
- reviewable Markdown carriers and chapter extracts;
- cross-links from domain, architecture, doctrine, and register documentation;
- documented inputs to steward review, correction, supersession, and future ADR work.

It emits no policy decision, evidence closure result, schema conformance result, promotion approval, or release state by itself.

## Validation

For changes in this lane:

1. Run `git diff --check`.
2. Confirm every added or changed relative link and referenced local path resolves in the current tree.
3. Review the KFM meta block, truth labels, edition lineage, supersession wording, and authority boundary against the changed source material.
4. Check that no new carrier duplicates an existing role and that no path reintroduces `docs/atlas/` as writable authority.
5. If content is generated or converted, verify its declared source and review record separately from the Markdown diff.

There is no verified executable atlas-specific validator. At the reviewed snapshot, `.github/workflows/docs-build.yml` and `.github/workflows/link-check.yml` are TODO-only workflow stubs, `tools/docs/` contains no executable helper, and the child lanes under `tools/validators/docs/` contain README scaffolds plus `.gitkeep` files rather than validator programs. Do not cite those surfaces as successful enforcement.

## Review burden

`.github/CODEOWNERS` has no `docs/atlases/`-specific rule, so changes currently fall through to the repository-wide `@kfm/maintainers` owner.

Substantive atlas changes should also receive review from the affected domain or subsystem steward and a docs/atlas editor. The exact handles for those roles are **NEEDS VERIFICATION**. Changes that choose a canonical filename, alter authority, or migrate an artifact path must include the relevant ADR or migration record rather than resolving the choice in an ordinary content edit.

## Related folders

| Folder | Relationship |
|---|---|
| [`../atlas/`](../atlas/) | Deprecated compatibility/mirror lane; do not add new atlas content there. |
| [`master-atlas-v1.1/`](master-atlas-v1.1/) | Proposed per-chapter Markdown extract layout for Atlas v1.1. |
| [`KFM_Domains_Culmination_Atlas_v1_1.pdf/`](KFM_Domains_Culmination_Atlas_v1_1.pdf/) | Existing PDF-suffixed directory; its README documents the unresolved artifact-path collision. |
| [`../domains/`](../domains/) | Per-domain documentation and dossier context. |
| [`../doctrine/`](../doctrine/) | Placement, authority, lifecycle, and truth-posture doctrine. |
| [`../adr/`](../adr/) | Accepted and proposed architecture decisions; no ADR-S-02 file was found in the reviewed snapshot. |
| [`../registers/`](../registers/) | Drift, verification, and document-register surfaces. |
| [`../../tools/docs/`](../../tools/docs/) | Documentation-tooling boundary; executable helpers were not present at review time. |
| [`../../tools/validators/docs/`](../../tools/validators/docs/) | Proposed documentation-validator lanes; no executable child validator was present at review time. |

## ADRs

- **ADR-S-02 — doctrine artifact placement under `docs/` (`dossiers/` vs `atlases/`):** referenced by Directory Rules and multiple atlas documents, but no matching ADR file was found. Acceptance remains **NEEDS VERIFICATION**.
- **Atlas-Markdown naming decision:** repeatedly proposed by current carrier files to reconcile overlapping filename conventions. No accepted ADR file was found; further carrier variants should wait for that decision.
- **Directory Rules v1.4 §13.5, “Docs naming duplication”:** the current documented resolution is to use `docs/atlases/` and deprecate or mirror `docs/atlas/`. Directory Rules §18 records OPEN-DR-09-h as the associated drift item.

This README implements the existing folder-README requirement; it does not accept, number, or supersede an ADR.

## Last reviewed

2026-07-16 — reviewed against the direct directory inventory, `docs/atlas/README.md`, Directory Rules v1.4 §§6.1, 13.5, and 15, `.github/CODEOWNERS`, documentation workflow stubs, and the currently present docs-tooling and docs-validator files at commit `9741610a833bc7112a1d42a766fae592baf8f1af`.

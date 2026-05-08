<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/flora/registers/file-manifest
title: Flora — FILE_MANIFEST (Lane File Inventory & Control Register)
type: standard
version: v0.1
status: draft
owners: TBD — flora-steward (NEEDS VERIFICATION); KFM docs steward (NEEDS VERIFICATION)
created: 2026-05-07
updated: 2026-05-07
policy_label: public
related:
  - docs/domains/flora/README.md
  - docs/domains/flora/ARCHITECTURE.md
  - docs/domains/flora/CURRENT_STATE.md
  - docs/domains/flora/SOURCE_REGISTRY.md
  - docs/domains/flora/VERIFICATION_BACKLOG.md
  - docs/domains/flora/CHANGELOG.md
  - docs/adr/ADR-flora-schema-home.md
  - registers/  (top-level KFM register root — NEEDS VERIFICATION)
  - control_plane/document_registry.yaml  (NEEDS VERIFICATION)
tags: [kfm, flora, register, manifest, control-index, anti-fragmentation]
notes:
  - Path placement diverges from the Flora Architecture Blueprint (which lists FILE_MANIFEST.md directly under docs/domains/flora/, not under a registers/ subfolder) and from Directory Rules (which scopes /registers and /control_plane as repo-root governance roots, not per-domain subfolders). Adopt this path only after an ADR confirms the per-domain `registers/` convention. See "Placement Note" below.
  - All file rows are PROPOSED until the real repository is mounted and inspected. No file presence, no schema shape, no policy enforcement is asserted as fact.
  - Owners, dates, and badge targets are placeholders until a real CODEOWNERS / OWNERS map and CI workflow are confirmed.
[/KFM_META_BLOCK_V2] -->

# Flora — `FILE_MANIFEST` 🌾

> **One-line purpose.** Hand-authored, lane-scoped **control index** that lists every file the Flora domain proposes or owns, names its responsibility root, and pins each row to a status, owner, gate, and rollback handle so the lane cannot fragment behind contributors' backs.

---

## At a glance

[![Status: draft](https://img.shields.io/badge/status-draft-orange.svg)](#)
[![Type: register](https://img.shields.io/badge/type-register-blue.svg)](#)
[![Priority: P1](https://img.shields.io/badge/priority-P1-yellow.svg)](#)
[![Public-risk: low–medium](https://img.shields.io/badge/public--risk-low--medium-green.svg)](#)
[![Owners: TBD](https://img.shields.io/badge/owners-TBD-lightgrey.svg)](#)
[![ADRs: NEEDS VERIFICATION](https://img.shields.io/badge/ADRs-NEEDS%20VERIFICATION-lightgrey.svg)](#)

> [!IMPORTANT]
> This register is **PROPOSED**. The repository was **not** mounted in this session, so every file row below is an unverified *proposal* drawn from the attached Flora Architecture Blueprint and Directory Rules. Treat every path, status, and owner as **NEEDS VERIFICATION** until the real repo is inspected.

**Quick jump:** [Scope](#1-scope) · [Repo fit](#2-repo-fit) · [Inputs](#3-accepted-inputs) · [Exclusions](#4-exclusions) · [Placement note](#5-placement-note-honor-user-path-flag-divergence) · [Lane tree](#6-flora-lane-tree-proposed) · [Diagram](#7-where-this-register-sits) · [File inventory](#8-file-inventory-proposed) · [Task list](#9-task-list--definition-of-done) · [FAQ](#10-faq) · [Appendix](#11-appendix)

---

## 1. Scope

`FILE_MANIFEST` is the **single hand-authored map** of every artifact that lives under the Flora lane — docs, ADRs, registries, contracts, policies, validators, pipelines, packages, fixtures, tests, governed-API surfaces, UI payloads, CI workflows, and migration stubs. Its job is small and strict:

- **Inventory**, not invention. It records files that *exist* or are *proposed by an approved plan*; it does not invent new authority roots.
- **Control**, not governance. It pins each row to a *responsibility root*, a *status*, an *owner*, a *priority*, and a *rollback handle*. It does not replace ADRs, contracts, schemas, policies, or release manifests.
- **Anti-fragmentation**. It is the place reviewers check before merging a new flora-shaped file, so the lane doesn't quietly grow parallel schema, policy, registry, or doc homes.
- **Truth-labeled**. Every row carries one of `CONFIRMED · PROPOSED · UNKNOWN · NEEDS VERIFICATION` so memory cannot impersonate evidence.

> [!NOTE]
> This register is **interpretive prose plus a table**. The machine-readable companion (when one exists) lives under `data/registry/flora/` or `control_plane/` — see [§ 4 Exclusions](#4-exclusions).

---

## 2. Repo fit

| Aspect | Value | Truth label |
|---|---|---|
| Lane | `flora` | CONFIRMED (lane name; doctrine source: Flora Architecture Blueprint) |
| Owning root | `docs/` (documentation responsibility root) | CONFIRMED (Directory Rules) |
| Sibling docs | `README.md`, `ARCHITECTURE.md`, `CURRENT_STATE.md`, `SOURCE_REGISTRY.md`, `DATA_MODEL.md`, `PIPELINES_AND_LIFECYCLE.md`, `PUBLICATION_AND_POLICY.md`, `UI_AND_EVIDENCE_DRAWER.md`, `VERIFICATION_BACKLOG.md`, `ROADMAP.md`, `GLOSSARY.md`, `IDEA_INT

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-sources-catalog-template-source-family
title: Source family README template
type: template
version: v0.1
status: draft
owners: <PLACEHOLDER — Docs steward + Source steward>
created: 2026-05-20
updated: 2026-05-20
policy_label: public
related:
  - docs/sources/catalog/README.md
  - docs/doctrine/directory-rules.md
tags: [kfm, docs, sources, catalog]
notes:
  - "PROPOSED scaffold; sibling-link presence verified in Claude Code session."
  - "Template — copy to <family>/README.md and replace every <placeholder>. Keep the real KFM Meta Block above; replace the placeholder line below with a real meta block."
[/KFM_META_BLOCK_V2] -->

<KFM Meta Block v2 — type: readme>

# `<family>` source family

> Source-oriented catalog documentation for the **<family>** source family.
> Explains how <family> products land in `data/catalog/{stac,dcat,prov,domain}/`.

[![Status: draft](https://img.shields.io/badge/status-draft-orange)](#status)
[![Authority: docs-companion](https://img.shields.io/badge/authority-docs--companion-blue)](#authority-level)
[![Truth posture: cite--or--abstain](https://img.shields.io/badge/truth--posture-cite--or--abstain-success)](../../doctrine/truth-posture.md)
<!-- TODO: replace with real Shields.io endpoints once wired -->
[![CI: NEEDS VERIFICATION](https://img.shields.io/badge/CI-NEEDS%20VERIFICATION-lightgrey)](#validation)

**Status:** draft · **Owners:** `<PLACEHOLDER — Docs steward + Source steward for <family>>` · **Last reviewed:** <today>

---

## Contents
- [Purpose](#purpose)
- [Authority level](#authority-level)
- [Status](#status)
- [What belongs here](#what-belongs-here)
- [What does NOT belong here](#what-does-not-belong-here)
- [Directory tree](#directory-tree)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Validation](#validation)
- [Review burden](#review-burden)
- [Related folders](#related-folders)
- [ADRs](#adrs)
- [Last reviewed](#last-reviewed)

## Purpose
<one-paragraph plain-English statement of what <family> is and why KFM ingests it. NEEDS VERIFICATION for current rights / terms.>

## Authority level
`docs-companion` — explanatory only. Authority for placement, schema, policy, and source descriptors lives in `contracts/`, `schemas/`, `policy/`, and `data/registry/sources/<family>/` respectively.

## Status
PROPOSED — scaffold only. Per-product pages to be authored as products materialize in `connectors/<family>/` and `data/registry/sources/<family>/`.

## What belongs here
- Per-product Markdown pages explaining how each <family> product becomes catalog entries.
- Identity and namespace conventions for <family> entries.
- Cross-links to contracts, schemas, policy, and connector implementations.

## What does NOT belong here
- SourceDescriptor records (live in `data/registry/sources/<family>/`).
- Schemas (live in `schemas/contracts/v1/source/`).
- Policy rules (live in `policy/sources/`, `policy/sensitivity/`).
- Connector code (lives in `connectors/<family>/`).
- Catalog artifacts (live in `data/catalog/`).

## Directory tree
PROPOSED — see lane root [`docs/sources/catalog/INDEX.md`](../INDEX.md).

## Inputs
- `contracts/` — object families.
- `schemas/contracts/v1/source/` — machine shape (per ADR-0001).
- `data/registry/sources/<family>/` — source descriptors.
- `policy/sources/`, `policy/sensitivity/` — admissibility and release gates.
- Pass-23 / Pass-32 Consolidated Atlas — per-domain *Key source families* tables.

## Outputs
- Per-product Markdown pages (human-readable).
- Cross-links into contracts, schemas, policy, connectors, pipelines, validators.
- No machine artifacts.

## Validation
- Markdown lint (NEEDS VERIFICATION — workflow not yet wired).
- Link integrity against repo-relative targets.
- Per-product page conformance to `_template/SOURCE_PRODUCT_TEMPLATE.md`.

## Review burden
- New page: Docs steward + Source steward for <family>.
- Rights/sensitivity narrative changes: + Sensitivity reviewer (+ rights-holder rep if applicable).
- Identity/namespace convention changes: + at least one subsystem owner (`data/catalog/` or `contracts/`).

## Related folders
- [`docs/sources/catalog/README.md`](../README.md) — lane root.
- [`docs/sources/README.md`](../../README.md) — parent lane.
- [`docs/doctrine/directory-rules.md`](../../../doctrine/directory-rules.md) — placement authority.
- [`connectors/<family>/`](../../../../connectors/<family>/) — connector implementation.   <!-- append " *(verify presence)*" ONLY if Phase 0 marked ABSENT -->
- [`data/registry/sources/<family>/`](../../../../data/registry/sources/<family>/) — source descriptors.   <!-- same rule -->
- [`data/catalog/`](../../../../data/catalog/) — catalog artifacts.   <!-- same rule -->

## ADRs
- ADR-0001 (schema-home) — defaults schemas to `schemas/contracts/v1/`.
- PROPOSED — namespace pin (`kfm:` vs `ks-kfm:`) per OPEN-DSC-03.

## Last reviewed
<today> *(Claude Code scaffold authoring session — sibling-link presence verified in Phase 0)*.

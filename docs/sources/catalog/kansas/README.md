<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-sources-catalog-kansas-readme
title: kansas source family
type: readme
version: v0.1
status: draft
owners: <PLACEHOLDER — Docs steward + Source steward for kansas>
created: 2026-05-20
updated: 2026-05-20
policy_label: public
related:
  - docs/sources/catalog/README.md
  - docs/doctrine/directory-rules.md
tags: [kfm, docs, sources, catalog]
notes:
  - "Created as the kansas family overview during the flat-to-folder reorganization; sibling-link presence verified in Claude Code session."
[/KFM_META_BLOCK_V2] -->

# `kansas` source family

> Source-oriented catalog documentation for the **Kansas state-scoped** source family.

**Status:** draft · **Owners:** `<PLACEHOLDER — Docs steward + Source steward for kansas>` · **Last reviewed:** 2026-05-20

---

## Overview
The `kansas` family groups **Kansas state-scoped sources** — state agencies, universities, museums, and archives whose data KFM ingests. Unlike the single-product families, `kansas` aggregates many distinct Kansas institutions, each documented on its own product page in this folder.

## Product pages
| Page | Source |
|---|---|
| [`ksgs.md`](./ksgs.md) | Kansas Geological Survey (KGS) |
| [`kdwp.md`](./kdwp.md) | Kansas Department of Wildlife and Parks |
| [`khri.md`](./khri.md) | Kansas Historic Resources Inventory |
| [`kansas-memory.md`](./kansas-memory.md) | Kansas Memory (KSHS) |
| [`kansas-state-archives.md`](./kansas-state-archives.md) | Kansas State Archives |
| [`ksu-research-extension.md`](./ksu-research-extension.md) | KSU Research and Extension |
| [`ku-nhm.md`](./ku-nhm.md) | KU Biodiversity Institute & Natural History Museum |
| [`fhsu-sternberg.md`](./fhsu-sternberg.md) | FHSU Sternberg Museum of Natural History |

## Source authority
Authoritative SourceDescriptors live in [`data/registry/sources/`](../../../../data/registry/sources/) — do not duplicate descriptor fields here.

## Catalog profiles
Kansas sources span many domains and land across STAC, DCAT, PROV-O, and the domain projections in [`data/catalog/`](../../../../data/catalog/). See per-product pages and [`PROFILES.md`](../PROFILES.md).

## Identity & namespaces
Collection-id and namespace conventions follow [`IDENTITY.md`](../IDENTITY.md). The namespace pin (`kfm:` vs. `ks-kfm:`) is unresolved — see `OPEN-DSC-03` in [`OPEN-QUESTIONS.md`](../OPEN-QUESTIONS.md).

## Rights & sensitivity
NEEDS VERIFICATION per source — see [`RIGHTS-AND-SENSITIVITY-MAP.md`](../RIGHTS-AND-SENSITIVITY-MAP.md) and [`policy/sensitivity/`](../../../../policy/sensitivity/). Several Kansas natural-history and archaeological sources are sensitivity-gated (deny-by-default per ADR-0010). Never restate policy here.

## Validation
- Markdown lint (NEEDS VERIFICATION — workflow not yet wired).
- Link integrity against repo-relative targets.
- Per-product page conformance to [`_template/SOURCE_PRODUCT_TEMPLATE.md`](../_template/SOURCE_PRODUCT_TEMPLATE.md).

## Related contracts & schemas
- [`schemas/contracts/v1/source/`](../../../../schemas/contracts/v1/source/) — machine shape (per ADR-0001).
- [`contracts/`](../../../../contracts/) — object families.

## Related connectors & pipelines
- [`connectors/kansas/`](../../../../connectors/kansas/) — connector implementation.
- [`pipelines/ingest/`](../../../../pipelines/ingest/), [`pipelines/normalize/`](../../../../pipelines/normalize/), [`pipelines/validate/`](../../../../pipelines/validate/), [`pipelines/catalog/`](../../../../pipelines/catalog/).

## Open questions
- OPEN — confirm which Kansas institutions warrant their own STAC Collections vs. shared collections.
- OPEN — confirm rights / sensitivity tier per source.
- See [`OPEN-QUESTIONS.md`](../OPEN-QUESTIONS.md) for lane-wide `OPEN-DSC-*` items.

## Last reviewed
2026-05-20 *(Claude Code reorganization session — created as the kansas family overview during the flat-to-folder migration).*

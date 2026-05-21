<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-sources-catalog-usdot-readme
title: USDOT source family
type: readme
version: v0.1
status: draft
owners: <PLACEHOLDER — Docs steward + Source steward for usdot>
created: 2026-05-21
updated: 2026-05-21
policy_label: public
related:
  - docs/sources/catalog/README.md
  - docs/doctrine/directory-rules.md
tags: [kfm, docs, sources, catalog, usdot]
notes:
  - "Family scaffolded from the connectors/ inventory; descriptions grounded in docs/domains SOURCE_REGISTRY files. Beyond directory-rules.md §7.3 — see OPEN-DSC-14."
[/KFM_META_BLOCK_V2] -->

# `usdot` source family

> Source-oriented catalog documentation for the **USDOT** source family.

**Status:** draft — PROPOSED (beyond `directory-rules.md` §7.3) · **Owners:** `<PLACEHOLDER — Docs steward + Source steward for usdot>` · **Last reviewed:** 2026-05-21

---

## Overview
USDOT (the U.S. Department of Transportation) is the federal transportation department whose FHWA, FRA, STB, and BTS components publish the highway, rail, freight, and work-zone datasets that feed the roads-rail-trade domain. This family folder was scaffolded on 2026-05-21 because a `connectors/` companion exists; it is **not** one of the nine `directory-rules.md` §7.3 families and awaits ADR ratification — see [`OPEN-QUESTIONS.md`](../OPEN-QUESTIONS.md) `OPEN-DSC-14`.

## Product pages
| Page | Product |
|---|---|
| [`fhwa-hpms.md`](./fhwa-hpms.md) | FHWA Highway Performance Monitoring System |
| [`fhwa-nhfn.md`](./fhwa-nhfn.md) | FHWA National Highway Freight Network |
| [`fra-form57.md`](./fra-form57.md) | FRA Form 57 Rail Incident Reports |
| [`fra-gcis.md`](./fra-gcis.md) | FRA Grade Crossing Inventory System |
| [`stb-class1.md`](./stb-class1.md) | STB Class I Weekly Reports |
| [`ntad.md`](./ntad.md) | National Transportation Atlas Database |
| [`wzdx.md`](./wzdx.md) | Work Zone Data Exchange |

## Source authority
Authoritative SourceDescriptors live in [`data/registry/sources/`](../../../../data/registry/sources/) — do not duplicate descriptor fields here.

## Catalog profiles
PROPOSED — see [`PROFILES.md`](../PROFILES.md). Confirm per product which of STAC, DCAT, PROV-O, and the domain projections in [`data/catalog/`](../../../../data/catalog/) each product lands in.

## Identity & namespaces
Collection-id and namespace conventions follow [`IDENTITY.md`](../IDENTITY.md). The namespace pin (`kfm:` vs. `ks-kfm:`) is unresolved — see `OPEN-DSC-03` in [`OPEN-QUESTIONS.md`](../OPEN-QUESTIONS.md).

## Rights & sensitivity
NEEDS VERIFICATION per product — see [`RIGHTS-AND-SENSITIVITY-MAP.md`](../RIGHTS-AND-SENSITIVITY-MAP.md) and [`policy/sensitivity/`](../../../../policy/sensitivity/). Never restate policy here.

## Validation
- Markdown lint (NEEDS VERIFICATION — workflow not yet wired).
- Link integrity against repo-relative targets.
- Per-product page conformance to [`_template/SOURCE_PRODUCT_TEMPLATE.md`](../_template/SOURCE_PRODUCT_TEMPLATE.md).

## Related contracts & schemas
- [`schemas/contracts/v1/source/`](../../../../schemas/contracts/v1/source/) — machine shape (per ADR-0001).
- [`contracts/`](../../../../contracts/) — object families.

## Related connectors & pipelines
- Connector folders: `connectors/fhwa_hpms/`, `connectors/fhwa_nhfn/`, `connectors/fra_form57/`, `connectors/fra_gcis/`, `connectors/stb_class1/`, `connectors/ntad/`, `connectors/wzdx/` — all currently empty stubs.
- [`pipelines/ingest/`](../../../../pipelines/ingest/), [`pipelines/normalize/`](../../../../pipelines/normalize/), [`pipelines/validate/`](../../../../pipelines/validate/), [`pipelines/catalog/`](../../../../pipelines/catalog/).

## Open questions
- OPEN — confirm whether this family warrants `directory-rules.md` §7.3 promotion (ADR), per `OPEN-DSC-14`.
- OPEN — confirm rights, cadence, and endpoints per product.
- See [`OPEN-QUESTIONS.md`](../OPEN-QUESTIONS.md) for lane-wide `OPEN-DSC-*` items.

## Last reviewed
2026-05-21 *(Claude Code session — family scaffolded from the connector inventory; descriptions grounded in docs/domains SOURCE_REGISTRY files).*

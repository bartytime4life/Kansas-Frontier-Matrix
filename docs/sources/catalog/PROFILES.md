<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-sources-catalog-profiles
title: Source catalog profiles
type: profile
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
[/KFM_META_BLOCK_V2] -->

# Source catalog profiles

> KFM profiles over STAC, DCAT, and PROV-O — the metadata standards the source-catalog lane narrates.

**Status:** scaffold (PROPOSED)

Each profile below is **PROPOSED**. Version pins, conformance class lists, extension sets, asset roles, and MIME-type registries are **NEEDS VERIFICATION** — they must be confirmed against [`schemas/contracts/v1/source/`](../../../schemas/contracts/v1/source/) and the relevant program records before any profile leaves scaffold status.

## KFM-STAC profile
- **Base standard:** STAC — version pin PROPOSED `1.1.x` (NEEDS VERIFICATION; see KFM-P31-PROG-0004).
- **Conformance classes:** NEEDS VERIFICATION.
- **Extension set:** `kfm:provenance`, `kfm:care`, STAC `file` extension — NEEDS VERIFICATION against `schemas/contracts/v1/source/`.
- **Asset roles:** NEEDS VERIFICATION.
- **MIME types:** NEEDS VERIFICATION.
- **Catalog lane:** [`data/catalog/stac/`](../../../data/catalog/stac/).

## KFM-DCAT profile
- **Base standard:** DCAT — version pin PROPOSED (NEEDS VERIFICATION).
- **Distribution model:** dataset → distribution; `kfm:care` may attach at distribution level — NEEDS VERIFICATION.
- **Catalog lane:** [`data/catalog/dcat/`](../../../data/catalog/dcat/).

## KFM-PROV profile
- **Base standard:** W3C PROV-O — version pin PROPOSED (NEEDS VERIFICATION).
- **Core mapping:** `RunReceipt` and `EvidenceBundle` map to PROV activities and entities — NEEDS VERIFICATION.
- **Temporal vocabulary:** six time-kinds tracked per ADR-0014.
- **Catalog lane:** [`data/catalog/prov/`](../../../data/catalog/prov/).

## Related docs
- [`docs/sources/catalog/CROSSWALKS.md`](./CROSSWALKS.md) — cross-format mappings.
- [`docs/sources/catalog/IDENTITY.md`](./IDENTITY.md) — identity and namespace conventions.
- [`schemas/contracts/v1/source/`](../../../schemas/contracts/v1/source/) — machine shapes (per ADR-0001).

**Last reviewed:** 2026-05-20

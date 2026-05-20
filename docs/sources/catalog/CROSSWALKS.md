<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-sources-catalog-crosswalks
title: Source catalog crosswalks
type: register
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

# Source catalog crosswalks

> Register of cross-format mappings between the KFM-STAC profile and adjacent metadata standards.

**Status:** scaffold (PROPOSED)

Each crosswalk below is **PROPOSED and not yet authored**. The shared shape for an authored crosswalk is [`_template/CROSSWALK_TEMPLATE.md`](./_template/CROSSWALK_TEMPLATE.md). Field-level mappings must be confirmed against [`schemas/contracts/v1/source/`](../../../schemas/contracts/v1/source/) before any crosswalk leaves scaffold status.

## Crosswalk register

| Crosswalk | Purpose | Document |
|---|---|---|
| STAC × DCAT | Map KFM-STAC items and collections to DCAT datasets and distributions. | [`_template/CROSSWALK_TEMPLATE.md`](./_template/CROSSWALK_TEMPLATE.md) — PROPOSED, not yet authored |
| STAC × DwC | Map STAC plus `properties.taxon` to Darwin Core occurrence terms. | [`_template/CROSSWALK_TEMPLATE.md`](./_template/CROSSWALK_TEMPLATE.md) — PROPOSED, not yet authored |
| STAC × ISO 19115 | Map KFM-STAC to ISO 19115 geographic metadata. | [`_template/CROSSWALK_TEMPLATE.md`](./_template/CROSSWALK_TEMPLATE.md) — PROPOSED, not yet authored |
| STAC × PROV-O | Map `kfm:provenance` fields to W3C PROV-O entities and activities. | [`_template/CROSSWALK_TEMPLATE.md`](./_template/CROSSWALK_TEMPLATE.md) — PROPOSED, not yet authored |
| STAC × CIDOC-CRM | Map cultural-heritage STAC entries to CIDOC-CRM classes. | [`_template/CROSSWALK_TEMPLATE.md`](./_template/CROSSWALK_TEMPLATE.md) — PROPOSED, not yet authored |

> [!NOTE]
> The canonical home for authored crosswalks — this lane vs. `docs/standards/` — is unresolved. See [`OPEN-DSC-06`](./OPEN-QUESTIONS.md).

## Related docs
- [`docs/sources/catalog/PROFILES.md`](./PROFILES.md) — the KFM-STAC / DCAT / PROV profiles being crosswalked.
- [`docs/sources/catalog/_template/CROSSWALK_TEMPLATE.md`](./_template/CROSSWALK_TEMPLATE.md) — crosswalk authoring template.
- [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md) — placement authority.

**Last reviewed:** 2026-05-20

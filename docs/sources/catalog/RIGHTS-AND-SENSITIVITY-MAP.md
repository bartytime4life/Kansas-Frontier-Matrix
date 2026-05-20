<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-sources-catalog-rights-and-sensitivity-map
title: Source catalog rights and sensitivity map
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

# Source catalog rights and sensitivity map

> Per-family summary of typical rights, sensitivity tier, and publication posture. Explanatory only.

**Status:** scaffold (PROPOSED)

> [!IMPORTANT]
> This map **does not decide** rights or sensitivity. Authority lives in [`policy/sensitivity/`](../../../policy/sensitivity/) and [`policy/sources/`](../../../policy/sources/). Every row below is **NEEDS VERIFICATION** — values are placeholders pending confirmation against policy records and per-source terms.

## Family map

| Family | Typical rights | Sensitivity tier | Publication posture | Policy link |
|---|---|---|---|---|
| `usgs` | NEEDS VERIFICATION | NEEDS VERIFICATION | NEEDS VERIFICATION | [`policy/sensitivity/`](../../../policy/sensitivity/) |
| `fema` | NEEDS VERIFICATION | NEEDS VERIFICATION | NEEDS VERIFICATION | [`policy/sensitivity/`](../../../policy/sensitivity/) |
| `noaa` | NEEDS VERIFICATION | NEEDS VERIFICATION | NEEDS VERIFICATION | [`policy/sensitivity/`](../../../policy/sensitivity/) |
| `nrcs` | NEEDS VERIFICATION | NEEDS VERIFICATION | NEEDS VERIFICATION | [`policy/sensitivity/`](../../../policy/sensitivity/) |
| `kansas` | NEEDS VERIFICATION | NEEDS VERIFICATION | NEEDS VERIFICATION | [`policy/sensitivity/`](../../../policy/sensitivity/) |
| `gbif` | NEEDS VERIFICATION | NEEDS VERIFICATION | NEEDS VERIFICATION | [`policy/sensitivity/`](../../../policy/sensitivity/) |
| `inaturalist` | NEEDS VERIFICATION | NEEDS VERIFICATION | NEEDS VERIFICATION | [`policy/sensitivity/`](../../../policy/sensitivity/) |
| `census` | NEEDS VERIFICATION | NEEDS VERIFICATION | NEEDS VERIFICATION | [`policy/sensitivity/`](../../../policy/sensitivity/) |
| `local_upload` | NEEDS VERIFICATION | NEEDS VERIFICATION | NEEDS VERIFICATION | [`policy/sensitivity/`](../../../policy/sensitivity/) |

> [!NOTE]
> Deny-by-default applies to DNA, rare-species, archaeology, and infrastructure data per ADR-0010 — confirm tier assignments against that ADR and `policy/sensitivity/`.

## Related docs
- [`docs/sources/catalog/CARE-COMPLIANCE.md`](./CARE-COMPLIANCE.md) — CARE governance fields.
- [`policy/sensitivity/`](../../../policy/sensitivity/) — authoritative sensitivity rules.
- [`policy/sources/`](../../../policy/sources/) — authoritative source admissibility rules.

**Last reviewed:** 2026-05-20

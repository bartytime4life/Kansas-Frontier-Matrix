<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-sources-catalog-care-compliance
title: Source catalog CARE compliance
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

# Source catalog CARE compliance

> How CARE governance fields attach to KFM catalog entries. Explanatory only.

**Status:** scaffold (PROPOSED)

The **CARE Principles** (Collective benefit, Authority to control, Responsibility, Ethics) govern Indigenous and other rights-holder-sensitive data. This note explains where CARE fields surface in the catalog; it **does not decide** policy — authority is [`policy/sensitivity/`](../../../policy/sensitivity/).

## CARE fields
CARE fields appear in the `kfm:care` extension block on STAC `properties` and on DCAT distributions (Pass-10 C15-02):

| Field | Meaning (PROPOSED) |
|---|---|
| `consent` | Whether rights-holder consent for publication is on record. |
| `authority_to_control` | Identified rights-holder authority over the data. |
| `locality_restrictions` | Geographic generalization or suppression required. |
| `review_expiry` | Date after which the CARE assessment must be re-reviewed. |

## Default-deny rule
Per Pass-10 C15-03, publication is **default-deny** whenever `authority_to_control` is non-empty, until an explicit `PolicyDecision` admits it. This aligns with the deny-by-default posture of ADR-0010 for DNA, rare-species, archaeology, and infrastructure data.

## Related docs
- [`docs/sources/catalog/RIGHTS-AND-SENSITIVITY-MAP.md`](./RIGHTS-AND-SENSITIVITY-MAP.md) — per-family rights summary.
- [`policy/sensitivity/`](../../../policy/sensitivity/) — authoritative CARE and sensitivity rules.
- [`docs/sources/catalog/GLOSSARY.md`](./GLOSSARY.md) — `kfm:care` term.

**Last reviewed:** 2026-05-20

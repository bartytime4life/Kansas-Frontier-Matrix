<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/encyclopedia/chapters/07-domain-chapters
title: "How to use domain chapters"
type: planning-reference
version: v1.0
status: draft; repository-grounded; non-authoritative; placement-hold
owners: ["@bartytime4life via CODEOWNERS; domain review remains pending"]
created: 2026-10-08
created_note: Metadata records substantive draft authorship; the existing path predates this edition.
updated: 2026-10-08
policy_label: public; planning-reference
owning_root: docs/
responsibility: "Explain how to use domain chapters and route readers to the owning KFM sources."
truth_posture: PROPOSED guidance; repository-grounded draft at ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe; not ADR acceptance, source admission, release or publication.
related:
  - docs/encyclopedia/INDEX.md
  - docs/KFM-encyclopedia.md
[/KFM_META_BLOCK_V2] -->

# How to use domain chapters

Evidence snapshot: `main@ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe`. Draft reference; formal lane acceptance remains pending.

Detailed domain documents already exist under [docs/domains](../../domains/README.md). This chapter provides a consistent reading and review method so the encyclopedia does not become a competing copy of every domain guide.

## A useful domain packet

| Read in this order | Information to extract |
|---|---|
| Domain README and architecture | Scope, object families, current maturity and excluded claims |
| Sources and source registry | Native identifiers, editions, access, rights and sensitivity |
| Identity and lifecycle guides | Stable identity, corrections, transformations and phase boundaries |
| Contracts and schemas | Semantic obligations and machine-checkable fields |
| Verification and fixtures | Actual validation behavior and unsupported cases |
| Runbooks and release guidance | Preconditions, operator steps, review and rollback |

## Worked reading route: Soil

Start with the [Soil README](../../domains/soil/README.md), then [identity model](../../domains/soil/IDENTITY_MODEL.md) and [sources](../../domains/soil/SOURCES.md). A map unit can contain multiple components and horizons. Moisture measurements additionally require depth, unit, time and support type. Use the [verification guide](../../domains/soil/VERIFICATION.md) to distinguish the bounded fixture suites from live-source coverage.

When a map uses soil context, retain its survey vintage or modeled period. Do not turn a grid value into a field measurement or a component property into a homogeneous map-unit fact. Record the interpretation and any missing inputs.

## Worked reading route: settlements

The [settlements supplement](11-settlements-infrastructure.md) routes facility, footprint and infrastructure questions to their domain documents. A mapped asset does not prove current operation, condition, ownership or service availability.

## Review output

A domain review should end with a compact evidence list: implemented slice, source identity, accepted semantics if available, tests executed, limits, and next required decision. If a section is incomplete, identify the missing evidence directly. Never copy another domain's successful status into the current one merely because their directory layouts are similar.

[Chapter index](../INDEX.md) · [Reader guide](01-cover.md)

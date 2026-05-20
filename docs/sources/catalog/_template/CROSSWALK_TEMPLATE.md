<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-sources-catalog-template-crosswalk
title: Crosswalk template
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
  - "Template — copy to an authored crosswalk page and replace every <placeholder>. Replace the placeholder line below with a real meta block."
[/KFM_META_BLOCK_V2] -->

<KFM Meta Block v2 — type: crosswalk>

# <Standard A> × <Standard B> crosswalk

> Field-level mapping between <Standard A> and <Standard B> for KFM source-catalog entries. Explanatory only.

**Status:** draft · **Owners:** `<PLACEHOLDER — Docs steward + Source steward>` · **Last reviewed:** <today>

---

## Scope
- **From:** <Standard A> (version <…>) — NEEDS VERIFICATION.
- **To:** <Standard B> (version <…>) — NEEDS VERIFICATION.
- **Direction:** <one-way / bidirectional>.

## Mapping table
| <Standard A> field | <Standard B> field | Cardinality | Notes |
|---|---|---|---|
| <field> | <field> | <1:1 / 1:n / n:1> | NEEDS VERIFICATION |

## Unmapped and lossy fields
- <field> — no equivalent on the target side; PROPOSED handling: <…>.

## Authority
- Field names on both sides MUST be confirmed against `schemas/contracts/v1/source/` and the upstream standard before this crosswalk leaves draft status.
- Authority for placement, schema, and policy lives in `contracts/`, `schemas/`, and `policy/` — this crosswalk is `docs-companion` (explanatory) only.

## Last reviewed
<today> *(replace with the authoring date when this template is filled).*

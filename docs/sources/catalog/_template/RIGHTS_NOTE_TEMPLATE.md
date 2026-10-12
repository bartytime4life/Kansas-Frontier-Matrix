<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-sources-catalog-template-rights-note
title: Rights note template
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
  - "Template — copy alongside a family or product page and replace every <placeholder>. Replace the placeholder line below with a real meta block."
[/KFM_META_BLOCK_V2] -->

<KFM Meta Block v2 — type: register>

# Rights note — <source>

> Per-source rights and sensitivity note. Explanatory only — it does not decide policy.

**Status:** draft · **Owners:** `<PLACEHOLDER — Docs steward + Source steward for <family>>` · **Last reviewed:** <today>

---

## Source
- **Source:** <source name>
- **Family:** `<family>`
- **SourceDescriptor:** `data/registry/sources/<family>/<descriptor>` — NEEDS VERIFICATION.

## License and rights
- **License:** NEEDS VERIFICATION.
- **Attribution requirement:** NEEDS VERIFICATION.
- **Redistribution terms:** NEEDS VERIFICATION.

## Sensitivity
- **Sensitivity tier:** NEEDS VERIFICATION — see `policy/sensitivity/`.
- **CARE applicability:** NEEDS VERIFICATION — see [`CARE-COMPLIANCE.md`](../CARE-COMPLIANCE.md).
- **Publication posture:** NEEDS VERIFICATION — deny-by-default applies per ADR-0010 where relevant.

## Verification log
| Field | Source of truth | Status |
|---|---|---|
| License | <url or document> | NEEDS VERIFICATION |
| Attribution | <url or document> | NEEDS VERIFICATION |
| Sensitivity tier | `policy/sensitivity/` | NEEDS VERIFICATION |

## Authority
- This note is `docs-companion` (explanatory) only. Authoritative rights and sensitivity rules live in `policy/sensitivity/` and `policy/sources/`; the authoritative source record lives in `data/registry/sources/<family>/`.

## Last reviewed
<today> *(replace with the authoring date when this template is filled).*

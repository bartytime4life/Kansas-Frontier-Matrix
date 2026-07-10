<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/catalog-domain-settlements-infrastructure-readme
title: catalog/domain/settlements-infrastructure/ - Settlements Infrastructure Domain Catalog Compatibility Redirect
type: readme
version: v0.1
status: draft
owners: OWNER_TBD - Settlements/Infrastructure steward; Catalog steward; Registry steward; Evidence steward; Receipt steward; Proof steward; Release steward; Policy steward; Docs steward
created: 2026-07-10
updated: 2026-07-10
policy_label: public
related:
  - ../README.md
  - ../../README.md
  - ../../../data/README.md
  - ../../../data/catalog/README.md
  - ../../../data/catalog/domain/README.md
  - ../../../data/catalog/domain/settlements-infrastructure/README.md
  - ../../../data/registry/README.md
  - ../../../data/receipts/README.md
  - ../../../data/proofs/README.md
  - ../../../data/published/README.md
  - ../../../release/README.md
  - ../../../docs/domains/settlements-infrastructure/README.md
  - ../../../docs/doctrine/directory-rules.md
tags: [kfm, catalog, domain, settlements-infrastructure, settlements, infrastructure, compatibility-root, redirect, data-catalog-domain, non-authoritative, drift-fence]
notes:
  - Root-level catalog/domain/settlements-infrastructure/ is a compatibility redirect and drift-control fence only.
  - Canonical Settlements Infrastructure catalog records belong under data/catalog/domain/settlements-infrastructure/.
  - This file does not prove migration completeness, validator coverage, source-rights closure, receipt/proof closure, release approval, publication readiness, or CI enforcement.
[/KFM_META_BLOCK_V2] -->

<a id='top'></a>

# Settlements Infrastructure Domain Catalog Compatibility Redirect

`catalog/domain/settlements-infrastructure/`

This directory exists only to keep the legacy root-level `catalog/domain/` tree aligned with the repository-supported domain catalog lanes. It is not the canonical Settlements Infrastructure catalog home, not a registry, not a receipt/proof store, not a release or publication surface, and not a producer output target.

## Evidence Basis

| Evidence | Supports | Does not prove |
|---|---|---|
| `catalog/domain/README.md` | Root-level `catalog/domain/` is a compatibility redirect and drift fence. | Complete migration or enforcement maturity. |
| `data/catalog/domain/README.md` | Canonical domain catalog lanes live under `data/catalog/domain/`. | That every downstream record, schema, or validator is complete. |
| `data/catalog/domain/settlements-infrastructure/README.md` | `settlements-infrastructure/` is a repository-recognized canonical Settlements Infrastructure catalog lane. | Source-rights closure, proof closure, release approval, or public delivery readiness. |
| `docs/domains/settlements-infrastructure/README.md` | Domain doctrine exists outside this redirect path. | That this directory may host domain doctrine or implementation files. |
| Existing sibling redirects in `catalog/domain/` | Child compatibility README pattern is established for root-level domain lanes. | Permission to mirror every nested canonical sublane here. |

## Canonical Homes

| Family | Canonical home |
|---|---|
| Settlements Infrastructure catalog records | `data/catalog/domain/settlements-infrastructure/` |
| Parent domain catalog index | `data/catalog/domain/` |
| Source, rights, and sensitivity registry rows | `data/registry/` |
| Process receipts | `data/receipts/` |
| Proof support | `data/proofs/` |
| Release governance | `release/` |
| Public-safe published artifacts | `data/published/` |

## Allowed Contents

- `README.md` files that document redirect, compatibility, migration, or drift-control posture.
- Small migration or correction notes only when an owning repository document explicitly requires them here.
- Empty sentinels only when an existing repository rule explicitly requires them.

## Forbidden Contents

- Canonical catalog records, indexes, manifests, schemas, contracts, validators, source descriptors, registry rows, receipts, proofs, release records, published artifacts, generated files, caches, credentials, or runtime outputs.
- RAW, WORK, QUARANTINE, unpublished, canonical-internal, direct model-runtime, or policy-sensitive data.
- AI-generated wording presented as sovereign truth instead of a downstream carrier of cited evidence.

## Domain Guardrails
- Do not make this path a settlement gazetteer, infrastructure inventory, address authority, facility authority, or public map source.
- Do not publish sensitive facility, critical infrastructure, private-property, or uncertain historical-place detail from this redirect path.
- Settlement identity, source descriptors, receipts, proofs, release records, and public-safe derivatives must remain in their governed owning roots.

## Directory Shape

Expected root-level compatibility shape:

```text
catalog/domain/settlements-infrastructure/
+-- README.md
```

Nested canonical sublanes should not be mirrored here unless a future repository contract explicitly requires a root-level redirect for that child path.

## Change Rules

1. Prefer updating the canonical `data/catalog/domain/settlements-infrastructure/` lane for catalog work.
2. Keep this directory limited to redirect and drift-control documentation.
3. Link to owning repository documents instead of duplicating authority.
4. Mark unknown or unverified behavior as `NEEDS VERIFICATION` instead of implying maturity.
5. Preserve source-role separation, governed publication, receipts/proofs separation, and policy-safe public surfaces.

## Open Verification Items

- Actual migration completeness from any legacy root-level Settlements Infrastructure catalog material: `NEEDS VERIFICATION`.
- CI enforcement for this redirect boundary: `NEEDS VERIFICATION`.
- Completeness of downstream schemas, examples, fixtures, validators, release manifests, and public surfaces: owned outside this directory and `NEEDS VERIFICATION` here.

## Definition of Done

This redirect is complete when the root-level path exists, points to the canonical Settlements Infrastructure catalog lane, forbids trust-bearing content in the compatibility path, and does not duplicate authority owned by registry, receipt, proof, release, published, schema, policy, source, tool, or application directories.

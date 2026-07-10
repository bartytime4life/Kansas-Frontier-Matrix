<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/catalog-domain-people-dna-land-readme
title: catalog/domain/people-dna-land/ - People DNA Land Domain Catalog Compatibility Redirect
type: readme
version: v0.1
status: draft
owners: OWNER_TBD - People/DNA/Land steward; Consent steward; Catalog steward; Registry steward; Evidence steward; Receipt steward; Proof steward; Release steward; Policy steward; Docs steward
created: 2026-07-10
updated: 2026-07-10
policy_label: public
related:
  - ../README.md
  - ../../README.md
  - ../../../data/README.md
  - ../../../data/catalog/README.md
  - ../../../data/catalog/domain/README.md
  - ../../../data/catalog/domain/people-dna-land/README.md
  - ../../../data/registry/README.md
  - ../../../data/receipts/README.md
  - ../../../data/proofs/README.md
  - ../../../data/published/README.md
  - ../../../release/README.md
  - ../../../docs/domains/people-dna-land/README.md
  - ../../../docs/doctrine/directory-rules.md
tags: [kfm, catalog, domain, people-dna-land, consent, privacy, compatibility-root, redirect, data-catalog-domain, non-authoritative, drift-fence]
notes:
  - Root-level catalog/domain/people-dna-land/ is a compatibility redirect and drift-control fence only.
  - Canonical People DNA Land catalog records belong under data/catalog/domain/people-dna-land/.
  - This file does not prove migration completeness, validator coverage, source-rights closure, receipt/proof closure, release approval, publication readiness, or CI enforcement.
[/KFM_META_BLOCK_V2] -->

<a id='top'></a>

# People DNA Land Domain Catalog Compatibility Redirect

`catalog/domain/people-dna-land/`

This directory exists only to keep the legacy root-level `catalog/domain/` tree aligned with the repository-supported domain catalog lanes. It is not the canonical People DNA Land catalog home, not a registry, not a receipt/proof store, not a release or publication surface, and not a producer output target.

## Evidence Basis

| Evidence | Supports | Does not prove |
|---|---|---|
| `catalog/domain/README.md` | Root-level `catalog/domain/` is a compatibility redirect and drift fence. | Complete migration or enforcement maturity. |
| `data/catalog/domain/README.md` | Canonical domain catalog lanes live under `data/catalog/domain/`. | That every downstream record, schema, or validator is complete. |
| `data/catalog/domain/people-dna-land/README.md` | `people-dna-land/` is a repository-recognized canonical People DNA Land catalog lane. | Source-rights closure, proof closure, release approval, or public delivery readiness. |
| `docs/domains/people-dna-land/README.md` | Domain doctrine exists outside this redirect path. | That this directory may host domain doctrine or implementation files. |
| Existing sibling redirects in `catalog/domain/` | Child compatibility README pattern is established for root-level domain lanes. | Permission to mirror every nested canonical sublane here. |

## Canonical Homes

| Family | Canonical home |
|---|---|
| People DNA Land catalog records | `data/catalog/domain/people-dna-land/` |
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
- Do not store living-person, DNA, consent, identity graph, parcel ownership, or title-claim records in this redirect path.
- Do not turn AI-generated language, genealogy hints, assessor data, or DNA matches into sovereign truth or public claims.
- Consent, revocation, restricted evidence, receipts, proofs, and public-safe release derivatives must remain in their governed owning roots.

## Directory Shape

Expected root-level compatibility shape:

```text
catalog/domain/people-dna-land/
+-- README.md
```

Nested canonical sublanes should not be mirrored here unless a future repository contract explicitly requires a root-level redirect for that child path.

## Change Rules

1. Prefer updating the canonical `data/catalog/domain/people-dna-land/` lane for catalog work.
2. Keep this directory limited to redirect and drift-control documentation.
3. Link to owning repository documents instead of duplicating authority.
4. Mark unknown or unverified behavior as `NEEDS VERIFICATION` instead of implying maturity.
5. Preserve source-role separation, governed publication, receipts/proofs separation, and policy-safe public surfaces.

## Open Verification Items

- Actual migration completeness from any legacy root-level People DNA Land catalog material: `NEEDS VERIFICATION`.
- CI enforcement for this redirect boundary: `NEEDS VERIFICATION`.
- Completeness of downstream schemas, examples, fixtures, validators, release manifests, and public surfaces: owned outside this directory and `NEEDS VERIFICATION` here.

## Definition of Done

This redirect is complete when the root-level path exists, points to the canonical People DNA Land catalog lane, forbids trust-bearing content in the compatibility path, and does not duplicate authority owned by registry, receipt, proof, release, published, schema, policy, source, tool, or application directories.

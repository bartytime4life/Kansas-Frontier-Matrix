<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-domains-readme
title: connectors/domains/ — Domain-Scoped Connector Lane
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Source steward · Connector steward · Domain stewards · Data steward · Docs steward
created: 2026-06-16
updated: 2026-06-16
policy_label: public
related:
  - ../README.md
  - ../../docs/domains/README.md
  - ../../data/registry/sources/
  - ../../data/raw/
  - ../../data/quarantine/
  - ../../data/receipts/
  - ../../data/proofs/
  - ../../policy/
  - ../../release/
tags: [kfm, connectors, domains, source-admission, raw, quarantine, governance]
notes:
  - "connectors/domains/ is a connector grouping lane for domain-scoped source intake only."
  - "Domain-specific connector output may enter data/raw/ or data/quarantine/ only."
  - "This lane does not create domain doctrine, lifecycle truth, package authority, pipeline authority, policy authority, schema authority, or release authority."
  - "Specific child domains, connector modules, tests, fixtures, and CI enforcement remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Domain-Scoped Connectors

`connectors/domains/`

`connectors/domains/` is a connector grouping lane for domain-scoped source intake and admission helpers.

It may organize connector code by domain when a source-intake concern is primarily domain-scoped. It must not become domain doctrine, policy authority, schema authority, catalog authority, triplet authority, evidence closure, release approval, package authority, pipeline authority, or publication authority.

> [!IMPORTANT]
> **Status:** draft / `NEEDS VERIFICATION`  
> **Owning root:** `connectors/`  
> **Responsibility:** domain-scoped connector grouping and admission code  
> **Truth posture:** README path CONFIRMED; parent `connectors/` root CONFIRMED as source-specific fetch/admission root; `docs/domains/` root CONFIRMED as human-facing domain documentation; child-domain connector inventory, modules, tests, fixtures, and CI enforcement remain UNKNOWN / NEEDS VERIFICATION.

## Purpose

Use this folder when connector code is best organized by KFM domain lane rather than by a single source family.

A domain-scoped connector may retrieve or stage candidate source material, preserve source metadata, record retrieval context, and produce admission outputs for lifecycle review. It must not decide truth, write processed records, create catalog or triplet authority, close EvidenceBundles, release artifacts, or bypass steward review.

## Canonical fit

```text
connectors/
└── domains/
    └── README.md
```

Related roots:

```text
docs/domains/                 # human-facing domain documentation and navigation
data/registry/sources/        # source descriptors and activation state
data/raw/                     # admitted raw/staged source payloads
data/quarantine/              # held material requiring review
data/receipts/                # process and validation receipts
data/proofs/                  # EvidenceBundles and proof packs
policy/                       # source and publication rules
release/                      # release decisions and rollback/correction state
packages/domains/             # reusable domain helper libraries
pipelines/domains/            # executable domain processing logic
pipeline_specs/               # declarative pipeline definitions
```

## Authority boundary

```text
connectors/domains/
├── domain-scoped connector grouping
├── source-intake adapters
├── admission metadata helpers
├── source-role preservation helpers
└── connector documentation

OUTPUT LIMIT:
  data/raw/
  data/quarantine/

NOT HERE:
  domain doctrine
  reusable domain package code
  pipeline transformation logic
  processed data
  catalog records
  triplet records
  receipts/proofs as authority
  release decisions
  published artifacts
  policy rules
  schemas/contracts
  source registry rows as authority
```

## Allowed contents

| Allowed item | Example | Required posture |
|---|---|---|
| Domain connector sublane | `atmosphere/`, `hydrology/`, `flora/` | Must stay connector/admission scoped |
| Source adapter | domain-scoped source client | Must preserve source role and provenance |
| Admission helper | checksum, content type, timestamp, source metadata | Must write only raw/quarantine admission outputs |
| Connector docs | README or source-intake notes | Must not claim source admission or release state unless verified |
| Test references | no-network fixture notes | Tests and fixtures live in their owning roots |

## Forbidden contents

| Do not store here | Correct home |
|---|---|
| Domain doctrine or scope | `docs/domains/` |
| Reusable domain helper package code | `packages/domains/` |
| Executable domain transformation pipeline logic | `pipelines/domains/` |
| Declarative pipeline definitions | `pipeline_specs/` |
| Processed records | `data/processed/` after governed processing |
| Catalog or triplet records | `data/catalog/`, `data/triplets/` |
| Source descriptors or registry rows as authority | `data/registry/sources/` or governed registry homes |
| Receipts and proof packs as authority | `data/receipts/`, `data/proofs/` |
| Published artifacts or public layers | `data/published/` after governed release |
| Release decisions or rollback/correction records | `release/` |
| Policy rules and publication decisions | `policy/` and release-governed decision homes |
| Machine schemas | `schemas/contracts/v1/` |
| Human contracts and object meaning | `contracts/` |
| Generated reports and build/QA outputs | `artifacts/` |

## Domain-scoped admission posture

Domain-scoped connector code should preserve source and domain boundaries instead of collapsing them.

Connector code should preserve source identity, source role, domain lane target when applicable, retrieval time, source time where available, content digest, source limitations, review-needed flags, quarantine reason when review is required, and pointers needed for later EvidenceBundle and release review.

Connector code should not convert a candidate into a confirmed public claim. It should route material through governed lifecycle stages and leave confirmation, transformation, publication, correction, and rollback to their owning roots.

## Validation expectations

Before relying on a domain-scoped connector, verify:

- source descriptors exist and are active;
- child-domain placement is intentional and documented;
- connector tests use no-network fixtures where practical;
- output paths are limited to raw/quarantine admission lanes;
- source role, time, limitations, and sensitivity fields are preserved;
- downstream receipts/proofs/release records are produced only by governed stages outside this connector.

## Safe change pattern

For changes under `connectors/domains/`:

1. Confirm the file is connector code, connector docs, or connector-facing support material.
2. Confirm child-domain placement does not duplicate source-family connector lanes without a migration note.
3. Confirm it does not write processed, catalog, triplet, published, or release records directly.
4. Confirm source descriptors, source role, time, and limitation notes are preserved.
5. Confirm tests/fixtures are updated or explicitly marked `NEEDS VERIFICATION`.
6. Update docs or explain why the change is documentation-only.

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Actual `connectors/domains/` contents are inventoried.
- [ ] Child-domain connector placement is documented.
- [ ] Source coverage is tied to source descriptors.
- [ ] Outputs are verified to enter only raw/quarantine admission lanes.
- [ ] No domain doctrine, package, pipeline, processed, catalog, triplet, published, release, schema, policy, proof, receipt, registry, fixture, or report authority lives here.
- [ ] No-network tests and fixtures are verified or marked `NEEDS VERIFICATION`.
- [ ] CI/review behavior is verified or marked `NEEDS VERIFICATION`.

## Status summary

`connectors/domains/` is for domain-scoped connector grouping and source-admission code only. It is not a source of domain truth, policy authority, schema authority, catalog/triplet authority, evidence closure, release authority, publication authority, reusable package authority, or pipeline authority.

<p align="right"><a href="#top">Back to top</a></p>

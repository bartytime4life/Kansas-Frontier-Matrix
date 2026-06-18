<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-domains-pdl-census-readme
title: connectors/domains/people-dna-land/census/ README
type: readme
version: v0.1
status: draft
owners: OWNER_TBD
created: 2026-06-16
updated: 2026-06-16
policy_label: public
related:
  - ../../README.md
  - ../../../census/README.md
  - ../../../../docs/sources/catalog/census/README.md
  - ../../../../docs/domains/people-dna-land/SENSITIVITY_PROFILE.md
  - ../../../../data/raw/people-dna-land/
  - ../../../../data/quarantine/people-dna-land/
tags: [kfm, connectors, domains, census, source-admission]
notes:
  - "Domain-scoped Census connector lane."
  - "Outputs are limited to raw or quarantine admission lanes."
  - "Relationship to connectors/census/ remains NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# PDL Census Connector

`connectors/domains/people-dna-land/census/`

This folder is a domain-scoped connector lane for Census source intake used by the PDL domain.

It may contain connector code and connector-local documentation for source admission. It must not become domain doctrine, source-family authority, policy authority, schema authority, catalog authority, triplet authority, proof authority, release authority, reusable package authority, pipeline authority, or publication authority.

## Purpose

Use this folder only when Census connector behavior is intentionally scoped to the PDL domain.

Connector code may retrieve or stage candidate source material, preserve product metadata, record retrieval context, and prepare raw or quarantine admission outputs. It must not decide truth, write processed records, create catalog or triplet records, close proof bundles, release artifacts, or bypass review.

## Canonical fit

```text
connectors/
└── domains/
    └── people-dna-land/
        └── census/
            └── README.md
```

## Related roots

```text
connectors/domains/              # domain-scoped connector grouping
connectors/census/               # direct Census connector lane; relationship NEEDS VERIFICATION
docs/sources/catalog/census/     # Census source-family catalog pages
docs/domains/people-dna-land/    # domain documentation
data/raw/people-dna-land/        # raw staged outputs
data/quarantine/people-dna-land/ # held material requiring review
policy/                          # policy rules
release/                         # release decisions
```

## Authority boundary

```text
OUTPUT LIMIT:
  data/raw/people-dna-land/
  data/quarantine/people-dna-land/

NOT HERE:
  domain doctrine
  source-family authority
  reusable package code
  pipeline logic
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

| Allowed item | Required posture |
|---|---|
| Domain-scoped source adapter | Preserve source role, product family, and vintage. |
| Admission helper | Write only raw/quarantine admission outputs. |
| Source-role helper | Preserve role and limitation fields. |
| Connector docs | Do not claim admission or release state unless verified. |
| Test references | Point to owning test or fixture roots. |

## Forbidden contents

| Do not store here | Correct home |
|---|---|
| Domain doctrine or scope | `docs/domains/people-dna-land/` |
| Census source-family authority | `docs/sources/catalog/census/` and `data/registry/sources/` |
| Reusable package code | `packages/domains/people-dna-land/` |
| Executable transformation logic | `pipelines/domains/people-dna-land/` |
| Declarative pipeline definitions | `pipeline_specs/people-dna-land/` |
| Processed records | `data/processed/` |
| Catalog or triplet records | `data/catalog/`, `data/triplets/` |
| Release decisions | `release/` |
| Policy rules | `policy/` |
| Schemas or contracts | `schemas/`, `contracts/` |
| Generated reports | `artifacts/` |

## Admission posture

Connector code should preserve source family, product family, vintage, geography unit, retrieval time, source time when available, content digest, source role, aggregation unit, uncertainty fields when present, limitation notes, review-needed flags, and quarantine reason when review is needed.

Connector output should route through governed lifecycle stages and leave confirmation, transformation, publication, correction, and rollback to their owning roots.

## Placement warning

`connectors/census/` already exists as a direct Census connector lane. This domain-scoped lane is acceptable only if the repository intentionally supports this placement or is in migration.

| Claim | Status |
|---|---|
| This README path exists after this change | CONFIRMED |
| Direct `connectors/census/` lane exists | CONFIRMED |
| Canonical active connector lane | NEEDS VERIFICATION |
| Long-term coexistence | NEEDS VERIFICATION / ADR candidate |

## Validation expectations

Before relying on this connector, verify:

- source descriptors exist and are active;
- placement is intentional and documented;
- overlap with `connectors/census/` is resolved or documented;
- tests use no-network fixtures where practical;
- output paths are limited to raw/quarantine admission lanes;
- downstream receipts, proofs, and release records are produced only outside this connector.

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Actual folder contents are inventoried.
- [ ] Relationship to `connectors/census/` is resolved or documented.
- [ ] Source coverage is tied to source descriptors.
- [ ] Outputs are verified to enter only raw/quarantine admission lanes.
- [ ] No doctrine, source-family authority, package, pipeline, processed, catalog, triplet, published, release, schema, policy, proof, receipt, registry, fixture, or report authority lives here.
- [ ] Tests, fixtures, and CI behavior are verified or marked `NEEDS VERIFICATION`.

## Status summary

`connectors/domains/people-dna-land/census/` is for domain-scoped Census source-admission code only. It is not a source of truth, source-family authority, policy authority, schema authority, catalog/triplet authority, proof closure, release authority, publication authority, reusable package authority, or pipeline authority.

<p align="right"><a href="#top">Back to top</a></p>

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-domains-pdl-readme
title: connectors/domains/people-dna-land/ README
type: readme
version: v0.1
status: draft
owners: OWNER_TBD
created: 2026-06-16
updated: 2026-06-16
policy_label: public
related:
  - ../README.md
  - ../../../docs/domains/people-dna-land/SENSITIVITY_PROFILE.md
  - ../../../data/raw/people-dna-land/
  - ../../../data/quarantine/people-dna-land/
tags: [kfm, connectors, domains, source-admission]
notes:
  - "Domain-scoped connector grouping lane."
  - "Outputs are limited to raw or quarantine admission lanes."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# PDL Domain Connectors

`connectors/domains/people-dna-land/`

This folder is a domain-scoped connector grouping lane. It may contain connector-local documentation and source-admission helpers for this domain lane.

It must not become domain doctrine, policy authority, schema authority, catalog authority, triplet authority, proof authority, release authority, package authority, pipeline authority, or publication authority.

## Purpose

Use this folder for connector-facing material only.

Connector code may prepare candidate source material for governed admission. It must not decide final truth, write processed records, create catalog or triplet records, release artifacts, or bypass review.

## Canonical fit

```text
connectors/
└── domains/
    └── people-dna-land/
        └── README.md
```

## Related roots

```text
connectors/domains/              # domain-scoped connector grouping
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
  package code
  pipeline logic
  processed data
  catalog records
  triplet records
  proof authority
  release decisions
  published artifacts
  policy rules
  schemas/contracts
  registry rows
```

## Allowed contents

| Allowed item | Required posture |
|---|---|
| Source adapter | Preserve source identity and review posture. |
| Admission helper | Write only raw or quarantine admission outputs. |
| Connector docs | Do not claim admission or release state unless verified. |
| Test references | Point to owning test or fixture roots. |

## Forbidden contents

| Do not store here | Correct home |
|---|---|
| Domain doctrine or scope | `docs/domains/people-dna-land/` |
| Reusable package code | `packages/domains/people-dna-land/` |
| Transformation logic | `pipelines/domains/people-dna-land/` |
| Processed records | `data/processed/` |
| Catalog or triplet records | `data/catalog/`, `data/triplets/` |
| Release decisions | `release/` |
| Policy rules | `policy/` |
| Schemas or contracts | `schemas/`, `contracts/` |
| Generated reports | `artifacts/` |

## Validation expectations

Before relying on this connector lane, verify:

- source descriptors exist and are active;
- child connector placement is intentional and documented;
- tests use no-network fixtures where practical;
- output paths are limited to raw or quarantine admission lanes;
- downstream receipts, proofs, and release records are produced only outside this connector.

## Status summary

`connectors/domains/people-dna-land/` is for domain-scoped source-admission code only. It is not a source of truth, policy authority, schema authority, catalog/triplet authority, proof closure, release authority, publication authority, reusable package authority, or pipeline authority.

<p align="right"><a href="#top">Back to top</a></p>

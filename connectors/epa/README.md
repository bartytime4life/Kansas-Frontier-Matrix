<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-epa-readme
title: connectors/epa/ README
type: readme
version: v0.1
status: draft
owners: OWNER_TBD
created: 2026-06-16
updated: 2026-06-16
policy_label: public
related:
  - ../README.md
  - ../../docs/sources/catalog/epa/README.md
  - ../../data/raw/
  - ../../data/quarantine/
tags: [kfm, connectors, epa, source-admission]
notes:
  - "Source intake lane only."
  - "Outputs are limited to raw or quarantine admission lanes."
[/KFM_META_BLOCK_V2] -->

# EPA Connector

> Source-specific intake and admission lane for EPA source programs used by KFM.

`connectors/epa/`

## Scope

This folder may contain connector-local documentation and source-admission helpers for EPA source material.

It must not become source truth, domain doctrine, policy authority, schema authority, catalog authority, triplet authority, proof authority, release authority, pipeline authority, or publication authority.

## Repo fit

```text
connectors/
└── epa/
    └── README.md
```

Related roots:

```text
connectors/              # source-specific fetch and admission code
docs/sources/catalog/epa/# source-family documentation
data/raw/                # raw staged outputs
data/quarantine/         # held material requiring review
policy/                  # policy rules
release/                 # release decisions
```

## Authority boundary

```text
OUTPUT LIMIT:
  data/raw/
  data/quarantine/

NOT HERE:
  processed data
  catalog records
  triplet records
  proof authority
  release decisions
  published artifacts
  policy rules
  schemas/contracts
  source registry rows
  generated reports
```

## Inputs

| Accepted item | Required posture |
|---|---|
| Source adapter | Preserve source identity and review posture. |
| Admission helper | Prepare raw or quarantine admission output only. |
| Connector docs | Do not claim admission or release state unless verified. |

## Exclusions

| Do not store here | Correct home |
|---|---|
| Source-family documentation | `docs/sources/catalog/epa/` |
| Source descriptors | `data/registry/sources/` |
| Processed records | `data/processed/` |
| Catalog or triplet records | `data/catalog/`, `data/triplets/` |
| Release decisions | `release/` |
| Policy rules | `policy/` |
| Generated reports | `artifacts/` |

## Validation

Before relying on this connector, verify source descriptors, endpoint assumptions, tests, fixtures, output paths, and downstream receipt/proof/release ownership.

## Status summary

`connectors/epa/` is for source-admission code only. It is not source truth, policy authority, schema authority, catalog/triplet authority, proof closure, release authority, publication authority, or pipeline authority.

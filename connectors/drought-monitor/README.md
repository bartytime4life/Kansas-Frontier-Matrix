<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-drought-monitor-readme
title: connectors/drought-monitor/ README
type: readme
version: v0.1
status: draft
owners: OWNER_TBD
created: 2026-06-16
updated: 2026-06-16
policy_label: public
related:
  - ../README.md
  - ../../docs/sources/catalog/drought_monitor/README.md
  - ../../docs/sources/catalog/drought_monitor/drought-monitor.md
  - ../../data/registry/sources/
  - ../../data/raw/
  - ../../data/quarantine/
  - ../../policy/
  - ../../release/
tags: [kfm, connectors, drought-monitor, usdm, drought, source-admission]
notes:
  - "Connector lane for U.S. Drought Monitor source intake."
  - "Outputs are limited to raw or quarantine admission lanes."
  - "The source-family catalog marks drought_monitor as PROPOSED beyond the connector roots listed in directory rules."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Drought Monitor Connector

`connectors/drought-monitor/`

This folder is the connector lane for U.S. Drought Monitor source intake and admission helpers.

It may contain connector-local documentation and source-admission code for drought-classification source material. It must not become drought truth, hydrology truth, agriculture truth, hazards truth, policy authority, schema authority, catalog authority, triplet authority, proof authority, release authority, pipeline authority, or publication authority.

## Purpose

Use this folder for connector-facing material only.

Connector code may retrieve or stage candidate source material, preserve source metadata, record retrieval context, and prepare raw or quarantine admission outputs. It must not decide final truth, write processed records, create catalog or triplet records, release artifacts, or bypass review.

## Canonical fit

```text
connectors/
└── drought-monitor/
    └── README.md
```

## Related roots

```text
connectors/                              # connector root
docs/sources/catalog/drought_monitor/    # USDM source-family catalog docs
data/registry/sources/                   # source descriptors and activation state
data/raw/                                # raw staged outputs
data/quarantine/                         # held material requiring review
policy/                                  # policy rules
release/                                 # release decisions
```

## Authority boundary

```text
OUTPUT LIMIT:
  data/raw/
  data/quarantine/

NOT HERE:
  source-family truth
  domain doctrine
  processed data
  catalog records
  triplet records
  receipts/proofs as authority
  release decisions
  published artifacts
  policy rules
  schemas/contracts
  registry rows
  generated reports
```

## Allowed contents

| Allowed item | Required posture |
|---|---|
| Source adapter | Preserve source identity, release vintage, and review posture. |
| Admission helper | Write only raw or quarantine admission outputs. |
| Source-role helper | Preserve role, time, class, and limitation fields. |
| Connector docs | Do not claim admission or release state unless verified. |
| Test references | Point to owning test or fixture roots. |

## Forbidden contents

| Do not store here | Correct home |
|---|---|
| Source catalog authority | `docs/sources/catalog/drought_monitor/` and source registry homes |
| Domain doctrine or scope | `docs/domains/` |
| Processed records | `data/processed/` |
| Catalog or triplet records | `data/catalog/`, `data/triplets/` |
| Release decisions | `release/` |
| Policy rules | `policy/` |
| Schemas or contracts | `schemas/`, `contracts/` |
| Generated reports | `artifacts/` |

## Admission posture

USDM source intake should preserve source identity, product family, release date or week, retrieval time, content digest, classification fields, source role, limitation notes, review-needed flags, and quarantine reason when review is required.

Drought Monitor material may inform hydrology, agriculture, hazards, habitat, and related reasoning, but connector output is still admission material. Confirmation, transformation, publication, correction, and rollback belong to governed downstream stages.

## Placement warning

The source-family catalog describes `drought_monitor` as a proposed source family beyond the connector roots listed in directory rules. Treat this connector lane as draft until source activation, placement, tests, and CI behavior are verified.

| Claim | Status |
|---|---|
| This README path exists after this change | CONFIRMED |
| Source-family catalog page exists | CONFIRMED |
| Connector lane ratification | NEEDS VERIFICATION |
| Active endpoint behavior | NEEDS VERIFICATION |

## Validation expectations

Before relying on this connector, verify:

- source descriptors exist and are active;
- placement is intentional and documented;
- endpoint and cadence assumptions are documented;
- tests use no-network fixtures where practical;
- output paths are limited to raw or quarantine admission lanes;
- downstream receipts, proofs, catalog/triplet records, and release records are produced only outside this connector.

## Status summary

`connectors/drought-monitor/` is for U.S. Drought Monitor source-admission code only. It is not source-family truth, domain truth, policy authority, schema authority, catalog/triplet authority, proof closure, release authority, publication authority, or pipeline authority.

<p align="right"><a href="#top">Back to top</a></p>

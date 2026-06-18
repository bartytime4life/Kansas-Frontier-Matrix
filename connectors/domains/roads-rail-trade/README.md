<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-domains-roads-rail-trade-readme
title: connectors/domains/roads-rail-trade/ README
type: readme
version: v0.1
status: draft
owners: OWNER_TBD
created: 2026-06-16
updated: 2026-06-16
policy_label: public
related:
  - ../README.md
  - ../../../docs/domains/roads-rail-trade/README.md
  - ../../../data/raw/roads-rail-trade/
  - ../../../data/quarantine/roads-rail-trade/
  - ../../../policy/
  - ../../../release/
tags: [kfm, connectors, domains, roads-rail-trade, transport, source-admission]
notes:
  - "Domain-scoped connector grouping lane for roads, rail, and trade-route source intake."
  - "Outputs are limited to raw or quarantine admission lanes."
  - "Implementation inventory, tests, fixtures, and CI wiring remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Roads-Rail-Trade Domain Connectors

`connectors/domains/roads-rail-trade/`

This folder is a domain-scoped connector grouping lane for roads, rail, trade-route, mobility, and transport source intake.

It may contain connector-local documentation and source-admission helpers for the Roads / Rail / Trade Routes domain. It must not become domain doctrine, policy authority, schema authority, contract authority, catalog authority, triplet authority, proof authority, release authority, package authority, pipeline authority, or publication authority.

## Purpose

Use this folder for connector-facing material only.

Connector code may prepare candidate source material for governed admission. It may preserve source identifiers, retrieval context, temporal context, source role, and limitations. It must not decide final truth, write processed records, create catalog or triplet records, release artifacts, or bypass review.

## Canonical fit

```text
connectors/
└── domains/
    └── roads-rail-trade/
        └── README.md
```

## Related roots

```text
connectors/domains/               # domain-scoped connector grouping
docs/domains/roads-rail-trade/    # domain documentation
data/raw/roads-rail-trade/        # raw staged outputs
data/quarantine/roads-rail-trade/ # held material requiring review
policy/                           # policy rules
release/                          # release decisions
contracts/transport/              # semantic contracts, presence NEEDS VERIFICATION
schemas/contracts/v1/transport/   # machine shapes, presence NEEDS VERIFICATION
```

## Authority boundary

```text
OUTPUT LIMIT:
  data/raw/roads-rail-trade/
  data/quarantine/roads-rail-trade/

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
| Source adapter | Preserve source identity, source role, and review posture. |
| Admission helper | Write only raw or quarantine admission outputs. |
| Source-role helper | Preserve role, time, and limitation fields. |
| Connector docs | Do not claim admission or release state unless verified. |
| Test references | Point to owning test or fixture roots. |

## Forbidden contents

| Do not store here | Correct home |
|---|---|
| Domain doctrine or scope | `docs/domains/roads-rail-trade/` |
| Reusable package code | `packages/domains/roads-rail-trade/` or verified package root |
| Transformation logic | `pipelines/domains/roads-rail-trade/` |
| Processed records | `data/processed/` |
| Catalog or triplet records | `data/catalog/`, `data/triplets/` |
| Release decisions | `release/` |
| Policy rules | `policy/` |
| Schemas or contracts | `schemas/`, `contracts/` |
| Generated reports | `artifacts/` |

## Admission posture

Connector code should preserve source identity, source role, domain target, retrieval time, source time when available, valid time when available, content digest, limitation notes, review-needed flags, and quarantine reason when review is required.

Transport source intake must not collapse modern linework, historic route evidence, administrative road authority, rail operator status, or derived graph edges into one unreviewed truth object. Connector output should route through governed lifecycle stages and leave confirmation, transformation, publication, correction, and rollback to their owning roots.

## Validation expectations

Before relying on this connector lane, verify:

- source descriptors exist and are active;
- child connector placement is intentional and documented;
- tests use no-network fixtures where practical;
- output paths are limited to raw or quarantine admission lanes;
- downstream receipts, proofs, catalog/triplet records, and release records are produced only outside this connector.

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Actual folder contents are inventoried.
- [ ] Child connector placement is documented.
- [ ] Source coverage is tied to source descriptors.
- [ ] Outputs are verified to enter only raw or quarantine admission lanes.
- [ ] No doctrine, package, pipeline, processed, catalog, triplet, published, release, schema, policy, proof, receipt, registry, fixture, or report authority lives here.
- [ ] Tests, fixtures, and CI behavior are verified or marked `NEEDS VERIFICATION`.

## Status summary

`connectors/domains/roads-rail-trade/` is for domain-scoped source-admission code only. It is not a source of transport truth, policy authority, schema authority, catalog/triplet authority, proof closure, release authority, publication authority, reusable package authority, or pipeline authority.

<p align="right"><a href="#top">Back to top</a></p>

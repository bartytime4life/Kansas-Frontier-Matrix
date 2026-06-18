<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-archaeology-readme
title: connectors/archaeology/ — Archaeology Source Connector Lane
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Archaeology steward · Cultural-review reviewer · Source steward · Connector steward · Data steward · Docs steward
created: 2026-06-16
updated: 2026-06-16
policy_label: public
related:
  - ../README.md
  - ../../docs/domains/archaeology/README.md
  - ../../data/registry/sources/
  - ../../data/raw/archaeology/
  - ../../data/quarantine/archaeology/
  - ../../data/receipts/archaeology/
  - ../../data/proofs/archaeology/
  - ../../policy/domains/archaeology/
  - ../../schemas/contracts/v1/domains/archaeology/
  - ../../release/
tags: [kfm, connectors, archaeology, cultural-heritage, source-admission, raw, quarantine, review, governance]
notes:
  - "connectors/archaeology/ is for archaeology and cultural-heritage source-specific intake and admission code only."
  - "Connector output may enter data/raw/ or data/quarantine/ only."
  - "Archaeology source material has strict review and public-safety boundaries; connector code must not promote or expose protected details."
  - "Specific connector modules, source coverage, tests, fixtures, and CI enforcement remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology Connectors

`connectors/archaeology/`

`connectors/archaeology/` is the source-specific connector lane for archaeology and cultural-heritage intake and admission helpers.

It may contain code and connector documentation that supports governed source intake. It must not become archaeology truth, cultural review authority, policy authority, schema authority, catalog/triplet authority, evidence closure, release approval, or publication authority.

> [!IMPORTANT]
> **Status:** draft / `NEEDS VERIFICATION`  
> **Owning root:** `connectors/`  
> **Responsibility:** archaeology source-specific intake and admission code  
> **Truth posture:** README path CONFIRMED; parent `connectors/` root CONFIRMED as source-specific fetch/admission root; archaeology documentation root CONFIRMED as canonical domain documentation; connector implementation, source coverage, tests, fixtures, network behavior, and CI enforcement remain UNKNOWN / NEEDS VERIFICATION.

> [!CAUTION]
> Archaeology connector output is admission material, not proof of a site, artifact, feature, context, chronology, or cultural-heritage claim. Treat source records as candidates until source descriptors, rights, review, evidence closure, policy checks, and release controls are satisfied.

## Purpose

Use this folder for archaeology-specific connector code and documentation that supports governed source intake.

A connector may retrieve or stage candidate source material, preserve source metadata, record retrieval context, and produce admission outputs for lifecycle review. It must not decide truth, write processed records, create catalog/triplet authority, close EvidenceBundles, release artifacts, or bypass steward and cultural review.

## Canonical fit

```text
connectors/
└── archaeology/
    └── README.md
```

Related roots:

```text
docs/domains/archaeology/              # canonical human-facing domain documentation
data/registry/sources/                 # source descriptors and activation state
data/raw/archaeology/                  # admitted raw/staged source payloads
data/quarantine/archaeology/           # held material requiring review
data/receipts/archaeology/             # process and validation receipts
data/proofs/archaeology/               # EvidenceBundles and proof packs
policy/domains/archaeology/            # policy/admissibility rules
schemas/contracts/v1/domains/archaeology/ # machine-checkable shapes
release/                               # release decisions and rollback/correction state
```

## Authority boundary

```text
connectors/archaeology/
├── source-specific intake logic
├── admission metadata helpers
├── source-role preservation helpers
└── connector documentation

OUTPUT LIMIT:
  data/raw/archaeology/
  data/quarantine/archaeology/

NOT HERE:
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
| Source adapter | connector for one approved source family | Must preserve source role and provenance |
| Admission helper | checksum, content type, timestamp, source metadata | Must write only raw/quarantine admission outputs |
| Review routing helper | quarantine reason, review-needed flag | Must not bypass review |
| Connector docs | source-specific notes | Must not claim admission or release state unless verified |
| Test references | no-network fixture notes | Tests and fixtures live in their owning roots |

## Forbidden contents

| Do not store here | Correct home |
|---|---|
| Processed archaeology or cultural-heritage records | `data/processed/` after governed processing |
| Catalog or triplet records | `data/catalog/`, `data/triplets/` |
| Source descriptors or registry rows as authority | `data/registry/sources/` or governed registry homes |
| Receipts and proof packs as authority | `data/receipts/`, `data/proofs/` |
| Published artifacts or public layers | `data/published/` after governed release |
| Release decisions or rollback/correction records | `release/` |
| Policy rules and publication decisions | `policy/` and release-governed decision homes |
| Machine schemas | `schemas/contracts/v1/` |
| Human contracts and object meaning | `contracts/` |
| Reusable domain helper package code | `packages/` |
| Executable transformation pipeline logic | `pipelines/` |
| Declarative pipeline definitions | `pipeline_specs/` |
| Generated reports and build/QA outputs | `artifacts/` |

## Archaeology admission posture

Archaeology source intake is deny-by-default for protected detail until review says otherwise. Connector code should preserve:

- source identity and source role;
- retrieval time and source time when available;
- content digest and source locator;
- source limitations and rights notes;
- review-needed flags;
- quarantine reason when review is required;
- pointers needed for later EvidenceBundle and release review.

Connector code should not convert a candidate into a confirmed public claim. It should route material through governed lifecycle stages and leave confirmation, review, transformation, publication, correction, and rollback to their owning roots.

## Validation expectations

Before relying on this connector, verify:

- source descriptors exist and are active;
- connector tests use no-network fixtures where practical;
- output paths are limited to raw/quarantine admission lanes;
- review and policy checks are invoked where required;
- protected detail is not exposed through logs, reports, or config;
- downstream receipts/proofs/release records are produced only by governed stages outside this connector.

## Safe change pattern

For changes under `connectors/archaeology/`:

1. Confirm the file is connector code, connector docs, or connector-facing support material.
2. Confirm it does not write processed, catalog, triplet, published, or release records directly.
3. Confirm source roles, rights, limitations, review state, and temporal context are preserved.
4. Confirm protected detail is routed through quarantine or review where required.
5. Confirm tests/fixtures are updated or explicitly marked `NEEDS VERIFICATION`.
6. Update docs or explain why the change is documentation-only.

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Actual `connectors/archaeology/` contents are inventoried.
- [ ] Source coverage is listed and tied to source descriptors.
- [ ] Outputs are verified to enter only raw/quarantine admission lanes.
- [ ] No processed, catalog, triplet, published, release, schema, policy, proof, receipt, registry, or package authority lives here.
- [ ] Review routing and protected-detail handling are verified or marked `NEEDS VERIFICATION`.
- [ ] No-network tests and fixtures are verified or marked `NEEDS VERIFICATION`.
- [ ] CI/review behavior is verified or marked `NEEDS VERIFICATION`.

## Status summary

`connectors/archaeology/` is for archaeology source-specific intake and admission code only. It is not a source of archaeology truth, cultural review authority, policy authority, schema authority, catalog/triplet authority, evidence closure, release authority, publication authority, or reusable domain package authority.

<p align="right"><a href="#top">Back to top</a></p>

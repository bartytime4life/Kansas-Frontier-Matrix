<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-domains-agriculture-readme
title: connectors/domains/agriculture/ — Agriculture Domain-Scoped Connector Lane
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Agriculture steward · Source steward · Connector steward · Data steward · Docs steward
created: 2026-06-16
updated: 2026-06-16
policy_label: public
related:
  - ../README.md
  - ../../agriculture/README.md
  - ../../../docs/domains/agriculture/README.md
  - ../../../data/registry/sources/
  - ../../../data/raw/agriculture/
  - ../../../data/quarantine/agriculture/
  - ../../../data/receipts/agriculture/
  - ../../../data/proofs/agriculture/
  - ../../../policy/domains/agriculture/
  - ../../../packages/domains/agriculture/
  - ../../../pipelines/domains/agriculture/
  - ../../../pipeline_specs/agriculture/
  - ../../../release/
tags: [kfm, connectors, domains, agriculture, source-admission, raw, quarantine, governance]
notes:
  - "connectors/domains/agriculture/ is a domain-scoped connector lane for agriculture source intake only."
  - "Connector output may enter data/raw/agriculture/ or data/quarantine/agriculture/ only."
  - "This lane does not replace connectors/agriculture/; final placement remains NEEDS VERIFICATION."
  - "Specific modules, source coverage, tests, fixtures, and CI enforcement remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Agriculture Domain-Scoped Connectors

`connectors/domains/agriculture/`

`connectors/domains/agriculture/` is a domain-scoped connector lane for agriculture source intake and admission helpers.

It may organize agriculture intake code when domain-scoped placement is intentional. It must not become agriculture truth, domain doctrine, policy authority, schema authority, catalog/triplet authority, evidence closure, release approval, reusable package authority, transformation pipeline authority, or publication authority.

> [!IMPORTANT]
> **Status:** draft / `NEEDS VERIFICATION`  
> **Owning root:** `connectors/`  
> **Responsibility:** agriculture domain-scoped connector intake and admission code  
> **Truth posture:** README path CONFIRMED; `connectors/domains/` parent README CONFIRMED; direct `connectors/agriculture/` README CONFIRMED; child-domain connector placement, duplication posture, modules, tests, fixtures, and CI enforcement remain UNKNOWN / NEEDS VERIFICATION.

## Purpose

Use this folder for agriculture connector code and documentation only when the connector concern is intentionally domain-scoped under `connectors/domains/`.

A connector may retrieve or stage candidate source material, preserve source metadata, record retrieval context, and produce admission outputs for lifecycle review. It must not decide truth, write processed records, create catalog/triplet authority, close EvidenceBundles, release artifacts, or bypass steward review.

## Canonical fit

```text
connectors/
└── domains/
    └── agriculture/
        └── README.md
```

Related roots:

```text
connectors/domains/           # domain-scoped connector grouping
connectors/agriculture/       # direct agriculture connector lane; relationship NEEDS VERIFICATION
data/registry/sources/        # source descriptors and activation state
data/raw/agriculture/         # admitted raw/staged agriculture payloads
data/quarantine/agriculture/  # held material requiring review
data/receipts/agriculture/    # process and validation receipts
data/proofs/agriculture/      # EvidenceBundles and proof packs
policy/domains/agriculture/   # policy/admissibility rules
packages/domains/agriculture/ # reusable agriculture helpers
pipelines/domains/agriculture/# executable transformation logic
pipeline_specs/agriculture/   # declarative pipeline definitions
release/                      # release decisions and rollback/correction state
```

## Authority boundary

```text
connectors/domains/agriculture/
├── agriculture domain-scoped intake logic
├── source metadata helpers
├── admission output helpers
├── source-role preservation helpers
└── connector documentation

OUTPUT LIMIT:
  data/raw/agriculture/
  data/quarantine/agriculture/

NOT HERE:
  agriculture doctrine
  reusable agriculture package code
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
| Domain-scoped source adapter | agriculture source client | Must preserve source role and provenance |
| Admission helper | checksum, content type, timestamp, source metadata | Must write only raw/quarantine admission outputs |
| Source-role helper | source-role and limitation preservation | Must not strengthen source authority |
| Connector docs | README or source-intake notes | Must not claim source admission or release state unless verified |
| Test references | no-network fixture notes | Tests and fixtures live in their owning roots |

## Forbidden contents

| Do not store here | Correct home |
|---|---|
| Agriculture doctrine or scope | `docs/domains/agriculture/` |
| Reusable agriculture helper package code | `packages/domains/agriculture/` |
| Executable agriculture transformation pipeline logic | `pipelines/domains/agriculture/` |
| Declarative pipeline definitions | `pipeline_specs/agriculture/` |
| Processed agriculture records | `data/processed/agriculture/` after governed processing |
| Catalog or triplet records | `data/catalog/`, `data/triplets/` |
| Source descriptors or registry rows as authority | `data/registry/sources/` or governed registry homes |
| Receipts and proof packs as authority | `data/receipts/`, `data/proofs/` |
| Published artifacts or public layers | `data/published/` after governed release |
| Release decisions or rollback/correction records | `release/` |
| Policy rules and publication decisions | `policy/` and release-governed decision homes |
| Machine schemas | `schemas/contracts/v1/` |
| Human contracts and object meaning | `contracts/` |
| Generated reports and build/QA outputs | `artifacts/` |

## Agriculture admission posture

Agriculture source intake must preserve source role, limitation text, temporal context, and review state.

Connector code should preserve source identity, source role, agriculture domain target when applicable, retrieval time, source time, valid time when available, content digest, limitation text, review-needed flags, quarantine reason when review is required, and pointers needed for later EvidenceBundle and release review.

Connector code should not convert candidate source material into a confirmed public agriculture claim. It should route material through governed lifecycle stages and leave confirmation, transformation, publication, correction, and rollback to their owning roots.

## Placement warning

`connectors/agriculture/` already exists as a direct agriculture connector lane. This `connectors/domains/agriculture/` lane is acceptable only if the repository intentionally supports both patterns or is in migration.

Until verified, use these labels:

| Claim | Status |
|---|---|
| This README path exists after this change | CONFIRMED |
| Direct `connectors/agriculture/` lane exists | CONFIRMED |
| Which lane is canonical for active agriculture connector code | NEEDS VERIFICATION |
| Whether both lanes should remain long term | NEEDS VERIFICATION / ADR candidate |

## Validation expectations

Before relying on this domain-scoped connector, verify:

- source descriptors exist and are active;
- child-domain placement is intentional and documented;
- overlap with `connectors/agriculture/` is resolved or documented;
- connector tests use no-network fixtures where practical;
- output paths are limited to raw/quarantine admission lanes;
- source role, time, limitations, and review fields are preserved;
- downstream receipts/proofs/release records are produced only by governed stages outside this connector.

## Safe change pattern

For changes under `connectors/domains/agriculture/`:

1. Confirm the file is connector code, connector docs, or connector-facing support material.
2. Confirm this lane does not duplicate `connectors/agriculture/` without a migration note.
3. Confirm it does not write processed, catalog, triplet, published, or release records directly.
4. Confirm source descriptors, source role, time, and limitation notes are preserved.
5. Confirm tests/fixtures are updated or explicitly marked `NEEDS VERIFICATION`.
6. Update docs or explain why the change is documentation-only.

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Actual `connectors/domains/agriculture/` contents are inventoried.
- [ ] Relationship to `connectors/agriculture/` is resolved or documented.
- [ ] Source coverage is tied to source descriptors.
- [ ] Outputs are verified to enter only raw/quarantine admission lanes.
- [ ] No domain doctrine, package, pipeline, processed, catalog, triplet, published, release, schema, policy, proof, receipt, registry, fixture, or report authority lives here.
- [ ] No-network tests and fixtures are verified or marked `NEEDS VERIFICATION`.
- [ ] CI/review behavior is verified or marked `NEEDS VERIFICATION`.

## Status summary

`connectors/domains/agriculture/` is for agriculture domain-scoped connector grouping and source-admission code only. It is not a source of agriculture truth, policy authority, schema authority, catalog/triplet authority, evidence closure, release authority, publication authority, reusable package authority, or pipeline authority.

<p align="right"><a href="#top">Back to top</a></p>

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-agriculture-readme
title: connectors/agriculture/ — Agriculture Source Connector Lane
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Agriculture steward · Source steward · Connector steward · Data steward · Docs steward
created: 2026-06-16
updated: 2026-06-16
policy_label: public
related:
  - ../README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/domains/agriculture/README.md
  - ../../packages/domains/agriculture/README.md
  - ../../pipelines/domains/agriculture/README.md
  - ../../pipeline_specs/agriculture/README.md
  - ../../data/registry/agriculture/
  - ../../data/raw/agriculture/
  - ../../data/quarantine/agriculture/
  - ../../data/receipts/agriculture/
  - ../../data/proofs/agriculture/
  - ../../policy/domains/agriculture/
  - ../../schemas/contracts/v1/domains/agriculture/
  - ../../release/
tags: [kfm, connectors, agriculture, source-admission, raw, quarantine, rights, sensitivity, evidence, governance]
notes:
  - "connectors/agriculture/ is for agriculture source-specific fetch and admission code only."
  - "Connector output may enter data/raw/ or data/quarantine/ only; connectors do not write processed, catalog, triplet, published, or release records directly."
  - "Agriculture field-level and operator-related context requires rights, sensitivity, evidence, policy, review, and release controls before any public use."
  - "Specific connector modules, source coverage, network behavior, tests, fixtures, and CI enforcement remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Agriculture Connectors

`connectors/agriculture/`

`connectors/agriculture/` is the source-specific connector lane for agriculture intake and admission helpers.

It may contain code that fetches, stages, validates, and records source-admission context for agriculture datasets. It must not become agriculture truth, policy, schema, registry authority, pipeline transformation authority, evidence closure, release approval, or public publication authority.

> [!IMPORTANT]
> **Status:** draft / `NEEDS VERIFICATION`  
> **Owning root:** `connectors/`  
> **Responsibility:** agriculture source-specific fetch and admission code  
> **Truth posture:** README path CONFIRMED; parent `connectors/` root CONFIRMED as source-specific fetch/admission root; agriculture package boundary CONFIRMED as helper-code-only; connector implementation, source coverage, tests, fixtures, network behavior, and CI enforcement remain UNKNOWN / NEEDS VERIFICATION.

> [!CAUTION]
> Agriculture connectors must preserve source roles, rights, limitations, time, provenance, and review state. Field-level context, producer/operator context, and rights-limited source material must not be promoted, generalized, exposed, or published by connector code.

## Purpose

Use this folder for agriculture-specific connector code and documentation that supports governed source intake.

A connector may fetch or stage candidate source material, normalize source metadata enough for admission, and create admission outputs for lifecycle review. It must not decide truth, write processed records, create catalog/triplet authority, close EvidenceBundles, release artifacts, or bypass steward review.

## Canonical fit

```text
connectors/
└── agriculture/
    └── README.md
```

Related roots:

```text
data/raw/agriculture/          # accepted raw/staged source payloads
data/quarantine/agriculture/   # held material requiring review
pipelines/domains/agriculture/ # executable transformations, if present and verified
pipeline_specs/agriculture/    # declarative flow definitions, if present and verified
packages/domains/agriculture/  # reusable helper code
policy/domains/agriculture/    # policy/admissibility rules
data/registry/agriculture/     # source/rights/sensitivity registry rows
release/                       # release decisions and rollback/correction state
```

## Authority boundary

```text
connectors/agriculture/
├── source-specific fetch logic
├── admission metadata helpers
├── source-role preservation helpers
└── connector documentation

OUTPUT LIMIT:
  data/raw/agriculture/
  data/quarantine/agriculture/

NOT HERE:
  processed data
  catalog records
  triplet records
  receipts/proofs as authority
  release decisions
  published artifacts
  policy rules
  schemas/contracts
  reusable domain package code
```

## Allowed contents

| Allowed item | Example | Required posture |
|---|---|---|
| Source fetch adapters | fetch client for one approved source | Must preserve source role and provenance |
| Admission helpers | source descriptor lookup, checksum helper | Must write only raw/quarantine admission outputs |
| Connector docs | source-specific notes | Must cite source limits and review needs |
| No-network fixtures references | pointers to fixture homes | Fixtures themselves belong in accepted fixture roots |
| Connector tests references | test plan links | Tests belong under `tests/` |

## Forbidden contents

| Do not store here | Correct home |
|---|---|
| Processed agriculture records | `data/processed/` |
| Catalog or triplet records | `data/catalog/`, `data/triplets/` |
| Published artifacts or map layers | `data/published/` after governed release |
| Release decisions or rollback/correction records | `release/` |
| Policy rules and publication decisions | `policy/` and release-governed decision homes |
| Machine schemas | `schemas/contracts/v1/` |
| Human contracts and object meaning | `contracts/` |
| Reusable domain helper package code | `packages/domains/agriculture/` |
| Executable transformation pipeline logic | `pipelines/domains/agriculture/` |
| Declarative pipeline definitions | `pipeline_specs/agriculture/` |
| Lifecycle evidence, receipts, proofs, or registry rows as authority | `data/` owning subtrees |
| Generated reports and build/QA outputs | `artifacts/` |

## Agriculture intake posture

Agriculture sources often carry rights and sensitivity constraints. Connector code must:

- keep source-native identifiers separate from normalized identifiers;
- preserve source role, source time, valid time, and limitation text;
- route uncertain, rights-limited, or review-needed material to quarantine;
- avoid strengthening source authority because a field is convenient;
- avoid public-ready output claims;
- leave policy, evidence closure, release, correction, and rollback decisions to their owning roots.

## Validation expectations

Before relying on a connector here, verify:

- approved source descriptors and registry rows exist;
- fetch behavior is deterministic or fixture-backed in tests;
- output paths are limited to raw/quarantine admission lanes;
- policy and sensitivity checks are invoked where required;
- tests use no-network fixtures where practical;
- receipts/proofs/release records are produced only by governed downstream stages.

## Migration posture

If misplaced material is found here:

1. Do not treat it as authoritative until reviewed.
2. Identify the owning root.
3. Move it through a small, reviewable migration.
4. Preserve source refs, provenance notes, review notes, and rollback instructions.
5. Add a drift note if the misplaced connector material was already consumed.

## Safe change pattern

For changes under `connectors/agriculture/`:

1. Confirm the file is connector code, connector docs, or connector-facing support material.
2. Confirm it does not write processed, catalog, triplet, published, or release records directly.
3. Confirm source roles, rights, limitations, and temporal context are preserved.
4. Confirm tests/fixtures are updated or explicitly marked `NEEDS VERIFICATION`.
5. Update docs or explain why the change is documentation-only.

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Actual `connectors/agriculture/` contents are inventoried.
- [ ] Connector source coverage is listed and tied to source registry rows.
- [ ] Outputs are verified to enter only raw/quarantine admission lanes.
- [ ] No processed, catalog, triplet, published, release, schema, policy, or package authority lives here.
- [ ] No-network tests and fixtures are verified or marked `NEEDS VERIFICATION`.
- [ ] CI/review behavior is verified or marked `NEEDS VERIFICATION`.

## Status summary

`connectors/agriculture/` is for agriculture source-specific fetch and admission code only. It is not a source of agriculture truth, policy authority, schema authority, catalog/triplet authority, evidence closure, release authority, publication authority, or reusable domain package authority.

<p align="right"><a href="#top">Back to top</a></p>

# `schemas/contracts/v1/evidence/` — Evidence Schema Family Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-evidence-readme
title: schemas/contracts/v1/evidence/ — Evidence Schema Family Index
type: readme; schema-family-index; evidence-governance-boundary
authority_class: schema-family-index
version: v0.1
status: draft; real-shape-family-present; duplicate-name-conflict-visible; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — placeholder existed before v0.1 expansion
updated: 2026-07-04
policy_label: public; schemas; contracts-v1; evidence; evidence-ref; evidence-bundle; citation-validation; redaction-receipt; evidence-drawer; geo-manifest; spec-normalization; lifecycle-aware; release-gated; rollback-aware; no-parallel-authority
tags: [kfm, schemas, contracts, v1, evidence, EvidenceRef, EvidenceBundle, CitationValidationReport, RedactionReceipt, EvidenceDrawerPayload, KFMGeoManifest, spec_hash, citation, provenance, receipts, validation]
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../../../contracts/evidence/
  - ../../../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/registers/DRIFT_REGISTER.md
  - ../../../../docs/registers/VERIFICATION_BACKLOG.md
  - ../../../../fixtures/contracts/v1/evidence/
  - ../../../../policy/evidence/
  - ../../../../tools/validators/
  - ../../../../release/
notes:
  - "Expanded from a two-line placeholder at schemas/contracts/v1/evidence/README.md."
  - "This file indexes the evidence schema family; it does not store EvidenceBundle instances or proof outputs."
  - "Current search surfaced evidence_bundle.schema.json and evidence-bundle.schema.json. Treat hyphen/underscore duplicate naming as NEEDS VERIFICATION until steward resolution."
  - "Opened evidence_bundle.schema.json and evidence_ref.schema.json contain meaningful draft 2020-12 shapes but are marked PROPOSED."
  - "Opened evidence-bundle.schema.json is a permissive scaffold with empty properties and additionalProperties true."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-evidence-purple)
![shape](https://img.shields.io/badge/authority-machine--shape-informational)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)
![maturity](https://img.shields.io/badge/maturity-PROPOSED-orange)
![publication](https://img.shields.io/badge/publication-release--gated-critical)

> **Purpose.** `schemas/contracts/v1/evidence/` is the machine-checkable schema family for evidence references, evidence bundles, citation validation, evidence-facing UI payloads, redaction receipts, and evidence-related manifest shapes.
>
> **One-line boundary.** This folder defines evidence object **shape**. It does not store evidence records, source payloads, proof objects, receipts, release decisions, public artifacts, or generated AI answers.

---

## Quick jumps

[Status](#status) · [Authority and placement](#authority-and-placement) · [Repo fit](#repo-fit) · [Current schema inventory](#current-schema-inventory) · [Duplicate and naming risks](#duplicate-and-naming-risks) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Schema-family rules](#schema-family-rules) · [Evidence semantics guardrails](#evidence-semantics-guardrails) · [Promotion checklist](#promotion-checklist) · [Validation](#validation) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README exist? | Yes: `schemas/contracts/v1/evidence/README.md`. It was a two-line placeholder before this expansion. | **CONFIRMED** |
| Is `evidence/` listed as a real-shape family in `schemas/contracts/v1/README.md`? | Yes. | **CONFIRMED** |
| Are evidence schema files present? | Yes. Search surfaced multiple files under this folder. | **CONFIRMED path presence** |
| Are opened core schemas accepted production authority? | Not proven. Opened examples are marked `PROPOSED`. | **NEEDS VERIFICATION** |
| Is there a duplicate naming risk? | Yes. Both `evidence_bundle.schema.json` and `evidence-bundle.schema.json` exist, with different maturity and `$id` shapes. | **NEEDS VERIFICATION / drift-sensitive** |
| Does this README prove evidence closure or release readiness? | No. It is an index and boundary document only. | **CONFIRMED** |

> [!IMPORTANT]
> Evidence schema validity is not evidence truth. Public claims still require EvidenceRef resolution, EvidenceBundle support, source-role posture, rights, sensitivity, review state, release state, correction lineage, and rollback support.

---

## Authority and placement

ADR-0001's proposed schema-home rule places machine-checkable schema families under:

```text
schemas/contracts/v1/<family>/...
```

This folder is therefore the evidence schema family:

```text
schemas/contracts/v1/evidence/
```

Responsibilities are split:

- `schemas/contracts/v1/evidence/` defines machine-checkable evidence shapes.
- `contracts/evidence/` defines human-readable evidence meaning and invariants.
- `fixtures/contracts/v1/evidence/` should hold valid and invalid examples.
- `tools/validators/` should hold validator implementation.
- `policy/evidence/` and wider policy roots should hold rights, sensitivity, and exposure decisions.
- `data/receipts/`, `data/proofs/`, `data/catalog/`, and related lifecycle roots hold emitted records and proof/citation artifacts where applicable.
- `release/` holds release, correction, and rollback decisions.

This README does not amend ADR-0001, Directory Rules, evidence contracts, policy, validators, or release doctrine.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        ├── README.md
        └── evidence/
            ├── README.md                              # this file
            ├── evidence_ref.schema.json               # EvidenceRef shape
            ├── evidence_bundle.schema.json            # EvidenceBundle shape; PROPOSED
            ├── evidence-bundle.schema.json            # duplicate/legacy-style scaffold; NEEDS VERIFICATION
            ├── evidence-bundle.json                   # naming/status NEEDS VERIFICATION
            ├── citation_validation_report.schema.json
            ├── redaction_receipt.schema.json
            ├── evidence_drawer_payload.schema.json
            ├── kfm_geo_manifest.schema.json
            └── spec_normalization.md

contracts/
└── evidence/                                           # semantic meaning; not machine shape

fixtures/
└── contracts/v1/evidence/                              # expected valid/invalid examples; maturity NEEDS VERIFICATION

policy/
└── evidence/                                           # expected policy lane; maturity NEEDS VERIFICATION

tools/
└── validators/                                         # validator implementations; maturity NEEDS VERIFICATION

release/                                                # promotion/release/correction/rollback authority
```

---

## Current schema inventory

Current GitHub search surfaced the following files under `schemas/contracts/v1/evidence/`. This is a search-derived index, not a full mounted-checkout manifest.

| File | Primary role | Maturity note |
|---|---|---|
| `evidence_ref.schema.json` | EvidenceRef shape with `ref`, `kind`, and optional `bundle_ref`. | **PROPOSED / meaningful draft shape** |
| `evidence_bundle.schema.json` | EvidenceBundle shape with bundle ID, claim scope, evidence refs, source records, citations, rights, sensitivity, transforms, checksums, and spec hash. | **PROPOSED / meaningful draft shape** |
| `evidence-bundle.schema.json` | Hyphenated Evidence Bundle scaffold. | **PROPOSED scaffold / duplicate-name risk** |
| `evidence-bundle.json` | Evidence bundle adjacent JSON file. | **NEEDS VERIFICATION** |
| `citation_validation_report.schema.json` | Citation validation report shape. | **NEEDS VERIFICATION** |
| `redaction_receipt.schema.json` | Redaction receipt shape. | **NEEDS VERIFICATION** |
| `evidence_drawer_payload.schema.json` | Evidence Drawer payload shape for UI/API evidence display. | **NEEDS VERIFICATION** |
| `kfm_geo_manifest.schema.json` | Geospatial manifest shape connected to evidence/public artifact integrity. | **NEEDS VERIFICATION** |
| `spec_normalization.md` | Proposed scaffold for spec normalization notes. | **PROPOSED scaffold** |

> [!NOTE]
> Before promotion, regenerate inventory from a mounted checkout or schema registry and verify all `$id`, `$ref`, contract pointers, fixtures, validators, policy references, and CI coverage.

---

## Duplicate and naming risks

The current folder contains both underscore and hyphen variants for EvidenceBundle-related files:

```text
evidence_bundle.schema.json
evidence-bundle.schema.json
evidence-bundle.json
```

Opened evidence shows `evidence_bundle.schema.json` has meaningful required fields and strict `additionalProperties: false`, while `evidence-bundle.schema.json` is a permissive scaffold with empty `properties` and `additionalProperties: true`.

Required posture:

- Do not let both files evolve as parallel authorities.
- Do not delete or rename without migration review.
- Prefer one accepted canonical filename and one accepted `$id` pattern through schema-steward review.
- Use mirror/deprecation notes if compatibility is required.
- Update `$ref`, validators, fixtures, domain schemas, Evidence Drawer payloads, and API payloads before retiring a variant.

---

## What belongs here

- This README.
- Evidence family JSON Schema files.
- JSON-LD context files or equivalent machine-readable evidence shape files when approved.
- Schema-family notes for evidence shape, `$id`, `$ref`, canonicalization, and spec normalization.
- Migration notes, mirror notices, and deprecation notes for evidence schema placement.
- Links to paired contracts, fixtures, validators, schema registry records, source registry records, policy references, release references, correction references, rollback references, and tests.

---

## What does not belong here

- EvidenceBundle instances or EvidenceRef records as data.
- Source payloads, source registry records, or SourceDescriptor instances.
- Proof outputs, receipts, citation exports, or catalog records as emitted data.
- Semantic contract prose.
- Policy rules, sensitivity decisions, or redaction decisions.
- Validator implementation code.
- Runtime/API implementation code.
- Lifecycle data payloads.
- Release records, release manifests, promotion decisions, correction notices, or rollback cards as records.
- Public map tiles, PMTiles, GeoParquet, COGs, screenshots, dashboards, Story Nodes, Focus Mode answers, or generated summaries.
- Claims that a public statement is true merely because its evidence payload validates against a schema.

---

## Schema-family rules

| Rule | Requirement |
|---|---|
| Stable identity | Every evidence schema should have a stable `$id`; duplicate naming variants must be resolved by steward review or ADR/migration note. |
| Dialect | Use JSON Schema draft 2020-12 unless an ADR says otherwise. |
| EvidenceRef discipline | EvidenceRef identifies or points to evidence; it is not itself the whole EvidenceBundle unless explicitly modeled. |
| EvidenceBundle discipline | EvidenceBundle groups the evidence support for a claim scope; it must preserve source records, citations, rights, sensitivity, transforms, checksums, and spec hash where required by the accepted contract. |
| Citation validation | CitationValidationReport schemas should report validation outcomes without laundering weak or absent evidence into truth. |
| Redaction receipts | RedactionReceipt schemas should record transform reason, policy basis, before/after support, and rollback path without exposing protected details. |
| UI payload separation | EvidenceDrawerPayload is a display projection, not canonical evidence truth. |
| Manifest separation | Geo/Layer manifests can cite evidence integrity but do not replace EvidenceBundle or release decisions. |
| Policy separation | Rights, sensitivity, public-safe geometry, and access decisions belong in policy/release lanes. Schemas may shape fields; they do not decide exposure. |
| Release separation | Release records live under `release/` and related lifecycle roots; this folder only defines shapes. |

---

## Evidence semantics guardrails

Evidence shapes must preserve KFM's evidence-first truth posture:

- EvidenceBundle outranks generated language.
- EvidenceRef must resolve to the supporting bundle or a clearly bounded unresolved state.
- Source roles must remain visible: primary, corroborating, context, restricted, derived, model, or other accepted roles should not collapse.
- Rights and sensitivity must be explicit where material.
- Transform history must remain visible where redaction, generalization, clipping, simplification, aggregation, geoprivacy, or normalization occurs.
- Checksums and spec hashes must be stable enough to support reproducibility, review, and rollback.
- Public UI and AI surfaces may summarize evidence only through governed APIs, released artifacts, evidence resolution, and finite outcomes.

---

## Promotion checklist

An evidence schema should not advance beyond `PROPOSED` unless:

- [ ] Canonical filename and `$id` are settled.
- [ ] Duplicate hyphen/underscore variants are resolved, mirrored, or deprecated.
- [ ] Schema uses JSON Schema draft 2020-12 unless an ADR says otherwise.
- [ ] Paired semantic contract is linked.
- [ ] Valid fixtures are linked.
- [ ] Invalid fixtures are linked.
- [ ] Validator path is linked and exists.
- [ ] CI/schema-test support is linked or verified.
- [ ] Policy references are linked where rights, sensitivity, redaction, or public exposure are material.
- [ ] Release/correction/rollback behavior is clear where the schema affects publication.
- [ ] Downstream domain schemas, API payloads, Evidence Drawer payloads, MapLibre layers, and Focus Mode fixtures are updated if references change.

---

## Validation

Recommended local validation sequence:

```bash
# Inspect evidence schema files.
find schemas/contracts/v1/evidence -maxdepth 2 -type f | sort

# Detect duplicate EvidenceBundle naming variants.
find schemas/contracts/v1/evidence -maxdepth 1 -type f \
  | grep -Ei 'evidence[-_]bundle' \
  | sort

# Validate JSON syntax for all evidence schemas.
find schemas/contracts/v1/evidence -name '*.schema.json' -print0 \
  | xargs -0 -I{} python -m json.tool {} >/dev/null

# Run project validators when available.
python tools/validate_all.py || true
pytest tests/schemas tests/contract tests/evidence || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/evidence/README.md`.

Rollback for evidence schemas requires checking every downstream reference:

1. Revert or migrate the schema file.
2. Revert or update paired semantic contracts.
3. Revert or update fixtures and validators.
4. Revert or update schema registry entries.
5. Revert or update domain schemas that `$ref` evidence schemas.
6. Revert or update governed API payloads, Evidence Drawer payloads, MapLibre layer descriptors, and Focus Mode fixtures.
7. Revert or update release candidates, correction notices, and rollback cards if the schema entered release workflow.
8. Preserve migration/deprecation notes for any retired duplicate naming variant.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Which EvidenceBundle filename is canonical: `evidence_bundle.schema.json`, `evidence-bundle.schema.json`, or another ADR-selected form? | **NEEDS VERIFICATION / drift-sensitive** | Evidence steward + schema steward |
| Is `evidence-bundle.json` a fixture, schema-adjacent artifact, legacy file, or drift? | **NEEDS VERIFICATION** | Schema steward |
| Where are the accepted evidence contracts under `contracts/evidence/`? | **NEEDS VERIFICATION** | Contract steward |
| Which fixtures prove valid and invalid EvidenceRef, EvidenceBundle, citation validation, redaction receipt, and Evidence Drawer payload behavior? | **NEEDS VERIFICATION** | Validation steward |
| Which validators currently enforce these schemas? | **NEEDS VERIFICATION** | Validation steward |
| Which domain schemas and API/UI payloads currently `$ref` evidence schemas? | **NEEDS VERIFICATION** | Schema steward + API/UI steward |
| Which evidence schema fields are release-critical and require rollback-card coverage? | **NEEDS VERIFICATION** | Release steward |

---

## Maintainer notes

- Keep this README as the evidence schema-family index, not as evidence truth.
- Resolve duplicate naming before expanding EvidenceBundle consumers.
- Do not treat a valid EvidenceBundle shape as sufficient proof for publication.
- Preserve cite-or-abstain: public truth requires evidence, source role, rights, sensitivity, policy, review, release, correction lineage, and rollback support.

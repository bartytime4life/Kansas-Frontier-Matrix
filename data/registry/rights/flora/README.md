<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/rights/flora/readme
name: Flora Rights Registry README
path: data/registry/rights/flora/README.md
type: data-registry-rights-domain-readme
version: v0.2.0
status: draft
owners:
  - <registry-steward>
  - <rights-steward>
  - <flora-domain-steward>
  - <source-steward>
  - <sensitivity-steward>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: registry
registry_scope: flora-rights-registry-records
domain: flora
path_posture: existing-empty-placeholder-replaced; rights-registry-parent-currently-greenfield-stub; subtype-first-rights-registry-path-confirmed; concrete-records-unknown
sensitivity_posture: registry-internal; no-public-path; rights-unknown-fail-closed; sensitivity-independent-fail-closed; rare-plant-deny-default; culturally-sensitive-plant-knowledge-protected; attribution-and-redistribution-preserved; source-role-preserving; evidence-aware; policy-aware; release-blocked-until-gates-close
related:
  - ../README.md
  - ../../README.md
  - ../../sources/README.md
  - ../../sources/flora/
  - ../../flora/README.md
  - ../../flora/sources/README.md
  - ../../datasets/README.md
  - ../../datasets/flora/README.md
  - ../../domains/README.md
  - ../../crosswalks/README.md
  - ../../../raw/flora/
  - ../../../work/flora/
  - ../../../quarantine/flora/
  - ../../../processed/flora/
  - ../../../catalog/domain/flora/
  - ../../../catalog/stac/flora/README.md
  - ../../../published/layers/flora/
  - ../../../receipts/
  - ../../../proofs/
  - ../../../../docs/domains/flora/RIGHTS_AND_SENSITIVITY.md
  - ../../../../docs/domains/flora/SENSITIVITY.md
  - ../../../../docs/domains/flora/SOURCE_REGISTRY.md
  - ../../../../docs/domains/flora/SOURCE_FAMILIES.md
  - ../../../../docs/domains/flora/SOURCES.md
  - ../../../../docs/domains/flora/DATA_LIFECYCLE.md
  - ../../../../docs/domains/flora/PUBLICATION_AND_ROLLBACK.md
  - ../../../../contracts/domains/flora/
  - ../../../../schemas/contracts/v1/source/
  - ../../../../schemas/contracts/v1/domains/flora/
  - ../../../../schemas/contracts/v1/receipts/
  - ../../../../policy/domains/flora/
  - ../../../../policy/sensitivity/flora/
  - ../../../../policy/rights/
  - ../../../../policy/geoprivacy/
  - ../../../../release/
tags:
  - kfm
  - data
  - registry
  - rights
  - flora
  - source-rights
  - license
  - attribution
  - redistribution
  - rights-holder
  - steward-obligation
  - sensitivity
  - geoprivacy
  - rare-plants
  - culturally-sensitive-plants
  - redaction
  - source-role
  - evidence
  - provenance
  - release-gated
  - no-public-path
notes:
  - "This README replaces the empty placeholder at `data/registry/rights/flora/README.md`."
  - "The parent `data/registry/rights/README.md` is currently a greenfield stub, so rights-registry topology and canonical record shape remain NEEDS VERIFICATION."
  - "Flora rights registry records are registry/control records. They do not store source payloads, prove Flora claims, define contracts, enforce schemas, hold policy, close catalogs, issue licenses, or publish artifacts."
  - "Rights and sensitivity remain distinct independent fail-closed gates. Rights-clean material may still be denied for sensitivity, and sensitivity-safe material may still be denied for rights."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Flora Rights Registry

Subtype-first rights-registry lane for Flora rights, attribution, redistribution, steward-obligation, and release-readiness control records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: registry" src="https://img.shields.io/badge/family-registry-blueviolet">
  <img alt="Domain: flora" src="https://img.shields.io/badge/domain-flora-2ea44f">
  <img alt="Lane: rights" src="https://img.shields.io/badge/lane-rights-blue">
  <img alt="Boundary: not policy" src="https://img.shields.io/badge/boundary-not%20policy-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Flora rights boundary](#flora-rights-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Suggested directory shape](#suggested-directory-shape) · [Suggested registry shape](#suggested-registry-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/rights/flora/` is a registry lane for Flora rights-control records and rights-readiness pointers. It is not RAW source storage, WORK staging, QUARANTINE, PROCESSED data, catalog output, proof, receipt storage, semantic contract authority, schema authority, policy, release authority, source license authority, public API/UI material, or generated-answer authority.

---

## Scope

This directory documents and may hold Flora rights registry records, registry-local indexes, rights-source mappings, attribution obligations, redistribution notes, steward-obligation refs, rights-currentness refs, release-readiness pointers, and routing notes for Flora source families and derivatives.

A Flora rights registry record may describe:

- stable source, dataset, derivative, layer, or catalog-object identity for rights review;
- license, attribution, redistribution, terms-of-use, rights-holder, steward-obligation, and access posture;
- rights-currentness review state and source-terms review references;
- links to SourceDescriptor records and source activation state;
- links to policy decisions, validation receipts, review records, EvidenceBundle/proof refs, catalog refs, release candidates, release manifests, correction notices, and rollback cards;
- rights blockers that prevent activation, processing, catalog closure, release, export, redistribution, or public display.

They do **not** grant rights, interpret law, assert a live upstream license as fact without evidence, override steward restrictions, weaken sensitivity gates, or authorize publication.

---

## Path posture

The requested and existing lane is:

```text
data/registry/rights/flora/
```

This is a subtype-first registry path: registry family first (`rights`), then domain (`flora`). The parent currently exists only as a greenfield stub:

```text
data/registry/rights/README.md
```

Therefore, this README treats the target path as **CONFIRMED path presence / NEEDS VERIFICATION canonical shape**. Do not treat this README as proof that live rights registry records, schema validation, release integration, or governed API rights resolution already exist.

The Flora source registry also records rights posture in source admission records. This lane should not duplicate the canonical source descriptor. It should point to the source registry record, record rights review state when accepted, and preserve a conflict/rollback path when source rights posture changes.

---

## Repo fit

| Responsibility | Home | Boundary |
|---|---|---|
| Flora rights registry records | `data/registry/rights/flora/` | Rights-state pointers, attribution/redistribution obligations, terms-review refs, blockers, and release-readiness state. |
| Rights registry parent | `data/registry/rights/README.md` | Parent is currently a greenfield stub; canonical parent contract remains NEEDS VERIFICATION. |
| Flora source descriptors | `data/registry/flora/sources/` and/or `data/registry/sources/flora/` after topology reconciliation | Source identity/admission records; rights posture is pinned there and referenced here. |
| Flora dataset registry records | `data/registry/datasets/flora/` | Dataset identity and dataset-state records; not rights authority. |
| Flora source payloads | `data/raw/flora/`, `data/work/flora/`, `data/quarantine/flora/`, `data/processed/flora/` | Actual data belongs in lifecycle lanes, not rights registry records. |
| Human-facing Flora rights explanation | `docs/domains/flora/RIGHTS_AND_SENSITIVITY.md` | Explains rights/sensitivity gates; not registry storage. |
| Flora sensitivity explanation | `docs/domains/flora/SENSITIVITY.md` | Explains precision/audience rules; rights are out of scope there. |
| Flora semantic meaning | `contracts/domains/flora/` | Object-family meaning and invariants. |
| Machine schemas | `schemas/contracts/v1/source/`, `schemas/contracts/v1/domains/flora/`, `schemas/contracts/v1/receipts/`, or ADR-selected rights schema lane | Schema enforcement; rights-registry schema remains NEEDS VERIFICATION. |
| Rights, sensitivity, and geoprivacy policy | `policy/domains/flora/`, `policy/sensitivity/flora/`, `policy/rights/`, `policy/geoprivacy/` | Decisions and rules; registry records only point to policy outcomes. |
| Validation/redaction/policy/review receipts | `data/receipts/` | Process memory for checks and public-safe transforms. |
| Proof/evidence | `data/proofs/` or accepted proof lanes | EvidenceBundle closure, proof packs, signatures, and citation validation. |
| Catalog projections | `data/catalog/domain/flora/`, `data/catalog/stac/flora/`, STAC/DCAT/PROV lanes, and triplet lanes | Catalog/discovery carriers after catalog closure. |
| Published layer artifacts | `data/published/layers/flora/` if/when accepted | Released public-safe artifacts and direct sidecars only. |
| Release decisions | `release/` | Promotion, correction, rollback, supersession, withdrawal, and release manifests. |
| Public surfaces | governed APIs and released artifacts only | Public clients do not read this registry lane directly. |

---

## Flora rights boundary

| Rule | Handling |
|---|---|
| Registry record is control state | It records or points to rights review posture; it does not grant a license or decide policy. |
| Rights and sensitivity are separate gates | Passing rights does not relax sensitivity. Passing sensitivity does not clear rights. Both must close before public release. |
| Unknown terms fail closed | Unknown license, attribution, redistribution, endpoint terms, steward obligations, or rights-holder constraints block activation/release until reviewed. |
| SourceDescriptor remains upstream anchor | Source identity, source role, rights posture, source terms, cadence, and source head should remain anchored in the source registry record. |
| Rights travel downstream | License, attribution, rights-holder, dataset identity, terms-review refs, and obligation refs must remain attached through derivatives and published artifacts. |
| No license string without evidence | A registry record should not assert a specific license or rights holder unless supported by source evidence and review state. |
| Restricted means denied by default | Restricted or steward-controlled source material should route to authorized/reviewed surfaces only; public exposure requires explicit release support. |
| Rare-plant sensitivity still governs | Exact rare, protected, or culturally sensitive plant material can remain unpublishable even when rights are clear. |
| Redaction does not erase rights | Generalization, aggregation, withholding, or redaction may reduce sensitivity exposure, but rights obligations and attribution still travel. |
| Registry is not evidence closure | EvidenceBundle/proof support remains separate. |
| Registry is not catalog closure | STAC/DCAT/PROV/domain catalog and graph projections remain separate. |
| Registry is not release | Public exposure requires validation, policy, review, proof/catalog support, release manifest, correction path, and rollback path. |
| Public clients do not read this lane | Public UI/API surfaces consume governed APIs, released artifacts, and evidence/policy-safe envelopes. |

---

## Accepted material

Accepted content is limited to Flora rights registry records and registry-local support files:

- rights-family README files and registry-local indexes;
- source, dataset, derivative, layer, catalog-object, or release-candidate rights review records;
- source registry refs and SourceDescriptor refs;
- license, rights-holder, attribution, redistribution, terms-of-use, access, steward-obligation, and rights-currentness refs;
- rights review state, reviewer refs, review dates, expiration/recheck dates, and source-terms review refs;
- rights blockers, restriction notes, embargo notes, withdrawal notes, supersession refs, correction refs, and rollback refs;
- policy refs, sensitivity refs, geoprivacy refs, redaction refs, validation receipt refs, proof refs, EvidenceBundle refs, catalog refs, release refs, and review refs;
- registry-local manifests, checksums, signatures, and index sidecars.

Keep records compact and pointer-based. Do not embed full source payloads, license documents beyond short reviewed pointers, sensitive locations, proof packs, policy decisions, catalog records, release manifests, or Flora claim content in this lane.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw Flora source payloads, herbarium archives, occurrence exports, taxon tables, vegetation datasets, invasive records, phenology feeds, restoration records, rasters, shapefiles, GeoParquet, COG, PMTiles, or source-native tables | `data/raw/flora/`, `data/work/flora/`, `data/quarantine/flora/`, or `data/processed/flora/` depending on lifecycle state |
| Source descriptor/admission records | `data/registry/flora/sources/` or `data/registry/sources/flora/` after topology reconciliation |
| Dataset identity records | `data/registry/datasets/flora/` |
| Crosswalk mapping records | `data/registry/crosswalks/` |
| Domain-state records | `data/registry/domains/` |
| Semantic object contracts | `contracts/domains/flora/` |
| JSON Schema | `schemas/contracts/v1/...` |
| Rights policy, sensitivity policy, geoprivacy policy, access-control logic, redaction policy, or release rules | `policy/` |
| Validation receipts, redaction receipts, terms-review receipts, policy receipts, review receipts, or process-memory logs | `data/receipts/` |
| EvidenceBundle records, proof packs, signatures, or citation-validation closure | `data/proofs/` |
| STAC/DCAT/PROV/domain catalog records or graph/triplet projections | `data/catalog/` and `data/triplets/` |
| Published Flora layers, reports, dashboards, tiles, API payloads, or generated-answer carriers | `data/published/`, governed app/API roots, and release-approved public artifact lanes |
| ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal notice, or supersession notice | `release/` |
| Validator code, connector code, pipelines, fixtures, tests, or CI workflows | `tools/`, `connectors/`, `pipelines/`, `fixtures/`, `tests/`, `.github/workflows/` |

---

## Suggested directory shape

The map below is **PROPOSED** documentation guidance, not proof that child folders or records exist.

```text
data/registry/rights/flora/
├── README.md
├── source_terms/
│   ├── README.md
│   └── index.local.json
├── attribution/
│   ├── README.md
│   └── index.local.json
├── redistribution/
│   ├── README.md
│   └── index.local.json
├── steward_obligations/
│   ├── README.md
│   └── index.local.json
├── derivative_rights/
│   ├── README.md
│   └── index.local.json
├── release_readiness/
│   ├── README.md
│   └── index.local.json
└── index.local.json
```

Do not create a new child lane until the rights object family, source descriptor refs, evidence refs, policy refs, review state, release refs, and rollback path are known.

---

## Suggested registry shape

The exact rights-registry schema remains **NEEDS VERIFICATION**. A Flora rights registry record should be structured enough for audit, release readiness, correction, and rollback.

```json
{
  "id": "kfm-rights:flora:<stable-rights-id>",
  "record_type": "rights_registry_record",
  "domain": "flora",
  "rights_family": "source_terms | attribution | redistribution | steward_obligations | derivative_rights | release_readiness | other",
  "subject_ref": "source | dataset | derivative | layer | catalog_item | release_candidate",
  "source_registry_refs": [],
  "dataset_registry_refs": [],
  "layer_registry_refs": [],
  "rights_status": "allowed | attribution-required | restricted | unknown | denied | needs-review",
  "license_refs": [],
  "rights_holder_refs": [],
  "attribution_refs": [],
  "redistribution_refs": [],
  "terms_review_refs": [],
  "steward_obligation_refs": [],
  "policy_refs": [],
  "sensitivity_refs": [],
  "redaction_receipt_refs": [],
  "validation_receipt_refs": [],
  "evidence_refs": [],
  "proof_refs": [],
  "catalog_refs": [],
  "review_refs": [],
  "release_refs": [],
  "correction_refs": [],
  "rollback_refs": [],
  "public_exposure": "none | eligible-after-review | released-public-safe | permissioned | restricted | denied",
  "blockers": [],
  "created_at": "timestamp",
  "updated_at": "timestamp"
}
```

Do not treat this JSON block as a live schema. It is a maintainer-facing sketch until paired contracts, schemas, validators, fixtures, examples, CI, and review workflows are verified.

---

## Required checks before use

- [ ] Confirm the rights record belongs in `data/registry/rights/flora/`, not `data/registry/flora/sources/`, `data/registry/sources/flora/`, `contracts/`, `schemas/`, `policy/`, `data/receipts/`, `data/proofs/`, `data/catalog/`, `data/published/`, or `release/`.
- [ ] Confirm the subject of the rights review is identified: source, dataset, derivative, layer, catalog item, release candidate, or other reviewed object.
- [ ] Confirm license, attribution, redistribution, rights-holder, source terms, endpoint terms, steward obligations, access posture, review date, and recheck date are recorded or explicitly blocked.
- [ ] Confirm rights evidence exists before asserting any specific license, rights holder, redistribution permission, or public-release eligibility.
- [ ] Confirm unknown, restricted, expired, conflicting, or missing rights state fails closed.
- [ ] Confirm rights state does not override sensitivity, geoprivacy, rare-plant handling, cultural sensitivity, evidence closure, catalog closure, or release state.
- [ ] Confirm rights obligations travel to derivatives, catalog records, published artifacts, exports, API payloads, reports, and attribution surfaces.
- [ ] Confirm source roles, source identities, source vintages, and SourceDescriptor refs are preserved.
- [ ] Confirm validation receipts, redaction receipts, terms-review receipts, policy outcomes, and review records exist before catalog or release eligibility is asserted.
- [ ] Confirm EvidenceRef/EvidenceBundle and proof refs exist for consequential use.
- [ ] Confirm release refs point to ReleaseManifest/PromotionDecision objects rather than implying publication from rights state.
- [ ] Confirm correction, supersession, withdrawal, and rollback paths exist for changed source terms, rights errors, attribution defects, or release withdrawal.
- [ ] Confirm no public client, map layer, graph edge, vector index, generated answer, report, or dashboard reads this registry lane as direct public truth.

---

## Status notes

| Claim | Status |
|---|---:|
| This README replaces the empty placeholder at `data/registry/rights/flora/README.md`. | CONFIRMED authored |
| The target path existed in the live repository as an empty placeholder before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/rights/README.md` exists and is currently a greenfield stub. | CONFIRMED by GitHub contents API during this edit |
| Flora rights/sensitivity docs state rights and sensitivity are distinct questions and independent fail-closed gates before public release. | CONFIRMED by GitHub contents API during this edit |
| Flora rights/sensitivity docs state unknown rights fail closed and no specific license string is asserted without upstream confirmation. | CONFIRMED by GitHub contents API during this edit |
| Flora sensitivity docs state exact rare/protected/culturally sensitive plant locations are denied on public surfaces by default and require review, transformed/withheld geometry, and RedactionReceipt for public release. | CONFIRMED by GitHub contents API during this edit |
| Flora source registry README records that source descriptors include rights, license, attribution, redistribution, and terms posture and that rights-unclear feeds fail closed. | CONFIRMED by GitHub contents API during this edit |
| Concrete Flora rights registry payloads exist under this requested lane. | UNKNOWN |
| The final accepted parent contract for `data/registry/rights/` is resolved. | NEEDS VERIFICATION |
| A canonical Flora rights registry schema is enforced. | NEEDS VERIFICATION |
| CI validates Flora rights registry records. | UNKNOWN |
| This README grants public access to Flora rights registry internals. | DENY |

---

## Maintainer note

Flora rights registry records are useful because they make source terms, rights-holder obligations, attribution, redistribution, steward obligations, release readiness, correction, and rollback inspectable before a source or derivative reaches public surfaces. They become dangerous when treated as policy, legal advice, source payloads, proof closure, catalog closure, release decisions, or Flora truth. Keep the chain explicit:

```text
rights registry record -> source descriptor refs -> terms/evidence review -> policy/review outcome -> lifecycle payload -> validation/redaction receipt -> proof/catalog -> release -> governed public surface
```

Never collapse it into:

```text
rights registry record -> public Flora permission
```

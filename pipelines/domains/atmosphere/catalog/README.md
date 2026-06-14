<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-atmosphere-catalog-readme
title: Atmosphere Catalog Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <atmosphere-pipeline-owner>
  - <atmosphere-domain-steward>
  - <catalog-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public-with-atmosphere-catalog-proof-and-release-gates
path: pipelines/domains/atmosphere/catalog/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/atmosphere/README.md
  - pipelines/domains/atmosphere/normalize/README.md
  - pipelines/domains/atmosphere/validate/README.md
  - pipelines/domains/atmosphere/publish/README.md
  - docs/domains/atmosphere/README.md
  - docs/domains/atmosphere/DATA_LIFECYCLE.md
  - docs/runbooks/atmosphere/PROMOTION_RUNBOOK.md
  - pipeline_specs/atmosphere/catalog.yaml
  - contracts/domains/atmosphere/
  - schemas/contracts/v1/domains/atmosphere/
  - policy/domains/atmosphere/
  - data/processed/atmosphere/
  - data/catalog/domain/atmosphere/
  - data/triplets/atmosphere/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/atmosphere/
  - release/manifests/atmosphere/
tags: [kfm, pipelines, domains, atmosphere, catalog, catalog-matrix, evidence-bundle, triplet, air-quality, weather, climate, model-context, freshness, caveats, policy, governance]
notes:
  - "This README fills the blank pipelines/domains/atmosphere/catalog path as a nested executable Atmosphere catalog-closure sublane."
  - "Catalog logic is executable proof/catalog handoff support only; it does not own connectors, source descriptors, schemas, contracts, policy, validation, lifecycle data, release decisions, or governed API authority."
  - "Catalog closure binds processed Atmosphere records to catalog records, EvidenceBundles, graph/triplet projections, provenance, receipts, and release-candidate blockers; it does not publish."
  - "Realtime and historical atmospheric collections must remain split where cadence, freshness, rights, and evidence posture differ."
  - "AQI, concentration, AOD, PM2.5, model field, observation, public report, climate normal/anomaly, derived fusion, and advisory context remain separate knowledge characters."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere Catalog Pipeline

> Executable Atmosphere / Air / Climate sublane for closing processed atmospheric candidates into catalog records, EvidenceBundle-bound claim surfaces, graph/triplet projections, release-candidate blockers, catalog receipts, and release handoffs while preserving source roles, knowledge-character labels, caveats, freshness, policy outcomes, correction paths, and rollback boundaries.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-atmosphere%20catalog-2e7d32)
![authority](https://img.shields.io/badge/authority-catalog%20handoff%20logic-0a7ea4)
![proof](https://img.shields.io/badge/evidence-bundle%20required-d62728)
![publication](https://img.shields.io/badge/publication-no%20direct%20publish-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/atmosphere/catalog/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Atmosphere / Air / Climate  
**Sublane:** Catalog / proof closure / graph handoff  
**Placement posture:** nested executable sublane under `pipelines/domains/atmosphere/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no direct publication; catalog outputs are discovery, evidence, graph, and release-candidate inputs only until ReleaseManifest, correction, and rollback closure.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Catalog anti-collapse rules](#3-catalog-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Catalog scope](#6-catalog-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal catalog closure record](#11-minimal-catalog-closure-record)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Promotion, publication, correction, and rollback](#13-promotion-publication-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/domains/atmosphere/catalog/` is the executable sublane for Atmosphere catalog closure and graph/triplet handoff.

It supports catalog closure for:

- processed air-quality, weather, smoke/aerosol, climate, model, forecast, station, and advisory-context records;
- catalog collection splitting for realtime, historical, station, gridded, modeled, remote-sensing, climate-normal, anomaly, and derived-fusion products;
- EvidenceBundle closure, digest closure, catalog matrix entries, PROV activity refs, STAC/DCAT-like metadata, graph/triplet projections, and release-candidate blockers;
- source cadence, freshness, caveat, confidence, limitation, correction, and source-redirection fields needed by released surfaces;
- hold outcomes for unresolved EvidenceRef, stale source state, rights uncertainty, source-role collapse, knowledge-character collapse, missing caveats, missing ReviewRecord, schema drift, or graph projection failure.

This directory implements or will implement the **how** of Atmosphere catalog closure. It does not fetch source data, admit sources, normalize records, validate records, define schemas, decide policy, own release approval, serve governed API responses, or publish map artifacts.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/atmosphere/`? | Visible domain docs use `atmosphere` as the lane and treat `air` as slug drift / alias pending ADR. | CONFIRMED documentation pattern; implementation NEEDS VERIFICATION |
| Why `catalog/`? | This is a narrow executable sublane for catalog/proof closure and graph/triplet handoff from processed Atmosphere records. | PROPOSED / NEEDS VERIFICATION |
| Does this own EvidenceBundle truth? | No. It verifies/resolves EvidenceBundle refs and emits closure records; evidence remains its own proof artifact. | CONFIRMED proof separation |
| Does this publish? | No. Catalog closure prepares release candidates; release requires ReleaseManifest, correction path, and rollback target. | CONFIRMED release separation |
| Can clients read this lane directly? | No. Clients use governed APIs and released artifacts only. | CONFIRMED trust membrane posture |

> [!IMPORTANT]
> A catalog record is not publication. Atmosphere catalog closure proves discovery/proof/graph readiness for the checked scope; it still requires release review, policy state, ReleaseManifest, correction path, rollback target, and artifact assembly before any surface changes.

[⬆ Back to top](#top)

---

## 3. Catalog anti-collapse rules

Catalog closure must preserve processed records, catalog records, EvidenceBundles, graph/triplet projections, release candidates, and artifacts as separate objects.

Disallowed collapses:

```text
catalog closure -> public release
catalog record -> EvidenceBundle
EvidenceRef -> EvidenceBundle
catalog record -> public artifact
triplet projection -> canonical truth
catalog collection -> source descriptor
realtime product -> historical archive
AQI -> concentration
AOD -> PM2.5
model field -> observation
generated catalog summary -> evidence
catalog run -> ReleaseManifest
```

Required distinctions:

- processed object, CatalogMatrix entry, EvidenceBundle, graph/triplet projection, catalog receipt, release candidate, ReleaseManifest, CorrectionNotice, RollbackCard, and published artifact remain separate;
- realtime and historical atmospheric products remain distinct where cadence, freshness, rights, and evidence posture differ;
- STAC/DCAT/PROV metadata is discovery/provenance support, not source truth;
- knowledge-character labels remain validator-enforced and catalog-visible;
- every claim resolves evidence or abstains;
- clients never read processed, catalog, triplet, graph, or internal stores directly.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable Atmosphere catalog-closure logic.

Appropriate contents include:

- fixture-only catalog dry-run entrypoints;
- processed-record-to-catalog-entry builders;
- CatalogMatrix entry builders;
- EvidenceRef/EvidenceBundle resolution checks;
- STAC/DCAT/PROV metadata builders;
- graph/triplet projection builders;
- realtime-vs-historical collection splitters;
- freshness, caveat, confidence, limitation, source-vintage, and correction-surface field validators;
- release-candidate blocker builders;
- catalog receipt emitters, if not shared;
- hold routing helpers for missing evidence, stale state, schema drift, source-role collapse, graph projection failure, or release-readiness blockers.

A good placement test:

> If the code converts processed Atmosphere records into evidence-bound catalog records, graph/triplet projections, catalog receipts, or release-candidate blockers, it may belong here. If it fetches sources, admits sources, normalizes records, validates records, defines schemas, decides policy, approves release, or serves governed API/map output, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Source fetchers and API clients | `connectors/<source>` or accepted connector home |
| Ingest/source admission | `pipelines/domains/atmosphere/ingest/` or accepted ingest lane |
| Normalization mappers | `pipelines/domains/atmosphere/normalize/` |
| Validation logic | `pipelines/domains/atmosphere/validate/` |
| Publish artifact builders | `pipelines/domains/atmosphere/publish/` |
| Atmosphere doctrine and object meaning | `docs/domains/atmosphere/`, `contracts/domains/atmosphere/` |
| Source descriptors / source registry entries | `data/registry/sources/atmosphere/` or approved registry home |
| JSON Schemas | `schemas/contracts/v1/domains/atmosphere/` or accepted schema home |
| Policy, rights, sensitivity, release rules | `policy/...` responsibility roots |
| Declarative run specs | `pipeline_specs/atmosphere/...` |
| Fixtures | `fixtures/domains/atmosphere/catalog/` or accepted fixture home |
| Tests | `tests/pipelines/domains/atmosphere/catalog/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published lifecycle records | `data/...` lifecycle homes |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Release decisions and manifests | `release/...` responsibility roots |

[⬆ Back to top](#top)

---

## 6. Catalog scope

| Scope area | Catalog responsibility | Failure behavior |
|---|---|---|
| Processed input | Confirm processed records, validation reports, receipts, policy state, and digests exist. | Hold at PROCESSED. |
| Evidence closure | Resolve EvidenceRefs to EvidenceBundles and verify digest closure. | Hold; no public edge. |
| Catalog metadata | Build catalog entries with source role, cadence, time, geometry/grid, units, caveats, and freshness fields. | Hold on incomplete metadata. |
| Knowledge character | Preserve observation, public report, regulatory archive, model field, remote-sensing mask, climate normal/anomaly, derived fusion, and advisory context labels. | Fail on collapse. |
| Graph/triplet | Emit graph/triplet projections with provenance and invalidation refs. | Hold on graph projection failure. |
| Release blockers | Emit release-candidate readiness and blockers. | No direct publish. |
| Correction/rollback | Carry correction path and rollback target expectations forward. | Hold if missing for release-capable material. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Atmosphere catalog run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** approved fixtures, processed Atmosphere records, validation reports, transform receipts, aggregation receipts, model-run receipts, policy decisions, review records, and EvidenceRef candidates.
2. **Resolve** EvidenceRefs to EvidenceBundles and verify digest closure, source-role continuity, caveats, freshness, rights, and knowledge-character labels.
3. **Emit** catalog matrix entries, metadata records, graph/triplet projections, catalog receipts, and release-readiness blockers into accepted lifecycle homes.
4. **Hold** missing evidence, stale state, rights uncertainty, source-role collapse, missing caveats, graph projection errors, schema drift, or release-blocking defects.
5. **Prepare** release-candidate handoffs only when catalog/proof closure succeeds.
6. **Never publish directly.**

Catalog closure is the PROCESSED-to-CATALOG/TRIPLET proof gate. It is not public release and not public serving.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Atmosphere catalog run must check or explicitly fail closed on:

1. **Processed input gate** — processed record, validation report, receipts, policy state, and digest refs exist.
2. **EvidenceBundle gate** — EvidenceRefs resolve and claim-bearing records have proof closure.
3. **CatalogMatrix gate** — catalog entry exists with object family, source role, rights, cadence, time, spatial scope, and lifecycle refs.
4. **Knowledge-character gate** — AQI, concentration, AOD, model fields, observations, public reports, climate products, and advisory context remain distinct.
5. **Freshness/caveat gate** — source cadence, stale-state, caveat, confidence, correction, and limitation fields are present where required.
6. **PROV gate** — fetch, normalization, validation, aggregation/model, catalog, and review activities are recorded or referenced.
7. **Graph/triplet gate** — graph deltas/triplets carry provenance, source refs, evidence refs, and invalidation refs.
8. **Collection-split gate** — realtime and historical products are not mixed when cadence, rights, or freshness differ.
9. **Policy/review gate** — finite policy outcome and review state exist where materiality requires it.
10. **Release-blocker gate** — missing rollback target, correction path, caveats, or release review becomes an explicit blocker.
11. **No-direct-publish gate** — catalog does not write public UI, public API, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/atmosphere/catalog/
├── README.md                         # this file
├── CATALOG_CONTRACT.md               # PROPOSED: Atmosphere catalog execution contract
├── run_dry_fixture.py                # PROPOSED synthetic fixture only
├── build_catalog_matrix_entry.py     # PROPOSED
├── resolve_evidence_bundle_refs.py   # PROPOSED
├── build_stac_dcat_prov.py           # PROPOSED
├── build_graph_triplets.py           # PROPOSED
├── split_realtime_historical.py      # PROPOSED
├── validate_freshness_caveats.py     # PROPOSED
├── build_release_blockers.py         # PROPOSED
├── route_hold.py                     # PROPOSED
├── emit_catalog_receipt.py           # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/atmosphere/catalog.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use accepted lifecycle homes under `data/catalog/domain/atmosphere/`, `data/triplets/atmosphere/`, `data/receipts/`, `data/proofs/evidence_bundle/`, and `release/candidates/atmosphere/` before downstream release and published-layer roots.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/atmosphere/catalog/` or accepted fixture home | Synthetic processed/catalog fixture. |
| Processed input | `data/processed/atmosphere/<dataset_id>/<version>/` | Validated candidate input. |
| ValidationReport | `data/processed/atmosphere/` or accepted validation-report home | Required validation proof. |
| EvidenceBundle | `data/proofs/evidence_bundle/` | Required claim proof. |
| Catalog record | `data/catalog/domain/atmosphere/` | Discovery/proof projection; not public. |
| Triplet / graph delta | `data/triplets/atmosphere/` or accepted graph-delta home | Provenance-bound projection only. |
| Catalog receipt | `data/receipts/pipeline/atmosphere/catalog/<run_id>.yml` or accepted receipt home | Records inputs, checks, digests, and output refs. |
| Release candidate blocker | `release/candidates/atmosphere/` or accepted release-candidate home | Handoff only; no release decision. |

[⬆ Back to top](#top)

---

## 11. Minimal catalog closure record

The final schema is not defined here. This example shows the minimum information an Atmosphere catalog closure record should preserve.

```yaml
schema_version: kfm.atmosphere_catalog_closure.v1
catalog_run_id: atmosphere_catalog_run_YYYYMMDDThhmmssZ
pipeline_id: domains.atmosphere.catalog
status: HOLD
input:
  processed_ref: data/processed/atmosphere/<dataset_id>/<version>/<object_id>.json
  validation_report_ref: data/processed/atmosphere/<dataset_id>/<version>/validation_report.yml
  source_descriptor_ref: data/registry/sources/atmosphere/<source_id>.yml
catalog:
  catalog_record_ref: data/catalog/domain/atmosphere/<dataset_id>/<version>/<object_id>.json
  collection_type: <realtime|historical|station|grid|model|remote_sensing|climate|derived_fusion|advisory_context>
  knowledge_character: needs_review
evidence:
  evidence_ref_candidates: []
  evidence_bundle_ref: null
  evidence_resolved: false
freshness_caveats:
  cadence_ref: null
  freshness_state: needs_review
  caveats_ready: false
  source_redirection_ready: false
graph:
  triplet_refs: []
  graph_delta_ref: null
policy:
  policy_decision_ref: null
  review_record_ref: null
release_readiness:
  release_candidate_ref: null
  blockers:
    - EVIDENCE_OR_CAVEAT_OR_ROLLBACK_NOT_RESOLVED
anti_collapse:
  catalog_record_is_publication: false
  catalog_record_is_evidence_bundle: false
  triplet_projection_is_canonical_truth: false
  realtime_product_is_historical_archive: false
  aqi_is_concentration: false
  aod_is_pm25: false
outputs:
  receipt_ref: data/receipts/pipeline/atmosphere/catalog/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic, and no-network** until catalog specs, processed fixtures, evidence fixtures, policy fixtures, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/atmosphere/catalog/
├── test_no_network_dry_run.py              # PROPOSED
├── test_processed_input_required.py        # PROPOSED
├── test_validation_report_required.py      # PROPOSED
├── test_evidence_bundle_required.py        # PROPOSED
├── test_catalog_matrix_entry_required.py   # PROPOSED
├── test_realtime_historical_split.py       # PROPOSED
├── test_knowledge_character_preserved.py   # PROPOSED
├── test_freshness_caveats_required.py      # PROPOSED
├── test_graph_triplet_provenance.py        # PROPOSED
├── test_release_blockers_emitted.py        # PROPOSED
├── test_no_public_artifact_write.py        # PROPOSED
├── test_receipt_hashes.py                  # PROPOSED
└── test_no_direct_publish.py               # PROPOSED
```

A dry run should prove fixtures load without network access, processed inputs and validation reports are required, EvidenceBundles resolve, catalog matrix entries close, realtime/historical collections split correctly, knowledge-character labels are preserved, graph/triplet projections carry provenance, release blockers are explicit, receipts are deterministic, and no run writes directly to public UI, public API, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

Atmosphere catalog pipelines may prepare catalog records, graph/triplet projections, release-candidate blockers, and receipts. They do not publish.

Required chain:

```text
processed Atmosphere object + ValidationReport
  -> EvidenceBundle closure
  -> catalog matrix entry
  -> graph / triplet projection
  -> release candidate blockers
  -> ReleaseManifest
  -> RollbackCard
  -> public artifact
```

Correction and rollback posture:

- denied, held, failed, restricted, stale, conflicted, and incomplete catalog runs remain auditable;
- receipts preserve source refs, processed refs, validation refs, EvidenceBundle refs, catalog refs, graph refs, freshness refs, caveat refs, policy refs, review refs, and failure reasons;
- catalog records are superseded through governed state transitions, not hidden overwrite;
- downstream artifacts are invalidated if source refs, validation refs, EvidenceBundle refs, catalog refs, graph refs, freshness refs, caveat refs, policy refs, correction refs, or rollback refs drift;
- release rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/atmosphere/catalog/README.md` file;
- identifies this directory as a nested executable Atmosphere catalog-closure sublane;
- prevents connector, source-admission, normalization, validation, schema, contract, policy, fixture, test, data, public API, UI, release-decision, and publish authority from being placed here;
- preserves processed input, ValidationReport, EvidenceRef, EvidenceBundle, CatalogMatrix, PROV, graph/triplet, freshness, caveat, policy, release-blocker, correction, and rollback boundaries;
- blocks catalog-record-as-publication, catalog-record-as-EvidenceBundle, EvidenceRef-as-EvidenceBundle, triplet-as-canonical-truth, realtime-as-historical, AQI-as-concentration, AOD-as-PM2.5, generated-summary-as-evidence, and direct publication writes;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has processed fixtures, no-network tests, schema-backed catalog records, EvidenceBundle closure, catalog/triplet provenance tests, realtime/historical split tests, freshness/caveat tests, release-blocker tests, deterministic receipts, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `ATM-CAT-001` | Should Atmosphere catalog remain one sublane, or split into air-quality, weather, smoke/AOD, climate, model, advisory-context, and graph-projection catalog processors? | NEEDS VERIFICATION / ADR |
| `ATM-CAT-002` | Which schema owns catalog closure records, catalog receipts, graph deltas, and release blockers? | NEEDS VERIFICATION |
| `ATM-CAT-003` | Which catalog collection split is first-wave: realtime AQ, historical AQ, weather observations, smoke/AOD, climate normals, or model fields? | NEEDS VERIFICATION |
| `ATM-CAT-004` | Which CI job owns Atmosphere catalog invariant tests? | UNKNOWN |
| `ATM-CAT-005` | Which slug is authoritative for schema and contract homes: `atmosphere`, `air`, or both through an ADR-managed compatibility bridge? | NEEDS VERIFICATION / ADR |
| `ATM-CAT-006` | What graph/triplet projection vocabulary should be used for atmospheric parameter, station, network, time, and model-run relationships? | NEEDS VERIFICATION / ADR |
| `ATM-CAT-007` | Should release candidates be emitted by catalog closure or by a separate release-prep sublane? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic processed fixtures and negative tests. Do not add live source fetching, ingest authority, normalization authority, validation authority, schema authority, policy authority, direct public API code, direct UI code, release-manifest writes, public layer writes, or generated atmosphere summaries until EvidenceBundle refs, catalog matrix entries, graph/triplet projections, freshness/caveat fields, release blockers, deterministic receipts, review state, and rollback expectations are proven.

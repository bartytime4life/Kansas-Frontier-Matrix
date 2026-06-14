<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-archaeology-catalog-readme
title: Archaeology Catalog Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <archaeology-pipeline-owner>
  - <archaeology-domain-steward>
  - <catalog-steward>
  - <review-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public-with-archaeology-catalog-review-evidence-and-release-gates
path: pipelines/domains/archaeology/catalog/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/archaeology/README.md
  - pipelines/domains/archaeology/ingest/README.md
  - pipelines/domains/archaeology/normalize/README.md
  - pipelines/domains/archaeology/validate/README.md
  - pipelines/domains/archaeology/publish/README.md
  - docs/domains/archaeology/DATA_LIFECYCLE.md
  - docs/domains/archaeology/VALIDATORS.md
  - docs/domains/archaeology/PUBLICATION_AND_POLICY.md
  - docs/domains/archaeology/RELEASE_INDEX.md
  - pipeline_specs/archaeology/catalog.yaml
  - contracts/domains/archaeology/
  - schemas/contracts/v1/domains/archaeology/
  - policy/domains/archaeology/
  - policy/sensitivity/archaeology/
  - data/processed/archaeology/
  - data/catalog/domain/archaeology/
  - data/triplets/archaeology/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/archaeology/
  - release/manifests/archaeology/
tags: [kfm, pipelines, domains, archaeology, catalog, catalog-matrix, evidence-bundle, triplet, review, policy, provenance, release-blocker, governance]
notes:
  - "This README fills the blank pipelines/domains/archaeology/catalog path as a nested executable Archaeology catalog-closure sublane."
  - "Catalog logic is executable proof/catalog handoff support only; it does not own connectors, source descriptors, schemas, contracts, policy, validation, review decisions, lifecycle data, release decisions, or governed API authority."
  - "Catalog closure binds processed Archaeology records to CatalogMatrix entries, EvidenceBundles, graph/triplet projections, provenance, receipts, and release-candidate blockers; it does not publish."
  - "Candidate features, interpreted records, generated summaries, 3D representations, and public-safe representations must remain distinct from evidence and confirmed records."
  - "Concrete executable behavior, CI coverage, catalog schemas, graph projection wiring, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology Catalog Pipeline

> Executable Archaeology sublane for closing processed archaeology candidates into CatalogMatrix records, EvidenceBundle-bound claim surfaces, graph/triplet projections, release-candidate blockers, catalog receipts, and release handoffs while preserving source roles, candidate boundaries, review state, policy outcomes, representation receipts, correction paths, and rollback boundaries.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-archaeology%20catalog-8a6d3b)
![authority](https://img.shields.io/badge/authority-catalog%20handoff%20logic-0a7ea4)
![proof](https://img.shields.io/badge/evidence-bundle%20required-d62728)
![publication](https://img.shields.io/badge/publication-no%20direct%20publish-d62728)

**Status:** Draft  
**Path:** `pipelines/domains/archaeology/catalog/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Archaeology  
**Sublane:** Catalog / proof closure / graph handoff  
**Placement posture:** nested executable sublane under `pipelines/domains/archaeology/`; concrete behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no direct publication; catalog outputs are discovery, evidence, graph, review, and release-candidate inputs only until ReleaseManifest, correction, and rollback closure.

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

`pipelines/domains/archaeology/catalog/` is the executable sublane for Archaeology catalog closure and graph/triplet handoff.

It supports catalog closure for:

- processed archaeology records, survey/project records, candidate features, remote-sensing or geophysics candidates, chronology context, collection/repository references, documentation records, and released public-safe representation candidates;
- CatalogMatrix entries, STAC/DCAT-like discovery metadata, PROV activity refs, graph/triplet projections, and release-candidate blockers;
- EvidenceRef resolution to EvidenceBundles for every claim entering catalog;
- review-state, policy-state, source-role, source-vintage, rights, transformation receipt, public-representation, correction, and rollback references;
- candidate-vs-confirmed-record preservation, reality-boundary notes for synthetic or reconstructed carriers, and public-safe representation labels;
- hold outcomes for unresolved evidence, unresolved review, unresolved policy, source-role collapse, candidate-boundary collapse, missing transform receipts, graph projection failure, schema drift, or release-readiness blockers.

This directory implements or will implement the **how** of Archaeology catalog closure. It does not fetch source data, admit sources, normalize records, validate records, define schemas, decide policy, decide review outcomes, own release approval, serve governed API responses, or publish map artifacts.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/archaeology/`? | Archaeology is a domain lane under the domain-pipeline umbrella. | CONFIRMED path pattern; behavior NEEDS VERIFICATION |
| Why `catalog/`? | This sublane closes processed Archaeology records into catalog/proof/graph handoff records. | PROPOSED / NEEDS VERIFICATION |
| Does this own EvidenceBundle truth? | No. It verifies/resolves EvidenceBundle refs and emits closure records; evidence remains its own proof artifact. | CONFIRMED proof separation |
| Does this publish? | No. Catalog closure prepares release candidates; release requires ReleaseManifest, review state, correction path, and rollback target. | CONFIRMED release separation |
| Can clients read this lane directly? | No. Clients use governed APIs and released artifacts only. | CONFIRMED trust membrane posture |

> [!IMPORTANT]
> A catalog record is not publication. Archaeology catalog closure proves discovery/proof/graph readiness for the checked scope; it still requires release review, policy state, ReleaseManifest, correction path, rollback target, and artifact assembly before any public surface changes.

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
candidate feature -> confirmed record
remote-sensing anomaly -> confirmed record
3D representation -> direct evidence
reconstruction -> observation
publication transform receipt -> release approval
generated catalog summary -> evidence
catalog run -> ReleaseManifest
```

Required distinctions:

- processed object, CatalogMatrix entry, EvidenceBundle, graph/triplet projection, catalog receipt, release candidate, ReleaseManifest, CorrectionNotice, RollbackCard, and published artifact remain separate;
- candidate records remain labeled until steward/review process changes their status;
- STAC/DCAT/PROV metadata is discovery/provenance support, not source truth;
- public-safe representation, transform receipts, review records, and policy decisions stay attached to catalog entries;
- every claim resolves evidence or abstains;
- clients never read processed, catalog, triplet, graph, or internal stores directly.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable Archaeology catalog-closure logic.

Appropriate contents include:

- fixture-only catalog dry-run entrypoints;
- processed-record-to-catalog-entry builders;
- CatalogMatrix entry builders;
- EvidenceRef/EvidenceBundle resolution checks;
- STAC/DCAT/PROV metadata builders;
- graph/triplet projection builders;
- review-state and policy-state presence validators;
- public-representation, transform-receipt, reality-boundary, uncertainty, and candidate-status field validators;
- release-candidate blocker builders;
- catalog receipt emitters, if not shared;
- hold routing helpers for missing evidence, missing review, policy defects, source-role collapse, candidate-boundary collapse, graph projection failure, or release-readiness blockers.

A good placement test:

> If the code converts processed Archaeology records into evidence-bound catalog records, graph/triplet projections, catalog receipts, or release-candidate blockers, it may belong here. If it fetches sources, admits sources, normalizes records, validates records, defines schemas, decides policy, decides review outcomes, approves release, or serves governed API/map output, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Source fetchers and API clients | `connectors/<source>` or accepted connector home |
| Ingest/source admission | `pipelines/domains/archaeology/ingest/` |
| Normalization mappers | `pipelines/domains/archaeology/normalize/` |
| Validation logic | `pipelines/domains/archaeology/validate/` |
| Publish artifact builders | `pipelines/domains/archaeology/publish/` |
| Rollback support | `pipelines/domains/archaeology/rollback/` |
| Domain doctrine and object meaning | `docs/domains/archaeology/`, `contracts/domains/archaeology/` |
| Source descriptors / source registry entries | `data/registry/sources/archaeology/` or approved registry home |
| JSON Schemas | `schemas/contracts/v1/domains/archaeology/` or accepted schema home |
| Policy, rights, review, release rules | `policy/...` and review responsibility roots |
| Declarative run specs | `pipeline_specs/archaeology/...` |
| Fixtures | `fixtures/domains/archaeology/catalog/` or accepted fixture home |
| Tests | `tests/pipelines/domains/archaeology/catalog/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published lifecycle records | `data/...` lifecycle homes |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Release decisions and manifests | `release/...` responsibility roots |

[⬆ Back to top](#top)

---

## 6. Catalog scope

| Scope area | Catalog responsibility | Failure behavior |
|---|---|---|
| Processed input | Confirm processed records, validation reports, receipts, policy state, review state, and digests exist. | Hold at PROCESSED. |
| Evidence closure | Resolve EvidenceRefs to EvidenceBundles and verify digest closure. | Hold; no public edge. |
| Catalog metadata | Build catalog entries with source role, time, representation, object family, public-safe labels, and lifecycle refs. | Hold on incomplete metadata. |
| Candidate boundary | Preserve candidate, model, survey, record, interpretation, and confirmed-record distinctions. | Fail on collapse. |
| Review/policy | Carry ReviewRecord and PolicyDecision refs forward. | Hold when required refs are missing. |
| Graph/triplet | Emit graph/triplet projections with provenance and invalidation refs. | Hold on graph projection failure. |
| Release blockers | Emit release-candidate readiness and blockers. | No direct publish. |
| Correction/rollback | Carry correction path and rollback target expectations forward. | Hold if missing for release-capable material. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Archaeology catalog run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** approved fixtures, processed Archaeology records, validation reports, transform receipts, review records, policy decisions, and EvidenceRef candidates.
2. **Resolve** EvidenceRefs to EvidenceBundles and verify digest closure, source-role continuity, review state, public-representation state, rights, and candidate-boundary labels.
3. **Emit** catalog matrix entries, metadata records, graph/triplet projections, catalog receipts, and release-readiness blockers into accepted lifecycle homes.
4. **Hold** missing evidence, missing review, policy defects, source-role collapse, candidate-boundary collapse, missing transform receipts, graph projection errors, schema drift, or release-blocking defects.
5. **Prepare** release-candidate handoffs only when catalog/proof closure succeeds.
6. **Never publish directly.**

Catalog closure is the PROCESSED-to-CATALOG/TRIPLET proof gate. It is not public release and not public serving.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Archaeology catalog run must check or explicitly fail closed on:

1. **Processed input gate** — processed record, validation report, receipts, policy state, review state, and digest refs exist.
2. **EvidenceBundle gate** — EvidenceRefs resolve and claim-bearing records have proof closure.
3. **CatalogMatrix gate** — catalog entry exists with object family, source role, rights, review state, time, representation scope, and lifecycle refs.
4. **Candidate-boundary gate** — candidate features, survey records, model outputs, interpretations, and confirmed-record claims remain distinct.
5. **Representation gate** — public-safe representation, transform receipts, and reality-boundary notes are attached where required.
6. **PROV gate** — ingest, normalization, validation, catalog, transformation, and review activities are recorded or referenced.
7. **Graph/triplet gate** — graph deltas/triplets carry provenance, source refs, evidence refs, and invalidation refs.
8. **Policy/review gate** — finite policy outcome and review state exist where materiality requires it.
9. **Release-blocker gate** — missing rollback target, correction path, review record, transform receipt, or release review becomes an explicit blocker.
10. **No-direct-publish gate** — catalog does not write public UI, public API, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/archaeology/catalog/
├── README.md                         # this file
├── CATALOG_CONTRACT.md               # PROPOSED: Archaeology catalog execution contract
├── run_dry_fixture.py                # PROPOSED synthetic/public-safe fixture only
├── build_catalog_matrix_entry.py     # PROPOSED
├── resolve_evidence_bundle_refs.py   # PROPOSED
├── build_stac_dcat_prov.py           # PROPOSED
├── build_graph_triplets.py           # PROPOSED
├── validate_candidate_boundary.py    # PROPOSED
├── validate_review_policy.py         # PROPOSED
├── validate_public_representation.py # PROPOSED
├── build_release_blockers.py         # PROPOSED
├── route_hold.py                     # PROPOSED
├── emit_catalog_receipt.py           # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/archaeology/catalog.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use accepted lifecycle homes under `data/catalog/domain/archaeology/`, `data/triplets/archaeology/`, `data/receipts/`, `data/proofs/evidence_bundle/`, and `release/candidates/archaeology/` before downstream release and published-layer roots.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/archaeology/catalog/` or accepted fixture home | Synthetic/public-safe processed/catalog fixture. |
| Processed input | `data/processed/archaeology/<dataset_id>/<version>/` | Validated candidate input. |
| ValidationReport | `data/processed/archaeology/` or accepted validation-report home | Required validation proof. |
| EvidenceBundle | `data/proofs/evidence_bundle/` | Required claim proof. |
| Review / policy refs | accepted review and policy homes | Required where materiality or sensitivity applies. |
| Catalog record | `data/catalog/domain/archaeology/` | Discovery/proof projection; not public. |
| Triplet / graph delta | `data/triplets/archaeology/` or accepted graph-delta home | Provenance-bound projection only. |
| Catalog receipt | `data/receipts/pipeline/archaeology/catalog/<run_id>.yml` or accepted receipt home | Records inputs, checks, digests, and output refs. |
| Release candidate blocker | `release/candidates/archaeology/` or accepted release-candidate home | Handoff only; no release decision. |

[⬆ Back to top](#top)

---

## 11. Minimal catalog closure record

The final schema is not defined here. This example shows the minimum information an Archaeology catalog closure record should preserve.

```yaml
schema_version: kfm.archaeology_catalog_closure.v1
catalog_run_id: archaeology_catalog_run_YYYYMMDDThhmmssZ
pipeline_id: domains.archaeology.catalog
status: HOLD
input:
  processed_ref: data/processed/archaeology/<dataset_id>/<version>/<object_id>.json
  validation_report_ref: data/processed/archaeology/<dataset_id>/<version>/validation_report.yml
  source_descriptor_ref: data/registry/sources/archaeology/<source_id>.yml
catalog:
  catalog_record_ref: data/catalog/domain/archaeology/<dataset_id>/<version>/<object_id>.json
  object_family: <ArchaeologyObjectFamily>
  source_role: <record|survey|candidate|model|aggregate|interpretation|synthetic>
  candidate_boundary_state: needs_review
evidence:
  evidence_ref_candidates: []
  evidence_bundle_ref: null
  evidence_resolved: false
review_policy:
  review_record_ref: null
  policy_decision_ref: null
  review_resolved: false
representation:
  public_representation_ref: null
  transform_receipt_ref: null
  reality_boundary_note_ref: null
graph:
  triplet_refs: []
  graph_delta_ref: null
release_readiness:
  release_candidate_ref: null
  blockers:
    - EVIDENCE_OR_REVIEW_OR_REPRESENTATION_OR_ROLLBACK_NOT_RESOLVED
anti_collapse:
  catalog_record_is_publication: false
  catalog_record_is_evidence_bundle: false
  triplet_projection_is_canonical_truth: false
  candidate_feature_is_confirmed_record: false
outputs:
  receipt_ref: data/receipts/pipeline/archaeology/catalog/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/public-safe, and no-network** until catalog specs, processed fixtures, evidence fixtures, policy fixtures, review fixtures, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/archaeology/catalog/
├── test_no_network_dry_run.py              # PROPOSED
├── test_processed_input_required.py        # PROPOSED
├── test_validation_report_required.py      # PROPOSED
├── test_evidence_bundle_required.py        # PROPOSED
├── test_catalog_matrix_entry_required.py   # PROPOSED
├── test_review_policy_required.py          # PROPOSED
├── test_candidate_boundary_preserved.py    # PROPOSED
├── test_public_representation_required.py  # PROPOSED
├── test_graph_triplet_provenance.py        # PROPOSED
├── test_release_blockers_emitted.py        # PROPOSED
├── test_no_public_artifact_write.py        # PROPOSED
├── test_receipt_hashes.py                  # PROPOSED
└── test_no_direct_publish.py               # PROPOSED
```

A dry run should prove fixtures load without network access, processed inputs and validation reports are required, EvidenceBundles resolve, catalog matrix entries close, review/policy refs are present, candidate boundaries are preserved, graph/triplet projections carry provenance, release blockers are explicit, receipts are deterministic, and no run writes directly to public UI, public API, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

Archaeology catalog pipelines may prepare catalog records, graph/triplet projections, release-candidate blockers, and receipts. They do not publish.

Required chain:

```text
processed Archaeology object + ValidationReport
  -> EvidenceBundle closure
  -> CatalogMatrix entry
  -> graph / triplet projection
  -> release candidate blockers
  -> ReleaseManifest
  -> RollbackCard
  -> public-safe artifact
```

Correction and rollback posture:

- denied, held, failed, restricted, stale, conflicted, and incomplete catalog runs remain auditable;
- receipts preserve source refs, processed refs, validation refs, EvidenceBundle refs, review refs, policy refs, catalog refs, graph refs, representation refs, and failure reasons;
- catalog records are superseded through governed state transitions, not hidden overwrite;
- downstream artifacts are invalidated if source refs, validation refs, EvidenceBundle refs, review refs, policy refs, catalog refs, graph refs, representation refs, correction refs, or rollback refs drift;
- release rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/archaeology/catalog/README.md` file;
- identifies this directory as a nested executable Archaeology catalog-closure sublane;
- prevents connector, source-admission, normalization, validation, schema, contract, policy, review-decision, fixture, test, data, public API, UI, release-decision, and publish authority from being placed here;
- preserves processed input, ValidationReport, EvidenceRef, EvidenceBundle, CatalogMatrix, ReviewRecord, PolicyDecision, PROV, graph/triplet, representation state, release-blocker, correction, and rollback boundaries;
- blocks catalog-record-as-publication, catalog-record-as-EvidenceBundle, EvidenceRef-as-EvidenceBundle, triplet-as-canonical-truth, candidate-as-confirmed-record, generated-summary-as-evidence, and direct publication writes;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has processed fixtures, no-network tests, schema-backed catalog records, EvidenceBundle closure, catalog/triplet provenance tests, review/policy tests, representation tests, release-blocker tests, deterministic receipts, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `ARCH-CAT-001` | Should Archaeology catalog remain one sublane, or split into evidence closure, catalog matrix, graph projection, representation, and release-blocker processors? | NEEDS VERIFICATION / ADR |
| `ARCH-CAT-002` | Which schema owns catalog closure records, catalog receipts, graph deltas, and release blockers? | NEEDS VERIFICATION |
| `ARCH-CAT-003` | Which catalog fixture set should be first-wave: survey records, candidate features, chronology context, collection records, documentation surfaces, or generalized public-safe records? | NEEDS VERIFICATION |
| `ARCH-CAT-004` | Which CI job owns Archaeology catalog invariant tests? | UNKNOWN |
| `ARCH-CAT-005` | What graph/triplet vocabulary should be used for archaeology object-family, source-role, review, evidence, and representation relationships? | NEEDS VERIFICATION / ADR |
| `ARCH-CAT-006` | Should release candidates be emitted by catalog closure or by a separate release-prep sublane? | NEEDS VERIFICATION |
| `ARCH-CAT-007` | Which representation receipt is canonical for catalog-bound public-safe archaeology artifacts? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic/public-safe processed fixtures and negative tests. Do not add live source fetching, ingest authority, normalization authority, validation authority, schema authority, policy authority, review-decision authority, direct public API code, direct UI code, release-manifest writes, public layer writes, or generated archaeology summaries until EvidenceBundle refs, catalog matrix entries, graph/triplet projections, review/policy refs, representation receipts, release blockers, deterministic receipts, and rollback expectations are proven.

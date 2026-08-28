<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-hydrology-triplets-readme
title: Hydrology Triplets Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <hydrology-pipeline-owner>
  - <hydrology-domain-steward>
  - <graph-steward>
  - <catalog-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipelines/domains/hydrology/triplets/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/catalog/README.md
  - pipelines/domains/README.md
  - pipelines/domains/hydrology/README.md
  - pipelines/domains/hydrology/catalog/README.md
  - pipelines/domains/hydrology/catalog_close/README.md
  - docs/domains/hydrology/README.md
  - docs/domains/hydrology/DATA_LIFECYCLE.md
  - docs/domains/hydrology/PUBLICATION_POSTURE.md
  - docs/domains/hydrology/IDENTITY_MODEL.md
  - pipeline_specs/hydrology/triplets.yaml
  - contracts/domains/hydrology/
  - schemas/contracts/v1/domains/hydrology/
  - policy/domains/hydrology/
  - policy/sensitivity/hydrology/
  - data/processed/hydrology/
  - data/catalog/domain/hydrology/
  - data/triplets/hydrology/
  - data/quarantine/hydrology/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/hydrology/
  - release/manifests/hydrology/
tags:
  - kfm
  - pipelines
  - domains
  - hydrology
  - triplets
  - graph-projection
  - relationship-delta
  - evidence-bundle
  - source-role
  - provenance
  - review-state
  - watershed
  - huc
  - reach
  - gauge
  - topology
  - governance
notes:
  - "This README fills the blank pipelines/domains/hydrology/triplets path as a nested executable graph/triplet projection sublane."
  - "Hydrology triplet logic is executable projection support only; it does not own graph truth, catalog truth, object meaning, source descriptors, schemas, policy, lifecycle data, release decisions, or public API authority."
  - "Triplet outputs are downstream projections from processed Hydrology records and EvidenceBundle-backed catalog candidates; they do not replace canonical records, EvidenceBundles, validation, review state, policy, catalog state, or release state."
  - "Observed readings, modeled hydrographs, regulatory context, official-source context, derived topology, aggregates, and generated summaries must remain separate relationship classes."
  - "Regulatory-context records must never project as observed-condition records."
  - "Concrete executable behavior, graph schema, schedules, CI coverage, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology Triplets Pipeline

> Executable Hydrology sublane for building governed relationship and graph-projection candidates from processed Hydrology records and catalog handoffs. It preserves EvidenceBundle references, source roles, time/freshness state, provenance, review state, policy outcome, correction path, and rollback targets without turning graph projections into canonical truth.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-hydrology%20triplet%20projection-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20projection%20logic-0a7ea4)
![anti-collapse](https://img.shields.io/badge/triplet%20%E2%89%A0%20canonical%20truth-d62728)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/hydrology/triplets/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Hydrology  
**Sublane:** Triplet / graph projection  
**Placement posture:** nested executable sublane under `pipelines/domains/hydrology/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Publication posture:** no direct publication; graph outputs require processed-state input, EvidenceBundle closure, source-role separation, policy outcome, catalog/graph closure, release handoff, correction path, and rollback closure

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Triplet anti-collapse rules](#3-triplet-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Projection scope](#6-projection-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal triplet projection record](#11-minimal-triplet-projection-record)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Promotion, publication, correction, and rollback](#13-promotion-publication-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/domains/hydrology/triplets/` is the executable sublane for Hydrology graph/triplet projection.

It supports candidate processing for relationships such as:

- watershed contains HUC unit;
- HUC unit contains reach, waterbody, gauge, site, or observation dataset;
- stream/reach relates to another reach through an approved topology predicate;
- gauge observes variable at a site;
- observation belongs to site, source, parameter, time interval, and evidence bundle;
- regulatory context references a Hydrology feature while remaining regulatory context;
- NHDPlus HR network topology relates upstream/downstream features while preserving modeled topology lineage;
- WBD/HUC context links Hydrology features to cross-domain summaries without becoming cross-domain truth;
- 3DEP terrain support relates to hydrology processing without becoming observed hydrology;
- catalog candidates, graph deltas, release candidates, correction notices, and rollback packages remain cross-referenced but distinct.

This directory implements or will implement the **how** of triplet projection. It does not fetch source data, define Hydrology object meaning, define graph schemas, encode policy, store graph truth, mutate canonical records, decide release, issue official notices, or decide regulatory meaning.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/hydrology/`? | Hydrology is the domain lane used by Hydrology docs and pipeline READMEs. | CONFIRMED documentation pattern; behavior NEEDS VERIFICATION |
| Why `triplets/`? | This is a narrow executable lane for Hydrology-specific graph/triplet projection. | PROPOSED / NEEDS VERIFICATION |
| Does this replace `catalog/`? | No. Catalog handoff may prepare graph/triplet candidates; this lane is for Hydrology-specific relationship projection logic. | PROPOSED |
| Where do graph deltas live? | `data/triplets/hydrology/` or approved graph-delta home. | PROPOSED / NEEDS VERIFICATION |
| Does this own graph truth? | No. It emits projections with provenance and review-state refs; canonical records and EvidenceBundles remain separate. | CONFIRMED governance posture |
| Can this sublane publish? | No. It may prepare graph/triplet handoffs only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> Triplet candidates are projections. They are not canonical source records, not EvidenceBundles, not catalog truth, not release approval, and not a replacement for review state. A triplet output that lacks evidence, policy, source-role, time/freshness, correction, and rollback closure must abstain, deny, or quarantine.

[⬆ Back to top](#top)

---

## 3. Triplet anti-collapse rules

Hydrology triplet work must preserve truth class, provenance, and lifecycle state.

Disallowed collapses:

```text
triplet projection -> canonical truth
triplet edge -> EvidenceBundle
triplet delta -> review approval
catalog candidate -> public graph without release
regulatory context -> observed condition
observed reading -> modeled hydrograph
modeled topology -> field-observed relationship
WBD/HUC context link -> cross-domain truth
terrain support -> observed hydrology
generated summary edge -> evidence
rollback tombstone -> erased provenance
```

Required distinctions:

- source role and knowledge character are explicit on every node/edge where material;
- observed, modeled, regulatory, administrative, aggregate, derived, official-source context, and generated records remain distinct;
- relationship type, subject, predicate, object, evidence refs, source refs, policy refs, and time scope are explicit;
- observation time, valid time, source time, retrieval time, processing time, projection time, release time, and correction time remain distinct;
- graph deltas are appendable/auditable and do not silently mutate prior projections;
- public graph exposure requires release workflow closure.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable Hydrology graph/triplet projection.

Appropriate contents include:

- fixture-only triplet projection entrypoints;
- Hydrology node and edge candidate builders;
- relationship mappers for watershed, HUC, reach, waterbody, gauge, site, observation, regulatory context, topology, terrain support, and catalog records;
- predicate normalization helpers that preserve source-role and evidence state;
- graph delta builders with provenance and review-state refs;
- source-role and knowledge-character validators for graph edges;
- regulatory-context anti-collapse validators;
- observed/model/topology/terrain anti-collapse validators;
- EvidenceBundle reference validators;
- correction, tombstone, supersession, and rollback reference validators;
- receipt emitters, if not shared;
- thin adapters that read governed lifecycle inputs, not live source systems.

A good placement test:

> If the code transforms processed Hydrology records or closed catalog candidates into graph/triplet projection candidates with provenance and review-state refs, it may belong here. If it fetches source data, defines schemas, stores graph truth, decides policy, writes public graph artifacts, or approves release, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Source fetchers / connectors | `connectors/<source>` |
| Source descriptors / source registry entries | `data/registry/sources/hydrology/` or approved registry home |
| Hydrology architecture and doctrine | `docs/domains/hydrology/...` |
| Object meaning contracts | `contracts/domains/hydrology/` or accepted contract home |
| JSON Schemas or graph schemas | `schemas/contracts/v1/domains/hydrology/` or accepted schema home |
| Policy, rights, sensitivity, release rules | `policy/...` responsibility roots |
| Shared catalog framework logic | `pipelines/catalog/` or shared packages |
| Hydrology catalog handoff logic | `pipelines/domains/hydrology/catalog/` unless triplet projection is split here by ADR/spec |
| Declarative run specs | `pipeline_specs/hydrology/...` |
| Fixtures | `fixtures/domains/hydrology/triplets/` or accepted fixture home |
| Tests | `tests/pipelines/domains/hydrology/triplets/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Receipts and proofs | `data/receipts/...`, `data/proofs/...` |
| Release decisions | `release/candidates/hydrology/`, `release/manifests/hydrology/`, rollback/correction release homes |
| Public API, map, graph browser, or UI code | `apps/governed-api/`, `apps/explorer-web/`, packages |

[⬆ Back to top](#top)

---

## 6. Projection scope

| Scope area | Triplet responsibility | Failure behavior |
|---|---|---|
| Hydrology identity | Emit relationship candidates using stable source-bound IDs. | Quarantine if identity refs are unstable. |
| Watershed/HUC relations | Preserve hierarchy, source vintage, and evidence refs. | Abstain or quarantine on missing hierarchy support. |
| Reach/topology relations | Preserve modeled/derived topology lineage. | Deny if treated as observed relationship. |
| Gauge/site relations | Preserve station/site identity, variable, source role, and freshness. | No current-state implication without freshness state. |
| Observation relations | Preserve parameter, unit, time, QA, source, and evidence refs. | Quarantine on time/unit/source-role collapse. |
| Regulatory context | Label as regulatory context only. | Deny if treated as observed event. |
| Cross-domain context | Emit context edges with owning-domain refs and policy outcomes. | Deny if projection asserts cross-domain truth. |
| Release/rollback refs | Preserve correction, supersession, tombstone, and rollback refs. | Deny if provenance would be erased. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Hydrology triplet run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** approved fixtures, processed hydrology records, validation reports, catalog candidates, EvidenceBundle refs, policy outcomes, public-safe transform refs, correction refs, and rollback refs.
2. **Validate** source role, evidence refs, relationship types, identity refs, time/freshness state, sensitivity/public-safe state, correction path, and rollback target.
3. **Emit** graph/triplet delta candidates only into accepted lifecycle homes.
4. **Quarantine** missing EvidenceBundle, missing source role, invalid predicate, identity instability, regulatory/observed collapse, model/observation collapse, missing rollback target, schema drift, policy failure, or validation failure.
5. **Support release** only by providing reviewable graph handoff packages to catalog/release workflow.
6. **Never publish directly.**

Triplet projection is a projection step. It is not canonical truth and not public release by itself.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Hydrology triplet run must check or explicitly fail closed on:

1. **Input lifecycle gate** — input is processed, fixture-only, catalog candidate, or explicitly release-candidate material.
2. **Identity gate** — subject/object identifiers are deterministic and source-bound.
3. **Predicate gate** — relationship predicate is approved and does not overclaim truth.
4. **Source descriptor gate** — source identity, role, rights, cadence/freshness, and sensitivity posture are known.
5. **Source-role gate** — observed, modeled, regulatory, administrative, official-source context, aggregate, derived, and generated records remain distinct.
6. **Regulatory-context gate** — regulatory-context records remain regulatory context, not observed-condition records.
7. **Gauge/time-series gate** — variable, unit, cadence, observed time, valid time, retrieval time, and processing time are preserved.
8. **Model/topology receipt gate** — model, reconstruction, terrain, or topology relationships carry method receipt refs.
9. **Evidence gate** — claim-bearing relationships resolve EvidenceBundle support or abstain.
10. **Policy gate** — finite policy outcome exists; no silent allow.
11. **Projection gate** — graph deltas preserve provenance and do not replace canonical records, catalog records, or review state.
12. **Correction/rollback gate** — correction path and rollback target are present before release handoff.
13. **No-direct-publish gate** — no writes to public UI, public API, published graph artifacts, or release manifests without release workflow authority.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/hydrology/triplets/
├── README.md                         # this file
├── TRIPLET_CONTRACT.md               # PROPOSED: hydrology triplet projection contract
├── run_dry_fixture.py                # PROPOSED synthetic/redacted fixture only
├── build_node_candidates.py          # PROPOSED
├── build_edge_candidates.py          # PROPOSED
├── build_graph_delta.py              # PROPOSED
├── normalize_predicates.py           # PROPOSED
├── validate_identity_refs.py         # PROPOSED
├── validate_source_roles.py          # PROPOSED
├── validate_evidence_refs.py         # PROPOSED
├── validate_projection_not_truth.py  # PROPOSED
├── validate_correction_rollback.py   # PROPOSED
├── emit_receipt.py                   # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/hydrology/triplets.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use accepted graph homes under `data/triplets/hydrology/`, catalog homes under `data/catalog/domain/hydrology/`, quarantine homes under `data/quarantine/hydrology/`, proof homes under `data/proofs/`, receipt homes under `data/receipts/`, and release homes under `release/`.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/hydrology/triplets/` or accepted fixture home | Synthetic, generalized, or redacted. |
| Processed hydrology input | `data/processed/hydrology/<dataset_id>/<version>/` | Validated/restricted; not automatically public. |
| Catalog candidate input | `data/catalog/domain/hydrology/...` or approved catalog home | Projection source after catalog validation. |
| Evidence input | `data/proofs/evidence_bundle/` or accepted proof home | Required for claim-bearing relationships. |
| Graph delta candidate | `data/triplets/hydrology/...` or approved graph-delta home | Projection only. |
| Quarantine record | `data/quarantine/hydrology/<reason>/<run_id>/` | Failed, restricted, unresolved, or unsafe material. |
| Run receipt | `data/receipts/pipeline/hydrology/triplets/<run_id>.yml` or accepted receipt home | Records inputs, predicates, evidence refs, and outputs. |
| Release handoff | `release/candidates/hydrology/...` | Only through release workflow. |

[⬆ Back to top](#top)

---

## 11. Minimal triplet projection record

The final schema is not defined here. This example shows the minimum information a Hydrology triplet projection should preserve.

```yaml
schema_version: kfm.hydrology_triplet_projection.v1
projection_id: hydrology_triplet_<subject>_<predicate>_<object>_<run_id>_<hash>
pipeline_id: domains.hydrology.triplets
run_id: run_YYYYMMDDThhmmssZ
status: TRIPLET_CANDIDATE
subject:
  id: <hydrology_subject_id>
  family: <watershed|huc_unit|reach|gauge|site|waterbody|observation|regulatory_context|terrain_support|catalog_item>
predicate:
  id: <approved_predicate_id>
  label: <contains|observes|relates_to|intersects_context|has_evidence|derived_from|supersedes|withdraws>
object:
  id: <hydrology_object_id>
  family: <hydrology_or_context_family>
source:
  source_ids: []
  source_roles: []
  knowledge_character: <observed|modeled|regulatory_context|administrative|aggregate|derived|generated_context>
provenance:
  processed_ref: data/processed/hydrology/<dataset_id>/<version>/
  catalog_ref: data/catalog/domain/hydrology/<dataset_id>/<version>/catalog.json
  evidence_bundle_ref: data/proofs/evidence_bundle/<bundle_id>.json
  policy_decision_ref: null
time:
  valid_start: null
  valid_end: null
  observed_at: null
  projected_at: YYYY-MM-DDThh:mm:ssZ
anti_collapse:
  triplet_is_canonical_truth: false
  triplet_is_evidence_bundle: false
  regulatory_context_is_observed_condition: false
  modeled_topology_is_observed_relationship: false
  generated_summary_is_evidence: false
outputs:
  graph_delta_ref: data/triplets/hydrology/<dataset_id>/<version>/delta.jsonl
  receipt_ref: data/receipts/pipeline/hydrology/triplets/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/generalized/redacted, and no-network** until graph predicate profile, evidence, policy, release posture, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/hydrology/triplets/
├── test_no_network_dry_run.py             # PROPOSED
├── test_processed_or_catalog_input_required.py # PROPOSED
├── test_identity_refs_required.py         # PROPOSED
├── test_predicate_allowlist_required.py   # PROPOSED
├── test_source_role_required.py           # PROPOSED
├── test_regulatory_context_not_observed.py # PROPOSED
├── test_observed_not_modeled.py           # PROPOSED
├── test_graph_delta_not_canonical_truth.py # PROPOSED
├── test_triplet_not_evidence_bundle.py    # PROPOSED
├── test_cross_domain_context_not_truth.py # PROPOSED
├── test_evidence_bundle_required.py       # PROPOSED
├── test_rollback_target_required.py       # PROPOSED
├── test_receipt_hashes.py                 # PROPOSED
└── test_no_direct_publish.py              # PROPOSED
```

A dry run should prove fixtures load without network access, processed/catalog inputs are required, predicates are allowlisted, source roles are present, regulatory context stays regulatory context, graph deltas do not replace canonical truth, EvidenceBundle gaps produce abstention, receipts are deterministic, and no run writes directly to public UI, public API, published graph artifacts, or release manifests.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

Hydrology triplet pipelines may prepare graph candidates. They do not publish.

Required promotion chain:

```text
processed Hydrology record / closed catalog candidate
  -> triplet projection candidate
  -> graph delta validation
  -> policy decision
  -> EvidenceBundle closure
  -> catalog / triplet candidate
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> released graph artifact
```

Correction and rollback posture:

- denied, abstained, errored, restricted, stale, conflicted, and quarantined graph runs remain auditable;
- graph deltas preserve input hashes, predicate refs, evidence refs, source-role refs, and policy outcomes;
- graph deltas are superseded by governed state transition, not hidden overwrite;
- triplet candidates are invalidated if processed refs, EvidenceBundle refs, policy refs, source-role refs, predicate refs, catalog refs, correction refs, or rollback refs drift;
- graph rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/hydrology/triplets/README.md` file;
- identifies this directory as a nested executable Hydrology graph/triplet projection sublane;
- prevents source fetcher, source-profile, schema, contract, policy, fixture, test, data, proof, catalog-store, graph-store, app, UI, and release authority from being placed here;
- preserves source role, knowledge character, identity, predicates, evidence refs, policy refs, lifecycle, catalog/triplet, release, correction, and rollback boundaries;
- blocks triplet-as-canonical-truth, triplet-as-evidence, regulatory-context-as-observed, model-as-observation, WBD-context-as-truth, generated-summary-as-evidence, and direct graph/publication writes;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has processed/catalog fixtures, predicate allowlists, schema-backed graph deltas, contract conformance, source-role/evidence/policy/projection/no-direct-publish tests, deterministic receipts, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `HYDRO-TRIPLETS-001` | Should Hydrology triplet projection remain domain-specific, or should shared graph projection live in a central graph pipeline with Hydrology adapters? | NEEDS VERIFICATION / ADR |
| `HYDRO-TRIPLETS-002` | Which schema owns Hydrology predicates, node refs, edge refs, graph deltas, and quarantine reasons? | NEEDS VERIFICATION |
| `HYDRO-TRIPLETS-003` | Which first-wave predicates are approved: contains, observes, relates_to, intersects_context, derived_from, supersedes, withdraws, or has_evidence? | NEEDS VERIFICATION |
| `HYDRO-TRIPLETS-004` | Which CI job owns Hydrology triplet invariant tests? | UNKNOWN |
| `HYDRO-TRIPLETS-005` | Should graph projection be produced directly from processed records or only from catalog-close outputs? | NEEDS VERIFICATION |
| `HYDRO-TRIPLETS-006` | How should cross-domain context edges be policy-reviewed so they do not become cross-domain truth claims? | NEEDS VERIFICATION |
| `HYDRO-TRIPLETS-007` | Which rollback format is required for released graph artifacts? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic/generalized fixture-only dry runs and negative tests. Do not add live source fetching, schema authority, direct graph-store writes, direct public API code, direct UI code, release-decision logic, or generated relationship summaries until source roles, predicates, evidence refs, catalog/graph closure, release review, correction, and rollback are proven.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-triplets-readme
title: Triplets Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <pipeline-owner>
  - <graph-steward>
  - <catalog-steward>
  - <evidence-steward>
  - <policy-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public-with-graph-projection-and-release-gates
path: pipelines/triplets/README.md
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - pipelines/README.md
  - pipelines/catalog/README.md
  - pipelines/validate/README.md
  - pipeline_specs/triplets/
  - pipelines/domains/
  - data/processed/
  - data/catalog/
  - data/triplets/
  - data/quarantine/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/
  - release/manifests/
tags: [kfm, pipelines, triplets, graph-projection, provenance, evidence-bundle, catalog, receipts, governance]
notes:
  - "This README replaces the greenfield stub at pipelines/triplets/README.md with a governed implementation-lane contract."
  - "pipelines/ is executable logic; pipeline_specs/ is declarative configuration."
  - "This path is shared graph/triplet projection support, not a graph truth store, catalog authority, schema home, contract home, policy home, proof store, or release authority."
  - "Domain-specific triplet projection remains under domain lanes such as pipelines/domains/<domain>/triplets/ unless an ADR says otherwise."
  - "Concrete executable behavior, graph schema, CI coverage, fixtures, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Triplets Pipelines

> Shared executable graph/triplet projection lane for relationship candidates, graph deltas, provenance-bound edges, catalog handoffs, receipts, and release-readiness blockers — without owning canonical truth, EvidenceBundle truth, catalog truth, release decisions, policy decisions, schemas, contracts, or public API/UI behavior.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-shared%20triplets-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20projection%20logic-0a7ea4)
![truth](https://img.shields.io/badge/triplet%20%E2%89%A0%20canonical%20truth-d62728)
![publication](https://img.shields.io/badge/publication-no%20direct%20publish-d62728)

**Status:** Draft  
**Path:** `pipelines/triplets/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Sublane:** Shared triplet / graph projection support  
**Placement posture:** implementation sublane under `pipelines/`; exact long-term authority remains `NEEDS VERIFICATION / ADR` if this becomes a shared graph framework rather than a small helper lane  
**Public posture:** no direct publication; triplet outputs are graph projections, receipts, relationship candidates, and release-readiness blockers only.

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

`pipelines/triplets/` is the shared executable lane for relationship and graph-projection support that is useful across multiple KFM domain pipelines.

It may support:

- relationship candidate builders;
- graph-delta and triplet projection helpers;
- provenance, source-role, time, and evidence-reference preservation helpers;
- catalog-to-triplet handoff helpers;
- cross-domain relationship checks;
- duplicate-edge and identity-stability checks;
- graph invalidation and supersession helpers;
- no-network fixture runners;
- receipt and blocker builders;
- shared adapters used by domain-specific triplet sublanes.

This directory implements or will implement the **how** of shared graph projection support. It does not define graph truth, define domain object meaning, define graph schemas, decide policy, create EvidenceBundles, write catalog truth, approve release, or serve public clients.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | Triplet helpers are executable projection logic: the **how**. | CONFIRMED root responsibility |
| Why a shared `triplets/` lane? | It can hold reusable graph/triplet helpers that should not be duplicated across domain lanes. | PROPOSED / NEEDS VERIFICATION |
| Does this replace domain triplet lanes? | No. Domain-owned relationship logic stays under `pipelines/domains/<domain>/triplets/` or accepted domain graph sublanes. | CONFIRMED boundary posture |
| Is this a graph truth store? | No. Graph/triplet data belongs in accepted `data/triplets/` or graph-delta homes. | CONFIRMED authority separation |
| Is this a schema or contract home? | No. Schemas and contracts remain in their own responsibility roots. | CONFIRMED authority separation |
| Can public clients read this lane? | No. Public clients use governed APIs and released artifacts only. | CONFIRMED trust-membrane posture |

> [!IMPORTANT]
> A triplet projection is not canonical truth, not an EvidenceBundle, not catalog closure, and not release approval. It is a downstream carrier that must preserve evidence, source-role, review, time, correction, and rollback references.

[⬆ Back to top](#top)

---

## 3. Triplet anti-collapse rules

Disallowed collapses:

```text
triplet projection -> canonical truth
graph edge -> EvidenceBundle
relationship candidate -> confirmed fact
catalog record -> graph truth
EvidenceRef -> EvidenceBundle
schema-valid edge -> public claim
cross-domain edge -> new domain authority
generated graph summary -> evidence
pipeline run -> ReleaseManifest
```

Required distinctions:

- processed object, catalog entry, triplet projection, graph delta, EvidenceBundle, ReviewRecord, validation report, release candidate, ReleaseManifest, CorrectionNotice, RollbackCard, and public artifact remain separate;
- domain object ownership remains with the source domain lane;
- edges carry source, evidence, provenance, predicate, time, confidence, and review context;
- relationship candidates remain candidates until the owning process closes them;
- release-facing graph claims resolve EvidenceBundle support or abstain.

[⬆ Back to top](#top)

---

## 4. What belongs here

Appropriate contents include:

- shared triplet README files;
- fixture-only graph projection dry-run entrypoints;
- predicate and relationship candidate helpers;
- provenance and EvidenceRef propagation helpers;
- graph-delta builders;
- duplicate-edge and deterministic-id helpers;
- cross-domain boundary checks;
- catalog-to-triplet handoff helpers;
- graph invalidation and supersession helpers;
- triplet receipt builders;
- shared adapters used by domain graph/triplet lanes.

A good placement test:

> If the code helps multiple domain pipelines project evidence-bound relationships without owning canonical truth, it may belong here. If it only belongs to one domain, place it in that domain's triplet lane. If it owns graph schemas, policy, catalog truth, release decisions, or public serving, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Domain-specific graph workflows | `pipelines/domains/<domain>/triplets/` |
| Ingest/source admission | `pipelines/ingest/` or domain ingest lanes |
| Normalization or validation logic | `pipelines/normalize/`, `pipelines/validate/`, or domain lanes |
| Catalog builders | `pipelines/catalog/` or domain catalog lanes |
| Source access clients | `connectors/<source_id>/` or accepted connector home |
| Domain doctrine | `docs/domains/<domain>/` |
| Graph schemas | `schemas/...` accepted schema home |
| Contracts/object meaning | `contracts/...` accepted contract home |
| Declarative triplet specs | `pipeline_specs/triplets/` or domain-specific spec homes |
| Fixtures | `fixtures/triplets/` or domain fixture homes |
| Tests | `tests/pipelines/triplets/` or domain test homes |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Graph data / triplet materialization | `data/triplets/` or accepted graph-delta home |
| Release decisions | `release/...` |
| Public API/UI code | `apps/governed-api/`, `apps/explorer-web/`, packages |

[⬆ Back to top](#top)

---

## 6. Projection scope

| Scope area | Shared triplet responsibility | Failure behavior |
|---|---|---|
| Caller scope | Require an owning domain pipeline, catalog lane, or approved proof harness. | Hold if ownerless. |
| Input lifecycle | Confirm input is processed, catalog-ready, cataloged, fixture, or approved recheck material. | Fail or hold. |
| Predicate shape | Check predicate, subject, object, time, provenance, and source-role fields. | Fail projection. |
| Evidence | Carry EvidenceRef/EvidenceBundle refs but do not create proof. | Hold or abstain if unresolved. |
| Domain boundary | Preserve owning domain for subject/object records and cross-domain edges. | Fail on ownership collapse. |
| Identity | Build deterministic edge ids and duplicate checks. | Hold on instability. |
| Receipts | Emit deterministic projection receipts and graph-delta refs. | Fail closed on missing hashes. |
| Handoff | Return graph/triplet outputs to caller. | No release or public-serving side effects. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every shared triplet helper must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** fixture, processed, catalog-ready, or catalog refs only when a domain or catalog pipeline authorizes the call.
2. **Project** relationship candidates with provenance, source role, evidence refs, time, confidence, and review context.
3. **Emit** graph deltas, triplet files, receipts, invalidation refs, or release-readiness blockers.
4. **Return** to the owning domain/catalog/release lane for catalog closure, release, and public artifact decisions.
5. **Never create EvidenceBundles, mutate canonical records, approve release, or publish.**

[⬆ Back to top](#top)

---

## 8. Required gates

Every shared triplet component must check or explicitly fail closed on:

1. **Caller ownership gate** — an owning domain pipeline, catalog lane, or approved proof harness must provide scope.
2. **Input lifecycle gate** — input is fixture, processed, catalog-ready, cataloged, or approved recheck material.
3. **Predicate gate** — relationship predicate and edge vocabulary are accepted for the caller scope.
4. **Subject/object gate** — subject and object ids are stable and domain ownership is preserved.
5. **Evidence gate** — EvidenceRefs are preserved and EvidenceBundle readiness is explicit.
6. **Provenance gate** — source refs, run refs, transform refs, and catalog refs are carried forward.
7. **Time/freshness gate** — valid time, observed time, run time, and stale state remain distinct.
8. **Receipt gate** — every projection invocation emits deterministic receipt metadata.
9. **No-direct-catalog gate** — shared triplet support does not close catalog state by itself.
10. **No-direct-publish gate** — shared triplet support does not write public UI, public API, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/triplets/
├── README.md
├── TRIPLETS_SHARED_CONTRACT.md        # PROPOSED
├── run_dry_fixture.py                 # PROPOSED
├── build_edge_id.py                   # PROPOSED
├── validate_predicate.py              # PROPOSED
├── validate_subject_object.py         # PROPOSED
├── propagate_evidence_refs.py         # PROPOSED
├── build_graph_delta.py               # PROPOSED
├── check_duplicate_edges.py           # PROPOSED
├── emit_triplet_receipt.py            # PROPOSED only if not shared
└── adapters/                          # PROPOSED domain/proof adapters only
```

Declarative specs should live outside this directory:

```text
pipeline_specs/triplets/<profile>.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use accepted lifecycle homes under `data/triplets/`, `data/catalog/`, `data/quarantine/`, and `data/receipts/`, with domain-owned pipelines deciding the target domain lane.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Shared fixture | `fixtures/triplets/` or domain fixture home | Synthetic/public-safe by default. |
| Declarative spec | `pipeline_specs/triplets/` or domain spec home | The what, not executable logic. |
| Candidate input | `data/processed/<domain>/` or `data/catalog/domain/<domain>/` | Read by stable refs only. |
| Graph delta / triplets | `data/triplets/<domain>/` or accepted graph-delta home | Projection output; not canonical truth. |
| QUARANTINE reason | `data/quarantine/<domain>/` | Owned by calling domain lane. |
| Receipt | `data/receipts/pipeline/<domain>/triplets/` or accepted receipt home | Records inputs, checks, outcomes, hashes, and output refs. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced only; not created here. |

[⬆ Back to top](#top)

---

## 11. Minimal triplet projection record

The final schema is not defined here. This example shows the minimum information a shared triplet projection receipt should preserve.

```yaml
schema_version: kfm.shared_triplet_projection_receipt.v1
triplet_run_id: triplet_run_YYYYMMDDThhmmssZ
pipeline_id: triplets.<profile_id>
status: HELD
caller:
  owner_pipeline: pipelines/domains/<domain>/triplets
  domain: <domain>
  profile_ref: pipeline_specs/triplets/<profile_id>.yaml
input:
  source_refs: []
  catalog_refs: []
  evidence_bundle_refs: []
edge:
  subject_id: null
  predicate: null
  object_id: null
  edge_id: null
checks:
  caller_scope_resolved: false
  predicate_allowed: false
  subject_object_stable: false
  domain_boundaries_preserved: false
  evidence_refs_preserved: false
  provenance_ready: false
  duplicate_checked: false
anti_collapse:
  triplet_projection_is_canonical_truth: false
  graph_edge_is_evidence_bundle: false
  relationship_candidate_is_confirmed_fact: false
  pipeline_run_is_release_decision: false
outputs:
  graph_delta_ref: null
  triplet_ref: null
  receipt_ref: data/receipts/pipeline/<domain>/triplets/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Recommended tests:

```text
tests/pipelines/triplets/
├── test_no_network_dry_run.py              # PROPOSED
├── test_caller_scope_required.py           # PROPOSED
├── test_input_lifecycle_required.py        # PROPOSED
├── test_predicate_allowed.py               # PROPOSED
├── test_subject_object_stable.py           # PROPOSED
├── test_domain_boundaries_preserved.py     # PROPOSED
├── test_evidence_refs_not_fabricated.py    # PROPOSED
├── test_provenance_required.py             # PROPOSED
├── test_duplicate_edges_checked.py         # PROPOSED
├── test_no_catalog_closure_side_effect.py  # PROPOSED
└── test_no_direct_publish.py               # PROPOSED
```

A dry run should prove fixtures load without network access, caller scope is required, input lifecycle is checked, predicates are accepted for scope, subject/object ids are stable, EvidenceRefs are not fabricated, provenance is carried forward, duplicate edges are checked, receipts are deterministic, and no run writes directly to catalog closure, public UI, public API, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

Shared triplet helpers may prepare graph deltas, triplet outputs, invalidation hints, blockers, and receipts. They do not publish.

Required chain:

```text
calling domain / catalog pipeline
  -> shared triplet helper
  -> graph delta / triplet projection / receipt
  -> catalog or graph closure review
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public artifact
```

Correction and rollback posture:

- failed triplet runs remain auditable;
- receipts preserve input refs, catalog refs, predicate refs, subject/object ids, evidence refs, provenance refs, and failure reasons;
- triplet outputs are superseded through governed state transitions, not hidden overwrite;
- downstream artifacts are invalidated if catalog refs, EvidenceBundle refs, predicate vocabularies, review refs, correction refs, or rollback refs drift;
- rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- replaces the greenfield stub at `pipelines/triplets/README.md`;
- identifies this directory as a shared executable graph/triplet projection support lane under `pipelines/`;
- prevents domain-specific logic, schemas, contracts, source descriptors, lifecycle data, EvidenceBundles, release decisions, public API, UI, catalog authority, and publication authority from being placed here;
- preserves caller scope, subject/object ownership, predicate vocabulary, EvidenceRef, EvidenceBundle-readiness, provenance, time, lifecycle, correction, and rollback boundaries;
- blocks triplet-projection-as-canonical-truth, graph-edge-as-EvidenceBundle, relationship-candidate-as-confirmed-fact, generated-summary-as-evidence, catalog side effects, and direct publication writes;
- gives maintainers a fixture-first, receipt-emitting, fail-closed expansion pattern.

Future executable work in this lane is done only when it has public-safe fixtures, no-network tests, caller-scope checks, predicate tests, subject/object identity tests, domain-boundary tests, evidence/provenance tests, duplicate-edge tests, deterministic receipts, CI coverage, domain/catalog steward handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `PIPE-TRIPLET-001` | Is `pipelines/triplets/` the final accepted home for shared graph/triplet helpers, or should this move under `packages/`, `tools/graph/`, or domain lanes by ADR? | NEEDS VERIFICATION / ADR |
| `PIPE-TRIPLET-002` | Which schema owns shared triplet projection receipts, graph deltas, predicates, and edge reason codes? | NEEDS VERIFICATION |
| `PIPE-TRIPLET-003` | Should every domain triplet sublane call shared helpers, or only use them for common predicate, identity, and provenance checks? | NEEDS VERIFICATION |
| `PIPE-TRIPLET-004` | Which CI job owns shared triplet invariant tests? | UNKNOWN |
| `PIPE-TRIPLET-005` | Which predicate profiles belong in `pipeline_specs/triplets/` versus domain-specific specs? | NEEDS VERIFICATION |
| `PIPE-TRIPLET-006` | Should shared triplet helpers emit graph deltas directly, or only return projection fragments to domain lanes? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic/public-safe fixtures and negative tests. Do not add live source calls, domain truth ownership, schema authority, catalog-closure shortcuts, public API code, UI code, release-manifest writes, published-layer writes, or generated summaries until caller scope, input lifecycle, predicate vocabulary, subject/object identity, EvidenceRef handling, provenance, deterministic receipts, and rollback expectations are proven.

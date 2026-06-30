<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/triplets/readme
name: Triplets Data README
path: data/triplets/README.md
type: data-lifecycle-stage-readme
version: v0.1.0
status: draft
owners:
  - <data-steward>
  - <graph-steward>
  - <catalog-steward>
  - <evidence-steward>
  - <proof-steward>
  - <receipt-steward>
  - <policy-steward>
  - <release-steward>
  - <domain-stewards>
  - <docs-steward>
created: 2026-06-29
updated: 2026-06-29
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
lifecycle_stage: CATALOG/TRIPLET
artifact_family: graph-compatible-relationship-projections
path_posture: existing-greenfield-stub-replaced; canonical-plural-triplets-lane-confirmed-by-data-readme-and-directory-rules; paired-with-data-catalog; literal-data-triplet-s-path-is-compatibility-only; implementation-maturity-needs-verification
sensitivity_posture: no-public-path-by-default; triplets-are-projections-not-canonical-truth; graph-derived-not-truth; relationship-projection-not-evidence; evidence-refs-required-for-evidence-bearing-claims; source-role-preserving; rights-aware; sensitivity-aware; policy-aware; release-gated; derivative-invalidation-required; correction-and-rollback-aware
related:
  - ../README.md
  - ../catalog/README.md
  - ../processed/README.md
  - ../proofs/README.md
  - ../receipts/README.md
  - ../published/README.md
  - ../registry/README.md
  - ../rollback/README.md
  - ../triplet(s)/README.md
  - ../../release/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/doctrine/lifecycle-law.md
  - ../../docs/doctrine/trust-membrane.md
  - ../../contracts/
  - ../../schemas/
  - ../../policy/
tags:
  - kfm
  - data
  - triplets
  - graph
  - relationship-projection
  - graph-deltas
  - exports
  - catalog-triplet
  - evidence-ref
  - evidence-bundle
  - proof-pack
  - catalog-closure
  - release-gated
  - no-public-path
  - graph-derived-not-truth
  - not-canonical-truth
  - source-role
  - correction-path
  - rollback-path
  - cite-or-abstain
notes:
  - "This README replaces a greenfield stub at `data/triplets/README.md`."
  - "Directory Rules lists `data/triplets/` with `graph_deltas/` and `exports/` as part of the data lifecycle tree."
  - "Directory Rules states triplets are relationship projections and graph-compatible triples and must not carry canonical replacement semantics."
  - "The paired catalog lane is `data/catalog/`; catalog records and triplets are paired projections of the CATALOG / TRIPLET lifecycle stage."
  - "The literal `data/triplet(s)/` path exists separately and is treated as compatibility only, not a canonical lane."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Triplets Data

Parent lane for KFM graph-compatible relationship projections at the `CATALOG / TRIPLET` lifecycle stage.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: data" src="https://img.shields.io/badge/root-data%2F-0a7ea4">
  <img alt="Lifecycle: catalog triplet" src="https://img.shields.io/badge/lifecycle-CATALOG%20%2F%20TRIPLET-purple">
  <img alt="Boundary: projection not truth" src="https://img.shields.io/badge/boundary-projection%20not%20truth-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Triplet guardrails](#triplet-guardrails) · [Suggested directory shape](#suggested-directory-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!CAUTION]
> `data/triplets/` is not canonical domain truth, not source authority, not processed data, not proof, not catalog closure, not release authority, not policy authority, not schema authority, not public API/UI source, and not a substitute for EvidenceBundle support. Triplets are graph-compatible projections that must remain traceable to source records, canonical identifiers, catalog records, proof support, policy posture, and release state.

---

## Scope

`data/triplets/` materializes the `TRIPLET` side of KFM's `CATALOG / TRIPLET` lifecycle stage.

Use this lane for governed relationship projections such as:

- graph-compatible triples derived from processed and cataloged objects;
- relationship deltas created by governed graph-build or catalog-build runs;
- domain or cross-domain graph exports prepared for review, proof, release, or downstream publication;
- indexes that help reviewers inspect relationship projection coverage;
- release-linked triplet export manifests and digest sidecars;
- graph projection summaries that point to evidence, proof, catalog, receipts, policy, and release records.

A triplet can help a graph, search surface, story engine, Evidence Drawer, Focus Mode, or governed API traverse relationships. It does **not** make the relationship true by placement.

---

## Path posture

The canonical lane is:

```text
data/triplets/
```

Current evidence supports this placement:

- `data/README.md` lists `triplets` as a lifecycle data family under `data/`.
- Directory Rules lists `data/triplets/` with child concepts `graph_deltas/` and `exports/`.
- Directory Rules summarizes `triplets/` as relationship projections and graph-compatible triples that must not carry canonical replacement semantics.
- `data/catalog/README.md` identifies `data/triplets/` as the paired graph projection lane for the `CATALOG / TRIPLET` lifecycle stage.
- `data/triplet(s)/README.md` also exists, but that literal parentheses path is compatibility-only and should not receive payloads.

Therefore this README treats `data/triplets/` as **CONFIRMED path presence / DRAFT lifecycle parent contract / NEEDS VERIFICATION implementation maturity**.

---

## Repo fit

| Responsibility | Correct home | Boundary |
|---|---|---|
| Graph-compatible relationship projections | `data/triplets/` | This lane. Projection only, not canonical truth. |
| Catalog records | `data/catalog/` | Paired lifecycle projection; catalog is discovery and provenance, not graph edge storage. |
| Processed canonical candidates | `data/processed/` | Upstream normalized objects; triplets do not replace them. |
| Evidence and proof support | `data/proofs/` | EvidenceBundle, ProofPack, validation, and citation support. |
| Process memory | `data/receipts/` | Graph-build, catalog-build, transform, validation, AI, correction, and rollback receipts. |
| Released public-safe graph exports | `data/published/` after release | Public delivery only after release gates. |
| Release decisions | `release/` | ReleaseManifest, PromotionDecision, RollbackCard, CorrectionNotice, WithdrawalNotice, signatures. |
| Source admission | `data/registry/` | Sources, datasets, rights, sensitivity, and crosswalk records. |
| Contracts, schemas, policy | `contracts/`, `schemas/`, `policy/` | Meaning, machine shape, and allow/deny/restrict/abstain logic. |

---

## Accepted material

Accepted material is limited to governed graph-compatible relationship projections and their immediate inspection sidecars:

- graph deltas that add, change, supersede, withhold, or invalidate relationship projections;
- export bundles intended for graph projection consumers after review;
- relationship indexes grouped by domain, release, graph build, catalog build, or claim family;
- digest sidecars for triplet export bytes;
- evidence, proof, catalog, receipt, policy, review, release, correction, and rollback references;
- README files that explain a child lane, graph export, or projection boundary.

Every triplet-like record should preserve enough context to inspect:

- subject, predicate, object, and identifier scheme;
- domain and source role;
- evidence reference or abstention reason where the relationship is claim-bearing;
- catalog record reference where applicable;
- proof and validation references where applicable;
- sensitivity and rights posture;
- release/correction/rollback state;
- build receipt or provenance record.

---

## Exclusions

| Do not place here | Correct home |
|---|---|
| RAW source captures, downloads, scans, logs, or source-system dumps | `data/raw/`, `data/work/`, or `data/quarantine/` |
| Work scratch, unresolved graph joins, unreviewed entity matching, or experimental relationship extraction | `data/work/` or `data/quarantine/` |
| Canonical processed domain objects | `data/processed/` |
| STAC, DCAT, PROV, or domain catalog records | `data/catalog/` |
| EvidenceBundle, ProofPack, citation validation, integrity proof, or release proof | `data/proofs/` |
| Process receipts, graph-build receipts, validation receipts, AI receipts, or release-support receipts | `data/receipts/` |
| Published public-safe graph exports, API payloads, stories, reports, layers, or tiles | `data/published/` after release gates |
| Source descriptors, source registry records, rights records, sensitivity records, or crosswalk authority | `data/registry/` |
| Release manifests, promotion decisions, correction notices, withdrawal notices, rollback cards, or signatures | `release/` |
| Contracts, schemas, policy rules, tests, validators, implementation code, or UI code | `contracts/`, `schemas/`, `policy/`, `tests/`, `tools/`, `apps/`, `packages/` |
| Literal compatibility path content | `data/triplet(s)/` should stay marker-only and point here |

---

## Triplet guardrails

| Risk | Guardrail |
|---|---|
| Projection becomes truth | Treat every triplet as a derived graph projection unless proof and release state say otherwise. |
| Canonical replacement semantics | Do not let triplets replace processed domain records, source records, catalog records, or EvidenceBundles. |
| Evidence collapse | Claim-bearing relationships must point to EvidenceBundle/proof support or carry an abstention/withholding posture. |
| Source-role collapse | Observed, inferred, modeled, administrative, generated, historical, candidate, and AI-derived relationships must stay distinguishable. |
| Entity resolution overclaim | Identity links, same-as links, kinship links, route membership, parcel/person links, species/habitat links, facility/dependency links, and archaeology/cultural links require owning-domain review. |
| Sensitive join leakage | A relationship can reveal restricted data even when each node looks safe. Apply the strictest relevant policy. |
| Public path bypass | Public clients must not read this lane directly; public graph surfaces must go through release-resolved artifacts or governed APIs. |
| AI surface drift | Generated answers must not cite triplets as root evidence without resolving EvidenceRef/proof and release state. |
| Stale graph state | Corrections, withdrawals, rollbacks, and supersessions must invalidate graph exports, search surfaces, Evidence Drawer content, Focus Mode answers, and AI summaries. |

---

## Suggested directory shape

This layout follows Directory Rules and remains **PROPOSED** until concrete schemas, validators, and graph-build receipts prove implementation maturity.

```text
data/triplets/
├── README.md
├── graph_deltas/
│   └── README.md
├── exports/
│   └── README.md
├── domain/
│   └── <domain>/
│       └── README.md
├── indexes/
│   └── README.md
└── release_refs/
    └── README.md
```

Recommended record-level support fields:

| Field | Purpose |
|---|---|
| `triplet_id` | Stable projection identifier. |
| `subject_ref` | Governed subject identifier and namespace. |
| `predicate_ref` | Relationship predicate and contract/schema reference where available. |
| `object_ref` | Governed object identifier and namespace. |
| `domain` | Owning or primary domain. |
| `source_role` | Observed, inferred, modeled, administrative, generated, historical, candidate, or other governed source role. |
| `evidence_refs` | EvidenceBundle/proof references or explicit abstention/withholding reason. |
| `catalog_refs` | Catalog records tied to the relationship projection. |
| `receipt_refs` | Graph-build, transform, validation, policy, AI, correction, or rollback receipts. |
| `policy_state` | Allow, restrict, deny, abstain, hold, or review posture. |
| `release_state` | Unreleased, candidate, published, superseded, withdrawn, stale, or rollback-affected state. |

---

## Required checks before use

- [ ] Confirm concrete child directories under `data/triplets/`.
- [ ] Confirm triplet/graph schemas and contracts.
- [ ] Confirm graph-build receipt shape and storage home.
- [ ] Confirm validation rules for subject, predicate, object, namespace, source role, evidence refs, policy state, and release state.
- [ ] Confirm sensitivity checks for relationship joins that reveal restricted locations, living-person data, DNA/genomic context, archaeology, rare species, infrastructure, property, or cultural knowledge.
- [ ] Confirm catalog and proof closure requirements for claim-bearing triplets.
- [ ] Confirm release linkage for public graph exports.
- [ ] Confirm correction, withdrawal, stale-state, and rollback invalidation behavior.
- [ ] Confirm public clients resolve graph projections through governed APIs or released artifacts, not direct reads from `data/triplets/`.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target path presence | CONFIRMED | `data/triplets/README.md` existed as a greenfield stub before this update. |
| Data root | CONFIRMED README | `data/README.md` lists `triplets` as a lifecycle data family. |
| Directory Rules triplets lane | CONFIRMED doctrine | Directory Rules lists `data/triplets/` with `graph_deltas/` and `exports/`. |
| Lifecycle role | CONFIRMED doctrine | Directory Rules places triplets in `CATALOG / TRIPLET` and says they are relationship projections, not canonical replacements. |
| Catalog pairing | CONFIRMED README | `data/catalog/README.md` identifies `data/triplets/` as the paired graph projection lane. |
| Literal `data/triplet(s)/` path | CONFIRMED compatibility | The literal parentheses path exists and should remain a compatibility marker only. |
| Actual triplet payload inventory | UNKNOWN | This README does not prove any triplet payloads exist. |
| Schemas, contracts, validators, graph-build receipts, CI, release linkage | NEEDS VERIFICATION | No runtime enforcement was proven by this edit. |
| Public release readiness | DENY until proven | A triplets README cannot publish graph exports or make relationships true by itself. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `data/triplets/README.md` existed as a greenfield stub. | Did not define lane boundaries. |
| [`../README.md`](../README.md) | CONFIRMED README | `data/` owns lifecycle data and lists `triplets`. | Data root README is short and status `PROPOSED`. |
| [`../../docs/doctrine/directory-rules.md`](../../docs/doctrine/directory-rules.md) | CONFIRMED doctrine | `data/triplets/`, `graph_deltas/`, `exports/`, lifecycle invariant, and no canonical replacement semantics. | Exact implementation inventory remains unverified. |
| [`../catalog/README.md`](../catalog/README.md) | CONFIRMED README | Catalog and triplets are paired projections of the `CATALOG / TRIPLET` stage. | Catalog README does not prove triplet payloads exist. |
| [`../proofs/README.md`](../proofs/README.md) | CONFIRMED README | Proof lanes support evidence, validation, citation, release, correction, and rollback inspection. | Proof files are not triplet storage. |
| [`../receipts/README.md`](../receipts/README.md) | CONFIRMED README | Receipts are process memory and can support graph/correction/rollback actions. | Receipts are not proof or release authority. |
| [`../published/README.md`](../published/README.md) | CONFIRMED README | Published artifacts are downstream release-approved carriers and exclude catalog/triplet truth. | Published README does not prove graph exports exist. |
| [`../../release/README.md`](../../release/README.md) | CONFIRMED README | Release decisions live in `release/`, not `data/triplets/`. | Release root README is short and status `PROPOSED`. |

[Back to top](#top)

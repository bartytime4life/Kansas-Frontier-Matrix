<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/source-descriptors/readme
name: Source Descriptors Compatibility README
path: data/registry/source_descriptors/README.md
type: data-registry-source-descriptors-compatibility-readme
version: v0.2.0
status: draft
owners:
  - <registry-steward>
  - <source-steward>
  - <schema-steward>
  - <policy-steward>
  - <rights-steward>
  - <sensitivity-steward>
  - <proof-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: registry
registry_scope: source-descriptor-compatibility-and-routing
path_posture: existing-stub-replaced; requested-source-descriptors-path-confirmed; canonical-source-registry-parent-confirmed-at-data-registry-sources; source-descriptor-schema-home-has-singular-plural-variance-in-repo-docs; final-topology-needs-verification
sensitivity_posture: registry-internal; no-public-path; source-role-preserving; rights-and-sensitivity-fail-closed; evidence-aware; policy-aware; release-blocked-until-gates-close
related:
  - ../README.md
  - ../sources/README.md
  - ../sources/
  - ../datasets/README.md
  - ../domains/README.md
  - ../crosswalks/README.md
  - ../rights/README.md
  - ../sensitivity/README.md
  - ../layers/README.md
  - ../../raw/
  - ../../work/
  - ../../quarantine/
  - ../../processed/
  - ../../catalog/
  - ../../triplets/
  - ../../published/
  - ../../receipts/
  - ../../proofs/
  - ../../../contracts/
  - ../../../schemas/contracts/v1/
  - ../../../policy/
  - ../../../release/
  - ../../../docs/sources/catalog/
  - ../../../docs/architecture/directory-rules.md
  - ../../../docs/doctrine/directory-rules.md
tags:
  - kfm
  - data
  - registry
  - source-descriptors
  - sources
  - compatibility-lane
  - source-registry
  - SourceDescriptor
  - source-role
  - rights
  - sensitivity
  - evidence
  - provenance
  - release-gated
  - rollback
  - no-public-path
notes:
  - "This README replaces the greenfield stub at `data/registry/source_descriptors/README.md`."
  - "The canonical source registry parent verified in this session is `data/registry/sources/README.md`; this `source_descriptors/` lane is treated as a compatibility/routing lane unless an ADR, Directory Rules update, or migration note accepts it as canonical."
  - "Do not maintain duplicate SourceDescriptor instances under both `data/registry/sources/` and `data/registry/source_descriptors/`."
  - "SourceDescriptor records are admission and authority-control records. They do not store source payloads, define schemas, decide policy, emit receipts, prove claims, close catalogs, publish artifacts, or grant public access."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Source Descriptors Compatibility Lane

Compatibility README for the requested `data/registry/source_descriptors/` path.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: registry" src="https://img.shields.io/badge/family-registry-blueviolet">
  <img alt="Lane: source descriptors" src="https://img.shields.io/badge/lane-source__descriptors-blue">
  <img alt="Topology: needs verification" src="https://img.shields.io/badge/topology-NEEDS%20VERIFICATION-orange">
  <img alt="Boundary: not source data" src="https://img.shields.io/badge/boundary-not%20source%20data-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Compatibility boundary](#compatibility-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Suggested directory shape](#suggested-directory-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/source_descriptors/` is treated here as a compatibility/routing lane. The confirmed source-registry parent is `data/registry/sources/`. Do not place duplicate authoritative SourceDescriptor records here unless an ADR, Directory Rules update, migration note, or accepted registry contract explicitly makes this path canonical.

---

## Scope

This directory documents the requested `source_descriptors` path and protects it from becoming a parallel source-registry authority.

A SourceDescriptor-style record describes how a source may be treated before its material enters the KFM lifecycle. It can carry or point to source identity, source role, rights posture, sensitivity posture, cadence, steward, authority scope, attribution requirements, retrieval windows, public-release class, and supersession/correction state.

The source registry is an admission and authority-control surface. It can block or permit source admission under governed conditions, but it does not by itself prove claims, publish data, close evidence, approve policy, or make a public surface safe.

---

## Path posture

The requested lane exists as:

```text
data/registry/source_descriptors/
```

The verified canonical source-registry parent is:

```text
data/registry/sources/
```

The source-registry parent says `data/registry/sources/` records how each admitted source may be treated and identifies it as the pre-RAW admission membrane. It also permits per-domain subfolders such as:

```text
data/registry/sources/<domain>/
```

Therefore, this README treats `data/registry/source_descriptors/` as **CONFIRMED path presence / NEEDS VERIFICATION topology**. Until topology is reconciled, this lane should hold only README/routing notes, migration notes, redirect notes, or local compatibility indexes that point to the canonical source-registry lane.

Do not split active descriptor sets across both shapes:

```text
# Preferred unless superseded by ADR/migration decision
data/registry/sources/<domain>/

# Compatibility/routing only unless accepted as canonical
data/registry/source_descriptors/
```

---

## Repo fit

| Responsibility | Home | Boundary |
|---|---|---|
| Canonical source registry parent | `data/registry/sources/README.md` | Source admission and authority-control surface. |
| Requested compatibility lane | `data/registry/source_descriptors/README.md` | Routing note, redirect note, migration note, or topology warning only unless accepted as canonical. |
| Registry root | `data/registry/README.md` | Registry-family routing and governance boundaries. |
| Source payloads | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/` | Actual source and processed data; not descriptor records. |
| Source catalog documentation | `docs/sources/catalog/` | Human-facing source/product explanation; not authoritative descriptor instances. |
| Semantic contracts | `contracts/` | Object meaning and invariants. |
| Machine schemas | `schemas/contracts/v1/` or accepted schema root | Machine-checkable shape; exact SourceDescriptor schema home remains NEEDS VERIFICATION where repo docs use singular/plural variants. |
| Policy | `policy/` | Allow/deny/restrict/abstain, sensitivity, rights, runtime, and release decisions. |
| Receipts | `data/receipts/` | Activation, validation, review, transform, and run process memory. |
| Proof/evidence | `data/proofs/` or accepted proof lanes | EvidenceBundle closure, proof packs, signatures, and citation validation. |
| Catalog and graph projections | `data/catalog/` and `data/triplets/` | Catalog/discovery carriers and graph/triplet projections after closure. |
| Release authority | `release/` | ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal, and supersession authority. |
| Public surfaces | governed APIs and released artifacts only | Public clients do not read this compatibility lane directly. |

---

## Compatibility boundary

| Rule | Handling |
|---|---|
| Canonical source registry wins | Use `data/registry/sources/` unless a governed topology decision says otherwise. |
| No duplicate authority | Do not maintain descriptor instances in both `sources/` and `source_descriptors/`. |
| Compatibility is pointer-only | This lane may point to canonical descriptors, migration manifests, and topology decisions. |
| SourceDescriptor is admission control | It governs how a source may be admitted and used; it is not the source payload. |
| Source role is preserved | Processing, extraction, summarization, map rendering, graph projection, or AI explanation must not upgrade source role. |
| Rights and sensitivity travel | Rights, attribution, redistribution, endpoint terms, sensitivity, access posture, and steward caveats remain attached downstream. |
| Registry is not schema | SourceDescriptor schemas live in the accepted schema root, not here. |
| Registry is not policy | Policy decisions live under `policy/`; descriptors provide facts and refs for policy to evaluate. |
| Registry is not receipt | SourceActivationDecision and process receipts belong with accepted receipt lanes. |
| Registry is not proof | EvidenceBundle/proof support remains separate. |
| Registry is not catalog | Catalog/triplet closure remains separate. |
| Registry is not release | Public exposure requires validation, policy, review, proof/catalog support, release, correction, and rollback. |
| Public clients do not read this lane | Public UI/API surfaces consume governed APIs, released artifacts, catalog/triplet/proof-backed responses, and policy-safe envelopes. |

---

## Accepted material

Accepted content here is limited to compatibility and routing support:

- this README;
- redirect notes pointing to `data/registry/sources/`;
- migration notes if descriptor files are moved into or out of this path;
- topology decision notes that cite an ADR, Directory Rules update, or registry migration plan;
- local indexes that point to canonical SourceDescriptor records without duplicating their fields;
- rollback notes for any future path migration.

Do not place active SourceDescriptor payloads here unless governance explicitly accepts this path as canonical.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw or transformed source data | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/` |
| Canonical SourceDescriptor instances while `data/registry/sources/` remains canonical | `data/registry/sources/` and per-domain child lanes |
| SourceDescriptor schemas | `schemas/contracts/v1/` or accepted schema root |
| Source catalog prose | `docs/sources/catalog/` |
| Connector or watcher code | `connectors/`, `pipelines/`, `tools/`, `packages/`, or accepted implementation roots |
| Policy decisions or runtime allow/deny logic | `policy/` |
| SourceActivationDecision receipts, validation receipts, review receipts, or run receipts | `data/receipts/` |
| EvidenceBundle records or proof packs | `data/proofs/` or accepted proof lanes |
| Catalog/triplet records | `data/catalog/` and `data/triplets/` |
| Release manifests, correction notices, rollback cards, withdrawal, or supersession notices | `release/` |
| Secrets, credentials, API keys, tokens, or restricted source details | never in registry; use approved restricted storage and secret management |

---

## Suggested directory shape

The safest shape until topology is reconciled is:

```text
data/registry/source_descriptors/
└── README.md
```

A possible migration-only shape, if needed later, is:

```text
data/registry/source_descriptors/
├── README.md
├── MIGRATION.md          # PROPOSED only
└── index.local.json      # PROPOSED pointer index only; not canonical descriptor storage
```

Do not add descriptor payload subfolders here without an accepted topology decision.

---

## Required checks before use

- [ ] Confirm whether this path is compatibility-only, migration-only, or canonical before adding anything beyond README/routing material.
- [ ] Confirm canonical SourceDescriptor records are not duplicated between `data/registry/sources/` and `data/registry/source_descriptors/`.
- [ ] Confirm any pointer index here resolves to canonical source-registry records.
- [ ] Confirm schema-home singular/plural drift is resolved before naming a final schema path as authoritative.
- [ ] Confirm SourceDescriptor state does not override rights, sensitivity, policy, validation, proof, catalog, release, correction, or rollback state.
- [ ] Confirm no public client, map layer, graph edge, vector index, generated answer, report, or dashboard reads this compatibility lane as direct public truth.

---

## Status notes

| Claim | Status |
|---|---:|
| This README replaces the greenfield stub at `data/registry/source_descriptors/README.md`. | CONFIRMED authored |
| The requested path existed in the live repository as a greenfield stub before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/README.md` exists and describes registry records as governance/control records, not source payloads, schemas, policy, receipts, proofs, catalogs, or release authority. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/sources/README.md` exists and identifies `data/registry/sources/` as the source admission and authority-control surface. | CONFIRMED by GitHub contents API during this edit |
| Current search returned `data/registry/sources/README.md` as the relevant source-descriptor registry result. | CONFIRMED by GitHub search during this edit |
| Active SourceDescriptor payloads exist under `data/registry/source_descriptors/`. | UNKNOWN |
| This path is accepted as canonical instead of `data/registry/sources/`. | NEEDS VERIFICATION |
| Final SourceDescriptor schema home is fully reconciled. | NEEDS VERIFICATION |
| CI validates files in this compatibility lane. | UNKNOWN |
| Runtime registry resolution or governed API behavior reads this lane. | UNKNOWN |
| This README grants public access to source descriptor internals. | DENY |

---

## Maintainer note

This path exists, so it needs a boundary. Keep the safe chain explicit:

```text
compatibility pointer -> canonical SourceDescriptor -> rights/sensitivity gate -> RAW admission -> lifecycle processing -> receipts -> EvidenceBundle/proof -> catalog/triplet -> release -> governed public surface
```

Never collapse it into:

```text
source_descriptors/ -> public truth
```

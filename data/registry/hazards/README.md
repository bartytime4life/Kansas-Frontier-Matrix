<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/hazards/readme
name: Hazards Registry README
path: data/registry/hazards/README.md
type: data-registry-hazards-parent-readme
version: v0.2.0
status: draft
owners:
  - <registry-steward>
  - <hazards-domain-steward>
  - <source-steward>
  - <dataset-steward>
  - <crosswalk-steward>
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
registry_scope: hazards-domain-first-registry-parent
domain: hazards
path_posture: existing-parent-stub-replaced; sources-child-lane-confirmed; domain-first-registry-path-exists; canonical-subtype-first-topology-needs-verification
sensitivity_posture: registry-internal; no-public-path; not-an-alert-system; freshness-bound; source-role-preserving; evidence-aware; rights-aware; policy-aware; release-blocked-until-gates-close
related:
  - ../README.md
  - ../sources/README.md
  - ../sources/hazards/
  - ../datasets/README.md
  - ../domains/README.md
  - ../crosswalks/README.md
  - sources/README.md
  - ../../raw/hazards/README.md
  - ../../work/hazards/
  - ../../quarantine/hazards/
  - ../../processed/hazards/
  - ../../catalog/domain/hazards/
  - ../../receipts/
  - ../../proofs/
  - ../../../docs/domains/hazards/SOURCE_REGISTRY.md
  - ../../../docs/domains/hazards/SOURCES.md
  - ../../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md
  - ../../../docs/domains/hazards/DATA_LIFECYCLE.md
  - ../../../docs/domains/hazards/CONTINUITY_INVENTORY.md
  - ../../../contracts/domains/hazards/
  - ../../../schemas/contracts/v1/source/
  - ../../../schemas/contracts/v1/hazards/
  - ../../../policy/domains/hazards/
  - ../../../policy/sensitivity/
  - ../../../release/
tags:
  - kfm
  - data
  - registry
  - hazards
  - domain-first-registry
  - sources
  - source-descriptor
  - source-role
  - rights
  - sensitivity
  - freshness
  - operational-context
  - regulatory-context
  - remote-sensing
  - modeled-hazard
  - administrative
  - not-an-alert-system
  - evidence
  - provenance
  - release-gated
  - no-public-path
notes:
  - "This README replaces the greenfield stub at `data/registry/hazards/README.md`."
  - "This domain-first registry parent exists in the repository and currently has a confirmed `sources/` child README."
  - "The inspected Hazards source-registry doctrine names `data/registry/sources/hazards/` as the machine-readable source registry lane. Therefore this parent is treated as a compatibility/routing lane until registry topology is reconciled."
  - "Hazards remains not an alert system; time-bound source context must preserve freshness posture, stale-state handling, and release blockers."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hazards Registry

Domain-first registry parent for Hazards registry lanes.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: registry" src="https://img.shields.io/badge/family-registry-blueviolet">
  <img alt="Domain: hazards" src="https://img.shields.io/badge/domain-hazards-c62828">
  <img alt="Topology: needs verification" src="https://img.shields.io/badge/topology-NEEDS%20VERIFICATION-orange">
  <img alt="Boundary: not an alert system" src="https://img.shields.io/badge/boundary-not%20an%20alert%20system-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Confirmed child lanes](#confirmed-child-lanes) · [Hazards registry boundary](#hazards-registry-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Suggested directory shape](#suggested-directory-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/hazards/` is a domain-first registry parent. It is not RAW source storage, WORK staging, QUARANTINE, PROCESSED data, catalog output, proof storage, receipt storage, semantic contract authority, schema authority, policy, release authority, public API/UI material, current operational guidance, or generated-answer authority.

---

## Scope

`data/registry/hazards/` is a domain-first routing lane for Hazards registry material that already exists in the repository. Its current confirmed child is `sources/`, which documents source descriptor and source-admission records for the Hazards lane.

This parent README exists to prevent the domain-first path from becoming an unbounded parallel authority. It should route maintainers to the correct registry family and preserve the distinction between registry state and other KFM authority roots.

A Hazards registry lane may point to or summarize governance state for:

- Hazards source descriptors and source-admission records;
- source-role assignments and source-family posture;
- rights, sensitivity, cadence, source-head, activation, intake, correction, supersession, stale-state, and freshness state;
- regulatory-context, time-bound-context, remote-sensing, modeled-risk, administrative, historical-observation, and candidate-material blockers;
- links to lifecycle payloads under RAW, WORK, QUARANTINE, PROCESSED, CATALOG/TRIPLET, and PUBLISHED phases;
- links to contracts, schemas, policies, receipts, proofs, catalog records, release candidates, correction notices, and rollback cards.

It must not contain source payloads, current operational guidance, proof packs, catalog records, release manifests, public map artifacts, or generated-answer carriers.

---

## Path posture

The requested and existing parent lane is:

```text
data/registry/hazards/
```

This is a **domain-first** registry path. Current Hazards source-registry evidence also supports a **subtype-first** source registry pattern:

```text
data/registry/sources/hazards/
```

Other registry parents in this sequence use subtype-first lanes such as:

```text
data/registry/domains/
data/registry/datasets/
data/registry/crosswalks/
```

Therefore, `data/registry/hazards/` is treated as **CONFIRMED path presence / NEEDS VERIFICATION topology**. Until an ADR, Directory Rules update, registry README, migration note, or repository-wide inventory resolves the topology, do not create duplicate authoritative records in both domain-first and subtype-first locations.

---

## Repo fit

| Responsibility | Home | Boundary |
|---|---|---|
| Hazards domain-first registry parent | `data/registry/hazards/` | Routing/compatibility parent for existing domain-first registry lanes. |
| Confirmed Hazards child registry lane | `data/registry/hazards/sources/` | Source descriptor/admission records, with topology warning. |
| Cross-domain source registry parent | `data/registry/sources/README.md` | General source registry doctrine and subtype-first source registry pattern. |
| Potential canonical Hazards source lane | `data/registry/sources/hazards/` | Named by Hazards source-registry doctrine as machine-readable registry lane; needs topology reconciliation with this path. |
| Dataset registry records | `data/registry/datasets/` | Dataset identity and dataset-state records. |
| Domain registry records | `data/registry/domains/` | Domain-state records; do not duplicate here without topology decision. |
| Crosswalk registry records | `data/registry/crosswalks/` | Mapping state across source IDs, authority IDs, fields, classifications, and vocabularies. |
| Hazards source payloads | `data/raw/hazards/`, `data/work/hazards/`, `data/quarantine/hazards/`, `data/processed/hazards/` | Actual data belongs in lifecycle lanes, not registry parent files. |
| Hazards semantic meaning | `contracts/domains/hazards/` | Object-family meaning and invariants. |
| Hazards machine shape | `schemas/contracts/v1/source/`, `schemas/contracts/v1/hazards/`, or ADR-selected schema lane | Schema enforcement; path form remains NEEDS VERIFICATION until ADR/repo evidence resolves it. |
| Hazards policy and sensitivity | `policy/domains/hazards/`, `policy/sensitivity/`, `policy/rights/` | Exposure, rights, source-role, sensitivity, freshness, and admissibility rules. |
| Hazards validation receipts | `data/receipts/validation/hazards/` if/when accepted | Process memory for validation checks. |
| Hazards proof/evidence | `data/proofs/` or accepted proof lanes | EvidenceBundle closure, proof packs, signatures, and citation validation. |
| Hazards catalog projections | `data/catalog/domain/hazards/`, STAC/DCAT/PROV lanes, and triplet lanes | Catalog/discovery carriers after catalog closure. |
| Hazards release decisions | `release/` | Promotion, correction, rollback, supersession, withdrawal, and release manifests. |
| Public surfaces | governed APIs and released artifacts only | Public clients do not read this registry parent directly. |

---

## Confirmed child lanes

This confirms only path/README evidence. It does not prove emitted records, schemas, validators, fixtures, CI enforcement, signing, release integration, correction hooks, rollback hooks, governed API behavior, or public-safe summaries.

| Child lane | Status | Purpose | Boundary |
|---|---:|---|---|
| [`sources/`](sources/README.md) | CONFIRMED README | Domain-first Hazards source descriptor and source-admission registry lane. | Not source payload storage, Hazards truth, proof, receipt storage, catalog closure, semantic contract authority, policy, release authority, current-guidance authority, or public output. |

---

## Hazards registry boundary

| Rule | Handling |
|---|---|
| Registry parent is routing state | This parent orients to child registry lanes; it does not contain domain payloads. |
| Topology is unresolved | Do not silently duplicate records between `data/registry/hazards/...` and subtype-first lanes such as `data/registry/sources/hazards/`. |
| Not an alert system | Hazards registry state must not become current operational guidance or alert authority. |
| Source role is preserved | Hazards registry state must not upgrade observed, regulatory, modeled, aggregate, administrative, candidate, synthetic, context, or restricted source roles. |
| Time-bound context expires | Time-bound source material must preserve source time, retrieval time, freshness posture, stale-state handling, and public-use blockers. |
| Detection is not confirmation | Remote-sensing detections, reports, and candidates require disposition and evidence review before being treated as confirmed event claims. |
| Regulatory and administrative records stay scoped | Regulatory context and administrative actions must not be reframed as observed event truth without separate evidence. |
| Models are not observations | Risk, exposure, scenario, susceptibility, or modeled hazard surfaces require model identity, run receipts, uncertainty, and source-role preservation. |
| Registry is not validation | Validation receipts and run receipts remain separate process-memory objects. |
| Registry is not proof | EvidenceBundle/proof support remains separate. |
| Registry is not catalog | STAC/DCAT/PROV/domain catalog records and graph projections live under catalog/triplet lanes. |
| Registry is not release | Public exposure requires validation, policy, review, proof/catalog support, release manifest, correction path, and rollback path. |
| Public clients do not read this lane | Public UI/API surfaces consume governed APIs, released artifacts, catalog/triplet/proof-backed responses, and policy-safe envelopes. |

---

## Accepted material

Accepted content is limited to README/routing material and registry-local sidecars that do not duplicate authority from subtype-first lanes:

- parent README and routing notes;
- compatibility notes explaining the domain-first versus subtype-first topology;
- migration notes, redirect notes, rollback notes, or topology decision notes;
- local indexes that point to child registry lanes without becoming authoritative records themselves;
- checksums, manifests, and signatures for registry routing material where applicable;
- pointers to source descriptors, dataset registry records, crosswalk registry records, domain registry records, contracts, schemas, policy refs, lifecycle payloads, validation receipts, proof refs, catalog refs, release candidates, correction notices, supersession notices, withdrawal notices, stale-state notices, and rollback cards.

If a child lane under this parent stores actual registry records, it must state whether it is canonical, compatibility, migration-only, or mirrored, and it must name its conflict/rollback path.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw Hazards source payloads, regulatory packages, remote-sensing detection packages, administrative extracts, time-bound feed captures, modeled risk surfaces, rasters, shapefiles, GeoParquet, COG, PMTiles, or source-native tables | `data/raw/hazards/`, `data/work/hazards/`, `data/quarantine/hazards/`, or `data/processed/hazards/` depending on lifecycle state |
| Current public guidance, official-source substitution, private identifiers, access secrets, or restricted review material | denied, restricted, quarantined, or routed to governed restricted storage |
| Human-facing bibliography or source narrative | `docs/domains/hazards/`, `docs/sources/`, or source catalog docs |
| Canonical source descriptor records if `data/registry/sources/hazards/` is accepted as canonical | `data/registry/sources/hazards/` after topology reconciliation |
| Dataset identity records | `data/registry/datasets/` |
| Crosswalk mapping records | `data/registry/crosswalks/` |
| Domain-state records | `data/registry/domains/` |
| Semantic object contracts | `contracts/domains/hazards/` |
| JSON Schema | `schemas/contracts/v1/source/`, `schemas/contracts/v1/hazards/`, or ADR-selected schema lane |
| Policy rules, sensitivity rules, rights rules, access-control logic, or release rules | `policy/` |
| Validation receipts, run receipts, redaction receipts, policy receipts, review receipts, or process-memory logs | `data/receipts/` |
| EvidenceBundle records, proof packs, signatures, or citation-validation closure | `data/proofs/` |
| STAC/DCAT/PROV/domain catalog records or graph/triplet projections | `data/catalog/` and `data/triplets/` |
| Published Hazards layers, reports, dashboards, tiles, API payloads, or generated-answer carriers | `data/published/`, governed app/API roots, and release-approved public artifact lanes |
| ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal notice, or supersession notice | `release/` |
| Validator code, connector code, pipelines, fixtures, tests, or CI workflows | `tools/`, `connectors/`, `pipelines/`, `fixtures/`, `tests/`, `.github/workflows/` |

---

## Suggested directory shape

The map below is **PROPOSED** documentation guidance, not proof that child folders or records exist beyond confirmed README evidence.

```text
data/registry/hazards/
├── README.md
├── sources/
│   └── README.md
└── index.local.json
```

If subtype-first lanes are accepted as canonical, prefer a migration such as:

```text
data/registry/sources/hazards/       # canonical source descriptors
data/registry/hazards/README.md      # compatibility pointer / migration note only
```

Do not maintain two divergent descriptor sets.

---

## Required checks before use

- [ ] Confirm whether `data/registry/hazards/...` or subtype-first lanes such as `data/registry/sources/hazards/` are canonical before adding real registry payloads.
- [ ] Confirm a child object is a registry record, not source data, proof, receipt, catalog record, release decision, policy, schema, validator, fixture, or test.
- [ ] Confirm source identity, source role, rights posture, terms, cadence, source head, source time, retrieval time, freshness posture, stale-state behavior, and authority limits are preserved for any source-registry child records.
- [ ] Confirm registry state does not upgrade source role, evidence strength, review state, catalog state, release state, or public-safe posture.
- [ ] Confirm regulatory context, time-bound context, remote-sensing detection, modeled risk, administrative action, historical observation, and candidate material are not collapsed.
- [ ] Confirm Hazards is not presented as an alerting or current-guidance surface.
- [ ] Confirm restricted or operationally risky details are not exposed in registry files, local indexes, or public summaries.
- [ ] Confirm validation receipts exist before catalog or release eligibility is asserted.
- [ ] Confirm EvidenceRef/EvidenceBundle and proof refs exist for consequential use.
- [ ] Confirm catalog refs point to STAC/DCAT/PROV/domain catalog records rather than embedding them.
- [ ] Confirm release refs point to ReleaseManifest/PromotionDecision objects rather than implying publication from registry state.
- [ ] Confirm correction, supersession, withdrawal, stale-state, and rollback paths exist for mutable or time-bound Hazards source material.
- [ ] Confirm no public client, map layer, graph edge, vector index, generated answer, report, or dashboard reads this registry parent as direct public truth.

---

## Status notes

| Claim | Status |
|---|---:|
| This README replaces the greenfield stub at `data/registry/hazards/README.md`. | CONFIRMED authored |
| The target path existed in the live repository as a greenfield stub before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/hazards/sources/README.md` exists as a confirmed child lane. | CONFIRMED by GitHub contents API during this edit |
| The Hazards child `sources/` README marks the domain-first path as confirmed but layout-NEEDS VERIFICATION against `data/registry/sources/hazards/`. | CONFIRMED by GitHub contents API during this edit |
| Hazards source-registry doctrine names `data/registry/sources/hazards/` as the machine-readable registry lane. | CONFIRMED by GitHub contents API in this sequence |
| Hazards continuity inventory states Hazards is not an alert system and frames Hazards as historical, regulatory, modeled, and time-bound context information. | CONFIRMED by GitHub contents API in this sequence |
| Hazards RAW README keeps RAW source capture separate from registry, proof, receipt, policy, release, public, and alert authority. | CONFIRMED by GitHub contents API in this sequence |
| Concrete Hazards registry payloads exist under this parent lane. | UNKNOWN |
| The final accepted topology between domain-first and subtype-first registry lanes is resolved. | NEEDS VERIFICATION |
| CI validates Hazards registry records. | UNKNOWN |
| This README grants public access to Hazards registry internals. | DENY |

---

## Maintainer note

This parent exists because the repository already has a domain-first Hazards registry lane. Keep it useful but constrained. The safe chain is:

```text
registry pointer -> canonical registry record -> lifecycle payload -> validation receipt -> proof/catalog/policy/review -> release -> governed public surface
```

Never collapse it into:

```text
registry parent -> public Hazards truth
```

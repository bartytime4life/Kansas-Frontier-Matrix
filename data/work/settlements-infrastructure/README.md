<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/work/settlements-infrastructure/readme
name: Settlements Infrastructure Work README
path: data/work/settlements-infrastructure/README.md
type: data-work-domain-lane-readme
version: v0.1.0
status: draft
owners:
  - <data-steward>
  - <settlements-infrastructure-domain-steward>
  - <settlement-identity-steward>
  - <infrastructure-sensitivity-reviewer>
  - <pipeline-steward>
  - <source-steward>
  - <rights-reviewer>
  - <sensitivity-reviewer>
  - <policy-steward>
  - <evidence-steward>
  - <proof-steward>
  - <receipt-steward>
  - <catalog-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-29
updated: 2026-06-29
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
lifecycle_phase: work
domain: settlements-infrastructure
artifact_family: settlements-infrastructure-working-intermediates-and-candidates
path_posture: existing-greenfield-stub-replaced; broader-settlements-infrastructure-work-parent; singular-settlement-work-compatibility-lane-confirmed; directory-rules-lists-data-work-domain-run-id; canonical-path-docs-mark-settlements-infrastructure-vs-settlement-conflicted; implementation-maturity-needs-verification
sensitivity_posture: internal-work-only; no-public-path; release-blocked; candidate-not-truth; source-role-preserving; settlement-identity-infrastructure-condition-and-time-anti-collapse-required; critical-infrastructure-operator-dependency-cultural-sovereignty-archaeology-private-property-person-land-and-exact-location-joins-fail-closed; rights-needs-verification; evidence-aware; receipt-aware; policy-aware; correction-and-rollback-aware
related:
  - ../README.md
  - ../../README.md
  - ../settlement/README.md
  - ../../raw/settlements-infrastructure/README.md
  - ../../raw/settlement/README.md
  - ../../quarantine/settlements-infrastructure/README.md
  - ../../quarantine/settlement/README.md
  - ../../processed/settlements-infrastructure/README.md
  - ../../processed/settlement/README.md
  - ../../catalog/domain/settlements-infrastructure/README.md
  - ../../catalog/domain/settlement/README.md
  - ../../receipts/settlement/README.md
  - ../../proofs/settlement/README.md
  - ../../published/layers/settlements-infrastructure/README.md
  - ../../../docs/domains/settlements-infrastructure/README.md
  - ../../../docs/domains/settlements-infrastructure/CANONICAL_PATHS.md
  - ../../../docs/domains/settlements-infrastructure/DATA_LIFECYCLE.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../release/README.md
  - ../../../contracts/domains/settlements-infrastructure/
  - ../../../schemas/contracts/v1/domains/settlements-infrastructure/
  - ../../../policy/domains/settlements-infrastructure/
  - ../../../tools/validators/
tags:
  - kfm
  - data
  - work
  - settlements-infrastructure
  - settlement
  - infrastructure
  - lifecycle
  - raw-to-work
  - work-to-processed
  - quarantine-exit
  - municipality
  - census-place
  - townsite
  - ghost-town
  - fort
  - mission
  - reservation-community
  - infrastructure-asset
  - network-node
  - network-segment
  - facility
  - service-area
  - operator
  - condition-observation
  - dependency
  - candidate-assertion
  - place-identity
  - legal-status
  - temporal-scope
  - geometry-normalization
  - critical-infrastructure-review
  - source-role
  - no-public-path
  - not-release-authority
  - not-processed
  - not-proof
  - not-catalog
  - not-published
  - cite-or-abstain
notes:
  - "This README replaces the greenfield stub at `data/work/settlements-infrastructure/README.md`."
  - "This is the broader Settlements/Infrastructure WORK parent; the singular `data/work/settlement/README.md` path is treated as a compatibility sublane while segment topology remains conflicted."
  - "Directory Rules list `data/work/<domain>/<run_id>/` and describe WORK as normalized intermediates and candidate assertions that must not feed public API/UI or release aliases directly."
  - "WORK material is not settlement truth, not infrastructure truth, not processed truth, not catalog truth, not proof, not receipt authority, not policy authority, not release authority, and not public material."
  - "README presence does not prove work payloads, run manifests, validators, receipts, CI checks, policy enforcement, source descriptors, review completion, or release readiness."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Settlements / Infrastructure WORK

Working lifecycle parent for Settlements/Infrastructure normalization intermediates, candidate assertions, QA outputs, identity and geometry review packets, redaction/generalization trials, and run-local material that is not yet processed, cataloged, proven, released, or public.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: data" src="https://img.shields.io/badge/root-data%2F-0a7ea4">
  <img alt="Lifecycle: WORK" src="https://img.shields.io/badge/lifecycle-WORK-orange">
  <img alt="Domain: settlements-infrastructure" src="https://img.shields.io/badge/domain-settlements--infrastructure-7048e8">
  <img alt="Critical infrastructure: fail closed" src="https://img.shields.io/badge/critical%20infrastructure-fail%20closed-critical">
  <img alt="Boundary: candidate not truth" src="https://img.shields.io/badge/boundary-candidate%20not%20truth-critical">
</p>

**Quick links:** [Scope](#scope) · [Segment posture](#segment-posture) · [Repo fit](#repo-fit) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [WORK guardrails](#work-guardrails) · [Lifecycle flow](#lifecycle-flow) · [Suggested directory shape](#suggested-directory-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!CAUTION]
> `data/work/settlements-infrastructure/` is internal working state. It is not public, not release authority, not proof, not receipt authority, not catalog closure, not processed truth, not settlement legal-status truth, not infrastructure condition truth, not source registry authority, not policy authority, not a normal UI/API source, and not an AI-answer source.

---

## Scope

`data/work/settlements-infrastructure/` may hold Settlements/Infrastructure working material after RAW source capture or quarantine exit and before PROCESSED promotion.

This lane is appropriate for run-local, reviewable material such as:

- normalized intermediate records that still need validation;
- candidate `Settlement`, `Municipality`, `CensusPlace`, `Townsite`, `GhostTown`, `Fort`, `Mission`, and `ReservationCommunity` objects;
- candidate `InfrastructureAsset`, `NetworkNode`, `NetworkSegment`, `Facility`, `ServiceArea`, `Operator`, `ConditionObservation`, and `Dependency` objects;
- candidate name variants, legal-status intervals, census-place matches, historic-townsite matches, facility/service-area matches, operator-context matches, dependency candidates, and source-vintage alignment;
- geometry normalization, geometry repair, public-safe geometry trials, boundary-vintage alignment, network topology checks, service-area generalization, and over-precision review packets;
- identity reconciliation, dedupe, conflation, alias matching, dependency matching, and crosswalk drafts;
- source-role mapping outputs, citation mappings, rights/sensitivity review drafts, and QA summaries;
- aggregation, redaction, suppression, and generalization trials used to evaluate public-safe place, community, facility, service-area, or dependency representations;
- join packets that remain internal while evidence, source role, rights, sensitivity, cultural/sovereignty review, archaeology adjacency, person/land relation, hazard/hydrology relation, infrastructure dependency, policy, and review state are unresolved;
- run-local indexes and README files that explain work state without becoming proof, catalog, registry, policy, release, or public authority.

A file here may help a steward inspect a candidate. It does **not** make that candidate true, canonical, public, policy-admitted, evidence-supported, or released.

---

## Segment posture

The broader working segment in visible domain doctrine is:

```text
settlements-infrastructure
```

A singular compatibility lane also exists:

```text
data/work/settlement/
```

Current domain docs record `settlements-infrastructure` versus `settlement` as a conflicted / ADR-class naming issue. This README treats `data/work/settlements-infrastructure/` as the broader parent WORK lane because the path exists and the domain docs use the long segment as the working canonical form. It does not settle schemas, policy, release, validators, package names, route names, or migration behavior.

Until an ADR, Directory Rules update, migration note, or path map resolves this topology, do not create divergent WORK payloads under both `settlement` and `settlements-infrastructure` without a clear source, run, checksum, receipt, correction, and rollback relationship.

---

## Repo fit

| Responsibility | Correct home | Boundary |
|---|---|---|
| Settlements/Infrastructure RAW captures | [`../../raw/settlements-infrastructure/`](../../raw/settlements-infrastructure/README.md) | Broader domain source-edge material. |
| Settlement RAW compatibility captures | [`../../raw/settlement/`](../../raw/settlement/README.md) | Singular compatibility material. |
| Settlements/Infrastructure WORK candidates | `data/work/settlements-infrastructure/` | This lane. Internal only. |
| Settlement WORK compatibility candidates | [`../settlement/`](../settlement/README.md) | Compatibility sublane, not competing parent authority. |
| Settlements/Infrastructure quarantine holds | [`../../quarantine/settlements-infrastructure/`](../../quarantine/settlements-infrastructure/README.md) | Held broader-domain material. |
| Settlement quarantine compatibility holds | [`../../quarantine/settlement/`](../../quarantine/settlement/README.md) | Held singular-path material. |
| Settlements/Infrastructure processed artifacts | [`../../processed/settlements-infrastructure/`](../../processed/settlements-infrastructure/README.md) | Downstream broader processed parent. |
| Settlement processed compatibility artifacts | [`../../processed/settlement/`](../../processed/settlement/README.md) | Downstream processed compatibility lane. |
| Settlements/Infrastructure catalog records | [`../../catalog/domain/settlements-infrastructure/`](../../catalog/domain/settlements-infrastructure/README.md) | Broader catalog lane. |
| Settlement catalog compatibility records | [`../../catalog/domain/settlement/`](../../catalog/domain/settlement/README.md) | Catalog-stage alias, not WORK. |
| Settlement receipts | [`../../receipts/settlement/`](../../receipts/settlement/README.md) | Process memory; WORK may reference receipts but does not own them. |
| Settlement proofs | [`../../proofs/settlement/`](../../proofs/settlement/README.md) | EvidenceBundle/proof support; not WORK storage. |
| Published Settlements/Infrastructure layers | [`../../published/layers/settlements-infrastructure/`](../../published/layers/settlements-infrastructure/README.md) | Released public-safe carriers only. |
| Release decisions | `release/` | Release manifests, promotion decisions, rollback cards, corrections, withdrawals, signatures. |
| Contracts, schemas, policy, validators | `contracts/`, `schemas/`, `policy/`, `tools/validators/` | Separate authority roots. |

---

## Accepted material

Accepted content is limited to Settlements/Infrastructure working/intermediate material and work-local sidecars:

- run-local normalization outputs and candidate assertion files;
- identity reconciliation, legal-status alignment, geometry repair, place-name normalization, alternate-name matching, dedupe, conflation, crosswalk, unit/time conversion, source-vintage alignment, and QA outputs;
- facility, service-area, operator, condition-observation, dependency, and network-topology candidate outputs;
- source-role mapping drafts and source-field mapping drafts;
- aggregation, suppression, redaction, public-safe geometry, and generalization trials;
- work-local manifest, digest, and index sidecars used to inspect the run;
- references to RAW source captures, quarantine exits, receipts, proof candidates, policy decisions, and review notes;
- README files explaining local run or candidate boundaries.

All accepted material should preserve enough context to inspect source lineage, input digests, source role, run identity, tool/version where applicable, source vintage, observed/valid/retrieval/release/correction times where material, geometry handling, sensitivity posture, rights posture, reviewer state, and intended downstream path.

---

## Exclusions

| Do not place here | Correct home |
|---|---|
| Immutable source captures, source-native payloads, source query snapshots, source-head records, raw response mirrors, images, scans, OCR inputs, or source media | `data/raw/settlements-infrastructure/` or verified source-specific RAW lane |
| Rights-unclear, sensitivity-unclear, privacy-unsafe, source-role-unclear, critical-infrastructure-sensitive, cultural/sovereignty-sensitive, archaeology-adjacent, person/land-linked, hazard-stale, hydrology-stale, over-precise, or unresolved material requiring hold | `data/quarantine/settlements-infrastructure/` or compatible quarantine lane |
| Validated normalized settlement/place/infrastructure datasets ready for catalog/triplet promotion | `data/processed/settlements-infrastructure/` after validation and path review |
| Catalog records, STAC/DCAT/PROV/domain catalog entries, catalog matrices, or catalog indexes | `data/catalog/` |
| Graph/triplet projections, graph deltas, relationship exports, or public graph support | `data/triplets/` |
| EvidenceBundle, ProofPack, citation validation, integrity proof, or proof indexes | `data/proofs/` |
| RunReceipt, TransformReceipt, AggregationReceipt, RedactionReceipt, ValidationReceipt, AIReceipt, PolicyDecision, release-support receipt, or rollback receipt authority | `data/receipts/` or accepted receipt/rollback lanes |
| SourceDescriptor, source activation records, source registry entries, rights registry, sensitivity registry, or dataset registry records | `data/registry/` |
| Published layers, PMTiles, GeoParquet, reports, stories, API payloads, map tiles, public downloads, or release-linked artifacts | `data/published/` after release gates |
| ReleaseManifest, PromotionDecision, RollbackCard, CorrectionNotice, WithdrawalNotice, signatures, or release changelog | `release/` |
| Contracts, schemas, policy rules, validators, tests, implementation code, notebooks intended as code, apps, packages, or workflows | `contracts/`, `schemas/`, `policy/`, `tools/`, `tests/`, `apps/`, `packages/`, `.github/` |

---

## WORK guardrails

| Risk | Guardrail |
|---|---|
| Candidate becomes truth | WORK candidates remain candidates until processed validation, proof/catalog closure, policy review, and release state support stronger claims. |
| WORK becomes public | Public clients, normal UI surfaces, reports, stories, map layers, graph/vector indexes, Focus Mode, and AI answers must not read this lane directly. |
| Release alias bypass | WORK must not contain or update release aliases, current pointers, public route payloads, or published artifacts. |
| RAW mutation | RAW captures stay immutable; WORK may derive from RAW but must not overwrite or replace source captures. |
| Quarantine bypass | Rights-unclear, sensitivity-unsafe, source-role-unclear, over-precise, critical-infrastructure-sensitive, cultural/sovereignty-sensitive, archaeology-adjacent, hazard-stale, hydrology-stale, or person/land-linked material must move to quarantine or remain denied/held. |
| Source-role collapse | Census geography, GNIS/gazetteer records, municipal legal records, historic maps, operator/provider sources, KDOT/facility records, FEMA/hazard/resilience sources, modeled geometry, administrative indexes, candidates, and generated summaries must stay distinguishable. |
| Identity collapse | Settlement, Municipality, CensusPlace, Townsite, GhostTown, Fort, Mission, ReservationCommunity, InfrastructureAsset, Facility, ServiceArea, Operator, ConditionObservation, and Dependency must not collapse by name similarity, geometry overlap, operator name, or map label alone. |
| Time collapse | Source, observed, valid, retrieval, release, and correction times must remain distinct where material. |
| Critical infrastructure leakage | Exact facility, dependency, condition, operator, vulnerability, or service-area detail fails closed unless policy and review allow a public-safe representation. |
| Cross-lane ownership drift | Roads/Rail owns routes; Hydrology owns water evidence; Hazards owns hazard events and warnings; People/DNA/Land owns ownership, parcels, and living-person privacy; Archaeology owns sensitive site coordinates. WORK may hold candidate joins only. |
| AI overclaim | Generated labels, summaries, matching notes, dependency sketches, or inferred place narratives cannot stand in for EvidenceBundle, source role, validation, policy, review, or release state. |
| Stale or orphaned work | Work products should carry run identity, input refs, digests, timestamp/vintage, reviewer state, and intended disposition: process, quarantine, deny, hold, or delete through governed cleanup. |

---

## Lifecycle flow

```mermaid
flowchart LR
    RAW[data/raw/settlements-infrastructure] --> TRIAGE{Admission / triage}
    RAWC[data/raw/settlement] --> TRIAGE
    TRIAGE --> WORK[data/work/settlements-infrastructure]
    TRIAGE --> WORKC[data/work/settlement]
    TRIAGE --> QUAR[data/quarantine/settlements-infrastructure]
    QUAR -->|resolved with review| WORK
    WORKC -. compatibility relation .-> WORK
    WORK --> VALIDATE[validation / normalization / QA]
    VALIDATE -->|fails rights, sensitivity, identity, path, or source-role review| QUAR
    VALIDATE --> PROC[data/processed/settlements-infrastructure]
    PROC --> CAT[data/catalog/domain/settlements-infrastructure]
    CAT --> PUB[data/published/layers/settlements-infrastructure]
    PUB --> REL[release]

    classDef internal fill:#fff3cd,stroke:#8a6d3b,color:#202124;
    classDef hold fill:#f8d7da,stroke:#842029,color:#202124;
    classDef public fill:#d1e7dd,stroke:#0f5132,color:#202124;
    class WORK,WORKC,VALIDATE internal;
    class QUAR hold;
    class PUB,REL public;
```

> [!NOTE]
> This diagram is a responsibility map, not proof that pipelines, validators, receipts, policy engines, release manifests, or CI gates are currently wired.

---

## Suggested directory shape

Directory Rules list the pattern `data/work/<domain>/<run_id>/`. Exact Settlements/Infrastructure run layout is **PROPOSED** until schemas, pipeline specs, validators, and receipt conventions confirm it.

```text
data/work/settlements-infrastructure/
├── README.md
├── <run_id>/
│   ├── README.md
│   ├── work.manifest.json
│   ├── input_refs.json
│   ├── candidate_index.json
│   ├── normalized/
│   ├── candidates/
│   ├── identity_matching/
│   ├── geometry_review/
│   ├── topology_review/
│   ├── infrastructure_review/
│   ├── joins/
│   ├── qa/
│   ├── redaction_trials/
│   ├── generalization_trials/
│   ├── policy_review_refs.json
│   ├── receipt_refs.json
│   └── disposition.json
└── indexes/
    └── settlements_infrastructure.work.index.json
```

Do not pre-create empty child stubs unless a real run, migration, inventory, or steward decision requires them.

Recommended run-level fields:

| Field | Purpose |
|---|---|
| `run_id` | Stable working-run identifier. |
| `source_refs` | RAW captures, source registry records, or source descriptors feeding the run. |
| `input_digests` | Hashes or digests for source and intermediate inputs. |
| `source_role_state` | Observed, regulatory, modeled, aggregate, administrative, candidate, synthetic, or other governed posture. |
| `candidate_families` | Settlement/place/infrastructure object families represented by the run. |
| `rights_state` | Rights, terms, attribution, agreement, and use-limit posture. |
| `sensitivity_state` | Exact-location, critical-infrastructure, operator, dependency, cultural/sovereignty, archaeology, private-property, and person/land risk posture. |
| `identity_state` | Name, geometry, temporal, legal-status, facility/operator/dependency, and source-identifier reconciliation posture. |
| `validation_state` | Preflight, failed, held, passed, or needs review. |
| `intended_disposition` | `PROCESS`, `QUARANTINE`, `HOLD`, `DENY`, `ABSTAIN`, or `SUPERSEDE`. |
| `downstream_refs` | Processed, quarantine, receipt, proof, catalog, or release references if promoted later. |

---

## Required checks before use

- [ ] Confirm actual child run directories under `data/work/settlements-infrastructure/`.
- [ ] Confirm whether `data/work/settlement/` remains compatibility, migrates, or redirects to this lane.
- [ ] Confirm accepted Settlements/Infrastructure WORK manifest shape and naming convention.
- [ ] Confirm contracts, schemas, and validators for settlement/place/infrastructure candidate records.
- [ ] Confirm RAW source refs and input digest closure for every work run.
- [ ] Confirm source-role mapping for Census TIGER, GNIS, state/local GIS, municipal legal records, historical gazetteers/maps, infrastructure providers, KDOT/bridge/facility sources, and FEMA/hazard/resilience sources where used.
- [ ] Confirm legal municipality, CensusPlace, historic townsite, ghost-town, fort, mission, reservation-community, facility, service-area, operator, condition, and dependency identities are not collapsed by label or geometry.
- [ ] Confirm critical-infrastructure, operator, dependency, condition, cultural/sovereignty-sensitive, archaeology-adjacent, private property, people/land, exact-location, and vulnerable-facility joins are quarantined, redacted, aggregated, denied, or explicitly reviewed before downstream promotion.
- [ ] Confirm candidate outputs that advance to `data/processed/settlements-infrastructure/` have validation, receipt refs, policy posture, correction path, and rollback target where material.
- [ ] Confirm no public clients, normal UI, API, map layer, report, story, vector index, search surface, Focus Mode answer, or AI answer reads from this lane.
- [ ] Confirm work-local cleanup, retention, and supersession do not delete required provenance, receipts, evidence refs, or review state.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target path presence | CONFIRMED | `data/work/settlements-infrastructure/README.md` existed as a greenfield stub before this update. |
| Parent WORK README | CONFIRMED stub | `data/work/README.md` exists as a greenfield stub; this child README is self-bounding. |
| Singular WORK compatibility lane | CONFIRMED README | `data/work/settlement/README.md` exists and treats singular `settlement` as compatibility. |
| Data root | CONFIRMED README | `data/README.md` lists `work` under lifecycle data and excludes release decisions. |
| Directory Rules WORK path | CONFIRMED doctrine | Directory Rules list `data/work/<domain>/<run_id>/` and say WORK holds normalized intermediates and candidate assertions. |
| Settlements/Infrastructure domain doctrine | CONFIRMED README | Domain docs define object families, source families, cross-lane boundaries, sensitivity posture, and path conflict. |
| Segment conflict | CONFIRMED doctrine | `CANONICAL_PATHS.md` and `DATA_LIFECYCLE.md` mark `settlements-infrastructure` vs `settlement` as conflicted / ADR-class. |
| Settlements/Infrastructure RAW lane | CONFIRMED README | `data/raw/settlements-infrastructure/README.md` exists as the broader RAW parent. |
| Settlements/Infrastructure QUARANTINE lane | CONFIRMED README | `data/quarantine/settlements-infrastructure/README.md` exists as the broader hold lane. |
| Settlements/Infrastructure PROCESSED lane | CONFIRMED README | `data/processed/settlements-infrastructure/README.md` exists as the broader processed parent. |
| Settlements/Infrastructure CATALOG lane | CONFIRMED README | `data/catalog/domain/settlements-infrastructure/README.md` exists as the broader catalog parent. |
| Published layers lane | CONFIRMED README | `data/published/layers/settlements-infrastructure/README.md` exists and requires release/public-safe posture. |
| Actual WORK payload inventory | UNKNOWN | This README does not prove any work-run payloads exist. |
| WORK schemas, validators, receipts, CI, policy enforcement, release linkage | NEEDS VERIFICATION | No runtime enforcement was proven by this edit. |
| Public release readiness | DENY | A WORK README cannot publish, prove, or expose Settlements/Infrastructure claims. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `data/work/settlements-infrastructure/README.md` existed as a greenfield stub. | Did not define WORK-lane boundaries. |
| [`../README.md`](../README.md) | CONFIRMED stub | Parent WORK root exists. | Parent contract still needs expansion. |
| [`../../README.md`](../../README.md) | CONFIRMED README | `data/` owns lifecycle data and lists `work`. | Data root README is short and status `PROPOSED`. |
| [`../settlement/README.md`](../settlement/README.md) | CONFIRMED README | Singular WORK path is compatibility context. | Does not settle canonical segment topology. |
| [`../../../docs/domains/settlements-infrastructure/CANONICAL_PATHS.md`](../../../docs/domains/settlements-infrastructure/CANONICAL_PATHS.md) | CONFIRMED doctrine | Working canonical slug and `settlements-infrastructure` vs `settlement` conflict. | ADR/migration remains unresolved. |
| [`../../../docs/domains/settlements-infrastructure/DATA_LIFECYCLE.md`](../../../docs/domains/settlements-infrastructure/DATA_LIFECYCLE.md) | CONFIRMED doctrine / PROPOSED implementation | Lifecycle invariant, WORK role, gates, object ownership, and segment conflict. | Does not prove validators or pipelines. |
| [`../../raw/settlements-infrastructure/README.md`](../../raw/settlements-infrastructure/README.md) | CONFIRMED README | Broader RAW parent and domain halves. | Does not prove source payload presence. |
| [`../../quarantine/settlements-infrastructure/README.md`](../../quarantine/settlements-infrastructure/README.md) | CONFIRMED README | Broader quarantine parent and fail-closed posture. | Does not prove held payloads or automated policy enforcement. |
| [`../../processed/settlements-infrastructure/README.md`](../../processed/settlements-infrastructure/README.md) | CONFIRMED README | Broader processed parent and source-role/sensitivity posture. | Does not prove processed inventory or validators. |
| [`../../catalog/domain/settlements-infrastructure/README.md`](../../catalog/domain/settlements-infrastructure/README.md) | CONFIRMED README | Broader catalog parent and release-gated posture. | Does not prove catalog records. |
| [`../../published/layers/settlements-infrastructure/README.md`](../../published/layers/settlements-infrastructure/README.md) | CONFIRMED README | Published layers require release and public-safe posture. | Does not prove released artifacts exist. |

[Back to top](#top)

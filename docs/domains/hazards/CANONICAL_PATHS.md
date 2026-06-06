<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/domains/hazards/canonical-paths
title: Hazards Domain — Canonical Paths
type: standard
version: v2
status: draft
owners: <hazards-domain-steward TBD>; <directory-rules-steward TBD>
created: 2026-05-17
updated: 2026-06-05
policy_label: public
contract_version: "3.0.0"
related:
  - ../../../directory-rules.md
  - ./ARCHITECTURE.md
  - ./api-contracts.md
  - ./BLUEPRINT.md
  - ../README.md
  - kfm://standard/directory-rules
  - kfm://atlas/v1.1/section-24.13
  - kfm://encyclopedia/section-7.1
tags: [kfm, domains, hazards, directory-rules, canonical-paths]
notes:
  # CONTRACT_VERSION = "3.0.0" pinned per ai-build-operating-contract.md v3.0.
  # Schema-home form RESOLVED v1->v2 to the flat form `schemas/contracts/v1/hazards/`:
  #   TWO doctrine crosswalks converge on it — Atlas v1.1 Sec 24.13 AND Encyclopedia Sec 7.1
  #   (row updated 2026-05-24 for Directory Rules v1.3). The `/domains/hazards/` segment form
  #   appears only in the Build Manual's PROPOSED repo tree and in Directory Rules lane-pattern prose.
  #   The tension is preserved as a CONFLICTED open question (Sec 11) pending ADR-S-01 / ADR-0001.
  # Directory Rules is at v1.3 (Cesium retired; packages/maplibre-runtime/). Section refs are kept
  #   but NOT pinned to a specific subsection number unless verifiable.
  # All implementation paths remain PROPOSED until verified against a mounted repo.
[/KFM_META_BLOCK_V2] -->

# Hazards Domain — Canonical Paths

> Authoritative path map for everything the **Hazards** lane owns across KFM's responsibility roots — a domain-side index pinned to the Directory Rules Domain Placement Law and the lifecycle invariant `RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED`.

![Status: draft](https://img.shields.io/badge/status-draft-blue)
![Authority: domain index](https://img.shields.io/badge/authority-domain%20index-informational)
![Doctrine: Directory Rules v1.3](https://img.shields.io/badge/doctrine-Directory%20Rules%20v1.3-success)
![Contract: 3.0.0](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-blueviolet)
![Implementation: PROPOSED](https://img.shields.io/badge/implementation-PROPOSED-orange)
![Life-safety boundary](https://img.shields.io/badge/life--safety-not%20an%20alert%20authority-critical)
![Last updated: 2026-06-05](https://img.shields.io/badge/updated-2026--06--05-lightgrey)
<!-- TODO: replace shields above with repo-canonical Shields.io endpoints once selected. -->

**Status** — draft · **Owners** — `<hazards-domain-steward TBD>`, `<directory-rules-steward TBD>` · **Last updated** — 2026-06-05 · **`CONTRACT_VERSION = "3.0.0"`**

---

## Contents

- [1. Purpose and scope](#1-purpose-and-scope)
- [2. Authority and conformance](#2-authority-and-conformance)
- [3. Lane pattern at a glance](#3-lane-pattern-at-a-glance)
- [4. Canonical paths by responsibility root](#4-canonical-paths-by-responsibility-root)
- [5. Lifecycle paths under `data/`](#5-lifecycle-paths-under-data)
- [6. Release-plane paths](#6-release-plane-paths)
- [7. Cross-lane relations and shared homes](#7-cross-lane-relations-and-shared-homes)
- [8. Anti-patterns and drift watch](#8-anti-patterns-and-drift-watch)
- [9. Path-validation checklist for Hazards PRs](#9-path-validation-checklist-for-hazards-prs)
- [10. Compatibility and migration notes](#10-compatibility-and-migration-notes)
- [11. Open questions](#11-open-questions)
- [12. Related docs](#12-related-docs)

---

## 1. Purpose and scope

This document is the **Hazards domain's path index** — a single navigable map of where Hazards material lives across KFM's responsibility roots. It exists so contributors, reviewers, and stewards do not have to re-derive lane placement every time a fixture, schema, policy, pipeline, or release artifact for Hazards is added, moved, or audited.

It is **not** a license to create a `hazards/` root, a parallel schema home, or a separate publication path. The Hazards lane is a segment inside KFM's shared responsibility roots, governed by the same lifecycle, trust membrane, and authority rules as every other domain.

> [!IMPORTANT]
> **KFM Hazards is not an emergency alert authority.** Operational warnings and advisories are admitted as *context only*. Life-safety instruction is redirected to the issuing authority (e.g., NWS, FEMA, state EM). This boundary shapes several Hazards-specific path additions in §6 and §8.

> [!NOTE]
> **Schema-home form resolved in v2.** The v1 edition followed the `/domains/hazards/` **segment** form and treated Atlas §24.13 as the variance. The evidence runs the other way: **two** doctrine crosswalks — Atlas v1.1 §24.13 **and** KFM Encyclopedia §7.1 (row updated 2026-05-24 for Directory Rules v1.3) — converge on the **flat** form `schemas/contracts/v1/hazards/`. This doc now uses the flat form as primary and preserves the segment form as a CONFLICTED open question (§11) pending **ADR-S-01 / ADR-0001**.

[Back to top](#contents)

---

## 2. Authority and conformance

The Hazards lane sits inside a layered authority stack. Path claims in this document defer to the higher layer in case of conflict.

| Layer | Source | Authority for this doc |
|---|---|---|
| 1 | KFM operating law: lifecycle invariant, trust membrane, watcher-as-non-publisher, cite-or-abstain | **CONFIRMED** doctrine; binds every section here. |
| 2 | Accepted ADRs amending Directory Rules | Binding where accepted. The schema-home form question (§11) is a pending ADR candidate (ADR-S-01 / ADR-0001). |
| 3 | Directory Rules v1.3 (Domain Placement Law; Authority roots; Lifecycle; Anti-patterns) | **CONFIRMED** doctrine — primary basis for §§3–6 below. |
| 4 | Doctrine crosswalks: Atlas v1.1 §24.13 and Encyclopedia §7.1 (Hazards row) | **CONFIRMED** — the *more specific* mapping for the Hazards lane; both use the flat form. |
| 5 | Per-root `README.md` files in the repo | Refines this doc; cannot contradict layers 1–4. **NEEDS VERIFICATION** against mounted repo. |
| 6 | Mounted-repo convention | Where it conflicts with the layers above, raise via `docs/registers/DRIFT_REGISTER.md`, not as new authority. |

**Conformance language** (RFC 2119-style) follows the Directory Rules conformance section: **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, **MAY**.

> [!NOTE]
> Truth labels used below follow KFM convention: **CONFIRMED** (doctrine or verified evidence), **PROPOSED** (recommended path not yet verified in implementation), **INFERRED** (derivable but not directly stated), **NEEDS VERIFICATION** (checkable, not yet checked), **CONFLICTED** (sources disagree), **UNKNOWN** (not resolvable here).

[Back to top](#contents)

---

## 3. Lane pattern at a glance

The Hazards lane applies the Directory Rules **Domain Placement Law** uniformly: a domain MUST NOT become a root folder; instead, the domain name appears as a **segment** inside each owning responsibility root.

```mermaid
flowchart LR
    subgraph DOCTRINE["KFM Responsibility Roots (CONFIRMED)"]
        direction TB
        docs["docs/"]
        contracts["contracts/"]
        schemas["schemas/"]
        policy["policy/"]
        tests["tests/"]
        fixtures["fixtures/"]
        packages["packages/"]
        pipelines["pipelines/"]
        pipeline_specs["pipeline_specs/"]
        data["data/"]
        release["release/"]
    end

    subgraph LANE["Hazards Lane Segments (PROPOSED paths)"]
        direction TB
        d1["docs/domains/hazards/"]
        c1["contracts/hazards/"]
        s1["schemas/contracts/v1/hazards/"]
        p1["policy/domains/hazards/ + policy/release/hazards/"]
        t1["tests/domains/hazards/"]
        f1["fixtures/domains/hazards/"]
        pk1["packages/domains/hazards/"]
        pl1["pipelines/domains/hazards/"]
        ps1["pipeline_specs/hazards/"]
        da1["data/&lt;phase&gt;/hazards/"]
        re1["release/candidates/hazards/"]
    end

    docs --> d1
    contracts --> c1
    schemas --> s1
    policy --> p1
    tests --> t1
    fixtures --> f1
    packages --> pk1
    pipelines --> pl1
    pipeline_specs --> ps1
    data --> da1
    release --> re1

    classDef doctrine fill:#0b3954,stroke:#0b3954,color:#fff;
    classDef lane fill:#fef3c7,stroke:#92400e,color:#1f2937;
    class docs,contracts,schemas,policy,tests,fixtures,packages,pipelines,pipeline_specs,data,release doctrine;
    class d1,c1,s1,p1,t1,f1,pk1,pl1,ps1,da1,re1 lane;
```

> [!CAUTION]
> The diagram shows **PROPOSED** path segments derived from the Directory Rules Domain Placement Law and the doctrine crosswalks. They are not a claim that these directories currently exist in the repo. Note `contracts/hazards/` and `schemas/contracts/v1/hazards/` use the **flat** crosswalk form; see §11 for the pending segment-vs-flat ADR.

[Back to top](#contents)

---

## 4. Canonical paths by responsibility root

The table below is the Hazards lane's primary reference. Each row names a responsibility root, the Hazards-specific path inside it, what it owns, and what does **not** belong there.

| Responsibility root | Hazards path (PROPOSED) | Owns | Does NOT belong here | Status |
|---|---|---|---|---|
| `docs/` | `docs/domains/hazards/` | Domain README, this `CANONICAL_PATHS.md`, `ARCHITECTURE.md`, `api-contracts.md`, `BLUEPRINT.md`, runbooks, source dossiers, governance notes for Hazards. | Schemas, policy bundles, code, fixtures, release decisions. | Doctrine **CONFIRMED**; specific path **PROPOSED**. |
| `contracts/` | `contracts/hazards/` | Object-family **meaning** for `HazardEvent`, `HazardObservation`, `WarningContext`, `AdvisoryContext`, `DisasterDeclaration`, `FloodContext`, `WildfireDetection`, `SmokeContext`, `DroughtIndicator`, `EarthquakeEvent`, `HeatColdEvent`, `ExposureSummary`, `ResilienceSummary`, `HazardTimeline`, `ImpactArea`. | Machine-shape JSON Schemas (those live under `schemas/`); release decisions; policy. | **PROPOSED** (flat crosswalk form). |
| `schemas/` | `schemas/contracts/v1/hazards/` | Machine-checkable JSON Schemas for Hazards DTOs, layer manifests, and Hazards-flavored envelopes (e.g., `HazardsDecisionEnvelope`). Schema home is fixed by ADR-0001. | Object meaning (lives in `contracts/`); fixtures; instance data. | **PROPOSED** (flat crosswalk form; segment form CONFLICTED — §11). |
| `policy/` | `policy/domains/hazards/` | Allow/deny/restrict/abstain rules for Hazards: source-role anti-collapse, expiry/freshness denials, sensitive infrastructure joins, life-safety boundary enforcement. | Sensitivity registries for other domains; release manifests; tests. | **PROPOSED**. |
| `policy/` (release sub-lane) | `policy/release/hazards/` | Release-eligibility rules specific to Hazards (e.g., `not_emergency_alert_system` envelope flag, official-source referral requirement, stale-state denial). | Generic release policy (lives at `policy/release/`); life-safety operational decisions (KFM has no such authority). | **PROPOSED**; named explicitly by the Atlas §24.13 and Encyclopedia §7.1 crosswalks. |
| `tests/` | `tests/domains/hazards/` | Domain test suites: source-role anti-collapse, temporal-role, emergency-alert denial, operational expiry/freshness, catalog closure, Evidence Drawer disclaimer, UI no-direct-source. | Shared validator implementations (those live in `tools/validators/`); fixtures (those live in `fixtures/`). | **PROPOSED**. |
| `fixtures/` | `fixtures/domains/hazards/` (or `tests/fixtures/domains/hazards/` per repo convention) | Golden/valid/invalid/synthetic fixtures for Hazards: storm events, NFHL flood polygons, advisory polygons with expiry, earthquake catalog rows, FIRMS detections. | Schemas; canonical truth; published artifacts. | **PROPOSED**; choose **one** fixture home — `NEEDS VERIFICATION`. |
| `packages/` | `packages/domains/hazards/` | Reusable Hazards libraries: domain ontology helpers, source-role taxonomy, freshness/expiry utilities, exposure overlay helpers. | One-off scripts (those belong in `tools/` or `pipelines/`); deployable apps. | **PROPOSED**. |
| `pipelines/` | `pipelines/domains/hazards/` | Executable Hazards pipeline steps: ingest, normalize, validate, catalog, publish, rollback. | Declarative specs (those live in `pipeline_specs/`); connector definitions (those live in `connectors/`). | **PROPOSED**. |
| `pipeline_specs/` | `pipeline_specs/hazards/` | Declarative pipeline configuration for Hazards sources and transforms. | Executable logic; runtime adapters. | **PROPOSED**. |
| `data/` | See §5 | Lifecycle data by phase. | Release decisions (those live in `release/`); generated build artifacts. | **PROPOSED**. |
| `release/` | See §6 | Release candidates, manifests, rollback cards, correction notices for Hazards releases. | Released artifacts (those live in `data/published/`); receipts of process memory (those live in `data/receipts/`). | **PROPOSED**. |
| `connectors/` | Per-source, **not** per-domain — see §7 | Fetch and admission for Hazards source families (NOAA, NWS, FEMA, USGS, NASA, drought monitors). | Domain-bearing logic; publication. | **CONFIRMED** per-source rule (Directory Rules §7.3); paths **PROPOSED**. |
| `tools/validators/` | Cross-cutting validators with Hazards-aware fixtures | Generic validators for source descriptors, evidence bundles, promotion gates. Hazards-specific tests live in `tests/domains/hazards/`. | Domain-only logic that is not reusable. | **PROPOSED**. |

[Back to top](#contents)

---

## 5. Lifecycle paths under `data/`

The Hazards lane follows the lifecycle invariant exactly. Promotion between phases is a **governed state transition**, not a file move.

```text
data/
├── raw/hazards/<source_id>/<run_id>/         # Immutable source-edge captures.
├── work/hazards/<run_id>/                    # Normalized intermediates, candidate assertions.
├── quarantine/hazards/<reason>/<run_id>/     # Held: rights, sensitivity, source-role, schema,
│                                             #   expired operational context, life-safety drift.
├── processed/hazards/<dataset_id>/<version>/ # Validated normalized records, receipts attached.
├── catalog/
│   └── domain/hazards/                       # STAC/DCAT/PROV/domain catalog entries.
├── triplets/
│   ├── graph_deltas/                         # Hazards relations (event→declaration, event→exposure).
│   └── exports/
├── receipts/                                 # Run/validation/AI/ingest/release receipts (not domain-segmented).
├── proofs/                                   # EvidenceBundle/ProofPack closure (not domain-segmented).
├── published/
│   └── layers/hazards/                       # Released public-safe Hazards artifacts (e.g., PMTiles).
├── rollback/hazards/<release_id>/            # Alias-revert receipts (data plane).
└── registry/
    └── sources/hazards/                      # SourceDescriptors for Hazards source families.
```

### 5.1 Phase-by-phase Hazards rules

| Phase | Hazards-specific gate | Failure-closed outcome |
|---|---|---|
| `raw/hazards/` | `SourceDescriptor` exists; one of the **seven canonical source roles** declared (observed / regulatory / modeled / aggregate / administrative / candidate / synthetic); rights captured; sensitivity declared; payload or reference hashed. | Source not admitted; logged as candidate awaiting steward. |
| `work/hazards/` | Schema, geometry, time, identity, evidence, rights, and policy normalized; `TransformReceipt` + working `ValidationReport` + `PolicyDecision` emitted. | Move to `quarantine/hazards/` with reason; never silent promotion. |
| `quarantine/hazards/` | Common Hazards reasons: expired operational context labeled as current; warning/advisory used as life-safety instruction; unresolved rights on regulatory or proprietary feeds; source-role collapse (e.g., regulatory NFHL zone treated as observed event). | Hold; structured FAIL; remediation or denial. |
| `processed/hazards/` | `ValidationReport` pass; `EvidenceRef`s point to resolvable `EvidenceBundle`s; digest closure. | Stay in `work/`; structured FAIL. |
| `catalog/domain/hazards/` | `CatalogMatrix` entry; `EvidenceBundle` closure; graph/triplet projections where applicable. | HOLD at `processed/`; no public edge. |
| `published/layers/hazards/` | `ReleaseManifest` exists; rollback target exists; correction path exists; review state where required; **`not_emergency_alert_system`** posture set on operational-context layers. | HOLD at `catalog/`; no public surface change. |

> [!WARNING]
> The lifecycle is one-directional under normal promotion. Backward transitions (e.g., `published → quarantine` after a correction) are recorded via `CorrectionNotice` + `RollbackCard` in the **release plane** (§6), never by silent file deletion or overwrite.

> [!NOTE]
> The four source-family tags in the v1 phase-gate ("authority / observation / context / model") were the Hazards source-family role tags. They map onto the **seven canonical source roles** of the Atlas Source-Role Anti-Collapse Register (§24.1.1) — *role is fixed at admission and never upgraded by promotion*. "Operational" warning/advisory/watch is a freshness-bound sub-form carried with a canonical role, not an eighth role (OPEN under ADR-S-04).

[Back to top](#contents)

---

## 6. Release-plane paths

The release plane is **separate** from `data/published/`. Conflating released **artifacts** (`data/published/layers/hazards/`) with release **decisions** (`release/.../hazards/`) is one of the named drift patterns in the Directory Rules anti-pattern register.

```text
release/
├── candidates/hazards/         # Release-candidate dossiers for Hazards.
├── manifests/                  # ReleaseManifest by release_id (not domain-segmented at this level).
├── promotion_decisions/        # PromotionDecision records.
├── rollback_cards/             # Rollback decision artifacts (release plane).
├── correction_notices/         # Public correction notices.
├── withdrawal_notices/         # Withdrawal records.
├── signatures/                 # DSSE / Sigstore artifacts.
└── changelog/                  # Release-level changelog.
```

### 6.1 Hazards-specific release rules

- **MUST** include a `not_emergency_alert_system` posture in every Hazards `ReleaseManifest` whose payload includes operational-context layers (warnings, advisories, watches).
- **MUST** name an official referral source (e.g., NWS, FEMA, state EM) for any layer that depicts operational context.
- **MUST NOT** publish operational-context layers without an expiry/freshness contract.
- **SHOULD** route `rollback_cards/` and `correction_notices/` for hazard misclassifications through the steward-review queue before public publication, given the elevated misuse risk.
- **MAY** stage public release through `apps/review-console/` for layers whose source freshness is borderline.

> [!NOTE]
> Whether `not_emergency_alert_system` lives on the `ReleaseManifest`, the `LayerManifest`, both, or the `HazardsDecisionEnvelope` is **OPEN** (see §11 item 6 and the companion `api-contracts.md`).

[Back to top](#contents)

---

## 7. Cross-lane relations and shared homes

Hazards is one of KFM's most cross-cutting lanes. Files that legitimately span domains MUST follow the Directory Rules multi-domain placement rule — they live under the **lowest common responsibility root without a domain segment**, not under a single picked domain.

| Cross-cutting concern | Where it lives | Why |
|---|---|---|
| Hazards ↔ Hydrology flood/drought context | `tools/validators/<topic>/...`; `schemas/contracts/v1/<topic>/...` (no domain segment) | Cross-lane validator/schema, not a Hazards-only file. NFHL is owned by Hydrology's regulatory channel and cited by Hazards. |
| Hazards ↔ Atmosphere/Air smoke and heat/cold | Same as above. | Same. |
| Hazards ↔ Settlements/Infrastructure exposure overlays | Same as above. Critical-infrastructure sensitivity gates live in `policy/sensitivity/infrastructure/`, **not** under `policy/domains/hazards/`. | Sensitivity ownership stays with Settlements/Infrastructure (critical-asset deny lane). |
| Hazards ↔ Roads/Rail closure and resilience | Same. Route exposure decisions remain in the Roads/Rail lane. | Ownership rule. |
| Hazards source connectors (NOAA, NWS, FEMA, USGS, NASA) | `connectors/<source_family>/` — **per source**, not under a `hazards/` segment. | Connectors are source-specific, not domain-specific (Directory Rules §7.3; governed by ADR-S-04 source-role and ADR-S-12 cadence/quarantine). |
| Hazards `SourceDescriptor`s | `data/registry/sources/hazards/` | Registry records are domain-segmented by ownership. |

> [!TIP]
> A useful smell test: if a file would need to be edited every time *another* domain changes, it probably belongs in a cross-cutting home, not under `policy/domains/hazards/`.

[Back to top](#contents)

---

## 8. Anti-patterns and drift watch

The patterns below are the Hazards-specific versions of the Directory Rules anti-pattern register (§13). Each is a drift candidate; each has a fix.

| Anti-pattern | Symptom | Why it's wrong | Fix |
|---|---|---|---|
| **`hazards/` at repo root** | A `hazards/` folder appears at root with its own `data/`, `schemas/`, `policy/`, `docs/` subtree. | Violates Domain Placement Law; fragments the lifecycle; creates parallel schema/policy/data homes (Directory Rules §13.4). | Migrate piece by piece into the responsibility-root lane pattern; preserve `docs/domains/hazards/README.md`. |
| **Parallel Hazards schema home** | Schemas under both `contracts/hazards/*.schema.json` and `schemas/contracts/v1/hazards/*.schema.json` (or `jsonschema/`). | Two homes diverge silently; reviewers no longer know which is authoritative. | Per ADR-0001, `schemas/contracts/v1/...` is canonical; freeze old/mirror paths; add drift entry. |
| **Segment-vs-flat schema-home drift** | Some Hazards schemas land at `schemas/contracts/v1/domains/hazards/` and others at `schemas/contracts/v1/hazards/`. | The two doctrine forms (lane-pattern segment vs. crosswalk flat) are used inconsistently. | Pick one per ADR-S-01; until then prefer the crosswalk **flat** form and log the choice in `DRIFT_REGISTER.md` (§11). |
| **Operational warning treated as observed event** | `WarningContext` records flow into a `HazardEvent` catalog path without source-role separation. | Collapses source roles; violates Hazards anti-collapse posture. | Quarantine in `data/quarantine/hazards/source_role_collapse/<run_id>/`; require steward review. |
| **Life-safety drift** | Hazards layer published without `not_emergency_alert_system` posture; UI presents an advisory as instruction. | Violates the KFM Hazards boundary; Deny-by-Default register lists *Hazards — KFM as alert authority → not allowed*. | DENY at the release gate; emit `PolicyDecision` with reason; route correction through `release/correction_notices/`. |
| **Expired operational context shown as current** | Warning polygon with elapsed expiry remains visible on a public layer. | Stale state on a hazard surface is high-risk. | Freshness validator MUST deny; quarantine and rollback per `release/rollback_cards/`. |
| **Public client reads `data/processed/hazards/` directly** | `apps/explorer-web/` or an external consumer hits a canonical store. | Trust-membrane bypass (Directory Rules §7.1). | Public reads MUST route through `apps/governed-api/`. |
| **Connector publishes Hazards data** | A NOAA/NWS/FEMA connector writes to `data/processed/hazards/` or `data/published/layers/hazards/`. | Connectors do not publish (Directory Rules §7.3); watcher-as-non-publisher invariant. | Connector output stays in `data/raw/hazards/<source_id>/<run_id>/` or `data/quarantine/hazards/<reason>/<run_id>/`. |
| **Release manifest in `artifacts/`** | A Hazards `ReleaseManifest` ends up in `artifacts/` instead of `release/manifests/`. | Confuses build/QA scratch with release decisions (Directory Rules §13.2). | Move to `release/manifests/`; `artifacts/` is build/docs/qa/temporary only. |
| **Sensitive infrastructure exposure via Hazards layer** | A Hazards exposure overlay reveals precise critical-infrastructure geometry. | Critical-asset deny lane lives with Settlements/Infrastructure (Atlas §24.13). | Generalize geometry; route through `policy/sensitivity/infrastructure/`; emit `RedactionReceipt`. |

[Back to top](#contents)

---

## 9. Path-validation checklist for Hazards PRs

Reviewers SHOULD work through this list for any PR that adds, moves, or renames a Hazards-bearing path. It extends the Directory Rules path-validation checklist with Hazards-specific items.

- [ ] **Responsibility identified.** File maps to exactly one responsibility root.
- [ ] **Right root.** Chosen root matches the responsibility (e.g., a JSON Schema went to `schemas/`, not `contracts/`).
- [ ] **Domain segment correct.** `hazards/` appears as a *segment* inside a responsibility root, never as a root.
- [ ] **Schema-home form consistent.** New Hazards schemas use the **flat** crosswalk form `schemas/contracts/v1/hazards/` (pending ADR-S-01); not mixed with `…/domains/hazards/`.
- [ ] **Lifecycle phase correct** (for `data/` files). Phase named explicitly; no phase-skipping.
- [ ] **No new root without ADR.** No `hazards/` at root; no new sibling under `data/`.
- [ ] **No parallel authority.** No new home for Hazards schemas, contracts, policy, sources, registries, releases, proofs, or receipts.
- [ ] **README present.** Affected folders have READMEs that meet the Directory Rules folder-README contract.
- [ ] **Trust content placement.** Receipts → `data/receipts/`; proofs → `data/proofs/`; release manifests → `release/manifests/`; never `artifacts/`.
- [ ] **Public path discipline.** Routes go through `apps/governed-api/`, not directly to canonical stores.
- [ ] **Connector posture.** Connectors emit to `data/raw/hazards/...` or `data/quarantine/hazards/...`, never to `data/processed/` or `data/published/`.
- [ ] **Watcher posture.** Workers under `apps/workers/` emit receipts and candidate decisions; they do not publish.
- [ ] **Source-role labeled.** `SourceDescriptor` declares one of the seven canonical roles; role is fixed at admission.
- [ ] **Freshness/expiry contract.** Operational-context layers carry expiry and freshness fields.
- [ ] **Life-safety flag.** Release manifest sets `not_emergency_alert_system` posture for operational-context layers.
- [ ] **Official referral declared.** Operational-context layers name an official issuing authority for redirection.
- [ ] **Cross-lane sensitivity respected.** Critical-infrastructure or sensitive-occurrence joins routed through the owning lane's sensitivity policy.

[Back to top](#contents)

---

## 10. Compatibility and migration notes

The following are points of friction or PROPOSED state that may surface during repo inspection. Each is a candidate drift entry or ADR question.

| Item | Status | Notes |
|---|---|---|
| `schemas/contracts/v1/hazards/` (crosswalk flat form) vs. `schemas/contracts/v1/domains/hazards/` (lane-pattern segment form) | **CONFLICTED** | Two doctrine crosswalks (Atlas §24.13, Encyclopedia §7.1) use the **flat** form; the segment form appears in the Build Manual's PROPOSED repo tree and lane-pattern prose. This doc uses the flat form; an ADR (ADR-S-01 / ADR-0001) should freeze one. See §11. |
| Fixture home: `fixtures/domains/hazards/` vs. `tests/fixtures/domains/hazards/` | **NEEDS VERIFICATION** | Both `fixtures/` (root) and `tests/fixtures/` appear in proposed repo trees; choose one per repo convention; document the choice in both root READMEs. |
| `policy/release/hazards/` as a Hazards-specific release-policy sub-lane | **CONFIRMED in crosswalk / PROPOSED in repo** | Both the Atlas §24.13 and Encyclopedia §7.1 Hazards rows name it; not yet verified present in a mounted repo. |
| `apps/api/` vs. `apps/governed-api/` boundary | **OPEN** in Directory Rules; affects Hazards public path | Both appear in the proposed `apps/` tree; Hazards public routes MUST land on `apps/governed-api/`. |
| `data/rollback/hazards/` (data plane) vs. `release/rollback_cards/` (release plane) | **OPEN** in Directory Rules | This doc keeps both: `data/rollback/hazards/` for alias-revert receipts; `release/rollback_cards/` for the release decision. |
| Directory Rules version | **CONFIRMED v1.3** | v1.3 retired Cesium and uses `packages/maplibre-runtime/`; the v1 edition of this doc cited "v1.2"-era section numbers without a version. Section numbers here are kept but not pinned to a subsection unless verifiable. |

[Back to top](#contents)

---

## 11. Open questions

<details>
<summary>Click to expand the verification and ADR backlog</summary>

| # | Question | Why it matters | What would settle it |
|---|---|---|---|
| 1 | Is the canonical schema-home form for Hazards `schemas/contracts/v1/hazards/` (crosswalks) or `schemas/contracts/v1/domains/hazards/` (lane-pattern segment)? | Two forms in doctrine create exactly the parallel-home risk §8 flags. This doc resolves to the **flat** form because two crosswalks converge on it, but an ADR should freeze it. | ADR-S-01 / ADR-0001 confirming or amending the schema-home form; `DRIFT_REGISTER.md` entry for the v1→v2 correction. |
| 2 | Does the repo use `fixtures/domains/hazards/` or `tests/fixtures/domains/hazards/`? | Avoids two competing fixture homes. | Mounted-repo inspection + per-root README declaration. |
| 3 | Is `policy/release/hazards/` adopted as a stable sub-lane, or merged back into `policy/domains/hazards/`? | Hazards is one of the lanes most likely to need release-specific policy (life-safety boundary). | ADR; cross-lane survey of whether other domains (e.g., 3D `policy/release/scene/`) share the pattern. |
| 4 | Are NOAA/NWS/FEMA/USGS/NASA connectors structured per-source under `connectors/<source_family>/` with no Hazards umbrella? | Directory Rules §7.3 says per-source; verify no umbrella exists. | Mounted-repo inspection. |
| 5 | Does `apps/workers/` include a Hazards freshness/expiry watcher that respects watcher-as-non-publisher? | Workers MUST emit receipts and candidate decisions only. | Mounted-repo inspection + log/receipt audit. |
| 6 | Is `not_emergency_alert_system` a `ReleaseManifest` field, a `LayerManifest` field, a `HazardsDecisionEnvelope` field, several, or none? | Determines where the life-safety boundary is enforced. | Schema inspection under `schemas/contracts/v1/release/`, `…/runtime/`, `…/hazards/`; cross-check `api-contracts.md`. |
| 7 | Does "operational" warrant a distinct `source_role` enum value, or remain a freshness/policy overlay on observed/regulatory? | Affects every Hazards `SourceDescriptor` and validator. | ADR-S-04 (source-role vocabulary v1). |
| 8 | Where do `EvidenceDrawerPayload` disclaimer strings for Hazards live — content under `docs/`, schema under `schemas/`, or fixtures under `fixtures/`? | Affects UI no-direct-source tests and Drawer policy. | Cross-check `docs/architecture/ui/README.md` and per-root READMEs. |
| 9 | Verification backlog from the Hazards encyclopedia chapter (source endpoints/rights; role taxonomy and freshness states; emergency-alert boundary enforcement; release/correction/rollback drill) — current evidence state? | All four are **NEEDS VERIFICATION** in source doctrine. | Mounted-repo files, schemas, registry entries, tests, logs, emitted artifacts, review records, release manifests. |

</details>

[Back to top](#contents)

---

## 12. Related docs

- [`docs/doctrine/directory-rules.md`](../../../directory-rules.md) — root authority for placement, lifecycle, and trust membrane (v1.3). (CONFIRMED authority)
- [`docs/domains/hazards/ARCHITECTURE.md`](./ARCHITECTURE.md) — what the Hazards lane is.
- [`docs/domains/hazards/api-contracts.md`](./api-contracts.md) — governed API surfaces + decision envelopes.
- [`docs/domains/hazards/BLUEPRINT.md`](./BLUEPRINT.md) — lane implementation build plan.
- [`docs/domains/hazards/README.md`](./README.md) — domain landing page. *(TODO: confirm existence in mounted repo.)*
- [`docs/domains/README.md`](../README.md) — domains index. *(TODO: confirm.)*
- [`docs/standards/PROV.md`](../../standards/PROV.md) — provenance standards profile referenced by Hazards `EvidenceBundle`s. *(Filename `PROV.md` vs `PROVENANCE.md` is OPEN per Directory Rules OPEN-DR-01.)*
- [`docs/registers/DRIFT_REGISTER.md`](../../registers/DRIFT_REGISTER.md) — where to raise §10 / §11 items that cannot be resolved by ADR alone. *(TODO: confirm.)*
- [`docs/adr/`](../../adr/) — ADR home; questions in §11 are candidates here (ADR-S-01, ADR-S-04, ADR-0001).
- Atlas v1.1 §24.13 — Atlas Section ↔ Dossier ↔ Responsibility Root crosswalk. *(In project knowledge.)*
- Encyclopedia §7.1 — Domain → Atlas section → Responsibility root crosswalk. *(In project knowledge.)*

---

<sub>Last updated: **2026-06-05** · Owners: `<hazards-domain-steward TBD>`, `<directory-rules-steward TBD>` · `CONTRACT_VERSION = "3.0.0"` · [Back to top](#contents)</sub>

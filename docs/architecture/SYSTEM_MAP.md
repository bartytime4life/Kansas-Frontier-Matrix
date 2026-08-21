<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/architecture/system-map
title: KFM System Map
type: architecture-orientation
version: v2
status: repository-grounded draft
owners:
  - "@bartytime4life"
created: 2026-05-14
updated: 2026-08-18
policy_label: public
current_path: docs/architecture/SYSTEM_MAP.md
owning_root: docs/
responsibility: Human-readable whole-system orientation that maps accepted directory governance, current repository surfaces, lifecycle, trust objects, governed interfaces, release, and correction boundaries without creating independent authority.
truth_posture: >-
  CONFIRMED current repository paths and bounded implementation evidence at the pinned main commit;
  ACCEPTED Directory Rules v2 through ADR-0029; PROPOSED explanatory composition and desired
  end-to-end flow; UNKNOWN runtime, deployment, operational release, source activation, public
  availability, and production behavior unless separately proved.
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 70d2f1da3a480e14a19573ebec55258fc64e5f8e
  target_prior_blob: 6f760580bda6c23a6c227b3dd36edeaa7d34d9e0
  directory_rules_decision: ADR-0029 accepted
  root_registry_blob: 024f668b5f0a9239bafa4f8b09e2afd86300ff8c
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  current_open_prs_touching_target: 0
prepared_under_prompt: KFM Repository Build-Out & Markdown Modernization Implementation Agent v6.0.0
prompt_hash: sha256:b7a203460181956333f5a4b4ccda5eea87e97254b5d6396a4ad4186f1013dabb
notes:
  - Same-path modernization; no root, contract, schema, policy, runtime, release, deployment, or publication transition.
  - ADR-0029 is the only accepted numbered ADR in the current ADR index; all other numbered ADRs remain proposed.
  - The seven planes are an explanatory responsibility projection aligned with the current Skeleton Map and accepted root classes, not a new governance decision.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KFM System Map

> **One-line purpose.** Orient maintainers and reviewers to how Kansas Frontier Matrix responsibilities, lifecycle states, trust objects, implementation surfaces, release decisions, governed interfaces, and correction paths fit together—without treating this page as truth, policy, review, release, or publication authority.

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-d29922?style=flat-square)](#status-and-evidence-boundary)
[![Base: main@70d2f1d](https://img.shields.io/badge/base-main%4070d2f1d-0969da?style=flat-square)](#status-and-evidence-boundary)
[![Directory Rules: accepted](https://img.shields.io/badge/Directory%20Rules-v2%20accepted-1a7f37?style=flat-square)](../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
[![Publication authority: none](https://img.shields.io/badge/publication%20authority-none-b42318?style=flat-square)](#status-and-evidence-boundary)

> [!IMPORTANT]
> **This document is explanatory.** Accepted doctrine and ADRs, semantic contracts, machine schemas, policy, current code and configuration, executable tests and workflows, emitted receipts and proofs, append-only release records, and observed runtime evidence outrank this map for the questions they own. Repository presence proves bytes at a pinned commit; it does not prove behavior, review, release, deployment, public safety, or KFM publication.

## Status and evidence boundary

| Field | Current bounded result |
|---|---|
| Document role | Human-readable whole-system architecture orientation |
| Repository location | **CONFIRMED:** `docs/architecture/SYSTEM_MAP.md` |
| Owning responsibility root | **CONFIRMED:** `docs/` — human-readable explanation |
| Evidence base | **CONFIRMED:** `main@70d2f1da3a480e14a19573ebec55258fc64e5f8e` |
| Placement authority | **CONFIRMED:** Directory Rules v2 adopted by accepted ADR-0029 |
| Numbered ADR posture | **CONFIRMED:** ADR-0029 accepted; the other numbered ADRs remain proposed in the current index |
| Verified GitHub owner route | **CONFIRMED:** `@bartytime4life`; specialist stewardship remains `NEEDS VERIFICATION` |
| Implementation posture | **MIXED:** bounded fixture-first slices exist; live service, renderer, deployment, and operational-release claims remain held or unknown |
| Public or release authority | None |
| Change effect | Documentation plus paired generated provenance receipt; no executable or lifecycle state transition |

### Truth split used throughout

- **CONFIRMED** — repository bytes, accepted ADR-0029, active machine projections, or bounded implementation evidence inspected at the pinned base.
- **PROPOSED** — explanatory composition, desired integrated flow, or future behavior not yet proved end to end.
- **UNKNOWN** — runtime, deployment, source activation, operational release, public availability, or behavior not established by current evidence.
- **NEEDS VERIFICATION** — a concrete repository, CI, ownership, runtime, or release check remains before relying on the claim.

## Quick jump

- [1. Purpose](#1-purpose)
- [2. At a glance](#2-at-a-glance)
- [3. Architecture reading order](#3-architecture-reading-order)
- [4. Seven responsibility planes](#4-architectural-cut--seven-responsibility-planes)
- [5. Trust spine](#5-the-trust-spine)
- [6. Canonical lifecycle](#6-canonical-data-lifecycle)
- [7. Core object families](#7-core-object-families)
- [8. Responsibility-root map](#8-responsibility-root-map)
- [9. Governed public path](#9-governed-public-path)
- [10. Current maturity](#10-current-maturity)
- [11. Invariants and acceptance](#11-invariants-and-acceptance)
- [12. Open verification](#12-open-verification)
- [13. Related documents](#13-related-documents)
- [Rollback](#rollback)

---

## 1. Purpose

This page answers five orientation questions:

1. Which responsibility plane owns a concern?
2. Which accepted root or compatibility class contains the artifact?
3. Which lifecycle, evidence, policy, review, or release state is involved?
4. Which repository surface currently exists, and how mature is it?
5. Which evidence must be checked before a claim crosses the public trust membrane?

It does **not** replace [Directory Rules](../doctrine/directory-rules.md), the [ADR index](../adr/INDEX.md), [semantic contracts](./contract-schema-policy-split.md), schemas, policy, root READMEs, tests, generated receipts, release records, or runtime evidence.

### Placement basis

The file already exists under `docs/architecture/`, explains the system to humans, and does not change authority. Same-path modernization therefore preserves the `docs/` responsibility root under accepted Directory Rules. The paired AI provenance record belongs under `data/receipts/generated/`, not beside this document and not under `artifacts/` or `release/`.

[Back to top](#top)

---

## 2. At a glance

```text
SOURCE EDGE / PRE-RAW EVENT
    |
    v
RAW --> WORK / QUARANTINE --> PROCESSED --> CATALOG / TRIPLET --> PUBLISHED
             |                    |                 |                  |
             |                    |                 |                  +--> released public-safe artifacts
             |                    |                 +---------------------> discovery and provenance projections
             |                    +---------------------------------------> validated domain products
             +------------------------------------------------------------> unresolved or restricted material

PUBLISHED + EvidenceBundle + policy/review/release state
    |
    v
GOVERNED API / RELEASED ARTIFACTS
    |
    v
EXPLORER / MAP / EVIDENCE DRAWER / FOCUS MODE / EXPORTS
    |
    v
CORRECTION / WITHDRAWAL / SUPERSESSION / ROLLBACK / RECOMPILE
```

**Operating law:** public clients consume governed interfaces or released public-safe artifacts. They do not use RAW, WORK, QUARANTINE, candidate stores, internal proof stores, or direct model runtimes as their normal path.

[Back to top](#top)

---

## 3. Architecture reading order

Use the narrowest source that owns the question:

1. [Authority ladder](../doctrine/authority-ladder.md) and [truth posture](../doctrine/truth-posture.md) for claim authority.
2. Accepted ADRs and [Directory Rules](../doctrine/directory-rules.md) for decisions and placement.
3. [Skeleton Map](./SKELETON_MAP.md) and this page for orientation.
4. Semantic contracts, schemas, and policy for meaning, shape, and admissibility.
5. Code, configuration, fixtures, tests, workflows, and emitted artifacts for current behavior.
6. `release/`, correction records, and rollback evidence for promotion and public-state claims.
7. Runtime logs, deployed health evidence, and public probes for operational claims.

A lower layer may refine a higher layer but may not silently overrule it.

[Back to top](#top)

---

<a id="4-architectural-cut--the-five-planes"></a>
<a id="4-architectural-cut--seven-responsibility-planes"></a>

## 4. Architectural cut — seven responsibility planes

The earlier five-plane framing is preserved by the legacy anchor above. The current explanatory view uses seven planes so meaning, admissibility, lifecycle accountability, implementation, release, and exposure do not collapse into one another.

```text
1. DOCTRINE / DECISIONS
          |
2. MEANING / SHAPE
          |
3. ADMISSIBILITY
          |
4. LIFECYCLE / ACCOUNTABILITY
          |
5. IMPLEMENTATION
          |
6. RELEASE / CORRECTION
          |
7. RUNTIME / EXPOSURE
```

| Plane | Owns | Representative roots | Must not be mistaken for |
|---|---|---|---|
| 1. Doctrine and decisions | Operating law, accepted decisions, placement authority | `docs/`, `control_plane/` | Runtime behavior or release proof |
| 2. Meaning and shape | Object semantics and machine validation shape | `contracts/`, `schemas/` | Permission or policy outcome |
| 3. Admissibility | Rights, sensitivity, access, release eligibility | `policy/` | Canonical truth or implementation |
| 4. Lifecycle and accountability | Source registry, RAW through PUBLISHED lanes, receipts, proofs | `data/` | Promotion merely because a path exists |
| 5. Implementation | Apps, packages, connectors, pipelines, tools, runtime code, configuration | `apps/`, `packages/`, `connectors/`, `pipelines/`, `tools/`, `runtime/`, `configs/` | Public authority merely because code runs |
| 6. Release and correction | Promotion, release, correction, withdrawal, rollback decisions | `release/` | Data storage or generated scratch output |
| 7. Runtime and exposure | Governed API, released delivery artifacts, UI and AI interpretation | app/runtime surfaces downstream of release | Root truth, policy, or source authority |

### Cross-plane change discipline

A material change should identify every directly affected plane. A semantic change may require schema, fixture, validator, policy, implementation, documentation, and release compatibility work. A documentation-only correction must not imply those changes occurred.

[Back to top](#top)

---

## 5. The trust spine

```text
SourceDescriptor
    -> source capture or immutable source reference
    -> EvidenceRef
    -> EvidenceBundle resolution
    -> policy and sensitivity decision
    -> validation and review evidence
    -> proof and catalog closure
    -> release decision + rollback target
    -> governed response or released artifact
    -> map/UI/AI interpretation
    -> correction, withdrawal, or rollback lineage
```

| Stage | Minimum trust question | Failure posture |
|---|---|---|
| Source admission | Is identity, authority role, access, rights, cadence, and sensitivity known? | HOLD, QUARANTINE, or DENY |
| Evidence resolution | Can `EvidenceRef` resolve to the intended `EvidenceBundle` with valid digest and scope? | ABSTAIN, DENY, or ERROR |
| Policy and review | Is the requested use allowed for this actor, precision, time, and consequence? | DENY or HOLD |
| Validation | Do shape, identity, temporal, spatial, citation, and cross-object checks pass? | ERROR or HOLD |
| Promotion | Are proof, review, release, correction, and rollback obligations closed? | DENY or HOLD |
| Public response | Is the result released, public-safe, citable, in scope, and current enough? | ANSWER, ABSTAIN, DENY, or ERROR |

Receipts record process memory. Proofs support closure. Catalogs support discovery. Release records decide state transitions. None substitutes for another.

[Back to top](#top)

---

## 6. Canonical data lifecycle

The invariant remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

| Lifecycle lane | Responsibility | Public-client posture |
|---|---|---|
| `data/raw/` | Captured source material or immutable references | DENY |
| `data/work/` | Candidate normalization and analysis | DENY |
| `data/quarantine/` | Unresolved rights, sensitivity, quality, identity, or policy | DENY |
| `data/processed/` | Validated domain products, not automatically released | DENY by default |
| `data/catalog/` | Governed discovery records and catalog projections | Only released/public-safe views |
| `data/triplets/` | Derived relationship projections | Never sovereign truth |
| `data/receipts/` | Process and transformation memory | Internal unless separately released |
| `data/proofs/` | Validation/provenance closure support | Internal or controlled |
| `data/registry/` | Source and system registries | Governed exposure only |
| `data/published/` | Released public-safe carriers | Eligible only with matching release decision |

**CONFIRMED:** these canonical lanes are documented in [`data/README.md`](../../data/README.md). **UNKNOWN:** path presence alone does not establish live source activation, complete promotion, deployment, or public availability.

[Back to top](#top)

---

## 7. Core object families

| Family | Primary role | Authority boundary |
|---|---|---|
| `SourceDescriptor` | Source identity, authority role, rights, cadence, geography, sensitivity, activation posture | Must precede live use |
| `EvidenceRef` | Stable reference from a claim-bearing object to support | Not resolved evidence by itself |
| `EvidenceBundle` | Resolved evidence, provenance, scope, citations, review, and limitations | Outranks generated language |
| `PolicyDecision` | Allow, deny, restrict, redact, delay, or require review | Does not create source truth |
| `RuntimeResponseEnvelope` | Finite `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` result | Does not publish or promote |
| `RunReceipt` / `TransformReceipt` / `AIReceipt` | Inputs, tools, hashes, decisions, outputs, and failures | Process memory, not approval |
| `ProofPack` | Validation and provenance closure material | Support, not release authority |
| `CatalogMatrix` / STAC / DCAT / PROV projections | Discovery and interoperability | Derived and cross-checked |
| `LayerManifest` / artifact manifest | Released carrier identity and bindings | Must point to release/evidence state |
| `PromotionDecision` / `ReleaseManifest` | Governed state transition and released set | Append-only decision plane |
| `CorrectionNotice` / rollback record | Correction, withdrawal, supersession, and rollback lineage | First-class public-state control |

### Current implementation checkpoints

- [`packages/evidence-resolver/README.md`](../../packages/evidence-resolver/README.md) documents a bounded deterministic no-network candidate resolver with synthetic fixtures and tests. It is explicitly non-authoritative and not a public production resolver.
- [`packages/maplibre/README.md`](../../packages/maplibre/README.md) documents a package scaffold and admission holds, not a functional admitted renderer adapter.
- [`apps/governed-api/README.md`](../../apps/governed-api/README.md) establishes an app boundary; current routes, DTOs, middleware, deployment, and operational behavior remain `NEEDS VERIFICATION`.
- [`apps/explorer-web/README.md`](../../apps/explorer-web/README.md) documents a real workspace and bounded fixture-first projections; live transport, admitted renderer, deployment, release, and public availability remain held or unknown.

[Back to top](#top)

---

## 8. Responsibility-root map

### Root classes at the pinned base

The active [`root_registry.yaml`](../../control_plane/root_registry.yaml) is a machine projection of accepted Directory Rules, not independent authority.

| Class | Roots | Current meaning |
|---|---|---|
| Platform | `.github/` | GitHub automation and collaboration surface |
| Canonical | `apps/`, `configs/`, `connectors/`, `contracts/`, `control_plane/`, `data/`, `docs/`, `examples/`, `fixtures/`, `infra/`, `migrations/`, `packages/`, `pipeline_specs/`, `pipelines/`, `policy/`, `release/`, `runtime/`, `schemas/`, `scripts/`, `tests/`, `tools/` | Accepted responsibility roots |
| Compatibility | `artifacts/` | Transitional/generated compatibility surface; must not become release authority |
| Deprecated | `catalog/` | Converges toward `data/catalog/`; no new authority |
| Conditional / HOLD | `src/` | Requires explicit build-system proof or ADR; default convergence target `packages/` |

### Placement rule

A path is an authority claim. Choose one owning responsibility root first, then refine by lifecycle, execution role, scope, exposure, mutability, and retention. Domains are lanes inside responsibility roots, not new root folders.

Examples:

```text
docs/domains/<domain>/...
contracts/domains/<domain>/...
schemas/contracts/v1/domains/<domain>/...
policy/domains/<domain>/...
fixtures/domains/<domain>/...
tests/domains/<domain>/...
data/<lifecycle>/<domain>/...
```

[Back to top](#top)

---

## 9. Governed public path

```text
released EvidenceBundle + policy/review/release state
    -> governed API or released public-safe artifact
    -> Explorer / map / Evidence Drawer / Focus Mode / export
```

Normal public clients must not directly read:

- RAW, WORK, or QUARANTINE material;
- unreleased candidates or canonical/internal stores;
- internal proof, receipt, or review stores as public truth;
- direct model-runtime output;
- sensitive exact geometry hidden only by client styling;
- a graph, vector index, tile, scene, summary, or dashboard as sovereign truth.

MapLibre, PMTiles, MVT, COG, GeoParquet, graph projections, search indexes, dashboards, scenes, screenshots, stories, exports, and AI answers are downstream carriers. Each consequential public claim must remain traceable to evidence, policy, review, release, correction, and rollback appropriate to significance.

See [trust membrane](../doctrine/trust-membrane.md), [governed API](./governed-api/README.md), [map shell](./map-shell.md), and [governed AI](./governed-ai/README.md).

[Back to top](#top)

---

## 10. Current maturity

| Surface | Current bounded status | What is not proved |
|---|---|---|
| Directory governance | **CONFIRMED:** ADR-0029 accepted; Directory Rules v2 and machine root projection present | Complete recursive conformance and absence of all drift |
| Architecture documentation | **CONFIRMED:** architecture folder and connected doctrine exist | That every document is current, accepted, or implementation-backed |
| Data lifecycle | **CONFIRMED:** canonical lanes and root contract exist | Live source activation, full promotion, public release, storage operations |
| Evidence resolver | **CONFIRMED BOUNDED:** no-network candidate slice with fixtures/tests | Accountable production authority, canonical lookup, public contract, runtime service |
| Governed API | **CONFIRMED BOUNDARY:** app root and README exist | Current route graph, authn/authz, policy/evidence binding, deployment, health |
| Explorer Web | **CONFIRMED BOUNDED:** workspace and fixture-first projections exist | Live governed transport, admitted renderer, full shell, deployment, publication |
| MapLibre package | **CONFIRMED SCAFFOLD:** placeholder package surface exists | Functional adapter, pinned dependencies, consumer, renderer admission |
| Release | **CONFIRMED CONTROL ROOT:** append-only decision root and fixture-first profiles exist | Authenticated operational promotion, signing custody, public release, rollback drill |
| Deployment and operations | **UNKNOWN / NEEDS VERIFICATION** | Hosting, secrets, network exposure, logs, SLOs, backups, incident response, public availability |

The repository is neither “only conceptual” nor “fully operational.” It contains real bounded implementation slices and extensive governance surfaces, while several trust-critical integrations remain explicitly held, proposed, or unverified.

[Back to top](#top)

---

## 11. Invariants and acceptance

### Cross-plane invariants

1. EvidenceBundle outranks generated language and rendered carriers.
2. Public clients use governed interfaces or released public-safe artifacts.
3. Promotion is a governed state transition, not a path move, commit, pull request, merge, badge, or deployment.
4. Receipts, proofs, catalogs, reviews, decisions, manifests, corrections, rollbacks, and published artifacts remain distinct families.
5. Unknown rights, sovereignty, sensitivity, or harmful precision fails closed.
6. Deterministic identity, replay, and correction lineage are preferred where practical.
7. Watchers and drift detectors may propose work; they do not publish.
8. Docs describe and connect authority; they do not manufacture it.

### A proof-bearing slice is real only when it demonstrates

- admitted source identity or an explicitly synthetic fixture boundary;
- stable object identity and schema/contract closure;
- resolvable evidence support;
- policy, rights, sensitivity, and review outcomes;
- deterministic positive and negative fixtures;
- catalog/proof/receipt separation;
- a release decision and rollback/correction target where publication is claimed;
- governed API or released artifact delivery;
- trust-visible UI behavior with finite negative states;
- replay, correction, or rollback evidence proportionate to the claim.

A green test, attractive map, draft PR, generated receipt, or documentation badge does not independently satisfy that burden.

[Back to top](#top)

---

## 12. Open verification

| Priority | Verification item | Evidence needed |
|---|---|---|
| Q1 | Independent stewardship and separation of duties | Current accountable owner/reviewer assignments tied to executable repository routes |
| Q2 | Governed API runtime closure | Route tree, DTOs, middleware, authn/authz, policy/evidence bindings, tests, logs, deployment, health |
| Q3 | Explorer live composition | Governed transport, route tree, map boot, released layer flow, Evidence Drawer continuity, Focus Mode, deployment proof |
| Q4 | Renderer admission | Accepted decision, dependency/lock policy, supply-chain evidence, adapter tests, consumer and export proof |
| Q5 | Evidence resolver graduation | Accountable ownership, accepted contracts, authoritative repository lookup and digest binding, governed consumer |
| Q6 | Root and lifecycle convergence | Recursive closure for deprecated `catalog/`, conditional `src/`, triplet variants, and recorded drift |
| Q7 | Operational release and correction | Authenticated release authority, review separation, signing custody, correction propagation, cache invalidation, rollback drill |
| Q8 | Source and public-use posture | Current source terms, rights, sensitivity, sovereignty, precision transforms, and domain review |
| Q9 | Deployment and operations | Hosting, network exposure, secrets, observability, health, backup/restore, incident response, public probe |

Record unresolved items in the [drift register](../registers/DRIFT_REGISTER.md), [verification backlog](../registers/VERIFICATION_BACKLOG.md), issue, ADR, or decision packet appropriate to the owning question. Do not silently resolve them in this map.

[Back to top](#top)

---

## 13. Related documents

### Architecture and doctrine

- [`README.md`](./README.md) — architecture-folder contract
- [`SKELETON_MAP.md`](./SKELETON_MAP.md) — root, lifecycle, and authority orientation
- [`system-context.md`](./system-context.md) — actors and external boundaries
- [`contract-schema-policy-split.md`](./contract-schema-policy-split.md) — meaning, shape, and admissibility split
- [`governed-api/README.md`](./governed-api/README.md) — intended trust-membrane architecture
- [`map-shell.md`](./map-shell.md) — map shell and click-to-evidence design
- [`governed-ai/README.md`](./governed-ai/README.md) — bounded AI design
- [`deployment-topology.md`](./deployment-topology.md) — runtime and exposure design
- [`spatial-foundation.md`](./spatial-foundation.md) — spatial representation foundation
- [Directory Rules](../doctrine/directory-rules.md), [lifecycle law](../doctrine/lifecycle-law.md), [trust membrane](../doctrine/trust-membrane.md)

### Decisions and current boundaries

- [ADR index](../adr/INDEX.md) and [accepted ADR-0029](../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [Root registry](../../control_plane/root_registry.yaml) and [CODEOWNERS](../../.github/CODEOWNERS)
- [`data/README.md`](../../data/README.md) and [`release/README.md`](../../release/README.md)
- [`apps/governed-api/README.md`](../../apps/governed-api/README.md)
- [`apps/explorer-web/README.md`](../../apps/explorer-web/README.md)
- [`packages/evidence-resolver/README.md`](../../packages/evidence-resolver/README.md)
- [`packages/maplibre/README.md`](../../packages/maplibre/README.md)

---

## Rollback

This update changes one architecture document and its paired generated provenance receipt. Rollback is to revert the feature-branch commit, restore the prior `SYSTEM_MAP.md` blob `6f760580bda6c23a6c227b3dd36edeaa7d34d9e0`, remove the paired receipt through the same reviewed revert, and rerun the same documentation and hosted checks. No source, lifecycle, release, deployment, or public artifact depends on this documentation change by itself.

---

<sub>**Last reviewed:** `2026-08-18` · **Document version:** `v2` · **Role:** architecture orientation · **Base:** `main@70d2f1da3a480e14a19573ebec55258fc64e5f8e` · **Publication authority:** none</sub>

[Back to top](#top)

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/8dbf6d44-1ac0-4a5e-a1d6-1e87923da719
title: Core Glossary
type: standard
version: v1
status: draft
owners: kfm-core
created: 2026-03-01
updated: 2026-03-01
policy_label: public
related:
  - docs/MASTER_GUIDE_v13.md
  - docs/templates/
  - docs/architecture/
  - docs/domains/core/
  - data/
  - contracts/
tags: [kfm, glossary, domain-core]
notes:
  - Source-of-truth for core vocabulary used across schemas, pipelines, APIs, and UI.
[/KFM_META_BLOCK_V2] -->

# Core Glossary

![status](https://img.shields.io/badge/status-draft-yellow) ![policy](https://img.shields.io/badge/policy_label-public-brightgreen)

**Purpose:** Provide a single governed vocabulary for KFM core concepts so schemas, tests, pipelines, APIs, and UX stay consistent.

> **Rule:** If you need to define a term in another doc, prefer linking here instead.

## Navigation
- [Status tags](#status-tags)
- [System invariants](#system-invariants)
- [Truth path & zones](#truth-path--zones)
- [Identity, versions, artifacts](#identity-versions-artifacts)
- [Evidence & citations](#evidence--citations)
- [Policy & governance](#policy--governance)
- [Stories & UI trust surfaces](#stories--ui-trust-surfaces)
- [Time semantics](#time-semantics)
- [Catalog triplet (DCAT/STAC/PROV)](#catalog-triplet-dcatstacprov)
- [Diagram](#diagram)

---

## Status tags

- **CONFIRMED:** vocabulary and meaning are treated as non-negotiable invariants/contracts.
- **PROPOSED:** recommended pattern/wording; may change, but aligns with KFM posture.

---

## System invariants

### Trust membrane (CONFIRMED)
**Definition:** Clients never access storage/DB directly; all access goes through governed APIs applying policy, redaction, and logging.

### Governed API / PEP (Policy Enforcement Point) (CONFIRMED)
**Definition:** The runtime boundary that enforces policy before serving data, resolving evidence, rendering bundles, or returning tiles/queries.

### Cite-or-abstain (CONFIRMED)
**Definition:** If a claim cannot be tied to resolvable evidence (EvidenceRefs/EvidenceBundles) under policy, the system must abstain or reduce scope.

---

## Truth path & zones

### Truth path lifecycle (CONFIRMED)
**Definition:** The auditable lifecycle that moves data from upstream acquisition through zones and gates to governed runtime surfaces.

### Upstream (CONFIRMED)
**Definition:** External sources (open data portals, sensors, remote sensing archives, files) that KFM ingests or references.

### RAW (CONFIRMED)
**Definition:** Immutable acquisition copy of upstream payloads plus checksums; append-only.

### WORK / QUARANTINE (CONFIRMED)
**Definition:** Intermediate transforms and QA where failures are isolated; artifacts may be rewritten.

### PROCESSED (CONFIRMED)
**Definition:** Publishable artifacts in standardized formats with stable IDs and checksums.

### CATALOG / TRIPLET (CONFIRMED posture; PROPOSED profiles)
**Definition:** Cross-linked DCAT + STAC + PROV (and run receipts), describing metadata, assets, and lineage.

### PUBLISHED (CONFIRMED)
**Definition:** Governed runtime surfaces that serve only promoted dataset versions.

---

## Identity, versions, artifacts

### Dataset (CONFIRMED)
**Definition:** A logical dataset identity, such as "USGS NWIS (Kansas)" or "NOAA Storm Events." 

### DatasetVersion (CONFIRMED)
**Definition:** An immutable version of a dataset that corresponds to a specific promoted output set. A dataset can have many versions over time.

### Artifact (CONFIRMED)
**Definition:** A concrete file or object (GeoParquet, PMTiles, COG, JSONL, PDF) produced by a run and referenced by STAC/DCAT/PROV.

### Digest-addressed artifact (PROPOSED)
**Definition:** An artifact referenced by cryptographic digest (e.g., `sha256:...`) rather than (or in addition to) a mutable path.

### spec_hash (PROPOSED; recommended)
**Definition:** A deterministic hash computed from a canonical representation of a dataset spec, used to prevent "hash drift" and support signature verification/caching.

---

## Evidence & citations

### EvidenceRef (CONFIRMED)
**Definition:** A stable reference to evidence, using explicit schemes such as `dcat://`, `stac://`, `prov://`, `doc://`, `graph://`. The evidence resolver must be able to resolve an EvidenceRef in bounded calls.

### EvidenceBundle (CONFIRMED)
**Definition:** The resolved evidence view returned by the evidence resolver. It contains both human-readable and machine-readable fields, plus policy decision results.

### Evidence resolver (CONFIRMED)
**Definition:** A service/API that accepts an EvidenceRef (or structured reference), applies policy, and returns an EvidenceBundle; it fails closed if unresolvable or unauthorized.

### Resolvable citation (CONFIRMED)
**Definition:** A citation that can be opened by the UI (via EvidenceRef → EvidenceBundle) without guessing or manual lookup.

---

## Policy & governance

### PDP (Policy Decision Point) (PROPOSED; recommended)
**Definition:** The component that evaluates policy (e.g., OPA/Rego) and produces allow/deny + obligations + reason codes.

### policy_label (CONFIRMED)
**Definition:** The primary access-control and sensitivity classification input used for policy evaluation.

### Policy decision (CONFIRMED)
**Definition:** The output of policy evaluation: allow/deny, obligations, and reason codes (for auditing and UX).

### Obligation (redaction/generalization) (CONFIRMED)
**Definition:** A required transformation that makes an output safe to publish (e.g., generalize geometry, remove fields) rather than a hard deny.

### default-deny (PROPOSED defaults aligned to posture)
**Definition:** Deny unless explicitly allowed; treat sensitive-location and restricted datasets as deny-by-default unless policy permits a safe public derivative.

### Promotion Contract (CONFIRMED)
**Definition:** The minimum set of gates that must pass before a dataset version can be promoted to PUBLISHED.

### Run receipt / run_record (CONFIRMED)
**Definition:** A record emitted for every pipeline run (and Focus Mode query) containing inputs, outputs, environment, validation results, and policy decisions.

### Audit ledger (CONFIRMED)
**Definition:** An append-only log of governance-relevant events (runs, promotions, policy decisions). It is treated as a governed dataset itself (with redactions applied as needed).

---

## Stories & UI trust surfaces

### Story Node (CONFIRMED)
**Definition:** A versioned narrative bound to map state. A Story Node version includes narrative markdown, citations (EvidenceRefs), saved map state (camera, layers, time window, filters), plus policy label and review state.

### Map state (CONFIRMED)
**Definition:** The reproducible snapshot of map view + layers + filters + time window captured with Stories and used to replay analysis.

### Evidence drawer (CONFIRMED concept; PROPOSED UI details)
**Definition:** A shared UI panel that surfaces evidence details (license, dataset version, provenance, policy badge) and provides one-click access to citations.

### Focus Mode (CONFIRMED concept)
**Definition:** A governed Q&A workflow: policy pre-check → admissible evidence retrieval → evidence bundle creation → answer synthesis → citation verification hard gate → audit run receipt.

---

## Time semantics

### event time (PROPOSED)
**Definition:** When something happened (e.g., flood peak).

### valid time (PROPOSED)
**Definition:** The time a statement is considered true (e.g., a county boundary existed from X to Y).

### transaction time (PROPOSED)
**Definition:** When KFM recorded or published the data.

---

## Catalog triplet (DCAT/STAC/PROV)

### DCAT (CONFIRMED)
**Definition:** Answers: "What is this dataset? Who published it? What is the license? What are the distributions?"

### STAC (CONFIRMED)
**Definition:** Answers: "What assets exist? What are their spatiotemporal extents? Where are the files?"

### PROV (CONFIRMED)
**Definition:** Answers: "How were these outputs created? Which inputs, which tools, which parameters?"

---

## Diagram

```mermaid
flowchart LR
  Upstream[Upstream]
  RAW[RAW]
  WORK[WORK / Quarantine]
  PROC[PROCESSED]
  CAT[CATALOG / TRIPLET]
  PUB[PUBLISHED]

  Upstream --> RAW --> WORK --> PROC --> CAT --> PUB

  subgraph Gates[Promotion Contract gates]
    GA[Gate A: Identity and versioning]
    GB[Gate B: Licensing and rights metadata]
    GC[Gate C: Sensitivity and obligations]
    GD[Gate D: Triplet validation]
    GE[Gate E: QA thresholds]
    GF[Gate F: Run receipt and audit]
    GG[Gate G: Release manifest]
  end

  CAT -. must satisfy .-> Gates
  Gates -. required for promotion .-> PUB

  subgraph Trust[Trust membrane]
    Client[Clients: UI, tools]
    PEP[Governed API / PEP]
    Stores[Stores: PostGIS / object]
  end

  Client --> PEP --> Stores
  Stores --> PEP --> Client

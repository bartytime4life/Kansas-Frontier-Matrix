# 🧱 KFM Domain Contracts v2 (MCP Gates)

![Contracts](https://img.shields.io/badge/contracts-domain%2Fv2-6f42c1)
![Gates](https://img.shields.io/badge/gates-policy--as--code%20%7C%20fail--closed-111827)
![Evidence](https://img.shields.io/badge/evidence-STAC%20%2B%20DCAT%20%2B%20PROV-22c55e)
![Surfaces](https://img.shields.io/badge/surfaces-pipelines%20%7C%20graph%20%7C%20API%20%7C%20UI%20%7C%20AI-0ea5e9)

Contracts that define **what “real, shippable domain data” means** in Kansas Frontier Matrix (KFM) — and what the **gates** must enforce before anything gets ingested, published, or shown to users. 🧾🛡️

> [!IMPORTANT]
> **Contract-first** means contracts are the boundary. If an object crosses a boundary (pipeline → catalog, catalog → graph, API → UI, AI → user), it must have a **v2 contract** + pass gates.

---

## 🧭 Table of Contents

- [What lives here](#-what-lives-here)
- [Why domain contracts exist](#-why-domain-contracts-exist)
- [Design principles](#-design-principles)
- [Contract families](#-contract-families)
- [The v2 envelope (required fields)](#-the-v2-envelope-required-fields)
- [Gates that use these contracts](#-gates-that-use-these-contracts)
- [Canonical examples](#-canonical-examples)
  - [Dataset (Evidence Triplet bridge)](#dataset-evidence-triplet-bridge)
  - [Story Node (Evidence Manifest + PROV)](#story-node-evidence-manifest--prov)
  - [Pulse Thread (timely narrative update)](#pulse-thread-timely-narrative-update)
  - [Run Manifest (determinism receipt)](#run-manifest-determinism-receipt)
  - [Gate Decision (machine-verifiable outcome)](#gate-decision-machine-verifiable-outcome)
- [Versioning & compatibility](#-versioning--compatibility)
- [How to add / change a contract](#-how-to-add--change-a-contract)
- [See also](#-see-also)
- [Definition of Done](#-definition-of-done)

---

## 📦 What lives here

**Expected layout** (this README documents the contract surface; your repo may add more helpers over time):

```text
mcp/
└─ 🚦 gates/
   └─ 📜 contracts/
      └─ 🧩 domain/
         └─ 🧬 v2/
            ├─ 📂 schemas/        # 📐 JSON Schema source of truth (v2 contracts; breaking changes allowed vs v1)
            ├─ 📂 examples/       # 🧪 Example instances (known-pass/known-fail) used by CI + docs + generators
            ├─ 📂 vocab/          # 🧾 Controlled vocabularies (licenses, sensitivity labels, themes, enums)
            ├─ 📂 docs/           # 📚 Optional deeper notes/diagrams (rationale, migration notes, edge cases)
            └─ 📄 README.md       # 👈 you are here 📌 v2 overview: goals, differences from v1, and adoption plan
```

---

## 🎯 Why domain contracts exist

KFM is a multi-surface system (pipelines, catalogs, graph, API, UI, AI). Domain contracts ensure:

- **Interoperability** 🔌: contracts are shared between Python pipelines, Neo4j graph ingestion, API responses, UI renderers, and AI tooling.
- **Evidence-first publishing** 🧾: nothing is “official” until its metadata + lineage is present.
- **Governance & ethics by default** 🧠🛡️: licensing, sensitivity, CARE considerations, and redaction rules are enforced automatically.
- **Reproducibility** 🧪: runs produce deterministic receipts (manifests, hashes, provenance) so work can be replayed and audited.
- **Federation readiness** 🌐: contracts make it possible to exchange domain objects across regions/instances without losing meaning.

> [!NOTE]
> KFM’s mental model is often summarized as:
>
> **“PostGIS stores geo truth (vectors/rasters), Catalogs describe the assets, Graph links the context.”** 🗺️🕸️📚  
> Domain contracts are the glue that keeps those layers consistent.

---

## 🧠 Design principles

### ✅ Contract-first
- Contracts are **first-class artifacts**.
- Any change to a contract implies **versioning + compatibility checks**.
- Code adapts to contracts — not the other way around.

### ✅ Evidence-first
- Published data requires the **Evidence Triplet**: **STAC + DCAT + PROV**.
- Narratives require a **machine-readable Evidence Manifest** + PROV links.

### ✅ Fail closed
- If a gate can’t validate something, it rejects it.
- Vocabularies (licenses, sensitivity levels, governance flags) only expand via PR.

### ✅ API boundary enforcement
- The UI never “reaches around” the API to hit stores directly.
- Contracts assume a **governed API layer** that applies policy, redaction, and auth.

### ✅ Deterministic pipelines
- ETL and simulation outputs should be reproducible (fixed seeds, stable configs).
- Runs produce canonicalized manifests + digests.

---

## 🧩 Contract families

This folder is “domain” on purpose: these are shared objects that show up across KFM subsystems.

### 1) 🧱 Core primitives
- **IDs & References** (`KfmId`, `EntityRef`, `ArtifactRef`)
- **Time** (`TimeRange`, `TimeInstant`, `TimeGranularity`)
- **Space** (`GeoExtent`, `GeometryRef`, `CRSRef`)
- **Links** (`Link`, `ExternalRef`)

### 2) 📚 Evidence Triplet bridge
- **Dataset** (DCAT-like dataset record)
- **Collection / Item / Asset** (STAC-like records)
- **Provenance bundle refs** (PROV JSON-LD pointers, run IDs)

### 3) 🕸️ Knowledge graph entities
- **Place / Region**
- **Event**
- **Person / Organization**
- **Concept** (including *Conceptual Attention Nodes* used by UI + AI)

### 4) 📖 Narrative content
- **StoryNode** (markdown-driven narratives with map/data bindings)
- **EvidenceManifest** (YAML/JSON list of evidence with hashes, queries, transforms)
- **PulseThread** (timely, geotagged micro-narratives)

### 5) 🧪 Simulation & what-if
- **SimRunSpec** / **SimRunResult** (sandboxed scenario modeling outputs)
- **Diff / Patch artifacts** produced by sim-runs

### 6) 🚦 Gate artifacts
- **RunManifest** (inputs, outputs, tool versions, counts, digests)
- **GateDecision** (allow/deny + reasons + policy pack identity)

---

## 📦 The v2 envelope (required fields)

Every v2 contract instance should follow the same basic “envelope” so gates can treat objects uniformly.

```json
{
  "$schema": "kfm.domain.v2/<contract>.schema.json",
  "contract_version": "2.0.0",
  "type": "<ContractType>",
  "id": "urn:kfm:<namespace>:<slug>",
  "meta": {
    "title": "Human readable title",
    "tags": ["optional", "searchable"],
    "created_at": "2026-01-23T00:00:00Z",
    "created_by": "urn:kfm:agent:human|service|ai",
    "updated_at": "2026-01-23T00:00:00Z",
    "source_refs": ["optional external refs or repo paths"]
  },
  "governance": {
    "license": "CC-BY-4.0",
    "sensitivity": "public",
    "care_label": "Public",
    "access": "public",
    "attribution": ["Provider / Author names"]
  },
  "provenance": {
    "prov_ref": "data/prov/<...>.jsonld",
    "run_ref": "urn:kfm:run:<digest-or-ulid>"
  },
  "extensions": {}
}
```

> [!TIP]
> Use `extensions` for experimental fields. Keep the core stable; let innovation move fast without breaking old readers.

---

## 🚦 Gates that use these contracts

Below is the **minimum practical gate set** that should be able to operate purely from these domain contracts (plus policy rules).

| Gate 🚦 | What it blocks 🧯 | Contract surfaces 🧩 |
|---|---|---|
| 🧩 Schema Gate | malformed JSON/YAML, missing required fields | all `schemas/*` |
| 🧾 Evidence Triplet Gate | datasets missing STAC/DCAT/PROV | `Dataset`, `Collection`, `Item`, `Asset` |
| 🧬 Provenance Gate | broken lineage, orphan activities/entities | `provenance.*`, `RunManifest` |
| 🪪 License Gate | unlicensed content | `governance.license` |
| 🔒 Sensitivity Gate | leaks (sacred sites, endangered species coords, PII) | `governance.sensitivity`, redaction hints |
| 🤖 Citation Gate | AI/narratives with claims but no sources | `StoryNode`, `PulseThread`, `EvidenceManifest`, AI outputs |
| 🧪 Determinism Gate | runs without receipts / non-replayable configs | `RunManifest`, `SimRun*` |
| 🧯 Secrets Gate | committed credentials / tokens | any free-text fields |
| 🧊 Artifact Signature Gate | unsigned artifacts promoted to “published” | `ArtifactRef.signature` (if used) |

---

## 🧷 Canonical examples

### Dataset (Evidence Triplet bridge)

```json
{
  "$schema": "kfm.domain.v2/dataset.schema.json",
  "contract_version": "2.0.0",
  "type": "Dataset",
  "id": "urn:kfm:dataset:county-boundaries",
  "meta": {
    "title": "Kansas County Boundaries",
    "tags": ["boundaries", "admin", "kansas"],
    "created_at": "2026-01-23T00:00:00Z",
    "created_by": "urn:kfm:agent:pipeline:ingest-boundaries"
  },
  "governance": {
    "license": "CC-BY-4.0",
    "sensitivity": "public",
    "care_label": "Public",
    "access": "public",
    "attribution": ["Kansas GIS Provider"]
  },
  "evidence_triplet": {
    "stac_ref": "data/stac/collections/county-boundaries.json",
    "dcat_ref": "data/catalogs/dcat/datasets/county-boundaries.json",
    "prov_ref": "data/prov/runs/2026-01-23_ingest-boundaries.jsonld"
  },
  "spatial": {
    "bbox": [-102.0517, 36.9930, -94.5884, 40.0032],
    "crs": "EPSG:4326"
  },
  "temporal": {
    "start": "2020-01-01",
    "end": "2020-01-01",
    "granularity": "day"
  },
  "extensions": {}
}
```

---

### Story Node (Evidence Manifest + PROV)

**Story Nodes are narrative artifacts**, but they’re still governed and auditable.

A typical pattern is a Markdown story with YAML front-matter pointing to:
- an **Evidence Manifest** (YAML/JSON),
- a **PROV JSON-LD** bundle for lineage.

```markdown
---
id: "urn:kfm:story:dust-bowl-overview"
title: "Dust Bowl: Causes, Impacts, and Kansas Context"
status: "draft"
time:
  start: "1930-01-01"
  end: "1940-01-01"
place_refs:
  - "urn:kfm:place:kansas"
evidence_manifest: "evidence/EM-84.yaml"
prov_bundle: "evidence/PROV-84.jsonld"
license: "CC-BY-4.0"
sensitivity: "public"
care_label: "Public"
---

## Summary 🧭
A short narrative summary goes here with inline citations like [1], [2].

## Citations 🧾
1. Dataset: `urn:kfm:dataset:...`
2. Archive: `urn:kfm:doc:...`
```

> [!IMPORTANT]
> A gate should be able to verify:
> - every citation token maps to an Evidence Manifest entry,
> - every Evidence Manifest entry resolves to a known dataset/document (or a checksummed artifact),
> - the PROV bundle references the same entities.

---

### Pulse Thread (timely narrative update)

Pulse Threads are **short, geotagged updates** designed to surface emergent patterns (human-authored or AI-drafted, but always reviewable).

```json
{
  "$schema": "kfm.domain.v2/pulse_thread.schema.json",
  "contract_version": "2.0.0",
  "type": "PulseThread",
  "id": "urn:kfm:pulse:drought-early-signs-2026-01",
  "meta": {
    "title": "Early drought indicators in select watersheds",
    "tags": ["pulse", "drought", "hydrology"],
    "created_at": "2026-01-23T00:00:00Z",
    "created_by": "urn:kfm:agent:watcher:hydro-anomaly"
  },
  "governance": {
    "license": "CC-BY-4.0",
    "sensitivity": "public",
    "care_label": "Public",
    "access": "public",
    "attribution": ["KFM Watcher", "Human Curator"]
  },
  "geo": {
    "region_refs": ["urn:kfm:watershed:huc8:10260005"]
  },
  "as_of": "2026-01-23T00:00:00Z",
  "content": {
    "format": "markdown",
    "body": "Several gauges show 7-day flows in the lowest decile... [1][2]"
  },
  "evidence_manifest": "evidence/EM-PT-2026-01.yaml",
  "provenance": {
    "prov_ref": "data/prov/pulses/drought-early-signs-2026-01.jsonld",
    "run_ref": "urn:kfm:run:sha256:<digest>"
  }
}
```

---

### Run Manifest (determinism receipt)

A run manifest is the “receipt” for a pipeline execution: inputs, outputs, parameters, tool versions, counts, and a stable digest.

```json
{
  "$schema": "kfm.domain.v2/run_manifest.schema.json",
  "contract_version": "2.0.0",
  "type": "RunManifest",
  "id": "urn:kfm:run:sha256:<canonical_digest>",
  "canonical_digest": "sha256:<canonical_digest>",
  "started_at": "2026-01-23T00:00:00Z",
  "ended_at": "2026-01-23T00:03:12Z",
  "actor": "urn:kfm:agent:pipeline:ingest-boundaries",
  "inputs": [
    { "ref": "https://example.org/source.zip", "digest": "sha256:<...>" }
  ],
  "outputs": [
    { "ref": "data/processed/boundaries/counties.geojson", "digest": "sha256:<...>" }
  ],
  "tool_versions": {
    "python": "3.12.x",
    "gdal": "3.x",
    "kfm-pipeline": "v0.x"
  },
  "summary_counts": {
    "records_in": 105,
    "records_out": 105,
    "warnings": 0,
    "errors": 0
  },
  "extensions": {}
}
```

---

### Gate Decision (machine-verifiable outcome)

Gates should produce structured outcomes so the system can:
- show a clear reason for rejection,
- store audit trails,
- support “promote” workflows.

```json
{
  "$schema": "kfm.domain.v2/gate_decision.schema.json",
  "contract_version": "2.0.0",
  "type": "GateDecision",
  "id": "urn:kfm:gate-decision:2026-01-23T00-03-20Z:policy-pack@sha256:<...>",
  "gate_id": "license+provenance+evidence",
  "target_ref": "urn:kfm:dataset:county-boundaries",
  "decision": "allow",
  "evaluated_at": "2026-01-23T00:03:20Z",
  "policy_pack": {
    "name": "kfm-policy-pack",
    "digest": "sha256:<...>"
  },
  "reasons": [],
  "warnings": [],
  "extensions": {}
}
```

---

## 🔁 Versioning & compatibility

### Contract versioning
- Contracts follow semantic intent:
  - **MAJOR**: breaking shape/meaning change (new required fields, changed semantics)
  - **MINOR**: backward-compatible additions (new optional fields, new enum values via vocab PR)
  - **PATCH**: clarifications, docs, non-breaking tightenings

### v1 → v2 migration mindset
- Prefer **adapters** at boundaries (ports/adapters style) rather than “flag days”.
- Keep `extensions` as an escape hatch to avoid churn.

> [!TIP]
> If you must break: add a `MIGRATION.md` beside schemas and include:
> - field-by-field mapping,
> - examples before/after,
> - update notes for gates/policies.

---

## 🛠️ How to add / change a contract

1. **Define the intent** 🎯  
   What boundary does this cross (pipeline, graph, API, UI, AI)? What gates should enforce it?

2. **Update / add JSON Schema** 🧩  
   Place in `./schemas/` with clear naming.

3. **Add at least 2 examples** 🧪  
   - a minimal valid example
   - a realistic full example (with governance + provenance populated)

4. **Update policy rules (if needed)** 🚦  
   Schema validates shape. Policies validate meaning (licenses, sensitivity, evidence requirements).

5. **Run validation locally** ✅  
   Use your standard JSON Schema validator + policy gate runner (OPA/Conftest or equivalent).

6. **PR with a tight diff** 🔍  
   Contracts are shared APIs — keep changes reviewable.

---

## 🔗 See also

These are the “north star” docs that inform v2 contract choices:

- 🧭 **Architecture & system contracts**
  - `Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design`
  - `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation`
  - `Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖`
  - `Kansas Frontier Matrix – Comprehensive UI System Overview`
  - `📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide`

- 🧠 **Governance, evidence-first storytelling, and future expansions**
  - `Additional Project Ideas` (Pulse Threads, Evidence Manifests, canonical run manifests, OCI artifacts)
  - `Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM)`
  - `🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals`

- 🧰 **Reference libraries / research packs (PDF portfolios)**
  - `AI Concepts & more`
  - `Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas`
  - `Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl`
  - `Various programming langurages & resources 1`

---

## ✅ Definition of Done

For any PR touching **domain/v2** contracts:

- [ ] Schema updated (and still readable) 🧩  
- [ ] Examples updated (min + realistic) 🧪  
- [ ] Gates/policies updated if semantics changed 🚦  
- [ ] Evidence Triplet expectations remain intact (STAC/DCAT/PROV) 🧾  
- [ ] Sensitivity + CARE handling reviewed 🔒  
- [ ] Migration notes included if compatibility changes 🔁  
- [ ] Review checklist completed by a maintainer 👀  

---


---
title: "🚀 Kansas Frontier Matrix — Dataset Promotion & Release Governance"
path: "docs/governance/promotion/README.md"
version: "v11.2.6"
last_updated: "2025-12-13"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council · Reliability & Security Board"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Governance & Architecture Guide"
intent: "dataset-promotion-saga"
header_profile: "standard"
footer_profile: "standard"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

governance_ref: "../ROOT-GOVERNANCE.md"
ethics_ref: "../../faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../sovereignty/INDIGENOUS-DATA-PROTECTION.md"

classification: "Public"
sensitivity: "Low"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
jurisdiction: "US-KS"
indigenous_rights_flag: true
data_steward: "FAIR+CARE Council"

commit_sha: "<latest-commit-hash>"
signature_ref: null
provenance_chain:
  - "docs/governance/promotion/README.md@v11.2.6"

doc_uuid: "9b84fd7a-6f8b-4b83-bd8b-9accc9f2e65b"
semantic_document_id: "urn:kfm:doc:governance:dataset-promotion:v11.2.6"
event_source_id: "urn:kfm:event_source:docs:governance:promotion"

ai_transform_permissions:
  - "summarize"
  - "extract-metadata"
  - "generate-checklists"
  - "generate-non-normative-examples"
ai_transform_prohibited:
  - "alter-normative-requirements"
  - "invent-governance-status"
  - "fabricate-provenance"
  - "generate-release-signatures-or-attestations"
---

# 🚀 Dataset Promotion & Release Governance

## 📘 Overview

**Purpose**  
Define the canonical KFM dataset promotion lifecycle that moves data assets from internal processing into **trusted, signed, attested, published, and cataloged releases**.

Dataset promotion in KFM exists to:

- Guarantee **cryptographic trust** of released datasets
- Preserve **full lineage and provenance** across environments
- Enforce **FAIR + CARE + sovereignty** constraints before exposure
- Prevent partial or ambiguous releases
- Enable **safe rollback without data erasure**

**Promotion is a deterministic saga**  
Promotion is enforced as a deterministic saga: every step is ordered, replayable, auditable, and compensatable (rollback-safe), without destructive deletes.

**Core terms (normative)**
- **dataset_id**: stable dataset identifier (string; stable across versions)
- **dataset_version**: immutable version label for one dataset build (string; content-addressed where possible)
- **promotion_id**: idempotency key for a single end-to-end promotion attempt (string; stable across retries)
- **release_id**: immutable identifier for an externally discoverable release packet (string; derived from content digest + governance context)
- **stage**: one of `sign`, `attest`, `publish`, `catalog`
- **terminal state**: `succeeded` or `failed` (with an auditable reason), optionally followed by `compensated`

**Promotion lifecycle (ordered stages)**
1. **Sign**
2. **Attest**
3. **Publish**
4. **Catalog**

Each stage:
- Is idempotent (safe to retry)
- Emits OpenLineage + PROV‑O events
- Records immutable audit artifacts
- Has a defined compensation action (rollback without erasure)

---

## 🗂️ Directory Layout

Promotion governance is expressed in repository layout expectations for artifacts, logs, and catalogs.

~~~text
📁 KansasFrontierMatrix/
├── 📁 docs/                                      — Documentation layer (governance, standards, guides)
│   ├── 📁 governance/                             — Governance docs (authority + enforcement)
│   │   ├── 📄 ROOT-GOVERNANCE.md                  — Governance charter (binding authority)
│   │   └── 📁 promotion/                          — Dataset promotion governance (this doc)
│   │       └── 📄 README.md                       — ← Dataset Promotion & Release Governance
│   ├── 📁 faircare/                               — FAIR+CARE guidance (stewardship + ethics)
│   └── 📁 sovereignty/                            — Indigenous data protection + sovereignty policy
│
├── 📁 data/                                      — Data layer (raw → processed → released + cataloged)
│   ├── 📁 sources/                                — Source manifests (license/rights, checksums, access)
│   ├── 📁 processed/                              — Deterministic ETL outputs (pre-promotion)
│   ├── 📁 releases/                               — Immutable release packets (post-promotion)
│   ├── 📁 stac/                                   — STAC Collections/Items (discovery)
│   └── 📁 dcat/                                   — DCAT records (publication interoperability)
│
├── 📁 mcp/                                       — Reproducibility + run records
│   └── 📁 runs/                                   — Promotion run logs/config snapshots (saga traces)
│
└── 📁 .github/
    ├── 📁 workflows/                              — CI/CD workflows (validation + promotion automation)
    └── 📁 lineage/                                — CI lineage emission patterns (PROV‑O JSON‑LD)
        └── 📄 README.md                           — Single-job lineage emission guide
~~~

---

## 🧭 Context

KFM treats “release” as a **governed claim**: a dataset is not “published” merely because files exist. A dataset becomes **trusted** only after promotion completes with full auditability and governance gates.

**Environment semantics**
- **dev**: iteration and experimentation; artifacts may be mutable
- **staging**: rehearsal of promotion; must be replayable; gates enforced
- **production**: immutability and discoverability; catalog aliasing and rollback required

**Non-goals**
- Promotion does not authorize exposure of restricted knowledge.
- Promotion does not weaken sovereignty protections (it strengthens enforceability and audit).

---

## 🧪 Validation & CI/CD

Promotion must be continuously enforced by CI and runtime validators.

**Minimum validation expectations (policy-aligned)**
- Schema and metadata validity (required front-matter keys, required dataset metadata)
- License validation and compatibility
- Indigenous sensitivity classification and sovereignty checks
- PII and restricted-knowledge scanning (including protected-site leakage controls)
- Determinism/replayability checks (pipeline contract compliance)
- Provenance completeness checks (OpenLineage + PROV‑O coverage per stage)

**Lineage emission (required)**
Each promotion stage emits:
- An OpenLineage event (per stage boundary)
- A PROV‑O bundle or stage-scoped PROV entity graph

CI jobs SHOULD also emit a job-local provenance artifact following the CI lineage convention (see `.github/lineage/README.md`).

**Failure handling (normative)**

| Failure Point | Result |
|--------------|--------|
| Pre-sign gate | Promotion blocked (no stage side-effects permitted) |
| Sign failure | Retry or abort; emit auditable terminal state |
| Attest failure | Signature retained; publish blocked; emit auditable terminal state |
| Publish failure | Attestation retained; catalog blocked; emit auditable terminal state |
| Catalog failure | Release remains non-discoverable; emit auditable terminal state |

All failures MUST produce a terminal, auditable state and MUST NOT rely on destructive deletion for “cleanup.”

---

## 📦 Data & Metadata

Promotion is governed by **explicit artifacts** and **machine-validated metadata**.

### Required artifacts per stage (normative)

**1) Sign**
- Dataset content digest (SHA‑256)
- Signature artifact (Sigstore/Cosign or governed equivalent)
- Signature reference (URI or content-addressed path)

**2) Attest**
- SLSA provenance attestation (or governed equivalent)
- Input dataset references + checksums
- Pipeline version, environment hashes, and reproducibility evidence
- SBOM references (when applicable)

**3) Publish**
- Content-addressed artifact paths (immutable)
- Release manifest entry (immutable)
- Storage tier and residency compliance record (jurisdiction-aware)

**4) Catalog**
- STAC Item/Collection updates (versioned)
- DCAT Dataset/Distribution updates (versioned)
- PROV‑O lineage edges linking released artifacts to processing inputs
- Graph ingestion inputs for Neo4j entities/relationships

### Release manifest expectations (normative)

A release manifest SHOULD be a single machine-readable document that binds:
- dataset_id, dataset_version, promotion_id, release_id
- stage completion timestamps
- digests for all release assets
- signature references
- attestation references
- catalog record references (STAC/DCAT ids)
- governance gates evaluated + outcomes

Example (non-normative shape):

~~~json
{
  "dataset_id": "example.dataset",
  "dataset_version": "2025-12-13",
  "promotion_id": "prom_01JH9YXXXXXXX",
  "release_id": "rel_sha256_abcdef...",
  "digests": {
    "dataset": "sha256:...",
    "manifest": "sha256:..."
  },
  "sign": {
    "status": "succeeded",
    "signature_ref": "cosign://..."
  },
  "attest": {
    "status": "succeeded",
    "attestation_ref": "attest://..."
  },
  "publish": {
    "status": "succeeded",
    "artifact_root": "data/releases/example.dataset/rel_sha256_abcdef..."
  },
  "catalog": {
    "status": "succeeded",
    "stac_ref": "data/stac/example.dataset/collection.json",
    "dcat_ref": "data/dcat/example.dataset.jsonld"
  }
}
~~~

### No destructive deletes (normative)

Rollback is implemented via:
- Deny-lists / tombstones (logical removals)
- Alias pointer rollback (catalog pointer to prior trusted version)
- Superseding records (revocations or withdrawals) that remain auditable

---

## 🌐 STAC, DCAT & PROV Alignment

Promotion outputs MUST remain interoperable through the KFM STAC/DCAT/PROV profiles.

### STAC (discovery)

Catalog stage SHOULD produce:
- A STAC Collection for the dataset lineage (stable `collection.id`)
- A STAC Item per released dataset_version (stable, versioned `item.id`)
- Assets that point to immutable release artifacts (content-addressed where possible)

### DCAT (publication interoperability)

Catalog stage SHOULD produce:
- A DCAT Dataset record for dataset_id
- One or more Distributions representing:
  - the released artifact package(s)
  - associated metadata/manifest
  - license and access constraints

### PROV‑O (lineage)

Promotion stages map naturally to PROV:
- `prov:Entity`: raw inputs, processed outputs, released artifacts, catalogs
- `prov:Activity`: sign/attest/publish/catalog actions (each stage)
- `prov:Agent`: CI runner, pipeline service, signing authority, governance councils (as applicable)

Required relationship patterns:
- `prov:used` (stage consumes prior entities)
- `prov:generated` (stage produces artifacts)
- `prov:wasAssociatedWith` (agent responsibility)
- `prov:wasDerivedFrom` (released dataset derives from processed artifacts)

---

## 🧱 Architecture

Dataset promotion is a **saga** with strict ordering, idempotency, and compensations.

### Promotion lifecycle (saga model)

All datasets must pass the following ordered stages:

1. **Sign**
2. **Attest**
3. **Publish**
4. **Catalog**

Each stage:
- Is idempotent
- Emits OpenLineage + PROV‑O events
- Records immutable audit artifacts
- Has a defined compensation (rollback) action

### Stage definitions

#### 1) 🔐 Sign

**Objective**  
Establish cryptographic identity and integrity.

**Outputs**
- Dataset digest (SHA‑256)
- Signature artifact (Sigstore / Cosign)
- Signature reference (URI or governed path)

**Governance gates**
- License validation
- Indigenous sensitivity classification
- PII & restricted-knowledge scans

**Compensation**
- Signature revocation or superseding invalidation record
- Trust-list exclusion (no destructive deletes)

#### 2) 🧾 Attest

**Objective**  
Bind dataset to its production context.

**Outputs**
- SLSA provenance attestation
- Input datasets + checksums
- Pipeline version & environment hashes
- SBOM references (if applicable)

**Governance gates**
- Pipeline contract validation (KFM‑PDC)
- Reproducibility score ≥ policy threshold

**Compensation**
- Superseding “withdrawn” attestation linked by `promotion_id`

#### 3) 📦 Publish

**Objective**  
Release immutable artifacts into governed storage.

**Outputs**
- Content-addressed artifact paths
- Write-once object storage records (or governed equivalent)
- Release manifest entry

**Governance gates**
- Storage tier approval
- Jurisdictional data residency rules

**Compensation**
- Logical tombstone (deny-list)
- Pointer rollback to prior trusted version

#### 4) 🗂 Catalog

**Objective**  
Expose dataset through discovery and graph systems.

**Outputs**
- STAC Item / Collection
- DCAT Dataset / Distributions
- PROV‑O lineage edges
- Neo4j graph entities

**Governance gates**
- Metadata completeness checks
- FAIR/CARE labeling
- Public-safety review (if applicable)

**Compensation**
- Revert catalog alias to previous version
- Retain historical catalog records (no erasure)

### Exactly-once guarantees

KFM promotion enforces exactly-once semantics through:
- End-to-end idempotency keys (`promotion_id`)
- Transactional outbox pattern
- Content-addressed storage
- Versioned catalog aliasing

No stage may introduce side effects without a persisted saga state update.

---

## ⚖ FAIR+CARE & Governance

Promotion governance explicitly enforces:
- Indigenous data sovereignty controls
- NHPA §304 restrictions (where applicable)
- Jurisdictional export and residency constraints
- License compatibility matrices
- Ethical risk classifications and access constraints

**Non-bypass rule (normative)**  
No dataset may bypass promotion stages. Any exposure channel (API, catalog, graph, download) MUST point only to datasets in a terminal `succeeded` promotion state (or an approved exception explicitly recorded in governance with provenance).

---

## 🕰️ Version History

| Version | Date | Notes |
|-------:|------|-------|
| v11.2.6 | 2025-12-13 | Canonical saga governance alignment; normalized KFM-MDP v11.2.6 headings/metadata; clarified artifact expectations, idempotency, and non-destructive rollback. |

---

<div align="center">

[⬅️ Back to Governance Index](../README.md) · [⬅️ Back to Data Architecture](../../architecture/repo-focus.md) · [⬅️ Back to ROOT-GOVERNANCE](../ROOT-GOVERNANCE.md)

[🏛️ Governance Charter](../ROOT-GOVERNANCE.md) · [🤝 FAIR+CARE Guide](../../faircare/FAIRCARE-GUIDE.md) · [🪶 Indigenous Data Protection](../../sovereignty/INDIGENOUS-DATA-PROTECTION.md)

</div>

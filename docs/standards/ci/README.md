---
title: "🚦 KFM — CI Standards & Provenance Index"
path: "docs/standards/ci/README.md"
version: "v11.2.6"
last_updated: "2025-12-10"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability Engineering Guild · FAIR+CARE Council"
content_stability: "stable"

doc_kind: "Standard Index"
status: "Active / Enforced"
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

scope:
  domain: "ci-standards"
  applies_to:
    - "ci"
    - "github-actions"
    - "provenance"
    - "coverage-telemetry"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM Reliability Engineering Guild"

commit_sha: "<latest-commit-hash>"
signature_ref: "../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../../releases/v11.2.6/github-infra-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/actions-library-v11.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../governance/ROOT-GOVERNANCE.md"
ethics_ref: "../faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../sovereignty/INDIGENOUS-DATA-PROTECTION.md"

doc_uuid: "urn:kfm:doc:standards:ci:index:v11.2.6"
semantic_document_id: "ci-standards-index-v11.2.6"
event_source_id: "ledger:kfm:doc:standards:ci:index:v11.2.6"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
---

<div align="center">

# 🚦 **CI Standards & Provenance Index**  
_Entry point for CI / GitHub Actions / PROV‑O lineage in the Kansas Frontier Matrix_

[Status: Active](https://img.shields.io/badge/Status-Active-brightgreen "Status: Active & Enforced")

</div>

---

## 📘 Overview

This README is the **index and routing table for all CI / GitHub Actions standards** under `docs/standards/ci/`. It follows KFM‑MDP v11.2.6, which requires a predictable H2 sequence (`📘 Overview` → `🗂️ Directory Layout` → … → `🕰️ Version History`) and emoji‑formatted directory trees fenced with `~~~text`.   

The CI standards in this directory:

- Anchor CI in the **core KFM pipeline**  
  > Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j → API → React/MapLibre/Cesium → Story Nodes → Focus Mode :contentReference[oaicite:1]{index=1}  
- Treat **provenance (PROV‑O), coverage, and test results** as first‑class entities in our catalogs and graph.   
- Enforce **DevSecOps, FAIR+CARE, and sovereignty** constraints in CI (no secrets, no PII, no over‑precise coordinates for sensitive sites).   

Use this document when you need to:

- Discover which CI standards exist and where to find them.
- Understand how CI test lineage and coverage roll up into **STAC/DCAT catalogs and Neo4j**.
- Add or modify CI workflows in `.github/workflows/` **without breaking governance**.

---

## 🗂️ Directory Layout

> **Authoring note:** Per KFM‑MDP v11.2.6, directory layouts use `~~~text` fences and emoji icons; never backtick fences. :contentReference[oaicite:4]{index=4}  

~~~text
📂 docs/
└─ 📂 standards/
   └─ 📂 ci/
      ├─ 📄 README.md                        # this index
      ├─ 📄 prov-test-lineage.md             # PROV-O lineage for per-job + workflow aggregates
      └─ 📂 examples/
         ├─ 📄 job-lineage.example.jsonld    # sample per-job PROV-O JSON-LD
         └─ 📄 workflow-aggregate.example.jsonld
📂 .github/
└─ 📂 workflows/
   └─ 📄 ci.yml                              # primary CI pipeline (tests, lineage, telemetry)
📂 artifacts/
└─ 📂 tests/
   └─ <run-id>/
      ├─ 📄 junit.xml                        # test results
      ├─ 📄 coverage.xml                     # coverage report
      └─ 📂 prov/
         ├─ 📄 job-<job-id>.jsonld           # per-job lineage docs
         └─ 📄 workflow-aggregate.jsonld     # per-run aggregate lineage
📂 schemas/
└─ 📂 prov/
   └─ 📄 ci-test-lineage-v1.json             # JSON schema for CI PROV lineage validation
~~~

The directory structure is intentionally **parallel** to the CI pipeline described in the main KFM documentation: code and data live in `src/` and `data/`, CI definitions in `.github/workflows/`, artifacts in `artifacts/`, and schemas under `schemas/` for validation and governance.   

---

## 🧭 Context

KFM’s CI/CD model uses GitHub Actions to enforce **testing, schema validation, provenance, and deployment** on every change. :contentReference[oaicite:6]{index=6} This CI standards area sits between:

- **MCP / Master Coder Protocol** — ensuring reproducible, config‑driven workflows and experiment‑grade rigor for tests.   
- **KFM security & sovereignty policy** — SBOMs, SLSA attestations, vulnerability scanning, and Indigenous sovereignty safeguards.   
- **STAC/DCAT/PROV standards** — CI artifacts (test reports, coverage, lineages) are cataloged as datasets and distributions, with PROV‑O entities/activities linking to commits and runs.   

This README defines **how CI standards are organized and how they plug into**:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j → API → React/MapLibre/Cesium → Story Nodes → Focus Mode :contentReference[oaicite:10]{index=10}  

---

## 🧪 Validation & CI/CD

The CI standards in this directory cover three main concerns:

1. **Test Execution & Lineage (prov-test-lineage.md)**  
   - Models each test job as a `prov:Activity` with explicit `prov:startedAtTime` / `prov:endedAtTime`, inputs (commit + environment) and outputs (JUnit + coverage artifacts). :contentReference[oaicite:11]{index=11}  
   - Emits **per‑job** and **per‑workflow aggregate** JSON‑LD documents into `artifacts/tests/<run-id>/prov/`.  
   - Enables audit‑grade lineage for CI runs and coverage trends across time.

2. **Schema & Policy Validation** (normative behavior, referenced here)  
   - CI workflows validate:
     - Markdown against KFM‑MDP (front‑matter, headings, directory layouts).   
     - STAC, DCAT, and PROV JSON against their schemas.   
     - SBOMs and SLSA attestations for supply‑chain integrity. :contentReference[oaicite:14]{index=14}  

3. **Telemetry & Governance**  
   - CI runs produce telemetry (`github-infra-telemetry.json`) that records:
     - Test status, coverage deltas, security scan results.   
     - Energy and carbon footprint subsets for CI workloads.   

**Planned / recommended standards for this area (backlog):**

- `stac-validation-ci.md` — CI profile for STAC Item/Collection validation and publication.
- `security-ci-guardrails.md` — mapping CI workflows to SECURITY.md and Scorecards checks.   

These are design targets; they may not yet exist in the repo and should be added through normal governance review.

---

## 📦 Data & Metadata

CI generates a **lot of data**. This README standardizes how we think about it:

- **Provenance documents** (`*.jsonld`) are modeled as `prov:Entity` instances describing CI `prov:Activity` runs. :contentReference[oaicite:18]{index=18}  
- **Test and coverage reports** (`junit.xml`, `coverage.xml`) are treated as **DCAT Distributions** of an internal “CI results” Dataset:
  - Dataset: “KFM CI Test & Coverage Results”.
  - Distributions: per‑run files referenced via `dcat:distribution` with checksums aligned to SPDX patterns.   
- **Schemas** under `schemas/prov/` provide **machine‑checkable contracts** for lineage JSON‑LD, enabling CI schema validation before artifacts are ingested into catalogs or Neo4j.   

This framing makes CI artifacts **catalog‑native** and **graph‑ready**, not one‑off logs.

---

## 🌐 STAC, DCAT & PROV Alignment

CI standards here follow the same metadata strategy as other KFM assets: **DCAT for cataloging, STAC for spatio‑temporal assets, PROV‑O for lineage**.   

Patterns:

- **DCAT Dataset / Distribution**: CI result collections are modeled as DCAT Datasets with Distributions for each run’s reports and telemetry, using `dct:title`, `dct:description`, `dct:license`, and `dcat:distribution`.   
- **PROV‑O Lineage**: Each CI job is a `prov:Activity` that `prov:used` a repo `prov:Entity` (commit) and generated artifact `prov:Entity` nodes, with timestamps and agents (GitHub Actions runners / workflows). :contentReference[oaicite:23]{index=23}  
- **Graph Ingestion**: Downstream, Neo4j ingests these as typed nodes and relationships (e.g., `:CIJobActivity`, `:CIArtifact`, `:USES_COMMIT`, `:GENERATED_ARTIFACT`), aligning with KFM‑OP v11 and PROV‑O semantics.   

This alignment allows queries like “show all CI runs that produced artifacts for release X” or “which commits are associated with coverage drops in module Y”.

---

## 🧠 Story Node & Focus Mode Integration

Even CI has stories:

- Each major CI standard (like `prov-test-lineage.md`) becomes a **Story Node** in documentation space, explaining lineage design and its implications for trust.   
- CI telemetry and provenance can be surfaced in Focus Mode as:
  - A timeline of coverage changes.
  - An overlay of “risky” commits (coverage drops, failing tests) across the codebase or feature areas.
- Narrative constraints still apply: **no hallucinated results, no fabricated incidents**, and extra care when CI touches datasets governed by Indigenous sovereignty or sensitive ecological / archaeological content.   

This README ensures CI standards are written so Story Nodes can cleanly reference them (stable paths, consistent headings).

---

## ⚖ FAIR+CARE & Governance

CI standards must uphold:

- **FAIR**:  
  - Findable — CI artifacts and schemas live in stable, documented paths (`artifacts/tests/`, `schemas/prov/`). :contentReference[oaicite:27]{index=27}  
  - Accessible — machine‑readable JSON‑LD and JSON schemas; public docs under `docs/standards/`.  
  - Interoperable — DCAT, STAC, PROV‑O, GeoSPARQL for spatial aspects.   
  - Reusable — clear licensing (CC‑BY 4.0) and versioned schemas.

- **CARE & Sovereignty**:  
  - CI telemetry and logs **must not contain PII, PHI, secrets, or precise coordinates of sensitive sites**; those are masked or excluded by design.   
  - Any CI workflow that touches governed data (e.g., archaeological location checks) must follow `sovereignty_policy` and coordinate with the FAIR+CARE Council.

Governance responsibilities:

- **Reliability Engineering Guild**: owns CI standards and approves changes to this directory.
- **Security Council**: reviews CI security guardrails and supply‑chain protections.   
- **FAIR+CARE Council**: ensures that telemetry and provenance respect Indigenous data sovereignty and CARE principles.   

---

## 🕰️ Version History

| Version  | Date         | Author / Guild                 | Summary                                                |
|----------|-------------|--------------------------------|--------------------------------------------------------|
| v11.2.6  | 2025-12-10  | Reliability Engineering Guild  | Initial CI standards index aligned to KFM‑MDP v11.2.6. |

---

<sub>

⬅️ Back to [Docs Root](../../README.md) · 📐 [Standards Index](../README.md) · ⚖️ [Governance Charter](../governance/ROOT-GOVERNANCE.md)

<br/>

© Kansas Frontier Matrix · CC‑BY 4.0 · Aligned with KFM‑MDP v11.2.6 · KFM‑OP v11 · MCP‑DL v6.3

</sub>


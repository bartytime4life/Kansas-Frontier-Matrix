---
title: "Architecture Decision Records (ADR)"
path: "docs/architecture/adr/README.md"
version: "v13.0.0"
last_updated: "2026-01-12"
status: "active"
doc_kind: "README"
license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"

governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
---

<a id="top"></a>

# 🧭📜 `docs/architecture/adr/` — KFM Architecture Decision Records

![ADR](https://img.shields.io/badge/ADR-decision%20log-8250df)
![Architecture](https://img.shields.io/badge/architecture-governed-1f6feb)
![Provenance](https://img.shields.io/badge/provenance-first-0aa3a3)
![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-required-2ea043)
![KFM-MDP](https://img.shields.io/badge/KFM--MDP-v11.2.6-informational)

> **ADRs are the “why” behind KFM.**  
> If it changes *architecture, contracts, data lineage, security posture, sovereignty posture,* or *operational guarantees*, it should land here.

---

## 🎯 Purpose

This folder contains **Architecture Decision Records (ADRs)** for the Kansas Frontier Matrix (KFM). ADRs:

- ✅ capture *context → decision → consequences* (and alternatives considered)
- ✅ provide a **durable audit trail** for major technical and governance-impacting choices
- ✅ reduce “tribal knowledge” and keep architecture consistent across:
  - 🧱 data pipelines (STAC/DCAT/PROV)
  - 🕸️ knowledge graph (Neo4j + ontology alignment)
  - 🧩 API + contracts (OpenAPI + GraphQL + schemas)
  - 🗺️ web UI (MapLibre/Cesium + Story Nodes + Focus Mode)
  - 🔐 security & compliance (policy gates, SLSA-ish attestations, telemetry)

---

## 🗂️ Directory Layout

```text
docs/architecture/adr/ 🧭📜
├─ README.md                          ✅ (this file)
├─ TEMPLATE.md                         🧩 canonical ADR template
├─ ADR-0001-example-decision.md        🧪 example (keep or delete once real ADRs exist)
├─ ADR-0002-....md                     ➕ add new decisions here
└─ _assets/                            🧷 diagrams/images used by ADRs (optional)
```

---

## 🧱 When an ADR is Required

Create an ADR when a change impacts **one or more** of the following:

### 🧬 Evidence / provenance / catalog contracts
- STAC/DCAT/PROV profile changes
- lineage guarantees, determinism rules, hashing strategy, signing/attestation
- “promotion saga” steps (sign → attest → publish → catalog) behavior changes

### 🧾 Public-facing contracts
- breaking changes to REST/OpenAPI payloads
- GraphQL schema/directive changes
- JSON Schemas that shape API or catalog payloads

### 🏗️ Architecture & infrastructure shape
- database topology (PostGIS/Neo4j), partitioning, replication, indexing strategy
- queue/broker adoption (e.g., Celery/Kafka) or job orchestration posture
- storage format canonicalization (GeoParquet/PMTiles/COGs/etc.)

### 🔐 Security, privacy, sovereignty, policy gates
- authn/authz changes, secrets posture, OPA/Conftest policy semantics
- CARE/Indigenous sovereignty constraints that affect data access or publishing

### 📈 Ops guarantees
- SLOs, observability/telemetry schema changes, error-budget behavior
- backfill strategy, idempotency & replay handling, “kill switch” semantics

> **Rule of thumb:** if someone could reasonably ask “why is it this way?” in 6 months, that’s an ADR.

---

## 🏷️ Naming & Status Rules

### File naming
- `ADR-####-kebab-case-title.md`
- 4 digits, zero-padded: `ADR-0007-...`

### Required statuses
Use one of:
- `proposed`
- `accepted`
- `superseded`
- `deprecated`
- `rejected`

### Superseding
If you supersede a decision:
- create a new ADR that **references** the older one
- update the older ADR’s status to `superseded`
- add a `superseded_by:` pointer

---

## 🧾 ADR Template

Create a new ADR by copying `TEMPLATE.md` and filling it in.

**Minimum bar (must-have sections):**
- Context
- Decision
- Alternatives considered
- Consequences (positive/negative)
- Migration/rollout plan
- Governance & compliance notes

---

## 🚦 Workflow

1. 🧩 **Draft** ADR from template
2. 🔍 **Review** via PR (tag: `architecture`, `governance`, `security` when relevant)
3. ✅ **Accept** by merging + setting status to `accepted`
4. 🧱 **Implement** with references in:
   - PR description (link the ADR)
   - commit message trailer (recommended): `Refs: ADR-00XX`
5. 🧪 **Enforce** with CI gates (recommended)
   - markdown lint
   - schema lint (if contracts affected)
   - policy checks (if security/governance impacted)

---

## 🧠 Decision Quality Checklist

Before merging an ADR, confirm:

- [ ] The *problem* is stated in a way a new contributor can understand
- [ ] The decision is **specific** (not “we should improve X”)
- [ ] Alternatives are real options, not strawmen
- [ ] Consequences include tradeoffs (latency, cost, complexity, risk)
- [ ] Governance links exist when the decision touches FAIR+CARE / sovereignty
- [ ] Rollout/backout path is described for high-impact changes

---

## 🧪 Recommended CI Guardrails (Optional but Strong)

Add lightweight rules so ADRs stay useful:

- **One ADR per “major” architecture PR**
- **Status must be present**
- **Superseded ADR must declare successor**
- **Contract-breaking PRs must reference an ADR** (OpenAPI/GraphQL/schema changes)

---

## 🧩 `TEMPLATE.md` (canonical)

> Keep the actual template in `docs/architecture/adr/TEMPLATE.md`.  
> This excerpt is here to show structure.

```markdown
---
title: "ADR-0000: <Decision Title>"
status: "proposed"
date: "YYYY-MM-DD"
owners: ["@team-or-handle"]
scope: ["api", "pipelines", "graph", "web", "ops", "governance"]
impacts:
  - "contracts"
  - "provenance"
  - "security"
supersedes: []
superseded_by: []
---

# ADR-0000: <Decision Title>

## Context
What is happening? Why now? What constraints exist?

## Decision
What are we doing? Be crisp and testable.

## Alternatives Considered
- A) ...
- B) ...
- C) ...

## Consequences
### ✅ Positive
- ...

### ⚠️ Negative / Risks
- ...

## Rollout / Migration Plan
- Step 1 ...
- Step 2 ...
- Backout plan ...

## Governance, Ethics, Sovereignty Notes
- FAIR+CARE considerations
- Data sovereignty constraints
- Risk management / approvals

## References
- Links to relevant docs/PRs/issues
```

---

## 📚 Project Evidence Pointers

These are “system context anchors” that often motivate ADRs:

- 📘 KFM system architecture & guide:  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx](file-service://file-PaBDqECcJe7NbC8hvXNGDS)  
- 🌟 Future proposals / roadmap drivers:  [oai_citation:1‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx](file-service://file-QrXwct2pX9kFpqgjtBiijR)  
- 🧾 Repository gap analysis & recommendations:  [oai_citation:2‡Audit of the Kansas Frontier Matrix (KFM) Repository.pdf](file-service://file-1RwSrWXaDb5fnJ5gZX5kS3)  
- 🛰️ Modeling & simulation rigor reference (when ADRs touch M&S credibility):  [oai_citation:3‡Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf](file-service://file-LuWF23hffNAZJaZm2Gzvcd)  

---

## 🔗 Navigation

- ⬅️ Back to **Architecture**: `docs/architecture/README.md`
- ⬅️ Back to **Docs Home**: `docs/README.md`
- 🧑‍⚖️ **Governance Root**: `docs/governance/ROOT_GOVERNANCE.md`

---

## 🧾 Version History

- **v13.0.0** (2026-01-12) — Initial ADR README for KFM v13 architecture cycle.

<a id="bottom"></a>

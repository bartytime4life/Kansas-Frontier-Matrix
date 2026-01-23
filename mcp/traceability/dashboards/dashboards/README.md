# 📊 MCP Traceability Dashboards

![MCP](https://img.shields.io/badge/MCP-Master%20Coder%20Protocol-6f42c1?style=for-the-badge)
![Traceability](https://img.shields.io/badge/Traceability-End--to--End%20Evidence-brightgreen?style=for-the-badge)
![Provenance](https://img.shields.io/badge/Provenance-PROV%20%2B%20STAC%20%2B%20DCAT-2ea44f?style=for-the-badge)
![Policy](https://img.shields.io/badge/Policy--as--Code-OPA%20%2F%20Rego-blue?style=for-the-badge)
![Fail Closed](https://img.shields.io/badge/Gates-Fail--Closed-red?style=for-the-badge)
![KFM](https://img.shields.io/badge/KFM-Kansas%20Frontier%20Matrix-black?style=for-the-badge)

> [!TIP]
> If you’re looking for **“the map behind the map”** 🗺️🧾 — these dashboards are the *proof layer*.

📍 **You are here:** `mcp/traceability/dashboards/dashboards/`

---

## 🧭 Contents

- [What this is](#-what-this-is)
- [Why MCP cares about dashboards](#-why-mcp-cares-about-dashboards)
- [Non-negotiables](#-non-negotiables)
- [Dashboard families](#-dashboard-families)
- [Traceability matrix view](#-traceability-matrix-view)
- [Folder contract](#-folder-contract)
- [Dashboard contract](#-dashboard-contract)
- [Data sources](#-data-sources)
- [How to add a dashboard](#-how-to-add-a-dashboard)
- [Operational conventions](#-operational-conventions)
- [Security, ethics, and access control](#-security-ethics-and-access-control)
- [Backlog](#-backlog)
- [Design inputs](#-design-inputs)

---

## 🧩 What this is

This directory stores **dashboards-as-code** for KFM’s traceability layer.

These dashboards answer questions like:

- ✅ **What data/version** is powering a layer, chart, story node, or AI answer?
- ✅ **Which pipeline run / PR** produced it?
- ✅ **Do we have provenance + catalog artifacts** (PROV/STAC/DCAT) end-to-end?
- ✅ **Which governance/policy rules** are failing, trending, or waived?
- ✅ **Is Focus Mode** meeting citation expectations (coverage, drift, blocked answers)?
- ✅ **Are artifacts tamper-evident** (digests, signatures, attestations)?

---

## 🧪 Why MCP cares about dashboards

MCP (Master Coder Protocol) pushes **scientific-method discipline** into engineering:
hypotheses → experiments → results → reproducibility → auditability.

Dashboards are the **operational face** of that discipline:
they visualize the **traceability matrix** (requirements ↔ code ↔ data ↔ evidence ↔ approvals) so maintainers and governance can act fast. 🧠📈

---

## 🧱 Non-negotiables

> [!IMPORTANT]
> Dashboards are **observability**, not a bypass around governance.

- 🧾 **Evidence-first:** dashboards must rely on governed artifacts (telemetry, catalogs, provenance, policy results) rather than ad-hoc “mystery queries.”
- 🧷 **Provenance-first publishing:** if provenance/citation requirements aren’t met, the platform should behave *fail-closed* (dashboards should clearly show *why*).
- 🧩 **Contract-first:** if data contracts are required upstream, dashboards should visualize contract compliance and drift.
- 🔒 **Respect sensitivity:** do not surface sensitive records/fields in dashboards unless policy allows.

---

## 🗂️ Dashboard families

Below is a **recommended** dashboard catalog. Implement as separate dashboard definitions (Grafana / Superset / custom UI panels — pick your runtime, keep the contract consistent).

### 1) 🚚 Ingestion & Pipeline Health
**Purpose:** Know if the engine is running.

**Key panels**
- Run success rate (hour/day/week)
- Stage latency (ingest → validate → transform → catalog → graph → publish)
- Bytes processed / records added
- Top failure reasons (grouped)
- Energy/carbon metrics (if captured)

---

### 2) 🧾 Provenance & Catalog Coverage
**Purpose:** Know if outputs are **publishable** and traceable.

**Key panels**
- “Missing boundary artifacts” list (STAC/DCAT/PROV)
- Provenance completeness score (per dataset)
- Provenance freshness (time since last PROV activity)
- “Unknown source” = 0 tolerance

---

### 3) 🛡️ Policy Pack Compliance
**Purpose:** Governance as code (OPA/Rego) in motion.

**Key panels**
- Violations over time (by rule)
- Violations per dataset / per run
- Waivers granted (who/when/why; expiry)
- “Fail-closed” events count (blocked publish, blocked answer)

---

### 4) 🏛️ Governance Ledger & Approvals
**Purpose:** Human oversight + signatures + audit.

**Key panels**
- Pending submissions (by council/workflow stage)
- Average time-to-approval
- Approvals by dataset/domain
- Signature/hash verification status (ledger integrity)

---

### 5) 🧠 Graph Integrity & Knowledge Health
**Purpose:** Make the graph *trustworthy*.

**Key panels**
- Orphan node count (no provenance / no edges / dangling refs)
- Schema drift / label explosions
- “Hub” nodes (suspicious degree spikes)
- Lag since last ingestion per domain
- Backup/restore verification (if implemented)

---

### 6) ✍️ Story Nodes & Narrative Evidence
**Purpose:** Keep narratives anchored to evidence.

**Key panels**
- Story nodes with missing citations/manifests
- Stories impacted by dataset updates (blast radius)
- “Evidence artifact” coverage (story ↔ datasets ↔ PROV)

---

### 7) 🤖 Focus Mode / AI Traceability
**Purpose:** Ensure AI is explainable and auditable.

**Key panels**
- Citation coverage (% answers with citations)
- “No answer due to missing source” count (and why)
- Model latency + cost telemetry
- Drift signals (answer changes, citation set changes)
- Audit Panel events (reviewed / flagged / corrected)

---

### 8) 🌦️ Live Dashboards (Public + Internal)
**Purpose:** Support “Monitor Present” mode (sensor feeds, alerts, and operational views).

**Key panels**
- Real-time station status + last reading timestamp
- “Source attribution present” checks (DCAT alignment)
- Threshold alerts (e.g., river level crossings)
- Public-friendly tiles: temp, wind, precipitation + map panel

---

### 9) 📦 Supply Chain & Artifact Signing
**Purpose:** Treat data like code (digests, signatures, attestations).

**Key panels**
- Artifact digest presence + verification results
- Signature verification (cosign) pass/fail
- SBOM/attestation coverage (if adopted)
- Provenance “referrers” attached to artifacts

---

## 🧬 Traceability matrix view

This view is a “one glance” mapping from pipeline stage → artifacts → what we can measure.

| Stage 🧱 | Primary artifacts 🧾 | Example signals 📈 | Dashboard(s) 📊 |
|---|---|---|---|
| Intake | Raw source receipts, checksums | Fetch success, duplicates, licensing flags | Ingestion Health |
| Validation | Policy results, contract checks | Fail-closed counts, top rules | Policy Pack |
| Transform | Processed outputs, run manifest | Reproducibility, config hash | Ingestion Health / Supply Chain |
| Catalog | STAC/DCAT/PROV | Missing artifacts, mismatch | Provenance & Catalog Coverage |
| Graph ingest | Neo4j/PostGIS updates | Orphans, lag, schema drift | Graph Integrity |
| Publish | Governed APIs | Coverage, latency, access gates | Governance / Live Dashboards |
| Narratives | Story manifests + citations | Broken references, blast radius | Story Nodes |
| AI | Answer logs + citations + PROV | Citation coverage, blocked answers | Focus Mode |

---

## 📁 Folder contract

> [!NOTE]
> The outer directory (`mcp/traceability/dashboards/…`) may also contain tooling.  
> The inner `dashboards/` directory is **definitions + assets**.

<details>
<summary><strong>Suggested structure</strong> (click to expand) 📂</summary>

```text
📁 mcp/
  📁 traceability/
    📁 dashboards/
      📁 dashboards/
        📄 README.md
        📁 catalog/                 # dashboard index (human-friendly)
        │  ├─ dashboards.yaml       # inventory: ids, owners, audiences, deps
        │  └─ panels.md             # shared panel patterns + queries
        📁 definitions/             # runtime exports (Grafana/Superset/etc.)
        │  ├─ grafana/              # *.json
        │  ├─ superset/             # *.yaml
        │  └─ custom-ui/            # JSON schema for React panels
        📁 datasources/             # adapters & query specs (NDJSON/SQL/Cypher)
        📁 assets/                  # screenshots, thumbnails, diagrams
        📁 tests/                   # schema checks, policy checks, lint rules
```
</details>

---

## 🧾 Dashboard contract

To keep dashboards consistent across runtimes, every dashboard definition **must** carry core metadata.

```yaml
# dashboards.yaml (inventory)
dashboards:
  - id: kfm.trace.ingestion.health
    title: "🚚 Ingestion & Pipeline Health"
    owner: "data-platform"
    audience: ["maintainers", "governance"]
    sensitivity: "internal"
    refresh: "5m"
    depends_on:
      - telemetry.ndjson
      - run_manifest.json
    slo:
      run_success_rate_24h: ">= 0.98"
      p95_end_to_end_latency: "<= 30m"
    links:
      runbook: "docs/runbooks/ingestion.md"
      policies: "tools/validation/policy"
```

✅ **Rules of thumb**
- `id` must be stable (never recycle IDs)
- include `owner`, `audience`, `sensitivity`, and `depends_on`
- link to a runbook if the dashboard can trigger action

---

## 🔌 Data sources

Dashboards should prefer artifacts that are already “official” in KFM’s ecosystem:

- 🧾 **Telemetry logs** (append-only; NDJSON preferred)
- 🧬 **Run manifests** (canonical, digestable metadata for reproducibility)
- 🏛️ **Governance ledger** (signatures/hashes, approvals, waivers)
- 🗺️ **Boundary artifacts:** STAC + DCAT + PROV
- 🧠 **Graph health reports:** orphans, drift, lag
- 🤖 **AI audit logs:** citations, “no-answer” events, review flags
- 📦 **OCI artifact metadata:** digests, signatures, attestations (optional)

---

## ➕ How to add a dashboard

1) **Write the traceability question** (1 sentence)  
2) **Declare inputs** (which artifacts prove the answer?)  
3) **Define metrics** (names + units + aggregation window)  
4) **Add to inventory** (`dashboards.yaml`)  
5) **Add runtime definition** (Grafana JSON / Superset YAML / custom UI schema)  
6) **Add screenshot** to `assets/` (thumbnail = nice ✨)  
7) **Add tests** (schema lint + policy lint + ID uniqueness)  
8) **Update this README** (catalog table / family list)

✅ **Definition of Done**
- [ ] dashboard has a stable `id`
- [ ] panels are reproducible (no manual-only edits)
- [ ] inputs are governed artifacts (not “mystery queries”)
- [ ] sensitivity label is correct
- [ ] has a runbook link (if operational)
- [ ] passes policy checks + schema checks
- [ ] screenshot exists (optional but recommended)

---

## 🧷 Operational conventions

- **Tag everything**: `domain=hydrology`, `stage=catalog`, `type=policy`, `audience=public/internal`
- **Keep a metric dictionary**: every metric name should have meaning + unit + source
- **Prefer rollups**: raw logs stay raw; dashboards consume rollups to stay fast
- **Version dashboards**: treat as code (PRs + review)

---

## 🔒 Security, ethics, and access control

> [!WARNING]
> Dashboards are a *leak vector* if we’re careless.

- Respect dataset classifications and tiered access
- Redact identifiers where needed (or aggregate)
- Ensure “public dashboards” only use public-safe datasets
- Any waiver should be visible (with expiry) to internal viewers

---

## 🧱 Backlog

- [ ] Create `dashboards.yaml` inventory + schema validation
- [ ] Implement rollup job for telemetry NDJSON → metrics table
- [ ] Implement graph health exporter → `docs/reports/qa/graph_health/`
- [ ] Add Focus Mode citation coverage collector
- [ ] Add governance ledger integrity verifier + dashboard panel
- [ ] Add artifact signature verification panel (cosign)

---

## 📚 Design inputs

This README is shaped by the project’s core architecture, governance, AI explainability, UI dashboard concepts, and MCP traceability practices.

**Core KFM docs**
- Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design
- Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation
- Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖
- Kansas Frontier Matrix – Comprehensive UI System Overview
- 📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide

**MCP + governance + ops**
- Scientific Method / Research / Master Coder Protocol Documentation
- Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities
- MARKDOWN_GUIDE_v13
- Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices

**Idea decks & extensions**
- 🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals
- Additional Project Ideas
- Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM)
- Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design

**Resource packs (research / future tooling)**
- AI Concepts & more (PDF portfolio)
- Data Management / Data Science / Bayesian Methods (PDF portfolio)
- Maps / Virtual Worlds / Archaeological CG / Geospatial WebGL (PDF portfolio)
- Various programming languages & resources (PDF portfolio)
- Data Mining Concepts & applications
- Geospatial Analysis with Python – Cookbook (and related geospatial cookbooks)

---

🧠✨ **If it can’t be traced, it isn’t trusted.**

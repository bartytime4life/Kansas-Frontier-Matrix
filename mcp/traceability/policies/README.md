# 🧾 MCP Traceability Policies (Kansas Frontier Matrix)

![Status](https://img.shields.io/badge/status-draft-informational)
![Policy as Code](https://img.shields.io/badge/policy-as--code-blue)
![OPA](https://img.shields.io/badge/OPA-Rego-7d3f98)
![Conftest](https://img.shields.io/badge/Conftest-CI%20gates-orange)
![Provenance](https://img.shields.io/badge/provenance-first-success)
![FAIR%2BCARE](https://img.shields.io/badge/FAIR%2BCARE-data%20governance-brightgreen)

> 🔍 **Rule of thumb:** If it can’t be traced, it can’t ship.  
> 🧠 **Focus Mode rule:** If it can’t be sourced, it must refuse.

---

## 🎯 Purpose

This folder is the **policy-as-code home** for **MCP (Master Coder Protocol) traceability** across the Kansas Frontier Matrix (KFM): data ingest ➜ transformations ➜ AI outputs ➜ published stories ➜ UI exports.

MCP expects **documentation-first, reproducible, traceable work** (think: “electronic lab notebook for the entire project”), including trace links between **questions/requirements → data → code → results** and a “traceability matrix” view across artifacts. ✅

---

## 🧭 Scope

These policies cover (at minimum):

- 🗃️ **Data assets**: datasets, layers, scans, points, derived products
- 🧬 **Metadata & provenance**: Evidence Triplet (**STAC / DCAT / PROV**) + data contracts
- 🧠 **AI outputs**: Focus Mode narratives, citations, governance ledger entries
- 🗺️ **UI visibility**: “map behind the map”, per-layer provenance & citations
- 🔐 **Security & sensitivity**: cultural protocols, restricted locations, access control, secrets hygiene
- 🧪 **Research & experimentation**: experiment IDs, run manifests, reproducible environments
- 🧱 **Supply chain**: SBOMs, attestations, signing, build lineage

---

## ✅ Non‑negotiables (Ship/No‑Ship Gates)

### 🧾 Evidence & provenance
- ✅ Every published dataset must have:
  - **Data contract** (required fields present)
  - **STAC/DCAT/PROV** coverage (Evidence Triplet)
  - **License** + attribution
  - **Sensitivity** classification when applicable  
- ❌ Missing provenance = **cannot publish** (fail closed)

### 🧠 AI integrity (Focus Mode)
- ✅ If the assistant uses a claim, it must provide a **citation trail** to source material
- ❌ If it cannot source a claim, it must **refuse** or explicitly mark uncertainty

### 🔐 Sensitive data safety
- ✅ Sensitive location info must be **generalized/redacted**
- ✅ Access controls must be applied for restricted materials
- ✅ Cultural protocol review must be honored (CARE-style governance)

---

## 📁 Directory Layout

```text
📁 mcp/
  📁 traceability/
    📁 policies/
      📄 README.md
      📁 rego/              # ✅ OPA/Rego policy rules (policy-as-code)
      📁 tests/             # ✅ Conftest tests + fixtures
      📁 schemas/           # ✅ JSON schemas (contracts, manifests, evidence)
      📁 waivers/           # ⚠️ Time-boxed exceptions (reviewed + expiring)
      📁 docs/              # 📚 Extra policy notes (optional)
```

> 💡 If the repo already has `tools/validation/policy/`, treat **one as the source of truth** and keep them synchronized (symlink, vendoring, or CI copy step).

---

## ⚖️ How Policies Are Enforced

### 1) 🧰 CI gates (pre-merge)
- ✅ Run **Conftest** against catalogs/contracts/manifests.
- ✅ Fail the build for policy violations (severity-based).

### 2) 🚦 Runtime authorization
- ✅ Use **OPA** as a decision point for:
  - publication permission  
  - access control decisions  
  - sensitive dataset export rules  
  - AI output publication rules (ex: “must include citations”)  

### 3) 🧑‍⚖️ Agent guardrails (W‑P‑E)
- ✅ Watcher/Planner/Executor agents must refuse actions that violate policy.
- ✅ Any exception must be explicitly logged (and usually needs approval proof).

---

## 🗂️ Policy Catalog (Categories)

| Category | What it protects | Typical artifacts | Examples (IDs) |
|---|---|---|---|
| 🧾 Contracts | Prevent “mystery data” | `*.contract.json` | `KFM-CONTRACT-*` |
| 🧬 Provenance | End-to-end lineage | `prov/*.jsonld` | `KFM-PROV-*` |
| 🗺️ Geo Validity | CRS/bounds sanity | STAC, raster/vector headers | `KFM-GEO-*` |
| 🏷️ License & Attribution | Legal reuse | license fields + citations | `KFM-LIC-*` |
| 🔐 Sensitivity | Prevent harm | sensitivity tags + ACL | `KFM-SENS-*` |
| 🧠 AI Output | Trustworthy answers | answer bundles + citations | `KFM-AI-*` |
| 🧾 Story Evidence | No unsourced storytelling | evidence manifests | `KFM-STORY-*` |
| 🧪 Experiments | Reproducibility | run manifests, IDs | `KFM-EXP-*` |
| 🧱 Supply Chain | Build integrity | SBOM, attestations | `KFM-SUPPLY-*` |
| 📚 Library Bundles | Indexability | extracted PDFs/MD | `KFM-LIB-*` |

---

## 📦 Required Trace Artifacts

### A) 🗃️ Dataset package (minimum)
A dataset is “publishable” only when it includes:

- `dataset.contract.json` ✅
- `stac/item.json` and/or `stac/collection.json` ✅
- `dcat/dataset.jsonld` (or equivalent DCAT record) ✅
- `prov/activity.jsonld` (or equivalent PROV record) ✅
- `LICENSE` / attribution ✅
- `sensitivity.json` (when applicable) ✅

### B) 🧠 AI answer package (minimum)
When an AI answer is stored/published:

- `answer.md` (human readable)
- `answer.json` (machine readable)
- `citations.json` (source anchors)
- `governance_ledger_entry.json` (policy results + approvals)

### C) 🧾 Story node evidence (minimum)
Every “story node” / narrative element must be backed by an evidence manifest:

- `evidence.yaml` (claims → citations → source files)
- CI validates that every claim has evidence (or is clearly labeled as speculation)

---

## 🧪 Traceability Matrix (MCP)

MCP encourages a “traceability matrix” that connects:

- Experiment / Feature ID
- Code version (commit hash)
- Data version (hash/URI)
- Outputs (model/data artifacts)
- Results reference (figures, reports, story nodes)

📌 Recommended location (adjacent to policies):

```text
📁 mcp/traceability/
  📄 traceability-matrix.csv   # or .md / .json
```

---

## 🧯 Waivers & Exceptions

Waivers are allowed **only** when:

- ✅ They are **time‑boxed** (must expire)
- ✅ They include a **reason**, **risk**, and **mitigation plan**
- ✅ They include the **approver** identity (human/role)
- ✅ They log which artifacts were affected

Suggested waiver structure:

```yaml
waiver_id: WAIVER-2026-001
policy_id: KFM-PROV-002
expires_on: 2026-03-01
reason: "Legacy scan missing complete chain-of-custody metadata"
risk: "Reduced auditability"
mitigation: "Backfill PROV; restrict export until complete"
approved_by: "Data Governance Council"
artifacts:
  - "data/catalog/collections/legacy_scans/*"
```

---

## 🔐 Sensitive Data & Cultural Protocols

When policies detect or label sensitive content:

- ✅ Don’t publish exact locations unless explicitly permitted
- ✅ Apply access control and/or generalization
- ✅ Require cultural protocol review steps where relevant
- ✅ Log all decisions in the governance ledger (including who approved what)

---

## 📚 PDF Portfolios & Reference Bundles

Some project resources are stored as **PDF portfolios** (containers) which are **not indexable** unless extracted.

**Policy rule:** portfolios must be “exploded” into individually searchable files (PDF/MD), and each extracted file must be assigned:
- license/attribution
- classification
- catalog entry (when used for decisions)

---

## 🔗 Project Docs This Policy Pack Aligns With

> 🧠 Treat this list as your **design authority** for traceability + governance.

- 📘 **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation**
- 🏗️ **Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design**
- 🧭🤖 **Kansas Frontier Matrix (KFM) – AI System Overview**
- 🧩 **Kansas Frontier Matrix – Comprehensive UI System Overview**
- 📚 **KFM Data Intake – Technical & Design Guide**
- 🌟 **KFM – Latest Ideas & Future Proposals**
- 💡 **Innovative Concepts to Evolve KFM**
- 🧰 **Additional Project Ideas**
- 🧠📦 **AI Concepts & more** (portfolio bundle)
- 🗃️📦 **Data Management…Bayesian Methods…** (portfolio bundle)
- 🗺️📦 **Maps/GoogleMaps/VirtualWorlds/Geospatial WebGL** (portfolio bundle)
- 🧑‍💻📦 **Various programming languages & resources** (bundle / placeholder)

---

## 🛠️ Maintainer Checklist

- [ ] Policies are versioned and reviewed like code
- [ ] CI runs Conftest gates on PRs
- [ ] Runtime uses OPA decisions for access/publish/export
- [ ] Evidence Triplet is enforced (STAC/DCAT/PROV)
- [ ] Focus Mode outputs include citations or refuse
- [ ] Sensitive content is labeled, restricted, and auditable
- [ ] Waivers expire and are reviewed
- [ ] Governance ledger captures key decisions

---

## ✍️ Contributing a New Policy (Quick Workflow)

1. 🧠 Define scope: what artifact + what risk
2. 🏷️ Assign a stable ID (`KFM-<CATEGORY>-###`)
3. 🧾 Add rule in `rego/`
4. ✅ Add tests in `tests/`
5. 🧪 Add fixtures + expected deny messages
6. 📚 Document rationale + remediation steps
7. 🔁 Ensure waiver path exists (if needed) + expires

---

<details>
<summary>📎 Source anchors used to build this README (for auditability)</summary>

- Automated policy gates across ingestion/AI/publish; fail-closed for missing license/provenance/citations/sensitivity. :contentReference[oaicite:0]{index=0}
- OPA + Conftest “policy pack” approach and repo policy location reference. :contentReference[oaicite:1]{index=1}
- “Contract-first” data contracts and enforced metadata discipline. :contentReference[oaicite:2]{index=2}
- Data intake: immutable raw trust boundary, deterministic pipelines, mandatory provenance & citations. :contentReference[oaicite:3]{index=3}
- STAC/DCAT/PROV mirrored into graph (trace graph backbone). :contentReference[oaicite:4]{index=4}
- AI governance ledger + provenance panel expectation. :contentReference[oaicite:5]{index=5}
- RAG: search results linked back to sources for traceability. :contentReference[oaicite:6]{index=6}
- FAIR+CARE enforcement with W‑P‑E agents refusing unsafe/unsourced actions. :contentReference[oaicite:7]{index=7}
- Supply chain trace: SBOMs + SLSA attestations + signing. :contentReference[oaicite:8]{index=8}:contentReference[oaicite:9]{index=9}
- Story node evidence manifest + CI validation pattern. :contentReference[oaicite:10]{index=10}
- UI provenance + citation surfacing (“map behind the map”). :contentReference[oaicite:11]{index=11}:contentReference[oaicite:12]{index=12}
- Sensitive data generalization + access control + CARE framing. :contentReference[oaicite:13]{index=13}
- Cultural protocol review checklist concept (sensitive handling). :contentReference[oaicite:14]{index=14}
- Vault/secrets management emphasis. :contentReference[oaicite:15]{index=15}
- PDF portfolio “must open in Acrobat” constraint (needs extraction). 
- MCP framing: documentation-first, reproducible, traceability matrix. :contentReference[oaicite:20]{index=20}:contentReference[oaicite:21]{index=21}
- “Audit and attribution policies” and alignment with MCP concepts. 

</details>


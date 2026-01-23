> According to a document from **2026-01-23**, KFM is built on **evidence-first + provenance-first** principles — this folder exists so our dashboards always have a *visual audit trail* (screenshots + metadata) that proves what the system showed, when, and why.  [oai_citation:0‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

# 📸 Dashboards Screenshot Evidence (MCP Traceability)

![Evidence-First](https://img.shields.io/badge/Evidence--First-%F0%9F%94%8E-blue)
![Provenance](https://img.shields.io/badge/Provenance-%E2%9B%93%EF%B8%8F%20enforced-success)
![MCP](https://img.shields.io/badge/MCP-Traceability-orange)
![Dashboards](https://img.shields.io/badge/Dashboards-%F0%9F%93%8A-informational)

📍 **You are here:** `mcp/traceability/dashboards/screenshots/`

This directory stores **screenshots as evidence artifacts** for:
- 📊 traceability dashboards (progress, audits, governance)
- 🧭 provenance/lineage UI views (Layer Info / Layer Provenance)
- 🤖 Focus Mode evidence (citations, audit panel, refusal states)
- 🔭 ingestion + telemetry dashboards (NDJSON logs → charts)
- 🔐 supply chain + artifact provenance views (OCI/cosign/attestations)

KFM’s UI is explicitly designed so users can “trace *the map behind the map*.”  [oai_citation:1‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)

---

## 🧭 Table of contents
- [What belongs in this folder](#-what-belongs-in-this-folder)
- [Golden rules](#-golden-rules)
- [Folder layout](#-folder-layout)
- [Naming convention](#-naming-convention)
- [Screenshot sidecar metadata](#-screenshot-sidecar-metadata)
- [What to capture](#-what-to-capture)
- [Capture standards](#-capture-standards)
- [Sensitive data & redaction](#-sensitive-data--redaction)
- [Manual workflow](#-manual-workflow)
- [Automated workflow](#-automated-workflow)
- [PR checklist](#-pr-checklist)
- [Project file map](#-project-file-map)

---

## ✅ What belongs in this folder

Add screenshots here when they provide **traceable proof** of one or more of the following:

1) **Provenance is visible** (source + license + processing summary)  
- UI must surface provenance and context.  [oai_citation:2‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)

2) **Policies were enforced** (Policy Pack decisions, access control, governance flags)

3) **Focus Mode is evidence-backed** (citations, audit panel, refusal if unsupported)  
- Focus Mode must cite sources and refuse rather than fabricate. 

4) **A run is reproducible** (dataset IDs, run_id, commit SHA, environment)

5) **A dashboard claim is audit-ready** (metrics + source logs + timestamps)  
- Ingestion telemetry is designed as append-only NDJSON to feed dashboards/audits.  [oai_citation:3‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 🥇 Golden rules

> [!IMPORTANT]
> A screenshot without context is **not evidence**. Every screenshot should be paired with a sidecar file describing *what it proves* and *what inputs produced it*.

**Always include (when applicable):**
- ⛓️ **Layer provenance UI** (Layer Info / Layer Provenance panel)  
  - Planned UI includes a “Layer Info” dialog and proposed “Layer Provenance” panel listing citations/metadata.  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- 🕒 **Timestamp** (and ideally “data as-of” time)
- 🧾 **run_id / pipeline run** reference (or CI run)
- 🧠 **Focus Mode citations** (and audit panel if shown)  [oai_citation:5‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
- 🧭 **Map extent + timeframe** if spatial/temporal

**Never commit screenshots that:**
- 🔓 expose restricted/sensitive locations or private attributes
- 🧑‍💻 reveal secrets/tokens/keys
- 🧩 omit provenance/citations for anything presented as “truth”

---

## 🗂 Folder layout

```text
📁 mcp/
  📁 traceability/
    📁 dashboards/
      📁 screenshots/  👈 (this folder)
        🖼️ 2026-01-23__ingestion-gate__success__dev__1920x1080__run-7c2a9f__sha-bb86bf1.png
        🧾 2026-01-23__ingestion-gate__success__dev__1920x1080__run-7c2a9f__sha-bb86bf1.shot.json
        🖼️ 2026-01-23__layer-provenance__multi-layer__stage__1920x1080__run-1a22ee__sha-bb86bf1.png
        🧾 2026-01-23__layer-provenance__multi-layer__stage__1920x1080__run-1a22ee__sha-bb86bf1.shot.json
        📄 README.md
        📄 INDEX.md            (optional gallery)
        📄 screenshots.ndjson   (optional machine-readable index)
```

---

## 🏷 Naming convention

**Filename format (recommended):**
```text
YYYY-MM-DD__<dashboard_or_view>__<scenario>__<env>__<resolution>__run-<run_id>__sha-<shortsha>.png
```

**Examples:**
- `2026-01-23__policy-pack__deny-sensitive-layer__stage__1920x1080__run-9f01c3__sha-bb86bf1.png`
- `2026-01-23__focus-mode__refuses-without-sources__dev__1366x768__run-81aa2d__sha-bb86bf1.png`

**Rules:**
- ✅ lowercase + hyphens only inside segments
- ✅ `__` separates segments
- ✅ no spaces
- ✅ screenshot + sidecar share the same stem

---

## 🧾 Screenshot sidecar metadata

For every `*.png`, add a matching `*.shot.json` (or `*.md`) file.

Why: dashboards must be **auditable**; KFM is designed to keep chain-of-custody and even aims for immutable logs of AI activity.  [oai_citation:6‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

### Sidecar schema (minimal)
```json
{
  "id": "shot_2026-01-23_ingestion-gate_success_run-7c2a9f",
  "captured_at_utc": "2026-01-23T05:44:00Z",
  "captured_by": "human|agent",
  "env": "dev|stage|prod",
  "route_or_view": "/dashboards/ingestion",
  "scenario": "ingestion gate success for dataset X",
  "proves": [
    "ingestion gate passed checksum + schema sanity",
    "telemetry log entry recorded",
    "policy pack decision allow"
  ],
  "run": {
    "run_id": "7c2a9f",
    "commit_sha": "bb86bf1707b50a9d3d43b06896fd387851de92b3",
    "ci_run": "optional-link-or-id"
  },
  "inputs": {
    "datasets": [
      { "dcat_id": "dcat:usgs-nwis", "license": "public-domain|unknown", "sensitivity": "public|restricted" }
    ],
    "stac": [
      { "collection": "river-gauge-observations", "item": "stac:item:..." }
    ],
    "layers": [
      { "layer_id": "hydrology.river_gauge", "source": "USGS NWIS" }
    ]
  },
  "provenance": {
    "prov_bundle": "data/provenance/<bundle>.jsonld",
    "telemetry": "logs/telemetry/ingest.ndjson",
    "policy_decision": "policy/decisions/<id>.json"
  },
  "redaction": {
    "applied": false,
    "notes": ""
  },
  "notes": "Anything unusual, known caveats, or follow-up tasks."
}
```

### Optional: machine index (NDJSON)
Because ingestion/telemetry is already append-only NDJSON by design, screenshots can be indexed the same way for easy dashboards & audits.  [oai_citation:7‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

Create/append:
- `screenshots.ndjson` — one JSON object per screenshot (matching the schema above)

---

## 📊 What to capture

| Dashboard / View | What it proves | Must show | Typical artifacts |
|---|---|---|---|
| 🧪 Ingestion Gate | checksum/schema/metadata gatekeeping + telemetry | gate results + dataset id + timestamp | png + shot.json |
| 📈 Telemetry / Metrics | ingestion events → dashboards | chart + underlying event source link | png + shot.json |
| 🛡️ Policy Pack Decisions | governance enforced | decision output + rule hit + affected dataset/layer | png + shot.json |
| ⛓️ Layer Info / Provenance | “map behind the map” is inspectable | layer source + license + processing summary | png + shot.json |
| 🤖 Focus Mode Answer | citations required | answer + citations + context | png + shot.json |
| 🤖 Focus Mode Refusal | “no speculation” enforced | refusal text + missing-source explanation | png + shot.json |
| 🧬 Story Evidence Manifest | narratives are auditable | manifest panel/list + referenced sources | png + shot.json |
| 🧰 Artifact / Signature View | artifact provenance & signing | digest + signature + attestation | png + shot.json |
| 🏥 Graph Health Checks | integrity, orphan nodes, lag | health summary + query timestamp | png + shot.json |

### Notes on a few key categories

- **Ingestion Gate** should reflect checksum + schema sanity + governance lite checks and telemetry logging.  [oai_citation:8‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- **Layer Provenance** should validate the planned UI commitment: provenance surfaced per layer; proposed panel lists active layers with citations, and sharing/export can auto-attach attribution.  [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- **Story Evidence Manifests** are explicitly proposed to make stories self-documenting with “receipts.”  [oai_citation:10‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
- **Artifact provenance** should include OCI/cosign-style signing and provenance attachments (PROV JSON-LD, run_id).  [oai_citation:11‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 🎛 Capture standards

Use Markdown best practices for images: clear names, keep file sizes reasonable, and prefer vector formats for diagrams when possible.  [oai_citation:12‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)

**Baseline standards (recommended):**
- 🖥️ **Desktop:** 1920×1080 (primary)
- 📱 **Mobile:** 390×844 (if the view is mobile-critical)
- 🎨 Theme: keep consistent (Light or Dark) per dashboard category
- ♿ Include at least one accessibility-mode capture when relevant (high-contrast)  
  - UI emphasizes accessibility (high-contrast modes, semantic HTML/ARIA).  [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

**Screenshot framing checklist:**
- show the dashboard header/title
- show filters/inputs (date range, layer toggles, scenario selection)
- show “data as-of” time (especially for real-time)
- show provenance/citations panels if present
- avoid clutter (close irrelevant side panels)

---

## 🔒 Sensitive data & redaction

KFM is explicitly designed to respect **FAIR + CARE** and handle sensitive content via governance + access controls.  [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

**If a screenshot touches sensitive layers or near-real-time feeds:**
- ✅ confirm the view is from an authorized role (or use a synthetic dataset)
- ✅ redact: blur sensitive attributes, remove identifying popups, generalize coordinates
- ✅ record the redaction method in the sidecar JSON

A proven pattern: **round sensitive coordinates** so the public view shows an approximate area (e.g., ~10 km).  [oai_citation:15‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)

Real-time examples can include **sensitive stations** that should be omitted or limited to authorized users.  [oai_citation:16‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 🧑‍🔬 Manual workflow

1. **Pick a scenario** (success/failure/regression/policy deny)  
2. **Open the dashboard/view** (ensure provenance panels are visible if applicable)  
3. **Set scope**: map extent + time range + active layers  
4. **Capture** screenshot → save with naming convention  
5. **Create sidecar** `*.shot.json` describing what the screenshot proves  
6. **Add to PR** (screenshots are expected for UI changes)  [oai_citation:17‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🤖 Automated workflow (recommended for CI)

MCP guidance pushes reusable templates + consistent logs and traceability across tasks → code → tests → docs.  [oai_citation:18‡Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf](file-service://file-TkRzAfTnxCYDUHauCf1NcH)

If you’re using automated UI tests / visual regression:
- generate screenshots as CI artifacts
- copy stable, reviewed snapshots into this folder as “golden evidence”
- include **commit SHA + CI run_id** in the filename + sidecar
- keep a `screenshots.ndjson` index for dashboards/audits

> [!TIP]
> MCP-oriented repo structure often includes experiment reports and SOPs; consider adding a “Dashboard Evidence Capture” SOP under `mcp/sops/` and reference screenshots here.  [oai_citation:19‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-ShqHKgjxCS9UT9vbcxDNzA)

---

## ✅ PR checklist

- [ ] Screenshot filenames follow the naming convention
- [ ] Each screenshot has a `*.shot.json` (or `*.md`) sidecar
- [ ] Provenance/citations visible where relevant (Layer Info / Layer Provenance / Focus Mode citations)  [oai_citation:20‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- [ ] No sensitive locations/PII leaked; redaction recorded if applied  [oai_citation:21‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)
- [ ] For real-time dashboards, “data as-of” time is visible and consistent with pipeline cadence (if applicable)  [oai_citation:22‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- [ ] PR description links dashboard changes → screenshots → run_id/commit (traceability)  [oai_citation:23‡Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf](file-service://file-TkRzAfTnxCYDUHauCf1NcH)

---

## 🧩 Design rationale (why these rules exist)

- **Provenance-first + no black boxes:** KFM requires that data and insights keep chain-of-custody and are explainable.  [oai_citation:24‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- **Focus Mode evidence:** answers must include citations; otherwise refuse/flag uncertainty. 
- **Telemetry → dashboards:** ingestion logs are append-only NDJSON to power audits and dashboards.  [oai_citation:25‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- **User-visible provenance:** UI supports layer provenance inspection and export attributions.  [oai_citation:26‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- **Evidence manifests:** stories should carry structured “receipts,” enabling audits and impact checks when data changes.  [oai_citation:27‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
- **Security & provenance at build time:** CI can attach attestations/signatures; artifacts can carry provenance refs (run_id, PROV).  [oai_citation:28‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg) [oai_citation:29‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 📚 Project file map

> This README is grounded in the project’s technical and design docs. Key sources (as provided in the repo artifacts):

### Core KFM docs
- 🧭 **AI System Overview** — Focus Mode citations, governance ledger, supply-chain integrity  
   [oai_citation:30‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  [oai_citation:31‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- 🧩 **Comprehensive Architecture, Features, and Design** — provenance enforcement, Layer Provenance panel, governance  
   [oai_citation:32‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  [oai_citation:33‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)
- 🖥️ **Comprehensive UI System Overview** — “map behind the map”, dashboards/live data vision  
   [oai_citation:34‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  [oai_citation:35‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)
- 🧱 **Comprehensive Technical Documentation** — repo layout, provenance files, UI QA/screenshots  
   [oai_citation:36‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  [oai_citation:37‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### Intake + traceability foundation
- 📥 **Data Intake – Technical & Design Guide** — ingestion gate, NDJSON telemetry, streaming governance  
   [oai_citation:38‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  [oai_citation:39‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  [oai_citation:40‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- 🌟 **Latest Ideas & Future Proposals** — provenance-first UI enhancements + dashboards/live extensions  
   [oai_citation:41‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)

### MCP + process docs
- 🧠 **Design Audit – Gaps & Enhancement Opportunities** — MCP directory + traceability dashboards recommendation  
   [oai_citation:42‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
- 🧪 **Open-Source Geospatial Mapping Hub Design** — MCP templates, experiment reporting, SOP patterns  
   [oai_citation:43‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)
- 🧬 **Scientific Method / Research / MCP Documentation** — versioning, changelogs, traceability matrix mindset  
   [oai_citation:44‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

### Governance + ethics references
- 💡 **Innovative Concepts to Evolve KFM** — CARE/TK labels, sensitivity-aware coordinate generalization  
   [oai_citation:45‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  [oai_citation:46‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)
- 🧠 **Additional Project Ideas** — evidence manifests, OCI artifact provenance, trust loops  
   [oai_citation:47‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

### Engineering reference libraries (portfolios / references)
- 🤖 **AI Concepts & more** (PDF portfolio)  [oai_citation:48‡AI Concepts & more.pdf](file-service://file-K6BctJjeUwvyCahLf9qdwr)
- 🌍 **Maps / GoogleMaps / Virtual Worlds / Archaeological / WebGL** (PDF portfolio)  [oai_citation:49‡Various programming langurages & resources 1.pdf](file-service://file-4wp3wSSZs7gk5qHWaJVudi)
- 💻 **Various programming languages & resources** (PDF portfolio)  [oai_citation:50‡Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf](file-service://file-RshcX5sNY2wpiNjRfoP6z6)
- 🧠 **Data Management / Architectures / Bayesian / Programming ideas** (PDF portfolio)  [oai_citation:51‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- ⛏️ **Data Mining Concepts & Applications**  [oai_citation:52‡Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf](file-service://file-RrXMFY7cP925exsQYermf2)
- 🧭 **Python Geospatial Analysis Cookbook** (recipes for validation/overlays/routing)  [oai_citation:53‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)

### Docs writing standards
- ✍️ **Markdown Guide (Syntax, Extensions, Best Practices)**  [oai_citation:54‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)
- 🧾 **Document Refinement Request**  [oai_citation:55‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 🧾 Appendix: quick embed snippet (for docs)

```md
![Ingestion Gate — Success](./2026-01-23__ingestion-gate__success__dev__1920x1080__run-7c2a9f__sha-bb86bf1.png)

*Evidence:* ingestion gate passed + telemetry recorded (see sidecar JSON for run_id + dataset IDs).
```

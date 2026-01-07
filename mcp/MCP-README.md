# 🧠🧭 KFM MCP — Matrix Control Protocol (`mcp/`)
<p align="left">
  <img alt="KFM" src="https://img.shields.io/badge/Kansas%20Frontier%20Matrix-MCP-2b6cb0" />
  <img alt="Governance" src="https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-2ea043" />
  <img alt="Evidence" src="https://img.shields.io/badge/evidence-STAC%20%7C%20DCAT%20%7C%20PROV-845ef7" />
  <img alt="Ops" src="https://img.shields.io/badge/ops-runbooks%20%7C%20SOPs%20%7C%20checklists-111827" />
  <img alt="Security" src="https://img.shields.io/badge/security-deny--by--default-critical" />
  <img alt="Repro" src="https://img.shields.io/badge/reproducibility-run%20manifests%20%7C%20versioning-brightgreen" />
  <img alt="Human" src="https://img.shields.io/badge/human--centered-autonomy%20%7C%20transparency-ff922b" />
</p>

> 🧭 **Purpose:** `mcp/` is KFM’s **operating system** — the governance rules, SOPs, runbooks, templates, and “how we work” norms that keep the platform **truthful, reproducible, secure, and human-centered**.  
> ✅ MCP is not code. It’s the **control plane** for *how* code + data + models are produced, reviewed, and trusted.

---

## 🔗 Quick navigation
- [🎯 What MCP is](#-what-mcp-is)
- [🧱 Non-negotiables (KFM invariants)](#-non-negotiables-kfm-invariants)
- [🗂️ Folder map (recommended)](#️-folder-map-recommended)
- [🧾 Evidence chain standard](#-evidence-chain-standard-stacdcatprov)
- [🏷️ Classification & redaction policy](#️-classification--redaction-policy)
- [🧪 Modeling & simulation governance](#-modeling--simulation-governance)
- [🤖 AI-assisted outputs policy](#-ai-assisted-outputs-policy)
- [🛡️ Security & abuse-resistance](#️-security--abuse-resistance)
- [⚙️ Ops runbooks (dev → prod)](#️-ops-runbooks-dev--prod)
- [✅ Review checklists (fast)](#-review-checklists-fast)
- [🧩 Templates (copy/paste)](#-templates-copypaste)
- [📚 Project file influence map (uses all project files)](#-project-file-influence-map-uses-all-project-files)

---

## 🎯 What MCP is

MCP is the **Matrix Control Protocol** for KFM:

- 🧾 **Governance:** who can publish what, under which classification, and with what evidence
- 🧰 **SOPs:** repeatable procedures for data ingest, cataloging, modeling, exporting, and review
- 🧪 **Rigor:** “don’t fool yourself” discipline for statistics, ML, simulation, and cartography
- 🛡️ **Security:** deny-by-default controls, safe-by-design operations, and incident pathways
- ❤️ **Human-centered:** autonomy, accountability, transparency, and no dark patterns

> [!IMPORTANT]
> MCP’s job is to ensure KFM doesn’t become “a map of vibes.”  
> Everything that ships must be **traceable**, **testable**, and **governed**.

---

## 🧱 Non-negotiables (KFM invariants)

### ⛓️ 1) Canonical pipeline order
**ETL → STAC/DCAT/PROV Catalogs → Graph → API → UI → Story Nodes → Focus Mode**

- If it’s not cataloged + provenance-linked, it’s not publishable. 🏷️🧬
- The graph is a *reference index*, not the source of truth. 🕸️
- The API is the **boundary of trust** (contracts + auth + redaction). 🚪

### 🧾 2) Evidence > vibes
- Every claim must point to evidence (sources + transforms + versions).
- If uncertainty exists, surface it (intervals, diagnostics, assumptions). 📉

### 🔒 3) No privacy downgrade
- Outputs cannot become less restricted than inputs unless a documented redaction step exists.

### 🧪 4) Reproducible by default
- Stable IDs, run manifests, deterministic parameters, and artifact tracking are required for anything that influences decisions.

### ❤️ 5) Human autonomy always
- Models support decisions; they don’t replace accountability.
- AI-assisted outputs are labeled, bounded, and auditable.

---

## 🗂️ Folder map (recommended)

> 🧩 If your repo’s `mcp/` differs, keep the **intent**: policy + procedures + templates + runbooks.

```text
mcp/
├─ 📄 MCP-README.md                      # 📘 you are here
├─ 🧭 00_overview/
│  ├─ 📄 mission.md                      # “why KFM exists” + scope boundaries
│  ├─ 📄 glossary.md                     # shared vocabulary (IDs, catalogs, runs)
│  └─ 📄 principles.md                   # north stars + non-negotiables
├─ 🏷️ 01_governance/
│  ├─ 📄 classification.md               # public/internal/restricted + rules
│  ├─ 📄 redaction.md                    # masking/generalization/deny rules
│  ├─ 📄 licensing.md                    # attribution, allowed licenses, unknown-license policy
│  ├─ 📄 provenance.md                   # STAC/DCAT/PROV requirements + evidence bundles
│  └─ 📄 exceptions.md                   # how to request policy exceptions (rare)
├─ 🧾 02_evidence/
│  ├─ 📄 evidence-bundles.md             # Story/Focus evidence bundle spec
│  ├─ 📄 run-manifests.md                # required fields, examples, storage
│  └─ 📄 catalog-qa.md                   # validation gates for catalogs
├─ 🧪 03_modeling/
│  ├─ 📄 statistics.md                   # EDA, regression, experimental design guardrails
│  ├─ 📄 bayesian.md                     # priors, posteriors, uncertainty reporting
│  ├─ 📄 ml.md                           # model cards, eval, drift, failure modes
│  ├─ 📄 simulation.md                   # V&V, sensitivity, scenario metadata
│  └─ 📄 optimization.md                 # objectives/constraints + artifact discipline
├─ 🗺️ 04_cartography/
│  ├─ 📄 map-design.md                   # symbology, ramps, legends, honesty rules
│  ├─ 📄 mobile-mapping.md               # offline constraints, location sensitivity
│  └─ 📄 webgl-3d.md                     # 3D is optional; coordinate sanity; safe loaders
├─ ⚙️ 05_ops/
│  ├─ 📄 environments.md                 # dev/stage/prod boundaries + secrets posture
│  ├─ 📄 runbooks.md                     # step-by-step ops runbooks
│  ├─ 📄 incident-response.md            # security + data incidents (private path)
│  └─ 📄 backups-restore.md              # backup discipline + encryption posture
├─ 🛡️ 06_security/
│  ├─ 📄 threat-model.md                 # what we assume attackers do
│  ├─ 📄 hardening-checklist.md          # API/UI/script hardening
│  └─ 📄 vuln-reporting.md               # how to disclose responsibly
└─ 🧩 07_templates/
   ├─ 📄 template_dataset_pr.md          # dataset PR checklist + metadata requirements
   ├─ 📄 template_model_run.md           # ML/Stats run report + artifacts
   ├─ 📄 template_simulation_run.md      # scenario + V&V + sensitivity
   ├─ 📄 template_story_node.md          # narrative + citations + evidence bundle refs
   ├─ 📄 template_adr.md                 # architecture decision record
   └─ 📄 template_incident.md            # incident report (private workflow)
```

---

## 🧾 Evidence chain standard (STAC/DCAT/PROV)

### ✅ Publishing rule
A dataset/result is “publishable” only when all are true:

- [ ] Has a stable ID (`dataset_id`, `layer_id`, `run_id`)
- [ ] Has a classification label (`public|internal|restricted`)
- [ ] Has a license/attribution (or is blocked with rationale)
- [ ] Has provenance: **STAC/DCAT/PROV** pointers
- [ ] Has transforms recorded (high-level is fine; not every command line)
- [ ] Has checksums for artifacts (recommended, required for offline bundles)

### 🧬 Evidence bundle (Story Nodes + Focus Mode)
When something becomes a narrative or an AI-assisted explainer, it must reference an **evidence bundle**:
- claim text
- supporting STAC items / PROV runs
- artifact pointers (plots, maps, tables)
- uncertainty (intervals / diagnostics / assumptions)

> [!TIP]
> Evidence bundles are how KFM avoids “trust me bro” map claims.

---

## 🏷️ Classification & redaction policy

### Allowed classifications (default set)
- `public` ✅
- `internal` 🟡
- `restricted` 🔴 *(rare in repo; typically pointer-only)*

### Redaction strategies (choose explicitly)
- ✂️ **Drop**: remove fields entirely
- 🫥 **Mask**: partially hide IDs/strings
- 🧮 **Generalize**: reduce precision (point → county)
- 📉 **Aggregate**: roll up to safe summaries
- ⏳ **Delay**: publish only after review/time threshold
- 🚫 **Deny**: no output (403 or blocked artifact)

### “No privacy downgrade”
If any input is `restricted`, outputs are at least `restricted` unless:
- a documented redaction step exists, AND
- review/approval is recorded, AND
- the resulting risk is explicitly assessed.

---

## 🧪 Modeling & simulation governance

### 📊 Statistics & experiments
Minimum expectations for inference that influences decisions:
- state assumptions (data-generating story)
- show diagnostics (residuals, outliers, coverage)
- report uncertainty (intervals, sensitivity)
- avoid misleading visual choices

### 🎲 Bayesian workflows
- priors are declared
- posterior summaries include credible intervals
- convergence/sanity checks are recorded

### 🧪 Simulation (NASA-grade posture)
- V&V status is explicit (verified/validated/plausible/experimental)
- scenario inputs + constraints are recorded
- sensitivity analysis is performed for key parameters
- runs emit artifacts + provenance pointers

### 🧠 Optimization
- objective + constraints are explicit
- results are tied to versions and inputs
- artifacts include parameter sweeps (when relevant)

---

## 🤖 AI-assisted outputs policy

AI/ML outputs must be:
- labeled as AI-assisted (no silent automation)
- provenance-linked (data + model + config versions)
- bounded (intended use / non-intended use)
- explainable via evidence bundle references

> [!IMPORTANT]
> KFM’s AI posture: **assist, don’t assert**.  
> The system must remain accountable to humans, not the other way around. ❤️

---

## 🛡️ Security & abuse-resistance

### Threat assumptions
- hostile inputs (GeoJSON, uploads, URLs)
- SSRF attempts via “fetch this link”
- injection via query params and metadata
- oversized payloads to crash parsers
- supply-chain drift (deps and scripts)

### Minimum controls
- deny-by-default policy gates
- strict input validation (types, sizes, allowlists)
- no secrets in repos/notebooks/scripts/logs
- safe error messages (no stack traces to clients)
- private vulnerability reporting path

> [!CAUTION]
> If you find a security issue, don’t post it publicly. Use the security policy.

---

## ⚙️ Ops runbooks (dev → prod)

MCP expects runbooks for:
- environment bootstrap (dev)
- DB/graph provisioning (dev/test)
- catalog build + validation + graph sync
- job queue health checks
- backup/restore drills (test-only rehearsals)
- incident response (private workflow)

> ✅ Keep runbooks “copy/paste runnable” with explicit confirmations for destructive steps.

---

## ✅ Review checklists (fast)

### 🗺️ Data layer PR (10-second scan)
- [ ] classification declared
- [ ] license/attribution present
- [ ] provenance pointers exist (STAC/DCAT/PROV)
- [ ] geometry/CRS sanity documented
- [ ] size/perf reasonable (tiles over blobs)
- [ ] no sensitive fields leaked

### 📊 Model run PR
- [ ] assumptions stated
- [ ] diagnostics included (plots/tables)
- [ ] uncertainty reported
- [ ] seed + versions recorded
- [ ] artifacts referenced (not dumped inline)
- [ ] model card / limits included (if ML)

### 🧪 Simulation run PR
- [ ] scenario + constraints recorded
- [ ] V&V status explicit
- [ ] sensitivity analysis present/justified
- [ ] reproducible run manifest attached
- [ ] outputs are cataloged/pointered

### 🛡️ Security scan
- [ ] no secrets in diffs
- [ ] no new risky parsers without bounds
- [ ] external URL usage reviewed (SSRF posture)
- [ ] logs don’t include sensitive payloads

---

## 🧩 Templates (copy/paste)

<details>
<summary><strong>📄 Template: Dataset PR (governed data)</strong></summary>

```markdown
## 📦 Dataset PR — <dataset_id>

### 🎯 Purpose
- What question/use does this dataset support?

### 🏷️ Classification
- `public|internal|restricted`:
- Rationale:

### 📜 License / Attribution
- License:
- Attribution string (if required):
- Source link / archive ref:

### 🧾 Provenance (required)
- STAC:
- DCAT:
- PROV:

### 🗺️ Spatial & temporal metadata
- CRS / EPSG:
- BBox:
- Time coverage:
- Geometry validity checks:

### 🧪 QA
- Validation tools/run output:
- Screenshots (if UI-facing):
- Known limitations:

### ✅ Checklist
- [ ] classification declared
- [ ] license/attribution included
- [ ] provenance pointers included
- [ ] checksums included (if artifacts shipped)
- [ ] no sensitive fields leaked
```

</details>

<details>
<summary><strong>📄 Template: Model run (stats/ML)</strong></summary>

```markdown
## 📊 Model Run — <run_id>

### 🎯 Goal
- What are we predicting/estimating and why?

### 📥 Inputs (evidence)
- dataset_ids:
- STAC/DCAT/PROV pointers:

### 🎛️ Parameters
- seed:
- splits:
- features:
- hyperparams:

### 🧪 Diagnostics
- residuals / calibration / error analysis:
- coverage/missingness:
- failure modes:

### 📉 Uncertainty
- intervals / credible intervals:
- sensitivity notes:

### 📦 Artifacts
- plots:
- metrics:
- model card link (if ML):

### 🏷️ Classification
- output classification:
- propagation rationale:
```

</details>

<details>
<summary><strong>📄 Template: Simulation run (V&V + sensitivity)</strong></summary>

```markdown
## 🧪 Simulation Run — <run_id>

### 🎯 Scenario
- description:
- objective:
- constraints:

### ✅ V&V status
- Verified:
- Validated:
- Experimental:
- Notes:

### 🎛️ Parameters + seeds
- parameters:
- seed(s):
- time step / solver details:

### 📉 Sensitivity analysis
- key parameters tested:
- observed sensitivity:

### 📦 Outputs
- artifacts:
- STAC/DCAT/PROV pointers:
- checksums:
```

</details>

---

## 📚 Project file influence map (uses all project files)

> Requirement: this section maps **every project file** to a concrete MCP responsibility (policy, SOP, template, or runbook expectation).

<details>
<summary><strong>🧠 Expand: Influence map (all project files)</strong></summary>

| Project file | How it shapes MCP (governance, SOPs, runbooks, templates) |
|---|---|
| `Kansas Frontier Matrix (KFM) – Comprehensive Engineering Design.docx` | Defines the overall system invariant pipeline, boundary rules, evidence-first posture, and “what must be governed” across KFM |
| `Latest Ideas.docx` | Converts vision into operational SOPs: what to prototype, how to validate, what to graduate, and what to keep experimental |
| `Data Spaces.pdf` | Drives interoperability and sharing posture: pointer-over-payload, data trust signals, and governance as infrastructure |
| `Introduction to Digital Humanism.pdf` | Establishes human-centered governance: transparency, agency, privacy, accountability, and anti-dark-pattern stance |
| `Principles of Biological Autonomy - book_9780262381833.pdf` | Reinforces autonomy/closure thinking: systems should keep humans in control; build feedback loops and stable controls |
| `On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf` | Adds audit-ready AI governance: labeling, accountability hooks, provenance, and policy-aware claims handling |
| `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf` | Shapes remote sensing SOPs: time-series, compositing, export tracking, and reproducible EO workflows |
| `python-geospatial-analysis-cookbook.pdf` | Anchors CRS sanity and geospatial workflows: transforms at boundaries, explicit SRIDs, and format discipline |
| `making-maps-a-visual-guide-to-map-design-for-gis.pdf` | Establishes cartography governance: legends/ramps as truth claims; clarity and non-misleading design rules |
| `Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf` | Drives mobile/offline constraints, location sensitivity awareness, and “context changes meaning” principles |
| `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf` | Informs ops runbooks: migrations, backups, query discipline, and safe operational patterns |
| `Scalable Data Management for Future Hardware.pdf` | Guides scalability SOPs: streaming, caching, concurrency bounds, and predictable performance guardrails |
| `concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf` | Establishes job orchestration discipline: backpressure, bounded work, timeouts, and retry policies |
| `ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf` | Shapes threat model and hardening checklists: segmentation, safe ops, and defensive assumptions |
| `Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf` | Adds adversarial mindset: hostile inputs, parsing risk, and minimal attack surface SOPs |
| `compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf` | Governs media assets: format selection, optimization rules, and avoiding repository bloat |
| `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf` | Sets 3D governance: coordinate sanity, safe loaders, and “3D optional + graceful degradation” requirements |
| `Spectral Geometry of Graphs.pdf` | Grounds graph governance: interpretability, bounded analytics, and avoiding mystified graph metrics |
| `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf` | Defines simulation V&V and sensitivity SOPs; reproducibility and credibility posture for scenarios |
| `Generalized Topology Optimization for Structural Design.pdf` | Adds optimization SOPs: objectives/constraints recorded, sweeps captured, artifacts and versions tracked |
| `Understanding Statistics & Experimental Design.pdf` | Sets statistical hygiene SOPs: proper comparisons, bias checks, and assumption disclosure |
| `graphical-data-analysis-with-r.pdf` | Establishes EDA norms: distributions, outliers, “look first,” and exploratory integrity |
| `regression-analysis-with-python.pdf` | Adds regression diagnostics requirements: residuals, assumptions, and honest reporting |
| `Regression analysis using Python - slides-linear-regression.pdf` | Standardizes quick regression run reports and minimal output shapes for reproducible baseline checks |
| `think-bayes-bayesian-statistics-in-python.pdf` | Codifies Bayesian SOPs: priors, posteriors, intervals, and uncertainty communication |
| `Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf` | Shapes ML SOPs: artifact-first workflows, eval discipline, model cards, and separating training from serving |
| `responsive-web-design-with-html5-and-css3.pdf` | Governs UI-facing artifacts: responsive constraints, performance budgets, and progressive enhancement mindset |
| `A programming Books.pdf` | Contributor shelf: broad engineering references used to standardize tooling and cross-language practices |
| `B-C programming Books.pdf` | Contributor shelf (B–C) |
| `D-E programming Books.pdf` | Contributor shelf (D–E) |
| `F-H programming Books.pdf` | Contributor shelf (F–H) |
| `I-L programming Books.pdf` | Contributor shelf (I–L) |
| `M-N programming Books.pdf` | Contributor shelf (M–N) |
| `O-R programming Books.pdf` | Contributor shelf (O–R) |
| `S-T programming Books.pdf` | Contributor shelf (S–T) |
| `U-X programming Books.pdf` | Contributor shelf (U–X) |

</details>

---

🌾 **MCP mantra:** ship only what you can explain, reproduce, and defend.  
🧭 Keep KFM honest. Keep it human. Keep it governed.
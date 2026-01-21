# 🧾 Model Card Templates (MCP)

![MCP](https://img.shields.io/badge/MCP-Templates-orange)
![Model%20Cards](https://img.shields.io/badge/Model%20Cards-Required-red)
![Provenance](https://img.shields.io/badge/Provenance-%E2%9B%93_enforced-brightgreen)
![Policy%20as%20Code](https://img.shields.io/badge/Policy%20as%20Code-OPA%20%2B%20Conftest-blue)
![FAIR%20%2B%20CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Governance-purple)

> [!IMPORTANT]
> In Kansas Frontier Matrix (KFM), **no model ships without a model card**.  
> If it touches ingestion 📥, analysis 🧠, simulation 🧪, or user-visible narratives 🧭—it needs documentation, provenance, evaluation, and governance sign-off ✅.

---

## 🎯 Why model cards exist in KFM

KFM is designed to be **evidence-first** and **provenance-first**: users should always be able to answer *“Where did this come from?”* and *“How was it produced?”*.

Model Cards are the standardized, reviewable way to document:

- ✅ **What a model does** (intended use, scope, UX surfaces)
- 🧬 **What it was built from** (datasets, preprocessing, provenance)
- 📊 **How it was evaluated** (metrics, coverage, segmentation, edge cases)
- ⚠️ **How it can fail** (limitations, risks, known failure modes)
- 🛡 **How it’s governed & secured** (policy-as-code, FAIR/CARE, access controls, prompt security)
- 🔁 **How it’s monitored** (drift, bias, regressions, incident playbooks)

In KFM, model cards aren’t just “docs”—they’re also **policy-validated metadata** that integrates with:
- the **Knowledge Graph** (lineage & explainability),
- the **Governance Ledger** (audit trails),
- and the **UI** (Focus Mode citations, provenance panels, traceability overlays).

---

## ✅ When you MUST create a model card

Create a model card for **any** of the following:

- 🤖 **LLM/RAG assistants** (e.g., Focus Mode)
- 🧲 **Embedding / retrieval models** (vectorization, rerankers, hybrid search)
- 🗺 **Geospatial ML** (raster segmentation/classification, vector inference, change detection)
- 🧾 **NLP extraction** (OCR post-processing, NER, entity linking, topic modeling)
- 🛰 **Remote sensing CV** (feature detection from imagery or scanned maps)
- 📈 **Time-series** (NowCast, anomaly detection, forecasting)
- 🧪 **Simulation models** (calibration pipelines, scenario models)
- 🧰 **Rule-based heuristics** that publish facts, influence decisions, or affect access/ranking

> [!NOTE]
> If a “model” is actually a **third-party API**, treat it as a model and document it the same way (vendor + version + terms + failure modes + governance + monitoring).

---

## 📦 Where things live (recommended)

```text
📁 mcp/
  📁 templates/
    📁 model_cards/
      📄 README.md   ✅ (this file)
      📄 model-card.min.md        (suggested)
      📄 model-card.full.md       (suggested)
      📄 model-card.llm-rag.md    (suggested)
      📄 model-card.geo-ml.md     (suggested)
      📄 model-card.timeseries.md (suggested)
      📄 model-card.sim.md        (suggested)
      📁 schema/
        📄 model_card.schema.json (suggested)
        📄 model_card.examples/   (suggested)

📁 docs/
  📁 model_cards/
    📄 <model_id>.md             ✅ canonical published model cards

📁 data/
  📁 audits/
    📁 <run_id>/
      📄 run_manifest.json
      📄 prov.jsonld
      📄 eval_report.md
      📄 evidence_manifest.json
```

> [!TIP]
> **Templates live here** (`mcp/templates/model_cards/`).  
> **Actual cards live in** `docs/model_cards/` so they are easy to discover, review, and publish.

---

## 🚀 Quickstart: create a new model card

1) **Pick an ID**
- Use a stable, namespaced ID (examples):
  - `kfm.ai.focus_mode.v1`
  - `kfm.geo.segmentation.landcover.v2`
  - `kfm.timeseries.nowcast.river_stage.v1`

2) **Copy a template**
- Copy a template from this folder into `docs/model_cards/`.

3) **Fill the “required” fields**
- Don’t leave placeholders. “TODO” is not a valid metadata value for production.

4) **Attach evidence**
- Any performance claim must point to an evaluation artifact (run manifest + metrics + datasets + provenance).

5) **Pass policy gates**
- Model cards should be checked by policy-as-code (OPA/Conftest) in CI (and locally if available).

---

## 🧩 Template choices (recommended set)

| Template | Best for | Why |
|---|---|---|
| `model-card.min.md` | Prototypes / experiments | Fast, still documents risks + scope |
| `model-card.full.md` | Production / published models | Complete governance + evaluation + ops |
| `model-card.llm-rag.md` | Focus Mode / assistants | Adds citation rules, retrieval corpora, prompt security |
| `model-card.geo-ml.md` | Raster/vector geospatial ML | Adds CRS, resolution, spatial CV, map layer output |
| `model-card.timeseries.md` | Forecasting / anomaly detection | Adds temporal CV, drift signals, horizon behavior |
| `model-card.sim.md` | Simulation / calibration models | Adds assumptions, equations, calibration, sensitivity |

> [!NOTE]
> If these template files don’t exist yet, this README defines the **standard** they should implement.

---

## 🧾 KFM Model Card Standard

### 1) YAML front matter (machine-validated metadata)

Every model card **MUST** start with YAML front matter:

```yaml
---
id: kfm.<domain>.<name>.v1
name: "<Human-friendly model name>"
status: draft | active | deprecated
type: llm_rag | embeddings | classifier | cv_segmentation | timeseries | simulation | heuristic
owners:
  maintainer: "<name or handle>"
  team: "<team or group>"
version:
  model: "1.0.0"
  card: "1.0.0"
  created: "YYYY-MM-DD"
  updated: "YYYY-MM-DD"

intended_use:
  primary_users: ["researchers", "analysts", "public"]
  user_surfaces: ["Focus Mode", "Ingestion Assistant", "Story Nodes"]
  decisions_supported: ["triage", "summarization", "linking"]
  decisions_not_supported: ["legal conclusions", "safety-critical control"]

interfaces:
  inputs:
    schema_ref: "<path or URL to JSON Schema / OpenAPI / typed contract>"
    examples_ref: "<path>"
  outputs:
    schema_ref: "<path or URL>"
    examples_ref: "<path>"

data:
  training:
    datasets:
      - id: "<dcat_id or kfm dataset id>"
        stac_ref: "<stac item/collection id or URL>"
        license: "<license>"
        provenance_ref: "<prov activity/entity id or file>"
    preprocessing_ref: "<pipeline config or commit>"
    sensitivity: public | internal | restricted
  evaluation:
    datasets:
      - id: "<dcat_id or kfm dataset id>"
        stac_ref: "<stac id>"
        provenance_ref: "<prov ref>"
    eval_report_ref: "<path to eval report>"
    evidence_manifest_ref: "<path to evidence manifest>"

retrieval: # for RAG / search models
  corpora:
    - "<collection id(s)>"
  refresh_policy: "<schedule + triggers>"
  embedding_model_ref: "<model id>"

distribution:
  oci:
    enabled: true
    registry: "<ghcr.io | internal registry>"
    repository: "<org>/<artifact>"
    digest: "sha256:<...>"
    signed: true
    signature_ref: "<cosign ref>"

governance:
  policy_pack_ref: "<policy pack version or commit>"
  faircare: true
  approvals_required:
    - "<role/team>"
  waiver_ref: "<optional waiver id + reason>"

security:
  pii_controls: ["redaction", "access-control", "minimization"]
  prompt_security: ["injection_filter", "tool_allowlist", "refusal_rules"]
  secrets_handling: ["no_secrets_in_prompts", "vaulted_tokens"]

monitoring:
  drift:
    signals: ["accuracy", "citation_coverage", "distribution_shift"]
    schedule: "<weekly/monthly>"
    thresholds_ref: "<path>"
  incident_playbook_ref: "<path>"

sustainability:
  telemetry_ref: "<energy/cost report path>"
---
```

> [!TIP]
> Keep the YAML **small but real**: if the field matters enough to track, it matters enough to be correct.

---

### 2) Required sections (human-readable narrative)

After YAML, every model card **MUST** include these headings:

1. **Summary**
2. **Intended Use**
3. **Model Details**
4. **Data & Provenance**
5. **Evaluation**
6. **Limitations & Failure Modes**
7. **Ethical Considerations**
8. **Security & Privacy**
9. **Operations & Monitoring**
10. **Changelog**

Optional but recommended:
- **UI Integration Notes**
- **Known Issues / Open Risks**
- **Decommission Plan** (if `deprecated`)

---

## 🔍 Evidence-first & provenance-first rules (KFM-specific)

### ✅ Citation discipline (especially for assistants)

For any model producing **user-visible text** (e.g., Focus Mode / Story Nodes):

- Every material factual claim **MUST** be tied to **retrievable sources** (dataset IDs, doc references, STAC/DCAT/PROV links, etc.).
- If the model can’t retrieve evidence, it **MUST refuse or clearly mark uncertainty**.
- Any AI-generated metadata or narrative must be **labeled as AI-generated** and logged for audit.

### ⛓ Provenance requirements

A model card is incomplete without lineage pointers:

- **Training lineage**: datasets + preprocessing + code version + environment
- **Evaluation lineage**: datasets + run configuration + metric outputs
- **Deployment lineage**: artifact digest + signature + policy pack version
- **Governance lineage**: approvals/waivers + ledger references where applicable

> [!NOTE]
> KFM treats *models as auditable artifacts*—the same way it treats maps and datasets.

---

## 🧭 UI Integration expectations

KFM’s UI philosophy is “**the map behind the map**”—traceability surfaced directly to the user:

When a model’s output appears in UI, model cards should document:
- where the output is rendered (map overlays, panels, story playback, Focus Mode answers),
- how provenance is shown (provenance panel, audit panel, citations),
- how users can verify or dispute outputs (feedback loops, corrections, flags),
- any constraints for mobile/touch experiences if relevant.

For geospatial outputs, include:
- output formats (COG/GeoJSON/PMTiles/KML/KMZ),
- how time is represented (timeline slider, time bins),
- performance budgets (tile size, query latency expectations).

---

## 🛡 Security, privacy, and ethics (FAIR + CARE)

Model cards MUST explicitly describe:
- **Sensitive data exposure risk** (including location sensitivity and Indigenous/community-controlled knowledge)
- **Access controls** and redaction strategies
- **Bias risks** and historical context pitfalls
- **Human-in-the-loop** review points (what’s automated vs what requires verification)

> [!IMPORTANT]
> If a model could plausibly surface restricted cultural heritage data, protected species locations, or sensitive infrastructure info, document the mitigation plan **before** deployment.

---

## 📈 Evaluation: what “good” looks like in KFM

Evaluation should be **reproducible and segment-aware**, not a single vanity metric.

Recommended evaluation elements:
- **Dataset coverage**: temporal + geographic + domain coverage
- **Segmented metrics**: performance by region, time period, data source type, document type
- **Stress tests**:
  - out-of-distribution inputs
  - noisy OCR / poor scans
  - adversarial prompts (for LLMs)
  - shifting real-time distributions (for NowCast)
- **Explainability checks**:
  - citation coverage (for assistants)
  - GeoXAI artifacts (for geospatial ML) where applicable

> [!TIP]
> For time-series, include backtesting strategy (rolling windows), horizon behavior, and alerting thresholds.

---

## 🔁 Monitoring & drift: “don’t set it and forget it”

KFM expects **ongoing monitoring**:

- Drift checks (accuracy changes, distribution shifts, citation coverage drops)
- Bias checks (diverse query sets, geo/temporal segmentation)
- Regression tests tied to governance policy packs
- Defined rollback plan (how to revert artifact digest safely)

Include:
- drift signals
- thresholds
- monitoring schedule
- incident playbook link
- escalation owners

---

## 📦 Artifact distribution (OCI + signing)

For production models (and any model that drives automated ingestion/analysis), document:

- **Where the artifact lives** (OCI registry recommended)
- **Exact immutable digest** (`sha256:...`)
- **Signing** (Cosign or equivalent)
- **SBOM / dependency record** (recommended)
- **Reproducible environment notes** (container, requirements, GPU expectations)

> [!NOTE]
> This aligns with KFM’s broader supply-chain security and reproducibility direction.

---

## 🧪 Example: Minimal model card skeleton

```markdown
---
id: kfm.geo.classifier.example.v0
name: "Example Geo Classifier"
status: draft
type: classifier
owners:
  maintainer: "@handle"
  team: "KFM Core"
version:
  model: "0.1.0"
  card: "0.1.0"
  created: "YYYY-MM-DD"
  updated: "YYYY-MM-DD"
---

## Summary
One paragraph describing what this model does and where it is used.

## Intended Use
- ✅ Intended:
- 🚫 Not intended:

## Model Details
- Approach:
- Inputs/Outputs:

## Data & Provenance
- Training datasets:
- Evaluation datasets:
- Provenance refs:

## Evaluation
- Metrics:
- Known good/bad segments:

## Limitations & Failure Modes
- What it struggles with:
- Known failure cases:

## Ethical Considerations
- Bias risks:
- Sensitive data risks:

## Security & Privacy
- Controls:
- Access considerations:

## Operations & Monitoring
- Drift signals:
- Incident playbook:

## Changelog
- YYYY-MM-DD: created
```

---

## ✅ PR checklist (copy/paste into your PR)

- [ ] Card uses a valid `id` + `version.model` + `version.card`
- [ ] Intended use is explicit; **non-intended** uses are explicit
- [ ] Training + evaluation datasets are identified (IDs + licenses)
- [ ] Provenance references exist (run manifest / PROV / evidence)
- [ ] Evaluation includes segmentation relevant to the model type (geo/time/source)
- [ ] Limitations include at least 3 realistic failure modes
- [ ] Ethics & sensitivity classification addressed (FAIR + CARE)
- [ ] Security & privacy mitigations documented
- [ ] Monitoring plan exists (signals + thresholds + owners)
- [ ] Distribution info is immutable (OCI digest + signature) for production models
- [ ] Changelog updated

---

## 📚 Project context & reference docs used to shape this standard

These templates are aligned with KFM’s broader architecture, governance, and UI principles:

- 📘 **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation** — openness, ethics, licensing discipline, future-ready governance.
- 🧱 **Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design** — policy pack enforcement, modularity, roadmap.
- 🧭 **Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖** — Focus Mode behavior, drift/bias monitoring, prompt security layers.
- 🖥 **Kansas Frontier Matrix – Comprehensive UI System Overview** — “map behind the map”, provenance surfacing, Focus Mode UX.
- 📥 **📚 KFM Data Intake – Technical & Design Guide** — immutability, deterministic pipelines, STAC/DCAT/PROV integration, FAIR/CARE oversight.
- 🌟 **KFM – Latest Ideas & Future Proposals** — PR→PROV integration, CI invariants, policy pack hardening, reproducible research practices.
- 💡 **Innovative Concepts to Evolve KFM** — GeoXAI, AR/4D concepts, crowdsourced verification, next-gen narrative tooling.
- 🧠 **Additional Project Ideas** — evidence manifests, artifact storage + signing, run manifests, policy waivers & governance mechanics.
- 🗺 **Kansas-Frontier-Matrix: Open-Source Geospatial Historical Mapping Hub Design** — early repo structure, MapLibre/Leaflet, notebooks-as-docs, MCP folder patterns.
- 🧪 **Scientific Method / Research / Master Coder Protocol Documentation** — reproducibility, experiment tracking, model cards as standard research artifacts.
- 🔍 **KFM Design Audit – Gaps & Enhancement Opportunities** — highlights need for modularity, interface specs, and consistent documentation standards.

### 📦 Reference libraries (included in the project, great for deep dives)

These are “toolbox” bundles used as supporting knowledge for KFM development (AI, geospatial, data engineering, Bayesian methods):

- 🤖 `AI Concepts & more.pdf` (portfolio)
- 🗺 `Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf` (portfolio)
- 🧱 `Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf` (portfolio)
- 🧰 `Various programming langurages & resources 1.pdf` (portfolio)

> [!TIP]
> If you cite external methods or algorithms in a model card, link to primary references (papers/docs) and/or note which internal library bundle informed the approach.

---

## 🧹 Maintenance notes (for template owners)

- Keep templates **stable**: update via versioned changes (bump `version.card` in examples).
- When policies evolve, update templates + schema together.
- Add at least one example card per new template type.
- Prefer **small, enforceable requirements** over verbose, unenforced narratives.

✨ If it can’t be validated, it’s a suggestion. If it’s critical, make it policy.

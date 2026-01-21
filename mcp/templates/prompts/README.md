# 🧩 MCP Prompt Templates (KFM) — `mcp/templates/prompts/`

![Status](https://img.shields.io/badge/status-active-brightgreen) ![Evidence-First](https://img.shields.io/badge/policy-evidence--first-blue) ![Governance](https://img.shields.io/badge/governance-OPA%20%2B%20PROV-purple)

> This folder defines **prompt templates as governed “contracts”**: reproducible, auditable, and safe-by-default—built for KFM’s **Focus Mode**, Story tooling, ingestion agents, and narrative pipelines.  
> The AI layer is designed to produce **AnswerWithCitations** via a strict prompt template and a governance check.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

---

## 📌 Why this folder exists

KFM’s AI outputs are treated as **first-class artifacts** (not ephemeral chat):  
- If the assistant **can’t cite**, it **must not answer**; outputs are checked (optionally) by policy gates (OPA) to ensure claims are cited.  [oai_citation:1‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- AI interactions can be logged to an **immutable governance ledger** and represented in **PROV** (who/what/when/inputs).  [oai_citation:2‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- Prompt security is layered (Prompt Gate filtering, tool allow/block lists, OPA checks).  [oai_citation:3‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  

This directory is where we keep those rules **explicit** and **versionable**.

---

## 🗂️ Suggested layout (you can evolve this)

```text
mcp/
└─ templates/
   └─ prompts/
      ├─ README.md                         👈 you are here
      ├─ shared/
      │  ├─ citation_rules.prompt.md       🔎 evidence + footnotes
      │  ├─ refusal_style.prompt.md        🧯 safe refusals + helpful redirects
      │  └─ output_contracts.prompt.md     📜 schemas + required sections
      ├─ focus_mode/
      │  ├─ qa.prompt.md                   🤖 Q&A with citations (RAG)
      │  └─ explainability.prompt.md       🧾 “audit panel” style reasoning trace
      ├─ story_nodes/
      │  ├─ authoring.prompt.md            📖 Markdown + JSON steps generator
      │  └─ evidence_manifest.prompt.md    🧾 evidence manifest stub + checks
      ├─ pulses/
      │  └─ pulse_thread.prompt.md         📍 geotagged “micro-story” updates
      ├─ intake/
      │  ├─ entity_linking.prompt.md       🧷 link people/places/events to graph
      │  └─ transform_planner.prompt.md    🧪 propose config; code executes safely
      └─ governance/
         ├─ policy_checks.prompt.md        🛡️ OPA/Rego assumptions + deny reasons
         └─ sensitivity.prompt.md          🧿 redaction/obfuscation rules
```

> Note: the broader repo “expected structure” explicitly carves out `mcp/` for methods/experiments and emphasizes governed templates + schemas.  [oai_citation:4‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧱 Template standard (the “prompt as contract” pattern)

### 1) Front-matter (metadata)
Use YAML front-matter to make prompts searchable, testable, and policy-checkable.  [oai_citation:5‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)

```yaml
---
id: focus_mode.qa.v1
owner: ai-platform
purpose: "Answer user questions from KFM sources with auditable citations."
policy:
  evidence_first: true
  sensitive_data: "deny_or_generalize"
inputs:
  question: string
  ui_context:
    bbox: [number, number, number, number]
    time_range: { start: string, end: string }
    active_layers: [string]
outputs:
  format: markdown
  must_include:
    - "Answer"
    - "Citations"
    - "Provenance"
    - "Refusal (when needed)"
---
```

### 2) Prompt sections (recommended)
Keep a consistent internal shape so linting and diff reviews are easy:

```text
## SYSTEM
## DEVELOPER
## USER
## OUTPUT CONTRACT
## REFUSAL RULES
## SOURCES / CITATION MACROS
```

---

## 🧭 Core rules every prompt must follow

### ✅ Evidence-first (no citations → no answer)
- Focus Mode and related prompts must produce footnote-style citations that link back to KFM sources.  [oai_citation:6‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- Runtime policy checks can enforce “every claim has a citation.”  [oai_citation:7‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  

### 🧾 Provenance & logging (make outputs auditable)
- Treat outputs as derivations: record inputs + activity + agent in PROV (and optionally in a governance ledger).  [oai_citation:8‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- For pipeline-style prompts, prefer a **Run Manifest** concept (schema’d, hashed, and used for policy checks).  [oai_citation:9‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  

### 🛡️ Prompt security (defense in depth)
Prompts must assume hostile input and rely on platform guardrails:
- **Prompt Gate** filtering/sanitization for injection attempts.  [oai_citation:10‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
- **Tool allow/block lists** (default: no internet; no arbitrary side effects).  [oai_citation:11‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
- **OPA/Rego checks** to block/redact disallowed output (sensitive coordinates, etc.).  [oai_citation:12‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  

### 🧿 Sensitive + cultural protocol aware
KFM is designed to respect CARE principles and cultural authority:
- Support “tiered access / protocols” (e.g., Traditional Knowledge labels / restricted content patterns).  [oai_citation:13‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  
- Support location obfuscation for sensitive records (e.g., rounding/precision reduction) when required.  [oai_citation:14‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  

---

## 🧠 Prompt packs (what we build prompts for)

### 🤖 Focus Mode (Q&A / RAG)
The reference flow is: **parse → retrieve → generate → governance check → AnswerWithCitations**.  [oai_citation:15‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
Also: retrieval is hybrid (graph + search) to ground answers.  [oai_citation:16‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

### 📖 Story Nodes (interactive narratives)
Stories are authored as **Markdown + JSON configuration** that drives map/timeline state transitions.  [oai_citation:17‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
The UI expects step-based playback and map updates (panning/zooming/layers/time).  [oai_citation:18‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  
Template-friendly story structure is explicitly intended to let authors contribute “without writing code.”  [oai_citation:19‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)

### 📍 Geotagged Pulse Threads (micro-narratives)
Pulse Threads are a “timely, location-specific narrative update,” stored as graph nodes with provenance and an evidence manifest.  [oai_citation:20‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### 🧩 Conceptual Attention Nodes (AI + UX “topic lenses”)
Concept nodes help the AI gather context systematically and can appear as UI filters/lenses (e.g., “Drought”).  [oai_citation:21‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  

### 🧪 Data intake & agent planning (human-in-the-loop)
Agents may propose configs, but code executes transforms after validation (and logs the AgentAction in provenance).  [oai_citation:22‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
No silent end-to-end automation: changes should be reviewable (e.g., PRs) and auditable.  [oai_citation:23‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 🧾 Citation macros (recommended)

### Footnotes (default)
Use Markdown footnotes for claims:

```md
Kansas streamflows show early drought signs.[^usgs]

[^usgs]: kfm://dataset/usgs_nwis?station=06752000&asof=2026-01-21T20:00:00Z
```

KFM explicitly supports footnote-style citations that connect to catalog/graph IDs.  [oai_citation:24‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

### “Sources” blocks (optional)
When generating structured outputs (Story Nodes, Pulse Threads), add a machine-friendly Sources section:

```yaml
sources:
  - id: dcat:usgs_nwis_realtime
    type: dcat
    href: kfm://dcat/usgs_nwis_realtime
  - id: stac:gauge_06752000_latest
    type: stac
    href: kfm://stac/items/gauge_06752000/latest
```

---

## 🧷 Output contracts (what the model MUST return)

### Focus Mode answer (minimum contract)
```md
## Answer
<plain-language answer>

## Citations
- [^1] ...
- [^2] ...

## Provenance
- generated_at: <timestamp>
- inputs: <entity ids / dataset ids>
- policy_checks: <pass|deny + rule ids>

## Notes / Limitations
<what’s missing, uncertainty, scope>
```

### Story Node generator contract (files to emit)
Story tooling should produce:
- `story.md` (narrative)
- `story.json` (steps: camera, layers, time)
- `evidence.yml` (citations + checksums + provenance pointers)

This aligns with Story Nodes being authored as Markdown + JSON configs and guided by templates.  [oai_citation:25‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  [oai_citation:26‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  
Evidence manifests can be used to audit stories and ensure citations resolve.  [oai_citation:27‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### Pulse Thread contract (files to emit)
- `pulse.md` (short narrative update)
- `pulse.json` (geotags + linked entities)
- `evidence.yml` (facts → sources mapping)

Pulse Threads are explicitly described as versioned, evidence-backed, and discoverable via map regions.  [oai_citation:28‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 🧪 Governance hooks (how prompts interact with policy)

- **Fail closed** when required metadata/citations are missing (CI/policy gates block merge).  [oai_citation:29‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
- Prefer structured artifacts (manifests, schemas) so Rego policies can validate compliance.  [oai_citation:30‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
- Artifact integrity patterns (OCI/ORAS/Cosign + PROV attachments) reinforce reproducibility for large outputs.  [oai_citation:31‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  

---

## 🧰 Adding a new prompt (contributor checklist)

- [ ] Pick an `id` and include YAML front-matter (owner, purpose, inputs, outputs).  [oai_citation:32‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)  
- [ ] Define an explicit output contract (schema or required headings).
- [ ] Include refusal conditions (no citations, sensitive data, missing scope).
- [ ] Add test cases (golden prompts + expected structure).
- [ ] Ensure human review path (no silent automation).  [oai_citation:33‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  

---

## 📚 Design anchors (what this README is built on)

### KFM-specific docs
- **Data contracts are mandatory; “no mystery layers.”**  [oai_citation:34‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- **Focus Mode = evidence-backed answers, citations, governance checks.**  [oai_citation:35‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  [oai_citation:36‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- **Prompt security layers (Prompt Gate, allowlists, OPA).**  [oai_citation:37‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
- **Story Nodes = Markdown + JSON, step-driven map state.**  [oai_citation:38‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  [oai_citation:39‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  
- **Pulse Threads + Conceptual Attention Nodes (future-forward narrative tooling).**  [oai_citation:40‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  [oai_citation:41‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
- **CARE + sensitivity-aware handling patterns.**  [oai_citation:42‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  [oai_citation:43‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  

### MCP / documentation rigor
- Domain-specific documentation patterns (model cards, experiment logs, reproducibility).  [oai_citation:44‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)  
- Repo layout emphasizes governed templates, schemas, and `mcp/` for methods/experiments.  [oai_citation:45‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  

---

## 📎 Project references (all currently attached “project files”)

> These are the upstream specs and reference packs that informed the prompt/template conventions here.

- 📘 Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf  [oai_citation:46‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- 🏗️ Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf  [oai_citation:47‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- 🧭 Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf  [oai_citation:48‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
- 🖥️ Kansas Frontier Matrix – Comprehensive UI System Overview.pdf  [oai_citation:49‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  
- 📥 📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf  [oai_citation:50‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- 🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf  [oai_citation:51‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)  
- 💡 Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf  [oai_citation:52‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  [oai_citation:53‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  
- 🧠 Additional Project Ideas.pdf  [oai_citation:54‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  [oai_citation:55‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  

### 📦 Reference portfolios (PDF “bundles”)
> These are PDF portfolios (may need Adobe Reader to browse the embedded docs). They’re kept as reference libraries for design + implementation decisions.

- 🗺️ Maps / Google Maps / Virtual Worlds / WebGL bundle  [oai_citation:56‡Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf](file-service://file-RshcX5sNY2wpiNjRfoP6z6)  
- 🤖 AI Concepts & more bundle  [oai_citation:57‡AI Concepts & more.pdf](file-service://file-K6BctJjeUwvyCahLf9qdwr)  
- 🧱 Data Management / Data Science / Bayesian bundle  [oai_citation:58‡Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf](file-service://file-RrXMFY7cP925exsQYermf2)  
- 🧰 Programming languages & resources bundle  [oai_citation:59‡Various programming langurages & resources 1.pdf](file-service://file-4wp3wSSZs7gk5qHWaJVudi)  

---

## 📓 Glossary (tiny, opinionated)

- **Evidence Manifest** 🧾: machine-readable mapping of claims → sources (often alongside narratives).  [oai_citation:60‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
- **Run Manifest** 🧪: per-run audit artifact (inputs/outputs/tools/versions + hash) used for governance checks.  [oai_citation:61‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
- **OPA / Rego** 🛡️: policy-as-code gates for “fail closed” compliance checks.  [oai_citation:62‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
- **STAC / DCAT / PROV** 🧬: discovery + catalog + provenance standards linked together for traceability.  [oai_citation:63‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  

---

---
title: "EXP-2026-01-21 — Focus Mode Citation Gate 🧠📎 (Evidence-First Output Enforcement)"
version: "v0.1.0"
status: "example/draft"
doc_kind: "Experiment Report"
experiment_id: "EXP-2026-01-21_focusmode-citation-gate"
created: "2026-01-21"
last_updated: "2026-01-21"
owners:
  - "KFM Core (AI + Governance)"
tags:
  - "mcp"
  - "dev_prov"
  - "focus-mode"
  - "citations"
  - "opa"
  - "prov"
  - "evidence-first"
risk_level: "medium"
license: "CC-BY-4.0"
fair_category: "FAIR+CARE"
care_label: "Public"
sensitivity: "public"
classification: "open"
doc_uuid: "urn:kfm:exp:2026-01-21:focusmode-citation-gate"
---

According to a document from 2026-01-21, this experiment report is an **example** (template + filled design) for implementing and validating a **Citation Gate** for KFM Focus Mode answers.

![status](https://img.shields.io/badge/status-example%2Fdraft-orange) ![domain](https://img.shields.io/badge/domain-Focus%20Mode-blue) ![policy](https://img.shields.io/badge/policy-OPA%20%2F%20Rego-green) ![provenance](https://img.shields.io/badge/provenance-PROV--ready-9cf)

---

## 📍 File Location

**Target path:** `mcp/dev_prov/examples/10_experiment_report_template/(example_report_tree)/EXP-2026-01-21_focusmode-citation-gate.md`

```text
📦 mcp/
  📦 dev_prov/
    📦 examples/
      📦 10_experiment_report_template/
        📦 (example_report_tree)/
          🧾 EXP-2026-01-21_focusmode-citation-gate.md  ← (this file)
          📁 artifacts/   (optional in real runs)
            📁 policy/
            📁 schemas/
            📁 logs/
            📁 eval/
```

---

<details>
<summary>🧭 Table of Contents</summary>

- [Why this experiment exists](#-why-this-experiment-exists)
- [Experiment question](#-experiment-question)
- [Hypothesis](#-hypothesis)
- [System context](#-system-context)
- [What is a “Citation Gate”?](#-what-is-a-citation-gate)
- [Design](#-design)
  - [Inputs/outputs](#inputsoutputs)
  - [Response schema](#response-schema-contract)
  - [Gate rules](#gate-rules)
  - [OPA/Rego policy](#oparego-policy-skeleton)
  - [UI behavior](#ui-behavior)
  - [Provenance logging](#provenance-logging)
- [Method](#-method)
- [Metrics](#-metrics)
- [Results](#-results)
- [Decision](#-decision)
- [Risks & mitigations](#-risks--mitigations)
- [Appendix](#-appendix)
- [References (project files used)](#-references-project-files-used)

</details>

---

## 🎯 Why this experiment exists

KFM’s design is explicitly **evidence-first**:

- Focus Mode should **cite sources** and **avoid fabricating** information; if something can’t be derived from verified data, the system should refuse or clearly indicate uncertainty. [oai_citation:0‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
- Data intake/governance calls out **hard enforcement**: “disallows unsourced outputs,” and even mentions a **runtime policy check (OPA) on outputs to ensure every claim has a citation** (and “if the AI cannot provide a source, it is not allowed to give an answer”). [oai_citation:1‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- KFM also uses policy-as-code patterns (OPA/Rego + CI gates) and proposes a “Policy Pack” approach where AI outputs must include citations (and Focus Mode can be checked at runtime). [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

This experiment defines a **Citation Gate** that makes the above requirements *mechanically enforceable*.

---

## ❓ Experiment question

**Can we implement a runtime “Citation Gate” that prevents Focus Mode from emitting any substantive claim unless it is attached to verifiable evidence (citations), while keeping user experience usable (reasonable latency + acceptable refusal rate)?**

---

## 🧪 Hypothesis

If we require a structured Focus Mode response containing:
1) an explicit **claim list** (or claim spans),
2) **citations** referencing retrievable KFM artifacts (DCAT/STAC/PROV/doc excerpts), and
3) a policy check that **fails closed**,

…then the system will:
- reduce “unsourced” answers to ~0,
- make auditing easier,
- align UI + governance expectations without relying on “prompt discipline” alone. [oai_citation:3‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

---

## 🧩 System context

### Focus Mode = grounded AI + citations
Focus Mode uses retrieval-augmented patterns (retrieve evidence → generate answer) and is designed to cite sources rather than invent data. [oai_citation:5‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg) [oai_citation:6‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

### UI expects visible citations
The UI system overview describes Focus Mode as an AI assistant that provides answers with citations, integrated into the interface for user verification and trust.

### The data backbone includes standardized catalogs + provenance
KFM’s intake approach emphasizes a “catalog triplet” (STAC item + DCAT dataset + PROV doc), and explicitly states that **without PROV a dataset can’t be published (CI can fail)**. [oai_citation:7‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 🚦 What is a “Citation Gate”?

A **Citation Gate** is a deterministic enforcement layer that sits between:
- **LLM output** (candidate answer) and
- **User-visible UI output / persisted artifacts**

…and only allows responses that satisfy a policy like:
- “every claim has at least one citation”
- citations reference real evidence objects
- provenance logging is attached

If checks fail, the gate either:
- triggers a **repair/regeneration** attempt, or
- **refuses** (fail closed) with an explanation.

This matches KFM’s emphasis that **unsourced outputs are disallowed** and policy checks can be applied at runtime. [oai_citation:8‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 🏗️ Design

### Inputs/outputs

**Input:**  
- `user_query`  
- `retrieved_evidence_bundle` (KG nodes, DCAT datasets, STAC items, PROV bundles, doc snippets)
- `candidate_answer` (model output, ideally structured)

**Output (gate decision):**
- ✅ `ALLOW` + normalized response + provenance payload  
or  
- ❌ `DENY` + machine-readable reason + user-safe refusal message

---

### Response schema contract

To make policy checks reliable, do **not** gate on “raw markdown” only. Prefer a structured response that can be validated.

Example contract (`kfm.focusmode.Answer.v1`):

```json
{
  "answer_markdown": "…",
  "claims": [
    {
      "claim_id": "clm-001",
      "text": "The Kansas River gauge at Topeka reads 12.3 ft as of 2026-01-21 15:00 UTC.",
      "citation_ids": ["cit-001"]
    }
  ],
  "citations": [
    {
      "citation_id": "cit-001",
      "kind": "dcat-dataset",
      "title": "USGS NWIS Kansas River at Topeka (example)",
      "stable_id": "dcat:usgs:nwis:06889000",
      "retrieved_at": "2026-01-21T15:02:11Z",
      "locator": {
        "type": "api",
        "query": "station=06889000"
      }
    }
  ],
  "provenance": {
    "prov_bundle_id": "prov:run:focusmode:2026-01-21T15:02:12Z:abcd1234",
    "retrieval_run_id": "retr:2026-01-21T15:01:59Z:efgh5678"
  }
}
```

Why: KFM already prioritizes traceability (datasets have provenance & licensing metadata) [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC) and disallows unsourced outputs [oai_citation:10‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)—a structured schema makes that enforceable.

---

### Gate rules

**R0 — Fail closed**  
If the gate cannot validate the response, **deny** (don’t “best-effort” an uncited answer). This aligns with “no provenance → can’t publish” governance posture. [oai_citation:11‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

**R1 — Every claim requires ≥ 1 citation**  
- `claims[*].citation_ids` must be non-empty.

**R2 — Citation integrity**
- every `citation_id` must exist in `citations[]`
- every citation must contain:
  - `stable_id` (dataset/doc ID, STAC item ID, commit SHA, etc.)
  - `retrieved_at` timestamp

**R3 — Evidence type constraints**
- numerical/time-sensitive claims must cite datasets or APIs (not only narratives)
- cultural/sensitive location outputs must obey sensitivity rules (future policy extension). (KFM discusses sensitivity tagging and location generalization.) [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

**R4 — Optional “multi-proof” for inferences (stretch goal)**
For “inference-class” claims (e.g., “likely site of interest”), require ≥ 2 independent sources (map + text, etc.). This matches the project’s multi-source correlation idea: surfacing inferences only when supported by multiple evidences. [oai_citation:13‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)

---

### OPA/Rego policy skeleton

KFM governance materials explicitly discuss OPA checks in runtime contexts for outputs and policy packs for AI output compliance. [oai_citation:14‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) [oai_citation:15‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

Example Rego sketch:

```rego
package kfm.focusmode.citation_gate

default allow = false

deny[msg] {
  not input.claims
  msg := "Missing claims[]; cannot prove per-claim citations"
}

deny[msg] {
  count(input.claims) == 0
  msg := "No claims provided"
}

deny[msg] {
  some i
  claim := input.claims[i]
  count(claim.citation_ids) == 0
  msg := sprintf("Claim %s has no citations", [claim.claim_id])
}

deny[msg] {
  some i
  some j
  cid := input.claims[i].citation_ids[j]
  not citation_exists(cid)
  msg := sprintf("Claim references unknown citation_id: %s", [cid])
}

citation_exists(cid) {
  some k
  input.citations[k].citation_id == cid
}

allow {
  count(deny) == 0
}
```

> ✅ In a real run, store this in `artifacts/policy/citation_gate.rego` and evaluate with OPA at runtime + in CI (Conftest). The project already describes policy gates in CI flows. [oai_citation:16‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

### UI behavior

The UI system overview expects Focus Mode to show citations as part of the user experience.

**When gate passes**
- show answer markdown
- render claim-linked footnotes / hover tooltips
- add a “🔎 View Evidence” affordance that opens a source list

**When gate denies**
- show a refusal message:
  - “I can’t answer that from available sources.”
  - offer next-best actions:
    - suggest narrowing the query
    - suggest ingesting a missing dataset/document
- optionally show a debug-only “why denied” panel (dev builds)

> This aligns with “if the AI cannot provide a source, it is not allowed to give an answer.” [oai_citation:17‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

### Provenance logging

KFM aims to attach provenance to AI outputs and governance events (including linking PRs to PROV). [oai_citation:18‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)

For Focus Mode answers:
- record a PROV bundle:
  - `prov:Entity` = the answer artifact
  - `prov:used` = each cited dataset/doc
  - timestamps, retrieval run IDs, policy decision outcome

Real-time question example is explicitly envisioned: provide the reading + timestamp + cite dataset, and log that usage in PROV. [oai_citation:19‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 🧫 Method

This report follows a scientific-method style experiment structure (question → hypothesis → method → results → conclusion) per project research/protocol guidance. [oai_citation:20‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

### Procedure (example)

1) **Create a query suite** (20–50 questions) spanning:
   - fact lookup from ingested docs
   - geospatial/time queries
   - “why/how” interpretive questions
   - sensitive/safety red-team prompts (optional)

2) For each query:
   - run retrieval + LLM generation
   - evaluate the candidate response via Citation Gate
   - record:
     - ALLOW/DENY
     - reasons
     - citations present/missing
     - latency

3) Manual review (sampled) for:
   - correctness
   - citation relevance (not “random citations”)

---

## 📏 Metrics

| Metric | Definition | Target |
|---|---|---|
| Claim citation coverage | % claims with ≥1 valid citation | 100% (hard) |
| Citation validity | % citation_ids that resolve to real evidence | 100% |
| Refusal rate | % queries denied due to missing evidence | ≤ X% (tune) |
| Latency overhead | added p50/p95 time due to gating | ≤ Y ms |
| “Citation spam” rate | citations that don’t support claim | drive to 0 |

---

## 🧾 Results

> **Template note:** No empirical numbers are included here because this file is an example report. In a real run, paste tables and attach logs in `artifacts/logs/`.

### Findings (expected / design-level)

- A pure “regex for [1] [2]” approach is too brittle; structured `claims[] + citations[]` is the enforceable path.
- Runtime OPA checks are compatible with KFM’s “policy pack” concept and CI policy gate posture. [oai_citation:21‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC) [oai_citation:22‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
- UI can cleanly support evidence panels; the project already sketches “View Evidence” style affordances for traceability. [oai_citation:23‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## ✅ Decision

**Adopt** Citation Gate for Focus Mode as a two-layer check:

1) **Schema validator** (fast, deterministic)
2) **OPA policy evaluation** (policy-as-code, auditable)

**Fail closed** if either layer fails.

---

## ⚠️ Risks & mitigations

### Risk: Missing or non-indexable sources → high refusal rate
Some “project library” PDFs are **PDF portfolios** that recommend opening in Acrobat/Adobe Reader, which may reduce machine extractability for search/indexing. [oai_citation:24‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) [oai_citation:25‡Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf](file-service://file-RrXMFY7cP925exsQYermf2) [oai_citation:26‡Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf](file-service://file-RshcX5sNY2wpiNjRfoP6z6) [oai_citation:27‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

**Mitigation**
- detect PDF portfolio format at intake
- export internal attachments to normal PDFs
- ingest as separate documents with IDs (so citations can resolve)

### Risk: Citation relevance (“citation spam”)
**Mitigation**
- require citations to reference **specific evidence items** (dataset IDs, doc excerpt hashes, commit SHAs)
- add optional rule: each claim cites at least one evidence item with a locator (line range, bbox/time range, query params)

### Risk: “Inference” claims
**Mitigation**
- label claims as `fact|interpretation|inference`
- require ≥2 sources for `inference` (multi-proof), consistent with multi-source correlation principles. [oai_citation:28‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)

### Risk: Evidence integrity & tamper resistance
**Mitigation (optional hardening)**
- store evidence artifacts in OCI registries and sign with Cosign; citations can reference content digests for verification. [oai_citation:29‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 🧰 Appendix

### A) Example “denied” response (user-safe)

```json
{
  "decision": "DENY",
  "user_message": "I can’t answer that from the currently available verified sources. If you add a source dataset or document, I can re-check and cite it.",
  "deny_reasons": [
    "Claim clm-003 has no citations"
  ]
}
```

### B) Evidence manifest concept (optional integration)

KFM project ideas propose an **evidence manifest** that backs narratives with sources and a UI affordance to inspect them. [oai_citation:30‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

For Focus Mode, we can emit:
- `AnswerArtifact.json`
- `EvidenceManifest.json` (list of evidence items + digests)
- `ProvBundle.jsonld`

---

## 📚 References (project files used)

> These are the sources used to derive this experiment design. Inline citations throughout the doc point at supporting excerpts.

### Core KFM design docs
- 📚 Data Intake (governance + enforcement): `📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf` [oai_citation:31‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  [oai_citation:32‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- 🧭🤖 AI System Overview (Focus Mode behavior): `Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf` [oai_citation:33‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
- 🧱 Architecture / Policy Pack: `Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf` [oai_citation:34‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- 🖥️ UI System Overview (citations in UX): `Kansas Frontier Matrix – Comprehensive UI System Overview.pdf`  [oai_citation:35‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  
- 🛠️ Technical Documentation (traceability + metadata posture): `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf` [oai_citation:36‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  

### Roadmap / ideation docs
- 🌟 Latest proposals (provenance framework + citations): `🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf` [oai_citation:37‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)  
- 💡 Innovative concepts (evidence-based copilot + citations): `Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf` [oai_citation:38‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  [oai_citation:39‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  
- 🧠 Additional project ideas (evidence manifest, policy gates, artifact signing): `Additional Project Ideas.pdf` [oai_citation:40‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T) [oai_citation:41‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T) [oai_citation:42‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  [oai_citation:43‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  

### “Library” bundles (ingestion caveat)
- 🗂️ `AI Concepts & more.pdf` (PDF portfolio; extraction caveat) [oai_citation:44‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- 🗂️ `Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf` (PDF portfolio; extraction caveat) [oai_citation:45‡Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf](file-service://file-RrXMFY7cP925exsQYermf2)  
- 🗂️ `Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf` (PDF portfolio; extraction caveat) [oai_citation:46‡Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf](file-service://file-RshcX5sNY2wpiNjRfoP6z6)  
- 🗂️ `Various programming langurages & resources 1.pdf` (PDF portfolio; extraction caveat) [oai_citation:47‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  

### Helpful supporting references discovered in the project corpus
- 🗺️ Mapping hub design (multi-source correlation; MapLibre/Leaflet UI): `Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf` [oai_citation:48‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw) [oai_citation:49‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)  
- 🧪 Scientific method protocol: `Scientific Method _ Research _ Master Coder Protocol Documentation.pdf` [oai_citation:50‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)  
- 📝 Markdown governance best practices (evidence-first + CI validation): `Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx` [oai_citation:51‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)

---

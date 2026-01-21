# 🛡️ 08_security_defensive — Defensive Security, Governance & Safety (MCP Notebooks)

<p align="left">
  <a href="../README.md">⬅️ Notebooks Index</a> •
  <a href="#-quickstart">🚀 Quickstart</a> •
  <a href="#-policy-pack-opa--conftest">🧩 Policy Pack</a> •
  <a href="#-incident-response--rollback">🧯 Incident Response</a> •
  <a href="#-references--project-files">📚 References</a>
</p>

![Status](https://img.shields.io/badge/status-draft-yellow)
![Scope](https://img.shields.io/badge/scope-defensive%20security-blue)
![Governance](https://img.shields.io/badge/governance-FAIR%2BCARE-8A2BE2)
![Policy](https://img.shields.io/badge/policy-OPA%20%2B%20Conftest-2E8B57)
![Principle](https://img.shields.io/badge/principle-provenance--first-brightgreen)
![AI](https://img.shields.io/badge/AI-Focus%20Mode%20%2B%20Citations-black)

> [!IMPORTANT]
> This folder is **defensive-only**: hardening, policy enforcement, auditing, privacy protection, and supply‑chain integrity.  
> No “how to exploit” content, no offensive tooling walkthroughs.

---

## 🎯 Purpose

This notebook pack documents and tests **KFM’s defense-in-depth** approach across:

- ✅ **Policy-as-code gates** (OPA + Conftest) to enforce governance and security invariants in CI/CD and pipelines.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
- ✅ **Fail-closed ingestion + publishing** (schema, STAC/DCAT/PROV completeness, license, sensitivity labels, provenance completeness).  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- ✅ **Focus Mode AI safety**: retrieval + citations + governance checks + prompt security layers.  [oai_citation:2‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg) [oai_citation:3‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
- ✅ **Supply chain & artifact integrity**: SBOM/SLSA ideas + cryptographic signing for data/code artifacts, and provenance attachments.  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC) [oai_citation:5‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
- ✅ **Privacy + inference control** for public APIs & aggregated outputs (query auditing, differential privacy concepts).  [oai_citation:6‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)

KFM’s north star is **trust-by-construction**: _no mystery layers_, _no uncited AI claims_, and _governance embedded at every step_.  [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:8‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 🧭 Scope & Non‑Goals

### In scope ✅
- Threat modeling (data → graph → AI → UI → exports)
- Authentication/authorization assumptions + policy enforcement points
- Rate limiting + input validation patterns for APIs
- Prompt security guardrails for LLM-facing surfaces
- Secrets hygiene (“no secrets in git”) + rollback playbooks
- Artifact signing + attestations (data + code)
- Privacy controls (sensitivity tiers, redaction, aggregation, inference control)

### Out of scope ❌
- Offensive exploitation steps
- Weaponized payloads
- Credential theft / malware workflows

---

## 🗂️ Directory Layout

mcp/
└─ 📓 notebooks/
   └─ 🛡️ 08_security_defensive/
      ├─ ✅📄 README.md                               # 👈 you are here 📌 Scope, safety rules, and how outputs become policy/runbooks
      ├─ 🧯📓 01_threat_model.ipynb                    # Threat modeling: assets, trust boundaries, abuse cases, mitigations
      ├─ ⚖️📓 02_policy_pack_opa_conftest.ipynb        # Policy-as-code: writing/testing OPA/Rego + Conftest gates
      ├─ 🛡️🌐📓 03_api_defenses_rate_limit_input_validation.ipynb
      │     # API defenses: rate limiting, input validation, request shaping, safe error handling
      ├─ 🧠🔒📓 04_prompt_security_focus_mode.ipynb     # Prompt security: injection patterns, containment, evidence-first rules
      ├─ 🔐📦📓 05_supply_chain_sbom_slsa_cosign.ipynb  # Supply chain: SBOM, SLSA provenance, signing (cosign), verification
      ├─ 🔒🧹📓 06_sensitive_data_privacy_inference_control.ipynb
      │     # Privacy: PII redaction, sensitivity labels, inference risk controls, safe logging
      ├─ 🚨🔁📓 07_incident_response_rollback.ipynb     # Incident response: rollback playbooks, comms, postmortem patterns
      └─ 📦 assets/
         ├─ ⚖️ policies/                               # Policy snippets + example Rego/Conftest configs used by notebooks
         ├─ 🧪 sample_data/                            # Tiny safe fixtures for demos/tests (no real secrets/PII)
         └─ 📝 reports/                                # Exported writeups/figures (threat models, checklists, summaries)
```

> [!NOTE]
> Notebook filenames are the **recommended canonical set** for this track.  
> If the repo uses different names, keep the same ordering & intent (threat model → policy gates → runtime defenses → incident playbooks).

---

## 🔒 KFM Defensive Principles (Non‑Negotiables)

### 1) “Fail closed” governance gates 🧱
KFM enforces automated policy gates at key checkpoints (ingestion, AI inference, publication). Minimum gates include schema validation, STAC/DCAT/PROV completeness, license presence, sensitivity classification, provenance completeness — and **AI answers must include citations** or they must refuse.  [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

### 2) Policy-as-code is the guardrail, not an afterthought 🧩
Governance rules are encoded in OPA (Rego) and tested in CI via Conftest; examples include “every dataset must have a license” and “AI outputs must include at least one citation”.  [oai_citation:10‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

### 3) Provenance-first intake + no “mystery layers” 🧾
Data intake is “provenance-first”: every piece of data carries lineage and reproducibility context; outputs are traceable to inputs and steps, and unsourced data is not accepted into the official catalog.  [oai_citation:11‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### 4) Focus Mode is retrieval + citations + governance checks 🤖🛡️
Focus Mode uses retrieval (graph + docs) and returns answers **with citations**. It includes a **governance check** stage before returning results.  [oai_citation:13‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
If it cannot ground an answer, it should refuse or clearly state uncertainty.  [oai_citation:14‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

### 5) Sensitive data handling is tied to FAIR+CARE 🧑‍⚖️
FAIR+CARE governance rules are being codified. Sensitive/culturally sensitive/PII content should be flagged and handled via restrictions, aggregation/redaction, and review triggers (e.g., sensitive areas like sacred sites).  [oai_citation:15‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)

### 6) Automation must be auditable + stoppable (kill switch) 🕵️🧯
Watcher–Planner–Executor automation is designed to open PRs (not auto-merge), keep operations idempotent/traceable, and includes a **kill-switch** to disable agent actions.  [oai_citation:16‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)

### 7) Supply chain integrity is part of “evidence-first” 📦🔏
KFM documents application security (auth, rate limiting, prompt security, secrets management, CSP) and supply chain practices (SBOM, dependency integrity).  [oai_citation:17‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
KFM also explores OCI-based artifact storage with Cosign signing and provenance attachments, including registry permission controls for restricted artifacts.  [oai_citation:18‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 🧠 Threat Model Snapshot

> [!TIP]
> Keep threat modeling boring and systematic. The win is **coverage + evidence**, not novelty.

### Trust boundaries (high level)
- **Browser/UI** ↔️ **API** (REST/GraphQL) ↔️ **Services** (Neo4j/PostGIS/search/object storage)  
  UI is decoupled from backend via APIs; provenance/citations must be surfaced to maintain trust.  [oai_citation:19‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt) [oai_citation:20‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)
- **CI/CD** ↔️ **Repo** ↔️ **Artifact registry / releases**
- **Work/Sandbox** ↔️ **Promoted/Published** (especially for simulations and experimental outputs)  [oai_citation:21‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

### What we defend (assets)
| Asset | Example threats | Primary defensive controls |
|---|---|---|
| 🔑 Identity & access | token theft, privilege escalation | authN/authZ, RBAC/ABAC policies, secrets management  [oai_citation:22‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC) |
| 🗺️ Data layers & downloads | sensitive leakage, unauthorized access | sensitivity classification + fail-closed policy gates  [oai_citation:23‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC) |
| 🧠 Focus Mode answers | hallucinations, prompt injection, leakage | prompt security layers + governance check + citations-required  [oai_citation:24‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg) [oai_citation:25‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC) |
| 🧾 Provenance chain | tampering, unverifiable outputs | PROV-required, evidence manifests, signed artifacts  [oai_citation:26‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T) [oai_citation:27‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T) |
| 🚚 Supply chain | dependency compromise, build tampering | SBOM + attestations + signature verification  [oai_citation:28‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC) [oai_citation:29‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe) |

---

## 🧱 Defense-in-Depth Map

### Layered controls (where to enforce what)
| Layer | Control | Evidence artifact |
|---|---|---|
| 🧑‍💻 Dev (local) | pre-commit lint, secret scanning, safe configs | scan report, lint report |
| 🧪 CI | OPA/Conftest policy checks, schema validation, unit tests | conftest output, validator logs  [oai_citation:30‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg) |
| 🏗️ Pipelines | “Detect → Validate → Promote” staged flow | run manifest, promotion PR  [oai_citation:31‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg) |
| 🧠 AI runtime | prompt gate + governance check (citations + no restricted output) | answer bundle w/ citations  [oai_citation:32‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg) |
| 🌐 API edge | auth, rate limiting, input sanitization, format allowlists | gateway logs, rate-limit metrics  [oai_citation:33‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC) |
| 📦 Release | SBOM, signatures, attestations, provenance attachments | SBOM + signature + attestation  [oai_citation:34‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe) |

---

## 📓 Notebook Lineup (Recommended)

### 📓 01_threat_model.ipynb
- Build a KFM-focused STRIDE-ish model (UI/API/graph/AI/artifacts)
- Identify trust boundaries & “data-to-answer” chain
- Output: `assets/reports/threat_model.md`

### 📓 02_policy_pack_opa_conftest.ipynb
- Use/extend OPA policy pack patterns for:
  - license required
  - STAC/DCAT/PROV completeness
  - sensitivity classification required
  - AI answers must include citations  
   [oai_citation:35‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg) [oai_citation:36‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

### 📓 03_api_defenses_rate_limit_input_validation.ipynb
- Defensive API patterns:
  - input sanitization
  - rate limiting
  - allowlisted formats for uploads
  - JWT/RBAC assumptions  
   [oai_citation:37‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

### 📓 04_prompt_security_focus_mode.ipynb
- Model the Focus Mode request pipeline and insert guardrails:
  - strict prompt templates with citations
  - governance check stage
  - “refuse if cannot cite” behavior  
   [oai_citation:38‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg) [oai_citation:39‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

### 📓 05_supply_chain_sbom_slsa_cosign.ipynb
- Artifact integrity:
  - SBOM generation concept
  - SLSA-like provenance attestations concept
  - OCI artifact storage + Cosign signing + PROV attachments  
   [oai_citation:40‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T) [oai_citation:41‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)

### 📓 06_sensitive_data_privacy_inference_control.ipynb
- Sensitivity tiers + FAIR+CARE governance triggers
- Privacy preserving patterns for public queries:
  - query auditing / inference control
  - differential privacy for aggregates  
   [oai_citation:42‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe) [oai_citation:43‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)

### 📓 07_incident_response_rollback.ipynb
- Incident drill: “PII slipped into a dataset”
- Emergency restriction → purge → revert → postmortem
- Use “kill switch” + rollback guidance  
   [oai_citation:44‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) [oai_citation:45‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)

---

## 🚀 Quickstart

> [!WARNING]
> Use **synthetic/sample data only** in this notebook track unless you are explicitly operating inside a governed, approved environment.

### 1) Run policy checks (CI parity, locally)
```bash
# Example (paths based on KFM docs)
conftest test -p tools/validation/policy ./data
```
Policy pack location and Conftest usage are described in the AI system overview.  [oai_citation:46‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

### 2) Generate “evidence artifacts” for notebooks
KFM emphasizes evidence-first outputs (citations, provenance, manifests). A notebook run should emit:
- `run_manifest.json` (inputs, hashes, params)
- `prov.jsonld` (W3C PROV-O)
- `report.md` (human explanation + links)

This aligns with KFM’s requirement that outputs remain traceable and auditable.  [oai_citation:47‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

### 3) Keep experiments in sandbox until promoted
Simulations/experimental outputs should stay in “workbench” areas and only become official after review/promotion.  [oai_citation:48‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 🧩 Policy Pack (OPA + Conftest)

KFM codifies governance rules via OPA (Rego) and runs them through Conftest in CI to block non-compliant changes.  [oai_citation:49‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

### Minimal policy patterns (pseudo‑Rego)
```rego
package kfm.governance

# 1) License required for every dataset metadata object
deny[msg] {
  input.kind == "dataset"
  not input.license
  msg := "Dataset missing license."
}

# 2) Sensitivity label required (public/internal/restricted)
deny[msg] {
  input.kind == "dataset"
  not input.sensitivity
  msg := "Dataset missing sensitivity classification."
}

# 3) AI answers must include citations (fail-closed)
deny[msg] {
  input.kind == "ai_answer"
  count(input.citations) == 0
  msg := "AI output missing citations."
}
```

> [!NOTE]
> The “AI output must include citations” rule is explicitly treated as a policy gate: if it can’t cite, it should refuse.  [oai_citation:50‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

---

## 🤖 Prompt Security & Focus Mode Guardrails

KFM’s Focus Mode pipeline includes a governance check and delivers answers with citations.  [oai_citation:51‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

### Defensive requirements to test in notebooks
- ✅ **Citations-or-refusal** behavior for all answers.  [oai_citation:52‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
- ✅ Prompt security layer to reduce prompt injection/misuse risk.  [oai_citation:53‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- ✅ “No output less restricted than inputs” (if retrieval touches restricted data, output must respect restrictions). (Recommended extension; implement as policy.)

### Evidence-first UI expectations
UI is designed to surface provenance and keep outputs traceable (layers with attributions; AI answers with citations).  [oai_citation:54‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)

---

## 🕵️ Privacy & Inference Control

Even without direct access to raw datasets, **outputs** can leak sensitive information through repeated querying or inference. The privacy-preserving data mining literature highlights:

- **Query auditing / inference control**: deny queries that enable disclosure of confidential data.  [oai_citation:55‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)
- **Differential privacy**: protect record-level privacy in query results, especially for aggregates.  [oai_citation:56‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)

### Where this fits in KFM (practical mapping)
- Public aggregate endpoints (stats dashboards, “counts by county”, time series summaries)
- Graph exploration queries that could reconstruct sensitive attributes through repeated probing
- “Nearby” queries for sensitive points (e.g., sacred sites) → require generalization, suppression, or review gates.  [oai_citation:57‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)

---

## 🧯 Incident Response & Rollback

### Scenario: Sensitive/PII data slipped through
KFM’s intake guidance anticipates emergency procedures:
- revoke public access immediately (flip classification to restricted)
- remove/purge the data, revert the commit, and improve policy checks
- treat it like a secrets incident: “no secrets in git” mindset applies for sensitive data too  [oai_citation:58‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

### Kill switch for automation agents
If an automated agent is producing risky PRs, disable agent actions immediately with the kill-switch configuration flag.  [oai_citation:59‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)

---

## 📦 Artifact Integrity (OCI + Signatures)

KFM explores an OCI artifact approach using Cosign + ORAS, with registry permission controls for restricted artifacts and provenance attachments (e.g., PROV JSON-LD) as referrers.  [oai_citation:60‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### Evidence-first Story Nodes (optional but powerful)
Story Nodes can carry:
- human citations block
- machine-readable evidence manifest (YAML/JSON)
- embedded PROV JSON-LD bundle tying the story to sources and generation activity  [oai_citation:61‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 🗄️ Database hygiene (geospatial note)

A practical defensive data separation pattern in PostGIS work:
- store spatial tables in a separate schema outside the default `public` schema (helps organization and separation of duties).  [oai_citation:62‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)

> [!CAUTION]
> Cookbook examples may show weak passwords for demonstration—**do not reuse** those patterns in real environments. (Use secrets managers + env vars.)  [oai_citation:63‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)

---

## 🧰 Definition of Done (for this notebook pack)

Inspired by the repo’s documentation expectations (purpose, directory layout, invariants, CI gates).  [oai_citation:64‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

- [ ] Each notebook produces a `report.md` + `run_manifest.json` + `prov.jsonld`
- [ ] A policy suite exists for: license, sensitivity, provenance completeness, AI citations
- [ ] At least one incident drill notebook exists and is runnable end-to-end
- [ ] Supply-chain notebook demonstrates SBOM + signature verification workflow (conceptual or implemented)
- [ ] Privacy notebook includes inference control tests for aggregate endpoints

---

## 📚 References & Project Files

### Core KFM docs (primary)
-  [oai_citation:65‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg) **Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖** (policy pack, prompt security layers, citations, W‑P‑E)  [oai_citation:66‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
-  [oai_citation:67‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC) **KFM – Comprehensive Architecture, Features, and Design** (fail-closed policy gates; security overview)  [oai_citation:68‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC) [oai_citation:69‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
-  [oai_citation:70‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt) **KFM – Comprehensive UI System Overview** (provenance surfaced; decoupled UI/API)  [oai_citation:71‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt) [oai_citation:72‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)
-  [oai_citation:73‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) **KFM Data Intake – Technical & Design Guide** (provenance-first intake; sandbox→promotion; rollback)  [oai_citation:74‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) [oai_citation:75‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) [oai_citation:76‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
-  [oai_citation:77‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) **KFM – Comprehensive Technical Documentation** (data contracts; no mystery layers)  [oai_citation:78‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
-  [oai_citation:79‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe) **🌟 Latest Ideas & Future Proposals** (FAIR+CARE codification; kill switch; supply chain rigour)  [oai_citation:80‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe) [oai_citation:81‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)
-  [oai_citation:82‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T) **Additional Project Ideas** (OCI artifacts + cosign/oras; evidence manifests)  [oai_citation:83‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T) [oai_citation:84‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
-  [oai_citation:85‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC) **Innovative Concepts to Evolve KFM** (CARE-informed governance; access controls; trust)  [oai_citation:86‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)
-  [oai_citation:87‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H) **Kansas-Frontier-Matrix: Open-Source Geospatial Historical Mapping Hub Design** (baseline system architecture + traceable metadata pattern)  [oai_citation:88‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)
-  [oai_citation:89‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) **MARKDOWN_GUIDE_v13 (Draft)** (documentation map + required structure)  [oai_citation:90‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### Security/privacy supporting refs (embedded docs)
-  [oai_citation:91‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH) **Data Mining — Concepts & Applications** (query auditing, inference control, differential privacy)  [oai_citation:92‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)
-  [oai_citation:93‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp) **Python Geospatial Analysis Cookbook** (PostGIS schemas; operational hygiene)  [oai_citation:94‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)

### PDF portfolios (open in Acrobat to access full embedded content)
-  [oai_citation:95‡AI Concepts & more.pdf](file-service://file-K6BctJjeUwvyCahLf9qdwr) **AI Concepts & more (portfolio)**  [oai_citation:96‡AI Concepts & more.pdf](file-service://file-K6BctJjeUwvyCahLf9qdwr)
-  [oai_citation:97‡Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf](file-service://file-RrXMFY7cP925exsQYermf2) **Data Management / Architectures / Data Science (portfolio)**  [oai_citation:98‡Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf](file-service://file-RrXMFY7cP925exsQYermf2)
-  [oai_citation:99‡Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf](file-service://file-RshcX5sNY2wpiNjRfoP6z6) **Maps / Google Maps / Virtual Worlds / WebGL (portfolio)**  [oai_citation:100‡Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf](file-service://file-RshcX5sNY2wpiNjRfoP6z6)
-  [oai_citation:101‡Various programming langurages & resources 1.pdf](file-service://file-4wp3wSSZs7gk5qHWaJVudi) **Various programming languages & resources (portfolio)**  [oai_citation:102‡Various programming langurages & resources 1.pdf](file-service://file-4wp3wSSZs7gk5qHWaJVudi)

---

## 🕰️ Version History

- **2026-01-20** — Initial README scaffold for `08_security_defensive` (defensive security + policy gates + provenance-first framing).

# 🧠 KFM AI Policy Rules (Focus Mode) — `POLICY_RULES.md`

![Policy as Code](https://img.shields.io/badge/policy%20as%20code-OPA%20%2B%20Rego-blue)
![Evidence First](https://img.shields.io/badge/evidence--first-No%20Source%2C%20No%20Answer-brightgreen)
![Security](https://img.shields.io/badge/security-least%20privilege-orange)
![RAG](https://img.shields.io/badge/architecture-RAG%20%2B%20Governance-purple)

> [!IMPORTANT]
> **These rules are non-negotiable.** If a feature cannot comply, it must be redesigned or blocked.  
> KFM’s AI is an **evidence-backed analyst**, not an oracle. ✅

---

## 🎯 Scope

This policy applies to **any** feature that uses an LLM or embedding model inside KFM, including:

- 💬 **Focus Mode** Q&A
- 🧾 Summaries / “explain this dataset”
- 🧩 Entity extraction / tagging
- 🗺️ Map-context explanations (time + place-aware answers)
- 🧠 Tool-using / agent-like flows (if enabled)

**Not** covered here (tracked elsewhere):
- 📥 Data ingestion pipeline governance (PROV + licensing) — only referenced as dependencies
- 🧪 Model training details (fine-tuning pipelines) — only referenced as constraints

---

## 🧭 Core Principles (Invariants)

These are the “physics” of the system — breaking them breaks trust:

1. **Evidence-first** ⛓  
   Every factual claim must be traceable to an approved source.

2. **No Source, No Answer** 🚫📄  
   If retrieval returns nothing relevant, the AI must **not guess**.

3. **Least privilege sandbox** 🧰🔒  
   The model is treated as untrusted: it generates text (and embeddings) — **nothing more**.

4. **Layered architecture, always** 🏗️  
   UI never talks to the model directly; all AI flows route through the governed API layer.

5. **Governance at boundaries** 🛡️  
   Policy gates exist at **ingestion**, **serving**, and **AI output**.

6. **Community & data sovereignty** 🤝  
   Sensitive knowledge (e.g., protected cultural sites) is controlled by policy + role-based access.

---

## 📦 Where These Rules “Live” (Typical Layout)

```text
docs/
└── architecture/
    └── ai/
        ├── POLICY_RULES.md              👈 you are here
        ├── OLLAMA_INTEGRATION.md
        └── (other AI docs)

policy/
├── ai_policies.rego                     🛡️ LLM behavior rules (citations, privacy, safety)
├── data_policies.rego                   📚 dataset metadata/licensing gates
├── security.rego                        🔐 access control & role rules
└── compliance.rego                      ✅ optional compliance/community constraints

src/
└── server/
    └── ai/
        ├── focus_pipeline.*             🧩 parse → retrieve → prompt → postprocess
        ├── prompt_gate.*                🧼 input filtering & sanitization
        ├── policy_checks.*              🛡️ OPA calls + local checks (citations, redaction)
        └── ollama_client.*              🧠 model API wrapper (generate/embed)
```

> [!NOTE]
> File names are illustrative but intentionally aligned to the project’s described modular AI layout.

---

## 🧱 Enforcement Gates (End-to-End)

```mermaid
flowchart LR
  U[User 🧑‍🚀] --> UI[Focus Mode UI 🗺️]
  UI --> API[Backend API Orchestrator 🧩]

  API --> PG[Prompt Gate 🧼\n(sanitize user input)]
  PG --> RET[Retrieval 🔎\n(Neo4j/PostGIS/Search/Vectors)]
  RET --> PROMPT[Prompt Builder 🧱\n(numbered SOURCES + rules)]
  PROMPT --> LLM[LLM Runtime 🧠\n(Ollama)]
  LLM --> PP[Postprocess ✂️\n(parse citations + structure)]
  PP --> OPA[OPA Policy Engine 🛡️\n(Rego decision)]
  OPA -->|allow| OUT[Answer ✅\n+ citations map]
  OPA -->|deny/transform| SAFE[Fallback 🚧\n+ redactions]
  OUT --> LOG[Provenance Ledger ⛓️]
  SAFE --> LOG
```

---

## ✅ Policy Matrix (What Must Be Enforced)

| ID | Policy Name | Level | Enforced At | Default On Fail |
|---:|------------|:-----:|-------------|-----------------|
| CIT-001 | At least one citation required | **MUST** | Postprocess + OPA | Block answer |
| CIT-002 | Every factual claim must be cited | **MUST** | OPA | Block or request clarification |
| CIT-003 | No invented citations | **MUST** | Postprocess + OPA | Block answer |
| CIT-004 | “No Source, No Answer” behavior | **MUST** | Prompt + Postprocess | Safe refusal |
| INP-001 | Prompt injection neutralization | **MUST** | Prompt Gate | Refuse / sanitize |
| INP-002 | Remove profanity / hate / disallowed requests | **MUST** | Prompt Gate | Refuse / sanitize |
| ACC-001 | Role-based access to sensitive datasets | **MUST** | Retrieval + OPA | Deny or mask |
| ACC-002 | No private personal data disclosure | **MUST** | Prompt Gate + OPA | Refuse |
| SAN-001 | LLM has no direct tool/DB/network access | **MUST** | Infrastructure | Not deployable otherwise |
| LOG-001 | Immutable provenance logging | **MUST** | API layer | Block feature release |
| GOV-001 | Versioned policies & policy hash logged | **SHOULD** | OPA + Logging | Warn + backlog task |
| CI-001 | Policy-as-code checks in CI | **SHOULD** | CI | PR fails |

---

# 📜 Policy Rules (Normative)

## RFC Keywords ✅
The keywords **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** are used as defined in RFC-style requirements.

---

## 🧾 A) Citation & Evidence Rules (CIT-*)



### CIT-001 — Citation Presence
- The final answer **MUST** contain **at least one** valid citation marker (e.g., `[1]`).
- If no markers exist, the system **MUST** discard the answer and return a safe fallback.

### CIT-002 — Cite Every Factual Claim
- Any factual statement (dates, counts, locations, claims about events, “X happened”) **MUST** have a citation.
- Non-factual content (formatting, transition sentences) **MAY** be uncited.

### CIT-003 — No Invented Sources
- The model **MUST NOT** cite sources that are not included in the retrieval bundle.
- Postprocessing **MUST** validate every marker points to a real source entry.

### CIT-004 — No Source, No Answer
- If retrieval yields no relevant sources, the answer **MUST** be:
  - a refusal (“I can’t find evidence in the approved sources”), or
  - a clarification question (“Which county/year/layer?”), **not** speculation.

### CIT-005 — Compact, High-Signal Context Only
- Retrieval **MUST** provide excerpts/snippets/facts (not entire articles).
- Prompt builder **MUST** pass sources as a numbered list for deterministic citing.

> [!TIP]
> “Citations are the product.” The narrative is just a helpful wrapper around traceable evidence.

---

## 🧼 B) Input Safety & Sanitization (INP-*) — “Prompt Gate”



### INP-001 — Prompt Injection Neutralization
- User input **MUST** be sanitized before it reaches the LLM.
- The Prompt Gate **MUST** neutralize or remove:
  - “Ignore previous instructions…”
  - attempts to exfiltrate system prompts, secrets, tokens, keys
  - attempts to force unsafe actions or bypass governance

### INP-002 — Disallowed Content Filtering
The Prompt Gate **MUST** block or sanitize:
- hate/harassment content
- sexual content involving minors (hard block)
- requests for private personal data (living individuals)
- instructions to commit wrongdoing or bypass security controls

### INP-003 — Preserve User Intent (When Safe)
- Sanitization **SHOULD** preserve benign intent (e.g., “summarize drought impacts”) while removing malicious payload.

---

## 🔎 C) Retrieval & Data Access Rules (RET-* / ACC-*)



### RET-001 — Approved Sources Only
- Retrieval **MUST** use only KFM-approved stores and indices:
  - Knowledge graph (Neo4j)
  - Spatial/statistical data (PostGIS)
  - Full-text index
  - Vector similarity index
- The LLM **MUST NOT** browse the internet or use external unvetted sources.

### RET-002 — Evidence Bundle Contract
Retrieval output **MUST** include:
- `source_id`
- `title`
- `type` (dataset/doc/graph-node/etc.)
- `snippet` (or structured fact payload)
- `license` (if applicable)
- `sensitivity` label (if applicable)

### ACC-001 — Role-Based Access Control (RBAC)
- Access to datasets and facts **MUST** be filtered by user role.
- If a dataset is **Restricted** (example: precise archeological site locations), the system **MUST** deny or mask.

### ACC-002 — Masking / Degradation Policy
When user lacks permissions:
- The system **MAY** return a degraded answer (e.g., county-level aggregation instead of exact coordinates).
- Any masking **MUST** be logged as a transformation decision.

---

## 🧠 D) Generation Rules (LLM-*)



### LLM-001 — “Use Only Provided Sources”
- Prompt templates **MUST** instruct the model to use **only** the provided evidence bundle.
- The model **MUST** treat anything outside SOURCES as unknown.

### LLM-002 — No Unapproved Tools
- By default, the model **MUST** have no tools beyond text generation (and embeddings if used).
- If tools are enabled, they **MUST** be:
  - explicitly whitelisted
  - validated server-side
  - policy-checked before execution and before returning results

### LLM-003 — Deterministic Output Contract
- The model output **SHOULD** be structured enough to reliably parse citations and extract the citations map.

---

## ✂️ E) Postprocessing Rules (POST-*)



### POST-001 — Citation Parsing & Validation
Postprocessing **MUST**:
- detect all citation markers
- validate marker indices exist
- build a `citations_map` (marker → source metadata)

### POST-002 — Refuse on Invalid Evidence
If the answer contains:
- zero citations
- invalid citation markers
- references to restricted info without authorization  
…then the response **MUST** be blocked or sanitized before user delivery.

---

## 🛡️ F) Governance Rules (OPA-*) — Open Policy Agent



### OPA-001 — OPA Decision Required
- Before returning any AI answer, the backend **MUST** obtain an OPA decision:
  - `allow: true/false`
  - optional `redactions[]`
  - optional `reason`

### OPA-002 — What OPA Must Check (Minimum)
OPA policies **MUST** evaluate:
- citations are present and valid
- content doesn’t violate safety rules
- sensitivity labels are honored
- user role permits access

### OPA-003 — Safe Fallback on Deny
If OPA denies:
- The user response **MUST** be a safe refusal or clarification prompt.
- The system **MUST NOT** leak restricted information in denial explanations.

---

## 🧾 G) Logging & Audit Rules (LOG-*)



### LOG-001 — Immutable Provenance Ledger
Every AI interaction **MUST** be logged with:
- question text (sanitized)
- user role (and pseudonymous user identifier if applicable)
- retrieved source IDs + sensitivity labels
- model ID + model version
- prompt template version/hash
- OPA decision + policy bundle hash/version
- any redactions/masking applied

### LOG-002 — Traceability as a Product Feature
- The UI **SHOULD** expose citations as clickable footnotes (source title + metadata).
- Admin/maintainer views **SHOULD** allow auditing by query id.

---

## 🧪 H) CI & Regression Rules (CI-*)



### CI-001 — Policy-as-Code Gate in PRs
- CI **SHOULD** run policy checks (e.g., Conftest against Rego) that can fail PRs for:
  - missing provenance files for new/updated datasets
  - missing license metadata
  - banned phrases in AI prompt templates
  - policy violations in configuration

### CI-002 — AI Regression Tests
- CI **SHOULD** include tests ensuring:
  - answers include citations under normal conditions
  - “no source” paths refuse correctly
  - restricted datasets are blocked/masked as expected

---

# 🧩 OPA Integration: Contracts & Examples

## 📥 Expected OPA Input Shape (Example)

```json
{
  "user": {
    "id_hash": "user_abc123",
    "role": "public"
  },
  "request": {
    "feature": "focus_mode",
    "question_sanitized": "What happened in Finney County in the 1930s?"
  },
  "retrieval": {
    "sources": [
      {
        "marker": 1,
        "source_id": "dataset_drought_1935",
        "title": "Drought Index 1935",
        "type": "dataset",
        "license": "CC-BY",
        "sensitivity": "public"
      }
    ]
  },
  "answer": {
    "text": "Severe drought impacts peaked around 1935 [1].",
    "citations_found": [1]
  }
}
```

## 📤 Expected OPA Output Shape (Example)

```json
{
  "allow": true,
  "redactions": [],
  "reason": "ok",
  "policy_bundle_hash": "sha256:..."
}
```

## 🧷 Minimal Rego Skeleton (Illustrative)

```rego
package kfm.ai

default allow := false

deny[msg] {
  count(input.answer.citations_found) == 0
  msg := "missing_citations"
}

deny[msg] {
  some i
  src := input.retrieval.sources[i]
  src.sensitivity == "restricted"
  input.user.role != "admin"
  msg := "restricted_source_not_allowed"
}

allow {
  not deny[_]
}
```

> [!WARNING]
> Rego above is **illustrative**. Actual rules must match your real role taxonomy + sensitivity labels.

---

# 🧯 Safe Fallback Templates (Copy/Paste Friendly)

### Missing evidence
> I can’t find supporting sources in the approved KFM data for that question.  
> Try specifying a county, year range, or dataset/layer to narrow the search.

### Restricted data
> I can’t share that level of detail because it comes from restricted or sensitive data.  
> I *can* provide a higher-level summary (county-level or aggregated) if you want.

### Policy blocked output
> I’m not able to provide that response due to KFM safety/governance policies.  
> If you rephrase your question with a narrower scope, I can try again using approved sources.

---

# ✅ Developer Checklist (PR Gate)

- [ ] Prompt templates instruct **“use only SOURCES”** + citations
- [ ] Prompt Gate sanitizes injection attempts & disallowed content
- [ ] Retrieval emits `source_id`, `license`, `sensitivity`, snippet/fact payload
- [ ] Postprocess validates citations + builds `citations_map`
- [ ] OPA decision is required before returning answers
- [ ] Provenance logging includes sources + model + prompt + policy hash
- [ ] Tests cover: citations present, “no source” refusal, restricted masking/deny

---

# 📚 Design Sources (Internal)

This file codifies constraints described across:
- `docs/architecture/ai/OLLAMA_INTEGRATION.md`
- `docs/architecture/AI_SYSTEM_OVERVIEW.md`
- `docs/architecture/system_overview.md`
- Project technical blueprint + system documentation PDFs shipped with this repo

---

**End of file.**


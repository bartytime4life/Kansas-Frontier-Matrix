# 🛡️ Policy Tests (tests/policy)

![Policy-as-Code](https://img.shields.io/badge/policy-as--code-OPA-blue) ![Default Deny](https://img.shields.io/badge/default-deny-critical) ![Fail Closed](https://img.shields.io/badge/fail--closed-required-red) ![Provenance First](https://img.shields.io/badge/provenance-first-success) ![FAIR+CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-governance-brightgreen)

> [!IMPORTANT]
> This folder contains the **tests** that prove our governance rules are enforceable, reviewable, and repeatable.  
> If we can’t test a rule, we don’t really control it.

---

## 🧭 What lives here

This directory is the “policy safety net” for the **Kansas Frontier Matrix (KFM)** stack: pipeline → catalog/provenance → database → API → UI. KFM’s blueprint explicitly rejects bypassing governance checks: the UI never directly touches databases, and all access is mediated through backend validation + governance rules.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

**These tests are designed to ensure:**
- ✅ **No data enters KFM without documentation** (metadata + provenance required).
- ✅ **Fail-closed behavior**: missing or uncertain info blocks actions (default-deny).
- ✅ **Tiered access + community control** (CARE “Authority to Control”).
- ✅ **AI output governance** (Focus Mode is constrained; citations required; forbidden info refused).

KFM is described as a provenance-first platform where datasets, stories, and even AI answers trace back to sources (“the map behind the map”).  [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🧠 Why policy tests exist

### 1) Governance is part of the architecture (not a PDF on a shelf)
KFM’s design includes concrete enforcement (validation + governance rules in the API layer, policy enforcement layers, and CI checks), not just guidelines.  [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 2) “Fail closed” is the default
KFM’s blueprint calls out “Fail Closed (Governance by Default)” explicitly: if a policy/check fails, the action is blocked (e.g., missing license causes CI failure; forbidden AI output is refused).  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 3) Provenance-first + FAIR/CARE require automation
KFM bakes FAIR + CARE into the workflow via required metadata/provenance and automated checks (e.g., license checks, tiered visibility).  [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 4) Trustworthy systems need “assurance,” not vibes
Digital Humanism governance work emphasizes that assurance depends on processes, policies, practices, and procedures across the lifecycle—including data governance.  [oai_citation:6‡Introduction to Digital Humanism.pdf](sediment://file_0000000090a071f5afd5c78c4383e488) [oai_citation:7‡Introduction to Digital Humanism.pdf](sediment://file_0000000090a071f5afd5c78c4383e488)

---

## 🧩 How policy fits into the KFM pipeline

KFM uses a strict canonical order and treats shortcuts as design flaws unless proven otherwise.  [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

```mermaid
flowchart LR
  A[📥 Raw data] --> B[🧼 Processed outputs]
  B --> C[🗂️ Catalog + Provenance]
  C --> D[🗄️ Database]
  D --> E[🧠 API (validation + governance)]
  E --> F[🖥️ UI / Focus Mode]
```

> [!NOTE]
> Policy tests should cover **every “gateway”** where a rule can be enforced: PR/CI, ingestion pipelines, API endpoints, and AI response post-processing.  [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 📦 Suggested folder layout (conventional)

> Your repo may differ—this is the intended shape for *policy-as-code testing* in KFM.

```text
tests/policy/
├── README.md                     # 👈 you are here
├── policies/                     # 🧠 policy modules (e.g., rego / rules)
│   ├── access_control.rego
│   ├── data_intake.rego
│   ├── licensing.rego
│   └── ai_response.rego
├── cases/                        # 🧪 test cases (inputs + expected decisions)
│   ├── access/
│   ├── intake/
│   ├── licensing/
│   └── ai/
└── fixtures/                     # 📦 reusable test data
    ├── users/
    ├── datasets/
    └── requests/
```

---

## ▶️ Run policy tests locally

> [!TIP]
> If you already have a task runner (Makefile, npm scripts, Poetry, etc.), mirror these commands behind a single `make policy-test`/`npm run policy:test` wrapper for consistency.

### Option A — OPA-native (if using Rego)
```bash
opa test ./tests/policy -v
```

### Option B — Docker (keeps CI/dev identical)
```bash
docker run --rm -v "$(pwd)":/workspace -w /workspace openpolicyagent/opa:latest \
  test ./tests/policy -v
```

### Option C — Python harness (if policy tests are scenario-based)
```bash
pytest -q tests/policy
```

---

## 🧪 Test taxonomy (what we verify)

### 1) 📥 Data intake must produce Catalog + Provenance
KFM’s pipelines are expected to output:
- processed data in `data/processed/`
- catalog metadata in `data/catalog/` (e.g., STAC items/collections, DCAT records)
- provenance logs in `data/provenance/` (W3C PROV lineage)

…and CI should reject contributions that don’t meet the documentation requirements (“no data enters KFM without documentation”).  [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

**Example test ideas**
- ✅ adding `data/processed/foo.geojson` requires `data/catalog/foo.stac.json` + `data/provenance/foo.prov.json`
- ✅ catalog entry must include license, spatial/temporal extent, and source info
- ✅ provenance must record inputs + transformation context (script version/commit, timestamps, outputs)

### 2) 📜 Licensing is mandatory (and enforced in CI)
KFM explicitly uses license checks as a governance gate; missing license blocks merge.  [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

**Example test ideas**
- ✅ deny ingest/merge if `license` is missing/unknown
- ✅ deny if license is incompatible with redistribution (project policy-specific)

### 3) 🔐 Tiered access control (CARE: Authority to Control)
KFM describes tiered visibility/access control and community ownership of sensitive data, including the ability to retract data when needed.  [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

The blueprint proposes metadata fields like `accessLevel` and `ownerGroup` to express restrictions and stewardship.  [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

**Example test ideas**
- ✅ `Restricted` datasets require membership in `ownerGroup`
- ✅ `Withdrawn`/retracted datasets deny access (even to admins) unless explicitly allowed for governance workflows
- ✅ public UI endpoints must never leak restricted metadata beyond safe summaries

### 4) 🧠 Focus Mode (AI) must be policy-constrained + evidence-backed
KFM states Focus Mode is not an ungoverned chatbot; it is constrained by policies for ethical and factual responses.  [oai_citation:15‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

KFM also describes an agentic/tool-using flow where the AI calls allowed tools (e.g., safe database search), synthesizes answers, and returns citations; provenance logs can capture intermediate steps.  [oai_citation:16‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:17‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

**Example test ideas**
- ✅ AI answer must include citations to KFM sources (or refuse)
- ✅ AI must refuse requests that would reveal forbidden/private info (“fail closed”)  [oai_citation:18‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- ✅ AI tool calls must go through approved tools/APIs only (no direct DB access)  [oai_citation:19‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- ✅ output filters enforce “no black-box answers” (traceability requirement)  [oai_citation:20‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 5) 🕵️ Audit logs + privacy preservation
Data Spaces research highlights that trustworthy data sharing ecosystems depend on robust governance models and adherence to best practices like provenance and quality assurance.  [oai_citation:21‡Data Spaces.pdf](sediment://file_0000000053c071f5a9733b1b09cc9f76)

It also describes access control patterns combining user context + data classification (e.g., public/internal/confidential/restricted) and stresses privacy-protecting approaches (e.g., pseudonymized logs).  [oai_citation:22‡Data Spaces.pdf](sediment://file_0000000053c071f5a9733b1b09cc9f76) [oai_citation:23‡Data Spaces.pdf](sediment://file_0000000053c071f5a9733b1b09cc9f76)

Digital Humanism explicitly frames privacy as a fundamental right and stresses that security and privacy are central to human-centered technology goals.  [oai_citation:24‡Introduction to Digital Humanism.pdf](sediment://file_0000000090a071f5afd5c78c4383e488)

**Example test ideas**
- ✅ audit logs do not store raw personal identifiers when not required
- ✅ access decisions can emit “reason codes” without leaking sensitive attributes
- ✅ data classification labels are always present and validated

---

## 🧱 Policy test input schema (recommended)

Use one consistent input shape so rules stay composable and tests stay readable.

```json
{
  "user": {
    "id": "user_123",
    "roles": ["read-only"],
    "groups": ["community_x"]
  },
  "resource": {
    "type": "dataset",
    "id": "census_1900",
    "classification": "restricted",
    "ownerGroup": "community_x",
    "status": "active",
    "license": "CC-BY-4.0"
  },
  "action": "read",
  "context": {
    "surface": "api",
    "purpose": "research",
    "requestId": "req_abc"
  }
}
```

This aligns with:
- KFM’s proposed `accessLevel`/`ownerGroup` concepts for tiered access.  [oai_citation:25‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- Data Spaces-style access control that combines **user context + data classification**.  [oai_citation:26‡Data Spaces.pdf](sediment://file_0000000053c071f5a9733b1b09cc9f76) [oai_citation:27‡Data Spaces.pdf](sediment://file_0000000053c071f5a9733b1b09cc9f76)

---

## ✍️ How to add a new policy test

1. 🧩 **Pick the domain**: `access/`, `intake/`, `licensing/`, `ai/`
2. 🧪 **Add a case**:
   - `cases/<domain>/<name>.input.json`
   - `cases/<domain>/<name>.expected.json` *(or expected allow/deny + reason codes)*
3. ✅ **Write/adjust the rule** in `policies/`
4. 🔁 **Run the suite**
5. 🧾 **Document rationale** in the case file header or a short `cases/<domain>/README.md`

> [!TIP]
> Keep tests small and “table-driven.” You want dozens of tiny cases rather than a few mega-scenarios.

---

## ✅ Core invariants checklist (must always be tested)

- [ ] **Default deny**: if anything is missing/unknown → deny.  [oai_citation:28‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- [ ] **License required** for any dataset exposed/merged.  [oai_citation:29‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- [ ] **Metadata + provenance required** for processed data.  [oai_citation:30‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- [ ] **Tiered access enforced** for sensitive/community data (CARE authority).  [oai_citation:31‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:32‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- [ ] **AI answers cite sources or refuse**; no black-box outputs.  [oai_citation:33‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- [ ] **UI never bypasses governance** (no direct DB access).  [oai_citation:34‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🔒 Local LLM + privacy (Focus Mode alignment)

Ollama is explicitly positioned as a way to run models locally/offline so prompts/responses don’t leave the machine—useful for sensitive contexts.  [oai_citation:35‡Comprehensive Guide to Ollama and Its Supported Open-Source LLMs.pdf](file-service://file-WLPhJVNoBxYKcy3utQSwBi)

**Policy test implication:** when Focus Mode uses local inference, tests should still enforce the same governance gates:
- tool calls must be approved
- access control must be enforced
- citations required
- no forbidden disclosure

---

## 🧰 Policy + documentation discipline

Our project’s documentation protocol emphasizes meticulous tracking and domain-specific documentation (datasets, preprocessing, model documentation). Treat policy tests as part of that reproducibility envelope.  [oai_citation:36‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

---

## 📚 References (project sources)

- **Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint**  [oai_citation:37‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)  
  Evidence for provenance-first design, policy enforcement layers, fail-closed governance, and Focus Mode constraints.  [oai_citation:38‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:39‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

- **Data Spaces**  [oai_citation:40‡Data Spaces.pdf](sediment://file_0000000053c071f5a9733b1b09cc9f76)  
  Trust + governance challenges, access control patterns using user context and data classification, privacy-preserving logging considerations.  [oai_citation:41‡Data Spaces.pdf](sediment://file_0000000053c071f5a9733b1b09cc9f76) [oai_citation:42‡Data Spaces.pdf](sediment://file_0000000053c071f5a9733b1b09cc9f76) [oai_citation:43‡Data Spaces.pdf](sediment://file_0000000053c071f5a9733b1b09cc9f76)

- **Introduction to Digital Humanism**  [oai_citation:44‡Introduction to Digital Humanism.pdf](sediment://file_0000000090a071f5afd5c78c4383e488)  
  Human-centered goals, privacy as a fundamental right, and governance/assurance framing for AI + data governance.  [oai_citation:45‡Introduction to Digital Humanism.pdf](sediment://file_0000000090a071f5afd5c78c4383e488) [oai_citation:46‡Introduction to Digital Humanism.pdf](sediment://file_0000000090a071f5afd5c78c4383e488) [oai_citation:47‡Introduction to Digital Humanism.pdf](sediment://file_0000000090a071f5afd5c78c4383e488)

- **Comprehensive Guide to Ollama and Its Supported Open-Source LLMs**  [oai_citation:48‡Comprehensive Guide to Ollama and Its Supported Open-Source LLMs.pdf](file-service://file-WLPhJVNoBxYKcy3utQSwBi)  
  Local/offline execution rationale for privacy-sensitive workflows.  [oai_citation:49‡Comprehensive Guide to Ollama and Its Supported Open-Source LLMs.pdf](file-service://file-WLPhJVNoBxYKcy3utQSwBi)

- **Scientific Method / Research / Master Coder Protocol Documentation**  [oai_citation:50‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)  
  Documentation rigor and dataset/model documentation expectations.  [oai_citation:51‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)
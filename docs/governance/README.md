# 🏛️ Governance (Kansas Frontier Matrix / Kansas-Matrix-System)

![Docs](https://img.shields.io/badge/docs-governance-blue?style=for-the-badge)
![Policy-as-Code](https://img.shields.io/badge/policy--as--code-OPA%20%2B%20CI-informational?style=for-the-badge)
![Default](https://img.shields.io/badge/default-fail%20closed-critical?style=for-the-badge)
![Trust](https://img.shields.io/badge/trust-provenance%20%2B%20audit-2ea44f?style=for-the-badge)

> **Governance is a first-class feature.** We encode rules in both **human process** and **machine-enforced gates** so data, maps, and AI outputs stay trustworthy, auditable, and respectful.

---

## 🧭 Quick Navigation

- [🎯 Purpose & scope](#-purpose--scope)
- [🧩 Governing principles](#-governing-principles)
- [👥 Roles & responsibilities](#-roles--responsibilities)
- [🏛️ Councils & oversight](#-councils--oversight)
- [🧱 Policy-as-code](#-policy-as-code)
- [🗂️ Data lifecycle governance](#-data-lifecycle-governance)
- [🧾 Provenance & audit trails](#-provenance--audit-trails)
- [🔐 Privacy, sensitive data, and community control](#-privacy-sensitive-data-and-community-control)
- [🛡️ Security & supply chain integrity](#️-security--supply-chain-integrity)
- [🤖 AI governance](#-ai-governance)
- [🗳️ Decision records](#️-decision-records)
- [🚨 Incidents & exception handling](#-incidents--exception-handling)
- [🧰 Templates](#-templates)
- [📦 Suggested folder layout](#-suggested-folder-layout)
- [📚 Grounding sources](#-grounding-sources)

---

## 🎯 Purpose & scope

This folder defines **how we make decisions** and **how we enforce trust** across:

- 📦 **Data** (ingestion, licensing, sensitivity classification, retirement)
- 🗺️ **Maps & narratives** (publication rules, review standards)
- 🤖 **AI outputs** (citations required, policy checks, logging)
- 🔒 **Security & privacy** (least privilege, audits, incident response)
- 🧑‍🤝‍🧑 **Community & ethics** (FAIR+CARE, Indigenous data sovereignty)

---

## 🧩 Governing principles

### 1) ✅ Fail-closed by default  
If anything is missing (license, metadata, sensitivity label, provenance), we **block** the action instead of “best-effort passing.” [oai_citation:0‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### 2) 🧪 Evidence-first and reproducible  
Anything we publish should be traceable back to sources, transformations, and approvals. Provenance is not optional. [oai_citation:1‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### 3) 🧭 Open-by-default, but not reckless  
We favor openness and interoperability—but restrict, aggregate, or withhold where privacy, safety, or community control requires it. [oai_citation:2‡Kansas Frontier Matrix (KFM) – Unified Technical Blueprint.pdf](sediment://file_0000000000d8722f9ee56b2c59e5a887)

### 4) 🪶 FAIR + CARE as operating system  
We treat **FAIR** (Findable, Accessible, Interoperable, Reusable) and **CARE** (Collective Benefit, Authority to Control, Responsibility, Ethics) as enforceable expectations, not slogans. [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 5) 🔐 Least privilege everywhere  
Users/services get only the permissions they need. Authorization is enforced consistently at runtime and in CI.  [oai_citation:4‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 👥 Roles & responsibilities

> Roles shown below are the baseline RBAC model used throughout the system. [oai_citation:5‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

| Role | ✅ Typical capabilities | 🚫 Not allowed / guarded actions |
|---|---|---|
| **Public Viewer** | Read **publicly approved** datasets & stories | Access restricted datasets; bypass API rules |
| **Contributor** | Draft story nodes; suggest data; open PRs | Publish datasets directly; run ingestion; override policies |
| **Maintainer** | Review/approve contributions; manage content | “Approve without checks” (CI/policy gates still apply) |
| **Admin** | Run ingestion pipelines; configure policies | Bypass governance gates (still audited & policy-bound) |

### Supporting functions (not always GitHub roles)

- 🧑‍🔬 **Data Steward / Data Owner**: accountable for source accuracy & update cadence, plus dataset metadata quality. [oai_citation:6‡Kansas Frontier Matrix (KFM) – Unified Technical Blueprint.pdf](sediment://file_0000000000d8722f9ee56b2c59e5a887)
- 🔐 **Security & Compliance**: audits, monitoring, incident response readiness. [oai_citation:7‡Kansas Frontier Matrix (KFM) – Unified Technical Blueprint.pdf](sediment://file_00000000ec9c71f8ab8a6826cbce8605)
- 🧭 **Governance Board / Council**: approves inclusion of datasets and ethical guidelines for data + AI use. [oai_citation:8‡Kansas Frontier Matrix (KFM) – Unified Technical Blueprint.pdf](sediment://file_0000000000d8722f9ee56b2c59e5a887)

---

## 🏛️ Councils & oversight

Governance is both **automated** and **human-led**.

**Multi-tier oversight** (conceptual model):
- 🧬 **FAIR+CARE Council**
- 🪶 **Indigenous Data Governance Board**
- 🤖 **AI Oversight Board**
- 🛡️ **Security/Cybersecurity Subcommittee** (privacy, incidents, audits)

These bodies define policy direction; policy-as-code enforces it in runtime/CI. [oai_citation:9‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695) [oai_citation:10‡Kansas Frontier Matrix (KFM) – Unified Technical Blueprint.pdf](sediment://file_00000000ec9c71f8ab8a6826cbce8605)

**Escalation rule**: if a decision impacts **privacy**, **community control**, or **model behavior**, escalate to the relevant council/board even if code checks pass.

---

## 🧱 Policy-as-code

We enforce governance rules using:

- **Runtime authorization policies** (e.g., via Open Policy Agent / “policy pack”) for every request and for AI outputs. [oai_citation:11‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695) [oai_citation:12‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- **CI policy checks** (e.g., Conftest) to prevent non-compliant data/code merges (missing license, missing sensitivity label, missing provenance, etc.). [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 🔑 Golden rules (non-negotiable)

- 📜 **No license → no merge / no publish** [oai_citation:14‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- 🧾 **No provenance → not publishable** [oai_citation:15‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- 🧷 **No sensitivity label → no serve** (data must be classified before exposure) [oai_citation:16‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- 🤖 **No source → no answer** (AI must cite or refuse) [oai_citation:17‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 🗂️ Data lifecycle governance

### Canonical pipeline order ✅  
All data must flow through the “truth path”:

**Raw → Processed → Catalog/Prov → Database → API → UI** [oai_citation:18‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

Shortcuts are considered flawed unless there is a documented exception with council approval.

### Onboarding checklist ✅

A dataset cannot move forward unless it has:

- 🧾 **Source manifest** (publisher, license, classification) [oai_citation:19‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- 🧭 **Metadata** (STAC/DCAT as applicable) [oai_citation:20‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- 🧬 **Provenance** (PROV record capturing lineage) [oai_citation:21‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### Publication gates 🚦

- **Ingestion gate**: blocks if manifest/license/classification missing. [oai_citation:22‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- **Catalog gate**: blocks if STAC/DCAT/PROV links missing. [oai_citation:23‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- **AI gate**: blocks if missing citations or violates sensitivity/safety policy. [oai_citation:24‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 🧾 Provenance & audit trails

Provenance logging is **mandatory**:

- Every catalog dataset must have an associated **PROV** record; otherwise it is treated as **not publishable**. [oai_citation:25‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- Pipeline runs produce manifest logs (checksums, timestamps, “who ran it”) and are stored as immutable records (e.g., under `data/provenance/`). [oai_citation:26‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- AI interactions (question, sources, model version, policy decision) are recorded in an append-only ledger for auditability. [oai_citation:27‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 🔐 Privacy, sensitive data, and community control

### Privacy by design
- Minimize handling of PII; de-identify before becoming part of the open catalog.
- Use established privacy practices (purpose limitation, data minimization, consent, correction) and align with modern privacy standards **in spirit**. [oai_citation:28‡Kansas Frontier Matrix (KFM) – Unified Technical Blueprint.pdf](sediment://file_00000000ec9c71f8ab8a6826cbce8605)

### Sensitive locations & sensitive communities
For archeological sites, sacred lands, or other sensitive contexts, public presentation may require:
- aggregation (e.g., county-level instead of exact coordinates),
- rounding/generalization, or
- suppression/redaction when required. [oai_citation:29‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### Indigenous data sovereignty
Data contributed by Indigenous communities is governed under an Indigenous Data Sovereignty posture, with community control over labeling and sharing. [oai_citation:30‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 🛡️ Security & supply chain integrity

Security governance includes:
- mandatory security training,
- periodic audits of access rights,
- logged and auditable access—especially for sensitive datasets,
- an incident response plan (breach/leak handling). [oai_citation:31‡Kansas Frontier Matrix (KFM) – Unified Technical Blueprint.pdf](sediment://file_00000000ec9c71f8ab8a6826cbce8605)

Supply chain integrity expectations:
- code review for changes,
- SBOMs for releases,
- build provenance (e.g., SLSA),
- signed/verified containers,
- CI vulnerability scans (e.g., OWASP tooling),
- secure deployment defaults (HTTPS/HSTS, CSP, security headers). [oai_citation:32‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 🤖 AI governance

### “Least privilege” model
AI operates as an untrusted sandbox:
- it only sees **provided snippets** (no open internet access),
- outputs must be policy-checked,
- and everything is logged for later audit. [oai_citation:33‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### Policy check for AI answers
Before returning an answer, policy enforcement verifies:
- required citation markers are present,
- content does not violate safety rules or sensitivity labels,
- the user’s role permits viewing the information,
- otherwise the response is refused/redacted with a safe fallback. [oai_citation:34‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 🗳️ Decision records

Major decisions must be documented and discoverable (examples):
- releasing a dataset of concern,
- introducing/changing an AI model,
- changing sensitivity classifications,
- adding new governance gates.

Decision records may be stored in machine-readable formats (e.g., JSON-LD) to support transparency and auditability. [oai_citation:35‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 🚨 Incidents & exception handling

### Incident response (security/privacy)
- Contain & classify: reclassify data, purge caches if needed, restrict access.
- Notify governance/security oversight and perform a post-mortem review. [oai_citation:36‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### Exceptions (“break-glass”)
Exceptions are rare and must:
- be time-boxed,
- be logged,
- include an after-action review and policy update proposal.

---

## 🧰 Templates

<details>
<summary><strong>📦 Dataset Onboarding Request</strong> (copy/paste)</summary>

```markdown
## Dataset Onboarding Request

**Name/ID:**  
**Source / Publisher:**  
**License:**  
**Update cadence:**  
**Sensitivity classification:** (public/internal/confidential/restricted)  
**Intended use:**  
**Risks/constraints:** (PII? sensitive locations? community-owned?)  
**Required metadata:** (STAC/DCAT fields)  
**Provenance plan:** (inputs → transforms → outputs)  
**Steward/Owner:**  
**Approvals needed:** (FAIR+CARE / Indigenous / Security / AI)
```
</details>

<details>
<summary><strong>🧱 Policy Change Proposal</strong> (copy/paste)</summary>

```markdown
## Policy Change Proposal

**Policy area:** (data / AI / access control / release)  
**Problem statement:**  
**Proposed rule change:**  
**Rationale (evidence):**  
**Expected impact:** (users, datasets, workflows)  
**Backwards compatibility:**  
**Test plan:** (CI checks / Conftest / regression)  
**Rollout plan:** (phased? flag? immediate?)  
**Approvals needed:** (which council/board?)
```
</details>

<details>
<summary><strong>🗳️ Decision Record (ADR-lite)</strong> (copy/paste)</summary>

```markdown
## Decision Record

**Date:**  
**Decision owner:**  
**Context:**  
**Decision:**  
**Alternatives considered:**  
**Consequences / tradeoffs:**  
**Policy/code references:**  
**Approvals:**  
**Follow-ups:**  
```
</details>

---

## 📦 Suggested folder layout

```text
📁 docs/
  📁 governance/
    📝 README.md                # You are here
    🏛️ council-structure.md     # Council composition & escalation paths
    📁 decisions/               # Decision records (ADR/JSON-LD)
    📁 policies/                # Policy-as-code docs & rationale
    📁 templates/               # Copy/paste templates for requests
```

---

## 📚 Grounding sources

The governance rules above are grounded in the project’s design/blueprint docs, especially:

- Security & governance as “fail closed,” RBAC roles, and OPA enforcement. [oai_citation:37‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- Mandatory provenance, immutable pipeline manifests, and AI audit ledger. [oai_citation:38‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- Policy gates for ingestion/catalog/AI outputs and “block over allow.” [oai_citation:39‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- Privacy-by-design, audits, and incident response planning. [oai_citation:40‡Kansas Frontier Matrix (KFM) – Unified Technical Blueprint.pdf](sediment://file_00000000ec9c71f8ab8a6826cbce8605)
- FAIR+CARE and canonical pipeline order (Raw → … → UI). [oai_citation:41‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
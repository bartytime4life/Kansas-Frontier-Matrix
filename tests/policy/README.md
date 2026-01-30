# 🧪🛡️ Policy Test Suite (OPA/Conftest) — `tests/policy/`

![Policy-as-Code](https://img.shields.io/badge/policy-as--code-2b2b2b)
![OPA](https://img.shields.io/badge/OPA-Open%20Policy%20Agent-2b2b2b)
![Rego](https://img.shields.io/badge/Rego-ruleset-2b2b2b)
![Conftest](https://img.shields.io/badge/Conftest-policy%20testing-2b2b2b)

> **According to a document from 2026-01-29**, KFM treats `policy/` as the source of truth and enforces governance both:
> - **in CI** via Conftest checks (e.g., missing PROV metadata or banned AI phrases fail the build), and  
> - **at runtime** via OPA decisions (deny / allow / sanitize).:contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}

---

## 🎯 What this folder is

This folder contains **test cases + fixtures** for KFM’s **policy-as-code** gates.

KFM is designed to be **fail-closed**: if a policy or compliance check fails, the action is blocked (CI blocks merge; runtime blocks requests / AI output).:contentReference[oaicite:2]{index=2}

These tests exist to protect the system’s core promises:

- **Pipeline integrity** (Raw → Processed → Catalog/PROV → Database → API → UI):contentReference[oaicite:3]{index=3}
- **FAIR + CARE governance-by-default** (metadata completeness, licensing, provenance, access control, sensitive handling):contentReference[oaicite:4]{index=4}:contentReference[oaicite:5]{index=5}
- **“API-mediated access only”** (UI does not talk to databases directly; policy enforcement happens in the API layer):contentReference[oaicite:6]{index=6}

---

## ⚡ Quickstart (run policy tests locally)

> [!TIP]
> Run these from the **repo root** so Conftest can find the policy bundle under `policy/`.

### ✅ Run all policy checks
```bash
conftest test .
```
:contentReference[oaicite:7]{index=7}

### 🎯 Run checks on a specific file or subtree
```bash
conftest test data/processed/mydata.csv
# or
conftest test data/
```
:contentReference[oaicite:8]{index=8}

### 🧠 What to do when it fails
CI/local output typically includes **which Rego rule was violated** and a human-readable message to fix (e.g., “Dataset missing license”, missing PROV, banned phrase in a prompt).:contentReference[oaicite:9]{index=9}

---

## 🧩 What we test (policy coverage map)

### 1) 📦 Data onboarding gates (FAIR checklist)
KFM treats FAIR as an enforceable checklist—**if requirements aren’t met, the data doesn’t enter**.:contentReference[oaicite:10]{index=10}

Typical policy assertions validated here:
- Processed data must be **cataloged** and have **provenance** entries (CI ensures new processed files have corresponding `data/catalog` + `data/provenance`).:contentReference[oaicite:11]{index=11}
- Metadata must include at minimum **license + citation** (enforces “Reusable” legal clarity).:contentReference[oaicite:12]{index=12}
- Cross-layer alignment: **STAC + DCAT + PROV** required, and CI validates conformance to KFM profiles.:contentReference[oaicite:13]{index=13}

### 2) 🔐 Access control + sovereignty (CARE: Authority to Control)
KFM supports **restricted datasets** controlled by a group, with policy conditions like:
- `accessLevel: "Restricted"`
- `ownerGroup: "TribeABC"`
- allow only if `user.groups` contains `ownerGroup`
- deny all access if dataset `status: "withdrawn"` (takedown respected):contentReference[oaicite:14]{index=14}

### 3) 🤖 AI guardrails (safe & governed “Focus Mode”)
KFM’s AI assistant is explicitly **not an ungoverned chatbot**; it is constrained by policy for ethical + factual responses.:contentReference[oaicite:15]{index=15}

Examples of guardrails covered by policy tests:
- **Banned phrase** / disallowed prompt patterns → CI failure (contributors must remove/adjust).:contentReference[oaicite:16]{index=16}
- **Restricted information leakage** → OPA denies or requires sanitization before output.:contentReference[oaicite:17]{index=17}

### 4) 🧯 Governance scans (secrets, PII, sensitive locations, classification drift)
KFM’s CI includes governance/security scans to prevent “oops we shipped it” failures:
- secret scanning (keys/tokens/passwords)
- PII/sensitive data scans
- sensitive location checks (ensure protected coordinates aren’t exposed)
- classification consistency (don’t downgrade data classification through processing without approved de-identification):contentReference[oaicite:18]{index=18}

---

## 🗂️ Recommended folder layout (for this `tests/policy/` suite)

> [!NOTE]
> If the repository already has a different structure, keep it — but try to preserve the same intent.

```text
📁 tests/
└─ 📁 policy/                               🛡️ policy-as-code tests (fail-closed governance gates)
   ├─ 📄 README.md                            📘 how policy tests run + what they enforce
   ├─ 📁 fixtures/                            🧰 governed fixtures (small + synthetic)
   │  ├─ 📁 data/                              📦 sample datasets / metadata objects (STAC/DCAT/PROV snippets)
   │  ├─ 📁 users/                             👤 user contexts (roles, groups, orgs)
   │  └─ 📁 ai/                                🤖 prompt + answer contexts (citations, attachments, controls)
   └─ 📁 cases/                                🧪 executable policy scenarios (organized by lane)
      ├─ 📁 fair/                              ✅ metadata/provenance/license gates (FAIR)
      ├─ 📁 care/                              🧑‍🤝‍🧑 access control & takedown rules (CARE)
      ├─ 📁 ai/                                🤖 AI policy enforcement cases (Focus Mode guardrails)
      └─ 📁 scans/                             🔎 PII/secret/sensitive-location cases (if applicable)
```

---

## 🧰 How CI uses these tests

When you open a PR, CI runs lint/tests plus **policy checks**. If policy fails, CI blocks the merge and tells you what rule failed and why.:contentReference[oaicite:19]{index=19}

Common CI-triggered fixes:
- add missing **license** or **citation** to metadata
- add missing **PROV** record / provenance entry
- remove banned phrase / update AI prompt content
- ensure processed data is linked in catalogs/provenance correctly:contentReference[oaicite:20]{index=20}:contentReference[oaicite:21]{index=21}

---

## 🧱 Writing policy tests (conventions that keep us sane)

### ✅ Test case anatomy (recommended)
Each test case should include:
- **Input**: a realistic fixture (dataset metadata, request context, AI response context, etc.)
- **Expectation**: allow/deny/sanitize + (optional) reason string
- **Minimal blast radius**: only test one rule-family per case

### 🧠 “Fail closed” mindset
Policies and checks should err on the side of caution: incomplete metadata, unclear licensing, or missing governance tags should default to deny/fail until explicitly compliant.:contentReference[oaicite:22]{index=22}

---

## 🧪 Runtime parity (don’t test CI-only behavior)

KFM policies are used in **two places**:
1) CI gates (Conftest)  
2) Runtime enforcement (OPA called by API or embedded evaluation)

OPA integration can be sidecar-based or embedded, but either way `policy/` remains the source of truth; API checks can deny access, or return sanitized results (e.g., mask/round sensitive locations).:contentReference[oaicite:23]{index=23}

> [!IMPORTANT]
> If you add a CI rule that has runtime impact, add at least one “runtime-shaped” fixture:
> - user role/group context  
> - dataset sensitivity/accessLevel  
> - AI answer references + sensitivity tags

---

## 🧾 Auditability & policy versioning

OPA decisions can be tied to a **policy bundle hash / commit**, enabling “why was this blocked?” traceability later (e.g., “blocked by `ai_policies.rego` (commit …)”).:contentReference[oaicite:24]{index=24}

This suite should keep tests stable across time by:
- pinning fixtures to explicit, readable fields
- avoiding “today/now” dependencies
- preferring explicit expected messages

---

## 🧑‍⚖️ Governance review triggers (beyond automated tests)

Some changes require manual governance review even if tests pass:
- introducing culturally sensitive or sovereignty-tagged datasets (e.g., precise archaeological site locations)
- adding AI narrative features that could be perceived as factual (must include safeguards + disclosures)
- integrating new external data sources (license + provenance + standards alignment review):contentReference[oaicite:25]{index=25}

---

## 🔎 Glossary (quick ref)

- **OPA**: Policy engine that evaluates rules at runtime for allow/deny/sanitize decisions.:contentReference[oaicite:26]{index=26}
- **Conftest**: CI/local policy test runner applying Rego policies to files in the repo.:contentReference[oaicite:27]{index=27}
- **Rego**: Policy language used by OPA/Conftest.
- **FAIR + CARE**: Governance principles encoded into workflow + policy gates.:contentReference[oaicite:28]{index=28}:contentReference[oaicite:29]{index=29}
- **STAC / DCAT / PROV**: Required metadata/catalog/provenance layers validated by CI.:contentReference[oaicite:30]{index=30}

---

## 📎 References (project docs used to shape this suite)

- KFM blueprint: OPA + Conftest, fail-closed governance, FAIR/CARE, runtime enforcement patterns.:contentReference[oaicite:31]{index=31}:contentReference[oaicite:32]{index=32}
- KFM Markdown/standards guide: STAC/DCAT/PROV alignment + CI governance scans.:contentReference[oaicite:33]{index=33}:contentReference[oaicite:34]{index=34}
- Data classification & policy enforcement patterns (reference model): role-based access control + policy enforcement sequencing.:contentReference[oaicite:35]{index=35}:contentReference[oaicite:36]{index=36}


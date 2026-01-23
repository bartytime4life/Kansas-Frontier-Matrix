---
title: "MCP Gate Example 06 — Privacy 🔒"
path: "mcp/gates/examples/06-privacy/README.md"
version: "v0.1.0"
last_updated: "2026-01-23"
status: "draft"
doc_kind: "Example / Guide"
license: "CC-BY-4.0"
fair_category: "FAIR+CARE"
---

# 🔒 MCP Gate 06 — Privacy (KFM-style)

![MCP Gate](https://img.shields.io/badge/MCP%20Gate-Privacy-8A2BE2)
![Policy as Code](https://img.shields.io/badge/Policy%20as%20Code-OPA%20%2F%20Rego-1f6feb)
![CI Friendly](https://img.shields.io/badge/CI-Conftest%20Ready-success)
![Default](https://img.shields.io/badge/Default-Fail%20Closed-critical)
![Focus Mode](https://img.shields.io/badge/Integrates-Focus%20Mode%20%26%20UI-informational)

A **Privacy Gate** is the “last line of defense” that prevents KFM (and any KFM-derived system) from leaking **sensitive locations**, **personal data**, or **sovereign/culturally governed knowledge**—even when everything else “looks fine.”

This example turns KFM’s privacy philosophy into **policy-as-code** so it can run:
- ✅ in **CI** (pre-merge / pre-release)
- ✅ at **runtime** (API queries, exports, tile serving, AI answers)
- ✅ inside **UI flows** (warnings, role-based visibility, export blocks)
- ✅ inside **Focus Mode** governance checks (redaction + refusal)

> [!IMPORTANT]
> This is an engineering implementation pattern, not legal advice. If you introduce regulated datasets (e.g., health), involve a qualified reviewer.

---

## 🧭 Why KFM needs a Privacy Gate

KFM is designed to be evidence-first and transparent, but **not everything should be equally public**:
- **Sensitive geospatial points** (e.g., archaeological sites, endangered species habitat) can enable harm if exposed precisely.
- **Living persons’ data** (names, addresses, contact info) must not be published.
- **Cultural/sovereign data** may require **community approval** and **differential access** (not “open by default”).

Privacy must be enforced in a **fail-closed** way: if the system can’t prove it’s safe to show, it **doesn’t show it**. 🛑

---

## 🧠 What the gate decides

This gate returns one of three outcomes:

| Outcome | Meaning | Example |
|---|---|---|
| ✅ Allow | Safe to return as-requested | Public dataset + coarse results |
| ✅ Allow + Obligations | Allowed only if we transform/label/log | “Show it, but round coordinates to ~10 km and add a warning” |
| ❌ Deny | Not safe, or missing required approvals | Confidential data + unauthorized user, or “exact sacred site coordinates” |

### Decision contract (recommended)
```json
{
  "allow": false,
  "reason": "confidential_requires_authorization",
  "obligations": [
    {
      "type": "ui_warning",
      "severity": "danger",
      "message": "This request involves restricted data."
    },
    {
      "type": "audit_log",
      "event": "privacy.denied"
    }
  ]
}
```

---

## 🗺️ Where this gate sits in the KFM pipeline

```mermaid
flowchart LR
  A[🧪 Data Intake] --> B[🧱 Process/Normalize]
  B --> C[📦 Publish / Serve]
  C --> D[🖥️ UI Layer]
  C --> E[🤖 Focus Mode]
  D --> F[👤 User]
  E --> F

  subgraph Gates ✅
    G1[🔍 Ingestion Gate]
    G2[📜 Policy Gates (CI)]
    G3[🔒 Privacy Gate (Runtime)]
    G4[🧾 Citation Gate (AI)]
  end

  A --> G1 --> B
  B --> G2 --> C
  C --> G3 --> D
  C --> G3 --> E
  E --> G4 --> F
```

---

## 🗂️ Example directory layout

> This README is the “contract + walkthrough.” The example expects a standard gate folder shape like:

```text
📦 mcp/gates/examples/06-privacy/
├─ 📄 README.md
├─ 🧠 policy/                       # OPA/Rego policies
│  ├─ 🔒 privacy.rego
│  ├─ 🧭 geo_precision.rego
│  ├─ 🏷️  sovereignty.rego
│  └─ 🧽 pii_findings.rego
├─ 🧪 inputs/                       # test inputs (JSON)
│  ├─ ✅ public_request.json
│  ├─ ⚠️ sensitive_request_generalized.json
│  ├─ ❌ sensitive_request_exact_location.json
│  └─ ❌ sovereign_request_no_approval.json
└─ 📤 expected/                     # expected decisions (optional)
   ├─ public_request.decision.json
   └─ ...
```

---

## 🔧 Prerequisites

- 🧩 **Conftest** (recommended) to run policies as tests in CI  
- 🧠 **OPA** (optional) if you want to run policies as a service  
- 🛠️ A pipeline step that produces **privacy findings** (PII scanner / metadata classifier / sensitivity tags)

> [!TIP]
> Treat privacy as a *composed gate*: metadata validation + sensitivity rules + role checks + geo-obfuscation + auditing.

---

## 🚀 Quickstart (CI-style)

Run all privacy gate tests:

```bash
# from repo root (example)
conftest test mcp/gates/examples/06-privacy/inputs \
  --policy mcp/gates/examples/06-privacy/policy
```

If you want pretty JSON output for a single request:

```bash
conftest test mcp/gates/examples/06-privacy/inputs/sensitive_request_exact_location.json \
  --policy mcp/gates/examples/06-privacy/policy \
  --output json | jq
```

---

## 🔒 The KFM privacy rules this gate encodes

### Rule 1 — Everything must be classified 🏷️
If a dataset/request **has no sensitivity label**, the gate denies.

**Why:** Unlabeled data is ungovernable data.

---

### Rule 2 — “No output may be less restricted than its inputs” 🧱➡️🔐
If you derived a layer/story/AI answer from restricted input data, you **cannot publish it publicly** without applying at least the same restrictions (or tighter).

**Practical implication:** A public Story Node cannot embed a confidential layer screenshot, coordinates, or quotes without permission + transformations.

---

### Rule 3 — Precision controls for sensitive geospatial data 🧭
For sensitive layers, the gate enforces one or more:
- **Round coordinates** (e.g., ~10 km accuracy)  
- **Generalize geometry** (hex bins / coarse polygons instead of points)
- **Limit zoom level** (show only at low resolution)
- **Block export** (no raw GeoJSON/CSV download for public)

> [!WARNING]
> “Exact point + sensitive label” is a common failure mode. Your policies must detect and stop it.

---

### Rule 4 — PII must be removed, aggregated, or refused 🧽
If PII is detected (or even suspected), the gate should:
- ✅ allow only if **redaction obligations** are applied  
- ❌ deny if it can’t guarantee safe transformation

Examples of PII / sensitive personal data:
- names + addresses
- phone numbers / emails
- exact home coordinates
- any “living individual” record fields

---

### Rule 5 — Sovereignty & cultural protocol enforcement 🪶
Some content must respect **Authority to Control**:
- community-defined access rules
- TK labels / cultural protocols
- “approved by” metadata
- “community only” or “restricted” roles

This gate treats “sovereign” classification as **stronger than ordinary sensitivity**.

---

### Rule 6 — Auditability is not optional 🧾
If you deny or apply transformations, record the decision with:
- event type (`privacy.denied`, `privacy.obfuscated`, etc.)
- correlation ID
- minimal safe context (no raw PII in logs)

---

## 🧪 Example inputs (copy/paste ready)

### ✅ Public request
```json
{
  "subject": { "id": "anon", "roles": ["public"] },
  "resource": {
    "id": "kfm.layer.public.counties",
    "sensitivity": "public"
  },
  "request": {
    "action": "read",
    "format": "tile",
    "geo_precision_m": 1000
  },
  "findings": { "pii": { "detected": false } }
}
```

Expected result: `allow: true`

---

### ⚠️ Sensitive request (generalized allowed)
```json
{
  "subject": { "id": "u123", "roles": ["researcher"] },
  "resource": {
    "id": "kfm.layer.sensitive.endangered_species",
    "sensitivity": "sensitive",
    "handling": { "min_geo_precision_m": 10000 }
  },
  "request": {
    "action": "read",
    "format": "tile",
    "geo_precision_m": 500
  },
  "findings": { "pii": { "detected": false } }
}
```

Expected result: `allow: true` **with obligations**:
- `geo_generalize` to ≥ 10 km
- `ui_warning`
- `audit_log`

---

### ❌ Sensitive request (exact location denied)
```json
{
  "subject": { "id": "anon", "roles": ["public"] },
  "resource": {
    "id": "kfm.layer.sensitive.archaeology_sites",
    "sensitivity": "sensitive",
    "handling": { "min_geo_precision_m": 10000 }
  },
  "request": {
    "action": "export",
    "format": "geojson",
    "geo_precision_m": 1
  },
  "findings": { "pii": { "detected": false } }
}
```

Expected result: `allow: false`  
Reason example: `export_blocked_for_sensitive_location_data`

---

### ❌ Sovereign request (approval missing)
```json
{
  "subject": { "id": "u777", "roles": ["researcher"] },
  "resource": {
    "id": "kfm.layer.sovereign.sacred_sites",
    "sensitivity": "confidential",
    "sovereignty": {
      "authority": "tribal_nation_x",
      "requires_approval": true,
      "approved_by": null
    }
  },
  "request": { "action": "read", "format": "geojson", "geo_precision_m": 10000 },
  "findings": { "pii": { "detected": false } }
}
```

Expected result: `allow: false`  
Reason example: `sovereignty_approval_required`

---

## 🧠 Rego policy sketch (privacy.rego)

> This is a **minimal** pattern. Production policies should be split across files and tested heavily.

<details>
<summary>📄 Click to expand sample Rego</summary>

```rego
package mcp.gates.privacy

default decision := {
  "allow": false,
  "reason": "deny_by_default",
  "obligations": [{"type":"audit_log","event":"privacy.denied"}]
}

# ✅ allow fully if public
decision := {"allow": true, "reason":"public_ok", "obligations":[{"type":"audit_log","event":"privacy.allowed"}]} {
  input.resource.sensitivity == "public"
  not input.findings.pii.detected
}

# ❌ deny if PII detected and we can't guarantee redaction (simple stance for example)
decision := {"allow": false, "reason":"pii_detected", "obligations":[{"type":"audit_log","event":"privacy.denied.pii"}]} {
  input.findings.pii.detected
}

# ✅ allow sensitive, but enforce generalization + warnings
decision := {
  "allow": true,
  "reason": "sensitive_allowed_with_obfuscation",
  "obligations": [
    {"type":"geo_generalize","min_precision_m": min_precision_m},
    {"type":"ui_warning","severity":"warning","message":"Sensitive layer: location precision reduced."},
    {"type":"audit_log","event":"privacy.obfuscated"}
  ]
} {
  input.resource.sensitivity == "sensitive"
  input.subject.roles[_] == "researcher"

  min_precision_m := input.resource.handling.min_geo_precision_m
  input.request.geo_precision_m < min_precision_m
}

# ❌ block exporting sensitive location datasets to public
decision := {"allow": false, "reason":"export_blocked_sensitive", "obligations":[{"type":"audit_log","event":"privacy.denied.export"}]} {
  input.resource.sensitivity == "sensitive"
  input.request.action == "export"
  input.subject.roles[_] == "public"
}

# ❌ sovereign data requires approval metadata
decision := {"allow": false, "reason":"sovereignty_approval_required", "obligations":[{"type":"audit_log","event":"privacy.denied.sovereignty"}]} {
  input.resource.sovereignty.requires_approval == true
  input.resource.sovereignty.approved_by == null
}
```

</details>

---

## 🧩 UI integration expectations (what the gate enables)

KFM’s UI is designed to surface provenance and context (“the map behind the map”). The privacy gate feeds the UI with **obligations** such as:

- `ui_warning` → show a modal / banner (acknowledgement required)
- `hide_by_default` → don’t auto-enable the layer
- `deny_export` → disable download buttons
- `redact_fields` → hide columns in popups
- `geo_generalize` → render hexagons or coarse polygons instead of points

> [!NOTE]
> The gate should not *only* deny—it should also “shape safe experiences” via obligations.

---

## 🤖 Focus Mode integration (AI must respect privacy)

Focus Mode is designed to:
- always provide **citations** (or refuse)
- run a **governance check** before returning answers
- surface governance flags (including privacy notices) in an audit panel

In practice, the privacy gate should be called for:
- AI answers that include **coordinates**, **addresses**, or **personal narratives**
- AI summarization of restricted documents
- AI-generated Story Nodes that embed restricted layers

**If an answer requires restricted info to be correct**, the AI should refuse (or safely generalize) rather than “helpfully” leaking it.

---

## 🧠 Advanced privacy patterns (extensions)

This example is intentionally simple, but KFM’s privacy posture supports richer approaches:

### 🧬 Group anonymization (k-anonymity / l-diversity / t-closeness)
Useful when publishing row-level tabular extracts or microdata:
- **k-anonymity** for identity protection
- **l-diversity** to prevent homogeneity attacks
- **t-closeness** to control sensitive attribute distribution shift

### 🧾 Query auditing & inference control
Track queries and deny those that enable inference:
- online auditing (during query)
- offline auditing (after the fact)

### 🎛 Differential privacy for aggregates
For public dashboards / stats, add noise with privacy budgets.

> [!TIP]
> For geospatial privacy: combine **aggregation** + **precision limits** + **audit logs**. It’s the “belt + suspenders” strategy.

---

## ✅ Definition of done (privacy gate)

- [ ] Deny-by-default behavior is proven with tests
- [ ] Unclassified data is denied
- [ ] Sensitive layers cannot be exported publicly
- [ ] Sensitive location precision is generalized (≥ configured threshold)
- [ ] Sovereign datasets require approval metadata
- [ ] PII findings cause deny or mandatory redaction obligations
- [ ] All decisions emit privacy-safe audit events

---

## 📚 Project files this example is grounded in

These documents informed the rules and UI/AI expectations in this gate:

- 📘 **Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf**
- 🧾 **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf**
- 🖥️ **Kansas Frontier Matrix – Comprehensive UI System Overview.pdf**
- 🤖 **Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf**
- 📥 **📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf**
- 🌟 **🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf**
- 🧠 **Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf**
- 🧩 **Additional Project Ideas.pdf**
- 🧠 **AI Concepts & more.pdf** *(PDF portfolio — open in Acrobat for embedded docs)*
- 🗃️ **Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf** *(PDF portfolio)*
- 🗺️ **Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf** *(PDF portfolio)*
- 🧰 **Various programming langurages & resources 1.pdf** *(PDF portfolio)*

---

## 🔭 Next steps (recommended)

1. 🧪 Add more test cases for:
   - export attempts by privileged roles
   - “allow with redaction” behavior
   - offline pack generation restrictions
2. 🔐 Define a small standard vocabulary for `obligations.type`
3. 🧾 Wire `audit_log` obligations into the telemetry ledger (append-only NDJSON)
4. 🧭 Add explicit geo-privacy strategies (grid snap vs hex bin vs rounding) per dataset

---

📌 *If you’re building KFM-like systems, privacy is not a feature—it's a gate.* 🔒


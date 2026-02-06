# 🛡️ KFM API Policy Pack (OPA) — `api/policies/`

<p align="center">
  <strong>Policy-as-Code</strong> 🧩 • <strong>Fail Closed</strong> 🔒 • <strong>Least Privilege</strong> 🧠 • <strong>Evidence-First (“No Source, No Answer”)</strong> 📎 • <strong>FAIR + CARE</strong> 🌾
</p>

<!-- ✅ Badge block (replace <ORG>/<REPO> + workflow filenames as needed) -->
<p align="center">
  <a href="https://github.com/<ORG>/<REPO>/actions">
    <img alt="CI" src="https://img.shields.io/github/actions/workflow/status/<ORG>/<REPO>/ci.yml?branch=main&label=CI&logo=githubactions">
  </a>
  <a href="https://github.com/<ORG>/<REPO>/actions">
    <img alt="Policy Gate" src="https://img.shields.io/github/actions/workflow/status/<ORG>/<REPO>/policy-gate.yml?branch=main&label=Policy%20Gate&logo=opa">
  </a>
  <a href="https://github.com/<ORG>/<REPO>/actions">
    <img alt="CodeQL" src="https://img.shields.io/github/actions/workflow/status/<ORG>/<REPO>/codeql.yml?branch=main&label=CodeQL&logo=github">
  </a>
  <a href="https://github.com/<ORG>/<REPO>/blob/main/LICENSE">
    <img alt="License" src="https://img.shields.io/github/license/<ORG>/<REPO>?label=license">
  </a>
  <a href="https://github.com/<ORG>/<REPO>/releases">
    <img alt="Release" src="https://img.shields.io/github/v/release/<ORG>/<REPO>?include_prereleases&label=release">
  </a>
  <img alt="OPA" src="https://img.shields.io/badge/OPA-policy--engine-blue">
  <img alt="Rego" src="https://img.shields.io/badge/Rego-policy--language-informational">
  <img alt="Fail Closed" src="https://img.shields.io/badge/default-fail--closed-critical">
</p>

---

## 🚦 TL;DR

- **Every request** (REST / GraphQL / tiles / AI) gets a **policy decision** 🧠
- The system **fails closed**: missing license, sensitivity, provenance, unknown role → **deny** 🔒
- Policies run in **CI** (block non-compliant changes) **and** at **runtime** (authorize + sanitize) ✅
- AI is **evidence-first**: *“No Source, No Answer”* 📎

> **Design mantra:** *No UI → DB shortcuts. Everything flows through the governed API “truth path.”* 🧱

---

## 🧭 Contents

- [🧠 What this policy pack is](#-what-this-policy-pack-is)
- [🧱 Where policies run](#-where-policies-run)
- [📁 Folder layout](#-folder-layout)
- [📦 Entrypoints](#-entrypoints)
- [🧾 Input contract](#-input-contract)
- [🎛️ Decision contract](#️-decision-contract)
- [🧽 Sanitization directives](#-sanitization-directives)
- [✅ CI policy gate](#-ci-policy-gate)
- [⚙️ Runtime integration patterns](#️-runtime-integration-patterns)
- [🧪 Testing & debugging](#-testing--debugging)
- [🧩 Adding a new policy](#-adding-a-new-policy)
- [📎 Examples](#-examples)
- [🧾 Auditing & provenance](#-auditing--provenance)
- [❓ FAQ](#-faq)
- [📚 Project references](#-project-references)

---

## 🧠 What this policy pack is

Welcome to the **policy “brain”** for the Kansas Frontier Matrix (KFM) API layer. This directory defines **how requests are allowed, denied, or sanitized**—consistently—across:

- 🌐 REST endpoints
- 🧬 GraphQL queries
- 🗺️ Tile services (vector/raster/PMTiles)
- 🤖 AI endpoints (“Focus Mode”)

KFM’s broader architecture is intentionally **governed and evidence-first**: data and answers must remain **traceable**, **auditable**, and **policy-compliant** end-to-end (the “map behind the map”). 📎🗺️

> 🔒 **Fail-Closed Rule:** If policy cannot prove a request is safe + compliant, the answer is **no**.

---

## 🧱 Where policies run

```mermaid
flowchart LR
  A[👤 Client: UI / External App] --> B[🌐 KFM API (REST/GraphQL/Tiles/AI)]
  B --> C{🛡️ OPA Decision}
  C -->|allow ✅| D[📦 Data / Tiles / AI Answer]
  C -->|deny ⛔| E[401/403 or safe refusal]
  C -->|sanitize 🧽| F[✅ Filtered / rounded / aggregated output]

  subgraph CI[🤖 CI Policy Gate]
    G[PR change] --> H[🧪 Conftest + Rego tests]
    H -->|pass ✅| I[merge]
    H -->|fail ⛔| J[block + report violations]
  end
```

### 🧱 The “Truth Path” (why this matters)
KFM is designed so **nothing bypasses governance**. Policies are the guardrails that keep the system honest—especially for:
- licensing / attribution
- sensitivity + privacy protections
- provenance requirements
- AI safety + evidence rules
- culturally protected knowledge (CARE) 🌾

---

## 📁 Folder layout

> Keep it boring. Predictable structure = testable governance 😄

```text
📦 api/
  └── 🛡️ policies/
      ├── README.md
      ├── 📜 rego/
      │   ├── security.rego            # RBAC/ABAC, endpoint & method protection
      │   ├── data_policies.rego       # license/sensitivity/provenance gating
      │   ├── ai_policies.rego         # citations, AI safety, sensitive output checks
      │   ├── compliance.rego          # governance council / publish rules
      │   └── lib/
      │       ├── strings.rego
      │       ├── sanitize.rego
      │       ├── time.rego
      │       └── schema.rego          # (recommended) input/decision validation helpers
      ├── 🧪 tests/
      │   ├── security_test.rego
      │   ├── data_policies_test.rego
      │   ├── ai_policies_test.rego
      │   └── compliance_test.rego
      ├── 🗂️ data/
      │   ├── roles.json               # role → capabilities map (optional)
      │   ├── sensitivities.json       # standard taxonomy + constraints (optional)
      │   ├── licenses.json            # allowed license identifiers (optional)
      │   └── denylist.json            # disallowed prompt patterns, etc. (optional)
      ├── 🧬 schemas/                  # (recommended) JSON schemas for input/decision
      │   ├── input.schema.json
      │   └── decision.schema.json
      └── 📦 bundle/
          └── (optional OPA bundle outputs)
```

<details>
<summary>✨ Why add <code>schemas/</code>?</summary>

Schema files let you:
- validate policy input shape early (fail fast, clearer errors)
- keep the API ↔ policy boundary stable as the system grows
- generate documentation for clients that need to craft input payloads

</details>

---

## 📦 Entrypoints

We keep **stable, boring** entrypoints so API integration stays simple.

Recommended packages + entrypoint rules:

- `data.kfm.security.decision` 🔐
- `data.kfm.data.decision` 🧾
- `data.kfm.ai.decision` 🤖
- `data.kfm.compliance.decision` 🌾

> ✅ **Rule:** once published, avoid renaming packages/entrypoints unless you version them (`v1`, `v2`, …).

---

## 🧾 Input contract

OPA input should be **explicit, minimal, and complete**. Treat it like an API request DTO.

✅ Suggested input shape (example):

```json
{
  "request": {
    "id": "req_01HX…",
    "method": "GET",
    "path": "/api/v1/datasets/ks-1857",
    "query": {"year": "1857"},
    "headers": {"x-request-id": "…"},
    "ip": "203.0.113.42"
  },
  "user": {
    "id": "user_123",
    "roles": ["public_viewer"],
    "groups": ["public"],
    "org": "kfm"
  },
  "resource": {
    "type": "dataset",
    "id": "ks-1857",
    "license": "CC-BY-4.0",
    "sensitivity": "public",
    "provenance": {"prov_present": true},
    "tags": ["history", "census"]
  },
  "context": {
    "environment": "prod",
    "endpoint_kind": "rest",
    "time": "2026-02-06T00:00:00Z"
  },
  "ai": {
    "question": null,
    "answer": null,
    "citations": []
  }
}
```

### 🔎 Input hygiene rules
- **Never** rely on hidden state (if the policy needs it, pass it)
- Prefer **typed enums** for sensitivity, endpoint kind, roles
- Pass only what you’re willing to log (OPA inputs often end up in audits)

---

## 🎛️ Decision contract

Every entrypoint returns a **single decision object** with a stable shape. This is the “contract” between the API and policies.

✅ Recommended decision output:

```json
{
  "allow": false,
  "reasons": [
    { "code": "default_deny", "detail": "Missing or ambiguous governance requirements." }
  ],
  "sanitize": [],
  "obligations": [
    { "op": "audit_log", "level": "info" },
    { "op": "attach_policy_version" }
  ],
  "meta": {
    "policy_package": "kfm.data",
    "policy_version": "git:COMMIT_SHA_OR_BUNDLE_HASH",
    "decision_id": "dec_01HX…"
  }
}
```

### ✅ Meaning of each field
| Field | Purpose |
|------|---------|
| `allow` | hard allow/deny gate |
| `reasons[]` | machine-readable reason codes (✅ for client UX + auditing) |
| `sanitize[]` | transformations the API **must apply** before returning data |
| `obligations[]` | required side effects (audit, provenance stamp, risk logging, etc.) |
| `meta` | policy provenance (bundle hash / git SHA) |

> 🧠 **Key idea:** `allow=false` can still return **safe refusal guidance**; `allow=true` can still require sanitization.

---

## 🧽 Sanitization directives

Sanitization is how we keep legitimate use-cases working **without** over-sharing.

Common directives:
- 🗺️ `round_coordinates` (reduce precision)
- 🧱 `aggregate_to_admin_level` (point → county)
- 🧍 `suppress_fields` (remove identifiers)
- 🧪 `apply_thresholding` (suppress low-count groups)
- 🎭 `mask_geometry` (strip exact shapes; provide bounding boxes)
- ⛔ `redact_text_spans` (remove restricted strings in narratives)

Example sanitize payload:

```json
{
  "sanitize": [
    { "op": "round_coordinates", "meters": 5000 },
    { "op": "suppress_fields", "fields": ["owner_name", "exact_geometry"] },
    { "op": "aggregate_to_admin_level", "level": "county" }
  ]
}
```

> 🌾 This is especially important for **sensitive locations** (e.g., archaeological sites, culturally protected places), where public views should be generalized.

---

## ✅ CI policy gate

Policy checks run in CI to prevent non-compliant changes from shipping.

### What CI should block ⛔
- dataset added/modified without a license
- sensitivity not declared
- provenance missing (no PROV record / lineage metadata)
- “disallowed intent” patterns introduced into AI prompts/templates
- governance-required approvals missing (publish rules)

### Local parity (recommended)
Run the same checks locally before PRs:

```bash
# ✅ Rego unit tests
opa test api/policies -v

# ✅ Repo-wide Conftest checks (CI parity)
conftest test . -p api/policies/rego
```

---

## ⚙️ Runtime integration patterns

KFM can enforce policies at runtime via:

### 1) 🧱 OPA sidecar (common)
- API sends input to OPA over HTTP
- OPA returns decision JSON
- API enforces allow/deny/sanitize + obligations

Example query:

```bash
curl -s \
  -X POST "http://opa:8181/v1/data/kfm/security/decision" \
  -H "Content-Type: application/json" \
  -d @input.json | jq
```

### 2) 🧩 Embedded evaluation (WASM / library)
- Evaluate Rego in-process (fast, fewer network hops)
- Still version + audit decisions the same way

> ✅ Either way, **policies in this directory remain the source-of-truth**.

---

## 🧪 Testing & debugging

### ✅ Evaluate decisions locally
```bash
opa eval \
  -d api/policies/rego \
  -d api/policies/data \
  -i input.json \
  "data.kfm.data.decision"
```

### 🧯 Debug tips
- Add **reason codes** early (debugging “deny with no explanation” is misery)
- Prefer `tests/` coverage over “it works on my machine”
- Keep reusable helpers in `rego/lib/*` to avoid logic spaghetti 🍝

<details>
<summary>🧠 Suggested “reason code” naming</summary>

Use consistent, grep-friendly codes:

- `default_deny`
- `missing_license`
- `missing_sensitivity`
- `missing_provenance`
- `role_not_authorized`
- `culturally_protected_requires_owner_group`
- `ai_missing_citations`
- `ai_restricted_dataset_reference`
- `privacy_low_count_suppression_required`

</details>

---

## 🧩 Adding a new policy

### ✅ Checklist
- [ ] Pick the domain: **security / data / AI / compliance**
- [ ] Add rule(s) under `rego/` with **default deny**
- [ ] Add tests under `tests/` (must include deny + allow cases)
- [ ] If needed, add standard data under `data/`
- [ ] Update this README if you introduce new `sanitize` ops or obligations
- [ ] Document the **risk** being mitigated + **examples** of pass/fail

### ✍️ Style conventions
- Keep packages stable: `package kfm.*`
- Prefer readable entrypoints:
  - `kfm.security.decision`
  - `kfm.data.decision`
  - `kfm.ai.decision`
  - `kfm.compliance.decision`
- Avoid deep nesting; extract to `rego/lib/*`
- Reasons should be **machine-readable** objects, not just strings

---

## 📎 Examples

### 1) 🤖 Evidence-first AI: require citations

Enforce: answers must include at least one citation marker (example: `[12]`).

```rego
package kfm.ai

default decision = {
  "allow": false,
  "reasons": [{"code": "ai_missing_citations"}],
  "sanitize": [],
  "obligations": [{"op": "audit_log", "level": "info"}],
  "meta": {"policy_package": "kfm.ai"}
}

decision = {
  "allow": true,
  "reasons": [],
  "sanitize": [],
  "obligations": [{"op": "audit_log", "level": "info"}],
  "meta": {"policy_package": "kfm.ai"}
} {
  re_match("\\[\\d+\\]", input.ai.answer)
}
```

💡 Upgrade idea: if missing citations, return a **safe refusal** obligation:

```json
{
  "obligations": [
    { "op": "safe_refusal", "template": "No Source, No Answer. Please provide sources or use approved datasets." }
  ]
}
```

---

### 2) 🗺️ Sensitive location handling (mask / round / aggregate)

```rego
package kfm.data

default decision = {
  "allow": false,
  "reasons": [{"code": "default_deny"}],
  "sanitize": [],
  "obligations": [{"op": "audit_log", "level": "info"}],
  "meta": {"policy_package": "kfm.data"}
}

# ✅ Public is readable
decision = {
  "allow": true,
  "reasons": [],
  "sanitize": [],
  "obligations": [{"op": "audit_log", "level": "info"}],
  "meta": {"policy_package": "kfm.data"}
} {
  input.resource.sensitivity == "public"
}

# ✅ Restricted allowed for admins
decision = {
  "allow": true,
  "reasons": [],
  "sanitize": [],
  "obligations": [{"op": "audit_log", "level": "info"}],
  "meta": {"policy_package": "kfm.data"}
} {
  input.resource.sensitivity == "restricted"
  "admin" in input.user.roles
}

# 🧽 Restricted sanitized for non-admins (optional pattern)
decision = {
  "allow": true,
  "reasons": [{"code": "sanitized_restricted_dataset"}],
  "sanitize": [
    {"op": "round_coordinates", "meters": 5000},
    {"op": "suppress_fields", "fields": ["exact_geometry"]}
  ],
  "obligations": [{"op": "audit_log", "level": "warn"}],
  "meta": {"policy_package": "kfm.data"}
} {
  input.resource.sensitivity == "restricted"
  not ("admin" in input.user.roles)
}
```

---

### 3) 🔐 Endpoint protection (pipeline triggers)

```rego
package kfm.security

default decision = {
  "allow": false,
  "reasons": [{"code": "role_not_authorized"}],
  "sanitize": [],
  "obligations": [{"op": "audit_log", "level": "warn"}],
  "meta": {"policy_package": "kfm.security"}
}

decision = {
  "allow": true,
  "reasons": [],
  "sanitize": [],
  "obligations": [{"op": "audit_log", "level": "info"}],
  "meta": {"policy_package": "kfm.security"}
} {
  input.request.path == "/api/v1/ingest/runPipeline"
  input.request.method == "POST"
  "admin" in input.user.roles
}
```

---

### 4) 🧾 Publish gating: license + sensitivity + provenance required

> **Fail closed**: if metadata isn’t complete, it’s not publishable.

```rego
package kfm.compliance

default decision = {
  "allow": false,
  "reasons": [{"code": "default_deny"}],
  "sanitize": [],
  "obligations": [{"op": "audit_log", "level": "warn"}],
  "meta": {"policy_package": "kfm.compliance"}
}

decision = {
  "allow": true,
  "reasons": [],
  "sanitize": [],
  "obligations": [{"op": "audit_log", "level": "info"}],
  "meta": {"policy_package": "kfm.compliance"}
} {
  input.resource.license != ""
  input.resource.sensitivity != ""
  input.resource.provenance.prov_present == true
}
```

---

## 🧾 Auditing & provenance

Policies must be **auditable** and **replayable**.

Recommended audit fields (API executes; policies require via obligations):
- `request_id`
- `user_id` (or pseudonymous ID if required)
- `decision.allow`
- `decision.reasons[]`
- `decision.sanitize[]`
- `policy_version` (commit SHA or bundle hash)
- `resource_id` (dataset/story/tile layer id)
- `timestamp`

### 🤖 AI provenance (Focus Mode)
AI outputs should be stored as first-class artifacts:
- question + answer
- sources/citations used
- model version
- policy decision (including sanitize + obligations)

> This enables “show your work” accountability—especially when decisions are challenged later.

---

## ❓ FAQ

### “Should policies deny, or sanitize?”
Both are valid:
- **deny** when risk is unacceptable or requirements are missing (fail closed)
- **sanitize** when the use-case is legitimate but precision is harmful (e.g., sensitive sites)

### “Do we enforce policies only at runtime?”
No—**CI policy gates** prevent non-compliant assets and metadata from ever shipping.

### “Where does token validation happen?”
Typically **outside** OPA:
- API middleware validates token/session
- claims are passed into OPA (`user.roles`, `user.groups`, `user.org`, etc.)
- OPA decides allow/deny + obligations; API enforces.

### “How does FAIR + CARE show up in code?”
- FAIR can be enforced as **required metadata gates** (license, provenance, catalog fields)
- CARE shows up as **collective protection rules** (culturally protected data handling, access by owner group, precision reduction, consent-driven constraints)

---

## 📚 Project references

> These are the primary design sources informing the governance + policy-as-code posture of KFM.

- **Kansas Frontier Matrix — Comprehensive System Documentation**  [oai_citation:0‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
- **KFM — Comprehensive Technical Blueprint** (governance, CI gates, runtime enforcement patterns)  [oai_citation:1‡Artificial Intelligence & Machine Learning in Health Care & Medical Sciences.pdf](sediment://file_0000000036fc71fda445161776f735db)  
- **Indigenous Statistics (2nd ed., 2025)** (Indigenous Data Sovereignty + CARE framing)  [oai_citation:2‡Indigenous Statistics.pdf](sediment://file_0000000033ec72308e1f791a79f61bfe)  
- **Node.js / Web service foundations** (supporting API/CI ergonomics context)  [oai_citation:3‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)  
- **Documentation + layout polish references** (Markdown + web presentation best practices)  [oai_citation:4‡professional-web-design-techniques-and-templates.pdf](sediment://file_000000000acc71f8b2e5128c030179fc)  [oai_citation:5‡learn-to-code-html-and-css-develop-and-style-websites.pdf](sediment://file_00000000ed6471fdb0ecead71e051444)  
- **Visuals / diagram asset considerations** (when embedding images in docs)  [oai_citation:6‡Various Programming Concepts.pdf](sediment://file_00000000e86c71fd9eceb7eec4bba22e)  

---

### ✅ House rule (keep this README honest) 🌱
If you change:
- entrypoints,
- reason codes,
- sanitize ops,
- obligations,
- or CI gate behavior…

…update this README in the same PR. No surprises.
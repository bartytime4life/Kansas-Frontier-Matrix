# 🛡️ KFM API Policy Pack (OPA) — `api/policies/`

**Policy-as-Code** 🧩 • **Fail Closed** 🔒 • **Least Privilege** 🧠 • **Evidence-First (“No Source, No Answer”)** 📎 • **FAIR + CARE** 🌾

Welcome to the policy “brain” for the Kansas Frontier Matrix (KFM) API layer.  
This directory defines **how requests are allowed, denied, or sanitized**—consistently—across REST, GraphQL, tile services, and AI endpoints.

---

## 📌 Why this exists

KFM is designed as an evidence-first geospatial knowledge system where:

- **All access flows through the API** (no UI → DB shortcuts) 🧱
- **Every request is governed** by *explicit*, versioned policy checks ✅
- The platform **fails closed**: if required metadata or governance conditions aren’t satisfied, the system blocks the operation 🔒
- AI outputs are treated as first-class artifacts and must stay **traceable + auditable** 🧾

This policy pack helps enforce those guarantees at:
- ✅ **CI time** (prevent non-compliant changes from merging)
- ✅ **Runtime** (authorize + sanitize every request and response)

---

## 🧭 Contents

- [🧠 Policy philosophy](#-policy-philosophy)
- [🧱 Where policies run](#-where-policies-run)
- [📁 Suggested folder layout](#-suggested-folder-layout)
- [🎛️ Decision contract](#️-decision-contract)
- [🗂️ Policy domains](#️-policy-domains)
- [🧪 Testing locally](#-testing-locally)
- [🧩 Adding a new policy](#-adding-a-new-policy)
- [📎 Examples](#-examples)
- [🧾 Auditing & provenance](#-auditing--provenance)
- [❓ FAQ](#-faq)

---

## 🧠 Policy philosophy

### 1) 🔒 Fail closed by default
If anything is missing or ambiguous (license absent, sensitivity unset, provenance missing, unknown role), **deny**.

### 2) 🧠 Least privilege (RBAC + ABAC)
Access is determined by:
- **User role(s)** (RBAC)
- **Resource sensitivity + classification tags** (ABAC)
- **Context** (endpoint type, query shape, org/group membership, environment)

### 3) 🌾 FAIR + CARE governance is “real”
We aim for open exploration **without** exposing sensitive locations, private records, or culturally protected data.

### 4) 📎 Evidence-first AI
AI responses must be grounded and verifiable:
- “No Source, No Answer” means the system should **refuse** or **de-escalate** rather than hallucinate.
- Policies should be able to enforce **citations**, **topic limits**, and **sensitive-data protections** for AI.

---

## 🧱 Where policies run

```mermaid
flowchart LR
  A[👤 Client: UI / External App] --> B[🌐 KFM API (REST/GraphQL/Tiles/AI)]
  B --> C{🛡️ Policy Decision}
  C -->|allow ✅| D[📦 Data / Tiles / AI Answer]
  C -->|deny ⛔| E[403 / 401 / safe refusal]
  C -->|sanitize 🧽| F[✅ Return filtered/rounded/aggregated output]

  subgraph CI[🤖 CI Policy Gate]
    G[PR change] --> H[🧪 Conftest / Rego checks]
    H -->|pass ✅| I[merge]
    H -->|fail ⛔| J[block + report violations]
  end
```

---

## 📁 Suggested folder layout

> Your repo may vary. This layout keeps things predictable and testable.

```text
📦 api/
  └── 🛡️ policies/
      ├── README.md
      ├── 📜 rego/
      │   ├── security.rego          # RBAC/ABAC allow/deny + endpoint rules
      │   ├── data_policies.rego      # dataset license/sensitivity/provenance gating
      │   ├── ai_policies.rego        # citation + AI safety + sensitive output checks
      │   ├── compliance.rego         # governance checks (e.g., publish rules)
      │   └── lib/
      │       ├── strings.rego
      │       ├── sanitize.rego
      │       └── time.rego
      ├── 🧪 tests/
      │   ├── security_test.rego
      │   ├── data_policies_test.rego
      │   └── ai_policies_test.rego
      ├── 🗂️ data/
      │   ├── roles.json              # optional: role definitions / capability maps
      │   ├── sensitivities.json      # optional: standard sensitivity taxonomy
      │   └── denylist.json           # optional: banned prompt patterns, etc.
      └── 📦 bundle/
          └── (optional OPA bundle outputs)
```

---

## 🎛️ Decision contract

To keep the API integration simple, every policy “entrypoint” should return a **single decision object** with a stable shape.

✅ Recommended output:

```json
{
  "allow": false,
  "reasons": ["default deny"],
  "sanitize": {
    "mask_coordinates": true,
    "rounding_meters": 5000,
    "suppress_fields": ["owner_name", "exact_geometry"]
  },
  "obligations": {
    "audit": true,
    "log_level": "info",
    "policy_version_required": true
  }
}
```

### Key idea 🧠
- `allow=false` can still return `sanitize` instructions if you prefer **safe partial disclosure**
- `obligations` tell the API what it **must** do if it proceeds (audit logging, provenance stamping, etc.)

---

## 🗂️ Policy domains

### 🔐 1) `security.rego` — RBAC + endpoint protection
Typical rules include:
- Only Admin can hit ingestion/pipeline-trigger endpoints
- Contributor can draft/submit, but not publish
- Public Viewer can read **only** public-approved datasets/stories

### 🧾 2) `data_policies.rego` — dataset governance (license, sensitivity, provenance)
Typical rules include:
- A dataset **must** have a license before it’s publishable
- A dataset **must** declare a sensitivity classification
- A dataset **must** have provenance (PROV) before it can enter “public catalog” flows

### 🌾 3) `compliance.rego` — governance council rules
This is where “human governance” becomes enforceable guardrails, e.g.:
- withdrawn datasets are not accessible
- culturally protected datasets are access-controlled by owner group
- release processes require approvals (modeled as metadata assertions)

### 🤖 4) `ai_policies.rego` — evidence + safety for Focus Mode
Typical rules include:
- require citations in answers (format is project-specific)
- block answers that reference restricted datasets for unauthorized users
- prevent disclosure of private information about living individuals
- refuse disallowed intents (e.g., exploitative requests)

---

## 🧪 Testing locally

> The goal: contributors can catch governance failures **before** opening a PR.

### ✅ OPA unit tests
Run Rego tests (example):
```bash
opa test api/policies -v
```

### ✅ Conftest checks (CI parity)
Run policy checks against repo content (example):
```bash
conftest test . -p api/policies/rego
```

> If your CI checks for missing license fields, missing sensitivity tags, or missing provenance records, keep local runs aligned with CI.

---

## 🧩 Adding a new policy

### ✅ Checklist
- [ ] Decide the **policy domain** (security / data / AI / compliance)
- [ ] Add rule(s) under `rego/` with **default deny**
- [ ] Add test coverage under `tests/`
- [ ] If needed, add policy data under `data/`
- [ ] Update [Decision contract](#️-decision-contract) usage if introducing new obligations/sanitize outputs
- [ ] Document the **intent** (what risk is mitigated) + **examples** (what should pass/fail)

### ✍️ Style conventions
- Keep packages stable (avoid renaming `package kfm.*` once published)
- Prefer clear “entrypoint” rules:
  - `kfm.security.decision`
  - `kfm.data.decision`
  - `kfm.ai.decision`
- Avoid deeply nested logic—extract to `rego/lib/*`
- Return **structured** reasons (machine readable), not just strings

---

## 📎 Examples

### 1) 📎 AI citations requirement (evidence-first)

> Enforce: answers must include at least one citation marker (example pattern: `[12]`)

```rego
package kfm.ai

default allow_answer = false

allow_answer {
  re_match("\\[\\d+\\]", input.answer)
}
```

✅ Recommended upgrade: return a decision object:

```rego
package kfm.ai

default decision = {
  "allow": false,
  "reasons": ["missing_citations"],
  "sanitize": {},
  "obligations": {"audit": true}
}

decision := {
  "allow": true,
  "reasons": [],
  "sanitize": {},
  "obligations": {"audit": true}
} {
  re_match("\\[\\d+\\]", input.answer)
}
```

---

### 2) 🗺️ Sensitive location handling (mask / round / aggregate)

Common patterns:
- round coordinates to reduce precision
- return county-level aggregates instead of exact points
- suppress fields that could deanonymize

```rego
package kfm.data

default decision = {"allow": false, "reasons": ["default_deny"], "sanitize": {}, "obligations": {"audit": true}}

decision := out {
  # allow reading public datasets
  input.resource.sensitivity == "public"
  out := {"allow": true, "reasons": [], "sanitize": {}, "obligations": {"audit": true}}
}

decision := out {
  # allow restricted dataset only for authorized roles
  input.resource.sensitivity == "restricted"
  "admin" in input.user.roles
  out := {"allow": true, "reasons": [], "sanitize": {}, "obligations": {"audit": true}}
}

decision := out {
  # for non-admins, sanitize instead of deny (optional pattern)
  input.resource.sensitivity == "restricted"
  not ("admin" in input.user.roles)
  out := {
    "allow": true,
    "reasons": ["sanitized_restricted_dataset"],
    "sanitize": {"mask_coordinates": true, "rounding_meters": 5000},
    "obligations": {"audit": true}
  }
}
```

---

### 3) 🔐 Endpoint protection (pipeline triggers)

```rego
package kfm.security

default allow = false

# Only Admin can run ingestion / pipeline actions
allow {
  input.request.path == "/api/v1/ingest/runPipeline"
  input.request.method == "POST"
  "admin" in input.user.roles
}
```

---

## 🧾 Auditing & provenance

Policies should be **auditable** and **replayable**.

Recommended logging fields (API responsibility, policy-defined requirement):
- `request_id`
- `user_id` (or pseudonymous id if required)
- `decision.allow`
- `decision.reasons`
- `decision.sanitize`
- `policy_version` (commit SHA or bundle hash)
- `resource_id` (dataset/story/tile layer id)
- `timestamp`

✅ Why this matters:
- If a decision is challenged later, we can identify **which exact policy** produced the decision.
- AI answers should include policy decision context as part of their provenance record.

---

## ❓ FAQ

### “Should policies deny, or sanitize?”
Both are valid. Prefer:
- **deny** when risk is unacceptable or requirements are missing (fail closed)
- **sanitize** when the use-case is legitimate but precision is harmful (e.g., sensitive sites)

### “Do we enforce policies only at runtime?”
No—CI policy gates prevent non-compliant assets and metadata from ever shipping.

### “Where does token validation happen?”
Typically **outside** OPA (API middleware verifies token), then passes claims to OPA:
- roles
- groups
- org affiliation
- scopes

OPA decides authorization + obligations; the API executes them.

---

## 📚 References (project library)
- Kansas Frontier Matrix — architecture, governance model, and policy-gated “truth path”
- KFM Technical Blueprint — policy-as-code approach (OPA/Rego), CI enforcement, audit/versioning patterns
- Privacy techniques — query auditing, inference controls, and differential privacy patterns (where needed)

> Keep this README aligned with the **real policy entrypoints** and **actual API integration points** as implementation evolves. 🌱
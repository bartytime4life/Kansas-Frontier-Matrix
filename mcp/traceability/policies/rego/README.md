# 🛡️ Rego Policy Pack — Traceability & Provenance (MCP)

![OPA](https://img.shields.io/badge/Open%20Policy%20Agent-OPA-blue)
![Rego](https://img.shields.io/badge/Policy%20Language-Rego-informational)
![Conftest](https://img.shields.io/badge/Runner-Conftest-success)
![Governance](https://img.shields.io/badge/Governance-FAIR%20%2B%20CARE-purple)
![Mode](https://img.shields.io/badge/Mode-Fail--Closed-critical)

> [!IMPORTANT]
> This folder contains **policy-as-code** rules (Rego) used to enforce KFM’s **contract-first + provenance-first** philosophy:
> - ✅ No “black box” layers, narratives, or AI answers  
> - ✅ Every output stays **traceable** (sources → transforms → outputs)  
> - ✅ Governance stays **explicit & reviewable** (policies versioned in Git)  
> - ✅ CI gates **fail closed** by default (waivers are deliberate + time-bounded)

---

## 🧭 What lives here?

This is the **Traceability slice** of the broader KFM Policy Pack (OPA + Conftest).  
Think of it as the “**trust gate**” that ensures anything merged, published, or served can answer:

- **Where did this come from?** (sources, licensing, providers)
- **What happened to it?** (pipeline run + transformations)
- **Who/what did it?** (agents, reviewers, tools, versions)
- **How can we verify it?** (evidence manifests, checksums, PROV links)
- **Is it safe to show/export?** (sensitivity, CARE/ethics, privacy constraints)

---

## 📚 Table of Contents

- [Quick Start](#-quick-start)
- [Policy Evaluation Flow](#-policy-evaluation-flow)
- [Core Artifacts & Inputs](#-core-artifacts--inputs)
- [Policy Categories](#-policy-categories)
- [Rule Conventions](#-rule-conventions)
- [Running Locally](#-running-locally)
- [Testing](#-testing)
- [Waivers](#-waivers)
- [Adding a New Policy](#-adding-a-new-policy)
- [Roadmap Ideas](#-roadmap-ideas)
- [Design Inputs](#-design-inputs)

---

## ⚡ Quick Start

### ✅ Prereqs
- **OPA** (Open Policy Agent)
- **Conftest** (policy runner commonly used in CI)
- A generated **PR snapshot** file (example: `repo.snapshot.json`) assembled by the project’s policy tooling (often under something like `api/scripts/policy/`).

### ▶️ Run policies against a snapshot
```bash
conftest test repo.snapshot.json -p mcp/traceability/policies/rego
```

### 🧪 Run unit tests
```bash
opa test -v mcp/traceability/policies/rego
```

> [!TIP]
> If your repo uses a different root policy dir (ex: `tools/validation/policy/`), keep this folder as a **vendorable module** and have CI include it.

---

## 🔁 Policy Evaluation Flow

```mermaid
flowchart TD
  A[PR / Commit] --> B[Snapshot Builder<br/>repo.snapshot.json]
  B --> C[Conftest / OPA Eval]
  C -->|deny[] not empty| D[❌ Block Merge (Fail Closed)]
  C -->|warn[] only| E[⚠️ Warn + Allow (Optional)]
  C -->|clean| F[✅ Merge]
  F --> G[Build / Ingest / Sim]
  G --> H[Run Manifest + PROV JSON-LD]
  H --> I[UI + Focus Mode show outputs<br/>with citations + lineage]
```

---

## 🧾 Core Artifacts & Inputs

KFM’s traceability layer is built around a few **portable, reviewable artifacts**:

### 1) 🧩 Repo / PR Snapshot (`repo.snapshot.json`)
A single JSON input describing what changed in a PR and the relevant parsed content, typically including:
- changed file paths
- parsed JSON/YAML where applicable
- optional diff context / metadata (author, branch, timestamps)
- optional linkouts to governance config

**Minimal example (illustrative):**
```json
{
  "repo": {
    "base": "main",
    "head": "feature/new-dataset",
    "changed_files": [
      {
        "path": "data/catalog/stac/items/foo.json",
        "kind": "stac-item",
        "parsed": { "id": "kfm.foo", "license": "CC-BY-4.0" }
      }
    ]
  }
}
```

---

### 2) 🧪 Run Manifest (`data/audits/<run_id>/run_manifest.json`)
A structured audit record per pipeline run. Typical fields include:
- `run_id`, `run_time`
- `idempotency_key`
- `canonical_digest` (hash of canonicalized manifest content)
- `source_urls`
- `tool_versions`
- `summary_counts` (records in/out, errors, etc.)

This manifest is **policy-checkable** and forms part of the trace ledger.

---

### 3) 🧾 PROV JSON-LD (W3C PROV)
Provenance is expected to be **mandatory** for publishing and governance.  
Policies commonly enforce:
- derived outputs must have matching PROV describing inputs + activity + agent
- PR-level provenance (optional/advanced): mapping Git history / PR actions to PROV-O

**Illustrative snippet (shape only):**
```json
{
  "@context": "https://www.w3.org/ns/prov.jsonld",
  "entity": { "...": {} },
  "activity": { "...": {} },
  "used": { "...": {} },
  "wasGeneratedBy": { "...": {} },
  "wasAssociatedWith": { "...": {} }
}
```

---

### 4) 🧷 Evidence Manifests (Narratives)
For Story Nodes / Pulse Threads, KFM favors **evidence-first narratives**:
- human-readable citations block (short)
- machine-readable evidence manifest (YAML/JSON)
- PROV bundle tying the narrative to sources + creation activity

**Why it matters:** it makes narratives **auditable** (like “supplementary material” built-in).

---

## 🧰 Policy Categories

This folder is **traceability-focused**, but it can be organized into subpackages that mirror the platform’s governance model:

- 📦 **Catalog / Metadata**  
  Validate required STAC/DCAT fields, licensing, provider/contact, stable IDs.

- 🧬 **Provenance**  
  Ensure PROV exists where required; enforce “no derived output without declared lineage”.

- 🧾 **Run Manifests**  
  Require manifests for automated ingests/sims; check digests/idempotency keys; verify tool versions logged.

- 🧷 **Evidence / Narrative Traceability**  
  Citations ↔ evidence manifest consistency; resolvable sources; checksums present.

- 🧠 **AI Traceability (Focus Mode)**  
  Require outputs include citations / provenance anchors; optionally enforce model/version disclosure.

- 🧿 **Sensitivity / CARE / Ethics**  
  If data is labeled sensitive, ensure proper flags/reviews/obfuscation requirements are satisfied.

- 🔒 **Security & Secrets**  
  Block obvious secrets; require pinned digests for containers; require signed artifacts where applicable.

- 🕵️ **Privacy / Inference Controls (optional runtime)**  
  Gate queries/exports when output could enable re-identification or inference.

---

## 🧩 Rule Conventions

### ✅ Packages
Use explicit, searchable package names:
- `package kfm.traceability.prov`
- `package kfm.traceability.manifest`
- `package kfm.traceability.evidence`
- `package kfm.traceability.privacy`

### 🏷️ Rule IDs
Policies should emit stable IDs in messages for fast triage:
- `KFM-PROV-###` (provenance)
- `KFM-MANI-###` (run manifests)
- `KFM-EVID-###` (evidence manifests)
- `KFM-SEC-###` (security)
- `KFM-PRIV-###` (privacy / inference control)

### 🚫 Deny / ⚠️ Warn pattern
Conftest commonly expects:
- `deny[msg]` → blocks merge
- `warn[msg]` → advisory (optional)

**Example skeleton:**
```rego
package kfm.traceability.prov

deny[msg] {
  some f in input.repo.changed_files
  is_derived_output(f.path)
  not has_matching_prov(f.path)
  msg := sprintf("KFM-PROV-001: %s changed but no matching PROV update was found.", [f.path])
}

# helpers (recommended pattern)
is_derived_output(path) { endswith(path, ".parquet") }
has_matching_prov(path) { false } # TODO: implement lookup logic
```

> [!NOTE]
> Keep helper logic in `_lib/` so rules stay readable and testable.

---

## 🧑‍💻 Running Locally

### Option A: Conftest (most CI-like)
```bash
conftest test repo.snapshot.json \
  -p mcp/traceability/policies/rego
```

### Option B: OPA eval (debugging)
```bash
opa eval -d mcp/traceability/policies/rego -i repo.snapshot.json "data.kfm.traceability"
```

> [!TIP]
> Add a small `make policy` or `task policy` wrapper so contributors can run this without memorizing flags.

---

## 🧪 Testing

Recommended structure:
```
📁 mcp/traceability/policies/rego
├─ 📄 README.md
├─ 📁 _lib/                  # helpers
├─ 📁 provenance/             # prov rules
├─ 📁 manifests/              # run manifest rules
├─ 📁 evidence/               # story/pulse evidence rules
├─ 📁 security/               # secrets/supply-chain rules
└─ 📁 tests/
   ├─ 📁 fixtures/
   └─ 🧪 *_test.rego
```

### Writing tests (OPA)
```rego
package kfm.traceability.prov_test

test_missing_prov_is_denied {
  input := {
    "repo": {
      "changed_files": [{"path": "data/derived/foo.parquet"}]
    }
  }
  denies := data.kfm.traceability.prov.deny with input as input
  count(denies) > 0
}
```

Run:
```bash
opa test -v mcp/traceability/policies/rego
```

---

## 🪪 Waivers

Waivers are allowed, but should be:
- ✅ explicit
- ✅ scoped (file globs / rule ids)
- ✅ time-bounded (expiry)
- ✅ reviewed

**Suggested `waivers.yml` shape:**
```yaml
waivers:
  - id: WVR-2026-0001
    rule_id: KFM-PROV-001
    scope:
      paths:
        - "data/legacy/**"
    expires: "2026-06-01"
    reason: "Legacy import missing upstream provenance; remediation scheduled."
    approved_by: "FAIR+CARE Council / Maintainer"
```

> [!WARNING]
> Waivers should never silently become permanent. Expired waivers should fail CI.

---

## ➕ Adding a New Policy

1. 🧩 Pick a category + ID (ex: `KFM-EVID-002`)
2. 🧾 Write the rule in the appropriate package folder
3. 🧪 Add tests with fixtures
4. 🧵 Ensure the message is actionable:
   - what failed
   - why it matters
   - how to fix
5. 🔍 Keep it deterministic (avoid time-based randomness)
6. ✅ Make sure it fails closed unless intentionally warning-only

---

## 🧠 Roadmap Ideas

These are **future-friendly** areas to expand traceability governance:

### 🔎 Privacy & Inference Control (runtime OPA)
- Query auditing: deny queries that could enable disclosure via inference
- Differential privacy / noise-on-outputs policies for certain aggregates
- k-anonymity / l-diversity / t-closeness thresholds for publishable exports

### 🌍 AR / 4D Digital Twin outputs
- Require the same provenance + evidence manifests for AR overlays & temporal simulations
- Ensure attribution carries into exported AR scenes

### 🧾 Supply-chain hardening
- Require signed artifacts (Cosign)
- Require SLSA provenance attestations for automated PRs and build outputs
- Enforce pinned digests for container bases and tooling

---

## 🗂️ Design Inputs

This README is intentionally aligned with the project’s existing design documentation and research packs:

### ✅ Core KFM design docs
- `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf`
- `Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf`
- `Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf`
- `Kansas Frontier Matrix – Comprehensive UI System Overview.pdf`
- `📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf`
- `🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf`
- `Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf`
- `Additional Project Ideas.pdf`

### 📦 Knowledge packs (PDF portfolios)
> [!TIP]
> These are PDF portfolios (open in Adobe Reader/Acrobat for best browsing). They are included as reference packs that inform policy thinking across AI, security, data engineering, and geospatial tooling.

- `AI Concepts & more.pdf` (AI/ML books & references)
- `Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf` (GIS/WebGL/virtual worlds)
- `Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf` (data engineering, stats, cryptography, governance)
- `Various programming langurages & resources 1.pdf` (language + CI/CD references)

---

### 🧭 One-liner philosophy (for contributors)
> “If you can’t show your work (sources, transforms, provenance), it doesn’t ship.” ✅

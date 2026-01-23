<!--
📄 File: mcp/traceability/policies/waivers/README.md
🧭 Scope: Policy Pack waivers (time‑bound exceptions) with full traceability hooks.
-->

# 🧾 Policy Waivers (Traceability • Policy Pack)

![OPA / Conftest](https://img.shields.io/badge/OPA%20%2B%20Conftest-Policy%20Pack-informational)
![Provenance-first](https://img.shields.io/badge/Provenance-First%20Class-success)
![FAIR+CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Governance%20Core-blue)
![Fail-Closed](https://img.shields.io/badge/Default-Fail--Closed-critical)

> 🚨 **Waivers are exceptions, not a workflow.**  
> If you can fix the policy failure, fix it. If you must ship or ingest before fixing it, **waive it with guardrails, evidence, and an expiration**.

---

## ✨ TL;DR

A **waiver** is a **time‑boxed** and **reviewed** exception to an automated policy gate (CI and/or runtime).  
This folder is where those exceptions live so that KFM can stay:

- **Transparent** (everyone can see the rule, the exception, and who approved it)
- **Reproducible** (every exception points to the exact run + inputs + outputs)
- **Accountable** (every exception expires and is re‑reviewed)

---

## 🧠 Why this exists (KFM philosophy)

KFM is built around governance that’s **codified**, **auditable**, and **user-visible**:
- policy-as-code gates (CI + runtime),
- provenance-first data lifecycle,
- a governance ledger / audit trail,
- and UI that surfaces source & lineage “behind the map.” 🗺️🔎

Waivers are the **pressure valve** that preserves shipping velocity *without* breaking trust.

---

## ✅ What waivers are allowed to do

Waivers can be used when a requirement is **temporarily impossible** or **temporarily not actionable**, for example:

- 🧾 **Catalog/Metadata gaps**: missing optional metadata fields while an upstream source is being clarified.
- 📜 **Licensing delays**: license text is pending written confirmation but ingestion is urgent for internal review.
- 🧹 **Style/Lint/Test friction**: temporary exceptions during large refactors, migrations, or toolchain transitions.
- 🧪 **R&D sandbox**: allowing experimental pipelines/models **in non-public environments** with clear “provisional” labeling.
- ⚡ **Operational emergencies**: a time-critical patch that requires a narrowly scoped exception (with follow-up remediation).

---

## 🚫 What waivers must NOT do (hard gates)

The following are **non-negotiable** (or only waivable in **isolated sandbox** modes that cannot publish to users):

- 🔒 **No secrets / credential leakage** (ever).
- 🧬 **No bypassing provenance for public outputs** (no “mystery layers”).
- 🧑‍⚖️ **No publishing restricted/sensitive data** without the correct approvals and handling.
- 🤖 **No disabling citation/provenance requirements for user-facing AI outputs**.
- 🧯 **No weakening security controls** without a compensating control + explicit security review.

If you think you need to waive one of the above, stop and escalate through governance review.

---

## 🗂️ Where waivers fit in the policy system

KFM policies are typically grouped into categories (example taxonomy):

- 🗃️ **Catalogs**
- ⛓️ **Provenance**
- 🧭 **Sovereignty / Sensitivity**
- 🔌 **API**
- 📚 **Story**
- 🛡️ **Security**
- 🎨 **Style**

Each policy is referenced by a stable ID (example pattern: `KFM-CAT-001`, `KFM-PROV-001`, etc.).  
Waivers must reference **exactly one** policy ID per waiver record (scope can be multiple files/artifacts, but the policy target is singular).

---

## 🧬 Traceability requirements (the “Evidence Bundle”)

Every waiver must link to an **evidence bundle** that makes the exception auditable:

- 🧾 **Policy ID** being waived
- 🧪 **Run Manifest** (pipeline/run record: inputs, outputs, environment, hashes)
- 🧬 **PROV** lineage artifact(s) (what used what, what generated what)
- 🗺️ **STAC/DCAT** metadata references (discovery + distributions)
- 🧾 **CI run / checks** (what failed, what passed, what was skipped)
- 🏛️ **Approval record** (who approved, what roles, when)
- 🧯 **Mitigation plan** (what prevents harm *now*)
- 🧹 **Remediation plan** (what will remove the waiver)

> 💡 If the waiver is for something that impacts the UI or exports, add a **user-visible disclaimer plan** (e.g., “Provisional” badge in provenance panel + export footer note).

---

## 🧾 Waiver file formats

This directory supports **two complementary representations**:

1) **`waivers.yml`** (index for automation)
2) **One waiver file per waiver** (human-readable, PR-reviewable)

### 📌 Naming convention (recommended)

`WAIVER__<POLICY_ID>__<TRACKING_ID>__YYYY-MM-DD.md`

Examples:
- `WAIVER__KFM-CAT-001__GH-1234__2026-01-23.md`
- `WAIVER__KFM-PROV-004__OPS-778__2026-01-23.md`

---

## 🧩 Waiver template (copy/paste)

<details>
<summary><strong>📄 Waiver Markdown Template</strong> (click to expand)</summary>

```markdown
---
waiver_id: WAIVER-2026-0001
policy_id: KFM-CAT-001
status: proposed # proposed | active | expired | revoked
requested_by: github:@your-handle
requested_on: 2026-01-23
expires_on: 2026-02-23

scope:
  repo_paths:
    - data/catalog/your_dataset.stac.json
    - data/dcat/your_dataset.json
  artifacts:
    - oci://registry.example/kfm/data/your_dataset@sha256:...
  environments:
    - ci
    - staging

impact:
  user_visible: false
  affects_exports: false
  affects_focus_mode: false

risk:
  level: low # low | medium | high | critical
  summary: "License text pending from upstream; dataset stays internal until resolved."

evidence:
  policy_failure:
    conftest_output: "CI job link or pasted conftest deny message"
  traceability:
    run_manifest: "data/provenance/run-manifests/RUN-2026-01-22T10-11-00Z.json"
    prov: "data/provenance/prov/your_dataset__RUN-....jsonld"
    stac: "data/catalog/your_dataset.stac.json"
    dcat: "data/dcat/your_dataset.json"
  approvals:
    - role: Maintainer
      approver: github:@maintainer1
      date: 2026-01-23
    - role: FAIR+CARE Council (if required)
      approver: github:@council-rep
      date: 2026-01-23

mitigations:
  - "Dataset remains non-public (internal only) until license confirmed."
  - "Exports disabled for this dataset in UI until waiver removed."

remediation:
  owner: github:@your-handle
  tracking_issue: "GH-1234"
  plan:
    - "Obtain written license confirmation from upstream."
    - "Update DCAT license field + add citation."
    - "Remove waiver + rerun CI policy gate."

rollback:
  plan: "Revert PR / remove dataset references from catalogs if license not obtained before expiry."
---

# Rationale

Explain the situation, why a waiver is needed, and why it’s safe **with mitigations**.

## What’s blocked?

Describe the failing policy gate and the failing artifact(s).

## Why the waiver is the least-bad option

Explain why immediate compliance is not feasible today.

## Safety & ethics notes (FAIR+CARE)

Call out any Authority-to-Control, sensitive locations, or community protocols.
```

</details>

---

## 🔁 Waiver lifecycle

```mermaid
flowchart TD
  A[Policy Gate Fails 🚫] --> B{Fix is feasible now?}
  B -- Yes --> C[Fix policy violation ✅]
  B -- No --> D[Create waiver record 🧾]
  D --> E[Attach evidence bundle 🧬]
  E --> F[Approval workflow 👥]
  F --> G[Waiver becomes ACTIVE ⏳]
  G --> H[Mitigate + label (UI/exports) 🏷️]
  H --> I[Remediate root cause 🧹]
  I --> J[Remove waiver + re-run gates ✅]
  G --> K[Expiry date reached 🕰️]
  K --> L{Renew justified?}
  L -- No --> M[Waiver EXPIRES ❌ + rollback if needed]
  L -- Yes --> N[Renew with updated evidence + approvals 🔁]
```

---

## 👥 Approval matrix (recommended)

| Risk level | Typical use | Minimum approvers | Notes |
|---|---|---|---|
| **Low** | Cosmetic metadata, non-public docs | 1 Maintainer | Must still expire |
| **Medium** | Catalog gaps, temporary QA bypass | Maintainer + Domain Steward | Add mitigation steps |
| **High** | Anything touching sensitivity, governance, exports | Maintainer + FAIR+CARE Council | Often requires community liaison |
| **Critical** | Anything that could expose harm or weaken security | Maintainer + Security + FAIR+CARE Council | Prefer “no waiver” — redesign |

---

## 🤖 AI / Focus Mode waiver rules

KFM’s AI governance assumes:
- outputs are logged,
- citations/provenance are mandatory,
- bias/drift checks exist,
- and unsafe prompts are mitigated via prompt-security layers.

**Waivers must not allow user-facing AI outputs without citations.**  
If an experiment requires different behavior, it must occur in an explicitly labeled **sandbox** environment that cannot publish.

---

## 🗺️ UI implications (provenance must stay visible)

If a waiver affects anything user-visible (layers, stories, exports):

- Add a 🏷️ **“Provisional”** or **“Restricted”** indicator in the layer/story provenance panel.
- Ensure exports include the same disclaimer (footer or metadata sidecar).
- Ensure share links preserve the waiver state (so downstream users can see it).

---

## 🔐 Supply chain + artifact integrity

If the waiver references OCI-hosted artifacts (tiles, models, data packs):

- Prefer immutable digests (`@sha256:...`) over floating tags.
- Prefer signed artifacts where possible.
- Include the artifact digest in the evidence bundle so that future audits can retrieve the exact bytes.

---

## 🧪 Example waivers

<details>
<summary><strong>Example: Temporary missing license field (internal-only)</strong></summary>

- **Policy**: `KFM-CAT-001` (license required)
- **Reason**: upstream agency email confirmation pending
- **Mitigation**: dataset marked internal-only; exports disabled
- **Expiry**: 30 days
- **Remediation**: update DCAT license + remove waiver
</details>

<details>
<summary><strong>Example: Experimental pipeline non-determinism (sandbox)</strong></summary>

- **Policy**: `KFM-PROV-00X` (determinism / reproducibility expectation)
- **Reason**: early prototype model produces slight diffs run-to-run
- **Mitigation**: sandbox only; no publishing; store full run manifests + seeds; label “Experimental”
- **Expiry**: 14 days (short leash)
- **Remediation**: add determinism controls or promote as a separate “research-only” module
</details>

---

## ✅ Maintainer checklist

- [ ] Waiver references **one** policy ID
- [ ] Expiration date is set (short, realistic)
- [ ] Evidence bundle is complete (run manifest + PROV + catalogs)
- [ ] Mitigations are specific and enforceable
- [ ] Remediation has an owner + tracking issue
- [ ] User-visible impacts are labeled (if applicable)
- [ ] Renewal (if any) requires updated evidence + fresh approvals

---

## 📚 Design inputs (project files)

These project documents informed how KFM treats governance, traceability, UI transparency, and policy enforcement:

- **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf**
- **Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf**
- **Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf**
- **Kansas Frontier Matrix – Comprehensive UI System Overview.pdf**
- **📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf**
- **🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf**
- **Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf**
- **Additional Project Ideas.pdf**
- **Scientific Method _ Research _ Master Coder Protocol Documentation.pdf**
- **MARKDOWN_GUIDE_v13.md.gdoc**
- **AI Concepts & more.pdf** *(PDF portfolio bundle)*
- **Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf** *(PDF portfolio bundle)*
- **Various programming langurages & resources 1.pdf** *(PDF portfolio bundle)*
- **Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf** *(PDF portfolio bundle)*

---

## 🧭 Related directories (expected)

- `mcp/traceability/` — traceability framework and evidence patterns
- `mcp/traceability/policies/` — policy IDs, rationale, and policy-as-code sources
- `tools/validation/policy/` — OPA/Rego policy pack + Conftest entrypoints
- `data/catalog/` + `data/dcat/` + `data/provenance/` — metadata + lineage artifacts

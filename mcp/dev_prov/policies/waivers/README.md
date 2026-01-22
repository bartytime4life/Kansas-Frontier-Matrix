# 🧾 Policy Waivers (MCP · Dev Provenance)

![Policy-as-Code](https://img.shields.io/badge/policy--as--code-OPA%20%2B%20Conftest-blue)
![Fail Closed](https://img.shields.io/badge/default-fail--closed-critical)
![Provenance](https://img.shields.io/badge/provenance-PROV--O%20tracked-success)
![Governance](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-informational)

> [!IMPORTANT]
> A **waiver** is a **time-bound, narrowly-scoped, human-approved exception** to a policy gate.  
> It is **not** a bypass, **not** “just this once forever,” and **not** a way around provenance, sovereignty, or security.

---

## 🔗 Quick Navigation

- [✨ Why waivers exist](#-why-waivers-exist)
- [📁 Where waivers live](#-where-waivers-live)
- [🧠 What can be waived vs cannot](#-what-can-be-waived-vs-cannot)
- [🧾 Waiver file format](#-waiver-file-format)
- [🧑‍⚖️ Approval matrix](#-approval-matrix)
- [🔁 Waiver lifecycle](#-waiver-lifecycle)
- [🤖 Agents & automation rules](#-agents--automation-rules)
- [🧬 Provenance + governance ledger integration](#-provenance--governance-ledger-integration)
- [🗺️ UI + export behavior](#️-ui--export-behavior)
- [🧪 Examples](#-examples)
- [🧰 Templates](#-templates)
- [📚 Source docs used](#-source-docs-used)

---

## ✨ Why waivers exist

Kansas Frontier Matrix (KFM) treats governance as **policy-as-code** (OPA/Rego + Conftest), enforced in CI and optionally at runtime. Policies encode things like:

- **FAIR/CARE governance** (licenses, provenance, classification propagation)
- **Security** (no secrets, no sensitive leaks)
- **Evidence-first narratives** (citations required, AI text labeled)
- **Operational integrity** (mandatory CI checks, link checks, schema validation)

That “fail-closed” posture is intentional: if something is missing (license, provenance links, classification safety), CI blocks the merge.

A waiver exists for the cases where:
- We need forward motion **without lying** about compliance
- The issue is **real, tracked, and fixable**
- The exception is **temporary**, **reviewed**, and **visible/auditable**

---

## 📁 Where waivers live

Recommended structure (keep it boring, predictable, and reviewable):

```text
📦 mcp/
 └─ 📦 dev_prov/
    └─ 📦 policies/
       └─ 📦 waivers/
          ├─ 📄 README.md              👈 you are here
          ├─ 📄 waivers.yml            ✅ single source of truth (default)
          └─ 📁 examples/              🧪 copy/paste-ready samples
             ├─ 📄 KFM-WVR-2026-0001.yml
             └─ 📄 KFM-WVR-2026-0002.yml
```

> [!NOTE]
> If your repo already uses a different convention (e.g., per-domain waiver files), keep the **schema identical** and add a small loader that merges them into a single in-memory list for policy evaluation.

---

## 🧠 What can be waived vs cannot

### 🚫 “Hard No” (Non-waivable)
These are “stop the world” constraints because waiving them breaks trust, safety, or sovereignty:

- 🔐 **Secrets / credentials scanning**
- 🧬 **Classification / sovereignty downgrades**
  - You can’t produce an output less restricted than the most restricted input.
- 🧍 **PII exposure / sensitive location leaks**
- 🧾 **Published human-facing content without sources**
  - (Internal drafts can be treated differently via *policy design*, not ad-hoc waivers.)
- 🧷 **Tampering with raw evidence**
  - Raw data must remain immutable; transformations happen downstream with explicit configs.
- 🧰 **“Waive the waiver”**
  - Any attempt to add a waiver without required fields/approvals must fail CI.

### ✅ “Usually OK” (Waiverable with guardrails)
These are common, legitimate exceptions **when time-bound and tracked**:

- 📜 **License metadata temporarily missing** (external provider delay)
- 🔗 **External link checks failing** (upstream website downtime)
- 📦 **Supply-chain signature enforcement** (dev-only, temporary, with compensating controls)
- 🧪 **Experimental feature flags** (limited scope; clearly labeled in UI as “experimental”)
- 🌱 **Telemetry artifact missing** (only if sustainability auditor approves; strict expiry)

---

## 🧾 Waiver file format

Default: `waivers.yml`

### ✅ Required principles
A valid waiver must be:

- ⏳ **Time-bound** (expires)
- 🎯 **Scoped** (what it applies to)
- 🧑‍⚖️ **Approved** (role-based approvals)
- 🧾 **Justified** (reason + impact + remediation)
- 🧬 **Provenance-linked** (issue/PR + artifact identifiers/digests where applicable)

---

### 📄 `waivers.yml` schema (recommended)

```yaml
schema_version: 1

waivers:
  - waiver_id: "KFM-WVR-2026-0001"
    status: "approved"            # proposed | approved | denied | expired
    policy_id: "KFM-CAT-001"      # stable policy ID (Catalogs/Provenance/etc.)
    title: "Temporary license waiver for upstream dataset"

    # ✅ Scope (match rules)
    scope:
      paths:
        - "data/catalogs/dcat/**/*.json"
      dataset_ids:
        - "usgs_nwis_realtime_water"
      environments:
        - "ci"                    # ci | dev | staging | prod
      notes: "Applies only to DCAT record for this dataset."

    # ✅ Time bounds
    requested_at: "2026-01-22"
    expires_at: "2026-02-15"      # MUST be set (short-lived by default)

    # ✅ Why this waiver is needed
    reason: >
      Upstream publisher has not yet provided formal license text; dataset is
      widely used operationally and already public, but license metadata is pending.
    impact: >
      Catalog completeness reduced until license confirmed; downstream reuse must be
      treated as provisional.

    # ✅ Compensating controls (what we do instead right now)
    compensating_controls:
      - "Mark dataset as provisional in UI badges and exports."
      - "Block packaging into offline packs until license confirmed."

    # ✅ Remediation plan (how it gets removed)
    remediation_plan:
      - "Obtain license statement from upstream contact."
      - "Update DCAT license field + add evidence link."
      - "Remove waiver entry."
    tracking:
      issue: "#1234"
      pr: "#1237"

    # ✅ Evidence and integrity anchors
    evidence:
      - type: "email"
        ref: "docs/evidence/licenses/usgs_nwis_2026-01-20.eml"
      - type: "url"
        ref: "https://example.org/dataset-page"
      - type: "artifact_digest"
        ref: "sha256:abcdef..."

    # ✅ Approvals (role-based)
    approvals:
      - role: "maintainer"
        approver: "@repo-maintainer"
        date: "2026-01-22"
      - role: "faircare_council"
        approver: "@council-chair"
        date: "2026-01-22"

    # ✅ Provenance hooks (optional but strongly recommended)
    provenance:
      prov_activity_id: "prov:kfm:waiver:KFM-WVR-2026-0001"
      governance_ledger_ref: "ledger:entry:2026-01-22-0009"
```

---

### 🧷 Scope matching rules (how policies should interpret waivers)

A policy denial is considered waived **only if**:

1. `policy_id` matches exactly ✅  
2. waiver `status == approved` ✅  
3. `expires_at` is in the future ✅  
4. the target is inside scope (path / dataset_id / environment) ✅  
5. the waiver includes required approvals ✅  

> [!TIP]
> “Scope” must be **narrow by default**. If you find yourself writing `**/*`, you probably want a policy refactor (or multiple targeted waivers with short lifetimes), not a blanket waiver.

---

## 🧑‍⚖️ Approval matrix

Use roles (not individuals) so the governance model scales.

| Policy domain 🧩 | Examples | Required approvers ✅ | Notes |
|---|---|---|---|
| 📚 Catalogs (`KFM-CAT-*`) | license missing, contact missing | Maintainer + FAIR/CARE rep | Often acceptable with short expiry |
| 🧬 Provenance (`KFM-PROV-*`) | missing provenance links | Maintainer + Data Steward | **Never** waive provenance for *published outputs* |
| 🪶 Sovereignty (`KFM-SOV-*`) | classification propagation | FAIR/CARE Council + Community Liaison | Usually **non-waivable** (fix policy design instead) |
| 🔐 Security (`KFM-SEC-*`) | secret scanning | Security Lead | Usually **non-waivable** |
| 📖 Story (`KFM-STORY-*`) | citations required | Story Steward + Maintainer | Public narratives must remain evidence-backed |
| 🧠 AI (`KFM-AI-*`) | citation coverage, prompt rules | AI Steward + Maintainer | “No citations” is **non-waivable** for user-facing AI |
| 🌱 Telemetry (`KFM-TEL-*`) | energy report artifact | Sustainability Auditor + Maintainer | Short expiry; document reason + mitigation |

---

## 🔁 Waiver lifecycle

```mermaid
flowchart TD
  A[Policy gate fails in CI ❌] --> B{Can we fix root cause now?}
  B -- Yes --> C[Fix + rerun CI ✅]
  B -- No --> D[Create waiver request (Issue + PR)]
  D --> E{Is it waiverable?}
  E -- No --> F[Reject ❌ + escalate to Council/Security]
  E -- Yes --> G[Add waiver entry (scoped + expiring)]
  G --> H[Required approvals attached ✅]
  H --> I[CI re-runs: deny becomes waived warning ⚠️]
  I --> J[Merge PR (no auto-merge) 🔒]
  J --> K[Ledger + PROV updated 🧬]
  K --> L[Remediation work tracked 🎯]
  L --> M{Waiver removed before expiry?}
  M -- Yes --> N[Clean compliance restored ✅]
  M -- No --> O[Waiver expires ⏳ → CI blocks again ❌]
```

---

## 🤖 Agents & automation rules

KFM-style automation (Watcher–Planner–Executor) is powerful, but must remain **auditable** and **human-reviewed**.

Rules:

- 🤖 Agents may **propose** a waiver (open Issue + PR), but **cannot approve** it.
- 🧑‍💻 Waivers must go through the same PR review and CI gates as human changes.
- 🧨 If an agent starts producing risky proposals, use the **kill-switch** and investigate.
- 🧾 If commits are signed/attested (Sigstore/Cosign), include the attestation reference under `evidence`.

---

## 🧬 Provenance + governance ledger integration

Waivers are governance events. Treat them as first-class provenance artifacts:

- 📌 Record the waiver as a PROV activity/entity (`prov_activity_id`)
- 🧾 Append a ledger entry referencing:
  - waiver_id
  - policy_id
  - scope
  - approvals (role + date)
  - expiry
  - artifact digests when relevant (OCI digests, run manifests, etc.)

> [!IMPORTANT]
> Waivers should be queryable in the same way datasets, runs, and AI outputs are queryable: **who approved what, when, and why**.

---

## 🗺️ UI + export behavior

Because KFM emphasizes “the map behind the map,” waivers must be **visible** where users might reasonably rely on impacted outputs:

- 🏷 UI badges should show: `WAIVED (expires YYYY-MM-DD)` for affected datasets/layers/stories
- 🧾 Exports (maps, story bundles, offline packs) should include waiver metadata in:
  - attribution footnotes
  - provenance panels (“Layer Provenance”)
  - generated citations bundles for AI narratives

If a waiver reduces user trust (license unknown, provisional data), UI should nudge toward verification:
- “Provisional until license confirmed”
- “Restricted until community approval”
- “Experimental feature—validation pending”

---

## 🧪 Examples

### Example 1 — License temporarily missing (Catalog policy)

```yaml
waiver_id: "KFM-WVR-2026-0003"
status: "approved"
policy_id: "KFM-CAT-001"
title: "License metadata pending from upstream"

scope:
  paths: ["data/catalogs/dcat/usgs_nwis_realtime.json"]
  dataset_ids: ["usgs_nwis_realtime_water"]
  environments: ["ci", "dev"]

requested_at: "2026-01-22"
expires_at: "2026-02-15"

reason: "Upstream license statement pending; dataset already public; enforcement would block ingestion pipeline update."
impact: "Reuse terms unclear until license confirmed."
compensating_controls:
  - "UI shows 'Provisional license' badge"
  - "No offline pack export"
remediation_plan:
  - "Obtain written license statement"
  - "Update DCAT license + remove waiver"
tracking:
  issue: "#1234"
  pr: "#1237"
approvals:
  - role: "maintainer"
    approver: "@maintainer"
    date: "2026-01-22"
  - role: "faircare_council"
    approver: "@council-chair"
    date: "2026-01-22"
```

### Example 2 — Artifact signature waiver (dev-only)

```yaml
waiver_id: "KFM-WVR-2026-0004"
status: "approved"
policy_id: "KFM-SEC-040"
title: "Allow unsigned OCI artifact in dev while registry signing pipeline is repaired"

scope:
  paths: ["artifacts/registry/**"]
  environments: ["dev"]     # 🚫 NOT allowed in prod

requested_at: "2026-01-22"
expires_at: "2026-01-29"

reason: "Cosign signer workflow temporarily failing; dev iteration blocked."
impact: "Reduced supply-chain integrity in dev environment only."
compensating_controls:
  - "Pin artifact by digest only (no tags)"
  - "Restrict access to dev registry"
  - "Manual hash verification in PR review"
remediation_plan:
  - "Fix cosign signer job"
  - "Re-sign artifacts and remove waiver"
tracking:
  issue: "#1301"
approvals:
  - role: "security_lead"
    approver: "@security"
    date: "2026-01-22"
  - role: "maintainer"
    approver: "@maintainer"
    date: "2026-01-22"
```

### Example 3 — Telemetry artifact missing (sustainability gate)

```yaml
waiver_id: "KFM-WVR-2026-0005"
status: "approved"
policy_id: "KFM-TEL-010"
title: "Telemetry JSON temporarily missing for one pipeline run"

scope:
  paths: ["data/audits/2026-01-22-run-009/**"]
  environments: ["ci"]

requested_at: "2026-01-22"
expires_at: "2026-02-01"

reason: "Telemetry collector crashed mid-run; rerun would delay time-sensitive update."
impact: "Sustainability report incomplete for this run."
compensating_controls:
  - "Post-run manual summary added to audit README"
  - "Telemetry collector fix prioritized"
remediation_plan:
  - "Patch telemetry collector"
  - "Backfill telemetry for this run if possible"
tracking:
  issue: "#1408"
approvals:
  - role: "sustainability_auditor"
    approver: "@sustainability"
    date: "2026-01-22"
  - role: "maintainer"
    approver: "@maintainer"
    date: "2026-01-22"
```

---

## 🧰 Templates

<details>
<summary><strong>📝 Waiver Request (Issue Template)</strong></summary>

```markdown
## 🧾 Waiver Request

**Policy ID:** (e.g., KFM-CAT-001, KFM-PROV-001)  
**Proposed Waiver ID:** (e.g., KFM-WVR-YYYY-NNNN)  
**Scope:** (paths, dataset_ids, environment)  
**Expires:** (YYYY-MM-DD)  

### Why is this needed?
Explain the blocking condition and why it cannot be fixed immediately.

### Impact
What trust/compliance signal is reduced? Who is affected?

### Compensating controls
What will we do to reduce risk while the waiver exists?

### Remediation plan
Concrete steps + owner(s) + target date to remove waiver.

### Evidence
Links/files/emails/artifact digests that support the claim.

### Approvals needed
- [ ] Maintainer
- [ ] Security Lead (if SEC/SUPPLY)
- [ ] FAIR/CARE Council (if SOV/SENSITIVE)
- [ ] Community Liaison (if cultural/Indigenous data)
- [ ] Sustainability Auditor (if telemetry/energy gates)
- [ ] AI Steward (if AI policy)
```
</details>

<details>
<summary><strong>✅ PR Checklist for Waivers</strong></summary>

```markdown
- [ ] Waiver is **scoped** (no broad globs without justification)
- [ ] Waiver has a **short expiry**
- [ ] Waiver includes **reason + impact**
- [ ] Waiver includes **compensating controls**
- [ ] Waiver includes **remediation plan** + tracking issue
- [ ] Required **role approvals** captured
- [ ] UI/export visibility considered (badges, provenance panel, attribution)
- [ ] If applicable: artifact digests / run manifest hashes included
```
</details>

---

## 📚 Source docs used

This README is derived from the project’s design and governance documents, including (but not limited to):

- 📘 **KFM Data Intake – Technical & Design Guide** (policy pack, waiver mechanics, governance workflows, agent architecture)
- 🧭 **KFM AI System Overview** (governance ledger, provenance panels, citations + governance checks)
- 🗺️ **KFM UI System Overview** (provenance surfaced in UI; exports carry attribution)
- 🏗️ **KFM Architecture, Features, and Design** (OPA/Conftest policy pack; runtime and CI enforcement)
- 🧾 **KFM Comprehensive Technical Documentation** (sensitive data handling; permission & generalization)
- 💡 **Innovative Concepts to Evolve KFM** (credit/authority; policy + ethics; future AR/digital twin implications)
- 🧰 **Additional Project Ideas** (OCI artifacts, Cosign signatures, run manifests, canonical hashing, fail-closed gates)
- 🌟 **Latest Ideas & Future Proposals** (PR → PROV mapping and dev provenance traceability)
- 📦 **Resource Portfolios** (AI concepts, data management/Bayesian methods, programming resources, geospatial/WebGL references)

> [!NOTE]
> Several reference PDFs are stored as **PDF portfolios** (collections). Open them in a PDF portfolio-capable viewer when you need the embedded sub-documents.

---

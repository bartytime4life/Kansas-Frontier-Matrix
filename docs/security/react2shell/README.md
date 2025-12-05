---
title: "🛡️ KFM v11.2.4 — React2Shell (CVE-2025-55182 / 66478) Emergency Hardening Playbook"
path: "docs/security/react2shell/README.md"
version: "v11.2.4"
last_updated: "2025-12-05"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Monthly · Supply Chain Security · Frontend Risk Council"
content_stability: "stable"
backward_compatibility: "n/a (security bulletin)"
status: "Active / Enforced"

doc_kind: "Security Bulletin"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "security/frontend"
  applies_to:
    - "frontend"
    - "react"
    - "nextjs"
    - "ssr"
    - "ci-cd"
    - "supply-chain"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Medium-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
classification: "Public"
indigenous_rights_flag: true

commit_sha: "<latest-commit-sha>"
previous_version_hash: "<prior-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../releases/v11.2.4/security-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/security-incident-schema-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"

doc_uuid: "urn:kfm:doc:security:react2shell-hardening-v11.2.4"
semantic_document_id: "kfm-doc-security-react2shell-hardening-v11.2.4"
event_source_id: "ledger:kfm:doc:security:react2shell-hardening"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
---

<div align="center">

# 🛡️ React2Shell Critical Vulnerability Response (KFM Hardening Bulletin)  
`docs/security/react2shell/README.md`

**Purpose:**  
Define KFM’s governed emergency response and long-term hardening protocol for the React2Shell vulnerability (CVE-2025-55182 / CVE-2025-66478), ensuring all React/Next.js-based frontends, SSR workers, and build pipelines are patched, isolated, and continuously verified under deterministic, SBOM-verified supply-chain rules.

</div>

---

## 📘 Overview

The **React2Shell** vulnerability family (CVE-2025-55182 / CVE-2025-66478) enables **unauthenticated remote code execution (RCE)** through unsafe handling of React Server Components (RSC) flight payloads in **React 19.x** and downstream frameworks, including **Next.js** and related RSC-enabled stacks.

For KFM, this bulletin:

- Classifies React2Shell as a **critical supply-chain and runtime risk**.  
- Establishes **minimum safe versions** for React, Next.js, and RSC-related packages.  
- Defines a **five-step mitigation pipeline** that must be followed for all affected deployments.  
- Locks in **permanent frontend architecture adjustments** to reduce the RSC attack surface.  
- Integrates React2Shell handling with:
  - SLSA + SBOM verification.  
  - Frontend runtime isolation.  
  - Zero-trust ingestion perimeter.  
  - Event-driven CI/CD auditing and telemetry.  

All KFM deployments and forks that use React/Next.js must treat this document as **normative** until superseded.

---

## 🗂️ Directory Layout

```text
📂 docs/security/
└── 📂 react2shell/
    ├── 📄 README.md           # 🛡️ React2Shell Hardening Bulletin (this file)
    ├── 📄 mitigations.md      # 📜 Detailed mitigation patterns & examples
    ├── 📄 waf-rules.md        # 🧱 WAF rule definitions & deployment notes
    ├── 📂 sbom-diff/          # 🧪 SBOM diff reports (before/after patches)
    └── 📂 audits/             # ✅ Audit reports & red-team findings
```

Any additional React2Shell-related docs (e.g., incident-specific timelines) must be added under `audits/` or linked from this index.

---

## 🧭 Context

### 1. Affected KFM components

#### 1.1 Frontend cluster

- `src/web/kfm-frontend/` (React + MapLibre + Cesium stack).  
- Any **RSC-enabled build pipeline**.  
- Any **SSR worker / edge-render process** (Node, edge runtimes, or equivalent).

#### 1.2 API gateways

- Asset-serving proxies that may handle flight payloads.  
- Flight-payload streaming endpoints (if enabled) or edge functions that parse RSC responses.

#### 1.3 Reproducibility environment

- Node-based deterministic builds.  
- Deployment bundles relying on **React 19.x** prior to the patched versions enumerated below.  

Even if a specific deployment does not use RSC explicitly, **transitive dependencies** or framework defaults may enable RSC-related paths. SBOMs and lockfiles must therefore be considered authoritative for exposure analysis.

---

## 🧱 Architecture

### 1. Required versions (enforced immediately)

All KFM-managed environments **must** use the following minimum versions or newer **patched** equivalents:

| Package              | Safe Minimum Version                          | Notes                                      |
|----------------------|-----------------------------------------------|--------------------------------------------|
| React                | **19.0.1+**, 19.1.2+, 19.2.1+                 | Mandatory; pin exact version per release   |
| `react-server-dom-*` | Matching patched set                          | Must be version-matched with React         |
| Next.js              | **15.0.5 / 15.1.9 / 15.2.6 / 15.3.6 / 15.4.8 / 15.5.7 / 16.0.7** | All KFM deployments must use one of these  |
| Turbopack RSC modules | Latest patched artifacts                     | Verified via SBOM and provenance           |

All version bumps must be committed with:

- Deterministic lockfiles (`package-lock.json`, `pnpm-lock.yaml`, etc.).  
- Build reproducibility attestations.  
- SBOM delta diffs highlighting React/Next.js-related changes.

### 2. Mitigation pipeline (mandatory sequence)

#### Step 1 — Immediate dependency pin & rebuild

- Update all React/Next.js/RSC-related packages to patched versions.  
- Freeze lockfiles and commit them.  
- Verify signatures + provenance using SLSA generators.  
- Regenerate SBOM and attach to the release manifest.

#### Step 2 — RSC attack surface reduction

KFM temporarily or permanently disables:

- Arbitrary server actions not explicitly declared and audited.  
- Undocumented server endpoints, especially those handling flight payloads.  
- Any non-declared RSC boundary (dynamic imports acting as RSC entrypoints).

All SSR workers must reject:

- Unknown or malformed flight payloads.  
- Non-signed or non-schema-conformant streams.  
- Cross-origin RSC frames and untrusted origins.

#### Step 3 — Traffic-level protection

The edge/WAF layer must enforce:

- Strict payload size and rate limits for RSC/flight endpoints.  
- Schema validation of flight payload format and headers.  
- WAF rules scoped to known React2Shell exploit signatures.  
- Canary/shadow deployments before promoting to production.

#### Step 4 — Runtime isolation

Frontend SSR workers must run under:

- Non-root users.  
- No filesystem write permission for application directories.  
- Syscall sandbox mode (seccomp or equivalent).  
- Deterministic CPU/memory resource caps to limit impact of exploit attempts.

#### Step 5 — Verification tests

Deterministic CI gates must execute:

- RSC flight-fuzzer tests designed around React2Shell payload variants.  
- Replay-based exploit regression suite using captured malicious patterns (sanitized).  
- SBOM dependency drift detector focused on React/Next.js stacks.  
- Build reproducibility validator to ensure patched vs. unpatched builds are distinguishable and traceable.

### 3. Frontend architecture adjustments

#### 3.1 Enforced separation

KFM permanently enforces:

- Explicit **RSC boundaries** separated from user-influenced data flows.  
- No dynamic eval/loader pathways that can turn data into code.  
- No inline server actions or ad-hoc API endpoints without governance-approved design docs.

#### 3.2 Directed dataflow model

The canonical pipeline becomes:

> **Client → Static Payload → Sandboxed Server Renderer → Typed Flight Response → Client**

Requirements:

- No untyped, unverified, or dynamic code paths permitted in the RSC data path.  
- Type-safe flight responses; validation must run before hydration on the client.  
- All deviations from this model must be documented and reviewed as exceptions.

---

## 🧪 Validation & CI/CD

React2Shell hardening is enforced via CI/CD:

- **Workflow policies**
  - All frontend builds must:
    - Run SBOM generation and diff checks for React/Next.js dependencies.  
    - Execute the React2Shell regression suite (flight fuzzing + replay tests).  
    - Fail builds if unsafe versions or unverified RSC modules are detected.  

- **Policy-as-code**
  - Security rules for React2Shell must be codified:
    - In repository-level policies (e.g., `policy/` under this directory).  
    - In CI configuration (e.g., reusable workflow templates).  

- **Attestations**
  - Each hardened release must produce:
    - SLSA-style provenance attestations referencing patched versions.  
    - Links from attestations to this bulletin (`doc_uuid`, `version`) as the policy baseline.

Any CI/CD pipeline that bypasses React2Shell checks is considered non-compliant.

---

## 📦 Data & Metadata

### 1. Telemetry & observability fields

For RSC/SSR-related traffic and builds, telemetry must emit at least:

- `flight.validation.status`  
- `rsc.payload.anomaly_score`  
- `waf.react2shell.block.count`  
- `sbom.revision.hash`  
- `build.determinism.pass`  
- `sandbox.violation.count`  

Daily rollups must feed into:

- The provenance ledger (as time-stamped events).  
- Security anomaly graph(s) for cluster-wide pattern detection.  
- Deployment reliability budgets (SLO/SLA monitoring).

### 2. Release artifacts

React2Shell hardening status must be expressible via:

- `sbom_ref` and `manifest_ref` in this document’s front matter.  
- Tagged releases that clearly identify:
  - Patched React/Next.js versions.  
  - Date/time of cutover.  
  - React2Shell hardening checks that were applied.

---

## 🌐 STAC, DCAT & PROV Alignment

Although React2Shell primarily targets the frontend runtime, the response is captured in KFM’s **provenance and catalog** ecosystem:

- **DCAT**
  - Security bulletins like this one can be modeled as `dcat:Dataset` or `dcat:CatalogRecord`:
    - `dct:title` = this document’s title.  
    - `dct:description` = summary of React2Shell mitigation.  
    - `dct:modified` = `last_updated`.  

- **PROV-O**
  - React2Shell patching activities are `prov:Activity` instances:
    - `prov:used` unpatched builds and vulnerability advisories.  
    - `prov:generated` hardened artifacts and deployments.  
    - Linked to this bulletin via `prov:wasInfluencedBy`.  

- **SBOM & provenance linkage**
  - SBOM entries for React/Next.js libraries must be linked to:
    - Vulnerability records (CVE IDs).  
    - Provenance events describing patching and redeployment.

This alignment ensures React2Shell is tracked not only as a one-off incident but as part of the long-term provenance chain.

---

## ⚖ FAIR+CARE & Governance

React2Shell is now a **permanent class** in KFM’s supply-chain threat model:

- **FAIR**
  - *Findable*: this bulletin and related audits are indexed under security docs and catalogs.  
  - *Accessible*: mitigation steps are available to all maintainers and derivative deployments.  
  - *Interoperable*: SBOMs, telemetry, and attestations are expressed in open formats.  
  - *Reusable*: hardening patterns (SSR isolation, RSC boundaries, WAF rules) can be reused across projects.  

- **CARE & responsibility**
  - While primarily technical, React2Shell hardening ensures:
    - Frontend compromise cannot silently corrupt Story Nodes or governance views.  
    - Data and narratives about Indigenous communities or sensitive sites are not exposed via compromised UI layers.  
  - Upgrades to React/Next.js must:
    - Pass an **RSC Safety Review**.  
    - Undergo a **Supply-Chain Diff Audit**.  
    - Obtain **Governance Council Approval** (Security + Frontend Risk Council).  

No uncontrolled React/Next.js upgrades are permitted in KFM after this bulletin.

---

## 🕰️ Version History

| Version | Date       | Status            | Summary                                       |
|--------:|------------|-------------------|-----------------------------------------------|
| v11.2.4 | 2025-12-05 | Active / Enforced | Initial governed React2Shell hardening bulletin. |

Future revisions must:

- Document new React/Next.js patches and any changes to required versions.  
- Update WAF rules, SBOM expectations, and test suites as the exploit class evolves.  
- Link to incident-specific audit documents when applicable.

---

<div align="center">

🛡️ **KFM v11.2.4 — React2Shell Emergency Hardening Playbook**  
Secure-by-Design · Provenance-Driven · Frontend Supply-Chain Hardened  

[📘 Docs Root](../../README.md) · [🔐 Security Index](../README.md) · [⚖ Governance](../../standards/governance/ROOT-GOVERNANCE.md)

</div>
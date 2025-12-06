---
title: "🛡️ KFM v11.2.4 — React2Shell Emergency Security Advisory (CVE-2025-55182) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/react2shell-advisory/README.md"
version: "v11.2.4"
last_updated: "2025-12-06"

release_stage: "Critical · Governed"
lifecycle: "Immediate Enforcement Only"
review_cycle: "Continuous · Security Board · Supply-Chain Oversight"
content_stability: "stable"
backward_compatibility: "N/A (hotpatch advisory)"
status: "Active / Enforced"

doc_kind: "Security Advisory"
intent: "react2shell-emergency-advisory"
role: "security-hotpatch-guidance"
header_profile: "standard"
footer_profile: "standard"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "releases/v11.2.4/sbom.spdx.json"
manifest_ref: "releases/v11.2.4/manifest.zip"
telemetry_ref: "releases/v11.2.4/security-telemetry.json"
telemetry_schema: "schemas/telemetry/security-advisory-v1.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-v2.json"

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Security Critical"
sensitivity: "Security Advisory (non-sensitive content; operationally critical)"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
classification: "Public Document"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
risk_category: "Security"
redaction_required: false

data_steward: "KFM Security Board"
ttl_policy: "Valid until superseded by later React2Shell or RSC transport advisories"
sunset_policy: "Superseded when upstream React/Next.js advisories and KFM security board retire this CVE"

ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "TechArticle"
  owl_time: "Instant"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/security/react2shell-advisory/README.md@v11.2.4"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: false
  must_reference_origin_root: true

json_schema_ref: "schemas/json/security-advisory-react2shell-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/security-advisory-react2shell-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"

doc_uuid: "urn:kfm:doc:security:react2shell-advisory:v11.2.4"
semantic_document_id: "kfm-security-react2shell-advisory-v11.2.4"
event_source_id: "ledger:kfm:doc:security:react2shell-advisory:v11.2.4"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-historical-claims"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🧭 Context"
    - "🧱 Architecture"
    - "📦 Data & Metadata"
    - "🧪 Validation & CI/CD"
    - "🗂️ Directory Layout"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"

diagram_profiles:
  - "mermaid-flowchart-v1"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "provenance-check"
  - "footer-check"
  - "accessibility-check"
  - "security-advisory-check"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Security-First × Supply-Chain Aware × FAIR+CARE Grounded"
  architecture: "Zero-Trust · Defense-in-Depth · Verified Provenance"
  analysis: "Evidence-Led · Incident-Ready · Governance-Aligned"
  data-spec: "SBOM-Backed · Telemetry-Driven · Open Mitigations"
  telemetry: "Transparent Alerts · Actionable Metrics · Safe Automation"
  graph: "Hardened Semantics · Protected Lineage · Controlled Access"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_version_history: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true

deprecated_fields: []
---

<div align="center">

# 🛡️ **React2Shell Crisis Advisory**  
### **CVE-2025-55182 · Remote Code Execution in React Server Components**  
### **Mandatory Mitigation for All KFM Deployments**

**Diamond⁹ Ω / Crown∞Ω Ultimate Certified**  
**Security Guidance · Zero-Latitude Tolerance**

</div>

---

## 📘 Overview

CVE-2025-55182 (“React2Shell”) is an unauthenticated **remote code execution (RCE)** vector within React Server Components’ Flight serialization channel.

A crafted request can induce execution of attacker-supplied payloads on servers running unpatched React RSC runtimes. Because the Kansas Frontier Matrix exposes components via API-first interfaces and real-time workers, any unpatched environment constitutes a **catastrophic ingress vector**.

This advisory defines:

- The **scope** of vulnerable stacks within KFM.  
- The **minimum patch levels** for React / Next.js / KFM internal RSC transport.  
- Mandatory **WAF and runtime guardrails**.  
- A **verification checklist** suitable for CI/CD and operational runbooks.

All environments **must** apply hotpatches and mitigations immediately.

---

## 🧭 Context

### Impact on the Kansas Frontier Matrix

The vulnerability affects systems that:

- Serve **React Server Components (RSC)** directly or via Next.js App Router.  
- Emit or transform **Flight responses** (Focus Mode v3 uses audited Flight nodes).  
- Use **edge workers**, **SSR nodes**, or **RSC-aware middleware**.

Within KFM, at-risk modules include (non-exhaustive):

| Module / Area              | Risk Level | Reason                                      |
|---------------------------|-----------|---------------------------------------------|
| `src/web/frontend`        | Severe    | Direct RSC execution surface                |
| `src/api/gateway/router`  | Severe    | Accepts user-controlled routing inputs      |
| Focus Mode v3 (RSC Bridge)| Critical  | Flight serialization transforms             |
| Story Node Renderer       | Moderate  | Indirect Flight channel dependencies        |
| Autonomous Pipelines UI   | Moderate  | RSC-based SSR rendering                     |

Any compromised SSR node can become a **remote command runner** capable of:

- Altering or exfiltrating datasets.  
- Corrupting lineage and provenance.  
- Poisoning models and autonomy decisions.  
- Escalating into graph / API / telemetry layers.

This is treated as a **Tier-0 emergency advisory**.

---

## 🧱 Architecture

### React / Next.js / RSC Baselines

#### React

All KFM deployments that use React Server Components **must** run a patched React version, one of:

- `19.0.1`  
- `19.1.2`  
- `19.2.1`

Any earlier version in an RSC context is considered **vulnerable**.

#### Next.js

All KFM deployments using Next.js App Router / RSC must run a patched Next.js release that:

- Includes the upstream React2Shell mitigation.  
- Ships a corrected Flight transport implementation.  
- Enforces stricter validation on RSC payloads.

Patch level should be recorded in:

- Deployment manifests.  
- SBOM (`releases/v11.2.4/sbom.spdx.json`).  
- Security telemetry tags.

#### KFM Internal RSC Runtime

The KFM patchset `kfm-rsc-transport-hotfix-1` is **mandatory** wherever KFM runs custom RSC bridges or Flight handlers. The hotfix:

- Hardens Flight transforms (strict schema checks, size limits).  
- Adds deterministic parser validation and rejection paths.  
- Enforces content-based execution guards (no dynamic `eval`, blocked dangerous patterns).  
- Integrates with the **write-ahead log (WAL)** so malformed segments are rejected and auditable without corrupting state.

### Ingress and Zero-Trust Controls

Until this advisory is superseded:

- All RSC / SSR endpoints must be treated as **high-risk ingress**.  
- Only authenticated and signed requests are allowed on SSR paths used by KFM internal operators.  
- Anonymous POSTs to RSC endpoints are **disallowed**.  
- Data promotion flows (`raw → work → processed`) involving RSC-driven actions must respect **immutability locks** during hotpatch windows.

---

## 📦 Data & Metadata

### Telemetry & Metrics

Security telemetry for this advisory is emitted into:

- `releases/v11.2.4/security-telemetry.json`  
- Structures defined in `schemas/telemetry/security-advisory-v1.json`

Recommended metrics:

- `security.react2shell.blocked_attempts` — count of WAF-blocked exploit signatures.  
- `security.react2shell.patched_nodes` — number of nodes reporting patched React / Next.js baseline.  
- `security.react2shell.unpatched_nodes` — number of nodes still reporting vulnerable versions.  
- `security.react2shell.hotfix_version` — deployed `kfm-rsc-transport-hotfix-*` version.  

These metrics should be:

- Aggregated per environment (`dev`, `staging`, `prod`).  
- Exported to dashboards used by the Security Board and Ops teams.  
- Logged with timestamps and node identifiers (or anonymized tags where required).

### SBOM and Manifest Integration

SBOM and release manifest must:

- List patched React and Next.js packages with exact versions and hashes.  
- Include the hotfix and WAF profile as explicit components or configuration assets.  
- Reference this advisory (`kfm-security-react2shell-advisory-v11.2.4`) by ID and version.

---

## 🧪 Validation & CI/CD

### Required Patch Levels

To be considered compliant:

- **React** — version must be ≥ the patched baseline (`19.0.1`, `19.1.2`, or `19.2.1`).  
- **Next.js** — must match known patched versions for React2Shell.  
- **KFM RSC Runtime** — `kfm-rsc-transport-hotfix-1` (or later superseding hotfix) installed and enabled.

### Mandatory Mitigations

#### 1. WAF Guardrails

All deployments must enable the KFM-provided WAF profile:

~~~text
waf/profiles/react2shell-blocklist-v1.yaml
~~~

Requirements:

- Active on HTTP/1.1 and HTTP/2 (including server push streams, if enabled).  
- Monitored via `security.react2shell.blocked_attempts`.  
- Configured to **block**, not just log, suspicious RSC payload patterns.

#### 2. Runtime Containment

At the runtime level:

- Enable strict-mode RSC execution.  
- Disable or sandbox `eval` and other dynamic code injection paths.  
- Enforce deterministic serializer and deserializer checks for Flight payloads.  
- Require provenance enforcement on all incoming RSC segments (e.g., signed origin metadata).

#### 3. Zero-Trust Ingress

Until revocation is announced:

- Disallow **all anonymous POSTs** to RSC endpoints.  
- Require **signed requests** or equivalent strong auth on SSR paths used by KFM tools.  
- Apply temporary **immutability locks** on `data/processed/*` during hotpatch windows so compromised SSR nodes cannot silently rewrite critical products.

### Verification Checklist

To be compliant with this advisory, an environment must pass **all** of the following:

- [ ] React version ≥ patched baseline (19.0.1 / 19.1.2 / 19.2.1)  
- [ ] Next.js upgraded to a React2Shell-patched release  
- [ ] `kfm-rsc-transport-hotfix-1` (or newer) applied and verified  
- [ ] WAF profile `react2shell-blocklist-v1.yaml` installed and enforced  
- [ ] Telemetry reporting `security.react2shell.blocked_attempts` per environment  
- [ ] Replay audit of last 7 days of API / SSR logs for anomalous RSC payloads  
- [ ] Immutable dataset lock active for critical processed datasets during patch window  
- [ ] Graph hardening guard `graph.rsc-inject` configured to `DENY` for untrusted payloads  

Where possible, wire this checklist into CI:

- Deployment pipelines fail if version checks or configuration checks fail.  
- Post-deploy verification scripts confirm WAF and telemetry configuration.

---

## 🗂️ Directory Layout

### Advisory-Related Files (ASCII-safe)

~~~text
docs/
  security/
    react2shell-advisory/
      README.md                # This file

schemas/
  telemetry/
    security-advisory-v1.json  # Telemetry schema for security advisories

releases/
  v11.2.4/
    sbom.spdx.json
    manifest.zip
    security-telemetry.json

waf/
  profiles/
    react2shell-blocklist-v1.yaml
~~~

Rules:

- `README.md` is the canonical advisory; no other file may redefine its mandatory patch levels.  
- Telemetry schema and WAF profile paths must remain stable across the lifetime of this advisory or be clearly versioned if changed.  
- Any additional per-environment runbooks or IR docs should **reference** this file, not fork its content.

---

## ⚖ FAIR+CARE & Governance

Although CVE-2025-55182 is a **technical vulnerability**, failure to mitigate it has direct FAIR+CARE implications:

- **Integrity** — Unpatched RSC nodes can corrupt datasets, lineage, and Story Nodes, undermining Reusability and trust.  
- **Sovereignty** — Compromise of systems holding heritage or Indigenous data could violate sovereignty and CARE commitments.  
- **Transparency** — SBOM, telemetry, and this advisory ensure that patch status is auditable and explainable.

Governance responsibilities:

- The **KFM Security Board** owns this advisory and any subsequent updates.  
- The **FAIR+CARE Council** and **data stewards** must be informed of any suspected compromise involving sensitive datasets.  
- Incident response procedures in `docs/security/incident-response.md` apply; this advisory does not replace IR playbooks, but augments them.

---

## 🕰️ Version History

| Version   | Date       | Notes                                                                                 |
|----------:|------------|---------------------------------------------------------------------------------------|
| **v11.2.4** | 2025-12-06 | Initial emergency React2Shell advisory for CVE-2025-55182 aligned with KFM-MDP v11.2.4; defines patch baselines, WAF profile, telemetry, and zero-trust ingress requirements. |

---

<div align="center">

🛡️ **Kansas Frontier Matrix · Security Standards Division**  
Diamond⁹ Ω / Crown∞Ω Ultimate Certification Chain  

[⚖ Governance](docs/standards/governance/ROOT-GOVERNANCE.md) ·  
[📦 SBOM](releases/v11.2.4/sbom.spdx.json) ·  
[📊 Security Telemetry](releases/v11.2.4/security-telemetry.json)

</div>
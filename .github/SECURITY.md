---
title: "🛡️ Kansas Frontier Matrix — Security Policy & Vulnerability Disclosure (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: ".github/SECURITY.md"
version: "v11.0.0"
last_updated: "2025-11-18"

review_cycle: "Annual / Autonomous · FAIR+CARE Council Oversight"

commit_sha: "<latest-commit-hash>"

sbom_ref: "../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../releases/v11.0.0/manifest.zip"
telemetry_ref: "../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../schemas/telemetry/security-policy-v1.json"

governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"

status: "Active / Enforced"
doc_kind: "SecurityPolicy"
intent: "security-and-disclosure"
role: "security-policy"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Security"
redaction_required: false

provenance_chain:
  - ".github/SECURITY.md@v10.0.0"

previous_version_hash: "<previous-sha256>"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "CreativeWork"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../schemas/json/security-policy-v11.schema.json"
shape_schema_ref: "../schemas/shacl/security-policy-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:security-policy-v11.0.0"
semantic_document_id: "kfm-security-policy"
event_source_id: "ledger:.github/SECURITY.md"
immutability_status: "mutable-plan"
doc_integrity_checksum: "<sha256>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified historical claims"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "United States / Kansas"
classification: "Public Document"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next security-policy update"
---

<div align="center">

# 🛡️ **Kansas Frontier Matrix — Security Policy & Vulnerability Disclosure**  
`.github/SECURITY.md`

**Purpose**  
Define how the Kansas Frontier Matrix (KFM) community reports and handles security issues, supply-chain risks, and privacy concerns — in alignment with **MCP-DL v6.3**, **KFM-MDP v11.0.0**, **FAIR+CARE**, and **Diamond⁹ Ω / Crown∞Ω** governance.

</div>

--- ✦ ---

## 📘 Scope

This policy applies to:

- All code, configurations, and workflows in the **Kansas Frontier Matrix** repository  
- CI/CD infrastructure defined under `.github/`  
- Scripts and tools under `src/`, `web/`, `tools/`, and `data/` that could impact security  
- The handling and representation of **data** (especially sensitive and governed datasets)  

This policy does **not** grant permission to attack infrastructure outside of this repository or associated demo environments.

--- ✦ ---

## 📮 Reporting a Vulnerability

If you believe you have found a security or privacy issue:

1. **Do not** open a public GitHub issue with sensitive details.  
2. Contact the maintainers via the designated private channel (for example, GitHub Security Advisory or a listed email in the repo profile).  
3. Provide the following information:
   - A clear description of the issue  
   - Steps to reproduce  
   - Affected components (paths, services, datasets)  
   - Impact assessment (what could an attacker do?)  
   - Any suggested mitigations  

We will:

- Acknowledge receipt as soon as reasonably possible  
- Triage and validate the issue  
- Coordinate on a fix and an appropriate disclosure timeline  
- Credit researchers, if desired and consistent with privacy and safety

> Do **not** attempt to access data you are not authorized to access, exploit the issue in production, or pivot to third-party systems.

--- ✦ ---

## 🔐 Security Principles

KFM follows these core security principles:

1. **Least Privilege** — CI/CD, scripts, and services are given the minimum access required.  
2. **Defense in Depth** — multiple layers: code validation, CI checks, dependency scanning, and manual review.  
3. **Secure Defaults** — conservative defaults for access, logging, and network use.  
    4. **No Secrets in Repo** — secrets must never be committed; use GitHub secrets / OIDC / key management systems.  
5. **Privacy by Design** — avoid ingesting or exposing PII; anonymize and aggregate where possible.  
6. **Transparency** — security fixes are documented in release notes and, when safe, in issues or advisories.

--- ✦ ---

## 🧱 Threat Model (High-Level)

KFM is primarily concerned with:

- **Supply-chain risks**  
  - Compromised dependencies (npm/pip)  
  - Malicious GitHub Actions or workflow steps  
  - Tampered SBOM or manifest files  

- **Data integrity & provenance**  
  - Unauthorized modification of datasets or STAC/DCAT metadata  
  - Corruption of knowledge-graph content  
  - Inaccurate or malicious Story Node narratives  

- **CI/CD pipeline misuse**  
  - Unauthorized changes to workflows  
  - Use of CI runners to exfiltrate secrets or data  
  - Abuse of automation to publish unsafe artifacts  

- **Privacy & ethical risks**  
  - Exposure of sensitive location data (e.g., heritage sites)  
  - Inadvertent inclusion of PII in datasets or logs  

--- ✦ ---

## 🔒 Protections in Place

### 1. Repository Protections

- Protected `main` and `release/*` branches  
- Required status checks for critical CI workflows  
- Required reviews for changes in:
  - `.github/**`
  - `schemas/**`
  - `src/graph/**`
  - `data/**` and STAC/DCAT catalogs  

### 2. Dependency & Supply Chain Security

- **Dependabot** for:
  - `github-actions`  
  - `npm` (`/web`, root)  
  - `pip` (root and `/tools`)  
- SBOM generation and verification (`sbom.spdx.json`) per release  
- Vulnerability scanning via:
  - `codeql.yml` for static code analysis  
  - `trivy.yml` (or equivalent) for CVE scanning of images/lockfiles  

### 3. CI/CD Integrity

- No plaintext secrets or tokens in workflow files  
- Use of GitHub Secrets and/or OIDC-based authentication  
- Restricted permissions for GitHub Actions tokens  
- Peer review required for changes to workflows and security policy

--- ✦ ---

## 🧠 AI & Focus Mode Safeguards

While not traditional “security” in the cyber sense, AI misuse can cause **informational harm**:

- AI-powered narratives must be grounded in actual data and sources  
- No speculative or fabricated events or attributions  
- No generation of targeted or sensitive information about real individuals  
- Internal guardrails and validators check:
  - Grounding of answers  
  - Exclusion of prohibited data categories  
  - Explicit labeling of limitations  

Potential AI-related concerns should be reported through the same security channel if they result in **harmful outputs, leakage of sensitive information, or governance violations**.

--- ✦ ---

## 📊 Logging, Telemetry & Privacy

KFM aims for **useful observability** without compromising privacy:

- CI logs capture:
  - Build results  
  - Test and validation outcomes  
  - Workflow metadata (IDs, durations)  

- CI logs intentionally avoid:
  - Secrets  
  - Sensitive dataset contents  
  - PII  

Telemetry:

- Aggregated into `releases/<version>/focus-telemetry.json`  
- Used to monitor:
  - Reliability and performance  
  - FAIR+CARE validation rates  
  - Security and validation failures  

Telemetry is **not** used to track individuals.

--- ✦ ---

## 🧩 Responsible Use of Data

Certain datasets may involve:

- Cultural heritage sites  
- Archaeological locations  
- Indigenous lands and histories  
- Sensitive ecological data (e.g., endangered species locations)  

For these, security is also ethical:

- Coordinates may be generalized (e.g., via H3)  
- Sensitive detail may be omitted from public graphs and STAC catalogs  
- Access may be limited or fully withheld in public builds  

If you notice that data appears to violate these constraints, please report it as a **security/ethics issue**.

--- ✦ ---

## 🚨 When We Issue Advisories

We may publish:

- GitHub Security Advisories  
- Release notes with security sections  
- Documentation updates reflecting mitigation or policy changes  

Advisories are appropriate when:

- A vulnerability has realistic exploitation potential  
- Fixes or mitigations are available  
- Transparency does not materially increase risk  

--- ✦ ---

## 🧭 Maintainer Responsibilities

Maintainers are expected to:

- Follow this policy when responding to reports  
- Treat reporters with respect, and maintain confidentiality where requested and appropriate  
- Avoid downplaying issues; if in doubt, triage thoroughly  
- Ensure fixes are reviewed and pass:
  - CI/CD workflows  
  - FAIR+CARE validation  
  - Security scans  
  - Documentation requirements  

Whenever feasible, maintainers should also add **regression tests** or validations to prevent reintroduction.

--- ✦ ---

## 🕰️ Version History

| Version  | Date         | Author            | Summary                                           |
|---------:|-------------:|------------------|---------------------------------------------------|
| v11.0.0  | 2025-11-18   | KFM Core Team     | Upgraded to KFM-MDP v11; expanded threat model and AI safeguards. |
| v10.0.0  | 2025-??-??   | KFM Core Team     | Initial SECURITY.md, basic disclosure and policy. |

--- ✦ ---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT**  
Governed under **Master Coder Protocol v6.3** and **KFM-MDP v11.0.0**  
FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to GitHub Overview](README.md) · [CI/CD Architecture](ARCHITECTURE.md) · [Governance Charter](../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
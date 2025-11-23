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

---

# 📘 Scope

This policy applies to:

- All code, configurations, and workflows in the **Kansas Frontier Matrix** repository  
- CI/CD infrastructure defined under `.github/`  
- Scripts and tools under `src/`, `web/`, `tools/`, and `data/` that could impact security  
- The handling and representation of **data** (especially sensitive and governed datasets)  

This policy does **not** grant permission to attack infrastructure outside of:

- This repository  
- Official demo or test environments explicitly provided by the project  

---

# 🗂 Repository Security Context

```text
Kansas-Frontier-Matrix/
│
├── .github/                               # GitHub config, CI/CD, security configuration
│   ├── SECURITY.md                        # This security policy & vulnerability disclosure document
│   ├── workflows/                         # CI/CD workflows (lint, tests, scans, governance)
│   └── ISSUE_TEMPLATE/                    # Issue and security-report templates
│
├── releases/                              # Release artifacts
│   ├── v11.0.0/
│   │   ├── sbom.spdx.json                 # Software Bill of Materials (SBOM)
│   │   ├── manifest.zip                   # Release manifest
│   │   └── focus-telemetry.json           # Telemetry (including security-related metrics)
│   └── ...                                # Other versions
│
├── schemas/                               # Schemas for security-related telemetry and governance
│   ├── telemetry/
│   │   └── security-policy-v1.json        # Telemetry schema used by this SECURITY policy
│   └── ...                                # Additional schemas (energy, carbon, lineage, etc.)
│
└── docs/                                  # Governance and standards
    └── standards/
        └── governance/
            └── ROOT-GOVERNANCE.md         # Global governance charter referenced by this policy
````

---

# 📮 Reporting a Vulnerability

If you believe you have found a security or privacy issue:

1. **Do not** open a public GitHub issue containing sensitive details.
2. Use one of the following private channels (example patterns; check repo profile for the active ones):

   * GitHub Security Advisory workflow
   * A dedicated security email (e.g., `security@<project-domain>`)
3. Provide as much detail as you can:

   * A clear description of the issue
   * Steps to reproduce
   * Affected components (paths, services, datasets)
   * Impact assessment (what an attacker could do)
   * Any suggested mitigations or workarounds

We will:

* Acknowledge receipt as soon as reasonably possible
* Triage and validate the issue
* Coordinate on a fix and appropriate disclosure timeline
* Credit researchers, if desired and consistent with privacy and safety

> Please **do not** attempt to:
>
> * Access data you are not authorized to view
> * Exploit the issue in production environments
> * Pivot to third-party systems or infrastructure

---

# 🔐 Security Principles

KFM follows these core security principles:

1. **Least Privilege**
   CI/CD, scripts, and services are granted the minimum access needed to function.

2. **Defense in Depth**
   Multiple layers of controls: code validation, CI checks, dependency scanning, and manual review.

3. **Secure Defaults**
   Conservative defaults for access, logging, network egress, and feature flags.

4. **No Secrets in Repo**
   Secrets must never be committed. Use:

   * GitHub Secrets
   * OIDC-based federation
   * External secret managers (e.g., AWS/GCP secret stores)

5. **Privacy by Design**
   KFM avoids ingesting or exposing PII whenever possible; anonymization and aggregation are preferred when context allows.

6. **Transparency**
   Security fixes are documented in:

   * Release notes
   * Security advisories (when appropriate)
   * Standards or policy documentation (e.g., this file)

---

# 🧱 Threat Model (High-Level)

KFM’s primary security concerns include:

## 1. Supply-Chain Risks

* Compromised or malicious dependencies (npm, pip, system packages)
* Malicious or misconfigured GitHub Actions
* Tampered SBOM or manifest files

## 2. Data Integrity & Provenance

* Unauthorized modification of datasets or STAC/DCAT metadata
* Corruption or injection attacks on the knowledge graph (Neo4j)
* Inaccurate or malicious Story Node or Focus Mode narratives

## 3. CI/CD Pipeline Misuse

* Unauthorized changes to workflows under `.github/workflows/`
* Abuse of CI runners to exfiltrate secrets or sensitive data
* Use of pipeline automation to publish unsafe or unvalidated artifacts

## 4. Privacy & Ethical Risks

* Exposure of sensitive location data (e.g., cultural heritage sites, sacred places)
* Inadvertent inclusion of PII/PHI in datasets or logs
* Narrative harms (e.g., AI content that misrepresents communities or events)

---

# 🔒 Protections in Place

## 1. Repository Protections

* Protected `main` and `release/*` branches
* Required status checks for critical CI workflows
* Required code review for changes to:

  * `.github/**`
  * `schemas/**`
  * `src/graph/**`
  * `data/**` and STAC/DCAT catalogs

## 2. Dependency & Supply-Chain Security

* **Dependabot** is configured for:

  * `github-actions`
  * `npm` (frontend + root)
  * `pip` (backend + tools)

* **SBOM**:

  * `releases/<version>/sbom.spdx.json` generated per release
  * SBOM verification as part of release validation

* Vulnerability scanning:

  * `codeql` for language-level static analysis
  * Container/image and lockfile scanning (e.g., `trivy` or equivalent)

## 3. CI/CD Integrity

* No plaintext secrets or tokens inside workflow files
* Use of:

  * GitHub Secrets
  * OIDC-based identity with cloud providers
* Restrictive permissions on `GITHUB_TOKEN` and ephemeral credentials
* Peer review and governance review required for:

  * Workflow changes
  * Security policy changes

---

# 🧠 AI & Focus Mode Safeguards

While not a traditional cyber vulnerability, harmful AI outputs are treated as **security & ethics concerns** in KFM:

* AI-generated narratives must be grounded in actual data and graph facts
* No fabrication of events, people, or causal links
* No targeted or sensitive profiling of real individuals
* Narrative and QA layers include:

  * Grounding checks against KG entities
  * Prohibited-topic filters
  * CARE and sovereignty-aware constraints

You should report AI safety issues (e.g., harmful or leaking content) through the same security channel, especially if:

* They reveal sensitive locations or private data
* They misrepresent communities in harmful ways
* They violate FAIR+CARE or KFM governance policies

---

# 📊 Logging, Telemetry & Privacy

KFM aims for **high observability** without compromising privacy.

## Logging

CI and runtime logs contain:

* Build/test outcomes
* Validation results
* Pipeline identifiers and timing

Logs are designed **not** to include:

* Secrets
* PII/PHI
* Sensitive raw dataset contents

## Telemetry

Metrics, including some security-related events, are aggregated into:

```text
releases/<version>/focus-telemetry.json
```

Telemetry is used to monitor:

* Reliability and performance
* FAIR+CARE validation outcomes
* Security-related validation failures

Telemetry is **not** used to track individual users.

---

# 🧩 Responsible Use of Data

Certain KFM datasets involve:

* Cultural heritage sites
* Archaeological data
* Indigenous lands and histories
* Sensitive ecological information (e.g., endangered species locations)

For these:

* Coordinates may be generalized (e.g., via H3 masking)
* Sensitive detail may be omitted from public graphs and catalogs
* Access to detailed data may be limited or withheld entirely

If you notice data that appears to violate these constraints, please report it as a **security and ethics issue**.

---

# 🚨 Security Advisories & Disclosure

We may publish:

* GitHub Security Advisories
* Release notes with dedicated **Security** sections
* Updates to this SECURITY policy

Advisories are appropriate when:

* A vulnerability has realistic exploitation potential
* Fixes or mitigations are available
* Public disclosure does not significantly increase risk

We strive for **coordinated vulnerability disclosure** with reporters.

---

# 🧭 Maintainer Responsibilities

Maintainers are expected to:

* Follow this policy when responding to reports
* Treat reporters with respect and maintain confidentiality when requested and appropriate
* Avoid downplaying issues; triage thoroughly and conservatively
* Ensure that fixes:

  * Are properly reviewed
  * Pass CI, tests, and governance checks
  * Include regression tests or validations where applicable

When security issues intersect with FAIR+CARE or sovereignty concerns, maintainers must also coordinate with the **FAIR+CARE Council** and relevant community stewards.

---

# 🕰 Version History

| Version |       Date | Author        | Summary                                                                            |
| ------: | ---------: | ------------- | ---------------------------------------------------------------------------------- |
| v11.0.0 | 2025-11-18 | KFM Core Team | Upgraded to KFM-MDP v11; expanded threat model, AI safeguards, and CI integration. |
| v10.0.0 | 2025-??-?? | KFM Core Team | Initial SECURITY.md, basic disclosure and repository protections.                  |

---

[Root README](../README.md) · [Architecture](../ARCHITECTURE.md) · [Governance Charter](../docs/standards/governance/ROOT-GOVERNANCE.md)

```

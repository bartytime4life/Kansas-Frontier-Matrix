---
title: "🛡️ Kansas Frontier Matrix — Security Policy & Vulnerability Disclosure (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: ".github/SECURITY.md"
version: "v11.2.3"
last_updated: "2025-12-08"
review_cycle: "Annual · FAIR+CARE Security Council · Architecture Board"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../releases/v11.2.3/manifest.zip"
telemetry_ref: "../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../schemas/telemetry/security-policy-v1.json"
energy_schema: "../schemas/telemetry/energy-v2.json"
carbon_schema: "../schemas/telemetry/carbon-v2.json"

governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.5"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

status: "Active / Enforced"
doc_kind: "SecurityPolicy"
intent: "security-and-disclosure"
category: "Security · Governance · Supply Chain · Responsible Disclosure"

fair_category: "F1-A1-I1-R1"
care_label: "Collective Benefit · Authority to Control · Responsibility · Ethics"
sensitivity_level: "Low"
public_exposure_risk: "Low"
risk_category: "Security"
indigenous_rights_flag: false
redaction_required: false
data_steward: "KFM FAIR+CARE Security Council"

provenance_chain:
  - ".github/SECURITY.md@v10.0.0"
  - ".github/SECURITY.md@v11.0.0"
  - ".github/SECURITY.md@v11.2.2"
  - ".github/SECURITY.md@v11.2.3"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "CreativeWork"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../schemas/json/security-policy-v11.schema.json"
shape_schema_ref: "../schemas/shacl/security-policy-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:security-policy-v11.2.3"
semantic_document_id: "kfm-security-policy"
event_source_id: "ledger:.github/SECURITY.md"
immutability_status: "mutable-plan"
machine_extractable: true

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative-additions"
  - "governance-override"
  - "unverified historical claims"

accessibility_compliance: "WCAG 2.1 AA+"
classification: "Public Document"
jurisdiction: "United States / Kansas"
lifecycle_stage: "stable"
ttl_policy: "12 months"
sunset_policy: "Superseded upon next security-policy update"

prov_profile: "PROV-O Plan + KFM Governance Extensions"
openlineage_profile: "OpenLineage v2.5 · CI/CD and AI pipeline events"
---

<div align="center">

# 🛡️ **Kansas Frontier Matrix — Security Policy & Vulnerability Disclosure**  
`.github/SECURITY.md`

**Purpose**  
Provide a clear, governed, and FAIR+CARE-aligned process for handling **vulnerabilities, supply-chain risks, incident response, and ethical security concerns** across the Kansas Frontier Matrix (KFM) ecosystem.

[![Security Governance](https://img.shields.io/badge/Security-Governed-brightgreen)]() ·  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-orange)]() ·  
[![SBOM](https://img.shields.io/badge/SBOM-SPDX_2.3-blue)]()  

</div>

---

## 📘 Overview

This policy defines how KFM manages:

- Security vulnerabilities and incident reports  
- Supply-chain and dependency risks  
- Data integrity and provenance threats  
- Privacy, FAIR+CARE, and sovereignty-sensitive risks  
- AI, Story Node, and Focus Mode v3 narrative safety issues  

It is enforced via:

- **KFM-MDP v11.2.5** (Markdown & documentation rules)  
- FAIR+CARE governance and sovereignty policies  
- CI/CD gating and CODEOWNERS review  
- SBOM + manifest verification  
- Schema/ontology validation (KFM-STAC/DCAT/JSON-LD/PROV-O)  
- OpenLineage + PROV-O provenance checks  

This file is the **public-facing entry point**. Deeper standards live in `docs/security/`.

---

## 🗂️ Repository Security Context

```text
Kansas-Frontier-Matrix/
├── 🛡️ .github/                          # GitHub configuration, CI/CD, security policy
│   ├── 🛡️ SECURITY.md                   # ← Public security & disclosure policy (this file)
│   ├── 🤖 actions/                      # Composite CI actions (schema-lint, worm-defense, etc.)
│   └── 🤖 workflows/                    # CI pipelines (lint, tests, scans, provenance, FAIR+CARE)
│
├── 📚 docs/
│   └── 🔒 security/                     # Full security & supply-chain governance framework
│       ├── 📄 README.md                 # Security & supply chain governance index
│       ├── 📄 threat-model.md           # STRIDE/LINDDUN threat modeling
│       ├── 📄 secrets-policy.md         # Secret lifecycle, encryption, rotation
│       ├── 📄 supply-chain.md           # SBOM, SLSA, signing, provenance
│       ├── 📄 vulnerability-management.md # CVE scanning, triage, patch SLAs
│       ├── 📄 incident-response.md      # Incident lifecycle & postmortems
│       └── 📂 supply-chain/
│           ├── 📄 README.md             # NPM worm defense & supply-chain sub-framework
│           └── 📂 npm-ignore-scripts/   # Lifecycle-script suppression standards
│
└── 📦 releases/<version>/               # Versioned artifacts & telemetry
    ├── 🧾 sbom.spdx.json               # SPDX SBOM
    ├── 📜 manifest.zip                 # Release manifest
    └── 📊 focus-telemetry.json         # Telemetry (incl. security & governance metrics)
```

The documents under `docs/security/` are **normative** and referenced by this policy.

---

## 📮 Reporting a Vulnerability

**Please do not disclose security issues publicly.**

Use one of these private channels:

1. **GitHub Security Advisory** (preferred)  
2. **Security contact email**: `security@<domain>` (if listed in the repo profile)

When reporting, include:

- Clear description of the issue  
- Impact and severity (if known)  
- Steps to reproduce (PoC if possible)  
- Affected components (paths, services, or workflows)  
- Any suggested mitigations or additional context  

### Maintainer Response

KFM maintainers will:

- Acknowledge receipt promptly  
- Validate the issue and assign severity  
- Coordinate mitigation and patch development  
- Create regression tests where appropriate  
- Publish a security advisory and changelog entry once a fix is available  
- Credit researchers when safe and permitted (opt-in)  

**Do NOT:**

- Attack production systems or unrelated infrastructure  
- Attempt privilege escalation beyond proof-of-concept needs  
- Access or attempt to access data you are not authorized to see  
- Exfiltrate or share sensitive cultural, personal, or sovereign data  

---

## 🔐 Core Security Principles

1. **Least Privilege**  
   CI workflows, services, and human accounts operate with minimal required permissions.

2. **Defense in Depth**  
   Multiple layers of protection: schemas → static analysis → CI gating → SBOM/SLSA → runtime monitoring.

3. **Secure Defaults**  
   Conservative permissions on Actions tokens, locked-down branches, and mandatory review for sensitive areas.

4. **Zero Secrets in Repo**  
   No secrets in committed code or configuration. Use GitHub Secrets, cloud KMS/Vault, or equivalent secure stores.

5. **Privacy & Sovereignty by Design**  
   Avoid PII; apply masking, aggregation, and H3 generalization to sensitive geographies and heritage data in accordance with FAIR+CARE and sovereignty policies.

6. **AI & Narrative Safety**  
   Story Nodes and Focus Mode narratives must be grounded in real data, avoid fabrication, and respect community and sovereignty constraints.

---

## 🔎 Threat Model Alignment

KFM’s security program is designed around:

- **STRIDE** — spoofing, tampering, repudiation, information disclosure, denial of service, elevation of privilege.  
- **LINDDUN** — privacy threats (linkability, identifiability, non-repudiation, detectability, disclosure, content unawareness, policy non-compliance).  
- **FAIR+CARE** — community and cultural impact framework for data and narratives.

Detailed threat models: `docs/security/threat-model.md`.

---

## 🔗 Supply-Chain & Dependency Integrity

KFM enforces strict supply-chain controls, as specified in `docs/security/supply-chain.md` and related docs:

- **SBOMs**  
  - SPDX 2.3 and, where applicable, CycloneDX SBOMs for releases.  

- **Provenance & Signing**  
  - SLSA-style provenance attestations.  
  - Cosign/Sigstore signatures and checksums for release artifacts.  

- **Scanning & Policy**  
  - Automated scanning with tools such as osv-scanner, Grype, and Trivy.  
  - Dependency-confusion and registry anomaly detection (`docs/security/supply-chain/dependency-confusion/`).  
  - NPM worm-defense (lifecycle-script suppression + anomaly rules) via `docs/security/supply-chain/npm-ignore-scripts/`.  

Artifacts that fail integrity, signature, or policy checks **cannot be promoted to release**.

---

## 🧪 Vulnerability Management (SLAs)

KFM uses a CVSS-inspired severity model with the following **target SLAs**:

| Severity | Detection SLA | Patch SLA  | Notes                   |
|--------: |--------------:|-----------:|-------------------------|
| Critical | 4 hours        | 24 hours   | Blocks CI/CD & releases |
| High     | 24 hours       | 72 hours   | Requires expedited fix  |
| Medium   | 48 hours       | 7 days     | Logged & monitored      |
| Low      | Weekly sweep   | Next sprint | Best-effort remediation |

The full vulnerability-management standard, including exception processes and scoring notes, is in:

- `docs/security/vulnerability-management.md`

---

## 🚨 Incident Response

KFM follows a NIST 800-61–inspired lifecycle:

1. **Detection** — alerts, telemetry, reports  
2. **Analysis** — confirm, scope, and classify the incident  
3. **Containment** — stop further impact  
4. **Eradication** — remove root cause  
5. **Recovery** — restore systems and validate integrity  
6. **Postmortem** — MCP-formatted analysis and follow-up actions  

Incident reports and postmortems live under:

```text
docs/security/reports/incident-response/
```

Security incidents may also trigger:

- Updates to `docs/security/` standards  
- SBOM and manifest regeneration  
- Governance ledger entries and FAIR+CARE review  

---

## 🧠 AI, Story Nodes & Focus Mode Safety

AI-driven capabilities (Story Nodes & Focus Mode v3) are treated as part of the **attack surface**.

KFM requires that:

- AI outputs are grounded in graph-backed facts and approved datasets.  
- Narratives do not fabricate historical events, individuals, or attributions.  
- Indigenous and culturally sensitive narratives follow sovereignty policies and FAIR+CARE guidance.  
- Protected site coordinates and sensitive locations are generalized or suppressed.  
- Prompting and model behavior are monitored for harmful or biased patterns.  

If you observe dangerous or misleading AI behavior (e.g., leaking sensitive coordinates, fabricating events, or generating harmful narratives), report it using the same channels as other vulnerabilities and label the report **“AI / Narrative Safety”**.

---

## 📊 Telemetry, Logging & Sustainability

Security-related telemetry contributes to:

```text
releases/<version>/focus-telemetry.json
```

This telemetry may include:

- Security workflow outcomes (pass/fail and severity signals)  
- Governance and FAIR+CARE checks  
- SBOM and provenance verification status  
- Energy and carbon metrics related to security and scanning workloads  

Telemetry **never** contains:

- Secrets or credentials  
- PII or PHI  
- Precise coordinates of protected heritage or sensitive sites  
- Non-governed or raw incident data  

Telemetry schemas:

- `schemas/telemetry/security-policy-v1.json`  
- `schemas/telemetry/energy-v2.json`  
- `schemas/telemetry/carbon-v2.json`  

---

## 🧩 Responsible Use of Sensitive Data

Certain datasets require **heightened protection**:

- Archaeological and cultural heritage sites  
- Indigenous lands and sacred locations  
- Sensitive ecology and endangered species habitats  
- Any data flagged with sovereignty or high CARE sensitivity  

Controls include:

- H3-based spatial generalization and masking  
- Removal of exact coordinates and identifiers from public releases  
- Additional FAIR+CARE Council review before publishing new or modified layers  
- Documented licensing and data-sharing agreements  

Security reports involving these domains are jointly handled by:

- Security maintainers  
- FAIR+CARE Council  
- Relevant sovereignty stewards and domain experts  

---

## 🧭 Maintainer Responsibilities

Maintainers are responsible for:

- Monitoring private reporting channels and triaging reports promptly  
- Respecting the confidentiality of reporters and affected communities  
- Applying fixes consistently across affected branches/environments  
- Ensuring regression tests, validators, and CI rules are updated as needed  
- Updating SBOMs, manifests, incident-response logs, and telemetry to reflect changes  
- Coordinating with governance bodies (Security Council, FAIR+CARE, Architecture Board) when risk intersects ethics, sovereignty, or major architectural choices  

---

## 🕰️ Version History

| Version | Date       | Summary                                                                                                                                |
|--------:|------------|----------------------------------------------------------------------------------------------------------------------------------------|
| v11.2.3 | 2025-12-08 | Aligned with KFM-MDP v11.2.5; updated front-matter telemetry/metadata; clarified AI/narrative safety, telemetry, and FAIR+CARE links. |
| v11.2.2 | 2025-11-27 | Rebuilt policy using `docs/security` governance; added supply-chain, SBOM/SLSA, NPM worm defense, and telemetry links.                |
| v11.0.0 | 2025-11-18 | Initial v11 security policy aligned with new CI/CD, FAIR+CARE, and sovereignty architecture.                                          |
| v10.0.0 | Legacy     | Early SECURITY.md baseline prior to v11 repository restructure.                                                                        |

---

<div align="center">

🛡️ **Kansas Frontier Matrix — Security Policy & Vulnerability Disclosure (v11.2.3)**  
Secure by Design · FAIR+CARE-Governed · Provenance-First  

[⬅️ Root README](../README.md) · [📚 Security Governance](../docs/security/README.md) · [🛡 Governance Charter](../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
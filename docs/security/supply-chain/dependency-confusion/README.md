---
title: "🛡️ KFM v11 — Dependency-Confusion Defense & Supply-Chain Integrity (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/dependency-confusion/README.md"
version: "v11.2.3"
last_updated: "2025-11-30"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Supply-Chain Security · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
backward_compatibility: "Aligned with v10.x → v11.x supply-chain security contract"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.3/release-manifest.zip"
telemetry_ref: "../../../../releases/v11.2.3/security-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/security-v3.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

doc_kind: "Security Pattern"
intent: "dependency-confusion-defense"

fair_category: "F1-A1-I1-R1"
care_label: "CARE · Governance · Protection of Critical Infrastructure"

classification: "Security · Supply Chain · Dependency Management"
sensitivity_level: "High"
sensitivity: "Security-Sensitive (Non-personal)"
public_exposure_risk: "Low"
indigenous_rights_flag: true
risk_category: "High"
redaction_required: false

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next supply-chain security revision"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/security/supply-chain/dependency-confusion/README.md@v11.2.2"
  - "docs/security/supply-chain/dependency-confusion/README.md@v11.2.1"
  - "docs/security/supply-chain/dependency-confusion/README.md@v11.0.0"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: false

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:security:dependency-confusion:root:v11.2.3"
semantic_document_id: "kfm-depconf-root-pattern-v11.2.3"
event_source_id: "ledger:depconf.root.v11.2.3"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "diagram-extraction"
  - "metadata-extraction"

ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"
---

<div align="center">

# 🛡️ **KFM v11 — Dependency-Confusion & Registry-Hijack Defense**  
### _Supply-Chain Integrity for CI/CD, Pipelines, and Knowledge-Graph Infrastructure_  

📦 **Reproducible Builds** · 🔐 **Supply-Chain Governance** · 🧬 **Provenance-Linked**  
🌐 **Registry-Pinned** · 🧱 **SLSA-Backed** · 🛰️ **Lineage-Verifiable**

</div>

---

## 1️⃣ Purpose

This directory defines the **official KFM defense pattern for dependency confusion & registry hijack**, ensuring no external registry package can silently override, impersonate, or supersede an internal module name used across:

- AI/ML pipelines  
- Orchestration DAGs  
- Geospatial ETL workers  
- Archaeology & heritage data governance services  
- KFM internal tooling packages (`kfm-*` namespaces)  
- Focus Mode / Story Node runtime modules  

All defensive controls here are **mandatory** for **v11.2.x** supply-chain compliance.

---

## 2️⃣ Directory Layout (Emoji-Prefix Standard)

~~~text
docs/security/supply-chain/dependency-confusion/
├── 📄 README.md                        # This file — root pattern & overview
│
├── 📁 policy/                          # Registry, pinning, signatures, fallback policies
│   ├── 📄 README.md                    # High-level policy overview
│   ├── 📄 rules.md                     # Enforcement rules
│   ├── 📄 registry-isolation.md        # Registry allow-list / isolation rules
│   ├── 📄 signature-requirements.md    # Cryptographic signature & provenance rules
│   ├── 📄 fallback-controls.md         # Degraded-mode and emergency controls
│   ├── 📄 exceptions.md                # SER-approved exceptions
│   ├── 📄 incidents.md                 # Incident log + forensics
│   └── 📂 evidence/                    # Machine evidence vault
│       ├── 🛰️ namespace-scan.json
│       ├── 🧬 sbom-diff.json
│       ├── 🔐 registry-audit.json
│       └── 🧾 attestation-verify.json
│
├── 📁 checks/                          # CI/CD & local automated check definitions
│   ├── 📄 README.md                    # Automated checks index
│   ├── 📄 ci-validation-rules.md       # CI validation + fail conditions
│   ├── 📄 provenance-hooks.md          # Provenance / SLSA hooks
│   ├── 📄 registry-anomaly-detection.md# Registry anomaly detection logic
│   ├── 📄 pre-commit-rules.md          # Developer pre-commit enforcement rules
│   └── 📄 local-scan-guidance.md       # Local/manual scan guidance (KFM-DTK usage)
│
└── 📁 examples/                        # Concrete example scenarios & patterns
    ├── 📄 README.md                    # Index of examples
    ├── 📄 namespace-collision-basic.md
    ├── 📄 namespace-collision-firstpublish.md
    ├── 📄 namespace-collision-versionrace.md
    ├── 📄 typosquat-examples.md
    ├── 📄 registry-fallback.md
    ├── 📄 mirror-drift.md
    ├── 📄 sbom-drift-basic.json
    ├── 📄 lockfile-drift-attack.md
    ├── 📄 invalid-cosign.sig
    ├── 📄 missing-provenance.json
    ├── 📄 sandbox-network-leak.md
    └── 📄 implicit-upgrade-attack.md
~~~

---

## 3️⃣ Threat Model — Registry-Based Substitution

### 3.1 Attack Vector

Dependency confusion occurs when:

- A **private-registry module** (e.g., `@kfm/geo-h3`)  
- Shares the **same name** as a public-registry module  
- And the public one advertises a **higher version number**  

Many package managers may prefer the **public package**, allowing:

- Silent malicious code execution  
- Credential/token exfiltration  
- Data integrity compromise  
- Lineage poisoning  
- Malicious pipeline stage injection  

### 3.2 Why KFM Is a High-Value Target

Because KFM orchestrates:

- Indigenous-rights–protected heritage datasets  
- High-resolution geospatial layers  
- Sensitive archaeological and environmental coordinates  
- Energy/carbon telemetry & sustainability reports  
- Automated Focus Mode narratives and explainability overlays  

…a registry hijack could compromise **ethical, scientific, and legal safety** and undermine  
**trust in KFM outputs**.

---

## 4️⃣ Mandatory Protective Controls

### 4.1 Registry Isolation Requirements

All KFM environments MUST:

- **Disable global registry fallbacks** in CI/CD and production.  
- **Whitelist only approved internal registries** (KFM and vetted mirrors).  
- Set `always-auth=true` for internal scopes.  
- **Reject unscoped public modules** in CI/CD jobs.  
- Enforce strict namespace scoping for first-party packages (`@kfm/*`).  

Where possible, lock down:

- `.npmrc` / `.pip.conf` / `poetry.toml` / `Cargo.toml` / `settings.xml`  
- Docker base images and build containers  
- Local developer environments (with documented overrides only)

### 4.2 Strict Version Pinning

Every module used in KFM MUST be:

- **Pinned by exact version** (`"1.2.3"`; never `^1.2.3` or `~1.2.3`)  
- **Backed by SBOM entries** (SPDX / CycloneDX)  
- **Validated with integrity hashes** (e.g., `integrity` in lockfiles, SHA-256 checksums)  
- **Subject to deterministic rebuild verification** in CI  

Lockfile changes MUST:

- Be reviewed via code review  
- Be scanned for registry/URL anomalies  
- Be tied to a governance ticket or PR label (`supply-chain-change`)

### 4.3 Build-Time Verification Hooks

CI/CD MUST integrate:

- Registry-origin attestation checks  
- SLSA-level provenance validation for build artifacts  
- Lockfile drift detection & SHA-lock verification  
- OpenLineage-linked resolution logs for dependency graphs  
- Registry metadata and maintainer-signature scanning  
- Anomaly detection on new transitive dependencies  

### 4.4 Metadata-Signature Enforcement

Every internal package MUST include:

- Provenance signatures (e.g., Sigstore)  
- Maintainer keychain entries (GPG / Sigstore identities)  
- Published SBOM fragments  
- Build attestations  
- Registry signature records (e.g., `rekor` logs)  

All MUST be validated during:

- Package resolution steps  
- Pipeline initialization  
- DAG promotion (dev → stage → prod)  
- Environment migration (new clusters/runtimes)

---

## 5️⃣ KFM v11.2 Registry-Resolution Pipeline

### 5.1 Resolution Order (Enforced)

1. **Internal Verified Registry (Primary)**  
2. **Internal Fallback Mirror (Read-Only)**  
3. **Local Cache (Signed, Verified)**  
4. **Public Registry Sources (DISABLED for CI/CD)**  

Public registries MAY be allowed only in **offline development mode** with clear documentation and  
local overrides — never in CI or production.

### 5.2 Automatic Deployment Failures

CI MUST **abort** the build if:

- A package name exists **both internally and publicly**  
- Public registry version **matches or exceeds** internal version  
- Signature or digest mismatch occurs  
- Maintainer identity is **unverified** or unexpected  
- SBOM provenance cannot be linked to attestation  

**No overrides** without:

- Multi-sig approval  
- Governance ticket  
- Logged justification in the security ledger  

---

## 6️⃣ Provenance Integration (STAC · DCAT · JSON-LD · PROV-O)

Dependency metadata is integrated into KFM lineage:

- Package identity → `prov:Entity`  
- Build job → `prov:Activity`  
- Maintainer signature → `prov:Agent`  
- Hash integrity → `kfm:IntegrityDigest`  
- Registry source → `kfm:RegistryURI`  

This ensures full traceability from:

> **Git commit → dependency → build environment → pipeline stage → dataset → STAC Item**  

Governance tools MUST be able to answer:

- “Which package version produced this dataset?”  
- “Which registry did it come from?”  
- “Which maintainer key signed it?”  

---

## 7️⃣ Governance & Policy Enforcement

All controls here are governed by:

- **Supply-Chain Security Working Group**  
- **FAIR+CARE Council**  
- **CI/CD Governance Board**

Violations trigger automatic:

- Build termination  
- Canary rejection for risky deployments  
- WAL rollback (where applicable)  
- Multi-sig approval requirement for any override  
- Security event logged under `ledger/security/supply-chain/`  

Recurring violations MUST trigger:

- Policy review  
- Post-incident analysis  
- Possible revocation of access for offending credentials or roles  

---

## 8️⃣ Version History

| Version | Date       | Summary                                                                                  |
|--------:|------------|------------------------------------------------------------------------------------------|
| v11.2.3 | 2025-11-30 | Upgraded to extended v11.2.2 metadata; aligned directory layout with policy/checks/examples. |
| v11.2.2 | 2025-11-30 | Full rewrite using KFM-MDP v11.2.2; added Diamond⁹ Ω certification.                      |
| v11.1.0 | 2025-10-15 | Added multi-registry fail-closed behavior and stronger CI gates.                         |
| v11.0.0 | 2025-09-01 | Introduced mandatory signature & SBOM correlation.                                       |

---

<div align="center">

🔐 [Policy Suite](./policy/README.md) • 🧪 [Automated Checks](./checks/README.md) • 🧭 [Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

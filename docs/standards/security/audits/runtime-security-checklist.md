---
title: "🧾 KFM v11 — Runtime Security Checklist (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/security/audits/runtime-security-checklist.md"
version: "v11.0.0"
last_updated: "2025-11-23"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../releases/v11.0.0/security-audits-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/security-audits-runtime-v1.json"
governance_ref: "../../governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active · Enforced"
doc_kind: "Runtime Audit Checklist"
semantic_document_id: "kfm-security-runtime-checklist-v11"
doc_uuid: "urn:kfm:standards:security:audits:runtime-security-checklist:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Medium-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🧾 **KFM v11 — Runtime Security Checklist**  
`docs/standards/security/audits/runtime-security-checklist.md`

**Purpose:**  
Provide a **standardized runtime security checklist** for KFM v11 services, pipelines, workers, and UIs.  
This checklist is used for **pre-release**, **quarterly**, and **incident-response** audits to verify that  
runtime environments, dependencies, SBOMs, attestations, secrets, and FAIR+CARE constraints are  
implemented and monitored correctly.

</div>

---

# 📘 1. Scope & Usage

This checklist applies to:

- All **runtime environments** (prod/stage/dev) for:
  - ETL / Autonomous pipelines
  - AI/ML inference services
  - API backends
  - MapLibre/Cesium / web UIs
- All **container images** that process KFM data
- All scheduled DAGs (LangGraph v11)
- All public-facing interfaces serving KFM outputs

**When to use this document:**

- Before each **v11.x release**
- During **quarterly security & FAIR+CARE audits**
- After any **security-relevant incident** or **major stack upgrade**
- When onboarding **new services** into the KFM runtime

---

# 🧩 2. Build & Supply-Chain Security

> Goal: ensure every deployable artifact is SBOM-documented, attested, and checksum-verified.

### ✅ Build & Artifact Checks

- [ ] **SBOM generated** for every release image / artifact  
  - [ ] `releases/<ver>/sbom.spdx.json` exists  
  - [ ] All runtime binaries, images, key data artifacts appear in SBOM  

- [ ] **Checksums registered**  
  - [ ] `data/archive/<quarter>/checksums/registry.jsonl` exists and includes all runtime artifacts  
  - [ ] `sha256` in registry matches on-disk or registry digests  

- [ ] **SLSA / in-toto attestations present**  
  - [ ] Each runtime image has `releases/<ver>/attestations/<image>.slsa.json`  
  - [ ] `subject.digest.sha256` in attestation matches checksum registry  

- [ ] **Checksum ⇄ SBOM ⇄ Provenance cross-check**  
  - [ ] `make validate-checksum-sbom` passes  
  - [ ] `make validate-provenance` passes  

- [ ] **OpenLineage run linkage**  
  - [ ] Attestations or SBOMs reference OpenLineage runs where applicable  
  - [ ] `lineage_run_uri` resolvable for critical pipeline artifacts  

---

# 🧱 3. Container & Runtime Environment Security

> Goal: ensure runtime containers and hosts are hardened and free from untracked drift.

### 🧱 Container Image Hardening

- [ ] Base images are **minimal** (e.g., distroless, slim)  
- [ ] Images are **built from lockfiles** (pinning dependencies)  
- [ ] Latest image tags are **immutable** and versioned (e.g., `kfm-api:v11.0.0`)  
- [ ] Image registry uses **signed images** (Sigstore/Cosign or similar)  
- [ ] `cosign verify` / equivalent passes for all deployed images  

### 🖥 Host & Orchestrator Controls

- [ ] OS packages up-to-date with security patches  
- [ ] Kubernetes / orchestration:
  - [ ] Pods use **non-root** users  
  - [ ] Read-only root filesystem where possible  
  - [ ] Resource limits (CPU/Memory) set  
  - [ ] Network policies restrict egress/ingress to required endpoints  
- [ ] Audit logs enabled at cluster and node level  

---

# 🔐 4. Secrets & Configuration Management

> Goal: avoid secret leakage and ensure configuration is auditable and least-privileged.

### 🔐 Secrets Management

- [ ] Secrets stored in a **dedicated secret manager** (not in code or plain YAML)  
- [ ] No secrets in:
  - [ ] Git history
  - [ ] Container images
  - [ ] STAC metadata  
- [ ] Secret rotation policy documented & applied (per governance)  
- [ ] Secrets access is **role-based** and logged  

### ⚙ Configuration

- [ ] All runtime config is:
  - [ ] Environment-based (env vars, configmaps, etc.)  
  - [ ] Documented in MCP/SOPs  
  - [ ] Version-controlled (non-secret portions)  
- [ ] No production-only flags enabled in dev/test  
- [ ] No debug/trace logging of sensitive data  

---

# 🧬 5. Dependency & Vulnerability Management

> Goal: ensure no known-vulnerable libraries or binaries run untracked.

### 📦 Dependencies

- [ ] Dependency lockfiles used (e.g., `poetry.lock`, `package-lock.json`, etc.)  
- [ ] CI runs dependency vulnerability scans:
  - [ ] `pip-audit` / `npm audit` / equivalent  
  - [ ] OS package scanner (e.g., Trivy, Grype)  

- [ ] High/critical vulnerabilities:
  - [ ] Are documented with remediation plan  
  - [ ] Are mitigated or accepted by governance  

### 🔎 SBOM Vulnerability Scans

- [ ] SBOM scanned against vulnerability databases  
- [ ] Vulnerability reports linked into audit trail  

---

# 🛰 6. Pipeline & API Runtime Controls

> Goal: prevent misbehavior of ETL/AI pipelines and API endpoints at runtime.

### 🛰 Pipelines (LangGraph / Autonomous)

- [ ] All DAGs have:
  - [ ] Retry + backoff configured  
  - [ ] Idempotent node behavior  
  - [ ] Timeout limits  
  - [ ] Circuit-breakers or kill-switches for runaway loops  

- [ ] Pipelines:
  - [ ] Validate all inputs (schema, size, type)  
  - [ ] Validate outputs (STAC, schemas, CRS, vertical-axis)  
  - [ ] Fail safe and alert on anomalies  

### 🌐 APIs

- [ ] TLS enforced for all external endpoints  
- [ ] AuthN/AuthZ where applicable  
- [ ] Reasonable rate limits  
- [ ] Input validation & sanitization  
- [ ] Clear error responses without leaking implementation details  

---

# 📊 7. Logging, Monitoring & Telemetry

> Goal: detect anomalies, security events, and provenance issues early.

### 📊 Telemetry

- [ ] Prometheus / metrics endpoints integrated for critical services  
- [ ] Logging includes:
  - [ ] Request IDs
  - [ ] Pipeline run IDs
  - [ ] OpenLineage run IDs  

- [ ] Logs:
  - [ ] Avoid secrets  
  - [ ] Are retained per policy  
  - [ ] Are searchable via centralized log system  

### 🧭 Security & Audit Logs

- [ ] Access logs for:
  - [ ] API endpoints  
  - [ ] Admin operations  
  - [ ] Data exports  

- [ ] Automated alerts:
  - [ ] Too many failed auth attempts  
  - [ ] Unusual access patterns  
  - [ ] Unexpected pipeline failures  

---

# 🌱 8. FAIR+CARE & Data Ethics Runtime Checks

> Goal: ensure runtime behavior respects FAIR+CARE, especially for Indigenous and sensitive data.

### 🌱 CARE Controls

- [ ] H3 generalization enabled for sensitive locations at runtime  
- [ ] Applications:
  - [ ] Do **not** render raw coordinates for L3/L4 sites  
  - [ ] Enforce **masking rules** from `archaeology-sensitive-locations.md`  

- [ ] Focus Mode v3:
  - [ ] Avoids generating narratives that reveal restricted knowledge  
  - [ ] Honors `care:authority` & `care:consent_required` flags  

### 🔍 FAIR Constraints

- [ ] All APIs expose metadata about data source, license, and provenance  
- [ ] No proprietary data is exposed without license checks  
- [ ] Users can inspect lineage for displayed data  

---

# 🧯 9. Incident Response & Recovery

> Goal: ensure clear playbooks exist for security incidents and rapid, verified recovery.

### 🧯 Incident Playbooks

- [ ] Incident response SOPs documented and accessible  
- [ ] Roles & responsibilities clear (who triages, who communicates)  
- [ ] Runbooks exist for:
  - [ ] Data corruption  
  - [ ] Compromised secrets  
  - [ ] Supply-chain compromise  
  - [ ] SBOM/attestation integrity loss  

### 💾 Backups & Recovery

- [ ] Backups configured and tested  
- [ ] Recovery procedures validated regularly  
- [ ] After recovery:
  - [ ] Checksums re-verified  
  - [ ] SBOM and attestations updated as needed  

---

# 📝 10. Audit Result Recording

For each runtime audit cycle:

- [ ] Fill out **artifacts-audit-template.md** for critical artifacts  
- [ ] Save completed checklists in:
  - [ ] `docs/archives/provenance/audits/security/<YYYY-MM-DD>-runtime-checklist.md`  
- [ ] Attach:
  - [ ] SBOM snapshot  
  - [ ] Checksum registry snapshot  
  - [ ] Attestation bundle  
  - [ ] OpenLineage summary  

These records become part of the **provenance archive**.

---

# 🕰 Version History

- **v11.0.0 (2025-11-23)** — Initial runtime security checklist for KFM v11.

---

<div align="center">

**Kansas Frontier Matrix — Runtime Security Checklist (v11)**  
*Secure · Auditable · FAIR+CARE-Aligned*

</div>

---

### 🔗 Footer  
[⬅ Back to Security Audits Index](./README.md) · [🔗 Checksum–SBOM–Provenance Standard](../checksum-sbom-provenance.md) · [🏛 Governance](../../governance/ROOT-GOVERNANCE.md)


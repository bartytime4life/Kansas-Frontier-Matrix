---
title: "🛡️ KFM v11.2.4 — React2Shell (CVE-2025-55182 / 66478) Emergency Hardening Playbook"
path: "docs/security/react2shell/README.md"
version: "v11.2.4"
last_updated: "2025-12-05"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Monthly · Supply Chain Security · Frontend Risk Council"
content_stability: "stable"
backward_compatibility: "n/a (security bulletin)"
status: "Active / Enforced"

commit_sha: "<latest-commit-sha>"
previous_version_hash: "<prior-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../releases/v11.2.4/security-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/security-incident-schema-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"

license: "CC-BY-4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
---

# 🛡️ React2Shell Critical Vulnerability Response (KFM Hardening Bulletin)

## 1. Purpose

This document establishes **KFM’s governed response protocol** for the *React2Shell* vulnerability (CVE-2025-55182 / CVE-2025-66478).  
This vulnerability enables **unauthenticated remote code execution (RCE)** through unsafe handling of React Server Components (RSC) flight payloads in React 19.x and downstream frameworks, including Next.js.

This playbook aligns with KFM’s:
- Deterministic software supply-chain rules  
- Frontend runtime isolation architecture  
- SLSA + SBOM verification  
- Zero-trust ingestion perimeter  
- Event-driven CI/CD auditing  

---

## 2. Affected KFM Components

### 2.1. Frontend Cluster
- `src/web/kfm-frontend/` (React + MapLibre + Cesium stack)
- Any RSC-enabled build pipeline
- Any SSR worker / edge-render process

### 2.2. API Gateways
- Asset-serving proxies
- Flight-payload streaming endpoints (if enabled)

### 2.3. Reproducibility Environment
- Node-based deterministic builds  
- Deployment bundles relying on React 19.x prior to patched versions  

---

## 3. Required Versions (Enforced Immediately)

| Package | Safe Minimum Version | Notes |
|--------|-----------------------|-------|
| React | **19.0.1+**, 19.1.2+, 19.2.1+ | Mandatory |
| react-server-dom-* | Matching patched set | Must be pinned |
| Next.js | **15.0.5 / 15.1.9 / 15.2.6 / 15.3.6 / 15.4.8 / 15.5.7 / 16.0.7** | All KFM deployments must use one of these |
| Turbopack RSC modules | Latest patched artifacts | Verified by SBOM |

All version bumps must be committed with:
- Deterministic lockfiles  
- Build reproducibility attestation  
- SBOM delta diff  

---

## 4. KFM Mitigation Pipeline (Mandatory Sequence)

### Step 1 — **Immediate Dependency Pin & Rebuild**
- Update all React-related packages to patched versions.
- Freeze lockfile.
- Verify signature + provenance via SLSA generator.
- Regenerate SBOM; attach to release manifest.

### Step 2 — **RSC Attack Surface Reduction**
KFM disables the following until audit completion:
- Arbitrary server actions  
- Undocumented server endpoints  
- Any non-declared RSC boundary  

All SSR workers must reject:
- Unknown flight payloads  
- Non-signed streams  
- Cross-origin RSC frames  

### Step 3 — **Traffic-Level Protection**
KFM edge layer enforces:
- Strict payload size limits  
- Schema validation of flight format  
- WAF rules scoped to React2Shell exploit signatures  
- Canary shadow deployment before promotion

### Step 4 — **Runtime Isolation**
Frontend SSR workers must run with:
- Non-root user  
- No filesystem write permission  
- Syscall sandbox mode  
- Deterministic CPU/memory caps  

### Step 5 — **Verification Tests**
Deterministic CI gates run:
- RSC flight-fuzzer tests  
- Replay-based exploit regression suite  
- SBOM dependency drift detector  
- Build reproducibility validator  

---

## 5. KFM Frontend Architecture Adjustments

### 5.1. Enforced Separation
KFM permanently enforces:
- **RSC boundary separation** from user-influenced data  
- No dynamic eval/loader pathways  
- No inline server actions without governance approval  

### 5.2. Directed Dataflow Model
The pipeline becomes:

**Client → Static Payload → Server Renderer (sandboxed) → Typed Flight Response → Client**

No untyped, unverified, or dynamic code paths are permitted.

---

## 6. Monitoring, Telemetry & Forensics

Telemetry emitted per request:
- `flight.validation.status`
- `rsc.payload.anomaly_score`
- `waf.react2shell.block.count`
- `sbom.revision.hash`
- `build.determinism.pass`
- `sandbox.violation.count`

Daily rollups feed into:
- Provenance ledger  
- Security anomaly graph  
- Deployment reliability budget  

---

## 7. Incident Response (If Suspicious Activity Detected)

1. **Quarantine** suspicious SSR workers  
2. **Snapshot filesystem** (read-only)  
3. **WAL replay** of flight activity  
4. **Neo4j security graph** enrichment  
5. **Regenerate artifact lineage**  
6. **Apply hotfix pipeline** (fast-track, deterministic)  

---

## 8. Long-Term Governance

This vulnerability is now a **permanent class** in KFM’s supply-chain threat model.  
All future frontend upgrades must pass:

- RSC Safety Review  
- Supply-chain Diff Audit  
- Governance Council Approval  

No uncontrolled React/Next.js upgrades are permitted.

---

## 9. Directory Layout

```
docs/
└── security/
    └── react2shell/
        ├── README.md
        ├── mitigations.md
        ├── waf-rules.md
        ├── sbom-diff/
        └── audits/
```

---

## 10. Version History

| Version | Date | Summary |
|--------|-------|---------|
| v11.2.4 | 2025-12-05 | Initial governed hardening bulletin |

---

# 🔚 Footer

**Kansas Frontier Matrix (KFM)**  
FAIR+CARE Aligned • Deterministic • Open Knowledge Infrastructure  

📘 Documentation Hub — `/docs/`  
🧪 Standards Registry — `/docs/standards/`  
🛠️ Pipelines Index — `/docs/pipelines/`  
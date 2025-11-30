---
title: "🛡️ KFM v11 — Supply-Chain Defense Against Shai-Hulud 2.0 (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/shai-hulud-2.0/README.md"
version: "v11.2.3"
last_updated: "2025-11-29"

release_stage: "Stable / Enforced"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Security Guild · FAIR+CARE Council Oversight"
backward_compatibility: "Aligned with v10.x → v11.x defense profiles"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.3/manifest.zip"
signature_ref: "../../../../releases/v11.2.3/signature.sig"
attestation_ref: "../../../../releases/v11.2.3/slsa-attestation.json"

telemetry_ref: "../../../../releases/v11.2.3/security-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/supply-chain-defense-v11.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
status: "Active / Enforced"
doc_kind: "Security Architecture"
intent: "supply-chain-defense-overview"
fair_category: "F1-A2-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🛡️ **KFM Supply-Chain Defense — Shai-Hulud 2.0 Mitigation Blueprint**
`docs/security/supply-chain/shai-hulud-2.0/README.md`

**Purpose:**  
Protect KFM’s deterministic AI/ETL/graph stack against the cross-ecosystem **Shai-Hulud 2.0** supply-chain worm:  
npm • Maven • PyPI • GitHub Actions • lifecycle scripts • poisoned artifacts • compromised runners.

**Scope:**  
Dependency hardening · SLSA provenance · CI kill-switches · SBOM deltas · runner governance  
</div>

---

## 🚨 1. Threat Model Summary

Shai-Hulud 2.0 is a **multi-ecosystem supply-chain worm** capable of:

- Hijacking npm maintainers  
- Republishing tainted Maven artifacts  
- Injecting payloads into lifecycle hooks (`preinstall`, `install`, `postinstall`)  
- Using Bun-loader evasion patterns  
- Exfiltrating SSH/GitHub/cloud tokens  
- Registering **rogue self-hosted runners**  
- Dropping hidden persistence workflows (`discussion.yaml`)  
- Triggering destructive branches when containment is detected  

KFM enforces **zero-trust dependency intake**, immutable builds, and full elimination of installer hooks.

---

## 🧱 2. KFM Hardening Principles (v11 Enforcement)

1. **Deterministic dependency freezing** — pinned versions + SHA256 integrity  
2. **Lifecycle hook ban** — pipeline halts immediately if any install script is detected  
3. **Network-isolated builds** — build containers cannot reach public internet  
4. **Immutable CI/CD** — golden images + reproducible builds  
5. **SBOM-driven variance detection** — unexpected deps → kill-switch  
6. **Runner governance** — no unverified self-hosted runners; hashed audits  

---

## 🛟 3. SOC Detection Signatures

### High Confidence
- `setup_bun.js`, `bun_loader.js`, `bun_environment.js`  
- Unauthorized runner registration  
- Presence of `.github/workflows/discussion.yaml`  
- Token exfil to random repositories  

### Medium Confidence
- Sudden republishing of trusted libraries  
- Bun executable/runtime discovered unexpectedly  
- Shadow-mirror artifact lineage mismatch  

---

## 🔐 4. CI/CD Protection Patterns

### Required
- **WAL + rollback** for all artifact updates  
- **Digest mismatch kill-switch**  
- **Canary dependency tests**  
- **Idempotent graph-safe upserts**  

### Forbidden
- Network during install  
- Tarball ingest without attestation  
- Dynamic import bypassing manifests  

---

## 🧬 5. SLSA v11 Provenance Enforcement

All ingested artifacts must include:

- `buildType`  
- `builder.id`  
- `invocation.configSource`  
- complete `materials[]` hash list  

Mismatch = **blocked ingestion**.

---

## 🗂️ 6. Directory Layout

~~~text
docs/security/supply-chain/shai-hulud-2.0/
├── 📄 README.md                      # This file
├── 📊 indicators/                    # IOC catalogs, signature patterns, hashed indicators
├── 🛡️ protections/                   # CI guards, dependency-freeze rules, validation policies
├── 🧬 provenance/                    # SLSA v11 templates, attestations, provenance bundles
├── 🔧 workflows/                     # Hardened GitHub workflow templates
├── 📑 reports/                       # Incident reports, worm timelines, threat chronicles
└── 📦 stac/                          # STAC / JSON-LD metadata for security artifacts
~~~

---

## 🔍 7. Story Node & Focus Mode Integration

- Threat cascade narratives across ecosystems  
- Spatial & temporal propagation mapping  
- STAC-backed metadata for forensic replay  
- Focus Mode v3: entity-centered summaries with lineage & explainability  

---

## ♻️ 8. Version History

**v11.2.3 — 2025-11-29**  
• Updated to Emoji-Prefix Layout Standard v11.2.2  
• Fully rebuilt for box-integrity and canonical directory style  
• Hardening principle clarifications  

**v11.2.2 — 2025-11-29**  
• Initial Shai-Hulud 2.0 integration  

---

<div align="center">

**🛡️ KFM Security · Deterministic · FAIR+CARE**

[📘 Docs Root](../../../..) · [🧪 Pipelines](../../../pipelines) · [🌐 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>


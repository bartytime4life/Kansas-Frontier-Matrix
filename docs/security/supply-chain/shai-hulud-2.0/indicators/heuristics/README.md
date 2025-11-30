---
title: "🧠 KFM v11 — Shai-Hulud 2.0 Heuristic Indicators (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/shai-hulud-2.0/indicators/heuristics/README.md"
version: "v11.2.3"
last_updated: "2025-11-29"

release_stage: "Stable / Enforced"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Security Guild · FAIR+CARE Council Oversight"
backward_compatibility: "Aligned with v10.x → v11.x heuristic-governance model"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.3/manifest.zip"
signature_ref: "../../../../../../releases/v11.2.3/signature.sig"
attestation_ref: "../../../../../../releases/v11.2.3/slsa-attestation.json"

telemetry_ref: "../../../../../../releases/v11.2.3/security-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/supply-chain-defense-v11.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
status: "Active / Enforced"
doc_kind: "IOC-Heuristic-Signatures"
intent: "supply-chain-defense-heuristic-indicators"
fair_category: "F1-A2-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🧠 **Shai-Hulud 2.0 — Heuristic Indicator Catalog**
`docs/security/supply-chain/shai-hulud-2.0/indicators/heuristics/README.md`

**Purpose:**  
Define all **behavioral**, **contextual**, and **non-pattern** heuristic indicators used to identify  
Shai-Hulud 2.0 across package ecosystems, CI/CD systems, and provenance chains.

**Scope:**  
Behavioral signals · anomaly cues · dependency drift · workflow irregularities · provenance mismatches  

</div>

---

## 🧬 1. Overview

Heuristic indicators serve as **behavior-driven detection rules**, catching Shai-Hulud 2.0 variants  
that bypass static signatures (hash, regex, YARA) through polymorphism or structural evasion.

These heuristics are **deterministic in evaluation**, but capture higher-level behaviors such as:

- abnormal execution environments  
- repeated artifact mutation across builds  
- suspicious workflow invocation patterns  
- dependency drift inconsistent with declared manifests  
- provenance weaknesses not attributable to normal processes  

Heuristics complement:

- file-hash IoCs  
- pattern-based signatures  
- structural graph signatures  

---

## 🧱 2. Heuristic Categories

### **1. Behavioral Loader Heuristics**
- Suspicious Bun-loader pre-execution checks  
- Import-delay or time-based evasion mechanisms  
- `process.env.*` probing or environment scanning bursts  
- Conditional execution triggered by install-time metadata  

### **2. Manifest & Dependency Drift Heuristics**
- Declared dependencies absent in runtime  
- Spurious or duplicate imports  
- Divergence between repeated lockfile generations  
- Negative drift in dependency graph metrics  

### **3. CI/CD Anomalous Activity Heuristics**
- Runner registration with non-human timing patterns  
- Workflows containing hidden or reordered steps  
- Build steps intermixed with install routines  
- Outbound network calls during dependency installation  

### **4. Provenance Drift Heuristics**
- Low-confidence SLSA material matches  
- Unexpected `builder.id` changes between builds  
- Missing attestations or incomplete material lists  
- Temporal drift between commit timestamps and build events  

### **5. Cross-Ecosystem Behavioral Correlations**
- Identical heuristic cues across npm/Maven/PyPI/Bun  
- Shared loader-logic anomalies (Bun/ESBuild)  
- Multi-registry publication with consistent anomaly markers  

---

## 🧬 3. Heuristic Schema (KFM v11 IOC Format)

Each heuristic includes:

- `id` — UUIDv4  
- `severity` — low/medium/high/critical  
- `confidence` — float 0–1  
- `rule_type` — heuristic  
- `signal` — description of the behavioral cue  
- `ecosystem` — npm | maven | pypi | bun | github-actions  
- `first_seen` / `last_seen`  
- `provenance` — PROV-O lineage  
- `mitigation` — review/block/isolate/rebuild  
- `evidence_assets[]` — synthetic safe examples  

Heuristic rules MUST be:

- reproducible  
- deterministic  
- fully documented  
- free of sensitive data  

---

## 📦 4. STAC Integration

Each heuristic is expressed as a **STAC Item**:

- `properties.datetime` — detection timestamp  
- `properties.heuristic_type` — behavior | dependency | cicd | provenance  
- `assets.heuristic` — the heuristic JSON rule  
- `assets.provenance` — PROV-O bundle  
- `assets.metadata` — DCAT metadata  

STAC enables:

- timeline clustering  
- cross-ecosystem anomaly correlation  
- Focus Mode narrative linking  

---

## 🗂️ 5. Directory Layout

~~~text
docs/security/supply-chain/shai-hulud-2.0/indicators/heuristics/
├── 📄 README.md            # This file
├── 🧠 behavior/            # Runtime & loader behavior heuristics
├── 🧬 dependency/          # Manifest/lockfile drift & dependency anomalies
├── 🛠️ cicd/                # Workflow timing, runner anomalies, CI/CD irregularities
├── 🧾 provenance/          # Provenance-weakening heuristic signals
├── 📦 stac/                # STAC Items / Collections for heuristic rules
└── 🧷 samples/             # Synthetic examples used for CI validation & onboarding
~~~

---

## 🔍 6. Story Node & Focus Mode Integration

Heuristics generate **Story Node v3** entities containing:

- the heuristic class  
- linked events & artifacts  
- a temporal footprint (first_seen → last_seen)  
- provenance-backed narrative text  
- relations to structural, pattern, and file-hash indicators  

Focus Mode v3 uses these to:

- explain unexpected behaviors  
- highlight emerging infection sequences  
- unify signals from multiple ecosystems  
- support analyst reasoning with deterministic, reproducible logic  

---

## 🧭 Version History

| Version | Date       | Summary                                                                                                   |
|---------|------------|-----------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Complete rewrite; emoji-prefix directory added; governance/H3 upgrades; aligned with KFM-MDP v11.2.2.     |
| v10.4.0 | 2025-11-15 | Earlier satellite overview; pre-v11 metadata structure.                                                    |

---

<div align="center">

[📘 Docs Root](../../../../../../..) · [🧪 Pipelines](../../../../../../../pipelines) · [🌐 Governance](../../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>


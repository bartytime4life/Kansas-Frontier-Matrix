---
title: "🛠️ Kansas Frontier Matrix — Web Utility Modules (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/utils/README.md"
version: "v10.3.1"
last_updated: "2025-11-13"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/web-utils-v2.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🛠️ **Kansas Frontier Matrix — Web Utility Modules**  
`web/src/utils/README.md`

**Purpose:**  
Define the **reusable, deterministic TypeScript utilities** used across the KFM Web Platform.  
These utilities provide **accessibility**, **provenance**, **schema validation**, **CARE-aware redaction**, and **telemetry instrumentation**, forming the backbone of Focus Mode v2.4 and all map/timeline UX logic.

[![Docs](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)]()  
[![License: MIT](https://img.shields.io/badge/License-MIT-green)]()  
[![Status](https://img.shields.io/badge/Status-Stable-success)]()

</div>

---

## 📘 Overview

The **utilities module** provides the pure, fully testable, cross–component logic that powers:

- Accessibility enforcement (WCAG 2.1 AA)  
- Provenance chips, ledger link generation, JSON-LD lineage  
- Runtime schema validation of all API DTOs  
- CARE-aware redaction (sovereignty, sensitivity, restricted content)  
- Formatting for dates, numbers, metadata labels  
- Telemetry emission (WebVitals, ethics, a11y, energy/CO₂e est.)  

All utilities MUST be:

- **Pure functions**  
- **Strictly typed**  
- **Deterministic**  
- **Side-effect free** (exceptions: telemetry emitters)  
- **Governance-aware**  

These functions support **React components, hooks, Focus Mode, mapping, timeline, and Story Nodes**.

---

## 🗂️ Directory Layout (v10.3.1)

~~~~~text
web/src/utils/
├── README.md
│
├── schemaGuards.ts        # Runtime DTO validation (Focus/STAC/DCAT/Graph)
├── provenance.ts          # Provenance chips, JSON-LD lineage, ledger linking
├── a11y.ts                # Accessibility helpers (ARIA, focus, keyboard logic)
└── formatters.ts          # Date/number/label formatting for consistent UI
~~~~~

---

## 🧩 Module Responsibilities

### 1. **schemaGuards.ts**

**Purpose:**  
Guarantee payload integrity from REST/GraphQL/STAC/DCAT by validating structure before it reaches UI components.

**Enforces:**  
- Required fields for Focus Mode responses  
- Required STAC/DCAT asset metadata  
- Required entity fields (Person, Place, Event, StoryNode)  
- Type-safety via predicates  
- Fails fast → component refuses to render malformed payloads  

**CI Behavior:**  
If any guard test fails → **merge blocked**.

---

### 2. **provenance.ts**

**Purpose:**  
Generate provenance badges, lineage chains, JSON-LD merges, citation chips, and governance deep links.

**Features:**  
- Build provenance chips linking to STAC Items → DCAT → ledger  
- CARE-aware provenance warnings (restricted dataset flags)  
- Resolve dataset → storynode → event relationships  
- Normalize lineage references from API payloads  
- Output consistent citation tokens  

**Governance Integration:**  
Outputs must point to:

```
../../../docs/reports/audit/web-governance-ledger.json
```

---

### 3. **a11y.ts**

**Purpose:**  
Centralize **WCAG 2.1 AA** logic required across all components.

**Includes:**  
- Focus traps  
- Skip link helpers  
- ARIA role/landmark utilities  
- Reduced-motion detectors  
- Screen-reader announcements  
- Keyboard map/timeline navigation helpers  

**Tokens referenced from:**  
```
docs/design/tokens/accessibility-tokens.md
```

---

### 4. **formatters.ts**

**Purpose:**  
Normalize formatting for UI elements.

**Contains:**  
- `formatDate()` — ISO → human-readable  
- `formatRange()` — time intervals  
- `formatNumber()` — locale-aware formatting  
- `formatLayerLabel()` — STAC/DCAT layer names  
- `formatCitation()` — provenance label formatting  

This ensures timeline, map legends, and Focus Mode use **identical formats**.

---

## ⚙️ Utility Workflow

~~~~~mermaid
flowchart TD
  A["Component Interaction"] --> B["Utility Function<br/>(schema/a11y/provenance/format)"]
  B --> C["Telemetry Event<br/>(WebVitals · A11y · Ethics)"]
  C --> D["Governance Sync<br/>(FAIR+CARE · Provenance)"]
  D --> E["Focus Mode Context<br/>Explainability + Lineage"]
~~~~~

---

## 🧾 Example Utility Metadata Record (v10.3.1)

~~~~~json
{
  "id": "web_utils_registry_v10.3.1",
  "modules": ["schemaGuards.ts", "provenance.ts", "a11y.ts", "formatters.ts"],
  "wcag_compliance": "2.1 AA",
  "fairstatus": "certified",
  "checksum_verified": true,
  "telemetry_linked": true,
  "efficiency_score": 99.4,
  "timestamp": "2025-11-13T17:22:00Z",
  "governance_ref": "docs/reports/audit/web-governance-ledger.json"
}
~~~~~

---

## 🧠 FAIR+CARE Governance Matrix

| Principle | Implementation | Oversight |
|----------|----------------|-----------|
| **Findable** | Utilities registered & indexed in governance ledgers | @kfm-data |
| **Accessible** | WCAG 2.1 AA utility compliance | @kfm-accessibility |
| **Interoperable** | JSON-LD, STAC/DCAT, DTO-aligned output | @kfm-architecture |
| **Reusable** | Pure, testable utility functions | @kfm-design |
| **Collective Benefit** | Ethical automation across UI workflows | @faircare-council |
| **Authority to Control** | CARE-based redaction & consent logic | @kfm-governance |
| **Responsibility** | Sustainability logging & ethical safeguards | @kfm-security |
| **Ethics** | Prevent misuse of culturally sensitive content | @kfm-ethics |

**Audit Paths:**  
- FAIR+CARE: `docs/reports/fair/data_care_assessment.json`  
- Provenance: `docs/reports/audit/data_provenance_ledger.json`

---

## 🧩 Module Summary Table

| Module | Description | Role |
|--------|-------------|------|
| `schemaGuards.ts` | Runtime DTO validators for Focus/STAC/DCAT/Graph | Data Integrity |
| `provenance.ts` | JSON-LD lineage + citation chips + ledger linking | Governance / Provenance |
| `a11y.ts` | ARIA/focus helpers, keyboard ops, announcements | Accessibility |
| `formatters.ts` | Dates, numbers, labels, UI formatting | UI Consistency |

---

## 🔐 CI/CD & Validation

| Workflow | Purpose | Artifact |
|----------|----------|----------|
| `docs-lint.yml` | Markdown & metadata conformity | `reports/self-validation/docs/lint_summary.json` |
| `build-and-deploy.yml` | Web integration & build health | `docs/reports/telemetry/build_metrics.json` |
| `telemetry-export.yml` | Merge runtime metrics | `releases/v10.3.0/focus-telemetry.json` |
| `codeql.yml` | Security scanning | `reports/security/codeql/*.sarif` |
| `trivy.yml` | Dependency CVE scanning | `reports/security/trivy/*.json` |

All modules must pass **strict TypeScript**, **A11y**, **FAIR+CARE**, and **schema** tests.

---

## 🌱 Sustainability Metrics

| Metric | Target | Verified By |
|--------|--------|-------------|
| Energy per UI interaction | ≤ 0.5 Wh | @kfm-sustainability |
| Carbon output | ≤ 1.2 gCO₂e | @kfm-security |
| Renewable energy | 100% RE100 | @kfm-infrastructure |
| FAIR+CARE certification | 100% | @faircare-council |

Telemetry stored in:

```
../../../releases/v10.3.0/focus-telemetry.json
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|--------|--------|--------|---------|
| v10.3.1 | 2025-11-13 | Web Architecture Team | Upgraded from v9.7.0 → v10.3.1; aligned with new utils layout & telemetry schema v2. |
| v9.7.0 | 2025-11-05 | KFM Core Team | Previous utility registry baseline. |

---

<div align="center">

**Kansas Frontier Matrix — Web Utility Modules**  
Deterministic Logic × FAIR+CARE × Provenance by Design × Accessibility  
© 2025 Kansas Frontier Matrix — MIT License  

[Back to Source Index](../README.md) · [Source Architecture](../ARCHITECTURE.md)

</div>

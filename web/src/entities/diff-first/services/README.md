---
title: "🛰️ Kansas Frontier Matrix — Diff-First Entity Services Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/entities/diff-first/services/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous + FAIR+CARE Council"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/web-entity-diff-services-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/web-entity-diff-services-v2.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Architecture Overview"
intent: "web-entity-diff-services"
role: "overview"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Mixed (entity- and dataset-dependent)"
sensitivity_level: "Entity-dependent"
public_exposure_risk: "Medium"
indigenous_rights_flag: "Conditional"
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true

provenance_chain:
  - "web/src/entities/diff-first/services/README.md@v10.3.2"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "SoftwareSourceCode"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"

json_schema_ref: "../../../../../schemas/json/web-entity-diff-services-readme-v11.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/web-entity-diff-services-readme-v11-shape.ttl"
doc_uuid: "urn:kfm:doc:web-entity-diff-services-readme-v11.2.2"
semantic_document_id: "kfm-doc-web-entity-diff-services-readme-v11"
event_source_id: "ledger:web/src/entities/diff-first/services/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with strict constraints"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "summaries"
  - "speculative-additions"
  - "unverified-historical-claims"
  - "governance-override"
  - "content-alteration"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "United States / Kansas"
classification: "Public / Geospatial- + Governance-sensitive logic"

ttl_policy: "Review each major release"
sunset_policy: "Superseded upon Diff-First services v12 overhaul"
---

<div align="center">

# 🛰️ **Kansas Frontier Matrix — Diff-First Entity Services Architecture**  
`web/src/entities/diff-first/services/README.md`

**Purpose:**  
Define the **deep-architecture, FAIR+CARE-certified service layer** for the Diff-First Entity subsystem.  
These services retrieve release-to-release diff payloads, guarantee schema and governance correctness,  
enforce CARE protections, and feed normalized, telemetry-validated models into the **Diff-First Components**,  
**Hooks/Model**, **Drawer**, **Focus Mode v3**, and **Governance UI**.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![License: MIT](https://img.shields.io/badge/License-MIT-green)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Services-orange)]()  
[![Status: Stable](https://img.shields.io/badge/Status-Stable-success)]()

</div>

---

## 📘 Overview

The **Diff-First Services Layer** is responsible for:

- Retrieving **canonical entity diffs** between releases (`R_prev`, `R_curr`)  
- Normalizing raw API responses into **FAIR+CARE-certified diff models**  
- Providing **stable, versioned contracts** for UI, hooks, and test layers  
- Enforcing **CARE masking** on diff nodes and relations  
- Marshaling provenance (STAC · DCAT · PROV-O · Neo4j lineage)  
- Emitting **telemetry** for diff compute time, governance deltas, and A11y coverage  
- Guaranteeing **MCP-DL v6.3** reproducibility (deterministic inputs → outputs)  
- Caching results ethically (no sensitive payload persistence beyond ephemeral caches)  

It forms the backend-facing backbone of the **Diff-First Entity Architecture**.

---

## 🗂️ Directory Layout

~~~text
web/src/entities/diff-first/services/
│
├── 📘 README.md        # This file
└── 🛰️ diffClient.ts    # Sole service entrypoint for Diff-First data retrieval
~~~

`diffClient.ts` is the **only** service module allowed to call the diff API directly.

---

## 🧩 High-Level Service Architecture

*(Use ```mermaid``` in-repo; `~~~mermaid` here avoids nested-fence issues.)*

~~~mermaid
flowchart TD
    REQ[UI/Hook Request<br/>entityId · R_prev · R_curr] --> CLIENT[diffClient]
    CLIENT --> NET[Network Layer<br/>REST · GraphQL]
    NET --> RAW[RawDiffResponse]
    RAW --> GUARD[Schema Guards<br/>type safety · governance fields]
    GUARD --> CARE[CARE & Sovereignty Enforcement]
    CARE --> NORM[Normalizer<br/>canonical diff model]
    NORM --> CACHE[Ephemeral Cache<br/>ethical memory cache]
    NORM --> OUT[Diff Model<br/>structural · governance · explainability]
    OUT --> TEL[Telemetry Hooks]
~~~

---

## 🧬 Canonical Data Contract

The service **must** return the normalized `EntityDiff` structure used across UI + hooks + tests.

### `EntityDiff` (Normalized)

~~~ts
export type EntityDiff = {
  entityId: string;
  entityType: "person" | "place" | "event" | "dataset";
  releasePrev: string;
  releaseCurr: string;
  summary: {
    added: number;
    removed: number;
    changed: number;
    severity: "low" | "med" | "high";
  };
  properties: PropertyChange[];
  relations: RelationChange[];
  text: TextChange[];
  governance: GovernanceChange;
  explainability?: ExplainabilityDelta[];
};
~~~

The service enforces:

- **strict static typing** via TypeScript + schema guards  
- **governance validation** (CARE, sovereignty, license) before returning  
- **shape stability** across releases (versioned schema where necessary)  

---

## 🛰️ diffClient.ts — Deep Architecture Specification

`diffClient.ts` MUST:

### 1️⃣ Perform Release-Aware Fetching

- Pull diffs for exact `(entityId, R_prev, R_curr)` tuples.  
- Support release navigation sourced from ReleasePicker/`useReleaseTags`.  
- Resolve release aliases (e.g., “latest”, pinned tags) deterministically.

### 2️⃣ Use Stable API Endpoints

Example canonical endpoint:

~~~http
GET /api/entities/{entityId}/diff?from={R_prev}&to={R_curr}
~~~

All endpoint changes must be versioned and correspond to schema changes.

### 3️⃣ Apply Triple-Layer Validation

- **Network-level**:
  - HTTP errors  
  - timeouts  
  - stale cache / version mismatches  

- **Schema-level**:
  - JSON shape  
  - field types  
  - presence of required governance fields  

- **Domain-level**:
  - relation types & constraints  
  - severity rules  
  - required redaction logic hooks  

Only after all three layers pass is the diff accepted.

### 4️⃣ Enforce FAIR+CARE Masking

- Remove or mask restricted relation targets (IDs not exposed to UI when blocked)  
- Redact sensitive text content (replacing with governed placeholders)  
- Obfuscate sovereign entity identifiers where required by policy  
- Apply CARE token adjustments (e.g., `restricted` → block or generalize)  

#### CARE Masking Pipeline

~~~mermaid
flowchart TD
    META[Raw Diff Metadata] --> CAREPROC[CARE Processor]
    CAREPROC --> MASK[Mask · Redact · Obfuscate]
    MASK --> SAFE[CARE-Safe Diff Model]
~~~

### 5️⃣ Build Provenance-Rich Responses

`diffClient` must retain:

- Provenance lineage (input releases, source counts, pipeline IDs)  
- Dataset references (STAC/DCAT IDs used to derive changes)  
- Checksum metadata (when available)  
- Release identifiers (`releasePrev`, `releaseCurr`) and timestamps  
- Story Node links (if entity has narrative representation)  

### 6️⃣ Attach Telemetry Fields

The service should collaborate with telemetry hooks to record:

- `diff_fetch_ms`  
- `diff_parse_ms`  
- `governance_deltas` count  
- `explainability_drift_detected` flag  
- `energy_estimate_wh` (from pipeline metrics)  
- `a11y_path_validated` (flag when A11y path is verified downstream)  

Telemetry is appended (via telemetry pipeline) to:

~~~text
../../../../../releases/v11.2.2/web-entity-diff-services-telemetry.json
~~~

---

## 🔐 FAIR+CARE Governance Enforcement

The diff service must implement:

- CARE tag propagation and enforcement  
- Restricted-content suppression for sensitive datasets or relations  
- Sovereignty protection (e.g., masking geography connected to Indigenous/tribal data)  
- Consent-flag tracking and change detection  
- License-change detection and surface-of-impact calculation  
- Lineage continuity alerts for datasets/entities  

Governance comparator:

~~~mermaid
flowchart LR
    PREV["R_prev Governance"] --> GCOMP[Governance Comparator]
    CURR["R_curr Governance"] --> GCOMP
    GCOMP --> GDIFF["GovernanceChange<br/>CARE · license · consent · sovereignty"]
~~~

Governance output is always merged into the final diff model returned to callers.

Governance-specific logs may be written downstream to:

~~~text
../../../../../docs/reports/audit/web-entity-diff-services-governance.json
~~~

---

## ♿ Accessibility Integration (WCAG 2.1 AA)

While `diffClient` itself is not UI, it must:

- Return diff structures that are **safe and structured for A11y**:
  - Text diffs safe for screen readers (no raw ANSI; only structured text changes)  
  - Labels and keys that can be mapped to accessible descriptions in UI  
- Not rely on color or presentational hints; all semantics must be in data fields usable by UI.

Conceptual A11y normalization:

~~~mermaid
flowchart TD
    RAWTXT[Raw Text Diff] --> A11YTXT[Accessible Normalizer<br/>(in model/normalizer layer)]
    A11YTXT --> UI[Diff Components]
~~~

The service cooperates with model/normalization code to ensure accessible-ready diff data.

---

## 🌱 Sustainability Considerations

Services MUST:

- Minimize payload sizes (no unused fields, no redundant data)  
- Avoid unnecessary recomputation (use ephemeral caching where safe)  
- Cache results **ethically**:
  - ephemeral in-memory per session  
  - no long-term storage of sensitive diff payloads  
- Reduce parsing overhead via stable schema and streaming if needed  
- Include energy estimation metadata (sourced from pipeline telemetry, not guessed ad hoc)  

These metrics feed sustainability dashboards and are essential to KFM’s sustainability commitments.

---

## ⚙️ CI / Validation Requirements

**Validation layers:**

| Validation Layer       | Workflow / Tool             |
|------------------------|----------------------------|
| Schema integrity       | `schema-validate.yml`      |
| CARE enforcement       | `faircare-validate.yml`    |
| Provenance continuity  | lineage validator pipelines|
| A11y metadata presence | `accessibility_scan.yml`   |
| Telemetry correctness  | `telemetry-export.yml`     |
| Security               | CodeQL + Trivy             |
| Documentation          | `docs-lint.yml`            |

CI requires **100% clean** governance, schema, and telemetry validation before merge.

---

## 🧾 Example Service Metadata Record

~~~json
{
  "id": "entity_diff_services_v11.2.2",
  "requests_handled": 73210,
  "cache_hit_rate": 0.47,
  "governance_deltas_detected": 2450,
  "care_warnings_triggered": 131,
  "explainability_drift_events": 53,
  "avg_fetch_ms": 72.3,
  "energy_use_wh": 0.49,
  "telemetry_synced": true,
  "checksum_verified": true,
  "timestamp": "2025-11-30T23:58:00Z"
}
~~~

This is an example **service-level telemetry/metadata record**, not a runtime API response.

---

## 🕰 Version History

| Version | Date       | Summary                                                                                                                                                                   |
|--------:|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Upgraded to KFM-MDP v11.2.2; added telemetry v2, FAIR+CARE v11 semantics, energy/carbon tracking, and stricter governance + masking flows in diffClient.                  |
| v10.3.2 | 2025-11-14 | Deep architecture version added — CARE masking pipeline, provenance continuity, explainability delta support, sustainability metrics, and MCP-DL v6.3 validation.        |

---

## ⚖️ Footer

<div align="center">

**Kansas Frontier Matrix — Diff-First Services Architecture**  
🛰️ X-Release Diff Intelligence · 🔐 FAIR+CARE Compliance · 🔗 Provenance Fidelity · 🌱 Sustainable Fetching  

[Back to Diff-First Module](../README.md) •  
[Docs Root](../../../../README.md) •  
[Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

© 2025 Kansas Frontier Matrix — MIT License  

**End of Document**

</div>
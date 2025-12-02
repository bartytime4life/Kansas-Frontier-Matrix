---
title: "⚡🌍 KFM v11 — Energy → kWh → CO₂e Conversion Ledger (FAIR+CARE · OTel-Compliant)"
description: "Canonical, deterministic Joules → kWh → kg CO₂e conversion rules and metadata standard for all KFM v11 energy/carbon telemetry."
path: "docs/energy/conversion/README.md"
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Energy & Carbon Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x conversion-safe"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../releases/v11.2.3/energy-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/energy-carbon-v2.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Energy/Carbon Conversion Ledger"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "energy"
  applies_to:
    - "energy-conversion-ledger"
    - "telemetry-normalization"
    - "carbon-accounting"

semantic_intent:
  - "standard"
  - "governance"
  - "telemetry"
category: "Documentation · Standard · Energy/Carbon"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: false

data_steward: "Energy & Carbon Council · Telemetry WG"
ttl_policy: "24 months"
sunset_policy: "Supersedes v11.2.2 energy ledger spec"

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
  - "docs/energy/conversion/README.md@v11.2.2"
  - "docs/energy/conversion/README.md@v11.2.1"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/docs-energy-conversion-ledger-v11.2.3.schema.json"
shape_schema_ref: "schemas/shacl/docs-energy-conversion-ledger-v11.2.3-shape.ttl"
story_node_refs: []

immutability_status: "mutable"

doc_uuid: "urn:kfm:doc:energy:conversion-ledger:v11.2.3"
semantic_document_id: "kfm-energy-co2e-ledger-v11.2.3"
event_source_id: "ledger:kfm:doc:energy:conversion-ledger:v11.2.3"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

transform_registry:
  allowed:
    - "summary"
    - "timeline-generation"
    - "semantic-highlighting"
    - "a11y-adaptations"
    - "diagram-extraction"
    - "metadata-extraction"
  prohibited:
    - "content-alteration"
    - "speculative-additions"
    - "unverified-architectural-claims"
    - "narrative-fabrication"
    - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "footer-check"
  - "accessibility-check"
  - "diagram-check"
  - "metadata-check"
  - "provenance-check"
---

<div align="center">

# ⚡🌍 KFM v11 — Energy → kWh → CO₂e Conversion Ledger  

`docs/energy/conversion/README.md`  

**Purpose:**  
Define the canonical, deterministic Joules → kWh → kg CO₂e conversion rules and metadata contract for all governed KFM v11 pipelines and telemetry.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue "Master Coder Protocol v6.3")]() ·
[![KFM-MDP v11.2.2](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.2-informational "Markdown Protocol v11.2.2")]() ·
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold "FAIR+CARE Compliant")]() ·
[![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen "Status: Active & Enforced")]()

</div>

---

## 📘 Overview

### Scope

This document defines the **governed energy & carbon conversion ledger** used across KFM v11:

- Normalizes **energy.joules** (J) → **energy.kwh** (kWh)
- Converts **energy.kwh** → **carbon.kg_co2e** (kg CO₂e)
- Binds each conversion to:
  - Region-specific emission factor (`factor`, kg CO₂e / kWh)
  - Source span / event ID (`source_span_id`)
  - Provenance and schema version

It is the **single source of truth** for:

- AI inference and training telemetry
- ETL and scheduler compute job energy reporting
- STAC/DCAT dataset-level energy & carbon metadata
- Global KFM carbon ledger and Story Nodes that expose emissions

### Design Goals

- **Deterministic**: Same input Joules + region + factor ⇒ same kWh and kg CO₂e.
- **Reproducible**: Conversion logic is config- and schema-driven, not ad-hoc.
- **Auditable**: Every record carries region, factor, schema, and provenance.
- **Interoperable**: Aligned with STAC 1.0.0, DCAT 3.0, PROV-O, OWL-Time.
- **Governed**: Factors locked and versioned by the Energy & Carbon Council.

---

## 🗂️ Directory Layout

~~~text
docs/energy/conversion/
├── 📄 README.md                         # Canonical ledger spec (this file)
│
├── 🔢 constants/                        # Physical constants & factors
│   ├── 📄 joules-to-kwh.md              # 1 kWh = 3,600,000 J definition + rationale
│   └── 📄 egrid-factors.md              # eGRID subregion emission factors (versioned)
│
├── 🧮 formulas/                         # Language-agnostic conversion math
│   ├── 📄 energy-to-kwh.md              # J → kWh pipeline rule
│   └── 📄 kwh-to-co2e.md                # kWh → kg CO₂e via regional factor
│
├── 📊 examples/                         # Worked examples and validation cases
│   ├── 📄 sample-span.md                # OTel span → normalized CO₂e record
│   └── 📄 daily-pipeline.md             # Daily aggregation into the ledger
│
└── 🧪 tests/                            # Canonical test vectors for CI
    ├── inputs.json                      # Input test events (J, region, factor, metadata)
    └── expected.json                    # Golden outputs (kWh, kg_co2e, factor, region)
~~~

---

## 🧭 Context

### Upstream

Typical producers of `energy.*` / `carbon.*` events:

- **OpenTelemetry spans**
  - Span attributes like `energy.watt_seconds` or `energy.joules`
  - `span_id` and `trace_id` used as `source_span_id`
- **Scheduler / infra telemetry**
  - Compute job runtimes, power counters, energy summaries
- **Batch ETL**
  - Aggregated Joule tallies by pipeline/day/cluster

All upstream producers must normalize to **SI Joules** before J → kWh conversion.

### Downstream

Ledger outputs are consumed by:

- Time-series stores and warehouses (ledger tables/streams)
- Neo4j knowledge graph nodes/relationships for compute runs and datasets
- STAC/DCAT metadata for energy/carbon-rich assets
- Global carbon ledger dashboards and Story Nodes

This README defines the **semantic and numeric contract** that all implementations must honor.

---

## 🧠 Story Node & Focus Mode Integration

When Story Nodes or Focus Mode surfaces energy/carbon metrics:

1. **Ledger is truth**  
   Story Nodes treat `energy.kwh` and `carbon.kg_co2e` as **already normalized**. No further rescaling.

2. **Key fields**

   - `energy.joules`
   - `energy.kwh`
   - `carbon.kg_co2e`
   - `region`
   - `factor`
   - `schema_version`
   - `provenance`
   - `source_span_id`

3. **Narrative guardrails**

   - No per-person blame; only system/pipeline-level metrics.
   - Highlight uncertainty when factors change between versions.
   - Expose region and factor (e.g. “Midwest eGRID factor vY”) in detailed views.

4. **Graph mapping**

   - Convert ledger rows to graph nodes/edges using CIDOC-CRM + PROV-O:
     - `:EnergyConversionActivity` (prov:Activity)
     - `:EnergyTelemetrySpan` / `:ComputeRun` (geo:Feature-like event)
     - `:EmissionFactorRegion` (geo:Feature)
   - Use OWL-Time for time intervals and PROV-O for lineage.

---

## 🧪 Validation & CI/CD

All changes to the ledger spec, constants, or factors must pass CI:

1. **Vector tests**

   - `tests/inputs.json` + `tests/expected.json` define canonical cases.
   - All language implementations (Go, Python, TypeScript, etc.) must:
     - Load inputs
     - Run conversion
     - Match expected values within agreed tolerances.

2. **Constant integrity**

   - `constants/joules-to-kwh.md` must encode `1 kWh = 3_600_000 J`.
   - `constants/egrid-factors.md` must:
     - Provide non-negative factors
     - Avoid duplicate region codes
     - Document source (year, EPA table) and version.

3. **Schema checks**

   - All sample events and examples must validate against:
     - `schemas/telemetry/energy-carbon-v2.json`
   - GitHub Actions run schema-lint and metadata-check for this doc and examples.

4. **Determinism**

   - Conversion implementations must:
     - Avoid randomness or hidden side effects
     - Be pure functions of (joules, region, factor, config).

5. **CI wiring**

   - CI workflow: `.github/workflows/kfm-ci.yml`
   - Failing any of:
     - `markdown-lint`, `schema-lint`, `metadata-check`, `provenance-check`
     - or language-specific test suites
   - → blocks merge to governed branches.

---

## 📦 Data & Metadata

Each conversion event MUST include at minimum:

| Field              | Type      | Unit        | Description                                             | Required |
|--------------------|-----------|------------|---------------------------------------------------------|----------|
| `energy.joules`    | float     | J          | Raw SI Joules from upstream telemetry.                  | Yes      |
| `energy.kwh`       | float     | kWh        | `energy.joules / 3_600_000`.                            | Yes      |
| `carbon.kg_co2e`   | float     | kg CO₂e    | `energy.kwh * factor`.                                  | Yes      |
| `region`           | string    | —          | eGRID subregion or governed region key.                 | Yes      |
| `factor`           | float     | kg/kWh     | Emission factor for `region` (kg CO₂e per kWh).         | Yes      |
| `provenance`       | string/IRI| —          | PROV-O lineage pointer (activity or pipeline run).      | Yes      |
| `source_span_id`   | string    | —          | Upstream OTel span ID or equivalent event ID.           | Yes      |
| `schema_version`   | string    | —          | Telemetry schema tag (e.g. `"energy-carbon-v2"`).       | Yes      |

### Field constraints

- **Units**
  - `energy.joules` MUST be in Joules, no implicit prefix.
  - `energy.kwh` MUST be in kWh (not Wh, not MWh).
- **Factor selection**
  - `factor` MUST be pulled from the currently-approved eGRID factor table for the event’s `region`.
  - If `region` cannot be determined deterministically, event MUST NOT be emitted as governed ledger output.
- **Provenance**
  - `provenance` SHOULD be a resolvable PROV-O record describing:
    - Inputs, activity, agent, and configuration.

---

## 🧱 Architecture

### Canonical equations

1. **Joules → kWh**

```text
energy.kwh = energy.joules / 3_600_000
```

2. **kWh → kg CO₂e**

```text
carbon.kg_co2e = energy.kwh * factor
```

where:

- `factor` is the region-specific kg CO₂e per kWh.

### Implementation contract

All implementations MUST:

- Expose a stable entrypoint, e.g.:

  - `@kfm/energy/convert-v11` (TS/JS)
  - `kfm_energy_convert_v11` (Python/Go/Bash wrappers)

- Accept input with at least:

  - `energy.joules`
  - `region`
  - `factor` (or derive factor from `region` and factor table)
  - `source_span_id`
  - `schema_version`

- Emit outputs conforming to **📦 Data & Metadata** contract.

### Error handling

- If `factor` lookup fails (unknown region or missing factor):
  - Do NOT emit governed ledger event.
  - Emit a structured error/diagnostic event with:
    - Region value
    - Timestamp
    - Upstream span ID
- If numeric overflow/NaN occurs:
  - Treat as fatal for that event; log and drop, do not emit partial records.

---

## ⚖ FAIR+CARE & Governance

- **FAIR**
  - **Findable**: Ledger events indexed by `source_span_id`, `region`, `schema_version`, and time.
  - **Accessible**: Exposed via governed APIs and STAC/DCAT catalogs where appropriate.
  - **Interoperable**: Units and field names harmonized across KFM telemetry.
  - **Reusable**: Documented factors, equations, and version history.

- **CARE**
  - System-level emissions; avoid per-person blame.
  - Respect Indigenous and community data sovereignty where energy data intersects sensitive infrastructure or land.

- **Governance**

  - Energy & Carbon Council:
    - Owns factor updates and ledger equation changes.
    - Approves new regions or special-case factors.
  - Any change to:
    - `constants/`, `formulas/`, `tests/`
    - This README
    - Telemetry schema for energy/carbon
  - MUST go through governance review and CI sign-off.

---

## 🕰️ Version History

| Version      | Date       | Summary                                                   |
|-------------|------------|-----------------------------------------------------------|
| v11.2.3     | 2025-12-02 | Aligned with KFM-MDP v11.2.2; clarified field contract.   |
| v11.2.2     | 2025-12-01 | Initial governed energy → CO₂e conversion ledger spec.    |

<div align="center">

⚡🌍 **KFM v11 — Energy → kWh → CO₂e Conversion Ledger**  
Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence  

[📘 Docs Root](../../..) · [📂 Standards Index](../../standards/README.md) · [⚖ Governance](../../standards/governance/ROOT-GOVERNANCE.md)

</div>
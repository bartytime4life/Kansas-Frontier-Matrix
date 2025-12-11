---
title: "🛰️ Kansas Frontier Matrix — JPSS Remote-Sensing Event Index"
path: "docs/events/remote-sensing/jpss/README.md"
version: "v11.2.6"
last_updated: "2025-12-11"

release_stage: "Stable / Governed"
lifecycle: "Active"
review_cycle: "Annual · Remote-Sensing Council"
content_stability: "stable"
status: "Active / Canonical"

doc_kind: "Event Index"
intent: "jpss-remote-sensing-event-registry"
semantic_document_id: "kfm-doc-events-remote-sensing-jpss-index-v11.2.6"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.6/remote-sensing-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/remote-sensing-v11.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

heading_registry:
  approved_h2:
    - "1. Scope and role in the KFM pipeline"
    - "2. Directory layout (JPSS event docs)"
    - "3. Event modeling conventions"
    - "4. Integration with ETL, catalogs, and graph"
    - "5. Telemetry, QA, and reproducibility"
    - "6. Story Nodes and Focus Mode"
    - "7. Governance, FAIR+CARE, and sovereignty"
    - "8. Version history"
    - "9. Footer"

doc_uuid: "urn:kfm:events:remote-sensing:jpss:index:v11.2.6"
---

<div align="center">

# 🛰️ JPSS Remote-Sensing Events — KFM Index  
`docs/events/remote-sensing/jpss/`

**Purpose:** Canonical index and governance contract for **NOAA JPSS–related remote-sensing event docs**  
that materially affect KFM pipelines, catalogs, graph state, and downstream Story Nodes / Focus Mode.

</div>

---

## 1. Scope and role in the KFM pipeline

This directory defines how **JPSS operational events** (algorithm transitions, reprocessing campaigns,  
major outages, sensor anomalies, calibration epoch changes, etc.) are represented inside the standard  
Kansas Frontier Matrix pipeline:

Deterministic ETL  
→ STAC / DCAT / PROV catalogs  
→ Neo4j graph  
→ API layer  
→ React / MapLibre / Cesium frontends  
→ Story Nodes and Focus Mode.

In particular, this index governs:

- Which JPSS events are documented as **KFM event records**.  
- The **file layout and naming conventions** for those event records.  
- How event records are linked into:
  - ETL configs and calibration ledgers.  
  - STAC/DCAT metadata and PROV bundles.  
  - The Neo4j graph (e.g., algorithm updates and sensor streams).  
  - Focus Mode and Story Node narratives where appropriate.

This README is **domain-generic** for JPSS; individual events (for example,  
`2025-12-11-idps-block-2.3-mx15.md`) provide **frozen historical records** for specific changes.

---

## 2. Directory layout (JPSS event docs)

Emoji-enriched, CI-safe layout for this module, using the outer-backticks / inner-tilde fencing profile.

~~~text
📂 docs/
└── 📂 events/
    └── 📂 remote-sensing/
        ├── 📄 README.md                     # Remote-sensing events root index (multi-mission)
        └── 📂 jpss/
            ├── 📄 README.md                 # This file – JPSS-specific event index & governance
            │
            ├── 📂 _templates/               # Authoring templates for new JPSS event records
            │   └── 📄 event-summary-template.md
            │
            ├── 📂 _archive/                 # Deprecated / superseded event docs (kept for lineage)
            │   └── 📄 <older-event>.md
            │
            └── 📂 2025/
                └── 📄 2025-12-11-idps-block-2.3-mx15.md
                                            # Example: IDPS Block 2.3 Mx15 algorithm transition (frozen)
~~~

Conventions:

- **One directory per calendar year** under `jpss/` (e.g., `2025/`), containing dated event markdown files.  
- **Event files are immutable historical records** once marked frozen; corrections require a new version ID.  
- `_templates/` is the **only place** to add authoring templates; `_archive/` holds retired or superseded docs.  
- Any structural change here must update this README and pass **markdown + link validation** in CI.

---

## 3. Event modeling conventions

Each JPSS event markdown file:

- Lives under `docs/events/remote-sensing/jpss/<YYYY>/`.  
- Uses `doc_kind: "Event Summary"` and `status: "Historical Event Record"` in front matter.  
- Is **time-bounded** (single instant or interval) and **pipeline-relevant**.

### 3.1 File naming

Pattern:

- `YYYY-MM-DD-<system>-<short-id>.md`

Examples:

- `2025-12-11-idps-block-2.3-mx15.md`  
- `2026-03-04-jpss-1-atms-safe-mode-entry.md`  
- `2026-07-15-jpss-viirs-cloud-reprocessing-r1.md`

Requirements:

- `YYYY-MM-DD` in **UTC**, matching the event’s primary operational timestamp.  
- `<system>` is a stable short tag (e.g., `idps`, `jpss-1`, `jpss-2`, `ground-segment`).  
- `<short-id>` is a concise, human-readable slug stable across data, graph, and docs.

### 3.2 Semantic content

Each Event Summary must, at minimum, include:

- **Overview** — context, responsible agency, short description.  
- **Operational impact** — which product classes / streams are affected (e.g., ATMS SDR, VIIRS EDR).  
- **KFM impact** — which ETL jobs, catalog entries, and graph entities are affected.  
- **PROV lineage capsule** — identifying the primary `prov:Activity`, `prov:Entities`, and `prov:Agents`.  
- **Downstream notes** — requirements for harmonization, reprocessing, or Story Node updates.

Where relevant, events should:

- Name **algorithm versions** (e.g., `"Mx15"`) exactly as used in STAC/DCAT/graph properties.  
- Capture **calibration epochs** (e.g., `calibration_epoch = 2025-12-11T16:30Z`).  
- Reference upstream **bulletins or administrative messages** by ID and date.

---

## 4. Integration with ETL, catalogs, and graph

JPSS events exist in docs, but they are **live, first-class references** in the data pipeline.

### 4.1 ETL integration

- ETL configs under `configs/remote-sensing/jpss/` **must reference** event IDs for any change that:
  - Alters calibration, geolocation, or algorithm behavior.  
  - Introduces or retires a data stream.  
  - Triggers reprocessing campaigns or backfills.

Minimum expectations:

- An `event_id` and `event_doc_path` field in ETL configs pointing at the markdown record.  
- A calibration ledger entry under `data/work/remote-sensing/calibration-ledger/` keyed by event ID.  
- Deterministic, config-driven behavior; no implicit “magic” transitions.

### 4.2 STAC / DCAT / PROV

For asset-level metadata:

- **STAC Items** representing SDR/EDR products across an epoch boundary MUST:
  - Include properties such as `processing:software.version`, `processing:lineage`,  
    `kfm:event_id`, and `kfm:calibration_epoch`.  
- **DCAT datasets** tracking JPSS-derived products MUST update:
  - Dataset version fields (e.g., `v11.2.6-rs.1`).  
  - `dct:provenance`, `dct:source`, and change notes referencing event IDs.  
- **PROV bundles**:
  - Represent the event as a `prov:Activity` (e.g., `jpss-idps-block2.3-mx15-transition`).  
  - Connect that activity to:
    - Upstream announcements and bulletins (`prov:used`).  
    - New or updated product series (`prov:generated`).  
    - Responsible organizations (`prov:wasAssociatedWith`).

### 4.3 Graph model (Neo4j)

The Neo4j graph stores JPSS events in the **operations / remote-sensing** portion of the KFM-OP ontology.

Typical pattern (conceptual, not a full schema):

- `:AlgorithmUpdate`, `:SensorStream`, `:CalibrationEpoch`, `:EventDocument`.  
- Relationships such as:
  - `(:AlgorithmUpdate)-[:UPDATES]->(:SensorStream)`  
  - `(:CalibrationEpoch)-[:DEFINED_BY]->(:AlgorithmUpdate)`  
  - `(:EventDocument)-[:DESCRIBES]->(:AlgorithmUpdate)`  

Graph ingestion code in `src/graph/remote-sensing/` must:

- Use IDs derived from **event doc front matter**, not ad hoc strings.  
- Include unit tests under `src/graph/remote-sensing/tests/` that exercise queries across:
  - Time boundaries (pre / post event).  
  - Affected sensors and derived products.  
  - Links back to the markdown event records.

---

## 5. Telemetry, QA, and reproducibility

The JPSS event domain participates in KFM’s telemetry and reliability framework.

Each event that changes operational behavior MUST:

- Emit structured telemetry consistent with `remote-sensing-telemetry.json` and  
  `remote-sensing-v11.json`, including:
  - `run_id`, `job_name`, and environment identifiers.  
  - `latency_ms`, error counts, and error budget usage.  
  - `energy_wh` and `carbon_ug` where available.  
- Be recorded in `mcp/experiments/remote-sensing/` with:
  - Config snapshot hashes.  
  - STAC/DCAT validation reports.  
  - Key QA metrics (e.g., bias, noise metrics across the transition).

Reproducibility expectations:

- Re-running the same ETL with the same inputs and configs MUST produce bitwise-identical outputs.  
- OpenLineage events MUST be emitted for significant transitions, enabling end-to-end lineage from:
  - Upstream archives → KFM ETL → catalogs → graph → Focus Mode narratives.

---

## 6. Story Nodes and Focus Mode

JPSS events are **global operational changes** with local consequences for Kansas.  
They can drive Story Nodes and Focus Mode only when their effects are traceable in KFM data.

### 6.1 Story Nodes

When a JPSS event has clear, Kansas-relevant implications (for example, a calibration shift that  
changes precipitation or soil moisture products over Kansas), authors may create Story Nodes under:

- `docs/story/remote-sensing/`  
- or cross-domain where appropriate (e.g., hydrology, agriculture, climate).

Each such Story Node must:

- Cite the JPSS event’s **semantic document ID** from this directory.  
- Distinguish between:
  - **Facts**: timestamps, algorithm versions, product changes.  
  - **Interpretation**: how those changes affect Kansas analyses.  
  - **Speculation**: what might happen next, clearly labeled or omitted.  
- Link to:
  - Relevant STAC Collections / Items.  
  - Affected graph entities (e.g., `SensorStream`, `AlgorithmUpdate`).  
  - This README and the specific event markdown file.

### 6.2 Focus Mode

Focus Mode may:

- Surface JPSS events as **timeline markers** when visualizing remote-sensing products over Kansas.  
- Expose a short, non-speculative summary in side panels (e.g.,  
  “ATMS algorithm update Mx15 applied at 2025-12-11T16:30Z; calibration baselines shifted”).  
- Provide links back to:
  - The relevant Event Summary file.  
  - Any Story Nodes built on top of that event.

Focus Mode must **not**:

- Infer speculative causal stories from algorithm changes alone.  
- Hide the fact that a change in data behavior is due to **upstream system changes** rather than  
  geophysical phenomena.

---

## 7. Governance, FAIR+CARE, and sovereignty

JPSS events concern **global satellite systems**, but KFM uses them in a Kansas-focused,  
FAIR+CARE-aligned context.

Requirements:

- **FAIR**:
  - Event docs are findable under this index with stable IDs and paths.  
  - Access policies for derived data (especially higher-level products) are documented.  
  - Standard schemas (STAC/DCAT/PROV) and open formats are used.  
- **CARE**:
  - Event narratives must consider downstream use in analyses that could affect communities  
    (e.g., agriculture, water resources, environmental justice).  
  - When JPSS-driven changes materially alter conclusions for sensitive domains, governance  
    processes must be engaged, and Story Nodes should reflect the uncertainty and context.  
- **Sovereignty**:
  - Where JPSS-derived products intersect with Indigenous territories or sensitive land uses,  
    data governance decisions for those layers take precedence over opportunistic visualization.  
  - Event docs themselves are generally **non-sensitive**, but their implications for derived  
    layers may be subject to sovereignty agreements documented elsewhere in the repo.

If there is any uncertainty about how to represent or communicate the impact of a JPSS event,  
the default is conservative: escalate to the Remote-Sensing Council and relevant governance bodies  
before treating a dataset as production-ready.

---

## 8. Version history

| Version  | Date       | Author        | Notes                                                |
|----------|------------|--------------|------------------------------------------------------|
| v11.2.6  | 2025-12-11 | `<your-name>` | Initial JPSS event index aligned with KFM-MDP 11.2.6 |

Update this table whenever structure or governance semantics change, and ensure any breaking change  
is accompanied by corresponding updates to ETL configs, schemas, and tests.

---

## 9. Footer

<div align="center">

**🔗 KFM Documentation Navigation**  
[⬅️ Remote-Sensing Events Index](../README.md) •  
[📚 Architecture Overview](../../../architecture/README.md) •  
[📐 Standards Index](../../../standards/INDEX.md) •  
[🛡 Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md)

**End of Document**

</div>
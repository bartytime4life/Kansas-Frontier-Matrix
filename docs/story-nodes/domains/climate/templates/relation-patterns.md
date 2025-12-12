---
title: "🌦️ KFM v11.2.6 — Climate Story Node Relation Patterns (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/story-nodes/domains/climate/templates/relation-patterns.md"
version: "v11.2.6"
last_updated: "2025-12-12"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Climate Systems Board · FAIR+CARE Council · AI Attribution Governance Board"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Relation Pattern Guide"
header_profile: "standard"
footer_profile: "standard"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:doc:storynodes:domains:climate:templates:relation-patterns:v11.2.6"
semantic_document_id: "kfm-storynodes-climate-relation-patterns-v11.2.6"
event_source_id: "ledger:docs/story-nodes/domains/climate/templates/relation-patterns.md"
immutability_status: "version-pinned"

sbom_ref: "../../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.6/storynode-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/storynodes-v11.json"
schema_ref: "../../../../../schemas/json/story-node.schema.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"

domain: "climate"
intent: "kfm-climate-storynode-relation-patterns"
lifecycle_stage: "stable"

fair_category: "F1-A2-I2-R2"
care_label: "Environmental · Attribution-Sensitive"
classification: "Public-Safe"
jurisdiction: "Kansas / United States"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "narrative-fabrication"
  - "governance-override"

ttl_policy: "36 months"
sunset_policy: "Superseded by v12 climate relation pattern library"
---

<div align="center">

# 🌦️ **Climate Story Node — Relation Patterns (KFM v11.2.6)**  
### *Safe Graph Modeling for Events, Datasets, Models, Indices, and Attribution*  

`docs/story-nodes/domains/climate/templates/relation-patterns.md`

**Purpose**  
Define the **canonical, governed relation patterns** used by Climate Story Nodes to connect:
events ↔ datasets ↔ model runs ↔ derived products ↔ documents ↔ analogs ↔ attribution evidence  
in a way that is **schema-consistent**, **scientifically precise**, and **attribution-safe**.

</div>

---

## 📘 Overview

Climate Story Nodes rely on relations to:

- link **events** to the **observations** and **datasets** that support them,
- link **derived products** to their upstream sources (PROV-like graph lineage),
- connect **historical analogs** without implying causality,
- attach **attribution evidence** only when supported and reviewed,
- support Focus Mode exploration across:
  - event timelines,
  - dataset collections,
  - model/reanalysis families,
  - derived indices and summaries.

Relations are **normative**. Use only approved `rel` values in this guide unless governance approves additions.

---

## 🚫 Prohibited Relation Behaviors

Do **not** use relations to:

- imply causal claims (“caused-by”) without peer-reviewed attribution evidence,
- link to private datasets or non-public model configs,
- link to person-level impact records,
- link to sensitive infrastructure targets.

If you need something not covered, file a governance proposal.

---

## 🧠 Relation Principles (Normative)

1. **Exactly one `about`** per Story Node.
2. **Observations vs Model output** must be reflected in relation choice:
   - observations and public measurement datasets → `derived-from` and/or `references`
   - model/reanalysis sources → `derived-from` (with narrative clarifying “model”)
3. **Attribution** requires:
   - `attribution-evidence` relation to a study/assessment entity (public and citable),
   - narrative confidence statement,
   - no overreach beyond evidence.
4. All targets must be **public-safe** identifiers.

---

## 🔗 Relation Pattern Library

Each pattern includes:

- `rel` value (required)
- meaning
- usage rules (normative)
- example snippet (JSON)

> Note: ID namespaces are illustrative. Use your repo’s canonical ID schemes (`event:`, `dataset:`, `doc:`, `stac:`, `prov:`, etc.).

---

## 🧱 1) Primary Topic

### `rel: "about"`
**Meaning:** The Story Node’s primary subject (a climate event, trend, or phenomenon).  
**Rules (normative):**
- Exactly one per node.
- Target should be an **event** or **phenomenon** entity, not a dataset.

**Example**
~~~json
{ "rel": "about", "id": "event:climate:ks:heatwave:2022-06" }
~~~

---

## 📚 2) Documents and Narrative Sources

### `rel: "references"`
**Meaning:** Supporting narrative evidence: reports, advisories, assessments, papers.  
**Rules (normative):**
- Use for documents that support claims.
- Do not use for raw data sources (prefer `derived-from` for datasets).

**Example**
~~~json
{ "rel": "references", "id": "doc:noaa:ncei:climate-summary-2022-06" }
~~~

---

## 🧪 3) Data Lineage and Inputs

### `rel: "derived-from"`
**Meaning:** The node’s claims or derived products are based on this dataset/model/reanalysis/observation source.  
**Rules (normative):**
- Use for:
  - NEXRAD composites,
  - GOES imagery products,
  - ERA5,
  - HRRR outputs,
  - station aggregates,
  - gridded analyses.
- If linking to STAC items, prefer `stac:<collection>/<item>` IDs when available.

**Example**
~~~json
{ "rel": "derived-from", "id": "dataset:era5:reanalysis" }
~~~

**Example (STAC)**
~~~json
{ "rel": "derived-from", "id": "stac:kfm-climate-era5/items/2022-06-heat-anom" }
~~~

---

## 🧾 4) Produced Outputs (Artifacts / Derived Assets)

### `rel: "produced"`
**Meaning:** This Story Node corresponds to, or produced, a derived artifact/asset (e.g., anomaly raster, index time-series, summary parquet).  
**Rules (normative):**
- Use only when the artifact exists and is addressable.
- Pair with provenance notes in narrative or PROV metadata.

**Example**
~~~json
{ "rel": "produced", "id": "asset:climate:ks:2022-06:t2m_anomaly_raster" }
~~~

---

## ⏱️ 5) Temporal Continuity and Sequences

### `rel: "preceded-by"` / `rel: "followed-by"`
**Meaning:** Relationship between events in a sequence without implying causality.  
**Rules (normative):**
- Use for multi-episode events (heatwave phases, drought progression).
- Do not use to claim one caused the other; explain in narrative.

**Example**
~~~json
{ "rel": "preceded-by", "id": "event:climate:ks:heatwave:2022-06-early" }
~~~

---

## 🧭 6) Spatial Context (Coarse-Scale Only)

### `rel: "located-in"`
**Meaning:** The event or phenomenon occurred within a generalized region.  
**Rules (normative):**
- Coarse region/watershed/county set only.
- Avoid over-precision for sensitive contexts (rare in climate, but still possible for infrastructure).

**Example**
~~~json
{ "rel": "located-in", "id": "region:kansas" }
~~~

---

## 🧊 7) Teleconnection and Driver Context (Non-Causal)

### `rel: "associated-with"`
**Meaning:** A contextual association (e.g., a blocking pattern, ENSO phase) without asserting causation.  
**Rules (normative):**
- Use when describing co-occurrence or background climate state.
- If a stronger claim is needed, support it with `references` and cautious language.

**Example**
~~~json
{ "rel": "associated-with", "id": "phenomenon:teleconnection:enso:la-nina" }
~~~

---

## 🧷 8) Analog Events (Comparison Without Causality)

### `rel: "analog-of"`
**Meaning:** The event resembles another event in some aspects (pattern, magnitude range, seasonality).  
**Rules (normative):**
- Must specify comparison basis in narrative (which variables, which metrics).
- Do not imply recurrence or deterministic behavior.

**Example**
~~~json
{ "rel": "analog-of", "id": "event:climate:us:heatwave:1936" }
~~~

---

## 🧠 9) Attribution Evidence (Strictly Controlled)

### `rel: "attribution-evidence"`
**Meaning:** Links to a formal attribution study, assessment, or evidence entity used for attribution statements.  
**Rules (normative):**
- Required **if and only if** the node includes attribution claims.
- Target must be a public, citable study/assessment.
- Must include confidence and limitations in narrative.
- This relation does **not** imply certainty; it provides the evidence pointer.

**Example**
~~~json
{ "rel": "attribution-evidence", "id": "doc:peer-reviewed:attribution:heat-extremes-central-plains-2023" }
~~~

---

## 🛡️ 10) Governance / Review Requirements

### `rel: "requires-review"`
**Meaning:** Flags that this node requires explicit reviewer sign-off (domain board, attribution specialist, governance).  
**Rules (normative):**
- Use for any node containing:
  - attribution statements,
  - high-impact claims,
  - contentious interpretation,
  - novel derived metrics.
- CI may enforce this for certain tags.

**Example**
~~~json
{ "rel": "requires-review", "id": "policy:climate-attribution-governance" }
~~~

---

## 🧩 Valid Relation Matrix (Quick Reference)

~~~text
about                 → event, phenomenon (exactly one)
references            → reports, papers, advisories, assessments
derived-from          → datasets, observations, reanalysis, model outputs, STAC items
produced              → derived artifacts/assets (rasters, indices, summaries)
preceded-by/followed-by → event phases/episodes (sequence without causality)
located-in            → regions, watersheds, county sets (coarse only)
associated-with       → teleconnections / background states (non-causal)
analog-of             → historical analog events (comparison)
attribution-evidence  → attribution studies/assessments (required if attribution claims exist)
requires-review       → governance/policy nodes (when required)
~~~

---

## 🧪 Common Mistakes (And Fixes)

- **Mistake:** Using `references` for datasets  
  **Fix:** use `derived-from` for datasets; keep `references` for documents.

- **Mistake:** “caused-by” relation  
  **Fix:** use `attribution-evidence` + cautious narrative + confidence statement.

- **Mistake:** Multiple `about` relations  
  **Fix:** pick one primary event; link other events via `preceded-by`, `followed-by`, or `analog-of`.

---

## 🕰️ Version History

| Version | Date       | Summary                                                                 |
|--------:|------------|-------------------------------------------------------------------------|
| v11.2.6 | 2025-12-12 | Initial governed climate relation pattern library; attribution-safe additions (`attribution-evidence`, `requires-review`). |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
[📚 Docs Home](../../../../../README.md) ·
[🌦️ Climate Domain](../README.md) ·
[🧪 Climate Examples](../examples/README.md) ·
[🗒️ Climate Notes](../notes/README.md) ·
[📏 Standards Index](../../../../../standards/README.md) ·
[🛡 Governance Charter](../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🌿 FAIR+CARE Guide](../../../../../standards/faircare/FAIRCARE-GUIDE.md)

</div>


---
title: "🌦️ Climate Story Node Template (KFM v11.2.6) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/story-nodes/domains/climate/templates/story-node-climate.md"
version: "v11.2.6"
last_updated: "2025-12-12"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Climate Systems Board · FAIR+CARE Council · AI Attribution Governance Board"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Template"
template_type: "markdown-authoring-template"
header_profile: "standard"
footer_profile: "standard"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:doc:storynodes:domains:climate:templates:story-node-climate-md:v11.2.6"
semantic_document_id: "kfm-storynodes-climate-template-markdown-v11.2.6"
event_source_id: "ledger:docs/story-nodes/domains/climate/templates/story-node-climate.md"
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
intent: "kfm-climate-storynode-template"
governance_level: "FAIR+CARE · Attribution-Safe Scientific Communication"
attribution_sensitive: true

fair_category: "F1-A2-I2-R2"
care_label: "Environmental · Attribution-Sensitive"
classification: "Public-Safe Authoring Template"
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
sunset_policy: "Superseded by v12 climate template"
---

<div align="center">

# 🌦️ **Climate Story Node — Authoring Template (KFM v11.2.6)**  
### *Public-Safe · Evidence-First · Attribution-Responsible · FAIR+CARE-Aligned*  

`docs/story-nodes/domains/climate/templates/story-node-climate.md`

**Purpose**  
Provide a governed authoring template for **Climate Story Nodes** that ensures:  
**scientific rigor**, **attribution safety**, **clear uncertainty framing**, **valid spacetime modeling**,  
and **schema-ready structure** for Focus Mode and graph ingestion.

</div>

---

## 🧩 Instructions for Authors (Normative)

- Do **not** include personal data, individual addresses, or person-level impact stories.
- Do **not** include sensitive infrastructure details (internal-only facilities, vulnerabilities).
- Do **not** “prove” causation from correlation:
  - avoid *“caused by climate change”* unless you cite a specific attribution study and state confidence.
- Do **clearly separate**:
  - **Observation** (measured/observed),
  - **Model Output** (forecast/reanalysis/simulation),
  - **Interpretation** (your evidence-backed synthesis),
  - **Attribution** (only when supported; must state confidence and limits).
- Do **state uncertainty**:
  - data gaps, radar artifacts, model bias, resolution limits, sampling issues.
- Do use **public-safe generalized geometry**:
  - region, county set, watershed, grid box footprint, or raster footprint (when safe).
- Do use **units correctly** (CF conventions where applicable) and define variables explicitly.
- All finalized nodes MUST validate against `story-node.schema.json` and pass domain ethics checks.

---

## 🌦️ Story Node Template (Fill In All Sections)

## 🧾 Metadata

**ID (public-safe):**  
Format (recommended): `clm-ks-{slug}-{yyyy}-{nn}`  
Example: `clm-ks-heatwave-2022-01`

**Title:**  
Short, descriptive, non-sensational.  
Example: *Regional Heatwave Conditions in Kansas (June 2022)*

**Summary (2–3 sentences):**  
A brief, evidence-first synopsis suitable for Focus Mode previews.  
Include:
- where (generalized),
- when (interval),
- what was observed,
- what is uncertain (if relevant).

**Tags (optional):**  
Examples: `heatwave`, `drought`, `severe-weather`, `wind`, `smoke`, `reanalysis`, `radar`

---

## 📖 Narrative

### 1) Context (Observation-First)
Describe what happened in public-safe terms:
- event type (heatwave/drought/tornado outbreak/wind episode/smoke intrusion/etc.),
- generalized affected region,
- generalized timing and evolution.

**Avoid:**
- sensational language,
- unsupported impact claims,
- “record-breaking” unless cited.

---

### 2) Evidence (Observations)
List the direct observational evidence used (examples):
- NWS products (warnings/advisories summaries),
- NEXRAD composites,
- GOES imagery,
- surface station observations (aggregated),
- precipitation analyses,
- published NOAA summaries.

**If you cite “anomaly”**, specify:
- baseline period,
- method (climatology source),
- units.

---

### 3) Evidence (Model Output / Reanalysis)
Summarize model or reanalysis evidence (examples):
- HRRR / GFS (forecast guidance),
- ERA5 (reanalysis),
- other public reanalysis products.

**Rules:**
- Explicitly label model output as model output.
- If you compare to observations, describe the mismatch and uncertainty.

---

### 4) Methods & Derived Metrics (If Used)
If you computed derived indices, document:
- method,
- parameters,
- baseline,
- limitations.

Examples (use only when justified):
- temperature anomaly (°C or K),
- precipitation anomaly (mm),
- wind speed (m/s),
- CAPE (J/kg),
- SPI/SPEI (dimensionless; specify time window).

---

### 5) Interpretation (Evidence-Backed)
Explain what the evidence suggests.
- keep claims proportional to data support,
- include alternative explanations where relevant,
- include what you **cannot** conclude.

---

### 6) Attribution Statement (Only If Supported)
If you include attribution:
- cite the relevant attribution study or formal assessment,
- state confidence level and why.

**Recommended structure:**
- **Claim scope:** what is being attributed (frequency/intensity likelihood, not “the event” as a single cause).
- **Evidence basis:** citations and method type.
- **Confidence:** low/medium/high, with a sentence explaining the uncertainty.

If you cannot support attribution, explicitly say so.

---

### 7) Uncertainty & Limitations
Include at least one uncertainty paragraph.
Examples:
- data gaps,
- radar beam blockage,
- cloud contamination in satellite products,
- model resolution/bias,
- reanalysis smoothing,
- station coverage issues.

---

### 8) Environmental Justice & Impact Framing (When Relevant)
If describing impacts:
- keep it aggregated and evidence-backed,
- avoid stereotypes or blaming communities,
- do not include person-level narratives.

If EJ is relevant, describe:
- differential exposure risk (aggregated),
- uncertainty and data limitations,
- sources for any claims.

---

## 🌐 Spacetime

### Geometry (Generalized GeoJSON)
Use generalized geometry appropriate to the event (region/county set/watershed/footprint).

~~~json
{
  "type": "Feature",
  "geometry": {
    "type": "Polygon",
    "coordinates": [/* generalized / safe */]
  },
  "properties": {
    "masking_level": "region",
    "notes": "Generalized footprint for public-safe climate storytelling."
  }
}
~~~

**Geometry rules**
- Valid GeoJSON required for publishable nodes.
- Prefer:
  - counties / multi-county polygon,
  - watershed polygon,
  - coarse region polygon,
  - raster footprint (when the raster itself is public and safe).
- Avoid overly precise storm track lines unless they are already public and you are using a generalized envelope.

---

### Temporal Bounds
Provide an interval and precision that match the evidence.

**Start:** `YYYY-MM-DDThh:mm:ssZ` (or `YYYY-MM-DD`)  
**End:** `YYYY-MM-DDThh:mm:ssZ` (or `YYYY-MM-DD`)  
**Precision:** `"hour" | "day" | "month" | "year" | "range"`  
**Original Label (optional):** Human label, e.g., `"June 2022 Heatwave (Kansas)"`

---

## 📊 Variables & Units (Recommended Table)

Use this table if you reference variables, anomalies, or indices.

| Variable | Meaning | Units | Source (Observation/Model) | Notes / Method |
|---------|---------|------:|----------------------------|----------------|
| `t2m_anom` | 2m temperature anomaly vs baseline | °C | Reanalysis | Baseline: <fill in> |
| `precip_total` | Total precipitation | mm | Observation | Aggregated over region |
| `wind_gust_max` | Max gust (aggregated) | m/s | Observation | Station coverage limits |
| `spi_3mo` | Standardized Precipitation Index (3 month) | — | Derived | Method: <fill in> |

---

## 🔗 Relations (Graph Links)

Use relations to connect this node to datasets, documents, and analog events.

**Rules**
- Exactly one `about`.
- Use `references` for documents and reports.
- Use `derived-from` for datasets/models/reanalysis inputs.
- Use `analog-of` for historical analog events (public-safe; cite basis).

~~~json
[
  {
    "rel": "about",
    "id": "event:climate:ks:heatwave:2022-06"
  },
  {
    "rel": "references",
    "id": "doc:noaa:ncei:climate-summary-2022-06"
  },
  {
    "rel": "derived-from",
    "id": "dataset:era5:reanalysis"
  },
  {
    "rel": "derived-from",
    "id": "dataset:noaa:nexrad:composite"
  },
  {
    "rel": "analog-of",
    "id": "event:climate:us:heatwave:1936"
  }
]
~~~

---

## 🗃 Sources & Provenance

List public sources only:
- NOAA / NWS reports,
- dataset landing pages and identifiers,
- STAC/DCAT references for assets,
- processing pipeline references (if applicable).

**Provenance minimum (recommended)**
- Source dataset IDs (or STAC item IDs)
- Processing summary (what you did)
- Known limitations
- Rights/license notes for media and rasters

---

## 🖼 Media (Optional, STAC-Linked)

Only include media that is:
- licensed for use,
- clearly labeled as observation vs derived,
- public-safe.

~~~json
[
  {
    "href": "https://example.org/stac/climate/ks/2022-06/era5_t2m_anom.tif",
    "title": "ERA5 2m Temperature Anomaly (Generalized Region)",
    "mime": "image/tiff",
    "license": "CC-BY 4.0",
    "role": "data"
  }
]
~~~

---

## ✅ Pre-Submit Checklist (Quick)

- [ ] Observation vs model output is clearly separated.
- [ ] Any attribution statements are evidence-backed and confidence-labeled (or omitted).
- [ ] Geometry is valid GeoJSON and generalized.
- [ ] Units are correct; variables are defined.
- [ ] Uncertainty is explicitly stated.
- [ ] Sources are public and properly cited.
- [ ] Relations include exactly one `about`.
- [ ] Final node validates against `story-node.schema.json`.

---

## 🕰️ Version History

| Version | Date       | Summary                                                                 |
|--------:|------------|-------------------------------------------------------------------------|
| v11.2.6 | 2025-12-12 | Initial governed climate Markdown authoring template; attribution-safe structure; schema-ready sections and validation checklist. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
[📚 Docs Home](../../../../../README.md) ·
[🌦️ Climate Domain](../README.md) ·
[🗒️ Climate Notes](../notes/README.md) ·
[🧪 Climate Examples](../examples/README.md) ·
[📏 Standards Index](../../../../../standards/README.md) ·
[🛡 Governance Charter](../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🌿 FAIR+CARE Guide](../../../../../standards/faircare/FAIRCARE-GUIDE.md)

</div>


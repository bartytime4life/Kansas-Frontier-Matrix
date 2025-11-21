---
title: "🌊 Kansas Frontier Matrix — Tuttle Creek Lake Water Injection Dredging (WID) 2025 Technical Summary"
path: "docs/analyses/hydrology/tuttle-creek/water-injection-dredging-2025.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Annual / Hydrology & Hazards Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/docs-analyses-hydrology-wid-v1.json"
governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Analysis"
intent: "hydrology-wid-technical-summary"
semantic_document_id: "kfm-analyses-hydrology-tuttle-creek-wid-2025"
doc_uuid: "urn:kfm:docs:analyses:hydrology:tuttle-creek:wid-2025:v11.0.0"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🌊 **Kansas Frontier Matrix — Tuttle Creek Lake Water Injection Dredging (WID) 2025 Technical Summary**  
`docs/analyses/hydrology/tuttle-creek/water-injection-dredging-2025.md`

**Purpose:**  
Provide a concise, v11-compliant technical summary of the 2025 Water Injection Dredging (WID)  
demonstration at Tuttle Creek Lake (Kansas), framed for ingestion into KFM’s ETL → STAC → graph →  
Focus Mode pipeline.

</div>

---

# 📘 Overview

The Kansas Water Office (KWO), in partnership with the U.S. Army Corps of Engineers (USACE), conducted a  
first-of-its-kind **Water Injection Dredging (WID)** demonstration at **Tuttle Creek Lake**, near Manhattan, Kansas,  
in **September 2025**. The core objective was to test whether WID can serve as a viable long-term sediment  
management strategy for a large multipurpose reservoir whose conservation pool has been heavily impaired  
by sedimentation.

This document:

- Restates the key technical facts and monitoring framework of the 2025 WID Phase 1 trial.  
- Normalizes the information for KFM v11 integration (directory layout, STAC hints, graph model).  
- Provides a Story Node–friendly narrative for Focus Mode v3.

---

# 🧭 1. Project Summary

- **Reservoir:** Tuttle Creek Lake, Big Blue River basin, Kansas.  
- **Operator:** USACE Kansas City District.  
- **State partner:** Kansas Water Office (KWO).  
- **Method:** Water Injection Dredging (WID) – using low-pressure, high-volume jets to fluidize bottom  
  sediment into a density current that flows to the dam outlet, exporting sediment downstream.  
- **Phase 1 demo window:** Approximately **10 days**, ~**17–27 September 2025**.  
- **Strategic goal:** Establish whether WID can be operated:

  - At meaningful production rates (cubic yards per hour / per season).  
  - Cost-effectively (dollars per cubic yard).  
  - Without unacceptable downstream water-quality or ecological impacts.  

This demonstration is a critical input to long-term decisions about sediment maintenance for Tuttle Creek  
and, by extension, other Kansas reservoirs facing chronic capacity loss.

---

# 🏞️ 2. Reservoir Condition & Sedimentation

Key baseline conditions motivating WID:

- Since dam closure in **1962**, approximately **438 million cubic yards** of sediment have accumulated in  
  Tuttle Creek Lake.  
- The reservoir has lost roughly **46%** of its **original conservation storage**.  
- Projections indicate that, **without intervention**, about **75%** of the multipurpose pool could be filled  
  with sediment by **2074**, leaving only **~25%** of its original capacity.  
- Primary sediment sources:

  - **Big Blue River** and **Little Blue River** inflows.  
  - Watershed-scale drivers, including agricultural land use, channel erosion, and major flood events.

Implications for KFM:

- Tuttle Creek is an archetypal **sedimentation-risk reservoir** for Kansas.  
- It is a candidate “anchor site” for Story Nodes combining hydrology, land use, hazards, and policy.  

---

# 🚧 3. 2025 Demonstration Project

## 🚢 3.1 WID Technique & Equipment

- **Platform:** Approx. **120 ft barge** outfitted with an array of water-jet manifolds.  
- **Operation:**  

  - Jets inject water into surficial bed sediments, reducing shear strength and creating a **turbid, dense  
    near-bed flow** (density current).  
  - This density current is guided toward the **dam outlet works**.  
  - Sediment-laden water is then **discharged downstream**, where deposition occurs under riverine flow.

- **Control variables:**  

  - Jet flow rate and pressure.  
  - Barge position and track.  
  - Duration and timing of injections relative to reservoir level and outlet gate operations.

## 🎯 3.2 Primary Evaluation Targets

The demonstration is structured to answer several performance questions:

- **Production:**  
  - What **sediment removal rate** (cy/hr) is achievable under different operational settings?  
  - What is the **sustainable daily and seasonal removal volume** given physical and regulatory constraints?

- **Cost:**  
  - What is the **unit cost** of sediment removed (USD per cubic yard), including mobilization, fuel, crew,  
    and monitoring costs?  

- **Environmental performance:**  
  - Are downstream **turbidity**, **TSS**, **nutrients**, and **DO** kept within acceptable thresholds?  
  - Are there measurable adverse effects on aquatic biota, habitats, or geomorphology?

- **Feasibility for long-term operations:**  
  - Can WID be scaled to **routine, multi-year maintenance** rather than one-off dredging campaigns?  
  - How does WID compare, in lifecycle terms, to alternatives such as traditional cutterhead dredging or  
    structural modifications?

## 💰 3.3 Funding Snapshot

Approximate 2025 funding envelope for the demo phase:

- **USACE / Federal:** ~**$7.1M** (including Infrastructure / R&D streams).  
- **State / KWO:** ~**$2M**.  

These figures should be treated as indicative order-of-magnitude values for KFM narratives and not as  
contractual totals.

---

# 📡 4. Environmental Monitoring & QA/QC

## 🧪 4.1 Water Quality Monitoring Framework

Monitoring is performed:

- **Within the reservoir** (near the WID operation and along the density current path).  
- **At the dam and immediate tailwater**.  
- **Downstream** in the **Big Blue River** and, at coarser resolution, the **Kansas River**.

Key parameters (stationary and/or profiling):

- **Turbidity (NTU)**.  
- **Total Suspended Solids (TSS)**.  
- **Dissolved Oxygen (DO)**.  
- **Nutrients** (various forms of nitrogen and phosphorus).  
- **Metals / legacy contaminants** (e.g., if sediments mobilize stored pollutants).  
- **Biological indicators** (e.g., fish, benthic invertebrates, mussel communities).  
- **Sediment granulometry** (particle-size distribution).

Protective triggers:

- DO dropping below critical thresholds for aquatic life.  
- Turbidity or TSS exceeding regulatory or fishery-based criteria.  
- Evidence of significant adverse impacts in downstream biological surveys.

KFM integration:

- These parameters map to standard **time-series entities** in the hydrology and water-quality domains.  
- They can be used to build Focus Mode summaries of **“before / during / after”** WID operations.

## 🌎 4.2 Downstream Ecological & Geomorphic Analysis

Baseline and impact-overview elements include:

- **Channel morphology** and riverbed substrate.  
- Key habitats (riffles, pools, backwaters).  
- Sensitive or protected **mussel** and **fish** species distributions.  
- **Riparian vegetation** stress and potential deposition zones.  

Relevant reference: a **2023 Kansas State University capstone study** modeled turbidity plumes and density  
current behavior under hypothetical WID operations, providing pre-demonstration expectations for:

- Likely plume extents and duration.  
- DO response scenarios.  
- Areas of particular ecological interest or concern.

---

# 📊 5. Costs, Performance Questions & Open Issues

The demonstration is intentionally structured as a **decision-support experiment**. The main open questions:

- **Production envelope:**  

  - Achievable sediment removal rates (cy/hr).  
  - Operational constraints (gate capacity, reservoir level, equipment endurance).  

- **Annualized and lifecycle costs:**  

  - How does WID scale if implemented every year or every few years?  
  - What is the cost per **acre-foot** of capacity preserved or reclaimed?

- **Ecological resilience vs. chronic disturbance:**  

  - Are repeated WID campaigns compatible with long-term ecological health?  
  - How much sediment actually traverses the dam and reaches downstream rivers versus redepositing in  
    the forebay or channel margins?

- **System-level implications:**  

  - How would a successful WID program at Tuttle Creek interact with upstream watershed BMPs,  
    reservoir reoperations, or structural modifications?  

These questions should be encoded into KFM as **hypotheses** and **research prompts** linked to the WID  
Story Node and Focus Mode views, so future monitoring updates can be narratively and analytically attached.

---

# 🛰️ 6. Data Sources & Documentation

This section lists key external sources relevant to WID at Tuttle Creek, for ETL ingestion and citation within  
Story Nodes and Focus Mode.

## 🏛️ 6.1 Official Technical & Regulatory Sources

- **USACE WID Project Page** – Project narrative, monitoring plan, and sedimentation context.  
- **Kansas Water Office WID Demonstration Page** – State objectives, planning docs, and presentations.  
- **USACE Draft Environmental Assessment (EA) & FONSI** – Detailed environmental analysis and mitigation  
  measures.  
- **Kansas Legislative Testimony (Water Committee, Feb 2025)** – Sedimentation trends, funding rationale,  
  and policy framing.

## 🎓 6.2 Academic & Independent Research

- **Kansas State University (KSU) 2023 Capstone – Downstream Effects of WID** – Turbidity plume modeling,  
  density current behavior, and ecological risk scenarios.  
- **Stakeholder / NGO papers** (e.g., Friends of the Kaw) – Provide alternative perspectives, citing concerns  
  about river health, sediment contamination, and long-term systemic impacts.

## 📰 6.3 Journalism & Public Context

- **Kansas Reflector (19 Nov 2025)** – Field reporting from WID Phase 1; interviews with engineers and  
  stakeholders; descriptions of on-the-water operations and public sentiment.

For KFM, each of these sources should be represented as:

- A **Document node** in the graph.  
- One or more **STAC Items** (when a digital asset is spatial/temporal, e.g., a PDF geo-tagged to Tuttle  
  Creek and 2025-09).  
- A **PROV-O provenance link** connecting WID Story Nodes and Focus Mode summaries to their source  
  documents.

---

# 🧱 7. Structured Data & KFM Integration

## 🗂 7.1 Suggested Directory Layout

```text
docs/
├── analyses/
│   ├── hydrology/
│   │   ├── README.md
│   │   ├── tuttle-creek/
│   │   │   ├── water-injection-dredging-2025.md   # this file
│   │   │   └── monitoring-design-2025.md          # future detailed QA/QC spec
│   │   └── statewide/
│   │       └── sedimentation-overview.md
└── standards/
    └── ...
```

For ETL and datasets (aligned with the monorepo layout):

```text
data/
├── sources/
│   └── usace_tuttle_creek_wid_2025.json      # source manifest for WID-related assets
├── raw/
│   └── hydrology/
│       └── tuttle-creek-wid-2025/            # PDFs, CSVs, shapefiles, etc.
├── processed/
│   └── hydrology/
│       └── tuttle-creek-wid-2025/            # cleaned CSVs, GeoJSON, COGs
└── stac/
    └── hydrology/
        └── tuttle-creek-wid-2025/            # STAC Collection + Items for WID assets
```

## 🛰️ 7.2 STAC Item Template (Example)

This example illustrates how the WID Phase 1 demo could be represented as a STAC Item for a monitoring  
dataset (e.g., turbidity time series near the dam during the trial window).

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "tuttle-creek-wid-2025-phase1-turbidity",
  "collection": "tuttle-creek-wid-2025",
  "geometry": {
    "type": "Point",
    "coordinates": [-96.6005, 39.2758]
  },
  "bbox": [-96.601, 39.275, -96.600, 39.276],
  "properties": {
    "datetime": "2025-09-17T00:00:00Z",
    "end_datetime": "2025-09-27T23:59:59Z",
    "kfm:site": "Tuttle Creek Dam tailwater",
    "kfm:parameter": "turbidity",
    "kfm:units": "NTU",
    "kfm:project": "WID-Phase1-2025",
    "providers": [
      { "name": "USACE Kansas City District", "roles": ["producer", "host"] },
      { "name": "Kansas Water Office", "roles": ["sponsor"] }
    ]
  },
  "assets": {
    "timeseries": {
      "href": "https://example.org/data/tuttle-creek/wid-2025/turbidity_timeseries.csv",
      "type": "text/csv",
      "roles": ["data"]
    },
    "report": {
      "href": "https://example.org/docs/tuttle-creek/wid-2025/wq-summary.pdf",
      "type": "application/pdf",
      "roles": ["metadata", "documentation"]
    }
  }
}
```

This STAC record can be exported to DCAT (for cataloging) and mapped into Neo4j via:

- A **Dataset node** (DCAT:Dataset).  
- An **Observation/Series node** with relationships to **Place (dam)** and **Event (WID Phase 1)**.  

## 🕸️ 7.3 Graph Model Notes (CIDOC-CRM + GeoSPARQL)

Conceptual mapping for WID within the KFM knowledge graph:

- **E53 Place:**  

  - `Place:Tuttle_Creek_Reservoir` (GeoSPARQL geometry: reservoir polygon).  
  - `Place:Tuttle_Creek_Dam` (GeoSPARQL geometry: dam footprint).  
  - `Place:Big_Blue_River_Downstream_Reaches`.

- **E5 Event / E7 Activity:**  

  - `Event:WID_Phase1_2025` – an E7 Activity representing the 10-day demonstration.  
  - Linked with `P7_took_place_at` → `Place:Tuttle_Creek_Reservoir`.  
  - Linked with OWL-Time `time:hasBeginning` and `time:hasEnd`.

- **E39 Actor:**  

  - `Actor:USACE_Kansas_City_District`.  
  - `Actor:Kansas_Water_Office`.  
  - Potentially `Actor:Kansas_State_University_Team`.

- **E73 Information Object / E31 Document:**  

  - `Document:USACE_WID_EA_2024`.  
  - `Document:KWO_WID_Project_Summary`.  
  - `Document:KSU_WID_Capstone_2023`.

- Relationships:

  - `Event:WID_Phase1_2025` `P14_carried_out_by` → `Actor:USACE_Kansas_City_District`.  
  - `Document:USACE_WID_EA_2024` `P70_documents` → `Event:WID_Phase1_2025`.  

This schema ensures that Focus Mode can traverse from a WID Story Node to:

- Places (reservoir, dam, downstream reaches).  
- Actors (agencies, universities, NGOs).  
- Documents (technical and narrative).  
- Observations (time-series data from monitoring networks).

---

# 📖 8. Story Node / Focus Mode Narrative

This section provides a narrative suitable for use as a **Story Node v3** body and as the base text for  
Focus Mode v3 when a user focuses on “Tuttle Creek WID 2025”.

> **“The Silt That Choked a Reservoir — And the Technology That Fought Back”**  
>  
> By 2025, sediment had already stolen nearly half of Tuttle Creek Lake’s original conservation storage.  
> Without intervention, projections showed that three-quarters of its multipurpose pool could be clogged  
> with silt by 2074. The reservoir, built to tame floods and secure water supply, was quietly filling from  
> the bottom up.  
>  
> In September 2025, Kansas chose to test a different path: **Water Injection Dredging**. For ten days, a  
> 120-foot barge, armed with jet manifolds, moved methodically across the lake floor. Instead of digging  
> and hauling sediment by barge, engineers used high-volume water jets to fluidize the mud and create a  
> controlled density current that slipped toward the dam outlet.  
>  
> On the surface, the lake looked much as it always had. Below, sensors pulsed and operators watched  
> live feeds of turbidity, dissolved oxygen, and river gauges downstream. Biologists tracked fish and  
> mussel habitats; hydrologists monitored how far and how fast the sediment plume traveled. Every hour  
> of WID was both an engineering operation and a scientific experiment.  
>  
> The 2025 demonstration did not answer every question. It did, however, mark a turning point: Tuttle  
> Creek became one of the first large U.S. reservoirs to seriously test water-powered sediment export as a  
> long-term management tool. For the Kansas Frontier Matrix, it is a key Story Node in the evolving  
> narrative of how Kansans respond to aging infrastructure, changing rivers, and the slow, quiet hazard of  
> sedimentation.

When encoded as a Story Node JSON (per `story-node.schema.json`), this narrative should be:

- Spatially grounded at `Place:Tuttle_Creek_Reservoir`.  
- Temporally grounded to `2025-09-17T00:00:00Z` → `2025-09-27T23:59:59Z` (with `precision: "day"`).  
- Linked to related events (historic sedimentation, future adaptation decisions) via `relations`.

---

# 🕰 9. Version History

- **v11.0.0 (2025-11-21):** Initial KFM v11 migration of Tuttle Creek WID 2025 technical summary; added  
  STAC template, graph model notes, and Story Node narrative.  

---

[⬅️ Back to Hydrology Analyses](../README.md) • [🏠 Back to KFM v11 Master Guide](../../reference/kfm_v11_master_documentation.md) • [📂 Data & Sources Index](../../data/README.md)

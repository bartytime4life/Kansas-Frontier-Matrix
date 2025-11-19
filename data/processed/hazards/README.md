Weights are dataset-dependent.

Outputs stored in:

~~~~text
hazard_intensity_index_v11.0.0.csv
~~~~

---

# 8. 🧍 Exposure & Vulnerability Modeling

Exposure datasets quantify:

- Population  
- Buildings  
- Infrastructure  
- Agriculture  
- Land use  

Spatial units:

- Census tracts  
- Block groups  
- H3 cells  

Example fields:

~~~~text
tract_id, pop, pop_age65, pop_under5, structures, ag_value, exposure_score
~~~~

---

# 9. 🔐 Governance Architecture (FAIR+CARE v11)

Governance flows for hazards:

### Required:

- CARE assessment for human-impact metrics (fatalities, injuries)  
- Sovereignty filtering for tribal lands  
- Masking for sensitive facility locations  
- Public exposure risk scoring  

Governance artifacts:

~~~~text
metadata/faircare_certification.json
metadata/masking_policies.json
docs/reports/audit/data_provenance_ledger.json
~~~~

---

# 10. 🧮 Integrity Architecture (Checksums)

Every file in this directory has an entry in:

~~~~text
data/archive/2025Q4/checksums/hazards_checksums.json
data/checksums/manifest.json
~~~~

Rules:

- SHA-256 with prefix `sha256-`  
- File path must be exact  
- Dataset ID must match STAC/DCAT  

---

# 11. 🛰 STAC/DCAT Publication Requirements

Hazards have a domain-level STAC Collection:

~~~~text
data/processed/hazards/stac_collection.json
~~~~

Each dataset has:

- STAC Item  
- DCAT Dataset  
- JSON-LD provenance  
- Quality & sustainability metadata  

---

# 12. 🔍 Focus Mode v3 Integration

Hazards datasets power:

- Time-slider hazard timelines  
- Narrative hazard sequences  
- Story Node v3 generation  
- Predictive hazard overlays  
- Risk mosaics and explainability overlays  

All hazards must include:

- Temporal precision  
- Geometry validity  
- Domain-specific annotations  

---

# 13. 📜 Internal Reference Citation

~~~~text
Kansas Frontier Matrix (2025). Processed Hazards Data (v11.0.0).
FAIR+CARE-certified, checksum-verified hazards datasets integrating tornado,
flood, drought, wildfire, and exposure domains. Aligned to STAC/DCAT, ISO 19115,
and KFM-OP v11 ontology for scientific and public resilience applications.
~~~~

---

# 14. 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.0.0 | 2025-11-19 | Full v11 hazards architecture: schema tables, ontology, lineage, exposure modeling, STAC/DCAT integration. |
| v10.2.2 | 2025-11-12 | Added Focus v2.1, Streaming-STAC support, telemetry v2. |
| v10.0.0 | 2025-11-09 | Initial hazards processed layer structure. |

<div align="center">

**Kansas Frontier Matrix — Hazards Domain**  
FAIR+CARE Certified · Sustainability Validated · Diamond⁹ Ω / Crown∞Ω  

© 2025 Kansas Frontier Matrix — CC-BY 4.0  

</div>

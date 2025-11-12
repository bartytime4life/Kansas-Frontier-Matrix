```
---
title: "🗣️ Kansas Frontier Matrix — Oral Histories Integration (Hydrology & Agriculture Context)"
path: "docs/archives/oral-histories/README.md"
version: "v10.0.0"
last_updated: "2025-11-11"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.0.0/manifest.zip"
telemetry_ref: "../../../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/oral-histories-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
data_contract_ref: "../../contracts/data-contract-oral-histories-v1.json"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🗣️ **Oral Histories Integration for Hydrology & Agriculture**
`docs/archives/oral-histories/README.md`

**Purpose:**  
Bring digitized **oral histories** (interviews, community archives, farm/ranch recollections) into KFM so models can link **human memory** to **hydrological** and **agricultural** change (e.g., drought onset cues, flood markers, crop practice shifts). This adds *why* and *how* to the *what* in instrument records.

</div>

---

## 🗂️ Directory Layout
```

docs/archives/oral-histories/        # Methods, ethics, schemas, examples
├─ README.md                        # You are here
├─ intake/                          # Source registry & harvesting playbooks
│   ├─ registry.csv                 # Archive -> URL, license, access terms
│   ├─ harvest-playbook.md          # Step-by-step ingest (PDF, audio, text)
│   └─ rights-review-checklist.md   # Use permissions, embargo, sensitivity
├─ schema/                          # JSON Schemas (FAIR+CARE aligned)
│   ├─ oral-history-record.schema.json
│   └─ segment.schema.json
├─ nlp/                             # NLP configs & recipes (spaCy, PyTorch)
│   ├─ config_spacy.cfg
│   ├─ prompts/ner_hydrology.md
│   └─ patterns/                     # Gazetteers & rule patterns
│       ├─ hydrology_terms.txt
│       └─ agriculture_terms.txt
├─ mapping/                         # KG mappings (CIDOC CRM, OWL-Time, GeoSPARQL)
│   ├─ cidoc_crm_mapping.ttl
│   ├─ owl_time_alignment.ttl
│   └─ geosparql_alignment.ttl
├─ governance/                      # Consent, ethics, redaction, community review
│   ├─ consent-model.md
│   ├─ redaction-policy.md
│   └─ community-review-process.md
├─ examples/                        # Worked examples (before/after)
│   ├─ sample_transcript_raw.txt
│   ├─ sample_transcript_segments.json
│   └─ sample_graph_triples.ttl
└─ reports/                         # Validation & linkage reports
├─ coverage-summary.md
└─ hydrology-linkage-index.csv

```

---

## 📘 Background (Plain Language)
- **Oral histories** are recorded memories/stories. They capture signals like “the river used to flood after cottonwood fluff” or “we switched wheat varieties after the ’56 drought.”  
- These clues help interpret datasets (stream gauges, rainfall, landcover) by adding human context (timing, coping strategies, local markers) that instruments don’t record.

---

## 🧩 Data Model (FAIR+CARE)
**Record → Segment → Annotations → Links**
- **Record:** interview-level metadata (who, when, where, rights, community steward).
- **Segment:** short passages (30–300 words) with start/end offsets and timestamps.
- **Annotations:** entities (rivers, crops), events (drought, flood), cues (phenology), practices (irrigation).
- **Links:** connections to KFM assets (USGS gauge IDs, PRISM periods, crop layers), plus provenance and consent.

**Minimum fields (segment):**
- `record_id`, `segment_id`, `text`, `speaker_role`, `time_range`, `location_hint`, `event_tags[]`, `rights_flag`, `consent_scope`, `provenance.activity`, `quality.score`.

---

## ⚖️ Ethics & Rights (Must-Do)
- **Consent scope first.** Respect **no-derive** or **no-ML** flags.  
- **Redact** sensitive items (addresses, health, minors, legal risk).  
- **Community review** before publishing derived features.  
- **Attribution** to the archive and narrators; carry license/terms forward.

See: `governance/consent-model.md`, `governance/redaction-policy.md`, `governance/community-review-process.md`.

---

## ⚙️ Ingest → NLP → Graph (Workflow)
1. **Harvest**  
   - Register sources in `intake/registry.csv` (archive name, URL, format, license).  
   - Pull transcripts (PDF/audio/text). For audio-only, run ASR → `.txt`.  
   - Run **rights review** checklist; tag `consent_scope`.

2. **Normalize**  
   - Convert to UTF-8 `.txt`; split by speaker/time; store `examples/*_raw.txt`.  
   - Create `segments.json` using `schema/segment.schema.json`.

3. **NLP Pass**  
   - spaCy pipeline (config in `nlp/config_spacy.cfg`):  
     - **NER:** rivers, creeks, counties, reservoirs, crops, pests, implements.  
     - **Temporal:** seasons, relative years (“the year after the big flood”).  
     - **Cues:** phenology terms (cottonwood fluff, cicada hum), soil cues (cracks), livestock stress.  
   - Gazetteers in `nlp/patterns/`.

4. **Event Linking**  
   - Map mentions to KFM entities:  
     - **Hydrology:** USGS site IDs, flood/drought episodes (OWL-Time intervals).  
     - **Ag:** crop calendars, variety switches, irrigation adoption dates.  
   - Emit RDF triples using `mapping/*.ttl` (CIDOC CRM events; GeoSPARQL for places).

5. **Validation & Reports**  
   - Produce coverage stats (`reports/coverage-summary.md`).  
   - Emit `hydrology-linkage-index.csv` (segment_id ↔ gauge_id ↔ date_range ↔ confidence).

6. **Focus Mode Surfacing**  
   - Expose segments on timeline near sensor events (with consent-aware filters).  
   - Show “human cue cards” in map popovers (e.g., “dust devils increased before crop failure”).

---

## 🧪 Quick Start (Make It Work)
- **Place a test transcript** at `examples/sample_transcript_raw.txt` (1–2 pages).  
- **Run segmentation** (pseudo-CLI shown below; wire to your ETL job):
  - `kfm-oral split --in examples/sample_transcript_raw.txt --out examples/sample_transcript_segments.json`
- **NLP tag**:
  - `kfm-oral nlp --in examples/sample_transcript_segments.json --cfg nlp/config_spacy.cfg --out examples/sample_transcript_segments.tagged.json`
- **Link to hydrology**:
  - `kfm-oral link --in examples/sample_transcript_segments.tagged.json --map mapping/*.ttl --out examples/sample_graph_triples.ttl`
- **Report**:
  - `kfm-oral report --in examples/sample_transcript_segments.tagged.json --out reports/hydrology-linkage-index.csv`

*(Implement these as Python entrypoints or Make targets within existing KFM ETL.)*

---

## 🧭 Annotation Targets (Starter Lists)
- **Hydrology:** “Arkansas River”, “Neosho”, “Smoky Hill”, “flood”, “sandbar”, “well went dry”, “stock pond”.  
- **Agriculture:** “winter wheat”, “milo”, “alfalfa”, “center pivot”, “terraces”, “no-till”.  
- **Cues:** “cottonwood fluff”, “cicadas loud”, “soil cracked”, “sandhills shifted”, “ice jam”.

Add to `nlp/patterns/hydrology_terms.txt` and `agriculture_terms.txt`.

---

## 🔗 Knowledge Graph Mapping (Summary)
- **CIDOC CRM**: model interviews as **E7 Activity**, utterances as **E33 Linguistic Object**, events as **E5 Event** with time via **OWL-Time**.  
- **GeoSPARQL**: rivers/reservoirs as Features; link segments by place hints or disambiguated toponyms.  
- **Provenance**: use **PROV-O** to record ASR, redaction, NLP steps.

---

## 📊 Telemetry & Quality
- Log: #segments processed, %with locations, %linked to gauges, avg. NER confidence.  
- Ethics telemetry: #segments redacted, consent scopes used, community approvals pending.  
- Store in `telemetry_ref` with schema `telemetry_schema`.

---

## ✅ Definition of Done (Pilot)
- 1 archive registered, 50+ segments processed.  
- ≥60% segments have at least one hydrology or agriculture link.  
- Consent-compliant display in Focus Mode with redaction upheld.  
- Coverage report and linkage CSV generated.

---

## 🧾 Version History
| Version | Date       | Author | Summary                                    |
|--------:|------------|--------|--------------------------------------------|
| v10.0.0 | 2025-11-11 | KFM    | Initial oral histories integration module. |

<div align="center">

© Kansas Frontier Matrix — Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to docs/] · [Governance Charter]

</div>
```

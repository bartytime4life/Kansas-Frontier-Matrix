<div align="center">

# 🗣️ Kansas Frontier Matrix — Oral Histories Integration

`docs/integration/oral-histories.md`

**Purpose:** Document the reproducible integration of **Indigenous and community oral histories**
into the **Kansas Frontier Matrix (KFM)** — preserving narrative context, ensuring
ethical handling, and linking testimonies semantically to **places, events, and time periods**.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../)
[![Provenance](https://img.shields.io/badge/Integrity-SHA256%20%7C%20PROV--O-green)](../../docs/standards/metadata.md)
[![Ontology](https://img.shields.io/badge/Ontology-CIDOC%20CRM%20%7C%20PROV--O%20%7C%20OWL--Time-orange)](../../docs/standards/ontologies.md)
[![Audio & Metadata](https://img.shields.io/badge/Data-Audio%20%7C%20Transcript%20%7C%20STAC%201.0-purple)](../../docs/standards/data-formats.md)

</div>

---

## 🎯 Integration Objective

To integrate **recorded oral histories**—Indigenous narratives, community testimonies, and settler recollections—
into KFM’s knowledge graph as verifiable, time-aware entities. Each record becomes both a digital artifact (audio, text, or video) and a structured semantic node linked to historical events, people, and locations.

**Goals**

* 🎧 Preserve voices as `crm:E73_Information_Object` with transcripts and metadata
* 🌎 Link narratives to `crm:E53_Place` and `crm:E5_Event` nodes in Neo4j
* 🧠 Represent temporal context (`time:Interval`, `prov:atTime`)
* 🧩 Index audio and text under STAC 1.0 for discoverability
* 🔐 Ensure ethical handling (permissions, cultural sensitivity tags)

---

## 🧭 Primary Sources and Partners

| Partner / Archive                               | Format              | Coverage              | Access                                                 | License              |
| :---------------------------------------------- | :------------------ | :-------------------- | :----------------------------------------------------- | :------------------- |
| **Kansas Oral History Project (KOHP)**          | MP3, PDF Transcript | 1970–present          | [kansasoralhistory.org](https://kansasoralhistory.org) | CC BY-NC 4.0         |
| **Tribal Historic Preservation Offices (THPO)** | WAV, TXT            | Pre-contact → present | Partnership / permission                               | Community agreements |
| **Library of Congress — Voices of the Plains**  | MP3, JSON           | 1930s–1960s           | [loc.gov/audio](https://www.loc.gov/audio/)            | Public Domain        |
| **Local Museums & Historical Societies**        | MP3, PDF            | 1880–2025             | Institutional exports                                  | Mixed (CC BY, PD)    |

---

## 🧩 File Structure and Preferred Formats

| Type             | Native Input | Converted Format         | Tool                  |
| :--------------- | :----------- | :----------------------- | :-------------------- |
| Audio Recordings | MP3/WAV      | FLAC + SHA256 checksum   | `ffmpeg`, `sha256sum` |
| Transcripts      | PDF/DOCX     | UTF-8 TXT + VTT segments | `pandoc`, `whisperx`  |
| Metadata         | CSV/JSON     | STAC Item (JSON)         | `jq`, `python-stac`   |
| Speaker photos   | JPEG         | WebP (optimized)         | `cwebp`               |

Example conversion

```bash
ffmpeg -i oral_history_01.mp3 -ar 44100 -ac 1 -c:a flac data/processed/oral/01.flac
pandoc sarah_brown_transcript.pdf -t plain -o data/processed/oral/01.txt
sha256sum data/processed/oral/01.flac > data/checksums/oral/01.flac.sha256
```

---

## 🔄 Integration Workflow

```mermaid
flowchart TD
  A["🎧 Collect Audio + Transcript"] --> B["🧮 Normalize + Transcribe<br/>to UTF-8 TXT + VTT"]
  B --> C["🧾 Generate STAC Metadata + SHA256"]
  C --> D["🧠 Ingest → Neo4j as E73_Information_Object"]
  D --> E["🗺️ Link to Places (E53) and Events (E5)"]
  E --> F["🚀 Publish → Timeline + Map + AI Summaries"]
  style A fill:#eef7ff,stroke:#0077cc
  style B fill:#fff0f5,stroke:#cc0088
  style C fill:#ecf9f0,stroke:#33aa33
  style D fill:#fffbea,stroke:#e8a500
  style E fill:#e8f0ff,stroke:#0066aa
  style F fill:#f0e8ff,stroke:#8844cc
```

<!-- END OF MERMAID -->

---

## 🧾 Example STAC Item — Oral History Record

```json
{
  "stac_version": "1.0.0",
  "id": "oral_history_sarah_brown_1978",
  "type": "Feature",
  "properties": {
    "datetime": "1978-04-12T00:00:00Z",
    "description": "Interview with Sarah Brown of Cowley County on Dust Bowl life and farming migration.",
    "license": "CC BY-NC 4.0",
    "keywords": ["oral history","Dust Bowl","Kansas","migration"],
    "providers": [{"name":"Kansas Oral History Project","roles":["producer","licensor"]}]
  },
  "assets": {
    "audio": {
      "href": "data/processed/oral/1978_sarah_brown.flac",
      "type": "audio/flac",
      "roles": ["data"],
      "title": "Oral History Audio"
    },
    "transcript": {
      "href": "data/processed/oral/1978_sarah_brown.txt",
      "type": "text/plain",
      "roles": ["metadata"]
    },
    "checksum": {
      "href": "data/checksums/oral/1978_sarah_brown.flac.sha256",
      "type": "text/plain",
      "roles": ["checksum"]
    }
  },
  "bbox": [-97.02, 37.24, -97.02, 37.24],
  "links": [
    {"rel":"collection","href":"../collection.json"},
    {"rel":"documentation","href":"../../../docs/integration/oral-histories.md"}
  ]
}
```

Validate via:

```bash
stac-validator data/stac/oral/oral_history_sarah_brown_1978.json
```

---

## 🧠 Ontology Mapping (CIDOC CRM + OWL-Time)

| Entity                | Class                        | Description                                   |
| :-------------------- | :--------------------------- | :-------------------------------------------- |
| Audio recording       | `crm:E73_Information_Object` | Digital file containing spoken testimony      |
| Interview event       | `crm:E7_Activity`            | Recording session (time, place, participants) |
| Speaker / interviewee | `crm:E21_Person`             | Voice source, identified actor                |
| Interviewer           | `crm:E39_Actor`              | Collector / recorder                          |
| Topic / Theme         | `skos:Concept`               | Dust Bowl, farming, tribal sovereignty, etc.  |
| Location              | `crm:E53_Place`              | County or settlement referenced               |
| Time Span             | `time:Interval`              | Recording and historical reference period     |

---

## 🔗 Cross-Domain Connections

| Linked Dataset         | Relation              | Purpose                                |
| :--------------------- | :-------------------- | :------------------------------------- |
| **Climate Hazards**    | `prov:wasInformedBy`  | Narratives describing Dust Bowl storms |
| **Deeds & Homesteads** | `crm:P70_documents`   | Recollections of land transfers        |
| **Treaties**           | `crm:P67_refers_to`   | Accounts of tribal lands and migration |
| **GIS Archive**        | `geo:hasGeometry`     | Spatial mapping of story locations     |
| **Research Notes**     | `prov:wasGeneratedBy` | Used in historical interpretation      |

---

## 🧮 Provenance Example (RDF PROV-O)

```turtle
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix crm: <http://www.cidoc-crm.org/cidoc-crm/> .
@prefix kfm: <https://kfm.org/id/> .

kfm:oral/1978_sarah_brown
  a crm:E73_Information_Object ;
  prov:wasGeneratedBy kfm:event/interview_1978_cowley ;
  prov:wasAttributedTo kfm:actor/sarah_brown ;
  crm:P7_took_place_at kfm:place/Cowley_County ;
  crm:P4_has_time-span kfm:time/1978 ;
  prov:wasDerivedFrom <https://kansasoralhistory.org/interviews/sarah-brown> .
```

---

## 🧩 Ethical & Access Guidelines

| Aspect                          | Policy                                                                  |
| :------------------------------ | :---------------------------------------------------------------------- |
| **Consent & Usage Rights**      | Verify license (CC BY-NC, PD, or community MOU) before distribution     |
| **Sensitive Content**           | Tag entries with `mcp:sensitive = true`; restrict AI summaries          |
| **Indigenous Data Sovereignty** | Follow Tribal NAGPRA and CARE Principles for Indigenous Data Governance |
| **Attribution**                 | Always credit speaker and source archive                                |
| **Preservation**                | Audio stored lossless (FLAC) with checksum for fixity                   |

---

## 🧩 CI Validation Hooks

| Check            | Tool                             | Purpose                   |
| :--------------- | :------------------------------- | :------------------------ |
| Metadata Syntax  | `stac-validator`                 | Ensures valid STAC fields |
| Checksum         | `sha256sum -c`                   | Verifies audio integrity  |
| Ontology Mapping | `scripts/check_cidoc_links.py`   | Confirms semantic classes |
| Graph Ingestion  | `scripts/graph_ingest_oral.py`   | Loads records into Neo4j  |
| License Audit    | `scripts/check_license_flags.py` | Confirms usage rights     |

Run:

```bash
make stac-validate
make docs-validate
```

---

## 🧠 MCP Compliance Summary

| Principle               | Implementation                                        |
| :---------------------- | :---------------------------------------------------- |
| **Documentation-first** | Integration logged here before pipeline execution     |
| **Reproducibility**     | Automated transcription + metadata generation scripts |
| **Open Standards**      | STAC 1.0 · CIDOC CRM · OWL-Time · PROV-O              |
| **Provenance**          | SHA256 + RDF chains link audio → transcript → graph   |
| **Auditability**        | CI logs under `data/work/logs/oral/`                  |

---

## 📎 Related Documentation

| File                                   | Purpose                                    |
| :------------------------------------- | :----------------------------------------- |
| `docs/integration/climate-hazards.md`  | Links narratives about storms and droughts |
| `docs/integration/deeds.md`            | Ties land stories to ownership records     |
| `docs/standards/ontologies.md`         | CIDOC/OWL-Time class reference             |
| `docs/notes/research.md`               | Research findings based on oral histories  |
| `docs/architecture/knowledge-graph.md` | Graph schema for audio + text entities     |

---

## 📅 Version History

| Version | Date       | Author                 | Summary                                                       |
| :------ | :--------- | :--------------------- | :------------------------------------------------------------ |
| v1.1    | 2025-10-05 | KFM Cultural Data Team | Added ethical framework, ontology table, and RDF examples     |
| v1.0    | 2025-10-04 | KFM Documentation Team | Initial oral history integration guide (STAC + CRM alignment) |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Voice Preserved. Every Story Proven.”*
📍 [`docs/integration/oral-histories.md`](.) · Official MCP-compliant oral history integration guide for the Kansas Frontier Matrix.

</div>


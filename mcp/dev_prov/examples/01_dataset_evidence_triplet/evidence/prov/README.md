# 🧾 PROV Evidence — Dataset Evidence Triplet (Example 01)

**Path:** `mcp/dev_prov/examples/01_dataset_evidence_triplet/evidence/prov/`  
**Companions:** `../stac/` 📦 + `../dcat/` 🗂️  
**Role in KFM:** PROV = **“how it was made”** (lineage + audit trail) 🔗 — the third leg of the **STAC/DCAT/PROV** evidence triplet.  [oai_citation:0‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) [oai_citation:1‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

| ✅ Item | Value |
|---|---|
| Example | `01_dataset_evidence_triplet` |
| Evidence type | `PROV` (W3C PROV-O / PROV-JSON via JSON-LD) |
| KFM metadata profile | `KFM-PROV` (versioned profile alongside KFM-STAC + KFM-DCAT)  [oai_citation:2‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) [oai_citation:3‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) |
| Principle | **Provenance-first**: no “mystery layers”, no black-box datasets, no uncited AI outputs  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC) |

---

> [!IMPORTANT]
> **Canonical pipeline order is non‑negotiable**: `sources → raw → work → processed → catalogs (STAC/DCAT) → PROV → graph → API → UI → Focus Mode`.  
> If any document suggests bypassing this order, it’s wrong by definition. ✅ [oai_citation:6‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:7‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 🧭 What lives in this folder

This folder holds **PROV bundles** (usually **JSON-LD**) that describe:

- **Entities** 📦: source files, intermediate artifacts, final dataset assets, published layers/items
- **Activities** ⚙️: ingestion runs, transforms, validations, publishing steps
- **Agents** 👤🤖: humans, CI runners, pipeline services, AI assistants (when applicable)
- **Relationships** 🔗: `prov:used`, `prov:wasGeneratedBy`, `prov:wasDerivedFrom`, `prov:wasAssociatedWith`, etc.  [oai_citation:8‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### 📁 Suggested example layout

```text
mcp/dev_prov/examples/01_dataset_evidence_triplet/
└─ evidence/
   ├─ stac/        🧭 “where/when + assets”
   ├─ dcat/        🗂️ “what/why/legal”
   └─ prov/        🧾 “how (lineage + audit)”
      ├─ README.md
      ├─ example-01.prov.jsonld
      └─ example-01.run_manifest.json   (optional, but recommended)
```

KFM commonly stores PROV in `data/prov/` (Master Guide v13 naming) **or** `data/provenance/` (older/alternate naming). Keep your implementation consistent with the repo’s chosen convention.  [oai_citation:9‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

---

## 🧩 How PROV fits the “Evidence Triplet”

KFM treats each dataset as a **triplet**:

- **STAC** 📦: spatial/temporal assets and discovery
- **DCAT** 🗂️: dataset‑level catalog semantics (owner/provider/license/description)
- **PROV** 🧾: lineage chain (inputs → processes → outputs → responsible agents)

This triplet is both a **data contract** and a **trust mechanism** (no dataset is allowed into the system without the evidence).  [oai_citation:11‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

---

## 🧾 KFM‑PROV “practical profile” (what we expect)

Even in examples, the PROV bundle should make these questions answerable:

1. **What** was produced? (entity IDs + locations + checksums)  
2. **From what** inputs? (source IDs + retrieval receipts + time windows)  
3. **How** was it produced? (activity + plan/config + parameters + tool versions)  
4. **By whom/what**? (agents: human + service/CI)  
5. **When**? (run timestamps + validity window)  
6. **Under what rules**? (license + sensitivity classification + policy gate results)

KFM’s governance/policy gates explicitly require schema correctness, STAC/DCAT/PROV completeness, license presence, sensitivity classification, and provenance completeness (fail‑closed).  [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

> [!TIP]
> If you already generate a **Run Manifest** (run_id, run_time, tool_versions, inputs/outputs, canonical digest), you can reference it from PROV and/or translate it into PROV Activities/Entities.  [oai_citation:14‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 🧪 Minimal PROV JSON‑LD bundle (example)

Below is a **minimal** PROV bundle pattern used in KFM documentation: entities + activity + agent, with `used` and `wasGeneratedBy` relationships.  [oai_citation:15‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

```json
{
  "@context": "https://www.w3.org/ns/prov.jsonld",
  "@id": "urn:kfm:prov:bundle:example-01:run-2026-01-21T00:00:00Z",

  "entity": {
    "urn:kfm:entity:source:input-a": {
      "prov:label": "Input A (raw source extract)",
      "prov:type": "prov:Entity",
      "kfm:sha256": "REPLACE_WITH_SHA256",
      "prov:location": "data/raw/example-01/input-a.ext",
      "kfm:source_id": "kfm.source.example.input-a"
    },
    "urn:kfm:entity:dataset:output-layer": {
      "prov:label": "Output Layer (processed dataset)",
      "prov:type": "prov:Entity",
      "kfm:sha256": "REPLACE_WITH_SHA256",
      "prov:location": "data/processed/example-01/output-layer.pmtiles",
      "kfm:dataset_id": "kfm.dataset.example.output-layer@v1"
    }
  },

  "activity": {
    "urn:kfm:activity:pipeline:example-01": {
      "prov:type": "prov:Activity",
      "prov:label": "Example 01 ingestion pipeline run",
      "prov:startedAtTime": "2026-01-21T00:00:00Z",
      "prov:endedAtTime": "2026-01-21T00:02:15Z",
      "kfm:run_id": "run_2026-01-21T00:00:00Z_example-01",
      "kfm:pipeline_ref": "pipelines/example-01/pipeline.yaml",
      "kfm:git_sha": "REPLACE_WITH_COMMIT_SHA",
      "kfm:policy_pack": "policy/v13",
      "kfm:run_manifest": "evidence/prov/example-01.run_manifest.json"
    }
  },

  "agent": {
    "urn:kfm:agent:ci": {
      "prov:type": "prov:Agent",
      "prov:label": "CI Runner",
      "kfm:system": "ci"
    }
  },

  "used": {
    "urn:kfm:activity:pipeline:example-01": [
      "urn:kfm:entity:source:input-a"
    ]
  },

  "wasGeneratedBy": {
    "urn:kfm:entity:dataset:output-layer": "urn:kfm:activity:pipeline:example-01"
  },

  "wasAssociatedWith": {
    "urn:kfm:activity:pipeline:example-01": "urn:kfm:agent:ci"
  }
}
```

> [!NOTE]
> KFM commonly uses **stable identifiers** (URNs/DOIs/IDs) so provenance edges remain durable as the repository evolves.  [oai_citation:16‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 🔗 Cross‑linking expectations (STAC ⇄ DCAT ⇄ PROV)

KFM explicitly expects the three standards to be **cross-linked**, not siloed.  [oai_citation:17‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### STAC → PROV
STAC Items/Collections can include a provenance pointer (for example, an `assets.provenance` link or a `links[]` entry).  [oai_citation:18‡Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf](file-service://file-RrXMFY7cP925exsQYermf2)

### DCAT → STAC + PROV
DCAT records aggregate dataset metadata, and KFM uses DCAT + STAC alignment so catalogs can route users/tools to both assets and lineage.  [oai_citation:19‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### PROV → Graph
PROV is used to generate lineage edges in the knowledge graph so the system can answer:
- “Which datasets did this layer come from?”
- “Which pipeline run produced this artifact?”
- “Which stories/pulses depend on this dataset?”  [oai_citation:20‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) [oai_citation:21‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## ✅ Validation & policy gates (fail‑closed)

KFM uses **validators** (JSON Schema / SHACL) and **policy gates** to enforce that provenance is complete and consistent.  [oai_citation:22‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) [oai_citation:23‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

### What *must* be true before merge/publish
- A dataset cannot be published without STAC/DCAT/PROV completeness and a known license.  [oai_citation:24‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- If processed data changes, provenance must change accordingly (no “silent” edits).  [oai_citation:25‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- Focus Mode outputs must have citations; otherwise it refuses (policy violation).  [oai_citation:26‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

---

## 🧠 UI + Focus Mode: provenance is user-facing (not just backend)

KFM’s UI is designed to show the **“map behind the map”** — every layer and story should surface lineage, license, and citations.  [oai_citation:27‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)

- Layer Info dialogs include **source/metadata** (and are designed to expand into a **Layer Provenance panel** listing citations).  [oai_citation:28‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- Exported maps/views can include an attribution/provenance snippet so context isn’t lost.  [oai_citation:29‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- Architecture explicitly calls out provenance metadata as necessary for trustworthy outputs and citations in Focus Mode.  [oai_citation:30‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

---

## 🧪 MCP context: “Methods & Computational Experiments”

This example lives under `mcp/` because KFM treats reproducible runs, notebooks, and method artifacts as first‑class engineering objects (not “side notes”).  [oai_citation:31‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

> [!GOOD PRACTICE]
> When a dataset is created from a computational experiment (e.g., notebook run), record:
> - notebook ID / run ID
> - environment (tool versions)
> - inputs and outputs
> - canonical digest / reproducibility keys  
> and tie them into PROV.  [oai_citation:32‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T) [oai_citation:33‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 🚀 Advanced patterns (how this scales beyond the example)

### ⏱️ Streaming + real-time updates
Future proposals describe watcher pipelines that generate STAC items + DCAT entries and update provenance tags/metadata during ingestion.  [oai_citation:34‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)

### 🧾 Evidence-first narratives (Story Nodes, Pulse Threads)
Pulse/Story content can ship with:
- a human-readable citations block
- a machine-readable evidence manifest
- an embedded PROV snippet linking narrative → evidence → creation activity  [oai_citation:35‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T) [oai_citation:36‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### 📦 OCI artifacts + signed provenance (supply chain for data)
KFM proposals include storing large data artifacts in registries and attaching **PROV JSON-LD** as an artifact “referrer,” with signing to provide a certificate of origin.  [oai_citation:37‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T) [oai_citation:38‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### 🧠 GeoXAI & explainability
Innovations like GeoXAI and evidence-based AI assistants become far more credible when the system can show lineage and the exact inputs behind model outputs.  [oai_citation:39‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC) [oai_citation:40‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)

---

## 🔐 Security, privacy, and governance (provenance is part of safety)

- Policy gates encode ethics + quality checks (license, sensitivity, provenance completeness).  [oai_citation:41‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- Provenance is also an **audit surface**: query auditing, inference control, logging/monitoring help manage risk and misuse.  [oai_citation:42‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)

---

## 🧰 Troubleshooting (common PROV issues)

- **“I updated processed data but didn’t touch provenance.”**  
  Expect CI/policy failure. Update the PROV bundle and (ideally) run manifest.  [oai_citation:43‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

- **“My PROV exists, but nothing links to it.”**  
  Ensure STAC and/or DCAT include a pointer to the PROV bundle (cross-link expectation).  [oai_citation:44‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

- **“The UI can’t show lineage for this layer.”**  
  If provenance isn’t present (or is malformed), the layer becomes a “mystery layer,” which conflicts with KFM’s contract-first stance.  [oai_citation:45‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 📚 Reference libraries included in the project (PDF portfolios)

KFM ships several **PDF portfolios** that bundle deeper technical references (AI, geospatial, programming, data management). Open them with a portfolio-capable reader for full access.  
- AI references 📦: `AI Concepts & more.pdf`  [oai_citation:46‡AI Concepts & more.pdf](file-service://file-K6BctJjeUwvyCahLf9qdwr)  
- Geospatial + WebGL references 🗺️: `Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf`  [oai_citation:47‡Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf](file-service://file-RshcX5sNY2wpiNjRfoP6z6)  
- Programming language references 🧰: `Various programming langurages & resources 1.pdf`  [oai_citation:48‡Various programming langurages & resources 1.pdf](file-service://file-4wp3wSSZs7gk5qHWaJVudi)  
- Data management references 🗄️: `Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf`  [oai_citation:49‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

---

## ✅ “Definition of done” checklist for PROV in this example

- [ ] PROV bundle exists (JSON-LD) and parses
- [ ] Entities include **inputs + outputs** (with locations and checksums where possible)
- [ ] Activity includes `run_id` / timestamps / plan reference
- [ ] Agent is recorded (CI/service or human)
- [ ] `used` and `wasGeneratedBy` relationships connect inputs → activity → outputs
- [ ] STAC and/or DCAT link to this PROV bundle
- [ ] Passes schema validation + policy gates (fail-closed)  [oai_citation:50‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

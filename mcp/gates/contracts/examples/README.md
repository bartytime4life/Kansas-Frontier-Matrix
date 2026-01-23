# 🧱🔐 MCP Contracts & Gates — Examples

![Policy as Code](https://img.shields.io/badge/policy%20as%20code-OPA%20%2B%20Conftest-7D64FF)
![Contracts](https://img.shields.io/badge/contracts-JSON%20Schema%20%7C%20JSON--LD%20%7C%20OpenAPI-1f6feb)
![Evidence Triplet](https://img.shields.io/badge/evidence-STAC%20%2B%20DCAT%20%2B%20PROV-0ea5e9)
![Governance](https://img.shields.io/badge/governance-fail--closed-critical)
![FAIR+CARE](https://img.shields.io/badge/principles-FAIR%20%2B%20CARE-22c55e)
![Supply Chain](https://img.shields.io/badge/supply%20chain-SBOM%20%2B%20SLSA%20%2B%20Cosign-64748b)

> **Purpose 🎯**: This folder is a copy/paste-friendly “sandbox” of **example contracts** (schemas) and **example gates** (policy checks) used by **KFM’s Master Coder Protocol (MCP)** to keep data, AI outputs, UI layers, and narratives **governed**, **reproducible**, and **provenance-linked**.
>
> **Examples only ⚠️**: These files are meant to teach patterns and accelerate implementation. Canonical rules should live in `mcp/gates/` + `mcp/gates/contracts/` (or your repo’s single source-of-truth location).

---

## 🧠 The mental model (super quick)

### ✅ Contract
A **contract** describes *what valid looks like*:
- shape (fields, types)
- constraints (required fields, enums, formats)
- IDs + versioning
- provenance pointers (STAC/DCAT/PROV references)

### 🚦 Gate
A **gate** enforces validity at boundaries:
- **CI gates** (PR merge blockers)
- **Pipeline gates** (ingestion + ETL)
- **Runtime gates** (API + Focus Mode output checks)

🔒 **Fail-closed by default**: if we can’t validate provenance / safety / compliance, we don’t publish.

---

## 🧭 KFM’s “evidence-first” invariant (the triplet rule)

KFM treats these as a minimum **evidence triplet** for anything that appears in the UI, feeds the graph, or is quoted by the AI:

- **STAC** → *assets* (rasters/vectors/collections + spatiotemporal extent)
- **DCAT** → *dataset metadata* (license, publisher/provider, description)
- **PROV** → *lineage* (inputs → processing activity → outputs)

If a layer/story/answer is missing **any** part of the triplet, it should be blocked by gates. ✅📚🧾

---

## 🗂️ Suggested example layout

> Your repo may differ — this is a recommended structure that matches KFM’s “contracts + policy packs + payloads” mindset.

```text
mcp/gates/contracts/examples/
├─ 📜📄 README.md                          # 👈 you are here 📌 How to use these examples (validate schemas, run gates, add cases)
├─ 📐 contracts/                           # 📐 “What valid looks like”: example schema files used by docs/tests
│  ├─ 🧾📐 run_manifest.schema.json         # Run manifest contract (who/what/when + inputs/outputs + digests)
│  ├─ 📎📐 evidence_manifest.schema.json    # Evidence manifest contract (claims→citations→artifacts)
│  ├─ 🤖📐 focus_answer_artifact.schema.json # Focus Mode answer artifact contract (citations, redactions, receipts)
│  ├─ 🧵📐 pulse_thread.schema.json         # Pulse thread contract (short narrative + evidence bundle)
│  ├─ 🧠📐 concept_node.schema.json         # Concept node contract (graph-ish knowledge unit + refs)
│  └─ 🧭📐 ui_context.schema.json           # UI context contract (safe client context snapshot; no sensitive leakage)
├─ 🧪 payloads/                            # 🧪 “Example instances”: valid sample payloads that conform to the schemas
│  ├─ ✅🧾 run_manifest.example.json        # Example run receipt (deterministic fields + hashes)
│  ├─ ✅📎 evidence_manifest.example.yml    # Example evidence manifest (YAML form; mirrors JSON structure)
│  ├─ ✅🤖 focus_answer.example.json        # Example Focus Mode output (citations required + uncertainty/limits)
│  ├─ ✅🧵 pulse_thread.example.json        # Example pulse thread instance (meta + narrative + evidence refs)
│  ├─ ✅🧠 concept_node.example.json        # Example concept node (ids, labels, citations, relationships)
│  └─ ✅🧭 ui_context.example.json          # Example safe UI context (route/map/session metadata, redacted)
├─ 🚦 gates/                               # 🚦 “How we enforce”: policy rules + example waivers
│  ├─ ⚖️ rego/                             # ⚖️ OPA/Rego gate rules (deny-by-default patterns)
│  │  ├─ ⚖️📄 KFM-CAT-001-license-required.rego           # Requires explicit license fields in catalogs/manifests
│  │  ├─ ⚖️📄 KFM-PROV-001-prov-required.rego             # Requires PROV linkage for processed/derived artifacts
│  │  ├─ ⚖️📄 KFM-EVID-001-citations-match-evidence.rego  # Ensures citations resolve to evidence manifest entries
│  │  ├─ ⚖️📄 KFM-AI-001-citations-required.rego          # Requires citations for AI outputs (evidence-first)
│  │  ├─ ⚖️📄 KFM-SEC-001-sensitive-redaction.rego        # Enforces redaction/sensitivity rules (no secrets/PII)
│  │  └─ ⚖️📄 KFM-PIPE-001-pipeline-ordering.rego         # Enforces canonical pipeline ordering / linkage expectations
│  └─ 🧯🧾 waivers.example.yml                 # Example waiver file (time-boxed exceptions with ids/rationale/expiry)
└─ 🧪 tests/                                # 🧪 Regression suite: known-pass and known-fail cases for CI
   ├─ ✅ pass/                               # Inputs that MUST pass (guard against over-blocking)
   └─ ❌ fail/                               # Inputs that MUST fail (guard against under-blocking)
```

---

## 🧪 Run these examples locally

### Option A: JSON Schema validation (contracts)
```bash
# Python-based quick validation
python -m pip install jsonschema pyyaml

python -m jsonschema \
  -i payloads/run_manifest.example.json \
  contracts/run_manifest.schema.json
```

### Option B: OPA/Conftest (gates)
```bash
# Requires conftest + opa installed
conftest test payloads/ --policy gates/rego --all-namespaces
```

### Option C: CI-style “single command”
```bash
make gates
# recommended: gates = lint + schema validation + conftest + secret scan + (optional) signing checks
```

---

## 🚦 Gate matrix (what we enforce and where)

| Gate ID 🆔 | What it prevents 🚫 | Boundary 🧱 | Typical inputs |
|---|---|---|---|
| `KFM-CAT-001` | “mystery” datasets (missing license/publisher) | CI + intake | DCAT JSON/JSON-LD |
| `KFM-PROV-001` | publishing outputs without lineage | CI + pipeline | PROV bundle refs |
| `KFM-EVID-001` | narrative claims without evidence links | CI + runtime | Story/Focus artifacts |
| `KFM-AI-001` | AI answers without citations/confidence | runtime | Focus Mode output |
| `KFM-SEC-001` | leaking sensitive coords / PIIs | CI + runtime | payloads + UI config |
| `KFM-PIPE-001` | bypassing catalogs (graph/UI updated first) | CI | changed file set / manifests |
| `KFM-API-001` | UI bypassing API boundary | CI | `web/` dependency + code scan |
| `KFM-SUP-001` | unsigned/unverifiable artifacts | pipeline + release | SBOM/SLSA/Cosign |

> 💡 Tip: Keep gate IDs stable and human-readable: `KFM-<DOMAIN>-<NNN>` (ex: `KFM-AI-001`, `KFM-PROV-001`).

---

## 🧾 Example contracts (schemas + payloads)

### 1) 🧾 `RunManifest` — deterministic pipeline receipt
**Why:** KFM pipelines should produce a run ledger (inputs, outputs, tool versions, counts, errors) and include a **canonical digest** (RFC 8785-style canonicalization + SHA-256) to support idempotency + provenance.

✅ Example payload (`payloads/run_manifest.example.json`)
```json
{
  "schema_version": "1.0.0",
  "run_id": "2026-02-01T03:14:15Z__kfm.dataset.example.v2",
  "dataset_id": "kfm.dataset.example.v2",
  "pipeline": {
    "name": "pipelines/georef_and_cog",
    "version": "13.2.0",
    "container_image": "ghcr.io/kfm/pipelines/georef_and_cog@sha256:REPLACE_ME"
  },
  "source_urls": [
    "https://example.org/source/ellis_co_1894_map.tif"
  ],
  "inputs": [
    {
      "uri": "data/raw/maps/ellis_co_1894_map.tif",
      "sha256": "REPLACE_ME",
      "byte_size": 123456789
    }
  ],
  "outputs": [
    {
      "path": "data/processed/maps/ellis_co_1894_map.cog.tif",
      "sha256": "REPLACE_ME",
      "media_type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "crs": "EPSG:4326"
    }
  ],
  "tool_versions": {
    "python": "3.12.1",
    "gdal": "3.8.2"
  },
  "summary_counts": {
    "records_in": 1,
    "records_out": 1,
    "errors": 0
  },
  "evidence_triplet": {
    "stac_ref": "data/stac/maps/ellis_co_1894_map.collection.json",
    "dcat_ref": "data/catalogs/dcat/kfm.dataset.example.v2.jsonld",
    "prov_ref": "data/prov/runs/2026-02-01__kfm.dataset.example.v2.prov.jsonld"
  },
  "canonical_digest": "sha256:REPLACE_ME",
  "idempotency_key": "sha256:REPLACE_ME"
}
```

✅ Minimal schema fragment (`contracts/run_manifest.schema.json`)
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Run Manifest",
  "type": "object",
  "required": [
    "schema_version",
    "run_id",
    "dataset_id",
    "pipeline",
    "inputs",
    "outputs",
    "tool_versions",
    "summary_counts",
    "evidence_triplet",
    "canonical_digest",
    "idempotency_key"
  ],
  "properties": {
    "schema_version": { "type": "string" },
    "run_id": { "type": "string" },
    "dataset_id": { "type": "string" },
    "pipeline": {
      "type": "object",
      "required": ["name", "version"],
      "properties": {
        "name": { "type": "string" },
        "version": { "type": "string" },
        "container_image": { "type": "string" }
      }
    },
    "inputs": {
      "type": "array",
      "items": { "type": "object", "required": ["uri", "sha256"] }
    },
    "outputs": {
      "type": "array",
      "items": { "type": "object", "required": ["path", "sha256"] }
    },
    "evidence_triplet": {
      "type": "object",
      "required": ["stac_ref", "dcat_ref", "prov_ref"],
      "properties": {
        "stac_ref": { "type": "string" },
        "dcat_ref": { "type": "string" },
        "prov_ref": { "type": "string" }
      }
    }
  }
}
```

---

### 2) 🧾 `EvidenceManifest` — citations must map to evidence IDs
**Why:** Story Nodes and Focus Mode content must be machine-checkable: each claim/footnote points to an entry in an evidence manifest, which itself points to cataloged sources.

✅ Example payload (`payloads/evidence_manifest.example.yml`)
```yaml
schema_version: "1.0.0"
artifact_id: "SN-1936-DUST-BOWL-HEAT"
generated_at: "2026-02-01T12:00:00Z"

evidence:
  - id: "E-001"
    kind: "dataset"
    dcat_ref: "data/catalogs/dcat/kfm.dataset.drought_index.v1.jsonld"
    stac_ref: "data/stac/climate/drought_index.collection.json"
    note: "1930s drought index layer used in narrative + map overlay"

  - id: "E-002"
    kind: "document"
    uri: "data/library/usgs_historical_topo_guide.pdf"
    locator:
      page: 12
    note: "USGS reference for historic topo map handling"

transforms:
  - run_manifest_ref: "data/audits/2026-02-01__kfm.dataset.drought_index.v1/run_manifest.json"
    prov_ref: "data/prov/runs/2026-02-01__kfm.dataset.drought_index.v1.prov.jsonld"
```

✅ Gate expectation
- `KFM-EVID-001` should deny if a citation references `E-999` but evidence list has no `E-999`.

---

### 3) 🧠 `FocusAnswerArtifact` — the AI output becomes governed data
**Why:** Focus Mode must:
- cite sources (or refuse)
- respect sensitivity policies
- record provenance + governance flags
- include uncertainty / confidence for interpretive content

✅ Example payload (`payloads/focus_answer.example.json`)
```json
{
  "schema_version": "1.0.0",
  "answer_id": "FA-2026-02-01T12:34:56Z-acde",
  "question": "What is noteworthy about this county in the 1930s?",
  "context": {
    "bbox_wgs84": [-100.5, 37.0, -99.5, 38.0],
    "time_range": { "start": "1930-01-01", "end": "1939-12-31" },
    "active_layer_ids": ["kfm.layer.drought_index_1930s"]
  },
  "answer_markdown": "The drought severity increased in mid-1930s according to the drought index layer.[^E-001]\n\n[^E-001]: See evidence E-001.",
  "citations": [
    { "evidence_id": "E-001", "kind": "dataset", "ref": "data/catalogs/dcat/kfm.dataset.drought_index.v1.jsonld" }
  ],
  "confidence": 0.74,
  "governance_flags": [
    { "code": "EVIDENCE_LINKED", "severity": "info", "message": "All claims mapped to evidence entries." }
  ],
  "evidence_manifest_ref": "payloads/evidence_manifest.example.yml",
  "prov_ref": "data/prov/answers/FA-2026-02-01T12:34:56Z-acde.prov.jsonld"
}
```

---

### 4) ⚡ `PulseThread` — geotagged micro-story for “what’s happening here?”
**Why:** Pulse Threads are short, time-stamped narratives that connect map context + story context with evidence links.

✅ Example payload (`payloads/pulse_thread.example.json`)
```json
{
  "schema_version": "1.0.0",
  "pulse_id": "PT-2026-02-01-001",
  "title": "Drought signals intensify across the corridor",
  "created_at": "2026-02-01T15:20:00Z",
  "geo": {
    "bbox_wgs84": [-100.5, 37.0, -99.5, 38.0],
    "place_ids": ["kfm.place.county.ford_ks"]
  },
  "time_range": { "start": "1934-01-01", "end": "1936-12-31" },
  "narrative_markdown": "Map layers show sustained drought severity peaks.[^E-001]\n\n[^E-001]: Evidence E-001.",
  "evidence_manifest_ref": "payloads/evidence_manifest.example.yml",
  "prov_ref": "data/prov/pulse/PT-2026-02-01-001.prov.jsonld",
  "tags": ["climate", "drought", "1930s"]
}
```

---

### 5) 🧩 `ConceptNode` — “Conceptual Attention Nodes” (pattern/hypothesis container)
**Why:** Concept nodes store structured hypotheses and “signals” that can be inspected, debated, and traced.

✅ Example payload (`payloads/concept_node.example.json`)
```json
{
  "schema_version": "1.0.0",
  "concept_id": "CAN-0007",
  "label": "Dust Bowl migration pressure indicator",
  "summary": "Hypothesis: drought severity + crop loss signals correlate with out-migration patterns.",
  "signals": [
    { "type": "dataset_ref", "evidence_id": "E-001" },
    { "type": "note", "text": "Add county-level population change dataset to strengthen test." }
  ],
  "status": "draft",
  "owners": ["@kfm-research"],
  "created_at": "2026-02-01T18:10:00Z"
}
```

---

### 6) 🗺️ `UIContext` — map viewport + time + active layers (Focus Mode input)
**Why:** Focus Mode is context-aware; we pass a constrained context bundle that can be validated + policy-checked.

✅ Example payload (`payloads/ui_context.example.json`)
```json
{
  "schema_version": "1.0.0",
  "bbox_wgs84": [-100.5, 37.0, -99.5, 38.0],
  "zoom": 8,
  "time_range": { "start": "1930-01-01", "end": "1939-12-31" },
  "active_layer_ids": ["kfm.layer.drought_index_1930s"],
  "interaction": { "selected_feature_id": "kfm.feature.county.ford_ks" }
}
```

---

## 🔐 Example gates (OPA/Rego snippets)

> These are intentionally short. In the real policy pack, each rule should include:
> - stable ID (`KFM-…`)
> - clear deny message (actionable)
> - optional waiver support (with expiry)

### `KFM-AI-001` — citations required for AI output
```rego
package kfm.ai

deny[msg] {
  input.kind == "focus_answer"
  count(input.citations) == 0
  msg := "KFM-AI-001: Focus Mode answer must include at least one citation (or refuse)."
}
```

### `KFM-CAT-001` — license required in DCAT record
```rego
package kfm.catalog

deny[msg] {
  input.kind == "dcat_dataset"
  not input.license
  msg := "KFM-CAT-001: Dataset missing license (no data without known terms)."
}
```

### `KFM-PROV-001` — provenance required before publish
```rego
package kfm.prov

deny[msg] {
  input.kind == "publishable_artifact"
  not input.prov_ref
  msg := "KFM-PROV-001: Artifact missing prov_ref (provenance-first publishing)."
}
```

### `KFM-EVID-001` — citations must match evidence manifest IDs
```rego
package kfm.evidence

deny[msg] {
  input.kind == "focus_answer"
  some i
  cid := input.citations[i].evidence_id
  not evidence_exists(cid)
  msg := sprintf("KFM-EVID-001: citation evidence_id '%s' not found in evidence manifest.", [cid])
}

evidence_exists(cid) {
  some j
  input.evidence_manifest.evidence[j].id == cid
}
```

### `KFM-SEC-001` — sensitive coordinate redaction
```rego
package kfm.security

deny[msg] {
  input.kind == "ui_layer"
  input.sensitivity == "restricted"
  input.exposes_precise_coordinates == true
  msg := "KFM-SEC-001: Restricted layer must not expose precise coordinates (require fuzzing/aggregation)."
}
```

### `KFM-PIPE-001` — pipeline ordering (no bypass)
```rego
package kfm.pipeline

deny[msg] {
  input.changed.graph_updated
  not input.changed.catalogs_updated
  msg := "KFM-PIPE-001: Graph updates require catalog updates (STAC/DCAT/PROV) in the same change."
}
```

---

## 🧑‍⚖️ Waivers (rare, time-boxed, auditable)

Waivers exist for reality (e.g., license pending, upstream metadata delay), but should be:
- **explicit**
- **scoped** (glob/path/IDs)
- **time-boxed** (expiry date)
- **approved** (named reviewer)

Example (`gates/waivers.example.yml`)
```yaml
waivers:
  - id: "KFM-CAT-001"
    scope:
      paths:
        - "data/catalogs/dcat/pending/**"
    reason: "Upstream license statement pending written confirmation."
    expires: "2026-03-01"
    approved_by: "@maintainer-handle"
```

---

## 🧭 How this fits KFM’s overall system (contracts everywhere)

KFM is designed as modular subsystems with explicit “do not break” invariants:
- ETL deterministic + replayable
- Catalogs machine-validated (STAC/DCAT/PROV)
- Graph schema stable (migrations required)
- API contract-first (OpenAPI/GraphQL)
- UI respects redaction + provenance
- Story/Focus provenance-linked only (no hallucinations)

---

## 🧰 Contributor recipes (add new stuff safely)

### ✅ Add a new data layer / dataset
1. Add/refresh processed data artifact(s)
2. Add **STAC** + **DCAT** records
3. Add **PROV** bundle linking inputs → activity → outputs
4. Update layer registry / API endpoint (contract-first)
5. Run gates (schema + rego + tests)
6. Ensure UI popup/legend cites provenance source

### ✅ Add a new Story Node
1. Create `story.md` + `story.json` (or your Story Node format)
2. Create/refresh `evidence_manifest.yml`
3. Ensure citations map to evidence IDs
4. Add PROV record if story is derived/processed
5. Run gates (especially `KFM-EVID-001`, `KFM-PROV-001`)

### ✅ Add a new Focus Mode tool / capability
1. Define the **contract first** (request + response schemas)
2. Add a runtime gate (OPA) for safety + provenance
3. Add telemetry/audit artifact output contract (so it becomes governed data)
4. Add tests: pass + fail payloads

---

## 📦 Reference libraries included in this project (PDF portfolios)

Some “project files” are **PDF portfolios** (they contain many embedded PDFs). They’re included to support deep implementation work (AI, geospatial/WebGL, data engineering, security, language notes).

<details>
<summary>📚 What’s inside (high level)</summary>

- **AI Concepts & more.pdf** 🤖  
  Embedded references for AI systems, probabilistic ML, deep learning, RL, and building AI apps.

- **Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf** 🗺️🕹️  
  Embedded references for map design, projections, Google Earth Engine, Google Maps APIs, and WebGL.

- **Data Managment-Theories-…-Baysian Methods-…pdf** 🧮🔐  
  Embedded references for data engineering, CI/CD for data+software, cryptography/network security, Bayesian methods, clean architecture.

- **Various programming langurages & resources 1.pdf** 💻  
  Embedded “Notes for Professionals” across many languages + extra technical references.

</details>

### 🔍 Optional: extract embedded PDFs (utility snippet)
```python
# Use this if you want to unpack portfolio PDFs into a folder for grep/search.
# (Works for many portfolios using PyMuPDF/fitz.)
import fitz
from pathlib import Path

portfolio = Path("AI Concepts & more.pdf")  # change as needed
out_dir = Path("mcp/_unpacked_portfolio") / portfolio.stem
out_dir.mkdir(parents=True, exist_ok=True)

doc = fitz.open(portfolio)
for name in doc.embfile_names():
  data = doc.embfile_get(name)
  (out_dir / name).write_bytes(data)

print(f"Extracted {len(doc.embfile_names())} files to {out_dir}")
```

---

## ✅ Definition of Done (DoD) for adding new contracts/gates/examples

- [ ] Contract exists (schema) 📜
- [ ] At least one **PASS** payload ✅
- [ ] At least one **FAIL** payload ❌
- [ ] Gate produces actionable deny messages 🧯
- [ ] Waiver path exists (but not required) ⏳
- [ ] Provenance pointers included (STAC/DCAT/PROV refs) 🧾
- [ ] Sensitivity/redaction considered (FAIR+CARE) 🛡️
- [ ] CI command documented (how to run locally) 🧪

---

## 📚 Design references (project docs this folder aligns with)

These examples mirror patterns described across the KFM documentation set:

- `📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf`  
- `Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf`  
- `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf`  
- `Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf`  
- `Kansas Frontier Matrix – Comprehensive UI System Overview.pdf`  
- `🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf`  
- `Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf`  
- `Additional Project Ideas.pdf`  
- `Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf`  
- `MARKDOWN_GUIDE_v13.md.gdoc`  

> 🧭 If you’re unsure where to start: implement **RunManifest + EvidenceManifest + FocusAnswerArtifact** contracts, then wire up **KFM-AI-001 / KFM-PROV-001 / KFM-CAT-001** as your first “hard gates”.

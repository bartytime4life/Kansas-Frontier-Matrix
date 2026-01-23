# 📐 Data Schema Contracts — MCP Gates (KFM)

![Contract-First](https://img.shields.io/badge/Contract--First-required-2ea44f)
![Evidence-First](https://img.shields.io/badge/Evidence--First-provenance%20linked-2ea44f)
![Fail-Closed](https://img.shields.io/badge/Safety-fail--closed-critical)
![JSON%20Schema](https://img.shields.io/badge/JSON%20Schema-draft%202020--12-blue)
![OPA](https://img.shields.io/badge/OPA%2FRego-policy%20gates-purple)

> **Goal 🎯**: This folder defines the **data-side contracts** (schemas + profiles) that power **MCP gates** across the Kansas Frontier Matrix (KFM): ingestion, publication, UI/story content, packaging, and AI outputs.  
> KFM treats “schemas + provenance + policy” as first-class infrastructure — **no mystery layers, no uncited answers, no bypassing the pipeline**. :contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}

---

## 🔗 Quick Jump
- [Why this exists](#-why-this-exists)
- [Contracts vs Gates](#-contracts-vs-gates)
- [Folder layout](#-folder-layout)
- [Schema catalog](#-schema-catalog)
- [Core contract families](#-core-contract-families)
- [Validation (local + CI)](#-validation-local--ci)
- [Versioning + compatibility](#-versioning--compatibility)
- [Adding a new domain](#-adding-a-new-domain)
- [Contribution checklist](#-contribution-checklist)
- [Sources & project files](#-sources--project-files)

---

## 🧭 Why this exists

KFM’s architecture is **contract-first**: every dataset (and many derived artifacts) must ship with a **metadata JSON “data contract”** containing source, license, spatial/temporal extent, and processing steps — enforced via validators and CI. This supports automatic attribution and ensures Focus Mode can return **citations** rather than “trust me” answers. :contentReference[oaicite:2]{index=2}

KFM also has **automated policy gates** that (at minimum) enforce:
- schema validity  
- STAC/DCAT/PROV completeness  
- license presence  
- sensitivity classification + handling  
- provenance completeness  
- **AI answers must include citations** (or refuse)  
- **fail-closed** behavior if checks can’t run or data is uncertain :contentReference[oaicite:3]{index=3}:contentReference[oaicite:4]{index=4}

---

## 🚦 Contracts vs Gates

### Contracts 📜
Machine-readable rules for **shape + meaning** of artifacts:
- JSON Schema for structural validation
- Profiles/extensions (KFM-STAC, KFM-DCAT, KFM-PROV, KFM-specific)
- “Sidecar” configs for UI/Story Nodes
- Manifest schemas (evidence manifests, artifact refs, AI answer envelopes)

### Gates 🛡️
Automated enforcement points:
- **Ingestion gates** (validators) raise errors if constraints fail :contentReference[oaicite:5]{index=5}
- **CI gates** (e.g., Conftest policy tests) fail PRs on violations :contentReference[oaicite:6]{index=6}
- **Policy gates** (OPA/Rego) enforce cross-file invariants like pipeline ordering and provenance-first publishing :contentReference[oaicite:7]{index=7}
- **Governance checks** for AI output (AnswerWithCitations) :contentReference[oaicite:8]{index=8}

---

## 🧱 Folder layout

> This README describes the **intended canonical structure** for `mcp/gates/contracts/data/schema/`.  
> If your repo already has a root-level `/schemas/` folder, treat this as the **MCP-facing view** (keep them in sync).

```text
mcp/gates/contracts/data/schema/
├── ✅📄 README.md                          # 👈 you are here 📌 What lives here, how validation works, and how to add/update schemas
├── 📐 profiles/                            # 📐 Authoritative JSON Schemas (source of truth for contract validation)
│   ├── 🗄️📐🧾 kfm.dataset.schema.json       # Dataset contract (identity, license, distributions, classification, links)
│   ├── 🛰️📐🧾 kfm.stac.item.schema.json     # STAC Item + KFM profile overlay (assets/links/time/extent rules)
│   ├── 🗂️📐🧾 kfm.dcat.dataset.schema.json  # DCAT Dataset/Distribution + KFM extensions (discovery + access policy)
│   ├── 🧬📐🧾 kfm.prov.bundle.schema.json    # PROV bundle (entities/activities/agents + derivation/linkage constraints)
│   ├── 🎬📐🧾 kfm.story-node.config.schema.json # Story Node config (steps/actions/layers/time/citations pointers)
│   ├── 📎📐🧾 kfm.evidence-manifest.schema.json # Evidence manifest (claim→citation→artifact + digests/paths)
│   ├── 🗺️📐🧾 kfm.ui.layer.schema.json      # UI layer contract (sources, style refs, bounds, time-binding, legend refs)
│   ├── 🤖📐🧾 kfm.ai.answer.schema.json      # AI answer envelope (citations required, uncertainty, redactions, receipts)
│   └── 📦📐🧾 kfm.oci.artifact-ref.schema.json # OCI artifact reference (registry/repo/digest/mediaType/annotations)
├── 🧪 examples/                             # 🧪 Minimal + golden examples (docs/tests; should validate cleanly)
│   ├── ✅🧾 dataset.contract.example.json    # Example dataset contract instance (known-good baseline)
│   ├── ✅🧾 stac.item.example.json           # Example STAC Item instance (known-good)
│   ├── ✅🧾 dcat.dataset.example.jsonld      # Example DCAT dataset/distributions (known-good)
│   ├── ✅🧾 prov.bundle.example.jsonld       # Example PROV bundle (known-good lineage)
│   ├── 🎬 story-node/                       # Story Node example bundle (content + config kept together)
│   │   ├── 📝📄 node.md                      # Narrative markdown (citations/refs; small fixture)
│   │   └── 🧭🧾 node.config.json             # Story config (steps/actions; references layers/time/citations)
│   ├── ✅📎 evidence-manifest.example.yaml   # Example evidence manifest (YAML form; mirrors JSON structure)
│   └── ✅🤖🧾 ai.answer.example.json         # Example AI answer (citations + redactions + uncertainty fields)
├── ✅ tests/                                # ✅ Contract tests (automated validation + invariants)
│   ├── 🧪 ajv/                              # JSON Schema validation harness (AJV configs + runner glue)
│   ├── ⚖️ conftest/                         # OPA/Rego invariants beyond schema (link rules, policy checks, “fail-closed”)
│   └── 🧩 fixtures/                         # Additional edge-case fixtures (pass/fail variants for regression coverage)
└── 🔁 migrations/                           # 🔁 Version bumps + migration notes (what changed, why, and how to update payloads)
```

---

## 🗺️ Schema catalog

<details>
<summary><strong>📚 Contract index (click to expand)</strong></summary>

| Contract / Schema | What it governs | Key gates that depend on it |
|---|---|---|
| `kfm.dataset.schema.json` | Dataset “data contract” metadata JSON (source/license/space/time/steps) | ingestion schema gate, license gate, provenance gate :contentReference[oaicite:9]{index=9}:contentReference[oaicite:10]{index=10} |
| `kfm.stac.item.schema.json` | STAC Items/Collections + KFM profile extensions | STAC completeness gate, pipeline ordering gate :contentReference[oaicite:11]{index=11}:contentReference[oaicite:12]{index=12} |
| `kfm.dcat.dataset.schema.json` | DCAT JSON-LD dataset catalog entries | DCAT completeness, provenance linkage, UI provenance popups :contentReference[oaicite:13]{index=13}:contentReference[oaicite:14]{index=14} |
| `kfm.prov.bundle.schema.json` | PROV JSON-LD lineage bundles | provenance gate, AI answer provenance/citation gate :contentReference[oaicite:15]{index=15}:contentReference[oaicite:16]{index=16} |
| `kfm.story-node.config.schema.json` | Story Node map-state config sidecar | story integrity gate, link + layer existence gate :contentReference[oaicite:17]{index=17}:contentReference[oaicite:18]{index=18} |
| `kfm.evidence-manifest.schema.json` | Evidence manifests (YAML/JSON) for Story Nodes | citation↔manifest alignment gate, provenance linking gate :contentReference[oaicite:19]{index=19} |
| `kfm.ui.layer.schema.json` | UI layer registry entries (provenance, redaction hints) | provenance UI gate, CARE redaction compliance gate :contentReference[oaicite:20]{index=20}:contentReference[oaicite:21]{index=21} |
| `kfm.ai.answer.schema.json` | Focus Mode “AnswerWithCitations” envelope | governance check gate, “no uncited claims” gate :contentReference[oaicite:22]{index=22}:contentReference[oaicite:23]{index=23} |
| `kfm.oci.artifact-ref.schema.json` | OCI artifact references + signatures/SBOM | supply chain + provenance attestation gates :contentReference[oaicite:24]{index=24}:contentReference[oaicite:25]{index=25} |

</details>

---

## 🧬 Core contract families

### 1) Dataset “Data Contract” 📦

**KFM requires a dataset contract before acceptance** — it’s how the platform prevents “mystery layers” and ensures attribution/citations can be generated automatically. :contentReference[oaicite:26]{index=26}

**Recommended minimal fields (conceptual):**
- `id` (stable, versioned)  
- `title`, `description`
- `license` (required)
- `spatial` + `temporal` extent
- `sources[]` (URLs/refs + capture metadata)
- `processing[]` (steps, tools, params, determinism)
- `provenance` (links to PROV bundle)
- `sensitivity` (FAIR+CARE classification)

> Example dataset ID pattern appears in graph ingestion output as: `kfm.ks.landcover.2000_2020.v1` :contentReference[oaicite:27]{index=27}

```json
{
  "schema_version": "1.0.0",
  "id": "kfm.ks.landcover.2000_2020.v1",
  "title": "Kansas Landcover 2000–2020",
  "license": "CC-BY-4.0",
  "spatial": { "bbox": [-102.05, 36.99, -94.59, 40.00], "crs": "EPSG:4326" },
  "temporal": { "start": "2000-01-01", "end": "2020-12-31" },
  "sources": [
    { "name": "…", "uri": "…", "retrieved_at": "…", "checksum": "sha256:…" }
  ],
  "processing": [
    { "step": "reproject", "tool": "gdalwarp", "params": { "t_srs": "EPSG:4326" } }
  ],
  "provenance": { "prov_bundle_ref": "data/prov/kfm.ks.landcover.2000_2020.v1.prov.jsonld" },
  "sensitivity": { "level": "public", "care_label": "none" }
}
```

**Gate expectations**
- ❌ reject if missing `license` :contentReference[oaicite:28]{index=28}
- ❌ reject if sensitivity is missing/incorrect :contentReference[oaicite:29]{index=29}
- ❌ reject if provenance is missing/incomplete :contentReference[oaicite:30]{index=30}

---

### 2) Boundary artifacts: STAC + DCAT + PROV 🔺

KFM’s pipeline is explicitly staged:
**Raw → ETL → STAC → DCAT → PROV → Graph → API → UI → Story Nodes → Focus Mode** :contentReference[oaicite:31]{index=31}

At publication time, KFM writes:
- STAC: `data/stac/collections/` + `data/stac/items/`  
- DCAT: `data/catalog/dcat/`  
- PROV: `data/prov/`  
…and treats these as required “boundary artifacts” before data is considered published. :contentReference[oaicite:32]{index=32}

> **Design rule 🧩**: If a domain needs custom metadata, extend the KFM STAC/DCAT profiles instead of adding ad-hoc fields. :contentReference[oaicite:33]{index=33}

---

### 3) Story Nodes: governed narrative as data 📖🧠

Story Nodes are not “just docs” — they’re **machine-ingestible governed artifacts**:
- they must include provenance/citations for factual claims  
- they should reference graph entities via stable IDs  
- they should distinguish facts vs interpretation :contentReference[oaicite:34]{index=34}

A Story Node is represented as a **folder** containing:
- a Markdown narrative file  
- a JSON config defining layers/camera/map-state for that node :contentReference[oaicite:35]{index=35}

#### Evidence manifests 🧾
Pulse proposals add a **machine-readable evidence manifest (YAML/JSON)** plus a PROV snippet so the system (and users) can verify exact supporting material. CI can validate that citations in the text have corresponding manifest entries and that references resolve. :contentReference[oaicite:36]{index=36}

**Minimal evidence manifest idea (conceptual):**
```yaml
schema_version: 1.0.0
story_node_id: kfm.story.railroads.expansion.1870.v1
evidence:
  - id: dcat:kfm.ks.railroads.1870.v1
    kind: dataset
    checksum: sha256:...
    locator: data/catalog/dcat/kfm.ks.railroads.1870.v1.jsonld
  - id: doc:news.kansasweekly.1870-05-03.p1
    kind: document
    checksum: sha256:...
    locator: data/processed/docs/news/kansasweekly/1870-05-03.pdf
prov:
  locator: data/prov/kfm.story.railroads.expansion.1870.v1.prov.jsonld
```

---

### 4) UI layer registry contracts 🗺️✨

KFM’s UI is **provenance-forward**: “every visualization is linked to its source data and metadata” (the “map behind the map”). :contentReference[oaicite:37]{index=37}

The UI is designed to be **configuration + standard-schema driven**, decoupled from backend via APIs, and reusable across regions. :contentReference[oaicite:38]{index=38}

**Contract requirement when adding a new layer/feature:**
- layers must tie back to provenance (e.g., popups cite DCAT/STAC)
- comply with CARE (hide precise coordinates if sensitive) :contentReference[oaicite:39]{index=39}

---

### 5) Focus Mode AI output envelope 🤖✅

The AI pipeline is explicitly:
**UserQuestion → Retrieval → LLM Draft → Governance Check → AnswerWithCitations** :contentReference[oaicite:40]{index=40}

Focus Mode combines:
- semantic search linked to sources  
- Neo4j graph traversal (CIDOC-CRM, OWL-Time)  
- hybrid retrieval (RAG) for broad coverage :contentReference[oaicite:41]{index=41}

And KFM policy gates require citations; if sources can’t be provided, the assistant must refuse. :contentReference[oaicite:42]{index=42}

**Recommended `kfm.ai.answer.schema.json` fields (conceptual):**
- `question`
- `answer_markdown`
- `citations[]` (stable catalog IDs + locators)
- `retrieval_trace` (what indices queried, filters, timestamps)
- `policy_results` (pass/fail + reasons)
- `prov` link to PROV record for this answer

---

### 6) OCI artifacts + provenance attestations 📦🔏

KFM proposals treat large/binary artifacts as OCI objects:
- transfer via **oras**  
- sign with **cosign**  
- attach SBOM + provenance manifests (in-toto/SLSA style)  
- optionally attach PROV JSON-LD as a referrer :contentReference[oaicite:43]{index=43}:contentReference[oaicite:44]{index=44}

This supports FAIR interoperability + CARE controls (registries can restrict sensitive artifacts). :contentReference[oaicite:45]{index=45}

---

### 7) Forward-looking extensions: 4D + AR + “digital twin” 🛰️🕰️

Innovative concepts propose integrating:
- time-native 4D “digital twin” approaches (time as a core element)
- AR overlays and hybrid 2D/3D storytelling patterns :contentReference[oaicite:46]{index=46}

**Schema implication**: contracts should support optional:
- `rendering_hints` (2D/3D/AR)
- `time_states` / temporal resolution
- 3D assets references (e.g., tilesets/models) via artifact refs

---

## ✅ Validation (local + CI)

### Structural validation (JSON Schema)
Use **AJV** (Node) or **python-jsonschema** to validate examples against `profiles/*.schema.json`.

### Cross-file invariants (OPA/Rego)
KFM’s policy pack uses **OPA/Rego + Conftest** to enforce rules like:
- **Pipeline ordering** (no downstream artifacts without upstream boundary artifacts) :contentReference[oaicite:47]{index=47}
- **Provenance-first publishing** (processed changes require PROV updates) :contentReference[oaicite:48]{index=48}
- **API boundary** (UI can’t directly talk to Neo4j) :contentReference[oaicite:49]{index=49}

### CI behavior
CI is expected to **block merges if checks fail**, including schema checks, provenance completeness, broken links, and “missing citation” violations. :contentReference[oaicite:50]{index=50}:contentReference[oaicite:51]{index=51}

---

## 🔁 Versioning + compatibility

**Recommendation**: SemVer for schemas + artifacts.

- Patch: clarify docs, loosen constraints safely, add optional fields
- Minor: add new optional fields, new enum values, new extension blocks
- Major: breaking changes (rename/remove/required fields)

> KFM governance depends on stable, queryable metadata — breaking changes must ship with a migration note + dual-read strategy if needed. (Keep “fail-closed” principles: unclear data must not silently pass.) :contentReference[oaicite:52]{index=52}

---

## 🧩 Adding a new domain

KFM’s required staging + catalog outputs pattern:

1. **Ingest raw** → `data/raw/<domain>/…`  
2. **Transform** → `data/work/<domain>/…` → `data/processed/<domain>/…`  
3. **Publish boundary artifacts**:
   - STAC → `data/stac/…`
   - DCAT → `data/catalog/dcat/…`
   - PROV → `data/prov/…` :contentReference[oaicite:53]{index=53}
4. **Only then** update graph/API/UI/story layers (pipeline ordering) :contentReference[oaicite:54]{index=54}

KFM’s intake philosophy also requires:
- raw data is immutable evidence  
- deterministic config-driven ETL  
- provenance is mandatory from ingestion onward :contentReference[oaicite:55]{index=55}:contentReference[oaicite:56]{index=56}

---

## 🧰 Contribution checklist

### If you change schemas ✅
- [ ] Update `profiles/*.schema.json`
- [ ] Add/adjust `examples/` instances
- [ ] Add/adjust `tests/` (AJV + Conftest)
- [ ] If breaking: add `migrations/<version>/README.md`

### If you add data ✅
- [ ] Add the dataset contract JSON (source/license/space/time/steps)
- [ ] Publish STAC + DCAT + PROV boundary artifacts before graph/UI references :contentReference[oaicite:57]{index=57}
- [ ] Ensure license present + sensitivity classification complete :contentReference[oaicite:58]{index=58}

### If you add Story Nodes ✅
- [ ] Use the Story Node template conventions (citations + graph IDs) :contentReference[oaicite:59]{index=59}
- [ ] Add sidecar map-state config JSON :contentReference[oaicite:60]{index=60}
- [ ] Add evidence manifest + PROV link (preferred) :contentReference[oaicite:61]{index=61}

### If you touch AI ✅
- [ ] Ensure output is AnswerWithCitations (policy must refuse otherwise) :contentReference[oaicite:62]{index=62}:contentReference[oaicite:63]{index=63}

---

## 📚 Sources & project files

> The following project documents informed these contracts & gates:

### Core KFM specs
- :contentReference[oaicite:64]{index=64} 📚 KFM Data Intake – Technical & Design Guide (pipeline stages, OPA policy pack, fail-closed)
- :contentReference[oaicite:65]{index=65} Kansas Frontier Matrix – Comprehensive UI System Overview (schema/config-driven UI + provenance UX)
- :contentReference[oaicite:66]{index=66} Innovative Concepts to Evolve KFM (4D/AR extensions, future schema considerations)
- :contentReference[oaicite:67]{index=67} Additional Project Ideas / Pulse concepts (evidence manifests, OCI artifacts, policy-as-tests)

### Supporting architecture & AI docs
- Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation (contract-first, no mystery layers) :contentReference[oaicite:68]{index=68}
- Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖 (governance check → AnswerWithCitations, RAG + graph) :contentReference[oaicite:69]{index=69}:contentReference[oaicite:70]{index=70}
- Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design (policy gates list, fail-closed) :contentReference[oaicite:71]{index=71}

### Reference bundles (PDF portfolios) 📦
These are included in the repo as deeper background for implementation patterns:
- :contentReference[oaicite:72]{index=72} AI Concepts & more (AI/RAG/LLM references)
- :contentReference[oaicite:73]{index=73} Maps/GoogleMaps/VirtualWorlds/Geospatial/WebGL (rendering + GIS references)
- :contentReference[oaicite:74]{index=74} Data Management / Bayesian / CI/CD / Lakehouse bundles
- :contentReference[oaicite:75]{index=75} Various programming languages & resources (implementation language/tooling references)

---

## 🧠 Reminder: “policy is a test”
KFM treats policy checks like tests: a failing license check blocks a dataset addition just like a failing unit test blocks buggy code. :contentReference[oaicite:76]{index=76}


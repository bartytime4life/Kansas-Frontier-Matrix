# 🧾 `tools/attest` — Provenance & Integrity Attestations (KFM)

![Provenance-first](https://img.shields.io/badge/Provenance-first-2ea44f)
![Contract-first](https://img.shields.io/badge/Contract-first-0ea5e9)
![Reproducibility](https://img.shields.io/badge/Reproducibility-a855f7)
![Supply%20chain](https://img.shields.io/badge/Supply%20chain-attestation-f59e0b)
![Status](https://img.shields.io/badge/Status-WIP-yellow)

> [!IMPORTANT]
> **KFM Rule:** if an artifact can’t explain where it came from, it **doesn’t ship**.  
> `tools/attest` is how we make that rule enforceable ✅

---

## 🎯 What this tool is

`tools/attest` is the **attestation + provenance** toolkit for the Kansas Frontier Matrix (KFM).  
It produces **machine-verifiable** (and human-readable) proof that a dataset/layer/model/story output:

- ✅ matches a cryptographic hash (integrity)
- ✅ was produced by a known pipeline + version (reproducibility)
- ✅ cites its sources (provenance / audit trail)
- ✅ passed required validators (contract-first compliance)
- ✅ can be verified later (non-repudiation-ready workflows)

Think of it as: **“nutrition labels” + “tamper seals”** for every artifact in KFM.

---

## 🧭 Why `attest` exists (the KFM problem it solves)

KFM is **provenance-first** and **contract-first** across the full pipeline:

`ETL → Catalogs → Graph → API → UI → Story → Focus Mode AI`

At any stage, we need to answer:

- “**What is this layer?**”
- “**Who produced it, with what code + parameters?**”
- “**What sources does it rely on?**”
- “**Can I reproduce it?**”
- “**Has it been altered since publication?**”

`tools/attest` makes those answers **queryable and verifiable**, not “tribal knowledge” 🧠❌

---

## ⚡ Quickstart (expected UX)

> [!NOTE]
> Command names are **the target interface**. If the implementation differs today, align it toward this.

### 1) Generate an attestation (sidecar)
```bash
kfm-attest create \
  --artifact data/out/ks_counties_1850.geojson \
  --kind layer.vector \
  --pipeline etl/counties \
  --run-id "$(date -u +%Y%m%dT%H%M%SZ)" \
  --out data/out/ks_counties_1850.attest.json
```

### 2) Verify integrity + policy
```bash
kfm-attest verify \
  --artifact data/out/ks_counties_1850.geojson \
  --attestation data/out/ks_counties_1850.attest.json \
  --policy policies/attest/required_checks.yml \
  --strict
```

### 3) (Optional) Sign it
```bash
kfm-attest sign \
  --attestation data/out/ks_counties_1850.attest.json \
  --key keys/attest_private.pem \
  --out data/out/ks_counties_1850.attest.signed.json
```

### 4) Register it (Catalog / Graph)
```bash
kfm-attest register \
  --attestation data/out/ks_counties_1850.attest.signed.json \
  --catalog stac \
  --graph neo4j
```

---

## 🏗️ Where `attest` sits in the KFM architecture

```mermaid
flowchart LR
  A[ETL Jobs] --> B[Catalogs<br/>(STAC/DCAT)]
  B --> C[Knowledge Graph<br/>(Lineage + Semantics)]
  C --> D[API]
  D --> E[UI]
  E --> F[Story Engine]
  F --> G[Focus Mode AI]

  subgraph Attestation Gate ✅
    X[Create Attestation] --> Y[Validate Contract + Checks]
    Y --> Z[Sign + Timestamp (optional)]
  end

  A --> X
  B --> X
  C --> X
  Z --> B
  Z --> C
```

**Design intent:** `attest` is not “extra documentation.” It is a **hard gate** that prevents “mystery layers.”

---

## 🧩 What an attestation contains

### ✅ Minimum fields (v1)
Every attestation should include:

- **Artifact identity**
  - stable ID (UUID/ULID)
  - content hash (SHA-256)
  - size, media type
  - logical name / KFM slug
- **Production context**
  - pipeline name
  - run ID
  - git commit / repo
  - container image digest (if any)
  - parameters + environment fingerprint
- **Inputs (sources + dependencies)**
  - source artifacts (with their hashes)
  - citations (human-readable)
  - license + usage constraints
- **Quality checks**
  - schema validation
  - topology checks (geo)
  - statistical sanity checks (if model output)
- **Signature block (optional but preferred)**
  - key id
  - signature
  - timestamp / notary chain (optional)

### 📄 Example JSON (trimmed)
```json
{
  "schema": "kfm.attest/v1",
  "artifact": {
    "id": "ulid:01HQX2VY4M0Q6T7S0M0P4Y9Y8Z",
    "name": "ks_counties_1850.geojson",
    "kind": "layer.vector",
    "sha256": "b6a9...e2c1",
    "bytes": 2849931,
    "mediaType": "application/geo+json"
  },
  "producedBy": {
    "pipeline": "etl/counties",
    "runId": "2026-01-13T00:00:00Z",
    "git": { "repo": "kansas-frontier-matrix", "commit": "abc1234" },
    "env": { "python": "3.12.0", "os": "linux", "arch": "x86_64" },
    "params": { "year": 1850, "simplify": 0.0 }
  },
  "inputs": [
    { "ref": "scan:county_map_1850", "sha256": "91f2...a8c0" },
    { "ref": "gazetteer:usgs_names", "sha256": "00aa...bb11" }
  ],
  "checks": [
    { "name": "contract.schema", "result": "pass" },
    { "name": "geo.topology", "result": "pass" }
  ],
  "citations": [
    { "label": "Source Map (1850 County Survey)", "uri": "kfm://sources/maps/1850_county_survey" }
  ],
  "signature": null
}
```

---

## 🧠 Core principles (non-negotiable)

### 1) Provenance-first 🧾
Attestation must make it easy to trace back:
- source documents
- transformations
- assumptions
- validation evidence

### 2) Contract-first 📜
Artifacts must pass a **data contract** before they are admitted to catalogs/graph.

> [!TIP]
> Treat contracts like API schemas: breaking changes require version bumps.

### 3) Deterministic + idempotent pipelines 🔁
If the same inputs + same pipeline version run twice, it should produce:
- the same output hash **or**
- an explicit reason in the attestation (nondeterminism recorded: seeds, stochastic runs, UQ, etc.)

### 4) Stable identifiers 🆔
Use **unique, meaningless IDs** for entities/artifacts, then attach meaning as attributes.  
This keeps the lineage graph stable even when labels/titles change.

### 5) Policies are data (regulation tables) ⚙️
What’s required to publish an artifact shouldn’t be hidden inside code.
- required checks
- allowed licenses
- required citation fields
- redaction rules (privacy)

Put them in `policies/attest/*` and make `verify` enforce them.

---

## 🔐 Integrity, signing, and non‑repudiation

Attestation can be used at multiple assurance levels:

| Level | Name | What you get | When to use |
|---:|---|---|---|
| 0 | Hash-only | Detects corruption | local dev, scratch outputs |
| 1 | Hash + checks | Integrity + baseline quality | ETL outputs, drafts |
| 2 | Signed | Integrity + author accountability | anything published |
| 3 | Signed + timestamp/notary | Non-repudiation & long-term audit | public releases, legal/regulatory contexts |
| 4 | Reproducible build proof | Rebuild → same hash | “gold” datasets / flagship releases |

> [!WARNING]
> Signatures are only as strong as **key handling**. Don’t store private keys in repo. Ever.

---

## 🗃️ Storage + querying (attestation registry)

`attest` supports **two storage modes**:

1) **Sidecar-only**
- `.attest.json` sits next to artifact
- good for portability / offline validation

2) **Registry-backed**
- attestations are ingested into a registry DB (Postgres recommended)
- enables fast queries:
  - “show lineage for layer X”
  - “find all artifacts derived from source Y”
  - “list all artifacts produced by pipeline version Z”

### Suggested registry tables (minimal)
- `attestations(id, artifact_id, sha256, kind, produced_at, jsonb)`
- `artifacts(id, name, sha256, media_type, bytes)`
- `edges(src_id, rel, dst_id)` (lineage graph edges)
- `signatures(attestation_id, key_id, alg, sig, ts)`

> [!TIP]
> Keep the registry **append-only** where possible (auditability + easier replication).

---

## 🧪 Testing strategy

### Unit tests
- hash calculation is stable
- schema validation catches missing fields
- policy enforcement fails correctly

### Golden fixtures
- a directory of tiny artifacts + known attestations
- every format we support: GeoJSON, GeoTIFF, PNG/JPEG, glTF, JSON, CSV

### Property tests (recommended)
- random artifacts → attest → verify roundtrip
- registry ingest → query lineage invariants

---

## 🔌 Integrations

### ETL
- `create` + `verify` should run at the end of every ETL job
- failure should block promotion to catalog

### STAC/DCAT
- attestation metadata should be linkable from catalog entries
- store `sha256` + `attestation_uri` in catalog properties

### Knowledge Graph
- ingest attestation into lineage graph:
  - `Artifact --derivedFrom--> Artifact`
  - `Artifact --producedBy--> Run`
  - `Run --used--> PipelineVersion`
  - `Artifact --cites--> Source`

### UI / Story Engine
- provenance card:
  - “Sources”
  - “Created by”
  - “Checks passed”
  - “Download attestation”
- this is part of “trust UX” (don’t hide it)

---

## 📁 Suggested folder layout

```text
🧰 tools/
  🧾 attest/
    README.md
    📦 src/
      attest/
        __init__.py
        cli.py
        hash.py
        schema/
          attest.v1.schema.json
        policy/
          evaluator.py
        registry/
          postgres.py
        sign/
          signer.py
          verifier.py
    🧪 tests/
    🧷 examples/
    🔒 policies/
      attest/
        required_checks.yml
        allowed_licenses.yml
```

---

## 📚 Project Library Index (used by this tool)

This project ships with a **deliberately wide reference shelf**. `attest` draws on them like this:

### 🔬 Reproducibility, scientific rigor, and experiment traceability
- `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf` — reproducibility, V&V, uncertainty reporting, governance 🛰️
- `Understanding Statistics & Experimental Design.pdf` — replication, statistical assumptions, power, documentation discipline 📈
- `Scientific Method _ Research _ Master Coder Protocol Documentation.pdf` — lab‑notebook style traceability for investigations 🧪
- `graphical-data-analysis-with-r.pdf` — EDA workflows & reporting consistency 📊
- `regression-analysis-with-python.pdf` + `Regression analysis using Python - slides-linear-regression.pdf` — model artifacts + evaluation metadata 🧮
- `think-bayes-bayesian-statistics-in-python.pdf` — capturing priors, posteriors, and sampling settings for reproducible inference 🎲
- `Understanding Machine Learning.pdf` — ML lifecycle considerations & evaluation framing 🤖
- `Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf` — deep learning experiment hygiene (library reference) 🧠

### 🗺️ Geospatial provenance (KFM’s core domain)
- `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf` — end‑to‑end KFM system constraints + provenance requirements 🧭
- `Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf` — blueprint + system intent 🧱
- `MARKDOWN_GUIDE_v13.md.gdoc` — repo invariants, subsystem boundaries, “no drift” rules 🧷
- `python-geospatial-analysis-cookbook.pdf` — geospatial processing patterns + formats 🧰
- `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf` — remote sensing derivations + metadata expectations 🛰️
- `making-maps-a-visual-guide-to-map-design-for-gis.pdf` — cartographic design + making provenance visible in maps 🎨
- `Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf` — mobile mapping ethics + context sensitivity 📱
- `Archaeological 3D GIS_26_01_12_17_53_09.pdf` — 3D GIS assets and documentation needs 🏺
- `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf` — 3D visualization artifacts + rendering pipelines 🧊
- `compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf` — imagery formats, compression, and metadata pitfalls 🖼️

### 🗄️ Data management, scale, and future-proofing
- `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf` — JSONB, indexing, operational basics 🐘
- `Database Performance at Scale.pdf` — workload-aware design, performance tradeoffs, operational scaling 🚀
- `Scalable Data Management for Future Hardware.pdf` — data system scaling patterns & future architectures 🧬
- `Data Spaces.pdf` — trust, governance, interoperability in distributed data sharing 🤝

### 🔐 Security, governance, and human-centered accountability
- `Introduction to Digital Humanism.pdf` — accountability, privacy/security principles, governance & certification 🧑‍⚖️
- `On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf` — prediction/explanation framing + governance implications ⚖️
- `ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf` — defensive security mindset for key handling 🛡️
- `Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf` — security awareness reference (defensive use only) 🧯

### 🧱 Engineering references (implementation support)
- `concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf` — distributed + concurrency patterns ⚙️
- `Spectral Geometry of Graphs.pdf` — graph thinking for lineage/relationships 🕸️
- `Generalized Topology Optimization for Structural Design.pdf` — simulation/optimization artifacts (future use-case) 🏗️
- `Principles of Biological Autonomy - book_9780262381833.pdf` — complex systems modeling (future use-case) 🧬
- `A programming Books.pdf`, `B-C programming Books.pdf`, `D-E programming Books.pdf`, `F-H programming Books.pdf`, `I-L programming Books.pdf`, `M-N programming Books.pdf`, `O-R programming Books.pdf`, `S-T programming Books.pdf`, `U-X programming Books.pdf` — language/tooling reference shelf 📚

---

## 🗺️ Roadmap

- [ ] v1 JSON Schema finalized (`attest.v1.schema.json`)
- [ ] policy engine (`required_checks.yml`, `allowed_licenses.yml`)
- [ ] registry ingestion (Postgres)
- [ ] graph export (Neo4j / property graph)
- [ ] signature support (pluggable signer)
- [ ] UI provenance card component
- [ ] test fixtures pack (geo + imagery + 3D)

---

## ✅ Definition of Done (for this tool)

An artifact is “publishable” when:

- ✅ attestation exists
- ✅ `verify --strict` passes
- ✅ citations are present and valid
- ✅ contract schema passes
- ✅ integrity verified (hash matches)
- ✅ attestation is registered to Catalog + Graph (for published artifacts)
- ✅ (preferred) attestation is signed + timestamped for releases

---

## 🧩 Maintainers’ checklist

- [ ] Are we preventing “mystery layers”?
- [ ] Can a contributor reproduce the artifact from attestation alone?
- [ ] Does the UI show provenance without digging?
- [ ] Are policies versioned and reviewable?
- [ ] Are keys handled safely?

---

<!--
Internal workspace file citations (for the Kansas-Matrix-System knowledge base).
These are kept in HTML comments so they don’t clutter the README rendering.

Core KFM + repo rules:
-  [oai_citation:0‡Database Performance at Scale.pdf](file-service://file-36z8qyiVJRtrSs6QG7Epen)  (KFM Comprehensive Technical Documentation)
-  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  (Archaeological 3D GIS)
-  [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)   (Kansas-Frontier-Matrix Open-Source Hub Design)
-  [oai_citation:3‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  (MARKDOWN_GUIDE_v13)

Design + architecture:
-  [oai_citation:4‡F-H programming Books.pdf](file-service://file-QofzooQDG9grJwh9nFN9SY)  (Flexible Software Design)
-  [oai_citation:5‡F-H programming Books.pdf](file-service://file-QofzooQDG9grJwh9nFN9SY)   (F-H programming Books — includes crypto + design refs)

Data + performance:
-  [oai_citation:6‡U-X programming Books.pdf](file-service://file-3hYtSGHtHmb6wyTtavym6M)  (Database Performance at Scale)
-  [oai_citation:7‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)   (Scalable Data Management for Future Hardware)

Security + tooling references:
-  [oai_citation:8‡B-C programming Books.pdf](file-service://file-7V9zHZSJakZZrJAw9ASCMJ)  (Bash Notes / tooling)
-  [oai_citation:9‡M-N programming Books.pdf](file-service://file-EYCp5md89QY2cy5PCYS18e)  (MATLAB Notes)
-  [oai_citation:10‡I-L programming Books.pdf](file-service://file-T9sYu87k1GPNNKMLddx41a)  (Implementing Programming Languages)
-  [oai_citation:11‡O-R programming Books.pdf](file-service://file-M6zCNBGmJbot7A2aaUUy9M)  (Objective-C Notes)
-->

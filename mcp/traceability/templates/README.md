# Traceability Templates 🧾🔗  
**MCP (Master Coder Protocol) × KFM (Kansas Frontier Matrix)** — *evidence-first, provenance-first templates for data, graphs, stories, and AI.*

![MCP](https://img.shields.io/badge/MCP-Master%20Coder%20Protocol-blue)
![KFM](https://img.shields.io/badge/KFM-Kansas%20Frontier%20Matrix-7b2cbf)
![Provenance](https://img.shields.io/badge/Provenance-First-brightgreen)
![Standards](https://img.shields.io/badge/Standards-STAC%20%7C%20DCAT%20%7C%20PROV-orange)
![Governance](https://img.shields.io/badge/Governance-FAIR%20%2B%20CARE-success)
![Policy-as-Code](https://img.shields.io/badge/Policy-as--Code-OPA%20%2B%20Conftest-informational)
![Supply%20Chain](https://img.shields.io/badge/Supply%20Chain-SBOM%20%2B%20SLSA%20%2B%20Sigstore-yellow)

> [!IMPORTANT]  
> **KFM invariant:** *Anything that shows up in the UI or Focus Mode must be traceable back to cataloged sources and provable processing.*  
> No “mystery layers.” No unsourced narratives. No unlogged transformations.

---

## 🎯 What lives in this folder

This folder contains **copy/paste scaffolds** for the traceability artifacts KFM expects across the full pipeline:


flowchart LR
  A[🔧 ETL Pipelines] --> B[📦 Catalogs: STAC + DCAT + PROV]
  B --> C[🕸️ Graph: Neo4j]
  C --> D[🔌 API Boundary: governed access]
  D --> E[🗺️ UI: map + timeline + layers]
  E --> F[📖 Story Nodes: evidence manifest]
  F --> G[🧠 Focus Mode: citations ledger]


### ✅ Templates are for:
- 📦 **Datasets & derived artifacts** (including AI outputs and simulations)
- 🧬 **Lineage & provenance** (inputs → activities → outputs; agents & tools)
- 🧾 **Run logging** (manifests, telemetry, hashes, idempotency keys)
- 🗺️ **UI transparency** (layer provenance panels, export attributions, “View Evidence”)
- 📚 **Story Nodes** (evidence manifests + PROV links, research-paper discipline)
- 🤖 **AI (Focus Mode)** (citations required, governance ledger entries, bias/drift reports)
- 🛡️ **Governance & policy gates** (OPA/Conftest checks; fail-closed)
- 🔐 **Supply chain attestation** (SBOM, SLSA/in-toto provenance, cosign signing)
- 🧩 **Design Packs & domain specs** (SampleUnitSpec / PreprocessSpec / MetricSpec)
- 🧭 **Future/advanced** (digital twins, AR overlays, crowdsourced verification)

---

## 🚦 Non‑negotiable invariants (MCP + KFM)

These templates encode KFM’s “rules of the road”:

- 🧱 **Pipeline ordering is absolute**: ETL → Catalogs → Graph → API → UI → Story Nodes → Focus Mode  
- 🔒 **API boundary rule**: UI never queries graph directly; governed API is the only access path.
- 🧾 **Provenance-first publishing**: nothing enters graph/UI/story/AI without metadata + lineage.
- ♻️ **Deterministic, idempotent ETL**: same inputs/config → same outputs; reruns safe.
- 🧠 **Evidence-first narrative**: every claim must cite evidence; AI text must be identified + sourced.
- 🧰 **Policy gates fail closed**: missing license / missing provenance / missing sensitivity label → no merge.
- 🤖 **Agents are auditable**: Watcher/Planner/Executor must log actions; no auto-merge; kill-switch exists.
- 🔐 **Supply chain hygiene**: SBOM + signed artifacts; no secrets in repo; threat model + secrets policy.

---

## 🗂️ Where these templates “land” in the repo

This folder is **templates only**. The generated artifacts typically live elsewhere:

- 📁 `data/stac/` → STAC Collections + Items  
- 📁 `data/catalog/dcat/` → DCAT JSON-LD dataset records  
- 📁 `data/prov/` → PROV JSON-LD bundles (runs, datasets, stories, AI)  
- 📁 `data/audits/<run_id>/` → run manifests, telemetry, checksum files  
- 📁 `docs/reports/story_nodes/` → story markdown + evidence manifests  
- 📁 `mcp/` → methods & computational experiments (runs, notebooks, model cards)

> [!TIP]  
> **Think “boundary artifacts.”** Catalog + lineage files are the formal interface between subsystems.

---

## ⚡ Quickstart (copy → fill → validate → link)

1. 🧩 Pick the right template below  
2. 📝 Copy it into the correct output location (or into your PR as a new artifact)  
3. 🔁 Replace `TODO_*` placeholders  
4. ✅ Validate (schema + policy gates)  
5. 🔗 Link it:
   - STAC ↔ DCAT ↔ PROV
   - Graph nodes point to **IDs**, not raw blobs
   - UI panels point to **catalog + lineage**
6. 📌 Commit with meaningful message (agents include structured references)

---

## 🧭 Template index

- 🧱 **Core Evidence Triplet** (STAC / DCAT / PROV)
- 🧾 **Run Manifests & Telemetry** (determinism + auditability)
- 📚 **Story Nodes** (evidence manifests + narrative provenance)
- 🤖 **Focus Mode (AI)** (citations + governance ledger)
- 🛡️ **Policy & Governance** (OPA/Conftest + FAIR/CARE + sensitivity)
- 🔐 **Supply Chain** (SBOM + SLSA/in-toto + Cosign)
- 🕸️ **Graph Health** (constraints + audits)
- 🧩 **Design Packs & Specs** (domain-level traceability)
- 🧪 **Advanced / Future** (simulations, AR, crowdsourced verification, offline packs)
- 📦 **Reference Libraries** (PDF portfolios included in this project)

---

# 🧱 Core Evidence Triplet Templates (STAC / DCAT / PROV)

KFM uses the “triplet” so **humans, machines, and the UI** can all verify provenance.

## 1) STAC Item / Collection 🛰️

**Use for:** spatial assets (COG, GeoParquet, PMTiles, 3D tiles, vector layers, etc.)

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "TODO_STAC_ITEM_ID",
  "collection": "TODO_COLLECTION_ID",
  "geometry": null,
  "bbox": null,
  "properties": {
    "datetime": "TODO_ISO8601_DATETIME_OR_NULL",
    "kfm:profile": { "name": "KFM-STAC", "version": "TODO_PROFILE_VERSION" },
    "kfm:classification": "public|restricted|sensitive",
    "kfm:sensitivity": {
      "contains_sensitive_sites": false,
      "care": ["CollectiveBenefit", "Responsibility"],
      "tk_labels": []
    }
  },
  "assets": {
    "data": {
      "href": "TODO_URL_OR_OCI_REFERENCE",
      "type": "TODO_MEDIA_TYPE",
      "roles": ["data"],
      "title": "Primary dataset asset",
      "extra_fields": {
        "kfm:digest": "sha256:TODO",
        "kfm:distribution": {
          "oci": {
            "registry": "ghcr.io",
            "repo": "TODO_ORG/TODO_NAME",
            "tag": "TODO_TAG",
            "digest": "sha256:TODO",
            "media_type": "TODO_MEDIA_TYPE",
            "referrers": {
              "prov": "TODO_PROV_REF",
              "sbom": "TODO_SBOM_REF",
              "cosign": "TODO_COSIGN_REF"
            }
          }
        }
      }
    }
  },
  "links": [
    { "rel": "self", "href": "TODO_SELF_HREF" },
    { "rel": "root", "href": "TODO_ROOT_HREF" },
    { "rel": "parent", "href": "TODO_COLLECTION_HREF" },
    { "rel": "via", "href": "TODO_PROV_BUNDLE_HREF", "title": "PROV lineage" }
  ]
}
```

## 2) DCAT Dataset (JSON‑LD) 📇

**Use for:** dataset-level catalog entries (licenses, publishers, distributions, themes)

```json
{
  "@context": [
    "https://www.w3.org/ns/dcat2.jsonld",
    { "kfm": "https://example.org/kfm#" }
  ],
  "@id": "TODO_DCAT_DATASET_URI",
  "@type": "dcat:Dataset",
  "dct:title": "TODO_TITLE",
  "dct:description": "TODO_DESCRIPTION",
  "dct:license": "TODO_SPDX_LICENSE_ID",
  "dct:publisher": { "@id": "TODO_PUBLISHER_URI" },
  "dcat:theme": ["TODO_THEME"],
  "dcat:distribution": [
    {
      "@type": "dcat:Distribution",
      "dct:title": "Primary distribution",
      "dcat:mediaType": "TODO_MEDIA_TYPE",
      "dcat:downloadURL": "TODO_URL_OR_OCI_REFERENCE",
      "kfm:digest": "sha256:TODO"
    }
  ],
  "kfm:profile": { "name": "KFM-DCAT", "version": "TODO_PROFILE_VERSION" },
  "kfm:provenance": { "prov_bundle": "TODO_PROV_BUNDLE_HREF" }
}
```

## 3) PROV Bundle (JSON‑LD) 🧬

**Use for:** lineage across ingestion, transformations, model runs, story authoring, AI answers.

```json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "dct": "http://purl.org/dc/terms/",
    "kfm": "https://example.org/kfm#"
  },
  "@graph": [
    {
      "@id": "kfm:activity/TODO_RUN_ID",
      "@type": "prov:Activity",
      "prov:startedAtTime": "TODO_ISO8601",
      "prov:endedAtTime": "TODO_ISO8601",
      "prov:used": [
        { "@id": "kfm:entity/TODO_INPUT_DATASET_ID" }
      ],
      "prov:wasAssociatedWith": { "@id": "kfm:agent/TODO_AGENT_ID" },
      "kfm:params_ref": "TODO_CONFIG_OR_MANIFEST_PATH",
      "kfm:canonical_digest": "sha256:TODO_RFC8785_CANONICAL_HASH"
    },
    {
      "@id": "kfm:entity/TODO_OUTPUT_DATASET_ID",
      "@type": "prov:Entity",
      "prov:wasGeneratedBy": { "@id": "kfm:activity/TODO_RUN_ID" },
      "dct:license": "TODO_SPDX_LICENSE_ID",
      "kfm:digest": "sha256:TODO"
    },
    {
      "@id": "kfm:agent/TODO_AGENT_ID",
      "@type": "prov:Agent",
      "prov:type": "human|service|ci|wpe-agent",
      "kfm:actor": "TODO_NAME_OR_BOT_ID"
    }
  ]
}
```

---

# 🧾 Run Manifest & Telemetry Templates (Determinism + Auditability)

## Run Manifest (`run_manifest.json`) 🪪

**Why:** gives every pipeline run a **self-contained “receipt”** and supports idempotency.

> [!NOTE]  
> Recommended: canonicalize manifest JSON (RFC 8785) → compute SHA‑256 → store as `canonical_digest` + optional `idempotency_key`.

```json
{
  "schema": "kfm.run_manifest@v1",
  "run_id": "RUN-YYYYMMDDThhmmssZ-TODO",
  "canonical_digest": "sha256:TODO",
  "idempotency_key": "sha256:TODO",
  "created_at": "TODO_ISO8601",
  "pipeline": {
    "name": "TODO_PIPELINE_NAME",
    "version": "TODO_SEMVER",
    "git": { "commit": "TODO_SHA", "repo": "TODO_URL_OR_PATH" }
  },
  "inputs": [
    {
      "id": "TODO_INPUT_ID",
      "uri": "TODO_SOURCE_URL_OR_PATH",
      "etag": "TODO_IF_AVAILABLE",
      "digest": "sha256:TODO"
    }
  ],
  "outputs": [
    {
      "id": "TODO_OUTPUT_ID",
      "path": "data/processed/TODO",
      "digest": "sha256:TODO",
      "stac_item": "data/stac/items/TODO.json",
      "dcat": "data/catalog/dcat/TODO.jsonld",
      "prov": "data/prov/TODO.jsonld"
    }
  ],
  "tool_versions": {
    "python": "TODO",
    "gdal": "TODO",
    "tippecanoe": "TODO",
    "node": "TODO"
  },
  "telemetry": {
    "events_file": "telemetry.ndjson",
    "metrics": {
      "records_in": 0,
      "records_out": 0,
      "warnings": 0,
      "errors": 0
    }
  },
  "governance": {
    "license_verified": true,
    "sensitivity_labeled": true,
    "policy_gate_report": "TODO_PATH"
  }
}
```

## Checksums (`checksums.sha256`) 🧮

```txt
# sha256  path
TODO_SHA256  data/processed/TODO/file1.ext
TODO_SHA256  data/processed/TODO/file2.ext
```

## Telemetry (`telemetry.ndjson`) 📈

Each line is a JSON event. Keep it append-only.

```json
{"ts":"TODO_ISO8601","run_id":"RUN-...","stage":"download","event":"start","details":{}}
{"ts":"TODO_ISO8601","run_id":"RUN-...","stage":"transform","event":"stats","details":{"records_in":123,"records_out":120}}
{"ts":"TODO_ISO8601","run_id":"RUN-...","stage":"publish","event":"complete","details":{"stac":"...","prov":"..."}}
```

---

# 📚 Story Node Traceability Templates (Evidence-first narrative)

Story Nodes in KFM are **not just Markdown** — they’re **queryable, auditable, and linked to evidence**.

## Story Node Markdown (`story_node.md`) 📝

```md
---
id: "SN-TODO"
title: "TODO_TITLE"
status: "draft|published"
timeframe: "TODO_RANGE"
regions: ["TODO"]
tags: ["history", "ecology", "treaties"]
evidence_manifest: "EM-TODO.yaml"
prov_bundle: "data/prov/story/SN-TODO.jsonld"
stac_refs:
  - "data/stac/items/TODO.json"
dcat_refs:
  - "data/catalog/dcat/TODO.jsonld"
ai_assisted: false
---

## Summary
TODO

## Narrative
Write claims like a research paper — add footnotes or bracketed citations (e.g., [E1], [E2]) and ensure
every citation is backed by the Evidence Manifest.

## Evidence
- [E1] TODO
- [E2] TODO
```

## Evidence Manifest (`EM-*.yaml`) 🧾

```yaml
schema: kfm.evidence_manifest@v1
story_id: SN-TODO
items:
  - id: E1
    kind: dataset|document|map|image|oral_history|simulation|ai_artifact
    title: "TODO"
    uri: "TODO_URL_OR_REPO_PATH"
    digest: "sha256:TODO_IF_AVAILABLE"
    how_used: "TODO_SHORT_METHOD_NOTE"
    derived_query: "TODO_QUERY_IF_APPLICABLE"
    sensitivity:
      classification: public|restricted|sensitive
      care: ["CollectiveBenefit", "AuthorityToControl", "Responsibility", "Ethics"]
      tk_labels: []
  - id: E2
    kind: dataset
    title: "Cataloged dataset"
    stac_item: "data/stac/items/TODO.json"
    dcat: "data/catalog/dcat/TODO.jsonld"
    prov: "data/prov/TODO.jsonld"
```

> [!TIP]  
> CI can validate: **every in-text citation ↔ evidence manifest item exists**, and every dataset citation resolves to STAC/DCAT/PROV.

---

# 🤖 Focus Mode (AI) Traceability Templates

Focus Mode is governed: **no citations → refuse answer**.  
Every AI action should be attributable, policy-checked, and ledgered.

## AI Answer Record (`focus_answer.json`) 🧠

```json
{
  "schema": "kfm.focus_answer@v1",
  "request_id": "REQ-TODO",
  "ts": "TODO_ISO8601",
  "question": "TODO",
  "answer": "TODO",
  "citations": [
    { "id": "E1", "stac_item": "data/stac/items/TODO.json", "quote": "TODO_OPTIONAL_SNIPPET" }
  ],
  "context_snapshot": {
    "map": { "bbox": null, "layers": ["TODO"], "time": "TODO_RANGE" }
  },
  "model": { "name": "TODO_MODEL", "version": "TODO", "provider": "TODO" },
  "uncertainty": { "confidence": "low|medium|high", "notes": "TODO" },
  "provenance": { "prov_bundle": "data/prov/ai/REQ-TODO.jsonld" },
  "policy": { "gate": "pass|fail", "report": "TODO_PATH" }
}
```

## Governance Ledger Entry (`governance_ledger.ndjson`) 🧾🔒

Append-only NDJSON:

```json
{"ts":"TODO_ISO8601","event":"focus_mode_answer","request_id":"REQ-TODO","actor":"kfm-agent|human","policy_gate":"pass","citations_count":3,"sensitivity":"public","energy_estimate_wh":null}
```

## Bias / Drift / QA Reports (placeholders) 📊

Keep these lightweight but consistent:

- `bias_report.json`
- `drift_report.json`
- `xai_audit.json` (explanations + which evidence/weights influenced the output)

---

# 🛡️ Policy & Governance Templates (OPA / Conftest)

Policy gates encode governance (FAIR/CARE, security, provenance requirements) as code.

## Governance Card (`governance_card.json`) ⚖️

```json
{
  "schema": "kfm.governance_card@v1",
  "allowed_licenses": ["CC-BY-4.0", "CC0-1.0", "ODC-By-1.0", "MIT"],
  "required_dataset_fields": ["license", "publisher", "provenance_ref", "sensitivity"],
  "sensitivity_levels": ["public", "restricted", "sensitive"],
  "care_required": true,
  "tk_labels_supported": true
}
```

## OPA Rego Skeleton (`policy_gate.rego`) 🚧

```rego
package kfm.gates

deny[msg] {
  input.kind == "dataset"
  not input.license
  msg := "Missing license"
}

deny[msg] {
  input.kind == "story_node"
  count(input.evidence.items) == 0
  msg := "Story node must include evidence items"
}

deny[msg] {
  input.kind == "focus_answer"
  count(input.citations) == 0
  msg := "Focus Mode answer must include citations (fail closed)"
}
```

---

# 🔐 Supply Chain Templates (SBOM / SLSA / Cosign)

KFM treats **data like code**: versioned, reviewable, and verifiable.

- 📄 `sbom.spdx.json` — SBOM per release / per pipeline container
- 📄 `slsa_provenance.intoto.json` — in-toto / SLSA attestation for CI builds
- 📄 `cosign.bundle.json` — signature bundle reference (keyless/OIDC when available)

> [!NOTE]  
> When artifacts are stored in an OCI registry (ORAS), signatures + SBOM + PROV can be attached as **OCI referrers**.

---

# 🕸️ Graph Health Check Templates

These templates help keep the graph honest and prevent “floating facts.”

## Graph Health Report (`graph_health_report.md`) 🧪

- Orphan detection (nodes without provenance)
- Constraint checks (relationship rules)
- Cardinality checks (e.g., every Dataset must map to at least 1 STAC Item)

## Cypher Snippets (`graph_health_checks.cypher`) 🕵️

```cypher
// Orphaned datasets: no provenance ref
MATCH (d:Dataset)
WHERE d.prov_bundle IS NULL
RETURN d LIMIT 50;

// Provenance activity missing inputs or outputs
MATCH (a:ProvActivity)
WHERE NOT (a)-[:USED]->() OR NOT (a)<-[:WAS_GENERATED_BY]-()
RETURN a LIMIT 50;
```

---

# 🧩 Design Packs & Domain Specs Templates

Design Packs make new domains **reviewable and traceable** (and prevent ad-hoc drift).

## Design Pack (`design_pack.md`) 📦

- Scope & definitions  
- Data contracts + schemas  
- Ontology mappings (CIDOC‑CRM / GeoSPARQL / OWL‑Time)  
- Pipeline specs + expected outputs  
- Quality gates + evaluation metrics  
- Integration points: Graph ↔ API ↔ UI ↔ Story Nodes ↔ Focus Mode  

## Domain Spec Files (structured) 🧾

- `SampleUnitSpec.yaml` (what counts as a unit of observation)
- `PreprocessSpec.yaml` (how raw becomes analysis-ready)
- `MetricSpec.yaml` (how performance/quality is measured)

These IDs can be referenced in PROV so people know **exactly** which rules generated results.

---

# 🧪 Advanced / Future Templates (Digital Twins, AR, Crowd Verification)

These reflect KFM’s roadmap direction: simulations, AR storytelling, crowdsourced verification, and offline-first field use.

## Simulation Run Manifest (`sim_run_manifest.json`) 🌎⏱️

Capture: model version, seed, parameters, input datasets (STAC/DCAT/PROV), outputs, uncertainty.

## AR Scene Manifest (`ar_scene_manifest.json`) 🥽

Capture: anchors, coordinate system, assets (glTF/3D tiles), alignment methods, and provenance.

## Crowd Verification Record (`crowd_verification.yaml`) 🧑‍🤝‍🧑✅

Capture: tasks, worker contributions, consensus rules, quality control, and provenance.

## Offline Pack Manifest (`offline_pack_manifest.json`) 🧳📴

Capture: included datasets + digests + licenses + size budget + sensitivity restrictions.

---

# 🔧 Validation checklist (what CI should enforce)

Use this list as a **PR gate** mindset:

- [ ] Schema validation passes (JSON Schema / SHACL where relevant)
- [ ] STAC/DCAT/PROV alignment present for each publishable dataset
- [ ] License present and allowed (SPDX)
- [ ] Sensitivity classification included (and handling rules satisfied)
- [ ] Checksums exist for published artifacts
- [ ] Run manifest includes inputs/outputs and tool versions
- [ ] No secrets / tokens committed
- [ ] Story Nodes: citations ↔ evidence manifest consistency
- [ ] Focus Mode: citations required, governance ledger appended, policy gate report attached

---

# 📦 Reference Libraries included in this project (PDF portfolios)

Several project files are **PDF Portfolios** (collections of embedded books/papers).  
To list embedded documents locally:

```bash
pdfdetach -list "<portfolio>.pdf"
```

To extract an embedded file (by number):

```bash
pdfdetach -save 12 -o extracted.pdf "<portfolio>.pdf"
```

## AI Concepts & more.pdf 📚🤖

<details>
<summary><strong>Embedded files (36)</strong></summary>

1. A Developer’s Guide to Building AI Applications - English.pdf  
2. A Gentle Introduction to Symbolic Computation.pdf  
3. AI Foundations of Computational Agents 3rd Ed.pdf  
4. Artificial Intelligence & Machine Learning in Health Care & Medical Sciences.pdf  
5. Artificial Neural Networks Models & Applications.pdf  
6. Artificial-neural-networks-an-introduction.pdf  
7. Basics of Linear Algebra for machine Learning (Discover The Mathematical LLanguage of Data in Python) - Jason Brownlee.pdf  
8. Data Science &-  Machine Learning (Mathematical & Statistical Methods).pdf  
9. Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf.pdf  
10. Deep Learning with Python.pdf  
11. Foundations of Machine Learning - Foundations_of_Machine_Learning.pdf  
12. Gradient Expectations - Stucture, Origins, & Synthesis Of Predictive Neural Networks.pdf  
13. Introduction to Digital Humanism.pdf  
14. Introduction to Machine Learning with Python - Introduction to Machine Learning with Python.pdf  
15. Neural Network Architectures and Activation Functions_ A Gaussian Process Approach - 106621.pdf  
16. Neural Network Toolbox User_s Guide - nnet.pdf  
17. Neural Networks Using C# Succinctly - Neural_Networks_Using_C_Sharp_Succinctly.pdf  
18. On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf  
19. Pattern Recognition and Machine Learning.pdf  
20. Principles of Biological Autonomy - book_9780262381833.pdf  
21. Recurrent Neural Networks for Temporal Data Processing.pdf  
22. Regression analysis using Python - slides-linear-regression.pdf  
23. Volume 1 Machine Learning under Resource Constraints - Fundamentals .pdf  
24. Volume 2 Machine Learning under Resource Constraints - Discovery in Physics .pdf  
25. Volume 3 Machine Learning under Resource Constraints - Applications.pdf  
26. artificial-intelligence-a-modern-approach.pdf  
27. artificial-neural-networks-in-real-life-applications.pdf  
28. deep-learning-in-python-prerequisites.pdf  
29. haykin.neural-networks.3ed.2009.pdf  
30. java-artificial-intelligence-made-easy-w-java-programming.pdf  
31. neural networks and deep learning.pdf  
32. neural-network-design.pdf  
33. neural-network-learning-theoretical-foundations.pdf  
34. python-machine-learning-a-crash-course-for-beginners-to-understand-machine-learning-artificial-intelligence-neural-networks-and-deep-learning-with-scikit-learn-tensorflow-and-keras.pdf  
35. regression-analysis-with-python.pdf  
36. understanding-machine-learning-theory-algorithms.pdf  

</details>

## Maps / Google Maps / Virtual Worlds / Archaeology / WebGL 🗺️🕹️

<details>
<summary><strong>Embedded files (14)</strong></summary>

1. Archaeological 3D GIS_26_01_12_17_53_09.pdf  
2. Computer Graphics using JAVA 2D & 3D.pdf  
3. DesigningVirtualWorlds.pdf  
4. Geographic Information System Basics - geographic-information-system-basics.pdf  
5. Google Earth Engine Applications.pdf  
6. Map Reading & Land Navigation.pdf  
7. Spectral Geometry of Graphs.pdf  
8. Understanding_Map_Projections.pdf - 710understanding_map_projections.pdf  
9. geoprocessing-with-python.pdf  
10. google-maps-javascript-api-cookbook.pdf  
11. graphical-data-analysis-with-r.pdf  
12. making-maps-a-visual-guide-to-map-design-for-gis.pdf  
13. python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf  
14. webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf  

</details>

## Data Management / Architectures / Bayesian Methods 🧠🗃️

<details>
<summary><strong>Embedded files (31)</strong></summary>

1. An Introduction to Statistical Learning.pdf  
2. Architecture of Advanced Numerical Analysis Systems - 978-1-4842-8853-5.pdf  
3. Bayesian Methods for Hackers Probabilistic Programming and Bayesian Inference.pdf  
4. Bayesian computational methods.pdf  
5. Bio-Inspired Computational Algorithms & Their Applications.pdf  
6. Comprehensive CI_CD Guide for Software and Data Projects.pdf  
7. Data Mining Concepts & applictions.pdf  
8. Data Science_ Theories, Models, Algorithms, and Analytics - DSA_Book.pdf  
9. Data Spaces.pdf  
10. Database Performance at Scale.pdf  
11. Foundations of Machine Learning - Foundations_of_Machine_Learning.pdf  
12. Genetic Programming New Approaches & Successfull Applications.pdf  
13. Git Notes for Professionals - GitNotesForProfessionals.pdf  
14. Gradient Expectations - Stucture, Origins, & Synthesis Of Predictive Neural Networks.pdf  
15. Haskell Notes for Professionals - HaskellNotesForProfessionals.pdf  
16. Hibernate Notes for Professionals - HibernateNotesForProfessionals.pdf  
17. Recurrent Neural Networks for Temporal Data Processing.pdf  
18. Scalable Data Management for Future Hardware.pdf  
19. Statistics Done Wrong - Alex_Reinhart-Statistics_Done_Wrong-EN.pdf  
20. The Data Engineering Cookbook.pdf  
21. The Data Lakehouse Platform For Dummies.pdf  
22. The Elements of Statistical Learning.pdf  
23. Theory & Practice of Cryptography & Network Security Protocols & Technologies.pdf  
24. Understanding Statistics & Experimental Design.pdf  
25. an-introduction-to-the-finite-element-method.pdf  
26. bayes-rule-a-tutorial-introduction-to-bayesian-analysis.pdf  
27. clean-architectures-in-python.pdf  
28. haykin.neural-networks.3ed.2009.pdf  
29. implementing-programming-languages-an-introduction-to-compilers-and-interpreters.pdf  
30. numerical-methods-in-engineering-with-matlab.pdf  
31. think-bayes-bayesian-statistics-in-python.pdf  

</details>

## Various programming languages & resources 🧰💻

<details>
<summary><strong>Embedded files (69)</strong></summary>

1. Algorithms Notes for Professionals - AlgorithmsNotesForProfessionals.pdf  
2. An Introduction to Spatial Data Analysis and Visualisation in R - An Introduction to Spatial Data Analysis in R.pdf  
3. Angular 2+ Notes for Professionals - Angular2NotesForProfessionals.pdf  
4. AngularJS Notes for Professionals - AngularJSNotesForProfessionals.pdf  
5. Bash Notes for Professionals - BashNotesForProfessionals.pdf  
6. C Notes for Professionals - CNotesForProfessionals.pdf  
7. C# Notes for Professionals - CSharpNotesForProfessionals.pdf  
8. C++ Notes for Professionals - CPlusPlusNotesForProfessionals.pdf  
9. CSS Notes for Professionals - CSSNotesForProfessionals.pdf  
10. Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf  
11. Comprehensive CI_CD Guide for Software and Data Projects.pdf  
12. Crafting a Compiler.pdf  
13. Entity Framework Notes for Professionals - EntityFrameworkNotesForProfessionals.pdf  
14. Essentials of Compilation - An Incremental Approach (python).pdf  
15. Excel VBA Notes for Professionals - ExcelVBANotesForProfessionals.pdf  
16. Free Android Development Book.pdf  
17. Generalized Topology Optimization for Structural Design.pdf  
18. HTML5 Canvas Notes for Professionals - HTML5CanvasNotesForProfessionals.pdf  
19. HTML5 Notes for Professionals - HTML5NotesForProfessionals.pdf  
20. Handbook Of Applied Cryptography (old).pdf  
21. Introduction to Numerical Methods for Variational Problems.pdf  
22. Introduction to finite element methods.pdf  
23. Introduction-to-Docker.pdf  
24. Java Notes for Professionals - JavaNotesForProfessionals.pdf  
25. JavaScript Notes for Professionals - JavaScriptNotesForProfessionals.pdf  
26. Kotlin Notes for Professionals - KotlinNotesForProfessionals.pdf  
27. LaTeX Notes for Professionals - LaTeXNotesForProfessionals.pdf  
28. Linux Notes for Professionals - LinuxNotesForProfessionals.pdf  
29. MATLAB Notes for Professionals - MATLABNotesForProfessionals.pdf  
30. MATLAB Programming for Engineers Stephen J. Chapman.pdf  
31. Matlab-Modeling, Programming & Simulations.pdf  
32. Microsoft SQL Server Notes for Professionals - MicrosoftSQLServerNotesForProfessionals.pdf  
33. MongoDB Notes for Professionals - MongoDBNotesForProfessionals.pdf  
34. MySQL Notes for Professionals - MySQLNotesForProfessionals.pdf  
35. NET Framework Notes for Professionals - DotNETFrameworkNotesForProfessionals.pdf  
36. Node.js Notes for Professionals - NodeJSNotesForProfessionals.pdf  
37. OCaml Practice.pdf  
38. Objective-C Notes for Professionals - ObjectiveCNotesForProfessionals.pdf  
39. Oracle Database Notes for Professionals - OracleDatabaseNotesForProfessionals.pdf  
40. PHP Notes for Professionals - PHPNotesForProfessionals.pdf  
41. Perl Notes for Professionals - PerlNotesForProfessionals.pdf  
42. PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf  
43. PowerShell Notes for Professionals - PowerShellNotesForProfessionals.pdf  
44. Python Notes for Professionals - PythonNotesForProfessionals.pdf  
45. R Notes for Professionals - RNotesForProfessionals.pdf  
46. React JS Notes for Professionals - ReactJSNotesForProfessionals.pdf  
47. React Native Notes for Professionals - ReactNativeNotesForProfessionals.pdf  
48. Ruby Notes for Professionals - RubyNotesForProfessionals.pdf  
49. Ruby on Rails Notes for Professionals - RubyOnRailsNotesForProfessionals.pdf  
50. SQL Notes for Professionals - SQLNotesForProfessionals.pdf  
51. ScipyLectures-simple.pdf  
52. Solving Ordinary Differential Equations in Python.pdf  
53. Solving PDEs in Python.pdf  
54. Spring Framework Notes for Professionals - SpringFrameworkNotesForProfessionals.pdf  
55. Swift Notes for Professionals - SwiftNotesForProfessionals.pdf  
56. The-Data-Engineers-Guide-to-Apache-Spark.pdf  
57. The-web-application-hackers-handbook-finding-and-exploiting-security-flaws.pdf  
58. TypeScript Notes for Professionals - TypeScriptNotesForProfessionals.pdf  
59. VBA Notes for Professionals - VBANotesForProfessionals.pdf  
60. Visual Basic .NET Notes for Professionals - VisualBasic_NETNotesForProfessionals.pdf  
61. Xamarin.Forms Notes for Professionals - XamarinFormsNotesForProfessionals.pdf  
62. applied-data-science-with-python-and-jupyter.pdf  
63. black-hat-python-python-programming-for-hackers-and-pentesters.pdf  
64. flexible-software-design-systems-development-for-changing-requirements.pdf  
65. iOS Developer Notes for Professionals - iOSNotesForProfessionals.pdf  
66. jQuery Notes for Professionals - jQueryNotesForProfessionals.pdf  
67. python-machine-learning-a-crash-course-for-beginners-to-understand-machine-learning-artificial-intelligence-neural-networks-and-deep-learning-with-scikit-learn-tensorflow-and-keras.pdf  
68. responsive-web-design-with-html5-and-css3.pdf  
69. software-architecture-patterns.pdf  

</details>

---

## 🧾 Suggested “starter set” to implement first (if this folder is empty)

If you’re bootstrapping templates, start with these:

1. ✅ `run_manifest.json` + `checksums.sha256` + `telemetry.ndjson`  
2. ✅ STAC Item + DCAT Dataset + PROV Bundle templates  
3. ✅ Story Node markdown + Evidence Manifest  
4. ✅ Focus Mode answer record + governance ledger entry  
5. ✅ Governance card + OPA policy skeleton  
6. ✅ SBOM + SLSA provenance placeholder for releases  
7. ✅ Graph health check cypher snippets  

---

## 🧠 Glossary (mini)

- **STAC**: SpatioTemporal Asset Catalog (spatial assets & collections)  
- **DCAT**: Data Catalog Vocabulary (dataset-level catalog & distributions)  
- **PROV**: W3C provenance model (entities, activities, agents)  
- **Evidence Manifest**: structured list of evidence behind a narrative or analysis  
- **OPA / Rego**: policy-as-code engine and language  
- **Conftest**: tool to run OPA policies against repo artifacts  
- **SBOM**: Software Bill of Materials  
- **SLSA / in-toto**: build provenance/attestation frameworks  
- **ORAS / Cosign**: OCI artifact distribution + cryptographic signing  
- **W‑P‑E**: Watcher → Planner → Executor agent pattern (auditable automation)

---

🧩 If you add a new template: **also add**
- ✅ a schema (`schemas/…`)  
- ✅ a validator (or conftest rule)  
- ✅ an example file (ideally under `examples/`)  
- ✅ a short doc update (link it from the master docs)


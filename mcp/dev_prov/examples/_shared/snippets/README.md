<!--
🧩 Shared snippet library for MCP dev_prov examples.
Goal: keep provenance-first patterns consistent + copy/paste friendly.
Prefer <details> blocks to keep this README scannable.
-->

# 🧩 Shared Snippets — `mcp/dev_prov` 🧾

<p align="center">
  <img alt="MCP" src="https://img.shields.io/badge/MCP-dev__prov-blue" />
  <img alt="Provenance" src="https://img.shields.io/badge/provenance-PROV%20%7C%20STAC%20%7C%20DCAT-6f42c1" />
  <img alt="Policy" src="https://img.shields.io/badge/policy-OPA%20%2B%20Conftest-orange" />
  <img alt="Evidence First" src="https://img.shields.io/badge/evidence--first-%E2%9C%85-brightgreen" />
  <img alt="Reproducible" src="https://img.shields.io/badge/reproducible-lab%20notebook-0aa" />
</p>

> 🧭 **Purpose:** This folder is a **copy/paste library** for the `dev_prov` example suite.  
> Every example that creates/changes **code, data, AI outputs, map layers, exports, or narratives** should emit **auditable provenance** and pass **policy gates** (no silent rewrites, no uncited claims, no bypassing governance). ✅

---

## 🧠 What “dev_prov” means here

In Kansas Frontier Matrix (KFM), “provenance” isn’t a nice-to-have — it’s the *interface contract* between pipeline stages:

- **ETL → Catalogs → Graph → API → UI → Story Nodes → Focus Mode** (ordering is non‑negotiable) 🧱
- Data is not “published” until it has the **evidence triplet**: **STAC + DCAT + PROV** 📦🧾
- The UI must **never** bypass the API and query the graph directly (governed API boundary) 🛡️
- Derived artifacts (including AI outputs) are treated as first‑class datasets with full metadata and lineage 🤖🧾
- Sensitive / sovereignty classifications propagate forward (outputs can’t be less restricted than inputs) 🏷️🔒

This snippets folder exists so every example implements those rules the same way.

---

## 🗺️ You are here

```text
mcp/
  dev_prov/
    examples/
      _shared/
        snippets/
          README.md     👈 you are here
          ...           (shared templates used by multiple examples)
```

---

## 📌 Quick links

- [Snippet contract](#-snippet-contract)
- [Placeholders](#-placeholders)
- [What you’ll find here](#-what-youll-find-here)
- [Core snippet templates](#-core-snippet-templates)
  - [PROV bundle (JSON‑LD)](#1--prov-bundle-json-ld)
  - [Evidence triplet (STAC/DCAT/PROV)](#2--evidence-triplet-stacdcatprov)
  - [OPA policy gate (Rego)](#3--opa-policy-gate-rego)
  - [GitHub PR → PROV mapping](#4--github-pr--prov-mapping)
  - [Story Node evidence manifest](#5--story-node-evidence-manifest)
  - [Focus Mode answer envelope](#6--focus-mode-answer-envelope)
  - [Layer provenance metadata](#7--layer-provenance-metadata)
  - [Offline pack + signed distribution](#8--offline-pack--signed-distribution)
  - [Sensitive data classification + redaction](#9--sensitive-data-classification--redaction)
  - [Run manifest + reproducibility log](#10--run-manifest--reproducibility-log)
- [Definition of Done for new snippets](#-definition-of-done-for-new-snippets)
- [Source docs used](#-source-docs-used)

---

## 🧾 Snippet contract

Every snippet should be:

1. **Minimal but complete** (smallest usable unit) 🧩  
2. **Evidence-first** (outputs link to STAC/DCAT/PROV or an evidence manifest) 📎  
3. **Append‑only friendly** (no silent rewrites; use new versions + hashes) 🧱  
4. **Policy-ready** (it should pass OPA/Conftest gates with no exceptions) 🛡️  
5. **Copy/paste safe** (clear placeholders, no secrets, deterministic defaults) ✅

### ✅ Snippet header template (recommended)

```text
# 🧩 SNIPPET: <name>
# Purpose: <one sentence>
# Inputs:  <list>
# Outputs: <list>
# Replace: {{PLACEHOLDER_1}}, {{PLACEHOLDER_2}}
# Notes:   <gotchas / policy expectations>
```

---

## 🧷 Placeholders

Snippets use `{{ALL_CAPS}}` placeholders. Common ones:

- `{{RUN_ID}}`, `{{RUN_AT}}` (ISO 8601)
- `{{GIT_SHA}}`, `{{REPO_URL}}`, `{{BRANCH}}`
- `{{PR_NUMBER}}`, `{{GITHUB_ACTOR}}`
- `{{DATASET_ID}}`, `{{STAC_ITEM_ID}}`, `{{DCAT_DATASET_ID}}`, `{{PROV_BUNDLE_ID}}`
- `{{INPUT_HASH_SHA256}}`, `{{OUTPUT_HASH_SHA256}}`
- `{{CLASSIFICATION}}` (e.g., `public`, `restricted`, `sensitive`)

---

## 📦 What you’ll find here

> 🧭 This directory is intentionally shared across examples — treat it like a tiny “API surface” for templates.

Typical snippet categories you’ll see (or add):

| Category | Why it exists | What it enforces |
|---|---|---|
| 🧾 `prov/` | Dev + data lineage templates | Who/what/when/with what inputs |
| 🗂️ `catalog/` | STAC/DCAT skeletons | Evidence-first publishing |
| 🛡️ `policy/` | Rego rules + test inputs | “Fail closed” governance |
| 🧪 `ci/` | CI workflow fragments | Gatekeeping on every PR |
| 📖 `story/` | Evidence manifests | No uncited narrative |
| 🎯 `focus/` | Focus Mode envelopes | Citations & context bundles |
| 🗺️ `layers/` | Map layer provenance metadata | Provenance panel correctness |
| 📦 `packs/` | Offline/export manifests | Provenance travels with exports |
| 🔒 `privacy/` | Classification + redaction patterns | Sovereignty & safety |

---

# 🧱 Core snippet templates

## 1) 🧾 PROV bundle (JSON‑LD)

Use this when you need to record a **dev event** (PR, CI run, release) *or* a **data event** (ETL run, export build) as a PROV activity.

<details>
<summary><b>📄 Template: PROV bundle skeleton (JSON‑LD)</b></summary>

```json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "dcterms": "http://purl.org/dc/terms/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "kfm": "https://kansasfrontiermatrix.org/ns#",
    "dev": "https://kansasfrontiermatrix.org/ns/dev#"
  },
  "@id": "urn:kfm:prov:bundle:{{PROV_BUNDLE_ID}}",
  "@type": "prov:Bundle",

  "dcterms:created": { "@value": "{{RUN_AT}}", "@type": "xsd:dateTime" },

  "prov:agent": [
    {
      "@id": "urn:git:actor:{{GITHUB_ACTOR}}",
      "@type": ["prov:Agent", "dev:Contributor"],
      "dcterms:identifier": "{{GITHUB_ACTOR}}"
    },
    {
      "@id": "urn:gh:bot:actions",
      "@type": ["prov:Agent", "dev:CIBot"],
      "dcterms:title": "GitHub Actions"
    }
  ],

  "prov:entity": [
    {
      "@id": "urn:git:commit:{{GIT_SHA}}",
      "@type": ["prov:Entity", "dev:Commit"],
      "dcterms:identifier": "{{GIT_SHA}}",
      "kfm:hash_sha256": "{{COMMIT_HASH_SHA256}}"
    },
    {
      "@id": "urn:kfm:dataset:{{DATASET_ID}}",
      "@type": ["prov:Entity", "kfm:Dataset"],
      "dcterms:identifier": "{{DATASET_ID}}",
      "kfm:classification": "{{CLASSIFICATION}}"
    }
  ],

  "prov:activity": [
    {
      "@id": "urn:kfm:activity:{{RUN_ID}}",
      "@type": ["prov:Activity", "dev:PipelineRun"],
      "prov:startedAtTime": { "@value": "{{RUN_AT}}", "@type": "xsd:dateTime" },

      "prov:wasAssociatedWith": [
        { "@id": "urn:gh:bot:actions" },
        { "@id": "urn:git:actor:{{GITHUB_ACTOR}}" }
      ],

      "prov:used": [
        { "@id": "urn:git:commit:{{GIT_SHA}}" }
      ],

      "prov:generated": [
        { "@id": "urn:kfm:artifact:{{OUTPUT_HASH_SHA256}}" }
      ]
    }
  ],

  "prov:wasGeneratedBy": [
    {
      "prov:entity": { "@id": "urn:kfm:artifact:{{OUTPUT_HASH_SHA256}}" },
      "prov:activity": { "@id": "urn:kfm:activity:{{RUN_ID}}" }
    }
  ]
}
```

</details>

✅ Best practices:
- Treat every important action as an **Activity** with explicit **Agents** and **Entities**.
- Include **hashes** for inputs/outputs so “same inputs → same outputs” can be verified.
- Emit a new PROV bundle per run (append‑only; never “edit history”).

---

## 2) 🗂️ Evidence triplet (STAC/DCAT/PROV)

KFM’s “evidence-first publishing” requires:

- **STAC** (assets + spatial/temporal info) 🗺️
- **DCAT** (discoverability + distributions) 🧾
- **PROV** (lineage + transformation) 🧬

<details>
<summary><b>📄 Template: STAC Item + DCAT Dataset + PROV linkage</b></summary>

### 🗺️ STAC Item (minimal)
```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "{{STAC_ITEM_ID}}",
  "collection": "{{STAC_COLLECTION_ID}}",
  "bbox": [-180, -90, 180, 90],
  "geometry": null,
  "properties": {
    "datetime": "{{RUN_AT}}",
    "kfm:dataset_id": "{{DATASET_ID}}",
    "kfm:classification": "{{CLASSIFICATION}}",
    "kfm:prov_bundle": "urn:kfm:prov:bundle:{{PROV_BUNDLE_ID}}"
  },
  "assets": {
    "data": {
      "href": "{{ASSET_HREF}}",
      "type": "{{MIME_TYPE}}",
      "roles": ["data"],
      "extra_fields": {
        "kfm:hash_sha256": "{{OUTPUT_HASH_SHA256}}"
      }
    }
  },
  "links": [
    { "rel": "via", "href": "{{DCAT_DATASET_URI}}" },
    { "rel": "derived_from", "href": "{{INPUT_STAC_ITEM_URI}}" }
  ]
}
```

### 🧾 DCAT Dataset (JSON‑LD minimal)
```json
{
  "@context": {
    "dcat": "http://www.w3.org/ns/dcat#",
    "dcterms": "http://purl.org/dc/terms/",
    "prov": "http://www.w3.org/ns/prov#",
    "kfm": "https://kansasfrontiermatrix.org/ns#"
  },
  "@id": "urn:kfm:dcat:dataset:{{DCAT_DATASET_ID}}",
  "@type": "dcat:Dataset",
  "dcterms:title": "{{TITLE}}",
  "dcterms:description": "{{DESCRIPTION}}",
  "dcterms:license": "{{LICENSE_SPDX_OR_URL}}",
  "kfm:classification": "{{CLASSIFICATION}}",
  "prov:wasGeneratedBy": { "@id": "urn:kfm:activity:{{RUN_ID}}" },
  "dcat:distribution": [
    {
      "@type": "dcat:Distribution",
      "dcterms:format": "{{MIME_TYPE}}",
      "dcat:accessURL": "{{STAC_ITEM_URI}}",
      "kfm:hash_sha256": "{{OUTPUT_HASH_SHA256}}"
    }
  ]
}
```

### 🧬 PROV bundle reference pattern
- STAC `kfm:prov_bundle` → `urn:kfm:prov:bundle:...`
- DCAT `prov:wasGeneratedBy` → Activity in the PROV bundle
- Graph nodes should store **references** to STAC/DCAT/PROV IDs (not bulky payloads)

</details>

---

## 3) 🛡️ OPA policy gate (Rego)

Policy snippets codify the KFM invariants (fail closed; no bypass). Examples include:

- **Processed data changed but no PROV update** (classic “silent rewrite”)
- **Missing license / missing metadata**
- **UI or tooling attempting to bypass the governed API boundary**
- **Classification downgrade**

<details>
<summary><b>📄 Template: deny processed-data changes without PROV update (KFM-PROV-001 style)</b></summary>

```rego
package kfm.policy.provenance

# Expected input shape:
# input.changed_files = [{"path": "data/processed/foo.csv"}, {"path":"data/prov/foo.jsonld"}, ...]
# (Adapt to your conftest input adapter.)

deny[msg] {
  some f
  f := input.changed_files[_].path
  startswith(f, "data/processed/")

  not prov_updated

  msg := "KFM-PROV-001: Processed data changed without matching PROV update (append-only rule)."
}

prov_updated {
  some p
  p := input.changed_files[_].path
  startswith(p, "data/prov/")
}
```

</details>

✅ Tip: pair this with a tiny test input JSON under `policy/testdata/` so the snippet is demonstrably correct.

---

## 4) 🔁 GitHub PR → PROV mapping

KFM explicitly treats DevOps activity (PRs, reviews, CI runs) as provenance events that can be recorded and later queried alongside data lineage.

<details>
<summary><b>📄 Template: PR event mapping → PROV Activity</b></summary>

```json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "dcterms": "http://purl.org/dc/terms/",
    "dev": "https://kansasfrontiermatrix.org/ns/dev#"
  },
  "@id": "urn:kfm:prov:bundle:pr:{{PR_NUMBER}}:{{GIT_SHA}}",
  "@type": "prov:Bundle",
  "prov:agent": [
    {
      "@id": "urn:git:actor:{{GITHUB_ACTOR}}",
      "@type": ["prov:Agent", "dev:Contributor"]
    }
  ],
  "prov:entity": [
    { "@id": "urn:git:pr:{{PR_NUMBER}}", "@type": ["prov:Entity", "dev:PullRequest"] },
    { "@id": "urn:git:commit:{{GIT_SHA}}", "@type": ["prov:Entity", "dev:Commit"] }
  ],
  "prov:activity": [
    {
      "@id": "urn:git:activity:pr_opened:{{PR_NUMBER}}",
      "@type": ["prov:Activity", "dev:PullRequestOpened"],
      "prov:wasAssociatedWith": [{ "@id": "urn:git:actor:{{GITHUB_ACTOR}}" }],
      "prov:used": [{ "@id": "urn:git:commit:{{GIT_SHA}}" }],
      "prov:generated": [{ "@id": "urn:git:pr:{{PR_NUMBER}}" }]
    }
  ]
}
```

</details>

✨ When combined with policy gates, you can explain **why** a PR was blocked (“missing license”, “missing PROV”) with a **traceable audit chain**.

---

## 5) 📖 Story Node evidence manifest

Story Nodes / narrative artifacts must be **machine-ingestible** and evidence-linked: every claim points to cataloged sources.

<details>
<summary><b>📄 Template: evidence manifest (YAML)</b></summary>

```yaml
# 🧩 SNIPPET: story/evidence_manifest.yaml
story_id: "{{STORY_ID}}"
title: "{{TITLE}}"
status: draft # draft|review|published
created_at: "{{RUN_AT}}"

claims:
  - id: C1
    text: "{{CLAIM_TEXT}}"
    confidence: "{{CONFIDENCE_ENUM}}" # high|medium|low
    evidence:
      - dcat: "urn:kfm:dcat:dataset:{{DCAT_DATASET_ID}}"
      - stac: "{{STAC_ITEM_URI}}"
      - prov: "urn:kfm:prov:bundle:{{PROV_BUNDLE_ID}}"

outputs:
  - type: story_node
    path: "docs/reports/story_nodes/{{STORY_ID}}/story.md"
    hash_sha256: "{{OUTPUT_HASH_SHA256}}"
```

</details>

✅ This is the bridge between narrative and the evidence triplet.

---

## 6) 🎯 Focus Mode answer envelope

Focus Mode responses must be **bounded by evidence**: citations are first-class, and any AI-generated suggestion is explicitly labeled.

<details>
<summary><b>📄 Template: Focus Mode response payload (JSON)</b></summary>

```json
{
  "mode": "focus",
  "story_id": "{{STORY_ID}}",
  "answer": "{{ANSWER_TEXT}}",
  "confidence": "{{CONFIDENCE_ENUM}}",
  "citations": [
    {
      "label": "Primary dataset",
      "dcat": "urn:kfm:dcat:dataset:{{DCAT_DATASET_ID}}",
      "stac": "{{STAC_ITEM_URI}}",
      "prov": "urn:kfm:prov:bundle:{{PROV_BUNDLE_ID}}"
    }
  ],
  "ai_generated": true,
  "audit": {
    "run_id": "{{RUN_ID}}",
    "run_at": "{{RUN_AT}}",
    "policy_pack": "{{POLICY_PACK_VERSION}}"
  }
}
```

</details>

---

## 7) 🗺️ Layer provenance metadata

Every map layer should carry provenance metadata so the UI can surface it in a **Layer Provenance panel** (and exports can carry provenance forward).

<details>
<summary><b>📄 Template: layer config (TypeScript-ish object)</b></summary>

```ts
export const layer = {
  id: "{{LAYER_ID}}",
  title: "{{TITLE}}",
  source: {
    type: "{{SOURCE_TYPE}}", // vector|raster|geojson|tileset
    href: "{{ASSET_HREF}}",
    hash_sha256: "{{OUTPUT_HASH_SHA256}}"
  },
  catalog: {
    dcat: "urn:kfm:dcat:dataset:{{DCAT_DATASET_ID}}",
    stac: "{{STAC_ITEM_URI}}",
    prov: "urn:kfm:prov:bundle:{{PROV_BUNDLE_ID}}"
  },
  governance: {
    classification: "{{CLASSIFICATION}}",
    license: "{{LICENSE_SPDX_OR_URL}}",
    citations_required: true
  }
};
```

</details>

---

## 8) 📦 Offline pack + signed distribution

Exports/offline packs should carry provenance + hashes and (optionally) be distributed as signed artifacts.

<details>
<summary><b>📄 Template: offline pack manifest (YAML)</b></summary>

```yaml
pack_id: "{{PACK_ID}}"
created_at: "{{RUN_AT}}"
includes:
  - stac: "{{STAC_ITEM_URI}}"
  - dcat: "urn:kfm:dcat:dataset:{{DCAT_DATASET_ID}}"
  - prov: "urn:kfm:prov:bundle:{{PROV_BUNDLE_ID}}"

artifacts:
  - path: "exports/{{PACK_ID}}/tiles.pmtiles"
    hash_sha256: "{{TILES_HASH_SHA256}}"
  - path: "exports/{{PACK_ID}}/catalog.json"
    hash_sha256: "{{CATALOG_HASH_SHA256}}"

distribution:
  type: oci # e.g., stored in a container registry
  ref: "{{OCI_REF}}" # registry/repo:tag or @digest
  signing:
    method: "sigstore/cosign"
    transparency_log: true
```

</details>

---

## 9) 🔒 Sensitive data classification + redaction

Snippets here support the rule: **no output artifact can be less restricted than its inputs**.

<details>
<summary><b>📄 Template: classification tag block (YAML)</b></summary>

```yaml
classification:
  level: "{{CLASSIFICATION}}" # public|restricted|sensitive
  reason: "{{REASON}}"
  propagation: "inherit"
  map_display:
    strategy: "generalize" # generalize|blur|hide
    radius_meters: 10000
```

</details>

<details>
<summary><b>📄 Template: policy rule — prevent classification downgrade (Rego)</b></summary>

```rego
package kfm.policy.classification

deny[msg] {
  input.output.classification.level == "public"
  input.input_max_classification.level != "public"
  msg := "KFM-CLASS-001: Output classification cannot be less restrictive than inputs."
}
```

</details>

---

## 10) 🧪 Run manifest + reproducibility log

This is the “lab notebook” side of dev provenance: every run should be reconstructible with config, environment, and references.

<details>
<summary><b>📄 Template: run_manifest.yaml</b></summary>

```yaml
run_id: "{{RUN_ID}}"
run_at: "{{RUN_AT}}"
git:
  repo: "{{REPO_URL}}"
  sha: "{{GIT_SHA}}"
  branch: "{{BRANCH}}"

objective: "{{OBJECTIVE}}"
hypothesis: "{{HYPOTHESIS}}" # optional but encouraged

inputs:
  - id: "{{DATASET_ID}}"
    dcat: "urn:kfm:dcat:dataset:{{DCAT_DATASET_ID}}"
    stac: "{{STAC_ITEM_URI}}"
    hash_sha256: "{{INPUT_HASH_SHA256}}"

method:
  pipeline: "{{PIPELINE_NAME}}"
  config_path: "{{CONFIG_PATH}}"
  parameters:
    seed: "{{SEED}}"
    crs_target: "EPSG:4326"

outputs:
  - path: "{{OUTPUT_PATH}}"
    hash_sha256: "{{OUTPUT_HASH_SHA256}}"
    prov: "urn:kfm:prov:bundle:{{PROV_BUNDLE_ID}}"

validation:
  - "schema: stac"
  - "schema: dcat"
  - "schema: prov"
  - "policy: opa/conftest"
```

</details>

✅ Keep “run manifests” append‑only and tied to PROV bundles via IDs and hashes.

---

## ✅ Definition of Done for new snippets

Before adding a snippet, make sure it:

- [ ] Has a **clear name** + a 1‑sentence purpose 🧩  
- [ ] Uses `{{PLACEHOLDERS}}` consistently 🧷  
- [ ] Produces or references **STAC/DCAT/PROV** (or an evidence manifest) 📦  
- [ ] Is compatible with **policy gates** (OPA/Conftest) 🛡️  
- [ ] Avoids secrets and includes no private keys 🔐  
- [ ] Doesn’t teach bypasses (fail closed) 🚫  
- [ ] Mentions classification/sovereignty expectations when relevant 🏷️  
- [ ] Includes a tiny example input/output (or testdata) ✅

---

## 📚 Source docs used

> These snippets are aligned with KFM’s evidence-first, contract-first, and governance-first architecture.

<details>
<summary><b>📎 Click to expand the project references</b></summary>

### Core KFM docs
- Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖  [oai_citation:2‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
- Kansas Frontier Matrix – Comprehensive UI System Overview  [oai_citation:3‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)
- 📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide  [oai_citation:4‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM)  [oai_citation:5‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)
- 🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals  [oai_citation:6‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)
- Additional Project Ideas  [oai_citation:7‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### Repo + documentation standards
- MARKDOWN_GUIDE_v13 (contract-first, evidence-first pipeline rules)  [oai_citation:8‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- Kansas-Frontier-Matrix — Open-Source Geospatial Historical Mapping Hub Design  [oai_citation:9‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw)

### Research / reproducibility protocol
- Scientific Method _ Research _ Master Coder Protocol Documentation  [oai_citation:10‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

### Reference libraries (PDF portfolios)
> ⚠️ Some reference packs are “PDF portfolios” and may require opening in Acrobat/Reader to browse attachments.
- AI Concepts & more (portfolio)  [oai_citation:11‡AI Concepts & more.pdf](file-service://file-K6BctJjeUwvyCahLf9qdwr)
- Maps · GoogleMaps · VirtualWorlds · Archaeological · Computer Graphics · Geospatial · WebGL (portfolio)  [oai_citation:12‡Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf](file-service://file-RrXMFY7cP925exsQYermf2)
- Various programming languages & resources (portfolio)  [oai_citation:13‡Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf](file-service://file-RshcX5sNY2wpiNjRfoP6z6)
- Data Management · Architectures · Data Science · Bayesian Methods (portfolio)  [oai_citation:14‡Various programming langurages & resources 1.pdf](file-service://file-4wp3wSSZs7gk5qHWaJVudi)

### Extracted supporting references (from the portfolios)
- KFM Python Geospatial Analysis Cookbook (supporting geospatial patterns)  [oai_citation:15‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)
- Data Mining Concepts & Applications (supporting privacy / re-run considerations)  [oai_citation:16‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)

### Legacy/earlier citation markers surfaced by the build system
-  [oai_citation:17‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)
-  [oai_citation:18‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
-  [oai_citation:19‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)
-  [oai_citation:20‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

</details>

---

## 🧭 Next steps

- If you add a new snippet file, **update this README** with:
  - the category it belongs to
  - the placeholder set it uses
  - the policy gate it must satisfy

Happy provenance-building 🧾✨

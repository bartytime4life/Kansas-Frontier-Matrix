# 📮 API Request Examples (Contract-First) — `api/contracts/examples/requests/`

![Contracts](https://img.shields.io/badge/contracts-first-1f6feb)
![Evidence](https://img.shields.io/badge/evidence-first-2ea043)
![Geo](https://img.shields.io/badge/GeoJSON%20%7C%20COG%20%7C%20STAC%20%7C%20DCAT%20%7C%20PROV-0ea5e9)

Welcome! This folder holds **copy/paste-ready HTTP requests** that are meant to stay aligned with our **API contracts** (OpenAPI + GraphQL) and our **evidence-first pipeline** (catalogs + provenance before narratives). 🧭

> **Rule of thumb:** If a request example doesn’t match the contract, the example is wrong — not the other way around. ✅

---

## 🧱 What lives here?

- ✅ **Requests only**: `.http`, `curl` snippets, `.json` payloads, `.graphql` queries
- ✅ **Deterministic** examples: stable params, reproducible outputs, fixture-friendly
- ✅ **Safe** examples: **no secrets**, **no PII**, **no protected coordinates**
- ✅ **Contract-aligned**: mirrors OpenAPI/GraphQL schemas and expected headers

If you’re looking for **schemas/specs**, those belong in **`api/contracts/`** (or the canonical contract home for the repo), not here. 📜

---

## 🗂️ Suggested layout (recommended)

```text
api/contracts/examples/requests/
├── 📄 README.md
├── 📁 _shared/                      # reusable snippets + env templates
│   ├── 📄 .env.example
│   ├── 📄 headers.http              # shared headers block for .http files
│   └── 📄 vars.http                 # base_url/token variables for .http files
├── 📁 catalog/                      # STAC/DCAT/PROV discovery
│   ├── 📄 stac_search.http
│   ├── 📄 dcat_feed.http
│   └── 📄 prov_get.http
├── 📁 datasets/                     # dataset metadata + feature access
│   ├── 📄 dataset_get.http
│   ├── 📄 features_geojson.http
│   └── 📄 raster_tile.http
├── 📁 graph/                        # GraphQL knowledge graph queries
│   ├── 📄 graphql_query.graphql
│   └── 📄 graphql_request.http
├── 📁 analysis/                     # analysis jobs (submit/poll/results)
│   ├── 📄 job_submit.http
│   ├── 📄 job_status.http
│   └── 📄 job_result.http
└── 📁 story/                        # Story Nodes + Focus Mode bundles
    ├── 📄 story_list.http
    ├── 📄 story_get.http
    └── 📄 focus_bundle.http
```

---

## 🚀 Quickstart

### 1) Set env vars (recommended)
Create `api/contracts/examples/requests/_shared/.env` (gitignored) from the template:

```bash
cp api/contracts/examples/requests/_shared/.env.example \
   api/contracts/examples/requests/_shared/.env
```

Example `_shared/.env.example`:

```bash
# ✅ base URL for your running API (local, docker, staging, etc.)
KFM_API_BASE_URL=http://localhost:8000

# ✅ optional auth token (leave blank for public endpoints)
KFM_API_TOKEN=

# ✅ stable identifiers used in examples (prefer fixtures)
KFM_DATASET_ID=example.public.dataset
KFM_STAC_COLLECTION_ID=example.collection
KFM_STAC_ITEM_ID=example.item
KFM_STORY_SLUG=example-story
```

---

## 🧰 Supported formats & tools

### ✅ `.http` (VS Code REST Client / IntelliJ HTTP client)
- Great for team sharing + variables + easy execution.
- Prefer this format for **most** examples.

### ✅ `curl` snippets
- Minimal dependencies.
- Great for docs and CI smoke runs.

### ✅ `.graphql`
- Store GraphQL queries separately for readability.
- Wrap them with a `.http` or `curl` request when needed.

---

## 🧩 Shared conventions

### 🌐 Base URL
Use **one** base URL everywhere:

- `${KFM_API_BASE_URL}` in bash/curl examples
- `{{base_url}}` in `.http` examples (see template below)

### 🧾 Common headers (recommended baseline)
```http
Accept: application/json
Content-Type: application/json
```

For GeoJSON responses:
```http
Accept: application/geo+json
```

For JSON-LD (DCAT/PROV):
```http
Accept: application/ld+json
```

Auth (if required):
```http
Authorization: Bearer {{token}}
```

### 🧷 Request IDs (optional but helpful)
If your API supports it, include:
```http
X-Request-Id: {{request_id}}
```

---

## 📚 Example requests (copy/paste ready)

> **Heads up:** Endpoint paths below are **illustrative**. The **OpenAPI/GraphQL contracts** are the source of truth for the exact paths, params, and response shapes. 🧠

---

### 1) 🗂️ Catalog — STAC search (POST)

<details>
<summary><strong>📄 catalog/stac_search.http</strong></summary>

```http
### STAC Search (bbox + datetime)
@base_url = {{$dotenv KFM_API_BASE_URL}}
@token = {{$dotenv KFM_API_TOKEN}}
@collection_id = {{$dotenv KFM_STAC_COLLECTION_ID}}

POST {{base_url}}/v1/stac/search
Accept: application/json
Content-Type: application/json
Authorization: Bearer {{token}}

{
  "collections": ["{{collection_id}}"],
  "bbox": [-102.05, 36.99, -94.60, 40.00],
  "datetime": "1850-01-01T00:00:00Z/1900-12-31T23:59:59Z",
  "limit": 10
}
```
</details>

---

### 2) 🧾 Catalog — DCAT feed (GET)

<details>
<summary><strong>📄 catalog/dcat_feed.http</strong></summary>

```http
### DCAT feed (dataset discovery)
@base_url = {{$dotenv KFM_API_BASE_URL}}

GET {{base_url}}/v1/catalog/dcat
Accept: application/ld+json
```
</details>

---

### 3) 🧬 Catalog — PROV lineage (GET)

<details>
<summary><strong>📄 catalog/prov_get.http</strong></summary>

```http
### PROV lineage bundle for a dataset (JSON-LD)
@base_url = {{$dotenv KFM_API_BASE_URL}}
@dataset_id = {{$dotenv KFM_DATASET_ID}}

GET {{base_url}}/v1/catalog/prov/{{dataset_id}}
Accept: application/ld+json
```
</details>

---

### 4) 🧱 Dataset — metadata (GET)

<details>
<summary><strong>📄 datasets/dataset_get.http</strong></summary>

```http
### Dataset metadata (should link out to STAC/DCAT/PROV where applicable)
@base_url = {{$dotenv KFM_API_BASE_URL}}
@dataset_id = {{$dotenv KFM_DATASET_ID}}

GET {{base_url}}/v1/datasets/{{dataset_id}}
Accept: application/json
```
</details>

---

### 5) 🗺️ Dataset — GeoJSON features (GET)

<details>
<summary><strong>📄 datasets/features_geojson.http</strong></summary>

```http
### GeoJSON features for a dataset (filtered by bbox + time)
@base_url = {{$dotenv KFM_API_BASE_URL}}
@dataset_id = {{$dotenv KFM_DATASET_ID}}

GET {{base_url}}/v1/datasets/{{dataset_id}}/features?bbox=-102.05,36.99,-94.60,40.00&datetime=1860-01-01T00:00:00Z/1870-12-31T23:59:59Z&limit=500
Accept: application/geo+json
```
</details>

---

### 6) 🧱 Raster — tile request (GET)

<details>
<summary><strong>📄 datasets/raster_tile.http</strong></summary>

```http
### Raster tile (example; contract defines exact format: png/jpg/pbf/etc.)
@base_url = {{$dotenv KFM_API_BASE_URL}}
@dataset_id = {{$dotenv KFM_DATASET_ID}}

GET {{base_url}}/v1/tiles/{{dataset_id}}/12/1053/1566.png
Accept: image/png
```
</details>

---

### 7) 🧠 GraphQL — knowledge graph query

<details>
<summary><strong>📄 graph/graphql_query.graphql</strong></summary>

```graphql
query PersonWithEvents($personId: ID!, $from: DateTime!, $to: DateTime!) {
  person(id: $personId) {
    id
    name
    events(from: $from, to: $to, limit: 50) {
      id
      label
      startTime
      endTime
      places(limit: 10) { id name }
      sources(limit: 10) { id title dcatRef stacRef provRef }
    }
  }
}
```
</details>

<details>
<summary><strong>📄 graph/graphql_request.http</strong></summary>

```http
### GraphQL request wrapper
@base_url = {{$dotenv KFM_API_BASE_URL}}
@token = {{$dotenv KFM_API_TOKEN}}

POST {{base_url}}/graphql
Accept: application/json
Content-Type: application/json
Authorization: Bearer {{token}}

{
  "query": "query PersonWithEvents($personId: ID!, $from: DateTime!, $to: DateTime!) { person(id: $personId) { id name events(from: $from, to: $to, limit: 50) { id label startTime endTime places(limit: 10) { id name } sources(limit: 10) { id title dcatRef stacRef provRef } } } }",
  "variables": {
    "personId": "person:example",
    "from": "1850-01-01T00:00:00Z",
    "to": "1900-12-31T23:59:59Z"
  }
}
```
</details>

---

### 8) 🧪 Analysis — submit → poll → result

<details>
<summary><strong>📄 analysis/job_submit.http</strong></summary>

```http
### Submit an analysis job (example)
@base_url = {{$dotenv KFM_API_BASE_URL}}
@token = {{$dotenv KFM_API_TOKEN}}

POST {{base_url}}/v1/analysis/jobs
Accept: application/json
Content-Type: application/json
Authorization: Bearer {{token}}

{
  "type": "example_analysis",
  "inputs": {
    "datasetId": "{{$dotenv KFM_DATASET_ID}}",
    "bbox": [-102.05, 36.99, -94.60, 40.00],
    "datetime": "1900-01-01T00:00:00Z/1900-12-31T23:59:59Z"
  },
  "options": {
    "deterministic": true
  }
}
```
</details>

<details>
<summary><strong>📄 analysis/job_status.http</strong></summary>

```http
### Poll job status
@base_url = {{$dotenv KFM_API_BASE_URL}}
@job_id = job:example

GET {{base_url}}/v1/analysis/jobs/{{job_id}}
Accept: application/json
```
</details>

<details>
<summary><strong>📄 analysis/job_result.http</strong></summary>

```http
### Fetch job result (often a dataset/distribution link)
@base_url = {{$dotenv KFM_API_BASE_URL}}
@job_id = job:example

GET {{base_url}}/v1/analysis/jobs/{{job_id}}/result
Accept: application/json
```
</details>

---

### 9) 🎬 Story Nodes — list → get → Focus bundle

<details>
<summary><strong>📄 story/story_list.http</strong></summary>

```http
### List published story nodes
@base_url = {{$dotenv KFM_API_BASE_URL}}

GET {{base_url}}/v1/story-nodes?status=published&limit=25
Accept: application/json
```
</details>

<details>
<summary><strong>📄 story/story_get.http</strong></summary>

```http
### Get a story node by slug
@base_url = {{$dotenv KFM_API_BASE_URL}}
@slug = {{$dotenv KFM_STORY_SLUG}}

GET {{base_url}}/v1/story-nodes/{{slug}}
Accept: application/json
```
</details>

<details>
<summary><strong>📄 story/focus_bundle.http</strong></summary>

```http
### Focus Mode context bundle (should be provenance-linked only)
@base_url = {{$dotenv KFM_API_BASE_URL}}
@slug = {{$dotenv KFM_STORY_SLUG}}

GET {{base_url}}/v1/story-nodes/{{slug}}/focus-bundle
Accept: application/json
```
</details>

---

## ✅ “Definition of done” for a new request example

When you add a request example, make sure it:

- [ ] **Matches the contract** (OpenAPI/GraphQL schema)
- [ ] Uses **fixture-safe identifiers** (no “random” IDs)
- [ ] Avoids **secrets/PII/sensitive locations**
- [ ] Is **reproducible** (same inputs → same shape of output)
- [ ] Includes **notes inline** if anything is intentionally optional/variant
- [ ] Updates this README if it introduces a new category or convention

---

## 🧯 Security & governance guardrails (non-negotiable)

- 🔒 Never commit real tokens or API keys
- 🧍 Never commit personal data (PII) in examples
- 🧭 If an endpoint may expose sensitive locations, examples must demonstrate **redaction-safe** usage (coarser bbox, generalized geometry, public-safe layer, etc.)
- 🧾 Prefer requests that reinforce **provenance visibility** (catalog links, lineage refs)

---

## 🧾 Minimal templates (starter snippets)

### 🧪 `.http` starter
```http
@base_url = {{$dotenv KFM_API_BASE_URL}}
@token = {{$dotenv KFM_API_TOKEN}}

GET {{base_url}}/v1/health
Accept: application/json
Authorization: Bearer {{token}}
```

### 🧰 `curl` starter
```bash
curl -sS "${KFM_API_BASE_URL}/v1/health" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer ${KFM_API_TOKEN}"
```

---

## ✨ Tips that keep examples maintainable

- ✅ Prefer **GET** examples for “docs + smoke tests”
- ✅ Keep payloads **small** and **schema-valid**
- ✅ Use **ISO-8601** for datetime ranges
- ✅ Use **WGS84 (EPSG:4326)** for bbox/geo params unless a contract explicitly says otherwise
- ✅ If you need a “real” ID, add a **fixture dataset** and reference it consistently

---

💡 If you’re unsure what to write, start by copying an existing request from this folder and only change **one thing** at a time. Small diffs make contract drift easy to spot. 👀

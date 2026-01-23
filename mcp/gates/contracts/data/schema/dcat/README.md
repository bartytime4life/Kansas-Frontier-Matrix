# 🧾 DCAT Dataset Contract (KFM Profile) — `mcp/gates/contracts/data/schema/dcat`

![Contract](https://img.shields.io/badge/contract-DCAT-blue)
![Evidence](https://img.shields.io/badge/evidence-STAC%20%2B%20DCAT%20%2B%20PROV-purple)
![Policy](https://img.shields.io/badge/policy-OPA%20%2B%20Conftest-success)
![Gates](https://img.shields.io/badge/gates-fail--closed-critical)
![Format](https://img.shields.io/badge/format-JSON--LD-informational)

> **Rule of the road:** if it shows up in **UI** or **Focus Mode**, it must be **traceable**, **cataloged**, and **provable**.  
> DCAT is the **catalog “front cover”** for each dataset (discovery + licensing + distribution pointers).

---

## 🎯 What this contract is

This folder documents the **DCAT contract** that KFM uses to publish **dataset-level catalog metadata**.

DCAT in KFM is used to:

- 🔎 **Make datasets discoverable** (title, description, keywords, themes, contact, publisher).
- 🪪 **Make datasets usable** (license, rights/access, governance tags).
- 🔗 **Point to the evidence triplet** (STAC + DCAT + PROV) and the actual artifacts.
- 🧠 Support **Focus Mode citations** and **UI source attribution** (the UI pulls “Source: …” style labels from catalog metadata).
- 🧾 Enable external indexing/harvesting (DCAT is friendly to portals/catalog tools).

---

## 🧭 Where this fits in the KFM pipeline

KFM follows **evidence-first publishing**: data is not “in the platform” until the metadata exists and passes gates.

```mermaid
flowchart LR
  A[📥 data/raw (immutable evidence)] --> B[🧪 data/work (transforms)]
  B --> C[📦 data/processed (derivatives)]
  C --> D[🧷 Catalog Triplet<br/>STAC + DCAT + PROV]
  D --> E[🕸 Knowledge Graph (Neo4j)]
  E --> F[🧰 API Layer (FastAPI/GraphQL)]
  F --> G[🗺 UI + 🧠 Focus Mode]
```

**This README is for (D):** the **DCAT** part of the triplet.

---

## ✅ Scope

### ✅ In scope
- `dcat:Dataset` records (JSON-LD)
- `dcat:Distribution` entries (download URLs, access URLs, formats, checksums, OCI references)
- KFM extensions (`kfm:*`) for:
  - classification / sensitivity
  - sovereignty / CARE governance markers
  - run manifests and deterministic pipeline metadata pointers
  - cross-links to STAC + PROV artifacts

### ❌ Out of scope (but required elsewhere)
- STAC schema (Items/Collections) → see `mcp/gates/contracts/data/schema/stac/`
- PROV schema (lineage) → see `mcp/gates/contracts/data/schema/prov/`
- Graph model / ontology rules (Neo4j import shapes)
- UI rendering rules (legend, layer cards, citations UI)
- Domain-specific specs (Design Packs, SampleUnitSpec, MetricSpec) — DCAT may reference them, but they are separate artifacts.

---

## 🗂️ Expected layout (contract + examples)

> The repo may evolve, but this is the intended “shape” 👇

```text
📦 mcp/
 └─ 🚪 gates/
    └─ 📜 contracts/
       └─ 📂 data/
          └─ 🧬 schema/
             └─ 🧾 dcat/
                ├─ README.md              👈 you are here
                ├─ dcat.dataset.schema.json   (expected)
                ├─ context.jsonld             (expected)
                └─ examples/
                   ├─ minimal.dataset.jsonld
                   ├─ full.dataset.jsonld
                   └─ oci.distribution.jsonld
```

---

## 🧩 KFM DCAT profile (what “valid” means)

KFM uses DCAT as a **dataset catalog record**, typically serialized as **JSON-LD**.

### 1) Dataset identity (stable + versioned)
A DCAT Dataset record **MUST** have:

- `@type: "dcat:Dataset"`
- A stable identifier:
  - `@id` (IRI/URN recommended)
  - `dct:identifier` (string, used heavily in tooling + graph import)

**Recommended dataset ID pattern (human + machine friendly):**
- `"{region}.{domain}.{slug}.v{semver}"`  
  Example: `ks.landcover.1990_2020.v1.0.0`

### 2) Core discovery metadata (minimum viable catalog)
A DCAT Dataset record **MUST** include:

- `dct:title`
- `dct:description`
- `dct:publisher` *or* `dct:creator`
- `dct:license`  
  - **Use an SPDX-style string** whenever possible (helps policy gates).
- `dcat:keyword` (at least 1)
- `dcat:distribution` (at least 1)

### 3) Evidence-triplet linkage (non-negotiable in KFM)
To satisfy **evidence-first publishing**, a DCAT Dataset record **MUST** include distributions that point to:

- 🛰️ **STAC Collection/Item** for spatial + temporal detail
- 🧬 **PROV (JSON-LD)** for lineage

> **Practical rule:**  
> **No “mystery layers”** — if a dataset is in graph/UI, the DCAT must link to STAC + PROV.

### 4) Governance, sensitivity, and CARE/FAIR controls
KFM strongly encourages (and may require via policy gates) adding:

- `kfm:classification`: `public | restricted | sensitive | internal`
- `kfm:sensitivity`: structured object (see suggested shape below)
- `dct:accessRights`: human-readable access statement
- `kfm:care_label`: e.g., `culturally_sensitive` (when applicable)
- `kfm:sovereignty`: optional governance object for community authority / restrictions

This metadata supports:
- role-based access behavior
- geo-obfuscation rules
- redaction policy
- council/oversight workflows

---

## 🔗 Cross-links KFM expects

KFM systems cross-reference metadata artifacts to remain auditable and navigable.

### Required cross-links
- DCAT → STAC (distribution)
- DCAT → PROV (distribution)

### Strongly recommended cross-links
- DCAT → **Run Manifest** (distribution or relation)
- DCAT → **Governance Card** (policy profile reference)
- DCAT → **Design Pack / domain specs** (via `dct:conformsTo`)

---

## 📦 Distributions: patterns KFM supports

A dataset typically has **multiple distributions**, not just “one file”.

### 🛰️ Pattern A — STAC pointer (required)
- `kfm:role: "stac"`
- `dcat:accessURL`: STAC collection URL (or local repo path)

### 🧬 Pattern B — PROV pointer (required)
- `kfm:role: "prov"`
- `dcat:downloadURL`: PROV JSON-LD

### 🧱 Pattern C — Direct file downloads (common)
- GeoTIFF, GeoParquet, GeoJSON, CSV, PMTiles, MBTiles, PDFs, etc.
- Include:
  - `dct:format` and/or `dcat:mediaType`
  - `kfm:checksum` (sha256 recommended)

### 🌐 Pattern D — API access (when data is query-driven)
- `dcat:accessURL`: API endpoint  
- `dct:format`: `application/json` or service descriptor
- Recommended:
  - `kfm:queryPolicy`: “rate limited”, “auth required”, etc.

### 🧊 Pattern E — OCI Artifact Distribution (big artifacts, reproducibility, supply chain)
KFM may store large artifacts (tilesets, models, packaged data) as **OCI artifacts**, signed and referenced by digest.

- `dcat:accessURL`: `oci://...@sha256:<digest>`
- `kfm:oci` object for registry metadata (repo/tag/digest/mediaType)
- Optional:
  - signature/attestation references (Cosign/Sigstore)

---

## 🧾 Suggested JSON-LD shapes

### Minimal dataset (satisfies core contract)
```json
{
  "@context": [
    {
      "dcat": "http://www.w3.org/ns/dcat#",
      "dct": "http://purl.org/dc/terms/",
      "prov": "http://www.w3.org/ns/prov#",
      "foaf": "http://xmlns.com/foaf/0.1/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "kfm": "urn:kfm:terms:"
    }
  ],
  "@id": "urn:kfm:dataset:ks.landcover.1990_2020.v1.0.0",
  "@type": "dcat:Dataset",
  "dct:identifier": "ks.landcover.1990_2020.v1.0.0",
  "dct:title": "Kansas Landcover 1990–2020",
  "dct:description": "Annual landcover rasters clipped to Kansas boundary.",
  "dct:publisher": {
    "@type": "foaf:Organization",
    "foaf:name": "Kansas GIS Dept."
  },
  "dct:license": "CC-BY-4.0",
  "dcat:keyword": ["landcover", "Kansas", "raster"],
  "kfm:classification": "public",
  "dcat:distribution": [
    {
      "@type": "dcat:Distribution",
      "dct:title": "STAC Collection",
      "dct:format": "application/json",
      "dcat:accessURL": "https://example.kfm/stac/ks.landcover.1990_2020/collection.json",
      "kfm:role": "stac"
    },
    {
      "@type": "dcat:Distribution",
      "dct:title": "PROV Bundle (JSON-LD)",
      "dct:format": "application/ld+json",
      "dcat:downloadURL": "https://example.kfm/prov/ks.landcover.1990_2020/v1/prov.jsonld",
      "kfm:role": "prov"
    }
  ]
}
```

### OCI distribution example (optional)
```json
{
  "@type": "dcat:Distribution",
  "dct:title": "Vector Tiles (PMTiles) — OCI Artifact",
  "dct:format": "application/x-pmtiles",
  "dcat:accessURL": "oci://ghcr.io/kfm/tiles/ks-landcover@sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
  "kfm:oci": {
    "repository": "ghcr.io/kfm/tiles/ks-landcover",
    "digest": "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "mediaType": "application/x-pmtiles",
    "signed": true
  }
}
```

### Suggested sensitivity object (KFM extension)
```json
{
  "kfm:sensitivity": {
    "level": "sensitive",
    "reason": "private_land",
    "handling": ["redact_exact_coordinates", "auth_required"],
    "review": { "required": true, "authority": "FAIR+CARE Council" }
  }
}
```

---

## 🧪 Validation and gates (how this stays trustworthy)

KFM treats **metadata as code** and enforces it via:

- ✅ schema validation (e.g., JSON Schema and/or SHACL)
- ✅ policy-as-code gates (OPA/Rego executed by Conftest)
- ✅ fail-closed defaults (missing required metadata blocks publishing)

### Local dev ergonomics (suggested)
- `conftest test <dcat-files> -p api/scripts/policy/`
- `jsonschema -i <record.jsonld> dcat.dataset.schema.json`

> CI must remain the source of truth. Local checks are for faster iteration.

---

## 🔁 Versioning rules

### Profile versioning
KFM metadata profiles are versioned (SemVer).  
**When this contract changes, bump the profile version** and keep backwards-compat guidance.

**Suggested bump rules:**
- **MAJOR**: required fields change or semantics break
- **MINOR**: new optional fields or stricter validation that remains compatible
- **PATCH**: documentation/typos/non-breaking constraints

### Dataset versioning
Datasets should be versioned and older versions should be **discoverable** (not silently overwritten).

Recommended DCAT properties:
- `dcat:version` (string)
- `dct:isVersionOf` (links to the “conceptual dataset”)
- `dct:replaces` / `dct:isReplacedBy` (deprecation chains)

---

## 🧠 Focus Mode + UI expectations

DCAT isn’t just “admin metadata” — it is used in user-facing behavior:

- 🗺 **UI legend + popups** can pull attribution like “Source: …” from catalog metadata.
- 🧠 **Focus Mode answers must include citations**; DCAT provides dataset-level citation anchors.
- 🧬 **Dynamic answers** still require provenance logging (PROV references to query inputs).

---

## ✅ Contract checklist (PR-ready)

- [ ] Dataset has a stable `dct:identifier`
- [ ] Dataset has `dct:title` + `dct:description`
- [ ] Dataset has `dct:license` (SPDX-style when possible)
- [ ] Dataset has at least 1 keyword
- [ ] Dataset includes `dcat:distribution[]`
- [ ] Distributions include **STAC** + **PROV** pointers
- [ ] Classification/sensitivity fields are present when needed
- [ ] No secrets or credentials in metadata (policy gate will fail)
- [ ] Record passes schema + policy gates

---

## 📚 Further reading (project docs + reference bundles)

These documents informed this contract and its governance expectations:

- 📘 **KFM Comprehensive Technical Documentation** — contract-first & provenance-first architecture
- 🏗️ **KFM Comprehensive Architecture, Features, and Design** — data layer, governance, policy gates
- 🧭 **KFM AI System Overview** — Focus Mode, explainability, citations requirements
- 🗺️ **KFM Comprehensive UI System Overview** — map legends, discovery UX, provenance visibility
- 📥 **KFM Data Intake – Technical & Design Guide** — evidence triplet, pipeline stages, validation
- 💡 **Innovative Concepts to Evolve KFM** — sovereignty, cultural protocols, ethical governance
- 🧠 **Latest Ideas & Future Proposals** — automation agents, CI/CD validation lanes, attestations
- 🧪 **Additional Project Ideas** — OCI artifacts, run manifests, policy-as-code expansion
- 🧰 **Reference bundles (PDF portfolios)**:
  - AI concepts 📦
  - Mapping/WebGL/geospatial 📦
  - Data management & Bayesian methods 📦
  - Programming language resources 📦

> If you add a new “domain” to KFM, consider producing a **Design Pack** and linking it via `dct:conformsTo`.

---


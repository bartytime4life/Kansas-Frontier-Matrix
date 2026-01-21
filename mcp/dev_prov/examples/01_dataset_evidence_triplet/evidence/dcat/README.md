# 📦 DCAT Evidence (Discovery Metadata) — `01_dataset_evidence_triplet`

![DCAT](https://img.shields.io/badge/DCAT-2.x-2ea44f)
![JSON--LD](https://img.shields.io/badge/JSON--LD-RDF-blue)
![KFM](https://img.shields.io/badge/KFM-evidence--first-purple)
![CI](https://img.shields.io/badge/policy-gates%20fail--closed-red)

> [!IMPORTANT]
> This folder is **only** the **DCAT** piece of the “evidence triplet” for this example dataset.
>
> ✅ **DCAT** = *discovery + governance metadata* (title, publisher, license, keywords, distributions)  
> ✅ **STAC** = *asset-level spatiotemporal indexing* (collections/items/files/tiles)  
> ✅ **PROV** = *lineage + reproducibility* (inputs → transforms → outputs, agents, timestamps)

---

## 🧭 Where this fits

```text
mcp/dev_prov/examples/01_dataset_evidence_triplet/evidence/
├─ stac/          🛰️ spatiotemporal + assets (Collections/Items)
├─ dcat/          📦 discovery + governance metadata (this folder)
└─ prov/          🧾 lineage bundle (how/when/who produced it)
```

In “real” KFM publishing, these same concepts land in canonical catalog locations (e.g., `data/stac/...`, `data/catalog/dcat/...`, `data/prov/...`). This example mirrors the pattern locally so you can understand/validate the **triplet contract** before wiring it into full pipelines.

---

## 🎯 What goes in `evidence/dcat/`

Place **one DCAT dataset entry** (usually JSON-LD) that:

- Makes the dataset *discoverable* 🧭
- Carries governance constraints ⚖️ (license + classification + sensitivity)
- Points users/tools to where the dataset actually lives 📍 (STAC + downloads/APIs + provenance)

Typical filenames you’ll see:
- `dataset.jsonld`
- `<dataset_id>.dcat.jsonld`
- `dcat.dataset.jsonld`

> [!TIP]
> Keep DCAT records **small, stable, and versioned**. The **big stuff** (tiles, GeoParquet, COGs, etc.) should live in STAC assets / distributions — not embedded here.

---

## ✅ Minimum DCAT checklist (KFM-aligned)

**Required (baseline):**
- [ ] **Title** + **Description**
- [ ] **Publisher / Provider**
- [ ] **License** (prefer SPDX identifiers/URLs)
- [ ] **Keywords** (+ optional themes)
- [ ] **Temporal coverage** (when the dataset applies)
- [ ] **Spatial coverage** (optional but strongly recommended for geospatial)
- [ ] **Distributions** (how to access the data)
- [ ] **Identifiers** (stable dataset id / URI)

**KFM extensions (recommended):**
- [ ] **`kfm:dataset_id`** (canonical ID shared across STAC/DCAT/PROV)
- [ ] **`kfm:classification`** (`public`, `internal`, `restricted`, …)
- [ ] **`kfm:sensitivity`** / sovereignty flags (esp. if culturally sensitive / restricted)

> [!NOTE]
> KFM treats “analysis outputs” and AI-derived layers as **first-class datasets** too — they get **their own DCAT entry**, not just a note in a report. 🧠🗺️

---

## 🔗 Cross-linking rules (don’t skip this)

DCAT is the **front door**, so it should point to:
- 🛰️ **STAC Collection URL / file** (for detailed asset/spatiotemporal metadata)
- 🧾 **PROV bundle URL / file** (for how it was produced, by whom, and from what)

This enables downstream layers (graph → API → UI → Focus Mode) to stay **traceable** and **auditable** end-to-end.

---

## 🆔 Dataset IDs & versioning

Use a canonical dataset identifier consistently across:
- DCAT record (`dct:identifier`, `@id`, or `kfm:dataset_id`)
- STAC Collection + Items (custom fields or links)
- PROV bundle (entities + activities reference the same dataset id)

A common convention in KFM docs is a **namespaced** id style like:

```text
kfm.ks.<domain>.<dataset_name>.<version>
```

Example:
```text
kfm.ks.landcover.2000_2020.v1
```

> [!IMPORTANT]
> If you bump the dataset version, **don’t overwrite history**.
> Add a new DCAT record (new id/version), keep the old record for auditability.

---

## 📦 Distribution patterns (what “access” can mean)

DCAT `dcat:distribution` can point to multiple access paths:

### 1) 🛰️ STAC-based discovery (recommended)
- Distribution points at a STAC Collection (and STAC points at the concrete assets).

### 2) 🌐 API-based access (common in KFM)
- Distribution points at an API query endpoint (e.g., table-backed access).

### 3) 📦 OCI registry artifacts (optional, advanced)
KFM proposes/uses OCI registries (ORAS + Cosign) for **content-addressed** artifacts like PMTiles / GeoParquet / COGs. If you do this:
- Record a distribution that includes the `oci://...` reference and digest pinning.
- Treat signatures/provenance as first-class attachments.

> [!TIP]
> Multiple distributions are good: “STAC catalog”, “API query”, “download”, “OCI artifact”.
> That’s not redundancy — it’s *interoperability* ✅

---

## 🧾 Minimal JSON-LD template (copy/paste + edit)

> [!NOTE]
> This is a practical **example template** for the demo. For strict production rules, align with `KFM_DCAT_PROFILE.md` (and your repo policy gates).

```json
{
  "@context": {
    "dcat": "http://www.w3.org/ns/dcat#",
    "dct": "http://purl.org/dc/terms/",
    "foaf": "http://xmlns.com/foaf/0.1/",
    "prov": "http://www.w3.org/ns/prov#",
    "vcard": "http://www.w3.org/2006/vcard/ns#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",

    "kfm": "https://kansas-frontier-matrix.org/ns/kfm#"
  },

  "@id": "urn:kfm:dataset:kfm.ks.example.dataset.v1",
  "@type": "dcat:Dataset",

  "dct:identifier": "kfm.ks.example.dataset.v1",
  "dct:title": "Example Dataset — Evidence Triplet Demo",
  "dct:description": "Demonstrates KFM evidence-first publishing: DCAT (discovery), STAC (assets), PROV (lineage).",

  "dct:publisher": {
    "@type": "foaf:Organization",
    "foaf:name": "Kansas Frontier Matrix"
  },

  "dcat:contactPoint": {
    "@type": "vcard:Kind",
    "vcard:fn": "KFM Data Team",
    "vcard:hasEmail": "mailto:data@example.org"
  },

  "dct:license": "https://spdx.org/licenses/CC-BY-4.0.html",

  "dcat:keyword": [
    "kansas",
    "evidence-first",
    "provenance",
    "example"
  ],

  "dct:temporal": {
    "@type": "dct:PeriodOfTime",
    "dcat:startDate": "2000-01-01",
    "dcat:endDate": "2020-12-31"
  },

  "dct:hasPart": [
    { "@id": "../stac/collection.json" },
    { "@id": "../prov/bundle.jsonld" }
  ],

  "dcat:distribution": [
    {
      "@type": "dcat:Distribution",
      "dct:title": "STAC Collection",
      "dcat:accessURL": { "@id": "../stac/collection.json" },
      "dct:format": "application/json",
      "dcat:mediaType": "application/json"
    },
    {
      "@type": "dcat:Distribution",
      "dct:title": "KFM API Access",
      "dcat:accessURL": { "@id": "/api/v1/query?table=example_table" },
      "dct:format": "application/json",
      "dcat:mediaType": "application/json"
    }
  ],

  "kfm:classification": "public",
  "kfm:sensitivity": "none"
}
```

---

## 🧪 Validation expectations (what should fail CI)

Expect validation to **fail closed** if:
- 🚫 license is missing/invalid
- 🚫 required fields (title/description/distribution/ids) are missing
- 🚫 STAC/DCAT/PROV “triplet completeness” is broken
- 🚫 sensitivity/classification rules are violated
- 🚫 provenance is missing where required

> [!IMPORTANT]
> If you’re using this example to build dev-provenance tooling:  
> your PROV bundle can include **pipeline run ids**, **config hashes**, and even **GitHub PR → PROV** mappings so you can answer:
> “Which code change produced this dataset, and who reviewed it?” 🧾🔍

---

## 🧠 Why DCAT matters downstream

DCAT is used to power:
- 🔎 Dataset discovery/search experiences
- 🧾 Attribution & licensing displays in the UI (e.g., “Source: …”)
- 🧬 Graph ingestion (Dataset nodes populated from DCAT properties)
- 🤖 Focus Mode evidence constraints (answers must cite sources; provenance stays attached)

---

## 🧯 Common pitfalls

- **Mixing concerns**: putting file-level asset details in DCAT instead of STAC
- **Broken linkage**: DCAT doesn’t point to STAC/PROV → downstream cannot remain traceable
- **Unstable IDs**: changing identifiers breaks lineage and graph references
- **No governance metadata**: missing license/classification/sensitivity triggers policy gates

---

## 📚 Suggested “next reads” (in-repo)

- `KFM_DCAT_PROFILE.md` (field rules + extensions)
- `KFM_STAC_PROFILE.md`
- `KFM_PROV_PROFILE.md`
- `MARKDOWN_GUIDE_v13.md` / Master Guide sections on evidence-first publishing


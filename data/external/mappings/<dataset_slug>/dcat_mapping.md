---
title: "DCAT Mapping — <dataset_slug>"
path: "data/external/mappings/<dataset_slug>/dcat_mapping.md"
version: "v0.1.0"
last_updated: "2026-01-29"
status: "draft"
doc_kind: "Mapping (DCAT)"
license: "CC-BY-4.0"

# Protocol / profiles (repo-governed)
markdown_protocol_version: "1.0"
dcat_profile_version: "KFM v11"

# Dataset identity
domain: "external"
dataset_slug: "<dataset_slug>"

# Governance / ethics
governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"          # public | internal | restricted | sensitive
classification: "open"         # open | controlled | confidential
jurisdiction: "US"

# Traceability (fill at release)
doc_uuid: "urn:kfm:doc:mapping:dcat:<dataset_slug>:v0.1.0"
commit_sha: "<commit-hash>"
doc_integrity_checksum: "sha256:<to-be-filled>"
---

![DCAT](https://img.shields.io/badge/DCAT-2.x-blue)
![KFM Profile](https://img.shields.io/badge/KFM%20DCAT%20Profile-v11-purple)
![Status](https://img.shields.io/badge/status-draft-yellow)
![Domain](https://img.shields.io/badge/domain-external-555)

# 🗺️ DCAT Mapping — `<dataset_slug>`

> 🧠 **What this is:** A governed mapping contract that explains *exactly* how we populate the DCAT record for this dataset (and how it cross-links to STAC + PROV).  
> ✅ **What this enables:** Repeatable catalog generation, schema validation in CI, and consistent discoverability.

---

## 📘 Overview

### Purpose
Define a **deterministic** and **auditable** mapping from:
- upstream/source metadata ➜ **DCAT Dataset** fields
- KFM artifacts (STAC + PROV + processed files) ➜ **DCAT distributions & lineage links**

### Scope
| ✅ In Scope | ❌ Out of Scope |
|---|---|
| Field-by-field DCAT mapping | The ETL logic itself (handled by pipelines) |
| Distribution strategy (STAC / files / APIs) | UI/Frontend presentation rules |
| Versioning & linkage expectations | Graph modeling details beyond “link targets” |
| Governance & sensitivity flags (public/restricted) | Legal review of upstream license text |

### Audience
- **Primary:** Data engineers & pipeline authors 🛠️
- **Secondary:** Domain stewards, governance reviewers ⚖️, catalog consumers 🔎

### Definitions
- **DCAT**: Data Catalog Vocabulary (RDF) used to publish dataset metadata.
- **Dataset**: A conceptual data product (may have multiple files/distributions).
- **Distribution**: A specific access mechanism or downloadable artifact for a dataset.
- **STAC**: SpatioTemporal Asset Catalog (Collections/Items) for geospatial assets.
- **PROV**: Provenance records describing how a dataset was generated/processed.
- **KFM Profile**: Project-specific constraints/extensions over base standards.

### Key Artifacts
| Artifact | Path (expected) | Notes |
|---|---|---|
| 🧾 This mapping doc | `data/external/mappings/<dataset_slug>/dcat_mapping.md` | Source-of-truth for DCAT field decisions |
| 🗂️ DCAT output (JSON-LD or TTL) | `data/catalog/dcat/<dataset_slug>.{jsonld,ttl}` | Must validate against KFM DCAT schema |
| 🛰️ STAC Collection | `data/catalog/stac/<dataset_slug>/collection.json` | Prefer using as primary spatial/temporal index |
| 🧬 PROV bundle (JSON-LD) | `data/prov/<dataset_slug>.prov.jsonld` | Required lineage + reproducibility |
| ✅ DCAT schema | `schemas/dcat/` | CI validates output |
| 📌 Source registry (if used) | `data/sources/<dataset_slug>.json` | Upstream landing page/license/attribution |

### Definition of Done ✅
- [ ] Front-matter complete & valid
- [ ] Every **required** DCAT field mapped (no “mystery blanks”)
- [ ] Distributions listed + file/API targets exist (or are scheduled in pipeline)
- [ ] STAC + PROV links included (and resolvable)
- [ ] Sensitivity/classification consistent with upstream + pipeline outputs
- [ ] DCAT output validates against `schemas/dcat/*`
- [ ] No broken internal links (if present) + no secrets/PII/sensitive coords leaked

---

## 🗂️ Directory Layout

### This document (context)
```text
data/
└── 📁 external/
    └── 📁 mappings/
        └── 📁 <dataset_slug>/
            └── 📄 dcat_mapping.md   👈 you are here
```

### Related repository paths
| Area | Path | Why it matters |
|---|---|---|
| 📚 Standards | `docs/standards/KFM_DCAT_PROFILE.md` | Field requirements, cardinality rules, extensions |
| 🛰️ Standards | `docs/standards/KFM_STAC_PROFILE.md` | Ensures spatial/temporal consistency + linking |
| 🧬 Standards | `docs/standards/KFM_PROV_PROFILE.md` | Lineage rules + agents/activities |
| 🗃️ Catalog roots | `data/catalog/dcat/` | Canonical DCAT outputs live here |
| 🗃️ Catalog roots | `data/catalog/stac/` | Canonical STAC outputs live here |
| 🧾 Provenance root | `data/prov/` | Canonical PROV outputs live here |
| 🧪 Schemas | `schemas/dcat/` | CI validation source-of-truth |

---

## 🧾 DCAT Mapping Contract

### Mapping inputs (what we read)
Fill these in for `<dataset_slug>` (as applicable):

- **Upstream landing page:** `<url>`
- **Upstream metadata format:** `<html | json | xml | pdf | api>`
- **Upstream license identifier + URL:** `<e.g., CC-BY-4.0 + link>`
- **Source registry file (optional):** `data/sources/<dataset_slug>.json`
- **Processed output artifacts:** `<list key outputs produced by pipelines>`
- **STAC collection path:** `data/catalog/stac/<dataset_slug>/collection.json`
- **PROV bundle path:** `data/prov/<dataset_slug>.prov.jsonld`

### Output targets (what we generate)
- **DCAT dataset record (canonical):** `data/catalog/dcat/<dataset_slug>.jsonld` *(preferred)*  
  - Optional parallel serialization: `data/catalog/dcat/<dataset_slug>.ttl`

---

## 🧱 Required DCAT Fields (Minimum Contract)

> ⚠️ **Minimum required** fields here should match `docs/standards/KFM_DCAT_PROFILE.md`.  
> This section is the “human contract”; the next section provides a “machine mapping”.

### 1) Core identity & description
| DCAT / DCTERMS field | Req | Source | Transform | Notes |
|---|:---:|---|---|---|
| `dct:identifier` | ✅ | `<dataset_slug>` | `slug_to_identifier()` | Stable across versions |
| `dct:title` | ✅ | `<source.title>` | `trim()` | Human-readable name |
| `dct:description` | ✅ | `<source.abstract>` | `md_to_text()` | Include methodology summary if needed |
| `dcat:keyword` | ✅ | `<source.keywords>` | `split_dedupe()` | Keep discoverability high |
| `dcat:theme` | ◻️ | `<kfm.theme>` | `map_to_vocab()` | Use controlled vocab if available |
| `dct:language` | ◻️ | `<source.language>` | `iso_639_1()` | Default `en` if unspecified |
| `dct:publisher` | ✅ | `<source.publisher>` | `normalize_org()` | Could be KFM or upstream org (be explicit) |
| `dct:creator` | ◻️ | `<source.creator>` | `normalize_agent()` | If distinct from publisher |
| `dct:license` | ✅ | `<source.license_url>` | `as_uri()` | Must be resolvable |
| `dct:rights` | ◻️ | `<source.rights>` | `normalize_text()` | Use if license is not enough |
| `dct:accessRights` | ◻️ | `<classification>` | `map_access_rights()` | Reflect governance constraints |

### 2) Temporal & spatial coverage
| DCAT / DCTERMS field | Req | Source | Transform | Notes |
|---|:---:|---|---|---|
| `dct:spatial` | ◻️ | `<kfm.spatial>` or STAC bbox | `bbox_to_location()` | Prefer STAC-derived bbox unless sensitive |
| `dct:temporal` | ◻️ | `<kfm.temporal>` or STAC dates | `to_period()` | Prefer STAC-derived interval |
| `dct:issued` | ◻️ | `<first_publish_date>` | `date_iso8601()` | First time we published this dataset in KFM |
| `dct:modified` | ✅ | `<last_pipeline_run>` | `date_iso8601()` | Update on each metadata-relevant change |
| `dct:accrualPeriodicity` | ◻️ | `<source.update_frequency>` | `map_to_dct_frequency()` | e.g., annual / monthly / irregular |
| `dct:provenance` | ✅ | PROV link | `link_to_prov()` | Human-friendly provenance statement + link |

### 3) Contact & landing page
| DCAT / DCTERMS field | Req | Source | Transform | Notes |
|---|:---:|---|---|---|
| `dcat:landingPage` | ✅ | `<upstream_landing_page>` | `as_uri()` | If KFM has a landing page, include *both* (see notes) |
| `dcat:contactPoint` | ◻️ | `<kfm.contact>` | `to_vcard()` | Recommended for usability |
| `foaf:page` | ◻️ | `<docs page>` | `as_uri()` | Optional documentation page |

---

## 📦 Distributions (DCAT `dcat:distribution`)

> 💡 We treat **STAC** as a *first-class* distribution for geospatial discoverability, and optionally include direct file downloads + API endpoints.

### Distribution inventory (fill this table)
| Dist ID | Type | `dcat:accessURL` | `dcat:downloadURL` | `dct:format` / `dct:mediaType` | Notes |
|---|---|---|---|---|---|
| `<dataset_slug>:stac` | STAC Collection | `data/catalog/stac/<dataset_slug>/collection.json` | — | `JSON / application/json` | Primary geospatial index |
| `<dataset_slug>:prov` | PROV bundle | `data/prov/<dataset_slug>.prov.jsonld` | — | `JSON-LD / application/ld+json` | Lineage + reproducibility |
| `<dataset_slug>:export:<fmt>` | File export | `<path or URL>` | `<path or URL>` | `<GeoJSON|Parquet|CSV|COG>` | Add one per user-facing artifact |
| `<dataset_slug>:api` | API | `<api endpoint>` | — | `JSON / application/json` | Only if stable + documented |

### Distribution rules ✅
- Every distribution must declare:
  - access mechanism (`accessURL` and/or `downloadURL`)
  - a format/media type
  - a short description (recommended)
  - size/checksum when available (recommended for reproducibility)

---

## 🔗 Cross-layer linkage expectations (STAC ⇄ DCAT ⇄ PROV)

### DCAT ➜ must link outward
- Include at least one distribution that points to:
  - 🛰️ STAC Collection (or static STAC endpoint)
  - 🧬 PROV record for lineage

### STAC / PROV ➜ should link back
- STAC Collection/Items should include a backlink to DCAT dataset identifier (project convention).
- PROV should reference the DCAT dataset identifier via the generated entity/derivation relationship (project convention).

> ✅ If any of these links are missing, CI/graph integrity checks may fail in later stages.

---

## 🧬 Versioning & lineage expectations

### Dataset versioning (recommended)
- Use semantic-ish dataset versions where meaningful (e.g., `vYYYY.MM.DD` or `vMAJOR.MINOR.PATCH`).
- When a new version is created:
  - Update `dct:modified`
  - Add lineage linkage:
    - DCAT: update `dct:provenance` statement
    - PROV: include `prov:wasRevisionOf` to previous version entity
- If the schema/meaning changes materially, treat as a **new dataset version** and maintain backward pointers.

---

## 🧷 Machine-readable mapping (optional, for automation)

> If your DCAT generator supports it, keep this YAML block aligned with the tables above.

```yaml
dcat:
  dataset:
    id: "urn:kfm:dataset:<dataset_slug>"
    identifier: "<dataset_slug>"
    title:
      from: "source.title"
      transform: ["trim"]
    description:
      from: "source.description"
      transform: ["normalize_whitespace"]
    keywords:
      from: "source.keywords"
      transform: ["split", "lower", "dedupe", "sort"]
    landing_page:
      from: "source.landing_page"
    license:
      from: "source.license_url"
    publisher:
      from: "source.publisher"
    issued:
      from: "kfm.issued"
    modified:
      from: "kfm.modified"
    spatial:
      from: "stac.collection.bbox"
      transform: ["bbox_to_location"]
      policy:
        if_sensitive: "generalize_to_admin_area"
    temporal:
      from: "stac.collection.datetime_range"
      transform: ["to_period"]
    provenance:
      link: "data/prov/<dataset_slug>.prov.jsonld"
  distributions:
    - id: "urn:kfm:distribution:<dataset_slug>:stac"
      access_url: "data/catalog/stac/<dataset_slug>/collection.json"
      media_type: "application/json"
      format: "STAC"
    - id: "urn:kfm:distribution:<dataset_slug>:prov"
      access_url: "data/prov/<dataset_slug>.prov.jsonld"
      media_type: "application/ld+json"
      format: "PROV"
    # Add additional downloadable artifacts here
```

---

## 🧪 Validation Checklist (CI-aligned)

> Copy/paste as a PR checklist or local preflight.

- [ ] DCAT output exists: `data/catalog/dcat/<dataset_slug>.{jsonld,ttl}`
- [ ] DCAT validates against `schemas/dcat/*`
- [ ] All referenced distributions resolve (paths/URLs)
- [ ] STAC Collection exists + validates against `schemas/stac/*`
- [ ] PROV bundle exists + validates against `schemas/prov/*`
- [ ] No broken internal links in this doc (if you added any)
- [ ] Classification/sensitivity consistent end-to-end (raw ➜ processed ➜ catalog)
- [ ] Sensitive coordinates not present in public DCAT/STAC outputs (if `sensitivity != public`)

---

## ⚖ Governance & Sensitivity (FAIR+CARE)

### Data sensitivity rules
- If `sensitivity` or `classification` is not public/open:
  - Use generalized spatial coverage (e.g., state/county bbox) instead of exact coords.
  - Ensure distributions do **not** expose restricted files or endpoints.
  - Prefer gated API access rather than direct download URLs.

### Attribution & community respect
- Always preserve upstream attribution requirements in `dct:description` or `dct:provenance`.
- If data relates to culturally sensitive locations or community knowledge:
  - Set `care_label` accordingly and route through governance review.

---

## 🕰️ Version History
| Version | Date | Summary | Author |
|---|---:|---|---|
| v0.1.0 | 2026-01-29 | Initial DCAT mapping scaffold for `<dataset_slug>` | `<you>` |


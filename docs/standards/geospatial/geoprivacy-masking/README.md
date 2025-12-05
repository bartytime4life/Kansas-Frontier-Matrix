---
title: "🛡️ KFM v11.2.4 — Geospatial Privacy & Cultural-Safety Masking Standards (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/geospatial/geoprivacy-masking/README.md"
version: "v11.2.4"
last_updated: "2025-12-05"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council · Tribal Sovereignty Board"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x privacy-contract compatible"
status: "Active / Enforced"

doc_kind: "Standard"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "geospatial-privacy"
  applies_to:
    - "ingest"
    - "etl"
    - "analysis"
    - "stac"
    - "dcat"
    - "graph"
    - "api"
    - "frontend"
    - "story-nodes"
    - "focus-mode"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
classification: "Public"
indigenous_rights_flag: true

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.4/privacy-masking-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/geoprivacy/v1.json"
governance_ref: "../../governance/ROOT-GOVERNANCE.md"

doc_uuid: "urn:kfm:doc:standards:geoprivacy-masking-v11.2.4"
semantic_document_id: "kfm-doc-geoprivacy-masking-v11.2.4"
event_source_id: "ledger:kfm:doc:standards:geoprivacy"

license: "Apache-2.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
---

<div align="center">

# 🛡️ KFM Geospatial Privacy & Cultural-Safety Masking Standard  
v11.2.4 · Deterministic · STAC/DCAT/PROV-Aligned · Sovereignty-Protected  

`docs/standards/geospatial/geoprivacy-masking/README.md`

**Purpose:**  
Define the only approved geospatial masking methods permitted in KFM ingest, ETL, analysis, graph, API, and frontend layers to protect Indigenous cultural sites, landowner privacy, and sovereignty-aligned datasets while preserving deterministic, catalog-ready, provenance-rich spatial behavior.

</div>

---

## 📘 Overview

### 🎯 Goals of this standard

The Kansas Frontier Matrix (KFM) exposes thousands of Kansas-linked spatial datasets — archaeology, soils, geomorphology, hydrology, climate, historical infrastructure, cultural landscapes. Many contain points that, if published directly, would violate:

- Cultural-sensitivity rules and Indigenous sovereignty obligations.  
- Landowner privacy and parcel-level confidentiality.  
- Ethical expectations on archaeological and sacred-site protection.  

This standard defines **the only approved masking methods** allowed anywhere in KFM:

1. Protect Indigenous cultural sites from exposure, scraping, or triangulation.  
2. Provide deterministic anonymization that remains stable across reprocessing runs.  
3. Guarantee privacy-preserving resolution for all Story Nodes, MapLibre/Cesium layers, and API endpoints.  
4. Prevent coordinate rounding attacks, reverse inference, spatial cross-correlation, and high-zoom deanonymization.  
5. Require complete PROV-O lineage and telemetry for every masking decision.  

All other masking approaches are either deprecated or forbidden.

---

## 🧭 Context

KFM’s operational pipeline is:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j knowledge graph → API layer → React/MapLibre/Cesium frontend → Story Nodes → Focus Mode.

Within this stack:

- **Ingest & ETL** are responsible for applying masking **before** any tiling, indexing, or analysis that might leave the constrained environment.  
- **STAC/DCAT catalogs** must carry explicit masking metadata so downstream consumers see both the method and its parameters.  
- **Neo4j** holds only masked geometries, never raw coordinates, along with sensitivity labels and masking provenance.  
- **API** surfaces masked coordinates, sensitivity labels, and masking metadata, enforcing zoom and access controls.  
- **Frontend (MapLibre/Cesium, Story Nodes, Focus Mode)** renders only masked or generalized geometry, never raw coordinates, and must obey sensitivity- and sovereignty-driven rendering rules.  

This standard is tightly coupled to:

- The **Geoethical Reflection Layer** (`kfm_geoethics`) for Story Nodes.  
- The **Data Access Labels Standard** for “Open / Restricted / Tribal-only / Withheld” labels.  
- KFM’s PROV and OpenLineage-based **lineage and audit** framework.

---

## 🧱 Architecture

### 1. Required method: deterministic donut geomasking

KFM enforces the **Deterministic Donut Geomasking Method** as the universal masking protocol for point-based geoprivacy.

**Given:**

- Original point: `lat`, `lon` (kept only in vault / high-security store).  
- Sensitivity label: `public | community | sensitive | sacred`.  
- Absolute ID: `record_id` (stable, opaque identifier).  
- Global secret salt: stored only in sealed vault path.  

**Steps:**

1. `seed = HMAC_SHA256(secret_salt, record_id)`  
2. Draw random bearing `θ ∼ U(0, 2π)` from a seeded RNG.  
3. Draw random radius `r ∼ U(r_min, r_max)` from sensitivity table (below).  
4. Offset geodesically on ellipsoid (`lat2, lon2 = geodesic_offset(lat, lon, θ, r)`).  
5. Validate location stays within approved spatial domain.  
6. If invalid → redraw radius (up to 5 tries), otherwise fail the record and emit an error event.  

**Determinism:** because the seed depends only on `record_id` and the global `secret_salt`, the same input always yields the same masked output, across ETL runs and environments.

### 2. Sensitivity → radius table

The masking radius is driven by a sensitivity label:

| label      | r_min | r_max | purpose                                  |
|------------|-------|-------|------------------------------------------|
| public     | 50m   | 150m  | low-risk POI generalization             |
| community  | 250m  | 500m  | rural privacy protection                |
| sensitive  | 1km   | 3km   | archaeological masking                  |
| sacred     | 3km   | 10km  | CARE-principle maximum protection       |

Additional rule:

- For **`sacred`** labels, masking **must also** impose multi-level H3 generalization (R8+), so no point-like representation is exposed at any interactive zoom level.

### 3. Deprecated & forbidden techniques

The following **must not** appear anywhere within the KFM pipeline (ingest, notebooks, ad-hoc scripts, or UIs):

#### 3.1 Naïve decimal rounding

- **Forbidden:** rounding lat/lon to N decimal places.  
- **Reason:** inconsistent spatial precision across latitudes and trivial reversal via intersection with parcel boundaries or other layers.

#### 3.2 Additive noise without bounded annulus

- **Forbidden:** simple Gaussian/Uniform jitter without strict inner/outer radius bounds.  
- **Reason:** too many points remain close to originals or drift unrealistically far, enabling reverse inference and outlier spotting.

#### 3.3 Constant-vector shifts

- **Forbidden:** “shift all points by a constant vector.”  
- **Reason:** instantly reversible when any original location is known or guessed.

Any discovery of these patterns in code or derived datasets is a **governance violation** and must trigger an incident review.

### 4. Integration with KFM systems

- **Deterministic ETL nodes**
  - Masking occurs **before**:
    - Tile generation.
    - H3 indexing.
    - Stratigraphic or hydrological linking.
  - Masked geometries are the **only** ones allowed outside vault contexts (e.g., notebooks, Story Nodes, embeddings).

- **Neo4j knowledge graph**
  - Raw coordinates **never** enter Neo4j.  
  - Graph stores:
    - Masked geometry.
    - Sensitivity label.
    - Links to masking provenance (PROV/OpenLineage).  
  - Sacred nodes require relationship-level access gating and may only be exposed as generalized H3 regions.

- **API layer**
  - APIs must:
    - Enforce zoom-dependent filtering (e.g., clamp or suppress sacred & sensitive geometries at high zoom).  
    - Ensure masked points never appear literally colocated with parcel polygons.  

- **Frontend (MapLibre/Cesium)**
  - Sacred data must degrade to H3 hex outlines or higher-level polygons, not points.  
  - Community points may appear as approximate icons with donut-masked positions baked in.  
  - Story Node & Focus Mode views must not reverse or “sharpen” masked locations.

### 5. Reference implementation sketch

```python
def geomask(lat, lon, record_id, label, salt):
    seed = hmac_sha256(salt, record_id)
    rng = Random(seed)
    r_min, r_max = RADIUS_TABLE[label]
    for _ in range(5):
        bearing = rng.uniform(0, 2*math.pi)
        r = rng.uniform(r_min, r_max)
        lat2, lon2 = geodesic_offset(lat, lon, bearing, r)
        if within_allowed_domain(lat2, lon2):
            return lat2, lon2
    raise MaskingError("Unable to generate valid geometry")
```

This reference code is **illustrative** only; production implementations must be tested, versioned, and wired into ETL with full PROV/OpenLineage recording.

---

## 📦 Data & Metadata

### 1. Required masking metadata

Every masked geometry must include the following STAC/DCAT-aligned fields (namespaced here as `kfm:*`):

```json
{
  "kfm:privacy_method": "donut_geomask_v1",
  "kfm:r_min_m": 250,
  "kfm:r_max_m": 500,
  "kfm:seed_strategy": "HMAC(record_id, secret_salt)",
  "kfm:sensitivity_label": "community",
  "kfm:masking_run_id": "urn:kfm:etl-run:2025-12-05T00:00Z",
  "kfm:prov_ref": "prov/<record-id>.jsonld"
}
```

These fields must be:

- Present on any STAC Item or DCAT Dataset whose geometry has been masked.  
- Propagated to any derivative layers that reuse the same masked geometry (e.g., tiles, Story Nodes, embeddings).  

### 2. PROV-O lineage

Each masked geometry must be represented in PROV as:

- `prov:Entity` — the masked geometry record.  
- `prov:used` → original sensitive record (vault-only reference, not raw coordinates).  
- `prov:wasGeneratedBy` → the masking ETL job (activity UUID).  
- `prov:wasInfluencedBy` → sovereignty review tag or geoethical policy.  

The `kfm:prov_ref` field must point to a resolvable PROV document (e.g., JSON-LD) in the provenance store.

---

## 🌐 STAC, DCAT & PROV Alignment

This standard is explicitly designed to be STAC/DCAT/PROV-aligned:

- **STAC 1.x**
  - Masked Items:
    - Carry `properties["kfm:privacy_method"]`, `kfm:sensitivity_label`, and radius fields.  
    - May store access labels and sovereignty info in `properties["kfm:access_label"]` and related geoethical fields.  
  - Collections summarizing sensitive assets must indicate the presence of masked geometries and their minimum radii.

- **DCAT 2.0/3.0**
  - Masked datasets:
    - Map sensitivity and access labels into `dct:accessRights`, `dct:rights`, and/or related properties.  
    - Link to geoethical policies via qualified relations referencing `kfm_geoethics` or equivalent policy docs.  
    - Reference masking activities and PROV bundles through `dct:provenance` and custom properties.

- **PROV-O**
  - Masking jobs are `prov:Activity` instances:
    - `prov:used` original coordinates (vault-only entity).  
    - `prov:generated` masked geometries exposed to downstream systems.  
    - `prov:wasAssociatedWith` ETL pipelines or services.  
  - Sovereignty and review context can appear as `prov:Agent` / `prov:Entity` records, linked via `prov:wasInfluencedBy`.

Implementations should favor existing vocabularies and KFM profiles (KFM-STAC, KFM-DCAT, KFM-PROV) over ad-hoc keys wherever possible.

---

## 🧪 Validation & CI/CD

All ingestion pipelines touching `Point`, `LineString`, or `Polygon` geometries must include automated tests that verify masking compliance.

### 1. Distance validation

- Assert that the distance between original and masked centroids is:
  - `>= r_min` and `<= r_max` for the assigned sensitivity label.  
- Tests must run on:
  - Sample fixtures.
  - Synthetic edge cases (boundary conditions, near edges of allowed domains).

### 2. Deterministic stability

- Same `(record_id, label, salt)` input must always produce the **same** masked location.  
- CI should:
  - Re-run masking on a fixture set.
  - Compare against golden masked outputs.

### 3. Anti-triangulation tests

- Combinations of masked layers must not:
  - Collapse into identical geometries at high zoom.
  - Recreate raw site positions via intersections of multiple masked datasets.  
- Tests include:
  - Checking for repeated geometries after masking across multiple layers.
  - Evaluating high-zoom visual clustering patterns.

### 4. Sovereignty compliance tests

- Datasets labeled `sacred` must:
  - Require explicit tribal review flags before ingestion or publication.  
  - Never expose point-level geometries in API/tiles/frontend.  
- CI should:
  - Fail ingestion if required flags or governance approvals are missing.  
  - Verify that `sacred` datasets are rendered only as generalized regions or H3 cells.

### 5. Workflow integration

- `.github/workflows/kfm-ci.yml` (or equivalent) must run:
  - Masking unit tests.
  - Schema validation for geoprivacy-related metadata.
  - Provenance checks to ensure `kfm:prov_ref` references exist for masked entities.

---

## 🗂️ Directory Layout

```text
📂 docs/standards/geospatial/
└── 📂 geoprivacy-masking/
    ├── 📄 README.md                         # 🛡️ Geoprivacy & masking standard (this file)
    ├── 📂 examples/
    │   └── 📄 validation-tests.md           # 🧪 Example test cases & patterns
    └── 📂 schemas/
        └── 📄 geoprivacy-masking-v1.json    # 📦 JSON Schema for masking metadata blocks
```

Author rules:

- Any new schema or example file under this directory must be documented here or in `validation-tests.md`.  
- The schema file must remain in sync with this standard’s required fields and terminology.

---

## ⚖ FAIR+CARE & Governance

This standard is a core enforcement tool for FAIR+CARE and Indigenous data sovereignty in KFM:

- **FAIR**
  - *Findable*: masking metadata (`kfm:privacy_method`, `kfm:sensitivity_label`, etc.) is searchable via STAC/DCAT and graph queries.  
  - *Accessible*: masking policies and parameters are visible in catalogs and, where appropriate, surfaced in UI tooltips/legends.  
  - *Interoperable*: masking semantics are aligned with STAC/DCAT/PROV and KFM’s internal geospatial ontologies.  
  - *Reusable*: clear licensing, versioning, and provenance make masked datasets reusable without re-identification risk.

- **CARE & sovereignty**
  - *Collective benefit*: donut masking with tiered radii prevents dataset misuse while preserving scientific and educational value.  
  - *Authority to control*: sensitivity labels and sovereignty review tags reflect Tribal/community governance decisions.  
  - *Responsibility*: explicit `sensitivity_label`, `kfm_geoethics` integration, and sovereignty tests hold KFM operators accountable.  
  - *Ethics*: forbidden techniques and strict CI checks prevent casual or legacy privacy shortcuts.

Governance hooks:

- This document is subordinate to:
  - KFM Governance Framework.  
  - Sovereignty and Indigenous Data Protection policies.  
  - Geoethical Reflection Layer standard for Story Nodes.  
- Any exception to these masking rules requires:
  - Formal review by FAIR+CARE Council.  
  - Approval by Tribal Sovereignty Board where applicable.  
  - Documentation of the exception and its rationale.

---

## 📚 Reference Standards & Resources (Footer)

- [FAIR Principles](https://www.go-fair.org/fair-principles/)  
- [CARE Principles for Indigenous Data Governance](https://www.gida-global.org/care)  
- [CIDOC-CRM](https://www.cidoc-crm.org/) · [PROV-O](https://www.w3.org/TR/prov-o/) · [GeoSPARQL](https://www.ogc.org/standard/geosparql/)  
- [Data Access Labels Standard](../../governance/data-access-labels/README.md)  
- [KFM Governance Framework](../../governance/ROOT-GOVERNANCE.md)  
- [KFM Markdown Authoring Protocol — KFM-MDP v11.2.4](../kfm_markdown_protocol_v11.2.4.md)  
- [Geoethical Reflection Layer for Story Nodes](../../../frontend/story-nodes/geoethical-reflection/README.md)  

Use these references when designing or reviewing any masking-related code, ETL logic, or UI rendering.

---

## 🕰️ Version History

| Version | Date       | Status            | Notes                                                                                      |
|--------:|------------|-------------------|--------------------------------------------------------------------------------------------|
| v11.2.4 | 2025-12-05 | Active / Enforced | Initial KFM-MDP v11.2.4–aligned release; standardizes deterministic donut masking & metadata. |

Future revisions must:

- Preserve or document breaking changes to masking parameters or sensitivity labels.  
- Update STAC/DCAT/PROV mappings and schemas in lockstep with this document.  
- Extend tests and telemetry requirements to cover any new geomasking modes (e.g., polygons, corridors).  

---

<div align="center">

🛡️ **KFM v11.2.4 — Geoprivacy & Cultural-Safety Masking Standard**  
Scientific Insight · FAIR+CARE Ethics · Sovereignty-First  

[📘 Docs Root](../../../..) · [📂 Standards Index](../../README.md) · [⚖ Governance](../../governance/ROOT-GOVERNANCE.md)

</div>
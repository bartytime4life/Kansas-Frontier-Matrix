<!--
doc_id: KFM-ANALYSIS-READINESS-TILE-V1
title: Daily Readiness Tile Specification (NDVI + Air Quality)
type: standard
version: v1
status: draft
owners: [@bartytime4life]  <!-- NEEDS VERIFICATION -->
created: 2026-04-02
updated: 2026-04-02
policy_label: public  <!-- NEEDS VERIFICATION -->
related: [
  docs/governance/ROOT_GOVERNANCE.md,
  docs/domains/air/README.md,
  docs/analyses/remote-sensing/README.md
]
tags: [kfm, readiness, ndvi, smoke, qa, provenance]
notes: [
  First formalization of readiness tile pattern,
  Thresholds configurable per domain,
  Requires run_receipt signing infrastructure
]
-->

# 🧭 Daily Readiness Tile Specification  
**Purpose:** Define a governed, evidence-first mechanism to determine whether NDVI deltas (or similar outputs) may be safely emitted.

---

## 🔎 Scope

### ✔ Includes
- Pixel-level readiness evaluation
- Smoke / cloud / QC integration
- Emission gating logic
- Provenance enforcement (run_receipt requirement)
- Admin-level aggregation (county/state)

### ✖ Excludes
- NDVI computation itself  
- Upstream ingestion pipelines  
- Visualization UI (handled by Focus surfaces)

---

## 🧩 Repo Fit

| Layer | Role |
|------|------|
| `RAW` | Source ingestion (ABI, HMS, MAIAC, HRRR) |
| `WORK` | Intermediate QC + masking |
| `PROCESSED` | Readiness tile generation |
| `CATALOG` | Evidence linking + metadata |
| `PUBLISHED` | COG + JSON release |

---

## 📥 Accepted Inputs

| Source | Type | Role |
|-------|------|------|
| ABI L2 CMIP | Satellite | Cloud + radiance |
| HMS Smoke | Polygon | Smoke classification |
| MAIAC AOD | Raster | Aerosol density |
| HRRR Smoke | Forecast | Near-term plume prediction |

---

## 🚫 Exclusions

- Unsigned or unverifiable inputs  
- Inputs lacking QC flags  
- Derived layers without provenance chain  

---

# 🧱 Core Artifact Structure

## 1. Cloud-Optimized GeoTIFF (COG)

### Bands

| Band | Type | Description |
|-----|------|-------------|
| `mask_health` | float32 | 0–1 confidence score |
| `readiness_flag` | uint8 | 0 = not ready, 1 = ready |
| `qc_reason_codes` | uint16 | Bitmask of failure reasons |

---

### QC Reason Bitmask

| Bit | Code | Meaning |
|----|------|--------|
| 0 | CLOUD | Cloud contamination |
| 1 | THIN_CIRRUS | Partial obstruction |
| 2 | HEAVY_SMOKE | HMS heavy overlap |
| 3 | LOW_SOLAR | Poor illumination |
| 4 | ABI_QC_FAIL | Sensor quality failure |
| 5 | AOD_MISSING | Missing aerosol data |
| 6 | FORECAST_SMOKE | HRRR predicted plume |

---

### Metadata (COG tags)

```json
{
  "contributing_sources": [
    {
      "name": "ABI-L2-CMIP",
      "spec_hash": "sha256:...",
      "evidence_ref": "run_receipt://abi/..."
    }
  ]
}
```

---

## 2. JSON Sidecar

### Required Fields

```json
{
  "run_id": "YYYY-MM-DD_region_vX",
  "product": "ndvi_delta",
  "spec_version": "1.0.0",
  "region": "US-KS"
}
```

---

### Summary Metrics

| Field | Description |
|------|------------|
| `readiness_score` | Mean mask_health |
| `fraction_ready` | Area passing threshold |
| `level` | Quality classification |
| `primary_blocker` | Dominant failure cause |

---

### Admin Aggregation

```json
"percent_coverage_by_admin": {
  "state": {"US-KS": 0.74},
  "county": {"20091": 0.88}
}
```

---

### Provenance Block

```json
"inputs": [
  {
    "source": "HMS-Smoke",
    "spec_hash": "sha256:...",
    "evidence_ref": "run_receipt://hms/..."
  }
]
```

---

### Emit Decision

```json
"emit_decision": {
  "allowed": true,
  "reasons": []
}
```

---

# 🧪 Quality Ladder

| Level | Range | Meaning |
|------|------|--------|
| 0 | < 0.30 | FAIL |
| 1 | 0.30–0.60 | SUSPECT |
| 2 | 0.60–0.80 | ACCEPTABLE |
| 3 | ≥ 0.80 | HIGH |

---

# 🚦 Emission Gate (Fail-Closed)

Emission is **allowed ONLY IF**:

### 1. Coverage Requirement
- `mask_health ≥ 0.75`
- ≥ 70% of region area

### 2. Smoke Constraint
- No HMS **heavy smoke** in AOIs

### 3. Provenance Requirement
- All inputs have **signed run_receipts**

---

### If ANY condition fails:
```text
→ emit_decision.allowed = false
```

---

# 🧠 Scoring Model (Reference Implementation)

```python
candidate = abi.clear_sky & abi.qc_good

mask_health = 1.0
mask_health -= 0.4 * cloud_thin_prob
mask_health -= 0.3 * aod_risk
mask_health -= 0.2 * hrrr_heavy_prob
mask_health = clip(mask_health, 0, 1)

readiness_flag = (
    (mask_health >= 0.75) &
    candidate &
    ~hms.heavy_aoi
)

area_fraction_ready = area(readiness_flag)/area(region)
readiness_score = mean(mask_health[candidate])
```

---

# 🔐 Governance Alignment

## Truth Path Compliance
✔ RAW → WORK → PROCESSED → CATALOG → PUBLISHED enforced

## Evidence Rule
✔ Every input must resolve to:
```
EvidenceRef → EvidenceBundle
```

## Runtime Outcomes
- ANSWER → emit allowed  
- ABSTAIN → insufficient data  
- DENY → policy violation  
- ERROR → system failure  

---

# ⚠️ Risk Handling

| Condition | Action |
|----------|--------|
| Missing AOD under clouds | Lower mask_health |
| Forecast plume incoming | Penalize readiness |
| QC ambiguity | Add reason code |
| Missing evidence | HARD FAIL |

---

# 🧭 Operational Notes

- COG must include internal tiling + overviews  
- JSON must remain <50 KB  
- All thresholds must be configurable per region  
- Default mode: **fail closed**

---

# ✅ CI / Definition of Done

- [ ] All inputs signed and verified  
- [ ] COG passes schema validation  
- [ ] JSON sidecar passes schema validation  
- [ ] Readiness thresholds applied  
- [ ] Admin aggregation computed  
- [ ] Emit decision recorded  
- [ ] EvidenceRefs resolvable  

---

# 📎 Future Extensions (PROPOSED)

- Temporal stability scoring  
- Cross-day anomaly detection  
- Multi-product readiness fusion  
- AOI-specific threshold overrides  

---

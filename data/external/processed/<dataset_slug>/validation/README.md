# 🔍 Validation — `<dataset_slug>` (External · Processed)

![Stage](https://img.shields.io/badge/stage-processed-blue?style=flat-square)
![Domain](https://img.shields.io/badge/domain-external-0aa?style=flat-square)
![Validation](https://img.shields.io/badge/validation-required-brightgreen?style=flat-square)
![Catalogs](https://img.shields.io/badge/catalogs-STAC%20%7C%20DCAT%20%7C%20PROV-7b2cbf?style=flat-square)
![Governance](https://img.shields.io/badge/governance-fail--closed-red?style=flat-square)
![CI](https://img.shields.io/badge/CI-gated-critical?style=flat-square)

> 🧪 This folder is the **validation contract + evidence** for the processed dataset at:
>
> `data/external/processed/<dataset_slug>/`

---

## 🎯 Purpose

Validation is the required quality gate between **ETL outputs** and the **published boundary artifacts** (STAC/DCAT/PROV), before anything reaches the **graph**, **API**, or **UI**. In KFM, pipeline ordering is non-negotiable. [^pipeline-order]

This folder exists to make sure that:

- ✅ The processed files are structurally correct (format/schema) and semantically plausible (ranges/constraints).
- 🧾 The dataset is ready to be “published” with STAC/DCAT/PROV metadata and lineage. [^boundary-artifacts] [^catalog-paths]
- 🔐 Safety & governance rules (PII/sensitive location/classification) are respected, and **no PR merges** if they aren’t. [^ci-gates] [^security-scans]

---

## 🧭 Quick Navigation

### 📁 Data staging (domain-first)
KFM expects domain-scoped staging directories:

- **Raw (immutable):** `data/external/raw/<dataset_slug>/`
- **Work (intermediate):** `data/external/work/<dataset_slug>/`
- **Processed (this dataset):** `data/external/processed/<dataset_slug>/`  
  ↳ **Validation (you are here):** `data/external/processed/<dataset_slug>/validation/` [^domain-layout]

### 🧾 Required “boundary artifacts” for publication
At publication time, every dataset must produce:

- **STAC** (collections + items): `data/stac/collections/`, `data/stac/items/`
- **DCAT** (JSON-LD): `data/catalog/dcat/`
- **PROV** (lineage bundle): `data/prov/` [^catalog-paths]

> If your change adds/updates processed data, ensure the matching metadata + provenance entries are updated too. CI enforces this. [^ci-gates]

### 🧰 Validation tooling homes
Validation and catalog tooling should live in:

- `src/pipelines/` (canonical pipeline code)
- `tools/` (standalone validation utilities, if needed) [^validation-tools]

---

## 📁 Folder Layout

Recommended structure inside `validation/` (adjust as needed, but keep it deterministic 🔁):

```text
validation/
├── README.md                         # this file 📌
├── contract/                         # the “what must be true” definitions 📜
│   ├── dataset_contract.yml          # schema pointers, keys, CRS, constraints, etc.
│   └── checks.yml                    # enabled checks + thresholds
├── schemas/                          # dataset-specific schemas (if not in global `schemas/`) 🧩
│   └── <dataset_slug>.schema.json
├── baselines/                        # expected metrics for regression checks 📈
│   └── baseline_metrics.json
├── reports/                          # generated outputs (commit small + stable) 🧾
│   ├── latest.md
│   ├── latest.json
│   └── latest.summary.csv
├── samples/                          # small repro snippets / failing rows / invalid geoms 🧪
│   └── invalid_records.<ext>
└── logs/                             # optional; generally avoid committing large logs 🧯
```

---

## ✅ Dataset Contract

> Fill this section in. Treat it as a **contract-first** artifact: schema/contract changes trigger strict checks and should be versioned intentionally. [^contract-first]

### 🪪 Dataset identity
| Field | Value |
|---|---|
| Dataset slug | `<dataset_slug>` |
| Display name | `<Human-friendly name>` |
| Source / provider | `<e.g., USGS / NOAA / county assessor / etc.>` |
| License | `<SPDX or plain-language>` |
| Attribution | `<required attribution statement>` |
| Update cadence | `<one-time / monthly / annual / ad hoc>` |
| Intended audience | `<internal / public / research>` |
| Classification | `<public / internal / restricted / confidential>` |

> ⚠️ Classification must **never be downgraded** through processing unless an approved de-identification/redaction step is documented. [^classification]

### 📦 Assets validated (processed outputs)
List the files this validation covers.

| Path (relative) | Format | Geometry | CRS | Primary key / unique ID | Notes |
|---|---|---|---|---|---|
| `../<file>` | `<geojson/parquet/csv/tif/...>` | `<point/line/polygon/raster>` | `<EPSG:####>` | `<field>` | `<notes>` |
| `../<file>` | `<...>` | `<...>` | `<...>` | `<...>` | `<...>` |

### 🧾 Metadata + lineage links (required)
Fill with the canonical IDs/paths for this dataset’s published records.

| Artifact | Expected location | ID / filename |
|---|---|---|
| STAC Collection | `data/stac/collections/` | `<collection_id>.json` |
| STAC Item(s) | `data/stac/items/` | `<item_id>.json` |
| DCAT Dataset | `data/catalog/dcat/` | `<dataset_slug>.jsonld` |
| PROV Bundle | `data/prov/` | `<dataset_slug>.prov.json` |

> PROV should link the whole chain (raw → work → processed) and identify the producing run/config (e.g., run ID / commit hash). [^prov-end-to-end]

---

## 🧪 Checks Performed

### 🧱 Check severity (how we fail)
| Severity | Meaning | Result |
|---|---|---|
| **BLOCKER** ⛔ | Contract broken; unsafe/invalid output | Fail validation + CI |
| **WARN** ⚠️ | Suspicious but not proven wrong | Report + review |
| **INFO** 📝 | Observability metrics | Report only |

### ✅ Validation matrix (edit per dataset)
| Category | Example checks | Severity | Where results land |
|---|---|---:|---|
| Format | parses cleanly; stable encoding; no truncated rows | BLOCKER | `reports/latest.*` |
| Schema | required fields; types; enums; null policy | BLOCKER | `reports/latest.json` |
| Uniqueness | primary key unique; no duplicate features | BLOCKER | `reports/latest.summary.csv` |
| Completeness | required fields non-null above threshold | WARN/BLOCKER | `reports/latest.md` |
| Spatial validity | valid geometries; non-empty; no NaN coords | BLOCKER | `samples/invalid_*` |
| CRS sanity | CRS matches contract; axis order correct | BLOCKER | `reports/latest.md` |
| Extent sanity | bbox within expected region/area | WARN/BLOCKER | `reports/latest.md` |
| Temporal sanity | dates parse; range within expected bounds | WARN | `reports/latest.md` |
| Value ranges | numeric min/max plausible | WARN | `reports/latest.summary.csv` |
| Governance | license present; attribution present | BLOCKER | `reports/latest.md` |
| Safety | no PII; no sensitive locations leaked | BLOCKER | CI logs + `reports/latest.md` |
| Classification | no downgrades; tags propagate | BLOCKER | CI logs + `reports/latest.md` |

---

## ▶️ Running Validation Locally

> 🔁 Prefer running validation through the deterministic pipeline path (idempotent, logged) rather than ad-hoc manual edits. [^deterministic]  
> ✋ Do **not** hand-edit processed outputs to “make validation pass”; fix the pipeline and regenerate. [^no-manual-edits]

### 1) Find the dataset pipeline entrypoint
Look under `src/pipelines/` for the domain/dataset implementation. [^pipelines-home]

### 2) Run validation (examples — replace with real commands used here)
```bash
# Example A: pipeline-run validation mode (preferred)
python -m src.pipelines.external.<dataset_slug>.run --validate

# Example B: standalone validator (if tools/ provides it)
python tools/validate_dataset.py --domain external --dataset <dataset_slug> --stage processed
```

### 3) Commit the right artifacts ✅
Commit **small, stable** outputs:
- `contract/` and `schemas/` (contract artifacts)
- `baselines/` (if used for regression)
- `reports/latest.md` + `reports/latest.json` (summary evidence)
- `samples/invalid_*` (only if it helps reproduce failures; keep small)

Avoid committing:
- huge raw logs
- full debug dumps
- temporary scratch outputs

---

## 🤖 CI Expectations (what will block your PR)

KFM CI is designed to keep `main` “CI-clean” by enforcing:

- Schema validation + provenance completeness
- Required metadata presence
- Security/governance scans (secrets, PII, sensitive content)
- Missing PROV / broken links / sensitive leaks → **build fails** [^ci-gates] [^security-scans]

---

## 🏛️ Governance Notes (External domain)

Because this dataset is in `external/`, adding a new external provider/source (or materially changing the source) may trigger a **manual governance review**, including license verification, provenance quality, and standards alignment. [^external-source-review]

If this dataset involves sensitive cultural locations / sovereignty concerns, ensure:
- redaction/generalization is applied consistently across processed data + metadata + API exposure [^security-scans]
- the justification is documented (contract + metadata + pipeline notes)

---

## 🧩 Reviewer Checklist (PR-ready)

- [ ] Processed outputs updated under `data/external/processed/<dataset_slug>/`
- [ ] Validation artifacts updated in this folder (`reports/`, `contract/`, `baselines/` as applicable)
- [ ] STAC/DCAT/PROV entries exist and match this dataset (paths filled above)
- [ ] No classification downgrade; no sensitive location/PII leak
- [ ] CI is green ✅

---

## 📚 References (project docs)

[^domain-layout]: Recommended domain layout includes `data/<domain>/raw`, `data/<domain>/work`, and `data/<domain>/processed`.:contentReference[oaicite:0]{index=0}

[^pipeline-order]: Pipeline ordering is absolute (ETL → catalogs → graph → API → UI → narrative); no stage can bypass prior contracts/outputs.:contentReference[oaicite:1]{index=1}

[^catalog-paths]: Catalog outputs are written to `data/stac/…`, `data/catalog/dcat/…`, and `data/prov/…`.:contentReference[oaicite:2]{index=2}

[^boundary-artifacts]: STAC/DCAT/PROV are required “boundary artifacts” before data is considered fully published and consumed downstream.:contentReference[oaicite:3]{index=3}

[^contract-first]: “Contract-first” treats schemas/contracts as first-class artifacts; changes trigger strict versioning/compat checks.:contentReference[oaicite:4]{index=4}

[^deterministic]: Deterministic, idempotent ETL is required for reproducibility; runs are logged and repeatable.:contentReference[oaicite:5]{index=5}

[^ci-gates]: Validation gates are enforced via CI (schema validation, provenance completeness, security scans); violations fail the build.:contentReference[oaicite:6]{index=6}

[^security-scans]: CI includes secret scanning, PII/sensitive data scans, sensitive location checks, and classification consistency checks.:contentReference[oaicite:7]{index=7}

[^classification]: Classification propagation is enforced; outputs must not be less restricted than inputs without approved review/redaction.:contentReference[oaicite:8]{index=8}

[^external-source-review]: New external data sources trigger manual review of license, provenance quality, and standards alignment.:contentReference[oaicite:9]{index=9}

[^prov-end-to-end]: PROV should link raw → intermediate → processed and identify the producing run/config (e.g., run ID/commit hash).:contentReference[oaicite:10]{index=10}

[^validation-tools]: Catalog generation & validation tooling should live in `src/pipelines/` and/or `tools/` (and be referenced consistently).:contentReference[oaicite:11]{index=11}

[^pipelines-home]: `src/pipelines/` is the canonical home for ETL jobs and data transformation code.:contentReference[oaicite:12]{index=12}

[^no-manual-edits]: Avoid manual edits to processed outputs; fix pipelines so changes are reproducible and reviewable.:contentReference[oaicite:13]{index=13}


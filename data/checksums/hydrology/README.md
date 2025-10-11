<div align="center">

# 💧 Kansas Frontier Matrix — Hydrology Checksums  
`data/checksums/hydrology/`

**Mission:** Guarantee **data integrity, reproducibility, and provenance** for all processed hydrology datasets —  
rivers, watersheds, flood zones, aquifers, groundwater levels — via **SHA-256 checksum verification** and **CI/CD gates**.

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../.github/workflows/site.yml)  
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../.github/workflows/stac-validate.yml)  
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../.github/workflows/codeql.yml)  
[![Trivy Security](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/trivy.yml?label=Trivy%20Security)](../../../.github/workflows/trivy.yml)  
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)

</div>

---

## 📚 Overview

`data/checksums/hydrology/` houses **SHA-256 checksum files (`.sha256`)** for all **processed hydrology datasets** in KFM.  
Each checksum is a **cryptographic fingerprint** confirming the asset is unchanged since validation — enabling reproducibility  
and transparent provenance across environments.

**Checksums provide:**
- 💧 **Integrity** — Detects corruption, bit-flips, or manual edits.  
- 🔁 **Reproducibility** — Verifies deterministic ETL outputs across rebuilds.  
- 🔗 **Provenance** — Binds datasets to metadata, STAC Items, and source manifests.  
- 🔍 **Auditability** — Automates verification and CI/CD enforcement.  

All `.sha256` files are created by the **Hydrology ETL** (`make hydrology`) and validated on every commit.

---

## 🧭 Hydrology Integrity Workflow

```mermaid
flowchart LR
  S["data/sources/hydrology/*.json\nSource Manifests"] --> R["data/raw/hydrology/**\nNHD · NFHL · Observations"]
  R --> P["src/pipelines/hydrology_pipeline.py\nETL · Clean · Derive"]
  P --> O["data/processed/hydrology/**\nGeoJSON · COG · CSV"]
  O --> C["data/checksums/hydrology/*.sha256\nPer-asset digests"]
  O --> T["data/stac/hydrology/**.json\nSTAC Items (checksum:sha256)"]
  C --> V["CI Validation\nsha256sum -c + STAC parity"]
%% END OF MERMAID
````

<!-- END OF MERMAID -->

---

## 🗂️ Directory Layout

```bash
data/checksums/hydrology/
├── README.md
├── nhd_flowlines_ks.geojson.sha256
├── watersheds_huc12_ks.geojson.sha256
├── fema_nfhl_ks.geojson.sha256
├── groundwater_levels_ks.geojson.sha256
└── flood_events_ks.geojson.sha256
```

> Each `.sha256` corresponds to a dataset in `data/processed/hydrology/` and is verified in CI via `sha256sum -c`.

---

## 🧮 Example `.sha256` File

```bash
# File: watersheds_huc12_ks.geojson.sha256
a30f8ccbd7f2b6171cbfe38bb99a4c28a7f26dcbf2a032dcac34d79b94cf6a0f  watersheds_huc12_ks.geojson
```

This proves `data/processed/hydrology/watersheds_huc12_ks.geojson` matches the canonical build output.

---

## ⚙️ Generation & Verification

**Make targets**

```bash
make hydrology-checksums          # generate checksums after ETL
make hydrology-checksums-verify   # verify checksums (used by CI)
```

**Python CLI**

```bash
python src/utils/generate_checksums.py data/processed/hydrology/ --algo sha256
```

**Steps**

1. Discover `.geojson`, `.tif`, `.csv` (configurable).
2. Compute SHA-256 via `hashlib` or `sha256sum`.
3. Write `<filename>.sha256` to `data/checksums/hydrology/`.
4. CI re-computes and cross-checks digests on each commit; logs → `data/work/logs/hydrology_checksums.log`.

---

## 🧰 CI/CD Validation

**Command executed in CI**

```bash
sha256sum -c data/checksums/hydrology/*.sha256
```

| Outcome       | Behavior                                                        |
| :------------ | :-------------------------------------------------------------- |
| ✅ **Success** | Files verified; build proceeds.                                 |
| ❌ **Failure** | Pipeline halts; reprocess asset, regenerate checksum, recommit. |
| 🧾 **Logs**   | Results archived under `data/work/logs/` for MCP audits.        |

> Integrated with **`.github/workflows/stac-validate.yml`** to enforce checksum–metadata parity.

---

## 🔗 Integration with Metadata & STAC

| Component                             | Function                                                  |
| :------------------------------------ | :-------------------------------------------------------- |
| `data/stac/hydrology/**.json`         | STAC Items include `"checksum:sha256"` for each asset.    |
| `data/processed/metadata/hydrology/`  | Mirrors checksum/provenance for non-STAC artifacts.       |
| `src/pipelines/hydrology_pipeline.py` | Emits checksums at end of ETL; writes verification logs.  |
| `.github/workflows/stac-validate.yml` | Validates checksum integrity and STAC schema conformance. |
| `data/checksums/manifest.sha256`      | Aggregates domain manifests for global verification.      |

---

## 🧩 Troubleshooting & Remediation

| Issue                     | Likely Cause                             | Recommended Fix                                         |
| :------------------------ | :--------------------------------------- | :------------------------------------------------------ |
| CI fails on hash mismatch | File changed or truncated post-ETL       | `make hydrology-checksums` → commit updated `.sha256`.  |
| Missing checksum          | New layer produced without digest        | Run generator CLI and add the sidecar file.             |
| STAC mismatch             | `checksum:sha256` out of sync            | `make stac` to refresh Items from current checksums.    |
| Random mismatches         | Non-deterministic compression/timestamps | Pin libs, set `SOURCE_DATE_EPOCH`, normalize GDAL opts. |

---

## 🧠 MCP Compliance Matrix

| MCP Principle           | Implementation                                              |
| :---------------------- | :---------------------------------------------------------- |
| **Documentation-first** | README defines policy, structure, commands, and CI hooks.   |
| **Reproducibility**     | Deterministic hashing + CI verification on each commit.     |
| **Open Standards**      | SHA-256 (FIPS 180-4), STAC checksum extension, POSIX paths. |
| **Provenance**          | Checksums + STAC Items bind assets to immutable identities. |
| **Auditability**        | CI failure gates and retained logs ensure traceability.     |

---

## 📅 Version History

| Version  | Date       | Summary                                                                                                   |
| :------- | :--------- | :-------------------------------------------------------------------------------------------------------- |
| **v1.2** | 2025-10-11 | Protocol v1.1 upgrade: front-matter, Mermaid flow, CI parity clarifications, remediation guide tightened. |
| **v1.1** | 2025-10-10 | Added FEMA NFHL & flood events; expanded CI logging, troubleshooting, manifest integration.               |
| **v1.0** | 2025-10-04 | Initial hydrology checksum docs — rivers, watersheds, floods, groundwater layers verified.                |

---

<div align="center">

**Kansas Frontier Matrix** — *Every River Verified: Data Integrity That Flows.*
📍 [`data/checksums/hydrology/`](.) · Linked to the **Hydrology STAC Collection** and **Global Manifest Registry**.

</div>
```

<div align="center">

# ⚠️ Kansas Frontier Matrix — Hazards Checksums  
`data/checksums/hazards/`

**Mission:** Guarantee **integrity, reproducibility, and provenance** of all processed **natural hazard datasets** —  
including tornado tracks, floods, wildfires, drought indices, and disaster declarations — through  
**SHA-256 validation** and **automated CI/CD enforcement** across the Kansas Frontier Matrix (KFM).

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../.github/workflows/site.yml)  
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../.github/workflows/stac-validate.yml)  
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../.github/workflows/codeql.yml)  
[![Trivy Security](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/trivy.yml?label=Trivy%20Security)](../../../.github/workflows/trivy.yml)  
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)

</div>

---

## 📚 Overview

The `data/checksums/hazards/` directory contains **SHA-256 checksum manifests (`.sha256`)**  
for all processed **hazard datasets** within KFM.  

These digests act as immutable fingerprints proving that hazard data —  
such as tornado tracks, wildfire perimeters, and FEMA disaster records —  
remain byte-for-byte consistent and reproducible across processing environments.

**Checksums ensure:**
- 🧱 **Integrity** — Detect silent corruption or unauthorized modification.  
- 🔁 **Reproducibility** — Confirm deterministic ETL outputs across rebuilds.  
- 🔗 **Provenance** — Link all assets to their STAC metadata and source manifests.  
- 🧩 **Auditability** — Enable automatic verification and historical traceability in CI/CD.  

All `.sha256` files are generated via the **Hazards ETL (`make hazards`)**  
and validated in real-time during every workflow run.

---

## 🧭 Hazards Integrity Workflow

```mermaid
flowchart LR
  S["data/sources/hazards/*.json\nSource Manifests"] --> R["data/raw/hazards/**\nNOAA · FEMA · USFS"]
  R --> P["src/pipelines/hazards_pipeline.py\nETL · Merge · Derive"]
  P --> O["data/processed/hazards/**\nGeoJSON · TIFF · CSV"]
  O --> C["data/checksums/hazards/*.sha256\nIntegrity Proofs"]
  O --> T["data/stac/hazards/**.json\nSTAC Items (checksum:sha256)"]
  C --> V["CI Validation\nsha256sum -c + STAC parity"]
%% END OF MERMAID
````

<!-- END OF MERMAID -->

---

## 🗂️ Directory Layout

```bash
data/checksums/hazards/
├── README.md
├── tornado_tracks_1950_2024.geojson.sha256
├── flood_events_1900_2025.geojson.sha256
├── wildfire_perimeters_2000_2024.geojson.sha256
├── drought_index_2000_2025.tif.sha256
└── fema_disaster_declarations_1953_2025.csv.sha256
```

> Each `.sha256` corresponds to a dataset under `data/processed/hazards/`
> and is verified automatically via `sha256sum -c` during CI.

---

## 🧮 Example `.sha256` File

```bash
# File: tornado_tracks_1950_2024.geojson.sha256
8fb29cda3d0e44182f26c7bceff74b2c81b83e742d47d836b33151f871bb69d1  tornado_tracks_1950_2024.geojson
```

This confirms that
`data/processed/hazards/tornado_tracks_1950_2024.geojson`
is identical to the last validated version and has not been altered.

---

## ⚙️ Generation & Validation Workflow

**Make targets**

```bash
make hazards-checksums          # Generate checksums for all hazard outputs
make hazards-checksums-verify   # Verify all hashes (CI enforcement)
```

**Python CLI**

```bash
python src/utils/generate_checksums.py data/processed/hazards/ --algo sha256
```

**Steps**

1. Discover `.geojson`, `.tif`, `.csv` files under `data/processed/hazards/`.
2. Compute SHA-256 using `hashlib` for deterministic hashing.
3. Write `<filename>.sha256` to `data/checksums/hazards/`.
4. CI validates all hashes; logs saved to `data/work/logs/hazards_checksums.log`.

---

## 🧰 CI/CD Verification

**Command executed by CI**

```bash
sha256sum -c data/checksums/hazards/*.sha256
```

| Outcome     | Behavior                                              |
| :---------- | :---------------------------------------------------- |
| ✅ **Pass**  | Integrity verified, metadata synchronized.            |
| ❌ **Fail**  | Pipeline stops; re-run ETL and regenerate checksums.  |
| 🧾 **Logs** | Written to `data/work/logs/` for MCP audit retention. |

> Coupled with **STAC validation workflows** (`.github/workflows/stac-validate.yml`)
> to ensure checksum–metadata consistency before merge or deploy.

---

## 🔗 Integration with Metadata & STAC

| Component                             | Function                                                      |
| :------------------------------------ | :------------------------------------------------------------ |
| `data/stac/hazards/**.json`           | STAC Items embed `"checksum:sha256"` for each hazard dataset. |
| `data/processed/metadata/hazards/`    | Mirrors checksum values for non-STAC assets.                  |
| `src/pipelines/hazards_pipeline.py`   | Automates checksum creation and validation after ETL.         |
| `.github/workflows/stac-validate.yml` | Ensures checksum integrity + STAC schema conformance.         |
| `data/checksums/manifest.sha256`      | Aggregates all domain manifests for global validation.        |

---

## 🧩 Troubleshooting & Maintenance

| Issue                | Likely Cause                                      | Resolution                                           |
| :------------------- | :------------------------------------------------ | :--------------------------------------------------- |
| CI fails on mismatch | File changed or reprocessed without updated hash. | Run `make hazards-checksums` and recommit checksums. |
| Missing `.sha256`    | New dataset not yet hashed.                       | Execute generator CLI or `make hazards-checksums`.   |
| STAC drift           | STAC `checksum:sha256` not refreshed.             | Run `make stac` to rebuild metadata.                 |
| Random mismatches    | Non-deterministic compression or timestamps.      | Set `SOURCE_DATE_EPOCH`; normalize export settings.  |

---

## 🧠 MCP Compliance Matrix

| MCP Principle           | Implementation                                        |
| :---------------------- | :---------------------------------------------------- |
| **Documentation-first** | Each dataset includes README + `.sha256` manifest.    |
| **Reproducibility**     | Deterministic SHA-256 validation ensures consistency. |
| **Open Standards**      | FIPS 180-4 SHA-256 + STAC checksum extension.         |
| **Provenance**          | Datasets linked via ETL → checksum → STAC.            |
| **Auditability**        | CI failure gates + archived logs for traceability.    |

---

## 📅 Version History

| Version  | Date       | Summary                                                                                                          |
| :------- | :--------- | :--------------------------------------------------------------------------------------------------------------- |
| **v1.2** | 2025-10-11 | Upgraded to KFM Markdown Protocol v1.1; added Mermaid workflow, CI parity details, and reproducibility controls. |
| **v1.1** | 2025-10-10 | Added FEMA disaster checksums, enhanced troubleshooting and STAC integration.                                    |
| **v1.0** | 2025-10-04 | Initial checksum documentation — tornado, flood, wildfire, drought verified.                                     |

---

<div align="center">

**Kansas Frontier Matrix** — *Every Storm Verified: Integrity Through Time.*
📍 [`data/checksums/hazards/`](.) · Linked to **Hazards STAC Collection** and **Global Manifest Registry**.

</div>
```

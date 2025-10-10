```yaml
---
name: 🐛 Bug Report
about: Report a reproducible issue in code, data, pipelines, workflows, or documentation.
title: "[BUG] <Concise, action-oriented summary>"
labels: ["bug", "needs-review", "triage"]
assignees: []
version: "v2.0.0"
last_updated: "2025-10-10"
tags: ["bug", "reproducibility", "ci", "stac", "data-integrity"]
governance:
  requires_repro_steps: true
  requires_logs: true
  requires_provenance: true
  reviewers_required: 2
security:
  sensitive_data: "Do not include secrets or API keys in issue content."
---
```

<div align="center">

# 🐞 Kansas Frontier Matrix — Bug Report Template

### *“Every Bug Leaves a Trace — Every Trace Leads to Reproducibility.”*

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../.github/workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../LICENSE)

</div>

---

## 🧩 Summary

Clearly describe the **unexpected behavior** or **data discrepancy**. Include what you were attempting to do and what went wrong.

> **Example:**
> Terrain ETL workflow fails checksum verification for 2020 LiDAR tiles when reprojecting to EPSG:4326.

---

## 🧠 Context

| Field                         | Description                                                                    |
| :---------------------------- | :----------------------------------------------------------------------------- |
| **Module / Workflow**         | (e.g., `terrain_pipeline.py`, `stac-validate.yml`, `src/graph/build_graph.py`) |
| **Data Domain**               | (e.g., Terrain, Hydrology, Hazards, Landcover, Climate, AI/NLP)                |
| **Branch / Commit**           | (e.g., `main`, `feature/lidar-v2`, `4a8e91c`)                                  |
| **Environment**               | (OS, Python/Node version, GitHub runner type, Docker image)                    |
| **Date Observed**             | (e.g., `2025-10-10`)                                                           |
| **Dataset Version / STAC ID** | (e.g., `terrain_ks_1m_v2.3`, `stac/items/terrain_ks_2020.json`)                |
| **Workflow Run URL**          | (link to CI/CD run if applicable)                                              |

---

## 🔁 Steps to Reproduce

Provide **deterministic steps** to replicate this issue.

```bash
# Example
make terrain
# or
python src/pipelines/terrain/terrain_pipeline.py --config config/test_terrain.yaml
```

1. **Step 1** — Command or Make target used
2. **Step 2** — Input file(s) or dataset IDs
3. **Step 3** — Observed output or failure state

---

## 🧠 Expected Behavior

Describe **what should have happened** if the system behaved correctly.
*(Include file outputs, logs, or expected message.)*

---

## 💥 Actual Behavior

Describe **what actually happened** — including error messages, stack traces, or screenshots.

```bash
# Example error
FileNotFoundError: 'data/processed/terrain/ks_1m_dem_2020.tif' missing.
```

> **Optional:** Attach log excerpt or upload `.log` file under `data/work/logs/`.

---

## 📄 Logs & Evidence

| Artifact              | Path / Link                                                    |
| :-------------------- | :------------------------------------------------------------- |
| **Log File**          | `data/work/logs/<domain>_etl_debug.log`                        |
| **CI/CD Run URL**     | (e.g., `https://github.com/bartytime4life/.../runs/123456789`) |
| **Screenshot / JSON** | Attach below (if UI or API related)                            |

<details><summary><b>Example Traceback (expand)</b></summary>

```bash
Traceback (most recent call last):
  File "src/pipelines/terrain_pipeline.py", line 214, in <module>
    main()
FileNotFoundError: Missing intermediate COG at data/work/tmp/dem_fill_stage.tif
```

</details>

---

## 🔍 Checksum / Integrity Verification

If the issue relates to data integrity, include hash comparisons.

| File                                        | Expected SHA-256 | Observed SHA-256 |
| :------------------------------------------ | :--------------- | :--------------- |
| `data/processed/terrain/ks_1m_dem_2020.tif` | `abc123...`      | `def789...`      |
| `data/stac/items/terrain_ks_2020.json`      | `ffd234...`      | `ffd234...` ✅    |

---

## 🧾 Impact Assessment

| Category               | Impact / Notes                                                         |
| :--------------------- | :--------------------------------------------------------------------- |
| **Severity**           | 🟥 Critical / 🟧 Major / 🟨 Moderate / 🟩 Minor                        |
| **Affected Pipelines** | (`make terrain`, `make hydrology`, etc.)                               |
| **Downstream Effects** | (e.g., web UI map missing tiles, graph edges broken, STAC invalidated) |
| **User Impact**        | (Researchers, API clients, CI/CD jobs, public site)                    |

---

## 🧰 Suggested Fix / Next Steps *(Optional)*

If possible, provide proposed resolutions:

* [ ] Patch ETL pipeline logic
* [ ] Re-run `make checksums`
* [ ] Update STAC metadata (datetime, bbox, CRS)
* [ ] Regenerate missing artifacts
* [ ] Verify in local environment (`make validate-<domain>`)
* [ ] Submit PR referencing this issue

---

## 🧪 Validation Commands

Provide the exact commands to **validate or reproduce**.

```bash
# Verify checksum integrity
make checksums

# Rebuild affected pipeline
make terrain

# Validate STAC JSON
make stac-validate

# Run all pre-commit tests
pre-commit run --all-files
```

---

## 🧭 Versioning Impact

| Scope                     | Current Version | Affected | Action                 |
| :------------------------ | :-------------- | :------- | :--------------------- |
| **Dataset / STAC**        | `v1.3.0`        | ✅        | bump → `v1.3.1`        |
| **Pipeline / Script**     | `v2.0.0`        | ✅        | fix → `v2.0.1`         |
| **Workflow (CI/CD)**      | `v1.2.0`        | ❌        | none                   |
| **Repo Release (SemVer)** | `v1.4.0`        | ✅        | patch release required |

---

## 🧠 MCP Compliance Checklist

| MCP Principle           | Confirmed                                        |
| :---------------------- | :----------------------------------------------- |
| **Documentation-first** | 🗹 Clear summary + structured context            |
| **Reproducibility**     | 🗹 Steps + deterministic validation commands     |
| **Open Standards**      | 🗹 Error reproducible via Make/CI workflows      |
| **Provenance**          | 🗹 Logs, checksums, STAC items attached          |
| **Auditability**        | 🗹 CI/CD reference linked; reproducible evidence |
| **Versioning**          | 🗹 Version fields updated or impact noted        |

---

## 🧩 Related Issues / References

* Linked PRs: #…
* Similar Issues: #…
* Affected Datasets: `data/stac/items/...`
* Documentation References: `docs/sop/terrain_pipeline.md`

---

## 🧠 Additional Notes

Include screenshots, system specs, related discussions, or diagnostic insight that can accelerate triage.

---

<div align="center">

### 🧭 Kansas Frontier Matrix — *“Every Bug Leaves a Trace · Every Trace Leads to Reproducibility.”*

**Report · Verify · Fix · Document · Version.**

</div>

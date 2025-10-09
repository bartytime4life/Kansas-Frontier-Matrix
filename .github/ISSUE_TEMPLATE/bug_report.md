---
name: 🐛 Bug Report
about: Report a reproducible issue in code, data, workflows, or documentation.
title: "[BUG] <Brief description>"
labels: ["bug", "needs-review"]
assignees: []
---

## 🐞 Summary
A clear and concise description of the issue or unexpected behavior.

---

## 🧩 Context

| Field | Description |
|:------|:-------------|
| **Module / Workflow** | (e.g., `terrain_pipeline.py`, `stac-validate.yml`) |
| **Data Domain** | (e.g., Terrain, Hydrology, Climate, Landcover) |
| **Branch / Commit** | (e.g., `main`, `d4f9e12`) |
| **Environment** | (OS, Python version, GitHub runner type) |
| **Date Observed** | (e.g., `2025-10-04`) |

---

## 🔁 Steps to Reproduce
Provide **deterministic steps** to reproduce the issue.

```bash
# Example
make terrain
# or
python src/pipelines/terrain/terrain_pipeline.py --config config/test_terrain.yaml
````

1. Step 1 — Describe what command or workflow was executed
2. Step 2 — Mention relevant input files or parameters
3. Step 3 — Describe what you observed

---

## 🧠 Expected Behavior

Describe what **should have happened** or what output was expected.

---

## 💥 Actual Behavior

Describe what **actually happened** — include logs, screenshots, or error messages.

```bash
# Example error
FileNotFoundError: No such file or directory 'data/processed/terrain/ks_1m_dem_2018_2020.tif'
```

---

## 📄 Logs & Evidence

Attach or paste logs, tracebacks, or CI/CD run links that illustrate the problem.

* **Log File Path:** (e.g., `data/work/logs/terrain_etl.log`)
* **CI/CD Run URL:** (if applicable)

---

## 🔍 Checksum Validation

If this issue involves **data integrity**, include any related checksum results.

| File                                             | Expected Hash | Observed Hash |
| :----------------------------------------------- | :------------ | :------------ |
| `data/processed/terrain/ks_1m_dem_2018_2020.tif` | `abc123...`   | `def456...`   |

---

## 🧾 Impact Assessment

| Category               | Impact                                                                 |
| :--------------------- | :--------------------------------------------------------------------- |
| **Criticality**        | 🟥 High / 🟧 Medium / 🟩 Low                                           |
| **Affected Pipelines** | (List ETL or CI/CD workflows affected)                                 |
| **Downstream Effects** | (Describe if other datasets, metadata, or visualizations are impacted) |

---

## 🧰 Suggested Fix or Next Steps *(Optional)*

If you have insights or possible resolutions, please document them here.

* [ ] Patch ETL pipeline
* [ ] Update STAC metadata
* [ ] Regenerate checksums
* [ ] Other (describe)

---

## 🧠 MCP Compliance

| Principle               | Confirmation                                      |
| :---------------------- | :------------------------------------------------ |
| **Documentation-first** | 🗹 Description and context provided               |
| **Reproducibility**     | 🗹 Steps and configuration included               |
| **Open Standards**      | 🗹 Error reproducible via public workflows        |
| **Provenance**          | 🗹 Logs and hashes provided for traceability      |
| **Auditability**        | 🗹 CI/CD reference or reproducible command listed |

---

## 🧩 Additional Notes

Include any other context, screenshots, related issues, or insights helpful to reviewers.

---

**Kansas Frontier Matrix — “Every Bug Leaves a Trace.”**

<div align="center">

# 💡 Kansas Frontier Matrix — Feature Request Template

### *“Every Feature Builds the Future · Every Change is Reproducible.”*

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)
[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../LICENSE)

</div>

---

## 💡 Summary

Provide a clear, concise description of the **feature, enhancement, or optimization**.
Include background context, existing limitation, and expected benefits.

> **Example:**
> Add slope classification to terrain pipeline outputs and include gradient visualization in the MapLibre UI.

---

## 🎯 Motivation / Use Case

Explain **why** this feature is needed and what **problem** it solves.

| Field                    | Description                                                                                     |
| :----------------------- | :---------------------------------------------------------------------------------------------- |
| **Domain / Module**      | (Terrain, Hydrology, Climate, Metadata, Web UI, AI/NLP)                                         |
| **Pipeline / Component** | (e.g., `terrain_pipeline.py`, `graph_ingest.py`, `stac-validate.yml`, `web/config/layers.json`) |
| **Use Case**             | (e.g., “Enable classification maps for slope ranges.”)                                          |
| **Current Limitation**   | (e.g., “No slope visualization or categorization available.”)                                   |
| **Dependencies**         | (e.g., Requires WhiteboxTools v2.2+, or STAC schema update.)                                    |

---

## 🧩 Proposed Solution

Describe the proposed implementation or design change in detail.
Include technical specifics, proposed workflow changes, and architecture impacts.

```bash
# Example Implementation
python src/pipelines/terrain/terrain_pipeline.py --add-slope-classification
```

| Type                                   | Action | Expected Impact |
| :------------------------------------- | :----- | :-------------- |
| [ ] Add new data transformation module |        |                 |
| [ ] Modify ETL pipeline step           |        |                 |
| [ ] Extend STAC metadata schema        |        |                 |
| [ ] Create new visualization layer     |        |                 |
| [ ] Update documentation / SOP         |        |                 |
| [ ] Other (describe below)             |        |                 |

---

## 🧮 Expected Outcome

Explain what the system will accomplish after implementation.

| Metric              | Expected Change                                           |
| :------------------ | :-------------------------------------------------------- |
| **Data Quality**    | (Improved accuracy, consistency, or schema richness.)     |
| **Reproducibility** | (Deterministic outputs or better pipeline documentation.) |
| **Usability**       | (Simpler workflows, improved automation, or UI clarity.)  |
| **Performance**     | (Reduced runtime, lower memory, faster ETL execution.)    |

---

## ⚙️ Implementation Plan *(Optional)*

| Step | Action                        | Owner | Dependencies | Version Impact |
| :--- | :---------------------------- | :---- | :----------- | :------------- |
| 1    | Draft feature design          |       |              |                |
| 2    | Implement or refactor code    |       |              |                |
| 3    | Add unit / integration tests  |       |              |                |
| 4    | Update docs and STAC metadata |       |              |                |
| 5    | Peer review and merge         |       |              |                |

> **Tip:** If this feature introduces versioned schema or data format changes, include a `CHANGELOG.md` entry and bump SemVer accordingly.

---

## 🧭 Versioning Impact

| Scope                     | Current Version | Proposed | Notes                    |
| :------------------------ | :-------------- | :------- | :----------------------- |
| **Dataset / STAC Schema** | `v1.2.0`        | `v1.3.0` | Adds new metadata fields |
| **Pipeline / Script**     | `v2.0.0`        | `v2.1.0` | Refactored terrain ETL   |
| **Repo (SemVer)**         | `v1.4.0`        | `v1.5.0` | Minor feature addition   |

> Use **Semantic Versioning** rules:
> 🩵 Patch → Fix · 💛 Minor → Feature · ❤️ Major → Breaking Change

---

## 🔗 Related Artifacts

| Artifact Type            | Reference                                                  |
| :----------------------- | :--------------------------------------------------------- |
| **STAC Item(s)**         | (If schema or property changes are required.)              |
| **Checksum(s)**          | (If feature affects validation.)                           |
| **Workflow / Log**       | (Relevant job or run URL.)                                 |
| **Related Issues / PRs** | (List or link existing work.)                              |
| **SOP / ADR Link**       | (`docs/adr/ADR-XXXX-<title>.md` or `docs/sop/<domain>.md`) |

---

## 🧠 MCP Compliance

| MCP Principle           | Confirmation                                                   |
| :---------------------- | :------------------------------------------------------------- |
| **Documentation-first** | 🗹 Feature documented with motivation and technical context.   |
| **Reproducibility**     | 🗹 Deterministic test cases and validation paths defined.      |
| **Open Standards**      | 🗹 Uses STAC, JSON Schema, or GeoTIFF/COG conventions.         |
| **Provenance**          | 🗹 Linked to affected datasets, commits, and workflows.        |
| **Auditability**        | 🗹 Traceable through CI validation and review checkpoints.     |
| **Versioning**          | 🗹 Semantic version increment or dataset STAC version updated. |

---

## 📈 Potential Impact

| Category                   | Description                                                |
| :------------------------- | :--------------------------------------------------------- |
| **Performance**            | (Estimate time, memory, or computational improvements.)    |
| **Data Scope**             | (Which datasets, layers, or models will be affected?)      |
| **Backward Compatibility** | (Will legacy scripts break?)                               |
| **UI / Visualization**     | (Will map layers, timelines, or popups change?)            |
| **Security / Compliance**  | (Does this feature alter access control or data exposure?) |

---

## 🧮 Validation Requirements

Before merging this feature, confirm the following checks are performed:

* [ ] Unit tests added and passing
* [ ] STAC schema validated via `make stac-validate`
* [ ] ETL reproducibility confirmed (input → output deterministic)
* [ ] License and data compliance verified
* [ ] Docs updated under `/docs/sop/` or `/docs/adr/`
* [ ] Version bump in `CHANGELOG.md`

---

## 📊 Governance Review Checklist (Maintainers)

| Criteria                           | Reviewer Action               | Status |
| :--------------------------------- | :---------------------------- | :----- |
| Design Doc Submitted (`docs/adr/`) | Verify scope and traceability | ☐      |
| STAC Schema Impact Assessed        | Review schema versioning      | ☐      |
| CI/CD Tests Passing                | Confirm green checks          | ☐      |
| Security Review Complete           | Verify no new vulnerabilities | ☐      |
| Version / Tag Bump Approved        | Align with SemVer policy      | ☐      |

---

## 🧩 Additional Notes

Include sketches, UML diagrams, mockups, or example screenshots to aid understanding.
If available, attach figures or JSON snippets showing expected outputs.

---

<div align="center">

### 💡 Kansas Frontier Matrix

**“Every Feature Builds the Future — Versioned, Proven, and Reproducible.”**

</div>

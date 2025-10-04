<div align="center">

# 🧾 Kansas Frontier Matrix — Standard Operating Procedure (SOP) Template  
`docs/templates/sop.md`

**Purpose:** Provide a reproducible, standardized documentation framework  
for operational procedures in the **Kansas Frontier Matrix (KFM)** — ensuring that  
every process, pipeline, and task adheres to **MCP** principles of documentation-first reproducibility,  
open standards, and auditable provenance.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)

</div>

---

## 🧭 SOP Metadata

| Field | Description |
|:------|:-------------|
| **SOP ID** | Unique identifier (e.g., `SOP-2025-001-STAC`) |
| **Title** | Short title describing the process |
| **Author(s)** | Individual(s) responsible for this procedure |
| **Date Created** | YYYY-MM-DD |
| **Last Updated** | YYYY-MM-DD |
| **Version** | v1.0, v1.1, etc. |
| **Status** | Draft / In Review / Approved / Deprecated |
| **Domain** | Data / Pipelines / Web / CI-CD / Metadata / Documentation |
| **Associated Workflow(s)** | (e.g., `stac-validate.yml`, `checksums.yml`) |
| **Approval Authority** | Reviewer or governing team that authorizes procedure |
| **License** | CC-BY 4.0 (Documentation) / MIT (Code) |

---

## 🎯 Objective

Define the **purpose** of this procedure, its expected outcomes, and its relevance  
to the KFM system or workflows.

> Example:  
> *To establish a standardized validation workflow for all STAC Items and metadata JSON files  
> to ensure compliance with STAC 1.0.0 and MCP reproducibility principles.*

---

## 🧩 Scope

Clearly define **where and when** this SOP applies.

| Parameter | Definition |
|:------------|:-------------|
| **Applies To** | (Departments, systems, or pipelines) |
| **Exclusions** | (What this SOP does *not* cover) |
| **Dependencies** | (Other SOPs, data layers, or CI/CD jobs) |
| **Frequency** | (e.g., Per commit, daily, per dataset release) |

> Example:  
> *Applies to all JSON metadata files within `data/stac/` and runs automatically  
> on every pull request or commit to `main`.*

---

## ⚙️ Prerequisites & Requirements

| Requirement | Description |
|:--------------|:-------------|
| **Software** | (Python, GDAL, Node, etc.) |
| **Access Permissions** | (GitHub Actions runner, write access, etc.) |
| **Dependencies** | (List scripts, tools, or Makefile targets) |
| **Data / Inputs** | (List directories or specific input files) |
| **Validation Schema** | (Link to `schema.json` or STAC spec used for validation) |

> Example:  
> *Requires `stac-validator >= 3.0`, Python 3.11, and the `data/stac/` directory populated with items.*

---

## 🔄 Procedure Steps

Detail **each step in exact execution order**.  
Use command examples and add bullet points for clarity.

### Step 1 — Initialize Validation Environment
```bash
make setup
pip install stac-validator jsonschema
````

### Step 2 — Run Validation Script

```bash
make stac-validate
```

### Step 3 — Review Output

Check logs in:

```
data/work/logs/validation/
```

### Step 4 — Approve or Reject Changes

* If validation succeeds: merge the PR.
* If errors found: resolve and rerun SOP.

---

## 🧮 Outputs & Deliverables

| Output                | Format    | Location             | Description                       |
| :-------------------- | :-------- | :------------------- | :-------------------------------- |
| **Validation Log**    | `.log`    | `data/work/logs/`    | Records all validation messages   |
| **Checksum Manifest** | `.sha256` | `data/checksums/`    | Confirms file integrity           |
| **STAC Report**       | `.json`   | `data/work/logs/ci/` | STAC validation results           |
| **Summary Report**    | `.md`     | `_site/reports/`     | Human-readable validation summary |

---

## 🧾 Error Handling & Troubleshooting

| Error Type              | Likely Cause                             | Resolution                           |
| :---------------------- | :--------------------------------------- | :----------------------------------- |
| **Validation Failure**  | Invalid schema or missing metadata field | Fix `collection.json` and re-run SOP |
| **Checksum Mismatch**   | File corruption or outdated hash         | Rebuild file and update hash         |
| **Missing Source File** | Incorrect manifest reference             | Correct entry in `data/sources/`     |
| **Network Failure**     | API or fetch timeout                     | Retry or run `make fetch-raw`        |

> Always record failed steps in `data/work/logs/errors/` for traceability.

---

## 🧠 Quality Assurance (QA)

Outline how results are reviewed and approved.

| QA Reviewer             | Step            | Verification                                       |
| :---------------------- | :-------------- | :------------------------------------------------- |
| **Data Manager**        | Post-validation | Confirms STAC compliance                           |
| **Metadata Curator**    | Metadata review | Reviews completeness of descriptions               |
| **Automation Engineer** | CI/CD test      | Confirms passing workflows in `.github/workflows/` |

All QA actions are logged in:

```
data/work/logs/qa/<SOP-ID>_review.log
```

---

## 🧩 Revision & Control

Describe how changes to this SOP are managed and versioned.

| Version | Date       | Author             | Reviewer             | Change Summary                 |
| :------ | :--------- | :----------------- | :------------------- | :----------------------------- |
| v1.0    | 2025-10-04 | Documentation Team | Data Governance Lead | Initial SOP template creation. |

> **Control Rule:** Any update must include a change log entry, approval from governance lead,
> and revalidation via CI/CD.

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                        |
| :---------------------- | :-------------------------------------------------------------------- |
| **Documentation-first** | Procedure documented before implementation.                           |
| **Reproducibility**     | Each step deterministic and automatable.                              |
| **Open Standards**      | Formats: Markdown, JSON Schema, STAC, YAML.                           |
| **Provenance**          | All steps logged and linked to version control.                       |
| **Auditability**        | Logs, reports, and approvals recorded in GitHub Actions + QA folders. |

---

## 📎 Related Documentation

| File                                     | Description                                        |
| :--------------------------------------- | :------------------------------------------------- |
| `docs/templates/experiment.md`           | Experiment documentation template.                 |
| `docs/architecture/ci-cd.md`             | Full CI/CD validation and automation architecture. |
| `docs/architecture/data-architecture.md` | Data flow and validation lifecycle.                |
| `data/ARCHITECTURE.md`                   | Implementation details of data-level validation.   |
| `.github/workflows/stac-validate.yml`    | GitHub Actions workflow that implements this SOP.  |

---

## 🧾 References

1. **SpatioTemporal Asset Catalog (STAC) v1.0.0** — [https://stacspec.org](https://stacspec.org)
2. **Master Coder Protocol (MCP)** — Internal KFM Documentation Framework
3. **Open Geospatial Consortium (OGC)** Standards — [https://ogc.org](https://ogc.org)

---

## 📅 Version History

| Version | Date       | Author                 | Summary                                                                         |
| :------ | :--------- | :--------------------- | :------------------------------------------------------------------------------ |
| v1.0    | 2025-10-04 | KFM Documentation Team | Initial Standard Operating Procedure (SOP) template for reproducible workflows. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Procedure Documented. Every Operation Reproducible.”*
📍 [`docs/templates/sop.md`](.) · Template for MCP-compliant operational procedures in Kansas Frontier Matrix.

</div>

# 🚀 Kansas Frontier Matrix — Pull Request Template  
`.github/PULL_REQUEST_TEMPLATE.md`

**Purpose:** Ensure that every change to the Kansas Frontier Matrix is **documented, reproducible, validated, and auditable**,  
in accordance with the **Master Coder Protocol (MCP)** and repository governance standards.

---

## 🧩 Summary

Provide a concise summary describing what this PR does.

> _Example:_  
> Adds new STAC metadata for the 2020–2024 NOAA Climate dataset and updates corresponding checksum records.

---

## 🔄 Related Issues / Discussions

Link to relevant GitHub issues, discussions, or project tasks.

> Closes #123  
> Related to Discussion: [Climate Pipeline Update](https://github.com/bartytime4life/Kansas-Frontier-Matrix/discussions/45)

---

## 🧠 Type of Change

Select all that apply:

- [ ] 🐛 **Bug Fix** — non-breaking fix resolving a reproducible issue  
- [ ] 💡 **Feature / Enhancement** — adds new functionality or workflow improvements  
- [ ] 🗃️ **New Dataset / Integration** — introduces new data source, manifest, or STAC metadata  
- [ ] 🧩 **Metadata Update** — modifies or corrects STAC or schema documentation  
- [ ] 📖 **Documentation Update** — improves README files or internal documentation  
- [ ] ⚙️ **CI/CD / Workflow Update** — modifies GitHub Actions or automation scripts  
- [ ] 🔒 **Security / Validation** — updates checksums, licenses, or validation logic  
- [ ] 🧹 **Refactor / Cleanup** — improves code readability, structure, or naming conventions

---

## 🧮 Implementation Details

Provide key information about your changes.

| Field | Description |
|:------|:-------------|
| **Affected Directories** | (e.g., `data/processed/climate/`, `data/stac/`, `src/pipelines/`) |
| **New Files Added** | (List any new scripts, datasets, or metadata files) |
| **Pipelines Modified** | (e.g., `terrain_pipeline.py`, `climate_pipeline.py`) |
| **Dependencies Updated** | (List any modified Python packages or GitHub Actions) |
| **Validation Performed** | (Checksum verified, STAC validated, schema validated, etc.) |

---

## ✅ Checklist (MCP + CI/CD Compliance)

Before requesting a review, ensure the following requirements are met.

### 🧠 Documentation-First

- [ ] Updated or added README.md for affected directories  
- [ ] Added or revised STAC metadata if applicable  
- [ ] Documented new datasets in `data/sources/` manifest(s)

### 🔄 Reproducibility

- [ ] Ran relevant Makefile target(s) successfully (`make <target>`)  
- [ ] Regenerated checksums for new/modified datasets  
- [ ] Confirmed all changes are deterministic and reproducible  

### 🧩 Open Standards

- [ ] Verified STAC Items/Collections pass `stac-validator`  
- [ ] Used only open formats (GeoTIFF, GeoJSON, CSV, JSON, NetCDF, etc.)  
- [ ] Followed schema and naming conventions defined in MCP documentation  

### 🔍 Provenance

- [ ] Linked all data or metadata changes to a documented source manifest  
- [ ] Included `last_verified` date in any new source JSON files  
- [ ] Updated provenance chains in metadata if data lineage changed  

### 🧾 Auditability

- [ ] All GitHub Actions workflows passed (`checksums.yml`, `stac-validate.yml`, etc.)  
- [ ] Logs available in `data/work/logs/` for affected pipelines  
- [ ] Peer-reviewed by at least one other contributor (or `@core-maintainers`)  

---

## 🧰 Validation Commands (Example)

Provide any commands used to validate or test your changes locally.

```bash
# Validate STAC structure
make stac-validate

# Rebuild terrain pipeline
make terrain

# Compute new checksums
make checksums

# Run site build and view locally
make site && open _site/index.html
````

---

## 📎 Supporting Artifacts

Attach or link supporting materials for this pull request.

| Type                     | Reference                                      |
| :----------------------- | :--------------------------------------------- |
| **Logs**                 | `data/work/logs/<domain>_etl_debug.log`        |
| **Checksums**            | `data/checksums/<domain>/*.sha256`             |
| **STAC Item(s)**         | `data/stac/<domain>/*.json`                    |
| **Visuals / Thumbnails** | `data/processed/metadata/<domain>/thumbnails/` |
| **Screenshots**          | *(if applicable)*                              |

---

## 📊 Review Notes

Provide any specific notes, testing conditions, or concerns for reviewers.

> *Example:*
> "This dataset has partial coverage for 2019; verify temporal alignment before merging."

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation Verified                                 |
| :---------------------- | :------------------------------------------------------ |
| **Documentation-first** | 🗹 Updated README, metadata, and manifest files         |
| **Reproducibility**     | 🗹 Pipelines and datasets validated deterministically   |
| **Open Standards**      | 🗹 Formats and metadata adhere to public specifications |
| **Provenance**          | 🗹 Source, checksum, and STAC links verified            |
| **Auditability**        | 🗹 All validations logged and CI/CD workflows passed    |

---

## 🧩 Reviewer Checklist

For maintainers or reviewers — verify each condition before approval.

* [ ] All CI workflows pass
* [ ] No schema violations detected
* [ ] Checksums verified and updated
* [ ] Documentation conforms to MCP standards
* [ ] Code readability and formatting confirmed
* [ ] Datasets properly linked in STAC catalog
* [ ] Data provenance and license validated

---

### ✍️ Additional Comments (Maintainers Only)

(Include peer review notes, validation results, or merge approvals.)

---

**Kansas Frontier Matrix — “Every Pull Request Builds the Past, Present, and Future.”**

```

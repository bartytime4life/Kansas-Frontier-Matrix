<div align="center">

# 🚀 **Kansas Frontier Matrix — Pull Request Template**

`📁 .github/PULL_REQUEST_TEMPLATE.md`

**Mission:** Ensure every PR is **documented · reproducible · validated · auditable · versioned** under:

* ✅ Master Coder Protocol (MCP)
* 🔢 Semantic Versioning (SemVer)
* 🛡️ KFM Governance Standards

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../workflows/site.yml)
[![STAC ✅ Validated](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/stac-validate.yml?label=STAC%20%E2%9C%85%20Validated)](../workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../workflows/codeql.yml)
[![Trivy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/trivy.yml?label=Trivy)](../workflows/trivy.yml)
[![Pre-Commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen.svg)](https://pre-commit.com/)
[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue.svg)](../../docs/)

</div>

---

## 🧹 Summary

Briefly describe the purpose, motivation, and outcome of this PR.

> **Example:** Adds STAC Items for NOAA Climate (2020–2024) and updates `web/config/layers.json`.

---

## 🗃️ Linked Work

| Type              | Reference              | Notes               |
| ----------------- | ---------------------- | ------------------- |
| 🐞 **Issue**      | Closes #...            |                     |
| 💬 **Discussion** | #...                   | Context / rationale |
| 📘 **ADR**        | `docs/adr/ADR-####.md` | Decision reference  |

---

## 🧠 Type of Change

Select **all that apply**:

* [ ] 🐛 Bug Fix
* [ ] 💡 Feature / Enhancement
* [ ] 🗃️ Dataset / STAC Metadata
* [ ] 📖 Documentation / Guides
* [ ] ⚙️ CI/CD / Automation
* [ ] 🔒 Security / Validation
* [ ] 🪩 Refactor / Cleanup
* [ ] 💥 Breaking Change (requires migration)

---

## 🧰 Change Summary

| Field             | Details                                     |
| ----------------- | ------------------------------------------- |
| **Scope**         | Affects X files · Risk: Low / Medium / High |
| **Dirs Affected** | `data/hydro/` · `src/pipelines/` · etc.     |
| **New Files**     | List any new scripts, datasets, STACs       |
| **Dependencies**  | Package bumps · Action pins                 |
| **Validation**    | STAC, JSON Schema, tests, SBOM              |
| **Rollback Plan** | Git tag, cleanup steps, revert notes        |
| **Migration**     | Rebuild required? Yes / No                  |

---

## 📦 Versioning & Release

| Component        | Scope           | Change Type         | Version Bump        |
| ---------------- | --------------- | ------------------- | ------------------- |
| 🧱 **Repo**      | Overall repo    | Feature             | `vX.Y.Z → vX.Y+1.Z` |
| 🔌 **API**       | Endpoints       | Compatibility shift | `v1.3 → v1.4`       |
| 🗺️ **Web UI**   | UI interaction  | Minor change        | `v1.2 → v1.3`       |
| 🌐 **STAC Data** | Metadata/schema | Patch bump          | `v1.0.0 → v1.0.1`   |

**Release Checklist:**

* [ ] CHANGELOG.md updated
* [ ] STAC version updated
* [ ] Git tag pushed
* [ ] Artifacts attached
* [ ] Maintainers notified

---

## 📜 Changelog Template

### Added

* NOAA Climate 2020–2024 · New STAC Items & thumbnails

### Changed

* Reprojected `soil_survey_1967` → EPSG:4326

### Fixed

* Corrected D8 accumulation logic in hydrology ETL

### Security

* Pinned `actions/setup-node@v4` · SBOM regen · Trivy scan passed

---

## ✅ MCP + CI Matrix

| ✅ Principle           | Verification Source                      |
| --------------------- | ---------------------------------------- |
| 📖 Docs Updated       | README · STAC · ADR · CHANGELOG          |
| 🧱 Reproducibility    | Deterministic output + checksum verified |
| 📦 Standards          | COG · GeoJSON · CSV · NetCDF             |
| 🧬 Provenance Tracked | STAC lineage · licenses · checksums      |
| 🕵️ Auditability      | CI logs + artifacts (≥90d retained)      |
| 🔢 Versioning         | SemVer across code/data/docs             |

---

## 🧾 Data Lineage

* [ ] Updated `data/sources/*.json`
* [ ] Verified STAC `derived_from` fields
* [ ] Recalculated SHA-256 checksums (`make checksums`)

---

## 🧪 QA & Validation

```bash
pre-commit run --all-files
make stac-validate
make checksums
make site && open _site/index.html
make hydro  # or domain-specific target
```

---

## 📌 Artifacts

| Artifact    | Location                                |
| ----------- | --------------------------------------- |
| Logs        | `data/work/logs/hydro_etl_debug.log`    |
| Checksums   | `data/checksums/hydro/*.sha256`         |
| STAC Items  | `data/stac/hydro/`                      |
| Thumbnails  | `data/processed/metadata/hydro/thumbs/` |
| Screenshots | *(Attach below or link)*                |

---

## ♿ Accessibility (for UI changes)

| Check                   | Status |
| ----------------------- | :----: |
| Keyboard Navigation     |    ☑   |
| Color Contrast (≥4.5:1) |    ☑   |
| ARIA Labels / Roles     |    ☑   |
| Motion Preferences      |    ☑   |

---

## 🔐 Security & Licensing

| Check                        | Status |
| ---------------------------- | :----: |
| SBOM Regenerated             |    ☑   |
| No New CVEs (Trivy/CodeQL)   |    ☑   |
| Action Pins Verified         |    ☑   |
| License Compliance (CC/MIT)  |    ☑   |
| Secrets Scan / OIDC Verified |    ☑   |

---

## 💥 Breaking Changes (If any)

| Component | Description               | Migration Required?         |
| --------- | ------------------------- | --------------------------- |
| API       | `/v1/events → /v2/events` | See `docs/api_migration.md` |
| Data      | STAC schema refactor      | `make hydro` required       |
| Web Layer | Map config renamed        | `web/config/layers.json`    |

---

## 🧭 Reviewer Checklist

| ✅ Check                               | Done? |
| ------------------------------------- | :---: |
| Version headers and changelog present |   ☑   |
| STAC + CI validation passed           |   ☑   |
| Git tag pushed / artifacts archived   |   ☑   |
| Review approved by CODEOWNERS         |   ☑   |

---

## 🕓 Version History

| Version | Date       | Author          | Summary                                            |
| ------- | ---------- | --------------- | -------------------------------------------------- |
| v2.4.0  | 2025-10-16 | Core Docs Team  | UI polish, reviewer checklists, version sync table |
| v2.3.1  | 2025-10-15 | KFM Maintainers | MCP-DL v6.3 alignment · Mermaid formatting fixes   |
| v2.3.0  | 2025-10-15 | KFM Maintainers | CI status badge upgrades · table polish            |
| v2.2.0  | 2025-10-14 | Docs Team       | Data lineage fields + checksum alignment           |
| v2.0.0  | 2025-10-10 | Core Team       | Semantic versioning structure introduced           |

---

<div align="center">

**Kansas Frontier Matrix** — “Every PR leaves a trail. Every trail leaves a version.”

</div>

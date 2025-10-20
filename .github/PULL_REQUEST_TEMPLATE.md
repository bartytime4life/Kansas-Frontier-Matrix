---
title: "🚀 Kansas Frontier Matrix — Pull Request Template"
document_type: "Contribution Template · Governance Workflow"
version: "v3.0.0"
last_updated: "2025-10-20"
status: "Tier-Ω+∞ Certified · Stable"
license: ["MIT (code)", "CC-BY 4.0 (docs)"]
owners: ["@kfm-architecture", "@kfm-docs", "@kfm-security"]
template_version: "MCP-DL v6.3.2"
---

<div align="center">

# 🚀 **Kansas Frontier Matrix — Pull Request Template**  
`📁 .github/PULL_REQUEST_TEMPLATE.md`

**Mission:** Guarantee every PR is **documented · reproducible · validated · auditable · versioned** under:

* ✅ **Master Coder Protocol (MCP-DL v6.3.2)**
* 🔢 **Semantic Versioning (SemVer)**
* 🛡 **Kansas Frontier Matrix Governance Standards**

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../workflows/site.yml)
[![STAC ✅ Validated](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/stac-validate.yml?label=STAC%20%E2%9C%85%20Validated)](../workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../workflows/codeql.yml)
[![Trivy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/trivy.yml?label=Trivy)](../workflows/trivy.yml)
[![SBOM](https://img.shields.io/badge/SBOM-Syft%20%2B%20Grype-blue)](../workflows/sbom.yml)
[![SLSA Provenance](https://img.shields.io/badge/Supply--Chain-SLSA%20Level%202-green)](../workflows/slsa.yml)
[![Docs · MCP-DL v6.3.2](https://img.shields.io/badge/Docs-MCP--DL%20v6.3.2-blue.svg)](../../docs/)

</div>

---

## 🧹 Summary
Briefly describe the purpose, motivation, and expected outcome.  
> *Example:* Adds STAC Items for NOAA Climate (2020–2024) and updates `web/config/layers.json`.

---

## 🗃️ Linked Work
| Type | Reference | Notes |
|:--|:--|:--|
| 🐞 Issue | Closes #… | |
| 💬 Discussion | #… | Context / Rationale |
| 📘 ADR | `docs/adr/ADR-####.md` | Decision reference |
| 🔒 Policy | `docs/standards/security.md` | Related rule |

---

## 🧠 Type of Change
Mark all that apply.  
☐ Bug Fix ☐ Feature ☐ Dataset/STAC ☐ Docs ☐ CI/CD ☐ Security ☐ SBOM ☐ Refactor ☐ Breaking Change  

---

## 🧰 Change Summary
| Field | Details |
|:--|:--|
| **Scope** | Affects X files · Risk Low/Med/High |
| **Dirs Affected** | `data/hydro/`, `src/pipelines/` … |
| **New Files** | Scripts / datasets / workflows |
| **Dependencies** | Package bumps / action pins |
| **Validation** | STAC · Schema · SBOM · OPA |
| **Rollback Plan** | Git tag + cleanup |
| **Migration** | Y / N |

---

## 📦 Versioning & Release
| Component | Scope | Change | Bump |
|:--|:--|:--|:--|
| 🧱 Repo | Overall | Feature | `vX.Y.Z → vX.Y+1.Z` |
| 🔌 API | Endpoints | Compatibility | `v1.3 → v1.4` |
| 🗺 Web UI | UX | Minor | `v1.2 → v1.3` |
| 🌐 STAC | Metadata | Patch | `v1.0.0 → v1.0.1` |
| 🤖 AI | Models | Retrain | `v2.0.0 → v2.1.0` |

**Release Checklist**  
☐ CHANGELOG updated ☐ STAC version bump ☐ Tag pushed  
☐ `make sbom` run ☐ Provenance signed ☐ Maintainers notified

---

## 📜 Changelog Template
### Added  
– NOAA Climate 2020–24 STAC Items – Nightly `ai-model.yml` workflow  
### Changed  
– Reprojected `soil_survey_1967` → EPSG:4326 – Pinned action SHAs  
### Fixed  
– Hydrology ETL D8 logic – Markdown link validator  
### Security  
– SBOM & SLSA attestations – Trivy scan passed ✅  

---

## ✅ MCP + CI Matrix
| Principle | Verification |
|:--|:--|
| 📖 Docs | README · STAC · ADR · CHANGELOG |
| 🧱 Reproducibility | Deterministic output + hashes |
| 📦 Standards | GeoJSON · COG · STAC 1.0 |
| 🧬 Provenance | DVC hash + SLSA attestation |
| 🕵️ Auditability | CI logs · SBOM · Artifacts |
| 🔢 Versioning | SemVer across domains |
| ⚙️ Automation | pre-commit · docs · ai-model |
| 🛡 Security | CodeQL · Trivy · OPA |

---

## 🧾 Data Lineage
☐ `data/sources/*.json` updated ☐ `derived_from` verified  
☐ Checksums (`make checksums`) ☐ DVC metadata synced  

---

## 🧪 QA & Validation
```bash
pre-commit run --all-files
make stac-validate
make checksums
make sbom
make site && open _site/index.html
make ai-model-test   # if AI modified
```

---

## 📌 Artifacts
| Artifact | Path |
|:--|:--|
| Logs | `data/work/logs/...` |
| Checksums | `data/checksums/...` |
| STAC Items | `data/stac/...` |
| SBOM | `artifacts/sbom/sbom.json` |
| Provenance | `artifacts/prov/build.prov.json` |
| Thumbnails | `data/processed/metadata/.../thumbs/` |
| Screenshots | *(Attach below or link)* |

---

## ♿ Accessibility (UI Changes)
| Check | Status |
|:--|:--:|
| Keyboard Nav | ☑ |
| Contrast ≥ 4.5:1 | ☑ |
| ARIA Labels | ☑ |
| Motion Pref | ☑ |
| Screen Reader | ☑ |

---

## 🔐 Security & Licensing
| Check | Status |
|:--|:--:|
| SBOM Regenerated | ☑ |
| SLSA Signed | ☑ |
| No New CVEs | ☑ |
| Actions Pinned | ☑ |
| OPA Checks Passed | ☑ |
| License Valid | ☑ |
| Secrets Scan OK | ☑ |

---

## 💥 Breaking Changes (if any)
| Component | Description | Migration |
|:--|:--|:--|
| API | `/v1/events → /v2/events` | See `docs/api_migration.md` |
| Data | STAC schema refactor | `make hydro` |
| Web | Map layer rename | `web/config/layers.json` |
| Model | NER update | Update model card v2.1.0 |

---

## 🧭 Reviewer Checklist
| Check | ✓ |
|:--|:--:|
| Version + Changelog present | ☑ |
| STAC + CI passed | ☑ |
| SBOM + Provenance verified | ☑ |
| Artifacts archived | ☑ |
| CODEOWNERS approved | ☑ |

---

## 🕓 Version History
| Ver | Date | Author | Summary |
|:--|:--|:--|:--|
| **v3.0.0** | 2025-10-20 | @kfm-architecture | Rebuilt template · added accessibility + QA matrix + data lineage |
| v2.5.0 | 2025-10-18 | Core Docs Team | Added SBOM/SLSA & AI policy lint |
| v2.4.0 | 2025-10-16 | Docs Team | Accessibility checks added |
| v2.3.1 | 2025-10-15 | Maintainers | MCP-DL alignment |
| v2.2.0 | 2025-10-14 | Core Team | Lineage & checksum QA |
| v2.0.0 | 2025-10-10 | Maintainers | SemVer + Changelog introduced |

---

<div align="center">

**Kansas Frontier Matrix** — “Every PR leaves a trail · Every trail leaves a version.”  
This template enforces **provenance · reproducibility · auditability** across code, data, docs, and AI pipelines.

</div>

<!-- MCP-FOOTER-BEGIN
MCP-VERSION: v6.3.2
MCP-TIER: Ω+∞
DOC-PATH: .github/PULL_REQUEST_TEMPLATE.md
DOC-HASH: sha256:pr-template-v3-0-0-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
MCP-CERTIFIED: true
VALIDATION-HASH: {auto.hash}
GENERATED-BY: KFM-Automation/DocsBot
LAST-VALIDATED: {build.date}
MCP-FOOTER-END -->
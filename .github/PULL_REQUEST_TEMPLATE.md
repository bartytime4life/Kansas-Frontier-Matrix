<div align="center">

# 🚀 Kansas Frontier Matrix — Pull Request Template  

**Path:** `.github/PULL_REQUEST_TEMPLATE.md`  
**Purpose:** Ensure every change is **documented · reproducible · versioned · validated · auditable** under the  
**Master Coder Protocol (MCP)** · **Semantic Versioning (SemVer)** · **KFM Governance Standards**

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../.github/workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../.github/workflows/trivy.yml)
[![Pre-Commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen.svg)](https://pre-commit.com/)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue.svg)](../docs/)
[![License MIT](https://img.shields.io/badge/License-MIT-green.svg)](../LICENSE)

</div>

---

```yaml
---
template: "KFM Pull Request Template"
version: "v2.3.0"
last_updated: "2025-10-15"
authors: ["@bartytime4life", "@kfm-architecture", "@kfm-dataops"]
reviewers_required: 2
semver:
  bump: "auto-detect"
  allowed: ["patch","minor","major"]
mcp:
  validation_required: true
  provenance_required: true
security:
  actions_pinned: true
  codeql_scan: true
  trivy_scan: true
license: "MIT | CC-BY 4.0"
---


⸻

🧩 Summary

Describe what this PR changes and why — motivation + measurable outcomes.

Example: Adds STAC Items for NOAA Climate (2020-2024) and updates web/config/layers.json.

⸻

🔄 Linked Issues / Discussions

Type	Reference	Notes
🧾 Issue	Closes # …	
💬 Discussion	# …	Context / background
📘 ADR	docs/adr/ADR-####-<title>.md	Architecture Decision Record


⸻

🧠 Type of Change

Option	Description
🐛 Bug Fix	Resolve reproducible issue
💡 Feature / Enhancement	New functionality / workflow
🗃️ Dataset / Integration	New source · manifest · STAC metadata
📖 Documentation Update	READMEs · guides · ADRs
⚙️ CI/CD / Workflow	Automation · pre-commit
🔒 Security / Validation	CVE fix · checksum · SBOM
🧹 Refactor / Cleanup	Readability · structure
💥 Breaking Change	API / schema migration required


⸻

🧮 Implementation Summary

Field	Description
Affected Dirs	data/processed/hydro/ · src/pipelines/
New Files	Scripts · datasets · metadata (relative paths)
Deps Updated	pip / Node · Action pins
Validation	STAC · schema · unit/integration tests
Compatibility	Maintained / broken (see notes)
Scope	≈ X files · Y insertions · Risk Low / Med / High
Rollback Plan	Tag · cleanup · data revert
Migration	Steps to rebuild data if schema changed


⸻

🧭 Versioning (SemVer)

Domain	Change	New Version
Repo Overall	Minor feature add	vX.Y.Z → vX.Y+1.Z
API	Endpoint update	v1.3 → v1.4
Web UI	UI toggle changes	v1.1 → v1.2
Data STAC	Metadata update	v1.0.0 → v1.1.0

Release Checklist
	•	CHANGELOG updated
	•	STAC properties.version bumped
	•	Tag GitHub release vX.Y.Z
	•	Attach STAC/SBOM/SARIF artifacts
	•	Notify Maintainers via Release Notes

⸻

📜 Changelog (Sample)

### Added
- NOAA Climate 2020-2024 STAC Items · map integration  

### Changed
- Reprojected `soil_survey_1967` → EPSG:4326  
- Modularized `terrain_pipeline.py`  

### Fixed
- Hydrology accumulation bug (D8 step)  

### Security
- Pinned `actions/setup-node@v4` · SBOM regen · Trivy passed


⸻

✅ MCP / CI Compliance

Principle	Verification
📖 Documentation	READMEs · STAC · CHANGELOG
🧮 Reproducibility	Deterministic pipelines + checksums
🌐 Open Standards	COG · GeoJSON · CSV/JSON · NetCDF
🧾 Provenance	Source · License · STAC lineage
🕵️ Auditability	CI logs + artifacts (≥ 90 days)
🔢 Versioning	SemVer applied to all domains


⸻

🔍 Provenance / Data Lineage
	•	data/sources/*.json updated (URL + license + last_verified)
	•	Added STAC derived_from / dependencies fields
	•	Checksums verified → data/checksums/<domain>/

⸻

🧰 Validation Commands

make stac-validate
make hydro
make checksums
pre-commit run --all-files
make site && open _site/index.html


⸻

📎 Artifacts / Attachments

Type	Path / Link
Logs	data/work/logs/<domain>_etl_debug.log
Checksums	data/checksums/<domain>/*.sha256
STAC Items	data/stac/<domain>/*.json
Visuals	data/processed/metadata/<domain>/thumbs/
Screenshots	Attach below


⸻

🧪 Testing / QA

Item	Result
Coverage	%
Performance Impact	Minimal / Improved / N A
Manual Steps	1️⃣ …  2️⃣ …


⸻

♿ Accessibility (UI Changes)

Check	Status
Keyboard Navigation	☑
Color Contrast ≥ 4.5:1	☑
ARIA Labels / Roles	☑
Reduced Motion Pref	☑


⸻

🔒 Security / License Review

Audit Item	Status
SBOM Updated	☑
No new CVEs (CodeQL / Trivy)	☑
License Compliance	☑
Secrets Scan / OIDC	☑
Actions Pinned (no @latest)	☑

Mini Audit Summary: All Actions pinned ✔  ·  No plaintext secrets ✔  ·  OIDC deployments active ✔

⸻

💥 Breaking Changes

Component	Description	Migration / Mitigation
API	/api/v1/events → /api/v2/events	See docs/api_migration.md
Dataset	Hydrology schema refactor	make hydrology
Web Layer	Map config rename	Update layers.json


⸻

🧾 Reviewer Checklist

#	Action	Done
1	Verify version: headers updated	☐
2	Check CHANGELOG / STAC versions	☐
3	Ensure release tag created	☐
4	Confirm CI green	☐
5	Approve and merge	☐


⸻

🧭 Validation Flow

flowchart TD
  A["Open PR"] --> B["Pre-Commit + Tests"]
  B --> C["STAC / Schema Validation"]
  C --> D["Security (CodeQL + Trivy)"]
  D --> E["Version Sync (SemVer / STAC)"]
  E --> F["Review & Merge"]
  F --> G["Release Tag + Artifact Archive"]
%% END OF MERMAID


⸻

🕓 Version History

Version	Date	Author	Summary
v2.3.0	2025-10-15	KFM Maintainers	Polished tables · visual layout enhancement
v2.2.0	2025-10-14	KFM Maintainers	MCP-DL v6.2 alignment · checksum field
v2.1.0	2025-10-13	Core Docs	Risk / rollback enhancements
v2.0.0	2025-10-10	Architecture Team	SemVer integration
v1.0.0	2025-07-01	Project Launch	Initial template release


⸻


<div align="center">


🧭 Kansas Frontier Matrix

“Every Pull Request Builds the Past, Present, and Future — Versioned Forever.”

</div>
```
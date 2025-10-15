<div align="center">

# 🚀 Kansas Frontier Matrix — Pull Request Template  
**Path:** `.github/PULL_REQUEST_TEMPLATE.md`  

**Purpose:** Enforce **traceable, reproducible, versioned, validated, and auditable** development under the  
**Master Coder Protocol (MCP)**, **FAIR** principles, and **KFM governance**.

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
template: "Kansas Frontier Matrix Pull Request Template"
version: "v2.2.0"
last_updated: "2025-10-15"
authors: ["@bartytime4life", "@kfm-architecture", "@kfm-dataops"]
status: "Stable"
maturity: "Production"
semver:
  bump: "auto-detect"
  allowed: ["patch","minor","major"]
  changelog_required: true
governance:
  reviewers_required: 2
  codeowners_check: true
security:
  actions_pinned: true
  trivy_scan_required: true
  codeql_scan_required: true
mcp:
  validation_required: true
  provenance_required: true
fair:
  findable: true
  accessible: true
  interoperable: true
  reusable: true
ontology:
  aligns_with: ["CIDOC CRM:E7_Activity","W3C PROV:Activity","OWL-Time:Interval"]
integrity:
  checksum_sha256: "<insert-after-merge>"
license: "MIT | CC-BY 4.0"
---

<!-- Reviewers: link related ADRs for design decisions requiring architectural sign-off. -->




⸻

🧩 Summary

Describe what this PR does and why.
Include measurable outcomes and relevant hypotheses (per MCP experiment format).

Example:
Adds STAC Items for NOAA Climate (2020-2024), refreshes checksums, and updates web/config/layers.json.

⸻

🔄 Related Issues / Discussions
	•	Closes # …
	•	Related # …
	•	Discussion …
	•	Milestone …
	•	ADR → docs/adr/ADR-####-<title>.md

⸻

🧠 Type of Change (select all that apply)
	•	🐛 Bug Fix — reproducible issue resolved
	•	💡 Feature / Enhancement — new functionality or workflow improvement
	•	🗃️ Dataset Integration — new source / manifest / STAC metadata
	•	🧩 Metadata Update — schema or documentation correction
	•	📖 Documentation Update — READMEs / guides / ADRs
	•	⚙️ CI/CD Workflow — automation / linting / governance
	•	🔒 Security / Validation — CVE mitigation / checksum update / SBOM
	•	🧹 Refactor / Cleanup — structural / naming improvements
	•	💥 Breaking Change — API or schema change (requires migration section)

⸻

🧮 Implementation Details

Field	Description
Affected Directories	e.g. data/processed/hydro/, src/pipelines/
New Files Added	scripts / datasets / metadata (relative paths)
Dependencies Updated	pip/Node locks + Action pins
Validation Performed	STAC + schema validated, tests pass
Backward Compatibility	maintained / intentionally broken
Versioning Impact	see SemVer section
Size / Scope	X files changed · Y insertions · Risk Low/Med/High
Rollback Plan	how to revert (tag + cleanup)
Data Migration	rebuild / rehydrate instructions


⸻

🧭 Versioning Summary (SemVer Alignment)

Scope	Proposed Version	Reason / Impact
Repo Overall	vX.Y.Z → vX.Y+1.Z	Added new datasets / pipelines
API	v1 → v2 or v1.3 → v1.4	Endpoint change
Web UI	v1.1 → v1.2	Layer / UI updates
Data STAC	v1.0.0 → v1.1.0	Metadata schema update

Tag Checklist
	•	CHANGELOG updated
	•	STAC Item properties.version bumped
	•	Git Release tag vX.Y.Z created
	•	Artifacts (SARIF/STAC/SBOM) attached
	•	Maintainers notified via Release Notes

⸻

📜 Changelog (Keep a Changelog)

### Added
- NOAA Climate 2020-2024 STAC items + map integration.

### Changed
- Re-projected `soil_survey_1967` → EPSG:4326.  
- Modularized `terrain_pipeline.py`.

### Fixed
- Hydrology accumulation bug in WhiteboxTools D8.

### Security
- Pinned `actions/setup-node@v4` · SBOM regenerated · Trivy scan passed.


⸻

✅ MCP + CI/CD Compliance

MCP Principle	Verification
Documentation	READMEs / STAC metadata / CHANGELOG
Reproducibility	deterministic pipelines + checksums
Open Standards	COG · GeoJSON · CSV/JSON · NetCDF
Provenance	source · license · checksum · STAC lineage
Auditability	CI logs + artifacts retained ≥ 90 days
Versioning	Semantic versions synced across domains


⸻

🔍 Provenance / Data Lineage
	•	data/sources/*.json updated (source URL + license + last_verified)
	•	STAC derived_from / dependencies fields added
	•	Checksums verified under data/checksums/<domain>/

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
Screenshots	attach below


⸻

🧪 Testing / QA Notes
	•	Coverage … %
	•	Manual steps →
	1.	…   2. …
	•	Performance impact → minimal / improved / N A

⸻

♿ Accessibility (If UI Changes)
	•	Keyboard navigation verified
	•	Color contrast ≥ 4.5:1
	•	ARIA labels/roles validated
	•	prefers-reduced-motion honored

⸻

🔒 Security / License Review
	•	SBOM updated  (tools/sbom)
	•	No new CVEs (CodeQL + Trivy)
	•	Dataset license compliance verified
	•	No plaintext secrets (committed)
	•	All Actions pinned (no @latest)

Mini Audit — Pins ✔ · Secrets 🔐 · OIDC ✅

⸻

💥 Breaking Changes

Component	Description	Migration / Mitigation
API	/api/v1/events → /api/v2/events	see docs/api_migration.md
Dataset	hydrology refactor	make hydrology
Web UI	layer config renamed	update layers.json


⸻

🧾 Reviewer Versioning Checklist

#	Action	Status
1	Confirm version: headers bumped	☐
2	CHANGELOG + STAC versions synced	☐
3	Release tag vX.Y.Z created	☐
4	CI/CD green	☐
5	Approve + merge	☐


⸻

🧭 PR Validation Flow

flowchart TD
  A["Open PR"] --> B["Pre-Commit + Tests"]
  B --> C["STAC / Schema Validate"]
  C --> D["Security Scans (CodeQL + Trivy)"]
  D --> E["Version Sync ( SemVer / STAC )"]
  E --> F["Review + Merge"]
  F --> G["Release Tag + Artifact Archive"]
%% END OF MERMAID


⸻

📊 Release Notes (Preview)
	•	Add NOAA Climate 2020-2024 STAC layers
	•	Change CRS metadata for soil_survey_1967
	•	Security Pin actions/setup-node@v4 · SBOM attached

⸻

🕓 Version History

Version	Date	Author	Summary
v2.2.0	2025-10-15	KFM Maintainers	MCP-DL v6.2 upgrade · FAIR fields added
v2.1.0	2025-10-13	KFM Maintainers	Risk / rollback enhancements
v2.0.0	2025-10-10	KFM Maintainers	SemVer integration
v1.4.0	2025-09-15	Core Docs	Enhanced template for MCP compliance
v1.0.0	2025-07-01	Project Launch	Initial PR governance template


⸻


<div align="center">


🧭 Kansas Frontier Matrix

“Every Pull Request builds the Past, Present, and Future — Versioned Forever.”

</div>
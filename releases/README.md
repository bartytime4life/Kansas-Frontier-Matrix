---
title: "KFM Releases"
path: "releases/README.md"
version: "v1.0.0"
last_updated: "2025-12-21"
status: "draft"
doc_kind: "Guide"
license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v11.0.0"
dcat_profile: "KFM-DCAT v11.0.0"
prov_profile: "KFM-PROV v11.0.0"

governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:releases:readme:v1.0.0"
semantic_document_id: "kfm-releases-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:releases:readme:v1.0.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# KFM Releases

## 📘 Overview

### Purpose

- Provide a **single, versioned home** for KFM release bundles (artifacts intended for distribution, audit, and reproducibility).
- Standardize what gets stored in `releases/` (e.g., manifests, SBOMs, signed bundles, telemetry snapshots) and how those artifacts link back to the canonical KFM pipeline outputs.

### Scope

| In Scope | Out of Scope |
|---|---|
| Versioned release bundles under `releases/<version>/` | Day-to-day working outputs (use `data/work/`), raw ingest sources (use `data/raw/` / `data/sources/`) |
| Release manifests, SBOMs, signatures, checksums | Secrets/credentials, signing private keys, or any PII |
| Documentation snapshots and sample exports tied to a release | Ad-hoc exports not tied to a versioned run |
| Telemetry snapshots that are schema-governed and non-sensitive | Unreviewed sensitive datasets or restricted-location material |

### Audience

- Primary: Release managers / maintainers, DataOps, CI/CD maintainers
- Secondary: Auditors, downstream integrators, curators, researchers consuming packaged releases

### Definitions (link to glossary)

- Link: `docs/glossary.md` (if not present, add via governance process)
- Terms used in this doc:
  - **Release bundle:** A versioned collection of KFM artifacts intended to be reproducible.
  - **Release manifest:** A machine-readable index of artifacts, checksums, and provenance pointers.
  - **SBOM:** “Software Bill of Materials” for the release build and its dependencies.
  - **Telemetry snapshot:** A versioned capture of selected operational/quality signals (schema-governed).

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Release directory | `releases/` | Maintainers | Top-level home for release bundles |
| Versioned bundle | `releases/<version>/` | Maintainers | One folder per release version |
| Release manifest | `releases/<version>/release-manifest.*` | Maintainers | Filename/format TBD; must be machine-readable |
| SBOM | `releases/<version>/sbom.*` | Maintainers | Format TBD (SPDX or CycloneDX) |
| Checksums | `releases/<version>/checksums.sha256` | Maintainers | Strongly recommended for all artifacts |
| Signatures | `releases/<version>/signatures/` | Maintainers | Signing mechanism/tooling TBD |
| Telemetry snapshot | `releases/<version>/telemetry/` | Maintainers | Only non-sensitive, schema-validated snapshots |
| Docs snapshot | `releases/<version>/docs-snapshot/` | Maintainers | Optional: frozen docs used for the release |
| Sample exports | `releases/<version>/exports/` | Maintainers | Optional: curated “sample exports” for validation demos |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] `releases/` purpose and boundaries are clear (what belongs here vs. elsewhere)
- [ ] A versioned bundle layout is defined (even if some fields remain “TBD”)
- [ ] Validation + governance expectations are explicit (esp. sensitivity and provenance)

## 🗂️ Directory Layout

### This document

- `path`: `releases/README.md` (must match front-matter)

### Expected layout (recommended)

> Note: exact filenames and formats for manifests/SBOM/signatures may be finalized by governance; placeholders below support consistent organization now.

~~~text
📁 releases/
├── 📄 README.md
└── 📁 <version>/
    ├── 📄 release-manifest.<json|yaml>        # index + provenance pointers
    ├── 📄 sbom.<spdx|cdx|json>                # SBOM (format TBD)
    ├── 📄 checksums.sha256                    # checksums for artifacts
    ├── 📁 signatures/                         # detached signatures (tooling TBD)
    │   └── 📄 <artifact>.sig
    ├── 📁 catalogs/                           # optional snapshots/pointers
    │   ├── 📁 stac/
    │   ├── 📁 dcat/
    │   └── 📁 prov/
    ├── 📁 docs-snapshot/                      # optional frozen docs
    ├── 📁 exports/                            # optional sample exports
    └── 📁 telemetry/                          # optional telemetry snapshots
~~~

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed outputs (canonical data) |
| STAC | `data/stac/` | STAC catalogs (canonical) |
| DCAT | `data/catalog/dcat/` | DCAT outputs (canonical) |
| PROV | `data/prov/` | Provenance bundles (canonical) |
| Documentation | `docs/` | Canonical governed docs |
| Schemas | `schemas/` | JSON schemas (telemetry, catalogs, etc.) |
| CI/CD | `.github/workflows/` | Validation and release automation |

## 🧭 Context

### What “release” means in KFM

A **KFM release** is a *versioned snapshot of outputs* intended to be:
- reproducible (re-runnable from pinned inputs/config + recorded lineage),
- auditable (clear checksums + provenance pointers),
- safe to distribute (no restricted/secret material).

**Important boundary:** `releases/` is for *packaging and distribution*, not as the canonical source of truth for datasets or catalogs.

## 📦 Data & Metadata

### What may be included in a release bundle

A release bundle may contain (or point to) the artifacts below:
- **Manifests** that enumerate exactly what is in the bundle and where it came from.
- **SBOMs** describing the build’s software dependency graph.
- **Signed bundles / signatures** for integrity verification (mechanism TBD).
- **Telemetry snapshots** used for quality and reproducibility checks.
- **Documentation snapshots, run manifests, and sample exports** (if the project chooses to freeze these alongside a release).

## 🌐 STAC, DCAT & PROV Alignment

### Provenance requirements (release bundle level)

Release artifacts should link back to:
- STAC collection/item identifiers for published datasets
- DCAT dataset identifiers/mappings (where applicable)
- PROV activity/run identifiers and upstream sources

### Versioning expectations

- Each `releases/<version>/` folder should represent **one coherent versioned bundle**.
- If a new release supersedes another, the relationship should be recorded in the manifest and/or PROV lineage.

## 🧱 Architecture

### Release bundle as the “distribution edge” of the pipeline

~~~mermaid
flowchart LR
  A[ETL outputs] --> B[STAC/DCAT/PROV catalogs]
  B --> C[Graph build]
  C --> D[API layer]
  D --> E[UI + Story Nodes]
  B --> F[Release packaging]
  F --> G[releases/<version>/ bundle]
~~~

### Manifest contract (recommended shape)

> Format and schema are **TBD** (not confirmed in repo). The example below illustrates the minimum intent.

~~~json
{
  "release_version": "vX.Y.Z",
  "commit_sha": "<latest-commit-hash>",
  "generated_at": "YYYY-MM-DDTHH:MM:SSZ",
  "pipeline_contract_version": "KFM-PPC v11.0.0",
  "artifacts": [
    {
      "path": "catalogs/stac/...",
      "type": "stac",
      "sha256": "<checksum>",
      "notes": "Snapshot or pointer (define policy)."
    },
    {
      "path": "sbom.json",
      "type": "sbom",
      "sha256": "<checksum>"
    }
  ],
  "provenance": {
    "prov_bundle_path": "catalogs/prov/...",
    "run_id": "prov:activity:<id>"
  }
}
~~~

## 🧠 Story Node & Focus Mode Integration

- If a release includes Story Nodes (or Focus Mode bundles), they must remain **provenance-linked** and safe to render.
- Any predictive/AI-derived content (if shipped at all) should be clearly labeled and carry uncertainty/confidence metadata.

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks (front-matter keys, paths)
- [ ] Schema validation for any included catalogs (STAC/DCAT/PROV snapshots)
- [ ] Checksums computed and stored for included artifacts
- [ ] Signature verification process documented (if signatures are used)
- [ ] Security and sovereignty checks applied to any distributable artifacts

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands
# 1) validate schemas (STAC/DCAT/PROV)
# 2) run pipeline tests / integrity checks
# 3) generate release manifest + checksums
# 4) (optional) sign artifacts + verify signatures
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| TBD | TBD | `releases/<version>/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates

- If a release bundle includes new public-facing datasets, new telemetry, or any sensitivity-affecting changes, route through the appropriate governance review.
- If sovereignty constraints apply to any data domain, ensure distribution contents comply with `docs/governance/SOVEREIGNTY.md`.

### CARE / sovereignty considerations

- Do not distribute restricted locations, culturally sensitive knowledge, or other protected content without explicit approvals and the required redaction/generalization rules.

### AI usage constraints

- Ensure this doc’s AI permissions/prohibitions match intended use.
- Do not treat release packaging documentation as permission to generate or infer policies.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-21 | Initial `releases/` README scaffold | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`


---
title: "KFM Releases"
path: "releases/README.md"
version: "v1.0.1"
last_updated: "2025-12-28"
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

doc_uuid: "urn:kfm:doc:releases:readme:v1.0.1"
semantic_document_id: "kfm-releases-readme-v1.0.1"
event_source_id: "ledger:kfm:doc:releases:readme:v1.0.1"
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

- Provide a **single, versioned home** for KFM **release bundles**: artifacts packaged for distribution, verification, audit, and reproduction.
- Enable downstream consumers (including institutional partners and auditors) to verify they have **exactly** what was reviewed and approved (via checksums and, when used, signatures/attestations).
- Keep release packaging aligned to KFM’s canonical ordering:

  **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

- Enforce the “one canonical home per subsystem” rule: `releases/` is the **distribution edge**, not a second copy of canonical data/catalog/code.

### Scope

| In Scope | Out of Scope |
|---|---|
| Versioned bundles under `releases/<version>/` | Day-to-day working outputs (use `data/work/<domain>/`) |
| Release manifest + checksums for all shipped artifacts | Raw ingest sources (use `data/raw/<domain>/` and/or `data/sources/` if present) |
| Optional SBOM(s) and optional signatures/attestations | Secrets/credentials/private keys; unredacted PII |
| Optional snapshots for offline audit (catalogs/docs/exports) when explicitly chosen per release | Unreviewed sensitive datasets, restricted locations, or culturally sensitive knowledge without approvals and required redaction/generalization |
| Telemetry snapshots that are schema-governed, non-sensitive, and reviewable | Unbounded logs, raw traces, or telemetry containing identifiers/PII |

### Audience

- Primary: Release managers / maintainers, DataOps, CI/CD maintainers
- Secondary: Auditors, downstream integrators, curators, researchers consuming packaged releases

### Definitions

- Glossary: `docs/glossary.md` (**not confirmed in repo** — update this link if the glossary lives elsewhere)

Terms used in this document:

- **Release bundle**: A versioned collection of artifacts intended to be **verifiable**, **reproducible**, and **safe to distribute**.
- **Release manifest**: Machine-readable index of bundle contents (paths, digests, media types) plus pointers back to provenance and contracts.
- **Run manifest**: Machine-readable summary of the pipeline run(s) used to produce released artifacts (may live in `data/prov/` and/or in the release bundle).
- **SBOM**: Software Bill of Materials for the code/build environment used to generate release artifacts.
- **Attestation**: A verifiable statement binding a build/run to specific artifact digests (e.g., SLSA provenance).
- **Telemetry snapshot**: A curated capture of CI/quality signals used to validate or reproduce a release (schema-governed, non-sensitive).

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Release directory | `releases/` | Maintainers | Home for release bundles (**distribution edge**) |
| This guide | `releases/README.md` | Maintainers | Governs what “belongs” under `releases/` |
| Versioned bundle | `releases/<version>/` | Maintainers | One folder per release version tag |
| Release notes | `releases/<version>/RELEASE_NOTES.md` | Maintainers | Recommended summary + known issues (filename **not confirmed in repo**) |
| Release manifest | `releases/<version>/release-manifest.json` | Maintainers | **Required**; schema recommended (**not confirmed in repo**) |
| Checksums | `releases/<version>/checksums.sha256` | Maintainers | **Required**; must cover **all shipped files** |
| SBOM | `releases/<version>/sbom.*` | Maintainers | Recommended: SPDX JSON or CycloneDX JSON |
| Signatures | `releases/<version>/signatures/` | Maintainers | Optional; detached signatures for critical artifacts |
| Attestations | `releases/<version>/attestations/` | Maintainers | Optional; build/run provenance attestations (tooling TBD) |
| Run manifest | `releases/<version>/run-manifest.json` | Pipelines / Maintainers | Optional; may instead be referenced from `data/prov/` |
| Telemetry snapshot | `releases/<version>/telemetry/` | Maintainers | Optional; schema-validated + non-sensitive only |
| Catalog snapshots | `releases/<version>/catalogs/` | Maintainers | Optional; snapshot vs pointer policy must be explicit |
| Docs snapshot | `releases/<version>/docs-snapshot/` | Maintainers | Optional; frozen docs used for this release |
| Sample exports | `releases/<version>/exports/` | Maintainers | Optional; curated samples for demos/validation |

### Definition of done

This README is considered complete when:

- [ ] Front-matter is complete and valid (protocol versions + identifiers + checksum placeholder present)
- [ ] `releases/` purpose and boundaries are explicit (what belongs here vs. canonical data/catalog locations)
- [ ] A **minimum required bundle** is defined (manifest + checksums, with clear rules)
- [ ] Validation + governance expectations are explicit (esp. sensitivity, provenance, reproducibility)
- [ ] Paths match the v12 Master Guide repo layout where confirmed; any uncertainty is marked **not confirmed in repo**

---

## 🗂️ Directory Layout

### This document

- `path`: `releases/README.md` (must match front-matter)

### Related repository paths

| Area | Canonical path | What lives here |
|---|---|---|
| Sources | `data/sources/` | Source bundles “as received” (licenses, checksums, original packages) (**if present**) |
| Raw data | `data/raw/<domain>/` | Raw inputs (no edits; provenance anchors) |
| Working data | `data/work/<domain>/` | Intermediate outputs; not distributable by default |
| Processed data | `data/processed/<domain>/` | Published/derived datasets (distribution candidates) |
| STAC | `data/stac/{collections,items}/` | Canonical STAC catalogs |
| DCAT | `data/catalog/dcat/` | Canonical DCAT outputs |
| PROV | `data/prov/` | Canonical provenance bundles (per run / per dataset) |
| Graph ingest | `data/graph/` | Import fixtures (CSV/Cypher) if used (**not confirmed in repo**) |
| ETL / pipelines | `src/pipelines/` | Deterministic transforms; write outputs to `data/**` |
| Graph code | `src/graph/` | Ontology + ingest logic (no UI access) |
| API boundary | `src/server/` | REST/GraphQL APIs + redaction/generalization |
| API contracts | `src/server/contracts/` | Contracts + contract tests (**if present**) |
| UI | `web/` | React/Map UI; must not query Neo4j directly |
| Story Nodes | `docs/reports/story_nodes/` | Draft/published Story Nodes and assets |
| Schemas | `schemas/` | JSON Schema constraints (STAC/DCAT/PROV/story/ui/telemetry) |
| Runs & experiments | `mcp/runs/` / `mcp/experiments/` | Run logs, experiment artifacts (if used) |
| Tools | `tools/` | Validators, QA scripts, release helpers (if present) |
| Tests | `tests/` | Unit + integration tests |
| CI | `.github/` | Workflows + policy gates |

### Expected layout (recommended)

> Note: exact filenames and formats for manifests/SBOM/signatures/attestations may be finalized by governance. The structure below keeps organization stable even as formats evolve.

~~~text
📁 releases/
├── 📄 README.md
└── 📁 vX.Y.Z/
    ├── 📄 RELEASE_NOTES.md                   # RECOMMENDED (filename not confirmed in repo)
    ├── 📄 release-manifest.json              # REQUIRED: machine index (paths + digests + provenance pointers)
    ├── 📄 checksums.sha256                   # REQUIRED: sha256 for ALL shipped files
    ├── 📄 sbom.spdx.json                     # RECOMMENDED: SPDX JSON (or sbom.cdx.json)
    ├── 📄 run-manifest.json                  # OPTIONAL: pipeline run summary (or reference data/prov/)
    ├── 📁 signatures/                        # OPTIONAL: detached signatures (mechanism TBD)
    │   ├── 📄 release-manifest.json.sig
    │   ├── 📄 checksums.sha256.sig
    │   └── 📄 <artifact>.sig
    ├── 📁 attestations/                      # OPTIONAL: build/run provenance attestations (tooling TBD)
    │   ├── 📄 release.slsa.json
    │   └── 📄 <artifact>.slsa.json
    ├── 📁 catalogs/                          # OPTIONAL: snapshot copies for offline audit OR structured pointers
    │   ├── 📁 stac/
    │   ├── 📁 dcat/
    │   └── 📁 prov/
    ├── 📁 docs-snapshot/                     # OPTIONAL: frozen docs used for the release
    ├── 📁 exports/                           # OPTIONAL: curated samples for demos/validation
    └── 📁 telemetry/                         # OPTIONAL: schema-governed, non-sensitive snapshots
~~~

---

## 🧭 Context

### Background

Releases exist to solve a predictable downstream problem: **“Which exact set of artifacts was reviewed, validated, and approved?”**  
Without a bundle + manifest + digests, consumers are forced to trust moving targets (branch heads, regenerated catalogs, or unpinned artifacts).

A KFM release bundle provides an auditable “snapshot of intent” that binds:

- the producing commit (`commit_sha`),
- the produced artifacts (via `sha256` digests),
- and the evidence chain (STAC/DCAT/PROV pointers, run IDs).

### Assumptions

- Release bundles are **optional** (“if used”) and should remain **lightweight** by default (pointer mode).
- Any snapshot-mode bundle must remain **verbatim** with canonical artifacts and must still be digest-verified.
- Governance may require additional artifacts (SBOM/signature/attestation) depending on distribution context.

### Constraints / invariants

- Canonical ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**.
- `releases/` is packaging only; canonical artifacts remain in `data/`, `src/`, `web/`, `docs/`, `schemas/`.
- UI must not read Neo4j directly; all access is through contracted APIs that enforce redaction/generalization.
- No sensitive leakage: release bundles must not contain unreviewed restricted locations, culturally sensitive knowledge, secrets, or unredacted PII.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Do we standardize a `schemas/releases/release-manifest.schema.json` and enforce it in CI? | TBD | TBD |
| Do we require SBOM for every release (or only public distribution)? | TBD | TBD |
| Do we adopt signing + verification tooling (and which mechanism)? | TBD | TBD |
| Do we allow snapshot-mode bundles by default, or only for auditor/offline needs? | TBD | TBD |

### Future extensions

- Release manifest schema under `schemas/releases/` (**not confirmed in repo**)
- Standard signing + verification tooling (documented and CI-verified)
- Telemetry schema + stable metrics under `schemas/telemetry/`
- Snapshot drift detection in CI (“snapshot matches canonical digests”)
- Attestation generation/verification gates (SLSA or equivalent)

---

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  A[ETL outputs<br/>data/{raw,work,processed}/<domain>] --> B[Catalogs<br/>data/stac + data/catalog/dcat + data/prov]
  B --> C[Graph build<br/>src/graph (+ optional data/graph fixtures)]
  C --> D[API boundary<br/>src/server]
  D --> E[UI<br/>web]
  E --> F[Story Nodes<br/>docs/reports/story_nodes]
  F --> G[Focus Mode<br/>provenance-linked only]
  B --> H[Release packaging<br/>releases/]
  H --> I[Release bundle<br/>releases/<version>/]
~~~

### Optional: release verification sequence

~~~mermaid
sequenceDiagram
  participant Consumer
  participant Release as Release bundle
  participant Canonical as Canonical artifacts (data/**, docs/**, etc.)

  Consumer->>Release: Fetch release-manifest.json + checksums.sha256
  Consumer->>Release: Verify checksums (and signatures/attestations if present)
  alt bundle_mode == snapshot
    Consumer->>Release: Use bundled copies under releases/<version>/
  else bundle_mode == pointer
    Consumer->>Canonical: Fetch canonical artifacts by path
  end
  Consumer->>Consumer: Verify sha256 digests match manifest
  Consumer->>Consumer: Proceed with audit / integration
~~~

---

## 📦 Data & Metadata

### What “release” means in KFM

A **release bundle** is the distribution edge of KFM. It packages *reviewed* artifacts so a downstream consumer can:

- verify integrity (checksums/signatures),
- verify provenance (PROV pointers / attestations),
- reproduce the build/run (pinned versions + run manifests),
- audit sensitivity compliance (explicitly non-sensitive public bundle).

**Important boundary:** `releases/` is for packaging and distribution. Canonical sources remain under:

- `data/**` (datasets and catalogs),
- `schemas/**` (validation contracts),
- `src/**` and `web/**` (code),
- `docs/**` (governed documentation).

Pipeline/catalog systems must not treat `docs/` as an output location for STAC/DCAT/PROV artifacts.

### Snapshot vs pointer policy

A release may be constructed in one of two valid modes:

1. **Pointer mode (default recommendation)**  
   Release manifest lists canonical artifact paths (e.g., `data/stac/...`) and their digests. The bundle itself contains only manifest + checksums (+ optional SBOM/signatures/attestations).

2. **Snapshot mode (auditor/offline distribution)**  
   Release bundle includes copies under `releases/<version>/catalogs/` and/or `docs-snapshot/`. Snapshotted copies must be exact copies of canonical artifacts and must still be referenced (and digest-verified) via the manifest.

The release manifest must declare which mode is used, to avoid ambiguity.

### What must never be included

- Secrets/credentials (tokens, keys, private signing material)
- Unredacted PII or personal contact details
- Restricted locations or culturally sensitive knowledge without explicit approvals and required generalization/redaction
- Any artifact that bypasses governance rules defined in `docs/governance/**`

---

## 🌐 STAC, DCAT & PROV Alignment

### Release-level provenance requirements

For every dataset/evidence product shipped (directly or by pointer), the release bundle must be able to link to:

- STAC Collection + Item(s)
- DCAT dataset record (minimum title/description/license/keywords)
- PROV activity describing lineage for the transform that generated the released artifact(s)

Additionally:

- Every pipeline run should emit a PROV activity bundle under `data/prov/`, and a run manifest (which may live in `data/prov/` or `releases/<version>/`).

### Versioning expectations

- Release folders should follow a stable tag pattern: `v<MAJOR>.<MINOR>.<PATCH>`.
- If a release supersedes another, record predecessor/successor linkage in the release manifest and ensure catalog/graph version lineage reflects it.

### What should be recorded in the release manifest

At minimum:

- `release_version`
- `commit_sha`
- `generated_at`
- `pipeline_contract_version` (and STAC/DCAT/PROV profile versions)
- `bundle_mode` (`pointer` or `snapshot`)
- a complete `artifacts[]` list with SHA256 digests
- `provenance` pointers (e.g., PROV bundle path(s) and run/activity IDs)

---

## 🧱 Architecture

### Release bundle as the distribution edge

Release packaging is the last-mile step that **must not mutate canonical artifacts**. It should only:

- enumerate outputs (manifest),
- bind digests (checksums),
- bind to provenance (PROV pointers / attestations),
- and (optionally) snapshot copies for offline audit.

### Subsystem contracts (release-aware)

| Subsystem | Contract artifacts | “Do not break” rule |
|---|---|---|
| ETL | configs + run logs + validation | deterministic, replayable |
| Catalogs | STAC/DCAT/PROV schemas + validators | machine-validated |
| Graph | ontology + migrations + constraints | stable labels/edges |
| APIs | OpenAPI/GraphQL schema + tests | backward compat or version bump |
| UI | layer registry + a11y + audit affordances | no hidden data leakage |
| Focus Mode | provenance-linked context bundle | no hallucinated sources |
| Releases | manifest + checksums + (optional) SBOM/signatures/attestations | verifiable, auditable, no sensitive leakage |

### Manifest contract (recommended shape)

> Format and schema are **TBD** (**not confirmed in repo**). The example below illustrates the minimum intent.

~~~json
{
  "release_version": "vX.Y.Z",
  "bundle_mode": "pointer",
  "commit_sha": "<latest-commit-hash>",
  "generated_at": "YYYY-MM-DDTHH:MM:SSZ",
  "pipeline_contract_version": "KFM-PPC v11.0.0",
  "profiles": {
    "stac_profile": "KFM-STAC v11.0.0",
    "dcat_profile": "KFM-DCAT v11.0.0",
    "prov_profile": "KFM-PROV v11.0.0"
  },
  "artifacts": [
    {
      "path": "checksums.sha256",
      "type": "checksum",
      "sha256": "<checksum>"
    },
    {
      "path": "sbom.spdx.json",
      "type": "sbom",
      "sha256": "<checksum>"
    },
    {
      "path": "data/stac/collections/<collection>.json",
      "type": "stac",
      "sha256": "<checksum>",
      "notes": "Pointer-mode: canonical path + digest; snapshot-mode: also copied under releases/<version>/catalogs/stac/."
    }
  ],
  "provenance": {
    "prov_bundle_paths": [
      "data/prov/<run_or_dataset_bundle>.json"
    ],
    "run_id": "prov:activity:<id>"
  }
}
~~~

---

## 🧩 Extension points checklist (for future work)

- [ ] Data: new domain added under `data/{raw,work,processed}/<domain>/...`
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

---

## 🧠 Story Node & Focus Mode Integration

- If a release includes Story Nodes (or Focus Mode bundles), they must remain **provenance-linked** and safe to render.
- Focus Mode must only consume provenance-linked context; any predictive/AI-generated content must be:
  - opt-in,
  - clearly marked,
  - accompanied by uncertainty/confidence metadata,
  - never presented as unmarked fact.
- The UI must not read Neo4j directly; access is mediated by the API boundary, which enforces redaction/generalization.

---

## 🧪 Validation & CI/CD

### Minimum validation checklist (release bundle)

- [ ] Markdown protocol checks (front-matter keys, `path`, required sections)
- [ ] Release manifest is present and lists **every shipped artifact**
- [ ] `checksums.sha256` covers all shipped artifacts and matches actual digests
- [ ] Snapshot drift check (if snapshot-mode): snapshotted files match canonical digests
- [ ] Schema validation for included catalogs (STAC/DCAT/PROV) when snapshot-mode is used
- [ ] Provenance pointers resolve (PROV bundle paths + run/activity IDs exist and are consistent)
- [ ] SBOM generated (if required by policy) and included in checksums
- [ ] Signature verification process documented (if signatures are used)
- [ ] Attestation verification process documented (if attestations are used)
- [ ] Security and sovereignty checks applied to distributable artifacts

### CI mapping (system-wide alignment)

Release packaging should not bypass the system’s standard CI gates, including:

- Markdown protocol validation
- Link/reference checks (no orphan pointers)
- JSON schema validation (STAC/DCAT/PROV/telemetry as applicable)
- Graph integrity tests (when graph fixtures are included)
- API contract tests (when API artifacts are included)
- UI layer registry schema checks (when UI artifacts are included)
- Security + sovereignty scanning gates (where applicable)

### Reproduction (placeholder)

~~~bash
# Replace with repo-specific commands (not confirmed in repo)
# 1) validate schemas (STAC/DCAT/PROV/telemetry)
# 2) run pipeline tests / integrity checks
# 3) generate release-manifest.json + checksums.sha256
# 4) (optional) generate sbom + sign artifacts + emit attestations
# 5) verify signatures/attestations in CI
~~~

### Telemetry signals (optional)

| Signal | Source | Where recorded |
|---|---|---|
| Schema validation pass/fail | CI / validators | `releases/<version>/telemetry/` |
| Reference integrity (no orphans) | graph/catalog checks | `releases/<version>/telemetry/` |
| Sensitivity gate results | governance scans | `releases/<version>/telemetry/` |
| `classification_assigned` | catalog/CI | `releases/<version>/telemetry/` |
| `redaction_applied` | API/ETL/CI | `releases/<version>/telemetry/` |
| `promotion_blocked` | CI policy gate | `releases/<version>/telemetry/` |
| `catalog_published` | catalog pipeline | `releases/<version>/telemetry/` |
| `focus_mode_redaction_notice_shown` | UI telemetry | `releases/<version>/telemetry/` |

---

## ⚖ FAIR+CARE & Governance

### Governance review triggers

Route through governance review when a release includes:

- New sensitive layers or new public-facing datasets
- New AI narrative behaviors (Story Nodes / Focus Mode)
- New external data sources
- New public-facing endpoints
- Any change that impacts sovereignty constraints or redaction/generalization rules

### CARE / sovereignty considerations

- Do not distribute restricted locations, culturally sensitive knowledge, or other protected content without explicit approvals and required redaction/generalization rules.
- Enforce redaction/generalization at the API boundary and validate Story Node assets before shipping.

### AI usage constraints

- Ensure this doc’s `ai_transform_permissions` / `ai_transform_prohibited` match intended use.
- Release packaging documentation is **not** permission to generate new policy or to infer sensitive locations.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-27 | Initial `releases/` README (universal template-aligned) | TBD |
| v1.0.1 | 2025-12-28 | Align paths to Master Guide v12 + add Context/Diagrams + tighten release boundaries | TBD |

---

Footer refs:

- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty policy: `docs/governance/SOVEREIGNTY.md`
- Markdown work protocol: `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` (**not confirmed in repo**)
- v13 Blueprint (if adopted): `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` (**not confirmed in repo**)

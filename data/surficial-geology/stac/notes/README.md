---
title: "📝 Surficial Geology — STAC Notes"
path: "data/surficial-geology/stac/notes/README.md"

version: "v0.1.0"
last_updated: "2025-12-14"
release_stage: "Draft / In-Progress"
content_stability: "draft"

status: "Active"
doc_kind: "Index"
header_profile: "standard"
footer_profile: "standard"

license: "CC-BY 4.0"
markdown_protocol_version: "KFM-MDP v11.2.6"

scope:
  domain: "surficial-geology"
  applies_to:
    - "data/surficial-geology/stac/notes/**"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
classification: "Public"
sensitivity: "General (non-sensitive; auto-mask rules apply)"

jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
provenance_chain: []

doc_uuid: "urn:kfm:doc:data:surficial-geology:stac:notes-readme:v0.1.0"
semantic_document_id: "surficial-geology-stac-notes-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:surficial-geology:stac:notes-readme:v0.1.0"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "metadata-extraction"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-relationship-claims"
  - "narrative-fabrication"
  - "governance-override"
---

<div align="center">

# 📝 **Surficial Geology — STAC Notes**
`data/surficial-geology/stac/notes/README.md`

**Purpose**  
Provide a small, governed place for **human-authored notes** about the Surficial Geology STAC catalog (structure, decisions, exceptions, migrations) without editing the machine-validated STAC JSON itself.

</div>

---

## 📘 Overview

This directory is for **short, human-readable notes** that support the Surficial Geology STAC catalog.

Use STAC notes for:

- catalog structure decisions (Collections/Items layout, naming, sharding approach),
- STAC profile/extension choices and rationale (what is used and why),
- link/asset conventions (how `assets.*.href` is formed; what roles/types are expected),
- migrations (id changes, path changes, shard scheme changes) and how to interpret them,
- known limitations in catalog metadata (extent approximation, time handling, external href constraints).

Do not use STAC notes for:

- raw source acquisition details (use `data/surficial-geology/raw/**`),
- run-by-run lineage narratives (use `data/surficial-geology/lineage/notes/**`),
- output artifact documentation (use `data/surficial-geology/outputs/**` READMEs),
- replacing or “fixing” STAC JSON (fix the generator/pipeline and regenerate).

---

## 🗂️ Directory Layout

~~~text
📁 data/surficial-geology/stac/                        — Dataset-local STAC root
├── 📄 README.md                                       — STAC root conventions
├── 📁 collections/                                    — STAC Collections
├── 📁 items/                                          — STAC Items (and optional shards)
└── 📁 notes/                                          — STAC catalog notes (this directory)
    ├── 📄 README.md                                   — This file
    ├── 📄 YYYY-MM-DD__<short_slug>.md                 — Recommended: one topic per note
    └── 📁 _archive/                                   — Optional: superseded notes kept for auditability
~~~

Notes:

- Prefer adding a new dated note over rewriting history.
- Keep notes small, scoped, and cross-referenced to the exact STAC JSON and run identifiers they discuss.

---

## 🧭 Context

In the KFM pipeline, STAC notes support the catalog layer:

Deterministic ETL → outputs (tiles/vectors/metadata) → STAC (Collections/Items) → graph ingestion → API → frontend → Story Nodes → Focus Mode

These notes exist to explain catalog intent while keeping STAC JSON:

- machine-validated,
- deterministic,
- stable for consumers.

Canonical STAC entry points for Surficial Geology:

- `data/surficial-geology/stac/README.md`
- `data/surficial-geology/stac/collections/README.md`
- `data/surficial-geology/stac/items/README.md`
- `data/surficial-geology/stac/items/shards/README.md` (if sharding is used)

---

## 📦 Data & Metadata

### Recommended note structure

Each note SHOULD make it easy to separate facts from interpretation:

- **Facts (supported)**: what exists (paths, ids, schema, validator behavior).
- **Decision**: what was chosen and why.
- **Impact**: who/what it affects (API, ingestion, UI, downstream users).
- **Evidence pointers**: repo-relative paths and run IDs (no pasted logs).

### Required hygiene

- No secrets, tokens, credentials, or signed URLs.
- No PII (names/emails/phones) unless explicitly governed and approved.
- No sensitive precision or restricted knowledge.
- No embedded “hidden requirements” that should be implemented in code/config but aren’t.

If a note defines a rule (e.g., asset role names, sharding policy), ensure it is also encoded in the generator/config so it remains deterministic.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

Notes may be referenced from STAC JSON as documentation links when helpful, but notes must not replace core STAC fields.

If linked from STAC:

- link to a stable repo-relative path,
- treat notes as documentation/supporting metadata.

### DCAT

Notes may be treated as documentation distributions if DCAT publication includes documentation artifacts, but they should not contradict dataset-level rights/licensing.

### PROV

Notes may be represented as documentation entities supporting a catalog-generation activity, but authoritative run lineage remains in:

- `data/surficial-geology/lineage/prov/**`, and/or
- `data/surficial-geology/lineage/openlineage/**`, and/or
- `mcp/runs/**` (run logs/config snapshots).

---

## 🧪 Validation & CI/CD

Minimum expectations for committing STAC notes:

- passes secret and PII scanning expectations,
- contains only repo-safe, governance-safe content,
- keeps paths and ids accurate (no stale references).

Notes should never be required for STAC JSON to validate; validation must rely on the STAC JSON and governed metadata sources.

---

## ⚖ FAIR+CARE & Governance

Catalog documentation can increase inference risk when combined with other data.

- Prefer generalization over precision when describing locations or extents.
- Do not include restricted coordinates or discoverability guidance for sensitive sites.
- Keep licensing and rights statements consistent with authoritative source tracking under `data/surficial-geology/raw/**/license/**`.
- Record governance-driven decisions (masking/generalization, publication constraints) clearly and conservatively.

See governance and sovereignty policies linked in the footer.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v0.1.0**  | 2025-12-14 | Initial `stac/notes/` README defining what belongs here, naming conventions, and safe linkage to STAC/DCAT/PROV. |

---

<div align="center">

📝 **Surficial Geology — STAC Notes**  
KFM Catalog Layer · Documentation-First · Governance-Aware

[📘 Docs Root](../../../../docs/README.md) ·
[📂 Standards Index](../../../../docs/standards/README.md) ·
[📄 Templates Index](../../../../docs/templates/README.md) ·
[⚙ CI/CD Workflows](../../../../docs/workflows/README.md) ·
[📈 Telemetry Standard](../../../../docs/standards/telemetry_standards.md) ·
[📊 Telemetry Docs](../../../../docs/telemetry/README.md) ·
[♿ UI Accessibility Standard](../../../../docs/standards/ui_accessibility.md) ·
[🏛️ Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0

</div>


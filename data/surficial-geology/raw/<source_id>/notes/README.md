---
title: "📝 Surficial Geology — Raw Source Notes (<source_id>)"
path: "data/surficial-geology/raw/<source_id>/notes/README.md"

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
    - "data/surficial-geology/raw/<source_id>/notes/**"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
classification: "Public"
sensitivity: "General (non-sensitive; auto-mask rules apply)"

jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
provenance_chain: []

doc_uuid: "urn:kfm:doc:data:surficial-geology:raw:<source_id>:notes-readme:v0.1.0"
semantic_document_id: "surficial-geology-raw-<source_id>-notes-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:surficial-geology:raw:<source_id>:notes-readme:v0.1.0"

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

# 📝 **Surficial Geology — Raw Source Notes (<source_id>)**
`data/surficial-geology/raw/<source_id>/notes/README.md`

**Purpose**  
Capture **human-authored, non-authoritative notes** about this raw source intake (quirks, interpretation, decisions, and QA observations) without polluting machine-validated metadata or deterministic ETL inputs.

</div>

---

## 📘 Overview

This folder is for **source-specific notes** that help future maintainers understand:

- how the source was acquired and interpreted,
- known limitations or anomalies in the raw files,
- decisions made for governance (masking/generalization, exclusions),
- QA observations that should be reflected in deterministic pipelines.

Notes here are **documentation**, not the “source of truth” for:
- licensing (store authoritative license text/links under `raw/<source_id>/license/`),
- machine metadata (store under `raw/<source_id>/metadata/`),
- lineage/provenance events (store under `data/surficial-geology/lineage/`),
- transformations (store as config + code + run artifacts under `mcp/runs/`).

### What belongs here

- Plain-language acquisition context (what was downloaded, from where, when).
- Definitions/interpretation guidance for attributes and classifications used by the source.
- Known issues and “gotchas” (topology defects, missing attributes, inconsistent units).
- Governance and safety decisions (what precision is acceptable, what must be masked).

### What does not belong here

- Secrets, credentials, API keys, or any access tokens.
- Personal data (PII) or sensitive location details that violate sovereignty policy.
- Large binaries, raw dataset copies, or ad-hoc “fixed” exports.
- Decisions that should be encoded as deterministic rules but aren’t (write down the decision here, but implement it in pipeline/config).

---

## 🗂️ Directory Layout

~~~text
📁 notes/                                       — Human-authored notes for this source_id
├── 📄 README.md                                — This file (what notes are for + conventions)
├── 📄 acquisition.md                           — (optional) acquisition + retrieval context
├── 📄 interpretation.md                        — (optional) attribute meanings + domain quirks
├── 📄 qa-qc.md                                 — (optional) QA findings + known issues
└── 📄 governance-decisions.md                  — (optional) masking/exclusions + rationale
~~~

Conventions:

- Prefer **small, readable Markdown** files over one ever-growing log.
- If you need time-sliced notes, use `YYYY-MM-DD_<topic>.md` naming.
- Keep notes **source-scoped** (this folder only describes `<source_id>`).

---

## 🧭 Context

In the Surficial Geology domain, this folder supports long-term maintainability by providing “why” and “how to interpret” alongside the raw data, while keeping the pipeline deterministic.

Typical lifecycle:

1. Raw acquisition is recorded (authoritative artifacts under `raw/<source_id>/`).
2. Deterministic ETL converts/normalizes into processed forms (outside `raw/`).
3. Outputs are generated as distributions (under `data/surficial-geology/outputs/`).
4. Lineage is emitted (OpenLineage/PROV/manifests under `data/surficial-geology/lineage/`).
5. Catalog metadata references distributions (STAC/DCAT under `data/stac/` and related catalogs).

Use this notes folder to explain:
- why a field is treated a certain way,
- why a geometry rule exists,
- why a subset was excluded,
- what caveats should show up in Story Nodes / Focus Mode narratives.

---

## 📦 Data & Metadata

### Recommended note structure (inside any note file)

Use clear labeling so future readers (and safe summarizers) can separate:

- **Facts (sourced)**: what the upstream provider states or what is directly observed.
- **Interpretation**: how KFM interprets/apply those facts.
- **Speculation (explicitly hypothetical)**: allowed only if clearly labeled as such.

Example skeleton:

~~~text
Facts:
- …

Interpretation:
- …

Speculation (clearly hypothetical):
- …
~~~

### Cross-references (preferred)

When a note mentions an artifact, prefer referencing by:
- repo-relative path (for committed files),
- checksum/manifest ids (when available),
- run identifiers (when referencing a deterministic processing run).

Do not paste large external texts; link or cite them in the source metadata or license folder.

---

## 🌐 STAC, DCAT & PROV Alignment

This folder is documentation-first and can be represented as a documentation distribution when helpful:

- **DCAT**: treat key note files as documentation `dcat:Distribution` with `mediaType: text/markdown`.
- **STAC**: if a STAC Item references documentation, include a documentation asset role (e.g., `roles: ["metadata","documentation"]`) pointing to the note file path.
- **PROV-O**: note files may be `prov:Entity` used by:
  - an ingestion `prov:Activity` (as guidance / plan),
  - a curation decision record (as supporting evidence for exclusions/masking).

Keep the authoritative provenance trail in the lineage folders; notes can be linked as supporting context.

---

## 🧪 Validation & CI/CD

At minimum, notes must pass governance and documentation hygiene:

- No secrets, tokens, or credentials.
- No obvious PII.
- No sensitive restricted knowledge or disallowed precision (especially for protected sites or sovereignty-flagged locations).
- Markdown remains KFM-MDP compliant (front-matter present; approved H2 headings only in this README).

If a note introduces a new actionable rule (“we must dissolve polygons by X”), ensure the corresponding deterministic pipeline/config change exists (and is referenced).

---

## ⚖ FAIR+CARE & Governance

Even geologic and environmental layers can become sensitive when combined with other datasets.

When writing notes:

- Record sovereignty-related concerns and the rationale for any generalization/masking.
- Avoid including precise sensitive locations, even “for internal convenience,” if the policy disallows it.
- Prefer describing decisions at a **policy/rule level** rather than exposing restricted coordinates.

If a conflict exists between openness and safety, document the decision here and encode enforcement in catalogs/lineage and pipelines.

See the governance, FAIR+CARE, and sovereignty policies linked in the footer.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v0.1.0**  | 2025-12-14 | Initial `raw/<source_id>/notes/` README defining what belongs in source notes, naming conventions, and how notes relate to metadata, lineage, and governance. |

---

<div align="center">

📝 **Surficial Geology — Raw Source Notes (<source_id>)**  
KFM Data Layer · Documentation-First · Governance-Aware

[📘 Docs Root](../../../../../docs/README.md) ·
[📂 Standards Index](../../../../../docs/standards/README.md) ·
[📄 Templates Index](../../../../../docs/templates/README.md) ·
[⚙ CI/CD Workflows](../../../../../docs/workflows/README.md) ·
[📈 Telemetry Standard](../../../../../docs/standards/telemetry_standards.md) ·
[📊 Telemetry Docs](../../../../../docs/telemetry/README.md) ·
[♿ UI Accessibility Standard](../../../../../docs/standards/ui_accessibility.md) ·
[🏛️ Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC‑BY 4.0

</div>


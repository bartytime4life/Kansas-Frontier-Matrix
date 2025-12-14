---
title: "🧾 Surficial Geology — Raw Source License"
path: "data/surficial-geology/raw/<source_id>/license/README.md"

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
    - "data/surficial-geology/raw/<source_id>/license/**"

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

doc_uuid: "urn:kfm:doc:data:surficial-geology:raw:<source_id>:license-readme:v0.1.0"
semantic_document_id: "surficial-geology-raw-<source_id>-license-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:surficial-geology:raw:<source_id>:license-readme:v0.1.0"

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

# 🧾 **Surficial Geology — Raw Source License**
`data/surficial-geology/raw/<source_id>/license/README.md`

**Purpose**  
Capture the authoritative license, rights, and attribution requirements for raw source `<source_id>` in an auditable way that downstream manifests and catalogs can reference.

</div>

---

## 📘 Overview

This folder records **license and rights evidence** for the raw source identified by `<source_id>`.

### What `<source_id>` means

`<source_id>` is a stable identifier for a specific upstream provider + dataset (or a specific release/snapshot of that dataset). It should match the identifier used by:

- raw intake manifests / source manifests
- STAC/DCAT catalog records
- provenance (PROV/OpenLineage) run records

### What belongs here

- Upstream license text (when redistribution is allowed)
- Terms-of-use snapshots or statements captured at retrieval time
- Required attribution language and any usage constraints
- A small, machine-readable rights summary for deterministic pipelines

### What does not belong here

- “Guessed” licensing (only record what is explicitly provided by the source)
- Secrets, credentials, or private contact information
- Any restricted content that cannot be redistributed in-repo (store only citations + hashes + retrieval metadata)

---

## 🗂️ Directory Layout

~~~text
📁 license/                                      — License/rights evidence for this raw source
├── 📄 README.md                                 — This file (how licensing is recorded here)
├── 📄 LICENSE.txt                               — License text (verbatim; only if redistribution allowed)
├── 📄 TERMS_OF_USE.txt                          — Terms snapshot (verbatim; only if redistribution allowed)
├── 📄 ATTRIBUTION.md                            — Required attribution statement(s)
├── 🧾 rights.summary.json                        — Normalized rights summary (machine-readable)
└── 🧾 retrieval.proof.json                       — Where/when/how the license info was retrieved (urls + dates + hashes)
~~~

Notes:

- If the upstream license cannot be copied into the repo, omit `LICENSE.txt` / `TERMS_OF_USE.txt` and record:
  - the canonical URL(s),
  - retrieval date/time,
  - and a checksum/hash of the retrieved text/file (in `retrieval.proof.json`).

---

## 🧭 Context

License and rights metadata influences the KFM pipeline end-to-end:

Deterministic ETL → catalogs (STAC/DCAT/PROV) → graph (Neo4j) → API → frontend → Story Nodes → Focus Mode

In practice, this folder exists so that:

- Ingestion can deterministically apply license constraints (access, redistribution, attribution).
- Catalogs (STAC/DCAT) can expose correct `license` / `rights` fields.
- Provenance can demonstrate that licensing was checked and recorded at the time of acquisition.

---

## 📦 Data & Metadata

### `rights.summary.json` expectations

Keep this file small and stable. It should be easy for pipelines to parse and map into STAC/DCAT.

Recommended fields (adapt as needed, but keep keys consistent once adopted):

- `source_id`
- `source_uri`
- `license_id` (e.g., SPDX identifier when known)
- `license_name`
- `license_url`
- `rights_statement`
- `attribution_required` (boolean)
- `attribution_text`
- `redistribution_allowed` (boolean / unknown)
- `derivatives_allowed` (boolean / unknown)
- `commercial_use_allowed` (boolean / unknown)
- `access_restrictions` (array)
- `notes`
- `retrieved_at` (ISO date/time)
- `retrieved_by` (agent name or pipeline id; no personal emails)

### `retrieval.proof.json` expectations

This file should provide reproducibility and auditability:

- canonical URL(s) of license / TOS
- retrieval timestamp(s)
- file hashes (sha256) for any copied license text/files
- any “click path” notes if license was embedded behind navigation

### Attribution handling

If the source requires attribution:

- Put the exact attribution statement in `ATTRIBUTION.md`.
- Ensure downstream exports and catalog records carry the same attribution (do not paraphrase).

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Map licensing into STAC `license` fields on the relevant Collection/Item.
- Reference attribution and rights documents via STAC links or assets when appropriate (and allowed).

### DCAT

- Map licensing into DCAT fields (e.g., `dct:license`, `dct:rights`, `dcat:accessRights`).
- Treat each distributed file (if any) as a `dcat:Distribution` that inherits or references the correct rights.

### PROV

- Treat `rights.summary.json` (and any license documents) as `prov:Entity`.
- Ingest/acquisition activities should reference these entities via `prov:used` to show that rights were considered during acquisition and processing.

---

## 🧪 Validation & CI/CD

Minimum expectations for committed licensing artifacts:

- No secrets, tokens, or credentials.
- No PII (especially personal emails/phones) unless explicitly required and approved by governance.
- If storing verbatim license text, ensure redistribution is permitted.
- `rights.summary.json` is valid JSON and stays schema-stable once adopted.
- `retrieval.proof.json` includes retrieval dates and verifiable hashes/URLs.

---

## ⚖ FAIR+CARE & Governance

Licensing is a governance boundary:

- If a source is “open” but has restrictions (attribution, non-commercial, no-derivatives, share-alike, or access controls), record that here and ensure downstream publishing honors it.
- If sovereignty or sensitivity flags apply, treat them as higher-priority constraints than convenience and record the decision path in rights summaries and provenance.

See the governance and sovereignty policies linked in the footer.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v0.1.0**  | 2025-12-14 | Initial license folder README template for raw source `<source_id>` (rights evidence + catalog/provenance mapping). |

---

<div align="center">

🧾 **Surficial Geology — Raw Source License**  
KFM Data Layer · Rights-First · Provenance-First

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


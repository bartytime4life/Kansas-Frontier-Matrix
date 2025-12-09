---
title: "📂 Kansas Frontier Matrix — Source Agreements Directory"
path: "data/sources/agreements/README.md"
version: "v0.1.0"
last_updated: "2025-12-09"

release_stage: "Draft / Experimental"
lifecycle: "Incubation"
review_cycle: "Quarterly · FAIR+CARE Council & Data Governance Board"
content_stability: "evolving"

status: "Active / In-Repo Canonical"
doc_kind: "Standard"
header_profile: "standard"
footer_profile: "standard"

license: "CC-BY 4.0"
markdown_protocol_version: "KFM-MDP v11.2.5"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

scope:
  domain: "data-sources"
  applies_to:
    - "data/sources/agreements/**"

fair_category: "F1-A1-I1-R1"
care_label: "Mixed · Contractual / sovereignty-sensitive"
sensitivity: "Licensing & data use"
sensitivity_level: "Low–Medium"
public_exposure_risk: "Medium"
classification: "Internal-Default"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

governance_ref: "docs/governance/ROOT-GOVERNANCE.md"
ethics_ref: "docs/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "docs/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

provenance_chain:
  - "data/sources/README.md@v0.1.0"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: false
  must_reference_origin_root: false

doc_uuid: "urn:kfm:data:sources:agreements:readme:v0.1.0"
semantic_document_id: "data-sources-agreements-readme-v0.1.0"
event_source_id: "ledger:kfm:data:sources:agreements:readme:v0.1.0"
doc_integrity_checksum: "<sha256>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "provenance-check"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"

requires_directory_layout_section: true
requires_version_history: true

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# 📂 **Kansas Frontier Matrix — Source Agreements Directory**  
`data/sources/agreements/README.md`

**Purpose**  
Define how **legal, licensing, and sovereignty agreements** for all external data sources are
stored, versioned, validated, and linked into STAC, DCAT, PROV, and the KFM knowledge graph.

</div>

---

## 📘 Overview

### 1. What this directory is for

`data/sources/agreements/` is the **canonical registry of source agreements** that govern any
data coming into the Kansas Frontier Matrix:

- Open data licenses (CC‑BY, CC‑0, etc.).
- Terms of service / click‑through agreements.
- MOUs and data sharing agreements with agencies, archives, universities, vendors.
- Tribal / Indigenous data agreements and sovereignty protocols.
- Any custom conditions that constrain how KFM can ingest, process, publish, or train on data.

Every external dataset represented under `data/sources/**` **must** be backed by at least one
agreement manifest in this directory, even if the source appears “public domain”, so that:

- Licensing and rights are **explicit, auditable, and machine‑readable**.
- Sovereignty / CARE constraints are visible to ETL, graph ingestion, and AI layers.
- STAC/DCAT catalogs and the Neo4j graph can safely expose or restrict data.

### 2. Relationship to the KFM pipeline

This directory feeds the entire KFM pipeline:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j knowledge graph →  
> API layer → React/MapLibre/Cesium frontend → Story Nodes → Focus Mode

- **ETL jobs** read agreement manifests to decide:
  - whether a dataset can be fetched at all,
  - how it can be cached, generalized, anonymized, or redacted,
  - what usage and redistribution rules apply.
- **STAC Collections/Items** use manifests to populate `license`, `providers`, and custom
  `kfm:agreement_*` properties.
- **DCAT datasets and distributions** derive `dct:license`, `dct:rights`, and `dct:accessRights`
  from this directory.
- **PROV entities** model agreements as first‑class `prov:Entity` nodes linked to dataset entities.
- **Story Nodes & Focus Mode** consult manifests before rendering sensitive maps or narratives.

---

## 🗂️ Directory Layout

> Layout profile: `immediate-one-branch-with-descriptions-and-emojis`

    data/
      sources/
        agreements/
          README.md                          # 📂 You are here: standard for all agreements

          templates/
            agreement-manifest.schema.json   # 🧬 JSON Schema used in CI for manifests
            agreement-manifest.example.yaml  # 📋 Canonical example manifest

          public/                            # 🌐 Agreements for open/public data
            <source-id>/
              LICENSE.txt                    # 📜 Verbatim license (if redistributable)
              agreement-manifest.yaml        # 🧾 Machine-readable agreement summary
              notes.md                       # ✏️ Optional human notes (no secrets)

          restricted/                        # 🔒 Agreements with redistribution or access limits
            <source-id>/
              agreement-manifest.yaml        # 🧾 Agreement with internal / embargoed limits
              access-notes.md                # 🔐 Who can see what, at what resolution

          tribal/                            # 🪶 Indigenous / tribal data agreements
            <source-id>/
              agreement-manifest.yaml        # 🧾 CARE-aligned agreement summary
              sovereignty-notes.md           # 🛡 Cultural protocols & contacts (high-level only)

          third_party/                       # 🤝 Vendor / partner / commercial API contracts
            <source-id>/
              agreement-manifest.yaml        # 🧾 Summary of rights & restrictions
              contact.md                     # 📇 Non-sensitive contact / escalation info

          archive/                           # 🕰 Immutable snapshots of superseded manifests
            <yyyy>/
              <source-id>/
                agreement-manifest.vYYYYMMDD.yaml  # 📦 Frozen manifest snapshot (read-only)

**Naming conventions**

- `<source-id>` MUST match the canonical source id used under `data/sources/<source-id>/`.
- All manifests are named `agreement-manifest.yaml` (or `.json`) inside each `<source-id>/`.
- Historical snapshots live under `archive/` with date‑stamped filenames.
- Full contracts that cannot be committed (e.g., sensitive tribal MOUs) are **not** stored here —
  instead, the manifest encodes a summary and references an external governed vault URI.

---

## 🧱 Architecture

### 1. Agreement categories

Each agreement belongs to exactly one **visibility category**, which determines placement:

- **public/** — Open licenses and ToS where redistribution is allowed and no special sovereignty
  or privacy constraints apply. (Typical: state/federal portals, NOAA, USGS, DASC.)
- **restricted/** — Agreements that limit redistribution, require registration, or include moderate
  confidentiality clauses (embargoed or conditional datasets).
- **tribal/** — Agreements governed by Indigenous nations or community protocols. These can
  override “open” assumptions and may require generalization or narrative redaction.
- **third_party/** — Contracts with vendors, private archives, or commercial APIs. Outputs may
  need to be tagged “non‑redistributable” or “internal‑only”.
- **archive/** — Immutable manifest snapshots at the time of major change (license shifts,
  revocations, or scope expansions).

### 2. KFM modules that depend on this directory

Design targets (paths may evolve, but roles are stable):

- `src/pipelines/agreements/validate_agreements.py`  
  - validates all manifests against `agreement-manifest.schema.json`,  
  - enforces policy rules (category vs directory, required fields, SPDX, etc.).
- `src/graph/agreements/ingest_agreements.py`  
  - ingests agreements into Neo4j as nodes like `:Agreement`, `:License`,
    `:SovereigntyConstraint`.
- `src/api/agreements/routes.py`  
  - exposes read‑only agreement information to internal tools (no secret contract text).
- `src/web/app/admin/agreements/*`  
  - internal UI for data stewards to browse, diff, and review agreement metadata.

Frontend **must not** read raw manifests directly from `data/`; it goes via API + policy filters.

---

## 📦 Data & Metadata

### 1. Core `agreement-manifest` schema (YAML sketch)

Each manifest is a deterministic, MCP‑style config describing what is allowed or forbidden.

    id: "src-noaa-ncei-daily-climate"
    title: "NOAA NCEI Daily Climate Data for Kansas"
    source_uri:
      - "https://www.ncei.noaa.gov/"
    provider:
      name: "NOAA National Centers for Environmental Information"
      kind: "federal-agency"
    category: "public"                    # public|restricted|tribal|third_party
    agreement_type:
      - "license"                         # license|tos|mou|tribal_agreement|custom

    license:
      spdx: "CC-BY-4.0"                   # SPDX id or "Proprietary" / "Custom"
      label: "Creative Commons Attribution 4.0 International"
      license_text_ref: "LICENSE.txt"     # relative path or external URI

    rights_and_use:
      data_sharing_scope: "public"        # public|internal|embargoed|no_redistribution
      allowed_uses:
        - "research"
        - "education"
      prohibited_uses:
        - "re-identification"
      derived_data_rules:
        - "may_publish_aggregates_only"
        - "must_not_republish_raw_records"
      citation_required: true
      citation_text: "NOAA NCEI (year): Dataset title. Retrieved via Kansas Frontier Matrix."

    temporal_scope:
      effective_date: "2023-01-01"
      expiration_date: null               # or ISO date if known
      review_cycle: "biennial"

    jurisdiction:
      - "US-federal"
      - "Kansas"

    sensitivity:
      contains_pii: false                 # none|anonymized|contains_pii_prohibited
      data_category: "public"             # public|internal|restricted|confidential

    sovereignty:
      indigenous_rights_flag: false       # true for tribal/CARE datasets
      communities: []                     # populated for tribal agreements

    stac:
      collections:
        - "kfm-climate-noaa-ncei-daily"
      items: []                           # optional item IDs

    dcat:
      datasets:
        - "urn:kfm:dcat:dataset:noaa-ncei-daily"

    prov:
      entities:
        - "urn:kfm:entity:dataset:noaa-ncei-daily"
      wasGeneratedBy:
        - "urn:kfm:activity:etl:noaa-ncei-daily-v1"

    version:
      agreement_version: "2025.1"
      supersedes: "2023.2"
      change_log:
        - "2025-02-01: Updated license from CC-BY-3.0 to CC-BY-4.0."
        - "2025-02-01: Clarified derived-data rules for AI training."

    security:
      contract_vault_ref: null            # URI in secret contract vault (if applicable)

**Required blocks**, at minimum:

- `id`, `title`, `source_uri`, `provider`, `category`, `agreement_type`
- `license.spdx` or explicit `"Custom"` / `"Proprietary"` with `license.license_text_ref`
- `rights_and_use.data_sharing_scope`
- `temporal_scope.effective_date`
- `sensitivity.data_category`, `sensitivity.contains_pii`

For `tribal/` manifests, the `sovereignty` block is **mandatory** and more detailed.

---

## 🌐 STAC, DCAT & PROV Alignment

### 1. STAC integration

For each dataset with a manifest:

- **Collections**:
  - `license` → from `license.spdx` if standard, else `"proprietary"` / `"other"`.
  - `properties.kfm:agreement_id` → `manifest.id`.
  - `links[]` includes a `rel: "license"` link to a public LICENSE URL (when allowed).
- **Items**:
  - inherit `license` from Collection unless stricter per‑asset terms apply.
  - `properties.kfm:agreement_category` → `public|restricted|tribal|third_party`.

This is implemented in a STAC‑emitting ETL step and validated in CI via STAC linters.

### 2. DCAT integration

- Each manifest describes a `dcat:Dataset` (agreement resource), with:
  - `dct:title` ← `title`
  - `dct:description` ← short summary from `rights_and_use`
  - `dct:license` / `dct:rights` ← `license.spdx` or license URL.
- Data catalogs for actual datasets link to these agreement datasets via `dct:isReferencedBy`
  or a qualified relationship that captures “regulated by”.

This lets external catalog harvesters see which datasets are governed by which agreements.

### 3. PROV‑O (and GeoSPARQL) integration

- Each manifest is a `prov:Entity` with:
  - `prov:wasRevisionOf` for `version.supersedes`
  - `prov:generatedAtTime` for `temporal_scope.effective_date`
- ETL and ingestion activities (`prov:Activity`) declare that they:
  - `prov:used` both the agreement entity and upstream dataset entities,
  - generating derived dataset entities via `prov:wasGeneratedBy`.

If agreements have geographic scope (“Kansas‑only”, “CONUS”), that extent can be modeled as
GeoSPARQL geometries attached to the agreement entity.

---

## 🧠 Story Node & Focus Mode Integration

Story Nodes and Focus Mode must respect agreements:

- Each Story Node that references a dataset includes:
  - `kfm:agreement_id`
  - `kfm:agreement_category`
  - references to any `sovereignty.communities` when Indigenous data is involved.
- Focus Mode rendering logic:
  - hides or generalizes maps/narratives when `data_sharing_scope` requires it,
  - implements `sovereignty` rules (e.g., “no public story nodes with precise site locations”),
  - blocks narratives that contradict `rights_and_use.derived_data_rules`.

Example: A Story Node about a tribal site may only show an H3‑generalized polygon and a
high‑level description, never a pinpoint location or culturally sensitive details.

---

## 🧪 Validation & CI/CD

### 1. Schema validation

- JSON Schema: `data/sources/agreements/templates/agreement-manifest.schema.json`
- Example: `data/sources/agreements/templates/agreement-manifest.example.yaml`

CI targets (illustrative names):

1. `agreements-schema-lint`  
   - validate all `agreement-manifest.(yaml|json)` against the schema.

2. `agreements-policy-lint`  
   - check:
     - `category` matches directory,
     - `tribal/` manifests have full `sovereignty` block,
     - SPDX identifiers are valid or clearly `"Custom"` / `"Proprietary"`.

3. `agreements-crossref-lint`  
   - ensure `stac.collections`, `dcat.datasets`, and `prov.entities` refer to real IDs
     defined in `data/stac/**`, DCAT dumps, and graph configs.

### 2. CLI / Make integration

Suggested interface:

- `make agreements-validate` → run all three linters.
- `python -m kfm.agreements validate` → CLI entry point in `src/pipelines/agreements/`.

No PR that touches `data/sources/**` or `data/stac/**` should merge unless **all** agreement checks pass.

---

## ⚖ FAIR+CARE & Governance

### 1. FAIR

Agreements support FAIR metadata for all ingested datasets:

- **Findable** — manifests have stable IDs and are linked from STAC/DCAT/graph entities.
- **Accessible** — public agreements and summaries are open where allowed.
- **Interoperable** — structured YAML/JSON with STAC/DCAT/PROV alignment.
- **Reusable** — clear license, rights, and derived‑data rules.

### 2. CARE & Indigenous data sovereignty

For `tribal/` manifests:

- `sovereignty.indigenous_rights_flag: true` is required.
- `sovereignty.communities[]` enumerates communities/authorities recognized in the agreement.
- A spatial generalization policy must be encoded (e.g., H3 resolution, coarsened polygons).
- `sovereignty.narrative_restrictions[]` lists constraints on stories and narrative use.

All changes to tribal manifests require review by:

- FAIR+CARE Council,
- relevant tribal or Indigenous partners (when specified by the agreement),
- Security/Data Governance as needed.

No CI override may bypass sovereignty rules.

### 3. Contract & AI safety

- Contracts governing AI training or synthetic data must be reflected in `rights_and_use`
  and, if needed, dedicated `ai_limits` fields.
- AI systems (including Focus Mode and any training pipelines) must:
  - obey `derived_data_rules`,
  - tag outputs as “agreement‑constrained” where relevant,
  - exclude from training any datasets marked `no_redistribution` or equivalent.

---

## 🕰️ Version History

| Version | Date       | Author            | Changes                                                                 |
|--------:|------------|-------------------|-------------------------------------------------------------------------|
| v0.1.0  | 2025-12-09 | KFM System Author | Initial definition of `data/sources/agreements/` layout and standards.  |

---

### Kansas Frontier Matrix — Governance Footer

- 📜 **Root Governance**  
  [`docs/governance/ROOT-GOVERNANCE.md`](../../../docs/governance/ROOT-GOVERNANCE.md)

- 🌱 **FAIR+CARE & Ethics**  
  [`docs/faircare/FAIRCARE-GUIDE.md`](../../../docs/faircare/FAIRCARE-GUIDE.md)

- 🪶 **Indigenous Data Protection & Sovereignty**  
  [`docs/sovereignty/INDIGENOUS-DATA-PROTECTION.md`](../../../docs/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

- 🔐 **Security & Vulnerability Handling**  
  [`SECURITY.md`](../../../SECURITY.md)

- 🧾 **Markdown Authoring Protocol (KFM-MDP v11.2.5)**  
  [`docs/standards/kfm_markdown_protocol_v11.2.5.md`](../../../docs/standards/kfm_markdown_protocol_v11.2.5.md)

By editing this file, you agree to uphold these policies and to keep agreement metadata
**accurate, reproducible, and respectful of all licensing and sovereignty constraints.**
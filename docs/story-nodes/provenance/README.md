---
title: "🧾 KFM — Story Node Provenance (Index)"
path: "docs/story-nodes/provenance/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · FAIR+CARE Council · Focus Mode Board"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Index"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

classification: "Public"
jurisdiction: "Kansas / United States"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: true

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<none>"
doc_integrity_checksum: "<sha256>"

semantic_document_id: "kfm-doc-storynode-provenance-index"
doc_uuid: "urn:kfm:doc:storynode:provenance:index:v11.2.6"
event_source_id: "ledger:kfm:doc:storynode:provenance:index:v11.2.6"
provenance_chain: []

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed (navigation + banner parsing); must not invent provenance."

ai_transform_permissions:
  - "summarize"
  - "extract_banner_fields"
  - "generate_navigation_aids"
  - "format_to_kfm_mdp"

ai_transform_prohibited:
  - "invent_sources_or_citations"
  - "invent_governance_status"
  - "fabricate_provenance_or_dataset_relationships"
  - "generate_sensitive_locations"
  - "include_credentials_or_secrets"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 Context"
    - "🧱 Architecture"
    - "🗺️ Diagrams"
    - "🧠 Story Node & Focus Mode Integration"
    - "🧪 Validation & CI/CD"
    - "📦 Data & Metadata"
    - "🌐 STAC, DCAT & PROV Alignment"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "footer-check"
  - "accessibility-check"
  - "metadata-check"
  - "provenance-check"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

fencing_profile: "outer-backticks-inner-tildes-v1"

requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true
---

# 🧾 Story Node Provenance

**Purpose**  
Define the conventions and reusable patterns KFM uses to keep Story Nodes evidence-led, integrity-checkable, and lineage-traceable.

## 📘 Overview

Story Nodes are narrative overlays that must remain trustworthy under review and portable across exports (web UI, PDF, screenshots, offline bundles).

This provenance area standardizes:

- minimal “trust signals” shown to end users,
- machine-readable provenance fields for Focus Mode,
- linkage to catalog and lineage systems (STAC / DCAT / PROV),
- governance and sovereignty-safe redaction rules.

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 📁 story-nodes/
    └── 📁 provenance/
        ├── 📄 README.md                      — Provenance patterns index (this file)
        └── 📁 banner-3line/
            └── 📄 README.md                  — 3-line provenance banner pattern
~~~

## 🧭 Context

Provenance for Story Nodes serves two audiences:

- **Humans**: quick trust checks (source, integrity, lineage) without reading long audit logs.
- **Systems**: deterministic parsing so Focus Mode can show “why” and “where from” without guessing.

A Story Node is “provenance-complete” when it provides, at minimum:

- a clear source reference (catalog ID or document ID),
- an integrity signal (checksum; optionally signature / attestation),
- a compact derivation summary that does not leak restricted information.

If any of these are unknown, the Story Node must say “Unknown” rather than infer.

## 🧱 Architecture

### Provenance surfaces

KFM uses two complementary provenance surfaces:

1. **UI banner** (human-facing): a compact, stable banner shown at the top of a Story Node.
2. **Structured metadata** (machine-facing): fields used for catalogs, audits, and traceability.

The UI banner is intentionally minimal. It does not replace full STAC/DCAT records or PROV-O graphs.

### Recommended pattern

Use the 3-line banner pattern:

- `banner-3line`: `./banner-3line/README.md`

Minimal form:

~~~text
Source: <label> · <canonical_id>
Integrity: sha256:<digest> · sig:<ref> · attest:<ref>
Lineage: <input_id> → <activity_id> → <story_node_id>
~~~

### Redaction and generalization

When provenance fields could reveal restricted information:

- prefer stable IDs over descriptive details,
- generalize geographic precision in lineage labels (avoid coordinates),
- use access-safe identifiers when evidence is restricted,
- preserve integrity information when possible (checksums do not require location disclosure).

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A[Evidence asset or dataset] --> B[Catalog record: STAC or DCAT]
  B --> C[Lineage: PROV-O activity chain]
  C --> D[Story Node]
  D --> E[UI banner: Source + Integrity + Lineage]
  D --> F[Structured fields: machine extraction]
~~~

## 🧠 Story Node & Focus Mode Integration

Focus Mode may:

- extract banner fields (Source, Integrity, Lineage),
- display compact trust indicators,
- provide navigation to evidence assets and lineage traces (where allowed).

Focus Mode must not:

- invent missing provenance values,
- expand a generalized lineage into restricted details,
- fabricate evidence relationships not present in catalogs or the graph.

If provenance is missing:

- render “Unknown” (or “Not provided”),
- optionally suggest remediation steps (without guessing).

## 🧪 Validation & CI/CD

Recommended checks for Story Nodes that include a provenance banner:

- banner keys must match exactly (`Source:`, `Integrity:`, `Lineage:`),
- the three lines must be contiguous (no blank lines between),
- no secrets or internal endpoints,
- no restricted location disclosure in provenance fields,
- integrity line includes algorithm label (e.g., `sha256:`).

Docs in this directory must also pass:

- front matter schema validation,
- approved heading registry,
- inner-fence rules (`~~~` for code blocks),
- footer governance links present.

## 📦 Data & Metadata

When a Story Node is generated or updated, the system should emit structured provenance fields suitable for:

- registries,
- audits,
- catalog linking,
- replay and verification.

Minimum fields (conceptual):

- `story_node_id` (stable identifier)
- `source_id` (dataset or document ID)
- `checksum` (algorithm + digest)
- `signature_ref` / `attestation_ref` (optional)
- `lineage_summary` (one-line chain)
- `rights_and_sensitivity` (flags applied to prevent leakage)

Structured provenance should be treated as authoritative over the banner text where they conflict.

## 🌐 STAC, DCAT & PROV Alignment

Intended mapping:

- **STAC**: provenance can point to Items and Collections that hold evidence assets and derived layers.
- **DCAT**: provenance can reference datasets and distributions, including rights and license properties.
- **PROV-O**: provenance lineage corresponds to Activities (transforms) and Entities (inputs/outputs), with Agents for responsible systems and stewards.

The banner is a compact presentation layer. Full provenance remains in catalogs and lineage records.

## ⚖ FAIR+CARE & Governance

Hard constraints:

- do not include secrets, tokens, or private endpoints,
- do not disclose restricted or sensitive locations,
- respect Indigenous data sovereignty controls by default,
- do not invent citations or sources.

If a Story Node references culturally sensitive materials:

- apply masking/generalization,
- ensure rights and stewardship are represented in structured provenance fields,
- require review or gating per governance policy.

## 🕰️ Version History

| Version | Date | Summary |
|---:|---:|---|
| **v11.2.6** | 2025-12-14 | Created provenance patterns index for Story Nodes; defined minimal completeness criteria; linked the 3-line banner pattern and aligned checks for CI validation. |

---

[⬅ Back to Documentation Index](../../README.md) · [📂 Standards Index](../../standards/README.md) · [🏛️ Governance Charter](../../standards/governance/ROOT-GOVERNANCE.md) · [🤝 FAIR+CARE Guide](../../standards/faircare/FAIRCARE-GUIDE.md) · [🪶 Indigenous Data Protection](../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)


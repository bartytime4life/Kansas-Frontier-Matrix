---
title: "🧾 KFM — Story Node Provenance Banner (3‑Line Minimal Pattern)"
path: "docs/story-nodes/provenance/banner-3line/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · FAIR+CARE Council · Focus Mode Board"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Design Note"
header_profile: "standard"
footer_profile: "standard"

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

signature_ref: "<release-signature-path>"
attestation_ref: "<slsa-attestation-path>"
provenance_chain: []

semantic_document_id: "kfm-storynode-provenance-banner-3line"
doc_uuid: "urn:kfm:design:storynode:prov-banner-3line:v11.2.6"
event_source_id: "ledger:kfm:design:storynode:prov-banner-3line:v11.2.6"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed (banner parsing + navigation); must not invent provenance."

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
---

# 🧾 KFM — Story Node Provenance Banner (3‑Line Minimal Pattern)

**Purpose**  
Define a minimal, consistent **3‑line provenance banner** for Story Nodes that preserves trust and auditability without clutter. The banner surfaces: **(1) Source**, **(2) Integrity**, **(3) Lineage**.

## 📘 Overview

Story Nodes are narrative overlays that must remain evidence-led and provenance-aware. A small, stable banner at the top of each Story Node supports:

- quick human trust signals (what this is, where it came from),
- machine extraction (Focus Mode can parse it deterministically),
- governance review (integrity and lineage are visible),
- portability (the banner survives exports and screenshots).

This pattern is intentionally minimal: it is not a full citation block, and it must not expand into a multi-paragraph audit log.

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 📁 story-nodes/
    └── 📁 provenance/
        └── 📁 banner-3line/
            └── 📄 README.md              — 3-line provenance banner pattern (this file)
~~~

## 🧭 Context

The banner is designed to appear at the top of a Story Node (or Story Node UI card) and answer three questions immediately:

1. **Source** — What evidence item (or authority) is this Story Node based on?
2. **Integrity** — Can we detect tampering or mismatch (checksum, signature, attestation)?
3. **Lineage** — What is the shortest safe derivation chain from raw evidence to this Story Node?

Where the Story Node is sensitive, the banner must not leak restricted information (especially precise locations). In those cases, use generalized identifiers and high-level lineage descriptions.

## 🧱 Architecture

### Canonical 3-line keys

Use these keys exactly (case and punctuation) for deterministic parsing:

- `Source:`
- `Integrity:`
- `Lineage:`

### Line 1 — Source (who/what)

Requirements:

- a concise, human-readable label, plus a canonical identifier when available
- avoid long descriptions; keep the label compact

Recommended formats:

- `Source: <label> · <canonical_id>`
- `Source: <label> · <catalog_ref>`

Examples of canonical identifiers:

- `urn:kfm:dataset:...`
- `stac:item:...`
- `dcat:dataset:...`
- `urn:kfm:document:...`

### Line 2 — Integrity (tamper signal)

Requirements:

- include a checksum digest for the primary evidence artifact when available
- optionally include signature and attestation references

Recommended formats:

- `Integrity: sha256:<digest> · sig:<ref> · attest:<ref>`
- `Integrity: sha256:<digest>`

### Line 3 — Lineage (short derivation)

Requirements:

- a short, human-readable derivation chain that fits on one line
- use stable IDs when possible; otherwise use safe human labels
- keep it minimal: raw → transform → output

Recommended formats:

- `Lineage: <input_id> → <activity_id> → <output_id>`
- `Lineage: <input_label> → <process_label> → <story_node_id>`

### Example (UI string)

~~~text
Source: KHS Archive Photograph · urn:kfm:document:khs:photo:1892-001
Integrity: sha256:9f2c…c8a1 · sig:releases/v11.2.6/signature.sig · attest:releases/v11.2.6/slsa-attestation.json
Lineage: urn:kfm:document:khs:photo:1892-001 → urn:kfm:activity:etl:ocr:v11.2.6 → urn:kfm:storynode:smoky-hill:segment-04
~~~

### Example (Markdown snippet)

~~~text
Source: <label> · <canonical_id>
Integrity: sha256:<digest> · sig:<ref> · attest:<ref>
Lineage: <input_id> → <activity_id> → <story_node_id>
~~~

Parsing note:

- Keep the three lines contiguous.
- Prefer ASCII separators (`:` and `·`) and arrow `→` for readability. If `→` is not available, use `->`.

## 🧠 Story Node & Focus Mode Integration

Focus Mode may extract and display these banner fields as “trust badges” and navigation shortcuts.

Rules:

- Focus Mode may summarize the Story Node, but must not invent sources, integrity values, or lineage.
- If banner fields are missing, Focus Mode should render “Unknown” (or “Not provided”) rather than guessing.
- If the Story Node is sovereignty-sensitive, Focus Mode must respect masking rules and must not expand generalized lineage into restricted details.

Recommended extraction fields (machine view):

- `source_label`, `source_id`
- `checksum_alg`, `checksum_digest`
- `signature_ref`, `attestation_ref`
- `lineage_chain` (as a compact string, not expanded graph)

## 🧪 Validation & CI/CD

Recommended CI checks for Story Node banner compliance:

- exactly one `Source:` line
- exactly one `Integrity:` line
- exactly one `Lineage:` line
- the three lines are contiguous (no blank lines between them)

Example lint rule shape (documentation-only):

~~~text
Story Node banner required:
  ^Source:\\s+.+$
  ^Integrity:\\s+.+$
  ^Lineage:\\s+.+$
~~~

Common failure causes:

- keys don’t match exactly (e.g., “Sources:” or “Lineage -”)
- blank line inserted between banner lines
- checksum included without algorithm label (use `sha256:`)
- sensitive coordinates accidentally included in `Source:` or `Lineage:`

## 📦 Data & Metadata

If the banner is generated automatically, the generating system should also emit a structured record suitable for catalogs and audits.

Minimal JSON shape (for sidecar or metadata registry):

~~~json
{
  "banner_version": "v11.2.6",
  "source": {
    "label": "<human label>",
    "id": "<canonical id or catalog ref>"
  },
  "integrity": {
    "checksum": {
      "alg": "sha256",
      "digest": "<hex>"
    },
    "signature_ref": "<optional>",
    "attestation_ref": "<optional>"
  },
  "lineage": {
    "summary": "<one-line chain>",
    "input_ids": ["<optional>"],
    "activity_ids": ["<optional>"],
    "output_ids": ["<optional>"]
  }
}
~~~

## 🌐 STAC, DCAT & PROV Alignment

Mapping guidance:

- **STAC**: the `source.id` and `output_ids` may reference STAC Items/Collections; integrity may mirror checksum extensions.
- **DCAT**: the banner can point to a `dcat:Dataset` or `dcat:Distribution` identifier for the evidence or derived asset.
- **PROV-O**: the lineage chain corresponds to `prov:Entity` (inputs/outputs) and `prov:Activity` (transform).

The banner is a compact human-and-machine hint; it is not a replacement for full STAC/DCAT/PROV records.

## ⚖ FAIR+CARE & Governance

Constraints:

- Do not include secrets, internal endpoints, or credentials.
- Do not include restricted or sensitive locations. Prefer stable IDs, generalized regions, or redacted forms.
- If the evidence is under access restrictions, use an access-safe identifier and avoid revealing private collection details.
- Ensure the banner remains truthful: if a checksum or lineage is unknown, state it as unknown.

## 🕰️ Version History

- v11.2.6 (2025-12-14): Initial publication of the 3-line provenance banner pattern for Story Nodes.

---

[⬅ Back to Documentation Index](../../../README.md) · [📂 Standards Index](../../../standards/README.md) · [🏛️ Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md) · [🤝 FAIR+CARE Guide](../../../standards/faircare/FAIRCARE-GUIDE.md) · [🪶 Indigenous Data Protection](../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

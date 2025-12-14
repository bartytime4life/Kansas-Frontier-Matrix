---
title: "🧾 KFM — Story Node Provenance Banner (3-Line Minimal Pattern)"
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

semantic_document_id: "kfm-storynode-provenance-banner-3line"
doc_uuid: "urn:kfm:design:storynode:prov-banner-3line:v11.2.6"
---

# 🧾 Story Node Provenance Banner — 3-Line Minimal Pattern

**Purpose**  
A minimal 3-line provenance banner that can be placed at the top of every Story Node to preserve trust and auditability without heavy UI. It shows: **(1) Source, (2) Integrity, (3) Lineage**.

## 📘 Overview

This banner pattern provides a compact, deterministic “trust header” that is readable to humans and reliably extractable by Focus Mode. It is intentionally not a full citation section and must stay short.

The banner answers three questions:

1. **Source** — what evidence item (or authority) supports the Story Node?
2. **Integrity** — can we detect mismatch or tampering (checksum, optional signature/attestation)?
3. **Lineage** — what is the shortest safe derivation chain from evidence to this Story Node?

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 📁 story-nodes/
    └── 📁 provenance/
        └── 📁 banner-3line/
            └── 📄 README.md                      — This pattern
~~~

## 🧭 Context

Story Nodes are narrative overlays and must remain evidence-led. A provenance banner is a low-cost way to:

- signal trust quickly (what this is based on),
- make integrity observable (checksum present),
- make lineage legible (derivation chain visible),
- support governance review and reproducibility.

If a Story Node is sovereignty-sensitive or location-sensitive, the banner must not reveal restricted details (especially precise locations). Prefer stable IDs and generalized lineage descriptions.

## 🧱 Architecture

### The 3 lines

Use these keys exactly for deterministic parsing:

- `Source:`
- `Integrity:`
- `Lineage:`

**Line 1 — Source (who/what)**  
Concise human label + canonical ID (when available).

**Line 2 — Integrity (untampered?)**  
Checksum (algorithm + digest), plus optional signature/attestation references.

**Line 3 — Lineage (where did it come from?)**  
Short human-readable derivation path (raw → transform → Story Node). Keep it one line.

### Recommended formats

~~~text
Source: <label> · <canonical_id>
Integrity: sha256:<digest> · sig:<ref> · attest:<ref>
Lineage: <input_id> → <activity_id> → <story_node_id>
~~~

Notes:

- Keep the three lines contiguous (no blank lines between them).
- Use stable IDs where possible (e.g., `urn:kfm:…`, `stac:…`, `dcat:…`).
- If `→` is not available, use `->`.

### Example (UI string)

~~~text
Source: KHS Archive Photograph · urn:kfm:document:khs:photo:1892-001
Integrity: sha256:9f2c1f2b…c8a1 · sig:releases/v11.2.6/signature.sig · attest:releases/v11.2.6/slsa-attestation.json
Lineage: urn:kfm:document:khs:photo:1892-001 → urn:kfm:activity:etl:ocr:v11.2.6 → urn:kfm:storynode:smoky-hill:segment-04
~~~

### If information is unknown

Do not guess.

~~~text
Source: Unknown
Integrity: Unknown
Lineage: Unknown
~~~

## 🧠 Story Node & Focus Mode Integration

Focus Mode may extract and display these banner fields as “trust badges” and navigation shortcuts.

Rules:

- If a field is missing or unknown, Focus Mode must render “Unknown” (or “Not provided”) rather than inferring.
- Focus Mode must not invent checksums, signatures, sources, lineage, or governance status.
- When sovereignty rules apply, Focus Mode must not expand generalized lineage into restricted details.

Recommended extraction fields:

- `source_label`, `source_id`
- `checksum_alg`, `checksum_digest`
- `signature_ref`, `attestation_ref`
- `lineage_summary` (compact string; do not auto-expand into graph claims)

## 🧪 Validation & CI/CD

Recommended lint checks for Story Nodes using this banner:

- exactly one `Source:` line
- exactly one `Integrity:` line
- exactly one `Lineage:` line
- lines must be contiguous (no blank lines between)
- checksum must include algorithm label (e.g., `sha256:`)

Example rule shape (documentation-safe):

~~~text
^Source:\\s+.+$
^Integrity:\\s+.+$
^Lineage:\\s+.+$
~~~

Common failure causes:

- key mismatch (e.g., `Sources:` or `Lineage -`)
- blank line inserted between banner lines
- sensitive coordinates included in the banner

## 📦 Data & Metadata

If the banner is auto-generated, also emit a structured record (sidecar, registry, or ledger) for audit and catalog linking.

Minimal JSON shape:

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

- **STAC**: `source.id` and derived assets may reference STAC Items/Collections; integrity may mirror checksum extensions.
- **DCAT**: banner may reference a `dcat:Dataset` or a `dcat:Distribution` identifier.
- **PROV-O**: lineage chain corresponds to `prov:Entity` (inputs/outputs) and `prov:Activity` (transform).

The banner is a compact hint; it does not replace full STAC/DCAT/PROV records.

## ⚖ FAIR+CARE & Governance

Hard constraints:

- Do not include secrets, internal endpoints, or credentials.
- Do not include restricted or sensitive locations; prefer stable IDs and generalized descriptions.
- If evidence is restricted, use an access-safe identifier and avoid disclosing private collection details.
- Truthfulness is mandatory: if a checksum or lineage is unknown, state it as unknown.

## 🕰️ Version History

| Version | Date | Summary |
|---:|---:|---|
| **v11.2.6** | 2025-12-14 | Initial publication of the 3-line provenance banner pattern for Story Nodes; standardized keys and parsing rules; added lint guidance and metadata shape. |

---

[⬅ Back to Documentation Index](../../../README.md) · [📂 Standards Index](../../../standards/README.md) · [🏛️ Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md) · [🤝 FAIR+CARE Guide](../../../standards/faircare/FAIRCARE-GUIDE.md) · [🪶 Indigenous Data Protection](../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

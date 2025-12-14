---
title: "🧬 KFM — DRIFT Embeddings (Community + Entity Vectors · Determinism · CARE-Safe Indexing)"
path: "docs/search/drift/embeddings/README.md"

version: "v11.2.6"
last_updated: "2025-12-13"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council Oversight"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Reference + Runbook"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

intent: "drift-embeddings"
audience:
  - "Search Engineering"
  - "Graph + Provenance Engineering"
  - "Focus Mode Engineering"
  - "Reliability Engineering"
  - "Governance Reviewers"

classification: "Public (Governed)"
fair_category: "F1-A2-I2-R2"
care_label: "CARE-Aware Retrieval"
sensitivity_level: "Medium"
public_exposure_risk: "Medium"
redaction_required: true
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

sensitivity: "Embedding pipelines may touch heritage-context materials; CARE screening mandatory; no restricted locations or raw sensitive text in public artifacts."
risk_category: "Governed"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:doc:search:drift:embeddings:v11.2.6"
semantic_document_id: "kfm-drift-search-embeddings"
event_source_id: "ledger:docs/search/drift/embeddings/README.md"
immutability_status: "version-pinned"
machine_extractable: true

telemetry_schema: "../../../../schemas/telemetry/drift-search-v11.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

json_schema_ref: "../../../../schemas/json/drift-embeddings-v11.schema.json"
shape_schema_ref: "../../../../schemas/shacl/drift-embeddings-v11-shape.ttl"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
security_ref: "../../../security/supply-chain/README.md"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "metadata-extraction"
  - "diagram-extraction"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "content-alteration"
  - "narrative-fabrication"
  - "governance-override"

accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
ttl_policy: "Review every 12 months"
sunset_policy: "Superseded by drift-search-v12"
---

<div align="center">

# 🧬 **KFM — DRIFT Embeddings**
`docs/search/drift/embeddings/README.md`

**Purpose**  
Define the governed **embedding layer** for DRIFT Search: how vectors are generated, masked, versioned, snapshotted,
and queried to support **global→local hybrid retrieval**, while enforcing **determinism**, **provenance**, and
**CARE/sovereignty protections**.

<img src="https://img.shields.io/badge/Embeddings-Community%20%2B%20Entity-blue" />
<img src="https://img.shields.io/badge/Determinism-Required-brightgreen" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Gated-gold" />
<img src="https://img.shields.io/badge/Sensitivity-Medium%20%7C%20Redaction%20Required-orange" />
<img src="https://img.shields.io/badge/License-MIT-green" />

</div>

---

## 📘 Overview

DRIFT uses embeddings to improve **global recall** before Neo4j performs **local precision traversal**.

This layer covers:

- which embedding families are produced (community/entity/document surrogates),
- how inputs are sanitized and policy-gated prior to embedding,
- how vectors are snapshotted (for reproducibility),
- how retrieval uses those vectors without leaking restricted details,
- how provenance records model/version/config and policy decisions.

### Non-negotiables (governed)

- Embeddings MUST be generated from **policy-safe text/fields** only.
- Restricted content MUST NOT be embedded into public indexes.
- Embedding runs MUST be reproducible (model id, template/config hash, deterministic pipeline).
- Every embedding index MUST have an **index snapshot id** and provenance bundle.

---

## 🗂️ Directory layout

~~~text
📁 docs/search/drift/embeddings/                       — Embeddings reference + runbook (documentation)
├── 📄 README.md                                       — This document
├── 📁 policies/                                       — Masking + inclusion policies for embedding inputs
│   ├── 🧾 embedding_input_allowlist.yml               — Allowed fields per entity/dataset type
│   ├── 🧾 embedding_redaction_rules.yml               — Mask/generalize rules prior to embedding
│   └── 🧾 embedding_scope_policy.yml                  — Role/sensitivity gating (what can be indexed)
├── 📁 templates/                                      — Optional templates for “community summaries”
│   ├── 🧾 community_summary.template.md               — Deterministic summarization template (policy-safe)
│   └── 🧾 community_summary.schema.json               — Schema for summary payloads that get embedded
└── 📁 examples/                                       — Redaction-safe manifests (no vectors, no sensitive text)
    ├── 🧾 embedding_manifest.example.json
    └── 🧾 index_snapshot.example.json
~~~

Recommended operational output paths (house defaults; pipeline may override):

~~~text
📁 data/processed/search/drift/embeddings/             — Embedding artifacts and index snapshots (operational)
├── 📁 snapshots/
│   └── 📁 <index_snapshot_id>/
│       ├── 🧾 manifest.json                           — Model/config/policy metadata + checksums
│       ├── 🧾 vectors.meta.json                       — Dimensions, counts, normalization (no raw text)
│       ├── 🧾 ids.parquet                             — Stable ids mapped to vector rows (refs-only)
│       └── 🧾 index/                                  — ANN index files (format depends on backend)
└── 📄 latest.json                                     — Pointer to latest snapshot id (optional)

📁 mcp/runs/search/drift/                              — Run logs and config snapshots (reproducibility)
└── 📁 <run_id>/
    ├── 🧾 config.snapshot.json                        — Resolved config (model id, policies, scopes)
    ├── 🧾 provenance.jsonld                            — PROV bundle for embedding activity
    └── 📄 validate.log                                — Validation report (dims, leakage checks, determinism)
~~~

> Public docs MUST NOT store raw vectors inline. Example files in `docs/` should contain only manifests and schema-safe metadata.

---

## 🧩 Embedding families (what we index)

DRIFT embeddings are organized into a small number of families to keep behavior auditable.

### 1) Community embeddings (recommended)

**What**: vectors representing “community summaries” (graph communities, thematic clusters, or curated groupings).  
**Why**: improves recall for broad narrative questions before local graph traversal.

Inputs SHOULD be:

- curated or deterministic “community summary” text,
- non-sensitive descriptors (region-level, non-doxxable),
- stable identifiers (`urn:kfm:community:*`).

### 2) Entity embeddings (recommended)

**What**: vectors representing individual graph entities (Place/Event/Person/Document/Dataset).  
**Why**: supports similarity search to find candidate nodes for local traversal.

Inputs MUST be restricted to allowlisted fields such as:

- titles, controlled vocab keywords, high-level summaries,
- temporal ranges (as text tokens or normalized fields),
- generalized spatial descriptors (region/H3 coarse if allowed),
- provenance-safe identifiers (never secrets).

### 3) Dataset / catalog embeddings (optional)

**What**: vectors from STAC/DCAT metadata descriptions.  
**Why**: helps route queries toward the correct datasets and collections.

Inputs SHOULD be:

- dataset title/description/license/provenance summaries,
- spatial/temporal coverage at generalized granularity,
- explicit rights and sensitivity labels.

### 4) Document chunk embeddings (restricted; policy-dependent)

If used, MUST be access-controlled and MUST obey sensitivity and sovereignty policies:

- do not embed restricted cultural site narratives into public indexes,
- do not embed raw protected location descriptions when they enable re-identification,
- prefer embedding **sanitized summaries** rather than full text.

---

## 🛡️ CARE and sovereignty protections

Because `redaction_required: true`:

- embeddings MUST exclude any raw protected coordinates and re-identifying location descriptions,
- embedding inputs MUST be masked/generalized first,
- the index MUST record a `care_gate_status` and `sovereignty_gate` outcome for the snapshot.

### Required pre-embedding transforms (minimum)

- remove or mask coordinate-like patterns (policy-defined regex/heuristics),
- generalize spatial mentions to approved region granularity,
- drop restricted fields entirely when policy says “deny”,
- hash or remove identifiers that could enable doxxing.

### Required policy outputs (minimum)

- `care_gate_status`: `allow` | `redact` | `deny`
- `sovereignty_gate`: `clear` | `restricted` | `conflict` | `unknown`
- `redaction_summary`: counts + normalized reason codes (no sensitive details)

---

## 🎛️ Determinism contract

Embedding generation MUST be reproducible.

### Required controls (pin and record)

- embedding model id and exact version (or digest)
- tokenizer version (if applicable)
- embedding dimensionality (`d`)
- normalization behavior (e.g., `l2_normalize: true|false`)
- text canonicalization rules (whitespace/unicode normalization)
- field allowlist version/hash
- redaction policy version/hash
- index build parameters (e.g., ANN graph params) and version
- fixed locale and timezone

### Stable mapping (required)

The mapping between ids and vectors MUST be stable:

- `row_i` corresponds to `entity_id_i` deterministically
- stable sort order (e.g., `ORDER BY urn ASC`) before vectorization
- emit `ids.parquet` or equivalent refs-only mapping for audit

---

## 🗺️ Embedding pipeline flow

~~~mermaid
flowchart TD
  A["Sources - graph entities + STAC/DCAT metadata"] --> B["Allowlist fields"]
  B --> C["Mask / generalize (CARE gate)"]
  C --> D["Canonicalize text (deterministic)"]
  D --> E["Embed (pinned model + version)"]
  E --> F["Normalize vectors (policy-defined)"]
  F --> G["Build ANN index (snapshot)"]
  G --> H["Emit manifest + PROV + telemetry"]
~~~

---

## 📦 Embedding manifest (required)

Each index snapshot MUST include a machine-readable manifest.

### Minimum manifest fields

- `index_snapshot_id`
- `created_utc`
- `embedding_model_id` and version/digest
- `dimensionality`
- `normalization`
- `scope` (what families/types are included)
- `counts` (vectors by family/type)
- `policy_bundle_hash` and `allowlist_hash`
- `care_gate_status`, `sovereignty_gate`, `redaction_summary`
- `checksums` for key artifacts (ids map, index files, manifest)

### Example (redaction-safe)

~~~json
{
  "index_snapshot_id": "urn:kfm:search:index:snapshot:drift:abcd1234ef567890",
  "created_utc": "2025-12-13T00:00:00Z",
  "embedding_model": {
    "id": "embedding-model:<pinned>",
    "version": "sha256:<digest>",
    "dimensionality": 1024,
    "l2_normalize": true
  },
  "scope": {
    "families": ["community", "entity", "catalog"],
    "notes": "No restricted full-text embeddings included."
  },
  "counts": {
    "community": 120,
    "entity": 250000,
    "catalog": 3400
  },
  "governance": {
    "care_gate_status": "redact",
    "sovereignty_gate": "unknown",
    "redaction_summary": {
      "events_total": 3,
      "reasons": ["spatial_precision_reduced", "restricted_fields_dropped"]
    },
    "policy_bundle_hash": "sha256:…",
    "allowlist_hash": "sha256:…"
  },
  "artifacts": {
    "ids_map_ref": "data/processed/search/drift/embeddings/snapshots/.../ids.parquet",
    "index_ref": "data/processed/search/drift/embeddings/snapshots/.../index/",
    "prov_ref": "data/processed/prov/search/drift/embeddings/.../prov.jsonld"
  },
  "checksums": {
    "ids.parquet": "sha256:…",
    "index.tar": "sha256:…"
  }
}
~~~

---

## 📜 Provenance mapping (minimum)

Embedding production MUST be recorded as a first-class provenance activity.

### PROV-O

- `prov:Activity`: `drift_embedding_build`
- `prov:Entity` inputs:
  - index source snapshot refs (graph snapshot id, STAC/DCAT snapshot id)
  - allowlist and policy bundle entities (by hash)
  - embedding model descriptor entity (by digest)
- `prov:Entity` outputs:
  - embedding snapshot manifest
  - ids map
  - ANN index bundle
- `prov:Agent`:
  - embedding runner (software agent)
  - CI validator (software agent)

### OpenLineage (optional; recommended when telemetry is on)

- job: `drift/embeddings/build`
- run id: stable per snapshot build
- inputs/outputs: snapshot refs, manifest refs, index refs

---

## 🧪 Validation and CI gates

Embedding snapshots MUST be validated before adoption by DRIFT retrieval.

Minimum checks:

- schema validation of manifest
- dimensionality consistency (all vectors have `d`)
- deterministic ordering checks (ids map stable)
- leakage checks:
  - no coordinate-like patterns in embedded source text (pre-embed logs must be safe)
  - no restricted endpoints or secrets
- governance checks:
  - `care_gate_status` and `sovereignty_gate` present
  - policy hashes recorded
- index integrity checks:
  - ANN index can load
  - id→vector row mapping resolves

Validation output SHOULD be recorded in:

- `mcp/runs/search/drift/<run_id>/validate.log`

---

## 🧰 Operational runbook (implementation-agnostic)

A compliant embedding build SHOULD:

1. Resolve inputs:
   - graph snapshot refs
   - STAC/DCAT snapshot refs (if used)
   - policy bundle and allowlists
2. Apply field allowlists and CARE redaction/generalization.
3. Canonicalize text and compute `source_pack_hash`.
4. Generate vectors using a pinned model.
5. Build an ANN index and create `index_snapshot_id`.
6. Emit:
   - manifest (required)
   - ids mapping (refs-only)
   - provenance bundle (required)
   - telemetry references (optional)
7. Validate and publish the snapshot id.

---

## 🕰️ Version history

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-13 | Initial governed DRIFT embeddings reference; codified embedding families, determinism controls, CARE-safe indexing, snapshot manifests, provenance mapping, and validation gates. |

---

<div align="center">

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Gated-gold" />
<img src="https://img.shields.io/badge/Sensitivity-Medium%20%7C%20Redaction%20Required-orange" />

[⬅ Back to DRIFT Search](../README.md) ·
[🔍 Search Index](../../README.md) ·
[📜 DRIFT Provenance](../provenance/README.md) ·
[🗂️ DRIFT STAC](../stac/README.md) ·
[🏛️ Governance](../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>


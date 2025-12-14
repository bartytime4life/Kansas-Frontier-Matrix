---
title: "📜 KFM — DRIFT Provenance (PROV-O + OpenLineage · Retrieval Episodes · CARE Policy Events)"
path: "docs/search/drift/provenance/README.md"

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

intent: "drift-provenance"
audience:
  - "Search Engineering"
  - "Graph + Provenance Engineering"
  - "Catalog Engineering"
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

sensitivity: "Provenance references heritage-context retrieval episodes; CARE screening mandatory; no restricted locations in artifacts."
risk_category: "Governed"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:doc:search:drift:provenance:v11.2.6"
semantic_document_id: "kfm-drift-search-provenance"
event_source_id: "ledger:docs/search/drift/provenance/README.md"
immutability_status: "version-pinned"
machine_extractable: true

telemetry_schema: "../../../../schemas/telemetry/drift-search-v11.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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

# 📜 **KFM — DRIFT Provenance**
`docs/search/drift/provenance/README.md`

**Purpose**  
Define how DRIFT Search emits **machine-verifiable provenance** for retrieval episodes using **PROV-O JSON-LD**
(and optional **OpenLineage**), including **CARE/sovereignty policy events**, deterministic identifiers,
and validation gates.

<img src="https://img.shields.io/badge/PROV-KFM--PROV%20v11-blue" />
<img src="https://img.shields.io/badge/OpenLineage-Optional-brightgreen" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Gated-gold" />
<img src="https://img.shields.io/badge/Sensitivity-Medium%20%7C%20Redaction%20Required-orange" />
<img src="https://img.shields.io/badge/License-MIT-green" />

</div>

---

## 📘 Overview

DRIFT provenance exists to make retrieval:

- auditable (what was used, what was produced),
- replayable (index snapshot + config hashes + stable IDs),
- governed (CARE/sovereignty decisions are explicit and queryable),
- safe (no restricted locations, no doxxable identifiers, no secrets).

A “retrieval episode” is treated as a first-class governed activity:

- the **query** is represented safely (hashes, not raw text by default),
- the **inputs** include index snapshot references, policy bundles, and constraints,
- the **outputs** include evidence manifests and safe narrative payloads,
- every decision is recorded as a provenance event.

---

## 🗂️ Directory Layout

~~~text
📁 docs/search/drift/provenance/                       — Provenance reference and runbook (documentation)
├── 📄 README.md                                       — This document
└── (optional) profiles/                               — Profiles/shapes (must be provenance-safe)

📁 data/processed/prov/search/drift/                   — DRIFT retrieval provenance (operational outputs; house path)
├── 📁 episodes/
│   └── 📁 <episode_id>/
│       ├── 🧾 prov.bundle.jsonld                      — PROV-O bundle for the episode
│       ├── 🧾 openlineage.events.jsonl                — Optional OpenLineage events
│       ├── 🧾 policy.events.json                      — CARE/sovereignty policy events (summary-only)
│       └── 🧾 evidence.manifest.json                  — Evidence references only (no raw restricted content)
└── 📄 index.json                                      — Optional index of episodes (ids + timestamps only)

📁 mcp/runs/search/drift/                              — Run logs and config snapshots (reproducibility)
└── 📁 <run_id>/
    ├── 🧾 inputs.json                                 — Resolved inputs and snapshot refs
    ├── 🧾 outputs.json                                — Produced artifacts + checksums
    └── 📄 validate.log                                — Validation results
~~~

> The `data/` and `mcp/` paths above are recommended house paths. If your pipeline uses different paths, it MUST still emit:
> stable episode IDs, provenance bundles, and validation logs.

---

## 🧭 Provenance model

DRIFT uses PROV-O (JSON-LD) as the lineage truth, with optional OpenLineage for operational observability.

### Core PROV roles

- **prov:Activity**: a retrieval run (and its stages)
- **prov:Entity**: inputs/outputs (index snapshots, evidence manifests, STAC items, redaction summaries)
- **prov:Agent**: service runner, CI validator, and (optionally) reviewers

### Required relations (minimum)

- `prov:used`:
  - episode Activity **used** query representation, constraints, index snapshot refs, and policy bundle
- `prov:wasGeneratedBy`:
  - evidence manifest, policy summary, STAC item refs **generated by** the episode Activity
- `prov:wasDerivedFrom`:
  - narrative outputs are **derived from** evidence manifest and governed sources (as references)
- `prov:wasAssociatedWith`:
  - episode Activity associated with an Agent (runner)

---

## 🧱 Deterministic identifiers

All provenance identifiers MUST be stable and collision-resistant.

### Episode ID (recommended)

Derive `episode_id` deterministically from canonicalized seed material:

- `query_hash`
- `constraints` (time range, generalized region scope, role)
- `workflow_id` + `workflow_version`
- `policy_bundle_hash`
- `index_snapshot_id` (or snapshot set hash)

Recommended form:

- `urn:kfm:search:drift:episode:<sha256_16>`

### Query representation (privacy-safe)

Default posture is to store:

- `query_hash` = sha256(normalized query text)
- optional `query_summary` = short, policy-safe summary

Avoid storing raw query text unless explicitly allowed by policy and classification.

---

## 🛡️ CARE and sovereignty policy events

Because this system is `CARE-Aware Retrieval` and `redaction_required: true`, provenance MUST include explicit policy events.

### Policy event requirements

Provenance MUST record (at minimum):

- gate outcome:
  - `care_gate_status`: `allow` | `redact` | `deny`
  - `sovereignty_gate`: `clear` | `restricted` | `conflict` | `unknown`
- redaction summary:
  - counts by category (e.g., “geometry generalized”, “dataset masked”)
- denial reasons:
  - normalized reason codes only (no sensitive details)

### Prohibited in policy/provenance artifacts

Do not include:

- raw protected coordinates,
- “how to locate” instructions,
- restricted collection identifiers that enable re-identification,
- secrets, tokens, or signed URLs.

---

## 🗺️ Provenance flow

~~~mermaid
flowchart TD
  A["DRIFT retrieval run"] --> B["CARE and sovereignty gate"]
  B --> C["Evidence manifest (refs only)"]
  B --> D["Policy events (summary-only)"]
  C --> E["Narrative / Story Node stub (policy-gated)"]
  C --> F["STAC retrieval episode item (optional)"]
  D --> G["PROV bundle (JSON-LD)"]
  E --> G
  F --> G
  G --> H["Validation gates (PROV schema + leakage checks)"]
~~~

---

## 📦 Required artifacts

A governed DRIFT episode SHOULD produce:

- `prov.bundle.jsonld` (required)
- `policy.events.json` (required; summary-only)
- `evidence.manifest.json` (required; references only)
- `openlineage.events.jsonl` (optional; recommended when telemetry is enabled)

### Evidence manifest rules

The evidence manifest MUST contain only:

- stable identifiers (e.g., `urn:kfm:*`),
- catalog references (STAC/DCAT ids),
- graph entity ids,
- optional aggregate counts and types.

It MUST NOT embed full-text document content or restricted geometry.

---

## 🌐 STAC/DCAT alignment

### STAC linkage

If DRIFT emits a STAC “retrieval episode” Item:

- the STAC Item SHOULD link (via assets) to:
  - `prov.bundle.jsonld`
  - `policy.events.json`
  - `evidence.manifest.json`
- the PROV bundle SHOULD include a `prov:Entity` representing that STAC Item and relate it to the episode Activity.

### DCAT linkage (optional)

If published externally, a DCAT Distribution MAY represent the episode bundle:

- distribution href points to a governed endpoint (not raw restricted storage),
- provenance reference points to the PROV bundle id/href.

---

## 🧾 Minimal PROV bundle shape (schematic)

This snippet demonstrates expected structure with placeholders. It is schematic and not exhaustive.

~~~json
{
  "@context": [
    "https://www.w3.org/ns/prov.jsonld",
    { "kfm": "urn:kfm:" }
  ],
  "@id": "urn:kfm:prov:bundle:search:drift:episode:<episode_id>",
  "prov:activity": [
    {
      "@id": "urn:kfm:prov:activity:search:drift:episode:<episode_id>",
      "prov:startedAtTime": "2025-12-13T00:00:00Z",
      "prov:endedAtTime": "2025-12-13T00:00:10Z",
      "prov:wasAssociatedWith": { "@id": "urn:kfm:prov:agent:drift-runner" },
      "prov:used": [
        { "@id": "urn:kfm:entity:search:queryhash:<sha256>" },
        { "@id": "urn:kfm:entity:search:indexsnapshot:<snapshot_id>" },
        { "@id": "urn:kfm:entity:policy:bundle:<policy_hash>" }
      ]
    }
  ],
  "prov:entity": [
    {
      "@id": "urn:kfm:entity:search:drift:evidence-manifest:<episode_id>",
      "prov:wasGeneratedBy": { "@id": "urn:kfm:prov:activity:search:drift:episode:<episode_id>" }
    },
    {
      "@id": "urn:kfm:entity:search:drift:policy-events:<episode_id>",
      "prov:wasGeneratedBy": { "@id": "urn:kfm:prov:activity:search:drift:episode:<episode_id>" }
    }
  ],
  "prov:agent": [
    {
      "@id": "urn:kfm:prov:agent:drift-runner",
      "prov:type": "prov:SoftwareAgent"
    }
  ]
}
~~~

---

## 🧪 Validation and CI gates

DRIFT provenance MUST be validated before any governed publication.

Minimum checks:

- JSON-LD parse and structural validation (PROV-O context present and resolvable)
- required relations present:
  - Activity exists for episode
  - outputs reference `prov:wasGeneratedBy`
  - inputs recorded via `prov:used`
- determinism checks:
  - episode_id stable for identical inputs/snapshots
  - config/policy hashes recorded
- leakage checks:
  - no raw coordinates
  - no restricted dataset endpoints
  - no secrets or signed URLs

Validation outputs SHOULD be recorded under `mcp/runs/search/drift/<run_id>/validate.log`.

---

## 🧰 Operational runbook (implementation-agnostic)

A compliant DRIFT runner should:

1. Create a run context:
   - normalize query and compute `query_hash`
   - resolve index snapshot ids
   - resolve policy bundle hash
2. Execute retrieval and CARE gate.
3. Emit:
   - `evidence.manifest.json` (refs only)
   - `policy.events.json` (summary-only)
   - `prov.bundle.jsonld` (full lineage for inputs/outputs/gates)
4. Validate:
   - PROV bundle checks
   - leakage checks
5. Optionally emit:
   - STAC retrieval episode Item linking to the artifacts

---

## 🕰️ Version history

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-13 | Initial governed DRIFT provenance reference; codified deterministic IDs, required artifacts, CARE/sovereignty policy events, and validation gates. |

---

<div align="center">

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/PROV-KFM--PROV%20v11-blue" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Gated-gold" />
<img src="https://img.shields.io/badge/Sensitivity-Medium%20%7C%20Redaction%20Required-orange" />

[⬅ Back to DRIFT Search](../README.md) ·
[🔍 Search Index](../../README.md) ·
[🗂️ DRIFT STAC](../stac/README.md) ·
[🏛️ Governance](../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[🛰 Telemetry Schema](../../../../schemas/telemetry/drift-search-v11.json)

© 2025 Kansas Frontier Matrix — MIT  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>


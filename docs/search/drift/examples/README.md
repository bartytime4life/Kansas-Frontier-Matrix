---
title: "🧪 KFM — DRIFT Examples (Redaction-Safe Runs · Golden Fixtures · CI Validation)"
path: "docs/search/drift/examples/README.md"

version: "v11.2.6"
last_updated: "2025-12-13"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council Oversight"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Examples + Test Fixtures"
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

intent: "drift-examples"
audience:
  - "Search Engineering"
  - "Graph + Provenance Engineering"
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

sensitivity: "Examples must remain redaction-safe; no restricted locations or re-identifying joins."
risk_category: "Governed"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:doc:search:drift:examples:v11.2.6"
semantic_document_id: "kfm-drift-search-examples"
event_source_id: "ledger:docs/search/drift/examples/README.md"
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

# 🧪 **KFM — DRIFT Examples**
`docs/search/drift/examples/README.md`

**Purpose**  
Provide **redaction-safe example runs** and **golden fixtures** for DRIFT Search that support:
determinism tests, CARE leakage checks, provenance validation (PROV/OpenLineage), and STAC episode emission validation.

<img src="https://img.shields.io/badge/Examples-Redaction--Safe-brightgreen" />
<img src="https://img.shields.io/badge/CI-Golden%20Fixtures-blue" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Gated-gold" />
<img src="https://img.shields.io/badge/Sensitivity-Medium%20%7C%20Redaction%20Required-orange" />
<img src="https://img.shields.io/badge/License-MIT-green" />

</div>

---

## 📘 Overview

This directory contains **example DRIFT retrieval episodes** suitable for:

- onboarding (how DRIFT structures inputs/outputs),
- regression testing (golden outputs under deterministic configuration),
- policy testing (CARE and sovereignty gates),
- provenance testing (PROV-O bundles and optional OpenLineage event streams),
- STAC testing (retrieval episode STAC Items and assets).

### Redaction-first posture (non-negotiable)

All examples MUST be safe to publish in-repo:

- no raw protected coordinates,
- no restricted site identifiers that enable re-identification,
- no secret URLs, tokens, or signed links,
- no “how to locate” instructions.

Where specificity is required, use:

- `query_hash` and a short, policy-safe `query_summary`,
- generalized spatial scope (region id or coarse H3),
- stable URNs that do not resolve to restricted content without access controls.

---

## 🗂️ Directory Layout

~~~text
📁 docs/search/drift/examples/                          — DRIFT example runs (redaction-safe)
├── 📄 README.md                                        — This document
├── 📁 episode_minimal/                                 — Smallest valid DRIFT episode (happy path)
│   ├── 🧾 query.example.json                            — Query representation (hash + safe summary)
│   ├── 🧾 constraints.example.json                      — Time + generalized space + role constraints
│   ├── 🧾 run_context.example.json                      — Determinism + versions + hashes (template/policy/index)
│   ├── 🧾 anchors.example.json                          — Vector anchors (ids + scores; no sensitive content)
│   ├── 🧾 graph_results.example.json                    — Graph-local results (refs-only; no geometry)
│   ├── 🧾 evidence.manifest.example.json                — Evidence bundle (refs-only)
│   ├── 🧾 policy.events.example.json                    — CARE/sovereignty policy events (summary-only)
│   ├── 🧾 prov.bundle.example.jsonld                    — PROV-O episode bundle (validated)
│   └── 🧾 stac.item.example.json                        — STAC retrieval episode Item (optional)
├── 📁 episode_redaction/                               — Demonstrates redaction/generalization behavior
│   ├── 🧾 query.example.json
│   ├── 🧾 constraints.example.json
│   ├── 🧾 policy.events.example.json                    — Shows redact/deny outcomes (summary-only)
│   ├── 🧾 evidence.manifest.example.json                — References only; sensitive entities omitted/aggregated
│   └── 🧾 prov.bundle.example.jsonld
└── 📁 episode_deny/                                     — Demonstrates fail-closed behavior
    ├── 🧾 query.example.json
    ├── 🧾 constraints.example.json
    ├── 🧾 policy.events.example.json                    — Deny reason codes (normalized)
    └── 🧾 prov.bundle.example.jsonld
~~~

> Examples are documentation and fixtures. If you need restricted examples (e.g., internal coordinates), store them in an
> access-controlled system and reference only non-sensitive hashes/ids here.

---

## 🧭 What an example “episode” contains

A DRIFT example episode is a compact representation of an execution:

- inputs (query + constraints + determinism settings),
- intermediate retrieval products (anchors and graph results),
- governance outputs (policy events, redaction summary),
- evidence outputs (refs-only manifest),
- provenance outputs (PROV bundle; optional OpenLineage),
- optional STAC episode Item referencing artifacts.

---

## 📦 Example file contracts

### `query.example.json` (recommended)

- MUST contain `query_hash`
- SHOULD contain a policy-safe `query_summary`
- MUST NOT contain raw query text if it would create leakage risk

~~~json
{
  "query_hash": "sha256:…",
  "query_redacted": true,
  "query_summary": "Generalized query summary suitable for public docs."
}
~~~

### `constraints.example.json` (recommended)

- generalized spatial scope only
- explicit time bounds when used

~~~json
{
  "time_range": { "start": "1850-01-01", "end": "1900-12-31" },
  "spatial_scope": { "type": "region", "region_id": "kansas" },
  "role": "public"
}
~~~

### `run_context.example.json` (recommended)

- determinism controls and pinned version identifiers

~~~json
{
  "episode_id": "urn:kfm:search:drift:episode:0123abcd4567ef89",
  "workflow_id": "drift:hybrid-global-local",
  "workflow_version": "v11.2.6",
  "determinism": {
    "seed": 1337,
    "timezone": "UTC",
    "locale": "C",
    "temperature": 0
  },
  "hashes": {
    "template_hash": "sha256:…",
    "policy_bundle_hash": "sha256:…",
    "index_snapshot_id": "urn:kfm:search:index:snapshot:…"
  },
  "code_commit_sha": "<latest-commit-hash>"
}
~~~

### `graph_results.example.json` (required to be safe)

- MUST be refs-only and avoid geometry fields
- SHOULD include node types/labels and stable ids

~~~json
{
  "nodes": [
    { "urn": "urn:kfm:entity:…", "labels": ["Place"], "display": "Generalized place label" }
  ],
  "edges": [
    { "from": "urn:kfm:entity:…", "to": "urn:kfm:entity:…", "type": "RELATED_TO" }
  ]
}
~~~

### `policy.events.example.json` (required)

- MUST include gate outcomes and redaction summary
- MUST NOT include sensitive details

~~~json
{
  "care_gate_status": "redact",
  "sovereignty_gate": "unknown",
  "redaction_summary": {
    "events_total": 2,
    "reasons": ["spatial_precision_reduced", "restricted_terms_masked"]
  }
}
~~~

---

## 🗺️ Example episode flow

~~~mermaid
flowchart TD
  A["Query (hash + summary)"] --> B["HyDE expansion (internal)"]
  B --> C["Vector anchors (safe ids + scores)"]
  C --> D["Graph-local retrieval (refs-only)"]
  D --> E["CARE + sovereignty gate (summary-only)"]
  E --> F["Evidence manifest (refs-only)"]
  F --> G["PROV bundle (JSON-LD)"]
  F --> H["STAC episode item (optional)"]
~~~

---

## 🧪 How CI should use these examples

Examples can be used as fixtures for:

- determinism tests:
  - stable episode ids and stable output ordering
- policy tests:
  - correct allow/redact/deny behavior for known cases
- leakage tests:
  - ensure example outputs never contain coordinate-like patterns or restricted endpoints
- schema tests:
  - validate PROV bundles against KFM-PROV profile (v11)
  - validate STAC Items against KFM-STAC profile (v11), where included

---

## ⚖ FAIR+CARE & Governance

All example content MUST remain:

- public-safe and redaction-safe,
- provenance-complete (PROV bundle included for each example episode),
- compliant with Indigenous data protection policies.

If an example cannot be made safe:

- do not include it in this directory,
- include only hashed identifiers and normalized policy outcomes.

---

## 🕰️ Version history

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-13 | Initial governed DRIFT examples index; defined required example episode fixtures and CI validation posture. |

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


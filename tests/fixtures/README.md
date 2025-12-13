---
title: "🧱 Kansas Frontier Matrix — Test Fixtures & Mock Data (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/fixtures/README.md"
version: "v11.2.6"
last_updated: "2025-12-13"
review_cycle: "Continuous · Autonomous Systems Oversight · FAIR+CARE Council"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-sha256>"
doc_integrity_checksum: "<sha256>"
signature_ref: "../../../releases/v11.2.6/signatures/tests-fixtures-readme.sig"
event_source_id: "ledger:tests/fixtures/README.md"
immutability_status: "version-pinned"

sbom_ref: "../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.6/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../releases/v11.2.6/tests-fixtures-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/tests-fixtures-v11.json"

validation_reports:
  - "../../../reports/self-validation/work-tests-fixtures.json"
  - "../../../reports/fair/tests_fixtures_summary.json"
  - "../../../reports/audit/ai_tests_fixtures_ledger.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

status: "Active / Enforced"
doc_kind: "Fixtures Guide"
intent: "tests-fixtures-overview"
semantic_document_id: "kfm-doc-tests-fixtures"
doc_uuid: "urn:kfm:tests:fixtures:v11.2.6"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
classification: "Testing · Mock Data · Synthetic Data"
sensitivity: "Low"
fair_category: "F1-A1-I2-R3"
care_label: "Ethical · Public · Low-Risk"

ttl_policy: "12-month review"
sunset_policy: "Superseded upon v12 fixture architecture"

provenance_chain:
  - "tests/fixtures/README.md@v11.0.0"
  - "tests/fixtures/README.md@v11.2.6"

ai_transform_permissions:
  - "summarize"
  - "extract_metadata"
  - "generate_checklists"
  - "propose_fixture_additions_non_authoritative"
ai_transform_prohibited:
  - "fabricate_provenance_or_hashes"
  - "insert_secrets_tokens_or_credentials"
  - "include_or_infer_pii"
  - "introduce_real_world_sensitive_coordinates"
  - "weaken_sovereignty_or_masking_rules"
  - "change_governance_status_language"
---

<div align="center">

# 🧱 **Kansas Frontier Matrix — Test Fixtures & Mock Data (v11 LTS)**
`tests/fixtures/README.md`

**Purpose**  
Define the **canonical synthetic fixture suite** used by the KFM v11 Test Platform to enable **deterministic, sovereignty-safe, FAIR+CARE-aligned testing** of ETL, AI, governance, Story Node v3, Focus Mode v3, STAC/DCAT, and telemetry pipelines.

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Governance%20Aligned-orange" />
<img src="https://img.shields.io/badge/Accessibility-WCAG_2.1_AA%2B-blueviolet" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

</div>

---

## 📘 Overview

The fixture layer is the **safety boundary** for KFM tests.

Fixtures are **synthetic**, **non-identifying**, **version-pinned** datasets and payloads that:

- prevent accidental leakage of sensitive or sovereign information
- enable deterministic CI runs (local and hosted)
- provide representative shapes for schema, provenance, and governance checks
- validate behavior under both **success** and **expected failure** conditions

### ✅ Guarantees

Fixtures in `tests/fixtures/` MUST guarantee:

- **No PII** (names, emails, phone numbers, addresses, IDs)
- **No real-world sensitive locations** (sacred sites, archaeological sites, restricted lands)
- **No production secrets** (tokens, keys, credentials, internal endpoints)
- **Determinism** (seeded generation, stable ordering, reproducible hashes)
- **Schema fidelity** (aligns with:
  - Story Node v3 schema + SHACL shapes
  - STAC 1.x + DCAT 3.0 metadata expectations
  - Telemetry v11 events
  - `data-contract-v3.json` constraints)

### 🚫 Non-goals

Fixtures are not intended to:

- mirror full production volumes
- encode private, licensed, or restricted datasets
- approximate real tribal geographies or culturally sensitive water-use patterns
- serve as “sample data” for public demonstrations unless explicitly curated for that purpose

### 🧩 Fixture categories

KFM fixtures are organized into **four primary categories**:

1. **📦 Data fixtures** — tabular, vector, raster, time-series, document snippets (synthetic)
2. **🧠 AI fixtures** — deterministic mock model outputs + XAI artifacts (SHAP/LIME-like payloads)
3. **🧬 Governance fixtures** — synthetic ledger entries, policy outcomes, audit traces
4. **📊 Observability fixtures** — telemetry events, energy/CO₂ stubs, runtime summaries

---

## 🗂️ Directory Layout

~~~text
📁 tests/
├── 📁 fixtures/                                      — Synthetic, deterministic fixtures (THIS DIRECTORY)
│   ├── 📄 README.md                                  — Fixture governance + usage rules (this document)
│   ├── 🧾 metadata.json                               — Fixture pack metadata (IDs, dates, owners, scopes)
│   ├── 🧾 mock_manifest.json                          — SHA-256 manifest for all fixture files
│   │
│   ├── 📁 data/                                       — Synthetic datasets (contract-aligned)
│   │   ├── 🧾 mock_dataset.contract_v3.json            — Minimal contract-aligned dataset (tabular-like)
│   │   ├── 🧾 mock_timeseries.daily.json               — Synthetic hydrology/climate time-series
│   │   ├── 🧾 mock_vector.geojson                      — Synthetic GeoJSON geometries (safe region)
│   │   └── 🧾 mock_raster.stac_item.json               — STAC Item stub for a raster-like asset
│   │
│   ├── 📁 ai/                                         — Synthetic AI inputs/outputs (NO training data)
│   │   ├── 🧾 mock_ai_output.focusmode_v3.json         — Focus Mode-like payload + citations stubs
│   │   ├── 🧾 mock_xai.shap_summary.json               — SHAP-style summary payload (synthetic)
│   │   └── 🧾 mock_drift_report.json                   — Embedding/drift report stub (synthetic)
│   │
│   ├── 📁 governance/                                 — Synthetic governance + sovereignty artifacts
│   │   ├── 🧾 mock_ledger_entry.prov_care.json          — Ledger entry with CARE + sovereignty flags
│   │   ├── 🧾 mock_policy_decision.json                — Policy result: allow/restrict/escalate
│   │   └── 🧾 mock_audit_trace.json                    — Governance audit trace (synthetic)
│   │
│   ├── 📁 telemetry/                                  — Telemetry event fixtures
│   │   ├── 🧾 mock_tests_telemetry_v11.json             — Tests telemetry event bundle (energy/CO₂/runtime)
│   │   └── 🧾 mock_accessibility_metrics.json           — A11y summary fixture (WCAG checks)
│   │
│   └── 📁 negative/                                   — Intentional failures to assert CI gates
│       ├── 🧾 bad_schema.storynode.json                 — Violates Story Node schema (expected fail)
│       ├── 🧾 bad_metadata.stac_item.json               — Violates STAC fields (expected fail)
│       └── 🧾 bad_governance.flags.json                 — Violates CARE/sovereignty policy (expected fail)
└── …
~~~

---

## 📦 Data & Metadata

### 1) Naming conventions

Fixtures MUST follow:

- lowercase filenames
- explicit domain + purpose + version markers where relevant  
  Examples:
  - `mock_dataset.contract_v3.json`
  - `mock_ai_output.focusmode_v3.json`
  - `mock_tests_telemetry_v11.json`

### 2) Determinism and seed policy

All generated fixtures MUST be reproducible.

- Use a single constant seed for the fixture pack:
  - `KFM_TEST_SEED = 114226` (do not change without bumping pack version)
- If a fixture needs multiple streams, derive sub-seeds deterministically:
  - `seed_sub = sha256("fixture-name" + KFM_TEST_SEED)[:8]`

Record seed usage in `metadata.json`.

### 3) Geometry and coordinate policy

Fixtures MUST be sovereignty-safe.

Rules:

- Prefer **H3-only** geometry representations for governance-sensitive flows.
- If raw GeoJSON is required, use the **KFM Synthetic Reference Box (SRB)**:
  - a small bounding box around **Null Island** (0,0) to avoid Kansas/tribal geography coupling
  - never use real-world heritage coordinates

Recommended SRB:

~~~json
{
  "srb_name": "KFM_SRB_NULL_ISLAND",
  "crs": "EPSG:4326",
  "bbox": [-0.01, -0.01, 0.01, 0.01]
}
~~~

### 4) Minimum required fixture metadata

`tests/fixtures/metadata.json` MUST include:

- `fixture_pack_id` (stable)
- `version` (matches front-matter)
- `created_utc`
- `seed`
- `scope` (what tests rely on it)
- `owner_group` (routing)
- `policy_assertions` (e.g., “no_pii”, “no_sensitive_coords”)
- `hash_manifest_ref`

Example:

~~~json
{
  "fixture_pack_id": "kfm-tests-fixtures",
  "version": "v11.2.6",
  "created_utc": "2025-12-13T00:00:00Z",
  "seed": 114226,
  "owner_group": "@kfm-tests",
  "scope": ["unit", "integration", "e2e", "schema", "governance", "telemetry", "a11y"],
  "policy_assertions": ["no_pii", "no_secrets", "no_sensitive_coords", "deterministic"],
  "hash_manifest_ref": "tests/fixtures/mock_manifest.json"
}
~~~

### 5) Checksum manifest rules

`mock_manifest.json` is the integrity anchor.

Requirements:

- SHA-256 for every file in `tests/fixtures/**`
- stable sort order by path
- manifest includes its own SHA-256 in the footer metadata

Example structure:

~~~json
{
  "algorithm": "sha256",
  "generated_utc": "2025-12-13T00:00:00Z",
  "files": [
    { "path": "tests/fixtures/data/mock_timeseries.daily.json", "sha256": "<sha256>" }
  ],
  "manifest_sha256": "<sha256>"
}
~~~

---

## 🧱 Architecture

### 1) Fixture lifecycle

Fixtures follow a controlled lifecycle:

1. **Author or generator** creates/updates fixture files (deterministic)
2. **Schema validation** runs locally and in CI
3. **Manifest rebuild** updates checksums
4. **Governance checks** assert no PII/secrets/sensitive coords
5. **Telemetry snapshot** records fixture-run cost envelope
6. **Merge gating** blocks if any rule fails

### 2) Fixture “pack” concept

Fixtures are treated as a **pack** with a single version:

- pack changes require:
  - bumping `version`
  - updating `last_updated`
  - updating `provenance_chain`
  - regenerating `mock_manifest.json`

### 3) Negative fixtures

Negative fixtures are REQUIRED to prevent silent regressions.

Rules:

- Store under `tests/fixtures/negative/`
- Each negative fixture MUST document the expected failure:
  - schema failure
  - governance failure
  - telemetry schema failure

Include an “expected failure descriptor” adjacent to the file when useful:

~~~json
{
  "fixture": "bad_schema.storynode.json",
  "expected_failure": "schema-lint",
  "reason": "missing required field: spacetime.when"
}
~~~

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Test runner loads fixture pack"] --> B["Schema and contract validation"]
  B --> C["Pipeline under test executes"]
  C --> D["Governance checks: CARE and sovereignty"]
  D --> E["Provenance output checks: PROV-O and OpenLineage"]
  E --> F["Telemetry checks: energy, CO2, runtime, A11y"]
  F --> G["CI gate decision: pass or block"]
~~~

This flow is intentionally **linear and deterministic** so failures are attributable to a single step boundary.

---

## 🌐 STAC, DCAT & PROV Alignment

Fixtures exist to validate KFM’s interoperability layer without using real data.

### STAC expectations (fixture-level)

- Provide minimal viable STAC Item / Collection shapes for schema tests
- Include placeholder `assets` with safe dummy URIs
- Keep geometry within SRB (or omit geometry if schema allows)

### DCAT expectations (fixture-level)

- DCAT fixtures should validate:
  - dataset identity and versioning fields
  - license and access fields (public)
  - temporal coverage shapes

### PROV-O / OpenLineage expectations (fixture-level)

Fixtures validate that tests and pipelines can emit provenance **without inventing** relationships.

A minimal PROV-O fixture block should include:

~~~json
{
  "prov:entity": "fixture_run_output",
  "prov:wasGeneratedBy": "tests.fixtures.validation",
  "prov:used": ["tests/fixtures/metadata.json", "tests/fixtures/mock_manifest.json"],
  "prov:wasAssociatedWith": "kfm-ci"
}
~~~

---

## 🧠 Story Node & Focus Mode Integration

Fixtures support **safe testing** for narrative-adjacent subsystems:

### Story Node v3

Fixtures should exercise:

- schema-required fields and shapes
- sovereignty masking behavior (prefer H3-only)
- citation placeholders (no real citations required in fixtures)
- narrative safety checks (no speculation; neutral tone)

### Focus Mode v3

Fixtures should exercise:

- “3-panel” payload structures (Context, Timeline, Map)
- citation formatting and provenance links
- refusal behavior when a prompt attempts to bypass governance

---

## 🧪 Validation & CI/CD

Fixture compliance is CI-enforced (minimum profiles):

- `schema-lint`
- `metadata-check`
- `provenance-check`
- `secret-scan`
- `pii-scan`
- `diagram-check`
- `footer-check`

### Local validation checklist

Run before committing fixture changes:

~~~text
1) Validate JSON schemas (Story Node / STAC / telemetry)
2) Validate fixture metadata completeness
3) Regenerate mock_manifest.json (sha256)
4) Run secret scan + PII scan
5) Run tests that consume fixtures (unit + integration smoke)
~~~

### CI behavior

- Any fixture failure blocks:
  - PR merges
  - release promotion
  - governance certification

---

## ⚖ FAIR+CARE & Governance

Fixtures are governed artifacts even when “only tests”.

### CARE posture (fixture pack)

- **Collective Benefit:** ensures safe QA across the platform
- **Authority to Control:** fixtures cannot approximate restricted geographies
- **Responsibility:** maintainers must prevent leakage and bias patterns
- **Ethics:** fixtures must not encode harmful or discriminatory content

### Sovereignty posture (fixture pack)

- fixtures MUST NOT contain:
  - tribal land boundaries
  - sacred sites
  - sensitive archaeological coordinates
  - culturally identifying text

If a test requires verifying masking behavior, it must do so with:

- SRB geometry and/or H3-only representations
- synthetic policy flags (no real-world inferences)

---

## 🕰️ Version History

| Version | Date | Summary |
|--------:|------|---------|
| v11.2.6 | 2025-12-13 | Upgraded to KFM-MDP v11.2.6; added fixture pack taxonomy, negative fixtures, SRB geometry policy, deterministic seed rules, checksum manifest requirements, and CI validation checklist. |
| v11.0.0 | 2025-11-24 | Initial v11 fixtures guide; sovereignty-safe synthetic fixtures; telemetry v11 alignment; CARE-aware test scaffolding. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
🧱 Synthetic QA · FAIR+CARE Governance · Sovereignty-Safe Testing · KFM-MDP v11.2.6

[⬅️ Back to Tests Index](../README.md) ·
[🧪 Test Architecture](../ARCHITECTURE.md) ·
[🏛️ Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

</div>

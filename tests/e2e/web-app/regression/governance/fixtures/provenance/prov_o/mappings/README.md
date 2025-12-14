---
title: "🧾 Kansas Frontier Matrix — PROV-O Fixture Mappings (Governance E2E) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/governance/fixtures/provenance/prov_o/mappings/README.md"

version: "v11.2.6"
last_updated: "2025-12-13"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous Systems Oversight · FAIR+CARE Council"
content_stability: "stable"

status: "Active · Enforced"
doc_kind: "Fixtures Guide"
header_profile: "standard"
footer_profile: "standard"
intent: "tests-e2e-web-app-regression-governance-fixtures-provenance-prov-o-mappings"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-regression-governance-fixtures-provenance-prov-o-mappings-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:governance:fixtures:provenance:prov-o:mappings:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/governance/fixtures/provenance/prov_o/mappings/README.md"
immutability_status: "version-pinned"
machine_extractable: true

classification: "Public Document"
sensitivity: "Low"
public_exposure_risk: "Low"
fair_category: "F1-A1-I2-R3"
care_label: "Public · Low-Risk"
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../../../../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../../../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../../../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../../../../../../releases/v11.2.6/tests-e2e-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/tests-e2e-v11.json"
energy_schema: "../../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

ttl_policy: "6-month review"
sunset_policy: "Superseded upon next v12 E2E framework update"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
  - "layout-normalization"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"
  - "sensitive-coordinate-disclosure"
  - "pii-insertion"
  - "secret-insertion"

provenance_chain:
  - "tests/e2e/web-app/regression/governance/fixtures/provenance/prov_o/mappings/README.md@v11.2.6"
---

<div align="center">

# 🧾 **PROV‑O Fixture Mappings (Governance E2E) (v11 LTS)**
`tests/e2e/web-app/regression/governance/fixtures/provenance/prov_o/mappings/README.md`

**Purpose**  
Define the **canonical mapping fixtures** that connect **PROV‑O fixture bundles/fragments** to:
- regression scenario IDs,
- normalized evidence surfaces (IDs, hashes, references),
- stable UI expectations (provenance chips, links, and governance overlays).

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Surface-Governance%20E2E-blueviolet" />
<img src="https://img.shields.io/badge/Provenance-PROV--O-informational" />
<img src="https://img.shields.io/badge/Governance-FAIR%2BCARE-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ PROV‑O Fixtures](../README.md) ·
[⬅️ Governance Provenance](../../README.md) ·
[🧭 Governance Regression](../../../README.md)

</div>

---

## 📘 Overview

This folder contains **mapping fixtures** that make PROV‑O test data **runner-friendly** and **assertion-friendly**.

These mappings exist to solve a recurring E2E problem:

- PROV‑O fixtures are often stored as **bundles** (multiple JSON fragments) or as **fragments** (partial graphs).
- E2E regression specs need a stable way to:
  - select which PROV‑O entities/activities matter for a scenario,
  - normalize label aliases (human-friendly names vs stable IDs),
  - verify that provenance UI surfaces show **IDs and references** without leaking full payloads.

**What mappings do**
- 🧷 Bind `scenario_id` → PROV‑O bundle(s) and fragment(s)
- 🧭 Define “expected provenance anchors” (experiment IDs, dataset IDs, model card IDs)
- 🧾 Provide stable aliasing (e.g., “Hydrology Reconstruction Run” → `prov:Activity` ID)
- 🛡️ Enforce safe reporting patterns (IDs/hashes only; no full dumps)

**What mappings do not do**
- They do not invent provenance.
- They do not replace application governance controls.
- They do not store real-world identifiers, sensitive coordinates, or restricted content.

---

## 🗂️ Directory Layout

This folder is one layer inside the PROV‑O fixture hierarchy.

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 regression/
            └── 📁 governance/
                └── 📁 fixtures/
                    └── 📁 provenance/
                        └── 📁 prov_o/
                            ├── 📄 README.md                               — PROV‑O fixtures overview (parent)
                            │
                            ├── 📁 bundles/                                — Full synthetic PROV‑O bundles (scenario-ready)
                            ├── 📁 expected/                               — Expected normalized provenance anchors
                            ├── 📁 fragments/                              — Reusable partial PROV‑O graphs (small pieces)
                            │
                            └── 📁 mappings/                               — This folder (mapping layer)
                                ├── 📄 README.md                           — This guide
                                ├── 🧾 scenario_to_bundle.json             — scenario_id → bundle path(s)
                                ├── 🧾 scenario_to_fragments.json          — scenario_id → fragment path(s)
                                ├── 🧾 alias_registry.json                 — stable aliases for UI-facing labels
                                └── 🧾 entity_role_map.json                — canonical “roles” for entities/activities
~~~

Notes:
- Filenames above represent the **canonical target layout** for mapping fixtures.
- If your repo uses different names, keep the same **intent**, **separation**, and **safety constraints**.

---

## 🧭 Context

### Why mappings exist (determinism + auditability)

Without mappings, governance E2E specs tend to:
- hardcode fixture paths inside test logic,
- duplicate aliasing rules across suites,
- assert against brittle UI text instead of stable IDs,
- accidentally print too much context when debugging.

Mappings keep provenance assertions:
- ✅ deterministic (stable selection and stable normalization),
- ✅ small (minimal “what matters” definitions),
- ✅ safe (no payload dumps required to diagnose failures),
- ✅ consistent across governance suites.

### Safety rules (non-negotiable)

Mapping fixtures MUST:
- reference only **synthetic** PROV‑O bundles/fragments,
- avoid realistic coordinate-like or location-like values,
- use **IDs/hashes** as anchors (placeholders allowed, e.g., `<sha256>`),
- remain safe to publish as part of a public repo.

Mapping fixtures MUST NOT:
- include raw “document body” fields,
- embed full API response payloads,
- embed secrets, tokens, credentials, or private URLs.

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["E2E selects scenario_id"] --> B["Load scenario mappings"]
  B --> C["Load PROV-O bundles or fragments"]
  C --> D["Normalize aliases and roles"]
  D --> E["Render provenance UI surface"]
  E --> F["Assert anchors and governance invariants"]
~~~

Interpretation:
- Mappings convert “scenario intent” into deterministic fixture selection and stable provenance assertions.

---

## 🧠 Story Node & Focus Mode Integration

Governance regression often validates provenance surfaces that appear in:

- Story Node v3 pages (provenance chips, dataset references)
- Focus Mode v3 (evidence references, experiment/model card links)

Mapping fixtures SHOULD support:
- scenario-level expectations like “this page must show at least one experiment reference”,
- stable anchor checks like “the UI displays the prov:Activity ID (or its alias)”.

Mapping fixtures MUST NOT:
- encode narrative content,
- encode sensitive site information,
- make claims about real events.

---

## 🧪 Validation & CI/CD

Mapping fixtures are validated and scanned as part of governance E2E suites.

Mappings MUST pass:
- ✅ JSON parse validation
- ✅ schema validation (if/when a mapping schema exists)
- ✅ secret scan
- ✅ PII scan (best-effort)
- ✅ governance safety lint (no coordinate-like patterns, no payload dumps)

Recommended lint rules for mappings:
- enforce stable key ordering (or apply a formatter in CI),
- require `schema_version`,
- require that every referenced path stays within `tests/e2e/**`,
- forbid external URLs unless explicitly whitelisted and non-sensitive.

---

## 📦 Data & Metadata

### Recommended mapping file: `scenario_to_bundle.json`

Purpose:
- deterministic selection of a PROV‑O bundle for a scenario.

~~~json
{
  "schema_version": "v11.2.6",
  "scenarios": {
    "gov_masking_required": {
      "bundles": [
        "../bundles/gov_masking_required_bundle.json"
      ],
      "tags": ["@regression", "@governance"]
    }
  }
}
~~~

### Recommended mapping file: `scenario_to_fragments.json`

Purpose:
- compose scenarios from reusable fragments.

~~~json
{
  "schema_version": "v11.2.6",
  "scenarios": {
    "gov_provenance_minimal": {
      "fragments": [
        "../fragments/prov_activity_minimal.json",
        "../fragments/prov_entities_minimal.json"
      ]
    }
  }
}
~~~

### Recommended mapping file: `alias_registry.json`

Purpose:
- provide stable, human-readable aliases while anchoring to stable IDs.

~~~json
{
  "schema_version": "v11.2.6",
  "aliases": {
    "activity:hydro_reconstruction_run": {
      "prov_id": "prov:activity:hydro_recon_001",
      "label": "Hydrology Reconstruction Run"
    },
    "entity:dataset_stub": {
      "prov_id": "prov:entity:stac_hydro_stub",
      "label": "Synthetic Hydrology Dataset"
    }
  }
}
~~~

### Recommended mapping file: `entity_role_map.json`

Purpose:
- normalize “what this thing is used for” (so tests can assert intent safely).

~~~json
{
  "schema_version": "v11.2.6",
  "roles": {
    "primary_activity": ["prov:activity:hydro_recon_001"],
    "input_entities": ["prov:entity:stac_hydro_stub"],
    "output_entities": ["prov:entity:recon_series_stub"]
  }
}
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

These are test fixtures (not production datasets):

- **DCAT**: mapping JSONs can be treated as `dcat:Distribution` artifacts (`mediaType: application/json`) if cataloged.
- **STAC**: if represented, use:
  - `geometry: null`
  - `properties.datetime` as fixture generation/update time
  - assets: mapping JSON file(s)
- **PROV‑O**:
  - mapping fixtures are `prov:Entity` that *describe how to select other entities*,
  - the E2E run is a `prov:Activity`,
  - CI runners and maintainers are `prov:Agent`.

---

## 🧱 Architecture

### How mappings are consumed (recommended pattern)

1. Scenario selection
   - spec chooses a `scenario_id` (tagged via `@governance`, `@regression`)

2. Fixture resolution
   - load `scenario_to_bundle.json` and/or `scenario_to_fragments.json`
   - resolve file paths deterministically

3. Normalization
   - apply `alias_registry.json` and `entity_role_map.json`
   - build a minimal “expected anchors” object for UI assertions

4. Assertion
   - assert that provenance UI shows anchors (IDs/labels)
   - assert governance invariants (no raw precision, no restricted bypass)

### Anti-patterns (avoid)
- hardcoding fixture paths inside every spec file
- asserting full JSON payload equality for PROV‑O graphs
- printing full PROV‑O bundles in CI output on failure

---

## ⚖ FAIR+CARE & Governance

Mapping fixtures support governance by ensuring provenance remains:

- **Findable** (stable IDs and aliases)
- **Auditable** (deterministic selection and normalization)
- **Safe** (no raw sensitive precision; no restricted content)
- **Respectful** (no culturally harmful framing; no inference traps)

If a mapping change weakens governance:
- treat it as a governance-impacting change,
- require review from the appropriate working group and FAIR+CARE Council,
- prefer fixing the underlying app behavior rather than loosening mapping constraints.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Initial PROV‑O mappings guide aligned to KFM‑MDP v11.2.6 (deterministic scenario mapping, safe aliasing, governance‑friendly assertions). |

<div align="center">

[🏛️ Governance Charter](../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>


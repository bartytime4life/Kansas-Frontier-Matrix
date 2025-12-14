---
title: "🧾 Kansas Frontier Matrix — Governance Provenance Fixtures (E2E) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/governance/fixtures/provenance/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous Systems Oversight · FAIR+CARE Council"
content_stability: "stable"

status: "Active · Enforced"
doc_kind: "Fixtures Guide"
header_profile: "standard"
footer_profile: "standard"
intent: "tests-e2e-web-app-regression-governance-fixtures-provenance"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-regression-governance-fixtures-provenance-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:governance:fixtures:provenance:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/governance/fixtures/provenance/README.md"
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

signature_ref: "../../../../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../../../../releases/v11.2.6/tests-e2e-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/tests-e2e-v11.json"
energy_schema: "../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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
  - "tests/e2e/web-app/regression/governance/fixtures/provenance/README.md@v11.2.6"
---

<div align="center">

# 🧾 **Governance Provenance Fixtures (E2E) (v11 LTS)**
`tests/e2e/web-app/regression/governance/fixtures/provenance/README.md`

**Purpose**  
Define the **canonical synthetic provenance fixture layer** used by governance E2E regression suites.  
Fixtures in this folder simulate **PROV‑O + OpenLineage + governance mapping** surfaces in a way that is **deterministic**, **auditable**, and **sovereignty-safe** (IDs/hashes only; no payload dumps; no sensitive precision).

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Surface-Web%20App%20E2E-blueviolet" />
<img src="https://img.shields.io/badge/Provenance-PROV--O%20%2B%20OpenLineage-informational" />
<img src="https://img.shields.io/badge/Governance-FAIR%2BCARE-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Governance Fixtures](../README.md) ·
[⬅️ Governance Regression](../../README.md) ·
[🧭 E2E Guide](../../../../../README.md)

</div>

---

## 📘 Overview

This folder provides **synthetic provenance fixtures** that governance suites use to validate:

- 🧬 **Provenance surfaces are present** (IDs, hashes, references are non-empty).
- 🔗 **Cross-mappings are consistent** (OpenLineage job/run ↔ PROV‑O activity/entity ↔ UI evidence chips).
- 🛡️ **Redaction and masking rules hold** (no raw dumps; no coordinate-like fragments; no restricted reconstruction).
- 🧾 **Auditability** (fixtures are small, diff-friendly, and stable; a reviewer can understand intent quickly).

These fixtures are intentionally designed to be:
- **ID-first**: stable identifiers, not full documents.
- **Minimal**: smallest payload that still exercises UI logic.
- **Deterministic**: stable ordering, stable timestamps (or timestamp-free when possible).
- **Safe**: no PII, no secrets, no sensitive precision, no realistic “fake site” data.

**Non-goals**
- This folder is not a full provenance archive.
- Fixtures are not intended to mirror real-world ledger contents.
- Fixtures do not attempt to “prove correctness” of historical or scientific claims—only governance/provenance UI invariants.

---

## 🗂️ Directory Layout

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 regression/
            └── 📁 governance/
                └── 📁 fixtures/
                    └── 📁 provenance/
                        ├── 📄 README.md                          — This guide
                        │
                        ├── 🧾 provenance_registry.json            — Scenario ID → provenance fixture bundle map
                        │
                        ├── 📁 governance/                         — Governance-facing fragments (tiers, flags, redaction cues)
                        │   ├── 🧾 gov_public.json                  — Public governance state (synthetic)
                        │   ├── 🧾 gov_masked.json                  — Masked governance state (synthetic)
                        │   └── 🧾 gov_restricted.json              — Restricted/blocked governance state (synthetic)
                        │
                        ├── 📁 mappings/                           — Crosswalks between IDs used by UI and lineage systems
                        │   ├── 🧾 entity_id_map.json               — UI entity IDs → synthetic canonical IDs
                        │   ├── 🧾 evidence_id_map.json             — Evidence chip IDs → dataset/model/experiment anchors
                        │   └── 🧾 run_id_map.json                  — run_id/job_id → scenario + bundle anchors
                        │
                        ├── 📁 openlineage/                        — OpenLineage-like fragments (job/run + facets, minimal)
                        │   ├── 🧾 job_fragment.json
                        │   ├── 🧾 run_fragment.json
                        │   └── 🧾 dataset_facets.json
                        │
                        └── 📁 prov_o/                              — PROV‑O-like fragments (Activity/Entity/Agent, minimal)
                            ├── 🧾 prov_activity.json
                            ├── 🧾 prov_entity.json
                            └── 🧾 prov_agent.json
~~~

Notes:
- Names above are the **canonical target layout** for a governance-friendly provenance fixture set.
- If your suite consolidates fragments into fewer files, keep the same safety posture: **IDs/hashes only**, no full dumps.

---

## 🧭 Context

### Safety posture (IDs and hashes, not payload dumps)

Fixtures MUST:
- include only **stable identifiers** and **hash placeholders** (e.g., `<sha256>`),
- avoid embedding full documents, full API responses, or full ledger records,
- avoid any geometry-bearing keys unless explicitly `null` or redacted.

Fixtures MUST NOT:
- include coordinate-like pairs, bboxes, GeoJSON/WKT fragments, or “almost-real” geometry,
- include realistic personal names, addresses, emails, phone numbers, or other PII,
- include any secrets, credentials, tokens, or internal URLs.

### Determinism contract (what makes a provenance fixture “good”)

Provenance fixtures SHOULD:
- sort arrays and keep stable key ordering (formatter enforced in CI if needed),
- use fixed timestamps only when required to drive UI formatting,
- use synthetic IDs that never collide across scenarios.

Recommended placeholder conventions:
- `RUN_ID_REDACTED`
- `JOB_ID_REDACTED`
- `DATASET_ID_REDACTED`
- `MODEL_CARD_ID_REDACTED`
- `EXPERIMENT_ID_REDACTED`
- `HASH_REDACTED`

### Mapping philosophy (crosswalks are first-class)

The UI often needs to join:
- governance badges/tier flags,
- evidence chips,
- provenance overlays,
- lineage viewers.

For E2E determinism, keep joins explicit in `mappings/` rather than implicit in test code.

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Select scenario_id"] --> B["Load provenance_registry.json"]
  B --> C["Load governance fragment"]
  B --> D["Load mappings crosswalks"]
  B --> E["Load OpenLineage fragments"]
  B --> F["Load PROV-O fragments"]
  C --> G["Render governance surfaces"]
  D --> G
  E --> G
  F --> G
  G --> H["Assert IDs and hashes only"]
  H --> I["Write safe artifacts and telemetry"]
~~~

Interpretation:
- Governance E2E tests treat provenance fixtures as **a minimal, joinable graph of fragments** used to validate UI invariants without exposing sensitive content.

---

## 🧠 Story Node & Focus Mode Integration

Governance provenance fixtures may be consumed by:
- Story Node pages (provenance chips, evidence references, redaction banners),
- Focus Mode panels (context/timeline/map with provenance overlays),
- governance overlays (CARE tier + sovereignty flags + restriction messages).

Minimum integration invariants:
- provenance chips show **IDs/hashes** (not raw documents),
- “details” panes remain redacted in masked/restricted scenarios,
- restricted state persists across route transitions and panel switching.

---

## 🧪 Validation & CI/CD

Provenance fixtures MUST pass:
- ✅ JSON parse validation
- ✅ schema validation (when fixture schemas exist)
- ✅ secret scan
- ✅ PII scan (best-effort)
- ✅ leak-safety checks (no coordinate-like or geometry-dump patterns)

Recommended CI rules for this folder:
- block merges if any fixture contains forbidden key patterns (`coordinates`, `bbox`, `geometry`) unless explicitly `null` or redacted,
- block merges if any fixture contains high-precision number patterns that resemble coordinates,
- enforce deterministic formatting (prettier/formatter) to reduce noisy diffs.

---

## 📦 Data & Metadata

### Registry shape (recommended)

`provenance_registry.json` SHOULD map scenario IDs to fragment paths.

~~~json
{
  "schema_version": "v11.2.6",
  "scenarios": {
    "gov_public": {
      "governance": "governance/gov_public.json",
      "mappings": [
        "mappings/entity_id_map.json",
        "mappings/evidence_id_map.json",
        "mappings/run_id_map.json"
      ],
      "openlineage": [
        "openlineage/job_fragment.json",
        "openlineage/run_fragment.json"
      ],
      "prov_o": [
        "prov_o/prov_activity.json",
        "prov_o/prov_entity.json",
        "prov_o/prov_agent.json"
      ],
      "tags": ["@regression", "@governance"]
    }
  }
}
~~~

### OpenLineage fragment (minimal, safe)

~~~json
{
  "job": {
    "namespace": "kfm.tests",
    "name": "e2e.governance.regression",
    "facets": {
      "kfmGovernance": {
        "care_tier": "Tier B",
        "sovereignty_flag": true,
        "restricted_state": false
      }
    }
  },
  "run": {
    "runId": "RUN_ID_REDACTED",
    "eventTime": "2020-01-01T00:00:00Z"
  }
}
~~~

### PROV‑O fragment (minimal, safe)

~~~json
{
  "prov:activity": {
    "e2e_run": {
      "prov:label": "E2E governance regression run",
      "prov:type": "kfm:TestRun",
      "kfm:run_id": "RUN_ID_REDACTED"
    }
  },
  "prov:entity": {
    "fixture_bundle": {
      "prov:label": "Provenance fixture bundle",
      "prov:type": "kfm:TestFixture",
      "kfm:sha256": "HASH_REDACTED"
    }
  }
}
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

These fixtures are test data artifacts (not production datasets):

- **DCAT**: provenance fixtures can be treated as `dcat:Distribution` artifacts (`mediaType: application/json`).
- **STAC**: if represented as STAC Items, use:
  - `geometry: null`
  - `properties.datetime` from the run (not embedded as “live” time)
  - assets: fragment files + registry
- **PROV‑O**:
  - a fixture fragment is a `prov:Entity`,
  - an E2E run is a `prov:Activity`,
  - CI and maintainers are `prov:Agent`.

---

## 🧱 Architecture

### Recommended consumption pattern (specs + assertions)

Specs SHOULD:
1. select `scenario_id`,
2. load `provenance_registry.json`,
3. load fragments (governance + mappings + OpenLineage + PROV‑O),
4. drive UI navigation via page objects,
5. assert only high-signal, safe invariants:
   - required IDs/hashes present
   - tiers/flags correct
   - restricted state redacts as expected
   - no payload dump or precision-like content is visible

This avoids:
- duplicating provenance logic across tests,
- hardcoding IDs in assertion logic,
- snapshotting unsafe content.

---

## ⚖ FAIR+CARE & Governance

Provenance fixtures are governance-sensitive because they validate and shape:
- what the UI is allowed to display,
- what evidence is required for claims,
- how restricted/sovereign states behave.

Non-negotiable constraints:
- no sensitive precision leakage,
- no restricted inference scaffolding,
- no PII or secrets,
- conservative redaction by default.

If a fixture violates policy:
- remove it immediately,
- invalidate impacted suites until corrected,
- route review to the relevant working group and FAIR+CARE Council.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-14 | Initial governance provenance fixtures guide aligned to KFM‑MDP v11.2.6 (ID-first fragments, explicit mappings, deterministic and sovereignty-safe). |

<div align="center">

[🏛️ Governance Charter](../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>


---
title: "📦 Kansas Frontier Matrix — Provenance Fixtures: PROV‑O Bundles (E2E) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/governance/fixtures/provenance/prov_o/bundles/README.md"

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
intent: "tests-e2e-web-app-regression-governance-fixtures-provenance-prov-o-bundles"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-regression-governance-fixtures-provenance-prov-o-bundles-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:governance:fixtures:provenance:prov-o:bundles:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/governance/fixtures/provenance/prov_o/bundles/README.md"
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
  - "tests/e2e/web-app/regression/governance/fixtures/provenance/prov_o/bundles/README.md@v11.2.6"
---

<div align="center">

# 📦 **Provenance Fixtures — PROV‑O Bundles (E2E) (v11 LTS)**
`tests/e2e/web-app/regression/governance/fixtures/provenance/prov_o/bundles/README.md`

**Purpose**  
Define the **canonical PROV‑O bundle fixtures** (JSON‑LD) used by governance E2E regression suites to validate:
- provenance chip rendering and evidence surfaces,
- redaction posture (public / masked / restricted),
- **reference‑only** provenance handling (IDs + hashes, no payload dumps).

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Provenance-PROV--O-informational" />
<img src="https://img.shields.io/badge/Format-JSON--LD-blueviolet" />
<img src="https://img.shields.io/badge/Policy-Reference--Only-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ PROV‑O Fixtures](../README.md) ·
[⬅️ Provenance Fixtures](../../README.md) ·
[⬅️ Governance Fixtures](../../../README.md) ·
[🧭 E2E Guide](../../../../../../../README.md)

</div>

---

## 📘 Overview

This folder contains **PROV‑O “bundles”**: single, scenario-ready JSON‑LD files that package the minimum provenance signals a governed UI must display safely.

A bundle is designed to be:
- ✅ **scenario-ready** (a single file can drive a full governance E2E scenario),
- ✅ **deterministic** (stable IDs; stable ordering),
- ✅ **reference-only** (IDs + labels + hashes/placeholders — never full payloads),
- ✅ **sovereignty-safe** (no coordinate-like values, no geometry, no bboxes),
- ✅ **auditable** (small enough to review in diffs; intent is explicit).

**Bundles in this folder MUST NOT**
- contain real run IDs, real dataset IDs, real people/org identifiers,
- include `geometry`, `bbox`, `coordinates`, WKT fragments, or lat/long-like strings,
- embed full documents, long narratives, or raw API payload dumps,
- include secrets, credentials, tokens, or production URLs.

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
                        └── 📁 prov_o/
                            ├── 📄 README.md                           — PROV‑O fixtures overview
                            ├── 🧾 registry.json                        — Scenario/bundle registry
                            │
                            ├── 📁 bundles/
                            │   ├── 📄 README.md                         — This guide (bundle rules + shapes)
                            │   ├── 🧾 prov_public_bundle.jsonld          — Public posture (no masking required)
                            │   ├── 🧾 prov_masked_bundle.jsonld          — Masked posture (policy-safe placeholders)
                            │   └── 🧾 prov_restricted_bundle.jsonld      — Restricted posture (blocked/redacted UX)
                            │
                            ├── 📁 fragments/                             — Optional: composable building blocks
                            ├── 📁 mappings/                              — Optional: type/predicate → UI mapping
                            └── 📁 expected/                              — Expected chip sets + redaction posture
~~~

---

## 🧭 Context

### What belongs in a PROV‑O bundle

A bundle SHOULD include only what the UI needs to render provenance safely:

- minimal `prov:Activity` representing the run (synthetic),
- minimal `prov:Entity` entries representing:
  - fixture bundle,
  - “output artifact” placeholders,
  - “input dataset” placeholders (reference-only IDs),
- minimal `prov:Agent` entries:
  - CI runner (synthetic),
  - governance council (synthetic label only),
- relationships:
  - `prov:used`,
  - `prov:wasGeneratedBy`,
  - `prov:wasAssociatedWith`.

A bundle SHOULD ALSO carry a tiny, bundle-local metadata block to drive deterministic UI expectations:
- `bundle_id`
- `schema_version`
- `posture` (`public` | `masked` | `restricted`)
- `presentation` (`reference_only`)
- `allow_payload_dump` (`false`)

### Naming conventions (recommended)

Use a stable naming scheme:

- `prov_public_bundle.jsonld`
- `prov_masked_bundle.jsonld`
- `prov_restricted_bundle.jsonld`

If you add scenario-specific bundles:
- `prov_<scenario_id>_bundle.jsonld` (where `<scenario_id>` is stable and synthetic)

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Select scenario_id in governance E2E"] --> B["Resolve bundle path from registry.json"]
  B --> C["Load bundle (bundles/*.jsonld)"]
  C --> D["UI renders provenance chips and overlays"]
  D --> E["Assert: chip set + redaction posture"]
  E --> F["Assert: reference-only (no payload dumps)"]
~~~

Interpretation:
- Bundles are the single-file provenance inputs that make governance E2E scenarios deterministic and safe.

---

## 🧪 Validation & CI/CD

Bundles MUST pass:
- ✅ JSON parse validation
- ✅ JSON‑LD sanity checks (if validator exists in repo)
- ✅ secret scan
- ✅ PII scan (best-effort)
- ✅ governance leak checks (no precision leakage patterns)

Recommended bundle lint rules:
- require `@context` with only allowed prefixes (no production domains),
- forbid high-risk keys:
  - `geometry`, `bbox`, `coordinates`, `wkt`, `POINT(`, `POLYGON(`,
- forbid coordinate-like regex matches (high-precision decimals in pairs),
- enforce stable ordering (IDs and arrays sorted deterministically).

---

## 📦 Data & Metadata

### Recommended minimal bundle shape (safe JSON‑LD)

~~~json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "kfm": "urn:kfm:",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "kfm:bundle_meta": {
    "schema_version": "v11.2.6",
    "bundle_id": "prov_masked",
    "posture": "masked",
    "presentation": "reference_only",
    "allow_payload_dump": false
  },
  "prov:Activity": [
    {
      "@id": "kfm:prov:activity:test_run_001",
      "prov:label": "E2E governance run (synthetic)",
      "prov:startedAtTime": "2020-01-01T00:00:00Z"
    }
  ],
  "prov:Entity": [
    {
      "@id": "kfm:prov:entity:fixture_bundle_001",
      "prov:label": "PROV-O fixture bundle (synthetic)",
      "prov:value": "REFERENCE_ONLY"
    }
  ],
  "prov:Agent": [
    {
      "@id": "kfm:prov:agent:ci_runner",
      "prov:label": "CI runner (synthetic)"
    }
  ],
  "prov:wasAssociatedWith": [
    {
      "prov:activity": "kfm:prov:activity:test_run_001",
      "prov:agent": "kfm:prov:agent:ci_runner"
    }
  ]
}
~~~

### Masked vs restricted posture (how to represent safely)

- **Masked bundle**:
  - include “masked” markers and generalized IDs (e.g., `H3_CELL_REDACTED`),
  - do not include any value that could be interpreted as a real coordinate.

- **Restricted bundle**:
  - represent restricted references as withheld:
    - `prov:label: "RESTRICTED_REFERENCE"`
    - optional `kfm:restriction_reason: "POLICY_BLOCK"`
  - ensure UI asserts *blocked/redacted UX* without revealing content.

---

## 🌐 STAC, DCAT & PROV Alignment

Bundles are **test fixtures**, not real provenance exports:

- **DCAT**: treat bundles as test distributions (`mediaType: application/ld+json`).
- **STAC**: if indexed, use a non-spatial item:
  - `geometry: null`
  - `properties.datetime` = `last_updated`
  - assets: bundle JSON‑LD paths
- **PROV‑O**:
  - bundles are `prov:Entity`,
  - test execution consuming them is a `prov:Activity`,
  - CI is a `prov:Agent`.

---

## 🧱 Architecture

### How bundles are typically used (recommended)

E2E specs SHOULD:
1. select `scenario_id`,
2. resolve bundle via `registry.json`,
3. inject via API mock or test provenance sink,
4. assert:
   - chip presence and categories,
   - redaction posture,
   - reference-only behavior,
   - absence of precision leakage,
5. write artifacts as summaries (counts, IDs, rule IDs), not payload dumps.

Avoid:
- inline bundle JSON in test specs (hard to audit, easy to drift),
- snapshotting full JSON‑LD outputs without redaction.

---

## ⚖ FAIR+CARE & Governance

Bundles must uphold governance invariants:

- **Authority to Control**: provenance must not become an inference channel.
- **Responsibility & Ethics**: block unsafe UI exposures even during failures.
- **Collective Benefit**: transparent traceability without harm.

If a bundle violates policy:
- remove or redact immediately,
- invalidate dependent scenarios until corrected,
- route review to the relevant working group and FAIR+CARE Council.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-14 | Initial PROV‑O bundles guide aligned to KFM‑MDP v11.2.6 (JSON‑LD, reference-only posture, deterministic governance E2E support). |

<div align="center">

[🏛️ Governance Charter](../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>


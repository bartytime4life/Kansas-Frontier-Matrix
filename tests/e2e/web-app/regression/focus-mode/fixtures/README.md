---
title: "🧩 Kansas Frontier Matrix — Focus Mode v3 Regression Fixtures (E2E) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/focus-mode/fixtures/README.md"

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
intent: "tests-e2e-web-app-regression-focus-mode-fixtures"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-regression-focus-mode-fixtures-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:focus-mode:fixtures:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/focus-mode/fixtures/README.md"
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

signature_ref: "../../../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../../../releases/v11.2.6/tests-e2e-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/tests-e2e-v11.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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
  - "tests/e2e/web-app/regression/focus-mode/fixtures/README.md@v11.2.6"
---

<div align="center">

# 🧩 **Focus Mode v3 Regression Fixtures (E2E) (v11 LTS)**
`tests/e2e/web-app/regression/focus-mode/fixtures/README.md`

**Purpose**  
Define the **canonical synthetic fixture set** used by **Focus Mode v3 regression E2E** tests.  
Fixtures in this folder simulate **known UI + governance states** without using real individuals, real sites, or restricted data.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/E2E-Fixtures-informational" />
<img src="https://img.shields.io/badge/Surface-Focus%20Mode%20v3-blueviolet" />
<img src="https://img.shields.io/badge/Governance-FAIR%2BCARE-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Focus Mode Regression](../README.md) · [🧾 Spec Rules](../specs/README.md) · [🧭 E2E Guide](../../../../README.md)

</div>

---

## 📘 Overview

This folder contains **synthetic, deterministic fixtures** used to drive Focus Mode v3 regression scenarios.

Fixtures here exist to:
- 🧠 Provide stable **Context · Timeline · Map** inputs for regression specs.
- 🛡️ Simulate governance conditions (CARE tiers, sovereignty flags, restricted states) safely.
- 🧾 Provide stable **provenance/evidence surfaces** (IDs, hashes, references) without dumping full payloads.
- 🧪 Enable regression tests to assert **masking invariants** and “no-leak” requirements.

Fixtures here MUST be:
- **Synthetic** (non-identifying; non-realistic for restricted knowledge).
- **Deterministic** (stable IDs; stable ordering; stable timestamps where possible).
- **Sovereignty-safe** (no raw sensitive-like geometry; no plausible site coordinates).

Fixtures here MUST NOT:
- include real people, real addresses, real place coordinates, or restricted cultural information,
- include production tokens, credentials, or secrets,
- rely on live network access as a required dependency.

---

## 🗂️ Directory Layout

This folder is organized for **scenario discovery**, **runner-friendly loading**, and **clear governance intent**.

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 regression/
            └── 📁 focus-mode/
                └── 📁 fixtures/
                    ├── 📄 README.md                         — This guide (fixture rules + governance)
                    │
                    ├── 🧾 scenario_registry.json             — Scenario ID → fixture bundle mapping
                    │
                    ├── 📁 scenarios/                         — Scenario bundles (synthetic, deterministic)
                    │   ├── 🧾 focus_safe.json                 — Fully public, non-sensitive scenario
                    │   ├── 🧾 focus_masked.json               — Masked/generalized scenario (H3-safe)
                    │   └── 🧾 focus_restricted.json           — Restricted state (blocked/redacted UX)
                    │
                    ├── 📁 api_mocks/                         — Optional API response stubs (if runner uses interception)
                    │   ├── 🧾 focus_mode_entity.json
                    │   ├── 🧾 focus_mode_panels.json
                    │   └── 🧾 focus_mode_provenance.json
                    │
                    ├── 📁 expected_ui/                       — Expected “high-signal” UI assertions (counts, IDs, flags)
                    │   ├── 🧾 focus_safe_expected.json
                    │   ├── 🧾 focus_masked_expected.json
                    │   └── 🧾 focus_restricted_expected.json
                    │
                    └── 📁 provenance/                        — Provenance fragments (IDs/hashes only; no full dumps)
                        ├── 🧾 focus_safe_prov.json
                        ├── 🧾 focus_masked_prov.json
                        └── 🧾 focus_restricted_prov.json
~~~

Notes:
- Filenames above are the **canonical target layout** for this folder.
- If your repo chooses a different extension (`.yaml`) or schema naming, keep the structure and intent consistent.

---

## 🧭 Context

### Fixture design principles (high-signal over high-volume)
Fixtures SHOULD:
- be small enough to debug from a diff,
- contain just enough data to render panels and trigger governance logic,
- avoid long narrative bodies (prefer short synthetic strings + reference IDs),
- preserve deterministic ordering (arrays sorted; stable keys).

Fixtures SHOULD NOT:
- mirror real historical events in detail,
- embed plausible restricted knowledge even as “fake data,”
- include full external documents (use short synthetic excerpts only).

### IDs and timestamps (determinism contract)
Use stable deterministic identifiers:
- `scenario_id`: stable string key (e.g., `focus_safe`)
- `entity_id`: stable synthetic ID (UUID allowed if pinned)
- `run_seed`: a numeric seed (if a generator is used)

Timestamps:
- Use fixed timestamps where possible (e.g., `2020-01-01T00:00:00Z`)
- If “now” is required, it MUST be injected by a deterministic clock provider in the runner, not generated by the fixture.

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Load scenario_registry.json"] --> B["Select scenario_id"]
  B --> C["Load scenario bundle (scenarios/*.json)"]
  C --> D["Optional API mocks (api_mocks/*.json)"]
  D --> E["Render Focus Mode panels"]
  E --> F["Assert expected_ui (counts, flags, IDs)"]
  F --> G["Assert provenance fragments (IDs and hashes)"]
  G --> H["Write artifacts and telemetry"]
~~~

Interpretation:
- Fixtures are the stable, non-sensitive input layer enabling deterministic E2E regression assertions for Focus Mode v3.

---

## 🧠 Story Node & Focus Mode Integration

Fixtures MAY represent:
- an entity opened directly in Focus Mode,
- an entity reached from a Story Node route transition.

When fixtures simulate Story Node linkage:
- use synthetic Story Node IDs,
- keep relationships shallow and deterministic,
- ensure governance flags are preserved across navigation.

Minimum integration invariants:
- entity identity remains stable across panel interactions,
- provenance surfaces remain non-empty (IDs/hashes),
- restricted state remains restricted across route transitions.

---

## 🧪 Validation & CI/CD

Fixtures are CI-scanned and CI-validated.

Fixtures MUST pass:
- ✅ JSON/YAML parse validation
- ✅ schema validation (when a fixture schema exists)
- ✅ secret scan
- ✅ PII scan (best-effort)
- ✅ sovereignty safety checks (no coordinate leakage patterns)

Recommended checks (fixture lint rules):
- enforce stable key ordering in JSON (or apply a formatter in CI),
- forbid lat/long-like fields unless explicitly null or generalized,
- forbid raw geometry payloads unless geometry is clearly synthetic and policy-safe.

---

## 📦 Data & Metadata

### Scenario registry (canonical shape)
The registry maps scenario IDs to fixture bundles.

Example (simplified):
~~~json
{
  "schema_version": "v11.2.6",
  "scenarios": {
    "focus_safe": {
      "bundle": "scenarios/focus_safe.json",
      "expected": "expected_ui/focus_safe_expected.json",
      "provenance": "provenance/focus_safe_prov.json",
      "tags": ["@regression"]
    },
    "focus_masked": {
      "bundle": "scenarios/focus_masked.json",
      "expected": "expected_ui/focus_masked_expected.json",
      "provenance": "provenance/focus_masked_prov.json",
      "tags": ["@regression", "@governance"]
    },
    "focus_restricted": {
      "bundle": "scenarios/focus_restricted.json",
      "expected": "expected_ui/focus_restricted_expected.json",
      "provenance": "provenance/focus_restricted_prov.json",
      "tags": ["@regression", "@governance"]
    }
  }
}
~~~

### “Expected UI” files (what belongs there)
Expected UI files MUST contain only **high-signal assertions**, such as:
- required panel presence flags,
- expected counts (evidence chips, timeline entries),
- required governance badges (CARE tier, sovereignty icon),
- restricted-state UI expectations (masked/redacted/blocked).

Example (simplified):
~~~json
{
  "scenario_id": "focus_masked",
  "expect": {
    "panels_ready": ["context", "timeline", "map"],
    "care_tier": "Tier B",
    "sovereignty_flag_visible": true,
    "raw_coordinates_visible": false,
    "evidence_chip_min_count": 1
  }
}
~~~

### Provenance fragments (IDs/hashes only)
Provenance fixture fragments SHOULD include only:
- `dataset_ids`, `experiment_ids`, `model_card_ids` (when relevant),
- `hashes` (sha256 placeholders allowed),
- stable reference anchors.

Do NOT include full documents or full dataset dumps.

---

## 🌐 STAC, DCAT & PROV Alignment

### PROV-O alignment (fixture interpretation)
- A scenario bundle is a `prov:Entity`.
- A test run is a `prov:Activity`.
- CI runner + maintainers are `prov:Agent`.

Fixture provenance content MUST remain:
- synthetic,
- non-identifying,
- safe to publish.

### STAC/DCAT alignment (optional for fixture catalogs)
If fixtures are indexed:
- treat the fixture bundle as documentation/test data (not a real dataset),
- set `geometry: null` for STAC-like representations,
- ensure any “coverage” fields are synthetic and non-sensitive.

---

## 🧱 Architecture

### How fixtures are used by specs (recommended pattern)
Specs SHOULD:
- select `scenario_id`,
- load the registry,
- load bundle + expected + provenance fragments,
- drive UI interactions using page objects,
- call shared assertions that consume `expected_ui`.

This avoids:
- hardcoding payloads in test logic,
- duplicating scenario selection logic,
- fragile assertions scattered across specs.

---

## ⚖ FAIR+CARE & Governance

### Sovereignty and masking rules (non-negotiable)
Fixtures MUST:
- never encode raw sensitive-like coordinates,
- simulate masked states without revealing precision,
- ensure restricted-state fixtures produce safe UI behaviors:
  - redacted, masked, or blocked.

### Ethical fixture language rules
Synthetic text MUST:
- avoid colonial framing and culturally harmful phrasing,
- avoid implying genealogy or sacred knowledge,
- remain minimal and purely functional for testing.

### Escalation
If a fixture is found to violate policy:
- remove it immediately,
- invalidate related specs until corrected,
- route review to the relevant working group and FAIR+CARE Council.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Initial Focus Mode v3 regression fixtures guide aligned to KFM-MDP v11.2.6 (deterministic, sovereignty-safe, governance-aware). |

<div align="center">

[🏛️ Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>


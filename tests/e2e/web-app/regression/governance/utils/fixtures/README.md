---
title: "🧺 Kansas Frontier Matrix — Governance E2E Utility Fixtures (Web App Regression) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/governance/utils/fixtures/README.md"

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
intent: "tests-e2e-web-app-regression-governance-utils-fixtures"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-regression-governance-utils-fixtures-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:governance:utils:fixtures:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/governance/utils/fixtures/README.md"
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
  - "tests/e2e/web-app/regression/governance/utils/fixtures/README.md@v11.2.6"
---

<div align="center">

# 🧺 **Governance E2E Utility Fixtures (Web App Regression) (v11 LTS)**
`tests/e2e/web-app/regression/governance/utils/fixtures/README.md`

**Purpose**  
Define the **synthetic fixture assets** consumed by governance E2E utilities (navigation/waits/parsers/leak checks).  
Fixtures here are **not app datasets** — they are **small, deterministic inputs** used to validate governance behavior and safety invariants.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Scope-Governance%20Utilities-orange" />
<img src="https://img.shields.io/badge/Data-Synthetic%20Only-brightgreen" />
<img src="https://img.shields.io/badge/Policy-No%20Precision%20Leak-red" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Utilities](../README.md) ·
[⬅️ Governance Regression](../../README.md) ·
[🧭 E2E Guide](../../../../../README.md)

</div>

---

## 📘 Overview

These fixtures exist to keep governance utility behavior:

- ✅ **deterministic** (stable IDs, stable ordering, stable timestamps),
- 🛡️ **sovereignty-safe** (no raw sensitive-like coordinates; no plausible site geometry),
- 🧪 **testable** (small inputs that trigger high-signal behaviors),
- 🧾 **auditable** (fixtures can be reviewed as diffs; no opaque generators required).

Fixtures in this folder typically support utility tests such as:

- **precision leakage detection** (coordinate-like text, GeoJSON-like fragments, high-precision bboxes),
- **governance badge parsing** (CARE tier, sovereignty flag visibility),
- **redaction/masking assertions** (expected safe UI strings),
- **allowlist/denylist behaviors** for known safe placeholders.

Fixtures here MUST be:

- synthetic, non-identifying, and publishable,
- minimal (only what utilities need),
- compatible with CI scans (secret/PII best-effort, governance safety checks).

Fixtures here MUST NOT:

- include real people, real addresses, or real-world site coordinates,
- include plausible restricted knowledge (even “fake”),
- embed credentials, tokens, or secrets,
- rely on network fetch as a required dependency.

---

## 🗂️ Directory Layout

This directory is intentionally small and reviewable.

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 regression/
            └── 📁 governance/
                └── 📁 utils/
                    └── 📁 fixtures/
                        ├── 📄 README.md                         — This guide (rules + shapes)
                        │
                        ├── 🧾 fixture_registry.json             — Fixture IDs → file paths + tags
                        ├── 🧾 governance_states.json             — Synthetic CARE/sovereignty state combinations
                        │
                        ├── 🧾 leak_patterns.json                 — Regex/pattern catalog for leak detection utilities
                        ├── 🧾 leak_allowlist.json                — Explicit allowlist of safe placeholders/tokens
                        ├── 🧾 redaction_expectations.json        — Expected “safe UI” render fragments
                        │
                        └── 🧾 sample_ui_strings.json             — Synthetic UI strings to test parsers (no payload dumps)
~~~

Notes:
- Filenames above represent the **canonical target layout** for governance utility fixtures.
- If the repo uses `.yaml` instead of `.json`, keep the same intent and structure.
- Keep fixtures small enough to review in a PR diff.

---

## 🧭 Context

### Determinism contract
Fixtures SHOULD:
- use stable `fixture_id` keys,
- use stable timestamps when required (e.g., `"2020-01-01T00:00:00Z"`),
- avoid runtime generation (unless seeded and recorded by the runner).

If a “current time” concept is required:
- the utility MUST accept a deterministic clock provider,
- fixtures MUST NOT call `Date.now()` equivalents.

### Safety contract (no precision leakage)
Fixtures MUST:
- never contain raw coordinate pairs that look real,
- never include high-precision lat/long-like floats,
- never include GeoJSON geometry dumps that could be mistaken for a real location.

Allowed patterns:
- explicit placeholders (e.g., `"LAT_REDACTED"`, `"H3_R8_CELL_ID"`)
- null/empty geometry fields for non-spatial fixtures

Disallowed patterns:
- realistic coordinates (even if “random”),
- realistic bboxes (min/max lon/lat),
- any polygon/line geometry with plausible real extents.

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Utility test selects fixture_id"] --> B["Load fixture_registry.json"]
  B --> C["Read fixture file (json/yaml)"]
  C --> D["Run utility function"]
  D --> E["Assert expected behavior"]
  E --> F["Write artifacts + telemetry summary"]
~~~

Interpretation:
- Fixtures are the stable input layer for governance utility behavior (parsing, leak detection, redaction expectations).

---

## 🧪 Validation & CI/CD

Fixtures MUST pass:
- ✅ parse validation (JSON/YAML),
- ✅ secret scan,
- ✅ PII scan (best-effort),
- ✅ governance safety checks (no coordinate-like leakage patterns),
- ✅ formatting normalization (if enforced by repo tooling).

Recommended fixture lint rules:
- forbid numeric patterns matching `[-]?\d{1,3}\.\d{4,}` unless explicitly allowlisted,
- forbid keys like `"coordinates"`, `"geometry"`, `"bbox"` unless values are null/placeholders,
- require stable sorting of arrays (when semantics allow).

Governance-related fixture violations are treated as **stop-ship** for this surface:
- remove/patch immediately,
- quarantine dependent tests until corrected.

---

## 📦 Data & Metadata

### `fixture_registry.json` (canonical shape)
The registry maps IDs to files and test tags.

~~~json
{
  "schema_version": "v11.2.6",
  "fixtures": {
    "leak_patterns_default": {
      "path": "leak_patterns.json",
      "tags": ["@governance", "@regression"],
      "description": "Default coordinate/geometry leak detection patterns."
    },
    "leak_allowlist_default": {
      "path": "leak_allowlist.json",
      "tags": ["@governance"],
      "description": "Explicit allowlist of safe placeholders and tokens."
    },
    "redaction_expectations_default": {
      "path": "redaction_expectations.json",
      "tags": ["@governance"],
      "description": "Expected safe UI fragments for masked/redacted states."
    }
  }
}
~~~

### `governance_states.json` (recommended minimal structure)
This file provides deterministic combinations without encoding real-world meaning.

~~~json
{
  "states": [
    {
      "state_id": "public_low_risk",
      "care_label": "Public · Low-Risk",
      "sovereignty_flag_visible": false,
      "expected_mode": "unrestricted"
    },
    {
      "state_id": "masked_required",
      "care_label": "Tier B",
      "sovereignty_flag_visible": true,
      "expected_mode": "masked"
    },
    {
      "state_id": "restricted_block",
      "care_label": "Tier A",
      "sovereignty_flag_visible": true,
      "expected_mode": "restricted"
    }
  ]
}
~~~

### `leak_patterns.json` (recommended approach)
Prefer explicit patterns with human-readable intent.

~~~json
{
  "patterns": [
    {
      "id": "lat_long_pair_high_precision",
      "type": "regex",
      "value": "(-?\\d{1,3}\\.\\d{4,})\\s*,\\s*(-?\\d{1,3}\\.\\d{4,})",
      "severity": "block",
      "description": "Detects coordinate-like pairs with high precision."
    },
    {
      "id": "geojson_coordinates_key",
      "type": "substring",
      "value": "\"coordinates\"",
      "severity": "block",
      "description": "Blocks GeoJSON-like coordinate dumps in UI/debug text."
    }
  ]
}
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

Fixtures in this folder are test utilities assets (not real datasets):

- Treat as documentation/test entities if cataloged.
- Prefer non-spatial representations:
  - `geometry: null` in STAC-like mappings
  - `mediaType: application/json` in DCAT distributions

PROV-O interpretation:
- fixture files are `prov:Entity`,
- a utility test run is a `prov:Activity`,
- CI is a `prov:Agent`.

---

## 🧱 Architecture

### How utilities should consume fixtures (recommended)
Utilities SHOULD:
- load registry → resolve file → parse → validate shape,
- avoid scattering file paths across specs,
- treat missing/invalid fixture as a hard error with a clear message,
- avoid printing full fixture content to logs (return small structured summaries).

### When to add a new fixture
Add a fixture when:
- a new leak pattern must be enforced,
- a new redaction invariant is introduced,
- governance parsing logic needs stable input coverage.

Do NOT add fixtures for:
- app-wide scenario payloads (belongs under scenario fixtures),
- large UI snapshots (belongs under artifacts/snapshots).

---

## ⚖ FAIR+CARE & Governance

Fixtures MUST:
- remain synthetic and non-identifying,
- avoid culturally harmful phrasing (even as “test text”),
- avoid plausible replication of restricted knowledge,
- enforce sovereignty policy outcomes (masked/redacted/blocked) without exposing precision.

If a fixture accidentally introduces a leak vector:
- delete/patch immediately,
- rotate/refresh dependent expected outputs as needed,
- route review to the appropriate working group and FAIR+CARE Council.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Initial governance utility fixtures guide aligned to KFM‑MDP v11.2.6 (determinism, leak detection, redaction expectations, safe placeholders). |

<div align="center">

[🏛️ Governance Charter](../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>


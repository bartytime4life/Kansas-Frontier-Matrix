---
title: "🧩 Kansas Frontier Matrix — Governance Regression Scenarios (E2E Fixtures) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/governance/fixtures/scenarios/README.md"

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
intent: "tests-e2e-web-app-regression-governance-fixtures-scenarios"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-regression-governance-fixtures-scenarios-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:governance:fixtures:scenarios:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/governance/fixtures/scenarios/README.md"
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
  - "tests/e2e/web-app/regression/governance/fixtures/scenarios/README.md@v11.2.6"
---

<div align="center">

# 🧩 **Governance Regression Scenarios (E2E Fixtures) (v11 LTS)**
`tests/e2e/web-app/regression/governance/fixtures/scenarios/README.md`

**Purpose**  
Define the **canonical synthetic scenario bundles** used by **governance regression E2E** tests to validate:
- FAIR+CARE routing and UI signals,
- sovereignty masking behaviors,
- restricted-state blocking/redaction,
- precision leak prevention (UI/console/network-visible surfaces).

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Surface-Web%20App%20E2E-blueviolet" />
<img src="https://img.shields.io/badge/Governance-FAIR%2BCARE-orange" />
<img src="https://img.shields.io/badge/Policy-Merge%20Blocking-red" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Governance Fixtures](../README.md) ·
[⬅️ Governance Regression](../../README.md) ·
[🧭 E2E Guide](../../../../../README.md)

</div>

---

## 📘 Overview

This folder contains **scenario bundles** for governance E2E regression tests.

A **scenario** is a minimal, deterministic “world state” for a test run that defines:

- what route(s) or UI surface(s) the test opens,
- what synthetic data the UI receives (direct fixture loads or API interception),
- what governance state is being simulated (CARE tier, sovereignty flags, restricted state),
- what the test must assert (badges, redactions, safe fallbacks, and no-leak invariants).

Scenarios in this folder MUST be:

- ✅ **Synthetic** (non-identifying; no real individuals, no real sites)
- ✅ **Deterministic** (stable IDs; stable ordering; stable timestamps where possible)
- ✅ **Sovereignty-safe** (no raw geometry dumps; no plausible sensitive coordinates)
- ✅ **High-signal** (small enough to debug via diffs; focused assertions)

Scenarios in this folder MUST NOT:

- include real coordinate pairs, real addresses, or restricted cultural knowledge,
- include production tokens, secrets, or credentials,
- depend on external network availability as a required dependency.

---

## 🗂️ Directory Layout

This folder stores **scenario bundles** only. Supporting artifacts live in sibling folders (`api_mocks/`, `expected/`, `allowlists/`, `provenance/`).

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 regression/
            └── 📁 governance/
                └── 📁 fixtures/
                    ├── 📁 scenarios/                                  — This folder (scenario bundles)
                    │   ├── 📄 README.md                               — This guide
                    │   │
                    │   ├── 📁 gov_synth_001/                          — Scenario bundle: public-safe baseline
                    │   │   ├── 🧾 scenario.json                        — Scenario definition (routes, tags, fixture refs)
                    │   │   ├── 🧾 notes.json                           — Optional: short rationale (synthetic)
                    │   │   └── 🧾 inputs.json                          — Optional: local inputs (non-sensitive)
                    │   │
                    │   ├── 📁 gov_synth_002/                          — Scenario bundle: masking required (no precision)
                    │   │   ├── 🧾 scenario.json
                    │   │   └── 🧾 inputs.json
                    │   │
                    │   └── 📁 gov_synth_003/                          — Scenario bundle: restricted state (blocked/redacted)
                    │       ├── 🧾 scenario.json
                    │       └── 🧾 inputs.json
                    │
                    ├── 📁 api_mocks/                                  — API response stubs (if runner intercepts)
                    ├── 📁 expected/                                   — High-signal expected results (counts/flags/ids)
                    ├── 📁 allowlists/                                 — Safe placeholders only (no realistic examples)
                    └── 📁 provenance/                                 — IDs/hashes only (no payload dumps)
~~~

Notes:
- Folder names above are the **canonical target layout**.
- Scenario IDs (`gov_synth_###`) are illustrative; choose any naming scheme that remains deterministic and consistent.

---

## 🧭 Context

### Scenario design principles

Scenarios SHOULD:
- test one governance claim at a time (high-signal failures),
- keep payloads minimal and structured (prefer references over bodies),
- encode governance intent explicitly (tier, flags, restricted status),
- avoid brittle UI text assertions (prefer IDs, badges, counts, and invariants).

Scenarios SHOULD NOT:
- mirror real-world cases with realistic detail,
- contain long narratives,
- embed coordinates or full geometry objects,
- require multiple minutes to execute.

### Scenario naming and stability

Recommended pattern:
- `gov_synth_001`, `gov_synth_002`, `gov_synth_003` … (monotonic, stable)
- or `gov_masking_required`, `gov_restricted_blocked`, etc. (semantic, stable)

Every scenario MUST declare:
- `scenario_id` (string)
- `schema_version` (must match `v11.2.6` for governed E2E docs)
- `tags` (e.g., `@regression`, `@governance`)
- `entry_route` (or `routes`)
- fixture references (paths to sibling fixture folders)

### Safe geometry and “no-leak” rules

If a scenario needs spatial behavior:
- use `geometry: null`, or
- use synthetic placeholders that cannot be confused with real coordinates, or
- encode H3-like placeholders (e.g., `H3_R8_CELL_ID`) without numeric lat/long values.

Never encode:
- `[-97.1234, 38.5678]`-style pairs,
- GeoJSON `coordinates` arrays,
- WKT fragments (e.g., `POINT(`),
- high-precision `bbox` fields.

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Select scenario_id"] --> B["Load scenario bundle"]
  B --> C["Resolve fixture references"]
  C --> D["Boot app in deterministic test mode"]
  D --> E["Run governance assertions"]
  E --> F["Run leak checks"]
  F --> G["Write artifacts and telemetry"]
~~~

Interpretation:
- A scenario bundle is the deterministic input contract for governance regression, enabling consistent assertions and safe reporting.

---

## 🧠 Story Node & Focus Mode Integration

Governance regression scenarios may traverse:
- general UI routes (home/search/detail),
- Story Node pages (provenance chips, redactions),
- Focus Mode panels (context/timeline/map), when governance overlays are present.

If a scenario touches narrative surfaces, it MUST assert:
- governance badges are visible (CARE tier, sovereignty flags),
- restricted content remains withheld/redacted,
- provenance surfaces show IDs/hashes (not payload dumps),
- precision does not appear in any UI-visible text or debug panes.

---

## 🧪 Validation & CI/CD

Scenarios are CI-scanned and may be merge-blocking.

Scenarios MUST pass:
- ✅ JSON parse validation
- ✅ schema validation (if a scenario schema exists)
- ✅ secret scan
- ✅ PII scan (best-effort)
- ✅ governance lint (no coordinate-like patterns, no geometry dumps)

Recommended CI behavior:
- `@governance` scenarios run on PRs affecting governed surfaces
- all scenarios run on nightly schedules for broader coverage
- governance failures are not retryable by default

---

## 📦 Data & Metadata

### Scenario file: recommended minimal shape

Each scenario bundle should include a `scenario.json` with stable fields.

~~~json
{
  "schema_version": "v11.2.6",
  "scenario_id": "gov_synth_002",
  "title": "Masking required (synthetic)",
  "tags": ["@regression", "@governance"],
  "entry_route": "/focus-mode/synth/entity-002",
  "governance_state": {
    "care_tier": "Tier B",
    "sovereignty_flag": true,
    "restricted": false,
    "masking_required": true
  },
  "fixtures": {
    "api_mocks": "../api_mocks/endpoints/gov_synth_002.json",
    "expected": "../expected/cases/gov_synth_002_expected.json",
    "allowlists": "../allowlists/leak_allowlist.json",
    "provenance": "../provenance/prov_o/bundles/gov_synth_002_prov.json"
  }
}
~~~

### What belongs in `inputs.json` (and what does not)

Allowed:
- synthetic identifiers,
- minimal panel-ready strings,
- stable timestamps (fixed),
- flags and counts,
- short synthetic labels.

Not allowed:
- full documents,
- realistic coordinates,
- long narrative bodies,
- any text that implies genealogy or sensitive cultural inference.

---

## 🌐 STAC, DCAT & PROV Alignment

These scenario bundles are test fixtures (not production datasets):

- **DCAT**: scenario bundles may be treated as `dcat:Distribution` artifacts (`mediaType: application/json`) if cataloged for audits.
- **STAC**: if represented as non-spatial items, use:
  - `geometry: null`
  - `properties.datetime` as fixture update time
  - assets: `scenario.json` (and optional `inputs.json`)
- **PROV-O**:
  - a scenario bundle is a `prov:Entity`,
  - the E2E run is a `prov:Activity`,
  - CI runners and maintainers are `prov:Agent`.

---

## 🧱 Architecture

### How scenarios are consumed by governance specs (recommended)

1. A spec selects `scenario_id` (from a registry or folder discovery)
2. Load `scenario.json`
3. Resolve fixture references to sibling folders
4. Boot app in deterministic test mode
5. Apply assertions:
   - governance overlays
   - restricted-state behavior
   - “no-leak” invariants
6. Emit artifacts + telemetry

This architecture keeps:
- scenario intent in fixtures,
- logic in reusable assertions/utils,
- reports safe and minimal.

---

## ⚖ FAIR+CARE & Governance

Scenarios are governance-critical because they validate **user-visible policy outcomes**.

Scenarios MUST ensure:
- **Authority to Control**: masking and restricted behavior is enforced and testable.
- **Responsibility & Ethics**: no leakage, no harmful framing, safe fixtures only.
- **Collective Benefit**: consistent enforcement improves trust and reduces risk.

If a scenario is found to violate policy:
- remove or quarantine immediately,
- invalidate dependent specs until corrected,
- route review to the relevant working group and FAIR+CARE Council.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-14 | Initial governance regression scenarios guide aligned to KFM‑MDP v11.2.6 (synthetic scenario bundles, deterministic selection, no-leak safety rules). |

<div align="center">

[🏛️ Governance Charter](../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>


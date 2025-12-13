---
title: "🧩 Kansas Frontier Matrix — Parsing Utilities (Governance Regression E2E) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/governance/utils/parsing/README.md"

version: "v11.2.6"
last_updated: "2025-12-13"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous Systems Oversight · FAIR+CARE Council"
content_stability: "stable"

status: "Active · Enforced"
doc_kind: "Testing Utility Guide"
header_profile: "standard"
footer_profile: "standard"
intent: "tests-e2e-web-app-regression-governance-utils-parsing"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-regression-governance-utils-parsing-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:governance:utils:parsing:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/governance/utils/parsing/README.md"
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
  - "tests/e2e/web-app/regression/governance/utils/parsing/README.md@v11.2.6"
---

<div align="center">

# 🧩 **Parsing Utilities (Governance Regression E2E) (v11 LTS)**
`tests/e2e/web-app/regression/governance/utils/parsing/README.md`

**Purpose**  
Define the **canonical parsing utility layer** used by governance regression E2E suites to transform E2E-visible signals into **safe, deterministic, auditable structures**, including:

- DOM text and UI-state extraction
- console and error normalization
- network-response summarization (without dumping payloads)
- redaction and precision-safe snippet generation
- stable output shapes for assertions, leak checks, and reports

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Surface-Web%20App%20E2E-blueviolet" />
<img src="https://img.shields.io/badge/Focus-Safe%20Parsing-blueviolet" />
<img src="https://img.shields.io/badge/Governance-FAIR%2BCARE-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Governance Utilities](../README.md) ·
[⬅️ Governance Regression](../../README.md) ·
[🧭 E2E Guide](../../../../../README.md)

</div>

---

## 📘 Overview

Parsing utilities are the **bridge** between “what the test runner can observe” and “what governance suites can safely assert.”

### What parsing utilities do

Parsing utilities SHOULD:

- normalize E2E signals into stable, deterministic shapes (arrays sorted, keys stable),
- extract only the minimum required information to support assertions,
- redact or summarize any high-risk content (precision, raw geometry, verbose debug payloads),
- generate stable anchors for auditing:
  - rule IDs
  - selector names / test IDs
  - URL paths
  - safe hashes (placeholders allowed in fixtures)

### Non-goals

Parsing utilities are not:

- a substitute for application-level policy enforcement,
- a content “reconstruction” engine,
- an OCR pipeline for screenshots (screenshots are artifacts, not a primary parse source),
- a place to store full payloads or raw sensitive-like geometry.

### Core constraints (must-haves)

- **Deterministic**: identical inputs produce identical parse outputs.
- **Safe by construction**: the default output must be safe to store in artifacts.
- **High signal**: parsing should support clear failure diagnosis without leaking content.

---

## 🗂️ Directory Layout

This folder typically contains pure parsing helpers, redaction tools, and output schemas.

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 regression/
            └── 📁 governance/
                └── 📁 utils/
                    ├── 📁 parsing/
                    │   ├── 📄 README.md                         — This guide
                    │   ├── 📄 parse_dom.ts                       — DOM text extraction and normalization
                    │   ├── 📄 parse_ui_state.ts                  — State flags (ready, restricted, masked, etc.)
                    │   ├── 📄 parse_console.ts                   — Console/error capture normalization
                    │   ├── 📄 parse_network.ts                   — Network response summarization (no raw dumps)
                    │   ├── 📄 redact.ts                          — Precision-safe snippet redaction helpers
                    │   ├── 📄 normalize.ts                       — Sorting, canonicalization, stable serialization
                    │   ├── 📄 schemas.ts                         — Parse output shape constants (test-local)
                    │   └── 📄 hashing.ts                         — Optional stable hashing for evidence anchors
                    │
                    ├── 📁 leak_checks/                           — Rule matching and leak enforcement utilities
                    └── 📁 navigation/                             — Route builders and deterministic readiness guards
~~~

Notes:
- Filenames shown are the **canonical target layout**. The repository may use different names or languages.
- Parsing utilities should remain small, test-local, and dependency-light.

---

## 🧭 Context

### Safe parsing rules (non-negotiable)

Parsing utilities MUST NOT:

- write raw network payloads into CI logs or artifacts,
- emit raw coordinate-like pairs or geometry fragments in reports,
- serialize full “debug views” or API responses verbatim.

Parsing utilities MUST:

- redact first, then report,
- prefer safe summaries:
  - counts
  - IDs
  - stable flags
  - rule identifiers
  - redacted snippets
- preserve enough context for debugging:
  - page name
  - selector/test-id
  - route path (not tokenized query dumps)

### Deterministic ordering contract

When parsing produces arrays or maps, utilities SHOULD:

- sort by stable keys (e.g., `id`, `rule_id`, `selector`),
- normalize whitespace and Unicode consistently,
- strip volatile fragments (timestamps, stack addresses) unless explicitly required and stabilized.

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Collect E2E-visible signals"] --> B["Normalize and canonicalize"]
  B --> C["Redact risky fragments"]
  C --> D["Produce parse outputs"]
  D --> E["Assertions and leak checks consume outputs"]
  E --> F["Write safe artifacts and telemetry"]
~~~

Interpretation:
- Parsing is a safety boundary: it transforms raw observations into a controlled, auditable format that governance suites can store and reason over.

---

## 🧠 Story Node & Focus Mode Integration

Governance E2E regression commonly validates narrative surfaces (Story Nodes and Focus Mode), which creates special parsing risks:

- narrative text can be long (avoid copying),
- provenance panels may include references (prefer IDs/hashes),
- map/timeline surfaces can reveal precision (never parse and re-emit raw geometry).

### Recommended narrative parsing outputs

For Story Node / Focus Mode surfaces, parsing utilities SHOULD yield:

- panel readiness flags (`context_ready`, `timeline_ready`, `map_ready`)
- governance badges:
  - `care_tier`
  - `sovereignty_flag_visible`
  - `restricted_state`
- evidence summary:
  - `evidence_chip_count`
  - `reference_ids` (synthetic or hashed anchors)

---

## 🧪 Validation & CI/CD

Parsing utilities are expected to be:

- unit tested (pure inputs → deterministic outputs),
- used in governance regression suites (integration coverage),
- linted to prevent unsafe output patterns.

Recommended checks:

- deterministic snapshot tests of parse outputs (redacted, stable),
- “no raw payload” enforcement:
  - forbid writing JSON blobs above a size threshold
  - forbid keys like `coordinates`, `geometry`, `bbox` unless explicitly null/synthetic and redacted
- strict secret/PII scans over artifacts.

---

## 📦 Data & Metadata

### Parse output model (recommended minimum)

Parsing utilities SHOULD produce a small structured object usable by assertions:

~~~json
{
  "schema_version": "v11.2.6",
  "run_id": "e2e_2025-12-13_001",
  "scenario_id": "governance_masked_required",
  "page": "FocusMode",
  "route_path": "/focus-mode/entity/<synthetic-id>",
  "signals": {
    "ui_text_tokens": ["CARE:Tier B", "SOVEREIGNTY:visible"],
    "flags": {
      "restricted_state": false,
      "sovereignty_flag_visible": true,
      "raw_coordinates_visible": false
    },
    "counts": {
      "evidence_chip_count": 2
    }
  },
  "evidence": [
    {
      "source": "ui_text",
      "location": { "selector": "data-testid=governance-badge" },
      "snippet_redacted": "CARE: Tier B …",
      "hash": "<sha256>"
    }
  ]
}
~~~

### Redaction rules (recommended)

Redaction helpers SHOULD support:

- coordinate-like redaction (`LAT_REDACTED`, `LON_REDACTED`)
- geometry-key redaction (`"coordinates" …`, `"geometry" …`)
- long-string truncation (bounded length)
- whitespace normalization for stable snapshots

---

## 🌐 STAC, DCAT & PROV Alignment

Parsing outputs are test artifacts:

- **DCAT**: parse reports can be treated as `dcat:Distribution` (`mediaType: application/json`).
- **STAC**: if represented, use:
  - `geometry: null`
  - `properties.datetime` as run time
  - assets: `parse-output.json`
- **PROV-O**:
  - parsing is a sub-activity within the E2E run (`prov:Activity`),
  - parsing rules and fixtures are `prov:Entity`,
  - CI and maintainers are `prov:Agent`.

---

## 🧱 Architecture

### Recommended layering

- `parse_*` modules are pure and focused (DOM, console, network summaries).
- `normalize.ts` enforces stable shapes and ordering.
- `redact.ts` enforces safety invariants before any output leaves the process.
- output models are minimal and built for assertions + auditing.

### Anti-patterns (avoid)

- storing full network responses “for debugging”
- outputting raw DOM dumps or HTML fragments
- printing raw payloads into console logs
- allowing “debug mode” flags that bypass redaction

---

## ⚖ FAIR+CARE & Governance

Parsing utilities uphold governance by ensuring tests:

- detect safety failures (precision leaks) without reproducing them,
- store safe artifacts that can be audited and shared,
- avoid embedding restricted knowledge in test infrastructure.

If a parsing utility is found to emit unsafe content:

- treat as a governance incident for the test platform,
- remove/patch immediately,
- re-run affected governance suites and validate artifacts are safe.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Initial parsing utilities guide aligned to KFM‑MDP v11.2.6 (safe redaction-first parsing, deterministic normalization, governance-ready outputs). |

<div align="center">

[🏛️ Governance Charter](../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>


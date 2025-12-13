---
title: "🧰 Kansas Frontier Matrix — Web App Regression E2E Fixtures (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/fixtures/README.md"

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
intent: "tests-e2e-web-app-regression-fixtures"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-regression-fixtures-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:fixtures:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/fixtures/README.md"
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
  - "tests/e2e/web-app/regression/fixtures/README.md@v11.2.6"
---

<div align="center">

# 🧰 **Kansas Frontier Matrix — Web App Regression E2E Fixtures (v11 LTS)**
`tests/e2e/web-app/regression/fixtures/README.md`

**Purpose**  
Define the canonical **fixture bundle(s)** used by the **Web App Regression E2E** suite.  
These fixtures are **synthetic**, **deterministic**, **sovereignty-safe**, and **CI-auditable** to validate: map + timeline UX, Story Node v3 rendering, Focus Mode v3 panels, and governance overlays.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Fixtures-Synthetic-informational" />
<img src="https://img.shields.io/badge/Governance-FAIR%2BCARE-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Regression Suite](../README.md) · [🧭 E2E Guide](../../../README.md) · [🧱 Test Fixtures (Global)](../../../../fixtures/README.md)

</div>

---

## 📘 Overview

Regression E2E fixtures exist to make “broad coverage” tests:
- reproducible across CI runners and local machines,
- safe to publish in a public repository,
- strong enough to exercise governance rules (CARE tiers, sovereignty masking, restricted surfaces),
- stable enough to avoid brittle coupling to live services.

### Non-negotiable fixture rules
Fixtures MUST:
- be **synthetic** (no real people, no real restricted sites, no real sensitive coordinates),
- be **deterministic** (seeded; stable IDs; stable timestamps),
- be **non-identifying** (no PII; no plausible real-world identity reconstruction),
- include only the **minimum content** needed for high-signal tests.

Fixtures MUST NOT:
- embed or imply sacred-site inference, genealogies, or culturally harmful framing,
- include production tokens, secrets, or external service credentials,
- require external network access to pass a regression run.

### Fixture layering (where this folder fits)
- `tests/fixtures/` is the global “shared synthetic” layer.
- `tests/e2e/resources/` is the E2E-wide synthetic layer.
- **This folder** is the Web App Regression-only layer:
  - smaller, targeted datasets for stable UI coverage
  - governance-state scenarios (safe/blocked/masked)
  - storynode/focus-mode payloads tuned for regression flows

---

## 🗂️ Directory Layout

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 regression/
            └── 📁 fixtures/
                ├── 📄 README.md                              — This guide
                │
                ├── 🧾 fixture-bundle.json                    — Bundle index (IDs, versions, paths)
                ├── 🧾 checksums.sha256                       — SHA-256 list for all fixture artifacts
                ├── 🧾 metadata.json                          — Provenance + governance metadata (synthetic)
                │
                ├── 📁 storynodes/                            — Synthetic Story Node v3 fixtures
                │   ├── 🧾 storynode_safe.json                 — Non-sensitive, fully renderable
                │   ├── 🧾 storynode_masked.json               — Masked/generalized geometry scenario
                │   └── 🧾 storynode_restricted.json           — Restricted/redacted scenario
                │
                ├── 📁 focus-mode/                             — Synthetic Focus Mode v3 payload fixtures
                │   ├── 🧾 focus_safe.json                     — Context/Timeline/Map aligned (non-sensitive)
                │   ├── 🧾 focus_masked.json                   — Masked overlay scenario
                │   └── 🧾 focus_restricted.json               — Restricted overlay scenario
                │
                ├── 📁 governance/                             — Governance overlay fixtures
                │   ├── 🧾 care_tier_a.json                    — Tier A routing simulation (synthetic)
                │   ├── 🧾 care_tier_b.json                    — Tier B routing simulation (synthetic)
                │   ├── 🧾 care_tier_c.json                    — Tier C routing simulation (synthetic)
                │   └── 🧾 sovereignty_flags.json              — Sovereignty flags + masking expectations
                │
                ├── 📁 map/                                    — Map layer fixtures (non-sensitive)
                │   ├── 🧾 layers_manifest.json                — Layer IDs, toggles, expected UI labels
                │   └── 🧾 features_synthetic.geojson           — Synthetic features (safe bounding boxes)
                │
                └── 📁 timeline/                               — Timeline fixtures
                    └── 🧾 timeline_events.json                — Synthetic OWL-Time-compatible timeline events
~~~

Notes:
- Filenames are examples; keep the “bundle + checksums + metadata” pattern stable.
- If you add new fixtures, update `fixture-bundle.json` and `checksums.sha256`.

---

## 🧭 Context

### Deterministic identifiers (recommended)
Fixtures SHOULD use stable IDs so tests remain readable and debuggable:
- story node IDs: `kfm:storynode:test:<slug>:v11`
- focus mode entity IDs: `kfm:focus:test:<slug>:v11`
- governance case IDs: `kfm:gov:test:<tier>:<slug>:v11`

### Geometry safety rules
Fixtures MUST ensure geospatial content is safe:
- prefer “obviously synthetic” bounding boxes (non-plausible or non-localized),
- if Kansas-shaped extents are required for UI logic, use generalized polygons that do not resemble real sites,
- for “masked” cases, geometry SHOULD be generalized (H3-like cell geometry or coarse bbox),
- do not include raw coordinate dumps in fixture descriptions.

### Narrative safety rules
Fixtures MUST:
- avoid speculative or causal claims,
- avoid genealogy language,
- avoid culturally harmful phrasing even in placeholder text,
- keep narratives short and purely functional for UI.

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Load regression fixture bundle"] --> B["Boot deterministic test stack"]
  B --> C["Inject synthetic states (storynodes, focus-mode, governance)"]
  C --> D["Run UI flows (map, timeline, provenance surfaces)"]
  D --> E["Assert governance outcomes (masked, restricted, safe)"]
  E --> F["Write artifacts (report, traces, checksums)"]
~~~

Interpretation:
- Fixtures define the predictable states the UI must handle.
- Governance outcomes are asserted as UI-visible behaviors (masked, restricted, safe).

---

## 🧠 Story Node & Focus Mode Integration

### Story Node v3 fixture expectations
Story Node fixtures SHOULD include:
- `id`, `type`, `title`
- `narrative.body` (short, neutral, synthetic)
- `spacetime.geometry` (safe; masked when required)
- `spacetime.when` (synthetic OWL-Time interval or instant)
- `relations` (minimal; synthetic IDs)
- `provenance` references (IDs/hashes only; no raw dumps)

Minimum scenarios to support regression coverage:
- **safe**: fully renderable geometry + timeline
- **masked**: geometry generalized; UI indicates masking
- **restricted**: UI shows redaction/blocked content path

### Focus Mode v3 fixture expectations
Focus Mode fixtures SHOULD include:
- the 3 panels (Context/Timeline/Map) with consistent entity grounding
- “citations/provenance stubs” as identifiers (not fabricated sources)
- governance overlay flags in the payload so UI behavior can be asserted

---

## 🧪 Validation & CI/CD

Fixtures in this folder are validated by CI through:
- schema validation (JSON shape checks where applicable)
- checksum verification (`checksums.sha256`)
- secret scan and PII scan
- governance safety checks (no raw sensitive precision patterns)
- markdown lint (for this README)

Expected CI behavior:
- fixture changes SHOULD be tested by regression E2E scheduled workflows
- governance-related fixture changes SHOULD trigger additional review routing per policy

---

## 📦 Data & Metadata

### Required bundle files
This folder MUST include, at minimum:
- `fixture-bundle.json` (what exists + versions + intended suites)
- `checksums.sha256` (SHA-256 of each artifact file)
- `metadata.json` (provenance + governance declaration)

### Recommended `fixture-bundle.json` shape (example)
~~~json
{
  "bundle_id": "kfm:e2e:webapp:regression:fixtures:v11.2.6",
  "created": "2025-12-13T00:00:00Z",
  "seed": 112233,
  "fixtures": [
    { "id": "storynode_safe", "path": "storynodes/storynode_safe.json" },
    { "id": "focus_safe", "path": "focus-mode/focus_safe.json" },
    { "id": "care_tier_b", "path": "governance/care_tier_b.json" }
  ],
  "checksums_file": "checksums.sha256",
  "governance_mode": "synthetic-only"
}
~~~

### Recommended `metadata.json` fields (example)
~~~json
{
  "bundle_id": "kfm:e2e:webapp:regression:fixtures:v11.2.6",
  "classification": "Public Document",
  "sensitivity": "Low",
  "care_label": "Public · Low-Risk",
  "sovereignty_policy_applied": true,
  "contains_real_coordinates": false,
  "contains_pii": false,
  "provenance": {
    "commit_sha": "<latest-commit-hash>",
    "generated_by": "kfm-tests-fixture-tooling",
    "checksums_verified": true
  }
}
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

Fixtures and fixture bundles may be represented as:
- **PROV-O**
  - bundle generation as `prov:Activity`
  - each fixture file as `prov:Entity`
  - CI runner / maintainers as `prov:Agent`
- **DCAT**
  - bundle as `dcat:Dataset` (optional)
  - individual fixture artifacts as `dcat:Distribution` (optional)

Governance-safe rule:
- alignment records must reference **IDs, hashes, and paths**, not raw sensitive-like payloads.

---

## 🧱 Architecture

### Design pattern (fixture-driven UI testing)
Fixtures are designed to:
- drive stable UI states without reliance on mutable backend environments
- explicitly encode governance states that the UI must surface
- minimize domain complexity while preserving test signal

Recommended pattern:
- one fixture → one primary UI state
- one test → one primary claim
- avoid “fixture mutation” inside tests; prefer loading a fixture variant

---

## ⚖ FAIR+CARE & Governance

Fixtures MUST remain compliant with:
- FAIR+CARE Council expectations for public synthetic assets
- Indigenous Data Protection policy (no restricted coordinate-like content)
- repo secret/PII scanning rules

### Governance invariants (fixtures must preserve)
- “masked” fixtures must never include raw precision equivalents
- “restricted” fixtures must exercise the blocked/redaction UX without leaking payload contents
- CARE tier fixtures must simulate routing states without implying real-world authority decisions

If a fixture change could weaken sovereignty protections:
- treat as governance-impacting
- route to review per governance workflow

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Initial governed regression E2E fixtures guide (bundle + checksums + metadata; synthetic-only; sovereignty-safe). |

<div align="center">

[🏛️ Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>


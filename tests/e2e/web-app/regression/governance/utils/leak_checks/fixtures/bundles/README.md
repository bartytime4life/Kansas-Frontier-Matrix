---
title: "📦 Kansas Frontier Matrix — Leak Checks Fixture Bundles (E2E) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/governance/utils/leak_checks/fixtures/bundles/README.md"

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
intent: "tests-e2e-governance-leak-checks-bundles"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-governance-leak-checks-bundles-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:governance:utils:leak-checks:fixtures:bundles:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/governance/utils/leak_checks/fixtures/bundles/README.md"
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
  - "tests/e2e/web-app/regression/governance/utils/leak_checks/fixtures/bundles/README.md@v11.2.6"
---

<div align="center">

# 📦 **Leak Checks — Fixture Bundles (E2E) (v11 LTS)**
`tests/e2e/web-app/regression/governance/utils/leak_checks/fixtures/bundles/README.md`

**Purpose**  
Define how **bundle fixtures** group multiple leak-check cases into deterministic suites used by E2E governance regression tests.  
Bundles improve CI routing (smoke vs regression), reduce duplication, and keep leak-check signals auditable.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Test%20Type-E2E%20Governance-blueviolet" />
<img src="https://img.shields.io/badge/Surface-Leak%20Checks-informational" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Fixtures Root](../README.md) ·
[🧪 Leak Checks Module](../../README.md) ·
[🧭 E2E Guide](../../../../../../../README.md)

</div>

---

## 📘 Overview

A **bundle** is a deterministic manifest that groups multiple leak-check fixture cases into a named suite.

Bundles exist to:

- 📦 Run a known set of cases together (e.g., SAFE suite vs LEAK suite).
- 🚦 Enable CI gating (fast smoke bundle vs broader regression bundle).
- 🧾 Keep expected outcomes centralized and auditable.
- 🧪 Reduce duplicated “case lists” across spec files.

Bundles MUST:

- reference only synthetic fixture cases from `../cases/`,
- preserve stable ordering,
- declare expected outcomes at the case level,
- remain safe to publish (no plausible coordinates, no secrets, no PII).

Bundles MUST NOT:

- embed the full case payloads (cases are the source of truth),
- include network-dependent data as a required dependency,
- encode plausible real-world coordinates or geometries.

---

## 🗂️ Directory Layout

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 regression/
            └── 📁 governance/
                └── 📁 utils/
                    └── 📁 leak_checks/
                        └── 📁 fixtures/
                            ├── 📄 README.md                          — Fixtures guide (policy + formats)
                            ├── 🧾 fixture_registry.json               — Fixture ID → case file mapping
                            ├── 📁 cases/                              — Individual test cases (single-signal)
                            └── 📁 bundles/                            — Bundled suites (this folder)
                                ├── 📄 README.md                       — Bundle rules + canonical shapes
                                ├── 🧾 bundle_safe_suite.json           — SAFE: should not flag
                                ├── 🧾 bundle_leak_suite.json           — LEAK: should flag
                                └── 🧾 bundle_smoke_min.json            — Minimal PR gate selection (optional)
~~~

---

## 🧭 Context

### Why bundles exist

Leak checks often require:
- multiple surfaces (DOM excerpts, network excerpts, download previews),
- both positive and negative coverage,
- careful separation of “merge-blocking” vs “nightly” cases.

Bundles provide a governed mechanism to:
- keep the spec code thin,
- keep case selection consistent across runners,
- make CI intent obvious by filename and tags.

### Naming rules

Bundle filenames SHOULD follow:

- `bundle_<suite>.json`

Recommended suites:
- `bundle_smoke_min.json` — minimal, high-signal PR gate selection
- `bundle_safe_suite.json` — negative controls (should pass)
- `bundle_leak_suite.json` — positive controls (should fail)
- `bundle_regression_full.json` — optional superset for scheduled runs

### Determinism contract

Bundles MUST:
- list cases in stable order,
- avoid globbing or directory scans as primary selection,
- reference cases by `fixture_id` (preferred) or explicit relative `path` (allowed).

If a generator is used to produce bundles:
- the seed MUST be pinned,
- the resulting JSON MUST be committed (bundles are artifacts, not runtime outputs).

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Select bundle file"] --> B["Load bundle manifest"]
  B --> C["Resolve fixture_ids via registry"]
  C --> D["Load case payloads"]
  D --> E["Run leak detectors"]
  E --> F["Compare outcomes to bundle expectations"]
  F --> G["Write reports, snapshots, telemetry"]
~~~

Interpretation:
- Bundles define which cases run together and what outcomes are expected, while payload truth remains in `cases/`.

---

## 🧪 Validation & CI/CD

Bundles are merge-sensitive governance artifacts.

Bundles MUST pass:

- ✅ JSON parse validation
- ✅ schema validation (if bundle schema exists)
- ✅ secret scan
- ✅ PII scan (best-effort)
- ✅ fixture lint checks:
  - case references exist
  - duplicate fixture_ids not allowed
  - stable ordering (no nondeterministic sorting)

### CI routing (recommended)

- PR gate uses `bundle_smoke_min.json` (fast, deterministic).
- Nightly uses `bundle_regression_full.json` (optional).
- Governance suites SHOULD always include at least one SAFE and one LEAK case.

Retries are discouraged for governance failures.

---

## 📦 Data & Metadata

### Bundle manifest (canonical shape)

Bundles SHOULD be simple and explicit:

~~~json
{
  "schema_version": "v11.2.6",
  "bundle_id": "bundle_safe_suite",
  "description": "Negative controls for leak detection (should not flag).",
  "tags": ["@governance", "@regression"],
  "cases": [
    {
      "fixture_id": "safe_dom_excerpt",
      "expected": "pass"
    },
    {
      "fixture_id": "safe_network_excerpt",
      "expected": "pass"
    }
  ]
}
~~~

### Bundle case fields (allowed set)

Each case entry SHOULD include:

- `fixture_id` (preferred) — must exist in `../fixture_registry.json`
- `expected` — `pass` or `fail`
- `expect_categories` (optional) — list of match categories for LEAK cases
- `notes` (optional) — short explanation (keep it brief)

Example LEAK case entry:

~~~json
{
  "fixture_id": "leak_like_numbers_oob",
  "expected": "fail",
  "expect_categories": ["coordinate_like_numeric_pair"],
  "notes": "Synthetic out-of-range numeric pair; must be flagged."
}
~~~

### What should NOT be in bundles

Bundles MUST NOT contain:
- the full `payload` text,
- embedded geometry objects,
- long excerpts of documents,
- any plausible coordinate pair.

Those belong in controlled `cases/` files and must follow the fixture safety rules.

---

## 🧱 Architecture

### How bundles integrate with specs

Specs SHOULD:
- choose a bundle by name (configurable via tag or env),
- load the bundle manifest,
- resolve fixture_ids via `fixture_registry.json`,
- execute cases with shared helpers,
- emit one report per bundle.

This design:
- keeps spec code small,
- keeps fixture intent centralized,
- makes it easy to quarantine individual cases without rewriting tests.

---

## ⚖ FAIR+CARE & Governance

### Sovereignty-safe requirements (non-negotiable)

Bundles MUST:
- never reference or encode plausible coordinates,
- remain synthetic and publish-safe,
- preserve governance intent:
  - SAFE bundles validate no false positives,
  - LEAK bundles validate enforcement catches leak-like signals.

### Escalation

If a bundle introduces or amplifies policy risk:
- remove/rollback the bundle change immediately,
- quarantine affected suites,
- route review to FAIR+CARE Council and governance test owners.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Initial leak-check bundle guide aligned to KFM-MDP v11.2.6 (deterministic, explicit, governance-safe). |

<div align="center">

[🏛️ Governance Charter](../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>


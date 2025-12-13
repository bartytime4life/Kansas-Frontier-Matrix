---
title: "🧪 Kansas Frontier Matrix — Leak Checks Fixture Cases (E2E) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/governance/utils/leak_checks/fixtures/cases/README.md"

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
intent: "tests-e2e-governance-leak-checks-cases"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-governance-leak-checks-cases-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:governance:utils:leak-checks:fixtures:cases:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/governance/utils/leak_checks/fixtures/cases/README.md"
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
  - "tests/e2e/web-app/regression/governance/utils/leak_checks/fixtures/cases/README.md@v11.2.6"
---

<div align="center">

# 🧪 **Leak Checks — Fixture Cases (E2E) (v11 LTS)**
`tests/e2e/web-app/regression/governance/utils/leak_checks/fixtures/cases/README.md`

**Purpose**  
Define the **canonical single-signal fixture cases** used by governance leak checks in E2E regression tests.  
Cases in this folder are **synthetic**, **deterministic**, and designed to verify that KFM surfaces **do not leak** sensitive precision, restricted content, secrets, or PII-like patterns.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Test%20Type-E2E%20Governance-blueviolet" />
<img src="https://img.shields.io/badge/Fixture%20Unit-Case-informational" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Bundles](../bundles/README.md) ·
[📦 Fixtures Root](../README.md) ·
[🧪 Leak Checks Module](../../README.md)

</div>

---

## 📘 Overview

A **case** is the smallest fixture unit for leak checks:

- One case = one primary “leak-like” (or “safe”) signal.
- Cases are assembled into suites via `../bundles/*.json`.
- Cases are resolved by ID via `../fixture_registry.json`.

Cases exist to validate **negative controls** (no false positives) and **positive controls** (detectors fire reliably), across multiple surfaces:

- 🧭 UI/DOM excerpts
- 🌐 network-response excerpts
- 📦 download/preview excerpts
- 🧾 provenance chips / evidence surfaces (IDs and hashes only)

Cases MUST be:

- **Synthetic**: no real persons, no real addresses, no real site geometry.
- **Deterministic**: stable IDs, stable ordering, stable timestamps (or injected clock).
- **Publish-safe**: suitable for public repos and CI logs.

Cases MUST NOT:

- contain plausible real-world coordinates or “real-looking” site geometry,
- include any secrets, tokens, or credential-like strings,
- contain identifying personal information,
- require live network access as a dependency.

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
                        ├── 📄 README.md                               — Leak checks overview (policy + runbook)
                        └── 📁 fixtures/
                            ├── 📄 README.md                           — Fixtures guide (formats + guardrails)
                            ├── 🧾 fixture_registry.json                — Fixture ID → case path mapping
                            ├── 📁 bundles/                             — Bundle manifests (suite selection)
                            │   ├── 📄 README.md
                            │   └── 🧾 bundle_smoke_min.json
                            └── 📁 cases/                               — Single-signal case fixtures (this folder)
                                ├── 📄 README.md                        — Case rules + canonical schema
                                ├── 🧾 safe_dom_excerpt.json             — Negative control (should pass)
                                ├── 🧾 safe_network_excerpt.json         — Negative control (should pass)
                                ├── 🧾 leak_like_numeric_pair.json       — Positive control (should fail)
                                ├── 🧾 leak_like_token_pattern.json      — Positive control (should fail)
                                └── 🧾 leak_like_geometry_dump.json      — Positive control (should fail; synthetic only)
~~~

---

## 🧭 Context

### Case philosophy: “single-signal, high-signal”
Cases SHOULD:

- focus on one detector category per file,
- be small enough to read in a diff,
- use short excerpts (not full pages),
- be explicit about expectations.

Cases SHOULD NOT:

- combine multiple unrelated leak patterns,
- embed large blobs of HTML/JSON unless required,
- replicate real historical narratives or real geographic descriptions.

### Naming conventions
Recommended filename prefixes:

- `safe_*.json` — negative controls (expected: `pass`)
- `leak_like_*.json` — positive controls (expected: `fail`)

Recommended surfaces:

- `dom` — what a user sees in the rendered UI
- `network` — API payload excerpts captured/recorded by the runner
- `download` — content written to disk (export, JSON download, report artifact)

### Deterministic IDs and ordering
Each case MUST include:

- a stable `fixture_id`,
- a stable `schema_version`,
- explicit `expected` outcome,
- stable ordering for any arrays in the case.

If a generator is used:
- the generator must be seeded,
- the resulting case JSON must be committed and treated as the artifact of record.

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Load fixture_registry.json"] --> B["Resolve fixture_id to case path"]
  B --> C["Load case payload"]
  C --> D["Run leak detectors"]
  D --> E["Compare to expected outcome"]
  E --> F["Emit report + snapshots + telemetry"]
~~~

Interpretation:
- Cases are the atomic inputs; bundles select groups of cases; the detector output is compared against each case’s declared expectation.

---

## 🧪 Validation & CI/CD

Cases are **governance-sensitive** and must be CI-clean.

Cases MUST pass:

- ✅ JSON parse validation
- ✅ schema validation (when a case schema exists)
- ✅ secret scan
- ✅ PII scan (best-effort)
- ✅ leak-check fixture lint rules:
  - `fixture_id` is unique across all cases
  - referenced surfaces are valid
  - `expected` is one of `pass` / `fail`
  - no plausible coordinate patterns (see governance rules below)

### Quarantine policy
If a case is flaky or unstable:
- move it out of PR-gated bundles (e.g., keep it only in nightly bundles),
- keep the case itself deterministic (flake ≠ randomness; flake = fragile setup).

Governance failures are **not** retryable by default.

---

## 📦 Data & Metadata

### Canonical case shape (recommended)
A case file SHOULD follow this structure:

~~~json
{
  "schema_version": "v11.2.6",
  "fixture_id": "leak_like_numeric_pair",
  "description": "Synthetic numeric-pair pattern intended to trigger coordinate-like detectors.",
  "surface": "dom",
  "payload_type": "text",
  "payload": "[999.999, -999.999] -- synthetic sentinel values (invalid range; non-real).",
  "expected": "fail",
  "expect_categories": ["coordinate_like_numeric_pair"],
  "tags": ["@governance", "@regression"]
}
~~~

### Payload rules
Payloads MUST:

- be short excerpts (not full pages),
- avoid plausible real-world lat/lon pairs,
- avoid real entity names (people, addresses, real institutions),
- avoid secrets (tokens/keys/cookies).

If a detector requires numeric-like patterns:
- use **clearly invalid sentinel values** (e.g., `999.999`) or tokenized placeholders.

### Expected outcomes
- `expected: "pass"` for negative controls
- `expected: "fail"` for positive controls

`expect_categories` SHOULD be present for positive controls to keep detector intent explicit and auditable.

---

## 🌐 STAC, DCAT & PROV Alignment

### PROV-O interpretation (tests)
- A case file is a `prov:Entity`.
- A leak-check run is a `prov:Activity`.
- The CI runner and maintainers are `prov:Agent`s.

Case files MUST remain safe to publish (public repo + CI logs).

### STAC/DCAT (optional indexing)
If test fixtures are indexed:
- treat them as test artifacts, not real datasets,
- use `geometry: null` for any STAC-like representation,
- ensure any coverage fields are synthetic and non-sensitive.

---

## 🧱 Architecture

### How specs should consume cases (recommended)
Specs SHOULD:

1. choose a bundle,
2. resolve case IDs via the registry,
3. load case payloads,
4. run detectors against the relevant surface output,
5. compare to `expected` and `expect_categories`,
6. emit a per-bundle report and per-case snapshots on failure.

This avoids hardcoding leak patterns inside test code and keeps fixtures auditable.

---

## ⚖ FAIR+CARE & Governance

### Sovereignty-safe rules (non-negotiable)
Cases MUST NOT encode:

- plausible real-world coordinates,
- plausible site geometry or “realistic” restricted map output,
- any content that could be interpreted as restricted cultural knowledge.

Case fixtures are allowed to simulate leak-like patterns ONLY when:
- the patterns are synthetic,
- values are clearly invalid or tokenized,
- the intent is solely detector verification.

### Ethical language rules
Even synthetic payload text MUST:
- avoid colonial framing,
- avoid culturally harmful phrasing,
- avoid implying genealogy or sacred knowledge.

### Escalation
If any case violates policy:
- delete or remediate immediately,
- remove it from all bundles until reviewed,
- route review to FAIR+CARE Council and governance test owners.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Initial leak-check case guide aligned to KFM-MDP v11.2.6 (atomic fixtures, deterministic, governance-safe). |

<div align="center">

[🏛️ Governance Charter](../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>


---
title: "🕵️ Kansas Frontier Matrix — Leak Checks Test Suite (E2E) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/governance/utils/leak_checks/__tests__/README.md"

version: "v11.2.6"
last_updated: "2025-12-13"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous Systems Oversight · FAIR+CARE Council"
content_stability: "stable"

status: "Active · Enforced"
doc_kind: "Testing Guide"
header_profile: "standard"
footer_profile: "standard"
intent: "tests-e2e-governance-leak-checks-tests"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-governance-leak-checks-tests-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:governance:utils:leak-checks:tests:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/governance/utils/leak_checks/__tests__/README.md"
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

signature_ref: "../../../../../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../../../../../releases/v11.2.6/tests-e2e-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/tests-e2e-v11.json"
energy_schema: "../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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
  - "tests/e2e/web-app/regression/governance/utils/leak_checks/__tests__/README.md@v11.2.6"
---

<div align="center">

# 🕵️ **Leak Checks — Test Suite (E2E) (v11 LTS)**
`tests/e2e/web-app/regression/governance/utils/leak_checks/__tests__/README.md`

**Purpose**  
Define the **canonical leak-check test suite** used to prevent **sensitive precision leakage** and other governed-data escapes across **web UI regression flows** (Focus Mode, Story Nodes, governance overlays, downloads, tooltips, and provenance surfaces).

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Test%20Type-E2E%20Governance-blueviolet" />
<img src="https://img.shields.io/badge/Policy-Leak%20Prevention-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Leak Checks](../README.md) · [🧰 Governance Utils](../../README.md) · [🧭 E2E Guide](../../../../README.md)

</div>

---

## 📘 Overview

This folder contains **merge-blocking** governance regression tests that detect and fail on:

- **Sensitive precision leakage**
  - raw lat/long values in UI text, tooltips, downloads, or debug panels
  - raw GeoJSON coordinate arrays being displayed or returned in UI-exposed payloads
  - “too-precise” representations where masking/generalization is required
- **Restricted-state failures**
  - restricted content rendering instead of redacting/masking/blocking
  - governance badges missing or inconsistent with the scenario’s expected state
- **Provenance surface regressions**
  - missing required reference anchors (IDs/hashes)
  - evidence chips showing forbidden payload content

These tests are designed to be:

- **Deterministic** (stable fixtures, stable selectors, stable assertions)
- **Sovereignty-safe** (no real locations; no plausible restricted geometries)
- **High-signal** (one primary policy claim per spec, minimal noise)

---

## 🗂️ Directory Layout

This test suite lives under the governance utilities path and is intentionally colocated with the leak-check implementation.

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 regression/
            └── 📁 governance/
                └── 📁 utils/
                    └── 📁 leak_checks/
                        ├── 📄 README.md                          — Leak checks module guide (concepts + patterns)
                        ├── 📁 __tests__/                         — Leak checks test suite (this folder)
                        │   ├── 📄 README.md                      — This guide (suite rules + CI behavior)
                        │   ├── 📄 dom_leak.spec.ts               — DOM/text surface leak assertions
                        │   ├── 📄 network_leak.spec.ts           — API/network surface leak assertions
                        │   ├── 📄 downloads_leak.spec.ts         — Download/artifact leak assertions
                        │   └── 📁 snapshots/                     — Optional golden baselines (deterministic)
                        └── 📁 fixtures/                          — Suite-local synthetic fixtures (non-identifying)
                            ├── 🧾 leak_cases.json                — Targeted synthetic “should fail” cases (quarantined)
                            └── 🧾 allowlist.json                 — Approved false-positive exceptions (minimal)
~~~

Notes:
- Filenames are the **canonical target layout**. If the runner uses a different naming convention, preserve the *structure and intent*.
- Any fixture under this suite must remain **synthetic**, **non-identifying**, and **safe to publish**.

---

## 🧭 Context

### What “leak” means in KFM E2E

A “leak” is any user-visible or user-accessible output that exposes information at a precision or category that governance forbids, including:

- raw coordinate-like strings (lat/long, projected coordinates, WKT-like forms)
- raw geometry dumps (GeoJSON coordinate arrays) in UI surfaces
- “hidden” leaks in:
  - DOM text
  - downloadable files
  - URL query strings
  - API responses surfaced through debug tools
  - logs/console errors visible in test artifacts

### Determinism contract

These tests MUST:
- use **scenario fixtures** with fixed IDs and fixed timestamps (or injected time)
- avoid “sleep-and-hope” timing (use event/state-driven waits)
- produce stable, comparable failure artifacts (same input → same output)

### Suite scope boundaries

These tests do NOT attempt to:
- validate scientific correctness of datasets
- validate model quality metrics
- replace unit-level masking tests

They do:
- validate that **governed surfaces** never reveal **forbidden precision**.

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Run spec"] --> B["Render scenario state"]
  B --> C["Collect surfaces (DOM, network, downloads)"]
  C --> D["Apply leak matchers (patterns + allowlist)"]
  D -->|no matches| E["PASS (no leak)"]
  D -->|match found| F["FAIL + write leak report artifact"]
~~~

Interpretation:
- Leak checks treat the application as a black box and scan what a user could see or retrieve.

---

## 🧪 Validation & CI/CD

### Merge-blocking policy

- Leak-check specs are **merge-blocking** when included in `@smoke` or `@governance` gates.
- Governance failures are **not retryable by default** (retries can hide real leaks).

### Expected artifacts (on failure)

On a failure, the suite SHOULD emit:
- a concise failure message including:
  - surface type (`dom`, `network`, `download`)
  - scenario ID
  - matcher ID
- a machine-readable leak report artifact

Recommended artifact location:
~~~text
reports/
└── e2e/
    └── leak_checks/
        ├── leak-report.json
        ├── excerpts/                          # redacted excerpts only
        └── traces/                            # runner traces (optional)
~~~

### Quarantine rule

- If a test is flaky, it must be quarantined behind `@nightly` **only if** it does **not** reduce leak prevention coverage.
- Any quarantine MUST keep at least one equivalent high-signal leak assertion in merge-blocking gates.

---

## 📦 Data & Metadata

### Leak report shape (recommended)

A leak report must be safe to store and share. It MUST:
- avoid dumping full payloads
- include **redacted excerpts** only
- include enough metadata to reproduce locally

Example (simplified):
~~~json
{
  "schema_version": "v11.2.6",
  "run_id": "<ci-run-id>",
  "scenario_id": "focus_masked",
  "surface": "dom",
  "violations": [
    {
      "matcher_id": "latlon_high_precision",
      "rule": "no-raw-coordinates",
      "location": "FocusModeMapTooltip",
      "excerpt_redacted": "… lat=<redacted> lon=<redacted> …",
      "severity": "blocker"
    }
  ],
  "allowlist_applied": false
}
~~~

### Pattern/allowlist rule (minimal by design)

- Patterns MUST be reviewed and kept minimal.
- Allowlists MUST be:
  - rare
  - narrowly scoped
  - documented with a reason and an expiry review window

---

## 🌐 STAC, DCAT & PROV Alignment

### PROV-O alignment

- A leak-check run is a `prov:Activity`.
- Fixtures and matcher configs are `prov:Entity`.
- CI runner and maintainers are `prov:Agent`.

The leak report artifact is a test `prov:Entity` and should be referenceable from:
- governance ledgers (if used)
- CI summaries and release telemetry

### Telemetry alignment

Leak checks SHOULD contribute to `tests-e2e-telemetry.json` with:
- `leak_checks_total`
- `leak_checks_failed`
- `leak_checks_by_surface` (dom/network/download)
- runtime and artifact byte totals (where available)

---

## 🧱 Architecture

### Test design pattern (recommended)

Each spec SHOULD follow:
1. bootstrap scenario (synthetic fixture)
2. render or navigate to governed surface
3. collect one surface type (DOM *or* network *or* download)
4. run matchers
5. assert “no violations”
6. emit artifact on failure

This keeps failures:
- localized
- easy to reproduce
- easy to triage (what leaked, where, and why)

### Surface types (canonical set)

- **DOM**: visible text, tooltip content, modal content, debug panels
- **Network**: intercepted JSON payloads that are rendered or user-exposed
- **Downloads**: exported JSON/CSV/GeoJSON artifacts, if available in UI

---

## ⚖ FAIR+CARE & Governance

### Non-negotiable governance rules

This suite MUST enforce:
- no sensitive coordinate disclosure in any user-visible surface
- restricted-state UI is redacted/masked/blocked (never “partially shown”)
- governance badges and labels reflect the scenario’s expected classification

### Escalation policy

If any leak-check test fails:
- treat as **stop-ship** for governed-output changes
- route to:
  - the relevant UI/pipeline owner
  - governance reviewers for masking/policy verification
  - FAIR+CARE Council when sovereignty controls are implicated

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Initial leak-checks test suite guide aligned to KFM-MDP v11.2.6 (deterministic, sovereignty-safe, merge-blocking governance assertions). |

<div align="center">

[🏛️ Governance Charter](../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>


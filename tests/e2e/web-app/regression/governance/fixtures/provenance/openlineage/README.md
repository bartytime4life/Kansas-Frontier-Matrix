---
title: "🔗 Kansas Frontier Matrix — Provenance Fixtures: OpenLineage (E2E) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/governance/fixtures/provenance/openlineage/README.md"

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
intent: "tests-e2e-web-app-regression-governance-fixtures-provenance-openlineage"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-regression-governance-fixtures-provenance-openlineage-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:governance:fixtures:provenance:openlineage:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/governance/fixtures/provenance/openlineage/README.md"
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
  - "tests/e2e/web-app/regression/governance/fixtures/provenance/openlineage/README.md@v11.2.6"
---

<div align="center">

# 🔗 **Provenance Fixtures — OpenLineage (E2E) (v11 LTS)**
`tests/e2e/web-app/regression/governance/fixtures/provenance/openlineage/README.md`

**Purpose**  
Define the **canonical OpenLineage fixture set** used by governance E2E regression suites to validate:
- provenance surfaces (chips, overlays, evidence panels),
- OpenLineage facet parsing and UI mapping,
- governance-safe presentation (reference-only; no payload dumps; no precision leakage).

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Provenance-OpenLineage%20v2.5-informational" />
<img src="https://img.shields.io/badge/Surface-Governance%20E2E-blueviolet" />
<img src="https://img.shields.io/badge/Policy-Reference--Only-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Provenance Fixtures](../README.md) ·
[⬅️ Governance Fixtures](../../README.md) ·
[⬅️ Governance Regression](../../../README.md) ·
[🧭 E2E Guide](../../../../../../README.md)

</div>

---

## 📘 Overview

This folder contains **synthetic OpenLineage events and mapping helpers** used by E2E suites to validate provenance UX without using:
- real datasets,
- production job/run identifiers,
- sensitive geometries, coordinates, or plausible “real site” references,
- full payload dumps.

These fixtures exist to support **high-signal, governance-safe** assertions such as:
- ✅ provenance chips render and remain non-empty (IDs/hashes only),
- ✅ OpenLineage facets are interpreted consistently (job/run/dataset facets),
- ✅ restricted/masked states never expand into raw payload visibility,
- ✅ telemetry/provenance views remain safe under failure conditions (no debug leaks).

**Non-goals**
- These fixtures are not authoritative OpenLineage documentation.
- These fixtures are not production schemas or runtime config.
- These fixtures are not a place to store “realistic fake” data that could enable sensitive inference.

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
                        └── 📁 openlineage/
                            ├── 📄 README.md                         — This guide
                            │
                            ├── 🧾 registry.json                      — Index of fixture bundles and intended usage
                            │
                            ├── 📁 events/                            — Synthetic OpenLineage events (reference-only)
                            │   ├── 🧾 run_start_minimal.json          — Minimal run start event (safe fields only)
                            │   ├── 🧾 run_complete_minimal.json       — Minimal run complete event (safe fields only)
                            │   ├── 🧾 run_fail_safe.json              — Failure event (redacted errors; no payload dumps)
                            │   └── 🧾 run_with_governance_facets.json  — Includes CARE/sovereignty facet placeholders
                            │
                            ├── 📁 facets/                            — Synthetic facet fragments (composable)
                            │   ├── 🧾 job_facets.json                 — Job facet placeholders + allowed keys
                            │   ├── 🧾 run_facets.json                 — Run facet placeholders + allowed keys
                            │   ├── 🧾 dataset_facets.json             — Dataset facet placeholders (no locations)
                            │   └── 🧾 kfm_facets.json                 — KFM-specific facet placeholders (governance-safe)
                            │
                            ├── 📁 mappings/                          — UI-oriented mapping helpers for tests (optional)
                            │   ├── 🧾 facet_to_chip_map.json          — Facet type → UI chip type
                            │   └── 🧾 facet_redaction_rules.json      — Facet presentation rules (reference-only)
                            │
                            └── 📁 expected/                          — Expected summaries (safe, high-signal)
                                ├── 🧾 expected_chip_set.json          — Expected chip categories present for a scenario
                                └── 🧾 expected_redaction_state.json   — Expected redaction posture (masked/restricted)
~~~

Notes:
- Filenames above are the **canonical target layout**.
- If your repo uses a different layout, preserve intent:
  - events (synthetic OL payloads),
  - facets (composable fragments),
  - mapping helpers (UI expectations),
  - expected summaries (safe assertions).

---

## 🧭 Context

### Why OpenLineage fixtures exist in governance E2E

OpenLineage surfaces are user-visible via:
- provenance chips,
- “evidence” panels,
- run/job identifiers in audit views,
- safe summaries in telemetry/provenance overlays.

These surfaces are high-risk for regressions that can cause:
- debug payload dumps,
- unintended precision leakage via “dataset facets,”
- exposure of restricted routing metadata.

### Reference-only rule (non-negotiable)

Fixtures MUST remain **reference-only**:
- IDs and hashes are allowed (synthetic placeholders are preferred).
- Human-readable labels must be minimal and non-identifying.
- No raw documents, no geometry payloads, no coordinate-like fields.

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Load OpenLineage registry"] --> B["Select event bundle for scenario"]
  B --> C["Inject event(s) into test stack or mock layer"]
  C --> D["UI renders provenance surfaces"]
  D --> E["Assertions validate chips and redaction posture"]
  E --> F["Write safe artifacts (summaries only)"]
~~~

Interpretation:
- OpenLineage fixtures provide deterministic provenance inputs so the UI can be validated without unsafe payload exposure.

---

## 🧠 Story Node & Focus Mode Integration

OpenLineage fixtures may be used by E2E scenarios that traverse governed narrative surfaces:

- **Story Node v3**: evidence chips / provenance overlays should show stable references.
- **Focus Mode v3**: provenance/evidence panels should remain safe across panel switching.

Minimum invariants supported by these fixtures:
- provenance references remain stable during navigation,
- masked/restricted posture remains consistent across route transitions,
- failures never cause raw payload leakage into UI or artifacts.

---

## 🧪 Validation & CI/CD

OpenLineage fixtures MUST pass:
- ✅ JSON parse validation
- ✅ secret scan
- ✅ PII scan (best-effort)
- ✅ leak checks (no coordinate-like strings, no geometry keys, no bbox payloads)

Recommended fixture lint rules:
- enforce `schema_version` keys in `registry.json` and any expected summary file,
- require deterministic ordering of arrays and object keys (formatter in CI is recommended),
- explicitly forbid high-risk keys (examples: `coordinates`, `geometry`, `bbox`, `wkt`) unless value is `null` or `"REDACTED"`.

---

## 📦 Data & Metadata

### Registry model (recommended minimal shape)

~~~json
{
  "schema_version": "v11.2.6",
  "bundles": {
    "ol_minimal_pass": {
      "events": [
        "events/run_start_minimal.json",
        "events/run_complete_minimal.json"
      ],
      "expected": [
        "expected/expected_chip_set.json",
        "expected/expected_redaction_state.json"
      ],
      "tags": ["@regression", "@governance"]
    },
    "ol_fail_safe": {
      "events": ["events/run_fail_safe.json"],
      "expected": ["expected/expected_redaction_state.json"],
      "tags": ["@regression", "@governance"]
    }
  },
  "defaults": {
    "redaction_posture": "reference_only",
    "allow_payload_dump": false
  }
}
~~~

### Fixture content guardrails (what belongs in an OpenLineage event)

Allowed (recommended):
- synthetic `job.name`, `run.runId` placeholders,
- synthetic dataset identifiers (string aliases),
- KFM governance facets as **placeholders** (no sensitive content),
- minimal timestamps.

Forbidden:
- real URLs containing secrets,
- raw payload dumps or embedded stack traces,
- location-like data that could be interpreted as a real place.

---

## 🌐 STAC, DCAT & PROV Alignment

OpenLineage fixtures are **test assets**, not production provenance.

- **DCAT**: event fixtures may be treated as test distributions (`mediaType: application/json`).
- **STAC**: if represented as STAC items, use:
  - `geometry: null`
  - `properties.datetime` set to fixture update time
  - assets: `events/*.json`, `facets/*.json`
- **PROV‑O**:
  - fixture files are `prov:Entity`,
  - E2E run consuming them is a `prov:Activity`,
  - CI runner is a `prov:Agent`.

---

## 🧱 Architecture

### Recommended fixture usage pattern

Governance E2E specs SHOULD:
1. select a bundle from `registry.json`,
2. inject events into the test stack (API mock/intercept or local provenance sink),
3. validate UI surfaces with:
   - chip presence/type assertions,
   - redaction posture assertions,
   - “no payload dump” assertions,
4. write artifacts as **summaries only** (counts, chip types, rule IDs).

This avoids:
- hardcoding OpenLineage content in specs,
- fragile string matching on raw JSON,
- unsafe snapshotting of full event payloads.

---

## ⚖ FAIR+CARE & Governance

OpenLineage fixtures must uphold:
- **Authority to Control**: reference-only provenance; no sensitive precision.
- **Responsibility**: prevent “debug surfaces” from becoming leakage channels.
- **Ethics**: avoid embedding plausible restricted knowledge, even synthetically.

If a fixture is found to violate policy:
- remove it immediately,
- invalidate dependent tests until fixed,
- route review to the appropriate working group and FAIR+CARE Council.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-14 | Initial OpenLineage provenance fixtures guide aligned to KFM‑MDP v11.2.6 (reference-only, governance-safe, deterministic E2E support). |

<div align="center">

[🏛️ Governance Charter](../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>


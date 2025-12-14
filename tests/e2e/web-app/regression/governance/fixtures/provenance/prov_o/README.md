---
title: "🧬 Kansas Frontier Matrix — Provenance Fixtures: PROV‑O (E2E) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/governance/fixtures/provenance/prov_o/README.md"

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
intent: "tests-e2e-web-app-regression-governance-fixtures-provenance-prov-o"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-regression-governance-fixtures-provenance-prov-o-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:governance:fixtures:provenance:prov-o:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/governance/fixtures/provenance/prov_o/README.md"
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
  - "tests/e2e/web-app/regression/governance/fixtures/provenance/prov_o/README.md@v11.2.6"
---

<div align="center">

# 🧬 **Provenance Fixtures — PROV‑O (E2E) (v11 LTS)**
`tests/e2e/web-app/regression/governance/fixtures/provenance/prov_o/README.md`

**Purpose**  
Define the **canonical PROV‑O fixture set** used by governance E2E regression suites to validate:
- provenance surfaces (chips, overlays, evidence panels),
- PROV‑O parsing and UI mapping (Activity / Entity / Agent),
- governance-safe presentation (**reference-only**, no payload dumps, no precision leakage).

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Provenance-PROV--O-informational" />
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

This folder contains **synthetic PROV‑O fragments** used by governance E2E suites to validate that the web app:

- renders provenance references safely (IDs, labels, hashes),
- correctly distinguishes `prov:Activity`, `prov:Entity`, and `prov:Agent`,
- preserves a governed **reference-only** posture in UI and artifacts,
- does not regress into unsafe debug behaviors (payload dumps, stack traces containing sensitive fragments).

Fixtures here MUST be:
- ✅ **Synthetic** (non-identifying; no real people, no real datasets, no real runs),
- ✅ **Deterministic** (stable IDs and stable ordering),
- ✅ **Sovereignty-safe** (no coordinate-like values; no geometry payloads; no bboxes),
- ✅ **Auditable** (fixture intent is clear; outputs are safe to store as artifacts).

Fixtures here MUST NOT:
- include real individuals, addresses, emails, or organizational identifiers,
- embed raw coordinates or plausible “real site” geometries,
- store full documents or “realistic fake” narrative content,
- include secrets, tokens, credentials, or production URLs.

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
                            ├── 📄 README.md                         — This guide
                            │
                            ├── 🧾 registry.json                      — Bundle index (scenario → prov fragment set)
                            │
                            ├── 📁 fragments/                         — Composable PROV‑O fragments (synthetic)
                            │   ├── 🧾 activity_minimal.jsonld         — prov:Activity (minimal, safe)
                            │   ├── 🧾 entity_minimal.jsonld           — prov:Entity (minimal, safe)
                            │   ├── 🧾 agent_minimal.jsonld            — prov:Agent (minimal, safe)
                            │   └── 🧾 relations_minimal.jsonld        — wasGeneratedBy / used / wasAssociatedWith
                            │
                            ├── 📁 bundles/                            — Scenario bundles (reference-only)
                            │   ├── 🧾 prov_public_bundle.jsonld        — Public posture (no masking required)
                            │   ├── 🧾 prov_masked_bundle.jsonld        — Masked posture (policy-safe placeholders)
                            │   └── 🧾 prov_restricted_bundle.jsonld    — Restricted posture (blocked/redacted UX)
                            │
                            ├── 📁 mappings/                           — UI mapping helpers (optional)
                            │   ├── 🧾 prov_to_chip_map.json            — PROV predicate/type → UI chip mapping
                            │   └── 🧾 prov_redaction_rules.json        — Reference-only presentation rules
                            │
                            └── 📁 expected/                           — Expected summaries (safe, high-signal)
                                ├── 🧾 expected_chip_set.json          — Expected chip categories per bundle
                                └── 🧾 expected_redaction_state.json   — Expected redaction posture (masked/restricted)
~~~

Notes:
- Filenames above are the **canonical target layout**.
- Use `.jsonld` for JSON-LD; use `.ttl` only if your repo already supports RDF/Turtle fixtures.
- If `.ttl` is used, keep it minimal and synthetic (no external IRIs that imply real systems).

---

## 🧭 Context

### Why PROV‑O fixtures matter in governance E2E

Provenance is a governance surface. If it regresses, the UI may:
- lose traceability (empty chips, missing “used/wasGeneratedBy” links),
- accidentally leak unsafe details through debug views,
- display restricted items as if they were public.

These fixtures exist so tests can validate:
- provenance is **present**,
- provenance is **safe**,
- provenance is **stable** and **deterministic** in the UI.

### Reference-only rule (non-negotiable)

Fixtures MUST remain **reference-only**:
- Use synthetic IDs (stable strings are preferred).
- Use placeholder hashes (e.g., `<sha256>` or `HASH_REDACTED`).
- Do not embed raw payload contents (documents, geometry, coordinate-like strings).

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Load PROV-O registry"] --> B["Select bundle for scenario"]
  B --> C["Inject PROV fragments or bundle into test stack"]
  C --> D["UI renders provenance chips / overlays"]
  D --> E["Assertions validate chip set + redaction posture"]
  E --> F["Write safe artifacts (summaries only)"]
~~~

Interpretation:
- PROV‑O fixtures provide deterministic provenance inputs so governance E2E can validate safe rendering and policy posture.

---

## 🧠 Story Node & Focus Mode Integration

PROV‑O fixtures are used wherever provenance becomes user-visible, including:

- Story Node v3 evidence/provenance chips,
- Focus Mode v3 evidence panels and provenance overlays,
- governance audit and verification panels.

Minimum invariants supported by these fixtures:
- chips and references remain stable during navigation,
- redaction posture (public/masked/restricted) remains consistent across route transitions,
- failure modes never dump raw provenance payloads into the UI or artifacts.

---

## 🧪 Validation & CI/CD

PROV‑O fixtures MUST pass:
- ✅ JSON parse validation (and JSON-LD validation if available)
- ✅ secret scan
- ✅ PII scan (best-effort)
- ✅ leak checks (no coordinate-like strings; no geometry keys; no bbox payloads)

Recommended fixture lint rules:
- require `@context` for JSON-LD fragments where used,
- enforce stable ordering in arrays (IDs sorted),
- forbid high-risk keys and patterns unless explicitly redacted:
  - `coordinates`, `geometry`, `bbox`, `wkt`, `POINT(`, `POLYGON(`,
  - lat/long-like numeric pairs.

---

## 📦 Data & Metadata

### Registry model (recommended minimal shape)

~~~json
{
  "schema_version": "v11.2.6",
  "bundles": {
    "prov_public": {
      "bundle": "bundles/prov_public_bundle.jsonld",
      "expected": [
        "expected/expected_chip_set.json",
        "expected/expected_redaction_state.json"
      ],
      "tags": ["@regression", "@governance"]
    },
    "prov_masked": {
      "bundle": "bundles/prov_masked_bundle.jsonld",
      "expected": [
        "expected/expected_chip_set.json",
        "expected/expected_redaction_state.json"
      ],
      "tags": ["@regression", "@governance"]
    },
    "prov_restricted": {
      "bundle": "bundles/prov_restricted_bundle.jsonld",
      "expected": [
        "expected/expected_chip_set.json",
        "expected/expected_redaction_state.json"
      ],
      "tags": ["@regression", "@governance"]
    }
  },
  "defaults": {
    "presentation": "reference_only",
    "allow_payload_dump": false
  }
}
~~~

### Minimal PROV‑O fragment shapes (recommended)

A minimal `prov:Activity` fragment (synthetic):

~~~json
{
  "@context": { "prov": "http://www.w3.org/ns/prov#" },
  "@id": "kfm:prov:activity:test_run_001",
  "@type": "prov:Activity",
  "prov:label": "E2E governance run (synthetic)",
  "prov:startedAtTime": "2020-01-01T00:00:00Z"
}
~~~

A minimal `prov:Entity` fragment (synthetic):

~~~json
{
  "@context": { "prov": "http://www.w3.org/ns/prov#" },
  "@id": "kfm:prov:entity:fixture_bundle_001",
  "@type": "prov:Entity",
  "prov:label": "PROV-O fixture bundle (synthetic)",
  "prov:value": "REFERENCE_ONLY"
}
~~~

A minimal relationship fragment (synthetic):

~~~json
{
  "@context": { "prov": "http://www.w3.org/ns/prov#" },
  "@id": "kfm:prov:rel:gen_001",
  "@type": "prov:wasGeneratedBy",
  "prov:entity": "kfm:prov:entity:fixture_bundle_001",
  "prov:activity": "kfm:prov:activity:test_run_001"
}
~~~

Guardrails:
- Keep timestamps fixed and synthetic.
- Keep labels short and non-identifying.
- Prefer `REFERENCE_ONLY` markers over payload content.

---

## 🌐 STAC, DCAT & PROV Alignment

PROV‑O fixtures are **test assets**, not production provenance.

- **DCAT**: PROV fixture bundles may be treated as test distributions (`mediaType: application/ld+json`).
- **STAC**: if represented as a STAC item:
  - `geometry: null`
  - `properties.datetime` set to fixture update time
  - assets: `bundles/*.jsonld`, `fragments/*.jsonld`
- **PROV‑O**:
  - fixture files are `prov:Entity`,
  - E2E test run consuming them is a `prov:Activity`,
  - CI runner is a `prov:Agent`.

---

## 🧱 Architecture

### Recommended usage pattern in governance E2E

Governance E2E specs SHOULD:
1. select bundle ID from `registry.json`,
2. inject the bundle into the test stack (API mock/intercept or local provenance sink),
3. assert:
   - chip presence and categories,
   - correct redaction posture,
   - absence of payload dumps or precision leakage,
4. write artifacts as **summaries only** (counts, chip types, rule IDs).

Avoid:
- hardcoding provenance fragments directly inside specs,
- snapshotting full JSON-LD payloads into test artifacts without redaction,
- allowing debug panes to render full provenance structures to end users.

---

## ⚖ FAIR+CARE & Governance

PROV fixtures exist to uphold non-negotiable constraints:

- **Authority to Control**: provenance must not become a channel for sensitive inference.
- **Responsibility & Ethics**: governance posture must hold even under error states.
- **Collective Benefit**: transparent, safe traceability without harm risk.

If a PROV fixture violates policy:
- remove it immediately,
- invalidate dependent tests until corrected,
- route review to the appropriate working group and FAIR+CARE Council.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-14 | Initial PROV‑O provenance fixtures guide aligned to KFM‑MDP v11.2.6 (synthetic JSON‑LD fragments, reference-only posture, governance-safe E2E support). |

<div align="center">

[🏛️ Governance Charter](../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>


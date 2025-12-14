---
title: "🧾 Kansas Frontier Matrix — Provenance Fixtures: PROV‑O Expected Outputs (E2E) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/governance/fixtures/provenance/prov_o/expected/README.md"

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
intent: "tests-e2e-web-app-regression-governance-fixtures-provenance-prov-o-expected"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-regression-governance-fixtures-provenance-prov-o-expected-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:governance:fixtures:provenance:prov-o:expected:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/governance/fixtures/provenance/prov_o/expected/README.md"
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
  - "tests/e2e/web-app/regression/governance/fixtures/provenance/prov_o/expected/README.md@v11.2.6"
---

<div align="center">

# 🧾 **Provenance Fixtures — PROV‑O Expected Outputs (E2E) (v11 LTS)**
`tests/e2e/web-app/regression/governance/fixtures/provenance/prov_o/expected/README.md`

**Purpose**  
Define the **canonical “expected outputs” fixtures** for PROV‑O provenance rendering in governance E2E regression suites.  
These files represent the **safe, reference‑only UI expectations** (chips, badges, redaction posture, IDs/hashes) that must hold for public, masked, and restricted scenarios.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Provenance-PROV--O-informational" />
<img src="https://img.shields.io/badge/Surface-Governance%20E2E-blueviolet" />
<img src="https://img.shields.io/badge/Policy-Reference--Only-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ PROV‑O Fixtures](../README.md) ·
[⬅️ Provenance Fixtures](../../README.md) ·
[⬅️ Governance Fixtures](../../../README.md) ·
[🧭 E2E Guide](../../../../../../../README.md)

</div>

---

## 📘 Overview

This folder contains **expected outcome fixtures** used by tests to assert that PROV‑O provenance:

- renders as **reference-only** UI (IDs/hashes/labels, not payload dumps),
- respects governance posture:
  - **public** (no masking required),
  - **masked** (generalized / redacted precision),
  - **restricted** (blocked / withheld UX),
- never becomes a **leak channel** (no coordinates, no geometry, no bboxes),
- remains deterministic across:
  - browsers,
  - CI runners,
  - scenario bundles.

These fixtures SHOULD be treated as **test contracts**: if UI changes legitimately, update expected files; if UI changes accidentally, expected files catch regressions.

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
                            ├── 📄 README.md                           — PROV‑O fixtures overview
                            ├── 🧾 registry.json                        — Scenario/bundle registry
                            │
                            ├── 📁 bundles/                             — JSON‑LD bundles consumed by the app/tests
                            │   ├── 📄 README.md
                            │   └── 🧾 prov_*_bundle.jsonld
                            │
                            └── 📁 expected/
                                ├── 📄 README.md                         — This guide (expected outputs contract)
                                ├── 🧾 expected_public.json               — Expected chips + posture (public)
                                ├── 🧾 expected_masked.json               — Expected chips + posture (masked)
                                ├── 🧾 expected_restricted.json           — Expected chips + posture (restricted)
                                └── 🧾 expected_schema.json               — Optional: fixture schema (if enforced)
~~~

Notes:
- The filenames above are the **canonical target layout**.
- If your runner prefers `.yaml`, keep the same structure and semantics.

---

## 🧭 Context

### What “expected” means in this folder

An expected fixture is a **high-signal assertion map** for provenance UX. It SHOULD describe:

- what chips/badges must appear (by type and count),
- what reference anchors must exist (IDs and hash placeholders),
- what the redaction posture must be (`public | masked | restricted`),
- what MUST NOT appear (payload dumps, coordinate-like patterns).

Expected fixtures MUST NOT contain:
- any raw provenance bundle payloads (those belong in `../bundles/`),
- any geometry/coordinates/bboxes (even “fake” ones),
- any production references (URLs, dataset IDs, org/person IDs).

### “Reference-only” contract (non-negotiable)

Expected fixtures should enforce:
- IDs are shown, but not expanded into full JSON‑LD,
- hashes may appear as placeholders (`<sha256>`) or safe synthetic tokens,
- restricted scenarios show “withheld/blocked” states without revealing details.

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Load scenario bundle (bundles/*.jsonld)"] --> B["Render provenance surface"]
  B --> C["Extract UI signals (chips/badges/labels)"]
  C --> D["Load expected fixture (expected/*.json)"]
  D --> E["Compare: counts + posture + anchors"]
  E --> F["Fail if: missing signals or unsafe exposure"]
~~~

Interpretation:
- Expected fixtures act as the stable contract between provenance bundles and governed UI behavior.

---

## 🧠 Story Node & Focus Mode Integration

Provenance UI is often shared across:
- Story Node v3 evidence chips,
- Focus Mode v3 provenance panels,
- Governance overlays and drilldowns.

Expected fixtures in this folder SHOULD remain compatible with shared UI components by asserting:
- common chip types (dataset reference, run reference, model/experiment reference where applicable),
- shared redaction posture rules,
- shared “no payload dump” behavior.

When a scenario is entered through Story Node routes, expected fixtures SHOULD still hold:
- same posture,
- same “no sensitive precision” invariants,
- same reference-only behavior.

---

## 🧪 Validation & CI/CD

Expected fixtures MUST pass:
- ✅ JSON parse validation
- ✅ secret scan
- ✅ PII scan (best-effort)
- ✅ governance leak checks (no coordinate-like patterns)
- ✅ schema validation (if `expected_schema.json` is enforced)

Recommended test behavior:
- treat missing required fields as a test failure,
- treat extra fields as tolerated only if explicitly allowed by schema,
- treat any “precision-like token” match as a **block**.

---

## 📦 Data & Metadata

### Recommended expected fixture shape (minimal, high-signal)

~~~json
{
  "schema_version": "v11.2.6",
  "scenario_id": "prov_masked",
  "posture": "masked",
  "presentation": "reference_only",
  "expect": {
    "chips": {
      "dataset_refs_min": 1,
      "run_refs_min": 1,
      "agent_refs_min": 1
    },
    "badges": {
      "care_label_required": true,
      "sovereignty_indicator_required": true
    },
    "anchors": {
      "allowed_hash_placeholders": ["<sha256>"],
      "required_id_prefixes": ["kfm:prov:"]
    },
    "must_not": {
      "payload_dump_visible": true,
      "coordinates_like_visible": false,
      "geometry_like_visible": false,
      "bbox_like_visible": false
    }
  }
}
~~~

Guidelines:
- Keep `expect` compact and deterministic.
- Prefer “min counts” over brittle exact counts unless a UI contract demands exactness.
- Use placeholders rather than embedding real-looking values.

### Optional schema for expected fixtures

If enforced, `expected_schema.json` SHOULD:
- require `schema_version`, `scenario_id`, `posture`, `presentation`, `expect`,
- prohibit additionalProperties unless explicitly needed,
- forbid high-risk keys (geometry/coordinates/bbox/wkt).

---

## 🌐 STAC, DCAT & PROV Alignment

Expected fixtures are **test artifacts**, not real provenance exports:

- **DCAT**: expected fixtures can be treated as test distributions (`mediaType: application/json`).
- **STAC**: if indexed, use non-spatial representation:
  - `geometry: null`
  - `properties.datetime` = `last_updated`
- **PROV‑O**: these files do not represent provenance themselves; they represent **UI expectations** for provenance presentation.

---

## 🧱 Architecture

### How expected fixtures should be used (recommended pattern)

Governance E2E specs SHOULD:
1. pick a `scenario_id`,
2. render the provenance UI surface,
3. extract **signals** (chip labels/types/counts; badges; posture),
4. load `expected/<scenario>.json`,
5. compare:
   - required minimums,
   - required posture,
   - must-not exposure checks,
6. write a small, redacted assertion report to artifacts.

Avoid:
- snapshotting full UI HTML,
- snapshotting full JSON‑LD expansions,
- relying on pixel diffs for provenance correctness.

---

## ⚖ FAIR+CARE & Governance

Expected fixtures enforce governance invariants:

- **Authority to Control**: reference-only behavior prevents provenance from becoming a precision leak channel.
- **Responsibility & Ethics**: restricted scenarios must remain restricted across navigation and refresh.
- **Collective Benefit**: provenance remains transparent (traceability) without enabling harm.

If an expected fixture needs to change:
- treat it like a governance contract update,
- update tests and fixtures together,
- ensure leak checks remain strict (do not “allowlist around” a real leak).

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-14 | Initial PROV‑O expected outputs guide aligned to KFM‑MDP v11.2.6 (reference-only UX contract, deterministic assertions, leak-safe invariants). |

<div align="center">

[🏛️ Governance Charter](../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>


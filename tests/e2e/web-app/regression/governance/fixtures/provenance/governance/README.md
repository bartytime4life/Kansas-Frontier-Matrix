---
title: "🏛️ Kansas Frontier Matrix — Governance Provenance Fixtures: Governance Fragments (E2E) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/governance/fixtures/provenance/governance/README.md"

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
intent: "tests-e2e-web-app-regression-governance-fixtures-provenance-governance"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-regression-governance-fixtures-provenance-governance-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:governance:fixtures:provenance:governance:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/governance/fixtures/provenance/governance/README.md"
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
  - "tests/e2e/web-app/regression/governance/fixtures/provenance/governance/README.md@v11.2.6"
---

<div align="center">

# 🏛️ **Governance Provenance Fixtures — Governance Fragments (E2E) (v11 LTS)**
`tests/e2e/web-app/regression/governance/fixtures/provenance/governance/README.md`

**Purpose**  
Define the **canonical governance fragment fixtures** used by E2E regression suites to validate **CARE tiers**, **sovereignty flags**, **restriction states**, and **redaction cues** in UI surfaces—using **synthetic, deterministic, sovereignty-safe** content (IDs/hashes only; no payload dumps; no precision leakage).

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Surface-Governance%20E2E-blueviolet" />
<img src="https://img.shields.io/badge/Policy-CARE%20%2B%20Sovereignty-orange" />
<img src="https://img.shields.io/badge/Rule-No%20Precision%20Leak-red" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Provenance Fixtures](../README.md) ·
[⬅️ Governance Fixtures](../../README.md) ·
[⬅️ Governance Regression](../../../README.md) ·
[🧭 E2E Guide](../../../../../../README.md)

</div>

---

## 📘 Overview

This folder contains **governance-only provenance fragments**: small synthetic JSON objects that represent the governance posture for a scenario.

These fixtures exist so E2E suites can assert non-negotiable invariants:

- ✅ CARE tier labels are present and correct (Tier A/B/C semantics simulated).
- ✅ Sovereignty indicators are visible when required (and absent when not required).
- ✅ Restricted states trigger safe UX behavior (blocked, redacted, masked).
- ✅ UI evidence surfaces expose **references** (IDs/hashes) without exposing **payloads**.
- ✅ No precision leakage occurs (no coordinate-like pairs, no geometry/bbox dumps).

These fixtures MUST be:
- **Synthetic** (non-identifying; not derived from real people, real sites, or real restricted knowledge).
- **Deterministic** (stable IDs, stable ordering, stable timestamps only if required).
- **Safe by construction** (placeholders and policy-safe strings; no lat/long-like tokens; no secrets).

These fixtures MUST NOT:
- include real individuals, real addresses, or realistic sensitive narratives,
- include raw coordinates, bboxes, GeoJSON, WKT, or any geometry-like payload,
- include secrets, tokens, or credentials,
- include any content that could be interpreted as a “real location” or “real restricted site.”

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
                        └── 📁 governance/
                            ├── 📄 README.md                     — This guide
                            │
                            ├── 🧾 gov_public.json                — Public posture (no restrictions; sovereignty flag off)
                            ├── 🧾 gov_masked.json                — Mask-required posture (generalized/redacted UX)
                            ├── 🧾 gov_restricted.json            — Restricted posture (blocked/withheld UX)
                            │
                            └── 🧾 gov_schema_hint.json            — Optional “shape hint” (non-authoritative, test-only)
~~~

Notes:
- If additional posture variants are needed, keep them small and name them by intent:
  - `gov_public_*`
  - `gov_masked_*`
  - `gov_restricted_*`

---

## 🧭 Context

### What “governance fragments” represent

A governance fragment is the **minimum synthetic state** needed to drive UI gating and assertions. It typically includes:

- CARE classification (simulated tier label and rationale codes)
- Sovereignty flag(s) (boolean indicators and required masking behavior)
- Restricted state flags (blocked/redacted/masked)
- UI-level copy keys (banner IDs, not full narratives)
- Evidence rules (IDs/hashes required; payload dumps forbidden)

### Canonical posture meanings (E2E semantics)

- **Public**
  - UI is allowed to render normal content.
  - Governance badges may be present, but sovereignty masking is not required.

- **Masked**
  - UI must redact or generalize sensitive-like fields (simulation).
  - Any “location-like” representation must stay generalized.
  - Evidence surfaces must remain ID/hash-only.

- **Restricted**
  - UI must block or withhold protected content (simulation).
  - The user-visible state must clearly indicate a restriction without leaking details.

### Determinism rules

Fixtures SHOULD:
- use stable `posture_id` values (e.g., `gov_public`)
- keep arrays sorted and keys stable
- avoid “now” timestamps unless required (prefer fixed ISO timestamp strings)

Fixtures MUST NOT:
- include “random-ish” UUIDs unless pinned and stable
- embed content that looks like real coordinates (including high-precision decimals)

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Select scenario_id"] --> B["Load governance posture fragment"]
  B --> C["Render governance badges and banners"]
  C --> D["Apply masking or restriction UX"]
  D --> E["Assert invariants (no leaks, correct tier/flags)"]
  E --> F["Write safe artifacts and telemetry summary"]
~~~

Interpretation:
- Governance fragments are the posture input that must deterministically drive the correct UI gating behavior.

---

## 🧠 Story Node & Focus Mode Integration

Governance fragments may be used to validate governance behavior in:
- Story Node v3 routes (evidence chips, redaction banners, restricted overlays)
- Focus Mode v3 panels (context/timeline/map; provenance overlays; restricted handling)

Minimum integration invariants:
- Governance posture remains consistent across navigation.
- Restricted content stays restricted across panel switching.
- Evidence surfaces remain **reference-only** (IDs/hashes), not full payload.

---

## 🧪 Validation & CI/CD

Governance fragment fixtures MUST pass:
- ✅ JSON parse validation
- ✅ secret scan
- ✅ PII scan (best-effort)
- ✅ leak checks (no coordinate-like patterns; no geometry/bbox keys unless redacted)

Recommended fixture lint rules:
- forbid keys: `coordinates`, `geometry`, `bbox` unless explicitly `null` or `"REDACTED"`
- forbid patterns that resemble lat/long pairs with high precision
- enforce deterministic formatting and sorted keys (formatter in CI)

---

## 📦 Data & Metadata

### Recommended minimal shape (canonical)

~~~json
{
  "schema_version": "v11.2.6",
  "posture_id": "gov_masked",
  "care": {
    "tier": "Tier B",
    "label": "Public · Low-Risk",
    "codes": ["CARE_SIM_B01"],
    "notes_ref": "GOV_NOTES_REDACTED"
  },
  "sovereignty": {
    "flag": true,
    "masking_required": true,
    "masking_method": "H3_GENERALIZED_REDACTED"
  },
  "restriction": {
    "state": "masked",
    "reason_code": "GOV_REASON_MASK_REQUIRED",
    "ui_banner_id": "BANNER_MASKED_REDACTED"
  },
  "evidence": {
    "require_ids": true,
    "allow_payload_dump": false,
    "required_refs": {
      "dataset_ids": ["DATASET_ID_REDACTED"],
      "experiment_ids": ["EXPERIMENT_ID_REDACTED"],
      "model_card_ids": ["MODEL_CARD_ID_REDACTED"]
    },
    "hashes": {
      "bundle_sha256": "HASH_REDACTED"
    }
  }
}
~~~

### Redaction policy for fixtures (hard rule)

Fixtures MUST:
- use placeholders for any risky string fields,
- keep any “reference lists” limited to synthetic IDs,
- avoid embedding any content that could be mistaken as real.

---

## 🌐 STAC, DCAT & PROV Alignment

These fixtures are test artifacts (not production datasets):

- **DCAT**: governance fragments can be treated as `dcat:Distribution` artifacts (`mediaType: application/json`).
- **STAC**: if represented as STAC items, use:
  - `geometry: null`
  - `properties.datetime` as a test timestamp
  - assets: fragment files only
- **PROV‑O**:
  - fragment files are `prov:Entity`
  - E2E runs are `prov:Activity`
  - CI runner is `prov:Agent`

---

## 🧱 Architecture

### Recommended consumption pattern (E2E)

E2E suites SHOULD:
1. select a `scenario_id`,
2. load the scenario bundle,
3. load the relevant governance posture fragment from this folder,
4. drive navigation and interactions,
5. assert posture-specific invariants:
   - tier label visible
   - sovereignty flag behavior correct
   - restricted/masked behavior correct
   - no payload dumps
   - no precision leakage

This keeps governance logic:
- explicit,
- reusable across suites,
- auditable from fixture diffs.

---

## ⚖ FAIR+CARE & Governance

Governance fragments exist to enforce:
- **Authority to Control**: sovereignty flags and restriction states must never be bypassed.
- **Responsibility & Ethics**: blocked/masked states must remain safe and non-leaky.
- **Collective Benefit**: public-facing surfaces remain respectful and protective.

If a governance fixture violates policy:
- remove it immediately,
- block merges until corrected,
- route review to the relevant working group and FAIR+CARE Council.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-14 | Initial governance posture fragment fixtures guide aligned to KFM‑MDP v11.2.6 (deterministic, sovereignty-safe, reference-only evidence). |

<div align="center">

[🏛️ Governance Charter](../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>


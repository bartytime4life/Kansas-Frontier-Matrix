---
title: "🧭 Kansas Frontier Matrix — Provenance Fixtures: UI & Provenance Mappings (E2E) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/governance/fixtures/provenance/mappings/README.md"

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
intent: "tests-e2e-web-app-regression-governance-fixtures-provenance-mappings"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-regression-governance-fixtures-provenance-mappings-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:governance:fixtures:provenance:mappings:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/governance/fixtures/provenance/mappings/README.md"
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
  - "tests/e2e/web-app/regression/governance/fixtures/provenance/mappings/README.md@v11.2.6"
---

<div align="center">

# 🧭 **Provenance Fixtures — UI & Provenance Mappings (E2E) (v11 LTS)**
`tests/e2e/web-app/regression/governance/fixtures/provenance/mappings/README.md`

**Purpose**  
Define the **canonical mapping fixtures** used by governance E2E regression suites to translate **provenance references** into **stable UI expectations** (labels, badges, chip types, redaction behavior) without exposing payload dumps, sensitive precision, or identifying data.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Surface-Governance%20E2E-blueviolet" />
<img src="https://img.shields.io/badge/Layer-Provenance%20Mappings-informational" />
<img src="https://img.shields.io/badge/Policy-Reference--Only-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Provenance Fixtures](../README.md) ·
[⬅️ Governance Fixtures](../../README.md) ·
[⬅️ Governance Regression](../../../README.md) ·
[🧭 E2E Guide](../../../../../../README.md)

</div>

---

## 📘 Overview

This folder contains **synthetic mapping fixtures** that define how the E2E test harness should interpret provenance-related references.

Mappings exist so tests can assert UI behavior in a **stable, deterministic, governance-safe** way, even when upstream payload shapes evolve.

Mappings here SHOULD enable tests to:
- ✅ validate that evidence/provenance chips render with correct **type + label + icon category**,
- ✅ validate that governance indicators (CARE tier, sovereignty flags, restricted states) map to the correct **badges/banners**,
- ✅ validate that the UI surfaces **references only** (IDs/hashes), not raw payload dumps,
- ✅ validate redaction behavior using stable “display rules” rather than fragile string matching.

Mappings here MUST be:
- **Synthetic** (non-identifying; no real dataset IDs required; placeholders are expected).
- **Deterministic** (stable keys; stable ordering; minimal ambiguity).
- **Safe by construction** (no coordinates, no geometry, no plausible sensitive reconstruction).

Mappings here MUST NOT:
- embed full provenance payloads (OpenLineage events, PROV documents, etc.),
- include “example” coordinate-like values (even fake ones that look real),
- include secrets, tokens, or credentials.

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
                        └── 📁 mappings/
                            ├── 📄 README.md                          — This guide
                            │
                            ├── 🧾 mapping_registry.json               — Canonical index of mapping files + schema_version
                            │
                            ├── 🧾 chip_type_map.json                  — Ref type → UI chip type (dataset/experiment/model_card/etc.)
                            ├── 🧾 badge_map.json                      — Governance posture → UI badges/banners (Tier/sovereignty/restricted)
                            ├── 🧾 redaction_map.json                  — Restricted/masked states → UI redaction behaviors and copy keys
                            │
                            ├── 🧾 source_alias_map.json               — Stable aliases for synthetic sources (IDs/hashes → display labels)
                            └── 🧾 ui_selector_map.json                — Optional: stable selector aliases for provenance surfaces
~~~

Notes:
- Filenames above are a **canonical target layout**. If your repo uses different names, preserve the same intent:
  - registry (index)
  - chip typing
  - badge/banner mapping
  - redaction mapping
  - aliasing (synthetic reference labels)

---

## 🧭 Context

### What these mappings are (and are not)

Mappings are **test-time interpretive tables**. They answer questions like:
- “If the UI shows a `MODEL_CARD_ID_REDACTED`, what chip category should render?”
- “If a scenario is `masked`, which badge appears and which UI areas must be redacted?”
- “Which selector aliases are valid targets for provenance assertions?”

Mappings are NOT:
- the canonical governance policy (policy lives in the standards),
- production configuration for runtime behavior,
- a place to store real provenance artifacts.

### Stability contract

Mappings SHOULD change only when:
- UI taxonomy changes (chip types, badges, banners),
- governance UI rules change (redaction presentation / restricted posture behavior),
- provenance surfaces are reorganized (selector names change).

When mappings change, update the corresponding expected UI snapshots and ensure the diffs remain auditable.

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Load scenario bundle"] --> B["Load mapping_registry.json"]
  B --> C["Resolve chip types + labels via maps"]
  C --> D["Apply governance posture maps (badges/redaction)"]
  D --> E["Assert UI (selectors + expected badges/chips)"]
  E --> F["Write safe artifacts (IDs/hashes only)"]
~~~

Interpretation:
- Mappings convert reference-only provenance inputs into stable UI expectations without requiring payload dumps.

---

## 🧠 Story Node & Focus Mode Integration

Mappings may be reused across governed narrative surfaces:

- **Story Node v3**: evidence chips, provenance references, redaction banners.
- **Focus Mode v3**: provenance overlays, “evidence” panels, restricted/withheld states.

Minimum invariants supported by mappings:
- chip categories remain consistent across routes and panel switching,
- governance posture drives consistent badge/banner presentation,
- restricted/masked states remain reference-only and non-leaky.

---

## 🧪 Validation & CI/CD

Mapping fixtures MUST pass:
- ✅ JSON parse validation
- ✅ secret scan
- ✅ PII scan (best-effort)
- ✅ leak checks (no coordinate-like patterns; no geometry/bbox payloads)

Recommended mapping lint rules:
- enforce `schema_version` on every mapping file,
- require deterministic ordering (sorted keys),
- forbid high-risk keys (e.g., `coordinates`, `geometry`, `bbox`) unless explicitly `"REDACTED"` or `null`,
- require explicit “unknown/default” handling (so tests don’t fail unpredictably).

---

## 📦 Data & Metadata

### Mapping registry (recommended minimal shape)

~~~json
{
  "schema_version": "v11.2.6",
  "maps": {
    "chip_type_map": "chip_type_map.json",
    "badge_map": "badge_map.json",
    "redaction_map": "redaction_map.json",
    "source_alias_map": "source_alias_map.json",
    "ui_selector_map": "ui_selector_map.json"
  },
  "defaults": {
    "unknown_chip_type": "reference",
    "unknown_badge": "badge_unknown",
    "unknown_redaction": "redaction_safe_default"
  }
}
~~~

### Chip type mapping (example)

~~~json
{
  "schema_version": "v11.2.6",
  "ref_types": {
    "dataset_id": "chip_dataset",
    "experiment_id": "chip_experiment",
    "model_card_id": "chip_model_card",
    "sop_id": "chip_sop",
    "hash_sha256": "chip_hash"
  }
}
~~~

### Badge mapping (example)

~~~json
{
  "schema_version": "v11.2.6",
  "posture_to_badges": {
    "public": ["badge_care_public"],
    "masked": ["badge_care_masked", "badge_sovereignty_flag"],
    "restricted": ["badge_care_restricted", "badge_sovereignty_flag", "badge_withheld"]
  }
}
~~~

### Redaction mapping (example)

~~~json
{
  "schema_version": "v11.2.6",
  "redaction_rules": {
    "masked": {
      "ui_banner_id": "BANNER_MASKED_REDACTED",
      "allow_payload_dump": false,
      "raw_precision_visible": false
    },
    "restricted": {
      "ui_banner_id": "BANNER_RESTRICTED_REDACTED",
      "allow_payload_dump": false,
      "raw_precision_visible": false
    }
  }
}
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

These mappings are **test fixtures**, not production provenance.

- **DCAT**: mapping files may be treated as documentation/test distributions (`mediaType: application/json`).
- **STAC**: if mapped to STAC items, use:
  - `geometry: null`
  - `properties.datetime` = fixture update timestamp
  - assets: mapping JSON files
- **PROV‑O**:
  - mapping files are `prov:Entity`,
  - E2E runs consuming them are `prov:Activity`,
  - CI runner + maintainers are `prov:Agent`.

---

## 🧱 Architecture

### Recommended usage pattern (E2E)

Governance E2E specs SHOULD:
1. load the mapping registry,
2. resolve mapping tables once per run (memoized),
3. normalize UI observations into reference tokens (IDs/hashes),
4. compare normalized observations to expected outputs using mapping rules.

This prevents:
- fragile tests that depend on UI micro-copy,
- duplicated “magic strings” in specs,
- accidental leakage from storing raw payloads in snapshots.

---

## ⚖ FAIR+CARE & Governance

Mappings exist to protect governed surfaces by making it easy to:
- assert reference-only behavior,
- enforce redaction/restriction UX deterministically,
- detect drift before it reaches production.

Non-negotiable constraints:
- never weaken sovereignty protections by “mapping around” restrictions,
- never add allowlist-like behavior here to bypass leak checks,
- never embed realistic or identifying content in mapping examples.

If a mapping change reduces governance coverage:
- treat as a governance regression,
- route to the relevant working group and FAIR+CARE Council for review.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-14 | Initial provenance mapping fixtures guide aligned to KFM‑MDP v11.2.6 (reference-only, deterministic UI mapping, governance-safe). |

<div align="center">

[🏛️ Governance Charter](../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>


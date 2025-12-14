---
title: "✅ Kansas Frontier Matrix — Governance Fixture Allowlists (E2E) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/governance/fixtures/allowlists/README.md"

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
intent: "tests-e2e-web-app-regression-governance-fixtures-allowlists"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-regression-governance-fixtures-allowlists-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:governance:fixtures:allowlists:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/governance/fixtures/allowlists/README.md"
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
  - "tests/e2e/web-app/regression/governance/fixtures/allowlists/README.md@v11.2.6"
---

<div align="center">

# ✅ **Governance Fixture Allowlists (E2E) (v11 LTS)**
`tests/e2e/web-app/regression/governance/fixtures/allowlists/README.md`

**Purpose**  
Define the **canonical allowlist fixtures** used by governance regression E2E suites to:
- remove known-safe placeholders from leak scans,
- keep redaction tokens stable across fixtures and assertions,
- prevent “convenient bypasses” that weaken governance guarantees.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Category-Allowlist%20Fixtures-blueviolet" />
<img src="https://img.shields.io/badge/Policy-Placeholder%20Only-orange" />
<img src="https://img.shields.io/badge/Rule-No%20Precision%20Bypass-red" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Governance Fixtures](../README.md) ·
[🕵️ Leak Checks](../../utils/leak_checks/README.md) ·
[🧭 E2E Guide](../../../../../README.md)

</div>

---

## 📘 Overview

Allowlists in governance E2E exist for **one reason**: to keep leak checks and UI assertions **signal-rich** without flagging known-safe redaction tokens.

These allowlists:

- ✅ recognize **explicit placeholders** (e.g., `COORDINATE_REDACTED`) as safe,
- ✅ allow stable **masking tokens** (e.g., `H3_CELL_REDACTED`) to pass,
- ✅ prevent tests from failing due to intentionally redacted strings,
- ❌ do not permit bypassing governance rules with “realistic-looking” values.

**Non-goals**
- Allowlists are not a “make the scanner quiet” mechanism.
- Allowlists are not allowed to contain any realistic coordinate/bbox/geometry examples.
- Allowlists do not change application behavior; they only shape how test utilities interpret outputs.

---

## 🗂️ Directory Layout

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 regression/
            └── 📁 governance/
                └── 📁 fixtures/
                    └── 📁 allowlists/
                        ├── 📄 README.md                         — This guide (rules + safety constraints)
                        │
                        ├── 🧾 safe_placeholders.json             — Canonical placeholder tokens (recommended)
                        ├── 🧾 leak_scan_allowlist.json            — Allowlists consumed by leak-check utilities
                        └── 🧾 allowlist_manifest.json             — Optional: checksums + schema version
~~~

Notes:
- Filenames above represent the **canonical target layout**.
- If your implementation uses different filenames, keep the same intent:
  - placeholders are explicit,
  - allowlists are minimal,
  - manifest is optional but recommended for checksum tracking.

---

## 🧭 Context

### What is safe to allowlist

Allowed allowlist entries MUST be **explicit placeholders**, such as:

- `COORDINATE_REDACTED`
- `BBOX_REDACTED`
- `GEOMETRY_REDACTED`
- `H3_CELL_REDACTED`
- `PAYLOAD_REDACTED`
- `HASH_SHA256_REDACTED`

Allowed allowlist entries MAY include stable **UI-safe tokens**, such as:

- `RESTRICTED_STATE_BLOCKED`
- `MASKED_STATE_GENERALIZED`
- `CARE_TIER_BADGE_VISIBLE`

### What is never safe to allowlist

Never allowlist:

- numeric-looking coordinate pairs (even “fake”),
- decimal-heavy strings,
- bbox-like sequences,
- any raw geometry fragments (`"coordinates"`, WKT-like strings),
- any token that could plausibly be used to reconstruct sensitive precision.

**Rule of thumb**  
If a human could mistake it for a real location or real boundary, it does not belong in an allowlist.

### Relationship to leak checks

Leak checks typically apply allowlists **before** running block rules:

1. Collect scan targets (UI text, console, response summaries)
2. Remove known placeholders via allowlist
3. Run block rules
4. Report by rule ID (without dumping raw content)

This keeps leak checks strict while preventing placeholder noise.

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Collect scan targets"] --> B["Apply allowlist (placeholders only)"]
  B --> C["Run block rules (precision and geometry)"]
  C --> D["Generate redacted report"]
  D --> E["Fail CI on severity block"]
~~~

Interpretation:
- Allowlists reduce false positives from intentional redaction, without weakening precision-leak enforcement.

---

## 🧪 Validation & CI/CD

Allowlist fixtures MUST pass:

- ✅ parse validation (JSON)
- ✅ secret scan
- ✅ PII scan (best-effort)
- ✅ governance fixture lint rules

Recommended lint rules for allowlists:

- forbid numeric-heavy entries,
- forbid entries containing commas or whitespace sequences that resemble pairs,
- forbid keys like `"lat"`, `"lon"`, `"lng"`, `"bbox"`, `"coordinates"` unless value is an explicit placeholder token,
- require a `schema_version` and stable ordering if using object maps.

**Change control**
- allowlist changes are governance posture changes,
- review them like code (PR required, CI required, audit trail required).

---

## 📦 Data & Metadata

### Canonical placeholder file (recommended shape)

~~~json
{
  "schema_version": "v11.2.6",
  "placeholders": [
    "COORDINATE_REDACTED",
    "BBOX_REDACTED",
    "GEOMETRY_REDACTED",
    "H3_CELL_REDACTED",
    "PAYLOAD_REDACTED",
    "HASH_SHA256_REDACTED"
  ],
  "notes": "Placeholders only. No realistic examples."
}
~~~

### Leak scan allowlist file (recommended shape)

Use a structure that supports multiple target types without expanding scope.

~~~json
{
  "schema_version": "v11.2.6",
  "targets": {
    "ui_text": ["COORDINATE_REDACTED", "BBOX_REDACTED", "GEOMETRY_REDACTED"],
    "console": ["PAYLOAD_REDACTED"],
    "network_summary": ["HASH_SHA256_REDACTED", "H3_CELL_REDACTED"]
  }
}
~~~

### Manifest (optional but recommended)

~~~json
{
  "schema_version": "v11.2.6",
  "files": [
    { "path": "safe_placeholders.json", "sha256": "<sha256>" },
    { "path": "leak_scan_allowlist.json", "sha256": "<sha256>" }
  ]
}
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

Allowlists are test fixtures, not real datasets.

- **DCAT**: treat allowlists as test distributions (`mediaType: application/json`).
- **STAC**: if represented, use `geometry: null` and attach JSON assets.
- **PROV-O**:
  - allowlist files are `prov:Entity`,
  - governance E2E runs are `prov:Activity`,
  - CI is a `prov:Agent`.

All representations must remain synthetic and safe to publish.

---

## ⚖ FAIR+CARE & Governance

Allowlists must uphold the strictest invariants:

- **Authority to Control**: never permit anything that looks like precision leakage.
- **Responsibility**: avoid “testing shortcuts” that weaken enforcement.
- **Ethics**: keep fixtures minimal, non-identifying, and non-reconstructible.
- **Collective Benefit**: ensure governance safety is consistently testable across environments.

If an allowlist entry is found to be unsafe:
- remove it immediately,
- rotate any dependent fixtures to placeholders,
- re-run governance suites and publish an audit note per repo policy.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-14 | Initial governance allowlists guide aligned to KFM‑MDP v11.2.6 (placeholder-only, strict change control, leak-check integration). |

<div align="center">

[🏛️ Governance Charter](../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>


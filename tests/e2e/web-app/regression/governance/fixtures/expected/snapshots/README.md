---
title: "📸 Kansas Frontier Matrix — Governance Expected Snapshots (E2E Fixtures) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/governance/fixtures/expected/snapshots/README.md"

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
intent: "tests-e2e-web-app-regression-governance-fixtures-expected-snapshots"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-regression-governance-fixtures-expected-snapshots-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:governance:fixtures:expected:snapshots:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/governance/fixtures/expected/snapshots/README.md"
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
  - "tests/e2e/web-app/regression/governance/fixtures/expected/snapshots/README.md@v11.2.6"
---

<div align="center">

# 📸 **Governance Expected Snapshots (E2E Fixtures) (v11 LTS)**
`tests/e2e/web-app/regression/governance/fixtures/expected/snapshots/README.md`

**Purpose**  
Define the **canonical “expected snapshot” baselines** used by governance E2E regression suites.  
Snapshots in this folder represent **sanitized, policy-safe, deterministic** UI/output fragments used to detect regressions **without** embedding payload dumps or sensitive precision.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Fixtures-Expected%20Snapshots-blueviolet" />
<img src="https://img.shields.io/badge/Governance-FAIR%2BCARE-orange" />
<img src="https://img.shields.io/badge/Policy-No%20Sensitive%20Precision-red" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Expected Baselines](../README.md) ·
[📌 Expected Cases](../cases/README.md) ·
[⬅️ Governance Fixtures](../../README.md) ·
[🧭 E2E Guide](../../../../../../README.md)

</div>

---

## 📘 Overview

This folder contains **expected snapshot baselines** for governance regression scenarios.

In KFM E2E governance testing, a “snapshot” means:
- a **small**, **sanitized** representation of something user-visible (or E2E-visible) that must remain stable,
- captured in a **diff-friendly** format (text or minimal JSON),
- safe to publish (no secrets, no PII, no sensitive precision, no full payload dumps).

Snapshots exist to catch regressions like:
- restricted-state UI rendering “too much” detail,
- governance badges or banners disappearing,
- “Details/JSON” panels accidentally exposing forbidden fields,
- tooltip text or labels leaking precision-like content.

**Relationship to “Expected Cases”**
- **Expected Cases** (`../cases/`) define *high-signal boolean/count invariants* (flags, tiers, minimum counts).
- **Expected Snapshots** (this folder) define *small stable fragments* where a structured boolean is not enough (e.g., a redaction banner block, a provenance label list, a sanitized debug excerpt).

---

## 🗂️ Directory Layout

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 regression/
            └── 📁 governance/
                └── 📁 fixtures/
                    └── 📁 expected/
                        └── 📁 snapshots/
                            ├── 📄 README.md                          — This guide
                            │
                            ├── 🧾 snapshot_manifest.json              — Scenario ID → snapshot file map (+ hashes)
                            │
                            ├── 📁 gov_public/                          — Public-mode snapshots (no masking required)
                            │   ├── 📄 banner.snap.txt                  — Sanitized banner block snapshot
                            │   ├── 📄 provenance_list.snap.txt         — ID-only evidence/provenance list snapshot
                            │   └── 🧾 details_panel.snap.json          — Minimal redacted “details” snapshot (no dumps)
                            │
                            ├── 📁 gov_masked/                          — Masking-required snapshots (no precision visible)
                            │   ├── 📄 banner.snap.txt
                            │   ├── 📄 map_tooltip.snap.txt             — Tooltip text with redaction tokens only
                            │   └── 🧾 details_panel.snap.json
                            │
                            └── 📁 gov_restricted/                      — Restricted/blocked state snapshots
                                ├── 📄 banner.snap.txt
                                └── 📄 blocked_state.snap.txt
~~~

Notes:
- Filenames above are a **recommended** convention for consistent discovery.
- Keep snapshots **small** and **scenario-scoped** (avoid one giant snapshot per suite).

---

## 🧭 Context

### What belongs in a governance snapshot

Governance snapshots SHOULD capture:
- a redaction banner / restriction banner block (text-only),
- a short list of provenance chip labels (IDs/hashes only),
- a sanitized “details” panel excerpt that demonstrates redaction logic,
- a blocked-state UI message (minimal text).

Governance snapshots SHOULD NOT capture:
- raw API responses,
- full graph entities,
- long narratives,
- any coordinate-like values, bboxes, GeoJSON fragments, or geometry dumps.

### Redaction token policy (safe placeholders)

Snapshots MUST use **explicit redaction placeholders**, such as:
- `KFM_REDACTED`
- `H3_CELL_REDACTED`
- `BBOX_REDACTED`
- `COORDINATE_REDACTED`
- `HASH_REDACTED`

Snapshots MUST NOT contain:
- realistic coordinates,
- realistic bboxes,
- geometry arrays,
- “almost-real” site descriptions that could enable inference.

### Normalization rules (determinism)

Before committing snapshot updates:
- normalize whitespace (no trailing spaces),
- normalize ordering (sorted lists; stable ordering),
- normalize timestamps (fixed or removed unless explicitly required),
- normalize IDs (stable synthetic IDs only).

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Load scenario fixtures"] --> B["Render governed UI state"]
  B --> C["Capture candidate snapshot"]
  C --> D["Normalize + redact"]
  D --> E["Compare to expected snapshot baseline"]
  E -->|match| F["Pass"]
  E -->|diff| G["Fail and write safe diff artifact"]
~~~

Interpretation:
- Snapshots are compared only after **normalization + redaction** so diffs remain deterministic and safe.

---

## 🧠 Story Node & Focus Mode Integration

Governance snapshots may be used for:
- Story Node pages where masking/restriction banners appear,
- Focus Mode panels where provenance chip lists and redaction cues appear,
- cross-navigation flows where restricted state must persist.

Minimum invariants for narrative surfaces:
- restriction state persists across route transitions,
- provenance remains **ID-only** (no expansion into raw payload dumps),
- masked scenarios never show precision-like fragments in map tooltips or details panels.

---

## 🧪 Validation & CI/CD

Expected snapshots MUST pass:
- ✅ parse validation (when JSON snapshots exist),
- ✅ secret scan,
- ✅ PII scan (best-effort),
- ✅ leak-safety checks (no coordinate-like patterns; no geometry keys unless null).

Recommended CI behavior:
- snapshot diffs are **merge-blocking** for governance suites unless explicitly reviewed and approved,
- snapshot updates should require:
  - a governance-focused review,
  - a matching expected-case review when applicable,
  - a passing leak-check run.

**Snapshot update policy**
- Do not “auto-accept” governance snapshots in CI.
- Updates must be intentional and reviewed (snapshots change what we treat as acceptable).

---

## 📦 Data & Metadata

### Snapshot manifest (recommended shape)

The manifest binds scenario IDs to snapshot files and enables hashing.

~~~json
{
  "schema_version": "v11.2.6",
  "snapshots": {
    "gov_public": {
      "dir": "gov_public",
      "files": [
        { "path": "gov_public/banner.snap.txt", "sha256": "<sha256>" },
        { "path": "gov_public/provenance_list.snap.txt", "sha256": "<sha256>" },
        { "path": "gov_public/details_panel.snap.json", "sha256": "<sha256>" }
      ]
    },
    "gov_masked": {
      "dir": "gov_masked",
      "files": [
        { "path": "gov_masked/banner.snap.txt", "sha256": "<sha256>" },
        { "path": "gov_masked/map_tooltip.snap.txt", "sha256": "<sha256>" },
        { "path": "gov_masked/details_panel.snap.json", "sha256": "<sha256>" }
      ]
    }
  }
}
~~~

### Text snapshot guidance

Text snapshots SHOULD:
- be short (prefer <200 lines),
- use stable headings if needed,
- include redaction placeholders instead of sensitive fragments.

Example (sanitized):
~~~text
GOVERNANCE_STATE: masked
CARE_TIER: Tier B
SOVEREIGNTY_FLAG: visible
DETAILS_PANEL: KFM_REDACTED
PROVENANCE: [EXPERIMENT_ID_REDACTED, DATASET_ID_REDACTED]
~~~

### JSON snapshot guidance

JSON snapshots MUST:
- avoid raw payload structures,
- avoid geometry and coordinate-bearing keys,
- include only minimal fields needed to assert redaction behavior.

Example (sanitized):
~~~json
{
  "governance_state": "masked",
  "care_tier": "Tier B",
  "sovereignty_flag_visible": true,
  "details_panel": "KFM_REDACTED",
  "raw_coordinates_visible": false
}
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

Expected snapshots are test fixtures (not production datasets):

- **DCAT**: snapshot files may be treated as test artifact distributions (`mediaType: text/plain` or `application/json`).
- **STAC**: if represented as STAC items, use:
  - `geometry: null`
  - `properties.datetime` derived from the run (not embedded in snapshots)
  - assets: snapshot files + manifest
- **PROV-O**:
  - snapshot files are `prov:Entity`,
  - an E2E run is a `prov:Activity`,
  - CI runners/maintainers are `prov:Agent`.

---

## 🧱 Architecture

### Recommended snapshot pipeline

1. **Capture**
   - capture only the minimal UI slice required (banner block, list, small excerpt)
2. **Normalize**
   - stable ordering, stable whitespace, deterministic IDs
3. **Redact**
   - replace any risky fragments with explicit placeholders
4. **Hash**
   - compute sha256 for manifest binding
5. **Compare**
   - diff vs expected baseline (fail fast on mismatch)
6. **Report**
   - write safe diffs (no raw dumps; redacted output only)

### Anti-patterns (avoid)

- storing screenshots as “expected snapshots” (screenshots belong in artifacts, not fixtures),
- snapshotting full HTML/DOM dumps,
- snapshotting full JSON payloads,
- allowing unreviewed snapshot churn in governance suites.

---

## ⚖ FAIR+CARE & Governance

Expected snapshots are governance-critical fixtures:

- **Authority to Control**: snapshots must never enable inference of restricted locations or protected knowledge.
- **Responsibility**: snapshots must remain minimal and reviewable.
- **Ethics**: synthetic text only; avoid harmful framing even in placeholders.
- **Collective Benefit**: consistent guardrails across releases.

If a snapshot baseline is found to include unsafe content:
- remove it immediately,
- invalidate impacted suites until corrected,
- fix the underlying UI/mock behavior (do not “paper over” with a snapshot update).

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-14 | Initial governance expected snapshots guide aligned to KFM‑MDP v11.2.6 (sanitized, deterministic baselines; manifest binding; merge-blocking diffs). |

<div align="center">

[🏛️ Governance Charter](../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>


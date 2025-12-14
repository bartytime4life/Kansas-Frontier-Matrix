---
title: "🧬 Kansas Frontier Matrix — Provenance Fixtures: PROV‑O Fragments (E2E) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/governance/fixtures/provenance/prov_o/fragments/README.md"

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
intent: "tests-e2e-web-app-regression-governance-fixtures-provenance-prov-o-fragments"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-regression-governance-fixtures-provenance-prov-o-fragments-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:governance:fixtures:provenance:prov-o:fragments:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/governance/fixtures/provenance/prov_o/fragments/README.md"
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
  - "tests/e2e/web-app/regression/governance/fixtures/provenance/prov_o/fragments/README.md@v11.2.6"
---

<div align="center">

# 🧬 **Provenance Fixtures — PROV‑O Fragments (E2E) (v11 LTS)**
`tests/e2e/web-app/regression/governance/fixtures/provenance/prov_o/fragments/README.md`

**Purpose**  
Define the **canonical PROV‑O fragment fixtures** used by governance E2E regression suites to assemble safe, deterministic provenance bundles for UI rendering and leak‑safe verification.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Provenance-PROV--O-informational" />
<img src="https://img.shields.io/badge/Fixtures-Fragments-blueviolet" />
<img src="https://img.shields.io/badge/Governance-FAIR%2BCARE-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ PROV‑O Fixtures](../README.md) ·
[⬅️ Provenance Fixtures](../../README.md) ·
[⬅️ Governance Fixtures](../../../README.md) ·
[🧭 E2E Guide](../../../../../../../README.md)

</div>

---

## 📘 Overview

This folder contains **small, composable PROV‑O fragments** (typically JSON‑LD) used to build test‑safe provenance bundles.

Fragments exist to:
- 🧾 Provide **deterministic provenance structure** (Agent/Activity/Entity + relations) for UI regression tests.
- 🛡️ Ensure provenance surfaces remain **reference‑only** (IDs/hashes/labels), not payload dumps.
- 🚫 Prevent provenance from becoming a **precision leak channel** (no coordinates, no geometry, no bboxes).
- 🧪 Enable tests to assert **governance posture** across scenarios:
  - `public` (no masking required),
  - `masked` (generalized / redacted precision),
  - `restricted` (blocked / withheld UX).

**Non‑goals**
- Fragments are not “real provenance.” They are **synthetic test fixtures**.
- Fragments do not encode domain truth; they encode **UI‑relevant provenance shape**.
- Fragments must not include content that could plausibly reconstruct restricted knowledge.

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
                            ├── 🧾 registry.json                        — Scenario/bundle registry (optional)
                            │
                            ├── 📁 bundles/                             — Full synthetic bundles assembled for tests
                            │   └── 📄 README.md
                            │
                            ├── 📁 expected/                            — “Reference‑only” UI expectations
                            │   └── 📄 README.md
                            │
                            └── 📁 fragments/
                                ├── 📄 README.md                         — This guide
                                ├── 🧾 fragments_registry.json            — Fragment catalog + composition rules (optional)
                                │
                                ├── 🧾 agent.fragment.jsonld              — prov:Agent stub (synthetic)
                                ├── 🧾 activity.fragment.jsonld           — prov:Activity stub (synthetic)
                                ├── 🧾 entity.fragment.jsonld             — prov:Entity stub (synthetic)
                                ├── 🧾 relations.fragment.jsonld          — prov:used / prov:wasGeneratedBy / associations
                                └── 🧾 redaction.fragment.jsonld          — Masking posture + safe display hints
~~~

Notes:
- Filenames above represent the **canonical target layout** for a fragment library.
- If your implementation uses `.json` instead of `.jsonld`, keep the same semantics and safety rules.

---

## 🧭 Context

### Fragment design principles

Fragments SHOULD:
- be small enough to review in a PR diff,
- contain only the minimum keys required to render UI provenance signals,
- use stable deterministic identifiers,
- use placeholder hashes (`<sha256>`) rather than realistic values.

Fragments MUST NOT:
- include coordinates, geometries, bboxes, WKT, or GeoJSON keys,
- embed production URLs, tokens, credentials, or secrets,
- include real organization/person names or identifying text.

### Deterministic IDs (recommended)

Use stable synthetic identifiers such as:
- `urn:kfm:test:prov:agent:<id>`
- `urn:kfm:test:prov:activity:<id>`
- `urn:kfm:test:prov:entity:<id>`

Avoid:
- runtime-generated UUIDs unless pinned and recorded,
- “now” timestamps inside fragments.

### Governance posture (required concept)

Fragments should be composable into scenario bundles with an explicit posture:
- `public` — reference-only, no special masking banners required
- `masked` — reference-only + explicit redaction banner indicators
- `restricted` — reference-only + “withheld/blocked” state indicators

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Select scenario posture"] --> B["Load fragments (agent/activity/entity/relations)"]
  B --> C["Compose synthetic bundle"]
  C --> D["Render provenance UI"]
  D --> E["Assert reference-only signals (chips/badges)"]
  E --> F["Run leak checks (no precision exposure)"]
~~~

Interpretation:
- Fragments are a safe building block that lets tests validate provenance UX without importing real provenance data.

---

## 🧠 Story Node & Focus Mode Integration

Provenance UI is shared across governed surfaces:
- Story Node v3 evidence/provenance chips,
- Focus Mode v3 provenance panels,
- governance overlays and audit views.

Fragments SHOULD support this reuse by encoding:
- stable IDs for dataset/model/run references (synthetic),
- stable “chip labels” and “badge intent” fields (if your UI uses them),
- redaction posture hints without exposing sensitive details.

Minimum cross-surface invariants:
- provenance remains **reference‑only**,
- redaction posture stays consistent across route transitions,
- restricted scenarios remain restricted (no “expand to reveal”).

---

## 🧪 Validation & CI/CD

Fragments MUST pass:
- ✅ JSON/JSON‑LD parse validation
- ✅ secret scan
- ✅ PII scan (best-effort)
- ✅ governance leak checks (pattern-based)
- ✅ schema validation (if a fragment schema is enforced)

Recommended lint rules for fragment fixtures:
- forbid keys commonly associated with spatial precision (examples: `coordinates`, `bbox`, `geometry`, `wkt`)
- forbid numeric patterns that resemble high-precision lat/long pairs
- enforce deterministic ordering (formatter or canonicalization step)

Flake policy:
- provenance fixture failures are not retryable by default (treat as a governance regression).

---

## 📦 Data & Metadata

### Recommended fragment shape (safe, UI-first)

A fragment SHOULD contain only:
- identifiers,
- minimal labels,
- minimal timestamps (optional and pinned),
- stable relations (in a separate relations fragment if helpful),
- safe hashes as placeholders.

Example `prov:Agent` fragment (synthetic, simplified):
~~~json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "kfm": "urn:kfm:"
  },
  "@id": "urn:kfm:test:prov:agent:ci_runner",
  "@type": "prov:Agent",
  "prov:label": "KFM CI Runner (synthetic)"
}
~~~

Example `prov:Activity` fragment (synthetic, simplified):
~~~json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@id": "urn:kfm:test:prov:activity:e2e_run_001",
  "@type": "prov:Activity",
  "prov:label": "E2E Governance Run (synthetic)",
  "prov:startedAtTime": "2020-01-01T00:00:00Z"
}
~~~

Example relations fragment (synthetic, simplified):
~~~json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@id": "urn:kfm:test:prov:relations:e2e_run_001",
  "@type": "prov:Bundle",
  "prov:wasAssociatedWith": {
    "@id": "urn:kfm:test:prov:agent:ci_runner"
  },
  "prov:used": [
    { "@id": "urn:kfm:test:prov:entity:fixture_bundle_001" }
  ]
}
~~~

### Naming conventions (recommended)

- Prefix fragments by type: `agent.*`, `activity.*`, `entity.*`, `relations.*`, `redaction.*`
- Keep fragments posture-agnostic where possible; apply posture via:
  - a separate `redaction.fragment.*`, or
  - a scenario bundle composer that adds posture metadata.

---

## 🌐 STAC, DCAT & PROV Alignment

Fragments are test fixtures (not production catalogs):

- **PROV‑O**: fragments model `prov:Agent`, `prov:Activity`, and `prov:Entity` in a synthetic, minimal form.
- **DCAT**: fragments are test artifacts (`mediaType: application/ld+json` or `application/json`).
- **STAC**: if indexed as items, use non-spatial representation:
  - `geometry: null`
  - `properties.datetime` pinned to a deterministic time

All representations must remain:
- synthetic,
- non-identifying,
- leak-safe.

---

## 🧱 Architecture

### Composition pattern (recommended)

1. Load `fragments_registry.json` (if present) to select required fragments.
2. Compose fragments into a scenario bundle:
   - add posture metadata (`public|masked|restricted`)
   - add safe hash placeholders
3. Feed the composed bundle to:
   - UI API mocks, or
   - a fixture loader in the test stack
4. Run UI assertions against:
   - reference-only chips/badges
   - no precision leak rules

Avoid:
- embedding composed bundles directly into test code (prefer fixture files),
- duplicating fragment content across scenarios (use composition).

---

## ⚖ FAIR+CARE & Governance

Fragments exist to support governance outcomes:

- **Authority to Control**: prevents provenance UIs from revealing precision or restricted details.
- **Responsibility & Ethics**: keeps test content safe and non-harmful.
- **Collective Benefit**: provides transparent provenance signals (traceability) without enabling misuse.

If a fragment is found to violate policy:
- remove it immediately,
- invalidate related scenarios until fixed,
- route review to the relevant working group and FAIR+CARE Council.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-14 | Initial PROV‑O fragments guide aligned to KFM‑MDP v11.2.6 (synthetic composition, reference‑only UX support, leak‑safe invariants). |

<div align="center">

[🏛️ Governance Charter](../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>


---
title: "🧪 Kansas Frontier Matrix — Leak Checks Fixtures (E2E) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/governance/utils/leak_checks/fixtures/README.md"

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
intent: "tests-e2e-governance-leak-checks-fixtures"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-governance-leak-checks-fixtures-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:governance:utils:leak-checks:fixtures:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/governance/utils/leak_checks/fixtures/README.md"
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
  - "tests/e2e/web-app/regression/governance/utils/leak_checks/fixtures/README.md@v11.2.6"
---

<div align="center">

# 🧪 **Leak Checks — Fixtures (E2E) (v11 LTS)**
`tests/e2e/web-app/regression/governance/utils/leak_checks/fixtures/README.md`

**Purpose**  
Define the canonical **synthetic fixture set** used by governance **leak-check** E2E tests.  
Fixtures here simulate “leak-like” and “safe” surfaces in a way that is **deterministic**, **auditable**, and **sovereignty-safe**.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Test%20Type-E2E%20Governance-blueviolet" />
<img src="https://img.shields.io/badge/Domain-Leak%20Detection-informational" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Leak Checks Module](../README.md) ·
[🧩 Governance Regression](../../../README.md) ·
[🧭 E2E Guide](../../../../../../README.md)

</div>

---

## 📘 Overview

Leak-check fixtures are **purpose-built synthetic inputs** used to ensure KFM surfaces never expose:

- raw coordinate precision,
- sensitive geometry payloads,
- restricted or sovereignty-protected content,
- secrets, tokens, or identifying strings.

These fixtures are designed for two roles:

- ✅ **Negative tests (SAFE cases):** confirm leak checkers do *not* false-positive on normal content.
- 🚫 **Positive tests (LEAK cases):** confirm leak checkers *do* detect leak-like patterns (using non-realistic, policy-safe strings).

Fixtures MUST be:

- **Synthetic**: no real individuals, no real addresses, no real site geometry.
- **Deterministic**: stable IDs, stable ordering, stable timestamps.
- **Policy-safe**: “leak-like” strings must not be plausibly usable as real coordinates or restricted knowledge.

Fixtures MUST NOT:

- contain plausible latitude/longitude pairs within valid Earth ranges,
- include WKT/GeoJSON coordinate arrays that could represent real sites,
- include any production-like token, credential, or secret.

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
                        └── 📁 fixtures/
                            ├── 📄 README.md                           — This guide (fixture policy + formats)
                            │
                            ├── 🧾 fixture_registry.json                — Fixture ID → file mapping + tags
                            ├── 🧾 redaction_tokens.json                — Canonical redaction tokens (shared)
                            ├── 🧾 allowlist_patterns.json              — Allowed patterns (safe UI strings)
                            ├── 🧾 blocklist_patterns.json              — Leak-like patterns to detect (synthetic)
                            │
                            ├── 📁 cases/                               — Individual test cases (small, high-signal)
                            │   ├── 🧾 safe_dom_excerpt.json             — SAFE: redacted/normal UI excerpt
                            │   ├── 🧾 safe_network_excerpt.json         — SAFE: redacted network excerpt
                            │   ├── 🧾 leak_like_numbers_oob.json        — LEAK: out-of-range numeric patterns
                            │   ├── 🧾 leak_like_wkt_stub.json           — LEAK: WKT-like stub (synthetic + incomplete)
                            │   └── 🧾 leak_like_geojson_stub.json       — LEAK: GeoJSON-like stub (geometry removed)
                            │
                            └── 📁 bundles/                             — Optional grouped fixtures for larger specs
                                ├── 🧾 bundle_safe_suite.json
                                └── 🧾 bundle_leak_suite.json
~~~

Notes:
- File names above are the **canonical target layout** for this folder.
- If your repo uses `.yaml`, keep the structure and meaning the same.
- Keep fixtures tiny: “diff-readable” is a governance feature.

---

## 🧭 Context

### Fixture design principles

Fixtures SHOULD:

- encode one primary signal per file (one “thing to detect”),
- keep payloads short (ideally < 200 lines),
- use stable deterministic IDs (no random generation unless seed is pinned and recorded),
- avoid accidentally creating plausible real-world coordinates.

Fixtures SHOULD NOT:

- imitate real locations, tribal lands, or archaeological sites,
- include full API responses (use excerpt stubs),
- embed complete geometries (use null geometry + explicit placeholders).

### “Leak-like” content rules (strict)

To test coordinate-leak detection without embedding plausible coordinates:

- Prefer **out-of-range** numeric pairs:
  - latitude outside `[-90, 90]`
  - longitude outside `[-180, 180]`

Example (safe to publish, still “leak-like” for regex):
- `lat=999.999999, lon=-999.999999`

If a fixture must include coordinate-like syntax, it MUST be:
- obviously out of range, and
- labeled as synthetic, and
- validated by leak-check fixture lint rules.

### Canonical redaction tokens

Use these exact tokens consistently:
- `<redacted>`
- `<masked>`
- `<synthetic-id>`
- `<sha256>`

Avoid ambiguous placeholders (e.g., `XXX`, `???`) in governance fixtures.

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Load fixture_registry.json"] --> B["Select fixture_id"]
  B --> C["Load case payload (cases/*.json)"]
  C --> D["Normalize + redact (if applicable)"]
  D --> E["Run leak detectors"]
  E --> F["Assert expected result (pass/fail + matches)"]
  F --> G["Write artifacts + telemetry"]
~~~

Interpretation:
- Leak-check fixtures are inputs; the leak-check engine must normalize/redact and then assert policy invariants.

---

## 🧠 Story Node & Focus Mode Integration

Leak checks are designed to protect user-visible narrative and map surfaces, including:

- Focus Mode v3 tooltips and panel excerpts,
- Story Node v3 “spacetime” and related UI views,
- provenance and evidence chips,
- download previews and JSON views.

Fixtures MAY simulate Story Node or Focus Mode excerpts, but must:
- keep IDs synthetic,
- keep geometry null or explicitly masked,
- avoid narrative content beyond a short synthetic excerpt.

---

## 🧪 Validation & CI/CD

Fixtures in this folder are CI-scanned and must pass:

- ✅ parse validation (JSON/YAML)
- ✅ schema validation (if fixture schemas exist)
- ✅ secret scan
- ✅ PII scan (best-effort)
- ✅ leak safety scan (no plausible real coordinate pairs)
- ✅ deterministic formatting (stable ordering)

### Quarantine policy

If a fixture causes flakiness or ambiguous false positives:
- move it behind a `@nightly`-only suite,
- reduce the fixture scope and signal,
- document the change in the fixture registry.

Governance-related failures are **not** auto-retryable by default.

---

## 📦 Data & Metadata

### Fixture registry (canonical shape)

The registry maps fixture IDs to files and tags.

~~~json
{
  "schema_version": "v11.2.6",
  "fixtures": {
    "safe_dom_excerpt": {
      "path": "cases/safe_dom_excerpt.json",
      "expected": "pass",
      "tags": ["@governance", "@regression"]
    },
    "leak_like_numbers_oob": {
      "path": "cases/leak_like_numbers_oob.json",
      "expected": "fail",
      "tags": ["@governance", "@regression"]
    }
  }
}
~~~

### Case file format (recommended)

Each case file should be small and explicit:

~~~json
{
  "fixture_id": "leak_like_numbers_oob",
  "surface": "dom_excerpt",
  "notes": "Synthetic out-of-range coordinate-like numbers to validate regex detection without plausible real coordinates.",
  "payload": {
    "text": "DEBUG: lat=999.999999 lon=-999.999999 <redacted>"
  },
  "expect": {
    "should_flag": true,
    "match_categories": ["coordinate_like_numeric_pair"],
    "raw_coordinates_plausible": false
  }
}
~~~

### Allowlist / blocklist patterns

- `allowlist_patterns.json` contains safe strings the detector must not flag.
- `blocklist_patterns.json` contains patterns that should always be flagged.

Patterns should be short, documented, and conservative.

---

## 🌐 STAC, DCAT & PROV Alignment

### PROV-O alignment (fixture interpretation)

- A fixture case is a `prov:Entity`.
- A leak-check test run is a `prov:Activity`.
- CI/test runner is a `prov:Agent`.

Fixtures must remain publish-safe; provenance references must remain synthetic.

### STAC/DCAT alignment (optional)

If fixtures are cataloged:
- treat them as test artifacts (documentation / QA data), not real datasets,
- ensure any STAC-like representation uses `geometry: null`,
- keep `dcat:Dataset` metadata clearly labeled as synthetic QA assets.

---

## 🧱 Architecture

### How leak-check fixtures are used (recommended pattern)

Specs SHOULD:
1. select a `fixture_id`,
2. load the registry,
3. load one case file,
4. run normalizer/redactor,
5. run detector(s),
6. assert expected result + match categories.

This prevents:
- hardcoding test strings in code,
- scattering policy assumptions across tests,
- accidental introduction of plausible sensitive patterns.

---

## ⚖ FAIR+CARE & Governance

### Sovereignty-safe fixture mandate (non-negotiable)

Fixtures MUST:
- never store plausible real coordinates,
- never store full geometry payloads,
- never attempt to emulate restricted cultural information.

### Ethical language rules

Synthetic text MUST:
- avoid colonial framing,
- avoid genealogy inference,
- avoid content that could be harmful if surfaced.

### Escalation

If any fixture is found to violate policy:
- remove it immediately,
- invalidate dependent tests until corrected,
- route review to the governance test owners and FAIR+CARE Council.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Initial leak-check fixtures guide aligned to KFM-MDP v11.2.6 (deterministic, sovereignty-safe, minimal, audit-friendly). |

<div align="center">

[🏛️ Governance Charter](../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>


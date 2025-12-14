---
title: "🧼 Kansas Frontier Matrix — Artifact Redaction (Governance Regression E2E) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/governance/artifacts/redaction/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous Systems Oversight · FAIR+CARE Council"
content_stability: "stable"

status: "Active · Enforced"
doc_kind: "Redaction Guide"
header_profile: "standard"
footer_profile: "standard"
intent: "tests-e2e-web-app-regression-governance-artifacts-redaction"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-regression-governance-artifacts-redaction-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:governance:artifacts:redaction:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/governance/artifacts/redaction/README.md"
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
  - "tests/e2e/web-app/regression/governance/artifacts/redaction/README.md@v11.2.6"
---

<div align="center">

# 🧼 **Artifact Redaction (Governance Regression E2E) (v11 LTS)**
`tests/e2e/web-app/regression/governance/artifacts/redaction/README.md`

**Purpose**  
Define the **canonical redaction rules and workflow** for governance regression E2E artifacts so reports remain:
- auditable and useful for debugging,
- deterministic and schema-valid,
- and **safe-by-design** (no precision leaks, no PII, no secrets).

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/E2E-Redaction-blueviolet" />
<img src="https://img.shields.io/badge/Governance-FAIR%2BCARE-orange" />
<img src="https://img.shields.io/badge/Policy-No%20Leaks-red" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Artifacts Guide](../README.md) ·
[🧾 Templates](../templates/README.md) ·
[🕵️ Leak Checks](../../utils/leak_checks/README.md)

</div>

---

## 📘 Overview

Redaction is the **final safety boundary** for governance E2E artifacts.

Even when tests use synthetic fixtures, artifacts can still become unsafe if they contain:
- coordinate-like patterns,
- geometry dumps,
- raw payload strings,
- stack traces that embed restricted fragments,
- secrets or tokens.

Redaction MUST be applied before:
- artifacts are uploaded to CI,
- artifacts are referenced in telemetry,
- artifacts are copied into release bundles.

### Redaction principles

- **Fail closed**: if redaction cannot guarantee safety, do not publish the artifact.
- **Prefer hashes**: store `sha256` hashes of evidence rather than evidence itself.
- **Minimal snippets only**: if a snippet is required, keep it short and redacted.
- **Deterministic output**: same input → same redacted output.

### Non-goals

- Redaction is not a replacement for application governance enforcement.
- Redaction must not be used to “hide” genuine governance failures; it must preserve failure signals (rule IDs, selectors, severities).
- Redaction must not attempt to reconstruct or normalize restricted content.

---

## 🗂️ Directory Layout

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 regression/
            └── 📁 governance/
                └── 📁 artifacts/
                    ├── 📁 redaction/
                    │   ├── 📄 README.md                       — This guide
                    │   ├── 🧾 redaction_rules.json            — Redaction patterns + placeholders (reviewed)
                    │   ├── 🧾 redaction_allowlist.json         — Safe placeholders only (no real-looking examples)
                    │   ├── 📄 redaction_apply.ts              — Applies redaction to candidate artifacts
                    │   ├── 📄 redaction_validate.ts           — Validates redaction effectiveness (scan)
                    │   └── 📄 index.ts                        — Public exports
                    │
                    ├── 📁 templates/                          — Artifact templates (placeholders)
                    └── 📄 README.md                           — Artifact contract for governance regressions
~~~

Notes:
- `redaction_rules.json` and `redaction_allowlist.json` are governance-critical files and must be reviewed carefully.
- Runtime redaction outputs should not be committed; they belong in `reports/` during CI runs.

---

## 🧭 Context

### What must be redacted (minimum)

Redaction MUST protect against:

- coordinate-like numeric pairs at high precision,
- bbox-like sequences (four numbers) at high precision,
- GeoJSON/WKT-like fragments (including `"coordinates"` keys),
- stack traces that include request/response bodies,
- URLs with embedded tokens,
- environment variables, headers, cookies,
- any PII-like patterns (best-effort scan).

### What must be preserved (for debugging)

Redaction MUST preserve:

- rule IDs and severities (`pass/warn/block`),
- scenario IDs and suite tags,
- stable selector names (e.g., `data-testid=...`),
- request “names” or endpoint identifiers (without raw bodies),
- hashes of removed or redacted content.

### Safe placeholder vocabulary (recommended)

Use explicit placeholders that cannot be confused with real values:

- `<REDACTED_COORD_PAIR>`
- `<REDACTED_BBOX>`
- `<REDACTED_GEOMETRY>`
- `<REDACTED_TOKEN>`
- `<REDACTED_PII>`
- `<REDACTED_PAYLOAD>`
- `<REDACTED_STACK_TRACE>`

Do not use numeric-looking placeholders.

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Artifact candidate generated"] --> B["Apply redaction rules"]
  B --> C["Apply allowlist (safe placeholders only)"]
  C --> D["Validate (leak scan + secret scan)"]
  D -->|pass| E["Write redacted artifact to reports/"]
  D -->|fail| F["Block upload + fail CI gate"]
~~~

Interpretation:
- Redaction is a gate: if validation fails, governance artifacts are not published and CI blocks.

---

## 🧪 Validation & CI/CD

Redaction MUST be enforced in CI for governance suites.

Recommended gating:
- run redaction on:
  - leak-check reports,
  - governance summaries,
  - any runner-generated JSON reports,
  - console logs captured for artifacts (if enabled).
- validate redaction with:
  - leak scans on artifacts,
  - secret scan on artifacts,
  - PII scan (best-effort) on artifacts.

### Redaction failure policy

- Redaction failure is **stop-ship** for governance suites.
- Redaction failures are **not retryable by default**.
- Fix the underlying artifact generation to avoid producing unsafe content.

---

## 📦 Data & Metadata

### Redaction rules (recommended shape)

Rules MUST be abstract and must not include real-looking examples.

~~~json
{
  "schema_version": "v11.2.6",
  "rules": [
    {
      "rule_id": "redact_high_precision_coord_pairs",
      "type": "regex",
      "severity": "block",
      "replacement": "<REDACTED_COORD_PAIR>",
      "notes": "Redacts coordinate-like pairs with high precision."
    },
    {
      "rule_id": "redact_geojson_coordinates_key",
      "type": "string",
      "severity": "block",
      "match": "\"coordinates\"",
      "replacement": "\"coordinates\": <REDACTED_GEOMETRY>",
      "notes": "Redacts GeoJSON coordinate keys to avoid geometry dumps."
    }
  ]
}
~~~

### Allowlist (recommended shape)

Allowlists MUST contain only placeholders that are explicitly safe.

~~~json
{
  "schema_version": "v11.2.6",
  "allowed_placeholders": [
    "<REDACTED_COORD_PAIR>",
    "<REDACTED_BBOX>",
    "<REDACTED_GEOMETRY>",
    "<REDACTED_TOKEN>",
    "<REDACTED_PII>",
    "<REDACTED_PAYLOAD>",
    "<REDACTED_STACK_TRACE>"
  ],
  "notes": "This allowlist must never contain values resembling real coordinates or identities."
}
~~~

### Redaction validation report (recommended minimal shape)

~~~json
{
  "schema_version": "v11.2.6",
  "artifact_path": "<path>",
  "status": "pass",
  "rules_applied": ["redact_high_precision_coord_pairs"],
  "leak_scan": { "block": 0, "warn": 0 },
  "secret_scan": { "findings": 0 },
  "pii_scan": { "findings": 0 },
  "hash_before": "<sha256>",
  "hash_after": "<sha256>"
}
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

Redaction outputs are test artifacts.

- **DCAT**: redacted reports are `dcat:Distribution` artifacts (`mediaType: application/json`)
- **STAC**: if represented, use non-spatial items (`geometry: null`)
- **PROV-O**:
  - redaction is a `prov:Activity` in the E2E run chain
  - rules and allowlists are `prov:Entity`
  - CI runner is a `prov:Agent`

---

## 🧱 Architecture

### Recommended redaction pipeline (implementation posture)

1. Normalize input (stable encoding and line endings)
2. Apply block rules (redact high-risk patterns)
3. Apply warn rules (optional; for safety hardening)
4. Apply allowlist normalization (ensure placeholders are consistent)
5. Validate with leak/secret/pii scanners
6. Write artifact and record before/after hashes

### Anti-patterns (avoid)

- storing raw artifacts “just in case” alongside redacted artifacts
- allowing exceptions by adding real-looking examples to allowlists
- printing redacted and unredacted content to CI logs
- relying on redaction to justify unsafe app behavior

---

## ⚖ FAIR+CARE & Governance

Redaction enforces:

- **Authority to Control**: prevents artifacts from becoming a leakage channel.
- **Responsibility**: blocks unsafe outputs even when tests “pass.”
- **Ethics**: prevents avoidable harm via accidental exposure.
- **Collective Benefit**: enables safe audit and debugging across teams.

If a redaction rule change reduces protection:
- treat as governance-impacting,
- require review by governance maintainers and FAIR+CARE Council,
- prefer tightening rules and increasing hashing over adding exceptions.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-14 | Initial artifact redaction guide aligned to KFM‑MDP v11.2.6 (rules + allowlists + validation gates; fail-closed posture). |

<div align="center">

[🏛️ Governance Charter](../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>


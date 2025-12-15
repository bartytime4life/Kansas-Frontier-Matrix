---
title: "🛰️ Kansas Frontier Matrix — API Utility Layer (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/utils/api/README.md"
version: "v11.2.3"
last_updated: "2025-12-15"
review_cycle: "Quarterly · FAIR+CARE Council & Web Architecture Board"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"

telemetry_ref: "../../../../releases/v11.2.2/focus-telemetry.json"
system_telemetry_ref: "../../../../releases/v11.2.2/system-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-utils-api-v11.json"

signature_ref: "<optional-if-published: ../../../../releases/v11.2.2/signature.sig>"
attestation_ref: "<optional-if-published: ../../../../releases/v11.2.2/slsa-attestation.json>"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

status: "Active / Enforced"
doc_kind: "Architecture"
intent: "web-api-utils"
role: "frontend-api-helpers"
category: "Web · Utilities · API · Fetch Layer"

classification: "Public Document"
fair_category: "F1-A1-I2-R3"
care_label: "Public · Governed"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: true
risk_category: "Low"
redaction_required: false
data_steward: "KFM FAIR+CARE Council"

provenance_chain:
  - "web/src/utils/api/README.md@v11.2.2"
  - "web/src/utils/api/README.md@v11.0.0"
  - "web/src/utils/api/README.md@v10.4.0"
  - "web/src/utils/api/README.md@v10.3.0"
provenance_requirements:
  versions_required: true
  newest_first: true

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "WebAPI"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"

json_schema_ref: "../../../../schemas/json/web-utils-api-readme-v11.schema.json"
shape_schema_ref: "../../../../schemas/shacl/web-utils-api-readme-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:web-utils-api-readme:v11.2.3"
semantic_document_id: "kfm-doc-web-utils-api-readme"
event_source_id: "ledger:web/src/utils/api/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-historical-claims"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"
  - "content-alteration"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next API-utils revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🛰️ **Kansas Frontier Matrix — API Utility Layer (v11.2.3)**  
`web/src/utils/api/README.md`

**Purpose**  
Define the deterministic, FAIR+CARE-governed, sovereignty-safe API utility layer used across the  
KFM Web Platform for interacting with:  
- REST endpoints  
- GraphQL queries  
- STAC/DCAT APIs  
- Focus Mode & Story Node endpoints  
- Telemetry sinks  
- Governance lookups  

This layer ensures consistent, safe, observable API behavior and keeps the web UI from coupling to backend quirks.

[![License: MIT](https://img.shields.io/badge/License-MIT-green)]() ·
[![MCP-DL v6.3](https://img.shields.io/badge/MCP--DL-v6.3-blue)]() ·
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Governed-gold)]()

</div>

---

## 📘 Overview

The API utility layer in `web/src/utils/api/**` provides:

- 🧩 Standardized fetch wrappers (retry, abort, timeouts)
- 🔐 Governance-safe parameter handling (no sensitive coordinate leakage)
- 🛡️ CARE & sovereignty compliance checks and propagation
- 🧾 Provenance propagation into responses (PROV-friendly fields)
- 🧬 JSON-LD friendly response shapes (where applicable)
- 🧪 Response validators (STAC, DCAT, Focus/Story payload guards)
- 📡 Telemetry hooks for latency, errors, and governance flags
- 🧊 Deterministic response normalization (stable sorting, canonical key order where needed)
- 🧵 GraphQL wrapper with type guards and error taxonomy

Constraints:

- Framework-agnostic (no React imports)
- No DOM usage (no `window`, no `document`, no browser globals)
- Deterministic behavior (same input → same output/error)
- No UI/business logic (only low-level request/response helpers)

This layer powers (examples):

- Story Node v3 loading
- Focus Mode v3 entity fetches
- Map layer metadata fetches
- Dataset previews and catalog browsing
- Timeline hydration
- Governance overlay lookups (CARE/sovereignty/license)

---

## 🗂️ Directory Layout

~~~text
web/src/utils/api/
├── 📄 apiClient.ts            # Core fetch wrapper (timeouts, retries, aborts, headers)
├── 📄 responseGuards.ts       # STAC/DCAT/Story/Focus/Graph response guards + schema checks
├── 📄 jsonRequest.ts          # Safe JSON helpers (POST/PUT/PATCH) with deterministic encoding
├── 📄 graphqlClient.ts        # GraphQL query/mutation wrapper with strict result validation
├── 📄 stacClient.ts           # STAC Item/Collection fetch helpers + STAC guard integration
├── 📄 dcatClient.ts           # DCAT dataset/distribution fetch helpers + DCAT guard integration
├── 📄 focusClient.ts          # Focus Mode v3 request helpers (entity → context → narrative)
├── 📄 storyClient.ts          # Story Node v3 request helpers (cards, details, relations)
├── 📄 governanceClient.ts     # CARE/sovereignty/license metadata lookups (public-safe)
└── 📄 telemetryClient.ts      # Frontend telemetry sender (schema-validated, no PII)
~~~

Directory rule: this folder must contain only *transport + shape validation + normalization* utilities.

---

## 🧱 Architecture

### Request/Response lifecycle (frontend)

~~~mermaid
flowchart LR
  UI["UI (components/hooks)"] --> SVC["web/src/services (feature orchestration)"]
  SVC --> API["utils/api/apiClient.ts"]
  API --> GUARD["utils/api/responseGuards.ts"]
  GUARD --> NORM["Deterministic normalization"]
  NORM --> SVC
  SVC --> UI
  API --> TEL["utils/api/telemetryClient.ts (latency/errors)"]
~~~

### Core design principles

- Single hardened entrypoint for HTTP (`apiClient.ts`)
- Guards sit between the network and UI (fail fast)
- Normalization ensures stable UI rendering (no backend ordering assumptions)
- Governance metadata is treated as first-class (carried, not discarded)
- Telemetry is opt-in per call-site but uses consistent schema + taxonomy

### Error taxonomy (recommended)

API utilities should surface errors consistently so the UI and CI logs are actionable.

~~~text
Category (example)         When used
- network_timeout          Request exceeded timeout budget
- network_unreachable      DNS/connection issues, offline
- http_non_2xx             Any non-success status; include status + safe message
- schema_invalid           Response failed guard/schema validation
- governance_blocked       CARE/sovereignty rules prevent returning details
- parse_error              JSON/text parsing failed
- rate_limited             429 / backoff suggested
- unknown                  Anything else; preserve safe debug context
~~~

---

## 🧭 Context

Position in the web stack:

- UI consumes *services/hooks* which call this layer for transport.
- This layer does not decide “what to fetch”; it decides “how to fetch safely and consistently”.
- The layer is the enforcement point for:
  - request shaping (safe params)
  - response shaping (guards)
  - observability (telemetry)
  - governance propagation (CARE/sovereignty/license/provenance)

Boundary rules:

- Do not import React, map libraries, or UI modules here.
- Do not import raw configuration that would make tests non-deterministic.
- Do not create new ontological claims or historical assertions (transport only).

---

## 📦 Data & Metadata

### Required metadata behavior (layer responsibilities)

- Preserve provenance fields returned by APIs (do not drop or rename casually).
- Preserve CARE label / rights flags returned by APIs.
- Ensure pagination metadata is surfaced in a predictable shape.
- Normalize date/time text into a machine-safe representation (no “sharpening” fuzzy dates).

### Governance-safe parameter rules (must)

- Never encode restricted coordinates (or over-precise coordinates) in URLs.
- Avoid exposing restricted IDs in query strings when a safer alias exists.
- If an API offers “generalized” vs “precise” modes, default to generalized unless explicitly allowed.

### Deterministic normalization (examples)

- Stable sort lists before returning to UI (explicit comparator, no locale-dependent sorting).
- Canonicalize optional arrays to `[]` rather than `undefined` when it improves downstream safety.
- Avoid auto-filling missing fields; missing stays missing (guards decide pass/fail).

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Treat STAC as the canonical structure for spatial/temporal dataset discovery.
- Validate at minimum:
  - `type`
  - `stac_version`
  - `id`
  - `bbox` / `geometry` (when present)
  - `datetime` or `start_datetime` / `end_datetime`
  - `assets` integrity (roles, hrefs)

### DCAT

- Treat DCAT as the canonical structure for catalog-level dataset descriptions.
- Validate at minimum:
  - identifiers (URI/URN)
  - license/rights statements
  - temporal/spatial coverage
  - distributions (downloads/services) where present

### PROV

- Preserve PROV-friendly fields (run IDs, derivation links, “wasDerivedFrom”-style relationships).
- When the UI needs a “provenance summary”, generate it deterministically and keep it clearly labeled as a UI summary (not new provenance).

---

## ⚖ FAIR+CARE & Governance

This layer is governance-sensitive because it controls what can be requested and returned.

Minimum governance requirements:

- Reject unvalidated responses (schema/guard failure is not “best effort”; it is a stop condition).
- Never expose restricted coordinates, protected site identifiers, or disallowed fields.
- Treat sovereignty as a hard constraint: if data is masked/generalized, do not attempt to reconstruct precision.
- Preserve CARE metadata across transforms (do not strip labels).
- If governance metadata is missing when required, fail safe (return a governance error, not partial sensitive content).

Governance violations are release-blocking via repository CI policy (e.g., FAIR+CARE validation and security/audit workflows).

---

## 🧠 Story Node & Focus Mode Integration

This layer supports narrative-facing features by enforcing “facts must remain evidence-led” *at the transport boundary*.

Recommended integration practices:

- `storyClient.ts` should:
  - validate Story Node v3 payloads before the UI renders
  - surface provenance chains and evidence links as first-class fields
  - ensure narrative text is accompanied by references (when required by the Story Node contract)

- `focusClient.ts` should:
  - validate Focus Mode v3 response shapes
  - apply governance overlays *before* returning results to the UI layer
  - propagate any “blocked/provisional” governance status to the UI so it can render safe fallbacks

---

## 🧪 Validation & CI/CD

Test locations (expected):

~~~text
tests/unit/web/utils/api/**
tests/integration/web/utils/api/**
~~~

Minimum test coverage targets:

- Deterministic fetch behavior (timeouts, retries, abort)
- Error taxonomy mapping (network/http/schema/governance)
- Guard coverage for:
  - STAC Items/Collections
  - DCAT dataset/distribution shapes
  - Story Node and Focus response shapes
- “No leakage” tests:
  - restricted params are rejected or generalized
  - restricted fields are not returned from helpers
- Telemetry schema validation and “no PII” checks for event payloads

CI expectations:

- Fail fast on schema invalid responses.
- Block merges on governance regressions (CARE/sovereignty checks).
- Treat changes in this layer as high-impact (web architecture review recommended).

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.3 | 2025-12-15 | Reformatted to KFM-MDP v11.2.6 (single H1, approved H2 registry, outer-backticks/inner-tildes); expanded architecture/context/governance guidance without removing existing data. |
| v11.2.2 | 2025-11-28 | Full v11.2.2 upgrade; emoji layout; governance, sovereignty, CARE, STAC/DCAT, v3 alignment. |
| v11.0.0 | 2025-11-24 | v11 API utility layer established for Focus/Story/graph and catalog fetch patterns. |
| v10.4.0 | 2025-11-15 | Early v10.4 API utils introduction. |
| v10.3.0 | 2025-11-13 | Initial API utility block. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  

[⬅️ Back to Utils Overview](../README.md) ·
[🧭 Web Source Overview](../../README.md) ·
[🌐 Web Platform](../../../README.md) ·
[🛡 Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[⚖ FAIR+CARE Guide](../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

</div>
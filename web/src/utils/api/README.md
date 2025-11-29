---
title: "🛰️ Kansas Frontier Matrix — API Utility Layer (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/utils/api/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"
review_cycle: "Quarterly · FAIR+CARE Council & Web Architecture Board"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-utils-api-v11.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

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
  - "web/src/utils/api/README.md@v10.3.0"
  - "web/src/utils/api/README.md@v10.4.0"
  - "web/src/utils/api/README.md@v11.0.0"
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

doc_uuid: "urn:kfm:doc:web-utils-api-readme:v11.2.2"
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
  - "governance-override"
  - "content-alteration"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next API-utils revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🛰️ **Kansas Frontier Matrix — API Utility Layer (v11.2.2)**  
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
This layer ensures consistent, safe, observable API behavior.

</div>

---

# 🧭 1. Overview

The API utility layer in `web/src/utils/api/**` provides:

- 🧩 **Standardized fetch wrappers** (retry, abort, timeouts)  
- 🔐 **Governance-safe parameter handling** (no sensitive coordinate leakage)  
- 🛡️ **CARE & sovereignty compliance**  
- 🧾 **Provenance propagation** into responses  
- 🧬 **JSON-LD friendly response shapes**  
- 🛠 **Response validators** (STAC, DCAT, graph entity types)  
- 🌩 **Telemetry hooks** for latency, errors, ethics flags  
- 🧊 **Deterministic response normalization**  
- 📜 **GraphQL wrapper** with type guards & error taxonomy  

These utilities must remain:

- **Pure data-to-data transforms**  
- Framework-agnostic (no React imports)  
- Fully TypeScript-strict  
- 🚫 No DOM, no window, no browser globals  

They power:

- Story Node v3 loading  
- Focus Mode v3 entity fetches  
- Map layer metadata fetches  
- Dataset previews  
- Timeline event hydration  
- Governance overlay metadata lookups  

---

# 🗂 2. Directory Structure (Emoji-Rich · v11.2.2)

~~~text
web/src/utils/api/
│
├── 🌐 apiClient.ts          # Core fetch wrapper (retry, abort, headers, governance)
├── 🧪 responseGuards.ts     # STAC/DCAT/StoryNode/GraphQL response validators
├── 🧾 jsonRequest.ts        # Safe JSON POST/PUT/PATCH helpers with type guards
├── 🧵 graphqlClient.ts      # GraphQL wrapper (query/mutate w/ deterministic transforms)
├── 🧬 stacClient.ts         # STAC Item/Collection fetcher with schema validation
├── 🗂 dcatClient.ts         # DCAT dataset/distribution fetcher
├── 🎯 focusClient.ts        # Focus Mode v3 API requester (entity → context → narrative)
├── 📚 storyClient.ts        # Story Node v3 fetcher (cards, details, relations)
├── 🔐 governanceClient.ts   # CARE/sovereignty/license metadata lookups
└── 📡 telemetryClient.ts    # Frontend telemetry event sender (OpenTelemetry v11)
~~~

This directory **must not contain business logic** — only low-level API helpers.

---

# 🧱 3. Module Descriptions

## 🌐 `apiClient.ts` — Core Fetch Wrapper

Provides a hardened wrapper around `fetch()`:

- Timeout + abort controllers  
- Automatic JSON parsing  
- Error taxonomy generation  
- Consistent headers (versioning, provenance, governance flags)  
- CARE-safe query parameter encoding  
- Sovereignty-aware redactions in request paths  

Guarantees:

- No sensitive coordinate leakage  
- Deterministic errors  
- Telemetry hooks before/after fetch  
- Enforced method/verb whitelisting  

---

## 🧪 `responseGuards.ts` — Response Validators

Contains type guards + schema validators for:

- Story Node v3  
- Focus Mode v3 response shapes  
- STAC Collections/Items  
- DCAT datasets  
- GraphQL entity payloads  
- Temporal extents  
- Governance metadata (`careLabel`, `sovereignty`, `license`)  

Guarantees:

- Malformed responses fail fast  
- No rendering until governance validation passes  

---

## 🧾 `jsonRequest.ts` — Safe JSON Helpers

Features:

- Deterministic JSON encoding  
- Automatic provenance stamping (e.g., `"via": "web-client-v11.2.2"`)  
- CARE-aware sanitization of outgoing payloads  
- Response validation via `responseGuards`  

Supports:

- POST/PUT/PATCH/DELETE  
- Typed payloads and responses  

---

## 🧵 `graphqlClient.ts` — GraphQL Wrapper

Capabilities:

- Query + mutation helpers  
- Deterministic error formatting  
- Strict response validation via GraphQL result schemas  
- Mapping GraphQL → UI-ready shapes (no speculation)  
- Automatic inclusion of:
  - CARE labels  
  - Sovereignty flags  
  - Provenance metadata  

Must never:

- Invent missing fields  
- Sharpen uncertain temporal or spatial detail  

---

## 🧬 `stacClient.ts`

Loads and validates:

- STAC Collections  
- STAC Items  
- Assets, roles, extents  
- Temporal/spatial metadata  

Applies:

- Coordinate masking  
- Governance metadata merges  
- Data contract alignment (`KFM-STAC v11`)  

---

## 🗂 `dcatClient.ts`

Loads DCAT datasets/distributions:

- Validates DCAT Dataset JSON-LD  
- Extracts license, temporal coverage, spatial extents  
- Aligns with `KFM-DCAT v11` profile  
- Propagates FAIR metadata to consuming UIs  

---

## 🎯 `focusClient.ts`

Requests Focus Mode v3:

- Focal entity resolution  
- Context window generation  
- Narrative blocks  
- Related entities  
- Governance overlays  

Applies **strict CARE/sovereignty filters** before returning data to the web UI.

---

## 📚 `storyClient.ts`

Requests Story Node v3:

- Cards  
- Details  
- Relations  
- Provenance chains  
- Temporal + spatial footprints  

Validates Story Node v3 schema before returning results.

---

## 🔐 `governanceClient.ts`

Used for:

- CARE/sovereignty lookups  
- License metadata  
- Rights-holder identification  
- Data-use restrictions  

Must not:

- Bypass global sovereignty rules  
- Disclose restricted values  

---

## 📡 `telemetryClient.ts`

Handles emission of:

- WebVitals  
- Navigation events  
- Dataset previews  
- Focus Mode context loads  
- Error taxonomies  
- A11y usage patterns  

All events must conform to:

- Telemetry schema (`web-utils-api-v11.json`)  
- No PII  
- No sensitive/tribal data  

---

# 🔐 4. Governance Rules

API utilities MUST:

- Reject unvalidated API responses  
- Never expose restricted coordinates or IDs  
- Enforce sovereignty masking  
- Retain CARE metadata across transforms  
- Apply STAC/DCAT/Fair metadata alignment  
- Produce PROV-O friendly provenance fields  

Governance violations → CI failure via:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `security_audit.yml`  

---

# ♿ 5. Accessibility Expectations

While these utilities don't render UI, they **feed A11y-sensitive components**:

- Temporal text must align with A11y formatters  
- Error messages must avoid ambiguity and be screen-reader safe  
- Response guards must ensure missing A11y metadata is surfaced, not hidden  

---

# 🧪 6. Testing Requirements

All utilities must have test coverage under:

~~~text
tests/unit/web/utils/api/**
tests/integration/web/utils/api/**
~~~

Tests must verify:

- Deterministic fetch behavior  
- Schema-validated responses  
- Temporal/spatial governance compliance  
- Provenance metadata retention  
- No leakage of restricted attributes  

---

# 🕰 7. Version History

| Version | Date       | Summary                                                                                 |
|--------:|------------|-----------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-28 | Full v11.2.2 upgrade; new emoji layout; governance, sovereignty, CARE, STAC/DCAT, v3 alignment. |
| v10.4.0 | 2025-11-15 | Early v10.4 API utils introduction.                                                    |
| v10.3.0 | 2025-11-13 | Initial API utility block.                                                              |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  

[⬅️ Back to Utils Overview](../README.md) · [🧭 Web Source Overview](../../README.md) · [🌐 Web Platform](../../../README.md)

</div>
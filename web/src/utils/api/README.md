---
title: "🔗 Kansas Frontier Matrix — API Response & Validation Utilities (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/utils/api/README.md"
version: "v10.4.1"
last_updated: "2025-11-15"
review_cycle: "Quarterly / Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.4.1/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.4.1/manifest.zip"
telemetry_ref: "../../../../releases/v10.4.1/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-utils-api-v1.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Architecture"
intent: "web-api-utilities"
fair_category: "F1-A1-I1-R1"
---

<div align="center">

# 🔗 **Kansas Frontier Matrix — API Response & Validation Utilities**  
`web/src/utils/api/README.md`

**Purpose:**  
Define the **frontend-side API validation, schema checking, error normalization,  
and FAIR+CARE metadata propagation utilities** used across the KFM React client.  
These modules ensure all API interactions (REST + GraphQL) are **safe, deterministic,  
schema-aligned, and MCP-compliant** before reaching UI components.

</div>

---

## 🧭 Overview

The `web/src/utils/api/` module contains **pure TypeScript utilities** responsible for:

- Validating responses from the FastAPI/GraphQL backend  
- Converting server errors → uniform UI-safe error objects  
- Enforcing JSON Schema constraints on all incoming payloads  
- Propagating FAIR + CARE metadata from API → UI  
- Guarding the app against malformed/unsafe data  
- Ensuring consistent error handling across all timeline/map/Focus Mode flows  

These utilities **never** perform actual network I/O.  
Network calls occur in `web/src/api/`, which relies on these utilities for correctness.

---

## 📂 Directory Layout

```

web/src/utils/api/
│
├── validateResponse.ts     # JSON Schema validation & API contract enforcement
├── normalizeError.ts       # Converts API errors → deterministic UI-safe structures
├── extractMeta.ts          # Pulls FAIR/CARE metadata from headers & JSON bodies
└── assertSchema.ts         # Low-level schema runtime checking (internal)

````

---

## 🧱 Module Descriptions

### 🧩 `validateResponse.ts`

Primary entry point for ensuring all API payloads are valid.

Performs:

- JSON Schema validation (STAC, DCAT, Graph, Focus Mode schemas)  
- Strict type validation of entities, relationships, and temporal fields  
- CARE checks (e.g., redacting restricted location fields when required)  
- Normalization of allowed-but-imperfect data (e.g., missing summaries → fallback)  

Example conceptual output:

```ts
interface Validated<T> {
  ok: true;
  data: T;
  meta: { license: string; provenance: string; sensitivity?: string };
}

interface Failed {
  ok: false;
  error: NormalizedError;
}
````

This ensures **all API flows are safe before entering React state**.

---

### 🧩 `normalizeError.ts`

Handles the messy part of real-world APIs.

Converts:

* FastAPI error bodies
* GraphQL errors
* Network failures
* Unexpected/malformed JSON
* CARE-denied access errors
* STAC/DCAT incompatibilities

Into a stable, deterministic shape:

```ts
interface NormalizedError {
  title: string;
  detail: string;
  status: number | null;
  retryable: boolean;
  faircare?: { restricted: boolean; reason?: string };
}
```

All UI components consume these normalized errors uniformly.

---

### 🧩 `extractMeta.ts`

Extracts FAIR + CARE metadata from:

* HTTP headers
* API JSON bodies
* STAC/DCAT fields
* Graph provenance nodes

Populates a canonical structure:

```ts
interface ApiMeta {
  license: string;
  source: string;
  provenance: string;
  confidence?: number;
  sensitivity?: "public" | "restricted";
}
```

Used by:

* Focus Mode v2 narrative cards
* Dataset info panels
* Layer metadata displays
* Provenance inspector modal

---

### 🧩 `assertSchema.ts`

Low-level schema-enforcement engine (internal use only).

Capabilities:

* Validate arbitrary JSON objects against provided schemas
* Provide MCP-aligned, human-readable failure messages
* Prevent UI components from ever receiving structural surprises
* Used by test harness for snapshot schema conformance

---

## 🧪 Testing Requirements

All utilities must have corresponding tests under:

```
tests/web/utils/api/*.test.ts
```

Tests MUST verify:

* Correct validation of all major schema types
* Safe rejection of malformed or tampered API payloads
* Preservation + propagation of FAIR/CARE metadata
* Deterministic error normalization across all failure modes
* Full handling of empty, partial, or mixed-format responses

---

## ⚙️ Development Standards

Modules under `utils/api` MUST:

* Be written in **TypeScript**
* Export only **pure functions** (no side effects)
* Never perform fetch/network calls
* Include full JSDoc docstrings
* Be fully compatible with STAC/DCAT/Story Node schemas
* Pass ESLint + Prettier + KFM Docs Lint
* Preserve or redact CARE-sensitive fields as required
* Integrate cleanly with upstream `web/src/api/` wrappers

---

## 🧭 Future Extensions (v10.5+)

Planned improvements:

* Full OpenAPI schema auto-binding for REST endpoints
* GraphQL introspection → TS schema generator
* Live schema hot-reload for streaming endpoints
* CARE-aware “contextual redaction policies” for sensitive entities
* Schema-based performance tracing for improved telemetry

---

## 🏁 Version History

| Version | Date       | Changes                                         |
| ------- | ---------- | ----------------------------------------------- |
| v10.4.1 | 2025-11-15 | Initial creation under KFM-MDP v10.4 standards. |

---

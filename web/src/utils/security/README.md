---
title: "KFM Web UI — Security Utilities (README)"
path: "web/src/utils/security/README.md"
version: "v1.0.0"
last_updated: "2025-12-26"
status: "draft"
doc_kind: "README"
license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v11.0.0"
dcat_profile: "KFM-DCAT v11.0.0"
prov_profile: "KFM-PROV v11.0.0"

governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:web:utils:security:readme:v1.0.0"
semantic_document_id: "kfm-web-utils-security-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:utils:security:readme:v1.0.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# KFM Web UI — Security Utilities

> **Purpose (required):** Define the **front-end (web) security utility patterns** used across the KFM UI to reduce XSS/data-leak risk, keep the UI aligned with **KFM architecture invariants**, and ensure governance signals (classification/redaction) are handled consistently in the client.

---

## 📘 Overview

### Purpose

This directory is the canonical home for **client-side security helpers** used by the KFM web UI (React + map/narrative surfaces). The goal is to centralize patterns that are easy to get wrong when duplicated across components (e.g., sanitization, safe URL handling, governance gating).

**Important:** Security enforcement (authorization, redaction/generalization) is **owned by the API boundary**. The UI implements **defense-in-depth** and **safe rendering**, but must not be treated as the source of truth.

### Scope

| In Scope | Out of Scope |
|---|---|
| UI-safe rendering helpers (escape/sanitize) | Server-side authorization logic |
| Safe handling of URLs, query params, route inputs | Graph (Neo4j) access, cypher queries, or DB drivers |
| Client-side “governance-aware” display guards (e.g., hide exact coords when flagged) | Any attempt to “downgrade” classification client-side |
| Utilities to reduce accidental leakage (logs, exports, copy-to-clipboard guards) | Infrastructure security (CSP headers, TLS, secrets storage) |

### Audience

- **Primary:** Front-end contributors working under `web/`
- **Secondary:** Security reviewers, governance reviewers, and API engineers validating boundary responsibilities

### Definitions

- Link (not confirmed in repo): `docs/glossary.md`
- Terms used in this doc include: **XSS**, **injection**, **open redirect**, **PII**, **classification**, **sensitivity**, **redaction/generalization**, **provenance**, **Focus Mode**.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline ordering + invariants | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical pipeline; UI must follow invariants |
| Governance baseline | `docs/governance/ROOT_GOVERNANCE.md` | Governance | Review triggers + publishing rules |
| Sovereignty policy | `docs/governance/SOVEREIGNTY.md` | Governance | Sensitive location rules and CARE alignment |
| Ethics baseline | `docs/governance/ETHICS.md` | Governance | High-risk content handling |
| API contracts | `src/server/contracts/**` *(or legacy)* | API | UI only consumes contract-stable payloads |
| UI schemas | `schemas/ui/**` | Frontend/Platform | Layer registry + UI config validation |
| Security docs (expected) | `docs/security/` | Security/Governance | Threat model + redaction guidance (not confirmed in repo) |

### Definition of done (for this document)

- [x] Front-matter complete and `path` matches file location
- [x] KFM invariants relevant to UI are stated (esp. no direct graph access)
- [x] Directory layout and intended module responsibilities described
- [ ] Actual filenames/functions updated to match what exists in `web/src/utils/security/` (once implemented)
- [ ] Security reviewer + governance reviewer sign-off if this folder introduces new render pathways

---

## 🗂️ Directory Layout

### This document

- `path`: `web/src/utils/security/README.md` (must match front-matter)

### Related repository paths (orientation)

| Area | Path | What lives here |
|---|---|---|
| UI (this layer) | `web/` | React/Map UI, Focus Mode UX |
| UI utilities | `web/src/utils/` | Shared helpers (this folder is security-specific) |
| API boundary | `src/server/` *(or `src/api/` — not confirmed in repo)* | Contracts, authorization, redaction/generalization |
| API contracts | `src/server/contracts/` | OpenAPI/GraphQL contract artifacts |
| Schemas | `schemas/` | JSON Schemas for UI configs, telemetry, contracts |
| Governed docs | `docs/` | Master guide, governance, standards |

### Expected file tree for this sub-area

> This is the **recommended** structure. Some files may not exist yet (**not confirmed in repo**).

~~~text
📁 web/
└── 📁 src/
    └── 📁 utils/
        └── 📁 security/
            ├── 📄 README.md                  # (this file)
            ├── 📄 sanitizeText.ts            # escape/sanitize untrusted strings (recommended)
            ├── 📄 sanitizeMarkdown.ts        # safe markdown rendering pipeline (recommended)
            ├── 📄 safeUrl.ts                 # safe href builders + allowlist enforcement (recommended)
            ├── 📄 safeQueryParams.ts         # parse/validate query params (recommended)
            ├── 📄 governanceGuards.ts        # classification/redaction-aware UI guards (recommended)
            ├── 📄 clipboardGuards.ts         # prevent copying restricted coordinates (optional)
            └── 📄 index.ts                   # consolidated exports (recommended)
~~~

---

## 🧭 Context

KFM’s canonical pipeline is intentionally staged:

**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → API boundary → UI → Story Nodes → Focus Mode**

The UI sits downstream of the API boundary and must treat all incoming content as **untrusted input**—including graph-derived metadata, Story Node text, and any user-generated or external content.

### Non‑negotiable UI invariants

1. **No UI direct-to-graph reads.** The client must never query Neo4j directly; all graph access happens through the API boundary.
2. **No secrets in the browser bundle.** Never embed credentials, Neo4j URIs, or private keys in `web/`.
3. **Defense‑in‑depth rendering.** UI must not create new XSS/HTML injection surfaces when displaying catalog/graph/narrative content.
4. **Governance-aware display.** UI must avoid exposing sensitive locations (e.g., exact coordinates) when content is flagged or redacted by policy.

### UI threat model (high-level)

- **XSS via narrative content** (Story Nodes, markdown, metadata descriptions)
- **XSS via data fields** (names/labels/attribution strings rendered into DOM)
- **Open redirects / URL injection** (unsafe link construction; user-controlled href)
- **Sensitive location leakage** (rendering exact coords, excessive precision, map interactions that reveal restricted geometry)
- **Accidental disclosure via logs/storage** (console logging payloads, storing restricted data in localStorage, exporting raw JSON)

This folder exists to make the safe path the easy path.

---

## 🧱 Architecture

### Boundary rule: the API enforces security; the UI enforces safe rendering

- **API boundary responsibilities (source of truth):**
  - authorize requests
  - apply redaction/generalization based on classification
  - return contract-stable payloads

- **UI responsibilities (defense-in-depth):**
  - safely render content without introducing injection
  - respect governance flags and avoid UI-only “workarounds”
  - avoid caching/logging restricted details

### Contract expectations (example only)

> The exact names/types are **not confirmed in repo**. This illustrates the pattern the UI expects from the API.

~~~ts
// Example governance envelope the UI can consume.
// NOT CONFIRMED IN REPO: shape and field names are illustrative only.
export type GovernanceEnvelope = {
  sensitivity?: string;                 // e.g., "public" | "restricted"
  classification?: string;              // e.g., "open" | "internal" | "restricted"
  redaction?: {
    applied?: boolean;
    method?: string;                    // e.g., "coarse" | "masked" | "none"
    notice?: string;                    // user-visible explanation
  };
};
~~~

### Usage patterns (illustrative)

~~~ts
// NOT CONFIRMED IN REPO: function names are illustrative.
import { sanitizeText, safeExternalHref, shouldRenderGeometry } from "./index";

// 1) Safe text rendering
const title = sanitizeText(apiRecord.title);

// 2) Safe external links (avoid open redirects / javascript: URLs)
const href = safeExternalHref(apiRecord.attributionUrl);

// 3) Governance-aware rendering decisions
if (!shouldRenderGeometry(apiRecord.governance)) {
  // Render a redaction notice, not the geometry
}
~~~

### Rules for adding new utilities here

- **Pure + deterministic:** Prefer small, side‑effect-free functions.
- **Browser-safe:** Do not import server-only libraries or Node-only modules.
- **No “HTML passthrough”:** Avoid helpers that encourage `dangerouslySetInnerHTML`.
- **Explicit allowlists:** If sanitizing HTML/markdown, use allowlists and document them.
- **Governance first:** Never “reconstruct” redacted data client-side.
- **Testable:** New helpers should have unit tests (where the repo supports them).

---

## 🧪 Validation & CI/CD

### Validation steps (recommended)

- [ ] Typecheck/lint pass for `web/`
- [ ] Unit tests for security utilities (if test runner exists)
- [ ] Link/reference checks for this README (if doc lint exists)
- [ ] **Forbidden-string scan for web bundle** (e.g., ensure no `neo4j://` or driver imports)
- [ ] Secrets scan (no tokens/keys committed)
- [ ] If new rendering pathways are added: security review + governance review

### Reproduction

> Commands below are **placeholders** (not confirmed in repo). Replace with repo-accurate scripts.

~~~bash
# NOT CONFIRMED IN REPO — replace with actual tooling
# pnpm -C web lint
# pnpm -C web test
# pnpm -C web typecheck

# Optional CI-style check (concept):
# rg -n "neo4j://|@neo4j|cypher|neo4j-driver" web/
~~~

### Telemetry signals (optional, if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| `focus_mode_redaction_notice_shown` | UI event | `docs/telemetry/` + `schemas/telemetry/` (if present) |
| `ui_render_blocked_by_classification` | UI guard | same |
| `external_link_blocked` | safeUrl helper | same |

---

## ⚖ FAIR+CARE & Governance

- Treat **location-bearing content** as potentially sensitive by default.
- If a UI change:
  - increases coordinate precision,
  - adds a new export/copy pathway,
  - introduces a new markdown/HTML render surface,
  - or adds a new map layer that can reveal sensitive areas by interaction/zoom,  
  then it should trigger **governance review** and likely **security review**.

- Do not use UI logic to “downgrade” classification. If the UI believes it has received unsafe data, the correct action is to:
  - block rendering, and/or
  - show a redaction notice, and/or
  - report the issue for API-boundary remediation.

### AI usage constraints

- Do not use AI to infer sensitive locations (directly or indirectly).
- Any narrative or Focus Mode content must remain provenance-linked and labeled appropriately at the product layer; UI security helpers may support safe display, but must not fabricate sources.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-26 | Initial security utilities README scaffold (structure + invariants + recommended layout) | TBD |

---

### Footer refs

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`
- Security docs (expected): `docs/security/` (not confirmed in repo)

---


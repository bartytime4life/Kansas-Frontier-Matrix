---
title: "🧩 Kansas Frontier Matrix — Story Utilities Module (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/features/story/utils/README.md"
version: "v10.3.2"
last_updated: "2025-11-14"
review_cycle: "Quarterly / Autonomous + FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.3.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.3.2/manifest.zip"
telemetry_ref: "../../../../releases/v10.3.2/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-story-utils-v1.json"
governance_ref: "../../../../docs/standards/governance/DATA-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧩 **Kansas Frontier Matrix — Story Utilities Module**  
`web/src/features/story/utils/README.md`

**Purpose:**  
Provide **pure, deterministic, FAIR+CARE-aligned utility functions** that power the Story Nodes subsystem.  
These utilities perform narrative formatting, Markdown → HTML transformation, governance redaction, link routing, provenance handling, and A11y-safe rendering for the KFM Web Platform.

<img alt="MCP" src="https://img.shields.io/badge/Docs-MCP_v6.3-blue" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Story_Compliant-orange" />
<img alt="Status" src="https://img.shields.io/badge/Status-Stable-brightgreen" />
<img alt="License" src="https://img.shields.io/badge/License-MIT-green" />

</div>

---

## 📘 Overview

The Story Utilities module contains **all shared logic** used by:

- `StoryCard`
- `useStory`
- `story-service.ts`
- Timeline & Map synchronization helpers
- Focus Mode narrative overlays
- Telemetry reporters (web-story-v1)

Utilities must be:

- **Pure** (no side effects)
- **Deterministic**
- **FAIR+CARE-enforced**
- **A11y-compatible**
- **TypeScript-strict**
- **Schema-backed** (`story-node.schema.json`)

---

## 🗂️ Directory Layout

~~~~~text
web/src/features/story/utils/
├── README.md                 # This file
├── formatters.ts             # Markdown → HTML, link routing, media handling
├── governance.ts             # CARE filters, sovereignty masking, redaction logic
├── provenance.ts             # Story-level lineage + citation mapping
└── types.ts                  # Shared types for utils
~~~~~

---

## 🧩 Utility Responsibilities

### 1. `formatters.ts` — Narrative & Link Formatting

Handles rendering concerns:

- Markdown → sanitized HTML  
- Preservation of headings, lists, footnotes  
- Inline link transformation:
  - `story:xxxx` → in-app Story Node route  
  - `place:xxxx` → map highlight  
  - `event:xxxx` → Focus Mode event focus
- Image embedding rules:
  - Required `alt` text (WCAG)
  - Support for captions via `figcaption`
- Media validation against governance rules

**Example:**

~~~~~text
import { sanitize } from "./sanitize";

export function renderMarkdown(md: string): string {
  const html = marked(md, { gfm: true });
  return sanitize(html); // strips unsafe tags, scripts, iframes
}
~~~~~

---

### 2. `governance.ts` — CARE + Sovereignty Rules

Ensures Story Node visibility follows FAIR+CARE and KFM Governance Charter.

Enforced policies:

- CARE Tag Behavior:
  - `public` → render fully  
  - `restricted` → mask narrative, show summary only  
  - `sensitive` → hide node unless user has clearance  
- Sovereignty protections:
  - Hide sensitive geometries inside tribal lands not approved  
  - Mask specific text segments flagged in node metadata  
- License boundaries (CC-BY vs restricted docs/assets)

**Example:**

~~~~~text
export function canDisplayStory(node, userRoles) {
  if (node.governance?.care_tag === "sensitive") return false;
  if (node.governance?.care_tag === "restricted" && !userRoles.includes("editor"))
    return false;
  return true;
}
~~~~~

---

### 3. `provenance.ts` — Lineage, Citations & Evidence Mapping

Links Story Nodes to:

- Evidence datasets (STAC items, collections, assets)  
- Linked entities (event, person, place IDs)  
- Governance ledger entries  
- AI citation tokens from Focus Mode

Generates consistent provenance chips:

```

📄 Kansas Historical Society — Document #1281
🛰 Landsat Scene LC08_29/030 (Cloud 12%)
🏛 Governance: CARE Tag = public

```

Enables Focus Mode “Why this story?” explanations.

---

## 🧠 Key Concepts

### 🔒 Deterministic Story Rendering  
Utilities ensure that given the same story-node payload, rendering is *bitwise identical*, supporting reproducible history visualization.

### ♻ FAIR+CARE Continuous Enforcement  
Governance filters run **every time** a Story Node is rendered, not just when it is fetched.

### 📡 Telemetry-Aware  
Utilities send structured context to Telemetry:

- unlabeled images  
- links to sensitive content  
- rendering latency  
- CARE tag outcomes  

Telemetry is stored in:

~~~~~text
../../../../releases/v10.3.2/focus-telemetry.json
~~~~~

---

## 📚 Utility Examples

### Example — Convert Story Node Markdown to HTML

~~~~~text
import { renderMarkdown } from "./formatters";

const html = renderMarkdown(node.narrative.body);
~~~~~

### Example — Apply CARE-Based Visibility

~~~~~text
import { canDisplayStory } from "./governance";

if (!canDisplayStory(node, user.roles)) return null;
~~~~~

### Example — Build Provenance Chips

~~~~~text
import { buildProvenance } from "./provenance";

const chips = buildProvenance(node);
~~~~~

---

## ✔ CI / Validation Requirements

| Area            | Validator / Workflow                              |
|-----------------|---------------------------------------------------|
| Schema          | schema-validate.yml (story-node.schema.json)      |
| Governance      | faircare-validate.yml                             |
| Telemetry       | telemetry-export.yml                              |
| Accessibility   | accessibility_scan.yml                            |
| Security        | CodeQL + Trivy                                    |
| Documentation   | docs-lint.yml                                     |

---

## 🕰️ Version History

| Version | Date       | Author       | Summary |
|--------:|------------|--------------|---------|
| v10.3.2 | 2025-11-14 | `@kfm-web`   | Upgraded utilities to FAIR+CARE v10.3, added sovereignty masking, provenance chip builder, and story-node-safe markdown pipeline. |
| v9.9.0  | 2025-11-08 | `@kfm-web`   | Initial utilities for Story Node rendering and governance filtering. |

---

<div align="center">

**Kansas Frontier Matrix — Story Utilities**  
📖 Narrative Integrity · 🔐 FAIR+CARE Governance · ♿ Accessible & Ethical Rendering  
© 2025 Kansas Frontier Matrix — MIT License  

[Back to Story Feature](../README.md) · [Governance Charter](../../../docs/standards/governance/DATA-GOVERNANCE.md)

</div>

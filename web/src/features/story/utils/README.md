---
title: "🧰 Story Utilities — Markdown Rendering, Governance & Narrative Tools (KFM-Ready)"
path: "web/src/features/story/utils/README.md"
version: "v9.9.0"
last_updated: "2025-11-08"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v9.9.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v9.9.0/manifest.zip"
telemetry_ref: "../../../../../releases/v9.9.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/web-story-utils-v1.json"
governance_ref: "../../../../../docs/standards/governance/DATA-GOVERNANCE.md"
license: "MIT"
---

<div align="center">

# 🧰 **Story Utilities — Markdown Rendering, Governance & Narrative Tools**  
`web/src/features/story/utils/README.md`

**Purpose:**  
Provide **reusable utility functions** for KFM’s **Story Node** system — handling markdown conversion, content formatting, ethical visibility (FAIR+CARE), and telemetry logging for narrative interactions.  
This toolkit supports **story-card rendering**, **Focus Mode narrative links**, and **content validation pipelines**, aligned with **MCP-DL v6.3** and **FAIR+CARE governance**.

[![Docs · MCP](https://img.shields.io/badge/Docs·MCP-v6.3-blue)](../../../../../docs/)
[![License](https://img.shields.io/badge/License-MIT-green)](../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Validated-orange)](../../../../../docs/standards/)
[![Status](https://img.shields.io/badge/Status-Stable-brightgreen)](#)

</div>

---

## 📘 Overview

These utilities form the **core infrastructure** for transforming, validating, and ethically rendering story content.  
They are imported by `story-card.tsx`, `story-service.ts`, and `focus-panel.tsx` to ensure **consistent display and ethical control** of narrative text.

**Key Responsibilities**
- 📝 Convert story markdown to accessible HTML.  
- 🔗 Resolve internal and external entity links.  
- ⚖️ Enforce FAIR+CARE visibility (CARE tags, provenance).  
- 📊 Log telemetry events for user interactions and accessibility metrics.  

---

## 🗂️ Directory Layout

```plaintext
web/
└─ src/
   └─ features/
      └─ story/
         └─ utils/
            README.md            # This file — story utilities overview
            formatters.ts        # Markdown → HTML & hyperlink resolver
            governance.ts        # CARE tagging and visibility enforcement
            telemetry.ts         # Narrative view logging
            a11y-utils.ts        # Accessibility helpers (focus, region labels)
```

---

## 📝 Markdown Renderer (`formatters.ts`)

Converts story text from Markdown or HTML-safe formats to accessible components.  
Supports **inline media**, **citations**, **focus links**, and **internal references**.

```ts
import { marked } from "marked";

export function renderMarkdown(markdown: string): string {
  marked.setOptions({
    breaks: true,
    headerIds: false,
    mangle: false
  });
  return marked.parse(markdown);
}
```

### Internal Entity Links

Automatically converts links like `[Fort Larned](story:fort-larned-1859)`  
into in-app navigation events:

```ts
export function resolveStoryLinks(html: string): string {
  return html.replace(/href="story:(.*?)"/g, 'href="#" data-story-id="$1" class="story-link"');
}
```

> *Focus Mode Integration:*  
> Click handlers detect `.story-link` and trigger `kfm:focus:select` with target ID.

---

## ⚖️ Governance Enforcement (`governance.ts`)

Controls story visibility according to FAIR+CARE tags.  
Ensures sensitive or restricted narratives are not rendered without consent.

```ts
export function enforceCareTag(node: any): string | null {
  const tag = node.governance?.care_tag ?? "public";
  if (tag === "sensitive") return null;
  if (tag === "restricted") {
    return `⚠ Restricted narrative: content hidden per FAIR+CARE policy.`;
  }
  return node.narrative?.body ?? "";
}
```

**CARE Tag Behavior**

| Tag | Description | UI Rendering |
|------|-------------|--------------|
| `public` | Open access narrative | Full render |
| `restricted` | License or ethical restriction | Text masked or summarized |
| `sensitive` | Protected heritage/cultural info | Hidden with warning |

---

## 📊 Telemetry (`telemetry.ts`)

Logs story-related events for analytics, accessibility audits, and model evaluation.

```ts
export function logStoryView(storyId: string, userRole = "public") {
  const log = {
    event: "story-view",
    story_id: storyId,
    timestamp: new Date().toISOString(),
    user_role: userRole
  };
  console.debug("[KFM StoryTelemetry]", log);
  fetch("/api/telemetry", { method: "POST", body: JSON.stringify(log) });
}
```

**Telemetry Schema:**  
`schemas/telemetry/web-story-utils-v1.json`

| Field | Type | Description |
|--------|------|-------------|
| `event` | string | Event type (`story-view`, `story-link-click`) |
| `story_id` | string | Unique story node identifier |
| `timestamp` | string | ISO timestamp |
| `user_role` | string | FAIR+CARE role classification |
| `latency_ms` | number | Optional performance timing |

---

## ♿ Accessibility Utilities (`a11y-utils.ts`)

Provides WAI-ARIA and keyboard enhancements for story exploration.

```ts
export function focusRegion(id: string) {
  const region = document.getElementById(id);
  if (region) region.focus({ preventScroll: false });
}

export function announceUpdate(text: string) {
  const liveRegion = document.getElementById("aria-live-region");
  if (liveRegion) {
    liveRegion.textContent = text;
    liveRegion.setAttribute("aria-live", "polite");
  }
}
```

**Accessibility Targets**
- Screen readers detect story updates (`aria-live="polite"`).  
- Keyboard shortcuts (`←`/`→`/`Esc`) navigable between stories.  
- Focus rings and skip links included via `a11y-utils.ts`.

---

## 🧩 Integration Example

```tsx
import { renderMarkdown, resolveStoryLinks } from './formatters';
import { enforceCareTag, logStoryView } from './governance';

export function StoryRenderer({ story }) {
  const content = enforceCareTag(story);
  if (!content) return <p>⚠ Hidden per CARE tag.</p>;
  const html = resolveStoryLinks(renderMarkdown(content));
  React.useEffect(() => logStoryView(story.id), [story.id]);
  return <section dangerouslySetInnerHTML={{ __html: html }} />;
}
```

---

## 🧠 Governance Workflow

1. `story-node` schema defines `governance.care_tag`.  
2. Renderer applies filters from `governance.ts`.  
3. Telemetry logs each view, tracking access frequency by tag.  
4. FAIR+CARE council audits logs for misuse or visibility issues.  

---

## 🧾 Internal Citation

```text
Kansas Frontier Matrix (2025). Story Utilities — Markdown Rendering, Governance & Narrative Tools (v9.9.0).
Provides FAIR+CARE compliant utilities for transforming and ethically displaying story narratives within KFM’s interactive web interface.
```

---

## 🕰️ Version History

| Version | Date       | Author | Summary |
|--------:|------------|--------|----------|
| v9.9.0 | 2025-11-08 | `@kfm-web` | Added markdown renderer, CARE governance filter, telemetry, and a11y utils. |

---

<div align="center">

**Kansas Frontier Matrix**  
*Narrative Integrity × FAIR+CARE Governance × Accessible Storytelling*  
© 2025 Kansas Frontier Matrix · Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Story Docs](../README.md) · [Web Features Index](../../README.md) · [Governance Charter](../../../../../docs/standards/governance/DATA-GOVERNANCE.md)

</div>


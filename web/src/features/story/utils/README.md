
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

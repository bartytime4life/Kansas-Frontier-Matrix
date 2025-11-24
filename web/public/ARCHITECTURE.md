---
title: "🗂️ Kansas Frontier Matrix — Web Public Assets Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/public/ARCHITECTURE.md"
version: "v11.0.0"
last_updated: "2025-11-25"
release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · FAIR+CARE Council Oversight"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-sha>"
doc_uuid: "urn:kfm:web-public-architecture-v11.0.0"
semantic_document_id: "kfm-doc-web-public-architecture"
doc_kind: "Architecture"
intent: "web-public-assets-architecture"

sbom_ref: "../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../releases/v11.0.0/manifest.zip"

telemetry_ref: "../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/web-public-architecture-v4.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT / CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0"
ontology_protocol_version: "KFM-OP v11.0"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-P · Public-Safe"
sensitivity_level: "Low"
indigenous_data_flag: false
risk_category: "Low"
public_benefit_level: "High"

accessibility_compliance: "WCAG 2.1 AA"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative-additions"
  - "fabricated-historical-content"

machine_extractable: true
immutability_status: "version-pinned"
ttl_policy: "12 months"
sunset_policy: "Superseded upon next major update"
jurisdiction: "United States · Kansas"
classification: "Public Document"
---

<div align="center">

# 🗂️ **Kansas Frontier Matrix — Web Public Assets Architecture (v11)**  
`web/public/ARCHITECTURE.md`

**Purpose:**  
Define the **complete static-assets architecture** for `web/public/**` —  
including SPA shell, PWA metadata, icons, images, and public-safe governance rules.  
All assets follow **KFM-MDP v11**, **FAIR+CARE-P**, accessibility, sustainability, and  
telemetry v4 compliance.

</div>

---

# 📘 Overview

`web/public/**` contains all **immutable, pre-compiled, CDN-served assets**:

- `index.html` — SPA shell  
- `manifest.json` — PWA metadata  
- Icons — PWA + platform branding  
- Images — non-sensitive UI artwork, map thumbnails, hero images  
- `robots.txt` — crawler rules  
- `favicon.ico` — primary site icon  

In KFM v11, **public assets must be**:

- License-clear (MIT / CC-BY)  
- Accessible (alt text, ARIA patterns)  
- Public-safe per **CARE-P**  
- Energy/carbon-profiled (telemetry v4)  
- Provenance-tracked (checksum + ledger)  

---

# 🗂️ Directory Layout (v11 canonical)

Directory rendered with **inline comments**, safe `~~~~text` fence:

~~~~text
web/public/                          # Static, CDN-served public assets (no build step)
│
├── ARCHITECTURE.md                  # This architecture document (v11)
├── README.md                        # Public-assets overview + governance notes
│
├── index.html                       # SPA shell + React mount point (#root)
│
├── manifest.json                    # PWA manifest (name, theme, icons, scope)
├── robots.txt                       # Search engine crawl directives
├── favicon.ico                      # Primary favicon (32×32)
│
├── icons/                           # PWA + platform iconography (FAIR+CARE-P safe)
│   ├── icon-192.png                 # PWA install icon (192×192)
│   ├── icon-512.png                 # PWA install icon (512×512)
│   ├── maskable-512.png             # Maskable icon for Android install surfaces
│   └── metadata.json                # Checksums · licenses · a11y tags · provenance
│
└── images/                          # Public-safe imagery for UI (not sensitive)
    ├── logo-full.png                # Full KFM brandmark
    ├── logo-mark.png                # Compact logo mark
    ├── hero/                        # Hero images for landing/splash sections
    ├── maps/                        # Simple/low-sensitivity map thumbnails
    ├── ui/                          # UI illustrations · onboarding visuals
    └── metadata.json                # FAIR+CARE-P annotations · license · SHA-256
~~~~

All assets are **immutable** and must maintain **public-safety guarantees**.

---

# 🌐 Architectural Role

### 1. SPA Bootstrap (index.html)

- Defines `<meta>` tags for accessibility, color scheme, and theme-color.  
- Provides React mount root (`<div id="root">`).  
- Loads build output from Vite.  
- Must **never** embed secrets or internal URLs.

### 2. PWA Infrastructure

`manifest.json` defines:

- App name, icons, orientation  
- Theme and background color  
- Display mode (`standalone`)  
- Start URL and scope  
- Maskable icons for adaptive systems  

Icons must meet:

- Square format  
- Required PWA sizes: **192×192**, **512×512**  
- High contrast and WCAG-safe palette  
- Public-generalizable symbolism (no restricted cultural motifs)

### 3. Public Imagery

Images are:

- Public-safe  
- License-compliant  
- Accessibility-audited  
- Vetted for CARE-P compliance  
- Energy-optimized (WebP/AVIF preferred)  

Governance rules prohibit:

- Sensitive heritage photography  
- Unreviewed Indigenous cultural imagery  
- Exact depictions of restricted sites  

---

# ♿ Accessibility Requirements (WCAG 2.1 AA)

**All images must include:**

- `alt` text describing meaning or purpose  
- Or `alt=""` if decorative and marked via CSS  

**Icons**:

- Decorative icons: hidden via ARIA  
- Semantic icons: paired with visible text or ARIA label  

**Theme Color Considerations**:

- `manifest.json` theme color MAY NOT reduce contrast  
- Must align with the Web UI’s high-contrast modes  

---

# ⚖️ Governance · FAIR+CARE-P Model

CARE-P (Public) rules:

- No sensitive Indigenous imagery  
- No exact coordinates of protected places  
- Avoid culturally significant iconography unless approved  
- All assets must include:  
  - `license`  
  - `checksum_sha256`  
  - `alt_text`  
  - `care_label: "Public"`  
  - `sensitive: false`  

Governance metadata lives in:

~~~~text
web/public/icons/metadata.json
web/public/images/metadata.json
~~~~

Governance ledger references are appended to:

~~~~text
docs/reports/audit/web_public_assets.json
~~~~

---

# 🌿 Sustainability & Telemetry v4

Telemetry collects (non-PII):

- **Bytes served** per asset  
- **Estimated energy (Wh)** using energy schema v2  
- **CO₂ (gCO₂e)** using carbon schema v2  
- **Cache hit rate**  
- **Format efficiency** scoring (PNG → WebP/AVIF)  
- **A11y usage patterns**

Telemetry exported to:

~~~~text
../../releases/v11.0.0/focus-telemetry.json
docs/reports/telemetry/web_public_assets/*.json
~~~~

Performance requirements (v11):

| Metric | Target |
|--------|--------|
| Avg image weight | ≤ 350 KB |
| Energy render cost | ≤ 0.03 Wh |
| Carbon per view | ≤ 0.04 gCO₂e |
| RE100 hosting compliance | Required |
| Lighthouse Perf | ≥ 95 |

---

# 🔒 Privacy & Security

- All public files are **world-readable**, must contain no sensitive content.  
- No secrets or internal environment keys allowed in any asset.  
- Filenames must not encode sensitive concepts (e.g., “grave-site.png”).  
- `robots.txt` must reflect FAIR+CARE governance decisions.

---

# 🧪 CI/CD Validation

CI workflows enforce:

- Required fields in asset metadata:  
  - `checksum_sha256`  
  - `license`  
  - `alt_text`  
  - `faircare_label`  
- Accessibility scan (Lighthouse + axe)  
- Telemetry schema validation  
- Broken-link scan for images/icons  
- Cache-immUtability checks  

Failures block release.

---

# 🕰 Version History

| Version | Date | Summary |
|--------:|------|---------|
| **v11.0.0** | 2025-11-25 | Fully upgraded to v11; telemetry v4; sustainability v2; new metadata schema; FAIR+CARE-P enforcement; stable directory layout. |
| v10.4.0 | 2025-11-15 | Initial public-assets architecture for v10.4. |
| v10.0.0 | 2025-11-09 | First organized public asset spec. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix**  
MIT / CC-BY 4.0 · FAIR+CARE-P Compliant · Diamond⁹ Ω / Crown∞Ω  
KFM-MDP v11 · KFM-OP v11 · MCP-DL v6.3

</div>
---
title: "🎥 Kansas Frontier Matrix — Accessible Media & Time-Based Content (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/accessibility/patterns/media.md"
version: "v10.4.1"
last_updated: "2025-11-16"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/a11y-media-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.3"
status: "Active / Enforced"
doc_kind: "Pattern"
intent: "a11y-media"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
sensitivity_level: "Moderate"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM Accessibility Council · FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "docs/accessibility/patterns/media.md@v10.0.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "CreativeWork"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
json_schema_ref: "../../../schemas/json/a11y-media.schema.json"
shape_schema_ref: "../../../schemas/shacl/a11y-media-shape.ttl"
doc_uuid: "urn:kfm:doc:a11y-media-v10.4.1"
semantic_document_id: "kfm-doc-a11y-media"
event_source_id: "ledger:docs/accessibility/patterns/media.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified historical claims"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Public Document"
jurisdiction: "United States / Kansas"
role: "a11y-pattern-media"
lifecycle_stage: "stable"
ttl_policy: "Quarterly review"
sunset_policy: "Superseded upon next media accessibility standard update"
---

<div align="center">

# 🎥 **Kansas Frontier Matrix — Accessible Media & Time-Based Content**  
`docs/accessibility/patterns/media.md`

**Purpose:**  
Define standards and validation procedures for accessible video, audio, livestream, and time-based media across the Kansas Frontier Matrix (KFM).  
Ensures all media—historical recordings, oral histories, scientific visualizations, AI-narrated sequences, and immersive playback—meet **WCAG 2.1 AA**, **XAUR**, **ISO 9241-210**, and **FAIR+CARE** ethical communication rules.

![Badge Docs](https://img.shields.io/badge/Docs-MCP_v6.3-blue)
![Badge FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)
![Badge License](https://img.shields.io/badge/License-CC--BY%204.0-green)
![Badge Status](https://img.shields.io/badge/Status-Stable-success)

</div>

---

## 📘 Overview

Time-based media in KFM includes:

- Oral histories and interviews  
- Audiovisual map playback  
- Recorded demonstration videos  
- Field narration and ecological audio  
- Livestreamed workshops and webinars  
- Cesium/MapLibre time-dynamic visualizations  
- AI-generated narrative sequences (Focus Mode v2.5+)  

This pattern ensures that these media assets are:

- Fully accessible for hearing, vision, and cognitive needs  
- Ethically contextualized, with explicit cultural consent metadata  
- Machine-extractable for FAIR data alignment  
- Compatible across browsers, devices, and assistive technologies  

---

## 🗂️ Directory Context

```text
docs/accessibility/
│
├── README.md
├── testing-guide.md
├── tokens.md
└── patterns/
    ├── media.md                      # This file
    ├── navigation.md
    ├── notifications.md
    ├── network-infrastructure.md
    ├── minerals-energy.md
    ├── microbiology-ecosystem-health.md
    ├── parks-conservation.md
    ├── planetarium-3d.md
    ├── pollinators-ecosystem-services.md
    ├── prairie-restoration.md
    ├── rail-transit.md
    ├── soil-health.md
    ├── space-remote-sensing.md
    ├── system-controls.md
    ├── tables.md
    ├── telemetry-streams.md
    ├── testing-validation.md
    ├── tooltips.md
    ├── transportation-mobility.md
    ├── urban-planning.md
    ├── vehicle-logistics.md
    └── wildlife-tracking.md
```

---

## 🧩 Accessibility Requirements

| Requirement            | Description                                                             | WCAG / Standard |
|------------------------|-------------------------------------------------------------------------|------------------|
| Captions               | All prerecorded videos include synced captions.                         | WCAG 1.2.2       |
| Live Captions          | Live streams must provide real-time captions/transcripts.               | WCAG 1.2.4       |
| Audio Descriptions     | Visual events narrated for blind/low-vision users.                      | WCAG 1.2.5       |
| Transcripts            | All audio/video require transcripts in HTML or downloadable formats.    | WCAG 1.2.1       |
| Media Controls         | Must be fully keyboard-operable.                                        | WCAG 2.1.1       |
| Auto-Play Restriction  | No media begins playback without user action.                           | WCAG 2.2.2       |
| Cultural Consent       | Sensitive/Indigenous content requires FAIR+CARE consent attribution.    | CARE A-2         |
| Flash/Light Safety     | No flashes >3Hz; XR scenes must disable dangerous motion by default.    | WCAG 2.3.1       |

---

## 🧭 Example Implementation

~~~html
<figure
  role="group"
  aria-labelledby="media-title"
  aria-describedby="media-description"
  data-fair-consent="approved"
  data-ethics-reviewed="true"
>
  <video
    controls
    preload="metadata"
    aria-describedby="media-description"
    aria-label="Oral history interview with community elder"
    poster="/images/thumbnails/interview.jpg"
  >
    <source src="/media/interview.mp4" type="video/mp4" />
    <track
      src="/captions/interview_en.vtt"
      kind="captions"
      srclang="en"
      label="English"
      default
    />
  </video>

  <figcaption id="media-title">Oral History Interview</figcaption>

  <p id="media-description">
    Recorded in 2024. Includes transcript, bilingual captions, and FAIR+CARE cultural consent approval.
  </p>
</figure>
~~~

### Implementation Rules

- Always include `<track>` for captions; provide multiple language tracks where available.  
- Provide video poster images for orientation and assistive navigation.  
- Use `aria-label` and `aria-describedby` to link media to contextual metadata.  
- Media **must not autoplay** without explicit user consent.  
- Sensitive content must be labeled with `data-fair-consent`, `data-sensitive`, and `data-ethics-reviewed`.  

---

## 🎨 Design Tokens

| Token                | Description                         | Example |
|----------------------|-------------------------------------|---------|
| media.bg.color       | Player background                   | #212121 |
| media.focus.color    | Focus outline                       | #FFD54F |
| media.caption.color  | Caption text color                  | #FFFFFF |
| media.caption.bg     | Caption background overlay          | #000000AA |
| media.control.color  | Control icon/text color             | #FAFAFA |
| media.progress.color | Timeline/progress bar color         | #4FC3F7 |

---

## 🧾 FAIR+CARE Consent Metadata

Attributes applied to `<video>`, `<audio>`, `<figure>`, or data containers:

| Attribute                   | Description                                                    |
|----------------------------|----------------------------------------------------------------|
| `data-fair-consent`        | `"approved" | "conditional" | "denied"` — governs playback    |
| `data-origin`              | Culturally/governance-linked source label                      |
| `data-ethics-reviewed`     | `"true"` when FAIR+CARE review completed                        |
| `data-sensitive`           | `"true"` for sacred or restricted media                         |
| `data-protected-until`     | ISO date when restriction expires                              |

### Example

~~~html
<video
  controls
  data-fair-consent="approved"
  data-origin="tribal-recording"
  data-ethics-reviewed="true"
  data-sensitive="true"
>
  ...
</video>
~~~

---

## 🧪 Validation Workflows

| Tool             | Scope                                      | Output                                        |
|------------------|---------------------------------------------|-----------------------------------------------|
| axe-core         | Media control accessibility                 | a11y_media.json                               |
| Lighthouse CI    | Captions, transcripts, and playback safety  | lighthouse_media.json                         |
| FFmpeg Metadata  | Frame-level and audio metadata extraction   | metadata_scan.json                            |
| jest-axe         | Component-level media UI tests              | a11y_media_components.json                    |
| Manual QA        | Screen reader and keyboard playback checks  | FAIR+CARE Council logs                        |

Validation ensures:

- Caption tracks load correctly and sync to dialogue.  
- No autoplay violations occur across devices.  
- Cultural/ethical metadata displayed and respected in UI.  
- All media is reachable and operable with keyboard alone.  

---

## ⚖️ FAIR+CARE Integration

| Principle           | Implementation                                                                     |
|---------------------|-------------------------------------------------------------------------------------|
| Collective Benefit  | Media used to educate, preserve culture, and democratize scientific information.   |
| Authority to Control| Consent metadata determines visibility and playback availability.                  |
| Responsibility      | All media logged in Governance Ledger; transcripts archived for reproducibility.   |
| Ethics              | Content reviewed for cultural sensitivity, trauma-informed narration, and accuracy.|

---

## 🕰️ Version History

| Version | Date       | Author                 | Summary                                                                                   |
|--------:|------------|------------------------|-------------------------------------------------------------------------------------------|
| v10.4.1 | 2025-11-16 | Accessibility Council  | Upgraded to KFM-MDP v10.4.3; expanded FAIR+CARE metadata, added XR safety rules, ensured one-box formatting. |
| v10.0.0 | 2025-11-10 | FAIR+CARE A11y Council | Initial media accessibility standard with captioning, consent, and validation workflows.  |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Developed under **Master Coder Protocol v6.3** · Verified by **FAIR+CARE Council**  
[⬅ Back to Navigation](navigation.md) · [Back to A11y Patterns Index](README.md)

</div>
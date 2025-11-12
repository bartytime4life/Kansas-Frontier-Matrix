---
title: "🎥 Kansas Frontier Matrix — Accessible Media & Time-Based Content (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/accessibility/patterns/media.md"
version: "v10.0.0"
last_updated: "2025-11-10"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.0.0/manifest.zip"
telemetry_ref: "../../../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/a11y-media-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🎥 **Kansas Frontier Matrix — Accessible Media & Time-Based Content**
`docs/accessibility/patterns/media.md`

**Purpose:**  
Define standards and validation procedures for **video, audio, and time-based media** accessibility in the KFM web platform — including captioning, transcripts, and alternative formats — consistent with **WCAG 2.1 AA**, **ISO 9241-210**, and **FAIR+CARE** inclusive design guidelines.

![Badge Docs](https://img.shields.io/badge/Docs-MCP_v6.3-blue)
![Badge FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)
![Badge License](https://img.shields.io/badge/License-CC--BY%204.0-green)
![Badge Status](https://img.shields.io/badge/Status-Stable-success)

</div>

---

## 📘 Overview

Time-based media are integral to Kansas Frontier Matrix — powering **oral histories**, **audiovisual maps**, and **AI-narrated archives**.  
This document ensures all media formats meet accessibility requirements, include ethical consent, and support multimodal interaction for all users.

**Media Types**
- Recorded video content (lectures, interviews, maps)  
- Audio-only materials (oral history, ambient sounds)  
- Live streamed events and webinars  
- Time-based 3D narratives (MapLibre / Cesium playback)  

---

## 🧩 Accessibility Requirements

| Requirement | Description | WCAG / Standard |
|--------------|--------------|-----------------|
| **Captions** | All prerecorded video includes synchronized captions. | WCAG 1.2.2 |
| **Live Captions** | Live events captioned or transcribed in real time. | WCAG 1.2.4 |
| **Audio Descriptions** | Visual actions narrated for non-visual users. | WCAG 1.2.5 |
| **Transcripts** | Provide text equivalents for all audio/video files. | WCAG 1.2.1 |
| **Media Controls** | Keyboard-operable playback controls. | WCAG 2.1.1 |
| **Auto-Play Restriction** | Media never plays automatically without consent. | WCAG 2.2.2 |
| **Cultural Consent** | Indigenous or sensitive materials require explicit FAIR+CARE consent tags. | FAIR+CARE Ethics |

---

## 🧭 Example Implementation

```html
<figure role="group" aria-labelledby="media-title" aria-describedby="media-description">
  <video
    controls
    preload="metadata"
    aria-describedby="media-description"
    aria-label="Oral history interview with community elder"
    poster="/images/thumbnails/interview.jpg"
  >
    <source src="/media/interview.mp4" type="video/mp4" />
    <track src="/captions/interview_en.vtt" kind="captions" srclang="en" label="English" default />
  </video>
  <figcaption id="media-title">Oral History Interview</figcaption>
  <p id="media-description">Recorded in 2024. Includes transcript and FAIR+CARE cultural consent approval.</p>
</figure>
```

**Implementation Rules**
- Include `<track>` for captions in all videos.  
- Always provide poster image and title via `<figcaption>`.  
- Use `aria-label` and `aria-describedby` for metadata linkage.  
- Avoid autoplay; user consent required for playback.  

---

## 🎨 Design Tokens

| Token | Description | Example |
|--------|--------------|---------|
| `media.focus.color` | Outline for focused controls | `#FFD54F` |
| `media.bg.color` | Background for embedded player | `#212121` |
| `media.caption.color` | Caption text color | `#FFFFFF` |
| `media.caption.bg` | Caption background overlay | `#000000AA` |

---

## 🧾 FAIR+CARE Consent Metadata

| Attribute | Description |
|------------|--------------|
| `data-fair-consent="approved"` | Indicates consent verification for public playback. |
| `data-origin="tribal-record"` | Identifies culturally governed source material. |
| `data-ethics-reviewed="true"` | Confirms content passed FAIR+CARE ethical audit. |
| `data-sensitive="true"` | Flags restricted visibility; applies masking in UI. |

Example:
```html
<video controls data-fair-consent="approved" data-origin="tribal-record" data-ethics-reviewed="true">
  ...
</video>
```

---

## 🧪 Validation Workflows

| Tool | Scope | Output |
|-------|--------|--------|
| **axe-core** | Media control accessibility | `reports/self-validation/web/a11y_media.json` |
| **Lighthouse CI** | Caption/transcript compliance | `reports/ui/lighthouse_media.json` |
| **FFmpeg Script** | Metadata extraction for validation | `reports/media/metadata_scan.json` |
| **Manual QA** | NVDA/VoiceOver + playback control | FAIR+CARE logs |

---

## ⚖️ FAIR+CARE Integration

| Principle | Implementation |
|------------|----------------|
| **Collective Benefit** | Media amplifies shared cultural knowledge respectfully. |
| **Authority to Control** | Consent metadata determines playback availability. |
| **Responsibility** | All audiovisual content logged in Governance Ledger. |
| **Ethics** | Media reviewed for cultural sensitivity and trauma-informed narration. |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v10.0.0 | 2025-11-10 | FAIR+CARE A11y Council | Defined media accessibility patterns, FAIR+CARE consent attributes, and CI validation pipelines. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Developed under **Master Coder Protocol v6.3** · Verified by **FAIR+CARE Council**  
[⬅ Back to Navigation](navigation.md) · [Back to A11y Patterns Index](README.md)

</div>

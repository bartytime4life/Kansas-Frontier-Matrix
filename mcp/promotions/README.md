<!-- 📍 Path: mcp/promotions/README.md -->

# 📣 Promotions MCP

![Evidence-first](https://img.shields.io/badge/evidence--first-required-blue)
![Provenance](https://img.shields.io/badge/provenance-STAC%20%7C%20DCAT%20%7C%20PROV-orange)
![Human-in-the-loop](https://img.shields.io/badge/human--in--the--loop-always-success)
![Transparency](https://img.shields.io/badge/nothing%20is%20a%20black%20box-true-informational)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)

> **Purpose:** ship promotional content that is *as auditable as the product*.  
> No mystery claims. No “trust us bro.” Just **stories + evidence + clear CTAs**. 🧭

---

## 📚 Table of contents

- [What this is](#-what-this-is)
- [Quick start](#-quick-start)
- [Folder layout](#-folder-layout)
- [Messaging kit](#-messaging-kit)
- [Audience map](#-audience-map)
- [Evidence-first workflow](#-evidence-first-workflow)
- [Templates](#-templates)
- [Guardrails](#-guardrails)
- [Visual assets guide](#-visual-assets-guide)
- [Metrics](#-metrics)
- [Reference library](#-reference-library)
- [Contributing](#-contributing)
- [FAQ](#-faq)

---

## 🧩 What this is

This folder is the **Promotions module** inside `mcp/` (Master Coder Protocol). It’s a **repeatable system** for creating campaigns, announcements, and press-ready copy for **Kansas Frontier Matrix (KFM)**—without breaking KFM’s core ethos:

- **Evidence-backed outputs** (citations, provenance, sources) 🧾
- **Human agency** (AI helps draft; humans approve) 👥
- **Transparency by design** (the “map behind the map”) 🗺️
- **Governance-aware comms** (sensitivity, privacy, cultural protocols) 🔒

If you can’t point to a dataset / doc / commit / demo proving a claim, **it doesn’t ship**.

---

## 🔥 Quick start

1. **Pick a campaign type** 🎯  
   - Feature drop (UI/AI)  
   - Dataset release  
   - Story Node launch  
   - Partnership / community call  
   - Roadmap teaser (clearly labeled)

2. **Create a campaign folder** 📦  
   Example: `mcp/promotions/campaigns/2026-01-timeline-slider/`

3. **Fill out the brief** 📝  
   Use the template in [Templates](#-templates).

4. **Build a claim ledger** 🧷  
   Every claim needs a source pointer (dataset ID, doc, PR).

5. **Generate drafts + review** ✅  
   Draft with AI if you want—**label AI text** and keep the claim ledger attached.

---

## 🗂 Folder layout

Recommended structure (add as you grow):

```text
mcp/
  promotions/
    README.md
    campaigns/
      2026-01-feature-name/
        brief.md
        claims.yml
        assets/
          screenshots/
          gifs/
          charts/
        outputs/
          social-twitter.md
          social-linkedin.md
          blog-outline.md
          press-release.md
        review/
          checklist.md
          approvals.md
    brand/
      voice.md
      messaging.md
      boilerplate.md
      do-dont.md
    templates/
      campaign-brief.md
      claim-ledger.yml
      press-release.md
      social/
        twitter-thread.md
        linkedin-post.md
        bluesky-post.md
        mastodon-post.md
      community/
        newsletter.md
        discord-announcement.md
        event-abstract.md
```

---

## 🧠 Messaging kit

### One-line description

**KFM is a geospatial knowledge + modeling platform** that turns maps, documents, and datasets into an **auditable, queryable, mappable system**—with a built-in AI assistant that **cites sources**.

### Taglines

Pick one that matches the moment (keep it simple):

- **“Mapping new frontiers of knowledge together.”** 🌾
- **“The map behind the map.”** 🗺️
- **“Nothing is a black box.”** 🧪
- **“Every insight has a source.”** 🧾

### Elevator pitches

**10-second**  
KFM helps people explore Kansas through time with maps, story narratives, and an evidence-backed AI assistant—so every claim is traceable.

**30-second**  
KFM combines a 2D/3D mapping UI, timeline navigation, Story Nodes, and Focus Mode (AI Q&A). The difference is trust: KFM enforces provenance and citations end-to-end, so users can always inspect sources, licenses, and processing—not just see pretty layers.

**2-minute**  
KFM is designed like “data + metadata + governance” as a single product. Datasets enter through a contract-first pipeline (metadata required), are cataloged and connected in the knowledge graph, and are surfaced through a UI that emphasizes transparency and context. The AI assistant is advisory-only: it helps explain what you’re seeing, cites the underlying sources, and refuses to invent answers. The result is a living atlas that can support education, research, civic planning, and community storytelling—without losing auditability.

---

## 🎯 Audience map

| Audience | What they care about | Headline angle | Proof anchors |
|---|---|---|---|
| Educators 🏫 | engaging, accurate stories | “Time-travel through Kansas with guided story narratives.” | Story Nodes + timeline demos |
| Researchers 🔬 | provenance, reproducibility | “Every insight is traceable to data + processing steps.” | STAC/DCAT/PROV, ledger |
| Civic planners 🏙️ | context + scenarios | “From static maps to scenario exploration.” | simulations + layers + governance |
| Developers 🧑‍💻 | APIs + extensibility | “Open standards + modular architecture.” | REST/GraphQL + MapLibre/Cesium |
| Public/history fans 🧭 | wonder + clarity | “Explore places, events, and archives—without guesswork.” | Focus Mode citations |

---

## 🧾 Evidence-first workflow

### The non-negotiables

- **Every published claim is traceable** 🔗  
  If it’s factual, it needs an evidence pointer (dataset/doc/PR).

- **AI output must be labeled** 🏷️  
  Drafts can be AI-assisted. Final copy must be human-reviewed.

- **Roadmap vs shipped must be explicit** 🧭  
  If it’s planned, say “planned”, “exploratory”, or “proposed”.

### Suggested review flow

1. **Draft copy from brief**
2. **Run a “claim pass”**: extract claims into `claims.yml`
3. **Add evidence pointers**
4. **Edit for voice + clarity**
5. **Final pass**: sensitivity + licensing + attribution
6. **Ship** 🚀

---

## 🧰 Templates

> Keep templates close to output. If it’s used often, it should be a file in `templates/`.

<details>
<summary><strong>📝 Campaign brief template</strong></summary>

```markdown
# Campaign brief

## Name
- Campaign: <!-- e.g., Timeline Slider MVP -->
- Date window:
- Owner:

## Goal
- What outcome are we driving? (signups, repo stars, contributors, dataset adoption)

## Audience
- Primary:
- Secondary:

## What shipped
- Bullet list of shipped features/datasets

## Key proof points
- Datasets / PRs / demo links:
- Screenshots/GIFs:

## Messaging pillars
- Pillar 1:
- Pillar 2:
- Pillar 3:

## CTA
- “Try the demo”
- “Open an issue”
- “Contribute a Story Node”
- “Download offline pack”

## Constraints
- Sensitivity notes:
- Licensing/attribution notes:
- What we must NOT claim:
```
</details>

<details>
<summary><strong>🧷 Claim ledger template</strong></summary>

```yaml
campaign: "Timeline Slider MVP"
claims:
  - id: C001
    claim: "The map supports timeline-based filtering and playback."
    status: verified # verified | inferred | roadmap
    evidence:
      - type: doc
        ref: "🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf"
        pointer: "Mapping Infrastructure → Dynamic Timeline & 4D Mapping"
  - id: C002
    claim: "AI answers include citations and refuse to fabricate when sources are missing."
    status: verified
    evidence:
      - type: doc
        ref: "Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf"
        pointer: "Focus Mode → Always cites sources"
  - id: C003
    claim: "AR uses the same data endpoints as the main platform."
    status: roadmap
    evidence:
      - type: doc
        ref: "Kansas Frontier Matrix – Comprehensive UI System Overview.pdf"
        pointer: "AR Integration → uses same data services"
```
</details>

<details>
<summary><strong>📣 Social post template</strong></summary>

```markdown
## Hook
One sentence that states what shipped *and why it matters*.

## What’s new
- ✅ Feature/Dataset
- ✅ Feature/Dataset
- ✅ Feature/Dataset

## Proof
- 📸 Screenshot/GIF: (path)
- 🧾 Evidence: (claim ledger IDs)

## CTA
- Try it:
- Docs:
- Contribute:
```
</details>

<details>
<summary><strong>📰 Press release skeleton</strong></summary>

```markdown
# Headline
KFM introduces [feature] to help [audience] do [outcome] with evidence-backed mapping.

## Subhead
One line that explains the differentiator (provenance-first, citations, transparency).

## Body
- What shipped
- Why now
- Who it helps
- How it works (high level)
- Quotes (optional)
- Links to demo/docs
- Attribution + licensing notes
```
</details>

---

## 🛡 Guardrails

### No hype claims

Avoid phrases like:
- “AI discovers truth”
- “Fully automated”
- “Guaranteed accuracy”
- “Replaces experts”

Prefer:
- “Evidence-backed”
- “Advisory-only”
- “Designed for auditability”
- “Human-reviewed”

### Sensitivity and privacy

- Don’t publish **exact sensitive coordinates** or details that enable misuse.
- If a location or dataset has restricted/sensitive classification, **generalize**.
- If content involves Indigenous knowledge or culturally sensitive materials:  
  follow cultural protocol labeling (e.g., TK labels) and access rules. 🤝

### Attribution

- Always include dataset credits where required.
- If using third-party basemaps, imagery, archives, or licenses, include acknowledgments.

---

## 🖼 Visual assets guide

### The “minimum viable promo pack”

For any release/campaign, try to capture:

- 🗺️ **2D map view**: layer toggles + legend visible  
- 🌍 **3D view**: terrain/globe moment (if relevant)  
- ⏱️ **Timeline slider**: before/after or animated scrub  
- 📖 **Story Node playback**: narrative + map action synced  
- 🧠 **Focus Mode**: a single answer with citations visible  
- 🧾 **Provenance panel**: source/license shown (“map behind the map”)

### Screenshot rules

- Show UI context: legend + layer names > floating crop
- Use 1 strong hero image; everything else supports it
- Never show private tokens, internal-only layers, or restricted nodes

---

## 📈 Metrics

Promotions is still engineering: measure, iterate, and document.

Suggested metrics by channel:

- Social: impressions, saves, click-through, follows
- Community: issue creation, PRs, new contributors
- Product: demo usage, docs clicks, dataset downloads
- Partnerships: replies, meetings scheduled, pilot requests

### Lightweight experimentation

- Run A/B variants (headline vs story hook)
- Track which proof points drive clicks
- Keep an “insights” note per campaign: what worked, what didn’t 🧠

---

## 📚 Reference library

These are the **source-of-truth** project docs that this promotions pack is built from:

### Core KFM docs

- 📘 `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf`  
  Architecture, UI/AI principles, provenance-first rules, policy posture.
- 🧱 `Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf`  
  End-to-end architecture + feature set and how it composes.
- 🤖 `Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf`  
  Focus Mode, explainability, governance, prompt security.
- 🎛️ `Kansas Frontier Matrix – Comprehensive UI System Overview.pdf`  
  Maps (2D/3D), timeline, Story Nodes, offline packs, AR ideas.
- 📥 `📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf`  
  Data contracts, STAC/DCAT/PROV integration, policy-as-code, CI checks.
- 💡 `Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf`  
  Future-facing ideas like 4D digital twins, AR storytelling, cultural protocols.
- 🌟 `🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf`  
  Roadmap proposals like timeline slider MVP and high-performance tiling.

### Research and skills libraries

Some files are **PDF portfolios** (a container with many embedded books/docs).  
You can extract them locally to browse the individual references.

- 🧠 `AI Concepts & more.pdf`
- 🗺️ `Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf`
- 🧑‍💻 `Various programming langurages & resources 1.pdf`
- 🧮 `Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf`

#### Extract embedded PDFs from a portfolio

```bash
# List embedded files
pdfdetach -list "docs/references/AI Concepts & more.pdf"

# Extract everything into a folder
mkdir -p docs/references/extracted/ai
pdfdetach -saveall -o docs/references/extracted/ai "docs/references/AI Concepts & more.pdf"
```

> Tip: extracted references are great for deep-dive blog posts, talk abstracts, and technical proof points—just keep claims tied to KFM’s actual shipped features.

---

## 🤝 Contributing

### What to contribute here

- New campaign folders 📦
- Better templates 🧰
- Approved copy variations ✍️
- Screenshot packs / GIF recipes 🎞️
- A clearer message map 🧭

### Contribution rules

- Use PRs ✅
- Include a claim ledger 🧷
- Add a review checklist 🧾
- Keep tone consistent (see `brand/` once it exists)

---

## ❓ FAQ

### Is this just “marketing content”?

It’s **marketing with governance**: copy is treated like a product artifact—versioned, reviewable, and evidence-backed.

### Can I use AI to write everything?

AI can draft. Humans approve. If AI wrote it, label it and keep the claim ledger with sources.

### What if something is only planned?

Say it’s planned. Promotions should never blur roadmap into “shipped.”

### How do we avoid misinformation?

We don’t publish uncited claims. Every statement must map to a dataset, doc, demo, or PR.

---

🧭 **North Star:** If a user clicks what we say, they should land on **proof**—not vibes.

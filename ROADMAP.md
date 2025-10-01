<div align="center">

# 🚦 Kansas-Frontier-Matrix — Roadmap  

**Mission:** Track milestones, issues, and MCP deliverables in sync with  
`.github/roadmap/roadmap.yaml` via `.github/workflows/roadmap.yml`.  

[![Roadmap Sync](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/roadmap.yml/badge.svg)](../../actions/workflows/roadmap.yml)  
[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../actions/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](../../actions/workflows/stac-badges.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../actions/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../actions/workflows/trivy.yml)  

🔁 **PRs** → dry-run only (no writes)  
✅ **Pushes to `main`** → apply roadmap changes  

</div>

---

## 📚 Contents
- [Milestones (targets)](#-milestones-targets)
- [Dependency graph](#-dependency-graph)
- [Progress snapshot](#-progress-snapshot)
- [Milestone 1 — Enrich Data Sources (`m1-data`)](#-milestone-1--enrich-data-sources-m1-data)
- [Milestone 2 — Analytical Enhancements (`m2-analytics`)](#-milestone-2--analytical-enhancements-m2-analytics)
- [Milestone 3 — Storytelling & Education (`m3-story`)](#-milestone-3--storytelling--education-m3-story)
- [Milestone 4 — Technical Enhancements (`m4-tech`)](#-milestone-4--technical-enhancements-m4-tech)
- [Milestone 5 — MCP Integration (`m5-mcp`)](#-milestone-5--mcp-integration-m5-mcp)
- [Label taxonomy](#-label-taxonomy)
- [Definitions of Done (DoD)](#-definitions-of-done-dod)
- [Working agreements](#-working-agreements)
- [Edit the source roadmap](#-edit-the-source-roadmap)
- [Run the sync locally](#-run-the-sync-locally)
- [FAQ / Troubleshooting](#-faq--troubleshooting)

---

## 🎯 Milestones (targets)

| Key            | Title                    | Target date |
|----------------|--------------------------|-------------|
| `m1-data`      | Enrich Data Sources      | 2025-10-31  |
| `m2-analytics` | Analytical Enhancements  | 2025-11-30  |
| `m3-story`     | Storytelling & Education | 2025-12-31  |
| `m4-tech`      | Technical Enhancements   | —           |
| `m5-mcp`       | MCP Integration          | —           |

```mermaid
flowchart TD
  M1["Milestone 1<br/>Enrich Data Sources<br/>(Oct 31, 2025)"] --> M2["Milestone 2<br/>Analytical Enhancements<br/>(Nov 30, 2025)"]
  M2 --> M3["Milestone 3<br/>Storytelling & Education<br/>(Dec 31, 2025)"]
  M3 --> M4["Milestone 4<br/>Technical Enhancements"]
  M4 --> M5["Milestone 5<br/>MCP Integration"]


⸻

🧭 Dependency graph

graph LR
  data[Data Sources<br/>m1-data] --> analytics[Analytics & Models<br/>m2-analytics]
  analytics --> story[Storytelling & Education<br/>m3-story]
  story --> tech[Tech Enhancements<br/>m4-tech]
  data --> tech
  tech --> mcp[MCP Integration<br/>m5-mcp]
  analytics --> mcp


⸻

📈 Progress snapshot

Auto-rendered from .github/roadmap/roadmap.yaml

	•	M1 — Enrich Data Sources: ██████████ 75%
	•	M2 — Analytical Enhancements: ███████░░ 60%
	•	M3 — Storytelling & Education: ████░░░░░ 40%
	•	M4 — Technical Enhancements: ██░░░░░░░ 20%
	•	M5 — MCP Integration: ███░░░░░░░ 30%

⸻

🗺 Milestone 1 — Enrich Data Sources (m1-data)

Issue: Oral Histories & Indigenous Narratives (oral-histories)

Tasks
	•	Inventory oral-history archives (tribal, KHRI, local historical societies).
	•	Digitize & geocode transcripts (MCP experiment template).
	•	Link narratives to features via glossary tooltips/popups.

Deliverables
	•	data/sources/oral_histories.json
	•	Story hooks in web/config/story_layers.json

DoD
	•	Narrative appears as a timeline card + map popup with glossary links.

⸻

Issue: Paleoclimate & Fire Regimes (paleo-fire)

Tasks
	•	Integrate drought indices, pollen cores, charcoal/fire records.
	•	Cross-link with KGS & Neotoma; add STAC entries.

Deliverables
	•	data/sources/paleoclimate.json
	•	stac/collections/*, stac/items/*

DoD
	•	Drought + fire layers visible with citation + uncertainty.

⸻

Issue: Hydrology & Water Management (hydro-expansion)

Tasks
	•	Add NOAA/FEMA flood-event datasets & irrigation/management.
	•	Prototype flood scenarios (HEC-RAS; MCP modeling SOP).

Deliverables
	•	data/sources/hydrology.json
	•	STAC wired collections/items

DoD
	•	Flood layers visible with timeline + experiment doc.

⸻

Issue: Kansas River (KGS) → STAC → Viewer (kgs-kansas-river)

Tasks
	•	Source: data/sources/ks_kansas_river.json
	•	STAC: stac/collections/ks_kansas_river.json (+ children)
	•	Items: channels/floodplains/gauges in stac/items/ks_kansas_river/*.json
	•	Makefile: hydrology-fetch, hydrology-stac, site mirror
	•	Web config: ensure ksriv_* in web/app.config.json / layers.json

Acceptance
	•	Layers render in viewer; provenance in STAC; mirrored to web/data/processed/hydrology/kansas_river/*.geojson.

⸻

📊 Milestone 2 — Analytical Enhancements (m2-analytics)
	•	Predictive Modeling (predictive-modeling): ABM/Bayesian hybrids; reproducible notebook + experiment report.
	•	Uncertainty Quantification (uncertainty-quant): Confidence scores for NLP/georeferencing; UI encodings.
	•	Symbolic Reasoning (symbolic-reasoning): Ontology schema (CIDOC-CRM + GeoSciML); treaty inference rules.
	•	Fractal & Pattern Analysis (fractal-patterns): Sinuosity metrics, clustering/power-law analysis.

⸻

📖 Milestone 3 — Storytelling & Education (m3-story)
	•	Santa Fe Trail Story Map (sft-storymap): Routes + sources → interactive story page.
	•	Dust Bowl Timeline (dustbowl-timeline): 1930s overlays (climate + newspapers).
	•	Glossary Annotations (glossary-annotations): Glossary-linked tooltips on map features.
	•	Crowdsourcing Portal (crowdsourcing-portal): Web form → PR bot → validated in CI.

⸻

🧩 Milestone 4 — Technical Enhancements (m4-tech)
	•	3D Time Animation (time-3d): CesiumJS prototype + regionated KMZ.
	•	Semantic Web (semantic-web): Map entities to Wikidata; RDF/OWL dump.
	•	Modularity (modularity): Define plugin boundaries; doc in docs/architecture.md.
	•	APIs & Downloads (apis-downloads): REST/GraphQL endpoints; GeoJSON/CSV exports.

⸻

🧪 Milestone 5 — MCP Integration (m5-mcp)
	•	Experiment Reports (experiments-first-3): Georeferencing, NLP placenames, predictive modeling.
	•	SOPs (sop-docs): Georeference + dataset SOPs; CI enforced.
	•	Model Cards (model-cards): NLP placenames, change detection; lineage + metrics.
	•	CI/CD Reproducibility (ci-repro): STAC validate + CodeQL + prebuild path green.

⸻

🏷 Label taxonomy

data, hydrology, stac, web, story, education, analytics, uncertainty,
ontology, reasoning, fractal, 3d, semantic-web, api,
mcp, sop, model-card, ci, docs, good-first-issue

⸻

✅ Definitions of Done (DoD)
	•	STAC-complete: item + collection, license, bbox, temporal, checksum.
	•	Reproducible: make fetch … stac site works locally + CI.
	•	Provenance: source metadata logged in STAC + data/sources/*.json.
	•	Docs: update docs/CHANGELOG.md / whats-new.md if user-facing.
	•	Uncertainty: confidence/error fields & UI encoding plan.
	•	Security: CodeQL & Trivy pass; .env.example included.

⸻

🤝 Working agreements
	•	One issue = one outcome; checklist tasks map to commits.
	•	Every PR linked to an Issue + Milestone.
	•	Schema first for new data.
	•	MCP discipline: experiments, SOPs, model cards under mcp/**.
	•	Roadmap sync: PR = dry-run, main = apply.

⸻

🛠 Edit the source roadmap

Edit .github/roadmap/roadmap.yaml; this doc is generated from it.

milestones:
  - key: m1-data
    title: Enrich Data Sources
    due: 2025-10-31

issues:
  - key: kgs-kansas-river
    title: Kansas River (KGS) — Source → STAC → Viewer
    milestone: m1-data
    labels: [data, hydrology, stac, web]


⸻

🧪 Run the sync locally

npm ci
npm run validate

# Dry run (no writes)
npm run sync:dry

# Apply (requires GH token with repo scope)
GITHUB_TOKEN=ghp_xxx npm run sync

Triggers:
	•	PR → dry_run=true (no writes)
	•	main → dry_run=false (apply)
	•	Manual dispatch → override dry_run

⸻

❓ FAQ / Troubleshooting
	•	Edited this file but sync says “no changes”?
→ Edit .github/roadmap/roadmap.yaml instead; re-run sync.
	•	CI fails STAC validation?
→ Run make stac-validate locally; fix bbox/datetime/license.
	•	New dataset not rendering?
→ Ensure layer in web/app.config.json + layers.json; check assets under web/data/**.
	•	Where do MCP docs live?
→ Experiments → mcp/experiments/*.md
→ SOPs → mcp/sops/*.md
→ Model cards → mcp/model_cards/*.md

⸻

💡 Pro tip: Add a Project board badge here and link this doc from your main README so contributors see milestones, labels, and DoD at a glance.
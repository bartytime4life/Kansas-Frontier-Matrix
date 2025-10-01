<div align="center">


🚦 Kansas-Frontier-Matrix — Roadmap

This doc mirrors .github/roadmap/roadmap.yaml and stays in lock-step via .github/workflows/roadmap.yml (drives scripts/sync-roadmap.js).

🔁 PRs run the sync in dry-run (no writes).
✅ Pushes to main (or manual dispatch with dry_run=false) apply changes.

</div>



⸻

📚 Contents
	•	Milestones (targets)
	•	Dependency graph
	•	Progress snapshot
	•	Milestone 1 — Enrich Data Sources (m1-data)
	•	Milestone 2 — Analytical Enhancements (m2-analytics)
	•	Milestone 3 — Storytelling & Education (m3-story)
	•	Milestone 4 — Technical Enhancements (m4-tech)
	•	Milestone 5 — MCP Integration (m5-mcp)
	•	Label taxonomy
	•	Definitions of Done (DoD)
	•	Working agreements
	•	Edit the source roadmap
	•	Run the sync locally
	•	FAQ / Troubleshooting

⸻

🎯 Milestones (targets)

Key	Title	Target date
m1-data	Enrich Data Sources	2025-10-31
m2-analytics	Analytical Enhancements	2025-11-30
m3-story	Storytelling & Education	2025-12-31
m4-tech	Technical Enhancements	—
m5-mcp	MCP Integration	—

flowchart TD
  M1["Milestone 1<br/>“Enrich Data Sources”<br/>(Oct 31, 2025)"] --> M2["Milestone 2<br/>“Analytical Enhancements”<br/>(Nov 30, 2025)"]
  M2 --> M3["Milestone 3<br/>“Storytelling & Education”<br/>(Dec 31, 2025)"]
  M3 --> M4["Milestone 4<br/>“Technical Enhancements”"]
  M4 --> M5["Milestone 5<br/>“MCP Integration”"]


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

Update by editing .github/roadmap/roadmap.yaml. The sync renders status here.

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
	•	data/sources/oral_histories.json (license, contact, update cadence).
	•	Story hooks in web/config/story_layers.json.

DoD
	•	Provenance (license/attribution) captured in STAC; sample narrative appears as a timeline card + map popup with glossary links.

⸻

Issue: Paleoclimate & Fire Regimes (paleo-fire)

Tasks
	•	Integrate drought indices, pollen cores, charcoal/fire records.
	•	Cross-link with KGS & Neotoma; add STAC collections/items.

Deliverables
	•	data/sources/paleoclimate.json
	•	STAC under stac/collections/*, stac/items/*.

DoD
	•	At least one drought time series overlays the timeline; fire regime layer renders with citation + uncertainty.

⸻

Issue: Hydrology & Water Management Expansion (hydro-expansion)

Tasks
	•	Add flood-event datasets (NOAA/FEMA) & irrigation/management (when public).
	•	Prototype historical flood scenarios (HEC-RAS; MCP modeling SOP).

Deliverables
	•	data/sources/hydrology.json
	•	STAC wired (collections/items).

DoD
	•	Flood layers visible (map + time slider), with scenario doc in mcp/experiments/.

⸻

Issue: Kansas River (KGS) — Source → STAC → Viewer (kgs-kansas-river)

Tasks
	•	Source: data/sources/ks_kansas_river.json (ArcGIS REST + metadata).
	•	STAC: stac/collections/ks_kansas_river.json (+ children).
	•	Items: channels/floodplains/gauges under stac/items/ks_kansas_river/*.json.
	•	Makefile: hydrology-fetch, hydrology-stac (and site to mirror vectors).
	•	Web config: ensure ksriv_* layers in web/app.config.json / web/layers.json.

Acceptance
	•	Layers render in the web viewer; provenance in STAC; make site mirrors web/data/processed/hydrology/kansas_river/*.geojson.

Dirs touched
	•	data/processed/hydrology/kansas_river/
	•	stac/collections/ks_kansas_river.json
	•	stac/items/ks_kansas_river/*.json
	•	web/data/processed/hydrology/kansas_river/*.geojson
	•	web/app.config.json, web/layers.json

⸻

📊 Milestone 2 — Analytical Enhancements (m2-analytics)

Issue: Predictive Modeling (predictive-modeling)

Tasks
	•	Train on settlement sites + drivers (DEM, hydrology, soils).
	•	Log experiments in mcp/experiments/EXP-SETTLE-PRED.md.
	•	Explore Bayesian + ABM/GIS hybrids.

Acceptance
	•	Reproducible notebook + experiment report with metrics, seed, data snapshots.

⸻

Issue: Uncertainty Quantification (uncertainty-quant)

Tasks
	•	Confidence scores for NLP toponyms & georeferencing/rectification.
	•	UI encodings: opacity/error bars/probabilistic shading.

Acceptance
	•	Uncertainty visible in UI; documented in STAC assets + docs/uncertainty.md.

⸻

Issue: Symbolic & Knowledge-Based Reasoning (symbolic-reasoning)

Tasks
	•	Ontology schema (CIDOC-CRM + GeoSciML + treaty/legal vocabs).
	•	Treaty/legal land-transfer inference rules.

Acceptance
	•	Example SPARQL/GraphQL queries + rule snippets; RDF/OWL snapshot in exports/semantic/.

⸻

Issue: Fractal & Pattern Analysis (fractal-patterns)

Tasks
	•	Meander fractal dimension, sinuosity metrics; clustering/power-law tests.

Acceptance
	•	Metrics JSON in analytics/metrics/ + brief analysis note; optional overlay layer configured.

⸻

📖 Milestone 3 — Storytelling & Education (m3-story)

Issue: Interactive Story Maps — Santa Fe Trail (sft-storymap)

Tasks
	•	Assemble routes + primary sources; timeline step-through views.

Acceptance
	•	Hosted story page (in web/story/) with linked sources; offline build step in make site.

⸻

Issue: Dust Bowl Timeline Prototype (dustbowl-timeline)

Tasks
	•	Compose 1930s overlays (climate + newspapers + soils).

Acceptance
	•	Time slider demo with source footers + uncertainty badges.

⸻

Issue: Glossary & Educational Annotations (glossary-annotations)

Tasks
	•	Link glossary terms into map tooltips.
	•	Overlays: railroads, treaties, forts, migration routes.

Acceptance
	•	Glossary tooltips render with term IDs; examples captured in docs/education/.

⸻

Issue: Crowdsourcing Submission Portal (crowdsourcing-portal)

Tasks
	•	Web form → GitHub PR bot; contributor guide docs/CONTRIBUTING.md.

Acceptance
	•	End-to-end submission merged via PR; CI validates file format & STAC.

⸻

🧩 Milestone 4 — Technical Enhancements (m4-tech)

Issue: 3D Time Animation (time-3d)

Tasks
	•	CesiumJS prototype (1850–present); regionated KML/KMZ exports.

Acceptance
	•	3D demo + KML sample in earth/ and link from viewer.

⸻

Issue: Semantic Web Integration (semantic-web)

Tasks
	•	Map entities to Wikidata; publish RDF/OWL.

Acceptance
	•	RDF dump + minimal SPARQL/GraphQL access plan in docs/semantic/.

⸻

Issue: Modularity & Extensibility (modularity)

Tasks
	•	Define plugin boundaries for ingestion/AI/UI; document extension points.

Acceptance
	•	docs/architecture.md updated; minimal plugin example under examples/plugins/.

⸻

Issue: APIs & External Tools (apis-downloads)

Tasks
	•	REST/GraphQL endpoints; GeoJSON/CSV downloads.

Acceptance
	•	Minimal API spec in docs/api.md + sample responses in examples/api/.

⸻

🧪 Milestone 5 — MCP Integration (m5-mcp)

Issue: Experiment Reports (First Three) (experiments-first-3)

Tasks
	•	Use mcp/experiments/experiment_template.md.
	•	Georeferencing, NLP placename extraction, predictive settlement modeling.

Acceptance
	•	Three completed reports with code, inputs, outputs, and discussion.

⸻

Issue: SOP Documentation (sop-docs)

Tasks
	•	mcp/sops/georeference_map.md, mcp/sops/add_dataset.md.

Acceptance
	•	SOPs referenced by CI preflight; make prebuild enforces.

⸻

Issue: Model Cards (model-cards)

Tasks
	•	mcp/model_cards/nlp_placename.md, mcp/model_cards/change_detection.md.

Acceptance
	•	Model cards linked from README & docs; includes training data lineage + eval metrics.

⸻

Issue: CI/CD Reproducibility (ci-repro)

Tasks
	•	STAC validation job + CodeQL in CI; make prebuild path green.

Acceptance
	•	CI green; docs updated in README.md and docs/ci.md.

⸻

🏷 Label taxonomy

data, hydrology, stac, web, story, education, analytics, uncertainty, ontology, reasoning, fractal, 3d, semantic-web, api, mcp, sop, model-card, ci, docs, good-first-issue

Tip: add color & emoji to top labels for fast scanning (e.g., data = teal 📦, analytics = purple 📈).

⸻

✅ Definitions of Done (DoD)
	•	STAC-complete: Asset has STAC item + collection, license, bbox, temporal extent, checksums.
	•	Reproducible: make fetch … stac site builds the same artifacts locally and in CI.
	•	Provenance: Source metadata (license, source URL, date fetched) is captured in STAC + data/sources/*.json.
	•	Docs: A short entry in docs/CHANGELOG.md and, if user-visible, docs/whats-new.md.
	•	Uncertainty: If applicable, include confidence or error fields and UI encoding plan.
	•	Security: CodeQL & Trivy pass; no secrets in repo; .env.example provided when needed.

⸻

🤝 Working agreements
	•	One issue = one clear outcome; checklist tasks map to commits.
	•	Every PR has a linked Issue + Milestone.
	•	Schema first: propose JSON schemas for new data before adding files.
	•	MCP discipline: experiments, SOPs, and model cards live under mcp/** and are referenced from issues.
	•	Sync cadence: roadmap sync runs on PR (dry-run) and main (apply).

⸻

🛠 Edit the source roadmap

Edit .github/roadmap/roadmap.yaml; this doc is generated from it.

Example snippet

milestones:
  - key: m1-data
    title: Enrich Data Sources
    due: 2025-10-31

issues:
  - key: kgs-kansas-river
    title: Kansas River (KGS) — Source → STAC → Viewer
    milestone: m1-data
    labels: [data, hydrology, stac, web]
    tasks:
      - Add sources, collections, items
      - Wire Makefile hydrology targets
      - Mirror vectors to web/data and render layers


⸻

🧪 Run the sync locally

# Validate roadmap schema and scripts
npm ci
npm run validate

# Dry run (prints plan, no writes)
npm run sync:dry

# Apply (writes to GitHub; requires a token with repo scope)
GITHUB_TOKEN=ghp_xxx npm run sync

Workflow triggers
	•	On PR: dry_run=true (no writes).
	•	On main: dry_run=false (apply).
	•	Manual dispatch: override dry_run.

⸻

❓ FAQ / Troubleshooting

The sync says “no changes” but I edited this doc
This file is generated; edit .github/roadmap/roadmap.yaml, then re-run the sync.

CI fails STAC validation
Run: make stac-validate locally; fix missing fields (bbox, datetime, license) or invalid JSON.

New dataset isn’t rendering
Check web/app.config.json and web/layers.json entries exist; verify assets under web/data/**; clear cache or hard refresh.

Where do I put experiments / SOPs / model cards?
	•	Experiments → mcp/experiments/*.md
	•	SOPs → mcp/sops/*.md
	•	Model cards → mcp/model_cards/*.md
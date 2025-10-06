<div align="center">


🧭 Kansas Frontier Matrix — Navigation Components

docs/design/mockups/figma/components/navigation/

Interactive · Temporal · Spatial · Accessible Navigation System

</div>



⸻

🪶 Overview

The Navigation Components define the core interaction framework of the Kansas Frontier Matrix (KFM) web interface — uniting space, time, and knowledge discovery.

This system integrates the Header, Timeline, Layer Controls, and Detail Panel into an accessible, modular, and time-aware UI connected to the KFM knowledge graph and STAC-driven map layers.

⸻

🧩 Components

Component	Description	Key Features
Header Bar	Branding, global search, and utility actions.	Brand → Home, / → focus search, Help, Language, Auth
Timeline	Time navigation and filtering tool.	Zoom, play, drag, filter events, synchronized map layers
Layer Controls	Visibility and legend management.	Toggle overlays, adjust opacity, STAC-driven structure
Detail Panel	Displays selected entity/event data.	AI summary, related entities, source citations
Keyboard & Accessibility	Ensures full interaction parity.	WAI-ARIA roles, shortcuts, focus management


⸻

🧱 Directory Layout

docs/design/mockups/figma/components/navigation/
├── README.md                 # This specification file
├── wireframes/               # PNG/SVG design exports
├── figma-refs.json           # Mappings to Figma nodes
└── assets/                   # Icons, color tokens, and layout previews


⸻

🧭 System Integration (GitHub-Safe Mermaid)

flowchart LR
  subgraph UI["User Interface"]
    A["Header\n(search · help · admin)"]
    B["Timeline\n(range · play · zoom)"]
    C["Layer Controls\n(toggles · legends)"]
    D["Map View\n(overlays · events)"]
    E["Detail Panel\n(summaries · links)"]
  end

  subgraph API["Backend API"]
    F["FastAPI / GraphQL"]
  end

  subgraph DATA["Knowledge Systems"]
    G["Neo4j Graph\n(entities · events · links)"]
    H["STAC Catalog\n(layers.json)"]
  end

  %% Data flow
  A --> F
  B --> F
  C --> H
  D --> F
  E --> F
  F --> G
  F --> H
  H --> D

<!-- END OF MERMAID -->



⸻

🔄 Event Flow Contracts

Emitter	Event	Payload	Consumer	Effect
Timeline	time:changed	{ start, end }	Map	Filters visible events/layers
Search	search:selected	{ entityId }	Map, Timeline	Zoom and focus on entity
Map	map:entity:clicked	{ entityId }	Detail Panel	Fetch dossier and sources
Layers	layers:toggle	{ layerId, on }	Map	Show/hide overlay
Detail Panel	detail:relation:selected	{ relatedId }	Map, Timeline	Jump to related entity


⸻

🧠 Accessibility & Inclusivity
	•	Fully keyboard navigable (Tab, Enter, Esc)
	•	Screen-reader support (ARIA: banner, search, main, complementary)
	•	Timeline instructions as aria-describedby regions
	•	Color contrast ≥ WCAG 2.1 AA
	•	Non-color differentiation in map legends

⸻

⚙️ Rendering & Data Sources

Subsystem	Technology	Purpose
Map	MapLibre GL JS	Spatial rendering, overlays, interactivity
Timeline	HTML5 Canvas	High-FPS temporal rendering
Layer Config	STAC-derived layers.json	Defines source URLs, legends, extents
Graph	Neo4j	Entity linkage and relationships
API	FastAPI / GraphQL	Data delivery and search endpoints


⸻

🧪 Testing & QA

Category	Tool	Scope
Unit	Vitest / Jest	Timeline logic, state synchronization
Integration	Playwright	Search → Detail → Map workflow
Accessibility	Axe-core	Keyboard, ARIA compliance
Performance	Lighthouse	FPS, network latency, bundle size


⸻

🧰 Developer & Designer Workflow
	1.	Figma → Code Parity
Maintain identical component names between Figma and React components.
	2.	Update Procedure
	•	Modify UI → update figma-refs.json
	•	Sync design tokens → run make design-sync
	•	Commit README + assets changes together
	3.	PR Checklist
✅ Documentation updated
✅ Accessibility tested
✅ Layer config validated
✅ Mermaid diagram renders cleanly

⸻

🧭 Usage Demo (Local Preview)

# Build & serve the design system locally
make data             # Prepare STAC + configs
make site             # Build site
make serve            # Serve at http://localhost:4000

Then open the app and test:
	1.	Global search (/)
	2.	Timeline scrub (drag / play)
	3.	Toggle layers
	4.	Inspect detail panels

⸻

🧩 Design Tokens (Sample)

Token	Light	Dark	Purpose
--kfm-color-bg	#ffffff	#0b1020	Page background
--kfm-color-accent	#7ec8ff	#7ec8ff	Active elements
--kfm-font-body	"Inter", sans-serif	"Inter", sans-serif	UI text


⸻

📜 Change Log

Date	Version	Summary
2025-10-05	v1.0	Initial GitHub-compliant release
2025-10-06	v1.1	Added accessibility & event contracts
2025-10-07	v1.2	Revised Mermaid diagram & design tokens


⸻


<div align="center">


© Kansas Frontier Matrix Project
A Master-Coder-Protocol documentation standard — for reproducibility, design clarity, and long-term maintainability.

</div>

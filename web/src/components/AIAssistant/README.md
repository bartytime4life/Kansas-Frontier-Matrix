<div align="center">

# 🤖 Kansas Frontier Matrix — AI Assistant Component  
`web/src/components/AIAssistant/`

**Conversational Exploration · Summaries · Q&A · Entity Linking**

[![Build](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/ci.yml?label=Build)](../../../../../.github/workflows/ci.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../../.github/workflows/codeql.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../../../../LICENSE)

</div>

---

## 🧭 Overview

The **AI Assistant** is the interactive, natural-language exploration panel of the  
**Kansas Frontier Matrix Web Application**. It allows users to query the knowledge graph in plain  
English, receive AI-generated summaries or answers, and view **citations linked to map/timeline entities**.

It’s powered by backend `/api/ask` and `/api/entity/{id}` endpoints that use fine-tuned  
LLM models on historical Kansas data. The frontend component is responsible for:

- Capturing user queries.  
- Sending requests to the backend AI API.  
- Rendering responses with linked entities (people, places, events).  
- Highlighting referenced items on the **map** and **timeline**.  
- Managing chat history, loading state, and user interaction.  

This component is a fusion of **React**, **AIContext**, and **Framer Motion animations**, aligning with the  
project’s **Master Coder Protocol (MCP)** philosophy — document-first, reproducible, and explainable AI.

---

## 🧱 Directory Structure

```text
web/src/components/AIAssistant/
├── AIAssistant.tsx        # Main container component
├── ChatInput.tsx          # Input bar for user prompts
├── ChatMessage.tsx        # Renders each message (user + AI)
├── AICitation.tsx         # Displays linked entities and sources
├── styles.scss            # Theming, layout, animations
└── __tests__/             # Unit tests for message flow and rendering


⸻

⚙️ Component Architecture

flowchart TD
  UI["ChatInput\n(user query)"] --> API["AI API\nPOST /ask"]
  API --> RES["AIResponse\n(text, citations, entities)"]
  RES --> MSG["ChatMessage\nrenders text + links"]
  MSG --> CITE["AICitation\nlinks to events/places"]
  CITE --> MAP["MapView\nhighlight entities"]
  CITE --> TL["TimelineView\nfocus on events"]
  RES --> HIST["AIContext\nstores chat history"]
%% END OF MERMAID


⸻

🧩 Key Features

Feature	Description	Backend Link
Conversational Input	Users can ask natural-language questions about Kansas history.	/api/ask
Knowledge Summaries	Retrieves condensed summaries for entities (people, places, treaties).	/api/entity/{id}
Entity Linking	Detects mentioned entities and highlights them on the map/timeline.	Neo4j Knowledge Graph
Citations Panel	Displays references to original data sources (treaties, maps, documents).	Source metadata
AI Confidence	Shows model confidence levels and evidence count.	AIResponse metadata
Streaming Support	Streams AI text responses for smoother UX.	FastAPI StreamingResponse
Accessibility	Keyboard focus, ARIA roles, and reduced motion animations.	WCAG 2.1 AA


⸻

💬 Example Usage

import React from "react";
import { AIAssistant } from "./AIAssistant";

export default function RightPanel() {
  return (
    <aside className="ai-panel">
      <AIAssistant />
    </aside>
  );
}

User Flow Example

sequenceDiagram
  participant U as User
  participant A as AIAssistant
  participant S as Server (FastAPI)
  participant G as Graph (Neo4j)

  U->>A: "Show me droughts in western Kansas during the 1930s"
  A->>S: POST /api/ask
  S->>G: Query drought events (1930–1940, region=Kansas)
  G-->>S: Results with entities & sources
  S-->>A: AIResponse { text, entities, citations }
  A-->>U: "The Dust Bowl drought (1930–1939) devastated western Kansas..." + linked map highlights
%% END OF MERMAID


⸻

🧠 Data Model (TypeScript)

export interface AIResponse {
  text: string;                   // formatted answer
  citations?: Citation[];         // links to data sources
  entities?: EntityReference[];   // mapped entities (events/places)
  confidence?: number;            // 0–1 range
  timestamp: string;              // ISO 8601
}

export interface EntityReference {
  id: string;
  type: "Person" | "Place" | "Event" | "Document";
  label: string;
  coordinates?: [number, number];
}

These types are imported from web/src/types/ai.d.ts for consistent use across
the web app and backend data exchange.

⸻

🎨 UI & Styling
	•	Layout: Two-column split — messages (left) and citations (right).
	•	Animations: Framer Motion transitions (fade-in, slide-up) for chat messages.
	•	Theming: Dynamic text/background contrast synced with ThemeContext.
	•	Scrollable History: Infinite-scroll chat container with anchored auto-scroll.
	•	Markdown Rendering: Supports lists, italics, code blocks for formatted AI answers.

⸻

🧪 Testing & Validation

Tests live under __tests__/AIAssistant.test.tsx and validate:
	•	Rendering of message history.
	•	API mock responses and async loading behavior.
	•	Entity link click → triggers map/timeline highlights.
	•	Accessibility roles (aria-live="polite" for streaming messages).

Tools:
	•	Jest + React Testing Library
	•	MSW (Mock Service Worker) for simulating API responses
	•	axe-core for accessibility auditing

Coverage goal: ≥ 90%.

⸻

🧾 Provenance & Integrity

Artifact	Description
Inputs	AI endpoints (/ask, /entity/{id}), Neo4j entity data, STAC metadata
Outputs	React-rendered conversational UI with contextual highlights
Dependencies	React 18+, Axios, Framer Motion, Markdown-it, TypeScript
Integrity	Tested via CI, responses verified with provenance citations, strict TypeScript checks


⸻

🔗 Related Documentation
	•	Web Frontend Components
	•	Context — AIContext
	•	Utilities — aiUtils.js
	•	Web UI Architecture
	•	AI/ML System Overview

⸻

📜 License

Released under the MIT License.
© 2025 Kansas Frontier Matrix — Developed under the Master Coder Protocol (MCP)
for transparent, auditable, and interpretable AI systems.

“Every answer tells a story — the AI Assistant turns Kansas data into dialogue.”


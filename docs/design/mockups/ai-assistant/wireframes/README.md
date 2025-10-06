<div align="center">

# 🤖 Kansas Frontier Matrix — AI Assistant Wireframes  
`docs/design/mockups/ai-assistant/wireframes/`

**Conversational · Knowledge-Linked · Contextual**

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../../docs/)
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../../../docs/design/)
[![Figma Source](https://img.shields.io/badge/Figma-AI%20Assistant%20Wireframes-purple)](../figma-refs.json)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../../LICENSE)

</div>

---

## 🎯 Purpose

This directory contains **Figma-exported wireframes** illustrating the Kansas Frontier Matrix **AI Assistant** — the conversational layer of the system that connects users to the underlying **knowledge graph** and **data catalog** through natural language interaction.

The AI Assistant enables users to:
- Ask questions about Kansas history, geography, or environmental events  
- Receive **grounded, explainable answers** with citations and map/timeline highlights  
- Interact with AI responses (e.g., click entities to reveal context on map or panels)  
- Navigate across datasets or historical events seamlessly via dialogue  

Each wireframe captures a **specific stage of the conversation flow**, showing how AI integrates with the rest of the Frontier Matrix interface.

---

## 📁 Directory Layout

```text
docs/design/mockups/ai-assistant/wireframes/
├── README.md                  # This documentation file
├── ai-assistant-panel.png     # Assistant panel layout
├── conversation-flow.svg      # Flow diagram of dialogue and data retrieval
├── response-citation.png      # Example of AI answer with source references
├── entity-highlight.png       # UI preview showing map/timeline integration
└── figma-refs.json            # Figma node references and export metadata

Each exported wireframe corresponds to a Figma node ID recorded in figma-refs.json for version control and provenance.

⸻

🧩 Conversation Flow Overview

sequenceDiagram
  participant User
  participant Assistant
  participant API
  participant Graph
  participant Map
  User->>Assistant: Ask a historical or spatial question
  Assistant->>API: POST /ask (user_input)
  API->>Graph: Query context entities (places, events, dates)
  API->>Assistant: Inject context + generate response
  Assistant-->>User: Return answer + citations + highlights
  Assistant-->>Map: Highlight referenced locations or events

<!-- END OF MERMAID -->


This flow represents the AI Assistant’s role as a semantic bridge between unstructured user input and structured project data.

⸻

🧠 Design Components

Component	Description	Purpose
Input Bar	Text entry with autocomplete for known entities	Supports natural and structured input
Response Bubble	AI-generated messages with embedded citations	Displays contextual, evidence-based results
Citation List	Links to STAC Items, documents, or knowledge graph entities	Enables provenance verification
Entity Highlight	Interactive references (e.g., “Fort Larned”) linking to map view	Synchronizes conversation with visualization
Feedback Icons	User feedback on helpfulness/accuracy	Enables model fine-tuning via MCP logging


⸻

🧭 Wireframe Details

File	View	Description
ai-assistant-panel.png	Sidebar Interface	Slide-in assistant panel with conversation history and entity linkouts
conversation-flow.svg	Interaction Flow	Depicts message flow between user, API, and graph
response-citation.png	Annotated Response	Example of an AI message with inline citations and map highlights
entity-highlight.png	Map Context	Demonstrates how AI-identified entities appear on the map/timeline


⸻

🎨 Design Tokens (for UI Consistency)

Token	Example	Purpose
--kfm-ai-bg	#0b1020	Assistant panel background
--kfm-ai-accent	#4F9CF9	Button and bubble highlight color
--kfm-ai-text	#ffffff	Text foreground
--kfm-ai-border	#1e2533	Divider and panel border
--kfm-ai-radius	1rem	Bubble and panel rounding

These align with the global design tokens in web/src/styles/tokens.css for visual parity with the rest of the interface.

⸻

🧾 Provenance & Integrity

Asset	Figma Node	Export Date	SHA256
ai-assistant-panel.png	figma://node/70:11	2025-09-30	sha256-6ea2…
conversation-flow.svg	figma://node/70:13	2025-09-30	sha256-90cd…
response-citation.png	figma://node/70:15	2025-09-30	sha256-12df…
entity-highlight.png	figma://node/70:18	2025-09-30	sha256-4a2e…

All wireframes undergo SHA256 checksum verification during CI/CD to ensure integrity and design provenance per MCP standards.

⸻

📚 Related Documents
	•	AI Assistant Design
	•	Prompt Templates
	•	AI System Developer Documentation
	•	Web UI Architecture
	•	System Architecture

⸻

📜 License & Credits

AI Assistant wireframes © 2025 Kansas Frontier Matrix Project.
Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0).
Created by the KFM Design & Interaction Team, following Master Coder Protocol documentation-first and open-design principles for reproducibility, accessibility, and collaborative development.


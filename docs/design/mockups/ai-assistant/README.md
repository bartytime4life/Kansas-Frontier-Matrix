<div align="center">

# 🤖 Kansas Frontier Matrix — AI Assistant  
`docs/design/mockups/ai-assistant/`

**Conversational · Context-Aware · Knowledge-Linked**

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../docs/design/)
[![Backend Integration](https://img.shields.io/badge/API-/ask%20endpoint-orange)](../../../../src/api/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../LICENSE)

</div>

---

## 🎯 Purpose

The **AI Assistant** is the conversational interface of the Kansas Frontier Matrix.  
It enables users to **query the knowledge graph** in natural language and receive **contextual, explainable, and linked responses**—bridging human inquiry and structured historical data.

The assistant integrates:
- 🧠 **AI Models** — NLP and summarization (Hugging Face Transformers, spaCy)
- 🌐 **Knowledge Graph** — Neo4j entities (People, Places, Events, Documents)
- 🗺 **Visualization Hooks** — map/timeline highlights for referenced entities
- 📑 **MCP Logging** — prompt provenance, model versioning, and reproducibility

Its goal is to provide **trustworthy and explainable** historical insight — not speculation — by grounding answers in verified sources and metadata.

---

## 🧩 Architecture Overview

```mermaid
flowchart TD
  A["User Query\nNatural language"] --> B["FastAPI /ask Endpoint"]
  B --> C["Prompt Builder\nContext Assembly"]
  C --> D["AI Model\nTransformer (BART/T5/GPT)"]
  D --> E["Response Parser\nEntities · Links · Citations"]
  E --> F["Frontend (AI Assistant Panel)\nText + Interactive Highlights"]
  C --> G["Knowledge Graph\nNeo4j / Cypher"]
  G --> C
  E --> H["MCP Log\nPrompt · Response · Model Metadata"]

<!-- END OF MERMAID -->


Key Steps
	1.	User submits a question (via web UI or command-line interface).
	2.	The /ask API endpoint builds a context-aware prompt, combining:
	•	User input
	•	Relevant entities from the graph
	•	STAC or document excerpts
	3.	The AI model generates a structured answer (JSON or markdown).
	4.	The parser extracts references (places, people, events) and aligns them with known graph IDs.
	5.	The frontend displays an interactive response — clickable entities light up on the map and timeline.
	6.	Each exchange is logged under MCP provenance for traceability.

⸻

🧠 Conversation Design

Element	Description	Implementation
Prompt Template	Defines how user query + context form the input	Stored in /prompt-templates/ as JSON
Context Injection	Includes top 3–5 relevant entities via graph lookup	Cypher + full-text search
Response Schema	Enforces structured output (JSON: { answer, citations, highlights })	Validated in API layer
Citation Tracking	Attaches STAC item IDs or document URLs to responses	Ensures provenance
Memory Context	Maintains local conversation window (last 3–5 turns)	State managed by frontend React context
Error Handling	Fallback message if graph lacks supporting data	“I couldn’t find verified records for that topic yet.”


⸻

🗂 Directory Layout

docs/design/mockups/ai-assistant/
├── README.md                 # This file
├── wireframes/               # Assistant UI mockups (chat + map highlight)
│   ├── ai-panel.png
│   ├── conversation-flow.svg
│   └── figma-refs.json
├── prompt-templates/         # JSON prompt formats for API /ask
│   ├── historical_query.json
│   ├── document_summary.json
│   └── entity_link.json
└── assistant-flow.json       # High-level UX flow definition (nodes, transitions)

Each file supports documentation-first AI development — every change in the assistant’s logic must be documented before implementation.

⸻

🧾 Example Prompt Template

{
  "template_id": "historical_query",
  "description": "Answers time/place-based questions using Frontier Matrix data.",
  "prompt": "Answer the question based on Kansas historical records.\nQuestion: {{user_input}}\nRelevant Context:\n{{entity_context}}\nInclude citations and confidence scores.",
  "expected_output": {
    "type": "object",
    "properties": {
      "answer": { "type": "string" },
      "citations": { "type": "array", "items": { "type": "string" } },
      "highlights": { "type": "array", "items": { "type": "string" } }
    }
  },
  "model": {
    "engine": "huggingface/bart-large-cnn",
    "temperature": 0.2,
    "max_tokens": 512
  }
}


⸻

💬 Frontend Integration

Component	Description
AI Assistant Panel	Slide-in sidebar that displays responses; supports markdown rendering, clickable citations, and animated highlights.
Input Bar	Uses debounced input with autocomplete for entities and suggestions.
Context Highlights	On receiving a response, the frontend calls /entity/{id} for each reference and highlights those nodes on the map/timeline.
Loading State	Spinner + “Consulting the archive…” message while waiting for model output.

Hotkeys:
	•	Ctrl + / — Focus assistant input
	•	Esc — Close panel
	•	Enter — Submit query

⸻

🔍 Provenance & Logging (MCP Integration)

Every interaction is logged for audit and reproducibility:

Field	Description
timestamp	ISO8601 UTC time of query
user_query	Original input
resolved_entities	Graph nodes included in context
model_id	AI model used
model_version	Model checksum or commit
response_hash	SHA256 of full AI output
citations	Linked sources (STAC IDs, URLs)

Logs are stored in logs/ai/ (outside the docs tree) and versioned periodically.
This ensures scientific-grade traceability of AI outputs per MCP requirements.

⸻

📊 Evaluation Metrics

Metric	Description	Target
Precision (Entity Linking)	% of extracted entities correctly mapped	≥ 90%
Citation Coverage	% of responses including valid source citations	≥ 95%
Latency (Response Time)	Avg. round-trip under 5 seconds	≤ 5s
User Satisfaction	Measured via feedback prompts	≥ 4.5 / 5
Reproducibility	Every answer traceable to data + model version	100%


⸻

🧾 Related Documents
	•	Web UI Architecture
	•	System Architecture
	•	ETL & AI Pipeline
	•	Prompt Template Index

⸻

📜 License & Credits

AI Assistant design © 2025 Kansas Frontier Matrix Project.
Licensed under CC-BY 4.0.
Developed collaboratively by the KFM Design & AI Integration Team, under the Master Coder Protocol for reproducibility, transparency, and open science.


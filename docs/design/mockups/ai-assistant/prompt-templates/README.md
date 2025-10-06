<div align="center">

# 🧠 Kansas Frontier Matrix — AI Assistant Prompt Templates  
`docs/design/mockups/ai-assistant/prompt-templates/`

**Structured · Context-Aware · Grounded in Historical Data**

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../docs/)
[![AI Integration](https://img.shields.io/badge/API-/ask-orange)](../../../../../src/api/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../LICENSE)

</div>

---

## 🎯 Purpose

This directory defines **prompt templates** used by the Kansas Frontier Matrix **AI Assistant** (`/ask` endpoint).  
Each template specifies how **natural language queries** are transformed into structured AI inputs and how responses are validated against the knowledge graph and data catalog.

These templates ensure **reproducibility, interpretability, and provenance** in every AI-generated answer — aligning with the Master Coder Protocol (MCP).

---

## 📁 Directory Layout

```text
docs/design/mockups/ai-assistant/prompt-templates/
├── README.md                   # This documentation
├── historical_query.json        # Answering historical/geospatial questions
├── document_summary.json        # Summarizing archival documents or letters
├── entity_link.json             # Linking text mentions to knowledge graph nodes
└── schema/                      # JSON Schema definitions for validation
    ├── prompt_template.schema.json
    └── ai_response.schema.json

Each .json file defines a reproducible prompt configuration for a specific class of AI tasks,
with version, model, and validation schema fields for MCP traceability.

⸻

🧩 Template Specification

All templates follow this standard schema:

{
  "$schema": "./schema/prompt_template.schema.json",
  "template_id": "string",
  "description": "string",
  "prompt": "string (supports {{placeholders}})",
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
  },
  "version": "0.1.0",
  "license": "CC-BY 4.0"
}


⸻

🧠 Template Types

Template	Description	Model	Output
historical_query.json	Answers user questions about Kansas history (places, dates, events).	BART / T5	Structured JSON with citations and confidence
document_summary.json	Summarizes archival documents, treaties, or diaries into concise text.	BART	Short natural-language summary (≤100 words)
entity_link.json	Matches recognized entities to graph IDs in Neo4j.	spaCy + fuzzy match	JSON mapping of extracted text → entity IDs


⸻

💬 Example: historical_query.json

{
  "template_id": "historical_query",
  "description": "Answers time/place-based questions using Frontier Matrix data.",
  "prompt": "Answer the following question about Kansas history.\nQuestion: {{user_input}}\nRelevant Context:\n{{entity_context}}\nRespond factually with source citations.",
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
    "temperature": 0.25,
    "max_tokens": 512
  },
  "version": "0.1.0"
}

This prompt template is used by the FastAPI /ask endpoint to process natural language queries into reproducible, data-backed answers.
Responses are then validated against ai_response.schema.json before returning to the user.

⸻

🧩 Schema Validation (MCP Rule)

Each prompt and model output must pass validation against its associated JSON Schema:

flowchart TD
  A["User Query"] --> B["Prompt Template"]
  B --> C["LLM Model\n(BART/T5)"]
  C --> D["Response JSON"]
  D --> E["Validation\n(ai_response.schema.json)"]
  E --> F["Frontend Display\n(Map · Timeline · Panels)"]

<!-- END OF MERMAID -->


Validation is performed in the backend pipeline before caching results or sending them to the frontend UI.

⸻

🧾 Provenance & Integrity

Template	Schema	Last Updated	SHA256
historical_query.json	prompt_template.schema.json	2025-09-30	sha256-82a3…
document_summary.json	prompt_template.schema.json	2025-09-30	sha256-f0bd…
entity_link.json	prompt_template.schema.json	2025-09-30	sha256-7e42…

All prompt templates are validated via JSON Schema and tracked in CI (see .github/workflows/schema-validate.yml).

⸻

📚 Related Documents
	•	AI Assistant Design
	•	AI System Developer Documentation
	•	Web UI Architecture
	•	System Architecture
	•	Markdown “Standard Kit”

⸻

📜 License & Credits

Prompt template definitions © 2025 Kansas Frontier Matrix Project.
Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0).
Developed by the KFM AI Integration Team under the Master Coder Protocol — ensuring every prompt and model interaction is documented, versioned, and reproducible.


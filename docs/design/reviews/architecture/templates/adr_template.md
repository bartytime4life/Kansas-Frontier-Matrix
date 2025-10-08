<div align="center">

# 🧭 Kansas Frontier Matrix — Architecture Decision Record (ADR Template)  
`docs/design/reviews/architecture/templates/adr_template.md`

**Purpose:** Document key **architectural decisions** made during Kansas Frontier Matrix (KFM) development —  
capturing context, rationale, alternatives, and consequences.  
All ADRs are versioned, reviewable, and reproducible under the **Master Coder Protocol (MCP)**.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../)  
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../)  
[![Architecture Governance](https://img.shields.io/badge/ADR-Tracked-orange)](../../../)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY--4.0-lightgrey)](../../../../../LICENSE)

</div>

---

## 🧾 ADR Metadata

| Field | Value |
|--------|--------|
| **ADR ID** | `ADR-{{ id }}-{{ slug }}` |
| **Title** | `{{ short_title }}` |
| **Date** | `{{ ISO8601_DATE }}` |
| **Status** | proposed / accepted / superseded / deprecated |
| **Version** | `v{{ semver }}` |
| **Authors / Reviewers** | `@architecture-team`, `@lead-dev`, `@qa-lead` |
| **Component Scope** | ETL · STAC · Graph · API · Web UI |
| **Related Review(s)** | `architecture_review_{{ related_id }}` |
| **Commit Reference** | `{{ GIT_COMMIT }}` |
| **Confidence** | low / medium / high |

---

## 🎯 Context

Describe the architectural challenge or decision point prompting this ADR.  
Include background, constraints, and links to any related tickets or prior ADRs.

> Example: *The team must decide whether to store AI-enriched metadata within the STAC catalog  
or manage it externally in the Knowledge Graph.*

---

## 💡 Decision

Clearly state the **decision made**.  
Summarize the architecture pattern, tool, or approach that was selected and why.

> Example: *We decided to embed AI/ML summary fields within STAC Items as optional extensions  
to improve provenance traceability while maintaining interoperability.*

---

## 🧠 Rationale

Explain **why** this decision was made, referencing:
- Performance considerations  
- Reproducibility / maintainability  
- MCP documentation-first policy  
- Open standards compliance (STAC · CIDOC CRM · OWL-Time)

> Example: *Integrating summaries directly in STAC reduces duplication between metadata stores,  
aligns with FAIR principles, and simplifies the provenance chain.*

---

## ⚖️ Alternatives Considered

| Option | Description | Pros | Cons | Decision |
|---------|--------------|------|------|:--------:|
| **Option A** | Embed summaries in STAC Items | Self-contained metadata | Larger STAC files | ✅ |
| **Option B** | Store summaries in Neo4j graph | Flexible linkage model | Requires Graph API for retrieval | ❌ |
| **Option C** | Maintain summaries as standalone JSON | Easier export | Harder synchronization | ❌ |

---

## 🔍 Implications

| Aspect | Impact | Mitigation / Action |
|---------|---------|--------------------|
| **Data Model** | Slightly larger STAC item size | Optimize compression and schema fields |
| **Performance** | Minimal I/O overhead in STAC load | Use lazy loading in ETL |
| **Interoperability** | Retains compatibility with STAC validators | Validate via CI workflow |
| **Testing** | Update integration tests to include new field | Add case to `tests/stac/test_stac_extensions.py` |

---

## 🧮 Validation & CI Integration

```yaml
# .github/workflows/adr_validate.yml
on:
  pull_request:
    paths:
      - "docs/design/reviews/architecture/adr/**/*.md"
jobs:
  validate-adr:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Validate Markdown format
        run: npx markdownlint-cli2 "docs/design/reviews/architecture/adr/**/*.md"
      - name: Confirm related diagram / review exists
        run: test -f docs/design/diagrams/system_architecture.mmd
````

---

## 🧩 Related Diagrams & References

| Resource                        | Description                         | Path                                                          |
| ------------------------------- | ----------------------------------- | ------------------------------------------------------------- |
| **System Architecture Diagram** | Overall ETL → Graph → API → UI flow | `docs/design/diagrams/system_architecture.mmd`                |
| **Related Review**              | Architecture Review File            | `docs/design/reviews/architecture/{{ related_review }}.md`    |
| **Data Provenance Reference**   | Provenance chain review             | `docs/design/reviews/architecture/provenance_chain_review.md` |

---

## 🧾 Provenance Metadata

```yaml
adr_id: "ADR-{{ id }}-{{ slug }}"
status: "accepted"
decision_date: "{{ ISO8601_DATE }}"
reviewed_by:
  - "@architecture-team"
  - "@data-governance"
  - "@frontend-lead"
commit: "{{ GIT_COMMIT }}"
scope: "ETL | STAC | Graph | API | UI"
related_reviews:
  - "architecture_pipeline_overview_v1.0"
  - "architecture_system_overview_v2.1"
confidence: "high"
summary: >
  Decision accepted. Embedded AI summaries in STAC Items to strengthen provenance alignment.
```

---

## 🪪 License

This Architecture Decision Record (ADR) template is released under **Creative Commons CC-BY 4.0**
© 2025 Kansas Frontier Matrix Architecture Collective

---

<div align="center">

### 🧭 Kansas Frontier Matrix — Architecture Decision Framework

**Documented · Reproducible · Transparent · Standards-Driven**

</div>

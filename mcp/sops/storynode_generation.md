---
title: "📖 KFM SOP — Story Node v3 Generation & Narrative Governance (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "mcp/sops/storynode_generation.md"
version: "v11.0.0"
last_updated: "2025-11-23"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · MCP Board · FAIR+CARE Council · Narrative Governance Team"
status: "Active / Enforced"
doc_kind: "SOP"
intent: "storynode-generation"
semantic_document_id: "kfm-sop-storynode-generation"
doc_uuid: "urn:kfm:mcp:sop:storynode-generation:v11.0.0"
event_source_id: "ledger:kfm:mcp:sop:storynode-generation:v11.0.0"
doc_integrity_checksum: "<sha256>"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

classification: "Governed Narrative Procedure"
sensitivity: "Mixed"
fair_category: "F1-A1-I3-R3"
care_label: "Collective Benefit · Authority to Control · Responsibility · Ethics"
immutability_status: "version-pinned"
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true

governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
signature_ref: "../../releases/v11.0.0/signature.sig"
attestation_ref: "../../releases/v11.0.0/slsa-attestation.json"
sbom_ref: "../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../releases/v11.0.0/manifest.zip"

telemetry_ref: "../../releases/v11.0.0/mcp-sops-telemetry.json"
telemetry_schema: "../../schemas/telemetry/mcp-sops-v11.json"

provenance_chain:
  - "prov:Plan:urn:kfm:mcp:sop:storynode-generation:v11.0.0"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
  - "layout-normalization"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-historical-claims"
  - "governance-override"
  - "sensitive-coordinate-exposure"
---

<div align="center">

# 📖 **KFM SOP — Story Node v3 Generation & Narrative Governance (v11 LTS)**
`mcp/sops/storynode_generation.md`

**Purpose**  
Define the **governed, deterministic, explainable, and CARE-compliant** procedure for generating, validating, and publishing **Story Node v3** entities within the Kansas Frontier Matrix v11 system. Story Nodes are the **primary narrative units** connecting people, places, events, documents, and datasets via **geospatial, temporal, and narrative context**.

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Story_Node-v3-informational" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Governance%20Aligned-orange" />
<img src="https://img.shields.io/badge/Accessibility-WCAG_2.1_AA%2B-blueviolet" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

</div>

---

## 📘 Overview

### 1. Scope (what this SOP governs)

This SOP applies to:

- ✅ All **new Story Node v3** creation
- ✅ **AI-assisted narrative drafting** (Focus Mode v3, CrewAI workers)
- ✅ **Manual historian/archaeologist contributions**
- ✅ Story Node updates triggered by:
  - new datasets
  - new archive integrations
  - new pipeline outputs
  - corrections from human reviewers
  - governance or masking rule changes

This SOP also governs:

- CARE + sovereignty checks
- H3 masking / generalization of sensitive spatial references
- schema validation and graph ingestion validation
- provenance logging (PROV-O + OpenLineage references)

### 2. Core principles (normative)

- **Deterministic by default:** every step must be replayable from config + inputs.
- **Evidence-led narrative:** every factual claim must map to a dataset/document/graph entity.
- **Governance-first:** sovereignty and CARE constraints override convenience or completeness.
- **No speculation:** Story Node v3 narrative must not invent missing facts.
- **Accessibility:** outputs must remain usable and navigable under WCAG 2.1 AA+ expectations.

### 3. Definitions (operational)

- **Story Node v3:** a governed narrative entity that binds **spacetime** + **relations** + **provenance** + **narrative**.
- **Focus Mode v3:** the UI/experience that renders story node context using the **Context · Timeline · Map** panels.
- **Sensitive spatial reference:** any location that requires masking/generalization under sovereignty policy, including cultural/heritage sites or restricted geographies.
- **Masking:** reducing precision (e.g., H3 R7–R9) or removing geometry entirely when governance requires it.

---

## 🗂️ Directory Layout

~~~text
. 🧭 (repo root)
├── mcp/ 🧪 (protocol artifacts)
│   └── sops/
│       └── storynode_generation.md 📖 (this SOP)
├── data/ 🗃️ (data + lineage)
│   ├── work/storynodes/context/ 🧾 (deterministic context packages)
│   │   └── <node-id>.json 📦 (graph + dataset + document neighborhood)
│   ├── processed/storynodes/ 📚 (published Story Node v3 entities)
│   │   └── <node-id>.json 🗺️ (Story Node v3 JSON)
│   └── provenance/storynodes/ 🔗 (lineage bundles)
│       └── <node-id>.jsonld 🧬 (PROV-O JSON-LD + OpenLineage refs)
├── schemas/ 🧾 (contracts)
│   ├── story-node.schema.json ✅ (Story Node v3 JSON Schema)
│   └── shacl/storynode-v3-shape.ttl ✅ (Story Node v3 SHACL shape)
├── src/ 🧠 (pipelines)
│   └── pipelines/storynode/ ⚙️ (generation + validation)
└── .github/workflows/ 🤖 (CI)
    └── mcp-validate.yml ✅ (docs + governance + provenance enforcement)
~~~

---

## 🧭 Context

### 1. Required inputs

| Input | Description | Must be governed? |
|---|---|---|
| Source datasets | STAC/DCAT registered datasets with lineage | Yes |
| Graph entities | Place/Event/Document/Dataset/Person-Group nodes and relations | Yes |
| Geospatial geometry | GeoJSON + masking plan (H3) if sensitive | Yes |
| Temporal information | OWL-Time instant/interval semantics | Yes |
| Provenance | PROV-O activity chain references and checksums | Yes |
| Narrative draft | AI or human text, constrained by this SOP | Yes |
| Metadata contracts | JSON Schema + SHACL shape references | Yes |

### 2. Optional inputs

- Images (only with explicit rights + license metadata)
- Maps/overlays for the Focus Mode map panel (non-sensitive by default)
- Cross-links to related Story Nodes (typed + validated)

### 3. Context extraction output (context package)

Context extraction MUST produce a machine-readable context package per Story Node:

- graph neighborhood (2–3 hop, configured)
- dataset metadata (STAC/DCAT identifiers)
- document references (IDs + snippets pointers)
- candidate spatial + temporal extents
- masking directives (if any)
- constraints for narrative generation (if AI is used)

Stored at:

~~~text
data/work/storynodes/context/<node-id>.json
~~~

Minimal shape (illustrative):

~~~json
{
  "node_id": "<node-id>",
  "context_hops": 2,
  "entities": [
    {"type": "Place", "id": "urn:kfm:place:..."},
    {"type": "Event", "id": "urn:kfm:event:..."}
  ],
  "datasets": [
    {"id": "stac:...", "dcat_id": "dcat:..."}
  ],
  "spacetime": {
    "geometry": {"type": "Polygon", "coordinates": []},
    "when": {"start": "YYYY-MM-DD", "end": "YYYY-MM-DD"}
  },
  "masking": {
    "required": true,
    "method": "H3",
    "resolution": "R7"
  },
  "constraints": {
    "no_speculation": true,
    "require_citations": true,
    "neutral_tone": true
  }
}
~~~

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A[Start: Story Node request] --> B[Extract context: Neo4j + STAC/DCAT]
  B --> C[Apply masking + governance filters]
  C --> D{AI drafting enabled?}
  D -->|Yes| E[Generate draft panels + citations]
  D -->|No| F[Human draft]
  E --> G[Human review + edits]
  F --> G
  G --> H[Build Story Node v3 JSON]
  H --> I[Validate: Schema + SHACL + GeoSPARQL + OWL-Time]
  I --> J{Pass?}
  J -->|No| K[Remediate + re-run validations]
  J -->|Yes| L[Write PROV-O + reference OpenLineage]
  L --> M[Commit outputs + ingest graph]
  M --> N[Publish gate: required approvals]
~~~

---

## 🧱 Architecture

### 1. Deterministic procedure (step-by-step)

#### Step 1 — Extract & prepare context
- Query Neo4j for a configured neighborhood (typically 2–3 hops).
- Collect: facts, dates, locations, actors.
- Collect: dataset provenance references (STAC/DCAT).
- Collect: relevant documents, media, and artifact references (if allowed).

Output:

~~~text
data/work/storynodes/context/<node-id>.json
~~~

#### Step 2 — Create narrative draft (AI + human)
If AI is used (Focus Mode v3 and/or CrewAI workers), the generator MUST:

- generate **Context · Timeline · Map** draft text/panels
- keep statements strictly grounded in provided context
- attach citations or stable references for each factual claim
- obey prohibitions:
  - no speculation
  - no genealogical inference
  - no restricted coordinate disclosure
  - no culturally biased/colonial phrasing

Human experts MUST review and edit for:

- factual correctness
- cultural sensitivity and governance compliance
- neutral tone and clarity
- accessibility (readability, structure)

#### Step 3 — Apply CARE & sovereignty filters
Required checks:

- Sensitive site or sensitive geography? → apply masking/generalization.
- Tribal relevance? → apply sovereignty tags and review route.
- Trauma/conflict topic? → apply narrative ethics style constraints.
- Any Tier A dataset implicated? → route to FAIR+CARE Council review.

Masking metadata MUST be recorded as structured metadata (not prose-only).

#### Step 4 — Build Story Node v3 JSON
Populate the Story Node v3 JSON entity using the official contracts:

~~~text
schemas/story-node.schema.json
schemas/shacl/storynode-v3-shape.ttl
~~~

#### Step 5 — Validate against the knowledge graph
- Every relation must resolve to an existing entity ID.
- Geometry must be valid and compliant with masking rules.
- Time must be OWL-Time compatible (instant or interval) and internally consistent.
- CIDOC-CRM role expectations must be satisfied.

#### Step 6 — Lineage logging (PROV-O + OpenLineage references)
Record:

- `prov:used` (datasets, documents, models)
- `prov:wasGeneratedBy` (activities: extraction, draft, review, publish)
- `prov:wasAssociatedWith` (agents: humans, CI, services)
- model versions + seeds (if AI used)
- masking and redaction decisions

Write lineage bundle:

~~~text
data/provenance/storynodes/<node-id>.jsonld
~~~

#### Step 7 — Commit outputs & publish
Write the final Story Node entity:

~~~text
data/processed/storynodes/<node-id>.json
~~~

Then (governed gate):

- register any STAC alignment assets (if applicable)
- ingest into Neo4j
- record governance ledger update (event_source_id lineage)
- generate Focus Mode preview
- require approvals before publication (see Governance section)

---

## 📦 Data & Metadata

### 1. Required Story Node v3 fields (normative)

A Story Node v3 JSON MUST include, at minimum:

1. `id`  
   Stable UUID/URN/ARK/DOI.

2. `type`  
   Must be `story-node`.

3. `title`  
   Human-readable, concise, accessibility-friendly.

4. `narrative`  
   - `body`: factual narrative (no speculation)
   - `format`: `markdown` or `text`
   - `citations`: stable references to datasets/documents/entities
   - `alternates`: optional language/audience variants
   - `media`: optional references (rights required)

5. `spacetime`  
   - `geometry`: GeoJSON (masked/generalized if required)
   - `bbox`: optional
   - `crs`: default `EPSG:4326` unless contract specifies otherwise
   - `place_labels`: human-readable names
   - `when`: OWL-Time aligned start/end

6. `relations`  
   Typed edges to graph entities (validated IDs). Examples:
   - `references`
   - `part_of`
   - `follows`
   - `influenced_by`
   - `located_in`

7. `provenance`  
   Pointers to PROV-O bundle + checksums.

8. `care_classification` and sovereignty markers  
   Structured fields describing CARE tier, masking, and review requirements.

### 2. Narrative constraints (facts vs interpretation)

Story Nodes MUST separate and label:

- **Facts:** directly supported by sources
- **Interpretation:** reasoned from facts (explicitly labeled)
- **Speculation:** must be omitted (Story Node v3 forbids speculative additions)

When interpretation is allowed by governance, it MUST be explicitly labeled and bounded by evidence.

### 3. Masking requirements (H3 + generalization)

When masking is required:

- degrade geometry to H3 cells at the required resolution (typically R7–R9)
- avoid storing raw coordinates for restricted places
- store masking method and resolution in structured metadata
- ensure map panel uses masked geometry only

---

## 🌐 STAC, DCAT & PROV Alignment

### 1. STAC alignment (optional but supported)

A Story Node may be represented as a STAC Item when it is useful for cataloging:

- `geometry` may be masked geometry or null (if fully non-spatial)
- `properties.datetime` should align to `last_updated` or the Story Node temporal anchor
- `assets` may include:
  - the Story Node JSON (`application/json`)
  - related media (with rights)
  - the PROV-O JSON-LD bundle (`application/ld+json`)

### 2. DCAT alignment (catalog record expectations)

Story Nodes SHOULD be discoverable via DCAT views as documentation-like records or narrative entities:

- use `semantic_document_id` as a stable identifier mapping
- include license + publisher/creator metadata
- include temporal and spatial coverage (masked where required)

### 3. PROV-O requirements (mandatory)

Each Story Node MUST have a PROV-O lineage bundle that:

- captures input datasets and documents
- captures generation activities and human review
- captures masking decisions as explicit activities or attributes
- references OpenLineage events when present (do not embed secrets/tokens)

---

## 🧠 Story Node & Focus Mode Integration

### 1. Focus Mode panels (Context · Timeline · Map)

Focus Mode v3 renders Story Nodes using:

- **Context Panel:** key facts + evidence pointers
- **Timeline Panel:** OWL-Time aligned events and ordering
- **Map Panel:** GeoJSON or masked-H3 geometry with safe extents

### 2. Allowed Focus Mode behaviors (bounded transformations)

Focus Mode MAY:

- summarize existing sections
- generate a timeline view of already-grounded events
- highlight entities and relationships already present
- extract metadata fields for indexing

Focus Mode MUST NOT:

- alter normative requirements in this SOP
- invent governance status or approvals
- fabricate provenance or dataset relationships
- infer sensitive locations or genealogies

### 3. Story Node ingestion expectations

Before a Story Node is allowed into the graph:

- all relations must resolve (no dangling references)
- provenance bundle must exist
- masking must be applied where required
- narrative must pass neutrality + safety filters

---

## ⚖ FAIR+CARE & Governance

### 1. CARE classification (required)

Each Story Node MUST carry CARE classification and review routing:

- **Tier A:** high risk (sovereignty-sensitive / restricted) → Council review required
- **Tier B:** moderate risk → governance check + domain reviewer
- **Tier C:** low risk → standard CI + reviewer approval

### 2. Sovereignty requirements (hard constraints)

- Never expose restricted coordinates in narrative, metadata, or diagrams.
- Apply masking/generalization for sensitive geographies by default.
- If a dataset or entity is sovereignty-protected, it may bypass AI drafting entirely.
- Human approval is mandatory for any publication touching sovereignty-tagged content.

### 3. Narrative ethics requirements

- neutral tone; avoid colonial framing and bias
- avoid sensationalizing trauma/conflict
- prefer primary sources and explicit uncertainty when allowed
- do not infer motivations, intent, or identity beyond evidence

---

## 🧪 Validation & CI/CD

### 1. Local validation runbook (minimum)

Run validations before committing Story Node outputs:

~~~text
schema-lint-v11 schemas/story-node.schema.json data/processed/storynodes/<node-id>.json
shacl-validate-v11 schemas/shacl/storynode-v3-shape.ttl data/processed/storynodes/<node-id>.json
~~~

### 2. CI enforcement

CI is expected to enforce at minimum:

- Markdown structure compliance (H1/H2 registry)
- directory layout fencing rules
- presence and consistency of front-matter keys
- provenance existence and coherence
- masking rules (no sensitive coordinate leakage)
- accessibility checks (heading order, list semantics)

Workflow reference:

~~~text
.github/workflows/mcp-validate.yml
~~~

### 3. Verification checklist (release gate)

Must pass before publishing:

- Story Node JSON schema validation
- SHACL validation
- CARE + sovereignty review route satisfied
- masking applied where required
- narrative ethics compliance
- provenance bundle present (PROV-O + OpenLineage references)
- STAC/DCAT alignment (when declared)
- graph ingestion tests
- accessibility checks
- CI green

### 4. Failure modes & recovery

Common failures:

- speculative or unverified claims
- sensitive coordinate exposure
- relations to missing graph entities
- temporal inconsistencies
- incomplete provenance bundle

Recovery actions:

- remove or rewrite unverifiable content
- apply/strengthen masking (H3)
- repair entity references and rerun graph checks
- correct time bounds and revalidate OWL-Time mapping
- regenerate provenance bundle and rerun CI

### 5. Telemetry & sustainability (required logging)

When Story Node generation uses compute (especially AI):

- record runtime duration
- record energy (Wh / kWh) and carbon estimate (gCO₂e) when available
- record I/O volume and any GPU-hours if used

Telemetry storage:

~~~text
releases/<version>/mcp-sops-telemetry.json
~~~

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.0.0 | 2025-11-23 | Initial Story Node v3 SOP with deterministic pipeline, provenance requirements, and governance routing. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MCP-DL v6.3  
Diamond⁹ Ω / Crown∞Ω Certified · FAIR+CARE Compliant · Narrative Governance Enforced

**Governance:** [ROOT-GOVERNANCE.md](../../docs/standards/governance/ROOT-GOVERNANCE.md) · **Ethics:** [FAIRCARE-GUIDE.md](../../docs/standards/faircare/FAIRCARE-GUIDE.md) · **Sovereignty:** [INDIGENOUS-DATA-PROTECTION.md](../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

</div>

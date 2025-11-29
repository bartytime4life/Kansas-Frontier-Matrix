---
title: "🧠 Kansas Frontier Matrix — Graph & Entity Utilities (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/utils/graph/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"
review_cycle: "Quarterly · FAIR+CARE Council & Web Architecture Board"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-utils-graph-v11.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11.0"

status: "Active / Enforced"
doc_kind: "Architecture"
intent: "web-graph-utilities"
role: "frontend-graph-normalization"
category: "Web · Graph · Utilities · Focus Mode · Story Nodes"

classification: "Public"
fair_category: "F1-A2-I2-R3"
care_label: "Public · Governed"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

risk_category: "Low"
redaction_required: false

provenance_chain:
  - "web/src/utils/graph/README.md@v10.3.1"
  - "web/src/utils/graph/README.md@v10.3.2"
  - "web/src/utils/graph/README.md@v10.4.1"
provenance_requirements:
  versions_required: true
  newest_first: true

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "SoftwareSourceCode"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../schemas/json/web-utils-graph-readme-v11.schema.json"
shape_schema_ref: "../../../../schemas/shacl/web-utils-graph-readme-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:web-utils-graph-readme:v11.2.2"
semantic_document_id: "kfm-doc-web-utils-graph-readme"
event_source_id: "ledger:web/src/utils/graph/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "summaries"
  - "speculative-additions"
  - "unverified-historical-claims"
  - "relationship-fabrication"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next graph-utils revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧠 **Kansas Frontier Matrix — Graph & Entity Utilities (v11.2.2)**  
`web/src/utils/graph/README.md`

**Purpose**  
Define the **frontend-side normalization, relationship flattening, subgraph extraction,  
entity merging, provenance propagation, and Focus Mode v3 bindings** used by the KFM  
Web Platform to transform Neo4j + API graph responses into **stable, deterministic,  
governance-safe UI structures**.

These utilities are:
- deterministic  
- typed  
- FAIR+CARE-governed  
- sovereignty-safe  
- fully aligned with Story Node v3 + Focus Mode v3  
- essential to map/timeline/focus synchronization  

</div>

---

# 🧭 Overview

The `web/src/utils/graph/` directory contains **pure functional TypeScript modules** responsible for:

- 🔄 **Normalizing** Neo4j graph nodes and relationships  
- 🪢 **Flattening** and sanitizing subgraphs into UI-ready arrays  
- 🧱 **Binding** graph entities to Focus Mode v3 + Story Node v3  
- 📍 **Spatial + temporal** extraction from graph structures  
- 🧬 **Provenance injection** (PROV-O, CARE labels, sovereignty flags)  
- 🔐 **Governance filtering** (masking, generalization, sensitive relationship suppression)  
- 🧊 **Deterministic ordering** for stable UI renders  
- ⚡ **High-performance graph transforms** without side effects  

These modules **NEVER**:
- touch the DOM  
- call the network  
- mutate global state  
- bypass FAIR+CARE constraints  

---

# 📂 Directory Layout (Emoji-Rich · v11.2.2)

~~~text
web/src/utils/graph/
│
├── 🧩 entityNormalize.ts     # Canonicalizes entities (Place/Event/StoryNode/Document/etc.)
├── 🔗 relationFlatten.ts     # Converts nested Neo4j subgraphs → flat edges + deduped nodes
├── 🎯 focusBindings.ts       # Focus Mode v3 entity → map/timeline binding logic
├── 🆔 idUtils.ts             # Stable ID hashing, deduplication, entity merging
└── 🗂️ groupByType.ts         # Splits heterogeneous node arrays into typed buckets
~~~

---

# 🧱 Module Descriptions

## 🧩 `entityNormalize.ts`

Normalizes raw Neo4j nodes into stable, UI-ready **canonical entities**.

**Features**

- Type canonicalization:  
  `Place | Event | Person | Document | StoryNode | Dataset`
- Temporal normalization (OWL-Time aligned)  
- Spatial extraction (GeoJSON-safe)  
- CARE-protected spatial masking (generalization)  
- Provenance merging:  
  - PROV-O `prov:used`, `prov:wasGeneratedBy`  
  - license, rights-holder, SBOM origin  
- Story Node v3 compatible shape  
- Focus Mode v3 compatible narrative model  

**Guarantees**

- No speculative fields  
- No hidden precision leaks  
- Deterministic output ordering  

---

## 🔗 `relationFlatten.ts`

Neo4j returns **deep nested subgraphs**.  
The UI requires **predictable, flat structures**.

**Performs**
- Extracts `{ nodes[], relationships[] }` → `{ flatNodes[], edges[] }`
- Deduplicates repeated nodes/edges
- Orders edges by semantic relationship importance  
- Applies sensitivity masking:
  - removes prohibited relationships  
  - generalizes links with sovereignty restrictions  

**Used by**

- Story Node relation panels  
- Focus Mode v3 evidence trails  
- Graph-derived timelines  
- “Related entities” UI modules  

---

## 🎯 `focusBindings.ts`

The glue binding **graph entities → Focus Mode v3 context**.

Computes:

- Highlighted Places, Events, Story Nodes  
- Time window for the focal entity  
- Spatial extents (BBox safely clamped)  
- Related entity clusters  
- CARE/sovereignty narratives (for overlays)  
- A stable `FocusContext`:

```ts
interface FocusContext {
  focusId: string;
  relatedPlaces: string[];
  relatedEvents: string[];
  relatedDocuments: string[];
  relatedStoryNodes: string[];
  timelineWindow: { start: string; end?: string };
  bbox: [number, number, number, number] | null;
  governance: { careLabel: string; sovereignty?: string };
}
```

---

## 🆔 `idUtils.ts`

Ensures **deterministic identity**:

- ID hashing + normalization  
- Deduplication of arrays and graphs  
- Composite ID generation for multi-entity relationships  
- Stable ordering for React key usage  

**Guarantees**

- No collisions  
- No nondeterminism  
- No sensitive key exposure in URLs  

---

## 🗂️ `groupByType.ts`

Groups heterogeneous graph nodes into:

```ts
{
  places: [...],
  events: [...],
  documents: [...],
  storyNodes: [...],
  datasets: [...],
  people: [...]
}
```

Used by:

- Focus Mode v3 relation panels  
- Story Node v3 contextual linking  
- Graph-based search  
- Relationship overlays  

---

# 🧪 Testing Requirements

All graph utilities MUST have:

- Deterministic normalization tests  
- CARE-compliance tests (masking, sensitive suppression)  
- Provenance propagation tests  
- Temporal normalization tests  
- Spatial extraction tests  
- Relationship flattening truth tables  
- ID stability tests  
- FocusContext generation tests  

All located under:

~~~text
tests/unit/web/utils/graph/**
tests/integration/web/utils/graph/**
~~~

---

# ⚙️ Development Standards

Modules MUST:

- Be pure, side-effect-free  
- Use TypeScript strict mode  
- Avoid DOM/React/MapLibre imports  
- Follow KFM-PDC v11 data contracts  
- Comply with FAIR+CARE & sovereignty rules  
- Pass lint/format/test/MDP validation  
- Implement JSDoc for all exported functions  
- Remain cyber/sovereignty safe  

---

# 🧭 Future Extensions (v11.3+)

- Cross-entity confidence inference for timelines  
- Story Node cluster-merging heuristics  
- Multi-graph federation adapters  
- Contextual subgraph compression for mobile  
- Provenance-guided color semantics  

---

# 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-28 | Full upgrade to KFM-MDP v11.2.2; emoji directory refresh; aligned with Focus Mode v3, Story Node v3, CARE masking, and CI/CD schema updates. |
| v10.4.1 | 2025-11-15 | Initial v10.4 graph-utils documentation. |
| v10.3.2 | 2025-11-14 | Early graph extraction logic. |
| v10.3.1 | 2025-11-13 | Initial utilities overview. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  

[⬅️ Back to Web Source](../../README.md) · [🌐 Web Platform Overview](../../../README.md) · [🛡 Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
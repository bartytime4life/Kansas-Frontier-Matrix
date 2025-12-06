---
title: "📡 KFM v11.2.4 — SNS Message Filtering Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/messaging/sns-filtering/README.md"
version: "v11.2.4"
last_updated: "2025-12-06"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Event Systems Board · FAIR+CARE Oversight"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x ingestion-contract compliant"
status: "Active / Enforced"

doc_kind: "Architecture Guide"
intent: "sns-message-filtering-architecture"
role: "event-routing-architecture"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "messaging"
  applies_to:
    - "sns"
    - "sqs"
    - "event-routing"
    - "alerting"
    - "etl"
    - "ai-workloads"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "KFM-Open"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: false
risk_category: "Event Systems Architecture"
redaction_required: false

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-hash>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "releases/v11.2.4/sbom.spdx.json"
manifest_ref: "releases/v11.2.4/manifest.zip"
telemetry_ref: "releases/v11.2.4/pipelines-telemetry.json"
telemetry_schema: "schemas/telemetry/event-systems-v1.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-v2.json"

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/pipelines/messaging/sns-filtering/README.md@v11.2.4"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: false
  must_reference_origin_root: true

json_schema_ref: "schemas/json/docs-pipelines-messaging-sns-filtering-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/docs-pipelines-messaging-sns-filtering-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"

doc_uuid: "urn:kfm:doc:pipelines:messaging:sns-filtering:v11.2.4"
semantic_document_id: "kfm-pipelines-messaging-sns-filtering-v11.2.4"
event_source_id: "ledger:kfm:doc:pipelines:messaging:sns-filtering:v11.2.4"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "metadata-extraction"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 Context"
    - "🧱 Architecture"
    - "📦 Data & Metadata"
    - "🧪 Validation & CI/CD"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"

diagram_profiles:
  - "mermaid-flowchart-v1"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "accessibility-check"
  - "footer-check"
  - "provenance-check"

ci_integration:
  workflow: ".github/workflows/event-systems-sns-filtering.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Deterministic Routing × Low-Noise Pipelines × Sustainable Intelligence"
  architecture: "SNS Filters · SQS Consumers · lakeFS/Lineage-Aware Eventing"
  analysis: "Event Systems · Telemetry-Driven · FAIR+CARE Grounded"
  data-spec: "STAC/DCAT/PROV-Compatible Event Metadata"
  telemetry: "Delivered vs Filtered · Latency · Attribute Health"
  graph: "Topics · Subscriptions · Contracts"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_version_history: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true

deprecated_fields: []
---

<div align="center">

# 📡 **SNS Message Filtering Architecture**  
`docs/pipelines/messaging/sns-filtering/README.md`

**Purpose:**  
Define the **canonical SNS message filtering architecture** for KFM v11.2.4 so that event routing is **deterministic**, **contract-visible**, and **FAIR+CARE aligned**, while minimizing noise, cost, and downstream retry load across Atmospheric, Hydrology, Soil, Heritage, and Real-Time Observations pipelines.

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j knowledge graph → API layer → React/MapLibre/Cesium frontend → Story Nodes → Focus Mode.

</div>

---

## 📘 Overview

Amazon SNS filtering is a foundational mechanism for reducing noise and downstream pressure in KFM’s event systems.  
This guide establishes:

- The **filter policy types** used across KFM,  
- The **publisher attribute/body contract**,  
- The **subscriber responsibilities** for reliability and governance, and  
- How the filtering layer aligns with **STAC/DCAT/PROV** and **FAIR+CARE**.

SNS filtering in KFM must achieve:

1. **Deterministic routing** — a message with a given attribute set always routes to the same set of subscribers.  
2. **Contract-visible filtering** — filters are documented, versioned, and testable.  
3. **Zero-drift schemas** — attributes and JSON-body fields align with DCAT/STAC/PROV metadata keys.  
4. **Cost & compute discipline** — subscribers receive only relevant messages.  
5. **Low-noise AI workloads** — AI/ETL pipelines are shielded from irrelevant trigger storms.  
6. **CARE-aligned sharding** — sensitive geospatial categories are filterable without leaking precise site information.

---

## 🗂️ Directory Layout

Authoritative layout for SNS filtering docs and supporting materials:

~~~text
KansasFrontierMatrix/
├── 📂 docs/
│   └── 📂 pipelines/
│       └── 📂 messaging/
│           └── 📂 sns-filtering/
│               ├── 📄 README.md                 # This file (architecture guide)
│               ├── 📂 examples/
│               │   ├── 📄 attribute-filter.json # Canonical attribute-based filter
│               │   ├── 📄 body-filter.json      # Canonical body-based filter
│               │   └── 📄 publisher-contract.md # Detailed attribute/body contract
│               └── 📂 tests/
│                   ├── 📄 contract-tests.md     # Publisher/consumer contract tests
│                   └── 📄 filter-validation.md  # Filter policy validation patterns
│
├── 📂 infra/
│   └── 📂 terraform/
│       └── 📂 messaging/
│           └── 📄 sns_filters.tf                # Terraform module(s) for SNS filters
│
├── 📂 src/
│   └── 📂 pipelines/
│       └── 📂 messaging/
│           └── 📂 sns_filtering/
│               ├── 📄 __init__.py
│               ├── 📄 filter_policies.py        # In-code representations of filter policies
│               ├── 📄 publisher_sdk.py          # Helpers enforcing attribute/body contract
│               ├── 📄 subscriber_adapter.py     # Subscription bindings & dead-letter wiring
│               ├── 📄 contract_validator.py     # Runtime checks against message schemas
│               └── 📄 telemetry_adapter.py      # Export delivered/filtered/latency metrics
│
└── 📂 .github/
    └── 📂 workflows/
        └── 📄 sns-filtering-contract-checks.yml # CI job for policy + contract validation
~~~

**Author rules:**

- All SNS filtering documentation lives under `docs/pipelines/messaging/sns-filtering/`.  
- Terraform, code modules, and tests must reference this document in comments or module docs.  
- Any new subdirectory under these trees must be added to this layout with an emoji and concise description.

---

## 🧭 Context

SNS sits at the **event-router layer** of KFM:

- Publishers emit **domain events** (e.g., hydro station updates, soils parcel deltas, heritage sensitivity updates).  
- SNS topics **fan out** events to SQS queues, Lambda functions, or other endpoints.  
- Filter policies determine **which subscribers see which messages**, acting as the first line of routing and noise control.

Within the KFM architecture:

- Filter policies must be **compatible** with STAC/DCAT metadata and PROV entities (e.g., `dataset`, `productLevel`, `env`).  
- Filtering decisions are part of the **provenance story**: why a given pipeline ran or did not run.  
- CARE and sovereignty overlays may restrict certain event flows; SNS filtering is one of the tools that enforces those constraints at the messaging layer.

---

## 🧱 Architecture

### Filter Policy Types Used in KFM

#### Attribute-Based Filtering (Preferred)

Used when:

- Publishers already define **message attributes**.  
- Routing must remain stable across minor body schema changes.  
- Low-latency, infrastructure-native filtering is desired.

Typical attribute keys:

- `env` (environment: `dev`, `stage`, `prod`)  
- `topicKind` (taxonomy root for routing; e.g., `hydro.river.gauge`)  
- `productLevel` (L0–L4)  
- `stationId` (for station-bound data)  
- `h3_bucket` (for spatial sharding)

Example attribute-based filter policy (SQS subscription):

~~~json
{
  "FilterPolicy": {
    "stationId": ["KICT", "KTOP"],
    "productLevel": ["L2", "L3"],
    "env": ["prod"],
    "topicKind": [{ "prefix": "hydro." }]
  }
}
~~~

Publisher contract example:

~~~bash
aws sns publish \
  --topic-arn arn:aws:sns:us-east-1:123456789012:events \
  --message '{"ts":"2025-12-06T00:00:00Z","value":12.3}' \
  --message-attributes '{
    "stationId":{"DataType":"String","StringValue":"KICT"},
    "productLevel":{"DataType":"String","StringValue":"L2"},
    "env":{"DataType":"String","StringValue":"prod"},
    "topicKind":{"DataType":"String","StringValue":"hydro.river.gauge"}
  }'
~~~

#### JSON Body Filtering (Allowed for Structured Payloads)

Used when:

- Body schema is **fixed and versioned**.  
- Multiple services publish the same **shared schema**.  
- Attributes would otherwise duplicate fields already present in the body.

Requirement: `FilterPolicyScope` must be set to `"MessageBody"`.

Example policy:

~~~json
{
  "FilterPolicy": {
    "station.id": ["KICT", "KTOP"],
    "product.level": ["L2", "L3"],
    "kind": [{ "prefix": "hydro." }]
  },
  "FilterPolicyScope": "MessageBody"
}
~~~

Expected payload example:

~~~json
{
  "station": { "id": "KICT" },
  "product": { "level": "L2" },
  "kind": "hydro.river.gauge",
  "ts": "2025-12-06T00:00:00Z",
  "value": 12.3
}
~~~

### Advanced Matching Patterns Used in KFM

KFM uses the full SNS filter syntax carefully, prioritizing readability and deterministic behavior.

| Pattern          | Use-Case                            | Example                                           |
|------------------|-------------------------------------|---------------------------------------------------|
| `anything-but`   | Exclude noisy product levels        | `"productLevel": { "anything-but": ["L0"] }`      |
| Numeric ranges   | Spatial buckets / sensor levels     | `"h3_bucket": [{ "numeric": [">=", 5, "<=", 15] }]` |
| Prefix           | Topic taxonomies                    | `"topicKind": [{ "prefix": "soil." }]`           |
| Exists           | Contract enforcement                | `"stationId": { "exists": true }`                |

### Publisher Contract (KFM-Wide)

Every message **must** include the following attributes (unless explicitly exempted by a documented contract):

| Field           | Required?     | Description                                           |
|-----------------|--------------|-------------------------------------------------------|
| `env`           | Yes          | One of: `dev`, `stage`, `prod`                       |
| `topicKind`     | Yes          | Taxonomy root for routing                            |
| `productLevel`  | Yes          | `L0`–`L4`, dataset maturity indicator                |
| `stationId`     | Conditional  | Required for station-bound data                      |
| `h3_bucket`     | Conditional  | Required for geospatial sharding / H3-based routing  |
| `schema_version`| Yes          | Ensures filter stability and body-contract version   |

Rules:

- All attributes must use correct **DataType** (`String`, `Number`, or `String.Array`).  
- `schema_version` is used to gate **breaking changes** in routing contracts.  
- Contracts must be documented in `publisher-contract.md` and versioned.

### Subscriber Responsibilities

Subscribers must:

1. **Validate the publish contract** (schema + required attributes) before processing.  
2. **Rely on SNS filters** — no re‑implementing the same logic server‑side in ad‑hoc ways.  
3. **Emit lineage records** into OpenLineage / PROV‑O to show which events were processed.  
4. **Report filter-drop metrics** (cases where messages should have matched but did not).  
5. **Fail closed**: if a filter behaves unexpectedly (e.g., volume collapse), halt consumption and raise a reliability signal.

---

## 📦 Data & Metadata

SNS filtering is tightly coupled to KFM’s metadata stack:

- **DCAT / STAC**  
  - Attributes like `env`, `productLevel`, `topicKind`, `stationId`, and `h3_bucket` map onto dataset metadata fields (e.g., `dct:spatial`, `dct:conformsTo`, STAC `properties.*`).  
- **PROV‑O**  
  - Subscription and consumption can be modeled as Activities that **use** event Entities and **generate** downstream dataset Entities.  
- **Story Nodes / Focus Mode**  
  - Event metadata allows Story Nodes to link back to **which event streams** drove updates to KFM narratives and maps.

Recommended alignment:

- Each SNS topic and subscription should be represented in the **Neo4j graph** as nodes and relationships so that event flows are navigable in the lineage graph.  
- Attributes used in filters should have corresponding **schema definitions** (JSON Schema / SHACL) and be included in telemetry exports for contract auditing.

---

## 🧪 Validation & CI/CD

KFM CI must enforce:

- **Filter policy validation**  
  - All policies under `infra/terraform/messaging/` must validate as proper SNS filter JSON.  
  - A small unit test suite should confirm that **sample messages** are routed as expected.

- **Publisher contract tests**  
  - Contract tests in `docs/pipelines/messaging/sns-filtering/tests/contract-tests.md` must include scenarios for each env, topicKind, and productLevel.  

- **Schema & contract drift checks**  
  - Any change to `schema_version` or attribute semantics must trigger contract tests and be reviewed by the Event Systems Board + FAIR+CARE Oversight.

- **Telemetry checks**  
  - Telemetry documents must conform to `schemas/telemetry/event-systems-v1.json`.  
  - Metrics should include:
    - Delivered messages/sec per subscription.  
    - Filtered-out messages/sec per subscription.  
    - End‑to‑end latency (publish → consume).  
    - Attribute presence/validity statistics (cardinality‑safe).

---

## ⚖ FAIR+CARE & Governance

Filtering is not just a technical optimization; it is part of **governance and ethics**:

- **FAIR**  
  - Filter policies and publisher contracts are documented, versioned, and discoverable alongside pipeline docs.  
  - Event attributes map cleanly to DCAT/STAC fields for interoperable catalogs.  

- **CARE**  
  - CARE‑aligned sharding (`h3_bucket` and `topicKind` for sensitive domains) helps ensure that sensitive geospatial event streams are routed only to authorized subscribers.  
  - Event attribute design avoids accidentally disclosing exact locations or identifiers where CARE or sovereignty policies require generalization.  

Governance rules:

- Changes to **filter policies** affecting sensitive domains (e.g., heritage overlays) must be reviewed by:
  - Event Systems Board, and  
  - FAIR+CARE Council (and relevant sovereignty stewards if applicable).  

- Publisher contracts must clearly document any fields that may encode **cultural, heritage, or sensitive spatial** information and specify masking or generalization rules.

---

## 🕰️ Version History

| Version   | Date       | Notes                                                   |
|----------:|------------|---------------------------------------------------------|
| **v11.2.4** | 2025-12-06 | Initial creation aligned with event-systems consolidation and KFM-MDP v11.2.4. |
| v11.2.3  | —          | Precursor design notes (superseded; not published).     |

---

<div align="center">

📡 **KFM v11.2.4 — SNS Message Filtering Architecture**  
Deterministic Event Routing · Low-Noise Pipelines · FAIR+CARE Aligned  

[📘 Pipelines Index](../../README.md) · [🧭 Event Systems Overview](../../architecture/events/README.md) · [⚖ Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
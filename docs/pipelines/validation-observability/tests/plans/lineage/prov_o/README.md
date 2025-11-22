---
title: "🧾 PROV-O Lineage Schema Test Plan — RDF/JSON-LD & Shape-Conformance Compliance (Diamond⁹ Ω / Crown∞ Ω Ultimate Certified)"
path: "docs/pipelines/validation-observability/tests/plans/lineage/prov_o/README.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Quarterly / Provenance Governance Board • FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/lineage-prov_o-testplan-v11.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "V11.0.0"
status: "Active / Enforced"
doc_kind: "Lineage-Test-Plan"
intent: "prov_o-lineage-testplan"
semantic_status: "Authoritative"
---

# 🧾 **PROV-O Lineage Schema Test Plan — RDF/JSON-LD & Shape-Conformance Compliance**

`docs/pipelines/validation- observability/tests/plans/lineage/prov_o/README.md`

**Purpose:**  
Define the official KFM v11 **lineage-schema test plan** for validating that all PROV-O–based lineage representations (RDF, JSON-LD, and associated SHACL/SHEx constraints) are syntactically correct, semantically valid, and fully aligned with:

- W3C PROV-O data model and constraints  
- KFM Lineage & Provenance Standards (PROV-O profile)  
- STAC/DCAT → PROV-O crosswalks (see STAC/DCAT & SHACL indices)  
- FAIR+CARE + CARE-S governance requirements for provenance  
- Model Promotion Gate v11 lineage criteria  

This plan ensures that all lineage graphs in the Kansas Frontier Matrix are **schema-safe, interoperable, and reproducible**.

---

## 📘 Overview

The **PROV-O Lineage Schema Test Plan** focuses on the **structure and semantics** of lineage graphs, independent of specific AI models or datasets.

It validates that:

- All PROV-O entities, activities, and agents are represented, typed, and linked correctly  
- All required properties and relations (e.g., `prov:used`, `prov:wasGeneratedBy`, `prov:wasAssociatedWith`) are present and consistent  
- All PROV-O graphs can be exported/imported as RDF and JSON-LD using KFM’s shared vocabularies and contexts  
- All lineage graphs pass shape validation against KFM’s PROV-O–based SHACL/SHEx constraints  
- Lineage graphs are plumbed into STAC/DCAT and OpenLineage-based pipelines without loss of semantics  

This plan is **foundational** for all lineage test suites (AI lineage, chain-closure, promotion-integrity, etc.).

---

## 🗂 Directory Layout

```text
docs/pipelines/validation-observability/tests/plans/lineage/prov_o/
│
├── README.md                                   # This file — PROV-O lineage schema test plan
│
├ holes/                                        # (Optional) Shared helpers for test cases
│
├── cases/                                      # Individual test-case suites
│   ├── rdf_conformance/                        # RDF syntax & vocabulary conformance
│   ├── jsonld_contexts/                        # JSON-LD @context + term mapping tests
│   ├── prov_core/                              # Entity/Activity/Agent + core relations
│   ├── derivation_chains/                      # prov:used / prov:wasDerivedFrom tests
│   ├── attribution_association/                # prov:wasAttributedTo / prov:wasAssociatedWith
│   ├── bundles/                                # Multi-bundle & named-graph handling
│   ├── stac_dcat_crosswalk/                    # STAC/DCAT → PROV-O alignment tests
│   ├── shacl_shapes/                           # PROV-O SHACL/SHEx constraint conformance
│   ├── sovereignty_lineage/                    # CARE-S lineage & restriction shapes
│   └── promotion_gate/                         # Schema-readiness criteria for Promotion Gate v11
│
├── configs/                                    # Execution configs for schema validation
│   ├── prov_o_schema_testplan_v11.yaml
│   ├── prov_o_shapes_config_v11.yaml
│   └── prov_o_contexts_v11.yaml
│
└── reports/                                    # Auto-generated validation reports
    ├── latest.json
    └── history/
```

---

## 🧩 PROV-O Lineage Schema Domains (Mandatory)

Each domain below represents a **required** compliance area. Any failure is **blocking**.

### 🧬 1. PROV-O Core Vocabulary & Typing

Verifies:

- All entities, activities, and agents are properly typed using PROV classes  
- Only permitted PROV-O properties are used  
- No undeclared or malformed IRIs for PROV terms  
- Domain/range expectations are respected  

**Blocking Conditions:**

- Missing `rdf:type` for key PROV resources  
- Use of non-registered or mis-typed PROV terms  
- Incompatible property usage (e.g., `prov:used` pointing to non-Entity)

---

### 📚 2. RDF Serialization & JSON-LD Conformance

Ensures that:

- RDF graphs serialize and parse without error (Turtle/JSON-LD)  
- JSON-LD uses KFM-approved `@context` definitions  
- Round-tripping (RDF ↔ JSON-LD) preserves identifiers and structure  
- No loss of PROV semantics during transformation  

**Blocking Conditions:**

- Serialization or parsing failures  
- Loss of type or relation information in round-trips  

---

### 🧱 3. Shape Constraints (SHACL/SHEx) Conformance

Validates:

- All PROV-O graphs pass KFM’s PROV-O SHACL/SHEx constraints  
- Required fields (e.g., `prov:wasGeneratedBy`, `prov:used`, `prov:startedAtTime`) are present where mandated  
- Shapes for datasets, models, Story Nodes, and telemetry are satisfied  

**Blocking Conditions:**

- Any shape violations in PROV-O graphs  
- Missing or unbound shape targets for known artifact types  

---

### 🔗 4. Relationship & Chain Semantics

Ensures:

- Correct use of PROV derivation (`prov:wasDerivedFrom`)  
- No cycles where prohibited  
- Temporal order respects `prov:startedAtTime` / `prov:endedAtTime` constraints  
- `prov:wasInformedBy`, `prov:wasInfluencedBy`, and `prov:alternateOf` are consistent  

**Blocking Conditions:**

- Ill-formed or contradictory derivation chains  
- Temporal inconsistencies in PROV relations  

---

### 🌐 5. STAC/DCAT–to–PROV-O Crosswalk

For datasets and resources:

- STAC Items and DCAT Datasets map cleanly to PROV `Entity`/`Activity`/`Agent`  
- `dct:publisher`, `dct:license`, `dct:provenance` are mirrored in PROV attributes  
- PROV graphs reference valid STAC/DCAT identifiers  

**Blocking Conditions:**

- Missing or inconsistent cross-references  
- Mismatched IDs or stale references  

---

### 🛰 6. OpenLineage Alignment

Ensures:

- OpenLineage runs, jobs, datasets map to PROV Activities & Entities  
- Lineage captured via OpenLineage can be fully translated to PROV-O  
- No loss of lineage fidelity in translation  

**Blocking Conditions:**

- Inability to derive PROV-O from OpenLineage events for any critical pipeline  

---

### 🪶 7. CARE-S & Sovereignty-Constrained Lineage

Enforces:

- PROV-O graphs respect sovereignty rules for Indigenous data  
- No PROV traces beyond authorized lineage boundaries  
- No linkages that would expose sensitive or restricted heritage data  

**Blocking Conditions:**

- Any `care_violation: true` in lineage-related PROV resources  

---

### 🚦 8. Promotion-Readiness Schema Criteria

Final schema readiness for Promotion Gate v11:

- All lineage graphs PROV-O compliant  
- All shape constraints satisfied  
- All references resolvable  
- All required governance and legal attributes present  

**Blocking Conditions:**

- Any non-compliance with PROV-O schema or KFM lineage rules  

---

## 🛠 Example PROV-O Schema Test Config

```yaml
prov_o_schema_testplan:
  version: "v11.0.0"
  required_domains:
    - rdf_conformance
    - jsonld_contexts
    - prov_core
    - derivation_chains
    - attribution_association
    - bundles
    - stac_dcat_crosswalk
    - shacl_shapes
    - sovereignty_lineage
    - promotion_gate

rules:
  require_valid_rdf: true
  require_valid_jsonld: true
  require_prov_core_relations: true
  require_shape_conformance: true
  require_resolvable_uris: true
  block_on_care_s_violation: true
  block_on_shape_failure: true
```

---

## 🧪 CI Integration

The PROV-O Lineage Schema Test Plan is executed via:

- `prov-o-schema-testplan.yml`  
- `lineage-integrity-testplan.yml`  
- `openlineage-governance-testplan.yml`  
- `stac-dcat-lineage-validate.yml`  
- `provenance-check.yml`  

Any failure in these tests:

- **Blocks merges** impacting lineage schemas or provenance logic  
- Prevents model/dataset/Story Node promotion via Promotion Gate v11  

---

## 🕰 Version History

| Version | Date       | Author              | Summary                                                  |
|--------:|------------|---------------------|----------------------------------------------------------|
| v11.0.0 | 2025-11-21 | `@kfm-governance`   | Initial creation of PROV-O Lineage Schema Test Plan.     |

---
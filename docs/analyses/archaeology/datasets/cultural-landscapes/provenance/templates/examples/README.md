---
title: "🧬 KFM v11.2.3 — Cultural Landscape Provenance Example Logs (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/provenance/templates/examples/README.md"
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
content_stability: "stable"
backward_compatibility: "Aligned with v11.2.3 provenance-contract (examples level)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/archaeology-cultural-landscapes-provenance-v1.json"

governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

status: "Active / Enforced"
doc_kind: "Provenance Examples Guide"
intent: "cultural-landscape-provenance-examples"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🧬 **Kansas Frontier Matrix — Cultural Landscape Provenance Example Logs**  
`docs/analyses/archaeology/datasets/cultural-landscapes/provenance/templates/examples/README.md`

**Purpose:**  
Define and govern the **example provenance logs** used to demonstrate PROV-O + CARE + KFM patterns for cultural landscape datasets in KFM.  
These examples are:

- **Non-authoritative** and **synthetic/abstracted**  
- Fully **PROV-O / CARE / KFM–valid**  
- Safe for **testing, demos, and tooling development**  
- Aligned with the parent cultural landscape provenance standard and templates

</div>

---

## 📘 Overview

This directory contains **worked example provenance logs** that show:

- How to fill in the **provenance templates** under `../`  
- How cultural landscape datasets should encode:
  - Data origins and transformations  
  - Spatial generalization and sensitivity  
  - FAIR+CARE and sovereignty reviews  
  - Versioning and lineage chains  
- How KFM expects **graph-safe**, **Story Node–ready**, and **Focus Mode–ready** provenance structures.

These files are used by:

- Human authors as concrete reference patterns  
- CI jobs as **smoke-test fixtures**  
- Tooling (scaffolders, linters) to validate round-trip behavior

They must always remain **clearly marked as examples** and must not be confused with authoritative dataset provenance.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/provenance/templates/examples/
├── 📄 README.md                                   # This file (examples guide & constraints)
├── 🧾 protohistoric-wichita-example.v1.json       # Example: Protohistoric Wichita region (generalized)
├── 🧾 great-bend-aspect-example.v2.json           # Example: Great Bend Aspect interaction sphere
└── 🧾 <future-example-*.json>                     # Additional governed example logs (if added)
~~~

**Directory contract:**

- All files here are **examples** and must include `"example"` in the filename.  
- No file in this directory is considered an **authoritative provenance record**.  
- Example names should mirror real dataset slugs where helpful, but the **content must remain synthetic/abstracted**.

Authoritative provenance logs live in:

- `docs/analyses/archaeology/datasets/cultural-landscapes/provenance/`

Templates that examples are based on:

- `docs/analyses/archaeology/datasets/cultural-landscapes/provenance/templates/README.md`

---

## 🧬 Example Types & Conventions

### 1. `protohistoric-wichita-example.v1.json`

Illustrates a **protohistoric cultural landscape region** with:

- Raw entity representing an abstracted ethnohistoric region  
- Generalized entity using **H3 or simplified polygons** only  
- Processed entity aligned with a hypothetical STAC Item  
- CARE fields documenting sensitivity, review, and visibility rules  
- Review activities showing combined FAIR+CARE + tribal review

Used to demonstrate:

- Protohistoric context handling  
- Required tribal review fields  
- Sensitivity generalization for historically grounded landscapes

### 2. `great-bend-aspect-example.v2.json`

Illustrates an **interaction sphere / aspect-scale region** with:

- Explicit multi-step generalization (e.g., different H3 resolutions)  
- Detailed `kfm:steps` arrays in `prov:Activity`  
- Multiple agents (analyst, working group, review body)  
- A `kfm:provenance_version` > v1 to show versioned updates

Used to demonstrate:

- Version upgrades in provenance (`v1` → `v2`)  
- Richer activity and agent modeling  
- Multi-stage boundary estimation and review

### 3. Future Examples

Future examples may cover:

- **Mobility corridors** (e.g., travel pathways or interaction routes)  
- **Resource procurement areas** (e.g., generalized quarry or hunting landscapes)  
- **Composite landscapes** that aggregate multiple sources or periods  

Any new example must:

- Follow the **file naming** and **schema** rules in this README and the parent templates README.  
- Be explicitly described in this README under a dedicated subsection.

---

## 🧪 Example Structure (Illustrative Pattern)

All examples must conform to the **same PROV-O + CARE + KFM profile** used for real provenance logs.

A minimal, illustrative pattern:

~~~json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "care": "https://schema.kfm.dev/care#",
    "kfm": "https://schema.kfm.dev/core#"
  },
  "prov:Entity": {
    "raw": {
      "prov:label": "Abstracted protohistoric region (example)",
      "prov:type": "Dataset",
      "kfm:source": "Synthetic example for KFM documentation",
      "kfm:stac_item": "example-protohistoric-region-v1"
    },
    "generalized": {
      "prov:label": "Generalized example region (H3 level 6)",
      "prov:type": "Dataset",
      "kfm:h3_resolution": 6,
      "care:notes": "Example-only; no real-world coordinates represented."
    },
    "processed": {
      "prov:label": "Processed cultural landscape example v1",
      "prov:type": "Dataset",
      "kfm:provenance_version": "v1"
    }
  },
  "care:sensitivity": "generalized",
  "care:review": "faircare",
  "care:notes": "Example log illustrating PROV-O + CARE shape.",
  "care:visibility_rules": "polygon-generalized"
}
~~~

**Key requirements:**

- The word `"example"` must be present in `prov:label` or `kfm:source` for all core entities.  
- No coordinates, geometries, or descriptions may be specific enough to represent real sensitive locations.  
- The example must still be **valid, ingestible JSON-LD**.

---

## ⚖ FAIR+CARE & Sovereignty Safeguards in Examples

Even though these logs are synthetic, they **must obey the same safeguards** as real data:

- **No restricted content**:
  - No exact ceremonial locations  
  - No burial ground outlines  
  - No sensitive ethnographic narratives  

- **Explicit CARE fields**:
  - `care:sensitivity` must never be `"restricted"` in examples.  
  - `care:review` should describe the **intended review path**, not real institutions.  
  - `care:notes` must clearly signal the synthetic/example nature.

- **Clear abstraction**:
  - If an example is loosely inspired by a real-world context (e.g., “Protohistoric Wichita”), it must be:
    - Generalized beyond any real confidential boundaries  
    - Free of any non-public knowledge or coordinates

If there is doubt about whether an example is sufficiently abstracted, it must be reviewed under the same governance channels as real data.

---

## 🧠 Relationship to Templates & Provenance Standard

This directory is tightly coupled to:

1. **Provenance Standard**  
   - `docs/analyses/archaeology/datasets/cultural-landscapes/provenance/README.md`  
   - Defines the **normative rules** for provenance structure, PROV-O usage, CARE fields, and CI gates.

2. **Provenance Templates**  
   - `docs/analyses/archaeology/datasets/cultural-landscapes/provenance/templates/README.md`  
   - Defines the **JSON-LD skeletons** that real provenance logs must conform to.

**Contract:**

- Every example JSON-LD file must be:
  - Expressible as a valid filling of one or more templates under `../`.  
  - Valid under the same PROV-O + CARE + KFM profile used in production.  
- If templates or the standard change, examples must be updated to remain:
  - **Schema-valid**  
  - **Illustrative** for the latest contract  
  - Useful for CI and developer tests

---

## 🧪 CI/CD & Usage in Testing

Examples in this directory are used by CI for:

- **Smoke tests** of:
  - Provenance parsers and validators  
  - Graph loaders (Neo4j ingestion)  
  - Story Node & Focus Mode explainability components  

- **Regression tests** to ensure:
  - No breaking changes to the provenance schema without explicit migration  
  - CARE and sovereignty constraints remain enforced  
  - KFM-MDP v11.2.2 machine-readability is preserved

Typical CI checks:

- `archaeology-provenance-validate.yml` (or equivalent)  
- `faircare-audit.yml`  
- `metadata-validate.yml`  

When provenance templates or core schemas change, these examples are the **first line of defense** against regressions.

---

## 🕰️ Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council   | Created governed examples directory; defined contracts for synthetic PROV-O + CARE example logs aligned with v11.2.3 provenance standard and templates. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.2 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Provenance Templates](../README.md) · [⬅ Back to Cultural Landscape Provenance Standard](../../README.md) · [⬅ Back to Cultural Landscape Datasets](../../../README.md)

</div>


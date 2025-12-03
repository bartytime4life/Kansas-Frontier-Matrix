---
title: "🧩 KFM v11.2.3 — Cultural Landscape Provenance Templates (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/provenance/templates/README.md"
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
content_stability: "stable"
backward_compatibility: "Aligned with v11.2.3 provenance-contract (template level)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/archaeology-cultural-landscapes-provenance-v1.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

status: "Active / Enforced"
doc_kind: "Provenance Template Guide"
intent: "cultural-landscape-provenance-templates"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🧩 **Kansas Frontier Matrix — Cultural Landscape Provenance Templates**  
`docs/analyses/archaeology/datasets/cultural-landscapes/provenance/templates/README.md`

**Purpose:**  
Define the **JSON-LD template library** for cultural landscape provenance logs in KFM.  
These templates standardize **PROV-O + CARE + KFM** fields so every cultural landscape dataset can generate:

- Machine-validated provenance logs  
- FAIR+CARE-audited records  
- Graph-safe entities and relations  
- Story Node / Focus Mode–ready explainability artifacts  

Templates here are **authoring contracts** used by humans, CI jobs, and scaffolding tools.

</div>

---

## 📘 Overview

This directory holds the **canonical provenance templates** for:

- Cultural landscape regions (interaction spheres, settlement areas, mobility corridors)  
- Derived generalized layers (H3/polygon generalized)  
- Review dossiers and ethical/sovereignty notes  
- Migration/upgrade templates between provenance schema versions  

Key properties:

- All templates are **JSON-LD** and **PROV-O–shaped**.  
- Each template is **KFM-MDP v11.2.2–compatible** and designed for machine-filling by ETL/AI tools.  
- CI uses these templates for:
  - Scaffolding new provenance logs  
  - Validating required fields and shapes  
  - Enforcing CARE and sovereignty safeguards  

For the governing provenance standard, see the parent document:

- `docs/analyses/archaeology/datasets/cultural-landscapes/provenance/README.md`

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/provenance/templates/
├── 📄 README.md                                  # This file (template contracts & usage rules)
│
├── 🧾 base-provenance-template.v1.json           # Minimal PROV-O + CARE + KFM skeleton
├── 🧾 landscape-region-template.v1.json          # For cultural landscape / interaction spheres
├── 🧾 review-dossier-template.v1.json            # For FAIR+CARE + tribal review bundles
├── 🧾 migration-template-v1-to-v2.json           # Example pattern for provenance version upgrades
│
└── 🧬 examples/                                  # Optional fully-populated example logs
    ├── 🧾 protohistoric-wichita-example.v1.json  # Example: Protohistoric Wichita region (generalized)
    └── 🧾 great-bend-aspect-example.v2.json      # Example: Great Bend Aspect interaction sphere
~~~

**Directory contract:**

- Files ending in `.template.json` or `.vX.json` under this directory are treated as **governed templates**.  
- Files under `examples/` are **non-authoritative** but must remain:
  - PROV-O valid  
  - CARE-compliant  
  - Consistent with the parent provenance README  

---

## 🧩 Template Types & Naming

All templates in this directory follow **semantic naming**:

- `base-provenance-template.v1.json`  
  - Lowest-common-denominator PROV-O + CARE + KFM structure  
  - Used when scaffolding any new provenance log  

- `landscape-region-template.v1.json`  
  - For cultural landscape datasets representing:
    - Interaction spheres  
    - Settlement regions  
    - Resource procurement areas  
    - Mobility corridors  
  - Includes landscape-specific fields (periodization, method, confidence, etc.)

- `review-dossier-template.v1.json`  
  - For documenting FAIR+CARE and tribal review processes  
  - Centralizes:
    - Review agents  
    - Governance references  
    - Sovereignty flags  
    - Visibility rules  

- `migration-template-v1-to-v2.json`  
  - Illustrates how to upgrade provenance logs between schema versions  
  - Used as a pattern for future automated migration tools  

**Naming rules:**

- Templates: `*-template.v<major>.json`  
- Examples: `<dataset-slug>-example.v<semver>.json`  
- All names must be **lowercase**, **dash-separated**, and **ASCII-only**.

---

## 🧬 Required Fields & Shapes (Across Templates)

All provenance templates in this directory must include, at minimum:

### 1. `@context`

- `prov` – PROV-O namespace  
- `care` – KFM CARE vocabulary  
- `kfm` – KFM core vocabulary  
- Optional: CIDOC-CRM, GeoSPARQL, OWL-Time prefixes for advanced use cases.

### 2. `prov:Entity` (Core Entities)

Templates must provide slots for:

- `raw`  
  - Original dataset / interpretation  
  - Required fields:
    - `prov:label`  
    - `prov:type`  
    - `kfm:source`  
    - `kfm:stac_item` (or equivalent dataset identifier)

- `generalized`  
  - Generalized/obfuscated representation used for public display  
  - Required fields:
    - `prov:label`  
    - `prov:type`  
    - `kfm:h3_resolution` and/or simplification parameters  
    - `care:notes`

- `processed`  
  - Cleaned and validated dataset used directly in KFM  
  - Required fields:
    - `prov:label`  
    - `prov:type`  
    - `kfm:provenance_version`  
    - `kfm:stac_item`

Templates may also expose optional entities such as `validation`, `review-dossier`, `supporting-evidence`.

### 3. `prov:Activity` (Core Activities)

Templates must include:

- `generalization`  
  - Slots for:
    - `prov:type`  
    - `prov:startTime` / `prov:endTime`  
    - `kfm:steps` (array of human-readable step descriptions)

- `review`  
  - Slots for:
    - `prov:type`  
    - `prov:label`  
    - `prov:endTime`  
    - `kfm:review_scope` (e.g., “ethics”, “tribal”, “technical”)

Templates may define extra activities such as `digitization`, `boundary_estimation`, `time_model_alignment`.

### 4. `prov:Agent` (Core Agents)

Required agent slots:

- `analyst`  
- `faircare`  
- `tribal`  
- `source_institution`

Each must have:

- `prov:label`  
- `prov:type`  
- Optional:
  - `kfm:identifier` (e.g., ORCID, ROR, internal ID)

### 5. Relations & CARE Fields

Templates must define array slots for:

- `prov:wasDerivedFrom`  
- `prov:wasGeneratedBy`  
- `prov:used`  
- `prov:wasAttributedTo`

And CARE fields:

- `care:sensitivity`  
- `care:review`  
- `care:notes`  
- `care:visibility_rules`

Default template values should be **safe placeholders**, never hard-coded to restricted values.

---

## 🧪 CI/CD & Validation

Templates in this directory are **first-class governed artifacts** and must:

- Pass JSON schema validation for:
  - PROV-O shape  
  - CARE extensions  
  - KFM archaeology provenance profile  

- Be referenced by:
  - `archaeology-provenance-validate` CI jobs  
  - Any scaffolding tools that generate provenance logs for:
    - New cultural landscapes  
    - Revised/updated landscape datasets  

**CI expectations:**

- Changes to `templates/*.json` trigger:
  - Template schema validation  
  - Backward-compatibility checks (where declared)  
  - A diff review by:
    - Cultural Landscape Working Group  
    - FAIR+CARE Council representatives  

- Provenance logs under `../` must always be derivable from:
  - `base-provenance-template.vX.json` **plus**  
  - Zero or more specialized templates (e.g., `landscape-region-template.vX.json`).

If a provenance log **cannot** be expressed as a valid filling of these templates, it is considered **schema-invalid** and must be revised.

---

## 🧭 Authoring Workflow (Human + Tooling)

Recommended workflow for contributors:

1. **Select template(s)**  
   - Start from `base-provenance-template.v1.json`.  
   - Layer on `landscape-region-template.v1.json` for landscape datasets.  
   - Add `review-dossier-template.v1.json` where governance is complex.

2. **Fill placeholders**  
   - Replace all placeholder tokens (e.g., `{{REQUIRED_VALUE}}`) with real values.  
   - Keep comments or `kfm:notes` fields only if useful for clarity (no schema-breaking comments in JSON).

3. **Run local validation**  
   - Use repo-provided tooling (e.g., `make validate-provenance`) to:
     - Validate JSON-LD structure  
     - Check PROV-O / CARE compliance  
     - Ensure alignment with STAC metadata

4. **Submit via PR**  
   - Include both:
     - The dataset provenance log (under `../`)  
     - The template(s) used, if they were extended or version-bumped

5. **Respond to CI/Governance feedback**  
   - Address any failures in:
     - `faircare-audit`  
     - `archaeology-provenance-validate`  
     - `metadata-validate` / `artifact-stac-validate`

---

## 🕰️ Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council   | Introduced governed provenance template library; aligned with v11.2.3 provenance standard and KFM-MDP v11.2.2. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.2 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Cultural Landscape Provenance Standard](../README.md) · [⬅ Back to Cultural Landscape Datasets](../../README.md)

</div>


---
title: "🧩 Kansas Frontier Matrix — OpenLineage CI Integration Standard (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/lineage/openlineage-ci-integration.md"
version: "v11.2.4"
last_updated: "2025-12-07"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability Engineering · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x compliant"

status: "Active / Enforced"
doc_kind: "Standard"
header_profile: "standard"
footer_profile: "standard"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.5"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"
openlineage_profile: "OpenLineage v2.5 · CI-integrated pipeline runs"

scope:
  domain: "lineage"
  applies_to:
    - "ci-workflows"
    - "pipelines"
    - "telemetry"
    - "provenance"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-commit-hash>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../releases/v11.2.4/signature.sig"
attestation_ref: "../../../releases/v11.2.4/slsa-attestation.json"
sbom_ref: "../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../releases/v11.2.4/lineage-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/openlineage-ci-v3.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../governance/ROOT-GOVERNANCE.md"
ethics_ref: "../faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I1-R1"
care_label: "Collective Benefit · Authority to Control · Responsibility · Ethics"
sensitivity: "General (non-sensitive)"
sensitivity_level: "None"
public_exposure_risk: "Low"
risk_category: "Low"
classification: "Public Document"
indigenous_rights_flag: false
redaction_required: false
data_steward: "KFM FAIR+CARE Council"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "TechArticle"
  prov_o: "prov:Activity"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

provenance_chain:
  - "docs/standards/lineage/openlineage-ci-integration.md@v11.2.3"
  - "docs/standards/lineage/openlineage-ci-integration.md@v11.2.0"

json_schema_ref: "../../../schemas/json/openlineage-ci-integration-v11.2.4.schema.json"
shape_schema_ref: "../../../schemas/shacl/openlineage-ci-integration-v11.2.4-shape.ttl"

doc_uuid: "urn:kfm:doc:standards:lineage:openlineage-ci-integration:v11.2.4"
semantic_document_id: "kfm-standard-openlineage-ci-integration-v11.2.4"
event_source_id: "ledger:docs/standards/lineage/openlineage-ci-integration.md@v11.2.4"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
ttl_policy: "24 months"
sunset_policy: "Superseded by next OpenLineage CI integration standard"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"

ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

transform_registry:
  allowed:
    - summary
    - timeline-generation
    - semantic-highlighting
    - a11y-adaptations
    - diagram-extraction
    - metadata-extraction
  prohibited:
    - content-alteration
    - speculative-additions
    - unverified-architectural-claims
    - narrative-fabrication
    - governance-override

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 Context"
    - "🗺️ Diagrams"
    - "🧠 Story Node & Focus Mode Integration"
    - "🧪 Validation & CI/CD"
    - "📦 Data & Metadata"
    - "🌐 STAC, DCAT & PROV Alignment"
    - "🧱 Architecture"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "diagram-check"
  - "accessibility-check"
  - "provenance-check"
  - "footer-check"

ci_integration:
  workflow: ".github/workflows/lineage.yml"
  environment: "dev → staging → production"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_version_history: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true

deprecated_fields:
  - "old_markdown_standard_v10.4"
---

<div align="center">

# 🧩 **Kansas Frontier Matrix — OpenLineage CI Integration Standard**  
`docs/standards/lineage/openlineage-ci-integration.md`

### *Deterministic provenance for every dataset, artifact, and pipeline run*

**Purpose**  
Define how the Kansas Frontier Matrix (KFM) integrates **OpenLineage** into CI/CD so that every ETL, AI inference, geospatial transformation, and Story Node generation produces **verifiable, machine-readable provenance**.

This standard is **mandatory** for all governed pipelines under `src/pipelines/` and for any CI workflow that produces data or model artefacts relied on by KFM.

</div>

---

## 📘 Overview

This standard specifies:

- How CI environments (GitHub Actions and equivalents) must expose **OpenLineage configuration** (`OPENLINEAGE_URL`, namespaces, run IDs).  
- How pipelines must **emit OpenLineage RunEvents** (START / COMPLETE / FAIL) for every governed run.  
- How OpenLineage runs are **linked into STAC Items, DCAT Datasets, PROV-O bundles, and SLSA attestations**.  
- How **FAIR+CARE and sovereignty rules** apply to lineage (including when and how to mask or generalize sensitive inputs).  
- How lineage artefacts are **organized on disk** and wired into `.github/workflows/lineage.yml`.

In-scope:

- Batch and streaming pipelines instrumented via OpenLineage-compatible clients.  
- Lineage for ETL, AI/ML workflows, geospatial transforms, and Story Node materialization.  
- CI/CD-managed runs initiated via `.github/workflows/` or equivalent orchestrators (e.g., Airflow, dbt, Spark jobs using CI runners or deployment hooks).

Out-of-scope (for this document):

- Detailed OpenLineage client configuration per engine (Airflow/Spark/dbt/GE).  
- Backend deployment details for Marquez or other lineage backends.  
- UI visualization specifics (addressed in separate architecture and web standards).

---

## 🗂️ Directory Layout

This standard assumes and enforces the following layout for lineage-related assets, following the `immediate-one-branch-with-descriptions-and-emojis` profile:

```text
📁 Kansas-Frontier-Matrix/
├── 📁 docs/
│   └── 📁 standards/
│       └── 📁 lineage/
│           └── 📄 openlineage-ci-integration.md     # This standard
├── 📁 schemas/
│   └── 📁 telemetry/
│       └── 🧾 openlineage-ci-v3.json                # Telemetry schema for lineage runs
├── 📁 dist/
│   ├── 📁 provenance/
│   │   └── 🧾 prov-<sha>.jsonld                     # PROV-O / OpenLineage-exported provenance bundles
│   └── 📁 attest/
│       └── 🧾 slsa-<sha>.json                       # SLSA attestations referencing lineage runs
└── 📁 .github/
    └── 📁 workflows/
        └── 📄 lineage.yml                           # Canonical OpenLineage CI workflow
```

**Directory layout rules (normative):**

- `openlineage-ci-integration.md` is the **source of truth** for lineage-in-CI behavior.  
- Telemetry schemas **MUST** be located under `schemas/telemetry/` and referenced via `telemetry_schema`.  
- PROV-O / JSON-LD bundles and SLSA attestations **MUST** be written under `dist/provenance/` and `dist/attest/` with filenames keyed by the **commit SHA** (e.g., `prov-<sha>.jsonld`, `slsa-<sha>.json`).  
- `.github/workflows/lineage.yml` **MUST** implement the CI pattern defined in this document and honor MDP v11.2.5 rules (including markdown + metadata validation for this standard).

Any structural changes to these directories require:

1. Updating this section.  
2. Updating relevant CI workflows (`lineage.yml`, `sbom_verify.yml`, etc.).  
3. Updating any dependent schemas and documentation.

---

## 🧭 Context

This standard sits at the intersection of:

- **.github/ Infrastructure Standard** (`.github/README.md`)  
  - Governs CI/CD, security, FAIR+CARE, and AI safety.  
  - Delegates **lineage-specific behavior** to this OpenLineage CI Integration standard.

- **KFM-MDP v11.2.5 (Markdown Protocol)**  
  - Requires this document to define a predictable structure (Overview → Directory Layout → … → Version History).  
  - Ensures this standard is machine-extractable into catalogs and the KFM knowledge graph.

- **STAC / DCAT / PROV**  
  - OpenLineage runs are treated as **prov:Activity** instances.  
  - Downstream artefacts (rasters, GeoJSON, tables, Story Node outputs) reference run IDs for provenance.

- **FAIR+CARE & Sovereignty Standards**  
  - Define when lineage must be masked or generalized (e.g., for protected archaeological or tribal datasets).  
  - Require this standard to define **masking and redaction rules** for lineage inputs.

The result: every governed pipeline run is **traceable**, **reproducible**, and **ethically constrained**, with lineage anchored in OpenLineage and propagated through catalog and provenance layers.

---

## 🗺️ Diagrams

A high-level view of OpenLineage in CI:

```mermaid
flowchart LR
    A[CI Trigger<br/>GitHub Actions / Scheduler] --> B[Pipeline Run<br/>src/pipelines/*]
    B --> C[OpenLineage Client<br/>RunEvent START/COMPLETE/FAIL]
    C --> D[OpenLineage Backend<br/>(e.g., Marquez)]
    D --> E[PROV-O Bundle<br/>dist/provenance/prov-&lt;sha&gt;.jsonld]
    E --> F[STAC/DCAT Updates<br/>data/stac/* · docs/data/*]
    F --> G[Releases & SLSA Attestations<br/>releases/v*/]
    G --> H[Story Nodes & Focus Mode<br/>UI / Neo4j Graph]
```

This standard formalizes each arrow in that diagram: which environment variables are required, which events must be emitted, what file paths must be written, and how catalog/provenance layers are patched.

---

## 🧠 Story Node & Focus Mode Integration

While this document primarily targets CI and pipeline engineers, its lineage rules directly support **Story Node** and **Focus Mode** features:

- Story Nodes that summarize an analysis or ETL output **MUST** be able to trace back to:
  - The OpenLineage `runId` that produced the underlying dataset.  
  - The corresponding PROV-O bundle in `dist/provenance/`.  
  - Any SLSA attestations and telemetry records.

- Focus Mode overlays **MAY**:
  - Surface OpenLineage metadata (inputs, outputs, job name) when a user inspects a dataset or Story Node.  
  - Show the CI workflow (`lineage.yml`) and commit SHA that ran the job.

- Focus Mode **MUST NOT**:
  - Fabricate lineage events that do not exist in OpenLineage.  
  - Remove or hide CARE-related masking flags (e.g., `care:maskingApplied`).

Implementations that feed lineage into Story Nodes must:

- Treat this standard as **normative** for what constitutes a “governed run”.  
- Use `semantic_document_id` and `event_source_id` fields when linking back to this spec.

---

## 🧪 Validation & CI/CD

This section defines how CI workflows (notably `.github/workflows/lineage.yml`) must behave.

### Required CI Workflow Pattern

A canonical lineage-enabled CI workflow **MUST**:

1. **Set CI + OpenLineage context**

   - Export environment variables (see Architecture section) including:
     - `OPENLINEAGE_URL`
     - `OPENLINEAGE_NAMESPACE="kfm"`
     - `OPENLINEAGE_PARENT_RUN_ID`
     - `KFM_RUN_SHA` (the commit being tested)

2. **Install dependencies**

   - Pipeline code under `src/pipelines/`.  
   - OpenLineage client libraries (Python/Java/other) and any wrappers.

3. **Execute the pipeline with a deterministic run ID**

   - A single **OpenLineage `runId`** must be deterministically derived from:
     - `KFM_RUN_SHA`  
     - CI job identifier (e.g., GitHub `run_id`)  
   - The same `runId` is reused across START / COMPLETE / FAIL events.

4. **Export PROV-O + OpenLineage bundle**

   - Generate `dist/provenance/prov-<sha>.jsonld` that:
     - References the OpenLineage `runId`.  
     - Is compatible with PROV-O (entities, activities, agents).  
     - Includes any CARE masking annotations.

5. **Patch STAC/DCAT records**

   - Update relevant STAC Items & DCAT Datasets with:
     - `prov:wasGeneratedBy`  
     - `openlineage:runId` and `openlineage:namespace`  
     - SLSA / telemetry references (see STAC/DCAT section).

6. **Generate SLSA attestation**

   - Create `dist/attest/slsa-<sha>.json` that references:
     - `KFM_RUN_SHA`  
     - OpenLineage `runId`  
     - PROV/telemetry artefacts for the run.

7. **Upload artefacts**

   - Publish:
     - Lineage telemetry (as per `telemetry_schema`)  
     - PROV-O bundle (`dist/provenance/prov-<sha>.jsonld`)  
     - SLSA attestation (`dist/attest/slsa-<sha>.json`)  
   - Ensure they are included in the release manifest (`manifest_ref`).

### CI Pattern Template (Canonical)

Conceptual structure of `.github/workflows/lineage.yml`:

```text
.github/workflows/lineage.yml
├── Set up Python / runtime
├── Install pipeline + OpenLineage deps
├── Export OPENLINEAGE_* and KFM_RUN_SHA
├── Execute pipeline with OL wrapper
├── Export PROV-O JSON-LD (prov-<sha>.jsonld)
├── Patch STAC/DCAT (add runId + prov links)
├── Generate SLSA attestation (slsa-<sha>.json)
└── Upload artefacts + telemetry
```

Protected branches and release workflows **MUST** require `lineage.yml` to pass for any PRs that:

- Modify `src/pipelines/`, `data/processed/`, `data/stac/`, or Story Node artefacts.  
- Affect CI behavior related to provenance or telemetry.

---

## 📦 Data & Metadata

This standard defines a minimal set of lineage-related artefacts for each governed run:

- **OpenLineage events**  
  - Sent to the configured backend via HTTP or other supported transports.  
  - Represented as `RunEvent` objects keyed by `runId`.

- **PROV-O JSON-LD bundle**

  - `dist/provenance/prov-<sha>.jsonld`  
  - Contains:
    - `prov:Activity` corresponding to the OpenLineage `runId`.  
    - `prov:Entity` objects for inputs and outputs.  
    - `prov:Agent` entries for CI worker, pipeline, and project.  
    - Optional CARE masking flags and roles.

- **SLSA attestation**

  - `dist/attest/slsa-<sha>.json`  
  - Binds:
    - Source repo and commit (`KFM_RUN_SHA`).  
    - CI workflow (`.github/workflows/lineage.yml`).  
    - OpenLineage `runId`.  
    - PROV/telemetry artefacts.

- **Telemetry**

  - As defined by `openlineage-ci-v3.json`, e.g.:
    - Run durations, dataset counts, masking statistics.  
    - Energy and carbon metrics in line with `energy_schema` and `carbon_schema`.

All of these artefacts are referenced from:

- Release bundles under `releases/v11.2.4/` (per `sbom_ref`, `manifest_ref`, `telemetry_ref`, `signature_ref`, `attestation_ref`).  
- STAC/DCAT records via properties shown in the next section.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC Properties (Mandatory)

Each STAC Item produced or updated by a governed pipeline **MUST** contain at least:

```json
{
  "prov:wasGeneratedBy": "<run-id>",
  "openlineage:runId": "<run-id>",
  "openlineage:namespace": "kfm",
  "slsa:attestation_ref": "dist/attest/slsa-<sha>.json",
  "kfm:telemetry_ref": "releases/v11.2.4/lineage-telemetry.json"
}
```

Additional properties **MAY** include:

- `kfm:prov_bundle_ref`: `"dist/provenance/prov-<sha>.jsonld"`  
- `kfm:ci_workflow`: `".github/workflows/lineage.yml"`

These properties must be:

- Schema-validated (STAC + custom KFM extensions).  
- Consistent with values present in release manifest and PROV-O bundle.

### DCAT / PROV-O Requirements

Each dataset registered in the DCAT catalog **MUST**:

- Include a `prov:Activity` describing the OpenLineage run that produced or updated it.  
- Use:
  - `prov:used` for each input dataset.  
  - `prov:generated` for each output dataset.  
  - `prov:wasAssociatedWith` for the pipeline worker / CI agent.  
  - `prov:startedAtTime` and `prov:endedAtTime`.  
- Include `prov:role` or equivalent qualifiers when:
  - CARE masking was applied to specific inputs or outputs.  
  - Additional roles (e.g., `care:SensitiveInputAggregator`) are involved.

The PROV-O bundle in `dist/provenance/prov-<sha>.jsonld` is the **canonical machine-readable form** of this information; STAC/DCAT records are views onto it.

---

## 🧱 Architecture

This section re-expresses the original “Core Requirements” in MDP-compliant structure.

### Core Runtime Requirements

Pipelines and CI environments **MUST** satisfy the following:

#### CI Environment Variables

All CI systems and orchestrators **MUST** expose at least:

| Variable                    | Meaning                                                     |
|----------------------------|-------------------------------------------------------------|
| `OPENLINEAGE_URL`          | Lineage endpoint (Marquez or equivalent)                    |
| `OPENLINEAGE_API_KEY`      | Optional secured token (if backend is authenticated)        |
| `OPENLINEAGE_NAMESPACE`    | Namespace; **MUST** equal `"kfm"` for governed runs        |
| `OPENLINEAGE_PARENT_RUN_ID`| Parent run ID (CI run, DAG run, or replay identifier)      |
| `KFM_RUN_SHA`              | Exact commit SHA for reproducibility                        |

Additional engine-specific variables (e.g., `OPENLINEAGE_TRANSPORT`, `OPENLINEAGE_ENV`) may be used but do not replace the above.

#### Event Emission

For each governed pipeline run, the OpenLineage client **MUST** emit:

- A **START** `RunEvent` when the run begins.  
- A **COMPLETE** `RunEvent` on success.  
- A **FAIL** `RunEvent` on error.  
- Input and output dataset descriptors for all governed IO:
  - Paths, URIs (S3, lakeFS, local FS, DB tables, etc.).  
  - Optional facets (schema, row counts, sizes) per OpenLineage spec.

Run IDs **MUST** be deterministic (derivable from `KFM_RUN_SHA` + CI job ID) to allow replays and correlation with other systems.

### Linking to Artifacts

Every processing step that produces a user-visible or cataloged artefact **MUST** embed lineage references into:

- **STAC Items**  
  - Via `prov:wasGeneratedBy`, `openlineage:runId`, `openlineage:namespace`, and attestation/telemetry refs.

- **DCAT Datasets**  
  - Via PROV-O relations (`prov:wasGeneratedBy`, `prov:used`, `prov:generated`).

- **KFM Provenance Bundle**  
  - JSON-LD in `dist/provenance/prov-<sha>.jsonld`.

- **SLSA Attestations**  
  - `dist/attest/slsa-<sha>.json` referencing the OpenLineage `runId` and CI workflow.

These links make OpenLineage the **runtime backbone** for provenance, with STAC/DCAT/PROV and SLSA forming the catalog and supply-chain layers.

---

## ⚖ FAIR+CARE & Governance

### CARE-Aligned Lineage Masking Rules

For sensitive archaeological, heritage, ecological, or sovereign datasets, lineage must **not** reveal:

- Exact locations of protected sites.  
- Internally sensitive dataset identifiers or raw paths.  
- Disallowed cross-joins or combinations of sensitive datasets.

Instead, pipelines **MUST** apply one or more of:

- **H3 resolution generalization** of spatial coordinates.  
- **Site obfuscation** (distance fuzzing / donut masking).  
- **Aggregation** of sensitive inputs into coarse, categorized groups.  
- **Redaction** of raw paths, replaced with symbolic URIs such as `"masked://sensitive"`.

Serialized provenance **MUST** indicate masking:

```json
{
  "care:maskingApplied": true,
  "care:maskingStrategies": [
    "h3-generalization",
    "donut-masking",
    "path-redaction"
  ]
}
```

Governance implications:

- Runs that **should** be masked but are not will fail FAIR+CARE checks and must be remedied before release.  
- Masking rules are **additive** to security controls: even if access is restricted, masked lineage improves safety for derived views and telemetry exports.

---

## 🕰️ Version History

| Version   | Date       | Summary                                                                                   |
|----------:|-----------:|-------------------------------------------------------------------------------------------|
| **v11.2.4** | 2025-12-07 | Aligned with KFM-MDP v11.2.5; elevated emoji `🗂️ Directory Layout` section; added full metadata front-matter; clarified CI workflow + artefact layout; tightened STAC/DCAT/PROV requirements and CARE masking rules. |
| v11.2.3  | 2025-12-02 | Updated STAC/DCAT crosswalk and OpenLineage-run embedding guidance; internal CI refinements. |
| v11.2.0  | 2025-11-20 | Initial lineage governance spec defining OpenLineage integration into CI/CD for KFM pipelines. |

---

<div align="center">

🧩 **Kansas Frontier Matrix — OpenLineage CI Integration Standard**  
Deterministic · Reproducible · FAIR+CARE · Governance-First  

[📘 Docs Root](../../..) · [📂 Standards Index](../README.md) · [⚖ Governance](../governance/ROOT-GOVERNANCE.md) · [🔧 GitHub Infra](../../../.github/README.md)

</div>

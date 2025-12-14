---
title: "🧾 KFM — Remote Sensing Validation Provenance (PROV-O · OpenLineage · STAC Linkage)"
path: "docs/analyses/remote-sensing/validation/methods/provenance/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing Board · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Index + Reference"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

intent: "remote-sensing-validation-provenance"
audience:
  - "Remote Sensing Engineering"
  - "Science QA Reviewers"
  - "Data Engineering"
  - "Reliability Engineering"
  - "Governance Reviewers"

classification: "Public"
sensitivity: "General (non-sensitive) unless overridden by dataset labels"
sensitivity_level: "Low"
public_exposure_risk: "Low"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "Remote Sensing Board · FAIR+CARE Council"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:methods:provenance:index:v11.2.6"
semantic_document_id: "kfm-remote-sensing-validation-provenance"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/methods/provenance/README.md"
immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "metadata-extraction"
  - "diagram-extraction"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"
---

<div align="center">

# 🧾 **KFM — Remote Sensing Validation Provenance**
`docs/analyses/remote-sensing/validation/methods/provenance/README.md`

**Purpose**  
Define the governed provenance posture for **remote-sensing validation** in KFM:
how validation runs emit **PROV-O** and/or **OpenLineage**, how those bundles link to **STAC/DCAT** artifacts,
and which minimum fields are required for deterministic audit and governance.

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="KFM-PROV v11" src="https://img.shields.io/badge/KFM--PROV-v11-blue" />
<img alt="Status Active Enforced" src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

Remote-sensing validation in KFM is **evidence-led** and **audit-first**:

- every validation output is traceable to:
  - the specific input artifacts evaluated (STAC assets / dataset versions),
  - the exact algorithm version and configuration,
  - the run context (runner version, timestamps, environment),
  - the governance posture (CARE and sovereignty gates),
- provenance must support:
  - deterministic reruns and rollbacks,
  - release promotion gates (pass/warn/fail),
  - “why did this metric change?” investigations without guessing.

This directory defines the provenance conventions used by:

- validation algorithms (`../algorithms/README.md`)
- metric definitions (`../metrics/README.md`)
- report rollups (`../../reports/README.md`)

---

## 🗂️ Directory Layout

~~~text
📁 docs/analyses/remote-sensing/validation/methods/
└── 📁 provenance/                                            — Provenance conventions (this directory)
    ├── 📄 README.md                                          — This reference (you are here)
    └── 📁 templates/                                         — Optional: PROV/OpenLineage template payloads
~~~

> Keep templates small. Store large run bundles (full traces) as governed artifacts and reference them from STAC/PROV.

---

## 🧾 Provenance outputs (what must exist)

Validation runs SHOULD emit (at minimum) one of:

- **PROV-O JSON-LD bundle** (preferred for KFM provenance graph alignment), and/or
- **OpenLineage event set** (preferred for operational job tracking)

Where both exist:

- OpenLineage may be treated as the “ops-friendly” event stream,
- PROV-O is the “governance-friendly” lineage bundle,
- cross-link using stable run identifiers.

### Minimum provenance artifacts (recommended)

- `prov_bundle.jsonld` (per run or per evaluation scope)
- `openlineage_events.json` (per run; may contain start/complete/fail events)
- `config_snapshot.json` (pinned parameters + thresholds + mask policy refs)
- `input_pack_manifest.json` (immutable input URIs + checksums)
- `output_manifest.json` (output URIs + checksums)

> Provenance is not optional for governed validation. Missing provenance is a gate failure under fail-closed policy.

---

## 🧬 PROV-O mapping (KFM-PROV v11 posture)

### Entities (prov:Entity)

Typical entities include:

- **Inputs evaluated**
  - STAC Item(s) and their asset hrefs (or immutable URIs)
  - dataset version identifiers
  - baseline/reference artifacts (previous release metrics, trusted reference grids)
- **Validation configuration**
  - algorithm config snapshot (including thresholds)
  - mask policy snapshot / hash
- **Outputs produced**
  - metrics summary JSON (small)
  - detailed report artifact (optional; referenced)
  - rollup contribution record (optional; referenced)

### Activities (prov:Activity)

At minimum:

- `validate_<family>_<algorithm>` (one activity per algorithm family run)
- optional sub-activities:
  - `enumerate_scope`
  - `apply_masks`
  - `compute_metrics`
  - `evaluate_thresholds`
  - `emit_reports`

### Agents (prov:Agent)

At minimum:

- pipeline runner (service identity)
- human steward or reviewer identity (when approval/override exists)
- CI validator agent (when CI emits/validates lineage)

### Relations (minimum)

- `prov:used` (activity → input entities)
- `prov:wasGeneratedBy` (output entities → activity)
- `prov:wasAssociatedWith` (activity → agent)
- `prov:wasDerivedFrom` (outputs derived from inputs, baselines, configs)

---

## 🧾 OpenLineage alignment (ops posture)

OpenLineage is recommended when:

- you need consistent “job/run/task” events across CI and schedulers,
- you want standardized event fields for monitoring and cost/energy attribution.

Recommended mapping:

- OpenLineage `runId` → KFM `run_id` (stable)
- OpenLineage inputs/outputs → PROV-O Entities
- OpenLineage job namespace + name → PROV-O `prov:Activity` identifiers

When both exist, include a cross-reference field in PROV:

- `kfm:openlineage_run_id`

---

## 🧷 Deterministic identifiers (required)

Validation provenance MUST use stable, deterministic identifiers:

### Run identifier

`run_id` should be stable within the governed run context, e.g.:

- `urn:kfm:run:<pipeline_name>:<yyyy-mm-ddThh:mm:ssZ>:<scope_hash>`

Where:

- `pipeline_name` is pinned and versioned
- `scope_hash` is derived from:
  - sorted input ids + checksums
  - config snapshot checksum
  - mask policy checksum

### Entity identifiers

For entities that correspond to catalog artifacts:

- use STAC `id` (or full URL/URN) when available
- include checksums for immutability:
  - `sha256` preferred

For derived artifacts:

- deterministic URN scheme:
  - `urn:kfm:artifact:validation:<family>:<run_id>:<name>`

---

## 📦 Required provenance fields (fail-closed)

A provenance bundle (PROV or OpenLineage) MUST provide enough information to reproduce and audit.

### Required (minimum)

- `run_id`
- `algorithm_id` and version
- `config_snapshot` reference or checksum
- `input_pack` reference or checksum (input URIs + digests)
- `created_utc` (timestamps)
- governance posture:
  - `care_gate_status`
  - `sovereignty_gate`
- outputs:
  - output artifact identifiers + digests (at least the metrics summary)

### Strongly recommended

- environment fingerprint (tool versions, container digest if available)
- baseline/reference identifiers (if used)
- sampling metadata:
  - seed
  - sample frame hash

---

## 🛡️ Governance and redaction rules (FAIR+CARE)

Provenance can leak sensitive detail if it embeds:

- precise coordinates,
- restricted site identifiers,
- “how to locate” references,
- signed URLs, tokens, or internal endpoints.

Rules:

- provenance stored in public docs paths MUST:
  - avoid raw coordinates
  - avoid restricted identifiers
  - prefer generalized spatial scopes (`kansas`, region, coarse H3)
- when restricted collections are involved:
  - set `care_gate_status = redact|deny`
  - include `redaction_summary` counts and reason codes
  - store detailed traces only in governed restricted locations (referenced, not embedded)

---

## 🗺️ Provenance linkage to STAC and DCAT

### STAC linkage (recommended pattern)

Validation outputs SHOULD be linked in STAC as either:

- assets on a validation STAC Item (preferred), or
- properties referencing provenance bundles.

Recommended fields:

- `assets.prov_jsonld` (href + checksum)
- `assets.metrics_summary_json` (href + checksum)
- `properties.kfm:algorithm_id`
- `properties.kfm:run_id`
- `properties.prov:wasDerivedFrom` (array of input ids)
- `properties.kfm:care_gate_status`
- `properties.kfm:sovereignty_gate`

### DCAT linkage (recommended pattern)

When validation outputs are published as datasets/distributions:

- use `dct:provenance` to summarize lineage and point to PROV JSON-LD
- distributions reference immutable artifacts (with checksums)

---

## 🧠 Standard provenance bundle shape (illustrative)

A minimal PROV-O JSON-LD bundle SHOULD include:

~~~json
{
  "@context": ["https://www.w3.org/ns/prov.jsonld"],
  "entity": {
    "urn:kfm:artifact:validation:input_pack:...": {
      "prov:type": "kfm:InputPack",
      "kfm:sha256": "<sha256>"
    },
    "urn:kfm:artifact:validation:config_snapshot:...": {
      "prov:type": "kfm:ConfigSnapshot",
      "kfm:sha256": "<sha256>"
    },
    "urn:kfm:artifact:validation:metrics_summary:...": {
      "prov:type": "kfm:MetricsSummary",
      "kfm:sha256": "<sha256>"
    }
  },
  "activity": {
    "urn:kfm:activity:validation:...": {
      "prov:type": "kfm:ValidationRun",
      "prov:startedAtTime": "YYYY-MM-DDTHH:MM:SSZ",
      "prov:endedAtTime": "YYYY-MM-DDTHH:MM:SSZ",
      "kfm:run_id": "urn:kfm:run:<...>",
      "kfm:algorithm_id": "kfm:rs:validate:<family>:<name>:v1",
      "kfm:care_gate_status": "allow|redact|deny",
      "kfm:sovereignty_gate": "clear|restricted|conflict|unknown"
    }
  },
  "agent": {
    "urn:kfm:agent:ci": {
      "prov:type": "kfm:CIValidator"
    }
  },
  "wasAssociatedWith": {
    "_:assoc1": {
      "prov:activity": "urn:kfm:activity:validation:...",
      "prov:agent": "urn:kfm:agent:ci"
    }
  },
  "used": {
    "_:used1": {
      "prov:activity": "urn:kfm:activity:validation:...",
      "prov:entity": "urn:kfm:artifact:validation:input_pack:..."
    },
    "_:used2": {
      "prov:activity": "urn:kfm:activity:validation:...",
      "prov:entity": "urn:kfm:artifact:validation:config_snapshot:..."
    }
  },
  "wasGeneratedBy": {
    "_:gen1": {
      "prov:entity": "urn:kfm:artifact:validation:metrics_summary:...",
      "prov:activity": "urn:kfm:activity:validation:..."
    }
  }
}
~~~

> The exact schema is governed by KFM-PROV v11; the snippet above illustrates minimum concepts and linkages.

---

## 🗺️ High-level provenance flow

~~~mermaid
flowchart TD
  A["Enumerate input artifacts (STAC/DCAT)"] --> B["Freeze config snapshot (pinned)"]
  B --> C["Compute validation metrics (deterministic)"]
  C --> D["Evaluate thresholds (policy)"]
  D --> E["Emit metrics summary + optional detailed report"]
  E --> F["Emit provenance (PROV-O and/or OpenLineage)"]
  F --> G["Link provenance into STAC/DCAT + rollups"]
~~~

---

## 🧪 CI/CD expectations (recommended)

CI SHOULD validate that:

- provenance bundle exists for every governed validation run,
- required fields are present (run_id, algorithm_id, inputs, outputs, checksums),
- there are no restricted fields or secrets in public artifacts,
- provenance references are resolvable (no dangling refs),
- reason-code ordering and outcome derivation are deterministic (where applicable).

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed provenance reference for remote-sensing validation; defined PROV-O/OpenLineage posture, deterministic ids, required fields, STAC/DCAT linkage patterns, and governance-safe redaction rules. |

---

<div align="center">

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="KFM-PROV v11" src="https://img.shields.io/badge/KFM--PROV-v11-blue" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

[⬅ Methods](../README.md) ·
[🧮 Algorithms](../algorithms/README.md) ·
[📐 Metrics](../metrics/README.md) ·
[🧾 Reports](../../reports/README.md) ·
[🏛️ Governance Charter](../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

---
title: "🧪 KFM — CI Test Lineage (Single‑Job Pattern · PROV‑O JSON‑LD)"
path: ".github/lineage/README.md"

version: "v11.2.6"
last_updated: "2025-12-13"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability & FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Runbook"
header_profile: "standard"
footer_profile: "standard"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

scope:
  domain: "documentation"
  applies_to:
    - ".github/lineage/**"
    - ".github/workflows/**"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"

indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by KFM-MDP v12"

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:doc:github:lineage:ci-test-lineage:v11.2.6"
semantic_document_id: "kfm-ci-test-lineage-single-job-prov-jsonld"
event_source_id: "ledger:kfm:doc:github:lineage:ci-test-lineage:v11.2.6"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "metadata-extraction"
  - "layout-normalization"

ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

story_node_refs: []
immutability_status: "version-pinned"
---

<div align="center">

# 🧪 **KFM — CI Test Lineage**
`.github/lineage/README.md`

**Purpose**  
Emit **one** PROV‑O JSON‑LD file per CI job at `artifacts/lineage/prov.jsonld` capturing **who/what ran, when, inputs, outputs, and status** so failures are immediately debuggable and runs are replayable.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/KFM--PROV-v11-blue" />
<img src="https://img.shields.io/badge/CI-Lineage%20Artifact-brightgreen" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Governance%20Aligned-orange" />

</div>

---

## 📘 Overview

This runbook defines a **single‑job** provenance emission pattern:

- **One file per job**: `artifacts/lineage/prov.jsonld`
- **Always emitted** (pass/fail) so post‑mortems don’t depend on logs
- **Minimal, stable identifiers** to support replay, audit, and graph ingestion

**Design constraints**

- Treat the PROV file as a **job-scoped bundle**.
- Prefer **stable IDs** (run id + attempt + job) over human strings.
- Include **hashes** for emitted artifacts when feasible.

---

## 🗂️ Directory Layout

~~~text
📁 .github/
├── 📁 lineage/
│   └── 📄 README.md                         — CI lineage runbook (this file)
└── 📁 workflows/
    └── 📄 kfm-ci.yml                        — CI workflow(s) emit prov.jsonld (job end)

📁 artifacts/
├── 📁 lineage/
│   └── 🧾 prov.jsonld                       — PROV‑O JSON‑LD (one per job)
├── 📁 test-results/
│   └── 🧾 junit.xml                         — optional test artifact
└── 📁 coverage/
    └── 🧾 coverage.xml                      — optional coverage artifact
~~~

---

## 🧭 Context

KFM treats provenance as a **first‑class, queryable output**. CI is part of the provenance chain: it validates, transforms, and produces artifacts that must be attributable to a run, a workflow, and a code revision.

This pattern intentionally keeps CI lineage:

- **Small** (single file)
- **Portable** (artifact upload/download)
- **Machine‑parseable** (JSON‑LD with PROV vocabulary)
- **Composable** (can be ingested later into graph / catalogs)

---

## 📦 Data & Metadata

### Emission contract

Each CI job MUST write:

- **Path**: `artifacts/lineage/prov.jsonld`
- **Timing**: at end of job
- **Condition**: always (pass/fail)

### Minimal PROV‑O JSON‑LD bundle (example)

Replace placeholders (e.g., `COMMIT_SHA`, `GITHUB_RUN_ID`) using your CI runtime values.

~~~json
{
  "@context": [
    "https://www.w3.org/ns/prov.jsonld",
    {
      "kfm": "urn:kfm:",
      "ci": "urn:kfm:ci:",
      "git": "urn:kfm:git:",
      "schema": "http://schema.org/",
      "status": { "@id": "schema:actionStatus", "@type": "@id" },
      "artifact": "schema:CreativeWork",
      "sha256": "schema:sha256"
    }
  ],
  "@id": "ci:run/GITHUB_RUN_ID/GITHUB_RUN_ATTEMPT/GITHUB_JOB",
  "@type": "prov:Bundle",
  "prov:hadMember": [
    {
      "@id": "ci:entity/repo",
      "@type": "prov:Entity",
      "prov:label": "Kansas Frontier Matrix Monorepo",
      "prov:location": "git@github.com:kfm/kansas-frontier-matrix.git",
      "git:ref": "refs/heads/main",
      "git:commit": "COMMIT_SHA"
    },
    {
      "@id": "ci:entity/test-config",
      "@type": "prov:Entity",
      "prov:label": "Pytest Config",
      "prov:value": "pytest.ini",
      "sha256": "SHA256_OF_FILE"
    },
    {
      "@id": "ci:agent/github-actions",
      "@type": ["prov:Agent", "prov:SoftwareAgent"],
      "prov:label": "GitHub Actions",
      "schema:softwareVersion": "runner-ubuntu-24.04"
    },
    {
      "@id": "ci:activity/test-job",
      "@type": "prov:Activity",
      "prov:label": "Run unit tests",
      "prov:startedAtTime": "2025-12-13T00:02:15Z",
      "prov:endedAtTime": "2025-12-13T00:04:29Z",
      "status": "schema:CompletedActionStatus",
      "prov:used": ["ci:entity/repo", "ci:entity/test-config"],
      "prov:wasAssociatedWith": "ci:agent/github-actions",
      "prov:generated": ["ci:entity/junit-report", "ci:entity/coverage-report"]
    },
    {
      "@id": "ci:entity/junit-report",
      "@type": ["prov:Entity", "artifact"],
      "prov:label": "JUnit XML",
      "prov:location": "artifacts/test-results/junit.xml",
      "sha256": "SHA256_OF_JUNIT"
    },
    {
      "@id": "ci:entity/coverage-report",
      "@type": ["prov:Entity", "artifact"],
      "prov:label": "Coverage XML",
      "prov:location": "artifacts/coverage/coverage.xml",
      "sha256": "SHA256_OF_COVERAGE"
    }
  ]
}
~~~

### Hashing helpers (recommended)

~~~bash
# Example: compute sha256 fields (Linux runners)
sha256sum pytest.ini | awk '{print $1}'
sha256sum artifacts/test-results/junit.xml | awk '{print $1}'
sha256sum artifacts/coverage/coverage.xml | awk '{print $1}'
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

- **PROV‑O**: `artifacts/lineage/prov.jsonld` is a job‑scoped `prov:Bundle` containing the `prov:Activity`, `prov:Entity` inputs/outputs, and the `prov:Agent` that executed the run.
- **DCAT**: CI lineage artifacts can be exposed as a `dcat:Distribution` of a CI run record (when promoted to a catalog).
- **STAC**: If represented as a non‑spatial STAC Item, set `geometry: null` and store `prov.jsonld` as an asset linked from the CI run’s catalog record.

---

## 🧪 Validation & CI/CD

### Workflow step pattern (GitHub Actions)

~~~yaml
- name: Emit CI lineage (PROV-O JSON-LD)
  if: always()
  run: |
    mkdir -p artifacts/lineage
    # Write prov.jsonld here (template + substitution)
    # Ensure this step never exposes secrets or tokens.

- name: Upload lineage artifact
  if: always()
  uses: actions/upload-artifact@v4
  with:
    name: lineage-${{ github.job }}
    path: artifacts/lineage/prov.jsonld
~~~

### Local smoke checks

~~~bash
test -s artifacts/lineage/prov.jsonld
python -m json.tool artifacts/lineage/prov.jsonld > /dev/null
~~~

---

## ⚖ FAIR+CARE & Governance

- Do **not** write secrets, tokens, credentials, or PII into provenance.
- Prefer identifiers already public in CI context (workflow/job/run IDs, commit SHA).
- If a job handles restricted or sovereignty‑sensitive materials, record lineage at a **safe abstraction level** (e.g., dataset IDs, not precise sensitive locations).

---

## 🕰️ Version History

| Version | Date | Notes |
|---|---:|---|
| v11.2.6 | 2025-12-13 | Initial governed runbook for single‑job PROV‑O JSON‑LD lineage emission. |

---

<div align="center">

**Governance & Policy**

[🏛️ Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

</div>

---
title: "🔐 Kansas Frontier Matrix — Data Integrity Standards"
path: "docs/standards/data-integrity/README.md"
version: "v11.2.6"
last_updated: "2025-12-12"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · FAIR+CARE Council · Security & Reliability Board"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Standards Index"
intent: "data-integrity-standards-index"
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

scope:
  domain: "data-integrity"
  applies_to:
    - "data/**"
    - "releases/**"
    - "mcp/**"
    - "tools/**"
    - ".github/**"
    - "docs/**"

classification: "Public"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
jurisdiction: "Kansas / United States"

indigenous_rights_flag: true
data_steward: "Security & Reliability Board"

commit_sha: "<latest-commit-hash>"
doc_uuid: "urn:kfm:doc:standards:data-integrity:index:v11.2.6"
semantic_document_id: "kfm-standards-data-integrity-index-v11.2.6"
event_source_id: "ledger:kfm:doc:standards:data-integrity:index:v11.2.6"
doc_integrity_checksum: "<sha256>"

governance_ref: "../governance/ROOT-GOVERNANCE.md"
ethics_ref: "../faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../sovereignty/INDIGENOUS-DATA-PROTECTION.md"

provenance_chain:
  - "docs/standards/data-integrity/README.md@v11.2.6"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
  - "layout-normalization"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# 🔐 Data Integrity Standards

`docs/standards/data-integrity/README.md` · Standards Index · v11.2.6

**Purpose**  
Define the governed standards that ensure KFM datasets are **tamper-evident**, **verifiable**, and **policy-compliant** across ETL, catalogs, graph ingest, and publication.

<img alt="KFM-MDP" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="MCP-DL" src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img alt="Status" src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

</div>

---

## 📘 Overview

Data integrity in KFM is the intersection of:

- **immutability** (raw inputs preserved; derived artifacts are reproducible),
- **tamper evidence** (checksums + signing),
- **verifiability** (offline verification from stored evidence),
- **provenance integrity** (lineage is complete and resolvable),
- **policy enforcement** (publish is blocked if governance requirements fail).

### What this index covers

This domain includes standards and controls for:

- checksum calculation and inventory manifests
- signing datasets and release bundles
- build/provenance attestations for deterministic runs
- policy-as-code gates (governance, licensing, sensitivity, provenance)
- verification workflows (CI, local, and downstream consumers)

### Minimum compliance statement (normative)

A dataset MUST NOT be published (served by API/UI, referenced by Story Nodes, or distributed externally) unless:

1. all artifacts are checksum-inventoried,
2. integrity evidence is present and verifiable (per release policy),
3. provenance is resolvable (STAC/DCAT/PROV alignment),
4. all policy gates pass (license, governance, sensitivity, sovereignty constraints).

### Standards in this domain

- **Dataset Signing, Attestation & Policy Enforcement**  
  `docs/standards/data-integrity/dataset-signing-attestation.md`

If additional domain standards exist, list them here as they are added:

- `docs/standards/data-integrity/artifact-manifests.md` (recommended)
- `docs/standards/data-integrity/policy-gates.md` (recommended)
- `docs/standards/data-integrity/verification-runbook.md` (recommended)

---

## 🗂️ Directory Layout

Recommended placement for data-integrity evidence, tooling, and release artifacts:

~~~text
docs/
└── 📁 standards/
    └── 📁 data-integrity/
        ├── 📄 README.md                                 🔐 This index
        └── 📄 dataset-signing-attestation.md             🔏 Signing + attestation + policy enforcement

tools/
└── 📁 integrity/                                        🧰 Integrity tooling (recommended)
    ├── 📄 manifest.py                                   🧾 Build/validate manifests
    ├── 📄 sign.py                                       ✍️ Sign release bundles
    ├── 📄 attest.py                                     🧾 Emit attestations
    ├── 📄 verify.py                                     ✅ Verify checksums/signatures/attestations
    └── 📁 policy/                                       🧷 Policy-as-code rules

mcp/
└── 📁 runs/
    └── 📁 <run_id>/                                     🧪 Config snapshot + logs + validation reports

releases/
└── 📁 <release_version>/
    ├── 📄 manifest.zip                                  📦 Artifact inventory + checksums
    ├── 📄 signature.sig                                 🔏 Signature (manifest bundle)
    ├── 📄 slsa-attestation.json                          🧾 Build/provenance attestation
    └── 📄 sbom.spdx.json                                 🧱 SBOM (when applicable)
~~~

---

## 🧭 Context

### Why this exists

KFM operates across long timelines, multiple systems, and multiple publication pathways. Integrity standards ensure:

- a dataset can be verified years later,
- provenance claims can be audited,
- governance and sovereignty constraints are enforced consistently,
- consumers (graph/API/UI) can reject untrusted artifacts.

### Trust boundaries

- **UI** MUST NOT assume correctness; it relies on API + catalog integrity evidence.
- **API** SHOULD refuse or quarantine datasets that fail verification or policy gates.
- **Story Nodes / Focus Mode** MUST reference cataloged items that resolve integrity evidence.

### Non-goals

- Secrets management and encryption-at-rest are handled by security policy, not by these standards.
- Integrity does not imply correctness; it proves **what** an artifact is and **how** it was made.

---

## 🧱 Architecture

Data-integrity controls are applied as a cross-cutting layer across KFM:

- ETL produces deterministic artifacts and run metadata
- manifests inventory outputs and checksums
- signing and attestation bind artifacts to identities and build steps
- policy gates block publication when requirements fail
- catalogs (STAC/DCAT/PROV) carry integrity references forward to graph/API/UI

---

## 📦 Data & Metadata

### Canonical integrity evidence objects

- **Checksums** (SHA-256 per artifact)
- **Manifest bundle** (inventory + checksums + minimal metadata)
- **Signature** (cryptographic binding of identity to manifest)
- **Attestation** (structured statement of inputs, config, toolchain, and outputs)
- **Gate report** (which policies passed/failed; non-sensitive)

### Required metadata (minimum)

Publishable artifacts MUST be traceable to:

- license and attribution expectations
- governance constraints (including sovereignty flags)
- run configuration snapshot
- provenance references (PROV entities/activities/agents)

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

Integrity evidence SHOULD be representable by:

- checksum-bearing assets (or checksum sidecars)
- asset roles (`data`, `metadata`, `provenance`, `manifest`)
- references to release evidence (manifest/signature/attestation) when governed

### DCAT

DCAT distributions SHOULD expose:

- license + publisher/creator
- distribution-level verification pointers (when feasible)
- a path to the manifest bundle for offline verification

### PROV-O

PROV MUST support:

- artifacts as `prov:Entity` with links to checksum-bearing evidence
- transformation steps as `prov:Activity`
- signing/publishing identities as `prov:Agent`

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Deterministic ETL outputs"] --> B["Checksum + manifest inventory"]
  B --> C["Signing + attestation"]
  C --> D["Policy evaluation gates"]
  D -->|pass| E["Catalog publish (STAC/DCAT/PROV)"]
  D -->|fail| F["Block publish + record gate report"]
  E --> G["Graph/API/UI/Story Nodes consume verified artifacts"]
~~~

---

## 🧠 Story Node & Focus Mode Integration

### Evidence rule (normative)

Story Nodes MUST only reference:

- STAC Items whose assets resolve to checksum-bearing artifacts,
- and (for governed releases) those artifacts MUST be verifiable via stored release evidence.

### Focus Mode constraints

Focus Mode MAY summarize integrity evidence and highlight verification states, but MUST NOT:

- invent verification outcomes,
- bypass policy gates,
- claim trust without verifiable evidence.

---

## 🧪 Validation & CI/CD

Minimum required gates for governed publication typically include:

- schema validation (data + catalogs)
- provenance completeness validation
- license and rights validation
- sensitivity/sovereignty policy checks
- checksum/manifest verification
- signature verification (per release policy)
- attestation validation (per release policy)

Any failure MUST block publish and must produce a non-sensitive gate report.

---

## ⚖ FAIR+CARE & Governance

- Integrity evidence MUST NOT leak restricted locations or controlled overlays.
- Sovereignty constraints apply to both datasets and the metadata about how they are produced and distributed.
- Exceptions to signing/attestation requirements MUST be explicitly documented and scoped by governance.

Binding references:

- Governance: `governance_ref`
- Ethics: `ethics_ref`
- Sovereignty: `sovereignty_policy`

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-12 | Created domain index for data-integrity standards; formalized scope, trust boundaries, and the integrity evidence model (manifest + signing + attestation + policy gates). |

---

<div align="center">

[📘 Docs Root](../../README.md) ·
[📑 Standards Index](../README.md) ·
[🔏 Dataset Signing Standard](./dataset-signing-attestation.md) ·
[⚖️ Governance Charter](../governance/ROOT-GOVERNANCE.md) ·
[🧬 FAIR+CARE Guide](../faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix · CC‑BY 4.0

</div>


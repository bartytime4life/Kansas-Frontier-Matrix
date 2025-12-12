---
title: "🛡️ Kansas Frontier Matrix — Supply-Chain Security Reference Repos (SLSA · Sigstore · Policy Gates)"
path: "docs/security/supply-chain/reference-repos/README.md"
version: "v11.2.6"
last_updated: "2025-12-12"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Security & Reliability Council · FAIR+CARE Oversight"
content_stability: "stable"

status: "Active / In-Repo Canonical"
doc_kind: "Reference Guide"
intent: "clone-and-adapt-reference-repos"
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
  domain: "security-supply-chain"
  applies_to:
    - ".github/**"
    - "ci/**"
    - "tools/**"
    - "scripts/**"
    - "mcp/**"
    - "releases/**"
    - "data/**"
    - "docs/**"

classification: "Public"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
jurisdiction: "Kansas / United States"

indigenous_rights_flag: true
data_steward: "Security & Reliability Council"

commit_sha: "<latest-commit-hash>"
doc_uuid: "urn:kfm:doc:security:supply-chain:reference-repos:v11.2.6"
semantic_document_id: "kfm-security-supply-chain-reference-repos-v11.2.6"
event_source_id: "ledger:kfm:doc:security:supply-chain:reference-repos:v11.2.6"
doc_integrity_checksum: "<sha256>"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

provenance_chain:
  - "docs/security/supply-chain/reference-repos/README.md@v11.2.6"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "a11y-adaptations"
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

# 🛡️ Supply-Chain Security Reference Repos
SLSA provenance · Sigstore signing · Policy gating patterns for KFM v11

</div>

---

## 📘 Overview

This guide catalogs pragmatic, README-rich example repositories that are useful to clone into a scratch space and adapt into KFM’s governed CI/CD patterns for:

- **provenance attestations** (SLSA / in-toto style)
- **signing and verification** (Sigstore / Cosign patterns)
- **policy-as-code gating** (OPA / Conftest / Rego patterns)

### KFM target outcome (normative)

Every governed artifact (code, container, dataset bundle, STAC/DCAT/PROV exports, UI builds) MUST be traceable to a **verifiable build** with:

- checksum inventory (manifest)
- attestations (provenance + build context)
- signature evidence (publisher identity binding)
- policy gates that block release/publish when requirements fail

### Scope notes

- These upstream references evolve. KFM adaptations MUST pin versions and record what was adopted.
- This document is a **reference guide**, not an upstream mirror of external repositories.

---

## 🗂️ Directory Layout

~~~text
docs/
└── 📁 security/
    └── 📁 supply-chain/
        ├── 📄 README.md
        ├── 📁 reference-repos/
        │   └── 📄 README.md                              ← this file
        ├── 📁 policies/
        │   ├── 📄 README.md
        │   └── 📁 rego/
        │       ├── 📄 README.md
        │       └── 📄 kfm-release-gates.rego
        └── 📁 workflows/
            ├── 📄 README.md
            └── 📄 provenance-workflow-map.md

.github/
└── 📁 workflows/
    ├── 📄 kfm-ci.yml
    ├── 📄 kfm-release.yml
    └── 📄 kfm-attest.yml

tools/
└── 📁 integrity/
    ├── 📄 manifest.py                                   (inventory + checksums)
    ├── 📄 sign.py                                       (signing wrapper)
    ├── 📄 attest.py                                     (attestation emission wrapper)
    ├── 📄 verify.py                                     (verification wrapper)
    └── 📁 policy/                                       (policy-as-code evaluation helpers)

releases/
└── 📁 v11.2.6/
    ├── 📄 sbom.spdx.json
    ├── 📄 manifest.zip
    └── 📁 attestations/
        ├── 📄 provenance.intoto.jsonl
        ├── 📄 sbom.attestation.json
        └── 📄 signature.bundle
~~~

---

## 🧭 Context

### Why reference repos are used

KFM is governed, long-lived, and multi-output (data + catalogs + graph + applications). Reference repos are used to accelerate adoption of established patterns for:

- tamper-evident publishing
- provenance reproducibility
- policy-enforced releases

### Compatibility statement

KFM patterns should remain compatible with:

- SLSA-style provenance attestations
- Sigstore / Cosign signing and verification
- OPA policy evaluation and Rego-based gates

Implementation details (tools, CI provider, keyless vs key-backed) may vary by environment, but **verification must remain portable**.

---

## 🧱 Architecture

### Where this fits in the KFM pipeline

~~~text
Deterministic ETL
  → Catalog builds (STAC/DCAT/PROV)
  → Graph ingest
  → API + UI builds
  → Story Nodes / Focus Mode distribution
  ↳ Integrity layer (manifests, signing, attestations, policy gates) applies across all stages
~~~

### The three reference repos

#### 1) slsa-framework/slsa-github-generator

Why it matters for KFM:

- a concrete blueprint for producing SLSA-style provenance using CI workflows
- useful when KFM needs repeatable provenance for:
  - release artifacts (e.g., manifest bundles)
  - SBOMs
  - build outputs (API container images, UI bundles)
  - deterministic data pipeline packages (ETL runners, catalog builders)

KFM adaptation pattern:

- treat KFM workflows as “builders” that emit:
  - provenance attestation
  - references to SBOM + manifest + telemetry bundles
- store attestations in `releases/<version>/attestations/` and link them from:
  - release manifests
  - governed dataset docs
  - CI lineage outputs

#### 2) sigstore/cosign

Why it matters for KFM:

- a practical standard for signing artifacts and verifying signatures
- matches KFM’s governance posture: artifacts must be tamper-evident, verifiable, and policy-gated

KFM adaptation pattern:

- sign:
  - container images (API, UI, workers)
  - immutable blobs (release archives, deterministic exports)
  - attestations (provenance, SBOM)
- verify on:
  - PR checks (optional soft gates)
  - release workflows (hard gates)
  - deployment workflows (hard gates)

#### 3) Trusted-builds demo ecosystems (policy-gated promotion)

Why it matters for KFM:

- demonstrates end-to-end: workflows + attestations + policy gates that decide whether to promote
- KFM can mirror this: “only ship if provenance + signatures + policy pass”

KFM adaptation pattern:

- encode policy checks aligned with KFM governance:
  - builder identity allowlist
  - pinning rules (actions are SHA-pinned)
  - SBOM present + referenced
  - attestation present + verified
  - “no secret outputs” rules (sanitization / redaction)
  - sovereignty constraints are enforced for public bundles

---

## 📦 Data & Metadata

### What counts as a “release artifact” in KFM

Minimum set for a governed release SHOULD include:

- `manifest.zip` (what shipped; inventory + checksums)
- `sbom.spdx.json` (what it contains)
- `attestations/*` (what proves how it was built)
- signature evidence (what proves integrity and publisher identity)

### Attestation and signing expectations (normative)

- every artifact in a governed release MUST be checksum-inventoried
- provenance attestations MUST reference the artifact checksums they claim to build
- signatures MUST bind identity to the release inventory (directly or via bundle)

---

## 🌐 STAC, DCAT & PROV Alignment

### Catalog artifacts as governed outputs

When a release includes STAC/DCAT/PROV outputs:

- catalogs are treated as first-class release artifacts
- catalogs MUST be included in the manifest inventory
- catalogs SHOULD be referenced by provenance attestations (build inputs, config, outputs)

### Linking integrity evidence into catalogs

Recommended (implementation-specific) approach:

- STAC assets reference checksums (or checksum sidecars)
- PROV entities link to checksum-bearing artifacts
- DCAT distributions include integrity hints where feasible

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Build outputs<br/>datasets, catalogs, containers, docs"] --> B["Inventory + checksums<br/>(manifest)"]
  B --> C["Provenance attestation<br/>(SLSA / in-toto style)"]
  B --> D["Signing evidence<br/>(Sigstore / Cosign patterns)"]
  C --> E["Policy gates<br/>(OPA / Rego)"]
  D --> E
  E -->|pass| F["Release publish + deploy"]
  E -->|fail| G["Block release + record gate report"]
~~~

---

## 🧠 Story Node & Focus Mode Integration

### Evidence rule (normative)

Story Nodes MUST reference cataloged Items whose artifacts are:

- checksum-inventoried, and
- verifiable under governed release rules where applicable

### Focus Mode guardrails

Focus Mode MAY summarize integrity evidence and policy status, but MUST NOT:

- claim trust without verification evidence
- bypass policy gates
- invent attestation contents or verification results

---

## 🧪 Validation & CI/CD

### CI/CD impact

Adds or modifies:

- `.github/workflows/kfm-attest.yml` (attestation job)
- `.github/workflows/kfm-release.yml` (sign + verify + gate)
- `docs/security/supply-chain/policies/rego/*` (policy-as-code)
- `tools/integrity/*` and/or `scripts/attest/*` (deterministic helpers)

### Expected gates

- PR: soft gates (report-only) for early adoption
- Release: hard gates (must pass) for governed artifacts

### Example workflow snippets (tilde-fenced)

Provenance emission:

~~~bash
./scripts/attest/generate_provenance.sh \
  --version "${KFM_VERSION}" \
  --manifest "releases/${KFM_VERSION}/manifest.zip" \
  --sbom "releases/${KFM_VERSION}/sbom.spdx.json" \
  --out "releases/${KFM_VERSION}/attestations/provenance.intoto.jsonl"
~~~

Signing:

~~~bash
cosign sign-blob \
  --output-signature "releases/${KFM_VERSION}/attestations/manifest.sig" \
  "releases/${KFM_VERSION}/manifest.zip"

cosign sign-blob \
  --output-signature "releases/${KFM_VERSION}/attestations/sbom.sig" \
  "releases/${KFM_VERSION}/sbom.spdx.json"
~~~

Verification + policy gate:

~~~bash
./scripts/attest/verify_all.sh "releases/${KFM_VERSION}"

opa eval \
  --data "docs/security/supply-chain/policies/rego/kfm-release-gates.rego" \
  --input "releases/${KFM_VERSION}/policy-input.json" \
  "data.kfm.release.allow == true"
~~~

---

## ⚖ FAIR+CARE & Governance

- provenance and signatures strengthen auditability without requiring trust in infrastructure
- integrity evidence MUST NOT be used to disclose restricted knowledge

If a dataset or Story Node is marked restricted (CARE / sovereignty / NHPA §304), policy gates MUST enforce:

- no public artifact publication
- no inclusion in public manifests
- gated access-only distribution paths

Binding references:

- Governance: `governance_ref`
- Ethics: `ethics_ref`
- Sovereignty: `sovereignty_policy`

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---:|---|
| v11.2.6 | 2025-12-12 | Applied KFM-MDP v11.2.6 structure: normalized front-matter, approved H2 ordering, tilde-fenced directory layout and examples, standardized footer governance links, and clarified reference-repo adaptation patterns. |

---

<div align="center">

[⬅️ Security Index](../../README.md) ·
[🧱 Architecture Index](../../../architecture/README.md) ·
[⚖️ Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🧬 FAIR+CARE Guide](../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix · CC‑BY 4.0

</div>

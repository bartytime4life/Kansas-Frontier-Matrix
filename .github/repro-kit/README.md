---
title: "🧳 KFM — CI-Triggered Repro-Kit Pattern (Deterministic, Sanitized, Attested)"
path: ".github/repro-kit/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability & FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Pattern"
header_profile: "standard"
footer_profile: "standard"
intent: "kfm-ci-repro-kit"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

semantic_document_id: "kfm-ci-repro-kit"
doc_uuid: "urn:kfm:ci:repro-kit:v11.2.6"
event_source_id: "ledger:.github/repro-kit/README.md"
immutability_status: "version-pinned"

governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
security_ref: "../../SECURITY.md"

sbom_ref: "../../releases/v11.2.6/sbom.spdx.json"
attestation_ref: "../../releases/v11.2.6/slsa-attestations/repro-kit.slsa.json"

telemetry_schema: "../../schemas/telemetry/github-workflows-v4.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

classification: "Public Document"
sensitivity: "Low to Medium (artifact content gated)"
sensitivity_level: "Variable"
risk_category: "Reliability & Security"
indigenous_rights_flag: "Dataset-level"
redaction_required: true

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "metadata-extraction"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-claims"
  - "hallucinated-datasets"
  - "governance-override"
---

<div align="center">

# 🧳 **KFM — CI-Triggered Repro-Kit Pattern**
`.github/repro-kit/README.md`

**Purpose**  
When CI fails, emit a compact **repro-kit**: a deterministic, sanitized, and attested bundle containing only what is needed to replay the failure locally or in CI.

**Why**  
Faster triage, smaller artifacts, safer sharing, and verifiable lineage (PROV-O + OpenLineage) under FAIR+CARE and security policy.

<br/>

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" alt="KFM-MDP v11.2.6" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" alt="MCP-DL v6.3" />
<img src="https://img.shields.io/badge/Supply%20Chain-SLSA%20%2F%20in--toto-success" alt="SLSA / in-toto" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" alt="Active / Enforced" />

</div>

---

## 📘 Overview

A **repro-kit** is a small, self-describing bundle produced by CI when a job fails. It contains:

- **Deterministic replay inputs** (or remote pointers + checksums)
- A tiny **replay script** (or OCI recipe)
- **Evidence**:
  - a **PROV-O JSON-LD** run document
  - an **OpenLineage** event JSON
  - validation summaries and integrity hashes
- **Sanitization evidence** showing secrets/PII redaction was applied
- **Attestation** (SLSA / in-toto) binding kit contents to the CI run identity

A repro-kit is intentionally **not** a general “debug dump.” It is:
- minimal,
- policy-gated,
- time-limited by default,
- and cryptographically verifiable.

**Design goals (normative):**
- **Deterministic**: only pinned/seeded inputs or remote pointers with checksums.
- **Minimal**: typically ≤ a few MB; exclude caches and bulky logs.
- **Portable**: 1-command replay (script or container).
- **Forensic**: input hashes, output hashes, config snapshot references.
- **Safe**: secrets scrubbed, PII redacted, governance gates enforced.
- **Ephemeral**: short TTL; long-term retention requires explicit promotion.

---

## 🗂️ Directory Layout

This pattern documentation lives here:

~~~text
📁 .github/
└── 📁 repro-kit/                     # CI repro-kit pattern (docs + contracts)
    └── 📄 README.md                  # This document
~~~

### Repro-kit bundle layout (normative)

A repro-kit MUST be a single archive (zip/tar) with the following structure:

~~~text
📦 repro-kit/                         # Root inside archive (single bundle)
├── 🧾 manifest.json                  # Required: primary manifest (machine-readable)
├── 📁 replay/                        # Replay entrypoints and human notes
│   ├── 🧪 repro.sh                   # Optional: POSIX replay script
│   ├── 🧪 repro.ps1                  # Optional: PowerShell replay script
│   └── 📄 README.md                  # Optional: replay notes (no secrets/PII)
├── 📁 inputs/                        # Minimal fixtures (or remote pointers)
│   ├── 📁 files/                     # Optional: tiny files needed to reproduce
│   └── 📁 pointers/                  # Required when inputs are remote (URIs + checksums)
├── 📁 evidence/                      # Required: lineage + validation + integrity
│   ├── 🧬 prov.jsonld                # Required: PROV-O Activity/Entity/Agent chain
│   ├── 🧾 openlineage.json           # Required: OpenLineage event JSON
│   ├── 🧾 validation-summary.json    # Recommended: validator outputs (counts, failures)
│   └── 🔐 checksums.sha256           # Required: sha256 list for files in the kit
├── 📁 sanitization/                  # Required: redaction evidence
│   ├── 🧾 redaction-report.json      # Required: what was removed/masked and why
│   └── 🧾 allowlist.json             # Optional: allowlisted fields/paths snapshot
└── 📁 attestations/                  # Required: supply-chain attestations
    ├── 🧾 repro-kit.slsa.json        # Required: SLSA/in-toto attestation (or equivalent)
    └── 🧾 signing-info.json          # Optional: signer metadata (no secrets)
~~~

**Rules (normative):**
- If an input cannot be safely included (size/sensitivity), include a **pointer** with:
  - `uri`, `retrieval_instructions`, and a **checksum/content hash**.
- If a kit cannot be safely produced (policy gate), CI must emit a **quarantine stub**:
  - `manifest.json` + `redaction-report.json` explaining why the kit was blocked.

---

## 🧭 Context

Repro-kits accelerate triage across:
- ETL failures (schema drift, contract violations, data quality regressions)
- Catalog validation failures (STAC/DCAT shape/links)
- Graph ingestion failures (dedupe/constraint regressions)
- Build/test failures (unit/integration/test fixture mismatches)
- Docs/lint policy failures (Markdown protocol checks, schema lint, etc.)

**Who uses them:**
- CI triagers
- maintainers and reviewers
- governance/security stewards (when the kit is quarantined)

**Where they fit:**
- Repro-kits are CI artifacts that bridge “a failing run” to “a replayable failure case.”
- Repro-kits complement (but do not replace) governed run logs and evidence under:
  - `mcp/runs/`
  - `data/reports/`

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["CI job fails"] --> B["Collect minimal inputs\n(pinned or pointers + checksums)"]
  B --> C["Sanitize\n(secret scan + PII redaction + policy gates)"]
  C --> D["Package\n(manifest + replay script + evidence)"]
  D --> E["Attest\n(SLSA / in-toto)"]
  E --> F["Upload\n(short TTL secure store)"]
  F --> G["Open GitHub Issue\n(link kit + evidence JSON)"]
  G --> H["Replay\n(local or CI)"]
~~~

~~~mermaid
flowchart LR
  K["📦 repro-kit bundle"] --> M["🧾 manifest.json"]
  K --> R["🧪 replay scripts"]
  K --> I["📁 inputs (files/pointers)"]
  K --> E["📁 evidence (prov/openlineage/validation)"]
  K --> S["📁 sanitization (redaction report)"]
  K --> A["📁 attestations (SLSA/in-toto)"]
~~~

---

## 🧪 Validation & CI/CD

### When to create a repro-kit (recommended triggers)

- On failure of:
  - data pipeline validation jobs
  - STAC/DCAT validation jobs
  - schema lint / contract tests
  - critical unit/integration tests
- On flaky failures:
  - only after `N` retries (to avoid generating kits for transient runner issues)

### What must be validated before upload (normative)

A kit MUST NOT be uploaded unless:

- `manifest.json` exists and is parseable
- checksums file exists and matches kit contents
- sanitization report exists and states `status: publishable`
- attestation exists (or a configured “attestation unavailable” exception applies)
- size and TTL policies are satisfied

### Local replay runbook (normative)

Minimum replay sequence (illustrative):

~~~text
1) Unpack repro-kit.zip
2) Verify evidence/checksums.sha256
3) Fetch any inputs/pointers (if present) using sanctioned tooling
4) Run replay/repro.sh (or repro.ps1)
5) Confirm the failure reproduces (expected_exit_code)
~~~

If the failure does not reproduce:
- the kit must be treated as incomplete,
- and a follow-up kit should be generated with updated minimal inputs.

---

## 📦 Data & Metadata

### `manifest.json` contract (normative)

The manifest MUST be sufficient to replay, verify, and trace the kit without guessing.

Required top-level fields:

~~~json
{
  "kit_version": "1",
  "kit_id": "urn:kfm:repro-kit:<uuid>",
  "created_at": "2025-12-14T00:00:00Z",
  "ttl_hours": 168,
  "classification": "internal",
  "reason": "CI failure reproduction",
  "repo": {
    "remote": "<origin-url-or-redacted>",
    "commit_sha": "<sha>",
    "ref": "<branch-or-pr>",
    "paths_touched": ["<optional>"]
  },
  "ci": {
    "provider": "github-actions",
    "workflow": "<workflow-name>",
    "job": "<job-name>",
    "run_id": "<run-id>",
    "run_attempt": 1,
    "runner_os": "<os>",
    "runner_arch": "<arch>"
  },
  "replay": {
    "entrypoint": "replay/repro.sh",
    "mode": "local",
    "expected_exit_code": 1,
    "notes": "Run from repo root. No network unless retrieving remote pointers."
  },
  "inputs": {
    "included_bytes": 123456,
    "pointers": [
      {
        "name": "source_dataset",
        "uri": "<remote-uri-or-dvc-pointer>",
        "checksum_sha256": "<sha256>",
        "size_bytes": 123,
        "retrieval": "Fetch via sanctioned tool; verify sha256 before use."
      }
    ]
  },
  "evidence": {
    "prov_path": "evidence/prov.jsonld",
    "openlineage_path": "evidence/openlineage.json",
    "validation_summary_path": "evidence/validation-summary.json",
    "checksums_path": "evidence/checksums.sha256"
  },
  "sanitization": {
    "redaction_report_path": "sanitization/redaction-report.json",
    "policy": "default"
  },
  "attestation": {
    "slsa_path": "attestations/repro-kit.slsa.json",
    "subject_digest_sha256": "<sha256-of-archive-or-root-manifest>"
  }
}
~~~

### Checksums file (normative)

`evidence/checksums.sha256` MUST list sha256 hashes for all files in the kit except the checksum file itself.

~~~text
<sha256>  manifest.json
<sha256>  evidence/prov.jsonld
<sha256>  evidence/openlineage.json
...
~~~

### Sanitization report (normative)

`sanitization/redaction-report.json` MUST state:

- which scanners ran (secret scan, PII scan, allowlist/denylist policy)
- what was removed/masked (paths/field names; no raw secrets)
- whether the kit is:
  - **publishable** (upload allowed), or
  - **quarantined** (upload blocked or restricted)

~~~json
{
  "status": "publishable",
  "scans": [
    { "name": "secret-scan", "result": "pass" },
    { "name": "pii-scan", "result": "pass" }
  ],
  "redactions": [
    { "type": "path-excluded", "path": "inputs/files/raw_dump.json", "reason": "exceeds size policy" },
    { "type": "field-masked", "field": "api_key", "reason": "secret pattern" }
  ],
  "policy": {
    "ttl_hours": 168,
    "max_size_bytes": 52428800,
    "network_allowed": false
  }
}
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC
A repro-kit MAY be represented as a non-spatial STAC Item (optional pattern):
- `geometry: null`
- `properties.datetime = last_updated`
- `assets.repro_kit.href` points to the artifact store location (or a stable pointer)

### DCAT
This document is a documentation dataset:
- `semantic_document_id` maps to `dct:identifier`
- Markdown is a `dcat:Distribution` (`mediaType: text/markdown`)
- The repro-kit bundle can be a `dcat:Distribution` with access constraints and TTL.

### PROV-O
- The repro-kit is a `prov:Entity` that was generated by a CI `prov:Activity`.
- CI bots and councils are `prov:Agent`s.
- Inputs, pointers, and validation evidence are additional `prov:Entity` nodes linked by `prov:used` and `prov:wasDerivedFrom`.

---

## 🧱 Architecture

### Components (logical)

A CI implementation of this pattern has five deterministic stages:

1. **Collect**
   - Select minimal files and pointers needed to reproduce the failure.
   - Never include caches unless they are the failing input and policy allows.

2. **Sanitize**
   - Run secret scan and PII scan.
   - Apply allowlist-based selection where possible.
   - If policy fails: emit a quarantine stub (manifest + redaction report) and stop.

3. **Package**
   - Build the bundle with a fixed layout.
   - Write `manifest.json` and `checksums.sha256`.
   - Include a replay entrypoint if feasible.

4. **Attest**
   - Generate an in-toto / SLSA attestation binding:
     - kit digests,
     - CI run identity,
     - commit SHA.
   - Signing keys are managed by CI and never embedded in the kit.

5. **Publish**
   - Upload to a short-TTL secure artifact store (or GitHub artifacts if configured).
   - Open/update an Issue linking:
     - kit location,
     - manifest,
     - validation summary,
     - attestation.

### Determinism contract (normative)

A repro-kit MUST be replayable without ambiguity:

- Inputs are included **or** referenced by stable pointers + checksums.
- Replay script MUST:
  - pin window/range/seed (if applicable),
  - fail if required inputs are missing,
  - verify checksums before running.
- Network retrieval is permitted only for explicitly listed pointers and MUST verify checksums before use.

---

## ⚖ FAIR+CARE & Governance

Repro-kits are governed artifacts.

**Hard constraints:**
- No secrets, tokens, credentials, private keys.
- No direct PII.
- No sensitive location precision when governance requires masking/generalization.
- No restricted Indigenous data or culturally sensitive materials unless authority exists and the kit is quarantined to a restricted store.

**Default posture:**
- **Fail-closed**: if sanitization or governance gates cannot certify safety, do not publish.
- **Short TTL** by default:
  - extension or promotion to long-term retention requires explicit approval.
- **Traceability** is mandatory:
  - every kit must be tied to a CI run + commit SHA + attestation.

Authoritative references:
- Governance: `../../docs/standards/governance/ROOT-GOVERNANCE.md`
- FAIR+CARE: `../../docs/standards/faircare/FAIRCARE-GUIDE.md`
- Sovereignty: `../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md`
- Security: `../../SECURITY.md`

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Upgraded repro-kit pattern to KFM-MDP v11.2.6; fixed emoji-aligned directory trees; defined normative bundle layout, manifest contract, sanitization evidence, attestation expectations, and fail-closed governance gates. |

---

<div align="center">

🧳 **KFM — CI-Triggered Repro-Kit Pattern (v11.2.6)**  
Deterministic · Sanitized · Attested · Traceable

[⬅ Back to Repository Root](../../README.md) ·
[⚖ Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[🛡️ Security Policy](../../SECURITY.md)

</div>

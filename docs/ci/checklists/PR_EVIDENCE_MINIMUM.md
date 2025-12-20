---
title: "🧾 PR Evidence: Minimum Merge Requirements — OpenLineage · PROV‑O · STAC · Sigstore"
path: "docs/ci/checklists/PR_EVIDENCE_MINIMUM.md"
version: "v12.0.0"
last_updated: "2025-12-20"
status: "active"
doc_kind: "Checklist"
license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v11.0.0"
dcat_profile: "KFM-DCAT v11.0.0"
prov_profile: "KFM-PROV v11.0.0"

governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:ci:checklists:pr-evidence-minimum:v12.0.0"
semantic_document_id: "kfm-ci-checklist-pr-evidence-minimum-v12.0.0"
event_source_id: "ledger:kfm:doc:ci:checklists:pr-evidence-minimum:v12.0.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# 🧾 PR Evidence Minimum Merge Requirements

Applies to evidence bundles covering **OpenLineage**, **PROV‑O JSON‑LD**, **STAC**, and **Sigstore/Cosign** attestations.

## 📘 Overview

### Purpose
This checklist defines the **minimum reproducibility and provenance evidence** that MUST be attached to every PR that changes **data-producing code**, **schemas**, **configs**, or **datasets**.
CI **fails closed** if any required element is missing or inconsistent.

### Scope

| In Scope | Out of Scope |
|---|---|
| PRs that change ETL / transforms / catalog builders | Pure copy-edit doc PRs with no runtime or catalog impact |
| PRs that change dataset schemas, validators, telemetry schemas | UI-only styling changes with no data provenance surface changes |
| PRs that add/modify processed outputs or derived datasets | Non-functional refactors that provably do not change outputs (still recommended to attach a dry-run evidence bundle) |
| PRs that change CI evidence collection / policy gates | — |

### Audience
- Primary: contributors shipping data-affecting changes
- Secondary: reviewers, CI Council, security reviewers

### Definitions
- Link: `docs/glossary.md`
- Terms used in this doc:
  - OpenLineage
  - PROV‑O JSON‑LD
  - STAC Item / Collection
  - Sigstore / Cosign / Rekor
  - SLSA provenance attestation
  - OPA / Rego “fail closed” policy gate
  - “Run ID” / “Job name” / “Commit SHA” (cross-consistency keys)

### Key artifacts
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| OpenLineage START event | `.github/lineage/runs/RUN_START.json` | PR author | MUST pair with COMPLETE, same `runId` |
| OpenLineage COMPLETE event | `.github/lineage/runs/RUN_COMPLETE.json` | PR author | MUST include outputs + checksums |
| PROV activity/entity bundle | `.github/lineage/prov/activity.jsonld` | PR author | MUST align with OpenLineage & STAC |
| Sigstore attestation | `.github/attestations/<runId>.intoto.jsonl` | PR author | MUST verify; Rekor inclusion proof required |
| Sigstore verification output | `.github/attestations/verify.txt` | CI | MUST capture verify output including log index |
| STAC Item(s) for outputs | `data/**/stac/**/<item-id>.json` | PR author | One per output (or per partition) |

### Definition of done
- [ ] All required evidence files exist in canonical paths
- [ ] OpenLineage START+COMPLETE pair validates and shares same `runId`
- [ ] PROV activity+entities validate and align to OpenLineage (checksums + identifiers)
- [ ] STAC Item(s) validate and align to OpenLineage + PROV (derived_from + checksums)
- [ ] Sigstore attestation verification passes and records Rekor log index
- [ ] Cross-consistency checks pass (job name + commit SHA consistent across artifacts)

## 🗂️ Directory Layout

### This document
- `path`: `docs/ci/checklists/PR_EVIDENCE_MINIMUM.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| PR evidence — lineage | `.github/lineage/` | OpenLineage + PROV artifacts used for CI gating |
| PR evidence — attestations | `.github/attestations/` | Cosign attestations + verification output |
| PR evidence policy | `.github/policy/` | OPA/Rego policy + CI-collected input bundle |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Canonical published catalogs (separate from PR evidence attachments) |
| CI workflows | `.github/workflows/` | GitHub Actions / CI gates |

### Expected file tree for this sub-area
~~~text
📁 docs/
└── 📁 ci/
    └── 📁 checklists/
        └── 📄 PR_EVIDENCE_MINIMUM.md

📁 .github/
├── 📁 lineage/
│   ├── 📁 runs/
│   │   ├── 📄 RUN_START.json
│   │   └── 📄 RUN_COMPLETE.json
│   └── 📁 prov/
│       └── 📄 activity.jsonld
├── 📁 attestations/
│   ├── 📄 <runId>.intoto.jsonl
│   └── 📄 verify.txt
└── 📁 policy/
    ├── 📄 pr_evidence.rego
    └── 📄 input.json
~~~

## 🧭 Context

### Background
KFM requires deterministic, provenance-linked outputs so downstream catalogs, graph builds, APIs, and Focus Mode narratives never drift from source evidence.

### Assumptions
- Runs are reproducible (stable configs, deterministic seeds, pinned environments where applicable).
- Output assets have stable **sha256** hashes available at build time.
- CI has access to the evidence bundle and verifies it as part of gating.

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode is preserved.
- Frontend consumes contracts via APIs (no direct graph dependency).
- CI **fails closed** for missing/inconsistent evidence.

### Operational profile
- Release stage: Stable / Governed
- Lifecycle: Long‑Term Support (LTS)
- Review cycle: Per‑PR · CI Council
- Content stability: stable
- SLSA target: ≥ SLSA L3 (attestation present)

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Should “schemaDataset.hashes.sha256” be required for inputs as well as outputs in all pipelines? | CI Council | TBD |
| Do partitioned outputs require both Collection + Item(s) or Item(s) only? | Catalog Council | TBD |

### Future extensions
- Add SBOM evidence (CycloneDX/SPDX) for containerized runs.
- Add telemetry evidence for energy/carbon signals where required.
- Extend policy to validate DCAT dataset records for new datasets (fail-closed).

## 🗺️ Diagrams

### Evidence gate dataflow
~~~mermaid
flowchart LR
  PR[PR changes] --> CI[CI evidence collector]

  CI --> OL[OpenLineage RUN_START/RUN_COMPLETE]
  CI --> PV[PROV activity.jsonld]
  CI --> ST[STAC Item(s)]
  CI --> SG[Sigstore attestation + verify.txt]

  OL --> OPA[OPA policy evaluation]
  PV --> OPA
  ST --> OPA
  SG --> OPA

  OPA -->|allow=true| MERGE[Merge allowed]
  OPA -->|allow=false| FAIL[Fail closed]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| PR diff | git | GitHub | change classification rules |
| OpenLineage run events | JSON | `.github/lineage/runs/` | schema + pairing + hashes |
| PROV bundle | JSON‑LD | `.github/lineage/prov/` | JSON‑LD lint + referential integrity |
| STAC Items | JSON | `data/**/stac/**` | STAC lint + derived_from resolution |
| Sigstore attestation | intoto JSONL | `.github/attestations/` | cosign verify-attestation + Rekor |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| OPA input bundle | JSON | `.github/policy/input.json` | internal CI contract |
| Gate decision | boolean | CI logs | policy evaluation |
| Verification transcript | text | `.github/attestations/verify.txt` | required evidence record |

### Sensitivity & redaction
- Do not commit secrets, credentials, or tokens in any evidence file.
- If verify output includes identities, ensure it contains no sensitive tokens; redact if policy requires.

### Quality signals
- Checksums present and consistent across OpenLineage ↔ PROV ↔ STAC ↔ Sigstore subject digests.
- Derived_from links resolve to all required inputs.
- Timestamps present and ordered (START < COMPLETE; generation times recorded in PROV).

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Each output dataset MUST have a STAC Item that:
  - includes `links[]` with `rel="derived_from"` for all inputs
  - includes per-asset sha256 (`checksum:sha256` or equivalent)
  - includes processing metadata:
    - `processing:software` (repo + commit)
    - `processing:lineage` pointer to PROV/OpenLineage evidence artifacts

### DCAT
- For PRs introducing a new dataset intended for publication:
  - a DCAT dataset record SHOULD be added/updated under `data/catalog/dcat/`
  - at minimum: title, description, license, keywords, distribution links

### PROV‑O
- `prov:Activity` identifies the run.
- `prov:used` lists inputs.
- `prov:generated` lists outputs.
- Entities include `kfm:checksumSha256` and version/commit reference.

### Versioning
- Use STAC versioning links and graph predecessor/successor relationships where applicable.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| Evidence collector | Build a single CI input bundle from repo artifacts | `.github/policy/input.json` |
| OpenLineage validator | Pair START/COMPLETE and assert hashes + IO | `.github/lineage/runs/*.json` |
| PROV validator | Lint JSON‑LD, validate references | `.github/lineage/prov/activity.jsonld` |
| STAC validator | Validate item schema + derived_from resolution | `data/**/stac/**` |
| Sigstore verifier | Verify attestations and capture Rekor log index | `.github/attestations/*` |
| OPA policy gate | Fail closed unless allow=true | `.github/policy/pr_evidence.rego` |

### Interfaces / contracts
- Evidence artifacts MUST be machine-parseable JSON/JSON‑LD.
- Hash algorithm: sha256 (required).
- Identity and policy for Sigstore verification is project-governed (do not hardcode secrets).

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Any dataset/asset used by Story Nodes or Focus Mode MUST remain provenance-linked.
- This checklist ensures evidence is present so UI audit panels can render:
  - dataset IDs
  - lineage links
  - checksum verification indicators

### Provenance-linked narrative rule
- Focus Mode only consumes provenance-linked content.

## 🧪 Validation & CI/CD

### Required evidence
All items below MUST pass for merge approval.

1) OpenLineage run telemetry pair
- Required files in `.github/lineage/runs/`:
  - `RUN_START.json`
  - `RUN_COMPLETE.json`
- Each MUST include:
  - `job`, `run` (stable `runId`), and `eventType` ∈ {`START`,`COMPLETE`}
  - non-empty `inputs[]` and `outputs[]` with dataset namespace+name
  - for each input/output asset: documentation/data-quality facets AND a content hash
    - example: `facets.schemaDataset.hashes.sha256`

Minimal example:
~~~json
{
  "eventType": "START",
  "job": {"namespace":"kfm/pipelines/air","name":"pm25_bias_correction"},
  "run": {"runId":"c0ffee-..."},
  "inputs":[
    {
      "namespace":"kfm://epa/aqs",
      "name":"pm25_raw",
      "facets":{
        "schemaDataset":{"hashes":{"sha256":"<sha256>"}}
      }
    }
  ],
  "outputs":[
    {"namespace":"kfm://kfm/pm25","name":"pm25_corrected"}
  ]
}
~~~

2) PROV‑O JSON‑LD activity/entity mapping
- File: `.github/lineage/prov/activity.jsonld`
- MUST contain:
  - `prov:Activity` (the run), `prov:used` (inputs), `prov:generated` (outputs)
  - `prov:wasAssociatedWith` (workflow/repo ref)
  - generation timestamps (e.g., via `prov:qualifiedGeneration`)
  - entities include checksum (`kfm:checksumSha256`) and version/commit reference

Minimal frame:
~~~json
{
  "@context":[
    "https://www.w3.org/ns/prov.jsonld",
    {"kfm":"https://kfm.example/ns#"}
  ],
  "@graph":[
    {
      "@id":"urn:run:c0ffee",
      "@type":"prov:Activity",
      "prov:startedAtTime":"2025-12-20T04:00Z",
      "prov:used":[{"@id":"urn:ds:epa_aqs_pm25_raw"}],
      "prov:generated":[{"@id":"urn:ds:kfm_pm25_corrected"}],
      "prov:wasAssociatedWith":{"@id":"urn:repo:kfm@<commit_sha>"}
    },
    {
      "@id":"urn:ds:epa_aqs_pm25_raw",
      "@type":"prov:Entity",
      "kfm:checksumSha256":"<sha256>"
    },
    {
      "@id":"urn:ds:kfm_pm25_corrected",
      "@type":"prov:Entity",
      "kfm:checksumSha256":"<sha256>"
    }
  ]
}
~~~

3) STAC evidence for outputs
- For each output dataset, commit a STAC Item under the appropriate domain path (canonical STAC placement is governed by the data catalog conventions in the repo).
- Each Item MUST include:
  - `links[]` with `rel="derived_from"` to all inputs
  - per-asset sha256 checksum (e.g., `assets.*["checksum:sha256"]`)
  - processing metadata:
    - `processing:software` with repo+commit
    - `processing:lineage` pointer to PROV/OpenLineage artifacts

Minimal fields:
~~~json
{
  "type":"Feature",
  "stac_version":"1.0.0",
  "properties":{
    "processing:software":[{"name":"kfm-pipelines","version":"<commit_sha>"}],
    "processing:lineage":"./../../../.github/lineage/prov/activity.jsonld"
  },
  "links":[{"rel":"derived_from","href":"kfm://epa/aqs/pm25_raw"}],
  "assets":{
    "data":{
      "href":"pm25_corrected.parquet",
      "checksum:sha256":"<sha256>"
    }
  }
}
~~~

4) Sigstore/Cosign attestation with Rekor timestamp
- Provide verified attestation for the run’s artifact set or container image:
  - `.github/attestations/<runId>.intoto.jsonl`
  - `.github/attestations/verify.txt` (captured output)
- Required validations:
  - `cosign verify-attestation` succeeds against project identity/policy
  - Rekor inclusion proof present (log index recorded)
  - subject digest(s) correspond to output asset checksums or image digest

Example verify command (record output):
~~~bash
cosign verify-attestation --type slsaprovenance --key cosign.pub \
  kfm.registry.local/pipelines/pm25@sha256:<digest> \
  | tee .github/attestations/verify.txt
~~~

### CI validation order
1. Schema & location: required files exist in required paths.
2. OpenLineage pair check: START & COMPLETE share same `runId`; IO lists non-empty; hashes present.
3. PROV JSON‑LD lint: activity↔entity references resolve; checksums align with OpenLineage.
4. STAC lint: derived_from links resolve; asset checksums match PROV/OpenLineage hashes.
5. Sigstore verify: verify-attestation exit code=0; Rekor log index captured in verify output.
6. Cross-consistency: job name + commit SHA consistent across all artifacts.

### Required paths
- `.github/lineage/runs/RUN_START.json`
- `.github/lineage/runs/RUN_COMPLETE.json`
- `.github/lineage/prov/activity.jsonld`
- `.github/attestations/<runId>.intoto.jsonl`
- `.github/attestations/verify.txt`
- `data/**/stac/**/<item-id>.json` (one per output)

### CI wiring with OPA and Rego
Place this policy at `.github/policy/pr_evidence.rego` and evaluate in CI.

~~~rego
package kfm.pr.evidence

default allow = false

required_paths := {
  ".github/lineage/runs/RUN_START.json",
  ".github/lineage/runs/RUN_COMPLETE.json",
  ".github/lineage/prov/activity.jsonld",
  ".github/attestations/verify.txt"
}

missing_required_paths[p] {
  p := required_paths[_]
  not input.fs.exists[p]
}

allow {
  # 1) All required files exist
  count(missing_required_paths) == 0

  # 2) OpenLineage START/COMPLETE pairing
  input.openlineage.start.run.runId == input.openlineage.complete.run.runId
  input.openlineage.start.eventType == "START"
  input.openlineage.complete.eventType == "COMPLETE"
  count(input.openlineage.complete.outputs) > 0

  # 3) Each output has a checksum and is mapped in PROV & STAC
  every_output_has_evidence

  # 4) Sigstore verification (incl. Rekor)
  input.sigstore.verify_ok == true
  input.sigstore.rekor_index != ""
}

every_output_has_evidence {
  not output_violation[_]
}

# Violation: missing checksum on any output
output_violation[out] {
  out := input.openlineage.complete.outputs[_]
  sha := out.facets.schemaDataset.hashes.sha256
  sha == ""
}

# Violation: no matching PROV entity for output checksum
output_violation[out] {
  out := input.openlineage.complete.outputs[_]
  sha := out.facets.schemaDataset.hashes.sha256
  sha != ""
  not prov_match(out.name, sha)
}

# Violation: no matching STAC asset checksum
output_violation[out] {
  out := input.openlineage.complete.outputs[_]
  sha := out.facets.schemaDataset.hashes.sha256
  sha != ""
  not stac_match(sha)
}

prov_match(name, sha) {
  ent := input.prov.entities[_]
  ent.name == name
  ent.checksumSha256 == sha
}

stac_match(sha) {
  item := input.stac_items[_]
  item.assets.data["checksum:sha256"] == sha
}
~~~

Minimal CI collector JSON handed to OPA (example path: `.github/policy/input.json`):
~~~json
{
  "fs":{"exists":{
    ".github/lineage/runs/RUN_START.json":true,
    ".github/lineage/runs/RUN_COMPLETE.json":true,
    ".github/lineage/prov/activity.jsonld":true,
    ".github/attestations/verify.txt":true
  }},
  "openlineage":{
    "start":{"eventType":"START","run":{"runId":"c0ffee"}},
    "complete":{"eventType":"COMPLETE","run":{"runId":"c0ffee"},"outputs":[{"name":"pm25_corrected","facets":{"schemaDataset":{"hashes":{"sha256":"abc123"}}}}]}
  },
  "prov":{"entities":[{"name":"pm25_corrected","checksumSha256":"abc123"}]},
  "stac_items":[{"assets":{"data":{"checksum:sha256":"abc123"}}}],
  "sigstore":{"verify_ok":true,"rekor_index":"1234567"}
}
~~~

### GitHub Actions snippet
Add a gate in `.github/workflows/ci.yml`:

~~~yaml
- name: Collect PR evidence → OPA input
  run: |
    python .github/policy/collect_pr_evidence.py > .github/policy/input.json

- name: Evaluate PR evidence policy
  uses: open-policy-agent/opa-github-actions@v2
  with:
    policy-path: .github/policy/pr_evidence.rego
    data-path: .github/policy/input.json
~~~

### Reviewer quicklist
Merge only if all items are ✅:

- [ ] OpenLineage START+COMPLETE present, same `runId`, IO populated, checksums present
- [ ] PROV activity+entities align; checksums match OpenLineage
- [ ] STAC Items exist; derived_from links correct; asset checksums match
- [ ] cosign verify-attestation passed; Rekor index recorded in verify output
- [ ] Rego policy gate evaluates to allow=true

### Notes & tips
- Use deterministic seeds/config snapshots so re-runs reproduce identical checksums.
- If outputs are partitioned:
  - attach one STAC Item per partition, OR
  - use a Collection + Items with per-asset checksums.
- For schema-only PRs:
  - still produce a dry-run OpenLineage+PROV linking schema version to no-op outputs
  - attach a governed waiver if policy requires it.

## ⚖ FAIR+CARE & Governance

### Review gates
- CI Council review: required (per-PR)
- Security council review: required when attestation identity/policy changes
- FAIR+CARE review: required when new sensitive layers or restricted locations are introduced

### CARE / sovereignty considerations
- Do not publish precise sensitive locations or culturally restricted details in evidence artifacts.
- Apply generalization/redaction policies before public release.

### AI usage constraints
- Do not generate new policy text from AI without human governance review.
- Do not infer sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v11.2.6 | 2025-12-20 | Prior checklist format (pre-v12 template alignment) | TBD |
| v12.0.0 | 2025-12-20 | Rebuilt to v12 Universal Governed Doc structure | TBD |

---

Footer refs:
- Back: `docs/ci/README.md`
- Data Architecture: `docs/architecture/README.md`
- Governance Charter: `docs/standards/README.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

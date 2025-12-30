---
title: "KFM Reproducibility Kit — Action: <action-name>"
path: ".github/repro-kit/actions/<action-name>/README.md"
version: "v1.0.0"
last_updated: "2025-12-30"
status: "draft"
doc_kind: "Guide"
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

doc_uuid: "urn:kfm:doc:github:repro-kit-action:<action-name>:readme:v1.0.0"
semantic_document_id: "kfm-github-repro-kit-action-<action-name>-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github:repro-kit-action:<action-name>:readme:v1.0.0"
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

# KFM Reproducibility Kit — Action: `<action-name>`

## 📘 Overview

### Purpose

This directory contains a **repo-local GitHub Action** located at `.github/repro-kit/actions/<action-name>/` that exists to:

- provide **CI ↔ local parity** for reproducibility steps (so checks don’t drift),
- package, hash, and/or validate **run manifests** and provenance artifacts for audit-friendly review,
- enforce KFM’s **provenance-first, contract-first** expectations at automation time.

> This README is required for every action under `.github/repro-kit/actions/`.
> Keep it **in sync** with `action.yml` in this same folder.

### Scope

| In Scope | Out of Scope |
|---|---|
| A composite (preferred) or JS/Docker action that orchestrates reproducible checks or packaging | Managing production secrets, privileged access, or replaying restricted data |
| Validating/packaging evidence artifacts, manifests, hashes, provenance bundles | Defining governance policy (see `docs/governance/**`) |
| Wrapping canonical validators/tests (no re-implementation) | Creating unsourced narrative or bypassing the API boundary |

### Audience

- CI maintainers (workflows/actions)
- Contributors running repro-kit steps locally
- Reviewers validating determinism, catalogs/provenance, and contract alignment

### Definitions (link to glossary)

- Link: `docs/glossary.md` *(not confirmed in repo; recommended)*
- **Deterministic**: same inputs + same config + same code revision ⇒ same outputs (byte-for-byte when practical).
- **Idempotent**: re-running does not create duplicates or inconsistent outputs.
- **Run manifest**: portable record capturing how to reproduce a run (inputs, config, commit SHA, versions, parameters).
- **PROV bundle**: provenance artifacts describing inputs, activities, outputs, and agents.
- **Stable identifier**: ID that remains stable across runs and links catalogs ↔ graph ↔ API ↔ UI.

### Key artifacts (what this action points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This action | `.github/repro-kit/actions/<action-name>/` | CI / Repro-kit maintainers | `action.yml` + this README |
| Repro-kit root README | `.github/repro-kit/README.md` | Repo maintainers | Canonical repro-kit intent + constraints |
| Merge-gating actions | `.github/actions/` | CI maintainers | Required PR gates live here |
| Workflows | `.github/workflows/` | CI maintainers | Workflows calling this action |
| Master Guide | `docs/MASTER_GUIDE_v12.md` | KFM maintainers | Canonical pipeline ordering + invariants |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Data engineering | Provenance-first metadata artifacts |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] Inputs/outputs tables reflect `action.yml`
- [ ] Failure modes + exit behavior documented
- [ ] Artifact naming/location documented (and doesn’t violate governance)
- [ ] Determinism and redaction rules are explicit
- [ ] Example workflow snippet provided

---

## 🗂️ Directory Layout

### This document

- `path`: `.github/repro-kit/actions/<action-name>/README.md` *(must match front-matter)*

### Expected file tree

~~~text
📁 .github/
└── 📁 repro-kit/
    └── 📁 actions/
        └── 📁 <action-name>/
            ├── 📄 action.yml
            ├── 📄 README.md
            └── 📁 src/                 # optional helper scripts (keep minimal)
~~~

---

## 🧭 KFM Alignment (non-negotiables)

### Canonical pipeline ordering (must not be violated)

This action must respect KFM’s canonical ordering:

**ETL → STAC/DCAT/PROV → Graph → API boundary → UI → Story Nodes → Focus Mode**

Implications for this action:

- If this action touches dataset outputs, it must validate or package **STAC/DCAT/PROV** artifacts **before** any graph load or narrative surfacing occurs.
- If this action validates UI or Story Nodes, it must enforce: **UI reads via APIs** and **no unsourced narrative**.
- This action must be **fail-closed** when it is used as a required reproducibility step (unless explicitly configured otherwise).

### Boundary with `.github/actions/`

Use `.github/repro-kit/actions/<action-name>/` when the primary purpose is:

- reproducibility packaging (manifests/hashes/prov bundles), and/or
- local/CI parity for reproduction workflows.

Prefer `.github/actions/` when the action is:

- a required merge gate, or
- primarily workflow glue without repro artifact packaging responsibilities.

---

## 🎯 What this action does

### Summary

**Action name:** `<action-name>`  
**Primary intent:** <!-- e.g., “package run manifest + hashes”, “validate catalogs”, “golden fixture compare” -->  
**Used by:** <!-- list workflows or scripts that call it -->

### Pipeline stages impacted (check all that apply)

- [ ] Tooling/CI (`.github/**`, `tools/**`)
- [ ] ETL (`src/pipelines/**`, writes outputs under `data/**/{raw,work,processed}`)
- [ ] Catalogs (`data/stac/**`, `data/catalog/dcat/**`, `data/prov/**`)
- [ ] Graph (`src/graph/**`, `data/graph/**`)
- [ ] API boundary (`src/server/**`, `src/server/contracts/**`)
- [ ] UI (`web/**`)
- [ ] Story Nodes (`docs/reports/story_nodes/**`)
- [ ] Schemas (`schemas/**`)
- [ ] Tests (`tests/**`)
- [ ] Releases (`releases/**`)

### Inputs

> Keep this table aligned with `action.yml`.

| Input | Required | Default | Description |
|---|---:|---|---|
| `target_root` | false | `.` | Root directory to operate on |
| `artifact_dir` | false | `repro-artifacts/` | Where to place packaged outputs (usually as CI artifacts) |
| `artifact_name` | false | `<action-name>` | Base name for produced artifacts |
| `fail_on_diff` | false | `true` | If comparing hashes, fail when diffs are detected |
| `redaction_mode` | false | *(omit unless policy exists)* | Only include if repo defines a mode |

### Outputs

> Keep this table aligned with `action.yml` outputs (if any).

| Output | Description |
|---|---|
| `artifact_path` | Path to packaged artifact directory/file |
| `summary_path` | Path to a machine-readable summary (if produced) |

### Environment assumptions

- Runner OS support: <!-- ubuntu-latest? other? -->
- Tool/runtime dependencies: <!-- e.g., node, python, jq -->
- Network requirements: <!-- e.g., none / allowlist / download-only -->

---

## 📦 Artifacts produced (and where they go)

### Expected artifacts

| Artifact | Location | Notes |
|---|---|---|
| Run manifest | `${artifact_dir}/manifest.json` | Must include commit SHA, versions, and stable IDs where applicable |
| Hash report | `${artifact_dir}/hashes.json` | Prefer stable ordering; include algorithm (sha256) |
| PROV bundle (optional) | `${artifact_dir}/prov_bundle.json` | If produced, also link to `data/prov/**` when meaningful |
| Human summary | `${artifact_dir}/summary.md` | Short, reviewer-friendly summary |

### Artifact rules

- Do **not** commit derived provenance/catalog payloads into `docs/**`.
- Prefer publishing artifacts as **workflow artifacts** unless the repo defines a canonical committed location.
- Artifacts must not leak restricted locations or sensitive identifiers; apply redaction/generalization upstream of packaging.

---

## 🔐 Security, governance, and data handling

### Hard constraints

- **No secrets**: never print tokens/keys; never embed credentials in outputs.
- **No accidental PII**: manifests must avoid personal data unless explicitly permitted and classified.
- **Sensitive locations**: do not log raw restricted geometries/coordinates; prefer generalized forms.

### Governance triggers (flag for human review)

Governance review is required when this action introduces or changes:

- packaging of new external data sources,
- new public-facing artifacts (e.g., releases),
- behaviors that could expose restricted locations via logs or artifacts,
- AI-assisted narrative generation or transformation beyond allowed modes.

---

## ♻️ Determinism & idempotency contract

### Determinism expectations

- Stable sort order for manifests/reports (avoid non-deterministic directory traversal).
- Fixed timestamps: prefer explicit timestamps from inputs; otherwise isolate runtime timestamps to metadata-only fields.
- Stable IDs/keys: do not re-key downstream identifiers silently; migrations must be explicit elsewhere.

### Idempotency expectations

- Re-running should overwrite artifacts in `${artifact_dir}` predictably (or write to a run-specific directory keyed by run ID).
- Never append duplicate records to manifests/reports without a run-scoped namespace.

---

## 🧩 How to use in a workflow

### Example (GitHub Actions)

~~~yaml
jobs:
  repro:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Run repro-kit action (<action-name>)
        uses: ./.github/repro-kit/actions/<action-name>
        with:
          target_root: "."
          artifact_dir: "repro-artifacts/"
          artifact_name: "<action-name>"
          fail_on_diff: true

      # Example artifact upload (workflow-level responsibility)
      - name: Upload repro artifacts
        uses: actions/upload-artifact@v4
        with:
          name: repro-artifacts-<action-name>
          path: repro-artifacts/
~~~

### Local reproduction

> Local reproduction commands are **not confirmed in repo**.
> If your repo supports local running (scripts, `act`, `make`, etc.), document the canonical command(s) here.

~~~bash
# Example only — replace with repo-standard local command(s):
# tools/repro-kit run <action-name> --artifact-dir repro-artifacts/
~~~

---

## ✅ Validation & failure modes

### What constitutes failure

- Missing required inputs or invalid configuration
- Validator failures (schema/contract checks)
- Hash diffs when `fail_on_diff: true`
- Forbidden content detected (secrets/PII/sensitive-location leakage)

### Typical exit behavior

- Fail-closed when used in CI gating contexts
- Emit a short summary file (`summary.md`) describing what failed and where to look next

### Troubleshooting checklist

- Confirm `action.yml` inputs match the workflow `with:` block
- Confirm paths exist and are repo-relative
- Confirm outputs are written under `${artifact_dir}`
- If diffs exist, inspect `${artifact_dir}/hashes.json` and any compare report

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-30 | Initial action README scaffold for `<action-name>` | TBD |

---

## 🔗 References

- Repro-kit root README: `.github/repro-kit/README.md`
- Repro-kit actions index: `.github/repro-kit/actions/README.md`
- Merge-gating actions: `.github/actions/README.md`
- Workflows: `.github/workflows/README.md`
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Governance root: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
---


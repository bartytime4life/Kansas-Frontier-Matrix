---
title:
  "KFM — data/work/_tmp Local Scratch (README)"
path:
  "data/work/_tmp/README.md"
version:
  "v1.0.0"
last_updated:
  "2025-12-17"
status:
  "draft"
doc_kind:
  "README"
license:
  "CC-BY-4.0"

markdown_protocol_version:
  "KFM-MDP v11.2.6"
mcp_version:
  "MCP-DL v6.3"
ontology_protocol_version:
  "KFM-ONTO v4.1.0"
pipeline_contract_version:
  "KFM-PPC v11.0.0"
stac_profile:
  "KFM-STAC v11.0.0"
dcat_profile:
  "KFM-DCAT v11.0.0"
prov_profile:
  "KFM-PROV v11.0.0"

governance_ref:
  "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref:
  "docs/governance/ETHICS.md"
sovereignty_policy:
  "docs/governance/SOVEREIGNTY.md"
fair_category:
  "FAIR+CARE"
care_label:
  "TBD"
sensitivity:
  "public"
classification:
  "open"
jurisdiction:
  "US-KS"

doc_uuid:
  "urn:kfm:doc:data:work:tmp:readme:v1.0.0"
semantic_document_id:
  "kfm-data-work-tmp-readme-v1.0.0"
event_source_id:
  "ledger:kfm:doc:data:work:tmp:readme:v1.0.0"
commit_sha:
  "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum:
  "sha256:<calculate-and-fill>"
---

# KFM `data/work/_tmp/` — Local Scratch (README)

## 📘 Overview

### Purpose
`data/work/_tmp/` is a **local-only scratch area** for temporary artifacts created while developing, debugging, or validating ETL steps.

It exists to keep “messy, throwaway” files out of:
- `data/raw/` (inputs / source drops)
- `data/work/` (structured, per-run staging intended to be reproducible)
- `data/processed/` (final outputs intended for ingestion + cataloging)

### Scope
| In Scope | Out of Scope |
|---|---|
| Local scratch outputs (quick exports, one-off subsets, ad-hoc joins) | Anything needed for reproducibility of a run (use run logs + structured work paths) |
| Caches (non-sensitive) | Secrets, tokens, credentials, private keys |
| Temporary downloads for investigation | Source-of-truth raw drops (use `data/raw/`) |
| Debug plots/snapshots used during development | Final datasets (use `data/processed/` and catalog them) |
| Experimental intermediate artifacts that should not be committed | Any artifact referenced by Story Nodes / Focus Mode evidence |

### Audience
- Contributors iterating on ETL code
- Maintainers doing validation/QA or debugging
- CI maintainers (to keep builds deterministic and clean)

### Definitions
- **Local scratch**: not durable, not reproducible, not guaranteed to exist
- **Promotion**: moving validated outputs to `data/processed/` (and then catalog/graph ingestion)
- **Run log**: an auditable record of how outputs were produced (belongs under `mcp/runs/` or repo-defined run path)

## 🗂️ Directory Layout

### Expected usage pattern
~~~text
🗂️ data/
├── 🧪 work/
│   ├── 📁 _tmp/
│   │   ├── 📄 README.md
│   │   ├── 🧹 cache/
│   │   ├── 🧷 scratch/
│   │   ├── 🧪 experiments/
│   │   └── 🧾 downloads/
│   └── 📁 <domain-or-pipeline>/
│       └── 📁 <run-id>/
└── 🏁 processed/
~~~

### Git hygiene and ignoring
This directory is intended to be **ignored** except for this README (and optionally a `.gitkeep`).

Recommended `.gitignore` snippet (place in repo root `.gitignore`, not here):
~~~gitignore
# Ignore everything in local scratch
data/work/_tmp/**

# Keep the directory and its documentation
!data/work/_tmp/
!data/work/_tmp/README.md
~~~

> If your repo uses a different ignore strategy (e.g., a `.gitignore` file inside this folder), apply the same rule: ignore all contents except `README.md`.

## ✅ Directory Contract

### What belongs here
- One-off “look at the data” outputs:
  - small CSV snippets
  - quick exports for sanity checks
  - temporary clipped rasters for inspection
- Local caches:
  - API response caches (non-sensitive)
  - downloaded tiles used for debugging (non-sensitive)
- Development-time scratch:
  - notebooks/notes (if your repo allows them)
  - temporary QA plots
  - diff artifacts

### What must NOT go here
- Anything required to reproduce an ETL run:
  - deterministic intermediates should live under structured `data/work/<domain>/<run-id>/...`
  - run metadata/logs should live under `mcp/runs/` (or your repo’s canonical run path)
- Any artifact that is “final”:
  - final outputs belong in `data/processed/` and must be validated + cataloged (STAC/DCAT/PROV as applicable)
- Any sensitive material:
  - precise culturally sensitive site coordinates
  - private/identifying information
  - credentials/secrets

## 🧭 Context

### Relationship to `data/work/`
- `data/work/` is the governed staging area for **structured** intermediates that support reproducibility.
- `data/work/_tmp/` is explicitly for **unstructured local scratch** that you should be willing to delete at any time.

### Retention / cleanup
- Treat `_tmp/` as disposable.
- Recommended practice:
  - remove contents regularly
  - never “depend” on `_tmp/` in code paths that run in CI
  - avoid checking `_tmp/` artifacts into PRs

## 🗺️ Diagrams

### Where `_tmp` fits in the overall flow
~~~mermaid
flowchart TD
  A["data/raw — inputs"] --> B["data/work — staging"]
  B --> C["data/processed — final outputs"]
  C --> D["data/stac — catalogs"]
  D --> E["Graph + APIs + UI"]

  X["data/work/_tmp — local scratch (ignored)"] -.-> B
~~~

## 🧠 Story Node & Focus Mode Integration

### Rule
- **Never** cite or reference `data/work/_tmp/` artifacts as evidence in Story Nodes / Focus Mode.
- Evidence must originate from promoted, validated, cataloged assets.

### Why
- `_tmp/` contents are not stable, not reproducible, and may contain unreviewed or sensitive material.

## 🧪 Validation & CI/CD

### CI expectations
- CI should not rely on `_tmp/` existing or containing anything.
- No pipeline code should write “required outputs” into `_tmp/`.

### Local developer workflow
- Use `_tmp/` to iterate quickly.
- When results stabilize:
  - move intermediates into structured `data/work/<domain>/<run-id>/...`
  - then promote validated outputs to `data/processed/`

## ⚖ FAIR+CARE & Governance

### Safety rules
- Do not store:
  - secrets/credentials
  - sensitive coordinates or culturally restricted locations
  - personal data
- If debugging requires sensitive material:
  - use redaction/generalization where possible
  - keep the artifacts off-repo (and off shared drives unless governed)

### Governance review triggers
- If anything from `_tmp/` is proposed for promotion or publication, it must go through the normal validation + governance gates.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-17 | Initial `data/work/_tmp/` README | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`


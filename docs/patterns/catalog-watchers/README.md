---
title: "🕵️ KFM — STAC/DCAT Watcher Pattern (Diff → Validate → SemVer → Governance PR)"
path: "docs/patterns/catalog-watchers/README.md"

version: "v11.2.6"
last_updated: "2025-12-13"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Catalog Board · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Pattern Pack"
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

intent: "catalog-watchers-diff-validate-semver-governance-pr"
audience:
  - "Catalog Engineering"
  - "Data Engineering"
  - "Graph + Provenance Engineering"
  - "Governance Reviewers"

---

<div align="center">

# 🕵️ **KFM — STAC/DCAT Watcher Pattern (Diff → Validate → SemVer → Governance PR)**
`docs/patterns/catalog-watchers/README.md`

**Purpose**  
Provide a **minimal, deterministic, CI-enforceable** pattern to detect upstream **STAC/DCAT** changes, validate them,
compute a reproducible **diff (RFC6902 JSON Patch)** with provenance, select a **SemVer bump**, and open a **governance PR**
that can be reviewed and merged safely.

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/STAC%2FDCAT%2FPROV-Aligned-brightgreen" />
<img src="https://img.shields.io/badge/Status-Stable%20%2F%20Governed-brightgreen" />

</div>

---

## 📘 Overview

This pattern defines a reproducible flow to:

1) Detect upstream catalog/object changes (S3/GCS object events, scheduled pulls, or GitHub webhooks).  
2) Validate **STAC** (PySTAC + stac-validator) and **DCAT** (SHACL).  
3) Compute a deterministic **RFC6902 JSON Patch** plus a provenance bundle.  
4) Select a SemVer bump (policy-driven).  
5) Open a governance PR containing the patch, validation results, and provenance manifest.

### Normative guarantees

- **Deterministic:** same inputs + same config ⇒ same diff artifacts and recommended SemVer bump.
- **Non-destructive:** watcher output is a PR proposal; it MUST NOT auto-merge governed catalogs.
- **Provenance-first:** every diff is accompanied by a provenance bundle and retrieval metadata.
- **Rights-aware:** merges are gated when license/rights/sensitivity labels change or conflict.

---

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 📁 patterns/
    ├── 📄 README.md                                  — Patterns index
    └── 📁 catalog-watchers/
        ├── 📄 README.md                              — This pattern pack
        ├── 📁 examples/                              — Optional: sample inputs/outputs for reviewers
        │   ├── 🧾 stac_before.json
        │   ├── 🧾 stac_after.json
        │   ├── 🧾 stac_patch.rfc6902.json
        │   ├── 🧾 dcat_before.jsonld
        │   ├── 🧾 dcat_after.jsonld
        │   ├── 🧾 dcat_patch.rfc6902.json
        │   ├── 🧾 prov_bundle.jsonld
        │   └── 🧾 watcher_run_manifest.json
        └── 📁 runbooks/
            ├── 📄 pr_review_checklist.md
            └── 📄 incident_notes.md

📁 mcp/
└── 📁 runs/
    └── 📁 catalog-watchers/                          — Run logs and reproducibility snapshots (per execution)
        └── 📁 <run_id>/
            ├── 🧾 inputs.json                        — Resolved source URIs + checksums/etags + timestamps
            ├── 🧾 outputs.json                       — Produced artifact list + hashes
            ├── 📄 validate.log                       — Validator output (STAC/DCAT/PROV)
            └── 🧾 diff_summary.json                  — Patch stats + semver decision

📁 tools/
└── 📁 catalog-watchers/                              — Optional: reference implementation (not required by this pattern)
    ├── 🐍 watcher.py                                 — Orchestrates: fetch → validate → diff → semver → PR bundle
    ├── 🐍 canonicalize.py                             — JSON canonicalization rules (stable key ordering + normalization)
    ├── 🐍 diff.py                                     — RFC6902 patch generation
    ├── 🐍 validate.py                                 — STAC/DCAT/PROV validators
    └── 🐍 pr_open.py                                  — PR assembler (no auto-merge)
~~~

---

## 🧭 Context

### The problem

Catalogs and metadata sources drift:

- upstream STAC Items/Collections can change assets, links, extents, or properties,
- DCAT datasets/distributions can change identifiers, license terms, or provenance fields,
- uncontrolled updates can break consumers and weaken governance guarantees.

### The goal

Turn uncontrolled catalog drift into a governed, reviewable, provenance-rich change proposal:

- **diff is explicit** (RFC6902 patch),
- **validity is proven** (validator logs),
- **impact is summarized** (SemVer recommendation),
- **review is enforceable** (governance PR with CI gates).

### Typical triggers (inputs)

- Object-store notification (S3/GCS): “catalog.json changed”
- Scheduled pull: “refresh remote catalog every N hours”
- GitHub webhook: “upstream repo pushed new STAC/DCAT JSON”
- Manual request: “watcher run for a specific dataset”

---

## 🧱 Architecture

### High-level stages

#### Stage 0 — Intake (resolve “old” and “new”)

- Identify `before` (previous governed artifact) and `after` (candidate upstream artifact).
- Record retrieval metadata for both:
  - source URI,
  - retrieved timestamp,
  - checksum and/or etag/version,
  - content-type.

#### Stage 1 — Normalize (canonicalize to reduce noise)

To avoid unstable diffs, canonicalize JSON prior to diff:

- sort object keys consistently,
- normalize whitespace and numeric formats where applicable,
- normalize ordering only when the target spec treats order as non-semantic (policy-controlled),
- preserve original copies for audit (raw `before` and raw `after` are retained).

#### Stage 2 — Validate (fail-fast)

- STAC:
  - structural validity (collection/item shape),
  - required fields and extensions,
  - link/asset schema checks.
- DCAT:
  - JSON-LD parse checks,
  - SHACL conformance against governed shapes,
  - required fields: identifiers, license, publisher, provenance.
- PROV:
  - bundle parse checks and required relations.

If validation fails, the run MUST emit a failure summary and MUST NOT open a “ready-to-merge” PR.

#### Stage 3 — Diff (RFC6902 JSON Patch)

- Produce `*.rfc6902.json` patch for each target:
  - `stac_patch.rfc6902.json`
  - `dcat_patch.rfc6902.json`
- Patch MUST be generated from canonicalized inputs (to keep diffs stable).

#### Stage 4 — SemVer decision (policy)

Compute a recommended SemVer bump based on change impact:

- **MAJOR**: identifier changes, schema shape changes, breaking property removals/renames,
  license changes, or rights/sensitivity escalation.
- **MINOR**: additive changes that are backward compatible (new items/assets/properties).
- **PATCH**: metadata-only changes that don’t affect consumer behavior (typos, description updates),
  and do not change rights/provenance semantics.

The SemVer decision MUST be reproducible from the diff summary + policy config.

#### Stage 5 — Governance PR assembly

Create a PR bundle that includes:

- patches (`*.rfc6902.json`),
- validation logs,
- provenance bundle,
- semver recommendation and reasoning (machine-readable),
- review checklist (human-readable).

---

## 📦 Data & Metadata

### Watcher run manifest (minimum)

A watcher run SHOULD emit a machine-readable manifest:

~~~json
{
  "run_id": "sha256:<truncated>",
  "started_at": "2025-12-13T00:00:00Z",
  "targets": [
    {
      "kind": "stac",
      "before_uri": "…",
      "after_uri": "…",
      "before_hash": "sha256:…",
      "after_hash": "sha256:…"
    },
    {
      "kind": "dcat",
      "before_uri": "…",
      "after_uri": "…",
      "before_hash": "sha256:…",
      "after_hash": "sha256:…"
    }
  ],
  "validation": {
    "stac": { "passed": true, "toolchain": ["pystac", "stac-validator"] },
    "dcat": { "passed": true, "toolchain": ["jsonld", "shacl"] },
    "prov": { "passed": true, "toolchain": ["jsonld", "kfm-prov-check"] }
  },
  "diff": {
    "patches": ["stac_patch.rfc6902.json", "dcat_patch.rfc6902.json"],
    "stats": { "ops_total": 12, "add": 7, "remove": 1, "replace": 4 }
  },
  "semver": {
    "recommended_bump": "MINOR",
    "reasons": ["added_stac_assets", "new_dcat_distribution"]
  }
}
~~~

### RFC6902 JSON Patch constraints (recommended)

- Prefer `add` / `replace` / `remove` operations only.
- Avoid non-deterministic paths (patch generation must be stable).
- For sensitive fields (license, rights, provenance), emit explicit patch ops and flag for review.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

Watcher changes MUST preserve:

- stable `id` semantics for Collections and Items,
- valid `links` and `assets` shapes,
- required KFM-STAC properties (where governed).

Recommended provenance fields in STAC Item/Collection properties:

- `kfm:watcher_run_id`
- `kfm:code_commit_sha`
- `kfm:algorithm_version`
- `prov:wasDerivedFrom` (references to before/after entities)

### DCAT

Watcher changes MUST preserve:

- stable `dct:identifier` semantics,
- `dct:license` and rights fields consistency,
- valid `dcat:distribution` entries with stable access URLs.

Recommended provenance fields in DCAT:

- `dct:provenance` summary referencing PROV bundle artifact
- `dct:modified` consistent with upstream change detection

### PROV-O (diff provenance)

A watcher run SHOULD describe:

- `prov:Activity` = watcher execution (diff/validate/assemble)
- `prov:Entity` for:
  - raw before artifact,
  - raw after artifact,
  - canonicalized before/after,
  - generated patch,
  - validation report bundle,
  - PR bundle artifact (if generated)
- relations:
  - `prov:used` (activity used before/after entities and validator configs)
  - `prov:wasGeneratedBy` (patch generated by watcher activity)
  - `prov:wasDerivedFrom` (patch derived from before/after)

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Trigger: event or schedule"] --> B["Fetch before and after"]
  B --> C["Canonicalize JSON"]
  C --> D["Validate STAC"]
  C --> E["Validate DCAT"]
  C --> F["Validate PROV"]
  D --> G["Generate RFC6902 patch"]
  E --> G
  F --> G
  G --> H["SemVer recommendation"]
  H --> I["Assemble governance PR bundle"]
  I --> J["Open PR - review required"]
~~~

---

## 🧠 Story Node & Focus Mode Integration

### Story Nodes (catalog change narratives)

Watcher outputs can be attached to Story Nodes as evidence for “what changed and why”:

- link to patch artifacts,
- link to validation reports,
- link to provenance bundle.

Story Nodes SHOULD distinguish:

- **fact**: patch operations and validated catalog state,
- **interpretation**: impact assessment (SemVer and downstream risk),
- **policy**: required approvals based on rights/sensitivity changes.

### Focus Mode constraints

Focus Mode MAY summarize diffs and validation results, but MUST NOT:

- invent governance approvals,
- infer license/rights changes not present in the diff,
- fabricate provenance relationships.

---

## 🧪 Validation & CI/CD

### CI checks (minimum)

Watcher PRs SHOULD trigger:

- `markdown-lint` (H1/H2 rules, fence profile rules)
- `schema-lint` (front-matter keys, required sections)
- `footer-check` (governance links present)
- `diagram-check` (Mermaid parse)
- `stac-validator` (STAC conformance)
- `shacl-validate` (DCAT JSON-LD conformance)
- `provenance-check` (PROV completeness and linkage)
- `secret-scan` and `pii-scan`

### Common failure causes (watcher-specific)

- diff produced from non-canonical JSON (noisy patch churn),
- invalid STAC links/assets after upstream reorganization,
- DCAT rights/license changes missing explicit review flags,
- patch touches identifiers without SemVer MAJOR recommendation.

---

## ⚖ FAIR+CARE & Governance

### Governance posture

- Watchers MUST open PRs; they MUST NOT auto-merge governed catalogs.
- PRs that include license/rights/sensitivity changes MUST be escalated for governance review.
- If a change introduces or surfaces stewardship constraints (e.g., Indigenous data policies),
  the watcher MUST mark the PR as “manual review required”.

### CARE protections (minimum)

- Do not publish sensitive locations or restricted knowledge via catalog diffs.
- If policy labels conflict between `before` and `after`, the watcher MUST:
  - flag the conflict,
  - recommend MAJOR (or block) depending on policy,
  - require manual review.

---

## 🕰️ Version History

| Version  | Date       | Notes |
|---------:|------------|------|
| v11.2.6  | 2025-12-13 | Initial governed watcher pattern pack (diff → validate → semver → governance PR). |

---

<div align="center">

🕵️ **KFM — STAC/DCAT Watcher Pattern (Diff → Validate → SemVer → Governance PR)**  
Catalog Integrity · Deterministic Diffs · Governed Change Control

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/Status-Stable%20%2F%20Governed-brightgreen" />

[📘 Docs Root](../../README.md) ·
[🗂️ Patterns Index](../README.md) ·
[🏛️ Governance Charter](../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC‑BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

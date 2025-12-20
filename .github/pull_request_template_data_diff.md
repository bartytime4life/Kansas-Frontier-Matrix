---
title: "🧩 KFM — Dataset Diff PR Template & Bot Playbook"
path: ".github/pull_request_template_data_diff.md"
version: "v12.0.0"
last_updated: "2025-12-20"
status: "active"
doc_kind: "Template + Playbook"
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

doc_uuid: "urn:kfm:doc:github:pr-template:data-diff:v12.0.0"
semantic_document_id: "kfm-github-pr-template-data-diff-v12.0.0"
event_source_id: "ledger:kfm:doc:github:pr-template:data-diff:v12.0.0"
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

# 🧩 KFM — Dataset Diff PR Template & Bot Playbook

## 📘 Overview

### Purpose
Deterministic, reproducible PR summary for dataset updates.

This file is both:
- A PR summary template (placeholders filled by CI/agent from structured artifacts)
- A bot playbook for producing, validating, and attaching review evidence

### Scope
| In Scope | Out of Scope |
|---|---|
| Dataset diff PR summaries from structured diff artifacts | Creating/altering governance policy |
| CI/agent rendering using deterministic inputs | Runtime API contract changes |
| Linking STAC/PROV + checksums for review | UI/Focus Mode feature changes |

### Audience
- Primary: Data-Ops reviewers, pipeline maintainers
- Secondary: Domain curators, FAIR+CARE reviewers

### Definitions
- Glossary: `docs/glossary.md` (if present)
- Terms used here: `dataset_key`, `diff.json`, STAC Item snippet, PROV snippet, checksum manifest

### Key artifacts
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This template + playbook | `.github/pull_request_template_data_diff.md` | Data-Ops | Rendered into PR body/comment |
| Diff artifact | `data/work/metadata/diff.json` | ETL | Machine-readable stats + links |
| STAC snippet | `data/work/metadata/stac_item.json` | Catalog | Minimal STAC Item JSON |
| PROV snippet | `data/work/metadata/prov.jsonld` | Catalog | Minimal PROV JSON-LD |
| Checksums manifest | `data/checksums/CHECKSUMS.txt` | Release | SHA256/SHA3 list |
| Optional workflow | `.github/workflows/data-diff-pr.yml` | CI/CD | Generates + posts summary |
| Optional renderer | `.github/actions/render_pr_body.py` | CI/CD | Deterministic placeholder replacement |

### Operational metadata
- Release stage: Stable / Governed
- Lifecycle: LTS
- Review cycle: Per-PR · Data-Ops & FAIR+CARE Council
- Content stability: stable

### How to use
1) Keep this file at `.github/pull_request_template_data_diff.md` (or copy to `.github/pull_request_template.md` if you want it as the default PR template).
2) Emit a machine-readable diff file during ETL, e.g. `data/work/metadata/diff.json`:
   - counts, feature class deltas
   - spatial footprint (bbox, CRS, area km², H3 stats)
   - QC outcomes (rules passed/failed, anomalies)
   - checksums & artifact URIs
   - STAC Item snippet (JSON)
   - PROV Activity/Entity/Agent snippet (JSON-LD)
3) Have CI render this template by substituting the placeholders below and post it into the PR (body or a tagged comment).

### Definition of done
- [ ] Front-matter complete + valid
- [ ] Placeholders are rendered from a single diff JSON + snippet files
- [ ] STAC/PROV snippets parse and validate
- [ ] Checksums and artifact bundle are accessible from CI
- [ ] QC failures triaged or waived with recorded rationale
- [ ] License & sovereignty constraints verified before merge

## 🗂️ Directory Layout

### This document
- `path`: `.github/pull_request_template_data_diff.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| GitHub templates/workflows | `.github/` | PR templates, CI workflows, action scripts |
| Work artifacts | `data/work/` | Deterministic intermediate outputs (diffs, snippets) |
| Processed outputs | `data/processed/` | Derived datasets (release candidates) |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | STAC/DCAT/PROV canonical outputs |
| Checksums | `data/checksums/` | Manifest used for reproducibility and supply-chain review |

### Expected file tree for this sub-area
~~~text
📁 .github/
├── 📄 pull_request_template_data_diff.md
├── 📁 workflows/
│   └── 📄 data-diff-pr.yml
└── 📁 actions/
    └── 📄 render_pr_body.py
📁 data/
├── 📁 checksums/
│   └── 📄 CHECKSUMS.txt
└── 📁 work/
    └── 📁 metadata/
        ├── 📄 diff.json
        ├── 📄 stac_item.json
        └── 📄 prov.jsonld
~~~

## 🧭 Context

### Background
Dataset updates in KFM require deterministic, reviewable summaries that:
- Describe what changed (counts, schema deltas, spatial footprint)
- Surface QC results and anomalies
- Provide provenance fragments (STAC + PROV) and reproducibility anchors (checksums, seed)

### Assumptions
- ETL emits a single machine-readable diff artifact per dataset update PR.
- Seeds are fixed for any nondeterministic steps and recorded in the diff artifact.
- Heavy artifacts (full diff tables, validation reports) are linked, not inlined.

### Constraints / invariants
- Canonical pipeline ordering is preserved: ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.
- The PR body must not require private data access to review; restricted data must be generalized/redacted per sovereignty policy.
- CI rendering must be deterministic (no network calls required to fill placeholders beyond artifact links).

### Open questions
| Question | Owner | Target date |
|---|---|---|
| How should multi-dataset PRs be summarized (one comment per dataset vs consolidated)? | TBD | TBD |
| What is the canonical diff JSON schema location under `schemas/`? | TBD | TBD |

### Future extensions
- Attach full diff tables and QC reports as STAC assets and link them in the PR body.
- Add an optional signed attestation bundle (SLSA provenance, SBOM pointers) to the artifact set.

## 🗺️ Diagrams

### Data-diff PR summary flow
~~~mermaid
flowchart LR
  A[ETL run] --> B[diff.json]
  B --> C[stac_item.json]
  B --> D[prov.jsonld]
  C --> E[Render PR body]
  D --> E
  E --> F[PR body or comment]
  F --> G[Review gates]
~~~

## 📦 Data & Metadata

### Inputs
These inputs are typically provided by CI (GitHub Actions) or an agent runner.

| Input | Type | Description |
|---|---|---|
| `KFM_DIFF_JSON` | path | Diff artifact (counts, schema deltas, spatial stats, QC, links) |
| `KFM_STAC_ITEM_JSON` | path | STAC Item snippet JSON |
| `KFM_PROV_JSONLD` | path | PROV JSON-LD snippet |
| `KFM_PREVIEW_TILES` | url list | MapLibre/Cesium tiles, PMTiles, XYZ |
| `KFM_CI_ARTIFACTS_URL` | url | CI run summary and artifact bundle |
| `KFM_CHECKSUMS_FILE` | path | SHA256/SHA3 manifest |
| `KFM_SEED` | string/int | Deterministic seed used in pipeline |
| `KFM_DATASET_KEY` | string | Canonical dataset key (e.g., `data/hydrology/usgs_streamflow`) |
| `KFM_RELEASE_TAG` | string | Intended data release tag |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| PR summary body | Markdown | PR body / PR comment | This template |
| Diff bundle | files | CI artifact | `diff.json` + snippets + checksums |

### Sensitivity & redaction
- If diffs contain restricted locations or culturally sensitive data, generalize/redact in emitted artifacts before rendering. See `sovereignty_policy` in front-matter.
- Avoid embedding raw PII in PR bodies; prefer links to restricted artifacts with access controls.

### Quality signals
- QC pass/fail counts and anomaly detector summaries must be present in the diff artifact.
- Schema/contract validation status must be explicit (pass/fail) with links to reports.

### PR Body template
This section is intended to be rendered and posted into the PR (body or comment).

#### Summary
- **Dataset:** {{KFM_DATASET_KEY}}
- **Release tag:** {{KFM_RELEASE_TAG}}
- **Pipeline seed:** `{{KFM_SEED}}`
- **Change type:** {{change_type}}  <!-- additions|updates|removals|mix -->
- **Reason / source window:** {{source_window_or_event}}

#### Diff stats
- **Total records (old → new):** {{old_count}} → {{new_count}} (Δ {{delta}})
- **Classes changed:** {{classes_changed}}
- **Fields changed:** {{fields_changed}}
- **Null/NaN deltas:** {{null_deltas}}
- **Duplicate resolutions:** {{dedup_count}} ({{method}})

#### Spatial footprint
- **CRS:** {{crs}}
- **BBox:** {{minx}}, {{miny}}, {{maxx}}, {{maxy}}
- **Area (~km²):** {{area_km2}}
- **H3 summary (r={{h3_res}}):** {{h3_cells}} cells; top deltas: {{top_h3_deltas}}
- **Geodetic checks:** {{geodetic_validations}}

#### QC outcomes
- **Rules passed:** {{qc_pass}} / {{qc_total}}
- **Rules failed:** {{qc_fail}} → see report
- **Anomalies flagged:** {{anomaly_count}} ({{detector}})
- **Schema/contract:** {{schema_version}} (✅/❌)
- **Data licensing & usage notes:** {{license_notes}} (FAIR+CARE reviewed: ✅/❌)

#### STAC snippet
~~~json
{{STAC_ITEM_JSON_SNIPPET}}
~~~

#### PROV snippet JSON-LD
~~~json
{{PROV_JSONLD_SNIPPET}}
~~~

#### Preview links
- **Web map / tiles:** {{KFM_PREVIEW_TILES}}
- **QC report:** {{qc_report_url}}
- **Diff table:** {{diff_table_url}}

#### Checksums and CI artifacts
- **Checksums file:** `{{KFM_CHECKSUMS_FILE}}`
- **CI run and artifacts:** {{KFM_CI_ARTIFACTS_URL}}

#### Governance and attestations
- **SLSA/attestations:** {{slsa_links}}
- **SBOM / manifests:** {{sbom_links}}
- **Energy/carbon telemetry:** {{telemetry_links}}
- **FAIR+CARE refs:** {{faircare_links}}

#### Reviewer checklist
- [ ] STAC/PROV snippets parse and validate
- [ ] QC failures triaged or waived with rationale
- [ ] License and sovereignty constraints verified
- [ ] Preview tiles render expected changes
- [ ] Checksums and artifact bundle accessible

### Expected diff JSON minimal schema
~~~json
{
  "dataset_key": "data/hydrology/usgs_streamflow",
  "release_tag": "2025.12.20",
  "seed": "123456",
  "change_type": "updates",
  "counts": { "old": 100000, "new": 101234, "delta": 1234 },
  "classes_changed": ["gauge_status", "county_fips"],
  "fields_changed": ["elev_m", "flow_cfs"],
  "null_deltas": { "flow_cfs": -42, "elev_m": 5 },
  "dedup": { "resolved": 37, "method": "station_id+time window" },
  "spatial": {
    "crs": "EPSG:4326",
    "bbox": [-102.1, 36.9, -94.6, 40.0],
    "area_km2": 213000,
    "h3_res": 6,
    "h3_cells": 1842,
    "top_h3_deltas": ["862a1072fffffff:+212", "862a10a3fffffff:-77"],
    "geodetic_checks": ["bbox_valid", "no_self_intersections"]
  },
  "qc": {
    "passed": 58,
    "failed": 2,
    "total": 60,
    "anomaly_count": 0,
    "detector": "TBD"
  },
  "schema_version": "kfm-hydro-v3.2",
  "license_notes": "CC-BY-4.0; sovereign constraints checked",
  "source_window": "USGS pulls 2025-12-19 to 2025-12-20",
  "links": {
    "qc_report": "https://example/qc.html",
    "diff_table": "s3://bucket/diffs/usgs_2025_12_20.parquet",
    "slsa": ["https://example/attest.json"],
    "sbom": ["docs/sbom/usgs_streamflow_2025_12_20.spdx.json"],
    "telemetry": ["docs/telemetry/runs/gh_12345.md"],
    "faircare": ["docs/governance/fair_care_hydro.md"]
  }
}
~~~

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- The PR body may include a minimal STAC Item snippet for quick review.
- Full STAC Items/Collections should live under `data/stac/items/` and `data/stac/collections/`.

### DCAT
- This PR summary does not inline DCAT records by default.
- If a dataset identifier changes (new dataset or major revision), link the DCAT record under `data/catalog/dcat/`.

### PROV-O
- The PR body includes a minimal PROV JSON-LD snippet for:
  - `prov:wasDerivedFrom` source identifiers
  - `prov:wasGeneratedBy` run/activity identifier
  - Agent identity for the pipeline runner (CI, service account, etc.)

### Versioning
- Dataset releases should link predecessor/successor (STAC versioning links where applicable).
- Diff artifacts should reference the intended `release_tag`.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| ETL diff generator | Produce `diff.json` deterministically | `tools/validation/diff.py` or equivalent |
| STAC emitter | Emit minimal STAC Item snippet | `tools/validation/stac_emit.py` |
| PROV emitter | Emit minimal PROV JSON-LD snippet | `tools/validation/prov_emit.py` |
| Renderer | Substitute placeholders into this template | `.github/actions/render_pr_body.py` |
| CI workflow | Run generators, upload artifacts, post PR comment | `.github/workflows/data-diff-pr.yml` |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Diff JSON schema | `schemas/` | Semver + changelog |
| STAC validation | STAC profile docs | Machine-validated |
| PROV validation | PROV profile docs | Machine-validated |

### LangGraph hook optional
~~~python
# Node consumes diff JSON and returns the rendered PR body string.
def render_pr_node(inputs):
    # inputs: paths/strings mirroring CI env
    ...
    return {"pr_body": rendered_markdown}
~~~

## 🧠 Story Node & Focus Mode Integration
- This artifact is an operational review surface, not a Story Node.
- It supports Focus Mode indirectly by enforcing provenance and QA upstream of catalog/graph ingestion.
- If a change impacts story-facing layers, ensure downstream story node updates remain provenance-linked.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] Diff JSON schema validation
- [ ] STAC snippet JSON parses and validates
- [ ] PROV snippet JSON-LD parses and validates
- [ ] Checksums manifest exists and matches produced artifacts
- [ ] Sovereignty/CARE checks pass or documented waiver exists

### GitHub Action bot minimal deterministic example
Create `.github/workflows/data-diff-pr.yml`:

~~~yaml
name: data-diff-pr
on:
  pull_request:
    types: [opened, synchronize, reopened]
    paths:
      - "data/**"
      - "src/pipelines/**"

jobs:
  summarize:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: write
      actions: read

    steps:
      - uses: actions/checkout@v4

      - name: Generate diff artifacts
        run: |
          python -m tools.validation.diff \
            --old data/work/processed@base \
            --new data/work/processed@head \
            --out data/work/metadata/diff.json \
            --seed "${{ github.run_id }}"

      - name: Build STAC and PROV snippets
        run: |
          python -m tools.validation.stac_emit \
            --diff data/work/metadata/diff.json \
            --out data/work/metadata/stac_item.json
          python -m tools.validation.prov_emit \
            --diff data/work/metadata/diff.json \
            --out data/work/metadata/prov.jsonld

      - name: Render PR body
        run: |
          python .github/actions/render_pr_body.py \
            --template .github/pull_request_template_data_diff.md \
            --diff data/work/metadata/diff.json \
            --stac data/work/metadata/stac_item.json \
            --prov data/work/metadata/prov.jsonld \
            --checksums data/checksums/CHECKSUMS.txt \
            --tiles "$(cat data/work/metadata/preview_tiles.url 2>/dev/null || echo '')" \
            > pr_body.md

      - name: Upload artifacts
        uses: actions/upload-artifact@v4
        with:
          name: data-diff-bundle
          path: |
            data/work/metadata/diff.json
            data/work/metadata/stac_item.json
            data/work/metadata/prov.jsonld
            data/checksums/CHECKSUMS.txt
            pr_body.md

      - name: Comment or update PR
        uses: thollander/actions-comment-pull-request@v3
        with:
          message: |
            <!-- kfm-data-diff-bot -->
            $(cat pr_body.md)
          comment-tag: kfm-data-diff-bot
~~~

### Helper renderer script sketch
Create `.github/actions/render_pr_body.py`:

~~~python
import json
import os
import sys

def load(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

tpl = load(sys.argv[sys.argv.index("--template") + 1])
diff = json.loads(load(sys.argv[sys.argv.index("--diff") + 1]))
stac = json.loads(load(sys.argv[sys.argv.index("--stac") + 1]))
prov = json.loads(load(sys.argv[sys.argv.index("--prov") + 1]))

checksums = os.environ.get("KFM_CHECKSUMS_FILE") or sys.argv[sys.argv.index("--checksums") + 1]
tiles = os.environ.get("KFM_PREVIEW_TILES") or sys.argv[sys.argv.index("--tiles") + 1]
ci_artifacts_url = os.environ.get("KFM_CI_ARTIFACTS_URL") or diff.get("links", {}).get("ci_artifacts", "")

fields = {
  "KFM_DATASET_KEY": diff.get("dataset_key", ""),
  "KFM_RELEASE_TAG": diff.get("release_tag", ""),
  "KFM_SEED": diff.get("seed", ""),
  "change_type": diff.get("change_type", ""),
  "old_count": diff.get("counts", {}).get("old", 0),
  "new_count": diff.get("counts", {}).get("new", 0),
  "delta": diff.get("counts", {}).get("delta", 0),
  "classes_changed": ", ".join(diff.get("classes_changed", [])),
  "fields_changed": ", ".join(diff.get("fields_changed", [])),
  "null_deltas": diff.get("null_deltas", ""),
  "dedup_count": diff.get("dedup", {}).get("resolved", 0),
  "method": diff.get("dedup", {}).get("method", ""),
  "crs": diff.get("spatial", {}).get("crs", ""),
  "minx": diff.get("spatial", {}).get("bbox", [None, None, None, None])[0],
  "miny": diff.get("spatial", {}).get("bbox", [None, None, None, None])[1],
  "maxx": diff.get("spatial", {}).get("bbox", [None, None, None, None])[2],
  "maxy": diff.get("spatial", {}).get("bbox", [None, None, None, None])[3],
  "area_km2": diff.get("spatial", {}).get("area_km2", ""),
  "h3_res": diff.get("spatial", {}).get("h3_res", ""),
  "h3_cells": diff.get("spatial", {}).get("h3_cells", ""),
  "top_h3_deltas": ", ".join(diff.get("spatial", {}).get("top_h3_deltas", [])),
  "geodetic_validations": ", ".join(diff.get("spatial", {}).get("geodetic_checks", [])),
  "qc_pass": diff.get("qc", {}).get("passed", 0),
  "qc_total": diff.get("qc", {}).get("total", 0),
  "qc_fail": diff.get("qc", {}).get("failed", 0),
  "anomaly_count": diff.get("qc", {}).get("anomaly_count", ""),
  "detector": diff.get("qc", {}).get("detector", ""),
  "schema_version": diff.get("schema_version", ""),
  "license_notes": diff.get("license_notes", ""),
  "qc_report_url": diff.get("links", {}).get("qc_report", ""),
  "diff_table_url": diff.get("links", {}).get("diff_table", ""),
  "slsa_links": ", ".join(diff.get("links", {}).get("slsa", [])),
  "sbom_links": ", ".join(diff.get("links", {}).get("sbom", [])),
  "telemetry_links": ", ".join(diff.get("links", {}).get("telemetry", [])),
  "faircare_links": ", ".join(diff.get("links", {}).get("faircare", [])),
  "STAC_ITEM_JSON_SNIPPET": json.dumps(stac, ensure_ascii=False, indent=2),
  "PROV_JSONLD_SNIPPET": json.dumps(prov, ensure_ascii=False, indent=2),
  "KFM_CHECKSUMS_FILE": checksums,
  "KFM_PREVIEW_TILES": tiles,
  "KFM_CI_ARTIFACTS_URL": ci_artifacts_url,
  "source_window_or_event": diff.get("source_window", ""),
}

out = tpl
for k, v in fields.items():
    out = out.replace("{{" + k + "}}", str(v))

print(out)
~~~

### Reproduction
~~~bash
# Example only — replace with repo-specific commands.
# 1) Generate diff artifacts
# 2) Validate schemas (STAC/DCAT/PROV)
# 3) Produce checksums
# 4) Render PR body
~~~

### Telemetry signals
| Signal | Source | Where recorded |
|---|---|---|
| CI run URL | GitHub Actions | `docs/telemetry/` (optional) |
| Energy/carbon telemetry | Runner tooling | `docs/telemetry/` (optional) |

## ⚖ FAIR+CARE & Governance

### Review gates
- Block merge if:
  - QC failures are un-waived
  - STAC/PROV snippets fail validation
  - License/sovereignty constraints are unresolved
  - Checksums manifest or artifact bundle is missing

### CARE / sovereignty considerations
- Apply redaction/generalization rules to restricted locations and culturally sensitive materials.
- Record any waivers with rationale and reviewer identity.

### AI usage constraints
- CI/agents may summarize and structure-extract.
- CI/agents must not generate policy or infer sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v12.0.0 | 2025-12-20 | Rebuilt into v12 governed doc structure; aligned profile refs; converted inner code fences to `~~~`. | TBD |
| v11.2.6 | 2025-12-20 | Prior template/playbook format. | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

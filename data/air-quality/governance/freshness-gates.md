---
title: "Air Quality — Freshness Gates"
path: "data/air-quality/governance/freshness-gates.md"
version: "v1.0.0"
last_updated: "2025-12-17"
status: "draft"
doc_kind: "Governance"
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

doc_uuid: "urn:kfm:doc:data:air-quality:freshness-gates:v1.0.0"
semantic_document_id: "kfm-air-quality-freshness-gates-v1.0.0"
event_source_id: "ledger:kfm:doc:data:air-quality:freshness-gates:v1.0.0"
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

# Air Quality — Freshness Gates

## 📘 Overview

### Purpose
This document defines **freshness expectations** and **enforcement gates** for the Air Quality data domain (`data/air-quality/`). These gates prevent stale datasets and stale derivatives from entering the KFM catalog/graph/UI surface area without explicit disclosure, exception handling, and provenance.

This governs:
- How “freshness” is measured for each air-quality dataset/product.
- What constitutes **warn** vs **fail** in CI for staleness.
- How to record and approve **time-bounded exceptions**.
- Minimum metadata required so Focus Mode and map layers can show **“as of”** dates.

### Scope
| In Scope | Out of Scope |
|---|---|
| Freshness rules for `data/air-quality/**` artifacts | Medical/public-health guidance derived from air quality values |
| CI checks that evaluate staleness from STAC/DCAT/PROV + processed outputs | Real-time alerting / paging / SRE on-call processes |
| Exception mechanism (expiry + approver + rationale) | Rewriting upstream provider cadences or policies |
| “As-of” disclosure requirements for UI/Focus Mode surfaces | Non-air-quality domains outside `data/air-quality/` |

### Audience
- Primary: Data/pipeline maintainers, CI owners, domain contributors
- Secondary: Reviewers, story node authors, UI layer owners

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Freshness anchor**: The timestamp used to evaluate staleness (e.g., coverage end datetime).
  - **Coverage end**: The end of the time period represented by a dataset snapshot.
  - **Staleness window**: Maximum allowed age of the anchor relative to “now” before warn/fail.
  - **Gate**: A CI-enforced check that yields pass/warn/fail.
  - **Exception**: A documented and time-bounded waiver to allow stale artifacts for a defined reason.
  - **As-of disclosure**: UI/Focus surfaces show the effective “data current through” timestamp.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Governance hub | `data/air-quality/governance/README.md` | TBD | Entry point for domain governance |
| Data classification | `data/air-quality/governance/DATA_CLASSIFICATION.md` | TBD | Sensitivity + release posture |
| Sources & licenses | `data/air-quality/governance/SOURCES_AND_LICENSES.md` | TBD | Authoritative source + license inventory |
| Freshness gates (this doc) | `data/air-quality/governance/freshness-gates.md` | TBD | Gate policy + required metadata |
| Pipeline contract (global) | `docs/MASTER_GUIDE_v12.md` | Maintainers | Canonical ordering + minimum CI gates |
| Root governance | `docs/governance/ROOT_GOVERNANCE.md` | Governance | Governance references + escalation |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] All claims link to datasets / schemas / tickets / commits (as applicable)
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `data/air-quality/governance/freshness-gates.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Air quality domain | `data/air-quality/` | Raw/work/processed/stac outputs for air-quality domain |
| Air quality governance | `data/air-quality/governance/` | Domain-level governance docs and policies |
| Data domains | `data/` | Raw/work/processed/stac outputs per domain |
| Documentation | `docs/` | Canonical governed docs (system-wide) |
| Graph | `src/graph/` | Graph build + ontology bindings |
| Pipelines | `src/pipelines/` | ETL + catalogs + transforms |
| Schemas | `schemas/` | JSON schemas + telemetry schemas |
| Frontend | `web/` | React + map clients |
| MCP | `mcp/` | Experiments, model cards, SOPs |

### Expected file tree for this sub-area
~~~text
data/
└── 📁 air-quality/
    ├── 📁 raw/
    ├── 📁 work/
    ├── 📁 processed/
    ├── 📁 stac/
    │   ├── 📁 collections/
    │   └── 📁 items/
    └── 📁 governance/
        ├── 📄 README.md
        ├── 📄 DATA_CLASSIFICATION.md
        ├── 📄 SOURCES_AND_LICENSES.md
        └── 📄 freshness-gates.md
~~~

## 🧭 Context

### Background
Air-quality layers and narratives can become misleading if the underlying data (or derived products) are stale. Because KFM can present environmental and time-sensitive information in map layers and Focus Mode contexts, the system must:
- Detect staleness deterministically, and
- Prevent stale content from being published without explicit disclosure or approval.

This document establishes **freshness gates** that apply at the ETL/catalog boundary and within CI.

### Assumptions
- Time comparisons use **UTC** unless a dataset explicitly defines a different time basis.
- Each dataset has a declared **freshness class** (based on expected update cadence).
- Freshness is evaluated against a canonical “now” at validation time (CI run time).
- Freshness evaluation prefers **coverage end** (what time the data represents) over file timestamps.

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode is preserved.
- Frontend consumes contracts via APIs (no direct graph dependency).
- Provenance is first-class: freshness decisions must be explainable via catalog/provenance metadata.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Where will the machine-readable freshness policy live (YAML/JSON), if introduced? | TBD | TBD |
| Which air-quality sources are included in this domain (authoritative list)? | TBD | TBD |
| Which sources require exceptions due to known cadence delays? | TBD | TBD |
| UI standard for “as-of” display + stale warnings (exact copy + UX)? | TBD | TBD |

### Future extensions
- Extension point A: Add a machine-readable policy file (e.g., `freshness-policy.yaml`) and a CI job that emits a structured report artifact.
- Extension point B: Add telemetry signals for freshness drift and exception usage over time.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[ETL + Normalization] --> G[Freshness Gate]
  G --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React/Map UI]
  E --> F[Story Nodes]
  F --> H[Focus Mode]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
 participant Dev as Contributor
 participant Repo as Repo/PR
 participant CI as CI
 participant Gate as Freshness Gate
 participant Cat as STAC/DCAT/PROV

 Dev->>Repo: PR updates air-quality artifacts
 Repo->>CI: Trigger workflow
 CI->>Cat: Validate catalogs + provenance
 CI->>Gate: Compute staleness vs thresholds
 Gate-->>CI: PASS / WARN / FAIL + report
 CI-->>Dev: Status checks + links to results
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| STAC Collections + Items | JSON | `data/air-quality/stac/**` | STAC schema validation |
| DCAT dataset views (if present) | JSON/RDF | domain catalog outputs | DCAT profile validation |
| PROV bundles / logs (if present) | JSON/RDF | domain provenance outputs | PROV profile validation |
| Processed outputs metadata | file + metadata | `data/air-quality/processed/**` | path existence + optional schema checks |
| Governance source inventory | Markdown | `data/air-quality/governance/SOURCES_AND_LICENSES.md` | reviewer check (manual) |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Freshness gate result | CI status | CI | Must be deterministic + reproducible |
| Freshness report (recommended) | JSON | CI artifact (recommended) | Schema (TBD / not confirmed in repo) |
| Exception register (recommended) | YAML/JSON | `data/air-quality/governance/` | Schema (TBD / not confirmed in repo) |

### Sensitivity & redaction
- Air-quality datasets are typically public; however, **do not infer sensitive locations** from privately-operated sensors or non-public station metadata.
- If any dataset includes private or restricted coordinates, apply generalization/redaction per `docs/governance/SOVEREIGNTY.md` and `data/air-quality/governance/DATA_CLASSIFICATION.md`.

### Quality signals
Freshness gates are one quality axis. Additional recommended signals for air-quality products:
- Coverage continuity (no unexpected gaps for a “daily” dataset)
- Range sanity checks for numeric measures (domain-specific; defined elsewhere)
- Station/geometry validity for spatialized assets (if applicable)

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections involved: Air-quality domain collections (TBD; define per dataset).
- Items involved: Snapshot/time-slice items (TBD; define per dataset).
- Extension(s): Use only approved extensions; any new, domain-specific extension requires schema/ontology review.

**Freshness anchor rules (preferred order):**
1. `properties.end_datetime` (preferred for time-series coverage)
2. `properties.datetime` (for snapshot items)
3. If neither exists: gate must fail (missing required temporal metadata), unless an explicit exception exists.

### DCAT
- Dataset identifiers: Must map to stable domain dataset IDs (TBD; define per dataset).
- License mapping: Must match `SOURCES_AND_LICENSES.md`.
- Contact / publisher mapping: Must reflect upstream source/publisher as applicable.

**Freshness mapping (recommended if DCAT views exist):**
- `dcterms:modified` represents last update time of the dataset distribution/view.
- `dcterms:accrualPeriodicity` encodes expected cadence (align with freshness class).

### PROV-O
- `prov:wasDerivedFrom`: Link processed outputs and catalog artifacts to upstream source entities.
- `prov:wasGeneratedBy`: Link STAC/DCAT/PROV outputs to ETL activities.
- Activity / Agent identities: Each refresh run is a PROV Activity with timestamps and a responsible Agent.

**Freshness and PROV**
- Gate outcomes should be explainable via PROV: what ran, when it ran, and what “coverage end” the outputs represent.

### Versioning
- Use STAC Versioning links and graph predecessor/successor relationships as applicable.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| Freshness policy | Declares cadence + thresholds + enforcement level | Governance doc + (optional) YAML/JSON policy |
| Freshness gate | Computes staleness and enforces warn/fail | CI job + report artifact |
| ETL | Ingest + normalize | Config + run logs |
| Catalogs | STAC/DCAT/PROV | JSON + validator |
| Graph | Neo4j | Cypher + API layer |
| APIs | Serve contracts | REST/GraphQL |
| UI | Map + narrative | API calls |
| Story Nodes | Curated narrative | Graph + docs |
| Focus Mode | Contextual synthesis | Provenance-linked |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog |
| API schemas | `src/server/` + docs | Contract tests required |
| Layer registry | `web/cesium/layers/regions.json` | Schema-validated |

### Extension points checklist (for future work)
- [ ] Data: new domain added under `data/<domain>/...`
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Air-quality layers and narratives must display **as-of** timestamps derived from the freshness anchor.
- Focus Mode should surface:
  - The dataset ID(s) used
  - The coverage window (start/end when applicable)
  - The freshness status (current / warning / stale) when available

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID.

### Optional structured controls
~~~yaml
focus_layers:
 - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV)
- [ ] Graph integrity checks (if air-quality data is loaded into graph in this change)
- [ ] API contract tests (if endpoints are affected)
- [ ] UI schema checks (layer registry) (if new/updated air-quality layers are added)
- [ ] Security and sovereignty checks (as applicable)
- [ ] **Freshness gate checks** (this document)

### Freshness gate policy (normative)

#### 1) Freshness anchors
Every dataset governed by this domain MUST declare (or be representable with) one of:
- **Coverage end** timestamp (preferred): `end_datetime`
- **Snapshot** timestamp: `datetime`

If a dataset cannot supply either, it is **non-compliant** unless explicitly waived.

#### 2) Freshness classes
Freshness is managed by class to avoid hardcoding per-source logic into CI.

| Freshness class | Intended for | Warn after | Fail after |
|---|---|---:|---:|
| `realtime` | Streaming/near-real-time feeds | 3 hours | 6 hours |
| `hourly` | Hourly-updated feeds | 6 hours | 12 hours |
| `daily` | Daily refresh products | 2 days | 4 days |
| `weekly` | Weekly refresh products | 10 days | 21 days |
| `monthly` | Monthly refresh products | 45 days | 60 days |
| `quarterly` | Quarterly refresh products | 120 days | 150 days |
| `annual` | Annual refresh products | 400 days | 500 days |

Notes:
- Thresholds are defaults. Dataset-specific overrides are allowed only with explicit documentation and review.
- “Warn” should not block merges by default; “Fail” should block merges (unless exception applies).

#### 3) Enforcement levels
Each dataset must select an enforcement level:
- `hard_fail`: staleness beyond fail threshold blocks merge
- `soft_fail`: staleness beyond fail threshold warns (used only for non-critical layers)
- `report_only`: gate emits report but does not fail (use sparingly; requires justification)

#### 4) Required disclosure for UI/Focus Mode
If a dataset is in `WARN` state but allowed through (e.g., non-blocking), UI/Focus Mode MUST:
- Display the **as-of** timestamp, and
- Indicate the freshness state (e.g., “Data may be stale”).

#### 5) Exceptions (waivers)
Exceptions are allowed only when:
- There is a documented upstream outage/cadence delay, or
- The dataset is intentionally frozen for historical reproduction, or
- A governance decision approves a non-standard cadence.

Exception requirements:
- Must include a reason, approver, and expiry date.
- Must be time-bounded (no open-ended exceptions).
- Must link to an issue/ticket or governance record (identifier only; no requirement to embed URLs in Markdown).

### Optional structured policy (recommended)
If/when a machine-readable policy file is introduced, use a structure like:

~~~yaml
# NOTE: Example structure only; path/filename not confirmed in repo.

freshness_defaults:
  realtime:   { warn_after: "PT3H",   fail_after: "PT6H" }
  hourly:     { warn_after: "PT6H",   fail_after: "PT12H" }
  daily:      { warn_after: "P2D",    fail_after: "P4D" }
  weekly:     { warn_after: "P10D",   fail_after: "P21D" }
  monthly:    { warn_after: "P45D",   fail_after: "P60D" }
  quarterly:  { warn_after: "P120D",  fail_after: "P150D" }
  annual:     { warn_after: "P400D",  fail_after: "P500D" }

datasets:
  - dataset_id: "kfm-air-quality-<dataset>"
    freshness_class: "daily"
    anchor: "stac_end_datetime"     # stac_end_datetime | stac_datetime
    enforcement: "hard_fail"
    required_catalogs: ["stac", "prov"]  # add "dcat" if DCAT views exist

exceptions:
  - dataset_id: "kfm-air-quality-<dataset>"
    reason: "Upstream cadence delay"
    approved_by: "<name-or-role>"
    expires: "2026-01-15"
    ticket: "<issue-id-or-governance-record-id>"
~~~

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands.
# These commands are NOT confirmed in repo; they document intent.

# 1) validate domain catalogs
# <stac-validate> data/air-quality/stac/
# <dcat-validate> data/air-quality/dcat/          # if present
# <prov-validate> data/air-quality/prov/          # if present

# 2) run freshness gate
# <freshness-gate-cli> --domain air-quality --policy data/air-quality/governance/<policy-file>

# 3) run doc lint / markdown protocol checks
# <mdp-lint> data/air-quality/governance/freshness-gates.md
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| `air_quality_freshness_age_seconds` | Freshness gate | `docs/telemetry/` + `schemas/telemetry/` |
| `air_quality_freshness_state` (PASS/WARN/FAIL) | Freshness gate | `docs/telemetry/` + `schemas/telemetry/` |
| `air_quality_freshness_exception_count` | Exception registry | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates
- Freshness threshold changes: maintainer review required.
- New dataset additions (new freshness class assignment): maintainer + governance review recommended.
- Any exceptions longer than one release cycle: governance review recommended.
- Any change that affects public-facing UI messaging: UI owner + governance review recommended.

(Approver roles are **not confirmed in repo**; align with `docs/governance/ROOT_GOVERNANCE.md`.)

### CARE / sovereignty considerations
- Air-quality data may intersect with sovereign/tribal jurisdictions or culturally sensitive areas.
- Do not use air-quality sensor metadata to infer sensitive site locations.
- Apply redaction/generalization rules when a source is not explicitly public, per sovereignty policy.

### AI usage constraints
- Ensure this document’s AI permissions/prohibitions match intended use.
- Do not use AI transformations to infer or reconstruct restricted locations from “nearby” public measurements.

## 🕰️ Version History
| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-17 | Initial draft freshness gates for air-quality domain | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

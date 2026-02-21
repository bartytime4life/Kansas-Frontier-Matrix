# Kansas Frontier Matrix (KFM)

> **Map-first • Time-aware • Governed • Evidence-first • Cite-or-abstain**  
> **Core posture:** default-deny • fail-closed • reproducible by digest • policy enforced in CI + runtime

**Status:** vNext (blueprint-driven build)  
**Core promise:** anything you can see, cite, export, or ask KFM to explain is traceable to an immutable **DatasetVersion** + resolvable **EvidenceBundle**, with **policy enforced consistently in CI and at runtime**.  
**Primary experiences:** **Map Explorer** + **Timeline** + **Stories** + **Catalog** + **Focus Mode**.

[![Status](https://img.shields.io/badge/status-vNext-blue)](#)
[![Governance](https://img.shields.io/badge/governance-fail--closed-critical)](#)
[![Evidence](https://img.shields.io/badge/evidence-cite--or--abstain-important)](#)
[![Policy](https://img.shields.io/badge/policy-default--deny-critical)](#)
[![License](https://img.shields.io/badge/license-TBD-lightgrey)](#)

---

## Quick navigation

[What this repo is](#what-this-repo-is) •
[Quick start](#quick-start) •
[System overview](#system-overview) •
[Core invariants](#core-invariants) •
[Key concepts and glossary](#key-concepts-and-glossary) •
[Architecture](#architecture) •
[Truth path and promotion contract](#truth-path-and-promotion-contract) •
[Deterministic identity and versioning](#deterministic-identity-and-versioning) •
[Catalog triplet and profiles](#catalog-triplet-and-profiles) •
[Evidence and citations](#evidence-and-citations) •
[Map and story UX](#map-and-story-ux) •
[Focus Mode AI](#focus-mode-ai) •
[Governance](#governance) •
[Datasets and sources](#datasets-and-sources) •
[Repository layout](#repository-layout) •
[Contributing](#contributing) •
[Security](#security) •
[Roadmap](#roadmap) •
[References](#references)

---

## What this repo is

KFM is a governed knowledge system where the **map + timeline** are the primary interface. The system is trustworthy because every user-visible claim is grounded in:

- immutable **DatasetVersions** (digest-addressed)
- policy-evaluated, resolvable **EvidenceBundles**
- reproducible **run receipts** + append-only **audit logging**
- strict catalogs (**DCAT + STAC + PROV**) that form the “anti-hallucination substrate”

KFM is also a **system of governed artifacts**:

- **Data artifacts** (raw/work/quarantine/processed) and their catalogs
- **Docs and narratives** (Story Nodes, ADRs, runbooks) with policy labels
- **Contracts** (OpenAPI, schemas, catalog profiles) enforced in CI
- **Policy-as-code** (default deny) enforced in CI + runtime

> **NOTE**  
> This README describes the **target operating model** for vNext. If some files/directories are not present on your branch, treat those sections as **PROPOSED conventions** and adjust to repo reality.

[↑ Back to top](#kansas-frontier-matrix-kfm)

---

## Quick start

> **NOTE**  
> This repository’s exact commands / package managers / service topology may vary by branch.  
> Prefer `make help` or `scripts/dev/*` if present.

### 1) Get oriented

~~~bash
# clone
git clone <REPO_URL>
cd Kansas-Frontier-Matrix

# discover the repo entrypoints
ls
~~~

### 2) Try the “common entrypoints” (if present)

~~~bash
# if a Makefile exists
make help

# if it’s a Node/TypeScript monorepo
node -v
npm -v
npm install
npm test

# if it’s a Python workspace
python --version
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
~~~

### 3) First principle while exploring

> **Rule of thumb:** if a thing is user-visible, it must be **promotable** and **citeable**.  
> If it cannot be cataloged and cited, it does not belong on the map.

[↑ Back to top](#kansas-frontier-matrix-kfm)

---

## System overview

KFM is “map-first,” but the map is only as trustworthy as the lifecycle behind it.

### High-level flow

~~~mermaid
flowchart LR
  A[Upstream sources] --> B[Connectors and pipeline runner]
  B --> C[RAW zone]
  C --> D[WORK and QUARANTINE]
  D --> E[PROCESSED zone]
  E --> F[Catalog triplet DCAT STAC PROV + run receipts]
  F --> G[Rebuildable projections DB Search Graph Tiles]
  F --> H[Governed API + policy engine + evidence resolver]
  G --> H
  H --> I[UI Map Explorer Timeline Stories Focus]
  H --> J[Exports and reports]
  H --> K[Append-only audit ledger]
~~~

### “Trust membrane” (enforcement boundary)

- **Clients MUST NOT** access object storage / DB directly.
- Access flows through a **governed API** that applies **policy**, **evidence resolution**, **redaction obligations**, and **audit logging** consistently.
- Backend domain logic **MUST NOT** bypass repository interfaces to talk directly to infrastructure.

### Canonical vs rebuildable (always keep straight)

- **Canonical:** processed artifacts in object storage, catalogs (DCAT/STAC/PROV), run receipts, and audit ledger.
- **Rebuildable projections:** PostGIS tables, search indexes, graph views, and tile bundles.

> **Rule:** if a projection and a catalog disagree, the catalog + processed artifacts win.

[↑ Back to top](#kansas-frontier-matrix-kfm)

---

## Core invariants

These are KFM’s “non-negotiables.” If we violate them, we don’t merely have bugs—we break governance.

### Invariants (what must always be true)

| Invariant | Meaning | How it’s enforced |
|---|---|---|
| **Truth path** | Data moves through zones (Raw → Work/Quarantine → Processed → Catalog → Published) with promotion gates | Promotion Contract gates (CI + pipeline) |
| **Trust membrane** | No direct client-to-storage/DB; domain logic never bypasses interfaces | Network controls + code structure + tests |
| **Evidence-first UX** | Evidence is not optional “details”—it’s a primary interaction everywhere | Evidence Drawer required + UI gating |
| **Cite-or-abstain Focus Mode** | If citations cannot be verified, Focus Mode abstains | Citation verification hard gate + eval harness |
| **Canonical vs rebuildable** | Object storage + catalogs + audit ledger are canonical; DB/search/tiles are projections | Rebuild scripts + “source of truth” discipline |
| **Deterministic identity** | DatasetVersion IDs and artifact addresses are stable and digest-based | Canonical hashing + “hash drift” checks |
| **Row-level traceability** | Every feature row in projections carries `dataset_version_id` + an `evidence_ref` | Projection schema + integration tests |
| **Policy-safe errors** | Public users must not infer restricted dataset existence via error differences | API error model + tests + monitoring |

> **Norms used in docs:** MUST / MUST NOT / SHOULD / MAY (RFC-style).  
> **Section tags:** CONFIRMED / PROPOSED / UNKNOWN (repository + governance dependent).

[↑ Back to top](#kansas-frontier-matrix-kfm)

---

## Key concepts and glossary

Use these terms consistently in code, schemas, tests, and documentation.

| Term | Definition (KFM meaning) |
|---|---|
| **Dataset** | A logical dataset identity (e.g., “NOAA Storm Events”) |
| **DatasetVersion** | An immutable version corresponding to a specific promoted output set |
| **Spec hash (spec_hash)** | Deterministic hash derived from canonical dataset spec; used to identify versions |
| **Artifact** | A concrete file/object produced by a run (GeoParquet, PMTiles, COG, JSONL, PDF…) |
| **EvidenceRef** | A stable reference to evidence using explicit schemes (dcat://, stac://, prov://, doc://, graph://, url://) |
| **EvidenceBundle** | Resolved evidence view returned by the evidence resolver (human card + machine metadata + digests + policy results) |
| **Policy label** | Primary sensitivity/access input used in authorization and obligations |
| **Obligation** | A required transformation or UX notice (e.g., geometry generalized; suppress export; show notice) |
| **Run receipt** | Immutable record of an operation (pipeline run / Focus query / publish event) with environment capture |
| **Audit ledger** | Append-only governed record of operations and approvals |
| **Quarantine** | Zone/state for artifacts that cannot be promoted (validation, rights, sensitivity issues) |
| **Valid time** | The time period when an assertion is true (e.g., a boundary exists) |
| **Transaction time** | The time when KFM recorded/published data (system time) |
| **Story Node** | Versioned narrative bound to map state + citations + policy label + review state |

[↑ Back to top](#kansas-frontier-matrix-kfm)

---

## Architecture

KFM keeps layers clean and enforces governance at boundaries.

### Clean layering (invariant)

- **Domain**: pure domain models and rules
- **Use cases**: workflows (ingest dataset, promote dataset version, publish story node, answer focus query)
- **Interfaces**: contracts (OpenAPI DTOs, schema registries, policy adapters, repository interfaces)
- **Infrastructure**: PostGIS, search, graph, object storage, CI, deployment

### Component decomposition (recommended build plan)

Start with a **modular monolith** so invariants are easier to enforce and test; split into services only when scaling/isolation demands it.

Core components:

1. **Pipeline runner + connectors** (acquire, snapshot, normalize, validate, write artifacts)
2. **Catalog generator** (DCAT/STAC/PROV + run receipts + profile validation + cross-link enforcement)
3. **Policy engine** (policy-as-code; same semantics in CI and runtime)
4. **Evidence resolver** (EvidenceRef → EvidenceBundle; policy + obligations applied; fail-closed)
5. **Governed API** (dataset discovery, queries, tiles, stories, Focus Mode, lineage endpoints)
6. **UI** (Map Explorer + Story Mode + Focus Mode; evidence drawer; policy notices; version badges)
7. **Index builders** (rebuildable projections: DB/search/graph/tiles)

### Architecture diagram (trust surfaces)

~~~mermaid
flowchart TB
  subgraph Clients
    UI[UI Map Story Focus]
    EXT[External clients]
  end

  subgraph Enforcement
    API[Governed API]
    POL[Policy engine]
    EV[Evidence resolver]
  end

  subgraph Canonical
    OBJ[Object storage artifacts]
    CAT[Catalogs DCAT STAC PROV + receipts]
    AUD[Audit ledger]
  end

  subgraph Projections
    DB[DB projection]
    SRCH[Search projection]
    GR[Graph projection]
    TL[Tile projection]
  end

  UI --> API
  EXT --> API
  API --> POL
  API --> EV
  EV --> CAT
  EV --> OBJ
  API --> DB
  API --> SRCH
  API --> GR
  API --> TL
  API --> AUD
~~~

[↑ Back to top](#kansas-frontier-matrix-kfm)

---

## Truth path and promotion contract

KFM is “map-first,” but the map is only as trustworthy as the data lifecycle behind it.

### Data lifecycle zones (truth path)

| Zone | Purpose | What belongs here | User-visible? |
|---|---|---|---|
| **RAW** | Immutable acquisition | Source snapshots + checksums + terms/license snapshots | No |
| **WORK** | Intermediate transforms | Normalization, enrichment, intermediate derivations | No |
| **QUARANTINE** | Failure isolation | Validation failures, rights-unclear artifacts, sensitivity concerns | No |
| **PROCESSED** | Publishable artifacts | Cleaned, validated, policy-ready outputs | Not until promoted |
| **CATALOG** | Canonical metadata + lineage | DCAT + STAC + PROV + run receipts + link validation | Indirectly |
| **PUBLISHED** | Governed runtime | Only policy-safe promoted versions reach UI/export | Yes |

### Promotion Contract (fail-closed gates)

Promotion is the act of moving from Raw/Work into Processed + Catalog/Lineage, and therefore into runtime surfaces.

**Minimal gates (starter):**
- **Identity & versioning:** deterministic DatasetVersion ID; promotion manifest exists; spec_hash drift check passes
- **Artifacts:** processed artifacts exist; each has digest; predictable paths; media types recorded
- **Catalogs:** DCAT/STAC/PROV schema-valid under profiles
- **Cross-links:** all links resolve; EvidenceRefs resolve
- **Policy:** policy_label assigned; obligations applied; default-deny tests pass
- **QA:** validation reports present; failures quarantined
- **Audit:** run receipt emitted; append-only audit entry; approvals captured if required
- **Rights:** license + rights holder present for every distribution; “metadata-only” allowed where mirroring is not permitted

### Promotion manifest (template)

~~~json
{
  "kfm_promotion_manifest_version": "v1",
  "dataset_slug": "example_dataset",
  "dataset_version_id": "2026-02.abcd1234",
  "spec_hash": "sha256:abcd1234",
  "released_at": "2026-02-20T13:00:00Z",
  "artifacts": [
    { "path": "events.parquet", "digest": "sha256:2222", "media_type": "application/x-parquet" },
    { "path": "events.pmtiles", "digest": "sha256:3333", "media_type": "application/vnd.pmtiles" }
  ],
  "catalogs": [
    { "path": "dcat.jsonld", "digest": "sha256:4444" },
    { "path": "stac/collection.json", "digest": "sha256:5555" },
    { "path": "prov/bundle.jsonld", "digest": "sha256:6666" }
  ],
  "qa": { "status": "pass", "report_digest": "sha256:7777" },
  "policy": { "policy_label": "public", "decision_id": "kfm://policy_decision/xyz" },
  "approvals": [
    { "role": "steward", "principal": "<id>", "approved_at": "2026-02-20T12:59:00Z" }
  ]
}
~~~

### Run receipt (starter shape)

A run receipt exists for:
- pipeline ingest / normalize / validate / promote
- index rebuilds (DB/search/tiles)
- story publish events
- Focus Mode answers

~~~json
{
  "kfm_run_receipt_version": "v1",
  "run_id": "kfm://run/2026-02-20T12:34Z.noaa.abcd1234",
  "kind": "pipeline|index|story_publish|focus",
  "inputs": [
    { "href": "raw/.../source.csv", "digest": "sha256:....", "zone": "raw" }
  ],
  "outputs": [
    { "href": "processed/.../events.parquet", "digest": "sha256:....", "zone": "processed" }
  ],
  "checks": { "qa_status": "pass", "catalog_valid": true, "links_ok": true },
  "policy": { "policy_label": "public", "decision_id": "kfm://policy_decision/xyz", "obligations": [] },
  "environment": {
    "git_commit": "<commit>",
    "container_image": "sha256:<image_digest>",
    "runtime": "kubernetes",
    "parameters": {}
  },
  "timestamps": { "started_at": "2026-02-20T12:34:56Z", "ended_at": "2026-02-20T12:45:10Z" },
  "audit_ref": "kfm://audit/entry/123"
}
~~~

[↑ Back to top](#kansas-frontier-matrix-kfm)

---

## Deterministic identity and versioning

KFM treats identity as a contract.

### DatasetVersion identity (starter)

**PROPOSED pattern (digest-backed):**
- `dataset_version_id = <yyyy-mm>.<spec_hash_prefix>`
- `spec_hash` is derived from a canonical dataset spec (`data/specs/<dataset_slug>.json`)

**Why this matters**
- guarantees reproducibility
- supports “what changed?” comparisons
- keeps Focus Mode answers pin-able to an immutable version

### Canonical object storage layout (reference)

**PROPOSED canonical layout (digest + version oriented):**

~~~text
raw/<dataset_slug>/<spec_hash>/...
work/<dataset_slug>/<spec_hash>/...
quarantine/<dataset_slug>/<spec_hash>/...
processed/<dataset_slug>/<dataset_version_id>/
  artifacts/...
  runtime_metadata.json
catalog/<dataset_slug>/<dataset_version_id>/
  dcat.jsonld
  stac/collection.json
  stac/items/*.json
  prov/prov.jsonld
  run_receipts/*.json
audit/
  ledger/<year>/<month>/append-only.log
~~~

[↑ Back to top](#kansas-frontier-matrix-kfm)

---

## Catalog triplet and profiles

KFM treats catalogs not as “nice metadata,” but as the **canonical interface** between pipeline outputs and runtime.

### Triplet responsibilities

- **DCAT answers:** “What is this dataset? Who published it? What is the license? What are the distributions?”
- **STAC answers:** “What assets exist? What are their spatiotemporal extents? Where are the files?”
- **PROV answers:** “How were these outputs created? Which inputs, which tools, which parameters?”

### Profiles (fail-closed)

KFM defines strict profiles for each catalog so validation is predictable.

**DCAT minimum fields (PROPOSED):**
- `dct:title`, `dct:description`, `dct:publisher`
- `dct:license` (or `dct:rights`)
- `dcat:theme` (controlled vocabulary)
- `dct:spatial` and `dct:temporal`
- `dcat:distribution` (one per artifact class)
- `prov:wasGeneratedBy` link to PROV activity bundle
- `kfm:policy_label`
- `kfm:dataset_id` and `kfm:dataset_version_id`

**STAC minimum (PROPOSED):**
- Collection: `id`, `title`, `description`, `extent`, `license`, links to DCAT, `kfm:dataset_version_id`, policy label
- Item: `id`, `geometry`/`bbox` (policy-consistent), `datetime` or start/end, assets with `href` + checksum + media_type, links to PROV/run receipt and DCAT distribution

**PROV minimum (PROPOSED):**
- `prov:Activity` per pipeline run
- `prov:Entity` per artifact (raw/work/processed)
- `prov:Agent` for pipeline and steward approvals
- `prov:used` and `prov:wasGeneratedBy` edges
- `kfm:policy_decision` references (decision_id + obligations)
- environment capture: container digest, git commit, parameters

### Cross-linking rules (must be testable)

- DCAT dataset → distributions → artifact digests
- DCAT dataset → `prov:wasGeneratedBy` → PROV bundle
- STAC collection → `rel="describedby"` → DCAT dataset
- STAC item → links → PROV activity and/or run receipt
- EvidenceRef schemes should resolve into these objects without guessing

> **CI MUST** include a link-checker that verifies cross-links for every promoted dataset version.

[↑ Back to top](#kansas-frontier-matrix-kfm)

---

## Evidence and citations

### EvidenceRef schemes (starter)

Prefer explicit schemes that can be resolved deterministically:

- `dcat://...`
- `stac://...`
- `prov://...`
- `doc://...`
- `graph://...`
- `url://...` (discouraged; use snapshots / governed docs when possible)

### Evidence resolver (contract)

The evidence resolver accepts an EvidenceRef (or structured reference), applies policy, and returns an **EvidenceBundle**:

- a human-readable **card** (what the UI shows)
- machine-readable metadata (what code/tests can validate)
- digests, dataset_version_id, and audit references
- policy decision results (allow/deny + obligations + reason codes)

**UI goal:** evidence resolution must be usable in **≤ 2 calls**.

### EvidenceBundle (template)

~~~json
{
  "bundle_id": "sha256:bundle...",
  "dataset_version_id": "2026-02.abcd1234",
  "title": "Record title",
  "policy": {
    "decision": "allow",
    "policy_label": "public",
    "obligations_applied": []
  },
  "license": { "spdx": "CC-BY-4.0", "attribution": "Source org" },
  "provenance": { "run_id": "kfm://run/2026-02-20T12:00:00Z.abcd" },
  "artifacts": [
    { "href": "processed/events.parquet", "digest": "sha256:2222", "media_type": "application/x-parquet" }
  ],
  "checks": { "catalog_valid": true, "links_ok": true },
  "audit_ref": "kfm://audit/entry/123"
}
~~~

### Evidence drawer (required trust surface)

The evidence drawer is not a “details panel.” It is a primary trust surface and MUST show (at minimum):

- Evidence bundle ID + digest
- DatasetVersion ID + dataset title
- License + rights holder + attribution (copyable)
- Policy label + obligations applied (with human-readable notice)
- Validation status + QA summary
- Provenance chain (run receipt link) + artifact digests (when permitted)
- Export controls (allowed/denied) with reason codes
- Audit reference for governed operations

[↑ Back to top](#kansas-frontier-matrix-kfm)

---

## Map and Story UX

KFM’s UI is governed. It renders what the API returns and never embeds privileged credentials.

### Core surfaces

- **Map Explorer** (primary): browse layers and time; inspect features; open evidence drawer; compare versions; export policy-safe views
- **Story Mode**: narrative nodes bound to map state and citations; versioned and reviewable; publish gates enforce evidence + policy
- **Catalog**: dataset discovery with policy-aware search and facets
- **Focus Mode**: governed Q&A constrained by view state + policy + evidence bundles
- **Admin/Steward** (restricted): promotion queue, QA reports, story review queue, limited policy operations

### Map state as a reproducible artifact

Map state captures:
- camera position (bbox/zoom)
- active layers + style parameters
- time window
- filters

Story Nodes store map state so stories replay the same view, and Focus Mode can accept `view_state` hints so answers are contextual and testable.

### Layer configuration (starter)

Layer configs define how a dataset version is rendered and interacted with on the map, including evidence behavior.

~~~json
{
  "layer_id": "noaa_storm_events",
  "title": "NOAA Storm Events",
  "dataset_version_id": "kfm://dataset/noaa_storm_events@<hash>",
  "rendering": {
    "type": "vector_tile",
    "source": "/api/v1/tiles/noaa_storm_events/{z}/{x}/{y}.pbf",
    "minzoom": 4,
    "maxzoom": 14
  },
  "time": { "field": "event_time_start", "mode": "range" },
  "evidence": {
    "on_click": { "kind": "stac", "template": "stac://noaa_storm_events/{feature_id}" }
  },
  "policy": { "policy_label": "public" }
}
~~~

### Story Nodes (v3: markdown + sidecar)

Story Nodes bind narrative to map state and citations. A Story Node has:
- a **markdown file** (human readable)
- a **sidecar JSON** (machine metadata: map state, citations, policy, review)

**Publishing gate:** all citations must resolve through the evidence resolver endpoint.

**Story Node markdown skeleton:**

~~~markdown
[KFM_META_BLOCK_V2]
doc_id: kfm://story/<uuid>@v1
title: <Story title>
type: story
version: v3
status: draft
owners: <names/teams>
created: YYYY-MM-DD
updated: YYYY-MM-DD
policy_label: public
related:
  - kfm://dataset/<slug>@<dataset_version_id>
[/KFM_META_BLOCK_V2]

# <Story title>

## Summary
<Short summary, including time window and scope.>

## Claims
1. <Claim text.> [CITATION: doc://...]
2. <Claim text.> [CITATION: stac://...]

## Narrative
<Full narrative with inline citations.>

## Evidence
- [CITATION: dcat://...]
- [CITATION: prov://...]
~~~

**Story Node sidecar skeleton:**

~~~json
{
  "kfm_story_node_version": "v3",
  "story_id": "kfm://story/<uuid>",
  "version_id": "v1",
  "status": "draft",
  "policy_label": "public",
  "review_state": "needs_review",
  "map_state": {
    "bbox": [-102.0, 36.9, -94.6, 40.0],
    "zoom": 6,
    "layers": [
      { "layer_id": "noaa_storm_events", "dataset_version_id": "2026-02.abcd1234" }
    ],
    "time_window": { "start": "1950-01-01", "end": "2024-12-31" }
  },
  "citations": [
    { "ref": "dcat://noaa_ncei_storm_events@2026-02.abcd1234", "kind": "dcat" },
    { "ref": "prov://run/2026-02-20T12:34Z...", "kind": "prov" }
  ]
}
~~~

[↑ Back to top](#kansas-frontier-matrix-kfm)

---

## Focus Mode AI

Focus Mode is not a general chatbot. It is a **governed workflow**.

### Control loop (reference design)

~~~mermaid
flowchart LR
  P[Policy pre-check] --> R[Plan retrieval]
  R --> Q[Retrieve policy-filtered evidence]
  Q --> B[Resolve EvidenceBundles]
  B --> S[Synthesize answer grounded in bundles]
  S --> V[Verify citations hard gate]
  V -->|pass| E[Emit run receipt + audit ref]
  V -->|fail| A[Abstain with policy-safe reason]
~~~

### Expectations

- **Citations are mandatory.** If citations cannot be verified, the correct behavior is to **abstain** (or reduce scope).
- Every query emits a **run receipt** capturing:
  - model identifier
  - prompt version
  - retrieval config version
  - policy engine version
  - input bundles by digest
  - output hash
- Prompt/model changes are treated like code changes and require review + evaluation harness pass.

### Prompt injection and data exfiltration defenses (starter)

Because Focus Mode may retrieve documents (including OCR), it must treat retrieved text as untrusted.

- Tool allowlist: the model cannot call arbitrary tools or fetch arbitrary URLs.
- Evidence resolver boundary: the model receives only policy-filtered evidence cards; restricted material is never passed through.
- Policy-safe refusal templates: deny or abstain without revealing restricted existence.
- Output scanning: block disallowed leakage patterns (coords/PII-like strings) where policy prohibits.

### Evaluation harness (release gate)

At minimum:
- citation coverage and resolvability
- correct abstention/refusal behavior (policy-safe)
- sensitivity leakage checks (coords/PII-like strings where prohibited)
- golden query regression suite pinned to DatasetVersions

[↑ Back to top](#kansas-frontier-matrix-kfm)

---

## Governance

Governance in KFM is not a policy document alone. It becomes enforceable behavior through **promotion gates**, **policy labels and obligations**, **access control**, and **append-only audit logging**.

### Baseline roles (starter)

| Role | Responsibilities | Key powers (must be audited) |
|---|---|---|
| **Public user** | Read public layers/stories; Focus Mode limited to public evidence | None |
| **Contributor** | Propose datasets/stories; draft content; cannot publish | Open PRs/issues (no approvals) |
| **Reviewer/Steward** | Approves promotions + story publishing; owns policy labels + redaction rules | Approve promotion; approve story publication; apply embargo; restrict export |
| **Operator** | Runs pipelines and manages deployments; cannot override policy gates | Deploy services; run pipeline jobs; manage infra credentials |
| **Governance council / community stewards** | Controls culturally sensitive materials; defines rules for restricted collections | Set constraints; require consultation; approve/deny public representations |

### RACI (minimum)

- **Dataset onboarding**
  - Responsible: contributor (spec + docs), data engineer (pipeline), GIS engineer (spatial QA)
  - Accountable: steward
  - Consulted: governance council (culturally sensitive), legal/compliance (rights unclear)
  - Informed: operator

- **Dataset promotion**
  - Responsible: operator (run), data engineer (validate outputs)
  - Accountable: steward
  - Consulted: governance council (sensitive), security (restricted infrastructure)
  - Informed: contributor

- **Story publishing**
  - Responsible: contributor (draft), historian/editor (review)
  - Accountable: steward
  - Consulted: governance council (Indigenous/cultural), legal (image reuse)
  - Informed: public

- **Policy changes**
  - Responsible: steward + policy engineer
  - Accountable: governance council or designated owner
  - Consulted: operators (runtime impact), contributors (workflow impact)
  - Informed: users

### Policy labels (starter list)

These vocabularies must be versioned and maintained:

- `public`
- `public_generalized`
- `restricted`
- `restricted_sensitive_location`
- `internal`
- `embargoed`
- `quarantine`

> **PROPOSED defaults aligned to KFM posture**
> - Default deny for sensitive-location and restricted datasets.
> - If any public representation is allowed, produce a separate **public_generalized** dataset version.
> - Never leak restricted metadata in 403/404 responses.
> - Do not embed precise coordinates in Story Nodes or Focus outputs unless policy explicitly allows.
> - Treat redaction/generalization as a first-class transform recorded in PROV.

### Policy-as-code (recommended pattern)

- Policy Decision Point (PDP): OPA or equivalent
- Policy Enforcement Points (PEP):
  - CI: schema validation + policy tests block merges
  - Runtime API: policy checks before serving data
  - Evidence resolver: policy checks before resolving evidence and rendering bundles
  - UI: shows policy badges/notices; never decides

**OPA/Rego policy bundle skeleton (default deny + tests):**

~~~text
policy/
  rego/
    kfm.rego
  fixtures/
    public_user.json
    steward_user.json
    dataset_public.json
    dataset_restricted.json
  tests/
    kfm_test.rego
~~~

**Minimal Rego starter:**

~~~rego
package kfm.policy

default allow = false

allow {
  input.role == "steward"
}

# Example obligation
obligations["show_notice"] {
  input.policy_label == "public_generalized"
}
~~~

**Minimal policy tests:**

~~~rego
package kfm.policy

test_default_deny {
  not allow with input as {"role": "public"}
}

test_steward_allow {
  allow with input as {"role": "steward"}
}
~~~

### Licensing and rights enforcement (non-optional)

Key principle: **online availability does not equal permission to reuse**.

Operational rules:
- Promotion gate requires license + rights holder for every distribution.
- “Metadata-only reference” is allowed: catalog an item without mirroring it if rights do not allow.
- Exports must include attribution and license text automatically.
- Story publishing gate blocks if rights are unclear for included media.

### Narrative review triggers (starter)

Any story should trigger additional review when:

- it cites `restricted_sensitive_location` datasets
- it could plausibly enable harm (vulnerable infrastructure, private individuals)
- it is produced primarily from OCR without corroborating structured data
- uncertainty is high or data quality is degraded

[↑ Back to top](#kansas-frontier-matrix-kfm)

---

## Datasets and sources

### Source selection rubric (starter)

Choose sources that:
- are authoritative and stable
- have clear licensing terms
- have defined spatiotemporal coverage
- are useful across multiple story arcs
- can be represented with evidence + provenance

Avoid early sources that:
- have unclear reuse rights for media
- contain high-risk PII or sensitive coordinates without a generalization pathway
- require heavy scraping without clear permission

### Anchor dataset shortlist (buildable vNext starter set)

These are “anchor” datasets because they support many story arcs and can be integrated with strong provenance.

- **Demographics:** IPUMS NHGIS (historical tables + boundaries)
- **Land:** BLM GLO land patents (public domain; names may be sensitive)
- **Hydrology:** USGS WaterData/NWIS (public domain)
- **Hazards:** NOAA Storm Events (public domain)
- **Disasters:** FEMA disaster declarations (public domain)
- **Basemap:** USGS National Map (public domain base layers)
- **Kansas GIS framework:** Kansas DASC Geoportal (state authoritative layers)

### “Anchor + more” (expanded, buildable extensions)

These are **PROPOSED** additions that typically integrate well in a map-first, time-aware system.

**Hazards + climate**
- NOAA SPC severe weather GIS (tornado tracks, hail/wind reports) *(public domain; verify attribution requirements)*
- U.S. Drought Monitor (weekly polygons)
- Wildfire perimeters (NIFC; Kansas Forest Service layers where available)

**Land cover + agriculture**
- National Land Cover Dataset (NLCD) (time series; raster → COGs)
- USDA Cropland Data Layer (annual; note licensing/terms)

**Boundaries + governance**
- Historical county boundaries (valid time critical)
- PLSS grids / survey lines (where permitted)
- Treaty/reservation boundaries (governance council review by default)

**Ecology + biodiversity (governance-heavy)**
- Public range/habitat models (e.g., GAP-derived products)
- Critical habitat designations (public), with careful narrative framing
- Internal heritage inventories: **restricted**, publish generalized derivatives only

### Source registry entry (required)

Every source must have a registry entry with:
- name and authority
- access method (API/bulk/scrape/manual)
- cadence
- license/terms snapshot
- sensitivity classification
- connector spec + credentials strategy
- known limitations + QA checks

> **Rule:** the registry is not optional documentation; it is an input to promotion gates.

[↑ Back to top](#kansas-frontier-matrix-kfm)

---

## Repository layout

> **CONFIRMED:** KFM’s blueprints recommend a modular monorepo layout with `apps/` and `packages/` plus governed `data/`, `docs/`, `contracts/`, and `policy/`.  
> **UNKNOWN until verified:** the exact current repo structure on your branch.

### Expanded layout (target + working structure)

This layout combines the blueprint’s “clean layering” with practical repo needs (pipelines, infra, investigations, quarantine, and eval).

~~~text
Kansas-Frontier-Matrix/
├─ README.md
│
├─ docs/                                         # Human-facing docs (governed; policy-labeled when served)
│  ├─ adr/                                       # Architecture Decision Records
│  ├─ governance/                                # Policy labels, obligations, review workflows, rubrics
│  ├─ runbooks/                                  # Oncall/DR/incident procedures (operations)
│  ├─ stories/                                   # Story Nodes (markdown + sidecars)
│  ├─ investigations/                            # Research notebooks, spike notes, controlled experiments
│  ├─ schemas/                                   # Human-readable schema docs (if not auto-generated)
│  └─ standards/                                 # MetaBlock templates, doc lint rules, style guides
│
├─ contracts/                                    # Machine-enforced contracts (CI gates + runtime boundaries)
│  ├─ openapi/                                   # REST boundary contracts
│  ├─ schemas/                                   # JSON Schemas (DTOs, manifests, receipts, configs)
│  └─ profiles/                                  # DCAT/STAC/PROV profile constraints + validators
│
├─ policy/                                       # Policy-as-code (default-deny; explicit allow)
│  ├─ rego/                                      # Authoritative policy rules
│  ├─ tests/                                     # Policy tests (fixtures-driven; run in CI)
│  └─ fixtures/                                  # Allow/deny + obligation fixtures (deterministic)
│
├─ data/                                         # Governed data zones (may be pointers in prod)
│  ├─ specs/                                     # Dataset onboarding specs (canonical inputs for spec_hash)
│  ├─ raw/                                       # Immutable acquisitions (never served)
│  ├─ work/                                      # Intermediates (regeneratable; never served)
│  ├─ quarantine/                                # Failed/blocked artifacts (rights/QA/sensitivity)
│  ├─ processed/                                 # Publishable artifacts (immutable per version)
│  ├─ catalog/                                   # DCAT/STAC/PROV + receipts (canonical metadata)
│  ├─ published/                                 # Published releases/exports (policy-safe)
│  └─ audit/                                     # Audit checkpoints (often external in prod)
│
├─ apps/                                         # Deployable applications (service boundaries)
│  ├─ api/                                       # Governed API (policy + evidence enforcement)
│  ├─ ui/                                        # Map/Story/Focus frontend
│  └─ workers/                                   # Pipeline runner + index builders
│
├─ packages/                                     # Libraries aligned to clean architecture
│  ├─ domain/                                    # Pure domain models + invariants
│  ├─ usecases/                                  # Workflows: ingest/promote/resolve/publish
│  ├─ adapters/                                  # Infrastructure adapters (DB, object store, OPA, search)
│  ├─ evidence/                                  # EvidenceRef parsing + bundle assembly
│  ├─ catalog/                                   # DCAT/STAC/PROV generation + validators
│  └─ shared/                                    # DTOs, schemas, utils, constants, reason codes
│
├─ infra/                                        # Infrastructure as code (env + provisioning)
│  ├─ k8s/                                       # Kubernetes manifests (base)
│  ├─ helm/                                      # Helm charts (optional)
│  └─ terraform/                                 # Cloud resources (optional)
│
├─ tools/                                        # Deterministic validators + linkcheck + hashing tools
│  ├─ validators/                                # validate_dcat / validate_stac / validate_prov
│  ├─ linkcheck/                                 # catalog link checking; citation resolvability checks
│  └─ hash/                                      # spec_hash generation + drift checks
│
├─ scripts/                                      # Operational entrypoints (CI/local parity)
│  ├─ promote/                                   # Promotion/publish commands (fail-closed; emits receipts)
│  ├─ lint/                                      # Lint/validate entrypoints (docs, schemas, policy, catalogs)
│  ├─ rebuild/                                   # Rebuild projections (DB/search/tiles) from canonical artifacts
│  └─ dev/                                       # Local dev orchestration helpers
│
└─ tests/                                        # Test suites (repo-wide)
   ├─ integration/                               # Integration tests (service-backed)
   └─ eval/                                      # Focus Mode evaluation harness (gold sets + expectations)
~~~

### Where “CI gates” live (recommended)

- `.github/workflows/` – pipeline definition (lint, tests, policy tests, validators, linkcheck, eval)
- `tools/*` – deterministic validators/linkcheck tools used by CI and locally
- `contracts/*` – schemas/profiles treated as production

**Example CI gate list (starter):**
- lint + typecheck
- unit tests
- validate DCAT/STAC/PROV
- linkcheck citations
- OPA policy tests
- spec_hash drift check
- evidence resolver contract tests
- Focus Mode eval (optional early)

[↑ Back to top](#kansas-frontier-matrix-kfm)

---

## Contributing

### What “good” looks like in KFM

- Every change is **reversible**, **testable**, and **governed**.
- Nothing user-visible ships without:
  - policy gates
  - resolvable citations
  - audit receipts
  - rights metadata

### Contribution paths

1) **Dataset onboarding**
- Add/update source registry entry
- Implement/adjust connector + normalization + validation
- Produce processed artifacts + catalogs
- Pass Promotion Contract gates
- Add layer config + evidence click behavior

2) **Story authoring**
- Use EvidenceRefs (not “trust me” claims)
- Verify citations resolve
- Respect policy labels + rights constraints
- Keep map state reproducible (saved view state)

3) **Policy changes**
- Default deny remains intact
- Update fixtures + tests
- Document rationale in an ADR
- Validate CI + runtime semantics remain aligned

### PR checklist (starter)

- [ ] No secrets or privileged tokens added
- [ ] Schemas and contracts updated (if needed)
- [ ] Policy fixtures/tests updated (if needed)
- [ ] Catalog lint + link-check passes (if applicable)
- [ ] Evidence resolver tests cover new EvidenceRefs (if applicable)
- [ ] For Focus Mode: eval harness passes and golden queries remain stable
- [ ] For stories: all citations resolve and are policy-allowed

[↑ Back to top](#kansas-frontier-matrix-kfm)

---

## Security

### Threat model checklist (starter)

- TM-001: Any client access storage/DB directly? **MUST be NO**
- TM-002: Can public users infer restricted existence via error differences? **MUST be NO**
- TM-003: Are downloads/exports checked against policy labels + rights? **MUST be YES**
- TM-004: Can retrieved documents inject instructions that bypass policy? **MUST be mitigated**
- TM-005: Are citations verified and policy-filtered before synthesis? **MUST be YES**
- TM-006: Are outputs scanned for restricted patterns (coords/PII-like strings) where required? **SHOULD be YES**
- TM-007: Are pipeline credentials least-privileged and rotated? **MUST be YES**
- TM-008: Are processed artifacts immutable by digest? **MUST be YES**
- TM-009: Are builds reproducible with SBOM and provenance? **SHOULD be YES**
- TM-010: Is the audit ledger append-only and access-controlled? **MUST be YES**
- TM-011: Are audit logs redacted where they could leak restricted data? **MUST be YES**

### Reporting

- Security contact: **TBD** (add an email/issue workflow)
- For vulnerabilities affecting policy, exports, or evidence resolution: treat as **high severity** and fail-closed.

[↑ Back to top](#kansas-frontier-matrix-kfm)

---

## Roadmap

> Keep roadmaps small, reviewable, and reversible. Prefer “glue artifacts” (contracts, validators, manifests, runbooks) before expanding scope.

### Phase 0 — Foundations (must exist before scale)

- [ ] Promotion Contract gates implemented and enforced
- [ ] Catalog profiles + validators (DCAT/STAC/PROV)
- [ ] Evidence resolver contract + EvidenceBundle template
- [ ] Policy-as-code (default deny) + fixtures-driven tests
- [ ] Audit ledger + run receipts (pipeline + Focus)

### Phase 1 — Map Explorer MVP (trust-first)

- [ ] Evidence Drawer everywhere (layer clicks, charts, narratives)
- [ ] Dataset version + policy badges on all layers
- [ ] “What changed?” version comparison view (policy-safe)

### Phase 2 — Story Mode MVP

- [ ] Story Nodes with saved map state + versioning
- [ ] Publish gate: all citations resolve + rights metadata present
- [ ] Review workflow (steward + optional governance council triggers)

### Phase 3 — Focus Mode MVP (governed AI)

- [ ] Cite-or-abstain loop + citation verification gate
- [ ] Evaluation harness with golden queries + regression gate
- [ ] Prompt/model governance recorded in run receipts

### Phase 4 — Expand datasets safely

- [ ] Anchor dataset onboarding (public-domain first)
- [ ] Sensitive-location patterns (restricted precise + public_generalized derivatives)
- [ ] Rights-aware archive integration (metadata-first when needed)

[↑ Back to top](#kansas-frontier-matrix-kfm)

---

## References

### Primary KFM specs (vNext)

- *KFM — Most Expansive Compendium (vNext)* (2026-02-21)
- *KFM — Definitive Design & Governance Guide (vNext)* (2026-02-20)
- *KFM — Ultimate Blueprint (Draft)* (2026-02-20)

### Secondary reference library (provided PDFs, non-exhaustive)

- GIS + mapping: *Mapping Urban Spaces*; *A Primer of GIS*; *Geostatistical Mapping*; *GIS in Sustainable Urban Planning*
- Web + UI: *Research-Based Web Design & Usability Guidelines*; *Using SVG with CSS3 and HTML5*
- DevOps + pipelines: *Docker GitOps OpenShift*; *Open-Source Data Pipelines*
- Security: *Software Security Guide for Developers (2026 Edition)*

> **Reminder:** KFM is evidence-first. Don’t add user-visible content that cannot be traced to catalogs + evidence bundles.

[↑ Back to top](#kansas-frontier-matrix-kfm)

---

<details>
<summary><strong>Appendix: Operational templates (starter)</strong></summary>

### Dataset onboarding “Definition of Done” (starter)

- [ ] Source registry entry exists (license/terms snapshot + sensitivity + cadence)
- [ ] Acquisition manifest recorded; RAW artifacts checksummed
- [ ] WORK transforms recorded; failures quarantined
- [ ] PROCESSED artifacts produced with digests and stable paths
- [ ] DCAT/STAC/PROV generated and profile-valid
- [ ] Cross-links resolve; EvidenceRefs resolvable
- [ ] Policy label assigned; obligations documented
- [ ] QA report present; thresholds defined; pass/degraded/fail states supported
- [ ] Promotion manifest created; approvals captured
- [ ] Layer config created; evidence click behavior mapped to EvidenceRefs
- [ ] Rebuild scripts exist for projections (DB/search/tiles) from canonical artifacts

### Story publishing “Definition of Done” (starter)

- [ ] Narrative markdown includes EvidenceRefs for claims
- [ ] Saved map state included (camera/layers/time/filters)
- [ ] All citations resolve and are policy-allowed
- [ ] Rights metadata for embedded media present
- [ ] Policy label + review state assigned
- [ ] Publish event emits audit_ref + run receipt

### Focus Mode “Definition of Done” (starter)

- [ ] Policy pre-check blocks disallowed scopes/topics
- [ ] Retrieval is policy-filtered and returns only EvidenceBundles
- [ ] Every claim is grounded in resolvable citations
- [ ] Citation verifier is a hard gate
- [ ] Output scanning blocks restricted leakage patterns
- [ ] Run receipt emitted with model + prompt + bundle digests + output hash
- [ ] Eval harness exists with golden queries pinned to DatasetVersions

</details>

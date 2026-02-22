# Kansas Frontier Matrix

> **Map-first • Time-aware • Governed • Evidence-first • Cite-or-abstain**  
> **Core posture:** default-deny • fail-closed • reproducible by digest • policy enforced in CI + runtime

**Status:** vNext (blueprint-driven build)  
**Owners:** _TBD_ (add repo teams / stewards; required for CODEOWNERS + review routing)  
**Core promise:** anything you can see, cite, export, or ask KFM to explain is traceable to an immutable **DatasetVersion** + resolvable **EvidenceBundle**, with policy enforced consistently in CI and at runtime.  
**Primary experiences:** **Map Explorer** + **Timeline** + **Stories** + **Catalog** + **Focus Mode**.

[![Status](https://img.shields.io/badge/status-vNext-blue)](#)
[![Governance](https://img.shields.io/badge/governance-fail--closed-critical)](#)
[![Evidence](https://img.shields.io/badge/evidence-cite--or--abstain-important)](#)
[![Policy](https://img.shields.io/badge/policy-default--deny-critical)](#)
[![License](https://img.shields.io/badge/license-TBD-lightgrey)](#)

---

## Start here

Pick the path that matches what you’re doing:

- **Contributing code/docs/data**
  - Read: `CONTRIBUTING.md` (workflow), `.github/README.md` (CI gates + CODEOWNERS), `SECURITY.md` (reporting)
  - Know: changes to `.github/`, `policy/`, `contracts/`, and promotion tooling are **governance-critical**

- **Stewardship and governance**
  - Read: `docs/governance/` (labels, obligations, review triggers), `policy/` (policy-as-code + fixtures), `contracts/` (schemas/profiles/vocab)

- **Operating pipelines and runtime**
  - Read: `docs/runbooks/` and `infra/`
  - Know: DB/search/tiles are rebuildable projections; **canonical truth is processed artifacts + catalogs + receipts + audit**

> **NOTE**  
> This README describes the **target operating model** for vNext. If some files/directories are not present on your branch, treat those sections as **PROPOSED** and reconcile with repo reality before enforcing gates.

[↑ Back to top](#kansas-frontier-matrix)

---

## Quick navigation

[What this repo is](#what-this-repo-is) •
[Repo entrypoints](#repo-entrypoints) •
[Reality check](#reality-check) •
[Quick start](#quick-start) •
[System overview](#system-overview) •
[Minimum build order](#minimum-build-order) •
[Core invariants](#core-invariants) •
[Key concepts and glossary](#key-concepts-and-glossary) •
[Architecture](#architecture) •
[Governed API](#governed-api) •
[Truth path and promotion contract](#truth-path-and-promotion-contract) •
[Deterministic identity and versioning](#deterministic-identity-and-versioning) •
[Catalog triplet and profiles](#catalog-triplet-and-profiles) •
[Evidence and citations](#evidence-and-citations) •
[Map and story UX](#map-and-story-ux) •
[Focus Mode AI](#focus-mode-ai) •
[Discover Mode](#discover-mode) •
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
- **Contracts** (OpenAPI, schemas, catalog profiles, vocabularies) enforced in CI
- **Policy-as-code** (default deny) enforced in CI + runtime

### What KFM is not

- Not an ungoverned GIS file dump.
- Not a “trust me” narrative system (stories must cite resolvable evidence).
- Not a general chatbot (Focus Mode is a governed workflow that must cite-or-abstain).
- Not “whatever the database says” (DB/search/tiles are projections; catalogs + processed artifacts are canonical).

[↑ Back to top](#kansas-frontier-matrix)

---

## Repo entrypoints

If you only read three things first:

1. `README.md` — this operating model and where to find things.
2. `.github/README.md` — governance and automation (CI gates, CODEOWNERS posture).
3. `contracts/` + `policy/` — the machine-enforced truth: schemas/profiles/vocab + policy tests.

### Governance-critical surfaces

These paths change enforcement behavior. Treat changes here as production configuration:

| Path | Why it’s critical | Expected controls |
|---|---|---|
| `.github/` | merge-time enforcement | CODEOWNERS + required checks |
| `policy/` | default-deny semantics + obligations | fixtures-driven tests in CI |
| `contracts/` | runtime boundaries + schemas | schema/profile validation in CI |
| `tools/` | validators and hash/link tooling | deterministic tests + golden fixtures |
| `data/registry/` | what can be promoted and shown | lint + validation + steward review |
| `apps/api/` | the trust membrane enforcement point | security review + integration tests |
| `infra/` | runtime posture | operator review + policy alignment |

### Expected top-level governance files

Recommended for a governed system; if missing on your branch, add them early:

- `LICENSE` (SPDX-friendly; TBD)
- `CONTRIBUTING.md` (contributor workflow + CI gates)
- `SECURITY.md` (vulnerability reporting + posture)
- `CODE_OF_CONDUCT.md` (optional but recommended)
- `CHANGELOG.md` (optional early; valuable later)

[↑ Back to top](#kansas-frontier-matrix)

---

## Reality check

Before implementing or “fixing” anything, verify what exists **on your branch**. This prevents governance failures caused by assumptions.

### Minimum verification steps

- Confirm whether this is a monorepo (`apps/` + `packages/`) or a different layout.
- Confirm the policy engine choice and how it is executed in CI and runtime.
- Confirm what is canonical (object storage + catalogs + audit ledger) vs rebuildable (DB/search/tiles).
- Confirm how documents are treated: served via governed APIs (policy-labeled) or only via Git.
- Confirm the UI stack and how map state is represented and persisted (Story Node sidecars, view-state tokens).
- Confirm how secrets are managed (must not live in repo; injected via CI/runtime secret stores).

> **Fail-closed rule:** if any of the above is unclear, default-deny and treat the feature as **PROPOSED** until verified.

[↑ Back to top](#kansas-frontier-matrix)

---

## Quick start

> **NOTE**  
> Exact commands / package managers / service topology vary by branch.  
> Prefer `make help` or `scripts/dev/*` if present.

### 1) Get oriented

~~~bash
git clone <REPO_URL>
cd Kansas-Frontier-Matrix

ls
~~~

### 2) Try the “common entrypoints” (if present)

~~~bash
# If a Makefile exists
make help

# If it’s a Node/TypeScript workspace
node -v
npm -v
npm install
npm test

# If it’s a Python workspace
python --version
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
~~~

### 3) First principle while exploring

> **Rule of thumb:** if a thing is user-visible, it must be **promotable** and **citeable**.  
> If it cannot be cataloged and cited, it does not belong on the map.

[↑ Back to top](#kansas-frontier-matrix)

---

## System overview

KFM is map-first, but the map is only as trustworthy as the lifecycle behind it.

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

### Trust membrane

- **Clients MUST NOT** access object storage / DB directly.
- Access flows through a **governed API** that applies **policy**, **evidence resolution**, **obligations**, and **audit logging** consistently.
- Backend domain logic **MUST NOT** bypass repository interfaces to talk directly to infrastructure.

### Canonical vs rebuildable

- **Canonical:** processed artifacts in object storage, catalogs (DCAT/STAC/PROV), run receipts, and audit ledger.
- **Rebuildable projections:** PostGIS tables, search indexes, graph views, and tile bundles.

> **Rule:** if a projection and a catalog disagree, the catalog + processed artifacts win.

[↑ Back to top](#kansas-frontier-matrix)

---

## Minimum build order

KFM’s safest path is to build trust primitives first, UI last.

### Minimum viable trust

- [ ] **Contracts**: schemas/profiles/vocab exist and validate in CI (`contracts/`)
- [ ] **Policy**: default-deny rules + fixtures-driven tests (`policy/`)
- [ ] **Deterministic identity**: canonical `spec_hash` + drift tests (`tools/hash/`)
- [ ] **Catalog triplet**: DCAT/STAC/PROV generation + validators + cross-link checks
- [ ] **Evidence resolver**: EvidenceRef → EvidenceBundle; policy applied; fail-closed
- [ ] **Run receipts + audit**: immutable receipts emitted for pipeline + Focus answers
- [ ] **Promotion gate**: no publish without manifests, validation, rights, and policy checks
- [ ] **Rebuildable projections**: DB/search/tiles built from canonical artifacts
- [ ] **UI surfaces**: Map Explorer/Stories/Focus render governed API results + evidence drawer

> **Reasoning:** if EvidenceRef cannot resolve deterministically, “map-first” becomes “trust me.”

[↑ Back to top](#kansas-frontier-matrix)

---

## Core invariants

These are KFM’s non-negotiables. Violating these breaks governance, not “just code.”

### Invariants

| Invariant | Meaning | How it’s enforced |
|---|---|---|
| **Truth path** | Data moves through zones (Raw → Work/Quarantine → Processed → Catalog → Published) with promotion gates | Promotion Contract gates (CI + pipeline) |
| **Trust membrane** | No direct client-to-storage/DB; domain logic never bypasses interfaces | Network controls + code structure + tests |
| **Evidence-first UX** | Evidence is not optional “details” — it’s a primary interaction everywhere | Evidence Drawer required + UI gating |
| **Cite-or-abstain Focus Mode** | If citations cannot be verified, Focus Mode abstains | Citation verification hard gate + eval harness |
| **Canonical vs rebuildable** | Object storage + catalogs + audit ledger are canonical; DB/search/tiles are projections | Rebuild scripts + “source of truth” discipline |
| **Deterministic identity** | DatasetVersion IDs and artifact addresses are stable and digest-based | Canonical hashing + “hash drift” checks |
| **Row-level traceability** | Every feature row in projections carries `dataset_version_id` + an `evidence_ref` | Projection schema + integration tests |
| **Policy-safe errors** | Public users must not infer restricted dataset existence via error differences | API error model + tests + monitoring |

> **Norms used in docs:** MUST / MUST NOT / SHOULD / MAY (RFC-style).  
> **Section tags:** CONFIRMED / PROPOSED / UNKNOWN.  
> Use **CONFIRMED** only when backed by in-repo artifacts; otherwise use **PROPOSED**.

[↑ Back to top](#kansas-frontier-matrix)

---

## Key concepts and glossary

Use these terms consistently in code, schemas, tests, and documentation.

| Term | Definition |
|---|---|
| **Dataset** | A logical dataset identity (e.g., “NOAA Storm Events”) |
| **DatasetVersion** | An immutable version corresponding to a specific promoted output set |
| **Spec hash** | Deterministic hash derived from a canonical dataset spec; used to identify versions |
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

### KFM URI patterns

KFM uses resolvable, stable identifiers. Examples:

- `kfm://dataset/<slug>@<dataset_version_id>`
- `kfm://run/<timestamp>.<slug>.<hash>`
- `kfm://audit/entry/<id>`
- Evidence refs: `dcat://...`, `stac://...`, `prov://...`, `doc://...`

> **Rule:** user-visible claims should reference evidence through an EvidenceRef resolvable to an EvidenceBundle.

[↑ Back to top](#kansas-frontier-matrix)

---

## Architecture

KFM keeps layers clean and enforces governance at boundaries.

### Clean layering

- **Domain:** pure domain models and invariants
- **Use cases:** workflows (ingest dataset, promote dataset version, publish story node, answer focus query)
- **Interfaces:** contracts (OpenAPI DTOs, schema registries, policy adapters, repository interfaces)
- **Infrastructure:** PostGIS, search, graph, object storage, CI, deployment

### Starting posture

Recommended: start as a modular monolith (plus worker processes) so invariants are easier to enforce and test; split into services only when isolation/scaling demands it.

Core components:

1. Pipeline runner + connectors
2. Catalog generator (DCAT/STAC/PROV + run receipts + profile validation + cross-link enforcement)
3. Policy engine (policy-as-code; same semantics in CI and runtime)
4. Evidence resolver (EvidenceRef → EvidenceBundle; policy + obligations applied; fail-closed)
5. Governed API (discovery, queries, tiles, stories, Focus Mode, lineage)
6. UI (Map Explorer + Story Mode + Focus Mode; evidence drawer; policy notices; version badges)
7. Index builders (rebuildable projections: DB/search/graph/tiles)

### Architecture diagram

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

[↑ Back to top](#kansas-frontier-matrix)

---

## Governed API

The governed API is the only supported way for clients to access data, evidence, and narratives.

### Design requirements

- Policy is enforced before data leaves the backend.
- Every response includes enough metadata to be traceable:
  - `dataset_version_id` (where relevant)
  - `audit_ref` (for governed operations)
  - policy decision summary where appropriate

### Illustrative endpoint surfaces

Actual routes may differ; treat these as contract targets:

- Catalog discovery
  - `GET /api/v1/datasets`
  - `GET /api/v1/datasets/{dataset_id}/versions`
  - `GET /api/v1/catalog/{dataset_version_id}`

- Evidence
  - `POST /api/v1/evidence/resolve` → EvidenceBundle(s)

- Map projections
  - `GET /api/v1/tiles/{layer_id}/{z}/{x}/{y}` (vector/raster)
  - `GET /api/v1/features/{layer_id}?bbox=...&time=...`

- Stories
  - `GET /api/v1/stories`
  - `GET /api/v1/stories/{story_id}`
  - `POST /api/v1/stories/{story_id}/publish` (steward-gated)

- Focus Mode
  - `POST /api/v1/focus/query` (policy + cite-or-abstain)

### Error model

Errors must be policy-safe and consistent so users cannot infer restricted existence.

Starter error shape:

~~~json
{
  "error": {
    "code": "NOT_FOUND|FORBIDDEN|VALIDATION_FAILED|POLICY_DENY",
    "message": "Policy-safe message",
    "request_id": "<trace id>",
    "audit_ref": "kfm://audit/entry/..."
  }
}
~~~

[↑ Back to top](#kansas-frontier-matrix)

---

## Truth path and promotion contract

KFM is map-first, but the map is only as trustworthy as the data lifecycle behind it.

### Data lifecycle zones

| Zone | Purpose | What belongs here | User-visible |
|---|---|---|---|
| **RAW** | Immutable acquisition | Source snapshots + checksums + terms/license snapshots | No |
| **WORK** | Intermediate transforms | Normalization, enrichment, intermediate derivations | No |
| **QUARANTINE** | Failure isolation | Validation failures, rights-unclear artifacts, sensitivity concerns | No |
| **PROCESSED** | Publishable artifacts | Cleaned, validated, policy-ready outputs | Not until promoted |
| **CATALOG** | Canonical metadata + lineage | DCAT + STAC + PROV + run receipts + link validation | Indirectly |
| **PUBLISHED** | Governed runtime | Only policy-safe promoted versions reach UI/export | Yes |

### Promotion contract

Promotion is moving from Raw/Work into Processed + Catalog and therefore into runtime surfaces.

Minimal fail-closed gates:

- Identity & versioning: deterministic DatasetVersion derived from canonical spec_hash; promotion manifest exists; spec_hash drift check passes
- Artifacts: processed artifacts exist; each has digest; stable paths; media types recorded
- Catalogs: DCAT/STAC/PROV schema-valid under profiles
- Cross-links: all links resolve; EvidenceRefs resolve
- Policy: policy_label assigned; obligations applied; default-deny tests pass
- QA: validation reports present; failures quarantined
- Audit: run receipt emitted; append-only audit entry; approvals captured if required
- Rights: license + rights holder present for every distribution; “metadata-only” allowed where mirroring is prohibited

### Promotion manifest template

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

### Run receipt template

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
    "runtime": "kubernetes|local",
    "parameters": {}
  },
  "timestamps": { "started_at": "2026-02-20T12:34:56Z", "ended_at": "2026-02-20T12:45:10Z" },
  "audit_ref": "kfm://audit/entry/123"
}
~~~

[↑ Back to top](#kansas-frontier-matrix)

---

## Deterministic identity and versioning

KFM treats identity as a contract.

### Deterministic identifiers

Baseline rule: DatasetVersion identity is derived deterministically from the canonical dataset spec (`data/specs/<dataset_slug>.json`), producing a `spec_hash`.

PROPOSED: include a human-friendly time component in `dataset_version_id` if it helps operators, but treat it as derived metadata — the `spec_hash` is the immutability anchor.

### Canonical object storage layout

Reference layout for the truth path:

~~~text
data/
  raw/<dataset_slug>/<dataset_version_id>/
    acquisition_manifest.json
    terms_snapshot.txt
    source_files/...
  work/<dataset_slug>/<dataset_version_id>/
    qa/...
    redaction_candidates/...
  quarantine/<dataset_slug>/<dataset_version_id>/
    reason.json
    artifacts/...
  processed/<dataset_slug>/<dataset_version_id>/
    artifacts/...
    runtime_metadata.json
  catalog/<dataset_slug>/<dataset_version_id>/
    dcat.jsonld
    stac/collection.json
    stac/items/*.json
    prov/prov.jsonld
    run_receipts/*.json
  published/<dataset_slug>/<dataset_version_id>/
    exports/...
  audit/
    ledger/<year>/<month>/append-only.log
~~~

> **Canonical rule:** once promoted, the processed + catalog artifacts are immutable. Projections must be rebuildable from these.

[↑ Back to top](#kansas-frontier-matrix)

---

## Catalog triplet and profiles

KFM treats catalogs not as “nice metadata,” but as the canonical interface between pipeline outputs and runtime.

### Triplet responsibilities

- DCAT answers: what is this dataset? who published it? what is the license? what are the distributions?
- STAC answers: what assets exist? what are their spatiotemporal extents? where are the files?
- PROV answers: how were these outputs created? which inputs, which tools, which parameters?

### Profiles

KFM defines strict profiles for each catalog so validation is predictable.

DCAT minimum fields:

- `dct:title`, `dct:description`, `dct:publisher`
- `dct:license` or `dct:rights`
- `dcat:theme` from controlled vocab
- `dct:spatial` and `dct:temporal`
- `dcat:distribution` one per artifact class
- link to PROV activity (`prov:wasGeneratedBy`)
- `kfm:policy_label`
- `kfm:dataset_id` and `kfm:dataset_version_id`

STAC minimum:

- Collection: `id`, `title`, `description`, `extent`, `license`, links to DCAT, `kfm:dataset_version_id`, policy label
- Item: `id`, `geometry`/`bbox` (policy-consistent), `datetime` or start/end, assets with `href` + checksum + media_type, links to PROV/run receipt and DCAT distribution

PROV minimum:

- `prov:Activity` per pipeline run
- `prov:Entity` per artifact (raw/work/processed)
- `prov:Agent` for pipeline + steward approvals
- `prov:used` and `prov:wasGeneratedBy` edges
- policy decision references (decision_id + obligations)
- environment capture: container digest, git commit, parameters

### Cross-linking rules

- DCAT dataset → distributions → artifact digests
- DCAT dataset → `prov:wasGeneratedBy` → PROV bundle
- STAC collection → `rel="describedby"` → DCAT dataset
- STAC item → links → PROV activity and/or run receipt
- EvidenceRef schemes resolve into these objects without guessing

### Catalog lint rules

A dataset version cannot be promoted unless:

- Each DatasetVersion has exactly one DCAT dataset record.
- STAC collection includes dataset_version_id and license.
- PROV bundle includes at least one Activity linking to every output artifact.
- Every artifact in processed appears in DCAT distributions and STAC assets (or is explicitly excluded with a reason).
- Checksums in catalogs match actual artifact digests.
- Catalogs contain no links to quarantine artifacts.

> CI MUST include profile validation + link-checking for every promoted DatasetVersion.

[↑ Back to top](#kansas-frontier-matrix)

---

## Evidence and citations

### EvidenceRef schemes

Prefer explicit schemes that can be resolved deterministically:

- `dcat://...`
- `stac://...`
- `prov://...`
- `doc://...`
- `graph://...`
- `url://...` (discouraged; use snapshots / governed docs when possible)

### Evidence resolver contract

The evidence resolver accepts EvidenceRefs, applies policy, and returns an EvidenceBundle:

- a human-readable card view (what the UI shows)
- machine-readable metadata (what code/tests validate)
- digests, dataset_version_id, audit references
- policy decision results (allow/deny + obligations + reason codes)

UI goal: evidence resolution should be usable in ≤ 2 calls.

### EvidenceBundle template

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

### Evidence drawer requirements

The Evidence Drawer is a primary trust surface and MUST show, at minimum:

- Evidence bundle ID + digest
- DatasetVersion ID + dataset title
- Policy label + decision + obligations (human-readable)
- License + rights holder + attribution (copyable)
- Provenance: run_id + last-validated timestamp
- Validation status + QA summary
- Export controls: allowed/denied with reason codes
- Audit reference for governed operations

[↑ Back to top](#kansas-frontier-matrix)

---

## Map and story UX

KFM’s UI is governed. It renders what the API returns and never embeds privileged credentials.

### Core surfaces

- Map Explorer: browse layers and time; inspect features; open evidence drawer; compare versions; export policy-safe views
- Timeline: time window selection with bitemporal awareness where needed (valid time vs transaction time)
- Story Mode: narrative nodes bound to map state and citations; versioned and reviewable; publish gates enforce evidence + policy
- Catalog: dataset discovery with policy-aware search and facets
- Focus Mode: governed Q&A constrained by view state + policy + evidence bundles
- Studio: optional story authoring/review UI (steward-gated)

### Map state as a reproducible artifact

Map state captures:

- camera position (bbox/zoom)
- active layers + style parameters
- time window
- filters

Story Nodes store map state so stories replay the same view, and Focus Mode can accept `view_state` hints so answers are contextual and testable.

### Layer configuration template

~~~json
{
  "layer_id": "noaa_storm_events",
  "title": "NOAA Storm Events",
  "dataset_version_id": "kfm://dataset/noaa_storm_events@2026-02.abcd1234",
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

### Story Nodes

Story Nodes bind narrative to map state and citations. A Story Node has:

- a markdown file (human narrative)
- a sidecar JSON (machine metadata: map state, citations, policy, review)

Publishing gate: all citations must resolve through the evidence resolver endpoint.

Story Node markdown skeleton:

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

Story Node sidecar skeleton:

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

[↑ Back to top](#kansas-frontier-matrix)

---

## Focus Mode AI

Focus Mode is not a general chatbot. It is a governed workflow.

### Control loop

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

- Citations are mandatory. If citations cannot be verified, the correct behavior is to abstain or reduce scope.
- Every query emits a run receipt capturing:
  - model identifier
  - prompt version
  - retrieval config version
  - policy engine version
  - input bundles by digest
  - output hash
- Prompt/model changes are treated like code changes and require review + evaluation harness pass.

### Prompt injection and data exfiltration defenses

Retrieved text is untrusted:

- Tool allowlist: the model cannot call arbitrary tools or fetch arbitrary URLs.
- Evidence resolver boundary: the model receives only policy-filtered evidence cards; restricted material is never passed through.
- Policy-safe refusal templates: deny or abstain without revealing restricted existence.
- Output scanning: block disallowed leakage patterns (coords/PII-like strings) where policy prohibits.

### Evaluation harness

At minimum:

- citation coverage and resolvability
- correct abstention/refusal behavior (policy-safe)
- sensitivity leakage checks (coords/PII-like strings where prohibited)
- golden query regression suite pinned to DatasetVersions

[↑ Back to top](#kansas-frontier-matrix)

---

## Discover Mode

Discover Mode is an optional but strongly recommended capability for governed research and “working notes.”

### Why it exists

- Investigations are where uncertainty lives.
- KFM must support exploration without accidentally publishing unverified claims.
- Discover Mode artifacts should be reproducible, policy-labeled, and easy to promote into Story Nodes once validated.

### Where it lives

Recommended locations:

- `docs/investigations/` — narrative exploration, method notes, hypotheses
- `data/work/` — intermediate datasets created during investigation
- `data/quarantine/` — blocked results with reason docs
- `tests/eval/` — evaluation artifacts when the investigation impacts Focus Mode

Rule: Discover Mode outputs are not user-visible until promoted through the same evidence + policy gates.

[↑ Back to top](#kansas-frontier-matrix)

---

## Governance

Governance in KFM is not just a policy document. It becomes enforceable behavior through promotion gates, policy labels and obligations, access control, and append-only audit logging.

### Baseline roles

| Role | Responsibilities | Key powers |
|---|---|---|
| Public user | Read public layers/stories; Focus Mode limited to public evidence | None |
| Contributor | Propose datasets/stories; draft content; cannot publish | Open PRs/issues |
| Reviewer/Steward | Approves promotions + story publishing; owns labels + redaction rules | Approve promotion/story; embargo; restrict export |
| Operator | Runs pipelines and manages deployments; cannot override gates | Deploy services; run jobs; manage infra credentials |
| Governance council / community stewards | Controls culturally sensitive materials; defines rules for restricted collections | Require consultation; approve/deny public representations |

### Controlled vocabularies

Recommended location: `contracts/vocab/` (versioned and enforced)

Policy labels starter:

- `public`
- `public_generalized`
- `restricted`
- `restricted_sensitive_location`
- `internal`
- `embargoed`
- `quarantine`

Artifact zones starter:

- `raw`
- `work`
- `processed`
- `catalog`
- `published`

Citation kinds starter:

- `dcat`
- `stac`
- `prov`
- `doc`
- `graph`
- `url` (discouraged)

### Policy defaults aligned to KFM posture

- Default deny for sensitive-location and restricted datasets.
- If any public representation is allowed, produce a separate public-generalized derivative.
- Never leak restricted metadata in 403/404 responses.
- Do not embed precise coordinates in Story Nodes or Focus outputs unless policy explicitly allows.
- Treat redaction/generalization as a first-class transform recorded in PROV.

### Licensing and rights enforcement

Operational rules:

- Promotion gate requires license + rights holder for every distribution.
- “Metadata-only reference” is allowed: catalog an item without mirroring it if rights do not allow.
- Exports must include attribution and license text automatically.
- Story publishing gate blocks if rights are unclear for included media.

### Narrative review triggers

Extra review required when:

- the story cites restricted-sensitive-location datasets
- it could plausibly enable harm (vulnerable infrastructure, private individuals)
- it is produced primarily from OCR without corroborating structured data
- uncertainty is high or data quality is degraded

[↑ Back to top](#kansas-frontier-matrix)

---

## Datasets and sources

### Source selection rubric

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

### Anchor dataset shortlist

These are anchor datasets because they support many story arcs and can be integrated with strong provenance.

- Demographics: IPUMS NHGIS (verify terms and attribution)
- Land: BLM GLO land patents (names may be sensitive; governance review for narratives)
- Hydrology: USGS WaterData/NWIS
- Hazards: NOAA Storm Events
- Disasters: FEMA disaster declarations
- Basemap: USGS National Map base layers
- Kansas GIS framework: Kansas DASC Geoportal authoritative layers

Rule: do not assert “public domain” or “free to reuse” without capturing and snapshotting source terms.

### Source registry entry

Every source must have a registry entry (recommended path: `data/registry/sources/`) with:

- source_id (stable)
- authority
- domain (hazards/demographics/admin/history/etc)
- access_method (api/bulk/portal/manual)
- cadence
- license/rights and a terms snapshot pointer
- sensitivity intent (policy_label)
- notes (limitations + QA checks)

Rule: the registry is an input to promotion gates, not optional documentation.

### Dataset onboarding spec

Dataset onboarding specs are canonical inputs to deterministic ID generation and pipeline execution (recommended path: `data/specs/<dataset_slug>.json`).

~~~json
{
  "kfm_dataset_spec_version": "v1",
  "dataset_slug": "<slug>",
  "title": "<human title>",
  "sources": [
    {
      "kind": "bulk|api|scrape|document|stream",
      "uri": "<url-or-identifier>",
      "terms_snapshot_required": true,
      "schedule": "cron(0 3 * * *)"
    }
  ],
  "transforms": [
    {
      "name": "normalize",
      "container_image": "<digest-pinned>",
      "params": { "crs": "EPSG:4326", "schema_version": "v1" }
    }
  ],
  "outputs": [
    { "zone": "processed", "path": "artifacts/data.parquet", "media_type": "application/x-parquet" }
  ],
  "policy": { "default_policy_label": "public" }
}
~~~

[↑ Back to top](#kansas-frontier-matrix)

---

## Repository layout

This layout aligns KFM features with governance boundaries and the truth path zones.

> UNKNOWN until verified: the exact current repo structure on your branch.  
> Treat this as a target layout and reconcile with reality.

### Expanded layout

~~~text
Kansas-Frontier-Matrix/
├─ README.md
├─ LICENSE
├─ CONTRIBUTING.md
├─ SECURITY.md
├─ CODE_OF_CONDUCT.md
├─ CHANGELOG.md
│
├─ .github/
│  ├─ workflows/
│  ├─ ISSUE_TEMPLATE/
│  ├─ PULL_REQUEST_TEMPLATE.md
│  └─ CODEOWNERS
│
├─ docs/
│  ├─ adr/
│  ├─ governance/
│  ├─ runbooks/
│  ├─ guides/
│  ├─ stories/
│  ├─ investigations/
│  ├─ schemas/
│  ├─ standards/
│  └─ diagrams/
│
├─ contracts/
│  ├─ openapi/
│  ├─ schemas/
│  ├─ profiles/
│  └─ vocab/
│
├─ policy/
│  ├─ rego/
│  ├─ tests/
│  ├─ fixtures/
│  └─ bundles/
│
├─ data/
│  ├─ specs/
│  ├─ registry/
│  ├─ fixtures/
│  ├─ raw/
│  ├─ work/
│  ├─ quarantine/
│  ├─ processed/
│  ├─ catalog/
│  ├─ published/
│  └─ audit/
│
├─ apps/
│  ├─ api/
│  ├─ ui/
│  ├─ workers/
│  ├─ studio/
│  └─ cli/
│
├─ packages/
│  ├─ domain/
│  ├─ usecases/
│  ├─ adapters/
│  ├─ ingest/
│  ├─ indexers/
│  ├─ exports/
│  ├─ stories/
│  ├─ focus/
│  ├─ evidence/
│  ├─ catalog/
│  ├─ policy/
│  ├─ geo/
│  ├─ observability/
│  ├─ ui-components/
│  └─ shared/
│
├─ infra/
│  ├─ k8s/
│  ├─ helm/
│  ├─ terraform/
│  ├─ gitops/
│  └─ dashboards/
│
├─ tools/
│  ├─ validators/
│  ├─ linkcheck/
│  ├─ hash/
│  └─ generators/
│
├─ scripts/
│  ├─ promote/
│  ├─ lint/
│  ├─ rebuild/
│  ├─ dev/
│  └─ release/
│
├─ configs/
│  ├─ env/
│  ├─ pipelines/
│  ├─ ui/
│  └─ observability/
│
├─ migrations/
│  ├─ postgis/
│  └─ search/
│
├─ examples/
│  ├─ sample_dataset/
│  ├─ sample_story/
│  ├─ sample_policy/
│  └─ sample_focus/
│
└─ tests/
   ├─ unit/
   ├─ integration/
   ├─ e2e/
   └─ eval/
~~~

### Where CI gates live

- `.github/workflows/` — pipeline definition (lint/tests/policy/linkcheck/eval)
- `tools/` — deterministic validators/linkcheck tools used by CI and locally
- `contracts/` — schemas/profiles/vocab treated as production

Starter CI gate list:

- lint + typecheck
- unit tests
- validate DCAT/STAC/PROV
- linkcheck citations
- policy tests (default deny + fixtures)
- spec_hash drift check
- evidence resolver contract tests
- Focus Mode eval suite

[↑ Back to top](#kansas-frontier-matrix)

---

## Contributing

### What good looks like in KFM

- Every change is reversible, testable, and governed.
- Nothing user-visible ships without:
  - policy gates
  - resolvable citations
  - run receipts + audit refs
  - rights metadata

### Contribution paths

1) Dataset onboarding
- Add/update source registry entry
- Add dataset spec (`data/specs/<dataset_slug>.json`)
- Implement/adjust connector + normalization + validation
- Produce processed artifacts + catalogs
- Pass Promotion Contract gates
- Add layer config + evidence click behavior

2) Story authoring
- Use EvidenceRefs (not “trust me” claims)
- Verify citations resolve through the evidence resolver
- Respect policy labels + rights constraints
- Keep map state reproducible (saved view state)

3) Policy changes
- Default deny remains intact
- Update fixtures + tests
- Document rationale in an ADR
- Validate CI + runtime semantics remain aligned

### PR checklist

- [ ] No secrets or privileged tokens added
- [ ] Schemas and contracts updated when needed
- [ ] Policy fixtures/tests updated when needed
- [ ] Catalog validation + linkcheck passes
- [ ] Evidence resolver tests cover new EvidenceRefs
- [ ] Focus Mode eval passes (when applicable)
- [ ] For stories: all citations resolve and are policy-allowed

[↑ Back to top](#kansas-frontier-matrix)

---

## Security

### Threat model checklist

- TM-001: Any client access storage/DB directly? MUST be NO
- TM-002: Can public users infer restricted existence via error differences? MUST be NO
- TM-003: Are downloads/exports checked against policy labels + rights? MUST be YES
- TM-004: Can retrieved documents inject instructions that bypass policy? MUST be mitigated
- TM-005: Are citations verified and policy-filtered before synthesis? MUST be YES
- TM-006: Are outputs scanned for restricted patterns where required? SHOULD be YES
- TM-007: Are pipeline credentials least-privileged and rotated? MUST be YES
- TM-008: Are processed artifacts immutable by digest? MUST be YES
- TM-009: Are builds reproducible with provenance and SBOM? SHOULD be YES
- TM-010: Is the audit ledger append-only and access-controlled? MUST be YES
- TM-011: Are audit logs redacted where they could leak restricted data? MUST be YES

### Reporting

- Security contact: TBD (add an email/issue workflow)
- For vulnerabilities affecting policy, exports, or evidence resolution: treat as high severity and fail-closed.

[↑ Back to top](#kansas-frontier-matrix)

---

## Roadmap

Keep roadmaps small, reviewable, and reversible. Prefer glue artifacts (contracts, validators, manifests, runbooks) before expanding scope.

### Phase 0 — Foundations

- [ ] Promotion Contract gates implemented and enforced
- [ ] Catalog profiles + validators (DCAT/STAC/PROV)
- [ ] Evidence resolver contract + EvidenceBundle template
- [ ] Policy-as-code default deny + fixtures-driven tests
- [ ] Audit ledger + run receipts pipeline and Focus

### Phase 1 — Map Explorer MVP

- [ ] Evidence Drawer everywhere
- [ ] Dataset version + policy badges on all layers
- [ ] What changed comparison view policy-safe

### Phase 2 — Story Mode MVP

- [ ] Story Nodes with saved map state + versioning
- [ ] Publish gate all citations resolve + rights metadata present
- [ ] Review workflow steward + governance triggers

### Phase 3 — Focus Mode MVP

- [ ] Cite-or-abstain loop + citation verification gate
- [ ] Evaluation harness with golden queries + regression gate
- [ ] Prompt/model governance recorded in run receipts

### Phase 4 — Expand datasets safely

- [ ] Anchor dataset onboarding public-first
- [ ] Sensitive-location patterns restricted precise + public generalized derivatives
- [ ] Rights-aware archive integration metadata-first when needed

[↑ Back to top](#kansas-frontier-matrix)

---

## References

### Primary KFM specs

- KFM — Definitive Design and Governance Guide vNext (source-of-truth consolidation)
- KFM — Most Expansive Compendium vNext
- KFM — Grand Master Blueprint vNext

### Secondary reference library

- GIS + mapping: Mapping Urban Spaces; A Primer of GIS; Geostatistical Mapping; GIS in Sustainable Urban Planning
- Web + UI: Research-Based Web Design and Usability Guidelines; Using SVG with CSS3 and HTML5
- DevOps + pipelines: Docker GitOps OpenShift; Open Source Data Pipelines
- Security: Software Security Guide for Developers 2026 Edition

Reminder: KFM is evidence-first. Don’t add user-visible content that cannot be traced to catalogs + evidence bundles.

[↑ Back to top](#kansas-frontier-matrix)

---

<details>
<summary><strong>Appendix: Operational templates</strong></summary>

### Dataset onboarding Definition of Done

- [ ] Source registry entry exists (license/terms snapshot + sensitivity + cadence)
- [ ] Dataset spec exists and spec_hash is stable
- [ ] Acquisition manifest recorded; RAW artifacts checksummed
- [ ] WORK transforms recorded; failures quarantined
- [ ] PROCESSED artifacts produced with digests and stable paths
- [ ] DCAT/STAC/PROV generated and profile-valid
- [ ] Cross-links resolve; EvidenceRefs resolvable
- [ ] Policy label assigned; obligations documented
- [ ] QA report present; thresholds defined; pass/degraded/fail states supported
- [ ] Promotion manifest created; approvals captured
- [ ] Layer config created; evidence click behavior mapped to EvidenceRefs
- [ ] Rebuild scripts exist for projections from canonical artifacts

### Story publishing Definition of Done

- [ ] Narrative markdown includes EvidenceRefs for claims
- [ ] Saved map state included camera/layers/time/filters
- [ ] All citations resolve and are policy-allowed
- [ ] Rights metadata for embedded media present
- [ ] Policy label + review state assigned
- [ ] Publish event emits audit_ref + run receipt

### Focus Mode Definition of Done

- [ ] Policy pre-check blocks disallowed scopes/topics
- [ ] Retrieval is policy-filtered and returns only EvidenceBundles
- [ ] Every claim is grounded in resolvable citations
- [ ] Citation verifier is a hard gate
- [ ] Output scanning blocks restricted leakage patterns
- [ ] Run receipt emitted with model + prompt + bundle digests + output hash
- [ ] Eval harness exists with golden queries pinned to DatasetVersions

</details>
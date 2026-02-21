# Kansas Frontier Matrix
> **Map-first • Time-aware • Governed • Evidence-first • Cite-or-abstain**

**Status:** vNext — blueprint-driven build  
**Owners:** TBD (add GitHub handles)  
**Core promise:** anything you can see, cite, export, or ask KFM to explain is traceable to an immutable **DatasetVersion** + resolvable **EvidenceBundle**, with **policy enforced consistently in CI and at runtime**.  
**Primary experiences:** **Map Explorer** + **Timeline** + **Stories** + **Catalog** + **Discover** + **Focus Mode**.

[![Status](https://img.shields.io/badge/status-vNext-blue)](#)
[![Governance](https://img.shields.io/badge/governance-fail--closed-critical)](#)
[![Evidence](https://img.shields.io/badge/evidence-cite--or--abstain-important)](#)
[![Policy](https://img.shields.io/badge/policy-default--deny-critical)](#)
[![Catalog](https://img.shields.io/badge/catalog-DCAT%20%2B%20STAC%20%2B%20PROV-informational)](#)
[![License](https://img.shields.io/badge/license-TBD-lightgrey)](#)

---

## Quick navigation

[How to read this README](#how-to-read-this-readme) •
[Quick start](#quick-start) •
[System overview](#system-overview) •
[User journeys](#user-journeys) •
[Core invariants](#core-invariants) •
[Key concepts](#key-concepts) •
[Controlled vocabularies](#controlled-vocabularies) •
[Architecture](#architecture) •
[Governed API](#governed-api) •
[Truth path](#truth-path) •
[Promotion Contract](#promotion-contract) •
[Catalogs](#catalogs) •
[Canonical storage and rebuild strategy](#canonical-storage-and-rebuild-strategy) •
[Evidence and citations](#evidence-and-citations) •
[Map UX](#map-ux) •
[Stories](#stories) •
[Discover](#discover) •
[Focus Mode AI](#focus-mode-ai) •
[Governance](#governance) •
[Datasets and sources](#datasets-and-sources) •
[Repository layout](#repository-layout) •
[Contributing](#contributing) •
[Security](#security) •
[Roadmap](#roadmap) •
[References](#references) •
[Appendices](#appendices)

---

## How to read this README

> **NOTE**
> This README is both an engineering entrypoint and a governance artifact.  
> It uses the following scope tags:
>
> - **CONFIRMED:** in the vNext spec docs provided to this workspace.
> - **PROPOSED:** recommended design that still requires repo alignment and implementation.
> - **UNKNOWN:** requires repo inspection or governance decision.

> **RULE**
> If a behavior affects user-visible content, data access, exports, or narratives, treat it as governed: it must be testable, reviewable, and fail-closed.

[↑ Back to top](#kansas-frontier-matrix)

---

## Quick start

> **NOTE**
> Repo commands, package managers, and service topology may vary by branch.  
> If files referenced here are missing, treat those parts as **target conventions** and update to match repo reality.

### 1) Get oriented

~~~bash
git clone <REPO_URL>
cd Kansas-Frontier-Matrix
ls
~~~

### 2) Try common entrypoints

~~~bash
# If a Makefile exists
make help

# If Node/TypeScript
node -v && npm -v
npm install
npm test

# If Python
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

KFM is a governed knowledge system where the **map + timeline** are the primary interface. The system is trustworthy because every visible claim is grounded in:

- immutable **DatasetVersions**
- policy-evaluated, resolvable **EvidenceBundles**
- reproducible **run receipts** plus append-only **audit logging**
- strict catalogs (**DCAT + STAC + PROV**) that form the anti-hallucination substrate

### High-level flow

~~~mermaid
flowchart LR
  A[Upstream sources] --> B[Connectors and pipeline runner]
  B --> C[RAW zone]
  C --> D[WORK and QUARANTINE]
  D --> E[PROCESSED zone]
  E --> F[Catalog triplet DCAT STAC PROV]
  F --> G[Rebuildable projections DB Search Graph Tiles]
  F --> H[Governed API and evidence resolver]
  G --> H
  H --> I[UI Map Timeline Story Discover Focus]
  H --> J[Exports and reports]
~~~

### Trust membrane

- **Clients MUST NOT** access object storage or databases directly.
- Access flows through a **governed API** that applies **policy**, **evidence resolution**, **obligations**, and **audit logging** consistently.
- Backend domain logic **MUST NOT** bypass repository interfaces to talk directly to infrastructure.

[↑ Back to top](#kansas-frontier-matrix)

---

## User journeys

These journeys define what “done” means for the MVP.

1) **Explore**
- Browse layers and time.
- Click a feature.
- Open evidence drawer.
- See dataset version, policy badge, license, provenance.

2) **Compare**
- Choose DatasetVersion A vs B.
- See a policy-safe “what changed” diff report.
- Inspect changed artifacts and QA metrics.

3) **Narrate**
- Save a view state.
- Attach citations.
- Draft a Story Node.
- Submit for review and publish an immutable story version.

4) **Discover**
- Save a query.
- Save a map state without narrative.
- Create an investigation artifact or notebook output with citations.

5) **Ask**
- Run Focus Mode with view-state context.
- Get an answer with verified citations, or abstain.

6) **Export**
- Export a policy-allowed subset (and never bypass obligations).
- Export includes license/attribution and dataset version stamps.

[↑ Back to top](#kansas-frontier-matrix)

---

## Core invariants

These are KFM’s non-negotiables. Violations are governance failures, not just bugs.

| Invariant | Meaning | Enforcement |
|---|---|---|
| **Truth path** | Data moves Raw → Work/Quarantine → Processed → Published with promotion gates | Promotion Contract in CI + pipelines |
| **Trust membrane** | No direct client-to-storage/DB; domain never bypasses interfaces | Network policy + code structure + tests |
| **Evidence-first UX** | Evidence is a primary interaction everywhere | Evidence drawer is required UI surface |
| **Cite-or-abstain Focus Mode** | If citations cannot be verified, Focus Mode abstains | Citation verification hard gate + eval harness |
| **Canonical vs rebuildable** | Object storage + catalogs + audit ledger are canonical; DB/search/tiles are projections | Rebuild scripts + source-of-truth discipline |
| **Deterministic identity** | IDs are stable and digest-based | Spec hashing + hash drift checks |
| **Link integrity** | Every EvidenceRef resolves or the release fails | Link checker gate in CI |
| **Sensitive location defaults** | Restricted precise geometry stays restricted; public uses generalized derivatives | Policy + obligations + export rules |

> **Norms used in docs:** MUST / MUST NOT / SHOULD / MAY (RFC-style).  
> **Section tags:** CONFIRMED / PROPOSED / UNKNOWN.

[↑ Back to top](#kansas-frontier-matrix)

---

## Key concepts

Use these terms consistently in code, schemas, tests, and documentation.

| Term | Definition |
|---|---|
| **Dataset** | Logical dataset identity (e.g., “NOAA Storm Events”) |
| **DatasetSpec** | Config declaring how a dataset is acquired, normalized, validated, and produced |
| **Spec hash** | Digest of spec inputs used to generate DatasetVersion IDs and prevent drift |
| **DatasetVersion** | Immutable promoted output set (artifacts + catalogs + receipts) |
| **Artifact** | Concrete file/object produced by a run (GeoParquet, PMTiles, COG, JSONL, PDF…) |
| **EvidenceRef** | Stable reference using explicit schemes (dcat://, stac://, prov://, doc://, graph://) |
| **EvidenceBundle** | Resolved evidence view returned by evidence resolver (human card + machine metadata + digests + policy results) |
| **Promotion manifest** | Immutable manifest proving what was promoted, with digests and approvals |
| **Acquisition manifest** | Immutable manifest proving what was captured in RAW, with checksums and terms snapshots |
| **Story Node** | Versioned narrative bound to map state + citations + policy label + review state |
| **Discover artifact** | Saved query, saved map state, or investigation object with citations |
| **Policy label** | Primary sensitivity/access input used in auth and obligations |
| **Obligation** | Required transformation or UX notice (e.g., generalize geometry, add attribution notice) |
| **Run receipt** | Reproducible record of an operation (pipeline run, Focus query, publish event) |
| **Audit ledger** | Append-only governed record of operations and approvals |

[↑ Back to top](#kansas-frontier-matrix)

---

## Controlled vocabularies

Controlled vocabularies are inputs to gates and should be versioned like code.

### Starter vocabularies

| Vocabulary | Examples | Used by |
|---|---|---|
| `policy_label` | `public`, `public_generalized`, `restricted`, `restricted_sensitive_location`, `internal`, `embargoed`, `quarantine` | Policy, exports, UI badges, Focus Mode |
| `artifact_zone` | `raw`, `work`, `quarantine`, `processed`, `catalog`, `published` | Storage layout, promotion gates |
| `citation_kind` | `dataset`, `document`, `map_layer`, `story_node`, `run_receipt` | Evidence resolver, UI, Focus Mode |
| `review_state` | `draft`, `in_review`, `governance_review`, `published`, `withdrawn` | Stories and publishing |

> **RULE**
> If you add a new vocabulary value, add:
> - a fixture
> - a policy test
> - documentation
> - a migration note

[↑ Back to top](#kansas-frontier-matrix)

---

## Architecture

KFM keeps layers clean and enforces governance at boundaries.

### Clean layering

- **Domain**: pure domain models and rules
- **Use cases**: workflows (ingest dataset, promote dataset version, publish story node, answer Focus query)
- **Interfaces**: contracts (OpenAPI DTOs, schema registries, policy adapters, repository interfaces)
- **Infrastructure**: PostGIS, search, graph, object storage, CI, deployment

### Component decomposition

Start with a modular monolith so invariants are easier to enforce and test; split into services only when scaling demands it.

Core components:

1. Pipeline runner and connectors
2. Catalog generator and validators
3. Policy engine and fixtures
4. Evidence resolver
5. Governed API
6. UI surfaces
7. Index builders for projections

### Architecture diagram

~~~mermaid
flowchart TB
  subgraph Clients
    UI[UI Map Timeline Story Discover Focus]
    EXT[External clients]
  end

  subgraph Enforcement
    API[Governed API]
    POL[Policy engine]
    EV[Evidence resolver]
  end

  subgraph Canonical
    OBJ[Object storage artifacts]
    CAT[Catalogs DCAT STAC PROV]
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

The governed API is the only access path for clients. It is the enforcement boundary.

### Responsibilities

- Apply policy decisions and obligations
- Resolve EvidenceRefs to EvidenceBundles
- Serve projections (tiles/search/query) built from canonical artifacts
- Emit run receipts and audit entries for governed operations
- Fail-closed without leaking restricted existence via error differences

### Illustrative resource surface

> **PROPOSED**
> Exact endpoints depend on repo implementation. Treat this as a contract planning sketch.

| Resource | Purpose | Notes |
|---|---|---|
| `/datasets` | Discover datasets and versions | Policy-aware search and facets |
| `/datasets/{slug}/versions/{id}` | DatasetVersion detail | Includes catalogs and artifacts list |
| `/evidence/resolve` | EvidenceRef → EvidenceBundle | Must be usable in ≤ 2 UI calls |
| `/tiles/{layer}/{z}/{x}/{y}` | Tile serving | Policy and obligation aware |
| `/stories` | Story Node list and retrieval | Review state and policy visible |
| `/discover/saved-queries` | Saved queries | Reproducible filters |
| `/focus/query` | Focus Mode Q&A | Cite-or-abstain; emits run receipts |
| `/runs/{id}` | Run receipts | Links to prov activity/bundle |
| `/audit/{id}` | Audit entries | Restricted to authorized roles |

[↑ Back to top](#kansas-frontier-matrix)

---

## Truth path

KFM is map-first, but the map is only as trustworthy as the data lifecycle behind it.

### Data lifecycle zones

| Zone | Purpose | What belongs here |
|---|---|---|
| **RAW** | Immutable acquisition | Source snapshots + checksums + terms/license snapshots |
| **WORK** | Intermediate transforms | Normalization, QA, join steps |
| **QUARANTINE** | Failure and risk containment | Failed validations, unclear rights, sensitive-location review |
| **PROCESSED** | Publishable artifacts | Clean, validated, policy-ready outputs |
| **CATALOG** | Canonical metadata + lineage | DCAT + STAC + PROV + receipts + link validation |
| **PUBLISHED** | Governed runtime | Only promoted, policy-allowed content reaches UI and exports |

[↑ Back to top](#kansas-frontier-matrix)

---

## Promotion Contract

Promotion is the act of making something eligible for runtime surfaces. Promotion must fail-closed.

### Gate model

> **CONFIRMED in vNext spec docs**
> Promotion gates are enumerated and treated as CI-and-runtime enforceable requirements.

| Gate | Requirement | Must fail if | Example checks |
|---|---|---|---|
| A | Identity and versioning | DatasetVersion ID not deterministic or spec hash missing | hash drift test |
| B | Licensing and rights | License/terms snapshot missing or unclear | license presence + allowlist |
| C | Artifacts and digests | Missing artifacts or digests mismatch | sha256 verification |
| D | Catalog validation | DCAT/STAC/PROV invalid or missing required fields | profile validation |
| E | Cross-link integrity | EvidenceRefs do not resolve or catalogs not cross-linked | link checker |
| F | Policy and obligations | Policy label missing or obligations not applied | policy fixture tests |
| G | Audit and approvals | Missing run receipt, audit entry, or required approval | audit schema validation |

### Promotion manifest template

~~~json
{
  "kfm_promotion_manifest_version": "v1",
  "dataset_slug": "example_dataset",
  "dataset_version_id": "2026-02.abcd1234",
  "spec_hash": "sha256:abcd1234",
  "released_at": "2026-02-20T13:00:00Z",
  "artifacts": [
    { "zone": "processed", "path": "events.parquet", "digest": "sha256:2222", "media_type": "application/x-parquet" },
    { "zone": "processed", "path": "events.pmtiles", "digest": "sha256:3333", "media_type": "application/vnd.pmtiles" }
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
  ],
  "audit_ref": "kfm://audit/entry/123"
}
~~~

[↑ Back to top](#kansas-frontier-matrix)

---

## Catalogs

KFM’s catalogs are canonical. Projections are rebuildable.

### Catalog triplet responsibilities

- **DCAT**: dataset identity, licensing, distribution links, human discovery metadata
- **STAC**: spatial and temporal extents, assets by type, collection/item semantics for geodata
- **PROV**: lineage and activities; ties runs and outputs to inputs

### Cross-link rules

> **RULE**
> Catalogs must link to each other and to the promotion manifest so EvidenceRefs can resolve deterministically.

Recommended cross-links:

- DCAT `Dataset` ↔ STAC `Collection`
- STAC `Collection` ↔ PROV `Bundle` / `Activity`
- All catalogs ↔ promotion manifest and run receipt IDs

[↑ Back to top](#kansas-frontier-matrix)

---

## Canonical storage and rebuild strategy

Canonical storage is immutable by digest. DB/search/tiles/graph are rebuildable projections.

### Canonical object layout

> **PROPOSED**
> Choose one canonical layout and enforce it in tooling.

~~~text
object-store://kfm/
├─ raw/
│  └─ <dataset_slug>/
│     └─ <snapshot_id>/
│        ├─ source_payload.*
│        ├─ acquisition_manifest.json
│        └─ terms_snapshot.*
├─ work/
│  └─ <dataset_slug>/<run_id>/...
├─ quarantine/
│  └─ <dataset_slug>/<run_id>/...
├─ processed/
│  └─ <dataset_slug>/<dataset_version_id>/
│     ├─ *.parquet
│     ├─ *.pmtiles
│     ├─ *.tif
│     └─ checksums.json
├─ catalog/
│  └─ <dataset_slug>/<dataset_version_id>/
│     ├─ dcat.jsonld
│     ├─ stac/collection.json
│     └─ prov/bundle.jsonld
└─ receipts/
   └─ <run_id>.json
~~~

### Projections

| Projection | Purpose | Rebuild principle |
|---|---|---|
| DB | querying features fast | rebuild from processed GeoParquet |
| Search | discovery and text facets | rebuild from DCAT + derived summaries |
| Graph | relationship navigation | rebuild from PROV + curated edges |
| Tiles | map rendering | rebuild from processed artifacts |

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
- `url://...` (discouraged; snapshot into governed docs when possible)

### Evidence resolver contract

The evidence resolver accepts an EvidenceRef and returns an EvidenceBundle:

- human-readable card for UI
- machine metadata for validation
- digests and dataset version
- policy decision and obligations applied

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

The evidence drawer is a primary trust surface and MUST show at minimum:

- Evidence bundle ID and digest
- DatasetVersion ID and dataset title
- License and attribution
- Policy label and obligations applied
- Validation and QA summary
- Provenance chain and run receipt link
- Export controls allowed or denied with reason codes
- Audit reference for governed operations

[↑ Back to top](#kansas-frontier-matrix)

---

## Map UX

KFM’s UI is governed. It renders what the API returns and never embeds privileged credentials.

### Core surfaces

- **Map Explorer**: browse layers and time; inspect features; open evidence drawer; compare versions; export policy-safe views
- **Timeline**: time-window navigation and dataset version switching
- **Catalog**: dataset discovery with policy-aware search and facets
- **Discover**: saved queries, saved map states, investigations, notebook outputs
- **Admin Steward**: promotion queue, QA reports, review workflows

### Map state as a reproducible artifact

Map state captures:

- camera position
- active layers and style parameters
- time window
- filters

Story Nodes and Discover artifacts store map state so views replay deterministically.

[↑ Back to top](#kansas-frontier-matrix)

---

## Stories

Stories are governed publications bound to map state and citations.

### Story Node standards

A publishable Story Node must:

- declare scope
- separate observation claims from interpretive claims
- include citations for every factual claim
- include uncertainty notes where sources conflict
- include licensing and attribution for embedded media
- include policy label and review state

### Review workflow

> **PROPOSED workflow**
1. Draft: contributor drafts Story Node; citations must resolve in-editor.
2. Review: steward and historian/editor review claims, citations, sensitivity.
3. Governance review: triggered for Indigenous histories, restricted sites, sensitive locations.
4. Publish: Story Node becomes immutable; edits create a new version.

Publishing is blocked if:

- citations do not resolve
- rights are unclear for included media
- sensitive locations appear without policy approval

### Cultural sensitivity and Indigenous data sovereignty

Operational guidance:

- do not publish precise locations for culturally sensitive sites
- allow community-controlled policy labels and release criteria
- use public_generalized derivatives as the default public representation
- provide narrative context that respects community perspectives and avoids appropriation

If permissions are unclear, fail closed and flag for governance review.

[↑ Back to top](#kansas-frontier-matrix)

---

## Discover

Discover bridges casual exploration and formal investigations.

### Discover primitives

- Saved queries
- Saved map states
- Dataset compare view
- QA metrics dashboard

### Reproducible notebooks

> **PROPOSED**
Notebook requirements:

- every notebook references dataset_version_id for all inputs
- every chart includes a link to the evidence bundle or dataset version
- notebooks stored by digest and referenced in PROV as activities
- exported notebooks include citations and policy notices

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
  V -->|pass| E[Emit run receipt]
  V -->|fail| A[Abstain with policy-safe reason]
~~~

### Expectations

- Citations are mandatory. If citations cannot be verified, Focus Mode abstains.
- Every query emits a run receipt capturing model ID, prompt version, retrieval config version, policy engine version, inputs and outputs by digest, and output hash.
- Prompt/model changes are governed like code changes.

### Evaluation harness

Minimum release gates:

- citation coverage and resolvability
- correct abstention behavior
- leakage checks for restricted patterns
- golden query regression pinned to DatasetVersions

[↑ Back to top](#kansas-frontier-matrix)

---

## Governance

Governance becomes enforceable behavior through promotion gates, policy labels and obligations, access control, and append-only audit logging.

### Baseline roles

| Role | Responsibilities | Key powers |
|---|---|---|
| Public user | Read public layers/stories; Focus Mode limited to public evidence | None |
| Contributor | Propose datasets/stories; draft content; cannot publish | PRs/issues |
| Reviewer Steward | Approves promotions + story publishing; owns labels + redaction rules | Promotion and publish approvals |
| Operator | Runs pipelines and deployments; cannot override policy gates | Deploy/run jobs |
| Governance council | Controls culturally sensitive materials; defines restricted rules | Release criteria and constraints |

### Policy-as-code

- PDP: OPA or equivalent
- PEP:
  - CI gates
  - Runtime governed API
  - Evidence resolver
  - UI as renderer, not decider

### Governance playbooks

> **PROPOSED**
- Rights clearance playbook
- Partner data agreement playbook
- Sensitive location release playbook
- Story content governance playbook
- Appeals and corrections workflow

[↑ Back to top](#kansas-frontier-matrix)

---

## Datasets and sources

### Source selection rubric

Choose sources that:

- are authoritative and stable
- have clear licensing terms
- have well-defined coverage
- are useful for multiple story arcs
- can be represented with evidence and provenance

Avoid early sources that:

- have unclear reuse rights for media
- contain high-risk PII or sensitive coordinates without a generalization pathway
- require heavy scraping without clear permission

### Anchor dataset shortlist

Buildable vNext starter set:

- **Demographics:** IPUMS NHGIS (historical tables + boundaries)
- **Land:** BLM GLO land patents (public domain; names may be sensitive)
- **Hydrology:** USGS WaterData/NWIS (public domain)
- **Hazards:** NOAA Storm Events (public domain)
- **Disasters:** FEMA disaster declarations (public domain)
- **Basemap:** USGS National Map (public domain base layers)
- **Kansas GIS framework:** Kansas DASC Geoportal (state authoritative layers)

### Expandable dataset menu

> **PROPOSED**
Add datasets that support Kansas story arcs and analytics while meeting rights and sensitivity constraints.

**Kansas-specific candidates**
- Kansas Mesonet meteorology
- Reservoir and river conditions
- Water quality monitoring and station locations
- Kansas Geological Survey datasets
- Kansas land cover products
- Transportation and state GIS layers

**National candidates**
- Census TIGER/Line boundaries
- NHD hydrology layers
- Soils and land cover products
- Historic topo maps and imagery archives

### Source registry entry required

Every source must have a registry entry with:

- name and authority
- access method
- cadence
- license and terms snapshot
- sensitivity classification
- connector spec and credentials strategy
- known limitations and QA checks

The registry is an input to promotion gates.

### Integration playbook

Each source integration follows a repeatable playbook:

1. Source assessment
2. Acquisition design
3. Normalization design
4. Validation design
5. Output design
6. Catalog design
7. Policy design
8. UI integration
9. Focus Mode integration

[↑ Back to top](#kansas-frontier-matrix)

---

## Repository layout

> **UNKNOWN until verified**
> Current repo structure, naming conventions, modules, deployment environment, integrated datasets, and current policy pack state.

### Expanded reference layout

~~~text
Kansas-Frontier-Matrix/
├─ README.md
│
├─ docs/
│  ├─ adr/
│  ├─ governance/
│  ├─ runbooks/
│  ├─ stories/
│  ├─ investigations/
│  └─ schemas/
│
├─ contracts/
│  ├─ openapi/
│  ├─ schemas/
│  └─ profiles/
│
├─ policy/
│  ├─ rego/
│  ├─ tests/
│  └─ fixtures/
│
├─ data/
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
│  └─ workers/
│
├─ packages/
│  ├─ domain/
│  ├─ usecases/
│  ├─ adapters/
│  ├─ evidence/
│  ├─ catalog/
│  └─ shared/
│
├─ infra/
│  ├─ k8s/
│  ├─ helm/
│  └─ terraform/
│
├─ scripts/
│  ├─ promote/
│  ├─ lint/
│  ├─ rebuild/
│  └─ dev/
│
└─ tests/
   ├─ integration/
   └─ eval/
~~~

[↑ Back to top](#kansas-frontier-matrix)

---

## Contributing

### What good looks like

- Every change is reversible, testable, and governed.
- Nothing user-visible ships without policy gates, resolvable citations, audit receipts, and rights metadata.

### PR checklist

- [ ] No secrets committed
- [ ] Schemas and contracts updated
- [ ] Policy fixtures and tests updated
- [ ] Catalog validation and link-check passes
- [ ] Evidence resolver tests cover new EvidenceRefs
- [ ] Focus Mode eval harness passes
- [ ] Story citations resolve and are policy-allowed

[↑ Back to top](#kansas-frontier-matrix)

---

## Security

### Threat model checklist

- TM-001: Any client access storage/DB directly? MUST be NO
- TM-002: Can public users infer restricted existence via error differences? MUST be NO
- TM-003: Are downloads and exports checked against labels and rights? MUST be YES
- TM-004: Can retrieved docs inject instructions that bypass policy? MUST be mitigated
- TM-005: Are citations verified and policy-filtered before synthesis? MUST be YES
- TM-006: Are outputs scanned for restricted patterns where required? SHOULD be YES
- TM-007: Are pipeline credentials least-privileged and rotated? MUST be YES
- TM-008: Are artifacts immutable by digest? MUST be YES
- TM-009: Are builds reproducible with SBOM and provenance? SHOULD be YES
- TM-010: Is audit ledger append-only and access-controlled? MUST be YES

[↑ Back to top](#kansas-frontier-matrix)

---

## Roadmap

> Keep roadmaps small, reviewable, and reversible. Prefer contracts and validators before expanding scope.

### Phase 0 Foundations

- [ ] Spec hashing and controlled vocabulary library
- [ ] Catalog validators and link checker
- [ ] Policy pack and fixture tests
- [ ] Evidence resolver service
- [ ] Dataset registry and discovery endpoints
- [ ] Audit ledger and run receipts

### Phase 1 Map Explorer baseline

- [ ] Evidence drawer everywhere
- [ ] Version and policy badges on layers
- [ ] Dataset comparison and diff reports

### Phase 2 Story Mode baseline

- [ ] Story Nodes with saved map state
- [ ] Publish gate: citations resolve and rights present
- [ ] Review workflow and governance triggers

### Phase 3 Focus Mode baseline

- [ ] Cite-or-abstain loop
- [ ] Evaluation harness with golden queries
- [ ] Prompt/model governance in receipts

[↑ Back to top](#kansas-frontier-matrix)

---

## References

### Primary KFM specs

- KFM Most Expansive Compendium vNext (2026-02-21)
- KFM Unified Technical Blueprint
- KFM Unified Technical Blueprint and Supporting Ideas

### Secondary reference library

**GIS and mapping**
- Mapping Urban Spaces
- The Map Reader
- A Primer of GIS Fundamental Geographic and Cartographic Concepts
- A Practical Guide to Geostatistical Mapping
- GIS in Sustainable Urban Planning and Management
- Archaeological 3D GIS
- Earth, Space, and Environmental Science Explorations with ArcGIS Pro
- Google Earth Engine Applications

**Web and UI**
- Research-Based Web Design and Usability Guidelines
- Using SVG with CSS3 and HTML5
- Everything You Know About CSS Is Wrong
- The Ultimate HTML Reference
- The Book of JavaScript
- Build Your First Web App
- Fullstack React
- ReactJS by Example
- SurviveJS Webpack and React

**APIs and fullstack**
- Node.js GraphQL
- Fullstack GraphQL Applications with GRANDstack
- Programming TypeScript
- TypeScript AngularJS FullStack
- Pro MERN Stack Development Express

**DevOps and pipelines**
- Docker GitOps OpenShift
- Data Pipelines OpenShift Podman Kubernetes Git
- Open Source Data Pipelines Red Hat Developer
- Podman in Action
- From Containers to Kubernetes with Node

**Security and engineering**
- Software Design
- Software Security Guide for Developers 2026 Edition Expanded Sections
- Test Driven Development with Python
- Practical Guide to Pandas for Data Science
- Data Mining Concepts and Applications
- Reverse Engineering of Real Time System Models from Event Trace Recordings

**Other technical references**
- Developing Graphics Frameworks with Python and OpenGL
- Programming 3D Applications with HTML5 and WebGL
- VLSI Physical Design From Graph Partitioning to Timing Closure
- Applications of MATLAB in Science and Engineering
- Professional Markdown Guide for GitHub Documentation

[↑ Back to top](#kansas-frontier-matrix)

---

## Appendices

<details>
<summary><strong>Appendix A: Operational Definition of Done templates</strong></summary>

### Dataset onboarding Definition of Done

- [ ] Source registry entry exists
- [ ] Acquisition manifest recorded and RAW checksummed
- [ ] WORK transforms recorded and failures quarantined
- [ ] PROCESSED artifacts produced with digests
- [ ] DCAT/STAC/PROV generated and profile-valid
- [ ] Cross-links resolve and EvidenceRefs resolvable
- [ ] Policy label assigned and obligations documented
- [ ] QA report present with thresholds and status
- [ ] Promotion manifest created and approvals captured
- [ ] Layer config created and evidence click mapped
- [ ] Rebuild scripts exist for projections

### Story publishing Definition of Done

- [ ] Narrative uses EvidenceRefs for claims
- [ ] Saved map state included
- [ ] Citations resolve and are policy-allowed
- [ ] Rights metadata present for media
- [ ] Policy label and review state assigned
- [ ] Publish emits audit ref and run receipt

</details>

<details>
<summary><strong>Appendix B: KFM MetaBlock v2 template</strong></summary>

> **KFM MetaBlock**
> - MetaBlockVersion: v2  
> - Purpose: <one sentence>  
> - Status: draft | in_review | published  
> - Owners: <role or handles>  
> - Scope: <what the artifact governs>  
> - Provenance: <links to datasets, receipts, ADRs>  
> - Policy: <policy label, obligations, constraints>  
> - LastReviewed: <YYYY-MM-DD>  
> - ChangeControl: <PR required, approvals required>  

</details>

<details>
<summary><strong>Appendix C: Map state schema sketch</strong></summary>

~~~json
{
  "kfm_map_state_version": "v1",
  "camera": { "bbox": [-102.0, 36.9, -94.6, 40.0], "zoom": 6 },
  "time_window": { "start": "1930-01-01", "end": "1939-12-31" },
  "layers": [
    { "layer_id": "noaa_storm_events", "dataset_version_id": "2026-02.abcd1234", "style": "default" }
  ],
  "filters": [
    { "layer_id": "noaa_storm_events", "expr": "event_type in ('Drought','Flood')" }
  ]
}
~~~

</details>

<details>
<summary><strong>Appendix D: Layer configuration schema sketch</strong></summary>

~~~json
{
  "kfm_layer_config_version": "v1",
  "layer_id": "noaa_storm_events",
  "title": "NOAA Storm Events",
  "dataset_slug": "noaa_storm_events",
  "dataset_version_id": "2026-02.abcd1234",
  "source": { "type": "pmtiles", "href": "processed/noaa_storm_events/2026-02.abcd1234/events.pmtiles" },
  "evidence": { "click_ref_template": "stac://noaa_storm_events/2026-02.abcd1234/items/{feature_id}" },
  "policy": { "default_label": "public", "obligations": [] }
}
~~~

</details>

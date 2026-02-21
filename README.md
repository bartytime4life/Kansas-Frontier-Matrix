# Kansas Frontier Matrix (KFM)

> **Map-first • Time-aware • Governed • Evidence-first • Cite-or-abstain**

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

[Quick start](#quick-start) •
[System overview](#system-overview) •
[Core invariants](#core-invariants) •
[Key concepts](#key-concepts) •
[Architecture](#architecture) •
[Truth path and promotion contract](#truth-path-and-promotion-contract) •
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

## Quick start

> **NOTE**
> This repository’s exact commands / package managers / service topology may vary by branch.
> If you don’t find the files referenced here, treat those sections as **target conventions** and update the README to match the repo reality.

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

# if it’s a Node/TypeScript workspace
npm -v && node -v
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

KFM is a governed knowledge system where the **map + timeline** are the primary interface. The system is trustworthy because every visible claim is grounded in:

- immutable **DatasetVersions**
- policy-evaluated, resolvable **EvidenceBundles**
- reproducible **run receipts** + append-only **audit logging**
- strict catalogs (**DCAT + STAC + PROV**) that form the “anti-hallucination substrate”

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
  H --> I[UI Map Story Focus]
  H --> J[Exports and reports]
~~~

### “Trust membrane” (enforcement boundary)

- **Clients MUST NOT** access object storage / DB directly.
- Access flows through a **governed API** that applies **policy**, **evidence resolution**, **redaction obligations**, and **audit logging** consistently.
- Backend domain logic **MUST NOT** bypass repository interfaces to talk directly to infrastructure.

[↑ Back to top](#kansas-frontier-matrix-kfm)

---

## Core invariants

These are KFM’s “non-negotiables.” If we violate them, we don’t merely have bugs—we break governance.

### Invariants (what must always be true)

| Invariant | Meaning | How it’s enforced |
|---|---|---|
| **Truth path** | Data moves through zones (Raw → Work/Quarantine → Processed → Published) with promotion gates | Promotion Contract gates (CI + pipeline) |
| **Trust membrane** | No direct client-to-storage/DB; domain logic never bypasses interfaces | Network controls + code structure + tests |
| **Evidence-first UX** | Evidence is not optional “details”—it’s a primary interaction everywhere | Evidence Drawer required + UI gating |
| **Cite-or-abstain Focus Mode** | If citations cannot be verified, Focus Mode abstains | Citation verification hard gate + eval harness |
| **Canonical vs rebuildable** | Object storage + catalogs + audit ledger are canonical; DB/search/tiles are projections | Rebuild scripts + “source of truth” discipline |
| **Deterministic identity** | DatasetVersion IDs and artifact addresses are stable and digest-based | Canonical hashing + “hash drift” checks |

> **Norms used in docs:** MUST / MUST NOT / SHOULD / MAY (RFC-style).  
> **Section tags:** CONFIRMED / PROPOSED / UNKNOWN (repository + governance dependent).

[↑ Back to top](#kansas-frontier-matrix-kfm)

---

## Key concepts

Use these terms consistently in code, schemas, tests, and documentation.

| Term | Definition (KFM meaning) |
|---|---|
| **Dataset** | A logical dataset identity (e.g., “NOAA Storm Events”) |
| **DatasetVersion** | An immutable version corresponding to a specific promoted output set |
| **Artifact** | A concrete file/object produced by a run (GeoParquet, PMTiles, COG, JSONL, PDF…) |
| **EvidenceRef** | A stable reference to evidence using explicit schemes (dcat://, stac://, prov://, doc://, graph://) |
| **EvidenceBundle** | Resolved evidence view returned by the evidence resolver (human card + machine metadata + digests + policy results) |
| **Story Node** | Versioned narrative bound to map state + citations + policy label + review state |
| **Policy label** | Primary sensitivity/access input used in authorization and obligations |
| **Obligation** | A required transformation or UX notice (e.g., geometry generalized) |
| **Run receipt** | Reproducible record of an operation (pipeline run / Focus query / publish event) |
| **Audit ledger** | Append-only governed record of operations and approvals |

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

[↑ Back to top](#kansas-frontier-matrix-kfm)

---

## Truth path and promotion contract

KFM is “map-first,” but the map is only as trustworthy as the data lifecycle behind it.

### Data lifecycle zones (truth path)

| Zone | Purpose | What belongs here |
|---|---|---|
| **RAW** | Immutable acquisition | Source snapshots + checksums + terms/license snapshots |
| **WORK / QUARANTINE** | Intermediate transforms | Normalization, QA, redaction candidates, failure quarantine |
| **PROCESSED** | Publishable artifacts | Cleaned, validated, policy-ready outputs (still not user-facing until promoted) |
| **CATALOG / TRIPLET** | Canonical metadata + lineage | DCAT + STAC + PROV + run receipts + link validation |
| **PUBLISHED** | Governed runtime | Only what’s safe and promotable reaches UI/Future exports |

### Promotion Contract (fail-closed gates)

Promotion is the act of moving from Raw/Work into Processed + Catalog/Lineage, and therefore into runtime surfaces.

**Minimal gates (starter):**
- **Identity & versioning:** deterministic DatasetVersion ID; promotion manifest exists
- **Artifacts:** processed artifacts exist; each has digest; predictable paths; media types recorded
- **Catalogs:** DCAT/STAC/PROV schema-valid under profiles
- **Cross-links:** all links resolve; EvidenceRefs resolve
- **Policy:** policy_label assigned; obligations applied; default-deny tests pass
- **QA:** validation reports present; failures quarantined
- **Audit:** run receipt emitted; append-only audit entry; approvals captured if required

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
  V -->|pass| E[Emit run receipt]
  V -->|fail| A[Abstain with policy-safe reason]
~~~

### Expectations

- **Citations are mandatory.** If citations cannot be verified, the correct behavior is to **abstain**.
- Every query emits a **run receipt** capturing model identifier, prompt version, retrieval config version, policy engine version, inputs/outputs by digest, and an output hash.
- Prompt/model changes are treated like code changes and require review + evaluation harness pass.

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

> **Suggested semantics (PROPOSED):**
> - Prefer **public_generalized** over “just denying everything” when a safe generalized representation is possible.
> - Default deny for sensitive-location and restricted datasets; never leak restricted existence via error differences.
> - Do not embed precise coordinates in Story Nodes or Focus outputs unless policy explicitly allows.

### Policy-as-code (recommended pattern)

- Policy Decision Point (PDP): OPA or equivalent
- Policy Enforcement Points (PEP):
  - CI: schema validation + policy tests block merges
  - Runtime API: policy checks before serving data
  - Evidence resolver: policy checks before resolving and rendering bundles
  - UI: shows policy badges/notices; never decides

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

- **Demographics:** IPUMS NHGIS (historical tables + boundaries)
- **Land:** BLM GLO land patents (public domain; names may be sensitive)
- **Hydrology:** USGS WaterData/NWIS (public domain)
- **Hazards:** NOAA Storm Events (public domain)
- **Disasters:** FEMA disaster declarations (public domain)
- **Basemap:** USGS National Map (public domain base layers)
- **Kansas GIS framework:** Kansas DASC Geoportal (state authoritative layers)

For archives with reuse constraints:
- Kansas Memory / Kansas Historical Society collections: treat as **metadata-first** until rights are cleared; mirror only what is allowed.

For sensitive heritage layers:
- archaeology sites and restricted heritage inventories: store precise geometry **restricted**; publish generalized derivatives or metadata-only records.

### Source registry entry (required)

Every source must have a registry entry with:
- name and authority
- access method (API/bulk/scrape/manual)
- cadence
- license/terms snapshot
- sensitivity classification
- connector spec + credentials strategy
- known limitations + QA checks

[↑ Back to top](#kansas-frontier-matrix-kfm)

---

## Repository layout

> **UNKNOWN until verified:** current repo structure, naming conventions, existing modules, deployment environment, which datasets are integrated, and the current policy bundle state.

### Proposed layout (reference)

~~~text
Kansas-Frontier-Matrix/
├─ README.md                                     # Project entrypoint (what KFM is + quickstart + key links)
│
├─ docs/                                         # Governance + engineering docs (human-facing)
│  ├─ adr/                                       # Architecture Decision Records (why choices were made)
│  ├─ governance/                                # Policy labels, obligations, review workflows, rubrics
│  ├─ runbooks/                                  # Operational procedures (oncall, incidents, backups, upgrades)
│  ├─ stories/                                   # Story templates/examples (if stored in-repo)
│  └─ schemas/                                   # Human-readable schema docs (if not maintained under contracts/)
│
├─ contracts/                                    # Machine-enforced contracts (CI gates + runtime boundaries)
│  ├─ openapi/                                   # OpenAPI contract(s) (REST boundary)
│  ├─ schemas/                                   # JSON Schemas (DTOs, manifests, configs, receipts)
│  └─ profiles/                                  # DCAT/STAC/PROV profile constraints + validators
│
├─ policy/                                       # OPA/Rego policy system (default-deny; explicit allow)
│  ├─ rego/                                      # Policy-as-code (authoritative rules)
│  ├─ tests/                                     # Policy tests (unit/regression/golden)
│  └─ fixtures/                                  # Allow/deny + obligation fixtures (synthetic/redacted; deterministic)
│
├─ data/                                         # Canonical artifacts or pointers (repo-dependent; governed zones)
│  ├─ raw/                                       # Immutable captures/manifests (never served)
│  ├─ work/                                      # Intermediates + receipts/validation (regeneratable; never served)
│  ├─ processed/                                 # Publishable artifacts (immutable per version)
│  ├─ catalog/                                   # Machine-readable catalogs (DCAT/STAC/PROV; cross-linked)
│  ├─ published/                                 # Published releases/exports (if tracked in-repo)
│  └─ audit/                                     # Audit checkpoints (if stored in-repo; often external in prod)
│
├─ src/                                          # Runtime code (services, pipelines, adapters)
│  ├─ api/                                       # Governed endpoints (routes/DTOs/auth/policy boundary)
│  ├─ evidence/                                  # Evidence resolver (citations → artifacts; policy-filtered)
│  ├─ policy/                                    # Policy adapter + reason codes (OPA client/wrapper)
│  ├─ catalog/                                   # Catalog parsers/validators/linters (STAC/DCAT/PROV)
│  ├─ ingest/                                    # Connectors + runner (acquire/discover/normalize/emit)
│  ├─ indexers/                                  # Rebuildable projections (DB/search/tiles; deterministic)
│  └─ ui/                                        # Frontend (only if monorepo; otherwise lives in top-level web/)
│
├─ tests/                                        # Test suites (repo-wide)
│  ├─ integration/                               # Integration tests (service-backed)
│  └─ eval/                                      # Focus Mode evaluation harness (gold sets + expectations)
│
└─ scripts/                                      # Operational wrappers (CI/local parity)
   ├─ promote/                                   # Promotion/publish entrypoints (fail-closed; emits receipts)
   ├─ lint/                                      # Lint/validate entrypoints (docs, schemas, policy, catalogs)
   └─ rebuild/                                   # Rebuild projections (indexes, tiles, caches) with runbooks
~~~

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
- TM-006: Are outputs scanned for restricted patterns (coords/PII) where required? **SHOULD be YES**
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

**Primary KFM specs (vNext):**
- *KFM — Grand Master Blueprint & Governance Compendium* (2026-02-21)
- *KFM — Definitive Design & Governance Guide* (2026-02-20)
- *KFM — Ultimate Blueprint (Draft)* (2026-02-20)

**Secondary reference library (provided PDFs, consolidated list):**
- **GIS + mapping + cartography**
  - *Mapping Urban Spaces*
  - *Archaeological 3D GIS*
  - *The Map Reader: Theories of Mapping Practice and Cartographic Representation*
  - *A Primer of GIS: Fundamental Geographic and Cartographic Concepts*
  - *A Practical Guide to Geostatistical Mapping (2nd ed.)*
  - *GIS in Sustainable Urban Planning and Management: A Global Perspective*
  - *Earth, Space, and Environmental Science Explorations with ArcGIS Pro (ed2)*

- **Remote sensing / cloud geospatial**
  - *Google Earth Engine Applications*

- **Web + UX + documentation**
  - *Research-Based Web Design & Usability Guidelines*
  - *Professional Markdown Guide for GitHub Documentation*
  - *Using SVG with CSS3 and HTML5*
  - *The Ultimate HTML Reference*
  - *Everything You Know About CSS Is Wrong*
  - *The Book of JavaScript: A Practical Guide to Interactive Web Pages*
  - *Build Your First Web App: Learn to Build Web Applications from Scratch*

- **JavaScript / TypeScript / Full-stack**
  - *Programming TypeScript*
  - *TypeScript-AngularJS-FullStack*
  - *Node.js-GraphQL*
  - *Fullstack GraphQL Applications with GRANDstack*
  - *Fullstack React: The Complete Guide to ReactJS and Friends*
  - *ReactJS by Example*
  - *SurviveJS — Webpack and React*
  - *Pro MERN Stack Development (Mongo, Express, React, Node)*

- **DevOps + pipelines + Kubernetes**
  - *Docker GitOps OpenShift*
  - *Data Pipelines: OpenShift / Podman / Kubernetes / Git*
  - *Open Source Data Pipelines for Intelligent Applications*
  - *Podman in Action*
  - *From Containers to Kubernetes with Node.js*

- **Security + software engineering**
  - *Software Security Guide for Developers (2026 Edition) — Expanded Sections*
  - *Software Design*

- **Data science**
  - *Practical Guide to Pandas for Data Science*
  - *Data Mining — Concepts and Applications*
  - *Applications of MATLAB in Science & Engineering*

- **Graphics + 3D**
  - *Programming 3D Applications with HTML5 and WebGL*
  - *Developing Graphics Frameworks with Python and OpenGL*

- **Other engineering reference**
  - *Reverse Engineering of Real-Time System Models from Event Trace Recordings*
  - *VLSI Physical Design: From Graph Partitioning to Timing Closure*
  - *Test-Driven Development with Python (Obey the Testing Goat)*

> **Reminder:** KFM is evidence-first. Don’t add user-visible content that cannot be traced to catalogs + evidence bundles.

[↑ Back to top](#kansas-frontier-matrix-kfm)

---

<details>
<summary><strong>Appendix: Operational templates (starter)</strong></summary>

### Dataset onboarding “Definition of Done” (starter)

- [ ] Source registry entry exists (license/terms snapshot + sensitivity + cadence)
- [ ] Acquisition manifest recorded; RAW artifacts checksummed
- [ ] WORK/QUARANTINE transforms recorded; failures quarantined
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

</details>
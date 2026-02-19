<!--
KFM-META (v1)
{
  "kfmDocID": "kfm:doc:architecture:kfm_full_design_and_engineering_plan",
  "title": "KFM Full Design & Engineering Plan (Linux-first, Cloud-ready)",
  "docKind": "universal_doc",
  "version": "0.1-draft",
  "created": "2026-02-18",
  "status": "draft",
  "governance": {
    "sensitivity": "public",
    "license": "CC-BY-4.0",
    "requiresReview": true,
    "trustMembrane": true,
    "evidenceFirst": true,
    "fairCareAligned": true
  },
  "sourceBasis": [
    {"title":"KFM_Masterpiece_Vision.pdf","generated":"2026-02-16"},
    {"title":"Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf","note":"repo structure + service architecture"},
    {"title":"KFM-Bluprint-&-Ideas.pdf","note":"policy-as-code + evidence resolver + Focus Mode constraints"},
    {"title":"MARKDOWN_GUIDE_v13.md.gdoc","note":"legacy YAML-frontmatter validation to be replaced"},
    {"title":"Podman in Action - podman-action.pdf","note":"Linux-first container runtime practices"},
    {"title":"Docker-GitOps-OpenShift.pdf","note":"GitOps repo structure patterns"},
    {"title":"Software Security Guide for Developers (2026 Edition) – Expanded Sections.pdf","note":"web token storage guidance"}
  ],
  "canonicalMetaHash": "TBD_by_ci",
  "links": {
    "schema_doc_meta": "schemas/docs/kfm_doc_meta.schema.json",
    "validator": "tools/docs/validate_docs.py"
  }
}
KFM-META-END
-->

# Kansas Frontier Matrix (KFM) — Full Design & Engineering Plan  
**Linux-first host → Cloud-scale provider (Kubernetes/OpenShift GitOps)**  
**Goal:** This document is buildable: a senior engineer should be able to implement KFM from scratch using only this plan + referenced standards.

> **Design posture:** Evidence-first, policy-gated, audit-ready. “Abstain is a feature.”  
> **Trust membrane:** UI/external clients never access databases directly.

---

<details>
<summary><strong>📌 Metadata Capsule (Human View)</strong></summary>

| Field | Value |
|---|---|
| Doc ID | `kfm:doc:architecture:kfm_full_design_and_engineering_plan` |
| Kind | `universal_doc` |
| Version | `0.1-draft` |
| Created | `2026-02-18` |
| Status | Draft |
| Runtime targets | Single Linux host (Podman/Docker), then Kubernetes/OpenShift |
| Non-negotiables | Trust membrane, fail-closed policy, cite-or-abstain, audit ledger |
| Output contract | Governed APIs + resolvable evidence links |

</details>

---

## 1) Non-Negotiables (System Guarantees)

These are system-level invariants. If any are violated, KFM is *not* KFM.

- **Trust membrane:** No UI or external client can talk to PostGIS/Neo4j/Search/Object store directly. All access is via the governed API boundary.
- **Fail-closed governance:** If policy is negative/unknown/unreachable → deny by default.
- **Truth path lifecycle:** **Raw → Work → Processed**, with **promotion gates**.
- **Mandatory metadata triad for publication:** **STAC + DCAT + PROV** always accompanies any published artifact.
- **Focus Mode “cited analyst”:** Retrieval-only from governed artifacts; must **cite or abstain**; every response emits an **audit reference**.
- **Auditability:** Every significant interaction (including Focus Mode) is logged with correlation IDs and is reviewable.

---

## 2) System Overview (Architecture)

### 2.1 The KFM “Truth Path” (End-to-End)

```mermaid
flowchart LR
  subgraph Sources["Data Sources"]
    S1[Archives/PDFs]
    S2[Open Data / Shapefiles]
    S3[Remote sensing / time series]
    S4[Partner feeds]
  end

  subgraph Ingest["Ingestion Plane (Governed Pipelines)"]
    P1[Ingest + Snapshot Raw]
    P2[Validate + Normalize]
    P3[Transform + Enrich]
    P4[QA Gates + Receipts]
    P5[Promote to Processed]
  end

  subgraph Artifacts["Artifacts + Metadata"]
    R[(Raw)]
    W[(Work)]
    PR[(Processed)]
    STAC[(STAC)]
    DCAT[(DCAT)]
    PROV[(PROV)]
    RECEIPT[(Run Receipt)]
  end

  subgraph Stores["Storage Plane"]
    PG[(PostGIS)]
    G[(Neo4j)]
    IDX[(Search/Vector Index)]
    OBJ[(Object Store)]
  end

  subgraph API["Governed API Plane"]
    GW[API Gateway / FastAPI]
    OPA[OPA Policy Engine]
    EV[Evidence Resolver]
    AI[Focus Mode (RAG Orchestrator)]
  end

  subgraph UX["Product Plane"]
    UI[React + MapLibre/Cesium]
    SN[Story Nodes]
    AUD[Audit/Explain Panel]
  end

  S1-->P1
  S2-->P1
  S3-->P1
  S4-->P1

  P1-->R-->P2-->W-->P3-->P4-->P5-->PR
  P5-->STAC
  P5-->DCAT
  P5-->PROV
  P5-->RECEIPT

  PR-->PG
  PR-->G
  STAC-->IDX
  DCAT-->IDX
  PROV-->IDX
  PR-->OBJ

  UI-->GW
  GW-->OPA
  GW-->PG
  GW-->G
  GW-->IDX
  GW-->OBJ
  GW-->EV
  UI-->AI
  AI-->GW
  UI-->AUD
  SN-->GW
```

### 2.2 Component List (Buildable Services)

**Backend services**
- `kfm-api` (FastAPI): REST-first; optional GraphQL as a façade (same service layer).
- `kfm-policy` (OPA): Rego policies, used in CI and runtime.
- `kfm-ingest` (pipeline runner): containerized ETL jobs for each dataset connector.
- `kfm-search` (indexer): builds text + vector indices from catalogs + docs.
- `kfm-audit` (append-only ledger writer): JSONL + signed digests (or DB append log).
- `kfm-evidence` (resolver): resolves `prov://`, `stac://`, `dcat://`, `doc://`, `graph://` refs.

**Stores**
- PostGIS: canonical spatial/temporal features and derived layers.
- Neo4j: lineage + narrative graph (entities/events/relations).
- Search index: free-text + metadata + embeddings for retrieval.
- Object store: big artifacts (COG, GeoParquet, PMTiles, documents, receipts, catalogs).

**Frontend**
- React + MapLibre (vector) + Cesium (3D optional)
- Focus Mode chat panel + citations drawer + audit/explain panel
- Story Node reader/editor (governed authoring)

---

## 3) Repository Structure (Monorepo, Governed)

> Principle: governance artifacts are first-class. Keep standards + schemas + policies versioned next to code.

```text
kfm/
├─ docs/
│  ├─ standards/               # Governance standards (FAIR/CARE, licensing, sensitivity)
│  ├─ templates/               # Universal Doc / Story Node templates (metadata capsule)
│  ├─ architecture/            # System diagrams + ADRs
│  └─ runbooks/                # Ops, incident response, backup/restore
├─ schemas/
│  ├─ docs/                    # JSON Schemas for doc metadata capsules
│  ├─ catalog/                 # STAC/DCAT/PROV profiles (schemas + profiles)
│  └─ receipts/                # run_receipt + attestation schemas
├─ policy/
│  ├─ rego/                    # OPA policies
│  └─ conftest/                # CI policy tests + fixtures
├─ data/
│  ├─ raw/                     # Immutable source snapshots
│  ├─ work/                    # Intermediates (reproducible)
│  └─ processed/               # Canonical publishable outputs
├─ catalogs/
│  ├─ stac/
│  ├─ dcat/
│  └─ prov/
├─ src/
│  ├─ api/                     # FastAPI app (Clean Architecture)
│  ├─ pipelines/               # ETL jobs + validators + receipts
│  ├─ search/                  # indexing + retrieval
│  └─ ui/                      # React web app
├─ infra/
│  ├─ local/                   # podman/compose + systemd
│  └─ gitops/                  # kustomize/helm overlays + argo/flux configs
├─ tools/
│  ├─ docs/                    # doc validators + metadata extractor
│  ├─ catalogs/                # stac/dcat/prov tooling
│  ├─ receipts/                # receipt signer/verifier
│  └─ dev/                     # local helper scripts
└─ .github/workflows/          # CI checks (lint, schema, policy, tests, build)
```

---

## 4) Clean Architecture Boundaries (Trust Membrane Friendly)

### 4.1 Backend Layering

**Domain layer (`src/api/domain/`)**  
Pure models (no DB, no HTTP). Examples:
- `Dataset`, `DatasetVersion`, `Asset`, `Feature`, `Event`, `Place`, `StoryNode`, `Citation`, `EvidenceRef`
- `PolicyDecision`, `SensitivityClass`, `License`
- `RunReceipt`, `ProvenanceActivity`

**Use Case / Service layer (`src/api/usecases/`)**  
Workflows:
- `PublishDatasetVersion`
- `ResolveEvidenceRef`
- `SearchKFM`
- `AnswerQuestionWithCitations` (Focus Mode)
- `GetStoryNode`, `ListStoryNodes`, `PublishStoryNode`

**Ports / Contracts (`src/api/ports/`)**  
Interfaces the usecases call:
- `DatasetRepository`, `GraphRepository`, `SearchRepository`, `ObjectStore`, `PolicyEngine`, `AuditLedger`

**Adapters / Infrastructure (`src/api/infra/`)**
- PostGIS impl, Neo4j impl, OpenSearch/Meili impl, S3/MinIO impl
- OPA adapter (HTTP or embedded)
- Audit sink (JSONL + signature; or DB append table)

### 4.2 Frontend Trust Membrane Rule

Frontend can only:
- call `kfm-api` endpoints
- render artifacts returned by `kfm-api` (already policy-checked)
- resolve citations via `kfm-api` evidence resolver
- never fetch object store URLs unless they’re pre-signed + policy-approved by the API

---

## 5) Data Lifecycle & Pipelines (Raw → Work → Processed)

### 5.1 Canonical Artifact Set per Dataset Version

For each `dataset_id@version`, produce:
- `data/processed/<dataset_id>/<version>/...` (GeoParquet/COG/PMTiles as appropriate)
- `catalogs/stac/<dataset_id>/<version>/...`
- `catalogs/dcat/<dataset_id>/<version>.jsonld`
- `catalogs/prov/<dataset_id>/<version>.jsonld`
- `receipts/<dataset_id>/<version>/run_receipt.json`
- optional: `sbom/`, `attestations/` (supply-chain)

### 5.2 Deterministic IDs (So citations don’t rot)

Minimum identity fields:
- `dataset_id` (stable semantic slug)
- `version` (semantic or date/versioned)
- `spec_hash` (hash of canonicalized dataset spec)
- `run_id` (immutable run identifier)

**Rule:** any hashed/signed object uses canonical JSON serialization (stable bytes) before hashing.

### 5.3 Validation Gates (Promotion Rules)

Promotion Raw/Work → Processed requires:
- Schema + type checks (geometry validity, CRS normalization, date ranges)
- License compatibility checks (before publish)
- Sensitivity classification review (before public endpoints/Story Nodes)
- Reproducibility check: same inputs + same code version rebuilds identical artifacts
- Policy-as-code approval (OPA/Conftest gate) must pass

---

## 6) Catalog & Provenance (Metadata Triad)

### 6.1 STAC (Assets & spatial-temporal discovery)
- Use STAC for asset-level metadata (collections/items/assets)
- Assets point to object store artifacts (COG/PMTiles/GeoParquet) via policy-checked URLs

### 6.2 DCAT (Dataset catalog record)
- DCAT record is the “landing page metadata” for datasets, includes distributions, license, publisher, temporal/spatial coverage, keywords, sensitivity.

### 6.3 PROV-O (Lineage & accountability)
- PROV records: Entities (inputs/outputs), Activities (transforms), Agents (who/what performed)
- Link PROV to STAC/DCAT via stable IDs

---

## 7) Governed API (REST-first; optional GraphQL)

### 7.1 Core Endpoint Surface (v1)

**Catalog / datasets**
- `GET /api/v1/datasets` (filters: keyword/theme/sensitivity/bbox/time range)
- `GET /api/v1/datasets/{id}` (DCAT summary + links to STAC/PROV + versions)

**Search**
- `GET /api/v1/search?query=...&filters=...` (text + spatial + metadata)

**Tiles**
- `GET /api/v1/tiles/{layer}/{z}/{x}/{y}` (vector/raster tiles from processed artifacts)

**Evidence**
- `GET /api/v1/evidence/resolve?ref=<scheme://...>` → returns:
  - human-readable evidence view
  - machine-readable metadata
  - access decision + redaction/generalization obligations

**Focus Mode**
- `POST /api/v1/ai/query` (alias `/api/v1/focus-mode/query`)
  - input: `{question, context, user_role}`
  - output: `{answer, citations[], audit_ref}`
  - refusal modes when citations cannot be produced

**Graph**
- `POST /graphql` (optional)
  - must route through same usecases as REST (no bypass)

### 7.2 Response Schema Rules (Anti-hallucination by contract)

- Every answer must include:
  - `citations[]` with resolvable `ref` values
  - `audit_ref` that points to a logged audit record
- Any claim without citations → model must abstain or return a qualified uncertainty object.

---

## 8) Policy-as-Code (OPA) — CI and Runtime Must Match

### 8.1 Policy Bundle Layout

```text
policy/rego/
├─ authz/            # roles, permissions, datasets access
├─ sensitivity/      # generalization/redaction rules
├─ focus_mode/       # cite-or-abstain enforcement, citation resolvability
├─ licensing/        # publish eligibility checks
└─ receipts/         # receipt invariants + signature rules
```

### 8.2 Fail-Closed Enforcement

- If OPA decision is missing/unknown/unreachable → **deny**
- OPA runs:
  - **in-process** for dev simplicity
  - **sidecar** for production isolation and standardization

### 8.3 Conftest Gate in CI

- Every PR runs:
  - JSON schema validation for catalogs/receipts/docs metadata
  - Conftest policy checks
- Required status check before merge

---

## 9) Audit Ledger & Observability

### 9.1 Audit Ledger (Append-only)

Log (min):
- request metadata (time, actor, role)
- route + params (redacted if needed)
- datasets referenced (ids + versions)
- citations emitted (refs)
- policy decision summary
- correlation_id
- Focus Mode: model version + retrieved context sources + final answer + citations

### 9.2 Correlation IDs

- Every request gets `X-KFM-Correlation-Id`
- Subcalls (db/search/object store) reuse correlation ID
- Observability stack uses correlation ID to trace

---

## 10) Frontend UX (React + MapLibre/Cesium)

### 10.1 Core UI Views

- Map view (layers, opacity, legend)
- Timeline (time slider, decade/year events)
- Dataset browser (DCAT landing pages)
- Story Node reader (guided narrative + citations + “inspect data”)
- Focus Mode panel (chat + citations + audit/explain)
- Admin/governance console (policy bundles, receipts, promotion gates)

### 10.2 “Explain Panel” (Trust UI)

User clicks:
- citation → evidence resolver drawer opens (snippet + provenance + policy badge)
- audit_ref → audit log view opens (who/what sources were used)

---

## 11) Documentation System Redesign (No YAML Frontmatter)

### 11.1 Problem

Legacy docs used YAML frontmatter; new requirement is **metadata embedded neatly** while remaining:
- human-friendly in GitHub
- machine-parseable for CI validation
- compatible with multiple renderers

### 11.2 New Standard: Metadata Capsule (KFM)

**Rule:** Every governed Markdown doc starts with a **JSON metadata capsule** inside an HTML comment:

```html
<!--
KFM-META (v1)
{ "...json..." }
KFM-META-END
-->
```

Then optionally a human-friendly `<details>` card (table).

### 11.3 Doc Metadata JSON Schema (Required Fields)

Required keys:
- `kfmDocID`, `title`, `docKind`, `version`, `created`, `status`
- `governance.sensitivity`, `governance.license`, `governance.requiresReview`
- `canonicalMetaHash` (CI can fill/verify)
- `links.schema_doc_meta`, `links.validator`

### 11.4 Validation Tooling

Implement `tools/docs/validate_docs.py`:
- find `docs/**/*.md`
- extract JSON capsule
- validate against `schemas/docs/kfm_doc_meta.schema.json`
- verify required section headings for docKind (Universal Doc / Story Node / API contract)
- fail CI if invalid

---

## 12) Linux-First Runtime (Single Host) → Cloud Provider (Kubernetes/OpenShift)

### 12.1 Local on Linux (Developer + Small Pilot)

**Preferred:** Podman rootless + systemd  
**Alternative:** Docker + docker compose

Minimum services:
- PostGIS
- Neo4j
- Search (OpenSearch/Meili—choose one)
- MinIO (S3-compatible object store)
- OPA
- kfm-api
- kfm-ui

### 12.2 Production (Cloud / Provider)

- Kubernetes/OpenShift
- GitOps (Argo CD or Flux)
- Kustomize overlays per environment:
  - `dev`, `staging`, `prod`
- CI builds, signs, and publishes images; CD syncs manifests

---

## 13) Security Plan (Baseline)

- Prefer server-side sessions or HttpOnly cookies; avoid long-lived tokens in localStorage
- Strong XSS defenses (CSP), secure cookie flags (Secure/HttpOnly/SameSite)
- Rate limiting, authN, authZ enforced at API boundary
- Secrets management: env vars + secret store; never commit secrets
- Supply chain:
  - SBOM generation
  - container scanning
  - signed images/attestations (cosign)

---

## 14) Testing & CI Gates (Definition of Done)

### 14.1 Test Layers

- Unit tests: domain + usecases
- Integration tests: PostGIS/Neo4j/search adapters
- Contract tests: OpenAPI + evidence resolver + Focus Mode response schema
- E2E tests: UI + API + citations drawer + audit panel
- Governance regression tests: policy fixtures (allow/deny), schema fixtures (valid/invalid)

### 14.2 CI Required Gates (Fail Closed)

- Lint + typecheck (backend + frontend)
- Schema validation (STAC/DCAT/PROV/receipts/docs-meta)
- Conftest policy checks
- Unit + integration tests
- Build + SBOM + sign (only if gates pass)
- Optional: deploy preview env (staging)

---

## 15) Thin-Slice Implementation Roadmap (Buildable Increments)

### Phase 0 — “Contracts First”
- Add schemas: doc meta capsule, run_receipt, minimal DCAT/STAC/PROV profiles
- Add fixtures (valid + invalid) + CI schema gate

**DoD:** CI fails on invalid examples; schema checks are required for merge.

### Phase 1 — “Fail-Closed Policy Gates”
- Add OPA policies + Conftest in PR CI
- Deny-by-default
- Add kill-switch for emergency stop

**DoD:** Any deny blocks merge; kill-switch blocks merge quickly.

### Phase 2 — “One Pilot Dataset End-to-End”
- Ingest one dataset through Raw→Work→Processed
- Emit STAC/DCAT/PROV + receipt
- Serve via API endpoints + render one layer in UI

**DoD:** User can view dataset in UI; click evidence; trace provenance.

### Phase 3 — “Evidence Resolver + Focus Mode MVP”
- Implement `/api/v1/evidence/resolve`
- Implement `/api/v1/ai/query`:
  - retrieval only from indexed governed artifacts
  - cite-or-abstain schema
  - audit_ref logging

**DoD:** Every citation resolves or returns correct 403/404 without leaks.

### Phase 4 — “GitOps Production”
- Add GitOps manifests + environment overlays
- Deploy to Kubernetes/OpenShift
- Observability dashboards + backups runbooks

**DoD:** Reproducible deploys, rollback, and audit trails.

---

## Appendix A — Story Node v3 (Governed Narrative) — Recommended Shape

Story Nodes are Markdown files with:
- Metadata capsule (JSON)
- Narrative sections
- Explicit citations (`stac://`, `dcat://`, `prov://`, etc.)
- Sensitivity notes + uncertainty notes

Build step extracts Story Nodes into:
- searchable index
- graph entities/edges
- API resources

---

## Appendix B — “Not Confirmed” Label Rule

If a claim cannot be traced to:
- a governed dataset version,
- an approved model run,
- or an approved document source,

KFM must label it: **not confirmed**.

---

## Appendix C — Ops Runbooks (Minimum Set)

- Backup/restore PostGIS + Neo4j + object store
- Policy update process (review + diff + rollout)
- Incident response: revoke tokens + rotate keys + disable publish
- Data rollback: revert to previous dataset version
- Audit review procedure
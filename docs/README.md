<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/1f731fb8-1614-4a01-a1a5-f8e5ed39c7e1
title: docs/ — Documentation hub
type: standard
version: v2
status: draft
owners: TBD
created: 2026-03-03
updated: 2026-03-04
policy_label: public
related:
  - docs/MASTER_GUIDE_v13.md
  - docs/governance/ROOT_GOVERNANCE.md
tags: [kfm, docs]
notes:
  - Entry point for repository documentation.
  - This README defines the REQUIRED docs/ layout for KFM vNext.
  - If your checkout differs, update the tree + links only after verifying the repo structure.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# docs/ — Documentation hub
**Governed, human-readable documentation for the Kansas Frontier Matrix (KFM).**

> **[CONFIRMED] Purpose:** `docs/` is the authoritative home for **governed documentation**: architecture blueprints, standards/profiles, governance policy, templates, specs, and published narrative artifacts (“Story Packs / Story Nodes”).

---

## IMPACT
- **Status:** draft
- **Owners:** TBD (set via `CODEOWNERS`)
- **Policy label:** public
- **[CONFIRMED] This hub exists to prevent “tribal-memory architecture.”**
- **[CONFIRMED] Hard exclusions:** secrets, raw datasets/binaries, and unreviewed sensitive details (especially precise vulnerable locations).

[![Docs](https://img.shields.io/badge/docs-entrypoint-blue)](./README.md)
[![Status](https://img.shields.io/badge/status-draft-lightgrey)](#impact)
[![MetaBlock](https://img.shields.io/badge/metablock-v2-required-red)](#metablock-v2-and-document-metadata)
[![Fail-closed](https://img.shields.io/badge/gates-fail--closed-red)](#review-gates-and-definition-of-done)
[![Docs Index](https://img.shields.io/badge/docs-index-PROPOSED-lightgrey)](#docs-registry-and-discovery)
[![Linkcheck](https://img.shields.io/badge/linkcheck-TODO-lightgrey)](#local-preview--checks)

**Quick links:** [Start here](#start-here) · [Project map](#kfm-project-map-what-is-in-scope) · [Docs layout](#required-docs-layout) · [Docs registry](#docs-registry-and-discovery) · [Specs](#specs-and-component-design-docs) · [MetaBlock v2](#metablock-v2-and-document-metadata) · [Gates](#review-gates-and-definition-of-done) · [Add a doc](#how-to-add-a-new-document) · [Unknowns](#unknowns-to-verify)

---

## Quick navigation
- [Evidence legend](#evidence-legend)
- [Start here](#start-here)
- [KFM project map](#kfm-project-map-what-is-in-scope)
- [Where docs fit: truth path and trust membrane](#where-docs-fit-truth-path-and-trust-membrane)
- [Docs authority levels](#docs-authority-levels)
- [Acceptable inputs](#acceptable-inputs-for-docs)
- [Exclusions](#exclusions-what-must-not-go-in-docs)
- [Required docs layout](#required-docs-layout)
- [Directory responsibilities](#directory-responsibilities-human-routing-table)
- [Docs registry and discovery](#docs-registry-and-discovery)
- [Docs taxonomy and routing](#docs-taxonomy-and-routing)
- [MetaBlock v2 and document metadata](#metablock-v2-and-document-metadata)
- [Standards and profiles](#standards-and-profiles)
- [Specs and component design docs](#specs-and-component-design-docs)
- [AI and MCP docs](#ai-and-mcp-documentation)
- [Knowledge graph docs](#knowledge-graph-and-ontology-documentation)
- [Reference docs](#reference-contracts-schemas-and-apis)
- [Stories](#stories-story-nodes-and-story-packs)
- [Review gates and definition of done](#review-gates-and-definition-of-done)
- [Local preview and checks](#local-preview--checks)
- [Unknowns to verify](#unknowns-to-verify)
- [FAQ](#faq)
- [Appendix](#appendix)
- [Back to top](#back-to-top)

---

## Evidence legend
KFM docs are governed. Every meaningful claim is explicitly labeled:

- **[CONFIRMED]** = enforced invariant or documented requirement.
- **[PROPOSED]** = recommended pattern; may not yet be implemented.
- **[UNKNOWN]** = not verified in this checkout; list the smallest verification step.

> **[CONFIRMED] Rule:** If you can’t ground it, mark it **[UNKNOWN]** and list the smallest verification step.

---

## Start here
Read these in order (or use as your quick orientation map):

1) **`docs/MASTER_GUIDE_v13.md`** — canonical overview + doc map (if present).  
2) **`docs/governance/ROOT_GOVERNANCE.md`** — governance charter and “how changes are approved.”  
3) **`docs/architecture/README.md`** — architecture boundaries, invariants, diagrams, and ADR index.  
4) **`docs/standards/README.md`** — standards/profiles that define “valid” in KFM.  
5) **`docs/specs/README.md`** — component-level design specs that become buildable work (if present).  
6) **`docs/stories/README.md`** — Story authoring + publishing workflow (governed narrative artifacts).  
7) **`docs/quality/README.md`** — gates, conformance checks, test strategy, determinism expectations.

> **[UNKNOWN]** If any linked file/folder is missing in your checkout, treat it as **a required gap** and create a placeholder stub (or update this README to match the verified tree).

---

## KFM project map: what is in scope
This section is a **project assessment** (what KFM contains, and what it explicitly must not be).

### What KFM is
- **[CONFIRMED]** KFM is a **pipeline → catalog → governed API → UI** system. It turns upstream data into immutable artifacts, validated catalogs, and governed runtime surfaces.
- **[CONFIRMED]** KFM includes **Map Explorer**, **Story Mode**, and **Focus Mode** (AI-assisted Q&A) where user-visible claims must be evidence-backed.
- **[CONFIRMED]** KFM treats **evidence, provenance, and policy** as first-class runtime constraints, not afterthoughts.

### What KFM is not
- **[CONFIRMED]** Not a “upload-and-forget portal.”
- **[CONFIRMED]** Not a UI that directly queries databases.
- **[CONFIRMED]** Not an ungoverned chatbot (Focus Mode is constrained by policy and citation gates).

### System slices (what exists conceptually)
Use this mental model when writing docs or adding features:

```mermaid
flowchart LR
  Up[Upstream sources] --> RAW[RAW zone]
  RAW --> WORK[WORK or QUARANTINE]
  WORK --> PROCESSED[PROCESSED zone]
  PROCESSED --> CATALOG[CATALOG triplet]
  CATALOG --> PUBLISHED[PUBLISHED surfaces]

  PUBLISHED --> API[Governed API]
  API --> UI[UI Map Story Focus]

  API --> POL[Policy engine]
  API --> EV[Evidence resolver]
  EV --> CATALOG
```

**[CONFIRMED] Interlock:** docs must never propose shortcuts that bypass policy enforcement or the evidence resolver.

### Repo surfaces KFM expects (outside docs)
> **[UNKNOWN]** The exact repo tree in *this checkout* must be verified. (This README links to target locations; update after running `tree -L 3`.)

**[PROPOSED]** Expected top-level repository slices (for orientation only):

| Path | Role | Docs should link to |
|---|---|---|
| `apps/` | runnable services (API, UI, workers, CLI) | `docs/architecture/`, `docs/guides/`, `docs/runbooks/` |
| `packages/` | core modules (ingest, catalog, evidence, policy, indexers) | `docs/specs/`, `docs/architecture/interfaces/` |
| `contracts/` | machine contracts (OpenAPI, JSON Schema, vocab) | `docs/reference/OPENAPI_INDEX.md`, `docs/reference/SCHEMA_REGISTRY.md` |
| `policy/` | OPA/Rego bundles + tests | `docs/standards/policy/`, `docs/guides/policy/` |
| `data/` | lifecycle zones + dataset specs + catalogs | `docs/data/` (documentation only) |
| `tools/` | validators, linters, spec hashers, linkcheckers | `docs/quality/`, `docs/reference/TOOLING_INDEX.md` |
| `infra/` | deployment (K8s/Terraform/GitOps) | `docs/architecture/DEPLOYMENT_TOPOLOGY.md`, `docs/runbooks/DEPLOY.md` |
| `configs/` | config templates (env, pipelines, UI) | `docs/guides/onboarding/DEV_ENV_SETUP.md` |
| `migrations/` | DB schema migrations | `docs/runbooks/BACKUP_RESTORE.md` + DB runbooks |
| `examples/` | sample datasets/stories/policies | `docs/reference/` and `docs/stories/_templates/` |
| `tests/` | unit/integration/e2e | `docs/quality/` |
| `mcp/` | AI artifacts (model cards, experiments, gates) | `docs/ai/` + `docs/templates/TEMPLATE__MODEL_CARD.md` |

---

## Where docs fit: truth path and trust membrane

### Truth path lifecycle (data zones)
**[CONFIRMED]** KFM uses a gated lifecycle (“truth path”) that documentation must not contradict:

```mermaid
flowchart LR
  Up[Upstream] --> RAW[RAW immutable]
  RAW --> WORK[WORK or QUARANTINE]
  WORK --> PROCESSED[PROCESSED publishable]
  PROCESSED --> CAT[CATALOG triplet]
  CAT --> PUB[PUBLISHED governed]

  PUB --> API[Governed API]
  API --> UI[UI surfaces]
```

- **[CONFIRMED]** RAW is append-only immutable acquisition + checksums.
- **[CONFIRMED]** WORK/QUARANTINE is where QA and redaction/generalization candidates happen.
- **[CONFIRMED]** PROCESSED holds publishable artifacts + checksums.
- **[CONFIRMED]** CATALOG is cross-linked **DCAT + STAC + PROV** plus run receipts.
- **[CONFIRMED]** PUBLISHED surfaces may only serve promoted versions that passed gates.

### Trust membrane (policy boundary)
**[CONFIRMED]** The trust membrane is the enforced boundary that prevents bypass:

```mermaid
flowchart LR
  C[Clients and UI] --> PEP[Governed API PEP]
  PEP --> REPO[Repository interfaces]
  REPO --> STORES[Stores DB and object]
  PEP --> PDP[Policy engine]
  PEP --> EV[Evidence resolver]
  EV --> CAT[Catalog triplet]
```

- **[CONFIRMED]** Clients/UI never access DB/object storage directly.
- **[CONFIRMED]** Backend domain logic must not bypass repository interfaces to reach storage directly.
- **[CONFIRMED]** Policy evaluation applies at the PEP and gates what can be returned.

> **[CONFIRMED] Doc rule:** If a document proposes behavior that breaks this membrane, it is incorrect by definition.

---

## Docs authority levels
This prevents “random docs” from becoming de-facto policy.

- **[CONFIRMED] Authority classes (minimum):**
  1) **Standards/Profiles** (`docs/standards/`) — normative. “MUST/SHALL” language allowed.
  2) **Governance** (`docs/governance/`) — normative. Overrides everything except repo policy enforcement.
  3) **Architecture** (`docs/architecture/`) — high authority; design boundaries + invariants + interfaces.
  4) **Specs** (`docs/specs/`) — buildable design docs; must link to contracts/tests.
  5) **Guides/Runbooks** (`docs/guides/`, `docs/runbooks/`) — operational; non-normative unless referenced by governance.
  6) **Investigations** (`docs/investigations/`) — explicitly non-authoritative.

- **[PROPOSED] Rule:** any doc intended to constrain behavior must be either:
  - a **Standard**, or
  - a **Spec** that is referenced by a Standard and guarded by CI/tests.

---

## Acceptable inputs for docs/
Docs are a production surface; keep them stable, reviewable, and retrieval-friendly.

**[CONFIRMED] Acceptable:**
- Architecture docs (diagrams, subsystem boundaries, contracts in human-readable form)
- Standards/profiles (STAC/DCAT/PROV profiles; repo conventions; doc protocol)
- Governance and review policy (non-secret)
- Specs (component-level buildable design documents)
- Templates (MetaBlock v2 docs, Story Nodes, contract extensions)
- Published narrative artifacts (Story Packs)

---

## Exclusions: what must NOT go in docs/
**[CONFIRMED] Never put in `docs/`:**
- Secrets (API keys, credentials, tokens)
- Raw datasets, large binaries, or lifecycle artifacts (RAW/WORK/PROCESSED belong under `data/`)
- Unreviewed sensitive details (precise vulnerable locations, restricted archeological sites, etc.)

**[PROPOSED] Avoid unless explicitly approved:**
- Generated build outputs (static site builds, compiled docs)
- Vendor bundles that should be fetched via tooling instead

---

## Required docs layout
This README defines the **target, “encompass-all-things”** documentation layout for KFM.

> **[CONFIRMED] Expectation:** Each major directory has its own `README.md` index.  
> **[CONFIRMED] Expectation:** Any missing path in this tree is a “docs debt” item (create stubs or adjust links after verification).

```text
docs/
  README.md                      # docs hub (index + rules + "where docs fit")

  MASTER_GUIDE_v13.md            # canonical overview + doc map (MUST exist if referenced)
  glossary.md                    # domain vocabulary (single source of truth)
  CHANGELOG.md                   # (PROPOSED) docs-surface change log (optional but useful)

  _registry/                     # (PROPOSED) machine-readable doc/story indices for retrieval
    README.md
    docs.index.yml               # doc_id → path/title/status/policy_label/tags
    docs.index.schema.json       # schema for docs.index.yml (CI validation)

  adr/                           # Architecture Decision Records (canonical home)
    README.md
    ADR-0001-template.md
    ADR-0002-<decision-slug>.md

  architecture/                  # blueprints + invariants + subsystem contracts (human-readable)
    README.md
    TRUST_MEMBRANE.md            # invariant: UI -> governed API only; no bypass
    TRUTH_PATH_LIFECYCLE.md      # invariant: Upstream→RAW→WORK→PROCESSED→CATALOG→PUBLISHED
    SYSTEM_CONTEXT.md            # “C4 L1” system context narrative
    DEPLOYMENT_TOPOLOGY.md       # local-first + cloud scale topology
    interfaces/                  # human-readable subsystem interfaces (PEP, repos, evidence, policy)
      README.md
      API_LAYER_CONTRACT.md
      POLICY_ENGINE_CONTRACT.md
      EVIDENCE_RESOLVER_CONTRACT.md
      REPOSITORY_LAYER_CONTRACT.md
      CATALOG_TRIPLET_CONTRACT.md
    diagrams/                    # architecture diagrams (Mermaid/SVG/PNG)
      README.md
    adr/                         # OPTIONAL: if you keep ADRs here, make it a stub pointing to docs/adr/
      README.md

  standards/                     # normative standards/profiles + repo conventions (CI-enforced where possible)
    README.md
    KFM_MARKDOWN_WORK_PROTOCOL.md
    KFM_REPO_STRUCTURE_STANDARD.md
    KFM_STAC_PROFILE.md
    KFM_DCAT_PROFILE.md
    KFM_PROV_PROFILE.md

    docs/                        # (PROPOSED) doc-level standards beyond the Markdown protocol
      README.md
      DOC_IDS_AND_METADATA.md
      LINKING_AND_ANCHORS.md
      DIAGRAMS_STYLE_GUIDE.md

    identity/
      README.md
      IDENTIFIERS_AND_NAMING.md          # dataset_id, evidence_ref, story_slug, etc.
      HASHING_AND_DIGESTS.md             # sha256, spec_hash, canonicalization rules

    policy/
      README.md
      POLICY_PACK_STANDARD.md            # bundle structure + tests
      REGO_V1_MIGRATION.md               # how/when to migrate policies and tests

    api/
      README.md
      API_VERSIONING_AND_ERRORS.md       # error model, pagination, stability guarantees

    evidence/
      README.md
      EVIDENCE_REF_STANDARD.md           # syntax + resolver guarantees

    catalog/
      README.md
      CATALOG_TRIPLET_STANDARD.md        # DCAT+STAC+PROV cross-linking expectations

    geo/                          # (PROPOSED) geospatial formats + CRS + tiling norms
      README.md
      CRS_AND_PROJECTIONS.md
      RASTER_FORMATS_COG.md
      VECTOR_FORMATS_GEOPARQUET.md
      TILE_FORMATS_PMTILES.md

    telemetry/                     # (PROPOSED) event naming + schemas + retention rules
      README.md
      TELEMETRY_EVENT_NAMING.md
      PIPELINE_RUN_TELEMETRY.md
      UI_TELEMETRY.md

    oci/                           # (PROPOSED) publishing artifacts to OCI registries (mediaTypes, referrers, attestations)
      README.md
      OCI_GEOSPATIAL_ARTIFACTS.md
      MEDIA_TYPES_REGISTRY.md
      DELTA_REFERRERS_STANDARD.md

    supply_chain/                  # (PROPOSED) SBOM, SLSA, signing/verification expectations
      README.md
      SBOM_STANDARD.md
      SLSA_ATTESTATION_STANDARD.md
      SIGNING_AND_VERIFICATION.md

    ui/
      README.md
      UI_TRUST_SURFACES_STANDARD.md      # what UI may render; citation UX rules; safe defaults

    ai/
      README.md
      MODEL_CARD_STANDARD.md
      RAG_RETRIEVAL_STANDARD.md
      AI_EVAL_AND_REDTEAM_STANDARD.md

    ontology/
      README.md
      KFM_ONTOLOGY_PROFILE.md            # graph vocab, mapping rules, time/geo semantics

  templates/                     # authoring templates (make “good docs” the path of least resistance)
    README.md
    TEMPLATE__KFM_UNIVERSAL_DOC.md
    TEMPLATE__STORY_NODE_V3.md
    TEMPLATE__API_CONTRACT_EXTENSION.md
    TEMPLATE__ADR.md
    TEMPLATE__RUNBOOK.md
    TEMPLATE__MODEL_CARD.md
    TEMPLATE__DATASET_ENTRY.md
    TEMPLATE__RUN_RECEIPT.md
    TEMPLATE__POLICY_CHANGE.md
    TEMPLATE__COMPONENT_SPEC.md          # (PROPOSED) spec template for docs/specs/*

  governance/                    # governance charter, ethics, sovereignty, review gates
    README.md
    ROOT_GOVERNANCE.md
    ETHICS.md
    SOVEREIGNTY.md
    REVIEW_GATES.md
    DATA_CLASSIFICATION.md              # policy labels + handling rules
    SENSITIVE_LOCATIONS_PLAYBOOK.md     # redaction/generalization rules
    WAIVERS_AND_EXCEPTIONS.md           # explicit override process + audit requirements
    ROLES_AND_RACI.md                   # (PROPOSED) who approves what (explicit)

  specs/                         # (PROPOSED) buildable component specs (versioned, reviewable)
    README.md
    agents/                      # watcher/planner/executor patterns; governed automation
      README.md
      WATCHER_CONTRACT.md
      PLANNER_CONTRACT.md
      EXECUTOR_CONTRACT.md
    pipelines/                   # pipeline-specific specs (beyond guides)
      README.md
      ingestion/                 # connector/pipeline specs (domain or cross-cutting)
      hydrology/
      hazards/
      climate/
    ui/                          # UI component specs (map/story/focus)
      README.md
    storage/                     # storage/distribution specs (object store, OCI, deltas)
      README.md
    observability/
      README.md

  ai/                            # (PROPOSED) AI surfaces: Focus Mode, Ollama, evaluation, safety
    README.md
    FOCUS_MODE_OVERVIEW.md
    OLLAMA_INTEGRATION.md
    MODEL_CARDS_INDEX.md
    EVALUATION_AND_BENCHMARKS.md

  knowledge_graph/               # (PROPOSED) Neo4j + ontology + graph ingestion/query patterns
    README.md
    GRAPH_DATA_MODEL.md
    ONTOLOGY_AND_VOCAB.md
    GRAPH_RAG_PATTERNS.md
    NEO4J_OPERATIONS.md

  reference/                     # (PROPOSED) indices into machine surfaces (contracts/schemas/policy)
    README.md
    OPENAPI_INDEX.md             # maps OpenAPI files → endpoints → owners
    SCHEMA_REGISTRY.md           # maps JSON schemas → purpose → validators
    POLICY_BUNDLE_INDEX.md       # maps policy bundles → gates → owners
    TOOLING_INDEX.md             # validators + linters + how to run

  guides/                        # “how do I do X safely?” procedural docs (human-operated)
    README.md
    onboarding/
      README.md
      DEV_ENV_SETUP.md
      FIRST_DATASET_WALKTHROUGH.md
      FIRST_STORY_WALKTHROUGH.md
    acquisition/
      README.md
      CONNECTOR_AUTHORING.md
      RAW_INGEST_PLAYBOOK.md
    geo/                         # (PROPOSED) GIS-centric how-tos (raster/vector/tiling/CRS)
      README.md
      VECTOR_ETL_PIPELINES.md
      RASTER_ETL_PIPELINES.md
      HYDROLOGY_WORKFLOWS.md
    pipelines/
      README.md
      BUILD_A_PIPELINE_STEP.md
      PROMOTION_FLOW.md
    catalogs/
      README.md
      EMIT_STAC_DCAT_PROV.md
      VALIDATE_CATALOGS.md
    apis/
      README.md
      ADD_NEW_ENDPOINT.md
      FOCUS_MODE_ENDPOINTS.md
    policy/
      README.md
      WRITE_A_POLICY.md
      DEBUG_POLICY_DENIALS.md
    observability/
      README.md
      TRACE_A_REQUEST.md
      READ_RUN_RECEIPTS.md
    ui/
      README.md
      RUN_UI_LOCALLY.md
      STORY_AUTHORING.md
    security/
      README.md
      SECRETS_AND_OIDC.md
      THREAT_MODELING_HOWTO.md

  runbooks/                      # “the system is on fire / needs operation” (ops-owned)
    README.md
    LOCAL_STACK.md
    DEPLOY.md
    BACKUP_RESTORE.md
    INCIDENT_RESPONSE.md
    DATA_PROMOTION_RUNBOOK.md
    POLICY_CHANGE_RUNBOOK.md
    DR_AND_ROLLBACK.md

  quality/                       # gates, conformance, and test strategy (fail-closed defaults)
    README.md
    GATES_DEFINITION_OF_DONE.md         # promotion gates + CI mapping
    CONTRACT_TESTS.md                   # schemas/contracts/OpenAPI checks
    DETERMINISM_AND_REPRO.md            # reproducibility expectations + checks
    PERFORMANCE_SLOS.md                 # API/pipeline SLOs (if applicable)
    SECURITY_BASELINE.md                # SBOM/vuln scan expectations (doc-level)

  data/                          # data-system documentation (NOT the datasets themselves)
    README.md
    DATA_LIFECYCLE.md
    DATASET_REGISTRY.md
    PROVENANCE_AND_RECEIPTS.md
    LICENSING_AND_ATTRIBUTION.md

  domains/                       # domain-specific docs (hydrology, soils, air, etc.)
    README.md
    hydrology/
      README.md
      DATA_SOURCES.md
      PIPELINES.md
    soils/
      README.md
      DATA_SOURCES.md
      PIPELINES.md
    air/
      README.md
      DATA_SOURCES.md
      PIPELINES.md
    hazards/
      README.md
      DATA_SOURCES.md
      PIPELINES.md

  diagrams/                      # shared diagrams (cross-cutting; referenced by many docs)
    README.md
    architecture/
    pipelines/
    ui/
    governance/
    domains/

  investigations/                # sandbox notes + experiments (explicitly not published outputs)
    README.md
    <topic>/
      README.md
      notes.md
      artifacts/                 # small, non-sensitive, non-authoritative samples only

  stories/                       # canonical Story Node home (governed narrative artifacts)
    README.md
    CODEOWNERS                   # optional: route reviews to approvers
    _schemas/                    # story pack schemas for CI validation
    _registry/                   # story index for UI discovery
    _governance/                 # story-specific governance helpers (optional)
    _lint/                       # story lint config
    _shared/                     # shared story utilities
    _templates/                  # story templates (reusable patterns)
    draft/                       # WIP (not published)
    review/                      # under governance review
    published/                   # immutable published story packs
      <story_slug>/
        story.md
        story.json               # map choreography/state (if used)
        assets/                  # approved media/data excerpts for that story
    withdrawn/                   # removed from publish surface (keep audit trail)

  reports/                       # OPTIONAL: generated/curated reports (non-story), or a stub redirect
    README.md                    # if you keep stories elsewhere, make this a redirect to docs/stories
```

---

## Directory responsibilities: human routing table

| Folder | Role | What good looks like | What must not happen |
|---|---|---|---|
| `docs/` | Hub + canonical entry points | MASTER_GUIDE + glossary stay current | Becomes a dumping ground |
| `docs/_registry/` | (PROPOSED) Machine indices | CI-valid index enables Focus Mode retrieval | Index drifts silently |
| `docs/architecture/` | Boundaries + invariants + diagrams + interface contracts | Stable invariants + interface docs + diagrams | Architecture changes without ADR/spec |
| `docs/adr/` | Decisions | Each “why” documented w/ rollback path | Decisions hidden in chat |
| `docs/standards/` | Standards/profiles + repo conventions | MUST/SHALL mapped to validators/tests | Standards drift without gates |
| `docs/specs/` | (PROPOSED) Buildable design specs | PR-ready specs that link to contracts + tests | “Specs” become wishlists |
| `docs/governance/` | Governance rules and review gates | Clear “who approves what” + escalation | Informal policy in Slack |
| `docs/guides/` | How-to docs | Steps are runnable; safe defaults | Confuses “how-to” with “must” |
| `docs/runbooks/` | Ops runbooks | Triage + restore + rollback are clear | No incident plan |
| `docs/quality/` | Gates + conformance | Fail-closed maps to CI checks | “Quality” undocumented |
| `docs/data/` | Data-system docs | Registry + receipts + licensing are clear | Datasets stored here |
| `docs/domains/` | Domain documentation | Each domain has sources + pipelines | Domain knowledge scattered |
| `docs/ai/` | (PROPOSED) AI system docs | Focus Mode boundaries + eval + safety | Ungoverned prompts/evals |
| `docs/knowledge_graph/` | (PROPOSED) graph modeling + ops | Ontology, graph patterns, GraphRAG | Ad-hoc labels/relations |
| `docs/reference/` | (PROPOSED) pointers to machine contracts | Humans can find schemas/contracts fast | Duplicates machine sources |
| `docs/stories/` | Story Packs | published is immutable + cited + governed | Drafts treated as published |
| `docs/investigations/` | Sandbox notes | Explicitly non-authoritative | Research gets mistaken as policy |

---

## Docs registry and discovery
**[PROPOSED]** Add a **docs index** so Focus Mode and humans can reliably discover “the right doc” without guessing.

### Why
- **[CONFIRMED]** KFM depends on evidence-first retrieval; discovery surfaces must be stable.
- **[PROPOSED]** A machine-readable docs index reduces link rot, improves search relevance, and enables validation (e.g., “no published doc missing MetaBlock”).

### Minimal structure (proposal)
- `docs/_registry/docs.index.yml` with one entry per doc containing:
  - `doc_id`, `path`, `title`, `type`, `status`, `owners`, `policy_label`, `tags`, `related`.
- Validate in CI against `docs/_registry/docs.index.schema.json`.

> **[UNKNOWN]** Whether the repo already has an index mechanism must be verified. If a different index exists, keep one canonical home and redirect.

---

## Docs taxonomy and routing

Use this matrix when adding a new file:

| Doc type | Put it here | Must include | Gate sensitivity |
|---|---|---|---|
| Canonical guide | `docs/` | MetaBlock v2, stable headings, links | Medium |
| Architecture overview | `docs/architecture/` | diagrams + boundaries + invariants | High |
| ADR | `docs/adr/` | decision, alternatives, consequences, rollback | High |
| Standard/profile | `docs/standards/` | normative language, test hooks, versioning | High |
| Spec (buildable) | `docs/specs/` | contract links + test hooks + rollout/rollback | High |
| Governance policy | `docs/governance/` | roles, gates, enforcement intent | Highest |
| Template | `docs/templates/` | how-to-use + example | Medium |
| How-to guide | `docs/guides/` | runnable steps + safety notes | Medium |
| Runbook | `docs/runbooks/` | triage + rollback + verify | Highest |
| Model card | `mcp/model_cards/` (or `docs/ai/`) | version pinning + eval + governance | Highest |
| Story Pack | `docs/stories/` | citations + review state + policy label | Highest |
| Investigation note | `docs/investigations/` | marked non-authoritative | Low |

---

## MetaBlock v2 and document metadata
**[CONFIRMED]** KFM uses **MetaBlock v2** (HTML comment) for docs, Story Packs, and dataset specs.

### Minimal MetaBlock v2 template
```html
<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<uuid>
title: <Title>
type: <guide|standard|story|dataset_spec|adr|run_receipt|spec|model_card>
version: v1
status: draft|review|published
owners: <team or names>
created: YYYY-MM-DD
updated: YYYY-MM-DD
policy_label: public|restricted|...
related:
  - kfm://dataset/<slug>@<version>
  - kfm://story/<id>@<version>
tags: [kfm]
notes: [<short notes>]
[/KFM_META_BLOCK_V2] -->
```

### MetaBlock rules
- **[CONFIRMED]** `doc_id` is stable — do not regenerate on edits.
- **[CONFIRMED]** bump `updated:` on meaningful edits.
- **[CONFIRMED]** `policy_label` is an input to governance (especially if docs are served through governed APIs).
- **[PROPOSED]** Use `related:` to link to datasets, Story Packs, ADRs, contracts, and policies by stable IDs.

---

## Standards and profiles
Standards under `docs/standards/` define what is “valid” in KFM. Treat them as contracts.

### Minimum set (required by this layout)
- `KFM_MARKDOWN_WORK_PROTOCOL.md`  
  **[CONFIRMED]** How to write KFM docs: headings, evidence labels, link discipline, templates, and doc gates.

- `KFM_REPO_STRUCTURE_STANDARD.md`  
  **[CONFIRMED]** The monorepo layout and boundaries: where data lives vs docs vs code; what must never cross the policy boundary.

- `KFM_STAC_PROFILE.md`  
  **[CONFIRMED]** KFM-specific STAC expectations (collections/items/assets + cross-links).

- `KFM_DCAT_PROFILE.md`  
  **[CONFIRMED]** KFM dataset-level metadata expectations (license, publisher, distribution, themes).

- `KFM_PROV_PROFILE.md`  
  **[CONFIRMED]** KFM provenance expectations for pipelines and story publishing.

> **[PROPOSED] Test enforcement rule:** every normative MUST/SHALL in a profile should map to a validator or CI check (or be explicitly marked “manual gate”).

---

## Specs and component design docs
**[PROPOSED]** `docs/specs/` is where you put “buildable” design docs that become work items and can be enforced by contracts/tests.

### What belongs in specs
- watcher/planner/executor automation patterns (auditable, PR-only mutation)
- pipeline-specific run contracts (inputs/outputs/idempotency keys)
- UI component specs that crosscut Map/Story/Focus
- storage/distribution specs (OCI publishing, delta graphs, integrity proofs)

### What does not belong in specs
- “maybe someday” ideas with no owners, no contracts, and no path to enforcement  
  → put those in `docs/investigations/`.

---

## AI and MCP documentation
**[PROPOSED]** AI system documentation needs a dedicated surface because it has unique governance risks.

Minimum required AI docs (proposal):
- **Focus Mode overview**: retrieval → evidence → synthesis → citation gate
- **Model governance**: model cards, version pinning, allowed uses, prohibited uses
- **Evaluation**: benchmarks, red-team scenarios, abstention rules, regression gates
- **Runtime operations**: local LLM runtime runbook (e.g., Ollama), model install/update, rollback

> **[CONFIRMED] Rule:** Focus Mode docs must never imply the UI calls models directly; model access is mediated by the governed API.

---

## Knowledge graph and ontology documentation
**[PROPOSED]** If Neo4j/graph semantics are core, you need an explicit place to define:
- the canonical ontology/vocabulary
- node/relationship naming conventions
- constraints/index patterns
- ingestion mapping rules
- graph-based retrieval patterns (GraphRAG)

> **[CONFIRMED] Rule:** ontology changes that affect meaning should require an ADR and an update to policy/tests (fail-closed).

---

## Reference: contracts, schemas, and APIs
**[PROPOSED]** Humans need a “map” to machine contracts without hunting through directories.

Minimum reference indices (proposal):
- **OpenAPI index**: where API specs live, ownership, versioning, endpoints
- **Schema registry**: JSON schemas + what they validate + how to run validators
- **Policy index**: bundles, gates, and ownership
- **Tooling index**: validators/linters + invocation patterns

> **[CONFIRMED]** Do not duplicate machine contracts in prose; instead, link to them and explain intent, compatibility, and enforcement points.

---

## Stories (Story Nodes and Story Packs)
`docs/stories/` is the canonical home for governed narrative artifacts.

### Lifecycle (docs-side)
- `_templates/` — reusable story patterns and rubrics  
- `draft/` — WIP stories (not published)  
- `review/` — under governance review  
- `published/<story_slug>/` — immutable published story pack  

### Published Story Pack (required)
A published story pack is a directory:

- `story.md` — narrative markdown (with citations and evidence references)
- `story.json` — optional map choreography/state
- `assets/` — only approved media/data excerpts that are allowed to ship with the story

> **[CONFIRMED] Publishing gate:** a story cannot be published unless citations resolve and the review state is captured.

---

## Review gates and definition of done
KFM is fail-closed: missing evidence blocks promotion/publishing.

### Docs-only gates (minimum)
- **[CONFIRMED] MetaBlock v2** present and valid.
- **[CONFIRMED] No secrets / no sensitive leakage.**
- **[PROPOSED] Link integrity**: internal links resolve or are marked TODO with an issue reference.
- **[PROPOSED] Ownership**: governance-impacting docs require `CODEOWNERS` approval.
- **[PROPOSED] Docs index updated** (if `docs/_registry/` is adopted).

### Standards/profile gates (minimum)
- **[CONFIRMED]** Changes to STAC/DCAT/PROV profiles must be paired with validator/test updates (or a documented manual gate).
- **[PROPOSED]** Add a “profile change note” section to each profile describing how to migrate.

### Specs gates (minimum)
- **[PROPOSED]** Specs must name owners and link to:
  - contracts they depend on
  - tests/validators that enforce them
  - rollout + rollback strategy

### Story gates (minimum)
- **[CONFIRMED]** citations are resolvable, policy-allowed, and stable.
- **[CONFIRMED]** review state recorded (draft/review/published) with owners.
- **[PROPOSED]** “narrative drift” checks: claims remain backed by promoted dataset versions.

### Copy/paste checklist (PR-ready)
- [ ] **[CONFIRMED]** MetaBlock v2 present and `updated:` bumped
- [ ] **[CONFIRMED]** No secrets, no sensitive location leakage
- [ ] **[PROPOSED]** Links validated (or explicit TODO + issue)
- [ ] **[PROPOSED]** If doc changes governance/standards, ADR created and owners approve
- [ ] **[PROPOSED]** If story, citations resolve and review state is captured
- [ ] **[PROPOSED]** If using docs registry, update `docs/_registry/docs.index.yml`

---

## How to add a new document
1) **Choose the smallest correct home**  
   - architecture vs standards vs governance vs specs vs templates vs stories vs guides/runbooks
2) **Create the file from a template**  
   - prefer `docs/templates/*`
3) **Add MetaBlock v2** at top  
4) **Update the nearest index README**  
   - and update `docs/MASTER_GUIDE_v13.md` if it is the canonical map
5) **Update registries** (if used)  
   - `docs/_registry/docs.index.yml`, `docs/stories/_registry/`, etc.
6) **Run local checks** (or closest equivalent)  
7) **Route review** via `CODEOWNERS` (and governance owners if policy changes)

---

## Local preview / checks
### Minimal, repo-agnostic checks (runnable)
```bash
# show docs tree (fallback to find if tree is unavailable)
command -v tree >/dev/null && tree -L 4 docs || find docs -maxdepth 4 -type f | sort

# confirm MetaBlock presence (at least once per doc)
grep -R --line-number --fixed-string "[KFM_META_BLOCK_V2]" docs | head -n 200

# quick internal link scan (cheap heuristic; not a real linkcheck)
grep -R --line-number -E '\]\(\.\/|^\[.*\]: \.\/' docs | head -n 200
```

### Repo-specific checks (pseudocode — rename to match your repo)
```bash
# pseudocode: replace with real targets if present in your repo
make docs.check
make linkcheck
make docs.lint
```

---

## Unknowns to verify
These are **[UNKNOWN] until verified in your checkout**:

1) Do the required paths exist exactly as specified in [Required docs layout](#required-docs-layout)?
   - Smallest step:
     ```bash
     find docs -maxdepth 3 -type d | sort
     ```

2) Is MetaBlock validation enforced in CI?
   - Smallest step: search `.github/workflows` for `MetaBlock` / `linkcheck` / `markdownlint`.

3) Who are the canonical docs owners?
   - Smallest step: check `.github/CODEOWNERS`; then set `owners:` in this README and directory READMEs.

4) Do you already have a discovery/index mechanism for docs (for Focus Mode retrieval)?
   - Smallest step: search for `docs.index`, `registry`, or a docs manifest JSON/YAML and identify the canonical one.

5) Which directory is canonical for Story Nodes today: `docs/stories/` or `docs/reports/story_nodes/`?
   - Smallest step: run:
     ```bash
     ls -la docs/stories docs/reports/story_nodes 2>/dev/null
     ```

---

## FAQ
**Can I put PDFs, screenshots, or datasets in `docs/`?**  
**[CONFIRMED]** Not as a substitute for governed lifecycle artifacts. Small illustrative images are fine; datasets belong under `data/` zones. If you keep PDFs as references, treat them as **non-authoritative** and link them from `docs/reference/` rather than embedding policy in PDFs.

**What if I’m unsure whether something is sensitive?**  
**[CONFIRMED]** Redact/generalize, mark “needs governance review,” and do not publish precise locations until policy explicitly allows.

**Can I claim a folder exists if I haven’t verified it?**  
**[CONFIRMED]** No. Mark it **[UNKNOWN]** and list the smallest verification step.

**Where do machine contracts live?**  
**[PROPOSED]** Keep machine contracts in `contracts/` and maintain human indices in `docs/reference/` so people can find them quickly.

---

## Appendix

<details>
  <summary>Optional extensions (PROPOSED) if your repo needs them</summary>

If you need more separation, consider adding:

- `docs/releases/` — release notes, versioning strategy, deprecation policy
- `docs/accessibility/` — map/story accessibility and WCAG guidance
- `docs/compliance/` — FAIR+CARE operationalization, retention, privacy
- `docs/training/` — contributor training modules and exercises (non-authoritative)

If you add any of these, update:
- `docs/MASTER_GUIDE_v13.md` (doc map)
- this README’s tree
- `CODEOWNERS` routing for the new surfaces

</details>

---

## Back to top
⬆️ <a href="#top">Back to top</a>

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION/skeleton-map
title: Skeleton Map
type: architecture-orientation
version: v2-draft
status: draft / proposed
owners: OWNER_TBD
created: TODO(repo-commit-date)
updated: TODO(repo-commit-date)
policy_label: NEEDS VERIFICATION
proposed_path: docs/architecture/SKELETON_MAP.md
truth_posture: CONFIRMED doctrine / LINEAGE prior scaffold / PROPOSED placement / UNKNOWN repo implementation depth
source_lineage:
  - Current draft generated from SKELETON_MAP.md v1 draft in this workspace.
  - Prior greenfield scaffold supplied as old SKELETON_MAP source.
  - Directory Rules governs placement and responsibility-root interpretation.
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/trust-membrane.md
  - docs/doctrine/lifecycle-law.md
  - docs/architecture/contract-schema-policy-split.md
  - docs/registers/DRIFT_REGISTER.md
  - docs/registers/VERIFICATION_BACKLOG.md
tags:
  - kfm
  - architecture
  - skeleton-map
  - directory-rules
  - trust-membrane
  - lifecycle
  - greenfield-scaffold
notes:
  - PROPOSED path until mounted-repo inspection confirms docs/architecture convention.
  - UNKNOWN current implementation depth: this file does not prove routes, workflows, packages, schemas, tests, data stores, release objects, or runtime behavior exist.
[/KFM_META_BLOCK_V2] -->

# Kansas Frontier Matrix — Skeleton Map

A lineage-aware, doctrine-grounded orientation map for the Kansas Frontier Matrix repository skeleton, lifecycle spine, trust membrane, responsibility roots, domain lanes, and scaffold inventory.

> [!IMPORTANT]
> **Status:** PROPOSED / NEEDS VERIFICATION  
> **Owner:** OWNER_TBD  
> **Proposed path:** `docs/architecture/SKELETON_MAP.md`  
> **Truth posture:** CONFIRMED doctrine / LINEAGE prior scaffold / PROPOSED placement / UNKNOWN repo implementation depth

> [!NOTE]
> This document is a **human-facing orientation map**. It is not a schema registry, source registry, policy engine, release manifest, proof pack, control-plane register, workflow inventory of record, or implementation proof. Current repository behavior remains **UNKNOWN** until a mounted checkout, tests, workflows, manifests, logs, dashboards, runtime evidence, and emitted artifacts are inspected.

## Quick jumps

- [What this map is](#what-this-map-is)
- [Evidence boundary](#evidence-boundary)
- [No-loss preservation from the old map](#no-loss-preservation-from-the-old-map)
- [Placement basis](#placement-basis)
- [The seven planes](#the-seven-planes)
- [One-screen skeleton](#one-screen-skeleton)
- [Lifecycle invariant](#lifecycle-invariant)
- [Trust membrane](#trust-membrane)
- [Responsibility roots](#responsibility-roots)
- [Domain coverage intent](#domain-coverage-intent)
- [Cross-cutting planes](#cross-cutting-planes)
- [Connector source families](#connector-source-families)
- [Workflow inventory intent](#workflow-inventory-intent)
- [Reading order for a new contributor](#reading-order-for-a-new-contributor)
- [Compatibility roots](#compatibility-roots)
- [Object-family anchors](#object-family-anchors)
- [Tree inventory at a glance](#tree-inventory-at-a-glance)
- [Do not do this](#do-not-do-this)
- [Implementation sequence](#implementation-sequence)
- [Verification checklist](#verification-checklist)
- [Rollback](#rollback)
- [Open questions](#open-questions)

## What this map is

`SKELETON_MAP.md` gives maintainers a fast, reviewable view of KFM's intended repository skeleton.

It answers five practical questions:

1. **Where does a file belong?** Responsibility root first, topic second.
2. **What lifecycle is a file part of?** RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, PUBLISHED, or an adjacent receipt/proof/release family.
3. **Where is the public trust boundary?** Public clients use governed APIs and released artifacts, not canonical/internal stores.
4. **What must remain separate?** Contracts, schemas, policy, data lifecycle, receipts, proofs, catalogs, manifests, reviews, corrections, release decisions, and rollback targets.
5. **What did the old scaffold intend?** Prior greenfield scaffold material is preserved as LINEAGE and converted into safer implementation intent rather than current-repo claims.

It is **not** a machine-readable control-plane map. A future machine index of roots, owners, gates, source families, or document authority belongs under `control_plane/` after repo inspection and ADR review.

[Back to top](#kansas-frontier-matrix--skeleton-map)

## Evidence boundary

| Evidence item | Status | What it supports | What it does not prove |
|---|---|---|---|
| Directory Rules | CONFIRMED doctrine | Responsibility-root placement, domain-lane rule, canonical-vs-compatibility root discipline, lifecycle invariant, ADR/drift requirements | Current repo files or implementation behavior |
| Old greenfield skeleton map | LINEAGE | Seven-plane orientation, trust membrane diagram, lifecycle table, domain coverage intent, connector/workflow candidates, contributor reading order, large scaffold tree idea | That 2,442 files / 789 directories exist in the current repo |
| Current v1 draft | PROPOSED draft | Safer truth labels, KFM Meta Block pattern, verification/rollback posture, responsibility-root explanation | Current repo maturity |
| Current workspace | LIMITED evidence | The uploaded corpus and generated Markdown are available | A mounted KFM checkout, tests, workflows, manifests, dashboards, logs, or runtime traces |

### Reading posture

Throughout this file:

- **CONFIRMED doctrine** means supported by KFM governing documents or supplied project doctrine.
- **LINEAGE** means prior scaffold or report material preserved for continuity, not implementation proof.
- **PROPOSED** means target design or placement not yet verified in a mounted repo.
- **UNKNOWN** means current implementation depth has not been verified.
- **NEEDS VERIFICATION** means checkable before commit, release, or publication.

[Back to top](#kansas-frontier-matrix--skeleton-map)

## No-loss preservation from the old map

The old skeleton map was stronger than a simple directory tree. It carried an orientation model for how KFM is meant to feel to a maintainer. This revision keeps that value while removing unsafe implementation overclaims.

| Old-map element | Preservation decision | Adjustment made |
|---|---|---|
| Generated greenfield scaffold stats: 2,442 files / 789 directories | RETAINED as LINEAGE | No longer stated as current repo fact |
| Seven planes | RETAINED | Converted into a doctrine/placement map |
| Trust membrane ASCII diagram | RETAINED conceptually | Recast as trust-flow explanation and public-surface rule |
| Lifecycle transition table | RETAINED | Kept as governed-state-change table |
| Domain coverage matrix | RETAINED | Reframed as coverage intent, not proof that every file exists |
| Cross-cutting planes | RETAINED | Marked as PROPOSED homes pending repo inspection |
| Connector inventory | RETAINED | Marked as source-family candidates; connectors do not publish |
| Workflow inventory | RETAINED | Marked as intended CI gate families, not confirmed workflows |
| Contributor reading order | RETAINED | Kept as proposed onboarding order |
| Compatibility roots | RETAINED / UPDATED | Aligned with Directory Rules and compatibility-root posture |
| Depth-limited tree | PARTIALLY RETAINED | Reduced to root-level orientation here; full old tree remains lineage source |
| “What to do next” | RETAINED | Rewritten as implementation sequence with verification gates |

### Main safety correction

The old map used implementation-sounding language such as “ships,” “has,” and “freshly generated repository skeleton.” This revision uses **LINEAGE**, **PROPOSED**, and **NEEDS VERIFICATION** so maintainers do not confuse prior scaffold intent with current repository evidence.

[Back to top](#kansas-frontier-matrix--skeleton-map)

## Placement basis

**PROPOSED path:** `docs/architecture/SKELETON_MAP.md`

| Question | Answer | Status |
|---|---|---|
| Primary responsibility | Explains architecture and placement rules to humans | CONFIRMED doctrine basis |
| Owning root | `docs/` | PROPOSED until repo inspection |
| Cross-domain or domain-specific? | Cross-domain / system-wide | CONFIRMED from document purpose |
| Likely subfolder | `docs/architecture/` | PROPOSED |
| Requires ADR? | No, unless the repo lacks the root or uses a conflicting doc convention | NEEDS VERIFICATION |

Related paths to verify before commit:

| Path | Relationship | Status |
|---|---|---|
| `docs/doctrine/directory-rules.md` | Governs placement doctrine | NEEDS VERIFICATION |
| `docs/doctrine/trust-membrane.md` | Governs public/internal boundary | NEEDS VERIFICATION |
| `docs/doctrine/lifecycle-law.md` | Governs lifecycle spine | NEEDS VERIFICATION |
| `docs/architecture/contract-schema-policy-split.md` | Explains contract/schema/policy separation | NEEDS VERIFICATION |
| `docs/registers/DRIFT_REGISTER.md` | Records repo structure drift | NEEDS VERIFICATION |
| `docs/registers/VERIFICATION_BACKLOG.md` | Records unresolved placement and implementation checks | NEEDS VERIFICATION |

[Back to top](#kansas-frontier-matrix--skeleton-map)

## The seven planes

KFM is easier to maintain when the **planes** are visible before the **topics**. The planes overlap in subject matter but not in authority.

| Plane | What it owns | Proposed homes | Status |
|---|---|---|---|
| **Doctrine & architecture** | Why KFM exists; evidence-first, map-first, time-aware, policy-aware, cite-or-abstain doctrine; ADRs | `docs/doctrine/`, `docs/architecture/`, `docs/adr/` | PROPOSED homes / CONFIRMED doctrine role |
| **Trust contracts & shape** | Object-family meaning and machine-checkable shape | `contracts/`, `schemas/contracts/v1/` | PROPOSED / schema home NEEDS VERIFICATION |
| **Policy & admissibility** | Allow, deny, restrict, abstain, redaction, sensitivity floors, rights compatibility, promotion gates | `policy/` | PROPOSED / policy root NEEDS VERIFICATION |
| **Lifecycle data** | RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED; receipts, proofs, registries, manifests | `data/` | CONFIRMED doctrine / PROPOSED structure |
| **Implementation** | Apps, packages, connectors, pipelines, pipeline specs, tools, scripts | `apps/`, `packages/`, `connectors/`, `pipelines/`, `pipeline_specs/`, `tools/`, `scripts/` | PROPOSED roots |
| **Release & correction** | Release decisions, manifests, signatures, rollback cards, correction notices, withdrawal notices | `release/` | CONFIRMED doctrine / PROPOSED structure |
| **Runtime & exposure** | Local runtime, model adapters, deployment, network, hardening, deny-by-default exposure | `runtime/`, `infra/`, `configs/` | PROPOSED roots |

Adjacent support roots:

| Root | Role | Status |
|---|---|---|
| `control_plane/` | Machine-readable governance maps and authority registers | PROPOSED |
| `tests/` | Proof that doctrine is enforceable | PROPOSED |
| `fixtures/` | Golden, valid, invalid, and regression examples | PROPOSED |
| `migrations/` | Governed schema, database, graph, and data migrations | PROPOSED |
| `examples/` | Walkthroughs and runnable examples | PROPOSED |
| `artifacts/` | Compatibility / build / QA / temporary outputs only | COMPATIBILITY / NEEDS VERIFICATION |

[Back to top](#kansas-frontier-matrix--skeleton-map)

## One-screen skeleton

This is the responsibility-root baseline. It is a **placement map**, not proof that every root exists in the current repository.

```text
Kansas-Frontier-Matrix/
├── README.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── SECURITY.md
├── LICENSE
├── .github/                    # workflows, issue/PR templates, governance hooks
├── docs/                       # human-facing doctrine, architecture, runbooks, registers
├── control_plane/              # machine-readable governance maps and authority registers
├── contracts/                  # object-family meaning and semantic contracts
├── schemas/                    # machine-checkable shapes
├── policy/                     # allow / deny / restrict / abstain rules
├── tests/                      # enforceability proof
├── fixtures/                   # golden, valid, invalid, and regression samples
├── tools/                      # validators, generators, builders, checkers
├── scripts/                    # small operational helpers
├── apps/                       # deployable applications
├── packages/                   # shared implementation libraries
├── connectors/                 # source-specific fetchers and admitters
├── pipelines/                  # executable pipeline logic
├── pipeline_specs/             # declarative pipeline configuration
├── data/                       # lifecycle data and emitted proof memory
├── release/                    # release decisions, manifests, rollback, correction
├── runtime/                    # local runtime adapters and harnesses
├── infra/                      # deployment, host, network, exposure posture
├── configs/                    # non-secret defaults and templates
├── migrations/                 # database, schema, and graph migrations
├── examples/                   # worked, runnable examples
└── artifacts/                  # compatibility / temporary output only, not trust-object authority
```

> [!CAUTION]
> Do not create new root folders because a topic feels large. Root folders carry repo-wide responsibility. Domain depth lives inside lanes under the correct responsibility root.

[Back to top](#kansas-frontier-matrix--skeleton-map)

## Lifecycle invariant

KFM's durable lifecycle law is:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Every transition is a **governed state change**, not a file move.

```mermaid
graph LR
  A[Source edge] --> B[data/raw]
  B --> C[data/work]
  B --> D[data/quarantine]
  C --> E[data/processed]
  D --> E
  E --> F[data/catalog]
  E --> G[data/triplets]
  F --> H[data/published]
  G --> H

  R[data/receipts] -. process memory .- B
  P[data/proofs] -. evidence/proof closure .- E
  L[release/] -. release decision + rollback .- H
```

| Stage | Authority artifact | Validator / gate family | Status |
|---|---|---|---|
| Source admission | `data/registry/sources/<source>.yaml` + `data/receipts/ingest/` | `tools/validators/validate_source_descriptor.py` | PROPOSED paths |
| RAW → WORK | `data/receipts/pipeline/` | `tools/validators/validate_run_receipt.py` | PROPOSED paths |
| WORK → QUARANTINE | Quarantine case record | Per-domain validator | PROPOSED paths |
| WORK → PROCESSED | `data/receipts/validation/` | `tools/validators/validate_evidence_bundle.py` | PROPOSED paths |
| PROCESSED → CATALOG | `data/catalog/{stac,dcat,prov}/` | `tools/validators/validate_catalog_matrix.py` | PROPOSED paths |
| CATALOG → PROOF | `data/proofs/evidence_bundle/`, `data/proofs/proof_pack/` | `tools/proof_pack/assemble_proof_pack.py` | PROPOSED paths |
| PROOF → REVIEW | `release/promotion_decisions/` | `tools/validators/validate_promotion_gate.py` | PROPOSED paths |
| REVIEW → PUBLISHED | `release/manifests/` + `data/published/` | `tools/release/release_dry_run.py` | PROPOSED paths |
| Rollback | `release/rollback_cards/` | `tools/release/rollback_apply.py` | PROPOSED paths |
| Correction | `release/correction_notices/` + `release/withdrawal_notices/` | Governed review console / correction workflow | PROPOSED paths |

### Lifecycle rule of thumb

| Lifecycle family | What belongs there | What does not belong there |
|---|---|---|
| `data/raw/` | Admitted source material before transformation | Public map layers, release manifests, UI payloads |
| `data/work/` | Intermediate work products | Published artifacts or public truth claims |
| `data/quarantine/` | Unclear, conflicted, sensitive, rights-uncertain, or invalid material | Material silently promoted as if safe |
| `data/processed/` | Validated normalized derivatives | Public release decision records |
| `data/catalog/` | Catalog records and discovery metadata | Proof bundles without catalog closure |
| `data/triplets/` | Graph/triplet projections | Canonical truth replacements |
| `data/published/` | Released public-safe artifacts | RAW, WORK, QUARANTINE, or candidate artifacts |
| `data/receipts/` | Process memory and run receipts | Release decisions |
| `data/proofs/` | Proof packs and EvidenceBundle-related support | Temporary build artifacts |
| `release/` | Release decisions, manifests, correction, rollback | Data lifecycle phases |

[Back to top](#kansas-frontier-matrix--skeleton-map)

## Trust membrane

The trust membrane keeps raw, unreviewed, sensitive, model-generated, or internal state from becoming public truth.

```mermaid
graph TD
  subgraph Internal[Canonical / internal side]
    RAW[data/raw]
    WORK[data/work]
    QUAR[data/quarantine]
    PROC[data/processed]
    CAT[data/catalog]
    TRIP[data/triplets]
    PROOF[data/proofs]
    REC[data/receipts]
    REL[release/]
  end

  subgraph Membrane[Trust membrane]
    API[apps/governed-api]
    POLICY[policy]
    SCHEMAS[schemas]
    CONTRACTS[contracts]
    EVIDENCE[EvidenceRef -> EvidenceBundle]
    REVIEW[review state + release state]
  end

  subgraph Public[Public / semi-public surfaces]
    WEB[explorer web shell]
    REVIEWUI[review console]
    MAP[MapLibre / map renderer]
    EXPORT[reports / screenshots / exports]
    AI[Focus Mode / governed AI]
  end

  RAW -. denied .-> WEB
  WORK -. denied .-> WEB
  QUAR -. denied .-> WEB
  PROC --> CAT
  PROC --> TRIP
  CAT --> PROOF
  TRIP --> PROOF
  PROOF --> REL
  POLICY --> API
  SCHEMAS --> API
  CONTRACTS --> API
  EVIDENCE --> API
  REVIEW --> API
  REL --> API
  API --> WEB
  API --> REVIEWUI
  API --> MAP
  API --> EXPORT
  API --> AI
```

### Public surface rule

Public clients and normal UI surfaces use governed APIs, released artifacts, catalog records, tile services, policy decisions, review state, and EvidenceBundle resolution.

They do **not** read canonical stores, RAW, WORK, QUARANTINE, unpublished candidates, direct model runtimes, or internal graph projections as normal public paths.

### Renderer rule

The map shell, Evidence Drawer, Focus Mode, story player, screenshots, dashboards, vector indexes, graph projections, tiles, and summaries are **carriers of evidence**, not sovereign truth.

MapLibre is a disciplined 2D renderer and interaction runtime downstream of trust. It must not become the canonical store, source registry, policy engine, citation authority, review authority, publication authority, or AI authority.

[Back to top](#kansas-frontier-matrix--skeleton-map)

## Responsibility roots

KFM uses responsibility roots so a path makes ownership and governance visible.

| Root | Primary responsibility | Common contents | Common mistake |
|---|---|---|---|
| `docs/` | Human-facing doctrine, architecture, runbooks, status, registers | Doctrine docs, architecture maps, runbooks, registers | Treating prose as a release decision |
| `control_plane/` | Machine-readable governance maps | Authority maps, document registries, source-to-gate maps | Duplicating prose docs as machine truth without schema |
| `contracts/` | Object-family meaning | Semantic Markdown, interface meaning | Storing divergent JSON Schema here |
| `schemas/` | Machine-checkable shape | JSON Schema, schema indexes, versioned shapes | Creating parallel schema homes |
| `policy/` | Allow, deny, restrict, abstain | Rego/policy files, sensitivity rules, tests references | Hiding policy in code or docs only |
| `tests/` | Proof that rules are enforceable | Unit/integration/regression tests | Letting test-only validators become the only validator |
| `fixtures/` | Golden, valid, and invalid examples | Positive/negative examples | Fixture sprawl across competing homes |
| `tools/` | Repo-wide validators, generators, builders | Validation tools, manifest checkers, catalog emitters | App-specific code here |
| `scripts/` | Small operational helpers | Repo helpers, local setup scripts | Governance-bearing validators hidden as helpers |
| `apps/` | Deployable systems | Governed API, web shell, review console | Public app bypassing governed API |
| `packages/` | Shared libraries | Evidence resolver, map wrapper, domain helpers | One-off scripts masquerading as packages |
| `connectors/` | Source-specific fetchers/admitters | Source connectors, admission probes | Connector publishing directly |
| `pipelines/` | Executable processing logic | Transform jobs, promotion dry-runs | Pipeline skipping lifecycle phases |
| `pipeline_specs/` | Declarative pipeline config | Watcher specs, ingest specs | Runtime code instead of declarative config |
| `data/` | Lifecycle data and emitted proof memory | raw/work/quarantine/processed/catalog/triplets/published/receipts/proofs/registry | Mixing release decisions with data artifacts |
| `release/` | Release decision, rollback, correction | Release manifests, rollback cards, correction records | Storing release decisions in `artifacts/` |
| `runtime/` | Local runtime adapters/harnesses | Model adapters, local harnesses | Exposing runtime directly to public clients |
| `infra/` | Deployment and exposure posture | Host/network/deployment templates | Secret or policy-bearing content without gates |
| `configs/` | Non-secret defaults/templates | Config examples, defaults | Secrets or environment-specific private data |
| `migrations/` | Database/schema/graph migrations | SQL, graph, schema migration files | Domain docs or pipeline logic |
| `examples/` | Worked runnable examples | Small demos and tutorials | Canonical fixtures or production workflows |
| `artifacts/` | Compatibility/build/QA temporary outputs | Build products, doc QA outputs, scratch artifacts | Receipts, proofs, release manifests, published data |

### Domain lane rule

Domain names are lane segments, not root folders.

Use this pattern:

```text
<responsibility-root>/<domain-or-topic-segment>/...
```

Examples:

```text
docs/domains/hydrology/
contracts/domains/hydrology/
schemas/contracts/v1/domains/hydrology/
policy/domains/hydrology/
tests/domains/hydrology/
fixtures/domains/hydrology/
packages/domains/hydrology/
pipelines/domains/hydrology/
pipeline_specs/hydrology/
data/raw/hydrology/
data/work/hydrology/
data/quarantine/hydrology/
data/processed/hydrology/
data/catalog/domain/hydrology/
data/published/layers/hydrology/
data/registry/sources/hydrology/
release/candidates/hydrology/
```

> [!WARNING]
> If the mounted repo uses a different convention, do not silently treat that as canon. Record the conflict in the drift register or verification backlog and resolve by ADR or migration plan.

[Back to top](#kansas-frontier-matrix--skeleton-map)

## Domain coverage intent

The old skeleton intended every domain to have visible homes across responsibility roots. Treat the checkmarks below as **coverage intent**, not proof that files exist.

| Domain | docs | contracts | schemas | policy | tests | fixtures | packages | pipelines | pipeline_specs | data | release |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| hydrology | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| soil | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| atmosphere | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| geology | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| fauna | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| flora | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| habitat | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| archaeology | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| settlements-infrastructure | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| hazards | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| roads-rail-trade | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| agriculture | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| people-dna-land | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

### Domain-name normalization to verify

| Old scaffold term | Safer review note |
|---|---|
| `geology (bedrock, surficial, natural_resources)` | Verify whether subdomains live under one geology lane or separate lane segments. |
| `habitat (ecoregions, biotopes, land_cover)` | Verify whether habitat/land-cover split requires shared schemas or domain-specific schemas. |
| `people-dna-land` | Deny/restrict by default for living-person, DNA, genealogy, and ownership-sensitive claims. |
| `roads-rail-trade` | Verify whether this is the accepted domain slug or transport subdomain naming differs. |
| `settlements-infrastructure` | Verify handling of critical infrastructure and exact-location exposure. |

[Back to top](#kansas-frontier-matrix--skeleton-map)

## Cross-cutting planes

The old skeleton identified these cross-cutting planes. Paths remain **PROPOSED** until mounted-repo evidence confirms them.

| Cross-cutting plane | Proposed homes / surfaces | Review note |
|---|---|---|
| Governed AI | `docs/architecture/governed-ai/`, `runtime/model_adapters/`, `runtime/mock/`, `runtime/ollama/`, `schemas/contracts/v1/runtime/`, `schemas/contracts/v1/ui/focus_*`, `policy/focus/`, `policy/runtime/`, governed API focus route, explorer focus panel | AI is interpretive and subordinate to evidence, policy, review, and release state. |
| Whole UI | `docs/architecture/ui/`, explorer web shell, review console, `packages/ui`, map wrapper packages, `schemas/contracts/v1/ui/`, `policy/ui/` | Public UI must consume governed envelopes and released artifacts. |
| Evidence / provenance | `contracts/evidence/`, `schemas/contracts/v1/evidence/`, evidence resolver package, `data/proofs/evidence_bundle/`, PROV catalog output, evidence validators | EvidenceBundle outranks generated language and map rendering. |
| Registries | `control_plane/`, `data/registry/`, `docs/registers/` | Separate human registers, machine governance maps, and data source registries. |
| Ops & observability | `infra/`, `docs/security/`, `docs/runbooks/`, admin/workers surfaces, telemetry receipts | Telemetry must redact prompts, raw evidence, and restricted coordinates. |
| Publication membrane | governed API, `release/`, `data/published/`, `docs/architecture/publication/` | Publication requires proof, review, correction path, rollback target. |

[Back to top](#kansas-frontier-matrix--skeleton-map)

## Connector source families

Connector source families are **candidate source-admission lanes**, not publication authority. Connectors emit to RAW or QUARANTINE. They do not publish.

Old-scaffold source-family set:

```text
usgs · fema · noaa · nrcs · epa · blm · ahgp · khri · ksgs · kdwp ·
ksu_research_extension · kansas_state_archives · kansas_memory · loc ·
census · gbif · inaturalist · ebird · openstreetmap · newspapers ·
familysearch · ftDNA · local_upload · manual_curation
```

Proposed source descriptor pattern:

```text
data/registry/<domain>/sources/*.yaml
# or, if repo convention confirms it:
data/registry/sources/<domain>/*.yaml
```

Examples from the old scaffold, all **PROPOSED / NEEDS VERIFICATION**:

```text
wbd_huc12.yaml
nhdplus_hr.yaml
usgs_water_data.yaml
fema_nfhl.yaml
nrcs_ssurgo.yaml
gbif.yaml
inaturalist.yaml
blm_land_patents.yaml
```

### Connector rule

| Connector action | Allowed? | Reason |
|---|---:|---|
| Fetch source material into RAW | Yes, after SourceDescriptor and rights checks | Admission starts lifecycle. |
| Quarantine source material | Yes | Fail-closed handling for rights, sensitivity, integrity, or source-role uncertainty. |
| Write directly to PROCESSED | No | Skips validation and normalization gates. |
| Write directly to CATALOG / TRIPLET | No | Skips proof and catalog closure discipline. |
| Write directly to PUBLISHED | No | Publication is a governed state transition, not a connector action. |

[Back to top](#kansas-frontier-matrix--skeleton-map)

## Workflow inventory intent

The old scaffold listed workflow families that would enforce the trust membrane. Treat these as intended CI gates, not confirmed `.github/workflows/` files.

```text
schema-validation
contract-drift
policy-test
validator-suite
e2e-smoke
hydrology-proof-slice
release-dry-run
deny-test
citation-validation
accessibility
link-check
codeql
dependency-scan
docs-build
ui-build
api-test
source-descriptor-validate
connector-gate
promotion-gate
rollback-drill
evidence-resolver
focus-mock-test
telemetry-policy
docs-control-plane
```

Expected domain workflow pattern:

```text
.github/workflows/domain-<domain>.yml
```

> [!IMPORTANT]
> The deny suite is the first proof of the trust membrane: no RAW leak via API, no direct model-runtime exposure, no telemetry leak of raw evidence, no prompt leakage, no restricted-coordinate leakage, and no public exact sensitive geometry by default.

[Back to top](#kansas-frontier-matrix--skeleton-map)

## Reading order for a new contributor

This is a proposed onboarding order. Verify file names and paths in a mounted repo before turning it into a README link list.

1. `README.md` and `docs/doctrine/` — what KFM is.
2. `docs/architecture/SYSTEM_MAP.md` and `docs/architecture/DIRECTORY_RULES.md` or `docs/doctrine/directory-rules.md` — how it is laid out.
3. `docs/adr/` — what has been decided.
4. `contracts/OBJECT_MAP.md` — object → contract → schema → policy → fixture → validator → emit-home crosswalk, if present.
5. `control_plane/` — machine-readable registers.
6. `docs/domains/hydrology/` — first proof-bearing lane, if that remains accepted.
7. `apps/governed-api/` — trust membrane implementation, if present.
8. `apps/explorer-web/` — map-first shell, if present.
9. `pipelines/hydrology/` and `pipeline_specs/hydrology/` — executable logic and declarative specs, if present.
10. `release/` and `data/published/hydrology/` — what published actually looks like, if present.

[Back to top](#kansas-frontier-matrix--skeleton-map)

## Compatibility roots

Compatibility roots are not equal to canonical roots. They require an explicit README/class declaration and may need ADR treatment depending on scope.

| Compatibility root | Status | Allowed use | Not allowed |
|---|---|---|---|
| `artifacts/` | Compatibility / optional | Build, docs, QA, temporary outputs | Receipts, proofs, release manifests, published data |
| `jsonschema/` | Compatibility / legacy | Frozen/generated mirror if ADR allows | Parallel schema authority |
| `policies/` | Compatibility / legacy | Frozen/generated mirror if ADR allows | Parallel policy authority |
| `ui/` | Compatibility / legacy | Legacy shell or packaging root if documented | Competing public shell without ADR |
| `web/` | Compatibility / legacy | Legacy web root if documented | Competing public shell without ADR |
| `styles/` | Compatibility / legacy | Map/style assets if ADR or README governs | Unreleased style authority |
| `viewer_templates/` | Compatibility / legacy | Legacy viewer templates if documented | Public viewer authority outside governed release |

[Back to top](#kansas-frontier-matrix--skeleton-map)

## Object-family anchors

The skeleton is not only folders. It is also the separation of trust-bearing object families.

| Object family | Purpose | Likely responsibility root | Status |
|---|---|---|---|
| `SourceDescriptor` | Source identity, role, rights, cadence, sensitivity, authority limits | `schemas/` + `data/registry/` | PROPOSED / NEEDS VERIFICATION |
| `EvidenceBundle` | Resolved support package for claims | `schemas/` + `data/proofs/` | PROPOSED / NEEDS VERIFICATION |
| `EvidenceRef` | Reference that resolves to an EvidenceBundle | `schemas/` / `contracts/` | PROPOSED / NEEDS VERIFICATION |
| `DecisionEnvelope` | Finite policy/runtime outcome carrier | `schemas/` / `policy/` | PROPOSED / NEEDS VERIFICATION |
| `RuntimeResponseEnvelope` | ANSWER / ABSTAIN / DENY / ERROR response wrapper | `schemas/` + governed API | PROPOSED / NEEDS VERIFICATION |
| `RunReceipt` | Auditable process memory for intake/transform/release actions | `schemas/` + `data/receipts/` | PROPOSED / NEEDS VERIFICATION |
| `PromotionReceipt` | Promotion gate record | `schemas/` + `release/` | PROPOSED / NEEDS VERIFICATION |
| `ReleaseManifest` | Published release identity, contents, supersession, rollback target | `schemas/` + `release/` | PROPOSED / NEEDS VERIFICATION |
| `CatalogMatrix` | Catalog closure / coverage / relation surface | `schemas/` + `data/catalog/` | PROPOSED / NEEDS VERIFICATION |
| `CorrectionNotice` | Published correction or withdrawal record | `release/` | PROPOSED / NEEDS VERIFICATION |
| `RollbackCard` | Reversal target and rollback procedure | `release/` | PROPOSED / NEEDS VERIFICATION |
| `LayerManifest` | Map/UI layer identity, source/evidence binding, release state | `schemas/` + `data/published/` | PROPOSED / NEEDS VERIFICATION |
| `MapReleaseManifest` | Cohesive map release bundle | `schemas/` + `release/` | PROPOSED / NEEDS VERIFICATION |
| `AIReceipt` | Records governed AI invocation metadata without preserving private chain-of-thought | `schemas/` + `data/receipts/` | PROPOSED / NEEDS VERIFICATION |

> [!WARNING]
> Do not collapse object families because they share a topic. Receipts, proofs, catalog records, release decisions, reviews, correction notices, and rollback targets answer different governance questions.

[Back to top](#kansas-frontier-matrix--skeleton-map)

## Tree inventory at a glance

The old scaffold described a depth-limited tree with **2,442 files** and **789 directories**. This revision does not repeat the full tree in the main body because doing so can make unverified paths look implemented. The old tree should remain a LINEAGE artifact until a mounted repo inspection confirms or supersedes it.

Root-level families recorded by the old scaffold:

```text
.github/
apps/
artifacts/
configs/
connectors/
contracts/
control_plane/
data/
docs/
examples/
fixtures/
infra/
migrations/
packages/
pipeline_specs/
pipelines/
policy/
release/
runtime/
schemas/
scripts/
tests/
tools/
.editorconfig
.env.example
.gitignore
.pre-commit-config.yaml
AUTHORS.md
CHANGELOG.md
CITATION.cff
... additional root files
```

### Legacy tree handling rule

| Situation | Handling |
|---|---|
| Old tree path matches Directory Rules and mounted repo | Keep or promote after verification. |
| Old tree path matches Directory Rules but is absent from repo | Treat as PROPOSED; create only through normal PR and review. |
| Old tree path conflicts with Directory Rules | Mark CONFLICTED; open drift entry or ADR. |
| Old tree path creates parallel authority | Do not create until ADR resolves authority. |
| Old tree path is a domain root | Reject or migrate into responsibility-root lane. |

[Back to top](#kansas-frontier-matrix--skeleton-map)

## Do not do this

| Anti-pattern | Why it breaks KFM | Safer handling |
|---|---|---|
| `hydrology/` at repo root | Domain folder fragments lifecycle and ownership | Use `docs/domains/hydrology/`, `data/<phase>/hydrology/`, etc. |
| `policies/` and `policy/` both active | Creates parallel policy authority | Verify canonical root; freeze/migrate mirror through ADR |
| `contracts/` and `schemas/` both defining JSON Schema | Creates divergent machine authority | Keep `schemas/contracts/v1/...` as default until ADR/repo evidence says otherwise |
| Public UI reads `data/processed/` directly | Bypasses trust membrane | Route through governed API and released artifacts |
| Connector writes to `data/published/` | Skips admission and promotion gates | Connector emits RAW or QUARANTINE candidates only |
| Watcher publishes | Turns observation into release | Watcher emits receipts and candidate decisions only |
| `artifacts/` stores trust objects | Blurs temporary output with receipts/proofs/release decisions | Keep trust objects in `data/receipts/`, `data/proofs/`, and `release/` |
| AI answer becomes source of truth | Generated language is interpretive | Resolve EvidenceBundle, validate citations, then answer or abstain |
| Map tile becomes truth | Tiles are delivery artifacts | Bind tiles to manifests, catalog, evidence, policy, release, rollback |
| Sensitive geometry is published exactly by default | Creates ecological, archaeological, cultural, privacy, or security risk | Redact, generalize, quarantine, staged access, or deny |
| Documentation page acts as canonical release decision | Docs explain; they do not decide alone | Promote decision to ADR, release manifest, or control-plane register as appropriate |
| Test-only validator becomes the validator | Tests are proof, not the only tool | Extract validator to `tools/validators/`; tests call it |

[Back to top](#kansas-frontier-matrix--skeleton-map)

## Minimal review flow

Use this flow before adding, moving, or renaming a path referenced by this map.

```mermaid
flowchart TD
  A[Proposed file or folder] --> B{Primary responsibility?}
  B -->|human explanation| DOCS[docs]
  B -->|machine governance map| CP[control_plane]
  B -->|object meaning| CONTRACTS[contracts]
  B -->|machine shape| SCHEMAS[schemas]
  B -->|allow / deny / restrict / abstain| POLICY[policy]
  B -->|lifecycle data / proof memory| DATA[data]
  B -->|release decision| RELEASE[release]
  B -->|runtime / app / package / tool| IMPL[apps / packages / tools / runtime / etc]

  DOCS --> C{Domain-specific?}
  CP --> C
  CONTRACTS --> C
  SCHEMAS --> C
  POLICY --> C
  DATA --> D{Lifecycle phase?}
  RELEASE --> C
  IMPL --> C

  D --> C
  C -->|yes| LANE[Use domain segment under responsibility root]
  C -->|no| CROSS[Use cross-domain topic segment]
  LANE --> E{Root exists and convention verified?}
  CROSS --> E
  E -->|yes| F[Proceed with PR + cited rule]
  E -->|no or conflict| G[Open verification/drift item or ADR]
```

[Back to top](#kansas-frontier-matrix--skeleton-map)

## Implementation sequence

This sequence preserves the old map's “trim/promote” intent while adding current truth labels and verification gates.

1. **Seal the doctrine layer.** Read `docs/doctrine/`, accept or rewrite, then promote through ADRs or doctrine-register process. **Status:** PROPOSED / NEEDS VERIFICATION.
2. **Seal canonical homes.** Confirm `schemas/contracts/v1/` as schema home, `contracts/` as semantic/object meaning home, and `policy/` as canonical policy home. **Status:** NEEDS VERIFICATION.
3. **Pick the first proof slice.** The older scaffold and KFM corpus repeatedly point toward hydrology as a safe first proof lane. Keep other domain stubs as deferred coverage intent until review. **Status:** PROPOSED.
4. **Build trust membrane stubs first.** Governed API fixtures can return finite outcomes such as ABSTAIN before live source activation. **Status:** PROPOSED.
5. **Land deny suite early.** Deny tests should pass before any real public surface or live connector. **Status:** PROPOSED.
6. **Wire receipts, proofs, catalog, and release dry-run.** The first slice should emit process memory, proof closure, catalog closure, and rollback target. **Status:** PROPOSED.
7. **Trim what you do not need.** The old scaffold was intentionally over-rich. Delete or defer unverified stubs rather than letting them harden into false authority. **Status:** PROPOSED.

[Back to top](#kansas-frontier-matrix--skeleton-map)

## Evidence basis

| Source | Status | Supports | Limits |
|---|---|---|---|
| Directory Rules | CONFIRMED doctrine | Responsibility-root placement, lifecycle invariant, domain lane rule, ADR/drift requirements, compatibility-root risks | Does not prove current repo contents |
| Old SKELETON_MAP source | LINEAGE | Seven planes, trust membrane, lifecycle table, domain coverage matrix, connector/workflow inventory, reading order, compatibility roots, tree inventory, next-step sequence | Does not prove the current repo has generated files or workflows |
| KFM Markdown Authoring guidance | CONFIRMED operating guidance | Truth labels, repo-unavailable fallback, GitHub Markdown expectations, no overclaiming, preservation of strong existing material | Does not prove repository implementation |
| KFM greenfield/build doctrine | CONFIRMED doctrine / PROPOSED implementation baseline | Responsibility-root monorepo, trust spine, promotion as governed transition | Greenfield/proposed material is not current repo proof |
| Current drafting environment | CONFIRMED limited evidence | Uploaded source corpus and generated Markdown available | Mounted repo, tests, workflows, manifests, logs, dashboards, and emitted artifacts not inspected |

[Back to top](#kansas-frontier-matrix--skeleton-map)

## Verification checklist

Before committing this file, verify:

- [ ] Target path is confirmed or intentionally accepted: `docs/architecture/SKELETON_MAP.md`.
- [ ] Adjacent docs exist or placeholders are updated: `docs/doctrine/directory-rules.md`, `docs/doctrine/trust-membrane.md`, `docs/doctrine/lifecycle-law.md`.
- [ ] Owner is assigned in the meta block and PR.
- [ ] `policy_label` is confirmed with docs steward.
- [ ] Links are converted from `NEEDS VERIFICATION` text to valid relative links only after repo inspection.
- [ ] Root names match accepted Directory Rules and ADRs.
- [ ] Schema-home convention is confirmed by ADR and repo evidence.
- [ ] `policy/` versus `policies/` convention is confirmed.
- [ ] `data/triplets/` spelling and role are confirmed.
- [ ] `artifacts/` compatibility posture is confirmed.
- [ ] `apps/governed-api/`, `apps/explorer-web/`, `ui/`, and `web/` boundaries are verified before any app path appears as fact.
- [ ] Old scaffold tree entries are either verified, migrated, deferred, or marked superseded.
- [ ] No sentence claims current implementation depth without source, test, workflow, manifest, log, dashboard, runtime, or emitted-artifact evidence.
- [ ] Mermaid diagrams render in GitHub.
- [ ] No public path bypasses governed APIs or released artifacts.
- [ ] Rollback path is documented in the PR.

[Back to top](#kansas-frontier-matrix--skeleton-map)

## Rollback

Rollback is required if this file:

- points maintainers to an unverified or wrong canonical root;
- creates a parallel schema, contract, policy, source, registry, release, receipt, proof, or lifecycle home;
- implies implementation maturity that has not been verified;
- weakens the RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED lifecycle;
- normalizes public access to canonical/internal stores;
- omits sensitivity, rights, policy, review, correction, or rollback boundaries;
- upgrades old scaffold paths from LINEAGE to current implementation without evidence.

Rollback target: `ROLLBACK_TARGET_TBD_AFTER_REPO_INSPECTION`

Suggested rollback action:

1. Revert this file with `git revert` or `git restore` according to repository policy.
2. Open or update `docs/registers/DRIFT_REGISTER.md` if the problem is a path/authority conflict.
3. Open or update `docs/registers/VERIFICATION_BACKLOG.md` if the problem is missing evidence.
4. If a root or schema-home convention was affected, require ADR review before reintroducing the change.

[Back to top](#kansas-frontier-matrix--skeleton-map)

## Open questions

| Question | Why it matters | Status |
|---|---|---|
| Is `docs/architecture/SKELETON_MAP.md` the accepted path? | Determines link targets and ownership | NEEDS VERIFICATION |
| Is `schemas/contracts/v1/` accepted as canonical schema home? | Prevents contract/schema drift | NEEDS VERIFICATION |
| Are `policy/` and `policies/` both present? | Prevents parallel policy authority | NEEDS VERIFICATION |
| Is `data/triplets/` the accepted spelling? | Prevents lifecycle sibling drift | NEEDS VERIFICATION |
| Is `artifacts/` retained as compatibility or retired? | Prevents trust-object mixing | NEEDS VERIFICATION |
| Which app path is the public shell? | Prevents UI root drift | UNKNOWN |
| Which app path is the governed API? | Defines trust membrane implementation | UNKNOWN |
| Which package owns EvidenceBundle resolution? | Needed before claims about runtime behavior | UNKNOWN |
| Should the full old 2,442-file tree be kept as appendix, separate lineage document, or retired? | Balances no-loss continuity against overclaiming risk | NEEDS VERIFICATION |

[Back to top](#kansas-frontier-matrix--skeleton-map)

<details>
<summary>Appendix A — Copy/paste placement test</summary>

```text
Placement test for SKELETON_MAP.md

Primary responsibility:
- Human-facing architecture and repository skeleton explanation.

Proposed path:
- docs/architecture/SKELETON_MAP.md

Directory Rules basis:
- Human explanation belongs under docs/.
- Cross-domain architecture belongs under docs/architecture/ rather than a domain lane.
- Domain names are not root folders.
- Old scaffold tree is lineage/proposed unless mounted repo evidence verifies it.

Evidence boundary:
- CONFIRMED doctrine.
- LINEAGE old scaffold.
- PROPOSED path.
- UNKNOWN repo implementation depth.

Required checks:
- Confirm docs/architecture/ convention in mounted repo.
- Confirm adjacent doctrine docs and registers.
- Confirm no root/schema/policy/lifecycle conflict.
- Confirm whether old scaffold paths are retained, migrated, deferred, or superseded.
```

</details>

<details>
<summary>Appendix B — One-line maintainer summary</summary>

`SKELETON_MAP.md` is the human-facing map of KFM responsibility roots, lifecycle phases, trust membrane, domain lanes, object-family separation, and prior greenfield scaffold intent; it is not proof of current implementation and must remain synchronized with Directory Rules, ADRs, mounted-repo evidence, and drift/verification registers.

</details>

# 🧱 KFM Architecture

**Folder:** `docs/architecture/`  
**Purpose:** Governed system design docs, blueprints, ADRs (architecture decision records), and diagrams for the Kansas Frontier Matrix (KFM).

> [!NOTE]
> This folder is intentionally *build-oriented*: architecture docs here should name **boundaries**, **contracts**, **validation gates**, and **acceptance criteria** (not just describe ideas).

---

## 📌 What belongs here

| Artifact type | What it is | When to use | Where it lives |
|---|---|---|---|
| **System overview** | “How the whole system works” at a glance | You need the mental model / onboarding | `docs/architecture/system_overview.md` *(if present)* |
| **Blueprints** | Multi-page designs/roadmaps | You’re defining a large design slice | `docs/architecture/KFM_*_BLUEPRINT*.md` |
| **ADRs** | Decision logs (with alternatives + tradeoffs) | You’re making a meaningful architecture decision | `docs/architecture/adr/ADR-####-<slug>.md` |
| **Diagrams** | C4-style context/container diagrams, flows | You need a visual that stays in sync | `docs/architecture/diagrams/` |

> [!TIP]
> If it’s **domain-specific ETL** or a **dataset runbook**, it probably belongs under `docs/data/<domain>/` (not here).  
> If it’s **schemas/contracts**, it belongs under `schemas/` (and is referenced from here).

---

## 🗂️ Expected layout

```text
docs/architecture/
├── README.md
├── system_overview.md                    # (if present) single-page “map of the system”
├── KFM_REDESIGN_BLUEPRINT_v13.md         # v13 restructure + rationale
├── KFM_NEXT_STAGES_BLUEPRINT.md          # roadmap beyond v13
├── KFM_VISION_FULL_ARCHITECTURE.md       # long-horizon architecture vision
├── diagrams/
│   ├── c4-context.mmd                    # optional
│   ├── c4-container.mmd                  # optional
│   └── flows/                            # optional
└── adr/
    ├── ADR-0001-example.md               # example decision record
    └── ADR-0002-<slug>.md
```

> [!IMPORTANT]
> If this folder drifts from the “expected layout” above, **update this README** and/or the governing docs that define the canonical structure.

---

## 🧭 Read order

Use this when you’re not sure where to start:

1. **`docs/MASTER_GUIDE_v13.md`** — canonical pipeline ordering + repo structure (system-wide source of truth)
2. **`docs/architecture/system_overview.md`** — one-page “how KFM works”
3. **Blueprints** — deeper design slices and roadmap
4. **ADRs** — why we chose X instead of Y (the durable decision trail)

---

## 🧷 Architecture invariants (must not regress)

> [!WARNING]
> These are “load-bearing” invariants.  
> If you believe one must change, write an ADR titled **“Change an invariant: <name>”** and route it through governance review.

### 1) Trust membrane is mandatory
- The **frontend never** talks to databases/object storage directly.
- **Policy evaluation** happens on every relevant request.
- Backend logic uses **repository interfaces (ports)** and cannot bypass them.
- **Audit + provenance** are produced as part of the normal request path.

### 2) Canonical pipeline ordering is inviolable
KFM’s data/narrative system must follow the strict ordering:

- **ETL → STAC/DCAT/PROV catalogs → graph → APIs → UI → Story Nodes → Focus Mode**

No stage may leapfrog or bypass a prior stage’s contracts or outputs.

### 3) Contract-first is the default
- Schemas and API contracts are *first-class repo artifacts*.
- Contract changes require explicit versioning and compatibility consideration.

### 4) Deterministic, idempotent pipelines
- ETL is config-driven, replayable, and fully logged.
- Same inputs ⇒ same outputs (within declared versioning rules).

### 5) Evidence-first narrative (and AI must cite or abstain)
- Story Nodes/Focus Mode must resolve claims to cataloged evidence.
- AI assistance is constrained by evidence and policy (no unsourced narrative).

### 6) Sensitivity and sovereignty are enforced in-machine
- Sensitive locations / culturally restricted knowledge require generalization and restricted handling.
- Redaction/masking is implemented as enforceable metadata + policy, not “nice-to-have” prose.

---

## 🗺️ Conceptual system model (C4-ish)

```mermaid
flowchart LR
  %% --- Data truth path ---
  S[Heterogeneous sources] --> RAW[data/raw/ (immutable snapshots)]
  RAW --> ETL[src/pipelines/ (ETL + transforms)]
  ETL --> PROC[data/processed/ (derived artifacts)]
  PROC --> CAT[Catalog boundary artifacts\nSTAC + DCAT + PROV]

  %% --- Storage targets ---
  CAT --> PG[(PostGIS\ngeo + tiles)]
  CAT --> KG[(Neo4j\nknowledge graph)]
  CAT --> OS[(Object store\nCOGs + media)]
  CAT --> SV[(Search/Vector\nOpenSearch/PG)]

  %% --- Runtime / access path ---
  UI[Web UI\nReact/TS + MapLibre] -->|requests| API[API Gateway\nFastAPI REST\n(+ optional GraphQL)]
  API --> PDP[Policy PDP\nOPA/Rego]
  API --> SVC[Use Cases / Services]
  SVC --> PORTS[Repository Ports (interfaces)]
  PORTS --> ADAPT[Adapters]
  ADAPT --> PG
  ADAPT --> KG
  ADAPT --> OS
  ADAPT --> SV

  %% --- Governance outputs ---
  SVC --> AUDIT[Audit + provenance writer]
  AUDIT --> LEDGER[(Append-only audit ledger)]

  %% --- Narrative surfaces ---
  UI --> STORY[Story Nodes\n(governed)]
  UI --> FOCUS[Focus Mode\n(cite-or-abstain)]
```

> [!NOTE]
> Treat the **catalog boundary artifacts** (STAC/DCAT/PROV) as the “glue layer” that binds pipelines to graph, APIs, UI, and narrative.

---

## 🧼 Clean layers (implementation contract)

```mermaid
flowchart TB
  INFRA[Infrastructure\n(DB clients, OPA adapter, web handlers)] --> INTEG[Integration\n(ports/contracts + DTOs)]
  INTEG --> UC[Use Cases / Services\n(workflows + business rules)]
  UC --> DOM[Domain\n(entities/value objects + invariants)]

  %% Dependency rule: arrows point inward only
  %% Outer layers may depend on inner; inner must not depend on outer
```

**Dependency rule:** outer layers can depend inward; inner layers **must not** depend outward.

---

## 🧾 ADRs

### When an ADR is required
Write an ADR when you:
- introduce or change a **core subsystem boundary**
- change a **contract** (schemas, OpenAPI, GraphQL SDL, policy interface)
- add or swap a **storage technology**
- change **pipeline ordering**, **promotion gates**, **policy model**, or **audit/provenance semantics**
- affect **sensitivity handling** (public vs restricted derivatives)

### ADR naming + placement
- Path: `docs/architecture/adr/ADR-####-<slug>.md`
- Use monotonically increasing numbers (`ADR-0001`, `ADR-0002`, ...)

<details>
<summary><strong>Minimal ADR template</strong> (copy/paste)</summary>

```markdown
# ADR-####: <Decision title>

- **Status:** proposed | accepted | superseded | deprecated
- **Date:** YYYY-MM-DD
- **Authors:** <names/handles>
- **Related:** <links or paths to issues/docs>

## Context
What problem are we solving? What constraints/invariants apply?

## Decision
What are we doing? What is the boundary/contract?

## Alternatives considered
List viable options and why they were rejected.

## Consequences
- Positive:
- Negative:
- Tradeoffs:

## Governance / FAIR+CARE / Sensitivity
What changes in access control, redaction, sovereignty, or ethics?

## Security & Compliance
Threat model notes, authz impacts, logging/audit expectations.

## Validation plan
What tests/CI gates prove this works and doesn’t regress invariants?

## Rollout / Backout
How do we ship safely? How do we revert?

## References
Paths to source docs, datasets, schemas, policies.
```
</details>

---

## ✅ Definition of Done for architecture changes

Use this checklist for PRs that touch architecture docs or architecture behavior:

- [ ] **ADR added/updated** (if decision is non-trivial)
- [ ] **Invariants checked** (trust membrane + pipeline ordering + contracts)
- [ ] **Contracts updated** (schemas/OpenAPI/GraphQL) *if applicable*
- [ ] **Policy updated + tested** (OPA/Rego) *if applicable*
- [ ] **Provenance/audit impacts documented** (what logs, where, how retained)
- [ ] **Migration plan included** (data/story/API compatibility)
- [ ] **Diagrams updated** (if architecture changed)
- [ ] **Validation steps are repeatable** (commands, tests, CI gates)
- [ ] **Sensitivity review performed** (if precise locations/cultural restrictions involved)

---

## 🔍 Governance + safety notes (architecture-level)

> [!CAUTION]
> Avoid placing precise sensitive locations, private-person identifiers, or culturally restricted information directly in architecture docs.
> If the architecture needs to reference restricted handling, describe it **abstractly** and point to governance/policy artifacts.

---

## 🧭 Maintenance rules for this folder

- Keep docs **short-lived in draft**: if a blueprint is used for implementation, promote it to “accepted” status (or split into ADRs).
- Keep ADRs **immutable**: supersede with a new ADR rather than rewriting history.
- Keep diagrams **text-first** where possible (Mermaid / `.mmd`) so they can be reviewed in PRs.

---

## 🕰️ Change log (README)

- **YYYY-MM-DD** — Initial `docs/architecture/README.md` scaffold.
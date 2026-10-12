<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/fauna-map-ui-contracts
title: Fauna — Map UI Contracts
type: standard
version: v1.1
status: draft
owners: <fauna-steward> + <ui-steward> + <governed-api-steward>  # PLACEHOLDER — confirm in CODEOWNERS
created: 2026-05-16
updated: 2026-06-02
policy_label: public
contract_version: "3.0.0"
related:
  - docs/domains/fauna/README.md                                          # PROPOSED — NEEDS VERIFICATION
  - docs/domains/fauna/IDENTITY_MODEL.md                                  # PROPOSED — companion in this series
  - docs/architecture/ui/LAYERING.md                                      # PROPOSED — NEEDS VERIFICATION
  - docs/architecture/ui/BOUNDARIES.md                                    # PROPOSED — NEEDS VERIFICATION
  - docs/architecture/governed-ai/FOCUS_FLOW.md                           # PROPOSED — NEEDS VERIFICATION
  - docs/runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md                         # CONFIRMED — drafted in this project series
  - ai-build-operating-contract.md                                        # CONFIRMED — canonical operating contract v3.0
  - directory-rules.md                                                    # CONFIRMED — this project (v1.2/v1.3)
  - policy/domains/fauna/README.md                                        # PROPOSED — NEEDS VERIFICATION
  - policy/sensitivity/fauna/README.md                                    # PROPOSED — NEEDS VERIFICATION
  - schemas/contracts/v1/map/layer_manifest.schema.json                   # PROPOSED — MapLibre Master v2.1 §11
  - schemas/contracts/v1/ui/evidence_drawer_payload.schema.json           # PROPOSED — MapLibre Master v2.1 §11
  - schemas/contracts/v1/ui/map_context_envelope.schema.json              # PROPOSED — MapLibre Master v2.1 §11
  - schemas/contracts/v1/ai/focus_mode_response.schema.json               # PROPOSED — MapLibre Master v2.1 §11
  - schemas/contracts/v1/ai/ai_receipt.schema.json                        # PROPOSED — MapLibre Master v2.1 §11
tags: [kfm, fauna, ui, maplibre, evidence-drawer, focus-mode, sensitivity, geoprivacy, trust-membrane]
notes:
  - "CONTRACT_VERSION = 3.0.0 pinned per ai-build-operating-contract.md."
  - All paths quoted are PROPOSED until verified against mounted-repo evidence.
  - Anchors are stable except §9 negative-state names; see Changelog for reconciliation to operating-contract §22.2 vocabulary.
  - "RuntimeResponseEnvelope (with FocusModeResponse + AIReceipt for AI surfaces) is canonical; the bespoke DecisionEnvelope is retired — see §6 and Changelog."
  - Schema homes corrected to map/ , ui/ , ai/ per MapLibre Master v2.1 §11 (was layers/ , runtime/decision_envelope).
[/KFM_META_BLOCK_V2] -->

# 🦌 Fauna — Map UI Contracts

> **Binds the Fauna domain to KFM's governed Map UI: which fauna layers may render, what an `EvidenceDrawerPayload` for a fauna feature must carry, how clicks resolve, how Focus Mode answers about fauna, and which sensitivity, freshness, and release gates fail closed at the renderer boundary.**

![Status](https://img.shields.io/badge/status-draft-yellow)
![Contract](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-1565c0)
![Doc type](https://img.shields.io/badge/type-standard-blue)
![Domain](https://img.shields.io/badge/domain-fauna-2E8B57)
![Renderer boundary](https://img.shields.io/badge/renderer-MapLibre%20%E2%87%92%20downstream-informational)
![Sensitivity default](https://img.shields.io/badge/sensitive%20occurrence-deny--by--default-critical)
![Truth posture](https://img.shields.io/badge/truth-cite--or--abstain-success)
![Last updated](https://img.shields.io/badge/last%20updated-2026--06--02-lightgrey)
<!-- TODO: replace with real Shields.io endpoints once CI/release badges land. -->

| Field | Value |
|---|---|
| **Status** | `draft` — awaiting steward + UI + governed-API review |
| **Version** | `v1.1` |
| **Owners** | Fauna steward · UI steward · Governed-API steward *(PLACEHOLDER — confirm CODEOWNERS)* |
| **Last reviewed** | 2026-06-02 |
| **Authority level** | Implementation-bearing standard for the Fauna × Map UI seam |
| **Schema home** | `schemas/contracts/v1/...` per ADR-0001 (PROPOSED until verified) |
| **Companion runbooks** | `docs/runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md`, `docs/runbooks/ui_VALIDATION.md` *(PROPOSED)* |

---

## 📑 Contents

1. [Purpose and scope](#1-purpose-and-scope)
2. [Authority, evidence, and truth labels](#2-authority-evidence-and-truth-labels)
3. [Trust-membrane invariants for Fauna map UI](#3-trust-membrane-invariants-for-fauna-map-ui)
4. [Fauna layer families and viewing modes](#4-fauna-layer-families-and-viewing-modes)
5. [LayerDescriptor / LayerManifest profile for Fauna](#5-layerdescriptor--layermanifest-profile-for-fauna)
6. [Click resolution and EvidenceDrawerPayload profile](#6-click-resolution-and-evidencedrawerpayload-profile)
7. [Focus Mode behavior for Fauna](#7-focus-mode-behavior-for-fauna)
8. [Sensitivity gates and geoprivacy transforms](#8-sensitivity-gates-and-geoprivacy-transforms)
9. [Trust-visible states, badges, and negative outcomes](#9-trust-visible-states-badges-and-negative-outcomes)
10. [Time-aware behavior](#10-time-aware-behavior)
11. [Anti-patterns (fail closed)](#11-anti-patterns-fail-closed)
12. [Validation, tests, and fixtures](#12-validation-tests-and-fixtures)
13. [Open questions register](#13-open-questions-register)
14. [Open verification backlog](#14-open-verification-backlog)
15. [Changelog](#15-changelog)
16. [Definition of done](#16-definition-of-done)
17. [Related docs](#17-related-docs)

---

## 1. Purpose and scope

**Purpose.** This document defines the **contracts a fauna feature must satisfy before it is rendered, clicked, summarized, exported, or explained** through any KFM map UI surface — `apps/explorer-web/`, `packages/maplibre/`, `packages/ui/`, or any downstream client consuming the same governed API. It is the binding seam between Fauna domain doctrine (taxonomy, occurrence evidence, sensitivity, geoprivacy) and the cross-cutting Map UI doctrine (`LayerManifest`, `StyleManifest`, `TileArtifactManifest`, `MapReleaseManifest`, `EvidenceDrawerPayload`, `MapContextEnvelope`, and the finite `RuntimeResponseEnvelope` / `FocusModeResponse` outcomes).

It is **not**:

- a layer registry (that lives in `data/published/layers/fauna/` and `data/registry/sources/fauna/`),
- a schema definition (machine shape lives under `schemas/contracts/v1/...`),
- a policy bundle (`policy/domains/fauna/...` and `policy/sensitivity/fauna/...`),
- a source dossier (`docs/domains/fauna/README.md` and the Fauna source registry).

> [!IMPORTANT]
> If this document and a current `LayerManifest` / `EvidenceDrawerPayload` / `MapContextEnvelope` schema disagree, the **schema wins** and a Drift Register entry is opened. Markdown explains; schemas enforce. *(Operating contract: "Markdown explains; schemas enforce" — `[ENCY]`, `[MAP-MASTER]`.)*

### 1.1 In scope

- Which fauna **layer families** are admissible on a public map.
- Which fields a fauna `LayerManifest` / layer descriptor MUST/MAY/MUST-NOT carry.
- What happens on **feature click** for a fauna feature, and what an `EvidenceDrawerPayload` MUST contain.
- How **Focus Mode** answers fauna questions (cite-or-abstain, deny on sensitive).
- How **sensitivity** is enforced *upstream of style* — never by style filter alone.
- How **trust-visible states** (`SOURCE_STALE`, `GENERALIZED_GEOMETRY`, `DENIED_BY_POLICY`, `RESTRICTED_ACCESS`, etc.) are surfaced.
- Anti-patterns and the test catalog that proves the contract holds.

### 1.2 Out of scope

- 3D scene rendering for fauna (deferred; same evidence/policy continuity rule applies when admitted, governed by the maplibre-3d admission policy).
- Steward exact-location console (separate restricted surface, not part of public Map UI).
- Live source connector implementation (governed by Fauna source dossier and source registry).
- Provider-specific Focus Mode model adapter (`apps/governed-api/src/ai/...` — governed-AI scope).

[⬆ Back to top](#-contents)

---

## 2. Authority, evidence, and truth labels

### 2.1 Authority order

The authority order in `directory-rules.md` §2.1 and the operating contract's Authority Ladder apply. For this document specifically:

1. **`ai-build-operating-contract.md` v3.0** — canonical operating law (`CONTRACT_VERSION = "3.0.0"`).
2. **KFM core invariants** — lifecycle law, trust membrane, cite-or-abstain, watcher-as-non-publisher, sensitivity fail-closed for sensitive taxa.
3. **Fauna doctrine** — `[DOM-FAUNA]`, `[DOM-HF]`, Encyclopedia.
4. **Map UI doctrine** — `[MAP-MASTER]` (Master MapLibre Components-Functions-Features v2.1), `[UIAI]`.
5. **Governed-AI doctrine** — `[GAI]` for Focus Mode bounds.
6. **Directory Rules** — for path placement; §12 Domain Placement Law applies to every path quoted below.
7. **ADRs** (e.g., ADR-0001 schema home; ADR-S-05 sensitivity tier scheme; ADR-S-06 AI surface boundary) — *PROPOSED until verified in mounted repo.*
8. **This document.**

### 2.2 Truth labels used below

| Label | Meaning in this doc |
|---|---|
| **CONFIRMED** | Established in attached KFM doctrine (operating contract, Encyclopedia, Atlas, MapLibre Master v2.1, Directory Rules) or in atlas/idea cards marked CONFIRMED. |
| **PROPOSED** | Design / placement / field shape consistent with doctrine but not verified against a mounted repo, schema, validator, fixture, or workflow. |
| **NEEDS VERIFICATION** | Checkable claim awaiting mounted-repo inspection (repo files, schemas, tests, manifests, workflows, logs, ADRs). |
| **UNKNOWN** | Not resolvable from materials currently in session. |

> [!NOTE]
> No statement in this file claims that a repo file, schema, route, fixture, or test currently exists in the live monorepo. Every implementation-shaped claim is **PROPOSED** or **NEEDS VERIFICATION** unless explicitly footed in an attached doctrine document.

[⬆ Back to top](#-contents)

---

## 3. Trust-membrane invariants for Fauna map UI

These invariants are CONFIRMED doctrine across `[MAP-MASTER]`, `[UIAI]`, `[GAI]`, `[ENCY]`, the operating contract §22, and `[DOM-FAUNA]`. They bind every fauna rendering pathway.

> [!WARNING]
> **Fauna-specific deny-by-default zones.** Per `[DOM-FAUNA] §I`, exact sensitive occurrences and nests, dens, roosts, hibernacula, and spawning sites **fail closed** unless a documented geoprivacy transform and review state explicitly allow release. **Style-only hiding is not a valid protection mechanism** *(operating contract §22.1 invariant 4: "No sensitive geometry hidden only by style filters")*. Sensitive geometry must be transformed **before** it reaches the renderer.

### 3.1 Renderer is downstream of trust

- MapLibre (or any future renderer) **never** acts as truth, citation, policy, publication, or release authority. *(Operating contract §22: "MapLibre, maps, tiles, popups, screenshots, dashboards, and layers are downstream carriers.")*
- The renderer consumes validated `LayerManifest` / `StyleManifest` / `TileArtifactManifest` / `MapReleaseManifest` only.
- Public clients **must not** read `data/raw/fauna/`, `data/work/fauna/`, `data/quarantine/fauna/`, candidate manifests, internal canonical stores, graph stores, vector indexes, model runtimes, or credentials.
- All public reads route through `apps/governed-api/` (PROPOSED route home).

### 3.2 Click is a governed claim-resolution request

Per the operating contract §22.1 click-to-truth path, feature properties from a clicked fauna feature **are not claims**. The click produces a governed request that returns a `RuntimeResponseEnvelope` plus either an `EvidenceDrawerPayload` (`ANSWER`) or a typed negative state (`ABSTAIN`, `DENY`, `ERROR`).

### 3.3 Focus Mode is bounded synthesis

Focus Mode about fauna runs only over **released** Fauna `EvidenceBundle`s. The browser never calls a model runtime directly. Citations are validated **before** display or export. Sensitivity, rights, and release state govern `ANSWER` / `ABSTAIN` / `DENY` / `ERROR`.

### 3.4 Publication gates are cumulative

Per `[DOM-FAUNA] §H` (pipeline shape) and `§I` (sensitivity, rights, publication posture), before a fauna artifact is exposed in the Map UI:

```mermaid
flowchart LR
    A["Source registry &amp; rights"] --> B["Taxonomic resolution"]
    B --> C["Sensitivity &amp; geoprivacy policy"]
    C --> D["Evidence closure"]
    D --> E["Public-safe derivative check"]
    E --> F["ReleaseManifest + RollbackCard"]
    F --> G(("Map UI eligible"))
    C -. fail .-> X[("quarantine / deny")]
    D -. fail .-> X
    E -. fail .-> X
    F -. fail .-> X
```

If any gate fails, the artifact does not enter the Map UI layer registry. *Diagram reflects doctrine; gate names match Fauna §H (Pipeline shape) and §I (Sensitivity, rights, publication posture) of the Atlas.*

[⬆ Back to top](#-contents)

---

## 4. Fauna layer families and viewing modes

CONFIRMED doctrine (Encyclopedia §7.5; Atlas §7.G): Fauna admits the following viewing products. **Tier** below is from the **PROPOSED** public-tier scheme (T0 open ↔ T4 denied) defined in Atlas §24.5.1 and pending ratification under **ADR-S-05**. The tier *scheme* and the per-row tier *values* are PROPOSED; the underlying transform-and-gate rules (geoprivacy + RedactionReceipt for sensitive occurrences; deny-by-default for sensitive sites) are CONFIRMED.

| Layer family | Geometry | Public default tier | Transform required for public release | Status |
|---|---|---|---|---|
| Species page map (taxon-bound landing) | mixed | T0 | none (taxon identity only; no exact points) | PROPOSED tier |
| Generalized occurrence density grid | aggregated cells (e.g. H3 / county / HUC) | T1 | aggregation + freshness; no exact points | PROPOSED tier |
| Range polygon (`RangePolygon`) | polygon | T1 | aggregation or generalization receipt | CONFIRMED T1 (Atlas §24.5.2) |
| Seasonal range (`SeasonalRange`) | polygon | T1 | generalization + temporal binding | PROPOSED tier |
| Migration route (`MigrationRoute`) | line | T1 | route-geometry generalization rule | PROPOSED tier |
| Abundance / richness indicator | grid / polygon | T1 | aggregation receipt | PROPOSED tier |
| Habitat association (read-only join to Habitat) | polygon | T1 | habitat-fauna thin-slice rules; Habitat owns suitability | PROPOSED tier |
| Disease / mortality context | point or grid | T1–T2 | sensitivity + steward review for clustering | PROPOSED tier |
| Invasive species record (EDDMapS-class) | point or polygon | T1 | rights + freshness; no private locator data | PROPOSED tier |
| **Occurrence Public** | point or grid | T1 | `RedactionReceipt` + geoprivacy transform | CONFIRMED T4→T1 path (Atlas §24.5.2) |
| **Occurrence Restricted** | point | **T4 — deny on public UI** | none — never rendered on public Map UI | CONFIRMED deny default |
| Sensitive sites — nests / dens / roosts / hibernacula / spawning | point or polygon | **T4 — deny on public UI** | none — never rendered on public Map UI by default | CONFIRMED deny default |
| Steward exact-location view | exact geometry | **internal** | restricted access surface; **not** in public Map UI | CONFIRMED separation |

> [!CAUTION]
> A `RangePolygon` or `SeasonalRange` derived from sensitive occurrences is **still a derived sensitivity surface** if the inference path makes the source points reconstructable. Public release of such derivatives requires a `RedactionReceipt` documenting the transform and residual-risk reason.

Cross-cutting viewing products inherited from `[MAP-MASTER]`: Evidence Drawer (§6), time-aware state and time slider (§10), trust badges (§9), sensitivity-redacted view (CONFIRMED for fauna/flora/archaeology/infrastructure/people), stale-data view, correction view, and governed Focus Mode.

[⬆ Back to top](#-contents)

---

## 5. LayerDescriptor / LayerManifest profile for Fauna

The Fauna domain profile binds the cross-cutting `LayerManifest` to fauna-specific obligations. Cross-cutting field names are PROPOSED per `[MAP-MASTER]` §11 (Implementation-Ready Object Map). Fauna-specific obligations are CONFIRMED doctrine.

> [!NOTE]
> Schema home is **PROPOSED** at `schemas/contracts/v1/map/layer_manifest.schema.json` per `[MAP-MASTER]` §11 (note: `map/`, not `layers/`). Verify against the mounted schema directory before depending on these paths. ADR-0001 governs the canonical schema home.

### 5.1 Required fields (`MUST`) on a Fauna layer manifest

| Field | Source of obligation | Notes |
|---|---|---|
| `layer_id`, `title`, `geometry_type`, `source_id`, `source_layer` | `[MAP-MASTER]` §11 LayerManifest baseline | unique within release. |
| `release_state` | trust-membrane invariant | must be `published`; unpublished candidates MUST NOT load. |
| `release_id` | `MapReleaseManifest` linkage | binds layer to a verifiable release. |
| `policy_label` | `[UIAI]` + Fauna §I | one of `public`, `restricted`, `redacted`; `restricted` MUST NOT appear in public catalogs. |
| `sensitivity_label` | Fauna §I | one of `public`, `restricted`, `redacted`; never absent on fauna layers. |
| `source_role` | Fauna §D + source-role anti-collapse (ADR-S-04) | `authority` / `observation` / `aggregator` / `model` / `context` — never collapsed. |
| `evidence_ref_field` | `[MAP-MASTER]` §11 LayerManifest baseline | property name carrying `EvidenceRef` for each feature. |
| `temporal_fields` | Fauna §D + Encyclopedia | observed / event / source / retrieval / release / correction times kept distinct where material. |
| `rights_status` | Fauna §I | `unknown` blocks publication. |
| `transform_receipt_ref` | `KFM-IDX-POL-005` + Atlas §24.5 | required for any layer derived from sensitive sources; references the `RedactionReceipt`. |
| `freshness_class` | `[MAP-MASTER]` trust-visible states | drives stale-badge logic. |
| `tile_artifact_ref` / digest fields | `TileArtifactManifest` | enables verify-before-render. |
| `rollback_target` | publication gate doctrine | required before publish. |

### 5.2 Forbidden fields (`MUST NOT`) on a public Fauna layer manifest

| Field / pattern | Why forbidden |
|---|---|
| Raw `precise_point` / exact lat-lon for sensitive taxa | Geoprivacy fail-closed; `[DOM-FAUNA] §I`. |
| Observer identity for sensitive observations | Privacy; may aid re-identification or harassment. |
| Cluster-revealing metadata for sensitive sites | Inference attack against generalized geometry. |
| Direct links to RAW / WORK / QUARANTINE storage | Trust-membrane invariant. |
| Model-runtime endpoints, credentials, signed URLs not bound to release | `[UIAI]` security notes; operating contract §22. |
| Style filters used as the **only** sensitivity guard | Operating contract §22.1 invariant 4. |

### 5.3 Compact JSON Schema sketch *(illustrative, not source of truth)*

> [!NOTE]
> This block is **illustrative only**. The authoritative shape lives in `schemas/contracts/v1/map/layer_manifest.schema.json`. Do not copy these field names into validators without checking the schema.

```json
{
  "$id": "https://kfm.local/schemas/contracts/v1/map/layer_manifest.fauna-profile.example.json",
  "title": "Fauna LayerManifest (illustrative profile)",
  "type": "object",
  "required": [
    "layer_id", "title", "geometry_type", "source_id", "source_layer",
    "release_state", "release_id",
    "policy_label", "sensitivity_label", "source_role",
    "evidence_ref_field", "temporal_fields",
    "rights_status", "freshness_class",
    "rollback_target"
  ],
  "properties": {
    "release_state": { "const": "published" },
    "policy_label": { "enum": ["public", "restricted", "redacted"] },
    "sensitivity_label": { "enum": ["public", "restricted", "redacted"] },
    "source_role": { "enum": ["authority", "observation", "aggregator", "model", "context"] },
    "rights_status": { "enum": ["clear", "needs_review", "unknown", "denied"] },
    "transform_receipt_ref": { "type": "string", "description": "Required when derived from sensitive sources" }
  },
  "allOf": [
    {
      "if": { "properties": { "sensitivity_label": { "enum": ["restricted", "redacted"] } } },
      "then": { "required": ["transform_receipt_ref"] }
    },
    {
      "if": { "properties": { "rights_status": { "const": "unknown" } } },
      "then": { "properties": { "release_state": { "not": { "const": "published" } } } }
    }
  ]
}
```

[⬆ Back to top](#-contents)

---

## 6. Click resolution and `EvidenceDrawerPayload` profile

CONFIRMED (operating contract §22.1; `[MAP-MASTER]` §N): a clicked fauna feature **resolves through a governed claim-resolution request**, never as a direct projection of MapLibre feature properties.

> [!IMPORTANT]
> **Envelope naming.** AI and runtime surfaces use the canonical **`RuntimeResponseEnvelope`** (operating contract §21.1). For the Map-UI click and Focus-Mode seams specifically, the carrier objects are **`EvidenceDrawerPayload`** (click) and **`FocusModeResponse` + `AIReceipt`** (Focus Mode), per `[MAP-MASTER]` §11. The bespoke `DecisionEnvelope` named in some earlier drafts is **retired** in favor of these. All four families share the finite outcome set `ANSWER / ABSTAIN / DENY / ERROR`.

### 6.1 Click resolution flow

```mermaid
sequenceDiagram
    autonumber
    participant U as User
    participant ML as MapLibreAdapter
    participant CL as Governed Client
    participant API as "apps/governed-api (claims, evidence, layers)"
    participant POL as "policy/domains/fauna + policy/sensitivity/fauna"
    participant EVD as EvidenceBundle store
    U->>ML: click fauna feature
    ML->>CL: "claim-resolution request (layer_id, feature_id, viewport, time, policy_ctx)"
    CL->>API: "POST /api/v1/claims/resolve"
    API->>POL: "pre-check (sensitivity, rights, release_state)"
    POL-->>API: "ALLOW / DENY / ABSTAIN"
    API->>EVD: "resolve EvidenceRef → EvidenceBundle"
    EVD-->>API: "bundle (or missing)"
    API-->>CL: "RuntimeResponseEnvelope + EvidenceDrawerPayload, or typed negative state"
    CL-->>ML: render outcome
    ML-->>U: "drawer / abstain / deny / error"
```

*Diagram reflects operating contract §22.1 and `[MAP-MASTER]` §N doctrine. The route name `/api/v1/claims/resolve` is PROPOSED and requires mounted-repo verification.*

### 6.2 Required `EvidenceDrawerPayload` fields for a Fauna feature

CONFIRMED required cross-cutting fields per `[MAP-MASTER]` §11. The **Fauna obligations** column adds domain-specific obligations.

| Cross-cutting field | Fauna obligation | Status |
|---|---|---|
| `feature_id`, `layer_id` | none beyond baseline | CONFIRMED doctrine |
| `claim` / layer assertion | MUST be taxon-bound; e.g. "Occurrence of *Taxon X*, generalized to a z=9 H3 cell" | CONFIRMED doctrine |
| finite outcome (`ANSWER` / `ABSTAIN` / `DENY` / `ERROR`) | DENY required for sensitive sites; ABSTAIN required for missing geoprivacy receipt | CONFIRMED doctrine |
| `evidence_bundle_refs` (`EvidenceRef[]`) | Must resolve to a **released** Fauna `EvidenceBundle` | CONFIRMED doctrine |
| `source_role` | Distinguish `authority` (e.g. USFWS ECOS-like), `observation` (e.g. agency monitoring), `aggregator` (e.g. GBIF/eBird/iNaturalist-like), `model` (suitability, predicted range), `context` (NLCD/NWI/PADUS/SSURGO-class) | CONFIRMED — never collapsed |
| `knowledge_character` | One of observation / regulatory / aggregator / model / status / context | CONFIRMED doctrine |
| `valid_time`, `observed_time`, `freshness` | Per Fauna §D — kept distinct where material | CONFIRMED doctrine |
| `release_state`, `review_state`, `correction_state` | release/correction lineage visible | CONFIRMED doctrine |
| `rights`, `sensitivity`, `transforms` | **Fauna MUST list the geoprivacy transform applied** (suppress, generalize-to-grid, generalize-to-watershed, generalize-to-county, buffer, jitter-with-constraints, delayed publication, steward-only access) — per `KFM-IDX-POL-005` | CONFIRMED doctrine |
| `provenance` | Source descriptor + ingest path + receipts | CONFIRMED doctrine |
| `related_manifest_refs` (e.g. `LayerManifest`, `MapReleaseManifest`) | Visible to steward / public as appropriate | CONFIRMED doctrine |
| **Limitations / caveats** block | MUST state generalization scale, uncertainty radius, and "this is a public-safe derivative — exact location not disclosed" where relevant | CONFIRMED Fauna obligation |

### 6.3 Required negative outcomes for Fauna clicks

Negative drawer states are first-class outcomes and **must be testable**. The reason codes below are reconciled to the **operating contract §22.2 canonical UI negative-state vocabulary** (`MISSING_EVIDENCE`, `SOURCE_STALE`, `DENIED_BY_POLICY`, `GENERALIZED_GEOMETRY`, `RESTRICTED_ACCESS`, `CONFLICTED_SUPPORT`, `CITATION_FAILED`, `RELEASE_WITHDRAWN`, `RUNTIME_ERROR`).

| Negative state (contract §22.2) | When it fires (Fauna) | Required UI behavior |
|---|---|---|
| `MISSING_EVIDENCE` | Click resolves to a feature with no released `EvidenceBundle` | Show "evidence not available" + correction path. |
| `RESTRICTED_ACCESS` / `GENERALIZED_GEOMETRY` | Sensitive taxon / site / occurrence; geoprivacy denies public exposure | Show generalized representation + "exact location not disclosed" notice. No exact geometry leaks via popup, hover, or selection effect. |
| `SOURCE_STALE` | Source freshness past defined threshold | Stale badge + abstain on consequential claims. |
| `CONFLICTED_SUPPORT` | Multiple sources disagree (e.g. authority vs aggregator) | Surface both with `source_role`; do not silently pick. |
| `RUNTIME_ERROR` | Payload fails schema validation | Show ERROR state; never render unparseable content. |
| `DENIED_BY_POLICY` | Rights `unknown`, sensitivity fail-closed, release missing | DENY with reason code; no fallback rendering. |
| `RELEASE_WITHDRAWN` | A prior release was withdrawn / superseded by correction | Withdrawn/superseded notice + link to current release. |

[⬆ Back to top](#-contents)

---

## 7. Focus Mode behavior for Fauna

CONFIRMED doctrine (`[GAI]`; Atlas §7.L; operating contract §21): AI is **interpretive, not the root truth source**. `EvidenceBundle` outranks generated language. Focus Mode answers about fauna must observe these obligations.

### 7.1 Allowed Focus Mode operations on Fauna

| Operation | Bounded by | Outcome |
|---|---|---|
| Summarize a **released** Fauna `EvidenceBundle` for a clicked or selected feature | citation validation on every claim | `ANSWER` with citations + `AIReceipt` |
| Compare two released Fauna evidence items (e.g. authority vs aggregator on the same taxon) | source-role separation visible in answer | `ANSWER` or `ABSTAIN` |
| Explain limitations of a public-safe derivative (e.g. generalization scale, uncertainty radius) | must reference the `RedactionReceipt` / transform | `ANSWER` |
| Draft a **steward-review note** for a candidate fauna claim | not a public route; restricted surface | `ANSWER` (review-only) |

### 7.2 Required Focus Mode behaviors

- **Pre-check** sensitivity, rights, and release state **before** evidence retrieval (operating contract §21.1 required flow).
- **Post-check** every cited `EvidenceRef` resolves and is admissible in current scope (`CitationValidationReport` PASS) — else `ABSTAIN`.
- Browser MUST NOT call Ollama / OpenAI / vector index / graph store / object store directly. Adapter lives in `apps/governed-api/src/ai/` (PROPOSED); provider neutrality per operating contract §21.5.
- The `MapContextEnvelope` sent to Focus Mode carries exactly `visible_layers`, `bounds`, `zoom`, `pitch`, `bearing`, `filters`, `time_window`, `selected_features`, `evidence_refs` — **no raw feature properties** and **no restricted geometry** *(field list CONFIRMED per `[MAP-MASTER]` §11)*.

### 7.3 Required Focus Mode denials and abstentions for Fauna

| Trigger | Outcome | Reason code (PROPOSED) |
|---|---|---|
| Question is about the **exact location** of a sensitive taxon or nest/den/roost/hibernacula/spawning site | `DENY` | `fauna.geoprivacy.exact_location_denied` |
| Question depends on an **unreleased** `EvidenceBundle` | `ABSTAIN` | `evidence.unreleased` |
| Question depends on a source with `rights_status = unknown` | `DENY` | `rights.unknown` |
| AI would otherwise generate a fauna claim with **no cite-able evidence** | `ABSTAIN` | `citation.missing` |
| AI is asked to act as an **emergency / wildlife-incident authority** | `DENY` | `boundary.alert_authority_denied` *(mirrors hazards-alert-boundary doctrine; Atlas §24.5.2 "KFM as alert authority — T4 forever")* |
| Question requests **observer identity** for a sensitive observation | `DENY` | `privacy.observer_identity_denied` |

> [!IMPORTANT]
> A Focus Mode answer about fauna that quotes or summarizes any unreleased candidate, raw point, or sensitive geometry is a **policy violation**, not a quality bug. The post-check **must** block emit, and the failure must be visible in the `AIReceipt`.

[⬆ Back to top](#-contents)

---

## 8. Sensitivity gates and geoprivacy transforms

CONFIRMED across `[DOM-FAUNA] §I`, Atlas §20.5 Deny-by-Default Register, Atlas §24.5.2 tier matrix, and `KFM-IDX-POL-005`:

| Class | Default tier (PROPOSED) | Allowed public transform | Required gates |
|---|---|---|---|
| Sensitive occurrence (rare / protected / sensitive taxon, exact point) | T4 | Geoprivacy generalization (grid, watershed, county) + `RedactionReceipt` → T1 | `RedactionReceipt` + `ReviewRecord` + `PolicyDecision` |
| Nest / den / roost / hibernaculum / spawning site | T4 | Suppression OR steward-only access; **no exact public release** by default | Steward review + `PolicyDecision` |
| Range polygon | T1 | Aggregate / generalized public-safe layer | `AggregationReceipt` or `RedactionReceipt` |
| Observer identity for sensitive obs | T4 | None for public | Deny at runtime |
| Disease / mortality clusters | T1–T2 | Generalization + steward review if reveals sensitive sites | `RedactionReceipt` + `ReviewRecord` |

*(The T4 → T1 motion for sensitive occurrence and the T1 range-polygon row are CONFIRMED in Atlas §24.5.2; the overall tier scheme remains PROPOSED pending ADR-S-05.)*

### 8.1 Transform taxonomy (per `KFM-IDX-POL-005`)

CONFIRMED as doctrine concept, PROPOSED implementation:

- **suppress** — feature withheld from public layer entirely.
- **generalize_to_grid** — coordinates aggregated to a fixed cell (H3 / square grid).
- **generalize_to_watershed** — projected to HUC polygon (joins with `[DOM-HYD]`).
- **generalize_to_county** — projected to county polygon.
- **buffer** — point replaced with a buffered region; buffer radius is policy-driven, never user-driven.
- **jitter_with_constraints** — point displaced under documented constraints; rarely admissible alone.
- **delayed_publication** — exact data released only after a specified embargo.
- **steward_only_exact** — exact geometry available only on the restricted steward console.

Every transform emits a `RedactionReceipt` stating `input_class`, `output_class`, `reason`, `policy_ref`, `reviewer`, `residual_risk`. The receipt is referenced from the layer manifest's `transform_receipt_ref` and from the `EvidenceDrawerPayload.transforms` list.

### 8.2 What sensitivity gates are NOT

> [!CAUTION]
> Style-only hiding (`!visible`, layout opacity, layer filter expressions) is **not** an accepted protection mechanism for sensitive fauna geometry *(operating contract §22.1 invariant 4)*. Sensitive geometry must be **transformed before it reaches the renderer**. A failing style does not unhide raw data, because raw data must not have been in the tile in the first place.

<details>
<summary><strong>Inference-attack notes (residual-risk register)</strong></summary>

- **Grid + observer date**: a generalized cell plus a precise timestamp can re-localize the observer or the site if the observer's habits are knowable. Either coarsen time or remove observer-bound metadata.
- **Sequence of generalized points** for one taxon over a season: can reconstruct migration route geometry below the generalization scale. Aggregate temporally before publishing.
- **Cross-domain join**: generalized fauna + fine-grained hydrology + fine-grained land cover may collapse to a narrow inference region. The habitat-fauna thin slice's `RedactionReceipt` should record the join risk and the policy that allowed (or denied) the join. Cross-lane join policy is ADR-class — see ADR-S-14.
- **Search index leakage**: derived search/vector indexes built over unreleased or restricted evidence may leak. Indexes are derivative; rebuild from released `EvidenceBundle`s only.

</details>

[⬆ Back to top](#-contents)

---

## 9. Trust-visible states, badges, and negative outcomes

CONFIRMED across `[MAP-MASTER]` §S and `[UIAI]`: badges are **annotations**, not proof. They surface trust state; they never substitute for an `EvidenceBundle`. Badges are generated from structured outcomes (`KFM-IDX-VAL-002`), not maintained by hand.

### 9.1 Required trust-visible states for Fauna layers

The UI-facing state names below map to the operating contract §22.2 vocabulary; the badge label is the human-facing surface.

| Badge / state | Contract §22.2 mapping | Trigger | UI cue |
|---|---|---|---|
| `released` | — (positive default) | `release_state` is `published` and `freshness_class` is fresh. | Default presentation. |
| `stale` | `SOURCE_STALE` | Source freshness past threshold. | Stale badge; `ABSTAIN` on consequential claims. |
| `degraded` | `RUNTIME_ERROR` (integrity) | Tile/style integrity check failed or fell back. | Degraded badge; no Focus Mode answers from this layer. |
| `denied` | `DENIED_BY_POLICY` | Policy deny (sensitivity, rights, missing manifest). | Deny notice with reason code; no rendering. |
| `redacted` | `GENERALIZED_GEOMETRY` / `RESTRICTED_ACCESS` | Public-safe derivative shown; exact geometry not disclosed. | Redacted badge + transform reference visible in drawer. |
| `unverified` | (verification failed/pending; `ML-061-140`) | Verification failed or pending. | Unverified badge; distinct visual treatment from stale. |
| `correction_pending` | (open `CorrectionNotice`) | A `CorrectionNotice` is open against the layer. | Correction badge linked to the notice. |
| `superseded` | `RELEASE_WITHDRAWN` | Newer release exists. | Superseded badge with link to current release. |

### 9.2 Badge accessibility

Per `[MAP-MASTER]` §S (`ML-061-138`, `ML-061-139`, `ML-061-140`, `ML-061-141`):

- Every badge must be keyboard-reachable.
- Every badge requires an accessible name + state announcement (screen reader).
- Badge color is **never** the sole channel — distinct icon / pattern / label.
- Badge click opens proof details (`ML-061-139`) — it does **not** replace the Evidence Drawer; it points into it.
- Exports and screenshots preserve verification badge state and manifest ID (`ML-061-141`).

[⬆ Back to top](#-contents)

---

## 10. Time-aware behavior

CONFIRMED doctrine (Encyclopedia; `[MAP-MASTER]` time category): temporal fields stay distinct where material. For fauna features, these are:

- `observed_time` — when the observation happened.
- `event_time` — when the underlying biological event occurred (often equal to `observed_time`, but separable for derived events such as nesting).
- `source_time` / `retrieval_time` — when the source produced / KFM retrieved the record.
- `release_time` — when the artifact entered the public Map UI.
- `correction_time` — when a correction was issued.

### 10.1 Time slider obligations

- The slider filters by **valid** / observed / source / release time per the layer's `temporal_fields` declaration.
- A change in time window MUST re-run sensitivity and freshness gates — a window into the past does not exempt sensitive sites from deny-by-default.
- Stale state derives from normalized timing fields. The UI must distinguish "no data in this time window" from "data is stale relative to the source's expected cadence" (`SOURCE_STALE`).

### 10.2 Versioning and supersession

A new release of a fauna layer must carry `supersedes` linkage in `MapReleaseManifest` and a `rollback_target`. The Evidence Drawer renders correction lineage so users can trace what changed.

[⬆ Back to top](#-contents)

---

## 11. Anti-patterns (fail closed)

> [!CAUTION]
> The list below is enforcement-bearing. Each anti-pattern is paired with a fixture that must fail closed. Several map directly to the operating contract §22.1 invariants.

| Anti-pattern | Why dangerous (Fauna) | Required test posture |
|---|---|---|
| Style-only hiding of sensitive geometry | Style failure exposes sensitive data; the data is in the tile. | Negative tile fixture: sensitive coordinate not present in tile at all. |
| Treating MapLibre output as a fauna claim | Renderer is not truth. | Click → drawer test on a fauna feature; popups never substitute. |
| Using popup or tooltip text as authoritative | Tooltips don't carry citation discipline (operating contract §22.1 invariant 5). | Tooltip text MUST link to drawer, not act as drawer. |
| Direct `addSource` from a candidate / unreleased PMTiles for fauna | Trust-membrane breach (invariant 3: layer toggle is not publication). | No-unreleased-tile-load test on the fauna layer registry. |
| Public route reading `data/processed/fauna/` or `data/catalog/domain/fauna/` directly | Bypasses governed API. | Trust-membrane test on the explorer-web shell. |
| Watcher writes to `data/published/layers/fauna/` | Watcher-as-non-publisher invariant violation. | Promotion test: only the governed promotion path may publish. |
| Aggregator data shown as **authority** | Source-role anti-collapse violation (ADR-S-04). | Drawer test: `source_role = aggregator` MUST display distinctly. |
| Focus Mode generates fauna location text from rendered features alone | Cite-or-abstain violation (invariant 6). | Focus Mode test: missing `EvidenceBundle` ⇒ `ABSTAIN`. |
| Re-identifying observer / cluster from generalized data | Inference leak; geoprivacy fail. | Inference-attack test on generalization scale and time coarseness. |
| Treating a `RangePolygon` as **observed presence** | Range is a derivative product, not an observation. | Drawer test: `knowledge_character` distinguishes range from occurrence. |
| Badge as Evidence-Drawer substitute | Trust theater. | Badge-click test: opens drawer, does not replace it (`ML-061-139`). |

[⬆ Back to top](#-contents)

---

## 12. Validation, tests, and fixtures

PROPOSED test catalog. Path placement follows Directory Rules §12 (Domain Placement Law) and §13 (lifecycle separation / anti-patterns).

| Test family | PROPOSED home | What it proves |
|---|---|---|
| Schema validity for Fauna layer-manifest profile | `tests/domains/fauna/layers/` + `fixtures/domains/fauna/layers/` | `MUST` fields present; `MUST NOT` fields absent. |
| `EvidenceDrawerPayload` resolution on Fauna click | `tests/domains/fauna/ui/drawer/` | Click on `Occurrence Public` returns `ANSWER`; click on internal `Occurrence Restricted` returns `DENY` or never renders. |
| Geoprivacy transform receipt presence | `tests/domains/fauna/policy/redaction/` | Every public-safe derivative carries a resolvable `RedactionReceipt`. |
| Tile field allowlist for Fauna PMTiles | `tests/domains/fauna/tiles/` | Tile properties contain no forbidden fields (exact lat-lon for sensitive taxa, observer identity, etc.). |
| Sensitive-geometry deny fixture | `fixtures/domains/fauna/sensitive_deny/` | Public request denied; style-only hiding rejected. |
| Stale-source fauna fixture | `fixtures/domains/fauna/stale_source/` | `SOURCE_STALE` badge + `ABSTAIN` behavior triggered. |
| Focus Mode citation gate on Fauna | `tests/domains/fauna/focus/citation/` | Missing or unreleased `EvidenceBundle` ⇒ `ABSTAIN`. |
| Focus Mode deny on sensitive-location question | `tests/domains/fauna/focus/deny_sensitive/` | Question targeting exact sensitive geometry ⇒ `DENY` with reason code. |
| Source-role anti-collapse | `tests/domains/fauna/sources/` | Authority / observation / aggregator / model never collapsed into one label. |
| Rollback restore for fauna release | `tests/domains/fauna/release/rollback/` | Prior `MapReleaseManifest` and tile digests restored; cache invalidation recorded. |
| Accessibility (badges, drawer, time slider) | `tests/domains/fauna/a11y/` | Keyboard, contrast, screen-reader, alt-text. |
| Visual regression (public Fauna layers) | `tests/domains/fauna/visual/` | No silent visual change post-release. |
| Cross-domain join risk (`fauna × habitat × hydrology`) | `tests/cross_domain/fauna_habitat/` (no domain segment — shared validator) | Inference-leak fixtures fail closed where they should. |

> [!NOTE]
> Per Directory Rules §12, the cross-domain test above lives under a **non-domain segment** of `tests/` (lowest common responsibility root, no domain folder). Single-domain tests live under `tests/domains/fauna/...`.

[⬆ Back to top](#-contents)

---

## 13. Open questions register

| ID | Question | Owner role | Resolution path |
|---|---|---|---|
| OQ-FAUNA-UI-01 | Confirm canonical schema home for `LayerManifest`, `EvidenceDrawerPayload`, `MapContextEnvelope`, `FocusModeResponse`, `AIReceipt` (PROPOSED `map/`, `ui/`, `ai/` per `[MAP-MASTER]` §11). | Schema steward | ADR-0001 + mounted schema files. |
| OQ-FAUNA-UI-02 | Confirm `apps/governed-api/` route names for `/claims/resolve`, `/evidence/{id}`, `/layers/...`, `/focus`, `/exports`, `/telemetry/ui`. | Governed-API steward | Mounted route source or OpenAPI artifact. |
| OQ-FAUNA-UI-03 | Confirm Fauna source registry contents, source-role labels, and current rights status per source. | Fauna steward | `data/registry/sources/fauna/` + source-dossier validators. |
| OQ-FAUNA-UI-04 | Confirm the exact list of fauna taxa flagged as sensitive (KDWP / USFWS / NatureServe crosswalks). | Fauna steward | Steward sensitivity register + crosswalk fixture. |
| OQ-FAUNA-UI-05 | Confirm the geoprivacy policy bundle (transform allowlist + per-class defaults) for Fauna. | Policy steward | `policy/sensitivity/fauna/` and `policy/domains/fauna/` rules. |
| OQ-FAUNA-UI-06 | Confirm habitat-fauna thin-slice manifest binding (does the first published thin slice carry the expected `LayerManifest`, `EvidenceBundle`, drawer payload, Focus behavior, rollback target?). | Fauna + UI stewards | Thin-slice release manifest + drawer fixture + Focus fixture. |
| OQ-FAUNA-UI-07 | Ratify the T0–T4 tier scheme (ADR-S-05) and confirm per-row Fauna tier values. | Steward + release authority | ADR-S-05; Atlas §24.5 reconciliation. |
| OQ-FAUNA-UI-08 | Confirm storage of `RedactionReceipt` and its linkage from the layer manifest's `transform_receipt_ref`. | Schema steward | Schema + fixture + emitted receipts. |
| OQ-FAUNA-UI-09 | Resolve naming discrepancy `PROV.md` vs `PROVENANCE.md` flagged in adjacent docs. | Docs steward | ADR. |
| OQ-FAUNA-UI-10 | Confirm runbook subfolder convention (`docs/runbooks/fauna/…` vs flat-prefix `docs/runbooks/fauna_…`). | Docs steward | Repo convention + ADR. |
| OQ-FAUNA-UI-11 | Confirm whether MapLibre Native / MapLibre RS are admitted Fauna renderers for any client tier. | UI steward | Mounted client list + ADR. |

[⬆ Back to top](#-contents)

---

## 14. Open verification backlog

These items remain `NEEDS VERIFICATION` (or `UNKNOWN` / `DEFERRED` where noted) before promotion from `draft` to `published`:

1. Schema homes `map/`, `ui/`, `ai/` confirmed against a mounted `schemas/contracts/v1/` tree (ADR-0001).
2. Governed-API route names confirmed (OQ-FAUNA-UI-02).
3. Fauna source registry + source-role + rights status confirmed (OQ-FAUNA-UI-03).
4. Sensitive-taxa list confirmed against the steward register (OQ-FAUNA-UI-04).
5. Geoprivacy policy bundle confirmed (OQ-FAUNA-UI-05).
6. Habitat-fauna thin-slice manifest binding confirmed (OQ-FAUNA-UI-06).
7. Taxonomic resolver implementation (which crosswalks, which authority order) — **UNKNOWN**.
8. `RedactionReceipt` storage + `transform_receipt_ref` linkage confirmed (OQ-FAUNA-UI-08).
9. 3D / scene-render policy for fauna — **DEFERRED** (governed by maplibre-3d admission policy; Scene Manifest + Reality Boundary Note + 3D admission gate).
10. T0–T4 tier scheme ratified via ADR-S-05 (OQ-FAUNA-UI-07).

[⬆ Back to top](#-contents)

---

## 15. Changelog

| Change | Type (per contract §37) | Reason |
|---|---|---|
| Pinned `CONTRACT_VERSION = "3.0.0"` in meta block, badge row, and authority order. | housekeeping | Doctrine-adjacent doc requirement. |
| Corrected schema homes: `layers/` → `map/`; added `ui/` and `ai/`; removed `runtime/decision_envelope.schema.json`. | reconciliation | `[MAP-MASTER]` v2.1 §11 PROPOSED homes are `map/`, `ui/`, `ai/`. |
| Retired bespoke `DecisionEnvelope` in favor of `RuntimeResponseEnvelope` (runtime) with `EvidenceDrawerPayload` (click) and `FocusModeResponse` + `AIReceipt` (Focus Mode). | reconciliation | Operating contract §21.1 + `[MAP-MASTER]` §11. Added §6 envelope-naming callout. |
| Reconciled §6.3 and §9.1 negative-state names to the operating contract §22.2 canonical vocabulary (`MISSING_EVIDENCE`, `SOURCE_STALE`, `DENIED_BY_POLICY`, `GENERALIZED_GEOMETRY`, `RESTRICTED_ACCESS`, `CONFLICTED_SUPPORT`, `CITATION_FAILED`, `RELEASE_WITHDRAWN`, `RUNTIME_ERROR`). | reconciliation | Prior ad-hoc lowercase names (`evidence_missing`, `restricted`, `stale`, `conflict`, `invalid_payload`, `policy_denied`) diverged from contract §22.2. |
| Marked the T0–T4 tier scheme PROPOSED pending ADR-S-05; flagged which Fauna tier rows are CONFIRMED (Atlas §24.5.2) vs PROPOSED. | clarification | Atlas §24.5.1 presents the tier scheme as PROPOSED. |
| Replaced stale idea-card citations (`ML-Q-082`, `ML-Q-076`, `ML-Q-080`, `ML-Q-083`, `ML-064-017`, `ML-061-094`, `KFM-IDX-POL-005` framing) with operating-contract §22.1/§22.2 and confirmed `ML-061-138..141` / Atlas §24.5 anchors where available. | clarification | Grounds claims in confirmed doctrine anchors. |
| Restructured tail into formal doctrine companion sections (Open Questions register with `OQ-FAUNA-UI-NN` IDs, Verification backlog, Changelog, Definition of done). | housekeeping | Aligns with the operating-contract doctrine-doc companion-section pattern. |
| Mermaid node/edge labels containing `(`, `)`, `/`, `→`, `&` double-quoted. | housekeeping | Mermaid parse safety. |
| Bumped version v1 → v1.1; `updated` 2026-05-16 → 2026-06-02. | housekeeping | MINOR bump; no operating-law change. |

> **Backward compatibility.** Section anchors §1–§12 are preserved. The tail anchor `#13-open-questions-and-verification-backlog` is split into `#13-open-questions-register` and `#14-open-verification-backlog`; the former §14 "Related docs" moves to §17. Reason codes in §6.3 changed from lowercase ad-hoc names to the contract §22.2 vocabulary — update any inbound references or fixtures keyed to the old names.

[⬆ Back to top](#-contents)

---

## 16. Definition of done

This document is done enough to enter the repository when:

- it is placed according to Directory Rules (proposed home `docs/domains/fauna/MAP_UI_CONTRACTS.md`, NEEDS VERIFICATION);
- a docs steward and the Fauna + UI + governed-API stewards review it;
- it is linked from the Fauna lane README and the UI/architecture index;
- it does not conflict with accepted ADRs (notably ADR-0001 schema home, ADR-S-04 source-role, ADR-S-05 tier scheme, ADR-S-06 AI surface boundary);
- the schema-home, envelope-naming, and negative-state-vocabulary reconciliations (Changelog) are logged in `docs/registers/DRIFT_REGISTER.md`;
- the `GENERATED_RECEIPT.json` planned in Section 2 is wired into CI;
- future changes follow the operating contract's §37 lifecycle.

[⬆ Back to top](#-contents)

---

## 17. Related docs

> Placeholders below are intentional and will resolve once neighboring docs land. *PROPOSED until verified per Directory Rules §2.5.*

- `docs/domains/fauna/README.md` — Fauna domain landing. *(PROPOSED)*
- `docs/domains/fauna/IDENTITY_MODEL.md` — Fauna identity model (companion in this series). *(PROPOSED)*
- `docs/domains/fauna/SENSITIVITY.md` — Fauna sensitivity classes and deny-by-default register. *(PROPOSED)*
- `docs/runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md` — operational refresh runbook. *(CONFIRMED — drafted in this project series)*
- `ai-build-operating-contract.md` — canonical operating contract, `CONTRACT_VERSION = "3.0.0"`. *(CONFIRMED)*
- `directory-rules.md` — repository placement doctrine. *(CONFIRMED)*
- `docs/architecture/ui/LAYERING.md` — cross-cutting layer manifest doctrine. *(PROPOSED)*
- `docs/architecture/ui/BOUNDARIES.md` — MapLibre adapter boundary. *(PROPOSED)*
- `docs/architecture/governed-ai/FOCUS_FLOW.md` — Focus Mode adapter & citation discipline. *(PROPOSED)*
- `docs/architecture/governed-ai/BOUNDARIES.md` — Governed-AI trust membrane. *(PROPOSED)*
- `docs/architecture/maplibre-3d.md` — 3D admission policy (deferred fauna scenes). *(CONFIRMED — this project)*
- `docs/standards/PROV.md` — provenance profile (resolve `PROVENANCE.md` naming via ADR). *(CONFIRMED — drafted in this project series)*
- `docs/standards/PMTILES.md` — PMTiles v3 conformance profile. *(PROPOSED)*
- `docs/standards/OGC-API-TILES.md` — tile delivery profile. *(PROPOSED)*
- `policy/domains/fauna/README.md` — fauna policy bundle. *(PROPOSED)*
- `policy/sensitivity/fauna/README.md` — sensitivity & geoprivacy rules. *(PROPOSED)*
- `contracts/OBJECT_MAP.md` — DTO crosswalk. *(PROPOSED)*
- ADRs *(PROPOSED — verify in `docs/adr/`)*: ADR-0001 Schema home (CONFIRMED cited by Directory Rules §2.4(3)); ADR-S-04 Source-role vocabulary; ADR-S-05 Sensitivity tier scheme; ADR-S-06 AI surface boundary; ADR-S-14 Cross-lane join policy; ADR-fauna-geoprivacy-transforms *(TODO)*.

---

<sub>Last updated: 2026-06-02 · Version: v1.1 · Status: draft · CONTRACT_VERSION: `3.0.0` · Owners: Fauna steward + UI steward + Governed-API steward *(PLACEHOLDER)*</sub>

<sub>[⬆ Back to top](#-contents)</sub>

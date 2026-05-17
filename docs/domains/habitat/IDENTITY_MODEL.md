<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/habitat-identity-model
title: Habitat — Identity Model
type: standard
version: v1
status: draft
owners: <habitat-domain-stewards>  <!-- placeholder; confirm via control_plane/object_family_register.yaml -->
created: 2026-05-17
updated: 2026-05-17
policy_label: public
related:
  - docs/domains/habitat/README.md
  - docs/domains/habitat/SOURCES.md
  - docs/domains/habitat/PIPELINE.md
  - docs/domains/habitat/SENSITIVITY.md
  - docs/domains/fauna/IDENTITY_MODEL.md
  - docs/standards/PROV.md
  - docs/architecture/contract-schema-policy-split.md
  - docs/adr/ADR-0001-schema-home.md
  - schemas/contracts/v1/domains/habitat/
tags: [kfm, habitat, identity, evidence, ddd, spec_hash]
notes:
  - All habitat-object identity rules are PROPOSED until verified against a mounted repo.
  - Schema home (schemas/contracts/v1/domains/habitat/) is the PROPOSED default per ADR-0001.
[/KFM_META_BLOCK_V2] -->

# 🧬 Habitat — Identity Model

How the Habitat domain answers *“is this the same thing?”* — deterministically, evidentially, and across releases.

![status: draft](https://img.shields.io/badge/status-draft-blue)
![doc type: standard](https://img.shields.io/badge/doc--type-standard-informational)
![domain: habitat](https://img.shields.io/badge/domain-habitat-2ea44f)
![lifecycle: RAW%20→%20PUBLISHED](https://img.shields.io/badge/lifecycle-RAW%20→%20PUBLISHED-orange)
![identity: spec_hash%20%2B%20JCS%2BSHA--256](https://img.shields.io/badge/identity-spec__hash%20%2B%20JCS%2BSHA--256-purple)
![sensitivity: fail--closed](https://img.shields.io/badge/sensitivity-fail--closed-critical)
![ci: TODO](https://img.shields.io/badge/ci-TODO-lightgrey)

> **Status:** draft · **Owners:** `<habitat-domain-stewards>` *(placeholder)* · **Last updated:** 2026-05-17

---

## 📑 Contents

- [1. Purpose & scope](#1-purpose--scope)
- [2. Doctrinal anchors](#2-doctrinal-anchors)
- [3. Identity philosophy: entity vs value object](#3-identity-philosophy-entity-vs-value-object)
- [4. The Habitat identity formula](#4-the-habitat-identity-formula)
- [5. `spec_hash`, `bundle_id`, `evidence_ref_id`](#5-spec_hash-bundle_id-evidence_ref_id)
- [6. Per-object identity table](#6-per-object-identity-table)
- [7. Temporal handling](#7-temporal-handling)
- [8. Sensitivity, geoprivacy, and identity exposure](#8-sensitivity-geoprivacy-and-identity-exposure)
- [9. Cross-lane identity coordination](#9-cross-lane-identity-coordination)
- [10. Validators, tests, and gate behavior](#10-validators-tests-and-gate-behavior)
- [11. Identity changes, renames, and migration](#11-identity-changes-renames-and-migration)
- [12. Open questions & verification backlog](#12-open-questions--verification-backlog)
- [13. Related docs](#13-related-docs)
- [Appendix A — Worked example: a `HabitatPatch` identity](#appendix-a--worked-example-a-habitatpatch-identity)
- [Appendix B — Truth labels used in this doc](#appendix-b--truth-labels-used-in-this-doc)

---

## 1. Purpose & scope

This document defines **what it means to be the same Habitat object** across releases, sources, and runs. It is the canonical identity contract for the Habitat domain — covering how identity is computed, how `EvidenceRef` resolves to `EvidenceBundle`, how temporal scope is kept distinct, and how identity interacts with sensitivity and publication gates.

**In scope.** Identity rules for every Habitat object family (CONFIRMED list: HabitatPatch, LandCoverObservation, EcologicalSystem, HabitatQualityScore, SuitabilityModel, ConnectivityEdge, Corridor, RestorationOpportunity, StewardshipZone, ModelRunReceipt, UncertaintySurface). The `spec_hash` construction. Bundle and reference ID derivation. Temporal scope. Identity-side behavior at promotion and rollback. Cross-lane identity coordination with Fauna, Flora, Soil/Hydrology, and Hazards.

**Out of scope.** Source-descriptor specifics (see [`SOURCES.md`](./SOURCES.md), PROPOSED). Pipeline mechanics (see [`PIPELINE.md`](./PIPELINE.md), PROPOSED). Sensitivity transform rules (see [`SENSITIVITY.md`](./SENSITIVITY.md), PROPOSED). MapLibre layer rendering. Schema *shape* — defined in `schemas/contracts/v1/domains/habitat/` *(PROPOSED path, ADR-0001)*.

> [!NOTE]
> This file is doctrine-first. Every implementation-level claim — schema paths, validator names, ID prefixes, gate code — is **PROPOSED** until verified against a mounted repo. See [§12](#12-open-questions--verification-backlog).

[⬆ Back to top](#-habitat--identity-model)

---

## 2. Doctrinal anchors

| Anchor | Source | Status |
|---|---|---|
| Domain ownership, scope, and non-ownership | `[DOM-HAB]` · `[DOM-HF]` · `[ENCY]` (Domains Culmination Atlas §6; Encyclopedia §7.4) | **CONFIRMED doctrine** |
| Object-family identity rule: *source id + object role + temporal scope + normalized digest* | `[DOM-HAB]` · `[ENCY]` (Habitat §E "Main object families") | **CONFIRMED doctrine** / **PROPOSED implementation** |
| Temporal-time separation: source / observed / valid / retrieval / release / correction | `[ENCY]` · `[DOM-HAB]` | **CONFIRMED doctrine** |
| `spec_hash` via RFC 8785 JCS + SHA-256 | New Ideas 5-8-26 (D1); Pass 10 C1-02; Pass 20 P2 EVD | **CONFIRMED doctrine** |
| Bundle/EvidenceRef derived IDs (`eb-…`, `er-…`) | New Ideas 5-8-26 (D2) | **CONFIRMED doctrine** / **PROPOSED implementation** |
| BLAKE3 considered for streaming artifact roots (tiles, large rasters) | New Ideas 5-10-26; Pass 20 P2 EVD | **CONFIRMED doctrine** / **PROPOSED implementation** |
| DDD entity-vs-value-object distinction | *Domain-Driven Design Reference* (Evans, pp. 11–12) | **CONFIRMED reference** |
| Habitat publication gates: ReleaseManifest, EvidenceBundle, validation/policy, review, correction, rollback | `[ENCY Appendix E]` · `[DOM-HAB]` · `[DOM-HF]` | **CONFIRMED doctrine** / **PROPOSED implementation** |
| Schema home convention `schemas/contracts/v1/domains/habitat/` | `directory-rules.md` §12 + ADR-0001 | **CONFIRMED doctrine** / **PROPOSED path** |

[⬆ Back to top](#-habitat--identity-model)

---

## 3. Identity philosophy: entity vs value object

Habitat carries both kinds of objects. The identity model treats them differently on purpose.

> [!IMPORTANT]
> **Entity.** Identity persists through change — a `HabitatPatch` remains the same patch even when its boundary is refined or its quality score updates. Identity is primary; attributes are secondary.
>
> **Value object.** Identity does *not* matter independently — an `UncertaintySurface` cell value, a `Hydrologic Soil Group` code, or an attribute on a `HabitatQualityScore` is *what it is*; two instances with identical attributes are interchangeable.

The DDD source is explicit: *“The model must define what it means to be the same thing.”* This document defines that for Habitat.

```mermaid
flowchart LR
  subgraph Entities["Identity-bearing entities (PROPOSED classification)"]
    HP[HabitatPatch]
    EC[EcologicalSystem]
    SM[SuitabilityModel]
    CE[ConnectivityEdge]
    CO[Corridor]
    RO[RestorationOpportunity]
    SZ[StewardshipZone]
    MR[ModelRunReceipt]
  end
  subgraph ValueLike["Observation / receipt / surface families (entity-like under source role)"]
    LCO[LandCoverObservation]
    HQS[HabitatQualityScore]
    US[UncertaintySurface]
  end
  Entities -- "deterministic ID + temporal scope" --> Bundle((EvidenceBundle))
  ValueLike -- "deterministic ID per source × time × geometry" --> Bundle
  Bundle -. "spec_hash governs equivalence" .-> Catalog[(Catalog index)]
```

> [!NOTE] *(PROPOSED classification)*
> The entity/value-object split above is a **PROPOSED** reading of the Habitat object families. The Atlas marks each family as “PROPOSED deterministic basis: source id + object role + temporal scope + normalized digest,” which is consistent with treating all of them as identity-bearing in a governed catalog. The split here is a design hint, not a contract. Confirmation requires schema inspection. See [§12](#12-open-questions--verification-backlog).

[⬆ Back to top](#-habitat--identity-model)

---

## 4. The Habitat identity formula

Habitat follows the **single project-wide identity rule** that the Domains Culmination Atlas applies uniformly to every domain object family:

> **PROPOSED deterministic basis:** `source id + object role + temporal scope + normalized digest`.
> **CONFIRMED temporal posture:** source, observed, valid, retrieval, release, and correction times stay distinct where material.

Expanded for Habitat:

| Component | Meaning in Habitat | Status |
|---|---|---|
| **source id** | Stable identifier of the originating `SourceDescriptor` (e.g., NLCD vintage, USFWS critical habitat snapshot, KDWP review extract, NatureServe ecological systems version). | CONFIRMED doctrine / PROPOSED schema field |
| **object role** | The object family within Habitat (e.g., `HabitatPatch`, `SuitabilityModel`, `ConnectivityEdge`). | CONFIRMED doctrine |
| **temporal scope** | The bounded time window the object represents: `valid_from`, `valid_to`, plus the source/observed/retrieval times it derives from. | CONFIRMED doctrine |
| **normalized digest** | `spec_hash` over the canonicalized identity-bearing spec (see [§5](#5-spec_hash-bundle_id-evidence_ref_id)). | CONFIRMED doctrine / PROPOSED implementation |

This formula gives Habitat objects identity that is:

- **Reproducible** — the same logical content produces the same ID on any machine.
- **Path-free** — moving an artifact does not change its identity.
- **Evidence-anchored** — the ID resolves through `EvidenceRef → EvidenceBundle`, not through location.
- **Drift-detectable** — a hash mismatch is a refusal-to-publish event, not a warning.

[⬆ Back to top](#-habitat--identity-model)

---

## 5. `spec_hash`, `bundle_id`, `evidence_ref_id`

### 5.1 Canonical hash (`spec_hash`)

> **CONFIRMED doctrine.** `spec_hash` is computed as **SHA-256** over the **RFC 8785 JCS** canonicalization of the identity-bearing spec, recorded with an explicit algorithm prefix.

| Property | Value |
|---|---|
| Canonicalization | RFC 8785 — JSON Canonicalization Scheme (JCS) |
| Hash | SHA-256 |
| Recorded form | `jcs:sha256:<hex>` (PROPOSED prefix convention) |
| Algorithm stability | SHA-256 fixed for v1; future migration requires ADR + dual-hash window |
| Streaming-artifact roots (PMTiles, large rasters) | **BLAKE3** root / Bao outboard proof, recorded alongside `spec_hash` (PROPOSED for habitat tiles & suitability rasters) |

**Included in the hashed spec** (PROPOSED for Habitat, derived from New Ideas 5-8-26 D1):

- `object_type`, `schema_version`
- `source_refs[]` (SourceDescriptor IDs + source-side `spec_hash`)
- `dataset_refs[]`, `evidence_refs[]`, `object_refs[]`
- temporal-scope fields (`valid_from`, `valid_to`, `observed_*`, `retrieval_*` where material)
- geometry fingerprint (e.g., `geometry_hash`) where geometry is identity-bearing
- `policy_label`, `rights_status`, `sensitivity`
- for `SuitabilityModel` / `ModelRunReceipt`: `model_id`, `model_version`, `inputs[]`, `parameters`, `uncertainty_surface_ref`, `validation_ref`

**Excluded** (transport / runtime / transient, do not affect identity):

- storage URLs, file paths, container digests for transport only
- wall-clock timestamps of the run itself (those belong on the receipt, not the spec)
- signatures, nonces, ephemeral request IDs

### 5.2 Derived IDs

> **CONFIRMED doctrine** / **PROPOSED implementation** (per New Ideas 5-8-26 D2):

```text
bundle_id        = "eb-" + base32(lowercase(SHA-256(spec_hash)))[:26]
evidence_ref_id  = "er-" + base32(lowercase(SHA-256(target_bundle_spec_hash)))[:26]
```

IDs derive **only** from the normalized spec — no environment entropy, no UUIDs, no minting.

> [!TIP]
> Two Habitat artifacts with the same `spec_hash` **are** the same Habitat object, regardless of where they live, who built them, or when. Two artifacts with different `spec_hash`es are different objects — even if they were called the same name.

### 5.3 Resolution path (`EvidenceRef → EvidenceBundle`)

```mermaid
sequenceDiagram
    autonumber
    participant Client as Public client / governed API
    participant Idx as Catalog index (keyed by spec_hash)
    participant EB as EvidenceBundle store
    participant Gate as Promotion / release gate

    Client->>Idx: resolve(evidence_ref.spec_hash)
    alt hit
        Idx-->>EB: lookup(bundle_id, spec_hash)
        EB-->>Client: EvidenceBundle (spec_hash matches)
        Client->>Gate: recompute bundle_id from spec_hash
        alt id matches
            Gate-->>Client: ANSWER
        else mismatch
            Gate-->>Client: DENY (hash_mismatch)
        end
    else miss
        Idx-->>Client: ABSTAIN (validator) → DENY (policy)
    end
```

Finite outcomes follow the governed-API contract: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`. *(CONFIRMED doctrine / PROPOSED implementation.)*

[⬆ Back to top](#-habitat--identity-model)

---

## 6. Per-object identity table

The eleven Habitat object families and how the identity formula applies to each. All rows are **CONFIRMED doctrine** for the object family and **PROPOSED implementation** for field names and exact constituents.

| Habitat object | Identity-bearing inputs (PROPOSED) | Geometry role | Notable risk if identity drifts |
|---|---|---|---|
| **HabitatPatch** | source id (e.g., NLCD vintage) · `valid_from`/`valid_to` · `geometry_hash` (polygon footprint) · class assignment | Polygon (primary) | Same patch double-counted across vintages; broken corridor graph |
| **LandCoverObservation** | source id · observed time · pixel/cell scope · class code · CRS + grid spec | Raster cell or polygon | Re-classification falsely read as land-cover change |
| **EcologicalSystem** | source id (e.g., NatureServe version) · system code · `valid_from`/`valid_to` | Polygon / categorical surface | Classification-drift misread as ecological shift |
| **HabitatQualityScore** | source id · target object ref (e.g., `HabitatPatch.spec_hash`) · model spec ref · valid time · score units | Polygon (inherited) | Stale score served as current; uncertainty stripped |
| **SuitabilityModel** | `model_id` · `model_version` · ordered inputs[] · parameters · training/source support · spatial resolution · uncertainty surface ref · validation ref | Raster (typical) | Two runs of the “same” model collapsed; model-vs-observation label lost |
| **ConnectivityEdge** | endpoints (two `HabitatPatch.spec_hash`) · edge kind · `valid_from`/`valid_to` · derivation method ref | Linestring / abstract edge | Patch re-identity orphans edges; least-cost result irreproducible |
| **Corridor** | ordered patch refs · derivation method · `valid_from`/`valid_to` · cost surface ref | Polyline / polygon | Same corridor minted twice on rebuild |
| **RestorationOpportunity** | candidate site geometry · driver inputs[] · scoring method ref · valid time | Polygon | Conservation prioritization replays differ silently |
| **StewardshipZone** | source id (e.g., PAD-US version) · jurisdiction · authority role · `valid_from`/`valid_to` | Polygon | Stewardship boundary version conflated; access decision misapplied |
| **ModelRunReceipt** | model identity & version · inputs[] · parameters · `run_time` · uncertainty surface ref · validation ref | (none — process object) | Receipt re-bound to a different run = unauditable model |
| **UncertaintySurface** | source-of-uncertainty refs · method · spatial scope · `valid_from`/`valid_to` | Raster | Confidence misread as fact when surface is missing |

> [!CAUTION]
> **Model vs observation labels are part of identity in spirit, even if encoded as `object_type`.** A `SuitabilityModel` output must never be silently re-identified as a `LandCoverObservation`. The Encyclopedia is explicit: *“Keep model vs observation labels visible.”*

[⬆ Back to top](#-habitat--identity-model)

---

## 7. Temporal handling

**CONFIRMED doctrine** (Domains Culmination Atlas, Habitat §E; Encyclopedia §7.4):

> Source, observed, valid, retrieval, release, and correction times stay **distinct where material**.

| Time | What it pins | Habitat examples |
|---|---|---|
| **source time** | When the source was authored / issued | NLCD 2021 vintage; USFWS critical habitat designation date |
| **observed time** | When the underlying world-fact was observed | Aerial image acquisition date for a patch boundary |
| **valid time** | The world-time window the object applies to | `valid_from` / `valid_to` for a patch class |
| **retrieval time** | When KFM fetched the source | Wall-clock at RAW capture |
| **release time** | When KFM published the derived object | `ReleaseManifest.release_time` |
| **correction time** | When a published object was corrected | `CorrectionNotice.time` |

> [!IMPORTANT]
> The identity formula uses **temporal scope** (valid + observed where material) as an identity input. *Retrieval* and *release* times are recorded but do **not** rotate identity — otherwise every re-pull would mint a new object. *Correction* time rotates identity only when the correction changes evidentiary meaning (per New Ideas 5-8-26 D1).

**Failure modes** *(PROPOSED, derived from New Ideas 5-8-26 §4):*

| Condition | Outcome |
|---|---|
| Missing bundle for an `EvidenceRef` | ABSTAIN (validator) → DENY (policy) on publish; emit `ResolutionError.missing_bundle` |
| `evidence_ref.spec_hash` ≠ `bundle.spec_hash` | DENY; emit `ResolutionError.hash_mismatch` |
| Non-deterministic serialization (same logical spec → different bytes) | ERROR; emit `NormalizationError.nondeterministic_serialization` |
| Identity-bearing field present in data but excluded from hashed spec | DENY; emit `NormalizationError.field_exclusion_violation` |
| Unexpected hash algorithm tag | DENY; require explicit migration gate |
| Material temporal scope missing | ABSTAIN (per Encyclopedia §6 "Temporal modeling") |

[⬆ Back to top](#-habitat--identity-model)

---

## 8. Sensitivity, geoprivacy, and identity exposure

Habitat is unusual: its own objects are mostly public-safe, but **joined to fauna/flora occurrence**, they can create exposure risk that the joined identity itself encodes. The identity model must not become a side channel.

> [!WARNING]
> **CONFIRMED / PROPOSED** (Habitat §I; Habitat–Fauna thin slice; Encyclopedia):
> Regulatory critical habitat, modeled habitat, species range, occurrence points, and landscape context **must not be flattened**. Sensitive occurrence details **deny by default**. Exact occurrence-linked habitat outputs must be generalized, redacted, reviewed, or denied when they create exposure risk.

Identity-model implications:

- **Public-safe derivatives are distinct objects.** A generalized `HabitatPatch` (e.g., grid-aggregated) is a **different object** with a **different `spec_hash`** than its precise counterpart. They must not share identity. (PROPOSED rule.)
- **Geoprivacy transforms emit receipts.** When a sensitive habitat–fauna join is transformed for public release, a `RedactionReceipt` / transform receipt is created and pinned in the EvidenceBundle. The transform’s parameters are part of the *public* object's identity-bearing spec. (CONFIRMED doctrine / PROPOSED encoding.)
- **`EvidenceBundle` outranks generated text.** Identity references resolve to bundles, not summaries. Focus Mode and AI surfaces never substitute generated language for the identity-anchored bundle. (CONFIRMED doctrine.)
- **Fail-closed.** Unknown rights, unresolved source role, missing evidence, unresolved sensitivity, or absent release state → no public identity is minted; the candidate is held in QUARANTINE.

[⬆ Back to top](#-habitat--identity-model)

---

## 9. Cross-lane identity coordination

Habitat does **not** own fauna taxa, plant taxa, or animal occurrences. Cross-lane references travel **by `EvidenceRef`**, never by inlining foreign identity fields.

```mermaid
flowchart LR
  HAB[Habitat objects]
  FAU[Fauna domain]
  FLR[Flora domain]
  SOIL[Soil / Hydrology]
  HAZ[Hazards]

  HAB -- "habitat_assignment(EvidenceRef)" --> FAU
  HAB -- "vegetation_context(EvidenceRef)" --> FLR
  HAB -- "substrate / moisture (EvidenceRef)" --> SOIL
  HAB -- "stress context (EvidenceRef)" --> HAZ

  classDef hab fill:#dff5e1,stroke:#2ea44f,color:#0b3d0b;
  classDef ext fill:#f6f8fa,stroke:#999,color:#222;
  class HAB hab;
  class FAU,FLR,SOIL,HAZ ext;
```

| Cross-lane relation | Identity discipline | Status |
|---|---|---|
| Habitat ↔ Fauna (habitat assignment, occurrence context) | Sensitive joins fail closed; identity of the public Habitat object differs from any restricted counterpart; transform receipt required for any geoprivacy-changing derivative. | CONFIRMED doctrine / PROPOSED implementation |
| Habitat ↔ Flora (vegetation community, rare plant context) | Rare-plant context obeys Flora’s sensitivity controls; Habitat identity does not encode Flora taxa. | CONFIRMED doctrine / PROPOSED implementation |
| Habitat ↔ Soil / Hydrology (substrate, moisture, wetlands, riparian) | Habitat carries refs to soil/hydrology objects by `EvidenceRef`; their identities remain owned upstream. | CONFIRMED doctrine / PROPOSED implementation |
| Habitat ↔ Hazards (fire, drought, flood, smoke stress) | Hazard context joined by ref; Habitat does not republish Hazard truth. | CONFIRMED doctrine / PROPOSED implementation |

> [!NOTE]
> The Habitat × Fauna thin-slice proof is the canonical place where this discipline is exercised in practice. See `[DOM-HF]` and the verification backlog in [§12](#12-open-questions--verification-backlog).

[⬆ Back to top](#-habitat--identity-model)

---

## 10. Validators, tests, and gate behavior

All items below are **PROPOSED**; verification requires a mounted repo.

<details>
<summary><strong>Identity validators (PROPOSED locations)</strong></summary>

| Validator | Purpose | Proposed home |
|---|---|---|
| `validate_spec_hash` | Recomputes `spec_hash` from canonicalized spec; fails on mismatch | `tools/validators/evidence/` |
| `validate_identity_derivation` | Checks `bundle_id` / `evidence_ref_id` derive correctly from `spec_hash` | `tools/validators/evidence/` |
| `validate_habitat_object_identity` | Asserts every Habitat object includes the four identity inputs from [§4](#4-the-habitat-identity-formula) | `tools/validators/domains/habitat/` *(PROPOSED, ADR-0001)* |
| `validate_temporal_scope_completeness` | Refuses publish when material temporal scope is missing | `tools/validators/evidence/` |
| `validate_model_run_receipt_linkage` | Asserts `SuitabilityModel` and `HabitatQualityScore` ids bind to a `ModelRunReceipt` | `tools/validators/domains/habitat/` |
| `validate_sensitivity_transform_separation` | Asserts public-safe derivatives carry distinct `spec_hash` from any restricted counterpart | `tools/validators/policy/` |

</details>

<details>
<summary><strong>Negative-path fixtures (PROPOSED)</strong></summary>

- `habitat/identity/missing_bundle.jsonl` — `EvidenceRef` with no resolvable `EvidenceBundle` → `ABSTAIN` → `DENY` on publish.
- `habitat/identity/hash_mismatch.jsonl` — `ref.spec_hash ≠ bundle.spec_hash` → `DENY`.
- `habitat/identity/nondeterministic_serialization.jsonl` — same logical spec, different bytes → `ERROR`.
- `habitat/identity/field_exclusion_violation.jsonl` — identity-bearing field omitted from hashed spec → `DENY`.
- `habitat/identity/algo_drift.jsonl` — unexpected hash algorithm tag → `DENY`.
- `habitat/identity/sensitivity_collision.jsonl` — public-safe derivative sharing `spec_hash` with restricted counterpart → `DENY`.

</details>

<details>
<summary><strong>Gate behavior at promotion (PROPOSED)</strong></summary>

| Stage | Identity-side requirement |
|---|---|
| RAW | `SourceDescriptor` exists with stable source id; raw payload checksum recorded. |
| WORK / QUARANTINE | Identity inputs reconstructible; quarantine reason recorded on failure. |
| PROCESSED | `EvidenceRef`, `ValidationReport`, and digest closure exist; `spec_hash` computed and stable. |
| CATALOG / TRIPLET | `EvidenceBundle` resolves; `bundle_id` re-derives; catalog index keyed by `spec_hash` first, `bundle_id` second. |
| PUBLISHED | `ReleaseManifest` references current `spec_hash`; rollback target points to a prior `spec_hash`; correction path is identity-aware. |

</details>

[⬆ Back to top](#-habitat--identity-model)

---

## 11. Identity changes, renames, and migration

Per `directory-rules.md` §14.3, a rename that changes what an object **means** is a content change, not a placement change. For Habitat that implies:

- **ADR required** (e.g., new object family, semantic narrowing of `HabitatPatch`, change to identity-bearing input set).
- **Schema version bump** per ADR-0001.
- **Compatibility map** for old fixtures (`old_spec_hash → new_spec_hash` where derivable; otherwise marked irreducible).
- **Dual-hash window** when the canonicalization or hash algorithm changes (see [§5.1](#51-canonical-hash-spec_hash)).
- **Old-fixture parity tests** in `tests/domains/habitat/identity/` *(PROPOSED).* 
- **Correction notices** for any released artifacts referencing the old identity, with rollback targets recorded on the previous `ReleaseManifest`.

> [!TIP]
> Identity rotation is a release event. Treat it like one: it has a `PromotionDecision`, a `CorrectionNotice`, and a `RollbackCard`. It does not happen as part of a code refactor.

[⬆ Back to top](#-habitat--identity-model)

---

## 12. Open questions & verification backlog

| Item | What would settle it | Status |
|---|---|---|
| Confirm `schemas/contracts/v1/domains/habitat/` is the canonical schema home for Habitat identity-bearing object schemas. | Mounted repo inspection; ADR-0001 check; existing schema files. | NEEDS VERIFICATION |
| Confirm the precise identity-bearing field set per object family (the table in [§6](#6-per-object-identity-table) is PROPOSED). | Mounted schema files; `spec_normalization` doc; validator fixtures. | NEEDS VERIFICATION |
| Confirm `jcs:sha256:<hex>` algorithm-prefix convention is used uniformly in habitat artifacts. | Mounted receipts; CI workflows; validator behavior. | NEEDS VERIFICATION |
| Confirm whether BLAKE3 root-hash sidecars are emitted for habitat tiles and large suitability rasters. | Mounted tile sidecars; release manifests. | NEEDS VERIFICATION |
| Confirm public-safe derivative rule: distinct `spec_hash` from sensitive counterpart, with transform receipt linkage. | Mounted Habitat × Fauna thin-slice fixtures; policy gates. | NEEDS VERIFICATION |
| Confirm catalog index is keyed by `spec_hash` (primary) and `bundle_id` (secondary), not by mutable paths. | Mounted catalog index spec / code. | NEEDS VERIFICATION |
| Confirm rollback-target identity discipline for Habitat releases. | Mounted `ReleaseManifest`s; `RollbackCard` samples. | NEEDS VERIFICATION |
| Verify `ModelRunReceipt` linkage requirements for `SuitabilityModel` and `HabitatQualityScore`. | Mounted receipt schema; validator. | NEEDS VERIFICATION |
| Verify habitat MapLibre overlay registry and Focus Mode behavior tied to identity. | Mounted layer registry; Focus Mode tests. | NEEDS VERIFICATION (mirrors Atlas §6.N) |

[⬆ Back to top](#-habitat--identity-model)

---

## 13. Related docs

- [`docs/domains/habitat/README.md`](./README.md) — Habitat domain landing. *(TODO if absent.)*
- [`docs/domains/habitat/SOURCES.md`](./SOURCES.md) — Habitat source families & roles. *(TODO if absent.)*
- [`docs/domains/habitat/PIPELINE.md`](./PIPELINE.md) — RAW → PUBLISHED for Habitat. *(TODO if absent.)*
- [`docs/domains/habitat/SENSITIVITY.md`](./SENSITIVITY.md) — Habitat sensitivity posture & geoprivacy. *(TODO if absent.)*
- [`docs/domains/fauna/IDENTITY_MODEL.md`](../fauna/IDENTITY_MODEL.md) — Fauna identity (counterparty for Habitat × Fauna thin slice). *(TODO if absent.)*
- [`docs/standards/PROV.md`](../../standards/PROV.md) — W3C PROV-O profile.
- [`docs/architecture/contract-schema-policy-split.md`](../../architecture/contract-schema-policy-split.md) — Contract/schema/policy split.
- [`docs/adr/ADR-0001-schema-home.md`](../../adr/ADR-0001-schema-home.md) — Canonical schema home decision.
- `schemas/contracts/v1/domains/habitat/` — Habitat schemas (PROPOSED path).
- `control_plane/object_family_register.yaml` — Cross-domain object-family register.

[⬆ Back to top](#-habitat--identity-model)

---

## Appendix A — Worked example: a `HabitatPatch` identity

> **Illustrative only.** All values below are placeholders; none reference a real published artifact.

A patch in a 2021 NLCD-derived layer, valid through the next NLCD vintage:

```json
{
  "object_type": "HabitatPatch",
  "schema_version": "v1",
  "source_refs": [
    { "source_id": "src:nlcd:2021:conus", "source_spec_hash": "jcs:sha256:9a3f…" }
  ],
  "evidence_refs": [
    { "evidence_ref_id": "er-bktz4…" }
  ],
  "geometry_hash": "blake3:7c2a…",
  "valid_from": "2021-01-01",
  "valid_to":   "2025-12-31",
  "patch_class": "mixed-prairie",
  "policy_label": "public",
  "rights_status": "open",
  "sensitivity": "T0"
}
```

After JCS canonicalization + SHA-256:

```text
spec_hash       = jcs:sha256:1b9e4f7c…  (illustrative)
bundle_id       = eb-2g4h5j6k7m8n9p0qrstuvwxyz
evidence_ref_id = er-9m8n7l6k5j4h3g2fedcba0987
```

Promotion-time gate:

1. Recompute `spec_hash` from the canonicalized spec → must match the value above.
2. Resolve `evidence_ref_id` → bundle whose `spec_hash` equals the ref → must match.
3. Recompute `bundle_id` from `spec_hash` → must match the stored `bundle_id`.
4. Confirm `ReleaseManifest` references this `spec_hash`; confirm rollback target points at a prior valid `spec_hash`.

Any failure → `DENY` (publication) or `ABSTAIN` (validator), per [§7](#7-temporal-handling) failure modes.

[⬆ Back to top](#-habitat--identity-model)

---

## Appendix B — Truth labels used in this doc

| Label | Meaning here |
|---|---|
| **CONFIRMED** | Verified from attached KFM doctrine: Domains Culmination Atlas, Encyclopedia, Pass 20 Idea Index, New Ideas 5-8-26 / 5-10-26, Master MapLibre Components, Directory Rules, DDD Reference. |
| **PROPOSED** | Design / placement / implementation detail consistent with doctrine but not yet verified against a mounted repo. |
| **NEEDS VERIFICATION** | Checkable against repo evidence (schemas, validators, manifests, fixtures, CI) but not yet checked in this session. |
| **UNKNOWN** | Not resolvable without further evidence. |

---

<sub>**Related docs:** [README](./README.md) · [SOURCES](./SOURCES.md) · [PIPELINE](./PIPELINE.md) · [SENSITIVITY](./SENSITIVITY.md) · [Fauna Identity Model](../fauna/IDENTITY_MODEL.md) · [PROV standard](../../standards/PROV.md)</sub>
<sub>**Last updated:** 2026-05-17 · **Doc version:** v1 (draft) · [⬆ Back to top](#-habitat--identity-model)</sub>

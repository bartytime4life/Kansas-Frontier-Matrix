<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/domains/fauna/api-contracts
title: Fauna — API Contracts
type: standard
version: v1
status: draft
owners: <fauna-domain-steward> + <contract-schema-steward>  # TODO confirm in OWNERS
created: 2026-05-16
updated: 2026-05-29
policy_label: public
related: [docs/domains/fauna/README.md, docs/domains/fauna/SCHEMAS.md, docs/domains/fauna/POLICY.md, docs/runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md, docs/architecture/governed-api.md, contracts/OBJECT_MAP.md, schemas/contracts/v1/runtime/runtime_response_envelope.schema.json, schemas/contracts/v1/ui/evidence_drawer_payload.schema.json, schemas/contracts/v1/map/layer_manifest.schema.json, schemas/contracts/v1/ai/ai_receipt.schema.json, ai-build-operating-contract.md]
tags: [kfm, fauna, api, contracts, governed-api]
notes: [CONTRACT_VERSION pinned 3.0.0 # all route paths, DTO field lists, and status codes PROPOSED until verified against a mounted repo and an accepted ADR # exact Fauna feature/detail resolver route is UNKNOWN per Atlas §7.J # Atlas §7.J names the DTO FaunaDecisionEnvelope # schema slug fauna vs domains/fauna is CONFLICTED → OQ-FAUNA-API-011]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# 🦫 Fauna — API Contracts

> Governed API surfaces, DTOs, finite outcomes, sensitivity posture, and validation
> contracts for the **Fauna** domain lane.

![status: draft](https://img.shields.io/badge/status-draft-yellow)
![doc type: standard](https://img.shields.io/badge/doc%20type-standard-blue)
![domain: fauna](https://img.shields.io/badge/domain-fauna-2ea44f)
![authority: governed%20API](https://img.shields.io/badge/authority-governed%20API-6f42c1)
![envelope: ANSWER%2FABSTAIN%2FDENY%2FERROR](https://img.shields.io/badge/envelope-ANSWER%20%7C%20ABSTAIN%20%7C%20DENY%20%7C%20ERROR-orange)
![sensitivity: deny--by--default](https://img.shields.io/badge/sensitivity-deny--by--default-critical)
![contract: 3.0.0](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-success)
![ci: TODO](https://img.shields.io/badge/ci-TODO-lightgrey)

| Field          | Value                                                                                  |
| -------------- | -------------------------------------------------------------------------------------- |
| **Status**     | `draft`                                                                                |
| **Owners**     | `<fauna-domain-steward>` + `<contract-schema-steward>` (placeholders — confirm in OWNERS) |
| **Last updated** | 2026-05-29                                                                           |
| **Contract**   | `CONTRACT_VERSION = "3.0.0"`                                                            |
| **Schema home** | `schemas/contracts/v1/` (per `ADR-0001-schema-home`) — Fauna-specific schemas: `schemas/contracts/v1/domains/fauna/` (slug CONFLICTED — see §13) |
| **Truth posture** | CONFIRMED doctrine; **PROPOSED** implementation. Exact routes, DTO field lists, and HTTP code mappings are **UNKNOWN** until repo verification. |

---

## Mini Table of Contents

1. [Scope and Boundary](#1-scope-and-boundary)
2. [Finite Outcome Grammar](#2-finite-outcome-grammar)
3. [Surface Map (Fauna API Contracts at a Glance)](#3-surface-map-fauna-api-contracts-at-a-glance)
4. [Request → Decision → Response Flow](#4-request--decision--response-flow)
5. [Surface 1 — Fauna Feature / Detail Resolver](#5-surface-1--fauna-feature--detail-resolver)
6. [Surface 2 — Fauna Layer Manifest Resolver](#6-surface-2--fauna-layer-manifest-resolver)
7. [Surface 3 — Fauna Evidence Drawer Payload](#7-surface-3--fauna-evidence-drawer-payload)
8. [Surface 4 — Fauna Focus Mode Answer](#8-surface-4--fauna-focus-mode-answer)
9. [Surface 5 — Correction Submit & Review Decision](#9-surface-5--correction-submit--review-decision)
10. [Sensitivity Posture and Required Denials](#10-sensitivity-posture-and-required-denials)
11. [Receipts and Audit Trail](#11-receipts-and-audit-trail)
12. [Validators, Tests, and Negative Fixtures](#12-validators-tests-and-negative-fixtures)
13. [PROPOSED File Homes](#13-proposed-file-homes)
14. [Open Questions and Verification Backlog](#14-open-questions-and-verification-backlog)
15. [Related Docs](#15-related-docs)

---

## 1. Scope and Boundary

**CONFIRMED doctrine / PROPOSED implementation.** This document specifies the
**governed API contracts** exposed by the Fauna domain lane: the externally observable
shape of requests, the DTOs returned, the finite outcome grammar, the sensitivity
gates that may convert an apparent answer into `ABSTAIN` or `DENY`, and the receipts
emitted as audit trail. It does **not** define internal storage, internal pipeline
shapes, or internal source-of-truth structures — those live behind the Fauna trust
membrane and reach public clients only through the surfaces below.

**This document is contract-bearing for:**

- Surfaces, DTOs, and outcomes that public or semi-public Fauna clients may rely on.
- Sensitivity-driven denial behavior on Fauna surfaces.
- Receipt and proof-object shape required at every Fauna runtime response.

**This document is not:**

- The schema authority. Each DTO has a separate schema file under
  `schemas/contracts/v1/...` (PROPOSED). The schema file wins on field shape; this doc
  cites it.
- The policy authority. Policy rules and obligations live under
  `policy/domains/fauna/...` (PROPOSED). This doc references their behavioral surface.
- The source registry. Fauna source descriptors live under
  `data/registry/sources/fauna/...` and per-source SOPs in
  `docs/runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md`.

> [!IMPORTANT]
> Every surface below is **PROPOSED**. The Atlas §7.J records the Fauna feature/detail
> resolver route as **UNKNOWN** ("route TBD") and names the response DTO
> `FaunaDecisionEnvelope`. Treat HTTP verbs, paths, and status codes in this document as
> design candidates pending an ADR and a mounted-repo verification pass. [DOM-FAUNA §7.J]

[↑ Back to top](#top)

---

## 2. Finite Outcome Grammar

**CONFIRMED doctrine.** Every Fauna runtime response is a finite envelope. A public
client receives exactly one of four outcomes; protocol-level success (an HTTP 200) is
**not** the same as `ANSWER`. The envelope reason carries the KFM truth label. [ENCY] [GAI]

| Outcome   | Meaning                                                                                   | Required body                              |
| --------- | ----------------------------------------------------------------------------------------- | ------------------------------------------ |
| `ANSWER`  | Evidence resolved, policy allows, release state is `published`, citation validation passed | `evidence_refs`, `policy_decision`, payload |
| `ABSTAIN` | Evidence is missing, ambiguous, or fails citation validation                              | `reason_code`, `evidence_refs[]` (may be empty) |
| `DENY`    | Policy, rights, sensitivity, or release state blocks the request                          | `policy_decision`, `reason_code`           |
| `ERROR`   | Validation, schema, or system failure                                                     | `error_code`, `details`                    |

> [!NOTE]
> `200 + ABSTAIN` is a successful interaction with a deliberate "no evidence" answer.
> A public client must render `ABSTAIN`/`DENY`/`ERROR` legibly — never as a generic
> "missing data" or "500 try again." This is a standing UX requirement on every Fauna
> client. PROPOSED — see Verification Backlog item **V-FAUNA-API-002**.

### 2.1 PROPOSED HTTP code mapping

> [!CAUTION]
> The mapping below is a **design candidate**. It is not enforced anywhere yet and
> has not been ratified by an ADR. **NEEDS VERIFICATION** before any client treats
> these codes as contract.

| Outcome   | PROPOSED HTTP code | Notes                                                                  |
| --------- | ------------------ | ---------------------------------------------------------------------- |
| `ANSWER`  | `200`              | Body carries `outcome: "ANSWER"`; not all `200`s are answers.          |
| `ABSTAIN` | `200`              | Body carries `outcome: "ABSTAIN"` and a reason; *not* `404`.           |
| `DENY`    | `403`              | Body carries `outcome: "DENY"` with `policy_decision` and reason code. |
| `ERROR`   | `400` / `422` / `500` | Distinguish bad request (`400`/`422`) from server failure (`500`). |

[↑ Back to top](#top)

---

## 3. Surface Map (Fauna API Contracts at a Glance)

Surfaces 1–4 are drawn directly from the Domains Atlas **§7.J** Fauna API table; surfaces
5–7 are drawn from the Encyclopedia / Atlas **§20.3 Master API Surface Table** (correction/
rollback, review queue, evidence resolver) applied to the Fauna lane. Routes shown are
**proposed**; exact paths remain UNKNOWN until verified. [DOM-FAUNA §7.J] [ENCY §20.3]

| # | Surface                              | PROPOSED route (illustrative)                          | DTO / schema (PROPOSED)                                  | Finite outcomes                  | Status                                       |
| - | ------------------------------------ | ------------------------------------------------------ | -------------------------------------------------------- | -------------------------------- | -------------------------------------------- |
| 1 | Fauna feature / detail resolver      | `GET /api/v1/domains/fauna/features/{id}`              | **`FaunaDecisionEnvelope`** (+ `FeatureDTO`, `EvidenceRef[]`) | ANSWER / ABSTAIN / DENY / ERROR  | PROPOSED; **exact route UNKNOWN** [§7.J]     |
| 2 | Fauna layer manifest resolver        | `GET /api/v1/layers/{layer_id}/manifest`               | `LayerManifest` (Fauna-tagged)                           | ANSWER / DENY / ERROR            | PROPOSED; public-safe release only [§7.J]    |
| 3 | Fauna Evidence Drawer payload        | `POST /api/v1/claims/resolve` *(map-feature path)*     | `EvidenceDrawerPayload` + `EvidenceBundle` projection    | ANSWER / ABSTAIN / DENY / ERROR  | PROPOSED; evidence- and policy-filtered [§7.J] |
| 4 | Fauna Focus Mode answer              | `POST /api/v1/focus/query`                             | `RuntimeResponseEnvelope` + `AIReceipt`                  | ANSWER / ABSTAIN / DENY / ERROR  | PROPOSED; AI never root truth [§7.J]         |
| 5 | Correction submit                    | `POST /api/v1/corrections`                             | `CorrectionNoticeCandidate`                              | ACCEPTED / DENY / ERROR          | PROPOSED [§20.3 correction/rollback]         |
| 6 | Review decision (steward-only)       | `POST /api/v1/review/{queue}/{id}/decision`            | `ReviewRecord` + `PolicyDecision`                        | ALLOW / RESTRICT / DENY / ERROR  | PROPOSED [§20.3 review queue]                |
| 7 | Evidence bundle resolution           | `GET /api/v1/evidence/{bundle_id}`                     | `EvidenceBundle`                                         | ANSWER / DENY / ERROR            | PROPOSED [§20.3 evidence resolver]           |

**Schema responsibility root:** `schemas/contracts/v1/` — per
[ADR-0001 (schema home)](../../adr/ADR-0001-schema-home.md). Fauna-specific schemas
are placed under `schemas/contracts/v1/domains/fauna/`. **PROPOSED**; verify against
mounted repo evidence and Directory Rules §6 / §12 before treating as canonical.

> [!NOTE]
> **DTO naming.** The Atlas §7.J names the per-domain envelope `FaunaDecisionEnvelope`
> (cf. §20.3's generic `DecisionEnvelope` / `DomainFeatureEnvelope`). Surface 1 uses
> `FaunaDecisionEnvelope`; surface 4 uses `RuntimeResponseEnvelope` (the Focus Mode
> runtime form). Whether these are one envelope with a domain projection or two distinct
> schemas is **NEEDS VERIFICATION** — see **V-FAUNA-API-011**.

[↑ Back to top](#top)

---

## 4. Request → Decision → Response Flow

The diagram below shows how a single Fauna request — say, a map click on an occurrence
marker — is processed by the trust membrane. The grammar is the same for every Fauna
surface: **resolve evidence → apply policy and sensitivity gates → emit a finite envelope with receipts**.

```mermaid
flowchart TD
    A[Public Client<br/>map click / Focus query / layer load] -->|HTTP request| B[Governed API<br/>Fauna surface]
    B --> C{Identity & scope<br/>resolution}
    C -->|invalid| Z1[ERROR<br/>400 / 422]
    C -->|valid| D[EvidenceRef → EvidenceBundle<br/>resolution]
    D -->|unresolvable| Z2[ABSTAIN<br/>reason: evidence_missing]
    D -->|resolved| E{Policy + sensitivity<br/>gate<br/>policy/domains/fauna/...}
    E -->|deny| Z3[DENY<br/>policy_decision + reason]
    E -->|allow| F{Release state<br/>= published?}
    F -->|no| Z4[ABSTAIN or DENY<br/>per release rule]
    F -->|yes| G{Citation validation<br/>cite-or-abstain}
    G -->|fail| Z5[ABSTAIN<br/>reason: uncited]
    G -->|pass| H[ANSWER<br/>FaunaDecisionEnvelope + receipts]

    H --> R[(AIReceipt /<br/>PolicyDecision /<br/>CitationValidationReport)]
    Z3 --> R
    Z2 --> R
    Z5 --> R
    classDef deny fill:#b22,stroke:#700,color:#fff;
    class Z3 deny;
```

> [!NOTE]
> **PROPOSED.** The flow reflects KFM doctrine on cite-or-abstain, evidence resolution,
> and policy gating, but the precise call graph (which adapter resolves evidence, which
> rule engine evaluates policy, which signer emits receipts) is **NEEDS VERIFICATION**
> against the mounted repo.

[↑ Back to top](#top)

---

## 5. Surface 1 — Fauna Feature / Detail Resolver

**Purpose.** Resolve a single Fauna feature (e.g., an occurrence, a range polygon, a
seasonal range, a sensitive site reference) to a `FeatureDTO` plus the `EvidenceRef`
list that supports its claims, wrapped in a `FaunaDecisionEnvelope`. [DOM-FAUNA §7.J]

### 5.1 Request (PROPOSED)

| Field           | Type      | Required | Notes                                                     |
| --------------- | --------- | -------- | --------------------------------------------------------- |
| `id`            | string    | yes      | Deterministic Fauna feature id. **PROPOSED** identity basis: source id + object role + temporal scope + normalized digest. |
| `time_context`  | string    | no       | ISO-8601 / interval. Defaults to release-current.         |
| `bbox`          | array     | no       | Used by some clients; **never** used to bypass geoprivacy.|
| `user_role`     | string    | no       | Used only for policy evaluation; never reflected in body. |

> [!CAUTION]
> The resolver does **not** accept "raw geometry" or "internal coordinates" arguments.
> Requests that imply RAW / WORK / QUARANTINE access are denied (see §10).

### 5.2 Response — `ANSWER` body (PROPOSED)

The DTO is the Fauna projection wrapped in `FaunaDecisionEnvelope` (PROPOSED schema home:
`schemas/contracts/v1/domains/fauna/feature_dto.schema.json`). The shape illustrated
below is **PROPOSED / illustrative**; field names and types may change.

```json
{
  "outcome": "ANSWER",
  "feature": {
    "feature_id": "kfm:fauna:occurrence:<sha256-prefix>",
    "object_family": "Occurrence Public",
    "taxon_ref": "kfm:fauna:taxon:<digest>",
    "geometry": {
      "type": "Point",
      "coordinates": [-98.45, 38.74],
      "geoprivacy_transform": {
        "method": "tile_precision",
        "params": {"z": 9},
        "redaction_receipt_ref": "kfm:receipt:redaction:<id>"
      }
    },
    "observed_time": "2025-08-12",
    "release_time": "2026-04-01",
    "source_role": "observation",
    "policy_label": "public",
    "sensitivity": "generalize"
  },
  "evidence_refs": [
    {"role": "primary", "ref": "kfm:evidence:bundle:<digest>"}
  ],
  "policy_decision": {
    "decision_id": "kfm:policy:decision:<id>",
    "outcome": "allow",
    "reasons": ["rights_status=public", "review_state=approved"]
  },
  "citation_validation": {
    "verdict": "ok",
    "resolved": 1,
    "missing": 0
  }
}
```

### 5.3 Outcome behavior

| Outcome   | Trigger (PROPOSED)                                                                            |
| --------- | --------------------------------------------------------------------------------------------- |
| `ANSWER`  | Feature is resolved, released, policy-allowed, and cited.                                     |
| `ABSTAIN` | Feature exists in lineage but lacks resolvable `EvidenceBundle` or fails citation validation. |
| `DENY`    | Feature is sensitive (nest / den / roost / hibernacula / spawning / steward-controlled) and no geoprivacy transform + Redaction Receipt has been recorded; OR rights status is unresolved; OR review state blocks release. |
| `ERROR`   | Invalid id, schema mismatch, or system failure.                                               |

[↑ Back to top](#top)

---

## 6. Surface 2 — Fauna Layer Manifest Resolver

**Purpose.** Return the release-bound manifest for a published Fauna map layer
(`LayerManifest`): release state, asset digests, allowed fields per tile, valid/release
time, evidence binding, and rollback target. [DOM-FAUNA §7.J]

### 6.1 Request (PROPOSED)

`GET /api/v1/layers/{layer_id}/manifest`

`layer_id` must reference a Fauna-tagged released layer. Unreleased / candidate layers
are not addressable on this surface.

### 6.2 Response — `ANSWER` body shape (PROPOSED)

| Field                  | Notes                                                                                          |
| ---------------------- | ---------------------------------------------------------------------------------------------- |
| `layer_id`             | Fauna-domain-tagged layer identifier.                                                          |
| `release_state`        | `published` only on this surface; candidate / quarantine states are not exposed.               |
| `tile_field_allowlist` | The set of fields that may appear in the served PMTiles / vector tile. Sensitive fields excluded. |
| `evidence_ref_field`   | Per-feature `EvidenceRef` used by the Evidence Drawer.                                         |
| `temporal_fields`      | Valid / release / observed time fields surfaced for time slider use.                           |
| `release_manifest_ref` | `ReleaseManifest` digest pinning this layer's release.                                         |
| `rollback_target`      | The prior released layer manifest, for emergency rollback.                                     |

> [!WARNING]
> The `tile_field_allowlist` is a **trust contract**, not a UI convenience.
> Validator tests must enforce that no field outside the allowlist appears in published
> Fauna tiles — see Validators §12 and `tile-field-allowlist` tests. PROPOSED. [DOM-FAUNA §7.K]

### 6.3 Outcome behavior

| Outcome  | Trigger (PROPOSED)                                                                |
| -------- | --------------------------------------------------------------------------------- |
| `ANSWER` | Layer is published and manifest closure passes.                                   |
| `DENY`   | Layer is not released, or layer is restricted to steward review surfaces only.    |
| `ERROR`  | Layer id invalid or manifest fails schema validation.                             |

Note: there is no `ABSTAIN` on this surface — the manifest either exists and is
released, or it is denied / errored. This matches the Atlas §7.J outcome set for the
layer manifest resolver (`ANSWER / DENY / ERROR`). [DOM-FAUNA §7.J]

[↑ Back to top](#top)

---

## 7. Surface 3 — Fauna Evidence Drawer Payload

**Purpose.** When a public client selects a Fauna feature on the map, the Drawer
payload exposes only what is policy-safe: the claim, its `EvidenceRef`s, source roles,
review state, rights, sensitivity, any transforms applied, and correction links. [DOM-FAUNA §7.J]

### 7.1 Request (PROPOSED)

`POST /api/v1/claims/resolve` with a feature reference produced by the map adapter.

The Drawer payload is delivered through the same governed API client as other Fauna
surfaces; no direct database query, no direct evidence-store call, and no model call
ever reaches the browser.

### 7.2 Response (PROPOSED — illustrative)

```json
{
  "outcome": "ANSWER",
  "drawer": {
    "feature_id": "kfm:fauna:occurrence:<digest>",
    "layer_id": "fauna.occurrence.public.v1",
    "claim_summary": "Observation of <taxon>, generalized to z=9 tile.",
    "evidence_bundle_refs": ["kfm:evidence:bundle:<digest>"],
    "source_summary": [
      {"source_id": "kfm:source:<id>", "role": "observation", "rights_status": "public"}
    ],
    "citations": [{"resolved": true, "ref": "kfm:evidence:<id>"}],
    "policy_state": {"sensitivity": "generalize", "policy_label": "public"},
    "release_state": "published",
    "limitations": ["geoprivacy_transform: tile_precision z=9"],
    "transforms": [{"redaction_receipt_ref": "kfm:receipt:redaction:<id>"}],
    "correction_link": "/corrections/new?subject=kfm:fauna:occurrence:<digest>"
  },
  "evidence_refs": [{"role": "primary", "ref": "kfm:evidence:bundle:<digest>"}],
  "policy_decision": {"outcome": "allow"},
  "citation_validation": {"verdict": "ok"}
}
```

### 7.3 Outcome behavior

The Drawer is the most user-facing trust surface; **negative outcomes must render**,
not hide.

| Outcome   | Drawer rendering (PROPOSED)                                                                    |
| --------- | ---------------------------------------------------------------------------------------------- |
| `ANSWER`  | Claim + citations + source roles + sensitivity badge + correction link.                        |
| `ABSTAIN` | "Evidence not available for this feature" + reason code + correction link.                     |
| `DENY`    | "Restricted — sensitive site / unresolved rights" + reason code; no geometry, no coordinates.  |
| `ERROR`   | "Cannot load evidence for this feature." Surface the request id; never the stack trace.        |

[↑ Back to top](#top)

---

## 8. Surface 4 — Fauna Focus Mode Answer

**Purpose.** Bounded synthesis through the governed AI adapter. A Focus query about
Fauna (e.g., "summarize what released evidence says about this taxon's range in this
HUC") is answered only over **released** `EvidenceBundle`s; an `AIReceipt` is emitted
for every call. [DOM-FAUNA §7.J] [GAI]

### 8.1 Request (PROPOSED)

`POST /api/v1/focus/query` — body shape `FocusModeRequest`
(`schemas/contracts/v1/ai/focus_mode_request.schema.json`).

| Field                  | Notes                                                                            |
| ---------------------- | -------------------------------------------------------------------------------- |
| `question`             | Free text scoped to released evidence.                                           |
| `map_context_envelope` | Bounded map context: visible layers, bounds, zoom, time window, selected features. |
| `evidence_refs`        | Optional pre-resolved `EvidenceRef`s to constrain scope.                         |
| `policy_context`       | Caller-asserted scope; the server reasserts via policy decision.                 |
| `user_role`            | Used only for policy evaluation.                                                 |

### 8.2 Response — `RuntimeResponseEnvelope` + `AIReceipt` (PROPOSED)

The shape is the generic `FocusModeResponse` / `RuntimeResponseEnvelope` (`outcome`,
`answer`, `citations`, `abstain_reason`, `deny_reason`, `evidence_used`,
`policy_decisions`, `ai_receipt_id`). For Fauna the additional discipline is:

- `ABSTAIN` whenever evidence is insufficient — including unanswerable questions about
  sensitive sites.
- `DENY` whenever the question would require exposing sensitive geometry, restricted
  personal/DNA inference, or emergency-alert behavior. KFM is **not** an alert
  authority.
- Every Focus call emits an `AIReceipt` recording prompt scope, evidence used, model
  identity, policy decision, and outcome.

> [!IMPORTANT]
> The Fauna Focus Mode answer must never contain a claim not backed by a resolved,
> released `EvidenceBundle`. Citation validation runs *before* the answer is rendered.
> If citation validation fails, the outcome is `ABSTAIN`, even if the model produced
> fluent text. **CONFIRMED doctrine; PROPOSED implementation.** [GAI] [DOM-FAUNA]

[↑ Back to top](#top)

---

## 9. Surface 5 — Correction Submit & Review Decision

**Purpose.** Provide a public correction path for Fauna claims and a steward-only
review decision surface for promotion / restriction / denial of candidate transitions.
Drawn from the §20.3 Master API Surface Table (correction/rollback; review queue). [ENCY §20.3]

### 9.1 Correction submit

`POST /api/v1/corrections`

Public surface. Accepts a `CorrectionNoticeCandidate` referencing a published Fauna
claim. The server records the candidate and emits a receipt; it does **not** mutate
the published artifact. Promotion of the correction is a separate governed transition.

| Outcome    | Trigger (PROPOSED)                                            |
| ---------- | ------------------------------------------------------------- |
| `ACCEPTED` | Candidate is well-formed and references a published claim.    |
| `DENY`     | Reference is to RAW/WORK/QUARANTINE or a restricted lane.     |
| `ERROR`    | Malformed candidate or schema validation failure.             |

### 9.2 Review decision (steward-only)

`POST /api/v1/review/{queue}/{id}/decision`

Steward-authenticated surface. Emits a `ReviewRecord` + `PolicyDecision` with decision
`ALLOW` / `RESTRICT` / `DENY` and policy-linked obligations — matching the §20.3 review
queue outcome set. [ENCY §20.3]

> [!CAUTION]
> The review decision surface is **never** exposed to public clients. Treat any
> apparent public path to this surface as a defect. **PROPOSED**; verify via
> `policy/domains/fauna/...` and an authorization smoke test (see V-FAUNA-API-007).

[↑ Back to top](#top)

---

## 10. Sensitivity Posture and Required Denials

**CONFIRMED / PROPOSED.** Per Atlas §7.I (verbatim doctrine): *exact sensitive
occurrence, nest, den, roost, hibernacula, spawning, and steward-controlled records fail
closed; public exact occurrence tiles for sensitive taxa are denied.* Unclear rights,
unresolved source role, missing evidence, unresolved sensitivity, or absent release
state blocks public promotion. [DOM-FAUNA §7.I] [ENCY §20.5] [DIRRULES]

### 10.1 Required denials on every Fauna surface

| Trigger                                                                       | Required outcome |
| ----------------------------------------------------------------------------- | ---------------- |
| Request implies RAW / WORK / QUARANTINE access                                | `DENY`           |
| Exact sensitive-location exposure (nest, den, roost, hibernacula, spawning)   | `DENY`           |
| Restricted personal / DNA inference about living persons                      | `DENY`           |
| Request would substitute for emergency alerting                               | `DENY`           |
| Answer would assert an uncited authoritative claim                            | `ABSTAIN`        |
| Source rights unresolved or `rights_status != public`                         | `DENY`           |
| Review state required and not approved                                        | `DENY` or `ABSTAIN` per policy |
| Geoprivacy transform required but no Redaction Receipt exists                 | `DENY`           |

> [!CAUTION]
> The §20.5 deny-by-default register allows release of a sensitive fauna record **only**
> when **geoprivacy + Redaction Receipt + public-safe derivative** are all present. No
> single one of those is sufficient. [DOM-FAUNA] [ENCY §20.5]

### 10.2 Geoprivacy transform record

When geometry is generalized or buffered before release, every transform must be
recorded in a Redaction Receipt and referenced from the served feature. This implements
the fauna geoprivacy conditional-schema rule (a fauna occurrence requires
`public_safe_geometry` when `geoprivacy_status` is obscured / private / generalized).
PROPOSED shape:

```json
{
  "transform_method": "tile_precision",
  "params": {"z": 9},
  "policy_ref": "policy/domains/fauna/sensitivity.rego#generalize_tiles",
  "redaction_receipt_ref": "kfm:receipt:redaction:<id>",
  "kept_fields": ["taxon_ref", "observed_time", "source_role"],
  "removed_fields": ["precise_point", "site_descriptor"]
}
```

> [!WARNING]
> A transform without a resolvable Redaction Receipt is **not** a transform. The
> served feature must be denied until the receipt is recorded. PROPOSED enforcement
> path: `tile-field-allowlist` validator + `redaction-receipt-resolution` validator.

[↑ Back to top](#top)

---

## 11. Receipts and Audit Trail

**CONFIRMED doctrine.** Every Fauna runtime response emits the receipts required to
reconstruct the decision after the fact. Schema homes below are confirmed in the Master
MapLibre components report's contract table where noted; receipt-class split is subject
to ADR-S-03. [MAP-MASTER] [ENCY §24.12]

| Receipt                       | When emitted                                  | PROPOSED schema home                                                  |
| ----------------------------- | --------------------------------------------- | --------------------------------------------------------------------- |
| `RuntimeResponseEnvelope`     | Every response on every surface               | `schemas/contracts/v1/runtime/runtime_response_envelope.schema.json`  |
| `PolicyDecision`              | Every gated request                           | `schemas/contracts/v1/policy/policy_decision.schema.json`             |
| `CitationValidationReport`    | Every `ANSWER` and every Focus call           | `schemas/contracts/v1/evidence/citation_validation_report.schema.json`|
| `AIReceipt`                   | Every Focus Mode answer                       | `schemas/contracts/v1/ai/ai_receipt.schema.json`                      |
| `Redaction Receipt`           | Every geoprivacy transform applied to a Fauna geometry | `schemas/contracts/v1/receipts/redaction_receipt.schema.json` (PROPOSED) |
| `ReleaseManifest` reference   | Every published layer manifest                | `schemas/contracts/v1/release/...` or `.../map/map_release_manifest.schema.json` (split open, ADR-S-03) |
| `PromotionDecision` reference | Every release-state transition                | `schemas/contracts/v1/release/promotion_decision.schema.json`         |

> [!NOTE]
> Receipts are **process memory and audit trail**. They are not the release authority.
> The release authority is `ReleaseManifest`. Do not place receipts in `release/`. [DIRRULES]

[↑ Back to top](#top)

---

## 12. Validators, Tests, and Negative Fixtures

PROPOSED validator set required before any Fauna surface advances past
`docs/runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md` synthetic-fixture stage. Rows 1–6 map
directly to the Atlas §7.K validator list. [DOM-FAUNA §7.K]

| Validator / test                                  | Surface(s) covered                | Status   |
| ------------------------------------------------- | --------------------------------- | -------- |
| Source-role authority tests                       | 1, 2, 7                           | PROPOSED [§7.K] |
| Taxonomy resolution and ambiguity tests           | 1, 3, 4                           | PROPOSED [§7.K] |
| Occurrence restricted/public split tests          | 1, 2, 3                           | PROPOSED [§7.K] |
| Redaction Receipt validation                      | 1, 2, 3                           | PROPOSED [§7.K] |
| Tile field allowlist tests                        | 2                                 | PROPOSED [§7.K] |
| Runtime Response Envelope negative cases          | All                               | PROPOSED [§7.K] |
| Citation validation (`cite-or-abstain`)           | 1, 3, 4                           | PROPOSED |
| Policy deny tests (sensitive sites, RAW access)   | All                               | PROPOSED |
| Release manifest closure                          | 2                                 | PROPOSED |
| Rollback drill                                    | 2                                 | PROPOSED |
| No-network fixtures (synthetic Fauna data only)   | All                               | PROPOSED |
| Non-regression for prior released lineage         | 2                                 | PROPOSED |

<details>
<summary><strong>Required negative fixtures (PROPOSED list)</strong></summary>

- Fauna feature request for a sensitive taxon's exact coordinates → must produce `DENY`.
- Layer manifest request for an unreleased candidate → must produce `DENY`.
- Drawer payload request for a feature whose `EvidenceBundle` is unresolvable → must produce `ABSTAIN`.
- Focus query that would only be answerable by citing unreleased evidence → must produce `ABSTAIN`.
- Focus query that solicits emergency alerting → must produce `DENY`.
- Correction submit referencing a RAW path → must produce `DENY`.
- Geoprivacy transform applied without a resolvable Redaction Receipt → must produce `DENY` on read.
- Tile produced with a field outside the allowlist → must fail the `tile-field-allowlist` validator at release gate.
- Citation validation report with `verdict: fail` reaching the renderer → must be intercepted and converted to `ABSTAIN`.
- Source descriptor with `rights_status` unresolved → must block public release path.

</details>

[↑ Back to top](#top)

---

## 13. PROPOSED File Homes

Per Directory Rules §6, §12, and `ADR-0001-schema-home`. **PROPOSED** — verify against
mounted repo state before treating as canonical. Do not create parallel schema /
contract / policy homes without an ADR.

> [!IMPORTANT]
> **Schema/contract slug is CONFLICTED (V-FAUNA-API-011).** The tree below uses the
> Directory Rules §12 lane form (`schemas/contracts/v1/domains/fauna/`), which the repo
> structure guiding document confirms. The Atlas §24.13 crosswalk instead uses
> `schemas/contracts/v1/fauna/` (no `domains/` segment). Directory Rules §12 governs in
> the authority order, but the conflict requires an ADR before either is canonical.
> [DIRRULES §12] [ENCY §24.13]

```text
docs/domains/fauna/
├── README.md
├── API_CONTRACTS.md          # this document
├── SCHEMAS.md                # PROPOSED — DTO field reference
├── POLICY.md                 # PROPOSED — sensitivity & rights policy doc
└── SOURCES.md                # PROPOSED — source family overview

contracts/domains/fauna/
├── README.md
├── OBJECT_MAP.md             # crosswalk: object family → DTO → schema → policy
└── ...

schemas/contracts/v1/domains/fauna/
├── feature_dto.schema.json
├── fauna_decision_envelope.schema.json   # per Atlas §7.J DTO name
├── occurrence_public.schema.json
├── occurrence_restricted.schema.json
├── range_polygon.schema.json
├── seasonal_range.schema.json
├── migration_route.schema.json
├── sensitive_site.schema.json
├── conservation_status.schema.json
├── taxon.schema.json
└── taxon_crosswalk.schema.json

schemas/contracts/v1/runtime/
└── runtime_response_envelope.schema.json

schemas/contracts/v1/ui/
├── evidence_drawer_payload.schema.json
└── map_context_envelope.schema.json

schemas/contracts/v1/map/
├── layer_manifest.schema.json
└── map_release_manifest.schema.json

schemas/contracts/v1/ai/
├── focus_mode_request.schema.json
├── focus_mode_response.schema.json
└── ai_receipt.schema.json

policy/domains/fauna/
├── sensitivity.rego
├── publication.rego
└── README.md

policy/geoprivacy/                     # cross-cutting geoprivacy (per repo structure doc)
tests/domains/fauna/
├── contracts/
├── policy/
├── tile_field_allowlist/
└── negative_fixtures/

fixtures/domains/fauna/
├── synthetic/
└── golden/

docs/runbooks/fauna/
└── SOURCE_REFRESH_RUNBOOK.md   # existing — referenced by this contract
```

> [!NOTE]
> The lane pattern above is the **shape**, not a claim that every path already exists.
> A mounted-repo verification pass (see Verification Backlog **V-FAUNA-API-001**) is
> required before any client treats these paths as present.

[↑ Back to top](#top)

---

## 14. Open Questions and Verification Backlog

| ID                  | Item                                                                                          | Evidence that would settle it                                                                 | Status              |
| ------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ------------------- |
| `V-FAUNA-API-001`   | Confirm exact Fauna feature/detail resolver route                                             | Mounted-repo API app, OpenAPI/route registry, or accepted ADR                                 | UNKNOWN [§7.J]      |
| `V-FAUNA-API-002`   | Confirm HTTP code mapping for ANSWER/ABSTAIN/DENY/ERROR                                       | Mounted-repo response middleware + accepted ADR                                               | NEEDS VERIFICATION  |
| `V-FAUNA-API-003`   | Confirm schema home placement under `schemas/contracts/v1/domains/fauna/`                     | `schemas/` tree inspection + ADR-0001 conformance check                                       | NEEDS VERIFICATION  |
| `V-FAUNA-API-004`   | Verify Redaction Receipt schema and resolution path                                           | `schemas/contracts/v1/receipts/redaction_receipt.schema.json` + resolver implementation       | NEEDS VERIFICATION  |
| `V-FAUNA-API-005`   | Verify tile-field-allowlist validator presence and CI wiring                                  | `tools/validators/...` + CI workflow inspection                                               | NEEDS VERIFICATION  |
| `V-FAUNA-API-006`   | Confirm Focus Mode adapter contract for Fauna (no direct browser-to-model path)               | Governed-AI adapter ADR (cf. ADR-S backlog) + runtime path inspection                         | NEEDS VERIFICATION  |
| `V-FAUNA-API-007`   | Confirm review queue surface is steward-authenticated and not publicly addressable            | API app + auth middleware + authorization smoke test                                          | NEEDS VERIFICATION  |
| `V-FAUNA-API-008`   | Confirm rollback target binding on every Fauna `LayerManifest`                                | Released `LayerManifest` inspection + rollback drill receipts                                 | NEEDS VERIFICATION  |
| `V-FAUNA-API-009`   | Confirm citation-validation interception order (before render, not after)                     | Focus pipeline inspection + negative fixture pass                                             | NEEDS VERIFICATION  |
| `V-FAUNA-API-010`   | Confirm naming of `CorrectionNoticeCandidate` vs `CorrectionNotice` in current schemas        | `schemas/contracts/v1/correction/...`                                                         | UNKNOWN             |
| `V-FAUNA-API-011`   | Resolve `FaunaDecisionEnvelope` (§7.J) vs generic `DecisionEnvelope`/`RuntimeResponseEnvelope`; and `fauna/` vs `domains/fauna/` schema slug | Schema inspection + ADR (DTO-naming + slug) | CONFLICTED [§7.J] [§24.13] |

[↑ Back to top](#top)

---

## 15. Related Docs

- [`docs/domains/fauna/README.md`](./README.md) — Fauna lane overview *(TODO confirm)*
- [`docs/domains/fauna/SCHEMAS.md`](./SCHEMAS.md) — DTO field reference *(TODO)*
- [`docs/domains/fauna/POLICY.md`](./POLICY.md) — sensitivity & rights policy *(TODO)*
- [`docs/domains/fauna/adr/README.md`](./adr/README.md) — Fauna ADR index
- [`docs/runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md`](../../runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md) — source refresh runbook
- [`docs/architecture/governed-api.md`](../../architecture/governed-api.md) — generic governed API architecture *(TODO confirm path)*
- [`ai-build-operating-contract.md`](../../../ai-build-operating-contract.md) — operating law (`CONTRACT_VERSION = "3.0.0"`)
- [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md) — Directory Rules
- [`docs/adr/ADR-0001-schema-home.md`](../../adr/ADR-0001-schema-home.md) — schema home decision
- [`contracts/OBJECT_MAP.md`](../../../contracts/OBJECT_MAP.md) — object family ↔ schema ↔ policy crosswalk
- Project knowledge: **KFM Domains Culmination Atlas v1.1** §7 (Fauna), §7.J (API surfaces), §7.I (sensitivity), §7.K (validators), §20.3 (Master API Surface Table), §20.5 (deny-by-default register).

---

### Footer

**Truth posture:** CONFIRMED doctrine; **PROPOSED** implementation. Every route, DTO
field list, and HTTP code mapping in this document remains a design candidate until
verified against mounted-repo evidence and ratified by an ADR.
**Last updated:** 2026-05-29 ·
**Version:** v1 (draft) · `CONTRACT_VERSION = "3.0.0"` ·
[↑ Back to top](#top)

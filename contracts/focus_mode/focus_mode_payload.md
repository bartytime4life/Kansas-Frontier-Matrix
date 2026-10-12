<a id="top"></a>
# `contracts/focus_mode/focus_mode_payload.md`

<!-- KFM Meta Block v2 -->
> **Object family:** `FocusModePayload` · **Lane:** `contracts/focus_mode/` (semantic Markdown contract; **NOT** the machine schema — that lives at `schemas/contracts/v1/focus_mode/focus_mode_payload.schema.json`) · **Authority:** semantic source of truth for the plan → payload crosswalk · **Owners:** `<OWNER:contract-steward>`, `<OWNER:focus-mode-steward>` · **Last reviewed:** 2026-05-22

![authority](https://img.shields.io/badge/authority-semantic%20contract-blue)
![schema--home](https://img.shields.io/badge/schema--home-schemas%2Fcontracts%2Fv1%2Ffocus__mode%2F-blue)
![status](https://img.shields.io/badge/status-PROPOSED-yellow)
![cite--or--abstain](https://img.shields.io/badge/cite--or--abstain-MANDATORY-red)
![finite--outcome](https://img.shields.io/badge/finite--outcome-ANSWER%20%7C%20ABSTAIN%20%7C%20DENY%20%7C%20ERROR-orange)

> [!IMPORTANT]
> A county Focus Mode Build Plan, by itself, is **not** a governed UI payload. It is planning + acceptance documentation. This contract defines how the plan, the layer registry, the evidence model, and the sensitivity posture **become** a `FocusModePayload` instance — and what governance objects must be present at each step. **(CONFIRMED doctrine** — `kfm_unified_doctrine_synthesis.md` Part VI promotion gates; `Master_MapLibre_Components-Functions-Features_v2_1_FULL.md` §16.3 COUNTY-01 acceptance items.)

---

## Contents

- [1. Object family and trust posture](#1-object-family-and-trust-posture)
- [2. `FocusModePayload` semantic shape](#2-focusmodepayload-semantic-shape)
- [3. Plan → payload crosswalk (the core of this contract)](#3-plan--payload-crosswalk-the-core-of-this-contract)
- [4. Required companion objects](#4-required-companion-objects)
- [5. Finite outcome envelope](#5-finite-outcome-envelope)
- [6. Validation requirements](#6-validation-requirements)
- [7. Sensitivity and rights filtering](#7-sensitivity-and-rights-filtering)
- [8. Versioning and ADR triggers](#8-versioning-and-adr-triggers)
- [9. Anti-patterns](#9-anti-patterns)
- [10. Cross-references](#10-cross-references)

---

## 1. Object family and trust posture

**CONFIRMED doctrine.** `FocusModePayload` is a **governed projection** consumed by the public UI surface in `apps/explorer-web/src/focus-modes/<area>-county/`. It is a downstream carrier — a payload — not sovereign truth. `(kfm_unified_doctrine_synthesis.md` Part VI; `Master_MapLibre_Components-Functions-Features_v2_1_FULL.md` §1 sovereign-truth determination.)`

Trust posture:

- **Cite-or-abstain is mandatory.** Every claim surfaced through a `FocusModePayload` must resolve to an `EvidenceBundle` via an `EvidenceRef`, or the surface must `ABSTAIN`.
- **AI is interpretive, not sovereign.** When `FocusModePayload` is consumed by the AI Focus Mode panel, the answer must trace to `EvidenceBundle`s; generated language must not stand in for evidence (`ai-build-operating-contract.md` §10).
- **Defaults fail closed.** Sensitivity lanes default to `DENY` / `ABSTAIN` per `docs/focus-modes/README.md` §7; overrides require a deny-fixture.
- **Public clients never read RAW/WORK/QUARANTINE.** Payloads are served from `data/published/api_payloads/focus-modes/<area>.json` through the governed API (`apps/governed-api/`), not directly from canonical stores.
- **No payload without promotion.** A `FocusModePayload` reaching public clients must reference a `PromotionDecision` whose gates A–G have passed and a `MapReleaseManifest` whose `rollback target` is recorded.

[↑ Back to top](#top)

---

## 2. `FocusModePayload` semantic shape

**PROPOSED semantic shape.** The machine schema at `schemas/contracts/v1/focus_mode/focus_mode_payload.schema.json` is authoritative for field types and validation; this section is authoritative for **meaning**. If the two diverge, an ADR is required (`directory-rules.md` §2.4).

```text
FocusModePayload
├── payload_id                 // deterministic ID (JCS+SHA-256 of canonical content)
├── schema_version             // matches contract major version; bump via ADR
├── area                       // bound area for this payload
│   ├── county                 //   human-readable county name
│   ├── lane                   //   kebab-case area slug (e.g., "ellsworth-county")
│   ├── scope                  //   "county" | "region" | "corridor"
│   └── bounding_geometry_ref  //   reference to MapContextEnvelope bounds
├── plan_anchor                // back-pointer to docs/focus-modes/<lane>/build-plan.md
├── release
│   ├── release_manifest_id    // MapReleaseManifest the payload was promoted under
│   ├── promotion_decision_id  // PromotionDecision envelope ID (gates A–G outcome)
│   ├── rollback_target_id     // rollback target reference
│   └── correction_path        // how a correction is filed for this slice
├── layers[]                   // CONFIRMED: every entry MUST satisfy COUNTY-01 (c)
│   └── LayerRegistryEntry     //   (see contracts/focus_mode/layer_registry_entry.md)
├── claims[]                   // evidence-bearing claims from evidence-model.md
│   ├── claim_id
│   ├── evidence_ref           //   MUST resolve to EvidenceBundle, else ABSTAIN
│   ├── policy_decision_id     //   PolicyDecision for this claim
│   ├── sensitivity_tier       //   T0..T4 (per ADR-S-05 PROPOSED)
│   └── citation_validation_report_id  // pre-display pass/fail per cite-or-abstain
├── ai_context                 // governed context for the AI Focus Mode panel
│   ├── map_context_envelope   //   bounds, layers, time_window, selected_features
│   ├── evidence_closure_ids[] //   EvidenceBundle IDs in scope
│   ├── policy_context         //   active PolicyDecision references
│   └── permitted_templates[]  //   templates the AI may use; OUTSIDE templates → ERROR
├── public_safety_notes        // human-readable summary of what is NOT shown and why
├── trust_visible_state
│   ├── sensitivity_labels[]   //   per-layer/per-claim labels surfaced in Evidence Drawer
│   ├── source_attributions[]  //   visible attribution per source
│   └── stale_markers[]        //   stale/STALE badges when source cadence exceeded
└── audit
    ├── created_at
    ├── created_by             // build pipeline identity (not a human handle)
    ├── run_receipt_id         // RunReceipt for the payload build
    └── content_hashes         // payload contents addressable hashes
```

> [!NOTE]
> The `claims[]` and `layers[]` arrays do **not** carry geometry or attributes that would re-expose denied lanes. Geometry detail is served per-layer through the governed API after policy filtering; the payload references but does not embed those details.

[↑ Back to top](#top)

---

## 3. Plan → payload crosswalk (the core of this contract)

**PROPOSED.** This crosswalk is what turns a `docs/focus-modes/<area>-county/` lane into a `FocusModePayload`. Every required field has a source in one of the seven required lane files (§6.2 of `docs/focus-modes/README.md`).

| `FocusModePayload` field | Plan source (in lane) | Companion governance object | Validator(s) |
|---|---|---|---|
| `payload_id` | (computed) | — | JCS+SHA-256 computation |
| `schema_version` | front-matter `schema_version` | ADR-0001 | schema lint |
| `area.county`, `area.lane`, `area.scope` | front-matter `area.*` | — | C09, C10 (validate_focus_mode_index.py) |
| `area.bounding_geometry_ref` | `build-plan.md` §2 + `data/catalog/sources/<area>/source_descriptors.yaml` | `MapContextEnvelope` schema | `validate_map_context_envelope.py` (PROPOSED) |
| `plan_anchor` | (path back-pointer) | — | C12 link resolution |
| `release.release_manifest_id` | front-matter `release.release_manifest_id` | `MapReleaseManifest` | `validate_release_manifest.py` |
| `release.promotion_decision_id` | front-matter `release.promotion_gates_passed` | `PromotionDecision` | `validate_promotion_decision.py` |
| `release.rollback_target_id` | front-matter `release.rollback_target_id` | rollback target schema | `validate_rollback_target.py` |
| `release.correction_path` | front-matter `release.correction_path` | correction schema | `validate_correction.py` |
| `layers[]` | `layer-registry.md` | `LayerManifest`, `SourceDescriptor`, `PolicyDecision`, sensitivity label | `validate_layer_manifest.py` |
| `claims[]` | `evidence-model.md` | `EvidenceRef` → `EvidenceBundle`, `PolicyDecision`, `CitationValidationReport` | `validate_evidence_bundle.py`, `validate_citation_validation_report.py` |
| `ai_context.map_context_envelope` | front-matter `canonical_paths.ui_lane` + `build-plan.md` §2 | `MapContextEnvelope` | `validate_map_context_envelope.py` |
| `ai_context.evidence_closure_ids[]` | `evidence-model.md` (each claim's `EvidenceRef`) | `EvidenceBundle` closure | `validate_evidence_closure.py` |
| `ai_context.policy_context` | `layer-registry.md` PolicyDecision refs + `public-safety-notes.md` | `PolicyDecision` | `validate_policy_decision.py` |
| `ai_context.permitted_templates[]` | front-matter (PROPOSED — add `ai_permitted_templates[]`) | template registry | template-registry validator (PROPOSED) |
| `public_safety_notes` | `public-safety-notes.md` (full text or summary) | — | C11 acceptance items |
| `trust_visible_state.sensitivity_labels[]` | per-layer in `layer-registry.md` + per-claim in `evidence-model.md` | `PolicyDecision.outcome` projection | `validate_policy_decision.py` |
| `trust_visible_state.source_attributions[]` | `source-seed-list.md` + `data/catalog/sources/<area>/source_descriptors.yaml` | `SourceDescriptor` | `validate_source_descriptor.py` |
| `trust_visible_state.stale_markers[]` | (computed at build time) | source cadence in `SourceDescriptor` | freshness validator |
| `audit.run_receipt_id` | (computed at build time) | `RunReceipt` | `validate_run_receipt.py` |
| `audit.content_hashes` | (computed at build time) | — | JCS+SHA-256 |

**Crosswalk invariants:**

1. **A claim with no resolved `EvidenceRef` produces `ABSTAIN`, never silent omission.** Every entry in `evidence-model.md` either earns a `claim` in the payload with a resolved evidence ref, or the slice surfaces `ABSTAIN` for that claim with a reason code.
2. **A layer with no `PolicyDecision` produces `DENY`.** Every entry in `layer-registry.md` either earns a `layer` entry with a `PolicyDecision`, or the slice surfaces `DENY` for that layer.
3. **A `sensitivity_lanes` default of `DENY` or `ABSTAIN` is preserved in the payload unless an override (with deny-fixture) is recorded in front-matter `sensitivity_overrides[]`.**
4. **No `RAW/WORK/QUARANTINE` path can appear anywhere in the payload.** Validator check (PROPOSED `check_no_lifecycle_path_leak.py`).
5. **The payload references only objects whose families are in the `ai-build-operating-contract.md` §29 trust-bearing-surface list.** Anything else is a contract break.

[↑ Back to top](#top)

---

## 4. Required companion objects

**CONFIRMED object families** (per `ai-build-operating-contract.md` §29 and `Master_MapLibre_Components-Functions-Features_v2_1_FULL.md` §16.3):

| Object | Schema home (PROPOSED) | Role at payload time |
|---|---|---|
| `SourceDescriptor` | `schemas/contracts/v1/source/source_descriptor.schema.json` | Source identity + rights + cadence |
| `EvidenceBundle` (resolved from `EvidenceRef`) | `schemas/contracts/v1/evidence/evidence_bundle.schema.json` | What supports each claim |
| `LayerManifest` | `schemas/contracts/v1/data/layer_manifest.schema.json` | Per-layer renderer + style + tile refs |
| `PolicyDecision` | `schemas/contracts/v1/policy/policy_decision.schema.json` | ALLOW / DENY / ABSTAIN per claim or layer |
| `CitationValidationReport` | `schemas/contracts/v1/evidence/citation_validation_report.schema.json` | Cite-or-abstain pre-display gate |
| `MapContextEnvelope` | `schemas/contracts/v1/ui/map_context_envelope.schema.json` | Bounded map context delivered to AI |
| `AIReceipt` (when AI Focus Mode runs) | `schemas/contracts/v1/ai/ai_receipt.schema.json` | Audit trail for AI execution |
| `PromotionDecision` | `schemas/contracts/v1/release/promotion_decision.schema.json` | Gates A–G outcome |
| `MapReleaseManifest` | `schemas/contracts/v1/release/map_release_manifest.schema.json` | Released layer/style/tile set |
| `RunReceipt` | `schemas/contracts/v1/proofs/run_receipt.schema.json` | What ran to produce the payload |
| `rollback target` | `schemas/contracts/v1/release/rollback_target.schema.json` | Reversible release reference |

> [!CAUTION]
> The schema homes above are PROPOSED. Live-repo presence is **NEEDS VERIFICATION** at the next mounted-repo session. If a schema is absent in the live repo, the validator for that family will fail closed and no payload will be promoted.

[↑ Back to top](#top)

---

## 5. Finite outcome envelope

**CONFIRMED doctrine** — `ai-build-operating-contract.md` Part V; `Master_MapLibre_Components-Functions-Features_v2_1_FULL.md` §16.2 (RuntimeReceipt family).

Every interaction routed through `FocusModePayload` resolves to one of four outcomes:

| Outcome | When | Required carriers in the response envelope |
|---|---|---|
| `ANSWER` | Evidence closure complete, policy allows, citation validation passes | `evidence_used[]`, `citations[]`, `policy_decisions[]`, `ai_receipt_id` (when AI), `citation_validation_report_id` |
| `ABSTAIN` | Evidence insufficient, missing, or stale | `abstain_reason`, `evidence_gap[]`, `ai_receipt_id` (when AI) |
| `DENY` | Policy denies (rights, sensitivity, release state, sovereignty) | `deny_reason`, `policy_decisions[]` (the denying decisions), `ai_receipt_id` (when AI) |
| `ERROR` | System fault: schema invalid, governance object missing, lifecycle path leak | `error_code`, `error_detail` (no private chain-of-thought) |

A `FocusModePayload` instance **must** carry the response-envelope fields necessary to compute each outcome cleanly. **Generation that "feels like an answer" without these fields is a contract break.**

[↑ Back to top](#top)

---

## 6. Validation requirements

A `FocusModePayload` instance is accepted into the published lane only when **all** of the following pass:

1. JSON Schema validation against `schemas/contracts/v1/focus_mode/focus_mode_payload.schema.json`.
2. The lane that produced it passes `tools/validators/validate_focus_mode_index.py` (all 12 checks).
3. For every `claim`, `EvidenceRef` resolves to an `EvidenceBundle` (or the claim is `ABSTAIN`).
4. For every `layer`, a `PolicyDecision` exists with outcome `ALLOW` (or the layer is `DENY`).
5. For every claim and layer, a `sensitivity_tier` is set; defaults applied per `docs/focus-modes/README.md` §7 unless overridden with a deny-fixture.
6. `release.release_manifest_id`, `release.promotion_decision_id`, and `release.rollback_target_id` are all non-null and resolve.
7. The payload's `audit.content_hashes` match a freshly recomputed canonical content hash (JCS+SHA-256).
8. The payload contains no `RAW/WORK/QUARANTINE` path strings.
9. The payload contains no `apps/web/src/focus-modes/` reference (drift per OPEN-DR-06).
10. Negative fixtures in `fixtures/focus_modes/<area>-county/invalid/` cover every `DENY`, `ABSTAIN`, and `ERROR` reason code the payload can emit.

[↑ Back to top](#top)

---

## 7. Sensitivity and rights filtering

**CONFIRMED doctrine.** The `FocusModePayload` is the **last opportunity** to filter before public exposure. Specifically:

- Lanes defaulting to `DENY` (per `docs/focus-modes/README.md` §7) **must not** appear as `ALLOW`d claims or layers, even at coarse resolution, unless the lane's `policy/sensitivity/<area>/` override file justifies the change and a deny-fixture at `fixtures/focus_modes/<area>-county/invalid/` proves the override is enforced.
- Generalization is permitted (e.g., a rare-species observation generalized to HUC-12 watershed for `ANSWER`) only when (a) the generalization transform is recorded as a `RedactionReceipt`, and (b) the payload's `trust_visible_state.sensitivity_labels[]` discloses the generalization.
- `Source-rights` must be resolved per the `SourceDescriptor`'s rights posture for every layer. Sources with `rights_posture: unknown` ABSTAIN.
- For sovereign data (Indigenous data, tribal sites): defer to CARE principles. The payload **must not** assert anything that contradicts a sovereign data steward's recorded posture.

[↑ Back to top](#top)

---

## 8. Versioning and ADR triggers

- The `schema_version` field is **monotonic**.
- Adding optional fields → minor bump, no ADR required.
- Removing fields, changing types, renaming fields, changing outcome enum → **ADR required** (per `directory-rules.md` §2.4(3) and `ai-build-operating-contract.md` §28).
- Changing the plan → payload crosswalk in §3 → ADR required (this contract's authority).
- Changing the finite outcome envelope (§5) → ADR required.
- Changing companion object families (§4) → ADR required.

[↑ Back to top](#top)

---

## 9. Anti-patterns

**Refuse the following.** Each violates a CONFIRMED invariant:

- ❌ A `FocusModePayload` whose `claims[]` reference no `EvidenceBundle`.
- ❌ Embedding generated AI prose into `claims[].evidence_ref` as a substitute for source evidence.
- ❌ Serving a payload from `data/processed/` or `data/work/` instead of `data/published/api_payloads/focus-modes/<area>.json`.
- ❌ A "preview" payload that surfaces denied lanes "for review" outside `release/candidates/`.
- ❌ A payload referencing `apps/web/src/focus-modes/` (OPEN-DR-06 drift).
- ❌ A payload whose `audit.content_hashes` do not match recomputed hashes.
- ❌ Encoding sensitivity decisions as **style** (e.g., transparent fill) rather than `PolicyDecision`+`RedactionReceipt`. **Style-only hiding is not accepted** (`Master_MapLibre_Components-Functions-Features_v2_1_FULL.md` cover-table sensitive-geometry-deny fixture).
- ❌ Treating a `FocusModePayload` as proof of underlying claims. The payload is a **carrier**; the proof is the `EvidenceBundle` it cites.

[↑ Back to top](#top)

---

## 10. Cross-references

- `docs/focus-modes/README.md` — control plane lane doctrine
- `docs/focus-modes/COUNTY_INDEX.md` — master index
- `docs/focus-modes/_template/county-build-plan.md` — plan template with front-matter spec
- `tools/validators/validate_focus_mode_index.py` — validator
- `schemas/contracts/v1/focus_mode/focus_mode_payload.schema.json` — machine schema (PROPOSED; verify presence)
- `directory-rules.md` §6.3 (`contracts/` semantic home); §6.4 (`schemas/` machine home); §6.7 (Focus Modes placement contract)
- `kfm_unified_doctrine_synthesis.md` Part III (cite-or-abstain); Part V (finite outcome envelope); Part VI (promotion gates A–G)
- `ai-build-operating-contract.md` §10 (AI is interpretive); §26 (governed loop); §29 (object-family guardrails)
- `Master_MapLibre_Components-Functions-Features_v2_1_FULL.md` §16.3 COUNTY-01..04; map of MapContextEnvelope / FocusModeRequest / FocusModeResponse

[↑ Back to top](#top)

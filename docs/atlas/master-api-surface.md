<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/PATH_TBD_AFTER_REPO_INSPECTION
title: docs/atlas/master-api-surface.md — Deprecated Pointer
type: standard
version: v1
status: deprecated
owners: OWNER_TBD (docs steward; placement steward)
created: 2026-05-25
updated: 2026-05-25
policy_label: public
related:
  - docs/atlas/README.md
  - docs/atlases/master-api-surface.md
  - docs/atlases/KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.md
  - docs/atlases/KFM_Domains_Culmination_Atlas_v1_1.pdf
  - docs/architecture/KFM_Unified_Implementation_Architecture_Build_Manual.md
  - docs/adr/ADR-S-02-docs-dossiers-vs-docs-atlases.md
  - contracts/source/
  - contracts/evidence/
  - contracts/data/
  - contracts/runtime/
  - contracts/governance/
  - contracts/domains/
  - schemas/contracts/v1/
  - docs/doctrine/ai-build-operating-contract.md
  - docs/doctrine/directory-rules.md
tags: [kfm, docs, atlas, pointer, deprecated, master-api-surface, redirect, governed-api]
notes:
  - "This is a pointer page in a deprecated compatibility lane. It carries no register content."
  - "Canonical atlas-register home (PROPOSED): docs/atlases/master-api-surface.md (NEEDS VERIFICATION — file may not yet exist as a standalone extract)."
  - "Authoritative current source: Atlas v1.0 §20.3 retained verbatim in Atlas v1.1; also referenced by Atlas v1.1 §24.3."
  - "Authoritative API resource enumeration (route names): KFM Unified Implementation Architecture Build Manual §13."
  - "Per-API-family meaning contracts and schemas live under contracts/<family>/ and schemas/contracts/v1/<family>/."
  - "Sunset: this pointer file SHOULD be removed when docs/atlas/ is retired at the end of the 30-day mirror window."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `docs/atlas/master-api-surface.md` — Deprecated Pointer

> This file is a **deprecation pointer** in the [`docs/atlas/`](./README.md) compatibility lane. It carries no register content. Read the canonical sources listed below.

![status: DEPRECATED](https://img.shields.io/badge/status-DEPRECATED-red)
![authority: compatibility · pointer](https://img.shields.io/badge/authority-compatibility%20%C2%B7%20pointer-lightgrey)
![canonical lane: docs/atlases/](https://img.shields.io/badge/canonical%20lane-docs%2Fatlases%2F-blue)
![canonical target: PROPOSED](https://img.shields.io/badge/canonical%20target-PROPOSED-yellow)
![ADR: ADR-S-02](https://img.shields.io/badge/ADR-ADR--S--02-yellow)

> [!IMPORTANT]
> **Status:** `DEPRECATED` (doctrine-CONFIRMED per [`docs/atlas/README.md`](./README.md) §5–§6).
> **Owner:** `OWNER_TBD` — docs steward.
> **Sunset:** end of the 30-day `docs/atlas/` mirror window. This file SHOULD be removed when the parent folder is retired.
> **Truth posture:** `CONFIRMED` deprecation framing / `PROPOSED` canonical-target paths / `NEEDS VERIFICATION` mounted-repo presence of every target listed below / `UNKNOWN` repo implementation depth.

**Quick jumps:** [What this register is](#1-what-this-register-is-orientation-only) · [Where the canonical content lives](#2-where-the-canonical-content-lives) · [Per-API-family redirects](#3-per-api-family-redirects) · [Why this file is here as a pointer](#4-why-this-file-is-here-as-a-pointer) · [What this file does NOT contain](#5-what-this-file-does-not-contain) · [Verification checklist](#6-verification-checklist) · [Rollback / removal](#7-rollback--removal)

---

## 1. What this register is (orientation only)

`CONFIRMED doctrine — the Master API Surface Table enumerates every governed API family in KFM, the domains it serves, its DTO/schema, and the finite outcomes it returns.` (Atlas v1.0 §20.3, retained verbatim in v1.1; cross-referenced by v1.1 §24.3 "Master Decision Outcome Envelope Reference".)

`CONFIRMED doctrine — public clients and normal UI surfaces use governed interfaces; canonical/internal stores are not normal public paths.` (`directory-rules.md` v1.2 §2.1 invariants; `ai-build-operating-contract.md` §10 invariants.)

This register has **two structurally distinct companion artifacts** in the corpus, each with its own responsibility root:

| Companion artifact | Role | Responsibility root |
|---|---|---|
| **Master API Surface Table** *(atlas-register form)* | Cross-domain register: API family × domains × DTO/schema × outcomes. | `docs/atlases/` |
| **API resource families** *(architecture form)* | Concrete `/api/...` resource enumeration with route conventions, request/response shapes, and feature-click examples. | `docs/architecture/` *(KFM Unified Implementation Architecture Build Manual §13)* |
| **Per-API-family meaning contract** *(contract form)* | Object-family semantics for each DTO (`SourceDescriptor`, `EvidenceBundle`, `LayerManifest`, `RuntimeResponseEnvelope`, `ReviewRecord`, `PolicyDecision`, `DomainFeatureEnvelope`, `DecisionEnvelope`). | `contracts/<family>/` |
| **Per-API-family JSON Schema** *(shape form)* | Machine shape for each DTO. | `schemas/contracts/v1/<family>/` |
| **Per-domain J. table** *(domain-dossier form)* | Each domain chapter's own "J. API, contract, and schema surfaces" table (Atlas v1.1 chs. 3–18). | `docs/atlases/` *(within the consolidated atlas)* and/or `docs/domains/<domain>/` |

The pointer page does not duplicate any of the four companion artifacts; it only redirects.

> [!NOTE]
> "Master API Surface" is a doctrinal-register name from Atlas v1.0 §20.3. It is not a code package, a route prefix, an OpenAPI document, or a deployable artifact. The file at `contracts/api/` (if it exists) is the meaning-contract layer; the file at `schemas/contracts/v1/api/` (if it exists) is the shape layer; the route names live in the UIA Build Manual.

[↑ back to top](#top)

---

## 2. Where the canonical content lives

| If you want to read… | Go to | Responsibility root | Status |
|---|---|---|---|
| The **master cross-domain register** (API family × domains × DTO × outcomes) | `docs/atlases/master-api-surface.md` *(as a standalone register extract)* | `docs/` — atlas lane | `PROPOSED` — file `NEEDS VERIFICATION`; may not yet exist as a standalone extract |
| The **authoritative current source** for the master register | `docs/atlases/KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.md` § "20.3 Master API Surface Table" | `docs/` — atlas lane | `PROPOSED placement` per Atlas v1.1 Appendix G; mounted-repo presence `NEEDS VERIFICATION` |
| The **edition-of-record PDF** for the master register | `docs/atlases/KFM_Domains_Culmination_Atlas_v1_1.pdf` § Ch. 20.3 | `docs/` — atlas lane | `PROPOSED placement` per Atlas v1.1 Appendix G G.4; mounted-repo presence `NEEDS VERIFICATION` |
| The **concrete API resource enumeration** with route names and feature-click examples | `docs/architecture/KFM_Unified_Implementation_Architecture_Build_Manual.md` §13 | `docs/architecture/` | `CONFIRMED in corpus`; exact filename `NEEDS VERIFICATION` |
| The **per-domain J. tables** (one per domain, with domain-scoped DTOs and outcomes) | Atlas v1.1 chs. 3–18 §J in the consolidated atlas, and/or `docs/domains/<domain>/` per-dossier J. sections | `docs/` — atlas + domain dossiers | `PROPOSED placement`; mounted-repo presence `NEEDS VERIFICATION` |
| The **finite outcome vocabulary** returned by every API family | [`docs/atlas/decision-outcome-envelope.md`](./decision-outcome-envelope.md) *(redirects to canonical homes)* + Atlas v1.1 §24.3 | `docs/` — atlas lane | `CONFIRMED reference`; standalone extract `PROPOSED` |
| The **governed-AI binding** for runtime-class API families | `docs/doctrine/ai-build-operating-contract.md` §9.2 (Trust objects: `RuntimeResponseEnvelope`, `AIReceipt`) and §11 (directory and placement contract) | `docs/doctrine/` | `CONFIRMED in attached corpus` |
| The **directory placement rule** for governed APIs | `docs/doctrine/directory-rules.md` v1.2 §11 (browser-side renderer scope), §6 (root contracts) | `docs/doctrine/` | `CONFIRMED in attached corpus` |

> [!CAUTION]
> All relative paths above are `PROPOSED` from this file's location and have not been verified against a mounted repo. Treat them as redirect targets to confirm, not as proof that the target file exists today.

[↑ back to top](#top)

---

## 3. Per-API-family redirects

`CONFIRMED corpus content — Atlas v1.0 §20.3 enumerates six API families.` Each has its own DTO and its own canonical home for meaning and shape. The table below tells you where to find each family's canonical artifacts; it does not reproduce the §20.3 register itself.

| API family *(per Atlas v1.0 §20.3)* | DTO / schema *(per §20.3)* | Meaning-contract home *(PROPOSED)* | Schema home *(PROPOSED)* | Route reference *(corpus)* |
|---|---|---|---|---|
| Source summary resolver | `SourceDescriptor` projection | `contracts/source/source_descriptor.md` | `schemas/contracts/v1/source/source_descriptor.schema.json` | UIA Build Manual §13.2 *(`/api/catalog`, `/api/claims/{claim_id}`)* |
| Domain feature/detail lookup | `DomainFeatureEnvelope` + `DecisionEnvelope` | `contracts/domains/domain_feature_envelope.md` + `contracts/runtime/decision_envelope.md` | `schemas/contracts/v1/domains/domain_feature_envelope.schema.json` + `schemas/contracts/v1/runtime/decision_envelope.schema.json` | UIA Build Manual §13.2 *(`/api/map/resolve-feature`)* |
| Layer manifest resolver | `LayerManifest` / `GeoManifest` | `contracts/data/layer_manifest.md` *(or domain-MapLibre family)* | `schemas/contracts/v1/data/layer_manifest.schema.json` | UIA Build Manual §13.2 *(`/api/layers`)* |
| Evidence resolver | `EvidenceBundle` | `contracts/evidence/evidence_bundle.md` | `schemas/contracts/v1/evidence/evidence_bundle.schema.json` | UIA Build Manual §13.2 *(`/api/evidence/{bundle_id}`)* |
| Focus Mode runtime | `RuntimeResponseEnvelope` + `AIReceipt` | `contracts/runtime/runtime_response_envelope.md` + `contracts/runtime/ai_receipt.md` | `schemas/contracts/v1/runtime/runtime_response_envelope.schema.json` + `schemas/contracts/v1/runtime/ai_receipt.schema.json` | UIA Build Manual §13.2 *(`/api/focus/query`)* |
| Review queue surface | `ReviewRecord` + `PolicyDecision` | `contracts/governance/review_record.md` + `contracts/governance/policy_decision.md` | `schemas/contracts/v1/governance/review_record.schema.json` + `schemas/contracts/v1/governance/policy_decision.schema.json` | UIA Build Manual §13.2 *(`/api/review/*`)* |

> [!NOTE]
> **All filenames in this table are `PROPOSED`.** They are consistent with the existing `contracts/{source,evidence,data,runtime,release,correction,governance,domains}/` family structure and the `schemas/contracts/v1/...` schema-home convention from ADR-0001, but mounted-repo presence is `NEEDS VERIFICATION` for every row. Route names in the right column are `CONFIRMED in corpus` (UIA Build Manual §13.2) but their wiring to a live HTTP surface is `UNKNOWN`.

[↑ back to top](#top)

---

## 4. Why this file is here as a pointer

`CONFIRMED doctrine:`

1. `docs/atlas/` (singular) is a **deprecated compatibility mirror** during a 30-day sunset window. See [`docs/atlas/README.md`](./README.md).
2. The canonical doc-lane for atlas-class registers is `docs/atlases/` (plural), per `directory-rules.md` v1.2 §6.1 + §13.5 row "Docs naming duplication", per the *KFM Repository Structure Guiding Document* migration plan row `Docs naming`, and per Atlas v1.1 Appendix G G.4.
3. During the sunset window, `docs/atlas/` is permitted to carry **only** the deprecation README and conforming pointer pages — no atlas content, no master register, no contract, no schema, no API route reference. *(Per [`docs/atlas/README.md`](./README.md) §5–§6.)*
4. This file is a conforming pointer page. It carries the deprecation banner, the redirect tables, and no register content.

If you arrived here from a legacy backlink, the redirect tables in §2 and §3 list every canonical home you might be looking for. Update your backlink to one of those targets and stop linking into `docs/atlas/`.

[↑ back to top](#top)

---

## 5. What this file does NOT contain

`CONFIRMED — this pointer page intentionally OMITS:`

- The §20.3 register body (API family × domains × DTO/schema × outcomes).
- Concrete `/api/...` route enumerations or route-conventions text.
- Request/response payload examples (e.g., feature-click request, Evidence Drawer payload).
- DTO field shapes for `SourceDescriptor`, `EvidenceBundle`, `LayerManifest`, `RuntimeResponseEnvelope`, `AIReceipt`, `ReviewRecord`, `PolicyDecision`, `DomainFeatureEnvelope`, `DecisionEnvelope`, or any other API-family DTO.
- The outcome × surface mapping (that's [`docs/atlas/decision-outcome-envelope.md`](./decision-outcome-envelope.md)'s redirect target).
- Per-domain J. tables (those live in the consolidated atlas and the per-domain dossiers).
- Validator/test catalogue rows (that's Atlas v1.0 §20.4, a separate register).
- Authentication, authorization, rate-limit, versioning, or deprecation policy for any concrete API surface.
- OpenAPI/AsyncAPI documents or generated API reference pages.

> [!WARNING]
> If a future PR adds any of the above content to this file, the PR re-opens parallel-authority drift and should be refused at review. The substantive content belongs at the canonical homes listed in §2 and §3.

[↑ back to top](#top)

---

## 6. Verification checklist

- [ ] Confirm the canonical atlas-register file exists at `docs/atlases/master-api-surface.md` *(or)* confirm that Atlas v1.0 §20.3 inside `docs/atlases/KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.md` is the authoritative reference and that no standalone register extract is needed.
- [ ] Confirm `docs/architecture/KFM_Unified_Implementation_Architecture_Build_Manual.md` §13 is present and current; resolve any drift between Atlas §20.3 DTOs and Build Manual §13 route names.
- [ ] For each of the six API families in §3, confirm the meaning-contract path under `contracts/<family>/` exists or file a routine PR to author it.
- [ ] For each DTO in §3, confirm the schema path under `schemas/contracts/v1/<family>/` exists per ADR-0001 schema-home rule, or file a routine PR to author it.
- [ ] Confirm the outcome vocabulary returned by every API family in §3 is consistent with Atlas v1.1 §24.3 and `ai-build-operating-contract.md` §9.2.
- [ ] Confirm every internal repo backlink to `docs/atlas/master-api-surface.md` has been redirected to one of the canonical homes in §2 or §3.
- [ ] Confirm no substantive register content has been added to this file (see §5).

[↑ back to top](#top)

---

## 7. Rollback / removal

This file **should be removed**, not maintained, when the `docs/atlas/` mirror window closes. The doctrinally-correct end-state is:

- `docs/atlas/` no longer exists in the repo.
- Every backlink that previously pointed at `docs/atlas/master-api-surface.md` now points to one of the canonical homes in §2 or §3.
- The deprecation entry in `control_plane/deprecation_register.yaml` is closed.

`PROPOSED rollback path` (if removal causes link breakage that the redirect map did not catch): restore this exact pointer file from git history under the original `docs/atlas/master-api-surface.md` path, extend the mirror window in the deprecation register, and reopen the migration manifest for a second pass of backlink redirection.

**Rollback target:** `ROLLBACK_TARGET_TBD` — record the migration manifest `git_sha_before` here once known.

[↑ back to top](#top)

---

<details>
<summary><strong>Appendix A — Evidence basis (source ledger)</strong></summary>

| Source | Status | Supports | Limits |
|---|---|---|---|
| `docs/atlas/README.md` (prior turn, this session) | `CONFIRMED doctrine framing` | `docs/atlas/` is a deprecated mirror; only README and pointer pages permitted. | Doctrine framing only; mounted-repo state `NEEDS VERIFICATION`. |
| `directory-rules.md` v1.2 §6.1 + §13.5 row "Docs naming duplication" | `CONFIRMED doctrine` | Canonical lane is `docs/atlases/`. | Commit-pinned doctrine, not a `ls` of the working tree. |
| Atlas v1.0 §20.3 "Master API Surface Table" *(retained verbatim in v1.1, p.128)* | `CONFIRMED corpus content` | Six API families with DTO and outcome enumeration; PROPOSED implementation status throughout. | Atlas-level register; not a route specification or schema authority. |
| Atlas v1.1 §24.3 "Master Decision Outcome Envelope Reference" | `CONFIRMED corpus content` | Confirms §20.3 is the cross-domain consolidation point for finite outcomes. | Cross-references §20.3; does not replace it. |
| Atlas v1.1 Appendix G G.4 "Edition identity and citation form" | `CONFIRMED edition statement` | Canonical placement of the v1.1 PDF and (by inheritance) of any extracted register at `docs/atlases/`. | Atlas explicitly notes "Final repo placement … NEEDS VERIFICATION". |
| `KFM_Unified_Implementation_Architecture_Build_Manual.md` §13 "Proposed API resource families" | `CONFIRMED corpus content` | Concrete `/api/...` resource enumeration with route conventions and feature-click examples. | Architecture proposal; route names are `CONFIRMED in corpus` but wiring is `UNKNOWN`. |
| Per-domain J. tables in Atlas v1.1 chs. 3–18 | `CONFIRMED corpus pattern` | Each domain dossier carries a domain-scoped API/contract/schema table mirroring §20.3 at domain granularity. | Per-domain extension; not authoritative for cross-domain consolidation. |
| `ai-build-operating-contract.md` §9.2 Trust objects | `CONFIRMED doctrine` | `RuntimeResponseEnvelope` and `AIReceipt` as runtime DTOs. | Doctrine, not implementation depth. |

**Memory is not evidence.** No mounted repo, CI run, workflow, dashboard, or branch state was inspected for this pointer page. Every implementation claim above is bounded to doctrine.

</details>

[↑ back to top](#top)

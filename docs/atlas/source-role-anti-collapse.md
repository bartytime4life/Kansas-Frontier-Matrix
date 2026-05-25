<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/PATH_TBD_AFTER_REPO_INSPECTION
title: docs/atlas/source-role-anti-collapse.md — Deprecated Pointer
type: standard
version: v1
status: deprecated
owners: OWNER_TBD (docs steward; placement steward)
created: 2026-05-25
updated: 2026-05-25
policy_label: public
related:
  - docs/atlas/README.md
  - docs/atlases/source-role-anti-collapse.md
  - docs/atlases/KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.md
  - docs/atlases/KFM_Domains_Culmination_Atlas_v1_1.pdf
  - docs/adr/ADR-S-02-docs-dossiers-vs-docs-atlases.md
  - contracts/source/source_descriptor.md
  - schemas/contracts/v1/source/source_descriptor.schema.json
  - policy/source_role/
  - tests/policy/source_role/
  - tools/validators/
  - docs/doctrine/ai-build-operating-contract.md
  - docs/doctrine/directory-rules.md
tags: [kfm, docs, atlas, pointer, deprecated, source-role, anti-collapse, redirect, policy]
notes:
  - "This is a pointer page in a deprecated compatibility lane. It carries no register content."
  - "Canonical atlas-register home (PROPOSED): docs/atlases/source-role-anti-collapse.md (NEEDS VERIFICATION — file may not yet exist as a standalone extract)."
  - "Authoritative current source: Atlas v1.1 §24.1 — Master Source-Role Anti-Collapse Register."
  - "v1.0 cross-references: §20.4 validator catalogue row 'Source-role anti-collapse'; §23.3 figure-to-generate."
  - "Enforcement implementation lives across contracts/source/, schemas/contracts/v1/source/, policy/, tests/policy/, and tools/validators/."
  - "Sunset: this pointer file SHOULD be removed when docs/atlas/ is retired at the end of the 30-day mirror window."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `docs/atlas/source-role-anti-collapse.md` — Deprecated Pointer

> This file is a **deprecation pointer** in the [`docs/atlas/`](./README.md) compatibility lane. It carries no register content. Read the canonical sources listed below.

![status: DEPRECATED](https://img.shields.io/badge/status-DEPRECATED-red)
![authority: compatibility · pointer](https://img.shields.io/badge/authority-compatibility%20%C2%B7%20pointer-lightgrey)
![canonical lane: docs/atlases/](https://img.shields.io/badge/canonical%20lane-docs%2Fatlases%2F-blue)
![canonical target: PROPOSED](https://img.shields.io/badge/canonical%20target-PROPOSED-yellow)
![doctrine: Atlas v1.1 §24.1](https://img.shields.io/badge/doctrine-Atlas%20v1.1%20%C2%A724.1-success)
![ADR: ADR-S-02](https://img.shields.io/badge/ADR-ADR--S--02-yellow)

> [!IMPORTANT]
> **Status:** `DEPRECATED` (doctrine-CONFIRMED per [`docs/atlas/README.md`](./README.md) §5–§6).
> **Owner:** `OWNER_TBD` — docs steward.
> **Sunset:** end of the 30-day `docs/atlas/` mirror window. This file SHOULD be removed when the parent folder is retired.
> **Truth posture:** `CONFIRMED` deprecation framing / `CONFIRMED` doctrine of the underlying register / `PROPOSED` canonical-target paths / `NEEDS VERIFICATION` mounted-repo presence of every target / `UNKNOWN` repo implementation depth.

**Quick jumps:** [What this register is](#1-what-this-register-is-orientation-only) · [Where the canonical content lives](#2-where-the-canonical-content-lives) · [Per-enforcement-surface redirects](#3-per-enforcement-surface-redirects) · [Why this file is here as a pointer](#4-why-this-file-is-here-as-a-pointer) · [What this file does NOT contain](#5-what-this-file-does-not-contain) · [Verification checklist](#6-verification-checklist) · [Rollback / removal](#7-rollback--removal)

---

## 1. What this register is (orientation only)

`CONFIRMED doctrine — KFM treats source role as a first-class identity attribute. An observed reading is not interchangeable with a modeled estimate; a regulatory determination is not interchangeable with an administrative compilation; an aggregate publication is not interchangeable with candidate evidence; synthetic content is never the same thing as observed reality.` (Atlas v1.1 §24.1.)

`CONFIRMED doctrine — the lifecycle and the governed API both fail closed when these roles are conflated. The role is set at admission (SourceDescriptor) and is preserved through every promotion. Promotion does not upgrade an observation to a regulation, or a model to an aggregate, or a candidate to a verified record — those are separate governed transitions with their own evidence and review requirements.` (Atlas v1.1 §24.1, reading note.)

The register has **seven canonical role classes** *(named but not defined here — see §2 for the canonical definitions)*: `Observed`, `Regulatory`, `Modeled`, `Aggregate`, `Administrative`, `Candidate`, `Synthetic`.

It has **multiple companion artifacts** in distinct responsibility roots:

| Companion artifact | Role | Responsibility root |
|---|---|---|
| **Master Source-Role Anti-Collapse Register** *(atlas-register form)* | Cross-domain register: seven role classes, anti-collapse failure modes (DENY conditions), required guardrails. | `docs/atlases/` *(Atlas v1.1 §24.1)* |
| **Validator catalogue entry** | Test family "Source-role anti-collapse" — negative case: regulatory/model/aggregate/admin source used as different truth class; expected outcome: `DENY`. | `docs/atlases/` *(Atlas v1.0 §20.4)* + `tests/policy/` / `tools/validators/` for the implementation |
| **Trust-membrane anti-patterns** *(related register)* | §24.9.2 row "Aggregate cited as per-place observation" and adjacent rows. | `docs/atlases/` *(Atlas v1.1 §24.9.2)* |
| **`SourceDescriptor` meaning contract** | The object family carrying `source_role` as a fixed-at-admission field. | `contracts/source/` |
| **`SourceDescriptor` JSON Schema** | The field-level enum and validation of `source_role`. | `schemas/contracts/v1/source/` |
| **Policy implementation** | OPA / Rego policy enforcing DENY for role-collapse attempts at admission, promotion, render, and citation surfaces. | `policy/` (admission, promotion, render policy packages) |
| **Per-domain J. tables and F. cross-lane relations** | Each domain dossier (chs. 3–18) carries its own role-collapse risks and guardrails relevant to that domain. | `docs/atlases/` *(within the consolidated atlas)* and/or `docs/domains/<domain>/` |
| **Figure-to-generate** | Atlas v1.0 §23.3 "Source-role anti-collapse diagram" — the visual showing the seven roles as separate channels. | `docs/atlases/` *(referenced in Atlas v1.0 §23.3; rendering pipeline `NEEDS VERIFICATION`)* |

The pointer page does not duplicate any of these companion artifacts; it only redirects.

> [!NOTE]
> **The doctrine is not implementation.** Atlas v1.1 §24.1 establishes the register as doctrine. Whether each enforcement surface (contract, schema, policy, validator, test) currently implements that doctrine in the mounted repo is `NEEDS VERIFICATION` for every surface listed below.

[↑ back to top](#top)

---

## 2. Where the canonical content lives

| If you want to read… | Go to | Responsibility root | Status |
|---|---|---|---|
| The **master register** (seven role classes + DENY conditions + required guardrails) | `docs/atlases/source-role-anti-collapse.md` *(as a standalone register extract)* | `docs/` — atlas lane | `PROPOSED` — file `NEEDS VERIFICATION`; may not yet exist as a standalone extract |
| The **authoritative current source** | `docs/atlases/KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.md` § "24.1 Master Source-Role Anti-Collapse Register" | `docs/` — atlas lane | `PROPOSED placement` per Atlas v1.1 Appendix G; mounted-repo presence `NEEDS VERIFICATION` |
| The **edition-of-record PDF** | `docs/atlases/KFM_Domains_Culmination_Atlas_v1_1.pdf` § Ch. 24.1 | `docs/` — atlas lane | `PROPOSED placement` per Atlas v1.1 Appendix G G.4; mounted-repo presence `NEEDS VERIFICATION` |
| The **validator-catalogue row** (test family, negative case, expected outcome) | Atlas v1.0 §20.4 "Source-role anti-collapse" *(retained verbatim in v1.1)* | `docs/` — atlas lane | `CONFIRMED corpus content`; placement of the extracted §20.4 catalogue `NEEDS VERIFICATION` |
| The **trust-membrane anti-patterns context** | Atlas v1.1 §24.9.2 | `docs/` — atlas lane | `CONFIRMED corpus content` |
| The **figure** ("observed / regulatory / modeled / aggregate / administrative / candidate / synthetic as separate channels") | Atlas v1.0 §23.3 figure-to-generate | `docs/` — atlas lane | `CONFIRMED corpus reference`; rendering target path `NEEDS VERIFICATION` |
| The **`SourceDescriptor` meaning contract** (with `source_role` field) | `contracts/source/source_descriptor.md` | `contracts/` — meaning | `PROPOSED`; `NEEDS VERIFICATION` |
| The **`SourceDescriptor` JSON Schema** (with `source_role` enum) | `schemas/contracts/v1/source/source_descriptor.schema.json` | `schemas/` — shape | `PROPOSED` per ADR-0001 schema-home; `NEEDS VERIFICATION` |
| The **policy implementation** (OPA / Rego) | `policy/source_role/` *(or `policy/admission/source_role.rego`, `policy/promotion/source_role.rego`, `policy/render/source_role.rego`)* | `policy/` — admissibility | `PROPOSED`; exact package layout `NEEDS VERIFICATION` |
| The **policy tests** (negative-fixture conformance) | `tests/policy/source_role/` | `tests/` | `PROPOSED`; `NEEDS VERIFICATION` |
| The **fixtures** (positive / negative role-collapse fixtures) | `fixtures/source_role/{valid,invalid}/` | `fixtures/` | `PROPOSED` per `directory-rules.md` v1.2 §6.6 fixture substructure; `NEEDS VERIFICATION` |
| The **doctrinal anchor** for source-role discipline in governed AI | `docs/doctrine/ai-build-operating-contract.md` §10 (core invariants) + §11 (placement contract) | `docs/doctrine/` | `CONFIRMED in attached corpus` |
| The **per-domain J. and F. sections** (where domain-specific role-collapse risks live) | Atlas v1.1 chs. 3–18 in the consolidated atlas; and/or `docs/domains/<domain>/` | `docs/` — atlas + domain dossiers | `PROPOSED placement`; mounted-repo presence `NEEDS VERIFICATION` |

> [!CAUTION]
> All relative paths above are `PROPOSED` from this file's location and have not been verified against a mounted repo. Treat them as redirect targets to confirm, not as proof that the target file exists today.

[↑ back to top](#top)

---

## 3. Per-enforcement-surface redirects

`CONFIRMED corpus content — the register's enforcement spans admission, promotion, render, citation, and AI runtime surfaces.` Each surface has its own canonical home for the enforcing artifact. The table below tells you where each enforcement surface lives; it does not reproduce the §24.1 DENY-condition table itself.

| Enforcement surface | What it does *(per Atlas v1.1 §24.1.2 + §24.9.2)* | Canonical home for the enforcing artifact *(PROPOSED)* | Outcome on collapse *(per corpus)* |
|---|---|---|---|
| **Admission** | `SourceDescriptor.source_role` is set at admission and immutable through promotion. | `contracts/source/source_descriptor.md` + `schemas/contracts/v1/source/source_descriptor.schema.json` + `policy/admission/source_role.rego` | Admission `DENY` if role cannot be determined or is ambiguous. |
| **Promotion** | Promotion never upgrades a role (e.g., modeled → observed, candidate → verified). | `policy/promotion/source_role.rego` + `tests/policy/source_role/promotion_test.rego` | Promotion `DENY` if proposed transition implies a role upgrade. |
| **Publication (release queue)** | Modeled product MAY not be published with observed framing; aggregate MAY not be published as per-place truth; synthetic MAY not be published without a Reality Boundary Note. | `policy/release/source_role.rego` *(or `policy/promotion/source_role.rego`)* + `release/` review gates | Release `DENY` / `HOLD`. |
| **Render (map / UI)** | Map layers and Evidence Drawer payloads MUST preserve role labeling. | `policy/render/source_role.rego` + MapLibre layer registry guards | Render `DENY` for collapsed presentation. |
| **Citation (AI / Focus Mode)** | AI surfaces MUST `ABSTAIN` when a query would force role collapse; MUST `DENY` when policy would emit a collapse. | `policy/render/source_role.rego` + AIReceipt evaluator + Focus Mode citation evaluator | `ABSTAIN` or `DENY`. |
| **Validator harness** | Test family "Source-role anti-collapse" — negative case: regulatory/model/aggregate/admin source used as different truth class. | `tools/validators/source_role/` + `tests/policy/source_role/` | Validator outcome `DENY` (per Atlas v1.0 §20.4). |
| **Sensitive-domain interlock** | Sensitive domains *(archaeology, fauna/flora, people/land, hazards, infrastructure)* default to `DENY` on collapse; redaction/generalization receipt required. | `policy/sensitivity/` + domain dossier J. tables | `DENY`; `RedactionReceipt` required if any release proceeds. |

> [!NOTE]
> **All policy and validator paths in this table are `PROPOSED`.** They are consistent with the existing `policy/{admission,promotion,release,render,sensitivity,consent}/` family structure and the `tools/validators/` flat-prefix naming convention from the *KFM Repository Structure Guiding Document*, but mounted-repo presence is `NEEDS VERIFICATION` for every row. The outcome vocabulary (`DENY` / `ABSTAIN` / `HOLD`) is `CONFIRMED` per Atlas v1.1 §24.3 and `ai-build-operating-contract.md` §9.2.

### 3.1 Most-at-risk domains (for navigation only)

`CONFIRMED corpus content — Atlas v1.1 §24.1.2 names six domain families as most at risk for specific role-collapse patterns.` Navigate to the matching domain dossier for the per-domain detail:

| Collapse pattern *(per §24.1.2)* | Most-at-risk domains *(per §24.1.2)* | Where the per-domain detail lives |
|---|---|---|
| Modeled product labeled or queried as observed | Air; Hydrology; Habitat; Agriculture; 3D | `docs/atlases/` chs. 4, 6, 9, 11, 18 (consolidated atlas) + per-domain dossiers |
| Regulatory zone labeled as an observed flood / event | Hydrology; Hazards; Air | `docs/atlases/` chs. 4, 11, 12 + per-domain dossiers |
| Aggregate cited as a per-place truth | Agriculture; People; Geology; Air | `docs/atlases/` chs. 9, 10, 11, 16 + per-domain dossiers |
| Administrative compilation cited as observation | People/Land; Settlements; Roads | `docs/atlases/` chs. 13, 14, 16 + per-domain dossiers |
| *(others — see §24.1.2 in the consolidated atlas)* | — | — |

> The chapter numbers above are from the v1.1 / v1.0 interior; mounted-repo file placement is `PROPOSED` per Atlas v1.1 Appendix G.

[↑ back to top](#top)

---

## 4. Why this file is here as a pointer

`CONFIRMED doctrine:`

1. `docs/atlas/` (singular) is a **deprecated compatibility mirror** during a 30-day sunset window. See [`docs/atlas/README.md`](./README.md).
2. The canonical doc-lane for atlas-class registers is `docs/atlases/` (plural), per `directory-rules.md` v1.2 §6.1 + §13.5 row "Docs naming duplication", per the *KFM Repository Structure Guiding Document* migration plan row `Docs naming`, and per Atlas v1.1 Appendix G G.4.
3. During the sunset window, `docs/atlas/` is permitted to carry **only** the deprecation README and conforming pointer pages — no atlas content, no master register, no contract, no schema, no policy file, no validator catalogue. *(Per [`docs/atlas/README.md`](./README.md) §5–§6.)*
4. This file is a conforming pointer page. It carries the deprecation banner, the redirect tables, and no register content.

If you arrived here from a legacy backlink, the redirect tables in §2 and §3 list every canonical home you might be looking for. Update your backlink to one of those targets and stop linking into `docs/atlas/`.

[↑ back to top](#top)

---

## 5. What this file does NOT contain

`CONFIRMED — this pointer page intentionally OMITS:`

- The definition or scope of any of the seven role classes (`Observed`, `Regulatory`, `Modeled`, `Aggregate`, `Administrative`, `Candidate`, `Synthetic`).
- The "typical example" enumeration per role.
- The "allowed downstream role" matrix.
- The anti-collapse failure-mode table (DENY conditions, required guardrails).
- The role-immutability rule's worked examples.
- The Reality Boundary Note specification for synthetic content.
- The Representation Receipt specification.
- The `SourceDescriptor.source_role` JSON Schema enum.
- Rego policy text, validator code, fixture content, or test cases.
- The figure-to-generate ("seven roles as separate channels").
- Per-domain J. table content.

> [!WARNING]
> If a future PR adds any of the above content to this file, the PR re-opens parallel-authority drift and should be refused at review. The substantive content belongs at the canonical homes listed in §2 and §3.

[↑ back to top](#top)

---

## 6. Verification checklist

- [ ] Confirm the canonical atlas-register file exists at `docs/atlases/source-role-anti-collapse.md` *(or)* confirm that Atlas v1.1 §24.1 inside `docs/atlases/KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.md` is the authoritative reference and that no standalone register extract is needed.
- [ ] Confirm `contracts/source/source_descriptor.md` exists and declares the `source_role` field as fixed-at-admission and immutable through promotion.
- [ ] Confirm `schemas/contracts/v1/source/source_descriptor.schema.json` exists per ADR-0001 schema-home rule and constrains `source_role` to the seven canonical role classes.
- [ ] Confirm a policy package exists under `policy/` enforcing role immutability at admission, promotion, release, and render gates (exact package layout per ADR if subdivision is contested).
- [ ] Confirm `tests/policy/source_role/` contains negative-case tests for each DENY condition in Atlas v1.1 §24.1.2.
- [ ] Confirm `fixtures/source_role/{valid,invalid}/` exists with role-collapse negative fixtures per `directory-rules.md` v1.2 §6.6 fixture substructure.
- [ ] Confirm the validator catalogue entry "Source-role anti-collapse" from Atlas v1.0 §20.4 is wired to a validator under `tools/validators/`.
- [ ] Confirm every internal repo backlink to `docs/atlas/source-role-anti-collapse.md` has been redirected to one of the canonical homes in §2 or §3.
- [ ] Confirm no substantive register content has been added to this file (see §5).

[↑ back to top](#top)

---

## 7. Rollback / removal

This file **should be removed**, not maintained, when the `docs/atlas/` mirror window closes. The doctrinally-correct end-state is:

- `docs/atlas/` no longer exists in the repo.
- Every backlink that previously pointed at `docs/atlas/source-role-anti-collapse.md` now points to one of the canonical homes in §2 or §3.
- The deprecation entry in `control_plane/deprecation_register.yaml` is closed.

`PROPOSED rollback path` (if removal causes link breakage that the redirect map did not catch): restore this exact pointer file from git history under the original `docs/atlas/source-role-anti-collapse.md` path, extend the mirror window in the deprecation register, and reopen the migration manifest for a second pass of backlink redirection.

**Rollback target:** `ROLLBACK_TARGET_TBD` — record the migration manifest `git_sha_before` here once known.

[↑ back to top](#top)

---

<details>
<summary><strong>Appendix A — Evidence basis (source ledger)</strong></summary>

| Source | Status | Supports | Limits |
|---|---|---|---|
| `docs/atlas/README.md` (prior turn, this session) | `CONFIRMED doctrine framing` | `docs/atlas/` is a deprecated mirror; only README and pointer pages permitted. | Doctrine framing only; mounted-repo state `NEEDS VERIFICATION`. |
| `directory-rules.md` v1.2 §6.1 + §13.5 row "Docs naming duplication" | `CONFIRMED doctrine` | Canonical lane is `docs/atlases/`. | Commit-pinned doctrine, not a `ls` of the working tree. |
| Atlas v1.1 §24.1 "Master Source-Role Anti-Collapse Register" | `CONFIRMED corpus content` | Seven canonical role classes; immutability at admission rule; six collapse-failure modes with DENY conditions and required guardrails; most-at-risk domain map. | Atlas-level register; not a policy or schema authority. |
| Atlas v1.0 §20.4 "Master Validator / Test Catalogue" row "Source-role anti-collapse" | `CONFIRMED corpus content` | Validator test family with named negative case (regulatory/model/aggregate/admin used as different truth class) and expected outcome (`DENY`). | Validator-catalogue row; not a validator implementation. |
| Atlas v1.0 §23.3 "Source-role anti-collapse diagram" (figure-to-generate) | `CONFIRMED corpus reference` | The seven roles modeled as separate channels in the canonical figure. | Reference to a figure-to-generate; rendering target path `NEEDS VERIFICATION`. |
| Atlas v1.1 §24.9.2 row "Aggregate cited as per-place observation" | `CONFIRMED corpus content` | Trust-membrane anti-pattern view of role collapse with DENY surfaces. | Anti-pattern register; not enforcement authority. |
| Atlas v1.1 §24.9.3 "Promotion that 'upgrades' a source role" counter-rule | `CONFIRMED corpus content` | Source role is fixed at admission; never upgraded by promotion. | Governance-process counter-rule; not implementation. |
| Atlas v1.1 Appendix G G.4 "Edition identity and citation form" | `CONFIRMED edition statement` | Canonical placement of the v1.1 PDF and (by inheritance) of any extracted register at `docs/atlases/`. | Atlas explicitly notes "Final repo placement … NEEDS VERIFICATION". |
| Atlas seed cards — FEATURE "Source-Role Anti-Collapse Register Capability" (`kfm_full_atlas_seed_cards.md`) | `PROPOSED implementation` / `CONFIRMED card content` | Categorizes the capability under `POL - Policy, OPA, Conftest, Decisions`; lists the seven collapse patterns by name. | Seed card; not implementation proof. |
| `ai-build-operating-contract.md` §10 core invariants + §11 placement contract | `CONFIRMED doctrine` | Source identity is preserved deterministically where practical; placement rule routes policy to `policy/`, contract to `contracts/`, schema to `schemas/`. | Doctrine, not implementation depth. |
| *KFM Repository Structure Guiding Document* — `policy/` and `contracts/` root contracts | `CONFIRMED doctrine` | Family structure under `contracts/{source,evidence,data,runtime,release,correction,governance,domains}/`; policy package family. | Doctrine, not implementation depth. |

**Memory is not evidence.** No mounted repo, CI run, workflow, dashboard, or branch state was inspected for this pointer page. Every implementation claim above is bounded to doctrine.

</details>

[↑ back to top](#top)

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/adr-0028-state-scale-focus-mode-scope  # NEEDS_VERIFICATION until registered
title: "ADR-0028 — State-scale Focus Mode scope (-state) and 13-domain coverage rule"
type: adr
adr_id: ADR-0028
version: v0.1
status: proposed
decision_date: 2026-05-23
owners:
  - <OWNER:focus-mode-steward>
  - <OWNER:directory-rules-steward>
  - <OWNER:schema-steward>
  - <OWNER:sensitivity-reviewer>
created: 2026-05-23
updated: 2026-05-23
policy_label: public
authority: amends directory-rules.md §6.7 (adds -state to allowed scope-suffix enumeration); establishes the 13-domain coverage rule for every Focus Mode at every scale
supersedes: none
superseded_by: none
related_adrs:
  - docs/adr/ADR-0001-schema-home.md                                      # CONFIRMED doctrine reference; PROPOSED file path
  - docs/adr/ADR-0003-policy-singular-is-canonical.md                     # PROPOSED file path
  - docs/adr/ADR-0027-county-focus-mode-control-plane.md                  # PROPOSED — county control plane (this ADR extends scope)
  - docs/adr/ADR-S-05-sensitivity-tier-scheme.md                          # PROPOSED — referenced for sensitivity tiers (T0–T4)
related:
  - docs/standards/directory-rules.md                                     # §6.7 placement contract; §2.4 ADR triggers
  - docs/focus-modes/README.md                                            # v0.3 (design spec this ADR evaluates)
  - docs/focus-modes/COUNTY_INDEX.md
  - docs/focus-modes/STATE_INDEX.md                                       # PROPOSED — single-area state-scale index
  - docs/focus-modes/_template/county-build-plan.md
  - docs/focus-modes/_template/state-build-plan.md                        # PROPOSED — emit on acceptance
  - docs/focus-modes/kansas-state/                                        # PROPOSED — emit on acceptance
  - contracts/focus_mode/focus_mode_payload.md
  - schemas/contracts/v1/focus_mode/focus_mode_payload.schema.json        # PROPOSED amendment: add scale_class + domain_coverage
  - schemas/contracts/v1/focus_mode/layer_registry_entry.schema.json      # PROPOSED amendment: add domain enum + scale_class
  - tools/validators/validate_focus_mode_index.py                         # PROPOSED amendment: recognize -state scope
  - tools/validators/validate_focus_mode_payload.py                       # PROPOSED — accept all four scale values
  - KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.md             # CONFIRMED — 13-domain enumeration (Appendix C)
  - kfm_unified_doctrine_synthesis.md                                     # CONFIRMED — cite-or-abstain; trust path
  - Master_MapLibre_Components-Functions-Features_v2_1_FULL.md            # CONFIRMED — COUNTY-01..04; Appendix C county family
  - ai-build-operating-contract.md                                        # CONFIRMED — §28 ADR triggers; §10 AI is interpretive
  - docs/registers/DRIFT_REGISTER.md                                      # NEEDS_VERIFICATION — open items closed by this ADR
tags:
  - kfm
  - adr
  - focus-mode
  - state-scale
  - county-scale
  - scope-suffix
  - domain-coverage
  - directory-rules
  - placement-contract
  - cite-or-abstain
  - governed-ai
  - trust-membrane
trigger_clause: "directory-rules.md §6.7 scope-suffix enumeration; docs/focus-modes/README.md §20 ADR trigger ('Adding a new scope suffix beyond -county, -region, -corridor'); §20 trigger ('Changing the YAML front-matter spec in a way that invalidates existing plans')"
closes_open_items:
  - OPEN-FM-09   # -state scope addition to directory-rules.md §6.7.2
  - OPEN-FM-10   # 13-domain coverage rule (every Focus Mode addresses every domain)
  - OPEN-FM-14   # state-scale release-candidate folder naming
opens_open_items:
  - OPEN-FM-15   # PROPOSED — cross-scale crosswalk artifact (state ↔ county evidence linkage; optional, non-blocking)
  - OPEN-FM-16   # PROPOSED — sensitivity-overrides at state scale (review whether any are justified at v0.3 launch)
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0028 — State-scale Focus Mode scope (`-state`) and 13-domain coverage rule

> **Decision summary (PROPOSED).** Amend `directory-rules.md` §6.7 to add `-state` as a fourth allowed Focus Mode scope suffix; establish `kansas-state` as the single canonical state-scale Focus Mode area; adopt the 13-domain coverage rule (every Focus Mode at every scale addresses every domain — either populated or abstain-on-record). This ADR amends doctrine, schemas, templates, and validators in coordinated v0.3 increments and does **not** authorize a state-scale composition derived from county roll-up.

![status](https://img.shields.io/badge/status-proposed-yellow)
![class](https://img.shields.io/badge/class-architecture%20decision-blue)
![authority](https://img.shields.io/badge/amends-directory--rules.md%20%C2%A76.7-blue)
![scope](https://img.shields.io/badge/scope-state%20%2B%2013--domain%20coverage-2b8a3e)
![supersession](https://img.shields.io/badge/supersedes-none-lightgrey)
![superseded%20by](https://img.shields.io/badge/superseded%20by-none-lightgrey)
![review%20burden](https://img.shields.io/badge/reviewers-focus--mode%20%2B%20directory--rules%20%2B%20schema%20%2B%20sensitivity-6f42c1)
![rollback](https://img.shields.io/badge/rollback-pre--v0.3%20directory--rules-informational)
![truth%20posture](https://img.shields.io/badge/truth-cite--or--abstain-0b7285)
![repo%20evidence](https://img.shields.io/badge/repo%20evidence-not%20mounted-lightgrey)
![effective](https://img.shields.io/badge/effective%20on-acceptance-orange)

**Status:** `proposed` · **Decision date:** 2026-05-23 · **Effective on:** acceptance · **Owners:** `<OWNER:focus-mode-steward>`, `<OWNER:directory-rules-steward>`, `<OWNER:schema-steward>`, `<OWNER:sensitivity-reviewer>` · **Last reviewed:** 2026-05-23

> [!IMPORTANT]
> **Authority and reconciliation.** This ADR proposes an amendment to `directory-rules.md` §6.7. Until status advances from `proposed` to `accepted` per the §7 acceptance criteria below, no `kansas-state/` lane may merge, the `directory-rules.md` text is unchanged, and the v0.3 design spec in `docs/focus-modes/README.md` remains explicitly **PROPOSED**. On acceptance, this ADR becomes part of the authority order (`directory-rules.md` §2.1 step 2: "Accepted ADRs that explicitly amend Directory Rules") and the §6.7 text MUST be amended in the same PR or its immediate follow-up.

> [!CAUTION]
> **Coupled decisions.** This ADR makes three decisions that are technically separable but operationally coupled (a state-scale composition without the coverage rule produces an umbrella that silently omits domains; the coverage rule without a state-scale composition leaves Kansas-wide questions unanswerable). Reviewers should approve or reject the ADR as a unit. See §5 for the alternative considered (split into two ADRs) and why it was rejected.

---

## Contents

- [1. Status](#1-status)
- [2. Context](#2-context)
- [3. Decision](#3-decision)
- [4. Consequences](#4-consequences)
- [5. Alternatives considered](#5-alternatives-considered)
- [6. Migration plan](#6-migration-plan)
- [7. Acceptance criteria](#7-acceptance-criteria)
- [8. Rollback plan](#8-rollback-plan)
- [9. Related ADRs and references](#9-related-adrs-and-references)
- [10. Open items not resolved by this ADR](#10-open-items-not-resolved-by-this-adr)
- [11. Notes and appendix](#11-notes-and-appendix)
- [12. ADR self-check](#12-adr-self-check)

---

## 1. Status

| Field | Value |
|---|---|
| ADR ID | ADR-0028 |
| Title | State-scale Focus Mode scope (`-state`) and 13-domain coverage rule |
| Status | `proposed` |
| Date | 2026-05-23 |
| Supersedes | none |
| Superseded by | none |
| Trigger clause | `directory-rules.md` §6.7 scope-suffix enumeration; `docs/focus-modes/README.md` v0.3 §20 ADR trigger ("Adding a new scope suffix beyond `-county`, `-region`, `-corridor`"); §20 trigger ("Changing the YAML front-matter spec in a way that invalidates existing plans") |
| Effective on | Acceptance (see §7) |

Status semantics follow `directory-rules.md` §2.4 enumeration: `proposed | accepted | superseded | rejected`.

[↑ Back to top](#top)

---

## 2. Context

### 2.1 The gap this ADR addresses

**CONFIRMED corpus state.** `directory-rules.md` §6.7.1 currently defines a Focus Mode as a "**county- or region-scale** proof slice" and §6.7.2 enumerates three allowed scope suffixes: `-county`, `-region`, `-corridor`. **There is no state-scale Focus Mode in the canonical scope-suffix enumeration today.**

**PROPOSED gap analysis.** With 105 counties and no statewide composition, three problems compound:

1. **No umbrella view.** The map frame most users open at first (the whole state) has no `MapReleaseManifest` whose extent is Kansas. Every public claim that should be statewide must either (a) be reconstructed in 105 county lanes, (b) be hidden in a cross-cutting layer with no Focus Mode home, or (c) be uncited. None of these is consistent with cite-or-abstain.
2. **Statewide-native sources have no canonical home.** Several KFM source-seed families are inherently statewide before they are county-bounded — `KFM_Domains_v1_1` lists USGS NHD at HUC-4, KGS statewide bedrock, KDHE statewide AQ network (AirNow + AQS + KDHE bulletins), KS DASC statewide layers, KDOT statewide network, NRCS gNATSGO, statewide NFHL. Under the county-only scope, these sources are placed in `data/catalog/sources/<domain>/` by domain but have no Focus Mode where they assemble into a citable claim at the statewide frame.
3. **Domain coverage is non-uniform.** Reviewing the 17+ in-flight county build plans, every county is bottom-up-driven by its distinctive history (Ellsworth's post-rock sandstone, Riley's Konza Prairie, Sedgwick's aviation). This is correct authorship discipline, but it leaves cross-county domain coverage uneven by construction — atmosphere, statewide hazards, and Frontier Matrix object families are unevenly addressed and sometimes silently omitted.

### 2.2 What "scale" means in KFM

**CONFIRMED doctrine.** A Focus Mode is the **cross-cutting compositional unit** that demonstrates the full trust path `SourceDescriptor → SourceIntakeRecord → EvidenceRef → EvidenceBundle → Claim/AtlasCard → DecisionEnvelope → ReleaseManifest → Public UI` for a **bounded spatial frame**. Scope suffixes (`-county`, `-region`, `-corridor`) name what kind of bound applies. **The state of Kansas is a valid spatial bound** — but the current enumeration has no syntactic place for it.

**PROPOSED framing.** Scale is a property of the *spatial bound*, not of the *evidence chain*. The trust path is identical at every scale; what differs is:

- the **extent** of the bound (Kansas vs Ellsworth County);
- the **resolution / generalization** of admissible evidence (HUC-4 vs HUC-12; statewide road network vs county-intersecting segments);
- the **cadence** at which `ReleaseManifest`s are issued (statewide datasets refresh on annual/quarterly cycles; county-bounded slices can move faster);
- the **sensitivity posture** along certain lanes (aggregation defeats some re-identification risks at state scale; archaeology / rare species / living-person / DNA / critical-infrastructure remain deny-default at both scales).

State scale is not a different kind of Focus Mode; it is the same kind at a different bound.

### 2.3 Why this is ADR-class

**CONFIRMED triggers.** Per `directory-rules.md` §2.4 and the `docs/focus-modes/README.md` v0.3 §20:

- §2.4 lists the canonical ADR triggers. **None of items §2.4(1)–(6) is named directly** by this change (no canonical root added/removed/renamed; no schema-home change; no lifecycle phase split or merge; no parallel home; no §3 invariant bent).
- **However**, §6.7 IS part of `directory-rules.md`, and changing its scope-suffix enumeration changes the placement contract that §6.7.2 makes binding. The `docs/focus-modes/README.md` v0.3 §20 (which restates §6.7) explicitly identifies "Adding a new scope suffix beyond `-county`, `-region`, `-corridor`" as an ADR trigger, and the README's reconciliation invariant ("`directory-rules.md` wins") only holds if the README cannot unilaterally extend the enumeration without an ADR.
- The change is therefore ADR-class **by the spirit of §2.4(5)** ("Creating a parallel home for any of: schemas, contracts, policy, sources, registries, releases, proofs, receipts") — extending the scope-suffix enumeration creates a new placement *target* under existing canonical roots, and the placement contract requires explicit governance.
- The change is **also** ADR-class because it amends the YAML front-matter spec in `_template/county-build-plan.md` and the schema `focus_mode_payload.schema.json` in a way that invalidates existing draft plans (which lack a `scale_class` field). This breaks no released payloads (none exist), but it does break the validator's acceptance of pre-amendment drafts unless `scale_class` is back-filled.

### 2.4 Doctrine cited

- `directory-rules.md` §3 (root-stays-boring), §6.7 (Focus Mode placement contract), §2.1 (authority order), §2.4 (ADR triggers), §12 (Domain Placement Law), §13.5 (drift anti-patterns 8–10), §18.d (v1.2 deferred items).
- `kfm_repository_structure_guiding_document.md` §3, §8.
- `kfm_unified_doctrine_synthesis.md` Part III (cite-or-abstain), Part VI (promotion gates), Part VII (publication/sensitivity), Part XI (validator worked example).
- `ai-build-operating-contract.md` §10 (AI is interpretive, EvidenceBundle outranks generation), §28 (ADR triggers).
- `KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.md` Appendix C (the 13-domain object-family enumeration this ADR adopts).
- `Master_MapLibre_Components-Functions-Features_v2_1_FULL.md` Appendix C (county build plan index).
- `docs/focus-modes/README.md` v0.3 (the design spec this ADR evaluates).

### 2.5 What this ADR does NOT address

- It does **not** change the 13-domain enumeration itself. (Future changes to the domain list require their own ADR, per `docs/focus-modes/README.md` v0.3 §20.)
- It does **not** authorize a derivation path from county lanes to the state lane. State-scale composition is independent (see §3.6).
- It does **not** alter the trust membrane, the cite-or-abstain posture, the promotion-gates sequence A–G, the lifecycle states, or the sensitivity-tier scheme.
- It does **not** modify the canonical UI shell (`apps/explorer-web/` per `directory-rules.md` §7.1.a) or its drift register entry (OPEN-DR-06).
- It does **not** resolve OPEN-DR-08 (three-casings-per-area design); that resolution remains a separate ADR.

[↑ Back to top](#top)

---

## 3. Decision

This ADR makes six coupled sub-decisions. Reviewers approve or reject the ADR as a unit.

### 3.1 Sub-decision A — Add `-state` to the allowed scope-suffix enumeration

**Amend `directory-rules.md` §6.7.1 and §6.7.2** to expand the allowed scope-suffix enumeration from three to four values:

> **Before (v1.2, current):** `-county`, `-region`, `-corridor`.
>
> **After (v1.3, proposed):** `-state`, `-county`, `-region`, `-corridor`.

A Focus Mode at state scope demonstrates the full KFM trust path for a state-wide bound. State scope is **not** a derived view; it is a parallel composition at a coarser spatial bound, with its own source seeds, its own evidence chain, its own promotion decisions, and its own `ReleaseManifest`.

### 3.2 Sub-decision B — Establish `kansas-state` as the single canonical state-scale Focus Mode

- **Canonical area name:** `kansas` (lower-case kebab/snake-case; matches Kansas as a place identifier).
- **Canonical lane (in `docs/`):** `docs/focus-modes/kansas-state/`.
- **Cardinality:** Exactly **one** state-scale Focus Mode at any time. The state-scale lane is a single-instance composition by construction; multiple Kansas-scale "modes" (e.g., a "historical-Kansas" vs "modern-Kansas") are time-scoped releases of the same Focus Mode, not parallel area lanes.
- **Per-root placement** (extends `directory-rules.md` §6.7.2 by adding a state-scale row; full table is reproduced in §4.1 below).

### 3.3 Sub-decision C — Adopt the 13-domain coverage rule at every scale

Every Focus Mode (state, county, region, corridor) MUST address all 13 thematic KFM domains in its `layer-registry.md`. Each (domain, area) cell is one of:

- **`populated`** — a layer-registry entry exists with a resolved `EvidenceRef`, a sensitivity class, an owner, a release state, and a style ref.
- **`abstain`** — an explicit row documenting why the domain is not represented at this scale and area (e.g., "no admissible statewide source meets the public release threshold," or "no archaeology sites in this county survive the steward-review threshold for public release").

A **missing** or **empty** domain row is a validator failure. Silent omission collapses cite-or-abstain.

The 13 canonical domains (CONFIRMED per `KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.md` Appendix C) are:

| # | Domain | Short-name (machine key) |
|---|---|---|
| 1 | Hydrology | `hydrology` |
| 2 | Soil | `soil` |
| 3 | Atmosphere / Air | `atmosphere_air` |
| 4 | Geology | `geology` |
| 5 | Fauna | `fauna` |
| 6 | Flora | `flora` |
| 7 | Habitat | `habitat` |
| 8 | Agriculture | `agriculture` |
| 9 | Hazards | `hazards` |
| 10 | Roads / Rail / Trade | `roads_rail` |
| 11 | Settlements / Infrastructure | `settlements_infrastructure` |
| 12 | Archaeology / Cultural Heritage | `archaeology` |
| 13 | People / DNA / Land / Genealogy | `people_dna_land` |

**Three cross-cutting spine families** — Spatial Foundation, Frontier Matrix (object-family group), Planetary/3D — are NOT enumerated in the matrix because they apply to **every** Focus Mode at every scale by construction. They are spine, not domain. Future ADRs MAY change this distinction.

### 3.4 Sub-decision D — Resolve OPEN-FM-14 (state-scale release-candidate folder naming)

The state-scale release-candidate folder is **`release/candidates/kansas-focus-mode/`**, following the existing county convention `<area>-focus-mode/`. The alternative considered (`release/candidates/kansas-state-focus-mode/`) was rejected because:

1. It would break the established pattern (`ellsworth-focus-mode/`, `smoky-hill-corridor-focus-mode/`, …) for one root only.
2. The cited "Kansas vs KFM" ambiguity is resolved by context (`STATE_INDEX.md`, the lane README, the `ReleaseManifest` itself).
3. Future state-scale release candidates can disambiguate via version (e.g., `kansas-focus-mode-v3.json`) rather than folder name.

### 3.5 Sub-decision E — Amend the YAML front-matter spec and machine schema

**Amend `_template/county-build-plan.md` and add `_template/state-build-plan.md`** to require two new YAML front-matter keys (effective for all new and existing draft plans):

```yaml
scale_class: state | county | region | corridor
domain_coverage:
  hydrology: populated | abstain
  soil: populated | abstain
  atmosphere_air: populated | abstain
  geology: populated | abstain
  fauna: populated | abstain
  flora: populated | abstain
  habitat: populated | abstain
  agriculture: populated | abstain
  hazards: populated | abstain
  roads_rail: populated | abstain
  settlements_infrastructure: populated | abstain
  archaeology: populated | abstain
  people_dna_land: populated | abstain
```

**Amend `schemas/contracts/v1/focus_mode/focus_mode_payload.schema.json`** to:

- Add `scale_class` as a required field with enum `["state", "county", "region", "corridor"]`.
- Add `domain_coverage` as a required map with the 13 keys above and value enum `["populated", "abstain"]`.

**Amend `schemas/contracts/v1/focus_mode/layer_registry_entry.schema.json`** to:

- Add `domain` as a required field with enum matching the 13 canonical domain machine keys.
- Add `scale_class` as a required field (must match the parent lane's `scale_class`).

**Amend `contracts/focus_mode/focus_mode_payload.md`** semantic contract to document the new fields and their relationships.

### 3.6 Sub-decision F — Disallow state-scale derivation from counties

The state-scale Focus Mode (`kansas-state`) MUST be composed from statewide source seeds (USGS NHD, KGS statewide bedrock, KDHE statewide AQ network, KS DASC statewide layers, KDOT statewide network, NRCS gNATSGO, statewide NFHL, statewide hazards declarations, etc.). It **MUST NOT** be derived by joining or aggregating county-lane outputs.

**Why this matters.** A derived state-scale view inherits whatever evidence the county lanes resolved — it is, at best, a meta-claim about counties, not a claim about Kansas. It is also subject to spatial-join error, version skew between county lanes, and silent quality propagation from the lowest-quality county. None of these is consistent with cite-or-abstain.

**A geographically overlapping state-scale claim and county-scale claim MAY share underlying evidence** (e.g., both cite USGS gauge 06864000 in Ellsworth County). What they MUST NOT do is have one derive from the other — each resolves its own `EvidenceRef` to its own `EvidenceBundle`.

**Future PROPOSED artifact (not part of this ADR).** A `contracts/focus_mode/cross_scale_crosswalk.md` MAY be authored later to document optional, non-derivative linkages between state-scale and county-scale claims (e.g., "the state-scale hydrology layer's HUC-4 polygon for Smoky Hill includes the HUC-12 sub-watershed that the ellsworth-county hydrology layer cites in detail"). The crosswalk would be a navigation aid, not an evidence chain. This is tracked as **OPEN-FM-15** (PROPOSED in §10).

[↑ Back to top](#top)

---

## 4. Consequences

### 4.1 What changes in `directory-rules.md`

**PROPOSED v1.3 amendment to §6.7.** The §6.7.2 placement table gains state-scale entries across all twelve host roots. The full amended table:

| Root | County-scale pattern (CONFIRMED v1.2) | State-scale pattern (PROPOSED v1.3, this ADR) | Authority |
|---|---|---|---|
| `docs/` | `docs/focus-modes/<area>-<scope>/` | `docs/focus-modes/kansas-state/` | Canonical |
| `contracts/` | `contracts/focus_mode/` (shared) | (shared lane) | Canonical |
| `schemas/` | `schemas/contracts/v1/focus_mode/` (shared) | (shared lane) | Canonical |
| `fixtures/` | `fixtures/focus_modes/<area>/{valid,invalid}/` | `fixtures/focus_modes/kansas/{valid,invalid}/` | Canonical |
| `apps/` | `apps/explorer-web/src/focus-modes/<area>/` | `apps/explorer-web/src/focus-modes/kansas/` | Canonical |
| `tools/` | `tools/validators/validate_focus_mode_*.py` (shared) | (shared) — validators MUST accept all four scale values | Canonical |
| `data/catalog/` | `data/catalog/sources/<area>/`, `data/catalog/stac/<area>/` | `data/catalog/sources/kansas/`, `data/catalog/stac/kansas/` | Canonical |
| `data/published/` | `data/published/layers/<area>/`, `data/published/api_payloads/focus-modes/<area>.json` | `data/published/layers/kansas/`, `data/published/api_payloads/focus-modes/kansas.json` | Canonical |
| `data/registry/` | `data/registry/sources/<area>/` (optional) | `data/registry/sources/kansas/` (optional) | Canonical |
| `release/` | `release/candidates/<area>-focus-mode/`, `release/manifests/<area>-focus-mode-v<n>.json` | `release/candidates/kansas-focus-mode/`, `release/manifests/kansas-focus-mode-v<n>.json` | Canonical (per §3.4) |
| `pipeline_specs/` | `pipeline_specs/focus_modes/<area>/` (optional) | `pipeline_specs/focus_modes/kansas/` (optional) | Canonical |
| `examples/` | `examples/focus-modes/<area>/` (optional) | `examples/focus-modes/kansas/` (optional) | Canonical |
| `policy/` | `policy/sensitivity/<area>/` (optional) | `policy/sensitivity/kansas/` (optional; rare — see §4.7) | Canonical |

**PROPOSED v1.3 amendment to §6.7.1** (definition):

> Before: "A **Focus Mode** is a governed, evidence-bounded, county- or region-scale proof slice…"
>
> After: "A **Focus Mode** is a governed, evidence-bounded, **state-, county-, region-, or corridor-scale** proof slice…"

**PROPOSED v1.3 amendment to §6.7.3** (casing convention): no structural change; the per-root casing logic already covers a single-token area like `kansas`. The §6.7.3 examples gain a state-scale row.

**PROPOSED v1.3 amendment to §6.7.4** (one area = one Focus Mode): no structural change; cardinality at state scope is governed by §3.2 of this ADR (exactly one).

**PROPOSED v1.3 amendment to §6.7.5** (what a Focus Mode is NOT): add two drift signatures:

> - **State-scale roll-up.** Deriving the state-scale Focus Mode by joining/aggregating county-scale outputs (→ §3.6 of ADR-0028).
> - **Domain-coverage omission.** Failing to address all 13 domains at every scale, populated or abstained on the record (→ §3.3 of ADR-0028).

**PROPOSED v1.3 amendment to §13.5** (drift anti-pattern register): two new rows, mirroring the §6.7.5 additions.

**PROPOSED v1.3 amendment to §18.d** (deferred items): close OPEN-FM-09, OPEN-FM-10, OPEN-FM-14; open OPEN-FM-15 (cross-scale crosswalk artifact) and OPEN-FM-16 (state-scale sensitivity overrides).

### 4.2 What changes in schemas

| Schema file | Change | Breaking? |
|---|---|---|
| `schemas/contracts/v1/focus_mode/focus_mode_payload.schema.json` | Add required `scale_class` enum; add required `domain_coverage` map | **Breaking for existing draft payloads** that lack these fields. **Non-breaking for released payloads** because none exist yet (no county lane has reached `released` status). |
| `schemas/contracts/v1/focus_mode/layer_registry_entry.schema.json` | Add required `domain` enum; add required `scale_class` field | Same — breaking for drafts, non-breaking for releases. |
| `contracts/focus_mode/focus_mode_payload.md` | Document new fields; no breaking semantic change | Non-breaking (semantic) |

**Schema versioning.** Per `directory-rules.md` §6.4 and ADR-0001, the schema home is `schemas/contracts/v1/...`. This ADR does NOT bump the major version (`v1` → `v2`) because the additions can be back-filled into existing draft fixtures within the same major version. Schema steward MAY require a minor-version bump in the file's `$id` (e.g., `v1.0` → `v1.1`) if the project's schema-versioning convention requires it; this is left to schema steward judgment.

### 4.3 What changes in validators

`tools/validators/validate_focus_mode_index.py` gains the v0.3 checks already enumerated in `docs/focus-modes/README.md` v0.3 §19 (checks 2, 6, 7, 8, 13, 15, 17). The full list of new behavior:

1. Recognize `-state` as a valid scope suffix; verify exactly one `kansas-state/` lane exists when any state-scale work is in flight.
2. Parse `STATE_INDEX.md` and verify it contains exactly one row (`area: kansas`, `scope: state`).
3. Verify `scale_class` front-matter key matches the lane's scope suffix.
4. Verify `domain_coverage` map contains all 13 canonical domain keys; each value ∈ `{populated, abstain}`.
5. Verify `layer-registry.md` contains a §14 matrix row consistent with the front-matter map.
6. Verify acceptance-checklist item (i) (13-domain coverage) is present.

`tools/validators/validate_focus_mode_payload.py` is amended (or emitted, if not yet present) to accept `scale_class ∈ {state, county, region, corridor}` and to enforce 13-domain coverage closure.

### 4.4 What changes in templates

- `docs/focus-modes/_template/county-build-plan.md` — amended YAML front-matter (adds `scale_class: county` default; adds `domain_coverage` map skeleton).
- `docs/focus-modes/_template/state-build-plan.md` — **NEW**. Emitted on ADR acceptance. Same shape as county template but with `scale_class: state`, `area: kansas`, and statewide-source-first source-seed-list ordering.

### 4.5 What changes in the directory tree

**New artifacts** (PROPOSED, emitted in the acceptance PR or its immediate follow-up):

- `docs/adr/ADR-0028-state-scale-focus-mode-scope.md` — this file.
- `docs/focus-modes/STATE_INDEX.md` — single-area state-scale index.
- `docs/focus-modes/_template/state-build-plan.md` — state-scale template.
- `docs/focus-modes/kansas-state/` — the single state-scale lane (PROPOSED to land as PR-1 of the four-PR sequence).

**Amended artifacts:**

- `docs/standards/directory-rules.md` — §6.7 amendments per §4.1 above; §18.d open-items register update; §21 changelog (v1.3 entry).
- `docs/focus-modes/README.md` — version bump v0.3 → v0.4 reflecting acceptance (changes PROPOSED labels on state-scale rows to CONFIRMED).
- `docs/focus-modes/_template/county-build-plan.md` — YAML front-matter additions.
- `docs/focus-modes/COUNTY_INDEX.md` — add `scale_class` column (default `county`) for consistency.
- `contracts/focus_mode/focus_mode_payload.md` — new fields documented.
- `schemas/contracts/v1/focus_mode/focus_mode_payload.schema.json` — schema additions.
- `schemas/contracts/v1/focus_mode/layer_registry_entry.schema.json` — schema additions.
- `tools/validators/validate_focus_mode_index.py` — new checks.
- `tools/validators/validate_focus_mode_payload.py` — new behavior (or emitted, if absent).
- `docs/registers/DRIFT_REGISTER.md` — close OPEN-FM-09, OPEN-FM-10, OPEN-FM-14; open OPEN-FM-15, OPEN-FM-16.

### 4.6 What changes for in-flight county draft plans

The 17+ draft county build plans currently lack a `scale_class` field and a `domain_coverage` map. On acceptance:

- **Back-fill is required**, not optional. Each draft plan owner SHOULD add `scale_class: county` and the `domain_coverage` map to their YAML front-matter on next revision.
- **No release is blocked** by the back-fill, because no county lane has reached `released` status (all are `draft`).
- **The validator MUST emit a deprecation warning, not an error**, for the first 14 days after acceptance, identifying lanes that lack the new keys. After 14 days, the warning becomes an error.
- **The new negative fixtures** (`missing_domain_coverage.invalid.json`, `wrong_scale_class.invalid.json`) MUST be present in each lane's `fixtures/focus_modes/<area>/invalid/` directory on next revision.

### 4.7 What changes for sensitivity policy

`policy/sensitivity/kansas/` is **permitted but not expected** at v0.3 launch. The default state-scale posture inherits cross-domain defaults; per-state overrides are rare and require the same ADR-level justification as per-county overrides (deny-fixture + documented rationale). **OPEN-FM-16** tracks whether any state-scale override is justified at launch.

The key sensitivity invariant (PROPOSED v0.3 §15 of README, restated by this ADR): aggregation at state scale lowers risk for some lanes (parcels, infrastructure footprints, fauna occurrences) but does **NOT** lower risk for archaeology coordinates, rare-species exact locations, living-person data, or DNA. Those remain deny-default at both scales.

### 4.8 What does NOT change

- The trust path itself (`SourceDescriptor → … → ReleaseManifest → Public UI`).
- The trust membrane (public UI never reads `data/raw/`, `data/work/`, `data/quarantine/`).
- The cite-or-abstain posture.
- The promotion-gates sequence A–G.
- The lifecycle states (`not-started`, `planned`, `draft`, `validated`, `payload-ready`, `released`, `rolled-back`, `deprecated`).
- The canonical UI shell (`apps/explorer-web/`).
- The schema home rule (per ADR-0001).
- The Domain Placement Law (`directory-rules.md` §12). Focus Modes remain cross-cutting; this ADR does not promote any domain to a root folder.
- The 13-domain enumeration itself. (Future changes to the list require their own ADR.)
- The casing convention's three-styles-per-area design (OPEN-DR-08 remains open and unresolved by this ADR).

### 4.9 CI and review impact

- CI MUST run `validate_focus_mode_index.py` and `validate_focus_mode_payload.py` on every PR touching `docs/focus-modes/`, `contracts/focus_mode/`, `schemas/contracts/v1/focus_mode/`, `fixtures/focus_modes/`, `apps/explorer-web/src/focus-modes/`, or `release/manifests/focus_modes/`.
- The acceptance PR adds a new reviewer role: **state-scale steward** (PROPOSED `<OWNER:state-scale-steward>`). The reviewer is responsible for the `kansas-state/` lane's content quality, statewide source-seed admissibility, and 13-domain coverage closure.
- The acceptance PR adds **two new fixture classes** (negative) to the required-negative-fixture list: `missing_domain_coverage.invalid.json` and `wrong_scale_class.invalid.json`.

[↑ Back to top](#top)

---

## 5. Alternatives considered

### 5.1 Alt A — Reject; keep county-only scope

**Considered.** Leave `directory-rules.md` §6.7 unchanged. Address statewide questions through cross-cutting layers (per `directory-rules.md` §12's "multi-domain and cross-cutting files" guidance) without elevating to a Focus Mode.

**Rejected because:**

- Cross-cutting layers have no `MapReleaseManifest`. The release gate is per-Focus-Mode, so a layer without a Focus Mode home cannot complete the trust path's `Release → Public UI` arc.
- Cross-cutting layers have no `EvidenceDrawerPayload`-shaped acceptance surface. The Evidence Drawer is governed at the Focus Mode level.
- The cross-cutting alternative produces an unauditable umbrella view by construction — exactly the failure-mode this ADR exists to prevent.

### 5.2 Alt B — Model state-scale as a "Frontier Matrix" object family rather than a Focus Mode

**Considered.** The `KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.md` Appendix C lists Frontier Matrix as a cross-cutting object family (`Frontier Definition`, `GeographyVersion`, `County-Year Panel`, …). One could argue the state-scale view IS the Frontier Matrix, and no new Focus Mode scope is needed.

**Rejected because:**

- Frontier Matrix object families are **cross-cutting analytical objects** (county-year panels, admin-boundary changes, crosswalks), not a spatial-frame composition. They appear at every scale.
- Confusing "Frontier Matrix object family" (an analytical lens) with "state-scale Focus Mode" (a spatial bound) would re-introduce the exact category collapse that `directory-rules.md` §12 (Domain Placement Law) warns against.
- The Focus Mode pattern's whole point is to make the spatial bound the unit of release governance. Hijacking Frontier Matrix to do that would split governance across two object models.

### 5.3 Alt C — Permit informal "state context" without elevating to a scope

**Considered.** Allow each county Focus Mode to carry an informal "statewide context section" that summarizes statewide framing for that county, without creating a state-scale Focus Mode.

**Rejected because:**

- The statewide framing would be authored 105 times, with no canonical version. (Drift by construction.)
- No `EvidenceRef` resolves at the state scale; the statewide claim has no `EvidenceBundle`.
- This is the current de facto situation, and it is the gap this ADR addresses.

### 5.4 Alt D — Different scope suffix names (`-statewide`, `-kansas`)

**Considered.** Use `-statewide` or `-kansas` instead of `-state`.

**Rejected because:**

- `-statewide` is a description, not a scope category. The other suffixes (`-county`, `-region`, `-corridor`) are spatial-unit categories; mixing categories with descriptions breaks the enumeration's symmetry.
- `-kansas` couples the scope to a place (Kansas), which is already encoded in the area name. Two places encoding the same fact is drift waiting to happen.
- `-state` is consistent with U.S. administrative-unit naming and matches the existing pattern.

### 5.5 Alt E — Different area name (`statewide`, `kansas-statewide`)

**Considered.** Use `statewide` as the area name (giving `docs/focus-modes/statewide-state/`) or `kansas-statewide` (giving `docs/focus-modes/kansas-statewide-state/`).

**Rejected because:**

- `statewide` is not a place; it is a property. The area name must identify the place.
- `kansas-statewide-state/` is redundant (the `-state` scope suffix already says "this is statewide"). It reads awkwardly.
- `kansas` is the unambiguous place identifier; in KFM's context, "kansas at state scale" is exactly `kansas-state`.

### 5.6 Alt F — Different release-candidate folder name (`kansas-state-focus-mode/`)

**Considered.** Use `release/candidates/kansas-state-focus-mode/` instead of `release/candidates/kansas-focus-mode/`, to disambiguate from "Kansas Frontier Matrix" (the whole project).

**Rejected because:**

- Pattern consistency wins. The county pattern is `<area>-focus-mode/`; changing this for state alone introduces inconsistency in one root.
- The cited ambiguity is context-resolved (the `STATE_INDEX.md`, the lane README, and the `ReleaseManifest` itself all carry the scope).
- See §3.4 for the full rationale.

**Reconsider if:** during the v0.3 implementation, the ambiguity proves to be a friction point in code review or onboarding. The decision can be revisited via a follow-up ADR.

### 5.7 Alt G — Permit multiple state-scale instances (multi-tenant or time-scoped)

**Considered.** Permit lanes like `kansas-historical-state/` and `kansas-modern-state/` as parallel state-scale compositions.

**Rejected because:**

- Time-scoping is governed by `ReleaseManifest` versioning and the `GeographyVersion` / `County-Year Panel` object families, not by lane multiplication.
- "One area = one Focus Mode" (`directory-rules.md` §6.7.4) is the existing invariant; this ADR extends it to state scale without weakening it.
- Multiple parallel state-scale lanes would re-introduce the umbrella-view fragmentation that motivated this ADR.

### 5.8 Alt H — Permit roll-up derivation from counties

**Considered.** Define the state-scale composition as a derived view that joins/aggregates county-scale outputs.

**Rejected because:**

- Derivation inherits the lowest-quality county evidence silently.
- Spatial joins across 105 county lanes introduce non-trivial geometry error without any provenance record of that error.
- Version skew between county lanes (each on its own cadence) means the derived view has no coherent temporal frame.
- A derived view is a meta-claim about counties, not a claim about Kansas. The two are not interchangeable for trust-path purposes.
- See §3.6 for the full rationale.

### 5.9 Alt I — Split this ADR into two ADRs (scope addition + coverage rule)

**Considered.** ADR-0028 covers only the `-state` scope addition; a separate ADR (e.g., ADR-0029) covers the 13-domain coverage rule.

**Rejected because:**

- The two changes are operationally coupled. A state-scale composition without the coverage rule produces an umbrella that silently omits domains — exactly the gap §2.1.3 identifies. The coverage rule without a state-scale composition leaves the umbrella unanswerable.
- The §3.5 schema and YAML front-matter amendments (the `scale_class` enum and the `domain_coverage` map) are joint requirements; splitting the ADR would force two schema bumps and two validator updates instead of one.
- The README v0.3 §20 ADR-trigger language treats them as a single v0.3 amendment.
- Reviewers can still vote granularly: the §3 sub-decisions A–F are individually motivated, and a reviewer who objects to one sub-decision can request a sub-decision change without rejecting the ADR as a whole.

**Reconsider if:** review feedback strongly suggests the two should be voted independently. In that case, this ADR can be superseded by ADR-0028A (scope) + ADR-0028B (coverage), with §3.5 amendments split across them.

### 5.10 Alt J — Defer the 13-domain coverage rule to a later ADR; only do scope addition now

**Considered.** Add the `-state` scope in this ADR; defer the 13-domain coverage rule.

**Rejected because:**

- Without the coverage rule, the `kansas-state` lane has no acceptance criterion that prevents silent omission of half the domains. The first state-scale release would then be uncited on those omissions, which contradicts cite-or-abstain.
- The coverage rule is what makes the state-scale view auditable as an umbrella. Deferring it defeats the ADR's purpose.

[↑ Back to top](#top)

---

## 6. Migration plan

This ADR's migration is **additive and reversible**. No existing released artifact changes; no existing canonical path is renamed or removed.

### 6.1 Ordering

```mermaid
flowchart LR
  P1[PR-1<br/>ADR + STATE_INDEX + templates + schema/contract amendments]:::p1
  P2[PR-2<br/>validator amendments + new negative fixtures]:::p2
  P3[PR-3<br/>kansas-state/ lane scaffold<br/>seven required files]:::p3
  P4[PR-4<br/>directory-rules.md §6.7 amendment + drift register update]:::p4
  P5[PR-5+<br/>back-fill scale_class + domain_coverage<br/>into existing county draft plans]:::p5

  P1 --> P2 --> P3 --> P4 --> P5

  classDef p1 fill:#dbeafe,stroke:#1e3a8a,color:#000
  classDef p2 fill:#fae8ff,stroke:#581c87,color:#000
  classDef p3 fill:#dcfce7,stroke:#14532d,color:#000
  classDef p4 fill:#fef3c7,stroke:#78350f,color:#000
  classDef p5 fill:#fee2e2,stroke:#7f1d1d,color:#000
```

### 6.2 Step-by-step

1. **PR-1 (this ADR + control-plane scaffolds)** — Land this ADR file, `STATE_INDEX.md`, `_template/state-build-plan.md`, the YAML front-matter amendment to `_template/county-build-plan.md`, and the schema/contract amendments. The README v0.3 file (already merged) stays at v0.3 until §6.4 below.
2. **PR-2 (validator amendments)** — Update `validate_focus_mode_index.py` and `validate_focus_mode_payload.py` for the new checks. Emit the two new negative-fixture classes (`missing_domain_coverage.invalid.json`, `wrong_scale_class.invalid.json`) into `fixtures/focus_modes/_template/invalid/` (or wherever the project's invalid-fixture canonical lane is — `NEEDS_VERIFICATION` on live-repo presence).
3. **PR-3 (`kansas-state/` lane scaffold)** — Scaffold the `docs/focus-modes/kansas-state/` lane with the seven required files. Status moves `not-started → planned → draft`. No `FocusModePayload` is built yet; this PR establishes the control-plane content.
4. **PR-4 (directory-rules.md §6.7 amendment)** — Amend `directory-rules.md` §6.7.1 (definition), §6.7.2 (placement table), §6.7.5 (what a Focus Mode is NOT), §13.5 (drift register), §18.d (deferred items), §21 (changelog v1.3 entry). Update `docs/focus-modes/README.md` from v0.3 → v0.4 (changes `-state` PROPOSED labels to CONFIRMED). Close OPEN-FM-09, OPEN-FM-10, OPEN-FM-14 in the drift register.
5. **PR-5+ (back-fill)** — For each in-flight county draft plan, back-fill `scale_class: county` and the `domain_coverage` YAML map. This can land in a single sweep PR or per-county PRs. The 14-day deprecation-warning window in §4.6 gives owners time to back-fill.

### 6.3 Cadence

- **PR-1 through PR-4 SHOULD land in close succession** (within 7 days of acceptance), to minimize the window in which the README and `directory-rules.md` are out of step.
- **PR-5+ MAY take up to the full 14-day deprecation-warning window** before the validator escalates from warning to error.

### 6.4 Effective-on semantics

- **On PR-1 merge:** This ADR's status MAY advance from `proposed` to `accepted` once §7 acceptance criteria are met. The README and `directory-rules.md` are not yet updated.
- **On PR-4 merge:** The `directory-rules.md` amendment is live; the README is updated to v0.4. The `-state` scope is canonical from this point forward.
- **On PR-5+ completion:** All in-flight county draft plans validate against the new schema. The 14-day deprecation-warning window closes.

[↑ Back to top](#top)

---

## 7. Acceptance criteria

The ADR's status advances from `proposed` to `accepted` only when **all** of the following are CONFIRMED:

### 7.1 Reviewer sign-off

- [ ] `<OWNER:focus-mode-steward>` — approves §3.1 (scope addition), §3.2 (canonical area + cardinality), §3.6 (no roll-up derivation).
- [ ] `<OWNER:directory-rules-steward>` — approves §4.1 (`directory-rules.md` §6.7 amendments) and §4.6 (in-flight county draft impact).
- [ ] `<OWNER:schema-steward>` — approves §3.5 and §4.2 (schema amendments), including the schema-versioning decision.
- [ ] `<OWNER:sensitivity-reviewer>` — approves §4.7 (state-scale sensitivity posture; deny-default lanes unchanged across scales).
- [ ] **PROPOSED new role:** `<OWNER:state-scale-steward>` — willing to take on ownership of the `kansas-state/` lane.

### 7.2 Draft artifacts present (PR-1 scope)

- [ ] This ADR file (`docs/adr/ADR-0028-state-scale-focus-mode-scope.md`).
- [ ] `docs/focus-modes/STATE_INDEX.md` draft.
- [ ] `docs/focus-modes/_template/state-build-plan.md` draft.
- [ ] Amended `docs/focus-modes/_template/county-build-plan.md` (YAML front-matter additions).
- [ ] Amended `schemas/contracts/v1/focus_mode/focus_mode_payload.schema.json` (draft of additions).
- [ ] Amended `schemas/contracts/v1/focus_mode/layer_registry_entry.schema.json` (draft of additions).
- [ ] Amended `contracts/focus_mode/focus_mode_payload.md` (semantic documentation of new fields).

### 7.3 Validator readiness (PR-2 scope)

- [ ] `tools/validators/validate_focus_mode_index.py` extension drafted, with all v0.3 checks (§4.3) implemented or stubbed.
- [ ] `tools/validators/validate_focus_mode_payload.py` drafted (or amended), accepting `scale_class ∈ {state, county, region, corridor}`.
- [ ] Two new negative-fixture classes (`missing_domain_coverage.invalid.json`, `wrong_scale_class.invalid.json`) drafted.

### 7.4 Risk surface review

- [ ] No `data/raw/`, `data/work/`, or `data/quarantine/` access introduced (trust membrane preserved).
- [ ] No `apps/web/` reference introduced (canonical shell preserved per `directory-rules.md` §7.1.a).
- [ ] No `.schema.json` files added under `contracts/focus_mode/` (schema home preserved per ADR-0001).
- [ ] No `focus_modes/` or `focus-modes/` directory at repo root (root-stays-boring per `directory-rules.md` §3).
- [ ] No state-scale derivation from county outputs (per §3.6).

### 7.5 Drift register updates

- [ ] OPEN-FM-09 (state-scale scope) closure entry drafted.
- [ ] OPEN-FM-10 (13-domain coverage rule) closure entry drafted.
- [ ] OPEN-FM-14 (release-candidate folder naming) closure entry drafted with §3.4 resolution.
- [ ] OPEN-FM-15 (cross-scale crosswalk artifact) open entry drafted.
- [ ] OPEN-FM-16 (state-scale sensitivity overrides review) open entry drafted.

### 7.6 Non-blocking observations

The following items are noted in this ADR but are **not** acceptance gates:

- Per-county owner back-fill (`<OWNER>` placeholders in `COUNTY_INDEX.md`) — separate workstream.
- Existence of `docs/registers/DRIFT_REGISTER.md` in the live repo (OPEN-DR-09) — NEEDS VERIFICATION; if absent, the close-entry artifacts go wherever the live drift register canonically lives.
- Resolution of OPEN-DR-06 (`apps/web/` drift) — separate ADR scope.
- Resolution of OPEN-DR-08 (three-casings-per-area) — separate ADR scope.

[↑ Back to top](#top)

---

## 8. Rollback plan

This ADR is reversible. Rollback affects only artifacts that this ADR introduces or amends.

### 8.1 Trigger for rollback

Rollback should be initiated if **any** of the following becomes true within the first 90 days after PR-4 merge:

- A material flaw is discovered in §3.3 (13-domain coverage rule) that makes it unenforceable (e.g., a domain that genuinely cannot be addressed at any scale even by abstain).
- A material flaw is discovered in §3.6 (no roll-up derivation) that makes the state-scale lane impossible to compose from admissible statewide sources (i.e., the alternative considered in §5.8 turns out to be the only feasible path).
- The schema amendments in §3.5 prove incompatible with downstream consumers in ways that cannot be back-fixed by minor version bumps.
- Reviewer consensus determines the ADR's coupling (§5.9 alternative) was the wrong call and the two decisions must be voted independently.

### 8.2 Rollback procedure

1. **Set ADR status:** `accepted → superseded` (with forward link to the replacing ADR or to a "rejected" marker).
2. **Revert `directory-rules.md` §6.7 amendments:** restore the v1.2 three-scope enumeration.
3. **Revert `docs/focus-modes/README.md`:** v0.4 → v0.3 (state-scale rows return to PROPOSED labels) or v0.3 → v0.2 (state-scale extension removed entirely), per the rollback scope.
4. **Revert schema amendments:**
   - Remove `state` from the `scale_class` enum.
   - Mark `domain_coverage` as optional (downgrade from required) for a one-release deprecation window.
   - After the deprecation window, remove `domain_coverage` entirely.
5. **Revert validator extensions:** restore pre-ADR check list.
6. **Handle the `kansas-state/` lane:**
   - If the lane has reached `draft` or earlier — `git rm` the lane with a `docs/registers/DRIFT_REGISTER.md` entry explaining the supersession.
   - If the lane has reached `validated` or later — write a `RollbackCard` per `directory-rules.md` §9.2 lifecycle invariants. Cache invalidation: invalidate any `ReleaseManifest` published under `release/manifests/kansas-focus-mode-v<n>.json`.
   - If the lane has reached `released` (i.e., a public claim exists at state scale) — rollback escalates to a full release-rollback governed by the existing `RollbackCard` discipline. This ADR's rollback does NOT bypass release-rollback governance.
7. **Update drift register:** close the OPEN-FM-15 and OPEN-FM-16 entries (if open); re-open OPEN-FM-09, OPEN-FM-10, OPEN-FM-14 with the rollback context attached.
8. **Communicate:** post a supersession notice in `docs/adr/INDEX.md` (if present, `NEEDS_VERIFICATION`) and in `docs/focus-modes/README.md` change log.

### 8.3 Rollback target reference

The rollback target is the **pre-v0.3 state of `docs/focus-modes/README.md`** (i.e., the v0.2 file) plus the **pre-amendment `directory-rules.md` §6.7 text** (i.e., v1.2). No published `ReleaseManifest` exists at state scale at the time of this ADR draft, so no released artifact rolls back.

[↑ Back to top](#top)

---

## 9. Related ADRs and references

### 9.1 ADRs

| ADR | Relationship |
|---|---|
| `ADR-0001-schema-home.md` (PROPOSED file path; CONFIRMED reference) | This ADR honors the schema-home rule: machine schemas live at `schemas/contracts/v1/focus_mode/`, not under `contracts/focus_mode/`. No exception. |
| `ADR-0003-policy-singular-is-canonical.md` (PROPOSED file path) | This ADR honors `policy/` (singular) as canonical for any per-state sensitivity overrides. |
| `ADR-0027-county-focus-mode-control-plane.md` (PROPOSED) | This ADR extends the county-control-plane ADR's scope to include state-scale. The two ADRs are coordinated; ADR-0027 owns the county scaffold, ADR-0028 owns the state-scale scaffold and the cross-scale coverage rule. |
| `ADR-S-05-sensitivity-tier-scheme.md` (PROPOSED) | This ADR references the T0–T4 tier scheme without amending it; the §4.7 / §15-of-README sensitivity table consumes the tier semantics. |
| Future ADR (PROPOSED) — "13-domain enumeration changes" | This ADR establishes the coverage rule over the 13-domain list; future changes to the list itself require a separate ADR. |

### 9.2 Doctrine documents

- `directory-rules.md` — §3, §2.1, §2.4, §6.7, §12, §13.5, §18.d, §21.
- `kfm_repository_structure_guiding_document.md` — §3, §8.
- `kfm_unified_doctrine_synthesis.md` — Part III (cite-or-abstain), Part VI (promotion gates), Part VII (publication/sensitivity), Part XI (validator worked example).
- `ai-build-operating-contract.md` — §10, §28, §29.
- `KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.md` — Appendix C (13-domain enumeration; CONFIRMED source for §3.3).
- `Master_MapLibre_Components-Functions-Features_v2_1_FULL.md` — §16.3 (COUNTY-01..04), Appendix C (county family).
- `docs/focus-modes/README.md` v0.3 — the design spec this ADR evaluates.

### 9.3 External standards (CONFIRMED references; no version pinning in this ADR)

- W3C PROV-O — provenance terms used by `EvidenceBundle` and `AIReceipt`.
- OGC STAC — catalog model under `data/catalog/stac/`.
- ISO 19115 — metadata crosswalk profile.

[↑ Back to top](#top)

---

## 10. Open items not resolved by this ADR

| ID | Item | Status | Disposition |
|---|---|---|---|
| OPEN-FM-15 | **PROPOSED v0.3** — cross-scale crosswalk artifact (optional, non-derivative documentation of state ↔ county evidence linkages) | NEW (opens with this ADR) | Future PROPOSED artifact `contracts/focus_mode/cross_scale_crosswalk.md`. Non-blocking. See §3.6 closing paragraph. |
| OPEN-FM-16 | **PROPOSED v0.3** — review whether any per-state sensitivity override is justified at v0.3 launch | NEW (opens with this ADR) | Sensitivity reviewer assesses on PR-3 review. Default: none. |
| OPEN-DR-06 | Several county draft plans reference `apps/web/`; canonical is `apps/explorer-web/` | CONFIRMED drift (pre-existing) | Out of scope for this ADR. See `directory-rules.md` §18.d. |
| OPEN-DR-07 | Validator orchestrator path (`tools/validate_all.py` live vs doctrine variant) | CONFIRMED variance (pre-existing) | Out of scope for this ADR. |
| OPEN-DR-08 | Three casings per area across roots | OPEN (pre-existing) | Out of scope for this ADR. The §3.2 / §4.1 placement table inherits the three-casing convention without resolving it. |
| OPEN-DR-09 | Existence of `docs/registers/DRIFT_REGISTER.md` | NEEDS VERIFICATION (pre-existing) | Affects where OPEN-FM-15 and OPEN-FM-16 are recorded; does not block this ADR. |

[↑ Back to top](#top)

---

## 11. Notes and appendix

### 11.1 What an `abstain` row looks like in `layer-registry.md`

**PROPOSED example, for illustration only.** A `kansas-state/layer-registry.md` row for Archaeology might read:

```markdown
| Domain | Archaeology |
| scale_class | state |
| status | abstain |
| reason | Statewide archaeology coordinates are deny-default at every scale (kfm_unified_doctrine_synthesis.md Part VII; ADR-0028 §4.7). The state-scale view publishes the cultural-temporal-period overlay (T0; CulturalTemporalPeriod object family) but does NOT publish site coordinates, even generalized, without per-site steward review. |
| owner | <OWNER:archaeology-steward> |
| evidence_ref | (none — abstain row) |
```

The `abstain` row is **not** an absence of information. It is an explicit, owned, citable record of why the domain is not represented at this (scale, area) cell. It survives validator review precisely because it is on the record.

### 11.2 What `populated` looks like

**PROPOSED example, for illustration only.** A `kansas-state/layer-registry.md` row for Hydrology might read:

```markdown
| Domain | Hydrology |
| scale_class | state |
| status | populated |
| layer_id | kfm://layer/kansas-state/hydrology/huc4-summary-v1 |
| evidence_ref | kfm://evidence/usgs-nhd-statewide-2025-q4 |
| evidence_bundle | resolved |
| sensitivity_class | T0 (regulatory) |
| time_scope | 2025-Q4 snapshot of USGS NHD high-resolution layer |
| style_ref | apps/explorer-web/src/focus-modes/kansas/styles/hydrology.json |
| owner | <OWNER:hydrology-steward> |
| release_state | draft |
```

### 11.3 Why the v1.2 → v1.3 jump (not v1.2.1)

This ADR amends `directory-rules.md` §6.7 (the placement contract). Per `directory-rules.md` §21 changelog conventions (PROPOSED), placement-contract amendments warrant a minor-version bump (v1.2 → v1.3), not a patch (v1.2.1). The §6.7.1 definition text changes; the §6.7.2 placement table gains rows; §6.7.5 gains drift signatures. A patch-level bump would understate the change.

### 11.4 Truth labels self-check

This ADR uses CONFIRMED, PROPOSED, NEEDS VERIFICATION, UNKNOWN, and EXTERNAL labels per the AI Build Operating Contract. Material truth-label distribution:

- **CONFIRMED:** Doctrine citations (directory-rules.md §6.7 current text; 13-domain enumeration from KFM_Domains_v1_1 Appendix C; trust path stages from kfm_unified_doctrine_synthesis.md); the gap analysis based on observable corpus state.
- **PROPOSED:** The scope addition (`-state`), the area name (`kansas`), the casing decisions, the §4.1 placement-table amendments, the §4.2 schema amendments, the §4.3 validator amendments, the §4.4 template amendments, the §3.4 OPEN-FM-14 resolution, the migration sequence in §6, the acceptance criteria in §7, the rollback plan in §8.
- **NEEDS VERIFICATION:** Live-repo presence of `docs/registers/DRIFT_REGISTER.md`; live-repo presence of `docs/adr/INDEX.md`; live-repo paths for ADR-0001, ADR-0003, ADR-0027; presence of in-flight county draft plans matching the README v0.3 §21 registry.
- **UNKNOWN:** Whether any in-flight county draft plan has begun back-fill of v0.3 YAML front-matter additions in advance of this ADR; whether `tools/validate_all.py` (canonical orchestrator path per §7.5.a) discovers `validate_focus_mode_index.py` and `validate_focus_mode_payload.py` via the registry yaml that may or may not exist at `tools/validators/registry.yaml` in the live repo.

### 11.5 Anti-fabrication discipline

This ADR leaves the following as **explicit placeholders** rather than inventing concrete values:

- `<OWNER:focus-mode-steward>`, `<OWNER:directory-rules-steward>`, `<OWNER:schema-steward>`, `<OWNER:sensitivity-reviewer>`, `<OWNER:state-scale-steward>` (new role).
- CI badge URLs (none invented).
- Schema `$id` URIs (left to schema steward judgment per §4.2).
- Spec hashes for any of the PROPOSED artifacts.
- Live-repo paths for `docs/registers/DRIFT_REGISTER.md`, `docs/adr/INDEX.md`, and validator registry yaml.

[↑ Back to top](#top)

---

## 12. ADR self-check

Per `directory-rules.md` §2.4 ADR template fields, this ADR declares:

| Field | Value |
|---|---|
| `id` | ADR-0028 |
| `title` | State-scale Focus Mode scope (`-state`) and 13-domain coverage rule |
| `status` | `proposed` |
| `date` | 2026-05-23 |
| `context` | §2 above |
| `decision` | §3 above (six coupled sub-decisions) |
| `consequences` | §4 above |
| `alternatives` | §5 above (ten alternatives considered) |
| `migration_plan` | §6 (KFM convention; not required by §2.4 minimum) |
| `acceptance_criteria` | §7 (KFM convention; not required by §2.4 minimum) |
| `rollback_plan` | §8 (KFM convention; not required by §2.4 minimum) |
| `supersedes` | none |
| `superseded_by` | none |

**Self-check items** (PROPOSED v0.3, mirrors the KFM ADR self-check convention):

- [x] All claims labeled CONFIRMED / PROPOSED / NEEDS VERIFICATION / UNKNOWN per §11.4.
- [x] Doctrine citations resolve to attached corpus documents.
- [x] Cited `directory-rules.md` sections (§6.7, §2.4, §13.5, §18.d, §21) reflect v1.2 corpus state.
- [x] Cited domain enumeration (13 domains) traceable to `KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.md` Appendix C.
- [x] No invented file paths claimed as live-repo CONFIRMED (placeholders marked NEEDS VERIFICATION or PROPOSED).
- [x] No bypass of trust membrane proposed (the AI surface and the lifecycle invariants are unchanged).
- [x] Rollback path defined (§8).
- [x] Acceptance criteria gated (§7); no auto-acceptance.
- [x] Reconciliation invariant preserved: this ADR amends `directory-rules.md`; the README is a downstream restatement.

---

> [!IMPORTANT]
> **Reconciliation invariant (this ADR).** On acceptance, the **canonical text** lives in `directory-rules.md` §6.7 (amended per §4.1 of this ADR). `docs/focus-modes/README.md` is updated to v0.4 to reflect the acceptance. If this ADR and `directory-rules.md` ever diverge after the §6.7 amendment lands, **`directory-rules.md` wins**; open a PR to amend this ADR or supersede it, do not amend `directory-rules.md` to match a stale ADR text.

---

**ADR ID:** ADR-0028 · **Status:** `proposed` · **Date:** 2026-05-23 · **Owners:** focus-mode steward, directory-rules steward, schema steward, sensitivity reviewer · **Last reviewed:** 2026-05-23 · [↑ Back to top](#top)

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs/domains/people-dna-land/SOURCE_REGISTRY
title: People / DNA / Land Domain — Source Registry
type: standard
version: v1
status: draft
owners: TODO — people-dna-land domain steward; source-registry steward; rights-holder representative; sensitivity reviewer; release authority
created: 2026-05-19
updated: 2026-06-07
policy_label: restricted
related:
  - docs/domains/people-dna-land/README.md
  - docs/domains/people-dna-land/SOURCE_LEDGER.md
  - docs/domains/people-dna-land/SOURCE_FAMILIES.md
  - docs/domains/people-dna-land/SENSITIVITY_PROFILE.md
  - docs/runbooks/people-dna-land/SOURCE_REFRESH_RUNBOOK.md
  - docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - directory-rules.md
  - schemas/contracts/v1/source/source-descriptor.json
  - schemas/contracts/v1/consent/consent_sidecar.schema.json
  - data/registry/sources/people-dna-land/
  - policy/domains/people-dna-land/
  - policy/consent/people/
  - policy/sensitivity/people/
tags: [kfm, people, dna, land, genealogy, source-registry, governance, admission, sensitivity, consent]
notes:
  - CONTRACT_VERSION = "3.0.0".
  - Human-facing control surface, not the machine-readable registry; not a bibliography; not a publication authority; not a substitute for consent.
  - This domain carries the highest publication-sensitivity posture in KFM. T4 (Denied) is the default for living-person fields, raw DNA segments, and private person-parcel joins.
  - CONFLICTED — folder slug people-dna-land vs Atlas name "People / Genealogy / DNA / Land"; canonical lane name is unsettled (deep-research slug-drift register; Atlas §24.13). Slug is PROPOSED, not CONFIRMED. Resolve by ADR. See OQ-PDL-REG-01.
  - CONFLICTED — SOURCE_REFRESH_RUNBOOK belongs under docs/runbooks/ per Directory Rules §6.1.b, not docs/domains/. See OQ-PDL-REG-02.
  - Consent does NOT publish data — a ConsentSidecar constrains a render gate; publication still requires ReleaseManifest + Promotion Gate G.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# 👥 People / DNA / Land Domain — Source Registry

> Human-facing admission and authority-control surface for source families the **People / Genealogy / DNA / Land Ownership** domain may admit, quarantine, restrict, or deny. **Not a bibliography. Not the truth store. Not a publication authority. Not a substitute for consent.**

![status: draft](https://img.shields.io/badge/status-draft-orange)
![doc type: standard](https://img.shields.io/badge/doc--type-standard-blue)
![domain: people--dna--land](https://img.shields.io/badge/domain-people--dna--land%20(PROPOSED)-6a1b9a)
![lifecycle: admission](https://img.shields.io/badge/lifecycle-admission-555)
![default tier: T4 denied](https://img.shields.io/badge/default--tier-T4%20Denied-b71c1c)
![consent: required](https://img.shields.io/badge/consent-required-c2185b)
![contract: v3.0.0](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-blue)
![ci: TODO](https://img.shields.io/badge/ci-TODO-lightgrey)
![last updated: 2026--06--07](https://img.shields.io/badge/last%20updated-2026--06--07-informational)

**Status:** draft &middot; **Owners:** TODO — people-dna-land domain steward; source-registry steward; rights-holder representative; sensitivity reviewer; release authority &middot; **Updated:** 2026-06-07
**Pinned:** `CONTRACT_VERSION = "3.0.0"`

> [!CAUTION]
> This is the **highest-sensitivity domain in KFM**. Living-person fields, raw DNA segments/kit tokens, and private person↔parcel joins default to **T4 — Denied**. Listing a source here is an admission-control act, **not** a publication grant and **not** a substitute for consent. Consent constrains a render gate; it does not publish data.

---

## Contents

1. [Purpose](#1-purpose)
2. [Repo fit](#2-repo-fit)
3. [What belongs here · Exclusions](#3-what-belongs-here--exclusions)
4. [The sensitivity boundary](#4-the-sensitivity-boundary)
5. [Source families](#5-source-families)
6. [Source-role discipline (anti-collapse)](#6-source-role-discipline-anti-collapse)
7. [SourceDescriptor field surface](#7-sourcedescriptor-field-surface)
8. [Sensitivity tiers and allowed transforms](#8-sensitivity-tiers-and-allowed-transforms)
9. [Consent, revocation, and DNA-specific controls](#9-consent-revocation-and-dna-specific-controls)
10. [Admission flow](#10-admission-flow)
11. [Pipeline shape](#11-pipeline-shape)
12. [Cross-lane relations](#12-cross-lane-relations)
13. [Anti-patterns and named denials](#13-anti-patterns-and-named-denials)
14. [Verification backlog and open questions](#14-verification-backlog-and-open-questions)
15. [Related docs](#15-related-docs)
16. [Appendix · Per-family admission notes](#16-appendix--per-family-admission-notes)

---

## 1. Purpose

This document is the **human-facing source registry** for the People / DNA / Land domain. It tells stewards, reviewers, and contributors:

- which **source families** the domain may admit and under what discipline;
- which **source roles** each family can legitimately carry (and which it cannot);
- what **rights, sensitivity, consent, and release class** apply at admission;
- which **publication tiers** are the default, and what governed transforms can lower a tier;
- which **anti-patterns** are blocked at the trust membrane.

It is paired with — and **does not replace** — the machine-readable registry under `data/registry/sources/people-dna-land/` (PROPOSED path; NEEDS VERIFICATION) and the canonical `SourceDescriptor` schema home under `schemas/contracts/v1/source/source-descriptor.json` (PROPOSED per Directory Rules §7.4 and ADR-0001; NEEDS VERIFICATION). It also pairs with the lane's [`SOURCE_LEDGER.md`](./SOURCE_LEDGER.md) (instance-level "what each source cannot prove") and [`SOURCE_FAMILIES.md`](./SOURCE_FAMILIES.md) (family→role taxonomy).

> [!IMPORTANT]
> **CONFIRMED doctrine.** The source registry is an **admission and authority-control surface**, not a bibliography. It exists to ensure source material is admitted, quarantined, restricted, or denied **before** it can shape public claims — never after. [DIRRULES; ENCY]

[↑ back to top](#top)

---

## 2. Repo fit

| Aspect | Value | Status |
|---|---|---|
| Proposed path | `docs/domains/people-dna-land/SOURCE_REGISTRY.md` | PROPOSED — Directory Rules §6 / §12 domain-lane pattern |
| Owning root | `docs/` (human-facing control plane) | CONFIRMED rule |
| Domain segment | `people-dna-land/` inside `docs/domains/` | PROPOSED — slug unsettled (see callout) |
| Doc class | Standard (KFM Meta Block v2 applies) | CONFIRMED |
| Upstream doctrine | `[DOM-PEOPLE]`, `[ENCY]`, `[DIRRULES]`, `[GAI]` | CONFIRMED |
| Downstream artifacts | `data/registry/sources/people-dna-land/` · `policy/domains/people-dna-land/` · `policy/consent/people/` · per-source descriptors · `SourceActivationDecision` records | PROPOSED |
| Pair documents | `README.md` · `SOURCE_LEDGER.md` · `SOURCE_FAMILIES.md` · `SENSITIVITY_PROFILE.md` · `SOURCE_REFRESH_RUNBOOK.md` | PROPOSED — NEEDS VERIFICATION |

> [!WARNING]
> **Slug is PROPOSED, not CONFIRMED (CONFLICTED → ADR).** A prior draft asserted the `people-dna-land` slug was "CONFIRMED by Directory Rules §6.1" with a "canonical illustration." Project evidence does not support that: Directory Rules illustrates domain lanes with `hydrology/ soil/ fauna/`, and the corpus slug-drift register records the People lane's canonical externally-presented name as **unsettled** — Atlas §16 names it "People / Genealogy / DNA / Land," schema/policy paths use `people/`, and `people-dna-land` appears only as a docs-slug variant. Treat the slug as PROPOSED until an ADR settles it; until then all cross-references resolve to this slug provisionally. Tracked as `OQ-PDL-REG-01`. [DIRRULES §6, §12; ATLAS §24.13; deep-research slug-drift register]

> [!WARNING]
> **Runbook placement conflict (CONFLICTED → ADR).** The related `SOURCE_REFRESH_RUNBOOK` is listed under `docs/domains/people-dna-land/` in earlier drafts, but Directory Rules §6.1.b makes `docs/runbooks/` the canonical home for operational procedures (source refresh explicitly named), with Pattern A (`docs/runbooks/people-dna-land/SOURCE_REFRESH_RUNBOOK.md`) matching the existing fauna runbook. This registry now points at the `docs/runbooks/` location. Tracked as `OQ-PDL-REG-02`. [DIRRULES §6.1.b, §18 OPEN-DR-02]

[↑ back to top](#top)

---

## 3. What belongs here · Exclusions

### Belongs here

- Source families that **carry person, genealogy, DNA, or land-instrument evidence** relevant to Kansas territory and Kansas-resident lineage.
- Source-role discipline notes for each family (which roles a family may carry; which it may not).
- Rights, sensitivity, consent, and release-class tagging at the family level.
- Pointers to per-source `SourceDescriptor` entries in `data/registry/sources/people-dna-land/` (PROPOSED).
- Activation status (`allowed`, `restricted`, `denied`, `needs-review`) — never inferred from data availability alone.

### Does **not** belong here

| Topic | Lives where instead | Citation |
|---|---|---|
| The `SourceDescriptor` JSON Schema | `schemas/contracts/v1/source/source-descriptor.json` (PROPOSED) | [DIRRULES §7.4 / ADR-0001] |
| The `ConsentSidecar` JSON Schema | `schemas/contracts/v1/consent/consent_sidecar.schema.json` (PROPOSED) | [Pass-23 KFM-P5-PROG-0005] |
| Policy decisions on allow/deny/restrict | `policy/domains/people-dna-land/`, `policy/consent/people/`, `policy/sensitivity/people/` | [DIRRULES §6.5] |
| Consent render gate logic | `policy/consent/render.rego` (PROPOSED) | [Pass-23 KFM-P5-PROG-0007] |
| Tests proving admission/redaction enforcement | `tests/domains/people-dna-land/` | [DIRRULES §4 Step 1] |
| Connector/watcher implementations | `connectors/<vendor>/` (e.g., GEDmatch, Ancestry, FamilyTreeDNA) | [DIRRULES §7.3] |
| Pipeline executable code | `pipelines/domains/people-dna-land/` | [DIRRULES §7.4] |
| Released catalog/publication artifacts | `data/catalog/domain/people-dna-land/`, `data/published/layers/people-dna-land/` | [DIRRULES §9.1] |
| Settlements, roads, archaeology, hydrology, agriculture sources | Their own domain `SOURCE_REGISTRY.md` files | [DOM-PEOPLE §B] |
| Frontier Matrix aggregate population panels | `docs/domains/frontier-matrix/` (PROPOSED domain segment) | [ENCY §17] |

> [!CAUTION]
> Settlements, roads, archaeology, hydrology, agriculture, hazards, and Spatial Foundation **provide context** to this domain — but they **do not weaken** living-person, DNA, title, or parcel-boundary controls. A context citation never lowers a sensitivity tier. [DOM-PEOPLE §B; CONFIRMED]

[↑ back to top](#top)

---

## 4. The sensitivity boundary

People / DNA / Land is the **highest-sensitivity domain in KFM**. Every source family in this registry is admitted under the assumption that **denial is the default**, and any tier reduction (T4 → T3 → T2 → T1 → T0) must be earned by a recorded, reviewable transform.

> [!WARNING]
> **CONFIRMED invariant.** Living-person output and DNA-derived outputs are **denied or restricted by default**; raw kit/vendor IDs and DNA segments are **not public**; assessor/tax records and parcel geometry are **not title truth**. Unclear rights, unresolved source role, missing evidence, unresolved sensitivity, or absent release state **blocks** public promotion. [DOM-PEOPLE §I; ENCY; DIRRULES]

### Four boundary claims this registry preserves

1. **Living-person fields fail closed.** Aggregation by tract or county with an `AggregationReceipt` is the only governed path from T4 to T1 for living-person attributes. [DOM-PEOPLE; Atlas §24.5.2 PROPOSED]
2. **Raw DNA segments and kit tokens are not public.** No transform releases raw DNA segments to T0 or T1. T3 only under named research agreement with a `ConsentGrant`, `ReviewRecord`, and `PolicyDecision`. [DOM-PEOPLE; Atlas §24.5.2 PROPOSED]
3. **Assessor and tax rolls are not title truth.** They are `administrative` compilations. Title authority lives in deeds, patents, and probate instruments — `observed` (instrument) or `regulatory` (recording layer), never collapsed. [DOM-PEOPLE; Atlas §24.1 anti-collapse]
4. **Parcel geometry is not title-boundary proof.** Plat / survey / metes-and-bounds / PLSS / subdivision geometry is `observed` (survey) or `derived`, not a title instrument. Boundary claims require a corresponding `LandInstrument`. [DOM-PEOPLE §C, §I; CONFIRMED doctrine]

[↑ back to top](#top)

---

## 5. Source families

The domain dossier `[DOM-PEOPLE §D]` enumerates six broad source families. Each is admitted family-wide here; individual sources within a family receive their own `SourceDescriptor`. **All `Activation` values below are PROPOSED until verified against a mounted registry; all per-source rights are NEEDS VERIFICATION (Atlas §16.D leaves them unverified).**

| # | Family | Typical examples | Carried roles (PROPOSED) | Default tier (PROPOSED) | Activation (PROPOSED) | Citation |
|---|---|---|---|---|---|---|
| 1 | **Vital / cemetery / burial / obituary / church / school / military / census / directory / court / probate records** | KS vital statistics; KSHS cemetery indexes; FamilySearch obituary collections; church registers; school censuses; military service files; decennial census; county directories; court dockets; probate files | `observed` (life event) · `administrative` (compilation) · `aggregate` (census tabulation) | T1 (historical/non-living) · **T4 (living-person fields)** | needs-review | [DOM-PEOPLE §D] |
| 2 | **GEDCOM / GEDZip / family-tree overlays** | User-submitted GEDCOM/GEDZip; Ancestry/FamilySearch/MyHeritage/WikiTree exports; researcher tree fragments | `candidate` (assertions for review) · `context` | T4 default; T2 reviewer where rights and living-flags resolved | needs-review | [DOM-PEOPLE §D] |
| 3 | **DNA vendor match CSV / segment / triangulation data** | AncestryDNA matches; 23andMe DNA Relatives exports; MyHeritage cM/segment data; FamilyTreeDNA chromosome browser exports; GEDmatch one-to-many / segment exports | `observed` (match measurement) · `modeled` (relationship hypothesis) · `candidate` | **T4 default. T3 only under named consent.** Raw segments never reach T0/T1. | denied by default | [DOM-PEOPLE §D; Pass-10 C9-03] |
| 4 | **Patent / deed / mortgage / lien / easement / lease / mineral / water / access / probate instruments** | BLM GLO land patents; county Register of Deeds filings; mortgage / lien records; easement & right-of-way grants; mineral & water severance; probate decrees | `observed` (instrument) · `regulatory` (recording-statute layer) | T0 (post-conveyance instruments, no living-person fields) · T2 (sensitive joins) | needs-review | [DOM-PEOPLE §D; Atlas §24.1] |
| 5 | **Assessor and tax-roll records** | County assessor parcel rolls; tax payment ledgers; valuation records | `administrative` (compilation) — **never** `observed` (title) | T1 (historical) · T2 (current with owner names) · T4 (joined to living-person identity) | needs-review | [DOM-PEOPLE §D; Atlas §24.1] |
| 6 | **Plat / survey / metes-and-bounds / PLSS / subdivision / derived geometry** | BLM **CadNSDI** (canonical present-day PLSS); BLM **GLO** scanned plats and field notes (historical layer); county plats; private surveys; subdivision filings | `observed` (survey monument) · `modeled` (computed geometry) · `regulatory` (recorded plat) | T0 (CadNSDI public layer) · T1 (derived geometry without owner) · T2 (joined to person) | allowed (CadNSDI/GLO) · needs-review (county/private) | [Atlas §24.1; Pass-23 KFM-P2-IDEA-0016] |

> [!NOTE]
> **Kansas cadastral spine (CONFIRMED named sources / PROPOSED admission).** BLM CadNSDI provides the canonical present-day PLSS; GLO scanned plats and field notes provide the historical survey layer. They are joined on township/range/section keys with watcher-fail-closed on key ambiguity, and original strings retained for audit. CadNSDI answers *"what does the present-day cadastre say"*; GLO answers *"what did the original survey find."* They are **not** merged into one source role. [Pass-23 KFM-P2-IDEA-0016; KFM-P2-PROG-0011]

> [!NOTE]
> **Role-vocabulary note.** Earlier drafts listed `model` and `derived` as source roles. The canonical seven-value enum (Atlas §24.1.1) uses **`modeled`** (not `model`); there is no separate `derived` role — computed/derived geometry carries `modeled`. This table uses the canonical spellings. [ENCY §24.1.1]

### Family-level rights and freshness summary

| Family | Rights / sensitivity | Freshness cadence | Status |
|---|---|---|---|
| Vital / cemetery / obituary / church / school / military / census / directory / court / probate | rights and current terms **NEEDS VERIFICATION** per source; sensitive joins fail closed; living-person fields T4 | source-vintage; episodic for current records | [DOM-PEOPLE §D] CONFIRMED doctrine |
| GEDCOM / GEDZip / tree overlays | rights and current terms **NEEDS VERIFICATION** per submitter; living-flag enforcement at ingest; deletion-on-request supported | submission-driven | [DOM-PEOPLE §D] CONFIRMED doctrine |
| DNA vendor match / segment / triangulation | rights and current terms **NEEDS VERIFICATION** per vendor TOS; consent token required; revocation introspected on every render; vendor-solvency variable per Pass-10 C9-03/C9-07 | vendor cadence; consent state checked live | [DOM-PEOPLE §D; Pass-10 C9-03, C9-07] |
| Patent / deed / mortgage / lien / easement / lease / mineral / water / access / probate instruments | rights and current terms **NEEDS VERIFICATION** per recording jurisdiction | episodic / on-record | [DOM-PEOPLE §D] |
| Assessor and tax-roll records | rights and current terms **NEEDS VERIFICATION** per county; living-person joins T4 | annual roll cadence; current-roll restricted | [DOM-PEOPLE §D] |
| Plat / survey / metes-and-bounds / PLSS / subdivision / derived geometry | rights and current terms **NEEDS VERIFICATION** per source; CadNSDI public-safe; private surveys T2 | CadNSDI rolling; GLO archival | [DOM-PEOPLE §D] |

[↑ back to top](#top)

---

## 6. Source-role discipline (anti-collapse)

Source role is **set at admission and never edited in place**. Corrections produce a new `SourceDescriptor` and a `CorrectionNotice`. The People / DNA / Land domain is the locus of **several of KFM's named source-role collapse risks** — all are DENY at the trust membrane. [ENCY §24.1]

### The seven `source_role` values (CONFIRMED enum, Atlas §24.1.1)

| Role | Meaning here | People/DNA/Land example |
|---|---|---|
| `observed` | A direct observation, instrument record, or measurement | A recorded deed; a death certificate; a DNA segment measurement |
| `regulatory` | An authoritative determination/layer issued by a governing or recording body | A recorded plat issued by a county Register of Deeds |
| `modeled` | A derivation produced by a defined model with a `ModelRunReceipt` | A relationship hypothesis derived from cM and segment counts; computed parcel geometry |
| `aggregate` | A roll-up bound to a named geometry scope and time unit | A decadal county population from the census |
| `administrative` | A compilation produced for administrative/registration/accounting use | An assessor's parcel roll; a probate court calendar |
| `candidate` | A pending assertion awaiting validation, dedup, or review | A GEDCOM-imported person record before steward review |
| `synthetic` | Generated content with a Reality Boundary Note | An AI-drafted narrative; never an instrument or title |

### Named collapses that DENY at the trust membrane

| Collapse | Cited domains | Membrane decision | Mitigation | Citation |
|---|---|---|---|---|
| **Aggregate cited as per-place truth.** Decadal county population used to describe a household. | People/DNA/Land, Agriculture, Geology, Air | **DENY** at the join; **ABSTAIN** at AI. | `AggregationReceipt` + geometry-scope guard + matrix-cell semantics. | [Atlas §24.1.2; DOM-PEOPLE] |
| **Administrative compilation cited as observation.** An assessor roll treated as a "lived event timeline." | People/Land, Settlements, Roads | **DENY** publication of compilation as an observed event series. | Source-role tag preserved; named `LifeEvent` / `AdminEvent` types. | [Atlas §24.1.2; DOM-PEOPLE] |
| **Assessor-as-title.** An assessor record used to assert title. | People/Land | **DENY** publication and AI claim. | Title remains an `observed`/`regulatory` instrument family; assessor remains `administrative`. | [DOM-PEOPLE; Atlas §24.1.2] |
| **DNA candidate exposed as confirmed relationship.** A match treated as established kinship. | People/DNA | **DENY** at the public membrane; route to QUARANTINE pending hypothesis review. | Promotion gate; relationship stays a `RelationshipHypothesis` until reviewed; no `PUBLISHED` edge until merged. | [DOM-PEOPLE; Atlas §24.1.2/24.1.3] |
| **Parcel geometry as title boundary.** A derived plat geometry used to assert a legal boundary. | People/Land | **DENY** boundary claim. | Geometry stays `observed` (survey) or `modeled`; boundary requires a `LandInstrument`. | [DOM-PEOPLE §C, §I] |
| **Promotion that upgrades role.** A `modeled` relationship promoted to `observed`. | All | **DENY** at promotion. | Source role fixed at admission; correction produces a new descriptor. | [Atlas §24.1; ENCY] |

[↑ back to top](#top)

---

## 7. SourceDescriptor field surface

PROPOSED descriptor surface for People / DNA / Land. **Schema home and field names remain PROPOSED until verified against the mounted `schemas/contracts/v1/source/source-descriptor.json`.** [DIRRULES §7.4; Atlas §24.1.3]

<details open>
<summary><strong>Role, identity, and rights fields</strong></summary>

| Field | Type / vocabulary | Required? | People/DNA/Land notes |
|---|---|---|---|
| `source_id` | stable string, kebab-cased | MUST | e.g., `kfm:source:ks-vital-statistics`, `kfm:source:blm-cadnsdi`, `kfm:source:gedmatch-segment-export`. NEEDS VERIFICATION: id convention. |
| `source_family` | enum (six families above) | MUST | One of the six families in §5. |
| `source_role` | enum: `observed` \| `regulatory` \| `modeled` \| `aggregate` \| `administrative` \| `candidate` \| `synthetic` | MUST | Set at admission; never edited in place. |
| `role_authority` | string | MUST when role ∈ {`regulatory`, `modeled`, `aggregate`} | Issuing body, model identity, or aggregation steward. |
| `role_aggregation_unit` | geometry-scope token | MUST when `source_role = aggregate` | `county`, `tract`, `township`, `decade`, etc. Prevents geometry-scope drift on join. |
| `role_model_run_ref` | EvidenceRef → `ModelRunReceipt` | MUST when `source_role = modeled` | Pins relationship-hypothesis model inputs and version. |
| `role_synthetic_basis` | `{ method, inputs, reality_boundary_note_ref }` | MUST when `source_role = synthetic` | Records what is and is not real. |
| `role_candidate_disposition` | enum: `pending`, `merged`, `rejected`, `quarantined` | MUST when `source_role = candidate` | No `PUBLISHED` edge until `merged`. |
| `rights_terms` | object: `license`, `attribution`, `redistribution`, `commercial_use`, `derived_works`, `last_reviewed` | MUST | NEEDS VERIFICATION per source; sensitive joins fail closed when unresolved. |

</details>

<details>
<summary><strong>Sensitivity, consent, and DNA fields</strong></summary>

| Field | Type / vocabulary | Required? | People/DNA/Land notes |
|---|---|---|---|
| `sensitivity_tier` | enum: `T0`, `T1`, `T2`, `T3`, `T4` | MUST | Default `T4` for any family that may carry living-person, DNA, or person-parcel fields. |
| `living_person_handling` | enum: `block`, `aggregate_then_release`, `redact_then_release`, `n/a (historical only)` | MUST | `block` is default for vital/cemetery/obituary/court/probate when the record may concern a living person. |
| `dna_class` | enum: `not_dna`, `match_count_only`, `segment_or_kit`, `raw_genotype` | MUST when family is DNA-adjacent | `raw_genotype` and `segment_or_kit` are T4 by default. |
| `consent_required` | boolean | MUST | `true` for any source that may carry living-person or DNA-derived content. |
| `consent_sidecar_ref` | content-address (sidecar_digest) | MUST when `consent_required = true` | Points at the `ConsentSidecar` the render gate consumes (§9). Consent does not publish; it constrains a render. [Pass-23 KFM-P5-PROG-0005] |
| `consent_token_kind` | enum: `none`, `sdjwt_vc`, `ga4gh_passport`, `ldp_vc_bbs2023` | MUST when `consent_required = true` | Token carries scopes, audience, expiry, revocation endpoint, consent-history hash. [Pass-10 C6-07; Pass-23 KFM-P5-PROG-0006] |
| `revocation_endpoint` | URL (Bitstring Status List) | MUST when `consent_token_kind ≠ none` | Introspected on every render; fail-closed (ABSTAIN) on unreachable. Cache TTL ~30s. [Pass-10 C6-08; Pass-23 KFM-P5-PROG-0006] |
| `vendor_solvency_class` | enum: `n/a`, `solvent`, `at_risk`, `distressed`, `bankrupt`, `wound_down` | MUST when family = DNA vendor | Tracks vendor TOS continuity; informs retention and revocation drills. [Pass-10 C9-07] |

</details>

<details>
<summary><strong>Cadence, attribution, integrity, and time fields</strong></summary>

| Field | Type / vocabulary | Required? | People/DNA/Land notes |
|---|---|---|---|
| `cadence_class` | enum: `static`, `rolling`, `episodic`, `vendor`, `streaming` | MUST | GLO is `static`; CadNSDI is `rolling`; assessor rolls are `episodic` (annual). |
| `freshness_expectation` | duration | SHOULD | When a refresh becomes "stale" (drives the stale-source marker). |
| `attribution_required` | object: `cite_text`, `cite_url`, `display_class` | MUST when `rights_terms.attribution = true` | Used by the governed API and the MapLibre Evidence Drawer. |
| `release_class` | enum: `public`, `reviewer`, `restricted`, `denied`, `needs-review` | MUST | Matches the activation decision in §10. |
| `ingest_hash` | bytes hex (BLAKE3 / SHA-256) | MUST | Tamper-evidence over the bytes admitted. |
| `time` | object: `source_time`, `observed_time`, `valid_time`, `retrieval_time`, `release_time`, `correction_time` | MUST | All six remain distinct where material. [DOM-PEOPLE §E] |
| `citation` | structured citation block | MUST | Renders in Evidence Drawer. |

</details>

[↑ back to top](#top)

---

## 8. Sensitivity tiers and allowed transforms

KFM publishes only the safest representation that still answers the steward's and the public's reasonable needs. **Tier defaults are CONFIRMED doctrine for this domain; tier transforms are PROPOSED until OPA rules and review queues are verified in the mounted repo.** [ENCY §24.5; DOM-PEOPLE §I]

| Object class | Default tier | Allowed transforms (PROPOSED) | Required gates | Reversibility |
|---|---|---|---|---|
| Living-person fields (name, current address, contact, age, identifiers) | **T4** | Aggregation by tract or county + `AggregationReceipt` → T1 | Consent **or** aggregation gate + `ReviewRecord` | Reversible: correction may demote a T1 to T4. |
| Raw DNA segment data / kit tokens / chromosome browser exports | **T4** | **No transform releases this to a public tier.** T3 only under explicit research agreement. | Named `ConsentGrant` + `ReviewRecord` + `PolicyDecision` | Reversible on revocation: returns to T4 with `CorrectionNotice` and `RevocationReceipt`. |
| Match-count-only DNA evidence (cM totals, shared-segment counts, no coordinates) | T3 | k-anonymized aggregate of match populations → T1 with `RedactionReceipt` | `ConsentGrant` + `ReviewRecord` | Reversible on consent revocation. |
| Relationship hypotheses (`modeled`) | T2 | Generalize to relationship class (e.g., "close cousin range") + redact identifiers → T1 | `ModelRunReceipt` + `RedactionReceipt` + `ReviewRecord` | Reversible. |
| Private person-parcel join | **T4** | Generalized parcel geometry + de-identified person → **T2 only** | `RedactionReceipt` + `ReviewRecord` | Reversible. |
| Historical person records (decedent confirmed; rights resolved) | T1 | None required for public release | Standard release gate | Standard. |
| Land instruments (deeds, patents, probates; no living-person fields) | T0 | None required | Standard release gate | Standard. |
| Assessor / tax-roll record with current-owner name | T2 (current) · T1 (historical) | Redact owner identity → T1; aggregate by parcel-class → T0 | `RedactionReceipt` or `AggregationReceipt` + `ReviewRecord` | Reversible. |
| CadNSDI PLSS public layer | T0 | None | Standard release gate | Standard. |
| GLO historical plats / field notes (raster + OCR) | T0 | None for the imagery; OCR text marked `candidate` until reviewed | Standard release gate; OCR `role_candidate_disposition` until merged | Standard. |

Tier transitions follow the master allowed-motion ladder: a tier **upgrade** (toward more public) needs *both* a transform receipt *and* a `ReviewRecord`; a tier **downgrade** (toward less public) needs only a `CorrectionNotice`. Each step is reversible; T1 → T0 supports rollback via `RollbackCard`. [ENCY §24.5.3]

> [!WARNING]
> The tier system is **operational, not advisory**. A tier reduction without the named artifact and reviewer is a doctrine violation, regardless of how plausible the public-safety story sounds.

[↑ back to top](#top)

---

## 9. Consent, revocation, and DNA-specific controls

People / DNA / Land is the only KFM domain in which **consent enforcement is part of every render**, not only every publication. This section names the rules; implementation lives in `policy/consent/people/` (PROPOSED) and the consent render gate `policy/consent/render.rego` (PROPOSED package `policy.consent.render`). [Pass-23 KFM-P5-PROG-0007]

> [!IMPORTANT]
> **Consent does NOT publish data (CONFIRMED doctrine).** A `ConsentSidecar` is a *constraint package* — it bounds what a render gate is allowed to materialize. Publication still requires a `ReleaseManifest` and Promotion Gate G approval. A consent token is never, by itself, a release authority. [Pass-23 KFM-P5-PROG-0005]

### ConsentSidecar (PROPOSED, Pass-23 KFM-P5-PROG-0005)

An immutable, content-addressed JSON object pairing a holder Verifiable Credential with a DSSE-signed consent receipt and a Bitstring Status List entry. Suggested home: `schemas/contracts/v1/consent/consent_sidecar.schema.json`. It carries a finite consent `scope ∈ {public_render, generalize_render, restricted_render, review_required}`, retention metadata with `expires_at`, and a list of sensitivity-class redaction obligations enforced at render time.

### ConsentDecision render gate (PROPOSED, Pass-23 KFM-P5-PROG-0007)

For each render, `policy.consent.render` consumes the sidecar plus a request context (actor, audience, requested_scope, now) and emits a finite `ConsentDecision` combining four checks:

| Outcome | Trigger | Surface behavior |
|---|---|---|
| `ALLOW` | DSSE envelope valid · Bitstring Status List non-revoked · requested scope ⊆ allowed scope · `now < retention.expires_at` | Render permitted with obligations propagated. |
| `DENY` | Any single check fails (default is deny) | Render blocked; default-deny outcome recorded. |
| `ABSTAIN` | Partial / unresolved evidence (e.g., status-list lookup unreachable) | Render withheld; **fail-closed-but-not-misclassified**. |
| `ERROR` | System error during evaluation | Render withheld; incident logged. |

> [!NOTE]
> A render that was `ALLOW` at request time is delivered even if the status list flips mid-render (the decision was correct at the time); **subsequent** renders `DENY`. Status-list lookups are cached with a short TTL (~30s). [Pass-23 KFM-P5-PROG-0006/0007]

### DNA vendor controls

- **Vendor capability and TOS registry** (PROPOSED): per-vendor record of raw-data download support, match/segment export, API limits, and privacy requirements. [Pass-23 KFM-P18-PROG-0023]
- **Vendor solvency tracking**: `vendor_solvency_class` per descriptor; vendor-loss-simulation drill cited as suggested future work post the 23andMe Chapter 11 filing (March 2025). [Pass-10 C9-03, C9-07]
- **DTC raw-genomic export rule**: raw direct-to-consumer files are **high-sensitivity assets**, stored only in encrypted storage with strict access scoping; **never republished**. Only k-anonymized or differentially-private aggregate derivatives may cross the publication boundary, and only under a documented consent scope. [Pass-10 C9-03]

### Revocation and erasure

- Revocation MUST be honored at the render gate, not only at the next publication cycle; revocation is a status-list bit flip, not a row mutation. [Pass-23 KFM-P5-PROG-0007]
- On revocation: issue a signed tombstone, append a new `spec_hash` and `RunReceipt` to the ledger, and trigger cache-invalidation hooks (PMTiles index bump, tile-server purge) so previously rendered tiles do not survive. [Pass-10 C6-08]
- The boundary between **tombstone** (record retained for explainability, contents nulled) and **erasure** (record removed) is an open question; right-to-be-forgotten obligations may require true deletion. Tracked as `OQ-PDL-REG-15`. [Pass-10 C6-08]
- A `RevocationReceipt` is emitted for every honored revocation and is auditable. [DOM-PEOPLE §C]

> [!IMPORTANT]
> **CONFIRMED doctrine.** AI may summarize **released** People / DNA / Land `EvidenceBundle` content, compare evidence, explain limitations, and draft steward-review notes. AI MUST **ABSTAIN** when evidence is insufficient and **DENY** where policy, rights, sensitivity, or release state blocks the request. AI is never the root truth source for this domain. [GAI; DOM-PEOPLE §L]

[↑ back to top](#top)

---

## 10. Admission flow

PROPOSED source-activation flow, drawn from CONFIRMED doctrine. The watcher MUST NOT publish or rewrite catalog; it emits a `SourceIntakeRecord` / `RunReceipt`, after which admission decisions follow. [IMPL-PIPE §13; DIRRULES §13 watcher-as-non-publisher]

1. **Propose** a new or updated `SourceDescriptor` (this registry receives a new row in §5).
2. **Review** source role, rights, sensitivity, cadence, access, and consent requirements.
3. **Resolve** rights and sensitivity; for DNA-adjacent sources, resolve consent posture and vendor TOS.
4. **Issue** a `SourceActivationDecision`: one of `allowed`, `restricted`, `denied`, `needs-review`.
5. **Stand up** fixtures, validators, and policy gates **before** any connector or watcher becomes active.
6. **Activate** the connector / watcher only after fixtures, validators, and policy gates exist and pass.
7. **Refresh** on cadence per the [`SOURCE_REFRESH_RUNBOOK`](../../runbooks/people-dna-land/SOURCE_REFRESH_RUNBOOK.md); emit `SourceIntakeRecord` and `ValidationReport` every tick.
8. **Re-evaluate** annually, or earlier on rights change, vendor TOS change, vendor distress, consent change, or doctrinal change.

### Activation decision matrix

| Outcome | Meaning | Downstream effect |
|---|---|---|
| `allowed` | Family may admit; per-source review applies | Connector eligible to run; pipeline gated by per-source `SourceDescriptor` |
| `restricted` | Family may admit only under named conditions (consent, redaction, generalization) | Connector eligible but `release_class ≠ public` until conditions verified |
| `denied` | Family rejected | No connector; no admission; no descriptor beyond a denial record |
| `needs-review` | Family unresolved | No admission; queued for steward and rights-holder review |

[↑ back to top](#top)

---

## 11. Pipeline shape

The People / DNA / Land lane follows the KFM lifecycle invariant. **Promotion is a governed state transition, not a file move.** [DIRRULES; DOM-PEOPLE §H]

```mermaid
flowchart LR
    A["External source<br/>(vital · GEDCOM · DNA vendor ·<br/>instrument · assessor · plat/PLSS)"] -->|"watcher tick"| B["RAW<br/>data/raw/people-dna-land/&lt;source_id&gt;/&lt;run_id&gt;/<br/>(PROPOSED path)"]
    B --> C{"Admission gate<br/>SourceDescriptor +<br/>rights + sensitivity +<br/>consent (if applicable)"}
    C -->|"pass"| D["WORK<br/>normalize · identity ·<br/>living-flag screen ·<br/>consent check"]
    C -->|"fail"| Q["QUARANTINE<br/>reason recorded ·<br/>RIGHTS_UNKNOWN ·<br/>SENSITIVITY_UNRESOLVED ·<br/>CONSENT_MISSING"]
    D --> E{"Validation +<br/>policy gate<br/>(role discipline ·<br/>tier check)"}
    E -->|"pass"| F["PROCESSED<br/>validated objects ·<br/>receipts ·<br/>public-safe candidates"]
    E -->|"fail"| Q
    F --> G["CATALOG / TRIPLET<br/>EvidenceBundle ·<br/>graph projection ·<br/>release candidate"]
    G --> H{"Release decision<br/>ReleaseManifest +<br/>review state +<br/>rollback target"}
    H -->|"approve"| P["PUBLISHED<br/>governed API ·<br/>Evidence Drawer ·<br/>Focus Mode (cite-or-abstain)"]
    H -->|"hold"| R["HELD CASE<br/>reviewable; AI ABSTAINs<br/>citing the held case"]
    P -.->|"consent revocation"| X["RevocationReceipt +<br/>CorrectionNotice +<br/>RollbackCard"]
    X --> Q

    classDef sens fill:#fce4ec,stroke:#c2185b,color:#880e4f;
    classDef ok fill:#e8f5e9,stroke:#2e7d32,color:#1b5e20;
    classDef gate fill:#fff8e1,stroke:#f9a825,color:#5d4037;
    classDef quar fill:#ffebee,stroke:#b71c1c,color:#7f0000;
    class B,D,F,G ok;
    class C,E,H gate;
    class Q,R,X sens;
    class P sens;
```

> [!NOTE]
> Diagram is illustrative of the **governed flow shape**, not a route map of the mounted repo. Path `data/raw/people-dna-land/<source_id>/<run_id>/` follows Directory Rules §9.1 and §4 Step 3 patterns; **PROPOSED until verified.**

[↑ back to top](#top)

---

## 12. Cross-lane relations

This domain consumes from and feeds context to other lanes. Every relation must preserve ownership, source role, sensitivity, and `EvidenceBundle` support. [DOM-PEOPLE §F; Atlas §24.4.14]

| Owner | Related lane | Relation type | Constraint |
|---|---|---|---|
| People / DNA / Land | Settlements | residence · cemetery · school · court · county · township · place | Living-person fields fail closed; residence anchors settlement membership only via reviewed assertion. |
| People / DNA / Land | Roads / Rail | migration · access · movement | Migration-path uncertainty preserved; never published as exact route for a living person. |
| People / DNA / Land | Archaeology | historic person · land · documentary · cultural-place context | Cultural affiliations cited with rights, sovereignty, and steward review. Sovereignty review can elevate to T4. |
| People / DNA / Land | Agriculture | farm · land use · producer-adjacent context | `LandParcel` context may bound field-candidate joins; **private person-parcel joins denied by default.** |
| People / DNA / Land | Frontier Matrix | aggregate population observations feed matrix cells | Matrix cell ≠ per-place truth; `AggregationReceipt` enforces geometry-scope guard. |
| People / DNA / Land | Governed AI / Focus Mode | summarization of **released** `EvidenceBundle` only | AI never reads RAW or WORK content; cite-or-abstain at every render. |

[↑ back to top](#top)

---

## 13. Anti-patterns and named denials

The trust membrane DENIES these patterns regardless of how the request is phrased. People / DNA / Land is the lane in which most of these collapses are tempting; the membrane is non-negotiable. [Atlas §24.1.2, §24.9; DOM-PEOPLE §I; ENCY]

| Anti-pattern | Membrane decision | Why |
|---|---|---|
| Treat assessor or tax roll as title authority | DENY publication; ABSTAIN at AI | Administrative compilation ≠ observed instrument. |
| Treat parcel geometry as legal boundary | DENY boundary claim | Geometry is `observed`/`modeled`; boundary requires a `LandInstrument`. |
| Promote a DNA candidate match to confirmed kinship | DENY at promotion gate | `candidate` role never edges to `PUBLISHED` until `merged`. |
| Join an aggregate cell to a single living person | DENY join; ABSTAIN at AI | Aggregate ≠ per-place truth. |
| Publish a living-person field without consent or aggregation | DENY at trust membrane | T4 default; only `AggregationReceipt` or `ConsentGrant` path opens lower tiers. |
| Republish raw DNA segment data | DENY at trust membrane | No transform path exists from raw segments to T0/T1. |
| Cite a GEDCOM tree as observation | DENY upgrade of role | Tree overlays are `candidate` or `context`, never `observed`. |
| Treat a `ConsentSidecar` as a release authority | DENY | Consent constrains a render; publication still requires `ReleaseManifest` + Promotion Gate G. |
| Use the admin path as a public path to bypass the trust membrane | DENY at infra | Admin shortcuts must be justified, constrained, documented, and audited; deny-by-default infra. |
| Re-publish a corrected claim without invalidating derivatives | DENY publication | `CorrectionNotice` must list invalidated derivatives; `RollbackCard` if needed. |
| Let AI text stand in for an `EvidenceBundle` | DENY at every Focus Mode surface | Cite-or-abstain; `AIReceipt` mandatory; release state required. |
| Honor a stale consent token at render | DENY/ABSTAIN at render gate | Revocation introspected on every render; fail-closed when introspection cannot complete. |

[↑ back to top](#top)

---

## 14. Verification backlog and open questions

CONFIRMED carry-forward from `[DOM-PEOPLE §N]` plus this revision's surfaced conflicts. Each item resolves when mounted-repo evidence supplies it (files, schemas, registry entries, tests, logs, review records, release manifests).

| # | Item | Evidence that would settle it | Status |
|---|---|---|---|
| 1 | Verify living-person policy implementation | `policy/domains/people-dna-land/` + tests | NEEDS VERIFICATION |
| 2 | Verify DNA consent / revocation enforcement at render | `policy/consent/render.rego` + tests + render integration | NEEDS VERIFICATION |
| 3 | Verify land-instrument chain logic | `contracts/domains/people-dna-land/` + chain-of-title / gap tests | NEEDS VERIFICATION |
| 4 | Verify geometry-role boundary logic | tests denying parcel-geometry-as-title-boundary | NEEDS VERIFICATION |
| 5 | Verify UI / API restricted-field no-leak behavior | governed-API contract tests + Evidence Drawer redaction tests | NEEDS VERIFICATION |
| 6 | Verify person-assertion evidence tests | `tests/domains/people-dna-land/` | NEEDS VERIFICATION |
| 7 | Verify GEDCOM import rights / living-flag tests | fixtures + tests | NEEDS VERIFICATION |
| 8 | Verify DNA consent and raw-ID no-log tests | logging audits + redaction tests | NEEDS VERIFICATION |
| 9 | Verify revocation cleanup tests | revocation drill artifacts | NEEDS VERIFICATION |
| 10 | Verify legal-description and chain-of-title gap tests | fixtures + tests | NEEDS VERIFICATION |
| 11 | Verify assessor-as-title denial | OPA rule + tests | NEEDS VERIFICATION |
| 12 | Verify graph-projection safety tests | tests denying sensitive triplet leakage | NEEDS VERIFICATION |
| 13 | Confirm Kansas vital-statistics, KSHS, BLM CadNSDI, BLM GLO source IDs | mounted registry | NEEDS VERIFICATION |
| 14 | Confirm per-vendor DNA TOS watchers | `connectors/<vendor>/` | NEEDS VERIFICATION |

### Open questions register

| ID | Question | Owner role | Resolution path |
|---|---|---|---|
| OQ-PDL-REG-01 | Is the canonical lane slug `people-dna-land`, or the Atlas name "People / Genealogy / DNA / Land" (schema/policy use `people/`)? | Docs steward + domain steward | ADR + Directory Rules / Atlas §24.13 |
| OQ-PDL-REG-02 | Does `SOURCE_REFRESH_RUNBOOK` live at `docs/runbooks/people-dna-land/` (Directory Rules §6.1.b) or beside the dossier? | Architecture steward + docs steward | ADR + §6.1.b / §18 OPEN-DR-02 |
| OQ-PDL-REG-15 | Tombstone-vs-erasure boundary for revoked DNA/personal records | Rights & Sovereignty reviewer | ADR + `docs/runbooks/revocation.md` |
| OQ-PDL-REG-16 | Multi-party consent shape (family claim where several living relatives have stake) | Consent / PDP owner | ConsentSidecar schema extension |

> [!TIP]
> When in doubt, **add the row, mark the status**. A documented unknown is part of the system; an undocumented assumption is a drift waiting to bite.

[↑ back to top](#top)

---

## 15. Related docs

PROPOSED targets. `NEEDS VERIFICATION` until each target exists in the mounted repo.

- [`docs/domains/people-dna-land/README.md`](./README.md) — domain landing (PROPOSED)
- [`docs/domains/people-dna-land/SOURCE_LEDGER.md`](./SOURCE_LEDGER.md) — instance-level "what each source cannot prove" (PROPOSED)
- [`docs/domains/people-dna-land/SOURCE_FAMILIES.md`](./SOURCE_FAMILIES.md) — family→role taxonomy (PROPOSED)
- [`docs/domains/people-dna-land/SENSITIVITY_PROFILE.md`](./SENSITIVITY_PROFILE.md) — tier disposition + revocation path (PROPOSED)
- `docs/runbooks/people-dna-land/SOURCE_REFRESH_RUNBOOK.md` — operations (PROPOSED; relocated per §6.1.b — OQ-PDL-REG-02)
- `docs/sources/SOURCE_DESCRIPTOR_STANDARD.md` — cross-cutting descriptor doctrine (PROPOSED)
- `docs/domains/archaeology/SOURCE_REGISTRY.md` · `docs/domains/habitat/SOURCE_REGISTRY.md` · `docs/domains/hazards/SOURCE_REGISTRY.md` — neighboring sensitive-lane precedent (authored prior session; presence NEEDS VERIFICATION)
- `docs/runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md` — operational template (authored prior session; presence NEEDS VERIFICATION)
- `docs/standards/PROV.md` — provenance crosswalk (authored prior session; naming-variance pending ADR per Directory Rules §18 OPEN-DR-01)
- `directory-rules.md` — placement and lifecycle authority (CONFIRMED)
- `schemas/contracts/v1/source/source-descriptor.json` — canonical schema home (PROPOSED per ADR-0001; NEEDS VERIFICATION)
- `schemas/contracts/v1/consent/consent_sidecar.schema.json` — consent sidecar schema (PROPOSED)
- `policy/domains/people-dna-land/` · `policy/consent/people/` · `policy/sensitivity/people/` — policy homes (PROPOSED)
- `data/registry/sources/people-dna-land/` — machine-readable registry (PROPOSED)

[↑ back to top](#top)

---

## 16. Appendix · Per-family admission notes

<details>
<summary><strong>Family 1 — Vital · cemetery · obituary · church · school · military · census · directory · court · probate records</strong></summary>

- **Carried roles:** `observed` (life event), `administrative` (compilation), `aggregate` (census tabulation), `context` (county directory listings).
- **Living-person handling:** `block` by default for vital records (birth, marriage, current address) until decedency or consent resolves; `aggregate_then_release` for census-class data only via tract/county aggregation with `AggregationReceipt`.
- **Rights:** Per-jurisdiction; KS vital-statistics access rules NEEDS VERIFICATION. State-archive holdings often release after long windows; current records typically blocked. KSHS cemetery indexes typically released; verify per index.
- **Anti-pattern:** A county directory (administrative compilation) cited as observation of where a person lived. The compilation date is not the residence date.
- **Activation:** `needs-review` family-wide; per-source review required.

</details>

<details>
<summary><strong>Family 2 — GEDCOM / GEDZip / family-tree overlays</strong></summary>

- **Carried roles:** `candidate` (assertions for review), `context` (researcher background). **Never** `observed`.
- **Living-flag enforcement at ingest:** GEDCOM `_PRIV` and Ancestry "Living Person" flags MUST be honored; absence does not imply consent.
- **Rights:** Per-submitter; trees may incorporate copyrighted sources (newspapers, books, photos) without rights resolution. Watcher fails closed when rights are unresolved.
- **Anti-pattern:** Promoting a tree-asserted relationship to a confirmed kinship. Trees are `candidate` until a steward merges them.
- **Activation:** `needs-review` family-wide; submitter-by-submitter review.

</details>

<details>
<summary><strong>Family 3 — DNA vendor match / segment / triangulation data</strong></summary>

- **Carried roles:** `observed` (the measurement itself), `modeled` (relationship hypothesis from cM and segment counts), `candidate` (unmerged match).
- **Vendor universe (Pass-10 C9-03 / KFM-P18-PROG-0023):** AncestryDNA, 23andMe, MyHeritage, FamilyTreeDNA, GEDmatch. Per-vendor TOS, raw-data download, segment export, and API limits MUST be recorded in the vendor capability registry.
- **Consent:** REQUIRED. Token kind: `sdjwt_vc`, `ga4gh_passport`, or `ldp_vc_bbs2023`. Revocation introspected on every render via Bitstring Status List.
- **Raw genotype:** Never republished. Encrypted storage with strict access scoping. Only k-anonymized or DP-aggregated derivatives cross the publication boundary, and only under explicit consent scope.
- **Vendor solvency:** Tracked per source; cite the 23andMe Chapter 11 filing (March 2025) as the canonical "vendor distress" precedent. Run vendor-loss-simulation drills.
- **Anti-pattern:** Treating a high-cM segment as confirmed kinship. The segment is `observed`; the kinship is `modeled` and stays a `RelationshipHypothesis` until reviewed.
- **Activation:** `denied` by default; per-vendor, per-kit `restricted` only with consent in place.

</details>

<details>
<summary><strong>Family 4 — Patent · deed · mortgage · lien · easement · lease · mineral · water · access · probate instruments</strong></summary>

- **Carried roles:** `observed` (the instrument), `regulatory` (the recording-statute layer).
- **Title authority lives here.** Assessor records do not.
- **Rights:** Public-record default; abstract-of-title services may carry licensing; verify per source.
- **Anti-pattern:** Inferring title from an unrecorded instrument or a recital in a later deed. Recital ≠ instrument.
- **Activation:** `needs-review` family-wide; allowed for most county Register-of-Deeds feeds after rights resolution.

</details>

<details>
<summary><strong>Family 5 — Assessor and tax-roll records</strong></summary>

- **Carried role:** `administrative`. **Never** `observed` (title) or `regulatory`.
- **Default tier:** T2 (current) · T1 (historical, decedent-only) · T4 (joined to living person).
- **Refresh cadence:** Annual roll cycles; assessor data is `episodic`, not `streaming`.
- **Anti-pattern:** Assessor-as-title. DENY at trust membrane; ABSTAIN at AI.
- **Activation:** `needs-review` per county; allowed when historical-only and de-identified.

</details>

<details>
<summary><strong>Family 6 — Plat · survey · metes-and-bounds · PLSS · subdivision · derived geometry</strong></summary>

- **Carried roles:** `observed` (survey monument), `modeled` (computed geometry), `regulatory` (recorded plat).
- **Cadastral spine:** BLM **CadNSDI** is the canonical present-day PLSS source; BLM **GLO** scanned plats and field notes are the historical layer. Joined on township/range/section keys; watcher fails closed on key ambiguity. [KFM-P2-IDEA-0016; KFM-P2-PROG-0011]
- **GLO legal-description normalization:** Parse township/range/section; normalize to county by **historical** boundary time slice; retain raw legal description for audit.
- **Imagery:** GLO raster outputs stored as COG with WMTS/XYZ or IIIF deep-zoom delivery; high-res originals archived.
- **Anti-pattern:** Parcel geometry as title boundary. Geometry stays `observed` or `modeled`; boundary claim requires a `LandInstrument` (Family 4).
- **Activation:** `allowed` for CadNSDI and GLO (public layers); `needs-review` for county and private surveys.

</details>

---

## Footer

> [!TIP]
> If something in this registry feels approximate, that is a feature: every PROPOSED row is a verification candidate. File evidence into `docs/registers/VERIFICATION_BACKLOG.md` (PROPOSED) and replace the label, do not erase it.

**Related docs:** [§15](#15-related-docs)
**Last updated:** 2026-06-07
**Version:** v1 (draft) · **Pinned** `CONTRACT_VERSION = "3.0.0"`

[↑ back to top](#top)

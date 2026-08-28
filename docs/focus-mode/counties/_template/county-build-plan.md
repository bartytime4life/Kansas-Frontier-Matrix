<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/focus-mode-county-build-plan-template
title: County Focus Mode Build-Plan Authoring Template
type: template
version: v2.0-draft
status: draft; authoring-aid; compatibility-lane; validator-contract-conflicted; non-publication
owners:
  - "@bartytime4life — current CODEOWNERS review route"
  - "NEEDS VERIFICATION — Focus architecture, evidence, policy, sensitivity, release, and county-scope stewardship"
created: 2026-05-23
updated: 2026-08-20
policy_label: public; documentation-template; county-scope; cite-or-abstain; non-authoritative
owning_root: docs/
responsibility: Provide a reusable county Focus Mode planning scaffold while keeping current path, schema, validator, policy, release, and publication uncertainty explicit.
truth_posture: CONFIRMED current repository surfaces and accepted placement principles / PROPOSED county-plan grammar and control-plane convergence / NEEDS VERIFICATION destination path, parser contract, payload admission, policy binding, release, and governed consumers
evidence_snapshot: "bartytime4life/Kansas-Frontier-Matrix main@7ef962c606beabd9119d0aae283171839f806093; prior target blob 327c6304cd5301a38c9e086610be12725f3fabf7"
related:
  - docs/focus-mode/README.md
  - docs/focus-mode/counties/COUNTY_INDEX.md
  - docs/adr/ADR-0027-county-focus-mode-control-plane.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - contracts/focus_mode/focus_mode_payload.md
  - schemas/contracts/v1/focus/README.md
  - schemas/contracts/v1/ui/map_context_envelope.schema.json
  - policy/focus/README.md
  - tools/validators/validate_focus_mode_index.py
  - tools/validators/validator_registry.json
notes:
  - "This same-path revision changes documentation only; it does not select or create a canonical Focus documentation lane."
  - "The fenced YAML in section 12 is retained as a compatibility authoring scaffold. Current validate_focus_mode_index.py does not parse it."
  - "No county plan, payload, policy decision, release, deployment, or publication is created by copying this file."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# County Focus Mode — Build-Plan Authoring Template

> **Purpose.** Help an author describe one county-scale Focus composition without turning a planning document into evidence, policy, machine admission, release authority, or publication proof.

> [!IMPORTANT]
> This tracked file is an **authoring aid in the current singular documentation lane**. It is not the canonical county-plan schema. Accepted Directory Rules v2 defines a county or Focus Mode as a composition scope, but it does not select an exact Focus documentation subtree. Proposed ADR-0027 discusses a plural replacement lane; it is not accepted. Do not create, move, or rename a county lane from this template alone.

> [!CAUTION]
> The current county-index validator and this template do not agree. `validate_focus_mode_index.py` targets `docs/focus-modes/`, expects YAML front matter and seven exact filenames, and does **not** parse the fenced block in section 12. The validator is also not registered in the current validator registry. A copied plan must not claim validator success until that contract is reconciled and a pinned run actually passes.

## Status and authority boundary

| Surface | Current repository evidence | What this template may claim |
|---|---|---|
| Current file | Present at `docs/focus-mode/counties/_template/county-build-plan.md` | Reusable documentation scaffold only |
| Placement | Accepted Directory Rules v2 §12.4 says county and Focus Mode are composition scopes; exact Focus docs path remains unresolved | Same-path editing is valid; structural migration remains on hold |
| County control-plane decision | ADR-0027 is `proposed` | Design input, not adopted authority |
| County index | Present as a collision-prevention/planning register with mixed maturity | Prevent duplicate selection; does not prove lane completeness |
| Semantic payload contract | `contracts/focus_mode/focus_mode_payload.md` exists and is marked `PROPOSED` | Crosswalk candidate only |
| Machine payload admission | No `schemas/contracts/v1/focus_mode/focus_mode_payload.schema.json` or `validate_focus_mode_payload.py` at the inspected base | `NEEDS VERIFICATION`; never imply schema-valid payload state |
| Focus policy | Policy files exist, while the Focus README says the policy is inactive | Planning defaults only; no operational enforcement claim |
| Release/publication | No county release evidence is established by this file | None; a plan, test, PR, or merge is not publication |

## How to use this template safely

1. Check the county index and repository for an existing county claim before drafting.
2. Resolve the writable destination against accepted Directory Rules, current path evidence, and any accepted successor to ADR-0027. If no decision closes the path, revise an existing same-path artifact or hold creation.
3. Replace every placeholder and every `PROPOSED — fill` prompt with county-specific, source-backed content. Keep `UNKNOWN` and `NEEDS VERIFICATION` visible.
4. Reference shared source, evidence, contract, schema, policy, fixture, registry, and release objects; do not copy them into the county documentation lane.
5. Build the support packet by **responsibility closure**, not by assuming seven files are universally required. The Focus README §13 is the current human guidance.
6. Run only validators that actually cover the chosen path and grammar. Record the command, version or commit, result, and negative fixtures.
7. Keep the plan at `draft` until evidence, rights, sensitivity, contract, validation, review, correction, and rollback dependencies are closed for the claimed use.

> [!NOTE]
> Preserve the explicit section anchors below when instantiating or revising a plan. They keep existing references stable while the control-plane grammar remains under review.

## Contents

- [1. Slice scope](#1-slice-scope)
- [2. Geographic and temporal frame](#2-geographic-and-temporal-frame)
- [3. Domains in scope](#3-domains-in-scope)
- [4. Source-seed signals](#4-source-seed-signals-summary)
- [5. Layer plan](#5-layer-plan-summary)
- [6. Evidence model](#6-evidence-model-summary)
- [7. Public-safety posture](#7-public-safety-posture-summary)
- [8. Promotion path](#8-promotion-path)
- [9. Acceptance criteria](#9-acceptance-criteria-reference)
- [10. Open questions](#10-open-questions)
- [11. Cross-references](#11-cross-references)
- [12. Candidate plan data](#12-plan-data-block-validator-input)
- [Appendix A. Copy-and-review checklist](#appendix-a-copy-and-review-checklist)
- [Appendix B. Truth labels](#appendix-b-truth-labels)

---

<a id="1-slice-scope"></a>

## 1. Slice scope

**PROPOSED — fill.** In one paragraph, state:

- the county-scale questions this composition is intended to answer;
- the bounded map, time, layer, claim, and audience context;
- the finite outcomes the user can see (`ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`, where applicable to the governed surface); and
- the questions or precision it refuses to answer and why.

Do not describe a county encyclopedia, unrestricted data portal, emergency-alert service, title system, source-of-record database, or general model chat surface. A Focus Mode composes governed references for a bounded purpose; it does not become sovereign truth.

[Back to top](#top)

---

<a id="2-geographic-and-temporal-frame"></a>

## 2. Geographic and temporal frame

**PROPOSED — fill.** Describe the scope without embedding protected geometry or source payloads in this document.

| Frame field | Required authoring question | County-plan value |
|---|---|---|
| Stable scope identity | Which registered or proposed `scope_id` identifies this composition? | `PROPOSED — fill` |
| Geographic reference | Which governed boundary or released geometry reference defines the county? | `PROPOSED — fill reference; do not paste protected geometry` |
| Display CRS | Which CRS does the public map use? | `PROPOSED — fill` |
| Analysis CRS | Which CRS is used for measurement, and where is reprojection recorded? | `PROPOSED — fill` |
| Tolerance/generalization | Which reviewed transform or public-safe profile applies? | `NEEDS VERIFICATION` |
| Temporal extent | What are the earliest and latest supported observations or valid times? | `PROPOSED — fill` |
| As-of/release context | Which release or candidate snapshot bounds the view? | `PROPOSED — fill reference` |
| Refresh/freshness | What cadence and stale threshold applies per source role? | `PROPOSED — fill` |
| Temporal roles | How are source, observation, valid, retrieval, release, correction, and supersession times kept distinct? | `PROPOSED — fill` |

The current [`MapContextEnvelope` schema](../../../../schemas/contracts/v1/ui/map_context_envelope.schema.json) is relevant UI shape evidence, not proof that this county plan has been admitted to a runtime.

[Back to top](#top)

---

<a id="3-domains-in-scope"></a>

## 3. Domains in scope

Start with `not-assessed`; never make every documented domain automatically in scope. For each participating domain, cite the registered identity, source roles, evidence, rights/sensitivity posture, and reason it is necessary to the county question.

| Domain or seam | Disposition | Evidence/source role | Rights and sensitivity | County-specific rationale |
|---|---|---|---|---|
| Hydrology | `not-assessed` | `PROPOSED — fill` | `PROPOSED — fill` | `PROPOSED — fill` |
| Soil | `not-assessed` | `PROPOSED — fill` | `PROPOSED — fill` | `PROPOSED — fill` |
| Atmosphere | `not-assessed` | `PROPOSED — fill` | `PROPOSED — fill` | `PROPOSED — fill` |
| Geology | `not-assessed` | `PROPOSED — fill` | `PROPOSED — fill` | `PROPOSED — fill` |
| Fauna / flora / habitat | `not-assessed` | `PROPOSED — fill` | rare-location review required | `PROPOSED — fill` |
| Archaeology / cultural places | `not-assessed` | `PROPOSED — fill` | exact or reconstructive location fails closed | `PROPOSED — fill` |
| Settlements / infrastructure | `not-assessed` | `PROPOSED — fill` | critical-detail review required | `PROPOSED — fill` |
| Hazards | `not-assessed` | `PROPOSED — fill` | not an emergency-broadcast authority | `PROPOSED — fill` |
| Agriculture | `not-assessed` | `PROPOSED — fill` | household, farm, and private-well risks reviewed | `PROPOSED — fill` |
| People / genealogy / DNA / land | `not-assessed` | `PROPOSED — fill` | living-person, genomic, consent, and title claims fail closed | `PROPOSED — fill` |
| Roads / rail / mobility | `not-assessed` | `PROPOSED — fill` | operational and infrastructure detail reviewed | `PROPOSED — fill` |
| Cross-domain seam | `not-assessed` | `PROPOSED — registered seam ID` | inherit the most restrictive applicable posture | `PROPOSED — fill` |

Allowed dispositions should be tied to an accepted profile; until then use plain truth labels such as `PROPOSED`, `NEEDS VERIFICATION`, `HOLD`, or `not-applicable` rather than inventing an enum.

[Back to top](#top)

---

<a id="4-source-seed-signals-summary"></a>

## 4. Source-seed signals (summary)

**PROPOSED — fill.** Summarize candidate sources here and keep the authoritative identity in the source registry. Accepted Directory Rules v2 is source-first: a source is registered once and may support several domains without duplicated RAW bytes or county-owned copies.

| Source ID or candidate | Source role | Authority class | Rights/terms | Spatial and temporal coverage | Cadence/freshness | Evidence refs | Limitations/state |
|---|---|---|---|---|---|---|---|
| `PROPOSED — fill` | `authoritative / corroborating / contextual / derived` | `PROPOSED — fill` | `UNKNOWN until reviewed` | `PROPOSED — fill` | `PROPOSED — fill` | `PROPOSED — fill` | `HOLD` |

Do not infer rights from public availability, copy source records into county docs, or activate a connector from a source-seed list. A watcher may propose work; it does not publish.

[Back to top](#top)

---

<a id="5-layer-plan-summary"></a>

## 5. Layer plan (summary)

**PROPOSED — fill.** Each visible layer is a governed projection, not canonical truth. Keep detailed registry state in its owning object family and summarize references here.

| Layer candidate | Released/candidate carrier ref | Source and evidence refs | Policy/sensitivity state | Time/freshness | Public-safe transform | UI behavior | Correction/withdrawal path |
|---|---|---|---|---|---|---|---|
| `PROPOSED — fill` | `PROPOSED — fill` | `PROPOSED — fill` | `HOLD` | `PROPOSED — fill` | `NEEDS VERIFICATION` | `PROPOSED — fill` | `PROPOSED — fill` |

Required negative behavior should include missing evidence, stale or revoked carrier, policy denial, unsupported time, sensitive precision, and renderer failure. Client-side hiding is not a sensitivity control; protected data must not be delivered to a public client.

[Back to top](#top)

---

<a id="6-evidence-model-summary"></a>

## 6. Evidence model (summary)

**PROPOSED — fill.** Define only claims the county composition needs. Every consequential claim must point through an `EvidenceRef` to a resolvable `EvidenceBundle`, carry source roles and limitations, and remain correctable.

| Claim ID | Claim scope | EvidenceRef | EvidenceBundle resolution | Source roles/citations | Policy/review state | Finite result when unresolved |
|---|---|---|---|---|---|---|
| `PROPOSED — fill` | `PROPOSED — fill` | `PROPOSED — fill` | `NEEDS VERIFICATION` | `PROPOSED — fill` | `HOLD` | `ABSTAIN` or `ERROR`, as the bound contract requires |

EvidenceBundle outranks generated language. Search indexes, maps, tiles, graphs, screenshots, summaries, dashboards, tests, badges, and model output are delivery or interpretation surfaces; none substitutes for evidence closure.

[Back to top](#top)

---

<a id="7-public-safety-posture-summary"></a>

## 7. Public-safety posture (summary)

**PROPOSED — fill.** Bind the plan to accepted policy and review evidence when available. Until a governing profile is proven, use the restrictive authoring posture below; it is not a claim that current Focus policy is active.

| Concern | Restrictive authoring posture | Required closure before a less restrictive result |
|---|---|---|
| Living-person, household, genealogy, health, or identifier data | `DENY` or `ABSTAIN` | lawful purpose, consent/authority, minimization, policy, review, expiry, revocation, correction |
| DNA/genomic data | `DENY` | explicit authority and consent, purpose/audience limits, policy, revocation propagation, independent review |
| Exact/reconstructive archaeology, burial, sacred, or culturally restricted location | `DENY` | do not expose exact detail; any public-safe derivative needs separate cultural/sovereignty/rights review, transform lineage, policy, validation, release, and rollback |
| Rare species, nests, dens, roosts, or sensitive habitat location | `DENY` | accepted species/location profile, generalization or suppression, policy, negative reconstruction tests, release |
| Critical or exploitable infrastructure and active operations | `DENY` | audience/purpose limit, approved generalization, security review, policy, release |
| Parcel/title, private well, or private-land inference | `ABSTAIN` or `DENY` | source-role and legal review, de-identification, policy, correction path |
| Emergency alert or current hazard instruction | `ABSTAIN` | defer users to the named authoritative emergency source; KFM does not become the alert authority |
| Unknown rights, terms, sovereignty, sensitivity, or audience | `HOLD`, `ABSTAIN`, or `DENY` | missing authority resolved and recorded |

Record every transformation and residual inference risk. Do not disclose protective thresholds, seeds, buffers, grids, or reconstruction recipes in a public plan when that detail could weaken the control.

[Back to top](#top)

---

<a id="8-promotion-path"></a>

## 8. Promotion path

A county plan is upstream planning evidence, not a lifecycle transition. Use the current release and promotion documents for the exact executable vocabulary; do not copy the older source-to-publication A–G labels from prior versions of this template as if they were the current gate contract.

| Stage | Required evidence | Failure posture | What completion does not prove |
|---|---|---|---|
| Scope and source identity | Stable scope/source references, roles, coverage, limitations | `HOLD` / `ABSTAIN` | rights or public fitness |
| Rights and sensitivity | Terms, consent/authority, sovereignty/cultural review, audience, precision posture | `DENY` / `HOLD` | schema or evidence closure |
| Evidence and contract closure | Resolving EvidenceRefs/Bundles, citations, contract/schema validation, finite negatives | `ABSTAIN` / `DENY` / `ERROR` | independent approval or release |
| Catalog/provenance closure | Traceable carrier, provenance, time, transforms, integrity, correction lineage | `HOLD` | publication |
| Independent review and release decision | Accountable review, applicable promotion evidence, manifest, correction and rollback targets | `DENY` / `HOLD` | deployment or public serving |
| Governed delivery | Released public-safe artifact or governed API response, cache/correction/withdrawal behavior | fail closed | universal truth or permanence |

Promotion is a governed state transition, not a file move, status string, pull request, merge, badge, validator pass, GitHub release, deployment, or model assertion.

[Back to top](#top)

---

<a id="9-acceptance-criteria-reference"></a>

## 9. Acceptance criteria reference

Build the checklist from the observable outcome and direct dependencies. Do not assume that eight legacy literals or seven documentation filenames are an accepted universal contract.

| Acceptance item | State | Evidence or negative proof | Accountable review | Recheck trigger |
|---|---|---|---|---|
| Scope identity and county collision are closed | `not-run` | `PROPOSED — fill` | `NEEDS VERIFICATION` | scope, path, or index change |
| Every participating domain and source role is justified | `not-run` | `PROPOSED — fill` | `NEEDS VERIFICATION` | domain/source change |
| Every visible layer has carrier, evidence, policy, sensitivity, time, and correction references | `not-run` | `PROPOSED — fill` | `NEEDS VERIFICATION` | layer or policy change |
| Every consequential claim resolves or returns the required finite negative outcome | `not-run` | `PROPOSED — fill` | `NEEDS VERIFICATION` | evidence/contract change |
| Rights, privacy, sovereignty, cultural sensitivity, and harmful precision are fail-closed | `not-run` | `PROPOSED — fill valid and invalid fixtures` | `NEEDS VERIFICATION` | source, audience, transform, or policy change |
| Runtime and UI consume only governed/released public-safe surfaces | `not-run` | `PROPOSED — fill` | `NEEDS VERIFICATION` | route, adapter, or consumer change |
| Validation is deterministic, no-network where practical, and includes exact negative cases | `not-run` | `PROPOSED — command, commit, report` | `NEEDS VERIFICATION` | validator/tool/profile change |
| Review, release, correction, withdrawal, and rollback are bound | `not-run` | `PROPOSED — fill` | `NEEDS VERIFICATION` | release or public-reliance change |

Allowed checklist states must come from the chosen validator or contract. Until one is bound, use `not-run`, `pass`, `fail`, `error`, or an explicit truth label consistently and explain the source of that vocabulary.

[Back to top](#top)

---

<a id="10-open-questions"></a>

## 10. Open questions

Do not hide path, schema, policy, source, or release uncertainty in prose. Give each material item a stable local ID and a concrete closure condition.

| ID | Question or conflict | Truth label | Blocking surface | Resolves when |
|---|---|---|---|---|
| `FM-<county>-01` | `PROPOSED — fill` | `NEEDS VERIFICATION` | `PROPOSED — fill` | `specific evidence, decision, or test` |

Escalate to an ADR or accepted migration record when a change would alter canonical path, identity, index/template grammar, contract/schema authority, policy outcome semantics, public API boundary, release authority, or another cross-root responsibility boundary.

[Back to top](#top)

---

<a id="11-cross-references"></a>

## 11. Cross-references

| Reference | Current role | Status at inspected base |
|---|---|---|
| [Focus Mode documentation lane](../../README.md) | Current lane evidence, responsibility-closure guidance, migration hold | Current; non-canonical path decision remains unresolved |
| [County index](../COUNTY_INDEX.md) | Collision-prevention and planning register | Present; implementation maturity is not proven |
| [ADR-0027](../../../adr/ADR-0027-county-focus-mode-control-plane.md) | Proposed county control-plane decision and convergence plan | `PROPOSED`; not acceptance authority |
| [ADR-0029](../../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Accepted adoption of exact Directory Rules v2 bytes | `ACCEPTED` placement authority |
| [Directory Rules v2](../../../doctrine/directory-rules.md) | Responsibility-root, scope, naming, dependency, migration, and rollback law | Adopted exact bytes via ADR-0029 |
| [FocusModePayload semantic contract](../../../../contracts/focus_mode/focus_mode_payload.md) | Proposed plan-to-payload semantics | Present; proposed and internally stale |
| [Focus schema family](../../../../schemas/contracts/v1/focus/README.md) | Current Focus request/response/runtime schema boundary | Present; not a county payload schema |
| [MapContextEnvelope schema](../../../../schemas/contracts/v1/ui/map_context_envelope.schema.json) | Bounded UI map-context shape | Present; runtime binding not established by this plan |
| [Focus policy README](../../../../policy/focus/README.md) | Current policy inventory and limitations | Present; policy described as inactive |
| [County index validator](../../../../tools/validators/validate_focus_mode_index.py) | Proposed plural-lane/index validator | Present; grammar/path mismatch with current lane/template |
| [Validator registry](../../../../tools/validators/validator_registry.json) | Current orchestration inventory | Focus index validator not registered at inspected base |
| [UI Focus flow](../../../architecture/ui/FOCUS_FLOW.md) | Governed Focus interaction and negative-state architecture | Documentation evidence only |
| [Publication promotion gates](../../../architecture/publication/promotion-gates.md) | Current bounded promotion-readiness vocabulary and conflict notes | Non-authoritative architecture; release remains held |

[Back to top](#top)

---

<a id="12-plan-data-block-validator-input"></a>

## 12. Plan data block (compatibility authoring scaffold)

> [!WARNING]
> **Not current validator input.** This single fenced YAML block is retained so existing template users and proposed contract work have a visible migration target. On the inspected `main`, `validate_focus_mode_index.py` searches YAML front matter instead and does not parse this fence. No schema at the former `schemas/contracts/v1/focus_mode/focus_mode_payload.schema.json` path exists. Do not call this block valid, canonical, or payload-ready.

Keep the legacy top-level keys stable until ADR-0027 or a successor accepts one grammar and synchronized contract, schema, validator, fixtures, and migration. Placeholder values are deliberately invalid as county claims.

```yaml
# === KFM Focus Mode Build Plan: compatibility plan data (NOT CURRENTLY ADMITTED) ===
schema_version: "1"                         # candidate lineage only; no current machine admission
kfm_artifact: "focus_mode_build_plan"       # proposed semantic family
area:
  county: "<County Name>"
  lane: "<county-lane-after-path-decision>" # do not infer canonical placement from this template
  scope: "county"
status: "draft"                             # documentation state; not release state
owner: "<OWNER>"
priority: "<P1|P2|P3-or-governing-profile>"
last_reviewed: "YYYY-MM-DD"
plan_anchors:
  - "docs/doctrine/directory-rules.md#124-geography-and-focus-mode"
  - "docs/focus-mode/README.md"
  - "docs/adr/ADR-0027-county-focus-mode-control-plane.md"
ui_shell: "apps/explorer-web"               # shell identity only; no per-county code path is inferred
canonical_paths:                             # fill only from verified owning-root authority
  ui_lane: "<NEEDS VERIFICATION>"
  fixtures: "<NEEDS VERIFICATION>"
  source_registry_refs: "<NEEDS VERIFICATION>"
  published_payload: "<NEEDS VERIFICATION>"
  release_manifest: "<NEEDS VERIFICATION>"
sensitivity_lanes:                           # restrictive authoring candidates; bind accepted policy before use
  parcel_title: "ABSTAIN"
  exact_archaeology: "DENY"
  burial_sacred: "DENY"
  rare_species_exact: "DENY"
  critical_infrastructure_exact: "DENY"
  living_person_identifiers: "DENY"
  dna_genomic: "DENY"
  emergency_alert: "ABSTAIN"
sensitivity_overrides: []                    # expected default; any exception needs separate authority and negatives
source_seed_families: []                     # source IDs/roles belong in the authoritative registry
required_layers_min: 0                       # planning counter only
required_layers_with_policy_decision: 0      # planning counter only
evidence_refs_resolved: 0                    # planning counter only
evidence_refs_total: 0                       # zero is not closure for a claim-bearing plan
release:
  promotion_gates_passed: []                 # do not populate from legacy labels without the bound profile
  release_manifest_id: null
  rollback_target_id: null
  correction_path: null
adr_open_questions:
  - "FM-CONTROL-PLANE-GRAMMAR"               # remove only after accepted grammar and migration evidence
# === end compatibility plan data ===
```

[Back to top](#top)

---

<a id="appendix--glossary-and-template-legend"></a>
<a id="appendix-a-copy-and-review-checklist"></a>

## Appendix A. Copy-and-review checklist

- [ ] Existing county claims, aliases, branches, and pull requests were checked for overlap.
- [ ] The destination path has an accepted placement basis; otherwise creation remains on hold.
- [ ] Template metadata was replaced with a county-plan identity without changing this template's identity.
- [ ] Every placeholder and `PROPOSED — fill` prompt was resolved or kept visibly unresolved.
- [ ] Scope, source roles, evidence, rights, sensitivity, audience, time, and limitations are explicit.
- [ ] No protected coordinates, private payloads, credentials, signed URLs, or harmful precision were copied into docs.
- [ ] Claims resolve through EvidenceRef to EvidenceBundle or surface the required negative state.
- [ ] UI and AI paths use governed/released public-safe interfaces, not canonical/internal stores.
- [ ] Positive and exact-negative fixtures cover evidence, policy, sensitivity, time, runtime, and correction failures.
- [ ] The validation command actually covers the chosen path and data grammar at a pinned commit.
- [ ] Reviewer, release, correction, withdrawal, and rollback evidence is referenced rather than inferred.
- [ ] The plan makes no release, deployment, publication, or public-safety claim beyond evidence.

### What a passing documentation check does not prove

A clean Markdown render, valid metadata block, resolving link set, parser success, or green pull-request check proves only the bounded check at the inspected revision. It does not prove source authority, evidence sufficiency, rights, privacy, cultural or sovereignty review, policy activation, runtime enforcement, independent approval, release, deployment, publication, correction propagation, or operational rollback.

[Back to top](#top)

---

<a id="appendix-b-truth-labels"></a>

## Appendix B. Truth labels

| Label | Use in a county plan |
|---|---|
| `CONFIRMED` | Verified in the current review from pinned repository evidence, a supplied admissible artifact, or a named authoritative source |
| `PROPOSED` | Requested design, candidate source, path, mapping, behavior, or future state not established as current |
| `UNKNOWN` | Evidence is unavailable or insufficient |
| `NEEDS VERIFICATION` | A specific check can settle the claim but has not yet been completed strongly enough |
| `HOLD` | A required authority, evidence, rights, sensitivity, policy, review, migration, or release dependency prevents the next transition |

## Revision history

| Date | Version | Change | Non-effect |
|---|---|---|---|
| 2026-05-23 | initial lineage | Created the county build-plan template | No county release or publication |
| 2026-05-24 | v1 lineage | Added Focus control-plane paths and proposed validator data | Proposal only |
| 2026-08-20 | v2.0-draft | Reconciled the template with current Directory Rules, Focus README, ADR-0027 status, schema inventory, validator behavior, and release boundary | No path migration, contract/schema/policy change, validator admission, release, deployment, or publication |

---

**Current path:** `docs/focus-mode/counties/_template/county-build-plan.md` · **Role:** compatibility-lane authoring aid · **Updated:** 2026-08-20 · [Back to top](#top)

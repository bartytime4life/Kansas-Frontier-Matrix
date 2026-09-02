<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/focus-mode/counties/haskell-county/readme
title: Haskell County Focus Mode Planning Lane
type: readme
version: v1.1
status: draft; repository-grounded; planning-only; compatibility-lane; non-release; non-publication
owners:
  - "NEEDS VERIFICATION — Focus Mode stewardship"
  - "NEEDS VERIFICATION — groundwater and water-administration review"
  - "NEEDS VERIFICATION — currentness, legal-boundary, rights, privacy, sensitivity, and release review"
created: 2026-08-21
updated: 2026-08-22
policy_label: public; documentation; county-scope; compatibility; cite-or-abstain; water-right-sensitive; groundwater-currentness-sensitive; privacy-sensitive; operational-precision-sensitive
owning_root: docs/
responsibility: >-
  Orient maintainers to the Haskell County planning artifacts tracked in the
  singular Focus Mode compatibility lane; expose their administrative-water,
  water-right, lawful-use, currentness, private-well and farm, evidence, and
  public-safety limits; and provide a review path without creating source,
  contract, schema, policy, lifecycle, release, deployment, or publication
  authority.
authority: >-
  Human-readable navigation and boundary documentation only. This README and
  its linked build plan do not determine current water-right standing or lawful
  use, admit sources, resolve evidence, activate policy, validate a payload,
  provide current groundwater or drought guidance, approve a release, deploy a
  product, or publish a claim.
truth_posture: >-
  CONFIRMED current repository path, one-byte predecessor, two-file directory,
  current main snapshot, linked build plan, current county-index finding, and
  accepted directory-governance decision / PROPOSED Haskell County proof-slice
  scope, source candidates, cards, layers, reason codes, interfaces, fixtures,
  reviewers, and implementation sequence derived from the linked build plan /
  UNKNOWN source admission, rights, external-fact freshness, scientific fitness,
  safe geometry, EvidenceRef-to-EvidenceBundle closure, policy outcomes,
  runtime behavior, accountable reviewers, release, correction propagation,
  rollback execution, deployment, and public parity / NEEDS VERIFICATION every
  county lifecycle, water-right, lawful-use, groundwater-currentness,
  private-operation, operational-precision, and public-use claim.
current_path: docs/focus-mode/counties/haskell_county/README.md
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 9656da3c88b9a21b844179ecc97a52136bb5799d
  target_prior_blob: 8b137891791fe96927ad78e64b0aad7bded08bdc
  build_plan_blob: 502eb7795822abab3c15056b617072e6ed4c43ff
  county_index_blob: 07e9b65cab9c4fd4ae31b61a84fecb06c6cde655
  focus_mode_readme_blob: 8600c0ac09452b4b03e5f60b94f1eb27c072b5db
  county_lane_readme_blob: 48621badd51614db7bff0882c19096fa388234ac
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  adr_0027_blob: 4dfb29c963cd5662265d3cb97f98be82212d5e08
  adr_0029_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
inspection_boundary: >-
  Current-session GitHub reads covered the complete one-byte predecessor, the
  complete Haskell County build plan, the current county index and Haskell row,
  current Focus Mode documentation, accepted Directory Rules v2 through
  ADR-0029, proposed ADR-0027, and prior branch-only Haskell authoring
  lineage. External-source currentness, source records, rights
  decisions, water-right or lawful-use determinations, EvidenceBundle
  resolution, policy execution, Haskell fixtures, runtime requests, release
  records, rollback drills, deployments, and public endpoints were not
  exercised.
related:
  - docs/focus-mode/counties/haskell_county/haskell_county_focus_mode_build_plan.md
  - docs/focus-mode/counties/COUNTY_INDEX.md
  - docs/focus-mode/counties/README.md
  - docs/focus-mode/README.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0027-county-focus-mode-control-plane.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - contracts/focus_mode/focus_mode_payload.md
  - schemas/contracts/v1/focus/README.md
  - policy/focus/README.md
tags: [kfm, focus-mode, haskell-county, planning, groundwater, high-plains-aquifer, water-administration, water-right-boundary, currentness, privacy, evidence, public-safety, compatibility, non-publication]
notes:
  - "v1.1 replaces the one-byte main-branch placeholder with a current-main, same-path planning-lane boundary."
  - "The linked build plan remains a proposal and is not silently promoted or rewritten by this README."
  - "The county index remains a separately reconciled shared inventory; its Haskell one-byte finding becomes stale after this leaf change."
  - "The edit does not decide singular-versus-plural Focus documentation placement or authorize migration."
  - "Water-right, lawful-use, private-well or farm, current-supply, future-availability, and operational-precision conclusions remain outside this document's authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Haskell County Focus Mode

> **Purpose.** Orient maintainers to the Haskell County planning lane, make its
> water-right, lawful-use, groundwater-currentness, private-operation,
> operational-precision, and evidence boundaries visible, and route future work
> through KFM source, evidence, policy, review, release, correction, and rollback
> controls.

> [!IMPORTANT]
> **Tracked planning artifacts are not implementation, adjudication, approval,
> or release evidence.** This directory contains this README and one Haskell
> County build plan. Their presence prevents accidental duplicate planning; it
> does not establish source admission, current water-right standing, lawful use,
> scientific correctness, validator success, runtime behavior, release,
> deployment, or publication.

> [!CAUTION]
> **Placement remains a compatibility question.** This same-path update repairs
> an existing README under `docs/focus-mode/counties/haskell_county/`.
> Accepted Directory Rules v2 governs responsibility-root placement. Proposed
> ADR-0027 describes a plural, kebab-case control plane but remains unaccepted.
> No file is moved, renamed, mirrored, copied into a parallel tree, or declared
> canonical here.

> [!WARNING]
> **Administrative water data is not a current water-right or lawful-use
> determination.** The linked plan proposes bounded, time-labeled High Plains
> aquifer, groundwater-management, and aggregate irrigation context. KFM must
> not infer whether a right is current or valid, whether it was lawfully used,
> whether a private well or farm is secure, or whether water is available now or
> in the future.

> [!WARNING]
> **Private and operational inference must fail closed.** Individual water
> records, diversion points, well locations, right-holder identity, private
> wells or farms, parcel or operation detail, current drought or supply advice,
> and vulnerability-oriented precision must not reach an ordinary public
> client. Missing authority, evidence, rights, safe geometry, temporal fitness,
> policy, review, or release closure requires `ABSTAIN`, `DENY`, or `ERROR`, not
> a fluent inference.

**Quick navigation:** [Status](#current-status) ·
[Responsibilities](#lane-responsibilities) ·
[Artifacts](#current-artifacts-and-reconciliation) ·
[Planning scope](#proposed-haskell-county-proof-slice) ·
[Water authority](#administrative-water-and-source-role-boundary) ·
[Safety](#public-safety-and-governed-outcomes) ·
[Readiness](#evidence-and-readiness-boundary) ·
[Follow-up](#smallest-safe-follow-up) ·
[Open questions](#open-questions) ·
[References](#cross-references-and-maintenance)

---

<a id="current-status"></a>

## Current status

| Field | Repository-grounded state |
|---|---|
| County | Haskell County, Kansas |
| Current lane | `docs/focus-mode/counties/haskell_county/` — existing singular compatibility tree |
| README role | Human navigation, scope, administrative-water boundary, and public-safety documentation |
| Directory inventory | This README plus `haskell_county_focus_mode_build_plan.md` |
| Main-branch predecessor | One UTF-8 newline byte; blob `8b137891791fe96927ad78e64b0aad7bded08bdc` |
| Shared county-index finding | `README_1_BYTE`; becomes stale when this leaf update lands and requires separate full-index reconciliation |
| Build-plan state | Present; substantial; planning-only; semantic, source, water-right, currentness, privacy, and release claims remain `NEEDS VERIFICATION` |
| County lifecycle | `NEEDS VERIFICATION` — no lifecycle state is assigned by this document |
| Executable county validation | `NOT_RUN` — this documentation change does not validate a `FocusModePayload` or county runtime |
| Accountable owner and independent reviewers | `NEEDS VERIFICATION`, including groundwater/water-administration, legal-boundary, currentness, rights/privacy, sensitivity, security/accessibility, and release review |
| Source, rights, evidence, policy, runtime, correction, rollback, release, deployment, publication | `NOT_RUN` or `UNKNOWN`; no positive state inferred |

The [county master index](../COUNTY_INDEX.md) is a shared collision-prevention
inventory. Its Haskell one-byte finding describes the pinned predecessor state.
This leaf README does not partially rewrite the high-churn 105-county snapshot.
`README_1_BYTE` and a future `TRACKED_PAIR` are inventory findings only; neither
is a payload, maturity, validation, water-right, lawful-use, promotion, release,
or publication state.

[Back to top](#top)

---

<a id="lane-responsibilities"></a>

## Lane responsibilities

### This README owns

- orientation to the current Haskell County documentation lane;
- links to the current planning artifact and inherited Focus Mode controls;
- explicit truth, water-right, lawful-use, temporal-fitness, privacy,
  operational-precision, public-interface, correction, and rollback boundaries;
- visible open questions and review triggers for future Haskell County work.

### This README does not own

| Object or decision family | Required owning surface or boundary |
|---|---|
| Current water-right standing, lawful use, priority, allocation, permits, compliance, or legal conclusions | Responsible legal and administrative authorities and qualified decision processes; never inferred by this README |
| Current groundwater, drought, supply, emergency, or operational guidance | Current responsible authorities; not KFM planning prose or dated context |
| Source identity, authority, rights, access, cadence, effective status, and correction | KFM source registry and source-admission process; not copied into a county README |
| Canonical or admitted evidence | Governed evidence objects and lifecycle roots; not this planning directory |
| Contract meaning and machine shape | Current contract and schema responsibility roots; neither is created or accepted here |
| Sensitivity, generalization, privacy, or public-use decisions | Accepted policy plus accountable review and negative proof; prose is not enforcement |
| Private well, farm, parcel, household, operation, or future-availability conclusions | Admissible evidence and lawful accountable processes; regional and district aggregates cannot support individual inference |
| Map, AI, API, or runtime behavior | Governed implementation surfaces consuming released public-safe artifacts |
| Promotion, release, correction, withdrawal, and rollback | Their distinct governed object families and accountable decisions |

A Focus Mode composes approved references across responsibility roots. It must
not duplicate canonical water records, source records, evidence, schemas,
policy, or released artifacts merely to make a county directory appear
complete.

[Back to top](#top)

---

<a id="current-artifacts-and-reconciliation"></a>

## Current artifacts and reconciliation

| Artifact | Current role | Evidence limit |
|---|---|---|
| `README.md` | This lane orientation and boundary surface | Documentation only; no legal, scientific, machine, operational, or release authority |
| [`haskell_county_focus_mode_build_plan.md`](./haskell_county_focus_mode_build_plan.md) | Detailed proposed county proof-slice and implementation plan | Planning claims, external facts, source fitness, paths, owners, reviewers, and release readiness require current verification |
| [County master index](../COUNTY_INDEX.md) | Repository inventory and duplicate-prevention navigation | Presence, filename, and predecessor-size evidence only; Haskell row is stale after this leaf change |
| [County lane README](../README.md) | Parent navigation for the tracked county corpus | Historical control-plane claims do not override accepted Directory Rules or current repository evidence |
| [Focus Mode compatibility README](../../README.md) | Current repository-grounded Focus documentation boundary | Keeps structural convergence separate from county content work |
| [County build-plan template](../_template/county-build-plan.md) | Compatibility-lane authoring aid | Not payload admission, a water determination, or release authority |

### Build-plan reconciliation

The linked build plan predates the current same-path README repair. Its statement
that no Haskell County plan had been found is **SUPERSEDED for repository
presence only**: the plan itself is present at the path above. Its external
facts, source roles, proposed paths, cards, interfaces, fixtures, milestones,
reviewers, and release claims are not silently validated.

The plan dates its checked public sources to **2026-05-24** and records a WIMAS
snapshot date of **2026-05-10**. Those dates are plan-derived, time-bounded
research evidence. They are not current source admission, current administrative
state, a water-right determination, or a lawful-use conclusion.

### Current collision result

| Check | Result |
|---|---|
| Target directory and expected plan | `CONFIRMED` on the pinned main snapshot |
| Main-branch README | `CONFIRMED` one-byte predecessor before this change |
| Prior Haskell authoring lineage | `CONFIRMED` in prior branch-only review history; those bytes are not present on main |
| Active target-path treatment | This current-main change is the intended Haskell leaf survivor; prior branch scope must not reintroduce a competing Haskell README |
| Shared county index | Left byte-unchanged here; its Haskell row needs a separately pinned complete reconciliation |
| Safe operation | Modernize the existing README in place; do not generate another Haskell plan, migrate the lane, or publish county claims |

Search and PR metadata are bounded repository evidence, not proof that no
external workspace or private artifact exists. Recheck overlap before later
structural, implementation, or release work.

### Placement basis

Accepted ADR-0029 adopts Directory Rules v2 and makes
`docs/doctrine/directory-rules.md` the writable human placement authority. This
is a same-path update to an existing human document under `docs/`. Proposed
ADR-0027 cannot authorize a plural/kebab-case migration, and no compatibility or
parallel authority is created.

[Back to top](#top)

---

<a id="proposed-haskell-county-proof-slice"></a>

## Proposed Haskell County proof slice

The build plan proposes a public-safe learning slice around three related but
non-interchangeable concerns:

1. **Haskell County orientation** — public geographic context without parcel,
   private-well, farm, household, right-holder, or operation inference.
2. **High Plains aquifer and groundwater-management context** — regional and
   district-scale explanation without a current or future local supply,
   private-well, farm, or parcel conclusion.
3. **Administrative-data fitness and non-determination** — a visible boundary
   separating dated public records and official routing from current water-right
   standing, lawful use, legal advice, and operational guidance.

### Proposed first-slice surfaces

| Proposed surface | Intended value | Required boundary |
|---|---|---|
| `WaterDataFitnessNotice` | Explain as-of, currentness, lawful-use, and official-redirect limitations before any administrative-water answer | No current-standing, lawful-use, entitlement, compliance, or legal conclusion |
| Haskell County orientation frame | Establish a future public-safe county scope | No parcel, well, farm, household, operation, right-holder, or individual inference |
| Southwest Kansas groundwater-management context card | Explain proposed administrative geography and source role | District membership and dated context only; no right, private-operation, or current-supply inference |
| High Plains aquifer context card | Provide regional explanatory context with scale, uncertainty, and time labels | No local well condition, current supply, future availability, drought action, or property conclusion |
| District-level aggregate irrigation/use card | Teach aggregation, geography, and time scope | No silent downscaling to Haskell, a farm, a right, a well, or an operation |
| Agricultural statistics candidate | Add county-level aggregate context after query, suppression, rights, and evidence review | No producer, parcel, farm, household, water-use, or causal profile |
| Soil context candidate | Add versioned soil interpretation after area, rights, and scientific-limit review | No land value, compliance, yield, suitability, or water-availability verdict |
| Official-current redirect card | Route present drought, emergency, supply, or right-standing questions to the responsible authority | Checked-at link-out only; no cached or generated operational verdict |
| Evidence Drawer and boundary panels | Expose source role, time basis, limitations, evidence, review, and reason codes | Unresolved evidence, policy, review, or release state cannot be polished into an answer |

These are **PROPOSED planning surfaces**. No card, layer, payload, source
descriptor, evidence bundle, policy decision, route, or released artifact is
confirmed by this README.

### Deferred or denied by default

- groundwater observations, trends, models, forecasts, or future-availability
  products without admitted evidence and explicit model fitness;
- current drought, emergency, restriction, supply, or operational guidance;
- detailed management, diversion, right-holder, well, farm, parcel, household,
  or vulnerability-relevant geometry;
- current water-right standing, validity, lawful use, priority, entitlement,
  allocation, permit, compliance, or legal advice;
- aggregate downscaling into individual, farm, right, well, or operation claims;
- direct public access to `RAW`, `WORK`, `QUARANTINE`, restricted source
  material, ungoverned observations, or model output.

[Back to top](#top)

---

<a id="administrative-water-and-source-role-boundary"></a>

## Administrative water and source-role boundary

### Candidate roles named by the build plan

| Plan-named candidate | Potential role after admission and review | Must not become |
|---|---|---|
| Kansas water-administration and groundwater-management material | Institutional responsibility, public administrative geography, and official routing | A KFM water-right, lawful-use, entitlement, allocation, permit, compliance, or legal determination |
| KGS and DWR WIMAS material | Dated administrative-data context and limitation notice | A current-standing decision, proof of lawful use, or current supply answer |
| High Plains aquifer material | Scale-bounded regional explanation | A local well condition, farm outcome, present supply, future availability, or drought instruction |
| District-level aggregate material | Dated, explicitly scoped district context | A Haskell-specific value or farm, right, well, parcel, household, or operation claim |
| USDA NASS statistical material | Reviewed county-scale aggregate after admission | Producer, farm, parcel, household, pumping, causation, blame, or compliance profile |
| NRCS soil material | Versioned, area-bounded scientific context after admission | Land value, yield, compliance, suitability, groundwater, or private-operation verdict |
| Generated KFM narrative | Bounded summary of resolved, released, policy-safe evidence | Evidence, source authority, current standing, legal judgment, review, policy, or release state |

A source name in a planning document is a research lead, not an admitted
`SourceDescriptor`. Before public use, implementation must establish exact
identity, authority role, rights, access, version, as-of/effective state,
correction behavior, safe scale, geometry, aggregation, sensitivity,
provenance, review, and release eligibility.

### Time, legal, and private-operation boundary

Public administrative or scientific material may be informative while still
being unfit for an individual or current decision. A record, district page,
aquifer explanation, aggregate, soil interpretation, map feature, or observation
must not be combined into current standing, lawful use, private-well condition,
farm security, property suitability, present supply, future availability,
compliance, causation, or responsibility.

When a user asks for a current or individual determination, a public product
must return a finite reason code and a safe official route when one is
available. It must not fill an evidence gap with a model inference, map
proximity, regional average, stale record, or cross-source correlation.

### Generated-language boundary

AI may summarize only a resolved, policy-allowed, review-supported, released
public-safe evidence bundle. It cannot determine water-right standing or lawful
use, predict well/farm/groundwater/supply outcomes, infer a private operation
from aggregates, decide source rights or temporal fitness, or use model
confidence as evidence.

[Back to top](#top)

---

<a id="public-safety-and-governed-outcomes"></a>

## Public safety and governed outcomes

### Finite outcomes

| Outcome | Haskell County use | Required visible state |
|---|---|---|
| `ANSWER` | A bounded public-safe orientation, source-role, data-fitness, regional aquifer, district-context, or aggregate response is supported by released evidence and policy | Evidence references, source roles, time basis, limitations, review/release state, and correction route |
| `ABSTAIN` | Evidence, authority, as-of state, freshness, geography, rights, or scope is insufficient; a current, future, or unsupported conclusion is requested | Stable reason code, evidence gap, official redirect where safe, and no answer-like fallback |
| `DENY` | The request seeks right-standing or lawful-use determination, private or operational detail, legal/current guidance, restricted content, or trust-membrane bypass | Stable reason code and safe alternative without leaking protected detail |
| `ERROR` | A required schema, resolver, policy evaluator, citation check, release record, or governed service failed | Stable error code; no permissive answer, raw-data fallback, or direct model path |

### Plan-derived candidate reason codes

| Boundary | Candidate reason code | Expected posture |
|---|---|---|
| Current water-right standing | `WATER_RIGHT_STANDING_REQUIRES_DWR` | `DENY`; route to the responsible authority |
| Lawful-use determination | `LAWFUL_USE_NONDETERMINATION` | `DENY` |
| Private well or farm detail | `PRIVATE_WELL_FARM_DETAIL_DENIED` | `DENY` |
| Parcel or operation water availability | `PROPERTY_WATER_AVAILABILITY_DENIED` | `DENY` |
| Future availability | `FUTURE_AVAILABILITY_UNSUPPORTED` | `ABSTAIN` or `DENY` as accepted policy requires |
| Current drought, supply, or operational advice | `OFFICIAL_CURRENT_GUIDANCE_REQUIRED` | `ABSTAIN`; route to a fit official current source |
| Operational precision | `OPERATIONAL_PRECISION_NOT_ADMITTED` | `DENY`, exclude, or reviewed generalization only |
| Aggregate downscaling | `AGGREGATE_TO_PRIVATE_INFERENCE` | `DENY` |
| Evidence or currentness gap | `EVIDENCE_REF_UNRESOLVED` / `SOURCE_CURRENTNESS_UNVERIFIED` | `ABSTAIN` or validation failure |
| Review and release closure | `REQUIRED_REVIEW_NOT_RECORDED` / `PUBLICATION_GATE_INCOMPLETE` | Block display, promotion, or publication |

These codes are **PROPOSED** and are not confirmed as the canonical runtime
registry.

### Required no-network negative proof

A credible later implementation should prove deterministically that:

1. a current water-right standing conclusion fails closed;
2. an administrative record cannot prove lawful use;
3. a dated record without as-of and limitation state cannot appear current;
4. private-well, farm, parcel, household, right-holder, or operation detail is denied;
5. a district or regional aggregate cannot be downscaled to an individual operation;
6. regional aquifer context cannot become a local well or future-supply forecast;
7. dated context cannot become current drought, emergency, restriction, or supply guidance;
8. unreviewed operational precision cannot enter a public card, tile, export, log, or accessibility label;
9. generated narrative cannot serve as evidence;
10. unresolved evidence, rights, time, review, correction, or rollback cannot produce `ANSWER` or a public-release claim;
11. public clients cannot read non-published lifecycle lanes.

[Back to top](#top)

---

<a id="evidence-and-readiness-boundary"></a>

## Evidence and readiness boundary

### Required public claim chain

```text
admitted source identity, role, time, and rights
  -> public-safe aggregate, generalized extract, or limitation notice
  -> EvidenceRef
  -> resolved EvidenceBundle
  -> water-administration / currentness / privacy / precision review
  -> PolicyDecision
  -> CitationValidationReport
  -> accountable ReviewRecord
  -> PromotionDecision and ReleaseManifest
  -> correction path and rollback target
  -> governed API
  -> public-safe map / Evidence Drawer / Focus response
```

Any missing material link narrows the output to `ABSTAIN`, `DENY`, `ERROR`, or
a held planning state. A README, plan, source link, public record, commit, pull
request, Markdown check, regional average, or schema-valid mock cannot replace
this chain.

### Readiness ledger

| Readiness area | Current state | Closure evidence needed |
|---|---|---|
| Placement | Same-path compatibility update; structural convergence held | Accepted migration authority plus consumer and rollback closure |
| Scope identity | `haskell-county` and `haskell` are planning identifiers | Registered stable scope identity and cross-root references |
| Source roles | Plan names candidate roles only | Admitted source records with authority, rights, time, limitations, and correction behavior |
| Administrative-water boundary | Non-determination is documented | Reviewed authority mapping, public limitation notice, reason codes, and negative proof |
| Temporal fitness | Plan records 2026-05-24 checks and a 2026-05-10 WIMAS snapshot | Exact as-of, effective, retrieval, freshness, supersession, withdrawal, and abstention behavior |
| Scientific scale | Regional aquifer context is proposed | Reviewed scale, uncertainty, geography, time basis, and tests preventing local overclaim |
| Aggregate privacy | District/county aggregates are candidates | Policy and fixtures preventing downscaling, joins, differencing, and private-operation inference |
| Operational precision | Exclusion/generalization is proposed | Rights, sensitivity review, transform receipt, and reconstruction-resistant negative proof |
| Contract and schema | Shared Focus surfaces exist but are not validated for Haskell here | Reviewed ownership, closed shape, fixtures, validator, and compatibility plan |
| Policy | No Haskell policy decision was executed | Reviewed rule package, native tests, evaluator binding, decision receipt, and governed consumer |
| UI/API/AI | Proposed surfaces only | Released public-safe envelope consumed through governed API with finite outcomes |
| Release, correction, rollback | Unproved | Review, promotion, manifest, correction propagation, withdrawal, rollback rehearsal, and owner |

[Back to top](#top)

---

<a id="smallest-safe-follow-up"></a>

## Smallest safe follow-up

The smallest dependency-closed follow-up is a **same-path reconciliation of the
existing Haskell build plan**, not a live administrative-data connector,
county payload, groundwater layer, or structural path migration.

That reconciliation should:

1. replace stale no-plan and older repository-inventory statements with current
   path evidence;
2. keep the plan's 2026-05-24 source checks and 2026-05-10 WIMAS snapshot
   explicitly time-bounded;
3. distinguish candidate source roles from admitted sources, EvidenceBundles,
   rights decisions, current-standing or lawful-use determinations, and approved
   public content;
4. replace unverified canonical-path assertions with current compatibility-lane
   evidence and the still-proposed ADR-0027 target;
5. reconcile contract, schema, policy, validator, fixture, runtime, release,
   correction, and rollback maturity against current repository files;
6. retain the strongest non-determination, temporal-fitness, private-operation,
   operational-precision, reason-code, and no-network negative-fixture
   boundaries without claiming implementation;
7. define a bounded acceptance packet for later review rather than a live or
   public product.

Explicit non-goals remain external source activation, live queries, private or
operational data, current/future water determinations, contract/schema/policy or
runtime changes, path migration, ADR acceptance, promotion, release,
deployment, or publication.

[Back to top](#top)

---

<a id="open-questions"></a>

## Open questions

### Water administration and scientific scope

- Which administrative statements may support a data-fitness card without
  turning KFM into a water-right or legal decision surface?
- Which aquifer and groundwater-management claims are supportable at regional,
  district, or county scale, and what time and uncertainty labels are required?
- Should the first proof remain entirely static and fixture-based until every
  non-determination and temporal-fitness boundary has negative coverage?

### Rights, time, privacy, and precision

- Which plan-named sources permit citation, excerpt, screenshot, cache, export,
  transformation, and public map display?
- How must as-of, limitation, supersession, correction, and official-redirect
  state survive normalization, evidence resolution, and rendering?
- What thresholds prevent joins, differencing, or repeated queries from
  revealing a right-holder, diversion, well, farm, parcel, household,
  operation, compliance, or vulnerability detail?
- Who reviews public-safe transforms and reconstruction resistance across maps,
  tiles, exports, logs, search, and accessibility text?

### Contract, policy, ownership, and operations

- Which shared surface owns Focus request, response, payload, runtime-envelope,
  and citation-report machine shape?
- What is the canonical reason-code registry for water-administration,
  currentness, privacy, aggregation, precision, and release obligations?
- Who owns the county composition, and who independently reviews water
  administration, legal boundary, hydrology, rights/privacy, sensitivity,
  security, accessibility, and release?
- What evidence would demonstrate parity between a released manifest, governed
  API, map surface, Evidence Drawer, export, correction route, and rollback
  target?

[Back to top](#top)

---

<a id="cross-references-and-maintenance"></a>

## Cross-references and maintenance

### Current repository references

- [Haskell County Focus Mode build plan](./haskell_county_focus_mode_build_plan.md)
- [County Focus Mode master index](../COUNTY_INDEX.md)
- [County lane README](../README.md)
- [County build-plan template](../_template/county-build-plan.md)
- [Focus Mode documentation control and compatibility lane](../../README.md)
- [Accepted Directory Rules v2](../../../doctrine/directory-rules.md)
- [ADR-0027 — County Focus Mode Control Plane](../../../adr/ADR-0027-county-focus-mode-control-plane.md)
- [ADR-0029 — Adopt Directory Governance Standard v2](../../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [FocusModePayload semantic contract](../../../../contracts/focus_mode/focus_mode_payload.md)
- [Focus schema-family index](../../../../schemas/contracts/v1/focus/README.md)
- [Focus policy boundary](../../../../policy/focus/README.md)

### Maintenance triggers

Review this README and the linked build plan when any of the following changes:

- Haskell directory, plan filename, shared index row, or structural migration state;
- ADR-0027 effective status or the Focus documentation placement decision;
- a plan-named source's authority, rights, time basis, public-safe scope, or correction guidance;
- a water-right, lawful-use, currentness, privacy, aggregation, precision, or sensitivity policy finding;
- Focus contract, schema, policy, validator, fixture, API, UI, or AI behavior;
- source admission, EvidenceBundle, review, release, correction, withdrawal,
  rollback, deployment, or public-parity evidence.

### Documentation validation expected

| Check | Required result |
|---|---|
| Metadata and heading structure | One complete KFM Meta Block and one H1 |
| Local navigation | Every fragment link resolves |
| Repository-relative links | Every linked path exists at the pinned main snapshot or its proposed status is explicit |
| Tables and code fences | Structurally balanced |
| Formatting | UTF-8, LF line endings, no tabs or trailing whitespace, final newline |
| Claim boundaries | No external-source currentness, water-right/lawful-use determination, current/future groundwater guidance, policy execution, release, deployment, or publication claim is inferred |
| County index | Left unchanged; stale Haskell one-byte finding disclosed for separate full reconciliation |
| Executable county validation | `NOT_RUN` unless a compatible validator is actually invoked and pinned |

### Correction and rollback

Before merge, close or abandon the draft pull request and branch. After merge,
use a transparent revert or bounded forward-fix PR against the actual merged
bytes. The README and generated provenance receipt should be corrected or
reverted together. A documentation rollback cannot retract an already released
public artifact; any future released Haskell content needs separate correction,
withdrawal, cache-invalidation, supersession, and rollback controls.

### Change history

| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-08-21 | Prior branch-only Haskell planning-lane modernization; did not reach main. |
| v1.1 | 2026-08-22 | Rebased the substantive boundary onto current main, removed stale stack claims, disclosed shared-index staleness, preserved plan-derived scope as proposal, and retained all source, evidence, policy, release, deployment, and publication holds. |

[Back to top](#top)

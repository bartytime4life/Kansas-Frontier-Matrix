<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/architecture/settlements-infrastructure
title: "Settlements & Infrastructure — Integration Architecture"
type: architecture-reference
version: v0.3-draft
status: "draft; repository-grounded; bounded-executable; relationship-HOLD; no-live-source; no-release; no-publication"
owners:
  - "@bartytime4life — verified CODEOWNERS review route"
  - "NEEDS VERIFICATION — independent domain, evidence, sensitivity, security, API, validation, release, correction, and rollback stewardship"
created: 2026-05-24
updated: 2026-08-19
policy_label: "public; architecture; settlements-infrastructure; critical-asset-sensitive; no-release; no-publication"
owning_root: docs/
current_path: docs/architecture/settlements-infrastructure/README.md
responsibility: >-
  Explain how the Settlements/Infrastructure bounded context composes with KFM's
  lifecycle, evidence, policy, validation, governed delivery, map/UI, release,
  correction, and rollback boundaries without replacing domain doctrine or
  creating contract, schema, policy, evidence, runtime, or publication authority.
truth_posture: >-
  CONFIRMED repository paths, accepted placement authority, bounded fixture-first
  profiles, deterministic validators/tests, shared EvidenceBundle projection, and
  explicit domain-wide holds / PROPOSED live-source admission, policy composition,
  evidence resolution, governed delivery, proof, release, and public use / UNKNOWN
  deployed behavior, source rights, steward authority, and operational protection.
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: d639f9ff40288d12244cd7bc84af538652f6dfb1
  target_prior_blob: 0fc768a7d2098e69467f0f493e4044335bcdfe90
  directory_rules_decision: ADR-0029 accepted
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  convergence_plan_blob: 099dedf747342db4f4b08ec29267292e47456aa9
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  domain_workflow_blob: a47d89c40efd58ac31bc44dbc56bdfb1ccc3a325
  policy_readme_blob: 792a67caab14d119cf4a21dee1365216bfaefb11
  place_identity_schema_blob: a1729587233b2541cede2db95f10434d43c52cb0
  place_identity_validator_blob: 1fa10eeb8534896851d17fb35b705f1c90ca1237
  place_identity_test_blob: 7cda69664ab7b5a866df054c25f69995d7b77879
  place_identity_workflow_blob: ebf6ee57fe64c03bceea9067d1a82da82777e140
  place_name_authority_schema_blob: bb0c94caf170bf13baf3b2939349db958b7b540c
  evidence_bundle_projection_blob: 44c022ffc7f24cc582b061c5f3145b716e3f150f
  merged_place_name_authority_pr: 2006
  merged_historical_place_resolution_pr: 2030
  merged_place_identity_pr: 2867
  merged_evidence_bundle_projection_pr: 2924
related:
  - ../document-convergence-plan.md
  - ../critical-asset-exposure.md
  - ../contract-schema-policy-split.md
  - ../evidence-drawer.md
  - ../governed-api/README.md
  - ../map-shell.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../doctrine/directory-rules.md
  - ../../domains/settlements-infrastructure/README.md
  - ../../domains/settlements-infrastructure/ARCHITECTURE.md
  - ../../../contracts/domains/settlements-infrastructure/README.md
  - ../../../schemas/contracts/v1/domains/settlements-infrastructure/README.md
  - ../../../policy/domains/settlements-infrastructure/README.md
tags: [kfm, architecture, settlements, infrastructure, evidence, sensitivity, critical-assets, maplibre, correction, rollback]
notes:
  - "Same-path documentation-only reconciliation; no structural migration or authority change."
  - "The architecture convergence plan keeps this page on HOLD pending classification of links, readers, and unique integration content."
  - "Repository-present bounded families include place-name authority, historical place resolution, Municipality/CensusPlace identity separation, and a shared EvidenceBundle projection."
  - "Those families are synthetic or projection-only; they do not establish source admission, policy approval, release, deployment, publication, or critical-asset exposure authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Settlements & Infrastructure — Integration Architecture

> **Operating rule.** KFM may describe places and public-safe infrastructure context only through bounded identity, source-role-preserving evidence, policy-aware transforms, finite outcomes, and governed release. A name, geometry, layer, graph edge, model result, or passing workflow never creates municipal status, infrastructure truth, release authority, or permission to expose harmful precision.

[![status: draft](https://img.shields.io/badge/status-draft-d4a72c?style=flat-square)](#status-and-authority)
[![relationship: HOLD](https://img.shields.io/badge/document%20relationship-HOLD-b42318?style=flat-square)](#document-relationship)
[![bounded profiles: present](https://img.shields.io/badge/bounded%20profiles-present-1f6feb?style=flat-square)](#current-bounded-implementation)
[![domain-wide validation: HOLD](https://img.shields.io/badge/domain--wide%20validation-HOLD-8250df?style=flat-square)](#validation-and-ci-maturity)
[![publication: none verified](https://img.shields.io/badge/publication-none%20verified-6e7781?style=flat-square)](#publication-correction-and-rollback)

> [!IMPORTANT]
> **This page is an integration overview, not domain authority.** Detailed domain language remains under [`docs/domains/settlements-infrastructure/`](../../domains/settlements-infrastructure/README.md). Contracts own meaning, schemas own machine shape, policy owns admissibility, evidence objects own support, and release records own publication state.

> [!CAUTION]
> **The document relationship remains on HOLD.** The architecture convergence plan records this page as overlapping detailed domain architecture. It stays in place until inbound links, unique content, readers, replacement scope, compatibility, and rollback are closed.

> [!WARNING]
> **Critical-asset and reconstruction risk fail closed.** Exact infrastructure geometry, interior layout, access paths, weak points, operator-sensitive details, live condition, capacity, outage, vulnerability, dependency paths, and cross-lane reconstruction hints must not reach ordinary public clients through data, style, metadata, URL, search, export, cache, telemetry, or generated language.

**Quick navigation:** [Status](#status-and-authority) · [Implementation](#current-bounded-implementation) · [Relationship](#document-relationship) · [Context](#bounded-context-and-ubiquitous-language) · [Topology](#placement-and-current-topology) · [Flow](#governed-operating-flow) · [Authority split](#contract-schema-policy-test-split) · [Sensitivity](#sensitivity-and-public-safe-representation) · [Delivery](#governed-delivery-and-user-surfaces) · [Seams](#cross-domain-seams) · [Validation](#validation-and-ci-maturity) · [Convergence](#implementation-convergence-plan) · [Release](#publication-correction-and-rollback) · [Holds](#conflict-and-hold-register) · [Acceptance](#acceptance-gates) · [Risks](#risks-and-anti-patterns) · [Questions](#open-questions) · [References](#references)

---

<a id="status-and-authority"></a>

## Status and authority

| Field | Current result |
|---|---|
| **Evidence snapshot** | `main@d639f9ff40288d12244cd7bc84af538652f6dfb1` |
| **Placement** | **CONFIRMED:** existing `docs/architecture/settlements-infrastructure/` path is placement-safe under accepted ADR-0029; this edit uses the same-path presumption. |
| **Document role** | Human-readable cross-root integration and maturity map. It is not doctrine, contract, schema, policy, evidence, review, proof, release, or runtime authority. |
| **Review route** | **CONFIRMED:** CODEOWNERS routes the repository review to `@bartytime4life`; independent specialist assignments remain **NEEDS VERIFICATION**. |
| **Relationship** | **HOLD:** long-term relationship to detailed domain documentation remains unresolved. |
| **Current implementation** | **BOUNDED:** four synthetic/projection families exist; broad domain operation remains mixed or held. |
| **Policy** | **PROPOSED/scaffolded:** policy documentation exists, but an accepted evaluator/bundle/consumer path was not established. |
| **Domain-wide readiness** | **HOLD:** source-level workflow retains semantic-validation, proof-producer, and release-dry-run holds. |
| **Deployment/publication** | **UNKNOWN / none established:** no live source, deployed domain API, public layer, model path, release, or correction propagation was proved. |

### Authority by question

| Question | Controlling evidence |
|---|---|
| Where does this page belong? | Accepted ADR-0029, adopted Directory Rules, existing path, and convergence plan. |
| What exists now? | Pinned repository files, validators, tests, workflows, fixtures, and merged PR records. |
| What does an object mean? | Its semantic contract. |
| What shape is valid? | Its machine schema and executable validator. |
| May information be exposed? | Source rights, sensitivity, policy, audience, purpose, review, release, and correction state. |
| Is a claim supported? | Resolved EvidenceRef-to-EvidenceBundle closure, not prose or visualization. |
| Is a capability released? | Governed release evidence and runtime observation, not a commit or green check. |

[Back to top](#top)

---

<a id="current-bounded-implementation"></a>

## Current bounded implementation

| Family | Repository evidence | What it proves | Explicit limit |
|---|---|---|---|
| Place-name authority graph | Contract/schema/fixtures/validator/tests/workflow from merged PR #2006 | Strict synthetic assertions, aliases, disputes, feature bindings, authority decisions, time, provenance, and finite validation | No live authority source, public gazetteer, legal status, or release |
| Historical place resolution | Contract/schema/fixtures/validator/tests/workflow from merged PR #2030 | Fixture-only exact name/time/source-role candidate evaluation with finite outcomes | No fuzzy production resolver, canonical place creation, source activation, or public route |
| Place identity | Closed schema, validator, nine focused tests, workflow from merged PR #2867 | Explicit `Municipality`/`CensusPlace` anti-collapse, temporal ordering, deterministic IDs, release-reference consistency | No real municipal/census determination, evidence admission, policy approval, or public geometry |
| EvidenceBundle projection | Domain-local `$ref` to shared EvidenceBundle plus focused validator/test/workflow from merged PR #2924 | Schema-shape convergence without a second domain EvidenceBundle authority | No real EvidenceRef lookup, bundle authentication, policy evaluation, or release |
| Domain-wide lane | Domain docs, many planned shapes, and a read-only workflow with explicit holds | Boundary presence and drift detection | No domain-wide semantic validator, proof producer, release dry run, or public operation |

> [!NOTE]
> A bounded profile may be **CONFIRMED executable** while real-world adoption remains **PROPOSED** and public use remains **HELD or DENIED**. This distinction prevents fixture success from being promoted into operational truth.

[Back to top](#top)

---

<a id="document-relationship"></a>

## Document relationship

| Surface | Owns | Does not own |
|---|---|---|
| [`docs/domains/settlements-infrastructure/README.md`](../../domains/settlements-infrastructure/README.md) | Domain reading map and detailed documentation entry | Machine shape, executable policy, evidence, or release |
| [`docs/domains/settlements-infrastructure/ARCHITECTURE.md`](../../domains/settlements-infrastructure/ARCHITECTURE.md) | Detailed bounded-context language and domain architecture | Contract/schema/policy/release authority |
| [`contracts/domains/settlements-infrastructure/`](../../../contracts/domains/settlements-infrastructure/README.md) | Semantic meaning and anti-collapse rules | Machine validation, policy decision, or release |
| [`schemas/contracts/v1/domains/settlements-infrastructure/`](../../../schemas/contracts/v1/domains/settlements-infrastructure/README.md) | Machine shape and bounded projections | Evidence sufficiency, admissibility, review, or publication |
| This page | Cross-root composition, current maturity, delivery boundaries, seams, correction, rollback, and open holds | Detailed domain doctrine or executable authority |

Structural action remains blocked until a no-loss comparison, inbound-link inventory, reader inventory, replacement reading path, compatibility decision, supersession record, and rollback plan are reviewed. This revision therefore changes the page in place and creates no redirect or migration.

[Back to top](#top)

---

<a id="bounded-context-and-ubiquitous-language"></a>

## Bounded context and ubiquitous language

The lane contains two connected subcontexts: **Settlements**, which describes place/community identity through time, and **Infrastructure**, which describes assets, facilities, networks, services, operators, condition observations, and dependencies.

| Concept | Meaning | Anti-collapse rule |
|---|---|---|
| `Settlement` | Evidence-bounded inhabited or historically inhabited place identity | Not automatically a legal municipality or census geography |
| `Municipality` | Legally constituted municipal entity | Not interchangeable with `CensusPlace`; authority and valid time are required |
| `CensusPlace` | Statistical geography for a stated census vintage | Not legal incorporation or continuous historical identity |
| `Townsite` / `GhostTown` | Historical settlement identity | Does not prove current habitation, legal status, or public-safe exact location |
| `Fort` / `Mission` / `ReservationCommunity` | Historically, culturally, militarily, or sovereignty-sensitive place identity | Requires source-role, cultural, tribal, legal, and sensitivity review appropriate to context |
| `InfrastructureAsset` | Physical asset identity | Not operator, owner, title, parcel, route, or exposure permission |
| `Facility` | Operational site or complex | Exact geometry, layout, access, condition, or operating detail may be restricted |
| `ServiceArea` | Time-scoped intended or observed coverage | Not a guarantee of present service at every location |
| `Operator` | Entity operating a system or facility | Operation is not ownership, title, public-contact permission, or policy authority |
| `ConditionObservation` | Time-scoped condition/status evidence | Not forecast, emergency instruction, or timeless current state |
| `Dependency` | Directed reliance between assets, systems, or services | Dependency and cascading-failure graphs are restricted by default |

Core rules: name assertion is not feature identity; historical identity is not current legal status; asset is not operator or owner; service area is not service guarantee; geometry is not permission; client-side hiding is not redaction; candidate/model output is not confirmed truth; and release never upgrades source authority.

[Back to top](#top)

---

<a id="placement-and-current-topology"></a>

## Placement and current topology

ADR-0029 adopts Directory Rules v2. The existing architecture path is retained because this page explains cross-root composition to humans. Adjacent authority remains separated by responsibility root:

```text
docs/        human architecture, domain guidance, decisions, runbooks
contracts/   semantic meaning
schemas/     machine shape
policy/      admissibility and obligations
fixtures/    synthetic examples
tools/       executable validators and producers
tests/       enforceability
apps/        governed delivery and client composition
data/        lifecycle records, evidence, receipts, proofs, and published bytes
release/     release decisions, candidates, correction, and rollback control
```

No new root, parallel domain authority, schema family, policy home, source registry, proof store, release lane, or publication path is created by this page.

[Back to top](#top)

---

<a id="governed-operating-flow"></a>

## Governed operating flow

```text
source event
  -> SourceDescriptor and rights/sensitivity review
  -> RAW capture with retrieval identity
  -> WORK or QUARANTINE
  -> normalized domain object plus transform receipt
  -> EvidenceRef -> EvidenceBundle resolution
  -> schema, domain, temporal, geometry, source-role, and policy validation
  -> candidate, review, proof, and catalog closure
  -> governed release decision with correction and rollback targets
  -> governed API or immutable public-safe carrier
  -> MapLibre / Evidence Drawer / Focus Mode / export
```

Each arrow is a governed transition. Watchers may propose work but do not publish. A validator result is not evidence, a receipt is not proof, a proof is not policy approval, a release candidate is not a release, and a UI render is not publication.

Finite public-facing outcomes remain `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`. Unknown identities, rights, sensitivity, source role, review state, or release binding fail closed rather than falling through to an answer.

[Back to top](#top)

---

<a id="contract-schema-policy-test-split"></a>

## Contract, schema, policy, fixture, and test split

| Concern | Owning root | Current posture |
|---|---|---|
| Domain meaning | `contracts/domains/settlements-infrastructure/` | Mixed: substantial bounded profiles plus broader planning surfaces |
| Machine shape | `schemas/contracts/v1/domains/settlements-infrastructure/` | Mixed: strict profiles, projections, aliases, and broader scaffolds |
| Admissibility | `policy/domains/settlements-infrastructure/` | Scaffolded/proposed; accepted evaluator and consumers not established |
| Synthetic evidence | `fixtures/` and profile-specific fixture lanes | Present for bounded profiles; not proof of real sources |
| Executable validation | `tools/validators/` | Substantial for bounded profiles; no domain-wide semantic validator established |
| Enforceability | `tests/` and profile workflows | Focused checks exist; domain-wide proof/release closure remains held |
| Evidence/proof/release | `data/` and `release/` | Structural lanes exist; operational domain closure not established |

The shared EvidenceBundle projection fixes a shape-drift seam only. It does not prove that EvidenceRefs resolve, that bundles are authentic or admissible, or that any consumer applies policy and release checks.

[Back to top](#top)

---

<a id="sensitivity-and-public-safe-representation"></a>

## Sensitivity and public-safe representation

Exposure decisions depend on object, operation, audience, purpose, precision, time, composition, source terms, and release state. Domain membership alone is not a sufficient policy decision.

| Risk | Safe default |
|---|---|
| Exact critical-asset or facility detail | DENY, generalize, redact, stage access, or omit |
| Interior layout, access route, weak point, control system, capacity, outage, vulnerability | DENY ordinary public delivery |
| Dependency or cascading-failure graph | DENY or aggregate unless qualified review authorizes a bounded derivative |
| Historic fort/mission/ghost-town precision overlapping archaeology, cultural context, or private land | QUARANTINE or generalize pending qualified review |
| Service area or infrastructure condition that could be mistaken for a guarantee or instruction | Display method, date, uncertainty, limitation, and official-channel disclaimer; otherwise ABSTAIN |
| Cross-lane join that reconstructs withheld detail | DENY the composition even when each input is individually public |

Public-safe transformation must occur before data reaches the browser or ordinary API response. Styling, hidden panels, client filters, shortened labels, and omitted popups are not redaction because the bytes remain exposed.

[Back to top](#top)

---

<a id="governed-delivery-and-user-surfaces"></a>

## Governed delivery and user surfaces

| Surface | Allowed role | Required boundary |
|---|---|---|
| Governed API | Return finite, policy-aware, release-bound projections | No canonical-store shortcut, raw protected detail, or internal policy diagnostics |
| MapLibre | Render released public-safe carriers and emit selection candidates | Pixels and feature properties are not evidence; restricted bytes never enter sources |
| Evidence Drawer | Show an allowed projection of evidence, source role, rights, freshness, review, release, limitations, and correction state | Drawer payload is not the canonical EvidenceBundle and cannot invent trust state |
| Focus Mode / AI | Interpret resolved, allowed evidence with citations and bounded confidence | No browser-to-model path, no unresolved EvidenceRef, no sensitive inference, no uncited answer |
| Search/graph | Find released entities and public-safe relations | No graph edge or search rank becomes sovereign truth; joins must be policy-checked |
| Export/story/screenshot | Carry released context outside the app | Preserve release ID, citation, temporal/spatial scope, limitations, sensitivity transform, and correction state |

No live Settlements/Infrastructure route, public layer, evidence resolver, model path, or release is claimed by this document.

[Back to top](#top)

---

<a id="cross-domain-seams"></a>

## Cross-domain seams

| Adjacent lane | Allowed relationship | Required protection |
|---|---|---|
| Roads/Rail/Trade | Facilities, depots, crossings, settlement access, generalized route context | Transport identity and network authority remain with the transport lane |
| Hazards | Exposure/resilience context and released impact summaries | Hazard observation/advisory identity remains separate; critical-asset precision stays restricted |
| Hydrology | Water-service context, generalized facilities, watershed relation | Hydrologic observations remain hydrology evidence; no safety guarantee inferred |
| Energy/Utilities | Public-safe service and facility context | Operator, ownership, capacity, outage, vulnerability, and exact dependency require policy review |
| People/DNA/Land | Historical associations or governed aggregate context | No living-person, title, ownership, genealogy, or genomic inference without owning-lane authority |
| Archaeology | Historical place relation and generalized context | Exact locations and cultural/tribal knowledge fail closed pending qualified stewardship |
| Governance/Administrative geography | Legal or administrative relation | Legal status and geography version require authoritative source and valid time |

A cross-domain join is a new consequential claim surface. It must preserve participant identity, source role, time, evidence, policy, review, release, and correction state; a join cannot inherit the least restrictive input policy by default.

[Back to top](#top)

---

<a id="validation-and-ci-maturity"></a>

## Validation and CI maturity

| Layer | Current result |
|---|---|
| Place identity | Closed schema, deterministic validator, nine focused tests, and dedicated workflow are repository-present |
| Place-name authority | Bounded contract/schema/fixtures/validator/tests/workflow are repository-present |
| Historical resolution | Fixture-only deterministic resolution and negative cases are repository-present |
| EvidenceBundle projection | Shared-shape projection and focused convergence validation are repository-present |
| Domain-wide semantic validation | **HOLD** in the domain workflow |
| Domain proof production | **HOLD** in the domain workflow |
| Domain release dry run | **HOLD** in the domain workflow |
| Real-source, policy, security, runtime, correction, and rollback proof | **UNKNOWN / not established** |

A workflow filename or green profile check proves only the commands and assertions it actually runs. It does not prove source rights, legal status, real evidence, policy enforcement, deployment isolation, public safety, release, or publication.

[Back to top](#top)

---

<a id="latest-hosted-evidence"></a>

## Latest hosted evidence

This page intentionally does not freeze a historical workflow-run table as durable architecture. Hosted checks are commit-specific operational evidence. Reviewers should inspect the exact PR head and compare failures with the exact base before classifying them as introduced, inherited, or external.

For this documentation-only change, required evidence is: exact-head one-file diff, metadata/anchor/link validation, applicable documentation checks, changed-area security/path checks, and explicit classification of any residual failure. Pending hosted CI is not a passing result.

[Back to top](#top)

---

<a id="implementation-convergence-plan"></a>

## Implementation convergence plan

### P0 — authority and exposure closure

1. Keep this page's relationship on HOLD until the document topology closes.
2. Inventory accepted contracts, canonical schemas, aliases, policies, evaluators, fixtures, validators, workflows, consumers, and lifecycle homes.
3. Ratify source-role, rights, sensitivity, precision, cross-lane inference, and qualified-review rules.
4. Preserve strict bounded profiles rather than broadening them into premature domain authority.

### P1 — next dependency-closed proof

The next sound slice is a **synthetic, no-network municipal legal-status support envelope** that consumes the existing place-identity distinction without asserting any real municipality. It should bind:

- one synthetic place identity;
- one legal-status evidence role;
- one census-geography evidence role;
- temporal validity and source-role requirements;
- supported, abstained, denied, and errored outcomes;
- no-network deterministic replay;
- policy/review/release placeholders that cannot be mistaken for approval; and
- focused contract/schema/fixture/validator/test/workflow closure in existing authority roots.

It must not activate Census, state, local, archival, utility, address, parcel, or operator sources; infer real legal status; expose exact infrastructure; add a live route; or promote lifecycle state.

### P2 — governed runtime and public-safe derivative

Only after the bounded profile, source admission, policy, evidence resolution, review, proof, and release gates close should KFM add a live governed resolver, public-safe projection, API/map integration, correction propagation, and rollback drill.

[Back to top](#top)

---

<a id="publication-correction-and-rollback"></a>

## Publication, correction, withdrawal, and rollback

A release requires exact candidate identity, source/evidence closure, rights and sensitivity decisions, validation, policy, qualified review, proof/catalog closure, immutable artifact identity, correction path, and rollback target. A commit, PR, workflow, fixture, schema, or generated receipt is not a release.

Correction must propagate through every released carrier: API, catalog, tile/raster/vector artifact, Evidence Drawer, search/graph projection, export, cache, and AI context. Withdrawn or superseded objects must remain historically inspectable where policy allows while no longer resolving as current.

This documentation change is rolled back by reverting its commit or restoring prior blob `0fc768a7d2098e69467f0f493e4044335bcdfe90`. It changes no source, data, policy, runtime, release, deployment, or public cache.

[Back to top](#top)

---

<a id="conflict-and-hold-register"></a>

## Conflict and HOLD register

| Item | Current status | Closure required |
|---|---|---|
| Architecture page versus detailed domain dossier | HOLD | Link/reader/content inventory, no-loss plan, replacement reading path, compatibility, supersession, rollback |
| Broad domain schema maturity | MIXED | Classify strict profiles, projections, aliases, and scaffolds without parallel authority |
| Contract/schema aliases and identity vocabulary | NEEDS VERIFICATION | Accepted canonical/compatibility map and migration rule |
| Policy evaluator and public consumers | HOLD | Accepted defaults/rules, evaluator, bundle, obligations, positive/negative fixtures, consumer wiring |
| EvidenceRef resolution | HOLD | Repository-local authority, digest binding, policy/review/release checks, finite outcomes, no-network proof before live lookup |
| Critical-asset precision and cross-lane inference | HOLD | Qualified security/sensitivity decision plus negative carrier tests |
| Domain-wide semantic/proof/release workflow | HOLD | Real commands, exact assertions, proof producer, release dry run, correction/rollback drill |
| Live sources and source rights | HOLD | Current SourceDescriptors, terms, attribution, cadence, source head, correction behavior, activation review |
| Public API/map/search/AI | HOLD | Released public-safe projection, authenticated delivery, policy enforcement, measured no-leak evidence |
| Stewards and separation of duties | NEEDS VERIFICATION | Named accountable roles and independent review where policy-significant |

[Back to top](#top)

---

<a id="acceptance-gates"></a>

## Acceptance gates

A bounded capability graduates only when:

1. ownership and placement are unambiguous under Directory Rules;
2. semantic contract and closed machine schema agree;
3. source roles, time, identity, geometry, and anti-collapse rules are explicit;
4. valid and invalid synthetic fixtures cover finite outcomes;
5. deterministic validators and tests prove exact polarity and no-network behavior;
6. EvidenceRefs resolve to scoped EvidenceBundles for consequential claims;
7. rights, sensitivity, audience, purpose, and cross-lane inference policy are enforced;
8. required review is authenticated and distinct from authoring where appropriate;
9. proof, catalog, release, correction, withdrawal, and rollback bind to exact identity;
10. API, map, Drawer, search, export, cache, telemetry, and AI carriers expose no forbidden bytes;
11. deployed behavior is measured at the released revision; and
12. documentation records current scope, limits, commands, owners, correction, and rollback.

Schema validity or a green profile workflow alone is insufficient.

[Back to top](#top)

---

<a id="risks-and-anti-patterns"></a>

## Risks and anti-patterns

- Treating a name match, map label, census feature, or historical assertion as legal municipal status.
- Treating public source availability as redistribution or precision permission.
- Publishing exact infrastructure data and relying on styling to hide it.
- Joining individually public datasets into a harmful reconstruction surface.
- Treating service area as guaranteed service or condition observation as safety instruction.
- Converting a synthetic fixture, schema pass, validator pass, PR, receipt, or proof into release authority.
- Letting a browser call canonical stores, graph/vector indexes, policy internals, or model providers directly.
- Creating a second EvidenceBundle, policy, schema, source registry, proof, or release authority for convenience.
- Conflating current code presence with deployed, operational, secure, reviewed, or public behavior.
- Moving or retiring this page before the convergence HOLD is closed.

[Back to top](#top)

---

<a id="open-questions"></a>

## Open questions

1. What is the reviewed canonical/compatibility map for all Settlements/Infrastructure contracts and schemas?
2. Which policy vocabulary, evaluator, bundle, and consumers are accepted for public-safe place and infrastructure exposure?
3. Which source families may support real municipality, census place, historical place, facility, service-area, condition, operator, and dependency claims?
4. What precision and composition rules apply to critical assets, historic sites, private land, cultural/tribal context, and cross-lane joins?
5. What repository-local authority resolves Settlements/Infrastructure EvidenceRefs, and what digest binds lookup?
6. Which capabilities require independent review or two-person release approval?
7. Which public API, map, search, export, and AI surfaces are actually intended, and what no-leak tests gate them?
8. How will corrections, withdrawals, stale state, supersession, and rollback invalidate all derivatives and caches?
9. Does this page remain the long-term cross-root integration overview, or should unique content move into the domain dossier after no-loss closure?
10. What measured runtime evidence is required before any capability is described as operational or public?

[Back to top](#top)

---

<a id="references"></a>

## References

### Architecture and governance

- [`docs/architecture/document-convergence-plan.md`](../document-convergence-plan.md)
- [`docs/architecture/critical-asset-exposure.md`](../critical-asset-exposure.md)
- [`docs/architecture/contract-schema-policy-split.md`](../contract-schema-policy-split.md)
- [`docs/architecture/evidence-drawer.md`](../evidence-drawer.md)
- [`docs/architecture/governed-api/README.md`](../governed-api/README.md)
- [`docs/architecture/map-shell.md`](../map-shell.md)
- [`docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md)

### Domain and bounded implementation

- [`docs/domains/settlements-infrastructure/README.md`](../../domains/settlements-infrastructure/README.md)
- [`docs/domains/settlements-infrastructure/ARCHITECTURE.md`](../../domains/settlements-infrastructure/ARCHITECTURE.md)
- [`contracts/domains/settlements-infrastructure/README.md`](../../../contracts/domains/settlements-infrastructure/README.md)
- [`contracts/domains/settlements-infrastructure/place_name_authority_graph.md`](../../../contracts/domains/settlements-infrastructure/place_name_authority_graph.md)
- [`contracts/domains/settlements-infrastructure/historical_place_resolution.md`](../../../contracts/domains/settlements-infrastructure/historical_place_resolution.md)
- [`contracts/domains/settlements-infrastructure/place-identity.md`](../../../contracts/domains/settlements-infrastructure/place-identity.md)
- [`schemas/contracts/v1/domains/settlements-infrastructure/README.md`](../../../schemas/contracts/v1/domains/settlements-infrastructure/README.md)
- [`schemas/contracts/v1/domains/settlements-infrastructure/place-identity.schema.json`](../../../schemas/contracts/v1/domains/settlements-infrastructure/place-identity.schema.json)
- [`schemas/contracts/v1/domains/settlements-infrastructure/evidence_bundle.schema.json`](../../../schemas/contracts/v1/domains/settlements-infrastructure/evidence_bundle.schema.json)
- [`policy/domains/settlements-infrastructure/README.md`](../../../policy/domains/settlements-infrastructure/README.md)
- [`.github/workflows/domain-settlements-infrastructure.yml`](../../../.github/workflows/domain-settlements-infrastructure.yml)
- [`.github/workflows/place-identity.yml`](../../../.github/workflows/place-identity.yml)

[Back to top](#top)

---

<a id="appendix-a--no-loss-reconciliation-ledger"></a>

## Appendix A — No-loss reconciliation ledger

| Prior v0.2 material | v0.3 treatment |
|---|---|
| Cross-root integration purpose and detailed-domain boundary | Preserved |
| Same-path placement and Directory Rules basis | Preserved against accepted ADR-0029 |
| Municipality/CensusPlace, historical/current, name/feature, asset/operator, service/guarantee anti-collapse | Preserved and grounded in current bounded profiles |
| RAW-to-PUBLISHED trust flow | Preserved |
| Critical-asset fail-closed posture | Preserved and extended across all carriers |
| Governed API, MapLibre, Evidence Drawer, Focus Mode, export | Preserved without live-route claims |
| Cross-domain seams | Preserved with explicit join-as-new-claim rule |
| Broad schema/policy/validator/workflow holds | Preserved while separating them from focused executable profiles |
| Recommended Municipality/CensusPlace first slice | Recorded as complete only at synthetic profile scope |
| EvidenceBundle compatibility gap | Updated: shared shape projection exists; runtime resolution remains held |
| Run-specific hosted-check table | Replaced with exact-head validation guidance to avoid stale architecture evidence |
| Publication, correction, withdrawal, rollback | Preserved |
| Conflict/HOLD register and open questions | Updated to current repository evidence |
| Document convergence uncertainty | Elevated to explicit relationship HOLD |

---

## Change history

| Date | Version | Change |
|---|---|---|
| 2026-05-24 | v0.1 | Initial architecture brief from doctrine and proposed paths. |
| 2026-08-14 | v0.2 | Repository-grounded topology, maturity, sensitivity, seams, release, correction, and rollback reconciliation. |
| 2026-08-19 | v0.3-draft | Reconciled merged bounded profiles, shared EvidenceBundle projection, mixed validation maturity, document-relationship HOLD, and the next dependency-closed slice. |

<sub>**Status:** draft · **Version:** v0.3-draft · **Evidence checkpoint:** `main@d639f9ff40288d12244cd7bc84af538652f6dfb1` · **Document relationship:** HOLD · **Publication effect:** none · [Back to top](#top)</sub>

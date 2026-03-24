<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<TODO-VERIFY-UUID>
title: ROOT_GOVERNANCE
type: standard
version: v1
status: draft
owners: @bartytime4life
created: <TODO-VERIFY>
updated: <TODO-VERIFY>
policy_label: public
related: [docs/standards/README.md, docs/governance/README.md, policy/README.md, contracts/README.md, schemas/README.md, tests/README.md, .github/README.md, docs/standards/faircare/FAIRCARE-GUIDE.md, docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md]
tags: [kfm, governance, standards, trust, publication, review]
notes: [UUID and file-history dates need verification before merge, owner grounded from current /docs/ CODEOWNERS rule]
[/KFM_META_BLOCK_V2] -->

# ROOT_GOVERNANCE

Core governance law and review-trigger standard for KFM truth-state transitions, publication limits, runtime boundaries, and correction behavior.

> **Status:** `draft`  
> **Owners:** `@bartytime4life` *(current `/docs/` owner; narrower file ownership still needs verification)*  
> **Path:** `docs/standards/governance/ROOT_GOVERNANCE.md`  
> ![status](https://img.shields.io/badge/status-draft-orange) ![type](https://img.shields.io/badge/type-standard-0a7d5a) ![surface](https://img.shields.io/badge/surface-governance-3559b7) ![posture](https://img.shields.io/badge/posture-evidence--first-5b6770) ![owner](https://img.shields.io/badge/owner-%40bartytime4life-6f42c1)  
> **Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Root rules](#root-rules) · [Review triggers](#review-triggers) · [Allowed outcomes](#allowed-outcomes) · [Decision flow](#decision-flow) · [Surface responsibilities](#surface-responsibilities) · [Change bundle](#governance-significant-change-bundle) · [Open verification items](#open-verification-items)

> [!IMPORTANT]
> This file is the cross-domain governance standard in `docs/standards/`. It does **not** replace the executable policy layer in `policy/`, the machine-readable contract and schema surfaces in `contracts/` and `schemas/`, the enforcement surfaces in `tests/` and workflows, or the operator procedures in runbooks. KFM governance stays trustworthy only when these surfaces move together.

> [!WARNING]
> Treat every implementation-shaped statement in this file as doctrine, review guidance, or change-control law unless direct mounted code, schemas, fixtures, workflows, manifests, or runtime evidence prove more. Do not read this standard as proof that a given route, validator, policy bundle, or UI payload already exists.

---

## Scope

This standard defines the **minimum root governance law** for Kansas Frontier Matrix across domains, products, delivery layers, and runtime behaviors.

It governs:

- how KFM treats publication, promotion, correction, and withdrawal as trust-bearing state changes
- which changes are governance-significant enough to require explicit review
- which outcomes are allowed when support, rights, sensitivity, or release conditions are incomplete
- what public and steward-facing surfaces must keep visible at point of use
- how this human-readable standard hands off to policy, contracts, schemas, tests, workflows, and runbooks

It does **not** define:

- machine-readable policy bundles
- JSON Schema field-by-field contracts
- test harness implementation
- workflow YAML details
- deployment topology
- domain-specific publication logic beyond the root rules every lane must inherit

---

## Repo fit

| Item | Value |
|---|---|
| Path | `docs/standards/governance/ROOT_GOVERNANCE.md` |
| Document role | Root governance standard for cross-cutting trust, publication, correction, and review law |
| Upstream context | [`../README.md`](../README.md), [`../../../README.md`](../../../README.md) |
| Operational governance companion | [`../../governance/README.md`](../../governance/README.md) |
| Machine-readable companions | [`../../../policy/README.md`](../../../policy/README.md), [`../../../contracts/README.md`](../../../contracts/README.md), [`../../../schemas/README.md`](../../../schemas/README.md) |
| Enforcement companions | [`../../../tests/README.md`](../../../tests/README.md), [`../../../.github/README.md`](../../../.github/README.md) |
| Related standards | [`../faircare/FAIRCARE-GUIDE.md`](../faircare/FAIRCARE-GUIDE.md), [`../sovereignty/INDIGENOUS-DATA-PROTECTION.md`](../sovereignty/INDIGENOUS-DATA-PROTECTION.md) |

### Current verified snapshot

| Check | Status | Notes |
|---|---:|---|
| File exists in public `main` | ✅ | Present at the expected standards path |
| Current file substance | ⚠️ | Scaffold-only before this revision |
| Standards index routes here | ✅ | `docs/standards/README.md` lists this file as a downstream governance surface |
| `/docs/` ownership signal exists | ✅ | Current CODEOWNERS assigns `/docs/` to `@bartytime4life` |
| Active workflow enforcement for this standard | ? | Needs direct verification from mounted workflow YAML / branch protection |
| Narrower per-file ownership | ? | Not separately verified |

---

## Truth posture used in this standard

| Label | Use here | Must **not** be mistaken for |
|---|---|---|
| **CONFIRMED** | Directly supported by current repo-facing evidence or stable KFM doctrine already reflected in adjacent repo docs | Proof of hidden code, hidden workflows, or mounted runtime behavior |
| **INFERRED** | Conservative structural completion where KFM doctrine strongly implies a seam must exist | Confirmed implementation |
| **PROPOSED** | Recommended standard wording, structure, or change discipline that fits current KFM doctrine and repo layout | Something already deployed |
| **UNKNOWN** | Not verified strongly enough in the current session to claim as current repo fact | A gap to smooth away with confident prose |
| **NEEDS VERIFICATION** | Review item that should be checked before merge or before treating a behavior as live | A blocker on useful drafting |

> [!NOTE]
> KFM governance is weakened when uncertainty gets polished away. Keep unresolved items visible until direct evidence closes them.

---

## Root rules

These rules are the root of governance for this standards surface.

### 1. Governance follows the truth path

KFM treats the path below as load-bearing:

```text
Source edge -> RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG -> PUBLISHED
```

Governance applies at every state change, not only at public release time.

### 2. Publication is a governed event

A public-facing value, map layer, dossier, story claim, export, or runtime answer is not “good enough” merely because a query succeeded. Publication requires rights, sensitivity, provenance, release state, and review posture to remain valid together.

### 3. No bypass of the trust membrane

Normal public and steward-facing surfaces must not bypass governed APIs, evidence resolution, or policy evaluation to reach truth-bearing internals directly.

### 4. Derived layers are not authoritative by default

Graphs, search indexes, vector tiles, map portrayals, caches, summaries, scenes, rankings, and model-assisted outputs remain **derived** unless explicitly promoted under governance.

### 5. Promotion changes trust state

Promotion is not a quiet file move. It is a governed state change that should be accompanied by the relevant artifacts, review context, and correction path.

### 6. Runtime outcomes stay finite and fail closed

When support is incomplete or policy conditions fail, KFM should prefer visible constrained outcomes over persuasive overreach.

Minimum runtime family:

- `ANSWER`
- `ABSTAIN`
- `DENY`
- `ERROR`

### 7. Correction preserves lineage

Supersession, narrowing, withdrawal, replacement, and generalization should preserve visible lineage instead of erasing prior public state.

### 8. Separation of duty matters for policy-significant change

Changes that alter publication rights, sensitivity posture, outward trust state, or correction visibility should not collapse proposal, approval, and release into one invisible action stream.

### 9. Documentation is part of governance

Behavior-significant governance changes should move with adjacent docs, policy surfaces, contracts, fixtures, tests, and runbooks. A doc-only governance change that leaves executable surfaces drifting is incomplete.

---

## Root invariants and their practical consequence

| Invariant | Practical consequence |
|---|---|
| Canonical truth path | Source material moves through staged, reviewable trust states before publication |
| Trust membrane | Public or external surfaces read through governed APIs only |
| Authoritative vs derived separation | Delivery convenience layers do not quietly become sovereign truth |
| Map-first, time-aware operation | Place and time remain coequal operating dimensions |
| Evidence-bounded runtime behavior | Focus-like synthesis remains subordinate to evidence and policy |
| Visible correction | Public trust surfaces preserve supersession, narrowing, withdrawal, and replacement cues |
| Fail-closed default | Unknown rights, unresolved evidence, stale projections, or sensitivity conflicts do not pass silently |
| Governance-coupled release | Release state, evidence linkage, and correction linkage remain attached downstream |

---

## What this file governs — and what it delegates

| Surface | This standard owns | This standard does **not** replace |
|---|---|---|
| `docs/standards/governance/ROOT_GOVERNANCE.md` | Root governance law, review triggers, allowed outcomes, cross-cutting obligations | Policy code, schemas, tests, workflow YAML |
| `policy/` | Executable policy posture, reasons, obligations, decision behavior | Human-readable root law |
| `contracts/` + `schemas/` | Machine-readable object definitions and validation shapes | Governance interpretation by itself |
| `tests/` + workflows | Evidence that rules are enforced and fail closed | The rules themselves |
| `docs/governance/` | Operational governance navigation and review-facing docs | Standards-layer root governance doctrine |
| `docs/runbooks/` | Incident, rollback, correction, restore, and operator procedures | Root governance law |
| Surface-specific docs | Local consequences for a feature, lane, or interface | Cross-domain root governance |

---

## Review triggers

Use this matrix when deciding whether a change must pass through explicit governance review.

| Trigger class | Why governance applies | Also inspect | Typical outcome set |
|---|---|---|---|
| Public claim or public-facing interpretation change | It changes what users may treat as supported truth | Evidence links, release state, correction path | publish · hold · generalize · deny |
| Promotion, publication, withdrawal, or supersession change | It changes trust state, not just storage state | Release artifacts, review notes, rollback/correction path | promote · publish · withdraw · supersede |
| Rights, sensitivity, or exact-location exposure change | It may change what can safely be shown or redistributed | Policy layer, sovereignty / FAIR+CARE / ethics companion docs | generalize · restrict · hold · deny |
| Runtime answer behavior change | It changes claim-bearing behavior at point of use | Focus envelope, evidence drill-through, negative-path tests | answer · abstain · deny · error |
| Derived layer begins to look authoritative | It risks blurring authoritative vs derived separation | Evidence Drawer behavior, release linkage, surface state | narrow · relabel · hold |
| Reviewer / approval boundary change | It changes who can approve or release policy-significant state | CODEOWNERS, review path, separation-of-duty expectations | approve · escalate · deny |
| Export behavior change | It changes what leaves the governed shell and what trust cues remain attached | Export preview, manifest/proof expectations, correction linkage | publish · restrict · generalize · deny |
| Story / dossier / teaching surface change | It can change interpretation, context, or audience burden | Narrative provenance, dates, perspective labels, correction visibility | publish · revise · hold |
| Domain-lane expansion | A new lane inherits root rules but adds lane-specific burden | Source descriptors, rights posture, support/time semantics | admit · stage · hold |

> [!TIP]
> If you are unsure whether governance applies, treat the change as governance-significant until proven otherwise.

---

## Allowed outcomes

KFM should prefer explicit governed outcomes over vague success language.

| Outcome | Meaning | Typical use |
|---|---|---|
| `promote` | Candidate material becomes release-bearing | Reviewed dataset/version or outward artifact is ready to move forward |
| `publish` | Public-safe outward state is allowed | Public-facing surface, export, or story node is approved for release scope |
| `hold` | Work is not publishable yet, but not rejected outright | Missing proof, incomplete review, unresolved dependencies |
| `quarantine` | Material is staged away from normal promotion flow | Validation failure, source anomaly, suspected sensitivity or rights issue |
| `generalize` | The public-safe version must reduce precision or detail | Exact location, culturally sensitive material, biodiversity or archaeology exposure |
| `restrict` | Visibility narrows to stewards or authorized roles | Rights, sensitivity, or review constraints |
| `deny` | Requested action is not allowed | Policy violation, unsupported publication path, forbidden surface |
| `abstain` | System refuses to answer as evidence is insufficient | Runtime evidence gap, citation failure, unresolved scope |
| `error` | Technical failure prevented a safe result | Resolver failure, schema failure, stale-state mismatch, system fault |
| `withdraw` | Previously outward state is pulled back visibly | Exposure issue, invalid release, rights change |
| `supersede` | A newer governed state replaces an older one with lineage intact | Correction, improved release, narrowed interpretation |

### Runtime note

Runtime claim-bearing surfaces should stay within the finite result family:

```text
ANSWER / ABSTAIN / DENY / ERROR
```

Publication and review workflows may use the broader governance vocabulary above.

---

## Decision flow

```mermaid
flowchart LR
    A[Source / change / runtime request] --> B[ROOT_GOVERNANCE]
    B --> C{Governance class}
    C -->|public claim or publication| D[Policy + review]
    C -->|people / social consequence| E[Operational ethics companion]
    C -->|rights / sensitivity / exact location| F[FAIR+CARE / sovereignty review]
    C -->|runtime answer behavior| G[Evidence resolution + runtime checks]

    E --> D
    F --> D
    G --> D

    D --> H{Supportable and public-safe?}

    H -->|yes| I[Promote / publish]
    H -->|limited| J[Hold / quarantine / generalize / restrict]
    H -->|no| K[Deny / abstain / error]

    I --> L[Governed API]
    J --> L
    K --> L

    L --> M[Map · Timeline · Dossier · Story · Focus · Export]
    M --> N[Correction visibility remains attached]
```

---

## Surface responsibilities

Every consequential surface should keep trust cues visible at point of use.

| Surface | Must keep visible | Governance burden |
|---|---|---|
| **Map / Explorer** | time scope, freshness, release context, route to evidence | Must not imply a derived portrayal is authoritative without evidence drill-through |
| **Timeline** | event grain, as-of basis, stale-state cues, compare basis | Must not flatten time ambiguity into a single apparent now |
| **Dossier** | identity, dependencies, service/hazard context, evidence links, correction state | Must behave like a durable object, not an untracked modal |
| **Story** | evidence-linked excerpts, dates, perspective labels, review/correction state | Narrative clarity must not sever provenance |
| **Evidence Drawer** | bundle members, quote context, transforms, release state, preview limits | Mandatory trust object for consequential claims |
| **Focus** | scoped retrieval, citation check, audit reference, finite result family | No uncited answer path; no policy bypass |
| **Compare** | explicit basis for side A / side B, time basis, uncertainty cues | Must preserve asymmetry instead of forcing false equivalence |
| **Export** | release scope, evidence linkage, preview policy, correction linkage | Export must not quietly drop trust cues |
| **Review / Stewardship** | diff, gates, policy labels, review notes, receipts | No hidden approvals; review state should stay legible |

---

## Governance-significant change bundle

A governance-significant change is not done until the related evidence surfaces move together.

### Minimum bundle

- [ ] Change class is named
- [ ] Affected audience and affected surfaces are named
- [ ] Allowed outcome set is decided **before** implementation
- [ ] Documentation changes are included or explicitly declared unnecessary
- [ ] Policy implications are updated or explicitly declared unchanged
- [ ] Contract/schema implications are updated or explicitly declared unchanged
- [ ] Fixture/test implications are updated or explicitly declared unchanged
- [ ] Rollback or correction path is named
- [ ] Ownership and approval boundary are rechecked
- [ ] Unknowns remain visible instead of being smoothed away

### Definition of done

A governance-sensitive change is ready only when:

1. the trust state it changes is explicit,
2. the outward consequence is reviewable,
3. the negative path is acceptable,
4. correction remains possible without erasing lineage, and
5. adjacent executable surfaces are not left drifting from the standard.

---

## Governance handoff rules

### To policy

Use `policy/` when the question is:

- what result should be emitted
- what reasons and obligations should be recorded
- whether a request is allowed, restricted, generalized, denied, or held

### To contracts and schemas

Use `contracts/` and `schemas/` when the question is:

- what object shape must exist
- what fields are required
- what versioned machine-readable objects must validate
- what runtime, release, or correction envelope is expected

### To tests and workflows

Use `tests/` and workflow surfaces when the question is:

- how fail-closed behavior is proven
- how invalid fixtures are rejected
- how merge or promotion is blocked
- how negative paths remain exercised

### To runbooks

Use runbooks when the question is:

- how a correction drill is executed
- how rollback or withdrawal is performed
- how restore, reissue, or incident communication works in practice

---

## Open verification items

These items should be checked before treating this standard as fully merged into live repo reality.

| Item | Why it still matters |
|---|---|
| Exact `doc_id` UUID | Required by the KFM meta block, not verified from current repo evidence |
| File `created` / `updated` dates | Public page inspection did not establish trustworthy file-history dates for this exact document |
| Narrower ownership than `/docs/` | Current evidence confirms `/docs/` ownership, not a stricter file-level owner |
| Mounted-checkout parity | Public `main` was inspected; local branch/worktree parity still needs verification |
| Active workflow YAML / required checks | Repo docs describe workflow intent, but active checked-in enforcement was not verified here |
| Executable policy bundle inventory | `policy/` doctrine is visible; mounted runnable bundles/tests remain unverified |
| Authoritative schema home decision | `contracts/` vs `schemas/` authority resolution still needs explicit confirmation |
| Related downstream standards substance | Some linked standards are documented as scaffold-level in current evidence and may need synchronized strengthening |

> [!CAUTION]
> Do not “resolve” these items by assumption during implementation. Close them with direct repo, workflow, schema, or runtime evidence.

---

## Merge guidance for maintainers

A good merge of this file should leave the repository in a clearer state than before.

Prefer these outcomes:

- this file becomes the stable human-readable governance root for `docs/standards/`
- adjacent surfaces link to it consistently
- policy and contract owners can point back here without using it as a substitute for executable rules
- future contributors can tell which governance questions belong here and which belong elsewhere

Avoid these outcomes:

- this file starts claiming enforcement that only tests or workflows could prove
- it duplicates `policy/README.md` or `contracts/README.md`
- it drifts into domain-specific governance that should live in lane docs
- it sounds more certain than current mounted evidence supports

---

<details>
<summary><strong>Quick glossary</strong></summary>

| Term | Working meaning in this file |
|---|---|
| **Truth path** | The staged path from source edge through publication |
| **Trust membrane** | The governed boundary preventing normal surfaces from bypassing policy and evidence resolution |
| **Authoritative** | The governed record or state that may anchor outward claims |
| **Derived** | Rebuildable delivery or retrieval material such as tiles, graphs, summaries, scenes, or rankings |
| **Public-safe** | Safe for the intended audience after rights, sensitivity, precision, and release checks |
| **Evidence Drawer** | The point-of-use trust object that keeps claims inspectable |
| **DecisionEnvelope** | A machine-readable policy result object |
| **EvidenceBundle** | A request-time support package for a claim, feature, export, or answer |
| **CorrectionNotice** | The lineage-preserving object that records supersession, withdrawal, narrowing, or replacement |

</details>

<p align="right"><a href="#root_governance">Back to top</a></p>

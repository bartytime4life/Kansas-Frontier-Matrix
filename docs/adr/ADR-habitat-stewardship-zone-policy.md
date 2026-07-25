<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/adr-habitat-stewardship-zone-policy
title: Habitat Stewardship-Zone Policy Boundary
type: adr
version: v1.0
status: draft
effective_decision_status: proposed
adr_id: unassigned
owners:
  - "NEEDS VERIFICATION — architecture decision owner"
  - "NEEDS VERIFICATION — Habitat domain steward"
  - "NEEDS VERIFICATION — stewardship/source steward"
  - "NEEDS VERIFICATION — policy and sensitivity steward"
  - "NEEDS VERIFICATION — evidence, release, correction, rollback, validation, and docs stewards"
reviewers_required:
  - Architecture steward
  - Docs steward
  - Habitat domain steward
  - Policy and sensitivity steward
  - Source and rights steward
  - Evidence steward
  - Release, correction, and rollback steward
  - Validation steward
created: "NEEDS VERIFICATION — scaffold predates this revision"
updated: 2026-07-24
policy_label: public
truth_posture: cite-or-abstain
responsibility_root: docs/
current_path: docs/adr/ADR-habitat-stewardship-zone-policy.md
supersedes: []
superseded_by: null
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 2e4049bf511dcc5c4425a297458bf58627b58299
  target_prior_blob: 7e0f72d384991df420cf993d5c64896985d9f0d2
  adr_readme_blob: f1b5d34a53b6c717832d587de54989ce8192bcaa
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  habitat_architecture_blob: 82263ea8f5862401e5aef57ec43f49711d12c998
  habitat_canonical_paths_blob: 837aa111f70b8df678b5545c72f92c1fdca73b66
  stewardship_zone_contract_blob: 915c30978c9cb20db834d6d3e90228a34a48907e
  stewardship_zone_schema_blob: 9ec074c467e01f4095f2081f083ddab17596b52d
  stewardship_zone_policy_blob: a5fc273691ba16c35f91837c2a224b1f13266587
  habitat_fixtures_readme_blob: 674c5acf8c2f1739762625e392616ce1034de0e6
  habitat_tests_readme_blob: 4503de9bcb1c92db45012d897d647fb39a9f7172
  stewardship_zone_tests_readme_blob: 1541f49b64cf7bddbc9d805db6623a00d72b74f9
  docs_control_plane_workflow_blob: 986fe1b4845c51f719bcfeeefe08729517ae543c
inspection_boundary: >
  Current-session GitHub reads of the target scaffold, ADR operating rules, Directory Rules,
  Habitat architecture and canonical-path guidance, the StewardshipZone semantic contract,
  paired schema, policy scaffold, Habitat fixture/test indexes, StewardshipZone test-lane
  documentation, and documentation-control workflow. No accepted ReviewRecord, live source
  activation, source-rights determination, policy evaluation, executable StewardshipZone test,
  emitted EvidenceBundle, public-safe projection, ReleaseManifest, correction, rollback,
  governed API response, map render, deployment, or production publication was exercised.
related:
  - docs/adr/README.md
  - docs/adr/INDEX.md
  - docs/adr/ADR-template.md
  - docs/doctrine/directory-rules.md
  - docs/domains/habitat/ARCHITECTURE.md
  - docs/domains/habitat/CANONICAL_PATHS.md
  - contracts/domains/habitat/stewardship_zone.md
  - schemas/contracts/v1/domains/habitat/stewardship_zone.schema.json
  - policy/domains/habitat/stewardship_zone.rego
  - policy/sensitivity/habitat/
  - fixtures/domains/habitat/
  - tests/domains/habitat/test_stewardship_zone/README.md
  - data/registry/sources/habitat/
  - release/manifests/habitat/
  - .github/workflows/docs-control-plane.yml
tags: [kfm, adr, habitat, stewardship-zone, policy, sensitivity, public-safe, evidence, release, rollback, context-not-authority]
notes:
  - "Same-path modernization of an existing unassigned PROPOSED scaffold."
  - "This revision does not assign an ADR number, update the ADR index, accept the decision, implement policy, or publish data."
  - "Assigning a permanent ADR number requires a separately scoped update to docs/adr/INDEX.md and validator closure."
  - "The source metadata remains draft and the effective decision status remains proposed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR — Habitat Stewardship-Zone Policy Boundary

> **Proposed decision.** KFM will treat `StewardshipZone` as an evidence-bound Habitat context object—not as land ownership, public-access permission, management instruction, regulatory designation, restoration approval, funding eligibility, policy authority, or release authority. Exact or exposure-sensitive stewardship-zone material will fail closed; only a governed public-safe projection may reach public clients after source, rights, sensitivity, evidence, review, release, correction, and rollback gates close.

[![Decision: proposed](https://img.shields.io/badge/decision-proposed-d4a72c?style=flat-square)](#status)
[![ADR identity: unassigned](https://img.shields.io/badge/ADR%20identity-unassigned%20scaffold-f59e0b?style=flat-square)](#adr-identity-and-index-boundary)
[![Policy: default deny scaffold](https://img.shields.io/badge/policy-default%20deny%20scaffold-b42318?style=flat-square)](#current-repository-evidence)
[![Schema: permissive scaffold](https://img.shields.io/badge/schema-permissive%20scaffold-b42318?style=flat-square)](#current-repository-evidence)
[![Tests: executable coverage unverified](https://img.shields.io/badge/tests-executable%20coverage%20unverified-6e7781?style=flat-square)](#current-enforcement-maturity)
[![Publication effect: none](https://img.shields.io/badge/publication-none-6e7781?style=flat-square)](#authority-and-publication-boundary)

> [!IMPORTANT]
> **This is an unassigned, proposed ADR.** The file is a tracked slug-only scaffold, not a numbered decision. This same-path, one-file modernization does not claim a permanent ADR ID or update the canonical ADR index. Acceptance requires a separately scoped numbering/index change and explicit review evidence.

> [!CAUTION]
> **The repository does not currently enforce this decision.** The paired JSON Schema accepts any object, the Habitat policy file contains only a default-deny scaffold, object-specific fixture payloads were not verified, and the test-lane README does not prove executable tests or passing CI.

> [!WARNING]
> **A stewardship-zone layer is not proof of permission or authority.** Map styling, feature visibility, a polygon boundary, a source program name, a stewardship label, or generated language must never be used to infer ownership, public access, legal status, management direction, restoration approval, or release state.

**Quick navigation:** [Status](#status) · [Evidence boundary](#evidence-boundary) · [Context](#context) · [Decision](#proposed-decision) · [Decision matrix](#proposed-decision-matrix) · [Placement](#placement-and-authority-boundaries) · [Evidence packet](#required-evidence-and-release-packet) · [Current evidence](#current-repository-evidence) · [Maturity](#current-enforcement-maturity) · [Convergence](#implementation-and-convergence-plan) · [Acceptance](#acceptance-gates) · [Consequences](#consequences) · [Alternatives](#alternatives-considered) · [Risks](#risk-and-open-question-ledger) · [Migration](#migration-and-compatibility) · [Rollback](#rollback-and-supersession) · [References](#references) · [History](#revision-history)

---

<a id="status"></a>

## Status

| Field | Current value |
|---|---|
| **ADR identity** | Unassigned slug-only scaffold; no permanent `ADR-NNNN` claimed |
| **Tracked path** | `docs/adr/ADR-habitat-stewardship-zone-policy.md` |
| **Source metadata** | `draft` |
| **Effective decision status** | `proposed` |
| **Decision class** | Habitat-domain policy, evidence, sensitivity, public-safe projection, review, and release boundary |
| **Primary responsibility root** | `docs/` — human architecture decision record |
| **Directory Rules trigger** | `n/a — non-structural domain policy decision`; this ADR does not add/rename roots, move schema authority, split lifecycle phases, or create parallel homes |
| **Affected authority roots** | `contracts/`, `schemas/`, `policy/`, `tests/`, `fixtures/`, `data/registry/`, `data/`, `release/`, and governed public clients |
| **Current implementation effect** | Documentation only |
| **Release/publication effect** | None |
| **Migration required now** | No file move; future schema tightening may require data/fixture migration |
| **Rollback required** | Yes—documentation rollback now; implementation and release rollback before any later adoption |
| **Supersedes / superseded by** | None / none |

<a id="adr-identity-and-index-boundary"></a>

### ADR identity and index boundary

The repository's ADR operating contract requires permanent records to use `ADR-NNNN-kebab-case-slug.md`, with filename, H1, and canonical index in agreement. It also inventories slug-only files separately as **unassigned scaffolds**.

This revision intentionally preserves the current path because the authorized change budget is one file and the user requested an in-place upgrade. Therefore:

- this document **MUST remain `proposed`**;
- it **MUST NOT be treated as accepted or numbered**;
- it **MUST NOT be added to the numbered inventory under a fabricated ID**;
- a later numbering PR **MUST** check the latest ADR index, open PRs, and active branches, then update this file and `docs/adr/INDEX.md` together;
- the ADR-index validator **MUST** pass before the numbered record can merge.

---

<a id="evidence-boundary"></a>

## Evidence boundary

### CONFIRMED in this repository snapshot

- The prior target was an 18-line `PROPOSED` scaffold that linked Habitat architecture and preserved responsibility-root separation.
- Habitat architecture identifies `StewardshipZone` as a Habitat object family, describes it as a stewardship-context polygon, assigns a **T1 default**, and requires steward review for material publication.
- The Habitat architecture states that sensitive occurrence-linked or steward-controlled geometry must be generalized, redacted, reviewed, delayed, held steward-only, or denied; client-side styling is not a sensitivity control.
- `contracts/domains/habitat/stewardship_zone.md` defines `StewardshipZone` as context and explicitly excludes ownership, public access, restoration approval, management authority, regulatory status, funding eligibility, and release authority.
- The paired schema exists but has no declared properties or required fields and permits additional properties.
- `policy/domains/habitat/stewardship_zone.rego` exists as a proposed default-deny scaffold only.
- Habitat test documentation defines a StewardshipZone test lane and finite failure expectations, but executable modules, fixture payloads, policy execution, CI coverage, and pass rates remain unverified.
- The documentation-control workflow validates ADR inventory coherence on pull requests, but it does not accept decisions, approve policy, change release state, or publish data.

### PROPOSED by this ADR

- The normative stewardship-zone policy boundary and decision matrix below.
- Required evidence, sensitivity, review, release, correction, rollback, and public-safe projection obligations.
- A staged convergence plan across contracts, schemas, policy, fixtures, tests, source registry, lifecycle artifacts, release objects, and public clients.

### UNKNOWN

- Whether any real `StewardshipZone` records exist in RAW, WORK, QUARANTINE, PROCESSED, CATALOG, or PUBLISHED lifecycle stores.
- Whether any current source descriptor has verified rights, redistribution, citation, authority-role, precision, and stewardship-contact terms for stewardship zones.
- Whether object-specific fixture payloads or executable test modules exist outside the inspected README surfaces.
- Whether a governed API, Evidence Drawer, map layer, Focus Mode response, or release manifest currently exposes or consumes stewardship-zone data.
- Whether any human reviewer or steward has accepted this decision.

### NEEDS VERIFICATION before acceptance

- Assign a permanent ADR number and update the canonical index in the same reviewed change.
- Confirm accountable owners and required reviewers through repository governance evidence.
- Define and validate field-level schema requirements without creating a parallel schema home.
- Implement policy outcomes, obligations, and reason codes beyond `default allow := false`.
- Add deterministic, no-network fixtures and executable negative-path tests.
- Verify source descriptors, rights, sensitivity, and public-safe geometry requirements for every admitted source family.
- Verify release-manifest, correction, withdrawal, rollback, stale-state, and cache-invalidation behavior.
- Verify public API, MapLibre, Evidence Drawer, export, and AI behavior through governed interfaces only.

### Out of scope

This ADR does not:

- decide land title, ownership, access permission, program eligibility, management authority, emergency action, or regulatory designation;
- define the final JSON Schema field set or Rego implementation;
- activate a source, ingest data, approve a record, generate a public-safe derivative, or authorize publication;
- change the schema-home rule, create a new root, or resolve unrelated Habitat schema inventory questions;
- accept itself, assign itself a permanent number, or update the ADR index;
- merge, deploy, release, or publish anything.

---

<a id="context"></a>

## Context

Habitat is a context lane. `StewardshipZone` is useful because conservation, management, administrative, protected-area, restoration-planning, and access-sensitive boundaries can explain why Habitat objects are reviewed, grouped, generalized, withheld, or routed to a steward.

The same convenience creates a high-risk semantic collapse. A polygon can appear authoritative even when its source role, rights, geometry precision, valid time, public exposure class, and release state are unresolved. Users may infer that a displayed zone proves:

- who owns land;
- whether the public may enter;
- whether a management action is approved or required;
- whether a site is regulated, protected, funded, or eligible;
- whether a habitat model is observational truth;
- whether an exact sensitive boundary is safe to reveal.

None of those inferences is supported by a stewardship-zone context object alone.

Current repository surfaces also show an enforcement gap: semantic guidance is substantially richer than the paired machine and policy controls. The contract describes context, evidence, sensitivity, review, release, correction, and rollback expectations, while the schema and policy remain permissive/minimal scaffolds. A decision record is needed to keep future schema, policy, tests, source descriptors, release objects, and UI behavior aligned.

### Decision drivers

1. **Context must not become authority.** `StewardshipZone` must remain distinct from ownership, access, regulatory, management, restoration, funding, and release decisions.
2. **Sensitive joins inherit risk.** Stewardship context can intersect rare species, rare plants, archaeology, cultural sites, infrastructure, private land, or access-sensitive areas.
3. **Public precision must be governed.** Exact boundaries can expose operational or sensitive context even when the source dataset is nominally public.
4. **Source role must remain explicit.** A program boundary, protected-area layer, easement inventory, administrative zone, or local stewardship record can support different claims and obligations.
5. **Evidence and time matter.** Source vintage, valid time, retrieval time, release time, correction time, and supersession must remain inspectable where material.
6. **The public trust membrane must hold.** Public clients consume governed released projections, not canonical/internal records or client-filtered sensitive geometry.
7. **Release must be reversible.** Public exposure requires correction, withdrawal, rollback, stale-state, and cache-invalidation paths.

---

<a id="proposed-decision"></a>

## Proposed decision

> **Decision:** KFM will govern `StewardshipZone` as evidence-bound Habitat context with a default sensitivity posture of **T1 or the most restrictive inherited tier**, explicit source and geometry-exposure roles, fail-closed public exposure, and separate policy/review/release authority. Public clients may receive only a released public-safe projection whose evidence, rights, sensitivity, review, correction, and rollback chain is inspectable.

### Core semantic rule

A `StewardshipZone` **MAY describe** stewardship, management, administrative, conservation, review, protected-area, restoration-planning, or public-safe summary context.

A `StewardshipZone` **MUST NOT by itself assert**:

- land ownership or title;
- public, private, tribal, or steward access permission;
- legal status or regulatory designation;
- management instruction, operational approval, or emergency guidance;
- restoration approval or funding/program eligibility;
- species occurrence, critical habitat, or modeled-habitat truth;
- public-release authority.

### Required policy rules

1. **Default classification.** A stewardship-zone record **MUST default to T1** unless reviewed evidence supports a different tier. A cross-domain join **MUST inherit the most restrictive applicable tier**.
2. **Explicit source role.** Every record **MUST identify the source descriptor, source-native record, source role, authority limits, rights/terms posture, citation obligation, and source vintage where material**.
3. **Explicit zone role.** Every record **MUST identify its role**, such as stewardship context, management context, administrative context, conservation context, review zone, restricted exact zone, or public-safe summary.
4. **Explicit exposure class.** Geometry **MUST be labeled** exact, generalized, aggregate, suppressed, delayed, steward-only, withheld, or public-safe. Missing exposure class blocks public use.
5. **Fail closed.** Unknown rights, unresolved sensitivity, missing source role, missing evidence, stale support, absent review, absent release state, or policy-engine failure **MUST NOT fall back to public allow**.
6. **Transform before delivery.** Sensitive geometry **MUST be transformed before** tile, API, export, search, graph, map, or AI delivery. Client-side filters, hidden layers, low opacity, zoom limits, or omitted popups are not sensitivity controls.
7. **Transform receipt.** Generalization, suppression, aggregation, buffering, grid/watershed/county projection, delay, or redaction **MUST emit a receipt** identifying input class, output class, policy basis, reason, reviewer where required, residual risk, and reproducible transform identity.
8. **Evidence closure.** A consequential or public-facing zone claim **MUST resolve through `EvidenceRef` to an admissible `EvidenceBundle`** or return a finite non-answer.
9. **Review boundary.** Sensitive, rights-constrained, exact, cross-domain, corrected, or public-facing zone products **MUST carry an attributable review state** appropriate to materiality.
10. **Release boundary.** Public exposure **MUST require** a governed release manifest, policy decision, public-safe artifact identity, correction path, rollback target, and stale/supersession behavior.
11. **Watcher boundary.** Watchers **MAY emit candidate changes and receipts**; they **MUST NOT publish, approve, overwrite canonical truth, or promote lifecycle state**.
12. **UI/AI boundary.** MapLibre, Evidence Drawer, exports, search, stories, dashboards, and AI **MUST display or explain the released posture**; they **MUST NOT infer missing permission or authority.**

### Public-safe projection rule

A public stewardship-zone projection is a separate, derived artifact—not a renamed canonical record. It must preserve a resolvable link to:

- the source descriptor and source-native locator;
- the internal/canonical zone identity or a privacy-preserving reference;
- the geometry transform and receipt;
- the evidence bundle;
- the policy decision and reason codes;
- review state;
- release manifest and artifact digest;
- correction/supersession lineage;
- rollback target.

The public projection **SHOULD minimize attributes** to the smallest set needed for the allowed claim. Internal steward names, contact details, restricted identifiers, exact easement/management notes, private access conditions, and sensitive cross-domain joins **MUST NOT be copied merely because the geometry was generalized**.

---

<a id="proposed-decision-matrix"></a>

## Proposed decision matrix

The executable policy may use surface-specific enums, but behavior must converge on a finite outward result. Policy-facing decisions may distinguish `ALLOW`, `RESTRICT`, `DENY`, `ABSTAIN`, and `ERROR`; governed runtime responses map to `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` as their contract requires.

| Condition | Policy disposition | Runtime/public disposition | Required obligations |
|---|---|---|---|
| Source role, rights, sensitivity, or evidence unresolved | `DENY` or `ABSTAIN`; hold/quarantine candidate | `ABSTAIN` or `DENY` | Record reason; do not expose; create verification task |
| Exact or steward-only geometry requested by an ordinary public client | `DENY` | `DENY` | Do not reveal existence/precision beyond allowed disclosure; audit attempt where policy requires |
| Sensitive cross-domain join (rare species, rare plants, archaeology/cultural context, infrastructure, private land/access) | `RESTRICT` or `DENY` | Public-safe `ANSWER`, `ABSTAIN`, or `DENY` | Apply most restrictive tier; transform before delivery; emit receipt; require review |
| Public-safe projection has source/rights/evidence/policy/review/release closure | `ALLOW` for the named projection only | `ANSWER` | Return release ID, evidence refs, transform posture, time scope, correction state |
| Request asks whether a zone proves ownership, access, legal status, management instruction, approval, or eligibility | `ABSTAIN` or `DENY` for unsupported inference | `ABSTAIN` or `DENY` | Explain context boundary; direct user to the actual authoritative source when available |
| Supporting source is stale, withdrawn, corrected, or superseded | `RESTRICT`, `ABSTAIN`, or `DENY` | Stale-state `ANSWER` only if contract permits; otherwise `ABSTAIN` | Display stale/correction state; block unsupported current claims; link successor/correction |
| Required review or release manifest is absent | `DENY` promotion | `ABSTAIN` or no public object | Keep candidate in WORK/QUARANTINE/CATALOG; do not infer publication from file existence |
| Policy engine, evidence resolver, transform verifier, or release resolver fails | `ERROR` and deny public exposure | `ERROR` | Fail closed; preserve diagnostic receipt without leaking restricted content |

---

<a id="placement-and-authority-boundaries"></a>

## Placement and authority boundaries

Directory Rules assign responsibilities by root. This ADR records the decision; it does not absorb the artifacts that enact it.

| Responsibility | Owning surface | Boundary |
|---|---|---|
| Decision rationale | `docs/adr/ADR-habitat-stewardship-zone-policy.md` | Proposed human decision record only |
| Habitat doctrine and lane context | `docs/domains/habitat/` | Explains domain ownership, lifecycle, and public posture |
| Object meaning | `contracts/domains/habitat/stewardship_zone.md` | Defines semantic contract; does not decide policy or release |
| Machine shape | `schemas/contracts/v1/domains/habitat/stewardship_zone.schema.json` | Field validation only; no policy or release authority |
| Domain admissibility | `policy/domains/habitat/stewardship_zone.rego` | Zone-role, evidence, review, and release gates |
| Cross-cutting sensitivity | `policy/sensitivity/habitat/` and applicable cross-domain policy | Most-restrictive sensitivity and geoprivacy rules |
| Enforceability proof | `tests/domains/habitat/test_stewardship_zone/` | Deterministic policy/schema/contract boundary tests |
| Synthetic examples | `fixtures/domains/habitat/stewardship_zone/` | Public-safe valid/invalid/denied/abstained/error examples only |
| Source identity and rights | `data/registry/sources/habitat/` | Source descriptors and activation posture |
| Lifecycle records | `data/<phase>/habitat/` | RAW/WORK/QUARANTINE/PROCESSED/CATALOG/PUBLISHED data as applicable |
| Transform/process memory | `data/receipts/` | Redaction/generalization/transform receipts; receipts are not truth or release |
| Evidence/proof closure | `data/proofs/` and catalog/evidence surfaces | Evidence support; not release authority |
| Release decision and rollback | `release/` and `release/manifests/habitat/` | Promotion, public scope, correction, withdrawal, rollback |
| Public delivery | governed API and released map artifacts | Downstream carrier only; never canonical/internal direct access |

### Parallel-authority prohibition

This ADR **MUST NOT** be used to create another stewardship policy, schema, contract, source registry, proof, receipt, or release home. If repository evidence reveals duplicates, the work must be recorded as drift and resolved through the approved migration/ADR route rather than by choosing whichever file is convenient.

---

<a id="required-evidence-and-release-packet"></a>

## Required evidence and release packet

A public or consequential `StewardshipZone` use should be supportable by the following packet. Exact field names remain PROPOSED until contracts/schemas are reviewed.

| Object or evidence | Minimum purpose |
|---|---|
| `SourceDescriptor` / activation decision | Source identity, role, authority limit, rights, cadence, citation, sensitivity, allowed use |
| Zone record | Stable ID, zone role, spatial/temporal scope, source refs, exposure class, sensitivity tier |
| `EvidenceRef` / `EvidenceBundle` | Resolvable support for the zone and any public interpretation |
| Rights/sensitivity decision | Permitted use, restrictions, obligations, reason codes, inherited tier |
| Geometry-transform receipt | Reproducible exact-to-public-safe transform, residual risk, reviewer where required |
| Validation report | Contract/schema/geometry/time/source-role/evidence/policy checks |
| Review record | Accountable review bound to exact subject/version where material |
| Public artifact manifest | Digest, bounds, zoom/scale limits, attribute allowlist, source/evidence/release refs |
| Release manifest / promotion decision | Public scope, approved artifact set, prior release, rollback target |
| Correction or supersession record | Changed/withdrawn facts and successor lineage |
| Rollback card | Restorable prior release and cache/search/tile invalidation steps |

### Minimum public payload posture

A public payload **SHOULD expose**:

- public zone ID or privacy-preserving reference;
- public-safe role/label;
- generalized or aggregate spatial scope;
- valid/source/release time as applicable;
- source role and citation;
- evidence lookup reference;
- policy/release posture;
- transform/generalization notice;
- stale/correction state;
- release ID.

A public payload **MUST NOT expose** merely because it exists internally:

- exact sensitive geometry;
- internal steward identities or contact details;
- private access rules or operational notes;
- restricted program identifiers;
- rare-species, rare-plant, archaeology/cultural, infrastructure, or land/access joins beyond the approved projection;
- raw source URLs or internal storage handles that bypass governed access;
- hidden model reasoning or generated assertions as evidence.

---

<a id="authority-and-publication-boundary"></a>

## Authority and publication boundary

This ADR is documentation. It does not enact policy, validate a record, approve a source, create an evidence bundle, issue a review record, generate a public-safe projection, or make a release.

The following are not publication authority:

- this Markdown file;
- a commit, pull request, merge, badge, or green documentation workflow;
- the presence of a JSON Schema or Rego file;
- a passing fixture or test;
- a watcher signal;
- a tile, PMTiles archive, API response, map layer, popup, screenshot, dashboard, graph edge, export, or AI answer.

KFM publication requires the governed release objects and gates appropriate to the claim's significance. A public client must read the released projection through the governed interface, not the canonical/internal record directly.

---

<a id="current-repository-evidence"></a>

## Current repository evidence

| Surface | CONFIRMED state at the evidence snapshot | What it proves | What it does not prove |
|---|---|---|---|
| Target ADR | 18-line proposed scaffold existed at this path | The path and planned topic existed | A decision, accepted status, or policy implementation |
| Habitat architecture | Defines `StewardshipZone`, T1 default, public-safe and review posture | Domain vocabulary and proposed lane rules | Enforced schema, policy, release, or public behavior |
| Canonical paths | Places contract/schema/policy/test/source/release surfaces in responsibility roots | Placement relationship | That every path is complete or active |
| Semantic contract | Rich context-not-authority boundary and proposed field semantics | Object meaning and anti-collapse intent | Field enforcement, source activation, policy pass, release |
| JSON Schema | Draft 2020-12 object with empty properties, no required fields, `additionalProperties: true` | A paired scaffold exists | Meaningful machine validation |
| Rego policy | Package plus `default allow := false` | Default deny posture at scaffold level | Decision reasons, obligations, transforms, tests, runtime integration |
| Habitat fixtures index | Documents synthetic no-network fixture discipline | Intended fixture boundary | Object-specific payload inventory or coverage |
| Habitat tests index | Lists StewardshipZone test lane | Intended enforceability surface | Executable modules, pass rate, CI coverage |
| StewardshipZone tests README | Defines invariants, finite outcomes, suggested modules, and checklist | Expected test behavior | Implemented tests or successful execution |
| Docs workflow | Runs ADR inventory validation on pull requests | Changed ADR inventory coherence can be checked | Decision acceptance, policy correctness, release, publication |

---

<a id="current-enforcement-maturity"></a>

## Current enforcement maturity

| Control | Current maturity | Required next evidence |
|---|---|---|
| ADR identity | Unassigned scaffold | Permanent number, filename/H1/index agreement, validator pass |
| Semantic contract | Draft, substantive | Reviewed contract version and explicit compatibility posture |
| Machine schema | Permissive scaffold | Required fields, enums, conditionals, references, valid/invalid fixtures, registry entry |
| Domain policy | Default-deny scaffold | Finite decision object, reason codes, obligations, tests, OPA/Conftest execution |
| Sensitivity/geoprivacy policy | Referenced, not verified here | Most-restrictive join rules, transform receipts, reviewer requirements |
| Fixtures | Parent guidance confirmed | Object-specific valid, invalid, restricted, generalized, stale, corrected, denied, abstained, and error fixtures |
| Tests | README lane confirmed | Executable no-network tests and observed results |
| Source activation | Unknown | Reviewed source descriptors, rights/terms, allowed-use and precision posture |
| Evidence resolution | Unknown | EvidenceRef/EvidenceBundle fixtures, resolver checks, citation validation |
| Public-safe projection | Unknown | Transform implementation, digest, attribute allowlist, residual-risk review |
| Release/correction/rollback | Unknown | Release manifest, promotion decision, correction/withdrawal, rollback drill |
| API/UI/AI | Unknown | Governed integration tests proving no direct internal-store or exact-geometry exposure |

> [!IMPORTANT]
> Until these controls close, the safe operational interpretation is: **the object family is documented, but no public stewardship-zone release is proven.**

---

<a id="implementation-and-convergence-plan"></a>

## Implementation and convergence plan

This sequence is PROPOSED. Each step should be a small, reviewable change with explicit validation and rollback.

1. **Assign ADR identity.** Check the live index, open PRs, and branches; claim the next permanent ID; rename/H1-update this file; update `docs/adr/INDEX.md`; run ADR validation.
2. **Confirm decision owners and reviewers.** Replace role placeholders only with verified repository governance evidence.
3. **Reconcile semantic contract.** Review `stewardship_zone.md` against this ADR; version any material semantic change; preserve context-not-authority exclusions.
4. **Harden the schema.** Add required identity, role, source, time, exposure, sensitivity, evidence, policy/review/release, correction, and rollback references. Reject unknown critical fields; document compatibility.
5. **Implement policy.** Replace the minimal scaffold with finite outcomes, reason codes, transform obligations, most-restrictive join behavior, stale/correction behavior, and fail-closed errors.
6. **Add fixtures.** Create compact synthetic fixtures for public-safe, exact restricted, missing rights, missing role, sensitive join, stale, corrected, superseded, policy error, and unsupported-authority inference cases.
7. **Add executable tests.** Prove schema/contract/policy parity, context-not-authority rules, pre-delivery transformation, evidence closure, review/release gates, correction, rollback, and no direct public-store access.
8. **Verify source descriptors.** Review source roles, rights, citation, precision, cadence, public-use obligations, and steward contacts for each source family before activation.
9. **Implement public-safe projection.** Create deterministic transformation and receipt generation; maintain exact/canonical and released/public-safe identities separately.
10. **Close release behavior.** Add artifact/release manifests, promotion decision, correction/withdrawal path, rollback card, and cache/search/tile invalidation test.
11. **Integrate governed clients.** Prove API, MapLibre, Evidence Drawer, exports, and AI use released public-safe artifacts and expose negative/stale/correction states.
12. **Observe CI.** Run repository-native validators and tests; treat green checks as bounded evidence, not decision acceptance or publication authority.

### Smallest implementation slice

The first proof should remain fixture-first and no-network:

```text
synthetic exact/internal zone fixture
  -> schema + semantic validation
  -> source/rights/sensitivity policy
  -> deterministic public-safe transform + receipt
  -> EvidenceBundle fixture
  -> review/release fixture
  -> public payload/layer fixture
  -> denied exact-public request
  -> correction + rollback fixture
```

This slice proves the boundary without activating a live source or publishing real geometry.

---

<a id="acceptance-gates"></a>

## Acceptance gates

This ADR must remain `proposed` until reviewers can mark all required gates complete with evidence.

- [ ] Permanent ADR ID is assigned without collision; filename, H1, meta block, and canonical index agree.
- [ ] Architecture, Habitat, policy/sensitivity, source/rights, evidence, release/correction/rollback, validation, and docs reviewers are identified from repository governance evidence.
- [ ] Semantic contract and ADR agree on context-not-authority boundaries.
- [ ] Machine schema has reviewed required fields and rejects unsafe/incomplete records.
- [ ] Policy returns finite decisions, reason codes, and obligations and fails closed on errors or unknowns.
- [ ] Most-restrictive sensitivity inheritance is tested across Habitat × Fauna/Flora/archaeology/infrastructure/land-access seams where applicable.
- [ ] Exact-to-public-safe transforms are deterministic, receipt-bearing, and tested for residual disclosure.
- [ ] Valid, invalid, restricted, generalized, stale, corrected, denied, abstained, and error fixtures exist.
- [ ] Executable no-network tests run in CI and negative paths fail as intended.
- [ ] Source descriptors and rights/terms reviews exist for every activated source.
- [ ] EvidenceRef resolves to EvidenceBundle for every consequential/public fixture claim.
- [ ] Public artifact and layer manifests include digest, scope, attribute allowlist, evidence, policy, release, correction, and rollback references.
- [ ] Governed API/UI/AI tests prove no direct canonical/internal-store or exact-sensitive-geometry access.
- [ ] Correction, withdrawal, supersession, stale-state, rollback, and cache invalidation are demonstrated.
- [ ] Explicit human review accepts or rejects the decision; a green workflow alone does not transition status.

---

<a id="consequences"></a>

## Consequences

### Positive

- Preserves a stable Habitat vocabulary while preventing stewardship context from becoming legal, operational, management, or release authority.
- Makes source role, geometry exposure, sensitivity, evidence, time, review, and release state visible and testable.
- Prevents client-side hiding and map presentation from masquerading as geoprivacy.
- Gives schema, policy, fixture, test, registry, release, API, map, and AI work one coherent decision boundary.
- Supports public-safe Habitat context without requiring blanket suppression of all stewardship information.
- Makes corrections and rollbacks part of the release design rather than afterthoughts.

### Negative

- Increases source-onboarding and release burden for stewardship-zone data.
- Requires separate internal/canonical and public-safe artifacts and identities.
- Requires policy, transform, evidence, review, and release tooling before public use.
- May reduce spatial precision, attributes, or availability in public surfaces.
- Tightening the permissive schema can invalidate existing ungoverned examples or records.

### Accepted tradeoffs

- **Less public precision for lower disclosure risk.** Public utility does not justify exposing exact sensitive or access-relevant context.
- **More abstentions/denials for stronger trust.** It is preferable to return a visible non-answer than infer permission or authority.
- **More object separation for auditability.** Zone, ownership/access authority, policy decision, review record, release manifest, and public artifact remain distinct even when a simpler flattened record would be easier to render.
- **Fixture-first delivery over live-source speed.** The first proof prioritizes deterministic governance over broad coverage.

---

<a id="alternatives-considered"></a>

## Alternatives considered

### Alternative A — Treat all stewardship zones as T0 public context

**Summary:** Publish source geometry and basic attributes whenever the upstream dataset is publicly accessible.

**Rejected because:** Public availability does not establish KFM rights posture, safe precision, attribute safety, current validity, cross-domain sensitivity, or permission to infer access/authority. Stewardship context sits close to rare-species, private-land, access, cultural, and infrastructure risks.

### Alternative B — Publish exact geometry and hide sensitive records in the browser

**Summary:** Deliver all geometry to the client and use style filters, zoom thresholds, role-based UI controls, or omitted popups.

**Rejected because:** Client-side hiding is not a sensitivity control. The bytes, tile features, network responses, caches, exports, or developer tools can expose the withheld information.

### Alternative C — Let `StewardshipZone` include ownership, access, management, approval, and eligibility

**Summary:** Flatten related administrative and legal meaning into one convenient map object.

**Rejected because:** This collapses distinct source roles and authorities, creates unsupported inferences, and makes correction/release governance ambiguous. Ownership/title/access and regulatory/eligibility decisions require their own authoritative evidence and domains.

### Alternative D — Put all rules in the semantic contract

**Summary:** Keep one detailed Markdown contract and avoid a separate ADR and policy implementation.

**Rejected because:** Contracts define meaning; policy decides admissibility; schemas define shape; tests prove enforceability; release objects authorize public state. One document cannot safely replace those authority surfaces.

### Alternative E — Keep the scaffold and decide case by case

**Summary:** Avoid a normative decision until live data arrives.

**Rejected because:** The current permissive schema and minimal policy scaffold create a predictable drift risk. Case-by-case handling would make source role, sensitivity, public projection, review, and release behavior inconsistent and difficult to test.

---

<a id="risk-and-open-question-ledger"></a>

## Risk and open-question ledger

| Risk or question | Current status | Required resolution |
|---|---|---|
| Permanent ADR number and index row | NEEDS VERIFICATION | Separate scoped numbering/index PR with collision check |
| Accountable decision owners and independent reviewers | NEEDS VERIFICATION | CODEOWNERS/governance assignments and explicit review record |
| Final sensitivity-tier vocabulary and T1 meaning | NEEDS VERIFICATION | Confirm against current accepted sensitivity contract/policy |
| Which source families may support zones | NEEDS VERIFICATION | Source descriptors with role, rights, terms, precision, citation, cadence |
| Whether public exact boundaries are ever allowed | PROPOSED default: no unless explicitly reviewed | Source- and claim-specific policy plus residual-risk review |
| Schema tightening compatibility | UNKNOWN | Inventory any existing records/fixtures; migration/quarantine plan |
| Policy outcome enum | NEEDS VERIFICATION | Align with current policy and runtime contracts without inventing a universal enum |
| Cross-domain most-restrictive inheritance | PROPOSED | Policy tests for Fauna, Flora, archaeology/cultural, infrastructure, and land/access seams |
| Steward identity/contact disclosure | PROPOSED restricted by default | Attribute allowlist and privacy review |
| Stale/superseded source behavior | NEEDS VERIFICATION | Freshness policy, stale badge, abstention, correction/successor links |
| Public cache/search/tile withdrawal | UNKNOWN | Release rollback and invalidation runbook/tests |
| Existing public clients or layers | UNKNOWN | Repository/runtime inventory and governed integration tests |
| Emergency or operational use | Out of scope / denied as authority | Explicit UI disclaimer and authoritative-channel routing where applicable |

---

<a id="migration-and-compatibility"></a>

## Migration and compatibility

This documentation update moves no file and changes no machine contract. Future adoption can still create a breaking machine-shape transition because the current schema accepts arbitrary objects.

Before schema/policy enforcement:

1. inventory any existing stewardship-zone fixtures and lifecycle records;
2. classify them as valid, migratable, quarantined, or unresolvable;
3. version the schema/contract when semantics or required fields change materially;
4. create deterministic migration or normalization receipts;
5. do not infer missing rights, sensitivity, source role, exposure class, evidence, review, or release state;
6. quarantine records that cannot be made safe without guesswork;
7. preserve old-to-new identity and correction lineage;
8. test old consumer behavior and public-carrier denial before activating new enforcement.

No compatibility mirror may become a second schema, policy, source, proof, receipt, or release authority.

---

<a id="rollback-and-supersession"></a>

## Rollback and supersession

### Documentation rollback before acceptance

- Revert the implementation commit or close the unmerged draft PR.
- Preserve this file as an unassigned proposed scaffold unless a reviewed cleanup explicitly retires or numbers it.
- Do not rewrite shared history.

### Implementation rollback after adoption

Any implementation must define rollback for:

- schema version and record migration;
- policy bundle and reason-code behavior;
- source activation;
- public-safe transform version;
- layer/API/export artifact;
- release manifest and alias/current pointer;
- search, cache, tile, and CDN invalidation;
- correction/withdrawal notice;
- restoration of the prior public-safe release.

Rollback does not erase correction history. If an accepted version of this decision is replaced, retain it and link both directions to the accepted successor ADR.

---

<a id="validation"></a>

## Validation expectations

For this Markdown revision:

- one H1;
- balanced fenced code blocks;
- valid GitHub alert syntax;
- meaningful badge alt text and anchor destinations;
- repo-relative links only to inspected or explicitly marked directory surfaces;
- no claim that documentation checks accept the ADR or implement policy;
- no unrelated file changes.

For later implementation:

```bash
python tools/validators/validate_adr_index.py
python -m pytest tests/validators/test_validate_adr_index.py -q --strict-config --strict-markers
pytest tests/domains/habitat/test_stewardship_zone
```

The first two commands are repository-documented ADR inventory checks. The StewardshipZone command remains **NEEDS VERIFICATION** until executable modules and the accepted test runner are confirmed. A passing check proves only its bounded assertion; it does not approve policy, release data, or publish a layer.

---

<a id="references"></a>

## References

### Governing repository evidence

- [`docs/adr/README.md`](./README.md) — ADR identity, lifecycle, index, review, and validation contract.
- [`docs/adr/ADR-template.md`](./ADR-template.md) — required ADR sections and status discipline.
- [`docs/doctrine/directory-rules.md`](../doctrine/directory-rules.md) — responsibility-root placement, no-parallel-authority, lifecycle, and migration rules.
- [`docs/domains/habitat/ARCHITECTURE.md`](../domains/habitat/ARCHITECTURE.md) — Habitat object families, T1 stewardship-zone default, sensitivity, validation, and release posture.
- [`docs/domains/habitat/CANONICAL_PATHS.md`](../domains/habitat/CANONICAL_PATHS.md) — Habitat responsibility-root crosswalk.
- [`contracts/domains/habitat/stewardship_zone.md`](../../contracts/domains/habitat/stewardship_zone.md) — semantic context-not-authority contract.
- [`schemas/contracts/v1/domains/habitat/stewardship_zone.schema.json`](../../schemas/contracts/v1/domains/habitat/stewardship_zone.schema.json) — current permissive schema scaffold.
- [`policy/domains/habitat/stewardship_zone.rego`](../../policy/domains/habitat/stewardship_zone.rego) — current default-deny policy scaffold.
- [`fixtures/domains/habitat/README.md`](../../fixtures/domains/habitat/README.md) — Habitat fixture boundary and current child inventory.
- [`tests/domains/habitat/README.md`](../../tests/domains/habitat/README.md) — Habitat test boundary and object-family lane inventory.
- [`tests/domains/habitat/test_stewardship_zone/README.md`](../../tests/domains/habitat/test_stewardship_zone/README.md) — StewardshipZone test expectations and current verification limits.
- [`.github/workflows/docs-control-plane.yml`](../../.github/workflows/docs-control-plane.yml) — read-only documentation and ADR inventory checks.

### Referenced responsibility surfaces requiring later verification

- `policy/sensitivity/habitat/`
- `fixtures/domains/habitat/stewardship_zone/`
- `data/registry/sources/habitat/`
- `data/receipts/`
- `data/proofs/`
- `release/manifests/habitat/`
- governed API, MapLibre, Evidence Drawer, export, and AI integration surfaces

---

<a id="revision-history"></a>

## Revision history

| Date | Version | Change | Decision effect |
|---|---|---|---|
| Before 2026-07-24 | Scaffold | 18-line placeholder referencing Habitat architecture | None; unassigned proposed scaffold |
| 2026-07-24 | v1.0 | Same-path, repository-grounded replacement with context boundary, policy matrix, evidence packet, convergence plan, acceptance gates, migration, and rollback | None; remains unassigned and proposed |

---

## Final operating rule

**Stewardship context may inform Habitat interpretation, but it never grants authority.** When source role, rights, sensitivity, evidence, review, release, correction, or rollback support is incomplete, KFM narrows, generalizes, holds, abstains, denies, or errors—it does not guess and it does not expose exact material by default.

<p align="right"><a href="#top">Back to top</a></p>

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-readme
title: Domain Contracts README
type: root-readme; governance-index; contract-authoring-guide
version: v0.2
status: draft; repo-facing; responsibility-root-index; implementation-bounded; NEEDS STEWARD REVIEW
owners:
  - OWNER_TBD — Contracts steward
  - OWNER_TBD — Domain stewards
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — placeholder existed before v0.2 expansion
updated: 2026-06-24
policy_label: public; contracts; domains; semantic-contracts; responsibility-root; directory-rules; trust-membrane; evidence-first; release-gated; rollback-aware; not-schema; not-policy; not-data; not-source-registry; not-release-approval; not-runtime-proof
tags: [kfm, contracts, domains, README, semantic-contracts, Domain Placement Law, Directory Rules, contracts-root, schemas, policy, fixtures, tests, data, release, EvidenceBundle, SourceDescriptor, PolicyDecision, ReviewRecord, ReleaseManifest, RollbackCard, AIReceipt]
related:
  - ../README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/doctrine/truth-posture.md
  - ../../docs/doctrine/trust-membrane.md
  - ../../docs/doctrine/lifecycle-law.md
  - ../../docs/architecture/contract-schema-policy-split.md
  - ../../schemas/contracts/v1/
  - ../../policy/domains/
  - ../../fixtures/domains/
  - ../../tests/domains/
  - ../../data/
  - ../../release/
notes:
  - "Expanded from a minimal placeholder: '# Domain contracts'."
  - "This README indexes the purpose, boundaries, authoring rules, and review posture for domain-specific semantic contracts."
  - "Contracts define meaning. Schemas define machine shape. Policy defines admissibility. Tests/fixtures prove enforcement. Data and release roots govern lifecycle and publication."
  - "This README is not an exhaustive live inventory of every domain contract file. Use repo search or generated manifests for complete inventory."
  - "The Roads/Rail/Trade transport slug conflict is explicitly called out because existing contract/schema scaffolds include a conflicted hybrid path."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Domain Contracts

> Domain-specific semantic contracts for KFM object families. These files define **what domain objects mean**. They do not define JSON shape, policy permission, source registry authority, executable pipelines, release approval, public API behavior, map rendering, graph truth, or AI answer truth.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts/domains" src="https://img.shields.io/badge/root-contracts%2Fdomains%2F-0a7ea4">
  <img alt="Purpose: semantic meaning" src="https://img.shields.io/badge/purpose-semantic__meaning-blue">
  <img alt="Lifecycle: release gated" src="https://img.shields.io/badge/lifecycle-release__gated-green">
  <img alt="Truth: evidence first" src="https://img.shields.io/badge/truth-evidence__first-purple">
  <img alt="Boundary: not schemas" src="https://img.shields.io/badge/boundary-not__schemas-critical">
</p>

`contracts/domains/README.md`

## Quick jumps

[Purpose](#purpose) · [Authority boundary](#authority-boundary) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Placement rule](#placement-rule) · [Authoring rule](#authoring-rule) · [Contract maturity](#contract-maturity) · [Observed lanes](#observed-lanes) · [Known conflicts](#known-conflicts) · [Review checklist](#review-checklist) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Purpose

`contracts/domains/` is the home for **domain-specific object meaning**.

A domain contract answers questions like:

- What does this object mean inside its bounded context?
- What is the object allowed to assert?
- What is explicitly out of scope?
- Which source roles, support types, evidence refs, time facets, policy decisions, reviews, releases, and rollback targets must remain visible?
- Which adjacent domain owns related truth?
- Which public surfaces may expose this object after validation, policy, review, release, and rollback gates close?

This root should help authors avoid turning generated Markdown, layer manifests, graphs, tiles, summaries, UI payloads, or AI answers into sovereign truth.

---

## Authority boundary

| Responsibility | Home | Rule |
|---|---|---|
| Semantic meaning | `contracts/domains/<domain>/...` | This root. Defines what domain objects mean. |
| Cross-domain object meaning | `contracts/<family>/...` | Use when the object is not owned by one domain lane. |
| Machine shape | `schemas/contracts/v1/...` | JSON Schema and machine-enforced field shape. |
| Policy/admissibility | `policy/domains/<domain>/...` | Allow, deny, restrict, abstain, sensitivity, source-role, rights, release gates. |
| Fixtures | `fixtures/domains/<domain>/...` | Valid/invalid/golden examples. |
| Tests | `tests/domains/<domain>/...` | Enforcement proof and negative-state tests. |
| Source registry | `data/registry/sources/...` or source-specific registry roots | SourceDescriptor and source authority metadata. |
| Data lifecycle | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/published` | RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED. |
| Release/correction/rollback | `release/...` | ReleaseManifest, correction path, RollbackCard, release decisions. |
| Pipeline implementation | `pipelines/`, `pipeline_specs/`, `packages/`, `tools/` | Executable or reusable implementation. |
| Public delivery | governed API, published artifacts, layer manifests, Evidence Drawer projections | Public clients do not read internal lifecycle stores. |

> [!IMPORTANT]
> **Contract says meaning. Schema says shape. Policy says whether/how. Pipeline says how. Release decides publication. EvidenceBundle outranks all generated text.**

---

## What belongs here

Place a file under `contracts/domains/<domain>/` when all of these are true:

1. The object belongs to a specific domain lane.
2. The file defines semantic meaning, boundaries, required evidence posture, public-use limitations, and related authority roots.
3. The file is human-readable Markdown for maintainers, reviewers, API authors, schema authors, validators, map authors, and governed-AI authors.
4. The file does not implement validation, ETL, policy, source admission, release, map rendering, or runtime behavior.

Examples of suitable files:

```text
contracts/domains/soil/soil_map_unit.md
contracts/domains/soil/soil_property.md
contracts/domains/fauna/taxon.md
contracts/domains/hydrology/watershed.md
contracts/domains/habitat/corridor.md
contracts/domains/settlement/README.md
```

These are examples of contract-lane placement. They are not a complete inventory.

---

## What does not belong here

Do **not** place the following in `contracts/domains/`:

| Item | Correct home |
|---|---|
| JSON Schema | `schemas/contracts/v1/...` |
| Policy code or policy registers | `policy/` |
| Valid/invalid examples | `fixtures/` |
| Tests or validators | `tests/`, `tools/validators/` |
| Source descriptors | source registry / `data/registry/sources/...` |
| Raw source data | `data/raw/...` |
| Normalized candidate records | `data/work`, `data/quarantine`, `data/processed` |
| Catalog, STAC/DCAT/PROV, EvidenceBundle records | `data/catalog`, catalog/proof roots |
| Published tiles/layers/artifacts | `data/published`, release-governed artifact roots |
| ReleaseManifest / RollbackCard | `release/...` |
| Pipelines or scripts | `pipelines/`, `pipeline_specs/`, `packages/`, `tools/` |
| UI payload rendering code | app/UI/viewer roots |
| AI prompts or model runtime outputs as truth | governed runtime roots plus EvidenceBundle-backed receipts |

---

## Placement rule

Use this sequence before adding or moving a file:

1. Identify the primary responsibility root.
2. Identify the owning domain lane.
3. Check the domain-specific README or canonical-path doc.
4. Check for ADRs or known slug conflicts.
5. Use the smallest reversible change.
6. Keep lifecycle and publication boundaries intact.

For a domain semantic contract, the default shape is:

```text
contracts/domains/<domain>/<object-or-contract-name>.md
```

But a domain-specific ADR or documented conflict may override or pause this default. Do not create parallel homes for the same object without a migration note or ADR.

---

## Authoring rule

Every domain contract should include, as appropriate:

- KFM Meta Block v2;
- clear truth/status labels: `CONFIRMED`, `PROPOSED`, `NEEDS VERIFICATION`, `UNKNOWN`, `CONFLICTED`, `DENY`, `ABSTAIN`, or `ERROR`;
- a one-paragraph semantic definition;
- explicit exclusions;
- schema posture: schema-confirmed, schema-stub-confirmed, schema-missing, or schema-conflicted;
- source role and support type requirements;
- all material time facets;
- EvidenceRef / EvidenceBundle requirements;
- sensitivity, rights, and public-use limitations;
- validation expectations and negative-state tests;
- release, correction, and rollback requirements;
- related docs, schemas, policy roots, tests, fixtures, data lifecycle, and release roots;
- open questions when authority is unresolved.

> [!WARNING]
> Do not write “the system does X” unless current repo evidence, schema, test, release, or runtime proof supports it. If proof is missing, use `PROPOSED` or `NEEDS VERIFICATION`.

---

## Contract maturity

| Maturity | Meaning | Public posture |
|---|---|---|
| `scaffold` | File exists only as a placeholder or generated path marker. | Not authoritative. Replace before use. |
| `draft` | Human-readable semantic contract exists. | Not enough for public release by itself. |
| `schema-missing` | No paired schema confirmed. | Fields are PROPOSED. |
| `schema-stub-confirmed` | Paired schema exists but is permissive/incomplete. | Fields remain PROPOSED until schema/validators mature. |
| `schema-aligned` | Contract fields and schema shape agree. | Still requires policy/test/release gates. |
| `validated` | Fixtures/tests/validators prove expected positive and negative states. | Still not published until release gates close. |
| `released` | Policy/review/release/rollback artifacts exist. | Public clients may consume only governed projections. |
| `corrected` / `rolled-back` | Correction/rollback has been recorded. | Dependent layers, drawers, graph projections, exports, and AI summaries must be invalidated or repointed. |

---

## Observed lanes

This README is not a full inventory. Current repo searches and file reads have shown examples under the following domain lanes:

| Lane | Example posture |
|---|---|
| `soil/` | Multiple expanded semantic contracts; some paired schemas are missing or stubs. |
| `fauna/` | README and object contracts observed by repo search. |
| `hydrology/` | Object contracts observed by repo search. |
| `habitat/` | Object contracts observed by repo search. |
| `geology/` | Object contracts observed by repo search. |
| `settlement/` | README observed by repo search. |
| `roads-rail-trade/` | Domain lane exists in docs and some contracts; schema/contract slug remains conflicted with `transport`. |
| `transport/` | Existing hybrid scaffolds observed; keep path-conflicted until ADR resolves home. |

A generated manifest or repository tree audit should be used for a complete inventory.

---

## Known conflicts

### Roads / Rail / Trade versus Transport

The Roads/Rail/Trade lane has an unresolved schema/contract-home conflict.

Current evidence shows:

| Form | Status |
|---|---|
| `contracts/domains/roads-rail-trade/` | Directory Rules-style / lane-pattern form. |
| `contracts/transport/` | Atlas crosswalk-style engineering form. |
| `contracts/domains/transport/` | Existing repo scaffolds, but documented as a fabricated hybrid in the lane registry. |

Until an ADR resolves the conflict:

- do not promote `contracts/domains/transport/` files as canonical authority;
- do not create parallel canonical road/rail/trade contract homes;
- mark affected files `PATH-CONFLICTED`;
- record rollback and migration targets;
- prefer bounded semantic cleanup over broad moves.

---

## Review checklist

Before a domain contract is promoted beyond draft, reviewers should verify:

- [ ] correct responsibility root and domain lane;
- [ ] no parallel contract home exists for the same object;
- [ ] paired schema home is known or schema-missing/stub/conflict is clearly marked;
- [ ] source role is explicit;
- [ ] support type is explicit where the domain needs it;
- [ ] material time facets are separated;
- [ ] EvidenceRef can resolve to EvidenceBundle for consequential claims;
- [ ] policy, sensitivity, rights, review, release, correction, and rollback references are planned or present;
- [ ] validation and negative-state tests are named;
- [ ] public clients are directed to governed APIs/released artifacts only;
- [ ] AI surfaces are evidence-subordinate and cite-or-abstain;
- [ ] rollback target is recorded for material edits.

---

## Rollback

Rollback this README if it:

- creates or endorses a new authority root without ADR support;
- treats `contracts/domains/` as schema, policy, test, data, source registry, release, pipeline, UI, or runtime authority;
- hides known path conflicts;
- claims implementation maturity without proof;
- weakens the RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED invariant;
- normalizes public clients reading internal lifecycle stores;
- allows generated language or AI output to outrank EvidenceBundle.

Rollback target: prior placeholder blob `890877c263286137c92328ab6f396d04c08f38a1`, followed by a drift note explaining why the richer README was reverted.

---

## Open questions

| ID | Question | Status |
|---|---|---|
| OQ-CONTRACTS-DOMAINS-01 | Should this root maintain a generated manifest of every domain contract, schema posture, and review state? | OPEN / DOCS + TOOLING REVIEW |
| OQ-CONTRACTS-DOMAINS-02 | Should domain contract files use snake_case, kebab-case, or source-preserving names where existing files conflict? | OPEN / STYLE + MIGRATION REVIEW |
| OQ-CONTRACTS-DOMAINS-03 | Which ADR will resolve the Roads/Rail/Trade versus Transport contract/schema home conflict? | OPEN / ADR REQUIRED |
| OQ-CONTRACTS-DOMAINS-04 | Should every domain lane require its own `contracts/domains/<domain>/README.md` before object contracts can be promoted? | OPEN / GOVERNANCE REVIEW |
| OQ-CONTRACTS-DOMAINS-05 | Should contract maturity be machine-indexed in a register under `control_plane/`? | OPEN / CONTROL-PLANE REVIEW |

<p align="right"><a href="#top">Back to top</a></p>

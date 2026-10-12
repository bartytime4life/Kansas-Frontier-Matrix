<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/examples/readme
title: examples/ — Governed Worked-Example Root
type: readme; root-readme; canonical-examples-root; non-authoritative-demonstration-boundary
version: v0.4.0
status: repository-grounded draft; mixed static and validator-backed examples; non-authoritative
updated: 2026-08-08
supersedes: v0.3.0 at the same path
prepared_under_prompt: KFM Repository Build-Out & Markdown Modernization Implementation Agent v6.0.0
current_path: examples/README.md
policy_label: public-review; synthetic-first; fail-closed; no-public-authority; cite-or-abstain
truth_posture: >
  CONFIRMED same-path canonical examples root, adopted Directory Rules v2.0.0 through
  ADR-0029, DIR-ROOT-EXAMPLES, nine direct child lanes, nine child READMEs, five
  substantive example artifacts, two placeholder files, validator-backed briefing examples,
  bounded changed-Markdown link checking, and explicit documentation/accessibility holds at
  main@0ab94b49111fad3801f3ab3da4afb6433cc14d23 / PROPOSED the maturity vocabulary
  and root admission checklist below / UNKNOWN runtime parity, deployed consumers, third-party
  sample licensing, and public effects / NEEDS VERIFICATION accountable owners, dedicated
  CODEOWNERS routing, root-wide example validation, host rendering, accessibility execution,
  currentness policy, correction propagation, and retirement drills
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: 0ab94b49111fad3801f3ab3da4afb6433cc14d23
  prior_blob: d3fbce80c82106935288d59a708bbb1a0118591e
  examples_tree: 750a5c39b08ab6c4b4b39851bfee498e3a5ea137
  root_registry_entry: DIR-ROOT-EXAMPLES
related:
  - ../docs/doctrine/directory-rules.md
  - ../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../control_plane/root_registry.yaml
  - ../.github/workflows/briefing-integration.yml
  - ../.github/workflows/link-check.yml
  - ../.github/workflows/docs-build.yml
  - ../.github/workflows/accessibility.yml
notes:
  - Markdown-only same-path modernization; no operational object or authority state changes.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `examples/` — Governed Worked-Example Root

> **Purpose.** `examples/` holds small, reviewable, preferably synthetic demonstrations of KFM contracts, flows, finite failure states, and trust boundaries. It is canonical **for examples only**—never for the source truth, evidence, policy, runtime, release, or publication state an example depicts.

> [!IMPORTANT]
> A polished example, valid payload, passing workflow, merged pull request, screenshot, or persuasive walkthrough does not establish evidence closure, policy permission, runtime parity, release approval, or KFM publication.

> [!WARNING]
> Maturity is mixed. `briefing_integration/` has repository-owned deterministic validation; most other lanes are README-only or static walkthroughs. Do not describe the whole root as runnable or validated.

**Navigate:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Inventory](#current-bounded-inventory) · [Maturity](#example-maturity-model) · [Contract](#example-contract) · [Safety](#sensitive-data-and-safety-posture) · [Maintenance](#maintenance-correction-and-rollback) · [Verification](#open-verification-register)

## Purpose

Examples make doctrine inspectable. A useful example demonstrates at least one of these:

- the smallest understandable success path;
- a finite negative state such as `ABSTAIN`, `DENY`, `ERROR`, `HOLD`, or `QUARANTINE`;
- the boundary between illustrative shape and operational authority;
- the relationship between an example and its owning contract, schema, policy, validator, fixture, test, app, package, lifecycle record, proof, receipt, or release object;
- source role, time, evidence, rights, sensitivity, correction, and rollback where material.

Examples become harmful when readers cannot tell where instruction ends and governed behavior begins.

<a id="authority-posture"></a>

## Authority level

| Surface | Posture |
|---|---|
| `examples/` | Canonical responsibility root for examples; registered as `DIR-ROOT-EXAMPLES`. |
| Example content | Non-authoritative demonstration. |
| Meaning and shape | Owned by `contracts/` and `schemas/`; examples must not create a competing definition. |
| Admissibility and exposure | Owned by `policy/`, evidence, review, and release controls. |
| Fixture or test status | Not automatic; graduation requires a separately reviewed artifact under `fixtures/` or `tests/`. |
| Publication | Denied by placement. Commit or merge is not promotion. |

This update stays at the existing tracked path, changes no ownership or lifecycle boundary, and creates no new authority surface.

<a id="status-notes"></a>

## Status

| Finding | Result |
|---|---|
| Placement | `CONFIRMED` — adopted Directory Rules v2.0.0 and `DIR-ROOT-EXAMPLES`. |
| Inventory | `CONFIRMED BOUNDED` — nine lanes, nine child READMEs, five substantive artifacts, two `.gitkeep` placeholders. |
| Validation | `MIXED` — briefing examples have deterministic validators; changed Markdown has a bounded local link check. |
| Documentation build | `WORKFLOW_HOLD` — no accepted generator or preview-publication handoff. |
| Accessibility | `WORKFLOW_HOLD` — axe and keyboard-navigation checks are not executed. |
| Runtime/public effect | `UNKNOWN` or `DENY` — placement and validation prove neither. |
| Ownership | `NEEDS VERIFICATION` — no dedicated `/examples/` CODEOWNERS route was established. |

<a id="accepted-material"></a>

## What belongs here

- worked walkthroughs with assumptions, expected outcome, operational home, non-goals, and correction triggers;
- minimal synthetic or safely transformed payload sketches with visible example markers;
- positive and negative paths with finite outcomes and reason codes;
- validator-backed examples that name their contract, schema, exact command, polarity, and limits;
- bounded code or configuration demonstrations with an entrypoint, dependencies, setup/reset, expected output, and failure behavior before being called runnable;
- UI, map, story, Focus, evidence, receipt, source-intake, and domain examples that point to their owning authorities and preserve trust-visible states;
- local READMEs defining scope, exclusions, validation, maintenance, and retirement.

<a id="exclusions"></a>

## What does NOT belong here

| Material | Correct home or action |
|---|---|
| RAW, WORK, QUARANTINE, processed, catalog, triplet, or published data | Corresponding `data/` lifecycle phase |
| EvidenceBundles, ProofPacks, validation records | `data/proofs/` |
| Run, ingest, transform, validation, AI, correction, rollback, or render receipts | `data/receipts/` |
| Release manifests, promotion decisions, corrections, withdrawals, rollback cards, signatures | `release/` |
| Source descriptors or activation decisions | Accepted registry/control-plane home |
| Contracts, schemas, policy, validators, fixtures, tests, apps, packages, pipelines, connectors, workflows | Their canonical responsibility roots |
| Secrets, private data, unclear-rights material, or harmful precision | Remove, synthesize, generalize, quarantine, delay, or deny |
| Generated prose presented as evidence | Never; generated language may interpret resolved evidence only |

## Inputs

Use accepted doctrine and ADRs, current contracts/schemas/policy, pinned implementation evidence, repository-owned validators, and synthetic rights-safe values. Mark consequential data as synthetic, transformed, source-backed but bounded, or unresolved. A source URL alone is not source admission, an immutable snapshot, or an `EvidenceBundle`.

## Outputs

Permitted outputs are static walkthroughs, synthetic payloads, bounded code/config demonstrations, expected-output fragments, and review aids. Every output remains non-authoritative and may be corrected, retired, or separately graduated. No example becomes a fixture, test, proof, receipt, release object, public API payload, or published artifact by copying or merging it.

## Validation

Validation must match the claimed maturity.

| Scope | Required evidence |
|---|---|
| README-only | Markdown structure, local links/anchors, no unsupported behavior claims |
| Static walkthrough | README checks plus snippet parse where practical, synthetic/safety review, explicit expected outcome |
| Validator-backed | Contract/schema validator, positive and negative polarity, deterministic/no-network posture, exact command |
| Runnable demo | Pinned dependencies, entrypoint, setup/reset, deterministic inputs, expected output, failure behavior, smoke test |

Repository-grounded commands currently include:

```bash
python tools/validators/governance/validate_briefing_signal.py \
  examples/briefing_integration/*.json

python tools/validators/governance/route_briefing_signals.py \
  examples/briefing_integration/*.json
```

For a changed-Markdown PR, the repository workflow runs its no-network link-check tests and validates local targets in changed Markdown. The equivalent checker shape is:

```bash
python tools/validators/docs/link-check/check_links.py \
  --repo-root . \
  --git-diff "<base>...HEAD" \
  --format text
```

A green result proves only the checked boundary. The current `Makefile` does not define `validate-examples`, `baseline-check`, or `public-path-check`; do not cite those stale command names.

## Review burden

Examples/docs review is always required. Add domain, evidence, policy/sensitivity, security/privacy, accessibility, runtime, or release reviewers when the example touches those boundaries. CODEOWNERS routing is not stewardship, approval evidence, policy permission, or release authority.

## Related folders

- [`fixtures/`](../fixtures/README.md) — deterministic validator/test inputs
- [`tests/`](../tests/README.md) — executable acceptance and regression checks
- [`contracts/`](../contracts/README.md) and [`schemas/`](../schemas/README.md) — meaning and machine shape
- [`policy/`](../policy/README.md) — admissibility and obligations
- [`data/proofs/`](../data/proofs/README.md), [`data/receipts/`](../data/receipts/README.md), and [`data/published/`](../data/published/README.md) — operational artifact families
- [`release/`](../release/README.md) — governed release, correction, withdrawal, and rollback
- [`tools/`](../tools/README.md) — validators and operational tooling

## ADRs

Directory Rules v2.0.0 is adopted through [ADR-0029](../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md). Structural moves, new authority roots, object-family changes, lifecycle changes, public-path changes, or trust-boundary changes must follow the applicable amendment class. An ADR proposed inside an example cannot authorize its own dependent change.

## Last reviewed

- **Date:** 2026-08-08
- **Pinned base:** `main@0ab94b49111fad3801f3ab3da4afb6433cc14d23`
- **Prior target blob:** `d3fbce80c82106935288d59a708bbb1a0118591e`
- **Examples tree:** `750a5c39b08ab6c4b4b39851bfee498e3a5ea137`
- **Method:** complete target review; recursive examples-tree inventory; relevant child, governance, workflow, Makefile, and open-PR reads
- **Not performed:** local checkout, dependency installation, example execution, browser render, deployment, or runtime observation
- **Human review:** pending

## Current bounded inventory

| Lane | Bounded contents | Maturity | Boundary |
|---|---|---|---|
| [`briefing_integration/`](briefing_integration/README.md) | README + two JSON records | `VALIDATOR_BACKED_EXAMPLE` | Local discovery/routing only; no issue mutation, source activation, release, or public use |
| [`evidence_bundles/`](evidence_bundles/README.md) | README | `README_ONLY` | Proof authority remains under `data/proofs/` |
| [`focus_flows/`](focus_flows/README.md) | README + [`hydrology_huc12_question.md`](focus_flows/hydrology_huc12_question.md) | `STATIC_WALKTHROUGH` | Governed API/evidence/AI runtime remains authoritative |
| [`habitat/`](habitat/README.md) | README + `.gitkeep` | `README_ONLY` | Domain, policy, lifecycle, and release remain elsewhere |
| [`ingest_receipts/`](ingest_receipts/README.md) | README | `README_ONLY` | Emitted receipts remain under `data/receipts/` |
| [`settlements-infrastructure/`](settlements-infrastructure/README.md) | README + `.gitkeep` | `README_ONLY` | Naming conflict and sensitive infrastructure remain unresolved outside examples |
| [`source_intake/`](source_intake/README.md) | README + [`usgs_nwis_walkthrough.md`](source_intake/usgs_nwis_walkthrough.md) | `STATIC_WALKTHROUGH` | No source admission, connector execution, RAW capture, or receipt emission |
| [`story_decks/`](story_decks/README.md) | README + [`kansas_drought_2012.md`](story_decks/kansas_drought_2012.md) | `STATIC_WALKTHROUGH` | Story runtime, payload, evidence, and release remain elsewhere |
| [`viewer_styles/`](viewer_styles/README.md) | README | `README_ONLY` | Styling is not evidence, policy, sensitivity transformation, or release |

The briefing records are [`gmd_action_plan_inventory_2026_07_29.json`](briefing_integration/gmd_action_plan_inventory_2026_07_29.json) and [`hays_water_local_consult_2026_07_29.json`](briefing_integration/hays_water_local_consult_2026_07_29.json). Both declare `DUPLICATE`, propose issue `#1647` as the existing bounded work target, set repository mutation and public use false, and deny source activation, proof construction, release, deployment, and publication. Fixture-backed routing is not live GitHub-state verification or mutation authority.

## Example maturity model

`PROPOSED` root vocabulary:

```text
README_ONLY
  -> STATIC_WALKTHROUGH
  -> VALIDATOR_BACKED_EXAMPLE
  -> RUNNABLE_DEMO
  -> FIXTURE_OR_TEST_AUTHORITY (outside examples/)
```

Advance only when the next state is verified. Move backward when contracts, sources, policy, dependencies, runtime, or release behavior invalidate an example.

<a id="example-contract"></a>

## Example contract

A consequential example should declare:

```yaml
example: true
authority: non_authoritative_example
do_not_publish: true
maturity: README_ONLY | STATIC_WALKTHROUGH | VALIDATOR_BACKED_EXAMPLE | RUNNABLE_DEMO
real_vs_synthetic: explicit
expected_outcome: ANSWER | ABSTAIN | DENY | ERROR | HOLD | QUARANTINE | NOT_APPLICABLE
operational_home: "<verified owning root or NEEDS VERIFICATION>"
validation_boundary: "<exact checks performed>"
correction_trigger: "<contract, policy, source, runtime, or release change>"
```

Do not invent metadata merely to satisfy this shape. State `NEEDS VERIFICATION` where the fact is unresolved.

<a id="lifecycle-and-trust-membrane-relationship"></a>

## Lifecycle and trust-membrane relationship

```text
SOURCE / PRE-RAW -> RAW -> WORK / QUARANTINE -> PROCESSED
-> CATALOG / TRIPLET -> PUBLISHED -> governed public surfaces
```

`examples/` sits beside this lifecycle as a teaching surface. It cannot activate sources, write lifecycle state, emit authoritative receipts/proofs, approve policy, promote, release, publish, correct downstream consumers, or execute rollback. Copy the concept, never the authority.

<a id="operational-home-crosswalk"></a>

## Sensitive data and safety posture

Use the least revealing representation that teaches the boundary. Remove credentials and private endpoints. Prefer synthetic values for living persons, genomics, parcels, wells, infrastructure, rare species, archaeology, and cultural or sacred sites. Generalize, redact, aggregate, delay, quarantine, or deny where rights, sensitivity, sovereignty, or harmful precision is unclear. Client-side hiding is not a public-safe transform.

## Maintenance, correction, and rollback

Re-review when a referenced contract, schema, policy, source role, identifier, validator, command, dependency, workflow, runtime, rights posture, filename, anchor, or ADR changes.

1. Mark misleading material stale, held, denied, or conflicted.
2. Pin the affected revision and changed authority.
3. Correct the smallest dependency-closed set and direct links.
4. Preserve prior state in Git and record supersession when meaning changes.
5. Re-run lane checks and the changed-Markdown link checker.

Before merge, rollback means closing or abandoning the draft PR/branch without force-push. After merge, revert the exact commit or submit a forward fix. Public reliance may additionally require governed correction or withdrawal outside this README.

## Open verification register

- `NEEDS VERIFICATION`: accountable owner/CODEOWNERS route; root-wide validator; host rendering; accessibility execution; external-currentness and licensing policy; stale-example service level; correction propagation; retirement drill; naming resolution for `focus_flows` and `settlements-infrastructure`; admitted source snapshots for briefing claims.
- `UNKNOWN`: executable entrypoints for non-briefing lanes; runtime parity; deployed consumers; public effects.

<a id="evidence-ledger"></a>
<a id="v020-to-v030-no-loss-ledger"></a>
<a id="v030-to-v040-no-loss-ledger"></a>

## Preservation and change record

v0.4.0 preserves the path, `doc_id`, purpose, non-authority boundary, ROOT_FULL headings, belongs/exclusions, lifecycle, sensitivity, correction, rollback, and compatibility anchors. It updates Directory Rules v1.4 references to adopted v2.0.0, expands the inventory from eight to nine lanes, records five substantive artifacts rather than three walkthroughs, recognizes the briefing validator lane, replaces stale Make targets with current repository-owned commands, and narrows blanket validation claims to their verified scopes. No operational payload, code, fixture, test, workflow, receipt, proof, release object, public route, or publication state changed.

## Status summary

- `CONFIRMED`: same-path placement, adopted directory governance, bounded inventory, briefing validation path, changed-Markdown local link checking, and docs/accessibility holds.
- `PROPOSED`: maturity vocabulary and root admission checklist.
- `UNKNOWN`: non-briefing runtime parity, deployed consumers, and public effects.
- `NEEDS VERIFICATION`: ownership, root-wide validation, rendering, accessibility, currentness, licensing, correction propagation, and retirement drills.
- `DENY`: treating example placement, validation, commit, PR, merge, screenshot, or prose as evidence, policy, release, deployment, publication, or public authority.

<p align="right"><a href="#top">Back to top</a></p>

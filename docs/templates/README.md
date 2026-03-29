<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS_VERIFICATION_UUID
title: templates
type: standard
version: v1
status: draft
owners: @bartytime4life (broad default CODEOWNERS ownership reported; docs/templates-specific mapping NEEDS VERIFICATION)
created: NEEDS_VERIFICATION
updated: 2026-03-29
policy_label: NEEDS_VERIFICATION
related: [../../README.md, ../standards/, ../governance/, ../reports/story_nodes/]
tags: [kfm, docs, templates, governance]
notes: [Source-bounded revision from the supplied baseline. Live docs/templates inventory, adjacent README conventions, and directory-specific CODEOWNERS mapping were not re-verified in this revision and should be checked against the active repository before merge.]
[/KFM_META_BLOCK_V2] -->

# templates

Governed template hub for reusable KFM documentation scaffolds, promotion-ready doc shells, and review-friendly Markdown patterns.

> **Status:** experimental  
> **Owners:** `@bartytime4life` *(broad default ownership is source-reported; recheck `../../.github/CODEOWNERS` for any directory-specific mapping before commit)*  
> ![status](https://img.shields.io/badge/status-experimental-orange) ![surface](https://img.shields.io/badge/surface-docs%2Ftemplates-2f81f7) ![scope](https://img.shields.io/badge/scope-governed%20doc%20templates-8250df) ![truth](https://img.shields.io/badge/truth-source--bounded-0a7d5a) ![owners](https://img.shields.io/badge/owners-%40bartytime4life-lightgrey)  
> **Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Evidence boundary](#current-evidence-boundary) · [Directory tree](#current-and-source-reported-footprint) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Template registry](#template-registry) · [Contribution gates](#contribution-gates) · [Task list](#task-list--definition-of-done) · [FAQ](#faq) · [Appendix](#appendix)

> [!NOTE]
> This README is intentionally conservative. It preserves the supplied doctrinal baseline, but live directory inventory, adjacent path presence, and CODEOWNERS mapping were not re-verified in this revision. Those details remain visibly marked `INFERRED` or `NEEDS VERIFICATION`.

> [!IMPORTANT]
> `docs/templates/` is for reusable **documentation scaffolds**. It is not a second truth path.
>
> Templates can standardize metadata, review sections, promotion reminders, and Markdown structure, but instantiated contracts, policy bodies, Story Nodes, reports, datasets, and runtime artifacts still belong in their owning surfaces.

## Scope

`docs/templates/` is the reusable scaffold shelf for KFM’s documentation layer.

Its job is to make repeatable documentation shapes easy to reuse without letting Markdown drift into unofficial system truth. In practice, that means the files here should help maintainers author README-like docs, governed standards notes, Story Node starting points, and API-change writeups that preserve KFM’s evidence-first posture.

Use this directory for:

- reusable Markdown templates that apply across more than one doc or directory
- shared metadata, status, evidence-boundary, or review scaffolds
- promotion-aware document shells that clarify required sections and link strategy
- lightweight authoring aids that reduce drift across docs without replacing local meaning

Do not use this directory for:

- filled-in canonical docs that belong in an owning directory
- policy logic, schema truth, or executable contract definitions
- generated evidence objects, receipts, manifests, or release artifacts
- runtime code, UI code, model outputs, data files, or secrets
- one-off drafts that are not truly reusable templates

[Back to top](#templates)

## Repo fit

**Surface path:** `docs/templates/`  
**This file:** `docs/templates/README.md`

**Role in repo:** directory README for the governed documentation template surface.

### Upstream and downstream anchors

| Direction | Surface | Why it matters | Status |
|---|---|---|---|
| Current | `docs/templates/` | reusable scaffold surface for documentation patterns | **CONFIRMED** target surface in supplied baseline |
| Current | [`README.md`](README.md) | directory contract and contributor entrypoint for this surface | **CONFIRMED** target file in supplied baseline |
| Upstream | [`../../README.md`](../../README.md) | likely root operating posture and trust framing | **INFERRED** / **NEEDS VERIFICATION** |
| Adjacent | [`../standards/`](../standards/) | likely consumer surface for governed standards docs | **INFERRED** / **NEEDS VERIFICATION** |
| Adjacent | [`../governance/`](../governance/) | likely consumer surface for ethics, review, and sovereignty docs | **INFERRED** / **NEEDS VERIFICATION** |
| Adjacent | [`../reports/story_nodes/`](../reports/story_nodes/) | likely home for Story Node instances that consume templates | **INFERRED** / **NEEDS VERIFICATION** |
| Downstream | `docs/templates/TEMPLATE__*.md` | reusable authoring entrypoints for other documentation surfaces | **INFERRED** / **NEEDS VERIFICATION** |

This directory matters because the supplied baseline presents KFM documentation as a governed control surface, not a loose collection of prose. Templates help docs stay reviewable, provenance-conscious, and structurally consistent without turning Markdown into an unofficial implementation layer.

## Accepted inputs

Content that belongs in `docs/templates/` includes:

| Template class | What belongs here | Notes |
|---|---|---|
| Directory README scaffolds | reusable index patterns for repo directories | keep scope, exclusions, and evidence posture explicit |
| Governed document shells | repeatable structures for standards, guidance notes, or operational docs | favor reusable sections over decorative snippets |
| Promotion-oriented templates | Story Node, API extension, and other doc classes with predictable review sections | only the template lives here; filled-in artifacts belong elsewhere |
| Authoring aids | placeholder comments, review checklists, metadata scaffolds | keep these lightweight and Markdown-native |
| Example fragments | small, clearly labeled examples that teach shape or section rhythm | examples should clarify structure, not become hidden truth |

## Exclusions

The following do **not** belong here as canonical truth:

| Does **not** belong here | Keep it here instead |
|---|---|
| filled-in governance, standards, runbooks, reports, or architecture docs | owning `docs/` subdirectory |
| OpenAPI, JSON Schema, vocabularies, or machine-enforced envelopes | `../../contracts/` and `../../schemas/` |
| policy bundles, deny-by-default logic, executable review rules | `../../policy/` |
| Story Node instances, published narratives, evidence drawers, or report deliverables | owning narrative/report surface |
| raw, work, processed, or cataloged datasets and receipts | governed data lifecycle surfaces |
| runtime code, workers, UI components, or service logic | owning code surface |
| secrets, credentials, signed URLs, or sensitive coordinates | never in docs |

## Evidence labels used here

| Label | Meaning in this README |
|---|---|
| **CONFIRMED** | directly supported by the supplied baseline or explicit target surface for this file |
| **INFERRED** | a reasonable conclusion from supplied baseline language, but not re-enumerated from a live repo tree in this revision |
| **PROPOSED** | a repo-native improvement or authoring rule added on purpose |
| **UNKNOWN** | not established strongly enough to present as current fact |
| **NEEDS VERIFICATION** | placeholder value or detail that should be rechecked against the active repository before merge |

## Current evidence boundary

> [!NOTE]
> The supplied `docs/templates/README.md` draft functions as the redesign baseline for this revision. Where that baseline named paths, files, or ownership without live re-verification, this README keeps uncertainty visible instead of smoothing it away.

| Observation | Status | Why it changes this README |
|---|---|---|
| The supplied baseline treats `docs/templates/` as a governed documentation surface rather than a scratch folder | **CONFIRMED** | this README should define the directory as an operational authoring surface, not a dumping ground |
| The supplied baseline names three specific template files under `docs/templates/` | **INFERRED** / **NEEDS VERIFICATION** | those filenames can remain in the registry and tree, but should stay visibly qualified until rechecked |
| Broad default ownership is reported as `@bartytime4life` | **INFERRED** / **NEEDS VERIFICATION** | owners can be shown, but directory-specific CODEOWNERS mapping should remain qualified |
| Adjacent surfaces `../standards/`, `../governance/`, and `../reports/story_nodes/` are presented as related consumers or peers | **INFERRED** / **NEEDS VERIFICATION** | cross-links can be preserved, but not upgraded into stronger implementation claims |
| Live tree inventory, adjacent README conventions, and `.github/CODEOWNERS` were not re-verified in this revision | **CONFIRMED** revision boundary | this README must not imply stronger repository inspection than actually occurred |

## Current and source-reported footprint

### Target surface

```text
docs/
└── templates/                                    # CONFIRMED target surface
```

### Source-reported template inventory

```text
docs/templates/
├── README.md                                     # CONFIRMED target file
├── TEMPLATE__KFM_UNIVERSAL_DOC.md                # INFERRED / NEEDS VERIFICATION
├── TEMPLATE__STORY_NODE_V3.md                    # INFERRED / NEEDS VERIFICATION
└── TEMPLATE__API_CONTRACT_EXTENSION.md           # INFERRED / NEEDS VERIFICATION
```

That split is intentional. This README distinguishes between the **confirmed target surface** and the **source-reported local inventory** so that maintainers can verify live repo state before merge.

[Back to top](#templates)

## Quickstart

Use a verify-first sequence before adding or revising templates.

> [!WARNING]
> The commands below are repo-local inspection examples. They are the right pre-merge checks in a live checkout, but they are not retroactive proof of current inventory unless actually run against the active repository.

```bash
# Inspect the current surface
ls -la docs/templates
find docs/templates -maxdepth 1 -type f | sort
sed -n '1,240p' docs/templates/README.md

# Re-check owners and adjacent governed docs surfaces
sed -n '1,200p' .github/CODEOWNERS 2>/dev/null
find docs/standards docs/governance docs/reports -maxdepth 2 -type f 2>/dev/null | sort

# Search for template references across docs and workflows
grep -RIn "TEMPLATE__KFM_UNIVERSAL_DOC\|TEMPLATE__STORY_NODE_V3\|TEMPLATE__API_CONTRACT_EXTENSION" docs .github 2>/dev/null

# Re-check broader repo framing before changing template contracts
sed -n '1,220p' README.md 2>/dev/null
```

## Usage

### When to use this directory

Reach for `docs/templates/` when the documentation need is **reusable**, not merely important. If more than one doc class needs the same governed skeleton, review hints, evidence-boundary language, or promotion reminders, a template belongs here.

### When **not** to use this directory

Do **not** add a template just because a document matters. If the artifact is the actual policy, actual contract, actual Story Node, or actual runbook, it belongs in its owning surface.

### Suggested authoring flow

1. Start in the owning docs surface and confirm the artifact type: directory README, governed standard, runbook, Story Node, or API extension note.
2. Check whether a reusable template already exists here.
3. If one exists, instantiate it in the owning surface and keep directory-local meaning there.
4. If none exists, add a new template here only when the shape is clearly reusable across multiple docs.
5. Keep behavior-significant doc changes in the same change stream as the contracts, policy, code, or runbooks they explain.

### Selection rule

Use the smallest template that preserves truth posture. A template succeeds when it reduces drift and review friction without hiding uncertainty or inventing implementation state.

> [!TIP]
> A KFM template should standardize **shape**, **reviewability**, and **truth posture**. It should not silently smuggle in system claims the template itself cannot prove.

## Diagram

```mermaid
flowchart TD
    A[Documentation need] --> B{Reusable across multiple docs?}
    B -- No --> C[Write in owning surface]
    B -- Yes --> D[Create or revise template in docs/templates/]
    D --> E[Carry metadata, scope, exclusions, and evidence posture]
    E --> F[Instantiate in the owning docs surface]
    F --> G[Link to standards, governance, contracts, or Story Nodes as needed]
    G --> H[Review, promote, or revise]
```

Templates are an authoring control surface, not a substitute for evidence, policy, or runtime enforcement.

## Template registry

| Template or pattern | Current status | Intended use | Where the instantiated artifact belongs |
|---|---|---|---|
| Directory README pattern | **PROPOSED** / modeled by this file | directory indexes with scope, repo fit, accepted inputs, exclusions, quickstart, diagram, and review checks | owning directory |
| `TEMPLATE__KFM_UNIVERSAL_DOC.md` | **INFERRED** / **NEEDS VERIFICATION** | general governed KFM docs that need a repeatable structure | owning `docs/` surface |
| `TEMPLATE__STORY_NODE_V3.md` | **INFERRED** / **NEEDS VERIFICATION** | provenance-linked Story Node or narrative promotion docs | `docs/reports/story_nodes/` or equivalent owning narrative surface |
| `TEMPLATE__API_CONTRACT_EXTENSION.md` | **INFERRED** / **NEEDS VERIFICATION** | doc-side extension notes for API or contract changes | contract- or standards-adjacent doc surface |
| Additional lightweight template classes | **PROPOSED** | only when a doc shape appears often enough to justify maintenance | owning surface after review |

### What a KFM-friendly template should standardize

| Concern | Minimum expectation |
|---|---|
| Purpose | one-line statement of what the instantiated doc is for |
| Status + owners | visible near the top |
| Scope | what belongs and what does not |
| Evidence boundary | what is confirmed, inferred, proposed, or still unknown |
| Relative links | repo-native paths by default |
| Reviewability | explicit task list, definition of done, or verification backlog |
| Truth posture | never imply live implementation that has not been verified |
| Promotion path | where the filled-in artifact belongs once it stops being a scaffold |

## Contribution gates

A new template should clear all of the following before merge.

| Gate | Pass condition |
|---|---|
| Reuse threshold | the pattern is expected to serve more than one doc or directory |
| Owning surface clarity | the completed artifact’s destination is explicitly named |
| Truth boundary | the template does not embed unverified implementation claims |
| Metadata fit | top matter aligns with repo norms or remains clearly placeholdered |
| Link hygiene | relative links resolve cleanly from `docs/templates/` |
| Reviewability | the template makes status, owners, scope, and verification work visible |
| Lifecycle clarity | the template makes promotion or handoff expectations explicit |

## Task list / definition of done

- [ ] The live `docs/templates/` tree was rechecked before merge.
- [ ] `.github/CODEOWNERS` was reopened and the owners line still matches this README.
- [ ] Any template filenames named in this README either exist now or remain clearly marked `INFERRED` / `NEEDS VERIFICATION`.
- [ ] New templates added here are genuinely reusable across more than one doc surface.
- [ ] No instantiated doc truth, policy body, schema, or release artifact was moved here for convenience.
- [ ] Relative links render correctly from `docs/templates/README.md`.
- [ ] Mermaid diagrams render cleanly in GitHub.
- [ ] Unknowns remain visible instead of being rewritten as certainty.

[Back to top](#templates)

## FAQ

### Does this README claim those named template files already exist in the live checkout?

No. It treats `docs/templates/` and `docs/templates/README.md` as the confirmed target surface for this revision, but keeps the three named template files visibly marked `INFERRED` / `NEEDS VERIFICATION` until the live tree is rechecked.

### Should a finished Story Node or API contract live here?

No. Only the reusable scaffold belongs here. The instantiated artifact belongs in its owning surface.

### When is a new template justified?

When the same governed doc shape will be reused across multiple files or directories, and the template reduces drift, review ambiguity, or missing-section risk.

### Is this directory allowed to set policy?

No. It can scaffold policy-facing docs, but canonical policy logic still belongs in governed policy and contract surfaces.

## Appendix

<details>
<summary>PROPOSED starter checklist for future template files</summary>

Use this as a lightweight check when adding a new reusable template:

- include a clear title and one-line purpose
- make status, owners, and intended audience visible
- state accepted inputs and exclusions
- add evidence-boundary guidance or truth-posture reminders
- keep relative links repo-native
- include a review checklist or definition of done
- point promoted artifacts to their owning surface
- avoid embedding repo-specific implementation claims the template cannot prove
- prefer calm placeholders such as `NEEDS VERIFICATION` over invented specificity

</details>

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS_VERIFICATION
title: correction
type: standard
version: v1
status: draft
owners: @bartytime4life
created: YYYY-MM-DD
updated: YYYY-MM-DD
policy_label: public
related: [tests/README.md, tests/e2e/README.md, .github/workflows/README.md, contracts/README.md, policy/README.md, schemas/README.md, docs/README.md]
tags: [kfm, tests, e2e, correction, verification]
notes: [doc_id and dates need verification; status is preserved from the supplied baseline until document-record metadata is reverified; owner is grounded in current public-main CODEOWNERS coverage for /tests/]
[/KFM_META_BLOCK_V2] -->

# correction

End-to-end correction proof surface for KFM correction lineage, visible supersession, stale-visible behavior, and replacement-safe trust cues.

> **Status:** experimental  
> **Owners:** `@bartytime4life`  
> **Path:** `tests/e2e/correction/README.md`  
> **Repo fit:** leaf family under [`../README.md`](../README.md); downstream of [`../../README.md`](../../README.md), [`../../../contracts/README.md`](../../../contracts/README.md), [`../../../policy/README.md`](../../../policy/README.md), [`../../../schemas/README.md`](../../../schemas/README.md), [`../../../docs/README.md`](../../../docs/README.md), and [`../../../.github/workflows/README.md`](../../../.github/workflows/README.md); upstream of future executable correction drills and lineage-proof cases under `tests/e2e/correction/**`  
> **Quick jump:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Current verified snapshot](#current-verified-snapshot) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Tables](#tables) · [Task list / definition of done](#task-list--definition-of-done) · [FAQ](#faq) · [Appendix](#appendix)  
> ![status](https://img.shields.io/badge/status-experimental-orange) ![owners](https://img.shields.io/badge/owners-%40bartytime4life-1f6feb) ![family](https://img.shields.io/badge/family-correction%20proof-bd561d) ![branch](https://img.shields.io/badge/branch-main-0a7d5a) ![inventory](https://img.shields.io/badge/current%20public%20inventory-README--only-lightgrey) ![truth](https://img.shields.io/badge/truth-CONFIRMED%20%7C%20INFERRED%20%7C%20PROPOSED-6f42c1)
>
> [!NOTE]
> The meta block above keeps `doc_id`, `created`, and `updated` as reviewable placeholders until document-record metadata is reverified from repo history or governance records. The impact block below describes the current maturity of the `correction/` leaf itself.
>
> [!IMPORTANT]
> Current public `main` inspection confirms that `tests/e2e/correction/` exists and currently exposes `README.md` only. That proves the leaf boundary and its documented burden, but it does **not** prove checked-in executable correction cases, runner/toolchain, proof-pack emitters, screenshot baselines, or automatically exercised correction drills.

| At a glance | Working rule |
|---|---|
| Leaf burden | Prove correction lineage end to end |
| Must stay visible | `superseded`, `withdrawn`, `stale-visible`, `correction-pending`, or equivalent trust cue |
| Must never happen | Silent overwrite of release-backed trust surfaces |
| Minimum lineage anchors | `CorrectionNotice` + affected release ref + replacement ref or explicit absence |
| Best first executable case | One synthetic, public-safe correction drill |

## Scope

`tests/e2e/correction/` exists to prove that KFM can correct a release-backed or outward trust-bearing result **without hiding the change**.

Good correction cases are **thin but whole**: one mistaken or withdrawn outward artifact, one governed correction path, and one visible lineage trail across the affected surfaces. This leaf is for correction-specific end-to-end proof such as supersession, withdrawal, replacement, stale-visible behavior, correction-pending cues, or precision narrowing that must remain inspectable in maps, dossiers, stories, Focus, exports, or adjacent trust surfaces when those surfaces are in scope.

This is not a generic regression bucket. If a case is really about release assembly, pure runtime outcome proof, policy grammar, schema shape, accessibility-only behavior, or deterministic replay, it should live in its more honest home.

### Status markers used here

| Marker | Meaning in this README |
|---|---|
| **CONFIRMED** | Visible on the current public branch or directly grounded in stable adjacent repo documentation |
| **INFERRED** | Strongly supported by repo doctrine and neighboring docs, but not re-proven from executable branch evidence in this revision |
| **PROPOSED** | Buildable guidance that fits KFM doctrine without claiming current implementation |
| **UNKNOWN** | Not verified strongly enough to describe as current repo reality |
| **NEEDS VERIFICATION** | A path, command, workflow, or implementation detail that should be checked against the checked-out branch before merge |

### Evidence boundary used here

| Evidence layer | What this README treats as settled |
|---|---|
| **CONFIRMED — current public repo** | `tests/e2e/correction/` exists; the current public tree shows `README.md` only in this leaf; no checked-in executable correction cases are visible from the public tree alone |
| **CONFIRMED — parent e2e family contract** | [`../README.md`](../README.md) defines `correction/` as the leaf for correction, supersession, replacement, and stale-visible proof |
| **CONFIRMED — tests family contract** | [`../../README.md`](../../README.md) treats verification as a governed trust surface, not a generic QA bucket |
| **CONFIRMED — workflow adjacency** | [`../../../.github/workflows/README.md`](../../../.github/workflows/README.md) exists, and current public `main` shows `.github/workflows/` as `README.md` only |
| **CONFIRMED — ownership** | [`../../../.github/CODEOWNERS`](../../../.github/CODEOWNERS) currently assigns `/tests/` to `@bartytime4life` |
| **NEEDS VERIFICATION** | Real runner/toolchain, checked-in executable cases, required checks, screenshot baselines, proof-pack emitters, and whether correction drills are exercised automatically |

[Back to top](#correction)

## Repo fit

**Path:** `tests/e2e/correction/README.md`  
**Role:** leaf README for correction-specific whole-path proof under `tests/e2e/`.

### Upstream anchors

| Relation | Path | Why it matters | Status |
|---|---|---|---|
| Parent family map | [`../README.md`](../README.md) | Defines `e2e/` as the whole-path proof family and assigns this leaf its burden | **CONFIRMED** |
| Wider tests lattice | [`../../README.md`](../../README.md) | Keeps this leaf aligned with the repo’s governed verification model | **CONFIRMED** |
| Repo root posture | [`../../../README.md`](../../../README.md) | Keeps correction proof tied to the governed, evidence-first repo identity | **CONFIRMED** |
| Workflow adjacency | [`../../../.github/workflows/README.md`](../../../.github/workflows/README.md) | Shows the current public automation boundary and its limits | **CONFIRMED** |
| Ownership boundary | [`../../../.github/CODEOWNERS`](../../../.github/CODEOWNERS) | Establishes review ownership for `/tests/` | **CONFIRMED** |
| Contract source | [`../../../contracts/README.md`](../../../contracts/README.md) | Correction cases should consume authoritative object families, not redefine them | **CONFIRMED** |
| Policy source | [`../../../policy/README.md`](../../../policy/README.md) | Correction can involve deny-by-default decisions, rights narrowing, or review-bearing outcomes | **CONFIRMED** |
| Schema boundary | [`../../../schemas/README.md`](../../../schemas/README.md) | Prevents schema-law drift while contract home remains a live repo concern | **CONFIRMED** |
| Runbooks and human-readable guidance | [`../../../docs/README.md`](../../../docs/README.md) | Correction procedures and operator guidance should stay synchronized with executable proof | **CONFIRMED** |
| Release-bearing sibling | [`../release_assembly/README.md`](../release_assembly/README.md) | Use that leaf when the core burden is release/proof-pack assembly rather than correction lineage | **CONFIRMED** as sibling path / **NEEDS VERIFICATION** as executable depth |
| Runtime-bearing sibling | [`../runtime_proof/README.md`](../runtime_proof/README.md) | Use that leaf when the core burden is runtime outcome proof rather than correction propagation | **CONFIRMED** as sibling path / **NEEDS VERIFICATION** as executable depth |

### Local rule

Keep this leaf **correction-led**.  
If a case cannot point to a correction-specific end-to-end burden, it probably belongs somewhere else.

## Accepted inputs

Accepted inputs for this directory are the **smallest artifacts needed to prove correction honestly**.

| Accepted input | What belongs here | Notes |
|---|---|---|
| Whole-path correction scenarios | One narrow but complete scenario that crosses real correction boundaries | Prefer one accountable drill over a wide decorative suite |
| Affected and replacement release refs | The old scope, the replacement scope, or an explicit absence of replacement | Avoid correction prose with no release lineage |
| `CorrectionNotice`-bearing examples | Emitted or asserted correction objects tied to the scenario | The schema or contract authority stays upstream |
| Surface-state evidence | Screenshots, snapshots, diffs, or other cues showing the outward correction state | **PROPOSED / NEEDS VERIFICATION** until the real runner is known |
| Derived rebuild or stale-visible evidence | Proof that projections rebuild, repoint, or remain visibly stale instead of silently drifting | Especially important for map-facing or export-facing cases |
| Audit and comparison output | Reports that show what changed, why, and how the system stayed trustworthy | Keep output reviewable and burden-led |
| Reused authoritative fixtures | Contract, policy, and release examples imported from their owning homes | Reuse; do not fork authority locally |
| Public-safe correction drills | Synthetic or non-sensitive cases that can be exercised without rights leakage | Strong first executable candidate |

## Exclusions

What does **not** belong here, and where it should go instead:

| Exclusion | Keep it out of `tests/e2e/correction/` | Put it here instead |
|---|---|---|
| Release assembly with no correction burden | That is broader release proof, not correction proof | [`../release_assembly/README.md`](../release_assembly/README.md) |
| Runtime `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` proof with no correction propagation | That is runtime proof first | [`../runtime_proof/README.md`](../runtime_proof/README.md) |
| Schema-shape-only validation for `CorrectionNotice` or related objects | This leaf proves behavior, not contract shape alone | [`../../contracts/README.md`](../../contracts/README.md) and [`../../../contracts/README.md`](../../../contracts/README.md) |
| Policy grammar or reason/obligation logic by itself | Decision grammar should stay isolated when possible | [`../../policy/README.md`](../../policy/README.md) and [`../../../policy/README.md`](../../../policy/README.md) |
| Accessibility-only correction cues | If the burden is readability/keyboard/motion only, keep it first-class | [`../../accessibility/README.md`](../../accessibility/README.md) |
| Deterministic replay without correction lineage | Repeatability is important, but not this leaf’s core job | [`../../reproducibility/README.md`](../../reproducibility/README.md) |
| Human-readable correction playbooks | Documentation is not executable proof | [`../../../docs/README.md`](../../../docs/README.md) |
| Canonical contracts, policy bundles, or emitted release artifacts as authority | This leaf should consume authority, not replace it | their owning contract, policy, release, or docs surfaces |

## Current verified snapshot

The current public `main` branch proves the following:

- `tests/e2e/` exists and currently contains `correction/`, `release_assembly/`, `runtime_proof/`, and `README.md`.
- The parent [`../README.md`](../README.md) already assigns this leaf the burden of correction, supersession, replacement, and stale-visible proof.
- `tests/e2e/correction/` currently contains `README.md` only.
- The checked-in leaf currently publishes boundary, placement, and inspection guidance, but the public tree does not prove executable correction cases under this leaf.
- Public `.github/workflows/` currently exposes `README.md` only; checked-in workflow YAML is not proven from visible repo files alone.
- `/tests/` currently resolves to `@bartytime4life` in repo ownership.

> [!CAUTION]
> Directory presence is **not** executable coverage. This leaf should stay explicit about what is currently visible, what is still merely doctrinal, and what still needs a checked-out branch to confirm.

[Back to top](#correction)

## Directory tree

### Current confirmed snapshot

```text
tests/
└── e2e/
    └── correction/
        └── README.md
```

### Proposed maturity shape — NEEDS VERIFICATION

```text
tests/
└── e2e/
    └── correction/
        ├── README.md
        ├── supersession/
        ├── withdrawal/
        ├── replacement_lineage/
        ├── stale_visible/
        ├── correction_pending/
        └── shared/
            ├── fixtures/
            └── cues/
```

> [!TIP]
> Keep this leaf **case-led**. Add real subtrees only when a real correction burden exists to justify them.

## Quickstart

### Safe inspection commands

These commands are safe because they inspect the current branch shape and adjacent documentation without assuming Playwright, Cypress, pytest, Vitest, Jest, or any other unverified runner.

```bash
# inspect the current local correction leaf
find tests/e2e/correction -maxdepth 4 -type d 2>/dev/null | sort
find tests/e2e/correction -maxdepth 4 -type f 2>/dev/null | sort

# re-read the parent family map and sibling leaves
sed -n '1,260p' tests/e2e/README.md 2>/dev/null || true
sed -n '1,220p' tests/e2e/runtime_proof/README.md 2>/dev/null || true
sed -n '1,220p' tests/e2e/release_assembly/README.md 2>/dev/null || true
sed -n '1,220p' tests/e2e/correction/README.md 2>/dev/null || true

# inspect ownership and current public workflow-lane documentation
sed -n '1,220p' .github/CODEOWNERS 2>/dev/null || true
find .github/workflows -maxdepth 2 -type f 2>/dev/null | sort
sed -n '1,220p' .github/workflows/README.md 2>/dev/null || true

# inspect adjacent authority surfaces before adding correction cases
sed -n '1,220p' tests/README.md 2>/dev/null || true
sed -n '1,220p' contracts/README.md 2>/dev/null || true
sed -n '1,220p' policy/README.md 2>/dev/null || true
sed -n '1,220p' schemas/README.md 2>/dev/null || true
sed -n '1,220p' docs/README.md 2>/dev/null || true

# check whether doctrine-proposed correction docs already exist locally
sed -n '1,220p' docs/runbooks/correction.md 2>/dev/null || true
sed -n '1,220p' docs/runbooks/rollback.md 2>/dev/null || true
sed -n '1,220p' docs/runbooks/stale_projection.md 2>/dev/null || true

# search for correction vocabulary before inventing new names
grep -RIn \
  -e 'CorrectionNotice' \
  -e 'ReleaseManifest' \
  -e 'ReleaseProofPack' \
  -e 'ProjectionBuildReceipt' \
  -e 'EvidenceBundle' \
  -e 'RuntimeResponseEnvelope' \
  -e 'superseded' \
  -e 'withdrawn' \
  -e 'stale-visible' \
  -e 'CORRECTION-PENDING' \
  -e 'replacement' \
  tests contracts policy schemas docs .github 2>/dev/null || true
```

### First local review pass

1. Confirm whether the checked-out branch still matches the current public `tests/e2e/correction/` shape.
2. Confirm whether this leaf is still README-only or already contains executable cases.
3. Confirm the actual runner/toolchain before documenting any command beyond safe inspection.
4. Confirm whether a proposed case is honestly correction-led, not release-assembly-led or runtime-led.
5. Confirm which visible cues the case must preserve (`superseded`, `withdrawn`, `stale-visible`, `correction-pending`, or precision narrowing).
6. Confirm which proof objects the case should consume rather than redefine.

## Usage

### When a case belongs here

Use `tests/e2e/correction/` when the smallest honest proof has to show that a correction stays visible and reconstructable across a whole path.

Typical cases include:

- a release-backed outward result becomes `superseded` and must link cleanly to a replacement release
- a published output is `withdrawn` or narrowed and the user-facing state must stay visible
- a corrected authoritative scope exists but derived delivery is still `stale-visible` until rebuild finishes
- a correction must propagate into outward trust surfaces such as map, dossier, story, Focus, or export
- a correction changes precision or access and the generalization/redaction has to stay inspectable
- an audit trail must prove that no silent overwrite occurred

### Naming guidance

Prefer burden-led names over generic test buckets.

| Better | Avoid |
|---|---|
| `supersession/` | `misc/` |
| `withdrawal/` | `correction_v2/` |
| `replacement_lineage/` | `ui_cases/` |
| `stale_visible/` | `edge_cases/` |
| `correction_pending/` | `helpers_everything/` |

Suggested test-file naming pattern:

```text
<subject>.<correction-burden>.<expected-visible-state>.test.*
```

Examples:

```text
release.supersession.visible_state.test.*
correction_notice.replacement_lineage.test.*
export.withdrawal.visible_denial.test.*
projection.stale_visible.after_correction.test.*
focus.corrected_claim.lineage_visible.test.*
```

### Placement rule

Choose the smallest honest proof home.

- If the case is about runtime outcome selection with no correction lineage, move it to [`../runtime_proof/README.md`](../runtime_proof/README.md).
- If the case is about publish/promotion/release evidence with no outward correction burden, move it to [`../release_assembly/README.md`](../release_assembly/README.md).
- If the case is only about schema validity, use the contracts/schema surfaces instead of widening this leaf.
- If the case is only about policy grammar, reason codes, or obligations, keep it in policy-oriented tests.
- If the case is only about accessibility presentation, keep it in the accessibility family.

### Escalation rule

A correction case stays here when **correction lineage is the main question**.

Escalate only when the proof stops being leaf-specific and becomes a broader e2e family concern, such as:

- a single run that must prove release assembly **and** runtime proof **and** correction together
- a steward or review workflow that spans multiple independent boundaries
- a repo-level orchestration flow that would make this leaf only one step in a larger governed drill

## Diagram

```mermaid
flowchart LR
    A[Affected release-backed output] --> B[Correction trigger]
    B --> C[Emit CorrectionNotice]
    C --> D{Replacement release ready?}
    D -- No --> E[Remain visible as stale-visible / withdrawn / correction-pending]
    D -- Yes --> F[Link replacement release]
    F --> G[Rebuild or repoint derived delivery]
    E --> H[Map / dossier / story / Focus / export show lineage]
    G --> H
    H --> I[Archive audit output and drill evidence]
    B -. forbidden .-> X[Silent overwrite]
```

## Tables

### Correction proof matrix

| Case | Must show end to end | Minimum proof objects | Minimum outward cues |
|---|---|---|---|
| Supersession with replacement | Old output is no longer primary, replacement is linked, and lineage is reconstructable | `CorrectionNotice` + affected release ref + replacement release ref | visible `superseded` cue plus replacement linkage |
| Withdrawal without replacement | Output is no longer valid or no longer publishable, and the system does not bluff around it | `CorrectionNotice` + review/policy linkage where relevant | visible `withdrawn` or equivalent unavailable state |
| Stale-visible before rebuild | Corrected authoritative scope exists, but derived delivery has not finished rebuilding | `CorrectionNotice` + release linkage + projection/rebuild context | visible `stale-visible` or `correction-pending` cue |
| Runtime correction propagation | A corrected claim no longer resolves as if the old state were still valid | `CorrectionNotice` + `EvidenceBundle` + `RuntimeResponseEnvelope` where runtime is in scope | visible corrected lineage or fail-closed runtime outcome |
| Generalized replacement | Precision narrows after correction and the system stays explicit about the downgrade | `CorrectionNotice` + policy/review linkage + affected release ref | visible generalization / reduced-precision cue |

### Placement matrix

| If you need to prove... | Best home | Why |
|---|---|---|
| Full correction lineage and visible user-facing state change | `tests/e2e/correction/` | That is this leaf’s core burden |
| Release assembly, proof-pack completeness, or promotion readiness without correction | `tests/e2e/release_assembly/` | That leaf owns release-bearing proof first |
| Runtime `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` behavior without correction propagation | `tests/e2e/runtime_proof/` | Keep runtime outcome proof honest and smaller |
| `CorrectionNotice` schema shape, valid/invalid fixtures, or contract grammar | `tests/contracts/` plus authoritative contract homes | Behavior proof should not replace contract authority |
| Reason/obligation logic or deny-by-default decision grammar for correction | `tests/policy/` plus authoritative policy homes | Keep policy law isolated when possible |
| Accessibility-only correction cues | `tests/accessibility/` | Interaction/readability proof should stay first-class |
| Deterministic rerun or replay sameness | `tests/reproducibility/` | Repeatability is not the same as correction lineage |

## Task list / definition of done

### First executable suite bootstrap

- [ ] Confirm whether a repo-wide runner, fixture convention, or workflow already governs this leaf.
- [ ] Add one synthetic, public-safe correction scenario before widening the tree.
- [ ] Reuse authoritative contract and policy language instead of cloning it locally.
- [ ] Assert **no silent overwrite** as part of the case, not as an afterthought.
- [ ] Assert at least one outward trust cue when the correction changes user-visible meaning.
- [ ] Capture affected and replacement release refs, or explicitly record that no replacement exists.
- [ ] Capture audit output and any screenshots/snapshots/diffs needed to review the correction path.
- [ ] Update adjacent docs if the leaf stops being README-only or if a stable local invocation path is introduced.

### Definition of done

1. The case is correction-led and whole-path, not merely a runtime or release test in disguise.
2. Affected and replacement scopes are explicit, or the absence of replacement is explicit.
3. `CorrectionNotice` or equivalent correction lineage is emitted, asserted, or otherwise made reconstructable.
4. At least one outward trust surface shows a visible correction consequence when user meaning changes.
5. Derived delivery either rebuilds/repoints or remains visibly stale instead of drifting silently.
6. Evidence linkage remains one hop away from the corrected claim where evidence resolution is in scope.
7. The case proves fail-closed behavior when correction cannot complete cleanly.
8. Local and/or CI invocation is documented, or explicitly marked **NEEDS VERIFICATION**.

## FAQ

### Why is `correction/` a separate e2e leaf instead of living inside `release_assembly/`?

Because correction is not just a release concern. It is a lineage and visibility concern. This leaf exists to prove that change stays inspectable after publication, not merely that a release artifact was assembled correctly.

### Does the current public repo prove executable correction drills?

No. The public branch currently proves the leaf exists, is README-only, and documents its correction burden. It does not prove a runner, case depth, required checks, or exercised drills.

### Can this leaf own the authoritative `CorrectionNotice` schema?

No. This leaf should consume correction contracts and policy outputs from their authoritative homes. It should prove how they behave together, not redefine them here.

### What is the best first executable case?

One synthetic, public-safe correction drill that proves:
1. an outward result changes,
2. the correction becomes visible,
3. lineage survives,
4. no silent overwrite occurs.

## Appendix

<details>
<summary>Correction-specific object families and visible states</summary>

### Object families this leaf is likely to touch

| Object family | Why this leaf may need it |
|---|---|
| `CorrectionNotice` | Primary correction-lineage object |
| `ReleaseManifest` / `ReleaseProofPack` | Anchors affected and replacement release scope |
| `ProjectionBuildReceipt` | Useful when corrected delivery must rebuild or repoint |
| `EvidenceBundle` | Keeps corrected support inspectable one hop away |
| `RuntimeResponseEnvelope` | Useful when correction changes runtime-visible behavior |
| `DecisionEnvelope` / `ReviewRecord` | Useful when correction involves review, denial, narrowing, or rights changes |

### Visible trust states to keep explicit when relevant

| Visible state | Why it matters |
|---|---|
| `superseded` | Signals that the older result is no longer primary |
| `withdrawn` | Signals that the prior result should not be used |
| `stale-visible` | Signals that the surface is intentionally visible but not yet refreshed |
| `correction-pending` | Signals that a correction exists but full replacement is not yet complete |
| `generalized` | Signals that a corrected replacement is deliberately less precise |
| replacement linked | Signals where the user should go next instead of leaving the correction as a dead end |

</details>

[Back to top](#correction)

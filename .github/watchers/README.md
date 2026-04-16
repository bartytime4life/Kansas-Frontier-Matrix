<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS_VERIFICATION
title: .github/watchers
type: standard
version: v1
status: draft
owners: @bartytime4life
created: 2026-03-29
updated: 2026-04-16
policy_label: public
related:
  - .github/README.md
  - .github/workflows/README.md
  - .github/actions/README.md
  - .github/CODEOWNERS
  - .github/PULL_REQUEST_TEMPLATE.md
  - ../data/receipts/README.md
  - ../data/work/README.md
  - ../tools/validators/README.md
  - ../tools/attest/README.md
tags: [kfm, github, watchers, governance, ci, receipts, proofs, gatehouse]
notes:
  - Current public main still shows `.github/watchers/` as README-only.
  - This revision aligns watcher doctrine with the updated workflow documentation: watchers are orchestrated by workflows, but watcher logic does not belong in `.github/watchers/`.
  - Receipt and proof separation is now explicit: watcher receipts are governed process memory; proofs remain separate trust objects.
  - Exact active-branch workflow inventory, watcher runtime code owners, and any non-public automation state remain UNKNOWN / NEEDS VERIFICATION.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `.github/watchers`

Gatehouse documentation lane for watcher doctrine, orchestration boundaries, receipt-bearing review posture, and future runtime handoff in Kansas Frontier Matrix.

> **Status:** experimental  
> **Owners:** `@bartytime4life`  
> **Path:** `.github/watchers/README.md`  
> **Repo fit:** docs-only watcher lane inside the `.github` gatehouse; upstream from [../README.md](../README.md), [../workflows/README.md](../workflows/README.md), [../actions/README.md](../actions/README.md), [../CODEOWNERS](../CODEOWNERS), and [../PULL_REQUEST_TEMPLATE.md](../PULL_REQUEST_TEMPLATE.md); downstream into future watcher runtime, policy, contracts, tests, receipts, and release evidence.  
> ![Status](https://img.shields.io/badge/status-experimental-orange) ![Owners](https://img.shields.io/badge/owners-%40bartytime4life-blue) ![Path](https://img.shields.io/badge/path-.github%2Fwatchers-lightgrey) ![Public main](https://img.shields.io/badge/public__main-README--only-lightgrey) ![Posture](https://img.shields.io/badge/posture-docs--only%20gatehouse-red) ![Receipts](https://img.shields.io/badge/receipts-process%20memory-informational)  
> **Quick jump:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Tables](#tables) · [Task list](#task-list) · [FAQ](#faq) · [Appendix](#appendix)

> [!IMPORTANT]
> Current public `main` inspection supports `.github/watchers/` as a **README-only** lane. This directory is presently a **docs-only watcher surface**, not a proven runtime implementation surface.

> [!NOTE]
> Use these labels throughout this README:
>
> - **CONFIRMED** = directly visible in the supplied repo Markdown or current checked-in public tree
> - **INFERRED** = conservative conclusion from confirmed repo evidence and KFM doctrine
> - **PROPOSED** = doctrine-consistent but not yet proven as checked-in behavior
> - **UNKNOWN** = not verifiable from current public evidence
> - **NEEDS VERIFICATION** = placeholder to close before merge or release-significant claims

> [!CAUTION]
> Watcher doctrine may live here. Canonical policy meaning, contract truth, tests, runtime code, receipt storage, and publish authority must not silently migrate into this docs lane.

---

## Scope

`.github/watchers/` is the watcher-facing edge of KFM’s repo-side gatehouse.

Today, this directory does four useful jobs:

- preserves watcher doctrine in a reviewable public place
- records what the current public tree actually proves
- keeps watcher orchestration distinct from watcher implementation
- prevents documentation from overclaiming runtime maturity, publish authority, or artifact state

It should **not** pretend that checked-in watcher runtime jobs, adapters, proof packs, or workflow YAML already exist in this directory when the current public tree does not show them.

### What this README is for

Use this file to keep five things clear:

1. what watcher doctrine requires
2. what public `main` currently proves
3. where watcher logic belongs once real code lands
4. how watcher workflows relate to this lane without collapsing boundaries
5. how receipts differ from proofs in watcher-bearing automation

### Current truth boundary

- **CONFIRMED:** `.github/watchers/README.md` exists
- **CONFIRMED:** the watcher lane sits under the `.github` gatehouse
- **CONFIRMED:** current public `main` shows this lane as documentation-only
- **CONFIRMED:** watcher behavior is expected to remain review-bearing and governed
- **INFERRED:** watcher orchestration belongs in `.github/workflows/`, not in this directory
- **PROPOSED:** future runtime watcher jobs, proof objects, and workflow implementations
- **UNKNOWN:** any non-public workflow YAML, GitHub ruleset, deployment, or emitted proof pack not visible in the checked-in public tree

### Core watcher doctrine captured here

Watcher behavior in KFM should remain:

- **bounded** — explicit source, cadence, and scope
- **review-bearing** — visible to maintainers before trust-significant change
- **fail-closed** — validation or policy failure stops downstream side effects
- **receipt-emitting** — process memory is preserved when runs occur
- **not self-publishing** — watchers do not become hidden release or publication lanes
- **rebuildable** — watcher outputs are derived from upstream sources and config, not sovereign truth

[Back to top](#top)

---

## Repo fit

This README belongs to the same review and governance boundary as the rest of `.github/`.

### Upstream and adjacent anchors

| Relation | Path | Why it matters |
| --- | --- | --- |
| Parent gatehouse | [../README.md](../README.md) | Defines `.github/` as the repo-side gatehouse for review, automation, and watcher control |
| Workflow documentation lane | [../workflows/README.md](../workflows/README.md) | Holds workflow inventory doctrine, including watcher orchestration signal and current drafted watcher-lane guidance |
| Local action documentation lane | [../actions/README.md](../actions/README.md) | Shows the reusable repo-local action seam that future watcher orchestration may call |
| Review ownership | [../CODEOWNERS](../CODEOWNERS) | Makes `/.github/` review routing explicit |
| PR evidence template | [../PULL_REQUEST_TEMPLATE.md](../PULL_REQUEST_TEMPLATE.md) | Requires truth labels, evidence links, validation, rollout, and rollback structure |
| Root operating index | [../../README.md](../../README.md) | Anchors repo-wide posture and visible top-level directory logic |
| Receipt surface | [../../data/receipts/README.md](../../data/receipts/README.md) | Watcher runs should emit governed process memory there, not under `.github/` |
| Work surface | [../../data/work/README.md](../../data/work/README.md) | Temporary watcher state belongs in bounded work paths, not in this docs lane |
| Validator surface | [../../tools/validators/README.md](../../tools/validators/README.md) | Watcher outputs should be contract- and linkage-checkable outside prose |
| Attestation surface | [../../tools/attest/README.md](../../tools/attest/README.md) | Proof-pack or attestation assembly is a separate concern from watcher receipts |
| Future canonical downstream surfaces | [../../policy/](../../policy/), [../../contracts/](../../contracts/), [../../schemas/](../../schemas/), [../../tests/](../../tests/), [../../docs/](../../docs/), [../../packages/](../../packages/) | Future watcher runtime and proof objects must live outside this docs lane |

### Boundary rule

This directory may describe:

- watcher doctrine
- current public inventory
- migration or handoff guidance
- orchestration boundaries
- receipt / proof distinctions
- review expectations for future watcher work

This directory must not become the sovereign home of:

- canonical policy logic
- canonical contracts or schemas
- runtime watcher code
- receipt storage
- proof-pack storage
- secret material
- autonomous publish authority
- long-lived evidence archives

### Watchers versus workflows

Keep the split explicit:

| Surface | Owns what |
| --- | --- |
| `.github/watchers/` | watcher doctrine, scope notes, handoff guidance, and review expectations |
| `.github/workflows/` | event triggers, scheduling, orchestration, validation order, artifact upload, and merge/promotion gates |
| `tools/` / `apps/` / future runtime owner surface | actual watcher logic, source handling, parsing, normalization, and deterministic behavior |
| `data/work/` | bounded temporary working state |
| `data/receipts/` | governed process memory |
| proof / release-evidence surfaces | release-significant or review-significant trust objects |

That boundary keeps this lane documentary, not operational.

---

## Accepted inputs

Use this directory for small, watcher-facing documentation artifacts only.

| What belongs here | Why |
| --- | --- |
| `README.md` | Directory contract and current public inventory |
| short watcher-lane notes | Keeps future implementation handoff reviewable |
| links to sibling `.github/` docs | Preserves gatehouse context for watcher changes |
| minimal illustrative examples | Clarifies watcher posture without pretending runtime exists here |
| migration notes | Records where real watcher code, receipts, and proofs must move once checked in |
| doctrine notes on receipts vs proofs | Prevents watcher artifacts from being conflated |

---

## Exclusions

Keep these out of `.github/watchers/` unless there is a very narrow documentation reason.

| Keep out of this directory | Why | Put it here instead |
| --- | --- | --- |
| checked-in workflow YAML as the canonical watcher home | job orchestration belongs in the workflow lane | [../workflows/](../workflows/) |
| repo-local action implementations | action glue belongs in the action lane | [../actions/](../actions/) |
| canonical policy bundles or rule bodies | policy meaning must stay reviewable outside prose | [../../policy/](../../policy/) |
| contract or schema truth | this README may reference them, but must not own them | [../../contracts/](../../contracts/), [../../schemas/](../../schemas/) |
| runtime watcher code, adapters, schedulers | current public `main` does not prove this directory as a runtime owner surface | future owner surface outside `.github/` (**NEEDS VERIFICATION**) |
| emitted receipts | receipts are governed process memory, not gatehouse docs | [../../data/receipts/](../../data/receipts/) |
| proof packs, attestations, release evidence | proofs are separate trust objects, not watcher-lane prose | governed proof / release surfaces outside `.github/` |
| working state or caches | temporary state belongs in bounded work paths | [../../data/work/](../../data/work/) |
| secrets, credentials, or publish keys | docs lanes must never become secret stores | GitHub environments or external secret management |

---

## Directory tree

### Current public inventory

```text
.github/
  watchers/
    README.md
```

### Adjacent confirmed gatehouse surfaces

```text
.github/
  README.md
  CODEOWNERS
  PULL_REQUEST_TEMPLATE.md
  actions/
    README.md
    metadata-validate-v2/
    metadata-validate/
    opa-gate/
    provenance-guard/
    sbom-produce-and-sign/
  workflows/
    README.md
```

### Current thin-slice orchestration signal

The watcher lane itself is still README-only, but adjacent workflow documentation now points to a drafted watcher orchestration family.

```text
.github/workflows/
  README.md
  incremental-stac-watcher.yml   # drafted in-session; active-branch presence NEEDS VERIFICATION
```

> [!NOTE]
> The current public tree still supports a **docs-only watcher lane**. Any top-level watcher runtime path, source adapter, or watcher-specific workflow YAML should be treated as **PROPOSED** or **NEEDS VERIFICATION** unless it is directly visible in the checked-in tree.

---

## Quickstart

### 1) Inspect the current watcher lane

```bash
ls -la .github/watchers
sed -n '1,260p' .github/watchers/README.md
```

### 2) Check the gatehouse surfaces that shape watcher review

```bash
sed -n '1,260p' .github/README.md
sed -n '1,260p' .github/workflows/README.md
sed -n '1,260p' .github/actions/README.md
sed -n '1,160p' .github/CODEOWNERS
sed -n '1,260p' .github/PULL_REQUEST_TEMPLATE.md
```

### 3) Before describing runtime watcher behavior

Confirm all of these first:

1. the owning code surface is checked in and visible
2. policy / contract / schema / test surfaces are linked
3. any workflow claim points to an actual checked-in YAML or to a clearly labeled proposal
4. any receipt claim points to `data/receipts/**`, not to ad hoc artifact storage
5. any proof claim stays separate from receipt claims

### 4) Before documenting watcher pathing

Inspect the expected governed surfaces:

```bash
ls -la data/work data/receipts tools/validators tools/attest 2>/dev/null || true
find .github/workflows -maxdepth 1 -type f \( -name '*.yml' -o -name '*.yaml' \) | sort
```

> [!WARNING]
> Do not add commands for non-existent runtime paths, source adapters, or workflow YAMLs until they are actually present in the reviewed tree.

---

## Usage

### How to use this README today

Use this file as a **truth-preserving boundary document**.

It should:

- state watcher doctrine clearly
- keep current public tree claims narrow
- preserve review-bearing and fail-closed posture
- point runtime work toward canonical policy, contract, schema, test, receipt, and proof surfaces
- prevent watchers from being described as hidden publish lanes

### What this directory currently proves

Current public `main` supports these statements:

- KFM has a watcher lane under `.github/`
- that lane is currently documentation-only
- watcher changes belong inside the same PR-first, evidence-aware gatehouse as other trust-significant repo surfaces
- watcher doctrine is being framed as derived, rebuildable, receipt-bearing, and not self-publishing
- watcher orchestration is adjacent to this lane rather than owned by it

### What this directory does **not** currently prove

This README alone does **not** prove:

- a checked-in runtime under a watcher owner surface
- a current watcher workflow YAML on public `main`
- live source adapters for any specific external source family
- proof packs or attestation bundles built from watcher runs
- autonomous publication behavior
- exact runtime or release path owners outside the visible public tree

### What a review-ready watcher proposal must name

A credible watcher proposal should identify:

1. the owner surface for runtime code
2. the source family and scope window
3. the bounded work path it uses
4. the receipt path it emits into
5. the validator or contract surface it must satisfy
6. the policy gate it must satisfy
7. whether any proof object is assembled after validation
8. the rollback or supersession path if a watcher emits a bad result

Illustrative example only:

```yaml
watcher_proposal:
  truth_posture: PROPOSED
  owner_surface: NEEDS VERIFICATION
  source_family: stac
  emit_only: true
  work_path: data/work/watchers/incremental-stac
  receipt_path: data/receipts/incremental_stac
  proof_objects:
    - run_receipt
    - policy_result
    - contract_validation
    - optional_proof_pack
    - rollback_note
  publish_authority: none
```

### Receipt / proof separation for watchers

This distinction should remain explicit everywhere watcher automation is documented:

| Object | Meaning |
| --- | --- |
| **Receipt** | process memory of a watcher run, validation result, or replay/correction trace |
| **Proof** | higher-order trust object such as a proof pack, attestation, or release-significant evidence bundle |
| **Summary** | reviewer-facing convenience rendering, not sovereign truth |
| **Work state** | bounded temporary intermediate state |

A watcher may emit receipts on every run. It should not silently imply that every receipt is also a proof object.

### How watcher workflows should be described here

When this README references watcher workflows, it should describe them in governance terms, not implementation hype.

Good documentation language:

- scheduled or manual orchestration
- explicit source and work path
- receipt emission
- contract validation
- policy validation
- commit or artifact upload only on pass
- optional proof-pack build after validation

Bad documentation language:

- self-healing publish bot
- autonomous release agent
- always-sync background lane
- automatic truth updater

---

## Diagram

```mermaid
flowchart LR
    A[".github/watchers/README.md<br/>CONFIRMED docs-only lane"] --> B["Watcher doctrine<br/>bounded · review-bearing · fail-closed"]

    B --> C[".github/workflows/README.md<br/>workflow orchestration doctrine"]
    B --> D[".github/actions/README.md<br/>reusable local action seam"]
    B --> E[".github/CODEOWNERS + PR template<br/>review boundary"]

    B -. PROPOSED / NEEDS VERIFICATION .-> F["Runtime watcher implementation<br/>owner surface outside .github/watchers"]
    F -. bounded temp state .-> G["data/work/**"]
    F -. process memory .-> H["data/receipts/**"]
    F -. validate against .-> I["contracts / schemas / policy / tests"]
    F -. optional higher-order proof .-> J["proof / release-evidence surfaces"]
    C -. orchestrates, not owns .-> F
```

---

## Tables

### Current public-main posture

| Surface | Current visible state | Posture | Why it matters |
| --- | --- | --- | --- |
| `.github/watchers/README.md` | present | **CONFIRMED** | watcher lane exists in the checked-in public tree |
| `.github/watchers/` | `README.md` only | **CONFIRMED** | current public watcher lane is documentary, not a proven runtime |
| `.github/workflows/` | README confirmed; watcher workflow signal drafted in-session | **CONFIRMED** README / **NEEDS VERIFICATION** watcher YAML | watcher orchestration is adjacent, not owned here |
| `.github/actions/` | local action dirs plus docs | **CONFIRMED** | future watcher automation can reuse gatehouse actions without moving canonical logic here |
| `/.github/` ownership | covered by `@bartytime4life` | **CONFIRMED** | review routing exists for watcher-lane changes |
| exact rulesets / required checks / OIDC / environment approvals | not derivable from checked-in tree alone | **UNKNOWN** | repo state and platform state are not the same thing |

### Watcher claim map

| Claim | Current status | Where it must be proven |
| --- | --- | --- |
| watcher doctrine belongs in the gatehouse | **CONFIRMED** | this README and sibling `.github/` docs |
| watcher orchestration belongs in workflows rather than here | **INFERRED** | `.github/workflows/` and checked-in YAML |
| runtime watcher code is checked in on public `main` | **UNKNOWN** | actual code inventory in a visible owner surface |
| watcher workflow YAML exists on public `main` | **UNKNOWN** | checked-in file under [../workflows/](../workflows/) |
| watcher runs emit receipts into governed storage | **PROPOSED** doctrine / **NEEDS VERIFICATION** implementation | `data/receipts/` plus runtime code and workflows |
| watcher proofs are separate from receipts | **INFERRED** from KFM doctrine | proof / release-evidence surfaces and attestation tooling |
| watcher lanes should remain PR-first and review-bearing | **CONFIRMED** doctrine / **PROPOSED** implementation | future workflows, policy gates, and receipts |

### Candidate thin-slice families

These are useful **PROPOSED** watcher families, not current public-runtime claims.

| Candidate lane | Representative sources | Why it fits a thin slice |
| --- | --- | --- |
| hydrology / soil moisture | Kansas Mesonet, USGS NWIS | aligns with KFM’s hydrology-first proof bias |
| incremental STAC closure | STAC catalogs or collections with bounded freshness checks | natural fit for receipt-bearing incremental observation |
| vegetation change | HLS VI plus corroborating disturbance sources | clear temporal comparison burden and strong map value |
| air / atmospheric context | state or public air-quality feeds | compact change detection with obvious public relevance |
| stewardship notices | USFWS pages or similar authority notices | low-risk text or metadata change detection with a clear review path |

---

## Task list

- [ ] Keep `.github/watchers/` accurate as a docs-only lane until runtime watcher assets are actually checked in.
- [ ] Keep watcher doctrine aligned with [../workflows/README.md](../workflows/README.md) so orchestration and implementation boundaries do not drift.
- [ ] Remove any path drift that implies a checked-in top-level watcher runtime without proof.
- [ ] When the first watcher workflow YAML lands, cross-link it here **and** in [../workflows/README.md](../workflows/README.md).
- [ ] When runtime watcher code lands, record the owning surface and update this README’s repo fit and exclusions.
- [ ] When receipts land, document their governed home under `data/receipts/**` rather than treating them as generic CI artifacts.
- [ ] Link first real watcher proof objects only after receipts, contract validation, policy results, and tests exist in-tree.
- [ ] Prefer one bounded hydrology- or STAC-first thin slice before broadening into a multi-source watcher wave.

### Definition of done

This README is in a healthy state when:

- current public inventory is accurate
- future implementation guidance is clearly labeled **PROPOSED**
- no path, command, or file name implies runtime existence without proof
- watcher logic, orchestration, work state, receipts, and proofs are clearly separated
- adjacent gatehouse links are valid
- watcher doctrine stays subordinate to canonical policy, contract, schema, and test surfaces

---

## FAQ

### Is `.github/watchers/` the runtime watcher directory?

No. Current public `main` shows `.github/watchers/` as `README.md` only.

### Can this README talk about watcher source families?

Yes, as long as they are clearly labeled as **PROPOSED** thin-slice candidates rather than current checked-in adapters.

### Where should watcher receipts live?

Not here. Receipts are governed process memory and should live under `data/receipts/**`.

### Where should watcher proof packs or attestations live?

Not here. They belong in the appropriate governed proof or release-evidence surfaces.

### Why keep a watcher lane under `.github/` at all?

Because watcher behavior changes trust state. Even before runtime code is visible, the gatehouse is the right place to define review-bearing, fail-closed, non-self-publishing expectations.

### What is the smallest credible next step?

A read-only, bounded watcher thin slice whose workflow orchestrates a single source family, uses `data/work/**` for temporary state, emits receipts to `data/receipts/**`, validates them, and stops before autonomous publication.

---

## Appendix

<details>
<summary>Proposed watcher packet and working terms</summary>

### Proposed watcher packet

A future runtime watcher implementation should not arrive as code alone.

| Object | Purpose | Status here |
| --- | --- | --- |
| watcher scope note | states source family, cadence, and claim class | **PROPOSED** |
| contract validation result | proves machine-shape expectations passed or failed | **PROPOSED** |
| policy result | proves deny-by-default review passed or failed | **PROPOSED** |
| test / fixture links | show deterministic behavior and negative-path coverage | **PROPOSED** |
| `run_receipt` or equivalent | binds inputs, outputs, and audit linkage as process memory | **PROPOSED** |
| optional proof pack | higher-order trust object assembled after sufficient validation | **PROPOSED** |
| rollback / supersession note | explains what happens when a watcher emits a bad or stale result | **PROPOSED** |

### Working terms used here

- **docs-only lane** — a checked-in documentation surface with no proven runtime inventory behind it
- **review-bearing** — a watcher may open a governed review path, but does not silently change trust state
- **receipt-emitting** — watcher runs preserve process memory suitable for replay, correction, and audit
- **derived / rebuildable** — watcher outputs can be regenerated from upstream sources and config; they do not become sovereign truth
- **PR-first** — review and evidence come before merge or release-bearing trust change

Until those proof objects are checked in, keep this lane documentary and conservative.

</details>

[Back to top](#top)

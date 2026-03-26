<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<NEEDS-VERIFICATION>
title: Kansas Frontier Matrix — Remote Sensing Time-Series Analysis
type: standard
version: v1
status: draft
owners: @bartytime4life
created: <NEEDS-VERIFICATION>
updated: <NEEDS-VERIFICATION>
policy_label: <NEEDS-VERIFICATION>
related: [../../README.md, ../README.md, ../validation/README.md]
tags: [kfm, analyses, remote-sensing, time-series]
notes: [Path is repo-targeted from the analyses index; doc_id, dates, and policy label require mounted-repo verification.]
[/KFM_META_BLOCK_V2] -->

# Kansas Frontier Matrix — Remote Sensing Time-Series Analysis

Governed module guide for documenting time-aware remote-sensing analyses, outputs, validation burden, and downstream reuse under `docs/analyses/remote-sensing/time-series/`.

> [!IMPORTANT]
> This README describes a **derived analysis surface**, not a sovereign truth surface. Time-series products belong here only when their inputs, methods, uncertainty, and evidence linkage stay visible at the point of use.

**Status:** experimental  
**Owners:** @bartytime4life  
**Path:** `docs/analyses/remote-sensing/time-series/README.md`  
**Repo fit:** child analysis module under `docs/analyses/remote-sensing/`, aligned to the broader `docs/analyses/` verification-first structure.

![Status](https://img.shields.io/badge/status-experimental-blue)
![Surface](https://img.shields.io/badge/surface-analysis%20module-6f42c1)
![Scope](https://img.shields.io/badge/scope-remote%20sensing%20time--series-0a7ea4)
![Truth](https://img.shields.io/badge/truth-CONFIRMED%20%7C%20INFERRED%20%7C%20NEEDS--VERIFICATION-444)
![Docs](https://img.shields.io/badge/docs-repo--native-success)

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Inputs](#inputs) · [Exclusions](#exclusions) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Tables](#tables) · [Task list](#task-list) · [FAQ](#faq) · [Appendix](#appendix)

---

## Scope

This module is for **time-aware remote-sensing analysis artifacts** and the Markdown that explains them.

It should capture analyses where change over time is the point, not an incidental attribute. Typical examples include:

- seasonal or phenological trajectories
- disturbance and recovery narratives
- trend fitting and breakpoint analysis
- image-collection compositing across a stated time window
- segment-based change detection
- index or classification evolution through time
- multi-date comparison products used by map, dossier, compare, story, or Focus surfaces

The module should make five things explicit:

1. **what changed**
2. **over which time window**
3. **from which inputs**
4. **under which assumptions**
5. **with what downstream publication burden**

> [!NOTE]
> In KFM terms, a time-series result is usually **derived** or **modeled** unless it has been explicitly promoted with the same release discipline expected elsewhere in the system.

[Back to top](#kansas-frontier-matrix--remote-sensing-time-series-analysis)

## Repo fit

| Role | Path | Relationship |
|---|---|---|
| Parent analyses index | [`../../README.md`](../../README.md) | Governing docs surface for analysis modules |
| Parent remote-sensing lane | [`../README.md`](../README.md) | Remote-sensing sibling/parent context |
| Validation companion | [`../validation/README.md`](../validation/README.md) | Validation-specific methods, error characterization, and review burden |
| This file | `./README.md` | Time-series module contract for scope, inputs, outputs, and reuse rules |

### Upstream

This README should inherit the `docs/analyses/` pattern: narrow module scope, explicit inputs, explicit exclusions, visible uncertainty, and a README that behaves like a maintained trust surface rather than a placeholder.

### Downstream

Material documented here may feed:

- map or compare views
- dossier context panels
- story nodes
- export packages
- bounded Focus responses

But only when release state, evidence linkage, and policy posture remain visible.

### Placement rule

Use this directory when the analysis is **primarily temporal**.  
Do **not** put work here just because the source imagery happens to contain dates.

[Back to top](#kansas-frontier-matrix--remote-sensing-time-series-analysis)

## Inputs

### Accepted inputs

The following belong here when they are governed, documented, and analysis-relevant:

- released or explicitly scoped image collections
- documented raster stacks used for multi-date analysis
- AOI definitions and masks used in time-windowed processing
- derived indices with named formulas and support semantics
- segment coefficients, trend tables, or time-series summaries
- validation notes tied to time-aware outputs
- notebooks or scripts **only when** they are referenced as implementation aids rather than treated as truth
- figure exports that explain temporal behavior
- method notes that describe cadence, compositing, masking, and model assumptions
- links to release-bearing artifacts, catalogs, or evidence packs where available

### Input discipline

Every non-trivial time-series entry should declare:

| Field | Why it matters |
|---|---|
| Time window | Prevents snapshot ambiguity |
| Cadence / revisit basis | Explains what “series” really means |
| Sensor/platform family | Affects comparability and interpretation |
| Spatial support / resolution | Prevents over-reading fine detail |
| QA / masking strategy | Cloud, shadow, noise, and missingness matter |
| Derived band/index logic | Keeps feature engineering inspectable |
| Method / model version | Makes reruns and corrections possible |
| Validation source | Prevents narrative-only confidence |
| Release state | Separates exploration from publication |
| Rights / sensitivity posture | Needed before outward reuse |

> [!WARNING]
> A sequence of pretty maps is not a time-series analysis record. Without time-window, method, masking, and uncertainty context, it is presentation residue.

[Back to top](#kansas-frontier-matrix--remote-sensing-time-series-analysis)

## Exclusions

This directory should **not** become a catch-all for remote-sensing material.

### Do not put these here

- raw source dumps better kept in source-edge or ingest lanes
- undocumented exploratory figures with no method note
- policy bundles, contract schemas, or CI logic as authoritative source objects
- UI feature proposals that belong in app or UX docs
- single-date image interpretation notes that are not actually temporal
- public-facing claims whose evidence path cannot be reconstructed
- exact sensitive coordinates or precise protected-site disclosures in public docs
- notebook output pasted as if it were already reviewed or released

### Put it elsewhere instead

| Content | Better home |
|---|---|
| Remote-sensing lane overview | [`../README.md`](../README.md) |
| Accuracy assessment / error characterization | [`../validation/README.md`](../validation/README.md) |
| Contracts / schemas / envelopes | repo contract and schema surfaces |
| Story publication guidance | story / publication docs |
| Policy bundles and reason codes | policy surfaces |
| Raw ingest and receipts | source / ingest / pipeline surfaces |

[Back to top](#kansas-frontier-matrix--remote-sensing-time-series-analysis)

## Directory tree

> [!NOTE]
> The public analyses index describes a remote-sensing subtree and names `time-series/`, but exact child-path parity in the mounted repo should still be rechecked before merge. Treat the tree below as a **recommended module-local shape**, not proof that every subpath already exists.

```text
docs/
└── analyses/
    └── remote-sensing/
        ├── README.md
        ├── validation/
        │   └── README.md
        └── time-series/
            ├── README.md
            ├── methods/                # method notes, algorithm writeups, parameter docs
            ├── datasets/               # dataset-specific analysis notes and release references
            ├── notebooks/              # referenced exploratory or reproducible notebooks
            ├── results/                # derived summaries, tables, change outputs
            ├── figures/                # plots and explanatory graphics for review/docs use
            └── validation/             # module-local checks if separate from lane-wide validation
```

### Layout guidance

- Keep the root README explanatory.
- Keep bulky reference material out of the top flow.
- Prefer one README per stable sub-area instead of a flat pile of ad hoc notes.
- Name subfolders by responsibility, not by tool brand.

[Back to top](#kansas-frontier-matrix--remote-sensing-time-series-analysis)

## Quickstart

1. Start from the parent analysis rules in [`../../README.md`](../../README.md).
2. Confirm that the work is truly **time-series** and not just “remote sensing with dates.”
3. Fill the KFM meta block at the top of this file with verified values.
4. State the analysis question in one sentence.
5. Record the time window, cadence basis, sensor/input family, and masking strategy.
6. Link the work to any released dataset, catalog record, evidence pack, or proof artifact that already exists.
7. Mark each output as **observed**, **derived**, **modeled**, **generalized**, or **blocked**.
8. Add uncertainty and validation notes before adding polished figures.
9. Declare whether the output is allowed to feed Story, Focus, Dossier, Compare, or Export.
10. Remove or quarantine anything that implies public readiness without release-bearing evidence.

### Starter checklist

- [ ] Module purpose is temporal, not generic
- [ ] Inputs are named and scoped
- [ ] Time semantics are explicit
- [ ] Method family is stated
- [ ] QA / masking is described
- [ ] Output state labels are visible
- [ ] Validation burden is surfaced
- [ ] Reuse rules are stated
- [ ] Sensitive/public-safe handling is stated
- [ ] Meta block placeholders are resolved or intentionally left flagged

[Back to top](#kansas-frontier-matrix--remote-sensing-time-series-analysis)

## Usage

### Write this README as a contract, not a brochure

Use concise prose, but make the decision-critical parts obvious.

A solid entry in this module usually answers:

- What phenomenon is changing?
- What observations support that claim?
- What part is measured vs derived vs modeled?
- What time basis is the reader supposed to interpret?
- What are the known blind spots?
- What can downstream surfaces safely reuse?

### Recommended subsection pattern for dataset- or method-specific child docs

```markdown
## Purpose
## Question
## Inputs
## Time window and cadence
## Method
## Output state
## Validation / uncertainty
## Release and evidence links
## Reuse constraints
```

### Method families that fit this module

| Method family | Best use here | Main caution |
|---|---|---|
| Seasonal / phenology summaries | Recurring annual behavior, vegetation timing, cyclical patterns | Easy to confuse seasonality with long-term change |
| Trend fitting | Direction and rate over a defined window | Sensitive to missingness, compositing, and breakpoints |
| Breakpoint / segment models | Disturbance, recovery, regime shifts | Derived model segments must not be narrated as direct observation |
| Multi-date compositing | Stable before/after comparison | Composite rules can hide volatility |
| Index trajectories | NDVI, moisture, burn, thermal, or other derived signatures over time | Index meaning is context-dependent, not universal |
| Change classification | Explicit change/no-change or class transition outputs | Validation burden rises fast |
| Multi-sensor fusion | Filling gaps or combining modalities | Cross-sensor comparability needs plain-language caveats |

### Output labeling rule

Use these labels directly in the doc when precision matters:

| Label | Meaning |
|---|---|
| **CONFIRMED** | Verified from repo-visible or release-visible evidence in scope |
| **INFERRED** | Strongly implied by the project structure or evidence, but not directly verified |
| **PROPOSED** | Recommended module pattern or next-step structure |
| **UNKNOWN** | Not verified in the current session |
| **NEEDS VERIFICATION** | Should be checked before treating as authoritative or merge-ready |

[Back to top](#kansas-frontier-matrix--remote-sensing-time-series-analysis)

## Diagram

```mermaid
flowchart LR
    A["Released or explicitly scoped remote-sensing inputs"] --> B["Time-series analysis module"]
    B --> C["Methods / notebooks / parameters"]
    B --> D["Derived outputs"]
    B --> E["Validation / uncertainty / field checks"]
    C --> D
    E --> D
    D --> F["Story / Focus / Dossier / Compare / Export reuse"]
    F --> G["Evidence-linked inspection"]
    H["RAW / WORK / QUARANTINE material"] -. not default public-facing input .-> B
    D -. derived or modeled unless explicitly promoted .-> G
```

### Reading the diagram

- Inputs flow into a temporal analysis record.
- Methods and validation are siblings, not afterthoughts.
- Derived outputs may travel downstream only with evidence-linked inspection.
- Unreleased source-edge material should not silently pass through this README as if it were already publishable.

[Back to top](#kansas-frontier-matrix--remote-sensing-time-series-analysis)

## Tables

### What belongs here

| Item | Belongs here? | Notes |
|---|---:|---|
| Time-windowed index comparison | Yes | Declare formula, masking, and support |
| Pixel/segment trend plots | Yes | State method and uncertainty |
| Disturbance/recovery narrative with release links | Yes | Mark modeled vs observed components |
| Single-date image caption | Usually no | Put with the relevant non-temporal analysis if time is incidental |
| Raw source download log | No | Source/ingest lane |
| Policy reason-code registry | No | Policy lane |
| Story-only editorial prose with no method context | No | Story surface, with links back here if needed |

### Downstream reuse matrix

| Downstream surface | Default stance | Conditions |
|---|---|---|
| Story | Restricted | Allowed when claims are evidence-linked and release state is visible |
| Focus | Restricted | Allowed only for bounded retrieval/synthesis with citation and abstention behavior |
| Dossier | Allowed with care | Time scope, freshness, and uncertainty must remain visible |
| Compare | Strong fit | Requires explicit basis of comparison and matched support semantics |
| Export | Restricted | Needs release-safe scope, lineage, and correction linkage |
| Public map labels | Limited | Avoid overclaiming from modeled or partial outputs |

### Minimum metadata spine for time-series outputs

| Minimum artifact or field | Why it should be present |
|---|---|
| SourceDescriptor reference | Names the source and intake context |
| Time window | Prevents ambiguous interpretation |
| Validation logic or QA note | Makes screening visible |
| ValidationReport or equivalent note | Captures what passed, failed, or remained partial |
| DatasetVersion / result version | Makes supersession possible |
| STAC/DCAT/PROV closure where relevant | Supports outward discovery and lineage |
| EvidenceBundle linkage | Keeps consequential claims inspectable |
| ReleaseManifest / ProofPack reference | Supports publication, rollback, and correction logic |

### Sensor-family reminder

| Sensor / source family | Time-series strength | Interpretation caution |
|---|---|---|
| Multispectral optical | Strong for vegetation, land cover, thermal proxies, change context | Cloud, haze, seasonal mismatch |
| Radar / SAR | Strong where cloud cover is persistent; useful for flood/moisture structure | Speckle, geometry, layover, processing assumptions |
| LiDAR-derived surfaces | Strong for repeat terrain/structure comparisons when aligned carefully | Repeatability and bare-earth vs surface distinctions |
| Administrative or field overlays | Valuable as corroboration and grounding | Not interchangeable with remotely sensed measurement |

[Back to top](#kansas-frontier-matrix--remote-sensing-time-series-analysis)

## Task list

### Definition of done for this module

- [ ] The module purpose is explicitly temporal
- [ ] Parent and sibling links resolve
- [ ] Inputs, time scope, and cadence are named
- [ ] Methods are described in project language, not just tool-brand language
- [ ] Derived vs modeled vs observed states are labeled
- [ ] Validation burden is surfaced in the main flow
- [ ] Public-safe handling is stated
- [ ] At least one downstream reuse rule is explicit
- [ ] Figures do not outrun the evidence
- [ ] Open unknowns stay visible instead of being smoothed away

### Review gates

- [ ] No claim implies release readiness without evidence linkage
- [ ] No modeled output is written as direct observation
- [ ] No single-date view is misrepresented as a long-run trend
- [ ] No sensitive exact-location content is exposed without stated policy posture
- [ ] No absent repo structure is described as mounted fact
- [ ] README remains readable in GitHub without external styling

[Back to top](#kansas-frontier-matrix--remote-sensing-time-series-analysis)

## FAQ

### Does every remote-sensing result with a date belong here?

No. Use this module when the analysis is fundamentally about **change, trajectory, seasonality, segmentation, cadence, or comparison across time**.

### Can this module reference notebooks?

Yes, but notebooks are supporting implementation artifacts unless they are explicitly promoted and linked to release-bearing evidence.

### Are change-detection outputs authoritative?

Usually no. They are typically **derived** or **modeled** until promoted through the same release discipline expected elsewhere in KFM.

### Can Story or Focus quote this module directly?

Only when evidence linkage, uncertainty, and release state stay visible. A smooth visual summary is not enough.

### Can public-facing maps use these outputs?

Yes, selectively. But generalized, stale, partial, modeled, or disputed material should be labeled in place, not hidden in appendix prose.

[Back to top](#kansas-frontier-matrix--remote-sensing-time-series-analysis)

## Appendix

<details>
<summary><strong>Suggested state vocabulary for time-series docs</strong></summary>

| State | Use in this module |
|---|---|
| Observed | Directly measured imagery or field-correlated source content |
| Derived | Computed from observed inputs by a stated rule |
| Modeled | Produced by fitted segments, classification, forecasting, or other model logic |
| Generalized | Reduced-precision or public-safe representation |
| Partial | Incomplete in time, space, quality, or coverage |
| Stale | No longer current enough for the implied use |
| Blocked | Withheld for rights, sensitivity, or publication reasons |

</details>

<details>
<summary><strong>Suggested minimum per-analysis header</strong></summary>

```
## Analysis snapshot

- Question:
- AOI:
- Time window:
- Cadence basis:
- Inputs:
- QA / masking:
- Method family:
- Output state:
- Validation basis:
- Release / evidence links:
- Public-safe notes:
```

</details>

<details>
<summary><strong>Open verification items for this README</strong></summary>

- Exact mounted existence of every child path under `docs/analyses/remote-sensing/time-series/`
- Repo-native document ID assignment convention for the KFM meta block
- Narrower path ownership, if different from `/docs/`
- Policy label taxonomy for this specific module
- Whether module-local `validation/` should exist in addition to the lane-wide validation README
- Whether the repo already uses a more specific analysis template for child-module READMEs

</details>

[Back to top](#kansas-frontier-matrix--remote-sensing-time-series-analysis)

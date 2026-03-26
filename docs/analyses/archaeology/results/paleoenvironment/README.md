<!-- [KFM_META_BLOCK_V2]
doc_id: <REVIEW_REQUIRED: kfm://doc/uuid-not-verified-in-mounted-repo>
title: Kansas Frontier Matrix — Paleoenvironmental Results
type: standard
version: v1
status: review
owners: Paleoenvironment WG · FAIR+CARE Council
created: <REVIEW_REQUIRED>
updated: <REVIEW_REQUIRED>
policy_label: restricted
related: [../README.md, ./climate/README.md, ./paleohydrology/README.md, ./vegetation/README.md, ./seasonality/README.md, ./drought-cycles/README.md, ./predictive/README.md, ./uncertainty/README.md, ./stac/, ./metadata/, ./provenance/]
tags: [kfm, archaeology, paleoenvironment, fair-care, stac, dcat, prov]
notes: [Owners, sibling families, and related paths are source-grounded from attached project documents; exact repo presence, created/updated dates, and canonical doc UUID remain NEEDS VERIFICATION because the mounted repo tree was not visible in the current session.]
[/KFM_META_BLOCK_V2] -->

# Kansas Frontier Matrix — Paleoenvironmental Results

Unified entrypoint for generalized paleoenvironment result families used as environmental context within KFM archaeology workflows.

> [!NOTE]
> **Status:** active *(source-grounded; mounted repo state not directly verified)*  
> **Owners:** Paleoenvironment WG · FAIR+CARE Council  
> **Classification:** Internal / CARE-Governed  
> **Path:** `docs/analyses/archaeology/results/paleoenvironment/README.md`  
> ![Status: Active](https://img.shields.io/badge/status-active-0a7f5a?style=flat-square)
> ![Policy: CARE-Governed](https://img.shields.io/badge/policy-CARE--governed-5b4db1?style=flat-square)
> ![Scope: Paleoenvironment](https://img.shields.io/badge/scope-paleoenvironment-1f6feb?style=flat-square)
> ![Evidence: PDF-grounded](https://img.shields.io/badge/evidence-PDF--grounded-8a4600?style=flat-square)
>  
> **Quick jump:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Tables](#tables) · [Task list](#task-list) · [FAQ](#faq) · [Appendix](#appendix)

> [!IMPORTANT]
> This directory is for **environmental context and derived result products**, not for cultural authority, exact-site disclosure, or unrestricted interpretive claims. Anything that risks cultural attribution, precise archaeological exposure, or unsupported historical narrative must be generalized, withheld, or routed into a stricter steward workflow.

> [!WARNING]
> The current-session workspace evidence for this task was document-only. The sibling paths and tree below are therefore **source-grounded but repo-unverified**. Verify local names and links before commit.

## Scope

This directory groups KFM archaeology-facing **paleoenvironmental analytical results** that provide deep-time environmental context for Late Prehistoric, Protohistoric, and Historic-period interpretation without becoming a proxy for cultural identity, ownership, site prediction, or restricted knowledge.

It is the landing page for result families such as climate, paleohydrology, vegetation, seasonality, drought cycles, predictive paleoenvironment layers, uncertainty outputs, and the metadata/provenance materials that make those outputs inspectable and governable.

| Truth posture | How to read this README |
| --- | --- |
| **CONFIRMED** | Purpose, environmental-only framing, FAIR+CARE posture, trust-visible release expectations, and the major paleoenvironment family names are grounded in the attached KFM source corpus. |
| **INFERRED** | Exact sibling links, some child-directory shapes, and some artifact placement details are conservative completions based on repeated attached project drafts. |
| **NEEDS VERIFICATION** | Mounted repo presence, actual file timestamps, exact doc UUID, local schema paths, CI command names, and whether every sibling README already exists. |

[Back to top](#kansas-frontier-matrix--paleoenvironmental-results)

## Repo fit

**Path:** `docs/analyses/archaeology/results/paleoenvironment/README.md`

**Role in the repo:** root index for archaeology-related paleoenvironment result families and their release-facing metadata, uncertainty, and provenance companions.

**Upstream links (INFERRED):** [Archaeology results root](../README.md)

**Downstream links (source-grounded family set; repo presence NEEDS VERIFICATION):**  
[Climate](./climate/README.md) · [Paleohydrology](./paleohydrology/README.md) · [Vegetation](./vegetation/README.md) · [Seasonality](./seasonality/README.md) · [Drought cycles](./drought-cycles/README.md) · [Predictive](./predictive/README.md) · [Uncertainty](./uncertainty/README.md)

This README should stay concise and navigational. Detailed method notes, family-specific prohibitions, and family-specific artifact rules belong in child READMEs.

[Back to top](#kansas-frontier-matrix--paleoenvironmental-results)

## Accepted inputs

The following belong here or immediately beneath this directory:

- Generalized paleoenvironment result families.
- Paleo-climate, paleo-hydrology, vegetation, seasonality, and drought-cycle outputs.
- Environmental-only predictive paleoenvironment layers.
- Uncertainty rasters, disagreement summaries, and fit/variance reports.
- STAC item sets and asset listings for released result layers.
- DCAT or JSON-LD discovery metadata for outward dataset description.
- PROV-O lineage bundles documenting reconstruction and transformation history.
- Family-level README files that define scope, limits, review expectations, and release posture.

## Exclusions

The following do **not** belong here:

- Raw proxy captures, unreviewed sample locations, or precision source extracts.
- Exact archaeological site coordinates, sensitive Indigenous knowledge, or restricted cultural materials.
- Cultural identity inference, migration reconstruction, or deterministic settlement claims.
- Unreleased candidate outputs that have not passed metadata, uncertainty, and policy review.
- Canonical source-onboarding contracts and raw ingest artifacts when they are acting as source-edge truth objects rather than result-pack companions.
- UI-only story copy with no evidence linkage.

Use the corresponding source/onboarding, working/quarantine, steward-only, or adjacent cultural-landscape analysis lanes instead of forcing those materials into this directory.

[Back to top](#kansas-frontier-matrix--paleoenvironmental-results)

## Directory tree

Source-grounded family names are shown below. Exact local presence remains **NEEDS VERIFICATION**.

```text
docs/analyses/archaeology/results/paleoenvironment/
├── README.md
├── climate/
├── paleohydrology/
├── vegetation/
├── seasonality/
├── drought-cycles/
├── predictive/
├── uncertainty/
├── stac/
├── metadata/
└── provenance/
```

[Back to top](#kansas-frontier-matrix--paleoenvironmental-results)

## Quickstart

Use this when reviewing or adding a paleoenvironment result family.

1. Confirm the family is **environmental-only**, generalized, and uncertainty-bearing.
2. Verify the family has a child README or equivalent scope note.
3. Ship the result with its metadata and lineage companions together.
4. Check that public-facing language stays contextual and does not drift into cultural certainty.
5. Do not publish anything here unless the release scope, evidence linkage, and correction path are visible.

```bash
# Illustrative only — verify actual repo paths and commands first.
cd docs/analyses/archaeology/results/paleoenvironment

# Review the family set before adding or renaming anything.
ls

# Add a new family skeleton only after verifying local conventions.
mkdir -p <family>/{stac,metadata,provenance,uncertainty}
touch <family>/README.md
```

```yaml
# Illustrative result-pack shape — not a confirmed mounted schema.
family: vegetation
result_scope: generalized
time_model: owl-time
spatial_generalization: h3-r7-plus
artifacts:
  uncertainty: true
  stac: true
  dcat: true
  prov: true
release_state: candidate
policy_review: required
```

[Back to top](#kansas-frontier-matrix--paleoenvironmental-results)

## Usage

Use this README as the **first stop** for archaeology-facing paleoenvironment material.

1. Start here to determine which family holds the environmental context you need.
2. Move into the relevant child README for family-specific structure and prohibitions.
3. Follow the linked metadata and provenance materials before using a layer in Story, Dossier, Export, or Focus.
4. Keep this page synchronized with family additions, removals, or naming changes.
5. Preserve the distinction between:
   - environmental context,
   - modeled output,
   - uncertainty expression, and
   - any higher-level archaeological interpretation that happens elsewhere.

> [!TIP]
> A good root README here reduces duplication: it should explain **where to go next**, **what belongs here**, and **what must never be implied from these layers**.

[Back to top](#kansas-frontier-matrix--paleoenvironmental-results)

## Diagram

```mermaid
flowchart LR
    A[Proxy records & environmental inputs] --> B[Reconstruction / modeling workflows]
    B --> C[Generalized paleoenvironment result layers]
    B --> D[Uncertainty layers]
    C --> E[STAC items]
    C --> F[DCAT metadata]
    B --> G[PROV-O lineage]
    D --> E
    D --> G
    E --> H[Governed release scope]
    F --> H
    G --> H
    H --> I[Map Explorer]
    H --> J[Story surface]
    H --> K[Evidence Drawer]
    H --> L[Focus Mode]
    H --> M[Export]

    N[No exact-site disclosure] -. governance .-> H
    O[No cultural attribution] -. governance .-> H
    P[Visible uncertainty] -. governance .-> H
```

[Back to top](#kansas-frontier-matrix--paleoenvironmental-results)

## Tables

### Result family registry

| Family | What belongs here | Typical contents | Interpretation boundary |
| --- | --- | --- | --- |
| `climate/` | Generalized paleoclimate reconstructions | temperature, precipitation, seasonality, drought/flood intervals, proxy composites | Environmental-only; no cultural timeline claims |
| `paleohydrology/` | Paleo-hydrology and moisture-balance context | paleochannels, alluvial generalizations, moisture balance, hydrology summaries | No exact-site prediction from river or water context alone |
| `vegetation/` | Paleovegetation and ecozone reconstructions | ecozones, biomass envelopes, canopy/groundcover, proxy assemblages | No habitat-to-group attribution |
| `seasonality/` | Seasonal climate reconstructions | winter/summer patterns, seasonal precipitation, temporal uncertainty | Use as temporal context, not behavioral certainty |
| `drought-cycles/` | Generalized drought/wet oscillation summaries | recurrence, severity, duration, clustering, proxy agreement | No deterministic historical explanation |
| `predictive/` | Environmental-only predictive paleoenvironment layers | paleoclimate, hydrology, vegetation, soils, temporal scenarios, predictive uncertainty | No cultural forecasting, identity inference, or fine-scale reconstruction |
| `uncertainty/` | Cross-family uncertainty outputs | disagreement, variance, interpolation confidence, ensemble spread | Must stay visible wherever consequential use occurs |
| `stac/` | Spatiotemporal release descriptors | item/asset references, extent, asset listings | Release-facing carrier, not a substitute for DCAT/PROV |
| `metadata/` | Dataset discovery and distribution records | purpose, scope, methods summary, FAIR+CARE statements | Discovery layer, not the whole evidence story |
| `provenance/` | Reconstruction and transformation lineage | proxy usage, activities, configuration lineage, masking/generalization history | Provenance must remain inspectable and role-safe |

### Contracts & metadata

| Artifact family | Minimum purpose here | Notes |
| --- | --- | --- |
| **STAC** | Carry spatiotemporal item/asset description for released layers | Best when the result is an asset-bearing spatiotemporal item |
| **DCAT / JSON-LD** | Describe outward dataset/distribution discovery | Should keep scope, method summary, distribution, and access posture legible |
| **PROV-O** | Preserve reconstruction, modeling, and masking lineage | Should remain linked to release-safe artifacts, not hidden behind prose |
| **Uncertainty companion** | Express disagreement, fit limits, spread, and ambiguity | Required for ethical and scientific use of derived outputs |
| **Evidence-linked release refs** | Support Evidence Drawer, Focus, and correction visibility | Do not imply that a pretty layer is self-authenticating |

### Trust-visible shell use

| Surface | How paleoenvironment results should appear | Must stay visible |
| --- | --- | --- |
| Map Explorer | Layered environmental context | time scope, freshness, uncertainty, route to evidence |
| Timeline | Time-bounded environmental change context | valid-time labels, compare basis, stale-state cues |
| Story surface | Human-authored narrative with evidence linkage | dates, perspective labels, correction/review state |
| Evidence Drawer | Immediate provenance inspection | lineage members, transforms, release scope, preview limits |
| Focus Mode | Bounded environmental context and synthesis | scoped retrieval, citation verification, answer/abstain/deny/error outcomes |
| Export | Policy-safe outward artifact generation | release scope, evidence linkage, correction linkage |

[Back to top](#kansas-frontier-matrix--paleoenvironmental-results)

## Task list

- [ ] Root README reflects the current family set without duplicating child-family method detail.
- [ ] Every released family has uncertainty material, not just a pretty output layer.
- [ ] STAC, DCAT, and PROV references are present where required.
- [ ] Environmental-only framing is explicit and stable.
- [ ] No exact-location leakage, identity inference, or cultural attribution is introduced.
- [ ] Story and Focus language remains contextual, bounded, and evidence-linked.
- [ ] Release state and correction path are visible for outward-facing artifacts.
- [ ] Naming seams have been checked against the mounted repo before merge.
- [ ] Metadata, provenance, and child links render correctly on GitHub.
- [ ] Any newly added family has a sibling README before publication.

### Definition of done

A change to this directory is ready when:

- the family is correctly placed,
- the README and child links are coherent,
- uncertainty is published alongside results,
- metadata and provenance are inspectable,
- public-safe interpretation boundaries are explicit, and
- the change does not quietly turn environmental context into cultural certainty.

[Back to top](#kansas-frontier-matrix--paleoenvironmental-results)

## FAQ

### Why is this under archaeology if the layers are environmental?

Because these datasets support archaeological interpretation with **environmental context**, but the datasets themselves remain environmental-only and governance-bounded.

### Can these layers be used in Focus Mode?

Yes, but only as scoped, evidence-linked environmental context with visible uncertainty and release state.

### Are predictive layers allowed here?

Yes, but only when they remain generalized, environmental-only, uncertainty-bearing, and free of cultural forecasting or identity linkage.

### Why are some links and names marked as inferred?

Because the current session did not expose a mounted repo tree. The attached project documents strongly imply these sibling families, but local file presence still needs repo verification.

### Is 3D required for these results?

No. KFM doctrine is 2D-first by default. Any 3D use must remain conditional, burden-bearing, and evidence-linked.

[Back to top](#kansas-frontier-matrix--paleoenvironmental-results)

## Appendix

<details>
<summary><strong>Inferred child-family starter shapes</strong></summary>

These are useful review targets, not confirmed mounted repo facts.

| Family | Likely child structure |
| --- | --- |
| `climate/` | `temperature/`, `precipitation/`, `seasonality/`, `drought-flood/`, `proxy-assemblages/`, `temporal/`, `uncertainty/`, `stac/`, `metadata/`, `provenance/` |
| `vegetation/` | `ecozones/`, `biomass/`, `canopy-groundcover/`, `proxy-assemblages/`, `temporal/`, `uncertainty/`, `stac/`, `metadata/`, `provenance/` |
| `drought-cycles/` | `frequency/`, `severity/`, `duration/`, plus uncertainty/metadata/provenance companions |
| `predictive/` | `climate/`, `hydrology/`, `vegetation/`, `soils/`, `drought-cycles/`, `temporal/`, `uncertainty/`, `stac/`, `metadata/`, `provenance/` |
| `provenance/` | lineage bundles, crosswalks, masking logs, reproducibility snapshots |

</details>

<details>
<summary><strong>Naming seam to verify before commit</strong></summary>

The attached drafts consistently use `paleohydrology/` at the root, while some predictive child drafts use `hydrology/` under `predictive/`. Keep that distinction unless the mounted repo has already standardized differently.

</details>

<details>
<summary><strong>Recommended maintainer rule</strong></summary>

Whenever a new family or child directory is added, update this root README in the same change so the landing page stays trustworthy.

</details>

[Back to top](#kansas-frontier-matrix--paleoenvironmental-results)

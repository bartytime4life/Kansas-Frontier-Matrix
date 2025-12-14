---
title: "🎯 KFM — Remote Sensing Validation Sampling (Deterministic Frames · Stratification · Governance)"
path: "docs/analyses/remote-sensing/validation/methods/sampling/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing Board · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Index + Reference"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

intent: "remote-sensing-validation-sampling"
audience:
  - "Remote Sensing Engineering"
  - "Science QA Reviewers"
  - "Data Engineering"
  - "Reliability Engineering"
  - "Governance Reviewers"

classification: "Public"
sensitivity: "General (non-sensitive) unless overridden by dataset labels"
sensitivity_level: "Low"
public_exposure_risk: "Low"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "Remote Sensing Board · FAIR+CARE Council"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:methods:sampling:index:v11.2.6"
semantic_document_id: "kfm-remote-sensing-validation-sampling"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/methods/sampling/README.md"
immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "metadata-extraction"
  - "diagram-extraction"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"
---

<div align="center">

# 🎯 **KFM — Remote Sensing Validation Sampling**
`docs/analyses/remote-sensing/validation/methods/sampling/README.md`

**Purpose**  
Define the governed sampling posture for KFM remote-sensing validation:
how to build **deterministic sample frames**, select samples reproducibly (seeds + stable ordering),
stratify without bias, and report results without governance leakage.

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Validation Sampling" src="https://img.shields.io/badge/Validation-Sampling-blue" />
<img alt="Status Active Enforced" src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

Sampling is used in validation when:

- full evaluation is too expensive (large rasters, dense time series),
- you need rapid feedback for NRT or daily runs,
- you need balanced coverage across conditions (e.g., land cover, season, cloud regime),
- you need stable, comparable metrics across releases.

Sampling is **not a loophole**: it must remain deterministic, auditable, and governance-safe.

This directory defines:

- sampling units and sample-frame construction,
- supported sampling modes (full, fixed-set, random, stratified, systematic),
- determinism requirements (seed, stable ordering, frame hashing, manifesting),
- FAIR+CARE and sovereignty rules for safe reporting.

Related references:

- Algorithms: `../algorithms/README.md`
- Metrics: `../metrics/README.md`
- Provenance: `../provenance/README.md`
- Reports: `../../reports/README.md`

---

## 🗂️ Directory Layout

~~~text
📁 docs/analyses/remote-sensing/validation/methods/
└── 📁 sampling/                                              — Sampling conventions (this directory)
    ├── 📄 README.md                                          — This reference (you are here)
    └── 📁 templates/                                         — Optional: sampling manifests and policy templates
~~~

> Keep templates small and normative. Store actual per-run sample manifests as governed artifacts and reference them via STAC/PROV.

---

## 🧱 Sampling units (what gets sampled)

Sampling begins by choosing the **sampling unit**. The unit MUST be explicit in every report and provenance bundle.

Common units:

- **STAC Item**: one acquisition/scene/granule per item
- **Tile**: fixed grid cell (e.g., WebMercator tiles, UTM tiles, H3 cells, internal tiling)
- **Pixel set**: a deterministic subset of pixels (only when masks and ordering are pinned)
- **Time step**: timestamps or windows (hourly/daily/weekly)
- **(Item × Tile)**: for tiled evaluation of items at scale

Rules:

- Prefer **Item** or **Tile** units for determinism and audibility.
- Pixel-level sampling MUST record mask policy + numeric policy + stable enumeration rules.

---

## 🧾 Sample frame (the candidate set)

A **sample frame** is the deterministic list of eligible candidate units.

The frame MUST be defined by:

- scope:
  - time window (UTC)
  - generalized spatial scope (region/coarse grid where required)
- eligibility filters (pinned):
  - QA masks (cloud/water/no-data)
  - product availability
  - governance eligibility (CARE/sovereignty gates)
- stable enumeration and ordering:
  - lexicographic by candidate id (or by `(time, id)` when time semantics matter)

The frame SHOULD be materialized as a governed artifact:

- `sample_frame_manifest.json` (candidate ids + counts + hashes)
- referenced from PROV and STAC as an asset (not embedded in docs)

---

## 🧩 Supported sampling modes (recommended)

### 1) Full coverage (`sampling = "full"`)

Use when:

- data volume is manageable,
- gates require full evaluation (e.g., promotion to public release),
- sensitive products require strict completeness checks.

Determinism:

- stable ordering still required
- results must include support counts (items/tiles/pixels)

### 2) Fixed set (`sampling = "fixed_set"`)

Evaluate a curated, stable set of items/tiles.

Use when:

- you want a stable “canary” set for release comparisons,
- you need consistent trend signals over time.

Rules:

- the fixed set must be versioned and governed
- changes to the set require review and version history notes

### 3) Random sampling (`sampling = "random"`)

Uniform random sample from the frame.

Use when:

- you need quick estimates of global performance,
- stratification is not required.

Determinism requirements:

- fixed PRNG
- pinned seed
- stable candidate ordering before selection
- record `frame_hash` and `selected_hash`

### 4) Stratified sampling (`sampling = "stratified"`)

Select samples by strata so that metrics aren’t dominated by common conditions.

Typical strata (examples):

- land cover / ecoregion class
- season/month
- sensor geometry bucket
- cloud fraction bucket
- QA tier (A/B/C)
- spatial region buckets (coarse H3 or admin regions)

Rules:

- strata definitions MUST be pinned and versioned
- per-stratum sample sizes MUST be deterministic
- minimum support per stratum MUST be reported (and may gate outcomes)

### 5) Systematic / space-filling sampling (`sampling = "systematic"`)

Deterministic coverage sampling such as:

- every Nth tile in stable ordering
- fixed coarse grid covering Kansas AOI
- low-discrepancy sequence over a stable frame

Use when:

- you want coverage without PRNG,
- you want stable spatial uniformity.

---

## 🎯 Determinism contract (non-negotiable)

Sampling MUST be reproducible:

- same inputs + same config + same seed → same sampled set
- sampled set must be derivable from:
  - pinned sampling config snapshot
  - sample frame manifest hash
  - seed (if PRNG used)

### Required fields (for every sampling run)

Sampling metadata MUST include:

- `sampling` mode: `full|fixed_set|random|stratified|systematic`
- `sampling_unit`: `item|tile|pixel_set|time_step|item_tile`
- `frame_hash_sha256` (hash of the ordered candidate list + scope)
- `seed` (required for PRNG sampling; forbidden for systematic-only unless used in deterministic seed derivation)
- `selected_count` and `candidate_count`
- `strata` summary when stratified (counts, sample sizes)

### Seed derivation (recommended)

If seeds must be derived deterministically per run:

- `seed = uint32(sha256(frame_hash + config_hash + algorithm_id)[0:8])`

Rules:

- do not derive seeds from wall-clock or host-specific values
- record both the derived seed and the inputs used to derive it (as hashes/refs)

### Sample manifest (recommended)

Sampling SHOULD emit a small manifest artifact referenced by STAC/PROV:

- contains selected ids (or references to selected partitions),
- contains the deterministic derivation fields above,
- can be re-generated and checked in CI.

---

## 🧾 Standard sampling metadata block (recommended)

Algorithm outputs SHOULD include a block like:

~~~json
{
  "sampling": {
    "mode": "stratified",
    "unit": "tile",
    "candidate_count": 12000,
    "selected_count": 600,
    "frame_hash_sha256": "<sha256>",
    "seed": 1337,
    "strategy_version": "v1",
    "strata": [
      {"key": "ecoregion=high_plains", "candidates": 3000, "selected": 150},
      {"key": "ecoregion=flint_hills", "candidates": 2000, "selected": 100}
    ]
  }
}
~~~

Notes:

- strata keys MUST not leak sensitive details (use generalized categories).
- detailed selected-id lists belong in a governed manifest artifact, not in public docs.

---

## 🛡️ FAIR+CARE and sovereignty rules

Sampling can leak sensitive information if it:

- samples tiny AOIs that imply locations,
- publishes per-sample lists for restricted collections,
- reports metrics at overly fine partitions.

Rules:

- public reporting MUST aggregate to safe scopes:
  - region or coarse grid only
  - minimum cluster size thresholds (policy-defined) before reporting
- when sovereignty restrictions apply:
  - sampling MUST exclude or gate restricted sources by policy
  - set `care_gate_status = redact|deny` when required
  - emit only aggregated support counts and outcomes (no per-sample lists)
- never embed:
  - raw coordinates
  - signed URLs
  - secrets or internal endpoints

---

## 🧪 CI/CD expectations (recommended)

Sampling-related checks SHOULD include:

- **reproducibility test**: regenerate selection from the same frame/config and verify `selected_hash` matches
- **support sanity**: fail/warn when support too low for valid inference (policy-defined)
- **strata completeness**: ensure required strata exist and have minimum support
- **governance scan**: ensure no restricted fields are embedded in sampling metadata
- **provenance presence**: sample manifest and config snapshot are referenced by PROV and/or OpenLineage

---

## 🗺️ High-level flow

~~~mermaid
flowchart TD
  A["Enumerate candidate units (deterministic ordering)"] --> B["Apply eligibility filters (pinned)"]
  B --> C["Build sample frame + frame_hash"]
  C --> D["Select sample (mode + seed + strata rules)"]
  D --> E["Write sample manifest (ids + hashes)"]
  E --> F["Run validation algorithms on selected set"]
  F --> G["Emit metrics + provenance + references"]
~~~

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed sampling reference for remote-sensing validation; defined sampling units, deterministic sample frames, supported modes, required metadata fields, governance-safe reporting rules, and CI reproducibility expectations. |

---

<div align="center">

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Validation Sampling" src="https://img.shields.io/badge/Validation-Sampling-blue" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

[⬅ Methods](../README.md) ·
[🧮 Algorithms](../algorithms/README.md) ·
[📐 Metrics](../metrics/README.md) ·
[🧾 Provenance](../provenance/README.md) ·
[🧾 Reports](../../reports/README.md) ·
[🏛️ Governance Charter](../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

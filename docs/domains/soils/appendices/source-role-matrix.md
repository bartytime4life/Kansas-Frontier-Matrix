<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION
title: Kansas Frontier Matrix — Soils — Source Role Matrix
type: standard
version: v1
status: draft
owners: [@bartytime4life, NEEDS VERIFICATION]
created: 2026-04-01
updated: 2026-04-01
policy_label: public
related: [
  "../README.md",
  "../sources/README.md",
  "../../../pipelines/ssurgo_to_catchment.md"
]
tags: [kfm, soils, appendix, source-role-matrix, provenance]
notes: [
  "Requested as part of the user-directed soils module build.",
  "Appendix page is PROPOSED and meant to keep source-role distinctions compact and reusable."
]
[/KFM_META_BLOCK_V2] -->

# Kansas Frontier Matrix — Soils — Source Role Matrix

Compact reference for keeping soil-source roles legible across the soils module.

| Source family | Authority class | Typical grain | Allowed downstream use | Must not be mistaken for |
|---|---|---|---|---|
| **SSURGO** | authoritative survey record | map unit / component / horizon | baseline soil truth, normalized extracts, evidence-linked derivation | statewide convenience grid |
| **SDA** | authoritative access/query surface | query result over source tables | reproducible extraction, acquisition automation, query lineage | independent sovereign dataset |
| **gSSURGO** | gridded derivative | raster cell | analytical stacking, statewide mapping, convenience summaries | raw survey structure |
| **gNATSGO** | broader gridded derivative | raster cell | continuity / broader-scale fallback use | local high-fidelity survey truth |
| **State / institutional portal** | discovery / service mirror | varies | discovery, retrieval, service exposure | authoritative origin |
| **KFM derived overlay** | subordinate derived product | reporting unit such as catchment/place/grid | map, story, API, dossier use with evidence and caution | authoritative survey replacement |

## Notes

- Keep this matrix synchronized with the lane README and sources child README.
- If live repo language standardizes different labels, update the matrix to match branch-local truth.
- Do not expand this appendix into a policy or schema page.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/published/layers/agriculture/crop-progress-county/2026q2-pmtiles/readme
title: data/published/layers/agriculture/crop_progress_county/2026Q2.pmtiles README
type: directory-readme
version: v0.1
status: draft
owners:
  - TODO(owner): data steward
  - TODO(owner): agriculture domain steward
  - TODO(owner): map-layer steward
  - TODO(owner): release steward
created: 2026-06-26
updated: 2026-06-26
policy_label: public-review
path: data/published/layers/agriculture/crop_progress_county/2026Q2.pmtiles/README.md
related:
  - ../README.md
  - ../../aggregate/README.md
  - ../../../../agriculture/README.md
  - ../../../../../../release/README.md
  - ../../../../../../contracts/README.md
  - ../../../../../../schemas/README.md
  - ../../../../../../policy/README.md
  - ../../../../../../docs/standards/PMTILES.md
notes:
  - "README for a proposed 2026Q2 PMTiles package directory under the county crop-progress Agriculture published layer lane. It replaces a placeholder file."
  - "This README does not prove that a PMTiles binary, manifest, checksum, validation report, or release record exists."
  - "PMTiles is treated as a derived release carrier, not as source evidence or release authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/published/layers/agriculture/crop_progress_county/2026Q2.pmtiles/`

> Instance-level README for the proposed **2026 Q2 county crop-progress Agriculture PMTiles package**.

![Status: draft](https://img.shields.io/badge/status-draft-orange)
![Lifecycle: PUBLISHED](https://img.shields.io/badge/lifecycle-PUBLISHED-2ea44f)
![Domain: agriculture](https://img.shields.io/badge/domain-agriculture-green)
![Layer: crop progress county](https://img.shields.io/badge/layer-crop--progress--county-blue)
![Carrier: PMTiles](https://img.shields.io/badge/carrier-PMTiles-blue)
![Release: 2026Q2](https://img.shields.io/badge/release-2026Q2-lightgrey)
![Authority: not release](https://img.shields.io/badge/authority-not--release-b91c1c)

> [!IMPORTANT]
> **Status:** `draft`  
> **Path:** `data/published/layers/agriculture/crop_progress_county/2026Q2.pmtiles/README.md`  
> **Truth posture:** CONFIRMED target path and parent county crop-progress layer README from current repo evidence / PROPOSED package layout and naming / NEEDS VERIFICATION for the actual `.pmtiles` file, release manifest, layer manifest, checksums, validation report, evidence refs, and governed map route.

> [!WARNING]
> This package directory is not release authority. A PMTiles package belongs here only after the release record, evidence support, validation, policy state, correction path, rollback support, and integrity references exist.

---

## 1. Scope

This directory is for one release-scoped PMTiles package for county crop-progress Agriculture layers.

Expected package family, once released:

- a PMTiles archive or pointer for the 2026 Q2 county crop-progress layer;
- a release-linked package manifest;
- checksum or digest records;
- layer metadata sidecars; and
- correction, supersession, withdrawal, or rollback references when applicable.

This directory should not contain source data, processed candidates, proof authority, receipt authority, policy logic, schemas, semantic contracts, release decisions, or unreviewed generated outputs.

[Back to top](#top)

---

## 2. Required release support

Before this package is treated as usable, verify:

- [ ] release authority exists under `release/`;
- [ ] evidence references resolve;
- [ ] validation passes or records finite outcomes;
- [ ] policy state allows this public map surface;
- [ ] county scope, crop scope, quarter, time period, and method are clear;
- [ ] PMTiles/profile metadata is present;
- [ ] integrity references bind the package to the release record;
- [ ] correction and rollback paths are recorded; and
- [ ] public clients load it only through governed interfaces or approved released-artifact paths.

[Back to top](#top)

---

## 3. Suggested package layout

```text
data/published/layers/agriculture/crop_progress_county/2026Q2.pmtiles/
├── README.md
├── agriculture.published.layer.crop_progress_county.2026Q2.<short_hash>.pmtiles
├── agriculture.published.layer.crop_progress_county.2026Q2.<short_hash>.manifest.json
├── agriculture.published.layer.crop_progress_county.2026Q2.<short_hash>.checksums.txt
└── retired/
```

This layout is PROPOSED until validated by contracts, schemas, fixtures, and release tooling.

[Back to top](#top)

---

## 4. Maintainer note

A PMTiles archive is a reusable public-facing carrier, not root truth and not release authority. Keep this package citable, release-linked, integrity-bound, correction-ready, and reversible. If release support is incomplete, keep the package upstream instead of treating this path as published output.

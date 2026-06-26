<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/published/layers/atmosphere/pm25-2026-pmtiles/readme
title: data/published/layers/atmosphere/pm25_2026.pmtiles README
type: directory-readme
version: v0.1
status: draft
owners:
  - TODO(owner): data steward
  - TODO(owner): atmosphere domain steward
  - TODO(owner): air-quality steward
  - TODO(owner): map-layer steward
  - TODO(owner): release steward
created: 2026-06-26
updated: 2026-06-26
policy_label: public-review
path: data/published/layers/atmosphere/pm25_2026.pmtiles/README.md
related:
  - ../README.md
  - ../pm25/README.md
  - ../../../atmosphere/README.md
  - ../../../../../release/README.md
  - ../../../../../contracts/README.md
  - ../../../../../schemas/README.md
  - ../../../../../policy/README.md
  - ../../../../../docs/domains/atmosphere/ARCHITECTURE.md
  - ../../../../../docs/domains/atmosphere/RELEASE_INDEX.md
  - ../../../../../docs/standards/PMTILES.md
notes:
  - "README for a proposed 2026 PMTiles package directory for Atmosphere PM2.5 layer carriers. It replaces an empty file."
  - "This README does not prove that a PMTiles binary, manifest, checksum, validation report, EvidenceBundle reference, or release record exists."
  - "PMTiles is treated as a derived release carrier, not as source evidence, proof authority, official AQI authority, medical guidance, regulatory authority, or release authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/published/layers/atmosphere/pm25_2026.pmtiles/`

> Instance-level README for the proposed **2026 Atmosphere PM2.5 PMTiles package**.

![Status: draft](https://img.shields.io/badge/status-draft-orange)
![Lifecycle: PUBLISHED](https://img.shields.io/badge/lifecycle-PUBLISHED-2ea44f)
![Domain: atmosphere](https://img.shields.io/badge/domain-atmosphere%2Fair-0aa)
![Layer: PM2.5](https://img.shields.io/badge/layer-PM2.5-blue)
![Carrier: PMTiles](https://img.shields.io/badge/carrier-PMTiles-blue)
![Release scope: 2026](https://img.shields.io/badge/release--scope-2026-lightgrey)
![Authority: not release](https://img.shields.io/badge/authority-not--release-b91c1c)

> [!IMPORTANT]
> **Status:** `draft`  
> **Path:** `data/published/layers/atmosphere/pm25_2026.pmtiles/README.md`  
> **Truth posture:** CONFIRMED target path, PM2.5 layer README, Atmosphere published README, and comparable Agriculture PMTiles package README from current repo evidence / PROPOSED package layout and naming / NEEDS VERIFICATION for the actual `.pmtiles` file, release manifest, layer manifest, checksums, validation report, EvidenceBundle references, PM2.5 method records, and governed map route.

> [!WARNING]
> This package directory is not release authority, source evidence, proof authority, official AQI authority, medical guidance, emergency guidance, regulatory determination, or raw observation storage. A PMTiles package belongs here only after release authority, EvidenceBundle support, validation, policy state, correction path, rollback support, and integrity references exist.

---

## 1. Scope

This directory is for one release-scoped PMTiles package for Atmosphere PM2.5 layer carriers.

Expected package family, once released:

- a PMTiles archive or pointer for a 2026 PM2.5 layer;
- a release-linked package manifest;
- checksum or digest records;
- layer metadata sidecars;
- source-role, pollutant-basis, averaging-period, method, time-scope, freshness/stale-state, caveat, and audience metadata; and
- correction, supersession, withdrawal, or rollback references when applicable.

This directory should not contain raw source captures, direct sensor feeds, direct forecast feeds, work candidates, quarantine holds, processed candidates, catalog authority, proof authority, receipt authority, policy logic, schemas, semantic contracts, source registries, release decisions, official AQI issuance, medical guidance, regulatory determinations, emergency instructions, or unreleased generated outputs.

[Back to top](#top)

---

## 2. Required release support

Before this package is treated as usable, verify:

- [ ] release authority exists under `release/`;
- [ ] EvidenceBundle references resolve;
- [ ] source roles, pollutant basis, observation or modeled method, averaging period, and time range are clear;
- [ ] validation passes or records finite outcomes;
- [ ] policy state allows this public map surface;
- [ ] time scope, freshness/stale-state posture, caveats, audience, and official-authority boundary are clear;
- [ ] PMTiles/profile metadata is present;
- [ ] integrity references bind the package to the release record;
- [ ] correction and rollback paths are recorded; and
- [ ] public clients load it only through governed interfaces or approved released-artifact paths.

[Back to top](#top)

---

## 3. Suggested package layout

```text
data/published/layers/atmosphere/pm25_2026.pmtiles/
├── README.md
├── atmosphere.published.layer.pm25.2026.<short_hash>.pmtiles
├── atmosphere.published.layer.pm25.2026.<short_hash>.manifest.json
├── atmosphere.published.layer.pm25.2026.<short_hash>.checksums.txt
└── retired/
```

This layout is PROPOSED until validated by contracts, schemas, fixtures, and release tooling.

[Back to top](#top)

---

## 4. Maintainer note

A PMTiles archive is a reusable public-facing carrier, not root truth, source evidence, release authority, official AQI authority, medical guidance, emergency guidance, regulatory determination, or raw observation storage. Keep this package citable, source-role-aware, pollutant-aware, averaging-period-aware, method-aware, time-aware, stale-state-aware, release-linked, integrity-bound, correction-ready, and reversible. If release support is incomplete, keep the package upstream instead of treating this path as published output.

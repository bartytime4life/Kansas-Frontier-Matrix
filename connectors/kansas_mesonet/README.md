<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-kansas-mesonet-underscore-readme
title: connectors/kansas_mesonet/ — Kansas Mesonet Compatibility Connector Lane
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Kansas source steward · Soil steward · Agriculture steward · Weather/atmosphere steward · Hydrology steward · Rights reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; compatibility-lane; noncanonical-path; station-sensor-source; rights-gated; no-publication
proposed_path: connectors/kansas_mesonet/README.md
truth_posture: CONFIRMED path exists / NONCANONICAL compatibility README / CANONICAL HOME NEEDS VERIFICATION
related:
  - ../README.md
  - ../kansas/README.md
  - ../kansas/mesonet/README.md
  - ../kansas-mesonet/README.md
  - ../../docs/sources/catalog/kansas/kansas-mesonet.md
  - ../../docs/sources/catalog/kansas/README.md
  - ../../docs/domains/soil/README.md
  - ../../docs/domains/agriculture/README.md
  - ../../docs/domains/weather-atmospheric/README.md
  - ../../docs/domains/hydrology/README.md
  - ../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../data/registry/sources/
  - ../../data/raw/soil/
  - ../../data/quarantine/soil/
  - ../../data/raw/weather-atmospheric/
  - ../../data/quarantine/weather-atmospheric/
  - ../../fixtures/
  - ../../schemas/contracts/v1/source/
  - ../../schemas/contracts/v1/sensors/
  - ../../policy/sensitivity/
  - ../../policy/rights/
  - ../../release/
tags: [kfm, connectors, kansas-mesonet, kansas, mesonet, compatibility, station-sensor, observed-source, station-health, source-admission, raw, quarantine, governance]
notes:
  - "This README fills a previously blank underscore top-level Kansas Mesonet connector path."
  - "The Kansas Mesonet source page corrected top-level Mesonet connector placement and says the adapter belongs under the canonical `connectors/kansas/` lane, specifically `connectors/kansas/kansas-mesonet/`."
  - "The existing `connectors/kansas-mesonet/` and `connectors/kansas/mesonet/` READMEs already document related compatibility/placement boundaries; this underscore path should not become a third authority root."
  - "Kansas Mesonet is in-situ observed point-station data with native temporal cadence preserved and station-health metadata required before downstream analytics."
  - "Operator consent and current source terms remain rights gates; unknown rights default to denial/hold before activation."
  - "Connector output may enter RAW or QUARANTINE handoff only; downstream validation, EvidenceBundle closure, station-health review, catalog/triplet projection, release review, publication, correction, and rollback remain outside this folder."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Kansas Mesonet Compatibility Connector Lane

> Compatibility README for the existing underscore top-level `connectors/kansas_mesonet/` path. This path is **not** the canonical connector home; Kansas Mesonet connector work belongs under the canonical `connectors/kansas/` source-family lane unless an ADR or migration decision says otherwise.

<p>
  <img alt="Status: compatibility" src="https://img.shields.io/badge/status-compatibility-yellow">
  <img alt="Canonicality: noncanonical path" src="https://img.shields.io/badge/canonicality-noncanonical__path-orange">
  <img alt="Source role: observed in-situ" src="https://img.shields.io/badge/source__role-observed__in--situ-blue">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Lifecycle: RAW or QUARANTINE only" src="https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE%20only-orange">
</p>

> [!IMPORTANT]
> **Status:** compatibility / noncanonical-path README · **Owner:** `OWNER_TBD`  
> **Path:** `connectors/kansas_mesonet/README.md`  
> **Truth posture:** `CONFIRMED` file exists · `NONCANONICAL` compatibility path · `NEEDS VERIFICATION` canonical implementation home  
> **Boundary:** source-admission compatibility only; no public current-conditions service, no advisory surface, no direct publication, no station observation to gridded/model collapse.

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Evidence ledger](#evidence-ledger) · [Lifecycle diagram](#lifecycle-diagram) · [Admission posture](#admission-posture) · [Anti-collapse rules](#anti-collapse-rules) · [Validation](#validation) · [Rollback](#rollback) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/kansas_mesonet/` is retained here only as a compatibility lane because the path already exists.

The Kansas Mesonet source profile says top-level Mesonet connector placement should not be treated as canonical. Governed connector work should converge under `connectors/kansas/`, with the exact child name still needing a placement decision.

This file may document the compatibility boundary, migration intent, and source-admission rules. It must not become the canonical connector home unless an ADR or migration decision explicitly authorizes that exception.

[Back to top ↑](#top)

---

## Repo fit

| Surface | Role | Status |
|---|---|---:|
| `connectors/kansas_mesonet/` | Existing underscore top-level compatibility path. | **CONFIRMED path / NONCANONICAL** |
| `connectors/kansas-mesonet/` | Existing hyphenated top-level compatibility path. | **CONFIRMED path / NONCANONICAL compatibility** |
| `connectors/kansas/mesonet/` | Short Kansas-family Mesonet sublane. | **CONFIRMED README path / PLACEMENT NEEDS VERIFICATION** |
| `connectors/kansas/kansas-mesonet/` | Source-page corrected home. | **PROPOSED / NEEDS VERIFICATION** |
| `connectors/kansas/` | Canonical Kansas connector-family lane. | **CONFIRMED** |
| `docs/sources/catalog/kansas/kansas-mesonet.md` | Human-facing Kansas Mesonet source product page. | **CONFIRMED** |
| `data/registry/sources/` | SourceDescriptor authority. | **Outside connector / NEEDS VERIFICATION for entries** |
| `data/raw/soil/` and weather/atmosphere raw lanes | Candidate RAW handoff targets. | **PROPOSED / NEEDS VERIFICATION** |
| `data/quarantine/soil/` and weather/atmosphere quarantine lanes | Candidate quarantine handoff targets. | **PROPOSED / NEEDS VERIFICATION** |
| `release/` | Release and publication controls. | **Out of scope for this compatibility lane** |

[Back to top ↑](#top)

---

## Accepted inputs

Accepted content for this noncanonical compatibility path:

- README-level migration and compatibility notes;
- links to the canonical Kansas source-family lane;
- notes that prevent this top-level path from becoming a parallel authority;
- temporary fixture or test notes only if they are explicitly migration-bound;
- station/sensor parser notes only if the implementation is intentionally retained here by ADR;
- quarantine criteria for unresolved rights, station identity, station-health, cadence, variable/depth identity, freshness, geometry, or source-shape issues.

New implementation code should prefer the canonical Kansas family lane unless an ADR says otherwise.

---

## Exclusions

This folder must not contain or imply authority over:

- canonical connector-family status;
- public current-conditions or advisory services;
- published station observations or derived analytics;
- direct writes to `PROCESSED`, `CATALOG`, `TRIPLET`, `PUBLISHED`, proof, receipt, or release stores;
- SourceDescriptor authority records;
- policy or schema authority;
- generated summaries presented as authoritative station truth;
- source activation without operator consent, current source terms, station-health, cadence, variable/depth identity, and review checks.

Redirect implementation and source-family authority to the canonical `connectors/kansas/` lane once verified.

[Back to top ↑](#top)

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---:|---|---|
| `connectors/kansas_mesonet/README.md` | **CONFIRMED** | Target file exists and was blank before this update. | Does not prove implementation files, tests, or CI. |
| `connectors/kansas/README.md` | **CONFIRMED** | Kansas connector family is the canonical source-admission lane for Kansas source products. | Does not prove final Mesonet child naming. |
| `connectors/kansas/mesonet/README.md` | **CONFIRMED** | Short Kansas-family Mesonet sublane exists and is placement-needs-verification. | Does not prove final canonical path. |
| `connectors/kansas-mesonet/README.md` | **CONFIRMED** | Existing hyphenated top-level path is compatibility-only. | Does not prove migration decision. |
| `docs/sources/catalog/kansas/kansas-mesonet.md` | **CONFIRMED** | Kansas Mesonet is in-situ observed point-station data; native cadence is preserved; station-health metadata must precede downstream analytics; operator consent is a rights gate; corrected home is under `connectors/kansas/`. | Does not prove current source terms, implementation, or final sublane name. |

---

## Lifecycle diagram

```mermaid
flowchart LR
  A[Kansas Mesonet station material] --> B[SourceDescriptor gate]
  B --> C{Admission decision}
  C -->|allowed with limits| D[RAW handoff]
  C -->|needs review| Q[QUARANTINE handoff]
  C -->|denied| X[No connector activation]
  D --> E[Station identity and cadence validation]
  Q --> E
  E --> F[Station-health review]
  F --> G[Rights and attribution review]
  G --> H[EvidenceBundle and policy review]
  H --> I[Catalog or triplet projection]
  I --> R[Release review]
  R --> P[Published public-safe artifact]
```

[Back to top ↑](#top)

---

## Admission posture

Expected behavior for Kansas Mesonet compatibility-path work:

- no live source access unless explicitly enabled and reviewed;
- no source fetch without an accepted SourceDescriptor and activation decision;
- no activation until operator consent/current source terms are resolved;
- no implicit publication from retrieved source material;
- no relabeling of station observations as gridded/model output;
- no silent merging with SMAP, SoilGrids, SSURGO, gNATSGO, or other soil/weather products;
- no loss of station ID, station location, variable, sensor depth, cadence, timestamp, source URI, license/rights, station-health, source role, review, or release-class metadata;
- unclear rights, source role, station identity, station health, cadence, variable/depth identity, freshness, or schema drift routes to quarantine or abstention.

---

## Anti-collapse rules

1. This underscore path is compatibility-only unless a governance decision says otherwise.
2. Kansas Mesonet is observed in-situ point-station data, not modeled raster data.
3. Mesonet data is not interchangeable with SMAP, SoilGrids, SSURGO, or gNATSGO.
4. Native cadence must be preserved; 5-minute, hourly, and daily values must not be silently collapsed.
5. Station-health metadata is a precondition before downstream analytics use the feed.
6. Operator consent/current source terms are activation gates, not courtesy notes.
7. Derived summaries, maps, tiles, joins, and AI explanations are downstream carriers, not sovereign truth.

---

## Validation

Compatibility-lane validation should check that:

- this path is not treated as canonical without ADR/migration evidence;
- source metadata is preserved;
- SourceDescriptor references are required for activation;
- operator consent/source-terms state is explicit before activation;
- station ID, station location, variable, depth, cadence, timestamp, source URI, rights, station-health, source role, review, and vintage fields are explicit where available;
- malformed or incomplete records fail closed;
- records with unclear rights, unresolved source role, unresolved station identity, missing station-health, or unresolved cadence/variable/depth identity route to quarantine;
- connector output is limited to RAW or QUARANTINE handoff;
- no connector run writes directly to processed, catalog, triplet, published, proof, receipt, or release stores.

Root-level validation, policy-as-code, EvidenceBundle closure, release review, public caveats, and rollback remain outside this compatibility lane.

[Back to top ↑](#top)

---

## Definition of done

This compatibility README is ready for first review when:

- [ ] Kansas Mesonet source page is linked and current enough for review.
- [ ] A placement decision resolves `connectors/kansas_mesonet/`, `connectors/kansas-mesonet/`, `connectors/kansas/mesonet/`, and `connectors/kansas/kansas-mesonet/`.
- [ ] SourceDescriptor home and Kansas Mesonet source ID are verified.
- [ ] Operator consent/current source terms are verified by source steward review.
- [ ] Live source access is disabled by default for connector code.
- [ ] Station identity, station-health, variable/depth identity, cadence, freshness, and anti-collapse checks are represented in tests.
- [ ] Connector output is limited to RAW or QUARANTINE handoff.
- [ ] No public current-conditions, advisory, or analytics claims are created by connector code.

---

## Rollback

Rollback is required if this README is used to justify canonical-family status, source activation, current-conditions/advisory claims, station-observation-to-grid collapse, silent cadence collapse, direct publication, or bypass of SourceDescriptor, operator consent, station-health, validation, review, release, or rollback gates.

Rollback target:

```text
commit prior to this update: SHA_TBD_AFTER_GIT_HISTORY_CHECK
```

Because the file was blank before this update, a safe rollback is to restore the blank placeholder or replace this document with a shorter redirect-only README until canonical placement is resolved.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm canonical Mesonet child path under `connectors/kansas/`. | **NEEDS VERIFICATION** | Directory Rules, ADR, migration note, or repo convention. |
| Confirm whether this underscore top-level path should remain. | **NEEDS VERIFICATION** | ADR or migration decision. |
| Confirm SourceDescriptor home and Kansas Mesonet source ID. | **NEEDS VERIFICATION** | Source registry entry and accepted schema. |
| Confirm operator consent/current terms. | **NEEDS VERIFICATION** | Rights review and SourceDescriptor rights block. |
| Confirm station-health contract and tests. | **NEEDS VERIFICATION** | Sensor schema, connector tests, and station-health fixtures. |
| Confirm cadence/freshness handling. | **NEEDS VERIFICATION** | Parser tests and validation report. |
| Confirm fixture strategy and CI wiring. | **NEEDS VERIFICATION** | Fixture registry, workflow files, and test logs. |

---

## Maintainer note

Do not build new authority here. This existing underscore path should either stay a clear compatibility pointer or be removed after migration. Implementation should converge under the canonical Kansas source-family lane unless an ADR says otherwise.

[Back to top ↑](#top)

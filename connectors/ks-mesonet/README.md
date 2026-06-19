<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-ks-mesonet-readme
title: connectors/ks-mesonet/ — Kansas Mesonet Short-Name Compatibility Connector Lane
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Kansas source steward · Weather-atmospheric steward · Soil steward · Agriculture steward · Hydrology steward · Rights reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; compatibility-lane; noncanonical-path; observed-sensor-source; operator-consent-gated; station-health-required; no-publication
proposed_path: connectors/ks-mesonet/README.md
truth_posture: CONFIRMED path exists / NONCANONICAL compatibility README / CANONICAL HOME CONFIRMED AS connectors/kansas/kansas-mesonet/ BY SOURCE PROFILE
related:
  - ../README.md
  - ../kansas/README.md
  - ../kansas/mesonet/README.md
  - ../kansas-mesonet/README.md
  - ../kansas_mesonet/README.md
  - ../../docs/sources/catalog/kansas/kansas-mesonet.md
  - ../../docs/domains/weather-atmospheric/README.md
  - ../../docs/domains/soil/README.md
  - ../../docs/domains/agriculture/README.md
  - ../../docs/domains/hydrology/README.md
  - ../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../data/registry/sources/
  - ../../fixtures/
  - ../../schemas/contracts/v1/source/
  - ../../schemas/contracts/v1/sensors/station_health.schema.json
  - ../../policy/sensitivity/
  - ../../policy/rights/
  - ../../release/
tags: [kfm, connectors, ks-mesonet, kansas-mesonet, mesonet, sensors, weather-atmospheric, soil, agriculture, hydrology, compatibility, observed-source, source-admission, station-health, operator-consent, raw, quarantine, governance]
notes:
  - "This README fills a previously blank top-level `ks-mesonet` connector path."
  - "The Kansas Mesonet source profile says top-level Mesonet connector placement is noncanonical and the adapter belongs under `connectors/kansas/kansas-mesonet/`."
  - "This shorthand `connectors/ks-mesonet/` path is therefore a compatibility lane, not a canonical connector root."
  - "Kansas Mesonet is an in-situ point-station observed source. Station health metadata must precede downstream analytics use."
  - "Operator consent and current terms remain rights gates; unknown rights default to deny or quarantine."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Kansas Mesonet Short-Name Compatibility Connector Lane

> Compatibility README for the existing top-level `connectors/ks-mesonet/` path. This path is **not** the canonical connector home; Kansas Mesonet work should converge under `connectors/kansas/kansas-mesonet/` unless a later ADR or migration decision says otherwise.

<p>
  <img alt="Status: compatibility" src="https://img.shields.io/badge/status-compatibility-yellow">
  <img alt="Canonicality: noncanonical path" src="https://img.shields.io/badge/canonicality-noncanonical__path-orange">
  <img alt="Canonical home: connectors/kansas/kansas-mesonet" src="https://img.shields.io/badge/canonical__home-connectors%2Fkansas%2Fkansas--mesonet-success">
  <img alt="Source role: observed" src="https://img.shields.io/badge/source__role-observed-blue">
  <img alt="Station health: required" src="https://img.shields.io/badge/station__health-required-orange">
</p>

> [!IMPORTANT]
> **Status:** compatibility / noncanonical-path README · **Owner:** `OWNER_TBD`  
> **Path:** `connectors/ks-mesonet/README.md`  
> **Truth posture:** `CONFIRMED` file exists · `NONCANONICAL` compatibility path · `CONFIRMED` source profile points canonical work to `connectors/kansas/kansas-mesonet/`  
> **Boundary:** source-admission compatibility only; no public current-conditions surface, no direct publication, no rights bypass.

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Evidence ledger](#evidence-ledger) · [Admission posture](#admission-posture) · [Anti-collapse rules](#anti-collapse-rules) · [Validation](#validation) · [Rollback](#rollback) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/ks-mesonet/` is retained here only as a shorthand compatibility lane because the path already exists.

The Kansas Mesonet source profile says the canonical adapter belongs under `connectors/kansas/kansas-mesonet/`, under the canonical `connectors/kansas/` family. New implementation should therefore use the canonical Kansas Mesonet lane unless an ADR or migration note explicitly keeps this shorthand path.

This path must not become a separate source-family root, public sensor service, station-health authority, schema root, source registry, release root, or publication surface.

[Back to top ↑](#top)

---

## Repo fit

| Surface | Role | Status |
|---|---|---:|
| `connectors/ks-mesonet/` | Existing shorthand top-level compatibility path. | **CONFIRMED path / NONCANONICAL** |
| `connectors/kansas/kansas-mesonet/` | Canonical Kansas Mesonet adapter home named by source profile. | **CONFIRMED by source profile / NEEDS VERIFICATION implementation depth** |
| `connectors/kansas/mesonet/` | Existing Kansas-lane Mesonet variant. | **CONFIRMED README path / PLACEMENT NEEDS VERIFICATION** |
| `connectors/kansas-mesonet/` | Existing top-level compatibility path. | **CONFIRMED README path / NONCANONICAL** |
| `connectors/kansas_mesonet/` | Existing alternate top-level compatibility path. | **CONFIRMED README path / NONCANONICAL** |
| `docs/sources/catalog/kansas/kansas-mesonet.md` | Kansas Mesonet source profile. | **CONFIRMED** |
| `data/registry/sources/` | SourceDescriptor authority. | **Outside connector / NEEDS VERIFICATION for entries** |
| `fixtures/` | Candidate fixture root. | **NEEDS VERIFICATION** |
| `policy/rights/` and `policy/sensitivity/` | Rights and sensitivity authority. | **Outside connector** |
| `release/` | Release and publication controls. | **Out of scope for this compatibility lane** |

[Back to top ↑](#top)

---

## Accepted inputs

Accepted content for this noncanonical compatibility path:

- README-level migration and compatibility notes;
- links to the canonical `connectors/kansas/kansas-mesonet/` path;
- notes that prevent this shorthand top-level path from becoming a parallel authority;
- temporary fixture or test notes only if explicitly migration-bound;
- adapter notes for Kansas Mesonet point-station metadata only if retained here by ADR or migration note;
- quarantine criteria for unresolved rights, operator consent, station identity, station health, geometry, cadence, variable identity, timestamp, endpoint/access method, or source-shape issues.

New implementation code should prefer `connectors/kansas/kansas-mesonet/` unless an ADR says otherwise.

---

## Exclusions

This folder must not contain or imply authority over:

- canonical connector-family status;
- public current-conditions or advisory publication;
- direct writes to processed, catalog, triplet, published, proof, receipt, or release stores;
- SourceDescriptor authority records;
- policy or schema authority;
- generated summaries presented as authoritative weather, soil, hydrology, or agriculture truth;
- source activation without SourceDescriptor, operator consent, rights, station-health, source-role, geometry, provenance, and review checks.

Redirect implementation and source-family authority to `connectors/kansas/kansas-mesonet/` once verified.

[Back to top ↑](#top)

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---:|---|---|
| `connectors/ks-mesonet/README.md` | **CONFIRMED** | Target file exists and was blank before this update. | Does not prove implementation files, tests, or CI. |
| `docs/sources/catalog/kansas/kansas-mesonet.md` | **CONFIRMED** | Source profile says top-level Mesonet placement was noncanonical and the adapter belongs under `connectors/kansas/kansas-mesonet/`; it also identifies Mesonet as observed point-station data with station-health and operator-consent gates. | Does not prove endpoint availability, activation, or implementation. |
| `connectors/kansas-mesonet/README.md` | **CONFIRMED** | Existing top-level Mesonet compatibility path. | Does not make top-level Mesonet paths canonical. |
| `connectors/kansas_mesonet/README.md` | **CONFIRMED** | Existing alternate top-level Mesonet compatibility path. | Does not make alternate top-level paths canonical. |
| `connectors/kansas/kansas-mesonet/` | **NEEDS VERIFICATION** | Named as canonical adapter home by source profile. | Actual files, code, fixtures, tests, and CI remain unverified here. |

---

## Admission posture

Expected behavior for Kansas Mesonet source-admission work:

- no live source access unless explicitly enabled and reviewed;
- no source fetch without an accepted SourceDescriptor, rights state, and activation decision;
- no implicit publication from retrieved station material;
- no conversion of point-station observations into gridded surfaces without downstream review;
- no collapse of Mesonet observations into modeled or survey sources;
- preserve source ID, source URI, station identity, variable identity, cadence, timestamp, geometry/uncertainty, station-health status, license/rights, review, and release-class metadata;
- unresolved rights, consent, station identity, variable identity, station health, geometry, endpoint, cadence, freshness, or schema drift routes to quarantine or abstention.

---

## Anti-collapse rules

The Kansas Mesonet lane must preserve the following controls:

1. `connectors/ks-mesonet/` is compatibility-only unless an ADR says otherwise.
2. Canonical Mesonet work belongs under `connectors/kansas/kansas-mesonet/`.
3. Mesonet observations are in-situ point-station observations, not modeled grid truth.
4. Native cadence, station identity, variable identity, geometry, and station-health metadata must remain explicit.
5. Operator consent/current terms are rights gates; unknown rights deny or quarantine admission.
6. Public release is a governed state transition, not a connector output.
7. Derived summaries, maps, tiles, joins, analyses, and AI explanations are downstream carriers, not sovereign truth.

---

## Validation

Compatibility-lane validation should check that:

- this path is not treated as canonical without ADR/migration evidence;
- SourceDescriptor and rights references are required for activation;
- station identity, variable identity, cadence, timestamp, geometry, and station-health metadata are explicit where available;
- observations are not silently converted into modeled grids;
- malformed or incomplete records fail closed;
- records with unresolved rights, consent, station identity, station health, variable identity, cadence, geometry, freshness, or access method route to quarantine;
- connector output is limited to RAW or QUARANTINE handoff;
- no connector run writes directly to processed, catalog, triplet, published, proof, receipt, or release stores.

Root-level validation, policy-as-code, EvidenceBundle closure, release review, public caveats, and rollback remain outside this compatibility lane.

[Back to top ↑](#top)

---

## Rollback

Rollback is required if this README is used to justify canonical-family status, direct publication, source activation, source-role collapse, rights/consent bypass, public advisory claims, or direct writes beyond RAW/QUARANTINE handoff.

Rollback target:

```text
commit prior to this update: SHA_TBD_AFTER_GIT_HISTORY_CHECK
```

Because the file was blank before this update, a safe rollback is to restore the blank placeholder or replace this document with a shorter redirect-only README until canonical placement is resolved.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm canonical `connectors/kansas/kansas-mesonet/` implementation files. | **NEEDS VERIFICATION** | Repo tree or mounted workspace. |
| Confirm whether this shorthand top-level path should remain. | **NEEDS VERIFICATION** | ADR or migration decision. |
| Confirm SourceDescriptor homes and station/variable identifiers. | **NEEDS VERIFICATION** | Source registry entries and accepted schemas. |
| Confirm current access method, cadence, terms, and operator consent record. | **NEEDS VERIFICATION** | Source steward review and current source documentation. |
| Confirm station-health schema and validation coverage. | **NEEDS VERIFICATION** | Schema, code, fixtures, and tests. |
| Confirm rights handling. | **NEEDS VERIFICATION** | Rights review, policy references, and tests. |
| Confirm fixture strategy and CI wiring. | **NEEDS VERIFICATION** | Fixture registry, workflow files, and test logs. |

---

## Maintainer note

Do not build new authority here. This existing shorthand path should either stay a clear compatibility pointer or be removed after migration. Implementation should converge under `connectors/kansas/kansas-mesonet/` unless an ADR says otherwise.

[Back to top ↑](#top)

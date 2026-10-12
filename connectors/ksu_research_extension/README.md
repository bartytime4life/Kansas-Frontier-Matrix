<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-ksu-research-extension-readme
title: connectors/ksu_research_extension/ — KSU Research and Extension Compatibility Connector Lane
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Kansas source steward · Agriculture steward · Weather steward · Soil steward · Rights reviewer · Sensitivity reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; compatibility-lane; noncanonical-path; snake-case-compatibility; umbrella-source; rights-gated; sensitivity-gated; no-publication
proposed_path: connectors/ksu_research_extension/README.md
truth_posture: CONFIRMED path exists / NONCANONICAL compatibility README / CANONICAL HOME CONFIRMED AS connectors/kansas/ksu-research-extension/ BY SOURCE PROFILE
related:
  - ../README.md
  - ../kansas/README.md
  - ../../docs/sources/catalog/kansas/ksu-research-extension.md
  - ../../docs/sources/catalog/kansas/kansas-mesonet.md
  - ../../docs/domains/agriculture/README.md
  - ../../docs/domains/weather-atmospheric/README.md
  - ../../docs/domains/soil/README.md
  - ../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../data/registry/sources/
  - ../../fixtures/
  - ../../schemas/contracts/v1/source/
  - ../../policy/sensitivity/
  - ../../policy/rights/
  - ../../release/
tags: [kfm, connectors, ksu, k-state, research-extension, agriculture, weather, soil, mesonet, compatibility, source-admission, raw, quarantine, governance]
notes:
  - "This README replaces the greenfield stub in the top-level snake_case KSU Research and Extension connector path."
  - "The KSU R&E source profile says v0.2 normalizes the connector slug to `connectors/kansas/ksu-research-extension/`."
  - "This top-level `connectors/ksu_research_extension/` path is compatibility-only, not a canonical connector root."
  - "KSU R&E is an umbrella source-family brief; Kansas Mesonet is a sibling per-surface product page."
  - "Connector output may enter RAW or QUARANTINE handoff only; validation, EvidenceBundle closure, rights/sensitivity review, catalog/triplet projection, release review, publication, correction, and rollback remain outside this folder."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KSU Research and Extension Compatibility Connector Lane

> Compatibility README for the existing top-level `connectors/ksu_research_extension/` path. This path preserves the older snake_case connector spelling but is **not** the canonical connector home; KSU Research and Extension work should converge under `connectors/kansas/ksu-research-extension/` unless a later ADR or migration decision says otherwise.

<p>
  <img alt="Status: compatibility" src="https://img.shields.io/badge/status-compatibility-yellow">
  <img alt="Canonicality: noncanonical path" src="https://img.shields.io/badge/canonicality-noncanonical__path-orange">
  <img alt="Canonical home: connectors/kansas/ksu-research-extension" src="https://img.shields.io/badge/canonical__home-connectors%2Fkansas%2Fksu--research--extension-success">
  <img alt="Source family: umbrella" src="https://img.shields.io/badge/source__family-umbrella-blue">
  <img alt="Lifecycle: RAW or QUARANTINE only" src="https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE%20only-orange">
</p>

> [!IMPORTANT]
> **Status:** compatibility / noncanonical-path README · **Owner:** `OWNER_TBD`  
> **Path:** `connectors/ksu_research_extension/README.md`  
> **Truth posture:** `CONFIRMED` file exists · `NONCANONICAL` compatibility path · `CONFIRMED` source profile points canonical work to `connectors/kansas/ksu-research-extension/`  
> **Boundary:** source-admission compatibility only; no direct publication, no source activation, no rights/sensitivity bypass.

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Evidence ledger](#evidence-ledger) · [Admission posture](#admission-posture) · [Anti-collapse rules](#anti-collapse-rules) · [Validation](#validation) · [Rollback](#rollback) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/ksu_research_extension/` is retained here only as a compatibility lane because the top-level snake_case path already exists.

The KSU Research and Extension source profile says the v0.1 connector family placement was already correct under `connectors/kansas/`, and v0.2 normalizes the slug to `connectors/kansas/ksu-research-extension/`. New implementation should therefore use the canonical Kansas/KSU R&E lane unless an ADR or migration note explicitly keeps this top-level path.

This path must not become a separate Kansas source-family root, schema root, source registry, release root, proof root, fixture dump, live harvester, public API, or publication surface.

[Back to top ↑](#top)

---

## Repo fit

| Surface | Role | Status |
|---|---|---:|
| `connectors/ksu_research_extension/` | Existing top-level snake_case compatibility path. | **CONFIRMED path / NONCANONICAL** |
| `connectors/kansas/ksu-research-extension/` | Canonical KSU R&E adapter home named by source profile. | **CONFIRMED by source profile / NEEDS VERIFICATION implementation depth** |
| `connectors/kansas/` | Canonical Kansas connector-family lane. | **CONFIRMED** |
| `docs/sources/catalog/kansas/ksu-research-extension.md` | KSU R&E umbrella source profile. | **CONFIRMED** |
| `docs/sources/catalog/kansas/kansas-mesonet.md` | Kansas Mesonet sibling per-surface product page. | **CONFIRMED** |
| `data/registry/sources/` | SourceDescriptor authority. | **Outside connector / NEEDS VERIFICATION for entries** |
| `fixtures/` | Candidate fixture root. | **NEEDS VERIFICATION** |
| `policy/rights/` and `policy/sensitivity/` | Rights and sensitivity authority. | **Outside connector** |
| `release/` | Release and publication controls. | **Out of scope for this compatibility lane** |

[Back to top ↑](#top)

---

## Accepted inputs

Accepted content for this noncanonical compatibility path:

- README-level migration and compatibility notes;
- links to the canonical `connectors/kansas/ksu-research-extension/` path;
- notes that prevent this top-level snake_case path from becoming a parallel authority;
- temporary fixture or test notes only if explicitly migration-bound;
- adapter notes for KSU R&E source metadata only if retained here by ADR or migration note;
- quarantine criteria for unresolved rights, source role, product identity, cadence, source vintage, endpoint/access method, or source-shape issues.

New implementation code should prefer `connectors/kansas/ksu-research-extension/` unless an ADR says otherwise.

---

## Exclusions

This folder must not contain or imply authority over:

- canonical connector-family status;
- public release decisions;
- direct writes to processed, catalog, triplet, published, proof, receipt, or release stores;
- SourceDescriptor authority records;
- policy or schema authority;
- generated summaries presented as authoritative agriculture, weather, soil, or flora truth;
- source activation without SourceDescriptor, rights, sensitivity, source-role, provenance, and review checks.

Redirect implementation and source-family authority to `connectors/kansas/ksu-research-extension/` once verified.

[Back to top ↑](#top)

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---:|---|---|
| `connectors/ksu_research_extension/README.md` | **CONFIRMED** | Target file existed as a greenfield stub before this update. | Does not prove implementation files, tests, or CI. |
| `docs/sources/catalog/kansas/ksu-research-extension.md` | **CONFIRMED** | KSU R&E source profile says the canonical Kansas family placement was already correct and v0.2 normalizes the slug to `connectors/kansas/ksu-research-extension/`; it also frames KSU R&E as an umbrella source brief. | Does not prove endpoint availability, rights clearance, activation, or implementation. |
| `docs/sources/catalog/kansas/kansas-mesonet.md` | **CONFIRMED** | Kansas Mesonet is treated as a sibling per-surface product page with its own admission posture. | Does not replace the KSU R&E umbrella profile. |
| `connectors/kansas/ksu-research-extension/` | **NEEDS VERIFICATION** | Named as canonical adapter home by source profile. | Actual files, code, fixtures, tests, and CI remain unverified here. |

---

## Admission posture

Expected behavior for KSU R&E source-admission work routed through this compatibility path:

- no live source access unless explicitly enabled and reviewed;
- no source fetch without an accepted SourceDescriptor and activation decision;
- no implicit publication from retrieved source material;
- no elevation of KSU R&E into a C7-10 Kansas-First Domain Authority;
- no collapse of the KSU R&E umbrella with Kansas Mesonet or other per-surface product pages;
- preserve source ID, source URI, product identity, source role, cadence/freshness, date/vintage, license/rights, review state, and release-class metadata;
- unclear rights, source role, product identity, endpoint, freshness, or schema drift routes to quarantine or abstention.

---

## Anti-collapse rules

The KSU R&E compatibility lane must preserve the following controls:

1. `connectors/ksu_research_extension/` is compatibility-only unless an ADR says otherwise.
2. Canonical KSU R&E connector work belongs under `connectors/kansas/ksu-research-extension/`.
3. KSU R&E is an umbrella source-family brief; Kansas Mesonet is a sibling per-surface product page.
4. KSU R&E is not a C7-10 Kansas-First Domain Authority and must not be elevated by connector placement.
5. KSU R&E source products must be admitted per SourceDescriptor and source role.
6. Public release is a governed state transition, not a connector output.
7. Derived summaries, maps, tiles, joins, analyses, and AI explanations are downstream carriers, not sovereign truth.

---

## Validation

Compatibility-lane validation should check that:

- this path is not treated as canonical without ADR/migration evidence;
- SourceDescriptor references are required for activation;
- source role, product identity, cadence/freshness, and source vintage are explicit where available;
- KSU R&E is not silently elevated to C7-10 Kansas-First Domain Authority status;
- malformed or incomplete records fail closed;
- records with unresolved rights, sensitivity state, source role, product identity, freshness, or access method route to quarantine;
- connector output is limited to RAW or QUARANTINE handoff;
- no connector run writes directly to processed, catalog, triplet, published, proof, receipt, or release stores.

Root-level validation, policy-as-code, EvidenceBundle closure, release review, public caveats, and rollback remain outside this compatibility lane.

[Back to top ↑](#top)

---

## Rollback

Rollback is required if this README is used to justify canonical-family status, direct publication, source activation, source-role collapse, authority elevation, rights/sensitivity bypass, or direct writes beyond RAW/QUARANTINE handoff.

Rollback target:

```text
commit prior to this update: SHA_TBD_AFTER_GIT_HISTORY_CHECK
```

A safe rollback is to restore the prior greenfield stub or replace this document with a shorter redirect-only README until canonical placement is resolved.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm canonical `connectors/kansas/ksu-research-extension/` implementation files. | **NEEDS VERIFICATION** | Repo tree or mounted workspace. |
| Confirm whether this top-level snake_case path should remain. | **NEEDS VERIFICATION** | ADR or migration decision. |
| Confirm SourceDescriptor homes and KSU R&E product IDs. | **NEEDS VERIFICATION** | Source registry entries and accepted schemas. |
| Confirm current access methods, cadence, and terms. | **NEEDS VERIFICATION** | Source steward review and current source documentation. |
| Confirm rights and sensitivity handling. | **NEEDS VERIFICATION** | Rights review, sensitivity review, and policy references. |
| Confirm fixture strategy and CI wiring. | **NEEDS VERIFICATION** | Fixture registry, workflow files, and test logs. |

---

## Maintainer note

Do not build new authority here. This existing top-level snake_case path should either stay a clear compatibility pointer or be removed after migration. Implementation should converge under `connectors/kansas/ksu-research-extension/` unless an ADR says otherwise.

[Back to top ↑](#top)

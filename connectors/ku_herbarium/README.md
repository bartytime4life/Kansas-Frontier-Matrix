<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-ku-herbarium-readme
title: connectors/ku_herbarium/ — KU Herbarium Compatibility Connector Lane
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Kansas source steward · Flora steward · Biodiversity steward · Rights reviewer · Sensitivity reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; compatibility-lane; noncanonical-path; snake-case-compatibility; flora-source; specimen-source; rights-gated; sensitivity-gated; no-publication
proposed_path: connectors/ku_herbarium/README.md
truth_posture: CONFIRMED path exists / NONCANONICAL compatibility README / CANONICAL HOME CONFIRMED AS connectors/kansas/ku-herbarium/ BY SOURCE PROFILE
related:
  - ../README.md
  - ../kansas/README.md
  - ../kansas/ku-herbarium/README.md
  - ../kansas/kbs_herbarium/README.md
  - ../../docs/sources/catalog/kansas/ku-herbarium.md
  - ../../docs/sources/catalog/kansas/kbs.md
  - ../../docs/sources/catalog/kansas/ku-nhm.md
  - ../../docs/domains/flora/README.md
  - ../../docs/domains/fauna/README.md
  - ../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../data/registry/sources/
  - ../../fixtures/
  - ../../schemas/contracts/v1/source/
  - ../../policy/sensitivity/
  - ../../policy/rights/
  - ../../release/
tags: [kfm, connectors, ku-herbarium, ku, kanu, mcgregor-herbarium, flora, biodiversity, dwca, ipt, compatibility, source-admission, raw, quarantine, governance]
notes:
  - "This README fills a previously blank top-level `ku_herbarium` connector path."
  - "The KU Herbarium source profile says v0.1 used `connectors/ku_herbarium/` outside the canonical Kansas connector lane and v0.2 corrects to `connectors/kansas/ku-herbarium/`."
  - "This top-level `connectors/ku_herbarium/` path is therefore a snake_case compatibility lane, not a canonical connector root."
  - "KU McGregor Herbarium (KANU) is framed as a per-surface product page parented under the KBS umbrella."
  - "Connector output may enter RAW or QUARANTINE handoff only; downstream validation, EvidenceBundle closure, rights/sensitivity review, catalog/triplet projection, release review, publication, correction, and rollback remain outside this folder."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KU Herbarium Compatibility Connector Lane

> Compatibility README for the existing top-level `connectors/ku_herbarium/` path. This path preserves the older snake_case connector spelling but is **not** the canonical connector home; KU R. L. McGregor Herbarium / KANU work should converge under `connectors/kansas/ku-herbarium/` unless a later ADR or migration decision says otherwise.

<p>
  <img alt="Status: compatibility" src="https://img.shields.io/badge/status-compatibility-yellow">
  <img alt="Canonicality: noncanonical path" src="https://img.shields.io/badge/canonicality-noncanonical__path-orange">
  <img alt="Canonical home: connectors/kansas/ku-herbarium" src="https://img.shields.io/badge/canonical__home-connectors%2Fkansas%2Fku--herbarium-success">
  <img alt="Source role: observed specimen-backed" src="https://img.shields.io/badge/source__role-observed__specimen--backed-blue">
  <img alt="Lifecycle: RAW or QUARANTINE only" src="https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE%20only-orange">
</p>

> [!IMPORTANT]
> **Status:** compatibility / noncanonical-path README · **Owner:** `OWNER_TBD`  
> **Path:** `connectors/ku_herbarium/README.md`  
> **Truth posture:** `CONFIRMED` file exists · `NONCANONICAL` compatibility path · `CONFIRMED` source profile points canonical work to `connectors/kansas/ku-herbarium/`  
> **Boundary:** source-admission compatibility only; no direct publication, no source activation, no rights/sensitivity bypass.

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Evidence ledger](#evidence-ledger) · [Admission posture](#admission-posture) · [Anti-collapse rules](#anti-collapse-rules) · [Validation](#validation) · [Rollback](#rollback) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/ku_herbarium/` is retained here only as a compatibility lane because the top-level snake_case path already exists.

The KU Herbarium source profile says v0.1 used `connectors/ku_herbarium/` outside the canonical family lane, and v0.2 corrects the connector placement to `connectors/kansas/ku-herbarium/`. New implementation should therefore use the canonical Kansas/KU Herbarium lane unless an ADR or migration note explicitly keeps this top-level path.

This path must not become a separate Kansas source-family root, flora truth store, schema root, source registry, release root, proof root, fixture dump, live harvester, public API, or publication surface.

[Back to top ↑](#top)

---

## Repo fit

| Surface | Role | Status |
|---|---|---:|
| `connectors/ku_herbarium/` | Existing top-level snake_case compatibility path. | **CONFIRMED path / NONCANONICAL** |
| `connectors/kansas/ku-herbarium/` | Canonical KU Herbarium adapter home named by source profile. | **CONFIRMED by source profile / NEEDS VERIFICATION implementation depth** |
| `connectors/kansas/` | Canonical Kansas connector-family lane. | **CONFIRMED** |
| `docs/sources/catalog/kansas/ku-herbarium.md` | KU Herbarium per-surface source profile. | **CONFIRMED** |
| `docs/sources/catalog/kansas/kbs.md` | KBS umbrella source profile. | **CONFIRMED / parent umbrella** |
| `data/registry/sources/` | SourceDescriptor authority. | **Outside connector / NEEDS VERIFICATION for entries** |
| `fixtures/` | Candidate fixture root. | **NEEDS VERIFICATION** |
| `policy/rights/` and `policy/sensitivity/` | Rights and sensitivity authority. | **Outside connector** |
| `release/` | Release and publication controls. | **Out of scope for this compatibility lane** |

[Back to top ↑](#top)

---

## Accepted inputs

Accepted content for this noncanonical compatibility path:

- README-level migration and compatibility notes;
- links to the canonical `connectors/kansas/ku-herbarium/` path;
- notes that prevent this top-level snake_case path from becoming a parallel authority;
- temporary fixture or test notes only if explicitly migration-bound;
- adapter notes for KANU source metadata only if retained here by ADR or migration note;
- quarantine criteria for unresolved rights, sensitivity, source role, specimen identity, taxonomy, event date, locality precision, endpoint/access method, or source-shape issues.

New implementation code should prefer `connectors/kansas/ku-herbarium/` unless an ADR says otherwise.

---

## Exclusions

This folder must not contain or imply authority over:

- canonical connector-family status;
- public release decisions;
- direct writes to processed, catalog, triplet, published, proof, receipt, or release stores;
- SourceDescriptor authority records;
- policy or schema authority;
- generated summaries presented as authoritative flora or biodiversity truth;
- source activation without SourceDescriptor, rights, sensitivity, source-role, provenance, and review checks.

Redirect implementation and source-family authority to `connectors/kansas/ku-herbarium/` once verified.

[Back to top ↑](#top)

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---:|---|---|
| `connectors/ku_herbarium/README.md` | **CONFIRMED** | Target file existed and was blank before this update. | Does not prove implementation files, tests, or CI. |
| `docs/sources/catalog/kansas/ku-herbarium.md` | **CONFIRMED** | KU Herbarium source profile says v0.1 used top-level `connectors/ku_herbarium/` and v0.2 corrects to `connectors/kansas/ku-herbarium/`; it frames KANU as a per-surface product page under the KBS umbrella. | Does not prove endpoint availability, rights clearance, activation, or implementation. |
| `docs/sources/catalog/kansas/kbs.md` | **CONFIRMED** | Parent umbrella source context for KBS/KU herbarium surfaces. | Does not replace the KANU per-surface profile. |
| `connectors/kansas/ku-herbarium/` | **NEEDS VERIFICATION** | Named as canonical adapter home by source profile. | Actual files, code, fixtures, tests, and CI remain unverified here. |

---

## Admission posture

Expected behavior for KU Herbarium source-admission work routed through this compatibility path:

- no live source access unless explicitly enabled and reviewed;
- no source fetch without an accepted SourceDescriptor and activation decision;
- no implicit publication from retrieved source material;
- no collapse of the KANU per-surface product with the KBS umbrella, KU NHM, KBS NHI, iDigBio, GBIF, USDA PLANTS, or generated summaries;
- preserve source ID, source URI, specimen identity, source role, event date, taxonomy, geometry/uncertainty, date/vintage, license/rights, review state, and release-class metadata;
- unresolved rights, sensitivity, source role, specimen identity, taxonomy, locality precision, endpoint, freshness, or schema drift routes to quarantine or abstention.

---

## Anti-collapse rules

The KU Herbarium compatibility lane must preserve the following controls:

1. `connectors/ku_herbarium/` is compatibility-only unless an ADR says otherwise.
2. Canonical KU Herbarium connector work belongs under `connectors/kansas/ku-herbarium/`.
3. KANU is a per-surface product page parented under the KBS umbrella; the two layers must remain distinct.
4. KANU records are specimen-backed observations and must remain distinguishable from nomenclature anchors, aggregated portals, and generated summaries.
5. Flora source products must be admitted per SourceDescriptor and source role.
6. Public release is a governed state transition, not a connector output.
7. Derived summaries, maps, tiles, joins, analyses, and AI explanations are downstream carriers, not sovereign truth.

---

## Validation

Compatibility-lane validation should check that:

- this path is not treated as canonical without ADR/migration evidence;
- SourceDescriptor references are required for activation;
- source role, specimen identity, taxonomy, event date, geometry/uncertainty, rights, sensitivity, and source vintage are explicit where available;
- KANU per-surface material remains distinct from the KBS umbrella and peer flora/biodiversity authorities;
- malformed or incomplete records fail closed;
- records with unresolved rights, sensitivity state, source role, specimen identity, taxonomy, locality precision, freshness, or access method route to quarantine;
- connector output is limited to RAW or QUARANTINE handoff;
- no connector run writes directly to processed, catalog, triplet, published, proof, receipt, or release stores.

Root-level validation, policy-as-code, EvidenceBundle closure, release review, public caveats, and rollback remain outside this compatibility lane.

[Back to top ↑](#top)

---

## Rollback

Rollback is required if this README is used to justify canonical-family status, direct publication, source activation, source-role collapse, umbrella/surface collapse, rights/sensitivity bypass, or direct writes beyond RAW/QUARANTINE handoff.

Rollback target:

```text
commit prior to this update: SHA_TBD_AFTER_GIT_HISTORY_CHECK
```

Because the file was blank before this update, a safe rollback is to restore the blank placeholder or replace this document with a shorter redirect-only README until canonical placement is resolved.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm canonical `connectors/kansas/ku-herbarium/` implementation files. | **NEEDS VERIFICATION** | Repo tree or mounted workspace. |
| Confirm whether this top-level snake_case path should remain. | **NEEDS VERIFICATION** | ADR or migration decision. |
| Confirm SourceDescriptor homes and specimen identity fields. | **NEEDS VERIFICATION** | Source registry entries and accepted schemas. |
| Confirm current access methods, cadence, and terms. | **NEEDS VERIFICATION** | Source steward review and current source documentation. |
| Confirm rights and sensitivity handling. | **NEEDS VERIFICATION** | Rights review, sensitivity review, and policy references. |
| Confirm fixture strategy and CI wiring. | **NEEDS VERIFICATION** | Fixture registry, workflow files, and test logs. |

---

## Maintainer note

Do not build new authority here. This existing top-level snake_case path should either stay a clear compatibility pointer or be removed after migration. Implementation should converge under `connectors/kansas/ku-herbarium/` unless an ADR says otherwise.

[Back to top ↑](#top)

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-ksgs-readme
title: connectors/ksgs/ — KSGS Slug Compatibility Connector Lane
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Kansas source steward · Geology steward · Hydrology steward · Rights reviewer · Sensitivity reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; compatibility-lane; noncanonical-path; slug-compatibility; geology-source; hydrology-source; rights-gated; sensitivity-gated; no-publication
proposed_path: connectors/ksgs/README.md
truth_posture: CONFIRMED path exists / NONCANONICAL compatibility README / CANONICAL HOME CONFIRMED AS connectors/kansas/kgs/ BY SOURCE PROFILE
related:
  - ../README.md
  - ../kgs/README.md
  - ../kansas/README.md
  - ../kansas/kgs/README.md
  - ../../docs/sources/catalog/kansas/ksgs.md
  - ../../docs/sources/catalog/kansas/kcc-oil-gas-reg.md
  - ../../docs/sources/catalog/kansas/kdhe.md
  - ../../docs/domains/geology/README.md
  - ../../docs/domains/geology/SOURCES.md
  - ../../docs/domains/hydrology/README.md
  - ../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../control_plane/source_authority_register.yaml
  - ../../data/registry/sources/
  - ../../data/raw/geology/
  - ../../data/quarantine/geology/
  - ../../data/raw/hydrology/
  - ../../data/quarantine/hydrology/
  - ../../fixtures/
  - ../../schemas/contracts/v1/source/
  - ../../policy/sensitivity/
  - ../../policy/rights/
  - ../../release/
tags: [kfm, connectors, ksgs, kgs, kansas, geology, hydrology, oil-gas, wwc5, las, geoportal, compatibility, slug-compatibility, source-admission, raw, quarantine, governance]
notes:
  - "This README replaces the greenfield stub in the top-level `ksgs` connector path."
  - "The KGS source profile preserves the `ksgs.md` catalog slug but says canonical connector work belongs under `connectors/kansas/kgs/`."
  - "This top-level `connectors/ksgs/` path is therefore a slug-compatibility lane, not a new canonical authority root."
  - "The `ksgs` slug versus `kgs/` connector-path discrepancy is preserved by the source profile and deferred to OPEN-KSGS-13 or a later ADR/repo convention."
  - "Connector output may enter RAW or QUARANTINE handoff only; downstream validation, EvidenceBundle closure, rights/sensitivity review, catalog/triplet projection, release review, publication, correction, and rollback remain outside this folder."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KSGS Slug Compatibility Connector Lane

> Compatibility README for the existing top-level `connectors/ksgs/` path. This path follows the preserved `ksgs` catalog slug but is **not** the canonical connector home; KGS connector work belongs under `connectors/kansas/kgs/` unless a later ADR or migration decision says otherwise.

<p>
  <img alt="Status: compatibility" src="https://img.shields.io/badge/status-compatibility-yellow">
  <img alt="Canonicality: noncanonical path" src="https://img.shields.io/badge/canonicality-noncanonical__path-orange">
  <img alt="Canonical home: connectors/kansas/kgs" src="https://img.shields.io/badge/canonical__home-connectors%2Fkansas%2Fkgs-success">
  <img alt="Slug: ksgs preserved" src="https://img.shields.io/badge/slug-ksgs__preserved-blue">
  <img alt="Lifecycle: RAW or QUARANTINE only" src="https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE%20only-orange">
</p>

> [!IMPORTANT]
> **Status:** compatibility / noncanonical-path README · **Owner:** `OWNER_TBD`  
> **Path:** `connectors/ksgs/README.md`  
> **Truth posture:** `CONFIRMED` file exists · `NONCANONICAL` compatibility path · `CONFIRMED` source profile points canonical work to `connectors/kansas/kgs/`  
> **Boundary:** source-admission compatibility only; no new KGS authority root, no direct publication, no rights/sensitivity bypass.

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Evidence ledger](#evidence-ledger) · [Admission posture](#admission-posture) · [Anti-collapse rules](#anti-collapse-rules) · [Validation](#validation) · [Rollback](#rollback) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/ksgs/` is retained here only as a compatibility lane for the preserved `ksgs` slug.

The KGS source profile states that the human-facing source catalog file uses `docs/sources/catalog/kansas/ksgs.md`, while the connector path uses `connectors/kansas/kgs/`. The source profile preserves both names and defers final reconciliation to OPEN-KSGS-13 or a later ADR/repo convention.

This path must not become a separate KGS connector root, publisher authority, schema root, source registry, release root, proof root, fixture dump, or publication surface.

[Back to top ↑](#top)

---

## Repo fit

| Surface | Role | Status |
|---|---|---:|
| `connectors/ksgs/` | Existing top-level slug-compatibility path. | **CONFIRMED path / NONCANONICAL** |
| `connectors/kgs/` | Existing top-level KGS compatibility path. | **CONFIRMED README path / NONCANONICAL** |
| `connectors/kansas/kgs/` | Canonical KGS adapter home named by source profile. | **CONFIRMED by source profile / NEEDS VERIFICATION implementation depth** |
| `connectors/kansas/` | Canonical Kansas connector-family lane. | **CONFIRMED** |
| `docs/sources/catalog/kansas/ksgs.md` | Human-facing KGS source catalog entry using preserved slug. | **CONFIRMED** |
| `control_plane/source_authority_register.yaml` | Machine-readable source authority register. | **Referenced by source profile / NEEDS VERIFICATION current contents** |
| `data/registry/sources/` | SourceDescriptor authority. | **Outside connector / NEEDS VERIFICATION for entries** |
| `data/raw/geology/`, `data/raw/hydrology/` | Candidate RAW handoff targets. | **PROPOSED / NEEDS VERIFICATION** |
| `data/quarantine/geology/`, `data/quarantine/hydrology/` | Candidate quarantine handoff targets. | **PROPOSED / NEEDS VERIFICATION** |
| `policy/rights/` and `policy/sensitivity/` | Rights and sensitivity authority. | **Outside connector** |
| `release/` | Release and publication controls. | **Out of scope for this compatibility lane** |

[Back to top ↑](#top)

---

## Accepted inputs

Accepted content for this noncanonical compatibility path:

- README-level migration and compatibility notes;
- links to the canonical `connectors/kansas/kgs/` path;
- notes that prevent this top-level slug path from becoming a parallel authority;
- temporary fixture or test notes only if they are explicitly migration-bound;
- adapter notes for KGS source material only if retained here by ADR or migration note;
- quarantine criteria for unresolved rights, source role, sub-product identity, geometry, source vintage, endpoint/access method, or source-shape issues.

New implementation code should prefer `connectors/kansas/kgs/` unless an ADR says otherwise.

---

## Exclusions

This folder must not contain or imply authority over:

- canonical connector-family status;
- public release decisions;
- direct writes to processed, catalog, triplet, published, proof, receipt, or release stores;
- SourceDescriptor authority records;
- policy or schema authority;
- generated summaries presented as authoritative geology, hydrology, production, or well-record truth;
- source activation without SourceDescriptor, rights, sensitivity, source-role, geometry, provenance, and review checks.

Redirect implementation and source-family authority to `connectors/kansas/kgs/` once verified.

[Back to top ↑](#top)

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---:|---|---|
| `connectors/ksgs/README.md` | **CONFIRMED** | Target file existed as a greenfield stub before this update. | Does not prove implementation files, tests, or CI. |
| `docs/sources/catalog/kansas/ksgs.md` | **CONFIRMED** | KGS source profile preserves the `ksgs` catalog slug, confirms the connector path `connectors/kansas/kgs/`, and documents the slug discrepancy as OPEN-KSGS-13. | Does not prove current source terms, endpoint stability, activation, or implementation. |
| `connectors/kgs/README.md` | **CONFIRMED** | Existing top-level KGS compatibility path. | Does not make top-level KGS paths canonical. |
| `connectors/kansas/kgs/` | **NEEDS VERIFICATION** | Named as canonical adapter home by source profile. | Actual files, code, fixtures, tests, and CI remain unverified here. |

---

## Admission posture

Expected behavior for KGS source-admission work routed through this compatibility path:

- no live source access unless explicitly enabled and reviewed;
- no source fetch without an accepted SourceDescriptor and activation decision;
- no implicit publication from retrieved source material;
- no loss of source ID, source URI, sub-product identity, source role, geometry/uncertainty, date/vintage, license/rights, review, or release-class metadata;
- unclear rights, source role, sub-product identity, geometry, endpoint, freshness, or schema drift routes to quarantine or abstention.

---

## Anti-collapse rules

The KSGS slug compatibility lane must preserve the following controls:

1. `connectors/ksgs/` is compatibility-only unless an ADR says otherwise.
2. Canonical KGS work belongs under `connectors/kansas/kgs/`.
3. `ksgs.md` as a catalog slug and `kgs/` as a connector path remain distinct until OPEN-KSGS-13 is resolved.
4. KGS sub-products must be admitted per SourceDescriptor and source role.
5. KGS source material must not be collapsed into KCC regulatory records, KDHE environmental records, or generated summaries.
6. Public release is a governed state transition, not a connector output.
7. Derived summaries, maps, tiles, joins, analyses, and AI explanations are downstream carriers, not sovereign truth.

---

## Validation

Compatibility-lane validation should check that:

- this path is not treated as canonical without ADR/migration evidence;
- source metadata is preserved;
- SourceDescriptor references are required for activation;
- source role, sub-product identity, geometry, and source vintage are explicit where available;
- rights and sensitivity states are explicit before promotion-track use;
- malformed or incomplete records fail closed;
- records with unresolved rights, sensitivity state, source role, sub-product identity, geometry, vintage, or access method route to quarantine;
- connector output is limited to RAW or QUARANTINE handoff;
- no connector run writes directly to processed, catalog, triplet, published, proof, receipt, or release stores.

Root-level validation, policy-as-code, EvidenceBundle closure, release review, public caveats, and rollback remain outside this compatibility lane.

[Back to top ↑](#top)

---

## Rollback

Rollback is required if this README is used to justify canonical-family status, direct publication, source activation, source-role collapse, rights/sensitivity bypass, or direct writes beyond RAW/QUARANTINE handoff.

Rollback target:

```text
commit prior to this update: SHA_TBD_AFTER_GIT_HISTORY_CHECK
```

A safe rollback is to restore the prior greenfield stub or replace this document with a shorter redirect-only README until canonical placement is resolved.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm canonical `connectors/kansas/kgs/` implementation files. | **NEEDS VERIFICATION** | Repo tree or mounted workspace. |
| Confirm whether this `ksgs` top-level path should remain. | **NEEDS VERIFICATION** | ADR or migration decision. |
| Resolve or retain `ksgs.md` versus `kgs/` slug discrepancy. | **NEEDS VERIFICATION** | OPEN-KSGS-13, ADR, or repo convention. |
| Confirm SourceDescriptor homes and KGS sub-product IDs. | **NEEDS VERIFICATION** | Source registry entries and accepted schemas. |
| Confirm current access methods, cadence, and terms. | **NEEDS VERIFICATION** | Source steward review and current source documentation. |
| Confirm rights and sensitivity handling. | **NEEDS VERIFICATION** | Rights review, sensitivity review, and policy references. |
| Confirm fixture strategy and CI wiring. | **NEEDS VERIFICATION** | Fixture registry, workflow files, and test logs. |

---

## Maintainer note

Do not build new authority here. This path exists because the `ksgs` slug exists in the source catalog, but implementation should converge under `connectors/kansas/kgs/` unless an ADR says otherwise.

[Back to top ↑](#top)

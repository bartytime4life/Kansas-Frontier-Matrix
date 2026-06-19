<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-kgs-las-readme
title: connectors/kgs_las/ — KGS LAS Compatibility Connector Lane
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Kansas source steward · Geology steward · Hydrology steward · Rights reviewer · Sensitivity reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; compatibility-lane; noncanonical-path; digital-well-log-source; rights-gated; sensitivity-gated; no-publication
proposed_path: connectors/kgs_las/README.md
truth_posture: CONFIRMED path exists / NONCANONICAL compatibility README / CANONICAL HOME CONFIRMED AS connectors/kansas/kgs/ BY SOURCE PROFILE
related:
  - ../README.md
  - ../kgs/README.md
  - ../kansas/README.md
  - ../kansas/kgs/README.md
  - ../../docs/sources/catalog/kansas/ksgs.md
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
tags: [kfm, connectors, kgs, ksgs, las, well-logs, well-tops, geology, hydrology, kansas, compatibility, source-admission, raw, quarantine, governance]
notes:
  - "This README fills a previously blank top-level KGS LAS connector path."
  - "The KGS source profile says canonical KGS connector work belongs under `connectors/kansas/kgs/` and identifies KGS LAS digital well logs and well tops as a KGS source-family row."
  - "This top-level `connectors/kgs_las/` path is therefore a compatibility sublane, not a new canonical authority root."
  - "LAS well-log and well-top source material must preserve well identity, log identity, curve/top identity, depth datum/unit context, source vintage, source role, and rights/sensitivity state."
  - "Connector output may enter RAW or QUARANTINE handoff only; downstream validation, EvidenceBundle closure, rights/sensitivity review, catalog/triplet projection, release review, publication, correction, and rollback remain outside this folder."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KGS LAS Compatibility Connector Lane

> Compatibility README for the existing top-level `connectors/kgs_las/` path. This path is **not** the canonical connector home; KGS LAS digital well-log and well-top work should converge under the canonical KGS connector lane, `connectors/kansas/kgs/`, unless a later ADR or migration decision says otherwise.

<p>
  <img alt="Status: compatibility" src="https://img.shields.io/badge/status-compatibility-yellow">
  <img alt="Canonicality: noncanonical path" src="https://img.shields.io/badge/canonicality-noncanonical__path-orange">
  <img alt="Canonical home: connectors/kansas/kgs" src="https://img.shields.io/badge/canonical__home-connectors%2Fkansas%2Fkgs-success">
  <img alt="Subject: LAS well logs" src="https://img.shields.io/badge/subject-LAS__well__logs-blue">
  <img alt="Lifecycle: RAW or QUARANTINE only" src="https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE%20only-orange">
</p>

> [!IMPORTANT]
> **Status:** compatibility / noncanonical-path README · **Owner:** `OWNER_TBD`  
> **Path:** `connectors/kgs_las/README.md`  
> **Truth posture:** `CONFIRMED` file exists · `NONCANONICAL` compatibility path · `CONFIRMED` KGS source profile points canonical KGS work to `connectors/kansas/kgs/`  
> **Boundary:** source-admission compatibility only; no operational drilling, engineering, reservoir, public well-log, or direct publication use.

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Evidence ledger](#evidence-ledger) · [Lifecycle diagram](#lifecycle-diagram) · [Admission posture](#admission-posture) · [Anti-collapse rules](#anti-collapse-rules) · [Validation](#validation) · [Rollback](#rollback) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/kgs_las/` is retained here only as a compatibility sublane because the path already exists.

The KGS source profile names KGS LAS digital well logs and well tops as a KGS source-family row and says the canonical KGS connector home was already `connectors/kansas/kgs/`, under the canonical `connectors/kansas/` family. LAS-specific implementation should therefore converge under the canonical KGS connector lane unless a later ADR or migration note explicitly keeps this sublane.

This path must not become a separate KGS authority root, well-log truth store, schema root, source registry, release root, or publication surface.

[Back to top ↑](#top)

---

## Repo fit

| Surface | Role | Status |
|---|---|---:|
| `connectors/kgs_las/` | Existing top-level LAS compatibility path. | **CONFIRMED path / NONCANONICAL** |
| `connectors/kgs/` | Existing top-level KGS compatibility path. | **CONFIRMED README path / NONCANONICAL** |
| `connectors/kansas/kgs/` | Canonical KGS adapter home named by source profile. | **CONFIRMED by source profile / NEEDS VERIFICATION implementation depth** |
| `connectors/kansas/` | Canonical Kansas connector-family lane. | **CONFIRMED** |
| `docs/sources/catalog/kansas/ksgs.md` | Human-facing KGS source catalog entry. | **CONFIRMED** |
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
- notes that prevent this top-level path from becoming a parallel authority;
- temporary fixture or test notes only if they are explicitly migration-bound;
- adapter notes for LAS digital well-log and well-top metadata only if retained here by ADR or migration note;
- quarantine criteria for unresolved rights, source role, well identity, log identity, curve/top identity, depth datum/unit context, geometry, source vintage, endpoint/access method, or source-shape issues.

New implementation code should prefer `connectors/kansas/kgs/` unless an ADR says otherwise.

---

## Exclusions

This folder must not contain or imply authority over:

- canonical connector-family status;
- public release decisions;
- operational drilling, reservoir, engineering, safety, or field-use decisions;
- direct writes to `PROCESSED`, `CATALOG`, `TRIPLET`, `PUBLISHED`, proof, receipt, or release stores;
- SourceDescriptor authority records;
- policy or schema authority;
- generated summaries presented as authoritative well-log, reservoir, hydrology, or geology truth;
- source activation without SourceDescriptor, rights, sensitivity, source-role, geometry/depth context, provenance, and review checks.

Redirect implementation and source-family authority to `connectors/kansas/kgs/` once verified.

[Back to top ↑](#top)

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---:|---|---|
| `connectors/kgs_las/README.md` | **CONFIRMED** | Target file exists and was blank before this update. | Does not prove implementation files, tests, or CI. |
| `docs/sources/catalog/kansas/ksgs.md` | **CONFIRMED** | KGS source profile says canonical connector path is `connectors/kansas/kgs/` and identifies KGS LAS digital well logs and well tops as a KGS source-family row. | Does not prove current source terms, endpoint stability, activation, or implementation. |
| `connectors/kgs/README.md` | **CONFIRMED** | Top-level KGS path is documented as noncanonical compatibility. | Does not prove LAS implementation depth. |
| `connectors/kansas/kgs/` | **NEEDS VERIFICATION** | Named as canonical adapter home by source profile. | Actual files, code, fixtures, tests, and CI remain unverified here. |

---

## Lifecycle diagram

```mermaid
flowchart LR
  A[KGS LAS / well-top source material] --> B[SourceDescriptor gate]
  B --> C{Admission decision}
  C -->|allowed with limits| D[RAW geology/hydrology handoff]
  C -->|needs review| Q[QUARANTINE handoff]
  C -->|denied| X[No connector activation]
  D --> E[Well/log/depth validation]
  Q --> E
  E --> F[Rights, sensitivity, and source-shape review]
  F --> G[EvidenceBundle and policy review]
  G --> H[Catalog or triplet projection]
  H --> I[Release review]
  I --> P[Published public-safe artifact]
```

[Back to top ↑](#top)

---

## Admission posture

Expected behavior for KGS LAS source-admission work:

- no live source access unless explicitly enabled and reviewed;
- no source fetch without an accepted SourceDescriptor and activation decision;
- no implicit publication from retrieved source material;
- no operational drilling, reservoir, engineering, safety, or field-use use;
- no conversion of LAS curves, well tops, or depth-indexed records into public geology, hydrology, reservoir, or resource truth without downstream review;
- no collapse of LAS logs into KGS bedrock map products, KCC regulatory records, KDHE environmental records, WWC5 records, or generated summaries;
- no loss of source ID, source URI, source role, well identity, log identity, curve/top identity, depth datum/unit context, geometry/uncertainty, date/vintage, license/rights, review, or release-class metadata;
- unclear rights, source role, well identity, log identity, curve/top identity, depth context, geometry, endpoint, vintage, or schema drift routes to quarantine or abstention.

---

## Anti-collapse rules

The LAS lane must preserve the following controls:

1. `connectors/kgs_las/` is compatibility-only unless an ADR says otherwise.
2. Canonical KGS work belongs under `connectors/kansas/kgs/`.
3. Well identity, log identity, curve/top identity, depth datum/unit context, geometry, and source vintage must remain explicit.
4. LAS source material must not be collapsed into KGS bedrock products, KCC regulatory records, KDHE environmental records, WWC5 records, or generated summaries.
5. Public release is a governed state transition, not a connector output.
6. Derived summaries, maps, tiles, joins, analyses, and AI explanations are downstream carriers, not sovereign truth.

---

## Validation

Compatibility-lane validation should check that:

- this path is not treated as canonical without ADR/migration evidence;
- source metadata is preserved;
- SourceDescriptor references are required for activation;
- source role, well identity, log identity, curve/top identity, depth datum/unit context, geometry, and source vintage are explicit where available;
- rights and sensitivity states are explicit before promotion-track use;
- malformed or incomplete records fail closed;
- records with unresolved rights, sensitivity state, source role, well identity, log identity, curve/top identity, depth context, geometry, vintage, or access method route to quarantine;
- connector output is limited to RAW or QUARANTINE handoff;
- no connector run writes directly to processed, catalog, triplet, published, proof, receipt, or release stores.

Root-level validation, policy-as-code, EvidenceBundle closure, release review, public caveats, and rollback remain outside this compatibility lane.

[Back to top ↑](#top)

---

## Definition of done

This compatibility README is ready for first review when:

- [ ] KGS source profile is linked and current enough for review.
- [ ] A migration or ADR decision resolves whether to remove this top-level path, keep it as a redirect, or migrate implementation under `connectors/kansas/kgs/`.
- [ ] Canonical LAS implementation home is verified.
- [ ] SourceDescriptor homes and LAS sub-product IDs are verified.
- [ ] Rights terms, access methods, cadence, fixture strategy, source-role strategy, and sensitivity checks are verified by source steward review.
- [ ] Live source access is disabled by default for connector code.
- [ ] Source-role, well identity, log identity, curve/top identity, depth datum/unit context, geometry, vintage, rights, sensitivity, and anti-collapse checks are represented in tests.
- [ ] Connector output is limited to RAW or QUARANTINE handoff.
- [ ] No public operational, drilling, reservoir, engineering, safety, hydrology, or geology claims are created by connector code.

---

## Rollback

Rollback is required if this README is used to justify canonical-family status, direct publication, source activation, source-role collapse, rights/sensitivity bypass, public operational claims, or direct writes beyond RAW/QUARANTINE handoff.

Rollback target:

```text
commit prior to this update: SHA_TBD_AFTER_GIT_HISTORY_CHECK
```

Because the file was blank before this update, a safe rollback is to restore the blank placeholder or replace this document with a shorter redirect-only README until canonical placement is resolved.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm canonical KGS LAS implementation home. | **NEEDS VERIFICATION** | Directory Rules, ADR, migration note, or repo tree. |
| Confirm whether this top-level path should remain. | **NEEDS VERIFICATION** | ADR or migration decision. |
| Confirm SourceDescriptor homes and LAS sub-product IDs. | **NEEDS VERIFICATION** | Source registry entries and accepted schemas. |
| Confirm current access methods, cadence, and terms. | **NEEDS VERIFICATION** | Source steward review and current source documentation. |
| Confirm rights and sensitivity handling. | **NEEDS VERIFICATION** | Rights review, sensitivity review, and policy references. |
| Confirm depth datum/unit normalization and release-generalization policy. | **NEEDS VERIFICATION** | Schemas, validators, policy references, fixtures, and review notes. |
| Confirm fixture strategy and CI wiring. | **NEEDS VERIFICATION** | Fixture registry, workflow files, and test logs. |

---

## Maintainer note

Do not build new authority here. This existing top-level path should either stay a clear compatibility pointer or be removed after migration. Implementation should converge under `connectors/kansas/kgs/` unless an ADR says otherwise.

[Back to top ↑](#top)

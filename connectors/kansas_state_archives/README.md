<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-kansas-state-archives-readme
title: connectors/kansas_state_archives/ — Kansas State Archives Compatibility Connector Lane
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Kansas source steward · Archives steward · Rights reviewer · Sensitivity reviewer · CARE/cultural review steward · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; compatibility-lane; noncanonical-path; archives-source; kshs-umbrella; rights-gated; sensitivity-gated; no-publication
proposed_path: connectors/kansas_state_archives/README.md
truth_posture: CONFIRMED path exists / NONCANONICAL compatibility README / CANONICAL HOME NEEDS VERIFICATION
related:
  - ../README.md
  - ../kansas/README.md
  - ../kansas/kshs-state-archives/README.md
  - ../../docs/sources/catalog/kansas/kansas-state-archives.md
  - ../../docs/sources/catalog/kansas/kansas-memory.md
  - ../../docs/sources/catalog/kansas/khri.md
  - ../../docs/sources/catalog/kansas/README.md
  - ../../docs/standards/oai-pmh.md
  - ../../docs/standards/iiif.md
  - ../../docs/standards/snac-eac-cpf.md
  - ../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../data/registry/sources/archives/
  - ../../data/raw/archives/
  - ../../data/quarantine/archives/
  - ../../fixtures/
  - ../../schemas/contracts/v1/source/
  - ../../policy/sensitivity/
  - ../../policy/rights/
  - ../../release/
tags: [kfm, connectors, kansas-state-archives, kansas, kshs, archives, compatibility, oai-pmh, iiif, snac, eac-cpf, rights, sensitivity, care, source-admission, raw, quarantine, governance]
notes:
  - "This README replaces a thin greenfield stub at a legacy-style top-level connector path."
  - "The Kansas State Archives source brief says the source catalog path moved from a flat snake_case slug to `docs/sources/catalog/kansas/kansas-state-archives.md`."
  - "The same brief frames Kansas State Archives as a KSHS umbrella layer and says per-surface connector adapters remain proposed under the confirmed `connectors/kansas/` family lane."
  - "This top-level `connectors/kansas_state_archives/` path is therefore documented as a compatibility lane, not a new canonical authority root."
  - "Rights, sensitivity, cultural-care, surface-specific access mechanics, per-surface descriptors, activation, fixtures, tests, CI wiring, and public-release classes remain NEEDS VERIFICATION."
  - "Connector output may enter RAW or QUARANTINE handoff only; downstream validation, EvidenceBundle closure, rights/sensitivity/CARE review, catalog/triplet projection, release review, publication, correction, and rollback remain outside this folder."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Kansas State Archives Compatibility Connector Lane

> Compatibility README for the existing top-level `connectors/kansas_state_archives/` path. This path is **not** the canonical connector home; KSHS/Kansas State Archives connector work belongs under the canonical `connectors/kansas/` source-family lane unless an ADR or migration decision says otherwise.

<p>
  <img alt="Status: compatibility" src="https://img.shields.io/badge/status-compatibility-yellow">
  <img alt="Canonicality: noncanonical path" src="https://img.shields.io/badge/canonicality-noncanonical__path-orange">
  <img alt="Source family: archives" src="https://img.shields.io/badge/source__family-archives-blue">
  <img alt="Rights: needs verification" src="https://img.shields.io/badge/rights-needs__verification-critical">
  <img alt="Lifecycle: RAW or QUARANTINE only" src="https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE%20only-orange">
</p>

> [!IMPORTANT]
> **Status:** compatibility / noncanonical-path README · **Owner:** `OWNER_TBD`  
> **Path:** `connectors/kansas_state_archives/README.md`  
> **Truth posture:** `CONFIRMED` file exists · `NONCANONICAL` compatibility path · `NEEDS VERIFICATION` canonical implementation home  
> **Boundary:** source-admission compatibility only; no public archive release, no direct publication, no rights/sensitivity/CARE bypass, no canonical-family claim.

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Evidence ledger](#evidence-ledger) · [Lifecycle diagram](#lifecycle-diagram) · [Admission posture](#admission-posture) · [Anti-collapse rules](#anti-collapse-rules) · [Validation](#validation) · [Rollback](#rollback) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/kansas_state_archives/` is retained here only as a compatibility lane because the path already exists.

The Kansas State Archives source brief documents a migration away from the flat snake_case slug and identifies Kansas State Archives as a KSHS umbrella source-family layer under the canonical Kansas source family. Per-surface adapters such as Kansas Memory, KHRI, and State Archives proper are expected to converge under `connectors/kansas/<surface_id>/` unless governance records a different decision.

This file may document the compatibility boundary, migration intent, and source-admission rules. It must not become the canonical connector home unless an ADR or migration decision explicitly authorizes that exception.

[Back to top ↑](#top)

---

## Repo fit

| Surface | Role | Status |
|---|---|---:|
| `connectors/kansas_state_archives/` | Existing top-level compatibility path. | **CONFIRMED path / NONCANONICAL** |
| `connectors/kansas/` | Canonical Kansas connector-family lane. | **CONFIRMED via source brief** |
| `connectors/kansas/kshs-state-archives/` | Proposed per-surface connector home for State Archives proper. | **PROPOSED / NEEDS VERIFICATION** |
| `connectors/kansas/kansas-memory/` | Proposed per-surface connector home for Kansas Memory. | **PROPOSED / NEEDS VERIFICATION** |
| `connectors/kansas/khri/` | Proposed per-surface connector home for KHRI. | **PROPOSED / NEEDS VERIFICATION** |
| `docs/sources/catalog/kansas/kansas-state-archives.md` | Human-facing KSHS umbrella source-family brief. | **CONFIRMED** |
| `data/registry/sources/archives/` | Candidate machine-readable source registry area. | **PROPOSED / NEEDS VERIFICATION** |
| `data/raw/archives/` | Candidate RAW handoff target. | **PROPOSED / NEEDS VERIFICATION** |
| `data/quarantine/archives/` | Candidate quarantine handoff target. | **PROPOSED / NEEDS VERIFICATION** |
| `policy/rights/` and `policy/sensitivity/` | Rights and sensitivity authority. | **Outside connector** |
| `release/` | Release and publication controls. | **Out of scope for this compatibility lane** |

[Back to top ↑](#top)

---

## Accepted inputs

Accepted content for this noncanonical compatibility path:

- README-level migration and compatibility notes;
- links to the canonical Kansas source-family lane;
- notes that prevent this top-level path from becoming a parallel authority;
- temporary fixture or test notes only if they are explicitly migration-bound;
- adapter notes for KSHS archive surfaces, OAI-PMH, IIIF, SNAC/EAC-CPF, or related archive access methods, if verified by source review;
- quarantine criteria for unresolved rights, cultural sensitivity, living-person content, collection identity, item identity, metadata shape, access-method questions, or surface-specific source-role issues.

New implementation code should prefer the canonical Kansas family lane unless an ADR says otherwise.

---

## Exclusions

This folder must not contain or imply authority over:

- canonical connector-family status;
- public archive release decisions;
- public item summaries presented as authoritative history;
- direct writes to `PROCESSED`, `CATALOG`, `TRIPLET`, `PUBLISHED`, proof, receipt, or release stores;
- SourceDescriptor authority records;
- policy or schema authority;
- rights, sensitivity, cultural-care, or living-person release decisions;
- generated summaries presented as authoritative source truth;
- source activation without SourceDescriptor, rights, sensitivity, cultural-care, provenance, and review checks.

Redirect implementation and source-family authority to the canonical `connectors/kansas/` lane once verified.

[Back to top ↑](#top)

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---:|---|---|
| `connectors/kansas_state_archives/README.md` | **CONFIRMED** | Target file exists and previously contained only a greenfield stub. | Does not prove implementation files, tests, or CI. |
| `docs/sources/catalog/kansas/kansas-state-archives.md` | **CONFIRMED** | KSHS/Kansas State Archives source brief moved from flat snake_case to the Kansas catalog family; `connectors/kansas/` is the confirmed family; per-surface adapters under `connectors/kansas/` remain proposed. | Does not prove current access method, per-surface descriptors, or connector activation. |
| `connectors/kansas/README.md` | **CONFIRMED** | Kansas connector family is the canonical source-admission lane for Kansas source products. | Does not prove a KSHS child adapter exists. |
| `connectors/kansas/kshs-state-archives/` | **NEEDS VERIFICATION** | Named as proposed State Archives proper adapter home by source brief. | Actual path/file presence is not verified in this update. |

---

## Lifecycle diagram

```mermaid
flowchart LR
  A[KSHS / Kansas State Archives source material] --> B[SourceDescriptor gate]
  B --> C{Admission decision}
  C -->|allowed with limits| D[RAW archives handoff]
  C -->|needs review| Q[QUARANTINE archives handoff]
  C -->|denied| X[No connector activation]
  D --> E[Surface identity and metadata validation]
  Q --> E
  E --> F[Rights, sensitivity, and CARE review]
  F --> G[EvidenceBundle and policy review]
  G --> H[Catalog or triplet projection]
  H --> I[Release review]
  I --> P[Published public-safe artifact]
```

[Back to top ↑](#top)

---

## Admission posture

Expected behavior for KSHS/Kansas State Archives source-admission work:

- no live source access unless explicitly enabled and reviewed;
- no source fetch without an accepted SourceDescriptor and activation decision;
- no implicit publication from retrieved source material;
- no use of archive item text or metadata as public truth without evidence, citation, rights, sensitivity, and review gates;
- no collapse of Kansas Memory, KHRI, State Archives proper, and adjacent KSHS surfaces into one untyped feed;
- no loss of surface identity, collection identity, item identity, source URI, title/creator/date fields, rights statement, cultural-care flags, sensitivity flags, access method, retrieval time, source role, review, or release-class metadata;
- unclear rights, sensitivity, cultural-care concerns, living-person concerns, item identity, source identity, access method, metadata shape, surface role, or schema drift routes to quarantine or abstention.

---

## Anti-collapse rules

The Kansas State Archives source brief identifies the controlling anti-collapse stack:

1. This top-level snake_case path is compatibility-only unless governance says otherwise.
2. The KSHS umbrella layer is not a substitute for per-surface descriptors.
3. Kansas Memory, KHRI, State Archives proper, and adjacent KSHS publication surfaces must retain surface-specific identity and source role.
4. A digitized item or metadata row is evidence, not an automatic public historical claim.
5. Archives material may carry cultural sensitivity, living-person, sovereignty, or rights concerns and must fail closed until reviewed.
6. Public release is a governed state transition, not a connector output.
7. Derived summaries, maps, timelines, search indexes, joins, and AI explanations are downstream carriers, not sovereign truth.

---

## Validation

Compatibility-lane validation should check that:

- the path is not treated as canonical without ADR/migration evidence;
- source metadata is preserved;
- SourceDescriptor references are required for activation;
- per-surface identity is explicit;
- rights, sensitivity, and cultural-care states are explicit before promotion-track use;
- collection identity, item identity, source URI, title/creator/date fields, access method, retrieval time, source role, review, and vintage fields are explicit where available;
- malformed or incomplete records fail closed;
- records with unclear rights, unresolved sensitivity, unresolved cultural-care concerns, unresolved item identity, unresolved surface identity, unresolved source role, or unresolved metadata shape route to quarantine;
- connector output is limited to RAW or QUARANTINE handoff;
- no connector run writes directly to processed, catalog, triplet, published, proof, receipt, or release stores.

Root-level validation, policy-as-code, EvidenceBundle closure, release review, public caveats, and rollback remain outside this compatibility lane.

[Back to top ↑](#top)

---

## Definition of done

This compatibility README is ready for first review when:

- [ ] Kansas State Archives source-family brief is linked and current enough for review.
- [ ] A migration or ADR decision resolves whether to remove this top-level path, keep it as a redirect, or move implementation under `connectors/kansas/kshs-state-archives/` or another ratified child path.
- [ ] Canonical KSHS surface implementation homes are verified.
- [ ] SourceDescriptor homes and KSHS surface source IDs are verified.
- [ ] Rights terms, access methods, item identity rules, surface identity rules, and sensitivity/CARE checks are verified by source steward review.
- [ ] Live source access is disabled by default for connector code.
- [ ] Metadata identity, rights, sensitivity, cultural-care, source-role, surface-role, and anti-collapse checks are represented in tests.
- [ ] Connector output is limited to RAW or QUARANTINE handoff.
- [ ] No public archive claims are created by connector code.

---

## Rollback

Rollback is required if this README is used to justify canonical-family status, direct publication, source activation, rights/sensitivity/CARE bypass, public historical claims, surface-role collapse, or direct writes beyond RAW/QUARANTINE handoff.

Rollback target:

```text
commit prior to this update: SHA_TBD_AFTER_GIT_HISTORY_CHECK
```

Because the previous file was only a greenfield stub, a safe rollback is to restore that stub or replace this document with a shorter redirect-only README until canonical placement is resolved.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm canonical KSHS / Kansas State Archives connector path. | **NEEDS VERIFICATION** | Directory Rules, ADR, migration note, or repo tree. |
| Confirm whether this top-level path should remain. | **NEEDS VERIFICATION** | ADR or migration decision. |
| Confirm per-surface connector homes. | **NEEDS VERIFICATION** | Repo tree and source-family migration note. |
| Confirm SourceDescriptor homes and source IDs. | **NEEDS VERIFICATION** | Source registry entries and accepted schemas. |
| Confirm current access methods, item identity, and metadata shapes. | **NEEDS VERIFICATION** | Source steward review and current source documentation. |
| Confirm rights and sensitivity handling. | **NEEDS VERIFICATION** | Rights review, sensitivity review, and policy references. |
| Confirm cultural-care review handling. | **NEEDS VERIFICATION** | Policy references and review receipts. |
| Confirm fixture strategy and CI wiring. | **NEEDS VERIFICATION** | Fixture registry, workflow files, and test logs. |

---

## Maintainer note

Do not build new authority here. This existing snake_case path should either stay a clear compatibility pointer or be removed after migration. Implementation should converge under the canonical Kansas source-family lane unless an ADR says otherwise.

[Back to top ↑](#top)

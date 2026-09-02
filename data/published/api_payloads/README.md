<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/published/api-payloads/readme
title: data/published/api_payloads README
type: directory-readme
version: v0.1
status: draft
owners:
  - TODO(owner): data steward
  - TODO(owner): API steward
  - TODO(owner): publication steward
  - TODO(owner): release steward
  - TODO(owner): domain stewards
created: 2026-06-25
updated: 2026-06-25
policy_label: public-review
path: data/published/api_payloads/README.md
related:
  - ../README.md
  - ../../README.md
  - ../../proofs/README.md
  - ../../receipts/README.md
  - ../../../release/README.md
  - ../../../contracts/README.md
  - ../../../schemas/README.md
  - ../../../policy/README.md
  - atmosphere/README.md
  - fauna/README.md
  - flora/README.md
  - soil/README.md
notes:
  - "Parent README for released API payload carriers under data/published/. It replaces a greenfield stub."
  - "This lane stores release-linked API payload snapshots or packages only after release gates pass."
  - "This README describes placement and boundaries; it does not prove emitted payloads, schemas, validators, CI, or governed API routes exist."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/published/api_payloads/`

> Parent published-data lane for released, public-safe KFM **API payload carriers**. Files here should be immutable, release-linked snapshots or packages consumed through governed API or approved released-artifact paths.

![Status: draft](https://img.shields.io/badge/status-draft-orange)
![Lifecycle: PUBLISHED](https://img.shields.io/badge/lifecycle-PUBLISHED-2ea44f)
![Carrier: API payload](https://img.shields.io/badge/carrier-API--payload-blue)
![Authority: not release](https://img.shields.io/badge/authority-not--release-b91c1c)
![Publication: release gated](https://img.shields.io/badge/publication-release--gated-blue)
![Truth: cite or abstain](https://img.shields.io/badge/truth-cite--or--abstain-6f42c1)

> [!IMPORTANT]
> **Status:** `draft`  
> **Owners:** `TODO(owner): data steward` · `TODO(owner): API steward` · `TODO(owner): publication steward` · `TODO(owner): release steward` · `TODO(owner): domain stewards`  
> **Path:** `data/published/api_payloads/README.md`  
> **Truth posture:** CONFIRMED target path and authored child lane READMEs from current repo evidence / PROPOSED child layout and naming / NEEDS VERIFICATION for emitted payloads, schemas, validators, release manifests, CI checks, and governed API routes.

> [!WARNING]
> This directory does not approve publication and is not the runtime governed API. Payload files belong here only after release authority exists under `release/`, evidence and catalog closure are complete, validation gates pass, policy state is recorded, and rollback/correction paths are available.

---

## Quick jumps

| Section | Use it for |
|---|---|
| [1. Scope](#1-scope) | What this parent lane is for. |
| [2. Repo fit](#2-repo-fit) | Neighboring authority roots. |
| [3. Accepted payloads](#3-accepted-payloads) | What may live here after release. |
| [4. Exclusions](#4-exclusions) | What must stay out. |
| [5. Child lane index](#5-child-lane-index) | Authored domain payload lanes. |
| [6. Publication gates](#6-publication-gates) | Minimum support before payloads land here. |
| [7. Suggested layout](#7-suggested-layout) | Proposed child structure. |
| [8. Maintenance checklist](#8-maintenance-checklist) | Checks before adding or changing payloads. |
| [9. Definition of done](#9-definition-of-done) | What remains before maturity. |

---

## 1. Scope

`data/published/api_payloads/` is the parent published carrier lane for release-approved API payload snapshots and packages across KFM domains.

Use this lane for payloads that are:

- tied to a release record;
- public-safe for the declared audience;
- traceable to evidence, catalog, validation, policy, review, correction, and rollback references;
- shaped for governed API, Evidence Drawer, map popup, Focus Mode, export, or public UI consumption; and
- explicit about source role, evidence support, time scope, caveats, and correction status.

This lane is downstream of release. It should not contain source captures, working candidates, held material, processed candidates, catalog drafts, proof objects, receipts, schemas, policy rules, release decisions, or direct model output.

[Back to top](#top)

---

## 2. Repo fit

| Neighbor | Role | Boundary |
|---|---|---|
| `data/raw/<domain>/` | Source capture lanes. | Not public-readable. |
| `data/work/<domain>/` | Working candidate lanes. | Not public-readable. |
| `data/quarantine/<domain>/` | Held-material lanes. | Not public-readable. |
| `data/processed/<domain>/` | Validated candidate lanes. | Upstream of release. |
| `data/catalog/` | Catalog lanes. | Discovery and lineage, not release authority. |
| `data/proofs/` | Proof-support lanes. | Support, not published payloads. |
| `data/receipts/` | Process-memory lanes. | Receipts do not publish. |
| `release/` | Release authority. | Manifests, correction, withdrawal, rollback, signatures. |
| `contracts/` | Semantic meaning. | Payloads conform; they do not define meaning. |
| `schemas/` | Machine shape. | Payloads validate; they do not define schemas. |
| `policy/` | Admissibility. | Payloads carry outcomes; policy lives elsewhere. |

[Back to top](#top)

---

## 3. Accepted payloads

| Payload type | Suggested placement | Required support |
|---|---|---|
| Released endpoint snapshot | `<domain>/endpoints/<release_id>/<endpoint_slug>.json` | Release, schema, evidence, policy, rollback refs. |
| Released Evidence Drawer payload | `<domain>/evidence_drawer/<release_id>/<payload_slug>.json` | Evidence, citation, validation, release refs. |
| Released Focus Mode payload | `<domain>/focus_mode/<release_id>/<payload_slug>.json` | Release, evidence, AI receipt where applicable. |
| Released map-popup payload | `<domain>/map_popups/<release_id>/<payload_slug>.json` | Source role, caveats, release refs. |
| Released export payload | `<domain>/exports/<release_id>/<payload_slug>.json` | Audience, policy, proof, release refs. |
| Released public summary | `<domain>/public_summaries/<release_id>/<payload_slug>.json` | Public-safe posture and evidence refs. |
| Domain payload index | `<domain>/indexes/<domain>-api-payload-index.json` | Points to release-approved payloads only. |
| Superseded payload | `<domain>/retired/<release_id>/<payload_slug>.json` | Supersession, correction, withdrawal, or rollback reference. |

[Back to top](#top)

---

## 4. Exclusions

| Excluded material | Correct home |
|---|---|
| Source payloads and source-system exports | `data/raw/<domain>/` |
| Working or held candidates | `data/work/<domain>/` or `data/quarantine/<domain>/` |
| Processed normalized data | `data/processed/<domain>/` |
| Catalog records | `data/catalog/` |
| Proof objects | `data/proofs/` |
| Receipts | `data/receipts/` |
| Release manifests, promotion decisions, rollback cards, correction notices, withdrawal notices, signatures | `release/` |
| Policy logic | `policy/` |
| Schemas | `schemas/` |
| Semantic contracts | `contracts/` |
| Direct model output or unreviewed AI summaries | governed AI/review paths before release |

[Back to top](#top)

---

## 5. Child lane index

| Lane | Current role |
|---|---|
| [`atmosphere/`](./atmosphere/) | Released Atmosphere / Air API payload carriers. |
| [`fauna/`](./fauna/) | Released Fauna API payload carriers. |
| [`flora/`](./flora/) | Released Flora API payload carriers. |
| [`soil/`](./soil/) | Released Soil API payload carriers. |
| [`soil/pedons/`](./soil/pedons/) | Released Soil pedon / SoilProfileView payload carriers. |
| [`soil/station_series/`](./soil/station_series/) | Released Soil station-series payload carriers. |

Additional domains should get a child README before live payload instances land there.

[Back to top](#top)

---

## 6. Publication gates

Before an API payload is placed here, verify:

- [ ] release authority exists under `release/`;
- [ ] every consequential claim resolves to evidence support;
- [ ] schema and domain validation gates pass or hold with finite reasons;
- [ ] catalog closure exists;
- [ ] policy decisions allow the target audience class;
- [ ] review records exist where required;
- [ ] source role, time scope, caveats, and public-safe posture are preserved;
- [ ] correction and rollback targets are traceable;
- [ ] payload digests or integrity refs bind the file to the release record.

If any gate is unresolved, hold the payload upstream.

[Back to top](#top)

---

## 7. Suggested layout

```text
data/published/api_payloads/
├── README.md
├── <domain>/
│   ├── README.md
│   ├── endpoints/
│   │   └── <release_id>/
│   ├── evidence_drawer/
│   │   └── <release_id>/
│   ├── focus_mode/
│   │   └── <release_id>/
│   ├── map_popups/
│   │   └── <release_id>/
│   ├── exports/
│   │   └── <release_id>/
│   ├── public_summaries/
│   │   └── <release_id>/
│   ├── indexes/
│   │   └── <domain>-api-payload-index.json
│   └── retired/
│       └── <release_id>/
└── cross_domain/
    └── <scope>/
```

Suggested deterministic file name:

```text
<domain>.published.api_payload.<payload_family>.<scope>.<release_id>.<short_hash>.json
```

This layout is PROPOSED until validated by contracts, schemas, fixtures, and release tooling.

[Back to top](#top)

---

## 8. Maintenance checklist

Before adding or changing a payload under this parent lane, verify:

- [ ] The payload is release-approved and public-safe for the intended audience.
- [ ] The release record points to this payload.
- [ ] Evidence, catalog, validation, policy, review, correction, and rollback refs are present where required.
- [ ] Source role, evidence support, time scope, caveats, and public-safe posture are preserved.
- [ ] The payload does not duplicate upstream, proof, receipt, catalog, schema, contract, policy, or release authority.
- [ ] The payload has a digest or integrity reference.
- [ ] Public clients consume it through governed interfaces or approved released artifact paths.
- [ ] Domain-specific rules are documented in the relevant child lane README.

[Back to top](#top)

---

## 9. Definition of done

This lane is operationally mature when:

- [ ] `data/published/README.md` defines the parent published-data contract.
- [ ] API payload contracts and schemas exist under approved homes.
- [ ] Release tooling writes or verifies payloads only after release authority is present.
- [ ] Validators block missing evidence, missing release refs, missing rollback, source-role collapse, missing review state, and unsafe public payload fields.
- [ ] Valid and invalid fixtures cover endpoint, Evidence Drawer, Focus Mode, map popup, export, public summary, correction, supersession, and rollback payloads.
- [ ] Governed API or released-artifact routes are documented and tested.
- [ ] Active domains have child README files before live payload instances land there.

---

## Maintainer note

Published API payloads are visible carriers, not truth or release authority. Keep them compact, citable, public-safe, audience-aware, caveat-aware, and reversible. If evidence, validation, policy, release, correction, or rollback support is incomplete, keep the payload upstream instead of placing it here.

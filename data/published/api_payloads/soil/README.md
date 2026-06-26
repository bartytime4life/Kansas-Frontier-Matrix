<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/published/api-payloads/soil/readme
title: data/published/api_payloads/soil README
type: directory-readme
version: v0.1
status: draft
owners:
  - TODO(owner): data steward
  - TODO(owner): soil domain steward
  - TODO(owner): API steward
  - TODO(owner): publication steward
  - TODO(owner): release steward
created: 2026-06-25
updated: 2026-06-25
policy_label: public-review
path: data/published/api_payloads/soil/README.md
related:
  - ../README.md
  - ../../README.md
  - ../../../proofs/README.md
  - ../../../proofs/soil/README.md
  - ../../../proofs/proof_pack/soil/README.md
  - ../../../proofs/validation_report/soil/README.md
  - ../../../receipts/README.md
  - ../../../../release/README.md
  - ../../../../docs/domains/soil/ARCHITECTURE.md
  - ../../../../contracts/README.md
  - ../../../../schemas/README.md
  - ../../../../policy/README.md
notes:
  - "Directory README for released Soil API payload carriers under data/published/api_payloads/."
  - "This lane stores release-linked API payload snapshots or packages only after release gates pass."
  - "This README describes placement and boundaries; it does not prove emitted payloads, schemas, validators, CI, or API routes exist."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/published/api_payloads/soil/`

> Published API-payload lane for released, public-safe Soil payload carriers. Files here should be immutable, release-linked API payload snapshots or packages consumed through governed API or approved released-artifact paths.

![Status: draft](https://img.shields.io/badge/status-draft-orange)
![Lifecycle: PUBLISHED](https://img.shields.io/badge/lifecycle-PUBLISHED-2ea44f)
![Domain: soil](https://img.shields.io/badge/domain-soil-795548)
![Carrier: API payload](https://img.shields.io/badge/carrier-API--payload-blue)
![Authority: not release](https://img.shields.io/badge/authority-not--release-b91c1c)
![Truth: cite or abstain](https://img.shields.io/badge/truth-cite--or--abstain-6f42c1)

> [!IMPORTANT]
> **Status:** `draft`  
> **Owners:** `TODO(owner): data steward` · `TODO(owner): soil domain steward` · `TODO(owner): API steward` · `TODO(owner): publication steward` · `TODO(owner): release steward`  
> **Path:** `data/published/api_payloads/soil/README.md`  
> **Truth posture:** CONFIRMED target path and Soil docs from current repo evidence / PROPOSED child layout and naming / NEEDS VERIFICATION for emitted payloads, schemas, validators, release manifests, CI checks, and governed API routes.

> [!WARNING]
> This directory does not approve publication. Payload files belong here only after release authority exists under `release/`, evidence and catalog closure are complete, validation gates pass, policy state is recorded, and rollback/correction paths are available.

---

## Quick jumps

| Section | Use it for |
|---|---|
| [1. Scope](#1-scope) | What this lane is for. |
| [2. Repo fit](#2-repo-fit) | Neighboring authority roots. |
| [3. Accepted payloads](#3-accepted-payloads) | What may live here after release. |
| [4. Exclusions](#4-exclusions) | What must stay out. |
| [5. Publication gates](#5-publication-gates) | Minimum support before a payload lands here. |
| [6. Soil payload rules](#6-soil-payload-rules) | Domain-specific public payload guardrails. |
| [7. Suggested layout](#7-suggested-layout) | Proposed child structure. |
| [8. Maintenance checklist](#8-maintenance-checklist) | Checks before adding or changing payloads. |
| [9. Definition of done](#9-definition-of-done) | What remains before maturity. |

---

## 1. Scope

`data/published/api_payloads/soil/` is the published carrier lane for release-approved Soil API payload snapshots and packages.

Use this lane for payloads that are:

- tied to a release record;
- public-safe for the declared audience;
- traceable to evidence, catalog, validation, policy, review, and rollback references;
- shaped for governed API, Evidence Drawer, map popup, Focus Mode, export, or public UI consumption; and
- explicit about source role, support type, evidence support, units, depth context, time scope, caveats, and correction status.

This lane is downstream of release. It should not contain source captures, working candidates, held material, processed candidates, catalog drafts, proof objects, receipts, schemas, policy rules, release decisions, or direct model output.

[Back to top](#top)

---

## 2. Repo fit

| Neighbor | Role | Boundary |
|---|---|---|
| `data/raw/soil/` | Source capture lane. | Not public-readable. |
| `data/work/soil/` | Working candidate lane. | Not public-readable. |
| `data/quarantine/soil/` | Held-material lane. | Not public-readable. |
| `data/processed/soil/` | Validated candidate lane. | Upstream of release. |
| `data/catalog/domain/soil/` | Catalog lane. | Discovery and lineage, not release authority. |
| `data/proofs/soil/` | Proof-support lane. | Support, not published payload. |
| `data/proofs/validation_report/soil/` | Validation-report lane. | Gate support, not publication authority. |
| `data/receipts/` | Process-memory lane. | Receipts do not publish. |
| `release/` | Release authority. | Manifests, correction, withdrawal, rollback, signatures. |
| `contracts/` | Semantic meaning. | Payloads conform; they do not define meaning. |
| `schemas/` | Machine shape. | Payloads validate; they do not define schemas. |
| `policy/` | Admissibility. | Payloads carry outcomes; policy lives elsewhere. |

[Back to top](#top)

---

## 3. Accepted payloads

| Payload type | Suggested placement | Required support |
|---|---|---|
| Released endpoint snapshot | `endpoints/<release_id>/<endpoint_slug>.json` | Release, schema, evidence, policy, rollback refs. |
| Released Evidence Drawer payload | `evidence_drawer/<release_id>/<payload_slug>.json` | Evidence, citation, validation, release refs. |
| Released Focus Mode payload | `focus_mode/<release_id>/<payload_slug>.json` | Release, evidence, AI receipt where applicable. |
| Released map-popup payload | `map_popups/<release_id>/<payload_slug>.json` | Source role, support type, caveats, release refs. |
| Released export payload | `exports/<release_id>/<payload_slug>.json` | Audience, policy, proof, release refs. |
| Released public summary | `public_summaries/<release_id>/<payload_slug>.json` | Public-safe posture and evidence refs. |
| Payload index | `indexes/soil-api-payload-index.json` | Points to release-approved payloads only. |
| Superseded payload | `retired/<release_id>/<payload_slug>.json` | Supersession, correction, withdrawal, or rollback reference. |

[Back to top](#top)

---

## 4. Exclusions

| Excluded material | Correct home |
|---|---|
| Source payloads, source-system exports, survey extracts, rasters, sensor dumps, or model files | `data/raw/soil/` |
| Working or held candidates | `data/work/soil/` or `data/quarantine/soil/` |
| Processed normalized data | `data/processed/soil/` |
| Catalog records | `data/catalog/` |
| Proof objects | `data/proofs/` |
| Receipts | `data/receipts/` |
| Release manifests or rollback cards | `release/` |
| Policy logic | `policy/` |
| Schemas | `schemas/` |
| Semantic contracts | `contracts/` |
| Unreviewed AI output | governed AI/review paths before release |

[Back to top](#top)

---

## 5. Publication gates

Before a Soil API payload is placed here, verify:

- [ ] release authority exists under `release/`;
- [ ] every consequential claim resolves to evidence support;
- [ ] schema and domain validation gates pass or hold with finite reasons;
- [ ] catalog closure exists;
- [ ] policy decisions allow the target audience class;
- [ ] review records exist where required;
- [ ] support type, source role, units, time scope, and caveats are preserved;
- [ ] correction and rollback targets are traceable;
- [ ] payload digests or integrity refs bind the file to the release record.

If any gate is unresolved, hold the payload upstream.

[Back to top](#top)

---

## 6. Soil payload rules

| Rule | Public payload posture |
|---|---|
| Support type is explicit | Payloads must distinguish static survey, gridded derivative, station reading, satellite-derived reading, profile evidence, and interpretation. |
| Evidence is visible | Payloads must cite EvidenceBundle support and preserve relevant source, valid, retrieval, and release time fields. |
| Interpretations are labeled | Suitability, erosion, and hydrologic-group payloads carry caveats and do not become crop, flood, legal, or engineering truth. |
| Units and depth matter | Soil property and moisture payloads preserve units, depth context, method, and quality context where material. |
| Cross-lane handoffs preserve ownership | Agriculture, hydrology, hazards, geology, habitat, flora, fauna, people/land, and settlement context remain owned by their domains. |
| AI is not root truth | AI summaries can consume released payloads but cannot replace EvidenceBundles, validation, release, or citations. |

[Back to top](#top)

---

## 7. Suggested layout

```text
data/published/api_payloads/soil/
├── README.md
├── endpoints/
│   └── <release_id>/
├── evidence_drawer/
│   └── <release_id>/
├── focus_mode/
│   └── <release_id>/
├── map_popups/
│   └── <release_id>/
├── exports/
│   └── <release_id>/
├── public_summaries/
│   └── <release_id>/
├── indexes/
│   └── soil-api-payload-index.json
└── retired/
    └── <release_id>/
```

Suggested deterministic file name:

```text
soil.published.api_payload.<payload_family>.<scope>.<release_id>.<short_hash>.json
```

This layout is PROPOSED until validated by contracts, schemas, fixtures, and release tooling.

[Back to top](#top)

---

## 8. Maintenance checklist

Before adding or changing a payload under this lane, verify:

- [ ] The payload is release-approved and public-safe for the intended audience.
- [ ] The release record points to this payload.
- [ ] Evidence, catalog, validation, policy, review, correction, and rollback refs are present where required.
- [ ] Source role, support type, evidence support, units, time scope, caveats, and public-safe posture are preserved.
- [ ] The payload does not duplicate upstream, proof, receipt, catalog, schema, contract, policy, or release authority.
- [ ] The payload has a digest or integrity reference.
- [ ] Public clients consume it through governed interfaces or approved released artifact paths.

[Back to top](#top)

---

## 9. Definition of done

This lane is operationally mature when:

- [ ] `data/published/api_payloads/README.md` defines the parent API-payload published-data contract.
- [ ] Soil API payload contracts and schemas exist under approved homes.
- [ ] Release tooling writes or verifies payloads only after release authority is present.
- [ ] Validators block missing evidence, missing release refs, missing rollback, support-type collapse, source-role collapse, missing review state, and unsafe public payload fields.
- [ ] Valid and invalid fixtures cover endpoint, Evidence Drawer, Focus Mode, map popup, public summary, correction, supersession, and rollback payloads.
- [ ] Governed API or released-artifact routes are documented and tested.

---

## Maintainer note

Published Soil API payloads should be compact, citable, public-safe, support-type-aware, caveat-rich, and reversible. If evidence, validation, policy, release, correction, or rollback support is incomplete, keep the payload upstream instead of placing it here.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/published/hazards/readme
title: data/published/hazards README
type: directory-readme
version: v0.1
status: draft
owners:
  - TODO(owner): data steward
  - TODO(owner): hazards domain steward
  - TODO(owner): publication steward
  - TODO(owner): release steward
created: 2026-06-26
updated: 2026-06-26
policy_label: public-review
path: data/published/hazards/README.md
related:
  - ../README.md
  - ../../README.md
  - ../../raw/hazards/README.md
  - ../../work/hazards/README.md
  - ../../quarantine/hazards/README.md
  - ../../processed/hazards/README.md
  - ../../catalog/domain/hazards/README.md
  - ../../triplets/hazards/README.md
  - ../../proofs/hazards/README.md
  - ../../proofs/validation_report/hazards/README.md
  - ../../receipts/README.md
  - ../../../release/README.md
  - ../../../docs/domains/hazards/ARCHITECTURE.md
  - ../../../docs/domains/hazards/DATA_LIFECYCLE.md
  - ../../../docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md
  - ../../../docs/domains/hazards/LIFE_SAFETY_BOUNDARY.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/doctrine/lifecycle-law.md
  - ../../../docs/doctrine/trust-membrane.md
  - ../../../contracts/README.md
  - ../../../schemas/README.md
  - ../../../policy/README.md
notes:
  - "Directory README for released Hazards carriers. It replaces a greenfield stub."
  - "This path is downstream of release decisions and does not itself approve release, define schemas, define policy, or prove claims."
  - "Hazards published carriers are analysis and resilience context, not emergency alerts, life-safety instructions, or regulatory determinations."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/published/hazards/`

> Published Hazards lane for released, public-facing Hazards carriers that have passed KFM release gates and are safe for governed API, approved released-artifact, map, report, export, timeline, or UI use.

![Status: draft](https://img.shields.io/badge/status-draft-orange)
![Lifecycle: PUBLISHED](https://img.shields.io/badge/lifecycle-PUBLISHED-2ea44f)
![Domain: hazards](https://img.shields.io/badge/domain-hazards-b91c1c)
![Boundary: not alert authority](https://img.shields.io/badge/boundary-not--alert--authority-critical)
![Authority: not release](https://img.shields.io/badge/authority-not--release-b91c1c)
![Publication: release gated](https://img.shields.io/badge/publication-release--gated-blue)
![Truth: cite or abstain](https://img.shields.io/badge/truth-cite--or--abstain-6f42c1)

> [!IMPORTANT]
> **Status:** `draft`  
> **Owners:** `TODO(owner): data steward` · `TODO(owner): hazards domain steward` · `TODO(owner): publication steward` · `TODO(owner): release steward`  
> **Path:** `data/published/hazards/README.md`  
> **Truth posture:** CONFIRMED target path and Hazards domain/lifecycle/publication-boundary docs from current repo evidence / PROPOSED child layout and instance naming / NEEDS VERIFICATION for emitted artifacts, release manifests, schemas, validators, CI checks, and governed API routes.

> [!WARNING]
> This directory is not release authority and is not an emergency-alert surface. Placement here must follow release records, evidence support, validation, policy review, catalog closure, correction path, and rollback support. If that support is incomplete, keep the artifact upstream.

---

## Quick jumps

| Section | Use it for |
|---|---|
| [1. Scope](#1-scope) | What this published lane is for. |
| [2. Repo fit](#2-repo-fit) | How this path relates to lifecycle and authority roots. |
| [3. Accepted artifacts](#3-accepted-artifacts) | What may live here after release. |
| [4. Exclusions](#4-exclusions) | What must stay out. |
| [5. Release checks](#5-release-checks) | Minimum checks before adding files. |
| [6. Hazards boundary rules](#6-hazards-boundary-rules) | Non-alert and source-role guardrails. |
| [7. Suggested layout](#7-suggested-layout) | Proposed child structure and naming. |
| [8. Definition of done](#8-definition-of-done) | What remains before maturity. |

---

## 1. Scope

`data/published/hazards/` is the Hazards domain's published carrier lane. It is downstream of release and should contain only public-facing artifacts that have already passed KFM promotion gates.

This lane may hold released carriers such as:

- historical hazard-context map layers;
- regulatory-context map layers;
- observation or detection summaries;
- model or indicator context products;
- public timelines and resilience summaries;
- API payload snapshots;
- report carriers;
- export or GeoParquet packages;
- public index manifests; and
- retired or superseded public artifacts with correction, withdrawal, or rollback references.

This lane should not contain raw source captures, working candidates, held material, processed candidates, catalog drafts, proof objects, receipts, policy logic, release decisions, schemas, semantic contracts, live alerting workflows, emergency instructions, regulatory determinations, or unreleased model/AI outputs.

[Back to top](#top)

---

## 2. Repo fit

| Neighbor | Role | Boundary |
|---|---|---|
| [`../../raw/hazards/`](../../raw/hazards/) | Source captures. | Not public-readable. |
| [`../../work/hazards/`](../../work/hazards/) | Working candidates. | Not public-readable. |
| [`../../quarantine/hazards/`](../../quarantine/hazards/) | Held material. | Not public-readable. |
| [`../../processed/hazards/`](../../processed/hazards/) | Validated candidates. | Upstream of release. |
| [`../../catalog/domain/hazards/`](../../catalog/domain/hazards/) | Catalog records. | Discovery and lineage, not release authority. |
| [`../../triplets/hazards/`](../../triplets/hazards/) | Graph projection. | Not public by itself. |
| [`../../proofs/hazards/`](../../proofs/hazards/) | Proof support. | Support, not published carrier. |
| [`../../proofs/validation_report/hazards/`](../../proofs/validation_report/hazards/) | Validation reports. | Gate support, not publication authority. |
| [`../../receipts/`](../../receipts/) | Process memory. | Receipts do not publish. |
| [`../../../release/`](../../../release/) | Release authority. | Manifests, correction, withdrawal, rollback, signatures. |
| [`../../../contracts/`](../../../contracts/) | Semantic meaning. | Published artifacts conform; they do not define meaning. |
| [`../../../schemas/`](../../../schemas/) | Machine shape. | Published artifacts validate; schemas live elsewhere. |
| [`../../../policy/`](../../../policy/) | Admissibility. | Published artifacts carry outcomes; policy lives elsewhere. |

[Back to top](#top)

---

## 3. Accepted artifacts

| Artifact type | Suggested placement | Required support |
|---|---|---|
| Released map carrier | `layers/<release_id>/<layer_slug>.*` | Release, evidence, validation, policy, rollback refs. |
| Released API payload | `api_payloads/<release_id>/<payload_slug>.json` | Schema validation, release refs, correction path. |
| Released report carrier | `reports/<release_id>/<report_slug>.md` or `.json` | Citations, evidence refs, release refs. |
| Released export package | `exports/<release_id>/<export_slug>.*` | Schema/version, audience class, release refs. |
| Released timeline package | `timelines/<release_id>/<timeline_slug>.*` | Evidence refs, temporal scope, release refs. |
| Released public summary | `public_summaries/<release_id>/<summary_slug>.json` | Public-facing posture, evidence refs. |
| Released public index | `indexes/published-hazards-index.json` | Points to release-approved artifacts only. |
| Retired public artifact | `retired/<release_id>/<artifact_slug>.*` | Supersession, correction, withdrawal, or rollback reference. |

[Back to top](#top)

---

## 4. Exclusions

| Excluded material | Correct home |
|---|---|
| Source payloads or source-system dumps | `data/raw/hazards/` |
| Working or held candidates | `data/work/hazards/` or `data/quarantine/hazards/` |
| Processed normalized data | `data/processed/hazards/` |
| Catalog records | `data/catalog/` |
| Proof objects or validation reports | `data/proofs/` |
| Receipts | `data/receipts/` |
| Release records and decisions | `release/` |
| Policy logic | `policy/` |
| Schemas | `schemas/` |
| Semantic contracts | `contracts/` |
| Live alerting, emergency instruction, or official determination surfaces | Outside KFM published carrier authority. |
| Direct model output or unreviewed AI summaries | Governed review paths before release. |

[Back to top](#top)

---

## 5. Release checks

Before adding or changing files here, verify:

- [ ] release authority exists under `release/`;
- [ ] evidence refs resolve for consequential claims;
- [ ] validation reports passed or recorded finite outcomes;
- [ ] catalog closure exists;
- [ ] policy state allows the target audience;
- [ ] source role and knowledge character are preserved;
- [ ] freshness, effective date, expiry date, or stale-state posture is recorded where material;
- [ ] correction and rollback paths are recorded;
- [ ] digests or integrity refs bind the artifact to the release record; and
- [ ] public clients consume the artifact only through governed interfaces or approved released-artifact paths.

[Back to top](#top)

---

## 6. Hazards boundary rules

| Rule | Public posture |
|---|---|
| Not alert authority | Published Hazards files are analysis and context carriers, not emergency alerts. |
| Not life-safety instruction | KFM surfaces must not replace official emergency or safety sources. |
| Not regulatory authority | Regulatory-context layers cite issuing authorities; KFM does not become the issuing body. |
| Source role is preserved | Historical, regulatory, observed, modeled, administrative, and derived roles must not collapse. |
| Time state is visible | Issue, effective, expiry, observation, retrieval, release, stale, and correction times are preserved where material. |
| Evidence is mandatory | Claims require evidence support and citation posture. Missing support means abstain or hold. |
| Cross-lane truth stays owned | Hydrology, Atmosphere, Geology, Infrastructure, Roads, Soil, Agriculture, Archaeology, People/Land, Flora, Fauna, and Habitat keep their own truth. |
| AI is not root truth | AI summaries can consume released evidence but cannot replace EvidenceBundles, validation, release, or citations. |
| Corrections are expected | Public artifacts must support correction, supersession, withdrawal, and rollback. |

[Back to top](#top)

---

## 7. Suggested layout

```text
data/published/hazards/
├── README.md
├── layers/
│   └── <release_id>/
├── api_payloads/
│   └── <release_id>/
├── reports/
│   └── <release_id>/
├── exports/
│   └── <release_id>/
├── timelines/
│   └── <release_id>/
├── public_summaries/
│   └── <release_id>/
├── indexes/
│   └── published-hazards-index.json
└── retired/
    └── <release_id>/
```

Suggested deterministic file name:

```text
hazards.published.<artifact_family>.<scope>.<release_id>.<short_hash>.<ext>
```

This layout is PROPOSED until validated by contracts, schemas, fixtures, and release tooling.

[Back to top](#top)

---

## 8. Definition of done

This lane is operationally mature when:

- [ ] `data/published/README.md` defines the parent published-data contract.
- [ ] Hazards published artifact contracts and schemas exist under approved homes.
- [ ] Release tooling writes or verifies Hazards published artifacts only after release authority is present.
- [ ] Validators block unreleased candidates, missing evidence, missing release refs, missing rollback, source-role collapse, stale-state ambiguity, alert-authority collapse, unsafe public carriers, and missing correction path.
- [ ] Valid and invalid fixtures cover map, API payload, report, export, timeline, public summary, corrected release, superseded release, and rollback target.
- [ ] Governed API or released-artifact routes are documented and tested.

---

## Maintainer note

Published Hazards artifacts are public-facing carriers, not emergency systems. Keep them citable, source-role-aware, time-aware, release-linked, correction-ready, and reversible. If release support is incomplete, keep the artifact upstream instead of placing it here.

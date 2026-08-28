<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/domains/agriculture/readme
title: Agriculture · Domain Lane README
type: readme
version: v0.3
status: draft; repository-grounded; documentation-only; non-authoritative; non-publisher
owners: ["@bartytime4life — verified GitHub review route only"]
created: 2026-05-15
updated: 2026-08-28
policy_label: public
owning_root: docs/
responsibility: Human-readable scope, boundaries, repository fit, source-role separation, safety posture, and navigation for the Agriculture domain lane
truth_posture: "CONFIRMED current repository paths and accepted Directory Rules placement / PARTIAL mixed implementation maturity and validation surfaces / UNKNOWN source admission, production retrieval, accountable stewardship, independent review, release, deployment, promotion, publication, and source-by-source rights until separately verified"
related: [docs/domains/README.md, docs/doctrine/directory-rules.md, docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md, docs/runbooks/agriculture/, contracts/domains/agriculture/, schemas/contracts/v1/domains/agriculture/, policy/domains/agriculture/, fixtures/domains/agriculture/, tests/domains/agriculture/, tools/validators/agriculture/, packages/domains/agriculture/, pipelines/domains/agriculture/, data/registry/sources/agriculture/, release/candidates/agriculture/]
tags: [kfm, domain, agriculture, governance, evidence, public-safe]
notes: ["Repository paths inspected at main@d0816eed65852b22577b9003e86159fd48f134df; the April 2026 Agriculture implementation dossier remains read-only design lineage; repository presence does not establish source admission, review, runtime use, release, deployment, promotion, or publication."]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# 🌾 Agriculture · Domain Lane

> Repository-grounded orientation for KFM agricultural observations, aggregate statistics, remote-sensing derivatives, agronomic interpretations, and public-safe cross-lane context. It is not a private farm-management system and does not authorize source admission, production retrieval, release, or publication.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![authority: explanatory](https://img.shields.io/badge/authority-explanatory-blue)
![implementation: repository grounded](https://img.shields.io/badge/implementation-repository__grounded-blue)
![sensitivity: aggregate default](https://img.shields.io/badge/public-aggregate__default-green)
![last reviewed: 2026--08--28](https://img.shields.io/badge/last%20reviewed-2026--08--28-blue)

**Status:** `draft; repository-grounded; documentation-only` · **Authority level:** explanatory and subordinate to current repository controls · **GitHub review route:** `@bartytime4life` via default CODEOWNERS · **Domain stewardship and independent review:** `NEEDS VERIFICATION` · **Updated:** 2026-08-28

> [!IMPORTANT]
> The May-era version of this README was authored under a no-mounted-repository assumption and labeled implementation-shaped paths `PROPOSED` or `UNKNOWN`. That assumption is historical lineage, not the current repository state. Current GitHub contains established Agriculture responsibility-root lanes. Their presence does **not** by itself prove source admission, runtime behavior, evidence closure, review, release, deployment, promotion, or publication.

---

## Contents

1. [Purpose](#1-purpose)
2. [Authority and status](#2-authority-and-status)
3. [Responsibility boundary](#3-responsibility-boundary)
4. [Current repository fit](#4-current-repository-fit)
5. [Source-role separation](#5-source-role-separation)
6. [Lifecycle and evidence law](#6-lifecycle-and-evidence-law)
7. [Rights, privacy, and public-safety posture](#7-rights-privacy-and-public-safety-posture)
8. [Cross-lane relations](#8-cross-lane-relations)
9. [Validation and proof surfaces](#9-validation-and-proof-surfaces)
10. [Maturity and hold semantics](#10-maturity-and-hold-semantics)
11. [Design lineage](#11-design-lineage)
12. [Open verification items](#12-open-verification-items)
13. [What this README does not authorize](#13-what-this-readme-does-not-authorize)
14. [Last reviewed](#last-reviewed)

---

## 1. Purpose

This folder is the human-facing documentation lane for KFM Agriculture. It explains current repository placement, responsibility boundaries, evidence posture, source roles, public-safety constraints, and where enforceable behavior lives.

Agriculture may represent or derive agricultural observations and public-safe products such as crop observations, aggregate crop statistics, vegetation-index observations, soil-crop context, irrigation context, conservation context, stress indicators, and agricultural-economy aggregates. Exact object semantics remain governed by the current contracts, schemas, policies, fixtures, validators, tests, and downstream release objects rather than by this README.

This README is therefore an **orientation surface**, not sovereign evidence and not an implementation registry. Where current repository bytes conflict with historical prose, current repository evidence and accepted governance control the implementation claim.

[↑ Back to top](#top)

---

## 2. Authority and status

The current authority order for Agriculture implementation claims is:

1. Current GitHub repository evidence at an exact commit or PR head: files, contracts, schemas, policies, validators, fixtures, tests, workflows, receipts, proofs, lifecycle objects, and release objects.
2. Accepted unsuperseded ADRs and the adopted Directory Rules. ADR-0029 accepts the current Directory Rules v2 bytes at `docs/doctrine/directory-rules.md`.
3. Current authoritative repository documentation.
4. Notion coordination state.
5. Google Drive doctrine, research, source dossiers, and design lineage.
6. Current official primary sources when version-sensitive rights, terms, endpoints, standards, or security behavior require external verification.

The old README's no-mounted-repository posture is superseded for current path-existence claims. It does not become evidence merely because it was repeated in a dossier, task page, generated summary, dashboard, tile, graph projection, or model output.

| Aspect | Current posture |
|---|---|
| Documentation placement | **CONFIRMED** at `docs/domains/agriculture/` under the accepted Directory Rules responsibility model. |
| Agriculture responsibility-root lanes | **CONFIRMED PRESENT / MATURITY MIXED**. See §4. |
| Contracts, schemas, fixtures, tests, policy, validators | **CONFIRMED PRESENT / BEHAVIOR BOUNDED BY THEIR OWN EVIDENCE**. Presence is not acceptance or runtime proof. |
| Package and pipeline surfaces | **CONFIRMED PRESENT / MATURITY MIXED**. Small or placeholder implementations must not be described as production-ready without exact evidence. |
| Source descriptors | **CONFIRMED PRESENT / NOT SOURCE ADMISSION**. Registry bytes document candidate or governed source state; they do not activate retrieval. |
| Release-candidate surface | **CONFIRMED PRESENT / NOT RELEASE**. Directory presence does not establish a governed transition. |
| Production retrieval and live source execution | **UNKNOWN / NOT INFERRED**. |
| Public release, deployment, promotion, publication | **UNKNOWN / NOT INFERRED**. |
| Accountable Agriculture stewardship and independent review | **NEEDS VERIFICATION**. Default CODEOWNERS routing is a review route, not proof of specialist authority. |

[↑ Back to top](#top)

---

## 3. Responsibility boundary

Agriculture owns agricultural-domain observations, derived indicators, aggregate statistics, and agronomic interpretations only where current contracts and policy establish that ownership. It may cite or join governed outputs from adjacent domains but must not absorb their canonical truth.

| Concern | Canonical owner | Agriculture rule |
|---|---|---|
| Soil map units, components, horizons, MUKEY semantics, soil source authority | **Soil** | Cite governed Soil outputs; do not redefine soil truth. |
| Streamflow, gauges, water observations, flood context, hydrologic source authority | **Hydrology** | Use as bounded input/context only. |
| Weather, climate, smoke, atmospheric observations or forecasts | **Atmosphere** | Use atmospheric evidence as input/context; do not restate it as Agriculture-owned observation truth. |
| Drought and other hazard-event semantics | **Hazards** | Agriculture may derive crop/stress context without becoming the hazard-event authority. |
| Plant taxonomy and sensitive botanical occurrences | **Flora** | Do not duplicate taxonomy or expose sensitive Flora geometry. |
| Parcels, ownership, living-person privacy, restricted person-land relations | **People-DNA-Land** | Person-parcel or operator-linked joins remain restricted by default. |

Agriculture-specific public-safe joins must preserve the source domain's provenance, temporal semantics, sensitivity, and correction path.

[↑ Back to top](#top)

---

## 4. Current repository fit

Accepted Directory Rules treat a domain as a scope segment inside responsibility roots, not as a new top-level authority root. Agriculture therefore reuses the established repository homes below.

| Responsibility root | Current Agriculture lane | Repository-grounded posture |
|---|---|---|
| Human documentation | `docs/domains/agriculture/` | Present; this README is explanatory. |
| Operational documentation | `docs/runbooks/agriculture/` | Present; runbooks remain subordinate to executable controls and exact-head evidence. |
| Semantic contracts | `contracts/domains/agriculture/` | Present; meaning carriers exist. |
| Machine-checkable schemas | `schemas/contracts/v1/domains/agriculture/` | Present; shape carriers exist under the accepted schema responsibility root. |
| Policy | `policy/domains/agriculture/` | Present; admissibility/public-safety policy remains authoritative only within its defined scope. |
| Deterministic fixtures | `fixtures/domains/agriculture/` | Present; includes positive and negative proof material. |
| Domain tests | `tests/domains/agriculture/` | Present; exact coverage must be verified per changed seam. |
| Validators | `tools/validators/agriculture/` | Present; do not create a parallel `tools/validators/domains/agriculture/` home. |
| Shared package code | `packages/domains/agriculture/` | Present; package existence does not establish production use. |
| Pipeline code | `pipelines/domains/agriculture/` | Present; current files include ingest/normalize/validate/catalog/triplet/publish/rollback surfaces, but individual maturity remains evidence-bounded. |
| Source registry | `data/registry/sources/agriculture/` | Present; registry descriptors are governance evidence, not automatic admission or activation. |
| Release candidates | `release/candidates/agriculture/` | Present; candidate presence is not release, deployment, promotion, or publication. |

Other Agriculture lanes may exist under catalog, lifecycle, receipt, proof, layer-registry, or workflow homes. Their existence and maturity must be checked at the exact head before making a positive claim. This README intentionally avoids creating a duplicate inventory authority.

[↑ Back to top](#top)

---

## 5. Source-role separation

Agriculture must preserve the role of each source family instead of collapsing all inputs into generic "field truth".

| Source family | Role boundary |
|---|---|
| **SSURGO / Soil Data Access** | Vector/tabular soil authority remains with Soil; Agriculture consumes governed soil context rather than redefining it. |
| **gSSURGO** | Derived gridded companion; not interchangeable with SSURGO tabular/vector source authority. |
| **Kansas Mesonet / NRCS SCAN / NOAA USCRN** | Station observations with source-specific spatial, temporal, quality, rights, and caveat semantics. |
| **NASA SMAP** | Satellite/grid soil-moisture product; not field truth and not a substitute for governed in-situ observations. |
| **NASA HLS / HLS-VI** | Remote-sensing observations and derived vegetation indices; derived indices remain interpretations of sensor observations rather than operator records. |
| **USDA NASS QuickStats / Crop Progress** | Aggregate official statistics; not field polygons, private farm records, or operator-level observations. |

Normalized observations, classifications, forecasts, models, aggregates, interpretations, and derived stress indicators must remain distinguishable in contracts, evidence, and public presentation. A tile, index, graph, summary, model result, or generated explanation is not sovereign evidence.

[↑ Back to top](#top)

---

## 6. Lifecycle and evidence law

Agriculture follows the repository lifecycle:

`RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED`

A lifecycle transition is governed state, not a directory move. Path presence cannot substitute for admission, validation, proof, review, release, correction, rollback, or publication authority.

Public or generated claims must retain evidence lineage. `EvidenceBundle` and its governed evidence references outrank generated language, renderer state, search indexes, dashboard projections, graph projections, or model output. AI may interpret governed evidence; it must not create source authority or silently convert uncertainty into a factual Kansas agriculture claim.

Receipts record execution or transformation facts within their defined scope. A receipt is not, by itself, proof, review, source admission, promotion, release, deployment, or publication authority.

[↑ Back to top](#top)

---

## 7. Rights, privacy, and public-safety posture

Agriculture is rights- and privacy-sensitive. The public default is aggregate or sufficiently generalized output, not farm-operator detail.

Deny by default unless explicit current policy, rights, sensitivity review, transformation evidence, release state, and rollback/correction authority establish otherwise:

- field polygons or reconstructable private field geometry;
- operator or farm identities;
- proprietary yield or farm-management data;
- pesticide or application records where rights or sensitivity are unresolved;
- person-parcel or operator-parcel joins;
- precise private wells or sensitive infrastructure;
- any source whose redistribution, automation, quota, licensing, or privacy terms remain unknown.

Public products should prefer reviewed county, HUC, or sufficiently generalized grid outputs. Field-level or operator-level exposure requires a separately governed decision; this README does not grant it.

Unknown terms or permissions produce `HOLD`, `DENY`, or `ABSTAIN`, not optimistic ingestion.

[↑ Back to top](#top)

---

## 8. Cross-lane relations

Cross-lane Agriculture products should be built as governed joins rather than ownership transfers. A join must preserve:

- the owning lane for each canonical input;
- evidence references and source role;
- temporal and spatial compatibility;
- units and aggregation semantics;
- sensitivity and redaction/generalization state;
- correction, supersession, and rollback paths;
- public-path policy where an output becomes externally visible.

Typical bounded relationships include Agriculture ↔ Soil suitability context, Agriculture ↔ Atmosphere stress/forcing context, Agriculture ↔ Hydrology irrigation/water context, Agriculture ↔ Hazards drought context, Agriculture ↔ Flora vegetation/taxonomy context, and Agriculture ↔ People-DNA-Land parcel/privacy constraints. None of these joins authorizes Agriculture to become the canonical owner of the adjacent lane's facts.

[↑ Back to top](#top)

---

## 9. Validation and proof surfaces

Repository-grounded validation currently has multiple Agriculture surfaces, including domain validators, deterministic fixtures/tests, Agriculture-specific workflows, observation contracts, NDVI/HLS materiality work, EvidenceBundle convergence, vegetation connectivity, and Soil-Agriculture public-safe context work.

For any change, use the narrowest repository-native proof surface that covers the changed behavior. Trust-bearing behavior should include a negative test when practical. Validation claims must bind to the exact tested head and distinguish:

`PASS` · `FAIL` · `SKIPPED` · `NOT_RUN` · `CANCELLED` · `STARTUP_FAILURE` · environmental · unknown · pending

Do not infer a hosted check result from path existence. Do not infer production readiness from a deterministic fixture. Do not infer public safety from a passing schema validator alone.

Primary navigation points:

- `tools/validators/agriculture/`
- `tests/domains/agriculture/`
- `fixtures/domains/agriculture/`
- `docs/runbooks/agriculture/`
- `.github/workflows/` for the current Agriculture-related workflow definitions

[↑ Back to top](#top)

---

## 10. Maturity and hold semantics

The Agriculture lane is **implemented in substantial repository surfaces but mixed in maturity**. That is intentionally different from both of these incorrect extremes:

- **Incorrect:** "Agriculture is only proposed because no repository has been inspected."
- **Incorrect:** "Agriculture is production-ready because contracts, schemas, pipelines, source descriptors, or release-candidate folders exist."

A positive readiness statement requires exact current evidence for the specific seam: producer, consumer, contract/schema compatibility, policy, deterministic proof, negative proof where trust-bearing, rights/sensitivity state, correction/rollback path, review, and any applicable release/publication transition.

Source admission, production retrieval, release, deployment, promotion, and publication remain separately governed states.

[↑ Back to top](#top)

---

## 11. Design lineage

The **KFM Agriculture Domain Implementation Dossier — Revised 2026-04-21** remains useful read-only design lineage for source families, candidate object concepts, privacy posture, and cross-domain ideas. It explicitly came from a period where the live repository was not mounted for verification.

Use the dossier to generate questions and candidate work, not to override current GitHub placement, contracts, schemas, policies, tests, workflow behavior, issue state, or release state. Proposal text repeated in Notion or generated summaries does not become implementation authority.

The prior README revision from May 2026 is likewise historical design lineage where it depended on the no-mounted-repository assumption.

[↑ Back to top](#top)

---

## 12. Open verification items

Before making broader Agriculture readiness claims, verify only the currently relevant seam. Common open questions include:

- exact workflow inventory and current hosted status at the selected head;
- completeness of contract → schema → fixture → validator → test bindings for a chosen object family;
- negative coverage for source-role anti-collapse and public-safe aggregation;
- EvidenceBundle projection and current consumers;
- Soil-Agriculture and Agriculture-Atmosphere/Hydrology compatibility boundaries;
- correction, supersession, rollback, and release-manifest closure;
- source-by-source rights, redistribution, quota, automation, and privacy terms;
- accountable Agriculture stewardship and independent review route;
- current public-path consumers, if any, and their release evidence.

These are verification targets, not permission to scaffold parallel responsibility roots or activate live sources.

[↑ Back to top](#top)

---

## 13. What this README does not authorize

This document does **not** authorize or prove:

- source admission or activation;
- live or production data retrieval;
- field/operator-sensitive exposure;
- acceptance of a proposed ADR;
- policy approval or independent review;
- promotion, release, deployment, or publication;
- readiness of a package, pipeline, workflow, public API, map layer, or generated interpretation;
- repository settings, permission, secret, environment, or branch-protection changes.

Those states remain governed by their owning repository controls and human review boundaries.

[↑ Back to top](#top)

---

<a id="last-reviewed"></a>

## Last reviewed

**2026-08-28** — Repository-grounded against `main@d0816eed65852b22577b9003e86159fd48f134df`. Reconciled the stale no-mounted-repository / blanket-`PROPOSED` posture with current Agriculture responsibility-root surfaces while preserving explicit holds around source admission, rights, sensitive data, runtime use, review, release, deployment, promotion, and publication.

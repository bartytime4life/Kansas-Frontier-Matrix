<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/fauna/ebd-derivative-release
title: Fauna — eBird Basic Dataset Derivative Release Runbook
type: runbook; operational-procedure; restricted-source; pre-publication; non-authoritative
version: v1.0
prior_version: PROPOSED scaffold
status: draft; repository-grounded; rights-sensitive; release-held; non-publisher
owners:
  - "@bartytime4life — verified GitHub review route only"
owner_status: >-
  Fauna, eBird/EBD source, rights, sensitivity, privacy, scientific-method,
  evidence, policy, release, independent-review, and operations assignments
  remain NEEDS VERIFICATION; CODEOWNERS routing does not create those authorities.
created: NEEDS VERIFICATION — the prior scaffold carried no creation date
updated: 2026-08-24
policy_label: public-review; fauna; ebird; ebd; derivative-release; restricted-source; fail-closed; no-publication-authority
current_path: docs/runbooks/fauna/EBD_DERIVATIVE_RELEASE.md
owning_root: docs/
responsibility: >-
  Document how an authorized KFM reviewer should classify, validate, and hand off
  a proposed derivative of the eBird Basic Dataset without redistributing source
  data, weakening the approved-purpose boundary, exposing sensitive or
  observer-linked information, overstating sampling support, or confusing a
  candidate, test, receipt, pull request, or merge with release or publication.
truth_posture: cite-or-abstain
truth_labels: [CONFIRMED, PROPOSED, UNKNOWN, NEEDS VERIFICATION, CONFLICTED, HOLD]
authority_class: explanatory operational documentation
canonical_relationship: same-path modernization; no new or parallel authority
prepared_under_prompt: KFM Repository Build-Out & Markdown Modernization Implementation Agent v6.0.0
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 67e1e2c698dff941b689dba35cfc968ac573a5af
  target_prior_blob: 61c177019167f891bf747314f54af45f59cd260d
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  parent_runbook_index_blob: 80f53b61d485c25acdb55eaa01129e13e63ca90e
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  fauna_source_families_blob: 137568eb5a81480813fc318f7a645f36d245adbe
  ebd_terms_policy_blob: 66055a17f8aee20dab54f564ea93b2cfd2988e7b
  ebird_redistribution_policy_blob: a22b9ae2ddd35ff899634640ee90676d0ef83277
  rare_species_policy_blob: a7269d357bb7570fc3680c299486e5d62cb33a68
  ebird_registry_candidate_blob: 7c780152759f812c4e6e9128f2b50212ec545b33
  fauna_candidate_index_blob: 653277efe3a44a96c29af481a73d7d90c41443ce
  fauna_domain_workflow_blob: 0edc73a77ee0ddb3193db2c0386ed6ac685b139a
  occurrence_retrieval_contract_blob: ab145d3c22bc7152c3eae0219f9081f1edc75601
  occurrence_retrieval_workflow_blob: d25591809843134492ee42a18d5aceb5a94ff0b0
external_authority_snapshot:
  checked_at: 2026-08-24
  authority: Cornell Lab of Ornithology / eBird official pages
  checked_surfaces:
    - https://www.birds.cornell.edu/home/ebird-data-access-terms-of-use/
    - https://support.ebird.org/en/support/solutions/articles/48001078113-ebird-data-privacy-and-data-use
    - https://support.ebird.org/en/support/solutions/articles/48000838205-download-ebird-data
    - https://support.ebird.org/en/support/solutions/articles/48000803210-sensitive-species-in-ebird
inspection_boundary: >-
  Current-session GitHub reads covered the target scaffold, accepted Directory
  Rules decision, parent runbook index, CODEOWNERS, Fauna source and release
  documentation, eBird connector and RAW boundaries, source registry candidate,
  rights and sensitivity policy scaffolds, current Fauna candidate and workflow
  holds, synthetic Fauna fixture validation, and the occurrence-retrieval
  snapshot profile. Official Cornell/eBird pages were checked for current
  source-product and terms guidance. Repository-native commands were not run in
  a mounted checkout during authoring. No eBird data were accessed, copied,
  transformed, released, deployed, promoted, or published.
related:
  - ../README.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../domains/fauna/SOURCES.md
  - ../../domains/fauna/SOURCE_FAMILIES.md
  - ../../domains/fauna/SENSITIVITY.md
  - ../../domains/fauna/RELEASE_INDEX.md
  - ../../sources/catalog/ebird/ebird-basic-dataset.md
  - ../../sources/catalog/ebird/sampling-event-data.md
  - ./SOURCE_REFRESH_RUNBOOK.md
  - ./PROMOTION_RUNBOOK.md
  - ./ROLLBACK_RUNBOOK.md
  - ../../../data/registry/fauna/sources/ebird.yaml
  - ../../../data/raw/fauna/ebird/README.md
  - ../../../policy/rights/fauna/ebd_terms.yaml
  - ../../../policy/domains/fauna/ebird_redistribution.md
  - ../../../policy/domains/fauna/rare_species_redaction.rego
  - ../../../release/candidates/fauna/README.md
  - ../../../release/manifests/fauna/README.md
  - ../../../contracts/source/occurrence_retrieval_snapshot.md
  - ../../../tests/domains/fauna/test_fauna_smoke.py
  - ../../../.github/workflows/domain-fauna.yml
  - ../../../.github/workflows/occurrence-retrieval-snapshot.yml
tags: [kfm, fauna, ebird, ebd, sed, derivative, release, rights, sensitivity, geoprivacy, no-network, governance]
notes:
  - "v1.0 replaces the inventory-generated placeholder with a repository-grounded, rights-sensitive review and release-handoff procedure."
  - "The document deliberately does not invent an EBD release command, candidate, policy decision, manifest, source admission, or published artifact."
  - "At the evidence snapshot, EBD rights, redistribution, source-registry, sensitivity-policy, candidate, proof, and release-dry-run closure remain held."
  - "The exact access agreement and supporting metadata accepted for a particular EBD download outrank this explanatory runbook."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Fauna — eBird Basic Dataset Derivative Release Runbook

> **Classify, validate, and hand off a proposed eBird Basic Dataset derivative without redistributing source data, exposing sensitive or observer-linked information, overstating scientific support, or turning documentation and CI into release authority.**

<p>
  <img alt="Status: repository-grounded draft" src="https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b">
  <img alt="Source: eBird Basic Dataset" src="https://img.shields.io/badge/source-eBird%20EBD-1f6feb">
  <img alt="Rights: purpose-bound" src="https://img.shields.io/badge/rights-purpose--bound-b42318">
  <img alt="Sensitivity: fail closed" src="https://img.shields.io/badge/sensitivity-fail%20closed-b42318">
  <img alt="Current release: hold" src="https://img.shields.io/badge/current%20release-HOLD-d4a72c">
  <img alt="Publisher: no" src="https://img.shields.io/badge/publisher-no-6e7781">
</p>

> [!IMPORTANT]
> **Current repository result: `HOLD`.** No verified EBD derivative candidate dossier, accepted EBD rights policy, executable EBD redistribution policy, enforced rare-species redaction policy, approved EBD release manifest, or accepted Fauna release-dry-run command was found at the evidence snapshot. This runbook may produce a review handoff; it cannot make those missing authorities exist.

> [!CAUTION]
> **The agreement attached to the exact EBD access request governs.** General official terms and support pages are preflight evidence, not replacements for the terms, approved purpose, supporting metadata, restrictions, and sensitive-data conditions accepted for the actual download.

> [!WARNING]
> **Do not publish original or near-original EBD/SED rows, exact or reverse-engineerable sensitive locations, observer-linked details, or a commercial derivative without required permission.** A map cell, chart, model surface, table, API response, download, index, or AI summary can still be a redistribution or harmful-precision surface.

**Quick navigation:** [Purpose](#1-purpose-scope-and-terminal-boundary) · [Authority](#2-authority-placement-and-non-effects) · [State](#3-current-repository-state) · [Terms](#4-ebd-product-and-terms-boundary) · [Classes](#5-derivative-classes-and-default-dispositions) · [Roles](#6-roles-and-separation-of-duties) · [Preflight](#7-preconditions-and-mandatory-stop-conditions) · [Rules](#8-scientific-source-role-and-public-safety-rules) · [Procedure](#9-derivative-review-and-release-handoff-procedure) · [Validation](#10-current-executable-validation) · [Outcomes](#11-finite-outcomes-and-reason-codes) · [Handoff](#12-review-handoff-packet) · [Correction](#13-correction-withdrawal-and-rollback) · [CI](#14-hosted-ci-and-exact-head-evidence) · [Holds](#15-current-holds-and-open-verification) · [Maintenance](#16-maintenance-and-document-rollback) · [Checklist](#appendix-a-operator-checklist) · [Template](#appendix-b-review-handoff-template) · [References](#appendix-c-current-evidence-and-official-references)

---

## 1. Purpose, scope, and terminal boundary

Use this runbook when KFM has—or is asked to prepare—a table, statistic, model surface, generalized map layer, report figure, API payload, export, or other representation whose inputs include the **eBird Basic Dataset (EBD)** or companion **Sampling Event Data (SED)**.

It answers six bounded questions:

1. Is the use within the purpose approved for the exact EBD request?
2. Is the output internal, a review candidate, or proposed public material?
3. Does it preserve EBD, SED, source role, checklist support, uncertainty, and non-detection limits?
4. Does it prevent original-data redistribution, re-identification, sensitive-species exposure, and reconstruction of protected rows?
5. Are evidence, policy, review, correction, withdrawal, and rollback support complete enough for an authorized release decision?
6. What must remain `HOLD`, `DENY`, `ABSTAIN`, or `ERROR`?

### In scope

- Exact access-request identity, approved-purpose matching, terms snapshotting, and supporting-metadata review.
- Original, near-original, internal, aggregate, modeled, visual, API, export, and public-map derivative classification.
- EBD/SED pairing and checklist-event non-detection limits.
- Source-role, specimen-versus-citizen-science, taxonomic, temporal, spatial, and evidentiary anti-collapse.
- Sensitive-species, nesting/roosting/breeding, private-site, observer-privacy, and reconstruction review.
- Candidate, evidence, validation, policy, human-review, correction, withdrawal, and rollback handoff.
- Current no-network synthetic checks and their explicit limits.
- Citation, term-propagation, product-copy, and logo-permission obligations after a separately authorized release.

### Out of scope

This runbook does not request or approve EBD access; access, copy, parse, transform, or inspect EBD/SED bytes; activate the eBird connector; decide the legal meaning of an agreement; create policy, evidence, review, or release objects; choose scientific or geoprivacy thresholds; mutate lifecycle state; or release, deploy, promote, or publish anything.

### Terminal boundary

The maximum current output is:

```text
NO_ACTION
HOLD_FOR_RIGHTS
HOLD_FOR_PURPOSE
HOLD_FOR_SOURCE_ADMISSION
HOLD_FOR_SENSITIVITY
HOLD_FOR_PRIVACY
HOLD_FOR_SCIENTIFIC_SUPPORT
HOLD_FOR_EVIDENCE
HOLD_FOR_POLICY
HOLD_FOR_VALIDATION
HOLD_FOR_REVIEW
HOLD_FOR_RELEASE_TOPOLOGY
HOLD_FOR_CORRECTION_PATH
HOLD_FOR_ROLLBACK
DENY
ABSTAIN
ERROR
REVIEW_HANDOFF_READY
```

`REVIEW_HANDOFF_READY` means only that a bounded, public-safe packet is ready for authorized review.

[Back to top](#top)

---

## 2. Authority, placement, and non-effects

**Placement outcome: `PLACE` — CONFIRMED for this same-path update.**

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts [Directory Rules v2](../../doctrine/directory-rules.md). This tracked file is a human operational procedure under `docs/`, with `fauna` as a domain segment. The update creates no root, lane, alias, mirror, schema, policy, evidence, release, or publication authority.

| Concern | Owning authority | Runbook role |
|---|---|---|
| eBird product documentation | `docs/sources/catalog/ebird/` | Preserve product distinctions |
| Fauna source-role doctrine | `docs/domains/fauna/SOURCES.md`, `SOURCE_FAMILIES.md` | Preserve roles; do not redefine them |
| Source admission and exact access terms | Accepted SourceDescriptor and access-request records | Require pointers |
| Rights and redistribution | `policy/rights/` plus authorized review | Require a decision |
| Sensitivity and geoprivacy | Fauna policy plus authorized stewards | Preserve fail-closed posture |
| Shape and meaning | `schemas/`, `contracts/` | Reference accepted definitions |
| Executable proof | `tools/validators/`, `tests/`, workflows | Point to exact bounded commands |
| Evidence | EvidenceRef/EvidenceBundle and proof authorities | Require resolution |
| Candidate and release state | Accepted `release/` lanes | Route work; do not change state |
| Published carriers | `data/published/` after release | Outside this procedure |
| Public UI/API/AI | Governed interfaces using released public-safe carriers | Outside this procedure |

Following this runbook does **not** authorize EBD access, redistribution, scientific validity, source admission, evidence closure, policy evaluation, review, lifecycle promotion, release, deployment, or publication.

[Back to top](#top)

---

## 3. Current repository state

Pinned checkpoint: `main@67e1e2c698dff941b689dba35cfc968ac573a5af`.

| Surface | CONFIRMED observation | Safe conclusion |
|---|---|---|
| Target file | 656-byte inventory placeholder, blob `61c17701...` | A procedure is needed |
| Source-family reference | EBD documented as restricted-use observed citizen-science; derivative policy remains open | Rights and precision unresolved |
| eBird connector | Version `0.0.0`; fetch/admit and connector tests remain placeholders | No active verified connector |
| eBird RAW lane | Human boundary for API/EBD/SED capture | No public path; payload presence unproved |
| SourceDescriptor candidate | Role, authority, license, redistribution, sensitivity, cadence, access, citation are `TBD` | Admission not closed |
| `ebd_terms.yaml` | Placeholder | No machine-readable terms decision |
| `ebird_redistribution.md` | Placeholder | No accepted redistribution policy |
| `rare_species_redaction.rego` | No-rule stub with `default deny := false` | Fail-closed enforcement not established |
| Fauna candidate lane | Parent README only; no verified child dossier | No active EBD candidate |
| Fauna manifest lane | Draft guidance; singular/plural path question open | No accepted EBD manifest |
| `domain-fauna` workflow | Synthetic fixture suite; proof and release dry run held | Validation bounded; release held |
| Retrieval snapshot profile | Fixture-only EBD/SED/GBIF request and sampling-support validation | No live access, rights, or release |
| CODEOWNERS | `@bartytime4life` is the verified GitHub route | Routing is not substantive authority |

Current determination:

```text
source admission             = HOLD
exact access terms snapshot  = MISSING / NEEDS VERIFICATION
approved-purpose binding     = MISSING / NEEDS VERIFICATION
EBD rights policy            = PLACEHOLDER
EBD redistribution policy    = PLACEHOLDER
rare-species policy runtime  = UNENFORCED / CONFLICTED
candidate dossier            = NOT ESTABLISHED
EvidenceBundle               = NOT ESTABLISHED
PolicyDecision               = NOT ESTABLISHED
independent review           = NOT ESTABLISHED
release manifest             = NOT ESTABLISHED
release dry run              = HOLD
publication                  = NOT ESTABLISHED
```

No EBD derivative is release-ready from current repository evidence.

[Back to top](#top)

---

## 4. EBD product and terms boundary

### Product distinctions

| Surface | Meaning | Review consequence |
|---|---|---|
| EBD | Bulk observation product; each row is a species observation on a checklist | Restricted source material; preserve release and terms |
| SED | Checklist-level effort companion | Pair deliberately; a checklist is not an occurrence |
| eBird API | Limited/recent/summary access | Do not relabel as EBD |
| eBird Observational Dataset via GBIF | Occurrence-oriented redistribution with less effort metadata | Preserve upstream identity and terms |
| eBird.org charts/maps | Published visual products | Separate citation/product conditions |
| Macaulay Library media | Photos, audio, video | Separate contributor copyright/licensing |

### Current official general terms, checked 2026-08-24

Official Cornell/eBird guidance states that:

- access requires a data request identifying the user and intended purpose;
- downloaded data are for non-commercial research and education unless written permission says otherwise;
- a different use requires a new request or written approval;
- original datasets must not be passed to third parties;
- original-format eBird data must not be publicly distributed;
- passed-on derived datasets must carry the same terms;
- acknowledgement and citation are required;
- an electronic copy of published products using eBird data should be sent to eBird;
- commercial reproduction of data or derivatives requires prior written permission;
- Cornell/eBird logos require express permission;
- supporting metadata and stipulations must be followed; and
- sensitive-species access and public display carry additional restrictions.

The exact accepted agreement and project-specific correspondence outrank this summary.

### Terms evidence order

1. Exact accepted access agreement and request.
2. Project-specific written permission or restriction.
3. Supporting metadata shipped with the release.
4. Current official Data Access Terms.
5. Current official support guidance.
6. KFM documentation.
7. Memory or assumption.

### Required restricted terms snapshot

Record an immutable reference/digest for:

- request/approval ID, requester, organization, and approved purpose;
- exact EBD/SED release or download;
- agreement and supporting-metadata digests;
- request, approval, retrieval, and review times;
- sensitive-data authorization;
- allowed users/environment;
- commerciality and permission;
- citation and attribution;
- derivative-sharing and term-propagation obligations;
- published-product-copy obligation;
- logo permission;
- reviewer, expiry, revocation, and supersession state.

Do not expose confidential terms, personal data, credentials, or download locators in this public runbook or PR.

[Back to top](#top)

---

## 5. Derivative classes and default dispositions

| Class | Example | Current default |
|---|---|---|
| Original source bytes | EBD/SED archive or file | `DENY` public distribution |
| Original-format subset | Selected rows or columns | `DENY` public distribution |
| Near-original extract | Row-level export with recoverable identity/location | `DENY` public distribution |
| Internal research table | Authorized normalized/partitioned rows | `RESTRICT / HOLD` |
| Checklist-event non-detection | Paired complete-checklist EBD/SED result | `HOLD_FOR_SCIENTIFIC_SUPPORT` |
| Aggregate table | Counts, rates, richness, occupancy summary | `HOLD` |
| Generalized map layer | County/cell summary or coarsened layer | `HOLD` |
| Modeled surface | Occupancy, abundance, trend, suitability, prediction | `HOLD` |
| Static chart/figure | Report visual based on EBD | `HOLD / REVIEW` |
| API/download/tiles | Public JSON, CSV, GeoParquet, PMTiles, MVT | `HOLD` |
| Search/graph/index | Search result, triplet, vector index | `HOLD` |
| AI answer | Generated text based on EBD derivative | `HOLD` |
| Commercial product | Commercial or revenue-supporting use | `DENY` absent written permission |
| Different-purpose reuse | Use outside approved request | `DENY / HOLD` |
| Logo-branded output | Cornell/eBird logo on derivative | `DENY` absent permission |

"Derived" is not synonymous with "public-safe." Review whether repeated queries, low counts, source identifiers, time filtering, joins, tiles, downloads, models, or AI can reconstruct observations, checklists, observers, nests, roosts, private sites, or protected locations.

[Back to top](#top)

---

## 6. Roles and separation of duties

| Role | Responsibility | Current assignment |
|---|---|---|
| EBD access holder | Exact request, purpose, agreement, authorized users | `NEEDS VERIFICATION` |
| Source steward | Product identity, SourceDescriptor, provenance | `NEEDS VERIFICATION` |
| Fauna steward | Source role, taxonomy, scientific scope | `NEEDS VERIFICATION` |
| Rights reviewer | Exact agreement and permissions | `NEEDS VERIFICATION` |
| Sensitivity/privacy reviewer | Species/site risk, observer privacy, reconstruction | `NEEDS VERIFICATION` |
| Evidence reviewer | EvidenceRef-to-EvidenceBundle closure | `NEEDS VERIFICATION` |
| Validation steward | Checks, fixtures, negative polarity | `NEEDS VERIFICATION` |
| Release authority | Release-state decision | `NEEDS VERIFICATION` |
| Independent reviewer | Separation when materiality requires | `NEEDS VERIFICATION` |
| GitHub reviewer | Repository review routing | `@bartytime4life` only |

Preparing the derivative, interpreting rights, approving sensitive handling, and authorizing release must not collapse into one unreviewed action. A GitHub approval does not substitute for source-holder permission, typed policy decisions, stewardship, or release authority.

[Back to top](#top)

---

## 7. Preconditions and mandatory stop conditions

### Preconditions

- [ ] Exact repository revision and artifact digest recorded.
- [ ] No overlapping PR/migration owns the same surface.
- [ ] Exact request, purpose, agreement, release, and metadata identified.
- [ ] Commerciality explicit; written permission present when required.
- [ ] Accepted SourceDescriptor resolved.
- [ ] EBD, SED, API, GBIF/EOD, visuals, and media kept distinct.
- [ ] Purpose, audience, geography, time, taxa, fields, formats, and access declared.
- [ ] Original/near-original and reconstruction risk assessed.
- [ ] Sensitive-species, breeding/nesting/roosting, private-site, observer, and checklist risks assessed.
- [ ] Scientific support and EBD/SED pairing declared.
- [ ] Evidence, policy, review, correction, withdrawal, and rollback requirements identified.
- [ ] Logs, fixtures, reports, and PR text are public-safe.

### Mandatory stop conditions

Stop when:

- exact terms or approved purpose cannot be produced;
- the use differs from the approved purpose without approval;
- commercial/revenue use lacks written permission;
- original or near-original EBD/SED would be distributed;
- citation, term propagation, or product-copy obligations are absent;
- SourceDescriptor or rights fields remain `TBD`;
- sensitive or observer-linked exposure is possible without enforced policy/review;
- restricted sensitive data are assumed without authorization;
- source obscuration is treated as proof that all KFM outputs are safe;
- EBD presence-only data are used to claim absence;
- checklist-event non-detection is expanded beyond event support;
- citizen-science data become specimen, range, status, or regulatory truth;
- a model/aggregate lacks method, uncertainty, validation, and evidence;
- a known-invalid fixture passes or zero tests are collected;
- the fix weakens suppression, negative tests, or authority boundaries;
- a candidate record is added while current Fauna CI deliberately holds unreviewed candidates;
- a test, receipt, PR, merge, or path is described as release approval;
- correction, withdrawal, rollback, or downstream invalidation is missing;
- hosted evidence belongs to an older head.

Unknown rights, sensitivity, privacy, purpose, evidence, policy, or release state yields `HOLD`, `DENY`, or `ABSTAIN`, never temporary publication.

[Back to top](#top)

---

## 8. Scientific, source-role, and public-safety rules

### EBD and SED

- EBD observation rows and SED checklist rows have different grains.
- Pair only through source-supported checklist identity and the same declared release.
- SED effort is not an observation.
- A complete checklist may support **checklist-event non-detection** under the declared method.
- Non-detection is not county-, habitat-, season-, history-, or time-wide absence.
- Missing rows, failed transfers, filters, rejected observations, incomplete checklists, unavailable SED, or errors are not zero observations.

### Source-role anti-collapse

EBD-derived material remains citizen-science `observed` support, separate from specimen evidence, taxonomy authority, legal/conservation status, range/model truth, stewardship determinations, evidence closure, and release decisions. It must not displace specimen records merely because it offers broad coverage or effort metadata.

### Time and version

Preserve source release, observation/checklist time, review state, retrieval time, transform time, model-run time, evidence/policy/review time, release time, and correction/supersession time. Never overwrite a prior derivative in place.

### Spatial support

Keep source coordinates, eBird-obscured coordinates, checklist location, KFM generalized support, aggregate cells, regions, model grids, ranges, and map display distinct. A KFM transform requires its own review even when eBird already obscures a record.

### Sensitive species and reconstruction

Official eBird public output currently hides sensitive species at site level and uses coarse map/region treatment. That is evidence of eBird's posture, not an automatic KFM release rule.

Review:

- global, regional, seasonal, state, federal, heritage, and steward restrictions;
- nests, roosts, colonies, leks, young, breeding behavior, private/restricted sites;
- low counts and rare combinations;
- repeated queries, differencing, time narrowing, cross-lane joins;
- map tiles, API filters, exports, screenshots, search, graph, and AI leakage.

The strictest applicable source, KFM, steward, rights, and sensitivity rule governs.

### Observer privacy

Do not expose names, account/contact details, group IDs, personal-location names, private comments, checklist links/IDs that defeat generalization, raw GPS tracks, hidden-checklist state, or separately licensed media metadata without explicit authority.

### Models and aggregates

Record question, approved purpose, source release, filtered population, EBD/SED support, spatial/temporal scope, method/software, deterministic inputs, evaluation, uncertainty, sensitivity/reconstruction review, evidence, digests, correction, and rollback. Model performance does not expand rights.

[Back to top](#top)

---

## 9. Derivative review and release-handoff procedure

### Step 1 — Freeze the subject

```yaml
repository: bartytime4life/Kansas-Frontier-Matrix
base_commit: <full SHA>
candidate_head: <full SHA>
candidate_artifact_id: <stable ID>
candidate_artifact_digest: <sha256>
changed_paths: [<path>]
public_effect_requested: <none | internal | review | proposed-public>
```

Confirm no overlap and use exact immutable bytes.

### Step 2 — Bind exact terms and purpose

In a restricted record, confirm request/approval, requester, organization, purpose, agreement, release, metadata, sensitive-data authorization, commerciality, users/environment, citation, sharing conditions, product-copy requirement, and written exceptions. Missing elements yield `HOLD_FOR_RIGHTS` or `HOLD_FOR_PURPOSE`.

### Step 3 — Define derivative and audience

```yaml
derivative_class: <internal-table | aggregate | model | map-layer | chart | api | export | other>
purpose: <approved-purpose mapping>
audience: <restricted | reviewer | proposed-public>
commercial_use: <true | false | unknown>
source_products: [EBD, SED]
geography: <public-safe scope>
time_scope: <declared interval>
taxon_scope: <declared and public-safe>
row_level_output: false
source_identifier_output: false
exact_location_output: false
```

Unknown audience, commerciality, or row/location exposure is a hold.

### Step 4 — Resolve source admission and provenance

Resolve an accepted SourceDescriptor; preserve product/release identity, source role, rights, sensitivity, retrieval and content digests, EBD/SED pairing, citation, and supersession. The current `data/registry/fauna/sources/ebird.yaml` template is insufficient because authority fields are `TBD`.

### Step 5 — Assess redistribution and reconstruction

Required conclusions:

```text
original_source_bytes_exposed        = false
source_rows_exposed                  = false
near_original_extract_exposed        = false
source_identifiers_exposed           = false or explicitly approved
observer_reidentification_possible   = false or denied
sensitive_location_reconstruction    = false or denied
repeated_query_reconstruction        = false or denied
commercial_reuse_unapproved          = false
terms_propagation_defined            = true
```

An aggregate that can reconstruct protected rows remains restricted.

### Step 6 — Validate scientific support

Declare the sampling-support profile; prove same-release pairing and completeness when using SED; document filters, method, uncertainty, and limits; distinguish zero from failed/not-evaluated transfer; keep non-detection event-scoped; and prevent specimen, taxonomy, status, range, or model-role collapse. Narrow unsupported claims or return `ABSTAIN`.

### Step 7 — Review sensitivity and privacy

Review public-safe artifacts for species/site risk, observer/checklist privacy, repeated-query leakage, joins, maps, APIs, exports, indexes, graphs, screenshots, and AI. Bind the transform/review references. Current source obscuration and generic synthetic tests do not replace an operational decision.

### Step 8 — Close evidence and validation

Assemble pointers to source admission, terms review, retrieval artifacts, transforms, method/quality/uncertainty, EvidenceRefs/Bundles, validation and negative fixtures, policy, sensitivity/privacy review, correction, and rollback. Do not relabel a README, log, receipt, or workflow summary as an EvidenceBundle.

### Step 9 — Apply current blockers

At this snapshot, these blockers are automatic:

```text
EBD_SOURCE_DESCRIPTOR_UNRESOLVED
EBD_TERMS_POLICY_PLACEHOLDER
EBD_REDISTRIBUTION_POLICY_PLACEHOLDER
EBD_SENSITIVITY_POLICY_UNENFORCED
EBD_CANDIDATE_CONTRACT_MISSING
EBD_PROOF_PRODUCER_MISSING
EBD_RELEASE_DRY_RUN_HELD
EBD_RELEASE_AUTHORITY_UNASSIGNED
```

Only the owning authority can clear them.

### Step 10 — Prepare a public-safe handoff

Use [§12](#12-review-handoff-packet). Point to restricted records without copying source rows, exact geometry, observer data, confidential terms, credentials, or reversible geoprivacy parameters.

The current `domain-fauna` workflow intentionally rejects an unreviewed child candidate. Do not create `release/candidates/fauna/<candidate>/` until an accepted candidate contract and workflow update are reviewed together.

### Step 11 — Obtain separate decisions

Obtain separate source/purpose, rights, sensitivity/privacy, scientific/evidence, policy, candidate/release, and release-authority decisions. One untyped "approved" comment is insufficient.

### Step 12 — Hand off, then stop

The authorized release handoff must name immutable artifacts, accepted manifest/decision lanes, evidence, policy, review, rights, sensitivity, validation, terms propagation, citation, product-copy action, public surfaces, correction, withdrawal, rollback, and downstream invalidation. This runbook stops before release.

[Back to top](#top)

---

## 10. Current executable validation

### Environment

```bash
export KFM_NO_NETWORK=1
export PYTHONDONTWRITEBYTECODE=1
export PYTHONHASHSEED=0
export PYTHONUNBUFFERED=1
export TZ=UTC

python tools/ci/install_python_ci.py project-test
```

Do not provide eBird credentials or source bytes.

### Generic Fauna synthetic safety suite

```bash
python -m unittest discover \
  --start-directory tests/domains/fauna \
  --pattern 'test_fauna_smoke.py' \
  --verbose
```

This proves bounded fixture parsing, network guards, declared synthetic acceptance, negative findings for missing references/unresolved governance/precision clues, and transform-reference/caveat requirements for one synthetic withheld scenario.

It does **not** prove EBD terms, source admission, real records, EBD/SED pairing, privacy, operational geoprivacy, evidence, policy, candidate, release, or publication.

### Occurrence Retrieval Snapshot profile

```bash
python -m pytest -q -p no:cacheprovider \
  tests/validators/test_validate_occurrence_retrieval_snapshot.py

python tools/validators/validate_occurrence_retrieval_snapshot.py --fixtures

python tools/validators/validate_generated_receipt.py \
  data/receipts/generated/genrec-occurrence-retrieval-snapshot-20260805.json \
  --repo-root .
```

This proves fixture-only retrieval intent, query snapshots, deterministic identity, EBD/SED sampling-support distinctions, append-only transfer state, false-empty prevention, fixture polarity, and authoring-receipt integrity.

It does **not** prove a live request, current terms, source activation, real pairing, rights/sensitivity review, occurrence/absence truth, evidence, release, or publication.

### Missing EBD-specific gates

No accepted command was verified for exact terms, approved-purpose matching, original/derived/reconstruction review, term propagation, citation/product-copy obligations, commercial permission, EBD-specific privacy/sensitivity, candidate schema, manifest, or release dry run. Those gaps remain `HOLD`.

[Back to top](#top)

---

## 11. Finite outcomes and reason codes

| Outcome | Meaning |
|---|---|
| `PASS` | Named bounded check passed; not release approval |
| `EXPECTED_REJECTION` | Known-invalid input was rejected |
| `FAIL` | Required check failed |
| `HOLD` | Authority, input, implementation, or review missing |
| `DENY` | Use conflicts with controlling restriction or safety rule |
| `ABSTAIN` | Evidence/scientific support insufficient for claim |
| `ERROR` | Procedure/infrastructure could not execute reliably |
| `NOT_RUN` | No execution occurred |
| `PENDING` | Required exact-head evidence unsettled |
| `REVIEW_HANDOFF_READY` | Public-safe packet ready for review only |

Proposed documentation reason codes:

| Reason code | Result |
|---|---|
| `EBD_ACCESS_AGREEMENT_MISSING` | `HOLD_FOR_RIGHTS` |
| `EBD_APPROVED_PURPOSE_MISSING` | `HOLD_FOR_PURPOSE` |
| `EBD_APPROVED_PURPOSE_MISMATCH` | `DENY` |
| `EBD_COMMERCIAL_PERMISSION_MISSING` | `DENY` |
| `EBD_ORIGINAL_DATA_REDISTRIBUTION` | `DENY` |
| `EBD_THIRD_PARTY_SOURCE_HANDOFF` | `DENY` |
| `EBD_DERIVED_TERMS_NOT_PROPAGATED` | `HOLD_FOR_RIGHTS` |
| `EBD_CITATION_MISSING` | `HOLD_FOR_RIGHTS` |
| `EBD_PRODUCT_COPY_PLAN_MISSING` | `HOLD_FOR_RIGHTS` |
| `EBD_LOGO_PERMISSION_MISSING` | `DENY` |
| `EBD_SUPPORTING_METADATA_UNREVIEWED` | `HOLD_FOR_RIGHTS` |
| `EBD_SOURCE_DESCRIPTOR_UNRESOLVED` | `HOLD_FOR_SOURCE_ADMISSION` |
| `EBD_TERMS_POLICY_PLACEHOLDER` | `HOLD_FOR_POLICY` |
| `EBD_REDISTRIBUTION_POLICY_PLACEHOLDER` | `HOLD_FOR_POLICY` |
| `EBD_SENSITIVITY_POLICY_UNENFORCED` | `HOLD_FOR_SENSITIVITY` |
| `EBD_SENSITIVE_DATA_AUTHORIZATION_MISSING` | `DENY` |
| `EBD_SENSITIVE_LOCATION_EXPOSURE` | `DENY` |
| `EBD_OBSERVER_PRIVACY_RISK` | `HOLD_FOR_PRIVACY` |
| `EBD_RECONSTRUCTION_RISK` | `DENY` |
| `EBD_PRODUCT_IDENTITY_COLLAPSE` | `DENY` |
| `EBD_SOURCE_ROLE_COLLAPSE` | `DENY` |
| `EBD_SED_PAIR_MISSING` | `ABSTAIN` |
| `EBD_COMPLETE_CHECKLIST_SUPPORT_MISSING` | `ABSTAIN` |
| `EBD_ABSENCE_CLAIM_OVERREACH` | `DENY` |
| `EBD_METHOD_OR_UNCERTAINTY_MISSING` | `HOLD_FOR_SCIENTIFIC_SUPPORT` |
| `EBD_EVIDENCE_UNRESOLVED` | `HOLD_FOR_EVIDENCE` |
| `EBD_VALIDATION_INCOMPLETE` | `HOLD_FOR_VALIDATION` |
| `EBD_CANDIDATE_CONTRACT_MISSING` | `HOLD_FOR_RELEASE_TOPOLOGY` |
| `EBD_RELEASE_DRY_RUN_HELD` | `HOLD_FOR_RELEASE_TOPOLOGY` |
| `EBD_REVIEW_AUTHORITY_UNASSIGNED` | `HOLD_FOR_REVIEW` |
| `EBD_CORRECTION_PATH_MISSING` | `HOLD_FOR_CORRECTION_PATH` |
| `EBD_ROLLBACK_TARGET_MISSING` | `HOLD_FOR_ROLLBACK` |
| `EBD_HOSTED_EVIDENCE_STALE` | `PENDING` |
| `EBD_PROCEDURE_ERROR` | `ERROR` |

These organize findings; they are not a machine/runtime enum unless an owning contract adopts them.

[Back to top](#top)

---

## 12. Review handoff packet

Required public-safe fields:

| Field | Requirement |
|---|---|
| Repository checkpoint | Base and exact head SHAs |
| Candidate | Stable ID, version, digest, class, audience |
| Purpose/commerciality | Exact approved-purpose mapping and commercial state |
| Terms evidence | Restricted reference/digest |
| Source products/release | EBD/SED kept distinct and release-paired |
| Scientific support | Completeness, effort, method, uncertainty, limits |
| Redistribution risk | Original, near-original, identifiers, reconstruction |
| Sensitivity/privacy | Safe review references |
| Evidence | Resolvable EvidenceRefs/EvidenceBundles |
| Validation | Exact commands, inputs, negative polarity, results |
| Policy/review | Typed outcomes and obligations |
| Release topology | Candidate, manifest, decision lanes/schemas |
| Public surfaces | API, map, tiles, export, search, graph, AI, docs |
| Terms obligations | Citation, terms propagation, product copy, logo permission |
| Reversal | Correction, withdrawal, rollback, cache/index invalidation |
| Findings | Introduced, inherited, unresolved, expected hold |
| Non-effects | What the packet does not authorize |

Interim shape:

```yaml
handoff_type: ebd_derivative_release_review
repository:
  base_commit: <sha>
  candidate_head: <sha>
candidate:
  id: <stable id>
  version: <version>
  sha256: <digest>
  class: <class>
  audience: <restricted | reviewer | proposed-public>
  commercial_use: <true | false>
source:
  products: [EBD, SED]
  release_ref: <safe reference>
  source_descriptor_ref: <accepted reference>
terms:
  review_ref: <restricted reference>
  approved_purpose_match: <PASS | FAIL | HOLD>
  derived_terms_propagated: <true | false>
  citation_ready: <true | false>
  product_copy_plan_ready: <true | false>
science:
  sampling_support: <profile>
  method_ref: <reference>
  limitations_ref: <reference>
safety:
  original_redistribution: false
  reconstruction_risk: <PASS | FAIL | HOLD>
  sensitivity_review_ref: <reference>
  privacy_review_ref: <reference>
governance:
  evidence_state: <RESOLVED | UNRESOLVED>
  policy_state: <ALLOW | RESTRICT | DENY | ABSTAIN | ERROR | NOT_EVALUATED>
  review_state: <state>
  release_state: <state>
  correction_ref: <reference or HOLD>
  withdrawal_ref: <reference or HOLD>
  rollback_ref: <reference or HOLD>
result:
  outcome: <finite outcome>
  reason_codes: []
  limitations: []
```

This is explanatory, not a ReleaseManifest, PolicyDecision, or machine contract.

[Back to top](#top)

---

## 13. Correction, withdrawal, and rollback

Trigger review when terms/purpose change, commercial use emerges, source or near-source data escape, citation/term/product-copy obligations fail, sensitive status changes, locations or observer data leak, EBD/SED pairing is wrong, claims exceed support, evidence/policy/review stops resolving, or public carriers retain stale/withdrawn material.

For rights, sensitivity, exact-location, privacy, or commercial-permission defects:

1. disable affected public surfaces first;
2. preserve audit evidence in restricted lanes;
3. do not repeat exposed material in issues, PRs, logs, or screenshots;
4. inventory every derivative, cache, index, graph, tile, export, and AI response;
5. notify authorized source, rights, sensitivity, and release contacts;
6. decide correction, withdrawal, or rollback through owning authorities.

| Action | Use when | Effect |
|---|---|---|
| Correction | Authorized claim can be replaced safely | New immutable version and CorrectionNotice |
| Withdrawal | Material must leave public state | Disable carriers and issue WithdrawalNotice |
| Rollback | A prior release remains valid under current controls | Restore through same governed release path |
| Supersession | New approved derivative replaces old | Forward link; no overwrite |
| Upstream error report | Error may belong to eBird source | Notify official process; KFM does not rewrite source |

A rollback target must be rechecked against current terms, purpose, sensitivity, privacy, evidence, policy, and interfaces. If it fails, withdraw and hold.

[Back to top](#top)

---

## 14. Hosted CI and exact-head evidence

Bind every result to the current head:

```yaml
head_sha: <full SHA>
workflow: <name>
run_id: <id>
status: <queued | in_progress | completed>
conclusion: <success | failure | cancelled | skipped | null>
observed_at: <timestamp>
```

Relevant workflows include `domain-fauna`, documentation checks, policy/security/topology checks, and `occurrence-retrieval-snapshot` when its path filter matches. This docs-only change may not trigger the latter; absence is not a pass.

Failure classes:

- **Introduced** — caused by candidate bytes/direct dependencies.
- **Inherited** — matching base/head comparison proves baseline debt.
- **Unresolved** — no sufficient comparison.
- **Expected hold** — workflow deliberately verifies missing proof/release closure.
- **Infrastructure** — runner/platform failure.
- **Stale** — older head.
- **Not applicable** — outside changed-area contract.

A green workflow proves only its declared commands. It does not prove terms, purpose, admission, rights, sensitivity, scientific validity, evidence, review, release, deployment, or publication.

[Back to top](#top)

---

## 15. Current holds and open verification

Blocking work:

- [ ] Accept an eBird SourceDescriptor with non-`TBD` role, rights, sensitivity, cadence, access, and citation.
- [ ] Capture exact agreement, purpose, release, and supporting metadata.
- [ ] Confirm commercial/non-commercial posture.
- [ ] Replace EBD terms and redistribution placeholders with reviewed authority or accepted equivalents.
- [ ] Replace the fail-open rare-species stub with accepted fail-closed policy and tests.
- [ ] Decide policy placement without parallel authority.
- [ ] Establish or select an accepted derivative candidate contract/schema/fixtures/validator/tests.
- [ ] Resolve singular/plural manifest topology.
- [ ] Update Fauna candidate workflow deliberately before adding a child candidate.
- [ ] Add EBD-specific purpose, commerciality, original/derived, reconstruction, citation, term-propagation, product-copy, and logo checks.
- [ ] Establish operational privacy, sensitivity, and geoprivacy validation.
- [ ] Resolve EvidenceRefs to EvidenceBundles for the exact derivative.
- [ ] Assign accountable rights, sensitivity, scientific, evidence, independent-review, and release roles.
- [ ] Establish correction, withdrawal, rollback, cache, and downstream invalidation.
- [ ] Record exact-head hosted validation.
- [ ] Verify deployed/public state separately.

Separate documentation follow-ups:

- modernize the one-byte `docs/runbooks/fauna/README.md`;
- reconcile proposal-era source-refresh, promotion, and rollback runbooks;
- reconcile the older EBD catalog page;
- update the Fauna release index only when real release state/topology changes.

[Back to top](#top)

---

## 16. Maintenance and document rollback

Re-review when official terms, an exact request, EBD/SED product structure, sensitive-data process, SourceDescriptor, policy, candidate contract, release topology, workflow hold, commercial/public use, or an incident changes.

A material update should freeze exact authority and bytes, inspect current official Cornell/eBird and KFM authorities, distinguish terms from implementation, update commands only from executable evidence, preserve version/reason, run documentation and changed-area checks, and use a reviewable branch/PR.

Before merge, close the draft PR and delete its branch if abandoned. After merge, revert through an ordinary PR and rerun documentation checks. A Markdown revert has no source, lifecycle, release, deployment, or publication effect.

[Back to top](#top)

---

## Appendix A — Operator checklist

### Authority and terms

- [ ] Record exact repo/head/artifact digests.
- [ ] Confirm no overlap.
- [ ] Resolve request, purpose, terms, release, metadata, and sensitive-data authorization.
- [ ] Confirm commerciality and permission.
- [ ] Confirm no original-data handoff or original-format redistribution.
- [ ] Confirm derived terms propagation, citation, product-copy plan, and logo permission.

### Source and science

- [ ] Resolve accepted SourceDescriptor.
- [ ] Preserve EBD/SED/API/GBIF/media identity.
- [ ] Record same-release EBD/SED pairing.
- [ ] Prove complete-checklist support for non-detection.
- [ ] Prevent broad absence claims.
- [ ] Preserve citizen-science versus specimen/status/range/model roles.
- [ ] Document method, filters, uncertainty, limits, and time/spatial support.

### Safety and governance

- [ ] Confirm no source rows/identifiers or reconstruction.
- [ ] Confirm no sensitive or observer/private-site leakage.
- [ ] Test repeated-query/differencing and every public carrier.
- [ ] Resolve evidence and exact negative validation.
- [ ] Obtain rights, sensitivity/privacy, scientific/evidence, policy, independent, and release reviews separately.
- [ ] Resolve candidate/manifest topology.
- [ ] Resolve correction, withdrawal, rollback, and downstream invalidation.
- [ ] Record exact-head CI.
- [ ] Record finite result, reason codes, unknowns, and non-effects.

[Back to top](#top)

---

## Appendix B — Review handoff template

```markdown
# <candidate-id> — EBD Derivative Review

## Status
`DRAFT | HOLD | DENY | ABSTAIN | REVIEW_HANDOFF_READY`

## Checkpoint
- Base:
- Head:
- Changed paths:

## Candidate
- ID / version / SHA-256:
- Derivative class:
- Audience:
- Commercial use:
- Public surfaces:

## Source and terms
- EBD release:
- SED release:
- SourceDescriptor:
- Access-request and terms review:
- Approved-purpose match:
- Commercial permission:
- Derived terms propagation:
- Citation:
- Product-copy plan:
- Logo permission:

## Scientific support
- Sampling profile:
- Complete-checklist support:
- Method / filters:
- Spatial and temporal support:
- Uncertainty / limitations:

## Safety
- Original/near-original risk:
- Reconstruction:
- Sensitive-species review:
- Observer/privacy review:
- Transform reference:

## Evidence, validation, and governance
- EvidenceRefs / EvidenceBundles:
- Validation and negative fixtures:
- Rights outcome:
- Sensitivity outcome:
- Policy outcome:
- Independent review:
- Candidate / manifest state:
- Correction / withdrawal / rollback:

## Result
- Outcome:
- Reason codes:
- Introduced / inherited / unresolved findings:
- Non-effects:
```

[Back to top](#top)

---

## Appendix C — Current evidence and official references

### Repository

- [Parent runbook index](../README.md)
- [Directory Rules](../../doctrine/directory-rules.md)
- [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [Fauna source families](../../domains/fauna/SOURCE_FAMILIES.md)
- [Fauna sensitivity](../../domains/fauna/SENSITIVITY.md)
- [Fauna release index](../../domains/fauna/RELEASE_INDEX.md)
- [EBD product page](../../sources/catalog/ebird/ebird-basic-dataset.md)
- [SED product page](../../sources/catalog/ebird/sampling-event-data.md)
- [eBird SourceDescriptor candidate](../../../data/registry/fauna/sources/ebird.yaml)
- [eBird RAW lane](../../../data/raw/fauna/ebird/README.md)
- [EBD terms placeholder](../../../policy/rights/fauna/ebd_terms.yaml)
- [eBird redistribution placeholder](../../../policy/domains/fauna/ebird_redistribution.md)
- [Rare-species policy stub](../../../policy/domains/fauna/rare_species_redaction.rego)
- [Fauna candidates](../../../release/candidates/fauna/README.md)
- [Fauna manifest guidance](../../../release/manifests/fauna/README.md)
- [Occurrence Retrieval Snapshot](../../../contracts/source/occurrence_retrieval_snapshot.md)
- [Fauna workflow](../../../.github/workflows/domain-fauna.yml)
- [Occurrence Retrieval Snapshot workflow](../../../.github/workflows/occurrence-retrieval-snapshot.yml)

### Official Cornell/eBird pages checked 2026-08-24

- [eBird Data Access Terms of Use](https://www.birds.cornell.edu/home/ebird-data-access-terms-of-use/)
- [eBird Data Privacy and Data Use](https://support.ebird.org/en/support/solutions/articles/48001078113-ebird-data-privacy-and-data-use)
- [Download eBird Data](https://support.ebird.org/en/support/solutions/articles/48000838205-download-ebird-data)
- [Sensitive Species in eBird](https://support.ebird.org/en/support/solutions/articles/48000803210-sensitive-species-in-ebird)

Official pages support general source/terms guidance. They do not prove the exact agreement, purpose, authorized users, sensitive-data permission, source release, or KFM state for a particular derivative.

[Back to top](#top)

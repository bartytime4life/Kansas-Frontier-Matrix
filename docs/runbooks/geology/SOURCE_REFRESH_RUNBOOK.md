<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/geology/source-refresh-runbook
title: Geology and Natural Resources Source Refresh Inspection Runbook
type: runbook
subtype: domain-source-refresh-inspection
version: v0.2
status: draft; repository-grounded; documentation-only; inspection-and-handoff-only; source-inactive-by-default; fail-closed; non-authoritative; non-activation; non-review; non-promotion; non-release; non-deployment; non-publisher
owners:
  - "@bartytime4life — verified GitHub review route"
  - "NEEDS VERIFICATION — accountable source, connector, Geology, Natural Resources, rights, sensitivity, evidence, policy, validation, review, release, correction, rollback, security, and operations stewards"
created: 2026-05-12
updated: 2026-08-25
policy_label: public-review; geology; natural-resources; source-refresh-inspection; operational-documentation; rights-aware; sensitive-location-aware; fail-closed; no-publication-authority
current_path: docs/runbooks/geology/SOURCE_REFRESH_RUNBOOK.md
owning_root: docs/
responsibility: >-
  Explain how to inspect an already-authorized Geology source-head signal, classify bounded
  no-change or material-change evidence, and prepare a non-authoritative handoff without
  admitting or activating a source, fetching live bytes, performing review, crossing a lifecycle
  boundary, promoting, releasing, deploying, or publishing.
truth_posture: cite-or-abstain
truth_labels: [CONFIRMED, PROPOSED, UNKNOWN, NEEDS VERIFICATION, CONFLICTED, HOLD]
authority_class: explanatory operational documentation
canonical_relationship: >-
  Existing direct child of docs/runbooks/geology/; reconciled in place under the lane README;
  no new path, alias, mirror, migration, connector, watcher, or sibling authority.
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 0f9e4f6f7730994899773451e835e513dc4c6c15
  target_prior_blob: e0a6d4e39f01bc957fe4bc66b6b918a376503b18
  lane_readme_blob: 62d96d10a9ca0831b9847fb325cd2604c97ba1c1
  source_descriptor_contract_blob: b57ae5ccc042c1423b75c168438800384c9b6713
  source_descriptor_schema_blob: 42da54b28a527850cce88ad89f68921c101fc56b
  source_authority_register_blob: 32729857bc8eb5001acb37b8ee8e60bcb6e0dc50
  subtype_source_registry_blob: 0bb2d794e3179186abfa371a3c99532f50d2c571
  domain_first_source_compatibility_blob: c19b8bcd1f8e89b65a65b2144df647dd98fe0674
  m118_source_descriptor_blob: 4f60685cbf397ad31415546fd32b07824654f7e9
  aem_domain_first_record_blob: 4e69fb735bdfea6dd212d6ebe8ffd76b6f6de12a
  connector_compatibility_index_blob: 9575bec2c30a5f7a7a227ed4a48d548a00be83d1
  m118_validation_workflow_blob: 205d8d488429d9bcb6054c1bae4a6e3876a63ce2
  production_material_change_contract_blob: 1f591a778ae1da037b27ca82d83b05b45fab4155
  production_material_change_schema_blob: 56b0de0c6421aeab8b547e2ca2f12698376d0a92
  production_material_change_validator_blob: f3ba5b007a3b0b92a3e643792befeb934cb0c546
  production_material_change_test_blob: 779ff37af46ac591df8f69dd602cf23faf4c78b1
  geology_policy_blob: 71e4a939510712346c3b80e62c47d1770e799c03
  geology_workflow_blob: 79b6066c9dede603df328d66601fe757ae68c5b3
related:
  - ./README.md
  - ./BEDROCK_REVIEW.md
  - ./NO_NETWORK_TEST_RUNBOOK.md
  - ./PROMOTION_RUNBOOK.md
  - ./ROLLBACK_RUNBOOK.md
  - ../../domains/geology/README.md
  - ../../domains/geology/SOURCES.md
  - ../../domains/geology/SOURCE_REGISTRY.md
  - ../../domains/geology/SOURCE_ROLE_MATRIX.md
  - ../../domains/geology/SENSITIVITY.md
  - ../../../contracts/source/source_descriptor.md
  - ../../../schemas/contracts/v1/sources/source_descriptor.schema.json
  - ../../../control_plane/source_authority_register.yaml
  - ../../../data/registry/sources/geology/README.md
  - ../../../data/registry/geology/sources/README.md
  - ../../../data/registry/sources/geology/kgs-m118-surficial-geology.source.json
  - ../../../connectors/geology/README.md
  - ../../../contracts/domains/geology/production_material_change.md
  - ../../../schemas/contracts/v1/domains/geology/production_material_change.schema.json
  - ../../../tools/validators/domains/geology/validate_production_material_change.py
  - ../../../tests/domains/geology/test_production_material_change.py
  - ../../../.github/workflows/kgs-m118-source-descriptor.yml
  - ../../../.github/workflows/domain-geology.yml
tags: [kfm, geology, natural-resources, runbook, source-refresh, inspection, source-head, material-change, no-network, rights, sensitivity, evidence, fail-closed]
notes:
  - "This revision removes illustrative live watcher commands, proposal-era path alternatives, and implied refresh side effects."
  - "The accepted source-registry topology is subtype-first under data/registry/sources/, while domain-first Geology YAML records remain present beneath a compatibility lane that prohibits independent writes; that recorded-state conflict must not be resolved by this runbook."
  - "The machine source-authority projection is PROPOSED, projection-only, implementation-absent, empty, and non-activating."
  - "The KGS M-118 SourceDescriptor is proposed and inactive, rights remain unresolved, and its connector activation state is disabled; its workflow validates declarations only with no network."
  - "The production material-change profile is a bounded no-network comparison of version-pinned KGS oil-and-gas metadata; it does not fetch source bytes or generalize to every Geology source family."
  - "This document creates no source descriptor, activation, fetch, source-head observation, receipt, evidence, policy decision, review, candidate, lifecycle transition, promotion, release, deployment, or public state."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Geology and Natural Resources Source Refresh Inspection Runbook

> **Use this runbook to inspect a source-head signal that an already-authorized source operation produced, classify the bounded evidence, and prepare a non-authoritative handoff.** This runbook is not a watcher, connector, scheduler, source-admission decision, fetch command, reviewer, lifecycle writer, or publisher.

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#current-repository-posture)
[![Source authority: empty](https://img.shields.io/badge/source%20authority-empty-b42318?style=flat-square)](#current-repository-posture)
[![M118: proposed inactive](https://img.shields.io/badge/M--118-proposed%20inactive-d4a72c?style=flat-square)](#current-repository-posture)
[![Connector topology: conflicted](https://img.shields.io/badge/connectors-CONFLICTED-d4a72c?style=flat-square)](#current-repository-posture)
[![Authority: inspection only](https://img.shields.io/badge/authority-inspection%20only-0969da?style=flat-square)](#authority-and-negative-authority)
[![Publisher: no](https://img.shields.io/badge/publisher-no-b42318?style=flat-square)](#authority-and-negative-authority)

> [!IMPORTANT]
> **Current safe determination at `main@0f9e4f6f7730…`: `HOLD — NO ACTIVE GEOLOGY SOURCE REFRESH PATH ESTABLISHED`.** The machine source-authority projection has no entries, the inspected KGS M-118 record is proposed/inactive with unresolved rights and disabled connector activation, source/connector topology remains conflicted, and no general Geology watcher runtime is established.

> [!CAUTION]
> A source descriptor file, endpoint URL, schedule proposal, workflow dispatch button, manual download, changed upstream page, HTTP status, `etag`, timestamp, digest, material-change result, pull request, or green validation job is not source admission, activation, evidence closure, review, promotion, release, deployment, or publication.

> [!WARNING]
> Never place credentials, private endpoints, exact or reverse-engineerable borehole/private-well/well-log/core/sample/geochemistry/sensitive-resource/operator/parcel/extraction-targetable coordinates, protected joins, redaction offsets, or source-native restricted payloads in an ordinary refresh packet, log, issue, pull request, screenshot, or generated summary.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-and-negative-authority) · [State](#current-repository-posture) · [Outcomes](#finite-procedure-outcomes) · [Triggers](#recognized-inspection-triggers) · [Preconditions](#preconditions-and-stop-conditions) · [Packet](#required-inspection-packet) · [Procedure](#procedure) · [No-change](#no-change-candidate-path) · [Material change](#material-change-candidate-path) · [Geology controls](#geology-specific-controls) · [Validation](#validation-and-command-boundary) · [Handoff](#handoff-boundary) · [Anti-patterns](#anti-patterns-to-refuse) · [Open work](#open-verification-register) · [Evidence](#evidence-basis) · [Rollback](#document-change-rollback)

---

## Purpose

This runbook supports a narrow, evidence-preserving inspection:

1. freeze the exact repository revision and the separately produced source-head signal;
2. verify that source identity, source role, authority, rights, sensitivity, and connector path are already established by owning surfaces;
3. compare immutable prior/current metadata without making a network request here;
4. classify `NO_CHANGE`, material-change-review candidate, or a fail-closed outcome;
5. record non-sensitive findings and immutable pointers; and
6. hand the result to owning source, evidence, policy, review, lifecycle, correction, and release processes.

It does not:

- create, admit, activate, suspend, or withdraw a `SourceDescriptor`;
- select a canonical source-registry or connector path;
- schedule a watcher or perform a live fetch;
- store RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED bytes;
- canonicalize or hash source bytes that were not already supplied by an authorized producer;
- create a `RunReceipt`, `EvidenceBundle`, `PolicyDecision`, review record, promotion candidate, release manifest, correction notice, withdrawal notice, or rollback card;
- open or approve a reviewed lifecycle transition;
- invalidate caches, rebuild tiles, change aliases, deploy, promote, release, or publish; or
- certify the freshness, completeness, accuracy, geology, rights, safety, or public usability of a source.

[Back to top](#top)

---

## Authority and negative authority

This file inherits the [Geology runbook lane boundary](./README.md). It describes safe inspection and handoff. It does not own a source or an operation.

| Concern | Owning surface | This runbook may do | This runbook must not do |
|---|---|---|---|
| Source identity and admission | canonical source registry, accepted authority/activation records | Require exact resolvable state | Mint, admit, activate, suspend, or withdraw |
| Source access | one accepted source-first connector/runtime | Inspect an already-produced bounded signal | Choose a path, fetch, authenticate, or schedule |
| Source role | source descriptor plus Geology doctrine/contracts | Check role preservation | Upgrade a role or convert context/model into observation |
| Rights and sensitivity | accepted rights/sensitivity policy and review | Require finite state and obligations | Infer permission from public reachability |
| Source payload lifecycle | governed `data/` lanes and writers | Reference immutable identities | Write, move, transform, or delete payloads |
| Evidence and receipts | `data/receipts/`, `data/proofs/`, EvidenceBundle family | Require support pointers | Manufacture evidence or receipts |
| Materiality | accepted contract/profile and accountable steward | Run a bounded existing validator | Generalize one profile to every source |
| Policy and review | `policy/` and accountable reviewers | Prepare a handoff | Evaluate policy, request review, or claim approval |
| Promotion/release | `release/` and owning operations | Identify downstream prerequisites | Promote, release, deploy, or publish |
| Correction/rollback | release accountability families and owning operations | Preserve lineage requirements | Execute correction, invalidation, withdrawal, or rollback |

A README cannot turn a proposed descriptor into an admitted source, an endpoint into permission, a change signal into evidence truth, or a materiality classification into a release decision.

[Back to top](#top)

---

## Current repository posture

The observations below are pinned to `main@0f9e4f6f7730994899773451e835e513dc4c6c15`.

| Surface | Confirmed repository evidence | Bounded conclusion |
|---|---|---|
| Accepted source topology | Directory Rules route machine source descriptors through `data/registry/sources/` | Subtype-first is the canonical write topology |
| Domain-first compatibility lane | `data/registry/geology/sources/README.md` prohibits independent descriptor writes but sibling YAML records are present | Recorded bytes and declared write contract are `CONFLICTED`; do not update either by convenience |
| Machine source authority | `PROPOSED`, `projection_only`, implementation `ABSENT`, completeness `empty`, `entries: []` | No active source authority is established by the projection |
| KGS M-118 descriptor | Proposed/inactive; public release false; rights unresolved; file not downloaded/hashed; connector activation disabled | May be schema-validated as a candidate only; no live refresh |
| GMD 3 AEM domain-first record | Proposed, disabled, noncanonical; product availability unknown; no endpoint or connector established | Announcement-bound planning/candidate evidence only |
| Other domain-first KGS/USGS records | Several are proposal templates with unresolved trust-bearing fields | Not admitted or refreshable by this runbook |
| Connector topology | KGS/KSGS product/family paths are mixed and conflicted; `connectors/geology/` is documentation-only | No general Geology connector/runtime path is established |
| M-118 workflow | No-network validation of one proposed inactive descriptor and generated authoring receipt | Validates declarations only; no fetch, activation, or admission |
| Production material-change profile | Deterministic no-network comparison of version-pinned KGS oil-and-gas metadata | Bounded `NO_CHANGE`, `REVIEW`, `HOLD`, or `ERROR`; no live KGS request |
| Geology workflow | Runs four bounded no-network profiles and explicitly holds broader proof/release | Not a refresh, watcher, policy, review, release, or publisher |
| Geology policy | Default-only scaffolds with unverified evaluator/consumer | Cannot authorize refresh or outward use |

### Current safe determination

```text
procedure_disposition: HOLD
reason: NO_ACTIVE_GEOLOGY_SOURCE_REFRESH_PATH
source_fetch_performed: false
lifecycle_effect: none
public_effect: none
```

This is a documentation conclusion for the pinned revision, not an activation or source-state record.

[Back to top](#top)

---

## Finite procedure outcomes

This runbook does not create a canonical repository-wide enum. Use the selected contract/validator vocabulary for machine records. For human inspection, record one bounded disposition:

| Disposition | Meaning | Permitted next step |
|---|---|---|
| `NO_CHANGE_CANDIDATE` | Authorized prior/current metadata appear unchanged under the named bounded profile | Hand off for owning receipt/audit handling; do not claim an emitted no-op receipt |
| `MATERIAL_CHANGE_CANDIDATE` | A bounded comparison found declared dimensions that require accountable inspection | Hand off; do not create review, promotion, or release state |
| `HOLD` | Authority, source identity, rights, sensitivity, baseline, connector, evidence, or required state is absent/conflicted | Preserve prior safe state |
| `ABSTAIN` | Evidence cannot support a change/no-change conclusion | Obtain admissible evidence or narrow scope |
| `RESTRICT` | Handling may continue only through approved restricted controls | Remove protected material from ordinary surfaces |
| `DENY` | Requested access, comparison, storage, or exposure violates a governing rule | Stop and record non-sensitive reason |
| `ERROR` | Inspection or validation could not produce a reliable result | Preserve inputs and diagnostics; no materiality claim |

`NO_CHANGE_CANDIDATE` is not proof that a watcher ran, a source is current, a source-head observation is authentic, a receipt exists, or a public freshness badge may reset.

`MATERIAL_CHANGE_CANDIDATE` is not an accepted change, review request, candidate admission, promotion request, release approval, cache invalidation instruction, or publication trigger.

The repository's current `ProductionMaterialChange` profile uses `NO_CHANGE`, `REVIEW`, `HOLD`, and `ERROR`. Preserve those exact values when operating that profile; map them to this runbook's explanatory dispositions only in prose.

[Back to top](#top)

---

## Recognized inspection triggers

An inspection may begin only from a separately authorized, immutable signal such as:

- a source-head record from an accepted connector run;
- a steward-authorized comparison request bound to exact prior/current snapshots;
- an accepted correction, supersession, withdrawal, rights, terms, or sensitivity notice;
- a declared cadence/freshness review from the owning source record;
- an exact manifest/digest mismatch reported by governed validation; or
- an incident response request from the owning security/correction authority.

The following do not authorize a fetch or refresh:

- a README schedule or proposal;
- an upstream URL being publicly reachable;
- a browser observation;
- a workflow dispatch button;
- a cron expression in planning material;
- a changed timestamp without content identity;
- an issue, pull request, chat instruction, or generated summary lacking source authority; or
- a proposed/disabled source descriptor.

At the pinned revision, no inspected trigger clears the authority and runtime prerequisites for a general live Geology refresh.

[Back to top](#top)

---

## Preconditions and stop conditions

### Preconditions

Before inspecting prior/current source-head material, require:

- exact repository revision and worktree state;
- canonical source ID and descriptor version;
- accepted admission/activation record from the owning authority;
- accepted source-first connector/runtime identity;
- authenticated actor and authorized operation scope;
- immutable prior and current source-head identities;
- source role, authority scope, rights, terms, attribution, redistribution, access, and sensitivity state;
- expected cadence/freshness semantics;
- object/claim families permitted for the source;
- bounded materiality profile and validator version;
- protected-handling classification; and
- correction, supersession, receipt, evidence, policy, review, lifecycle, and rollback destinations owned elsewhere.

### Mandatory stop conditions

Return a fail-closed outcome when:

- the source appears only in proposal-era or disabled records;
- the empty machine source-authority projection is being treated as activation;
- accepted registry identity or activation state cannot be resolved;
- canonical source-registry writer and compatibility/mirror state conflict;
- connector path, package, product dispatch, credential mode, or runtime is unresolved;
- the request requires this README to fetch or schedule live bytes;
- prior or current source-head identity is mutable, missing, or unauthenticated;
- rights, terms, attribution, redistribution, or access posture is unknown;
- exact/reconstruction-sensitive content would enter an ordinary repository surface;
- source role, object family, claim class, scale, time, geometry, depth, or uncertainty is collapsed;
- no accepted materiality profile applies to the source family;
- evidence, policy, reviewer authority, lifecycle writer, or rollback target is assumed rather than resolved;
- the operation would overwrite history, silently replace a descriptor, or bypass correction/supersession lineage;
- network access is attempted while the selected profile is no-network; or
- validation cannot produce a deterministic finite result.

### Safe pause behavior

1. Do not fetch or retry through an unverified path.
2. Preserve prior descriptor, source-head, lifecycle, and public state.
3. Do not reset freshness indicators, invalidate caches, rebuild derivatives, or open a promotion path.
4. Record only non-sensitive blocker codes and immutable pointers.
5. Route protected material and secrets outside ordinary repository surfaces.
6. Restart from an exact new revision only after owning authority resolves the blocker.

[Back to top](#top)

---

## Required inspection packet

### 1. Scope and identity

- exact repository commit;
- canonical source ID and descriptor version;
- source family/product and domain consumers;
- accepted connector/runtime identity;
- authorized actor/operation reference;
- prior/current source-head IDs and immutable digests;
- materiality profile ID/version; and
- public/lifecycle effect explicitly `none` during inspection.

### 2. Authority, rights, and sensitivity

- admission and activation state;
- source role and authority limits;
- publisher/steward identity;
- rights/license/terms and verification time;
- attribution and redistribution obligations;
- access/auth class without secrets;
- sensitivity floor and public-safe obligations; and
- unresolved conflicts or restrictions.

### 3. Prior/current metadata

- source version/edition;
- `etag`, `last_modified`, content length, and upstream version only when emitted by the authorized connector;
- canonical content/manifest/footprint digest as applicable;
- retrieval/observation time and method;
- temporal coverage;
- spatial/scale/CRS/depth/vertical context;
- record count or declared inventory dimensions where meaningful;
- source-role and support-type declarations; and
- correction/supersession state.

Metadata values are evidence inputs, not automatic proof of content identity or correctness.

### 4. Comparison and findings

- exact dimensions compared;
- unchanged/changed/unknown values;
- deterministic reason codes;
- schema/semantic findings;
- stale, regressing, missing-baseline, or rights-unknown findings;
- evidence references;
- procedure disposition; and
- explicit statement that no source fetch or lifecycle mutation occurred here.

### 5. Handoff pointers

- owning source/connector steward;
- evidence/receipt destination;
- rights/sensitivity/policy authority;
- accountable review route;
- lifecycle/correction/rollback authorities;
- open blockers and obligations; and
- restricted-handling route when applicable.

Do not embed source payloads, credentials, tokens, private endpoints, protected geometry, restricted attributes, or reversal-enabling transform detail.

[Back to top](#top)

---

## Procedure

### Step 0 — Freeze exact scope

Record the repository revision, source ID, descriptor version, authorized signal identity, prior/current snapshot digests, comparison profile, and intended audience. If any is missing, return `HOLD` or `ERROR`.

### Step 1 — Resolve canonical source state

Resolve the source through the accepted subtype-first registry and its owning activation/authority records. Do not use the domain-first compatibility lane as an independent writer.

At the pinned revision:

- the source-authority projection is empty and implementation-absent;
- the M-118 record is proposed/inactive with connector activation disabled;
- the GMD 3 AEM record is proposed, disabled, and noncanonical; and
- other domain-first templates leave trust-bearing fields unresolved.

Those states stop a live refresh.

### Step 2 — Resolve connector/runtime authority

Confirm one source-first connector path, package identity, product dispatch, credential mode, tests, fixtures, activation decision, and read/write boundary. The documentation-only `connectors/geology/` lane cannot satisfy this requirement.

If connector topology remains mixed or conflicted, return `HOLD`; do not choose a winner by path presence.

### Step 3 — Verify rights and sensitivity before reading content

Require current rights, terms, attribution, redistribution, access, and sensitivity decisions for the exact product/edition/API. Public reachability does not mean redistribution or public release is permitted.

If rights are unknown or protected content would cross into an ordinary surface, return `HOLD`, `RESTRICT`, or `DENY`.

### Step 4 — Accept only an already-produced authorized signal

This runbook has no live-fetch command. Receive immutable prior/current source-head metadata from the owning authorized producer. Verify actor, operation, time, identity, digest algorithm, and canonicalization profile.

Do not reconstruct a signal from browser observations, planning examples, or manual downloads.

### Step 5 — Preserve source role and claim class

Confirm that the comparison remains within the descriptor's admitted role and permitted claims. A changed production manifest is production-record evidence; it is not proof of a mineral occurrence, deposit, estimate, reserve, or physical geologic change.

### Step 6 — Select one accepted bounded profile

Name the exact contract/schema/validator. Do not apply the KGS oil-and-gas `ProductionMaterialChange` profile to M-118, AEM, boreholes, well logs, bedrock, surficial maps, MRDS, cross-sections, or other products without a separately accepted profile.

If no profile applies, return `HOLD`.

### Step 7 — Validate without network or mutation

Run the selected validator against local immutable packet bytes. Record tool version, input digest, output, exit code, finite outcome, and findings. The validator must not contact a source or write lifecycle/public state.

### Step 8 — Classify the procedure disposition

Apply fail-closed precedence. Distinguish:

- comparison evidence from source truth;
- `NO_CHANGE` from watcher/receipt proof;
- `REVIEW` from performed review;
- `HOLD` from a negative substantive claim; and
- `ERROR` from a materiality conclusion.

### Step 9 — Prepare the handoff

Prepare immutable pointers, findings, blockers, evidence references, rights/sensitivity state, and the explicit non-effects. Deliver to owning authorities only.

### Step 10 — Stop

Do not fetch, retry, write a receipt by imitation, mutate a source record, open a promotion candidate, invalidate caches, rebuild tiles, change public aliases, or cross any lifecycle boundary from this procedure.

[Back to top](#top)

---

## No-change candidate path

A `NO_CHANGE_CANDIDATE` requires:

- accepted source/connector authority;
- authenticated immutable prior/current signals;
- the same source, product, role, profile, canonicalization, and comparison scope;
- complete required dimensions;
- no rights, sensitivity, correction, or stale-state blocker;
- deterministic validation with no findings; and
- a separately owned destination for any no-op receipt or audit record.

This runbook does not emit the receipt. It records only that the bounded comparison is ready for owning handling.

Do not:

- reset a freshness badge or cadence clock;
- claim the watcher ran successfully beyond the supplied signal;
- rebuild tiles, catalogs, proofs, or evidence;
- emit new STAC/DCAT/PROV entities;
- invalidate caches;
- change release state; or
- publish a heartbeat.

The current production material-change fixture proves only its synthetic/version-pinned metadata rules. It does not establish a live no-change event.

[Back to top](#top)

---

## Material-change candidate path

A `MATERIAL_CHANGE_CANDIDATE` means only that the selected bounded profile found declared differences that require accountable handling.

Prepare:

- exact source and prior/current identities;
- changed dimensions and reason codes;
- source-role and claim-class limits;
- rights/sensitivity/correction state;
- immutable evidence and validation pointers;
- affected candidate/lifecycle scopes, without mutating them;
- required source, Geology, evidence, policy, review, release, correction, and rollback roles;
- open blockers and obligations; and
- explicit `review_state: NOT_PERFORMED`, `transition_applied: false`, `public_effect: none`.

Do not:

- call `REVIEW` an approval or a requested review;
- create a promotion candidate automatically;
- infer new geologic truth from metadata change;
- overwrite a descriptor or prior snapshot;
- admit new bytes to RAW/WORK/PROCESSED;
- rebuild public-safe geometry, tiles, catalogs, proofs, or AI indexes;
- emit a `PromotionDecision` or `ReleaseManifest`; or
- release, deploy, promote, or publish.

Use the [promotion handoff runbook](./PROMOTION_RUNBOOK.md) only after an independently governed candidate dossier actually exists and all prerequisites resolve.

[Back to top](#top)

---

## Geology-specific controls

### Source-role anti-collapse

Preserve:

- official map artifact versus direct observation;
- interpreted compilation versus measured sample;
- borehole/well-log reference versus geologic unit;
- regulatory/administrative record versus physical geology;
- production record versus well observation;
- geophysics/geochemistry measurement versus interpretation/model;
- occurrence versus deposit versus estimate versus reserve;
- permit/lease/operator context versus ownership or subsurface truth;
- aggregate versus per-site record; and
- announcement/planned campaign versus completed acquisition or released product.

### Scale, time, depth, and representation

Preserve map edition, scale, source vintage, valid/observation/retrieval/interpretation/correction times, CRS, geometry role, uncertainty, depth/elevation/interval, and vertical datum where applicable. A timestamp change alone is not materiality; an unchanged digest does not prove completeness.

### Rights and public-safe precision

Unknown rights fail closed. Public availability does not waive attribution, redistribution, commercial-use, sensitive-location, or public-safe representation requirements. Exact subsurface/resource detail and harmful joins require authorized restricted handling or a separately evidenced generalization/redaction path.

### Cross-domain source identity

Capture one source under one accepted identity even when Geology, Hydrology, Soil, Hazards, Agriculture, Infrastructure, Archaeology, or People/Land consume different projections. Do not create duplicate authorities or silently widen a source's claim role for another domain.

### MapLibre and governed AI

Public maps, Evidence Drawer, Focus Mode, search, dashboards, reports, exports, graphs, and AI surfaces consume only governed released carriers. They must not watch upstream sources, read registry records directly, or interpret this inspection packet as public truth.

[Back to top](#top)

---

## Validation and command boundary

### Documentation validation

Verify:

- valid UTF-8 and final newline;
- exactly one opening and closing KFM metadata marker;
- parseable metadata YAML;
- balanced fenced code blocks;
- internal heading-link coverage;
- relative links resolve at the pinned revision;
- no unresolved `TODO`, transient citation token, secret, endpoint credential, or sensitive coordinate;
- evidence snapshot paths/blobs match the exact base; and
- no statement implies source activation, review, promotion, release, deployment, or publication.

### M-118 candidate declaration validation

The current workflow validates one proposed inactive descriptor with no network:

```bash
python tools/validators/sources/validate_source_descriptor.py \
  data/registry/sources/geology/kgs-m118-surficial-geology.source.json

python -m pytest -q tests/schemas/test_kgs_m118_source_descriptor.py
```

A green result proves schema/declaration checks only. It does not resolve rights, download or hash M-118, activate a connector, admit source bytes, create evidence, or authorize use.

### Production material-change validation

The current bounded KGS oil-and-gas profile can validate its frozen packets:

```bash
python tools/validators/domains/geology/validate_production_material_change.py \
  fixtures/contracts/v1/domains/geology/production_material_change/valid/material_change_review.json

python -m pytest -q -p no:cacheprovider \
  tests/domains/geology/test_production_material_change.py
```

The profile performs no network request and no source, lifecycle, promotion, or publication write. Its `REVIEW` outcome means material-change review is required; it does not mean review occurred.

### No-network qualification

`KFM_NO_NETWORK=1` plus in-process guards is a bounded application-level control, not an operating-system firewall, network namespace, proxy policy, or universal proof of zero egress. Use the exact qualification in [NO_NETWORK_TEST_RUNBOOK.md](./NO_NETWORK_TEST_RUNBOOK.md).

[Back to top](#top)

---

## Handoff boundary

### Minimum handoff record

```yaml
procedure: geology-source-refresh-inspection
repository_revision: <40-hex commit>
source_id: <canonical id or null>
descriptor_version: <version or null>
signal_ref: <immutable authorized source-head ref or null>
comparison_profile: <exact profile id/version or null>
procedure_disposition: <NO_CHANGE_CANDIDATE|MATERIAL_CHANGE_CANDIDATE|HOLD|ABSTAIN|RESTRICT|DENY|ERROR>
reason_codes: []
evidence_refs: []
rights_state: <finite state>
sensitivity_state: <finite state>
source_fetch_performed: false
review_state: NOT_PERFORMED
transition_applied: false
public_effect: none
```

This example is explanatory and not a canonical schema specimen.

### Appropriate owning roles

A future live path may require distinct source, connector, Geology semantics, rights, sensitivity, evidence/proof, policy, validation, security, review, lifecycle, release, correction/rollback, and operations roles. At the pinned revision, accountable assignments and independent review remain `NEEDS VERIFICATION`.

Do not infer stewardship from file authorship, CODEOWNERS routing, a workflow actor, or a generated receipt.

### Handoff non-effects

Delivering the packet does not:

- admit, activate, suspend, or withdraw a source;
- perform or schedule a fetch;
- create a receipt or EvidenceBundle;
- request or complete review;
- open a promotion candidate;
- cross a lifecycle boundary;
- change a descriptor, alias, cache, tile, catalog, deployment, or public carrier; or
- release, deploy, promote, or publish.

[Back to top](#top)

---

## Anti-patterns to refuse

| Anti-pattern | Required response |
|---|---|
| Run an illustrative watcher command copied from planning prose | `DENY`; resolve accepted connector/runtime first |
| Treat a proposed/disabled descriptor as active | `HOLD` |
| Infer authority from the empty source-authority projection | `HOLD` |
| Write independently to the domain-first compatibility lane | `DENY`; use accepted topology/migration authority |
| Pick among conflicted KGS/KSGS connector paths by convenience | `HOLD` |
| Treat HTTP 200/304, timestamp, or `etag` as sufficient content evidence | `ABSTAIN` or `HOLD` |
| Treat `NO_CHANGE` as proof a watcher ran or source is current | `HOLD`; require authenticated signal/receipt authority |
| Treat `REVIEW` as performed review or approval | `DENY`; preserve `review_state: NOT_PERFORMED` |
| Apply the production material-change profile to another source family | `HOLD`; require an accepted profile |
| Collapse production/permit/estimate/reserve or model/observation roles | `DENY` |
| Put protected subsurface/resource detail in a public packet | `RESTRICT` or `DENY`; contain immediately |
| Auto-open promotion, rebuild tiles, invalidate caches, or publish on change | `DENY`; hand off to owning governance |
| Use AI output as a source-head, evidence, policy, or review object | `ABSTAIN` or `DENY` |

[Back to top](#top)

---

## Open verification register

- [ ] Establish accountable source, connector, Geology, rights, sensitivity, evidence, policy, review, lifecycle, release, correction, rollback, security, and operations ownership.
- [ ] Reconcile the domain-first Geology YAML records with the accepted subtype-first source-registry topology through explicit migration, mirror, tombstone, or removal governance.
- [ ] Populate or deliberately retire the empty machine source-authority projection through its owning process.
- [ ] Resolve KGS/KSGS connector path, package, product-dispatch, credential, fixture, test, activation, correction, and rollback topology.
- [ ] Resolve M-118 rights/terms, source-head content identity, admitted role, connector path, activation, evidence, policy, review, and release prerequisites without treating the descriptor candidate as permission.
- [ ] Keep the GMD 3 AEM source disabled until official product identity, endpoint, rights, acquisition state, evidence, and cross-domain ownership are verified.
- [ ] Establish accepted source-specific materiality profiles; do not generalize the production profile.
- [ ] Establish authenticated source-head signals, canonicalization rules, immutable receipts, correction/supersession lineage, and replay/audit handling.
- [ ] Establish active Geology policy evaluation and EvidenceBundle/proof closure before any downstream candidate path.
- [ ] Establish restricted handling, public-safe representation, invalidation, rollback, and incident drills.
- [ ] Verify downstream public consumers only after a separately governed release exists.

Every open item is separate from this documentation change and remains held until its owning authority records exact-revision evidence.

[Back to top](#top)

---

## Evidence basis

| Evidence | Status | Supports | Limit |
|---|---|---|---|
| Geology runbook lane README at `main@0f9e4f6f7730…` | `CONFIRMED` | Direct-child placement and instruction-only boundary | Does not establish a refresh path |
| Accepted Directory Rules and registry READMEs | `CONFIRMED` | Subtype-first canonical writer; domain-first compatibility restriction | Existing domain-first YAMLs create recorded-state conflict |
| Machine source-authority projection | `CONFIRMED` empty/absent posture | No authority is established by its entries | Does not enumerate external/live authority |
| M-118 descriptor and workflow | `CONFIRMED` proposed inactive candidate and no-network validation | Declaration/schema checks and explicit non-effects | No rights resolution, fetch, content hash, activation, or admission |
| GMD 3 AEM record | `CONFIRMED` proposed/disabled/noncanonical | Announcement-bound planning identity and explicit unknown product state | No endpoint, acquisition evidence, or released product |
| Connector compatibility documentation | `CONFIRMED` mixed/conflicted, README-heavy topology | No general Geology connector path is established | Differently named/runtime-only systems remain unknown |
| Production material-change contract/schema/validator/tests | `CONFIRMED` bounded no-network profile | Version-pinned KGS production metadata comparison | Not a generic watcher or live source truth |
| Geology policy and workflow | `CONFIRMED` default-only/held posture | Active policy and broader release maturity are unestablished | Green bounded tests do not activate or publish |
| Live source operations, scheduler, credentials, production receipts, logs | `UNKNOWN` in this update | — | No operational claim is made |

Proposal-era source-family tables, cadence values, watcher commands, automatic no-op receipt claims, and promotion flows are retained only as historical planning lineage outside current authority. Current repository evidence governs this procedure.

[Back to top](#top)

---

## Document change rollback

The prior proposal-era blob for this path is:

```text
e0a6d4e39f01bc957fe4bc66b6b918a376503b18
```

Revert the documentation commit or restore that blob in a reviewed follow-up if this reconciliation is incorrect. Reverting this Markdown performs no source activation/deactivation, fetch, receipt emission, lifecycle mutation, review, promotion, release, deployment, cache invalidation, rollback execution, or publication.

After any correction, update the lane README's child maturity summary and evidence snapshot through a separate exact-revision documentation change if necessary.

[Back to top](#top)

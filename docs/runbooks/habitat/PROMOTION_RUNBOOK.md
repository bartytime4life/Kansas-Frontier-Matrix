<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook/habitat/promotion
title: Habitat Promotion Runbook
type: runbook; operational-procedure; domain-lane; non-authoritative
version: v2.0.0
prior_version: v1
status: draft; repository-grounded; bounded-readiness-validator-present; no-active-habitat-candidate; source-authority-empty; habitat-policy-inactive; proof-and-release-holds; join-induced-sensitivity-deny-by-default; non-publisher
owners:
  - "@bartytime4life — verified GitHub review route only"
  - "NEEDS VERIFICATION — accountable Habitat, ecology, source, rights, sensitivity/geoprivacy, evidence, policy, validation, release, correction, rollback, operations, and independent-review assignments"
created: 2026-05-12
updated: 2026-08-25
policy_label: restricted-review; habitat; promotion-readiness; fail-closed; no-release-authority; no-publication-authority
current_path: docs/runbooks/habitat/PROMOTION_RUNBOOK.md
owning_root: docs/
responsibility: >-
  Provide the repository-grounded human procedure for evaluating one
  specifically identified Habitat candidate for accountable release review
  without granting source admission, ecological or regulatory authority,
  evidence, rights, sensitivity, policy, review, lifecycle-transition, release,
  deployment, or publication authority.
truth_posture: cite-or-abstain
truth_labels: [CONFIRMED, PROPOSED, UNKNOWN, NEEDS VERIFICATION, CONFLICTED, HOLD]
authority_class: explanatory operational documentation
path_posture: PLACE
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  content_inspection_commit: 434195e8727e6e8649fd6a9e7de06808c3e15261
  prior_blob: d67eeba7f839d07a7f142922f8fcfedee22f7323
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  promotion_sequence_adr_blob: 51cedfdf98b92f1a9af492ce3a1cde231eed9308
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  habitat_candidate_readme_blob: e55b9344cda673e069bce5525937f5a50666bf63
  ecoregion_candidate_readme_blob: d8946a7181fe0f141a1ae43c28755baf54d28a1c
  habitat_fauna_candidate_readme_blob: d5c3990bfdf8563721724d1e885022f28ba3f1df
  source_authority_register_blob: 32729857bc8eb5001acb37b8ee8e60bcb6e0dc50
  policy_gate_register_blob: bc8185b4762a947c742cf54a7ea4f2bf80670e21
  habitat_source_registry_readme_blob: 5d9c90f88ff7e2e2b0d4f2064bc835589196d8b8
  habitat_policy_readme_blob: cf6dd24db1a06cb857806c000500471bbe918ad7
  promotion_policy_readme_blob: 79287df1d828010d716ed43d2e24d6dbd610305b
  habitat_workflow_blob: 59771c027f688d7028a46c4635c0ec710b34e3ab
  promotion_gate_readme_blob: e729df0cc007e8cf0d9811afc25ec1f5ffbdffdd
  promotion_gate_workflow_blob: 9b567aad17de2a7419a2a0238386745c1cb5c11c
  habitat_proof_readme_blob: be4e0a82a86f12972de6f78e82fd3ca051618077
  habitat_published_readme_blob: 91ecc1c0e845b03fc0874c28f634b46978a6edce
inspection_boundary: >-
  Current-session GitHub reads of the exact target, accepted Directory Rules,
  proposed promotion-sequence ADR, Habitat candidate/source/policy/validation/
  proof/published boundaries, shared promotion validator and workflow,
  release-review guidance, and CODEOWNERS. Google Drive Habitat architecture
  material was used only as non-authoritative planning lineage. No protected
  ecological payload, live source, production policy evaluator, governed
  EvidenceBundle resolver, release service, deployed public surface, or
  lifecycle transition was exercised.
related:
  - ../README.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../adr/ADR-0018-promotion-gate-sequence.md
  - ../../doctrine/directory-rules.md
  - ../../domains/habitat/README.md
  - ../../domains/habitat/MODEL_VS_OBSERVATION.md
  - ../../domains/habitat/SENSITIVITY.md
  - ../../../control_plane/source_authority_register.yaml
  - ../../../control_plane/policy_gate_register.yaml
  - ../../../data/registry/sources/habitat/README.md
  - ../../../data/proofs/habitat/README.md
  - ../../../data/published/habitat/README.md
  - ../../../data/published/layers/habitat/README.md
  - ../../../policy/domains/habitat/README.md
  - ../../../policy/promotion/README.md
  - ../../../release/candidates/habitat/README.md
  - ../../../release/candidates/habitat/ecoregions/README.md
  - ../../../release/candidates/habitat/habitat_fauna_thin_slice/README.md
  - ../../../release/reviews/README.md
  - ../../../tools/validators/promotion_gate/README.md
  - ../../../.github/workflows/domain-habitat.yml
  - ../../../.github/workflows/promotion-gate.yml
  - ../../../.github/CODEOWNERS
  - ./NO_NETWORK_TEST_RUNBOOK.md
  - ./SOURCE_REFRESH_RUNBOOK.md
  - ./ROLLBACK_RUNBOOK.md
tags: [kfm, habitat, runbook, promotion, readiness, land-cover, model, observation, ecoregions, sensitivity, geoprivacy, evidence, policy, review, release, correction, rollback, fail-closed]
notes:
  - "v2.0.0 replaces proposal-era no-mounted-repository assumptions, guessed paths, lifecycle-wide file-move language, and speculative commands with current repository evidence and a bounded final-readiness procedure."
  - "The shared A-G validator is executable, deterministic, no-network, read-only, and non-publishing. PASS means APPROVE_READY for accountable review only."
  - "The Habitat workflow executes one synthetic land-cover materiality profile; Habitat proof production and release dry run remain explicit holds."
  - "The governed Habitat candidate tree contains a parent index plus ecoregions and Habitat x Fauna child indexes, but no non-README candidate record was established."
  - "Inspected Habitat source YAMLs are PROPOSED inventory placeholders; the central source-authority register remains empty."
  - "Habitat policy and shared promotion policy are proposed, evaluator-unbound, and inactive."
  - "No Habitat PromotionDecision, PromotionReceipt, accountable release ReviewRecord, ReleaseManifest, emitted proof payload, or released carrier was established."
  - "This document changes no source, data, contract, schema, policy, fixture, validator, workflow, evidence object, receipt, proof, review, release record, deployment, lifecycle state, or public surface."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat Promotion Runbook

> **Evaluate whether one specifically identified Habitat candidate has enough governed, public-safe support for accountable release review. Never translate documentation, a placeholder descriptor, fixture success, green workflow, schema-valid packet, `APPROVE_READY`, map rendering, or model output into promotion, release, deployment, or publication.**

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#current-repository-posture)
[![Candidate: absent](https://img.shields.io/badge/candidate-NO__ACTIVE__CANDIDATE-critical?style=flat-square)](#current-repository-posture)
[![A-G validator: bounded](https://img.shields.io/badge/A--G%20validator-bounded-0969da?style=flat-square)](#bounded-a-g-readiness-profile)
[![Habitat policy: inactive](https://img.shields.io/badge/Habitat%20policy-inactive-b42318?style=flat-square)](#current-repository-posture)
[![Proof and release: hold](https://img.shields.io/badge/proof%20%2B%20release-HOLD-d4a72c?style=flat-square)](#current-repository-posture)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#authority-boundary-and-handoff)

> [!IMPORTANT]
> **Promotion is a governed state transition, not a file move, commit, pull request, merge, workflow result, badge, candidate folder, catalog row, manifest-shaped file, model run, tile build, map-layer toggle, deployment, or generated summary.**

> [!CAUTION]
> **Current Habitat promotion is `HOLD`.** The governed candidate tree has a parent index and two child indexes, but no non-README candidate record. The central source-authority and policy-gate projections are empty. Habitat policy is proposed and evaluator-unbound. The Habitat workflow proves only a synthetic land-cover materiality profile and explicitly holds proof production and release dry-run work. No accountable Habitat release review, `PromotionDecision`, transition receipt, `ReleaseManifest`, emitted proof payload, or released carrier was established.

> [!WARNING]
> **Exact or reverse-engineerable ecological locations fail closed.** Do not expose rare-species context, nests, dens, roosts, hibernacula, spawning or breeding sites, migration bottlenecks, sensitive plant records, steward-controlled zones, private-land joins, cultural or archaeological context, infrastructure associations, access clues, withholding logic, or transform parameters in a candidate packet, pull request, log, screenshot, map, export, graph, cache, or AI answer.

**Quick navigation:** [Purpose](#purpose) · [Current posture](#current-repository-posture) · [Placement](#directory-rules-basis) · [Scope](#scope-and-authority-boundary) · [Lifecycle](#lifecycle-and-object-family-separation) · [Preflight](#preflight-and-mandatory-stops) · [Procedure](#promotion-readiness-procedure) · [Habitat gates](#habitat-specific-gates) · [A-G profile](#bounded-a-g-readiness-profile) · [Validation](#current-executable-validation) · [Packet](#candidate-review-packet) · [Outcomes](#finite-outcomes-and-current-holds) · [Handoff](#authority-boundary-and-handoff) · [Recovery](#correction-withdrawal-and-rollback) · [Checklist](#operator-checklist) · [Open work](#open-verification-register) · [Evidence](#evidence-basis) · [History](#change-history-and-no-loss-map) · [Document rollback](#document-change-rollback)

---

<a id="purpose"></a>

## Purpose

Use this runbook only for a bounded Habitat candidate already declared at `CATALOG` or `TRIPLET` and seeking a separately authorized transition toward a public-safe `PUBLISHED` carrier.

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

This runbook does not operate every lifecycle transition. Source intake, normalization, quarantine exit, processing, catalog construction, proof production, release execution, correction, and rollback remain owned by their own contracts, schemas, policy, pipelines, validators, records, and accountable humans.

The operator's product is an inspectable readiness or blocked handoff. A completed checklist cannot create missing authority.

### This runbook can establish

- the exact repository snapshot, candidate identity, and requested lifecycle boundary;
- whether a real dossier exists beyond a README or `.gitkeep`;
- which repository-native checks apply;
- which support is present, absent, stale, conflicted, unresolved, or merely proposed;
- which Habitat object-family, source-role, model/observation, regulatory/model, regionalization, sensitivity, geoprivacy, rights, temporal, spatial, uncertainty, and cross-domain distinctions must remain visible;
- whether the bounded A-G validator can evaluate the declared packet; and
- which finite non-publishing disposition and accountable handoff apply.

### This runbook cannot establish

- source admission, activity, authority, currency, or rights clearance;
- ecological correctness, species presence, legal effect, or management approval;
- public safety from client-side hiding or omitted fields;
- evidence authenticity merely because a reference is present;
- active policy merely because Rego source exists;
- reviewer qualification, assignment, independence, or authority;
- transition execution from a valid decision, receipt, or manifest shape; or
- promotion, release, deployment, publication, or public availability.

When this runbook conflicts with accepted ADRs, Directory Rules, current contracts, schemas, policy, source-admission records, EvidenceBundles, validators, review records, release decisions, correction records, rollback records, or runtime evidence, stop and record the conflict.

[Back to top](#top)

---

<a id="current-repository-posture"></a>

## Current repository posture

These conclusions are bounded to `main@434195e8727e6e8649fd6a9e7de06808c3e15261`.

| Surface | Status | Safe conclusion |
|---|---|---|
| Target path | **CONFIRMED** | Existing same-path documentation update. |
| Directory governance | **CONFIRMED / accepted** | ADR-0029 adopts Directory Rules v2; `docs/runbooks/` owns human operational procedures. |
| Promotion sequence | **CONFIRMED / proposed** | ADR-0018 remains proposed. Its narrow A-G names match the executable final-readiness validator but are not accepted universal authority. |
| Candidate inventory | **CONFIRMED / no active candidate** | Parent plus `ecoregions/` and `habitat_fauna_thin_slice/` README indexes exist; no non-README candidate record or child dossier was established. |
| Source-authority projection | **CONFIRMED / empty** | `PROPOSED`, projection-only, `implementation_status: ABSENT`, `entries: []`. |
| Habitat source registry | **CONFIRMED guidance / unresolved topology** | Subtype-first and domain-first source homes remain unresolved. Inspected NLCD and GAP/LANDFIRE YAMLs are `PROPOSED` placeholders, not admitted sources. |
| Habitat policy | **CONFIRMED / inactive and conflicted** | Eighteen default-only Rego scaffolds and marker-only children; no accepted package, entrypoint, native Rego tests, bundle, selector, evaluator, or governed consumer. |
| Promotion policy | **CONFIRMED / inactive** | Two no-op `PROPOSED` Rego stubs; not executed by the promotion workflow. |
| Policy-gate projection | **CONFIRMED / empty** | `PROPOSED`, projection-only, `implementation_status: ABSENT`, `entries: []`. |
| Habitat validation | **CONFIRMED / bounded** | One deterministic, synthetic, no-network land-cover materiality profile is executable. |
| Habitat proof | **CONFIRMED / HOLD** | No accepted proof producer or deterministic proof command. `data/proofs/habitat/` contains only README and `.gitkeep`. |
| Habitat release dry run | **CONFIRMED / HOLD** | No accepted command or candidate-manifest contract. |
| Shared readiness | **CONFIRMED / bounded** | Seven-gate, no-network, read-only validator; `PASS` means `APPROVE_READY` for accountable review only. |
| Published Habitat lanes | **CONFIRMED guidance / no payload** | Domain, layer, ecoregion, and land-cover lanes contain READMEs and `.gitkeep` markers; no emitted released carrier was established. |
| Habitat release records | **NOT ESTABLISHED** | No Habitat-specific governed release review, `PromotionDecision`, or `ReleaseManifest` surfaced in bounded search. |
| Review route | **CONFIRMED / routing only** | `@bartytime4life` is the verified GitHub route. Functional and independent release roles remain unverified. |
| Public runtime | **UNKNOWN** | No deployed governed Habitat endpoint, carrier readback, cache behavior, rollback drill, or SLO evidence was exercised. |

### Current determination

```text
Non-README Habitat candidate: not established
Admitted source: not established by central authority projection
Active Habitat policy: not established
Habitat proof payload: not established
Accountable release review: not established
PromotionDecision / transition receipt / ReleaseManifest: not established
Released Habitat carrier: not established
Operator disposition: NO_ACTIVE_CANDIDATE_VERIFIED / HOLD
```

This does not prove that no Habitat material exists elsewhere. It means the governed release path inspected here does not establish an active candidate or public release.

[Back to top](#top)

---

<a id="directory-rules-basis"></a>

## Directory Rules basis

The target remains:

```text
docs/runbooks/habitat/PROMOTION_RUNBOOK.md
```

Placement is **PLACE** because `docs/runbooks/` owns human operational procedures, `habitat/` is a domain segment within that responsibility root, the file already exists, and this change creates no parallel authority.

| Concern | Authority home | Relationship |
|---|---|---|
| Habitat meaning | [`docs/domains/habitat/`](../../domains/habitat/README.md) and accepted contracts | Referenced, not redefined. |
| Source admission | [`data/registry/sources/habitat/`](../../../data/registry/sources/habitat/README.md) and owning admission records | Required input, not created here. |
| Habitat policy | [`policy/domains/habitat/`](../../../policy/domains/habitat/README.md) | Required home; currently inactive. |
| Promotion policy | [`policy/promotion/`](../../../policy/promotion/README.md) | Shared source; currently inactive. |
| Candidate dossiers | [`release/candidates/habitat/`](../../../release/candidates/habitat/README.md) | Governed pre-publication lane. |
| Proof support | [`data/proofs/habitat/`](../../../data/proofs/habitat/README.md) | Required support; not release authority. |
| Validation | [`tools/validators/`](../../../tools/validators/promotion_gate/README.md), `tests/`, workflows | Findings only. |
| Review | [`release/reviews/`](../../../release/reviews/README.md) | Separate accountable record family. |
| Decisions, receipts, manifests | `release/` plus accepted contracts and schemas | Separate families; not emitted here. |
| Published carriers | [`data/published/`](../../../data/published/habitat/README.md) | Downstream only after governed release. |

[Back to top](#top)

---

<a id="scope-and-authority-boundary"></a>

## Scope and authority boundary

This runbook may assess public-safe derivatives of Habitat-scoped objects such as:

- `LandCoverObservation`, `HabitatPatch`, and `EcologicalSystem`;
- `HabitatQualityScore`, `SuitabilityModel`, and `UncertaintySurface`;
- `ConnectivityEdge`, `Corridor`, and `RestorationOpportunity`;
- `StewardshipZone` and model/transform receipts;
- an ecoregion-context carrier; or
- a public-safe Habitat x Fauna relation derivative preserving both domain ownership and the most-restrictive sensitivity posture.

Documentation names do not prove accepted contracts or schemas. The candidate must cite the accepted versions used at its pinned snapshot.

This runbook does **not**:

- discover, retrieve, activate, normalize, or quarantine sources;
- create evidence or decide neighboring-domain truth;
- establish legal or regulatory interpretation;
- run a live model or choose generalization parameters;
- activate policy or authenticate reviewers;
- create a decision, receipt, manifest, correction, withdrawal, or rollback record;
- mutate lifecycle state or write published bytes;
- deploy, update aliases/caches, or authorize API, UI, map, export, graph, or AI behavior.

Normal public clients use governed APIs and released public-safe carriers. They do not read internal lifecycle stores, candidate directories, registries, proof-working lanes, review-only records, policy source, or direct model output. Styling is not an access control.

### Separation of duties

Candidate author, Habitat steward, source/rights reviewer, sensitivity reviewer, evidence/proof steward, model reviewer, policy steward, validation owner, public-surface reviewer, release reviewer, transition authority, rollback owner, and operations owner are distinct functions when consequence requires it. Current assignments remain `NEEDS VERIFICATION`.

CODEOWNERS routing is not qualification, assignment, independence, or approval. If independent authority cannot be verified, use `HOLD_FOR_REVIEW_AUTHORITY`.

[Back to top](#top)

---

<a id="lifecycle-and-object-family-separation"></a>

## Lifecycle and object-family separation

```text
candidate + source/evidence/policy/validation context
-> readiness findings
-> accountable ReviewRecord
-> PromotionDecision
-> authorized transition operator
-> PromotionReceipt
-> ReleaseManifest
-> released public-safe carrier
-> governed public readback
-> correction / withdrawal / rollback
```

Each arrow is a separate responsibility.

| Family | Can support | Cannot prove by itself |
|---|---|---|
| Source descriptor/admission | Source identity, role, rights, cadence, sensitivity, allowed use. | Habitat truth, evidence closure, release. |
| Candidate dossier | Subject, artifacts, requested boundary, support pointers, blockers. | Approval or public state. |
| Receipt | What a process declared it ran and produced. | Ecological truth, rights, policy, review, release. |
| Validation report | Bounded checks and findings. | Source/reviewer authority or publication. |
| EvidenceBundle | Claim-scoped admissible support and limitations. | Policy or transition authority. |
| Policy result | Evaluation under an accepted policy context. | Evidence truth, live reviewer authority, applied transition. |
| Readiness `PASS` | `APPROVE_READY` under the bounded declared profile. | `APPROVE`, promotion, release, deployment, publication. |
| ReviewRecord | Accountable review when identity, authority, scope, independence, and validity are authenticated. | Transition execution. |
| PromotionDecision | Governed decision for named candidate and boundary. | Proof the transition occurred. |
| PromotionReceipt | Declared transition-attempt consistency and binding. | Support authenticity or public deployment. |
| ReleaseManifest | Released artifact set and rollback relationship when authentic and authorized. | Ecological truth or deployment readback. |
| Published carrier | Released public-safe bytes. | Canonical truth or evidence authority. |
| Correction/rollback records | Governed change and public lineage. | Permission to restore unsafe bytes. |

This runbook begins at final readiness. It cannot retroactively certify earlier lifecycle transitions.

[Back to top](#top)

---

<a id="preflight-and-mandatory-stops"></a>

## Preflight and mandatory stops

Record:

```text
repository / base_commit / branch_or_pr
candidate_id / dossier_path / author
current_state / requested_state / spec_hash
artifact_digests / evaluation_time_utc
known_overlapping_branch_or_pr
```

Do not invent a candidate ID or use a README, `.gitkeep`, illustrative release row, source placeholder, fixture, generated summary, or map layer as a candidate substitute.

Stop when any applies:

1. no real non-README candidate;
2. unpinned or overlapping repository/candidate state;
3. missing or contradictory candidate identity/digests;
4. current state is not `CATALOG` or `TRIPLET`, or requested state is not `PUBLISHED`;
5. unadmitted source, unknown rights, or unresolved stewardship;
6. unresolved EvidenceRefs or mismatched EvidenceBundle scope;
7. model/observation, regulatory/model, aggregate/observed, or regionalization/occurrence collapse;
8. output-level sensitivity or inference risk is unresolved;
9. exact or reverse-engineerable protected detail remains;
10. policy bundle/evaluator/result is inactive or unknown;
11. deterministic positive, negative, no-network, or candidate-specific validation is missing/failing;
12. accountable and independent review authority is unverified;
13. correction, withdrawal, derivative invalidation, rollback, or public-surface inventory is incomplete;
14. sensitive detail would enter Git, logs, screenshots, or public prose.

At the pinned snapshot, condition 1 applies. Stop at `NO_ACTIVE_CANDIDATE_VERIFIED`; do not fabricate candidate-specific validation.

[Back to top](#top)

---

<a id="promotion-readiness-procedure"></a>

## Promotion-readiness procedure

### 1. Pin authority and overlap

Pin the exact commit, candidate bytes, accepted Directory Rules, applicable ADRs, and open same-byte/same-candidate work. Record ADR-0018 as proposed.

```bash
git rev-parse HEAD
git status --short
git diff --name-status origin/main...HEAD
```

Blocked: `HOLD_FOR_AUTHORITY` or `HOLD_FOR_OVERLAP`.

### 2. Establish a real candidate

```bash
find release/candidates/habitat \
  -type f \
  ! -name 'README.md' \
  ! -name '.gitkeep' \
  -print
```

Require stable candidate identity, requested boundary, immutable artifact pointers and digests, contract/schema versions, author, support references, policy context, review needs, public-surface scope, correction path, and rollback target.

Current result: no candidate established.

Blocked: `NO_ACTIVE_CANDIDATE_VERIFIED` or `HOLD_FOR_CANDIDATE`.

### 3. Classify object family and knowledge character

Record:

- Habitat object family;
- source role: `observed`, `regulatory`, `modeled`, `aggregate`, `administrative`, `candidate`, or `synthetic`;
- source-native, normalized, derived, modeled, aggregated, generalized, or released character;
- neighboring-domain dependencies;
- representation, CRS, extent, resolution, scale, topology, geometry digest;
- source, observation, valid, retrieval, model-run, publication, effective, correction, and transaction times as applicable;
- uncertainty, fitness, omissions, and prohibited interpretations.

Blocked: `HOLD_FOR_SEMANTICS`, `ABSTAIN`, or `DENY`.

### 4. Verify source admission and rights

For every source, resolve stable ID, role, version/head, authority scope, cadence, rights/terms/attribution, sensitivity floor, steward controls, activation/admission decision, supersession, correction, and withdrawal posture.

Do not treat current NLCD, GAP/LANDFIRE, GBIF, KDWP, NatureServe, NWI, PAD-US, or other inventory placeholders as admitted sources by presence.

Current systemic hold: central source-authority projection is empty.

Blocked: `HOLD_FOR_SOURCE_ADMISSION`, `HOLD_FOR_RIGHTS`, `ABSTAIN`, or `DENY`.

### 5. Close evidence, identity, space, time, and integrity

Verify:

- consequential claims resolve `EvidenceRef` to admissible `EvidenceBundle`;
- scope, source role, place, time, scale, limitations, rights, sensitivity, and integrity match;
- candidate, manifest, receipt, and artifact digests agree;
- geometry, CRS, coordinate order, temporal intervals, and stale/superseded state are explicit;
- catalog/provenance references close without becoming truth;
- model/AI mediation carries required receipts without replacing evidence.

Blocked: `HOLD_FOR_EVIDENCE`, `ABSTAIN`, `DENY`, or `ERROR`.

### 6. Preserve model, regulatory, and regionalization boundaries

For models: require identity/version, input roles, model card or accepted equivalent, run receipt, deterministic inputs, Kansas/scale/time fitness, uncertainty, validation, and prohibited uses.

For regulation: preserve issuing authority, legal scope, effective time, and non-equivalence to model output.

For ecoregions/context: preserve framework, hierarchy, level, source/boundary versions, crosswalk loss, and the rule that context does not prove occurrence or habitat quality.

Blocked: `HOLD_FOR_MODEL_REVIEW`, `HOLD_FOR_REGULATORY_SCOPE`, `ABSTAIN`, or `DENY`.

### 7. Evaluate sensitivity and every public carrier

Evaluate the **produced output**, not only inputs.

- enumerate direct and inferred sensitive relationships;
- apply the most-restrictive posture;
- detect exact, narrowed, clustered, differenced, or reverse-engineerable detail;
- require public-safe transformation before rendering/serving;
- bind transform identity, input/output digests, review, reasons, obligations, and rollback;
- test tiles, properties, APIs, exports, search, graph edges, logs, caches, screenshots, and AI;
- keep transform parameters and withholding logic protected.

Blocked: `HOLD_FOR_SENSITIVITY`, `HOLD_FOR_GEOPRIVACY`, `DENY`, or `ERROR`.

### 8. Run repository-native Habitat checks

Current executable slice:

```bash
python -m unittest discover \
  --start-directory tests/validators/domains/habitat \
  --pattern 'test_land_cover_materiality.py' \
  --verbose

python tools/validators/domains/habitat/validate_land_cover_materiality.py --fixtures
```

This proves only deterministic synthetic land-cover materiality behavior and shared `MaterialChangeAssessment` shape.

Current explicit holds:

```text
WORKFLOW_HOLD: no accepted Habitat proof producer or deterministic proof command
WORKFLOW_HOLD: no accepted Habitat release dry-run command or candidate manifest contract
```

Blocked: `HOLD_FOR_VALIDATION`, `HOLD_FOR_PROOF`, or `ERROR`.

### 9. Run bounded A-G readiness only for a real packet

```bash
make publish-check
python tools/validators/validate_promotion_gate.py candidate.json
```

The validator checks declared closure; it does not dereference support, authenticate authority, evaluate Rego, verify production signatures, mutate state, or inspect deployment.

`PASS` means only `APPROVE_READY`.

Blocked: validator `ABSTAIN`, `DENY`, or `ERROR`.

### 10. Require accepted policy and accountable review

Require accepted policy bundle/digest, entrypoint/input contract, evaluator, candidate-specific result/reasons/obligations/validity/supersession, authenticated reviewer identity and assignment, authority interval, separation, scope/subject/spec/artifact bindings, and closed obligations.

Current result: Habitat and promotion policy are inactive; policy-gate projection is empty; accountable Habitat release-review authority is not established.

Blocked: `HOLD_FOR_POLICY` and `HOLD_FOR_REVIEW_AUTHORITY`.

### 11. Prove recovery and public readback

Require prior safe target, rollback-card identity, correction/withdrawal paths, derivative inventory, cache/search/graph/tile/API/export/AI invalidation, stale/revoked behavior, public readback plan, incident owner, and drill evidence appropriate to consequence.

Blocked: `HOLD_FOR_CORRECTION`, `HOLD_FOR_ROLLBACK`, or `DENY`.

### 12. Assemble handoff and stop

Prepare the packet below. Route it to separately accountable review and release authority. Do not issue a decision, apply a transition, assemble a release manifest, deploy, or publish from this runbook.

[Back to top](#top)

---

<a id="habitat-specific-gates"></a>

## Habitat-specific gates

| Gate | Required distinction | Fail-closed trigger |
|---|---|---|
| Habitat ownership | Habitat owns landscape context, patches, classification, suitability, connectivity, corridors, restoration opportunity, stewardship context, and uncertainty. | Candidate absorbs Fauna, Flora, hydrology, soil, archaeology, people, land-title, or infrastructure truth. |
| Land cover vs habitat | Land-cover classification is not automatically habitat quality, occupancy, conservation value, or management priority. | Candidate upgrades classes without accepted derivation and evidence. |
| Model vs observation | Suitability, connectivity, restoration, and ecological-system models remain modeled/aggregate products. | Model presented as observation, ground truth, legal designation, or presence proof. |
| Regulatory vs modeled | Regulatory products retain issuing authority, scope, effective time, and role. | Model/crosswalk presented as legal designation or legal effect. |
| Ecoregion vs occurrence | Ecoregions are versioned regionalization context. | Polygon presented as species presence, habitat quality, or conservation status. |
| Occurrence ownership | Animal occurrence remains Fauna-owned; plant occurrence remains Flora-owned. | Candidate copies, upgrades, or exposes occurrence truth without owning-lane public-safe support. |
| Most-restrictive join | Output inherits the most restrictive applicable posture and may become more sensitive through inference. | Least-restrictive input, client filtering, or missing label used to justify exposure. |
| Exact-location denial | Exact/reverse-engineerable sensitive ecology or stewardship detail is not public. | Coordinates, grids, paths, clusters, properties, joins, or access clues narrow a protected location. |
| Transform before delivery | Redaction, aggregation, generalization, clipping, or withholding is auditable and server-side/upstream. | Safety depends on styling, omitted UI fields, undocumented parameters, or manual edits. |
| Native classification | NLCD, NWI, GAP, LANDFIRE, EPA ecoregions, PAD-US, and other systems retain version and meaning. | Silent remap/merge/rename without crosswalk, loss note, and receipt. |
| Scale and uncertainty | Scale, resolution, intended use, validation coverage, uncertainty, and prohibited uses remain visible. | Fine-grained conclusion from coarse/generalized support or falsely certain narrative. |
| Time and stale state | Source, observation, model-run, valid, effective, publication, correction, and transaction times stay distinct. | Old/superseded source or model presented as current. |
| Corridor/connectivity | Derived analytical product, not guaranteed movement path or access direction. | Biological function overstated or sensitive endpoint/path exposed. |
| Restoration | Analytical opportunity, not permission, mandate, consent, funding, or prescription. | Prioritization model presented as approved action. |
| Stewardship/admin | Context is not title, access, consent, or legal authority. | Ownership, public access, or authorization implied without owning evidence. |
| Carrier parity | API, tile, map, export, search, graph, cache, screenshot, and AI preserve release/evidence/sensitivity/correction state. | One carrier leaks fields, precision, stale bytes, or unsupported claims. |

Do not place protected geometry, occurrence IDs, restricted source-native fields, transform thresholds/offsets/seeds, private parcel/person links, steward notes, or access-control detail in ordinary Git content. Use governed references and public-safe summaries.

[Back to top](#top)

---

<a id="bounded-a-g-readiness-profile"></a>

## Bounded A-G readiness profile

ADR-0018 remains proposed. This table describes the **implemented narrow validator**, not an accepted universal lifecycle sequence.

| Gate | Implemented name | Declared checks | Failure posture |
|:---:|---|---|---|
| A | Identity and closure | Profile, candidate, author, spec hash, exact boundary, minimal manifest identity. | `DENY` on missing/contradictory identity. |
| B | Asset integrity | Candidate/manifest/receipt hash agreement; unique digest-set equality. | `DENY` on mismatch/invalid digest. |
| C | Geometry and CRS | Declared validity, deterministic processing, `EPSG:4326`, finite ordered bbox. | `DENY` on invalid/nondeterministic geometry. |
| D | Temporal semantics | Strict real UTC seconds, ordered interval, packet-supplied evaluation instant. | `DENY` on malformed/inverted time. |
| E | Rights/sensitivity policy context | Known profile/labels, public-safe discipline, finite declared policy evaluation. | `DENY` on rejection; `ERROR` on evaluator failure. |
| F | Proof and catalog support | Evidence, attestation, STAC/DCAT/PROV, run receipt, conditional AI receipt declarations. | `ABSTAIN` unresolved evidence; `DENY` mandatory integrity/catalog gaps. |
| G | Review and rollback | Fixture-only ReviewRecord shape, canonical identities, declared authority/validity intervals, separation, bindings, rollback, correction. | `DENY` unsafe/contradictory; `ABSTAIN` missing authority/obligations/correction. |

| Validator result | Readiness | Exit | Meaning |
|---|---|---:|---|
| `PASS` | `APPROVE_READY` | `0` | May proceed to accountable review; no public effect. |
| `ABSTAIN` | `BLOCKED` | `1` | Support insufficient without unsafe contradiction. |
| `DENY` | `BLOCKED` | `1` | Mandatory, unsafe, or contradictory condition. |
| `ERROR` | `BLOCKED` | `2` | Could not evaluate safely. |

Precedence: `ERROR > DENY > ABSTAIN > PASS`.

The validator does not admit sources, resolve real evidence, verify rights/sensitivity, evaluate current Rego scaffolds, authenticate identities, choose qualified release roles, verify production signatures, prove transition execution, execute rollback, assemble release, inspect deployment, or grant public permission.

[Back to top](#top)

---

<a id="current-executable-validation"></a>

## Current executable validation

| Command/check | Proves | Does not prove |
|---|---|---|
| Habitat materiality unit command | Synthetic focused unit behavior. | Candidate, source, ecology, policy, proof, release. |
| Habitat materiality fixture command | Deterministic profile findings and shared shape validation. | Live data, rights, sensitivity, evidence, public safety. |
| `make publish-check` | Shared fixture-only ReviewRecord and bounded A-G behavior. | Habitat support authenticity, policy activation, transition. |
| `python tools/validators/validate_promotion_gate.py candidate.json` | Declared packet closure. | Dereferenced evidence, live authority, public state. |
| `domain-habitat` workflow | Synthetic materiality plus proof/release hold detectors. | Habitat release path. |
| `promotion-gate` workflow | Fail-closed doctrine checks, proposed decision shape, A-G proof, review hold. | Authenticated decision, release, publication. |

Rules:

- run at the exact candidate commit;
- record command, dependency lock, time, exit, and output identity as required;
- preserve negative-fixture results;
- classify introduced vs inherited failures against a pinned base;
- do not disable no-network or fail-closed controls to get green;
- do not use unpinned live data or undeclared dependencies as release evidence;
- workflow presence/green state does not prove required-check enforcement;
- docs validation does not change operational Habitat readiness.

[Back to top](#top)

---

<a id="candidate-review-packet"></a>

## Candidate review packet

Include:

1. **Snapshot and identity** — repository/commit, dossier, candidate ID/author, states, spec hash, artifact digests.
2. **Artifact inventory** — immutable pointers, formats, CRS, extent, resolution, scale, geometry digest, public carriers.
3. **Habitat classification** — object family, source role, knowledge character, model/regulatory/context distinctions, native classes/crosswalk loss, prohibited uses.
4. **Source admission** — descriptor/version/head, authority scope, rights/terms/attribution/cadence/sensitivity, admission decision.
5. **Evidence/provenance** — claim list, EvidenceRefs/Bundles, scope/limitations, receipts, catalog closure, unresolved support.
6. **Space/time/uncertainty** — geometry/CRS, temporal kinds, stale state, model fitness/validation/error.
7. **Sensitivity** — output tier/posture, joins, public-safe transforms/receipts, reviewer/obligations, leak testing.
8. **Validation** — exact commands/commit/results, negative fixtures, introduced vs inherited failures.
9. **Policy** — accepted bundle/digest, entrypoint, evaluator, result, reasons, obligations, validity/supersession.
10. **Review/separation** — authenticated identity/assignment/authority interval, independence, scope/subject/hash bindings.
11. **Recovery/public surfaces** — prior target, correction/withdrawal/invalidation/rollback, API/tile/map/export/search/graph/cache/AI readback.
12. **Finite disposition** — one non-publishing outcome, reason codes, blockers, next accountable owner.

The packet may state that restricted support exists and provide its governed reference. It must not reproduce protected bytes or reverse-engineering detail.

```markdown
# Habitat promotion-readiness handoff

## Snapshot
- Commit: <sha>
- Candidate: <id>
- Dossier: <path>
- Boundary: CATALOG | TRIPLET -> PUBLISHED
- Spec hash: <sha256>

## Bounded result
- Operator disposition: <finite outcome>
- A-G validator: PASS | ABSTAIN | DENY | ERROR | NOT_RUN
- Habitat-specific gates: PASS | BLOCKED | NOT_RUN
- Public effect: NONE

## Support
| Family | Status | Safe pointer or blocker |
|---|---|---|
| Source admission | ... | ... |
| Evidence | ... | ... |
| Rights/sensitivity | ... | ... |
| Validation/policy | ... | ... |
| Review authority | ... | ... |
| Correction/rollback | ... | ... |
| Public readback | ... | ... |

## Non-effects
No source activation, lifecycle mutation, promotion, release, deployment, or
publication occurred.
```

[Back to top](#top)

---

<a id="finite-outcomes-and-current-holds"></a>

## Finite outcomes and current holds

| Disposition | Meaning |
|---|---|
| `NO_ACTIVE_CANDIDATE_VERIFIED` | No real dossier at pinned snapshot. |
| `READY_FOR_ACCOUNTABLE_REVIEW` | Real candidate passed bounded declared and Habitat-specific checks; separate decision still required. |
| `HOLD_FOR_CANDIDATE` | Candidate identity/dossier missing. |
| `HOLD_FOR_AUTHORITY` / `HOLD_FOR_OVERLAP` | Applicable authority or active work unresolved. |
| `HOLD_FOR_SOURCE_ADMISSION` / `HOLD_FOR_RIGHTS` | Source or allowed use incomplete. |
| `HOLD_FOR_EVIDENCE` / `HOLD_FOR_PROOF` | Claim support or proof closure incomplete. |
| `HOLD_FOR_SEMANTICS` / `HOLD_FOR_MODEL_REVIEW` | Object/knowledge/model interpretation incomplete. |
| `HOLD_FOR_SENSITIVITY` / `HOLD_FOR_GEOPRIVACY` | Output exposure or transform incomplete. |
| `HOLD_FOR_VALIDATION` | Required deterministic/candidate checks incomplete/failing. |
| `HOLD_FOR_POLICY` | Accepted bundle/evaluator/result missing. |
| `HOLD_FOR_REVIEW_AUTHORITY` | Accountable, current, separated authority unverified. |
| `HOLD_FOR_CORRECTION` / `HOLD_FOR_ROLLBACK` | Recovery and invalidation incomplete. |
| `ABSTAIN` | Insufficient support for the requested readiness claim. |
| `DENY` | Unsafe/prohibited/contradictory condition. |
| `ERROR` | Evaluation could not complete safely. |

Do not use `APPROVED`, `PROMOTED`, `TRANSITION_APPLIED`, `RELEASED`, `DEPLOYED`, `PUBLISHED`, `LIVE`, or `PUBLIC_SAFE` as this runbook's terminal result.

Current direct result:

```text
NO_ACTIVE_CANDIDATE_VERIFIED
```

Current systemic holds:

```text
HOLD_FOR_SOURCE_ADMISSION
HOLD_FOR_PROOF
HOLD_FOR_POLICY
HOLD_FOR_REVIEW_AUTHORITY
HOLD_FOR_ROLLBACK
```

[Back to top](#top)

---

<a id="authority-boundary-and-handoff"></a>

## Authority boundary and handoff

A complete evaluation ends with a handoff:

```text
operator packet
-> Habitat/source/rights/sensitivity/evidence/model/validation review
-> accountable release ReviewRecord
-> governed PromotionDecision
-> authorized transition
-> PromotionReceipt
-> ReleaseManifest
-> released public-safe carrier
-> governed public readback
```

The accountable reviewer must decide whether identity, source admission, evidence, roles, sensitivity, policy, validation, authority, correction, rollback, and public readback are sufficient for the exact candidate.

`@bartytime4life` is the verified GitHub route. The inspected repository evidence does not establish all functional stewardship or independent release roles. Do not invent owners.

[Back to top](#top)

---

<a id="correction-withdrawal-and-rollback"></a>

## Correction, withdrawal, and rollback

Before release, identify:

- affected candidate/decision/receipt/manifest/release IDs;
- known-safe prior target and artifact digests;
- correction and withdrawal triggers;
- source/model supersession;
- affected tiles, APIs, exports, search, graphs, caches, screenshots, and AI projections;
- derivative invalidation and rebuild;
- rollback-card identity, operator, authority, and drill;
- public stale/revoked behavior and readback;
- incident owner and forward-repair path.

Withdraw when rights/terms, sensitivity, source/model status, evidence, public leak, reviewer authority, or release integrity changes.

No silent replacement, history deletion, or restoration of unsafe prior bytes is allowed. “Rebuild from source” is not sufficient when source version, rights, model inputs, transforms, or sensitivity decisions may have changed.

Use [`ROLLBACK_RUNBOOK.md`](./ROLLBACK_RUNBOOK.md) for lane-specific execution after reconciling its current grounding. This runbook verifies recovery readiness; it does not execute rollback.

[Back to top](#top)

---

<a id="operator-checklist"></a>

## Operator checklist

- [ ] Exact repository/candidate commits and overlap are recorded.
- [ ] A real non-README candidate exists with stable identity/digests and exact boundary.
- [ ] Habitat object family, source role, knowledge character, scale/time/uncertainty, native classes, and prohibited uses are explicit.
- [ ] Land cover, model, regulatory, ecoregion, occurrence, stewardship, restoration, and corridor meanings are not collapsed.
- [ ] Every source is admitted for the exact use/audience with rights and sensitivity resolved.
- [ ] Every consequential claim resolves to scope-matched EvidenceBundle support.
- [ ] Output-level sensitivity and most-restrictive joins are evaluated.
- [ ] Public-safe transforms occur before delivery and do not expose control-defeating details.
- [ ] Candidate-specific positive, negative, deterministic, and no-network validation runs at exact commit.
- [ ] Workflow holds are not reported as release passes.
- [ ] A-G result is recorded; `PASS` is only `APPROVE_READY`.
- [ ] Accepted policy bundle/evaluator/result and authenticated independent review exist.
- [ ] Correction, withdrawal, invalidation, rollback, and public readback are defined.
- [ ] One finite non-publishing disposition and next accountable authority are recorded.
- [ ] No source activation, lifecycle mutation, release, deployment, or publication occurred.

Current result: the real-candidate requirement fails. Stop at `NO_ACTIVE_CANDIDATE_VERIFIED`.

[Back to top](#top)

---

<a id="open-verification-register"></a>

## Open verification register

| ID | Item | Current status | Effect |
|---|---|---|---|
| `HAB-PROMO-V-001` | Real candidate dossier/payload inventory | Not established | Candidate hold |
| `HAB-PROMO-V-002` | Accepted Habitat source-registry topology | Conflicted | Source hold |
| `HAB-PROMO-V-003` | Authoritative admitted sources/activation decisions | Empty central projection | Source hold |
| `HAB-PROMO-V-004` | Source-specific rights, terms, attribution, cadence, steward controls | Needs verification | Rights hold |
| `HAB-PROMO-V-005` | Accepted candidate contracts/schemas | Needs verification | Semantics hold |
| `HAB-PROMO-V-006` | Evidence resolver, proof producer, emitted proof inventory | Workflow hold | Proof hold |
| `HAB-PROMO-V-007` | Accepted Habitat policy package/bundle/evaluator | Inactive/conflicted | Policy hold |
| `HAB-PROMO-V-008` | Active promotion policy and policy-gate entry | Absent | Policy hold |
| `HAB-PROMO-V-009` | Candidate model fitness/uncertainty review | Unknown | Model hold |
| `HAB-PROMO-V-010` | Public-safe transform profile and carrier leak tests | Needs verification | Sensitivity hold |
| `HAB-PROMO-V-011` | Candidate-specific validators/negative fixtures | Unknown | Validation hold |
| `HAB-PROMO-V-012` | Habitat proof and release-dry-run commands | Workflow hold | Proof/release hold |
| `HAB-PROMO-V-013` | Candidate-manifest contract and assembly path | Not established | Candidate hold |
| `HAB-PROMO-V-014` | Functional stewards and independent release authority | Needs verification | Review hold |
| `HAB-PROMO-V-015` | ADR-0018 acceptance or accepted successor | Proposed | Normative-sequence hold |
| `HAB-PROMO-V-016` | Required-check coupling | Needs verification | Operational assurance hold |
| `HAB-PROMO-V-017` | Habitat review/decision/receipt/manifest instances | Not established | No release authority |
| `HAB-PROMO-V-018` | Deployed public carrier and governed readback | Unknown | No publication claim |
| `HAB-PROMO-V-019` | Correction/withdrawal/cache invalidation/rollback drill | Needs verification | Recovery hold |
| `HAB-PROMO-V-020` | Complete external/restricted consumer inventory | Unknown | Recovery hold |
| `HAB-PROMO-V-021` | Sibling runbook and lane-index convergence | In progress/outside target | Documentation follow-up |

Do not convert open items into plausible defaults.

[Back to top](#top)

---

<a id="evidence-basis"></a>

## Evidence basis

### Current repository evidence

This revision used direct reads of:

- the exact target and accepted Directory Rules decision;
- proposed ADR-0018;
- Habitat parent and child candidate indexes;
- empty source-authority and policy-gate projections;
- Habitat source-registry guidance and representative placeholder YAMLs;
- Habitat and promotion policy boundaries;
- Habitat and promotion workflows;
- shared A-G validator;
- Habitat proof/published inventories;
- release-review guidance;
- CODEOWNERS; and
- bounded searches for Habitat review, promotion-decision, and manifest instances.

### Google Drive lineage

`kfm_habitat_architecture_pdf_only_blueprint_2026-04-21.pdf` was used as planning lineage for lifecycle, source-role separation, Habitat/Fauna/Flora ownership, sensitive-join fail-closed posture, evidence/receipt/review/recovery requirements, and fixture-first sequencing.

That PDF explicitly reported no mounted repository during its own authoring. It does not prove current paths, code, source activation, policy, workflows, tests, releases, or runtime behavior. Current repository evidence wins.

### Authoring limits

This update did not execute repo-native tests in a mounted checkout, access live/restricted Habitat data, authenticate stewards, evaluate Rego, resolve live evidence, verify production signatures, apply transitions, deploy, inspect public service, or run rollback.

Report static documentation validation and hosted checks separately from operational Habitat readiness.

[Back to top](#top)

---

<a id="change-history-and-no-loss-map"></a>

## Change history and no-loss map

| Version | Date | Change | Public/lifecycle effect |
|---|---|---|---|
| `v1` | 2026-05-12 | Proposal-era lifecycle and A-G runbook without mounted-repository evidence. | None |
| `v2.0.0` | 2026-08-25 | Same-path repository-grounded rewrite; narrows to final readiness, records current holds, aligns narrow A-G terms to implementation while preserving ADR status, and adds Habitat-specific gates/handoff/recovery. | None |

| v1 concern | v2.0.0 disposition |
|---|---|
| Lifecycle invariant | Preserved; no claim this runbook operates every transition. |
| Promotion as state transition | Preserved as leading invariant. |
| Habitat object families | Preserved as scope; acceptance remains contract/schema dependent. |
| A-G gates | Mapped to bounded implemented final-readiness profile; lifecycle-wide names not asserted as accepted. |
| Sensitivity overlays | Expanded to output-level, join-induced, carrier-wide controls. |
| Finite outcomes | Replaced speculative behavior with validator results and non-publishing operator dispositions. |
| Failure/reason handling | Converted to mandatory stops and stable holds. |
| Correction/rollback | Required before handoff; separate authority retained. |
| Tests/CI | Guessed commands replaced by current workflow commands and explicit holds. |
| Owners | Placeholders replaced by verified routing plus functional `NEEDS VERIFICATION`. |
| Repo fit | Resolved as same-path `PLACE`. |

[Back to top](#top)

---

<a id="document-change-rollback"></a>

## Document change rollback

This file is documentation only.

Before merge, close the draft pull request and remove only the task-owned branch after dependency checks.

After merge, revert the documentation commit through a reviewed pull request. The pre-v2 blob is:

```text
d67eeba7f839d07a7f142922f8fcfedee22f7323
```

Do not rewrite history or modify candidate, source, policy, proof, lifecycle, release, deployment, or public state as part of documentation rollback.

[Back to top](#top)

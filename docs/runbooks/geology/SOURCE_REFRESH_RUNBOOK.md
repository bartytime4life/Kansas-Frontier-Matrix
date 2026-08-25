<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook/geology/source-refresh
title: Geology Source Refresh Runbook
type: standard
subtype: operational-runbook
version: v2.0.0
prior_version: v1
status: draft; repository-grounded; documentation-only; no-network-first; live-refresh-hold; non-publisher
owner: "@bartytime4life — repository review route; operational steward roles NEEDS VERIFICATION"
created: 2026-05-12
updated: 2026-08-25
policy_label: repository-facing; restricted-by-default; non-release
current_path: docs/runbooks/geology/SOURCE_REFRESH_RUNBOOK.md
owning_root: docs/
path_posture: PLACE
truth_posture: cite-or-abstain
truth_labels: [CONFIRMED, PROPOSED, UNKNOWN, NEEDS_VERIFICATION, CONFLICTED, HOLD]
authority_class: explanatory operational procedure
authority_rank: subordinate to accepted doctrine and ADRs, source records, schemas, validators, policy, evidence, review, lifecycle, release, correction, and rollback records
prepared_under_prompt: KFM Repository Build-Out & Markdown Modernization Implementation Agent v6.0.0
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: 35d1c6c5b1adb4130ce6c24c37da40b1e7bf9769
  target_prior_blob: e0a6d4e39f01bc957fe4bc66b6b918a376503b18
  source_authority_register_blob: 32729857bc8eb5001acb37b8ee8e60bcb6e0dc50
  m118_descriptor_blob: 4f60685cbf397ad31415546fd32b07824654f7e9
  geology_ingest_spec_blob: 955422c3efe261d8f3bd0867962aaf2724ebc88e
  geology_ingest_placeholder_blob: f3924147d9c1ae38d6ba2a6aead360e1cea481b4
inspection_boundary: >-
  Current-session GitHub reads of the target, Directory Rules and ADR-0029,
  source authority projection, Geology source registries, descriptors, validators,
  connectors, pipeline surfaces, watcher specifications, sibling runbooks, and open PRs.
  Google Drive and attached Geology architecture material were read-only planning lineage.
release_effect: none
deployment_effect: none
publication_effect: none
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Geology Source Refresh Runbook

> **Purpose:** prepare, compare, validate, and hand off a possible Geology or Natural Resources source update without treating source contact, changed bytes, a receipt, green checks, a rendered map, or generated language as source admission, geologic truth, promotion, release, or publication.

> [!CAUTION]
> **Live Geology refresh execution is `HOLD` at the pinned repository state.** The source-authority projection is empty and reports `implementation_status: ABSENT`; the canonical M-118 descriptor is proposed, rights-unknown, connector-disabled, review-pending, and not released; KGS connector placement remains unresolved; `pipeline_specs/geology/ingest.yaml` has `stages: []`; `pipelines/domains/geology/ingest.py` is a placeholder; and no Geology watcher specification was found.

> [!WARNING]
> Exact borehole, well-log, core, sample, private-well, resource-occurrence, infrastructure-adjacent, cultural, or otherwise harmful-precision locations fail closed. Public availability does not establish redistribution rights, safe joins, or public-release fitness.

**Navigation:** [Boundary](#1-boundary) · [Current state](#2-authority-placement-and-current-state) · [Preflight](#3-authority-freeze) · [Source meaning](#4-source-registry-and-role) · [Procedure](#5-governed-procedure) · [Validation](#6-no-network-validation) · [Outcomes](#7-outcomes-and-materiality) · [Security](#8-rights-sensitivity-and-security) · [Handoff](#9-review-handoff) · [Failure and rollback](#10-failure-correction-and-rollback) · [Graduation](#11-live-graduation-gates) · [References](#12-related-surfaces)

---

## 1. Boundary

Use this runbook for a possible new version, correction, replacement, retirement, or changed source head. The operator must:

1. pin repository, source, descriptor, authority decision, connector, pipeline, prior source head, allowed effects, and rollback target;
2. run no-network contract checks before any separately authorized network contact;
3. preserve source role, authority scope, rights, sensitivity, scale, CRS/datum, time, uncertainty, attribution, and limitations;
4. route unresolved material to `HOLD` or governed QUARANTINE rather than guess;
5. write only through an accepted lifecycle owner and only to the authorized stage; and
6. prepare a bounded packet for [PROMOTION_RUNBOOK.md](./PROMOTION_RUNBOOK.md), then stop.

This runbook does **not** admit, activate, credential, schedule, approve, promote, release, deploy, or publish a source. It does not invent a live watcher or connector command, write directly to PROCESSED/CATALOG/TRIPLET/PUBLISHED, or certify reserve quantity, economic viability, title, permit status, regulatory compliance, production truth, life-safety suitability, or engineering fitness.

The lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed state transition, not a file move, PR, merge, checksum, receipt, proof, catalog row, rendered layer, or GitHub release.

[Back to top](#top)

---

## 2. Authority, placement, and current state

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts [Directory Rules v2](../../doctrine/directory-rules.md). This is a same-path `PLACE` under the human-readable runbook responsibility root:

```text
docs/runbooks/geology/SOURCE_REFRESH_RUNBOOK.md
```

No parallel registry, schema, connector, policy, lifecycle, receipt, proof, catalog, release, or publication authority is created.

| Surface | CONFIRMED state at the pinned commit | Safe conclusion |
|---|---|---|
| `control_plane/source_authority_register.yaml` | `status: PROPOSED`; `projection_only`; `implementation_status: ABSENT`; `completeness: empty`; `entries: []` | It admits or activates no Geology source |
| Canonical source lane | `data/registry/sources/geology/` has one M-118 descriptor | One proposed candidate exists; broad coverage does not |
| M-118 descriptor | rights `unknown`; public release false; connector `disabled`; review `needs_review`; release `not_released` | No-network validation target only |
| Compatibility lane | `data/registry/geology/sources/` is navigation/compatibility | Independent descriptor writes there are denied |
| KGS connector surfaces | Geology, KSGS, and KGS LAS scaffolds exist; final path and runnable behavior unresolved | No verified live command |
| Geology ingest spec | `stages: []` | No executable stage sequence |
| Geology ingest code | one-line placeholder | No live ingest implementation |
| Watcher specs | no Geology watcher found | Do not claim one exists |
| Shared validators | SourceDescriptor, SourceActivationDecision, SourceEventEnvelope, RunReceipt, and IngestReceipt validators exist | Bounded no-network checks are available |

**CONFIRMED:** no-network candidate and fixture validation is available. **HOLD / NEEDS VERIFICATION:** live access, credentials, scheduling, lifecycle persistence, broad Geology semantic processing, policy evaluation, evidence/catalog closure, promotion, release, deployment, and publication.

[Back to top](#top)

---

## 3. Authority freeze

Before mutation, record:

```yaml
repository_ref: <immutable SHA>
source_id: <canonical source_id>
source_descriptor_ref: <path plus blob/digest>
source_activation_decision_ref: <resolved record or HOLD>
source_head_prior_ref: <prior head or HOLD>
connector_ref: <accepted implementation version or HOLD>
pipeline_spec_ref: <non-placeholder spec or HOLD>
pipeline_implementation_ref: <tested implementation or HOLD>
rights_review_ref: <review or HOLD>
sensitivity_review_ref: <review or HOLD>
allowed_network_hosts: []
allowed_writes: []
forbidden_effects:
  - source_admission
  - source_activation
  - direct_processed_write
  - direct_catalog_write
  - direct_published_write
  - promotion
  - release
  - deployment
  - publication
rollback_target: <candidate cleanup or governed rollback reference>
```

Required role classes are source steward, connector operator, Geology steward, rights reviewer, sensitivity reviewer, validation/evidence steward, policy reviewer, release authority, correction/rollback authority, and independent reviewer where consequence requires separation. CODEOWNERS routing does not automatically establish those authorities.

At the pinned state, live execution does not pass this freeze. Return `HOLD`.

[Back to top](#top)

---

## 4. Source registry and role

The canonical machine write lane is:

```text
data/registry/sources/geology/
```

The domain-first sibling is compatibility/navigation only:

```text
data/registry/geology/sources/
```

Do not maintain an independent `SourceDescriptor` in the compatibility lane.

Use exact `source_role` values from the current schema. Preserve these anti-collapse rules:

- observation is not interpreted map unit;
- surface geology is not subsurface inference;
- well location is not log or lithology observation;
- occurrence is not deposit, estimate, reserve, production, or viability;
- physical geology is not permit, lease, operator, title, or compliance state;
- model, inversion, interpolation, or classification is not measurement;
- aggregate is not an individual place;
- historical context is not current truth;
- a derived public product is a downstream carrier, not sovereign evidence;
- a watcher signal may propose work but cannot publish.

Preserve source valid time, observation time, publication time, retrieval time, and KFM transaction time separately. Unresolved source role or claim class returns `HOLD` or proposed QUARANTINE; never choose the most permissive interpretation.

[Back to top](#top)

---

## 5. Governed procedure

### Step 0 — pin coordination

Record current `main`, create a task branch, search open PRs/branches for the exact target and source family, stop on unresolved overlap, and record prior blobs for every possible write.

### Step 1 — resolve the descriptor

Locate the canonical descriptor, reject compatibility-only records as authority, run the current validator, and confirm identity, version, type, role, authority limits, rights, sensitivity, cadence, access, citation, source head, public-release posture, review, release, lifecycle, and `spec_hash` where required. Missing or invalid descriptor means `HOLD`; repair/admission is separate work.

### Step 2 — resolve authority

Treat the central register only as its declared projection. Resolve and validate the owning `SourceActivationDecision` or accepted admission record. It must be current, source-bound, reviewer-bound, rights/sensitivity-aware, and route-limited. The pinned projection is empty, so live work stops here today.

### Step 3 — resolve rights and sensitivity

Recheck official terms before live access or redistribution. Record attribution, redistribution, derivative, commercial-use, caching, retention, and access constraints. Classify source-wide and geometry/field-level sensitivity and harmful joins. Unknown, expired, denied, or conflicted rights keep public release false and route to `HOLD` or QUARANTINE.

### Step 4 — resolve connector and pipeline

Select exactly one accepted source-first connector. Pin code/version, lockfile, allowlisted hosts, command, authentication mechanism, retry behavior, output contract, and tests. Require an explicit QUARANTINE route, no direct downstream write, and non-placeholder pipeline spec/code. The inspected KGS and Geology surfaces do not meet this gate.

### Step 5 — prove no-network behavior

Run [Section 6](#6-no-network-validation). Any failure stops the live profile. A pass proves only the implemented validator scope.

### Step 6 — future bounded source-head probe

Only after authorization: use the pinned connector and allowed host; send approved conditional headers and credentials; bound timeouts, retries, redirects, response size, decompression, archive depth, and content type; record status, validators, source time, retrieval time, and safe diagnostics; then classify the result under [Section 7](#7-outcomes-and-materiality).

### Step 7 — future immutable capture

Through the owning implementation only, write source-native bytes or an accepted immutable reference to RAW or QUARANTINE; compute digest and byte count; record media type, source/retrieval time, connector version, and source head; emit an `IngestReceipt` candidate; validate receipt-to-artifact and receipt-to-source-head bindings; never overwrite prior immutable captures.

### Step 8 — future WORK normalization

Parse in a bounded environment; preserve source IDs and lineage; normalize CRS/datum, units, time, scale, geometry, methods, uncertainty, and role without erasing source semantics; route invalid, restricted, ambiguous, over-precise, or rights-conflicted records to QUARANTINE; run schema, integrity, Geology, spatial, temporal, sensitivity, rights, evidence, and policy checks. Produce PROCESSED candidates only through the owning gate.

### Step 9 — compare and hand off

Record transport, metadata, semantic, geometry, rights/sensitivity, role, correction, supersession, retirement, and no-change dimensions separately. A byte change is not automatically geologic materiality. Prepare the review packet and stop before promotion.

[Back to top](#top)

---

## 6. No-network validation

Run from repository root in an isolated environment with declared test dependencies installed:

```bash
python tools/validators/validate_source_descriptor.py --fixtures
python tools/validators/validate_source_activation_decision.py --fixtures
python tools/validators/validate_source_event_envelope.py --fixtures
python tools/validators/validate_run_receipt.py --fixtures
python tools/validators/validate_ingest_receipt.py --fixtures

python tools/validators/validate_source_descriptor.py \
  data/registry/sources/geology/kgs-m118-surficial-geology.source.json
```

Explicit candidate examples:

```bash
python tools/validators/validate_source_activation_decision.py path/to/decision.json
python tools/validators/validate_source_event_envelope.py path/to/envelope.json
python tools/validators/validate_run_receipt.py path/to/run_receipt.json
python tools/validators/validate_ingest_receipt.py path/to/ingest_receipt.json \
  --source-descriptor path/to/source_descriptor.json \
  --source-head-key source_head \
  --artifact CAPTURE_SHA256=path/to/local/captured-artifact \
  --require-success
```

Use only digest keys defined by the receipt. Never put secrets or protected values in arguments. A pass does not resolve rights, approve a descriptor, activate a connector, authenticate a publisher, admit bytes, or permit release. See [NO_NETWORK_TEST_RUNBOOK.md](./NO_NETWORK_TEST_RUNBOOK.md).

[Back to top](#top)

---

## 7. Outcomes and materiality

| Surface | Finite values | Meaning |
|---|---|---|
| Local validators | `PASS`, `FAIL`/`DENY`, `ERROR` | Bounded validator result only |
| `SourceEventEnvelope` | `PROPOSE_SOURCE_ADMISSION`, `PROPOSE_QUARANTINE`, `NO_ACTION` | Candidate routing; no activation or publication |
| Smart Sync decision | `materialize`, `no_op` | Process result, not semantic promotion |
| Smart Sync reason | `content_changed`, `not_modified`, `validator_drift` | Reason for output or no output |
| Narrow KGS production packet | `NO_CHANGE`, `REVIEW`, `HOLD`, `ERROR` | Production-record assessment only |
| Operator work state | `HOLD` | Fail-closed stop |

`materialize` means candidate output is expected. It does not mean geologically material, admissible, policy-safe, evidence-closed, approved, released, or public.

Assess upstream edition/coverage; digests and counts; map scale, generalization, CRS/datum, geometry and topology; stratigraphic names/ages/lithology/correlation; well/core/sample identity and depth reference; methods, units, qualifiers, uncertainty and processing level; occurrence/deposit/estimate/reserve/production/regulatory class; rights, attribution, sensitivity, embargo and release conditions; source role, authority rank, allowed/prohibited claims, correction, supersession, withdrawal, and retirement.

The narrow KGS production material-change validator is not a generic Geology validator and must not be reused for M-118, bedrock maps, boreholes, logs, samples, mineral occurrences, or AEM inversions.

[Back to top](#top)

---

## 8. Rights, sensitivity, and security

- Treat `unknown`, `noassertion`, `permission_required`, expired, denied, or conflicted rights as release blockers.
- Separate access permission from redistribution and public-release permission.
- Public downloadability is not blanket permission for repackaging, bulk redistribution, exact-location joins, commercial use, or model training.
- Default exact wells, boreholes, logs, cores, samples, geophysical lines, inversion cells, sensitive occurrences, infrastructure-adjacent or cultural locations, and re-identifiable small cells to restricted review.
- Transform sensitive geometry before rendering. Style-only hiding, client filters, clustering, opacity, and zoom limits are not security controls.
- Allowlist schemes/hosts; deny arbitrary redirects and SSRF-capable destinations; bound timeouts, retries, response size, decompression, archive depth, file count, path traversal, XML expansion, JSON depth, and geometry complexity.
- Preserve source-native bytes; never execute embedded scripts, macros, notebooks, binaries, or source code.
- Keep credentials in approved secret storage, never descriptors, receipts, logs, PRs, or command history.
- Logs may contain public-safe source ID/endpoint label, run ID, code ref, validator version, outcome, reason, elapsed time, byte count, and digest. They must not contain secrets, signed URLs, raw restricted values, exact sensitive coordinates, private identifiers, or hidden reasoning.

[Back to top](#top)

---

## 9. Review handoff

Keep object families distinct:

| Object | Records | Does not prove |
|---|---|---|
| `SourceDescriptor` | how a source may be treated | activation or source truth |
| `SourceActivationDecision` | governed intake route | successful execution or valid data |
| `SourceEventEnvelope` | bounded signal and proposed disposition | admission, RAW write, approval, publication |
| `RunReceipt` / `IngestReceipt` | what ran and local integrity/process memory | evidence adequacy, policy approval, promotion |
| `EvidenceRef` / `EvidenceBundle` | claim support, scope, limitations | release decision by itself |
| validation report | implemented checks and findings | rights or public fitness outside scope |
| catalog/triplet projection | discovery or derived relation | sovereign truth or release |
| promotion/release record | governed transition and released set | permanent error-free status |
| correction/rollback record | correction, withdrawal, supersession, reversal | silent deletion authority |

The packet must include pinned repository/descriptor/decision/connector/pipeline/schema/validator/policy refs; prior/current source heads and times; artifact paths, types, counts, and digests; source role, authority scope, scale, CRS/datum, uncertainty, and limitations; rights/sensitivity/transform posture; exact validation commands, results, and limitations; receipts and local bindings; evidence/catalog/policy/review status; no-change/material-change/quarantine/correction classification; intended next transition; blockers; rollback target; and explicit non-effects.

Missing authority must be labeled `HOLD`, not approval.

[Back to top](#top)

---

## 10. Failure, correction, and rollback

| Failure | Required response |
|---|---|
| descriptor missing/invalid | `HOLD`; repair/admit separately |
| authority unresolved | `HOLD`; no live contact |
| rights/sensitivity unresolved | QUARANTINE proposal or `HOLD` |
| connector absent, placeholder, or path-conflicted | `HOLD`; do not invent a command |
| pipeline has no stages or placeholder code | stop before lifecycle write |
| timeout/rate limit/outage | bounded backoff; preserve prior state; no permissive fallback |
| redirect/host/content-type violation | deny or quarantine |
| digest mismatch/truncated capture | `ERROR`; do not normalize |
| schema/semantic failure | QUARANTINE and preserve safe findings |
| role/materiality ambiguity | `HOLD`; qualified review |
| evidence/policy/review/release/rollback gap | stop before promotion |

Retry only idempotent authorized retrieval. Respect quotas and `Retry-After`; never rotate identities, proxies, credentials, or hosts to evade limits. A `no_op` must not create fake changed output, advance lifecycle/release state, overwrite prior receipts, or hide validator drift.

Documentation rollback is revert the single commit, close the draft PR, or delete the unmerged branch. Candidate rollback preserves required audit metadata and prior immutable captures, discards disposable outputs or quarantines governed candidates, records rejection/supersession/hold, and reruns no-network checks. Released-state correction uses [ROLLBACK_RUNBOOK.md](./ROLLBACK_RUNBOOK.md); never silently delete or overwrite released material.

[Back to top](#top)

---

## 11. Live graduation gates

Live source-head probe, capture, or normalization remains `HOLD` until all are true:

- [ ] canonical rich descriptor and current accepted activation/admission record resolve;
- [ ] source, Geology, connector, rights, sensitivity, evidence, policy, operations, release, correction, rollback, and independent-review roles are named;
- [ ] current terms, attribution, redistribution, retention, derivative, and access rules are verified;
- [ ] harmful precision and unsafe joins are reviewed with public-safe transform tests;
- [ ] exactly one source-first KGS connector path is accepted and substantive, pinned, locked, allowlisted, secret-safe, and tested;
- [ ] the Geology ingest spec declares real stages and code is non-placeholder with positive, negative, no-network, retry, idempotency, sensitivity, and quarantine tests;
- [ ] any watcher is explicitly admitted and remains a non-publisher;
- [ ] source-specific and Geology semantic validators cover the source family;
- [ ] receipts bind to local artifacts; `EvidenceRef` resolves to adequate `EvidenceBundle`; policy and qualified review close;
- [ ] promotion, release, correction, withdrawal, and rollback remain separate and reviewable; and
- [ ] governed APIs and released public-safe carriers are the only normal public path.

Open items remain: source-authority owner/entries `UNKNOWN`; schema singular/plural authority `CONFLICTED`; final KGS connector path `CONFLICTED / HOLD`; other source descriptors and current terms `NEEDS VERIFICATION`; Geology watcher and executable ingest sequence `ABSENT`; broad Geology materiality validation `ABSENT / NEEDS VERIFICATION`; production policy, evidence/catalog closure, signer custody, release operation, deployment, and public runtime `UNKNOWN / NEEDS VERIFICATION`.

[Back to top](#top)

---

## 12. Related surfaces

- [Directory Rules v2](../../doctrine/directory-rules.md)
- [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [Geology Source Registry](../../domains/geology/SOURCE_REGISTRY.md)
- [Geology Sources](../../domains/geology/SOURCES.md)
- [Geology Source Role Matrix](../../domains/geology/SOURCE_ROLE_MATRIX.md)
- [Geology Data Lifecycle](../../domains/geology/DATA_LIFECYCLE.md)
- [Geology Sensitivity](../../domains/geology/SENSITIVITY.md)
- [SourceDescriptor Standard](../../sources/SOURCE_DESCRIPTOR_STANDARD.md)
- [Source authority projection](../../../control_plane/source_authority_register.yaml)
- [Canonical Geology registry](../../../data/registry/sources/geology/README.md)
- [M-118 descriptor](../../../data/registry/sources/geology/kgs-m118-surficial-geology.source.json)
- [Compatibility registry](../../../data/registry/geology/sources/README.md)
- [KSGS connector scaffold](../../../connectors/ksgs/README.md)
- [Geology ingest spec](../../../pipeline_specs/geology/ingest.yaml)
- [Watcher specs](../../../pipeline_specs/watchers/README.md)
- [Geology ingest placeholder](../../../pipelines/domains/geology/ingest.py)
- [No-network testing](./NO_NETWORK_TEST_RUNBOOK.md)
- [Bedrock review](./BEDROCK_REVIEW.md)
- [Promotion](./PROMOTION_RUNBOOK.md)
- [Rollback](./ROLLBACK_RUNBOOK.md)

---

## Change history

| Version | Date | Change |
|---|---|---|
| `v1` | 2026-05-12 | Proposal-era source-refresh plan |
| `v2.0.0` | 2026-08-25 | Grounded the runbook in current repository evidence, canonical registry placement, no-network validators, explicit live-execution holds, Geology anti-collapse rules, bounded outcomes, review handoff, and reversible rollback |

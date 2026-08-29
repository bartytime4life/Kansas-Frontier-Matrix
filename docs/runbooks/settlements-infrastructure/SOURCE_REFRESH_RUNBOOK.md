<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook/settlements-infrastructure/source-refresh
title: Settlements and Infrastructure — Source Refresh Readiness Runbook
type: runbook
version: v1.0.0
prior_version: v0.1
prior_state: proposal-era live-refresh procedure with unverified sources, writers, paths, commands, receipts, promotion behavior, and public-state effects
status: draft; repository-grounded; LIVE_SOURCE_REFRESH_HELD; BOUNDED_SOURCE_DESCRIPTOR_VALIDATION; BOUNDED_EVIDENCEBUNDLE_CONVERGENCE; NON_RELEASE; NON_DEPLOYMENT; NON_PUBLICATION
owners:
  - "@bartytime4life — verified GitHub review route"
  - "NEEDS VERIFICATION — accountable source, registry, rights, sensitivity, cultural, sovereignty, infrastructure-security, evidence, policy, operations, correction, rollback, release, and independent-review assignments"
created: 2026-05-12
updated: 2026-08-29
policy_label: repository-facing; critical-infrastructure-sensitive; cultural-and-sovereignty-sensitive; source-admission-held; fail-closed
current_path: docs/runbooks/settlements-infrastructure/SOURCE_REFRESH_RUNBOOK.md
owning_root: docs/
responsibility: repository-only source-refresh readiness review and accountable handoff for the Settlements/Infrastructure lane
truth_posture: cite-or-abstain
authority_class: explanatory operational documentation
authority_rank: subordinate to accepted doctrine and ADRs, source identities and activation records, contracts, schemas, policy, evidence, review, lifecycle, proof, release, correction, rollback, and competent official authorities
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: bd4eb1fd42e947a21f2d7679dd318f79973c0067
  target_before_update_blob: c8895a5e90d2d8bd2628c6ca72dd9f216c3a724e
  local_runbook_boundary_blob: 3ff33de15249486f520df1fafd934451b268012b
  canonical_source_registry_readme_blob: 913d694acbe8fbd1660790c9b4c8c614a9cdd627
  domain_first_source_registry_readme_blob: 9defa909410d4fba6d16ecf7f8ae6ea66da16d6e
  source_authority_register_blob: 32729857bc8eb5001acb37b8ee8e60bcb6e0dc50
  domain_connector_readme_blob: a6fc165cd2c1a2ed3baef5df06b02ea754f7a68f
  census_fetch_placeholder_blob: 1d9bbb1097c64a44b53650b38ed3c6262cb3c4a7
  census_admission_placeholder_blob: 04d57cd624f226fe1517cda4a7854c60570d91de
  census_descriptor_placeholder_blob: f3c1bd326d29065e41761a98b3535f8112604dcf
  source_descriptor_schema_blob: 582e70b834278c3c6ca9a8b31efbe0989c96f0bc
  source_descriptor_alias_blob: 42da54b28a527850cce88ad89f68921c101fc56b
  source_descriptor_validator_blob: a0420731a1b80ce6d156f8e4cfd928a6b13699f4
  source_descriptor_workflow_blob: 6d3f900efcddc17d24a528a92190544fc350b63b
  domain_workflow_blob: a47d89c40efd58ac31bc44dbc56bdfb1ccc3a325
  convergence_workflow_blob: 584ac26dcaf5791b1a560cb71bd059e889f55791
  no_network_runbook_blob: 90133c88ddf2d053a9ca1021e1951e2b241a4ebd
  raw_boundary_blob: 560113c00e257725c0a440cb489510af44c13b12
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  canonical_registry_placeholder_records: 1
  parallel_domain_first_descriptor_templates: 5
  source_authority_register_entries: 0
  verified_live_refresh_profiles: 0
related:
  - ./README.md
  - ./NO_NETWORK_TEST_RUNBOOK.md
  - ./PROMOTION_RUNBOOK.md
  - ./ROLLBACK_RUNBOOK.md
  - ../../domains/settlements-infrastructure/README.md
  - ../../domains/settlements-infrastructure/SOURCE_REGISTRY.md
  - ../../domains/settlements-infrastructure/CANONICAL_PATHS.md
  - ../../domains/settlements-infrastructure/SENSITIVITY.md
  - ../../sources/ADMISSION_PROCESS.md
  - ../../sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../doctrine/directory-rules.md
  - ../../doctrine/lifecycle-law.md
  - ../../doctrine/trust-membrane.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../.github/CODEOWNERS
  - ../../../.github/workflows/source-descriptor-validate.yml
  - ../../../.github/workflows/domain-settlements-infrastructure.yml
  - ../../../.github/workflows/settlements-infrastructure-evidence-bundle-convergence.yml
  - ../../../control_plane/source_authority_register.yaml
  - ../../../data/registry/sources/README.md
  - ../../../data/registry/sources/settlements-infrastructure/README.md
  - ../../../data/registry/settlements-infrastructure/sources/README.md
  - ../../../data/raw/README.md
  - ../../../connectors/settlements-infrastructure/README.md
  - ../../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../../schemas/contracts/v1/sources/source_descriptor.schema.json
  - ../../../fixtures/contracts/v1/source/source_descriptor/
  - ../../../tools/validators/validate_source_descriptor.py
  - ../../../tools/validators/sources/validate_source_descriptor.py
  - ../../../tests/validators/test_validate_source_descriptor_entrypoints.py
  - ../../../tests/schemas/test_common_contracts.py
  - ../../../schemas/contracts/v1/domains/settlements-infrastructure/evidence_bundle.schema.json
  - ../../../tools/validators/validate_settlements_infrastructure_evidence_bundle_projection.py
  - ../../../tests/validators/domains/settlements-infrastructure/test_evidence_bundle_schema_convergence.py
notes:
  - "This revision replaces unverified live-refresh instructions with a current repository readiness procedure."
  - "The available SourceDescriptor and EvidenceBundle profiles are synthetic and fixture-bound; they do not admit, activate, retrieve, transform, promote, release, deploy, or publish a source."
  - "Connected Drive material is planning lineage and Notion is coordination; GitHub controls current-behavior claims."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Settlements and Infrastructure — Source Refresh Readiness Runbook

> [!CAUTION]
> **Current result: `HOLD`.** Live Settlements/Infrastructure source refresh is
> not established by current repository evidence. Do not execute the retired
> fetch, watcher, source-write, receipt, signing, cache-invalidation, or
> promotion examples from the prior version of this file.

This runbook supports **repository-only readiness review** and bounded synthetic
validation. It does not contact Census, TIGER/Line, GNIS, KDOT, FEMA,
municipalities, infrastructure operators, archives, Tribal or Indigenous
stewards, OpenStreetMap, or any other source.

It is not municipal-law, census, address, ownership, utility, infrastructure-
condition, service-availability, emergency, safety, security, planning,
inspection, access, or regulatory authority.

**Navigate:** [current disposition](#current-repository-disposition) ·
[procedure](#repository-only-procedure) ·
[validation](#bounded-validation-profiles) ·
[live-refresh gates](#requirements-before-a-future-live-refresh) ·
[stop conditions](#mandatory-stop-conditions) ·
[handoff](#review-handoff) ·
[rollback](#documentation-correction-and-rollback)

## Purpose and terminal boundary

Use this runbook to determine whether the repository contains enough verified
source identity, rights, sensitivity, connector, lifecycle, evidence, policy,
review, correction, and rollback support to consider a future refresh.

The highest result this procedure can emit is:

```text
READY_FOR_ACCOUNTABLE_SOURCE_REFRESH_REVIEW
```

That result is a review handoff only. It is not source admission, activation,
retrieval, lifecycle mutation, evidence closure, approval, release, deployment,
promotion, or publication.

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
adopts the [Directory Rules](../../doctrine/directory-rules.md). The current path
is therefore retained: `docs/runbooks/` owns human operational procedures.
Source records, connectors, lifecycle objects, policy, proofs, and release
objects remain in their own responsibility roots.

## Current repository disposition

The following findings are pinned to the metadata snapshot. Re-inspect them at a
later revision before relying on this table.

| Surface | Verified repository evidence | Bounded conclusion |
|---|---|---|
| Canonical source-registry family | Directory Rules identify `data/registry/sources/` as canonical. Its Settlements/Infrastructure lane contains documentation, a Census/TIGER child, and one placeholder YAML. | No admitted source inventory established |
| Parallel domain-first view | `data/registry/settlements-infrastructure/sources/` contains five `PROPOSED — greenfield template` YAML files with unresolved fields. | Not an independent writer or activation surface |
| Source-authority projection | `control_plane/source_authority_register.yaml` is projection-only, implementation-absent, empty, and has `entries: []`. | No machine authority entry for a live refresh |
| Domain connector | `connectors/settlements-infrastructure/` contains documentation and `.gitkeep`. | No executable domain connector |
| Census connector | `fetch.py` and `admit.py` are comments-only placeholders; the descriptor retains unresolved role and rights fields. | No live Census retrieval or admission path |
| SourceDescriptor validation | Rich proposed schema, plural compatibility alias, two validator entrypoints, synthetic fixtures, focused tests, and a workflow exist. | Fixture shape and convergence only |
| EvidenceBundle projection | A no-network-compatible projection profile and workflow exist. | Schema delegation and fixture behavior only |
| RAW boundary | Source-first identity is required, but exact physical placement, writer interface, deduplication, migration, and rollback remain held. | Do not invent a RAW path |
| Domain policy, proof, and release | Policy remains evaluator-unbound; domain workflow records semantic-validation, proof-production, and release-dry-run holds. | No candidate may advance |

### Finite current result

```yaml
work_state: HOLD
reason_codes:
  - SI_SOURCE_INVENTORY_UNADMITTED
  - SI_SOURCE_AUTHORITY_REGISTER_EMPTY
  - SI_REGISTRY_WRITER_UNVERIFIED
  - SI_CONNECTOR_UNIMPLEMENTED
  - SI_RAW_PLACEMENT_UNRESOLVED
  - SI_POLICY_RUNTIME_UNVERIFIED
  - SI_PROOF_AND_RELEASE_PATHS_HELD
terminal_boundary: ACCOUNTABLE_REVIEW_HANDOFF_ONLY
network_access: NOT_PERFORMED
source_activation: NOT_PERFORMED
lifecycle_write: NOT_PERFORMED
release: NOT_PERFORMED
deployment: NOT_PERFORMED
publication: NOT_PERFORMED
```

## Source-role and safety rules

Retrieval, normalization, joining, cataloging, graph projection, mapping, or
generated language cannot upgrade a source's role.

| Material | May support | Must not be substituted for |
|---|---|---|
| Census/TIGER and census-place geography | Vintage-bound statistical geography and identifiers | Legal municipal status, ownership, cadastral truth, address validity, or current service status |
| GNIS, gazetteers, post-office records, and map labels | Name, location, or historical context within the source scope | Incorporation, continued existence, jurisdiction, or exact historic boundary |
| Municipal legal records | Bounded legal or administrative evidence for the issuing jurisdiction and effective period | Universal or current status without current review |
| State/local GIS and infrastructure inventories | Publisher-scoped administrative, observed, or contextual information | Current condition, capacity, availability, safety, ownership, dependency, or access |
| Historic maps and records | Dated evidence with scale, method, uncertainty, rights, and limitations | Surveyed exact geometry, present access, or unrestricted cultural publication |
| Community or volunteered data | Candidate or contextual evidence under license and role limits | Official designation, legal status, ownership, condition, or safety authority |
| Modeled, mapped, inferred, or AI-generated output | Derived representation with method, inputs, uncertainty, and evidence references | Source observation or sovereign truth |

Keep source, observed, valid/effective, retrieval, record, publication,
correction, and supersession time distinct where material.

Sensitive infrastructure, exact facility geometry, dependencies, condition
observations, operator-sensitive details, private-property or living-person
joins, culturally sensitive places, archaeology, and sovereignty-bearing
information fail closed until rights, policy, public-safe transformation, and
accountable review are established.

Cross-domain joins do not transfer authority. Roads/Rail/Trade owns route
semantics; Hydrology owns water evidence; Hazards owns hazard events and
warnings; People/DNA/Land owns living-person and parcel-sensitive material;
Archaeology and relevant cultural or sovereignty stewards govern protected
historic and cultural context.

## Repository-only procedure

### Step 1 — Freeze the evidence revision

Run from a clean checkout or dedicated worktree:

```bash
git remote get-url origin
git rev-parse HEAD
git status --short
```

Record the exact commit and inherited changes. Do not report a result against a
floating `main`.

### Step 2 — Inspect source authority and overlap

Review these surfaces at the exact revision:

```text
data/registry/sources/README.md
data/registry/sources/settlements-infrastructure/
data/registry/settlements-infrastructure/sources/
control_plane/source_authority_register.yaml
connectors/settlements-infrastructure/
connectors/census/src/census/
docs/sources/ADMISSION_PROCESS.md
docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
data/raw/README.md
```

Confirm:

1. which record is authoritative for each source identity;
2. whether the domain-first view is generated or independently writable;
3. whether a stable source ID, complete descriptor, and activation decision
   exist;
4. whether the connector and writer are substantive and tested;
5. whether exact RAW/QUARANTINE placement is accepted;
6. whether another branch, PR, migration, or steward owns the same source or
   topology.

A README, template, source name, URL, map layer, workflow, or passing fixture
does not establish admission or activation.

### Step 3 — Inspect placeholder posture

Use read-only repository checks:

```bash
git grep -n 'PROPOSED — greenfield template' -- \
  data/registry/settlements-infrastructure/sources/*.yaml

git grep -n 'TBD' -- \
  data/registry/settlements-infrastructure/sources/*.yaml

find data/registry/sources/settlements-infrastructure \
  -maxdepth 2 -type f -print | sort

find connectors/settlements-infrastructure \
  -maxdepth 3 -type f -print | sort

find connectors/census/src/census \
  -maxdepth 2 -type f -print | sort
```

If a real descriptor, activation record, substantive connector, writer, proof,
candidate, or published payload appears, stop using the pinned disposition and
inspect the new owning object.

### Step 4 — Run only bounded validation

Run the profiles in the next section. Record exact commands, environment,
inputs, commit, outcomes, and limitations. Do not classify unavailable checks
as passing.

### Step 5 — Reconcile the result

Use this precedence:

```text
ERROR > DENY > ABSTAIN > HOLD > READY_FOR_ACCOUNTABLE_SOURCE_REFRESH_REVIEW
```

A fixture `PASS` cannot override a source-refresh `HOLD`.

### Step 6 — Hand off; do not refresh

When every applicable prerequisite is supported, produce the minimized packet
in [Review handoff](#review-handoff) and route it to accountable reviewers.
This runbook ends there.

## Bounded validation profiles

### SourceDescriptor fixture profile

From the repository root:

```bash
python tools/validators/validate_source_descriptor.py --fixtures
python tools/validators/sources/validate_source_descriptor.py --fixtures
python -m pytest -q \
  tests/validators/test_validate_source_descriptor_entrypoints.py \
  tests/schemas/test_common_contracts.py \
  -k source_descriptor
```

The corresponding workflow is
[`.github/workflows/source-descriptor-validate.yml`](../../../.github/workflows/source-descriptor-validate.yml).

A pass supports only the tested schema, alias, entrypoint, rights-field, and
fixture expectations. It does not inventory registry records, choose a writer,
resolve naming drift, decide rights or sensitivity, admit or activate a source,
retrieve data, or authorize release.

### EvidenceBundle projection profile

Follow the complete guarded procedure in
[`NO_NETWORK_TEST_RUNBOOK.md`](./NO_NETWORK_TEST_RUNBOOK.md). The focused
repository commands are:

```bash
python -m unittest discover \
  --start-directory tests/validators/domains/settlements-infrastructure \
  --pattern 'test_evidence_bundle_schema_convergence.py' \
  --verbose

python \
  tools/validators/validate_settlements_infrastructure_evidence_bundle_projection.py \
  --fixtures
```

This profile checks the domain projection's delegation to the shared schema and
tracked synthetic fixtures. It does not construct or resolve a materialized
EvidenceBundle, evaluate domain semantics or policy, contact a source, produce
proof, or authorize release.

`KFM_NO_NETWORK=1` is not host-wide or runner-wide egress proof by itself.
Report only the exact guard and code path that ran.

## Requirements before a future live refresh

Do not add a live command to this runbook until all applicable items are
implemented, accepted, and verified at one exact revision.

### Source and authority closure

- stable source identity and one authoritative descriptor record;
- accepted SourceDescriptor vocabulary/path or explicit compatibility binding;
- source role, authority scope, rights, attribution, redistribution, access,
  sensitivity, cadence, source head, stale threshold, and permitted claim
  families;
- separately accountable activation decision;
- current endpoint or delivery identity, terms, versioning, rate limits, and
  retrieval constraints verified from the source owner;
- cultural, sovereignty, community, infrastructure-security, privacy, or legal
  review where applicable.

### Connector and lifecycle closure

- one verified registry writer and deterministic generated-view contract;
- accepted source-first RAW or QUARANTINE placement;
- substantive connector with timeouts, rate limits, retries, size limits,
  content-type checks, digesting, and safe error handling;
- deterministic capture identity, collision handling, idempotency, replay, and
  readback tests;
- accepted receipt contracts, schemas, validators, and storage responsibility;
- explicit no-change behavior that manufactures no new authority or state;
- no credential, private endpoint, restricted payload, or harmful precision in
  Git, public logs, PRs, or unapproved storage.

### Evidence, policy, review, and recovery closure

- domain semantic validation with positive, negative, stale, restricted, and
  cross-domain fixtures;
- EvidenceRef-to-EvidenceBundle closure for consequential claims;
- accepted candidate-bound policy result with finite outcome, reasons, and
  obligations;
- authenticated accountable review and separation of duties appropriate to
  risk;
- proof, catalog, correction, withdrawal, invalidation, rollback, candidate,
  and manifest support;
- governed public interfaces or immutable released public-safe carriers only.

Live source contact, admission, activation, lifecycle writes, release,
deployment, promotion, and publication remain separate governed operations.

## Mandatory stop conditions

| Condition | Result |
|---|---|
| Descriptor is a template, incomplete, or lacks activation | `HOLD` |
| Canonical writer, generated view, or path migration is unresolved | `HOLD` |
| Connector is documentation, `.gitkeep`, or comments-only code | `HOLD` |
| Rights, terms, role, authority, cadence, source head, or sensitivity is unresolved | `HOLD` or `DENY` |
| Exact RAW/QUARANTINE placement is unresolved | `HOLD` |
| Consequential EvidenceRef does not resolve | `ABSTAIN` or `HOLD` |
| Sensitive precision or protected information may be exposed | `DENY` or `ESCALATE` |
| A legal, operational, service, condition, ownership, access, safety, emergency, or regulatory answer lacks competent current authority | `ABSTAIN` |
| A test, workflow, digest, receipt, map, graph, or AI summary is offered as proof of admission or release | `DENY` the implied authority |
| Tooling or environment failure prevents a trustworthy result | `ERROR` |

Unknown conditions never imply approval.

## Review handoff

Use a public-safe, reference-only record. This example is documentation, not an
accepted schema or activation decision.

```yaml
settlements_infrastructure_source_refresh_review:
  repository: bartytime4life/Kansas-Frontier-Matrix
  revision: "<exact commit SHA>"
  source_family: "<source product, archive, feed, or steward collection>"
  result: "<HOLD|ABSTAIN|DENY|ERROR|ESCALATE|READY_FOR_ACCOUNTABLE_SOURCE_REFRESH_REVIEW>"
  registry:
    authoritative_descriptor: "<path or NOT_AVAILABLE>"
    writer_verified: false
    generated_view_binding_verified: false
  descriptor:
    source_id: "<stable ID or NOT_AVAILABLE>"
    status: "<template|candidate|admitted|activated|denied|unknown>"
    activation_ref: null
  connector:
    path: "<path or unresolved>"
    implementation_verified: false
    network_used: false
  validation:
    commands: []
    exact_results: []
    limitations: []
  non_effects:
    source_contacted: false
    source_retrieved: false
    source_admitted: false
    source_activated: false
    lifecycle_written: false
    evidence_closed: false
    policy_approved: false
    released: false
    deployed: false
    promoted: false
    published: false
  blockers: []
  accountable_reviewers_needed: []
```

Do not include credentials, temporary download URLs, restricted excerpts,
facility interiors, dependency topology, precise sensitive coordinates,
private-person or private-property detail, or protected cultural material.

## Proposal-lineage disposition

The prior v0.1 body is superseded at this path and remains available in Git
history. Its source-family ideas may inform future admitted descriptors, but
current evidence does not support its live polling, watcher cadence, domain-
first lifecycle destinations, signing, Rekor, cache invalidation, heartbeat,
kill-switch, receipt, or direct promotion instructions.

Connected Drive Settlements/Infrastructure material remains read-only doctrine,
research, and design lineage. Notion remains coordination. Current GitHub bytes
control claims about implemented behavior.

## Documentation validation

For changes to this runbook:

1. review the complete diff for accuracy and unrelated churn;
2. check one H1, heading order, anchors, fences, tables, alerts, whitespace, and
   every changed relative link;
3. reconcile commands and paths against the exact schemas, validators,
   fixtures, tests, workflows, source-admission docs, registry boundary, and
   no-network procedure;
4. run focused repository checks when the environment is available, otherwise
   report them as not run;
5. bind hosted results to the exact head and separate introduced, inherited,
   skipped, pending, and unavailable checks.

Documentation and fixture checks cannot prove source freshness, rights,
activation, retrieval, lifecycle mutation, evidence closure, policy approval,
proof, release, deployment, publication, correction, or rollback execution.

## Documentation correction and rollback

Re-review this runbook when a real descriptor or activation record appears, the
registry writer or topology changes, a substantive connector lands, exact RAW
placement is accepted, policy becomes executable, domain semantics graduate,
or proof/release/correction/rollback support changes.

Before merge, close the draft PR and delete only its feature branch. After a
separately authorized merge, revert the focused documentation commit or apply a
reviewed forward correction.

A documentation revert does not undo or perform source retrieval, admission,
activation, lifecycle writes, policy decisions, proof, promotion, release,
deployment, publication, correction, withdrawal, cache invalidation, or
operational rollback.

## Related repository surfaces

- [Local procedure boundary](./README.md)
- [No-network validation](./NO_NETWORK_TEST_RUNBOOK.md)
- [Promotion preflight](./PROMOTION_RUNBOOK.md)
- [Rollback readiness](./ROLLBACK_RUNBOOK.md)
- [Domain boundary](../../domains/settlements-infrastructure/README.md)
- [Domain source-registry guidance](../../domains/settlements-infrastructure/SOURCE_REGISTRY.md)
- [Canonical path guidance](../../domains/settlements-infrastructure/CANONICAL_PATHS.md)
- [Sensitivity guidance](../../domains/settlements-infrastructure/SENSITIVITY.md)
- [Source admission process](../../sources/ADMISSION_PROCESS.md)
- [SourceDescriptor standard](../../sources/SOURCE_DESCRIPTOR_STANDARD.md)
- [Directory Rules](../../doctrine/directory-rules.md)
- [Lifecycle Law](../../doctrine/lifecycle-law.md)
- [Trust Membrane](../../doctrine/trust-membrane.md)
- [Canonical source registry](../../../data/registry/sources/README.md)
- [Domain source-registry lane](../../../data/registry/sources/settlements-infrastructure/README.md)
- [Parallel domain-first source view](../../../data/registry/settlements-infrastructure/sources/README.md)
- [Source-authority projection](../../../control_plane/source_authority_register.yaml)
- [RAW boundary](../../../data/raw/README.md)
- [Domain connector boundary](../../../connectors/settlements-infrastructure/README.md)
- [SourceDescriptor schema](../../../schemas/contracts/v1/source/source_descriptor.schema.json)
- [SourceDescriptor compatibility alias](../../../schemas/contracts/v1/sources/source_descriptor.schema.json)
- [SourceDescriptor fixtures](../../../fixtures/contracts/v1/source/source_descriptor/)
- [Generic SourceDescriptor validator](../../../tools/validators/validate_source_descriptor.py)
- [Compatibility validator](../../../tools/validators/sources/validate_source_descriptor.py)
- [SourceDescriptor entrypoint tests](../../../tests/validators/test_validate_source_descriptor_entrypoints.py)
- [SourceDescriptor workflow](../../../.github/workflows/source-descriptor-validate.yml)
- [EvidenceBundle projection schema](../../../schemas/contracts/v1/domains/settlements-infrastructure/evidence_bundle.schema.json)
- [Projection validator](../../../tools/validators/validate_settlements_infrastructure_evidence_bundle_projection.py)
- [Projection tests](../../../tests/validators/domains/settlements-infrastructure/test_evidence_bundle_schema_convergence.py)
- [Projection workflow](../../../.github/workflows/settlements-infrastructure-evidence-bundle-convergence.yml)

[Back to top](#top)

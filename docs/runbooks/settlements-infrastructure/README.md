<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks-settlements-infrastructure-readme
title: docs/runbooks/settlements-infrastructure/ — Settlements and Infrastructure Operational Procedure Boundary
type: readme
subtype: boundary-compact
version: v1.3
prior_state: v1.2 boundary with three repository-grounded procedures and one proposal-era source-refresh procedure
status: draft; repository-grounded; four child procedures current within bounded documentation scope; static readiness, SourceDescriptor fixture validation, and EvidenceBundle projection convergence executable; live source refresh, domain semantic validation, proof, operational rollback, release, deployment, promotion, and publication held
owners:
  - "@bartytime4life — verified GitHub review route"
  - "NEEDS VERIFICATION — accountable Settlements/Infrastructure, source, registry, rights, infrastructure-security, cultural, sovereignty, evidence, policy, operations, correction, rollback, and release assignments"
created: 2026-08-28
updated: 2026-08-29
policy_label: repository-facing; critical-infrastructure-sensitive; cultural-and-sovereignty-sensitive; fail-closed
current_path: docs/runbooks/settlements-infrastructure/README.md
owning_root: docs/
responsibility: human procedure index and operational boundary for the Settlements/Infrastructure lane
truth_posture: cite-or-abstain
authority_class: explanatory operational documentation
authority_rank: subordinate to accepted doctrine and ADRs, contracts, schemas, source records, policy, evidence, lifecycle, review, release, correction, rollback, and competent official authorities
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: bd4eb1fd42e947a21f2d7679dd318f79973c0067
  prior_blob: 3ff33de15249486f520df1fafd934451b268012b
  no_network_runbook_blob: 90133c88ddf2d053a9ca1021e1951e2b241a4ebd
  promotion_runbook_blob: 290428184cc7eb89df1932724cc666592c358712
  rollback_runbook_blob: 9abe532e2476258850a8e318ac6d67f735224d51
  source_refresh_runbook_prior_blob: c8895a5e90d2d8bd2628c6ca72dd9f216c3a724e
  source_refresh_runbook_blob: 5bc74a2c4a70aeb2043f7c8e8a77eb66e52f4601
  domain_workflow_blob: a47d89c40efd58ac31bc44dbc56bdfb1ccc3a325
  evidence_bundle_convergence_workflow_blob: 584ac26dcaf5791b1a560cb71bd059e889f55791
  source_descriptor_workflow_blob: 6d3f900efcddc17d24a528a92190544fc350b63b
  source_descriptor_schema_blob: 582e70b834278c3c6ca9a8b31efbe0989c96f0bc
  source_descriptor_alias_blob: 42da54b28a527850cce88ad89f68921c101fc56b
  canonical_source_registry_readme_blob: 913d694acbe8fbd1660790c9b4c8c614a9cdd627
  domain_first_source_registry_readme_blob: 9defa909410d4fba6d16ecf7f8ae6ea66da16d6e
  source_authority_register_blob: 32729857bc8eb5001acb37b8ee8e60bcb6e0dc50
  domain_connector_readme_blob: a6fc165cd2c1a2ed3baef5df06b02ea754f7a68f
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  direct_child_runbooks: 4
  repository_grounded_child_procedures: 4
  verified_live_source_refresh_profiles: 0
  executable_domain_semantic_validator_profiles: 0
related:
  - ../README.md
  - ../../domains/settlements-infrastructure/README.md
  - ../../sources/ADMISSION_PROCESS.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../.github/workflows/domain-settlements-infrastructure.yml
  - ../../../.github/workflows/settlements-infrastructure-evidence-bundle-convergence.yml
  - ../../../.github/workflows/source-descriptor-validate.yml
  - ../../../data/registry/sources/settlements-infrastructure/README.md
  - ../../../data/registry/settlements-infrastructure/sources/README.md
  - ../../../control_plane/source_authority_register.yaml
  - ../../../connectors/settlements-infrastructure/README.md
notes:
  - "v1.3 reconciles the final proposal-era child after the source-refresh runbook became a repository-grounded readiness and accountable-review procedure."
  - "No child procedure contacts or activates a live source, validates real domain records, produces proof, executes production rollback, or authorizes release, deployment, promotion, or publication."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Settlements and Infrastructure Operational Procedure Boundary

This directory routes maintainers to Settlements/Infrastructure procedures and
states the lane's current fail-closed posture. It is an index and boundary
contract, not municipal-status, census, facility, condition, service,
dependency, source, policy, evidence, proof, rollback, release, or publication
authority.

> [!WARNING]
> KFM is not an emergency, public-safety, utility-service, infrastructure-
> condition, municipal-law, land-use, planning, inspection, security, legal, or
> regulatory authority. Repository files and passing checks cannot establish
> that a place is legally incorporated, a facility is safe, a service is
> available, or infrastructure is current, complete, lawful, or suitable for
> operational decisions.

> [!IMPORTANT]
> All four child runbooks are repository-grounded within their declared
> documentation boundaries. Current executable evidence remains limited to
> static readiness, fixture-only SourceDescriptor validation, and
> no-network-compatible EvidenceBundle projection convergence. Live source
> refresh, substantive domain validation, proof, production rollback, release,
> deployment, promotion, and publication remain held.

**Navigate:** [maturity](#current-maturity) ·
[procedures](#child-procedure-maturity) ·
[validation](#bounded-executable-profiles) ·
[safety](#safety-and-authority-boundaries) ·
[maintenance](#maintenance-and-documentation-rollback)

## Purpose and placement

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
adopts the [Directory Rules](../../doctrine/directory-rules.md). Human
procedures belong below `docs/runbooks/`; contracts, schemas, policy, source
records, lifecycle data, proofs, and release objects remain in their own
responsibility roots.

This README:

- distinguishes bounded executable checks from held operational work;
- routes readers to the current child procedures and responsibility roots;
- preserves settlement/infrastructure, legal/census, source-role, time,
  sensitivity, cultural, sovereignty, and cross-domain boundaries; and
- keeps validation, source admission, review, rollback, release, deployment,
  promotion, publication, and correction as separate states.

It does not resolve `settlement` versus `settlements-infrastructure` aliases,
the registry writer, generated views, exact RAW placement, SourceDescriptor
path/name variants, or accountable steward assignments.

## Current maturity

| Surface | Current evidence | Bounded conclusion |
|---|---|---|
| Static domain readiness | The domain workflow checks required paths, parses tracked JSON, classifies placeholders, and records explicit semantic/proof/release holds. | Readiness classification only |
| SourceDescriptor profile | Rich schema, plural compatibility alias, two validator entrypoints, synthetic fixtures, focused tests, and a workflow exist. | Shape, compatibility, and fixture polarity only |
| EvidenceBundle convergence | A separate profile checks domain projection delegation and shared synthetic fixtures. | Schema convergence only |
| Source registry | Canonical-family and domain-first layouts coexist; one placeholder record and five proposal templates were observed; the source-authority projection is empty. | No admitted or activated source inventory |
| Connectors | The domain connector is documentation-only; Census fetch/admission surfaces remain comments-only placeholders. | No live refresh path |
| Policy and semantic validation | Domain policy is evaluator-unbound; direct semantic validators remain unestablished. | Operational decisions held |
| Proof and release | Domain workflow records no accepted proof producer or release-dry-run command. | No release, promotion, or publication authority |
| Rollback | Documentation can describe readiness and failure classes; no released candidate-bound recovery evidence is established. | Production rollback held |

## Child-procedure maturity

| Procedure | Current classification | Safe use |
|---|---|---|
| [`NO_NETWORK_TEST_RUNBOOK.md`](./NO_NETWORK_TEST_RUNBOOK.md) | Repository-grounded, guarded local EvidenceBundle schema-convergence procedure | Run only the named synthetic profile and report its limitations |
| [`PROMOTION_RUNBOOK.md`](./PROMOTION_RUNBOOK.md) | Repository-grounded promotion preflight and accountable-review handoff | Prepare a bounded dossier; do not promote |
| [`ROLLBACK_RUNBOOK.md`](./ROLLBACK_RUNBOOK.md) | Repository-grounded rollback-readiness procedure | Assess recovery prerequisites; do not execute production rollback |
| [`SOURCE_REFRESH_RUNBOOK.md`](./SOURCE_REFRESH_RUNBOOK.md) | Repository-grounded source-refresh readiness procedure | Inspect repository state, run bounded fixture checks, and return `HOLD` or a review handoff; do not contact a source |

No child procedure becomes operational merely because a path, schema,
workflow, or long-form document exists.

## Bounded executable profiles

### Static readiness

The [domain workflow](../../../.github/workflows/domain-settlements-infrastructure.yml)
uses read-only repository permissions and records explicit holds for semantic
validation, proof production, and release dry run. A green run means those
checks and held-state sentinels behaved as written at one SHA.

### SourceDescriptor fixtures

```bash
python tools/validators/validate_source_descriptor.py --fixtures
python tools/validators/sources/validate_source_descriptor.py --fixtures
python -m pytest -q \
  tests/validators/test_validate_source_descriptor_entrypoints.py \
  tests/schemas/test_common_contracts.py \
  -k source_descriptor
```

The [workflow](../../../.github/workflows/source-descriptor-validate.yml) and
fixtures test selected shape, rights-field, alias, entrypoint, and negative-case
expectations. They do not admit, activate, retrieve, rights-clear, or release a
source.

### EvidenceBundle projection convergence

Use the complete guarded procedure in
[`NO_NETWORK_TEST_RUNBOOK.md`](./NO_NETWORK_TEST_RUNBOOK.md). The corresponding
[workflow](../../../.github/workflows/settlements-infrastructure-evidence-bundle-convergence.yml)
checks projection delegation and shared synthetic fixtures. It does not prove
materialized evidence, domain truth, policy approval, proof, or release.

## Safety and authority boundaries

Settlements/Infrastructure material can expose critical facilities, interiors,
dependencies, condition observations, service gaps, private-property context,
living-person proximity, reservation communities, culturally significant
places, archaeological locations, and harmful precision. Apply the most
restrictive supported exposure and stop when rights, sovereignty, consent,
sensitivity, source role, time, freshness, geometry lineage, uncertainty, or
correction status is unresolved.

Keep these distinctions visible:

- legal municipalities are not interchangeable with census places, named
  places, post offices, historic townsites, communities, or map labels;
- a facility record is not proof of ownership, operation, condition, capacity,
  availability, safety, access, or current status;
- generalized public geometry does not replace restricted canonical geometry;
- maps, schemas, tests, workflows, dashboards, indexes, and generated language
  are not sovereign truth;
- source admission, source activation, review, release, deployment, promotion,
  publication, correction, withdrawal, and rollback are separate transitions.

Do not place credentials, temporary source URLs, restricted payloads, facility
interiors, dependency graphs, exploitable condition details, precise sensitive
coordinates, private-person details, or protected cultural material in
runbooks, pull requests, logs, or synthetic fixtures.

## Stop conditions

Return `HOLD`, `ABSTAIN`, `DENY`, `ERROR`, or `ESCALATE` when any required item
is unresolved, including:

- source identity, role, rights, terms, cadence, currentness, legal authority,
  retrieval context, or activation;
- settlement, facility, operator, observation, service, dependency, geometry,
  or cross-domain identity;
- registry writer, generated-view binding, connector, RAW/QUARANTINE placement,
  or deterministic capture identity;
- policy, sensitivity, infrastructure-security, cultural, sovereignty,
  archaeology, privacy, or accountable reviewer authority;
- evidence, proof, candidate, manifest, correction path, invalidation plan, or
  rollback target;
- governed public interface, release, deployment, promotion, or publication
  state.

Never weaken a schema check, placeholder sentinel, no-network boundary, policy
hold, proof hold, release hold, negative fixture, or topology ratchet to obtain
a passing result.

## Related responsibility roots

- [Settlements/Infrastructure domain](../../domains/settlements-infrastructure/README.md)
- [Source admission process](../../sources/ADMISSION_PROCESS.md)
- [Directory Rules](../../doctrine/directory-rules.md)
- [Canonical source registry](../../../data/registry/sources/settlements-infrastructure/README.md)
- [Parallel domain-first source view](../../../data/registry/settlements-infrastructure/sources/README.md)
- [Source-authority projection](../../../control_plane/source_authority_register.yaml)
- [Domain connector boundary](../../../connectors/settlements-infrastructure/README.md)
- [Domain policy boundary](../../../policy/domains/settlements-infrastructure/README.md)
- [Domain proof boundary](../../../data/proofs/settlements-infrastructure/README.md)
- [Release-candidate boundary](../../../release/candidates/settlements-infrastructure/README.md)

## Maintenance and documentation rollback

Re-review this index when a child runbook changes, a descriptor or activation
record appears, the registry writer or topology changes, a substantive connector
lands, exact RAW placement is accepted, domain semantics or policy graduate, or
proof/release/correction/rollback evidence changes.

Before merge, close the draft PR and delete only its feature branch. After a
separately authorized merge, revert the focused documentation commit or submit a
reviewed forward correction. Documentation rollback does not undo source
admission, activation, evidence, policy, lifecycle, release, deployment,
promotion, publication, correction, withdrawal, or production rollback state.

[Back to top](#top)

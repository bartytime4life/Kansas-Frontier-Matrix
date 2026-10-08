<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract-guide/domains/hazards/domain-validation-report
title: Hazards validation report draft semantic contract
type: draft-semantic-contract
version: v1.0
status: draft; proposed; repository-grounded; review-required
owners:
  - OWNER_TBD - Hazards and validation stewards
created: 2026-10-08
updated: 2026-10-08
policy_label: public
owning_root: contracts/
responsibility: Hazards validation report draft semantic contract; explain semantic review requirements without adopting a schema, policy, source, or release decision
truth_posture: CONFIRMED inspected repository shape and paths; PROPOSED semantic review examples; UNKNOWN operational acceptance
related:
  - contracts/domains/hazards/README.md
  - schemas/contracts/v1/domains/hazards/domain_validation_report.schema.json
  - docs/domains/hazards/SOURCE_ROLE_MATRIX.md
  - docs/domains/hazards/LIFE_SAFETY_BOUNDARY.md
evidence_snapshot: ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe
[/KFM_META_BLOCK_V2] -->

# Contract: domain_validation_report

**Family:** `domains/hazards`
**Schema:** `schemas/contracts/v1/domains/hazards/domain_validation_report.schema.json`
**Status:** draft / PROPOSED; semantic review requirements, not an accepted report producer.

## Meaning

A Hazards domain validation report should bind the checks performed to an exact
candidate, validator/profile version and finite result. It explains what was
checked, what failed or remains unverified, and what downstream use remains held.
It is not an alert, warning, incident assessment, regulatory determination,
EvidenceBundle, source-admission decision or release authorization.

Hazards include source roles and times that cannot be conflated. Observations,
modeled risk, regulatory maps, infrastructure inventories and operational
advisories have different evidence and currentness requirements. A report must
state the profile actually tested instead of implying all hazard semantics passed.
See the [source-role matrix](../../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md)
and [life-safety boundary](../../../docs/domains/hazards/LIFE_SAFETY_BOUNDARY.md).

## Fields

The [current schema](../../../schemas/contracts/v1/domains/hazards/domain_validation_report.schema.json)
declares `id`, `version` and `spec_hash`, requires only string `id`, and permits
additional properties. It does not yet enforce the review fields below. Its
metadata names `tools/validators/domains/hazards/validate_domain_validation_report.py`,
but that file is absent at the pinned revision. A declared validator path is not
an executable producer or an emitted report.

| Proposed required meaning | Reviewer needs |
|---|---|
| Report identity | Stable report/candidate identity and version; exact hash algorithm must be accepted before use |
| Subject binding | Exact candidate/artifact identity, content digest and source/product version |
| Validation binding | Validator, schema and profile versions; invocation and environment |
| Scope | Quantity, source role, temporal support, geography and specific checks performed |
| Results | Per-check findings, severity/reason, finite outcome and rejected/missing evidence |
| Time | Execution time plus source valid/effective/expiry clocks where the profile requires them |
| Evidence | References to inputs and results under appropriate access controls |
| Limitations | Untested dimensions, synthetic/fixture status and operational boundaries |
| Governance | Separate source, rights, sensitivity, policy, review and release statuses |
| Correction | Prior report/subject supersession and revalidation trigger |

Field names beyond the existing three are design requirements for future schema
review, not a wire-format promise. Keep machine shape in the owning schema.

## Invariants

1. A report applies only to the exact subject and validator/profile it binds.
2. An expired advisory cannot become current because validation ran recently.
3. Missing, ambiguous or failed checks remain visible; a readiness hold is not
   an emitted proof or a domain-wide pass.
4. Observed, modeled, regulatory, administrative and operational roles retain
   their meaning through validation and display.
5. Fixture conformance does not establish live source availability, hazard truth,
   safe passage, public safety or permission to release.
6. Findings must avoid echoing secrets, sensitive infrastructure precision or
   restricted payloads into public logs or reports.

## Illustrative review cases

**Coherent synthetic report proposal:** a record binds a synthetic drought
materiality candidate and the exact profile, distinguishes its expected held or
candidate result, and explicitly leaves real source and release gates unresolved.

**Invalid report claim:** schema parsing is described as proof that a regulatory
flood map is a live flood warning, or a passed test is attached to subsequently
changed candidate bytes. These are semantic errors even if the open schema
accepts their JSON shape.

## Lifecycle

A future producer creates a report after executing the bound checks on an exact
candidate. Review and promotion remain separate. Changed source bytes, schema,
validator, policy or support semantics can require a new report; preserve the
old binding and link supersession rather than rewriting history. Released
consumers require their own correction/withdrawal process.

## Related contracts

- [Hazards contract index](README.md)
- [Decision envelope](hazards_decision_envelope.md)
- [Drought observation](drought_observation.md) and [declaration](drought_declaration.md)
- [Drinking-water advisory](drinking_water_advisory.md)
- [NFHL/NLD/NID source-role profile](nfhl_nld_nid_source_role_profile.md)
- [Hazards workflow](../../../.github/workflows/domain-hazards.yml)

The workflow already executes bounded profiles and retains broader holds. Its
results are evidence about those profiles; they do not implement this generic
report contract or resolve its missing producer.

## Open questions

Before this contract can graduate, reviewers must bind report identity/hash
semantics, closed schema fields, producer/validator, safe finding vocabulary,
fixtures for pass/fail/hold/error, source-clock rules and correction lineage.
Add exact negative tests for wrong-subject binding, expired-as-current claims,
source-role collapse, leaked sensitive detail and authority overclaims. Name
accountable reviewers without inventing assignments or accepted decisions.

Completion of this document supplies a real semantic review guide. Implementation,
source admission, evidence resolution, policy, release and public acceptance
remain independently unverified.

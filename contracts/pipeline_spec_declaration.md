<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/pipeline-spec-declaration
title: KfmPipelineSpecDeclaration Contract
type: contract
version: v1.0
status: proposed-inactive
owners: OWNER_TBD — Pipeline specification steward · Schema steward · Validation steward · Domain steward
created: 2026-08-30
updated: 2026-08-30
policy_label: public; pipeline-specification; declarative-only; inactive; no-live-effects
owning_root: contracts/
responsibility: define semantic meaning and fail-closed invariants for inactive pipeline declarations
truth_posture: CONFIRMED repository contract shape / PROPOSED inactive declarations / NEEDS VERIFICATION human review and activation prerequisites
related:
  - ../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../docs/doctrine/directory-rules.md
  - ../pipeline_specs/README.md
  - ../schemas/contracts/v1/pipeline_spec_declaration.schema.json
  - ../fixtures/contracts/v1/pipeline_spec_declaration/
  - ../tools/validators/validate_pipeline_spec_declarations.py
  - ../tests/validators/test_validate_pipeline_spec_declarations.py
tags: [kfm, pipeline-spec, declaration, inactive, fixture-only, compatibility-alias, fail-closed]
notes:
  - "This contract governs declarative repository records only."
  - "A conforming declaration cannot activate a source, execute a network request, write a lifecycle target, promote, release, or publish."
[/KFM_META_BLOCK_V2] -->

# KfmPipelineSpecDeclaration Contract

KfmPipelineSpecDeclaration is the common, fail-closed declaration shape for an
inactive pipeline stage boundary, an inactive pipeline candidate, or a
compatibility alias. It preserves reviewable intent without converting a file
under pipeline_specs into an executable or an activation registry entry.

## Status and authority

This contract is PROPOSED_INACTIVE. Schema validity and validator PASS are
bounded repository-conformance results. Neither result grants source,
execution, lifecycle, policy, promotion, release, publication, or public-use
authority.

ADR-0029 adopts Directory Rules v2, and this contract follows its authority
split:

| Surface | Authority |
|---|---|
| GitHub repository | The reviewed, version-controlled declaration, schema, fixtures, validator, tests, and workflow are the authoritative implementation record for this contract. |
| Google Drive | Referenced source documents may provide read-only lineage or background. A Drive document cannot mutate the declaration or grant runtime authority. |
| Notion | Coordination, planning, review notes, and task state only. A Notion page is not a schema, activation decision, release decision, or executable specification. |
| pipeline_specs/ | Declarative intent only. Recursive discovery is validation scope, never activation. |
| pipelines/ | Executable pipeline implementation belongs here and must be referenced explicitly when fixture-first implementation exists. |
| contracts/ | Semantic meaning, including this document. |
| schemas/ | Machine-checkable shape. |
| tools/validators/ and tests/ | Conformance enforcement, not operational authority. |

## Non-effects

Every declaration is inactive. It MUST NOT:

- activate or admit a source;
- fetch from a network;
- read live source material as an execution side effect;
- write RAW, QUARANTINE, WORK, PROCESSED, CATALOG, RELEASE, PUBLISHED,
  receipt, or other durable lifecycle targets;
- approve policy or evidence closure;
- promote or release an artifact;
- publish or authorize public use;
- treat a compatibility alias as a second writable authority.

The execution object records six independent DENIED boundaries so that one
permission cannot be inferred from another.

## Object profiles

| profile_kind | Meaning | Required posture |
|---|---|---|
| STAGE_BOUNDARY | An explicit declarative boundary for one pipeline stage. | NOT_IMPLEMENTED and DISABLED unless a later versioned contract says otherwise. |
| PIPELINE_CANDIDATE | A bounded candidate declaration. | NOT_IMPLEMENTED and DISABLED, or IMPLEMENTED_FIXTURE_FIRST and FIXTURE_ONLY. |
| COMPATIBILITY_ALIAS | A read-only path retained to route an old reference to one canonical declaration. | canonical_target required; NOT_IMPLEMENTED; DISABLED; never a second writable specification. |

IMPLEMENTED_FIXTURE_FIRST means only that a deterministic local fixture path,
implementation, fixtures, tests, and workflow are bound. It still requires
network_access, source_activation, lifecycle_write, promotion, release, and
publication to remain DENIED, and lifecycle.writes_targets to remain false.

## Fields

| Field | Requirement and meaning |
|---|---|
| schema_version | Exactly 1.0.0 for this schema generation. |
| object_type | Exactly KfmPipelineSpecDeclaration. |
| spec_id | Stable declaration identifier. It identifies the declaration, not an activated runtime job. |
| spec_version | Semantic version of the declaration. |
| profile_kind | STAGE_BOUNDARY, PIPELINE_CANDIDATE, or COMPATIBILITY_ALIAS. |
| domain_id | Registered domain or governed shared lane identifier. The validator checks path/domain coherence. |
| stage | INGEST, NORMALIZE, VALIDATE, CATALOG, PUBLISH, DERIVE, WATCH, REFRESH, PUBLISH_DRY_RUN, or UNSPECIFIED. |
| status | Exactly PROPOSED_INACTIVE. |
| implementation_status | NOT_IMPLEMENTED or IMPLEMENTED_FIXTURE_FIRST. |
| path | Repository-relative path to the declaration under pipeline_specs. It must match the file being validated. |
| purpose | Human-readable bounded intent that does not assert activation. |
| canonicalization_profile | Exactly kfm-canonical-json-v1. |
| canonical_target | Required only for COMPATIBILITY_ALIAS and prohibited for other profiles. It must resolve to a different canonical declaration. |
| source_docs | Sorted, unique, repository-relative documentation references. These are lineage only. |
| bindings | Seven closed, sorted, unique reference arrays described below. |
| lifecycle | Candidate input/output labels and an explicit false write posture. |
| execution | DISABLED or FIXTURE_ONLY plus six independent DENIED authorities. |
| required_gates | Sorted, unique gate names that remain prerequisites for any future activation. |
| reason_codes | Sorted, unique finite reason codes describing the inactive state. |
| non_effects | Sorted, unique statements of authority the declaration does not create. |
| rollback | Repository-only rollback strategy, exactly REVERT_DECLARATION_CHANGE. |
| spec_hash | SHA-256 of the canonical parsed object after removing the top-level spec_hash field. |
| validation | Optional bounded command and workflow references. Required for IMPLEMENTED_FIXTURE_FIRST. |

### Bindings

The bindings object is closed and contains exactly these seven arrays:

| Array | Meaning |
|---|---|
| source_descriptor_refs | Source descriptors referenced for review; the reference does not activate them. |
| contract_refs | Semantic contract references. |
| schema_refs | Machine-shape references. |
| implementation_refs | Executable implementation references under the accepted implementation roots. |
| fixture_refs | Deterministic local fixture references. |
| test_refs | Focused executable conformance-test references. |
| workflow_refs | CI workflow references. |

Empty arrays are explicit and valid for NOT_IMPLEMENTED declarations. A
fixture-first declaration must bind at least one source descriptor, contract,
schema, implementation, fixture, test, and workflow, and must include the
validation object.

### Lifecycle

lifecycle.candidate_inputs and lifecycle.candidate_outputs describe only
potential graph edges. They do not authorize a transition. Either array may be
empty when the declaration intentionally refuses to infer an unreviewed
lifecycle edge.

lifecycle.writes_targets is always false. declared_possible_targets is
optional and, when present, documents destinations a future reviewed
implementation might use. Listing a possible target does not create write
authority.

### Execution

execution.mode is:

- DISABLED when implementation_status is NOT_IMPLEMENTED; or
- FIXTURE_ONLY when implementation_status is IMPLEMENTED_FIXTURE_FIRST.

The following fields are always DENIED:

- network_access;
- source_activation;
- lifecycle_write;
- promotion;
- release;
- publication.

## Compatibility aliases

A COMPATIBILITY_ALIAS MUST provide canonical_target, MUST be NOT_IMPLEMENTED,
and MUST be DISABLED. canonical_target is prohibited for the other two
profiles. The validator additionally checks that canonical_target is not equal
to path, resolves within pipeline_specs, and points at a non-alias canonical
declaration.

An alias exists only to preserve inbound references during a reviewed
migration. It cannot be independently scheduled, bound to an implementation,
or edited as a second source of pipeline truth.

## Canonicalization and spec_hash

kfm-canonical-json-v1 is defined for this object as follows:

1. Parse exactly one UTF-8 YAML document as a mapping with duplicate keys,
   aliases, custom tags, non-finite numbers, and symlinks denied.
2. Remove the top-level spec_hash member.
3. Serialize the remaining parsed value as UTF-8 JSON with keys sorted,
   separators comma and colon, no insignificant whitespace, Unicode preserved,
   array order preserved, and non-finite values denied.
4. Compute SHA-256 over those bytes.
5. Encode the value as sha256 followed by a colon and 64 lowercase hexadecimal
   characters.

Equivalent reference pseudocode is:

    canonical = json.dumps(
        declaration_without_spec_hash,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")
    spec_hash = "sha256:" + hashlib.sha256(canonical).hexdigest()

The hash proves representation integrity only. It does not prove correctness,
admission, policy approval, evidence closure, activation, release, or
publication.

## Validation

The intended bounded validator and test entrypoints are:

- tools/validators/validate_pipeline_spec_declarations.py
- tests/validators/test_validate_pipeline_spec_declarations.py

The validator must support exact fixture polarity and deterministic findings:

| Outcome | Meaning |
|---|---|
| PASS | The declaration is safe to parse, schema-valid, hash-coherent, and semantically coherent for this inactive contract. |
| DENY | The declaration violates shape, hash, path, alias, binding, or fail-closed invariants. |
| ERROR | The declaration, schema, registry, or fixture cannot be read or evaluated safely. |

PASS is not activation. The validator may enumerate files for conformance, but
that enumeration MUST NOT be reused as a runtime registry or scheduler input.

## Change and rollback

Changes require contract/schema/fixture/validator/test parity and review by the
affected domain and pipeline-spec stewards. Changes to profile meaning,
canonicalization, hashing, authority boundaries, or conditional rules require
a versioned migration.

Rollback is limited to reverting the bounded repository declaration change.
It does not mutate runtime state, lifecycle stores, source systems, Drive,
Notion, release records, or public surfaces.

## Definition of done

A declaration conforms only when:

- it validates against the Draft 2020-12 schema;
- its parsed canonical projection reproduces spec_hash;
- its path and domain are coherent with repository placement;
- alias and fixture-first conditional rules pass;
- every execution authority remains DENIED;
- writes_targets remains false;
- fixtures produce the exact expected outcomes and findings;
- focused tests and CI pass without network or durable lifecycle writes.

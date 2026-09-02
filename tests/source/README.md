<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-source-readme
title: tests/source/ — Source assessment and anti-collapse test lane
type: README; directory-readme; source-test-lane; executable-inventory
version: v0.3
status: draft; repository-grounded; executable-partial; workflow-binding-unverified; no-network; fail-closed; non-authoritative
owner: "@bartytime4life — CONFIRMED CODEOWNERS review route; source, rights, sensitivity, privacy, QA, security, and release stewardship remain NEEDS VERIFICATION"
created: 2026-07-07
updated: 2026-08-30
supersedes: v0.2 documentation at the same path
policy_label: repository-facing; tests; source; source-role; source-health; retrieval-intent; fixture-only; no-network; fail-closed; non-publisher
current_path: tests/source/README.md
owning_root: tests/
responsibility: executable conformance checks for selected source schemas, assessments, candidates, summaries, roles, health states, and anti-authority-collapse boundaries
truth_posture: a passing test supports only its named assertion and checked revision; it does not admit or activate a source, prove source truth, resolve rights or sensitivity, close evidence, approve policy, or authorize release or publication
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 1ea6593ede80d5ce10f561c7eec72135d6ccf806
  direct_modules: 9
  source_defined_tests: 60
  directly_workflow_bound_modules: 0
related:
  - ../README.md
  - ../../contracts/source/README.md
  - ../../schemas/contracts/v1/source/README.md
  - ../../fixtures/contracts/v1/source/
  - ../../tools/validators/source/
  - ../../tools/validators/source_probe/
  - ../../tools/validators/source_role/
  - ../../data/registry/sources/README.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "v0.3 replaces the obsolete README-only direct-lane claim with the current nine-module executable inventory."
  - "The module and test counts describe source at the pinned commit, not a recorded run or permanent coverage promise."
  - "Repository code search did not establish a workflow command or Make target that directly collects tests/source."
  - "This README is authored at its canonical test-lane path; it is not generated or mirrored."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tests/source/` — Source assessment and anti-collapse test lane

> Executable, fixture-backed checks for selected source-governance objects and
> offline assessment behavior. This lane tests bounded conformance; it is not a
> source registry, admission decision, policy engine, evidence store, or
> publisher.

## Purpose and audience

Use this README to locate the direct tests under `tests/source/`, run the
focused collection, understand failure meaning, and identify current workflow
gaps. It serves maintainers and reviewers working on source descriptors,
offline assessment validators, retrieval declarations, source health,
source-role transitions, synthetic snapshot candidates, and steward-facing
summaries.

The prior v0.2 README described this directory as README-only. That claim is
materially false at the pinned revision: the directory contains nine
`test_*.py` modules and 60 source-defined test functions or methods.

## Authority and placement

Accepted [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
makes the Directory Rules path authoritative for placement. The
[`tests/` root contract](../README.md) assigns executable conformance evidence
to `tests/`, so this same-path README and the existing source tests are
precedent-backed children of that root.

| Concern | Authority home | Role of this lane |
|---|---|---|
| Source meaning and invariants | [`contracts/source/`](../../contracts/source/README.md) | Exercise named behavior; do not redefine it. |
| Machine shape | [`schemas/contracts/v1/source/`](../../schemas/contracts/v1/source/README.md) | Check selected schemas and fixture polarity. |
| Reusable fixtures | [`fixtures/contracts/v1/source/`](../../fixtures/contracts/v1/source/) | Consume synthetic review inputs; do not become fixture authority. |
| Validator and renderer implementation | `tools/validators/` and `tools/ci/` | Exercise entrypoints, outcomes, diagnostics, and effects. |
| Source identities and state | [`data/registry/sources/`](../../data/registry/sources/README.md) and governed decision surfaces | Test references and boundaries; never admit or activate. |
| Rights, sensitivity, sovereignty, privacy, policy, evidence, and release | Their accepted authority roots | Remain distinct from test success. |

## Confirmed direct inventory

At `main@1ea6593ede80d5ce10f561c7eec72135d6ccf806`,
the directory contains the following executable modules:

| Module | Tests | Direct subject and bounded assertion |
|---|---:|---|
| [`test_doctrine_artifact_descriptor_schema.py`](test_doctrine_artifact_descriptor_schema.py) | 1 | [Doctrine-artifact descriptor validator](../../tools/validators/source/validate_doctrine_artifact_descriptor.py): valid and invalid fixture replay through the declared schema. |
| [`test_doctrine_artifact_preflight_summary_schema.py`](test_doctrine_artifact_preflight_summary_schema.py) | 1 | [Doctrine-artifact preflight-summary validator](../../tools/validators/source/validate_doctrine_artifact_preflight_summary.py): valid and invalid fixture replay through the declared schema. |
| [`test_kansas_transportation_geometry_source_assessment.py`](test_kansas_transportation_geometry_source_assessment.py) | 9 | [Kansas transportation geometry source validator](../../tools/validators/source/validate_kansas_transportation_geometry_source_assessment.py): schema validity, exact case polarity, deterministic identity, four declared roles, zero-authority effects, no-network execution, unsafe JSON denial, and value-safe CLI diagnostics. |
| [`test_official_source_snapshot_candidate.py`](test_official_source_snapshot_candidate.py) | 3 | [Official-source snapshot candidate validator](../../tools/validators/source/official_source_snapshot_candidate.py): deterministic local capture metadata, content-bound identity, explicit non-authority flags, and authority-escalation rejection. |
| [`test_render_source_intake_steward_summary.py`](test_render_source_intake_steward_summary.py) | 10 | [Source-intake steward-summary renderer](../../tools/ci/render_source_intake_steward_summary.py): deterministic review projection, no-change handling, quarantine redaction, rollback holds, Markdown escaping, value-free errors, no-network enforcement, CLI exit behavior, and symlink denial. |
| [`test_retrieval_intent_query_snapshot_assessment.py`](test_retrieval_intent_query_snapshot_assessment.py) | 15 | [Retrieval intent/query snapshot validator](../../tools/validators/source/validate_retrieval_intent_query_snapshot_assessment.py): four-way fixture polarity, deterministic identity and query hash, zero-authority review result, abstention and no-claim behavior, query-drift denial, secret exclusion, no-network replay, unsafe-input rejection, CLI behavior, and value-safe diagnostics. |
| [`test_source_health_assessment.py`](test_source_health_assessment.py) | 13 | [Offline source-health validator](../../tools/validators/source/validate_source_health_assessment.py): exact valid and invalid outcomes, compatibility denial codes, bounded input handling, non-echoing findings, no-network validation, and credential-free deterministic CLI output. |
| [`test_source_probe_envelope.py`](test_source_probe_envelope.py) | 4 | [Source-probe envelope validator](../../tools/validators/source_probe/validate_source_probe_envelope.py): valid profile replay, exact negative codes, activation hold preservation, and `spec_hash` mismatch denial. |
| [`test_source_role_transition_assessment.py`](test_source_role_transition_assessment.py) | 4 | [Source-role transition validator](../../tools/validators/source_role/validate_source_role_transition_assessment.py): schema validity, fixture polarity, modeled-as-observed denial, and candidate-promotion hold behavior. |

This inventory is complete only for direct files at the pinned revision. Source
tests also exist under schema, policy, validator, connector, pipeline, domain,
and application-owned paths. Those adjacent suites are not silently claimed by
this lane.

## Running the lane

From the repository root:

```bash
KFM_NO_NETWORK=1 \
PYTHONDONTWRITEBYTECODE=1 \
PYTHONHASHSEED=0 \
PYTHONUNBUFFERED=1 \
TZ=UTC \
python -m pytest -q tests/source
```

This is a focused maintainer command derived from the current pytest layout.
It is not a dedicated Make target, a recorded run, or a canonical
repository-wide suite.

For the two schema-wrapper modules, these narrower commands exercise the
underlying fixture validators directly:

```bash
python tools/validators/source/validate_doctrine_artifact_descriptor.py --fixtures
python tools/validators/source/validate_doctrine_artifact_preflight_summary.py --fixtures
```

Run a single module during focused diagnosis:

```bash
KFM_NO_NETWORK=1 python -m pytest -q \
  tests/source/test_source_health_assessment.py
```

Command presence is not pass evidence. Record the exact revision, command,
environment, result, and any unavailable dependency when reporting execution.

## Inputs and outputs

The direct modules consume repository-owned schemas, validators, and synthetic
fixtures. Depending on the module, outputs are assertions over:

- schema and fixture polarity;
- deterministic hashes and assessment or snapshot identifiers;
- finite `PASS`, `ABSTAIN`, `DENY`, `ERROR`, `HOLD`, or review states;
- finding codes and safe JSON paths;
- presentation-only Markdown summaries;
- CLI exit status and deterministic serialized output; and
- explicit false authority effects such as no activation, no evidence
  emission, and no public-use approval.

Temporary files created by tests remain test-local. A rendered summary,
candidate snapshot, test log, or passing assertion is not a registry record,
EvidenceBundle, policy decision, review record, receipt, proof, release
manifest, or published artifact.

## Workflow boundary

Bounded repository code search did not find a workflow command, Make target, or
other hosted command that directly names `tests/source` or any of its nine test
filenames. The validator registry references the Kansas transportation
geometry assessment, but registry presence is not direct collection of its
test module.

Therefore:

- direct hosted collection for all nine modules is `UNKNOWN`;
- required-check and branch-protection status are `UNKNOWN`;
- adjacent validator, schema, policy, or domain workflows must not be reported
  as full `tests/source` coverage unless their commands actually collect it;
- a documentation-only change can pass documentation workflows without
  exercising these source tests; and
- workflow or Makefile expansion is implementation work outside this
  documentation correction.

## Interpreting failures

| Failure area | Investigate first | Do not infer |
|---|---|---|
| Schema or fixture replay | Matching schema, fixture polarity, expected errors, and validator entrypoint | That an invalid fixture should be weakened or relabeled |
| Identity or digest drift | Canonical serialization, declared identity subject, payload bytes, `query_hash`, `spec_hash`, and snapshot/assessment ID | That an identity change is cosmetic |
| Finite outcome mismatch | Derivation rules, fixture expectation, finding codes, and required obligations | That `PASS`, `HOLD`, `ABSTAIN`, `DENY`, and `ERROR` are interchangeable |
| Source-role collapse | Declared source role, observed/modeled distinction, candidate state, activation hold, and authority flags | That retrieval, schema validity, or registry presence grants authority |
| Unsafe input | Duplicate keys, non-finite values, non-object roots, file size, symlinks, and value-safe diagnostics | That a parser or harness failure is an expected governed denial |
| Network or credential behavior | `KFM_NO_NETWORK` handling, imports, socket use, tokens, and CLI diagnostics | That an offline pass proves a live source is available or admissible |
| Summary rendering | Input validation, redaction, rollback target, escaping, output path, and blocking exit | That a review-ready summary records completed review |

Fix the owning implementation, schema, contract, fixture, or test expectation
only after reconciling which surface is wrong. Do not make documentation claims
true by weakening executable behavior.

## Safety and authority limits

- Use synthetic or explicitly approved public-safe fixtures.
- Do not commit credentials, private URLs, personal data, restricted records,
  culturally sensitive material, precise protected locations, or live
  retrieved payloads.
- Preserve rights, license, sensitivity, sovereignty, privacy, provenance,
  freshness, correction, withdrawal, and rollback fields when the tested
  object touches them.
- Keep diagnostics value-safe; finding codes and paths should not echo
  protected inputs.
- A successful retrieval candidate remains a candidate. A healthy probe
  remains an observation. A registry record remains a record. None becomes
  source truth, evidence closure, policy approval, or publication authority by
  test placement or workflow success.
- Lifecycle movement remains governed separately:
  `RAW -> WORK/QUARANTINE -> PROCESSED -> CATALOG/TRIPLET -> PUBLISHED`.

## Maintenance checklist

When this lane changes:

1. Update the module and source-defined test counts.
2. Link each new module to the implemented validator, schema, fixture, renderer,
   or compatibility surface it exercises.
3. Add positive, abstention/hold, denial, error, correction, and tamper cases
   appropriate to the object.
4. Keep reusable fixtures in the accepted fixture root and public-safe.
5. Verify deterministic identity, unsafe-input, non-echo, no-network, and
   credential boundaries where relevant.
6. Preserve explicit false authority effects for candidate, probe, retrieval,
   role, and health objects.
7. Update hosted commands and path filters in the same reviewed change when CI
   collection intentionally expands.
8. Report exact execution evidence rather than inferring coverage from paths,
   registries, workflow names, or prose.

## Open verification

| Question | Status |
|---|---|
| Who provides accountable source, rights, sensitivity, sovereignty, privacy, QA, security, and release review beyond CODEOWNERS routing? | `NEEDS VERIFICATION` |
| Are any of the nine direct modules collected by an indirect hosted command? | `UNKNOWN` |
| Should the lane receive a dedicated workflow or Make target? | `OPEN` |
| Is any current source-related workflow a required check? | `UNKNOWN` |
| Which adjacent schema, policy, validator, connector, pipeline, domain, and application tests form the complete source-governance matrix? | `UNKNOWN` |
| What evidence is required before live retrieval, source admission, activation, lifecycle movement, or public use? | `NEEDS VERIFICATION` |

## Rollback

This is a same-path documentation correction. Before merge, close the draft
pull request. After merge, revert the documentation commit. Neither action
changes schemas, fixtures, validators, tests, source records, registry state,
policy, lifecycle data, release state, deployment, promotion, or publication.

[Back to top](#top)

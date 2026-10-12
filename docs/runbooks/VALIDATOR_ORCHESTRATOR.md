<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks-validator-orchestrator
title: Validator Orchestrator Runbook
type: runbook
version: v1.4
status: draft
owners: ["@bartytime4life"]
created: 2026-08-08
updated: 2026-08-25
policy_label: internal
owning_root: docs/
responsibility: Operate the bounded registry-driven validator orchestrator without treating a validation result as evidence, policy, review, release, or publication authority.
truth_posture: CONFIRMED current command, registry contract, and historical schema-runner boundary on this branch; hosted CI remains NEEDS VERIFICATION until the pull-request checks complete.
related:
  - ../../tools/validate_all.py
  - ../../tools/validators/validate_all.py
  - ../../tools/validators/validator_registry.json
  - ../../tools/validators/_common/run_all.py
  - ../../tools/validators/catalog_closure/validate_catalog_closure.py
  - ../../tools/validators/validate_catalog_matrix_closure.py
  - ../../tools/validators/validate_catalog_matrix_claim_closure.py
  - ../../tools/validators/catalog_closure/validate_catalog_distribution_mapping_profile.py
  - ../../tools/validators/dependencies/pnpm_audit_readiness.py
  - ../../tools/validators/release/validate_release_manifest.py
  - ../../tools/validators/release/validate_release_proof_pack_closure.py
  - ../../tests/validators/test_validate_release_manifest.py
  - ../../tests/validators/test_validate_release_proof_pack_closure.py
  - ../../tests/validators/test_validator_orchestrator.py
  - ../../tests/validators/test_catalog_validator_registry_convergence.py
  - ../../tests/validators/test_pnpm_audit_readiness.py
  - ../../tests/validators/test_legacy_schema_runner_scope.py
  - ../doctrine/directory-rules.md
  - ../dashboards/observability/validator-orchestrator-health.md
notes:
  - "Directory Rules v2 DIR-EXEC-006 permits tools/validate_all.py as a thin repository entrypoint while implementation remains under tools/validators/."
  - "This runbook implements the bounded orchestrator direction associated with KFM-P5-PROG-0009 and the Pass 6 validator-report expansions."
  - "The orchestrator runs repository-owned validators without a shell, forces no-network test posture, and emits finite machine-readable outcomes."
  - "Catalog closure registration coordinates four existing fixture-only validators; it does not accept ADR-0022 or create catalog, evidence, review, release, promotion, publication, or public-use authority."
  - "ReleaseManifest and ReleaseProofPackClosure registration coordinates existing fixture-only release-support validators in release-dry-run and full; PASS remains non-authoritative."
  - "The historical make schemas compatibility runner explicitly selects the nine reviewed schema fixture families; canonical full remains broader and retains catalog, release-support, and repository guardrail validators."
  - "The deterministic pnpm readiness checker is registered in full and changed-area selection; the separate advisory query remains owned by dependency-scan."
  - "A green orchestrator report proves only the selected checks completed successfully for the declared profile."
[/KFM_META_BLOCK_V2] -->

# Validator Orchestrator Runbook

`tools/validate_all.py` is the canonical thin entrypoint. The implementation and executable registry live under `tools/validators/`, consistent with Directory Rules v2 `DIR-EXEC-006`.

> [!IMPORTANT]
> The orchestrator is a checker coordinator. It does not resolve evidence, evaluate policy, authenticate review, approve promotion, assemble a release, publish data, or certify that every repository invariant is covered.

## Commands

Validate the registry without running child validators:

```bash
python tools/validate_all.py --validate-registry
```

List profiles and registered validator IDs:

```bash
python tools/validate_all.py --list
```

Run the complete bounded registry:

```bash
python tools/validate_all.py --profile full
```

Run the smaller trust-spine profile:

```bash
python tools/validate_all.py --profile focused
```

Run the release-adjacent fixture profile:

```bash
python tools/validate_all.py --profile release-dry-run
```

Select validators from changed repository paths:

```bash
python tools/validate_all.py \
  --profile changed-area \
  --changed-path contracts/runtime/decision_envelope.md \
  --changed-path schemas/contracts/v1/runtime/decision_envelope.schema.json
```

The direct changed-area profile preserves an empty-selection `ABSTAIN` by
default. Add `--require-match` when the caller is a gate and must fail if no
registered validator is selected:

```bash
python tools/validate_all.py \
  --profile changed-area \
  --changed-path contracts/runtime/decision_envelope.md \
  --require-match
```

Select exact registered IDs:

```bash
python tools/validate_all.py \
  --profile focused \
  --validator evidence-bundle \
  --validator decision-envelope
```

Write the deterministic report to a file:

```bash
python tools/validate_all.py \
  --profile full \
  --output artifacts/qa/validator-orchestrator.json \
  --quiet
```

Timing is excluded by default so identical validator outputs yield identical reports. Add timing only for operational inspection:

```bash
python tools/validate_all.py --profile full --include-timing
```

## Profiles

| Profile | Selection law | Empty selection |
|---|---|---|
| `focused` | Small trust-spine subset declared in the registry. | Configuration error. |
| `changed-area` | Every validator whose registered path glob matches at least one supplied changed path. | Defaults to `ABSTAIN` with `NO_MATCHING_VALIDATORS`, exit `0`; `--require-match` changes an empty selection to `FAIL`, exit `1`. |
| `release-dry-run` | Release-adjacent evidence, decision, receipt, bounded catalog-closure, ReleaseManifest, and release proof-pack closure fixture validators. | Configuration error. |
| `full` | Every registered validator exactly once, in registry order. | Configuration error. |

The `full` profile means every validator in `validator_registry.json`; it does not claim every executable checker in the repository has been registered.

### Registered dependency-readiness validator

`pnpm-dependency-readiness` registers the existing no-network repository
preflight in `full` and changed-area selection. It checks the exact pnpm and
Node declarations, workspace agreement, lockfile format and importer closure,
and absence of competing root lockfiles. Its path globs cover the dependency
workflow, root and workspace manifests, accepted lockfiles, competing
lockfiles, validator implementation, and focused tests.

This registration does not execute `pnpm audit`, query an advisory service,
admit a dependency, or establish vulnerability absence, provenance,
compatibility, release readiness, deployment approval, or publication
authority. The network-dependent, point-in-time audit remains in
`.github/workflows/dependency-scan.yml`.

### Registered catalog-closure validators

The following existing, fixture-only validators are registered in `release-dry-run` and `full`. They are intentionally not added to `focused`, which remains the smaller trust-spine subset.

| Validator ID | Bounded check | Non-effect of `PASS` |
|---|---|---|
| `catalog-closure-packet` | CatalogClosurePacket shape and internal STAC/DCAT/PROV readiness relationships. | Does not emit catalog records or authorize release. |
| `catalog-matrix-closure` | CatalogMatrix identity, digest, release-reference, reference-hygiene, and decision alignment. | Does not accept ADR-0022 or create evidence, review, or publication authority. |
| `catalog-matrix-claim-closure` | ClaimEnvelope-to-CatalogMatrix non-overstatement across evidence, source, policy, review, release, correction, rollback, and publication projection. | Does not resolve evidence, decide policy, approve review, promote, or publish. |
| `catalog-distribution-mapping-profile` | STAC/DCAT/PROV carrier mapping and deterministic candidate identity. | Does not write catalogs, activate OCI/ORAS, or authorize public use. |

Their path globs cover the existing contracts, schemas, fixtures, validators, focused tests, workflows, and source-reconciliation note that define each bounded profile. Generated authoring receipts remain outside this registration slice; receipt-integrity findings are not silently repaired or converted into catalog-validator outcomes.

### Registered release-support validators

`release-manifest` and `release-proof-pack-closure` are existing fixture-only validators registered in `release-dry-run` and `full`, not `focused`. Registration coordinates already-defined bounded checks; it does not create a release object or change release semantics.

| Validator ID | Bounded check | Non-effect of `PASS` |
|---|---|---|
| `release-manifest` | Local ReleaseManifest schema shape, deterministic identity, reference hygiene, lifecycle/release coherence, artifact metadata, rights/sensitivity posture, time ordering, and constant-false authority fields. | Does not resolve references, verify artifact bytes or signatures, execute policy, authenticate review, persist a release, promote lifecycle state, publish, or permit public use. |
| `release-proof-pack-closure` | Synthetic ReleaseProofPackClosure completeness across release-manifest, receipt, proof, catalog, review, correction, and rollback references while requiring all authority/mutation flags to remain false. | Does not validate referenced truth, approve promotion, create a release, mutate lifecycle state, publish, or authorize public use. |

The ReleaseProofPackClosure changed-area globs cover its existing contract, schema, fixtures, validator, focused test, dedicated workflow, source-reconciliation note, and this runbook. The profile is intentionally a structural closure check over synthetic references; a green result is not evidence that those references are authentic or approved.

## Finite outcomes and process exit codes

| Outcome | Exit | Meaning |
|---|---:|---|
| `PASS` | `0` | Every selected child validator exited `0`. |
| `ABSTAIN` | `0` | The `changed-area` profile matched no registered validator. No pass claim is made. |
| `FAIL` | `1` | The orchestrator completed with a child rejection, or a required changed-area selection matched nothing. |
| `ERROR` | `2` | Registry, path, I/O, timeout, or child-system failure occurred; or a child exited outside `0`/`1`. |

Downstream callers must preserve the distinction between exit `1` and exit `2`. An arbitrary nonzero exit is not proof of a reviewed validation rejection.

## Report contract

The default JSON report includes:

- registry identity and SHA-256 digest;
- named profile and selection mode;
- normalized changed paths or explicit validator IDs;
- aggregate finite outcome and reason code;
- registered and selected counts;
- one stable result per selected validator;
- child return code;
- SHA-256 digests and line counts for captured stdout/stderr;
- declared artifact references, when the registry supplies them;
- no timestamp and no duration unless `--include-timing` is requested.

Raw child output is not copied into the JSON report. `--verbose` prints bounded captured output to stderr for a local operator and should not be enabled on a public surface.

## Registry maintenance

`tools/validators/validator_registry.json` is executable selection metadata, not policy or release authority. For each new entry:

1. use a stable lowercase validator ID;
2. point only to a repository-relative Python file under `tools/validators/`;
3. use bounded arguments and timeout;
4. register nonempty path globs for changed-area selection;
5. add the ID to one or more named profiles;
6. keep `profiles.full` equal to the complete validator list, in the same order;
7. add focused positive and negative orchestrator tests when registry semantics change;
8. verify the child validator already has its own fixtures, tests, and authority boundary.

Do not register placeholder validators that intentionally raise `NotImplementedError`.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validator_orchestrator.py' \
  --verbose

python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_catalog_validator_registry_convergence.py' \
  --verbose

python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_legacy_schema_runner_scope.py' \
  --verbose

python -m pytest tests/validators/test_pnpm_audit_readiness.py -q
python -m unittest tests.validators.test_validate_release_manifest --verbose
python -m unittest tests.validators.test_validate_release_proof_pack_closure --verbose
python tools/validate_all.py --validate-registry
python tools/validate_all.py --profile release-dry-run --validator release-manifest
python tools/validate_all.py --profile release-dry-run --validator release-proof-pack-closure
python tools/validate_all.py --profile release-dry-run
python tools/validate_all.py --profile full
```

### Historical `make schemas` compatibility boundary

The existing compatibility surface remains available:

```bash
python tools/validators/_common/run_all.py
```

That command is the implementation behind `make schemas`. It uses the canonical orchestrator engine but explicitly requests the nine reviewed legacy schema-fixture validator IDs represented by `RUNNER_VALIDATORS`. It does **not** run catalog-closure validators, release-support validators, `workflow-security`, or `repository-topology` merely because those checks belong to the broader canonical `full` profile.

This separation is intentional:

- `make schemas` and `schema-validation` retain their historical schema/fixture responsibility;
- `python tools/validate_all.py --profile full` remains the complete registered aggregate and includes catalog closure, release-support validation, and repository guardrails;
- `make repository-guardrails` remains the dedicated workflow-security and repository-topology enforcement surface.

New callers should use `tools/validate_all.py` and choose the profile or explicit validators appropriate to their responsibility. Do not use `make schemas` as an alias for the complete validator registry.

## Failure handling

- Registry parse, duplicate key, nonfinite number, path escape, missing script, symlink, profile drift, or unsafe output path: exit `2`.
- Child timeout: child result `ERROR`, aggregate exit `2`.
- Child exit `1`: child result `FAIL`, aggregate exit `1` unless another child errors.
- Child exit `2` or any other code: child result `ERROR`, aggregate exit `2`.
- Changed-area no match: `ABSTAIN`, exit `0`, by default with no false all-pass statement; `--require-match` returns `FAIL`, exit `1`.

## Rollback

To remove only ReleaseProofPackClosure orchestration, revert its registry entry/profile memberships, the focused registry regression, and this runbook delta. The existing ReleaseProofPackClosure contract, schema, fixtures, validator, workflow, source map, release objects, and published artifacts are not changed by that rollback.

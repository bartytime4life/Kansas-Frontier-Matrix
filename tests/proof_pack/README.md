<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://tests/proof-pack/readme
title: tests/proof_pack/ — ProofPack Test Lane
type: README
version: v0.1.0
status: draft; repository-grounded; executable; bounded; no-network-oriented; non-authoritative
owner: "@bartytime4life — CONFIRMED CODEOWNERS review route; independent proof, QA, and release stewardship remain UNKNOWN"
created: 2026-08-30
updated: 2026-08-30
owning_root: tests/
policy_label: public; tests; proof-pack; deterministic; local-only; fail-closed; no-release-authority; non-publisher
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: e282b375a9f3881afdc30172c68f191cccde4220
  direct_modules: 2
  source_defined_tests: 12
truth_posture: CONFIRMED two focused test modules, one candidate fixture, two valid fixtures, eight invalid fixtures, and one dedicated workflow / PROPOSED release-support ProofPack semantics / UNKNOWN required-check status, production writers and consumers, canonical proof admission, authenticated review, signatures, retention, correction propagation, and operational rollback
notes:
  - "This human-maintained index documents executable test evidence; it is not a generated ProofPack, receipt, proof, release record, or publication surface."
  - "Passing tests establish only the checked local profile at the tested revision."
[/KFM_META_BLOCK_V2] -->

# ProofPack test lane

`tests/proof_pack/` verifies the deterministic assembler and checker for the
proposed `kfm.proof-pack.release-support.v1` profile. It tests local manifest
closure and failure behavior; it does not create proof, approve release, or
authorize publication.

> [!IMPORTANT]
> A passing ProofPack check means that the tested manifest satisfies the
> proposed schema, required-family, cross-binding, path, and digest rules. It
> does not authenticate evidence, policy, review, signatures, release state,
> deployment, or publication.

## Inventory

| Module | Tests | Implemented coverage |
|---|---:|---|
| [`test_assemble_proof_pack.py`](./test_assemble_proof_pack.py) | 4 | Golden-manifest equality, repeatability, explicit-output CLI behavior, and overwrite refusal |
| [`test_proof_pack_check.py`](./test_proof_pack_check.py) | 8 | Valid and corrected manifests, fixture polarity, required families, semantic findings, self-authority denial, socket denial, and closed Draft 2020-12 shape |
| **Total** | **12** | Source-defined test functions at the pinned evidence revision |

The implementation lives under [`tools/proof_pack/`](../../tools/proof_pack/README.md):

- [`assemble_proof_pack.py`](../../tools/proof_pack/assemble_proof_pack.py)
  builds a candidate at an explicit output path;
- [`proof_pack_check.py`](../../tools/proof_pack/proof_pack_check.py) checks
  schema, semantic bindings, local paths, and digests;
- [`_common.py`](../../tools/proof_pack/_common.py) supplies bounded JSON,
  path, symlink, size, and SHA-256 helpers.

## Authority and placement

Accepted [Directory Rules](../../docs/doctrine/directory-rules.md) place
executable conformance evidence under `tests/`. The surrounding responsibilities
remain separate:

| Responsibility | Repository authority | Test-lane role |
|---|---|---|
| Profile meaning | [`contracts/evidence/proof_pack.md`](../../contracts/evidence/proof_pack.md) | Exercise the proposed semantics; do not accept or redefine them |
| Machine shape | [`proof_pack.schema.json`](../../schemas/contracts/v1/evidence/proof_pack.schema.json) | Assert schema closure and selected references |
| Reusable synthetic examples | [`fixtures/contracts/v1/evidence/proof_pack/`](../../fixtures/contracts/v1/evidence/proof_pack/) | Replay candidate, valid, and invalid cases |
| Builder and checker | [`tools/proof_pack/`](../../tools/proof_pack/README.md) | Test deterministic implementation and CLI behavior |
| Canonical proof records | [`data/proofs/proof_pack/`](../../data/proofs/proof_pack/README.md) | No admission or write authority |
| Policy and release decisions | [`policy/proof/`](../../policy/proof/README.md) and [`release/`](../../release/README.md) | No decision, approval, signature, or promotion authority |
| Hosted orchestration | [`proof-pack-closure.yml`](../../.github/workflows/proof-pack-closure.yml) | Run bounded checks and report their result |

[`CODEOWNERS`](../../.github/CODEOWNERS) routes `tests/` review to
`@bartytime4life`. That route does not prove stewardship, independent review,
approval, or separation of duties.

## Fixtures and expected polarity

The focused checker command expects this exact synthetic inventory:

| Fixture class | Count | Purpose |
|---|---:|---|
| Candidate | 1 | Explicit assembler input for the release-support profile |
| Valid | 2 | Current and corrected release-support manifests |
| Invalid | 8 | Seven semantic negatives plus one schema-level self-authority denial |

The checker requires 11 component families: `EVIDENCE_BUNDLE`,
`VALIDATION_REPORT`, `INTEGRITY_MANIFEST`, `PROV_EXPORT`, `LINEAGE_INDEX`,
`PROMOTION_DECISION`, `RUNTIME_PROOF`, `CITATION_SAMPLE`, `CI_RUN`,
`RELEASE_ANCHOR`, and `ROLLBACK_REFERENCE`. `CORRECTION_HISTORY` is additionally
required when correction state is not `NONE`.

These files are synthetic review carriers. They do not establish that their
referenced evidence is true, rights are resolved, policy permits exposure, or a
release exists.

## Run locally

From the repository root, install the declared project-test dependencies and run
the complete focused lane:

```bash
python tools/ci/install_python_ci.py project-test
python -m pytest -q tests/proof_pack
```

Replay fixture polarity and local reference closure directly:

```bash
python tools/proof_pack/proof_pack_check.py --fixtures
```

Rebuild and compare the golden manifest without writing to a governed data lane:

```bash
tmp_file="$(mktemp)"
rm "$tmp_file"
python tools/proof_pack/assemble_proof_pack.py \
  --candidate fixtures/contracts/v1/evidence/proof_pack/candidates/release_support_candidate.json \
  --repo-root . \
  --output "$tmp_file"
cmp "$tmp_file" \
  fixtures/contracts/v1/evidence/proof_pack/valid/valid_release_support.json
rm "$tmp_file"
```

The assembler refuses an existing output unless the caller explicitly supplies
`--force`. Never point an exploratory run at `data/proofs/`, `release/`, or a
published-carrier path.

## Hosted workflow

[`proof-pack-closure.yml`](../../.github/workflows/proof-pack-closure.yml) uses
Python 3.11, read-only repository permissions, deterministic environment
settings, and `KFM_NO_NETWORK=1`. It runs:

1. exact fixture polarity and local reference closure;
2. all 12 tests in this lane;
3. the shared schema harness filtered to ProofPack;
4. deterministic golden-manifest reconstruction under `/tmp`; and
5. the current workflow-binding receipt check.

The workflow path filters include `tests/proof_pack/**`, so changes to this
README trigger the focused job. The receipt binds the workflow file only; this
README is not an immutable receipt artifact.

The checker suite explicitly replaces `socket.socket` with a denial stub for a
valid manifest. The implementation reads only repository-local inputs, but that
single regression is not proof of universal network isolation for every Python
dependency or hosted runner action.

## Result interpretation

| Result | Maintainer response |
|---|---|
| Golden comparison or determinism failure | Inspect input bytes, ordering, serialization, and implementation changes before updating expected output |
| Fixture-polarity failure | Preserve the failing fixture and finding code; correct the fixture, schema, contract, or checker at its owning surface |
| Required-family or cross-binding failure | Keep the candidate held; do not omit support or weaken the rule to obtain a pass |
| Path, symlink, file, size, or digest failure | Investigate provenance and referenced bytes; never rewrite a digest merely to match an unexplained file |
| Schema closure failure | Reconcile the semantic contract and schema before changing tests |
| Receipt failure | Distinguish workflow-byte drift from ProofPack behavior; do not regenerate lineage casually |
| Dependency or runner failure | Classify separately from a ProofPack assertion failure and retain the exact revision and logs |

`--no-reference-check` intentionally bypasses file and digest verification for
bounded diagnosis. A result produced with that flag is not local-reference
closure and must not be reported as such.

## Safety and non-effects

- Tests and fixtures are public-repository material; do not substitute
  restricted, private, personal, culturally sensitive, or harmful-precision
  payloads.
- The suite does not fetch sources or write lifecycle state.
- SHA-256 agreement proves only byte agreement with declared digests, not source
  identity, truth, consent, rights, currency, completeness, or audience fitness.
- Workflow success does not authenticate a reviewer or signature.
- Generated candidates and diagnostics are not receipts, admitted proofs,
  release decisions, deployments, or published artifacts.
- Public clients must use governed released interfaces rather than this internal
  test or proof lane.

## Maintenance

Update this README when a direct test module, fixture polarity, required component
family, CLI, size or path guard, schema binding, workflow command, receipt check,
or authority boundary changes. Keep source-defined counts synchronized with the
two test modules and preserve links to the implementation owner.

For a failed documentation change, close the unmerged pull request or revert its
commit. Do not delete tests, fixtures, tooling, contracts, schemas, receipts,
proofs, release records, or published material to make this README agree with an
unsupported claim.

## Known gaps

- Required-check and branch-protection status are **UNKNOWN**.
- The release-support profile remains **PROPOSED** rather than accepted doctrine.
- Production writers, consumers, and any governed canonical-admission path are
  **UNKNOWN**.
- Authenticated review, signature verification, retention, correction
  propagation, withdrawal, cache invalidation, and operational rollback are not
  established by this lane.
- Independent proof, QA, policy, release, and security stewardship remains
  **NEEDS VERIFICATION**.
- Complete repository-wide ProofPack coverage is not established by these 12
  tests.

See the [test-root contract](../README.md),
[`ADR-0011`](../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md),
and the [tooling README](../../tools/proof_pack/README.md) for the surrounding
responsibility boundaries.

# AI Evaluator Harness Contract

Status: **CONFIRMED repository implementation slice / PROPOSED production capability** · execution posture: **fixture-only / no-network**.

This contract defines the bounded evaluator record used to check candidate artifacts before human review. It evaluates candidate artifacts; it does **not** promote, release, publish, approve, or convert model output into evidence.

The public-safe profiles extend the existing generic evaluator family. They do not create a second evaluation authority, call a model, fetch sources, or replace evidence, policy, review, release, correction, or rollback controls.

## Current implementation snapshot

The following surfaces are present in the current repository and are the implementation evidence for this contract:

| Responsibility | Current path | What it establishes |
|---|---|---|
| Semantic contract | `contracts/ai/evaluator_harness/README.md` | Candidate-evaluation meaning and boundaries. |
| Machine shape | `schemas/contracts/v1/ai/evaluator_harness.schema.json` | JSON Schema Draft 2020-12 record shape and finite enums. |
| Synthetic cases | `fixtures/contracts/v1/ai/evaluator_harness/cases.json` | 13 replayable positive and negative cases. |
| Enforcement | `tools/validators/ai/validate_ai_evaluator_harness.py` | Deterministic, fail-closed evaluation and profile derivation. |
| Focused tests | `tests/validators/test_validate_ai_evaluator_harness.py` | Schema, replay, policy, network, profile, and hash assertions. |
| CI gate | `.github/workflows/ai-evaluator-harness.yml` | No-network focused validation and generated-receipt integrity checks. |
| Authoring receipt | `data/receipts/generated/genrec-pass12-ai-evaluator-public-safe-profile-20260809.json` | Artifact hashes and provenance for the evaluator slice. |
| Source maps | `docs/intake/exploratory/pass9-ai-evaluator-harness-source-map.md` and `docs/intake/exploratory/pass12-ai-evaluator-public-safe-profile-source-map.md` | Design lineage only; not runtime or publication authority. |

The presence of these files confirms the repository slice. It does not establish a model-serving path, EvidenceBundle resolution, policy-engine execution, human approval, release state, or public-use authorization.

## Required record semantics

An evaluation record identifies the candidate, artifact family, evidence references, deterministic metric checks, policy outcome, and finite evaluator result.

The schema requires:

- `evaluation_id`, `artifact_kind`, and `candidate_ref` for identity;
- a non-empty `evidence_refs` collection and explicit `metrics`;
- `policy_outcome` in `ALLOW`, `DENY`, `HOLD`, or `ERROR`;
- `deterministic=true` and `network_access=false` for an admissible fixture evaluation;
- `result` in `PASS`, `FAIL`, or `ERROR`;
- explicit `reason_codes` and a `sha256:` `spec_hash`.

Generic records use `GENERIC_DECLARED_METRICS` semantics. Optional profile records additionally provide `profile_input` and a deterministic `profile_spec_hash` bound to the profile, profile input, candidate reference, and evidence references.

## Finite evaluator behavior

The validator is fail-closed and returns only bounded outcomes:

- `PASS` requires deterministic execution, no network access, `policy_outcome=ALLOW`, evidence references, and every declared metric threshold to pass.
- A deterministic threshold miss returns `FAIL`; it remains a reviewable candidate outcome and never becomes publication authority.
- `ERROR` records an evaluator, schema, or explicit policy error. It must not fall back to `PASS`.
- `HOLD` or `DENY` policy outcomes cannot produce `PASS`.
- A non-deterministic or network-enabled record returns `DENY`, even when the schema would also reject it.
- Missing evidence or metrics, a derived-profile mismatch, or inconsistent declared results returns `DENY`.
- Generic declared metrics use explicit `{name,value,threshold,comparison}` records; no hidden composite score is authoritative.

The evaluator intentionally stops before human review and before every KFM promotion gate.

## Public-safe profiles

`PUBLIC_SAFE_RASTER_V1` and `PUBLIC_SAFE_TEXT_V1` derive declared metrics from bounded synthetic inputs and require exact parity between the derived values and the evaluator record.

- Raster derivation computes comparable-cell `coverage`, `rmse`, and `max_abs_error`. Shape mismatch is `DENY`/`FAIL`; insufficient coverage is `HOLD`/`FAIL`; threshold failures are `ALLOW`/`FAIL`.
- Text derivation computes `citation_coverage`, `unsupported_claims`, `sensitive_hits`, and `character_count`. An empty citation registry is `HOLD`/`FAIL`; unsupported, under-cited, or overlong output is `ALLOW`/`FAIL`; declared sensitive-term exposure is `DENY`/`FAIL`.
- `profile_spec_hash` binds the profile specification to the candidate and evidence references, so a record cannot silently substitute different inputs.

These profiles do not resolve an `EvidenceBundle`, execute policy, authenticate review, call a model, open binary artifacts, or fetch sources. Their outputs are evaluation evidence subordinate to evidence, policy, review, release, correction, and rollback state.

## Directory Rules basis

Per accepted ADR-0029 / Directory Rules v2, semantic meaning lives under `contracts/`, machine shape under `schemas/`, synthetic examples under `fixtures/`, enforcement under `tools/validators/`, tests under `tests/`, CI under `.github/workflows/`, and authoring accountability under `data/receipts/generated/`. No new responsibility root or parallel evaluator authority is introduced.

The KFM AI Build Operating Contract v3.0 in Google Drive is corroborating doctrine for the evidence-first, trust-membrane, and publication-separation boundaries above. It is not the source of repository paths, schema fields, workflow behavior, or production readiness; those claims are established by the GitHub surfaces in the implementation snapshot.

## Validation

Focused local checks:

```bash
python -m unittest tests.validators.test_validate_ai_evaluator_harness -v
python tools/validators/ai/validate_ai_evaluator_harness.py --fixtures
```

The CI workflow additionally installs the `project-test` dependency profile, compiles the validator and test module, and validates the generated receipt:

```bash
python tools/ci/install_python_ci.py project-test
python -m py_compile tools/validators/ai/validate_ai_evaluator_harness.py tests/validators/test_validate_ai_evaluator_harness.py
python tools/validators/validate_generated_receipt.py data/receipts/generated/genrec-pass12-ai-evaluator-public-safe-profile-20260809.json --repo-root .
```

CI sets `KFM_NO_NETWORK=1` and records the trust boundary in the job summary. A successful run proves the fixture/evaluator slice only; it does not authorize promotion, release, publication, or public use.

## Receipt maintenance

The generated receipt listed above binds this README and its companion artifacts by SHA-256. Any future README change must update the README entry in `artifact_hashes` in the same bounded change, or replace the receipt and workflow reference with a successor receipt. Do not treat a stale receipt as current evidence.

## Rollback

Revert the README and its corresponding generated-receipt hash update together. No source, model, policy, release, route, or public state is mutated by this documentation-and-receipt change.

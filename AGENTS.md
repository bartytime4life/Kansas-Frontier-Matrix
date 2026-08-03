# AGENTS.md — AI Agent Operating Guide for Kansas Frontier Matrix

> Read this file completely before making any change. Then read the path-scoped README for every root you will touch.

This file tells AI coding agents how to orient, operate, and stay within the trust boundaries of the Kansas Frontier Matrix (KFM) repository. It does not replace the governing doctrine; it links to it.

## Repository in one paragraph

KFM is a governed, evidence-first, map-first, time-aware spatial knowledge system for Kansas and the surrounding frontier. A file's **location** identifies its responsibility, authority, lifecycle, and review boundary. Changes must preserve the governed lifecycle, the cite-or-abstain evidence posture, and the public trust membrane. No merge, CI pass, or AI output is a data-publication event.

## Quick-start: setup and validation

```bash
# Python environment (Python 3.11+ required)
python -m venv .venv
. .venv/bin/activate
python -m pip install -e ".[test]"

# Run the full baseline — schemas and contract tests
make validate

# Check whitespace and line-ending hygiene
git diff --check
```

`make validate` runs two steps:

| Step | Command |
|---|---|
| `make schemas` | `python tools/validators/_common/run_all.py` |
| `make test` | `python -m pytest tests/schemas tests/contracts -q` |

Run narrower targets when your change touches a specific surface:

| Target | When to run |
|---|---|
| `make governed-api-smoke` | Any change to `apps/governed-api/` |
| `make governed-api-verify` | Governed API + import-boundary check |
| `make boundary-guards` | Policy, API, connector, or pipeline boundary |
| `make deny-test` | Public-route or runtime-import guard |
| `make ui-build` | Any change to `apps/explorer-web/` |
| `make maplibre-govern` | MapLibre performance governance |
| `make publish-check` | Promotion-gate or review-record changes |
| `make evidence-resolver` | Evidence-resolver package changes |

> **Readiness markers** (`make policy`, `make fixtures`, `make proof-slice`, `make catalog`, `make release-dry-run`) print `TODO` and exit 0. A zero exit is **not** validation evidence. Do not cite them as proof.
>
> Root JavaScript `lint`, `test`, and `build` scripts intentionally fail with `WORKFLOW_HOLD`. Do not run them.

## Branches, commits, and pull requests

- **Branch naming**: `agent/<short-description>` for every agent-created branch.
- **Scope**: one bounded purpose per branch. Do not bundle unrelated cleanup or migration.
- **Commits**: stage only intended files; write a terse descriptive message; never include credentials, private keys, or restricted payloads.
- **Pull requests**: use `.github/PULL_REQUEST_TEMPLATE.md` in full. Mark sections `Not applicable — <reason>` instead of deleting them.
- **Draft by default**: open draft pull requests for AI-authored, governance-significant, or not-yet-fully-validated work. Do not self-approve, merge, enable auto-merge, or mark ready without explicit authorization.

## Responsibility roots — where things go

| Primary responsibility | Owning root |
|---|---|
| Explain something to humans | `docs/` |
| Define an object's semantic meaning and invariants | `contracts/` |
| Define machine-checkable shape | `schemas/` |
| Decide allow, deny, restrict, hold, or abstain | `policy/` |
| Prove behavior is enforceable | `tests/` |
| Store deterministic valid, invalid, or denied examples | `fixtures/` |
| Provide repo-wide validators, generators, builders | `tools/` |
| Provide small operational helpers | `scripts/` |
| Implement a deployable application | `apps/` |
| Implement a shared library | `packages/` |
| Fetch from or admit a named external source | `connectors/` |
| Execute pipeline logic | `pipelines/` |
| Declare pipeline configuration | `pipeline_specs/` |
| Store lifecycle data, receipts, proofs, catalogs | correct phase under `data/` |
| Record release decisions, corrections, rollback | `release/` |
| Provide local runtime adapters | `runtime/` |
| Define deployment or exposure posture | `infra/` |
| Store non-secret configuration defaults | `configs/` |
| Migrate schema or canonical representation | `migrations/` |
| Demonstrate runnable patterns | `examples/` |
| Machine governance projections and indexes | `control_plane/` |

**Do not** create a new root directory, revive `catalog/` (frozen), treat `src/` as a writable authority, or place domain material at the repository root. Every new or moved path requires a [Directory Rules](docs/doctrine/directory-rules.md) basis stated in the pull-request description.

## Core invariants — never break these

1. **Lifecycle is governed.** `RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLETS → PUBLISHED`. Promotion is a governed state transition, not a file move.
2. **Claims resolve evidence.** An `EvidenceRef` must resolve to an `EvidenceBundle` before a consequential claim is authoritative.
3. **Public access crosses a trust membrane.** Ordinary clients use governed APIs and released public-safe artifacts only.
4. **Interpretive surfaces are subordinate.** AI, maps, tiles, graphs, summaries, and tests are not truth authorities.
5. **Automation does not publish.** Watchers and CI may emit candidates and records; they must not promote or publish.
6. **Object families stay distinct.** Receipts, proofs, catalogs, releases, and corrections have separate responsibilities.
7. **Sensitive material fails closed.** Unknown rights, living-person data, rare-species locations, archaeology, infrastructure, or cultural concerns require quarantine, redaction, or denial.
8. **Corrections are traceable.** Identity, replay, supersession, and rollback are preserved where consequences require them.

## Truth labels — use these for material claims

| Label | Meaning |
|---|---|
| `CONFIRMED` | Verified from repository files, tests, logs, or accepted decisions |
| `PROPOSED` | A design, path, or inference not yet verified in implementation |
| `UNKNOWN` | Not established strongly enough to act as fact |
| `NEEDS VERIFICATION` | Checkable, but not yet checked |

Cite exact repository paths and immutable commits for repository-state claims. A filename in a plan does not prove the file exists. A passing CI check does not prove evidence closure, release approval, or publication.

## AI-authored artifacts — receipt required

For any artifact you author or substantively modify with AI assistance:

1. Follow [`docs/doctrine/ai-build-operating-contract.md`](docs/doctrine/ai-build-operating-contract.md).
2. Create a generated-work receipt at `data/receipts/generated/<receipt>.json`.
3. Validate the receipt: `make schemas` (the generated_receipt schema is under `schemas/contracts/v1/receipts/`).
4. Record model identity, prompt or contract hash, pinned evidence references, truth labels, checks run, and checks skipped.
5. Set `human_review.state` to `pending` until an authorized reviewer acts.
6. Do not store prompts, private chain-of-thought, credentials, or sensitive payloads in the receipt.
7. Do not represent the receipt as proof, policy permission, release approval, or publication authority.

## Security and sensitive material

- Never place credentials, restricted payloads, private-person records, DNA/genomic data, exact sensitive locations, or critical-infrastructure vulnerability details in issues, pull requests, logs, fixtures, or receipts.
- Unknown rights or sensitivity → quarantine, redact, generalize, delay, abstain, or deny. **Fail closed.**
- Vulnerability reports follow [`SECURITY.md`](SECURITY.md) private-first, not public issues.

## Key doctrine references

| Document | Role |
|---|---|
| [`docs/doctrine/directory-rules.md`](docs/doctrine/directory-rules.md) | Canonical placement and responsibility authority |
| [`docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md`](docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Accepted adoption decision |
| [`docs/doctrine/ai-build-operating-contract.md`](docs/doctrine/ai-build-operating-contract.md) | AI-authored change and receipt discipline |
| [`docs/doctrine/lifecycle-law.md`](docs/doctrine/lifecycle-law.md) | Lifecycle and promotion boundary |
| [`docs/doctrine/trust-membrane.md`](docs/doctrine/trust-membrane.md) | Public and internal trust boundary |
| [`docs/doctrine/truth-posture.md`](docs/doctrine/truth-posture.md) | Evidence labels and cite-or-abstain behavior |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Full contribution, validation, review, and receipt workflow |
| [`docs/registers/DRIFT_REGISTER.md`](docs/registers/DRIFT_REGISTER.md) | Known repository/doctrine conflicts |

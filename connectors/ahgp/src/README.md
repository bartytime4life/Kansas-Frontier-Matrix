<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-ahgp-src-readme
title: connectors/ahgp/src/ — AHGP Connector Source Tree
type: readme; directory-readme; implementation-source-root
version: v0.1
status: draft; repository-grounded; implementation-placeholder; activation-unknown
owners: OWNER_TBD — Connector steward · Source steward · People/Genealogy steward · Validation steward · Docs steward
created: 2026-07-16
updated: 2026-07-16
policy_label: public; implementation-bearing; source-admission-only; no-network-on-import; raw-or-quarantine
owning_root: connectors/
current_path: connectors/ahgp/src/README.md
base_ref: main
base_commit: 975291ccc1342f323bb23ce723e7f5e4b1f44ddc
related:
  - ../README.md
  - ../pyproject.toml
  - ./ahgp/README.md
  - ../tests/README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0017-source-descriptor-admission-process.md
  - ../../../tools/validators/connector_gate/README.md
  - ../../../tests/policy/test_pipeline_connector_non_publisher.py
  - ../../../.github/CODEOWNERS
  - ../../../.github/workflows/connector-gate.yml
  - ../../../.github/workflows/policy-boundary-guards.yml
tags: [kfm, connectors, ahgp, python, source-tree, placeholder, import-safe, no-network, raw, quarantine, governance]
notes:
  - "Repository snapshot is bounded to main@975291ccc1342f323bb23ce723e7f5e4b1f44ddc."
  - "The child package currently contains an empty __init__.py, comment-only admit.py and fetch.py placeholders, a descriptor.yaml placeholder, and a package README."
  - "The pyproject declares kfm-connector-ahgp version 0.0.0 only; build backend, dependencies, package discovery, installation, activation, and runtime behavior are not established."
  - "This README documents the source-tree boundary; it does not activate AHGP, implement a fetch, admit a record, or claim validation results."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# AHGP connector source tree

`connectors/ahgp/src/`

## Purpose

This folder is the Python source-tree container for AHGP connector implementation support. Code below it may support explicitly invoked, descriptor-gated source intake, but it must remain import-safe and may hand source material only to governed **RAW** or **QUARANTINE** destinations.

This folder does not establish genealogy truth, source activation, rights or sensitivity policy, evidence closure, release approval, or publication authority.

## Authority level

**Implementation-bearing**, with the current implementation at **placeholder** maturity.

The authority split is:

| Surface | Authority |
|---|---|
| `connectors/ahgp/src/` | Container for source-specific Python implementation. |
| [`ahgp/`](./ahgp/README.md) | Child package boundary and package-level implementation guidance. |
| [`../README.md`](../README.md) | AHGP connector-lane scope and source-admission boundary. |
| [`../pyproject.toml`](../pyproject.toml) | Current project name and version declaration only. |
| Source descriptors and activation records | Governed registry/control-plane homes outside this tree. |
| Contracts and schemas | Their canonical `contracts/` and `schemas/` roots. |
| Rights, sensitivity, and release decisions | Their owning `policy/` and `release/` roots. |

This README is descriptive. It cannot make the child descriptor authoritative, activate a source, or upgrade placeholder code to operational status.

## Status

**CONFIRMED path and bounded inventory; implementation, activation, installation, and runtime behavior UNKNOWN or placeholder.**

The following inventory was inspected at `main@975291ccc1342f323bb23ce723e7f5e4b1f44ddc`:

| Path | Observed state | Safe conclusion |
|---|---|---|
| [`../pyproject.toml`](../pyproject.toml) | Declares `kfm-connector-ahgp` version `0.0.0`; no other project fields are present. | Project identity is a greenfield placeholder. Build backend, dependencies, package discovery, installation, and publishing are **UNKNOWN**. |
| [`ahgp/__init__.py`](./ahgp/__init__.py) | Empty file. | No exports or import-time actions are declared in this file. Public API remains **UNKNOWN / unimplemented**. |
| [`ahgp/admit.py`](./ahgp/admit.py) | One comment identifying an admission-gate placeholder. | No admission function, gate, outcome, or lifecycle write is implemented. |
| [`ahgp/fetch.py`](./ahgp/fetch.py) | One comment identifying a fetcher placeholder. | No endpoint, network client, authentication, cadence, retry, or fetch behavior is implemented. |
| [`ahgp/descriptor.yaml`](./ahgp/descriptor.yaml) | `name: ahgp`, `role: TBD`, `rights: TBD`, and `sensitivity_floor: public`. | The file is incomplete and must not be treated as an admitted SourceDescriptor or activation decision. Unresolved role and rights require fail-closed handling. |
| [`ahgp/README.md`](./ahgp/README.md) | Draft package-level boundary document. | Documents intended constraints; does not prove executable behavior. |
| [`../tests/README.md`](../tests/README.md) | Says only `Greenfield stub.` | No AHGP-specific test modules, fixtures, coverage, or results are established by that folder. |

Because the executable Python files are empty or comment-only in this snapshot, no connector operation is present to activate, validate, or rely on. Generated, ignored, branch-local, externally deployed, or dynamically supplied behavior was not established by this bounded repository inspection.

## What belongs here

Accepted content is limited to source-tree and package implementation support such as:

- importable AHGP package directories;
- side-effect-free constants and internal types;
- explicitly invoked fetch-client helpers that require caller-supplied configuration;
- parsers that preserve source wording, locators, identifiers, timestamps, and caveats;
- digest and admission-metadata helpers;
- finite admission-outcome builders;
- explicit handoff helpers for `data/raw/` or `data/quarantine/`;
- receipt-construction helpers whose stored records remain owned by `data/receipts/`;
- source-tree documentation.

Any future code must keep the following boundary:

1. **No network on import.** Importing `ahgp` or any child module must not open sockets, make HTTP requests, resolve endpoints, or probe AHGP.
2. **No mutation on import.** Imports must not write files, create directories, read credentials, mutate registries, activate sources, or change lifecycle state.
3. **Explicit execution only.** Fetch or admission behavior may run only through an explicit caller action with explicit configuration and an admitted descriptor/decision supplied by the owning governance surface.
4. **Fail closed.** Missing or `TBD` role, rights, sensitivity, source identity, configuration, or review state must deny, abstain, or route to review/quarantine; it must not default to public use.
5. **RAW or QUARANTINE only.** Source payloads may be handed off only to an explicit `data/raw/<domain>/<source_id>/<run_id>/` or `data/quarantine/<domain>/<source_id>/<run_id>/` destination. Receipts belong in `data/receipts/` and do not authorize promotion.

## What does NOT belong here

Do not place or implement the following under `connectors/ahgp/src/`:

- authoritative SourceDescriptor records, source activation decisions, or source registry rows;
- canonical contracts, schemas, policy rules, or controlled vocabularies;
- secrets, credentials, cookies, tokens, or local environment captures;
- network calls, credential reads, filesystem writes, or activation logic at import time;
- implicit or unbounded crawling;
- source payloads or lifecycle data themselves;
- direct writes to `data/work/`, `data/processed/`, `data/catalog/`, `data/triplets/`, `data/proofs/`, `data/published/`, or `release/`;
- automatic identity resolution, kinship assertions, or claims that a person, family relationship, burial, residence, event, or locality account is verified;
- evidence closure, policy decisions, promotion, release, rollback decisions, publication, public API/UI behavior, or AI-answer behavior;
- connector-local tests or fixtures when their established home is the sibling `tests/` tree or a governed repository fixture root.

## Inputs

No runtime inputs are implemented in the inspected snapshot.

Future code may accept only explicit, reviewable inputs such as:

| Input | Required posture |
|---|---|
| Admitted SourceDescriptor reference and activation decision | Supplied by the owning registry/control-plane path; never inferred from `descriptor.yaml`. |
| AHGP source or product locator | Exact, bounded, caller supplied, and preserved in admission metadata. |
| Runtime network configuration | Explicit timeouts, retry ceiling, user agent, cadence/rate limit, and authentication posture. |
| Rights and sensitivity decisions | Resolved before capture or routed to a fail-closed outcome. |
| Destination | Explicit RAW or QUARANTINE run path; never derived from import-time environment state. |
| Candidate bytes and response metadata | Preserve content type, digest inputs, retrieval time, source time, redirect information, and limitations where available. |

The checked-in [`ahgp/descriptor.yaml`](./ahgp/descriptor.yaml) is an incomplete placeholder because `role` and `rights` are `TBD`. It is not sufficient input for activation or live fetch.

## Outputs

No executable outputs are implemented or established in the inspected snapshot.

Future explicitly invoked code may support:

- source bytes plus preserved source metadata handed to RAW;
- held source bytes plus a reason and review target handed to QUARANTINE;
- deterministic admission metadata and content digests;
- finite outcomes such as deny, abstain, skip, no-op, rate-limited, quarantine, or error;
- receipt payloads routed by the caller to `data/receipts/`.

A connector output is a source-intake artifact, not proof that the source content is true, processed, cataloged, released, or publishable. Promotion beyond RAW or QUARANTINE belongs to downstream governed stages.

## Validation

The commands below are **review commands**, not claims that this README, the AHGP connector, or CI currently passes them:

```bash
git diff --check -- connectors/ahgp/src/README.md
python -m compileall -q connectors/ahgp/src/ahgp
PYTHONPATH=connectors/ahgp/src python -c "import ahgp; import ahgp.admit; import ahgp.fetch"
python -m pytest -q tests/policy/test_pipeline_connector_non_publisher.py
python tools/validators/_common/run_all.py
```

Interpret them narrowly:

- `compileall` checks syntax only; it does not prove package discovery, installation, network safety, or connector behavior.
- the explicit `PYTHONPATH` import is a local import-safety probe only; the `pyproject.toml` does not establish installation metadata.
- [`test_pipeline_connector_non_publisher.py`](../../../tests/policy/test_pipeline_connector_non_publisher.py) statically rejects connector/pipeline write contexts near `data/catalog`, `data/published`, or `release/`; it does not prove RAW/QUARANTINE routing or AHGP functionality.
- [`tools/validators/_common/run_all.py`](../../../tools/validators/_common/run_all.py) runs five registered top-level schema validators; it does not include an AHGP connector validator.

Current workflow posture:

| Workflow | Observed behavior | Limitation |
|---|---|---|
| [`connector-gate.yml`](../../../.github/workflows/connector-gate.yml) | Contains `connector-output-gate` and `ingest-receipt-presence` jobs. | Both jobs only echo `TODO`; no enforcement is established. |
| [`policy-boundary-guards.yml`](../../../.github/workflows/policy-boundary-guards.yml) | Triggers for `connectors/**` changes and runs `make boundary-guards-ci`. | Generic boundary suite; no AHGP-specific fetch, import, descriptor, or lifecycle test is named. |
| [`link-check.yml`](../../../.github/workflows/link-check.yml) | Defines a documentation link-check job. | Job only echoes `TODO`; link validation is not established by the workflow. |

Before activation, reviewers should require dedicated no-network fixtures and tests for import safety, explicit configuration, source-role and rights refusal, success/failure/timeout/rate-limit behavior, RAW/QUARANTINE-only routing, receipt construction, and denial of all later lifecycle writes.

## Review burden

[`CODEOWNERS`](../../../.github/CODEOWNERS) has no connector-specific or AHGP-specific rule in the inspected snapshot. Its repository fallback assigns `*` to `@kfm/maintainers`; that is the only confirmed code-owner coverage for this path.

Until named ownership is established, changes should also receive human review from the connector/source steward and, when genealogy or living-person material is affected, the People/Genealogy, rights, sensitivity, and privacy reviewers. Those additional roles are governance needs, not confirmed CODEOWNERS enforcement.

Changes that activate a source, add network behavior, change lifecycle destinations, introduce a contract, or create parallel authority require broader governance review and may require an ADR under Directory Rules.

## Related folders

- [`../`](../README.md) — AHGP connector-lane boundary.
- [`ahgp/`](./ahgp/README.md) — child Python package contract and current placeholder files.
- [`../tests/`](../tests/README.md) — connector-local test lane, currently a greenfield stub.
- [`../../../docs/sources/catalog/ahgp/`](../../../docs/sources/catalog/ahgp/README.md) — AHGP source-family documentation; documentation is not activation authority.
- [`../../../data/registry/sources/`](../../../data/registry/sources/README.md) — governed source-registry surface.
- [`../../../data/raw/`](../../../data/raw/README.md) — allowed admitted-source handoff surface.
- [`../../../data/quarantine/`](../../../data/quarantine/README.md) — allowed held-source handoff surface.
- [`../../../data/receipts/`](../../../data/receipts/README.md) — process-memory home for receipts.
- [`../../../policy/rights/`](../../../policy/rights/README.md) and [`../../../policy/sensitivity/`](../../../policy/sensitivity/README.md) — policy homes outside connector authority.
- [`../../../tools/validators/connector_gate/`](../../../tools/validators/connector_gate/README.md) — connector-readiness validator boundary; direct executable behavior remains unestablished there.

## ADRs

- [`Directory Rules §7.3 and §15`](../../../docs/doctrine/directory-rules.md) supplies the confirmed connector placement and folder-README contract used here.
- [`ADR-0017 — Source Descriptor Admission Process`](../../../docs/adr/ADR-0017-source-descriptor-admission-process.md) is present but has `status: proposed`. It describes a proposed source-admission flow and therefore must not be cited as an accepted activation decision for AHGP.
- No accepted AHGP-specific ADR governing implementation, activation, endpoints, package discovery, or runtime behavior was established by the bounded inspection for this README.

## Rollback and correction

If this README is used to justify network access, source activation, an authority upgrade, or writes beyond RAW/QUARANTINE, correct the dependent change first: stop the invocation, preserve any already-captured bytes and receipts for review, quarantine affected material, and record the mistaken assumption in the appropriate correction or drift surface.

Rollback for this documentation-only addition is removal or revision of `connectors/ahgp/src/README.md`; it must not delete source bytes, receipts, evidence, or review history. Any later executable rollback must disable the explicit caller/adapter path without relying on import side effects and must preserve traceable run outcomes.

## Last reviewed

2026-07-16 — repository-grounded documentation review at `main@975291ccc1342f323bb23ce723e7f5e4b1f44ddc`. Re-review by 2027-01-16 or sooner if package metadata, child modules, tests, workflows, SourceDescriptor state, activation state, or lifecycle routing changes.

<p align="right"><a href="#top">Back to top</a></p>

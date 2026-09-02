<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runtime-adapters-readme
title: runtime/adapters/ - Runtime Adapter Compatibility Index
type: readme
version: v1.2
status: active; compatibility-only; non-authoritative
policy_label: public
owners: OWNER_TBD - Runtime steward; Docs steward
created: 2026-08-12
updated: 2026-09-01
owning_root: runtime/
responsibility: Preserve the legacy runtime/adapters discovery path while routing new adapter work to its verified responsibility owner.
current_path: runtime/adapters/README.md
canonical_adapter_lane: runtime/model_adapters/
truth_posture: CONFIRMED runtime/ responsibility, current repository lane roles, alias inventory, and repository references at the pinned snapshot / PROPOSED ADR-0008 and ADR-0019 decisions / NEEDS VERIFICATION long-term alias disposition, external consumers, accepted provider-neutral invocation contract, provider admission, live runtime integration, deployment, and release state
repository: bartytime4life/Kansas-Frontier-Matrix
visibility: public
base_ref: main
base_commit: d44526e4e24dc8b2c99c27eccfbf18ca08a770fe
prior_blob: 3b881e773f7283971fc4cc66f7e6ccbe92a5966d
related:
  - ../README.md
  - ../model_adapters/README.md
  - ../model_adapters/AdapterContract.md
  - ../mock/README.md
  - ../ollama/README.md
  - ../../contracts/runtime/README.md
  - ../../policy/runtime/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0008-ollama-subordinate-to-governed-api.md
  - ../../docs/adr/ADR-0019-ai-adapter-contract-and-finite-envelopes.md
tags: [kfm, runtime, adapters, compatibility, model-adapters, migration]
notes:
  - "The created date records the README's first appearance in the current repository history, not an independently verified authoring date."
  - "runtime/adapters is retained for discovery and compatibility; new adapter work belongs in runtime/model_adapters or another verified responsibility root."
  - "Accepted Directory Rules govern the runtime root but do not explicitly prescribe the model_adapters child spelling."
  - "This README does not define an adapter contract, activate a provider or model, grant access, prove runtime behavior, or authorize release or publication."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `runtime/adapters/` - Runtime Adapter Compatibility Index

`runtime/adapters/` preserves a legacy discovery path. It is not an adapter
implementation lane, contract authority, provider registry, or public runtime
surface.

> [!IMPORTANT]
> Put new provider-neutral adapter implementation and handoff work in
> [`runtime/model_adapters/`](../model_adapters/). Use this directory only for
> compatibility, migration, and link-preservation records approved through a
> reviewable change.

## Status and evidence boundary

| Question | Current answer | Evidence boundary |
|---|---|---|
| What owns bounded runtime composition and local adapters? | [`runtime/`](../) | The accepted [Directory Rules](../../docs/doctrine/directory-rules.md) assign this responsibility to `runtime/`. |
| Where does this repository currently place provider-neutral adapter work? | [`runtime/model_adapters/`](../model_adapters/) | The current runtime and model-adapter READMEs use this lane, and the implementation files are present there. Directory Rules do not explicitly prescribe this child name. |
| What is `runtime/adapters/`? | Compatibility index only | At the pinned snapshot it contains only `.gitkeep` and this README. |
| May public clients call adapters directly? | No | Directory Rules deny direct model-adapter access; clients must use governed interfaces or released public-safe artifacts. |
| Is the long-term alias disposition decided? | **NEEDS VERIFICATION** | Repository references still exist, and no accepted decision authorizes retirement or deletion. |

The current adapter lane contains a bounded deterministic
[`MockAdapter.py`](../model_adapters/MockAdapter.py) and a placeholder
[`OllamaAdapter.py`](../model_adapters/OllamaAdapter.py). Their detailed and
current maturity belongs in the
[model-adapter README](../model_adapters/README.md), not in this compatibility
index. File presence does not prove live provider execution, policy or citation
enforcement, receipt persistence, deployment, release, or publication.

## Purpose and bounded scope

This README exists to:

- route contributors away from a duplicate adapter home;
- preserve links that still use `runtime/adapters/`;
- record the evidence required before this alias is changed or retired; and
- keep migration reversible without promoting compatibility records into
  authority.

This README does not:

- define semantic contracts or machine-checkable schemas;
- define runtime policy, provider or model admission, network access, or tool
  permissions;
- store adapter implementations, fixtures, receipts, evidence, secrets, model
  files, or operational logs;
- prove that an adapter is integrated or safe for production; or
- approve merge, activation, deployment, release, or publication.

## Responsibility routing

Use the owning surface for the artifact being changed.

| Work item | Owning surface | Boundary |
|---|---|---|
| Provider-neutral adapter implementation, adapter card, or runtime handoff | [`runtime/model_adapters/`](../model_adapters/) | Current repository lane; do not duplicate it here. |
| Descriptive adapter boundary | [`runtime/model_adapters/AdapterContract.md`](../model_adapters/AdapterContract.md) | Runtime note only; it does not own canonical semantic meaning. |
| Deterministic mock runtime guidance | [`runtime/mock/`](../mock/) and [`runtime/model_adapters/mock/`](../model_adapters/mock/) | Keep mock behavior no-network and fixture-backed. |
| Ollama-specific local wiring | [`runtime/ollama/`](../ollama/) | Internal, local runtime concern; never a direct public endpoint. |
| Runtime object meaning | [`contracts/runtime/`](../../contracts/runtime/) | Contracts own semantics. |
| Machine-checkable runtime shape | [`schemas/contracts/v1/runtime/`](../../schemas/contracts/v1/runtime/) | Schemas own structure. |
| Runtime allow, deny, hold, restrict, or abstain rules | [`policy/runtime/`](../../policy/runtime/) | Policy owns admissibility; adapter code does not. |
| Runtime contract fixtures | [`fixtures/contracts/v1/runtime/`](../../fixtures/contracts/v1/runtime/) | Fixtures are test inputs, not production evidence. |
| Executable runtime proof | [`tests/runtime_proof/`](../../tests/runtime_proof/) and applicable schema tests | Report only checks actually run. |
| Governed public API behavior | [`apps/governed-api/`](../../apps/governed-api/) | Public clients must not depend on adapter internals. |
| Release, correction, withdrawal, or rollback decision | [`release/`](../../release/) | Runtime output cannot publish or approve public state. |

If none of these homes clearly owns an artifact, apply the accepted
[Directory Rules placement protocol](../../docs/doctrine/directory-rules.md#5-deterministic-placement-protocol)
and record the uncertainty instead of creating another adapter, contract,
schema, policy, receipt, or release home.

## Authority and anti-collapse rules

1. `runtime/model_adapters/` is the repository's current provider-neutral
   adapter lane; `runtime/adapters/` is not a competing lane.
2. The accepted Directory Rules authorize the `runtime/` responsibility, but
   they do not by themselves prove an adapter implementation or mandate this
   child-directory spelling.
3. [`ADR-0008`](../../docs/adr/ADR-0008-ollama-subordinate-to-governed-api.md)
   and
   [`ADR-0019`](../../docs/adr/ADR-0019-ai-adapter-contract-and-finite-envelopes.md)
   document proposed runtime boundaries. Both remain draft/proposed and must
   not be presented as accepted decisions.
4. Evidence, contracts, schemas, policy, tests, receipts, and release records
   retain their own authority. Adapter code and generated language do not
   replace them.
5. Public clients use governed interfaces or released public-safe artifacts;
   they do not call adapters, model daemons, or canonical/internal stores
   directly.
6. Compatibility is not authority. Keeping a path for discovery does not make
   it a valid home for new implementation.

## Compatibility and migration discipline

### Current repository inventory

At `main@d44526e4e24dc8b2c99c27eccfbf18ca08a770fe`:

- `runtime/adapters/` contains `.gitkeep` and this README;
- repository references to `runtime/adapters/` remain in the runtime indexes,
  governed-AI compatibility documentation, two proposed ADRs, and a domain
  canonical-path note; and
- no accepted decision reviewed for this update authorizes moving, deleting,
  or repurposing the path.

External consumers are **UNKNOWN**. Repository search is not proof that no
external links exist.

### Before changing the alias

1. Pin the base commit and inventory every child, case variant, generated copy,
   and symbolic link.
2. Find repository consumers and identify any external consumers that can be
   verified.
3. Classify each item by responsibility; do not bulk-move by filename.
4. Obtain review for the proposed pointer, tombstone, migration, or retirement
   state.
5. Update canonical records first, then repair consumers and preserve forward
   links when needed.
6. Run the focused documentation and implementation checks required by the
   changed artifacts.
7. Record the prior commit or blob and a transparent revert path.
8. Delete the alias only after consumer closure and the required governance
   decision are evidenced.

Stop and mark the change **NEEDS VERIFICATION** when the target home, consumers,
authority effect, generated-source relationship, or rollback path cannot be
resolved.

## Contributor check

For an ordinary adapter change:

- start in [`runtime/model_adapters/`](../model_adapters/), not here;
- keep provider-specific transport behind the provider-neutral boundary;
- keep mock behavior deterministic and no-network;
- link rather than copy contracts, schemas, policy, evidence, receipts, or
  release rules;
- keep secrets, private prompts, protected evidence, model weights, and private
  endpoints out of Git;
- preserve finite, fail-safe outcomes and cite-or-abstain where evidence support
  is required; and
- do not infer runtime, deployment, or release maturity from README text or a
  passing shape test.

For a compatibility-only documentation change, inspect the current inventory
and references:

```bash
find runtime/adapters -mindepth 1 -maxdepth 2 -type f -print | sort
rg -n 'runtime/adapters' .
```

Validate changed Markdown with the repository's bounded, no-network checker:

```bash
base_sha="$(git merge-base origin/main HEAD)"
python -m unittest discover \
  --start-directory tests/validators/docs/link-check \
  --pattern 'test_*.py' \
  --verbose
python tools/validators/docs/link-check/check_links.py \
  --repo-root . \
  --git-diff "${base_sha}...HEAD" \
  --format text
```

These checks verify bounded documentation behavior only. They are not evidence,
policy, review, release, deployment, or publication approval.

## Maintenance, correction, and rollback

Update this index when the current adapter lane changes, the alias gains or
loses verified consumers, or an approved migration changes the disposition.
Keep implementation detail in its owning documentation rather than duplicating
it here.

Correct errors through a reviewable commit that names the affected claim and
preserves Git history. Roll back this README with a normal revert of the
documentation commit. A documentation revert does not roll back an adapter,
provider, policy, receipt, deployment, release, or published artifact.

## Open verification

- Decide whether this path remains a permanent pointer, becomes a governed
  tombstone, or can be retired after consumer closure.
- Verify external consumers before any rename or deletion.
- Verify the accepted provider-neutral invocation contract and its relationship
  to the descriptive `FocusRequest` note, `DecisionEnvelope`, and
  `RuntimeResponseEnvelope` before claiming interface conformance.
- Verify provider/model admission, policy execution, evidence resolution,
  citation validation, receipt persistence, correction propagation, and public
  API integration from current implementation evidence before claiming runtime
  readiness.

## Evidence basis

| Evidence | What it supports | Limitation |
|---|---|---|
| [Accepted Directory Rules](../../docs/doctrine/directory-rules.md) and [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | `runtime/` responsibility and no-direct-public-adapter boundary | Do not explicitly prescribe `runtime/model_adapters/`. |
| [`runtime/README.md`](../README.md) | Current child-lane classification and compatibility posture | Documentation is not execution proof. |
| [`runtime/model_adapters/README.md`](../model_adapters/) and current files in that directory | Current repository adapter lane and bounded implementation inventory | Do not prove provider integration, admission, or production use. |
| [`runtime/model_adapters/AdapterContract.md`](../model_adapters/AdapterContract.md) | Descriptive `FocusRequest` to `DecisionEnvelope` note | Not canonical semantic contract authority. |
| Proposed [ADR-0008](../../docs/adr/ADR-0008-ollama-subordinate-to-governed-api.md) and [ADR-0019](../../docs/adr/ADR-0019-ai-adapter-contract-and-finite-envelopes.md) | Proposed adapter, provider, finite-envelope, and public-boundary direction | Both decisions remain draft/proposed. |
| Repository inventory and reference search at the pinned base | Current alias contents and visible repository consumers | Does not prove external-consumer closure. |

<p align="right"><a href="#top">Back to top</a></p>

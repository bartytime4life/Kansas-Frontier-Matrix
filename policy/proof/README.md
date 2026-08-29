<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/policy/proof/readme
title: Proof Policy Routing and Hold Boundary
type: readme
version: v1.1
status: provisional; routing-only; implementation-empty; evaluator-unbound; non-release; non-publication
owner: NEEDS VERIFICATION — CODEOWNERS routes policy changes to @bartytime4life; proof-policy stewardship, evaluator ownership, independent review, retention, and release authority are not established here
created: 2026-08-28
updated: 2026-08-28
current_path: policy/proof/README.md
owning_root: policy/
policy_label: public; policy; routing-boundary; hold; non-release; non-publication
responsibility: Prevent the direct policy/proof marker lane from being mistaken for ProofPack meaning, proof storage, proof tooling, an active policy bundle, an evaluator entrypoint, release approval, or publication authority, and route contributors to current repository-backed proof responsibilities.
base_commit: 332a371f0be1aae68690853fba368a6289d2dab4
prior_blob: 79f6e1fa60f8df2b6610b28f54fb13a8e69d9d34
directory_governance: ADR-0029 accepted Directory Rules v2 for responsibility-first placement; proof, receipt, catalog, policy, release, and published carriers remain distinct responsibilities
truth_posture: CONFIRMED this directory contains only .gitkeep and this README; no Rego, bundle, evaluator, fixture, test, workflow, consumer, decision, receipt, proof instance, release artifact, or public behavior exists here; current GitHub evidence places ProofPack meaning, shape, instances, tooling, tests, and orchestration in separate owning surfaces / PROPOSED this routing-and-hold boundary / UNKNOWN future policy family, writer, reader, retention, evaluator, consumer, decision-receipt, release, correction, rollback, and publication bindings
[/KFM_META_BLOCK_V2] -->

# Proof policy routing and hold boundary

<a id="top"></a>

> **One-line purpose.** `policy/proof/` is a documented hold around an
> otherwise empty direct policy lane. It is not ProofPack authority, proof
> storage, an active policy bundle, an evaluator entrypoint, a release gate, or
> a public interface.

| Current question | Repository-backed answer |
|---|---|
| Does this directory contain executable policy? | **No.** It contains only `.gitkeep` and this README. |
| Does it own proof records or ProofPack semantics? | **No.** Proof support, semantic meaning, machine shape, tools, tests, and release decisions have separate owning surfaces. |
| Do current ProofPack checks activate this lane? | **No.** They validate one proposed, fixture-first release-support profile and explicitly create no policy, release, or publication authority. |
| What should happen when proof-related policy is unresolved? | Hold, restrict, deny, abstain, or error under the governing contract; do not invent a policy decision from proof presence or a green check. |

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-and-current-state) ·
[Routing](#authority-routing) · [Hold](#hold-contract) · [Inputs and outputs](#inputs-and-outputs) ·
[Safety](#rights-sensitivity-and-proof-limits) · [Validation](#validation) ·
[Maintenance](#maintenance-correction-and-rollback) · [Open questions](#open-questions) ·
[Related](#related-repository-surfaces)

## Purpose

This README closes a documentation gap without filling an implementation gap.
It gives maintainers an evidence-backed answer when they encounter the tracked
`policy/proof/` path:

- do not place proof records, ProofPack schemas, tooling, or release decisions
  here merely because they mention policy;
- do not interpret a ProofPack, EvidenceBundle, receipt, workflow, validator, or
  passing test as an admissibility decision;
- route each proof responsibility to its current owning surface; and
- preserve the missing policy-family decision until semantics, rules, evaluator,
  consumers, receipts, correction, rollback, and independent review are accepted.

This document does not choose a future rule family or authorize deletion,
migration, compatibility, evaluation, release, deployment, or publication.

## Authority and current state

The repository at `main@332a371f0be1aae68690853fba368a6289d2dab4`
provides the controlling evidence for this boundary.

| Evidence | What it establishes | What it does not establish |
|---|---|---|
| [Canonical policy root](../README.md) | `policy/` is the adopted policy-source responsibility root and direct children may have mixed maturity. | Every child is active, accepted, or executable. |
| [Accepted Directory Rules](../../docs/doctrine/directory-rules.md) and [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Responsibility-first placement and separation of proof, receipt, policy, release, and published carriers. | A proof-policy family, evaluator, or release binding. |
| [Proof-support root](../../data/proofs/README.md) | `data/proofs/` owns governed proof-support records and no-direct-public-path boundaries. | Policy permission, release approval, or factual truth. |
| [ProofPack contract](../../contracts/evidence/proof_pack.md) and [schema](../../schemas/contracts/v1/evidence/proof_pack.schema.json) | A proposed release-support profile has documented meaning and machine shape. | Accepted universal ProofPack semantics or policy activation. |
| [ProofPack tools](../../tools/proof_pack/README.md), [tests](../../tests/proof_pack/test_proof_pack_check.py), and [workflow](../../.github/workflows/proof-pack-closure.yml) | A bounded, deterministic, no-network assembler/checker profile is executable and tested. | Evidence authenticity, policy correctness, review, release, deployment, or publication. |
| This directory | `.gitkeep` and this README are tracked. | Rego, a bundle, evaluator, fixture, test, workflow, consumer, decision, receipt, or proof instance. |

Connected Drive planning material describes candidate proof systems but leaves
repository adoption and implementation unresolved. No relevant current Notion
authority was found. Those sources are historical or proposal lineage only;
current GitHub evidence and accepted repository doctrine control this boundary.

## Authority routing

Use the owning surface for the responsibility being changed.

| Responsibility | Current repository surface | Boundary |
|---|---|---|
| Policy-root placement and maturity | [`policy/README.md`](../README.md) | Root contract; not a general evaluator. |
| Proof-support records and indexes | [`data/proofs/`](../../data/proofs/README.md) | Governed support; not policy or release authority. |
| Release-support ProofPack instances | [`data/proofs/proof_pack/`](../../data/proofs/proof_pack/README.md) | Candidate proof records; not public truth or release decisions. |
| ProofPack semantic meaning | [`contracts/evidence/proof_pack.md`](../../contracts/evidence/proof_pack.md) | Proposed profile meaning; not machine enforcement. |
| ProofPack machine shape | [`proof_pack.schema.json`](../../schemas/contracts/v1/evidence/proof_pack.schema.json) | Shape only; schema validity is not admissibility. |
| Assembly and checking | [`tools/proof_pack/`](../../tools/proof_pack/README.md) | Executable support tooling; no canonical proof storage or approval authority. |
| Focused tests | [`test_assemble_proof_pack.py`](../../tests/proof_pack/test_assemble_proof_pack.py) and [`test_proof_pack_check.py`](../../tests/proof_pack/test_proof_pack_check.py) | Bounded behavior evidence; not operational release proof. |
| Hosted closure check | [`proof-pack-closure.yml`](../../.github/workflows/proof-pack-closure.yml) | Orchestration for the bounded profile; workflow success is not release. |
| Process receipts | [`data/receipts/`](../../data/receipts/README.md) | Process memory; receipts do not prove claims by themselves. |
| Release decisions, correction, and rollback | [`release/`](../../release/README.md) | Separate release authority; never inferred from this lane or a ProofPack pass. |
| General policy evaluation | [`packages/policy-runtime/`](../../packages/policy-runtime/README.md) | Placeholder runtime boundary; no accepted general evaluator is established. |
| Root-level compatibility fence | [`catalog/proof/`](../../catalog/proof/README.md) | Drift redirect only; not canonical proof storage. |

A proof object can reference a policy decision; it cannot create one. A policy
rule can require proof; it cannot make unsupported evidence true.

## Hold contract

Until an accepted decision and implementation establish otherwise:

1. Do not place Rego, bundle manifests, evaluator configuration, emitted
   decisions, receipts, proof records, or release artifacts in this directory.
2. Do not duplicate the ProofPack contract, schema, fixtures, tools, tests,
   workflow, or stored instances here.
3. Do not treat proof presence, schema validity, digest agreement, or workflow
   success as an allow decision.
4. Do not treat a policy result as evidence authenticity, proof closure, human
   review, release approval, or publication.
5. If a required proof-policy binding, evaluator, consumer, or decision receipt
   is absent, preserve the governing negative state instead of inventing closure.

A future change may supersede this hold only when it names the policy
responsibility, rule package and entrypoint, accepted inputs and outcomes,
ProofPack or EvidenceBundle bindings, evaluator, fixtures and negative tests,
consumers, authenticated decision receipts, retention, correction, rollback,
release dependency, and independent review path.

## Inputs and outputs

This documentation boundary consumes repository evidence only. Its output is
contributor routing and an explicit hold. It emits no policy decision, proof
record, evidence claim, receipt, permit, denial, obligation, release approval,
deployment state, or public artifact.

## Rights, sensitivity, and proof limits

Proof material can reference living people, DNA/genomics, Indigenous or cultural
knowledge, protected species, archaeology, land or title claims, critical
infrastructure, precise locations, and licensed or restricted sources. This empty
lane supplies no rules for those cases.

- Preserve provenance, source role, rights, consent, sensitivity, sovereignty,
  purpose, audience, precision, effective time, limitations, correction, and
  withdrawal state at their governing surfaces.
- A hash proves byte agreement, not source authority, consent, factual truth, or
  suitability for an audience.
- Maps, tiles, dashboards, indexes, tests, workflows, and generated language are
  not sovereign truth.
- Public clients must use governed interfaces or released public-safe artifacts,
  not policy source, proof stores, or this routing document.
- When evidence or authority is insufficient, narrow, generalize, hold, abstain,
  deny, or error as the governing contract requires.

## Validation

Focused documentation checks:

```bash
python tools/validators/docs/link-check/check_links.py \
  policy/proof/README.md policy/README.md tools/proof_pack/README.md
python tools/validators/docs/meta-block/check_meta_blocks.py \
  --profile required policy/proof/README.md policy/README.md tools/proof_pack/README.md
```

The link checker covers repository-local files, directories, images, and
fragments. The metadata checker covers the bounded metadata envelope. Passing
either command confirms only its exercised documentation QA scope at this
revision.

Focused ProofPack implementation checks are documented in the
[tooling README](../../tools/proof_pack/README.md). They validate only the named
fixture-first profile.

Reviewers should also verify that this directory contains only `.gitkeep` and
this README, the current parent inventory records 40 substantive direct-child
READMEs, zero one-byte direct-child placeholders, and no missing direct README;
every relative target resolves, and the base-to-head diff changes Markdown only.

## Maintenance, correction, and rollback

Recheck this README when accepted Directory Rules, proof or policy ADR status,
the direct contents of this directory, the ProofPack profile, a proof-policy
rule or evaluator, retention, correction, rollback, or public-use obligations
change.

For this documentation-only change, rollback means reverting the focused commits
or closing the unmerged draft PR. Reverting must not remove or alter proof
records, contracts, schemas, fixtures, tools, tests, workflows, receipts, release
artifacts, deployments, or published state.

## Open questions

| ID | Question | Current status |
|---|---|---|
| PROOF-POL-001 | What admissibility question, if any, should a future `policy/proof/` family answer? | **UNKNOWN / NEEDS DECISION** |
| PROOF-POL-002 | Which accepted rule package, bundle selector, evaluator, input profile, and finite outcomes would implement it? | **UNKNOWN** |
| PROOF-POL-003 | How would ProofPack and EvidenceBundle references bind to authenticated policy inputs and decision receipts without collapsing authority? | **NEEDS DESIGN AND IMPLEMENTATION** |
| PROOF-POL-004 | Who writes, reads, retains, corrects, withdraws, replays, and invalidates those decisions? | **NEEDS VERIFICATION** |
| PROOF-POL-005 | Which independent evidence, policy, rights, sensitivity, sovereignty, security, release, and domain reviews are required? | **NEEDS VERIFICATION** |

## Related repository surfaces

- [Canonical policy root](../README.md)
- [Proof-support root](../../data/proofs/README.md)
- [ProofPack instance lane](../../data/proofs/proof_pack/README.md)
- [ProofPack contract](../../contracts/evidence/proof_pack.md)
- [ProofPack tooling](../../tools/proof_pack/README.md)
- [Directory Rules](../../docs/doctrine/directory-rules.md)
- [ADR index](../../docs/adr/README.md)

[Back to top](#top)

## Changelog

| Version | Date | Change | Runtime effect |
|---|---|---|---|
| v1.1 | 2026-08-28 | Removed a nonexistent fragment-checker command, documented the supported link checker's fragment scope, and reconciled the parent policy inventory. | None; documentation only. |
| v1.0 | 2026-08-28 | Replaced the one-byte placeholder with a repository-grounded routing-and-hold boundary and separated proof support, policy, tooling, receipts, release, and publication responsibilities. | None; documentation only. |

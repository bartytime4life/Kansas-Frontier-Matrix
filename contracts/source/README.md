<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-source-readme
title: contracts/source — Source Contract Semantics README
type: readme
version: v0.2
status: draft; PROPOSED; semantic-contract-lane; source-admission-aware; source-role-anti-collapse
owners: OWNER_TBD — Source steward · Contracts steward · Schema steward · Policy steward · Catalog steward · Evidence steward · Docs steward
created: NEEDS VERIFICATION — stub existed before v0.2 expansion
updated: 2026-06-24
policy_label: public; contracts; source; semantic-contracts; source-descriptor; source-role; rights; sensitivity; citation; admission; fail-closed; no-source-truth
tags: [kfm, contracts, source, README, source-descriptor, source-role, rights, sensitivity, cadence, access-posture, citation, source-registry, admission, anti-collapse, evidence-first]
related:
  - ../README.md
  - ./source_descriptor.md
  - ../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../packages/source-registry/README.md
  - ../../data/registry/sources/
  - ../../control_plane/source_authority_register.yaml
  - ../../policy/source/
  - ../../policy/rights/
  - ../../policy/sensitivity/
  - ../../fixtures/contracts/v1/source/
  - ../../tests/contracts/source/
  - ../../tools/validators/
  - ../../docs/architecture/contract-schema-policy-split.md
notes:
  - "Expanded from the short stub at `contracts/source/README.md`."
  - "This README defines the source semantic-contract lane only; source registry records, source authority registers, schemas, policy, fixtures, tests, packages, lifecycle data, and release decisions remain in separate roots."
  - "The inspected source_descriptor contract exists at `contracts/source/source_descriptor.md`."
  - "The inspected source_descriptor schema exists at `schemas/contracts/v1/source/source_descriptor.schema.json` and records source identity, role, rights, sensitivity, cadence, access, citation, review, release, and lifecycle posture."
  - "The source descriptor standard says source registry is an admission and authority-control surface, not a bibliography."
  - "Rollback target for this expansion is previous stub blob SHA `2fe3bbb50c1432ef679be3220c40bb8b197919c0`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# contracts/source

> Semantic-contract lane for KFM source objects, especially `SourceDescriptor`. Contracts here define what source-governance objects mean. They do not store source data, admit sources by themselves, validate JSON, decide policy, publish releases, or make source claims true.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts-blue">
  <img alt="Family: source" src="https://img.shields.io/badge/family-source-0a7ea4">
  <img alt="Purpose: semantic meaning" src="https://img.shields.io/badge/purpose-semantic__meaning-blueviolet">
  <img alt="Default: fail closed" src="https://img.shields.io/badge/default-fail__closed-critical">
</p>

**Status:** draft / PROPOSED  
**Path:** `contracts/source/README.md`  
**Owning root:** `contracts/` — semantic meaning only  
**Primary inspected contract:** `contracts/source/source_descriptor.md`  
**Primary inspected schema:** `schemas/contracts/v1/source/source_descriptor.schema.json`  
**Policy homes:** `policy/source/`, `policy/rights/`, `policy/sensitivity/`  
**Registry homes:** `data/registry/sources/` and proposed control-plane source-authority registers  
**Truth posture:** CONFIRMED target was a short stub · CONFIRMED `source_descriptor.md` exists · CONFIRMED paired source descriptor schema exists · CONFIRMED source-registry package README separates helper code from source authority · NEEDS VERIFICATION for validator wiring, policy packages, fixtures, source-registry records, CI gates, runtime consumers, and release workflows unless checked separately

## Quick jumps

[Purpose](#purpose) · [Authority split](#authority-split) · [SourceDescriptor role](#sourcedescriptor-role) · [Accepted contents](#accepted-contents) · [Exclusions](#exclusions) · [Source anti-collapse rules](#source-anti-collapse-rules) · [Validation expectations](#validation-expectations) · [Open questions](#open-questions) · [Rollback](#rollback)

---

## Purpose

`contracts/source/` is the semantic-contract home for source-governance objects.

It answers:

- what a source-governance object means;
- what claims it can and cannot support;
- which role, rights, sensitivity, cadence, access, citation, review, release, and lifecycle fields matter semantically;
- which adjacent roots own schema shape, policy decisions, source registry records, implementation, fixtures, tests, and release state;
- how source-role anti-collapse must be preserved before downstream evidence, catalog, map, graph, API, or AI surfaces use source material.

It does not answer:

- whether a source claim is true;
- whether source data can be published;
- whether a source can bypass policy review;
- whether JSON is valid;
- whether a connector may run;
- whether rights or sensitivity are acceptable for a particular public surface;
- whether a release is approved.

---

## Authority split

| Responsibility | Correct home | Rule |
|---|---|---|
| Source object meaning | `contracts/source/` | This lane. Markdown semantic contracts only. |
| Source descriptor machine shape | `schemas/contracts/v1/source/` or accepted successor | JSON Schema owns field shape and validation surface. |
| Source admission policy | `policy/source/`, `policy/rights/`, `policy/sensitivity/` | Policy owns allow/deny/restrict/abstain behavior. |
| Source registry records | `data/registry/sources/` or accepted source registry roots | Registry/lifecycle records are not contract prose. |
| Source authority register | `control_plane/source_authority_register.yaml` or accepted register root | Authority-control register is separate from contract meaning. |
| Source resolver/helper code | `packages/source-registry/` or accepted implementation roots | Packages may load/normalize; they do not own truth. |
| Fixtures/tests | `fixtures/`, `tests/` | Proof and examples stay outside contracts. |
| Validators | `tools/validators/` or accepted validator roots | Executable validation stays outside contracts. |
| Release/correction/rollback | `release/` and release contract/release roots | Publication is a governed state transition. |
| Public API/UI/map/AI | governed runtime/API/UI/map/AI roots | Downstream consumers only. |

---

## SourceDescriptor role

The inspected source descriptor standard defines `SourceDescriptor` as the structured, persisted record that fixes source identity, role, rights, sensitivity, cadence, access posture, and citation guidance at admission. It anchors downstream receipts and is the first source-registry object resolved before a connector or watcher activates.

Inside KFM, `SourceDescriptor` is a governance handle. It is not:

- a citation by itself;
- a license file by itself;
- a source-data file;
- a release manifest;
- proof that the source claim is true;
- permission to publish;
- permission for AI to infer source authority.

---

## Accepted contents

Files in this lane may include:

| Accepted item | Purpose | Guardrail |
|---|---|---|
| `README.md` | Defines source contract-lane boundary. | Must preserve root split. |
| `source_descriptor.md` | Semantic meaning of SourceDescriptor. | Must stay paired with schema/policy/fixture/test posture. |
| `ingest_receipt.md` or future source receipt contracts | Source-related receipt meaning, if accepted. | Must not duplicate runtime/run receipt or release manifest authority. |
| Compatibility or migration notes | Link old source contract references to accepted homes. | Must identify rollback/backlink handling. |
| Contract indexes | Maintainer navigation only. | Must not claim unverified implementation maturity. |

Any new source contract must state:

1. what the object means;
2. what it does not prove;
3. which source role and rights/sensitivity posture it carries;
4. which schema, policy, fixtures, tests, validators, registry records, release/correction/rollback surfaces remain separate;
5. which downstream surfaces may consume it only after governed checks.

---

## Exclusions

| Do not put this here | Correct home | Reason |
|---|---|---|
| SourceDescriptor JSON instances | `data/registry/sources/` or accepted registry roots | Contracts do not store registry records. |
| JSON Schema | `schemas/contracts/v1/source/` or successor | Schemas own shape. |
| Policy rules | `policy/source/`, `policy/rights/`, `policy/sensitivity/` | Policy owns admissibility. |
| Source catalog profiles | `docs/sources/catalog/` | Human-facing catalog profile docs are not contracts. |
| Connector code | `connectors/`, packages, apps, tools, pipelines | Runtime implementation belongs outside contracts. |
| Source raw data | `data/raw/` and lifecycle roots | RAW data stays in lifecycle roots. |
| Tests/fixtures | `tests/`, `fixtures/` | Enforceability stays outside contracts. |
| Release manifests, rollback cards, correction notices | `release/` and release contract/release roots | Release state is separate. |
| Public claim text or AI summaries | governed evidence/runtime/API roots | EvidenceBundle outranks generated language. |

---

## Source anti-collapse rules

Source-governance contracts must preserve these rules:

- Source role is fixed at admission and must not be silently upgraded by promotion.
- Unknown rights fail closed.
- Unknown sensitivity fails closed.
- Candidate or restricted sources must not reach public surfaces without governed promotion, review, policy, and release state.
- Source role cannot be inferred by AI generation.
- A source descriptor controls how source material may be treated; it does not make the source's claims true.
- Source registry helper code may resolve descriptors but must not override descriptor authority, policy, rights, sensitivity, review, or release state.
- Corrections and supersessions must be auditable; source changes should produce new or superseding records rather than silent mutation.

---

## Validation expectations

NEEDS VERIFICATION in implementation:

- current validator path and wiring for source descriptors;
- fixture coverage for valid, restricted, rights-unknown, sensitivity-unknown, closed-access, candidate, superseded, and stale descriptors;
- policy/source enforcement of rights/sensitivity/source-role rules;
- source-registry record home and identity conventions;
- source authority register maturity;
- runtime/API/catalog/AI consumers resolving descriptors before use;
- release gates blocking unresolved or restricted source posture;
- correction/supersession paths for source descriptor updates.

---

## Open questions

- Should the schema path migrate from `schemas/contracts/v1/source/` to `schemas/contracts/v1/sources/`, as the schema metadata currently records both canonical and legacy paths?
- Which source-role vocabulary is final across all domains?
- Where should persisted SourceDescriptor records live once registry layout is finalized?
- Which policy package blocks sensitivity-floor downgrades and unresolved rights?
- Should source admission emit a dedicated receipt object in addition to SourceDescriptor?

---

## Rollback

Rollback is required if this lane is used as source data storage, schema authority, policy authority, source registry record authority, release approval, executable connector/runtime behavior, public API permission, or AI/source-truth authority.

Rollback target for this expansion: previous stub blob SHA `2fe3bbb50c1432ef679be3220c40bb8b197919c0`.

<p align="right"><a href="#top">Back to top</a></p>

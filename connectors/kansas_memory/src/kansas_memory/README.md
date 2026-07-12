<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-kansas-memory-src-package-readme
title: Kansas Memory compatibility package boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · Kansas source steward · Archives steward · Rights reviewer · Sensitivity reviewer · Cultural-care reviewer · Validation steward · Package maintainer · Docs steward
created: 2026-06-19
updated: 2026-07-12
policy_label: public-doctrine; compatibility-package; no-network-default; rights-gated; sensitivity-gated; no-publication
path: connectors/kansas_memory/src/kansas_memory/README.md
truth_posture: CONFIRMED package path and current file inventory / NONCANONICAL compatibility namespace / NEEDS VERIFICATION implementation and migration state
related:
  - ../README.md
  - ../../README.md
  - ../../tests/README.md
  - ../../../kansas/README.md
  - ../../../kansas/kansas-memory/README.md
  - ../../../../docs/sources/catalog/kansas/kansas-memory.md
  - ../../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../../schemas/contracts/v1/source/
  - ../../../../policy/rights/
  - ../../../../policy/sensitivity/
  - ../../../../data/raw/archives/
  - ../../../../data/quarantine/archives/
  - ../../../../release/
tags: [kfm, connectors, kansas-memory, archives, python-package, compatibility, source-admission, raw, quarantine, rights, sensitivity, cultural-care, governance]
notes:
  - "Current-session repository evidence confirms this README and an empty __init__.py in the package directory."
  - "No parser, fetcher, normalizer, validator, handoff, fixture, or runtime module is claimed by this README."
  - "The parent README classifies connectors/kansas_memory/ as a noncanonical compatibility lane; canonical placement remains governed by repository evidence and an ADR or migration record."
  - "Any future implementation must remain source-admission-only and may hand off only to governed RAW or QUARANTINE intake."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Kansas Memory compatibility package boundary

> Package-level contract for the existing `kansas_memory` Python namespace. The namespace is a **noncanonical compatibility surface** and currently provides no verified connector behavior.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Inventory: README plus empty init" src="https://img.shields.io/badge/inventory-README%20%2B%20empty%20__init__-blue">
  <img alt="Canonicality: compatibility" src="https://img.shields.io/badge/canonicality-compatibility-orange">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled%20by%20default-critical">
  <img alt="Lifecycle: RAW or QUARANTINE only" src="https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE%20only-orange">
</p>

> [!IMPORTANT]
> **CONFIRMED:** this directory contains `README.md` and an empty `__init__.py`.  
> **UNKNOWN:** no executable connector behavior, fixture set, test implementation, activation wiring, or CI coverage was verified for this package.  
> **BOUNDARY:** this namespace must not become a truth store, policy authority, release engine, public API, or publication path.

**Quick jumps:** [Purpose](#purpose) · [Current evidence](#current-evidence) · [Ownership boundary](#ownership-boundary) · [Permitted future work](#permitted-future-work) · [Prohibited behavior](#prohibited-behavior) · [Admission contract](#admission-contract) · [Validation and tests](#validation-and-tests) · [Graduation gate](#graduation-gate) · [Rollback](#rollback) · [Verification backlog](#verification-backlog)

---

## Purpose

`connectors/kansas_memory/src/kansas_memory/` is the Python package directory under the existing top-level Kansas Memory compatibility connector.

Its responsibility is deliberately narrow:

1. preserve a package namespace while canonical placement is resolved;
2. document the source-admission boundary for any later compatibility code;
3. prevent this path from silently becoming a parallel connector authority.

The package does **not** establish that Kansas Memory access is active, lawful for a particular use, technically available, schema-stable, or approved for publication.

---

## Current evidence

| Evidence | Status | What it proves | What it does not prove |
|---|---:|---|---|
| `README.md` | **CONFIRMED** | This package contract exists. | Runtime behavior or implementation maturity. |
| `__init__.py` | **CONFIRMED — empty** | The Python package marker exists. | Public exports, adapter behavior, or supported API. |
| `connectors/kansas_memory/README.md` | **CONFIRMED** | The parent path is documented as a noncanonical compatibility lane. | Final migration outcome or canonical child implementation. |
| `connectors/kansas/README.md` | **CONFIRMED** | Kansas sources are coordinated through the Kansas source-family admission lane. | That a `kansas-memory/` implementation is complete or active. |
| Parser, fetch, normalization, validation, handoff, or error modules | **NOT VERIFIED** | Nothing beyond the package marker is claimed. | Presence, behavior, tests, or CI coverage. |

> [!NOTE]
> Earlier wording described a proposed module tree. That proposal is removed from the package inventory because repository evidence does not confirm those modules.

---

## Ownership boundary

This package may eventually own **source-specific compatibility code** needed to interpret Kansas Memory responses or fixtures before governed handoff.

It does not own:

- source registration or activation decisions;
- canonical schemas or contract definitions;
- rights, sensitivity, cultural-care, sovereignty, or living-person policy;
- domain truth or historical interpretation;
- EvidenceBundle closure;
- processed records, catalog/triplet projection, proof, release, or publication;
- public routes, public search, public timelines, public maps, or AI answers.

Where placement or authority is disputed, the package must remain inert and the question must be resolved through current repository evidence, Directory Rules, and an ADR or migration record.

---

## Permitted future work

After placement and governance review, compatibility code in this namespace may support:

- deterministic parsing of approved fixtures;
- preservation of collection, item, source URI, and source-native identifiers;
- loss-minimizing metadata normalization without semantic or evidentiary upgrade;
- preservation of source dates, retrieval dates, rights statements, access notes, and review flags;
- explicit detection of missing or ambiguous identity, rights, sensitivity, or metadata fields;
- construction of caller-owned RAW or QUARANTINE admission candidates;
- deterministic error results that support deny, abstain, or quarantine outcomes;
- temporary import shims during an approved migration.

These are **allowed responsibilities**, not claims that the implementation exists.

---

## Prohibited behavior

Code in this package must not:

- perform live network access by default;
- embed credentials, tokens, cookies, private URLs, or session material;
- activate a source merely because configuration or code exists;
- infer rights or public-domain status from accessibility alone;
- suppress sensitivity, cultural-care, sovereignty, or living-person concerns;
- convert OCR, generated text, metadata, or an archival item into an authoritative historical claim;
- write directly to `PROCESSED`, `CATALOG`, `TRIPLET`, `PUBLISHED`, proof, receipt, or release stores;
- expose a normal public-client path to RAW, QUARANTINE, canonical stores, or connector internals;
- treat this compatibility namespace as canonical without an accepted migration decision;
- publish, promote, or approve its own output.

---

## Admission contract

Any later implementation must preserve the KFM lifecycle:

```text
source material
  -> SourceDescriptor and activation checks
  -> compatibility parsing or validation
  -> RAW candidate | QUARANTINE candidate | DENY | ABSTAIN | ERROR
  -> downstream validation and evidence work
  -> PROCESSED
  -> CATALOG / TRIPLET
  -> governed release
  -> PUBLISHED
```

The connector boundary ends at a caller-owned admission candidate or a finite failure outcome. A handoff is not promotion, publication, proof, or evidence closure.

Minimum candidate metadata should remain explicit where available:

- source and collection identity;
- item identifier and source URI;
- retrieval time and source-provided temporal fields;
- source-native metadata payload or a lossless reference to it;
- access method and parser/version identity;
- rights statement and unresolved-rights flag;
- sensitivity, cultural-care, sovereignty, and living-person review flags;
- validation findings and quarantine reasons;
- deterministic content or payload digest where repository contracts require it.

Exact field names and schema homes remain **NEEDS VERIFICATION** until confirmed from accepted contracts and tests.

---

## Runtime posture

Default behavior must be fail-safe:

- network disabled unless explicitly enabled by reviewed configuration;
- no activation without accepted source registration and activation evidence;
- no public output;
- no direct lifecycle advancement beyond RAW or QUARANTINE admission;
- no secrets in source, fixtures, logs, errors, or receipts;
- deterministic handling of malformed, ambiguous, or policy-incomplete material;
- quarantine or abstention when identity, rights, sensitivity, cultural-care, source role, or metadata shape cannot be resolved safely.

A future live-source mode requires separate source-steward, rights, security, and policy review, plus rate limits, observability, replay-safe receipts, and non-network default tests.

---

## Validation and tests

Implementation maturity must not be claimed until repository evidence demonstrates at least:

- fixture-only deterministic parsing tests;
- malformed and incomplete record tests;
- identity and source-URI preservation tests;
- rights and sensitivity metadata preservation tests;
- unresolved cultural-care or living-person routing tests;
- no-network-by-default tests;
- secret-redaction tests;
- RAW/QUARANTINE-only output tests;
- refusal tests for processed, catalog, release, or public output;
- schema or contract validation against the accepted source-admission envelope;
- CI execution for the relevant connector gate.

Tests must validate behavior, not merely README wording.

---

## Graduation gate

This package may move beyond an inert compatibility marker only when all applicable evidence is present:

- [ ] canonical placement is resolved by current repo convention, ADR, or migration record;
- [ ] a Kansas Memory source identity and SourceDescriptor are accepted;
- [ ] activation state is explicit and reviewable;
- [ ] current access method and source terms are verified;
- [ ] rights, sensitivity, cultural-care, sovereignty, and living-person handling are approved;
- [ ] input and output contracts are accepted;
- [ ] deterministic fixtures and negative cases exist;
- [ ] no-network and no-publication defaults are tested;
- [ ] CI runs the connector-specific validation path;
- [ ] migration and rollback targets are recorded.

Until then, the package remains **documentation plus an empty package marker**.

---

## Rollback

This documentation-only change is reversible by restoring the prior README blob:

```text
c61a5bc9b0e1e45df33020816ff9949d66421dc2
```

Use a normal revert commit or follow-up pull request. Do not rewrite shared history.

Rollback is required if this README is used to justify canonical status, live harvesting, source activation, policy bypass, implementation maturity, direct lifecycle promotion, or public release without the evidence listed above.

---

## Verification backlog

| Item | Status | Evidence needed |
|---|---:|---|
| Resolve the canonical Kansas Memory implementation home. | **NEEDS VERIFICATION** | Current repo tree, Directory Rules, ADR, or migration record. |
| Confirm whether this compatibility package should remain, redirect, or be removed. | **NEEDS VERIFICATION** | Migration plan and dependency search. |
| Confirm source identity, SourceDescriptor, and activation state. | **NEEDS VERIFICATION** | Accepted registry records and activation evidence. |
| Confirm current source access method and terms. | **NEEDS VERIFICATION** | Source-steward and rights review. |
| Confirm accepted admission envelope and schema home. | **NEEDS VERIFICATION** | Contracts, schemas, validators, and tests. |
| Confirm fixture inventory and CI wiring. | **NEEDS VERIFICATION** | Repository files and successful workflow evidence. |
| Confirm cultural-care, sovereignty, sensitivity, and living-person controls. | **NEEDS VERIFICATION** | Policy references, code, tests, and review receipts. |

---

## Maintainer rule

Keep this namespace inert, small, deterministic, and easy to remove. Compatibility is not authority. Source access is not activation. Metadata is not verified history. Connector output is not publication.

[Back to top ↑](#top)

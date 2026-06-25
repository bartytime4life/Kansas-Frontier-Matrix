<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-object-map
title: contracts/OBJECT_MAP.md — Contract Object Map
version: v0.1
status: draft; repo-facing; object-map; evidence-limited; not-complete-inventory
type: index; crosswalk; governance-map
owners: OWNER_TBD — Contracts steward · Schema steward · Policy steward · Evidence steward · Runtime steward · Release steward · UI steward · Domain stewards · Docs steward
created: NEEDS VERIFICATION — scaffold existed before v0.1 expansion
updated: 2026-06-24
policy_label: public; contracts; object-map; crosswalk; evidence-first; no-parallel-authority
tags: [kfm, contracts, object-map, schemas, fixtures, validators, policy, emitted-instances, EvidenceBundle, SourceDescriptor, RuntimeResponseEnvelope, ReleaseManifest, UI, domains]
related:
  - ./README.md
  - ./domains/README.md
  - ./v1/README.md
  - ./v1/domains/README.md
  - ./ui/README.md
  - ./source/README.md
  - ./runtime/README.md
  - ./policy/README.md
  - ./release/README.md
  - ./evidence/README.md
  - ../schemas/contracts/v1/
  - ../policy/
  - ../fixtures/
  - ../tests/
  - ../tools/validators/
  - ../release/
  - ../data/
notes:
  - "Expanded from a scaffold containing only the crosswalk purpose line."
  - "This map is not a generated full repository inventory; it records paths verified or recently touched in the current documentation sequence."
  - "Contracts define semantic meaning. Schemas define machine shape. Policy defines admissibility. Fixtures/tests/validators prove enforcement. Data/release roots govern emitted instances and publication."
  - "Rows marked PROPOSED or NEEDS VERIFICATION must not be treated as implemented behavior."
  - "Rollback target for this expansion is previous scaffold blob SHA `47f033409aa0f05c467fb125bf47ac6e1579e9f2`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Contract Object Map

> Crosswalk from contract documents to schema paths, fixture roots, validator paths, policy homes, and emitted-instance homes. This is a governed maintainer map, not a complete generated inventory and not implementation proof.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts-blue">
  <img alt="Scope: evidence-limited" src="https://img.shields.io/badge/scope-evidence__limited-orange">
  <img alt="Boundary: map not authority" src="https://img.shields.io/badge/boundary-map__not__authority-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite__or__abstain-green">
</p>

**Status:** draft / evidence-limited  
**Path:** `contracts/OBJECT_MAP.md`  
**Purpose:** help maintainers find the correct companion roots for contract objects  
**Truth posture:** CONFIRMED scaffold existed · CONFIRMED contract root says contracts define meaning and schemas define shape · CONFIRMED domain and UI lanes define semantic-contract boundaries · CONFIRMED versioned `contracts/v1/` paths are currently compatibility guards · NEEDS VERIFICATION for full object inventory, schema coverage, fixture coverage, validators, policy bundles, emitted-instance homes, CI behavior, and release state.

**Quick jumps:** [Rules](#rules) · [Root crosswalk](#root-crosswalk) · [Object map](#object-map) · [Compatibility guards](#compatibility-guards) · [How to add a row](#how-to-add-a-row) · [Validation backlog](#validation-backlog) · [Rollback](#rollback)

---

## Rules

1. **Contract Markdown defines meaning.** It does not validate, execute, publish, prove, or render.
2. **Schema paths define shape.** A contract row may reference a schema path without proving the schema is mature.
3. **Policy roots define admissibility.** A contract row must not imply policy allow/deny behavior unless policy evidence is verified.
4. **Fixtures, tests, and validators prove enforcement.** Until verified, mark them `NEEDS VERIFICATION`.
5. **Emitted instances do not live in contracts.** Instances belong under data/proof/release/runtime/API roots according to lifecycle and release state.
6. **Compatibility guards are not canonical homes.** They prevent drift while preserving rollback.

---

## Root crosswalk

| Responsibility | Primary root | What belongs there |
|---|---|---|
| Semantic meaning | `contracts/` | Human-readable contract Markdown. |
| Domain object meaning | `contracts/domains/<domain>/` | Domain-specific object semantics. |
| Cross-family object meaning | `contracts/<family>/` | Non-domain-specific semantic contracts. |
| Machine shape | `schemas/contracts/v1/...` | JSON Schema and machine field shape. |
| Policy/admissibility | `policy/` | Allow, deny, restrict, abstain, sensitivity, rights, and release gates. |
| Fixtures | `fixtures/` | Valid, invalid, golden, and negative examples. |
| Tests/validators | `tests/`, `tools/validators/` | Enforcement proof and validation tooling. |
| Source authority | source registry / source catalog / `data/registry/sources/...` | SourceDescriptor and source admission metadata. |
| Evidence/proof | `data/proofs/` or accepted proof roots | EvidenceBundle, receipts, and proof records. |
| Runtime results | governed runtime/API roots | Runtime envelopes and response instances. |
| Release/correction/rollback | `release/` and release contracts | ReleaseManifest, correction, withdrawal, rollback state. |
| Data lifecycle | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/published` | Governed lifecycle products. |

---

## Object map

### Source contracts

| Object or lane | Contract doc | Schema path | Fixtures | Validator | Policy | Emitted-instance home | Status |
|---|---|---|---|---|---|---|---|
| `SourceDescriptor` | `contracts/source/source_descriptor.md` | `schemas/contracts/v1/source/source_descriptor.schema.json` | `fixtures/contracts/v1/source/source_descriptor/` | `tools/validators/validate_source_descriptor.py` | `policy/source/` | source registry / source catalog roots | Contract and schema CONFIRMED; emitted homes NEED VERIFICATION. |
| `IngestReceipt` | `contracts/source/ingest_receipt.md` | `schemas/contracts/v1/source/ingest_receipt.schema.json` | `fixtures/source/ingest_receipt/` | validator path NEEDS VERIFICATION | source policy roots | receipt/provenance roots | Contract CONFIRMED; enforcement NEEDS VERIFICATION. |
| `DoctrineArtifactDescriptor` | `contracts/source/doctrine_artifact_descriptor.md` | `schemas/contracts/v1/source/doctrine_artifact_descriptor.schema.json` | fixtures NEEDS VERIFICATION | validator NEEDS VERIFICATION | source/docs policy roots | doctrine/source catalog roots | Contract and schema CONFIRMED; enforcement NEEDS VERIFICATION. |

### UI contracts

| Object or lane | Contract doc | Schema path | Fixtures | Validator | Policy | Emitted-instance home | Status |
|---|---|---|---|---|---|---|---|
| UI lane | `contracts/ui/README.md` | `schemas/contracts/v1/ui/` | `fixtures/ui/` | `tools/validators/ui/` | `policy/ui/` | governed UI/runtime projections | Lane guide CONFIRMED; implementation NEEDS VERIFICATION. |
| `EvidenceDrawerPayload` | `contracts/ui/evidence_drawer_payload.md` | `schemas/contracts/v1/ui/evidence_drawer_payload.schema.json` | `fixtures/ui/evidence_drawer_payload/` | `tools/validators/ui/validate_evidence_drawer_payload.py` | `policy/ui/`, `policy/evidence/` | governed Evidence Drawer payload projection | Contract and schema stub CONFIRMED; enforcement NEEDS VERIFICATION. |
| `CitationValidationReport` | `contracts/ui/citation_validation_report.md` | `schemas/contracts/v1/ui/citation_validation_report.schema.json` | `fixtures/ui/citation_validation_report/` | `tools/validators/ui/validate_citation_validation_report.py` | `policy/ui/`, `policy/evidence/` | governed citation report projection | Contract and schema stub CONFIRMED; evidence-family authority separate. |
| `FocusRequest` | `contracts/ui/focus_request.md` | `schemas/contracts/v1/ui/focus_request.schema.json` | `fixtures/ui/focus_request/` | `tools/validators/ui/validate_focus_request.py` | `policy/ui/`, `policy/focus/` | governed runtime request input | Contract and schema stub CONFIRMED; runtime behavior NEEDS VERIFICATION. |
| `FocusResponse` | `contracts/ui/focus_response.md` | `schemas/contracts/v1/ui/focus_response.schema.json` | `fixtures/ui/focus_response/` | `tools/validators/ui/validate_focus_response.py` | `policy/ui/`, `policy/focus/` | UI projection over runtime response | Contract and schema stub CONFIRMED; runtime authority remains separate. |
| `StoryManifest` | `contracts/ui/story_manifest.md` | `schemas/contracts/v1/ui/story_manifest.schema.json` | `fixtures/ui/story_manifest/` | validator NEEDS VERIFICATION | `policy/ui/`, `policy/story/` | governed story display manifest | Contract and schema stub CONFIRMED; story/release behavior NEEDS VERIFICATION. |
| `StoryNode` | `contracts/ui/story_node.md` | `schemas/contracts/v1/ui/story_node.schema.json` | `fixtures/ui/story_node/` | validator NEEDS VERIFICATION | `policy/ui/`, `policy/story/` | governed story-node projection | Contract and schema stub CONFIRMED; story player behavior NEEDS VERIFICATION. |
| `TrustBadgeState` | `contracts/ui/trust_badge_state.md` | `schemas/contracts/v1/ui/trust_badge_state.schema.json` | `fixtures/ui/trust_badge_state/` | validator NEEDS VERIFICATION | `policy/ui/` | trust-visible UI badge projection | Contract and schema stub CONFIRMED; badge implementation NEEDS VERIFICATION. |
| `UIEvent` | `contracts/ui/ui_event.md` | `schemas/contracts/v1/ui/ui_event.schema.json` | `fixtures/ui/ui_event/` | validator NEEDS VERIFICATION | `policy/ui/` | governed UI/runtime/telemetry-adjacent event carrier | Contract and schema stub CONFIRMED; telemetry/runtime wiring NEEDS VERIFICATION. |

### Runtime, policy, release, evidence lanes

| Lane | Contract docs | Schema path | Fixtures/tests/validators | Policy | Emitted-instance home | Status |
|---|---|---|---|---|---|---|
| Runtime | `contracts/runtime/` | `schemas/contracts/v1/runtime/` | runtime fixtures/tests/validators NEEDS VERIFICATION | `policy/runtime/` | governed runtime/API outputs | Multiple contracts CONFIRMED; implementation NEEDS VERIFICATION. |
| Policy | `contracts/policy/` | `schemas/contracts/v1/policy/` | policy fixtures/tests NEEDS VERIFICATION | `policy/` | policy decisions / policy outputs | Contracts CONFIRMED; executable policy behavior NEEDS VERIFICATION. |
| Release | `contracts/release/` | `schemas/contracts/v1/release/` | release fixtures/tests NEEDS VERIFICATION | release policy roots | `release/` | Contracts CONFIRMED; release state still evidence-gated. |
| Evidence | `contracts/evidence/` | `schemas/contracts/v1/evidence/` | evidence fixtures/tests NEEDS VERIFICATION | `policy/evidence/` | proof/evidence roots | Evidence-family contracts exist; proof closure not proven by this map. |

### Domain lanes

| Domain lane | Contract doc or README | Schema path | Fixtures/tests | Policy | Emitted-instance home | Status |
|---|---|---|---|---|---|---|
| Domain root | `contracts/domains/README.md` | `schemas/contracts/v1/...` | `fixtures/domains/`, `tests/domains/` | `policy/domains/` | data/proof/release roots by domain | Active semantic-contract root CONFIRMED. |
| Atmosphere | `contracts/domains/atmosphere/README.md` | `schemas/contracts/v1/domains/atmosphere/` | `fixtures/domains/atmosphere/`, `tests/domains/atmosphere/` | `policy/domains/atmosphere/` | Atmosphere data/proof/release roots | Active lane CONFIRMED; slug drift with `air` remains NEEDS ADR/VERIFICATION. |

---

## Compatibility guards

| Guard path | Points to | Why it exists | Status |
|---|---|---|---|
| `contracts/v1/README.md` | `contracts/` and `schemas/contracts/v1/` | Prevents versioned contract root from mirroring schemas or becoming parallel authority. | CONFIRMED guard. |
| `contracts/v1/domains/README.md` | `contracts/domains/` | Prevents versioned domain branch from becoming a second domain-contract root. | CONFIRMED guard. |
| `contracts/v1/domains/atmosphere/README.md` | `contracts/domains/atmosphere/` | Prevents versioned atmosphere branch from becoming parallel authority and records naming drift. | CONFIRMED guard. |
| `contracts/atmosphere/README.md` | `contracts/domains/atmosphere/` after ADR review | Compatibility/path-conflict surface for atmosphere/air drift. | CONFIRMED compatibility README. |
| `contracts/air/README.md` | atmosphere/air contract lane after ADR review | Air slug compatibility surface. | CONFIRMED by repo search; full status NEEDS VERIFICATION. |

---

## How to add a row

Before adding an object row:

1. Fetch the contract file and confirm it exists.
2. Fetch or search the paired schema path.
3. Identify fixture, validator, and policy homes from schema metadata or lane README.
4. Mark unverified companion paths as `NEEDS VERIFICATION`.
5. Identify emitted-instance home by responsibility root, not convenience.
6. Add rollback target if the map row changes authority posture.
7. Do not list generated guesses as CONFIRMED.

---

## Validation backlog

- [ ] Generate a full repo inventory for all `contracts/**/*.md` files.
- [ ] Join every contract to a schema path and schema status.
- [ ] Join every schema to fixtures, validators, policy roots, and tests.
- [ ] Identify duplicate/compatibility/parallel authority paths.
- [ ] Produce drift register entries for unresolved contract/schema/policy homes.
- [ ] Add CI validation that prevents unreviewed contract rows from claiming implementation maturity.

## Rollback

Rollback is required if this map becomes an implementation inventory, canonical schema registry, policy registry, release registry, proof store, source registry, public API contract, or generated truth source.

Rollback target for this expansion: previous scaffold blob SHA `47f033409aa0f05c467fb125bf47ac6e1579e9f2`.

<p align="right"><a href="#top">Back to top</a></p>

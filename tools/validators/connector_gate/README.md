<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-connector-gate-readme
title: tools/validators/connector_gate README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-connector-steward-plus-source-steward-plus-rights-steward-plus-sensitivity-steward-plus-policy-steward-plus-evidence-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; connector-gate-validator; source-admission; pre-RAW; fail-closed; rights-aware; sensitivity-aware; source-role-aware; non-authoritative
owning_root: tools/
responsibility: proposed connector-gate validator lane for checking connector preflight, source descriptor resolution, source-head posture, rights/access/cadence/citation/sensitivity posture, source-role and authority limits, credential/secret denial, network/intake boundary, RAW/WORK/QUARANTINE routing, finite negative outcomes, receipt/report destinations, policy linkage, evidence linkage, release linkage, correction and rollback linkage, and public-surface denial checks while deferring connector implementation, source registry authority, evidence records, policy decisions, receipts, release authority, and public outputs to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../sources/README.md
  - ../citation/README.md
  - ../evidence/README.md
  - ../../contracts/source/source_descriptor.md
  - ../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../schemas/contracts/v1/sources/source_descriptor.schema.json
  - ../../data/registry/sources/README.md
  - ../../docs/sources/ADMISSION_PROCESS.md
  - ../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../docs/runbooks/FIRST_INGEST.md
  - ../../docs/architecture/source-roles.md
  - ../../docs/architecture/source-role-anti-collapse.md
  - ../../data/raw/
  - ../../data/work/
  - ../../data/quarantine/
  - ../../data/processed/
  - ../../data/proofs/
  - ../../data/receipts/
  - ../../policy/source/
  - ../../policy/rights/
  - ../../policy/sensitivity/
  - ../../release/
notes:
  - "This README replaces a stray one-character file. It does not confirm executable files."
  - "No exact connector_gate evidence was found by repository search during this task. Connector-gate behavior in this README is therefore PROPOSED and must be verified before implementation claims."
  - "Source registry evidence says data/registry/sources/ is the pre-RAW admission membrane and that nothing should enter data/raw/ without a resolvable SourceDescriptor."
  - "SourceDescriptor evidence says source metadata records how a source may be treated, but does not make source claims true, authorize release, replace evidence, decide policy, or allow connectors/watchers/pipelines to bypass review."
  - "Connector gates must never store secrets, decide source admission alone, publish source data, create EvidenceBundles, decide policy, approve release, or expose public outputs."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/connector_gate

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-connector--gate--validator-informational)
![posture](https://img.shields.io/badge/posture-fail--closed-critical)
![boundary](https://img.shields.io/badge/boundary-pre--RAW--gate-blueviolet)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/connector_gate/` is the proposed validator lane for checking whether a connector or intake candidate is allowed to proceed toward RAW, WORK, or QUARANTINE based on SourceDescriptor, rights, sensitivity, access, cadence, citation, source-head, policy, receipt, evidence, and release posture.

---

## Purpose

`tools/validators/connector_gate/` exists for connector preflight and intake-gate validation under the durable `tools/validators/` surface.

The durable KFM question for this lane is:

> Before a connector, watcher, local upload, manual intake, or source-refresh job moves material toward a lifecycle lane, does it resolve an admitted SourceDescriptor, preserve source role and authority limits, respect rights/access/cadence/citation/sensitivity posture, avoid secrets, choose a valid RAW/WORK/QUARANTINE route, emit finite negative outcomes when blocked, and avoid bypassing policy, evidence, release, correction, rollback, or public-surface gates?

The answer should be a deterministic validation result. This folder should not run connectors, store connector payloads, store secrets, admit sources by itself, create SourceDescriptors, create EvidenceBundles, store receipts, decide policy, approve release, publish public map/API/UI/AI outputs, or convert connector output into truth.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/connector_gate/README.md` | **CONFIRMED** | This README replaces a stray one-character file. |
| Exact `connector_gate` doctrine or implementation | **NOT FOUND in this task** | Repository search did not find exact connector-gate docs or executables. This README is a proposed validator-lane contract. |
| Source registry admission boundary | **CONFIRMED in repo evidence / draft** | `data/registry/sources/README.md` defines the source registry as the pre-RAW admission membrane and says nothing should enter `data/raw/` without a resolvable SourceDescriptor. |
| SourceDescriptor contract | **CONFIRMED in repo evidence / draft** | `contracts/source/source_descriptor.md` says SourceDescriptor records how a source may be treated and does not make claims true, authorize release, replace evidence/policy/review/validation/source registry/release artifacts, or allow connectors/watchers/pipelines to bypass review. |
| Executable, connector inventory, schemas, fixtures, policy bundles, receipt emission, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This README does not claim a connector-gate executable, fixture set, report schema, receipt path, runtime route, or CI check exists. |

[Back to top](#top)

---

## Relationship to nearby lanes

| Concern | Preferred home |
|---|---|
| Connector-gate validator lane | `tools/validators/connector_gate/` |
| Shared validator plumbing | `tools/validators/_common/` |
| SourceDescriptor validation | `tools/validators/sources/` or accepted source validator lane |
| Citation/evidence validation | `tools/validators/citation/`, `tools/validators/evidence/`, `tools/validators/evidence_bundle/` |
| SourceDescriptor semantics | `contracts/source/source_descriptor.md` |
| SourceDescriptor machine shape | `schemas/contracts/v1/source/`, `schemas/contracts/v1/sources/` |
| Source registry/admission state | `data/registry/sources/` |
| Connector implementation | `connectors/`, `pipelines/`, `packages/`, or accepted implementation root after verification |
| Lifecycle payloads | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/` |
| Rights, source, and sensitivity policy | `policy/source/`, `policy/rights/`, `policy/sensitivity/`, or accepted policy homes |
| Receipts and proof support | `data/receipts/`, `data/proofs/` |
| Release, corrections, rollback, withdrawal | `release/` |

This README does not move, replace, or override those roots. It only defines where connector preflight/intake-gate validation may be documented or implemented after verification.

[Back to top](#top)

---

## Proposed validation focus

Until executable behavior and connector inventories are verified, this README treats the following as proposed validation concepts:

| Concept | Validator question | Must not be treated as |
|---|---|---|
| SourceDescriptor resolution | Does the connector/intake candidate resolve a current SourceDescriptor? | Source truth, source admission by itself, or release approval. |
| Connector identity | Is the connector, watcher, local upload, or manual intake path declared and scoped? | Authority to fetch or publish anything. |
| Access posture | Are authentication, rate limits, endpoint terms, access method, and credential posture safe? | A place to store secrets or credentials. |
| Rights and sensitivity | Do rights, attribution, redistribution, license, embargo, sensitivity, and geoprivacy defaults permit the requested action? | Policy approval by metadata alone. |
| Source role and authority limits | Are allowed/prohibited claim families and source roles preserved? | Claim truth or cross-domain authority. |
| Source-head posture | Are source version, ETag, checksum, timestamp, content identity, or equivalent head checks present where configured? | EvidenceBundle closure. |
| Lifecycle route | Is the intended route RAW, WORK, QUARANTINE, or HOLD/DENY/ABSTAIN/ERROR? | Publication or release. |
| Receipt/report destination | Are preflight/intake reports and receipts routed to accepted roots? | Proof storage unless accepted. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Connector-gate validator lane | `tools/validators/connector_gate/` |
| Shared validator plumbing | `tools/validators/_common/` |
| SourceDescriptor contract | `contracts/source/source_descriptor.md` |
| SourceDescriptor schemas | `schemas/contracts/v1/source/`, `schemas/contracts/v1/sources/` |
| Source registry/admission records | `data/registry/sources/` |
| Connector implementations | `connectors/`, `pipelines/`, `packages/`, or accepted implementation roots |
| Lifecycle payloads | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/` |
| Policy/admissibility | `policy/source/`, `policy/rights/`, `policy/sensitivity/`, `policy/` |
| Evidence/proof support | `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, correction, rollback, withdrawal | `release/` |
| Tests and fixtures | `tests/validators/connector_gate/`, `tests/connectors/`, `fixtures/connectors/`, `fixtures/source/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it checks declared connector-gate, SourceDescriptor, policy, lifecycle-route, evidence-linkage, receipt, and release-reference rules and writes reports/receipts only to accepted roots.
- **NEEDS VERIFICATION:** exact executable names, connector inventory, connector root maturity, schemas, fixtures, report shape, receipt emission, policy integration, source-head behavior, runtime behavior, and CI wiring.
- **DENY:** using this folder as connector runtime, credential store, source registry, SourceDescriptor store, schema home, policy home, source payload store, proof storage, receipt storage, release record store, public runtime surface, AI answer authority, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/connector_gate/` include checks that:

- verify a connector/intake candidate has a resolvable SourceDescriptor before any material enters `data/raw/`;
- verify the connector is allowed to use the declared access method without storing secrets or leaking credentials;
- verify rights, terms, attribution, redistribution, sensitivity, geoprivacy, embargo, cadence, and source-head posture before fetch/intake;
- verify source role, authority rank, allowed/prohibited claim families, and cross-domain limits remain visible;
- verify source-head checks such as ETag, checksum, modified time, content length, digest, or equivalent are captured where configured;
- verify blocked candidates return `DENY`, `HOLD`, `ABSTAIN`, or `ERROR` instead of silently fetching, transforming, or publishing;
- verify intake outputs route to RAW, WORK, QUARANTINE, or denial/hold with receipts and reports in accepted roots;
- emit deterministic findings for downstream review without running the connector, storing payloads, or approving release.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/connector_gate/` | Correct home |
|---|---|
| Connector implementation, fetchers, parsers, watchers, or ETL | `connectors/`, `pipelines/`, `packages/`, or accepted implementation roots |
| Secrets, credentials, API keys, tokens, cookies, session data | secret manager / environment configuration; never repository text |
| SourceDescriptor records or source registry records | `data/registry/sources/` |
| SourceDescriptor meaning/contracts | `contracts/source/` |
| SourceDescriptor schemas/enums | `schemas/contracts/v1/source/`, `schemas/contracts/v1/sources/` |
| Policy rules and sensitivity/admissibility decisions | `policy/` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| EvidenceBundles, proofs, receipts, ValidationReports, IngestReceipts | `data/proofs/`, `data/receipts/` |
| Release manifests, correction notices, rollback cards, withdrawals | `release/` |
| Public API, UI, map, tile, export, search, graph, Focus Mode, AI runtime output | governed application/runtime roots |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and fixture conventions |

[Back to top](#top)

---

## Connector-gate validator posture

Connector-gate validators must fail closed, deny, abstain, hold, or route to review when a candidate:

- lacks a resolvable SourceDescriptor or source registry admission state;
- lacks allowed source role, authority limit, access method, rights posture, sensitivity posture, citation posture, cadence posture, source-head posture, review state, or lifecycle route required for the requested action;
- attempts to store or expose credentials, secrets, session material, or private connector configuration in the repository;
- attempts to fetch, transform, or admit material before rights, sensitivity, source-role, or policy gates are satisfied;
- attempts to bypass RAW / WORK / QUARANTINE routing or writes directly to PROCESSED, CATALOG, TRIPLET, PUBLISHED, proof, release, public API, or AI surfaces;
- treats connector output, source metadata, source-head checks, or successful fetch as EvidenceBundle closure, truth, policy approval, release approval, or public safety;
- emits reports, receipts, or findings outside accepted roots;
- treats validator output as source admission, EvidenceBundle creation, PolicyDecision creation, release approval, publication, public API behavior, or AI answer authority.

The validator lane must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `CONNECTOR_GATE_PASS` | Configured connector-gate checks passed. |
| `CONNECTOR_GATE_FAIL` | One or more configured connector-gate checks failed. |
| `CONNECTOR_UNKNOWN` | Connector or intake lane is not recognized by configured registry. |
| `SOURCE_DESCRIPTOR_MISSING` | Required SourceDescriptor or source-registry pointer is absent. |
| `SOURCE_DESCRIPTOR_UNRESOLVED` | SourceDescriptor cannot be resolved safely. |
| `SOURCE_NOT_ADMITTED` | Source is draft, denied, retired, superseded, embargoed, or not admitted for requested use. |
| `SOURCE_ROLE_GAP` | Required source-role or authority-limit posture is missing. |
| `RIGHTS_OR_ACCESS_GAP` | Rights, access, attribution, redistribution, terms, or credential posture blocks intake. |
| `SENSITIVITY_GATE_DENIED` | Sensitivity, geoprivacy, or exposure posture denies the requested action. |
| `SOURCE_HEAD_MISSING` | Required source-head, checksum, digest, ETag, timestamp, or equivalent identity check is absent. |
| `SECRET_EXPOSURE_RISK` | Candidate appears to expose credentials, secrets, tokens, cookies, or private connector configuration. |
| `LIFECYCLE_ROUTE_INVALID` | Candidate writes to an invalid lifecycle state or bypasses RAW/WORK/QUARANTINE gates. |
| `CONNECTOR_OUTPUT_AS_TRUTH_DENIED` | Candidate treats connector output or successful fetch as truth/evidence/release approval. |
| `REPORT_DESTINATION_INVALID` | QA report or receipt destination is outside an accepted root. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `DENY` | Candidate is explicitly disallowed for the requested use. |
| `HOLD` | Candidate requires steward review, source admission, closure, or quarantine before use. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/connector_gate/
├── README.md
├── test_connector_gate.py
└── fixtures/
    ├── valid_admitted_source_preflight/
    ├── missing_source_descriptor/
    ├── unresolved_source_descriptor/
    ├── source_not_admitted/
    ├── rights_or_access_gap/
    ├── sensitivity_gate_denied/
    ├── missing_source_head/
    ├── secret_exposure_risk/
    ├── lifecycle_route_invalid/
    └── connector_output_as_truth_denied/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/connector_gate
```

```bash
python tools/validators/connector_gate/validate_connector_gate.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `validate_connector_gate.py` or the test path exists here.

[Back to top](#top)

---

## Review checklist

- [ ] Validator reads declared SourceDescriptor contracts, schemas, source registry records, source-role rules, and policy rather than defining meaning locally.
- [ ] Connector code, source registry records, SourceDescriptors, policy decisions, receipts, evidence, and release records remain separate.
- [ ] Credentials and secrets are never accepted in repo text, fixtures, reports, receipts, or validator output.
- [ ] Source role, authority limits, rights, sensitivity, cadence, access method, citation, source-head, review, and lifecycle route remain visible.
- [ ] Blocked sources produce finite negative outcomes rather than silent fetch, transform, or public exposure.
- [ ] Public-bound outputs never point clients at RAW, WORK, QUARANTINE, unresolved candidates, direct connector output, direct internal stores, direct model outputs, or incomplete proof closure.
- [ ] Reports and receipts are written only to accepted roots.
- [ ] Validator output is not described as truth, policy, release, publication, source admission, connector success, or Directory Rules approval.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-08 |
| Review state | Draft README replacement for stray one-character Connector Gate validator file. |
| Next smallest safe change | Verify actual connector-gate validator script path, connector inventory, accepted connector roots, SourceDescriptor schema binding, fixtures, report destination, receipt emission, policy enforcement, source-head behavior, lifecycle routing behavior, release linkage, and CI/runtime wiring before promoting this lane beyond draft. |

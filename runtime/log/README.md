<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runtime-log-readme
title: runtime/log/ — Runtime Log Compatibility, Review, and Handoff Index
type: readme; directory-readme; compatibility-index; runtime-observability-handoff-boundary
version: v1.1
status: draft; repository-grounded; path-canonicality-conflicted; README-only; no-log-store; no-receipt-authority; no-public-path; implementation-unconfirmed
owners: OWNER_TBD — Runtime steward · Observability steward · Receipt steward · Security and privacy steward · Policy steward · Evidence steward · Validation steward · Operations steward · Release steward · Migration steward · Docs steward
created: NEEDS VERIFICATION — blank file was replaced by v1 on 2026-07-03
updated: 2026-07-15
supersedes: v1 runtime review-notes guide
policy_label: "restricted-review; runtime; logs; observability; compatibility-index; no-raw-log-store; no-secret-store; no-receipt-authority; no-evidence-authority; no-release-authority; no-public-path; redaction-first; retention-aware; rollback-aware"
current_path: runtime/log/README.md
truth_posture: >
  CONFIRMED target v1 README and prior blob; current canonical runtime root; current governed
  local-runtime coordination lane; Directory Rules v1.4 canonical runtime tree omitting log/;
  receipt process-memory root; telemetry receipt lane; telemetry carrier-not-truth posture;
  current target path search; and current repository documentation boundaries /
  PROPOSED bounded runtime review-note profile, pointer-only log digest, handoff checklist,
  finite review states, retention classification, correction and migration process /
  CONFLICTED repository-present runtime/log path versus omission from the Directory Rules
  canonical runtime tree, plus the path name "log" suggesting an operational log store while
  the current safe role is compatibility, review, and handoff only /
  UNKNOWN raw-log backend, collectors, exporters, sinks, storage, retention enforcement,
  redaction pipeline, access control, alerting, dashboards, on-call integration, executable
  runtime log emission, receipt creation, tests, CI, deployment, operational health, and
  current production use /
  NEEDS VERIFICATION accepted owners, CODEOWNERS coverage, retention or migration decision,
  inbound-link inventory, note identity scheme, sensitivity labels, private telemetry system,
  receipt handoff contract, validation, correction propagation, and rollback automation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 21e44bb292afe8227a08b08b47683e581e92fc5b
  prior_blob: cb20b50f682656e083e86b41049cc885233b63f7
  runtime_root_blob: 894d15bb2e2d0185f433e35c690e0a6b42327fb9
  runtime_local_blob: bab47e442500cd84d3e840373ac2a9fd6126d74b
  receipts_root_blob: 6fdaab9348102e37591962e742a00452bc95f59c
  telemetry_receipts_blob: d98cf13b34d85838326b60a48f4b9c9c0a92bb03
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
related:
  - ../README.md
  - ../local/README.md
  - ../envelopes/README.md
  - ../service_configs/README.md
  - ../../data/receipts/README.md
  - ../../data/receipts/telemetry/README.md
  - ../../contracts/telemetry/README.md
  - ../../schemas/contracts/v1/telemetry/README.md
  - ../../docs/standards/TELEMETRY_MINIMUMS.md
  - ../../docs/adr/ADR-0016-telemetry-redaction-posture.md
  - ../../docs/dashboards/README.md
  - ../../docs/dashboards/DASHBOARD_CATALOG.md
  - ../../docs/security/SECRETS.md
  - ../../docs/security/INCIDENT_RESPONSE.md
  - ../../policy/runtime/README.md
  - ../../policy/sensitivity/README.md
  - ../../tests/
  - ../../tools/validators/
  - ../../release/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/registers/DRIFT_REGISTER.md
tags: [kfm, runtime, log, observability, compatibility-index, review-notes, telemetry, receipts, redaction, retention, no-secrets, no-public-path, migration, rollback]
notes:
  - "This revision changes only runtime/log/README.md."
  - "The lane remains a compatibility and handoff index. It is not confirmed as a canonical runtime lane and must not become a raw-log store."
  - "Durable process-memory receipts belong under data/receipts/; raw logs and telemetry payloads belong only in an approved private operational system; dashboards belong under docs/dashboards/."
  - "No runtime emitter, collector, exporter, sink, backend, alert, dashboard, receipt, validator, test, workflow, deployment, release record, or public route is created."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `runtime/log/` — Runtime Log Compatibility, Review, and Handoff Index

> **One-line purpose.** Preserve a bounded compatibility and review index for runtime logging and observability handoffs while keeping raw logs in approved private operational systems, durable process memory in governed receipt lanes, dashboards in documentation or approved observability surfaces, and evidence, policy, release, correction, and public authority outside this path.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Version: v1.1" src="https://img.shields.io/badge/version-v1.1-informational">
  <img alt="Lane: compatibility index" src="https://img.shields.io/badge/lane-compatibility__index-orange">
  <img alt="Storage: no raw logs" src="https://img.shields.io/badge/storage-no__raw__logs-critical">
  <img alt="Receipts: data receipts" src="https://img.shields.io/badge/receipts-data%2Freceipts-blue">
  <img alt="Public access: denied" src="https://img.shields.io/badge/public__access-denied-red">
</p>

> [!IMPORTANT]
> **`runtime/log/` is not a canonical runtime implementation lane and is not a log backend.** Directory Rules name `local/`, `model_adapters/`, `ollama/`, `mock/`, `service_configs/`, and `envelopes/` as canonical runtime sublanes; `log/` is repository-present but omitted. Until a governed placement decision is made, use this path only for compatibility, review, bounded handoff notes, migration records, and links to the systems that actually own logs, telemetry, receipts, dashboards, policy, and release.

> [!CAUTION]
> **Do not commit raw logs, traces, dumps, prompts, request bodies, stack traces, tokens, credentials, private endpoints, protected coordinates, living-person data, DNA or genomic material, precise sensitive locations, secret-bearing configuration, or restricted EvidenceBundle content.** Redaction, minimization, access control, retention, deletion, and incident response apply before any operational material leaves its approved private system.

> [!WARNING]
> **A log line is not evidence, a telemetry event is not truth, and a receipt is not proof or release.** Operational signals may support diagnosis and governance, but they cannot establish a domain claim, approve disclosure, close evidence, promote lifecycle state, authorize release, or become a direct public source.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Does not](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Boundaries](#logging-telemetry-receipt-and-dashboard-boundaries) · [Review notes](#bounded-runtime-review-note) · [Security](#security-privacy-redaction-and-retention) · [Failures](#finite-review-and-handoff-states) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Migration](#migration-correction-and-rollback) · [Open](#open-verification-register) · [Last reviewed](#last-reviewed)

---

## Purpose

`runtime/log/` is a **compatibility, review, and handoff index** for runtime logging and observability concerns that need a visible repository pointer but do not belong in canonical runtime implementation, lifecycle data, receipts, dashboards, contracts, schemas, policy, release, or public output.

This lane may help maintainers answer:

1. Which runtime component or run produced the operational signal?
2. Which approved private log or telemetry system owns the raw record?
3. Which redaction, sensitivity, access, retention, and deletion rules apply?
4. Which bounded digest or review summary is safe to record in Git?
5. Which receipt, validation, dashboard, incident, correction, or rollback record should receive the handoff?
6. Which negative state applies when support is missing, sensitive, stale, inaccessible, or unsafe?
7. Should the note remain here, move to another responsibility lane, or be retired?

This README does **not** establish that KFM currently has a runtime logger, collector, exporter, sink, backend, dashboard, alert router, on-call integration, retention engine, redaction engine, receipt emitter, or production deployment.

[Back to top](#top)

---

## Authority level

**Compatibility index / non-authoritative runtime-observability handoff.**

| Concern | Owning authority | `runtime/log/` role |
|---|---|---|
| Canonical runtime wiring | canonical runtime sublanes | References the component; does not implement it. |
| Raw logs, traces, metrics, events, crash dumps | approved private operational system | Stores no payload; records only a safe pointer or bounded digest. |
| Durable process memory | `data/receipts/` | Hands off to an accepted receipt family. |
| Telemetry process-memory receipts | `data/receipts/telemetry/` | References receipt IDs or expected handoff only. |
| Telemetry semantics | `contracts/telemetry/` | References canonical meaning. |
| Machine shape | accepted schema roots | References schemas; does not define them. |
| Telemetry minimums and redaction posture | standards, ADRs, and policy roots | Obeys them; does not replace them. |
| Dashboards and dashboard catalog | `docs/dashboards/` or accepted observability roots | Links to approved dashboard documentation. |
| Alerts, runbooks, on-call, incident handling | accepted operations and security roots | Links to approved procedures. |
| Evidence and proof | governed evidence/proof roots | May reference support; cannot create or close it. |
| Release, correction, withdrawal, rollback | `release/` | Cannot authorize any transition. |
| Public API, UI, map, search, or generated answer | governed application/public roots | No direct read path from this lane. |

### Anti-collapse rules

This lane must not collapse:

- raw operational logs into Git-tracked documentation;
- runtime logs into receipts;
- receipts into proofs;
- telemetry into evidence;
- dashboards into release authority;
- health into policy admission;
- incident diagnostics into public content;
- generated summaries into steward review;
- successful execution into lifecycle promotion;
- a path existing into canonical placement.

[Back to top](#top)

---

## Status

### Confirmed repository evidence

| Surface | Status | Safe conclusion |
|---|---:|---|
| `runtime/log/README.md` | **CONFIRMED** | The target README exists; its prior blob is recorded above. |
| `runtime/log/` canonicality | **CONFLICTED** | The path exists, but Directory Rules do not list it in the canonical runtime tree. |
| Target inventory | **README-only in bounded evidence** | No implementation is established by this review. |
| `runtime/README.md` | **CONFIRMED canonical root** | Runtime remains internal and subordinate to evidence, policy, release, correction, and public controls. |
| `runtime/local/README.md` | **CONFIRMED canonical local coordination lane** | General local runtime coordination belongs there, not in `runtime/log/`. |
| `data/receipts/README.md` | **CONFIRMED receipt root** | Durable process memory belongs under `data/receipts/`. |
| `data/receipts/telemetry/README.md` | **CONFIRMED telemetry-receipt lane** | Telemetry receipts are process memory, not a raw-log store, proof, release, or public truth. |
| Raw logs and telemetry payload stores | **UNKNOWN** | No approved backend, collector, sink, retention, or access-control implementation is established here. |
| Tests, CI, deployment, runtime health | **UNKNOWN** | Documentation presence is not operational proof. |

### Current maturity

The safe current classification is:

```text
repository-present compatibility/index README
not a canonical runtime sublane
not a raw-log or telemetry store
not a receipt lane
not a dashboard
not operational proof
```

### Placement decision

The primary responsibility of any future artifact determines its home:

| Artifact | Correct home |
|---|---|
| Runtime component wiring | canonical `runtime/` sublane |
| Raw logs, traces, metrics, events, dumps | approved private operational system |
| Durable run or telemetry receipt | `data/receipts/` or accepted subtype lane |
| Dashboard documentation/catalog entry | `docs/dashboards/` |
| Alerting and incident procedure | accepted operations/security/runbook root |
| Contract meaning | `contracts/` |
| Machine schema | `schemas/` |
| Policy | `policy/` |
| Tests and validators | `tests/`, `fixtures/`, `tools/validators/` |
| Release/correction/rollback | `release/` |
| Public-safe output | governed application or published-data root after release |

[Back to top](#top)

---

## What belongs here

Only bounded, non-sensitive, pointer-oriented compatibility material belongs here:

- this README;
- a short compatibility pointer explaining where runtime log concerns moved;
- a bounded runtime review note that contains no raw payload;
- a migration, supersession, deprecation, or retention decision record;
- a safe handoff note to a receipt, dashboard, incident, validation, correction, or rollback record;
- stable identifiers and resolvable references to approved systems;
- non-sensitive review conclusions such as `NO_ACTION`, `HANDOFF_REQUIRED`, or `MIGRATE`;
- redaction, retention, sensitivity, and access classifications by reference;
- open verification items and ownership decisions.

A note must be small enough to inspect manually and safe enough for repository review. It should summarize **what needs attention**, not reproduce the operational record.

[Back to top](#top)

---

## What does NOT belong here

- raw log lines, full traces, metrics streams, event payloads, crash dumps, core dumps, stack traces, or CI transcripts;
- prompts, model inputs, model outputs, private reasoning, request bodies, headers, cookies, session data, or tool arguments;
- credentials, tokens, passwords, signing keys, private URLs, secret-bearing configuration, or secret-store exports;
- protected coordinates, rare-species locations, archaeology locations, infrastructure details, living-person data, DNA/genomic data, parcel-person joins, or restricted EvidenceBundle contents;
- lifecycle data payloads from `RAW`, `WORK`, `QUARANTINE`, `PROCESSED`, `CATALOG`, `TRIPLET`, or `PUBLISHED`;
- durable RunReceipt, AIReceipt, telemetry receipt, validation receipt, incident receipt, correction receipt, or rollback receipt instances;
- EvidenceBundle, ProofPack, citation closure, policy decision, release manifest, promotion decision, rollback card, or correction notice;
- contracts, schemas, policy bundles, validator code, tests, workflows, service definitions, collectors, exporters, sinks, dashboards, or alert rules;
- generated text presented as evidence, review, policy, incident resolution, or release authority;
- public API, UI, map, search, graph, vector-index, or generated-answer content;
- material whose rights, sensitivity, retention, deletion, or disclosure posture is unresolved.

[Back to top](#top)

---

## Inputs

Permitted inputs to a bounded review note are references and minimized classifications, not raw operational content:

| Input | Requirement |
|---|---|
| Runtime component reference | Must identify the owning canonical runtime lane. |
| Run or event reference | Stable ID only; no raw payload. |
| Private log-system reference | Approved system and access class; avoid secret URLs. |
| Receipt reference | Resolvable accepted receipt ID or `N/A`. |
| Validation reference | Test, validator, or report pointer. |
| Dashboard reference | Approved dashboard/catalog pointer. |
| Policy/sensitivity reference | Required when operational material may expose protected context. |
| Incident/correction/rollback reference | Required when the note concerns failure, exposure, stale state, or invalidation. |
| Time bounds | Explicit event and observation times; no vague “current” claims. |
| Reviewer identity | Named steward or `OWNER_TBD`; no invented approval. |
| Retention class | Approved class or `NEEDS VERIFICATION`. |
| Redaction class | Approved profile or `NEEDS VERIFICATION`. |

Inputs must be minimized to the decision at hand. When a pointer cannot be safely or reliably resolved, record the negative state instead of copying the source material into Git.

[Back to top](#top)

---

## Outputs

Permitted outputs are bounded review and handoff records:

- `NO_ACTION`;
- `HANDOFF_REQUIRED`;
- `NEEDS_REVIEW`;
- `REDACTION_REQUIRED`;
- `RECEIPT_REQUIRED`;
- `INCIDENT_REQUIRED`;
- `CORRECTION_REQUIRED`;
- `ROLLBACK_REQUIRED`;
- `MIGRATE`;
- `SUPERSEDED`;
- `RETIRED`;
- `ERROR`.

A note may include:

- note ID and version;
- runtime component and run references;
- observation time window;
- safe bounded summary;
- sensitivity and redaction posture;
- retention posture;
- finite review state;
- reason codes;
- receipt, validation, dashboard, incident, correction, or rollback pointers;
- reviewer and review date;
- migration or deletion decision;
- unresolved blockers.

A note must not emit a public answer, domain claim, policy decision, release decision, or operational secret.

[Back to top](#top)

---

## Logging, telemetry, receipt, and dashboard boundaries

```text
runtime component
  -> approved private log / telemetry system
  -> redaction, minimization, access, retention, and policy controls
  -> bounded review signal
  -> runtime/log compatibility note only when repository-visible coordination is needed
  -> durable process-memory handoff to data/receipts/ when applicable
  -> dashboard or incident/correction/rollback handoff when applicable
  -> no public path without governed evidence, policy, validation, review, and release
```

This is a **PROPOSED governed handoff model**, not proof that every stage is implemented.

### Raw log versus review note

| Raw operational record | Bounded review note |
|---|---|
| High volume | Small and inspectable |
| May contain sensitive context | Redacted and minimized |
| Stored in approved private system | May be Git-tracked only when safe |
| Subject to operational retention | Subject to documentation retention and correction |
| Used for diagnosis | Used for governance and handoff |
| Not a receipt by default | May point to a receipt |
| Not public | Not public authority |

### Receipt distinction

A receipt records that a governed process occurred. A runtime review note explains why maintainers need to inspect, hand off, migrate, correct, or retire a runtime-observability concern. Neither artifact is evidence closure or release authority.

### Dashboard distinction

Dashboards visualize approved telemetry or derived operational state. A dashboard screenshot or URL is not evidence, policy, release, or incident closure. Dashboard definitions and catalog entries remain outside this lane.

[Back to top](#top)

---

## Bounded runtime review note

The following profile is **PROPOSED** and non-authoritative:

```markdown
# <runtime-log-note-id>

## Status
<NO_ACTION | HANDOFF_REQUIRED | NEEDS_REVIEW | REDACTION_REQUIRED | RECEIPT_REQUIRED | INCIDENT_REQUIRED | CORRECTION_REQUIRED | ROLLBACK_REQUIRED | MIGRATE | SUPERSEDED | RETIRED | ERROR>

## Scope
- Runtime component: <canonical path or ID>
- Run/event reference: <stable ID or N/A>
- Observation window: <ISO-8601 start/end>
- Private log-system reference: <approved pointer or N/A>

## Safe summary
<bounded, redacted summary; no raw payload>

## Governance posture
- Sensitivity: <class or NEEDS VERIFICATION>
- Redaction profile: <reference or NEEDS VERIFICATION>
- Retention class: <reference or NEEDS VERIFICATION>
- Access class: <reference or NEEDS VERIFICATION>
- Policy references: <paths/IDs or N/A>

## Handoffs
- Receipt: <ID/path or N/A>
- Validation: <ID/path or N/A>
- Dashboard: <ID/path or N/A>
- Incident: <ID/path or N/A>
- Correction: <ID/path or N/A>
- Rollback: <ID/path or N/A>

## Reason codes
- <controlled reason code>

## Reviewer
<steward or OWNER_TBD>

## Review date
<YYYY-MM-DD>

## Follow-up
<bounded next action or none>
```

### Naming posture

Until identity rules are accepted, use a conservative pattern:

```text
<YYYY-MM-DD>_<runtime-scope>_review-note.md
```

This filename pattern is **PROPOSED**. A deterministic note ID, schema, registry, and migration policy remain `NEEDS VERIFICATION`.

[Back to top](#top)

---

## Security, privacy, redaction, and retention

### Default rules

- deny direct public access;
- minimize before emission;
- redact before crossing a process, trust, review, or repository boundary;
- never log secrets or private reasoning;
- use stable references instead of copying protected payloads;
- separate health telemetry from evidence and policy;
- classify sensitivity before sharing;
- enforce least privilege;
- bound retention and deletion;
- preserve incident evidence without exposing it publicly;
- record correction, invalidation, and rollback when operational state changes.

### High-risk fields

The following require removal, hashing, tokenization, generalization, or denial unless an accepted policy explicitly permits handling:

- authentication material;
- precise private endpoints and network topology;
- prompts and request bodies;
- personal identifiers;
- DNA/genomic identifiers;
- exact sensitive coordinates;
- source-restricted content;
- filesystem paths revealing private environments;
- model paths, caches, or weights with rights restrictions;
- internal stack traces or exception payloads;
- user-supplied free text;
- correlation IDs that can be joined to protected records.

### Retention posture

A review note must identify one of:

- `TRANSIENT`;
- `RETAIN_UNTIL_HANDOFF`;
- `RETAIN_FOR_INCIDENT`;
- `RETAIN_FOR_CORRECTION`;
- `RETAIN_FOR_AUDIT`;
- `DELETE_AFTER_MIGRATION`;
- `NEEDS VERIFICATION`.

These values are **PROPOSED** until accepted policy or contract evidence establishes them.

[Back to top](#top)

---

## Finite review and handoff states

| State | Meaning |
|---|---|
| `NO_ACTION` | Reviewed; no governed handoff is required. |
| `HANDOFF_REQUIRED` | Another responsibility lane must receive the issue. |
| `NEEDS_REVIEW` | Ownership, sensitivity, evidence, or action is unresolved. |
| `REDACTION_REQUIRED` | Material cannot be shared or retained in its current form. |
| `RECEIPT_REQUIRED` | Durable process memory must be emitted in an accepted receipt lane. |
| `INCIDENT_REQUIRED` | Security, privacy, rights, or operational incident handling is required. |
| `CORRECTION_REQUIRED` | A prior note, dashboard, output, or derived state must be corrected or invalidated. |
| `ROLLBACK_REQUIRED` | A runtime binding, configuration, adapter, service, or release-support path must be reverted or disabled. |
| `MIGRATE` | The note or lane should move to a better responsibility home. |
| `SUPERSEDED` | A newer reviewed note replaces this one. |
| `RETIRED` | The note or compatibility path is no longer active. |
| `ERROR` | The review or handoff could not complete safely. |

Missing access, unresolved sensitivity, absent receipts, stale pointers, failed redaction, unknown ownership, or unavailable source records must produce a negative state rather than fabricated certainty.

[Back to top](#top)

---

## Validation

### Documentation validation

- [ ] Exactly one H1 exists.
- [ ] Required README sections remain present and ordered.
- [ ] Relative links resolve.
- [ ] Fenced blocks are balanced.
- [ ] No trailing whitespace or tabs.
- [ ] No credential, token, private-key, or secret patterns.
- [ ] No raw logs, traces, dumps, prompts, request bodies, or protected payloads.
- [ ] Truth labels distinguish `CONFIRMED`, `PROPOSED`, `UNKNOWN`, and `NEEDS VERIFICATION`.
- [ ] The compatibility posture is explicit.
- [ ] The note does not claim implementation, deployment, or operational health without evidence.

### Review-note validation

- [ ] Runtime component and owning lane are identified.
- [ ] Observation time window is explicit.
- [ ] Summary is bounded and redacted.
- [ ] No raw operational payload is copied.
- [ ] Sensitivity, access, redaction, and retention classes are present.
- [ ] Receipt, validation, dashboard, incident, correction, and rollback pointers are present or `N/A`.
- [ ] Finite state and reason codes are present.
- [ ] Public-path denial is explicit.
- [ ] Reviewer and review date are present.
- [ ] Migration or deletion posture is explicit.

### Implementation proof required before operational claims

To claim an implemented logging or observability capability, provide:

- executable logger/collector/exporter/sink code;
- approved private storage and retention configuration;
- redaction and sensitivity enforcement;
- access-control and audit evidence;
- schemas/contracts where applicable;
- fixtures and negative tests;
- current CI results;
- receipt emission and validation;
- incident and correction integration;
- dashboard/alert integration where claimed;
- deployment and health evidence;
- rollback and deletion tests.

[Back to top](#top)

---

## Review burden

| Change | Minimum review |
|---|---|
| Editorial clarification | Docs steward plus runtime steward |
| New review-note field or state | Runtime, observability, receipt, and docs stewards |
| Sensitivity, redaction, retention, or access change | Security/privacy and policy review |
| Receipt handoff change | Receipt and validation stewards |
| Dashboard or alert integration | Observability and operations review |
| Incident or correction behavior | Security, correction, and release stewards |
| New tracked file under `runtime/log/` | Directory Rules and migration review |
| Raw log or payload proposal | Reject by default; security and architecture review required |
| Canonical placement change | ADR or explicit Directory Rules amendment |
| Public exposure | Deny by default; governed API, policy, evidence, security, and release review |

No single runtime or observability maintainer may silently turn this path into a log store, receipt root, dashboard root, policy root, or public data source.

[Back to top](#top)

---

## Related folders

| Path | Responsibility |
|---|---|
| [`runtime/`](../) | Canonical internal runtime wiring and handoff root. |
| [`runtime/local/`](../local/) | General local runtime coordination. |
| [`runtime/envelopes/`](../envelopes/) | Runtime envelope helper and handoff notes. |
| [`runtime/service_configs/`](../service_configs/) | Runtime service-binding and activation handoff. |
| [`data/receipts/`](../../data/receipts/) | Durable governed process memory. |
| [`data/receipts/telemetry/`](../../data/receipts/telemetry/) | Telemetry process-memory receipts. |
| [`contracts/telemetry/`](../../contracts/telemetry/) | Telemetry semantic meaning. |
| [`schemas/contracts/v1/telemetry/`](../../schemas/contracts/v1/telemetry/) | Telemetry machine shapes. |
| [`docs/dashboards/`](../../docs/dashboards/) | Dashboard documentation and catalog. |
| [`policy/runtime/`](../../policy/runtime/) | Runtime policy authority when accepted and implemented. |
| [`policy/sensitivity/`](../../policy/sensitivity/) | Sensitivity handling authority. |
| [`tests/`](../../tests/) | Executable proof. |
| [`tools/validators/`](../../tools/validators/) | Validator implementation. |
| [`release/`](../../release/) | Release, correction, withdrawal, and rollback authority. |

[Back to top](#top)

---

## ADRs

### Relevant existing or proposed decisions

- Directory Rules govern placement and currently omit `runtime/log/` from the canonical runtime tree.
- ADR-0016 governs telemetry redaction posture.
- ADR-0011 distinguishes receipts, proofs, manifests, catalogs, and publication.
- Runtime and telemetry contracts, schemas, policy, and release decisions remain in their authority roots.

### ADR or maintainer decisions still needed

1. Retain, rename, migrate, or retire `runtime/log/`.
2. Identify the approved private log and telemetry system.
3. Define runtime log, trace, metric, and event retention classes.
4. Define redaction and sensitivity profiles.
5. Define bounded review-note identity and schema posture.
6. Define receipt handoff and telemetry-receipt subtype layout.
7. Define dashboard, alert, incident, correction, and rollback integration.
8. Define ownership, CODEOWNERS, and review separation.
9. Define deletion, legal hold, incident preservation, and correction propagation.
10. Define tests and CI that deny raw payloads in repository changes.

Until those decisions are accepted, this README remains compatibility guidance only.

[Back to top](#top)

---

## Migration, correction, and rollback

### Migration sequence

1. Inventory all tracked files and inbound links under `runtime/log/`.
2. Classify each artifact by primary responsibility.
3. Move raw operational material out of Git and into an approved private system.
4. Move durable process memory to an accepted `data/receipts/` lane.
5. Move dashboards and catalog entries to approved dashboard roots.
6. Move contracts, schemas, policy, tests, validators, and runbooks to their authority roots.
7. Leave a compatibility pointer when link preservation is required.
8. Record migration, supersession, correction, and rollback references.
9. Validate links and repository secret/log scans.
10. Retire the lane only after inbound references and rollback needs are resolved.

### Correction

When a note is wrong, stale, unsafe, or overexposed:

- mark it `CORRECTION_REQUIRED`;
- remove or redact unsafe material immediately;
- preserve incident evidence in the approved restricted system;
- identify affected receipts, dashboards, incidents, outputs, and releases;
- invalidate stale pointers or derived state;
- record the correction reason and replacement;
- notify owning stewards;
- verify caches, indexes, and public surfaces do not retain the unsafe material.

### Rollback

For this README revision, rollback is mechanical:

- revert the update commit; or
- restore prior blob `cb20b50f682656e083e86b41049cc885233b63f7`.

No runtime process, log backend, collector, sink, receipt, dashboard, test, deployment, release, or public route is changed by this documentation update.

[Back to top](#top)

---

## Open verification register

| Item | Evidence needed |
|---|---|
| Exact recursive `runtime/log/` inventory | Commit-pinned tree listing and file classification. |
| Accepted placement | Maintainer decision, drift entry, migration note, or ADR. |
| Inbound links | Repository-wide link and code-reference inventory. |
| Owners and CODEOWNERS | Current ownership rules plus steward confirmation. |
| Private operational backend | Approved architecture, deployment, access, retention, and security evidence. |
| Redaction and sensitivity | Accepted profiles, implementation, negative tests, and audit evidence. |
| Receipt handoff | Accepted contract/schema/profile, validator, fixtures, and emitted receipts. |
| Review-note identity | Deterministic ID scheme, schema posture, and migration plan. |
| Dashboard and alert integration | Approved catalog entries, ownership, tests, and access posture. |
| Incident and correction integration | Runbooks, incident records, invalidation tests, and correction propagation. |
| Retention and deletion | Accepted policy, enforcement, legal-hold posture, and deletion tests. |
| Runtime emission | Executable code, tests, current CI, deployment, and health evidence. |
| Secret and payload scanning | Fail-closed repository and CI checks. |
| Public boundary | Direct-access denial tests and governed-client route inventory. |
| Rollback automation | Tested disable, migration, restoration, and cleanup path. |

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-15 |
| Evidence base | `main@21e44bb292afe8227a08b08b47683e581e92fc5b` |
| Target prior blob | `cb20b50f682656e083e86b41049cc885233b63f7` |
| Review mode | Repository-grounded documentation revision; one-file scope |
| Implementation effect | None — documentation only |
| Rollback | Revert the update commit or restore the prior blob |

### Maintenance triggers

Re-review when:

- any tracked file is added below `runtime/log/`;
- a logger, collector, exporter, sink, backend, dashboard, or alert system is implemented;
- a runtime component begins emitting governed telemetry;
- a receipt subtype or handoff contract is accepted;
- redaction, sensitivity, access, retention, or deletion posture changes;
- an incident exposes unsafe logging;
- a correction or rollback affects observability state;
- a public or semi-public client gains a telemetry-derived feature;
- Directory Rules or an accepted ADR changes placement;
- the lane is migrated, renamed, deprecated, or retired.

### v1 → v1.1 change summary

- Reclassifies the path as a noncanonical compatibility and handoff index.
- Separates raw logs, telemetry, receipts, dashboards, incidents, evidence, and release authority.
- Records README-only maturity and avoids implementation overclaiming.
- Adds redaction, sensitivity, retention, access, incident, correction, and rollback controls.
- Replaces broad note statuses with finite review and handoff states.
- Adds bounded inputs, outputs, note profile, validation, review burden, ADR backlog, migration, and open verification.
- Preserves the prior README's useful pointer-lane intent while narrowing unsafe ambiguity around the word `log`.

<p align="right"><a href="#top">Back to top</a></p>

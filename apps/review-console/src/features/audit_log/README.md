<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://app/review-console/src/features/audit-log/readme
title: Review Console Audit Log — Read-Only Governed Audit Projection Boundary
type: app-readme; directory-readme; feature-boundary; read-only-audit-projection
version: v0.2
status: draft; repository-grounded; readme-only-direct-lane; review-console-package-placeholder; review-record-schema-paired; contract-schema-drift; executable-feature-not-established
owners: OWNER_TBD — Review steward · Audit steward · Governance steward · Security steward · Policy steward · Evidence steward · Release steward · API steward · UI steward · Validation steward · Docs steward
created: 2026-06-16
updated: 2026-07-19
policy_label: "public-governance; restricted-review; read-only-audit-projection; role-gated; append-only-aware; privacy-minimizing; no-local-writes; no-release-authority; no-truth-authority"
current_path: apps/review-console/src/features/audit_log/README.md
owning_root: apps/
responsibility: document the app-local, read-only Review Console feature boundary for rendering governed review-history and audit/provenance projections without creating, mutating, deleting, reclassifying, redacting in place, or treating UI history as the canonical audit ledger
truth_posture: CONFIRMED target README and prior v0.1 feature contract, apps/review-console parent README hierarchy, Review Console package manifest name review-console/private/version 0.0.0 with no scripts or dependencies, bounded audit_log direct-lane search surfacing only this README, ReviewRecord semantic contract at case-sensitive path contracts/governance/ReviewRecord.md, PROPOSED closed ReviewRecord schema with seven required fields and additionalProperties false, one valid and one invalid ReviewRecord schema fixture, common schema fixture harness, placeholder dedicated ReviewRecord validator, draft Review Console architecture, draft review-duty and audit-invariant documents, current PolicyDecision finite outcomes, and absence of overlapping open PR/branch work / PROPOSED a governed read-model envelope, explicit UI-state axis, append-only timeline semantics, public-safe reason rendering, deterministic ordering, pagination, export limits, cache invalidation, correction/supersession display, security controls, negative fixtures, and staged implementation sequence / CONFLICTED semantic ReviewRecord field roster versus closed schema, semantic contract filename ReviewRecord.md versus schema metadata and fixture docs pointing to review_record.md, Review Console architecture decision vocabulary versus current ReviewRecord schema vocabulary, and broad audit-log language versus no accepted generic AuditEvent contract / UNKNOWN exhaustive recursive feature inventory, accepted audit-event contract and storage home, governed API route and DTO, persistence technology, direct consumers, branch protection, deployment, telemetry, retention enforcement, and current full-suite pass state / NEEDS VERIFICATION named owners, accepted contract/schema reconciliation, explicit policy and RBAC rules, reason and obligation registries, reviewer identity projection, evidence/policy/release reference carrier, dedicated validator, feature implementation, fixtures, tests, API wiring, receipt/proof linkage, incident-response handoff, retention, correction, export, accessibility, observability, and rollback automation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  visibility: public
  base_ref: main
  base_commit: 66adcd917bc77232f6eac2218849f812019631dd
  prior_blob: 88670191f0d9fc95091d0d9dadc6214b87f6fded
  inventory_method: GitHub connector exact file reads plus bounded code, branch, and open-pull-request searches
  bounded_direct_lane_result: search for audit_log surfaced this README only; recursive lane enumeration remains NEEDS VERIFICATION
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../../../governed-api/README.md
  - ../../../../explorer-web/src/features/review_console_readonly/README.md
  - ../../../../../docs/architecture/ui/REVIEW_CONSOLE.md
  - ../../../../../docs/governance/REVIEW_DUTIES.md
  - ../../../../../docs/security/AUDIT_INVARIANTS.md
  - ../../../../../docs/doctrine/directory-rules.md
  - ../../../../../contracts/governance/ReviewRecord.md
  - ../../../../../schemas/contracts/v1/governance/review_record.schema.json
  - ../../../../../fixtures/contracts/v1/governance/review_record/README.md
  - ../../../../../tools/validators/validate_review_record.py
  - ../../../../../tests/schemas/test_common_contracts.py
  - ../../../../../policy/access/README.md
  - ../../../../../policy/decision/README.md
  - ../../../../../data/README.md
  - ../../../../../release/README.md
tags: [kfm, apps, review-console, audit-log, read-model, review-record, provenance, immutable-history, role-gated, evidence, policy, release-context, correction, rollback, safe-rendering]
notes:
  - "v0.2 preserves the existing feature path and narrows it to a read-only governed projection boundary."
  - "No generic AuditEvent contract, canonical audit-ledger storage path, feature implementation, API route, or deployment is established by this README."
  - "The current ReviewRecord schema is closed and cannot carry the richer lineage, evidence, policy, sensitivity, release, sequencing, integrity, or supersession fields described by adjacent prose without a versioned schema change or companion governed envelope."
  - "This update changes documentation and its generated-work receipt only."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Review Console Audit Log

`apps/review-console/src/features/audit_log/`

> App-local, role-gated, **read-only** feature boundary for rendering governed review history and audit/provenance projections. It may help authorized reviewers inspect what happened, when, to which subject, under which reviewed decision and obligations—but it is not the canonical audit ledger, a review recorder, a policy engine, an evidence store, a release authority, or a place to rewrite history.

![status](https://img.shields.io/badge/status-draft-yellow)
![version](https://img.shields.io/badge/version-v0.2-informational)
![maturity](https://img.shields.io/badge/maturity-README--only-lightgrey)
![mode](https://img.shields.io/badge/mode-read--only-blue)
![schema](https://img.shields.io/badge/ReviewRecord-schema--paired-orange)
![authority](https://img.shields.io/badge/authority-display__only-critical)
![default](https://img.shields.io/badge/default-fail__closed-critical)

**Quick links:** [Purpose](#purpose) · [Status](#status-and-evidence) · [Authority](#authority-and-directory-rules-basis) · [Read-only contract](#read-only-contract) · [Current ReviewRecord shape](#current-reviewrecord-shape) · [Drift](#contract-schema-and-vocabulary-drift) · [Timeline](#timeline-identity-order-and-time) · [Access](#access-sensitivity-and-safe-rendering) · [Provenance](#evidence-policy-release-and-provenance-context) · [Retention](#immutability-retention-correction-and-supersession) · [UI states](#finite-outcomes-and-ui-state-axis) · [Threats](#threat-model-and-negative-paths) · [Validation](#validation-test-and-fixture-matrix) · [Implementation](#smallest-sound-implementation-sequence) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Rollback](#rollback-correction-and-document-supersession)

> [!IMPORTANT]
> **Observed maturity:** README-only in the bounded direct-lane search. The Review Console package manifest is `private`, version `0.0.0`, and defines no scripts or dependencies. No audit-log implementation, route, adapter, component, hook, feature-local test, generic `AuditEvent` contract, or deployed audit reader was established in this session.

> [!CAUTION]
> The audit feature must never make UI convenience equivalent to audit authority. It must not create, update, delete, reorder, backdate, redact in place, merge, deduplicate, normalize, or silently hide canonical history. Any correction is a new governed artifact or superseding event, not mutation of the old event.

---

<a id="purpose"></a>

## Purpose

The audit-log feature is intended to make review and governance history inspectable inside the restricted Review Console.

A mature implementation may render governed projections of:

- `ReviewRecord` objects;
- policy-decision references and safe reason summaries;
- evidence, validation, receipt, and provenance references;
- reviewer-role and separation-of-duty posture;
- release-candidate, correction, withdrawal, and rollback context;
- supersession, expiry, stale-state, and unresolved-context indicators;
- safe audit-integrity and availability warnings;
- append-only chronological or causally ordered history.

The feature exists to help an authorized reviewer answer bounded questions:

1. What subject or artifact was reviewed?
2. Which review result was recorded?
3. When was it recorded?
4. Which reviewer role was asserted?
5. What reasons and obligations were attached?
6. Which companion evidence, policy, receipt, release, correction, or rollback artifacts support the display?
7. Is the event current, superseded, incomplete, restricted, malformed, or unavailable?
8. Can the user safely inspect or copy references without exposing protected payloads?

It does **not** answer whether the underlying review was correct merely because a row exists. It does not authorize promotion, release, correction, rollback, or public display.

[Back to top](#top)

---

<a id="status-and-evidence"></a>

## Status and evidence

### Current repository state

| Surface | Status | Safe conclusion |
|---|---:|---|
| `apps/review-console/src/features/audit_log/README.md` | **CONFIRMED** | Existing feature README; prior v0.1 already declared read-only intent. |
| Other direct-lane files | **NOT SURFACED IN BOUNDED SEARCH** | Search for `audit_log` surfaced this README only. This is bounded evidence, not proof of permanent absence. |
| `apps/review-console/package.json` | **CONFIRMED PLACEHOLDER** | Package is private, version `0.0.0`, with no scripts or dependencies. |
| Parent source and feature READMEs | **CONFIRMED DOCUMENTATION** | Parent boundaries describe candidate Review Console features, not implemented modules. |
| Review Console architecture | **CONFIRMED FILE / PROPOSED ARCHITECTURE** | Defines History as read-only and Decision Pane as the sole mutating conceptual surface. |
| Review duties | **CONFIRMED FILE / DRAFT GOVERNANCE** | Describes review roles and separation-of-duty burden; most role matrix details remain proposed. |
| Audit invariants | **CONFIRMED FILE / DRAFT DOCTRINE** | Requires auditable governance; append-only ledger language is itself marked proposed/ADR-class. |
| `ReviewRecord` semantic contract | **CONFIRMED at `contracts/governance/ReviewRecord.md`** | Rich proposed meaning exists; it is not executable authority. |
| `ReviewRecord` schema | **CONFIRMED / PROPOSED CLOSED SHAPE** | Seven required fields, closed role and decision enums, `additionalProperties: false`. |
| ReviewRecord fixtures | **CONFIRMED MINIMAL SHAPE COVERAGE** | One valid and one invalid case. |
| Common schema harness | **CONFIRMED CODE** | Discovers governance schema fixture families. |
| Dedicated ReviewRecord validator | **CONFIRMED PLACEHOLDER** | Raises `NotImplementedError`; no dedicated validation behavior exists. |
| Generic `AuditEvent` contract/schema | **NOT ESTABLISHED** | Do not invent a canonical event object or path from this README. |
| Audit persistence / ledger home | **UNKNOWN** | No accepted canonical storage technology or exact path was established. |
| Governed API audit route and DTO | **UNKNOWN** | No route or runtime consumer was established. |
| Dedicated feature tests/workflow | **NOT SURFACED** | No feature-specific executable proof was established in bounded search. |

### Evidence boundary

This README may state the files and shapes inspected in this session. It must not claim:

- a live audit-log UI;
- production audit persistence;
- append-only enforcement;
- role-based access enforcement;
- complete event coverage;
- tamper evidence;
- retention enforcement;
- a working ReviewRecord validator;
- review-console build readiness;
- deployed routes;
- operational dashboards;
- incident-response integration;
- release approval or public safety.

[Back to top](#top)

---

<a id="authority-and-directory-rules-basis"></a>

## Authority and Directory Rules basis

`apps/review-console/src/features/audit_log/` is an app-local feature lane under the canonical `apps/` deployable root.

| Concern | Owning responsibility | This feature's authority |
|---|---|---|
| Audit-history display | This feature | May render a governed read model after implementation and validation. |
| Review event meaning | `contracts/governance/ReviewRecord.md` and accepted companion contracts | None; consume only. |
| Machine shape | `schemas/contracts/v1/governance/review_record.schema.json` and accepted projection schemas | None; consume and validate only. |
| Review policy and RBAC | `policy/` plus governed runtime/API enforcement | None; do not infer authorization locally. |
| Evidence authority | EvidenceBundle and related evidence/proof lanes | None; display validated references only. |
| Audit persistence | Accepted audit/provenance authority path — **NEEDS VERIFICATION** | None; never write locally. |
| Receipts and proofs | `data/receipts/`, `data/proofs/` or accepted governed homes | Reference-only. |
| Lifecycle state | `data/` lifecycle and promotion machinery | None. |
| Release/correction/rollback | `release/` | Reference-only; never authorize. |
| Public trust path | `apps/governed-api/` | All remote data comes through governed interfaces. |
| Public read-only review slice | `apps/explorer-web/src/features/review_console_readonly/` | Separate surface with narrower exposure rules. |
| Shared UI primitives | `packages/ui/` after deliberate extraction | Feature-local until reusable code is proven and migrated. |
| Security and audit doctrine | `docs/security/`, `docs/governance/`, accepted ADRs | Consume; do not redefine. |

### Placement rule

Keep this lane app-local while it is specific to Review Console presentation. Extract reusable timeline or reference components to `packages/ui/` only after:

- at least two consumers are verified;
- sensitive-field behavior is parameterized and tested;
- the component accepts governed props rather than internal-store handles;
- extraction does not create a second audit, schema, policy, or release authority;
- migration and rollback are documented.

### Prohibited parallel homes

This feature must not create:

- a new audit ledger under `apps/`;
- a feature-local schema directory that competes with `schemas/contracts/v1/`;
- a feature-local semantic contract that competes with `contracts/`;
- a feature-local policy or role matrix;
- a browser-side evidence store;
- a release or correction registry;
- a hidden cache treated as canonical history;
- a generic audit package without an ADR and responsibility review.

[Back to top](#top)

---

<a id="read-only-contract"></a>

## Read-only contract

The feature is read-only by construction.

### Allowed effects

- request an authorized governed audit projection;
- validate the response envelope and feature DTO;
- render ordered event summaries and companion references;
- paginate or filter within server-authorized query limits;
- open separately authorized evidence, policy, receipt, review, correction, or release detail views;
- copy public-safe or role-authorized identifiers;
- request refresh;
- record local, ephemeral presentation state such as expanded rows or selected filters;
- emit privacy-minimized UI telemetry when separately approved.

### Forbidden effects

- submit or update a review decision;
- write an audit event;
- edit reasons or obligations;
- delete or hide an event from canonical history;
- alter reviewer identity or role;
- reorder events to change apparent meaning;
- replace a prior event with corrected text;
- mutate lifecycle, promotion, release, correction, withdrawal, or rollback state;
- fetch canonical/internal stores directly;
- write to receipts, proofs, release, or audit storage from the browser;
- call a model to infer missing event content;
- synthesize absent evidence or provenance;
- turn a copied reference into an exported raw payload.

### Write-attempt handling

Any unexpected write capability, mutation endpoint, editable field, delete affordance, or browser-side persistence of authoritative event content is a **stop condition**. The feature should be disabled or the change blocked until the owning policy, contract, schema, API, audit, and security boundaries are reviewed.

### Read model, not ledger

```text
canonical audit / review / receipt / release artifacts
  -> governed authorization and projection
  -> schema-validated audit read model
  -> Review Console audit_log feature
  -> read-only reviewer display
```

The projection may be derived and cached. It must never outrank or rewrite its source artifacts.

[Back to top](#top)

---

<a id="current-reviewrecord-shape"></a>

## Current ReviewRecord shape

The currently inspected schema is closed and requires exactly the following field family:

| Field | Required | Schema-confirmed shape | Safe display posture |
|---|---:|---|---|
| `review_id` | yes | string matching `^[a-z][a-z0-9_:.-]*$` | Display or copy only when policy allows. |
| `subject_ref` | yes | string | Treat as opaque governed reference; do not dereference directly from the browser. |
| `reviewer_role` | yes | enum: `steward`, `reviewer`, `auditor` | Display role label only; reviewer identity is not present in this schema. |
| `decision` | yes | enum: `approve`, `reject`, `request_changes` | Render exact value plus safe explanation; do not reinterpret as release approval. |
| `reasons` | yes | array of strings | Treat as potentially sensitive; public-safe mapping is required. |
| `obligations` | yes | array of strings | Render as binding downstream duties only when vocabulary is recognized. |
| `reviewed_at` | yes | JSON Schema `date-time` string | Preserve exact timestamp; format for display without changing the source value. |

The schema sets:

```text
additionalProperties: false
```

### Consequences of the closed shape

The current object cannot lawfully carry extra fields for:

- reviewer identity;
- author/producer identity;
- independent-review result;
- event type;
- sequence number;
- previous-event hash;
- event digest or signature;
- evidence references;
- policy-decision references;
- release/correction/rollback references;
- sensitivity or rights classification;
- redaction state;
- expiration or freshness;
- supersession links;
- receipt references;
- source system;
- ingestion time;
- transaction time;
- display-safe explanation;
- internal explanation;
- pagination cursor;
- integrity-verification result.

Do not serialize those properties into `ReviewRecord` v1. A richer audit projection requires either:

1. a separately governed and schema-paired read-model envelope;
2. companion object references carried by an accepted transport envelope; or
3. a deliberate, versioned ReviewRecord schema/contract migration with fixtures, validators, policy, consumers, and rollback.

### Minimal fixture evidence

Current fixture evidence proves only:

- one valid object with all seven required fields;
- one invalid object missing `review_id`;
- common JSON Schema discovery behavior.

It does not prove semantic correctness, authorization, audit integrity, ordering, retention, evidence closure, separation of duties, safe reason rendering, or runtime consumption.

[Back to top](#top)

---

<a id="contract-schema-and-vocabulary-drift"></a>

## Contract, schema, and vocabulary drift

### Confirmed conflicts

| Drift | Evidence | Required posture |
|---|---|---|
| Contract filename case | Actual semantic contract is `contracts/governance/ReviewRecord.md`; schema metadata and fixture docs reference lowercase `review_record.md`. | Resolve deliberately; do not create a duplicate lowercase semantic contract without migration or ADR review. |
| Semantic field roster vs schema | Contract proposes many fields not allowed by the seven-field closed schema. | Schema-confirmed shape governs current JSON validity; richer semantics remain proposed. |
| Reviewer roles | Contract proposes domain-specific role vocabulary; schema permits only `steward`, `reviewer`, `auditor`. | Do not display unsupported role values as schema-valid ReviewRecords. |
| Review dispositions | Contract proposes `approve_with_conditions`, `abstain`, `deny`, `escalate`, `informational`; schema permits only `approve`, `reject`, `request_changes`. | Keep proposed dispositions out of the current `decision` field. |
| Review Console actions | App docs discuss approve, reject, defer, annotate, route, and escalate. | Treat as conceptual workflow language, not current ReviewRecord enum. |
| Policy outcomes | `PolicyDecision` uses `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`. | Do not collapse review decision, policy outcome, and UI state into one field. |
| Generic audit events | Adjacent prose speaks broadly about audit/provenance events, but no accepted generic `AuditEvent` contract was established. | Use neutral “audit projection entry” language until a contract exists. |

### Safe precedence for this feature

Until accepted migration resolves the conflict:

1. **Current schema** controls whether a `ReviewRecord` JSON object is shape-valid.
2. **Current semantic contract** informs meaning only where it does not contradict the schema.
3. **Policy and access controls** determine whether a valid object may be exposed to a caller.
4. **Governed transport/read-model schema** determines what companion context may travel to the UI.
5. **This README** defines presentation and authority boundaries only.

### No silent normalization

The feature must not silently map:

- `defer` to `request_changes`;
- `deny` to `reject`;
- `approve_with_conditions` to `approve`;
- `ABSTAIN` to an empty timeline;
- `ERROR` to “no activity”;
- reviewer-specific roles to generic `reviewer` without preserving the source role elsewhere;
- missing actor identity to “system”;
- missing timestamp to current time.

Any mapping must be versioned, documented, tested, receipt-ready, reversible, and performed in the governed API/runtime layer—not improvised in a UI component.

[Back to top](#top)

---

<a id="timeline-identity-order-and-time"></a>

## Timeline identity, order, and time

A trustworthy audit view must make ordering limitations visible.

### Required identity posture

Each displayed entry should have a stable source reference. For current `ReviewRecord`, that is `review_id`. A future projection may also carry event or receipt identifiers, but only through accepted schemas.

The UI must not:

- derive identity from array position;
- reuse one row key for multiple source events;
- merge events because their text is similar;
- drop repeated events as duplicates without an accepted deduplication contract;
- treat a mutable database row id as a public canonical id without governance review.

### Time kinds

`reviewed_at` records review time according to the current schema. It does not necessarily equal:

- ingestion time;
- event-store transaction time;
- release time;
- correction time;
- UI retrieval time;
- client rendering time.

The feature should label the time kind it actually displays. It must not invent missing time kinds or overwrite `reviewed_at` with the browser clock.

### Ordering rules

PROPOSED safe order:

1. server-provided causal/sequence order when governed and schema-confirmed;
2. otherwise `reviewed_at` ascending or descending according to an explicit user control;
3. deterministic tie-break by stable identifier;
4. visible warning when ordering is ambiguous, partial, or cursor-bounded.

### Clock and pagination limitations

The UI must not claim a complete global chronology when:

- only one page is loaded;
- timestamps collide;
- time zones or precision differ;
- source systems have known clock skew;
- late-arriving events are possible;
- a filtered view hides event families;
- authorization removes restricted entries.

Use language such as “authorized projection,” “partial history,” or “page N” rather than “complete audit trail” unless completeness is proven.

[Back to top](#top)

---

<a id="access-sensitivity-and-safe-rendering"></a>

## Access, sensitivity, and safe rendering

Audit history can be more sensitive than the reviewed subject because it may reveal:

- reviewer identity or organizational role;
- existence of restricted records;
- sensitive source names;
- exact locations;
- living-person or genomic context;
- archaeological or culturally restricted material;
- rare-species review activity;
- infrastructure details;
- security events;
- internal policy reasons;
- correction or incident posture;
- release timing;
- unresolved disputes.

### Authorization invariants

- Authentication alone is insufficient; authorization is subject-, role-, purpose-, policy-, and field-sensitive.
- The governed API must decide access before returning the projection.
- Browser code must not infer access from hidden controls or route names.
- A denied child reference must remain denied even when the parent ReviewRecord is visible.
- A reviewer may be authorized for a subject but not for internal reasons, actor identity, sensitive geometry, or incident details.
- Public or semi-public review surfaces must use separately approved public-safe projections, never reuse the restricted Review Console DTO by convenience.

### Field minimization

Render only fields needed for the authorized review purpose.

| Data class | Default display posture |
|---|---|
| Stable ids | Show only when useful and policy-safe. |
| Reviewer role | Show schema-confirmed role; avoid implying a named person. |
| Reviewer identity | Not present in current schema; do not infer. |
| Reasons | Map to controlled, public-safe or role-safe text. |
| Obligations | Show recognized obligations; unknown values fail closed. |
| Subject reference | Keep opaque; resolve only through governed navigation. |
| Evidence/policy/release refs | Show only from accepted companion envelope and policy-approved fields. |
| Exact sensitive coordinates | Deny, redact, or generalize before projection. |
| Raw payloads and internal paths | Never display. |
| Secrets, tokens, headers, stack traces | Never display. |

### Redaction semantics

Redaction is not deletion and not local text replacement.

A safe projection may contain:

- a redaction marker;
- a generalized value;
- a safe reason code;
- an access-denied placeholder;
- a reference to a separately authorized detail view.

The UI must preserve that redaction occurred without revealing what was removed.

### Error safety

Errors must not reveal:

- SQL or storage queries;
- internal filesystem paths;
- object-store bucket names when restricted;
- raw JSON payloads;
- policy source code;
- evaluator traces;
- access tokens;
- reviewer private data;
- exact protected locations;
- chain-of-thought or hidden model reasoning.

[Back to top](#top)

---

<a id="evidence-policy-release-and-provenance-context"></a>

## Evidence, policy, release, and provenance context

An audit row is not self-proving.

### Companion context classes

| Context | Purpose | Authority limit |
|---|---|---|
| Evidence references | Show what support was considered. | Reference does not prove resolution or adequacy by itself. |
| EvidenceBundle status | Show closure/availability when authorized. | EvidenceBundle remains evidence authority. |
| PolicyDecision reference | Show policy result relevant to display or action. | PolicyDecision does not equal ReviewRecord or release approval. |
| Validation/receipt refs | Show process outputs used by the review. | Receipt is process memory, not proof by itself. |
| Release candidate/manifests | Explain release context. | Review Console does not issue or mutate them. |
| Correction/withdrawal/rollback refs | Explain later changes and current status. | Display only; no local correction authority. |
| Provenance activity/entity/agent refs | Explain derivation and actors. | Must use accepted contract/DTO and safe field projection. |

### Reference resolution

The browser should never dereference internal identifiers directly. Navigation must call a governed route that independently checks:

- caller identity and role;
- purpose and audience;
- subject and field permissions;
- sensitivity and rights;
- release state;
- current correction/withdrawal state;
- evidence availability;
- response schema and safe projection.

### Broken references

When a companion reference cannot resolve:

- keep the original authorized opaque reference visible if policy allows;
- mark the companion context unavailable or stale;
- do not delete the audit row;
- do not generate replacement context;
- use `ABSTAIN` or a bounded unavailable UI state where evidence support is required;
- expose a steward next step without leaking internal details.

### Review versus release

`decision = approve` in a ReviewRecord must never be rendered as “published,” “released,” or “safe for public use” unless a separate current release artifact and policy projection establish that state.

[Back to top](#top)

---

<a id="immutability-retention-correction-and-supersession"></a>

## Immutability, retention, correction, and supersession

### Append-only posture

KFM audit doctrine proposes an append-only ledger: revocation or correction is recorded as a new artifact rather than destructive mutation. Implementation enforcement remains unverified.

The feature should therefore be designed to display:

- original entries;
- later corrections;
- superseding reviews;
- revocation or withdrawal markers;
- invalidation or stale-state notices;
- links between old and new records;
- the current effective posture without erasing history.

### Never rewrite history in the UI

Do not:

- replace original reason text with corrected reason text;
- hide a rejected or superseded review by default without a visible filter state;
- change event timestamps during formatting or migration;
- collapse a correction into the original row;
- remove a row because its subject was withdrawn;
- treat a backend soft-delete flag as permission to omit governance history without policy review.

### Retention

Retention rules for ReviewRecords, audit projections, and caches remain **NEEDS VERIFICATION**.

Until accepted rules exist:

- keep browser caches short-lived and non-authoritative;
- do not persist sensitive timeline payloads in local storage;
- do not use service workers or offline caches for restricted history without security review;
- clear in-memory state on sign-out, role change, subject change, and access denial;
- preserve server-side retention decisions outside this feature;
- do not offer “delete history” or “clear canonical log” controls.

### Supersession display

A mature read model should distinguish:

- **superseded:** later record replaces current decision meaning;
- **corrected:** a later correction addresses an error while original remains visible;
- **withdrawn:** subject or release is no longer active;
- **expired/stale:** review must be refreshed;
- **invalidated:** integrity or policy issue makes the record unusable;
- **restricted:** record exists but current caller cannot inspect details.

These labels require accepted contracts or companion DTO fields. They are not valid additions to the current closed ReviewRecord object.

[Back to top](#top)

---

<a id="finite-outcomes-and-ui-state-axis"></a>

## Finite outcomes and UI-state axis

Do not collapse three different vocabularies:

1. `ReviewRecord.decision`: `approve | reject | request_changes`;
2. `PolicyDecision.outcome`: `ANSWER | ABSTAIN | DENY | ERROR`;
3. feature presentation state: loading, ready, empty, restricted, stale, malformed, partial, or failed.

### Proposed presentation states

| UI state | Meaning | Required behavior |
|---|---|---|
| `loading` | Authorized request is pending. | No stale content flash from prior subject. |
| `ready` | Schema-valid authorized projection is available. | Render exact scope and page/filter state. |
| `empty` | Authorized projection contains no entries for the query. | Do not imply no historical activity outside query/authorization scope. |
| `abstained` | Required support or context cannot be resolved safely. | Show bounded explanation and next step; do not infer. |
| `denied` | Policy blocks access. | Show safe denial; retain no protected cached content. |
| `stale` | Projection or companion context is beyond freshness policy. | Mark stale and block trust-bearing interpretation. |
| `partial` | Page, filter, authorization, or source availability limits completeness. | Display scope limitation prominently. |
| `malformed` | Response fails schema or semantic validation. | Fail closed; do not best-effort render fields. |
| `error` | Governed request or validation machinery failed. | Safe error only; no cached fallback as current truth. |

These are presentation states, not new `PolicyDecision` outcomes and not new ReviewRecord decisions.

### Empty is not abstain

- `empty` means the authorized query returned no entries.
- `abstained` means the system cannot responsibly determine or support the requested history.
- `denied` means policy blocks access.
- `error` means machinery failed.

The feature must keep them visually and semantically distinct.

### Cached data

A cached prior result must not be silently shown as current after:

- access denial;
- reviewer role change;
- subject switch;
- policy version change;
- correction/withdrawal;
- expiry;
- API error;
- logout.

[Back to top](#top)

---

<a id="query-filter-pagination-export-and-copy"></a>

## Query, filter, pagination, export, and copy

### Query contract

A future governed audit endpoint should bind query scope explicitly, including as applicable:

- subject reference;
- authorized event/review family;
- time range and time kind;
- page size and cursor;
- sort order;
- include/exclude superseded entries;
- requested companion context;
- purpose/audience;
- projection version.

Do not infer unrestricted query permission from the ability to open the Review Console.

### Filtering

Filters alter visibility, not history.

The UI must:

- show active filters;
- offer a clear reset;
- preserve denied/restricted counts only when policy allows;
- avoid claiming “complete” while filters are active;
- not use client-only filtering to enforce access control;
- not expose hidden values in filter option lists.

### Pagination

- Cursor semantics belong to the governed API contract.
- Do not construct cursors client-side from internal ids.
- Do not assume stable page boundaries across concurrent append-only events.
- Show when newer events may exist.
- Deduplicate only by accepted stable identity and without hiding conflicting source entries.

### Copy

Allowed copy actions should be limited to authorized, public-safe or role-safe values such as a stable reference.

Never copy by default:

- full raw event JSON;
- authentication or request headers;
- internal URLs or filesystem paths;
- protected subject fields;
- exact sensitive locations;
- reviewer private data;
- raw reasons not approved for exposure;
- hidden DOM content.

### Export

Bulk export is **not** implied by read access. Any export requires separate policy, purpose, minimization, audit, rate-limit, retention, and revocation controls. Until implemented and tested, the feature should not offer bulk export.

[Back to top](#top)

---

<a id="dependency-and-governed-api-boundary"></a>

## Dependency and governed API boundary

### Allowed dependency direction

```text
Review Console audit_log UI
  -> app-local validated read-model adapter
  -> apps/governed-api authorized audit projection
  -> policy / evidence / review / receipt / release services
  -> canonical governed artifacts
```

### Forbidden dependency direction

```text
Review Console browser
  -X-> data/raw | data/work | data/quarantine | canonical stores
  -X-> audit database or object store
  -X-> policy source bundles
  -X-> receipt/proof directories
  -X-> release manifests as writable files
  -X-> model runtime
  -X-> internal admin endpoints
```

### DTO boundary

A feature DTO should be:

- versioned;
- schema-paired;
- explicit about projection scope;
- explicit about partial/filtered state;
- safe for the authorized audience;
- separate from persistence models;
- separate from the closed ReviewRecord shape when carrying companion fields;
- validated before rendering;
- backward-compatible or migrated with an explicit consumer plan.

### Local adapter responsibilities

An app-local adapter may:

- parse and validate the governed envelope;
- map recognized fields to view models;
- format timestamps and labels;
- preserve stable ids;
- reject unknown enum values;
- clear stale cache state.

It may not:

- invent missing values;
- downgrade validation errors;
- infer policy;
- resolve evidence directly from stores;
- reinterpret review decisions;
- perform redaction itself;
- issue receipts or review records.

[Back to top](#top)

---

<a id="proposed-feature-map"></a>

## Proposed feature map

No implementation module is confirmed in the direct lane.

| Candidate module | Responsibility | Must not do | Status |
|---|---|---|---|
| `api` / `client` | Call governed audit projection endpoint. | Direct-store access or auth inference. | PROPOSED |
| `schema` / `decoder` | Validate envelope and read-model shape. | Best-effort rendering of malformed data. | PROPOSED |
| `timeline` | Render ordered entries with scope and partial-state labels. | Reorder or merge canonical history silently. | PROPOSED |
| `review_record_card` | Render seven schema fields safely. | Add unsupported fields to ReviewRecord. | PROPOSED |
| `companion_refs` | Render authorized evidence/policy/receipt/release refs. | Dereference internal stores directly. | PROPOSED |
| `filters` | Express server-authorized query filters. | Enforce access client-side. | PROPOSED |
| `pagination` | Handle opaque server cursors. | Generate or decode internal cursor contents. | PROPOSED |
| `safe_states` | Render loading/empty/abstain/deny/stale/partial/malformed/error. | Collapse distinct outcomes. | PROPOSED |
| `copy_ref` | Copy allowed identifiers. | Copy raw payloads. | PROPOSED |
| `access_cleanup` | Clear sensitive state on auth/role/subject changes. | Persist restricted data offline. | PROPOSED |
| `integrity_badge` | Display server-provided verification status. | Compute or claim integrity without accepted contract. | PROPOSED |

Module names are suggestions, not path commitments. Before creating files, re-check Directory Rules, parent app conventions, package tooling, and current implementation evidence.

[Back to top](#top)

---

<a id="threat-model-and-negative-paths"></a>

## Threat model and negative paths

### Threats this feature must resist

| Threat | Example | Required control |
|---|---|---|
| Horizontal access | Reviewer changes subject id to inspect another lane. | Server-side subject authorization on every request. |
| Vertical access | Ordinary reviewer accesses auditor-only detail. | Role/purpose/field policy; no client-only guard. |
| Existence leakage | Denial reveals that a protected subject exists. | Safe indistinguishable response where policy requires. |
| Sensitive reason leakage | Internal denial reason names protected location/source. | Controlled safe explanation separate from internal detail. |
| Cache bleed | Prior subject timeline flashes after navigation or logout. | Keyed caches, purge on context change, no persistent sensitive cache. |
| Event omission | Filter or bug hides adverse events. | Visible filters, deterministic tests, server scope metadata. |
| Event reordering | Sort bug changes apparent causality. | Stable server ordering contract and tie-break tests. |
| Duplicate collapse | Similar events are merged. | Stable identity; no content-based deduplication. |
| History rewrite | Correction replaces original row. | Append/supersede display; original remains inspectable when authorized. |
| Injection | Reason string contains HTML/script or bidi control abuse. | Escape output; text rendering; normalization/security tests. |
| CSV/formula injection | Exported field begins with `=`, `+`, `-`, or `@`. | No export until hardened; sanitize under accepted export contract. |
| Reference abuse | Opaque ref becomes arbitrary URL fetch. | Allowlisted governed navigation only. |
| Enumeration | Rapid cursor or id scanning. | Server rate limit, authorization, audit, opaque cursors. |
| Integrity overclaim | UI displays “verified” from presence of id. | Only server-provided, schema-confirmed verification result. |
| AI reconstruction | Model fills missing reason or actor. | No generative completion of audit data. |
| Screenshot/public sharing | Restricted history copied into public context. | Watermark/notice where appropriate; policy and training; copy minimization. |

### Required negative fixtures/tests

At minimum, future tests should cover:

- unauthenticated request;
- authenticated but unauthorized reviewer;
- subject exists but must not be disclosed;
- authorized ReviewRecord minimal valid case;
- missing required field;
- additional unexpected field;
- unknown reviewer role;
- unknown review decision;
- invalid timestamp;
- HTML/script injection in reasons;
- bidi/Unicode confusable content;
- unknown obligation;
- evidence ref unavailable;
- policy ref denied;
- release ref withdrawn;
- superseded review;
- partial page;
- duplicate timestamp with stable tie-break;
- late-arriving event;
- role change while page is open;
- logout with cached data;
- correction without original event;
- malformed governed envelope;
- API timeout/error with prior cached result;
- copy restriction;
- export absent/denied;
- no mutation controls or endpoints.

[Back to top](#top)

---

<a id="validation-test-and-fixture-matrix"></a>

## Validation, test, and fixture matrix

### Current proof

| Proof surface | Current state | What it proves | What it does not prove |
|---|---|---|---|
| ReviewRecord schema | Present; PROPOSED; closed | Seven-field JSON shape and enums. | Semantic adequacy, auth, audit integrity, UI safety. |
| Valid fixture | One minimal case | One object passes schema. | Decision variants, reasons, obligations, security. |
| Invalid fixture | One missing-id case | Required-field rejection. | Enum, extra-field, injection, timestamp, policy failures. |
| Common schema harness | Present | Fixture directories can be discovered. | Dedicated feature behavior or runtime wiring. |
| Dedicated validator | Placeholder | File path exists. | No validation behavior; it raises `NotImplementedError`. |
| Audit-log feature tests | Not surfaced | Nothing executable established. | All feature behavior remains unproved. |
| API tests/routes | Not surfaced for this feature | Nothing executable established. | Authorization and projection remain unproved. |

### Required validation layers

1. **Schema validation** — ReviewRecord and any companion read-model envelope.
2. **Semantic validation** — reasons, obligations, decision meaning, supersession, completeness.
3. **Policy validation** — subject, field, purpose, role, sensitivity, rights, release state.
4. **Integrity validation** — accepted hashes/signatures/sequence model when available.
5. **API contract tests** — authorization, pagination, filtering, error safety, DTO versioning.
6. **UI unit tests** — exact field rendering, escaping, states, ordering, cleanup.
7. **Integration tests** — governed API through feature rendering with negative cases.
8. **Accessibility tests** — timeline semantics, focus order, status announcements, keyboard access.
9. **Security tests** — injection, enumeration, cache bleed, copy/export restrictions.
10. **Runtime proof** — deployed behavior, logs, metrics, incident and rollback drills.

### Minimum acceptance assertions

- Direct lifecycle/canonical-store imports are absent.
- No write method is exposed from the feature.
- Unknown fields/enums fail closed.
- Reasons and obligations are escaped and vocabulary-checked.
- `approve` is not presented as release approval.
- Empty, abstain, deny, stale, malformed, partial, and error remain distinct.
- Restricted fields do not exist in client payloads, not merely hidden CSS.
- Logout/role/subject changes clear cached sensitive data.
- Original and superseding records remain distinguishable.
- Active filters and partial pagination are visible.
- No raw-payload copy or export is available.
- Accessibility status is conveyed without color alone.

[Back to top](#top)

---

<a id="ci-workflow-and-operational-status"></a>

## CI, workflow, and operational status

No dedicated audit-log feature workflow was surfaced in the bounded search.

Current documentation and schema files do not establish:

- a Review Console build command;
- a Review Console test command;
- an API contract test for audit history;
- a dedicated access-policy test;
- a dedicated audit-integrity validator;
- a deployed route;
- a runtime health check;
- telemetry or alerting;
- a retention job;
- incident-response automation;
- branch-protection requirements.

A green repository workflow must not be interpreted as proof that this feature exists or that audit history is complete, immutable, authorized, or safe.

### Future workflow requirements

A future feature workflow should:

- run on pull requests affecting the feature, its DTO/schema, API route, policy, fixtures, or shared UI;
- use least-privilege read permissions for untrusted PR code;
- avoid production secrets and audit stores;
- use synthetic fixtures only;
- pin toolchains and dependencies;
- run schema, unit, integration, accessibility, and security-negative tests;
- emit non-authoritative CI artifacts only;
- never deploy, publish, mutate audit data, or authorize release.

[Back to top](#top)

---

<a id="smallest-sound-implementation-sequence"></a>

## Smallest sound implementation sequence

This sequence is **PROPOSED** and deliberately stops before persistence or production deployment.

### Phase 0 — resolve authority and drift

1. Confirm owners and review burden.
2. Decide whether `ReviewRecord.md` or lowercase `review_record.md` is canonical; migrate references without creating divergent contracts.
3. Reconcile semantic contract fields with the closed schema through a versioned plan.
4. Decide whether a separate audit-projection contract is needed.
5. Confirm the canonical audit/provenance persistence authority and retention policy.
6. Accept reason, obligation, reviewer-role, and review-decision vocabularies.

### Phase 1 — contracts and synthetic proof

1. Define a versioned, closed governed audit read-model contract if companion context is required.
2. Add machine schema under the verified schema responsibility root.
3. Add valid and invalid synthetic fixtures.
4. Implement the dedicated ReviewRecord validator or remove the misleading placeholder through governed migration.
5. Add semantic and policy validators.
6. Add tests for additional fields, enums, timestamps, injection, partial views, and denied access.

### Phase 2 — governed API read path

1. Define authorized query scope and opaque cursor semantics.
2. Implement read-only endpoint with no mutation methods.
3. Perform server-side subject/field/purpose authorization.
4. Project safe reasons and obligations.
5. Bind companion references without exposing internal stores.
6. Add rate limits, safe errors, and audit of access where policy requires.
7. Add API contract and security tests.

### Phase 3 — feature slice

1. Add a strict decoder and view model.
2. Render one minimal ReviewRecord card.
3. Add loading, ready, empty, abstain, deny, stale, partial, malformed, and error states.
4. Add deterministic ordering and visible pagination/filter scope.
5. Add cache cleanup on auth/role/subject change.
6. Add accessibility and injection tests.
7. Keep copy limited to approved ids; omit export.

### Phase 4 — companion context

1. Add evidence, policy, receipt, release, correction, and rollback refs one family at a time.
2. Require independent authorization and schema validation for each detail view.
3. Add unresolved and denied-reference tests.
4. Add supersession/correction display only after accepted contracts exist.

### Phase 5 — operational maturity

1. Define retention and cache policy.
2. Add integrity/append-only verification if the accepted ledger supports it.
3. Add telemetry without sensitive payloads.
4. Add incident-response and rollback runbooks.
5. Validate deployed behavior with synthetic accounts and fixtures.
6. Record a ReviewRecord for policy-significant approval when governance requires it.

[Back to top](#top)

---

<a id="safe-change-and-review-checklist"></a>

## Safe change and review checklist

Before changing this feature:

### Placement and scope

- [ ] Target remains under the Review Console app because behavior is app-local.
- [ ] Shared code extraction is evidence-backed and does not create authority drift.
- [ ] No new root or parallel audit/schema/contract/policy home is created.
- [ ] Any new file path is checked against Directory Rules and current repo evidence.

### Contract and schema

- [ ] Every rendered field exists in an accepted schema or governed companion DTO.
- [ ] `additionalProperties: false` is respected.
- [ ] Contract filename/case drift is not duplicated.
- [ ] Review, policy, operational, and UI-state vocabularies remain separate.
- [ ] Backward compatibility and migration are documented.

### Security and privacy

- [ ] Server-side authorization covers subject, field, purpose, and reference navigation.
- [ ] Restricted fields are omitted from payloads.
- [ ] Reasons and obligations are escaped and safe-mapped.
- [ ] Cache cleanup is tested.
- [ ] Copy/export behavior is reviewed.
- [ ] Synthetic fixtures contain no real sensitive data.

### Audit integrity

- [ ] Feature remains read-only.
- [ ] Original records are not overwritten or hidden silently.
- [ ] Ordering and partial-view limits are visible.
- [ ] Supersession/correction uses accepted companion artifacts.
- [ ] Integrity badges are server-supplied and contract-backed.

### Evidence and release

- [ ] Evidence refs resolve through governed routes.
- [ ] Broken refs produce bounded unavailable/abstain state.
- [ ] Review approval is not rendered as release approval.
- [ ] Correction/withdrawal/rollback context is current where material.

### Validation and rollback

- [ ] Positive and negative fixtures are added.
- [ ] Unit, integration, accessibility, and security tests pass.
- [ ] No direct-store imports or write endpoints are introduced.
- [ ] Safe-disable and rollback are documented.
- [ ] Docs are updated with behavior changes.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

This feature is not done until all applicable items are satisfied.

### Governance

- [ ] Owners and reviewers are confirmed.
- [ ] Review duty and separation thresholds are accepted or explicitly bounded.
- [ ] Audit persistence and retention authority are confirmed.
- [ ] Path/case and contract/schema drift are resolved.

### Contracts

- [ ] ReviewRecord meaning and shape are aligned and versioned.
- [ ] Any audit read-model envelope has semantic contract and closed schema.
- [ ] Reason, obligation, role, decision, supersession, and integrity vocabularies are governed.
- [ ] PolicyDecision, ReviewRecord decision, and UI state remain distinct.

### API and policy

- [ ] Governed read-only route exists.
- [ ] No mutation methods are exposed.
- [ ] Subject/field/purpose authorization is server-enforced.
- [ ] Safe explanations and reference navigation are policy-gated.
- [ ] Pagination, filtering, freshness, and partial-state semantics are contracted.

### Feature

- [ ] Implementation files exist and are inventoried.
- [ ] Strict decode/validation occurs before render.
- [ ] Minimal and companion-context views are implemented incrementally.
- [ ] Accessibility and keyboard behavior are tested.
- [ ] Sensitive caches are short-lived and cleared correctly.
- [ ] Copy is bounded; export is absent or separately governed.

### Proof

- [ ] Dedicated validator is implemented and wired.
- [ ] Positive and negative fixture matrix is adequate.
- [ ] API, UI, integration, accessibility, and security tests pass.
- [ ] Runtime/deployment behavior is verified.
- [ ] Logs and metrics avoid sensitive payloads.
- [ ] Incident, correction, and rollback paths are tested.

### Publication posture

- [ ] No README, test, receipt, audit row, or review approval is treated as release authority.
- [ ] Public or semi-public views use separate approved projections.
- [ ] Human review and release duties remain auditable and separable.

[Back to top](#top)

---

<a id="open-verification-register"></a>

## Open verification register

| Item | Status | Why it matters | Resolution evidence |
|---|---:|---|---|
| Recursive direct-lane inventory | NEEDS VERIFICATION | Confirms whether files beyond README exist. | Repository tree/checkout and file manifest. |
| Review Console implementation inventory | UNKNOWN | Determines actual framework, routes, components, and tests. | Source tree and package tooling. |
| Canonical contract filename/case | CONFLICTED | Prevents duplicate `ReviewRecord.md` / `review_record.md` authority. | Migration note or ADR plus updated refs. |
| ReviewRecord contract/schema alignment | CONFLICTED | Current schema cannot carry proposed semantic fields. | Versioned contract/schema/fixtures/tests. |
| Generic audit-event object | UNKNOWN | Avoids inventing event fields and identities. | Accepted contract/schema or explicit decision not to create one. |
| Audit ledger/storage authority | UNKNOWN | Required for read-model source, retention, and integrity. | Architecture decision and operational evidence. |
| Append-only enforcement | NEEDS VERIFICATION | UI design depends on correction/supersession semantics. | Storage policy, tests, receipts, runtime evidence. |
| Governed API route/DTO | UNKNOWN | Required before feature implementation. | Route, OpenAPI/schema, tests, policy. |
| Reviewer identity projection | UNKNOWN | Current schema includes role but not identity. | Accepted companion DTO and privacy policy. |
| Reason-code registry | NEEDS VERIFICATION | Required for safe, stable explanations. | Registry, policy mapping, tests. |
| Obligation registry/interpreter | NEEDS VERIFICATION | Unknown obligations must fail closed. | Registry and UI/API tests. |
| Access/RBAC/purpose policy | UNKNOWN | Browser cannot enforce access itself. | Policy modules, fixtures, runtime tests. |
| Sensitive-field projection | UNKNOWN | Audit history may expose protected facts. | Field policy and negative fixtures. |
| Pagination/order contract | UNKNOWN | Prevents false completeness and reordered history. | DTO/schema/API tests. |
| Supersession/correction carrier | UNKNOWN | Current ReviewRecord cannot encode links. | Companion contract or versioned migration. |
| Retention/cache policy | UNKNOWN | Prevents indefinite client persistence. | Policy/runbook and tests. |
| Export policy | UNKNOWN | Read access does not imply bulk export. | Separate policy, contract, tests. |
| Feature-specific CI | NOT SURFACED | Needed for enforceability proof. | Workflow/job and passing run. |
| CODEOWNERS / branch protection | NEEDS VERIFICATION | Required review enforcement remains platform-specific. | Repository settings and verified identities. |
| Deployment/telemetry/incident integration | UNKNOWN | Required for operational claims. | Deployment config, logs, dashboards, drills. |
| Current repository-wide pass state | UNKNOWN | Avoids false quality claims. | Current complete CI evidence. |

[Back to top](#top)

---

<a id="evidence-ledger"></a>

## Evidence ledger

| Evidence | Status | Supports | Limit |
|---|---:|---|---|
| `apps/review-console/src/features/audit_log/README.md` prior blob `88670191…` | CONFIRMED | Existing path and read-only intent. | Does not prove implementation. |
| Bounded `audit_log` code search | CONFIRMED BOUNDED | Direct search surfaced target README only. | Not a recursive filesystem proof. |
| `apps/review-console/package.json` blob `9c83b3de…` | CONFIRMED | Private `0.0.0` manifest with no scripts/dependencies. | Does not prove absence of all source files. |
| `apps/review-console/src/README.md` blob `bb64035f…` | CONFIRMED DOCUMENTATION | Source-tree boundary and candidate features. | Candidate names are not code. |
| `apps/review-console/src/features/README.md` blob `249b01a9…` | CONFIRMED DOCUMENTATION | Parent feature boundary, read-only-by-default posture. | Implementation unknown. |
| `apps/review-console/README.md` blob `02512b6b…` | CONFIRMED DOCUMENTATION | App authority and single-decision-write posture. | Routes/runtime unknown. |
| `docs/architecture/ui/REVIEW_CONSOLE.md` blob `66d26b28…` | CONFIRMED FILE / PROPOSED | History read-only; Decision Pane sole mutating conceptual surface. | Draft explicitly not implementation evidence. |
| `docs/governance/REVIEW_DUTIES.md` blob `f815ffe1…` | CONFIRMED FILE / DRAFT | Separation-of-duties and ReviewRecord burden. | Most role matrix details proposed. |
| `docs/security/AUDIT_INVARIANTS.md` blob `0a07adec…` | CONFIRMED FILE / DRAFT | Detectable governance failures; append-only proposal. | Append-only enforcement not verified. |
| `contracts/governance/ReviewRecord.md` blob `9641345d…` | CONFIRMED semantic contract | Rich proposed meaning and anti-collapse rules. | Not aligned with current schema. |
| `schemas/contracts/v1/governance/review_record.schema.json` blob `fe2f2223…` | CONFIRMED / PROPOSED schema | Seven fields, enums, closed shape. | Does not prove semantics or runtime. |
| `fixtures/contracts/v1/governance/review_record/README.md` blob `fccac522…` | CONFIRMED | One valid/one invalid fixture and documented drift. | Minimal shape proof only. |
| `tools/validators/validate_review_record.py` blob `e1aa5fcc…` | CONFIRMED PLACEHOLDER | Declared validator path exists. | Raises `NotImplementedError`. |
| `tests/schemas/test_common_contracts.py` | CONFIRMED code from current repo evidence | Common fixture discovery. | Not feature or semantic proof. |
| `policy/decision/README.md` | CONFIRMED current policy documentation | Four canonical PolicyDecision outcomes and vocabulary separation. | Does not implement policy. |
| Branch and open-PR searches | CONFIRMED BOUNDED | No overlapping audit-log README work surfaced. | Search indexing may be incomplete. |

[Back to top](#top)

---

<a id="maintenance-triggers"></a>

## Maintenance triggers

Update this README when any of these changes:

- a feature file appears in this lane;
- Review Console package scripts or dependencies are added;
- a governed audit route or DTO is introduced;
- ReviewRecord contract/schema changes;
- contract path/case drift is resolved;
- a generic audit-event contract is accepted;
- reason, obligation, role, or decision vocabularies change;
- audit persistence or retention is selected;
- append-only or integrity enforcement lands;
- policy/RBAC rules are implemented;
- evidence/release/correction companion views are added;
- copy/export behavior changes;
- dedicated tests/workflows land;
- public/semi-public audit exposure is proposed;
- incident, deployment, or telemetry posture changes;
- correction, withdrawal, or rollback semantics change.

Documentation changes must accompany material behavior changes. Documentation does not substitute for tests or runtime evidence.

[Back to top](#top)

---

<a id="rollback-correction-and-document-supersession"></a>

## Rollback, correction, and document supersession

### Feature rollback

A future implementation should support a safe-disable path that:

- removes navigation to the feature;
- blocks the governed route or capability for the affected version;
- clears client caches;
- preserves canonical audit data;
- preserves access audit records;
- does not delete ReviewRecords, receipts, or release/correction artifacts;
- provides a bounded safe message to authorized users;
- records the rollback reason and target.

### Contract rollback

Schema or DTO rollback must account for already emitted objects and consumers. Do not force old records through a newer schema or rewrite them in place. Prefer versioned readers and explicit deprecation windows.

### Documentation rollback

For this v0.2 update:

- restore prior blob `88670191f0d9fc95091d0d9dadc6214b87f6fded` if the revision is rejected;
- revert the generated-work receipt separately;
- retain review discussion and correction history;
- do not present rollback as proof that implementation changed.

### No-loss preservation note

The previous README was substantive, not empty. This revision preserves its core intent:

- app-local feature placement;
- read-only audit/provenance display;
- no local audit writes;
- governed API and role gating;
- evidence, policy, release, correction, and rollback separation;
- safe states and validation expectations.

It narrows speculative module claims, replaces blanket uncertainty with current evidence, and surfaces contract/schema/path conflicts that the prior version did not reconcile.

[Back to top](#top)

---

## Status summary

`apps/review-console/src/features/audit_log/` is currently a documented feature boundary, not an established implementation.

The safest current posture is:

```text
read-only
+ governed API only
+ schema-validated projection
+ role/purpose/field policy
+ no local mutation
+ no history rewrite
+ explicit partial/stale/denied/error states
+ evidence/policy/release references only through accepted companion contracts
+ correction and supersession without deletion
+ cite or abstain
```

The next sound change is not a speculative UI component. It is resolution of the ReviewRecord contract/schema/path drift and definition of the smallest authorized audit read-model contract with negative fixtures and policy tests.

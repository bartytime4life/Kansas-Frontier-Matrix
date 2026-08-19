<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-architecture-briefing-live-issue-inventory-binding
title: Briefing Live Issue Inventory Binding — Current Repository Boundary
type: architecture-implementation-note
version: v1.0-draft
status: "draft; repository-grounded; implementation-present; profile-proposed-inactive; non-authoritative; no-live-activation; no-repository-mutation; archive-placement-hold"
owners:
  - "@bartytime4life — verified CODEOWNERS review route only"
  - "NEEDS VERIFICATION — accountable architecture, governance, briefing-integration, GitHub-integration, validation, security, and operations stewards"
created: 2026-08-08
updated: 2026-08-19
policy_label: "repository-facing; internal-control-plane; read-only; value-minimized; no-public-authority; no-repository-mutation"
owning_root: docs/
current_path: docs/architecture/briefing-live-issue-inventory-binding.md
responsibility: >-
  Explain the current repository binding between deterministic BriefingSignal issue
  routing, fixture-backed IssueInventoryProjection input, and stored
  GitHubIssueInventoryRead records; preserve the merge-repair lineage; define the
  no-network, no-write, freshness, identity, minimization, validation, correction,
  and graduation boundaries; and prevent test fixtures or read observations from
  being represented as current issue authority or mutation permission.
truth_posture: >-
  CONFIRMED accepted Directory Rules decision, PR #2179/#2180/#2292 lineage,
  current contract/schema/probe/validator/router/fixture/test/workflow bytes, current
  CODEOWNERS route, current checked-in fixture provenance, and current implementation
  boundaries / PROPOSED operational hardening, workflow-closure, retention, and
  future graduation steps / UNKNOWN approved live-read operator, least-privilege
  credential profile, production retention/audit lane, authorized issue writer,
  deployed consumer, required-check coupling, and runtime operation.
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 8d2535d3231c81b3d7bc32dff660ad8cc7983f64
  target_prior_blob: 7c0d7740a7419a34f3acd868521c450ab796a8d8
  directory_rules_decision: ADR-0029 accepted
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  issue_inventory_contract_blob: 1bebd47fe208d2dfbb5da08e577aa1dfa64f665f
  github_read_contract_blob: ab250735f6caf715c6598825c6bbe2aa2b517c75
  github_read_schema_blob: 1ff7440abd1a69becad90f556ba9fc3fb100ec64
  github_read_probe_blob: 3908159b614edf4ee0eedcac3af68ee49b568800
  stored_read_validator_blob: e00fac7067db636877464e4942355377d7ea3b2f
  router_blob: f92e1f43b2a1893cbadd01db36128b0756992cf8
  stored_read_fixture_blob: 93fb5ece6a4dde433de75e6efa7b32efadb80563
  api_fixture_blob: f6fb7127056a46bb2fd454ca39edd1b7e06be525
  adapter_test_blob: f7f677c8d51a32d53dccb05f9571c58007553c05
  binding_test_blob: 489538fbf130d21ce41a99aab28a782a892b1d61
  adapter_workflow_blob: 8e0db0e123dafe2e1a762da2eb8c668dcfad9afd
  briefing_workflow_blob: e20c0960bbc4e7aac7b3eaecd5cf68ef332e8da0
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  implementation_lineage:
    - "PR #2179 merge 7f402354df34ebccb81d64ea6d235f2e1bae8b07"
    - "PR #2180 stacked merge 2666813a3d5ff2c539fffc88856fc579290cd0c2"
    - "PR #2292 current-main repair merge 38cece49b89687416b13b806ec64d61f3f174387"
related:
  - README.md
  - briefing-integration.md
  - document-convergence-plan.md
  - ../doctrine/directory-rules.md
  - ../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../contracts/governance/briefing_signal.md
  - ../../contracts/governance/issue_inventory_projection.md
  - ../../contracts/governance/github_issue_inventory_read.md
  - ../../schemas/contracts/v1/governance/briefing_signal.schema.json
  - ../../schemas/contracts/v1/governance/issue_inventory_projection.schema.json
  - ../../schemas/contracts/v1/governance/github_issue_inventory_read.schema.json
  - ../../fixtures/contracts/v1/governance/github_issue_inventory_read/api_fixture.json
  - ../../fixtures/contracts/v1/governance/github_issue_inventory_read/fresh_receipt_1647.json
  - ../../tools/probes/github_issue_inventory_read.py
  - ../../tools/validators/governance/validate_issue_inventory_projection.py
  - ../../tools/validators/governance/validate_github_issue_inventory_read.py
  - ../../tools/validators/governance/route_briefing_signals.py
  - ../../tests/governance/test_github_issue_inventory_read.py
  - ../../tests/governance/test_briefing_signal_issue_inventory.py
  - ../../tests/governance/test_briefing_signal_live_issue_inventory.py
  - ../../.github/workflows/github-issue-inventory-read.yml
  - ../../.github/workflows/briefing-integration.yml
  - ../../.github/CODEOWNERS
tags:
  - kfm
  - architecture
  - implementation-note
  - briefing
  - github
  - issue-inventory
  - read-only
  - fixture
  - freshness
  - routing
  - no-network
  - no-mutation
  - correction
  - rollback
notes:
  - "Same-path documentation modernization only; no contract, schema, fixture, probe, validator, router, test, workflow, issue, repository setting, lifecycle object, release, deployment, or publication surface is changed."
  - "The checked-in fresh_receipt_1647.json is fixture-derived from api_fixture.json and is not current GitHub issue-state evidence."
  - "The live probe code exists, but the schema fixes profile_state to PROPOSED_INACTIVE and normal CI exercises fixture transport only."
  - "The architecture convergence plan keeps structural migration of this dated implementation note on HOLD; this change performs no move, rename, redirect, tombstone, supersession, or deletion."
  - "All prior major-section headings are retained as headings or explicit anchors for inbound-fragment compatibility."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>
<a id="briefing-live-issue-inventory-binding"></a>

# Briefing Live Issue Inventory Binding — Current Repository Boundary

> **Purpose.** Explain what the repository currently implements when a validated
> `BriefingSignal` declares an existing GitHub issue, how fixture and stored-read
> inputs remain separate, why every result is still a proposal, and what must
> close before any operational live read or issue write can be admitted.

> [!IMPORTANT]
> **The binding exists on current `main`, but it creates no write authority.** A
> successful stored-read binding can preserve the dry-run disposition
> `UPDATE_EXISTING_ISSUE`; it cannot open, edit, label, assign, comment on, close,
> reopen, transfer, lock, merge, or otherwise mutate a GitHub object.

> [!CAUTION]
> **The checked-in `fresh_receipt_1647.json` is test material, not a live
> inventory.** It is deterministically derived from the checked-in
> `api_fixture.json`. Its `FRESH` value means only “inside the fixture's declared
> five-minute replay window.” It must not be used to claim current issue state.

> [!WARNING]
> **Read-only code is not operational admission.** The live probe implements HTTP
> `GET` calls, but `GitHubIssueInventoryRead.profile_state` is fixed to
> `PROPOSED_INACTIVE`; normal CI supplies no live credential and performs no live
> GitHub read.

| Field | Current bounded result |
|---|---|
| Repository checkpoint | `main@8d2535d3231c81b3d7bc32dff660ad8cc7983f64` |
| Directory result for this edit | `PLACE` at the existing path for same-document correction; structural migration remains `HOLD` in the architecture convergence plan |
| Accepted placement authority | [`ADR-0029`](../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the exact [`Directory Rules v2`](../doctrine/directory-rules.md) bytes |
| Adapter/profile state | Implementation present; semantic/schema state `PROPOSED_INACTIVE` |
| Router network posture | No network; consumes local validated files only |
| Live probe network posture | Explicit operator invocation only; GET-only implementation; no live call in normal CI |
| Current checked-in stored record | Fixture-derived, historical, five-minute replay specimen; not current GitHub evidence |
| Current write path | None in this object family or router |
| Review route | `@bartytime4life` through [`CODEOWNERS`](../../.github/CODEOWNERS); routing is not stewardship, independent review, or approval |
| Evidence, policy, release, publication effect | None |

**Quick navigation:** [Scope](#1-goal-and-scope) · [Evidence](#2-evidence-and-lineage) · [Responsibilities](#3-current-responsibility-map) · [Routing](#fail-closed-routing) · [Inputs](#5-two-input-families) · [Probe](#6-github-read-acquisition-profile) · [Stored validation](#7-stored-read-validation) · [Binding outcomes](#8-binding-semantics-and-finite-outcomes) · [Identity](#9-identity-freshness-and-replay) · [Security](#10-security-credentials-and-minimization) · [Validation](#validation) · [Gaps](#12-current-gaps-and-stop-conditions) · [Graduation](#13-graduation-plan) · [Trust](#trust-boundary) · [Placement](#directory-rules-basis) · [Rollback](#rollback) · [Related](#18-related-surfaces)

---

<a id="1-goal-and-scope"></a>

## 1. Goal and scope

This page is the implementation-boundary companion to
[`briefing-integration.md`](briefing-integration.md). The durable briefing page
owns the whole briefing-to-system architecture. This page owns only the narrow
current-state explanation of one repair lineage and one integration seam:

```text
BriefingSignal declared existing-issue route
  -> read-only inventory input
  -> deterministic validation
  -> exactly-one-open-target binding or fail-closed hold/failure
  -> value-minimized routing proposal
```

### In scope

- the distinct fixture and GitHub-read profiles;
- the separate network-acquisition and no-network-consumption steps;
- stored-record validation and explicit replay time;
- issue-set binding and finite routing outcomes;
- field minimization, credential handling, and fixed-false authority effects;
- current tests and workflow coverage;
- current gaps, hard stop conditions, correction, and rollback;
- the historical stacked-PR repair that made the binding present on current
  `main`.

### Out of scope

- evaluating the truth or completeness of an issue body, comment, label, or
  attachment;
- searching the complete issue portfolio or selecting work from prose;
- Projects V2 fields, milestones, dependencies, sub-issues, assignees, reviewers,
  permissions, rulesets, branch protection, merge state, or repository-control
  authority;
- a long-lived issue-state database, cache, event stream, or watcher;
- source admission, `EvidenceBundle` creation, policy evaluation, review,
  promotion, proof, release, deployment, publication, or public use;
- any GitHub write operation.

The words “live,” “read,” “receipt,” “fresh,” and “bound” are descriptive of a
bounded observation or replay contract. They are not authority labels.

[Back to top](#top)

---

<a id="2-evidence-and-lineage"></a>

## 2. Evidence and lineage

### 2.1 Implementation lineage

| Change | CONFIRMED repository result | Boundary |
|---|---|---|
| [PR #2179](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/2179) | Added the `GitHubIssueInventoryRead` contract, closed schema, fixture transport, GET-only diagnostic probe, adapter tests, and dedicated fixture-only workflow; merged as `7f402354df34ebccb81d64ea6d235f2e1bae8b07` | Deliberately did not bind the profile into BriefingSignal routing |
| [PR #2180](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/2180) | Added stored-read validation and router binding on a branch stacked on the already-merged #2179 branch; merged there as `2666813a3d5ff2c539fffc88856fc579290cd0c2` | Its integration bytes did not enter default-branch history through that stacked merge context |
| [PR #2292](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/2292) | Replayed the five dependency-closed integration files onto then-current `main`; merged as `38cece49b89687416b13b806ec64d61f3f174387` | Restored only the no-network stored-record binding; no issue mutation or live activation |
| Current main | Contains the contract/schema/probe, stored validator, router option, fixture records, focused tests, and the two current workflow lanes listed below | Presence proves repository bytes, not an operational live service or authorized writer |

### 2.2 Current evidence hierarchy

For this seam, current implementation claims are controlled in this order:

1. accepted Directory Rules and applicable accepted ADRs;
2. current contracts and closed schemas;
3. current probe, validators, router, tests, and workflows;
4. checked-in fixtures as deterministic test inputs only;
5. this page and historical PR descriptions as explanatory lineage.

The supplied Briefing-to-System design remains useful doctrine: briefing prose is
an intake signal, not evidence or publication authority. Current repository bytes
control the narrower statement of what is implemented now.

### 2.3 Current-state caution demonstrated by the fixture

The stored test record declares issue `#1647` open inside a synthetic August 8
fixture. At this document refresh, GitHub reports
[`#1647`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/1647)
closed. The purpose of recording this dated contrast is not to maintain a second
issue ledger in Markdown. It demonstrates the governing rule: a checked-in
fixture or expired read can prove replay behavior, never current platform state.

[Back to top](#top)

---

<a id="3-current-responsibility-map"></a>

## 3. Current responsibility map

| Surface | Current responsibility | What it does not own |
|---|---|---|
| [`IssueInventoryProjection` contract](../../contracts/governance/issue_inventory_projection.md) | Defines the deterministic fixture-backed issue-state projection used by contract tests | Live GitHub state, evidence, permissions, or mutation |
| [`GitHubIssueInventoryRead` contract](../../contracts/governance/github_issue_inventory_read.md) | Defines a minimized, repository/ref-bound read observation and finite read outcomes | Issue truth, writer authorization, review, release, or publication |
| [`github_issue_inventory_read.schema.json`](../../schemas/contracts/v1/governance/github_issue_inventory_read.schema.json) | Defines the closed Draft 2020-12 machine shape and fixed-false effects | Semantic admission, operator authorization, currentness beyond recorded fields |
| [`github_issue_inventory_read.py`](../../tools/probes/github_issue_inventory_read.py) | Builds records from explicit fixture input or explicitly invoked GitHub GET requests | Scheduled operation, canonical storage, issue mutation, or router execution |
| [`validate_issue_inventory_projection.py`](../../tools/validators/governance/validate_issue_inventory_projection.py) | Validates deterministic fixture projections and owns shared issue-set binding semantics | Live acquisition or issue mutation |
| [`validate_github_issue_inventory_read.py`](../../tools/validators/governance/validate_github_issue_inventory_read.py) | Revalidates one stored read record, identity, exact issue set, `FRESH` outcome, and explicit replay time | Network access, re-reading current state, or write-time concurrency control |
| [`route_briefing_signals.py`](../../tools/validators/governance/route_briefing_signals.py) | Produces a deterministic, value-minimized routing report from local inputs | Network calls, issue creation/update, evidence, policy, review, or release |
| [`api_fixture.json`](../../fixtures/contracts/v1/governance/github_issue_inventory_read/api_fixture.json) | Synthetic API-shaped producer input | Historical or current GitHub fact |
| [`fresh_receipt_1647.json`](../../fixtures/contracts/v1/governance/github_issue_inventory_read/fresh_receipt_1647.json) | Deterministic stored-record replay specimen | Current issue state or an authenticated live-run receipt |
| Governance tests | Prove declared positive and negative behavior over synthetic inputs | Platform permissions, deployment, live GitHub behavior, or issue-body truth |
| Workflow files | Orchestrate bounded read-only checks over repository bytes | Operational activation, required-check status, human approval, or publication |
| This page | Explains composition, lineage, limits, and graduation | Contract, schema, policy, platform, or release authority |

Every artifact has one authority owner. The probe may produce a record used by a
validator, and the validator may feed a router, but producer relationships do not
collapse their responsibilities or homes.

[Back to top](#top)

---

<a id="fail-closed-routing"></a>

## Fail-closed routing

The current design separates **acquisition** from **consumption** so the router
remains deterministic and no-network:

```text
PATH A — deterministic contract test

checked-in IssueInventoryProjection
  -> validate projection shape, time, issue set, digest, and identity
  -> bind declared issue IDs
  -> routing proposal or fail-closed HOLD

PATH B — optional read observation

explicit operator invocation
  -> GET repository metadata
  -> GET default-branch ref
  -> GET each explicitly requested issue
  -> value-minimized GitHubIssueInventoryRead JSON on stdout
  -> store or pass as a local file under an approved handling procedure
  -> no-network stored-read validator with explicit --as-of
  -> shared issue-set binding
  -> routing proposal or fail-closed failure/HOLD
```

There is no direct edge from the probe to a GitHub writer and no writer is
implemented in this seam.

```text
BriefingSignal
  -> deterministic declared route
  -> exactly one inventory input family
  -> input-family validation
  -> issue-set binding
  -> UPDATE_EXISTING_ISSUE proposal
       OR HOLD_FOR_DEPENDENCY
       OR FAIL
  -X-> GitHub mutation
```

The router rejects simultaneous fixture and stored-read inputs. A stored read
requires an explicit `--as-of`; wall-clock time is never used implicitly for
replay. Invalid stored input fails before any signal is routed.

[Back to top](#top)

---

<a id="5-two-input-families"></a>

## 5. Two input families

The two profiles are intentionally related but non-interchangeable.

| Dimension | `IssueInventoryProjection` | `GitHubIssueInventoryRead` |
|---|---|---|
| Primary purpose | Deterministic fixture-backed contract test | Minimized observation shape for an explicitly invoked read |
| Contract status | `PROPOSED`, fixture-backed | `PROPOSED_INACTIVE` |
| Producer | Checked-in fixture construction | Probe fixture mode or explicit GET-only live mode |
| Network required | Never | Only for explicit live probe mode |
| Stored router input | Local projection file | Local stored-read file |
| Repository/ref binding | Repository name and fixture provenance | Repository name/id, default branch, and recorded branch-head SHA |
| Issue fields | Number, `OPEN`/`CLOSED`, update time | Number, `OPEN`/`CLOSED`, update time |
| Time model | Projection generation time | Retrieval time plus `stale_at`; replay requires explicit `as_of` |
| Identity | Projection digest and 16-hex projection ID | Response digest and 24-hex receipt ID |
| Deterministic tests | Canonical reference profile | Fixture-transport and stored-record replay profile |
| Live-state claim | Fixed false | Bounded observation only when actually acquired live; checked-in fixtures remain synthetic |
| Mutation/public effects | Fixed false | Six trust-bearing effect flags fixed false |

### 5.1 Fixture law

The fixture lane may simulate API responses, branch heads, issue states,
timestamps, and rate-limit headers. Simulation is allowed because its purpose is
to prove code behavior. It must remain clearly synthetic and must not be reused
as platform evidence.

### 5.2 Stored-read law

A file shaped like `GitHubIssueInventoryRead` is not automatically an
authenticated observation. Its provenance must establish how it was produced.
The current schema binds record content but does not itself distinguish a
fixture-mode producer from a live-mode producer. The checked-in specimen is
therefore classified by its repository provenance as **fixture-derived**.

### 5.3 No fallback

When a live read is unavailable, stale, malformed, unauthenticated, or otherwise
held, the system must not silently substitute a fixture and describe the result
as current. A fixture may be selected explicitly for tests; it is not an
operational fallback.

[Back to top](#top)

---

<a id="6-github-read-acquisition-profile"></a>

## 6. GitHub read acquisition profile

The current probe performs this explicit bounded sequence:

1. read repository metadata with `GET /repos/{repository}`;
2. read the default-branch ref with `GET /repos/{repository}/git/ref/heads/{branch}`;
3. read each explicitly requested issue with `GET /repos/{repository}/issues/{number}`;
4. reject any returned row containing `pull_request`;
5. minimize each issue to `number`, uppercase state, and `updated_at`;
6. record available rate-limit remaining/reset headers;
7. calculate `stale_at` from a default 300-second window;
8. calculate the response digest and receipt ID; and
9. print canonical compact JSON to stdout.

### 6.1 Explicit inputs

- repository in `owner/name` form is supplied by the caller;
- one or more issue numbers are supplied by repeated `--issue` arguments;
- fixture mode is selected with `--fixture`;
- deterministic time can be supplied with `--now`;
- live mode reads `KFM_GITHUB_READ_TOKEN` first, then `GITHUB_TOKEN`.

### 6.2 Finite producer outcomes

| Outcome | Current producer meaning |
|---|---|
| `FRESH` | Record built successfully and no explicit zero remaining rate limit was observed |
| `HOLD_RATE_LIMIT` | The merged response headers report zero remaining requests |
| `HOLD_AUTH` | Live mode was selected without an available token |
| `ERROR` | Transport, parsing, repository/ref binding, issue-set, PR-object, or local I/O failure |
| `STALE` | Returned by the separate freshness helper when evaluated after `stale_at` |
| `HOLD_BINDING` | Declared by the contract/schema vocabulary; current probe surfaces binding failures through `ERROR` rather than emitting this record outcome |

That last distinction matters: the semantic vocabulary is broader than every
currently emitted code path. Documentation must not claim an implemented
producer branch merely because an enum value exists in the schema.

### 6.3 Current operational limitations

- no scheduled live run is established;
- no operator runbook or approved live-reader role is established;
- the code enforces GET methods but does not verify that the supplied token is
  least-privilege or read-only;
- no retry/backoff strategy or conditional request is implemented;
- issue reads are one request per explicit issue ID; there is no portfolio
  pagination or search;
- probe output is printed to stdout; a canonical runtime retention, redaction,
  expiry, and audit home for real outputs is not established;
- the producer does not run the repository schema validator before printing its
  record;
- missing rate-limit headers are recorded as `null` and do not independently
  prevent `FRESH`;
- the producer accepts caller issue lists before the closed schema's 64-item cap
  is enforced by a later validation step.

These are bounded implementation facts and open graduation work, not reasons to
misrepresent the current probe as absent.

[Back to top](#top)

---

<a id="7-stored-read-validation"></a>

## 7. Stored-read validation

The stored-read validator performs no network access. It currently:

- rejects symbolic links, missing files, unreadable/invalid JSON, non-object
  roots, and closed-schema failures;
- recomputes `response_digest` over every field except `receipt_id` and
  `response_digest`;
- recomputes the deterministic `receipt_id` from that digest;
- requires requested issue IDs to be sorted and unique;
- requires returned issue rows to be sorted and to match the requested set
  exactly;
- requires `outcome == FRESH`;
- requires explicit caller-supplied `as_of` not later than `stale_at` and not
  earlier than `retrieved_at`; and
- returns the payload only when every finding closes.

### 7.1 What validation proves

A pass proves that the local record conforms to the current closed shape,
deterministic identity, exact issue-set, fixed-false effects, and declared replay
window. It does not prove:

- that the record came from live mode rather than fixture mode;
- that the issue state remains current at consumption or write time;
- that the recorded default-branch SHA equals the consuming checkout's current
  head;
- that issue content is correct;
- that the token used by a producer was least-privilege;
- that a GitHub mutation is allowed.

### 7.2 Current hardening gaps

The stored validator is materially narrower than the fixture-projection
validator. Current code does not yet add an explicit input-size cap,
duplicate-key rejection, non-finite-number rejection, canonical UTC-second
normalization for every timestamp, bounded schema-finding count, or producer-mode
attestation. The closed schema catches many malformed shapes, but it must not be
represented as those additional defenses.

A future hardening change should reuse the repository's existing deterministic
JSON-loading patterns rather than inventing another parser or authority family.

[Back to top](#top)

---

<a id="8-binding-semantics-and-finite-outcomes"></a>

## 8. Binding semantics and finite outcomes

Inventory binding is required only when the validated BriefingSignal route is
`UPDATE_EXISTING_ISSUE`. Other routes retain `inventory_status = NOT_REQUIRED`.

The shared binding function uses the signal's declared `matched_issue_ids` only
as requested target candidates. It independently checks those IDs against the
validated inventory input.

| Condition | Router result | Stable inventory marker / reason |
|---|---|---|
| Route is not `UPDATE_EXISTING_ISSUE` | Keep declared route | `NOT_REQUIRED` |
| Required inventory absent | `HOLD_FOR_DEPENDENCY` | `REQUIRED` / `ISSUE_INVENTORY_REQUIRED` |
| Inventory payload structurally unavailable | `HOLD_FOR_DEPENDENCY` | `INVALID` / `ISSUE_INVENTORY_INVALID` |
| At least one declared target missing | `HOLD_FOR_DEPENDENCY` | `TARGET_MISSING` / `ISSUE_INVENTORY_TARGET_MISSING` |
| No declared target open | `HOLD_FOR_DEPENDENCY` | `TARGET_CLOSED` / `ISSUE_INVENTORY_TARGET_CLOSED` |
| More than one declared target open | `HOLD_FOR_DEPENDENCY` | `AMBIGUOUS_OPEN_TARGETS` / `ISSUE_INVENTORY_AMBIGUOUS_OPEN_TARGETS` |
| Exactly one declared target open and none missing | Keep `UPDATE_EXISTING_ISSUE` proposal | `BOUND_OPEN_TARGET` / `ISSUE_INVENTORY_OPEN_TARGET` |
| Same successful binding through the stored-read option | Keep `UPDATE_EXISTING_ISSUE` proposal | `BOUND_OPEN_TARGET_LIVE_READ` plus `ISSUE_INVENTORY_LIVE_READ_FRESH` |
| Fixture and stored-read options both supplied | Report-level `FAIL` before signal evaluation | `ISSUE_INVENTORY_INPUT_AMBIGUOUS` |
| Stored read lacks explicit `as_of` | Report-level `FAIL` before signal evaluation | `LIVE_ISSUE_INVENTORY_AS_OF_REQUIRED` |
| Stored-read validation fails | Report-level `FAIL` before signal evaluation | Prefixed validator finding codes |

A successful route remains data describing a proposed next action. The report
always fixes `authority_created` and `repository_mutation_allowed` to false.

### 8.1 Write-time race boundary

Even a genuinely live record can become stale between read and any future
write. The current architecture avoids that race by implementing no writer. Any
future writer would require a separate authority decision and must re-read or
apply an equivalent GitHub concurrency precondition at write time. It must not
trust a stored routing receipt as an atomic write authorization.

### 8.2 No issue-body authority

An open issue may be stale, mistaken, superseded, unsafe, or scoped differently
from a signal. This binding checks only numeric target identity and open/closed
state. Human review remains responsible for deciding whether and how the signal
belongs in that issue.

[Back to top](#top)

---

<a id="9-identity-freshness-and-replay"></a>

## 9. Identity, freshness, and replay

### 9.1 Record digest

The current record digest uses canonical compact JSON with sorted keys and
excludes only the two self-referential fields:

```text
response_digest = "sha256:" + SHA256(canonical(record - receipt_id - response_digest))
receipt_id       = "kfm:github-issue-read:" + digest_hex[0:24]
```

Repository identity, numeric repository ID, recorded branch/head, requested
issue set, minimized rows, retrieval/stale times, rate-limit metadata, outcomes,
and fixed-false effects all participate in identity.

### 9.2 Freshness is not currentness proof

The current five-minute default is a producer profile value, not accepted KFM
policy. `FRESH` means that the record was evaluated inside its declared window;
it does not guarantee that GitHub state did not change during that window.

### 9.3 Replay law

- deterministic tests must provide explicit `--now` or `--as-of` values;
- the router must not consult wall-clock time for stored-record replay;
- an expired record may remain useful as immutable test/history input but must
  not route a current operation;
- refreshing a record produces a new digest and receipt ID rather than rewriting
  the old identity;
- fixture provenance and live acquisition provenance must remain distinguishable
  even when their machine shape is identical.

### 9.4 Retention remains unresolved

The current repository proves a fixture home, not a production retention policy
for real read observations. Real outputs may contain only minimized public issue
metadata, but their lifecycle, expiry, audit value, access class, correction, and
physical storage still require an explicit responsibility decision. Do not place
live outputs in the fixture lane or create a parallel receipt home by
convenience.

[Back to top](#top)

---

<a id="10-security-credentials-and-minimization"></a>

## 10. Security, credentials, and minimization

### 10.1 Current controls

- live requests use HTTP `GET` only;
- credentials are read from environment variables and are not serialized into
  output;
- errors expose only a finite outcome and exception class, not the token;
- the router and stored validator never call the network;
- issue rows omit title, body, comments, labels, assignees, milestone, project,
  reactions, author identity, and permissions;
- pull-request-shaped responses from the Issues API are rejected;
- all authority, evidence, release, publication, public-use, and repository-write
  effects are fixed false;
- current GitHub Actions jobs use read-only `contents: read` permissions and
  fixture transport.

### 10.2 Controls not established

- an approved fine-grained token definition and scope audit;
- a private operator/incident route for credential failures;
- secret scanning of operator output destinations;
- transport retry, backoff, conditional requests, or circuit breaking;
- a governed retention/expiry policy for live read records;
- a producer signature or attestation proving live versus fixture acquisition;
- an operational audit trail that binds actor, command, environment, and output;
- a write-capable adapter, permission check, or authorization record.

A broad token used with GET-only code does not become a read-only credential.
Operational admission must constrain both the code path and the credential's
platform scope.

### 10.3 Value-minimization consequence

Minimization reduces exposure and keeps routing deterministic, but it also means
the inventory cannot determine semantic fit. The absence of titles, bodies,
labels, and comments is intentional. Do not widen the read profile merely to
avoid human review.

[Back to top](#top)

---

<a id="validation"></a>

## Validation

### 11.1 Focused executable coverage present

| Test or workflow | Current bounded coverage |
|---|---|
| [`test_github_issue_inventory_read.py`](../../tests/governance/test_github_issue_inventory_read.py) | Fixture-mode record construction, closed schema, fixed-false effects, ref mismatch, pull-request rejection, rate-limit hold, stale helper, deterministic identity |
| [`test_briefing_signal_issue_inventory.py`](../../tests/governance/test_briefing_signal_issue_inventory.py) | Fixture projection binding, absent/missing/closed/ambiguous/open target behavior |
| [`test_briefing_signal_live_issue_inventory.py`](../../tests/governance/test_briefing_signal_live_issue_inventory.py) | Stored-record digest/ID replay, successful stored-read binding, stale rejection, required `as_of`, mutually exclusive inputs, explicit no-network assertion |
| [`github-issue-inventory-read.yml`](../../.github/workflows/github-issue-inventory-read.yml) | Compiles probe/tests, runs adapter tests, replays fixture transport with no credential, records read-only boundary |
| [`briefing-integration.yml`](../../.github/workflows/briefing-integration.yml) | Discovers all `test_briefing_signal*.py` tests, validates briefing and projection fixtures, and exercises projection-bound routing plus adjacent briefing foundations |

### 11.2 Workflow-coverage boundaries

Current workflow path filters are split:

- the adapter workflow watches the live-read contract, schema, fixtures, probe,
  adapter test, and its workflow;
- the briefing workflow watches governance validators/tests and briefing
  fixtures/examples, but its explicit routing command uses the deterministic
  `IssueInventoryProjection` path;
- the broad briefing unittest discovery does execute the stored-read binding
  test when that workflow runs;
- this architecture note itself is not currently in either specialized
  workflow's path filters.

Therefore a documentation-only edit to this page does **not** prove that the
adapter or binding tests re-ran. Repository-wide documentation, metadata, link,
document-graph, topology, security, and aggregate checks may still run, but they
must not be described as stored-read runtime proof.

### 11.3 Coverage gap

A change to the live-read contract/schema/fixture and a change to the stored
validator/router are not guaranteed by one dedicated path-filtered workflow to
exercise the complete producer -> stored validator -> router chain. Aggregate
checks may add coverage, but exact required-check coupling remains
`NEEDS VERIFICATION`. A later workflow change should close this deliberately,
not by weakening path filters or declaring documentation success sufficient.

### 11.4 Commands for a checkout

These are current repository commands to run in a suitable checkout; this page
does not claim they ran merely because they are documented.

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python -m pytest -q \
  tests/governance/test_github_issue_inventory_read.py \
  tests/governance/test_briefing_signal_issue_inventory.py \
  tests/governance/test_briefing_signal_live_issue_inventory.py
```

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/probes/github_issue_inventory_read.py \
  --repository bartytime4life/Kansas-Frontier-Matrix \
  --issue 1647 --issue 1675 \
  --now 2026-08-08T02:30:00Z \
  --fixture fixtures/contracts/v1/governance/github_issue_inventory_read/api_fixture.json
```

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/governance/route_briefing_signals.py \
  --github-issue-inventory-read \
  fixtures/contracts/v1/governance/github_issue_inventory_read/fresh_receipt_1647.json \
  --as-of 2026-08-08T02:31:00Z \
  examples/briefing_integration/*.json
```

The second and third commands are deterministic fixture/replay demonstrations.
They do not observe current GitHub state.

[Back to top](#top)

---

<a id="12-current-gaps-and-stop-conditions"></a>

## 12. Current gaps and stop conditions

### 12.1 Confirmed or bounded gaps

| Gap | Current status | Why it matters |
|---|---|---|
| Checked-in “fresh” record is fixture-derived | `CONFIRMED` | Prevents test data from being presented as current platform evidence |
| Profile remains `PROPOSED_INACTIVE` | `CONFIRMED` | Code presence is not operational admission |
| No authorized live-read operator/runbook | `UNKNOWN` | There is no accountable operational route to invoke and retain live results |
| No least-privilege token profile or scope verification | `NEEDS VERIFICATION` | GET-only code does not constrain platform token capability |
| No live/fixture producer attestation field | `CONFIRMED absence in current shape` | Machine shape alone cannot establish acquisition provenance |
| Stored validator lacks several hardened JSON input controls | `CONFIRMED` | Closed schema should not be overstated as duplicate-key/size/canonical-time protection |
| Stored validator does not compare recorded head to current consuming head | `CONFIRMED` | Digest binding is not current repository-head verification |
| No write-time re-read/concurrency contract | `NOT IMPLEMENTED` | A future writer cannot safely rely on a stored read |
| No authorized issue writer | `NOT IMPLEMENTED` | Routing remains proposal-only by design |
| No production retention/correction policy for real read records | `UNKNOWN / HOLD` | Real outputs must not be placed in fixtures or an invented parallel receipt home |
| Specialized workflow closure is split | `CONFIRMED` | Producer, consumer, and documentation changes do not all trigger one complete chain |
| Target-document archive migration | `HOLD` | The receiving history/archive lane, links, identity, and rollback are not closed |

### 12.2 Hard stop conditions

Do not activate or widen this seam when any of these remains true for the
requested operation:

- the operator and credential authority are unresolved;
- a fixture is being represented as live evidence;
- the stored record is stale, malformed, non-`FRESH`, digest-mismatched, or
  temporally inconsistent;
- repository/ref binding is missing;
- more than one declared target is open, a target is missing, or no target is
  open;
- the requested action needs issue content that the minimized profile does not
  carry;
- a write would rely on the stored read without a write-time recheck;
- the proposed implementation combines reading and writing in one unreviewed
  path;
- secrets, permissions, retention, audit, correction, or rollback are unclear;
- the change would imply source, evidence, policy, review, release, deployment,
  publication, or public-use authority.

`HOLD` is the expected safe result, not a reason to fall back to candidate-supplied
issue IDs or a synthetic fixture.

[Back to top](#top)

---

<a id="13-graduation-plan"></a>

## 13. Graduation plan

The current binding is sufficient as a synthetic/no-network proof. Operational
graduation should remain dependency-ordered and separately reviewable.

| Order | Smallest bounded change | Acceptance evidence | Non-effect |
|---:|---|---|---|
| 1 | Harden stored JSON loading and timestamp checks using existing repository patterns | Positive and single-fault negative fixtures for duplicate keys, oversize, non-finite values, canonical timestamps, and finding bounds | No network or GitHub mutation |
| 2 | Add one complete fixture producer -> schema/semantic validator -> stored validator -> router replay test | Exact deterministic output and fail-closed mutation of each identity/freshness/issue-set field | Fixture proof only |
| 3 | Reconcile specialized workflow path filters and check ownership | Exact-head runs prove the complete chain for every changed authority surface; no gate weakened | No live credential |
| 4 | Decide real-read retention, provenance, expiry, access, and correction responsibility | Accepted placement/handling decision, no fixture-lane misuse, secure local or CI artifact procedure | No writer or public use |
| 5 | Define and review a least-privilege live-read operator profile | Fine-grained read scope, secret-handling review, explicit command, audit metadata, rate-limit/error behavior, rollback | No issue mutation |
| 6 | Execute one bounded live-read rehearsal only after the prior gates close | Redacted/minimized receipt, exact repository/ref binding, no secret leakage, stale-state test, human review | Observation only |
| 7 | Consider a writer only through a separate architecture/governance packet | Explicit operation allowlist, write-time re-read/concurrency control, permissions, human confirmation, audit/correction/rollback, negative tests | No automatic approval, merge, release, or publication |

A writer is not the natural “next line” of this probe. It is a separate trust and
platform boundary with a different authority owner.

[Back to top](#top)

---

<a id="trust-boundary"></a>

## Trust boundary

This seam may support one bounded statement:

> At a recorded time, a validated minimized inventory input represented exactly
> one declared target as open, so the dry-run router preserved an
> `UPDATE_EXISTING_ISSUE` proposal.

It may not support any of these statements without separate evidence and
authority:

- the issue is still open now;
- the signal belongs in the issue semantically;
- the issue body or comments are true;
- the actor may edit the issue;
- the repository allows the proposed mutation;
- policy, review, source, evidence, lifecycle, proof, release, deployment, or
  publication gates passed;
- an issue update completed;
- KFM published anything.

All current outward reports preserve:

```json
{
  "authority_created": false,
  "repository_mutation_allowed": false
}
```

The live-read shape additionally fixes `evidence_created`, `release_authorized`,
`publication_authorized`, and `public_use_allowed` to false.

[Back to top](#top)

---

<a id="directory-rules-basis"></a>

## Directory Rules basis

Accepted ADR-0029 makes the exact Directory Rules v2 bytes the controlling
placement authority.

### 15.1 Current placement result

This update returns `PLACE` for the existing file because it is a human-readable
cross-root implementation-boundary note and the user requested an in-place
update. It does not create a new path or change an authority owner.

| Artifact | Owning responsibility root | Current home |
|---|---|---|
| Human architecture/integration explanation | `docs/` | `docs/architecture/` |
| Semantic meaning | `contracts/` | `contracts/governance/` |
| Machine shape | `schemas/` | `schemas/contracts/v1/governance/` |
| Diagnostic repository read probe | `tools/` | `tools/probes/` |
| Reusable deterministic validators/router | `tools/` | `tools/validators/governance/` |
| Synthetic producer and replay inputs | `fixtures/` | `fixtures/contracts/v1/governance/` |
| Conformance tests | `tests/` | `tests/governance/` |
| GitHub orchestration | `.github/` | `.github/workflows/` |

No schema, contract, policy, source, evidence, receipt, release, proof, or
publication authority is duplicated in this page.

### 15.2 Structural migration remains on HOLD

The current architecture convergence plan classifies this page as a dated
implementation repair note and keeps migration to a history/report/archive lane
on `HOLD`. That structural question is not resolved by modernizing the text.

A later migration requires, at minimum:

1. a verified receiving-lane contract;
2. complete source/target comparison;
3. inbound links and fragment inventory;
4. `doc_id`, title, status, and supersession continuity;
5. durable separation from [`briefing-integration.md`](briefing-integration.md);
6. updated navigation and document registry consumers;
7. changed-area documentation, graph, link, metadata, and topology checks; and
8. a reversible redirect/tombstone or other reviewed compatibility treatment.

Do not create a parallel “new,” “final,” or archived copy while this path remains
writable.

[Back to top](#top)

---

<a id="16-change-discipline"></a>

## 16. Change discipline

A future material change to this seam should identify the affected authority
families explicitly.

| Change | Required companion review |
|---|---|
| Record fields or outcomes | Contract, schema, fixture polarity, validator, tests, compatibility |
| Digest or ID grammar | Identity migration, historical fixture preservation, replay tests |
| Freshness window | Versioned profile, boundary fixtures, operations review |
| API fields or endpoints | Minimization, rights/privacy, rate-limit, transport, fixture update |
| Credential handling | Security review, least privilege, audit, incident/correction path |
| Router reason codes | Briefing contract, tests, downstream consumer compatibility |
| Workflow path filters/check names | Workflow security, required-check significance, exact-head evidence |
| Retention/storage | Directory Rules, access, expiry, correction, audit, rollback |
| Any GitHub write | Separate accepted authority and implementation packet; never implied by this read profile |

Historical test fixtures should be corrected by successor identity when their
identity-bearing fields change. Do not rewrite them to look like current live
records.

[Back to top](#top)

---

<a id="rollback"></a>

## Rollback

### 17.1 This documentation update

Before merge, close the draft pull request and retire its task branch if
appropriate. After an authorized merge, revert the one documentation commit or
restore prior blob `7c0d7740a7419a34f3acd868521c450ab796a8d8` through normal review.
No GitHub issue, credential, source, lifecycle record, cache, release,
deployment, or public artifact requires operational rollback because this change
is documentation-only.

### 17.2 Current implementation seam

The historical router repair can be disabled by removing the stored-read option
through a reviewed code revert while retaining the fixture-backed
`IssueInventoryProjection` path. That is repository rollback only; no external
issue mutation was produced by the seam.

### 17.3 Stale or incorrect read record

- stop using the record for current routing;
- retain its identity when needed for test/audit lineage;
- emit or capture a successor record rather than overwriting it;
- preserve the reason it was invalidated, expired, or superseded;
- rerun binding only with a validated in-window record;
- never “correct” platform state by editing a stored receipt.

### 17.4 Future writer boundary

If a separately authorized writer ever changes a GitHub issue, repository
rollback is not sufficient. The writer's own contract must define the inverse or
corrective platform action, actor/review evidence, idempotency, concurrency,
audit trail, and failure recovery. None of that authority is created here.

[Back to top](#top)

---

<a id="18-related-surfaces"></a>

## 18. Related surfaces

- [`briefing-integration.md`](briefing-integration.md) — durable whole-system
  briefing architecture and current bounded foundations.
- [`IssueInventoryProjection`](../../contracts/governance/issue_inventory_projection.md)
  — deterministic fixture profile and shared binding semantics.
- [`GitHubIssueInventoryRead`](../../contracts/governance/github_issue_inventory_read.md)
  — minimized read-observation semantics.
- [`github_issue_inventory_read.py`](../../tools/probes/github_issue_inventory_read.py)
  — explicit fixture/live producer.
- [`route_briefing_signals.py`](../../tools/validators/governance/route_briefing_signals.py)
  — no-network consumer and dry-run report.
- [`document-convergence-plan.md`](document-convergence-plan.md) — structural
  documentation disposition and migration HOLD.
- [`Directory Rules v2`](../doctrine/directory-rules.md) and
  [`ADR-0029`](../adr/ADR-0029-adopt-directory-governance-standard-v2.md) —
  controlling placement authority.

[Back to top](#top)

---

<a id="appendix-a-field-map"></a>

## Appendix A — `GitHubIssueInventoryRead` field map

| Field family | Current fields | Boundary |
|---|---|---|
| Shape/profile | `schema_version`, `profile_state` | Profile is fixed to `1.0.0` / `PROPOSED_INACTIVE` |
| Identity | `receipt_id`, `response_digest` | Deterministic content binding, not authenticity or platform authority |
| Finite state | `outcome` | Read-observation state only |
| Repository binding | `repository`, `repository_id`, `default_branch`, `default_branch_head_sha` | Recorded context, not a consume-time equality check |
| Requested set | `requested_issue_ids` | Explicit sorted unique positive issue IDs; schema maximum 64 |
| Minimized rows | `issues[].number`, `issues[].state`, `issues[].updated_at` | No semantic issue content or permissions |
| Freshness | `retrieved_at`, `stale_at` | Declared window, not atomic currentness |
| Rate limit | `rate_limit_remaining`, `rate_limit_reset_at` | Optional headers; explicit zero yields hold in current producer |
| Fixed non-effects | `repository_mutation_allowed`, `authority_created`, `evidence_created`, `release_authorized`, `publication_authorized`, `public_use_allowed` | Every value fixed false |

[Back to top](#top)

---

<a id="appendix-b-no-loss-ledger"></a>

## Appendix B — No-loss modernization ledger

| Prior section or statement | Current location | Treatment |
|---|---|---|
| Introductory proposed/non-authoritative boundary | Status table, §§1, 14 | Preserved and made repository-current |
| PR #2179/#2180 merge-context explanation | §2.1 | Preserved; completed with PR #2292 repair evidence |
| Original fail-closed routing diagram | [Fail-closed routing](#fail-closed-routing) | Preserved and expanded into separate acquisition/consumption paths |
| Mutual exclusion and explicit `--as-of` | §§4, 7, 8 | Preserved |
| `BOUND_OPEN_TARGET_LIVE_READ` and `ISSUE_INVENTORY_LIVE_READ_FRESH` | §8 | Preserved |
| Focused validation commands | [Validation](#validation) | Preserved, corrected as fixture/replay commands, and expanded with adapter coverage |
| Trust boundary | [Trust boundary](#trust-boundary) | Preserved and expanded |
| Directory Rules basis | [Directory Rules basis](#directory-rules-basis) | Preserved; reconciled with accepted ADR-0029 and convergence-plan HOLD |
| Rollback | [Rollback](#rollback) | Preserved and separated by documentation, code seam, stored record, and future writer |

[Back to top](#top)

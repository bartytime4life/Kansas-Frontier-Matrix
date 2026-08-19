<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-architecture-briefing-live-issue-inventory-binding
title: Briefing Live Issue Inventory Binding — Current Repository Boundary
type: architecture/implementation-note
version: v1.0-draft
status: "draft; repository-grounded; implementation-present; profile-proposed-inactive; non-authoritative; no-live-activation; no-repository-mutation; structural-migration-hold"
owners:
  - "@bartytime4life — verified CODEOWNERS review route only"
  - "NEEDS VERIFICATION — accountable architecture, governance, briefing-integration, GitHub-integration, validation, security, and operations stewards"
created: 2026-08-08
updated: 2026-08-19
policy_label: "repository-facing; internal-control-plane; read-only; value-minimized; no-public-authority; no-repository-mutation"
owning_root: docs/
responsibility: "Explain the current BriefingSignal-to-issue-inventory routing seam, preserve its repair lineage, distinguish synthetic replay from live observation, and define its no-network, no-write, freshness, identity, minimization, validation, correction, graduation, and rollback boundaries."
truth_posture: "CONFIRMED accepted Directory Rules, current repository bytes, focused tests, workflow definitions, CODEOWNERS route, and PR #2179/#2180/#2292 lineage / PROPOSED operational hardening, workflow closure, retention, and graduation / UNKNOWN approved live-read operator, least-privilege credential profile, production retention and audit lane, authorized writer, deployed consumer, required-check coupling, and runtime operation."
evidence_snapshot:
  - "Repository checkpoint: main@8d2535d3231c81b3d7bc32dff660ad8cc7983f64"
  - "Target prior blob: 7c0d7740a7419a34f3acd868521c450ab796a8d8"
  - "Accepted placement decision: ADR-0029"
  - "Implementation lineage: PR #2179, PR #2180, and PR #2292"
  - "Checked-in stored record is fixture-derived and is not current GitHub evidence"
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
  - "The live probe exists, but the schema fixes profile_state to PROPOSED_INACTIVE and normal CI exercises fixture transport only."
  - "The architecture convergence plan keeps structural migration of this dated implementation note on HOLD."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>
<a id="briefing-live-issue-inventory-binding"></a>

# Briefing Live Issue Inventory Binding — Current Repository Boundary

> **Purpose.** Explain what the repository currently implements when a validated
> `BriefingSignal` names an existing GitHub issue, how deterministic fixtures and
> stored read records remain separate, why every route is still a proposal, and
> what must close before any operational live read or issue write can be admitted.

> [!IMPORTANT]
> **The binding is present on current `main`, but it creates no write authority.**
> A successful binding can preserve the dry-run disposition
> `UPDATE_EXISTING_ISSUE`; it cannot open, edit, label, assign, comment on, close,
> reopen, transfer, lock, merge, or otherwise mutate a GitHub object.

> [!CAUTION]
> **`fresh_receipt_1647.json` is deterministic test material, not a live
> inventory.** It is generated from the checked-in `api_fixture.json`. Its
> `FRESH` value means only that the replay time is inside the fixture's declared
> five-minute window.

> [!WARNING]
> **Read-only code is not operational admission.** The probe contains an explicit
> HTTP `GET` mode, but `GitHubIssueInventoryRead.profile_state` is fixed to
> `PROPOSED_INACTIVE`; normal CI supplies no live credential and performs no live
> GitHub read.

| Field | Current bounded result |
|---|---|
| Repository checkpoint | `main@8d2535d3231c81b3d7bc32dff660ad8cc7983f64` |
| Placement result | `PLACE` at the existing path for this correction; structural migration remains `HOLD` |
| Placement authority | [`ADR-0029`](../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts [`Directory Rules v2`](../doctrine/directory-rules.md) |
| Adapter/profile state | Implementation present; contract/schema profile `PROPOSED_INACTIVE` |
| Router network posture | No network; consumes validated local files only |
| Probe network posture | Explicit operator invocation only; GET-only implementation; no normal-CI live call |
| Checked-in stored record | Fixture-derived, historical replay specimen; not current GitHub evidence |
| Current writer | None in this object family or router |
| Review route | `@bartytime4life` through [`CODEOWNERS`](../../.github/CODEOWNERS); routing is not stewardship, independent review, or approval |
| Evidence, policy, release, or publication effect | None |

**Quick navigation:** [Scope](#1-goal-and-scope) · [Evidence](#2-evidence-and-lineage) · [Responsibilities](#3-current-responsibility-map) · [Routing](#fail-closed-routing) · [Inputs](#5-two-input-families) · [Probe](#6-github-read-acquisition-profile) · [Stored validation](#7-stored-read-validation) · [Binding](#8-binding-semantics-and-finite-outcomes) · [Identity](#9-identity-freshness-and-replay) · [Security](#10-security-credentials-and-minimization) · [Validation](#validation) · [Gaps](#12-current-gaps-and-stop-conditions) · [Graduation](#13-graduation-plan) · [Trust](#trust-boundary) · [Placement](#directory-rules-basis) · [Rollback](#rollback)

---

<a id="1-goal-and-scope"></a>

## 1. Goal and scope

This page is the narrow implementation-boundary companion to
[`briefing-integration.md`](briefing-integration.md). The durable briefing page
owns the whole briefing-to-system architecture. This page owns only this seam:

```text
BriefingSignal declares an existing-issue route
  -> one read-only inventory input family
  -> deterministic validation
  -> exactly-one-open-target binding or fail-closed hold/failure
  -> value-minimized routing proposal
```

### In scope

- fixture and stored-read profile separation;
- acquisition versus no-network consumption;
- stored-record validation with explicit replay time;
- issue-set binding and finite routing outcomes;
- data minimization, credentials, and fixed-false authority effects;
- current tests and workflow coverage;
- gaps, stop conditions, graduation, correction, and rollback;
- the stacked-PR repair that made the binding present on current `main`.

### Out of scope

- deciding whether issue prose, comments, labels, or attachments are true;
- searching the entire issue portfolio or selecting work from issue text;
- Projects V2, milestones, dependencies, sub-issues, assignees, reviewers,
  permissions, rulesets, branch protection, or merge authority;
- a long-lived issue-state database, cache, event stream, or watcher;
- source admission, `EvidenceBundle` creation, policy, review, promotion, proof,
  release, deployment, publication, or public use;
- every GitHub write operation.

The terms **live**, **read**, **receipt**, **fresh**, and **bound** describe a
bounded observation or replay contract. They are not authority labels.

[Back to top](#top)

---

<a id="2-evidence-and-lineage"></a>

## 2. Evidence and lineage

### 2.1 Implementation lineage

| Change | Confirmed repository result | Boundary |
|---|---|---|
| [PR #2179](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/2179) | Added the `GitHubIssueInventoryRead` contract, closed schema, fixture transport, GET-only diagnostic probe, adapter tests, and fixture-only workflow; merged as `7f402354df34ebccb81d64ea6d235f2e1bae8b07` | Deliberately did not bind the profile into BriefingSignal routing |
| [PR #2180](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/2180) | Added stored-read validation and router binding on a branch stacked on the already-merged #2179 branch; merged there as `2666813a3d5ff2c539fffc88856fc579290cd0c2` | Its integration bytes did not reach default-branch history through that stacked merge context |
| [PR #2292](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/2292) | Replayed the five dependency-closed integration files onto then-current `main`; merged as `38cece49b89687416b13b806ec64d61f3f174387` | Restored only no-network stored-record binding; no mutation or live activation |
| Current `main` | Contains the contract/schema/probe, stored validator, router option, fixtures, focused tests, and both workflow lanes | Presence proves repository bytes, not an operational live service or writer |

### 2.2 Evidence hierarchy for this seam

1. accepted Directory Rules and applicable accepted ADRs;
2. current contracts and closed schemas;
3. current probe, validators, router, tests, and workflows;
4. checked-in fixtures as deterministic test inputs only;
5. this page and historical PR descriptions as explanatory lineage.

The Briefing-to-System doctrine remains controlling at architecture rank:
briefing prose is a discovery signal, not evidence or publication authority.
Current repository bytes control the narrower claim about present implementation.

### 2.3 Fixture/current-state contrast

The stored test record declares issue `#1647` open inside a synthetic August 8
replay. At this page's refresh, GitHub reports
[`#1647`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/1647)
closed. This contrast demonstrates the governing rule: a checked-in fixture or
expired observation can prove replay behavior, never current platform state.

[Back to top](#top)

---

<a id="3-current-responsibility-map"></a>

## 3. Current responsibility map

| Surface | Current responsibility | Does not own |
|---|---|---|
| [`IssueInventoryProjection`](../../contracts/governance/issue_inventory_projection.md) | Deterministic fixture-backed issue-state projection | Live GitHub state, evidence, permissions, mutation |
| [`GitHubIssueInventoryRead`](../../contracts/governance/github_issue_inventory_read.md) | Minimized, repository/ref-bound read observation and finite read outcomes | Issue truth, writer authorization, review, release, publication |
| [`github_issue_inventory_read.schema.json`](../../schemas/contracts/v1/governance/github_issue_inventory_read.schema.json) | Closed Draft 2020-12 machine shape and fixed-false effects | Operational admission or currentness beyond recorded fields |
| [`github_issue_inventory_read.py`](../../tools/probes/github_issue_inventory_read.py) | Fixture-mode or explicitly invoked GET-only record production | Scheduling, canonical storage, mutation, router execution |
| [`validate_issue_inventory_projection.py`](../../tools/validators/governance/validate_issue_inventory_projection.py) | Fixture projection validation and shared issue-set binding semantics | Live acquisition or mutation |
| [`validate_github_issue_inventory_read.py`](../../tools/validators/governance/validate_github_issue_inventory_read.py) | Stored-record shape, identity, issue-set, `FRESH`, and replay-time validation | Network access, current-state reread, write concurrency |
| [`route_briefing_signals.py`](../../tools/validators/governance/route_briefing_signals.py) | Deterministic value-minimized routing report from local inputs | Network, issue writes, evidence, policy, review, release |
| [`api_fixture.json`](../../fixtures/contracts/v1/governance/github_issue_inventory_read/api_fixture.json) | Synthetic API-shaped producer input | Historical or current GitHub fact |
| [`fresh_receipt_1647.json`](../../fixtures/contracts/v1/governance/github_issue_inventory_read/fresh_receipt_1647.json) | Deterministic stored-record replay specimen | Current issue state or authenticated live receipt |
| Focused tests | Positive and negative behavior over synthetic inputs | Platform permissions, deployment, live currentness |
| Workflows | Bounded read-only orchestration over repository bytes | Operational activation, human approval, publication |
| This page | Composition, lineage, limits, and graduation | Contract, schema, policy, platform, release authority |

Producer relationships do not collapse responsibility. The probe produces a
record; a validator checks it; the router consumes it. Each remains in its own
responsibility root.

[Back to top](#top)

---

<a id="fail-closed-routing"></a>

## Fail-closed routing

Acquisition and consumption are separate so routing remains deterministic and
no-network:

```text
PATH A — deterministic contract profile

checked-in IssueInventoryProjection
  -> validate shape, time, issue set, digest, identity
  -> bind declared issue IDs
  -> routing proposal or fail-closed HOLD

PATH B — optional read-observation profile

explicit operator invocation
  -> GET repository metadata
  -> GET default-branch ref
  -> GET each explicitly requested issue
  -> value-minimized GitHubIssueInventoryRead JSON
  -> approved local handling, if established
  -> no-network stored-record validation with explicit --as-of
  -> shared issue-set binding
  -> routing proposal or fail-closed failure/HOLD
```

```text
BriefingSignal
  -> deterministic declared route
  -> exactly one inventory family
  -> input validation
  -> issue-set binding
  -> UPDATE_EXISTING_ISSUE proposal
       OR HOLD_FOR_DEPENDENCY
       OR FAIL
  -X-> GitHub mutation
```

The router rejects simultaneous fixture and stored-read inputs. A stored record
requires explicit `--as-of`; wall-clock time is never used implicitly. Invalid
stored input fails before signal routing.

[Back to top](#top)

---

<a id="5-two-input-families"></a>

## 5. Two input families

| Dimension | `IssueInventoryProjection` | `GitHubIssueInventoryRead` |
|---|---|---|
| Purpose | Deterministic contract fixture | Minimized explicitly invoked read observation |
| Contract status | `PROPOSED`, fixture-backed | `PROPOSED_INACTIVE` |
| Producer | Checked-in fixture construction | Probe fixture mode or explicit GET mode |
| Network | Never | Explicit live mode only |
| Router input | Local projection file | Local stored-read file |
| Binding | Repository and fixture provenance | Repository ID, default branch, recorded head SHA |
| Issue fields | Number, state, update time | Number, state, update time |
| Time | Projection generation time | `retrieved_at`, `stale_at`, explicit `as_of` |
| Identity | Projection digest and 16-hex ID | Response digest and 24-hex receipt ID |
| Live-state claim | Fixed false | Bounded only when actually acquired live; checked-in specimens are synthetic |
| Mutation/public effects | Fixed false | Six trust-bearing effect flags fixed false |

### 5.1 Fixture law

Fixtures may simulate API responses, branch heads, issue states, timestamps, and
rate-limit headers to prove code behavior. They must remain synthetic and may
never be reused as platform evidence.

### 5.2 Stored-read law

Machine shape does not prove acquisition mode. The current schema binds record
content but has no producer-mode attestation. Repository provenance therefore
classifies the checked-in specimen as fixture-derived.

### 5.3 No fallback

Unavailable, stale, malformed, unauthenticated, or held live state must not fall
back to a fixture described as current. Fixture use is explicit and test-only.

[Back to top](#top)

---

<a id="6-github-read-acquisition-profile"></a>

## 6. GitHub read acquisition profile

The probe's current sequence is:

1. `GET /repos/{repository}`;
2. `GET /repos/{repository}/git/ref/heads/{branch}`;
3. `GET /repos/{repository}/issues/{number}` for each explicit ID;
4. reject any row containing `pull_request`;
5. retain only number, uppercase state, and `updated_at`;
6. record available rate-limit remaining/reset headers;
7. set `stale_at` from the default 300-second producer window;
8. calculate response digest and receipt ID; and
9. print canonical compact JSON to stdout.

### 6.1 Explicit inputs

- repository in `owner/name` form;
- one or more repeated `--issue` arguments;
- optional `--fixture` for fixture mode;
- optional `--now` for deterministic time;
- `KFM_GITHUB_READ_TOKEN`, then `GITHUB_TOKEN`, in live mode.

### 6.2 Finite producer outcomes

| Outcome | Current meaning |
|---|---|
| `FRESH` | Record built and no explicit zero remaining rate limit was observed |
| `HOLD_RATE_LIMIT` | Merged response headers report zero remaining requests |
| `HOLD_AUTH` | Live mode selected without a token |
| `ERROR` | Transport, parsing, repository/ref, issue-set, PR-object, or local I/O failure |
| `STALE` | Separate freshness helper evaluated after `stale_at` |
| `HOLD_BINDING` | Present in contract/schema vocabulary; current probe surfaces binding failures through `ERROR` rather than this record branch |

An enum value is not proof that every semantic branch is emitted by current code.

### 6.3 Operational limitations

- no scheduled live run or approved operator runbook;
- GET-only code does not verify least-privilege token scope;
- no retry/backoff or conditional requests;
- one request per explicit issue ID; no portfolio pagination/search;
- stdout output with no accepted production retention, redaction, expiry, or
  audit lane;
- producer does not run the repository schema validator before output;
- absent rate-limit headers remain `null` and do not independently block
  `FRESH`;
- caller issue lists reach later schema validation before the closed 64-item cap
  is enforced.

[Back to top](#top)

---

<a id="7-stored-read-validation"></a>

## 7. Stored-read validation

The stored validator makes no network call. It currently:

- rejects symlinks, missing/unreadable files, invalid JSON, non-object roots, and
  closed-schema failures;
- recomputes `response_digest` excluding `receipt_id` and `response_digest`;
- recomputes the deterministic receipt ID;
- requires sorted unique requested IDs;
- requires sorted returned rows matching the requested set exactly;
- requires `outcome == FRESH`; and
- requires explicit `as_of` between `retrieved_at` and `stale_at`.

### 7.1 What a pass proves

A pass proves conformance to the current shape, deterministic identity, exact
issue set, fixed-false effects, and declared replay window. It does not prove:

- live rather than fixture acquisition;
- current issue state at consumption or write time;
- equality between recorded branch head and the consuming checkout;
- correctness of issue content;
- least-privilege producer credentials; or
- mutation permission.

### 7.2 Current hardening gaps

The stored validator does not yet add an explicit input-size cap, duplicate-key
rejection, non-finite-number rejection, canonical UTC-second enforcement for all
timestamps, bounded schema findings, or producer-mode attestation. The closed
schema catches many malformed shapes but must not be overstated as those
additional defenses.

[Back to top](#top)

---

<a id="8-binding-semantics-and-finite-outcomes"></a>

## 8. Binding semantics and finite outcomes

Inventory binding is required only for `UPDATE_EXISTING_ISSUE`. Other routes use
`inventory_status = NOT_REQUIRED`.

| Condition | Router result | Marker or reason |
|---|---|---|
| Route does not update an existing issue | Keep declared route | `NOT_REQUIRED` |
| Required inventory absent | `HOLD_FOR_DEPENDENCY` | `REQUIRED` / `ISSUE_INVENTORY_REQUIRED` |
| Inventory invalid/unavailable | `HOLD_FOR_DEPENDENCY` | `INVALID` / `ISSUE_INVENTORY_INVALID` |
| Declared target missing | `HOLD_FOR_DEPENDENCY` | `TARGET_MISSING` / `ISSUE_INVENTORY_TARGET_MISSING` |
| No declared target open | `HOLD_FOR_DEPENDENCY` | `TARGET_CLOSED` / `ISSUE_INVENTORY_TARGET_CLOSED` |
| More than one declared target open | `HOLD_FOR_DEPENDENCY` | `AMBIGUOUS_OPEN_TARGETS` / `ISSUE_INVENTORY_AMBIGUOUS_OPEN_TARGETS` |
| Exactly one declared target open | Keep proposal | `BOUND_OPEN_TARGET` / `ISSUE_INVENTORY_OPEN_TARGET` |
| Same binding through stored-read option | Keep proposal | `BOUND_OPEN_TARGET_LIVE_READ` and `ISSUE_INVENTORY_LIVE_READ_FRESH` |
| Both input families supplied | Report-level `FAIL` | `ISSUE_INVENTORY_INPUT_AMBIGUOUS` |
| Stored read lacks `as_of` | Report-level `FAIL` | `LIVE_ISSUE_INVENTORY_AS_OF_REQUIRED` |
| Stored-read validation fails | Report-level `FAIL` | Prefixed validator finding codes |

Every successful report still fixes `authority_created` and
`repository_mutation_allowed` to false.

### 8.1 Write-time race boundary

A read can become stale before a later write. The current design avoids that race
by implementing no writer. Any future writer needs separate authority and a
write-time reread or equivalent concurrency precondition. A stored routing record
cannot be atomic write authorization.

### 8.2 No issue-body authority

The binding checks numeric identity and open/closed state only. An open issue may
be stale, wrong, superseded, unsafe, or semantically unrelated. Human review
remains responsible for deciding semantic fit.

[Back to top](#top)

---

<a id="9-identity-freshness-and-replay"></a>

## 9. Identity, freshness, and replay

```text
response_digest = "sha256:" + SHA256(canonical(record - receipt_id - response_digest))
receipt_id       = "kfm:github-issue-read:" + digest_hex[0:24]
```

Repository identity, numeric ID, branch/head, issue set, minimized rows,
retrieval/stale times, rate-limit metadata, outcomes, and fixed-false effects all
participate in identity.

### 9.1 Freshness is not currentness proof

The five-minute default is a producer value, not accepted KFM policy. `FRESH`
means only that evaluation occurred inside the declared interval; it cannot
prove GitHub state remained unchanged during that interval.

### 9.2 Replay law

- deterministic tests supply explicit `--now` or `--as-of`;
- stored replay never consults wall-clock time implicitly;
- expired records may remain immutable test/history inputs but cannot route a
  current operation;
- a refresh creates a new digest and receipt ID rather than rewriting the old
  identity;
- fixture and live provenance remain distinguishable even when shape is equal.

### 9.3 Retention remains unresolved

The repository proves a fixture home, not a production home for live read
records. Retention, expiry, access, audit value, correction, and physical storage
need an explicit responsibility decision. Live output must not be placed in
fixtures or an invented parallel receipt lane.

[Back to top](#top)

---

<a id="10-security-credentials-and-minimization"></a>

## 10. Security, credentials, and minimization

### Current controls

- live requests use HTTP `GET` only;
- credentials come from environment variables and are not serialized;
- errors expose finite outcome and exception class, not token value;
- router and stored validator never call the network;
- rows omit title, body, comments, labels, assignees, milestone, project,
  reactions, author identity, and permissions;
- pull-request-shaped issue responses are rejected;
- authority, evidence, release, publication, public-use, and write effects are
  fixed false;
- current workflow jobs use read-only `contents: read` and fixture transport.

### Not established

- approved fine-grained token definition and scope audit;
- private credential-failure route;
- secret scanning of output destinations;
- retry, backoff, conditional requests, or circuit breaking;
- governed live-record retention/expiry;
- live-versus-fixture producer signature/attestation;
- actor/command/environment/output audit trail;
- writer, write permission check, or authorization record.

A broad token does not become read-only merely because code performs GETs.
Operational admission must constrain both code path and platform scope.

[Back to top](#top)

---

<a id="validation"></a>

## Validation

### Focused coverage present

| Test or workflow | Current bounded coverage |
|---|---|
| [`test_github_issue_inventory_read.py`](../../tests/governance/test_github_issue_inventory_read.py) | Fixture construction, closed schema, fixed-false effects, ref mismatch, PR rejection, rate-limit hold, stale helper, deterministic identity |
| [`test_briefing_signal_issue_inventory.py`](../../tests/governance/test_briefing_signal_issue_inventory.py) | Fixture projection binding and absent/missing/closed/ambiguous/open target behavior |
| [`test_briefing_signal_live_issue_inventory.py`](../../tests/governance/test_briefing_signal_live_issue_inventory.py) | Stored digest/ID replay, successful binding, stale rejection, required `as_of`, exclusive inputs, no-network assertion |
| [`github-issue-inventory-read.yml`](../../.github/workflows/github-issue-inventory-read.yml) | Probe/test compilation, adapter tests, fixture transport without credential, read-only boundary |
| [`briefing-integration.yml`](../../.github/workflows/briefing-integration.yml) | Broad BriefingSignal test discovery, fixture validation, and projection-bound routing |

### Workflow boundary

The adapter workflow watches the live-read contract/schema/fixtures/probe/test.
The briefing workflow watches governance validators/tests and briefing fixtures,
but its explicit routing demonstration uses `IssueInventoryProjection`. Its test
discovery does include the stored-read binding test when the workflow runs.

This page itself is not in either specialized workflow's path filter. A
page-only edit therefore does not prove the adapter or binding tests reran.
Repository-wide documentation, metadata, link, graph, topology, security, and
aggregate checks are relevant exact-head evidence, but not runtime proof.

### Coverage gap

No one dedicated path-filtered workflow currently guarantees the complete
producer -> stored validator -> router chain for every changed authority surface.
A later workflow correction should close this deliberately without weakening a
gate or treating documentation success as implementation proof.

### Checkout commands

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

These are current repository commands, not claims that this connector-backed
documentation session executed them. The latter two use fixtures and do not
observe current GitHub state.

[Back to top](#top)

---

<a id="12-current-gaps-and-stop-conditions"></a>

## 12. Current gaps and stop conditions

| Gap | Status | Consequence |
|---|---|---|
| Checked-in “fresh” record is fixture-derived | `CONFIRMED` | Never present it as current platform evidence |
| Profile is `PROPOSED_INACTIVE` | `CONFIRMED` | Code presence is not operational admission |
| Approved operator/runbook | `UNKNOWN` | No accountable live invocation/retention route |
| Least-privilege token profile | `NEEDS VERIFICATION` | GET-only code does not constrain token capability |
| Producer-mode attestation | `NOT IMPLEMENTED` | Shape alone cannot establish acquisition provenance |
| Hardened stored JSON controls | `PARTIAL` | Closed schema must not be overstated |
| Consume-time branch-head equality | `NOT IMPLEMENTED` | Digest binding is not current-head verification |
| Write-time reread/concurrency | `NOT IMPLEMENTED` | Stored reads cannot authorize a future write |
| Authorized issue writer | `NOT IMPLEMENTED` | Routing remains proposal-only |
| Production retention/correction lane | `UNKNOWN / HOLD` | Do not misuse fixtures or invent parallel receipt authority |
| Specialized workflow closure | `PARTIAL` | Producer and consumer changes do not share one complete trigger |
| Structural migration of this page | `HOLD` | Receiving lane, links, identity, and rollback are unresolved |

### Hard stops

Do not activate or widen the seam when:

- operator or credential authority is unresolved;
- a fixture is presented as live evidence;
- the record is stale, malformed, non-`FRESH`, digest-mismatched, or temporally
  inconsistent;
- repository/ref binding is missing;
- targets are missing, all closed, or multiply open;
- the requested decision needs minimized-away issue content;
- a write would trust the stored read without a write-time check;
- reading and writing are collapsed into one unreviewed path;
- secrets, permissions, retention, audit, correction, or rollback are unclear;
- the change implies source, evidence, policy, review, release, deployment,
  publication, or public-use authority.

`HOLD` is the safe outcome, not a reason to trust caller-supplied IDs or fixtures.

[Back to top](#top)

---

<a id="13-graduation-plan"></a>

## 13. Graduation plan

| Order | Smallest bounded change | Acceptance evidence | Non-effect |
|---:|---|---|---|
| 1 | Harden stored JSON and timestamp validation with existing repository patterns | Single-fault fixtures for duplicate keys, oversize, non-finite values, canonical timestamps, bounded findings | No network or mutation |
| 2 | Add complete fixture producer -> semantic/schema validator -> stored validator -> router replay | Deterministic output plus identity/freshness/issue-set negative mutations | Fixture proof only |
| 3 | Reconcile specialized workflow triggers and check ownership | Exact-head runs exercise the whole chain for changed authority surfaces | No live credential |
| 4 | Decide live-read retention, provenance, expiry, access, and correction | Accepted placement/handling decision; no fixture misuse | No writer/public use |
| 5 | Define least-privilege live-read operator profile | Fine-grained scope, secret handling, explicit command, audit metadata, rate-limit/error behavior, rollback | No mutation |
| 6 | Execute one bounded live-read rehearsal | Minimized record, exact repository/ref binding, no secret leakage, stale test, human review | Observation only |
| 7 | Consider a writer through a separate governance packet | Allowlist, write-time reread, permissions, confirmation, audit, correction/rollback, negative tests | No automatic approval, merge, release, or publication |

A writer is not the next line of this probe. It is a separate trust and platform
boundary with a different authority owner.

[Back to top](#top)

---

<a id="trust-boundary"></a>

## Trust boundary

This seam may support one bounded statement:

> At a recorded time, a validated minimized inventory input represented exactly
> one declared target as open, so the dry-run router preserved an
> `UPDATE_EXISTING_ISSUE` proposal.

It cannot establish that:

- the issue is still open;
- the signal belongs in it semantically;
- issue prose is true;
- the actor may edit it;
- repository controls permit a mutation;
- evidence, policy, review, lifecycle, proof, release, deployment, or
  publication gates passed;
- an update occurred; or
- KFM published anything.

```json
{
  "authority_created": false,
  "repository_mutation_allowed": false
}
```

The read shape also fixes `evidence_created`, `release_authorized`,
`publication_authorized`, and `public_use_allowed` to false.

[Back to top](#top)

---

<a id="directory-rules-basis"></a>

## Directory Rules basis

Accepted ADR-0029 makes Directory Rules v2 the controlling placement authority.

### Current placement result

This update returns `PLACE` because this is a human-readable cross-root
implementation-boundary note updated in place. It creates no root or authority.

| Artifact | Owning root | Current home |
|---|---|---|
| Human implementation explanation | `docs/` | `docs/architecture/` |
| Semantic meaning | `contracts/` | `contracts/governance/` |
| Machine shape | `schemas/` | `schemas/contracts/v1/governance/` |
| Diagnostic read probe | `tools/` | `tools/probes/` |
| Validators/router | `tools/` | `tools/validators/governance/` |
| Synthetic inputs | `fixtures/` | `fixtures/contracts/v1/governance/` |
| Conformance tests | `tests/` | `tests/governance/` |
| GitHub orchestration | `.github/` | `.github/workflows/` |

### Structural migration remains on hold

The architecture convergence plan classifies this page as a dated implementation
repair note and holds migration to a history/report/archive lane. A later move
requires:

1. a verified receiving-lane contract;
2. complete source/target comparison;
3. inbound-link and fragment inventory;
4. `doc_id`, title, status, and supersession continuity;
5. separation from [`briefing-integration.md`](briefing-integration.md);
6. navigation and registry updates;
7. documentation, graph, link, metadata, and topology validation; and
8. reversible compatibility treatment.

Do not create a parallel “new,” “final,” or archive copy while this path remains
writable.

[Back to top](#top)

---

<a id="16-change-discipline"></a>

## 16. Change discipline

| Change | Required companion review |
|---|---|
| Record fields/outcomes | Contract, schema, fixtures, validator, tests, compatibility |
| Digest/ID grammar | Identity migration, historical fixture preservation, replay |
| Freshness window | Versioned profile, boundary fixtures, operations review |
| API fields/endpoints | Minimization, privacy/rights, rate limits, transport |
| Credentials | Security, least privilege, audit, incident/correction path |
| Router reason codes | Briefing contract, tests, consumer compatibility |
| Workflow triggers/check names | Workflow security, check significance, exact-head evidence |
| Retention/storage | Directory Rules, access, expiry, correction, audit, rollback |
| Any GitHub write | Separate accepted authority and implementation packet |

Historical fixtures receive successor identity when identity-bearing fields
change. They are never rewritten to look like current live records.

[Back to top](#top)

---

<a id="rollback"></a>

## Rollback

### Documentation update

Before merge, close the draft PR and retire the task branch if appropriate.
After merge, revert the documentation commits or restore prior blob
`7c0d7740a7419a34f3acd868521c450ab796a8d8` through normal review. No external
operational rollback is required for this page-only change.

### Current implementation seam

A reviewed code revert can remove the stored-read router option while retaining
the deterministic `IssueInventoryProjection` path. No external issue mutation
was produced by this seam.

### Stale or incorrect record

- stop using it for current routing;
- retain identity when needed for test/audit lineage;
- capture a successor rather than overwrite;
- preserve invalidation/expiry/supersession reason;
- bind only with a validated in-window record;
- never “correct” GitHub state by editing a stored record.

### Future writer boundary

A future writer requires its own inverse/corrective platform action,
actor/review evidence, idempotency, concurrency, audit trail, and failure
recovery. Repository rollback alone would not reverse an external issue write.

[Back to top](#top)

---

<a id="18-related-surfaces"></a>

## 18. Related surfaces

- [`briefing-integration.md`](briefing-integration.md) — durable briefing
  architecture and current bounded foundations.
- [`IssueInventoryProjection`](../../contracts/governance/issue_inventory_projection.md)
  — deterministic fixture profile and shared binding semantics.
- [`GitHubIssueInventoryRead`](../../contracts/governance/github_issue_inventory_read.md)
  — minimized read-observation semantics.
- [`github_issue_inventory_read.py`](../../tools/probes/github_issue_inventory_read.py)
  — explicit fixture/live producer.
- [`route_briefing_signals.py`](../../tools/validators/governance/route_briefing_signals.py)
  — no-network consumer and dry-run report.
- [`document-convergence-plan.md`](document-convergence-plan.md) — structural
  disposition and migration `HOLD`.
- [`Directory Rules v2`](../doctrine/directory-rules.md) and
  [`ADR-0029`](../adr/ADR-0029-adopt-directory-governance-standard-v2.md) —
  placement authority.

[Back to top](#top)

---

<a id="appendix-a-field-map"></a>

## Appendix A — `GitHubIssueInventoryRead` field map

| Family | Fields | Boundary |
|---|---|---|
| Shape/profile | `schema_version`, `profile_state` | Fixed `1.0.0` / `PROPOSED_INACTIVE` |
| Identity | `receipt_id`, `response_digest` | Content binding, not authenticity or authority |
| State | `outcome` | Read-observation state only |
| Repository | `repository`, `repository_id`, `default_branch`, `default_branch_head_sha` | Recorded context, not consume-time equality |
| Requested set | `requested_issue_ids` | Sorted unique positive IDs; schema maximum 64 |
| Minimized rows | `issues[].number`, `issues[].state`, `issues[].updated_at` | No prose, people, projects, or permissions |
| Freshness | `retrieved_at`, `stale_at` | Declared interval, not atomic currentness |
| Rate limit | `rate_limit_remaining`, `rate_limit_reset_at` | Optional headers; explicit zero holds current producer |
| Non-effects | six fixed-false effect fields | No mutation, authority, evidence, release, publication, or public use |

[Back to top](#top)

---

<a id="appendix-b-no-loss-ledger"></a>

## Appendix B — No-loss modernization ledger

| Prior material | Current location | Treatment |
|---|---|---|
| Proposed/non-authoritative boundary | Status table, §§1 and trust boundary | Preserved and made repository-current |
| PR #2179/#2180 explanation | §2.1 | Preserved and completed with #2292 repair |
| Fail-closed routing | [Fail-closed routing](#fail-closed-routing) | Preserved and separated into acquisition/consumption |
| Exclusive inputs and explicit `as_of` | §§4, 7, and 8 | Preserved |
| Live-read binding markers | §8 | Preserved |
| Focused commands | [Validation](#validation) | Preserved and correctly bounded as fixture/replay |
| Trust boundary | [Trust boundary](#trust-boundary) | Preserved and expanded |
| Directory Rules | [Directory Rules basis](#directory-rules-basis) | Reconciled with accepted ADR-0029 and migration hold |
| Rollback | [Rollback](#rollback) | Separated by documentation, code seam, record, and future writer |

[Back to top](#top)

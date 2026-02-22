<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/7ab0c044-2eea-48e8-8de3-8a8b3e1f83cf
title: Policy Fixtures
type: standard
version: v1
status: draft
owners: kfm-policy (TBD)
created: 2026-02-22
updated: 2026-02-22
policy_label: restricted
related: []
tags: [kfm, policy, fixtures, opa, conftest]
notes:
  - Policy fixtures are the shared “truth set” for allow/deny + obligations tests.
  - Keep CI + runtime semantics aligned; fail-closed on drift.
[/KFM_META_BLOCK_V2] -->

# Policy Fixtures
Policy decision **test cases** (inputs + expected outputs) used to keep **CI gates** and **runtime enforcement** aligned.

**Status:** draft • **Owners:** `kfm-policy` (TBD) • **Location:** `policy/fixtures/`

![status](https://img.shields.io/badge/status-draft-yellow)
![layer](https://img.shields.io/badge/layer-policy-blue)
![surface](https://img.shields.io/badge/surface-CI%20%2B%20runtime-informational)
![posture](https://img.shields.io/badge/posture-fail--closed-critical)

---

## Navigation
- [What lives here](#what-lives-here)
- [Non-negotiable invariants](#non-negotiable-invariants)
- [Fixture contract](#fixture-contract)
- [Directory layout](#directory-layout)
- [Running policy tests](#running-policy-tests)
- [Adding a new fixture](#adding-a-new-fixture)
- [Review checklist](#review-checklist)
- [FAQ](#faq)

---

## What lives here
This directory holds **fixtures-driven tests** for the policy engine (OPA/Rego *or equivalent*). A “fixture” is:

- an **input** policy query/request (`subject`, `action`, `resource`, `context`)
- an **expected decision** (`allow` / `deny`)
- **expected obligations** (e.g., redact/generalize, require-citation, audit logging, metadata-only fallbacks)

These fixtures are intended to be used by:
- **CI** (block merges when policy would deny or obligations are missing)
- **runtime** (the same semantics must apply when serving data / resolving evidence)

> NOTE: Treat fixtures as governed artifacts. If you put real identifiers, coordinates, or sensitive labels here, you can leak them through tests/logs.

[Back to top](#policy-fixtures)

---

## Non-negotiable invariants
These are the invariants this directory exists to enforce:

1. **One semantics:** CI and runtime MUST behave the same for the same inputs.  
2. **Fail-closed default:** if a fixture is missing/unknown, the safe default is **deny**.  
3. **Obligations are first-class:** “allow” without obligations is usually incomplete in KFM.  
4. **No sensitive leakage:** fixtures must not encode precise locations, secrets, or restricted metadata unless explicitly required and access-controlled.

[Back to top](#policy-fixtures)

---

## Fixture contract
### Canonical shape (PROPOSED)
Until a repo-specific schema exists, use this shape for new fixtures.

~~~json
{
  "kfm_policy_fixture_version": "v1",
  "case_id": "dataset.read.public_user.public_dataset",
  "description": "Public user reads a public dataset distribution.",
  "request": {
    "subject": {
      "principal_id": "user:synthetic_public",
      "roles": ["public"]
    },
    "action": "dataset.read",
    "resource": {
      "resource_type": "dataset_distribution",
      "dataset_id": "kfm:dataset/example",
      "policy_label": "public"
    },
    "context": {
      "client": "ui.map",
      "purpose": "browse",
      "now": "2026-02-22T00:00:00Z"
    }
  },
  "expected": {
    "decision": "allow",
    "obligations": [
      { "type": "require_citation" },
      { "type": "audit_log", "level": "standard" }
    ]
  }
}
~~~

### Decision fields (minimum)
- `expected.decision`: `"allow"` or `"deny"`
- `expected.obligations`: array (can be empty only when explicitly justified)
- `expected.reason_code`: *(optional but recommended)* stable, machine-readable reason string (e.g., `DENY_RESTRICTED_POLICY_LABEL`)

### Obligations (examples)
Obligations are how policy returns “**allowed, but only if…**” constraints.

Common obligation patterns (PROPOSED names; align to your policy bundle):
- `require_citation` — UI/exports must attach citation text
- `audit_log` — write decision receipt / log entry
- `redact_fields` — remove fields from API response / evidence bundle
- `generalize_geometry` — coarsen geometry precision (grid snap, centroid, bounding box)
- `metadata_only` — deny raw artifact access but allow catalog/metadata view
- `deny_no_leak` — ensure error responses do not reveal restricted metadata

[Back to top](#policy-fixtures)

---

## Directory layout
Because repo state may differ, this is a **recommended** (PROPOSED) layout. If your repo already has a structure, update this tree to match reality.

~~~text
policy/
└─ fixtures/
   ├─ README.md
   ├─ cases/
   │  ├─ dataset-access/
   │  ├─ evidence-resolver/
   │  ├─ focus-mode/
   │  ├─ story-render/
   │  └─ promotion/
   ├─ schemas/
   │  └─ policy_fixture.schema.json           (optional; recommended)
   ├─ _index.yml                              (optional; recommended registry)
   └─ _notes/                                 (optional; governance notes)
~~~

### Suggested naming
- **One fixture per file**
- File name mirrors `case_id`, e.g.  
  `dataset.read.public_user.public_dataset.json`

This makes it trivial to:
- grep for a behavior
- promote “policy behavior diffs” through PR review

[Back to top](#policy-fixtures)

---

## Running policy tests
Exact commands depend on the repo’s tooling. The patterns below are typical.

### Option A: OPA-native tests (Rego unit tests)
~~~bash
# Run all rego tests
opa test policy -v
~~~

### Option B: Conftest over fixtures (JSON/YAML inputs)
~~~bash
# Example: evaluate fixtures against policy bundle
conftest test policy/fixtures --policy policy/bundles
~~~

### CI expectation
- CI MUST run fixture tests on every PR that can affect policy behavior.
- CI SHOULD render a human-readable diff:
  - which cases flipped allow↔deny
  - which obligations changed

[Back to top](#policy-fixtures)

---

## Adding a new fixture
### 1) Choose the surface
Pick the policy surface you are testing (examples):
- dataset discovery / read
- tile or feature query
- evidence resolution (EvidenceRef → EvidenceBundle)
- story node render
- Focus Mode answer composition
- dataset promotion gate checks

### 2) Write the fixture
Create a new JSON file with:
- synthetic subject + roles
- action + resource
- minimal context (time, client, purpose)
- expected decision + obligations

### 3) Add at least one deny companion
For every new allow case, add a deny case that proves the boundary:
- same action/resource but stricter label
- missing license/rights
- sensitive location disallowed
- insufficient role

### 4) Run locally, then PR
- run the policy test command
- ensure output is stable (no timestamps in expected output unless intentionally asserted)

[Back to top](#policy-fixtures)

---

## Review checklist
Use this checklist in PR review.

- [ ] Fixture uses **synthetic** identifiers (no real people/emails/secrets).
- [ ] Case has an unambiguous `case_id` and short `description`.
- [ ] Expected output includes **obligations**, not just allow/deny.
- [ ] There is a deny boundary case (or a strong rationale why not).
- [ ] The fixture does **not** embed precise coordinates unless policy explicitly allows it.
- [ ] If the case involves restricted material: confirms **no metadata leak** via error surface.
- [ ] CI output makes it clear what changed (case-by-case).

[Back to top](#policy-fixtures)

---

## FAQ
### Why fixtures instead of only unit tests in Rego?
Fixtures force the policy to be tested at the **contract boundary**:
- what the rest of the system sends in
- what the policy must return out

This catches “integration drift” between CI, runtime, and UI contracts.

### Can fixtures be used in runtime smoke tests?
Yes. The same fixture suite can be replayed against:
- the CI policy engine
- a staging runtime PDP endpoint
to ensure the deployment is running the intended policy bundle.

### Are fixtures public?
Unknown. Treat them as **at least internal** until governance explicitly labels them otherwise.
If you need a public policy surface, create a curated public fixture subset.

[Back to top](#policy-fixtures)

---

## Diagram
~~~mermaid
flowchart LR
  F["Fixture (request + expected)"] --> CI["CI: policy tests (OPA/Conftest)"]
  F --> RT["Runtime: PDP evaluation"]
  CI --> D["Decision (allow/deny + obligations)"]
  RT --> D
  D --> PEP["PEPs: API / Evidence Resolver / Promotion Gate"]
  PEP --> UI["UI renders badges & notices\n(UI does not decide)"]
~~~

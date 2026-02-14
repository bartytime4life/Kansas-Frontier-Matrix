# Focus Mode Test Suite

<!-- Path: tests/focus/README.md -->

[![Focus Tests](https://img.shields.io/badge/tests-focus-blue?style=flat-square)](#running-the-suite)
[![OPA Default Deny](https://img.shields.io/badge/policy-OPA%20default--deny-critical?style=flat-square&logo=openpolicyagent)](#policy-gates)
[![Cite or Abstain](https://img.shields.io/badge/focus%20mode-cite%20or%20abstain-brightgreen?style=flat-square)](#non-negotiable-invariants)
[![Docker Compose](https://img.shields.io/badge/dev-docker%20compose-2496ED?style=flat-square&logo=docker&logoColor=white)](#quickstart)
[![License](https://img.shields.io/github/license/bartytime4life/Kansas-Frontier-Matrix?style=flat-square)](../../LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/bartytime4life/Kansas-Frontier-Matrix?style=flat-square)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/commits)
[![Open Issues](https://img.shields.io/github/issues/bartytime4life/Kansas-Frontier-Matrix?style=flat-square)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues)
[![Open PRs](https://img.shields.io/github/issues-pr/bartytime4life/Kansas-Frontier-Matrix?style=flat-square)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pulls)

> [!IMPORTANT]
> This folder is a **governed test contract**. Changes here can directly change:
> - what KFM will publish (promotion gates),
> - what Focus Mode will answer (cite-or-abstain enforcement),
> - what the UI is allowed to render (sensitivity + provenance controls).
>
> Treat PRs touching `tests/focus/**` like production changes.

## Purpose

Focus Mode is only “credible” if the system can continuously prove the following are true:

- **Evidence-first**: outputs are anchored to traceable sources.
- **Policy-first**: default-deny rules prevent leakage and enforce governance.
- **Fail-closed**: missing metadata / missing policy inputs / unknown sensitivity → deny or abstain.
- **Auditable**: each answer can be traced to an **audit record** and its evidence chain.
- **Trust membrane**: UI never talks to databases or storage directly; all access goes through the governed API + policy boundary.

This README defines the **test surfaces** that enforce those guarantees.

## Non-negotiable invariants

These are the hard requirements that tests in this folder must cover:

- [ ] **Cite or abstain**: every non-trivial answer either includes citations or returns an abstention with `citations=[]`.
- [ ] **Default deny**: policy evaluates to deny unless explicitly allowed.
- [ ] **Fail closed**: missing required policy inputs → deny (never “best effort allow”).
- [ ] **Sensitivity respected**: restricted evidence never appears for unauthorized roles.
- [ ] **Resolvable citations**: each `citation.ref` resolves to a human-readable evidence view in **≤ 2 API calls**.
- [ ] **Auditability**: every Focus answer includes `audit_ref`, and the audit record links back to `evidence_refs`.
- [ ] **Trust membrane**: frontend uses only the governed API; no direct DB calls, no raw storage URLs in the client.

## What this suite covers

| Surface | What we validate | Signals | Why it matters |
|---|---|---|---|
| Policy gate (OPA/Rego) | Default-deny, cite-or-abstain, sensitivity rules | `opa test` passes; deny cases behave correctly | Prevents unsafe publication + unsafe answers |
| Focus API contract | `/api/v1/ai/query` returns governed output shape | Has `answer_markdown`, `citations[]`, `audit_ref` | Keeps clients stable + testable |
| Evidence resolution | `citation.ref` resolves quickly and deterministically | 1–2 API calls to view evidence | Ensures citations are actionable, not decorative |
| Audit ledger | `/api/v1/audit/{audit_ref}` returns an AuditRecord | `evidence_refs` present + hash chain fields populated | Enables accountability and post-hoc review |
| UI boundary | UI never bypasses the policy/API boundary | static checks + E2E network assertions | Protects the trust membrane |

## Quickstart

### Prerequisites

- Docker + Docker Compose (v2)
- `curl`
- Optional but recommended:
  - `opa` CLI (or use the Docker-based runner below)
  - `jq` for nicer output viewing

### Start the dev stack

Run from repo root:

```bash
cp .env.example .env
docker compose up --build -d
```

Expected local endpoints (dev default):
- API docs: `http://localhost:8000/docs`
- Web UI: `http://localhost:3000`

## Running the suite

> [!NOTE]
> Commands below assume you run them from the **repo root**. If you run from `tests/focus/`, prepend paths with `../../`.

### 1) Policy gates

Run OPA unit tests (recommended baseline gate):

```bash
opa test policy -v
```

No local `opa` installed? Use Docker:

```bash
docker run --rm -v "$PWD":/work -w /work openpolicyagent/opa:latest test -v policy
```

What “passing” means:
- Allow cases must require `has_citations == true` and `sensitivity_ok == true`.
- Deny cases must deny missing citations or failing sensitivity.

### 2) Focus Mode contract smoke test

This verifies the endpoint responds with the governed shape (citations + audit ref).

```bash
curl -sS \
  -H "Content-Type: application/json" \
  -X POST "http://localhost:8000/api/v1/ai/query" \
  -d '{
    "question": "What is visible in the selected region over time?",
    "context": {
      "time_range": ["1850-01-01T00:00:00Z","1900-12-31T23:59:59Z"],
      "bbox": [-100, 37, -96, 39],
      "active_layers": ["layer_example_dataset"],
      "story_node_id": "story_example"
    }
  }'
```

Minimum checks you must be able to perform on the JSON:
- `audit_ref` exists and is a non-empty string
- `citations` exists and is an array (may be empty only when abstaining)
- `answer_markdown` exists (or an explicit abstention message)

If you have `jq`, you can quickly check:

```bash
curl -sS -H "Content-Type: application/json" -X POST "http://localhost:8000/api/v1/ai/query" \
  -d '{"question":"Give one sourced fact.","context":{"time_range":["1850-01-01T00:00:00Z","1900-12-31T23:59:59Z"],"bbox":[-100,37,-96,39],"active_layers":["layer_example_dataset"]}}' \
  | jq '{hasAuditRef:(.audit_ref|type=="string" and length>0), citationCount:(.citations|length), hasAnswer:(.answer_markdown|type=="string" and length>0)}'
```

### 3) Evidence resolution check

Once you have an answer, pick a citation ref and confirm it resolves fast.

#### Rule
For any `citation.ref` in a Focus answer, the UI must be able to resolve it in **≤ 2 API calls**.

#### Practical test
1. Call the Focus endpoint.
2. Extract the first `citation.ref`.
3. Resolve via evidence endpoint(s) required by the contract.

Example (shape depends on your implementation; the invariant is the **≤ 2 calls** rule):

```bash
# 1) Get answer
ANSWER_JSON="$(curl -sS -H "Content-Type: application/json" -X POST "http://localhost:8000/api/v1/ai/query" \
  -d '{"question":"Return one short, sourced statement.","context":{"time_range":["1850-01-01T00:00:00Z","1900-12-31T23:59:59Z"],"bbox":[-100,37,-96,39],"active_layers":["layer_example_dataset"]}}')"

# 2) Print citation refs (requires jq)
echo "$ANSWER_JSON" | jq -r '.citations[].ref'
```

Then resolve one ref with your evidence resolver endpoint(s). Typical patterns:
- `GET /api/v1/evidence/{ref}`
- or `GET /api/v1/sources/{id}` + `GET /api/v1/evidence/{ref}` (still capped at 2 total calls)

### 4) Audit ledger check

Every answer must be traceable:

```bash
# Extract audit_ref (requires jq)
AUDIT_REF="$(echo "$ANSWER_JSON" | jq -r '.audit_ref')"

# Fetch the audit record
curl -sS "http://localhost:8000/api/v1/audit/${AUDIT_REF}"
```

Minimum checks:
- response is a valid AuditRecord object
- includes `audit_ref`, `timestamp`, `event_type`, `subject`, `event_hash`
- includes `evidence_refs` referencing the same evidence used by citations

## Test model

### Policy gates

Policy is the primary safety rail.

- **Default deny** is required.
- **Cite-or-abstain** is enforced at output time (pre-return).
- **Sensitivity gates** prevent restricted evidence from being cited or displayed.

Expected policy input shape (conceptual):

- `actor`: role + attributes
- `request`: endpoint + context
- `answer`: text + citations + sensitivity flags

### Contract tests

Contract-first means the API surface should be stable and testable:

- `/api/v1/ai/query` returns a FocusAnswer
- `/api/v1/audit/{audit_ref}` returns an AuditRecord

All contract tests must be deterministic:
- never rely on “whatever the model returns today”
- use fixtures and gold sets where possible

### Gold-set regression

Focus Mode should be evaluable with regression suites:

- Maintain a small “gold” pack of Focus queries + expected behaviors:
  - **must abstain** when evidence is missing
  - **must cite** when evidence is available
  - **must deny** when policy forbids access

## Adding a new Focus Mode test

1. Pick the invariant you’re enforcing (from the checklist above).
2. Add/extend:
   - a policy unit test (OPA) if the rule is policy-based
   - a contract test if the API schema or resolvability is involved
   - a gold-set case if this is a behavioral regression
3. Ensure:
   - fixtures contain no sensitive real-world coordinates
   - evidence identifiers are stable and resolvable
4. Run locally:
   - `opa test policy -v`
   - smoke test the endpoint + audit + evidence resolver

## CI expectations

At minimum, CI must run:

- governed Markdown + Story Node validation
- catalog validation (STAC/DCAT/PROV) for data changes
- **policy tests**: `opa test policy -v`
- build checks after policy/docs/data gates pass

This suite should be treated as a required PR gate.

## Troubleshooting

### Containers are up but the API is not responding

- Check logs:
  ```bash
  docker compose logs -f api
  ```
- Confirm the API doc endpoint:
  - `http://localhost:8000/docs`

### Port conflicts

If you already have local services running, common collisions include:
- Postgres (5432)
- Neo4j (7474)
- API (8000)
- Web (3000)

Fix by stopping the conflicting service or adjusting compose port mappings.

### Policy denies everything

That’s usually correct at first.

Validate you are passing required policy inputs:
- actor role
- endpoint
- answer flags
- citations list

If policy “allows” without citations, that’s a bug: add a failing OPA test and fix the policy.

## Directory layout

> [!TIP]
> Keep this folder “thin and sharp”: it should test Focus guarantees, not become a dumping ground for unrelated tests.

```text
tests/
└── focus/
    ├── README.md
    ├── gold/
    │   ├── cases/                 # Gold-set: query + expected behavior (cite / abstain / deny)
    │   └── README.md              # How the gold runner works (deterministic, versioned)
    ├── policy/
    │   ├── inputs/                # Policy input fixtures (actor/request/answer)
    │   └── expectations/          # Expected allow/deny outcomes
    ├── contract/
    │   ├── openapi/               # Focus + audit contract assertions (schemas, examples)
    │   └── examples/              # Minimal request/response examples for docs + tests
    ├── integration/
    │   ├── api/                   # Focus endpoint + audit + evidence resolution integration tests
    │   └── ui/                    # UI trust-membrane checks (no direct DB calls)
    └── scripts/
        ├── run_policy.sh          # Runs OPA/conftest consistently (local + CI)
        └── run_smoke.sh           # One-command smoke: focus -> audit -> evidence
```

### Path registry

| Path | Contents | Governance note |
|---|---|---|
| `tests/focus/policy/` | Fixtures + expected decisions | Must stay default-deny |
| `tests/focus/contract/` | Schema/shape expectations | Contract-first; treat changes as breaking |
| `tests/focus/gold/` | Regression suite | Must be deterministic + versioned |
| `tests/focus/integration/` | End-to-end wiring checks | Enforce trust membrane |
| `tests/focus/scripts/` | One-command runners | Keep CI and local identical |

## Security and privacy

- Do **not** commit secrets. Use `.env`.
- Do **not** commit precise sensitive locations or restricted evidence.
- Prefer synthetic fixtures.
- Any test that touches sensitive handling must include:
  - deny/allow cases
  - an audit record expectation
  - a redaction/generalization expectation where applicable

---
✅ If you’re reviewing a PR that changes Focus Mode behavior, you should be able to point to:
- the invariant it affects,
- the test(s) that enforce it,
- the policy rule(s) that gate it,
- and the audit/evidence traces that make it reviewable.

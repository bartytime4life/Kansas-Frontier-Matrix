# policy/

This directory is the **source of truth for Kansas Frontier Matrix (KFM) governance rules** (“policy as code”).  
Policies exist to **protect communities, users, and data** while keeping KFM’s behavior **auditable, consistent, and enforceable** across:

- **CI** (prevent non-compliant changes from merging)
- **Runtime** (prevent non-compliant requests/outputs from being served)

> **Design intent:** governance is “baked in,” transparent, and versioned like code.

---

## What belongs here

This folder should contain:

- **OPA/Rego policy modules** (policy-as-code)
- **Policy test cases** (OPA unit tests and/or Conftest fixtures)
- **Policy data** used by rules (e.g., allow/deny lists, regex patterns, sensitivity tags), as appropriate

This folder should **not** contain:
- Secrets (tokens, passwords, API keys)
- Raw restricted data (unless this repo explicitly stores restricted data under controlled processes)
- One-off, undocumented “local hacks” that bypass governance

---

## Non-negotiable principles

These principles guide every rule in this folder:

1. **Fail safe / fail closed**
   - If a policy decision cannot be made confidently (OPA unavailable, malformed input, ambiguous state), **deny**.
2. **Least privilege**
   - Default capability is **none**; grant access only with explicit, reviewable rules.
3. **No output may be less restricted than its inputs**
   - Derived outputs (AI answers, exports, reports) must not relax the sensitivity of the underlying sources.
4. **No source, no answer**
   - For AI responses: if the system can’t cite approved sources, it must refuse rather than guess.
5. **FAIR + CARE compliance**
   - FAIR: Findable, Accessible, Interoperable, Reusable.
   - CARE (Indigenous data governance): Collective Benefit, Authority to Control, Responsibility, Ethics.
6. **Privacy & safety by default**
   - Never disclose personal details about living individuals.
   - Never disclose **exact coordinates** of sensitive locations (e.g., archaeological sites, sacred sites, endangered species habitats); generalize/mask as needed.

---

## Where policy is enforced in KFM

KFM governance is implemented as **multiple gates**—some are policy-as-code, some are code validations—with critical checks occurring at key lifecycle points:

### 1) Data ingestion & catalog publication gates
Policy checks must block publication when required metadata is missing, especially:
- license / reuse terms
- provenance records

### 2) Role-based access control gates (RBAC)
Requests for datasets, documents, and tools must be checked against:
- **user role** and associated permissions
- **dataset sensitivity** and any special flags (e.g., Indigenous heritage controls)

### 3) AI input gate (“Prompt Gate”)
Before any user question reaches the model, inputs must be sanitized to remove:
- prompt injection attempts
- disallowed content requests (private personal data, hate/profanity, etc.)

### 4) AI sandbox / tool allow-list
The AI agent must run with **no unapproved tools** by default.  
If tools are enabled, they must be explicitly allow-listed and reviewed.

### 5) AI output gate (OPA output filtering)
Before an AI answer is returned, it must pass policy checks for:
- citation presence and validity format
- disallowed content (privacy leaks, sensitive sites, restricted data)
- role/sensitivity compatibility (answer content must not reveal restricted info to unauthorized roles)

---

## Recommended policy domains

Below is a recommended (not mandatory) way to think about policies. Adjust naming to match the repository.

| Domain | What it governs | Typical examples |
|---|---|---|
| **data/** | dataset metadata, provenance, licensing, sensitivity classification | block publish without license/prov; enforce sensitivity tags |
| **access/** | RBAC + attribute-based constraints | deny restricted datasets to public users; enforce “Indigenous data” flag restrictions |
| **ai/** | AI behavior + output requirements | require citations; block PII; block sensitive location precision |
| **security/** | platform security invariants | deny privileged operations except for maintainers/admins |
| **compliance/** | higher-level governance checks | policy gates for prohibited uses; takedown/withdrawal enforcement |

---

## Directory layout

If you need a structure, start with something like:

```text
policy/
  README.md

  ai/
    *.rego
    *_test.rego

  data/
    *.rego
    *_test.rego

  access/
    *.rego
    *_test.rego

  security/
    *.rego
    *_test.rego

  compliance/
    *.rego
    *_test.rego

  tests/                 # Optional: Conftest fixtures or sample inputs
    inputs/
    expected/
```

If the repo already uses a different structure, **mirror that** and update this README accordingly.

---

## OPA/Rego conventions for KFM

### Default-deny pattern

KFM policies should default to deny, then explicitly allow:

- `default allow = false`
- `allow { ... }`

Prefer returning structured reasons when denying (when the caller supports it), e.g.:
- `deny[msg] { ... }`

### Keep policy inputs explicit

Every policy package must document the expected `input` shape it evaluates, e.g.:

```rego
# input example (illustrative)
# {
#   "user": {"role": "public" },
#   "resource": {"type": "dataset", "id": "…", "sensitivity": "restricted"},
#   "action": "read"
# }
```

---

## Example policy: enforce “No source, no answer” for AI

A minimal citation-enforcement rule (example) to require at least one numeric footnote like `[1]`:

```rego
package kfm.ai

default allow_answer = false

# Allow answer only if it contains at least one citation like "[number]"
allow_answer {
  re_match("\\[\\d+\\]", input.answer)
}
```

Notes:
- This checks for **presence**, not correctness of mapping.
- In practice, production policy should also validate that citations map to known catalog entities.

---

## CI enforcement (Conftest) and local testing

### CI expectations

Policy checks should run as a CI gate, alongside tests/linters, to prevent merging changes that violate governance (e.g., missing provenance, missing license metadata, disallowed phrases in prompts/templates).

### Local testing (recommended)

Install:
- `opa` (Open Policy Agent)
- `conftest` (for policy testing against repository files)

Then run one (or both) of:

```bash
# OPA unit tests
opa test ./policy -v
```

```bash
# Conftest evaluation (example pattern — adjust targets to match repo)
conftest test -p ./policy ./data ./docs ./api
```

If your policies require a specific input schema, include minimal fixtures under `policy/tests/` and document how to run them.

---

## Change management and reviews

### Who reviews policy changes

- **Maintainers/Admins** must review all policy changes.
- Changes that affect **Indigenous heritage controls**, sensitivity classification, release rules, or takedown/withdrawal behavior should also be reviewed through the project’s **FAIR+CARE governance process**.

### What every policy PR must include

- Clear statement of intent (“what risk are we reducing?”)
- The policy change (`*.rego`)
- Tests that demonstrate:
  - compliant cases pass
  - non-compliant cases fail
- Documentation updates if behavior changes (this README or relevant docs)

---

## Sensitive data guidance (must be reflected in policy)

Policies must prevent (at minimum):

- **Exact coordinates** for sensitive locations (archaeological sites, sacred sites, endangered species habitats)
- **Personal details** about living individuals (PII / private data)
- **Unauthorized access** to internal/restricted datasets (including those tagged “Indigenous data” requiring authorization)

When a request/response contains both public and restricted material, policy should:
- deny, or
- require masking/sanitization if the API supports partial disclosure

---

## Troubleshooting

### “CI failed due to policy”
Common causes:
- dataset added/changed without required metadata (license/provenance)
- restricted/sensitive content added without required flags/authorization markers
- AI prompt/template violates content rules

Steps:
1. Read the Conftest/OPA output and identify which rule fired.
2. Fix data/metadata OR adjust policy (only if the rule is incorrect).
3. Add/adjust tests to prevent regression.

### “Runtime denied my request / answer was blocked”
Common causes:
- user role not authorized
- answer contained restricted info or lacked citations
- OPA engine unreachable / uncertain decision (fail-closed behavior)

Steps:
1. Capture the decision context (role, action, resource, answer text).
2. Reproduce locally with an equivalent input fixture.
3. Update policy/tests or adjust request behavior (masking, aggregation, citation coverage).

---

## References inside this repository

- `docs/standards/faircare.md` (FAIR + CARE governance standard)
- KFM system documentation / developer guide (security, policy gates, OPA integration)


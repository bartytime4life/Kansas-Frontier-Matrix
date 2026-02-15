# Leak Case Golden Tests

**Status:** ✅ Governed • **Suite:** 🧪 Golden non‑regression • **Risk class:** 🔒 Data leakage prevention

This folder contains **golden leak cases**: minimal, repeatable scenarios that *previously* caused KFM to expose **restricted fields** (e.g., ownership/PII) or **overly‑precise sensitive locations** (e.g., archaeology / protected species), and must **never** be allowed again.

Leak cases are intentionally **small**, **stable**, and **fail‑closed**: if something is ambiguous, the expected behavior is deny or sanitize.

---

## What counts as a “leak”

A “leak” is any of the following outcomes for an **unauthorized** actor:

- A **restricted field** is returned (e.g., owner names, direct identifiers, private attributes).
- A **sensitive-location geometry** is returned at **high precision** (or in any form that can be reverse‑engineered to high precision).
- An **aggregate-only** dataset returns values below disclosure thresholds (e.g., small-count health/crime).
- A response omits required **audit** and **evidence** references, reducing traceability and accountability.

---

## Non‑negotiable invariants (acceptance criteria)

The leak-case suite exists to enforce these invariants:

- **Golden queries that previously leaked restricted fields must fail tests forever (non‑regression).**
- **Negative tests:** sensitive-location layers cannot be returned at **high precision** to unauthorized roles.
- **Field‑level tests:** owner names, health small counts, and exact archaeological coordinates are **redacted**.
- **Audit integrity:** every API response includes an **audit reference** and an **evidence bundle hash/digest**.

If a PR causes any leak case to pass incorrectly (or stop running), treat it as a **security/data governance regression**.

---

## Directory layout

```text
policy/tests/golden/leak_cases/
├── README.md
├── LC-0001-<slug>.yaml
├── LC-0002-<slug>.yaml
└── … (one file per leak scenario)
```

> Tip: Keep **one** scenario per file. If you need variants (different roles/scopes), model them as separate cases to preserve clarity and blame.

---

## Case naming conventions

Use:

- **Prefix:** `LC-` (Leak Case)
- **ID:** 4 digits, zero-padded (`0001`, `0002`, …)
- **Slug:** short kebab-case descriptor

**Pattern:** `LC-<id>-<slug>.yaml`

Examples:

- `LC-0007-parcel-owner-name-redaction.yaml`
- `LC-0012-archaeology-precise-geometry-deny.yaml`

---

## Case file requirements (what each case must capture)

Leak cases are “golden” only if they are **self-explanatory** and **actionable**.

### Required fields (recommended contract)

| Field | Type | Required | Meaning |
|---|---:|:---:|---|
| `id` | string | ✅ | Unique case identifier (matches filename). |
| `title` | string | ✅ | One-line description of the leak being prevented. |
| `risk` | string | ✅ | `restricted-field` \| `sensitive-location` \| `aggregate-only` \| `audit-integrity` \| `other`. |
| `origin` | object | ✅ | Where this leak came from (incident/issue/PR), plus dates. |
| `input` | object | ✅ | Actor + request context used by the policy/API harness. |
| `expected` | object | ✅ | The expected enforcement outcome (deny/redact/generalize) + audit/evidence requirements. |
| `notes` | string | optional | Extra context (why this mattered, gotchas). |

> ⚠️ If your current harness uses a different schema, keep the file **semantically equivalent** and update the harness later—do **not** water down the case.

---

## Example leak case (template)

```yaml
id: LC-0000-example-template
title: "Public role must never receive restricted fields (example template)"
risk: restricted-field

origin:
  discovered_date: "YYYY-MM-DD"
  reference:
    kind: "incident|issue|pr"
    id: "TBD"
  summary: "Describe the original leak in one sentence."

input:
  actor:
    role: "public"          # e.g., public | reviewer | admin | custodian
    scopes: []              # keep empty unless your auth model requires scopes
    grants: []              # use for custodian grants if applicable
  request:
    kind: "api|graphql|focus_mode"
    route: "<ROUTE_OR_OPERATION_NAME>"
    params: {}              # query params if applicable
    body: {}                # request body if applicable
  resource:
    kind: "dataset|layer|record"
    id: "<DATASET_OR_LAYER_ID>"
    sensitivity: "restricted"

expected:
  decision: "deny|allow_with_redaction|allow_with_generalization"
  must_not_expose:
    fields:
      - "owner_name"
      - "owner_address"
    geometry:
      - "precise_coordinates"
  geometry_precision:
    # Use one of: "suppressed", "generalized", "precise"
    required: "generalized"
    # Optional: if your harness supports numeric precision caps
    max_decimal_places: 3
  audit:
    require_audit_ref: true
    require_evidence_bundle_hash: true
```

---

## How leak cases are evaluated (conceptual)

Leak cases may be exercised by one or both of these mechanisms:

1. **Policy evaluation** (OPA/Rego): validate allow/deny and required redaction/generalization decisions.
2. **API contract evaluation**: validate response shape never includes restricted fields or overly-precise geometry.

```mermaid
flowchart LR
  Case[Leak case file\nLC-####-slug.yaml] --> Harness[Policy/API test harness]
  Harness --> Policy[OPA/Rego decision\n(default-deny)]
  Policy -->|deny| Deny[Deny / fail-closed]
  Policy -->|allow w/ controls| Controls[Redact / generalize]
  Controls --> Response[Response]
  Response --> Checks[Assertions:\n- no restricted fields\n- no high-precision sensitive locations\n- audit_ref present\n- evidence digest present]
```

---

## Adding a new leak case

1. **Reproduce** the leak in a safe/dev environment (never using production secrets).
2. **Minimize** the scenario:
   - smallest request that triggers the issue
   - smallest fixture data needed to prove it
3. **Write** a new `LC-####-<slug>.yaml`:
   - describe the leak and its origin
   - define actor role/scopes
   - specify expected deny/redact/generalize outcome
4. **Ensure the case is safe to commit**:
   - replace any real owner names, addresses, or sensitive coordinates with synthetic values
5. **Run the policy test harness locally** (use whatever entrypoint CI uses).
6. **Confirm**:
   - case fails before the fix (or demonstrates the vulnerability)
   - case passes only after the fix
7. **Open PR** with:
   - the new case file
   - the policy/app change that closes the leak
   - a short explanation of why the fix is correct and non-bypassable

---

## Definition of Done ✅ (for PRs touching leak cases)

- [ ] New/updated leak case has a unique `LC-####` ID and clear title.
- [ ] Case uses **synthetic** values (no real PII; no real sensitive coordinates).
- [ ] Expected outcome is **deny or sanitize** (not “best effort”).
- [ ] Case asserts **audit reference** + **evidence digest** presence.
- [ ] Local run of the policy test harness passes.
- [ ] CI passes, and the leak case is included in the executed suite (not skipped).
- [ ] If behavior changed intentionally, the PR includes a governance note explaining why.

---

## Governance & safety rules (do not skip)

> **🚫 Never commit real sensitive data**  
> Leak cases must not contain real parcel ownership/PII, real addresses, or precise archaeological site locations. Use synthetic fixtures that preserve *shape* (field names/types) without real-world risk.

> **🔐 “UI never fetches precise geometry w/o grant”**  
> Include or maintain at least one leak case asserting that **precise geometry is inaccessible** without an explicit grant/role. This prevents accidental reintroduction of precision leaks through UI/API changes.

---

## Troubleshooting

### “A leak case failed after my change”
- Check whether your change altered:
  - the policy input schema
  - role/scope mapping
  - redaction/generalization behavior
- If you intended to change behavior:
  - update the case to reflect the new *governed* expectation **and**
  - document the governance rationale in the PR (do not silently weaken cases)

### “Leak cases aren’t running in CI”
- Find the workflow step that runs policy tests and ensure it includes this directory.
- Leak cases are **merge-blocking** by design; if they are skipped, treat as a governance incident.

---

## Ownership

Changes in this folder should be reviewed by **policy maintainers** and **data governance reviewers**. These cases represent institutional memory; deleting or weakening them requires explicit rationale and auditability.


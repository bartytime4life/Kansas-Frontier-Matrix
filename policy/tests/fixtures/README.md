<!--
File: policy/tests/fixtures/README.md
KFM governed artifact: Policy test fixtures documentation.
-->

# Policy Test Fixtures

Deterministic **synthetic** inputs used by KFM’s OPA/Rego policy tests.

This directory exists to make policy behavior:

- **Reviewable** (humans can read the scenarios)
- **Reproducible** (CI runs are deterministic)
- **Regression-proof** (a previously-fixed leak must never reappear)
- **Fail-closed by default** (missing/invalid inputs should not accidentally allow access)

---

## What belongs here

Fixtures in this folder should represent **contract-level payloads** at the policy boundary (the “trust membrane”): requests, resources, and responses that the policy engine evaluates — not raw database rows.

Typical fixture categories:

- **Golden regression cases**  
  Inputs that historically exposed restricted fields or precise locations, kept forever as “must-deny” cases.

- **Negative access tests**  
  Inputs that attempt to retrieve restricted or sensitive-location data with insufficient privileges.

- **Field-level redaction tests**  
  Inputs/outputs that prove restricted fields (e.g., owner names, small counts, exact coordinates) are redacted or generalized.

- **Audit integrity cases**  
  Inputs/outputs that prove responses carry an `audit_ref` and a tamper-evident evidence/bundle reference (hash/digest).

- **Schema/shape tests (fail-closed)**  
  Inputs missing required keys (or containing malformed keys) that must **deny**.

---

## Sensitivity and synthetic-data rules

> [!IMPORTANT]
> **Never** commit real PII, real parcel owner names, real precise archaeological coordinates, or any embargoed/sensitive locations.  
> Fixtures must be **synthetic**, **minimal**, and **safe to publish**.

Use the platform’s sensitivity vocabulary consistently. When representing sensitivity in fixtures, prefer one of:

| Label | Meaning | Fixture expectations |
|---|---|---|
| `public` | Safe to publish without redaction | Public role may access unless another rule denies |
| `restricted` | Requires role-based access | Public role must be denied |
| `sensitive-location` | Coordinates must be generalized or suppressed | Public role must be denied for **precise** geometry |
| `aggregate-only` | Only publish above thresholds | Fixtures should test small-count suppression |

> [!NOTE]
> If you need a geometry to test “precision,” use **obviously synthetic** coordinates and/or synthetic geometries that are *not* real site locations. The goal is to test policy behavior, not to represent reality.

---

## Recommended fixture layout

You may organize fixtures by policy domain (recommended), by risk class, or by endpoint. Keep names stable and descriptive.

Example (illustrative) layout:

```text
policy/tests/fixtures/
  ai/
    allow_with_citations/
      input.json
    deny_without_citations/
      input.json

  data_access/
    allow_public_dataset_for_public_role/
      input.json
    deny_restricted_dataset_for_public_role/
      input.json

  redaction/
    deny_precise_sensitive_location_for_public_role/
      input.json

  audit/
    require_audit_ref_and_evidence_ref_on_response/
      input.json
```

### Naming rules

- Use **snake_case** for folder names.
- Prefer **positive intent** names: `deny_*` / `allow_*` / `require_*`.
- Keep fixtures **small** and **deterministic** (no random IDs; fixed timestamps).

---

## Minimal fixture “shapes” (examples)

These examples are *minimal shapes* you can copy to create new fixtures. They are intentionally small and synthetic.

<details>
<summary><strong>Focus Mode output policy (example input shape)</strong></summary>

```json
{
  "actor": { "role": "public" },
  "request": { "endpoint": "/api/v1/ai/query" },
  "answer": {
    "text": "Synthetic answer text.",
    "has_citations": true,
    "sensitivity_ok": true,
    "citations": [{ "id": "c1" }]
  }
}
```

</details>

<details>
<summary><strong>Dataset access policy (example input shape)</strong></summary>

```json
{
  "actor": { "role": "public" },
  "resource": {
    "kind": "dataset",
    "sensitivity": "public",
    "dataset_id": "example_dataset"
  }
}
```

</details>

<details>
<summary><strong>Audit record (example minimal shape)</strong></summary>

```json
{
  "audit_ref": "audit:example/00000001",
  "timestamp": "2026-02-13T00:00:00Z",
  "event_type": "policy.decision",
  "subject": { "kind": "request", "id": "req:example/0001" },
  "event_hash": "sha256:0000000000000000000000000000000000000000000000000000000000000000",
  "evidence_refs": ["bundle:sha256:1111111111111111111111111111111111111111111111111111111111111111"]
}
```

</details>

---

## Adding a new fixture

1. Create a new scenario folder under the closest domain (e.g., `ai/`, `data_access/`, `redaction/`, `audit/`).
2. Add `input.json` containing only the fields required to exercise the rule under test.
3. Ensure the scenario is asserted by the test harness (OPA unit tests and/or Conftest tests).
4. If the scenario is a **golden non-regression leak**, add a short explanation in a `notes.md` file.

### PR checklist (fixtures)

- [ ] Fixture is **synthetic** and contains **no sensitive real-world details**
- [ ] Fixture is **minimal** (only required fields)
- [ ] Fixture uses a recognized **sensitivity** label (when applicable)
- [ ] Fixture uses **fixed** values for timestamps/IDs (deterministic CI)
- [ ] A corresponding test exists and clearly asserts allow/deny (or redaction/audit requirement)
- [ ] If this is a past leak, it is marked as **golden non-regression**

---

## Common pitfalls to avoid

- **Accidentally realistic coordinates**: do not use coordinates copied from real sources.
- **Fixture bloat**: large fixtures slow CI and hide intent.
- **Nondeterminism**: random IDs, “now” timestamps, or unstable ordering.
- **Drift between tools**: ensure policies/tests run consistently under the pinned OPA/Conftest/Rego configuration used in CI.

---

## Ownership

If you are unsure whether a fixture is safe to commit (especially around restricted or sensitive-location data), treat it as **governance-reviewed** and escalate to the policy maintainers before merging.


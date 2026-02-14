# `tests/fixtures/` — Test Fixtures (Governed)

<!--
KFM fixtures are part of the governed delivery surface:
- They protect the trust membrane, policy gates, and "cite-or-abstain" behaviors.
- They must stay small, deterministic, and safe to distribute in-repo.
-->

![fixtures](https://img.shields.io/badge/tests-fixtures-informational)
![ci](https://img.shields.io/badge/CI-deterministic-success)
![governance](https://img.shields.io/badge/governance-fail--closed-critical)

> **Purpose:** This folder contains **small, synthetic, deterministic** fixtures used across KFM unit, integration, and contract tests.
> Fixtures here exist to make governance *testable* (non-regression) and CI *fast*.

---

## Why this exists

KFM’s platform contracts require **fail-closed behavior** (deny-by-default) and **non-regression** for sensitive data handling and audit integrity. Test fixtures are the stable inputs and “golden outputs” that let us prove those invariants continuously.

> [!IMPORTANT]
> Fixtures are **governed artifacts**.
> Treat changes like API changes: they can break tests *and* weaken safety guarantees if reviewed poorly.

---

## ✅ What belongs here (and what does not)

| ✅ Yes (commit-safe) | 🚫 No (do not commit) |
|---|---|
| **Synthetic** records created solely for tests | Production extracts / “real” dumps |
| **Redacted** examples that cannot re-identify people/places | Any unredacted PII, private ownership, or sensitive coordinates |
| “Golden” expected outputs for schema/policy/audit checks | Secrets (API keys, tokens), credentials, private endpoints |
| Minimal STAC/DCAT/PROV samples (tiny) | Large binaries / multi-GB rasters unless explicitly approved |
| Minimal API request/response snapshots | Anything that violates upstream redistribution terms |

> [!WARNING]
> If a fixture even *might* contain sensitive location detail (e.g., archaeology or protected species), **generalize** or **suppress** coordinates in the fixture.
> If you must represent a “precise vs generalized” split for a policy test, represent the *precise* version with **synthetic coordinates** that do not correspond to real sites.

---

## Directory layout

> Keep the layout boring and predictable. Prefer adding a new folder only when there is a stable category need.

```text
tests/
  fixtures/
    README.md                         # you are here

    receipts/                         # run receipts / ingestion receipts (synthetic)
      kfm.run_receipt.v1.example.json

    catalog/                          # “golden” catalog artifacts and expected outputs
      stac/
      dcat/
      prov/

    policy/                           # policy test vectors (allow/deny) + expected decisions
      inputs/
      expected/

    api/                              # request/response snapshots for governed endpoints
      requests/
      responses/

    data/                             # tiny datasets used by connector/transform tests
      tabular/
      geojson/
      parquet/                        # only if tiny and justified

    docs/                             # fixtures for Story Nodes / Focus Mode formatting tests
      story_node_v3/
      focus_mode/
```

---

## Fixture design rules (KFM defaults)

### 1) Keep fixtures small and deterministic
- Favor **tiny** inputs (think: tens of rows, not millions).
- Prefer **synthetic** values.
- Ensure stable sort order where applicable (IDs, timestamps, features).

### 2) Make governance testable
Fixtures should enable:
- **Schema validation** tests (required fields present, formats correct).
- **Policy gate** tests (“No Source, No Answer” / deny missing license or missing required metadata).
- **Audit integrity** tests (responses carry required audit/evidence references).
- **Non-regression** tests: if a bug ever leaked a field, a fixture should exist that would re-trigger the leak if reintroduced.

### 3) Treat redaction as a transformation (even in tests)
If a fixture represents a redacted derivative, keep:
- a separate *synthetic “raw-like”* version (if needed),
- a *redacted* version,
- and a note in sidecar metadata describing the redaction intent.

> [!NOTE]
> The goal is not “realism.” The goal is “provable behavior.”

---

## Recommended sidecar metadata (optional but strongly encouraged)

For any fixture that is used in **policy** or **audit** tests, add a sidecar file:

- `my.fixture.json`  
- `my.fixture.meta.yml`

Suggested fields:

```yaml
fixture_id: kfm.fixtures.receipts.run_receipt.example.v1
kind: receipt | policy_input | policy_expected | stac | dcat | prov | api_request | api_response | dataset
schema_id: kfm.run_receipt.v1
classification: public | restricted | sensitive-location | aggregate-only
purpose: "Policy regression test: deny-by-default without license"
used_by:
  - tests/policy/test_license_gate.py
  - tests/api/test_audit_headers.py
notes: "Synthetic values only. No real locations."
```

---

## Example fixture: `kfm.run_receipt.v1` (synthetic)

This is a minimal example of a receipt-shaped fixture intended for deterministic CI.

```json
{
  "example": "kfm.run_receipt.v1",
  "fetched_at": "2026-02-13T00:00:00Z",
  "accessURL": "https://example.org/source",
  "etag": "W/\"abc123\"",
  "last_modified": "Wed, 12 Feb 2026 00:00:00 GMT",
  "spec_hash": "sha256:<spec>",
  "artifact_digest": "sha256:<artifact>",
  "tool_versions": { "pipeline": "1.0.0" },
  "policy_gate": {
    "status": "pass",
    "checks": ["license_present", "stac_present"]
  }
}
```

---

## Golden tests: what we expect to lock down forever

> [!IMPORTANT]
> **Golden tests** are supposed to be annoying when they fail. That’s the point.

Use fixtures to maintain:
- **Golden catalog outputs** (DCAT/STAC/PROV) for known inputs.
- **Golden policy decisions** for key role/scope combinations.
- **Golden “leak prevention” queries**: if something leaked once, it must never leak again.

---

## Adding or updating a fixture

### Checklist
- [ ] Fixture is **synthetic** (or safely redacted).
- [ ] Fixture contains **no secrets** and no prohibited redistributable data.
- [ ] File is **small** and stable (ordering fixed, timestamps pinned where needed).
- [ ] If it is a policy fixture: it has a **clear expected allow/deny** outcome.
- [ ] If it is an API snapshot: it includes/validates **audit + evidence references** (as required by the contract).
- [ ] Update/refresh “golden” expected outputs intentionally (review diff carefully).

### Review posture
- Treat fixture changes like code changes.
- Large diffs should be split: “mechanical regen” vs “semantic change.”

---

## Footnotes / local provenance

- Primary governance expectations for sensitivity handling, redaction, and CI policy regression are described in internal KFM design artifacts (see project docs for the latest).
- This README intentionally stays language-agnostic (fixtures can be consumed by Go/Python/Node tests as needed).


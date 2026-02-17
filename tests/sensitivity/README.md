# Sensitivity Test Suite (KFM) 🔒🧭

![Governed](https://img.shields.io/badge/Governed-Evidence--first%20%E2%80%A2%20FAIR%2BCARE-2ea44f)
![Policy](https://img.shields.io/badge/Policy-Fail--closed%20by%20default-critical)
![Risk](https://img.shields.io/badge/Risk-Sensitive%20data%20leakage-important)

> [!IMPORTANT]
> **This folder is a governance gate.**
> If a sensitivity test fails, treat it like a **potential data leak / policy regression** until proven otherwise.
>
> “Sensitivity” in KFM is not only *privacy*—it includes **culturally restricted knowledge**, **site protection**, **re-identification risk**, and **license/rights constraints** that must be enforced across pipeline → catalogs → API → UI/Focus Mode.

---

## Why this exists

KFM is designed to be a **governed spatio-temporal knowledge system** where outputs are:
- evidence-first (cite or abstain),
- auditable (policy + provenance),
- safe to share (sensitivity-aware), and
- constrained by the **trust membrane** (clients never directly access storage).

This directory contains tests that ensure KFM **never**:
- exposes restricted coordinates or identifiers,
- “accidentally upgrades” restricted data into a public output,
- prints sensitive values to logs/receipts,
- returns AI answers that leak restricted facts,
- bypasses policy checks (fail-open),
- weakens restrictions downstream (UI/exports) compared to upstream policy labels.

---

## What “sensitivity” means in KFM

Sensitivity is a **risk classification** applied to data, derived artifacts, and narrative outputs.

### Common sensitivity categories (examples)
- **Sensitive location**: precise coordinates for protected sites (archaeological, conservation, culturally restricted).
- **Personal info / private individuals**: names, addresses, contact details, or re-identifiable combinations in archival documents.
- **Culturally restricted knowledge**: content subject to community authority-to-control and/or restricted dissemination norms.
- **Small-area re-identification risk**: aggregated statistics that become identifying at fine spatial/temporal resolution.
- **Rights/licensing constraints**: content that is “viewable” but not freely reusable/exportable.

> [!NOTE]
> These tests do **not** decide what is sensitive. They enforce that **whatever is labeled sensitive/restricted** is treated as such *everywhere*.

---

## Non‑negotiable invariants (what these tests enforce)

| Invariant | Meaning in practice | Test signal |
|---|---|---|
| **Fail‑closed policy** | If policy label / required governance metadata is missing, access is denied or output is withheld/sanitized. | Unknown label ⇒ deny; missing governance fields ⇒ deny; policy engine errors ⇒ deny |
| **No downstream loosening** | An output can never be less restricted than its upstream inputs. | Derived/public artifact must be ≥ as restrictive as source |
| **Redaction at every layer** | Redaction/generalization isn’t “UI-only”; it must exist in processed data, catalogs, API, and UI/Focus. | Any unauthorized path yields redacted fields |
| **Trust membrane** | UI/external clients never hit DB/object store directly; all data flows through governed API + policy boundary. | Contract tests verify API is sole ingress; no direct storage URLs in public responses |
| **Cite or abstain (Focus Mode)** | If claims can’t be supported with allowed evidence, Focus Mode abstains without leaking restricted details. | AI output contains citations or abstention + safe reason |
| **Auditability** | Sensitive access/redaction should emit auditable events/refs (without logging sensitive payloads). | Audit refs exist; logs are structural, not raw values |

---

## Sensitivity labels & expected behavior

> KFM uses machine-checkable policy labels (example set shown below). Adjust the set to match the repo’s canonical policy schema.

| Label | Allowed to public? | Typical handling | “Must never happen” |
|---|---:|---|---|
| `public` | ✅ Yes | Full fidelity, normal citations | N/A |
| `restricted` | ❌ No | Deny or sanitize fields; role-based access | Expose full record/asset to unauthorized users |
| `sensitive-location` | ❌ No (precise) | **Generalize/blur** geometry; separate “public summary” from “restricted coordinates” | Return exact coordinates, exact address, or high-precision geometry publicly |

---

## What belongs in `tests/sensitivity/`

This suite is cross-cutting: it should validate **pipeline outputs**, **catalog metadata**, **API responses**, and **Focus Mode / Story Node behavior**.

### Test types (recommended)

| Test type | Purpose | Example assertion |
|---|---|---|
| **Unit** | Redaction & classification helpers behave deterministically | `generalizePoint(…)` rounds to required precision; PII scrubber removes emails |
| **Contract** | API shapes respect policy + include required provenance signals | `GET /dataset/:id` never returns restricted fields unless authorized; response includes provenance bundle pointer |
| **Integration** | End-to-end flow is safe by default | “sensitive-location” dataset queried as anonymous ⇒ generalized geometry only |
| **Regression / Golden** | Prevent “oops we leaked it again” | Known sensitive scenario stays sanitized across refactors |

---

## Directory layout

> Layout below is a **recommended** structure. Create/adjust subfolders to match your stack (TS/Node, Python, etc).

```text
tests/
└── sensitivity/
    ├── README.md                  # you are here
    ├── cases/                     # scenario definitions (golden)
    │   ├── api/                   # API contract scenarios (policy + redaction)
    │   ├── focus_mode/            # cite-or-abstain + safe phrasing checks
    │   ├── story_nodes/           # narrative artifacts: no leakage, has citations, safe abstentions
    │   └── pipelines/             # raw→work→processed: policy label propagation + catalog gates
    ├── fixtures/                  # SANITIZED fixtures only (never real restricted coords)
    │   ├── datasets/
    │   ├── catalogs/              # STAC/DCAT/PROV minimal examples (valid + invalid)
    │   └── prompts/               # Focus Mode prompt fixtures (safe)
    ├── helpers/                   # assertions + matchers + schema validators
    └── reports/                   # optional: machine-readable test artifacts (CI upload)
```

---

## Running locally

Run the suite using whatever runner the component uses.

### Examples (adjust to your stack)
```bash
# Python / pytest
pytest -q tests/sensitivity

# Node / Jest (or similar)
npm test -- tests/sensitivity

# Monorepo (example)
pnpm -r test --filter ./tests/sensitivity
```

> [!TIP]
> Keep sensitivity tests **offline** (no live upstream calls). Use fixtures or mocked connectors so failures are deterministic.

---

## Adding a new sensitivity test

### 1) Pick the failure mode you want to prevent
Examples:
- Coordinate precision regression (e.g., rounding removed).
- API starts returning restricted attributes in a “public” path.
- Focus Mode starts paraphrasing restricted values (even without direct citation).
- Logs/receipts accidentally include full payloads.

### 2) Create a scenario (“case”) with explicit expectations
**A case should include:**
- Input(s): fixture data, policy label(s), user role/context, request/query.
- Expected output: **sanitized** response shape, redaction/generalization rules, citations/abstention behavior.
- Negative assertions: things that must *not* appear (exact lat/long, addresses, IDs, etc.).

### 3) Ensure the case is safe to commit
- ✅ Use synthetic coordinates (or fuzzed/shifted values).
- ✅ Use fake names/emails/IDs.
- ❌ Never commit real protected site locations or restricted identifiers.

---

## Case format (suggested)

You can represent cases as YAML/JSON that your test runner loads.

```yaml
# tests/sensitivity/cases/api/sensitive_location__public_user.yaml
id: sensitive_location__public_user
intent: "Public user requests a sensitive-location dataset; response must be generalized or denied."
policy:
  dataset_label: sensitive-location
  user_role: public
request:
  method: GET
  path: /api/datasets/khri/features
expect:
  decision: allow_sanitized   # allow | deny | allow_sanitized
  redactions:
    geometry_precision: ">= 1km"   # example rule; align with policy
    removed_fields:
      - exact_coordinates
      - site_id
  must_not_contain:
    - "(-?\\d{1,3}\\.\\d{5,})"   # high-precision lat/long
    - "site_id"
  must_contain:
    - "coordinates have been generalized"
  provenance:
    required: true
    must_include:
      - dataset_id
      - policy_label
audit:
  required: true
  must_include:
    - audit_ref
```

> [!NOTE]
> The exact schema is flexible—what matters is **explicit expectations** and **negative assertions** (leak-prevention).

---

## Redaction/generalization assertions (common patterns)

Use matchers that can be shared across tests:

- **Geometry precision checks**
  - Must not exceed allowed decimal places.
  - Must not include full WKT/WKB for restricted geometries.
  - Must not return raw `bbox`/centroids that reconstruct precise sites.

- **Text leakage checks**
  - Must not include addresses, phone numbers, emails.
  - Must not include restricted record identifiers.
  - Must not include “helpful” paraphrases of restricted values.

- **Logging/receipt checks**
  - Logs are structural (event types, counts, IDs that are permitted), not raw payloads.
  - Receipts never embed restricted fields.

---

## CI expectations

Add these checks to your CI pipeline as **required status checks**:

- ✅ run `tests/sensitivity/**`
- ✅ upload machine-readable report artifacts (JUnit/JSON) (optional but recommended)
- ✅ block merges on failures
- ✅ treat sensitivity label changes as requiring governance review (human + automated)

### Definition of Done (DoD) for sensitivity changes
- [ ] Policy/schema change is documented (ADR or governance note).
- [ ] At least one new/updated sensitivity test exists for the change.
- [ ] Tests cover API + Focus Mode paths *if applicable*.
- [ ] Negative assertions added (what must never leak).
- [ ] No real sensitive data added to repo.
- [ ] CI is configured to fail the PR on policy regressions.

---

## Governance review triggers (human-in-the-loop)

Sensitivity changes often require review beyond automation.

Trigger a review when:
- classification/sensitivity labels change for a dataset,
- a new redaction/generalization rule is introduced,
- a dataset moves from restricted → public (or vice versa),
- Story Node publishing rules change for sensitive domains,
- export/download capabilities are added for restricted sources.

> [!IMPORTANT]
> **Do not “fix” sensitivity test failures by weakening tests.**
> Fix the code/policy/data flow so KFM stays safe-by-design.

---

## Troubleshooting

<details>
  <summary><strong>Common failure: “Policy missing / label unknown”</strong></summary>

- Expected in fail-closed systems.
- Fix by ensuring:
  - dataset has a valid policy label in canonical metadata,
  - catalogs propagate the label,
  - API reads labels from the source of truth,
  - “default deny” is preserved.

</details>

<details>
  <summary><strong>Common failure: “Output contains high-precision lat/long”</strong></summary>

- Fix by applying generalization in the correct layer:
  - processed dataset derivation (preferred),
  - API masking (required safety backstop),
  - UI-only masking is insufficient.

</details>

<details>
  <summary><strong>Common failure: “Focus Mode leaks restricted details in prose”</strong></summary>

- Fix by:
  - enforcing policy checks *post-generation*,
  - restricting retrieval results to permitted evidence for that user,
  - requiring cite-or-abstain and safe refusal phrasing.

</details>

---

## Glossary

| Term | Meaning |
|---|---|
| **Redaction** | Removing fields/content entirely (deny or withhold) |
| **Generalization** | Reducing precision (e.g., rounding coords, larger polygons, aggregation) |
| **Fail-closed** | If uncertain, deny or sanitize (never fail-open) |
| **Trust membrane** | Clients can’t directly access storage; governed API + policy boundary only |
| **Golden test** | A regression test that locks expected safe output for a known scenario |

---

### Maintainers

- Owners should include: governance lead + API owner + pipeline owner.
- Rotate reviewers when sensitivity policy changes.

> 🧷 Keep this README updated whenever policy labels, redaction rules, or governance invariants change.

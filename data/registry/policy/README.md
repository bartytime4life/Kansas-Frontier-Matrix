<!--
KANSAS FRONTIER MATRIX (KFM) — GOVERNED ARTIFACT
File: data/registry/policy/README.md

This directory contains *policy registry data* (facts/config) that power KFM’s fail-closed governance.
It is reviewed and versioned like code because it directly affects what may be promoted, served, or shown.

Key invariant reminders:
- Trust membrane: clients/UI never access storage directly; all access is via governed APIs + policy boundary.
- Fail-closed: missing/unknown policy inputs must deny rather than guess.
-->

# 🛡️ Policy Registry (Data)

![Governed Artifact](https://img.shields.io/badge/Governed-Artifact-blue)
![Default Deny](https://img.shields.io/badge/Default-Deny-critical)
![Policy Data](https://img.shields.io/badge/OPA-Data%20Inputs-informational)

This folder is the **policy registry** for Kansas Frontier Matrix (KFM): the **versioned policy facts** and **controlled vocabularies** used by:

- **CI policy gates** (merge-blocking “deny-by-default” checks)
- **Runtime authorization + redaction** (API calls policy engine before returning data)
- **AI/Focus/Story output safety** (policy can deny or require sanitization)

> [!IMPORTANT]
> This folder is **not** the Rego policy code.  
> Rego lives under `policy/opa/` (or equivalent). This folder provides the *data* that policies evaluate.

---

## What lives here

### ✅ Yes (policy *data*)

- Controlled vocabularies: sensitivity classes, access levels, policy labels
- Dataset/record/field policy declarations (per-dataset policy facts)
- Redaction profile definitions (what generalization/suppression is required)
- Regression test fixtures for policy behavior (“this must never leak again”)

### ❌ No (policy *code* or secrets)

- No `*.rego` (those belong in `policy/opa/`)
- No credentials, API keys, tokens, or private endpoints
- No raw sensitive locations, no “exact” archaeology site coordinates, no PII

---

## Non-negotiable invariants (KFM)

> [!IMPORTANT]
> These are KFM’s operational “constitution” for policy:
> - **Trust membrane:** frontend/external clients never talk to databases/object stores directly; access goes through governed API + policy boundary.
> - **Fail-closed:** missing policy inputs or ambiguous policy state must deny.
> - **Promotion gates:** Raw → Work → Processed promotion only when checks + policy pass.
> - **Cite-or-abstain:** if evidence/policy cannot support output, abstain with a safe explanation.

(If you need to change an invariant, do it via a reviewed architecture decision record and update the corresponding CI gates.)

---

## Directory layout

> [!NOTE]
> If some subfolders aren’t present yet, this README defines the intended layout for thin-slice implementation.

```text
data/registry/policy/
├── README.md
├── vocab/
│   ├── sensitivity_classes.yml        # recommended sensitivity taxonomy
│   ├── policy_labels.yml              # labels used at dataset/record/field level
│   └── access_levels.yml              # coarse access controls (e.g., public/restricted)
├── datasets/
│   └── <dataset_id>.policy.yml        # per-dataset policy declaration (governed)
├── redaction/
│   ├── profiles/
│   │   └── <profile_id>.yml           # reusable redaction/generalization rules
│   └── README.md                      # optional: redaction-specific notes
└── tests/
    ├── fixtures/                      # pass/fail fixtures consumed by conftest/OPA tests
    └── golden_queries/                # non-regression checks (must fail forever if unsafe)
```

---

## Sensitivity classes and labels

KFM treats sensitivity as a first-class governed concept. The recommended set is:

- **Public**: safe to publish without redaction
- **Restricted**: role-based access required (example: parcel ownership)
- **Sensitive-location**: coordinates must be generalized or suppressed (example: archaeology, sensitive species)
- **Aggregate-only**: publish only above thresholds (example: health/crime small counts)

### Suggested mapping

| Concept | Purpose | Where used |
|---|---|---|
| `sensitivity_class` | Human + governance classification | dataset policy + UI metadata |
| `policy_label` | Machine-enforced label at dataset/record/field level | policy engine + CI gates |
| `access_level` | Coarse access category (who may request the dataset) | API auth + policy |

> [!TIP]
> Keep vocabularies small, explicit, and stable. Add new values only when policy + tests are ready.

---

## Redaction is a first-class transformation

KFM redaction/generalization is not an ad-hoc UI trick — it’s a **governed transformation**:

- Raw remains immutable.
- A redacted/generalized derivative is a **separate DatasetVersion** (often a separate `dataset_id`).
- The redaction step is recorded in provenance (PROV), and the derivative carries a policy label.

> [!WARNING]
> Sensitive-location governance must be built in, not bolted on. Prefer a **dual-asset model**:
> - **Public generalized** derivative
> - **Restricted precise** dataset (never exposed publicly)

---

## Data contracts

> [!IMPORTANT]
> Treat policy registry YAML/JSON as **contracts**.  
> They should be schema-validated and tested in CI.

### Dataset policy record (recommended minimum)

Each `datasets/<dataset_id>.policy.yml` should include:

| Field | Required | Type | Notes |
|---|---:|---|---|
| `dataset_id` | ✅ | string | Canonical dataset identifier (stable) |
| `status` | ✅ | enum | `active` \| `withdrawn` (deny if withdrawn) |
| `policy_label` | ✅ | enum | e.g., `public`, `restricted`, `sensitive-location`, `aggregate-only` |
| `access_level` | ✅ | enum | e.g., `public`, `restricted` |
| `sensitivity_class` | ✅ | enum | recommended taxonomy (see above) |
| `owner_group` | ⛔️* | string | Required when not public (who governs access) |
| `redaction_profile` | ⛔️* | string | Required when label implies redaction/generalization |
| `notes.rationale` | ✅ | string | Why this policy exists (safe wording) |
| `change_log` | ✅ | list | Human-readable history (date, change summary) |

\* *“Required when applicable” is enforced by policy tests (deny-by-default).*

#### Example: dataset policy file

```yaml
# datasets/kfm_khri.policy.yml
dataset_id: "kfm:khri"
status: "active"

# classification
sensitivity_class: "sensitive-location"
policy_label: "sensitive-location"
access_level: "restricted"

# governance ownership (required when not public)
owner_group: "kfm-governance-heritage"

# required transformations for any public-facing derivative
redaction_profile: "khri_public_generalized_v1"

notes:
  rationale: "Precise site locations must not be published; only generalized derivatives may be public."
  contact: "governance@kfm.example" # (example; avoid personal emails)

change_log:
  - date: "2026-02-17"
    change: "Initial policy declaration."
```

---

## Redaction profiles

Redaction profiles are reusable transformation specs for sensitive outputs.

### Example: sensitive-location generalization profile

```yaml
# redaction/profiles/khri_public_generalized_v1.yml
profile_id: "khri_public_generalized_v1"
applies_to:
  policy_label: "sensitive-location"

actions:
  - type: "geometry_generalize"
    method: "centroid"          # or "grid_snap", "bbox_only", etc.
    params:
      max_precision: "coarse"   # deliberately abstract; do not encode exact thresholds here unless governed
  - type: "suppress_fields"
    fields:
      - "owner_name"
      - "exact_site_location"
      - "access_instructions"

provenance:
  prov_activity_type: "kfm:redaction"
  statement: "Public derivative created by governed redaction profile; raw remains restricted."
```

> [!CAUTION]
> Do **not** encode “how to find sensitive things” in policy docs.  
> Redaction params should be expressed at a level that supports enforcement without increasing harm.

---

## How policy data is used

### CI (merge-blocking)

At minimum, CI should:

- Validate policy registry files against schemas (YAML/JSON schema)
- Run Conftest/OPA tests with **deny-by-default**
- Run **non-regression tests**:
  - golden queries that previously leaked restricted fields must fail forever
  - negative tests ensure sensitive-location data cannot be returned at high precision to unauthorized roles
  - audit integrity tests ensure every API response includes audit reference + evidence hash

### Runtime (API + policy engine)

KFM APIs should call the policy engine before returning data, stories, or AI outputs. Policies can:

- allow
- deny
- allow-with-required-sanitization (API performs the sanitization step declared by policy/redaction profile)

```mermaid
flowchart LR
  UI[Web UI / Clients] -->|requests| API[Governed API]
  API -->|decision input| OPA[Policy Engine (OPA)]
  OPA -->|allow / deny / sanitize| API
  API -->|sanitized response| UI

  subgraph Repo[Repo as Source of Truth]
    Rego[policy/opa/*.rego]
    PolicyData[data/registry/policy/*]
  end

  Repo --> CI[CI Gates: schema + conftest + regression]
  CI --> Deploy[Deploy policy bundle + registry data]
  Deploy --> OPA
```

---

## Making changes (safe workflow)

1. Update vocab (if needed) in `vocab/` **first**
2. Add/update dataset policy declaration in `datasets/`
3. Add/update redaction profile (if applicable)
4. Add/extend tests in `tests/` (include at least one deny test if changing restrictions)
5. Run local checks (example commands; adjust to repo tooling):
   - `conftest test data/registry/policy --policy policy/opa`
   - `conftest test tests/fixtures --policy policy/opa`
6. Open a PR with:
   - clear rationale
   - evidence for why policy is required
   - explicit mention of whether this changes public outputs

> [!IMPORTANT]
> Policy changes are behavior changes. Treat them like production code:
> - Require governance review (CODEOWNERS)
> - Require green CI gates
> - Prefer small, reversible increments

---

## Definition of Done (DoD) for policy registry changes

- [ ] Controlled vocab updated (if needed) and documented
- [ ] Dataset policy record updated and schema-valid
- [ ] Redaction profile updated (if applicable)
- [ ] At least **one deny test** added/updated for restricted behavior
- [ ] At least **one allow test** added/updated for authorized behavior
- [ ] Non-regression tests included if fixing/mitigating a leak
- [ ] CI passes with deny-by-default posture (no “soft fail”)
- [ ] Change log entry added to the dataset policy record

---

## Safety / sensitivity guardrails

> [!WARNING]
> Never commit:
> - precise sensitive locations (archaeology sites, sensitive species)
> - PII (names, addresses, emails of private individuals)
> - secrets (tokens, credentials)
>
> If you need to reference a sensitive source for governance review, use a **redacted reference** and store details in approved secure channels (not in git).

---

## Design sources (internal)

- KFM Comprehensive Data Source Integration Blueprint (v1.0, 2026-02-12)
- KFM Integration Idea Pack (2026-02-15)
- KFM Comprehensive Technical Blueprint (policy enforcement, auditability, OPA integration)

(Keep these references high-level; avoid embedding restricted or private source content here.)

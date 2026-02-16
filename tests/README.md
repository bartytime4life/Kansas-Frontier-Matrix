<!--
GOVERNED ARTIFACT NOTICE

This README is a governed artifact.

Why: It defines KFM’s automated trust enforcement. In KFM, tests are not “nice to have” — they are part of
the trust boundary and the promotion gatehouse.

Rule: If you change meaning (not just wording), route through governance review:
- required reviewers via CODEOWNERS
- the matching CI gates MUST be updated so the system remains fail-closed and deterministic

If a rule is missing or unclear, treat it as a governance gap and add the smallest enforceable test + doc fix.
-->

# 🧪 KFM Test Suite

![Governed](https://img.shields.io/badge/governed-critical-991b1b)
![Fail-closed](https://img.shields.io/badge/fail--closed-required-111827)
![Evidence-first](https://img.shields.io/badge/evidence--first-required-0f766e)
![Trust membrane](https://img.shields.io/badge/trust%20membrane-enforced-16a34a)
![Policy-as-code](https://img.shields.io/badge/policy-OPA%2FRego-2563eb)
![Promotion Contract](https://img.shields.io/badge/promotion-contract-7c3aed)
![Deterministic](https://img.shields.io/badge/determinism-spec__hash%20%7C%20checksums-6a5acd)
![Cite or abstain](https://img.shields.io/badge/focus%20mode-cite%20or%20abstain-critical)

KFM is a governed system. That means tests do more than validate correctness — they **enforce trust**:

- **Fail-closed gates:** missing proofs → no merge / no promotion
- **Evidence-first behavior:** claims must cite resolvable evidence or abstain/deny
- **Trust membrane:** UI/external clients **never** access stores directly (DB/graph/search/object store)
- **Sensitivity controls:** restricted & sensitive-location data must not leak (ever)
- **Deterministic receipts:** reproducibility via `spec_hash`, run manifests, and checksums
- **Audit integrity:** every governed response carries `audit_ref` and traceable evidence linkage

> [!IMPORTANT]
> The fastest way to break KFM is to let tests become “optional.”  
> This suite is the automated constitution: if it doesn’t fail when trust is violated, the platform is lying.

---

## Table of contents

- [Governance header](#governance-header)
- [Trust contract](#trust-contract)
- [Non-negotiables](#non-negotiables)
- [Change impact map](#change-impact-map)
- [Test taxonomy](#test-taxonomy)
- [Directory layout](#directory-layout)
- [Local quickstart](#local-quickstart)
- [Determinism guardrails](#determinism-guardrails)
- [Test data governance](#test-data-governance)
- [Governed artifact validation](#governed-artifact-validation)
- [Policy tests](#policy-tests)
- [Promotion & receipt tests](#promotion--receipt-tests)
- [Catalog & provenance tests](#catalog--provenance-tests)
- [Contract tests](#contract-tests)
- [Evidence resolver tests](#evidence-resolver-tests)
- [Focus Mode regression](#focus-mode-regression)
- [UI trust membrane tests](#ui-trust-membrane-tests)
- [Sensitivity regression](#sensitivity-regression)
- [Audit integrity tests](#audit-integrity-tests)
- [Security gates](#security-gates)
- [CI gatehouse mapping](#ci-gatehouse-mapping)
- [Gate IDs registry](#gate-ids-registry)
- [Contributing rules](#contributing-rules)
- [Troubleshooting](#troubleshooting)
- [References](#references)
- [FAQ](#faq)

---

## Governance header

| Field | Value |
|---|---|
| Document | `tests/README.md` |
| Status | **Governed** |
| Scope | Test taxonomy, release-blocking gates, fixture & baseline rules, deterministic receipts, sensitivity protections |
| Version | `v3.1.0` *(governed; SemVer applies)* |
| Effective date | 2026-02-16 |
| Owners | `.github/CODEOWNERS` *(if missing → governance gap)* |
| Review triggers | Any change affecting: fail-closed semantics, deny-by-default policy, sensitivity handling, contract compatibility, receipts/spec hashing, audit requirements, **or gate status-check names** |

> [!NOTE]
> “SemVer applies” means: if you change a contract or gate requirement, you’re changing system behavior.  
> Treat that like an API change, not a README tweak.

---

## Trust contract

KFM tests exist to uphold one principle:

> **If KFM cannot prove something is allowed and supported by evidence, KFM must not ship it.**

That principle becomes enforceable through:

### 1) Promotion is proof-based

A dataset (or derived artifact) is not “real” until the system can prove:

- where it came from (**raw capture**)
- how it was processed (**lineage/provenance**)
- what it contains (**catalogs + schemas**)
- what its rights/sensitivity are (**labels + license**)
- that it is reproducible (**receipts + digests + spec hashing**)

### 2) Serving truth is processed-only

KFM user-facing surfaces (API/UI/Story Nodes/Focus Mode) must serve from **Processed** artifacts and their
governed metadata.

### 3) Every claim has a citation contract

For Story Nodes and Focus Mode:

- **Citations must resolve** to a human-reviewable view
- If evidence is insufficient or non-resolvable → **abstain/deny**
- Every governed response must produce **`audit_ref`**

---

## Non-negotiables

These are invariants. Tests exist specifically to make violations impossible to merge.

1) **Fail closed**
- If policy, schemas, receipts, catalogs, or proofs cannot be validated → block merge/promotion.

2) **Deny by default**
- Policy evaluation must default-deny. Tests must prove both:
  - allow works when fully satisfied
  - deny triggers on missing keys / malformed inputs / uncertainty

3) **Evidence-first**
- No evidence → no claim.
- “Best guess” is not acceptable in governed answers. “I don’t know” (abstain) is correct.

4) **Trust membrane**
- UI and external clients **never** touch stores directly:
  - PostGIS/Postgres
  - graph store
  - search/vector
  - object store / artifact bucket
- All access flows: **UI → API → policy → stores → API → UI**

5) **Sensitivity protection**
- Restricted/sensitive-location/aggregate-only rules must be enforced in:
  - retrieval
  - response shaping
  - evidence resolution
  - UI presentation
- Tests must include *deny* cases and known leak regressions.

6) **Determinism**
- Re-runs of the same spec on the same inputs must produce:
  - stable hashes/checksums
  - stable normalized catalogs
  - stable receipts (or stable equivalence fields)

7) **Governance surface protection**
- The enforcement artifacts must be protected from unreviewed change:
  - `.github/CODEOWNERS` must exist
  - governance surfaces (tests/policy/schemas/CI workflows) must be CODEOWNERS-owned
  - CI must include the gates listed in this document (fail-closed)

> [!IMPORTANT]
> If governance surfaces are not protected, an attacker (or accident) can weaken gates and change “truth.”

---

## Change impact map

Use this to decide what must be updated in the same PR.

| If you change… | You MUST update/add… | Gate that will (should) fail if you don’t |
|---|---|---|
| Policy logic or policy input schema | policy unit tests + deny regressions + policy bundle compile tests | `policy/*` tests + conftest/OPA compile |
| API request/response shapes | OpenAPI validation + contract tests + golden schema fixtures | contract gate (OpenAPI diff) |
| Evidence resolver logic | resolver contract tests + 403/404 non-leaky cases + bounded-call assertions | evidence contract gate |
| Receipt/run manifest format | receipt schema tests + checksum verification + spec_hash semantics tests | promotion/receipt gate |
| Catalog emitters (DCAT/STAC/PROV) | schema validation + cross-link checks + golden normalized snapshots | catalog/prov gate |
| Focus Mode prompting / citation rules | gold-set regression + citation resolvability checks + abstain cases | focus regression gate |
| UI data access or network layer | trust membrane static checks + e2e smoke flows | ui membrane gate |
| Redaction/generalization rules | sensitivity regression suite + deny/leak tests + approval updates | sensitivity gate |
| Audit/logging surfaces | audit integrity tests + audit fetch/linkage tests | audit gate |
| Governance ownership / CI gate list | CODEOWNERS protection tests + CI “required checks” registry updates | governance surface gate |

> [!TIP]
> If you’re unsure, add the smallest negative test that would have caught the regression you’re afraid of.

---

## Test taxonomy

KFM tests are grouped by the kind of trust guarantee they enforce.

| Category | Purpose | Must be deterministic? | Runs on |
|---|---|---:|---|
| Unit | pure logic correctness; no network/services | ✅ | local + PR |
| Integration | adapters + real services (DB/OPA/etc.) | ✅ *(with pinned fixtures)* | PR + main |
| Contract | API compatibility (OpenAPI + runtime contract checks) | ✅ | PR + main |
| Policy | OPA/Rego + deny-by-default regression proofs | ✅ | PR + main |
| Receipts | run receipts + checksums + `spec_hash` semantics | ✅ | PR + main |
| Catalog/Prov | DCAT/STAC/PROV validation + cross-links | ✅ | PR + main |
| Regression | gold sets for Focus Mode, redaction, story rendering | ✅ | PR + main |
| E2E | full system flow (UI ↔ API ↔ policy ↔ evidence) | ✅ *(controlled env)* | nightly + release |
| Security | scanning + hardened CI rules | ✅ | PR + main |
| Governance surface | verifies enforcement artifacts are protected and present | ✅ | PR + main |

---

## Directory layout

Your repo may vary, but the concepts below are **normative**.

```text
tests/
├─ README.md                         # governed: this file
│
├─ unit/                             # hermetic unit tests (no services, no network)
├─ integration/                      # container-backed integration tests
├─ contract/                         # OpenAPI validation + compatibility tests
├─ policy/                           # OPA/Rego tests + fixtures (deny-by-default)
├─ receipts/                         # run receipts + spec_hash + checksum proofs
├─ catalogs/                         # DCAT/STAC/PROV validation + cross-link checks
├─ evidence/                         # evidence resolver contract tests (ref → view)
├─ focus/                            # Focus Mode gold sets + eval harness
├─ ui/                               # trust membrane checks + E2E smoke tests
├─ sensitivity/                      # redaction/generalization + leak regressions
├─ audit/                            # audit_ref presence + audit linkage tests
├─ security/                         # SAST/SCA/secret scanning + workflow hardening tests
├─ governance/                       # CODEOWNERS + CI gate registry + governed-doc integrity tests
│
├─ fixtures/
│  ├─ synthetic/                     # synthetic only (preferred)
│  ├─ public/                        # public-domain or explicitly licensed fixtures
│  ├─ gold/                          # governance-reviewed gold sets (diff-only updates)
│  └─ snapshots/                     # normalized outputs (stable diffs)
│
└─ helpers/                          # shared utilities (must not introduce non-determinism)
```

> [!IMPORTANT]
> Real restricted datasets do **not** belong in test fixtures. If a regression requires a sensitive example,
> create a synthetic proxy that exercises the same rule.

---

## Local quickstart

KFM can be implemented with different stacks (Go/Node/Python). This README standardizes **intent** and
**interfaces**, not a single language runtime.

### Fast path

Run the checks that must pass before you open a PR:

- unit tests
- policy tests
- receipt/cert proofs validation
- schema validations (OpenAPI + catalogs)

Example interface (recommended):

```bash
# local, fast
make test-unit
make test-policy
make test-contract
make test-receipts
make test-catalogs
make test-governance
```

### Full suite

Bring up services and run integration/regression:

```bash
docker compose up -d --build
make test-integration
make test-focus
make test-ui-smoke
docker compose down -v
```

> [!NOTE]
> Your repo may not use `make`. If so, implement the same interface via scripts
> (e.g., `./tools/test/*.sh`) so CI and local workflows stay consistent.

---

## Determinism guardrails

Determinism isn’t a vibe. It’s a testable property.

### Required controls

- Freeze time in tests (or inject a clock) — no “now()” in golden outputs
- Seed randomness in any test that uses RNG
- Normalize ordering before snapshotting (stable key order, stable list order)
- Fix locale/timezone in CI:
  - `TZ=UTC`
  - `LC_ALL=C` (or another explicit locale)
- For reproducible archives/build outputs, prefer a deterministic timestamp input such as `SOURCE_DATE_EPOCH`
  *(where your build tools support it)*

### Required assertions

- Two runs of the same spec + same fixtures produce identical:
  - `spec_hash`
  - checksums
  - normalized catalogs/snapshots

> [!TIP]
> If a test flakes, treat it as a trust failure until proven otherwise.

---

## Test data governance

Test data is a governed surface. It can leak secrets, break determinism, or create licensing risk.

### Allowed fixture classes

| Fixture class | Allowed? | Notes |
|---|---:|---|
| Synthetic (generated) | ✅ | preferred; easiest to govern |
| Public domain | ✅ | keep source metadata and license note |
| Open licensed (CC0/CC BY) | ✅ | store attribution + license text |
| Restricted / embargoed | ❌ | never commit; simulate |
| Sensitive locations / cultural heritage | ❌ | use generalized synthetic examples |

### Fixture requirements

All fixtures under `tests/fixtures/**` must include:

- provenance note (source or generator)
- license/sensitivity classification
- expected normalization rules (so diffs don’t churn)

Recommended pattern:

```text
tests/fixtures/public/<dataset>/
├─ README.md        # source, license, sensitivity, purpose
├─ input.*          # raw fixture
└─ expected.*       # normalized expected output (if applicable)
```

---

## Governed artifact validation

Tests must validate (and block drift of) these artifact classes:

- **Schemas & contracts**
  - OpenAPI for `/api/v1`
  - JSON Schemas for receipts/run records
  - Story Node schema
  - Evidence reference grammar (e.g., `stac://`, `prov://`)

- **Policy bundles**
  - compile + unit tests
  - regression denies

- **Promotion proofs**
  - checksums and digest files
  - deterministic `spec_hash`

- **Catalogs & lineage**
  - DCAT always for datasets
  - STAC when spatiotemporal assets exist
  - PROV for lineage of derived artifacts

- **Audit artifacts**
  - response `audit_ref`
  - server-side audit record linking decisions → evidence

- **Governance surfaces**
  - `.github/CODEOWNERS` exists
  - CODEOWNERS covers: `tests/**`, `policy/**`, `schemas/**`, `.github/workflows/**` *(or equivalent paths)*
  - CI exports status checks listed in [Gate IDs registry](#gate-ids-registry)

> [!IMPORTANT]
> If a governed artifact exists, it must be validated.
> If it doesn’t exist yet, the missing validator is a governance gap — not a “later” task.

---

## Policy tests

Policy is the active enforcement mechanism. KFM policy must be **deny-by-default**.

### What policy tests must prove

- missing/invalid input → deny
- default deny is preserved (no “allow all” fallback)
- cite-or-abstain enforcement (Focus Mode + Story Nodes)
- sensitivity rules: restricted/sensitive-location/aggregate-only
- role-based access control (RBAC) and least privilege
- non-leaky errors (no revealing of protected facts in deny messages)

### Recommended structure

- Table-driven tests (inputs + expected decisions)
- Explicit “missing key” tests for every required field
- A regression pack for known leak patterns

Example commands (if applicable):

```bash
opa test ./policy -v
conftest test . -p policy/conftest
```

> [!NOTE]
> Policy tests are not optional “security tests.” They are required correctness tests for KFM.

---

## Promotion & receipt tests

Promotion is blocked unless proofs validate.

### Terms (KFM-style)

- **run_record**: what happened (inputs, steps, outputs)
- **run_manifest**: what is being promoted (distributions, checksums, catalogs)
- **spec_hash**: deterministic hash of canonicalized spec/config used to produce outputs
- **checksums**: integrity proof of artifacts promoted/served

### Required assertions

- schemas validate for run records/manifests
- required keys exist (fail closed on missing fields)
- checksums exist and match artifacts
- `spec_hash` is stable and computed by documented rules
- referenced catalogs exist and validate
- missing license/sensitivity metadata → promotion fails

### Required negative tests

- checksum mismatch → fail
- missing catalogs → fail
- missing required receipt keys → fail
- missing sensitivity classification → fail

### Normative `spec_hash` algorithm (v1)

This defines the minimum deterministic contract for `spec_hash` *(additive, governed)*.

- Inputs:
  - a **spec object** (pipeline config) in JSON form
- Canonicalization (KFM-CJSON-1):
  - UTF‑8
  - object keys sorted lexicographically
  - no insignificant whitespace
  - numbers rendered without exponent where possible, with trailing zeros removed
- Hash:
  - `spec_hash = sha256(canonical_json_bytes)`
  - rendered as lowercase hex (64 chars)

Example representation:

```text
spec_hash: "ea37e38b850144a874afbf15e42c5f8fcb187ecf78166e6194eb12c9eb503643"
```

### Normative checksum file format (v1)

- Hash algorithm: SHA‑256
- File: `SHA256SUMS` (or equivalent) containing lines like:

```text
<hex_sha256><two_spaces><relative_path>
```

- Lines must be sorted by `relative_path` (stable diff)
- Verifiers must treat missing checksum entries as **fail-closed**

---

## Catalog & provenance tests

Catalogs are how KFM remains inspectable and interoperable.

### Required validations

- DCAT exists and validates *(required for all datasets)*
- STAC validates when applicable (collections/items/assets consistent)
- PROV validates (raw → derived lineage expressed)
- cross-links are clean (no dangling refs)
- digests match declared distributions/assets
- normalization is stable (to avoid noisy diffs)

### Test styles

- JSON Schema validation
- “golden normalized” snapshots for catalog outputs
- integration slice tests: small fixed datasets → stable outputs

> [!TIP]
> Normalize catalogs before snapshotting: stable ordering, stable formatting, stable IDs.

---

## Contract tests

Contracts define how the trust membrane is consumed.

### API stability rules

- `/api/v1` is stable. Breaking changes require a new version line (`/api/v2`).
- Contract tests must detect breaking changes against:
  - main branch baseline, or
  - the last tagged release spec

### Contract test scope

- OpenAPI schema validity
- endpoint compatibility checks for:
  - catalogs
  - evidence resolver
  - Focus Mode output schema
  - audit record retrieval (where applicable)
- “fail closed” error semantics (denies are safe and non-leaky)

---

## Evidence resolver tests

Evidence must be reviewable — citations are not “decorations.”

### Resolver acceptance criteria

- each citation reference resolves to a **human-readable view**
- unauthorized → 403 with non-leaky body
- missing → 404
- resolver outputs include metadata needed for review:
  - license/attribution
  - ids/digests when available
  - sensitivity class

### Performance constraint

- citations must resolve in a **bounded number of calls** (UI requirement)
- tests should enforce server-side behavior that supports this

### Normative evidence reference grammar (v1)

Evidence references must be parseable and resolvable by the evidence resolver.

Minimum contract:

- `evidence_ref` MUST be a URI with a known scheme
- schemes MAY include (non-exhaustive): `stac://`, `dcat://`, `prov://`, `file://`
- unknown scheme → deny/abstain

Recommended EBNF:

```ebnf
evidence_ref = scheme, "://", path, [ "#", fragment ] ;
scheme       = 1*( ALPHA / DIGIT / "+" / "-" / "." ) ;
path         = 1*( pchar / "/" ) ;
fragment     = 1*( pchar / "/" / "?" ) ;
```

> [!NOTE]
> This grammar is intentionally minimal; scheme-specific parsing belongs to the resolver adapter layer.

---

## Focus Mode regression

Focus Mode is governed: **cite or abstain**.

### Gold-set rules

Gold sets assert behavior, not “preferred wording.”

- evidence-required questions → citations present
- insufficient evidence → abstain/deny (no bluffing)
- citations resolvable via evidence resolver
- sensitivity gates respected (no leaks)
- `audit_ref` always present

### Gold-set format (recommended)

```yaml
id: focus_001
question: "When was X established?"
view_state:
  map:
    bbox: [-102.0, 36.9, -94.6, 40.0]
expected:
  allowed: true
  must_abstain: false
  min_citations: 2
  deny_reasons: []
```

### Updating gold sets

Gold sets are governed baselines. Changes require:

- explicit rationale in PR description
- diff review by CODEOWNERS
- confirmation that sensitivity constraints did not weaken

---

## UI trust membrane tests

The UI must not bypass governance.

### Must enforce

- no DB connection strings in frontend
- no direct connections to:
  - PostGIS/Postgres
  - graph DB
  - search/vector service
  - object store
- network calls are restricted to governed API endpoints

### Mechanisms

- static analysis (forbidden hosts/imports/ports)
- E2E smoke flows:
  - load story
  - open evidence panel
  - resolve citations (via resolver, not DB)
  - verify deny behavior is non-leaky

> [!IMPORTANT]
> A UI bypass is a total trust failure. Treat these tests like auth tests.

---

## Sensitivity regression

KFM sensitivity rules must not regress.

### Baseline classes

- public
- restricted
- sensitive-location
- aggregate-only

### Required tests

1) **Golden deny** queries for known leak patterns
2) Unauthorized access to high-precision sensitive-location outputs → deny
3) Field-level redaction/suppression tests
4) Evidence resolver non-leak checks
5) Audit linkage checks for governed responses

> [!NOTE]
> A “passing” sensitivity suite must include deny cases.
> It must prove the system refuses correctly — not just that it returns data.

---

## Audit integrity tests

Auditability is a trust requirement.

### Required assertions

- governed responses include `audit_ref`
- responses contain citations **or** are abstentions/denials (never unsupported claims)
- audit record (when fetched) links to:
  - policy bundle/version (if available)
  - evidence refs / digest bundle (if available)
  - request metadata (redacted appropriately)

### Recommended approaches

- contract tests on response schemas
- integration tests that fetch audit records and validate linkage

---

## Security gates

Security gates protect the repository and the CI pipeline itself.

Minimum expectations:

- secret scanning and push protections (no secrets in git history)
- dependency scanning (SCA) and alert handling
- workflow hardening:
  - least-privilege `GITHUB_TOKEN`
  - pinned action SHAs (or at least pinned major versions + reviewed)
  - avoid dangerous triggers for untrusted PRs
- branch protection:
  - required reviews
  - required status checks
  - optional signed commits for high-trust repos

Additional governance surface expectations:

- `.github/CODEOWNERS` exists and is reviewed like code
- CODEOWNERS covers enforcement surfaces:
  - tests, policy, schemas, CI workflows, gate registry docs

> [!IMPORTANT]
> CI is part of the trust boundary.  
> If an attacker can change the tests or skip them, they can change “truth.”

---

## CI gatehouse mapping

KFM should structure CI so that fail-closed gates run on every PR, with heavier checks deferred to nightly/release.

### Pull request gates (merge-blocking)

- ✅ unit tests
- ✅ policy tests (OPA/Rego + regression denies)
- ✅ receipt/spec_hash/checksum validation
- ✅ catalog validation (DCAT always; STAC/PROV when applicable)
- ✅ OpenAPI validation + compatibility diff
- ✅ Focus Mode gold-set regression (small, curated)
- ✅ UI trust membrane static analysis
- ✅ sensitivity regression (core deny cases)
- ✅ audit integrity assertions
- ✅ governance surface validation (CODEOWNERS + gate registry presence)

### Main branch / post-merge gates

- integration tests (containers + real services)
- expanded gold sets
- full catalog cross-link validation
- smoke E2E

### Nightly / pre-release gates

- full E2E suite
- performance/regression tracking
- long-running ingestion/promotion rehearsal
- security deep scans (if slower)

---

## Gate IDs registry

These are the **normative** gate identifiers and recommended CI status-check names.
Branch protection should require the status checks in this table (or documented equivalents).

> [!IMPORTANT]
> If a gate is required by this document but absent in CI, that is a governance gap.

| Gate ID | Recommended status check name | Merge-blocking? | Notes |
|---|---|---:|---|
| `unit` | `kfm/unit` | ✅ | fast + hermetic |
| `policy` | `kfm/policy` | ✅ | deny-by-default proofs |
| `contract` | `kfm/contract` | ✅ | OpenAPI validity + diff |
| `receipts` | `kfm/receipts` | ✅ | `spec_hash` + checksums |
| `catalogs` | `kfm/catalogs` | ✅ | DCAT required; STAC/PROV as applicable |
| `focus` | `kfm/focus` | ✅ | curated gold-set pack |
| `ui-membrane` | `kfm/ui-membrane` | ✅ | static checks + smoke |
| `sensitivity` | `kfm/sensitivity` | ✅ | must include deny cases |
| `audit` | `kfm/audit` | ✅ | `audit_ref` + linkage checks |
| `governance-surface` | `kfm/governance-surface` | ✅ | CODEOWNERS + gate registry |
| `security` | `kfm/security` | ✅ | secrets/SCA/workflow hardening |

---

## Contributing rules

### Golden rules

- **Don’t weaken a gate to “fix CI.”** Fix the bug or the missing proof.
- **Prefer negative tests for forbidden outcomes** (leaks, bypasses, missing proofs).
- **Make tests deterministic** (pin fixtures, freeze time, seed randomness).
- **No secrets. No restricted data. No surprise network calls.**

### PR checklist

#### All PRs
- [ ] Updated/added tests for affected subsystems (see [Change impact map](#change-impact-map))
- [ ] No secrets in code/logs/fixtures
- [ ] Deterministic outputs (time frozen / randomness seeded)
- [ ] Schema + contract changes are versioned and documented
- [ ] Fixtures include provenance + license + sensitivity metadata

#### Policy PRs
- [ ] Allow and deny cases covered
- [ ] Missing-key tests included (fail closed)
- [ ] Regression denies updated/added for new edge cases

#### API/Contract PRs
- [ ] OpenAPI updated and valid
- [ ] `/api/v1` compatibility proven (or moved to `/api/v2`)
- [ ] Audit + evidence response schemas updated

#### Data/Catalog PRs
- [ ] DCAT present and valid
- [ ] STAC/PROV present when applicable
- [ ] checksum and receipt tests added
- [ ] sensitivity class + redaction tests included as needed

#### Focus Mode PRs
- [ ] Gold sets updated/added
- [ ] Abstain behavior verified
- [ ] Citations resolvable verified

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Policy denies everything | missing policy input keys or schema drift | fix input schema + fixtures; prove allow without weakening default deny |
| Receipt tests fail | missing keys or unstable hash/digest generation | stabilize canonicalization + emitter; keep fail-closed |
| Catalog tests fail | invalid DCAT/STAC/PROV or broken links | fix catalogs; re-normalize; verify checksums |
| Contract tests fail | `/api/v1` breaking change | restore compatibility or move change to `/api/v2` |
| Gold set fails | behavior drift or policy tightening | confirm intent; update gold set only with governance rationale |
| UI trust membrane fails | UI calling stores directly | route through governed API; remove forbidden hosts/ports |
| Governance surface gate fails | CODEOWNERS missing or not protecting enforcement paths | add/repair CODEOWNERS; ensure gate registry is enforced |

---

## References

### KFM internal design authority

- KFM Next-Gen Blueprint & Primary Guide (governance invariants, CI gate expectations)
- KFM Comprehensive Data Source Integration Blueprint (promotion gates, catalogs, sensitivity classes)
- KFM Project Blueprint & Companion Blueprint (system invariants + “closing the enforcement loop”)
- KFM Master Corpus Consolidation Spec (schemas, deterministic IDs, provenance + retrieval constraints)

### External standards and tools

- STAC (spatiotemporal asset catalogs)
- DCAT (dataset catalog vocabulary)
- W3C PROV (provenance/lineage model)
- OPA/Rego (policy-as-code)
- JSON canonicalization for deterministic hashing (`spec_hash`) where applicable

---

## FAQ

<details>
  <summary><strong>Why treat tests as governance artifacts?</strong></summary>

Because in KFM, trust is a product feature — and tests are the automated enforcement mechanism.

A “green build” must mean:

- promotion proofs are present and correct,
- policy is deny-by-default and sensitivity-safe,
- the UI cannot bypass governance,
- citations resolve or the system abstains,
- and every served claim is auditable.

If the test suite doesn’t enforce those, KFM becomes a normal data app — and loses its core promise.

</details>

<details>
  <summary><strong>What does “fail-closed” mean in practice?</strong></summary>

Fail-closed means the safe default is denial:

- if a schema is missing → fail
- if a checksum can’t be verified → fail
- if a policy input is malformed → deny
- if evidence cannot be resolved → abstain/deny

Fail-open is faster in the short term but destroys trust long term.

</details>

<details>
  <summary><strong>What’s the smallest acceptable test for a new feature?</strong></summary>

Add one negative test that proves KFM refuses unsafe behavior, and one positive test that proves it allows
safe behavior when requirements are satisfied.

Start with the smallest gate that would have prevented the most damaging regression.

</details>

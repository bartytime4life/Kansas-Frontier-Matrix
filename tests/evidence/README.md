# tests/evidence/ — Evidence Tests (Governed • Fail-Closed • Merge-Blocking)

![governed](https://img.shields.io/badge/governed-yes-2b6cb0)
![evidence-first](https://img.shields.io/badge/evidence--first-required-2f855a)
![fail-closed](https://img.shields.io/badge/policy-fail--closed-c53030)
![ci-gates](https://img.shields.io/badge/CI-gates--as--code-805ad5)

KFM’s credibility depends on one principle: **if you can’t trace it, you can’t claim it.**

This folder contains the **evidence-first test harness** that enforces KFM’s system guarantees:

- **Cite-or-abstain** for Focus Mode and narratives (abstention is a feature, not a bug).
- **Bounded evidence resolvability** (citations must resolve to evidence views or correctly deny).
- **Policy equivalence** between CI and runtime (same semantics + fixtures).
- **Fail-closed promotion** (no publish/promotion if proofs are missing).
- **Regression protection** against **sensitive-location leakage** and other governed constraints.

> [!IMPORTANT]
> Treat everything here as *governance-critical*. These tests are intended to be **merge-blocking** for any change that affects:
> data pipelines, catalogs (STAC/DCAT/PROV), evidence resolver, Focus Mode, or promotion workflows.

---

## What counts as “evidence” in KFM?

In KFM, “evidence” is not a bare URL. It is a **governed reference** to a verifiable artifact, typically one of:

- **Catalog objects:** STAC (`stac://...`), DCAT (`dcat://...`)
- **Lineage objects:** PROV bundles (`prov://...`), run receipts (`receipt://...` or `prov://...`)
- **Documents/media:** (`doc://...`) with rights + redaction controls
- **Graph facts:** (`graph://...`) that can be expanded to source-backed lineage
- *(Optional later)* **Digest bundles:** (`oci://...@sha256:...`) when using OCI evidence bundles

---

## Evidence resolver contract (minimum, enforceable)

The evidence resolver is the “truth doorway”: it turns a citation reference into a governed evidence view.

**Contract (implementable minimum):**
- Stable schemes: `prov://`, `stac://`, `dcat://`, `doc://`, `graph://` *(and later `oci://`)*  
- Endpoint shape (example): `GET /api/v1/evidence/resolve?ref=<scheme://...>`
- Returns:
  1) **human-readable** evidence view  
  2) **machine-readable** metadata  
  3) **access decision + redaction obligations** (deny-by-default when uncertain)

**Contract test requirement:**
- Every `citation.ref` produced by Focus Mode must:
  - resolve successfully **OR**
  - return a **correct** `403/404`
  - **without leaking sensitive metadata**
  - in **bounded calls** (keep it tight: e.g., ≤ 2 “hops” through resolvers)

---

## CI gates this folder supports

The integration blueprint defines a minimum “CI Gate Set” where each gate should map to a CI job or contract test. [oai_citation:2‡KFM-Bluprint-&-Ideas.pdf](sediment://file_000000004e9c71f598d3d784f6a13c46)

| Gate (fail closed) | What must be true | What we test here |
|---|---|---|
| Determinism | Same inputs + config → same outputs (within tolerance) | Golden fixtures + replay snapshots |
| Schema | Canonical schema validates; STAC/DCAT validate | Schema lint + STAC/DCAT validators |
| Governance labels | Sensitivity/sovereignty enums consistent across STAC/DCAT/PROV | Policy fixtures + crosswalk checks |
| Provenance | PROV emitted on PASS and FAIL; cross-links exist | PROV link checks + receipt presence |
| Supply chain | SBOM + signatures/attestations verified (if enabled) | Attestation presence + verify hooks |
| Quality | Thresholds pass (counts, coverage, index health) | QA report parsing + threshold assertions |
| Telemetry | Run lifecycle + freshness + artifact metrics emitted | Telemetry schema checks (if present) |
| Promotion | Promotion blocked unless all above pass | “promotion manifest” policy cases |
| Rollback | Failed promotion triggers atomic restore + PROV revert | Integration-style simulation fixture |

> [!NOTE]
> If your repo hasn’t implemented a given gate yet, this README still defines the *target contract*.
> The tests may begin as **expected-failure** (“xfail”) and graduate to merge-blocking as implementation lands.

---

## Directory layout

This suite is designed to stay **tooling-agnostic**: the same fixtures can be used by Python, Node/TS, or CI policy runners.

```text
tests/
  evidence/
    README.md                    # you are here
    fixtures/
      positive/                  # valid, promotable examples
      negative/                  # fail-closed examples (missing proofs, missing labels, etc.)
      leak_regression/           # "known leak fixtures" (sanitized) for sensitive-location tests
    contracts/
      evidence_resolver.*        # resolver contract tests (API-level)
      focus_output_schema.*      # schema tests for Focus/Story outputs (must cite or abstain)
    schemas/
      *.schema.json              # test-pinned schema versions (STAC/DCAT/PROV/run receipts/etc.)
    policies/
      *.rego                      # policy bundles used in tests (or pinned mirrors)
      testcases/                 # conftest inputs/expected outputs
    golden/
      spec_hash/                 # canonicalization + hashing golden vectors
      replay/                    # replay snapshots for determinism tests
    reports/
      .gitkeep                   # optional local output directory (do not commit generated artifacts)
```

---

## Test categories

### 1) Evidence resolver contract tests (`contracts/`)
**Goal:** prove that citations are *auditable*.

**Must assert:**
- `ref` resolves to evidence view *or* fails with correct `403/404`
- no sensitive metadata leakage in deny responses
- bounded resolution (no unbounded graph traversals)

> [!WARNING]
> “Cite” without resolvability is effectively **non-auditable**. This category is P0.

---

### 2) Policy regression + fail-closed tests (`policies/`)
**Goal:** governance is enforced by code.

Recommended fixture families:
- Missing required rights/license → deny promotion
- Missing sensitivity label on sensitive-adjacent artifacts → deny public promotion
- Consent-required artifacts: missing/expired consent → deny public lane, allow internal (policy-dependent)
- Trust membrane checks: no “shadow endpoints”; no direct store access

---

### 3) Sensitive-location “known leak fixtures” (`fixtures/leak_regression/`)
**Goal:** prevent regressions that could expose restricted locations.

Rules:
- **Never** include real restricted coordinates in fixtures.
- Use **synthetic geometries** or **deliberately generalized** geometries.
- Explicitly test that policy:
  - blocks publication when unsure
  - requires generalization/redaction before public exposure
  - produces policy-safe explanations (no leaks)

> [!DANGER]
> High reputational + safety risk if restricted locations leak. Maintain these fixtures like security exploits: small, surgical, and reviewed.

---

### 4) Determinism + hashing golden tests (`golden/`)
**Goal:** receipts + comparisons mean something over time.

Coverage should include:
- canonical serialization (e.g., JSON canonicalization strategy)
- stable hash vectors (input → expected hash)
- replay checks on 3–5 **anchor datasets** (thin slice strategy)

---

## How to add a new evidence fixture

1. **Choose fixture type**
   - `positive/` if it should pass gates and be promotable
   - `negative/` if it should fail-closed (missing proofs/labels/etc.)
   - `leak_regression/` if it tests sensitive leakage mitigation

2. **Keep fixtures minimal**
   - smallest geometry / smallest document excerpt / smallest catalog entry that proves the behavior
   - avoid adding large binaries unless absolutely necessary

3. **Attach governance metadata**
   - rights/license fields present and consistent
   - sensitivity + sovereignty labels as required
   - provenance references present (even for expected failures when applicable)

4. **Add/extend tests**
   - Contract tests for resolver behavior
   - Policy tests for deny reasons (stable, machine-readable)
   - Schema validation tests for all emitted artifacts

5. **Document the reason**
   - Add a short note in the fixture folder explaining:
     - what regression it prevents
     - what policy gate it asserts
     - what the expected outcome is

---

## Local execution (wire to your repo runner)

Because KFM can be polyglot, your repo should provide **one** canonical entrypoint (recommended):

```bash
# Example (recommended pattern — adjust to your repo)
make test-evidence
```

Fallback patterns (if applicable in your stack):

```bash
# Python
pytest -q tests/evidence

# Policy packs
conftest verify policies/
conftest test policies/ --all-namespaces
```

> [!NOTE]
> If these commands don’t exist yet, add the thinnest wrapper script that calls your real tools.
> The goal is: **one command** runs the whole evidence suite locally and in CI.

---

## Definition of Done for evidence-critical changes

A PR that touches **pipelines, catalogs, resolver, Focus/Story output, or promotion** is “done” only when:

- [ ] Evidence tests pass (or approved, time-bounded exception with governance sign-off)
- [ ] New/changed outputs are schema-valid (STAC/DCAT/PROV + receipts)
- [ ] Policy tests updated with regression fixtures (deny reasons remain stable)
- [ ] Resolver contract tests cover new schemes/fields/behaviors
- [ ] Sensitive-location leak tests updated when redaction/generalization logic changes
- [ ] Determinism/golden tests updated only when intentionally changing invariants (requires ADR)

---

## Governance and safety notes

- **Fail-closed defaults** are mandatory: when policy cannot prove allow, it must deny.
- Never include:
  - restricted site coordinates
  - private personal data
  - credentials, tokens, or secrets (even “fake” ones that look real)

> [!TIP]
> When you need realistic data shapes, prefer **synthetic fixtures** + **property-based tests**
> over copying real sensitive records.

---

## Related contracts and docs (recommended to link in-repo)

- `docs/quality/` — QA gates, graph QA, artifact promotion checks  
- `docs/patterns/` — determinism, receipts, provenance/attestations  
- `docs/standards/` — STAC/DCAT/PROV profiles + compatibility matrix  
- `docs/governance/` — policy packs, sensitivity handling, CARE/FAIR rules  
- `web/README.md` — Focus Mode / evidence drawer UI behavior (if present)

---

## Provenance

This README is aligned to the KFM integration blueprint posture:

- **CI gates map to tests** (merge-blocking)  
- **Evidence resolver contract tests** are P0  
- **Cite-or-abstain** requires **resolvable refs** + policy-safe abstentions  
- **Known leak fixtures** protect against sensitive-location regressions

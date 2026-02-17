<!--
tests/catalogs/README.md

KFM Governance Note:
This README describes *contract-style* tests that treat catalogs & provenance as first-class artifacts.
If your repo’s actual runners/tools differ, keep the *checks* the same and swap the runner.
-->

# 🧪 Catalog Conformance Tests (STAC / DCAT / PROV)

![Governed](https://img.shields.io/badge/Governed-Evidence--First-success)
![Policy](https://img.shields.io/badge/Policy-Fail--Closed-critical)
![Scope](https://img.shields.io/badge/Scope-Catalogs%20%26%20Provenance-informational)

KFM’s catalogs & provenance are the glue between pipelines and everything downstream (graph, API, map UI, Story Nodes, Focus Mode). This folder exists to **fail fast** when those artifacts are malformed, incomplete, not cross-linked, or policy-violating.

> [!IMPORTANT]
> These tests are designed to be **merge-blocking** (PR gate): if a catalog/provenance requirement is missing, the system should **fail closed** rather than publish ambiguous or unsafe outputs.

---

## What this suite validates

| Check family | What we assert | Why it matters |
|---|---|---|
| **Schema conformance** | STAC / DCAT / PROV artifacts are well-formed and conform to the project’s required fields & versions | Prevents “looks fine in UI” but non-interoperable / non-auditable artifacts |
| **Cross-link integrity** | DCAT ↔ STAC ↔ PROV references form a navigable chain (no orphan catalogs, no dead refs) | Guarantees evidence can be followed from UI/API back to sources |
| **Determinism (golden tests)** | Stable IDs + stable spec hashes across re-runs when inputs are unchanged | Eliminates “truth drift” from non-deterministic packaging/IDs |
| **Policy gates (fail closed)** | Missing license/rights/CARE/sensitivity labels, insecure URLs, or other governance violations are denied | Turns governance into machine-checkable rules (not prose) |
| **Link-check cleanliness** | All catalog links that must resolve are resolvable in bounded calls | “Cite” without resolvability is non-auditable |
| **Negative leak fixtures** | Known “leak patterns” (e.g., sensitive-location exposures) are rejected | Proves redaction/generalization rules actually block leakage |

---

## Directory layout

> [!NOTE]
> This layout is intentionally small and reviewable. Prefer adding **fixtures + a focused assertion** over sprawling integration harnesses.

```text
tests/catalogs/
├─ README.md
├─ fixtures/
│  ├─ dcat/
│  │  ├─ valid/
│  │  └─ invalid/
│  ├─ stac/
│  │  ├─ valid/
│  │  └─ invalid/
│  ├─ prov/
│  │  ├─ valid/
│  │  └─ invalid/
│  ├─ crosslinks/
│  │  ├─ valid/
│  │  └─ invalid/
│  └─ sensitive/
│     ├─ should_deny/
│     └─ should_allow/
├─ golden/
│  ├─ spec_hash/
│  └─ canonical_ids/
└─ helpers/
   ├─ README.md
   └─ (optional small helper scripts)
```

### Fixture philosophy

- **`valid/`** fixtures represent the *minimum acceptable* contract for KFM.
- **`invalid/`** fixtures should each fail for **one crisp reason** (one missing field, one broken ref, one disallowed URL, etc.).
- **`sensitive/should_deny/`** must use **synthetic/redacted** values that still exercise the policy.

---

## Running locally

This folder supports two complementary execution styles:

1) **Policy & schema gate runs** (fast, deterministic, merge-friendly)  
2) **Unit/contract tests** for cross-link + determinism logic (golden tests)

### Policy gate (Conftest / OPA)

If your repo uses a policy pack (recommended), run policy checks over fixture inputs:

```bash
# Example pattern (adjust paths to match your repo)
conftest test tests/catalogs/fixtures -p policy/opa
```

What this should cover:
- required fields (STAC/DCAT/PROV)
- license allowlists / required SPDX fields
- deny insecure `accessURL` schemes when prohibited
- sensitivity & CARE gates

### Unit/contract runner (pytest or equivalent)

If the repo uses pytest, run:

```bash
pytest -q tests/catalogs
```

If the repo uses a different runner:
- keep test *names* and *inputs* stable
- preserve the same “golden” fixtures
- preserve the same failure messages (or map them)

---

## Adding a new test case

### Add a new schema/shape rule (required field, constraint, etc.)

- [ ] Add a **valid** example that should pass
- [ ] Add an **invalid** example that fails for **exactly one** missing/invalid constraint
- [ ] Add/extend a **policy test** (e.g., `_test.rego`) if policy-as-code is the enforcement layer
- [ ] Ensure failure output is **actionable** (“missing field X”, “invalid enum Y”, “insecure URL scheme”)

### Add a new cross-link rule (DCAT ↔ STAC ↔ PROV)

- [ ] Add a `crosslinks/valid/…` fixture where the full chain is navigable
- [ ] Add an `crosslinks/invalid/…` fixture with **one broken reference**
- [ ] Ensure the test asserts “which hop broke” (DCAT→STAC, STAC→PROV, etc.)

### Add/extend determinism golden tests

- [ ] Add a “same inputs, same outputs” golden case for `spec_hash`
- [ ] Add a “stable ID” golden case for canonical IDs
- [ ] Ensure the test proves *stability across re-emits* (not just format correctness)

---

## Governance and safety rules for test data

> [!WARNING]
> Do **not** commit real restricted locations, private identifiers, or culturally restricted information into fixtures.
> Use synthetic/redacted fixtures that still trigger the governance logic.

**Recommended patterns:**
- Synthetic geometries (simple boxes / centroids) with labeled sensitivity
- “Known leak fixtures” that mimic the shape of risky outputs without revealing real sites
- “Deny on uncertainty”: if classification/sensitivity is ambiguous in the fixture, the expected outcome should be **deny**

---

## CI expectations (merge gate vs deploy gate)

A common safe pattern:

- **Merge gate (PR)**: schema conformance + policy gate + determinism checks + link-check + negative leak fixtures  
- **Deploy gate (env)**: integration checks against live services (tiles, search, API latency, etc.)

> [!TIP]
> Prefer making the merge gate *fast and strict* so reviewers see meaningful diffs and governance failures early.

---

## Troubleshooting guide

| Failure you see | Usually means | Fix |
|---|---|---|
| “missing required field …” | Catalog contract drift or incomplete writer | Add required field to catalog writer; update fixtures only if governance approved |
| “broken reference …” | Cross-link chain is not navigable | Fix link fields; ensure IDs/paths match deterministic packaging rules |
| “policy denied: …” | Governance requirement not met | Add license/rights/CARE/sensitivity label; or correct unsafe URL/field |
| “golden mismatch” | Determinism regression | Fix canonicalization/hashing; verify stable ordering and stable serialization |
| “link-check failed” | Evidence chain not resolvable | Fix link targets; ensure bounded resolver calls; avoid non-deterministic URLs |

---

## Definition of Done for changes touching catalogs

- [ ] New/updated catalog artifacts have **valid + invalid** fixtures
- [ ] Policy gate has at least one **deny** fixture for the new rule
- [ ] Cross-link chain is tested end-to-end (DCAT ↔ STAC ↔ PROV where applicable)
- [ ] Determinism golden tests cover any new IDs/hashes introduced
- [ ] No sensitive data in fixtures (synthetic/redacted only)

---

<details>
<summary><strong>Glossary</strong></summary>

- **STAC**: SpatioTemporal Asset Catalog (geospatial asset catalogs)
- **DCAT**: Data Catalog Vocabulary (dataset/distribution metadata)
- **PROV / PROV-O**: W3C provenance model (lineage of entities/activities/agents)
- **Fail closed**: deny-by-default; promotion only when required evidence is present & verified
- **Golden test**: deterministic expected output checked into repo to catch drift

</details>

# KFM Policy Pack (OPA/Rego) — `infra/policy/rego`

![Policy-as-Code](https://img.shields.io/badge/policy--as--code-Rego%20%2F%20OPA-blue)
![Fail-Closed](https://img.shields.io/badge/mode-fail--closed-critical)
![Default Deny](https://img.shields.io/badge/default-deny-critical)
![Explainable Gates](https://img.shields.io/badge/gates-explainable-success)
![Governed](https://img.shields.io/badge/KFM-governed%20%7C%20evidence--first%20%7C%20FAIR%2BCARE-6f42c1)

This directory is **KFM’s control-plane policy pack**: OPA/Rego modules used to enforce governance invariants (metadata completeness, licensing, sensitivity/CARE constraints, provenance/receipt requirements, and promotion rules) in a **deny-by-default** manner.

> [!IMPORTANT]
> **Default deny / fail-closed is the safety posture.**
> If required metadata, provenance, signatures/attestations, or governance labels are missing, the run/promotion should fail — not “warn.”  
> This is what keeps KFM auditable and safe.

---

## Table of contents

- [What this policy pack is for](#what-this-policy-pack-is-for)
- [Where policies execute](#where-policies-execute)
- [Policy scope](#policy-scope)
- [Directory layout](#directory-layout)
- [Policy input contracts](#policy-input-contracts)
- [Quickstart (local)](#quickstart-local)
- [Authoring rules](#authoring-rules)
- [Testing strategy](#testing-strategy)
- [CI integration and kill-switch](#ci-integration-and-kill-switch)
- [Governance workflow and exceptions](#governance-workflow-and-exceptions)
- [Design goals](#design-goals)
- [Related governed docs](#related-governed-docs)

---

## What this policy pack is for

KFM is a governed, evidence-first system: **data → pipeline → catalogs/provenance → governed APIs → UI/Focus Mode**.

Policies are used to enforce that:
- catalogs and lineage are **present** and **machine-checkable**
- sensitive and sovereignty constraints are **enforced as fields**, not prose
- promotion/publishing is **blocked** unless requirements pass
- deny output is **explainable** and remediation-oriented

---

## Where policies execute

Policies typically run at two choke points:

1) **CI / PR gates (Conftest)**  
   - Block merges when required invariants fail.
   - Used for catalog/receipt validation, promotion lane rules, and governance checks.

2) **Runtime policy boundary (OPA)** *(not confirmed in repo)*  
   - Enforce access decisions at API boundaries (“trust membrane”).
   - Apply output guardrails (e.g., Focus Mode “cite-or-abstain” and redaction policies).

> [!NOTE]
> If your repo only uses Conftest today, keep the same policy modules; you can later reuse them in an OPA sidecar/server with minimal changes.

---

## Policy scope

This policy pack is organized by **concern**, not by “team ownership.”

| Category | What it governs | Example checks |
|---|---|---|
| `catalogs/*` | STAC / DCAT / PROV minimal required fields | Required keys present; allowed values; consistent IDs |
| `common/*` | Shared helpers, allowlists, common predicates | SPDX allowlist; sensitivity helpers; reusable error formatting |
| `domains/*` | Domain QC rules (optional / additive) | Geometry sanity checks; temporal constraints; materiality thresholds |
| `promotion/*` *(optional)* | Promotion gates for “publish candidate” artifacts | CARE constraints; license gates; “internal vs public” rules |
| `focus/*` *(optional)* | Output guardrails | “cite-or-abstain”; remove/redact disallowed content |
| `tests/*` | Rego unit tests and golden fixtures | `_test.rego` + `samples/` pass/fail fixtures |

---

## Directory layout

Recommended structure (aligns to KFM integration pack patterns):

```text
infra/
  policy/
    rego/
      README.md              # <-- you are here
      bundles.rego           # optional: bundle entry/exports (not confirmed in repo)

      common/
        helpers.rego
        license_allowlist.rego

      catalogs/
        stac_required.rego
        dcat_required.rego
        prov_required.rego

      domains/
        # domain packs (examples; keep optional and additive)
        # dirt_geometry.rego
        # air_nowcast.rego
        # logistics_temporal.rego

      promotion/
        # promotion gate packs (optional)
        # promotion_manifest_required.rego
        # care_tribal_boundary_gate.rego

      focus/
        # Focus Mode output checks (optional)
        # cite_or_abstain.rego
        # output_redaction.rego

      tests/
        *_test.rego
        samples/
          stac/
          dcat/
          prov/
          receipts/
          promotion/
          focus/
```

---

## Policy input contracts

Policies expect **typed, minimal inputs** (JSON artifacts) produced by pipelines, catalogs, and promotion workflows.

### A) Catalog artifacts: STAC / DCAT / PROV

These rules validate “minimum viable governance” for metadata and lineage.

**Minimum provenance keys (KFM core profile)**
- `prov:wasGeneratedBy`
- `prov:used`
- `kfm:run_id`
- `kfm:artifact_digest`
- `kfm:attestation_uri`
- `kfm:source_license`
- `kfm:data_sensitivity`

> Keep the required set small; expand over time without breaking the thin slice.

### B) Run receipts / manifests

Receipts/manifests are the per-run “proof objects” that support:
- deterministic identity
- reproducibility checks
- supply-chain evidence attachment
- “what changed, why, and is it allowed to ship?”

### C) Promotion manifest (policy input)

Promotion manifests are evaluated before publish/promotion.  
Minimal fields commonly referenced by CARE/sensitivity gates:

- `artifact.labels`
- `artifact.provenance.facets[]`
- `artifact.spatial.intersects_authoritative_tribal_boundary` *(boolean)*
- `artifact.intended_exposure` *(e.g., `public` / `internal`)*
- `run.lane`

### D) Focus Mode output checks (optional but recommended)

Output policy should be able to deny answers that:
- omit citations (“cite-or-abstain”)
- include disallowed sensitive detail
- violate user permissions / access constraints

---

## Quickstart (local)

### Prereqs
- `opa` (Open Policy Agent CLI)
- `conftest` (for CI-parity evaluation)

### Run unit tests (Rego)

```bash
opa test infra/policy/rego -v
```

### Evaluate sample fixtures with Conftest

```bash
conftest test infra/policy/rego/tests/samples --policy infra/policy/rego
```

### Evaluate a specific artifact (example)

```bash
conftest test data/<domain>/stac/collections/<collection>.json --policy infra/policy/rego
```

> [!TIP]
> Prefer golden fixtures + unit tests over “manual evaluation.” Policy drift should be caught by CI.

---

## Authoring rules

### 1) Keep policies small and composable
- One file per concern.
- Use `common/helpers.rego` for shared predicates.
- Avoid giant “kitchen sink” policies that are hard to review.

### 2) Make denies explainable
Deny messages should point to:
- **what** is missing/violated
- **where** (path)
- **how to fix** (remediation)

Example deny style (illustrative):

```rego
package kfm.catalogs.stac_required

deny[msg] {
  input.type == "Feature"
  not input.properties["kfm:run_id"]
  msg := "STAC Item missing properties.kfm:run_id (required for provenance)"
}
```

### 3) Version the policy pack
Policies should be treated as **versioned, reviewed artifacts**.

*(Suggested default — not confirmed in repo)*:
- add `infra/policy/rego/VERSION`
- require receipts/manifests reference the policy version used

### 4) Avoid leaking sensitive data in denies/logs
- Deny messages should not echo sensitive payload values.
- Prefer structural messages (“missing field X”) over printing entire inputs.

---

## Testing strategy

### Unit tests
- Add `_test.rego` files for every policy module.
- Use golden fixtures:
  - `tests/samples/**/valid/*.json`
  - `tests/samples/**/invalid/*.json`

### What to test
- ✅ Required fields present
- ✅ Allowed values / allowlists (e.g., license allowlist)
- ✅ Fail-closed behavior (missing critical fields denies)
- ✅ CARE gate behavior (missing consent blocks public promotion)
- ✅ “Internal lane” vs “public lane” differences (if applicable)

**Definition of Done for policy changes**
- [ ] `opa test` passes
- [ ] Conftest evaluation passes on valid fixtures and fails on invalid fixtures
- [ ] Deny messages are human-readable and remediation-oriented
- [ ] Policy version bumped (if versioning is enabled)
- [ ] CI wiring updated if new bundles/paths were added

---

## CI integration and kill-switch

In KFM’s PR-first governance loop, policies are **merge-blocking**.

A kill-switch pattern is recommended so maintainers can immediately fail closed during incident response.

Example kill-switch (illustrative):

```bash
if [ -f .github/KILL_SWITCH ] || [ "${DEPLOY_KILL_SWITCH}" = "1" ]; then
  echo "KILL_SWITCH_ACTIVE"
  exit 1
fi
```

> [!WARNING]
> Treat tool/version updates (OPA/Conftest) as **governed changes**:
> pin versions, regression-test policies, and roll forward deliberately.

---

## Governance workflow and exceptions

KFM’s posture is “policy + people”:
- policies enforce machine-checkable invariants
- humans review exceptions and high-risk changes

**Exception rule**:
- Any exception/waiver should reference a governance ticket and be time-bounded.

### CARE example gate (tribal boundary intersections)
A reference pattern: block public exposure of data intersecting authoritative tribal boundaries unless:
1) `authority_to_control` label exists, **and**
2) a `tribal_consent` provenance facet exists (with valid scope + expiry)

---

## Design goals

1) **Fail closed**
2) **Explainable denies**
3) **Deterministic + reproducible**
4) **Versioned + auditable**
5) **Composable + testable**
6) **Safe-by-default (sensitivity/CARE)**

---

## Related governed docs

- KFM “Truth Path” / system boundaries (governed APIs + policy boundary; trust membrane)
- Integration pack patterns for policy-as-code PR gates and receipts/manifests
- CARE compliance gate patterns (authority-to-control + consent facets)
- Focus Mode “cite-or-abstain” / output filtering through policy (optional but recommended)

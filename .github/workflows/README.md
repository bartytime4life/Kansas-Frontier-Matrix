<div align="center">

# ⚙️ GitHub Workflows (CI/CD)

**KFM’s automated “trust pipeline” — policy-governed, provenance-first, and merge-safe.**  
`./.github/workflows/*`

<p>
  <a href="../../README.md"><img alt="Repo README" src="https://img.shields.io/badge/README-Repo-0b7285?style=for-the-badge"></a>
  <a href="../README.md"><img alt=".github README" src="https://img.shields.io/badge/.github-Docs-7950f2?style=for-the-badge"></a>
  <a href="../actions/README.md"><img alt="Actions README" src="https://img.shields.io/badge/Actions-Composite%20Blocks-0ca678?style=for-the-badge"></a>
  <a href="../ISSUE_TEMPLATE/README.md"><img alt="Issue templates README" src="https://img.shields.io/badge/Issue%20Templates-Intake%20Forms-f08c00?style=for-the-badge"></a>
</p>

</div>

---

## 🎯 Purpose

This folder defines **GitHub Actions workflows** that keep Kansas Frontier Matrix (KFM) contributions:

- ✅ **reproducible** (consistent builds & deterministic checks),
- 🧾 **traceable** (metadata + provenance expectations),
- 🛡️ **governed** (policy as code + safety rails),
- 🚦 **merge-safe** (fail-closed gates).

> [!IMPORTANT]
> KFM is designed to **fail closed**: when policy/permission/provenance is uncertain, the system blocks the change rather than letting it slip through. This is enforced by CI gates.  
> See: “fail closed” + CI enforcement concepts in the KFM blueprint and governance docs.[^fail_closed][^policy_as_code][^validation_gates]

---

## 🧭 Folder map

```text
.github/workflows/
├─ ♻️ reusables/            # reusable workflow_call building blocks
├─ 🚦 *.yml                 # entrypoint workflows (PR, release, schedule, manual)
└─ 📘 README.md             # you are here
```

### ♻️ What counts as a “reusable workflow”?
Reusable workflows live under `reusables/` and are called from entry workflows via `workflow_call`.  
They act like **macro building blocks**: “PR validation”, “policy gate”, “docker build”, etc.

---

## 🧠 CI design principles (KFM-specific)

KFM workflows are not just “lint + tests”. They exist to protect KFM’s core invariants:

### 1) 🧾 Provenance-first
Anything that is “published” or “user-facing” should carry traceability:
- metadata (STAC/DCAT where relevant),
- provenance logs (PROV-style lineage),
- and clear citations for narratives/stories.[^pipeline_order][^validation_gates]

### 2) 🧱 Policy as Code (OPA/Rego)
Governance rules should be **versioned** and **machine-enforced** — not tribal knowledge.
CI should execute policy checks (often via tools like `conftest`) and fail PRs on violations.[^policy_as_code]

### 3) 🚫 No bypass routes
Workflows should protect the system boundaries (example: UI shouldn’t “touch the DB” directly).  
In practice: enforce contract checks, schema validation, and controlled interfaces.[^pipeline_order]

### 4) ✅ “Green main” discipline
CI should keep the main branch in a continuously shippable state:
- tests pass,
- security checks pass,
- governance checks pass,
- documentation requirements are met.[^ci_testing]

---

## 🧩 How workflows relate to composite actions

Most jobs should be assembled from **composite actions** in:

- `../actions/` → see **`.github/actions/README.md`** for details.

Common action blocks (by intent) include:

- 🧪 `setup-conftest/` → policy testing setup
- 🛡️ `policy-gate/` → policy enforcement “allow/deny”
- 🧾 `provenance-guard/` + `pr-provenance/` → provenance completeness checks
- 🧾 `metadata-validate/` → metadata schema checks (dataset cards, STAC/DCAT, etc.)
- 🗺️ `story-lint/` → story node format + citation hygiene
- 🧰 `setup-kfm/` → repo toolchain bootstrap
- 🧱 `docker-build/` → build container images
- 🧾 `sbom/` + ✅ `attest/` → supply-chain artifacts (SBOM/attestation)

> [!TIP]
> Prefer reusing an existing composite action over duplicating shell steps across multiple workflows.
> It keeps CI consistent and makes governance easier to reason about.

---

## 🧬 Typical CI “truth path” (PR → merge)

```mermaid
flowchart TD
  PR[🔀 Pull Request] --> CI[🚦 Entrypoint Workflow(s)]
  CI --> LINT[🧹 Lint/Format]
  CI --> TEST[🧪 Unit/Integration Tests]
  CI --> META[🗂️ Metadata Validate]
  CI --> PROV[🧾 Provenance Guard]
  CI --> POL[🛡️ Policy Gate (OPA/Rego)]
  CI --> SBOM[📦 SBOM / Attestation (as needed)]
  LINT --> PASS[✅ Required checks green]
  TEST --> PASS
  META --> PASS
  PROV --> PASS
  POL --> PASS
  SBOM --> PASS
  PASS --> MERGE[🎉 Merge Allowed]
```

This mirrors the KFM philosophy: data & narratives should follow a governed pipeline, and CI is the automated enforcement layer.[^pipeline_order][^validation_gates]

---

## 🗃️ Workflow categories (recommended)

> [!NOTE]
> Workflow filenames may change as the repo evolves. The categories below are the **pattern** to maintain.

### 🔀 PR validation workflows
Run on `pull_request`:
- lint / formatting
- tests
- metadata validation
- provenance checks
- policy gate (fail closed)

### 🧷 Release workflows
Run on tag / release / main merges:
- build/publish docker images
- generate SBOM
- create attestations
- release notes automation (e.g., Release Drafter integration if configured)

### 🕰️ Scheduled governance + QA workflows
Run on `schedule`:
- catalog QA
- governance scan
- periodic policy regression checks
- dependency hygiene checks

### 🧑‍✈️ Manual workflows (`workflow_dispatch`)
Run on demand:
- rebuild catalog/index
- run a special validation suite
- re-run a heavier pipeline in CI context

---

## ♻️ Reusable workflows: conventions

### ✅ Naming
Use intent-first names:
- `pr-validate.yml`
- `policy-gate.yml`
- `metadata-validate.yml`
- `docker-build.yml`

### ✅ Inputs/outputs
Reusable workflows should:
- declare typed inputs,
- default to safe behavior,
- and expose outputs for downstream jobs (e.g., “image tag”, “artifact path”).

### ✅ Minimal permissions
Workflows should request only what they need:
- `contents: read` by default
- elevate selectively per job
- avoid broad `write-all`

---

## 🧪 Local debugging tips (fast iteration)

### Option A) Re-run jobs in GitHub UI
- Use “Re-run jobs” for failed runs.
- Add debug logs using `ACTIONS_STEP_DEBUG` (repo/org setting) when needed.

### Option B) Use `act` locally (best-effort parity)
You can dry-run many workflows locally with [`act`](https://github.com/nektos/act).  
It’s not perfect parity, but great for speeding up iteration on bash steps and composite actions.

Example:

```bash
# list workflows / jobs
act -l

# run a pull_request workflow (example)
act pull_request

# run a specific job
act -j <job_id>
```

> [!CAUTION]
> Some features (OIDC tokens, marketplace integrations, protected secrets) won’t behave the same locally.
> Treat `act` as a developer convenience, not a source of truth.

---

## 🛡️ Security + supply chain defaults (recommended)

- 🔒 Pin third-party actions by SHA (not floating tags) for stronger supply-chain safety.
- 🧾 Generate SBOM for releases (and optionally for PR builds).
- ✅ Use attestations for release artifacts if you publish containers/binaries.
- 🧯 Keep a “kill-switch” job path available to disable publication if governance flags trigger.
- 🧼 Never print secrets; use masked outputs and redact logs.

These align with KFM’s principle of auditable, governed operations.[^fail_closed][^policy_as_code]

---

## 🧯 When CI fails (how to fix fast)

### Common failure causes
- Missing dataset metadata / license field
- Missing provenance artifacts for new processed outputs
- Story nodes missing citations or template fields
- Governance policy violation (OPA/Rego / Conftest)
- Broken links or schema drift

### How to respond
1. Read the failing job summary.
2. Fix the underlying data/doc issue (not just the symptom).
3. Re-run only the necessary jobs.
4. If CI policy seems wrong, open a governance issue using the appropriate template:
   - `governance_form.yml`
   - `governance_question.yml`

---

## 🧾 Sources

[^fail_closed]: KFM governance principle: “fail closed” — CI blocks merges when checks fail; policy/permission uncertainty should deny by default. See the KFM blueprint (governance + CI enforcement sections).  
[^policy_as_code]: KFM describes governance as policy-as-code (OPA/Rego) with CI enforcement (e.g., Conftest running policies on PRs).  
[^pipeline_order]: KFM’s canonical pipeline order and separation of concerns are treated as non-negotiable invariants (ETL → catalog/provenance → DB/graph → API → UI/stories/AI).  
[^validation_gates]: KFM explicitly treats CI as a validation gate for provenance completeness, schema validation, security scanning, and governance compliance.  
[^ci_testing]: Reproducibility/QA guidance: CI should run tests and checks on PRs and require a green pipeline before merge.
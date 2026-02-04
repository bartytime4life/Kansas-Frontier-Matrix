# 🛠️ `.github/workflows/` — CI/CD + Governance Gates

This directory holds **GitHub Actions workflows** that keep Kansas Frontier Matrix (KFM) **CI-clean** ✅, **policy-compliant** 🛡️, and **provenance-first** 🧾.

KFM is designed as a **pipeline → catalog → database → API → UI** system where every artifact must remain traceable and governed end-to-end.  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 📁 What lives here

```text
.github/
  workflows/
    README.md   👈 you are here
    *.yml       🤖 GitHub Actions workflows (CI, policy, security, release, scheduled jobs)
```

> [!NOTE]
> Workflow filenames can vary by repo iteration. Use this README as the **responsibility map** for what each workflow _should_ cover, then keep it synced with the actual `.yml` files.

---

## 🧭 The non‑negotiables these workflows protect

KFM’s “must not regress” invariants are enforced through automated CI/CD gates:

- **Pipeline ordering is absolute**: ETL → Catalogs (STAC/DCAT/PROV) → Graph → API → UI → Story Nodes → Focus Mode.  [oai_citation:3‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- **API boundary rule**: the UI must never talk to the graph directly; access goes through the governed API layer.  [oai_citation:4‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- **Provenance first**: published data must be registered with provenance before graph/UI usage.  [oai_citation:5‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- **“Fail closed” security posture**: missing metadata / failed policy ⇒ block by default.  [oai_citation:6‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## ✅ CI gates (a.k.a. “definition of done” for merges)

These are the **core validation gates** the workflows should run on PRs and mainline pushes:

### 📘 Docs + Story validation
- **Markdown protocol & front‑matter checks** (YAML front-matter + required sections).  [oai_citation:7‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- **Link/reference validation** (no broken internal refs/citations).  [oai_citation:8‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 🗺️ Metadata integrity (STAC/DCAT/PROV)
- **JSON schema validation** for:
  - STAC Items/Collections
  - DCAT dataset entries
  - PROV bundles
  - Story Node schemas (where applicable)  [oai_citation:9‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 🕸️ Graph correctness
- **Graph integrity tests** against a fixture dataset (constraints, ontology expectations).  [oai_citation:10‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 🔌 API contract & schema tests
- **Contract tests** + OpenAPI/GraphQL schema linting to prevent accidental breaking changes.  [oai_citation:11‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 🔐 Security + governance scans
- **Secret scanning** (prevent keys/tokens in repo).  [oai_citation:12‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- **PII / sensitive data scanning** (catch accidental inclusion).  [oai_citation:13‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- **Sensitive location checks** (ensure protected coordinates aren’t leaking into public outputs).  [oai_citation:14‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- **Classification consistency** (no “downgrade” of sensitivity through processing without approved de-identification).  [oai_citation:15‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

> [!TIP]
> Only when these gates pass (or are explicitly waived by maintainers in special cases) should merges be allowed.  [oai_citation:16‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🛡️ Policy-as-Code (OPA/Rego) + CI enforcement

KFM governance is encoded as **policy-as-code** in the repo (typically under `policy/`), intended to be **machine-enforceable** and versioned like application code.  [oai_citation:17‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

**How it’s enforced in CI:**
- CI runs **Conftest** to evaluate Rego policies against PR changes.  [oai_citation:18‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- Typical “hard stop” failures include:
  - dataset metadata missing required fields (e.g., **license**)  
  - missing provenance artifacts (e.g., **PROV**)  
  - disallowed phrases/unsafe AI prompt content  [oai_citation:19‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:20‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🏃 Run the same checks locally (recommended)

Keeping CI fast means **you run the same gates before pushing**.

### 🐍 Backend (Python)
```bash
# run tests (containerized dev setup)
docker-compose exec api pytest
```
### ✨ Format / lint
```bash
# Python style gates (examples used in project docs)
black .            # or black --check .
flake8
```

### 🌐 Frontend (Node)
```bash
npm test
npm run lint -- --fix
```

### 🧾 Policy checks (Conftest)
```bash
conftest test .
# or narrow it down
conftest test data/processed/mydata.csv
```

These commands are explicitly called out as the expected local mirrors for CI in KFM docs.  [oai_citation:21‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 📦 Build, images, and release flow

### 🧱 Build + push (post-merge)
After merge to `main`, CI/CD may:
- build Docker images for the API (and optionally frontend)
- tag them (e.g., commit SHA)
- push to a registry  [oai_citation:22‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 🏷️ Releases (tagged)
At release time, KFM’s pipeline may also produce **signed artifacts**, including:
- **SBOMs**
- **provenance attestations**  [oai_citation:23‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

> [!IMPORTANT]
> Keep “release-time” steps (signing, SBOM generation) separate from “PR-time” steps unless PR verification explicitly requires it.  [oai_citation:24‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## ⏰ Scheduled workflows (maintenance + hygiene)

GitHub Actions scheduled workflows can be used for routine operations like:
- retraining models on a cadence
- clearing logs
- refreshing derived dashboards/outputs  [oai_citation:25‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 🔑 Secrets, permissions, and environments

KFM’s philosophy is governance-first and “fail closed.”  [oai_citation:26‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

Recommended GitHub Actions conventions:
- Use **least-privilege** workflow permissions (`permissions:` block) 🔒
- Prefer **GitHub Environments** for any deploy jobs (adds manual approvals + scoped secrets)
- Never print secrets; scrub logs; upload only sanitized artifacts

Example secrets you *might* need (repo-dependent):
- `GHCR_TOKEN` / registry credentials (if pushing images)
- cloud provider credentials (only if deploying)
- `SENTRY_AUTH_TOKEN` / telemetry tooling tokens (if used)

> [!NOTE]
> This README doesn’t assume a specific cloud provider; wire secrets to your actual deployment target.

---

## 🧩 Authoring workflow rules (recommended)

To keep workflows aligned with KFM architecture:

- ✅ **Use path filters** so data-only PRs don’t run full container builds (but still run metadata/policy checks).
- ✅ **Add concurrency** to cancel redundant PR runs.
- ✅ **Cache dependencies** (pip/npm) to keep CI fast.
- ✅ **Upload artifacts** (test reports, schema validation outputs) for debugging.
- ❌ Don’t add workflow steps that bypass the canonical pipeline (e.g., “publish UI artifact” without metadata/provenance gates).  [oai_citation:27‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:28‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🗺️ CI mental model (Mermaid)

```mermaid
flowchart TD
  PR[Pull Request / Push] --> A[Lint + Tests]
  A --> B[Policy-as-Code: Conftest/Rego]
  B --> C[Metadata: STAC/DCAT/PROV Schema Validation]
  C --> D[Docs/Links Validation]
  D --> E[Security Scans: Secrets/PII/Sensitive Locations]
  E --> F{All Gates Pass?}
  F -- No --> X[❌ Block Merge (Fail Closed)]
  F -- Yes --> M[✅ Merge Allowed]
  M --> R[Release/Deploy (optional)]
```

---

## 🧯 Troubleshooting (common CI failures)

<details>
<summary><strong>Click to expand</strong> 🔍</summary>

### ❌ “Style issues found”
- Python: run `black .` (or `black --check .`) + `flake8` locally.  [oai_citation:29‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- JS: run `npm run lint -- --fix`.  [oai_citation:30‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### ❌ “Dataset missing license / missing PROV / policy violation”
- Run `conftest test .` locally to reproduce.
- Fix metadata/provenance gaps (license fields, PROV bundles, required schema fields).  [oai_citation:31‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:32‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### ❌ “Broken links / unresolved references”
- CI checks docs + Story Node references; fix paths or update citations.  [oai_citation:33‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### ❌ “Classification consistency / sensitive location flagged”
- Ensure outputs are not less restricted than inputs and that protected coordinates are generalized/withheld.  [oai_citation:34‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

</details>

---

## 🔗 Related docs (worth reading 🧠)

- `docs/governance/ROOT_GOVERNANCE.md` (governance model)  [oai_citation:35‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- `docs/governance/ETHICS.md` (ethics policy)  [oai_citation:36‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- `docs/governance/SOVEREIGNTY.md` (sovereignty + sensitive data handling)  [oai_citation:37‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- KFM Master Guide v13 (Draft) — CI gates + invariants  [oai_citation:38‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:39‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- KFM Comprehensive Blueprint — policy-as-code + Conftest enforcement  [oai_citation:40‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

### ✅ README upkeep checklist

- [ ] When a new workflow `.yml` is added, update this README with what it enforces.
- [ ] If a CI gate is added/removed, update the “CI gates” section so contributors know the rules.
- [ ] Keep “policy checks” aligned with `policy/*.rego` changes (policy drift is a hidden foot-gun 🧨).
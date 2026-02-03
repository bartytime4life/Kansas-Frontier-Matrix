# 🧪🛡️ Policy Tests (KFM) — `tests/policy/`

![Policy as Code](https://img.shields.io/badge/Policy-as%20Code-brightgreen)
![OPA](https://img.shields.io/badge/OPA-Rego-blue)
![Conftest](https://img.shields.io/badge/Conftest-policy%20tests-yellow)
![Default Deny](https://img.shields.io/badge/Default-DENY-critical)
![Evidence First](https://img.shields.io/badge/AI-Evidence%E2%80%91First-informational)

**This folder documents and standardizes how we test KFM governance policies** (✅ CI gating + ✅ runtime enforcement).  
KFM treats governance as **versioned, testable code** — if policy fails, the system **fails closed** 🔒.

---

## 🎯 What these tests protect

KFM policy gates exist to enforce project invariants like:

- 🔍 **Provenance-first**: nothing ships without provenance/metadata
- 🧾 **Evidence-first AI**: AI answers must cite sources (no “black-box” claims)
- 🧑‍⚖️ **RBAC + sensitivity**: users can only access what their role allows
- 🧭 **Ethics & control**: sensitive/community-controlled data stays controlled
- 🧱 **Fail closed**: if the system can’t verify compliance, it **denies** by default

> [!IMPORTANT]
> Policy tests are not “nice-to-have.” They are a **hard quality gate** for merges and deployments.

---

## 🗺️ Repo map (recommended)

> Adjust paths if your repo differs — the core idea is stable: **policies live in `/policy`, tests live here**.

```text
📁 policy/                         # ✅ Source-of-truth Rego policies
   ├─ 🛡️ security.rego             # RBAC, access rules, redaction/masking decisions
   ├─ 🧾 ai_policies.rego           # citations, sensitive-output rules, prompt constraints
   ├─ 🧬 data_policies.rego         # metadata/provenance/license rules
   └─ ⚖️ compliance.rego            # privacy/ethics/community rules

📁 tests/
  └─ 📁 policy/
     ├─ 📄 README.md                # 👈 you are here
     ├─ 📁 fixtures/                # test inputs (json/yaml/md/etc.)
     │  ├─ 📁 ai/
     │  ├─ 📁 data/
     │  ├─ 📁 security/
     │  └─ 📁 compliance/
     └─ 📁 docs/                    # optional: screenshots/examples/explanations
```

---

## 🧰 Tools

We use two complementary testing approaches:

### 1) ✅ CI / repo-content checks (Conftest)
**Conftest** evaluates Rego policies against files in the repo (data, metadata, prompts, etc.).  
It’s ideal for “no bad changes can land” enforcement.

### 2) ✅ Runtime decision checks (OPA-compatible inputs)
At runtime the backend typically queries a policy engine (OPA sidecar or embedded OPA) with structured inputs like:

- `user.role`
- `resource.sensitivity`
- `answer.text` + `answer.citations`
- `request.context` (map viewport, dataset ID, etc.)

We test these as **fixtures** too, so policy behavior is stable and reviewable.

---

## ⚡ Quick start (run policy tests locally)

> [!NOTE]
> Run from repository root unless you know your repo is structured differently.

### Install Conftest
- Install via package manager (recommended), or from releases:
  - Conftest: https://www.conftest.dev/

### Run all policy tests against fixtures
```bash
conftest test ./tests/policy/fixtures -p ./policy
```

### Run only AI policy fixtures
```bash
conftest test ./tests/policy/fixtures/ai -p ./policy
```

### Get machine-readable output (great for CI)
```bash
conftest test ./tests/policy/fixtures -p ./policy -o json
```

---

## 🧩 Policy “shape” conventions

To keep policies predictable and testable, prefer **consistent input shapes**:

### ✅ Runtime-style input (recommended)
```json
{
  "user": { "id": "u123", "role": "PublicViewer", "groups": ["TribeABC"] },
  "resource": { "type": "dataset", "id": "ks_hydrology_1880", "sensitivity": "Public" },
  "request": { "action": "read", "context": { "bbox": [-100, 37, -99, 38], "year": 1935 } },
  "ai": { "answer": "…", "citations": ["[1]", "[2]"] }
}
```

### ✅ Policy outputs
- **`deny[msg]`** → hard fail (CI should block merges; runtime should block/403)
- **`warn[msg]`** → soft fail (CI can surface but not necessarily block)
- **`allow` / `allow_*`** → explicit permissions (runtime decisions)

---

## 🧾 Invariant tests we expect to exist (minimum set)

### 🧠 AI: citation enforcement (“No Source, No Answer”)
**Goal:** AI answers should include citations in the required bracket format.

**Fixture examples (create these):**
- ✅ `fixtures/ai/allow_answer_with_citations.json`
- ❌ `fixtures/ai/deny_answer_missing_citations.json`

**Minimal Rego pattern (illustrative):**
```rego
package kfm.ai

default allow_answer = false

allow_answer {
  re_match("\\[\\d+\\]", input.ai.answer)
}
```

> [!TIP]
> For CI, many teams prefer a `deny[msg]` rule so Conftest reports a human-friendly reason:
> ```rego
> deny[msg] {
>   not allow_answer
>   msg := "AI answer must contain at least one source citation like [1]"
> }
> ```

---

### 🧬 Data: license + provenance required
**Goal:** Datasets must not be publishable without license + provenance metadata.

**Fixture examples:**
- ✅ `fixtures/data/dataset_ok.json`
- ❌ `fixtures/data/dataset_missing_license.json`
- ❌ `fixtures/data/dataset_missing_prov.json`

**Common checks:**
- `metadata.license` exists and non-empty
- provenance reference exists (e.g., `prov_id`, `prov_path`, or `provenance` block)
- sensitivity label exists (`Public | Internal | Confidential | Restricted`)

---

### 🧑‍⚖️ Security: role-based access control (RBAC)
**Goal:** Requests are allowed/denied based on user role and resource sensitivity.

**Fixture examples:**
- ✅ `fixtures/security/public_viewer_public_dataset.json`
- ❌ `fixtures/security/public_viewer_confidential_dataset.json`
- ✅ `fixtures/security/admin_confidential_dataset.json`

**Rule-of-thumb mapping (example)**
| Sensitivity | Who can access |
|---|---|
| Public | PublicViewer, Contributor, Maintainer, Admin |
| Internal | Contributor+, Maintainer, Admin |
| Confidential | Maintainer, Admin (and explicit allowlist) |
| Restricted | Admin (and explicit allowlist / owner group) |

> [!IMPORTANT]
> This table is a **policy decision**, not a hard law — encode the official mapping in `security.rego` and test it here.

---

### ⚖️ Compliance: community-controlled + takedown-aware
**Goal:** If a dataset/story is tagged as community-controlled, withdrawn, or restricted to an owner group, policies enforce control.

**Fixture examples:**
- ✅ `fixtures/compliance/owner_group_member_allowed.json`
- ❌ `fixtures/compliance/non_member_denied.json`
- ❌ `fixtures/compliance/withdrawn_denied.json`

---

## ➕ Adding a new policy test (checklist)

- [ ] 🧠 Identify the invariant (what must always be true?)
- [ ] 📁 Add a fixture file under the right subfolder
- [ ] 🧾 Ensure the fixture matches the expected `input` shape
- [ ] 🧪 Run `conftest test` locally
- [ ] ✅ Confirm **good** fixtures pass and **bad** fixtures fail
- [ ] 🧹 Keep messages actionable (“what to fix”, not just “denied”)
- [ ] 🔁 Add/update fixtures when policy evolves (policy changes must be versioned)

---

## 🤖 CI integration (sample GitHub Actions step)

> Drop this into an existing workflow job (or create a new `policy.yml`).

```yaml
- name: Install Conftest
  run: |
    curl -L https://github.com/open-policy-agent/conftest/releases/latest/download/conftest_Linux_x86_64.tar.gz \
      | tar -xz
    sudo mv conftest /usr/local/bin/conftest

- name: Policy tests (Conftest)
  run: |
    conftest test ./tests/policy/fixtures -p ./policy
```

---

## 🧯 Troubleshooting

### “No policies found” / “package not found”
- Confirm `-p ./policy` points at the folder containing `.rego` files
- Confirm your `package ...` names match how you reference them

### “All tests failed suddenly”
- Check for an input schema change (fixture keys renamed)
- Run with JSON output for clearer debugging:
  ```bash
  conftest test ./tests/policy/fixtures -p ./policy -o json
  ```

### “Policy too strict / noisy”
- Convert some checks from `deny` → `warn`
- Add a single allowlisted exception **with explicit justification**, then test it

---

## 📚 Glossary

- **OPA**: Open Policy Agent — evaluates policies for allow/deny decisions
- **Rego**: Policy language used by OPA
- **Conftest**: Runs Rego policies against files for CI validation
- **Fail closed**: Default action is **deny** unless policy explicitly allows
- **RBAC**: Role-Based Access Control

---

## ✅ Final note

Policy tests are the **seatbelt** of KFM. If you’re unsure whether something needs a policy test:

> **If breaking it would harm trust, safety, provenance, or access control — it needs a policy test.** 🧷
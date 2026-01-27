# 🧾 `metadata-validate` — KFM Metadata Gatekeeper (Composite GitHub Action)

![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-Composite%20Action-2088FF?logo=githubactions&logoColor=white)
![CI Policy](https://img.shields.io/badge/CI-policy%20enforced-6f42c1)
![Metadata](https://img.shields.io/badge/metadata-STAC%20%7C%20DCAT%20%7C%20PROV-0b7285)

> [!IMPORTANT]
> In KFM, **data isn’t “published” unless its metadata + provenance exists**. This action is the CI gate that blocks PRs which add/modify datasets without the required **boundary artifacts** (STAC/DCAT/PROV) and baseline quality checks.

---

## ✨ What this action does

This local action validates that **datasets + metadata remain in sync** whenever a PR changes anything under `data/**` (or your configured data root).

It’s designed to be used in pull-request workflows as a **hard validation gate** so `main` stays “CI-clean” and contracts remain trustworthy.

---

## ✅ Validation coverage

Typical checks this action enforces (depending on what’s configured in `action.yml`):

### 📦 Presence checks (the “no orphan data” rule)
- [x] Every new/changed file in `data/processed/**` has matching metadata records
- [x] STAC (Item/Collection) exists for the dataset
- [x] DCAT dataset/distribution entry exists (JSON-LD or equivalent)
- [x] PROV lineage bundle exists (inputs → activities → outputs)

### 🧪 Format checks (fast & cheap)
- [x] JSON parses (STAC / PROV / GeoJSON / JSON-LD)
- [x] Common structural expectations (required keys present, non-empty strings)
- [x] Optional: link sanity checks (e.g., DCAT distribution ↔ STAC ↔ processed asset)
- [x] Optional: GeoJSON sanity (basic coordinate plausibility / bbox existence)

### 🛡️ Policy checks (governance rules)
- [x] Required fields like `license`, `description`, `keywords`, etc.
- [x] Provenance completeness expectations (raw inputs referenced, pipeline run info)
- [x] Optional: “sensitivity/classification” rules for restricted material

> [!TIP]
> The exact checks are intentionally **policy-driven** so governance rules can evolve without rewriting pipelines. See **Extending / modifying rules** below.

---

## 🧱 Expected repo layout

KFM typically follows this “data lifecycle” pattern:

```text
📁 data/
├─ 📁 raw/                 # immutable source snapshots
├─ 📁 work/                # intermediate artifacts (optional but recommended)
├─ 📁 processed/            # curated outputs served by the system
│  └─ 📁 <domain>/...
├─ 📁 stac/                 # STAC catalog (Collections + Items)
│  ├─ 📁 collections/
│  └─ 📁 items/
├─ 📁 catalog/              # discovery catalogs
│  └─ 📁 dcat/              # DCAT dataset entries (JSON-LD, etc.)
└─ 📁 prov/                 # lineage bundles (W3C PROV JSON, etc.)
```

If your repo uses different folder names (e.g., `data/provenance/` instead of `data/prov/`), this action should be configured via inputs (see below).

---

## 🚀 Usage in a workflow

Create or update a workflow like `.github/workflows/metadata.yml`:

```yaml
name: Metadata validation

on:
  pull_request:
    paths:
      - "data/**"
      - "policy/**"
      - ".github/actions/metadata-validate/**"

jobs:
  validate-metadata:
    runs-on: ubuntu-latest
    steps:
      - name: 🧾 Checkout
        uses: actions/checkout@v4
        with:
          fetch-depth: 0 # ✅ required if the action computes diffs

      - name: ✅ Validate metadata & provenance
        uses: ./.github/actions/metadata-validate
        with:
          # Keep these aligned with your repo layout.
          # (See Inputs section; action.yml is the source of truth.)
          data_root: data
          processed_dir: data/processed
          stac_dir: data/stac
          dcat_dir: data/catalog/dcat
          prov_dir: data/prov
          changed_only: true
          strict: true
```

---

## 🧩 Inputs

> [!NOTE]
> `action.yml` is the **source of truth**. If any input names differ in your implementation, update this table to match.

| Input | Type | Default | What it controls |
|------|------|---------|------------------|
| `data_root` | string | `data` | Root folder for data validation. |
| `processed_dir` | string | `data/processed` | Where curated outputs live (the “published datasets”). |
| `stac_dir` | string | `data/stac` | Where STAC Collections/Items are stored. |
| `dcat_dir` | string | `data/catalog/dcat` | Where DCAT dataset entries live (often JSON-LD). |
| `prov_dir` | string | `data/prov` | Where PROV lineage bundles live. |
| `policy_dir` | string | `policy` | Policy-as-code rules (Rego/Conftest, schemas, etc.). |
| `changed_only` | boolean | `true` | Validate only files changed in the PR (faster). |
| `strict` | boolean | `true` | Fail the job on warnings (recommended for PRs). |
| `report_format` | string | `step-summary` | Where validation results are written (e.g., job summary). |

---

## 📤 Outputs

This action typically fails the workflow when validation fails.

If your implementation also emits outputs (e.g., counts, report paths), document them here.

| Output | Description |
|--------|-------------|
| *(optional)* `report_path` | Path to a generated validation report artifact. |
| *(optional)* `violations` | Count of violations detected. |

---

## 🧪 Run locally (recommended before pushing)

If your repo uses **OPA/Conftest** policies, you can test locally to mirror CI:

```bash
# Validate everything using repo policies
conftest test .

# Validate just a specific dataset (fast iteration)
conftest test data/processed/<domain>/<file>
```

If your validator is a script (Python/Node), document the local command here as well, for example:

```bash
# Example (adjust to your repo)
python .github/actions/metadata-validate/scripts/validate.py --changed-only
```

---

## 🧰 Extending / modifying rules

### 1) Update KFM profiles (contracts-first ✅)
These files define project standards and are the basis for schema + policy checks:

- 📘 `docs/standards/KFM_STAC_PROFILE.md`
- 📘 `docs/standards/KFM_DCAT_PROFILE.md`
- 📘 `docs/standards/KFM_PROV_PROFILE.md`

From this README’s folder, those are typically at:

- `../../../docs/standards/KFM_STAC_PROFILE.md`
- `../../../docs/standards/KFM_DCAT_PROFILE.md`
- `../../../docs/standards/KFM_PROV_PROFILE.md`

### 2) Update policies
Common pattern:

```text
📁 policy/
├─ 🧾 metadata/         # Rego rules (or equivalent)
├─ 🧪 schemas/          # JSON Schemas (optional)
└─ 🔐 security/         # secrets/leak checks, etc.
```

### 3) Keep action behavior documented
Whenever you change enforcement rules, update:
- `action.yml` (implementation) ✅
- `README.md` (this doc) ✅

---

## 🛠️ Troubleshooting

<details>
<summary><strong>❌ “Dataset missing license” / “missing required field”</strong></summary>

- Add `license` to the dataset metadata record(s) (STAC/DCAT).
- Ensure license is valid per KFM policy (e.g., a known SPDX or project-approved value).
</details>

<details>
<summary><strong>❌ “Missing PROV bundle / provenance file not found”</strong></summary>

- Ensure every `data/processed/**` output has a corresponding PROV file under `data/prov/**` (or configured directory).
- The PROV should reference:
  - raw source entities
  - the pipeline activity (script + version/commit)
  - the output entity path
</details>

<details>
<summary><strong>❌ “STAC/DCAT link mismatch”</strong></summary>

- Check that STAC `assets`/`links` point to the correct processed file path.
- Check that DCAT distribution references STAC or the dataset asset consistently.
</details>

<details>
<summary><strong>❌ “Invalid GeoJSON / JSON parse error”</strong></summary>

- Validate JSON locally (jq is handy): `jq . <file>`
- Confirm geometry structure and that files are not truncated.
</details>

---

## 🧭 Related docs (quick links)

- 🧩 Action definition: `./action.yml`
- 🧱 Policies: `../../../policy/`
- 📚 Standards:
  - `../../../docs/standards/KFM_STAC_PROFILE.md`
  - `../../../docs/standards/KFM_DCAT_PROFILE.md`
  - `../../../docs/standards/KFM_PROV_PROFILE.md`
- 🗺️ Master guide: `../../../docs/MASTER_GUIDE_v13.md` *(if present)*

---

## 🧠 Design intent (why we’re strict)

> [!IMPORTANT]
> KFM treats metadata + provenance as **first-class artifacts**. If a dataset can’t be traced and licensed, it can’t be trusted — and it shouldn’t ship.

This action is the practical enforcement point for that philosophy. 🔒✅

# 🧰 `tools/bin` — KFM Command-Line Utilities

![Governed](https://img.shields.io/badge/Governed-yes-2ea44f)
![Evidence-first](https://img.shields.io/badge/Evidence--first-cite%20or%20abstain-blue)
![Trust%20Membrane](https://img.shields.io/badge/Trust%20Membrane-enforced-important)
![FAIR%2BCARE](https://img.shields.io/badge/FAIR%2BCARE-aligned-success)

Repo-local **command-line tools** used to operate and validate Kansas Frontier Matrix (KFM) workflows: **ingest → validate → transform → catalog/provenance → serve**.

> [!IMPORTANT]
> These tools are **governed entrypoints**. They exist to *prevent* ad-hoc, uncited, un-auditable operations.
> If a workflow cannot produce machine-checkable artifacts (validation reports, catalogs, provenance/receipts),
> it does **not** belong here.

---

## 📌 Why this folder exists

A `/bin` directory conventionally holds **command-line scripts** and executables. In KFM, `tools/bin` is where we keep **repeatable operational utilities** that support the platform’s “Truth Path”:

1) **Acquire** (ingest / capture)  
2) **Validate** (schema, geometry, QA gates)  
3) **Enrich** (normalization, linking, classification)  
4) **Catalog** (DCAT / STAC / PROV + license + sensitivity)  
5) **Serve** (governed APIs + exports)  
6) **Explain** (Focus Mode / Story Nodes that cite or abstain)

---

## ✅ Non-negotiables (governance + architecture)

> [!WARNING]
> Tools in this directory must not create “shadow pipelines” or bypass governance.

### Trust membrane alignment
- The **UI/external clients never talk to databases directly**.
- Operational tools must **not** encourage manual DB access from developer laptops for production-like tasks.
- Where a tool needs data access, it should do so via the **governed backend runtime** (use-case/service layer + repository interfaces), or through **explicitly governed pipeline storage zones**.

### Evidence-first behavior
- Anything that could affect a user-visible claim must be traceable to:
  - a **dataset version**, and
  - the **exact records/assets used**, and
  - a **provenance chain** (inputs → transformation → outputs).

### Promotion gates (Raw → Work → Processed)
If a tool participates in dataset lifecycle operations, it must preserve these invariants:

- **Raw**: immutable, append-only capture; no transforms.
- **Work**: repeatable transforms + QA staging.
- **Processed**: query-ready; exposed via API; catalogs + provenance required.

Promotion should only happen when:
- checksums/manifests exist,
- validations pass,
- policy labels exist,
- catalog writers succeed (DCAT/STAC/PROV),
- contract/API checks relevant to the dataset pass.

---

## 🚀 Running tools

### Discover what exists
```bash
ls -la tools/bin
```

### Run a tool
```bash
./tools/bin/<tool> --help
```

### If a tool is not executable
```bash
chmod +x tools/bin/<tool>
```

> [!NOTE]
> Prefer running tools in a **reproducible environment** (CI runner / container / dev shell) when available.
> (Exact orchestration commands depend on the repo’s runtime setup.)

---

## 📒 Tool registry (update on every new tool)

<details>
<summary><strong>Open registry table</strong></summary>

| Tool | Purpose | Typical inputs | Outputs / artifacts | Writes? | Governance notes |
|---|---|---|---|---:|---|
| *(add tool here)* | *(what it does)* | dataset_id / paths / config | validation report / catalogs / receipt | ✅/❌ | policy labels, license handling, cite-or-abstain |
| *(add tool here)* |  |  |  |  |  |

</details>

> [!TIP]
> A PR that adds a tool should also update this table so operators can discover it without spelunking.

---

## 🧾 Run receipts & provenance (required for meaningful tools)

Any tool that changes state (writes files, promotes datasets, builds catalogs, reindexes, etc.) should emit a **run receipt** (JSON) describing:

- tool name + version (or git commit)
- timestamp(s)
- inputs + content hashes (where applicable)
- outputs (paths, IDs, checksums)
- policy labels / sensitivity class
- provenance link(s) (PROV activity/entity IDs)

Example receipt shape (illustrative):

```json
{
  "tool": "kfm-<name>",
  "started_at": "2026-02-16T18:40:00Z",
  "finished_at": "2026-02-16T18:41:12Z",
  "git": { "commit": "abc1234", "dirty": false },
  "inputs": [
    { "path": "raw/<dataset>/...", "sha256": "..." }
  ],
  "outputs": [
    { "path": "processed/<dataset>/...", "sha256": "..." }
  ],
  "policy": {
    "labels": ["public|restricted|sensitive-location"],
    "license": "SPDX-or-text"
  },
  "prov": {
    "activity_id": "prov:activity:...",
    "entities": ["prov:entity:..."]
  }
}
```

---

## 🧩 What belongs here (and what does not)

### ✅ Belongs in `tools/bin`
- Repeatable operational utilities:
  - validation runners (schema/geometry/time-range/license checks)
  - catalog builders (DCAT/STAC/PROV)
  - dataset promotion helpers (Raw → Work → Processed) **with gates**
  - index rebuilders (search/graph) **with receipts**
  - CI smoke checks (contract/regression checks) that enforce invariants

### ❌ Does NOT belong in `tools/bin`
- One-off personal scripts with no receipts, no provenance, no tests
- Tools that “just update the DB” without:
  - catalog updates
  - provenance/receipt output
  - policy labels
- Anything that requires copying secrets into files or the repo

---

## 🛠️ Adding a new tool

> [!IMPORTANT]
> New tools are production-affecting surface area. Treat them like API changes.

### Naming
- Prefer: `kfm-<verb>-<noun>` (e.g., `kfm-validate-dataset`, `kfm-build-catalogs`)
- Keep names explicit; avoid ambiguous “do-stuff” scripts.

### Definition of Done (DoD)
- [ ] `--help` documents usage, inputs, outputs, and side effects
- [ ] Defaults are safe (prefer `--dry-run` or explicit `--apply`)
- [ ] Emits a **run receipt** for stateful operations
- [ ] Produces/updates catalogs & provenance when required
- [ ] Enforces promotion gates (if it promotes)
- [ ] Does not bypass clean architecture boundaries:
  - CLI entrypoint → use-case/service → interfaces → infra adapters
- [ ] Has at least minimal tests (unit/contract/CI gate as appropriate)
- [ ] Updates the **Tool registry** table in this README

---

## 🧭 Directory layout

```text
tools/
└── bin/
    ├── README.md
    ├── <tool-1>
    ├── <tool-2>
    └── ...
```

---

## 📚 Design basis (why these rules exist)

- **KFM Masterpiece Vision** (Generated 2026-02-16): governance-first platform, trust membrane, validation & provenance expectations.
- **KFM Data Source Integration Blueprint v1.0** (2026-02-12): clean layers + trust membrane mechanics; dataset zones; promotion gates; DCAT/STAC/PROV requirements.
- **KFM Blueprint & Ideas**: thin-slice governed delivery and “validators + provenance receipts + tooling” emphasis.

> [!NOTE]
> This README is intentionally stricter than a typical tools folder because KFM treats governance
> as architecture—not a best-effort process.
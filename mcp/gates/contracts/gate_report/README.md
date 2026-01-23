> According to a document from **2026-01-22**, KFM governance relies on **policy gates (OPA + Conftest)**, **provenance-first publishing**, and **deterministic run manifests**. This contract standardizes the one artifact every gate emits: a **GateReport** 🧾✅

# 🧾 Gate Report Contract (`GateReport`)

![Status](https://img.shields.io/badge/status-draft-orange)
![Contract](https://img.shields.io/badge/contract-gate__report-blue)
![Format](https://img.shields.io/badge/format-JSON-0b7285)
![API](https://img.shields.io/badge/api-mcp.gates%2Fv1alpha1-6f42c1)
![Governance](https://img.shields.io/badge/governance-policy__gates%20%2B%20auditability-228be6)

A **GateReport** is the **canonical, machine-readable audit record** produced by any “gate” in the MCP/KFM ecosystem—data intake checks, policy enforcement, security scanning, provenance validation, AI safety checks, simulation promotion checks, etc. 🧠🛡️🧾

It’s designed to be:
- **Human-friendly** enough for PR reviews and UI surfacing 👀
- **Machine-friendly** enough for CI merge gates, dashboards, and governance ledgers 🤖
- **Evidence-first** by default (hashes + references over raw sensitive content) 🔍

---

## 📦 Location

```text
📦 mcp/
 └─ 🚦 gates/
    └─ 📜 contracts/
       └─ 🧾 gate_report/
          └─ README.md   ← you are here ✅
```

> 💡 Typical next files (recommended):
>
> ```text
> 🧾 gate_report/
>  ├─ gate_report.schema.json          # JSON Schema (authoritative validation)
>  └─ examples/
>     ├─ pass.minimal.json
>     ├─ fail.missing_prov.json
>     └─ warn.sensitivity_review.json
> ```

---

## 🧭 Why this contract exists

KFM is built around **contract-first interfaces**, **policy enforcement**, **provenance + lineage**, and **auditable automation**. Gates are the enforcement points; **GateReport** is the standardized output that makes those gates:
- **inspectable** ✅
- **reproducible** ♻️
- **traceable** 🧬
- **reviewable** 🧑‍⚖️
- **automatable** 🤖

GateReport is intentionally compatible with:
- **OPA/Conftest “deny/warn” results** 🧱
- **Watcher–Planner–Executor (W-P-E)** event/PR workflows 👁️➡️🧠➡️🛠️
- **Run manifests** (idempotency, canonical hashing, tool versions) 🧾🔒
- **UI trust indicators** (e.g., “provenance enforced” badge) 🏷️

---

## 🧩 Where GateReport fits

```mermaid
flowchart TD
  A[CI / Watcher / Runtime Trigger] --> B[Gate Runner]
  B --> C[GateReport.json 🧾]
  C --> D[Merge / Promotion Decision ✅❌]
  C --> E[Governance Ledger (append-only) 🧾🔏]
  C --> F[UI Badges + Trust Panels 🏷️]
  C --> G[Graph/PROV Links (Neo4j / PROV-O) 🧬]
```

---

## ✅ Contract principles (normative)

> **MUST / SHOULD** are used in the RFC sense.

1. **Fail-closed by default** 🔒  
   If the gate cannot conclusively pass (errors, missing evidence, policy engine failure), the GateReport **MUST** indicate `fail` or `error`, and downstream systems **MUST** treat it as blocking unless explicitly configured otherwise.

2. **Evidence-first** 🔍  
   GateReport **SHOULD** reference evidence via URIs/paths + cryptographic digests and keep raw sensitive content out of the report.

3. **Deterministic & idempotent-friendly** ♻️  
   GateReport **SHOULD** support canonicalization + hashing so identical inputs produce identical identities/digests.

4. **Portable across domains** 🌍  
   A GateReport produced for a geospatial ingest, a simulation run, a PR policy check, or an AI response check should share the same envelope.

5. **UI-ready** 🧭  
   GateReport **SHOULD** include short summaries and remediation hints suitable for UI/PR comments.

---

## 🧱 Contract at a glance

### Top-level shape (summary)

```json
{
  "api_version": "mcp.gates/v1alpha1",
  "kind": "GateReport",
  "metadata": { },
  "gate": { },
  "subject": { },
  "decision": { },
  "checks": [ ],
  "artifacts": [ ],
  "policy": { },
  "provenance": { },
  "signatures": [ ]
}
```

---

## 🧾 Field reference

### 1) `api_version` (required)
- **Type:** string
- **Example:** `"mcp.gates/v1alpha1"`
- **Meaning:** Version of this GateReport contract.

### 2) `kind` (required)
- **Type:** string
- **Value:** `"GateReport"`

### 3) `metadata` (required)
Core envelope metadata.

**Recommended fields**
- `report_id` (string): stable unique id (UUID or digest-based)
- `created_at` (string, ISO 8601): report creation timestamp
- `producer` (object):
  - `name` (string): runner name (`kfm-ci`, `kfm-wpe-executor`, etc.)
  - `version` (string): producer version
  - `environment` (object): optional runtime details (container image digest, OS, etc.)
- `labels` (object): freeform tags (domain, dataset family, environment)
- `canonical_digest` (object): optional
  - `algo` (string): e.g., `"sha256"`
  - `value` (string): digest of canonicalized report payload
- `idempotency_key` (string): optional (often equals digest)

> 🔧 **Digest tip:** Canonicalize JSON (e.g., RFC 8785) before hashing so everyone gets the same digest.

### 4) `gate` (required)
Describes the gate that produced the report.

**Fields**
- `gate_id` (string): stable ID, e.g. `kfm.prov.provenance_first`
- `gate_name` (string): human name, e.g. `"Provenance First Publishing"`
- `gate_version` (string): semver, e.g. `"1.3.0"`
- `gate_type` (string): recommended enum  
  `policy | validation | security | provenance | quality | ai | simulation | supply_chain | ui | graph`
- `scope` (string): recommended enum  
  `ci | runtime | batch | interactive`

### 5) `subject` (required)
What the gate evaluated.

**Fields**
- `subject_type` (string): recommended enum  
  `dataset | stac_item | dcat_dataset | prov_activity | pipeline_run | pull_request | artifact | ai_answer | simulation_run`
- `subject_id` (string): canonical ID (KFM ID, URN, GitHub PR ref, etc.)
- `uri` (string): optional pointer (repo path, storage URL, API URL)
- `digest` (object): optional
  - `algo` (string): `"sha256"`
  - `value` (string)

### 6) `decision` (required)
The gate’s overall outcome.

**Fields**
- `status` (string, required):  
  `pass | warn | fail | error | skip`
- `severity` (string):  
  `info | low | medium | high | critical`
- `summary` (string): short human message
- `fail_closed` (boolean): recommended default `true`
- `recommendation` (string): next step (fix metadata, request review, etc.)

> ⚠️ **Rule of thumb:** `error` means the gate couldn’t run reliably; downstream should treat it like `fail` unless explicitly overridden.

### 7) `checks` (required)
An array of granular checks (OPA rules, validators, scanners, heuristics).

**Each check**
- `check_id` (string): e.g. `KFM-PROV-001`
- `title` (string)
- `status` (string): `pass | warn | fail | error | skip`
- `severity` (string): `info | low | medium | high | critical`
- `message` (string): what happened
- `location` (object): optional
  - `path` (string): repo/file path
  - `line_start` / `line_end` (int)
- `evidence` (array): optional evidence references
- `remediation` (object): optional
  - `steps` (array of strings)
  - `owner` (string): `contributor | maintainer | wpe_agent`
  - `docs_ref` (string): internal doc path or anchor

### 8) `artifacts` (optional)
Outputs produced by the gate (reports, SBOMs, attestation files, diffs).

**Artifact**
- `name` (string): e.g. `"run_manifest.json"`, `"sbom.spdx.json"`
- `artifact_type` (string): `manifest | sbom | attestation | log | diff | bundle | report`
- `uri` (string): where it lives
- `digest` (object): `{ "algo": "sha256", "value": "…" }`
- `media_type` (string): e.g. `application/json`
- `generated_by` (string): tool name or gate runner id

### 9) `policy` (optional but recommended for policy gates)
OPA/Conftest or other policy-engine metadata.

**Fields**
- `engine` (string): e.g. `opa/conftest`
- `bundle_digest` (object): digest of the policy pack/bundle
- `rules_evaluated` (array): optional list of rule ids
- `decision_id` (string): optional policy decision trace id

### 10) `provenance` (optional but strongly recommended)
Linkage to PROV/STAC/DCAT and/or governance ledger entries.

**Fields**
- `prov_ref` (string): e.g. path/URI to PROV JSON-LD
- `stac_ref` (string): path/URI to STAC item/collection
- `dcat_ref` (string): path/URI to DCAT dataset record
- `ledger_entry_ref` (string): pointer to append-only governance ledger entry

### 11) `signatures` (optional)
Cryptographic signatures for the report and/or its artifacts.

**Fields**
- `signature_type` (string): `cosign | gpg | x509`
- `signed_at` (string, ISO 8601)
- `key_id` (string): optional key reference
- `signature` (string): base64 or envelope reference
- `transparency_log_ref` (string): optional (e.g., Rekor entry id)

---

## 🧪 Status semantics

| Status | Meaning | Typical action |
|---|---|---|
| `pass` ✅ | All required checks passed | Merge / promote |
| `warn` ⚠️ | Non-blocking issues | Merge w/ follow-up or require review |
| `fail` ❌ | Blocking violations | Fix before merge/promotion |
| `error` 🧯 | Gate couldn’t run reliably | Treat as fail (fail-closed) |
| `skip` ⏭️ | Gate not applicable | Document why |

---

## 🔍 Evidence patterns (recommended)

Evidence objects in checks should avoid leaking sensitive info and support audits.

**Common evidence types**
- `file_ref` (repo path + digest)
- `uri_ref` (URL + digest)
- `query_ref` (query text + digest of result snapshot)
- `log_ref` (NDJSON segment hash)
- `attestation_ref` (SLSA provenance)
- `sbom_ref` (SPDX document)

> 🧼 Redaction: If evidence contains sensitive content, store **only a hash + redacted snippet** in the GateReport.

---

## 🧷 Relationship to Run Manifest (strongly recommended)

In KFM patterns, **each pipeline run** emits a run manifest capturing:
- `run_id`, `run_time`
- `idempotency_key`
- `canonical_digest`
- `tool_versions`
- `source_urls`, outputs, summary counts

GateReport should reference that run manifest via `artifacts[]` and/or `provenance.ledger_entry_ref` rather than duplicating the entire run description.

---

## 🧭 Storage & discovery conventions

**Recommended canonical locations**
- `data/audits/<run_id>/gates/<gate_id>.gate_report.json`
- CI artifacts: attach GateReport(s) to PR checks
- Governance: append GateReport digest + decision to a signed ledger entry

**Recommended filename rules**
- Use stable `gate_id` in filenames
- Avoid spaces
- Prefer deterministic paths so tooling can auto-discover gate outputs

---

## 🧩 Common gate families (examples)

These aren’t required by the contract, but help standardize gate ids and expectations:

- 🧾 **Provenance / lineage**
  - “Processed data changed without matching PROV update”
  - “STAC item missing PROV cross-link”
- 🧱 **Policy pack (OPA/Conftest)**
  - “No dataset without license field”
  - “AI outputs must include citations”
  - “Sensitive datasets require review flag”
- 🗺️ **Geospatial validity**
  - Geometry validity checks (e.g., invalid polygons)
  - CRS/axis order requirements (WGS84 where required by STAC conventions)
- 🧠 **AI safety & quality**
  - Prompt injection defenses (“prompt gate”)
  - Citation requirements
  - Bias/drift monitoring hooks
- 🔐 **Supply chain**
  - SBOM present for release
  - SLSA attestation for automation PRs
  - Artifact signature verification
- 🧪 **Simulation promotion**
  - Sandbox vs promotion invariants
  - Reproducibility checklist (pinned inputs, parameters, environment, seeds)

---

## 🧾 Examples

### Example A — minimal PASS ✅

```json
{
  "api_version": "mcp.gates/v1alpha1",
  "kind": "GateReport",
  "metadata": {
    "report_id": "2edc8a67-2c6f-4c15-a0f7-61d5f7467d8b",
    "created_at": "2026-01-22T23:10:00Z",
    "producer": { "name": "kfm-ci", "version": "0.8.0" },
    "labels": { "env": "ci", "domain": "data_intake" }
  },
  "gate": {
    "gate_id": "kfm.policy.pack",
    "gate_name": "Policy Pack Evaluation",
    "gate_version": "1.0.0",
    "gate_type": "policy",
    "scope": "ci"
  },
  "subject": {
    "subject_type": "pull_request",
    "subject_id": "github:pr:1234"
  },
  "decision": {
    "status": "pass",
    "severity": "info",
    "summary": "All policy checks passed.",
    "fail_closed": true
  },
  "checks": []
}
```

---

### Example B — FAIL due to provenance-first publishing ❌🧬

```json
{
  "api_version": "mcp.gates/v1alpha1",
  "kind": "GateReport",
  "metadata": {
    "report_id": "sha256:5afc1bd1d7c1cf1c6dbfd3e1c2b2c5c96e67d53f5eaf5a6d57b7d1c0e2d3a4b5",
    "created_at": "2026-01-22T23:12:41Z",
    "producer": { "name": "kfm-ci", "version": "0.8.0" },
    "labels": { "env": "ci", "domain": "governance" }
  },
  "gate": {
    "gate_id": "kfm.prov.provenance_first",
    "gate_name": "Provenance-First Publishing",
    "gate_version": "1.2.0",
    "gate_type": "provenance",
    "scope": "ci"
  },
  "subject": {
    "subject_type": "pull_request",
    "subject_id": "github:pr:1235"
  },
  "decision": {
    "status": "fail",
    "severity": "high",
    "summary": "Processed data changed without matching PROV update.",
    "fail_closed": true,
    "recommendation": "Add/Update data/prov/* records for every processed output touched."
  },
  "checks": [
    {
      "check_id": "KFM-PROV-001",
      "title": "Processed outputs require matching PROV artifacts",
      "status": "fail",
      "severity": "high",
      "message": "data/processed/foo.csv changed but no corresponding data/prov/foo_prov.json was added/updated.",
      "location": { "path": "data/processed/foo.csv" },
      "evidence": [
        {
          "evidence_type": "file_ref",
          "path": "data/processed/foo.csv",
          "digest": { "algo": "sha256", "value": "REDACTED_EXAMPLE" }
        }
      ],
      "remediation": {
        "steps": [
          "Generate PROV JSON-LD for the pipeline run that produced foo.csv.",
          "Add data/prov/foo_prov.json and cross-link it from STAC/DCAT as required."
        ],
        "owner": "contributor",
        "docs_ref": "docs/guides/provenance/README.md"
      }
    }
  ],
  "policy": {
    "engine": "opa/conftest",
    "rules_evaluated": ["kfm.prov.provenance_first"]
  }
}
```

---

### Example C — WARN for sensitivity review flag ⚠️🏷️

```json
{
  "api_version": "mcp.gates/v1alpha1",
  "kind": "GateReport",
  "metadata": {
    "report_id": "b2f3b2b1-9e6f-4c05-9d4f-53c1f1d92f21",
    "created_at": "2026-01-22T23:15:02Z",
    "producer": { "name": "kfm-ci", "version": "0.8.0" },
    "labels": { "env": "ci", "domain": "governance" }
  },
  "gate": {
    "gate_id": "kfm.sensitivity.review_flag",
    "gate_name": "Sensitive Data Review Gate",
    "gate_version": "0.4.0",
    "gate_type": "policy",
    "scope": "ci"
  },
  "subject": {
    "subject_type": "dataset",
    "subject_id": "kfm:dataset:water_quality_private_wells_v2"
  },
  "decision": {
    "status": "warn",
    "severity": "medium",
    "summary": "Dataset flagged as potentially sensitive; requires reviewer confirmation.",
    "fail_closed": true,
    "recommendation": "Add reviewer approval + classification label before promotion."
  },
  "checks": [
    {
      "check_id": "KFM-SENS-002",
      "title": "Potential sensitive content detected",
      "status": "warn",
      "severity": "medium",
      "message": "Dataset appears to reference private infrastructure; ensure classification and redaction rules are applied.",
      "remediation": {
        "steps": ["Set kfm:classification and add review flag metadata.", "Confirm redaction at API boundary."],
        "owner": "maintainer"
      }
    }
  ]
}
```

---

## 🛠️ Implementation notes (practical)

### Validation
- Gate producers **SHOULD** validate reports against a JSON Schema before publishing.
- Gate consumers **MUST** treat non-conformant reports as `error` (fail-closed).

### Language bindings (recommended)
- **Python**: Pydantic models for GateReport + checks
- **TypeScript**: Zod/Ajv validators
- **Go/Rust**: generated structs from JSON Schema

### Signing (recommended for high-trust paths)
If GateReports are used for:
- automated merges (W-P-E)
- promotions to canonical datasets
- supply chain attestations

…then **sign GateReport digests** and store signature references in `signatures[]`.

---

## 🔁 Extending the contract safely

When adding fields:
- Add them as **optional** first (backward compatible)
- Prefer **new check ids** over redefining semantics
- Bump `api_version` only for breaking changes
- Keep “hot path” fields stable (`decision`, `checks`, `gate`, `subject`)

---

## 🔗 Related concepts (KFM/MCP)

- 🧬 STAC / DCAT / PROV cross-linking (metadata + lineage)
- 🧱 Policy Pack (OPA + Conftest) governance rules
- 🧾 Run Manifest & canonical hashing (idempotency)
- 👁️🧠🛠️ Watcher–Planner–Executor automation
- 🏷️ UI trust badges (e.g., provenance enforced)
- 🔐 SBOM + SLSA + signature/attestation workflows
- 🗺️ 2D/3D mapping assets (MapLibre / Cesium) + validity gates
- 🧪 Simulation promotion (sandbox → reviewed → cataloged)

---

## 🗓️ Changelog

- **v1alpha1** — Initial draft contract envelope for standardizing gate outputs 🧾✅

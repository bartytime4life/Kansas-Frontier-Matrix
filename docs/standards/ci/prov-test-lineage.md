---
title: "🧪 KFM — CI Test Lineage with PROV‑O (per‑job + workflow aggregate)"
path: "docs/standards/ci/prov-test-lineage.md"
version: "v11.2.5"
last_updated: "2025-12-09"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability Engineering Guild · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x CI lineage compatible"

doc_kind: "Standard"
status: "Active / Enforced"
header_profile: "standard"
footer_profile: "standard"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.5/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.5/manifest.zip"
attestation_ref: "../../../releases/v11.2.5/slsa-attestation.json"
signature_ref: "../../../releases/v11.2.5/signature.sig"
telemetry_ref: "../../../releases/v11.2.5/github-infra-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/actions-library-v11.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
---

<div align="center">

# 🧪 **CI Test Lineage with PROV‑O**  
_Per‑job provenance as `prov:Activity` + workflow aggregate for coverage trends_

</div>

## 📘 Overview
We model each **test job** as a `prov:Activity` that **uses** the repository at a specific `commit_sha` and **generates** artifacts (JUnit XML + coverage reports). Each job records:

- ISO‑8601 `startedAtTime` / `endedAtTime`
- Deterministic **run ID** (GitHub Run ID or full Actions URL)
- **Environment** (OS, Python, pytest, plugin versions)
- **Test counts** (passed/failed/xpassed/xfailed/skipped/error)
- **Coverage %** (line/branch) and artifact digests  

We also emit a **workflow aggregate** node for rollups (per‑matrix, per‑workflow) to trend coverage up/down.

## 🗂️ Directory Layout
~~~text
📁 Kansas-Frontier-Matrix/
├── 📁 docs/
│   └── 📁 standards/
│       └── 📁 ci/
│           ├── 📄 prov-test-lineage.md                 # this file
│           └── 📁 examples/
│               ├── 🧾 job-lineage.example.jsonld       # per-job PROV
│               └── 🧾 workflow-aggregate.example.jsonld
├── 📁 .github/
│   └── 📁 workflows/
│       └── 🧾 ci.yml                                   # emits lineage on every run
├── 📁 artifacts/
│   └── 📁 tests/
│       └── 📁 <run-id>/
│           ├── 🧾 junit.xml
│           ├── 🧾 coverage.xml
│           └── 📁 prov/
│               ├── 🧾 job-<job-id>.jsonld
│               └── 🧾 workflow-aggregate.jsonld
└── 📁 schemas/
    └── 📁 prov/
        └── 🧾 ci-test-lineage-v1.json                  # JSON schema for validation
~~~

## 🧪 Validation & CI/CD

### 🧩 JSON‑LD (Per‑Job) — Minimal Example
~~~json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "kfm": "https://kfm.example/ns#",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "@id": "urn:kfm:ci:job:github:<run_id>:<job_id>",
  "@type": "prov:Activity",
  "prov:startedAtTime": {"@type":"xsd:dateTime","@value":"2025-12-09T02:14:05Z"},
  "prov:endedAtTime":   {"@type":"xsd:dateTime","@value":"2025-12-09T02:16:47Z"},
  "kfm:runId": "github_actions_run:<run_id>",
  "kfm:runUrl": "https://github.com/<org>/<repo>/actions/runs/<run_id>",
  "prov:used": [
    {
      "@id": "urn:kfm:repo:<commit_sha>",
      "@type": "prov:Entity",
      "kfm:commitSha": "<commit_sha>",
      "kfm:branch": "main"
    },
    {
      "@id": "urn:kfm:env:python",
      "@type": "prov:Entity",
      "kfm:pythonVersion": "3.11.7",
      "kfm:pytestVersion": "8.3.3",
      "kfm:plugins": ["pytest-cov 5.0.0", "pytest-xdist 3.6.1"]
    }
  ],
  "prov:generated": [
    {
      "@id": "urn:kfm:artifact:junit:<digest>",
      "@type": "prov:Entity",
      "kfm:path": "artifacts/tests/<run-id>/junit.xml",
      "kfm:sha256": "<sha256>"
    },
    {
      "@id": "urn:kfm:artifact:coverage:<digest>",
      "@type": "prov:Entity",
      "kfm:path": "artifacts/tests/<run-id>/coverage.xml",
      "kfm:sha256": "<sha256>"
    }
  ],
  "kfm:testStats": {
    "collected": 1527,
    "passed": 1502,
    "failed": 3,
    "skipped": 18,
    "xfailed": 3,
    "xpassed": 1,
    "errors": 0,
    "durationSec": 161.9
  },
  "kfm:coverage": {
    "line": 92.4,
    "branch": 78.6,
    "measuredBy": "coverage.py 7.6.1"
  },
  "kfm:jobLabels": ["ubuntu-22.04","python-3.11","matrix:fast"]
}
~~~

### 📊 JSON‑LD (Workflow Aggregate) — Minimal Example
~~~json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "kfm": "https://kfm.example/ns#",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "@id": "urn:kfm:ci:workflow:github:<run_id>",
  "@type": "prov:Activity",
  "prov:startedAtTime": {"@type":"xsd:dateTime","@value":"2025-12-09T02:12:40Z"},
  "prov:endedAtTime":   {"@type":"xsd:dateTime","@value":"2025-12-09T02:18:03Z"},
  "kfm:runId": "github_actions_run:<run_id>",
  "kfm:jobs": [
    "urn:kfm:ci:job:github:<run_id>:linux-py311",
    "urn:kfm:ci:job:github:<run_id>:linux-py312",
    "urn:kfm:ci:job:github:<run_id>:windows-py311"
  ],
  "kfm:aggregateCoverage": {
    "lineMean": 92.1,
    "lineMin": 91.7,
    "lineMax": 92.5,
    "branchMean": 78.2
  },
  "kfm:trend": {
    "baselineCommit": "<prev_commit_sha>",
    "deltaLinePct": 0.6,
    "deltaBranchPct": 0.3,
    "direction": "up"
  }
}
~~~

### ⚙️ GitHub Actions Snippet (emits lineage files)
~~~yaml
# .github/workflows/ci.yml (excerpt)
- name: Export PROV lineage (per job)
  if: always()
  run: |
    python - <<'PY'
    import json, os, hashlib, datetime

    run_id = os.getenv("GITHUB_RUN_ID")
    job_id = os.getenv("GITHUB_JOB", "job")
    commit = os.getenv("GITHUB_SHA")

    now = datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
    start = os.getenv("KFM_JOB_START_ISO")

    junit_path = f"artifacts/tests/{run_id}/junit.xml"
    cov_path   = f"artifacts/tests/{run_id}/coverage.xml"

    def digest(p):
        try:
            with open(p, "rb") as f:
                return hashlib.sha256(f.read()).hexdigest()
        except FileNotFoundError:
            return None

    doc = {
      "@context": {
        "prov": "http://www.w3.org/ns/prov#",
        "kfm": "https://kfm.example/ns#",
        "xsd": "http://www.w3.org/2001/XMLSchema#"
      },
      "@id": f"urn:kfm:ci:job:github:{run_id}:{job_id}",
      "@type": "prov:Activity",
      "prov:startedAtTime": {"@type": "xsd:dateTime", "@value": start or now},
      "prov:endedAtTime":   {"@type": "xsd:dateTime", "@value": now},
      "kfm:runId":  f"github_actions_run:{run_id}",
      "kfm:runUrl": f"https://github.com/${{ github.repository }}/actions/runs/{run_id}",
      "prov:used": [
        {
          "@id": f"urn:kfm:repo:{commit}",
          "@type": "prov:Entity",
          "kfm:commitSha": commit
        }
      ],
      "prov:generated": [
        {
          "@id":   f"urn:kfm:artifact:junit:{digest(junit_path)}",
          "@type": "prov:Entity",
          "kfm:path":   junit_path,
          "kfm:sha256": digest(junit_path)
        },
        {
          "@id":   f"urn:kfm:artifact:coverage:{digest(cov_path)}",
          "@type": "prov:Entity",
          "kfm:path":   cov_path,
          "kfm:sha256": digest(cov_path)
        }
      ]
    }

    outdir = f"artifacts/tests/{run_id}/prov"
    os.makedirs(outdir, exist_ok=True)
    with open(f"{outdir}/job-{job_id}.jsonld", "w") as f:
        json.dump(doc, f, indent=2)
    PY
~~~

### ✅ Validation & Governance
- **Schema check**: validate `.jsonld` with `schemas/prov/ci-test-lineage-v1.json`.
- **CI gates**: fail PR if coverage drops more than allowed SLO delta.
- **FAIR+CARE**: no PII; artifacts and telemetry use non‑identifying run IDs.
- **Energy/Carbon**: attach spans to `telemetry_ref` using `energy_schema` / `carbon_schema`.

### 📈 What this answers quickly
- **What changed?** commit SHA + job labels + environment.
- **What did it produce?** JUnit/Coverage artifacts with digests.
- **Is coverage trending up/down?** workflow aggregate with baseline deltas.

---

### ✅ Drop‑in Tasks (backlog‑ready)
1) Add `schemas/prov/ci-test-lineage-v1.json` (draft v1).  
2) Wire per‑job exporter step (above) to all test matrices.  
3) Emit `workflow-aggregate.jsonld` in a final job and push to `artifacts/tests/<run-id>/prov/`.  
4) Add a Grafana/Neo4j facet to visualize coverage trend per path/module.

---

## 🕰️ Version History

| Version     | Date       | Summary                                                                                                  |
|------------:|-----------:|----------------------------------------------------------------------------------------------------------|
| **v11.2.5** | 2025-12-09 | Initial CI test lineage standard using PROV‑O; defines per‑job and workflow JSON‑LD, Actions exporter, and coverage/telemetry integration. |

---

<div align="center">

🧪 **KFM — CI Test Lineage with PROV‑O (per‑job + workflow aggregate)**  
Scientific Insight · Documentation‑First · FAIR+CARE Ethics · Sustainable Intelligence  

[📘 Docs Root](../..) · [📂 Standards Index](../README.md) · [⚖ Governance Charter](../governance/ROOT-GOVERNANCE.md)

</div>

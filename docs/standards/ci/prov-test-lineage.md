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
markdown_protocol_version: "KFM-MDP v11.2.5"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
---

<div align="center">

# 🧪 **CI Test Lineage with PROV‑O**  
`docs/standards/ci/prov-test-lineage.md`

**Purpose**  

Define a governed, PROV‑O–aligned CI lineage profile where each test job is a `prov:Activity` with
environment, test statistics, and coverage, plus a workflow‑level aggregate `prov:Activity` for coverage
trend analysis across KFM releases and matrices.

</div>

---

## 📘 Overview

We model each **test job** as a `prov:Activity` that **uses** the repository at a specific `commit_sha` and  
**generates** artifacts (JUnit XML + coverage reports). Each job records:

- ISO‑8601 `startedAtTime` / `endedAtTime`
- Deterministic **run ID** (GitHub Run ID or full Actions URL)
- **Environment** (OS, Python, pytest, plugin versions)
- **Test counts** (passed/failed/xpassed/xfailed/skipped/error)
- **Coverage %** (line/branch) and artifact digests

We also emit a **workflow aggregate** node for rollups (per‑matrix, per‑workflow) to trend coverage up/down
and to feed the CI → telemetry → Neo4j → API → Story Nodes pipeline.

---

## 🗂️ Directory Layout

This standard touches CI lineage docs under `docs/`, runtime workflows under `.github/`, emitted artifacts,
and validation schemas.

~~~text
📁 Kansas-Frontier-Matrix/
├── 📁 docs/
│   └── 📁 standards/
│       └── 📁 ci/
│           ├── 📄 prov-test-lineage.md              # this standard
│           └── 📁 examples/
│               ├── 🧾 job-lineage.example.jsonld    # per-job PROV-O JSON-LD
│               └── 🧾 workflow-aggregate.example.jsonld
├── 📁 .github/
│   └── 📁 workflows/
│       └── 📄 ci.yml                                # emits lineage on every run
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
        └── 🧾 ci-test-lineage-v1.json               # JSON schema for validation
~~~

---

## 📦 Data & Metadata

This section defines the **per‑job** and **workflow aggregate** PROV‑O JSON‑LD profiles used by CI to emit
machine‑readable test lineage.

### 🧩 Per‑Job JSON‑LD — Minimal Example

~~~json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "kfm": "https://kfm.example/ns#",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "@id": "urn:kfm:ci:job:github:<run_id>:<job_id>",
  "@type": "prov:Activity",
  "prov:startedAtTime": { "@type": "xsd:dateTime", "@value": "2025-12-09T02:14:05Z" },
  "prov:endedAtTime":   { "@type": "xsd:dateTime", "@value": "2025-12-09T02:16:47Z" },
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
  "kfm:jobLabels": ["ubuntu-22.04", "python-3.11", "matrix:fast"]
}
~~~

### 📊 Workflow Aggregate JSON‑LD — Minimal Example

~~~json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "kfm": "https://kfm.example/ns#",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "@id": "urn:kfm:ci:workflow:github:<run_id>",
  "@type": "prov:Activity",
  "prov:startedAtTime": { "@type": "xsd:dateTime", "@value": "2025-12-09T02:12:40Z" },
  "prov:endedAtTime":   { "@type": "xsd:dateTime", "@value": "2025-12-09T02:18:03Z" },
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

---

## 🧪 Validation & CI/CD

This section defines the CI wiring that emits PROV‑O lineage on every run and the governance rules
enforced via CI gates.

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

    def digest(path: str) -> str | None:
        try:
            with open(path, "rb") as f:
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
      "prov:startedAtTime": {
        "@type": "xsd:dateTime",
        "@value": start or now
      },
      "prov:endedAtTime": {
        "@type": "xsd:dateTime",
        "@value": now
      },
      "kfm:runId": f"github_actions_run:{run_id}",
      "kfm:runUrl": "https://github.com/${{ github.repository }}/actions/runs/{run_id}",
      "prov:used": [
        {
          "@id": f"urn:kfm:repo:{commit}",
          "@type": "prov:Entity",
          "kfm:commitSha": commit
        }
      ],
      "prov:generated": [
        {
          "@id": f"urn:kfm:artifact:junit:{digest(junit_path)}",
          "@type": "prov:Entity",
          "kfm:path": junit_path,
          "kfm:sha256": digest(junit_path)
        },
        {
          "@id": f"urn:kfm:artifact:coverage:{digest(cov_path)}",
          "@type": "prov:Entity",
          "kfm:path": cov_path,
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

A final workflow job **SHOULD** emit a corresponding `workflow-aggregate.jsonld` into the same
`artifacts/tests/<run-id>/prov/` directory, using the aggregate profile above.

### ✅ Validation & Governance

- **Schema check**  
  - Validate `.jsonld` files against `schemas/prov/ci-test-lineage-v1.json`.
- **CI gates**  
  - Fail PR if coverage drops more than the allowed SLO delta (per project config).
  - Optionally block merge if PROV lineage files are missing or schema‑invalid.
- **FAIR+CARE**  
  - No PII: artifacts and telemetry use non‑identifying run IDs and job labels.
  - Lineage is limited to repo, environment, and artifacts; no developer or account IDs.
- **Energy/Carbon**  
  - Attach CI spans to `telemetry_ref` using `energy_schema` / `carbon_schema`.
  - Allow correlation of test coverage and energy/carbon cost across releases.

### 📈 What this answers quickly

- **What changed?**  
  - `kfm:commitSha` + `kfm:jobLabels` + environment entities.
- **What did it produce?**  
  - JUnit + coverage artifacts with stable paths and SHA‑256 digests.
- **Is coverage trending up/down?**  
  - Workflow aggregate with coverage stats and deltas vs a `baselineCommit`.

### ✅ Drop‑in Tasks (backlog‑ready)

1. Add `schemas/prov/ci-test-lineage-v1.json` (draft v1) under `schemas/prov/`.  
2. Wire the per‑job exporter step (above) to all test matrices in `.github/workflows/ci.yml`.  
3. Emit `workflow-aggregate.jsonld` in a final job and push to `artifacts/tests/<run-id>/prov/`.  
4. Add a Grafana/Neo4j facet to visualize coverage trend per path/module, driven from the PROV graph.  

---

## 🕰️ Version History

| Version     | Date       | Summary                                                                 |
|------------:|-----------:|-------------------------------------------------------------------------|
| **v11.2.5** | 2025-12-09 | Initial governed CI PROV‑O test lineage standard (per‑job + workflow). |

---

<div align="center">

🧪 **KFM — CI Test Lineage with PROV‑O (per‑job + workflow aggregate)**  
Deterministic CI Lineage · PROV‑O Coverage Telemetry · KFM v11

[📘 Docs Root](../..) · [📂 Standards Index](../README.md) · [⚖ Governance Charter](../governance/ROOT-GOVERNANCE.md)

</div>
